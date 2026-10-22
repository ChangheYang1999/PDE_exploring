"""Fresh Arb1536 endpoint-derivative integrals and exact output audit."""
import sys,json,hashlib,math,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import flint
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/jet_extension/evidence';ctx.prec=1536;ctx.threads=1;t0=time.monotonic()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ar(q):q=F(q);return arb(q.numerator)/q.denominator
def ends(v):
 assert v.is_finite();out=[]
 for t in [v.lower(),v.upper()]:
  assert t.rad()==0;n,e=t.man_exp();out.append(F(int(n))*F(2)**int(e))
 return out
def within(o,z):
 lo,hi=F(o['lower_exact']),F(o['upper_exact']);a,b=ends(z);assert lo<=a<=b<=hi
r=json.loads((E/'checks.json').read_text());run=json.loads((E/'local_run.json').read_text())
assert r['status']=='PASS' and run['returncode']==0 and r['code_sha256']==sha(B/'research/jet_extension/code/check_extension.py') and r['proof_sha256']==sha(B/'research/jet_extension/PROOF.md')
assert datetime.fromisoformat(run['start_utc'])<datetime.fromisoformat(r['utc'])<datetime.fromisoformat(run['end_utc'])
assert r['symbolic_identities']==10 and r['cutoff']['qprime_bernstein']==[-60,-20,200,-120]
# Regenerate midpoint sum from the factored polynomial, independent of the check's integer polynomial sum.
N=r['quadrature']['N'];assert N==8192;sm=F()
for j in range(N):
 u=F(2*j+1,2*N);sm+=abs(-60*u*(1-u)*(1-3*u*u))/N
assert str(sm)==r['quadrature']['midpoint_exact'];assert F(r['quadrature']['error_exact'])==F(50,N)
assert F(r['quadrature']['midpoint_iv']['lower_exact'])<=sm<=F(r['quadrature']['midpoint_iv']['upper_exact'])
const={'C_B':3/arb.pi(),'C_S':9-16/(3*arb(3).sqrt()),'D_B':8*arb(2).sqrt()/7};pub={'C_B':F(955,1000),'C_S':F(593,100),'D_B':F(1617,1000)}
for key,z in const.items():
 for method in ['arb','iv']:
  o=r['constant_exports'][key][method];within(o,z);assert 0<F(o['lower_exact'])<=F(o['upper_exact'])<pub[key]
 assert F(r['constant_exports'][key]['public_strict_upper'])==pub[key]
# Independent polynomial endpoint integration via derivatives, with no incomplete-gamma moment routine.
def integral(poly,lo,hi,a):
 def anti(t):
  deriv=poly[:];s=arb(0);power=ar(a)
  while deriv:
   val=sum((c*F(t)**j for j,c in enumerate(deriv)),F());s+=ar(val)/power
   deriv=[(j+1)*deriv[j+1] for j in range(len(deriv)-1)];power*=ar(a)
  return -(-ar(a)*t).exp()*s
 return anti(hi)-anti(lo)
# z*(1-10(z-1)^3+15(z-1)^4-6(z-1)^5), expanded directly by binomial coefficients.
outer=[F(0)]*7;outer[1]=F(1)
for power,coef in [(3,-10),(4,15),(5,-6)]:
 for j in range(power+1):outer[j+1]+=coef*math.comb(power,j)*(-1)**(power-j)
assert [str(v) for v in outer]==r['cutoff']['outer_zchi_coefficients']
for n,value in enumerate(r['positive_moments_exact']):
 left=sum((F(math.comb(n,j),(j+1)*(j+2)) for j in range(n+1)),F())
 right=sum((F(c,n+j+1) for j,c in [(3,20),(4,-40),(5,27),(6,-6)]),F())
 assert F(value)==left+right and left>0 and right>0
assert len(r['positive_moments_exact'])==161
for row,expected in zip(r['frequency_checks'],[F(1,2),F(1),F(4),F(16)]):
 a=F(row['a']);assert a==expected;I=integral([F(0),F(1)],0,1,a)+integral(outer,1,2,a)
 for key in ['I_arb_moments','I_iv_positive_series']:within(row[key],I)
 within(row['P_arb'],ar(a*a)*I);within(row['S_arb'],1-ar(a*a)*I)
 assert F(row['remainder_upper_exact'])==F(8,7)*(2*a)**161/math.factorial(161)
 assert 0<F(row['I_iv_positive_series']['lower_exact']) and a*a*F(row['I_iv_positive_series']['upper_exact'])<1
assert len(r['frequency_checks'])==4
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','checks_sha256':sha(E/'checks.json'),'code_sha256':sha(__file__),'check_code_sha256':r['code_sha256'],'proof_sha256':r['proof_sha256'],'fresh_constant_containments':6,'fresh_frequency_containments':16,'exact_midpoints':N,'exact_positive_moments':161,'arb_bits':ctx.prec,'python_flint':flint.__version__,'seconds':time.monotonic()-t0,'scope':'Fresh endpoint-derivative integral consistency audit and exact sums, not a third independent proof.'}
(E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
