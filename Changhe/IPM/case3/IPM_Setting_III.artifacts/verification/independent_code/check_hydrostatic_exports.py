"""Result200: own numeric-only export checks, no producer imports or J rebuild."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,time
import numpy as np
from q_local_checkpoint import QLocalCheckpoint
import torch
def read_state(path):
    # Pickle GLOBAL metadata inspected: only numeric ndarray reconstruction added.
    with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):
        return QLocalCheckpoint(path)
start=time.monotonic()
r=Path('research/hydrostatic_exports_report_audit/verification')
old=Path('research/hydrostatic_state_audit/verification/states')
checks=[]
def check(name,condition,detail=None):
    checks.append(dict(name=name,pass_=bool(condition),detail=detail))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bits(a,b):
    return a.dtype==b.dtype and a.shape==b.shape and a.tobytes()==b.tobytes()
inputs=json.loads((r/'INPUTS.json').read_text())
for name,rec in inputs['inputs'].items():
    p=r/name;check('input hash '+name,sha(p)==rec['sha256'])
ss={};state_rows=[]
for path in sorted((r/'states').glob('*.pt')):
    tag=path.stem;q=read_state(path);ss[tag]=q
    io=q.data.get('inverse_options',{})
    check(tag+' explicit map/nodes/inverse',all(k in q.data for k in ('tk','basis_nodes','inverse_options','map_exponent_P')))
    check(tag+' binary map parameter',float(q.data['map_exponent_P'])==q.kappa)
    check(tag+' valid coefficient dimensions',q.u.size==sum(q.N+1-k for k in range(q.M)))
    scalar={k:getattr(q,k) for k in ['N','M','basis','L','kappa','cl']}
    row=dict(tag=tag,sha256=sha(path),parameters=scalar,inverse_options=io,old_identity=None)
    if (old/path.name).exists():
        a=read_state(old/path.name)
        same={k:getattr(a,k)==getattr(q,k) for k in scalar}
        same.update(u_bit_equal=bits(a.u,q.u),tk_bit_equal=bits(a.tk,q.tk))
        check(tag+' previous independently checked formula identity',all(same.values()),same)
        row['old_identity']=same
    else:row['scope']='Numeric formula frozen; independent residual and exact center still pending.'
    state_rows.append(row)
check('28 states frozen',len(ss)==28)
check('21 previously evaluated formulas',sum(x['old_identity'] is not None for x in state_rows)==21)
meta=json.loads((r/'spectra/META.json').read_text())
spectral=[]
for tag,m in meta['states'].items():
    q=ss[tag];p=r/'spectra'/(tag+'.npz')
    with np.load(p,allow_pickle=False)as z:data={k:z[k]for k in z.files}
    F=data['F'];nr=len(data['X']);extra=3 if m['centre']=='keep'else 2
    check(tag+' export state SHA',m['state_sha256']==sha(r/'states'/(tag+'.pt')))
    check(tag+' u and tk bit identity',bits(data['u'],q.u) and bits(data['tk'],q.tk))
    check(tag+' finite exported arrays',all(np.isfinite(a).all()for a in data.values()))
    check(tag+' dimensions',F.shape==(m['rows'],) and nr==len(data['Y']) and nr+extra==len(F) and q.u.size==m['unknowns'] and q.N==m['N'] and q.M==m['M'])
    check(tag+' binary scalar identity',float(data['P'])==q.kappa==m['P'] and float(data['c'])==float(q.data['c'])==m['c'] and float(data['c_map'])==q.kappa/(q.kappa-1)==m['c_map'])
    check(tag+' offsets',np.array_equal(data['offs'],np.r_[0,np.cumsum([q.N+1-k for k in range(q.M)])]))
    check(tag+' visible dimensions',data['vis_dims_per_mode'].shape==(q.M,) and int(sum(data['vis_dims_per_mode']))==len(data['S_vis']) and all(0<int(n)<=q.N+1-k for k,n in enumerate(data['vis_dims_per_mode'])))
    spectra={}
    for key in ('S_full','S_full_with_norm_rows','S_vis'):
        a=data[key];check(tag+' positive decreasing '+key,np.all(a>=0) and np.all(np.diff(a)<=0) and a[0]>0)
        spectra[key]={'size':len(a),'max':float(a[0]),'min':float(a[-1]),'below':{str(t):int(np.sum(a<t*a[0]))for t in (1e-13,1e-8,1e-4)}}
    check(tag+' threshold counts',spectra['S_full']['below']['1e-13']==m['n_full_below_1em13'] and spectra['S_vis']['below']['1e-13']==m['n_vis_below_1em13'] and spectra['S_vis']['below']['1e-08']==m['n_vis_below_1em8'])
    norm=float(np.linalg.norm(F));mx=float(np.max(np.abs(F)))
    check(tag+' exported residual norm/max',abs(norm-m['F_norm'])<=1e-13*norm and mx==m['F_max'])
    fr=m['residual_fractions'];err=abs(sum(fr[k]**2 for k in ('kept','dropped','outside'))-1)
    tol=10*max(m['rows'],m['unknowns'])*np.finfo(float).eps
    check(tag+' projection Pythagoras diagnostic',err<tol,dict(error=err,tolerance=tol,scope='Dimension-scaled export diagnostic, not a rigorous SVD error bound.'))
    check(tag+' normalized gradient bounds',0<=fr['grad']<=1 and fr['grad']<=np.hypot(fr['kept'],1e-13*fr['dropped'])+1e-13)
    spectral.append(dict(tag=tag,npz_sha256=sha(p),spectra=spectra,visible_dim=len(data['S_vis']),F_norm=norm,F_max=mx,rows=nr,extra_rows=F[-extra:].tolist(),x_axis_exact_zero_count=int(np.sum(data['X']==0)),y_axis_exact_zero_count=int(np.sum(data['Y']==0)),fractions=fr,projection_identity_error=err,scope='Export consistency only. Independent J/SVD and projection recomputation pending.'))
check('14 spectral exports',len(spectral)==14)
# Previously derived exact center values, never recomputed using the producer primitive.
prior=json.loads(Path('research/hydrostatic_state_audit/verification/ALL21_SUMMARY.json').read_text())
prior={d['tag']:d for d in prior['states']}
axis=[]
for line in (r/'axis_exact.txt').read_text().splitlines():
    match=re.match(r'(\S+)\s+.*D_exact\s+([+\-0-9.eE]+)',line)
    if not match or match[1]not in prior:continue
    tag=match[1];producer=float(match[2]);own=prior[tag]['exact']['delta_float']
    axis.append(dict(tag=tag,producer_printed=producer,own_exact_to_float=own,producer_minus_own=producer-own,scope='Comparison limited by producer log printing; own center evaluated exactly in result187.'))
headline=[]
for N in (48,64,96,128):
    tag=f'hsA_c3.0_N{N}';p=prior[tag];m=meta['states'][tag]
    headline.append(dict(tag=tag,a=p['exact']['a_float'],center=p['exact']['delta_float'],B=float(p['exact']['b']),E=float(p['exact']['E']),annulus_Nf=p['regions']['annulus']['R_Nf']['R_Nf'],far_Nf=p['regions']['far']['R_Nf']['R_Nf'],node_exported_max=m['F_max']))
# Printed ranges are cross-checked with explicitly stated rounding, not exact equalities.
ann=[.00946,.00949,.00189,.00333];far=[.00652,.0125,.00111,.00438]
check('draft independent annular maxima rounded',all(abs(d['annulus_Nf']-v)<=.005*v for d,v in zip(headline,ann)))
check('draft independent far maxima rounded',all(abs(d['far_Nf']-v)<=.005*v for d,v in zip(headline,far)))
check('draft B,E rounded',all(abs(d['B']-b)<.01 and abs(d['E']-e)<.01 for d,b,e in zip(headline,[-.55,-7.35,-4.86,-6.45],[-2.15,1.63,-.41,-.99])))
check('draft four full/visible dimensions',all(d['spectra']['S_full']['below']['1e-13']==n and d['visible_dim']==v and d['spectra']['S_vis']['below']['1e-08']==n8 and d['spectra']['S_vis']['below']['0.0001']==n4 for d,n,v,n8,n4 in zip([next(s for s in spectral if s['tag']==f'hsA_c3.0_N{N}')for N in (48,64,96,128)],[1,27,247,679],[504,823,1644,2658],[30,49,118,212],[138,243,550,954])))
check('draft kept-state center differences rounding',all(abs(next(d for d in axis if d['tag']==tag)['producer_minus_own'])<=bound for tag,bound in [('hsD_c3.0_N64_keep',8.6e-13),('hsD_c3.0_N96_keep',7.1e-13),('hsD_c3.0_N64_keep_cfree',7.6e-13),('hsD_c3.0_N64_keep_fine',9.6e-10)]))
out=dict(utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-start,code_sha256=sha(Path(__file__)),checks=checks,pass_count=sum(c['pass_']for c in checks),fail_count=sum(not c['pass_']for c in checks),states=state_rows,spectral=spectral,axis_comparisons=axis,headline=headline,scope='Static independent numerical export and previous-result comparison. Seven new fields and all Jacobian spectra/projections still need independent recomputation.')
(r/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['utc'],'PASS',out['pass_count'],'FAIL',out['fail_count'],'seconds',out['seconds'])
for c in checks:
    if not c['pass_']:print('FAIL',c)
print('Headline',json.dumps(headline))
print('Axis center comparison',json.dumps([x for x in axis if x['tag'].startswith(('hsA_c3','hsD_'))]))
if out['fail_count']:raise SystemExit(1)
