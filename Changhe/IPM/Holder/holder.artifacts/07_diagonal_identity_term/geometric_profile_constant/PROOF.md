# The projection profile with its full two-point geometry

## Statement

For 0<alpha<=1/2 let

$$g(z)=\frac12\left(|z|^\alpha+
 \operatorname{sgn}(z_1z_2)\left(\frac{2|z_1z_2|}{|z|}\right)^\alpha\right),
 \qquad g(0)=0.$$

For 0<u<1 and 0<=a,b<=pi/2 put

$$Q_\alpha(u,a,b)=
 \frac{1-u^\alpha+\sin(2a)^\alpha+u^\alpha\sin(2b)^\alpha}
 {2(1+u^2-2u\cos(a+b))^{\alpha/2}}.$$

At the single degenerate corner u=1,a=b=0 use the limiting bounds below,
not division by zero. Define

$$K^*_\alpha=\max\{1,\sup_{0<u<1,\ 0\le a,b\le\pi/2}Q_\alpha(u,a,b)\}.$$

Then [g]_alpha<=K^*_alpha. In every previously proved finite projection
witness, its seminorm denominator K_alpha may be replaced by K^*_alpha
or by any certified upper bound for K^*_alpha. This change preserves all
the other hypotheses of that witness theorem. No numerical value is
asserted without a complete interval covering certificate.

## Proof and finite covering procedure

The same-sign quadrants, the reverse ordering of opposite-sign values,
and the case where the negative point has larger radius have quotient
at most one. The local-profile proof and its extension to alpha<=1/2
establish these cases. In the only remaining case, central symmetry,
coordinate interchange and dilation reduce the points to e^{ia} and
u e^{-ib}. Substitution gives Q exactly. Boundary axes follow by
continuity and pairs involving the origin have quotient at most one.
If a+b>=pi/2, the distance is at least one, while 0<=g(negative)<=
u^alpha/2 and g(positive)<=1. Hence Q<=1 on that region.

Fix epsilon in (0,1/2). On u<=epsilon, Q<=(1-epsilon)^(-alpha).
On u>=1-epsilon the already proved refined-profile endpoint estimate
applies. With k=1/(1-alpha), R_*=(1-epsilon)^alpha and
c=alpha/(1-epsilon)^(1-alpha), this bound is

$$1+\frac{(k-1)c^2\epsilon^2}{8R_*}
   +\frac c2\epsilon^{1-\alpha}.$$

Cover [epsilon,1-epsilon] x [0,pi/2]^2 by rational rectangular boxes
in u,a/pi,b/pi. On each box the direct interval evaluation of Q is
valid wherever its distance lower bound is positive. The following
monotonic bounds reduce dependency losses. If S_a,S_b are upper bounds
for sin(2a),sin(2b), clipped at one, and u_l is the lower radial endpoint,
then its numerator divided by two is at most

$$N=\frac{1+S_a^\alpha-u_l^\alpha(1-S_b^\alpha)}2.$$

One may also replace N by min(N,1). The minimum squared distance over
a box is at least the minimum of 1+u^2-2u cos(t_l) on its radial interval,
where t_l is the lower endpoint of a+b. This convex quadratic is minimized
at the closest point of the interval to cos(t_l); if interval comparisons
cannot decide which endpoint applies, sin(t_l)^2 is always a valid lower
bound. The simpler bound (1-u_h)^2+4u_l sin(t_l/2)^2 is also valid and
may be maximized with that bound.

The one-dimensional A(u),B(u) bounds of the refined-profile proof also
remain valid, so any box upper bound may be reduced by their upper
bounds. Subdivide each unresolved box into two closed children with
exact common rational boundary. When every box upper bound is at most
a proposed K, and both endpoint bounds are at most K, the finite covering
proves K^*_alpha<=K. No assumed location of the maximum is used. Floating
point calculations may choose a subdivision order but cannot certify
or discard a box.
