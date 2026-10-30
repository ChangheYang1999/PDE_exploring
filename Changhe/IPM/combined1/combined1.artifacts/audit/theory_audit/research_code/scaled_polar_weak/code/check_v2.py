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
F=load('scaled_polar_primitive',RESEARCH/'scaled_field_audit/source/fields.py')
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

def main():
 args=argparse.ArgumentParser();args.add_argument('--mode',type=int,default=7);args.add_argument('--bits',type=int,default=2048);args.add_argument('--skip-calibration',action='store_true');args=args.parse_args()
 ctx.prec=args.bits;start=time.monotonic();n=args.mode;assert n in [1,7]
 source=RESEARCH/'multiscale_point_010/data/candidate010.json';point_path=RESEARCH/'multiscale_point_010/source/N4_result.json';source_point=json.loads(point_path.read_text())
 data=json.loads(source.read_text());probe_path=BASE/f'data/probe_n{n}.json';probe=json.loads(probe_path.read_text());peer_path=BASE/f'source/N4_010_n{n}.json';peer=json.loads(peer_path.read_text())
 assert sha(source) in peer['inputs'].values()
 calibration={}
 if not args.skip_calibration:
  c007=RESEARCH/'taylor_projection/source/canonical007.json';d=json.loads(c007.read_text());c0,delta0,R0,S0=fields(d);co,de,ro,so=Old.fields(d)
  assert c0==co and delta0==de and set(R0)==set(ro) and set(S0)==set(so)
  assert all(A==Rat(ro[k]) for k,A in R0.items()) and all(A==Rat(so[k]) for k,A in S0.items())
  calibration={'R1_exact_polar_fields':True,'source_sha256':sha(c007),'rho_terms':len(R0),'stream_terms':len(S0)}
  print('007 exact polar calibration complete',time.monotonic()-start,flush=True)
 c,delta,rho,stream=fields(data)
 point=evaluation(c,delta,rho,stream,*source_point['point']);checks={k:z.overlaps(arb(source_point['fields'][k])) for k,z in point.items()};assert all(checks.values()),checks
 print('010 polar fields',len(rho),len(stream),'all6points',checks,'seconds',time.monotonic()-start,flush=True)
 P=sum((Q(a)*TR**int(k) for k,a in probe['probe_coefficients'].items()),Rat())
 assert P.powers==(0,0) and all(P.P[k]==0 for k in range((n-1)//2))
 H=Q(probe['H_upper_exact']);sup=Sup.sup_certificate(P.P,Q(0),H,n)
 Qp=(1-4*TR)*P+2*TR*VR*P.derivative();A0=(2*c+1)*P+c*Qp
 Ds={k:td(A,(k[0]+1)*delta/2,2) for k,A in stream.items()};Dr={k:td(A,(k[0]+1)*delta/2,1) for k,A in rho.items()}
 modes={(0,n):A0}
 for (j,m),S in stream.items():
  put(modes,j+1,n+m,(n*Ds[j,m]*P-m*S*Qp)/2)
  put(modes,j+1,n-m,(-n*Ds[j,m]*P-m*S*Qp)/2)
 modes={k:A for k,A in modes.items() if A};by_mode={}
 for (ell,m),A in modes.items():by_mode.setdefault(m,[]).append((ell,A))
 mgroups={};mpairs=0
 for rows in by_mode.values():
  for i,(ell,A) in enumerate(rows):
   for k,(ell2,B) in enumerate(rows[i:],i):add(mgroups,ell+ell2,A*B*(1 if i==k else 2));mpairs+=1
 print('M groups assembled',len(mgroups),mpairs,time.monotonic()-start,flush=True)
 mraw,mrecords=group_integrals(mgroups,delta,Q(1),'M2');M2=arb.pi()/2*mraw
 cg={};cpairs=0;rho_rows=list(rho.items())
 for ix,((j,m),A) in enumerate(rho_rows):
  for iy in range(ix,len(rho_rows)):
   (k,l),B=rho_rows[iy];factor=1 if ix==iy else 2
   ac=2*(m==l)-(abs(m-l)==2*n)+(m+l==2*n);bc=2*(m==l)-(abs(m-l)==2*n)-(m+l==2*n)
   if ac or bc:add(cg,j+k+2,factor*(ac*Dr[j,m]*Dr[k,l]+bc*m*l*A*B));cpairs+=factor
 cg={ell:A*P*P for ell,A in cg.items()}
 print('C groups assembled',len(cg),cpairs,time.monotonic()-start,flush=True)
 craw,crecords=group_integrals(cg,delta,Q(1),'C2');C2=arb.pi()/8*craw
 direct={}
 for (j,m),R in rho.items():
  if m==n:add(direct,j+1,(c*Dr[j,m]-R)*P)
 for (j,m),S in stream.items():
  for (k,l),R in rho.items():
   term=Rat()
   if l+m==n:term+=(-m*S*Dr[k,l]+l*Ds[j,m]*R)/2
   if abs(l-m)==n:term+=(1 if l>m else -1)*(-m*S*Dr[k,l]-l*Ds[j,m]*R)/2
   if term:add(direct,j+k+2,term*P)
 iraw,irecords=group_integrals(direct,delta,Q(-1),'I_direct');I=arb.pi()/2*iraw
 parts={}
 for (j,m),R in rho.items():
  for (ell,l),A in modes.items():
   if l==m:add(parts,j+1+ell,R*A)
 braw,brecords=group_integrals(parts,delta,Q(-1),'I_parts');Ib=-arb.pi()/2*braw
 assert I.overlaps(Ib) and M2>0 and C2>0
 M,C=M2.sqrt(),C2.sqrt();D=M+C;radius=2*abs(I)/(D+(D*D+4*ar(H)*abs(I)).sqrt())
 vals={'pairing':I,'pairing_parts':Ib,'M':M,'C':C,'radius':radius}
 flags={k:z.overlaps(arb(peer[k])) for k,z in vals.items()};assert all(flags.values()),flags
 floor=Q(peer['strict_lower_exact']);assert ar(floor)<radius
 paths=[Path(__file__),BASE/'PROOF.md',BASE/'code/C_SYMMETRY.md',source,point_path,probe_path,peer_path,RESEARCH/'scaled_field_audit/source/fields.py',RESEARCH/'weak_probe_audit/code/reproduce.py',RESEARCH/'new_successor_weak/code/check.py']
 out={'utc':datetime.now(timezone.utc).isoformat(),'angular_mode':n,'precision_bits':ctx.prec,'source_sha256':sha(source),'inputs':{str(p):sha(p) for p in paths},'calibration':calibration,'independent_point_overlaps':checks,'M_pairs':mpairs,'C_ordered_pairs':cpairs,'M_moments':mrecords,'C_moments':crecords,'direct_moments':irecords,'parts_moments':brecords,'sup_certificate':sup,**{k:z.str(100) for k,z in vals.items()},'peer_comparisons':flags,'strict_lower_exact':str(floor),'elapsed_seconds':time.monotonic()-start,'status':'CONFIRMED independent polar assembly and CRT/direct2F1 integration'}
 target=BASE/f'verification/010_n{n}.json'
 with target.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
 print('DONE',out['utc'],'mode',n,'radius',radius.str(40),'floor',floor,'seconds',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
