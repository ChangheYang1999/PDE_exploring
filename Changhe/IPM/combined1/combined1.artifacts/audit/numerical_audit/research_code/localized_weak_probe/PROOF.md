# Necessary correction size at different radial scales

A smooth test function can detect a residual that a pointwise test misses. The probe y/(1+r^2)^2 used in the preceding result emphasizes the central region. Multiplication by t^k, where t=r^2/(1+r^2), moves its support toward larger radii while keeping every required integral in the exact finite-power class. The purpose here is to measure this change without a finite-box quadrature.

## Statement and hypotheses

Use the exact background assumptions and the divergence-form correction equation of ../pure_l2_probe/PROOF.md: smooth rho and U[rho], div U[rho]=0, U[rho]=O(r^gamma), grad rho=O(r^(gamma-1)) with gamma<1, F=(cX+U[rho]).grad rho-rho in L2, and a real distributional correction h in L2 at the same c. Set u=(1+r^2)^(-1), t=1-u. For an integer k>=0 define

phi_k=y t^k u^2,
A_k=||phi_k[(3c+1)+2c k u-4c t]||2,
B_k=||t^k u^2[1+2k u+4t] U[rho]||2,
C_k=||r t^k u^2 grad rho||2,
I_k=|<F,phi_k>|,
D_k=A_k+B_k+C_k.

For nonnegative integers a and positive integers b define

S(a,b)=a^a b^b/(a+b)^(a+b) if a>0, and S(0,b)=1.

Take H_0=1 and, for k>=1,

H_k=S(k,2)+2k S(k,3)+4 S(k+1,2).

Then every correction h as above, with m=||h||2, satisfies

I_k <= D_k m+H_k m^2.                                    (1)

In particular, when I_k>0,

m >= 2 I_k/[D_k+sqrt(D_k^2+4H_k I_k)].                    (2)

A maximum over finitely many k is still a necessary lower bound. No assertion is made that this finite list optimizes all test functions. The bounds concern one background at its fixed exponent; they do not exclude arbitrary distant stationary profiles.

## Proof of the necessary inequality

For a smooth test phi the divergence-form weak equation and the L2 contraction of the velocity multiplier give

|<F,phi>| <= m[||V.grad phi+(2c+1)phi||2+||phi grad rho||2]
              +m^2||grad phi||infinity,
V=cX+U[rho].

The proof and cutoff removal are in ../pure_l2_probe/PROOF.md. The same cutoff argument applies to phi_k: for each fixed k it is smooth, behaves as O(r^-3) at infinity, and its gradient is O(r^-4). Its additional zero at the origin introduces no singularity.

For r>0 differentiation gives

grad phi_k=t^k u^2[e_y+2yX u(k u/t-2)].

The apparent factor 1/t is canceled when k>=1; when k=0 its coefficient vanishes. By continuity the resulting polynomial identity holds at the origin. Since |yX|<=r^2 and r^2 u=t,

|grad phi_k| <= t^k u^2[1+2k u+4t].                       (3)

Also |phi_k|<=r t^k u^2, and

cX.grad phi_k+(2c+1)phi_k=phi_k[(3c+1)+2c k u-4c t].

These facts and the triangle inequality bound the two linear norms by D_k. The maximum of t^a(1-t)^b on [0,1] is S(a,b), by differentiation, including the endpoint case a=0. Taking the supremum in (3) term by term proves the stated H_k for k>=1. The sharper value H_0=1 was proved by the eigenvalues of the derivative of X/(1+r^2)^2 in the preceding result. This proves (1). The positive quadratic root gives (2).

## Exact whole-plane evaluation

The independently reconstructed residual has the finite form

F=r sum_(ell,n) u^(ell delta/2) P_(ell,n)(t) sin(n theta).

Angular orthogonality gives

<F,phi_k>=(pi/2) sum_ell integral_0^1 t^(k+1) u^(ell delta/2-1) P_(ell,1)(t) dt.       (4)

The parameter here is p=2 throughout. Every integral is evaluated by shifting its exact polynomial from t to u and applying integral_0^1 u^(b+j)du=1/(b+j+1). The exponent b>-1 is checked; failure stops evaluation.

For either velocity or density-gradient components the radial-Fourier representation has the form r^(-a)u^(-b_j)P_(j,n)(t), with a=3 or4 respectively, and b_j=(3+gamma-j delta)/2. The first two polynomial coefficients vanish exactly, so P=t^2 Q. After angular orthogonality, the pair of branches i,j in B_k^2 contributes

(pi/2) integral_0^1 t^(2k+1) u^(5-b_i-b_j)
 Q_i(t)Q_j(t)[1+2k u+4t]^2 dt.                            (5)

For C_k^2 the expression is the same without the last squared bracket. The identical exponent follows from the extra factor r in C_k and the extra derivative a=4. Off-diagonal branch pairs have factor two; cosine zero has angular factor two; vector components are summed separately. These are the same independently verified field expansions as in ../weak_probe/PROOF.md.

For A_k, put a=2k+2, b=2, L0=3c+1+2ck, L1=2c(k+2). The beta-integral identity gives

A_k^2=(pi/2) B(a,b)[L0^2-2L0L1 a/(a+b)+L1^2 a(a+1)/((a+b)(a+b+1))],
B(a,2)=1/[a(a+1)].                                       (6)

All polynomial coefficients and exponents start as exact rationals. Conversion to outward Arb balls, polynomial multiplication, finite summation and square roots enclose (4)-(6). The computed H_k is exact rational. A positive lower endpoint is required for every squared norm and for each claimed nonzero pairing. No asymptotic truncation, radial cutoff or quadrature enters a reported certificate.

## Evidence and scope

The source coefficient and residual-cache hashes, precision, k, all constituent norms, and the positive root are recorded for every run. Code is in code/ and numerical evidence in verification/. New values remain N4-ORIGIN until another lane reproduces them. The selection of k is a diagnostic search; the inequalities for each recorded k are rigorous if its interval evaluation succeeds.
