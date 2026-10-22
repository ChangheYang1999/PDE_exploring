"""Closed exact frequency-one projection and Arb512. No JS/TS, servers, RLScience, Lean/Lake."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/single_tail_hminus1_obstruction';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dec(s):
 neg=s.startswith('-');m,e=s.lstrip('+-').split('p');i,f=m[2:].split('.');q=Q(int(i+f,16),16**len(f))*Q(2)**int(e)
 return -q if neg else q
def aa(q):q=Q(q);return arb(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return Q(int(m))*Q(2)**int(e)
def box(x):
 assert x.is_finite();lo,hi=dy(x.lower()),dy(x.upper());assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':x.str(45)}
def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1;p=B/'data_exact/modal_v2.json';assert sha(p)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 raw=json.loads(p.read_text());arr=raw['arrays'];assert arr['Aout']['shape']==[260,10] and raw['outer_jl'][6]==[0,1]
 col=[dec(arr['Aout']['hex'][m*10+6]) for m in range(260)];k=dec(raw['scalars_hex']['k']);t=dec(arr['knots']['hex'][-1]);bo=dec(raw['scalars_hex']['bo']);assert 0<k<Q(1,4) and bo>120
 bd=(2*col[0]-col[2])/8;assert bd!=0;d=k-2;beta=2*k-1;a2=3*k-2;a3=4*k-3
 assert a3<d<a2<-1 and -2<d and a3<-2 and 2*k-3<a3 and k-4<a3
 exps=[k-j*(1-k)-2*l for j,l in raw['outer_jl']]+[3-bo]
 big=[(i,j,x+y-1) for i,x in enumerate(exps) for j,y in enumerate(exps) if x+y-1>a3];assert [(i,j) for i,j,x in big]==[(0,0),(0,1),(1,0)]
 assert all(x+y-1!=d for x in exps for y in exps)
 assert all(x-2*n-2<a3 for x in exps for n in range(1,523))
 Ld=aa(-2*bd/k)*aa((5-k)*t).exp()
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_NONZERO_REQUIRES_AUDIT','method':'Exact hex parser, closed projection (2A06-A26)/8, Arb512 exponential','bits':512,'seconds':time.monotonic()-start,'exact':{'k':str(k),'tplus':str(t),'bd':str(bd),'column6':list(map(str,col)),'d':str(d),'beta':str(beta),'a2':str(a2),'a3':str(a3),'large_ordered_pairs':[[i,j,str(x)] for i,j,x in big]},'values':{'bd':box(aa(bd)),'Ld':box(Ld),'scale':box(aa((5-k)*t).exp())},'files':{str(q.relative_to(B)):sha(q) for q in (p,D/'PROOF.md',Path(__file__))}}
 (E/'arb.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'bd':str(bd),'Ld':out['values']['Ld']['display'],'seconds':out['seconds']}))
if __name__=='__main__':main()
