"""Numerical comparisons, explicitly not interval certificates.

All three shapes are aligned to A0,e0. Suprema are found from polynomial
stationary-point equations: a dense grid brackets roots, then mpmath evaluates
the polynomial during scalar root refinement. No claim of a proved root count
or rounding bound is made. B is recomputed with the lead's supplied bref.py.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import resource
resource.setrlimit(resource.RLIMIT_AS,(1_900_000_000,1_900_000_000))
import sys
import json
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.optimize import brentq

mp.mp.dps=45
ROOT=Path(__file__).resolve().parent
import bref_input as bref

A0=F("10.150725")
e0=1/F("8.6000638")**2
r=F(1,2)
theta=F(9,10)


def M(q):
    return mp.mpf(q.numerator)/q.denominator if isinstance(q,F) else mp.mpf(q)


def deriv(p):
    return [k*p[k] for k in range(1,len(p))]


def peval(p,u):
    return mp.polyval([M(x) for x in p[::-1]],u)


def perturb(q):
    p=[F(0)]*(2*len(q)+6)
    for k,v in enumerate(q):
        for off,mult in ((3,1),(5,-2),(7,1)):
            p[2*k+off]+=mult*v
    return p


def candidates(poly,a,b):
    # The values refined below use 45 decimal places; longdouble is used
    # only for bracketing potential stationary points.
    x=np.linspace(float(a),float(b),16385,dtype=np.longdouble)
    pc=np.array([np.longdouble(str(M(c))) for c in poly[::-1]])
    y=np.polyval(pc,x)
    roots=[]
    for j in range(len(x)-1):
        if y[j]*y[j+1]<0:
            root=brentq(lambda z:float(peval(poly,M(z))),float(x[j]),float(x[j+1]),
                        xtol=1e-15)
            roots.append(M(root))
    return [M(a),M(b)]+roots


def sup_poly(poly,a,b):
    pts=candidates(deriv(poly),a,b)
    return max((abs(peval(poly,x)),x) for x in pts)


def distance(q1,q2):
    pp1,pp2=perturb(q1),perturb(q2)
    n=max(len(pp1),len(pp2))
    p=[(pp1[k] if k<len(pp1) else 0)-(pp2[k] if k<len(pp2) else 0) for k in range(n)]
    jets={j:p[j] for j in (3,5,7)}
    jet=sum(map(abs,jets.values()))
    raw=p[:]
    phi=p[:]
    for j,v in jets.items():
        raw[j]-=v
        phi[j]-=v
        phi[9]-=v*F(j-11,2)
        phi[11]-=v*F(9-j,2)
    # With sigma=1, division by u^6 is an exact polynomial operation.
    op=deriv(deriv(raw))[6:]
    op_phi=deriv(deriv(phi))[6:]
    so,xo=sup_poly(op,F(0),r)
    sp,xp=sup_poly(op_phi,F(0),r)
    w2=deriv(deriv(p))
    w3=deriv(w2)
    st,xt=sup_poly(w2,r,F(1))
    D=w2[:]
    D[0]-=sum(w2)
    critical=[F(0)]*max(len(D),len(w3)+1)
    for k,v in enumerate(w3):
        critical[k]+=v
        critical[k+1]-=v
    for k,v in enumerate(D):
        critical[k]+=theta*v
    # Remove the exact root at u=1 before bracketing.
    reduced=[]
    for cc in critical:
        reduced.append(cc+(reduced[-1] if reduced else 0))
    assert reduced[-1]==0
    reduced.pop()
    pts=candidates(reduced,r,F(1))
    def ratio(u):
        return abs(peval(D,u))/(1-u)**M(theta) if u<1 else mp.mpf(0)
    sh,xh=max((ratio(x),x) for x in pts)
    def fmt(x): return mp.nstr(x,15)
    return {"jet_sum_exact":str(jet),"jet_sum":fmt(M(jet)),
            "jet_differences_exact":{str(k):str(v) for k,v in jets.items()},
            "origin_raw":fmt(so),"origin_phi":fmt(sp),"tail_sup":fmt(st),
            "tail_holder":fmt(sh),"N_raw":fmt(M(jet)+so+st+sh),
            "N_phi":fmt(M(jet)+sp+st+sh),
            "maximizers":{"origin_raw":fmt(xo),"origin_phi":fmt(xp),
                          "tail_sup":fmt(xt),"tail_holder":fmt(xh)}}


def refs():
    fitted=json.loads((ROOT.parents[1]/"01-obstruction/data/fitted_reference.json").read_text())
    allrefs={"fitted":dict(A=A0,e=e0,q=list(map(F,fitted["q_power_coefficients_exact_decimal"])))}
    for K in (12,18):
        data=json.loads((ROOT/f"ref_c6g_K{K}.json").read_text(),parse_float=str)
        aa=F(data["A"])
        allrefs[f"K{K}"]=dict(A=aa,e=F(data["e"]),q=list(map(F,data["q_monomial"])))
    for v in allrefs.values():
        v["aligned_q"]=[A0/v["A"]*qq for qq in v["q"]]
    return allrefs


def analytic_examples():
    # Two-constants/Cauchy bound derived in the accompanying proof.
    a,b=mp.mpf(".02"),mp.mpf(".985")
    ctr,hh=(a+b)/2,(b-a)/2
    R=mp.mpf(4)
    ans=[]
    for d in map(mp.mpf,(".05",".1",".2",".3",".4")):
        # Max ellipse parameter on the closed d-neighbourhood of [0,1].
        S=max(a+b,2-a-b)+2*d
        v=S/(b-a)
        Rd=v+mp.sqrt(v*v-1)
        lam=1-mp.log(Rd)/mp.log(R)
        if lam<=0: continue
        C=d**-3+d**-5+d**-7+36*d**-9+2*d**-2+6*mp.mpf(".5")**mp.mpf(".1")*d**-3
        row={"d":str(d),"lambda":mp.nstr(lam,12),"C":mp.nstr(C,12)}
        for delta in map(mp.mpf,("1e-7","1e-6")):
            val=C*10**(1-lam)*delta**lam
            row[f"N_bound_delta_{delta}"]=mp.nstr(val,12)
        threshold=10*(mp.mpf("4.5e-6")/(10*C))**(1/lam)
        row["uniform_delta_needed_for_radius"]=mp.nstr(threshold,12)
        ans.append(row)
    return ans


if __name__=="__main__":
    rr=refs()
    pairs={}
    for left,right in (("K12","K18"),("K12","fitted"),("K18","fitted")):
        pairs[f"{left}-{right}"]=distance(rr[left]["aligned_q"],rr[right]["aligned_q"])
    print("distances",json.dumps(pairs,indent=2),flush=True)
    values={}
    for name,v in rr.items():
        # The lead routine changes global precision in Ref.__init__.
        qnums=[M(x) for x in v["aligned_q"]]
        rf=bref.Ref(M(A0),M(e0),qnums,dps=40)
        rf.setup(N=80)
        values[name]=mp.nstr(rf.B(),24)
        print("B aligned",name,values[name],flush=True)
    for pair in pairs:
        a,b=pair.split("-")
        pairs[pair]["B_difference_aligned"]=mp.nstr(mp.mpf(values[a])-mp.mpf(values[b]),18)
    result={"status":"numerical, no certified error bound for suprema or B values",
            "normalization":"aligned w_i=(A0/A_i)w_i_original; common A0,e0",
            "A0":str(A0),"e0":str(e0),"pairs":pairs,"B_aligned":values,
            "analytic_examples_numerical":analytic_examples()}
    (ROOT/"numerical_comparison.json").write_text(json.dumps(result,indent=2)+"\n")
