# Necessary L2 correction size on annuli of arbitrary radius

## Setting and statement

Let rho and U[rho] be smooth real fields on R2 with div U[rho]=0. Fix c and put V=cX+U[rho], F=V.grad rho-rho. Let U[h]=(-R1R2 h,R1^2 h), where Rj has Fourier multiplier i xi_j/|xi|. A correction is any real h in L2(R2) satisfying

F+div(Vh)-(2c+1)h+U[h].grad rho+div(h U[h])=0

in distributions. Local smoothness of the background suffices for this result; F need not belong to L2 globally. The multiplier obeys ||U[h]||2<=||h||2 by Plancherel, and h U[h] belongs to L1, so the equation is meaningful.

Let R>0. For 1<=s<=4 put q(s)=(s-1)^2(4-s)^2 and extend q by zero outside this interval. Define

phi_R(X)=y q(r^2/R^2)/R^2,
S(s)=(3c+1)q(s)+2cs q'(s),
W(s)=q(s)^2+[q(s)+2s q'(s)]^2,
A^2=(pi/2) integral_1^4 s S(s)^2 ds,
B_R^2=R^-4 integral_(R<r<2R) W(r^2/R^2)|U[rho]|^2 dX,
C_R^2=R^-4 integral_(R<r<2R) r^2 q(r^2/R^2)^2|grad rho|^2 dX,
I_R=|integral F phi_R|,
D_R=A+B_R+C_R,
H_R=108/R^2.

Every correction, with m=||h||2, satisfies

I_R <= D_R m+H_R m^2.                                  (1)

If I_R>0, then

m >= 2I_R/[D_R+sqrt(D_R^2+4H_R I_R)].                   (2)

These are necessary conditions at the fixed exponent c. They do not construct a correction. Taking the largest bound from finitely many radii remains valid and does not assert that all radii or all test functions were optimized.

## Weak estimate and admissibility of the probe

For smooth compact tests psi, integration by parts and the multiplier contraction give

|<F,psi>| <= m[||V.grad psi+(2c+1)psi||2+||psi grad rho||2]
             +m^2||grad psi||infinity.                 (3)

Although phi_R is piecewise polynomial, it belongs to C1 and has compact support. Indeed q and q' vanish at both endpoints. Mollification converges to phi_R together with its gradient uniformly on one fixed compact set. The linear coefficients there are bounded, h and U[h] are locally L2, and h U[h] is locally L1. Every term in the weak identity therefore converges, proving (3) for phi_R. No unproved regularity of h or behavior of the background at infinity enters this passage.

Set s=r^2/R^2. Direct differentiation gives

cX.grad phi_R+(2c+1)phi_R=(y/R^2)S(s),
grad phi_R=R^-2[q(s)e_y+2yX q'(s)/R^2].

The symmetric derivative of the vector map R^-2 q(s)X has eigenvalues R^-2 q(s) and R^-2[q(s)+2s q'(s)]. Thus |grad phi_R|^2<=R^-4 W(s). Also |phi_R|<=r q(s)/R^2 because q is nonnegative. Polar integration, using integral sin^2(theta)dtheta=pi and r^3dr=R^4s ds/2, proves the formula for A. The triangle inequality now bounds the linear bracket of (3) by D_R.

To prove the uniform derivative bound, write z=(s-1)/3 in [0,1]. The polynomials q and q+2s q' have degree-four Bernstein coefficients respectively

[0,0,27/2,0,0], and [0,27,135/2,-108,0].

This follows either by expanding q=81z^2(1-z)^2, or by the power-to-Bernstein formula. The Bernstein basis is nonnegative and sums to one. Both eigenvalue moduli are consequently at most108/R^2. Outside the annulus they vanish, and continuity covers the two boundaries. This proves H_R and then (1). Solving its increasing quadratic gives (2).

## Exact integral formulas for the campaign potentials

Set u=(1+r^2)^-1 and t=1-u. Let a=(1+4R^2)^-1, b=(1+R^2)^-1. The independently reconstructed residual has the finite representation

F=r sum_(ell,n) u^(ell delta/2) P_(ell,n)(t) sin(n theta).

If q(s)=sum_k q_k s^k, angular orthogonality gives

<F,phi_R>=(pi/(2R^2)) sum_(ell,k) q_k R^(-2k)
 integral_a^b t^(k+1) u^(ell delta/2-3-k) P_(ell,1)(t) du.       (4)

For a velocity component the radial representation is r^-3 u^(-b_j)t^2 Q_(j,n)(t); for a density derivative it is r^-4 u^(-b_j)t^2 Q_(j,n)(t), with b_j=(3+gamma-j delta)/2. For either B_R or C_R, a branch pair with an additional scalar polynomial weight sum_k w_k s^k contributes

(pi/(2R^4)) sum_k w_k R^(-2k)
 integral_a^b t^(k+1)u^(1-b_i-b_j-k) Q_i(t)Q_j(t)du.             (5)

The weight is W for B_R and q^2 for C_R. The extra r^2 in C_R exactly compensates the extra derivative. Off-diagonal branch pairs have factor two; the cosine zero mode has an additional factor two; different vector components are summed separately. Formula (5) follows by substituting r^2=t/u into the polar measure dX and the displayed radial fields. It uses every branch and every angular mode.

All polynomials and exponents are exact rationals. Replace t by1-u, multiply finite polynomials, and integrate each power. For exponent e,

integral_a^b u^e du=(b^(e+1)-a^(e+1))/(e+1) if e!=-1,
and log(b/a) if e=-1.

The endpoints are strictly positive, so every finite real power is integrable. This distinguishes these compact annular integrals from an unverified full-tail power integral. Arb arithmetic encloses the exact rational powers, logarithms, sums and square roots. The code requires positive squared norms and records all inputs, hashes, precision and real runtime. No radial quadrature, finite-tail replacement or asymptotic remainder estimate is used.

## Scope and verification

The fixed-radius formulas apply to any exact finite campaign potential satisfying the local smoothness assumptions. They can expose a large necessary L2 correction on an annulus even when a central point test is small. A rigorous value remains N4-ORIGIN until another lane reproduces it. The original weak identity and multiplier bound are also proved in ../pure_l2_probe/PROOF.md, independently reviewed by T4. This proof is written before executable evaluation. Code is in code/ and results in verification/. No formal proof-assistant build is run.
