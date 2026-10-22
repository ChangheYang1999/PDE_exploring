# Endpoint audit of an unweighted compactified polynomial inverse

UTC 2026-10-21T02:29:47.715187+00:00. Status: analytic diagnostic, prior to implementation. This concerns the lead's dr.py discretization, not a nonexistence result.

## Statement, hypotheses and notation

Put r=L tan(pi rho/2), L>0 and0<rho<1. Suppose a radial Fourier source coefficient is represented by its polynomial interpolant p(rho) at interior Chebyshev-Gauss nodes. For the sin(2theta) vorticity mode the canonical center strain, when defined, is

    c=(1/2) integral_0^infinity q(r)/r dr,
    q(r)=p((2/pi) arctan(r/L)).                         (1)

If either endpoint value p(0) or p(1) is nonzero, the corresponding one-sided improper integral in(1) diverges logarithmically. If p(1) is nonzero, the standard mode2 exterior Green integral also diverges. A finite Gauss rule over the compactified endpoint interval cannot certify that these integrals exist. This is a conditional statement about the literal interpolant; the numerical endpoint values of any particular data set must be checked.

For the first cosine mode, a nonzero p(1)=a instead yields a well-defined relative inverse at every finite r, but its velocity has a nonzero term linear in r. It is therefore outside the required sublinear velocity class. A nonzero p(0) in a positive angular mode also violates continuity of the source at the origin.

These facts do not exclude convergence of a sequence of discretizations to admissible functions. An endpoint-aware representation or a specified exterior extension can remove the defect. A Gaussian calibration, by itself, does not measure slow-tail accuracy.

## Proof of the endpoint statements

The change of variables satisfies

    (dr/d rho)/r = pi/[sin(pi rho)],

which is rho^-1+O(rho) at0 and(1-rho)^-1+O(1-rho) at1. Polynomial continuity gives p(rho)=p(0)+O(rho) and p(rho)=p(1)+O(1-rho). Thus a nonzero endpoint produces a fixed-sign nonintegrable term in the respective one-sided integral. Possible cancellation between endpoints is not ordinary convergence and is not the canonical inverse specified here. The mode2 exterior Green term uses the same integral integral_r^infinity q(t)/t dt, so the infinity statement follows directly.

For mode1, the relative stream coefficient is

    h(r)=(1/2)[r^-1 integral_0^r t²q(t)dt
                         -r integral_0^r q(t)dt].     (2)

As r tends to infinity, rho=1-2L/(pi r)+O(r^-3), hence q(r)=a+O(r^-1). Integration in(2) gives h(r)=-a r²/3+O(r log r). Consequently h'(r)=-2a r/3+O(log r), and the angular velocity formulas include nonzero linear terms. In particular V=o(r) fails if a is nonzero. At the origin, an angular mode with nonzero radial limit approaches different values along different rays, proving the continuity statement. This proves all asserted implications.

## Smooth slow-tail manufactured controls

Fix 0<s<1. The following Cartesian-smooth sources have the desired r^-s decay:

    omega1=x(1+r²)^[-(1+s)/2],
    omega2=2xy(1+r²)^[-1-s/2].                          (3)

Their radial coefficients are q1=r(1+r²)^[-(1+s)/2] and q2=r²(1+r²)^[-1-s/2]. Formula(1) gives exactly c2=1/(2s). The mode1 source has center strain0. For u=1+r², the radial integrals in(2) are

    I1=(u^[(1-s)/2]-1)/(1-s),
    A1=(u^[(3-s)/2]-1)/(3-s)
                         -(u^[(1-s)/2]-1)/(1-s).

For mode2, define

    A2=(1/2){(u^[2-s/2]-1)/(2-s/2)
             -2(u^[1-s/2]-1)/(1-s/2)
             +(u^[-s/2]-1)/(-s/2)},
    B2=u^[-s/2]/s.

Substitution t²+1=v in each integral verifies these primitives, their zero lower limits, and the exact tail integral. The mode2 stream and radial derivative are

    h2=(A2/r²+r² B2)/4,
    h2'=(-A2/r³+r B2)/2.                              (4)

Use Vr=-(1/r)partial_theta Psi, Vtheta=partial_r Psi. Equations(2),(4) therefore supply references independent of any Chebyshev interpolation or modal recurrence implementation. High precision arithmetic avoids subtractive cancellation at small r. The represented-polynomial endpoint values and the exact-source quadrature errors answer different questions and are reported separately.

## Dynamic normalization and scope

For the lead's evolution Omega_tau=-W.grad Omega+c_w Omega+Theta_x and Theta_tau=-W.grad Theta+(c_l+2c_w)Theta, with W=c_l X+V, preserving a0=Theta_xx(0)/2 and b0=Omega_x(0) gives c_w=c_l/2-c and c_l=4a0/b0. If a steady state has k=-c_w>0, set Omega_B=Omega/k, Theta_B=Theta/k², V_B=V/k and beta=c_l/k. Dividing its equations by k² and k³ respectively gives precisely B2-P. The center strain becomes c/k=1+beta/2. This is an amplitude normalization of a steady state, not a claim that any computed trajectory converges.

Dependencies: elementary Fourier-mode Green formulas, displayed and verified by differentiation; no external theorem beyond the full-plane inverse convention. No code from numerics will be imported. The lead's code may be copied into the verifier lane only to reproduce its behavior; all endpoint and reference calculations are independently implemented. No JavaScript/TypeScript, servers, RLScience cluster, Lean/Lake or GPU execution.
