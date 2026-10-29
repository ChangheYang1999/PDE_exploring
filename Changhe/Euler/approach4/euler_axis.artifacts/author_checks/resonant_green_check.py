# Lead cross-check of the verifier's resonant Green moment supplement (research/pressure/resonant_moments/PROOF.md):
# for -u'' - (d-1)u'/R + l(l+d-2)u/R^2 = f, n = 2l+d-2, the Green formula u = (1/n)[R^(-l-d+2) A(R) + R^l B(R)],
# A = int_0^R s^(l+d-1) f, B = int_R^inf s^(1-l) f, solves the equation; with f = a R^(-l-d) for R >= R0 and
# A = a log(R/Rs) + Cs, u = R^(-l-d+2)[(a/n) log(R/Rs) + Cs/n + a/n^2].
import sympy as sp, json
R,s,a,Rs,Cs=sp.symbols('R s a R_s C_s',positive=True)
out=[]
for d in (3,5):
    for l in range(0,6):
        n=2*l+d-2
        A=a*sp.log(R/Rs)+Cs
        B=sp.integrate(s**(1-l)*a*s**(-l-d),(s,R,sp.oo))
        u=sp.simplify((R**(-l-d+2)*A+R**l*B)/n)
        target=R**(-l-d+2)*(a/n*sp.log(R/Rs)+Cs/n+a/sp.Integer(n)**2)
        ok1=sp.simplify(u-target)==0
        f=a*R**(-l-d)
        L=-sp.diff(u,R,2)-(d-1)*sp.diff(u,R)/R+l*(l+d-2)*u/R**2
        ok2=sp.simplify(L-f)==0
        # A' must equal R^(l+d-1) f
        ok3=sp.simplify(sp.diff(A,R)-R**(l+d-1)*f)==0
        out.append(dict(d=d,l=l,n=n,closed_form=bool(ok1),solves_ODE=bool(ok2),moment_consistent=bool(ok3)))
# general-f Green formula solves the ODE (symbolic f)
F=sp.Function('f'); l,d=sp.symbols('l d',positive=True); n=2*l+d-2
Aint=sp.Integral(s**(l+d-1)*F(s),(s,0,R)); Bint=sp.Integral(s**(1-l)*F(s),(s,R,sp.oo))
u=(R**(-l-d+2)*Aint+R**l*Bint)/n
L=-sp.diff(u,R,2)-(d-1)*sp.diff(u,R)/R+l*(l+d-2)*u/R**2
gen=sp.simplify(sp.expand(L-F(R)))
res=dict(cases=out,all_pass=all(c['closed_form'] and c['solves_ODE'] and c['moment_consistent'] for c in out),general_green_residual=str(gen))
json.dump(res,open('checks/resonant_green_check_output.json','w'),indent=1)
print(res['all_pass'],len(out),res['general_green_residual'])
