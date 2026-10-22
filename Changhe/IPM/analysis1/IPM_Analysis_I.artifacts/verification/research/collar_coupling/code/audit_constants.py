"""Arb constants versus separately assembled iv integrals; rational identities."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
import sys,json,math,hashlib
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
from mpmath import iv
B=Path(__file__).resolve().parents[1];E=B/'evidence';ctx.prec=320;iv.dps=160
assert sys.flags.optimize==0
PINS={'PROOF.md':'b3c1c172ac52303facebdb5015bf3f386bf320e907bc3bc573e5694227c39b17','evidence/lead_collar_v2.md':'316b3b927b741bd56ff138305c18fdd8d3a9d4f811865ceaeb91a5ec8e970d56','../edge_velocity/evidence/verdict.json':'05e521dee3e2fb143433633a929a53088c3b60ae68d9af3362bb5c03a6ad208d'}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aa(q):q=F(q);return arb(q.numerator)/q.denominator
def iq(q):q=F(q);return iv.mpf(q.numerator)/q.denominator
def dy(x):m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def ie(x):
 assert not iv.isnan(x) and not iv.isinf(x);out=[]
 for s,m,e,bc in x._mpi_:
  assert bc>=0;out.append((-1 if s else 1)*F(int(m))*F(2)**int(e))
 assert out[0]<=out[1];return out

def compare(a,z):
 assert a.is_finite();lo,hi=dy(a.lower()),dy(a.upper());il,iu=ie(z);assert 0<lo<=il<=iu<=hi
 return {'arb_lower_exact':str(lo),'arb_upper_exact':str(hi),'iv_lower_exact':str(il),'iv_upper_exact':str(iu),'arb_display':a.str(25)}
def cadd(z,w):return z[0]+w[0],z[1]+w[1]
def cmul(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def cneg(z):return -z[0],-z[1]
def cinv(z):r=z[0]**2+z[1]**2;assert r;return z[0]/r,-z[1]/r
def cpow(z,n):
 if n<0:return cpow(cinv(z),-n)
 out=(F(1),F(0))
 for _ in range(n):out=cmul(out,z)
 return out

def exact_identities():
 count=0
 for W in [(F(3),F(4)),(F(2),F(1)),(F(-2),F(3))]:
  conj=(W[0],-W[1])
  for n in range(14):
   left=cadd(cadd(cpow(W,-n-2),cneg(cpow(conj,-n-2))),cadd(cpow(cneg(conj),-n-2),cneg(cpow(cneg(W),-n-2))))
   right=(F(0),4*cpow(W,-n-2)[1]) if n%2 else (F(0),F(0));assert left==right;count+=1
 # Coupling identity as a polynomial in independent symbols; integer coefficient dictionary.
 def mon(**d):return {tuple(sorted(d.items())):F(1)}
 def add(*ps):
  out={}
  for p in ps:
   for m,c in p.items():out[m]=out.get(m,F(0))+c
  return {m:c for m,c in out.items() if c}
 def mul(p,q):
  out={}
  for m,c in p.items():
   for n,d in q.items():
    e=dict(m)
    for x,v in n:e[x]=e.get(x,0)+v
    t=tuple(sorted(e.items()));out[t]=out.get(t,F(0))+c*d
  return {m:c for m,c in out.items() if c}
 def scale(p,c):return {m:c*d for m,d in p.items() if c*d}
 def prod(*ps):
  r={():F(1)}
  for p in ps:r=mul(r,p)
  return r
 s={x:mon(**{x:1}) for x in ['chi','y','x','u10','u12','u21','R1','R2','r1','r1p','r3','r3p','A','B','sig']};one={():F(1)};y=s['y'];y2=prod(y,y);y3=prod(y2,y);chi=s['chi']
 rx=add(prod(y,s['r1p']),prod(y3,s['r3p']),s['A']);ry=add(s['r1'],scale(prod(y2,s['r3']),3),s['B'])
 U1=add(prod(chi,add(s['u10'],prod(y2,s['u12']))),s['R1']);U2=add(prod(chi,y,s['u21']),s['R2']);scale1=scale(s['sig'],F(1,3))
 L=add(prod(add(U1,prod(scale1,s['x'])),rx),prod(add(U2,prod(scale1,y)),ry))
 q=add(prod(add(s['u10'],prod(scale1,s['x'])),s['r1p']),prod(add(s['u21'],scale1),s['r1']))
 cubic=prod(chi,y3,add(prod(s['u10'],s['r3p']),prod(s['u12'],s['r1p']),scale(prod(s['u21'],s['r3']),3)))
 er=prod(chi,add(prod(s['u10'],s['A']),prod(y2,s['u12'],add(rx,scale(prod(y,s['r1p']),-1))),prod(y,s['u21'],s['B'])))
 sb=prod(scale1,add(prod(add(one,scale(chi,-1)),y,add(prod(s['x'],s['r1p']),s['r1'])),prod(y3,add(prod(s['x'],s['r3p']),scale(s['r3'],3))),prod(s['x'],s['A']),prod(y,s['B'])))
 R=add(prod(chi,y,q),cubic,er,prod(s['R1'],rx),prod(s['R2'],ry),sb);assert L==R
 return {'reflection_series_checks':count,'coupling_polynomial_monomials':len(L),'coupling_identity':'PASS'}

def run():
 for path,digest in PINS.items():assert sha(B/path)==digest,(path,'dependency changed')
 face=json.loads((B/'../edge_velocity/evidence/verdict.json').read_text());assert face['status']=='CONFIRMED' and sha(B/'../edge_velocity/PROOF.md')==face['files']['research/edge_velocity/PROOF.md']
 cases=[]
 for b,g,x1,x2,d in [(F(3403,1000),F(23,20),F(1),F(7),F(9,20)),(F(3),F(23,20),F(1),F(7),F(9,20))]:
  assert F(5,2)<b<F(7,2) and 0<g<2 and x1>2*d>0
  d0=d/4;length=x2-x1;av={};vv={};fac=math.factorial
  SA=aa(2)**aa(2*b-7)*fac(7)/aa((7-2*b)*fac(3)**2);SK=aa(2)**aa(-2*b-1)/aa(2*b+1);C=aa(2)**aa(b)+SA.sqrt()+SK.sqrt()
  def imoment(p,a):return iv.gamma(iq(p+1))/iq(a)**iq(p+1)
  iSA=iq(F(1,4*fac(3)**2))*2*2*iq(2)**iq(-(7-2*b))/iq(7-2*b)*imoment(7,1)
  iSK=iq(F(1,4))*2*2*iq(2)**iq(-(2*b+1))/iq(2*b+1)*imoment(1,1);iC=iq(2)**iq(b)+iv.sqrt(iSA)+iv.sqrt(iSK);Ms=[];iMs=[];Js=[];iJs=[]
  for j in range(3):
   SB=aa(2)**aa(-2*b-1)*fac(2*j+1)/aa((2*b-2*j-1)*fac(j)**2);SC=3*aa(2)**aa(2*b-1)*fac(2*j+1)/fac(j)**2;C+=SB.sqrt()+SC.sqrt()
   iSB=iq(F(1,4*fac(j)**2))*4*iq(2)**iq(2*j+1-2*b)/iq(2*b-2*j-1)*imoment(2*j+1,2);iSC=iq(F(3,4*fac(j)**2))*iq(2)**iq(2*b)*2*imoment(2*j+1,1);iC+=iv.sqrt(iSB)+iv.sqrt(iSC)
   c=aa(2*b+1).gamma().sqrt()*aa(2)**aa(-b-1)/fac(j);ic=iv.sqrt(2*imoment(2*b,2))/(2*fac(j));e=(2*aa(2*d)**aa(2*b+1)/aa(2*b+1)).sqrt()/(2*fac(j));iee=iv.sqrt(2*iq(2*d)**iq(2*b+1)/iq(2*b+1))/(2*fac(j))
   # Max branch is proved by separated interval bounds, not chosen from a midpoint.
   assert c>e and ie(ic)[0]>ie(iee)[1];M=c;iM=ic;J=(aa(F(2)/(2*b-2*j-1))*aa(d0)**aa(2*j+1-2*b)).sqrt();iJ=iv.sqrt(2*iq(d0)**iq(2*j+1-2*b)/iq(2*b-2*j-1));Ms.append(M);iMs.append(iM);Js.append(J);iJs.append(iJ)
   av.update({f'c{j}':c,f'e{j}':e,f'J{j}':J,f'trace_H{j}':aa(2)**aa((b-j-F(1,2))/2)*M});vv.update({f'c{j}':ic,f'e{j}':iee,f'J{j}':iJ,f'trace_H{j}':iq(2)**iq((b-j-F(1,2))/2)*iM})
  Kn=C+sum((x*y for x,y in zip(Ms,Js)),arb(0));iKn=iC+sum((x*y for x,y in zip(iMs,iJs)),iv.mpf(0));RB=aa(x2*x2+d*d/4).sqrt();R0=2*RB;iRB=iv.sqrt(iq(x2*x2+d*d/4));iR0=2*iRB
  J=((1+1/R0)**aa(2*g)*arb.pi()/2*R0**aa(2*g-4)/aa(4-2*g)).sqrt();iJ=iv.sqrt((1+1/iR0)**iq(2*g)*(iv.pi/2)*iR0**iq(2*g-4)/iq(4-2*g));As=[];iAs=[]
  for m in range(5):
   gm=aa(F(128,9))*RB if m==0 else 4*fac(m+1)*2**(m+2)*R0**(1-m);igm=iq(F(128,9))*iRB if m==0 else 4*fac(m+1)*2**(m+2)*iR0**(1-m)
   A=fac(m+1)/(2*arb.pi())*aa(2/d)**(m+2)*(arb.pi()*R0**2).sqrt()*(1+R0)**aa(g)+gm*J/(4*arb.pi())
   weighted_area=iv.sqrt(iv.pi)*iR0*(1+iR0)**iq(g);ideriv=fac(m+1)*iq(2/d)**(m+2)/(2*iv.pi);iA=ideriv*weighted_area+igm/(2*iv.pi)*(iJ/2);As.append(A);iAs.append(iA);av[f'A{m}']=A;vv[f'A{m}']=iA
  k3=(2*aa(d/2)**aa(7-2*b)/aa(7-2*b)).sqrt();ik3=iv.sqrt(2*iq(d/2)**iq(7-2*b)/iq(7-2*b));k5=(2*aa(d/2)**aa(11-2*b)/aa(11-2*b)).sqrt();ik5=iv.sqrt(2*iq(d/2)**iq(11-2*b)/iq(11-2*b))
  Kf=As[3]/6*aa(length).sqrt()*k3+sum((As[j]/fac(j)*aa(length).sqrt()*Js[j] for j in range(3)),arb(0));iKf=iAs[3]/6*iv.sqrt(iq(length))*ik3+sum((iAs[j]/fac(j)*iv.sqrt(iq(length))*iJs[j] for j in range(3)),iv.mpf(0))
  av.update(C=C,K_n=Kn,K_f=Kf,k3=k3,k5=k5,Jfar=J);vv.update(C=iC,K_n=iKn,K_f=iKf,k3=ik3,k5=ik5,Jfar=iJ)
  vals={key:compare(a,vv[key]) for key,a in av.items()};cases.append({'inputs_exact':{key:str(value) for key,value in [('b',b),('g',g),('x1',x1),('x2',x2),('d',d)]},'values':vals})
 r={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_REQUIRES_REVIEW','source_sha256':sha(__file__),'proof_sha256':sha(B/'PROOF.md'),'lead_snapshot_sha256':sha(E/'lead_collar_v2.md'),'Arb_bits':ctx.prec,'iv_dps':iv.dps,'interval_containments':sum(len(c['values']) for c in cases),'exact_identities':exact_identities(),'cases':cases,'dependency_pins':PINS,'scope':'Constants for the proved local collar bounds. No floating lead output is trusted and no global inverse is asserted.'};(E/'constants_audit.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({'status':r['status'],'containments':r['interval_containments'],'exact':r['exact_identities'],'cases':[{key:c['values'][key]['arb_display'] for key in ['K_n','A0','K_f']} for c in cases]},indent=2))
if __name__=='__main__':run()
