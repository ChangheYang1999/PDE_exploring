"""Construct a trial reference; the fit is not a bound in N.

All coefficients are frozen as exact decimal strings. Negativity of the resulting
trace is checked with rational Bernstein bounds; sample residuals remain numerical.
"""
import resource
resource.setrlimit(resource.RLIMIT_AS,(1_900_000_000,1_900_000_000))
import json
import math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicHermiteSpline
from numpy.polynomial import Polynomial, Chebyshev

ROOT=Path(__file__).resolve().parent.parent/"data"
DATA=ROOT/"c6g_traces.npz"


def bernstein(coeff,a,b):
    n=len(coeff)-1
    cc=[sum(coeff[j]*math.comb(j,k)*a**(j-k)*(b-a)**k
            for j in range(k,n+1)) for k in range(n+1)]
    return [sum(cc[k]*F(math.comb(i,k),math.comb(n,k)) for k in range(i+1))
            for i in range(n+1)]


if __name__=="__main__":
    data=np.load(DATA,allow_pickle=False)
    A0,L=10.150725,8.6000638
    uu=data["x"]/L
    trace=CubicHermiteSpline(uu,data["w"]/L,data["wp"])
    nodes=np.linspace(.02,.985,701)
    base=lambda u:-A0*u*(1-u*u)/(1+u*u)
    fac=lambda u:u**3*(1-u*u)**2
    # Fit w, not q=(w-base)/fac: division near endpoints magnifies trial noise.
    mat=np.polynomial.chebyshev.chebvander(2*nodes**2-1,12)*fac(nodes)[:,None]
    coeff=np.linalg.lstsq(mat,trace(nodes)-base(nodes),rcond=None)[0]
    q=Chebyshev(coeff,domain=[0,1]).convert(kind=Polynomial)
    frozen=[format(float(c),".17g") for c in q.coef]
    qr=[F(c) for c in frozen]
    # w=-u(1-u^2)/(1+u^2)*H(u^2), H=A0-t(1-t^2)q(t).
    H=[F("10.150725")]+[F(0)]*(len(qr)+3)
    for i,c in enumerate(qr):
        H[i+1]-=c
        H[i+3]+=c
    while H[-1]==0:
        H.pop()
    lower=min(min(bernstein(H,F(i,128),F(i+1,128))) for i in range(128))
    assert lower>=F("10.150725")
    fit=lambda u:base(u)+fac(u)*Polynomial([float(F(c)) for c in frozen])(u*u)
    inband=(uu>=.02)&(uu<=.985)
    err=fit(uu[inband])-data["w"][inband]/L
    out={
        "status":"trial fit; no N-distance or obstruction certificate",
        "source_file":"reference_fit/data/c6g_traces.npz",
        "A0_exact":"10.150725","L0_exact":"8.6000638",
        "e0_exact":"1/(8.6000638)^2",
        "q_power_coefficients_exact_decimal":frozen,
        "fit_method":"701 equally spaced u in [0.02,0.985], unweighted least squares of w; degree 12 Chebyshev basis in u^2",
        "data_c_l":float(data["c_l"]),
        "source_slope_data_minus_A0":float(trace(1,1)-A0),
        "sampled_sup_w_residual_on_fit_band":float(np.max(np.abs(err))),
        "sampled_rms_w_residual_on_fit_band":float(np.sqrt(np.mean(err*err))),
        "sampled_sup_r12_residual_on_fit_band":float(np.max(np.abs(base(uu[inband])-data["w"][inband]/L))),
        "H_positive_rational_lower":f"{lower.numerator}/{lower.denominator}",
        "H_positive_lower_decimal":float(lower),
        "positivity_certificate":"exact rational Bernstein coefficients on 128 equal subintervals of [0,1]",
        "missing":"No certified g0, B0, or N-distance to the stored data; sampled w accuracy does not imply origin remainder accuracy."
    }
    (ROOT/"fitted_reference.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({k:v for k,v in out.items()
                      if k not in ("H_positive_rational_lower",)},indent=2))
