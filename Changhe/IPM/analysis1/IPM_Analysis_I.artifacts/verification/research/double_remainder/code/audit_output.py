"""Exact Machin certificate for every block constant; independent scalar audit."""
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
assert not sys.flags.optimize
ctx.prec=768;ctx.threads=1
B=Path(__file__).resolve().parents[3];E=B/'research/double_remainder/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def ae(x):
 assert x.is_finite()
 def one(y):assert y.rad()==0;m,e=y.man_exp();return F(int(m))*F(2)**int(e)
 return one(x.lower()),one(x.upper())
def bs(x):l,h=F(x['lower_exact']),F(x['upper_exact']);assert l<=h;return l,h
def atan_bounds(x,n=320):
 assert n%2==0 and 0<x<1
 s=sum((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n));return s,s+x**(2*n+1)/F(2*n+1)
def symbolic_cases(n,m):
 # Each vector coefficient is recorded as (rational, coefficient of pi).
 def small(k):return {k:(F(2)**(k+1)*F(4,3)**(k+1)/math.factorial(k),F(0))}
 def correction(k):return {p:(F(4)*8**p/math.factorial(p),F(0)) for p in range(k)}
 def large(k):
  v={p:(F(2)**(p+1)/math.factorial(p),F(0)) for p in range(k)};v[0]=(v.get(0,(F(0),F(0)))[0]+F(8,3),F(0));return v
 def comparable(k):
  v=correction(k);v[0]=(v.get(0,(F(0),F(0)))[0],F(1));return v
 def mul(v,w):
  terms={-1:F(0),0:F(0),1:F(0)}
  for p,(a,b) in v.items():
   for q,(c,d) in w.items():
    f=F(math.factorial(p+q+1),2);terms[-1]+=a*c*f;terms[0]+=(a*d+b*c)*f;terms[1]+=b*d*f
  assert terms[1]==0
  return terms[0],terms[-1]
 x={'S':small(n),'L':large(n),'C':comparable(n)};y={'S':small(m),'L':large(m),'C':comparable(m)};out={}
 for c in ['SS','SL','LS','LL','SC','LC','CS','CL']:out[c]=mul(x[c[0]],y[c[1]])
 alpha,beta=mul(correction(n),correction(m));assert alpha==0
 alpha=F(1)+sum(F(4)*8**p/math.factorial(p)*F(math.factorial(p+1),2) for p in range(n))+sum(F(4)*8**q/math.factorial(q)*F(math.factorial(q+1),2) for q in range(m));out['CC']=alpha,beta
 return out

def main():
 r=json.loads((E/'checks.json').read_text());al=json.loads((E/'algebra.json').read_text())
 assert r['status']=='PASS_SCALARS' and al['status']=='PASS_EXACT_ALGEBRA'
 assert r['source_sha256']==sha(B/'research/double_remainder/code/check_constants.py') and al['source_sha256']==sha(B/'research/double_remainder/code/check_algebra.py')
 assert r['proof_sha256']==al['proof_sha256']==sha(B/'research/double_remainder/PROOF.md') and r['lead_snapshot_sha256']==sha(E/'lead_corner_coupling.md')
 assert r['runtime']=={'python_flint':'0.9.0','mpmath':'1.3.0','arb_bits':512,'iv_decimal_digits':180}
 assert r['checks']=={'endpoint_containments':10,'nonfinite_rejections':3,'case_and_global_overlaps':78,'rows':6}
 assert al['checks']=={'kernel_derivative_polynomials':140,'commutator_order_and_homogeneous_sign':128,'homogeneous_degrees':64,'Stirling_monomial_identities':234,'positive_kernel_constants':448}
 lo5,hi5=atan_bounds(F(1,5));lo239,hi239=atan_bounds(F(1,239));pl,ph=16*lo5-4*hi239,16*hi5-4*lo239
 assert F(3)<pl<ph<F(22,7)
 t=F(1,5);t2=2*t/(1-t*t);t4=2*t2/(1-t2*t2);assert t4==F(120,119) and (t4-F(1,239))/(1+t4*F(1,239))==1
 pi_l,pi_h=ae(arb.pi());assert pi_l<=pl<ph<=pi_h
 counts=0;globalcounts=0;public=[];rationalcases=[]
 expected=[(6,3,'129/20','307/100'),(6,3,'1299/200','3403/1000'),(0,0,'0','0'),(0,3,'-49/100','307/100'),(6,0,'129/20','49/100'),(1,1,'1','1')]
 assert [(v['N'],v['M'],v['a_exact'],v['b_exact']) for v in r['rows']]==expected
 for idx,row in enumerate(r['rows']):
  n,m,a,b=row['N'],row['M'],F(row['a_exact']),F(row['b_exact']);forms=symbolic_cases(n,m);bycase={x['case']:x for x in row['nine_cases']};assert set(bycase)==set(forms)
  values=[]
  for c,(alpha,beta) in forms.items():
   assert alpha>=0 and beta>=0;l,h=alpha+beta/ph,alpha+beta/pl
   for method in ['arb','iv']:
    x,y=bs(bycase[c][method]);assert x<=l<=h<=y;counts+=1
   v=aa(alpha)+aa(beta)/arb.pi();values.append(v)
   rationalcases.append({'row':idx,'case':c,'constant_exact':str(alpha),'inverse_pi_coefficient_exact':str(beta)})
  mb_l=max(ae(v)[0] for v in values);mb_h=max(ae(v)[1] for v in values);mb=aa(mb_l).union(aa(mb_h))
  def L(N,a):
   vals=[2**(aa(-a*d)) for d in range(-2,3)]
   for delta in [F(N)+F(1,2)-a,a-F(N)+F(1,2)]:
    assert delta>0;q=2**aa(-delta);vals.append(q**3/(1-q))
   return sum(vals,arb(0))
  lx,ly=L(n,a),L(m,b);C=2**aa(abs(a)+abs(b))*mb*lx*ly
  for key,v in [('B',mb),('Lx',lx),('Ly',ly),('C',C)]:
   l,h=ae(v)
   for method in ['arb','iv']:
    x,y=bs(row[key][method]);assert x<=l<=h<=y;globalcounts+=1
  for coordinate,N,a0 in [('x',n,a),('y',m,b)]:
   tails=row['iv_geometric_tails'][coordinate];assert [F(z['delta_exact']) for z in tails]==[F(N)+F(1,2)-a0,a0-F(N)+F(1,2)]
   for z in tails:
    assert z['terms']==128 and z['first_power']==3 and z['remainder_first_power']==131
    l,h=bs(z['ratio']);assert 0<l<=h<1
    # Check the analytic finite-geometric decomposition at exact rational arguments.
    for q in [l,h]:assert sum(q**d for d in range(3,131))+q**131/(1-q)==q**3/(1-q)
  bounds=[bs(row['C'][method]) for method in ['arb','iv']];joint=(min(v[0] for v in bounds),max(v[1] for v in bounds))
  assert joint==(F(row['joint_C_lower_exact']),F(row['joint_C_upper_exact'])) and joint[1]<F(10)**row['strict_power10_upper_exponent']
  if idx in [0,1]:
   top=F(472500000000000000) if idx==0 else F(1114000000000000000);assert joint[1]<top
   public.append({'a_exact':row['a_exact'],'b_exact':row['b_exact'],'C_upper_exact':str(top),'strict':True})
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'proof_sha256':r['proof_sha256'],'checks_sha256':sha(E/'checks.json'),'algebra_sha256':sha(E/'algebra.json'),'block_endpoint_containments':counts,'global_endpoint_containments':globalcounts,'machin_pi_interval':[str(pl),str(ph)],'rational_case_forms':rationalcases,'public_bounds':public,'scope':'Exact rational block-constant certificate from the proved Machin identity; high-precision saved scalar checks and source linkage. Does not rerun the original Arb/iv or polynomial cores.'}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ['machin_pi_interval','rational_case_forms']}))
if __name__=='__main__':main()
