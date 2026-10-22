"""Exact tail coefficients and independent high-precision Cartesian manufactures."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,time,sys,hashlib
import numpy as np
import mpmath as mp
from r2_state_values import R2State
from exact_tail_residuals import COS,SIN,COS2,add,mul,scale,deriv,inv,chebs,linear,endpoints,ser,exactpoint,witness
root=Path('research/101_native_source_mixed_powers/verification');start=time.monotonic();mp.mp.dps=60
out={'started_utc':datetime.now(timezone.utc).isoformat(),'source_axis_tests':[],'cartesian':[]}
def mq(x):return mp.mpf(x.numerator)/x.denominator
def angular(poly,xx,yy):
 z=mp.mpc(xx,yy);ans=mp.mpc(0)
 for n,c in poly.items():ans+=(mq(c[0])+1j*mq(c[1]))*z**n
 assert abs(ans.imag)<mp.mpf('1e-48')*(1+abs(ans.real))
 return ans.real

def homogeneous(power,poly,x,y):
 r=mp.sqrt(x*x+y*y);return r**mq(power)*angular(poly,x/r,y/r)
def interaction(p,k,a,power):return add(scale(mul(p,deriv(a)),k),scale(mul(deriv(p),a),-power))
def dxangular(a,power):return add(scale(mul(COS,a),power),scale(mul(SIN,deriv(a)),Q(-1)))
# Certify a simple source-stream zero for both real seed defects.
for tag in ['blam12v','blam16v']:
 path=Path('verification/fixed_velocity_block_20261021T0056')/(tag+'_jet_schema_manufacture.npz');state=R2State(path);sf=state.seed_field
 assert sf.bb==3.
 vals,_=endpoints(sf,sf.rawG);A=mul(COS,linear(vals,chebs(sf.K)));P=inv(A,Q(5,3))
 axes=[]
 for sy in [Q(-1),Q(1)]:
  p=exactpoint(P,Q(0),sy);dp=exactpoint(deriv(P),Q(0),sy);assert p==0 and dp!=0
  axes.append({'sin_theta':str(sy),'PS0_value':str(p),'PS0_derivative':str(dp),'PS0_derivative_float':float(dp)})
 out['source_axis_tests'].append({'tag':tag,'source_schema_sha256':state.sha256,'native_L':sf.L,'native_K':sf.K,'native_Nt':sf.Nt,'axes':axes,'AS0':ser(A),'PS0':ser(P),'verdict':'BOTH_SOURCE_AXIS_ZEROS_EXACTLY_SIMPLE'})
 print(tag,[a['PS0_derivative_float'] for a in axes],flush=True)

# Finite homogeneous fields, used only on the punctured plane, with their exact
# whole-plane relative inverse. They are not claimed to be smooth profiles.
a=mul(COS,add({0:(Q(1),Q(0))},scale(SIN,Q(2,7))))
b=add(scale(COS,Q(1,5)),scale(mul(SIN,COS),Q(-2,11)))
h=mul(COS2,add({0:(Q(1),Q(0))},scale(SIN,Q(3,7))))
d=mul(COS2,add({0:(Q(2,9),Q(0))},scale(SIN,Q(-1,13))))
aS=add(scale(COS,Q(-2)),scale(mul(SIN,COS),Q(1,3)))
sigma=Q(1,3);kS=2-sigma;pS=inv(aS,kS);ell=Q(7,10)
for beta in [Q(31,10),Q(10,3),Q(7,2),Q(39,10)]:
 s=1/beta;m=1-2*s;k=2-s;k1=2-2*s;p0=inv(a,k);p1=inv(b,k1)
 ET=add(scale(d,Q(-1)),interaction(p0,k,h,m));DT=interaction(pS,kS,h,m)
 EO=add(scale(b,Q(-1)),interaction(p0,k,a,-s),scale(dxangular(h,m),Q(-1)));DO=interaction(pS,kS,a,-s)
 assert m-s>m-sigma>0>m-2*s
 assert -2*s>-s-sigma>-3*s
 e=scale(DT,ell/(beta*sigma));c=scale(DO,ell/(beta*sigma))
 assert not add(scale(e,-beta*sigma),scale(DT,ell));assert not add(scale(c,-beta*sigma),scale(DO,ell))
 termsT=[(m-s,ET),(m-sigma,scale(DT,ell)),(m-2*s,add(interaction(p0,k,d,m-s),interaction(p1,k1,h,m))),(m-3*s,interaction(p1,k1,d,m-s)),(m-s-sigma,scale(interaction(pS,kS,d,m-s),ell))]
 termsO=[(-2*s,EO),(-s-sigma,scale(DO,ell)),(-3*s,add(interaction(p0,k,b,-2*s),interaction(p1,k1,a,-s),scale(dxangular(d,m-s),Q(-1)))),(-4*s,interaction(p1,k1,b,-2*s)),(-2*s-sigma,scale(interaction(pS,kS,b,-2*s),ell))]
 def psi(x,y):return homogeneous(k,p0,x,y)+homogeneous(k1,p1,x,y)+mq(ell)*homogeneous(kS,pS,x,y)
 def theta(x,y):return homogeneous(m,h,x,y)+homogeneous(m-s,d,x,y)
 def omega(x,y):return homogeneous(-s,a,x,y)+homogeneous(-2*s,b,x,y)
 for R in [mp.mpf('0.7'),mp.mpf(3),mp.mpf(20),mp.mpf('1e4')]:
  for cx,sy in [(Q(3,5),Q(4,5)),(Q(-5,13),Q(12,13))]:
   x=R*mq(cx);y=R*mq(sy);u1=-mp.diff(lambda yy:psi(x,yy),y);u2=mp.diff(lambda xx:psi(xx,y),x);W=[mq(beta)*x+u1,mq(beta)*y+u2]
   tx=mp.diff(lambda xx:theta(xx,y),x);ty=mp.diff(lambda yy:theta(x,yy),y);ox=mp.diff(lambda xx:omega(xx,y),x);oy=mp.diff(lambda yy:omega(x,yy),y)
   rt=W[0]*tx+W[1]*ty-(mq(beta)-2)*theta(x,y);ro=W[0]*ox+W[1]*oy+omega(x,y)-tx
   pt=sum(homogeneous(q,P,x,y) for q,P in termsT);po=sum(homogeneous(q,P,x,y) for q,P in termsO)
   errT=abs(rt-pt)/(1+abs(rt));errO=abs(ro-po)/(1+abs(ro));assert max(errT,errO)<mp.mpf('1e-45')
   # Direct Cartesian Laplacian checks the chosen full-plane sign independently.
   ep=-(mp.diff(lambda xx:psi(xx,y),x,2)+mp.diff(lambda yy:psi(x,yy),y,2))-omega(x,y)-mq(ell)*homogeneous(-sigma,aS,x,y)
   assert abs(ep)/(1+abs(omega(x,y)))<mp.mpf('1e-45')
   out['cartesian'].append({'beta':str(beta),'r':str(R),'cos':str(cx),'sin':str(sy),'relative_temperature_expansion_error':str(errT),'relative_vorticity_expansion_error':str(errO),'elliptic_error':str(ep)})
 print('Cartesian beta',beta,'passed',flush=True)
out['exact_coefficient_tests']={'beta_count':4,'ordering_and_missing_power_checks':16,'mixed_correction_cancellations':8,'source_axes':4,'cartesian_rows':len(out['cartesian'])}
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),scope='Exact rational checks of real stored source tails plus punctured-plane homogeneous manufactures. No B2 profile or rigorous floating inverse certificate.')
(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
