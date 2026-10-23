"""Result187, independently reconstruct and test numeric hydrostatic states."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import argparse,json,hashlib,time,math,sys
sys.set_int_max_str_digits(0)  # Exact internally computed rational certificates can exceed4300 digits.
import numpy as np
import mpmath as mp
from q_local_checkpoint import QLocalCheckpoint
from q_high_precision_density import MPQDensity
from q_mp_primitives import mf,guard_digits
from independent_hydrostatic import CartesianQJet,VerticalInverse,exact_hydrostatic_center,quadrature_hydrostatic_center,finite_nodes
root=Path('research/hydrostatic_state_audit/verification');root.mkdir(parents=True,exist_ok=True)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()

def point_record(jet,inv,ell,x,y):
    x=float(x);y=float(y);g,gx,gy,gxx=map(float,jet(x,y));vel=inv.at(x,y);v1,v2=vel['V']
    Ax=(ell*x+v1)*gx;Ay=(ell*y+v2)*gy;R=Ax+Ay-g;dil=x*gx+y*gy;adv=v1*gx+v2*gy
    nf=abs(Ax)+abs(Ay)+abs(g);nv=abs(g)+abs(dil)+abs(adv)
    return dict(x=x,y=y,r=math.hypot(x,y),g=g,gx=gx,gy=gy,gxx=gxx,V1=v1,V2=v2,Phi=vel['Phi'],R=R,Nf=nf,Nv=nv,R_Nf=abs(R)/nf if nf else None,R_Nv=abs(R)/nv if nv else None,tail_V=vel['tail_V'])

def sample_summary(rows):
    summaries={}
    for name,lo,hi in [('tiny',0.,.01),('inner',.01,.1),('core',.1,1.),('annulus',1.,100.),('far',100.,1e300),('extent10',0.,10.),('extent100',0.,100.),('extent10000',0.,10000.000001)]:
        sub=[r for r in rows if lo<=r['r']<hi]
        if not sub:continue
        table={'count':len(sub),'undefined_Nf':sum(r['R_Nf'] is None for r in sub),'undefined_Nv':sum(r['R_Nv'] is None for r in sub)}
        for field in ['R','R_Nf','R_Nv']:
            valid=[r for r in sub if r[field] is not None]
            if valid:table[field]=max(valid,key=lambda r:abs(r[field]))
        summaries[name]=table
    return summaries

def state(tag,stage):
    outpath=root/f'{tag}.json';out=json.loads(outpath.read_text())if outpath.exists()else{}
    if stage in ['centers','all']:
        src=Path('../numerics/runs')/(tag+'.pt');dst=root/'states'/src.name
        if not dst.exists():dst.write_bytes(src.read_bytes())
        q=QLocalCheckpoint(dst);coeff=q.exact_coefficients();cH=exact_hydrostatic_center(coeff,F(q.kappa));a=sum(((-1)**j*v for j,v in enumerate(coeff[0])),F(0));d=sum(((-1)**(j+1)*j*j*v for j,v in enumerate(coeff[0])),F(0));b1=sum(((-1)**j*v for j,v in enumerate(coeff[1])),F(0))if q.M>1 else F(0)
        with mp.workdps(100):
            sc=mp.power(2,2*mf(q.kappa))/mf(q.L)**2;b=mf(2*d-a+b1)*sc;e=mf(2*d-a-b1)*sc;K=mf(sum(((-1)**k*sum(row) for k,row in enumerate(coeff)),F(0)))/2*mf(q.L)**(1/mf(q.kappa));p=1-1/mf(q.kappa);taildef=mf(q.cl)*p-1
            exact=dict(a=str(a),a_float=float(a),cH=str(cH),cH_float=float(cH),delta=str(F(q.cl)+cH-1),delta_float=float(F(q.cl)+cH-1),b=mp.nstr(b,90),e=mp.nstr(e,90),E=mp.nstr(e/mf(a),90),cubic_b_minus_6E=mp.nstr(b-6*e/mf(a),90),K=mp.nstr(K,90),p=mp.nstr(p,90),tail_defect=mp.nstr(taildef,90),lim_axis_R_Nf=mp.nstr(abs(taildef)/(abs(mf(q.cl)*p)+1),90),lim_axis_R_Nv=mp.nstr(abs(taildef)/(p+1),90))
        out=dict(tag=tag,started_utc=now(),status='CENTERS_DONE',source=str(src.resolve()),source_sha256=sha(dst),source_unchanged_at_copy=(sha(src)==sha(dst)),metadata=q.meta,node_reconstruction=q.node_reconstruction_details(),exact=exact,producer_result=q.data.get('result'),code_sha256=sha(__file__),evaluator_sha256=sha('independent_code/independent_hydrostatic.py'),proof_sha256=sha(root.parent/'PROOF.md'))
        out['center_GL']=[dict(order=n,value=quadrature_hydrostatic_center(q,n),error_from_exact=abs(quadrature_hydrostatic_center(q,n)-float(cH))) for n in [(q.N+2)//2,q.N+3]]
        outpath.write_text(json.dumps(out,indent=2)+'\n');print(now(),tag,'center',exact['delta_float'],'b',float(b),'E',float(e/mf(a)),flush=True)
        if stage=='centers':return
    q=QLocalCheckpoint(root/'states'/(tag+'.pt'));coeff=q.exact_coefficients();jet=CartesianQJet(q);ell=q.cl
    out['status']='RUNNING';out['quad_started_utc']=now();outpath.write_text(json.dumps(out,indent=2)+'\n')
    inv=VerticalInverse(jet.jet,q.p,order=20,tail_order=112,tail_scale=64.,inner_scale=.125)
    # Fixed independent physical samples. Axis points are exactly axis points.
    radii=np.unique(np.r_[np.geomspace(1e-5,.01,9),np.geomspace(.013,.099,8),np.geomspace(.113,.987,10),np.geomspace(1.13,98.7,14),np.geomspace(113.,10000.,10)])
    th=np.r_[0.,.00037,(np.arange(11)+.271)/11*np.pi/2,np.pi/2-.00043,np.pi/2]
    points=[]
    for r in radii:
        for t in th:
            if t==0:points.append((float(r),0.))
            elif t==np.pi/2:points.append((0.,float(r)))
            else:points.append((float(r*np.cos(t)),float(r*np.sin(t))))
    points.extend([(.137,.219),(.5,.5),(3.,0.),(0.,3.),(6.,8.),(30.,40.),(-.137,.219),(.137,-.219),(-.137,-.219)])
    rows=[];t0=time.monotonic()
    for j,(x,y)in enumerate(points):
        rows.append(point_record(jet.jet,inv,ell,x,y))
        if j%100==0:
            out['progress']=dict(done=j+1,total=len(points),elapsed_seconds=time.monotonic()-t0);out['samples']=rows;outpath.write_text(json.dumps(out,indent=2)+'\n');print(now(),tag,j+1,'/',len(points),flush=True)
    out['samples']=rows;out['regions']=sample_summary(rows)
    # Re-evaluate distinct maximizing points, ordinary probes and the exact center at three full-tail settings.
    chosen={(0.,0.),(.137,.219),(.5,.5),(0.,3.),(6.,8.),(30.,40.)}
    for table in out['regions'].values():
        for field in ['R','R_Nf','R_Nv']:
            if field in table:chosen.add((table[field]['x'],table[field]['y']))
    comparisons=[]
    for order,ntail,scale in [(14,64,16.),(20,112,64.),(28,192,256.)]:
        ii=VerticalInverse(jet.jet,q.p,order,ntail,scale,.125)
        cr=ii.center();block=dict(order=order,tail_order=ntail,split_scale=scale,center=cr,center_error=abs(cr-out['exact']['cH_float']),points=[])
        for x,y in sorted(chosen):block['points'].append(point_record(jet.jet,ii,ell,x,y))
        block['finite_R_identity']=[]
        for R in [1.,10.,100.,1000.]:
            ts,ws=finite_nodes(0.,R,order,.125);I=float(np.dot(ws*(1-ts/R),jet.jet(0.,ts)[:,3]));vr=ell*R+ii.at(0.,R)['V'][1];dd=I-(1-vr/R)
            block['finite_R_identity'].append(dict(R=R,defect=dd,error_from_exact=abs(dd-out['exact']['delta_float'])))
        comparisons.append(block);out['quadrature_comparisons']=comparisons;outpath.write_text(json.dumps(out,indent=2)+'\n');print(now(),tag,'quad',order,'centererr',block['center_error'],flush=True)
    # Scalar high precision density differentiation does not use analytic CartesianQJet.
    selected=[(.137,.219),(0.,.37),(.0113,.0187),(6.,8.)]
    peak=out['regions']['core']['R_Nf'];selected.append((peak['x'],peak['y']))
    out['mp_jet_checks']=[]
    for digits in [70,100]:
        with mp.workdps(digits+guard_digits(q.N,q.M,q.kappa)):
            mm=MPQDensity.__new__(MPQDensity);mm.coeff=[[mf(v)for v in row]for row in coeff];mm.L=mf(q.L);mm.kappa=mf(q.kappa);mm.ell=mf(q.cl)
            def rho(x,y):
                r=mp.sqrt(x*x+y*y)
                return r*mm.at(r,mp.atan2(y,x))[0] if r else mp.mpf(0)
            for x,y in selected:
                X,Y=mf(x),mf(y);vv=[rho(X,Y),mp.diff(lambda z:rho(z,Y),X),mp.diff(lambda z:rho(X,z),Y),mp.diff(lambda z:rho(z,Y),X,2)];ref=jet.jet(x,y)
                out['mp_jet_checks'].append(dict(target_digits=digits,working_digits=mp.mp.dps,point=[x,y],values=[mp.nstr(z,digits)for z in vv],absolute_double_errors=[float(abs(mf(z)-w))for z,w in zip(ref,vv)]))
        outpath.write_text(json.dumps(out,indent=2)+'\n');print(now(),tag,'MP',digits,'done',flush=True)
    # Dense local-axis derivative sign samples cost only density evaluations.
    yy=np.geomspace(1e-7,1e6,2001);ax=jet.jet(0.,yy);xx=jet.jet(yy,0.);sg=np.sign(ax[:,3]);nz=sg[sg!=0]
    out['axis_derivative_samples']=dict(range=[1e-7,1e6],count=len(yy),gxx_min=float(ax[:,3].min()),gxx_max=float(ax[:,3].max()),sign_changes=int(np.sum(nz[1:]!=nz[:-1])),min_gy_xaxis=float(xx[:,2].min()),argmin_gy_xaxis=float(yy[np.argmin(xx[:,2])]))
    out.update(status='DONE',finished_utc=now(),quad_elapsed_seconds=time.monotonic()-t0);outpath.write_text(json.dumps(out,indent=2)+'\n');print(now(),tag,'DONE',flush=True)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--tags',required=True);ap.add_argument('--stage',choices=['centers','quadrature','all'],default='all');args=ap.parse_args()
    gate=json.loads(Path('research/independent_hydrostatic_evaluator/verification/GATE.json').read_text());assert gate['status']=='PASS';assert gate['evaluator_sha256']==sha('independent_code/independent_hydrostatic.py')
    for tag in args.tags.split(','):state(tag,args.stage)
if __name__=='__main__':main()
