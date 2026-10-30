# Whole-plane weak distances at large radial indices

## Exact reference, spaces and statement

Fix the immutable candidate C1-N1-007-d2w-j7-e2bal with raw SHA256
ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21
and canonical SHA256
153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316.
Put c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
The canonical potential gives rho=-partial_y Delta chi and
u=(-chi_xyy,chi_xxy). Its independently audited exact origin and tail
constraints imply smooth S1 fields with sublinear growth O(r^gamma),
and its complete residual F=(cX+u).grad rho-rho belongs to L2(R2).

Let h be real, S1-symmetric and in L2(R2). Require that rho+h solve the
stationary equation at the same c in distributions, with the canonical
velocity decomposition U[rho+h]=u+U[h], divergence-free U[h],
||U[h]||2<=||h||2 and locally integrable weak products. For an integer
K>=1 set t=r2/(1+r2), v=1-t and phi_K=r v2 t^K sin(theta). Define

    I_K=int F phi_K,
    M_K=(2c+1)phi_K+(cX+u).grad phi_K,
    Cx_K=phi_K rho_x, Cy_K=phi_K rho_y,
    D_K=||M_K||2+sqrt(||Cx_K||2^2+||Cy_K||2^2).

Given a rigorously checked rational H_K>||grad phi_K||infinity,

    ||h||2 >= 2|I_K|/[D_K+sqrt(D_K^2+4H_K|I_K|)].          (1)

The computation supplies containing intervals at the exact finite list
of K recorded in its manifest. A strict rational floor is tested against
the containing interval, and remains OPEN independent candidate-level
review until that review is recorded. No full residual norm, inverse,
existence statement or global optimization over K follows. The all-c
extension requires the separate common-leading-tail chart theorem.

## Weak argument and cutoff justification

Subtract the equations and test with a smooth cutoff of phi_K. Integrate
both divergence-free transport terms by parts to obtain

    I_K=int h M_K-int phi_K U[h].grad rho
                         +int h U[h].grad phi_K.

The origin is smooth: r^(2K+1)sin(theta)=y(r2)^K. At infinity phi_K
is O(r^-3) and its gradient O(r^-4), for each fixed K. Reference fields
are sublinear. The displayed products converge by Cauchy-Schwarz and
the bound for U[h]. The corresponding escaping-annulus L2 norms tend
to zero, so the cutoff errors vanish. Thus
|I_K|<=D_K||h||2+H_K||h||2^2. Solving this quadratic gives(1).
Integration of the reference transport separately gives
I_K=-int rho M_K, which provides a second numerical pairing path.

## Keep the radial index outside the polynomial arrays

The previously audited factored construction gives, for n=1,

    phi_r=v2 t^K G sin(theta),
    phi_theta/r=v2 t^K cos(theta),
    G=(2K+1)-(2K+4)t.

Cartesian conversion and exact trigonometric products produce M_K,
Cx_K and Cy_K from every background angular mode. Each has the form

    r v2 t^K sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) trig(n theta).

All P are exact rational polynomials. K enters only through scalar
coefficients; the common t^K is never expanded into an array. For M_K
the coefficients are affine in K, and for Cx_K,Cy_K they are independent
of K. The constructor is checked coefficientwise against the audited
ordinary polynomial constructor at K=3,n=1. Actual fields at three
Cartesian points are also checked against directly differentiated phi.
This uses this lane's own factored construction, already independently
checked for candidate013 in N4-204. No foreign code is executed.

## Complete energies and two endpoint recurrences

Angular orthogonality contributes pi to each nonzero trigonometric
mode. Each vector component is squared separately. Retain every radial
cross term in the same frequency with multiplicity two. A product of
branches ell,j contributes

    (pi/2) int_0^1 v^b (1-v)^m P(1-v) Q(1-v) dv,
    b=1+(ell+j)delta/2, m=2K+1.

Construct both product polynomials in t and v with outward Arb
arithmetic, after exact conversion of each rational field polynomial.
For a polynomial R, the moments are finite Beta sums. Starting from
B(b+1,m+1), the v-endpoint recurrence multiplies the jth moment by
(b+j+1)/(b+m+j+2); the t-endpoint recurrence multiplies it by
(m+j+1)/(b+m+j+2). All inputs satisfy b>-1 and m>=0. These identities
follow from Gamma(z+1)=z Gamma(z). Gamma and all arithmetic are outward
Arb operations. Require the complete positive energy to have more than
150 relative bits and both endpoint intervals to overlap.

The direct pairing uses the whole first-sine projection and formula(1)
of ../far_pairing_audit/PROOF.md. Its four small-index calibration and
complete coefficient comparison against the full residual are already
bound there. This audit rehashes the projection and that result, computes
I_K anew, and requires agreement at every shared K. The independent
parts pairing uses rho and M_K without assembling any residual derivative.
Require both paths to overlap with more than150 relative bits.

## Exact finite maximum of the probe gradient

At fixed radius the angular maximum of |grad phi_K| is the larger of
v2(1-v)^K and |v2(1-v)^K[-3+(2K+4)v]|. The first reaches its maximum
at v=2/(K+2). Both radial endpoints vanish for K>=1. Dividing the
radial amplitude derivative by v(1-v)^(K-1) gives

    -6+(9K+18)v-(2K+4)(K+3)v2.

Check this polynomial identity exactly. Its discriminant is
3(K+2)(11K+6)>0. Enclose both quadratic roots and check they lie in
(0,1). The absolute radial amplitude is bounded by its values at these
two roots, since its zeros have value zero. Evaluate the angular
amplitude at its critical point. Choose a rational H_K strictly above
all three outward amplitudes and verify those strict inequalities.
The exact defining K, polynomial, roots and rational H_K are stored.
No huge expanded rational K^K is constructed; Arb integer powers use K
as an exponent. This is a complete finite critical-point argument.

## Compare the same denominator quantities used by N1

N1's frozen far_weak model extrapolates the following two norm envelopes
from a finite mesh value at K4096:

    Benv_K=||v2 t^K [1+2K v+4t] |u|||2,
    Cenv_K=||r v2 t^K |grad rho|||2.

Define also A_K=||(2c+1)phi_K+cX.grad phi_K||2. Since
|grad phi_K|<=v2 t^K[1+2K v+4t] and |sin(theta)|<=1,

    ||M_K||2<=A_K+Benv_K,
    sqrt(||Cx_K||2^2+||Cy_K||2^2)<=Cenv_K.                 (2)

These envelopes differ from the exact combined norm M_K and exact C_K.
The comparison with N1 must use Benv,Cenv, not those smaller norms.
Square the complete Fourier amplitudes of u1,u2,rho_x,rho_y, including
the factor2 for a constant cosine mode. After compactification their
radial product groups have b=5-p_i-p_j. Integrate them with power
m=2K+1 and multiplier [5+(2K-4)v]^2 for Benv, or multiplier1 for Cenv.
The complete A_K is

    A_K^2 = pi/[2a(a+1)]
       *[L0^2-2L0 L1 a/(a+2)+L1^2 a(a+1)/((a+2)(a+3))],
    a=2K+2, L0=3c+1+2cK, L1=2c(K+2).

This follows by integrating the square of
r v2 t^K[L0-L1 t]sin(theta). All envelope moments are over the whole
plane and require positive high-accuracy balls. At K1024 compare A,
Benv and Cenv with the independently audited earlier complete probe.
Check(2) numerically as an additional consistency test. Report each
N1 estimate's relative error against the corresponding complete norm.
This is a finite-list comparison, not a certified asymptotic rate.

## Data, execution and limits

All coefficients remain in exact JSON, consumed through the existing
source and projection interfaces. The manifest binds every source,
proof, executed module, previous calibration and frozen N1 model.
Large caches are read only from this lane. Outputs are small per-K
records and a manifest. Each accepted K can be resumed without
recomputing it after checking the manifest hash. Precision is at least
2048bits. Formal verification evidence here means executable exact and
outward arithmetic records; no Lean or Lake build is run. Only one CPU
computation runs at a time. This proof is written and checked before
the implementation.
