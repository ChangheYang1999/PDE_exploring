# Global fractional high-target membership of the modal residual

## Exact statement

Let rho be the exactly normalized, exactly C6-joined modal density of
topics04 and50, with

 k=1615536043799051/9007199254740992, ell=1/k,
 p=x^2 y, V=ell X+U[rho], F=V.grad rho-rho.

Use the canonical full-plane velocity. Write t=log r. Choose a smooth
q(t) equal0 for t<=0 and1 for t>=1, and set

 A_(delta,gamma)(t)=exp(delta t+(gamma-3-delta)t q(t)).

For every

 0<delta<2,  2k-1<gamma,  0<=sigma<13/2,

the function

 u_F(t,theta)=F(exp(t)cos(theta),exp(t)sin(theta))
                    /[p(exp(t)cos(theta),exp(t)sin(theta))
                      A_(delta,gamma)(t)]

has continuous angular extensions at both axes and belongs to
H^sigma(R times S1). It has the even cofactor parity under the two
Cartesian reflections. Thus F belongs to H_base^sigma of proof 71
with scalar coordinate j=0. In addition, if

 delta>1/4 and gamma<-3/8,

then F belongs to the exact low target Y=E G direct-sum R of proof 71.
These intervals are compatible for the actual k. The concrete choice

 delta=3/2, gamma=-1/2, sigma=25/4

satisfies all conditions. Consequently the actual normalized residual
belongs to the explicit high target Y intersect H_base^(25/4), and
also to Y intersect (H_base^(25/4)+Q) for any permitted bulk summand Q.
The norms are finite but no upper bound for their size is asserted.

This is a membership theorem, not an inverse theorem. Other proposed
high targets must specify their weights before this result applies.
The upper Sobolev endpoint is sharp at the nonzero jump established
in proof 67, on any open arc where its sixth-derivative jump is nonzero.

## Angular factorization including both axes

The modal density is rho=p a(t,theta), with a a finite cosine
polynomial in2theta. The canonical velocity has finitely many angular
modes and the IPM parities. Therefore V1/x and V2/y have smooth finite
angular polynomial extensions: an odd-x cosine polynomial is divisible
by cos(theta), and an odd-y sine polynomial by sin(theta), using the
finite trigonometric addition formulas. Put q_r=V_r/r and v=V_theta/r.
The exact cofactor identity is

 F/p=(2V1/x+V2/y-1)a+q_r partial_t a+v partial_theta a.       (1)

It holds off the axes by differentiation and extends across them by
the finite angular identities. In particular F/p is a finite angular
cosine polynomial, with coefficients depending on t. No division
estimate near a zero of p is being inferred from an absolute bound
on F. All bounds below follow from the cofactor identity itself.

## Origin cancellation and all cylinder derivatives

The inner continuation of a is a finite sum of a constant1, powers
r^(2j), j>=1, and r^bi times polynomials in log r of degree at most6,
with bi>50. Hence, for every fixed number of cylinder derivatives,

 a=1+O(r^2), partial_t a=O(r^2), partial_theta a=O(r^2).

The Green expansion of proof 52 gives

 V1/x=-A0+O(r^2), V2/y=D0+O(r^2),
 A0=2ell-1, D0=4ell-1,

with the same bounds after every fixed number of cylinder derivatives.
Indeed the inner modal Green expressions are finite sums of powers
and log powers; their first possible nonpolynomial term is
O(r^4(1+|log r|)) after division of V by a coordinate. This term and
all its fixed cylinder derivatives are O(r^2). The leading term
satisfies exactly

 -2A0+D0-1=0.

Also q_r and v and all their fixed cylinder derivatives are bounded.
Equation(1) therefore yields F/p=O(r^2), including every fixed
cylinder derivative. The exact central-strain normalization is
essential to the constant cancellation. Since A_(delta,gamma)=r^delta
at this end, u_F and all such derivatives are O(exp((2-delta)t)).
They are square integrable on t<0 when delta<2.

## Far cancellation

The outer density is a finite sum whose leading term is r^k Theta,
whose next possible power is r^(2k-1), and whose remaining powers
are no larger. The matching correction is r^(3-bo) times a log
polynomial, with bo>125, and is faster. All cylinder derivatives obey
these power bounds. The exact equality ell k=1 cancels the leading
term in (ell r partial_r-1)rho, so

 (ell r partial_r-1)rho=O(r^(2k-1)).

Proof 52's finite Green formula gives U=O(r^k), together with all fixed
cylinder derivatives. Since grad rho=O(r^(k-1)), the nonlinear term
U.grad rho is O(r^(2k-1)). To control the cofactor uniformly at the
axes, use(1), the divided-velocity angular formulas, and separate
ell r partial_r-1 before estimating. They give

 F/p=O(r^(2k-4))

with all fixed cylinder derivatives and with smooth bounded angular
coefficients. Since p A_(delta,gamma) has radial size r^gamma at this
end, u_F and all cylinder derivatives are O(exp((2k-1-gamma)t)).
These are square integrable on t>1 when gamma>2k-1.

## Fractional regularity across the finite knots

The original spline interval has finitely many knots. At every knot,
a is C6 and piecewise analytic; the velocity is C6 and piecewise
analytic by the finite radial Green ODE. Equation(1) is therefore C5
in t, piecewise analytic, with finite one-sided derivatives of all
orders. Multiplication by the smooth nonzero factor A^-1 preserves
these properties. A smooth compact cutoff of each angular coefficient
has a bounded piecewise smooth weak sixth derivative. There are no
point masses in that derivative because the derivatives through
order5 agree.

Such a sixth derivative belongs to H^tau(R) for every0<=tau<1/2.
For a direct proof, split the Gagliardo double integral into regions
on the same side and on opposite sides of each knot. Smoothness
bounds the same-side terms. The opposite-side part is bounded by a
constant times

 integral_0^epsilon integral_0^epsilon
                (x+y)^(-1-2tau) dx dy,

which is finite for tau<1/2. Terms a fixed distance from a knot have
no singularity. It follows that the original compact coefficient is
in H^(6+tau). Lower orders follow by the Fourier definition. There
are finitely many angular Fourier modes, so one-dimensional Hsigma
regularity of their radial coefficients is equivalent to cylinder
Hsigma regularity, with finite constants depending on those modes.

A finite partition of unity separates the compact knot interval and
the two smooth ends. The exponential derivative bounds above put the
end pieces in H^m for every fixed integer m, hence every finite real
order below m. Combining them proves u_F in Hsigma for sigma<13/2.
Proof 67's nonzero sixth-derivative jump proves failure at13/2 locally
on the specified arc; multiplication by a smooth nonvanishing radial
weight cannot remove that jump.

## Direct low-target membership

Let B_F=F/p and beta_F(t)=B_F(t,pi/2). Both have radial-logarithmic
bounds O(r^2) at0 and O(r^(2k-4)) at infinity. Their angular derivative
bounds and evenness give B_F-beta_F=O(cos(theta)^2) with the same radial
bounds. Thus

 F=E beta_F+R_F, R_F=p(B_F-beta_F).

The exact target G has weights e^(-t/2) at0 and e^(27t/4) at infinity.
Its two squared integrands for beta_F are bounded by

 C e^((7/2)t), t<0, and C e^((4k-5/4)t), t>1.

Both integrate since k<5/16. For R_F, the extra cos^2 in the cofactor
makes the angular squared exponent8-17/2=-1/2, which is integrable;
the radial powers are precisely the same. Hence beta_F in G and
R_F in R, proving F in Y directly. This part does not need positivity
of d or any inverse assumption. The parameter restrictions
1/4<delta<2 and 2k-1<gamma<-3/8 merely align the statement with the
verified correction spaces of proof 71.

## Dependencies and scope

The exact input, scalar normalization and joins are from topics04
and50. The canonical velocity and endpoint expansions are derived
in proof 52. Proof 67 provides the independent exact nonzero knot jump.
Every new inference here is an explicit factorization, power estimate
or elementary fractional-Sobolev integral. No floating residual norm,
collocation accuracy, injectivity or high inverse is used.
