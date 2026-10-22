"""Independent formal complex-series inversion, not the solver lane's code."""
from pathlib import Path
from datetime import datetime,timezone
import json,time,sys
import sympy as S
start=time.monotonic();out={'utc':datetime.now(timezone.utc).isoformat(),'checks':[]};N=6
s,z,w=S.symbols('s z w',real=True);ks=S.symbols('k0:6',real=True)
def eq(name,value):
 v=S.expand(value)
 assert not v.atoms(S.Float),(name,"unexpected floating coefficient",str(v))
 assert v==0,(name,str(v))
 out['checks'].append({'name':name,'pass':True})
def add(a,b):
 r=dict(a)
 for n,c in b.items():r[n]=S.expand(r.get(n,0)+c)
 return {n:c for n,c in r.items() if c!=0}
def mul(a,b,n=N):
 r={}
 for i,x in a.items():
  for j,y in b.items():
   if i+j<=n:r[i+j]=r.get(i+j,0)+x*y
 return {i:S.expand(x) for i,x in r.items() if S.expand(x)!=0}
def power(a,k,n=N):
 r={0:S.Integer(1)}
 for j in range(k):r=mul(r,a,n)
 return r
def deriv(a):return {i-1:i*x for i,x in a.items() if i}
def expr(a,x):return S.expand(sum(c*x**n for n,c in a.items()))
g={i+2:ks[i]/S.factorial(i+2) for i in range(5)}
gp=deriv(g);q={i-1:S.I*c for i,c in g.items()};qp=[power(q,j) for j in range(N)]
fc={}
# Lagrange-Burmann: [w^n] 4i g(u(w))=(4i/n)[s^(n-1)]g'(s)(1+i g(s)/s)^(-n).
for n in range(2,N+1):
 fc[n]=S.expand(4*S.I/S.Integer(n)*sum(S.binomial(-n,j)*mul(gp,qp[j]).get(n-1,0) for j in range(n)))
F=expr(fc,w);physical=S.expand(F.subs(w,s+S.I*z));Wr=S.expand(S.re(physical));Wz=S.expand(4*z-S.im(physical))
P1=S.Poly(Wr,s,z);P2=S.Poly(Wz,s,z)
eq('complex_jet_div4',S.diff(Wr,s)+S.diff(Wz,z)-4)
eq('complex_jet_curl0',S.diff(Wz,s)-S.diff(Wr,z))
# Verify the defining complex composition directly as a truncated series.
u={1:S.Integer(1)}
for i,c in g.items():u[i]=S.I*c
composed={}
for i,c in fc.items():composed=add(composed,{j:c*v for j,v in power(u,i).items()})
for n in range(N+1):eq(f'defining_composition_degree{n}',composed.get(n,0)-4*S.I*g.get(n,0))
def trace(poly,sigma):
 result={};powers={0:{0:S.Integer(1)}}
 for i in range(1,N+1):powers[i]=mul(powers[i-1],sigma)
 for (i,j),c in poly.terms():result=add(result,{a+j:c*b for a,b in powers[i].items() if a+j<=N})
 return result
# Independent order-by-order invariant curve; do not insert expected coefficients.
sig={}
for m in range(2,N+1):
 r=add(trace(P1,sig),{j:-v for j,v in mul(deriv(sig),trace(P2,sig)).items()})
 sig[m]=S.expand(S.sympify(r.get(m,0))/S.Integer(4*m))
res=add(trace(P1,sig),{j:-v for j,v in mul(deriv(sig),trace(P2,sig)).items()})
for m in range(N+1):eq(f'curve_invariance_degree{m}',res.get(m,0))
out['sigma_coefficients']={str(m):str(S.factor(c)) for m,c in sig.items()}
for m,c in sig.items():
 eq(f'sigma_weight{m}',sum((i+1)*ks[i]*S.diff(c,ks[i]) for i in range(len(ks)))-(m-1)*c)
 eq(f'sigma_reflection_parity{m}',c.subs({k:(-1)**i*k for i,k in enumerate(ks)},simultaneous=True)+c)
eq('sigma2_zero',sig[2]);eq('sigma3_k1_over18',sig[3]-ks[1]/18)
eq('sigma5_generic',sig[5]-(60*ks[0]**2*ks[1]-ks[3])/600)
eq('sigma6_generic',sig[6]-7*(705*ks[0]**3*ks[1]-18*ks[0]*ks[3]-25*ks[1]*ks[2])/32400)
# Independently construct arclength curvature jets with truncated series.
gfull={i+2:ks[i]/S.factorial(i+2) for i in range(6)};gpf=deriv(gfull);gp2=mul(gpf,gpf)
def binom_series(exponent):
 r={}
 for j in range(N+1):r=add(r,{i:S.binomial(exponent,j)*c for i,c in power(gp2,j).items()})
 return r
speed_inv=binom_series(-S.Rational(1,2));curv=mul(deriv(gpf),binom_series(-S.Rational(3,2)))
cjets=[]
for order in range(6):
 cj=curv.get(0,0);cjets.append(cj)
 eq(f'curvature_leading_k{order}',S.diff(cj,ks[order])-1)
 eq(f'curvature_reflection{order}',cj.subs({k:(-1)**i*k for i,k in enumerate(ks)},simultaneous=True)-(-1)**order*cj)
 if order%2:eq(f'curvature_first_odd{order}',cj.subs({ks[i]:0 for i in range(1,order,2)})-ks[order])
 curv=mul(speed_inv,deriv(curv))
eq('arclength_kappa3',cjets[3]-ks[3]+19*ks[0]**2*ks[1]);out['curvature_jets']={str(i):str(S.factor(c)) for i,c in enumerate(cjets)}
# Linear-response constants up to degree15, obtained from the harmonic Cauchy problem.
k=S.symbols('k',real=True);linear=[]
for j in range(7):
 d=2*j+3;gg=k*s**d/S.factorial(d)
 H1=S.expand(-4*sum((-1)**l*S.diff(gg,s,2*l)*z**(2*l+1)/S.factorial(2*l+1) for l in range((d//2)+1)))
 eq(f'linear_lap_degree{d}',S.diff(H1,s,2)+S.diff(H1,z,2))
 eq(f'linear_dirichlet_degree{d}',H1.subs(z,0))
 eq(f'linear_normal_degree{d}',S.diff(H1,z).subs(z,0)+4*gg)
 force=S.diff(H1,s).subs(s,0);ans=S.integrate(force/(4*z),z)
 wanted=(-1)**j*k*z**d/(d*S.factorial(d))
 eq(f'linear_invariant_coefficient_degree{d}',ans-wanted)
 linear.append({'degree':d,'coefficient':str(S.factor(ans/z**d))})
out['linear_constants']=linear
# Negative controls: dropping arclength conversion and using a factorial only both fail.
assert S.expand(cjets[3]-ks[3])!=0
assert S.expand(sig[3]-ks[1]/S.factorial(3))!=0
out['negative_controls']=[{'name':'graph_k3_is_not_general_arclength_kappa3','pass':True},{'name':'factorial_without_degree_factor_is_wrong','pass':True}]
out['method']='One-variable Lagrange-Burmann complex-series inversion; independent of lead coefficient-solving code. Generic jet to degree6 and seven linear curvature orders to degree15.'
out['all_passed']=True;out['elapsed_seconds']=time.monotonic()-start
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'checks':len(out['checks']),'negative_controls':len(out['negative_controls']),'elapsed_seconds':out['elapsed_seconds'],'sigma':out['sigma_coefficients'],'all_passed':True}))
