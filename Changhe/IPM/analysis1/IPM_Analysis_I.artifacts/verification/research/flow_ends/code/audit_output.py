"""Fresh scalar audit with exact angular identities and independent factorization."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import json,sys,time,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_ends/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ends(x):return tuple(F(int(m))*F(2)**int(e) for m,e in [v.man_exp() for v in (x.lower(),x.upper())])
def rec(x):l,u=ends(x);return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def main():
 t=time.monotonic();ctx.prec=1536;ctx.threads=1;r=json.loads((E/'checks.json').read_text());assert r['status']=='PASS' and r['code_sha256']==sha(B/'research/flow_ends/code/check_ends.py') and r['proof_sha256']==sha(B/'research/flow_ends/PROOF.md')
 for f,h in r['dependency_pins'].items():assert sha(B/f)==h
 x={n:F(v) for n,v in r['exact_inputs'].items()};N=261;ids=0
 # Laurent polynomial identities for sin(2n theta)/sin theta and /cos theta.
 for n in range(1,N+1):
  for reflect in [False,True]:
   row={}
   for j in range(n):
    for e,sgn in [(2*j+1,1),(-2*j-1,-1 if reflect else 1)]:
     value=sgn*((-1)**(n-1+j) if reflect else 1)
     for delta,mult in [(1,1),(-1,1 if reflect else -1)]:row[e+delta]=row.get(e+delta,0)+value*mult
   assert {k:v for k,v in row.items() if v}=={2*n:1,-2*n:-1};ids+=1
 factor_ids=0
 for m in range(260):
  row={}
  for f in [2*m+1,1-2*m,2*m+3,3-2*m]:
   j=(abs(f)-1)//2;row[j]=row.get(j,0)+(1 if f>0 else -1)
  assert sum((-1)**j*v for j,v in row.items())==0;factor_ids+=1
 k=aa(x['k']);cl=1/k;c=(3-k)/k;S=aa(x['a']+x['b']);gamma=aa(x['gamma']);R=(aa(x['ta']/32).exp())**32;Re=(aa((x['tb']+9)/32).exp())**32;D=aa(x['Cr']+522*x['Ct'])*R*R;L=(k-2)/k-D
 delta=(S-gamma)/(1+(6/R)**4);muR=S-delta;muE=gamma+(S-gamma)/(1+(Re/6)**4)
 inner=-1+(S-1)*cl+aa(x['b']-x['a'])*c+S*D-delta*L
 outer=-1+(muE-1)*cl+aa((x['a']+x['b'])*x['Q']+(x['a']+x['b']-x['gamma'])*x['P'])
 vals={'R':R,'Re':Re,'cl':cl,'c':c,'Cr':aa(x['Cr']),'Ct':aa(x['Ct']),'P':aa(x['P']),'Q':aa(x['Q']),'D':D,'inner_s_lower':L,'inner_v2_lower':(4-k)/k-D,'inner_v1_upper':(k-2)/k+D,'inner_T_upper':inner,'outer_s_lower':cl-aa(x['P']),'outer_vi_lower':cl-aa(x['Q']),'outer_T_upper':outer,'muR':muR,'muE':muE};count=0
 for n,v in vals.items():
  l,u=ends(v)
  for m in ['arb','iv']:
   z=r['values'][m][n];assert F(z['lower_exact'])<=l<=u<=F(z['upper_exact']),(n,m);count+=1
  if n in r['public']:
   direction,q=r['public'][n];assert u<F(q) if direction=='upper' else l>F(q)
 assert ends(R)[1]<F(float(4.8)) and ends(Re)[0]>20
 o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'check_code_sha256':r['code_sha256'],'proof_sha256':r['proof_sha256'],'checks_sha256':sha(E/'checks.json'),'fresh_containments':count,'angular_identities':ids,'factor_cancellations':factor_ids,'fresh_values':{n:rec(v) for n,v in vals.items()},'method':'Arb1536 with exp(t/32)^32, independent normalized eigenvalue and conic factorization, 522 exact Laurent polynomial identities. All dependency pins and outward public decimals rechecked.','seconds':time.monotonic()-t}
 (E/'output_audit.json').write_text(json.dumps(o,indent=2)+'\n');s=json.loads((E/'review_summary.json').read_text());s['audit']={k:v for k,v in o.items() if k!='fresh_values'};s['audit_sha256']=sha(E/'output_audit.json');(E/'review_summary.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps({k:v for k,v in o.items() if k not in ('fresh_values',)}))
if __name__=='__main__':main()
