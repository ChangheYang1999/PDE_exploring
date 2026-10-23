# A density-moment canonical inverse for the smooth verifier basis

Independent derivation, 2026-10-21 UTC, written before implementation.
This is a numerical-method result, not an existence argument.

## Statement and basis

Let 0<p<1, alpha=(1-p)/2, L>0, and N>=0, M>=1 integers. For
0<=k<M and 0<=j<=N consider the smooth Cartesian density basis

    rho_(k,j)(x,y)=y w sigma^k T_j(1-2w) cos(2k theta),
    r=|X|, w=(1+(r/L)^2)^(-alpha),
    sigma=r^2/(L^2+r^2).

Here T_j is the degree-j Chebyshev polynomial. At the origin the
formula is interpreted through
sigma^k cos(2k theta)=Re((x+i y)^(2k))/(L^2+r^2)^k.
Every finite combination is smooth on the plane, has the required
parities, and satisfies the density/first-derivative growth bound
with exponent p. This representation was developed independently
of the numerics lane.

We derive full-plane formulas for its canonical velocity using only
radial moments of the density. The upper moments reduce to finite
weighted integrals of Chebyshev polynomials and can be integrated
exactly in exact arithmetic by Gaussian quadrature. The lower
moments are convergent weighted integrals on [0,1], for which
quadrature convergence must be measured. The formulas do not impose
a finite physical boundary or a free harmonic strain. They are
independent of the existing Cartesian singular integral and of the
separately implemented multiprecision source primitives.

## Density modes and Green function

Write rho=r sum_(n odd) h_n(r) sin(n theta). The identity
sin(theta)cos(2k theta)=[sin((2k+1)theta)-sin((2k-1)theta)]/2
shows that, for k>=1, a basis element contributes
+w sigma^k T_j/2 to h_(2k+1) and its negative to h_(2k-1).
For k=0 it contributes w T_j to h_1.

For each even m>=2 define

    A_m=r^(-m-2) integral_0^r s^(m+1) h_(m-1)(s) ds,
    B_m=r^(m-2) integral_r^infinity s^(1-m) h_(m+1)(s) ds.

The moments converge. Near zero, smoothness gives h_n=O(r^(n-1));
at infinity h_n=O(r^(p-1)). In particular the tail exponent is
p-m<-1. Set

    psi_m/r^2=(B_m-A_m)/2,
    psi_m'/r=[m(A_m+B_m)-h_(m-1)-h_(m+1)]/2.          (1)

These give psi=sum_m psi_m sin(m theta), with

    U_r/r=-sum_m m(B_m-A_m) cos(m theta)/2,
    U_theta/r=sum_m [m(A_m+B_m)-h_(m-1)-h_(m+1)]
                                      sin(m theta)/2.  (2)

To prove (1), the x derivative of r h_n sin(n theta) contributes
[dot h_n+(1-n)h_n]/2 to mode n+1 and
[dot h_n+(1+n)h_n]/2 to mode n-1, where dot=r d/dr.
The canonical Poisson Green formula for source G_m is

    psi_m/r^2=(1/(2m))[
      r^(-m-2) integral_0^r s^(m+1)G_m(s)ds
      +r^(m-2) integral_r^infinity s^(1-m)G_m(s)ds].

In its lower integral, integration by parts gives
[h_(m-1)+h_(m+1)]/2-m A_m. In its upper integral it gives
-[h_(m-1)+h_(m+1)]/2+m B_m. The boundary terms at zero
and infinity vanish by the powers just stated. Adding gives (1).
Also dot A_m=h_(m-1)-(m+2)A_m and
 dot B_m=(m-2)B_m-h_(m+1); differentiating the first line
of (1) proves the second. Thus the velocity uses no numerical
radial differentiation.

The Green solution is smooth at zero. In particular the highest
relevant source mode is 2M and the sums are finite. At infinity
A_m,B_m=O(r^(p-1)), so U=O(r^p)=o(r). A difference of two
parity-preserving solutions of the div-curl equations with sublinear
velocity is a harmonic vector field. Interior gradient estimates
on expanding discs make it constant, and the parities remove that
constant. Therefore (1) is the canonical inverse and adds no strain.

## Upper moments in the basis

Put q=r/L, h=m/2. An upper density mode m+1 receives contributions
only from k=h and k=h+1, when those indices lie below M. Define
B_(m,k,j) by replacing h_(m+1) in B_m by w sigma^k T_j(1-2w),
without the angular coefficient. Let d=k-h, so d is zero or one,
and beta=(h-1)/alpha. Direct substitution u=w(s) gives

    ds/s=-du/[2 alpha u(1-u^(1/alpha))],

and consequently

    B_(m,k,j)=sigma^(h-1) w/(2 alpha)
      sum_(e=0)^d (-1)^e binomial(d,e) w^(e/alpha)
          I_(beta+e/alpha,j)(w),                       (3)
    I_(b,j)(w)=integral_0^1 v^b T_j(1-2wv)dv.

For example, before scaling u=w v the upper moment is
q^(m-2)/(2alpha) times the integral from zero to w of
u^beta(1-u^(1/alpha))^d T_j(1-2u)du.
Using q^(m-2)=sigma^(h-1)w^(-beta) proves (3) with every
power of L cancelled. This also checks the lowest case m=2.

Since b>=0, I is an integrable positive-weight polynomial integral.
An n-node Gauss-Jacobi rule for weight v^b on [0,1] integrates
it exactly in exact arithmetic whenever 2n-1>=N. Numerical root
and weight errors remain floating-point errors and must be checked.
Normalizing transformed weights to sum 1/(b+1) avoids an
unnecessary explicit factor 2^(-b-1), but does not prove stability
for unbounded b. An implementation may reject excessive b rather
than silently returning invalid weights.

## Lower moments in two charts

The lower mode m-1 receives k=h-1 (coefficient1 for h=1,
otherwise1/2) and k=h (coefficient-1/2), when present.
The unsigned basis moment is

    A_(m,k,j)=integral_0^1 u^(m+1)
          w(qu) sigma(qu)^k T_j(1-2w(qu))du.           (4)

For q<1, this equals

    integral_0^1 u^(m+1+2k)
        [q^2/(1+q^2u^2)]^k (1+q^2u^2)^(-alpha)
        T_j(1-2w(qu))du.                              (5)

For q>=1 use w(qu)=(qu)^(-2alpha)sigma(qu)^alpha,
which gives

    q^(-2alpha) integral_0^1 u^(m+p)
        sigma(qu)^(alpha+k) T_j(1-2w(qu))du.           (6)

The first chart avoids a large factor q^(-2alpha) at tiny q;
the second factors the far-field power and has a bounded remaining
integrand. Both weights have exponent greater than -1. Gaussian
quadrature is convergent for these continuous weighted integrands,
but the rates are not uniform in q,N,M. In particular a transition
near u=1/q can require refinement. No finite quadrature order is
certified by this derivation alone.

As an independent manufactured case, m=2,k=j=0 gives

    A=1/(2q^4) [((1+q^2)^(2-alpha)-1)/(2-alpha)
                  -((1+q^2)^(1-alpha)-1)/(1-alpha)].  (7)

It follows by substituting v=1+q^2u^2 in (4). Its removable
cancellation at q=0 can be resolved by multiprecision or series.
For this radial density all B_m vanish and only A_2 survives.

## Composite lower quadrature without truncation

For q>=1 choose J=ceil(log_2 q), a=2^(-J), so 1/2<qa<=1,
with J=0 permitted at q=1. Partition [a,1] into the J dyadic
intervals [2^(-j),2^(-j+1)], j=1,...,J. Apply ordinary
Gauss-Legendre quadrature to (6) on each interval, including the
weight u^(m+p) in the sampled integrand. The omitted interval is
not discarded. Its exact contribution to (4) is

    integral_0^a u^(m+1) w(qu) sigma(qu)^k T_j(...)du
           =a^(m+2) A_(m,k,j)(qa).                   (8)

Evaluate this last moment by the small chart (5). This is an exact
partition identity before numerical quadrature, with no physical
or radial truncation. On each nonzero panel qu varies by a factor
two, so the transition qu=1 is resolved without asking a single
rule to see an arbitrarily thin interval near u=0. This statement
explains a useful mesh choice; it is not a uniform error estimate
in N,M,q. All quadrature weights are positive. Underflow of an
extremely small tail in floating-point arithmetic still requires
an error assessment, although the algorithm never drops it by
mathematical definition. Numerical refinement is to compare panel
orders separately from upper-moment orders.

## Verification obligations and scope

Before solver use, compare (3)-(6) across lower quadrature orders,
check (7) and the associated closed stream with multiprecision,
compare a nonradial coefficient vector against the separate
source-primitive inverse and the direct Cartesian integral, and
verify the center strain without imposing its target. Keep all
failures and any repaired formulas. Test moderate, very small and
large radii, symmetry axes, and a change of L.

A solver using these formulas retains analytic Cartesian density
derivatives. Its validation still uses separate Cartesian and
multiprecision inverses. A finite basis cannot provide an exact
nontrivial finite-angular IPM profile; no sampled residual or
quadrature agreement is a proof of smooth-profile existence.
