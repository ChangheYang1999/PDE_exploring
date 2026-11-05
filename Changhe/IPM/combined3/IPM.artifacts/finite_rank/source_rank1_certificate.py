#!/usr/bin/env python3
"""Rigorous actual Candidate013 Cvs3 coefficient at phi_01 via Acb integration.

Certifies A_11 only. Finite-rank tail additionally needs a certified HS upper.
All removed angular harmonics are exactly orthogonal to the test products.
"""
import argparse,json,sys,time
from pathlib import Path
from flint import arb,acb,acb_series,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'coercivity_residual'))
import fields013 as ff
from asymptotics013 import Expansion
import hermite_polar as hp
from hermite_gram import packet,build
from interval_matrix import certify


def fourier(modes):
 out={}
 for (kind,n),v in modes.items():
  if n==0:out[0]=out.get(0,acb(0))+v
  else:
   c=v/2 if kind=='c' else v/acb(0,2)
   out[n]=out.get(n,acb(0))+c;out[-n]=out.get(-n,acb(0))+(c if kind=='c' else -c)
 return out

def product(a,b):
 out={}
 for i,v in a.items():
  for j,w in b.items():out[i+j]=out.get(i+j,acb(0))+v*w
 return out

def adiff(a,b,sign=1):
 out=dict(a)
 for i,v in b.items():out[i]=out.get(i,acb(0))+sign*v
 return out


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--bits',type=int,default=384);ap.add_argument('--tolerance',default='1e-9');ap.add_argument('--origin',default='.0001');ap.add_argument('--far',default='1000');ap.add_argument('--middle',default='32');ap.add_argument('--eval-limit',type=int,default=200000);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 ctx.prec=args.bits;start=time.time();ee=ff.Evaluator(args.bits,max_density_order=1,max_velocity_order=0)
 ee.groups=[row for row in ee.groups if row[1]<=8]
 orig=Expansion(ee,'origin',degree=12);far=Expansion(ee,'far',degree=12)
 delta,R=arb(args.origin),arb(args.far)
 gx=orig.point_bound('rho',1,0,delta);gy=orig.point_bound('rho',0,1,delta)
 # Entire basis radial formulas admit direct interval evaluation at r in[0,delta].
 h=hp.HermitePolar(0,1);hm=h.modes(arb(delta/2,delta/2))
 def supmode(mm):return sum((abs(v) for v in mm.values()),arb(0))
 ph,r1,r2,u1,u2=[supmode(hm[k]) for k in ['phi','r1','r2','u1','u2']]
 origin_err=arb.pi()*delta**2*(gx*(ph*u1+r1*r2)+gy*(ph*u2+r1*r1))
 G=far.point_bound('rho',1,0,R)+far.point_bound('rho',0,1,R)
 assert R>=16
 c=(2/arb.pi()).sqrt()
 tail_err=G*(4*c*(R+1/R)*(-R*R/2).exp()+25*arb.pi()/(2*R**4))
 print('bounds prepared',time.time()-start,'origin',origin_err,'tail',tail_err,flush=True)
 # Process-local complex extension. Every positive radial power is evaluated on
 # Re(1+r²)>0 and Re(t+r²)>0 when analytic evaluation is requested.
 ff.arb,ff.arb_series=acb,acb_series
 hp.arb=acb
 ec=ff.Evaluator(args.bits,max_density_order=1,max_velocity_order=0)
 ec.prepared=[row for row in ec.prepared if row[1]<=8]
 hc=hp.HermitePolar(0,1)
 calls=[0]
 def integrand_raw(r,analytic):
  calls[0]+=1
  if not r.real>0:return acb('nan')
  rr=r*r
  if not (1+rr).real>0 or not (acb(1)/8+rr).real>0:return acb('nan')
  b=ec.modes_at(r);v={k:fourier(m) for k,m in hc.modes(r).items()}
  dx=adiff(product(v['phi'],v['u1']),product(v['r1'],v['r2']),-1)
  dy=adiff(product(v['phi'],v['u2']),product(v['r1'],v['r1']))
  ans=acb(0)
  for key,prod in [(('rho',1,0),dx),(('rho',0,1),dy)]:
   bm=fourier(b[key])
   ans+=sum((val*bm.get(-n,acb(0)) for n,val in prod.items()),acb(0))
  return 2*acb.pi()*r*ans
 def integrand(r,analytic):
  try:return integrand_raw(r,analytic)
  except (ValueError,ZeroDivisionError):return acb('nan')
 vals=[]
 # Bernstein ellipse rho=2 is contained in the complex rectangle
 # c+[-5h/4,5h/4]+i[-3h/4,3h/4]. Chebyshev approximation of
 # degree2n-1 and exactness/positivity of Gaussian weights yield error
 # <=16*h*M*2^(-2n), where M bounds |f| on that rectangle.
 from fractions import Fraction as Rat
 left=Rat(args.origin);right=Rat(args.far);panels=[]
 while left<right:
  endpoint=min(right,left*Rat(3,2));panels.append((left,endpoint));left=endpoint
 target=arb(args.tolerance)/len(panels)
 nodes_cache={};records=[]
 panel=0
 while panel<len(panels):
  qa,qb=panels[panel]
  aa=arb(qa.numerator)/qa.denominator;bb=arb(qb.numerator)/qb.denominator
  cc=(aa+bb)/2;hh=(bb-aa)/2
  contour=acb(arb(cc,5*hh/4),arb(0,3*hh/4))
  Mbound=abs(integrand(contour,True))
  if not Mbound.is_finite():
   mid=(qa+qb)/2;panels[panel:panel+1]=[(qa,mid),(mid,qb)]
   continue
  target=arb(args.tolerance)*(bb-aa)/(R-delta)
  n=16
  while not 16*hh*Mbound*arb(2)**(-2*n)<target:
   n+=16
   if n>1024:raise RuntimeError('Contour error needs more than1024 nodes')
  if n not in nodes_cache:nodes_cache[n]=[arb.legendre_p_root(n,k,weight=True) for k in range(n)]
  zz=acb(0)
  for x,w in nodes_cache[n]:zz+=w*integrand(acb(cc+hh*x),False)
  zz*=hh
  error=16*hh*Mbound*arb(2)**(-2*n)
  zz+=acb(arb(0,error.upper()),arb(0,error.upper()))
  vals.append(zz)
  records.append({'panel':panel,'left':str(aa),'right':str(bb),'nodes':n,'contour_M':str(Mbound),'gauss_error_bound':str(error),'integral':str(zz)})
  print('panel',panel+1,'of',len(panels),'n',n,'value',zz.str(14),'seconds',time.time()-start,flush=True)
  args.output.with_suffix('.checkpoint.json').write_text(json.dumps({'status':'PARTIAL_QUADRATURE_ONLY','records':records,'origin_error':str(origin_err),'tail_error':str(tail_err)},indent=2)+'\n')
  panel+=1
 value=sum(vals,acb(0));assert value.imag.contains(0)
 A=value.real+arb(0,(origin_err+tail_err).upper())
 # Restore real backend before using B Gram.
 ff.arb,ff.arb_series=arb,__import__('flint').arb_series;hp.arb=arb
 gram=build(1,bits=args.bits);B=arb(gram['B'][0][0]['ball'])
 finite=certify([[A]],[[B]],bits=args.bits)
 out={'status':'RIGOROUS_A11_AND_GRAM_ONLY','basis':'normalized S1 Hermite phi_01(x,y)=sqrt(2/pi)*y*exp(-(x²+y²)/2)','q':'21/10','A11':packet(A),'B11':gram['B'][0][0],'finite_rank_C_N':finite,'origin_radius':args.origin,'far_radius':args.far,'origin_absolute_error':packet(origin_err),'far_absolute_error':packet(tail_err),'integrals':[str(z) for z in vals],'panels':records,'quadrature_proof':'Bernsteinellipse rho2; Chebyshevdegree2n-1 bestapprox bound2M*rho^-2n/(1-rho^-1); Gausspositiveexact weights then error16hM2^-2n.','calls':calls[0],'bits':args.bits,'elapsed_seconds':time.time()-start,'angular_selection':'Dx,Dy have only harmonics up to4; omitted potential harmonicsn>8 cannot contribute to b gradientsn≤4.','warning':'No HS upper or finite-rank operator tail is certified here; no IPM closure assertion.'}
 args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
