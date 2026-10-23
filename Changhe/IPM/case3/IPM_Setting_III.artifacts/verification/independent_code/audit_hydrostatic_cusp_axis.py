"""Result229: exact complete cusp and separately integrated far-axis checks.
Derivations preceded implementation in PROOF, REVIEW_ADDENDUM, AXIS_TAIL_PROOF.
Only own code is imported; producer artifacts are numerical coefficient inputs.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import sys,json,hashlib,time,traceback
sys.set_int_max_str_digits(0)
import numpy as np
import mpmath as mp
import torch
from q_local_checkpoint import QLocalCheckpoint
from independent_hydrostatic import CartesianQJet
from hydrostatic_cusp_functional import rational_data,factor,monomial_cusp,tail,cutoff_quadrature,exactmp
import hydrostatic_axis_tail_series as axis

R=Path('research/hydrostatic_cusp_row_audit');V=R/'verification'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
utc=lambda:datetime.now(timezone.utc).isoformat()
def write(p,o):Path(p).write_text(json.dumps(o,indent=2)+'\n')
def parse_pair(t):return F(int(t[0]),int(t[1]))
def strmp(t):return mp.nstr(t,80)
def guard(a):
 bits=max([0]+[abs(t.numerator).bit_length()-t.denominator.bit_length()for t in a if t])
 return int(bits*.30103)+40

def main():
 inputs=json.loads((V/'INPUTS.json').read_text())
 tracked=[Path(__file__),R/'PROOF.md',R/'REVIEW_ADDENDUM.md',R/'AXIS_TAIL_PROOF.md',V/'INPUTS.json',V/'SUMMARY.json',V/'CUSP_GATE.json',V/'AXIS_SERIES_GATE.json']
 tracked += [Path('independent_code')/s for s in ['q_local_checkpoint.py','q_checkpoint_reader.py','independent_hydrostatic.py','hydrostatic_cusp_functional.py','hydrostatic_axis_tail_series.py']]
 out=dict(status='RUNNING',utc_started=utc(),pid=os.getpid(),provenance={str(p):sha(p)for p in tracked},checks=[],states=[])
 def save():out['utc_updated']=utc();write(V/'CUSP_AXIS_CHECKS.json',out)
 def check(name,ok,evidence=None):
  out['checks'].append(dict(name=name,passed=bool(ok),evidence=evidence))
  if not ok:raise AssertionError(name)
 save()
 try:
  for gate,module in [('CUSP_GATE.json','hydrostatic_cusp_functional.py'),('AXIS_SERIES_GATE.json','hydrostatic_axis_tail_series.py')]:
   g=json.loads((V/gate).read_text());check('manufacture gate '+gate,g['status']=='PASS'and g['module_sha256']==sha(Path('independent_code')/module),g.get('count',len(g.get('checks',[]))))
  summ=json.loads((V/'SUMMARY.json').read_text());check('full inverse summary passed',summ['status']=='PASS'and all(c['passed']for c in summ['checks']),len(summ['checks']))
  for item in inputs['states']:
   tag=item['tag'];start=time.monotonic();check(tag+' sourcehash',sha(item['frozen'])==item['sha256'])
   with torch.serialization.safe_globals([np.ndarray,np._core.multiarray._reconstruct]):q=QLocalCheckpoint(item['frozen'])
   state=json.loads((V/(tag+'.json')).read_text());certpath=V/(tag+'.polynomials.json');cert=json.loads(certpath.read_text())
   check(tag+' certificatehash',sha(certpath)==state['polynomial_sha256'])
   kw=list(map(parse_pair,cert['k_w']));hw=list(map(parse_pair,cert['H_w']));PF=parse_pair(cert['P']);LF=parse_pair(cert['L']);pF=1-1/PF
   check(tag+' exactmapmetadata',PF==F(q.kappa)and LF==F(q.L)and 0<pF<F(1,2))
   # Endpoint of each stored local basis is one. Reconstruct the global basis
   # separately and compare in rational arithmetic before any physical scaling.
   b=[sum((F(float(v))for v in row),F(0))for row in q.coeff]
   global_coeff=q.exact_coefficients()
   check(tag+' exact independent endpoints',b==[sum(row,F(0))for row in global_coeff])
   data=rational_data(pF,b,20)
   check(tag+' angular K agrees with axis certificate',data['K']==hw[1])
   check(tag+' angular Q agrees with axis certificate',data['Q']==kw[1]/PF)
   angular=dict(p=str(pF),b_unscaled=list(map(str,b)),K_unscaled=str(data['K']),Q_unscaled=str(data['Q']),Cp_rational=str(data['Cp_rational']),kernel=list(map(str,data['kernel'])),A=list(map(str,data['A'])))
   angularpath=V/(tag+'.angular.json');write(angularpath,angular)
   row=dict(tag=tag,status='RUNNING',source_sha256=item['sha256'],polynomial_sha256=sha(certpath),angular_sha256=sha(angularpath),precision_runs=[],cutoffs=[],axis_runs=[],axis_crosschecks=[])
   out['states'].append(row);save()
   for digits in [140,200]:
    with mp.workdps(digits):
     P=exactmp(PF);p=exactmp(pF);C=exactmp(LF)/2**P;scale=C**(1/P);K=exactmp(data['K'])*scale;Cp=factor(pF)*exactmp(data['Cp_rational'])*scale
     direct,mass=monomial_cusp(pF,b);direct*=scale;error=abs(direct-Cp)/max(1,abs(Cp))
     check(tag+' cusp direct monomial '+str(digits),error<mp.mpf('1e-95'),strmp(error))
     row['precision_runs'].append(dict(digits=digits,K=strmp(K),Cp=strmp(Cp),Cp_K=strmp(Cp/K),monomial=strmp(direct),monomial_absolute_sum=strmp(mass*scale),monomial_relative_error=strmp(error)))
   with mp.workdps(100):
    check(tag+' cusp precision comparison',max(abs(mp.mpf(row['precision_runs'][0][k])-mp.mpf(row['precision_runs'][1][k]))for k in ['K','Cp','Cp_K'])<mp.mpf('1e-70'))
    P=exactmp(PF);p=exactmp(pF);C=exactmp(LF)/2**P;scale=C**(1/P);K=exactmp(data['K'])*scale;Cp=factor(pF)*exactmp(data['Cp_rational'])*scale
    for S in [10000,100000,1000000]:
     tv12,bd12=tail(pF,b,S,12,data);tv20,bd20=tail(pF,b,S,20,data)
     check(tag+' cusp tail bound S'+str(S),abs(tv12-tv20)<=bd12+bd20+mp.mpf('1e-90'),dict(error=strmp(abs(tv12-tv20)*scale),bound12=strmp(bd12*scale),bound20=strmp(bd20*scale)))
     cuts=[cutoff_quadrature(pF,b,S,n)for n in [64,96]]
     errors=[abs(exactmp(v)+tv20-Cp/scale)*scale/max(1,abs(K))for v in cuts]
     check(tag+' independent polar cutoff S'+str(S),max(errors)<mp.mpf('2e-8'),[strmp(e)for e in errors])
     row['cutoffs'].append(dict(S=S,tail=strmp(tv20*scale),tail_K=strmp(tv20*scale/K),tail_bound=strmp(bd20*scale),exact_cutoff_K=strmp((Cp-tv20*scale)/K),polar_cutoff_K=[strmp(exactmp(v)*scale/K)for v in cuts],polar_complete_errors_K=[strmp(e)for e in errors]))
   print(utc(),tag,'CUSP',row['precision_runs'][-1]['Cp_K'][:25],flush=True);save()
   G=guard(kw+hw);ys=[100,1000,10000,1000000,100000000,10000000000,1000000000000,10**16,10**18]
   for extra in [90,135]:
    with mp.workdps(G+extra):
     P=exactmp(PF);p=exactmp(pF);C=exactmp(LF)/2**P;k=list(map(exactmp,kw));H=list(map(exactmp,hw));c=exactmp(F(q.cl));K=exactmp(data['K'])*C**(1/P);Q=exactmp(data['Q'])*C**(1/P)
     c2=C**(2/P)*(H[2]-H[1]/(2*P));r2=(c*(2*p-1)-1)*c2+K*Q/(1-p);m0=axis.moment(k,P,C);e0=c*p-1
     old=state['far_field'][-1]
     for key,value in [('K',K),('Q',Q),('c2',c2),('r2',r2),('m0',m0),('cp_minus1',e0)]:
      check(tag+' independently reconstructed '+key+' dps'+str(mp.mp.dps),abs(value-mp.mpf(old[key]))<mp.mpf('1e-58')*max(1,abs(value)),strmp(value-mp.mpf(old[key])))
     a1=e0/(2+e0);ap=2*(r2-e0*c2)/(K*(2+e0)**2);a0=2*p*m0/(2+e0)**2
     run=dict(digits=mp.mp.dps,m0=strmp(m0),cp_minus1=strmp(e0),K=strmp(K),Q=strmp(Q),c2=strmp(c2),r2=strmp(r2),asymptotic=dict(linear=strmp(a1),power=strmp(ap),constant=strmp(a0),power_constant_crossover=strmp(abs(a0/ap)**(1/p)),binary_power_crossover=strmp(abs(ap/a1)**(1/(1-p)))),points=[])
     row['axis_runs'].append(run)
     for y in ys:
      a=axis.residual(P,C,H,k,c,y,64,m0);rr=axis.residual(P,C,H,k,c,y,96,m0);err=abs(a['V2']-rr['V2'])
      check(tag+' axis series bound '+str(extra)+' y'+str(y),err<=a['remainder_bound']+rr['remainder_bound']+mp.mpf('1e-75'),dict(error=strmp(err),bound64=strmp(a['remainder_bound']),bound96=strmp(rr['remainder_bound'])))
      yy=mp.mpf(y);linear=a1*yy;power=ap*yy**p;constant=a0;pred=linear+power+constant
      rec={key:strmp(val)for key,val in rr.items()};rec.update(asymptotic_total=strmp(pred),asymptotic_linear=strmp(linear),asymptotic_power=strmp(power),asymptotic_constant=strmp(constant),asymptotic_remainder=strmp(rr['y_signed_R_Nf']-pred))
      run['points'].append(rec)
     save();print(utc(),tag,'AXIS',mp.mp.dps,'done',flush=True)
   with mp.workdps(110):
    for a,z in zip(row['axis_runs'][0]['points'],row['axis_runs'][1]['points']):
     check(tag+' axis precision y'+a['y'],max(abs(mp.mpf(a[key])-mp.mpf(z[key]))/max(1,abs(mp.mpf(z[key])))for key in ['w','g','gy','V2','R','Nf','y_signed_R_Nf'])<mp.mpf('1e-65'))
   # Previous full-tail inverse is a different quadrature and reconstruction.
   fine={(p['x'],p['y']):p for p in state['levels'][-1]['points']};jet=CartesianQJet(q)
   for y in [10000]:
    z=next(t for t in row['axis_runs'][-1]['points']if float(t['y'])==y);old=fine[(0.,float(y))];j=jet.jet(0.,float(y))
    errors={key:abs(float(z[key])-old[key])for key in ['g','gy','V2','R','Nf']};errors.update(jet_g=abs(j[0]-float(z['g'])),jet_gy=abs(j[2]-float(z['gy'])))
    check(tag+' far axis previous inverse y'+str(y),errors['V2']<3e-8 and errors['R']<1e-9 and errors['g']<1e-9 and errors['jet_g']<1e-9,errors)
    row['axis_crosschecks'].append(dict(y=y,absolute_errors=errors,previous=old))
   row.update(status='DONE',seconds=time.monotonic()-start);save();print(utc(),tag,'DONE',row['seconds'],flush=True)
  for path,h in out['provenance'].items():check('unchanged '+path,sha(path)==h)
  out.update(status='PASS',utc_finished=utc(),count=len(out['checks']));save();print(utc(),'PASS',len(out['checks']),flush=True)
 except Exception:
  out.update(status='FAIL',utc_failed=utc(),error=traceback.format_exc());save();raise
if __name__=='__main__':main()
