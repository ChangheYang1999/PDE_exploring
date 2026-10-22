"""Independent symbolic and value-only checks of packet106; no lane code reused."""
import json,time
from pathlib import Path
import sympy as sy
import mpmath as mp
start=time.monotonic();out={'symbolic':[],'numeric':[]}
x,y,t=sy.symbols('x y t',real=True);ell,c=sy.symbols('ell c',positive=True)
T=1+4*t*x*x;z=4*t*x*x/T;w=t*y*y/T;kt=x**3*T**sy.Rational(-3,4)*sy.exp(-w)
P=6-11*z+sy.Rational(21,4)*z*z+z*(15-14*z)*w+4*z*z*w*w
err=sy.simplify((sy.diff(kt,x,2)+sy.diff(kt,y,2))/(x*T**sy.Rational(-3,4)*sy.exp(-w))-P);assert err==0;out['symbolic'].append('Laplacian K_t exact')
pa=c*x*y/(1+ell*(x*x+y*y));expected=4*c*ell*x*y*(3+ell*(x*x+y*y))/(1+ell*(x*x+y*y))**3
assert sy.factor(-sy.diff(pa,x,2)-sy.diff(pa,y,2)-expected)==0;out['symbolic'].append('strain rational Laplacian exact')
j=4*c*ell*y*(3+ell*y*y)/(1+ell*y*y)**3;pc=pa+j*x**3/(6*(1+x*x)**3)
assert sy.simplify(sy.diff(pc,x).subs(x,0)-c*y/(1+ell*y*y))==0
assert sy.simplify(sy.diff(-sy.diff(pc,x,2)-sy.diff(pc,y,2),x).subs(x,0))==0;out['symbolic'].append('axis velocity and zero vorticity-slope correction exact')
beta=sy.symbols('beta',positive=True);alpha=1/beta;l=sy.Rational(3,2)+alpha;tau=(l-1)/2;m=1/(2*l);kap=tau*(1-m);d=1-tau*(1+m)
assert sy.simplify(kap-m/2-alpha/2)==0;assert sy.simplify(1-d+m/2-(1+alpha)/2)==0;out['symbolic'].append('Laplace-density exponent identities exact')
zz,dd=sy.symbols('zz dd',positive=True);assert sy.simplify((1+zz)**dd/(1+ell*zz)-(1+zz)**(dd-1)/ell-(ell-1)/ell**2*(1+zz)**(dd-1)/(zz+1/ell))==0;out['symbolic'].append('Laplace decomposition with PLUS exact')
mp.mp.dps=50
for beta0 in ['2.01','2.5','3','8','100']:
 b=mp.mpf(beta0);a=1/b;mu=3*b/2+1;lc=mu/b;tc=(lc-1)/2;mc=1/(2*lc);kc=tc*(1-mc);dc=1-tc*(1+mc)
 def e(y):return y*(1+y*y)**tc
 def ep(y):return (1+y*y)**(tc-1)*(1+lc*y*y)
 def bv(y):return mu*y*(1+y*y)/(1+lc*y*y)
 # u=v^(1/m) removes the integrable power singularity completely.
 def hv(y):return 2/(mu*mc)*(1+y*y)**(-tc*mc)*mp.quad(lambda v:(1+y*y*v**(2/mc))**(-kc),[0,mp.mpf('.5'),1])
 for y0 in ['0','.1','1','10','-.7']:
  yy=mp.mpf(y0);hh=hv(yy);defect=bv(yy)*mp.diff(hv,yy)+b*hh/2-2/ep(yy);ee=bv(yy)*ep(yy)-mu*e(yy);assert abs(defect)<mp.mpf('1e-42');assert abs(ee)<mp.mpf('1e-42');out['numeric'].append({'beta':beta0,'y':y0,'axis_ode_error':mp.nstr(abs(defect),15),'chart_ode_error':mp.nstr(abs(ee),15),'H':mp.nstr(hh,18)})
 # Recover B(z) using the independent incomplete-gamma Laplace density.
 for z0 in ['0','.2','5']:
  zv=mp.mpf(z0);B=mp.quad(lambda v:(1+zv*v**(2/mc))**(-kc),[0,mp.mpf('.5'),1])/mc
  # t=v^(2/m) regularizes density at zero; v upper infinity.
  def regular(v):
   if not v:return mp.gamma(kc-mc/2)/(mc*mp.gamma(kc))
   tt=v**(2/mc);return mp.exp(-zv*tt)*mp.gammainc(kc-mc/2,tt,mp.inf)/(mc*mp.gamma(kc))
  BD=mp.quad(regular,[0,mp.mpf('.5'),1,2,mp.inf]);err=abs(B-BD)/max(1,abs(B));assert err<mp.mpf('1e-20'),(beta0,z0,err);out['numeric'].append({'beta':beta0,'z':z0,'Laplace_B_relative_error':mp.nstr(err,20)})
out['elapsed_seconds']=time.monotonic()-start;out['status']='CONFIRMED';Path('research/106_positive_axis_compatibility/verification/own_tests.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(out['symbolic']),'symbolic',len(out['numeric']),'numerical','elapsed',out['elapsed_seconds'],flush=True)
