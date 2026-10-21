"""Exact rational upper bounds for the certificate in 02-remainder/PROOF.md.

No floating point is used to establish an inequality. Decimals in the output
are outward-rounded from Fraction objects. Run from the workspace root:
timeout 540 env PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 \
  OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 \
  answer/03-norm-and-radius/verification/rational_certificate.py
"""
import json
import resource
from fractions import Fraction as F
from pathlib import Path

resource.setrlimit(resource.RLIMIT_AS, (1_900_000_000, 1_900_000_000))
ROOT = Path(__file__).resolve().parent


def out(x, places=12, upper=True):
    scale = 10**places
    if upper:
        n = -((-x.numerator * scale) // x.denominator)
    else:
        n = (x.numerator * scale) // x.denominator
    return f"{n // scale}.{n % scale:0{places}d}"


def decade_below(x):
    ans = F(1)
    while ans > x:
        ans /= 10
    return ans


def cert(A0s, es, hs, hps, taus):
    A0, e0, h, hp, tau = map(F, (A0s, es, hs, hps, taus))
    r, sigma, theta = F(1, 2), F(1), F(9, 10)
    ell, rr = 1-r, r*r
    Am_real, Ap_real = A0-h, A0+h
    Am, AM = Am_real-tau, Ap_real+tau
    bm, bp = 2/AM, 2/Am
    ep = e0+hp
    assert Am > 2 and sigma > bp and theta+bm > 1

    # Analytic majorants of all origin algebra norms. Eo <= r^2/(1-r^2).
    Z = n = (1+rr)/(1-rr)
    D = 4*rr/(1-rr)**2
    J = 4*(3+rr)/(1-rr)**3
    Eo = rr/(1-rr)
    gamma0 = 1-(2+bp)*Eo
    assert gamma0 > 0
    Z1 = max(r*r, r**4, r**6,
             r**7/((6+sigma)*(7+sigma)))/A0
    D1 = max(2*r*r, 4*r**4, 6*r**6,
             (8+sigma)*r**7/((6+sigma)*(7+sigma)))/A0
    J1 = max(F(6), 20*r*r, 42*r**4, r**5)/A0

    # Endpoint-anchored Holder seminorms <= derivative sup, since ell<=1.
    astar = A0*r*(1+r)/(1+rr)
    Ha = 2*A0/(1+rr)**2
    K0 = 2/(r*(1+rr))
    Hk = 2*(1+3*rr)/(rr*(1+rr)**2)
    w2S = 4*A0*r*(3-rr)/(1+rr)**3
    w2H = 12*A0*(1+6*rr+rr*rr)/(1+rr)**4
    gs, w2star = F(1, 2), A0
    gS = {p:(1+rr)**p/r**(2*p) for p in (2,3)}
    gH = {p:2*p*(1+rr)**(p-1)/r**(2*p+1) for p in (2,3)}
    # W0 = sup u^-b (1+u)^(b-2)(1+u^2).
    # It decreases in u and increases in b; use b<=1 at u=r.
    W0 = (1+rr)/(r*(1+r))

    ED = F(2,3)*n*n*Z1
    KD = 2/astar*(1+K0*ell/2)
    Hg = F(4,3)*n*Z1+ED+ell*KD
    aD = 2*ell/(3*astar)
    WD = (2+bp)*aD+(1+bp)*Hg
    d = min(F(1), 1/(4*n*Z1), astar/(2*ell),
            1/(12*Hg), 1/(4*WD), gamma0/(2*(2+bp)*ED))
    rho = A0/Am_real
    delta0 = d/(2*rho)
    assert n*Z1*d <= F(1,4) and d*Hg <= F(1,12)
    assert d*WD <= F(1,4) and ell*d/(2*astar) <= F(1,4)
    Nz = n/(1-n*Z1*d)
    gamma = 1-(2+bp)*(Eo+ED*d)
    assert gamma >= gamma0/2
    Tb = Nz**4/(2*gamma)*(1+Z+Z1*d+D+D1*d+ep*AM*(J+J1*d))
    Te = Nz**4*AM*(J+J1*d)/(2*gamma)
    Vb = Nz/gamma
    # Replace noninteger powers by rational upper bounds, using 0<bp<1.
    Fop = r**(-5)*max(1/bm, 1/(sigma-bp))
    Io = 1/(1-bp)
    It = 1/(theta+bm-1)
    cp = (1+bp)/(3*Am)
    amin = astar-ell*d/2
    Na = 1/amin
    Hainv = (Ha+d/2)/amin**2
    KH = (1/(1+theta)+K0/2+Hk*ell/2)*Na+(1+K0*ell/2)*Hainv
    gSh = {p:F(4,3)*gS[p] for p in (2,3)}
    gHh = {p:F(4,3)*(gH[p]+p*gS[p]*d*KD) for p in (2,3)}
    Qstar = F(2,3)*(abs(w2star)+d)*(1/(A0*gs**2)+ep*AM/(A0*gs**3))
    Qestar = F(2,3)*AM/A0*(abs(w2star)+d)/gs**3
    qeH = AM/(2*A0)*((w2S+d)*gHh[3]+(w2H+d)*gSh[3])
    qH = ((K0+d*KD)*gHh[2]+(Hk+d*KH)*gSh[2])/2+ep*qeH
    M = cp*(Fop*Tb+Qstar*Io*Vb+F(4,3)*W0*qH*It)
    Me = cp*(Fop*Te+Qestar*Io*Vb+F(4,3)*W0*qeH*It)
    DN = M/d
    KAv = rho*M/d*(1/tau+1/Am_real)
    Kev = rho*Me/d
    Rvv = 4*rho*rho*M/d**2

    # Pure parameter slice: B=P5 I3 + P3 I2, I_n=Beta(n-beta/2,beta).
    # Rigorous rational bounds for integrals with zero, one, two log factors.
    brlo, brhi = 2/Ap_real, 2/Am_real
    beta1, beta2 = 2/Am_real**2, 4/Am_real**3
    I0, I1, I2 = {}, {}, {}
    for nn in (2,3):
        pp = nn-1-brhi/2
        I0[nn] = 1/brlo
        I1[nn] = 1/brlo**2+1/(pp+1)**2+1/(brlo+1)
        I2[nn] = 4/brlo**3+2/(pp+1)**3+2/(brlo+2)
    p5 = max(abs(F(5,6)/aa-5*ee)
             for aa in (Am_real,Ap_real) for ee in (e0-hp,e0+hp))
    p3 = max(abs(F(1,2)/aa+ee)
             for aa in (Am_real,Ap_real) for ee in (e0-hp,e0+hp))
    pmax = {3:p5, 2:p3}
    p1 = {3:F(5,6)/Am_real**2, 2:F(1,2)/Am_real**2}
    p2 = {3:F(5,3)/Am_real**3, 2:1/Am_real**3}
    KAA = sum(p2[nn]*I0[nn]+(2*p1[nn]*beta1+pmax[nn]*beta2)*I1[nn]
              +pmax[nn]*beta1**2*I2[nn] for nn in (2,3))
    KAe = beta1*(5*I1[3]+I1[2])
    DA = sum(p1[nn]*I0[nn]+pmax[nn]*beta1*I1[nn] for nn in (2,3))
    De = 6/brlo

    beta0 = 2/A0
    SA = 6*A0*(4*A0-3)/(8*A0-1)
    # t^(1-beta/2)>=t gives Beta(2-beta/2,beta)>=1/[beta(1+beta)].
    B_lower = (16-beta0)/(3*A0*(4+beta0))/(beta0*(1+beta0))*(1-SA*e0)
    assert B_lower > 0
    par = DA*h+De*hp+KAA*h*h/2+KAe*h*hp
    margin = B_lower/2-par
    assert margin > 0, "These coarse parameter bounds give no radius."
    linear = DN+KAv*h+Kev*hp
    eps = min(delta0, margin/(2*(linear+Rvv*delta0)))
    eps_decade = decade_below(eps)
    # Direct exact-arithmetic verification of the final strict budget.
    assert par+linear*eps_decade+Rvv*eps_decade**2 < B_lower/2
    C2 = max(KAA/2,KAe/2,KAv/2,Kev/2,Rvv)
    names = dict(A0=A0,e0=e0,h=h,hp=hp,tau=tau,r=r,sigma=sigma,theta=theta,
                 A_m=Am,A_M=AM,b_minus=bm,b_plus=bp,Z=Z,n=n,D=D,J=J,Eo=Eo,
                 Gamma0=gamma0,Z1=Z1,D1=D1,J1=J1,a_star=astar,H_a=Ha,
                 K0=K0,H_k=Hk,w2S=w2S,w2H=w2H,gstar=gs,w2star=w2star,
                 g2S=gS[2],g2H=gH[2],g3S=gS[3],g3H=gH[3],W0=W0,
                 ED=ED,KD=KD,Hg=Hg,aD=aD,WD=WD,d=d,rho=rho,delta0=delta0,
                 Nz=Nz,Gamma=gamma,T=Tb,Te=Te,V=Vb,F=Fop,Io=Io,It=It,cplus=cp,
                 amin=amin,Na=Na,Hainv=Hainv,KH=KH,
                 g2S_hat=gSh[2],g2H_hat=gHh[2],g3S_hat=gSh[3],g3H_hat=gHh[3],
                 Qstar=Qstar,Qestar=Qestar,QH=qH,QeH=qeH,
                 M=M,Me=Me,DN=DN,KAv=KAv,Kev=Kev,Rvv=Rvv,
                 KAA=KAA,KAe=KAe,DA=DA,De=De,B_lower=B_lower,
                 parameter_budget=par,margin=margin,linear=linear,C2=C2,
                 epsilon_formula=eps,epsilon_decade=eps_decade)
    return {
        "inputs":dict(A0=A0s,e0=es,h=hs,hp=hps,tau=taus),
        "rounded_up":{k:out(v) for k,v in names.items()},
        "rounded_down":{k:out(names[k],18,False)
                        for k in ("d","delta0","B_lower","margin","epsilon_formula","epsilon_decade")},
        "exact":{k:f"{v.numerator}/{v.denominator}" for k,v in names.items()},
        "final_inequality_verified_with_Fraction":True,
    }


if __name__ == "__main__":
    cases = {
        "computed_parameters_r12":cert("10.150725","0.0135206","0.06","0.0003","1"),
        "earlier_reference_same_parameter_widths":cert("4","0.0625","0.06","0.0003","0.5"),
        "earlier_reference_fixed_parameters":cert("4","0.0625","0","0","0.5"),
    }
    (ROOT/"rational_bounds.json").write_text(json.dumps(cases,indent=2)+"\n")
    for key, val in cases.items():
        print(key)
        for name in ("d","delta0","M","Me","DN","KAv","Kev","Rvv","KAA","KAe",
                     "DA","De","B_lower","parameter_budget","margin","C2",
                     "epsilon_formula","epsilon_decade"):
            rounding = val["rounded_down"] if name in val["rounded_down"] else val["rounded_up"]
            print(f"  {name}: {rounding[name]}")
