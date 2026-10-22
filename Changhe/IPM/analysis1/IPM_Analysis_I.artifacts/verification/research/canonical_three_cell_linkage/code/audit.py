"""Independent integer-bit and signed-frequency full saved-record audit."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from collections import defaultdict
import struct,hashlib,json,time
import numpy as np
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_three_cell_linkage';E=D/'evidence'
def require(v,s):
 if not v:raise ValueError(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def b64(x):
 u=struct.unpack('>Q',struct.pack('>d',x))[0];s=u>>63;e=(u>>52)&2047;f=u&((1<<52)-1);require(e!=2047,'finite binary64')
 return (-1 if s else 1)*Q(f if e==0 else (1<<52)+f)*Q(2)**(-1074 if e==0 else e-1075)
def exp_interval(x):
 q=abs(x);require(q<32,'exact finite series ratio bound');term=Q(1);s=term
 for k in range(1,129):term=term*q/k;s+=term
 tail=(term*q/129)/(1-q/130);require(s>0 and tail>=0,'positive rational exponential bound')
 return (1/(s+tail),1/s) if x<0 else (s,s+tail)
def main():
 start=datetime.now(timezone.utc).isoformat();timer=time.monotonic();c=load(E/'checks.json');require(c['status']=='PASS_COMPLETE_SELECTED_CANONICAL_INPUT_BINDINGS_CONDITIONAL_ON_ARCHIVE_MOMENTS','actual first checker')
 pins={}
 for n,h in c['files'].items():
  p=Path(n);p=p if p.is_absolute() else B/p;require(sha(p)==h,'unchanged first-check pin '+n);pins[n]=h
 require(c['source_sha256']==sha(D/'code/check.py') and c['forcing_stream_sha256']==sha(E/'forcing_records.jsonl'),'actual full first output')
 linear=[defaultdict(Q) for _ in range(262)];deriv=[defaultdict(Q) for _ in range(262)]
 for m in range(260):
  for f in [2*m+1,1-2*m,2*m+3,3-2*m]:
   j=(abs(f)-1)//2;v=Q(1 if f>0 else -1,8)
   for n,factor in [(j+1,2-(j+1)),(j,2+j)]:
    if 1<=n<=261:linear[n][m]+=factor*v;deriv[n][m]+=v/2
 for table in [linear,deriv]:
  for n in range(1,262):table[n]={m:w for m,w in table[n].items() if w}
 count=0;decoded=0;expo=[];margin=None;geom=load(B/'research/middle_residual/evidence/partition_exact.json')
 with (E/'forcing_records.jsonl').open() as stream:
  for ci,cell in zip([0,4102,7808],c['cells'],strict=True):
   require(cell['cell']==ci,'exact selected cell order');p=B/'research/radial_tm_instance/evidence'/('selected_v3_cell_%04d.npz'%ci)
   with np.load(p,allow_pickle=False) as z:
    T=[[b64(x) for x in row] for row in z['T_mid']];rad=[[b64(x) for x in row] for row in z['T_rad']];fm=[[b64(x) for x in row] for row in z['F_mid']];fr=[[b64(x) for x in row] for row in z['F_rad']];sc=[b64(x) for x in z['scalar']]
   decoded+=2*8*260+2*261*8+36
   parent=geom['spans'][cell['parent']];a,b=Q(parent['a_exact']),Q(parent['b_exact']);q=ci-parent['first_cell'];left=((parent['count']-q)*a+q*b)/parent['count'];right=((parent['count']-q-1)*a+(q+1)*b)/parent['count'];require(Q(cell['left_exact'])==left and Q(cell['right_exact'])==right and a<=left<right<=b and right-left<=sc[0],'independent exact barycentric coordinates')
   lo,hi=exp_interval(left);require(sc[1]-sc[2]<=lo<=hi<=sc[1]+sc[2] and sc[1]-sc[2]>0,'independent rational E containment');expo.append({'cell':ci,'left_exact':str(left),'series_terms':129,'lower':str(lo),'upper':str(hi),'target_lower':str(sc[1]-sc[2]),'target_upper':str(sc[1]+sc[2])})
   for n in range(1,262):
    for k in range(8):
     center=sum((w*T[k][m] for m,w in linear[n].items()),Q(0));radius=sum((abs(w)*rad[k][m] for m,w in linear[n].items()),Q(0))
     if k<7:
      center+=(k+1)*sum((w*T[k+1][m] for m,w in deriv[n].items()),Q(0));radius+=(k+1)*sum((abs(w)*rad[k+1][m] for m,w in deriv[n].items()),Q(0))
     exactvalues={'image_lower':center-radius,'image_upper':center+radius,'target_lower':fm[n-1][k]-fr[n-1][k],'target_upper':fm[n-1][k]+fr[n-1][k]};v=min(exactvalues['image_lower']-exactvalues['target_lower'],exactvalues['target_upper']-exactvalues['image_upper']);require(v>=0,'fresh exact whole-box containment');exactvalues['margin']=v
     text=next(stream);require(text.endswith('\n'),'complete saved line');r=json.loads(text);require(set(r)=={'cell','n','k'}|set(exactvalues) and (r['cell'],r['n'],r['k'])==(ci,n,k),'exact record set/order')
     for name,val in exactvalues.items():require(Q(r[name])==val,'independent full endpoint recomputation '+name)
     count+=1;margin=v if margin is None else min(margin,v)
  require(stream.read()=='','no extra records')
 require(count==6264 and decoded==25116 and len(expo)==3,'complete independent counts');require(Q(c['forcing_worst']['margin'])==margin,'actual worst margin')
 for p in [D/'PROOF.md',D/'AUDIT_METHOD.md',D/'code/check.py',Path(__file__),E/'checks.json',E/'forcing_records.jsonl']:
  name=str(p.relative_to(B));h=sha(p);require(name not in pins or pins[name]==h,'unchanged audited pin');pins[name]=h
 out={'start_utc':start,'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_ALL_SELECTED_F_RECORDS_AND_RATIONAL_E','source_sha256':sha(__file__),'checks_sha256':sha(E/'checks.json'),'forcing_stream_sha256':sha(E/'forcing_records.jsonl'),'saved_records_recomputed':count,'independent_endpoint_equalities':5*count,'binary64_values_decoded':decoded,'exact_E_containments':3,'rational_E_enclosures':expo,'smallest_F_margin':str(margin),'seconds':time.monotonic()-timer,'files':dict(sorted(pins.items()))}
 with (E/'audit.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
 print(json.dumps({k:out[k] for k in ['utc','status','saved_records_recomputed','independent_endpoint_equalities','binary64_values_decoded','exact_E_containments','seconds']}))
if __name__=='__main__':main()
