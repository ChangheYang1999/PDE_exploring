# Canonical weighted tail pinning and its application to candidate007

Status: independent audit of Opus R1-023 R1/R2 and T2 the review of T4-189 R1/R2.
The exact candidate calculation is stored separately and initially OPEN
numerical-lane reproduction. The analytic reductions need no numerical data.

## Statement and normalization

Let 0<gamma<1 and 0<=a<=1+gamma. Put
w_a(X)=(1+|X|^2)^(-a/2). Let rho,u be smooth real fields, with rho of
S1 parity, div u=0, |u(X)|<=C_u |X|^gamma outside the unit disk, and

    rho(r,theta)=r^gamma Theta(theta)+o(r^gamma)

uniformly in angle, with smooth nonzero Theta. Let h be a real S1 element
of L2(w_a^2 dX). Define v=U[h] as the continuous extension of the canonical
IPM velocity from compact smooth S1 functions in that space. Suppose

    c' div(X(rho+h))-(2c'+1)(rho+h)+div((u+v)(rho+h))=0

in distributions for a real constant c'. Then c'gamma=1. In particular
neither a separate weighted norm assumption on v nor a bound for grad rho
is needed. If the C1, nonzero origin-slope hypotheses of T4-189 also hold,
its conclusion c[h]=0 remains valid, with the canonical contact term.

## Proof of the two analytic reductions

The audited odd velocity estimate T4-177/T4-192 gives

    ||w_a U[h]||2 <= 2/(2-a) ||w_a h||2,

since a<=1+gamma<2. Smooth compact S1 functions are dense in this weighted
space: truncate radially and mollify with an even radial kernel, which
preserves parity, then use local weighted equivalence with unweighted L2.
The bounded extension is unique. Convergence in the weighted space implies
local L2 convergence, so div v=0 in distributions. This establishes the
velocity hypothesis of the original proof without an unweighted Fourier
multiplier assumption for growing h.

Uniform tail convergence gives |rho(X)|<=C_0 |X|^gamma for |X|>=1.
Use the same escaping test phi_R=R^(-gamma-2)psi(X/R), supported in
R<|X|<2R, as T4-189. Keep the two background-density transport terms
in divergence form. Their bounds are

    |int rho u.grad phi_R|
       <=4^gamma C_0 C_u R^(gamma-1)||grad psi||1,
    |int rho v.grad phi_R|
       <=2^gamma C_0 5^(a/2) R^(a-2) n_R ||grad psi||2,

where n_R=||w_a v||_(L2(R<r<2R)) tends to zero. These replace the two
bounds that used grad rho and have the same decay powers. All remaining
terms and the nonzero limit (c'gamma-1)J are unchanged from T4-189.
Their powers are a-gamma-1<=0, a-2<0 and 2a-gamma-3<0. Hence every error
vanishes and c'gamma=1. This independently confirms both reviewers'
analytic simplifications.

## Exact candidate007 leading profile

Use c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
d=3+gamma. Its finite canonical potential expansion is

    chi=sum C_(j,m,k) r^(2k)(1+r^2)^(p_j-k) cos(2m theta),
    p_j=(d-j delta)/2,
    rho=-partial_y Delta chi.

Every term is smooth at the origin because k>=m. At infinity the j=0
leading potential is r^d sum_m A_m cos(2m theta), with
A_m=sum_k C_(0,m,k). Every j>=1 is lower order by at least delta>0;
each radial expansion within a branch has its next term lower by2.
These finite smooth radial powers admit termwise differentiated uniform
expansions of every fixed order, by Taylor expansion of (1+r^-2)^p.
Thus rho has a uniform leading term r^gamma Theta and the canonical
velocity, made from three derivatives of chi, is O(r^gamma).

For a homogeneous angular potential r^d A_m cos(n theta), n=2m,

    Delta = A_m(d^2-n^2)r^(d-2)cos(n theta),
    partial_y[r^k cos(n theta)]
      = r^(k-1)[(k-n)sin((n+1)theta)-(k+n)sin((n-1)theta)]/2.

Consequently the sin(theta) coefficient of Theta is exactly

    b_1=-A_0 d^2(d-2)+A_1(d^2-4)d/2.

All quantities in this formula are rational. The accompanying check
loads the already hashed canonical007 JSON and proves 18<b_1<19 by
integer comparisons. Therefore Theta is nonzero, once that finite check
is independently accepted. This is stronger evidence than a FLOAT print,
but does not replace the numerical-lane independence rule.

## Scope and dependencies

The analytic dependencies are the audited T4-177 velocity theorem and
T4-189 weak tail argument. The canonical application uses the exact
snapshot hash and its canonical representation, independently checked in
T4-195. This theorem concerns the original weighted affine chart only.
It does not exclude a solution in another chart with a different tail,
and gives no distance between charts. No inverse or existence claim.
