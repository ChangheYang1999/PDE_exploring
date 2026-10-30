# Independent audit of the scaled radial norm integrator

## Statement, notation and scope

Let a_1,...,a_s be distinct positive rational numbers, M_i nonnegative
integers, P a rational polynomial, and b a rational number greater than
-1. The integral

 J(P,b,M,a) = integral_0^1 v^b P(v) product_i(1+a_i v)^(-M_i) dv

converges absolutely. The exact reduction and outward arithmetic below
enclose this entire integral. They require neither a radial cutoff nor
spatial quadrature. A finite calibration suite checks implementations
of these identities. Passing that suite alone does not certify a norm
of a large candidate, its field reconstruction, a spectral bound or an
existence theorem.

For the field discussion fix c=4076476460239181/2251799813685248,
gamma=1/c, delta=1-gamma, v=1/(1+r^2), t=1-v and w=v^(delta/2).
A degree-d component has the following representation, with rational
polynomials P and finite Fourier modes T=sin(n theta) or cos(n theta):

 d even: r v^(d/2) sum w^ell P(t) T(theta)/product(1+a v)^N;
 d odd:  v^((d-1)/2) sum w^ell P(t) T(theta)/product(1+a v)^N.

The coefficient dictionaries must be combined exactly for each
(ell,T,n) before testing endpoint orders. The poles have a>0 and cannot
vanish on [0,1]. The norm conclusions stated here concern smooth fields
with these exact finite representations. A certificate for an actual
candidate additionally needs its immutable raw coefficients, complete
field identities, every contributing radial integral, outward endpoint
bounds and independent verification.

## A calibration domain defect

The frozen N3 test A includes the base exponent

 b_bad = -1/2 + 1824676646553933/4076476460239181 - 1
       = -8580076087609677/8152952920478362.

It satisfies b_bad+1=-427123167131315/8152952920478362<0 and b_bad>-2.
Consequently integral_0^1 v^b_bad/(1+a v)^i dv diverges to positive
infinity for every a>0 and every nonnegative integer i. Indeed its
integrand is at least (1+a)^(-i) v^b_bad, whose integral diverges.
The test loops over three scales, fifteen orders i=0,...,14, and six
shifts m=0,7,14,21,28,35. Thus 45 of its 810 requested moments are outside
the stated integral domain. All 270 moments in the third base class use
an inadmissible base I0. A finite overlap of analytically continued
hypergeometric expressions cannot establish convergence of the 45
moments. The 225 shifted moments have admissible final exponents; they
still require a convergent proof or correctly justified analytic
continuation, which is not the stated base-integral proof.

This does not refute the production accumulator. It asserts b>-1,
chooses b0=b-floor(b)-1 when b is nonintegral and b0=0 otherwise, and
sets m=b-b0. Thus -1<b0<=0 and m is a nonnegative integer. Its production
path satisfies the hypotheses of the recurrences below. For a repaired
calibration one may use delta-1/2 without the extra subtraction of 1.
The original source and failed domain interpretation are retained.

## Exact single-pole recurrences

Write J_a(b,i)=integral_0^1 v^b(1+a v)^(-i) dv for b>-1. The elementary
identity a v=(1+a v)-1 gives

 J_a(b+1,1) = (1/(b+1)-J_a(b,1))/a,
 J_a(b,i) = J_a(b,i-1)-a J_a(b+1,i).

Integrating the derivative of v^(b+1)(1+a v)^(-i), whose boundary value
at zero is zero because b+1>0, gives

 J_a(b+1,i+1) = ((b+1)J_a(b,i)-(1+a)^(-i))/(i a), i>=1.

Also J_a(b,0)=1/(b+1). With b=b0+m, -1<b0<=0 and integer m>=0,
these identities express every moment as R1+R2 I0(a,b0), with rational
R1,R2 and I0=J_a(b0,1). For i=1 induct on m using the first identity.
For i>=2,m>=1 the third displayed formula reduces both i and m. At
m=0 use the second identity and J_a(b0+1,i), which reduces to order i-1.
This proves termination and the exact representation by induction.

Euler's integral gives two equivalent expressions

 I0 = 2F1(1,b0+1;b0+2;-a)/(b0+1)
    = 2F1(1,1;b0+2;a/(1+a))/((1+a)(b0+1)).

Euler's integral applies since b0+1>0 and c-b=1>0. Pfaff's identity is
valid on the real path with 1+a>0. Independent outward evaluations of
both expressions must be finite and overlap. Their agreement checks
the special-function call, while Euler's integral supplies its meaning.
A precision-dependent cache must include the requested precision if
later calls are intended to gain accuracy; a wider valid cached ball
still remains an enclosure. The frozen production source includes the
precision in this cache key.

## Independent pole-order reduction

The N4 path uses a different recurrence. For k>=2, integration of the
derivative of v^(b+1)/(1+a v)^(k-1), followed by replacing a v with
(1+a v)-1, yields

 J_a(b,k) = ((1+a)^(1-k)-(b-k+2)J_a(b,k-1))/(k-1).

Its starting values are J_a(b,0)=1/(b+1) and the direct Euler 2F1
expression for J_a(b,1). This keeps the requested b fixed, whereas N3
reduces shifts m to a common b0. Comparing the two recurrences and the
direct Euler formula tests distinct exact arithmetic paths. All tested
integral exponents must satisfy b>-1 before either path is called.

## Several scales and polynomial numerators

For distinct a,b the rational identity

 1/((1+a v)(1+b v))
   = a/(a-b)/(1+a v)-b/(a-b)/(1+b v)

reduces products of pole powers to a finite sum of single-pole powers.
Repeated multiplication by one factor terminates because each local
reduction lowers one of the powers. N3 uses this recurrence for the
reciprocal common denominator and then expands P in monomials.
N4 instead divides P by the full denominator, obtains each principal
part from the truncated Taylor expansion at v=-1/a, and multiplies
back the proposed decomposition by the full denominator. Equality of
the resulting rational polynomials is an exact verification of the
entire partial fraction identity. This includes polynomial quotients
when deg(P) is at least the denominator degree.

Each monomial integral is R1+R2 I0. Bringing the rational coefficients
to common integer denominators and taking exact integer dot products
preserves this identity, including cancellation between different
monomials and scales. Sum all rational contributions exactly before
outward evaluation of each R2 I0. Every resulting ball must be finite;
its reported relative accuracy is a numerical quality diagnostic, not
an additional mathematical hypothesis. A broad ball is inconclusive
for a strict numerical inequality.

## Field differentiation and norm measure

Let K_N(t)=(1+a(1-t))^(-N). Since dK_N/dt=Na K_(N+1) and
dt/dr=2r v^2, one radial Cartesian derivative contributes
2Na t v P in even degree and 2Na v P in odd degree, with N increased
by one. The remaining derivative terms follow from the product rule
on the displayed radial factors and from differentiating sine and
cosine. Their angular factors are obtained from the usual exact
product-to-sum identities. Combining equal modes by a common positive
denominator preserves the function and its endpoint order.

For a polynomial P write P(t)=v^q P2(t), P2(1) nonzero. In a squared
weighted norm with weight squared v^A t^B, an ordered pair of terms has
radial exponent

 b=d-3+(ell+ell')delta/2+q+q'+A.

The remaining numerator is P2 P2' times t for even d and times t^B
for either parity. This follows from r dr=dt/(2v^2), r^2=t/v and the
radial prefactors above. Angular orthogonality contributes pi, except
cos(0)^2 contributes 2pi; cross terms with distinct row indices carry
factor 2. The measure contributes 1/2. For all Cartesian derivatives
of order d the component with nx x derivatives has multiplicity
binomial(d,nx). These account for every normalization in normsq_t.

For each diagonal term integrability requires
 d-3+ell delta+2q+A>-1. If every diagonal passes, every cross exponent
is their arithmetic mean and also passes. If a diagonal fails, a
nonzero divergent endpoint cannot be canceled by another branch when
(ell-ell')delta/2 is never an integer for distinct ell. Within a branch
and angular mode the complete rational coefficients must already have
been combined. Orthogonal angular modes and positive derivative
multiplicities cannot cancel a divergence. These assumptions are
checked before calling an infinite-norm verdict.

## Fractional weight remainder

For P2 the additional factor is (1+3t)^(4/5). Write it as
(5/2)^(4/5)(1+z)^(4/5), z=(3t-3/2)/(5/2), so |z|<=3/5.
For a Taylor polynomial G_N through N>=1, the ratio of consecutive
absolute binomial coefficients beyond N is less than one. Hence

 |(1+z)^(4/5)-G_N(t)|
 <= |binomial(4/5,N+1)|(3/5)^(N+1)/(1-3/5)=epsilon.

Integrate against the nonnegative squared field times its positive
radial weight. If S is its integral without this fractional factor and
T uses G_N, then the desired squared norm lies between
pi (5/2)^(4/5)(T-epsilon S) and
pi (5/2)^(4/5)(T+epsilon S), with the normalization above.
Individual branch cross integrals may have either sign; the error
bound uses the assembled nonnegative squared field, never separate
absolute values or an assumption that each cross term is positive.
Outward arithmetic encloses both bounds. Clamp a negative lower bound
to zero before taking square roots. Require a finite nonnegative upper
bound, and retain the containing square balls when writing decimal
summaries.

## Dependencies and verification

The independent N4 rational_pole_moments proof and code supply exact
Taylor decomposition and the pole-order recurrence. The frozen N3
modules supply the implementation under review. Their hashes and this
proof's hash are fixed before running the local calibration checker.
Only copies inside the N4 numerical auditor are executed. Exact domain checks, full
polynomial replays, recurrence/direct-form comparisons and finite
ball accuracy are recorded individually. Production candidate norms
remain OPEN until the actual candidate and complete output are audited.
No Lean build, server, JavaScript, GPU or remote computation is used.
