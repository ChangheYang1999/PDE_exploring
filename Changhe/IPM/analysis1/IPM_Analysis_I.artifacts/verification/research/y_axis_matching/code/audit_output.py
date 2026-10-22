"""Fresh1536-bit moments and log-form endpoint values, exact output audit."""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import sys,json,hashlib,time,math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,fmpq,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/y_axis_matching/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(z):z=F(z);return arb(fmpq(z.numerator,z.denominator))
def bounds(z):
 def dyad(m,e):return F(int(m))*F(2)**int(e)
 return tuple(dyad(*v.man_exp()) for v in (z.lower(),z.upper()))
def record(z):l,u=bounds(z);return {'lower_exact':str(l),'upper_exact':str(u),'display':[float(l),float(u)]}
def main():
 start=time.monotonic();ctx.prec=1536;ctx.threads=1;r=json.loads((E/'checks.json').read_text());assert r['status']=='PASS'
 assert r['code_sha256']==sha(B/'research/y_axis_matching/code/check_jets.py') and r['proof_sha256']==sha(B/'research/y_axis_matching/PROOF.md')
 rawp=B/'data_exact/modal_v2.json';assert r['data_sha256']==sha(rawp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 raw=json.loads(rawp.read_text());sig,e=raw['scalars_hex']['k'].split('p');lft,rgt=sig[2:].split('.');k=F(int(lft+rgt,16))*F(2)**(int(e)-4*len(rgt));assert k==F(1615536043799051,9007199254740992)
 cl=1/k;A=2*cl-1;D=4*cl-1;p2=2-1/D;g=F(1129,1000);s=F(153,50)
 exact={'k':k,'c_l':cl,'A':A,'D':D,'p1':F(1),'p2':p2,'p2_Sobolev_threshold':p2+F(1,2),'s':s,'gamma':g,'far_Hardy_margin':1+k-g,'jet1_rate':D*(s-F(3,2)),'jet2_rate':D*(s-F(5,2))+1,'local_matching_power':3-p2}
 assert {n:str(v) for n,v in exact.items()}==r['exact_parameters']
 counts=0;vals={};traces={};bare={}
 def contain(value,one,two):
  nonlocal counts
  ll,uu=bounds(value)
  for row in [one,two]:assert F(row['lower_exact'])<=ll<=uu<=F(row['upper_exact']);counts+=1
 for n,v in exact.items():
  fresh=aa(v);contain(fresh,r['values']['arb'][n],r['values']['iv'][n]);vals[n]=record(fresh)
 # Independent integration-by-parts recurrence for the polynomial trace moments.
 for ka in [1,4,16]:
  kap=aa(ka);end=(-kap).exp();J=[(1-end)/kap]
  for n in range(1,19):J.append((n*J[-1]-end)/kap)
  val=kap*sum(((-1)**j*math.comb(8,j)*J[2+2*j] for j in range(9)),arb(0))
  contain(val,r['trace_integrals']['arb'][str(ka)],r['trace_integrals']['iv'][str(ka)]);assert 0<bounds(val)[0]<bounds(val)[1]<F(2,ka*ka);traces[str(ka)]=record(val)
 for d in [F(1,10),F(1,100),F(1,1000)]:
  dd=aa(d);logratio=-3*(1+dd*dd).log()+aa((p2-k+4)/2)*(1+aa(cl/D)*dd*dd).log()
  vals2={'scaled':-logratio.exp(),'integral':-(logratio+aa(1-p2)*dd.log()).exp()};bare[str(d)]={}
  for n,val in vals2.items():contain(val,r['bare_matching_example']['arb'][str(d)][n],r['bare_matching_example']['iv'][str(d)][n]);bare[str(d)][n]=record(val)
 assert len(r['exact_identities'])==24 and set(r['exact_identities'].values())=={'0'} and counts==44
 o={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','code_sha256':sha(__file__),'check_code_sha256':r['code_sha256'],'proof_sha256':r['proof_sha256'],'checks_sha256':sha(E/'checks.json'),'fresh_containments':counts,'fresh_values':vals,'fresh_trace_integrals':traces,'fresh_bare_examples':bare,'method':'Arb1536 integration-by-parts recurrence and exponential of log formulas; independent exact hex parse and rational parameter derivation.','seconds':time.monotonic()-start,'scope':'Illustrative outputs and provenance, not coupled Fredholm data.'}
 (E/'output_audit.json').write_text(json.dumps(o,indent=2)+'\n');summary=json.loads((E/'review_summary.json').read_text());summary['audit_sha256']=sha(E/'output_audit.json');summary['audit']={k:v for k,v in o.items() if k not in ['fresh_values','fresh_trace_integrals','fresh_bare_examples']};(E/'review_summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in o.items() if k in ['utc','status','seconds','fresh_containments']}))
if __name__=='__main__':main()
