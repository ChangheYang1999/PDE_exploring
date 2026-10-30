"""Independent complete cover by global Bernstein coefficients and subdivision."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb,factorial
from functools import lru_cache
import gzip,json,sys,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,arb_mat,ctx
B=Path(__file__).resolve().parents[1];LANE=B.parents[1]
sys.set_int_max_str_digits(0);start=time.monotonic()
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat()
ar=lambda q:arb(Q(q).p)/Q(q).q
manifest=json.loads((B/'data/manifest.json').read_text())
assert sha(B/'PROOF.md')==manifest['proof_sha256']
assert sha(B/'data/parameters.json')==manifest['parameters_sha256']
for name,h in manifest['sources'].items():assert sha(B/'source'/name)==h,name
p=json.loads((B/'data/parameters.json').read_text());ctx.prec=p['precision_bits']
source=LANE/p['polynomial_dependency'];assert sha(source)==p['polynomial_sha256']
bindings={'manifest':sha(B/'data/manifest.json'),'checker':sha(Path(__file__)),'polynomials':sha(source)}
peer=json.loads((B/'source/N4_complete_cover.json').read_text());accepted=json.loads((B/'source/T4_378_result.json').read_text())
assert peer['all_pass'] and not peer['pending'] and accepted['all_exact_coefficients_equal']
assert accepted['peer_polynomial_sha256']==p['polynomial_sha256']
assert accepted['raw_sha256']==peer['raw_sha256']==p['raw_sha256']
paths={row['path'] for row in peer['accepted']};assert len(paths)==len(peer['accepted'])==p['expected_leaves']
children={}
for path in paths:
 for i,ch in enumerate(path):children.setdefault(path[:i],set()).add(ch)
assert not paths.intersection(children)
assert all(v in [{'t','T'},{'z','Z'}] for v in children.values())
def rectangle(path):
 a,b,c,d=Q(0),Q(1),Q(-1),Q(1)
 for ch in path:
  if ch=='t':b=(a+b)/2
  elif ch=='T':a=(a+b)/2
  elif ch=='z':d=(c+d)/2
  else:assert ch=='Z';c=(c+d)/2
 return a,b,c,d
rects=[rectangle(path) for path in sorted(paths)]
assert sum(((b-a)*(d-c) for a,b,c,d in rects),Q(0))==2
pairs=0
for i,(a,b,c,d) in enumerate(rects):
 assert 0<=a<b<=1 and -1<=c<d<=1
 for aa,bb,cc,dd in rects[:i]:
  assert max(a,aa)>=min(b,bb) or max(c,cc)>=min(d,dd);pairs+=1

def global_transform(n,angular=False):
 return arb_mat([[ar(sum((Q(comb(k,l)*comb(i,l)*(-1)**(k-l)*2**l,comb(n,l)) for l in range(min(i,k)+1)),Q(0))) if angular else ar(Q(comb(i,k),comb(n,k))) if k<=i else arb(0) for k in range(n+1)] for i in range(n+1)])
@lru_cache(8)
def halves(n,right=False):
 return arb_mat([[ar(Q(comb(n-i,j-i),2**(n-i))) if right and j>=i else ar(Q(comb(i,j),2**i)) if not right and j<=i else arb(0) for j in range(n+1)] for i in range(n+1)])
def bern_exact(P,n,a,b):
 local=P(Poly([a,b-a]));return [sum((local[k]*Q(comb(i,k),comb(n,k)) for k in range(min(i,local.degree())+1)),Q(0)) for i in range(n+1)]
# Independent small exact identities calibrate both transforms and half maps.
fixture_count=0
for n in [3,7]:
 P=Poly([Q((-1)**k*(k+1),k+2) for k in range(n+1)])
 for angular in [False,True]:
  a,b=(Q(-1),Q(1)) if angular else (Q(0),Q(1));coeff=bern_exact(P,n,a,b)
  got=global_transform(n,angular)*arb_mat([[ar(P[k])] for k in range(n+1)])
  assert all(v.contains(ar(e)) for v,e in zip(got.entries(),coeff,strict=True))
  for right in [False,True]:
   lo,hi=((a+b)/2,b) if right else (a,(a+b)/2)
   got=halves(n,right)*arb_mat([[ar(x)] for x in coeff]);expected=bern_exact(P,n,lo,hi)
   assert all(v.contains(ar(e)) for v,e in zip(got.entries(),expected,strict=True));fixture_count+=1
print('GEOMETRY_AND_FIXTURES',len(paths),pairs,fixture_count,'seconds',time.monotonic()-start,flush=True)
with gzip.open(source,'rt') as f:data=json.load(f)
assert data['raw_sha256']==p['raw_sha256'] and data['J']==8
n,m,J=103,80,8;delta=Q(data['delta']);assert delta==1-1/Q(p['c'])
assert Poly([Q(x) for x in data['denominator']])==(1+2499*Poly([1,-1]))**19
T=global_transform(n);Z=global_transform(m,True).transpose();P={};count=0
for key,rows in sorted(data['polynomials'].items()):
 label,st=key.split('_');j=int(st);assert label in ['rx','ry'] and 1<=j<=J
 M=arb_mat(n+1,m+1)
 for i,k,value in rows:M[i,k]=ar(value);count+=1
 P[label,j]=T*M*Z
 assert len(rows)==accepted['coefficient_counts'][key]
 print('GLOBAL_FIELD',key,'seconds',time.monotonic()-start,flush=True)
assert count==40082;del data,T,Z,M
@lru_cache(256)
def denominator(n,a,b):
 L,R=1+2499*(1-a),1+2499*(1-b)
 vals=[sum((Q(comb(19,k)*comb(n-19,i-k),comb(n,i))*L**(19-k)*R**k for k in range(max(0,i-(n-19)),min(19,i)+1)),Q(0)) for i in range(n+1)]
 assert all(v>0 for v in vals);return tuple(ar(v) for v in vals)
def normal(M,D):return arb_mat([[M[i,k]/D[i] for k in range(M.ncols())] for i in range(M.nrows())])
def extrema(M):
 xs=M.entries();low,high=xs[0],xs[0]
 for v in xs[1:]:low=low.min(v);high=high.max(v)
 return arb(low.lower()),arb(high.upper())
def absolute(M):
 out=arb(0)
 for v in M.entries():out=out.max(abs(v))
 return arb(out.upper())
def theta_bound(ranges,c,d):
 y0=ranges['ry'][0];x0=abs(ranges['rx'][0]).max(abs(ranges['rx'][1]));z=Q(0) if c<=0<=d else min(abs(c),abs(d))
 x=x0*(1-ar(z*z)).sqrt();value=(((y0*y0+x*x).sqrt()-y0)/2)
 return arb(value.upper())
def taylor(j,a,b):
 alpha=j*delta/2;mu=(a+b)/2;half=(b-a)/2;fall=Q(1);local=[arb(0) for _ in range(7)]
 for k in range(7):
  if k:fall*=alpha-k+1
  value=ar((-1)**k*fall/Q(factorial(k)))*(1-ar(mu))**ar(alpha-k)*ar(half)**k
  for l in range(k+1):local[l]+=value*comb(k,l)*2**l*(-1)**(k-l)
 coeff=[sum((local[k]*ar(Q(comb(i,k),comb(6,k))) for k in range(i+1)),arb(0)) for i in range(7)]
 mult=arb_mat(n+7,n+1)
 for i in range(n+1):
  for k in range(7):mult[i+k,i]=coeff[k]*ar(Q(comb(n,i)*comb(6,k),comb(n+6,i+k)))
 error=ar(abs(fall*(alpha-6))*half**7/Q(factorial(7)))*((1-ar(a))**ar(alpha-7)).max((1-ar(b))**ar(alpha-7))
 return mult,error

def range_cell(fields,path):
 a,b,c,d=rectangle(path);D=denominator(n,a,b);normalized={key:normal(M,D) for key,M in fields.items()}
 wl=(1-ar(b))**ar(delta/2);wh=(1-ar(a))**ar(delta/2)
 W=arb_mat([[sum((ar(Q(comb(j,k)*comb(i,k),comb(J,k)))*wl**(j-k)*(wh-wl)**k for k in range(min(i,j)+1)),arb(0)) for j in range(1,J+1)] for i in range(J+1)])
 plain={label:extrema(W*arb_mat([normalized[label,j].entries() for j in range(1,J+1)])) for label in ['rx','ry']}
 primary=theta_bound(plain,c,d);improved=None;correlated=None;denlower=min(arb(x.lower()) for x in D)
 if b<1:
  Dlarge=denominator(n+6,a,b);denlower=denlower.min(min(arb(x.lower()) for x in Dlarge))
  total={label:arb_mat(n+7,m+1) for label in ['rx','ry']};error={label:arb(0) for label in ['rx','ry']}
  for j in range(1,J+1):
   mult,e=taylor(j,a,b)
   for label in ['rx','ry']:total[label]+=mult*fields[label,j];error[label]+=e*absolute(normalized[label,j])
  correlated={}
  for label in ['rx','ry']:
   lo,hi=extrema(normal(total[label],Dlarge));correlated[label]=(arb((lo-error[label]).lower()),arb((hi+error[label]).upper()))
  improved=theta_bound(correlated,c,d)
 bound=primary if improved is None else primary.min(improved)
 assert denlower>0
 return {'path':path,'rectangle':list(map(str,[a,b,c,d])),'theta_upper':bound.str(110),'plain_theta_upper':primary.str(110),'correlated_theta_upper':None if improved is None else improved.str(110),'plain_ranges':{key:[x.str(100) for x in v] for key,v in plain.items()},'correlated_ranges':None if correlated is None else {key:[x.str(100) for x in v] for key,v in correlated.items()},'positive_denominator_lower':denlower.str(100),'pass':bool(bound<=ar(p['tau']))}
leavesdir=B/'verification/leaves';leavesdir.mkdir(exist_ok=True);records=[]
def walk(path,fields):
 if path in paths:
  target=leavesdir/(path+'.json')
  if target.exists():
   row=json.loads(target.read_text());assert row['bindings']==bindings and row['pass']
  else:
   cellstart=time.monotonic();row=range_cell(fields,path);row.update({'completed_utc':now(),'precision_bits':ctx.prec,'bindings':bindings,'elapsed_seconds':time.monotonic()-cellstart})
   with target.open('x') as f:json.dump(row,f,indent=2);f.write('\n')
  records.append(row);print('LEAF',len(records),path,'pass',row['pass'],'theta',arb(row['theta_upper']).str(14),'total_seconds',time.monotonic()-start,flush=True)
  assert row['pass'],('independent leaf did not pass',path,row['theta_upper'])
  return
 for ch in sorted(children[path]):
  radial=ch in 'tT';right=ch in 'TZ';M=halves(n if radial else m,right)
  child={key:M*value if radial else value*M.transpose() for key,value in fields.items()}
  walk(path+ch,child)
walk('',P)
assert len(records)==len(paths)==247 and all(row['pass'] for row in records)
# Use the accepted upper bound, with its complete source artifact bound above.
kappa=ar(p['kappa_upper'])
hessian=json.loads((B/'source/T4_366_017.json').read_text())
assert hessian['whole_plane'] and hessian['raw_sha256']==p['raw_sha256']
assert arb(hessian['values']['kappa'])<kappa
rate=ar(p['c'])+1-ar(p['tau'])-kappa;assert rate>ar(p['rate_floor'])
out={'completed_utc':now(),'elapsed_seconds':time.monotonic()-start,'precision_bits':ctx.prec,'bindings':bindings,'candidate':peer['candidate'],'raw_sha256':p['raw_sha256'],'leaf_count':len(records),'all_leaves_pass':True,'exact_partition_area':'2','disjoint_pairs_checked':pairs,'fixture_count':fixture_count,'independent_global_transform_and_subdivision':True,'coefficient_count':count,'theta_upper':p['tau'],'signed_rate_lower':rate.str(110),'leaf_sha256':{row['path']:sha(leavesdir/(row['path']+'.json')) for row in records},'foreign_code_executed':False,'status':'PASS independent complete017 signed-gradient cover'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('COMPLETE',len(records),'rate',rate.str(25),'seconds',out['elapsed_seconds'],flush=True)
