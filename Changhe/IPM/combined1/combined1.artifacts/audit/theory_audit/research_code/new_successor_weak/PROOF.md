# Frozen weak tests for newly published ordinary-basis successors

Status: analytic method audited in T4-182/T4-185 and subsequent independent
reproductions. Each new candidate computation is OPEN until independently
verified. This note defines the new raw-input path and its exact scope.

## Statement

Fix c>1 and a smooth S1 reference density R with canonical incompressible
velocity U_R. Here S1 means even in x and odd in y. Let rho=R+h solve

    (cX+U[rho]).grad rho-rho=0

weakly on the plane, with h in L2 and the canonical velocity difference
U[h] in L2. The order-zero Fourier multiplier for U satisfies
||U[h]||2<=||h||2. The reference may grow sublinearly. Assume all terms
in the integrations below are integrable, as verified for the finite
power references and decaying probes considered here. Put

    F=(cX+U_R).grad R-R,
    M=(2c+1)phi+(cX+U_R).grad phi,
    C=||phi grad R||2, H=||grad phi||infinity,
    I=integral F phi, D=||M||2+C.

Then every such exact solution satisfies

    |I| <= D ||h||2+H ||h||2^2.                         (1)

If H<=Hbar with Hbar>0, it follows that

    ||h||2 >= 2|I|/[D+sqrt(D^2+4Hbar|I|)].              (2)

A strict rational lower bound on the right side is therefore a necessary
L2 distance. Neither a failed optimization nor a large residual norm is
used as a nonexistence argument here.

## Weak argument and boundary terms

Subtract the reference equation, test against phi and integrate the terms
linear in h by parts. Since div U_R=0 and div(cX)=2c, the transport and
zeroth-order terms contribute -integral h M. The other linear term is
integral phi U[h].grad R. The nonlinear term is
-integral h U[h].grad phi. Cauchy-Schwarz and ||U[h]||2<=||h||2 give (1),
and solving the scalar quadratic gives (2). The sign of I is retained
in the computation; only the final inequality takes its absolute value.

Use compact cutoffs first. For the probes below phi=O(r^-3),
grad phi=O(r^-4), while R and U_R are O(r^gamma), gamma=1/c<1.
Then M and phi grad R are L2, h U[h] is L1, and the cutoff errors
vanish by Cauchy-Schwarz on escaping annuli. The reference pairing itself
is absolutely integrable because its slowest possible residual power is
at most gamma and gamma<1. Smooth S1 probes have no origin boundary term.
This justifies the weak calculation even though R need not be L2.

## Exact raw generators and polar fields

The candidate input is a finite list of rational coefficients with
ordinary generators

    r^(2m)(1+r^2)^(p_j-m) t^h,
    r^(2m)(1+r^2)^(p_j-m) t^w P_n(2t-1),
    t=r^2/(1+r^2), p_j=(3+1/c-j(1-1/c))/2,

each multiplied by cos(2m theta). Expanding the shifted Legendre polynomial
uses the exact formula

    P_n(2t-1)=sum_(k=0)^n (-1)^(n+k) binom(n,k)binom(n+k,k)t^k.

Combine equal (j,m,k) monomials rationally. This is the full potential;
no coefficient threshold is applied. Scaled denominators or explicit
independent powers are outside this input path and are rejected.

The previously audited polar differentiator gives

    R=r sum_(j,n) v^((j+1)delta/2) R_jn(t) sin(n theta),
    psi=r^2 sum_(j,n) v^((j+1)delta/2) S_jn(t) sin(n theta),
    v=1-t, delta=1-1/c, U_R=grad-perp psi.

All polynomials are exact rationals. Every apparent division by t is
performed only after its zero coefficients are checked. This supplies
origin values a0 and strain directly, and leading angular profiles from
the endpoint polynomials at t=1. Leading-profile equality with an audited
reference, together with T4-189, permits c-pinning only in that theorem's
stated correction chart. It does not grant an unrestricted free-c claim.

## Fixed probes and whole-plane integration

The probes are the frozen, already audited candidate007 mode-one and
mode-seven polynomials:

    phi=r(1+r^2)^(-2) P(t) sin(n theta), n in {1,7}.

Their exact rational coefficients and rational Hbar are copied without
retuning. A separate interval subdivision verifies H<=Hbar again.
In polar coordinates

    grad_r phi=v^2[(1-4t)P+2tvP'] sin(n theta),
    grad_theta phi=v^2 nP cos(n theta).

The maximum norm is bounded by v^2 times the larger absolute polynomial
coefficient at each radius. A finite dyadic interval cover and the
mean-value bound for each polynomial give the stated Hbar without a grid.

Angular orthogonality and sine/cosine products reduce I, ||M||2^2 and C^2
to finite sums of integrals

    integral_0^1 t(1-t)^b Q(t) dt.

Expand Q(1-v)=sum q_k v^k and use

    integral_0^1 (1-v)v^(b+k)dv=1/[(b+k+1)(b+k+2)],

only when b+k>-1. Coefficients and exponents are exact rationals;
2048-bit outward arithmetic encloses the signed sums. Every contributing
background angular mode is retained. The reference pairing is computed
both directly and by -integral R M; their enclosing intervals must agree.

## Evidence and limits

Freeze the input manifest, coefficient file and checksums, then bind them
to the newly built canonical representation. Store exact origin values,
all leading-profile comparisons, frozen probe hashes, integrability and
subdivision evidence, both signed pairings, norms and the strict rational
radius. No candidate is modified or published. An independently verified
positive radius excludes only balls smaller than that radius in the
specified canonical L2 class. Large radii alone do not rank the true
solution distances of different references.
