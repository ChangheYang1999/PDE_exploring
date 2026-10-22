"""Independently compute center Taylor coefficients using series algebra and global Green moments.

No automatic-differentiation or numerics-lane implementation. Smooth angular
harmonics become bivariate Cartesian polynomials before PDE multiplication.
"""
import json,datetime,math
from pathlib import Path
import numpy as np
from scipy.special import roots_jacobi
from read_polar_data import PolarData,cheb_all

DT=np.longdouble

def mul(a,b,n):return np.convolve(a,b)[:n+1]
def binom_series(p,n,L):
    a=np.zeros(n+1,dtype=DT);a[0]=1
    for j in range(1,n+1):a[j]=a[j-1]*(p-j+1)/(j*DT(L)**2)
    return a

def cheb_series(coeff,arg,n):
    p0=np.zeros(n+1,dtype=DT);p0[0]=1;p1=arg.copy();val=coeff[0]*p0
    if len(coeff)>1:val+=coeff[1]*p1
    for k in range(2,len(coeff)):
        p2=2*mul(arg,p1,n)-p0;val+=coeff[k]*p2;p0,p1=p1,p2
    return val

def radial_series(obj,m,coeff,kind,D):
    n=(D-m)//2;z=binom_series(-DT(1)/(2*obj.beta),n,obj.L);arg=-2*z;arg[0]+=1
    Q=cheb_series(coeff,arg,n);power=(DT(obj.gammaT)-m)/2 if kind=='T' else -(m+DT(1)/obj.beta)/2
    return mul(Q,binom_series(power,n,obj.L),n)/DT(obj.L)**m

def add_harmonic(poly,m,rad):
    for k,c in enumerate(rad):
      for j in range(1,m+1,2):
        im=DT(math.comb(m,j))*(-1)**((j-1)//2)
        for l in range(k+1):
          i=m-j+2*(k-l);jj=j+2*l
          if i+jj<len(poly):poly[i,jj]+=c*im*math.comb(k,l)

def derivative(a,axis):
    b=np.zeros_like(a)
    if axis==0:
      for i in range(1,len(a)):b[i-1,:]=i*a[i,:]
    else:
      for j in range(1,len(a)):b[:,j-1]=j*a[:,j]
    return b

def pmul(a,b):
    c=np.zeros_like(a);D=len(a)-1
    for i,j in zip(*np.nonzero(a)):
      for k,l in zip(*np.nonzero(b)):
        if i+j+k+l<=D:c[i+k,j+l]+=a[i,j]*b[k,l]
    return c

def evaluate(a,x,y):
    return sum(c*DT(x)**i*DT(y)**j for (i,j),c in np.ndenumerate(a) if c!=0)

def compute(obj,D=12,nquad=96,return_polys=False):
    T=np.zeros((D+1,D+1),dtype=DT);O=T.copy();P=T.copy();Cs={}
    for m in range(1,min(2*obj.NT,D+1),2):add_harmonic(T,m,radial_series(obj,m,obj.cT[(m-1)//2],'T',D))
    for m in range(2,min(2*obj.NO,D)+1,2):
        a=radial_series(obj,m,obj.cO[m//2-1],'O',D);add_harmonic(O,m,a)
        exponent=DT(obj.beta)*(m-2);z,w=roots_jacobi(nquad,0,float(exponent));z=np.asarray((z+1)/2,DT);w=np.asarray(w/w.sum()/(exponent+1),DT)
        Q=cheb_all(obj.cO[m//2-1:m//2],1-2*z)[0]
        C=DT(obj.beta)*DT(obj.L)**(2-m)/(2*m)*np.dot(w,Q);Cs[str(m)]=float(C)
        pp=np.zeros((D-m)//2+1,dtype=DT);pp[0]=C
        for k in range(len(pp)-1):pp[k+1]=-a[k]/(4*DT(k+1)*(m+k+1))
        add_harmonic(P,m,pp)
    Ux=-derivative(P,1);Uy=derivative(P,0);Wx=Ux.copy();Wy=Uy.copy();Wx[1,0]+=obj.beta;Wy[0,1]+=obj.beta
    termsT=[pmul(Wx,derivative(T,0)),pmul(Wy,derivative(T,1)),-(obj.beta-2)*T]
    termsO=[pmul(Wx,derivative(O,0)),pmul(Wy,derivative(O,1)),O,-derivative(T,0)]
    RT=sum(termsT);RO=sum(termsO);E=-derivative(derivative(P,0),0)-derivative(derivative(P,1),1)-O
    out={'harmonic_Green_moments':Cs,'temperature_rows':[],'vorticity_rows':[],'elliptic_max_through_degree_10':0.,'low_jets':{},'series_value_checks':[]}
    for name,R,terms,maxdegree in [('temperature_rows',RT,termsT,D-1),('vorticity_rows',RO,termsO,D-2)]:
      for deg in range(1,maxdegree+1):
        for i in range(deg+1):
          j=deg-i
          if (name=='temperature_rows' and (i%2 or j%2!=1)) or (name=='vorticity_rows' and (i%2!=1 or j%2!=1)):continue
          vals=[float(t[i,j]) for t in terms];scale=sum(abs(v) for v in vals)
          out[name].append({'powers':[i,j],'degree':deg,'coefficient':float(R[i,j]),'cartesian_group_terms':vals,'sum_abs_group_terms':scale,'relative_coefficient_defect':float(abs(R[i,j])/scale) if scale else 0.})
    out['elliptic_max_through_degree_10']=float(max(abs(E[i,j]) for i in range(D+1) for j in range(D+1-i) if i+j<=D-2))
    out['low_jets']={k:float(v) for k,v in {'a0':T[0,1],'b1':T[2,1],'b2':T[0,3],'g':O[1,1],'c':P[1,1],'d1':P[3,1],'d2':P[1,3]}.items()}
    # Compare values with a separately coded Clenshaw Cartesian field evaluator.
    for r in [.3,.15,.075,.0375]:
      x=r*np.cos(.413);y=r*np.sin(.413)
      tv=float(obj.Theta(np.array([x]),np.array([y]))[0]);ov=float(obj.Omega(np.array([x]),np.array([y]))[0]);pv=float(obj.Psi(np.array([x]),np.array([y]))[0])
      out['series_value_checks'].append({'r':r,'Theta_error':float(evaluate(T,x,y)-tv),'Omega_error':float(evaluate(O,x,y)-ov),'Psi_error':float(evaluate(P,x,y)-pv)})
    if return_polys:return out,T,O,P,RT,RO
    return out

def main():
    out=Path('runs/high_order_jets');out.mkdir(parents=True,exist_ok=True);rows=[]
    for name in ['chain240','res2']:
      base='polar_chain240_verification' if name=='chain240' else 'polar_res2_verification';obj=PolarData(Path('runs')/base/'source_coefficients.npz',radial_order=224)
      for n in [64,96,144]:
        row={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'name':name,'nquad':n,'sha256':obj.sha256,'result':compute(obj,nquad=n)};rows.append(row)
        print(json.dumps({'name':name,'nquad':n,'low_jets':row['result']['low_jets'],'degree5_T':[r for r in row['result']['temperature_rows'] if r['degree']==5]}),flush=True)
    (out/'results.json').write_text(json.dumps(rows,indent=2)+'\n')
if __name__=='__main__':main()
