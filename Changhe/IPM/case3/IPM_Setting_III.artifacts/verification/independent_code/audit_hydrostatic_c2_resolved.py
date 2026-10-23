"""Result235: independent c=2 complete hydrostatic inverse and logarithmic constants."""
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
import hydrostatic_axis_log_constant as logaxis
from hydrostatic_cusp_functional import rational_data,factor,monomial_cusp
import torch
from q_local_checkpoint import QLocalCheckpoint
from q_high_precision_density import MPQDensity
from q_mp_primitives import mf,guard_digits
from independent_hydrostatic import CartesianQJet,exact_hydrostatic_center,quadrature_hydrostatic_center,finite_nodes
from hydrostatic_power_tail import PowerVerticalInverse
from hydrostatic_axis_primitive import primitive
from hydrostatic_core_moment import cheb_to_w,guard,logarithm_coefficient,endpoint_second,exactmp
from audit_hydrostatic_states import point_record,sample_summary

ROOT=Path('research/hydrostatic_c2_resolved_audit');V=ROOT/'verification';Q=gmpy2.mpq
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
    files=[Path(__file__),proof]+[Path('independent_code')/p for p in ['q_local_checkpoint.py','q_checkpoint_reader.py','q_high_precision_density.py','q_mp_primitives.py','independent_hydrostatic.py','hydrostatic_power_tail.py','hydrostatic_axis_primitive.py','hydrostatic_core_moment.py','audit_hydrostatic_states.py','hydrostatic_axis_log_constant.py','hydrostatic_axis_tail_series.py','hydrostatic_cusp_functional.py']]
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
          ('research/hydrostatic_axis_core_moment/verification/CHECKS.json','library_sha256','hydrostatic_core_moment.py','DONE'),
          ('research/hydrostatic_axis_log_constant/verification/GATE.json','module_sha256','hydrostatic_axis_log_constant.py','PASS'),
          ('research/hydrostatic_cusp_row_audit/verification/CUSP_GATE.json','module_sha256','hydrostatic_cusp_functional.py','PASS')]:
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
            check('exact logarithmic exponent '+tag,PP==2 and F(q.cl)==2)
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
                    P=exactmp(PP);L=exactmp(LL);C=L/4;p=mp.mpf('.5');c=mf(q.cl)
                    vals=logaxis.constants(C,list(map(exactmp,hw)),list(map(exactmp,kw)))
                    blog=exactmp(logarithm_coefficient(kw,PP,LL))
                    check('independent rational logarithm '+tag+str(extra),abs(vals['B_log']-blog)<mp.mpf('1e-58'))
                    vals.update(p=p,cp_minus1=c*p-1)
                    row['far_field'].append(dict(precision=mp.mp.dps,**{key:mp.nstr(value,65)for key,value in vals.items()}))
            with mp.workdps(90):
                changes={key:float(abs(mp.mpf(row['far_field'][1][key])-mp.mpf(row['far_field'][0][key])))for key in row['far_field'][0]if key!='precision'}
                check('far coefficients precision '+tag,max(changes.values())<1e-50,changes)
            endpoint=[sum((F(float(v))for v in r),F(0))for r in q.coeff]
            check('two exact angular endpoints '+tag,endpoint==[sum(rr,F(0))for rr in coeff])
            cusp=rational_data(F(1,2),endpoint,12)
            check('angular and axis K Q '+tag,cusp['K']==F(hw[1]) and cusp['Q']==F(kw[1])/2)
            row['cusp'] = []
            for digits in [150,210]:
                with mp.workdps(digits):
                    C=exactmp(LL)/4;scale=mp.sqrt(C);K=mf(cusp['K'])*scale
                    Cp=factor(F(1,2))*mf(cusp['Cp_rational'])*scale;direct,mass=monomial_cusp(F(1,2),endpoint);direct*=scale
                    err=abs(Cp-direct)/max(1,abs(Cp));check('separate complete cusp '+tag+str(digits),err<mp.mpf('1e-95'),mp.nstr(err,20))
                    row['cusp'].append(dict(digits=digits,Cp=mp.nstr(Cp,90),Cp_K=mp.nstr(Cp/K,90),monomial_Cp=mp.nstr(direct,90),monomial_error=mp.nstr(err,25)))
            savepipe()
            row['center_finite_polynomial_quadrature']=[dict(order=n,value=quadrature_hydrostatic_center(q,n),error=abs(quadrature_hydrostatic_center(q,n)-float(cH)))for n in [(q.N+2)//2,q.N+3]]
            saverow();savepipe();print(utc(),tag,'EXACT','delta',float(delta),'b',exact['b'][:19],'E',exact['E'][:19],'B_log',row['far_field'][-1]['B_log'][:19],flush=True)
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
            row['axis_log_runs']=[]
            for extra in [80,125]:
                with mp.workdps(G+extra):
                    C=exactmp(LL)/4;k=list(map(exactmp,kw));H=list(map(exactmp,hw));cc=logaxis.constants(C,H,k);I0=logaxis.beta_I0(k)
                    run=dict(working_digits=mp.mp.dps,points=[]);row['axis_log_runs'].append(run)
                    for y in [100,1000,10000,1000000,100000000,10**12,10**20,10**28]:
                        z=logaxis.residual(C,H,k,y,96,I0);zz=logaxis.residual(C,H,k,y,160,I0)
                        err=abs(z['V2']-zz['V2']);check('log axis tail bound '+tag+str(extra)+' y'+str(y),err<=z['remainder_bound']+zz['remainder_bound']+mp.mpf('1e-60'),mp.nstr(err,20))
                        pred=cc['residual_sqrt']*mp.sqrt(y)+cc['residual_log']*mp.log(y)+cc['residual_constant']
                        rec={key:mp.nstr(value,80)for key,value in zz.items()};rec.update(asymptotic_prediction=mp.nstr(pred,80),asymptotic_remainder=mp.nstr(zz['y_signed_R_Nf']-pred,80));run['points'].append(rec)
                saverow();savepipe()
            with mp.workdps(110):
                for aa,bb in zip(row['axis_log_runs'][0]['points'],row['axis_log_runs'][1]['points']):
                    ee=max(abs(mp.mpf(aa[key])-mp.mpf(bb[key]))/max(1,abs(mp.mpf(bb[key])))for key in ['V2','R','Nf','y_signed_R_Nf'])
                    check('log axis precision '+tag+' y'+aa['y'],ee<mp.mpf('1e-65'),mp.nstr(ee,20))
            old=next(z for z in row['levels'][-1]['points']if z['x']==0 and z['y']==10000.)
            new=next(z for z in row['axis_log_runs'][-1]['points']if float(z['y'])==10000.)
            errs={key:abs(float(new[key])-old[key])for key in ['g','gy','V2','R','Nf']}
            row['axis_log_crosscheck']=dict(y=10000,absolute_errors=errs)
            check('log axis separate Cartesian inverse '+tag,errs['V2']<3e-8 and errs['R']<1e-9 and errs['g']<1e-9,errs)
            yy=np.geomspace(1e-7,1e6,2001);ax=jet.jet(0.,yy);xx=jet.jet(yy,0.);sg=np.sign(ax[:,3]);nz=sg[sg!=0]
            row['axis_derivative_samples']=dict(range=[1e-7,1e6],count=len(yy),gxx_min=float(ax[:,3].min()),gxx_max=float(ax[:,3].max()),sign_changes=int(np.sum(nz[1:]!=nz[:-1])),min_gy_xaxis=float(xx[:,2].min()),argmin_gy_xaxis=float(yy[np.argmin(xx[:,2])]))
            row.update(status='DONE',utc_finished=utc(),seconds=time.monotonic()-start);saverow()
            entry.update(status='DONE',utc_finished=utc(),seconds=row['seconds'],result_sha256=sha(outpath));savepipe();print(utc(),tag,'DONE',row['seconds'],flush=True)
        for p,h in pipe['code_and_proof_sha256'].items():check('unchanged code/proof '+p,sha(p)==h)
        pipe.update(status='DONE',utc_finished=utc());savepipe();print(utc(),'ALL DONE',len(pipe['checks']),flush=True)
    except Exception:
        pipe.update(status='FAILED',utc_failed=utc(),error=traceback.format_exc());savepipe();raise

if __name__=='__main__':main()
