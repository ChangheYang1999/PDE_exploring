"""Fresh1536-bit Cauchy-Schwarz and radial-integral constant audit."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx,fmpq
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/pure_source/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(z):z=F(z);return arb(fmpq(z.numerator,z.denominator))
def ends(z):
 def dyad(m,e):return F(int(m))*F(2)**int(e)
 return tuple(dyad(*v.man_exp()) for v in (z.lower(),z.upper()))
def rec(z):l,u=ends(z);return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def main():
 start=time.monotonic();ctx.prec=1536;ctx.threads=1;r=json.loads((E/'checks.json').read_text());assert r['status']=='PASS' and r['code_sha256']==sha(B/'research/pure_source/code/check_source.py') and r['proof_sha256']==sha(B/'research/pure_source/PROOF.md')
 raw=B/'data_exact/modal_v2.json';assert sha(raw)==r['data_sha256']=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6';sig,e=json.loads(raw.read_text())['scalars_hex']['k'].split('p');lft,rgt=sig[2:].split('.');k=F(int(lft+rgt,16))*F(2)**(int(e)-4*len(rgt));assert k==F(1615536043799051,9007199254740992)
 A=(2-k)/k;beta=(A-3)/A;exact={'k':k,'c_l':1/k,'A':A,'jump':-1/A,'radial_exponent':(3-2*A)/A,'divergence_power':beta,'boundary_vanishing_power':2/A,'delta':F(1,2),'sigma':F(153,50)};assert r['exact_parameters']=={n:str(v) for n,v in exact.items()}
 vals={n:aa(v) for n,v in exact.items()};l2=aa(4).log()/2;l10=aa(100).log()/2;a=(-l2/aa(A)).exp();ang=3*a**3/(1-a**3/8);pref=ang/aa(A)**4;vals.update({'log2':l2,'log10':l10,'angular_CS_lower':ang,'norm_prefactor_lower':pref,'axis_cutoff_a':a})
 for m in [1,2,3]:
  ratio=aa(F(10**m,2));integral=(aa(beta)*l2).exp()*((aa(beta)*ratio.log()).exp()-1)/aa(beta);vals['annulus_lower_'+str(m)]=pref*integral
 count=0
 for n,v in vals.items():
  l,u=ends(v)
  for method in ['arb','iv']:
   row=r['values'][method][n];assert F(row['lower_exact'])<=l<=u<=F(row['upper_exact']);count+=1
 assert count==34 and len(r['exact_identities'])==15 and set(r['exact_identities'].values())=={'0'}
 o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'check_code_sha256':r['code_sha256'],'proof_sha256':r['proof_sha256'],'checks_sha256':sha(E/'checks.json'),'fresh_containments':count,'fresh_values':{n:rec(v) for n,v in vals.items()},'method':'Arb1536 alternate CS factor3a3/(1-a3/8), ratio form of finite radial integral, squared-argument logarithms and independent exact hex parse.','seconds':time.monotonic()-start,'scope':'Illustrative lower-bound constants only.'}
 (E/'output_audit.json').write_text(json.dumps(o,indent=2)+'\n');s=json.loads((E/'review_summary.json').read_text());s['audit_sha256']=sha(E/'output_audit.json');s['audit']={k:v for k,v in o.items() if k!='fresh_values'};(E/'review_summary.json').write_text(json.dumps(s,indent=2)+'\n');print(json.dumps({k:v for k,v in o.items() if k in ['utc','status','seconds','fresh_containments']}))
if __name__=='__main__':main()
