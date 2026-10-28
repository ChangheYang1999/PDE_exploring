"""Certify N <= I from exact D6 polynomials, then audit the complete cover."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import sys,json,time,hashlib
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;BASE=HERE.parents[1]
sys.path.insert(0,str(BASE/'02_energy/verification'))
import auxiliary_certificate as ac
from compact_matrix import A
ctx.prec=320;start=time.monotonic();raw,B,_,_=ac.load(131,'N');delta=Q(raw['delta'])
Lt,Rt=ac.cc.split_matrices(ac.cc.NT);Lz,Rz=ac.cc.split_matrices(ac.cc.NZ)
stack=[(B,Q(0),Q(1),Q(-1),Q(1),'')];accepted=[];bad=[]
while stack and time.monotonic()-start<420:
 b,tl,th,zl,zh,path=stack.pop();lo,_=ac.factored_bounds(b,tl,th,zl,zh,delta,arb(1))
 if lo.is_finite() and lo>=0:accepted.append({'path':path,'t':[str(tl),str(th)],'z':[str(zl),str(zh)],'lower':lo.str(50)})
 elif len(path)>=42:bad.append({'path':path,'lower':lo.str(30)})
 else:
  axis='t' if path.lower().count('t')<=path.lower().count('z')+2 else 'z'
  left,right=ac.cc.split(b,axis,Lt if axis=='t' else Lz,Rt if axis=='t' else Rz)
  if axis=='t':
   m=(tl+th)/2;stack.extend([(right,m,th,zl,zh,path+'T'),(left,tl,m,zl,zh,path+'t')])
  else:
   m=(zl+zh)/2;stack.extend([(right,tl,th,m,zh,path+'Z'),(left,tl,th,zl,m,path+'z')])
 if len(accepted)%100==0:print('leaves',len(accepted),'pending',len(stack),'seconds',time.monotonic()-start,flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'status':'COMPLETE' if not stack and not bad else 'INCOMPLETE','source_sha256':raw['input_sha256'],'target':'1','precision_bits':320,'accepted':accepted,'failed':bad,'pending':[x[-1] for x in stack]}
file=HERE/'state131_N1_certificate.json';file.write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],len(accepted),len(bad),len(stack),flush=True)
if out['status']!='COMPLETE':raise SystemExit(1)
ctx.prec=384;_,B,_,_=ac.load(131,'N');Lt,Rt=ac.cc.split_matrices(ac.cc.NT);Lz,Rz=ac.cc.split_matrices(ac.cc.NZ)
paths={v['path']:v for v in accepted};assert len(paths)==len(accepted);lows=[]
def visit(path,b,tl,th,zl,zh):
 if path in paths:
  row=paths[path];assert list(map(Q,row['t']))==[tl,th] and list(map(Q,row['z']))==[zl,zh]
  assert not any(p!=path and p.startswith(path) for p in paths)
  lo,_=ac.factored_bounds(b,tl,th,zl,zh,delta,arb(1));assert lo.is_finite() and lo>=0;lows.append(lo);return
 kids={p[len(path)] for p in paths if p.startswith(path)};assert kids in ({'t','T'},{'z','Z'})
 ax='t' if kids=={'t','T'} else 'z';left,right=ac.cc.split(b,ax,Lt if ax=='t' else Lz,Rt if ax=='t' else Rz)
 if ax=='t':
  m=(tl+th)/2;visit(path+'t',left,tl,m,zl,zh);visit(path+'T',right,m,th,zl,zh)
 else:
  m=(zl+zh)/2;visit(path+'z',left,tl,th,zl,m);visit(path+'Z',right,tl,th,m,zh)
visit('',B,Q(0),Q(1),Q(-1),Q(1));assert len(lows)==len(paths)
lo=lows[0]
for a in lows:lo=lo.min(a)
audit={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'verdict':'CONFIRMED','target':'N <= I','source_sha256':raw['input_sha256'],'precision_bits':384,'leaves':len(lows),'minimum_I_minus_N':lo.str(55),'certificate_sha256':hashlib.sha256(file.read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
(HERE/'state131_N1_audit.json').write_text(json.dumps(audit,indent=2)+'\n');print(json.dumps(audit,indent=2),flush=True)
