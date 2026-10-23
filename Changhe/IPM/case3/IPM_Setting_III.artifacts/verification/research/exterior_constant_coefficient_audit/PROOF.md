# Exterior constant-coefficient constraints and changes of linear coordinates

Independent verifier reconstruction, 2026-10-21 UTC. The mathematical
argument was written before the supporting exact-arithmetic checker.
Frozen claim: verification/PROP364.md, SHA-256
731bcb24a267b18418d1e731177b1407012b92d2d593906a4735462e45c28dfa.

## Statement and dependencies

Let 0<p<1. Suppose rho is a locally integrable function on the plane
whose rescalings R^(-p) rho(R X) converge locally uniformly off zero
to a nonzero function F. Assume F is homogeneous of degree p,
C-infinity off zero, and |F(X)|<=C|X|^p. Let

    P(d)=sum_(j=m)^d P_j(d),

where each P_j is a homogeneous constant-coefficient differential
operator of order j, with complex coefficients and P_m nonzero.
There is no locally integrable sigma outside a compact set B such
that P(d)sigma=0 there distributionally and either of these conditions
holds:

(a) sup_(|X|=r)|rho(X)-sigma(X)|=o(r^p);
(b) |rho(X)-sigma(X)|<=C(1+|X|)^p outside B and
    R^(-p)(rho-sigma)(R X)->0 for almost every X as R tends to infinity.

The values of functions may be chosen as measurable representatives;
in (a) an essential supremum also suffices. No condition on their
signs is used. The conclusion excludes sigma=rho and approximations
of the stated types by finite sums of ridge functions
h_j(l_j.X+b_j), h_j locally integrable on the line and l_j nonzero.

For the IPM application, the previously independently checked
far-field results 3.6, 3.7, 3.23 give exactly these hypotheses with
p=1/c_l and F(0,1)=K nonzero. In particular smoothness off zero comes
from 3.23. The weaker Holder result by itself is not being used to
justify rapid Fourier decay. The primary origin, canonical inverse
and transport hypotheses enter through those far-field theorems.

We also verify the following extension of the finite-rank exclusion.
Suppose F is centrally odd, and let M be any invertible real two by
two matrix. Then rho(M(u,v)) cannot have finite separation rank on
v>0 outside a disc, even up to an error E with
R^(-p)E(R M(u,v))->0 for every (u,v) with v>0. This assertion needs
only that F is locally Holder of some order alpha>p off zero, with
the other far-field hypotheses above. It does not apply to nonlinear
coordinates such as (x/y,y).

We use elementary distributional Fourier inversion, the fact that
Fourier transform sends derivatives to multiplication by i xi, and
the finite order of a distribution on a compact set. The needed
point-support and smoothness consequences are proved below.

## Rescaling an exterior equation

Fix a compact Q not meeting zero and take R large enough that RQ
does not meet B. Set sigma_R(X)=R^(-p)sigma(R X).
In (a), every radius in RQ tends to infinity, so the error tends to
zero uniformly on Q after division by R^p. In (b) it is bounded on
Q by C(R^(-1)+|X|)^p and tends to zero almost everywhere. Dominated
convergence gives L1(Q) convergence. Thus in either case sigma_R
converges to F in distributions on the punctured plane.

For a test function phi supported in Q, the term of order j in the
original equation tested on phi(./R) equals

    R^(p+2-j) <P_j(d)sigma_R,phi>.

The factor R^2 is the Jacobian, R^p comes from the density, and
R^(-j) comes from differentiating the test function. Dividing the
sum by R^(p+2-m) gives

    <P_m(d)sigma_R,phi>
      =-sum_(j>m) R^(m-j)<sigma_R,P_j(-d)phi>.

Each pairing on the right converges and is bounded, whereas each
power R^(m-j) tends to zero. Passing to the limit proves
P_m(d)F=0 off zero. The lowest order is essential here. The highest
order would multiply the lower orders by diverging powers of R.
No derivatives of sigma_R need pointwise bounds.

## Removing a possible distribution at the origin

Because p>0, F extends as a locally integrable homogeneous tempered
distribution on the entire plane. Every order-m derivative is
homogeneous of degree p-m. Consequently u=P_m(d)F is supported at
zero and has this noninteger degree.

For completeness, a distribution u supported at zero is a finite
sum of derivatives of delta. Indeed, on a fixed compact neighborhood
its order is some integer N. If a test function and all of its
partial derivatives through order N vanish at zero, multiply it by
a cutoff supported in radius epsilon and equal to one near zero.
Taylor's theorem shows that every derivative of this product through
order N has supremum O(epsilon); the order bound implies its pairing
with u tends to zero. Since u is supported at zero, that pairing
equals the original one. Thus u depends only on the finite Taylor
jet through order N, which gives the claimed finite sum.

Under the test-function dilation phi_s(X)=phi(X/s), a derivative
of delta of order k pairs as s^(-k). A distribution homogeneous of
degree p-m pairs as s^(p-m+2). These exponents cannot agree for any
integer k because p is noninteger. Taking test functions with one
specified Taylor jet isolates each derivative of delta and forces
its coefficient to vanish. Therefore P_m(d)F=0 on the whole plane.
This argument includes m=0, when the conclusion is already immediate
from the nonzero scalar P_0.

## Fourier transform away from the origin

Choose a smooth radial eta equal to one near zero and equal to zero
outside radius two. The smooth annular function
chi(X)=eta(X)-eta(2X) satisfies
sum_(l in Z) chi(2^(-l)X)=1 for X nonzero. Hence

    F(X)=sum_l 2^(lp) (chi F)(2^(-l)X).

The identity holds in tempered distributions. Near zero the L1
sizes are O(2^(l(p+2))) and summable; at infinity polynomial growth
is absorbed by any Schwartz test function. There is therefore no
unmentioned point-supported term in this decomposition.

Since chi F is smooth and compactly supported, a=Fourier(chi F) is
Schwartz: multiplying its derivatives by powers of xi corresponds
to integrating derivatives of compactly supported smooth functions.
Fourier transformation of the preceding identity yields

    Fourier(F)(xi)=sum_l 2^(l(p+2)) a(2^l xi).

For any compact annulus r1<=|xi|<=r2 and derivative order |beta|,
the l-th differentiated term is bounded by
C 2^(l(p+2+|beta|)) as l tends to minus infinity. As l tends to plus
infinity its bound is C_M 2^(l(p+2+|beta|-M)) for any chosen M.
Both geometric series converge when M>p+2+|beta|. Thus the series
and all its derivatives converge uniformly on compact annuli and
represent a smooth function there, as well as the distributional
Fourier transform.

The transformed equation is P_m(i xi) Fourier(F)=0. A nonzero
complex polynomial has a zero set with empty interior on the real
plane. To see this, take a nonzero real or imaginary part after
expanding P_m(i xi); vanishing on an open rectangle would force all
its coefficients to vanish by applying the one-variable polynomial
identity first in one coordinate and then in the other.
Away from that zero set one can multiply the equation by the smooth
reciprocal to conclude Fourier(F)=0. This set is dense off zero.
Continuity of the Fourier function there now forces it to vanish
everywhere off zero. Its support is contained in {0}.

The point-support argument already proved implies that Fourier(F)
is a finite sum of delta derivatives. By Fourier inversion F is a
polynomial. A polynomial homogeneous of noninteger degree p is zero:
separate its finitely many integer-degree homogeneous parts and
compare their powers under dilation. This contradicts F nonzero and
proves the main assertion.

The smoothness and noninteger assumptions have a real role. A
homogeneous ridge |x|^p is annihilated by d_y but is not smooth at
points (0,y) with y nonzero. Homogeneous integer-degree polynomials
are smooth off zero and are annihilated by sufficiently high
constant-coefficient derivatives. Neither is a counterexample to
the stated theorem.

## Ridge sums

For l nonzero and v perpendicular to l, Fubini in coordinates along
l and v gives

    integral h(l.X+b) (v.grad)phi(X) dX=0.

Local integrability is sufficient because the support of phi is
compact. Thus v.grad annihilates this ridge distributionally.
For a finite sum, the product of the corresponding directional
derivatives annihilates every term; the factors commute. The product
is a nonzero polynomial differential operator, since none of its
linear factors is zero. The already proved theorem applies under
(a) or (b). Merely raywise errors without domination or local L1
control were not used and are not claimed to suffice here.

## Finite rank after an arbitrary invertible linear change

Write Ftilde(u,v)=F(M(u,v)). It is homogeneous, grows at most like
|(u,v)|^p, is Holder of order alpha>p locally off zero, and is odd
under (u,v)->(-u,-v). A supposed finite separation representation
of rank at most N forces every (N+1) by (N+1) rectangular evaluation
determinant of rho(R M(u_i,v_j))/R^p to vanish after subtracting the
raywise vanishing error. Passing to the limit gives the same zero
determinants for Ftilde. Hence

    V=span{Ftilde(.,v):v>0}

has dimension at most N. For clarity, if N+1 of these functions
were independent, there would be N+1 point evaluations forming an
invertible matrix, by elementary finite-dimensional duality.

Dilation T_s f(u)=f(su) maps V onto itself, since
Ftilde(su,v)=s^p Ftilde(u,v/s). It also maps
W={f-f(0):f in V} onto itself. A finite family of point evaluations
norms W. Near u=0 each f in a fixed basis satisfies an order-alpha
Holder estimate; finite dimensionality therefore gives
||T_s||<=C s^alpha for 0<s<=1. The growth bound gives
||T_(1/s)||<=C s^(-p). If W were nonzero, the identity
T_s T_(1/s)=I would give 1<=C^2 s^(alpha-p), a contradiction as
s tends to zero. Thus W=0.

It follows that Ftilde(u,v) is independent of u for v>0. By
homogeneity it equals C v^p there. Continuity at (1,0) gives
Ftilde(1,0)=0. The order-alpha Holder estimate at this nonzero point
implies |C|v^p<=L v^alpha, forcing C=0. Central oddness then gives
zero for v<0, and continuity gives zero on v=0 away from zero.
Invertibility of M contradicts F nonzero.

## Scope and verdict

The reconstructed theorem and the proposed linear-coordinate remark
are CONFIRMED under their explicit hypotheses. They exclude fixed
constant-coefficient linear constraints and finite separated shapes,
not the unrestricted nonlinear IPM problem. Variable-coefficient
angular operators are outside the argument. No principal YES or NO
endpoint follows.
