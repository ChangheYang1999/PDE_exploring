# The canonical Poisson inverse is not bounded by a half-line polynomial norm

Status: PROVED. Independent theory-part review at 2026-10-31T07:00Z confirmed the complete argument; closure recorded in V162. This is a general-input operator obstruction, not a conclusion about the generated nonlinear sequence.

## Statement and notation

Fix a reduced rational delta=a/b in(0,1), let g=gcd(a,2), mu_*=g/b, and set P_n=2-n delta. Let T be any real number and eta>0. For a polynomial in t with finite angular sine support, define

    ||H||_(eta,T) = sup_(t>=T) exp(-eta(t-T)) ||H(t,theta)||_(angular l1).

Let T_n be the canonical polynomial Poisson map at order n, with every resonant stream constant set to zero. There is no constant C, independent of n, such that

    ||T_n F||_(eta,T) <= C ||F||_(eta,T)

for all admissible polynomial inputs. This remains false with the restrictions

    maximum density frequency <=2n-1,
    deg_t F <= max(0,floor((n-1)/q_0)-epsilon),
    q_0=2b/g, epsilon=1 if a/g=1 and epsilon=0 otherwise.

More precisely, for every integer k>=1 there is an admissible order n and a single density harmonic for which the ratio is at least

    (1+2eta/mu_*)^k / [2e mu_*(k+1)].                 (1)

Thus the failure holds for every eta>0, however small, and every exterior threshold T.

## Polynomial family and its half-line bound

Define the degree-k polynomial

    L_k(x)=sum_(j=0)^k binom(k,j)(-x)^j/j!.

Its elementary generating identity is

    sum_(k>=0) L_k(x) z^k = exp(-xz/(1-z))/(1-z), |z|<1.    (2)

To verify(2), interchange the absolutely convergent sums near z=0 and use sum_(k>=j) binom(k,j)z^k=z^j/(1-z)^(j+1). Analytic continuation in the unit disc then gives the identity throughout that disc.

For x>=0 and |z|=r<1,

    Re(z/(1-z)) >= -r/(1+r).

This follows by writing z=r exp(i phi); the expression is increasing in cos(phi), with its minimum at cos(phi)=-1. Cauchy's coefficient bound applied to(2) gives

    |L_k(x)| <= r^(-k)/(1-r) exp(xr/(1+r)).

For k>=1 choose r=k/(k+1). Since r/(1+r)<1/2 and (1+1/k)^k<=e,

    exp(-x/2)|L_k(x)| <= e(k+1), x>=0.                (3)

Put p_k(t)=L_k(2eta(t-T)). Then(3) proves

    sup_(t>=T) exp(-eta(t-T))|p_k(t)| <= e(k+1).       (4)

No estimate of p_k on t<T is used in this bound.

## Canonical inverse at the boundary

For any mu>0 the unique polynomial solution of(D+mu)y=p is

    y(t)=sum_(j>=0) (-1)^j p^(j)(t)/mu^(j+1),

where the sum terminates. Equivalently,

    y(t)=integral_0^infinity exp(-mu u)p(t-u) du.      (5)

The integral converges because p is a polynomial, and integration by parts proves(D+mu)y=p. Uniqueness follows because a nonzero multiple of exp(-mu t) is not a polynomial.

For p=p_k, direct evaluation at t=T gives

    p_k^(j)(T)=binom(k,j)(-2eta)^j,
    y(T)=mu^(-1) sum_(j=0)^k binom(k,j)(2eta/mu)^j
        =mu^(-1)(1+2eta/mu)^k.                       (6)

Thus the canonical polynomial inverse samples a quantity exponentially larger than the bound(4).

## Embedding in admissible Poisson inputs

The congruence an=-g modulo2b has arbitrarily large positive solutions. For such a solution set

    m=(an+g)/b-2.

For sufficiently large n, m is a positive even integer, m-1<=2n-1, and P_n+m=mu_*. The admissible degree bound tends to infinity along this progression, so choose n large enough to permit degree k. Use

    F(t,theta)=p_k(t) sin((m-1)theta).

At output frequency m, the factored Poisson formula is exactly

    [sin(m theta)] T_n F = -1/2 (D+mu_*)^(-1)p_k.

There is no second density coefficient in this output channel. The mode is nonresonant, so the canonical constant convention does not alter it. The angular l1 norm of the output at T is at least the modulus of this coefficient. Dividing(6) by(4) proves(1). Since its numerator grows exponentially in k and its denominator only linearly, no uniform C exists.

## What harmonic freedom changes

For a scalar positive shift mu>0, the half-line solution with y(T)=0 is

    y_0(t)=integral_T^t exp(-mu(t-s))p(s) ds.

For t>=T it satisfies

    ||y_0||_(eta,T) <= ||p||_(eta,T)/(mu+eta).

Indeed multiply the integral estimate by exp(-eta(t-T)) and integrate exp(-(mu+eta)(t-s)). The canonical polynomial solution differs by

    y_can(t)-y_0(t)=y_can(T)exp(-mu(t-T)).

For the Poisson factor mu=P_n+m, multiplying this term by r^(P_n) yields a constant times r^(-m), a homogeneous exterior harmonic stream mode. Hence permitting a suitable harmonic term removes this scalar half-line obstruction. Such a term generally lies outside the prescribed polynomial-in-log-r coefficient at the fixed radial exponent. This observation does not prove convergence for any nonlinear choice of harmonic data.

For comparison, a negative shift mu=-nu<0 has the canonical solution

    y(t)=-integral_0^infinity exp(-nu u)p(t+u) du.

If 0<eta<nu, it obeys the half-line bound ||y||_(eta,T)<=||p||_(eta,T)/(nu-eta), because it only samples t+u>=T. This proves the claimed distinction between the two signs without imposing values below T.

## Dependencies and scope

The factored Poisson inverse and degree bounds are derived in topics10 and17. The elementary congruence is also used in topic89. All other identities and estimates are proved above. The norm here has a fixed eta; it is an auxiliary norm on log-polynomial coefficients, not the order-dependent radial weight of the complete far-field series. The examples are arbitrary admissible inputs, not asserted to be generated by the stationary recurrence. No convergence or divergence conclusion for that generated sequence follows.
