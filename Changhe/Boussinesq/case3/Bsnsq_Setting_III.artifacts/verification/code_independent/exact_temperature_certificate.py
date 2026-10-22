"""Reusable exact JSON / rational Bernstein certificate for b=3 temperatures.

All signs and bounds use Fraction arithmetic. Floats only choose a subdivision
axis and report progress. No solver code, server or JavaScript is used.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import comb,isqrt
from datetime import datetime,timezone
import json,hashlib,time,sys,argparse,resource
resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
Z=Q(0)

def polyadd(a,b):
 out=dict(a)
 for key,v in b.items():out[key]=out.get(key,Z)+v
 return {key:v for key,v in out.items() if v}
def polymul(a,b):
 out={}
 for (i,j),v in a.items():
  for (k,l),w in b.items():out[i+k,j+l]=out.get((i+k,j+l),Z)+v*w
 return {key:v for key,v in out.items() if v}
def polyscale(a,q):return {key:v*q for key,v in a.items() if v*q}
def polydiff(a,axis):
 out={}
 for (i,j),v in a.items():
  if axis==0 and i:out[i-1,j]=v*i
  if axis==1 and j:out[i,j-1]=v*j
 return out
def polypow(a,n):
 out={(0,0):Q(1)}
 for _ in range(n):out=polymul(out,a)
 return out

def spline_span(data,span):
 """Independent exact Cox recursion on t=A+width*u, one positive knot span."""
 knots=[Q(x) for x in data['knots']];degree=data['degree'];A=knots[span];B=knots[span+1];width=B-A
 assert width>0
 base={span:{(0,0):Q(1)}}
 for d in range(1,degree+1):
  nxt={}
  for i in range(span-d,span+1):
   ans={}
   if i in base and knots[i+d]!=knots[i]:
    factor={(0,0):(A-knots[i])/(knots[i+d]-knots[i]),(1,0):width/(knots[i+d]-knots[i])}
    ans=polyadd(ans,polymul(factor,base[i]))
   if i+1 in base and knots[i+d+1]!=knots[i+1]:
    factor={(0,0):(knots[i+d+1]-A)/(knots[i+d+1]-knots[i+1]),(1,0):-width/(knots[i+d+1]-knots[i+1])}
    ans=polyadd(ans,polymul(factor,base[i+1]))
   nxt[i]=ans
  base=nxt
 polys=[]
 for coeff in data['coefficients']:
  p={}
  for i,part in base.items():p=polyadd(p,polyscale(part,Q(coeff[i])))
  polys.append(p)
 # Basis partition of unity is checked exactly for each supplied knot span.
 partition={}
 for part in base.values():partition=polyadd(partition,part)
 assert partition=={(0,0):Q(1)}
 return A,B,polys

def span_fields(data,span):
 A,B,radial=spline_span(data,span)
 cheb=[{(0,0):Q(1)},{(0,1):Q(1)}]
 for k in range(2,len(radial)):cheb.append(polyadd(polyscale(polymul(cheb[1],cheb[-1]),Q(2)),polyscale(cheb[-2],Q(-1))))
 E={};O={}
 for k,p in enumerate(radial):
  if k%2:O=polyadd(O,polymul(p,cheb[k]))
  else:E=polyadd(E,polymul(p,cheb[k]))
 z={(0,0):1-A,(1,0):A-B};z6=polypow(z,6);one_minus_z6=polyadd({(0,0):Q(1)},polyscale(z6,Q(-1)))
 radialfac=polyscale(polymul(z,one_minus_z6),Q(1,3)/(B-A));envelope=polyscale(one_minus_z6,Q(-5,3))
 angfac={(0,0):Q(1),(0,2):Q(-1)};minus_eta={(0,1):Q(-1)}
 def differentiated(p,odd):
  q=polyadd(polymul(radialfac,polydiff(p,0)),polymul(envelope,p));q=polyadd(q,polymul(minus_eta,polydiff(p,1)))
  if odd:q=polyadd(q,polymul(z6,p))
  return polyadd(polyscale(p,Q(2)),polymul(angfac,q))
 return A,B,(E,O,differentiated(E,False),differentiated(O,True))

def tobern(poly,n,m):
 """u unchanged; eta=-1+2v, then exact power-to-Bernstein in each coordinate."""
 power=[[Z for _ in range(m+1)] for _ in range(n+1)]
 for (i,j),val in poly.items():
  for b in range(j+1):power[i][b]+=val*comb(j,b)*2**b*(-1)**(j-b)
 first=[[sum((power[a][j]*Q(comb(i,a),comb(n,a)) for a in range(i+1)),Z) for j in range(m+1)] for i in range(n+1)]
 return [[sum((first[i][b]*Q(comb(j,b),comb(m,b)) for b in range(j+1)),Z) for j in range(m+1)] for i in range(n+1)]

def coefficients(data,span):
 A,B,fields=span_fields(data,span);ans=[]
 for p,q in [fields[:2],fields[2:]]:
  both=list(p)+list(q);n=max([a for a,b in both]+[0]);m=max([b for a,b in both]+[0]);ans.extend([tobern(p,n,m),tobern(q,n,m)])
 return A,B,ans

def splitvec(v):
 tmp=list(v);left=[tmp[0]];right=[tmp[-1]]
 while len(tmp)>1:
  tmp=[(tmp[i]+tmp[i+1])/2 for i in range(len(tmp)-1)];left.append(tmp[0]);right.append(tmp[-1])
 return left,list(reversed(right))
def splitmat(a,axis):
 if axis==1:
  pieces=[splitvec(row) for row in a];return [p[0] for p in pieces],[p[1] for p in pieces]
 cols=[splitvec([row[j] for row in a]) for j in range(len(a[0]))]
 return [[cols[j][0][i] for j in range(len(cols))] for i in range(len(a))],[[cols[j][1][i] for j in range(len(cols))] for i in range(len(a))]

def sqrtbounds(q,bits=90):
 assert q>=0
 d=1<<bits;v=isqrt(q.numerator*d*d//q.denominator)
 lo=Q(v,d);hi=Q(v+1,d)
 assert lo*lo<=q<=hi*hi
 return lo,hi

def boundfields(mats,ta,tb):
 lo=sqrtbounds(1-(1-ta)**6)[0];hi=sqrtbounds(1-(1-tb)**6)[1]
 out=[]
 for E,O in [mats[:2],mats[2:]]:
  low=min(min(e+lo*o,e+hi*o) for er,orr in zip(E,O) for e,o in zip(er,orr))
  high=max(max(e+lo*o,e+hi*o) for er,orr in zip(E,O) for e,o in zip(er,orr))
  out.append((low,high))
 return out

def choose_axis(mats,ta,tb):
 # Heuristic only, never used to certify a sign.
 scores=[0.,0.]
 for mat in mats:
  scale=max([abs(float(q)) for row in mat for q in row]+[1e-100])
  for axis in [0,1]:
   if axis==0:vals=[abs(float(mat[i+1][j]-mat[i][j])) for i in range(len(mat)-1) for j in range(len(mat[0]))]
   else:vals=[abs(float(row[j+1]-row[j])) for row in mat for j in range(len(row)-1)]
   scores[axis]+=max(vals,default=0.)/scale
 # Source rho uncertainty enters only radial subdivision.
 scores[0]+=float(sqrtbounds(1-(1-tb)**6)[1]-sqrtbounds(1-(1-ta)**6)[0])
 return 0 if scores[0]>=scores[1] else 1

def certify(mats,ta,tb,depth,maxdepth,stats):
 stats['visited']+=1;bnd=boundfields(mats,ta,tb)
 if stats['visited']>stats.get('node_budget',200000) or time.monotonic()>stats.get('deadline',float('inf')):
  return {'open_budget':[[str(a),str(b)] for a,b in bnd]}
 if all(lo>0 for lo,hi in bnd):
  stats['leaves']+=1;stats['max_depth']=max(stats['max_depth'],depth)
  return {'positive':[str(v[0]) for v in bnd]}
 if any(hi<0 for lo,hi in bnd):return {'negative_box':[[str(a),str(b)] for a,b in bnd]}
 if depth>=maxdepth:return {'open':[[str(a),str(b)] for a,b in bnd]}
 axis=choose_axis(mats,ta,tb);pieces=[splitmat(a,axis) for a in mats];mid=(ta+tb)/2
 left=certify([p[0] for p in pieces],ta,mid if axis==0 else tb,depth+1,maxdepth,stats)
 right=certify([p[1] for p in pieces],mid if axis==0 else ta,tb,depth+1,maxdepth,stats)
 return {'axis':axis,'left':left,'right':right}

def audit_tree(mats,ta,tb,tree,stats,depth=0):
 assert depth<=512
 if 'axis' in tree:
  axis=tree['axis'];assert axis in[0,1];pieces=[splitmat(a,axis) for a in mats];mid=(ta+tb)/2
  a=audit_tree([p[0] for p in pieces],ta,mid if axis==0 else tb,tree['left'],stats,depth+1)
  b=audit_tree([p[1] for p in pieces],mid if axis==0 else ta,tb,tree['right'],stats,depth+1)
  return a and b
 b=boundfields(mats,ta,tb);stats['leaves']+=1
 return 'positive' in tree and all(lo>0 for lo,hi in b)

def verify_archive_input(data):
 """Tie the exact JSON to raw NPZ arrays without importing the field reader."""
 import numpy as np
 archive=Path(data['archive_path']);assert hashlib.sha256(archive.read_bytes()).hexdigest()==data['archive_sha256']
 with np.load(archive,allow_pickle=False) as a:
  degree=int(a['deg']);K=int(a['K']);Nt=int(a['Nt']);grade=float(a['grade'])
  assert degree==data['degree'] and K==len(data['coefficients'])
  assert float(a['beta_basis'])==3 and str(a['rmap'].item())=='r2'
  assert Q(data['L'])==Q.from_float(float(a['L']))
  knots=np.concatenate((np.zeros(degree),np.linspace(0,1,Nt+1)**grade,np.ones(degree)))
  assert [Q(t) for t in data['knots']]==[Q.from_float(float(t)) for t in knots]
  raw=a['cF'].reshape(K,len(knots)-degree-1)
  for k in range(K):
   for j in range(raw.shape[1]):assert Q(data['coefficients'][k][j])==(Q(0) if j<k//2 else Q.from_float(float(raw[k,j])))
 return data['archive_sha256']

def load_input(path):
 data=json.loads(path.read_text());assert data['basis_exponent']=='3';assert Q(data['L'])>0
 knots=[Q(q) for q in data['knots']];assert knots[0]==0 and knots[-1]==1 and all(a<=b for a,b in zip(knots,knots[1:]));degree=data['degree']
 assert isinstance(degree,int) and degree>=1 and data['coefficients']
 # At most degree-1 repeated interior knots ensures at least C1.
 assert all(knots.count(q)<=degree-1 for q in set(knots) if 0<q<1)
 assert all(len(c)==len(knots)-degree-1 for c in data['coefficients'])
 # The exact mask gives the stipulated center zeros for clamped splines.
 assert knots[:degree+1]==[0]*(degree+1) and knots[-degree-1:]==[1]*(degree+1)
 assert knots[degree+1]>0 and knots[-degree-2]<1
 for k,c in enumerate(data['coefficients']):assert all(Q(v)==0 for v in c[:k//2])
 spans=[i for i in range(degree,len(knots)-degree-1) if knots[i]<knots[i+1]]
 A,B,radial=spline_span(data,spans[0]);assert A==0
 for k,poly in enumerate(radial):assert all(i>=k//2 or not v for (i,j),v in poly.items())
 if 'archive_path' in data:verify_archive_input(data)
 return data,spans

def main():
 ap=argparse.ArgumentParser();ap.add_argument('input');ap.add_argument('output');ap.add_argument('--check',action='store_true');ap.add_argument('--maxdepth',type=int,default=24);ap.add_argument('--limit-seconds',type=float,default=480.)
 args=ap.parse_args();start=time.monotonic();inp=Path(args.input);dest=Path(args.output);data,spans=load_input(inp)
 if args.check:
  cert=json.loads(dest.read_text());assert cert['input_sha256']==hashlib.sha256(inp.read_bytes()).hexdigest();assert [q['span'] for q in cert['spans']]==spans
  stats={'leaves':0};accepted=True
  for item in cert['spans']:
   A,B,mats=coefficients(data,item['span']);ok=audit_tree(mats,A,B,item['tree'],stats);accepted &= ok
   print('checked',item['span'],ok,flush=True)
  res={'verdict':'CONFIRMED' if accepted else 'OPEN','elapsed_seconds':time.monotonic()-start,**stats,'utc':datetime.now(timezone.utc).isoformat(),'input_sha256':cert['input_sha256'],'certificate_sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'checker_code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'archive_sha256':data.get('archive_sha256')};dest.with_suffix('.check.json').write_text(json.dumps(res,indent=2)+'\n');print(res,flush=True);return
 cert={'input_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),'started_utc':datetime.now(timezone.utc).isoformat(),'spans':[],'stats':{'visited':0,'leaves':0,'max_depth':0},'status':'RUNNING'}
 if dest.exists():
  old=json.loads(dest.read_text());assert old['input_sha256']==cert['input_sha256'];cert=old
  def finished(tree):
   if 'axis' in tree:return finished(tree['left']) and finished(tree['right'])
   return 'positive' in tree or 'negative_box' in tree
  cert['spans']=[item for item in cert['spans'] if finished(item['tree'])]
  print('RESUME',len(cert['spans']),flush=True)
 cert['stats']['deadline']=start+args.limit_seconds;cert['stats']['node_budget']=cert['stats']['visited']+200000
 done={r['span'] for r in cert['spans']}
 for span in spans:
  if span in done:continue
  A,B,mats=coefficients(data,span);tree=certify(mats,A,B,0,args.maxdepth,cert['stats']);cert['spans'].append({'span':span,'tree':tree});cert['spans'].sort(key=lambda item:item['span']);cert['elapsed_seconds_this_process']=time.monotonic()-start;dest.write_text(json.dumps(cert,indent=2)+'\n')
  print('span',span,'of',spans[-1],'stats',cert['stats'],'seconds',time.monotonic()-start,flush=True)
  if time.monotonic()-start>args.limit_seconds:break
 cert['status']='SEARCH_COMPLETE' if len(cert['spans'])==len(spans) else 'CHECKPOINT';cert['ended_utc']=datetime.now(timezone.utc).isoformat();dest.write_text(json.dumps(cert,indent=2)+'\n');print(cert['status'],time.monotonic()-start,flush=True)
if __name__=='__main__':main()
