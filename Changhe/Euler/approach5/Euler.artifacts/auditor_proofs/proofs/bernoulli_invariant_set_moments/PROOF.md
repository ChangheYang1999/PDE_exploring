# Bernoulli and helicity identities on measurable invariant sets

## Exact hypotheses and statement

Let 2/5<c<1/2, omega be any finite real number, J(x1,x2,x3)=(-x2,x1,0), A=cI-omega J, a=1-2c, d=3c, k=(1-c)/c and eta=k-1=a/c. Let U be C2 and P be C1 on R3, with

    div U=0,
    (1-c)U+(Ay+U).grad U+omega JU+grad P=0.

Assume U is bounded, U(R .)->0 in distributions, and integral_1^infinity sup_(|y|>=r)||DU(y)|| dr/r is finite. Put B=Ay+U, Omega=curl U, h=U.Omega, g=U.B and H=P+|U|^2/2+Ay.U. The flow Phi of B and flow Gamma of Omega are complete.

There is a constant p_inf such that H0=H-p_inf and P0=P-p_inf satisfy

    |H0(y)|+|P0(y)|<=C(1+|y|)^(-eta).

P0 is the canonical L2 pressure. Under these hypotheses:

1. If D is open, Phi_T(D)=D for some T>0, and H composed with Phi_T equals H on D, then H=p_inf on D.
2. The helicity h belongs to L1(R3). For every measurable set E invariant under the whole Gamma flow,

       integral_E h dy=0.

3. For every measurable set D invariant under the whole Phi flow and every finite p>pcrit=3/eta,

       a p integral_D |H0|^(p-2) H0 g dy
           =d integral_D |H0|^p dy.

   Both integrals converge absolutely. Equivalently, with F=P0-|U|^2/2,

       integral_D |H0|^(p-2) H0 F dy
           =(1-d/(a p)) integral_D |H0|^p dy.

The statements audit Theory Agent A C28 and Corollaries H.1-H.3. The measurable-domain version of part3 is slightly stronger than its open-domain formulation. Part2 is an integral cancellation, not pointwise zero helicity.

## Pressure, bounds, and completeness

A209-A210 give the complete B flow, a proper scattering map S, a compact null core C=S^(-1)(0), and bounds |U|<=C(1+r)^(-k), |Omega|<=C(1+r)^(-k-1). They also give |Phi_t x-exp(tA)Sx|<=sup|U|/c. The vorticity is globally bounded, so its C1 flow is complete.

The exact Lamb relation is aU+grad H=B cross Omega. It gives |grad H|<=C r^-k outside a ball. Since k>1, radial integration gives a uniformly approached limit on each ray. The oscillation across a radius-r sphere is at most pi r sup|grad H|=O(r^(1-k)); thus the limits agree in p_inf and H-p_inf=O(r^-eta). Since |U|^2/2+Ay.U has that same bound, so does P-p_inf.

The tail gives U in L4, hence the canonical double-Riesz pressure is L2. A031 identifies its gradient with grad P, so the difference is a constant. The only possible L2 representative has zero limiting constant, proving the claim about P0. This also follows directly from the harmonic-difference and large-ball-mean argument in C28. No pressure normalization is assumed before determining p_inf.

For every x outside C, Phi_t x tends to infinity. Thus in part1,

    H(x)=H(Phi_(nT)x)->p_inf.

The complement of C is dense in D because C is null; continuity proves part1 everywhere on D. Only the stated discrete invariance is used.

## Helicity cancellation without an ergodic theorem

The bound |h|<=C(1+r)^(-2k-1) is integrable because k>1. Set

    f(y)=(1+|y|^2)^((k+2)/2), X=f Omega, dmu=f^-1dy.

The C1 field X has at most linear growth and therefore a complete flow chi. It preserves mu since div(f^-1X)=div Omega=0. The measure is finite, because k+2>3. The flows of X and Omega have the same oriented complete orbits; their time change is positive and f>=1. In particular every E as stated is chi-invariant. The bounded function H0 belongs to L1(mu), and fh belongs to L1(mu).

The exact equation Omega.H0=-a h gives, for any finite T>0,

    H0(chi_T x)-H0(x)=-a integral_0^T (f h)(chi_t x)dt.

Integrate over E with respect to mu. The left side is zero by invariance. Fubini is legitimate because the integral of the absolute right-side integrand is T integral_E |h| dy. Invariance on the right gives

    0=-a T integral_E h dy.

This proves part2. No limiting orbit, invariant-support value, basin regularity, or ergodic decomposition has been used. The proof applies to exact measurable invariant sets; changing them on null sets does not affect the integral.

## Bernoulli moments and all boundary terms

First, for every compactly supported C1 scalar psi,

    integral_D div(B psi)dy=0.

Indeed integral_D psi(Phi_t x)exp(dt)dx equals integral_D psi(y)dy by invariance. Differentiation at zero is dominated on a fixed compact set for small t. This proves the formula even when D has no regular boundary.

Take psi=|H0|^p chi_R, where chi_R is a smooth radial cutoff equal to1 on B_R and0 outside B_(2R), with |grad chi_R|<=C/R. Since BH0=-a g,

    div(B|H0|^p)=d|H0|^p-a p |H0|^(p-2)H0 g.

Both terms are absolutely integrable: H0 and g are bounded on compact sets and O(r^-eta) at infinity, so their displayed products are O(r^-peta), with peta>3. The cutoff error is bounded by C R^(3-peta), which tends to zero. Dominated convergence proves part3. No boundary term of D is discarded; invariance established its distributional replacement exactly.

Finally H0=F+g, so substitute g=H0-F to obtain the equivalent formula. The coefficient 1-d/(ap) is positive in the stated range. This forces a correlation, not a pointwise sign or vanishing of either field. For arbitrary P the formula must use H-p_inf. Adding an arbitrary pressure constant to H0 would generally destroy its global Lp integrability.

## Dependencies and scope

Dependencies are the already confirmed A031, A209-A210, A295, completeness for at-most-linear C1 fields, ordinary change of variables, Fubini, and cutoffs. Every finite omega is included; constants can depend on it. Full Dini decay is additional to the prompt. Parts1-3 do not prove that helicity has one sign, that basins cover the vortical set, or that U vanishes. No computation or formalization was used.
