"""High-precision far coefficients from binary data, independent homogeneous inverse."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,hashlib
import numpy as np
import mpmath as mp
ap=argparse.ArgumentParser();ap.add_argument('snapshot');ap.add_argument('--tag',default='qfree_N64_first');ap.add_argument('--evaluation',default='evidence/q_evaluations/qfree_N64_far/q2.json');ap.add_argument('--min-radius',type=float,default=1e8);args=ap.parse_args()
mp.mp.dps=85
data=np.load(args.snapshot,allow_pickle=False);N=int(data['N']);M=int(data['M']);L=mp.mpf(float(data['L']));kap=mp.mpf(float(data['p']));ell=mp.mpf(float(data['cl']));eta=1/kap;p=1-eta;D=ell-1
u=[mp.mpf(float(v)) for v in data['u']];ends=[];derivs=[];coef=[];start=0
for k in range(M):
 cc=u[start:start+N+1-k];start+=N+1-k;coef.append(cc);ends.append(mp.fsum(cc));derivs.append(mp.fsum(j*j*v for j,v in enumerate(cc)))
qn={};rn={}
def addmode(dic,n,v):
 if n==0:return
 if n<0:n=-n;v=-v
 dic[n]=dic.get(n,mp.mpf(0))+v
for k in range(M):
 ff=L**eta*ends[k]/2;gg=L**(2*eta)*(-eta*ends[k]/4-derivs[k]-mp.mpf(k)*ends[k]/2)/2
 # sin theta cos(2k theta)=(sin((1+2k)theta)+sin((1-2k)theta))/2
 for n in [1+2*k,1-2*k]:addmode(qn,n,ff/2);addmode(rn,n,gg/2)
ph={}
for m in range(2,2*M+1,2):ph[m]=((p-(m-1))*qn.get(m-1,0)+(p+(m+1))*qn.get(m+1,0))/(2*(m*m-(p+1)**2))
def harmonic(theta):
 th0=mp.fsum(v*mp.sin(n*theta) for n,v in qn.items());th0p=mp.fsum(n*v*mp.cos(n*theta) for n,v in qn.items());th1=mp.fsum(v*mp.sin(n*theta) for n,v in rn.items())
 ur=-mp.fsum(m*v*mp.cos(m*theta) for m,v in ph.items());ut=(p+1)*mp.fsum(v*mp.sin(m*theta) for m,v in ph.items());non=p*ur*th0+ut*th0p
 return {'Theta0':th0,'Theta0prime':th0p,'Theta1_Q':th1,'u0r':ur,'u0theta':ut,'nonlinear_coefficient':non,'C2_delta_zero':-D*th1+non,'C2_actual':(ell*(2*p-1)-1)*th1+non}
def poly_pair(cc,t):
 b1=mp.mpf(0);b2=mp.mpf(0);d1=mp.mpf(0);d2=mp.mpf(0)
 for v in cc[:0:-1]:
  b0=v+2*t*b1-b2;d0=2*b1+2*t*d1-d2;b2,b1=b1,b0;d2,d1=d1,d0
 return cc[0]+t*b1-b2,b1+t*d1-d2

def radial_z(r):
 target=mp.log(r/L)
 if target<=-mp.log(2)/2:
  lo=mp.mpf(0);hi=mp.mpf('.5');sig=min(mp.mpf('.49'),mp.exp(2*target+2*kap*mp.log(2)))
  for unused in range(350):
   val=mp.log(sig)/2-kap*mp.log(2*(1-sig))-target
   if val>0:hi=sig
   else:lo=sig
   new=sig-val/(1/(2*sig)+kap/(1-sig))
   if not lo<new<hi:new=(lo+hi)/2
   if abs(new-sig)<mp.mpf('1e-80')*max(abs(sig),mp.mpf('1e-300')):return 2*(1-new)
   sig=new
  raise ArithmeticError('High-precision inner radial map failed')
 z=min(mp.mpf('.999'),mp.exp(-target/kap));lo=mp.mpf(0);hi=mp.mpf(1)
 for unused in range(350):
  val=kap*mp.log(z)-mp.log1p(-z/2)/2+target
  if val>0:hi=z
  else:lo=z
  new=z-val/(kap/z+1/(4*(1-z/2)))
  if not lo<new<hi:new=(lo+hi)/2
  if abs(new-z)<mp.mpf('1e-80')*abs(z):return new
  z=new
 raise ArithmeticError('High-precision exterior radial map failed')

def density(r,theta):
 z=radial_z(r)
 sig=1-z/2;F=mp.mpf(0);Fz=mp.mpf(0)
 for k,cc in enumerate(coef):
  val,der=poly_pair(cc,1-z);angle=mp.cos(2*k*theta);F+=sig**k*val*angle;Fz+=(-mp.mpf(k)/2*sig**(k-1)*val-sig**k*der)*angle
 rho=r*z/2*mp.sin(theta)*F
 slope=z/2*mp.sin(theta)*(F-(F+z*Fz)/(kap+z/(4*sig)))
 return rho,slope
rows=[]
for theta in [mp.mpf('.0037'),mp.mpf('.039'),mp.mpf('.231'),mp.mpf('.789'),mp.mpf('1.487'),mp.pi/2]:
 vals=harmonic(theta);rows.append({'theta':mp.nstr(theta,45),**{k:mp.nstr(v,55) for k,v in vals.items()}})
limits=[]
for rr in [10,14,18,22,26,30,40,60,80]:
 r=mp.mpf(10)**rr;theta=mp.pi/2;h=harmonic(theta);actual,slope=density(r,theta);rr1=actual/r**p
 limits.append({'log10_r':rr,'rho_scaled':mp.nstr(rr1,55),'Theta0':mp.nstr(h['Theta0'],55),'second_scaled_density':mp.nstr((actual-r**p*h['Theta0'])/r**(2*p-1),55),'Theta1_Q':mp.nstr(h['Theta1_Q'],55),'axis_rho_r':mp.nstr(slope,55),'leading_predicted_axis_R_Nf':mp.nstr(abs(h['C2_actual'])/(2*abs(h['Theta0']))*r**(-eta),55)})

comparisons=[]
source=Path(args.evaluation)
if source.exists():
 for row in json.loads(source.read_text())['points']:
  if row['x']!=0 or row['y']<=0 or row['radius']<args.min_radius:continue
  r=mp.mpf(float(row['y']));rho,gy=density(r,mp.pi/2);U=mp.mpf(float(row['U'][1]));Rmp=(ell*r+U)*gy-rho;Nf=abs((ell*r+U)*gy)+abs(rho);Nv=abs(rho)+abs(r*gy)+abs(U*gy);fd=mp.mpf(float(row['residuals'][-1]['rho_y']))
  comparisons.append({'radius':row['radius'],'mp_R_Nf':mp.nstr(abs(Rmp)/Nf,55),'mp_R_Nv':mp.nstr(abs(Rmp)/Nv,55),'FD8_R_Nf':row['residuals'][-1]['R_Nf'],'FD8_relative_gradient_error':mp.nstr(abs(fd-gy)/max(abs(gy),mp.mpf('1e-100')),55),'relative_density_difference':mp.nstr(abs(mp.mpf(row['rho'])-rho)/abs(rho),55),'scope':'MP analytic density derivative with independently computed double-precision canonical U; inverse uncertainty remains represented by three quadrature levels.'})

# Independent analytic angular differentiation supplements the radial formula.
def density_gradient(r,theta):
 rho,slope=density(r,theta)
 z=radial_z(r)
 sig=1-z/2;F=mp.mpf(0);Ft=mp.mpf(0)
 for k,cc in enumerate(coef):
  vv,_=poly_pair(cc,1-z)
  F+=sig**k*vv*mp.cos(2*k*theta)
  Ft-=2*k*sig**k*vv*mp.sin(2*k*theta)
 tangential=z/2*(mp.cos(theta)*F+mp.sin(theta)*Ft)
 return rho,mp.cos(theta)*slope-mp.sin(theta)*tangential,mp.sin(theta)*slope+mp.cos(theta)*tangential

full_comparisons=[]
if source.exists():
 ev=json.loads(source.read_text())
 assert int(ev['metadata']['N'])==N and int(ev['metadata']['M'])==M
 assert mp.mpf(float(ev['metadata']['cl']))==ell
 for row in ev['points']:
  if row['y']==0 or row['radius']<args.min_radius:continue
  xx=mp.mpf(float(row['x']));yy=mp.mpf(float(row['y']));r=mp.sqrt(xx*xx+yy*yy);theta=mp.atan2(yy,xx)
  rho,gx,gy=density_gradient(r,theta)
  ux,uy=[mp.mpf(float(v)) for v in row['U']]
  t1=(ell*xx+ux)*gx;t2=(ell*yy+uy)*gy
  residual=t1+t2-rho;nf=abs(t1)+abs(t2)+abs(rho)
  nv=abs(rho)+abs(xx*gx+yy*gy)+abs(ux*gx+uy*gy)
  fd=row['residuals'][-1]
  graderr=mp.sqrt((mp.mpf(fd['rho_x'])-gx)**2+(mp.mpf(fd['rho_y'])-gy)**2)/mp.sqrt(gx*gx+gy*gy)
  full_comparisons.append({'x':row['x'],'y':row['y'],'radius':row['radius'],'mp_abs_R':mp.nstr(abs(residual),55),'mp_R_Nf':mp.nstr(abs(residual)/nf,55),'mp_R_Nv':mp.nstr(abs(residual)/nv,55),'FD8_R_Nf':fd['R_Nf'],'FD8_R_Nv':fd['R_Nv'],'FD8_relative_gradient_error':mp.nstr(graderr,55),'relative_density_difference':mp.nstr(abs(mp.mpf(row['rho'])-rho)/abs(rho),55)})

# Manufactured leading sin1 profile and independently known T1 non-profile.
pp=mp.mpf('.5');qq={1:mp.mpf('.5'),3:mp.mpf('-.5')}
ph2=((pp-1)*qq[1]+(pp+3)*qq[3])/(2*(4-(pp+1)**2));ph4=(pp-3)*qq[3]/(2*(16-(pp+1)**2))
assert abs(ph2+mp.mpf(4)/7)<mp.mpf('1e-80')
assert abs(ph4-mp.mpf(1)/22)<mp.mpf('1e-80')
# The input angular polynomial here is sin(theta)*(1-2cos²theta), giving sin1/2-sin3/2.
# Its stream coefficient is -4/7 sin2 +1/22 sin4, matching the independently derived T1 case.
# Check general scalar radial sin1 against H~r^-eta/(4-eta).
sin1phi=(p-1)/(2*(4-(p+1)**2));assert abs(2*sin1phi+1/(p+3))<mp.mpf('1e-80')
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','snapshot':str(Path(args.snapshot).resolve()),'sha256':hashlib.sha256(Path(args.snapshot).read_bytes()).hexdigest(),'precision_digits':mp.mp.dps,'derivative_comparison_min_radius':args.min_radius,'ell':str(ell),'map_kappa':str(kap),'p':str(p),'ell_p_minus1':mp.nstr(ell*p-1,55),'angular_rows':rows,'axis_density_limits':limits,'axis_derivative_comparisons':comparisons,'full_far_derivative_comparisons':full_comparisons,'evaluation_source':str(source),'checks':['finite trig product and homogeneous sin1 inverse','manufactured sin1-sin3 angular stream'],'scope':'Exact binary coefficients evaluated at85digits. Canonical homogeneous far inverse separately implemented. Nonzero second coefficient refutes this finite interpolant only. No interval rounding enclosure or continuum convergence certificate.'}
out=Path('research/finite_q_far_coefficients/verification');out.mkdir(exist_ok=True);(out/(args.tag+'.json')).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
