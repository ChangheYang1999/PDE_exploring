"""Fresh Arb768 audit of all saved constants and positive-integral bounds."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
assert not sys.flags.optimize
ctx.prec=768;ctx.threads=1
B=Path(__file__).resolve().parents[3];E=B/'research/annular_traces/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(x):x=F(x);return arb(x.numerator)/x.denominator
def ae(x):
 assert x.is_finite()
 def one(v):assert v.rad()==0;m,e=v.man_exp();return F(int(m))*F(2)**int(e)
 return one(x.lower()),one(x.upper())
def bounds(v):a,b=F(v['lower_exact']),F(v['upper_exact']);assert 0<=a<=b;return a,b
def mx(v):z=[ae(x) for x in v];return aa(max(x[0] for x in z)).union(aa(max(x[1] for x in z)))
def contain(saved,fresh):l,h=bounds(saved);a,b=ae(fresh);assert l<=a<=b<=h,(str(fresh),float(l),float(h))
def main():
 c=json.loads((E/'checks.json').read_text());g=json.loads((E/'algebra.json').read_text())
 assert c['status']=='PASS_TWO_METHOD_CONSTANTS' and g['status']=='PASS_EXACT_ALGEBRA'
 assert c['source_sha256']==sha(B/'research/annular_traces/code/check_constants.py') and g['source_sha256']==sha(B/'research/annular_traces/code/check_algebra.py')
 assert c['proof_sha256']==g['proof_sha256']==sha(B/'research/annular_traces/PROOF.md')
 assert c['runtime']=={'python_flint':'0.9.0','mpmath':'1.3.0','arb_bits':512,'iv_decimal_digits':180}
 assert c['checks']=={'endpoint_containments':10,'nonfinite_rejections':3,'special_function_containments':6,'constant_overlaps':216,'rows':18}
 assert g['checks']=={'kernel_derivatives':60,'multiplier_identities':2,'parity_and_nonzero_moment':27,'whole_window_subtractions':900,'homogeneity_identities':3600,'geometric_identities':16,'parity_resonances':54,'elementary_integral_identities':2}
 expected_names=['u10','u12','u21','v11','v13','v15','v20','v22','v24']
 expected_powers=[[1,3,5,7],[1,3,5],[0,2,4,6],[0,2,4,6],[0,2,4],[0,2],[1,3,5,7],[1,3,5],[1,3]]
 assert [r['trace'] for r in g['trace_table']]==expected_names
 integrals={};ic=0
 for rec in c['positive_integrals']:
  p=F(rec['p_exact']);q=None if rec['q_exact'] is None else F(rec['q_exact']);assert rec['cells']==4096 and rec['critical_cells'] in [1,2] and F(rec['left_exact'])==0
  if rec['kind']=='beta':
   assert q>1 and p>1 and F(rec['right_exact'])==1 and F(rec['peak_exact'])==(p-1)/(p+q-2)
   val=aa(p).gamma()*aa(q).gamma()/aa(p+q).gamma();assert bounds(rec['tail_upper'])==(0,0)
  else:
   assert rec['kind']=='gamma' and F(rec['right_exact'])==64 and F(rec['peak_exact'])==p-1<64
   val=aa(p).gamma();tail=aa(64)**aa(p-1)*arb(-64).exp()/aa(1-(p-1)/64);contain(rec['tail_upper'],tail)
  contain(rec['enclosure'],val);lo,hi=bounds(rec['enclosure']);assert lo<=F(rec['sum_lower_exact'])<=F(rec['sum_upper_with_tail_exact'])<=hi
  integrals[(rec['kind'],p,q)]=rec;ic+=1
 assert ic==6
 checked=0;public=[]
 for idx,row in enumerate(c['rows']):
  a0,b0=(F('6.45'),F('3.07')) if idx<9 else (F('6.495'),F('3.403'));label=expected_names[idx%9];assert row['trace']==label and (F(row['original_a_exact']),F(row['original_b_exact']))==(a0,b0)
  a,b=(b0,a0) if label.startswith('v') else (a0,b0);j=int(label[-1]);parity=1 if label[1]=='1' and label[0]=='u' or label[1]=='2' and label[0]=='v' else 0
  t=a+b-j-1;sig=b-j-F(1,2);s=sig.numerator//sig.denominator;th=sig-s;K=s+1
  ls=expected_powers[idx%9];P=ls[-1]+2;delta=P-t;mu=t-ls[-1]
  H={p:max(F(math.factorial(p),math.factorial(p-d))*F(2)**(p-d) for d in range(min(K,p)+1)) for p in ls}
  m=row['metadata'];assert m=={'a_exact':str(a),'b_exact':str(b),'j':j,'parity':parity,'t_exact':str(t),'sigma_exact':str(sig),'s':s,'theta_exact':str(th),'K':K,'powers':ls,'P':P,'near_exponent_exact':str(delta),'far_exponent_exact':str(mu),'H_exact':{str(p):str(v) for p,v in H.items()}}
  assert delta>0 and mu>0
  Q=(2*aa(a+F(1,2)).gamma()*aa(b+F(1,2)).gamma()/aa(a+b+1).gamma()*(2**aa(2*a+2*b+2)-1)/aa(2*a+2*b+2)).sqrt()
  J=aa(2*K+4+F(2)/((1-th)*(3-2*th))).sqrt();S=aa(K+F(1)/(1-th)+F(4)/th).sqrt()
  low=2**aa(b)/(math.factorial(j)*aa(2*b+1).sqrt());high=2**aa(-b-1)*aa(2*b+1).gamma().sqrt()/math.factorial(j);FF=2**aa(sig/2)*mx([low,high])
  def D(n):return arb(math.factorial(n+j+1))/(2*arb.pi())
  cn=Q*J/math.factorial(j)*mx([aa(F(2)**max(P-d,0)/math.factorial(max(P-d,0))*F(4,3)**(2+j+max(P,d)))*D(max(P,d)) for d in range(K+1)])
  cf=Q*J/math.factorial(j)*(mx([aa(F(4,3)**(2+j+d))*D(d) for d in range(K+1)])+sum((aa(H[p]/math.factorial(p))*D(p) for p in ls),arb(0)))
  cm=4**aa(abs(t))*(2*4**aa(sig)*S*2**aa(a)*FF+Q*J/math.factorial(j)*sum((aa(F(4)**p*H[p]/math.factorial(p))*D(p) for p in ls),arb(0)))
  tn=2**aa(-3*delta)/(1-2**aa(-delta));tf=2**aa(-3*mu)/(1-2**aa(-mu));total=cn*tn+5*cm+cf*tf
  fresh={'Q':Q,'J':J,'S':S,'F_low':low,'F_high':high,'F':FF,'C_near':cn,'C_far':cf,'C_mid':cm,'near_tail':tn,'far_tail':tf,'C':total}
  assert set(row['constants'])==set(fresh)
  for key,v in fresh.items():
   for method in ['arb','iv']:contain(row['constants'][key][method],v);checked+=1
  for rec,gap in zip(row['iv_dyadic_tails'],[delta,mu]):
   assert F(rec['gap_exact'])==gap and rec['terms']==128 and rec['first_power']==3 and rec['remainder_first_power']==131
   ratio=2**aa(-gap);contain(rec['ratio'],ratio);contain(rec['remainder'],ratio**131/(1-ratio))
  parts=[bounds(row['constants']['C'][m]) for m in ['arb','iv']];lo=min(v[0] for v in parts);hi=max(v[1] for v in parts)
  assert (lo,hi)==(F(row['joint_C_lower_exact']),F(row['joint_C_upper_exact'])) and hi<F(row['strict_public_C_upper_exact'])
  public.append({'trace':label,'a_exact':str(a0),'b_exact':str(b0),'C_upper_exact':row['strict_public_C_upper_exact'],'strict':True})
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','source_sha256':sha(__file__),'proof_sha256':c['proof_sha256'],'checks_sha256':sha(E/'checks.json'),'algebra_sha256':sha(E/'algebra.json'),'fresh_Arb_precision':768,'constant_endpoint_containments':checked,'positive_integral_containments':ic,'public_bounds':public,'scope':'Fresh saved-scalar and source audit. Does not rerun the positive mesh sums, which were actually computed by the separate iv core.'}
 (E/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
if __name__=='__main__':main()
