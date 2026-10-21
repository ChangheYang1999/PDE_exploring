"""Complete fitted-reference inventory and rational radius calculation.

Uses the separately executed interval certificate for B and parameter derivatives.
All remaining scalar inequalities use Fraction, or interval jets of rational
functions on whole intervals followed by outward rational rounding.
"""
import sys
import json
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"01-obstruction/verification"))
import certify as c
F,I,J = c.F,c.I,c.J
ROOT = Path(__file__).resolve().parent
A0,e0 = c.A0,c.e0


def ceilq(x,den=100):
    return F(-((-x.numerator*den)//x.denominator),den)


def interval_record(x):
    return F(x["lower"]),F(x["upper"])


def inventory():
    r,R,S = F(1,2),F(1,4),F(1,3)
    Qr = sum(abs(v)*R**k for k,v in enumerate(c.q))
    deltar = R*(1+R*R)*Qr/A0
    Z = (1+R)/(1-R)+R*(1+R)**2*Qr/A0
    n = (1+R)/(1-R)/(1-deltar)
    # z=(1-t)/(1+t) + zpoly(t).
    zp = [F(0)]*(len(c.q)+3)
    for k,v in enumerate(c.q):
        for off,mult in ((1,-1),(2,2),(3,-1)):
            zp[k+off] += mult*v/A0
    D = 4*R/(1-R)**2+sum(2*k*abs(v)*R**k for k,v in enumerate(zp))
    J0 = 4*(3+R)/(1-R)**3+sum(abs(v)*R**k for k,v in enumerate(c.Jpoly))
    # E coefficients: E_k=[t^k](1/z)/(2k). Bound the omitted absolute
    # coefficient sum using a larger weighted power-series algebra at S.
    N = 40
    zcoef = [F(1)]+[2*F(-1)**k for k in range(1,N)]
    for k in range(min(N,len(zp))):
        zcoef[k] += zp[k]
    inv = [F(1)]
    for k in range(1,N):
        inv.append(-sum(zcoef[j]*inv[k-j] for j in range(1,k+1)))
    Qs = sum(abs(v)*S**k for k,v in enumerate(c.q))
    deltas = S*(1+S*S)*Qs/A0
    assert deltas < 1
    Es = S/(1-S)+S*(1+S)**2*Qs/(2*A0*(1-deltas))
    Eo = sum(abs(inv[k])*R**k/(2*k) for k in range(1,N))+(R/S)**N*Es
    out = dict(Z=ceilq(Z),n=ceilq(n),D=ceilq(D),J=ceilq(J0),Eo=ceilq(Eo,1000))
    # Interval derivatives of rational functions, with exact translated
    # polynomials. Anchored Holder seminorm <= derivative supremum.
    tail = dict(Ha=F(0),K0=F(0),Hk=F(0),w2S=F(0),w2H=F(0))
    for i in range(128):
        a,b = r+(1-r)*F(i,128),r+(1-r)*F(i+1,128)
        u = J.var(c.box(a,b),1)
        t=u*u
        H=c.poly(c.H,t)
        aa=u*(1+u)*H/(1+t)
        k=2/u+2*u*(c.poly(c.Hp,t)/H-1/(1+t)+c.Fprime(t))
        w2=4*A0*u*(3-t)/(1+t)**3+c.poly(c.pp,u)
        for name,v in dict(Ha=aa.c[1],K0=k.c[0],Hk=k.c[1],
                           w2S=w2.c[0],w2H=w2.c[1]).items():
            tail[name]=max(tail[name],c.absmax(v))
    out.update({k:ceilq(v) for k,v in tail.items()})
    saved=json.loads((ROOT.parents[1]/"01-obstruction/data/obstruction_certificate.json").read_text())
    assert interval_record(saved["gstar"])[0] > F(2,5)
    assert F(saved["geometry"]["H_lower"]) >= A0
    assert F(saved["geometry"]["H_upper"]) < 2*A0
    assert F(saved["geometry"]["q_upper"]) < 0
    out["astar"]=A0*r*(1+r)/(1+r*r)
    out["gs"]=F(2,5)  # lower bound, used only in decreasing denominators
    out["w2star"]=A0+8*sum(c.q)
    out["gmin"]=F(4,5)*r*r/(1+r*r)
    out["W0"]=(out["astar"]/A0)**(-2)
    for p in (2,3):
        out[f"g{p}S"]=out["gmin"]**(-p)
        out[f"g{p}H"]=p*out["K0"]*out[f"g{p}S"]
    # These convenient rational majorants are verified against the interval
    # enclosures, not inferred from their displayed decimal approximations.
    chosen=dict(B_lower=F(7,25),DA=F(7,1000),De=F(71,10),
                KAA=F(7,1000),KAe=F(37,20))
    assert interval_record(saved["values_base"]["B"])[0] > chosen["B_lower"]
    for key,group,name in (("DA","values_base","BA"),("De","values_base","Be"),
                            ("KAA","values_box","BAA"),("KAe","values_box","BAe")):
        assert max(map(abs,interval_record(saved[group][name]))) < chosen[key]
    out.update(chosen)
    return out


def cert(ref,h,hp):
    r,sigma,theta,tau=F(1,2),F(1),F(9,10),F(1)
    ell=1-r
    Ar,AR=A0-h,A0+h
    Am,AM=Ar-tau,AR+tau
    bm,bp=2/AM,2/Am
    ep=e0+hp
    assert Am>2 and e0>hp and sigma>bp and theta+bm>1
    Z,n,D,J0,Eo=[ref[k] for k in ("Z","n","D","J","Eo")]
    astar,Ha,K0,Hk,w2S,w2H,gs,w2star,W0=[
        ref[k] for k in ("astar","Ha","K0","Hk","w2S","w2H","gs","w2star","W0")]
    gS={p:ref[f"g{p}S"] for p in (2,3)}
    gH={p:ref[f"g{p}H"] for p in (2,3)}
    Gamma0=1-(2+bp)*Eo
    assert Gamma0>0
    Z1=max(r*r,r**4,r**6,r**7/56)/A0
    D1=max(2*r*r,4*r**4,6*r**6,9*r**7/56)/A0
    J1=max(F(6),20*r*r,42*r**4,r**5)/A0
    ED=F(2,3)*n*n*Z1
    KD=2/astar*(1+K0*ell/2)
    Hg=F(4,3)*n*Z1+ED+ell*KD
    aD=2*ell/(3*astar)
    WD=(2+bp)*aD+(1+bp)*Hg
    d=min(F(1),1/(4*n*Z1),astar/(2*ell),1/(12*Hg),
          1/(4*WD),Gamma0/(2*(2+bp)*ED))
    rho=A0/Ar
    delta0=d/(2*rho)
    Nz=n/(1-n*Z1*d)
    Gamma=1-(2+bp)*(Eo+ED*d)
    assert Gamma>=Gamma0/2
    Tb=Nz**4/(2*Gamma)*(1+Z+Z1*d+D+D1*d+ep*AM*(J0+J1*d))
    Te=Nz**4*AM*(J0+J1*d)/(2*Gamma)
    Vb=Nz/Gamma
    Fop=r**(-5)*max(1/bm,1/(sigma-bp))
    Io,It=1/(1-bp),1/(theta+bm-1)
    cp=(1+bp)/(3*Am)
    amin=astar-ell*d/2
    Na=1/amin
    Hainv=(Ha+d/2)/amin**2
    KH=(1/(1+theta)+K0/2+Hk*ell/2)*Na+(1+K0*ell/2)*Hainv
    gSh={p:F(4,3)*gS[p] for p in (2,3)}
    gHh={p:F(4,3)*(gH[p]+p*gS[p]*d*KD) for p in (2,3)}
    Qstar=F(2,3)*(abs(w2star)+d)*(1/(A0*gs**2)+ep*AM/(A0*gs**3))
    Qestar=F(2,3)*AM/A0*(abs(w2star)+d)/gs**3
    QeH=AM/(2*A0)*((w2S+d)*gHh[3]+(w2H+d)*gSh[3])
    QH=((K0+d*KD)*gHh[2]+(Hk+d*KH)*gSh[2])/2+ep*QeH
    M=cp*(Fop*Tb+Qstar*Io*Vb+F(4,3)*W0*QH*It)
    Me=cp*(Fop*Te+Qestar*Io*Vb+F(4,3)*W0*QeH*It)
    DN=M/d
    KAv=rho*M/d*(1/tau+1/Ar)
    Kev=rho*Me/d
    Rvv=4*rho*rho*M/d**2
    DA,De,KAA,KAe,b0=[ref[k] for k in ("DA","De","KAA","KAe","B_lower")]
    par=DA*h+De*hp+KAA*h*h/2+KAe*h*hp
    margin=b0/2-par
    assert margin>0
    linear=DN+KAv*h+Kev*hp
    eps=min(delta0,margin/(2*(linear+Rvv*delta0)))
    # A convenient six-significant-digit rational radius below the formula.
    scale=10**13
    conservative_radius=F((eps.numerator*scale)//eps.denominator,scale)
    # Use the original quadratic inequality directly for a larger simple
    # closed-ball radius. No irrational root or rounding decision is needed.
    radius=F("0.0000045") if h else F("0.000005")
    assert radius<=delta0 and par+linear*radius+Rvv*radius**2<b0/2
    # If R_v is instead defined after subtracting the compatible phi_j,
    # N_raw <= (415/4) N_phi, as proved in 03-trace-uncertainty/PROOF.md.
    radius_phi=radius*F(4,415)
    C2=max(KAA/2,KAe/2,KAv/2,Kev/2,Rvv)
    values={k:v for k,v in locals().items() if isinstance(v,F)}
    values.update(ref)
    return {"exact":{k:str(v) for k,v in values.items()},
            "display":{k:float(v) for k,v in values.items()},
            "strict_budget_verified":True}


if __name__=="__main__":
    ref=inventory()
    cases={"varying_parameters":cert(ref,F("0.06"),F("0.0003")),
           "fixed_parameters":cert(ref,F(0),F(0))}
    data={"inventory_exact":{k:str(v) for k,v in ref.items()},
          "inventory_display":{k:float(v) for k,v in ref.items()},"cases":cases}
    (ROOT/"radius_certificate.json").write_text(json.dumps(data,indent=2)+"\n")
    print("inventory",data["inventory_display"])
    for k,v in cases.items():
        print(k,{n:v["display"][n] for n in
                 ("Gamma0","d","delta0","M","Me","DN","KAv","Kev","Rvv",
                  "par","margin","eps","radius")})
