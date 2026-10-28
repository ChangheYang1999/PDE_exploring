# Exact rectangle masses for finite-envelope witnesses

## Statement

Use the centrally odd, Y-even finite-envelope witness f of
`../PROOF.md`, with exponent alpha in (0,1). Write x=(1/2,0), y=-x and
nu=K_xx(.-x)-K_xx(.-y). Choose 0<delta<1/(2 sqrt(2)) and L>1 with
L/delta=2^N for a positive integer N. The construction below gives a
rigorous lower bound for the R_1^2 increment in terms of finite, exact
rectangle masses and certified envelope evaluations.

All coordinates may be rational. No interpolation consistency or
optimality of the input nodes is assumed.

## A disjoint square-shell partition

For r=delta,2delta,...,L/2, the first-quadrant part of the square annulus
r<=max(|X-1/2|,Y)<=2r is the union, up to boundaries, of these rectangles:

* upper band: max(0,1/2-2r)<=X<=1/2+2r, r<=Y<=2r;
* right strip: 1/2+r<=X<=1/2+2r, 0<=Y<=r;
* left strip, if nonempty: max(0,1/2-2r)<=X<=1/2-r, 0<=Y<=r.

Subdivide these rectangles in any finite way. They cover precisely the
first-quadrant rectangle [0,1/2+L] x [0,L] except for the upper half of
the square of radius delta about x. Their four symmetry copies cover
[-1/2-L,1/2+L] x [-L,L] except for the full small squares about x and y.
Interiors are disjoint. This outer rectangle contains B(0,L).

## Exact signed mass of each cell

For a rectangle E=[a,b] x [c,d] and a real pole p, define

$$A_p(X,Y)=\arg(Y+i(X-p))\in[-\pi/2,\pi/2].$$

All cells avoid the poles; if c=0, their horizontal interval stays on one
side of each pole. Therefore the corner expression is unambiguous and

$$m_p(E)=\int_E K_{xx}(X-p,Y)\,dX\,dY
=\frac{A_p(b,d)-A_p(a,d)-A_p(b,c)+A_p(a,c)}{2\pi}.$$

To verify this, first integrate K_xx in Y using the primitive
Y/[2pi((X-p)^2+Y^2)], and then in X. The limit as c decreases to zero is
valid for these cells. The mass of nu is m(E)=m_(1/2)(E)-m_(-1/2)(E).

An interval enclosure of nu on E gives a total-variation bound t(E):
if its sign is fixed, t=|m|; otherwise t=area(E) sup_E|nu|. The latter
supremum can be enclosed directly using
nu=Re(z/[pi(z^2-1/4)^2]). No numerical quadrature of the signed mass is
needed.

Let q be the cell midpoint and eta half its diagonal. Use the finite-tree
envelope evaluation and the variation epsilon(q,eta) from the preceding
proof. Then

$$\int_E\nu f\in m(E)f(q)+[-t(E)\epsilon,t(E)\epsilon].$$

Summing four times these intervals encloses the compact part of the full
increment. In particular, exact signed masses preserve cancellation of
the constant part of f close to a pole.

## Omitted small squares and the exterior

Put h=sqrt(2) delta. The two small squares lie in B(x,h) and B(y,h).
The principal-value integral of the own kernel over each full square is
zero, since the square is invariant under interchanging its coordinates
and K_xx changes sign under that interchange. Subtracting the value at
the pole, [f]<=1 therefore gives for the two own-kernel terms together

$$\frac4{\pi\alpha}h^\alpha.$$

This follows by enlarging to the two radius-h disks and using
int_0^(2pi)|cos(2theta)|/(2pi) dtheta=2/pi. The smooth cross terms over
the two squares have total absolute value at most

$$\frac{4\delta^2}{\pi(1-h)^2}\left(\frac12+h^\alpha\right).$$

Indeed their total area is 8delta^2, the other-pole kernel is at most
1/[2pi(1-h)^2], and |f|<=1/2+h^alpha there. Thus define

$$E_{\rm small}=\frac4{\pi\alpha}(\sqrt2\delta)^\alpha+
\frac{4\delta^2}{\pi(1-\sqrt2\delta)^2}
\left(\frac12+(\sqrt2\delta)^\alpha\right).$$

The omitted exterior is contained in {|z|>L}, so its absolute value is at
most E_tail(L) from the preceding proof. If J_low is the lower endpoint
of the compact interval sum and b is an upper bound for f(x), then

$$D_\alpha\ge J_{\rm low}-E_{\rm small}-E_{\rm tail}(L)-b.$$

The covering, mass formula, variation bound and endpoint estimates all
hold independently of any numerical approximation used to propose the
node data or to choose the subdivision.
