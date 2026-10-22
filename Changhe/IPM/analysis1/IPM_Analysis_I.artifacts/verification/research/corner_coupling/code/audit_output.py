"""Fresh Arb768 reconstruction of saved blocks and final scalar formulas."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import check_constants as core
from flint import arb,ctx
assert not sys.flags.optimize
ctx.prec=768;ctx.threads=1
B=Path(__file__).resolve().parents[3];E=B/'research/corner_coupling/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def aa(x):return core.aa(x)
def pp(base,x):return core.apow(base,x)
def main():
 r=load(E/'checks.json');a=load(E/'algebra.json')
 assert r['source_sha256']==sha(B/'research/corner_coupling/code/check_constants.py') and a['source_sha256']==sha(B/'research/corner_coupling/code/check_algebra.py')
 assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/corner_coupling/PROOF.md')
 assert r['status']=='PASS_TWO_METHOD_CONSTANTS' and a['status']=='PASS_EXACT_ALGEBRA' and r['checks']=={'rows':2,'shifted_rows':46,'overlaps':618,'beta_containments':2,'endpoint_containments':10,'nonfinite_rejections':3}
 counts={'block_endpoint_containments':0,'shifted_endpoint_containments':0,'final_endpoint_containments':0,'beta_integral_containments':0,'public_comparisons':0};public=[]
 def contain(saved,value,kind):
  lo,hi=core.ae(value)
  for method in ['arb','iv']:
   assert F(saved[method]['lower_exact'])<=lo<=hi<=F(saved[method]['upper_exact']);counts[kind]+=1
 for row in r['rows']:
  a,b,g=F(row['a_exact']),F(row['b_exact']),F(row['gamma_exact']);A=a+b;d=F(1,2);values={};coeffs={}
  assert row['d_exact']=='1/2' and g==F(1129,1000)
  for item in row['shifted_rows']:
   N,M=item['N'],item['M'];u,v=a-6+N,b-3+M
   assert (F(item['u_exact']),F(item['v_exact']))==(u,v)
   vectors=core.arb_blocks(N,M);forms=core.rational_blocks(N,M);blocks={}
   for case in core.CASES:
    rr,ss=map(F,item['cases'][case]['rational_plus_inverse_pi']);assert (rr,ss)==forms[case]
    value=aa(rr)+aa(ss)/arb.pi();lo,hi=core.ae(value);ol,oh=core.ae(vectors[case]);assert max(lo,ol)<=min(hi,oh)
    # If the exact form is an integer, keep its exact zero radius. The
    # unreduced pi/pi formula can have a radius at every working precision.
    blocks[case]=value;contain(item['cases'][case],value,'block_endpoint_containments')
   block=core.maximum(blocks.values(),'arb');lx=core.arb_L(N,u);ly=core.arb_L(M,v);c=pp(2,abs(u)+abs(v))*block*lx*ly
   for key,value in [('B',block),('Lx',lx),('Ly',ly),('C',c)]:contain(item[key],value,'shifted_endpoint_containments')
   coeff=F(0)
   if M<=2:coeff+=(F(15,2)-N)/(math.factorial(5-N)*math.factorial(2-M))
   if N<=4:coeff+=(F(9,2)-M)/(math.factorial(4-N)*math.factorial(3-M))
   assert coeff==F(item['coefficient_exact']);values[N,M]=c;coeffs[N,M]=coeff
  assert len(values)==23 and (5,3) not in values
  vel=sum((aa(coeffs[key])*c for key,c in values.items()),arb(0))
  beta=aa(a+F(1,2)).gamma()*aa(b+F(1,2)).gamma()/aa(A+1).gamma();integral=row['positive_beta_integral'];lo,hi=core.ae(beta)
  assert F(integral['sum_lower_exact'])<=lo<=hi<=F(integral['sum_upper_exact']);assert integral['cells']==4096 and (F(integral['p_exact']),F(integral['q_exact']))==(a+F(1,2),b+F(1,2));counts['beta_integral_containments']+=1
  monomial=(4*pp(d,20-2*A)/(aa(13-2*a)*aa(7-2*b))).sqrt();strain=(beta*pp(2,A-2)/aa(A-2)).sqrt()/arb.pi();tg=(2*beta/aa(4-2*g)).sqrt();h0=F(5,72);assert F(row['H0_exact'])==h0
  ff={0:d/(1-d)**3,**{q:F(math.factorial(q+1),2)/(1-d)**(q+2) for q in range(1,8)}}
  def sm(N,M,kind):return sum(F(math.comb(N,p)*math.comb(M,q),math.factorial(N)*math.factorial(M))*(2+p+d if kind==1 else 1+q+d)*ff[7-p-q] for p in range(N+1) for q in range(M+1))
  s1,s2=sm(5,2,1),sm(4,3,2);assert (s1,s2)==(F(row['S1_times_pi_exact']),F(row['S2_times_pi_exact']))
  unit=vel+aa(h0)*strain*monomial;far=monomial*tg*aa(s1+s2+h0)/arb.pi();comp=(unit**2+far**2).sqrt()
  final={'beta':beta,'M_d':monomial,'C_str':strain,'T_gamma':tg,'S1':aa(s1)/arb.pi(),'S2':aa(s2)/arb.pi(),'C_vel':vel,'C_unit':unit,'C_far':far,'C_comp':comp}
  pub={}
  for name,value in final.items():
   saved=row['constants'][name];contain(saved,value,'final_endpoint_containments')
   joint=max(F(saved[method]['upper_exact']) for method in ['arb','iv']);upper=F(saved['public_strict_upper_exact']);assert joint==F(saved['joint_upper_exact'])<upper and core.ae(value)[1]<upper;counts['public_comparisons']+=1;pub[name]=str(upper)
  public.append({'a_exact':str(a),'b_exact':str(b),'gamma_exact':str(g),'strict_bounds':pub})
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'proof_sha256':r['proof_sha256'],'checks_sha256':sha(E/'checks.json'),'algebra_sha256':sha(E/'algebra.json'),'fresh_arb_bits':ctx.prec,'checks':counts,'public_bounds':public,'scope':'Fresh saved-scalar and source audit. It recomputes Arb formulas at768bits and exact grouping factors. It does not rerun the separate positive iv mesh sum and is not a third independent method.'}
 (E/'output_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
