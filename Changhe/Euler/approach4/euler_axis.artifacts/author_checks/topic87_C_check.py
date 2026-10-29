# Lead check of topic 87 seed pole extraction: phi_seed = z u^(-p) P_1(v,w), u = 1 + a r^2 + z^2, v = a r^2/u, w = z^2/u.
# Expand at large R (eps = 1/R^2) and compare A_seed'(1), C_seed(1), C_seed'(1) with the stated formulas.
import sympy as sp, json
mu,a,p,eps=sp.symbols('mu a p eps',positive=True)
c=sp.symbols('c0:6')
V,W=sp.symbols('V W')
P1=c[0]+c[1]*V+c[2]*W+c[3]*V**2+c[4]*V*W+c[5]*W**2
d=a+(1-a)*mu**2
u_over_R2=d+eps
v=a*(1-mu**2)/u_over_R2; w=mu**2/u_over_R2
expr=mu*u_over_R2**(-p)*P1.subs({V:v,W:w})   # phi_seed / R^(1-2p)
ser=sp.series(expr,eps,0,2).removeO()
A=sp.simplify(ser.coeff(eps,0)); C=sp.simplify(ser.coeff(eps,1))
k=2*p
A1=P1.subs({V:0,W:1}); V1=sp.diff(P1,V).subs({V:0,W:1}); Z1=sp.diff(P1,W).subs({V:0,W:1})
Pww=sp.diff(P1,W,2).subs({V:0,W:1}); Pvw=sp.diff(P1,V,W).subs({V:0,W:1})
G0=p*A1+Z1; G1=2*a*((p+1)*(Z1-V1)+Pww-Pvw)
r={}
r['A1']=sp.simplify(A.subs(mu,1)-A1)==0
r['Aprime1']=sp.simplify(sp.diff(A,mu).subs(mu,1)-((1+k*(a-1))*A1-2*a*V1+2*a*Z1))==0
r['C1']=sp.simplify(C.subs(mu,1)+G0)==0
r['Cprime1']=sp.simplify(sp.diff(C,mu).subs(mu,1)+((1-2*(p+1)*(1-a))*G0+G1))==0
# envelope multipliers: R^n (1+R^2)^(-nu) = R^(n-2nu) (1 - nu eps + ...)
nu=sp.symbols('nu'); r['envelope_next_term']=sp.simplify(sp.series((1+eps)**(-nu),eps,0,2).removeO().coeff(eps,1)+nu)==0
# pole functional of Z = mu(1-mu^2)
g=sp.symbols('g'); Z=mu*(1-mu**2); r['LZ']=sp.simplify(g*(3-g)*Z.subs(mu,1)+4*sp.diff(Z,mu).subs(mu,1)+8)==0
print(r); json.dump({k_:bool(v_) for k_,v_ in r.items()},open('checks/topic87_C_check_output.json','w'),indent=1)
