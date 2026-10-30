"""Four-pole scalar fixtures, including mixed radius25/radius50 products."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import importlib.util,json,time,sys
from flint import arb,ctx,fmpq as Q,fmpq_poly as Poly
ROOT=Path(__file__).resolve().parents[3];BASE=ROOT/'research/joint_scaled_factored_weak'
spec=importlib.util.spec_from_file_location('n4_joint_scalar_moments',ROOT/'research/factored_pole_moments/code/moments.py')
M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
sys.set_int_max_str_digits(0);V=Poly([0,1]);ar=M.ar
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def main():
 tick=time.monotonic();ctx.prec=2048;dest=BASE/'verification/scalar_joint.json';assert not dest.exists()
 fixtures=[]
 for b,m,a,maximum in [(Q(-2,3),0,Q(624),36),(Q(-2,3),0,Q(2499),36),(Q(7,4),8,Q(99),24),(Q(5,3),3601,Q(624),64),(Q(5,3),3601,Q(2499),64),(Q(11,7),4801,Q(624),64),(Q(11,7),4801,Q(2499),64),(Q(-3,4),1045,Q(9999),24)]:
  start=time.monotonic();values,checks=M.pole_moments(b,m,a,maximum)
  assert min(x.rel_accuracy_bits() for x in values)>150 and all(c['direct_overlap'] and c['direct_accuracy_bits']>150 for c in checks)
  prior=[]
  if m==0:
   old=M.OLD.pole_moments(b,a,maximum);prior=[x.overlaps(y) for x,y in zip(values,old,strict=True)];assert all(prior)
  fixtures.append({'b':str(b),'m':m,'a':str(a),'maximum_power':maximum,'checks':checks,'old_m0_overlaps':prior,'first':values[0].str(100),'last':values[-1].str(100),'elapsed_seconds':time.monotonic()-start})
  print('POLE',b,m,a,maximum,'passed',time.monotonic()-start,flush=True)
 rows=[]
 cases=[(Q(1,3),0,Poly([2,-3,5]),[(Q(624),2),(Q(2499),3)]),(Q(-2,3),5,Poly([1,-5,2,7]),[(Q(99),2),(Q(624),4),(Q(2499),3),(Q(9999),2)]),(Q(7,4),12,Poly([3,0,-7,2]),[(Q(99),3),(Q(624),2),(Q(2499),2),(Q(9999),2)]),(Q(0),64,Poly([1]),[(Q(624),3),(Q(2499),2)]),(Q(5,7),522,Poly([2,0,-3,1]),[])]
 for b,m,N,factors in cases:
  start=time.monotonic();x,record=M.integral(b,m,N,factors)
  if m<=64:
   y,old=M.OLD.integral(b,N*(1-V)**m,factors);comparison='Independent expanded localization and old pole recurrence'
  else:
   y=sum((ar(c)*M.beta(b+j+1,m+1) for j,c in enumerate(N)),arb(0));comparison='Direct Gamma quotient for every polynomial beta moment'
  assert x.overlaps(y) and min(x.rel_accuracy_bits(),y.rel_accuracy_bits())>150
  rows.append({'b':str(b),'m':m,'numerator':[str(c) for c in N],'factors':[[str(a),k] for a,k in factors],'result':x.str(100),'comparison_result':y.str(100),'comparison':comparison,'overlap':True,'record':record,'elapsed_seconds':time.monotonic()-start})
  print('MIXED',b,m,'passed',time.monotonic()-start,flush=True)
 # An independent two-fraction identity checks mixed large localization directly.
 for b,m in [(Q(5,3),3601),(Q(11,7),4801)]:
  start=time.monotonic();a,d=Q(624),Q(2499);x,record=M.integral(b,m,Poly([1]),[(a,1),(d,1)])
  base=M.beta(b+1,m+1)
  def direct(pole):return base*(-ar(pole)).hypgeom_2f1(arb(1),ar(b+1),ar(b+m+2),bc=True,abc=True)
  y=(ar(a)*direct(a)-ar(d)*direct(d))/ar(a-d)
  assert x.overlaps(y) and min(x.rel_accuracy_bits(),y.rel_accuracy_bits())>150
  rows.append({'b':str(b),'m':m,'numerator':['1'],'factors':[[str(a),1],[str(d),1]],'result':x.str(100),'comparison_result':y.str(100),'comparison':'Direct hypergeometric evaluation of independent two-fraction identity','overlap':True,'record':record,'elapsed_seconds':time.monotonic()-start})
  print('LARGE MIXED',b,m,'passed',time.monotonic()-start,flush=True)
 paths=[BASE/'PROOF.md',Path(__file__),ROOT/'research/factored_pole_moments/code/moments.py',ROOT/'research/factored_pole_moments/PROOF.md',ROOT/'research/rational_pole_moments/code/moments.py',ROOT/'research/rational_pole_moments/PROOF.md',ROOT/'research/rational_pole_moments/reviews/T4/ACCEPTANCE.json']
 out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'inputs':{str(p.relative_to(ROOT)):sha(p) for p in paths},'pole_fixtures':fixtures,'integral_fixtures':rows,'elapsed_seconds':time.monotonic()-tick,'status':'OPEN independent review; complete own simultaneous-pole fixtures, no candidate result'}
 with dest.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('DONE',out['utc'],out['elapsed_seconds'],sha(dest),flush=True)
if __name__=='__main__':main()
