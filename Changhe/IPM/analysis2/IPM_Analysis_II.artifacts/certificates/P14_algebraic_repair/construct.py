"""Exact six-sector repair. Only own audited rational source records are read."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,sys,hashlib
HERE=Path(__file__).resolve().parent; BASE=HERE.parents[1]
sys.set_int_max_str_digits(0)

def clean(d):return {k:v for k,v in d.items() if v}
def moments(A,c):
 out={}
 for (j,m,k),v in A.items():
  a=(3+1/c-j*(1-1/c))/2
  L,D=out.get((j,m),(Q(0),Q(0)))
  out[j,m]=L+v,D+(a-k)*v
 return out

def run(name,K):
 if name=='state131':
  path=BASE/'source_audit/state131_exact.json';old=json.loads(path.read_text());c=Q(old['exact_parameters']['cl']);osh=old['canonical_serialization_sha256']
 else:
  path=BASE/'08_refits/verification'/f'{name}_audit.json';old=json.loads(path.read_text());c=Q(old['cl']);osh=old['canonical_sha256']
 assert K>=3
 A={tuple(k):Q(v) for k,v in zip(old['canonical_order'],old['canonical_coefficients'])};orig=A.copy()
 tailpath=BASE/'10_tail_splice/verification/state131_splice.json';t=json.loads(tailpath.read_text());assert c==Q(t['c'])
 Cs={int(n)-1:{int(m)//2:Q(v) for m,v in d['cosine_coefficients'].items()} for n,d in t['homogeneous_potential_orders'].items()}
 oldmom=moments(A,c); additions={}
 for j in range(6):
  ms=set(Cs[j])|{m for jj,m in oldmom if jj==j}
  p=(3+1/c-j*(1-1/c))/2
  for m in sorted(ms):
   L,D=oldmom.get((j,m),(Q(0),Q(0)));lead=Cs[j].get(m,Q(0))-L;k=m+K
   if j==0:assert lead==0
   if j<=1:
    B=-D;b=(p-k)*lead-B;a=lead-b
    pairs=[(k,a),(k+1,b)]
   else:pairs=[(k,lead)]
   for kk,v in pairs:
    if v:
     key=j,m,kk;A[key]=A.get(key,Q(0))+v;additions[key]=additions.get(key,Q(0))+v
 A=clean(A);additions=clean(additions);newmom=moments(A,c)
 for j in range(6):
  for m in set(Cs[j])|{m for jj,m in newmom if jj==j}:
   L,D=newmom.get((j,m),(Q(0),Q(0)))
   assert L==Cs[j].get(m,Q(0))
   if j<=1:assert D==0
 assert all(k>=m+K for j,m,k in additions)
 assert {k:v for k,v in A.items() if k[2]<K}=={k:v for k,v in orig.items() if k[2]<K}
 serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(A.items()))+'\n'
 destname=f'algebraic_{name}_k{K}'
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'name':destname,'verdict':'CONSTRUCTED_EXACTLY',
      'base_name':name,'base_canonical_sha256':osh,'base_record_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
      'stationary_tail_record_sha256':hashlib.sha256(tailpath.read_bytes()).hexdigest(),
      'cl':str(c),'K':K,'canonical_sha256':hashlib.sha256(serial.encode()).hexdigest(),
      'canonical_order':[list(k) for k in sorted(A)],'canonical_coefficients':[str(A[k]) for k in sorted(A)],
      'additions_order':[list(k) for k in sorted(additions)],'additions_coefficients':[str(additions[k]) for k in sorted(additions)],
      'canonical_term_count':len(A),'additions_term_count':len(additions),'all_six_leading_potentials_exact':True,
      'first_descendants_j0_j1_zero':True,'potential_jets_below_degree':2*K,
      'residual_power_bound':str(1-7*(1-1/c)),
      'scope':'Exact construction and moment checks. Independent audit pending. No background coefficient or residual-size certificate.'}
 (HERE/f'{destname}.json').write_text(json.dumps(out,indent=2)+'\n')
 print(destname,'terms',len(A),'additions',len(additions),'maxk',max(k for j,m,k in A),'sha',out['canonical_sha256'],flush=True)

if __name__=='__main__':
 for name in ('state131','n12_m10'):
  for K in (tuple(map(int,sys.argv[1:])) or (4,8,16)):run(name,K)
