"""Independent actual-state finite Jacobians, result201 SPECTRAL_PROOF.md.
Producer files are numeric inputs only. One sequential single-thread process.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time,sys
from fractions import Fraction
import numpy as np
from scipy.linalg import svd
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet,VerticalInverse,exact_hydrostatic_center,validate_inverse_options
from independent_hydrostatic_matrix import HydrostaticBasisMatrices,cheb_jet,residual_and_jacobian

ROOT=Path('verification')
os.chdir(ROOT)
V=Path('research/hydrostatic_jacobian_audit/verification')
SOURCE=Path('research/hydrostatic_exports_report_audit/verification')
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
number=lambda x:float(np.asarray(x))

def norm(x):
    return float(np.linalg.norm(x))

def exact_rational_record(value):
    return dict(encoding="hexadecimal_integers",numerator=hex(value.numerator),denominator=hex(value.denominator))

def bitwise_equal(a,b):
    a,b=np.asarray(a),np.asarray(b)
    return a.dtype==b.dtype and a.shape==b.shape and a.tobytes()==b.tobytes()

def difference(a,b):
    a,b=np.asarray(a),np.asarray(b)
    if a.shape!=b.shape:
        return dict(status='INCOMPARABLE_DIMENSIONS',shape_a=list(a.shape),shape_b=list(b.shape))
    if not a.size:raise ValueError('Cannot compare empty arrays')
    d=a-b;n=norm(b)
    return dict(status='COMPARED',max_absolute=float(np.max(np.abs(d))),frobenius=norm(d),relative_frobenius=norm(d)/n if n else None,reference_norm=n)


def mode_space(model):
    q=model.q;t=q.tk;sig=(1+t)/2;w=(1-t)/2;T=4*sig*w/(w+2*q.kappa*sig)
    blocks=[];dilation=np.zeros(model.nu);details=[];all_defects=[];all_targets=[]
    for k in range(q.M):
        sl=slice(model.offs[k],model.offs[k+1]);n=sl.stop-sl.start
        z=(2*t-1-q.tk[k])/(1-q.tk[k]) if q.basis=='local' else t
        scale=2/(1-q.tk[k]) if q.basis=='local' else 1.
        B,Bt,_=cheb_jet(z,n);Bt*=scale
        A=sig[:,None]**k*B;At=sig[:,None]**k*Bt
        if k:At+=.5*k*sig[:,None]**(k-1)*B
        values=A@q.u[sl];derivative=At@q.u[sl]
        target=-T*(derivative-values/(1-t))
        U,S,H=svd(A,full_matrices=False,lapack_driver='gesvd',check_finite=True)
        keep=S>=1e-8*S[0];Z=H[keep].T
        coeff=Z@((U[:,keep].T@target)/S[keep]);dilation[sl]=coeff
        block=np.zeros((model.nu,Z.shape[1]));block[sl]=Z;blocks.append(block)
        defect=A@coeff-target;all_defects.extend(defect.tolist());all_targets.extend(target.tolist())
        details.append(dict(mode=k,dimension=int(np.sum(keep)),singular_values=S.tolist(),projection_max_error=float(np.max(np.abs(defect))),projection_target_max=float(np.max(np.abs(target)))))
    visible=np.column_stack(blocks)
    return visible,dilation,dict(per_mode=details,visible_dimension=visible.shape[1],orthogonality_error=norm(visible.T@visible-np.eye(visible.shape[1])),dilation_projection_relative_max=float(np.max(np.abs(all_defects)))/float(np.max(np.abs(all_targets))) if np.max(np.abs(all_targets)) else None)

def spectrum(J,F=None,v=None):
    J=np.asarray(J,float)
    if J.ndim!=2 or not 0<J.shape[1]<=J.shape[0] or not np.isfinite(J).all():
        raise ValueError('Spectral diagnostics require a nonempty finite tall matrix')
    U,S,H=svd(J,full_matrices=False,lapack_driver='gesvd',check_finite=True)
    if S[0]==0:raise ValueError('Relative spectral scale is undefined for a zero matrix')
    out=dict(rows=J.shape[0],columns=J.shape[1],smax=float(S[0]),smin=float(S[-1]),relative_smin=float(S[-1]/S[0]),singular_values=S.tolist(),counts={str(c):int(np.sum(S<c*S[0]))for c in [1e-13,1e-8,1e-4]})
    if F is not None:
        F=np.asarray(F,float)
        if F.shape!=(J.shape[0],) or not np.isfinite(F).all():raise ValueError('Invalid residual vector')
        n=norm(F);out['gradient_norm']=norm(J.T@F)
        if n==0:
            out.update(residual_status='ZERO_RESIDUAL',residual_fractions=None,pythagorean_error=None)
        else:
            a=U.T@F;keep=S>=1e-13*S[0];outside=F-U@a
            parts=dict(kept=norm(a[keep])/n,dropped=norm(a[~keep])/n,outside=norm(outside)/n,grad=out['gradient_norm']/(S[0]*n))
            out['residual_status']='NONZERO_RESIDUAL';out['residual_fractions']=parts
            out['pythagorean_error']=abs(sum(parts[k]**2 for k in ('kept','dropped','outside'))-1)
            out['gradient_square_upper_bound']=parts['kept']**2+1e-26*parts['dropped']**2
    if v is not None:
        v=np.asarray(v,float)
        if v.shape!=(J.shape[1],) or not np.isfinite(v).all():raise ValueError('Invalid comparison direction')
        if norm(v)==0:out['dilation']=dict(status='ZERO_DIRECTION',relative_Jv=None,smallest_vector_overlap=None,subspace_overlap=None)
        else:
            vn=v/norm(v);a=H@vn
            out['dilation']=dict(status='NONZERO_DIRECTION',relative_Jv=norm(J@vn)/S[0],smallest_vector_overlap=abs(float(a[-1])),subspace_overlap={str(c):norm(a[S<c*S[0]])for c in [1e-13,1e-8,1e-4]})
    return out


def validate_frozen_inputs(tag):
    ledger=json.loads((SOURCE/'INPUTS.json').read_text())['inputs']
    paths=['spectra/META.json','states/'+tag+'.pt','spectra/'+tag+'.npz']
    for path in paths:
        if sha(SOURCE/path)!=ledger[path]['sha256']:raise ValueError('Frozen input hash changed: '+path)
    return {path:ledger[path]['sha256'] for path in paths}


def run(tag,levels,probe_only):
    if not levels:raise ValueError('At least one quadrature level is required')
    for a,b,c in levels:validate_inverse_options(a,b,c,.125)
    input_hashes=validate_frozen_inputs(tag)
    outdir=V/'states'/tag;outdir.mkdir(parents=True,exist_ok=True)
    meta=json.loads((SOURCE/'spectra/META.json').read_text())['states'][tag]
    pt=SOURCE/'states'/(tag+'.pt');npz=SOURCE/'spectra'/(tag+'.npz')
    assert sha(pt)==meta['state_sha256']
    with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):
        q=QLocalCheckpoint(pt)
    with np.load(npz,allow_pickle=False)as f:d={k:f[k].copy()for k in f.files}
    def raw(key):
        v=q.data[key]
        if hasattr(v,'detach'):v=v.detach().cpu().numpy()
        return np.asarray(v)
    assert bitwise_equal(raw('u').reshape(-1),d['u']) and bitwise_equal(raw('tk'),d['tk'])
    assert bitwise_equal(raw('p'),d['P']) and bitwise_equal(raw('cl'),d['c'])
    assert q.N==meta['N'] and q.M==meta['M'] and len(q.u)==meta['unknowns']
    assert q.kappa==meta['P'] and q.cl==meta['c'] and np.isfinite(q.L) and q.L>0
    assert np.isfinite(q.u).all() and d['X'].shape==d['Y'].shape
    assert d['F'].shape==(meta['rows'],) and meta['rows']==len(d['X'])+(3 if meta['centre']=='keep' else 2)
    assert meta['centre'] in ('keep','drop') and q.basis in ('local','cheb')
    model=HydrostaticBasisMatrices(q);scalar=CartesianQJet(q)
    assert bitwise_equal(model.offs,d['offs'])
    out=dict(started_utc=now(),pid=os.getpid(),tag=tag,status='RUNNING',metadata=meta,input_hashes=input_hashes,gate_sha256=sha(V/'GATE.json'),gate_dependencies=json.loads((V/'GATE.json').read_text())['dependencies'],source_sha256=sha(pt),export_sha256=sha(npz),code_sha256=sha(__file__),matrix_sha256=sha('independent_code/independent_hydrostatic_matrix.py'),proof_sha256=sha(V.parent/'SPECTRAL_PROOF.md'),levels=levels,probes=[],matrices=[],scope='Independent analytic density derivatives and complete hydrostatic inverse. Different finite map from producer FD. All spectra use the saved Euclidean coefficient and row norms.')
    path=outdir/'AUDIT.json'
    def save():
        out['updated_utc']=now();path.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    save();X,Y=d['X'],d['Y'];radius=np.hypot(X,Y)
    indices=sorted(set([0,len(X)//3,len(X)//2,len(X)-1,int(np.argmin(abs(radius-1))),int(np.argmax(np.abs(d['F'][:len(X)])))]))
    points=[(float(X[i]),float(Y[i]))for i in indices]+[(0.,.37),(.137,.219),(6.,8.)]
    previous=None
    for lev in levels:
        a,b,c=lev;values=[];contractions=[];jet_errors=[];scalar_errors=[]
        inverse=VerticalInverse(scalar.jet,q.p,a,b,c,.125)
        for x,y in points:
            B=model.jet(x,y)[0];ref=scalar.jet(x,y);jet_errors.append(difference(B@q.u,ref))
            W=model.velocity(x,y,order=a,tail_order=b,split=c)
            values.append(W);contractions.append(W@q.u);scalar_errors.append(difference(W@q.u,inverse.at(x,y)['V']))
        values=np.asarray(values);contractions=np.asarray(contractions)
        row=dict(level=lev,points=[list(p)for p in points],velocities=contractions.tolist(),max_jet_scaled_error=max(r['relative_frobenius']for r in jet_errors),max_scalar_velocity_absolute_error=max(r['max_absolute']for r in scalar_errors),scalar_errors=scalar_errors)
        if previous is not None:row.update(column_change=difference(values,previous[0]),contracted_change=difference(contractions,previous[1]))
        previous=(values,contractions);out['probes'].append(row);save();print(now(),tag,'PROBE',lev,row.get('contracted_change'),flush=True)
    if probe_only:
        out.update(status='PROBES_DONE',finished_utc=now());save();return
    visible,v,space=mode_space(model);out['mode_space']=space
    out['mode_space']['producer_dimensions']=d['vis_dims_per_mode'].tolist()
    out['mode_space']['dimensions_equal']=space['visible_dimension']==len(d['S_vis']) and [r['dimension']for r in space['per_mode']]==d['vis_dims_per_mode'].tolist()
    C=model.constraint_rows();exact_center=exact_hydrostatic_center(q.exact_coefficients(),Fraction(q.kappa))
    out['center_comparison']=dict(matrix=float(C[2]@q.u),exact_float=float(exact_center),exact_rational=exact_rational_record(exact_center),matrix_minus_exact=float(C[2]@q.u)-float(exact_center),functional='Exact compact polynomial center, distinct from a producer finite-difference center',center_row_included=meta['centre']=='keep')
    out['dilation']=dict(producer_comparison=difference(v,d['dilation_v']),a_row=float(C[0]@v),K_row=float(C[1]@v),C_row=float(C[2]@v),C_exact_generator=0.,center_row_included=meta['centre']=='keep',K_exact_generator=(1-q.p)*float(C[1]@q.u),visible_fraction=norm(visible.T@v)/norm(v) if norm(v) else None,v_norm=norm(v));save()
    np.savez_compressed(outdir/'directions.npz',dilation_v=v,producer_dilation_v=d['dilation_v'],constraints=C)
    previous=None
    for lev in levels:
        a,b,c=lev;started=time.monotonic();row=dict(level=lev,status='BUILDING',started_utc=now());out['matrices'].append(row);save()
        def progress(done,total):
            if done%32==0 or done==total:
                row['progress']=dict(done=done,total=total,elapsed=time.monotonic()-started);save();print(now(),tag,'BUILD',lev,done,'/',total,flush=True)
        m=model.sample_maps(X,Y,progress=progress,order=a,tail_order=b,split=c)
        F,J=residual_and_jacobian(m,q.u,q.cl,meta['centre']=='keep');assert F.shape==d['F'].shape
        jr=J[:len(X)];vf=visible.T@v;row.update(status='SVD',F_norm=norm(F),F_max=float(np.max(np.abs(F))),producer_F_change=difference(F,d['F']),constraints=(C@q.u).tolist(),jet_contraction_change=difference(np.stack([m[k]@q.u for k in ('G','Gx','Gy')],axis=1),scalar.jet(X,Y)[:,:3]));save()
        row['full_with_norm']=spectrum(J,F,v);row['residual_only']=spectrum(jr,v=v);row['visible_residual']=spectrum(jr@visible,v=vf);row['visible_with_norm']=spectrum(J@visible,F,vf)
        row['producer_singular_changes']={k:difference(row[name]['singular_values'],d[k])for k,name in [('S_full','residual_only'),('S_full_with_norm_rows','full_with_norm'),('S_vis','visible_residual')]}
        if previous is not None:
            row['previous_quadrature_change']=dict(F=difference(F,previous[0]),J=difference(J,previous[1]),singular_max_absolute=max(abs(np.asarray(row['full_with_norm']['singular_values'])-previous[2])))
        # Test the actual matrix's exact quadratic remainder in one reproducible direction.
        h=np.random.default_rng(20148).normal(size=len(q.u));h/=norm(h);step=2.**-6
        Fp,_=residual_and_jacobian(m,q.u+step*h,q.cl,meta['centre']=='keep')
        nonlinear=(m['V1']@h)*(m['Gx']@h)+(m['V2']@h)*(m['Gy']@h)
        defect=Fp-F-step*(J@h)-step*step*np.r_[nonlinear,np.zeros(len(F)-len(X))]
        row['quadratic_remainder_error']=dict(max_absolute=float(np.max(np.abs(defect))),scaled=norm(defect)/(1+norm(F)))
        row.update(status='DONE',finished_utc=now(),elapsed_seconds=time.monotonic()-started)
        np.savez_compressed(outdir/f'level_{a}_{b}_{float(c).hex()}.npz',F=F,S_full=row['residual_only']['singular_values'],S_full_with_norm_rows=row['full_with_norm']['singular_values'],S_vis=row['visible_residual']['singular_values'])
        previous=(F,J,np.asarray(row['full_with_norm']['singular_values']));del m,jr;save();print(now(),tag,'DONE MATRIX',lev,'F',row['F_norm'],'count13',row['full_with_norm']['counts']['1e-13'],flush=True)
    out.update(status='DONE',finished_utc=now());save();print(now(),tag,'DONE',flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--tag',default='hsA_c3.0_N48');p.add_argument('--probe-only',action='store_true');p.add_argument('--levels',default='20,112,64;28,192,256;36,320,1024');args=p.parse_args()
    gate=json.loads((V/'GATE.json').read_text());assert gate['status']=='PASS'
    for path,digest in gate['dependencies'].items():
        assert sha(path)==digest, 'Gate dependency changed: '+path
    edge=json.loads((V/'review_repairs/EDGE_CHECKS.json').read_text());assert edge['status']=='PASS'
    assert edge['driver_sha256']==sha(__file__)
    assert json.loads(Path('research/hydrostatic_extended_state_audit/verification/PIPELINE.json').read_text())['status']=='DONE'
    assert json.loads(Path('research/hydrostatic_trace_compatibility_diagnostic/verification/comparison/WINDOWS.json').read_text())['status']=='DONE'
    lev=[(int(a),int(b),float(c))for a,b,c in (s.split(',')for s in args.levels.split(';'))]
    run(args.tag,lev,args.probe_only)
