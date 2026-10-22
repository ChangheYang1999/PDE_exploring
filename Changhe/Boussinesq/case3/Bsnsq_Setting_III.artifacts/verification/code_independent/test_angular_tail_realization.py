"""Independent manufactured controls for147, no lead or NUM code used."""
from pathlib import Path
import sys,json,datetime,time,math
import numpy as np
import sympy as S
from numpy.polynomial.legendre import leggauss
from scipy.special import betainc,beta as beta_fn
from scipy.integrate import solve_ivp
root=Path(sys.argv[1]);root.mkdir(parents=True,exist_ok=True);start=time.monotonic()
r,th,m=S.symbols('r theta m',positive=True);f=S.Function('f')(th);A=S.Function('A')(th)
R=r/S.sqrt(S.diff(f,th));phi=f
exact=[{'name':'polar_area_jacobian','pass':S.simplify(R*(S.diff(R,r)*S.diff(phi,th)-S.diff(R,th)*S.diff(phi,r))/r-1)==0},
 {'name':'homogeneous_radial_map','pass':S.simplify(r*S.diff(R,r)-R)==0},
 {'name':'pulled_temperature_homogeneity','pass':S.simplify(r*S.diff(r**m*A,r)-m*r**m*A)==0}]
H=lambda t:betainc(8,8,np.clip(t,0,1))
l=-np.pi/2;u=np.pi/2;edge=.03;width=.08
class Compression:
 def __init__(self,a,b):
  self.a=a;self.b=b
  self.knots=np.unique([l,l+edge,l+2*edge,l+3*edge,a-width,a,b,b+width,u-3*edge,u-2*edge,u-edge,u])
  self.knots.sort();z,w=leggauss(24);self.z=z;self.w=w
  nodes=np.concatenate([aa+(bb-aa)*(z+1)/2 for aa,bb in zip(self.knots[:-1],self.knots[1:])]);weights=np.concatenate([(bb-aa)*w/2 for aa,bb in zip(self.knots[:-1],self.knots[1:])])
  bl,bu,br,bur=self.pieces(nodes);self.cl=(np.pi/2-np.sum(weights*bl))/np.sum(weights*bu);self.cr=(np.pi/2-np.sum(weights*br))/np.sum(weights*bur)
  assert self.cl>0 and self.cr>0
  self.prefix=[0.]
  for aa,bb in zip(self.knots[:-1],self.knots[1:]): self.prefix.append(self.prefix[-1]+(bb-aa)/2*np.sum(w*self.d0(aa+(bb-aa)*(z+1)/2)))
  self.prefix=np.array(self.prefix)
 def pieces(self,x):
  x=np.asarray(x);hl=H((self.a-x)/width);hr=H((x-self.b)/width);el=1-H((x-l-edge)/edge);er=1-H((u-x-edge)/edge)
  return (.01+.99*el)*hl,H((x-l-2*edge)/edge)*hl,(.01+.99*er)*hr,H((u-x-2*edge)/edge)*hr
 def d0(self,x):
  bl,bu,br,bur=self.pieces(x);return bl+self.cl*bu+br+self.cr*bur
 def g0(self,x):
  x=np.asarray(x);idx=np.clip(np.searchsorted(self.knots,x,side='right')-1,0,len(self.knots)-2);a=self.knots[idx];nodes=a[:,None]+(x-a)[:,None]*(self.z[None,:]+1)/2
  return l+self.prefix[idx]+(x-a)/2*np.sum(self.w[None,:]*self.d0(nodes),axis=1)
 def quadrature(self,n):
  z,w=leggauss(n);return np.concatenate([a+(b-a)*(z+1)/2 for a,b in zip(self.knots[:-1],self.knots[1:])]),np.concatenate([(b-a)*w/2 for a,b in zip(self.knots[:-1],self.knots[1:])])
controls=[]
for name,a,b,sigma in [('negative',-.2,.2,-1),('positive',1.05,1.25,1)]:
 c=Compression(a,b)
 for beta in [2.25,3.,6.]:
  s=1/beta;mm=1-2*s;rows=[]
  for order in [64,128]:
   ph,wt=c.quadrature(order);d0=c.d0(ph);g0=c.g0(ph)
   for eps in [1e-3,1e-8,1e-16,1e-32,1e-64]:
    gp=eps+(1-eps)*d0;g=eps*ph+(1-eps)*g0;af=np.cos(g)**2/gp**(mm/2);moment=float(2*np.sum(wt*(1-(mm+2)*np.cos(ph)**2)*af))
    rows.append({'order':order,'epsilon':eps,'moment':moment})
  endpoint_error=abs(c.prefix[-1]-np.pi);target=rows[-1]['moment'];controls.append({'family':name,'beta':beta,'total_derivative_error':endpoint_error,'coefficients':[c.cl,c.cr],'rows':rows,'pass':endpoint_error<1e-12 and sigma*target>0})
# Direct transport through an actual restored homogeneous-stream exterior.
# Incoming angular temperature A=cos^2. Integrate to log(r/N)=25/s.
scattering=[]
for beta in [2.25,3.,6.]:
 s=1/beta;mm=1-2*s;angles=np.array([-1.25,-.8,-.2,.3,.9,1.27]);B=.2
 for N in [10.,100.,1000.]:
  eps=N**(-s)
  def fun(t,Y):
   theta=Y[:len(angles)];logamp=Y[len(angles):];z=math.exp(t) if t<1 else math.e
   if t>=math.log(2):cut=1.;rgrad=0.
   else:
    h=z-1;cut=float(H(h));rgrad=z*h**7*(1-h)**7/beta_fn(8,8) if 0<h<1 else 0.
   er=-B*eps*math.exp(-s*t)*cut*np.sin(theta);et=-B*eps*math.exp(-s*t)*((2-s)*cut+rgrad)*np.cos(theta)
   return np.r_[et/(beta+er),-mm*er/(beta+er)]
  sol=solve_ivp(fun,[0,25/s],np.r_[angles,np.zeros_like(angles)],method='DOP853',rtol=2e-11,atol=2e-13,max_step=1.)
  angle_error=float(np.max(abs(sol.y[:len(angles),-1]-angles)));amp_error=float(np.max(abs(np.expm1(sol.y[len(angles):,-1]))));scattering.append({'beta':beta,'N':N,'epsilon':eps,'max_angle_error':angle_error,'max_multiplier_error':amp_error,'scaled_angle_error':angle_error/eps,'scaled_multiplier_error':amp_error/eps,'pass':bool(sol.success and angle_error/eps<2 and amp_error/eps<2)})
result={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'exact_controls':exact,'compression_controls':controls,'exterior_scattering_controls':scattering,'all_pass':all(z['pass'] for z in exact+controls+scattering),'scope':'Independent exact map identities, C7 angular compression manufactures and exterior exact-thermal characteristic integration. No finite global147 reference or148 zero-impulse glued field was computed. These finite controls supplement, not replace, the analytic proofs.'}
(root/'tests.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'all_pass':result['all_pass'],'counts':[len(exact),len(controls),len(scattering)],'elapsed_seconds':result['elapsed_seconds'],'moment_final':[(z['family'],z['beta'],z['rows'][-1]['moment'])for z in controls],'scattering_scaled_max':max(max(z['scaled_angle_error'],z['scaled_multiplier_error'])for z in scattering)},indent=2))
if not result['all_pass']:raise SystemExit(1)
