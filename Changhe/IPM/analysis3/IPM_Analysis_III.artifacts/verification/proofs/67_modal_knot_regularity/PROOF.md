# Finite regularity at the modal spline knots

## Statement and scope

Let rho be the exactly joined, normalized modal density of proof 04,
constructed from the original degree-seven spline data. Put
V=ell X+U[rho] and F=V.grad rho-rho. On the spline interval write

 rho(r,theta)=r^3 Phi(theta) a(log r,theta),
 Phi(theta)=cos(theta)^2 sin(theta),
 a(t,theta)=sum_(m=0)^259 s_m(t) cos(2m theta).

At an interior simple knot t_* define the exact one-sided jumps
j_m=s_m^(7)(t_*+)-s_m^(7)(t_*-), and
S(theta)=sum_m j_m cos(2m theta). Suppose some j_m with m>=1 is
nonzero. Let q(theta)=V_r(exp(t_*),theta)/exp(t_*), let
d=q(pi/2), and let gamma(t) be the continuous axis cofactor of F:

 gamma(t)=lim_(theta->pi/2) F(exp(t),theta)/(exp(3t) Phi(theta)).

Then F and its canonical remainder R=F-r^3 Phi gamma are not locally
H^(13/2) on every open arc of this knot circle. More precisely, each
nonempty open arc not contained in an axis contains a point where
this local Sobolev membership fails. At any such point they are
locally H^s for every s<13/2. They are piecewise analytic and C5 there,
with a nonzero jump in their sixth radial-logarithmic derivative.

The computation alongside this proof checks the nonzero-jump
hypothesis directly with rational arithmetic on the original NPZ.
No floating differentiation or value-sampling inference is used.

This refutes smoothness of the actual residual away from the origin.
A high target requiring ordinary or equivalent conormal H^N across
these arcs cannot contain this residual when N>=7. It does not
exclude a deliberately weaker target or a new smooth background.
No numerical residual norm or inverse assertion is made.

## Exact spline jump

For a degree-p spline with knot vector T and coefficients c, its
first derivative has degree p-1, knot vector T with the first and
last entries removed, and coefficients

 c'_i=p(c_(i+1)-c_i)/(T_(i+p+1)-T_(i+1)).

This identity follows by differentiating the Cox-de Boor recurrence
and cancelling adjacent terms. All denominators here are positive.
After seven repetitions the spline derivative is a degree-zero
spline on the distinct knots T_7,...,T_(n-8). Its coefficient on each
open interval is exactly the one-sided seventh derivative of s_m.
Adjacent coefficient subtraction therefore computes j_m exactly.
All stored doubles are interpreted as exact dyadic rationals.
The scalar normalization repair changes only the outer continuation
and leaves every interior spline coefficient unchanged.

## Velocity and residual across a knot

The spline is C6, and every mode is analytic on each open spline
span. The finite radial Green formulas show that V is C6 at an
interior knot and analytic on either side. One way to see the
regularity without a global singular-integral assertion is to use
the modal radial Poisson equation: its forcing is a linear
combination of s_m and s_m', hence C5; integrating the second-order
radial equation gives a C7 stream function. One spatial derivative
gives a C6 velocity. Angular differentiation preserves this finite
mode regularity.

In polar-logarithmic coordinates,

 F=q(t,theta) partial_t rho+v(t,theta) partial_theta rho-rho,
 q=V_r/r, v=V_theta/r.

Every term in the sixth t derivative has a continuous trace except
q partial_t^7 rho. The exact jumps are consequently

 [partial_t^6 F]=r_*^3 Phi(theta) q(theta) S(theta),
 [gamma^(6)]=d S(pi/2),
 [partial_t^6 R]=r_*^3 Phi(theta)
                    (q(theta) S(theta)-d S(pi/2)).             (1)

The axis identity in (1) can also be read from the exact axis row
of proof 46. The other axis-row coefficients involve at most six
continuous t derivatives and contribute no jump.

The radial component of V/r is a finite cosine polynomial in 2theta,
with nonzero constant Fourier coefficient ell. Thus q is a nonzero
polynomial in z=cos(2theta). Since one j_m for m>=1 is nonzero,
S is a nonconstant polynomial in z. Their product is nonconstant:
over the real polynomial ring its degree is deg(q)+deg(S)>=1.
In particular neither qS nor qS-dS(pi/2) vanishes identically.
A nonzero trigonometric polynomial has only finitely many zeros on
a compact period. Away from the axes Phi is nonzero. Hence both
jumps in (1) are nonzero on a nonempty part of every open arc.
The same argument shows that subtracting only the axis jet does
not remove the loss of regularity.

## Sobolev threshold of a jump

Use smooth local coordinates (u,v)=(t-t_*,theta-theta_*) around a
point where the relevant jump is nonzero. The Jacobian and its
inverse are smooth and bounded on a small rectangle. All derivatives
through order5 agree across u=0, while the sixth u derivative is
piecewise smooth with a jump bounded away from zero on a smaller
v interval. Such a function is not H^(1/2): its fractional seminorm
contains, for u>0 and u'<0, the integral of

 |g(u,v)-g(u',v')|^2 / ((u-u')^2+(v-v')^2)^(3/2).

Restrict |v-v'|<u+|u'| and sufficiently small u,|u'|. The numerator
is bounded below and integration in v' contributes a constant times
(u+|u'|)^(-2). The remaining positive integral
int_0^epsilon int_0^epsilon (u+w)^(-2) du dw diverges.
Thus the sixth derivative is not H^(1/2), so the original function
is not H^(13/2).

For every sigma<1/2 the corresponding cross-interface integral
has power (u+w)^(-1-2sigma) and is finite. The same-side seminorms
are finite by piecewise smoothness. Therefore the sixth derivatives
belong locally to H^sigma for sigma<1/2, and the original function
is locally H^s for s<13/2. Standard integer differentiation and
smooth coordinate change preserve these local conclusions.

## Consequence for a variable-order target

At a point with x and y nonzero, the fields x partial_x and
 y partial_y span the ordinary derivatives with smooth bounded
coefficients. Likewise scaled Cartesian derivatives are equivalent
to ordinary derivatives on a compact annulus. Requiring order N>=7
in any such local norm excludes the residual and also excludes its
canonical axis-jet remainder at the nonzero-jump points above.
An order function assigning high order to an open angular sector
across the selected knot must respect this finite regularity.

The mapping spaces of topics57 and63 remain valid spaces for
corrections. Their mapping bounds did not assert that the actual
residual has arbitrary high regularity. The unresolved high-inverse
claim needs both a precisely defined target and a membership proof.
