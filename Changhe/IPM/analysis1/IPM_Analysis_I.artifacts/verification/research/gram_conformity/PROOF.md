# Exact continuity and the diagnostic H1m section

## Statement and hypotheses

Fix L>0 and 0<k<1. For r=|X| put

    m(r)=(r/L)^3(1+r^2/L^2)^((k-3)/2),
    w(r)=m(r)^(-2)(1+r^2/L^2)^(-3/2).

Let X consist of locally integrable functions on R^2, modulo equality
almost everywhere, having a locally square integrable weak gradient and
finite value of the norm

    ||h||_X^2 = integral [h^2+r^2|grad h|^2] w(r) dX.

Assume h is C1 on finitely many open concentric annuli and extends C1
from each side to each finite positive interface circle. On sufficiently
small and sufficiently large radii, assume, uniformly in angle,

    |h|+r|grad h| <= C r^a                          near0,
    |h|+r|grad h| <= C r^b(1+log r)^q               near infinity,

where a>2, b<k+1/2 and q is a nonnegative integer; choose the large
radius greater than1. The derivatives in these assumptions are the
classical derivatives within pieces. The statement is:

1. h belongs to X if and only if its value traces agree on every
   interface. Matching first derivatives is unnecessary.
2. In particular, ideal finite combinations having exact continuous
   radial joins, central growth O(r^3), and exterior growth at most
   O(r^k(1+log r)) with the analogous gradient bounds belong to X.
   This includes the intended finite exponential-polynomial sections
   described below, under exact continuity at every piece boundary.
3. On D={h in X: h=x^2y a_h with a_h continuous near0}, define
   j(h)=a_h(0). Every level set {h in D:j(h)=c}, for any real c, is
   dense in D for the X norm. In particular j=0 does not define a
   closed constraint in this diagnostic norm. This is a statement
   about D with the inherited topology; no density of D in all X
   is asserted.

These are analytic statements, not certification of the actual floating
nullspace or matrix spectrum. Topic127 supplies the stated concentrated
central functions and the nonzero-jump test. The complete arguments needed
here are also given below.

## Proof of the continuity criterion

On each compact annulus w and r^2w are bounded above and below by positive
constants. On an interface r=R let [h]=h_out-h_in and nu be its outward
unit normal. Integration by parts on the adjacent annuli shows that the
weak gradient equals the piecewise gradient plus [h] nu times circle
measure. If every trace agrees, these boundary terms cancel. The
piecewise C1 gradient is locally square integrable and is the weak
gradient. First derivative jumps introduce no measure into this first
weak derivative.

Conversely, if a continuous jump trace b(theta) is nonzero, there is an
open angular arc on which it has a fixed nonzero sign. Choose a smooth
nonnegative phi supported in that arc, not identically zero, and a smooth
eta supported in(-1,1) with eta(0)=1. Test against

    F_d(r,theta)=nu(theta) phi(theta) eta((r-R)/d).

The singular pairing is R integral b phi dtheta, a nonzero constant.
The bounded piecewise-gradient pairing is O(d), while ||F_d||_L2 is
O(sqrt(d)). An L2 weak gradient would have pairing tending to0 by
Cauchy-Schwarz, a contradiction. Thus any nonzero value jump excludes X.

It remains to check the two ends, including the origin for a global weak
derivative. Near0, w is bounded by a constant times r^(-6). Hence the
norm integrand after angular integration is bounded by C r^(2a-5) dr.
This majorant is integrable for a>2. This is a sufficient growth
hypothesis, not a necessary condition on every member of X. The integration-by-parts boundary
term on the circle r=epsilon is O(epsilon^(a+1)) for a fixed smooth test,
and tends to0. Thus no distribution supported at0 is introduced.
Near infinity, w is bounded by a constant times r^(-2k-3), so the radial
integrand is at most

    C r^(2b-2k-2)(1+log r)^(2q) dr.

Since 2b-2k-2<-1, this is integrable. To see convergence directly, set
r=e^t: the integral becomes a polynomial in t times exp(-delta t),
where delta=2k+1-2b>0. Repeated integration by parts gives finite values
for each nonnegative integer power. These estimates prove1 and2.

## The intended radial pieces and the actual computation

For h=r^3 a(t,theta), t=log r, direct differentiation gives

    r partial_r h=r^3(3a+a_t),  partial_theta h=r^3 a_theta,

and therefore

    ||h||_X^2 = L^6 integral e^(2t)(1+e^(2t)/L^2)^(3/2-k)
                    [a^2+(3a+a_t)^2+a_theta^2] dt dtheta.       (1)

For a finite sum a=sum A_m(t) cos^2(theta) sin(theta) cos(2m theta),
all angular functions and their first derivatives are bounded. The
central pieces A_m proportional to e^(2j t), j>=0, give a>=3 in
statement2. The central integrability exponent in t is2+4j>0.
The exterior pieces A_m proportional to e^((k-3-d)t) times a polynomial
of degree at most1, with d>=0, give b=k-d<=k. The exterior exponential
factor in the energy is e^((-1-2d)t), multiplied by a polynomial of
degree at most2. This is integrable, including d=0 and the logarithmic
KP column. For example,

    integral_R^infinity r^(-2)(1+log(r/R))^2 dr = 5/R.          (2)

Finite exponential-polynomial pieces between the ends are bounded with
bounded first derivatives. Exact equality of their traces consequently
suffices. Finite internal spline breaks also count as interfaces in1.
It is insufficient to check only the two ends if the implemented internal
pieces have not been shown to match.

The frozen sources from127 describe the inner powers, compact middle
splines, sub-k outer powers, and k-order tail/KP/TAU terms in this pattern.
Their intended symbolic functions satisfy the endpoint estimates above.
Applying1 to an actual output additionally requires exact value matching
at every interface. The current floating nullspace only approximates the
constraint equations, and spline/cutoff polynomial conversion and discarded
small coefficients have not been proved exactly conforming. A nonzero
jump of arbitrarily small size is still excluded by1. A rigorous claim
could instead reconstruct continuous functions and control the difference
in a stated norm that is defined on both objects; no such reconstruction
or error bound is proved here.

Thus the currently reported singular values can be retained as floating
finite diagnostics. Neither their validity as rigorous X-section spectral
bounds nor continuum convergence follows from the continuity theorem.
The stronger final inverse space and operator estimates remain separate.

## Proof of the central-level-set assertion

Let p=x^2y and, for0<epsilon<=L, set

    b_epsilon=p(1-r^2/epsilon^2)_+^6.

These functions are C5 and compactly supported, and j(b_epsilon)=1.
Here is the norm bound used. With chi(s)=(1-s^2)^6 on[0,1], angular
integration gives pi/8 for (cos^2 theta sin theta)^2 and5pi/8 for its
derivative squared. Substituting r=epsilon s in(1) yields

    ||b_epsilon||_X^2
      = (pi/8)L^6 epsilon^2 integral_0^1
          s(1+(epsilon s/L)^2)^(3/2-k)
          [15chi^2+6s chi chi'+s^2 chi'^2] ds.

The bracket is6chi^2+(3chi+s chi')^2>=0 and the weight is<3.
The three polynomial integrals are1/26,-1/26,12/143, respectively
for s chi^2, s^2 chi chi', s^3 chi'^2. Their indicated combination
is123/286. Consequently

    ||b_epsilon||_X^2 <=(369pi/2288)L^6 epsilon^2<L^6 epsilon^2.

Topic127 independently checked these constants by two exact methods.
For any h in D and any c in R, put

    h_epsilon=h+(c-j(h)) b_epsilon.

Then j(h_epsilon)=c and

    ||h_epsilon-h||_X <= |c-j(h)| L^3 epsilon ->0.

This proves3. The level sets are proper and nonclosed in D: choose h
with j(h) different from c and apply this same sequence. No assumption
that D is dense in all X has been made. In particular there is no bounded
X-functional agreeing with j on D. This does not prevent testing a fixed
continuous reference direction in X, and it proves no near-kernel for
any operator. It imposes no obstruction on a stronger final norm in which
the central coefficient is controlled.

## Verification and scope

The proof is written before new computation. Two exact arithmetic methods
will verify the transformed energy exponents, quadratic form, and(2),
and will recheck the inherited127 hashes. No numerical lane code, matrix
assembly or SVD is executed. This result only resolves the functional
space interpretation of the diagnostic; no PDE endpoint is reached.
