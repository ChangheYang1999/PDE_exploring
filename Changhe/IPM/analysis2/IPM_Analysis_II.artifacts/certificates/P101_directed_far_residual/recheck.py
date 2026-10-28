"""Direct angular power restriction, without producer's subdivision matrices."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from hashlib import sha256
from datetime import datetime,timezone
import json,sys,time
from flint import arb,arb_mat,ctx
here=Path(__file__).parent;sys.set_int_max_str_digits(0)
def A(v):
 q=F(v);return arb(q.numerator)/q.denominator
def main(name):
 ctx.prec=512;start=time.monotonic();path=here/name;cert=json.loads(path.read_text());src=here/'sectors.json';data=json.loads(src.read_text());assert cert['status']=='COMPLETE' and not cert['failed'] and not cert['pending_paths'];assert cert['source_sha256']==sha256(src.read_bytes()).hexdigest();assert cert['epsilon_upper_rational']==data['epsilon_upper_rational'];target=F(cert['target'])-F(data['epsilon_upper_rational']);rows=data['rows'];degree=max(int(k) for p in rows for k in p['P']);P=arb_mat(len(rows),degree+1)
 for j,row in enumerate(rows):
  for k,v in row['P'].items():P[j,int(k)]=A(v)
 paths={row['path'] for row in cert['accepted']};assert len(paths)==len(cert['accepted']);tree={}
 for p in paths:
  node=tree
  for ch in p:assert 'leaf' not in node;node=node.setdefault(ch,{})
  assert not node;node['leaf']=True
 def complete(node):
  if 'leaf' in node:assert len(node)==1;return
  assert set(node) in ({'t','T'},{'z','Z'})
  for v in node.values():complete(v)
 complete(tree);checks=[]
 for index,leaf in enumerate(cert['accepted']):
  tl,th,zl,zh=F(0),F(1),F(-1),F(1)
  for ch in leaf['path']:
   if ch=='t':th=(tl+th)/2
   elif ch=='T':tl=(tl+th)/2
   elif ch=='z':zh=(zl+zh)/2
   else:assert ch=='Z';zl=(zl+zh)/2
  assert list(map(str,(tl,th)))==leaf['t'] and list(map(str,(zl,zh)))==leaf['z']
  # First substitute z=zl+(zh-zl)v in monomials, then elevate powers to Bernstein.
  S=arb_mat(degree+1,degree+1);B=arb_mat(degree+1,degree+1)
  for k in range(degree+1):
   for j in range(k+1):S[k,j]=A(comb(k,j)*zl**(k-j)*(zh-zl)**j)
  for j in range(degree+1):
   for i in range(j,degree+1):B[j,i]=A(F(comb(i,j),comb(degree,j)))
  local=P*S*B;weights=[]
  for row in rows:
   a=F(row['a'])
   if not a:weights.append(arb(1))
   else:
    lo=A(tl/data['R'])**A(a) if tl else arb(0);hi=A(th/data['R'])**A(a);weights.append(lo.union(hi))
  vals=(arb_mat([weights])*local).entries();upper=max((abs(v) for v in vals),key=lambda x:float(x.upper()))
  # Avoid ordering balls by a rounded diagnostic: merge the complete set.
  for v in vals:upper=upper.max(abs(v))
  upper*=((1-A(zl))/2).sqrt();assert upper<=A(target),(index,leaf['path'],upper,A(target));checks.append({'path':leaf['path'],'upper':upper.str(100)})
  if (index+1)%100==0:print(index+1,'rechecked',time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'leaves':len(checks),'checks':checks,'certificate_sha256':sha256(path.read_bytes()).hexdigest(),'sectors_sha256':sha256(src.read_bytes()).hexdigest(),'precision_bits':ctx.prec,'seconds':time.monotonic()-start};dest=path.with_suffix('.recheck.json');dest.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],len(checks),'PASS',out['seconds'],flush=True)
if __name__=='__main__':main(sys.argv[1])
