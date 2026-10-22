"""Fresh high-precision outputs and exact provenance for the conditional theorem."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,fmpq,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/far_domain/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ends(q):
 def dyad(m,e):return F(int(m))*F(2)**int(e)
 return tuple(dyad(*v.man_exp()) for v in (q.lower(),q.upper()))
def main():
 start=time.monotonic();ctx.prec=1536;ctx.threads=1;r=json.loads((E/'checks.json').read_text());assert r['status']=='PASS'
 assert r['code_sha256']==sha(B/'research/far_domain/code/check_domain.py') and r['proof_sha256']==sha(B/'research/far_domain/PROOF.md')
 assert r['data_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 # Fresh raw IEEE hexadecimal parse for k, not main Fraction.from_float path.
 raw=json.loads((B/'data_exact/modal_v2.json').read_text());h=raw['scalars_hex']['k'];sig,ex=h.split('p');left,right=sig[2:].split('.');k=F(int(left+right,16))*F(2)**(int(ex)-4*len(right));assert k==F(1615536043799051,9007199254740992)
 gamma=F(1129,1000);eps=F(1,10);cl=1/k
 exact={'k':k,'gamma':gamma,'c_l':cl,'epsilon':eps,'far_threshold_margin':1+k-gamma,'flow_growth_rate':1+cl-gamma*(cl+eps),'transport_rate':1-cl*(gamma-1),'Hardy_E_constant':1/(gamma-1),'Hardy_K_constant':1/(2-gamma),'kernel_safe_constant_rational':F(4)}
 assert {k:str(v) for k,v in exact.items()}==r['exact_parameters']
 assert exact['flow_growth_rate']>0 and 0<gamma-1<k<1
 # Atan expression is independent of Arb.pi. Negative exp instead of reciprocal positive exp.
 pi=16*aa(F(1,5)).atan()-4*aa(F(1,239)).atan()
 fresh={k:aa(v) for k,v in exact.items()};fresh.update(explicit_strain_lower=aa(F(4225,235298))*aa(F(-32,3)).exp()/pi,velocity_tail_constant=4/pi,component_vector_constant=aa(8).sqrt()/pi)
 checks=0;records={}
 for name,value in fresh.items():
  l,u=ends(value);records[name]={'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
  for method in ['arb','iv']:
   row=r['values'][method][name];ol,ou=F(row['lower_exact']),F(row['upper_exact']);assert ol<=l<=u<=ou,(name,method);checks+=1
 assert ends(fresh['explicit_strain_lower'])[0]>F('0.000000133')
 assert len(r['exact_identities'])==12 and set(r['exact_identities'].values())=={'0'}
 # Exact box arithmetic and all four reflected quadrants.
 q=F(5,4)**2*(3*F(5,4)**2-F(7,4)**2)**2/(2*F(7,4)**2)**3;assert q==F(4225,235298)
 assert 4*(F(7,4)-F(5,4))**2==1 and (F(5,4)-1)*(2-F(5,4))==F(3,16)
 o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'check_code_sha256':r['code_sha256'],'proof_sha256':r['proof_sha256'],'checks_sha256':sha(E/'checks.json'),'fresh_containments':checks,'fresh_values':records,'method':'Fresh Arb1536 atan Machin identity, negative exponential, exact hex digit parse, rational parameter/box reconstruction.','seconds':time.monotonic()-start,'scope':'Numerical illustrative constants and stored-output audit only; analytic hypotheses remain conditional.'}
 (E/'output_audit.json').write_text(json.dumps(o,indent=2)+'\n');s=json.loads((E/'review_summary.json').read_text());s['audit_sha256']=sha(E/'output_audit.json');s['audit']={k:v for k,v in o.items() if k not in ['fresh_values']};(E/'review_summary.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps({k:v for k,v in o.items() if k in ['utc','status','fresh_containments','seconds']}))
if __name__=='__main__':main()
