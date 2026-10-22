"""Arb512 generating-function constants; no JS/TS, servers, RLScience, Lean/Lake."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,sys,time
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/tail_local_velocity';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=Q(q);return arb(q.numerator)/q.denominator
def dy(v):m,e=v.man_exp();return Q(int(m))*Q(2)**int(e)
def box(v):
 assert v.is_finite();lo,hi=dy(v.lower()),dy(v.upper());assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':v.str(40)}
def fall(n,j):
 r=1
 for i in range(j):r*=n-i
 return r
def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1
 p=B/'data_exact/modal_v2.json';assert sha(p)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 data=json.loads(p.read_text());k=Q(float.fromhex(data['scalars_hex']['k']));t=Q(float.fromhex(data['arrays']['knots']['hex'][-1]));beta=2*k-1
 old=B/'research/normalized_tail_repair/evidence/verdict.json';prior=json.loads(old.read_text());N=Q(prior['public_bounds']['N_upper']);assert N==Q('38.37961982')
 S=[];diffs=[]
 for j in range(4):
  row=[Q(fall(2*m+3,j)) for m in range(j+1)];first=[]
  while row:
   first.append(row[0]);row=[row[i+1]-row[i] for i in range(len(row)-1)]
  S.append(sum((v*Q(1,4)**l/(1-Q(1,4))**(l+1) for l,v in enumerate(first)),Q(0)));diffs.append(list(map(str,first)))
 C=[4*N*s/(3-beta) for s in S];decay=aa((beta-3))*arb(3000).log();power=decay.exp()
 values={**{'C'+str(j):aa(c) for j,c in enumerate(C)},'u9':aa(C[0]*9**3)*power,'w9':aa(C[1]*9**2)*power,'power3000':power,'R_b':aa(t).exp()}
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_AUDIT','method':'Arb512; exact Newton differences for rational geometric sums; exp((beta-3)log3000)','seconds':time.monotonic()-start,'exact':{'k':str(k),'tplus':str(t),'N':str(N),'beta':str(beta),'S':list(map(str,S)),'C':list(map(str,C)),'differences':diffs},'values':{s:box(v) for s,v in values.items()},'files':{str(x.relative_to(B)):sha(x) for x in (p,old,D/'PROOF.md',Path(__file__))}}
 (E/'arb.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','seconds')}));print(json.dumps({k:v['display'] for k,v in out['values'].items()}))
if __name__=='__main__':main()
