"""Exact weighted Taylor checks. No servers, JS, GPU, or cluster use."""
import os
import resource
from pathlib import Path

resource.setrlimit(resource.RLIMIT_AS, (1900 * 1024**2, 1900 * 1024**2))
os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
import sympy as S

s, x = S.symbols("s x")
c, K = S.symbols("c K", real=True)
h = {n: S.Symbol(f"h{n}") for n in range(2, 7)}


def hom(poly, n):
    return S.Add(*(v * s**j * x**k for (j, k), v in S.Poly(S.expand(poly), s, x).terms()
                   if 2*j + k == n))


def trunc(poly, n):
    return S.Add(*(v * s**j * x**k for (j, k), v in S.Poly(S.expand(poly), s, x).terms()
                   if 2*j + k <= n))


def lap(poly):
    return 4*s*S.diff(poly, s, 2) + 8*S.diff(poly, s) + S.diff(poly, x, 2)


def residuals(phi, q, cv):
    def W(f):
        return 2*s*(cv-S.diff(phi, x))*S.diff(f, s) + (
            cv*x+2*phi+2*s*S.diff(phi, s))*S.diff(f, x)
    eta = -lap(phi)
    return S.expand(q+W(q)-2*S.diff(phi,x)*q), S.expand((1+cv)*eta+W(eta)-2*q*S.diff(q,x))


def s1(cv, kv, N):
    phi, q = x/2, kv
    rows = []
    for n in range(1, N+1):
        pu = [S.Symbol(f"p{j}_{n+1-2*j}") for j in range(1, (n+1)//2+1)]
        qu = [S.Symbol(f"q{j}_{n-2*j}") for j in range(n//2+1)]
        pn = h[n+1]*x**(n+1) + sum(a*s**j*x**(n+1-2*j) for j,a in enumerate(pu,1))
        qn = sum(a*s**j*x**(n-2*j) for j,a in enumerate(qu))
        rq, re = residuals(phi+pn, q+qn, cv)
        eq = S.Poly(hom(rq,n),s,x).coeffs()+S.Poly(hom(re,n-1),s,x).coeffs()
        sol = S.solve(eq, pu+qu, dict=True)
        assert len(sol) == 1
        pn = S.expand(pn.subs(sol[0]))
        qn = S.expand(qn.subs(sol[0]))
        phi += pn
        q += qn
        rows.append((n,pn,qn))
    rq,re = residuals(phi,q,cv)
    assert S.simplify(trunc(rq,N)) == 0
    assert S.simplify(trunc(re,N-1)) == 0
    return phi,q,rows


def show(poly):
    return str(S.collect(S.factor(poly), [s,x]))


if __name__ == "__main__":
    print("SymPy:", S.__version__)
    print("S1 generic first block")
    _,_,rows = s1(c,K,1)
    for n,p,q in rows:
        print("phi2 =", show(p))
        print("q1   =", show(q))
    print("\nS1 c=3/5, K=1; free h2,h3,h4,h5")
    phi,q,rows = s1(S.Rational(3,5),S.Integer(1),4)
    for n,pn,qn in rows:
        print(f"phi{n+1} =", show(pn))
        print(f"q{n} =", show(qn))
    print("PASS Rq weights 0..4; Reta weights 0..3")
    eps, tau = S.symbols("eps tau")
    sample = {h[2]:0, h[3]:0, h[4]:eps, h[5]:tau}
    sample_phi, sample_q = phi.subs(sample), q.subs(sample)
    print("S1 simple sample phi =", str(S.expand(sample_phi)))
    print("S1 simple sample q =", str(S.expand(sample_q)))
    print("S1 simple sample eta =", str(S.expand(-lap(sample_phi))))
    srq, sre = residuals(sample_phi, sample_q, S.Rational(3,5))
    assert trunc(srq,4) == trunc(sre,4) == 0
    print("PASS two-parameter sample: both residuals through weight 4")

    # Compact coefficients for arbitrary K at c=3/5, derived from
    # the axis equations and radial triangular recurrence.
    cv = S.Rational(3,5)
    delta = 1+cv
    A = 2*cv-1
    f = x/2 + sum(h[n]*x**n for n in range(2,6))
    b = {0:K}
    for n in range(1,5):
        # (delta*x+2*sum h_m*x^m) Q'
        # =2*sum m*h_m*x^(m-1) Q.
        b[n] = S.factor(sum(2*(2*m-n-1)*h[m]*b[n+1-m]
                           for m in range(2,n+2))/(delta*n))
    E = {}
    for n in range(4):
        E[n] = S.factor((2*sum(b[i]*(n+1-i)*b[n+1-i] for i in range(n+1))
                         -2*sum(h[m]*(n+1-m)*E[n+1-m] for m in range(2,n+1)))
                        /(delta*(n+1)))
    g = {n:S.factor(-(E[n]+(n+2)*(n+1)*h[n+2])/8) for n in range(4)}
    Q = sum(b[n]*x**n for n in b)
    G = sum(g[n]*x**n for n in g)
    # R = coefficient of s in q: [A + lower(x)]R + v R'
    # = 2 G' Q - 4 G Q'.
    rr = {}
    rhs = trunc(2*S.diff(G,x)*Q-4*G*S.diff(Q,x),2)
    for n in range(3):
        base = S.expand(rhs).coeff(x,n)
        extra = sum((4*m-2*(n+1-m))*h[m]*rr[n+1-m]
                    for m in range(2,n+2))
        rr[n] = S.factor((base+extra)/(A+n*delta))
    # eta's s coefficient, then phi's s^2 coefficients.
    F = {}
    for n in range(2):
        Es = sum(E[k]*x**k for k in E)
        R = sum(rr[k]*x**k for k in rr)
        rhs_eta = 2*(Q*S.diff(R,x)+R*S.diff(Q,x))-4*G*S.diff(Es,x)
        base = S.expand(rhs_eta).coeff(x,n)
        extra = sum((2*m-2*(n+1-m))*h[m]*F[n+1-m]
                    for m in range(2,n+2))
        F[n] = S.factor((base+extra)/(delta+A+n*delta))
    jcoef = {n:S.factor(-(F[n]+(n+2)*(n+1)*g[n+2])/24) for n in range(2)}
    # q s^2 constant: 2 A q20 = 4 g1 R0 - 4 g0 R1
    #                                  + 2 j1 K - 6 j0 b1.
    q20 = S.factor((4*g[1]*rr[0]-4*g[0]*rr[1]+2*jcoef[1]*K-6*jcoef[0]*b[1])/(2*A))
    compact_phi = f+s*G+s**2*sum(jcoef[n]*x**n for n in jcoef)
    compact_q = Q+s*sum(rr[n]*x**n for n in rr)+s**2*q20
    rq,re = residuals(compact_phi,compact_q,cv)
    assert all(S.factor(v)==0 for v in S.Poly(trunc(rq,4),s,x).coeffs())
    assert all(S.factor(v)==0 for v in S.Poly(trunc(re,3),s,x).coeffs())
    assert S.expand(compact_phi.subs(K,1)-phi)==0
    assert S.expand(compact_q.subs(K,1)-q)==0
    print("PASS compact arbitrary-K recurrence against both residuals and K=1 solve")
    for n in b:
        print(f"b{n} =", str(b[n]))

    cv = c
    a = (1+2*c)/4
    A2 = c-S.Rational(1,2)
    B2 = 2*c+S.Rational(1,2)
    H2 = x**2-s/4
    H3 = x**3-3*s*x/4
    H4 = x**4-3*s*x**2/2+s**2/8
    H5 = x**5-5*s*x**3/2+5*s**2*x/8
    H6 = x**6-15*s*x**4/4+15*s**2*x**2/8-5*s**3/64
    v1 = 8*K*h[2]/B2
    v02 = 6*K*h[3]/B2+24*K*h[2]**2/B2**2
    v10 = (-3*K*h[3]+8*K*h[2]**2/B2)/A2
    phi2 = a*x+h[2]*H2+h[3]*H3+h[4]*H4+h[5]*H5
    q2 = s*(K+v1*x+v02*x**2+v10*s)
    rq,re = residuals(phi2,q2,cv)
    assert all(S.factor(v)==0 for v in S.Poly(trunc(rq,4),s,x).coeffs())
    assert all(S.factor(v)==0 for v in S.Poly(trunc(re,3),s,x).coeffs())
    e4 = 16*K**2*h[2]/(B2*(1+c+2*A2))
    phi2 += h[6]*H6-e4*s**3/48
    rq,re = residuals(phi2,q2,cv)
    assert all(S.factor(v)==0 for v in S.Poly(trunc(re,4),s,x).coeffs())
    print("\nS2 PASS Rq weights 0..4; Reta weights 0..4 with phi6")
    print("S2 q at c=3/5 =", show(q2.subs(c,S.Rational(3,5))))
    print("S2 eta4 at c=3/5 =", show(e4.subs(c,S.Rational(3,5))*s**2))

    n = S.symbols("n",integer=True,positive=True)
    print("\nS1 B=n A:", S.solve(c+1-n*(2*c-1),c)[0], "n>=4")
    print("S2 B=n A:", S.solve(2*c+S.Rational(1,2)-n*(c-S.Rational(1,2)),c)[0], "n>=9")
    print("c=3/5: S1 n=8; S2 n=17")
    v,Vp,Q,Qp,kap,dd = S.symbols("v Vp Q Qp kap delta")
    eta = 2*Q*(Q-kap)/v
    check = v*(S.diff(eta,Q)*Qp+S.diff(eta,v)*Vp)+dd*eta-2*Q*Qp
    assert S.factor(check.subs(Qp,(Vp-dd)*Q/v))==0
    print("PASS exact axis identity eta = 2 Q (Q-K) / v")
    cv = S.Rational(3,5)
    print("Far-field exponents at c=3/5:",
          {"alpha": (1-cv)/cv, "q_power": -1/cv, "eta_power": -(1+cv)/cv})
