# Independent acceptance of reference compatibility and the actual021 difference

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248, delta=1-1/c. Let chi and
chi' be two finite, exact rational sums of the campaign generators

    (1+r^2)^(2-ell delta/2) t^m tau_R^w (1-tau_R)^q
        P_n(2 tau_R-1) cos(2m theta),
    t=r^2/(1+r^2), tau_R=r^2/(R^2+r^2), ell=j+1,

where m,j,w,n,q are nonnegative integers, R belongs to{1,10,25,50,100},
and P_n is the ordinary Legendre polynomial. Monomials have n=q=0,R=1;
ordinary shifted Legendre terms have q=0,R=1. Amplitudes and c are exact
rationals. Write rho=-partial_y Delta chi and
u=(-chi_xyy,chi_xxy), and likewise rho',u' for chi'. The generator
formula is part of the hypothesis and is bound to the raw JSON. A list
of floating coefficients or samples does not meet it.

Suppose the complete leading angular potential coefficients agree for
each ell=1,2,3,4. Explicitly, for every nonnegative integer m and each
such ell, the sums of amplitudes over all generators with j=ell-1,
that m and q=0 are equal. Missing coefficients mean exactly zero.
Call this hypothesis(P). It is a stronger sufficient test than matching
just the four nonintegrable density sectors.

Then g=rho'-rho and V=u'-u are smooth, real functions with

    partial^alpha g, partial^alpha V=O(r^(1-5delta-|alpha|))

for every fixed multi-index alpha. In particular g belongs to every
integer H^k(R^2), V belongs to L2(R^2), and X.grad g belongs to L2.
The density g has the S1 parity: even in x and odd in y. The canonical
L2 velocity U[g]=(-R1 R2 g,R1^2 g), with Riesz symbol
+i xi_j/|xi|, equals V. Thus these references satisfy hypothesis(S)
of R1-038 for the common correction class C of all real S1 L2 functions,
with the stationary equations interpreted as distributions below.
Membership in a more restrictive class is not inferred from(P) alone.

The exact radial integration procedure below encloses ||g||2 over the
whole plane when its exact endpoint and positive denominator checks pass.
Given an independently accepted strict parent weak-distance bound d>0,
a certified ||g||2<=tau, and an L2 ceiling b with tau<=d-b, no stationary
correction to rho' in that ceiling exists under the parent weak theorem's
background and canonical velocity hypotheses. This is a necessary-test
exclusion. The procedure constructs no solution or inverse. If the norm
comparison fails, it supplies no exclusion by this rule.

No actual successor is covered until its immutable raw input, prefix,
full fields, integration record and accepted parent evidence are bound.

## Smoothness and the complete tail cancellation

Each t^m cos(2m theta) equals the homogeneous harmonic polynomial
Re(x+iy)^(2m) divided by(1+r^2)^m. Every remaining factor is smooth on
the plane: the denominator R^2+r^2 is positive, and all its powers
are integral or powers of the positive1+r^2. Thus the potential, density
and explicit velocity are smooth. The stated parity follows by reflection
of the even harmonic modes and three Cartesian derivatives.

For r larger than every R and1, set z=r^-2. Each generator has a
convergent power series in z times r^(4-ell delta) cos(2m theta).
Its leading coefficient at z^0 is1 when q=0 and0 when q>0: t and
tau_R tend to1, P_n(1)=1, and1-tau_R has order z. All higher terms
lower the radial exponent by even integers. The series converges in a
fixed neighborhood of z=0 and can be differentiated any finite number
of times there. Finite angular sums preserve uniform angular derivative
bounds. Therefore subtraction under(P) cancels the leading potential
terms for ell<=4, including their Cartesian derivatives.

The remaining potential exponents are at most

    max(4-5delta, 2-delta)=4-5delta,

because the exact delta is positive and below1/2. Three derivatives
give the stated bound1-5delta for g and V; higher derivatives lower it
by their order. The exact delta is also above2/5, so1-5delta<-1.
In two dimensions integral_R^infinity r^(2(1-5delta)+1)dr converges.
Local smoothness then proves all the stated L2 and Sobolev assertions.
Multiplication of a first derivative by X restores the same decay and
proves the drift assertion. The constants can depend on the finite
input pair; no uniform estimate over all generator amplitudes is claimed.

This proof also shows why matching only a finite list without a complete
finite-generator representation or remainder argument would be inadequate.
For the present representation all omitted density sectors have exponents
1-ell delta-2k with either ell>=5 or k>=1, strictly below-1.

## Canonical velocity and distributional compatibility

The explicit difference fields obey, by commuting smooth derivatives,

    Delta V1=partial_xy g,   Delta V2=-partial_xx g,
    div V=0.

The L2 multiplier U[g] obeys the same Poisson equations. Its Fourier
symbols are xi_x xi_y/|xi|^2 and-xi_x^2/|xi|^2, respectively, so
||U[g]||2<=||g||2 and div U[g]=0. Hence V-U[g] is an L2 harmonic
vector field. Fourier transformation gives |xi|^2 times its transform
zero. Its L2 transform is supported at the singleton{0}, a null set,
so it vanishes. Thus V=U[g] exactly. No pointwise or tail gauge choice
is silently substituted for this global identity.

For C equal to all real S1 L2 functions define

    F_rho(h)=div((cX+u)(rho+h))+div(U[h](rho+h))
                 -(2c+1)(rho+h).

This equals the intended stationary equation because div u=div U[h]=0.
Every product defines a distribution locally. The smooth backgrounds
and X are bounded on compact sets, and h,U[h] are locally L2, so
h U[h] is locally L1. Background growth at infinity does not obstruct
these local distributional definitions. Linearity of U and V=U[g] give
F_(rho')(h)=F_rho(g+h). The same c, common vector space C containing g,
and this identity establish all of(S) for this choice of C. Restricting
to a stronger admissible correction class needs its own stability check;
for an exclusion it is enough that it is a subset of this weak class
with its stated L2 embedding and the same equation.

Let S(rho)={h in C:F_rho(h)=0}. Then S(rho')=S(rho)-g, and the two
sets are simultaneously empty. For nonempty sets, the triangle inequality
and infimum give

    dist(rho)-||g||2 <= dist(rho') <= dist(rho)+||g||2,
    dist(rho)=inf_(h in S(rho))||h||2.

These two inequalities also hold in the extended-real sense for empty
sets. An absolute difference of two infinite distances is not used.
If dist(rho)>d and ||g||2<=tau<=d-b, then dist(rho')>b. This proves
the screening conclusion without assuming attainment of either infimum.
It is the same argument as Opus T1 R1-038(a), independently audited in
T4-379. Their other endpoint-budget assertions are not needed here.

## Exact difference fields

Subtract the two exact generator lists by their complete(m,j,spec) keys,
without rounding. Exact zero coefficients may be removed. Check the
common c, every generator's supported form, and all(P) coefficients
before any norm interpretation. The derivative routine forms the raw
potential's third Cartesian derivatives and divides out their exact
origin factor, giving

    g=r sum_(ell,n) v^(ell delta/2) A_(ell,n)(t) sin(n theta),
    v=1-t,

where n is positive odd and each A is an exact rational function. Its
denominator is a product of positive factors1+(R^2-1)v. These are
1+99v,1+624v,1+2499v,1+9999v for nontrivial scales. Every exact division
by t is checked. The same construction gives V. Under(P), each retained
A_(ell,n)(1) is exactly zero for ell<=4; this is checked for density
and both explicit velocity fields as a separate consistency test.

Exact rational coordinate Taylor jets of the original difference
potential provide independent evaluations of g,V. Such finite point
checks bind the implementation to the input; the complete derivative
identity, rather than the point samples, gives the global fields.
Source hashes and complete rational field fingerprints are retained.

## Full-plane norm and outward evaluation

Orthogonality on the full circle gives
int_0^(2pi) sin(n theta)sin(m theta)dtheta=pi for n=m>0 and0 otherwise.
The radial measure is r dr=dt/(2v^2). Thus

    ||g||2^2=(pi/2) sum_L integral_0^1
        t v^(L delta/2-3) Q_L(t)dt,
    Q_L=sum_(ell+ell'=L,n) A_(ell,n) A_(ell',n).

The sum contains every ordered pair, including cross terms between
fractional branches. Form each Q_L exactly before integrating. Individual
Q_L may have either sign; only the complete squared density is nonnegative.
Changing variable from t to v yields a rational numerator N_L(v)
divided by positive D_L(v). Strip its exact zero order k_L at v=0
and set b_L=L delta/2-3+k_L. Check b_L>-1 for every nonzero group.
The endpoint at v=1 has no singular denominator. These exact checks
justify integration term by term over the complete interval[0,1].
No finite radial cutoff or angular quadrature is used.

For each rational group use exact polynomial division and partial
fractions

    N_L/D_L=P(v)+sum_(a,k) c_(a,k)/(1+a v)^k,

replaying the full identity after multiplying by D_L. Since b>-1 and
a>0, the pole primitive equals Euler's convergent integral

    J_k(b,a)=integral_0^1 v^b/(1+a v)^k dv
           =2F1(k,b+1;b+2;-a)/(b+1).

For k=0 it is1/(b+1). The implementation evaluates J_1 with outward
ball arithmetic and obtains higher k from

    (k-1)J_k=(1+a)^(1-k)-(b-k+2)J_(k-1).

This follows by integrating the derivative of v^(b+1)/(1+a v)^(k-1).
The boundary at0 vanishes by b>-1. Polynomial terms integrate exactly
to1/(b+j+1). Every group records its exponent, zero order, complete
numerator fingerprint, denominator powers, exact partial-fraction replay,
outward primitive ball and resulting accuracy. Addition and square root
remain outward. If cancellation prevents a finite positive squared norm
ball, the calculation is OPEN at that precision; a midpoint is not used
as a bound. A zero difference is handled by exact equality before this
positive-norm branch.

For an exclusion, compare the certified squared norm upper bound with
(d-b)^2 using exact rational d,b, with d>=b. Passing a non-strict upper
comparison is sufficient because the parent distance bound is strict.
The record also gives a rational outward upper bound tau when available.
Different d or b require the corresponding accepted theorem and L2
embedding; no stored rounded decimal is silently used as an exact input.

## Dependencies, verification and scope

The exact radial class and Cartesian jet are calibrated in N4-291/305/308;
the complete Hessian reconstruction in N4-303 and norm partition304 give
independent actual-candidate checks of its linear field and integration
path. N4-302 checks admissible primitive domains, N4-305 a complete
synthetic residual fixture. These are dependencies and calibrations,
not acceptance of a new density difference. Each actual input pair must
have its own complete record and independent reproduction. The positive
pole integral soundness argument is in rational_pole_moments/PROOF.md.
The transfer step uses only R1-038(a), as accepted by T4-379.

Potential-prefix equality is a sufficient condition here. Failure of it
does not prove the density difference is non-L2, because a potential
kernel or density cancellation might require a weaker check. No condition
number, optimizer convergence, minimum in a span, inverse bound, or
existence result follows from this computation.

## Actual021-minus020 acceptance and scope

For the numerical application here, the parent is
C1-N1-020-legqs25p50-quot013, raw SHA256
 bddbd3120852a815cfe850635564cb09ab52a98ec596a4cce3b72c98cf04f7cf,
and the successor is C1-N1-021-heldin14-legqs25p50, raw SHA256
 c6ed292b9f7129ad236f8441140745ec6accc3918d477ca2268e55bf7efc85c8.
N4-313 supplies the complete Cartesian calculation and T4-393/394
supply an independent proof of(P) and a polar/direct-hypergeometric
calculation. The first path uses local Taylor partial fractions and a
recurrence in pole order. The second uses extended-Euclidean CRT and
individual direct hypergeometric values. Both exact partial-fraction
identities imply the displayed Euler integral, so independent complete
moments can be compared without a quadrature assumption.

The actual comparison checks all2286 coefficient differences, the
complete(P) sums, density and velocity endpoint cancellations, nine
Cartesian/polar values, all834 ordered angular products and14 whole-plane
integrals. Recompute the positive squared norm from the entire signed
group sum, its square root and its rational upper bound

 tau=3674626624859862044982741129/500000000000000000000000000000.

Compare the parent strict floor231921834680339/125000000000000000
with the accepted parent020 certificate. For the original graded
ceiling25/54684, conservative sharpw ceiling28496/10^10, and conservative
TB ceiling3793/10^9, the independently computed norm is larger than
each parent-floor-minus-ceiling allowance. This is failure of each
of these sufficient transfer comparisons. It does not establish a
nearby solution or invalidate any independent direct weak exclusion.
No optimal norm bound or strongest possible prefix condition is claimed.

The general theorem's independent proof is read in full and every
scope qualification is retained, including the weak correction class,
canonical velocity and extended-real empty-set case. The numerical
acceptance is recorded only after source hashes, exact scalar identities,
all individual enclosures, accuracy bounds and strict comparisons pass.
Publisher source is inspected as text and never executed. Point samples
are implementation checks; the exact reconstruction and integration
arguments above establish the whole-plane calculation.
