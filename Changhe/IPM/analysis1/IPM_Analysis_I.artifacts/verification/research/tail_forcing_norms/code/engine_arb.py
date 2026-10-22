"""Exact rational antiderivatives and Arb512 balls. No JS/TS, servers, RLScience, Lean/Lake."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import json,hashlib,sys,time
from fractions import Fraction as Q
from pathlib import Path
from datetime import datetime,timezone
from flint import arb,ctx
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/tail_forcing_norms';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def aa(q):q=Q(q);return arb(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return Q(int(m))*Q(2)**int(e)
def box(x):
 assert x.is_finite();lo,hi=dy(x.lower()),dy(x.upper());assert lo<=hi
 return {'lower_exact':str(lo),'upper_exact':str(hi),'display':x.str(45)}
def mul(p,q):
 r=[Q(0)]*(len(p)+len(q)-1)
 for i,x in enumerate(p):
  for j,y in enumerate(q):r[i+j]+=x*y
 return r
def main():
 start=time.monotonic();ctx.prec=512;ctx.threads=1
 inp=B/'data_exact/modal_v2.json';assert sha(inp)=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
 data=json.loads(inp.read_text());k=Q(float.fromhex(data['scalars_hex']['k']));assert k==Q(1615536043799051,9007199254740992) and 0<k<Q(1,4)
 a,b=Q(1,4),Q(1,2);g=mul(mul([-a,1],[-a,1]),mul([b,-1],[b,-1]));gp=[i*g[i] for i in range(1,len(g))];g2=mul(g,g);gp2=mul(gp,gp)
 A=sum((q*(b**(i+2)-a**(i+2))/(i+2) for i,q in enumerate(g2)),Q(0));Bg=sum((q*(b**(i+2)-a**(i+2))/(i+2) for i,q in enumerate(gp2)),Q(0))
 Bang_r=sum((g2[i]*(b**i-a**i)/i for i in range(1,len(g2))),Q(0));Bang_log=g2[0];Bval=aa(Bg+Bang_r)+aa(Bang_log)*arb(2).log()
 J=arb(0)
 for i,q in enumerate(g):
  power=2*k+i+1;assert power>0
  J+=aa(q)*(aa(b)**aa(power)-aa(a)**aa(power))/aa(power)
 old=B/'research/far_residual_obstruction/evidence/arb.json';record=json.loads(old.read_text())['values']['E0'];lo,hi=Q(record['lower_exact']),Q(record['upper_exact']);assert lo<=hi<0;E0=aa(lo).union(aa(hi));mag=-E0
 CL=arb.pi().sqrt()*mag*J/aa(A).sqrt();CD=arb.pi().sqrt()*mag*J/Bval.sqrt()
 values={'A':aa(A),'B':Bval,'J':J,'C_L':CL,'C_D':CD,'E0':E0};assert all(values[x]>0 for x in ('A','B','J','C_L','C_D'))
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_REQUIRES_OUTPUT_AUDIT','method':'Arb512 exact expanded polynomial power antiderivatives','bits':512,'seconds':time.monotonic()-start,'exact':{'k':str(k),'g':list(map(str,g)),'A':str(A),'B_rational':str(Bg+Bang_r),'B_log2':str(Bang_log)},'values':{key:box(v) for key,v in values.items()},'files':{str(p.relative_to(B)):sha(p) for p in (inp,old,Path(__file__),D/'PROOF.md')}}
 (E/'arb.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','seconds')}));print(json.dumps({k:v['display'] for k,v in out['values'].items()}))
if __name__=='__main__':main()
