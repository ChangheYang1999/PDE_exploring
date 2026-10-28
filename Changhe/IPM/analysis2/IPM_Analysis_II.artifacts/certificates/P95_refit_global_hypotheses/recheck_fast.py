"""Independent source-polynomial reconstruction and direct cell restriction.
The Taylor product is convolved in powers, not multiplied in Bernstein form.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb,factorial
from functools import lru_cache
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time,argparse
sys.set_int_max_str_digits(0)
from flint import arb,arb_mat,ctx
here=Path(__file__).parent

def A(v):
 q=F(v);return arb(q.numerator)/q.denominator

def make_polys(d,kind):
 c=F(d['cl']);P={key:{(i,z):F(v) for i,z,v in rows} for key,rows in d['polynomials'].items()};out={(l,j):{} for l in ['a','b','q'] for j in range(7)}
 def add(l,j,key,v,shift=0):
  for (i,k),a in P[key].items():out[l,j][i+shift,k]=out[l,j].get((i+shift,k),F(0))+v*a
 if kind=='M':const=2*c+1-F(19,5);linear=0
 elif kind=='M1':const=F(1,2);linear=-c/5
 else:const=F(1,2)-c;linear=F(3,2)+c/5
 for l in ['a','b']:
  out[l,0][0,0]=const
  if linear:out[l,0][1,0]=linear
 for j in range(6):
  if kind=='M':terms=[('a','chi22',-2),('a','chi04',-1),('b','chi22',1),('q','chi31',1)]
  elif kind=='M1':terms=[('a','chi04',-1),('b','chi22',-1),('q','chi13',1)]
  else:terms=[('a','chi22',1),('a','chi04',-1),('b','chi22',-2),('q','chi31',-F(1,2)),('q','chi13',F(3,2))]
  for l,key,v in terms:
   add(l,j+1,f'{key}_{j}',v)
   if kind=='M2':add(l,j+1,f'{key}_{j}',3*v,1)
  if kind!='M':
   for l in ['a','b']:add(l,j+1,f'e_{j}',-F(1,5) if kind=='M1' else F(16,5),1)
 return {key:{k:v for k,v in p.items() if v} for key,p in out.items()}

@lru_cache(None)
def restrict(n,lo,hi):
 lo,hi=F(lo),F(hi)
 return arb_mat([[A(comb(k,i)*lo**(k-i)*(hi-lo)**i) if i<=k else arb(0) for k in range(n+1)] for i in range(n+1)])
@lru_cache(None)
def convert(n):return arb_mat([[A(F(comb(i,k),comb(n,k))) if k<=i else arb(0) for k in range(n+1)] for i in range(n+1)])
@lru_cache(None)
def T(n,lo,hi):return convert(n)*restrict(n,lo,hi)

def endpoints(path):
 a,b,c,d=F(0),F(1),F(-1),F(1)
 for letter in path:
  if letter=='t':b=(a+b)/2
  elif letter=='T':a=(a+b)/2
  elif letter=='z':d=(c+d)/2
  elif letter=='Z':c=(c+d)/2
  else:raise ValueError(letter)
 return a,b,c,d

def tree(paths,prefix=''):
 if prefix in paths:
  assert not any(p.startswith(prefix) and p!=prefix for p in paths);return
 letters={p[len(prefix)] for p in paths if p.startswith(prefix)};assert letters in [{'t','T'},{'z','Z'}],(prefix,letters)
 for q in letters:tree(paths,prefix+q)

def maxabs(v):
 out=arb(0)
 for x in v:out=out.max(abs(x))
 return out.upper()

def field_ranges(P,nt,nz,a,b,c,d,delta):
 radial=restrict(nt,str(a),str(b));angular=T(nz,str(c),str(d)).transpose();power={key:radial*mat*angular for key,mat in P.items()};bern={key:convert(nt)*v for key,v in power.items()}
 # Independent branch-variable range, including cells that touch infinity.
 wl=(1-A(b))**A(delta/2);wh=(1-A(a))**A(delta/2)
 W=arb_mat([[sum((A(F(comb(n,l)*comb(i,l),comb(6,l)))*wl**(n-l)*(wh-wl)**l for l in range(min(n,i)+1)),arb(0)) for n in range(7)] for i in range(7)])
 plain={}
 for label in ['a','b','q']:
  vals=(W*arb_mat([bern[label,j].entries() for j in range(7)])).entries();lo=hi=vals[0]
  for v in vals[1:]:lo=lo.min(v);hi=hi.max(v)
  plain[label]=lo.lower(),hi.upper()
 if b==1:return plain,None
 N=4;coeffs={};remainders={}
 for j in range(7):
  q=F(j)*delta/2;fall=F(1);vals=[]
  for l in range(N+1):
   if l:fall*=q-l+1
   vals.append(A((-1)**l*fall/factorial(l))*A(b-a)**l*(1-A(a))**A(q-l))
  coeffs[j]=vals;remainders[j]=A(abs(fall*(q-N))/factorial(N+1))*A(b-a)**(N+1)*(1-A(b))**A(q-N-1)
 improved={}
 for label in ['a','b','q']:
  combined=arb_mat(nt+N+1,nz+1);error=arb(0)
  for j in range(7):
   mat=power[label,j]
   multiplier=arb_mat(nt+N+1,nt+1)
   for i in range(nt+1):
    for l in range(N+1):multiplier[i+l,i]=coeffs[j][l]
   combined+=multiplier*mat
   error+=remainders[j]*maxabs(bern[label,j].entries())
  vals=(convert(nt+N)*combined).entries();lo=hi=vals[0]
  for v in vals[1:]:lo=lo.min(v);hi=hi.max(v)
  improved[label]=(lo-error).lower(),(hi+error).upper()
 return plain,improved

def eigen(rr,c,d):
 x,y=rr['a'][0],rr['b'][0];lo,hi=rr['q'];z=F(0) if c<=0<=d else min(abs(c),abs(d));off=abs(lo).max(abs(hi))*(1-A(z)**2).sqrt()
 return ((x+y-((x-y)**2+4*off**2).sqrt())/2).max(x.min(y)-off)

def main(args):
 ctx.prec=640;start=time.monotonic();src=here/args.file;d=json.loads(src.read_text());assert d['status']=='COMPLETE';ppath=here/f"{d['name']}.polynomials.json";data=json.loads(ppath.read_text());assert d['input_sha256']==sha256(ppath.read_bytes()).hexdigest();S=make_polys(data,d['kind']);nt=max(i for p in S.values() for i,k in p);nz=max(k for p in S.values() for i,k in p);P={}
 for key,p in S.items():
  mat=arb_mat(nt+1,nz+1)
  for (i,k),v in p.items():mat[i,k]=A(v)
  P[key]=mat
 paths={v['path'] for v in d['accepted']};assert len(paths)==len(d['accepted']);tree(paths);rows=[];delta=F(data['delta']);worst=arb(100)
 for cell in d['accepted']:
  a,b,c,e=endpoints(cell['path']);assert list(map(str,[a,b]))==cell['t'] and list(map(str,[c,e]))==cell['z'];plain,improved=field_ranges(P,nt,nz,a,b,c,e,delta);low=eigen(plain,c,e)
  if improved is not None:low=low.max(eigen(improved,c,e))
  assert low>=0,(cell['path'],low);worst=worst.min(low);rows.append({'path':cell['path'],'lower':low.str(80),'pass':True})
  if len(rows)%10==0:print(len(rows),'rechecked',time.monotonic()-start,flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(),'all_pass':True,'precision_bits':ctx.prec,'rows':rows,'leaves':len(rows),'primary_sha256':sha256(src.read_bytes()).hexdigest(),'polynomials_sha256':sha256(ppath.read_bytes()).hexdigest(),'worst':worst.str(80),'seconds':time.monotonic()-start};dest=src.with_name(src.stem+'.recheck.json');dest.write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],len(rows),'PASS',out['seconds'],flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('file');main(ap.parse_args())
