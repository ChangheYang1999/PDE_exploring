"""Fresh Arb1536 constants, independent exponent parse and differential rows."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import json,sys,time,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/lower_regularity/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ends(x):return tuple(F(int(m))*F(2)**int(e) for m,e in [v.man_exp() for v in (x.lower(),x.upper())])
def rec(x):l,u=ends(x);return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def main():
 start=time.monotonic();ctx.prec=1536;ctx.threads=1;r=json.loads((E/'checks.json').read_text());inp=json.loads((E/'inputs.json').read_text());data=B/'data_exact/modal_v2.json'
 assert r['status']=='PASS' and r['code_sha256']==sha(B/'research/lower_regularity/code/check_regularity.py') and r['proof_sha256']==sha(B/'research/lower_regularity/PROOF.md') and r['input_sha256']==sha(E/'inputs.json') and r['data_sha256']==sha(data)
 h=json.loads(data.read_text())['scalars_hex']['k'];mant,exp=h.split('p');a,b=mant[2:].split('.');k=F(int(a+b,16))*F(2)**(int(exp)-4*len(b));assert k==F(inp['k']);g=F(inp['g_illustration']);A=(2-k)/k;D=(4-k)/k;c0=(1+k)/k
 exact={'k':k,'g_illustration':g,'A':A,'D':D,'c0':c0,'weight_s_max':(F(13,2)*A+c0)/D,'weight_lower_s2.5':(F(5,2)*D-c0)/A,'rate_s2.5_a5':-c0-5*A+F(5,2)*D,'p2':(4*A+1)/D,'p2_threshold':(4*A+1)/D+F(1,2),'fast_s2':2*A-c0-g,'fast_s3':3*A-c0-g,'slow_s2':2-c0,'slow_s3':3-c0,'pure_fast_s2':2*A-c0,'pure_fast_s3':3*A-c0};checks=0
 for row in r['recurrences']:
  n=row['n'];p=(g+1-n)/A;exact['p_n'+str(n)]=p;exact['threshold_n'+str(n)]=p+F(1,2);b=list(map(F,row['coefficients_exact']));assert b[0]==1 and len(b)==(n+1)//2
  # coefficient of each monomial after differentiating every individual transport monomial
  for j in range(len(b)-1):
   q=p+2*j;t=n-2*j;later=q+2;ty=t-2
   cy=-(A*q+t-1)*t*(t-1)*b[j]
   cs=(g-(A*later+ty-1))*later*(later-1)*b[j+1]
   assert cy+cs==0;checks+=1
 assert r['exact_parameters']=={n:str(v) for n,v in exact.items()} and len(r['exact_identities'])==19 and set(r['exact_identities'].values())=={'0'}
 pi=4*aa(1).atan();vals={n:aa(v) for n,v in exact.items()};vals['pi']=pi
 pl,pu=map(F,r['pi_rational_bracket']);ctx.prec=4096;pi_check=4*aa(1).atan();assert aa(pl)<pi_check<aa(pu);ctx.prec=1536
 for order in inp['strain_orders']:
  s=F(order);tag='strain_'+order.replace('/','_');normsq=1/(64*pi*aa(s-1)*aa(s-2));vals[tag]=normsq.sqrt();vals[tag+'_c']=(normsq/9).sqrt()
 count=0
 for n,v in vals.items():
  l,u=ends(v)
  for m in ['arb','iv']:
   z=r['values'][m][n];assert F(z['lower_exact'])<=l<=u<=F(z['upper_exact']),(n,m);count+=1
 o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'check_code_sha256':r['code_sha256'],'proof_sha256':r['proof_sha256'],'checks_sha256':sha(E/'checks.json'),'fresh_containments':count,'fresh_differential_cancellations':checks,'fresh_values':{n:rec(v) for n,v in vals.items()},'method':'Arb1536 pi=4atan(1), Arb4096 inside the narrower exact Machin bracket, squared dual norm, independent exact hex parse and differentiated coefficient cancellations.','seconds':time.monotonic()-start}
 (E/'output_audit.json').write_text(json.dumps(o,indent=2)+'\n');summary=json.loads((E/'review_summary.json').read_text());summary['audit_sha256']=sha(E/'output_audit.json');summary['audit']={k:v for k,v in o.items() if k!='fresh_values'};(E/'review_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in o.items() if k in ('utc','status','seconds','fresh_containments','fresh_differential_cancellations')}))
if __name__=='__main__':main()
