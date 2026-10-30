# A complete finite-algebra tail certificate for the dyadic Laplacian

## Exact statement

Let the rational campaign density and stream have the finite polar form specified in ../weighted_full_residual/PROOF.md. Let their exact residual be

    F=r sum_(ell,n) z^(ell delta/2) P_(ell,n)(t) sin(n theta),
    t=r^2/(1+r^2), z=1-t, delta=1-1/c,

with every coefficient polynomial formed from the complete nonlinear equation. For state131 the leading exponent is b=2/c-1=1-2delta. Define

    T_(d,k)P=(k-2dt)P+2t(1-t)P',
    K_(ell,n)=T_(ell delta/2,1)^2 P_(ell,n)-n^2 P_(ell,n).

Then the exact radial Laplacian is

    Delta F=r^-1 sum_(ell,n) z^(ell delta/2) K_(ell,n)(t)sin(n theta).   (1)

Replace t by1-z and group all coefficients by the rational exponent

    e=ell delta/2-delta+k.

Suppose all nonzero exponents satisfy e>=0, and write C_e(theta) for the combined finite angular vector at exponent e. Equation(1) becomes the exact identity

    r^(2-b) Delta F=t^delta sum_e z^e C_e(theta).          (2)

The leading vector C_0 equals b^2 E+E'', where E is the leading residual angular vector. Let D=||C_0||_(L2(circle))>0. For an integer J>=1, set R0=2^J, z0=1/(1+R0^2), t0=1-z0 and

    E_J=(1-t0^delta)D+sum_(e>0) z0^e ||C_e||_(L2(circle)).  (3)

If the exact/interval calculation proves E_J<=epsilon D,0<=epsilon<1, then for every r>=R0

    ||Delta F(r,.)||_(L2(circle)) >= (1-epsilon)D r^(b-2). (4)

All terms in(3) are present; this is a finite algebraic bound for the full residual, not a truncated asymptotic series.

## Proof

The polar Laplacian is r^-2((r partial_r)^2+partial_theta^2). Applying r partial_r to r z^d P(t) gives r z^d T_(d,1)P. This proves(1). Since r^(1-b)=r^(2delta)=(t/z)^delta, factoring r^(2-b) from(1) proves(2), with all coincident exponents and modes combined. The finite polynomial expansion is exact on0<z<1.

For r>=R0,0<z<=z0 and t0<=t<1. Every e>0 gives z^e<=z0^e. Subtract C_0 from(2), apply the triangle inequality in angular L2, and use t^delta<=1 and1-t^delta<=1-t0^delta. This gives error at most E_J and proves(4). The angular norm of a finite sine sum is sqrt(pi sum_n coefficient_n^2), so all coefficient sums are exact rationals and the remaining powers and square roots can be enclosed by ball arithmetic.

## From the complete tail to Y

The independently audited plateau inequality gives

    Y(F)^2>=sum_(j>=J) 2^(2(2-a)j)||Delta F||_(L2(2^j<r<2^(j+1)))^2.

For b<1 and a>1+b, set eta=a-1-b and

    K=(1-2^(2b-2))/(2-2b)>0.

Integrating(4) on each shell and summing its geometric series proves

    Y(F)>=(1-epsilon)D sqrt(K) 2^(-eta J)/sqrt(1-2^(-2eta)).             (5)

This is independent of the low weight radius Rw. It uses only density terms of Y, so no uncontrolled velocity estimate enters the residual lower bound.

For state131, the admissible formal interval is 2/c<a<1+1/c. The inverse lower bound in ../farfield_resolvent_floor/PROOF.md, if independently accepted, and the audited universal radius ceiling would require

    Y(F)<sqrt(8pi)(1+c-ca)^2/(1+a).                       (6)

A uniform contradiction follows if a certified interval cover proves the lower bound(5) greater than the right side of(6) on the full open interval. Endpoint and interval-cover details, when executed, are recorded separately in verification. No finite point scan alone establishes a uniform contradiction.

## Verification and scope

The script reconstructs the full residual from the potential, differentiates every component, groups every exponent exactly, and checks positivity of all nonzero exponents before applying(3). It records exact input hashes and all rational angular squared norms. Candidate-specific numerical conclusions remain OPEN until independent reproduction. The possible scheme exclusion also depends on independent review of the genuine inverse lower-bound theorem. Neither theorem would exclude other choices of high space or the existence of the intended profile.

## Uniform interval-cover criterion

Put a=2/c+delta x with0<x<1, so eta=delta x and beta_infinity=(c-1)(1-x). With epsilon=1/2 and E=D^2/pi, the square of(5) exceeds the square of the right side of(6) exactly when

    (E K/4)(1+2/c+delta x)^2
       >8(c-1)^4(1-x)^4(1-2^(-2delta x))2^(2J delta x).   (7)

All factors are nonnegative on[0,1]. On a rational cell[l,h], the left side is bounded below by its value at l. The right side is bounded above by using(1-l)^4 for its decreasing factor and h for both increasing exponential factors. Outward ball evaluation of these two explicit quantities, with positive lower endpoint of their difference on every cell, proves(7) on the entire closed interval. Checking all consecutive endpoints j/N,(j+1)/N gives a complete cover without any numerical sampling inference. The non-strict endpoints are included by continuity; the actual membership window is open.
