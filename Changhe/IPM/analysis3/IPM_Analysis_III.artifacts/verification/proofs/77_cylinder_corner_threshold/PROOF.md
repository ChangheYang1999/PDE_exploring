# The cylinder origin weight changes the frozen corner threshold

## Exact setting and assertions

Let A>0, D=2A+1, ell=(D-A)/2 and Sigma=A+D. Consider the full-plane
frozen transport operator

 L00=-A x partial_x+D y partial_y-1.

Functions have even-x, odd-y parity. Fix a=17/4 and eta=5/4, and use

 R=L2_P(|x|^(-2a)max(1,r)^(2a-eta)dX),
 D00={h in R:L00 h in R in distributions}.

Let delta in(1/4,2) and beta=3+delta. Near the origin the bulk high norm
is the ordinary cylinder Hs norm of r^(-beta)h, with t=log r and theta.
The angular support of this bulk space stays a positive distance from
the y-axis. A separate factored high space may be present near the
axis, as in proof 71; the forcing constructed below vanishes there.

The scalar high-frequency energy threshold at the x-axis end of the
blown-up origin is

 s_x=3/2+delta A/Sigma.                                  (1)

This differs from the Cartesian weighted threshold (b0+aA)/D. For any
s>s_x there is a forcing f with arbitrary cylinder differentiability,
compact support in r, supported in a cone away from both axes, such
that f has the prescribed origin weight, f is inR, and the unique
D00 solution of L00h=f fails local ordinary Hs across a nonzero segment
of the x-axis. It consequently fails any proposed high space that
requires local Hs there. The construction works even when the target
has the factored high order sigma>6 of proof 71.

This is a theorem about L00 and the specified cylinder weight. It does
not transfer the failure to the full nonlocal modal operator. It also
does not invalidate the product mapping theorem in proof 71.

## Direct energy calculation on the cylinder

Write

 q(theta)=-A cos(theta)^2+D sin(theta)^2,
 v(theta)=Sigma sin(theta)cos(theta).

Conjugation by r^beta gives

 r^(-beta)L00 r^beta=q partial_t+v partial_theta+beta q-1.

With cylinder measure dt dtheta, the negative zeroth-order energy
coefficient is 1-beta q+v'/2. At theta=0 it equals

 1+beta A+Sigma/2=Sigma(3/2+delta A/Sigma),

using D=2A+1 and Sigma=3A+1. Commuting an angular derivative of order
s costs s v'(0)=s Sigma. This proves(1).

At theta=pi/2 the corresponding coefficient is

 1-beta D-Sigma/2+s Sigma
 =Sigma(s-5/2-delta D/Sigma).

For the factored unknown h/(x^2 y r^delta), the identity
L00(x^2 y u)=x^2 y(-A x partial_x+D y partial_y)u instead gives the
vertical-axis coefficient Sigma(s-1/2-delta D/Sigma). These are
normal-family coefficients, not a complete variable-order inverse.
At infinity, conjugation by r^gamma for the pure dilation ell X.grad-1
gives ell partial_t+ell gamma-1 and negative energy1-ell gamma.

## A forcing that tests the cylinder threshold

Choose tau>0 small enough that

 nu=1+(delta+tau)A/Sigma,   nu+1/2<s,                     (2)

and avoid odd positive integers for nu. Put B=3+delta+tau. Choose a
nonnegative, nonzero smooth phi supported in(1/2,1), and a smooth
nonnegative chi on[0,infinity), equal1 on[0,1/2] and0 on[1,infinity).
For x>0,y>0 define

 f(x,y)=x^B chi(x) phi(y/x),

and extend by the required parity. Set f=0 on the axes. For every
nonzero point of the axes, f vanishes in a neighborhood. Near0 its
angular support is strictly inside the cone 1/2<y/x<1 and

 r^(-beta) f=r^tau (cos(theta))^B phi(tan(theta)).

This belongs to H^N(dt dtheta) for every finite N, since all derivatives
are exponentially decaying as t tends to minus infinity and the
angular factor is smooth and compactly supported. Division by x^2y
on this angular support is harmless. Thus f is in the factored target
with the same delta and any finite sigma. The compact radial cutoff
also gives every stated far-field weight. Since B>a-1, f is inR.

The weighted transport energy is strictly positive globally: forr<1
it is b0+aA, b0=1+ell; forr>1 it is

 b0+eta A/2+(a-eta/2)Sigma sin(theta)^2>0.

The global linear flow is (e^(-At)x,e^(Dt)y). Therefore the unique
maximal-domain solution is the convergent Bochner integral

 h(x,y)=-integral_0^infinity e^(-u)
                  f(e^(-Au)x,e^(Du)y)du.                (3)

The positive weighted energy, the transport group and its resolvent
identity show h inR and L00h=f inR, hence h inD00. This avoids any
assumption about pointwise behavior of the solution at large x.

For0<x<1/2 and0<z=y/x<1/2, the cutoff chi(e^(-Au)x) is always1.
Substitute v=z exp(Sigma u) in(3). The angular support gives exactly

 h(x,y)=-C x^(B-nu)y^nu,
 C=(1/Sigma)integral_(1/2)^1 v^(-nu-1)phi(v)dv>0,
 nu=(1+AB)/Sigma=1+(delta+tau)A/Sigma.                   (4)

The parity extension replaces y^nu by sign(y)|y|^nu. On a compact
subsegment0<x0<x<x1<1/2 the x factor is smooth and nonzero. A cutoff
of sign(y)|y|^nu belongs locally to Hs in y exactly for s<nu+1/2,
when nu is not an odd positive integer. In particular(2) implies
failure at the claimed order. One direct proof differentiates an
integer number of times and evaluates the fractional difference
integral on pairs y,z of comparable positive size near0; the scaling
factor is epsilon^(2nu+1-2s), which is nonintegrable at or above the
threshold. The derivative is nonconstant unless it becomes a polynomial;
that exceptional case was excluded.

Tensoring with a nonzero smooth x cutoff preserves this local Sobolev
failure. Any Hilbert sum in which both summands have local Hs on this
segment also excludes h. This applies to proof 71 when sigma>s: the
factored summand is at least Hs locally after multiplication by x^2y,
and the bulk summand has local Hs by definition.

## Concrete parameter implications

For the actual frozen rates use k=1615536043799051/9007199254740992,
A=2/k-1, D=4/k-1. All threshold comparisons in the evidence are exact
rational arithmetic. For delta=3/2 the threshold(1) is less than2,
so s=21/10, while valid for the mapping theorem, cannot be justified
by this frozen-cylinder inverse. Taking tau=1/10 in(4) already gives
nu+1/2<21/10.

For delta=9/5 and s=41/20, the strict scalar inequality s<s_x holds.
There is room to choose sigma=25/4 below the spline-knot ceiling and
above the factored vertical-axis threshold. More generally delta<2
and s=2+epsilon require

 epsilon<2A/Sigma-1/2

if the x-axis scalar energy inequality is used. The actual weighted
normal-family and nonlocal coupling estimates remain separate tasks.

## Dependencies and verification scope

The proof uses the explicit linear flow, weighted change of variables,
the elementary Sobolev threshold for a power and exact rational rates.
It independently checks the corner-weight observation in the theory author's
TH_varorder consultation. The Cartesian counterexample of proof 64 is
a different norm calculation; neither may be substituted for the other.
