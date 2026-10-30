"""Independent polar rational fields and CRT/direct-hypergeometric moments."""
from pathlib import Path
from datetime import datetime, timezone
from math import comb
from functools import lru_cache
import argparse, hashlib, importlib.util, json, sys, time
from flint import fmpq as Q, fmpq_poly as Poly, arb, acb, ctx
sys.set_int_max_str_digits(0)
BASE=Path(__file__).resolve().parents[1];RESEARCH=BASE.parent

def load(name,p):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
F=load('scaled_polar_primitive',BASE/'code/rational.py')
Old=load('scaled_old_polar',RESEARCH/'weak_probe_audit/code/reproduce.py')
Sup=load('scaled_sup',RESEARCH/'new_successor_weak/code/check.py')
Rat,T,V,TR,VR=F.Rat,F.T,F.V,F.TR,F.VR
ar=F.ar
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()

def add(d,k,v):
 if v:d[k]=d.get(k,Rat())+v

def put(d,j,n,v):
 if n<0:n,v=-n,-v
 if n:add(d,(j,n),v)

@lru_cache(None)
def generator(m,spec):
 kind=spec[0];w=int(spec[1]);n=0 if kind=='mono' else int(spec[2]);q=int(spec[3]) if kind in ['legq','legqs'] else 0
 R=Q(spec[4]) if kind=='legqs' else Q(1);a=R*R-1
 assert kind in ['mono','leg','legq','legqs'] and (a==0 or a in F.SCALES)
 out=Rat()
 for k in range(n+1):
  powers=[0,0]
  if a:powers[F.SCALES.index(a)]=w+q+k
  coeff=Q((-1)**(n+k)*comb(n,k)*comb(n+k,k))*R**(2*q)
  out+=Rat(coeff*T**(m+w+k)*V**q,tuple(powers))
 return out

def euler(A,p):return 2*TR*VR*A.derivative()+2*p*TR*A

def td(A,a,d):return (d-2*a*TR)*A+2*TR*VR*A.derivative()

def fields(data):
 c=Q(data.get('cl_exact',data.get('cl')));delta=1-1/c;assert c>1
 if 'generators' in data:gens=data['generators']
 else:gens=[{'j':j,'m':m,'spec':['mono',k-m],'coef':v} for (j,m,k),v in zip(data['order'],data['coefficients'],strict=True)]
 pot={}
 for g in gens:add(pot,(int(g['j']),2*int(g['m'])),Q(g['coef'])*generator(int(g['m']),tuple(g['spec'])))
 rho,stream={},{}
 for (j,n),A in pot.items():
  p=(3+1/c-j*delta)/2
  lap=euler(euler(A,p),p)-n*n*A;D=euler(lap,p)-2*lap
  put(rho,j,n-1,(D+n*lap)/2);put(rho,j,n+1,-(D-n*lap)/2)
  plus=euler(A,p)-n*A;plus=euler(plus,p)-(n+2)*plus
  minus=euler(A,p)+n*A;minus=euler(minus,p)+(n-2)*minus
  put(stream,j,n+2,plus/4);put(stream,j,n-2,-minus/4)
 return c,delta,{k:A.divide_t(2) for k,A in rho.items() if A},{k:A.divide_t(2) for k,A in stream.items() if A}

def evaluation(c,delta,rho,stream,xs,ys):
 x,y=ar(Q(xs)),ar(Q(ys));r2=x*x+y*y;r=r2.sqrt();t=r2/(1+r2);v=1/(1+r2);z=acb(x/r,y/r)
 value,dr,dt,ur,ut=(arb(0) for _ in range(5))
 for (j,n),A in rho.items():
  trig=z**n;fac=v**ar((j+1)*delta/2);p=A.evaluate(t,v);d=td(A,(j+1)*delta/2,1).evaluate(t,v)
  value+=r*fac*p*trig.imag;dr+=fac*d*trig.imag;dt+=n*fac*p*trig.real
 for (j,n),A in stream.items():
  trig=z**n;fac=v**ar((j+1)*delta/2);p=A.evaluate(t,v);d=td(A,(j+1)*delta/2,2).evaluate(t,v)
  ur-=r*n*fac*p*trig.real;ut+=r*fac*d*trig.imag
 rx=x/r*dr-y/r*dt;ry=y/r*dr+x/r*dt;u1=x/r*ur-y/r*ut;u2=y/r*ur+x/r*ut
 return {'rho':value,'u1':u1,'u2':u2,'rho_x':rx,'rho_y':ry,'residual':(ar(c)*x+u1)*rx+(ar(c)*y+u2)*ry-value}

def inverse_mod(E,D):
 r0,r1=D,divmod(E,D)[1];s0,s1=Poly([]),Poly([1])
 while r1:
  q,r=divmod(r0,r1);r0,r1=r1,r;s0,s1=s1,s0-q*s1
 assert r0.degree()==0
 ans=divmod(s0/r0[0],D)[1]
 assert divmod(E*ans,D)[1]==Poly([1])
 return ans

@lru_cache(None)
def crt_data(powers):
 factors=[(a,k) for a,k in zip(F.SCALES,powers) if k]
 denominators=[(1+a*T)**k for a,k in factors];D=Poly([1])
 for Di in denominators:D*=Di
 rows=[]
 for (a,k),Di in zip(factors,denominators,strict=True):
  E,rem=divmod(D,Di);assert not rem
  rows.append((a,k,Di,E,inverse_mod(E,Di)))
 return D,rows

@lru_cache(None)
def pole(btext,atext,k):
 b,a=Q(btext),Q(atext);assert b>-1 and a>0 and k>0
 z=(-ar(a)).hypgeom_2f1(arb(k),ar(b+1),ar(b+2),bc=True,abc=True)/ar(b+1)
 assert z.is_finite();return z

def integrate(A,b,label):
 tick=time.monotonic();assert b>-1
 if not A:return arb(0),{'label':label,'exact_zero':True,'b':str(b)}
 N=V*A.numerator_v();D,rows=crt_data(A.powers);pol,rem=divmod(N,D)
 value=sum((ar(q/(b+i+1)) for i,q in enumerate(pol)),arb(0));replay=pol*D;count=0
 for a,k,Di,E,inv in rows:
  Ri=divmod(rem*inv,Di)[1];local=Ri(Poly([-1/a,1/a]))
  for j,q in enumerate(local):
   if q:
    order=k-j;assert order>0
    value+=ar(q)*pole(str(b),str(a),order);count+=1
  replay+=Ri*E
 assert replay==N
 assert value.is_finite() and value.rel_accuracy_bits()>150,(label,value.rel_accuracy_bits())
 record={'label':label,'b':str(b),'denominator_powers':list(A.powers),'polynomial_degree':pol.degree(),'principal_parts':count,'exact_CRT_replay':True,'accuracy_bits':value.rel_accuracy_bits(),'value':value.str(95),'elapsed_seconds':time.monotonic()-tick}
 print(label,'degree',pol.degree(),'poles',count,'bits',value.rel_accuracy_bits(),'seconds',record['elapsed_seconds'],flush=True)
 return value,record

def group_integrals(groups,delta,offset,label):
 total=arb(0);records=[]
 for ell,A in sorted(groups.items()):
  z,r=integrate(A,offset+ell*delta/2,f'{label}:{ell}');total+=z;records.append(r)
 return total,records

