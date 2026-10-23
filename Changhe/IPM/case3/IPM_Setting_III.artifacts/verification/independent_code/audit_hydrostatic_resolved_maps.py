"""Result227: independent full-plane hydrostatic audit of numeric hsG checkpoints."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import sys,json,hashlib,time,traceback,math
sys.set_int_max_str_digits(0)
import numpy as np
import mpmath as mp
import gmpy2
import torch
from q_local_checkpoint import QLocalCheckpoint
from q_high_precision_density import MPQDensity
from q_mp_primitives import mf,guard_digits
from independent_hydrostatic import CartesianQJet,exact_hydrostatic_center,quadrature_hydrostatic_center,finite_nodes
from hydrostatic_power_tail import PowerVerticalInverse
from hydrostatic_axis_primitive import primitive
from hydrostatic_core_moment import cheb_to_w,guard,beta_moment,integral_moment,endpoint_second,exactmp
from audit_hydrostatic_states import point_record,sample_summary

ROOT=Path('research/hydrostatic_resolved_map_audit');V=ROOT/'verification';Q=gmpy2.mpq
utc=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(p,obj):Path(p).write_text(json.dumps(obj,indent=2)+'\n')
def briefpoints():
    radii=np.unique(np.r_[np.geomspace(1e-5,.01,9),np.geomspace(.013,.099,8),np.geomspace(.113,.987,10),np.geomspace(1.13,98.7,14),np.geomspace(113.,10000.,10)])
    angles=np.r_[0.,.00037,(np.arange(11)+.271)/11*np.pi/2,np.pi/2-.00043,np.pi/2]
    points=[]
    for r in radii:
        for t in angles:
            if t==0:points.append((float(r),0.))
            elif t==np.pi/2:points.append((0.,float(r)))
            else:points.append((float(r*np.cos(t)),float(r*np.sin(t))))
    points.extend([(.137,.219),(.5,.5),(3.,0.),(0.,3.),(6.,8.),(30.,40.),(-.137,.219),(.137,-.219),(-.137,-.219)])
    assert len(points)==774
    return points

def compare(first,second):
    assert len(first)==len(second)
    out={}
    for key in ['V1','V2','R','R_Nf','R_Nv']:
        rows=[]
        for a,b in zip(first,second):
            assert (a['x'],a['y'])==(b['x'],b['y'])
            if a[key] is not None and b[key] is not None:
                rows.append(dict(x=a['x'],y=a['y'],change=b[key]-a[key],before=a[key],after=b[key]))
        out[key]=max(rows,key=lambda t:abs(t['change'])) if rows else None
    return out

def main():
    inputs=json.loads((V/'INPUTS.json').read_text());proof=ROOT/'PROOF.md'
    files=[Path(__file__),proof]+[Path('independent_code')/p for p in ['q_local_checkpoint.py','q_checkpoint_reader.py','q_high_precision_density.py','q_mp_primitives.py','independent_hydrostatic.py','hydrostatic_power_tail.py','hydrostatic_axis_primitive.py','hydrostatic_core_moment.py','audit_hydrostatic_states.py']]
    pipe=dict(status='RUNNING',utc_started=utc(),pid=os.getpid(),input_sha256=sha(V/'INPUTS.json'),code_and_proof_sha256={str(p):sha(p)for p in files},checks=[],states=[])
    def savepipe():pipe['utc_updated']=utc();write(V/'PIPELINE.json',pipe)
    def check(name,ok,evidence=None):
        pipe['checks'].append(dict(name=name,passed=bool(ok),evidence=evidence))
        if not ok:raise AssertionError(name)
    savepipe()
    try:
        for path,field,code,status in [
          ('research/hydrostatic_power_tail_inverse/parent_regression/verification/GATE.json','evaluator_sha256','independent_hydrostatic.py','PASS'),
          ('research/hydrostatic_power_tail_inverse/verification/GATE.json','module_sha256','hydrostatic_power_tail.py','PASS'),
          ('research/hydrostatic_axis_core_moment/verification/CHECKS.json','library_sha256','hydrostatic_core_moment.py','DONE')]:
            gate=json.loads(Path(path).read_text());check('parent gate '+code,gate['status']==status and gate[field]==sha(Path('independent_code')/code),dict(path=path,sha256=sha(path)))
        points=briefpoints();write(V/'POINTS.json',dict(points=points,number=len(points),extents=[10,100,10000]))
        for item in inputs['states']:
            tag=item['tag'];start=time.monotonic();entry=dict(tag=tag,status='RUNNING',utc_started=utc());pipe['states'].append(entry);savepipe()
            check('frozen numeric source '+tag,sha(item['frozen'])==item['sha256'])
            with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(item['frozen'])
            coeff=q.exact_coefficients();polys=primitive(coeff,q.kappa);cH=exact_hydrostatic_center(coeff,F(q.kappa));check('two exact center formulas '+tag,Q(cH.numerator,cH.denominator)==polys['cH'])
            a=sum(((-1)**j*v for j,v in enumerate(coeff[0])),F(0));d=sum(((-1)**(j+1)*j*j*v for j,v in enumerate(coeff[0])),F(0));b1=sum(((-1)**j*v for j,v in enumerate(coeff[1])),F(0))if q.M>1 else F(0)
            delta=F(q.cl)+cH-1
            exact=dict(a=str(a),a_float=float(a),cH=str(cH),cH_float=float(cH),delta=str(delta),delta_float=float(delta))
            with mp.workdps(100):
                scale=mp.power(2,2*mf(q.kappa))/mf(q.L)**2;b=mf(2*d-a+b1)*scale;e=mf(2*d-a-b1)*scale
                for key,value in [('b',b),('e',e),('E',e/mf(a)),('cubic_b_minus_6E',b-6*e/mf(a)),('cubic_axis_residual',e*(2+3*mf(delta))-mf(a)*b/3)]:exact[key]=mp.nstr(value,85)
            kw=cheb_to_w(polys['K']);hw=cheb_to_w(polys['H']);PP=Q(q.kappa);LL=Q(q.L)
            check('finite core exponent range '+tag,1<PP<2)
            check('two exact zero far endpoints '+tag,kw[0]==0 and hw[0]==0)
            kt,ktt=endpoint_second(polys['K']);ht,htt=endpoint_second(polys['H'])
            check('two independent k coefficients '+tag,kw[1]==-2*kt and kw[2]==2*ktt)
            check('two independent H coefficients '+tag,hw[1]==-2*ht and hw[2]==2*htt)
            cert={key:[[str(t.numerator),str(t.denominator)]for t in val]for key,val in [('k_w',kw),('H_w',hw)]}
            cert.update(P=[str(PP.numerator),str(PP.denominator)],L=[str(LL.numerator),str(LL.denominator)])
            certfile=V/(tag+'.polynomials.json');write(certfile,cert)
            row=dict(tag=tag,status='RUNNING',utc_started=utc(),source_sha256=item['sha256'],metadata=q.meta,node_reconstruction=q.node_reconstruction_details(),exact=exact,polynomial_sha256=sha(certfile),far_field=[],levels=[],comparisons=[])
            outpath=V/(tag+'.json')
            def saverow():row['utc_updated']=utc();write(outpath,row)
            G=guard(kw+hw)
            for extra in [65,105]:
                with mp.workdps(G+extra):
                    P=exactmp(PP);L=exactmp(LL);p=1-1/P;C=L/2**P;c=mf(q.cl);K=exactmp(hw[1])*C**(1/P);Qfar=exactmp(kw[1])*C**(1/P)/P;c2=C**(2/P)*(exactmp(hw[2])-exactmp(hw[1])/(2*P));r2=(c*(2*p-1)-1)*c2+K*Qfar/(1-p)
                    moment,mass=beta_moment(kw,PP,LL)
                    vals=dict(precision=mp.mp.dps,absolute_sum=mp.nstr(mass,15))
                    for key,value in [('p',p),('cp_minus1',c*p-1),('K',K),('Q',Qfar),('c2',c2),('r2',r2),('m0',moment)]:vals[key]=mp.nstr(value,65)
                    row['far_field'].append(vals)
            with mp.workdps(90):
                changes={key:float(abs(mp.mpf(row['far_field'][1][key])-mp.mpf(row['far_field'][0][key])))for key in ['p','cp_minus1','K','Q','c2','r2','m0']}
                check('far coefficients precision '+tag,max(changes.values())<1e-50,changes)
            if tag=='hsG_c3.0_N96_fine_log':
                with mp.workdps(G+65):
                    integral=integral_moment(kw,PP,LL);closed,_=beta_moment(kw,PP,LL);error=abs(integral-closed)
                    row['convergent_moment_integral']=dict(value=mp.nstr(integral,55),difference=mp.nstr(error,15),working_digits=mp.mp.dps)
                    check('finite integral vs beta state '+tag,error<mp.mpf('1e-45'),mp.nstr(error,15))
            row['center_finite_polynomial_quadrature']=[dict(order=n,value=quadrature_hydrostatic_center(q,n),error=abs(quadrature_hydrostatic_center(q,n)-float(cH)))for n in [(q.N+2)//2,q.N+3]]
            saverow();savepipe();print(utc(),tag,'EXACT','delta',float(delta),'b',exact['b'][:19],'E',exact['E'][:19],'m0',row['far_field'][-1]['m0'][:19],flush=True)
            jet=CartesianQJet(q);chosen={(0.,0.),(.137,.219),(.5,.5),(0.,3.),(6.,8.),(30.,40.)};previous=None
            for order,tail,split in [(32,96,16.),(48,160,64.),(64,192,128.)]:
                inv=PowerVerticalInverse(jet.jet,q.p,order,tail,split,.125);lev=dict(order=order,tail_order=tail,split=split,inner_scale=.125,center=inv.center(),points=[])
                lev['center_error']=abs(lev['center']-float(cH));row['levels'].append(lev)
                for i,(x,y) in enumerate(points):
                    lev['points'].append(point_record(jet.jet,inv,q.cl,x,y))
                    if i%100==0:saverow();print(utc(),tag,order,i+1,'/774',flush=True)
                lev['regions']=sample_summary(lev['points'])
                for table in lev['regions'].values():
                    for key in ['R','R_Nf','R_Nv']:
                        if key in table:chosen.add((table[key]['x'],table[key]['y']))
                if previous is not None:row['comparisons'].append(dict(from_order=previous['order'],to_order=order,pointwise_maximum_changes=compare(previous['points'],lev['points'])))
                previous=lev;saverow();print(utc(),tag,'LEVEL',order,'center error',lev['center_error'],flush=True)
            inv=PowerVerticalInverse(jet.jet,q.p,88,256,512.,.125)
            witness=dict(order=88,tail_order=256,split=512.,inner_scale=.125,center=inv.center(),points=[])
            witness['center_error']=abs(witness['center']-float(cH))
            for x,y in sorted(chosen):witness['points'].append(point_record(jet.jet,inv,q.cl,x,y))
            row['witnesses']=witness
            physical=[(p['x'],p['y'])for p in witness['points']];fine_lookup={(p['x'],p['y']):p for p in row['levels'][-1]['points']};shared=[p for p in witness['points']if(p['x'],p['y'])in fine_lookup]
            row['witness_refinement']=compare([fine_lookup[(p['x'],p['y'])]for p in shared],shared)
            row['finite_radius_identity']=[]
            for R in [1.,10.,100.,1000.]:
                ts,weights=finite_nodes(0.,R,64,.125);I=float(np.dot(weights*(1-ts/R),jet.jet(0.,ts)[:,3]));vR=q.cl*R+inv.at(0.,R)['V'][1];defect=I-(1-vR/R)
                row['finite_radius_identity'].append(dict(R=R,defect=defect,error_from_exact=abs(defect-float(delta))))
            selected=[(.137,.219),(0.,.37),(.0113,.0187),(6.,8.)];peak=row['levels'][-1]['regions']['core']['R_Nf'];selected.append((peak['x'],peak['y']))
            row['mp_jet_checks']=[];saverow()
            for digits in [70,100]:
                with mp.workdps(digits+guard_digits(q.N,q.M,q.kappa)):
                    mm=MPQDensity.__new__(MPQDensity);mm.coeff=[[mf(v)for v in rr]for rr in coeff];mm.L=mf(q.L);mm.kappa=mf(q.kappa);mm.ell=mf(q.cl)
                    def rho(x,y):
                        rr=mp.sqrt(x*x+y*y)
                        return rr*mm.at(rr,mp.atan2(y,x))[0] if rr else mp.mpf(0)
                    for x,y in selected:
                        X,Y=mf(x),mf(y);values=[rho(X,Y),mp.diff(lambda z:rho(z,Y),X),mp.diff(lambda z:rho(X,z),Y),mp.diff(lambda z:rho(z,Y),X,2)];ref=jet.jet(x,y)
                        row['mp_jet_checks'].append(dict(target_digits=digits,working_digits=mp.mp.dps,point=[x,y],values=[mp.nstr(z,digits)for z in values],absolute_double_errors=[float(abs(mf(z)-w))for z,w in zip(ref,values)]))
                saverow();print(utc(),tag,'MP',digits,'done',flush=True)
            yy=np.geomspace(1e-7,1e6,2001);ax=jet.jet(0.,yy);xx=jet.jet(yy,0.);sg=np.sign(ax[:,3]);nz=sg[sg!=0]
            row['axis_derivative_samples']=dict(range=[1e-7,1e6],count=len(yy),gxx_min=float(ax[:,3].min()),gxx_max=float(ax[:,3].max()),sign_changes=int(np.sum(nz[1:]!=nz[:-1])),min_gy_xaxis=float(xx[:,2].min()),argmin_gy_xaxis=float(yy[np.argmin(xx[:,2])]))
            row.update(status='DONE',utc_finished=utc(),seconds=time.monotonic()-start);saverow()
            entry.update(status='DONE',utc_finished=utc(),seconds=row['seconds'],result_sha256=sha(outpath));savepipe();print(utc(),tag,'DONE',row['seconds'],flush=True)
        for p,h in pipe['code_and_proof_sha256'].items():check('unchanged code/proof '+p,sha(p)==h)
        pipe.update(status='DONE',utc_finished=utc());savepipe();print(utc(),'ALL DONE',len(pipe['checks']),flush=True)
    except Exception:
        pipe.update(status='FAILED',utc_failed=utc(),error=traceback.format_exc());savepipe();raise

if __name__=='__main__':main()
