"""Independent finite-polynomial tests of the analytic center recurrence."""
import json,datetime,math
from pathlib import Path
import numpy as np
from high_order_jets import compute,derivative,pmul
from read_polar_data import PolarData
D=np.longdouble

def lowerP(i,j,h,a):
 n=i+j;ans=D(0)
 for (p,q),hv in h.items():
  u=i-p;v=j-q
  if 1<=p+q<=n-1 and u>=0 and v>=0:ans+=(-2*u*(2*q+1)+(2*p+1)*(2*v+1))*hv*a.get((u,v),0)
 return ans

def lowerQ(i,j,h,g):
 ans=D(0)
 for (p,q),hv in h.items():
  u=i-p;v=j-q
  if p+q>=1 and u>=0 and v>=0:ans+=(-(2*q+1)*(2*u+1)+(2*p+1)*(2*v+1))*hv*g.get((u,v),0)
 return ans

def fields(a,h,g,degree=14):
 A=np.zeros((degree+1,degree+1),dtype=D);H=A.copy();G=A.copy()
 for (i,j),v in a.items():A[2*i,2*j+1]=v
 for (i,j),v in h.items():H[2*i+1,2*j+1]=v
 for (i,j),v in g.items():G[2*i+1,2*j+1]=v
 return A,H,G

def residuals(a,h,g,beta):
 A,H,G=fields(a,h,g);wx=-derivative(H,1);wy=derivative(H,0);wx[1,0]+=beta;wy[0,1]+=beta
 rt=pmul(wx,derivative(A,0))+pmul(wy,derivative(A,1))-(beta-2)*A
 ro=pmul(wx,derivative(G,0))+pmul(wy,derivative(G,1))+G-derivative(A,0)
 return rt,ro

def manufactured():
 rng=np.random.default_rng(20261020);rows=[]
 for beta in [2.17,3.,5.3]:
  h={(i,j):D(rng.uniform(-.3,.3)) for n in range(6) for i in range(n+1) for j in [n-i]};h[0,0]=D(-2)
  a={(i,j):D(rng.uniform(-2,2)) for n in range(6) for i in range(n+1) for j in [n-i]};a[0,0]=D(2.3)
  g={(i,j):-D((2*i+3)*(2*i+2))*h[i+1,j]-D((2*j+3)*(2*j+2))*h[i,j+1] for n in range(5) for i in range(n+1) for j in [n-i]}
  rt,ro=residuals(a,h,g,D(beta));errt=erro=D(0)
  AA,HH,GG=fields(a,h,g);lap=-derivative(derivative(HH,0),0)-derivative(derivative(HH,1),1)
  el=max(abs(lap[2*i+1,2*j+1]-v) for (i,j),v in g.items())
  phi=2*np.arccos(D(-1))*np.arange(128,dtype=D)/128;xx=np.cos(phi);yy=np.sin(phi);eh=D(0)
  for n in range(1,6):
   vals=sum(h[n-j,j]*xx**(2*(n-j)+1)*yy**(2*j+1) for j in range(n+1));projected=2*np.mean(vals*np.sin((2*n+2)*phi))
   formula=sum((-1)**j*h[n-j,j] for j in range(n+1))/D(2)**(2*n+1);eh=max(eh,abs(projected-formula))
  for n in range(1,6):
   for i in range(n+1):
    j=n-i;L=2*i*(beta+2)+2*j*(beta-2)
    expected=L*a[i,j]+(2*i+1)*a[0,0]*h[i,j]+lowerP(i,j,h,a)
    errt=max(errt,abs(expected-rt[2*i,2*j+1]))
   for i in range(n):
    j=n-1-i;M=(2*i+1)*(beta+2)+(2*j+1)*(beta-2)+1
    expected=M*g[i,j]-2*(i+1)*a[i+1,j]+lowerQ(i,j,h,g)
    erro=max(erro,abs(expected-ro[2*i+1,2*j+1]))
  rows.append({'beta':beta,'temperature_formula_max_abs_error':float(errt),'vorticity_formula_max_abs_error':float(erro),'poisson_coefficient_max_abs_error':float(el),'circle_harmonic_projection_max_abs_error':float(eh)})
 return rows

def reconstruct(beta,a0,Cs,N=5):
 h={(0,0):D(-2)};a={(0,0):D(a0)};g={};rows=[]
 for n in range(1,N+1):
  P={(i,n-i):lowerP(i,n-i,h,a) for i in range(n+1)}
  Q={(i,n-1-i):lowerQ(i,n-1-i,h,g) for i in range(n)}
  coeff={(n,0):D(1)};offset={(n,0):D(0)}
  for i in range(n-1,-1,-1):
   j=n-1-i;L=D(2*(i+1)*(beta+2)+2*j*(beta-2));M=D((2*i+1)*(beta+2)+(2*j+1)*(beta-2)+1)
   A=D((2*i+3)*(2*i+2));B=D((2*j+3)*(2*j+2));fac=-A/B*(1-D(a0)/(L*M));other=(Q[i,j]+2*(i+1)*P[i+1,j]/L)/(M*B)
   coeff[i,j+1]=fac*coeff[i+1,j];offset[i,j+1]=fac*offset[i+1,j]+other
  den=sum((-1)**j*coeff[n-j,j] for j in range(n+1));const=sum((-1)**j*offset[n-j,j] for j in range(n+1))
  b=(D(2)**(2*n+1)*D(Cs[str(2*n+2)])-const)/den
  for i in range(n+1):
   j=n-i;h[i,j]=coeff[i,j]*b+offset[i,j];L=D(2*i*(beta+2)+2*j*(beta-2));a[i,j]=-((2*i+1)*D(a0)*h[i,j]+P[i,j])/L
  for i in range(n):
   j=n-1-i;g[i,j]=-D((2*i+3)*(2*i+2))*h[i+1,j]-D((2*j+3)*(2*j+2))*h[i,j+1]
  phi=2*np.arccos(D(-1))*np.arange(128,dtype=D)/128;xx=np.cos(phi);yy=np.sin(phi)
  values=sum(h[n-j,j]*xx**(2*(n-j)+1)*yy**(2*j+1) for j in range(n+1));projected=2*np.mean(values*np.sin((2*n+2)*phi))
  rows.append({'n':n,'moment_projection_error':float(projected-D(Cs[str(2*n+2)])),'moment_linear_coefficient':float(den/D(2)**(2*n+1)),'a':[[i,n-i,float(a[i,n-i])] for i in range(n+1)],'h':[[i,n-i,float(h[i,n-i])] for i in range(n+1)],'g':[[i,n-1-i,float(g[i,n-1-i])] for i in range(n)]})
 rt,ro=residuals(a,h,g,D(beta));et=max(abs(rt[2*i,2*j+1]) for i,j in a);eo=max(abs(ro[2*i+1,2*j+1]) for i,j in g)
 return rows,float(et),float(eo)

def main():
 out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'manufactured':manufactured(),'states':[]}
 for name,base in [('chain240','polar_chain240_verification'),('res2','polar_res2_verification')]:
  obj=PolarData(Path('runs')/base/'source_coefficients.npz',radial_order=224);old,T,O,P,RT,RO=compute(obj,nquad=128,return_polys=True)
  rows,et,eo=reconstruct(obj.beta,obj.a0,old['harmonic_Green_moments'])
  for row in rows:
   row['data_a']=[[i,j,float(T[2*i,2*j+1])] for i,j,_ in row['a']]
   row['data_h']=[[i,j,float(P[2*i+1,2*j+1])] for i,j,_ in row['h']]
   row['data_g']=[[i,j,float(O[2*i+1,2*j+1])] for i,j,_ in row['g']]
  out['states'].append({'candidate':name,'sha256':obj.sha256,'beta':obj.beta,'a0':obj.a0,'center_strain_fixed_exactly':-2,'actual_data_center_strain':old['low_jets']['c'],'reconstructed_RT_coefficient_max':et,'reconstructed_RO_coefficient_max':eo,'rows':rows})
 Path('runs/high_order_jets/recurrence_check.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'manufactured':out['manufactured'],'states':[{k:v for k,v in s.items() if k!='rows'} for s in out['states']]}),flush=True)

if __name__=='__main__':main()
