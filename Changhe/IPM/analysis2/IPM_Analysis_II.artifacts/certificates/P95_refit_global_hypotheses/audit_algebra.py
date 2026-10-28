"""Independent per-generator reconstruction, with exact complex-binomial angles."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as F
from math import comb
from functools import lru_cache
import sys,json,time,argparse
sys.set_int_max_str_digits(0)
here=Path(__file__).parent;root=here.parents[2]
sys.path.insert(0,str(root/'research/02_energy/verification'))
from compact_matrix import derivative,add,chebyshev

@lru_cache(None)
def odd_angle(n,kind):
 assert n%2;out={}
 for b in range(0 if kind=='c' else 1,n+1,2):
  j=b//2;h=(n-b-1)//2 if kind=='c' else (n-b)//2
  coef=F((-1)**j*comb(n,b),2**(h+j))
  for u in range(h+1):
   for v in range(j+1):out[u+v]=out.get(u+v,F(0))+coef*comb(h,u)*comb(j,v)*(-1)**v
 return {k:v for k,v in out.items() if v}

def main(args):
 start=time.monotonic();checks=[]
 def check(name,value):
  assert value,name
  checks.append({'name':name,'pass':True})
 source=root.parent/f's1-num/research/data/{args.name}.json';s=json.loads(source.read_text());p=here/f'{args.name}.polynomials.json';ep=here/f'{args.name}.derivatives.json';d=json.loads(p.read_text());e=json.loads(ep.read_text());c=F(s['cl']);delta=1-1/c
 check('source bytes',sha256(source.read_bytes()).hexdigest()==d['source_sha256']==e['source_sha256'])
 check('parameters',F(d['cl'])==c and F(e['cl'])==c and F(d['delta'])==delta and F(e['delta'])==delta)
 check('decay exponent',delta>F(4,9))
 # Independently expand the generator basis into the canonical monomials.
 coefficients={}
 for g in s['generators']:
  j,m,a,spec=g['j'],g['m'],F(g['coef']),g['spec']
  if spec[0]=='mono':terms=[(m+spec[1],a)]
  else:
   check('Legendre generator tag',spec[0]=='leg');w,n=spec[1:];terms=[(m+w+h,a*(-1)**(n-h)*comb(n,h)*comb(n+h,h)) for h in range(n+1)]
  for k,v in terms:coefficients[j,m,k]=coefficients.get((j,m,k),F(0))+v
 coefficients={k:v for k,v in coefficients.items() if v};serial='\n'.join(','.join(map(str,k))+':'+str(v) for k,v in sorted(coefficients.items()))+'\n'
 check('independent canonical hash',sha256(serial.encode()).hexdigest()==d['canonical_sha256']==e['canonical_sha256'])
 all_fields=[('chi22','xxyy',1,'c'),('chi04','yyyy',1,'c'),('chi31','xxxy',1,'s'),('chi13','xyyy',1,'s'),('e','xy',1,'c'),('u1','xyy',-1,'c'),('u2','xxy',1,'s'),('chi41','xxxxy',1,'s'),('chi32','xxxyy',1,'c'),('chi23','xxyyy',1,'s'),('chi14','xyyyy',1,'c'),('chi05','yyyyy',1,'s')]
 selected=[v for v in all_fields if args.group=='all' or (args.group=='base')==(v[0] in ['chi22','chi04','chi31','chi13','e'])]
 for label,axes,sign,kind in selected:
  shift=3 if len(axes)==5 else 2
  for j in range(6):
   trig={};exponent=(3+1/c-j*delta)/2
   for (jj,m,k),a in coefficients.items():
    if jj!=j:continue
    T={('c',2*m,0):a}
    for order,axis in enumerate(axes):T=derivative(T,exponent,k,order,axis)
    for (typ,n,l),v in T.items():
     if label=='e':
      check(f'e angular parity {j} {m} {k} {n} {l}',typ=='s');typ='c';v*=-n
     add(trig,typ,n,k-shift+l,sign*v)
   out={}
   for (typ,n,i),v in trig.items():
    check(f'{label} radial and angular parity {j} {typ} {n} {i}',i>=0 and typ==kind and n%2==len(axes)%2)
    C=odd_angle(n,typ) if len(axes)%2 else dict(enumerate(chebyshev(n//2-1,'U') if typ=='s' else chebyshev(n//2)))
    for k,a in C.items():out[i,k]=out.get((i,k),F(0))+v*a
   out={k:v for k,v in out.items() if v};stored={(i,k):F(v) for i,k,v in (d if label in ['chi22','chi04','chi31','chi13','e'] else e)['polynomials'][f'{label}_{j}']}
   check(f'{label} branch {j} all exact coefficients',out==stored)
  print(label,'PASS',time.monotonic()-start,flush=True)
 record={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'checks':checks,'group':args.group,'polynomials_sha256':sha256(p.read_bytes()).hexdigest(),'derivatives_sha256':sha256(ep.read_bytes()).hexdigest(),'source_sha256':sha256(source.read_bytes()).hexdigest(),'seconds':time.monotonic()-start}
 (here/f'{args.name}.algebra.{args.group}.json').write_text(json.dumps(record,indent=2)+'\n');print(record['utc'],len(checks),'PASS',record['seconds'],flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--name',default='nb_d2_exact');ap.add_argument('--group',choices=['base','higher','all'],default='all');main(ap.parse_args())
