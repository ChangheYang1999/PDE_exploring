# Corrections and exact scope of the theory author's first weighted theory draft

The audited version is the fixed snapshot in
`../20_frozen_origin_global/evidence/lead_snapshot.md`. This note supplies
proofs for the individual verdicts rather than treating an entire section
as correct or incorrect. No sampled number is certified here.

## Product-conic coercivity and its borderline

Let A>0,D=2A+1,b0=(A+3)/2, and near0 put
w=r^{-2beta}|cos theta|^{-2a}|sin theta|^{-2b}. Then for the frozen field
Y0=(-Ax,Dy),

 kappa(theta)=b0+aA-bD+(a+b-beta)(-A cos^2 theta+D sin^2 theta).

Its strict positivity on every ray is equivalent to

 [(A+D)b-b0]/A < beta < [(A+D)a+b0]/D.

This follows by evaluating the affine expression at -A and D. The cut-off
cubic x^2 y belongs to L2(w) near0 exactly when a<5/2,b<3/2,beta<4.
At a=5/2 and b=3/2 the two respective radial thresholds are both4.
Consequently coercivity together with exclusion of the cubic forces a>=5/2.
This conclusion in Proposition N1 is correct. Strict a>5/2 is not forced:
a=5/2,b=0,beta=3 gives positive endpoint margins b0+3A and D, while the
cubic is excluded by logarithmic angular divergence.

If a(t) is smooth and a weight contains |cos theta|^{-2a(t)}, its transport
logarithmic derivative has the term
 -a'(t) q(X) log|cos theta|.
At a fixed radius with outgoing axis rate q(0,y)>0, a'(t)<0 therefore
forces kappa to negative infinity on approach to the y-axis, provided the
other displayed terms remain bounded. Thus a lower coercive bound requires
a'(t)>=0 wherever that positive-axis-rate hypothesis holds. The claimed
positivity of q along the whole actual axis is a separate, uncertified
hypothesis in the first draft; a numerical sample is insufficient.

## The full y-axis jet equation

Assume enough local C4 regularity to take the following x jets, and write
h=x^2 g(y)+O(x^4), rho=x^2 rho_2(y)+O(x^4),
V1=u(y)x+O(x^3), V2=v(y)+O(x^2). Let c=c[h] be the raw strain.
The x^2 coefficient of the full normalized linearization is

 v g'+(2u-1)g
 +2 rho_2 partial_x U1[h](0,y)+rho_2' U2[h](0,y)
 +(c/3)(2 rho_2+y rho_2').

Every term follows by multiplying these Taylor expansions. The last term
is the coefficient of (c/3)X.grad rho and is missing from the first N3
formula. Equivalently one can replace U by W=U+cX/3 in both coupling
terms. For a normalized background at0, rho_2=y+O(y^3),
v=Dy+O(y^3), u=-A+O(y^2),
partial_x U1[h](0,y)=-c+O(y^2), U2[h](0,y)=cy+O(y^3).
The two U terms have leading coefficient -cy, while the normalization
term is +cy. Their cancellation is essential. For g=y beta(log y), the
remaining leading transport coefficient is D y beta_t. Without the
normalization term, the stated leading cancellation is false for c!=0.

This is a jet identity under the explicit regularity and expansion
hypotheses. It is not a trace theorem for arbitrary elements of an
unspecified weighted graph space.

## Far weights and exponent variations

For a nonzero angular leading coefficient on a set of positive measure,
a function r^p(log r)^j belongs to L2(r^{-2gamma}dX) at infinity exactly
when p<gamma-1, or in the equality case when the logarithmic factor is
square-integrable against dr/r. In particular the nonnegative integer
log powers relevant here are not in the equality case. For the radial
field ell X, the transport energy coefficient is 1+ell-ell gamma.
Thus the window 2k<gamma<1+k, ell k=1, simultaneously admits a nonzero
r^{2k-1} leading residual, excludes r^k and has positive transport margin.
The lower inequality is only necessary if that residual leading coefficient
is actually nonzero; an upper asymptotic estimate alone does not prove it.

The literal statement that r^{k'}-r^k cannot be written as
r^k(C+d log r)+o(r^k) is false when k'<k: take C=-1,d=0.
The following stronger-space conclusion is valid and is what the nonlinear
formulation needs. Fix gamma<1+k and a nonzero angular theta. If
0<|delta|<1+k-gamma, then

 r^{k+delta}theta-r^k theta
 is not in span{r^k theta,r^k log r theta}+L2(r^{-2gamma}dX).

For delta>0 the higher power cannot be cancelled. For delta<0 any nonzero
log coefficient or any constant coefficient other than -1 leaves a
nonintegrable r^k term; with those terms cancelled, r^{k+delta} remains
nonintegrable since k+delta>gamma-1. This proof also explains why the
asymptotic o(r^k) formulation was too weak. Differentiating the exponent
twice gives r^k(log r)^2, which lies outside the fixed first-order tangent
space. A consistent nonlinear formulation must treat the varying exponent
parametrically or use another space that actually admits the family.

## Compensation uses the uncompensated strain

Suppose h=h0+d KP, c is linear, and the leading r^k theta coefficient of
Lh is ell d+(k/3)c[h]. Cancellation is equivalent to

 d=-k c[h]/(3ell).

If 3ell+k c[KP] is nonzero, it is also equivalent to

 d=-k c[h0]/(3ell+k c[KP]).

The second denominator must be paired with the uncompensated strain c[h0],
not with c[h]. An assertion using the latter double-counts the dependence
of the strain on the added KP column. The denominator and all image/tail
membership conditions remain part of the operator realization.

## A Lipschitz velocity does not imply a Holder derivative of the density

The condition partial_x h in C^alpha, with the usual decay conditions for
the Riesz transforms, is sufficient for DU[h] in C^alpha and hence for a
Lipschitz velocity. It is not equivalent to a Lipschitz velocity.
Here is a compact counterexample for every fixed0<alpha<1.

Choose an odd compactly supported C2 function p(x), supported away from0,
with p'' continuous but not C^alpha near some positive point. Arrange
integral_0^infinity p=0 by subtracting a smooth bump away from that point;
this does not change the failure of Holder regularity. Such a p is obtained
by integrating twice a compact continuous function with modulus
1/|log|x-x0|| near x0 and correcting its two moments by smooth bumps,
then extending oddly and correcting the half-line integral. Let
P(x)=integral_{-infinity}^x p(s)ds. It is compact, even and zero near0.
Take a nonzero odd q in C_c^infinity(R), and set

 psi=p(x)q(y),
 h=-p'(x)q(y)-P(x)q''(y).

Then -Delta psi=partial_x h exactly, so its compact stream gives the
canonical velocity U[h]=(-p q',p' q). The density h is compact, C1, even
in x, odd in y, and vanishes near the y-axis; all origin jets vanish.
The velocity has bounded first derivatives and is Lipschitz. Its strain
at0 is0. But partial_x h=-p''q-pq'' is not C^alpha at a point where
q is nonzero. Thus even within this compact admissible parity class the
asserted necessity is false. The valid equivalence, with suitable spaces
and decay, is between DU in C^alpha and partial_x h in C^alpha, using
curl U=-partial_x h and the Riesz identities; this is a stronger condition
than merely DU bounded.

## Claims which remain open

The draft's global characteristic geometry, uniformly bounded transit
times, all sampled radial and anisotropic margins, the full edge Garding
lemma including the origin corner, the unspecified global jet Banach norm,
and the resulting conditional theorem on that unspecified domain are not
proved by the preceding calculations. In particular a phrase such as
"the pure transport operator is invertible by Theorem O and the margin"
does not supply its global jet boundary conditions or its closed domain.
The radial theorem proved in proof 21 is not a substitute for those steps.
