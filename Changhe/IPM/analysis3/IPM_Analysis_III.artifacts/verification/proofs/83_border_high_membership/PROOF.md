# High-target membership of the exact normalization correction

## Statement, spaces and scope

Let rho be the exactly normalized, exactly C6-joined finite modal trial
of topics04 and50, with canonical full-plane velocity U[rho]. Set

 k=1615536043799051/9007199254740992, ell=1/k,
 p=x^2 y, V=ell X+U[rho], Gbar=X.grad rho,
 Lfix h=V.grad h-h+U[h].grad rho.

Choose smooth radial functions chi0 and chiinf with chi0=1 near0 and
compact support, and with 0<=chiinf<=1, chiinf=0 for r<=1 and chiinf=1
for all sufficiently large r. Let Theta be the exact leading angular
tail of rho. Define

 Phi=chiinf r^k Theta, KP=chiinf r^k log(r) Theta,
 gfar=(1-chi0)Gbar-k Phi,
 yKP=Lfix KP+(c[KP]/3)chi0 Gbar-ell Phi,
 d=3ell+k c[KP], zeta=(ell gfar-k yKP)/d.

These are the unshifted logarithmic variation and the same bordering
convention as proof 31. That topic proves d>=3ell>0 for this actual
Theta and the specified nonnegative cutoffs. No inverse is assumed.

Write t=log r and choose q smooth with q=0 on t<=0 and q=1 on t>=1.
For 0<delta<2 and gamma>2k-1 set

 A(t)=exp(delta t+(gamma-3-delta)t q(t)).

For each f in {gfar,yKP,zeta}, the quotient f/(p A), defined first off
the axes, has a continuous angular extension and belongs to
H^sigma(R times S1) for every 0<=sigma<13/2. Thus it belongs to the
zero-scalar-coordinate base target H_base^sigma of proof 71. This is
true in particular for delta=9/5, gamma=-1/2 and sigma=25/4.

The same three functions belong to the strong low target Y=E G direct
sum R, where

 R=L2_P(|x|^(-17/2) max(1,r)^(29/4) dX),
 G=L2(wG(t)dt), wG=e^(-t/2) for t<=0 and e^(27t/4) for t>=0,
 (E beta)(X)=p beta(log r),

and P denotes even-x, odd-y parity. Consequently they belong to
Y intersect H_base^sigma. The rank-one map h -> c[h] zeta is bounded
from the actual strong graph domain Z of proof 76 to that intersection,
with norm at most ||c||_(Z*) ||zeta||_(Y intersect H_base^sigma), for
any fixed convention for the intersection norm. This asserts that the
constant is finite; no numerical upper bound for it is claimed.

This result does not establish any derivative gain for the full
coupling, injectivity, a high-regularity inverse, or a uniform inverse
for perturbed transport fields. A proposed variable-order target must
contain the stated base space before the result applies to it.

## Exact angular factorization

The trial has rho=p a(t,theta), with a a finite polynomial in cos(2theta).
Theta=cos(theta)^2 sin(theta) times another such polynomial. Hence
KP=p b(t,theta), where b has finite angular bandwidth and smooth radial
coefficients on finite t intervals. The velocities of rho and KP have
the IPM parities and finite angular bandwidth. The finite trigonometric
identities imply that U1/x and U2/y have finite, smooth angular
extensions. In particular an odd-x angular factor is divisible by
cos(theta), and an odd-y factor by sin(theta).

For either such velocity W and any p b, one has exactly

 W.grad(p b)/p=(2W1/x+W2/y)b+(W_r/r)b_t+(W_theta/r)b_theta.       (1)

Also Gbar/p=3a+a_t. Thus gfar/p and yKP/p are finite angular polynomials,
even under both Cartesian reflections. Every estimate below is an
estimate of these cofactors. An absolute O(r^j) bound on a function is
not divided by p without (1).

## Origin cancellation and bounds

The verified inner modal expansion gives

 a=1+O(r^2), U[rho]=c[rho](-x,y)+O(r^3),

with these orders preserved by every fixed number of cylinder
derivatives on a sufficiently small punctured disk. Here and below
such statements permit constants depending on the derivative order.
The exact normalization is c[rho]=3ell-1.

KP vanishes on r<=1. Its canonical velocity is smooth near0. This can
be seen by differentiating the reflected full-plane kernel: for the
first derivative the exterior integral is bounded at infinity by a
constant times integral_1^infinity r^(k-2)(1+log r)dr, which converges
because k<1; higher derivatives improve the power. The zeroth-order
velocity is defined by the canonical symmetric integral and its odd
parities. Equivalently the finite modal Green formulas give the same
analytic interior field. Those parities and the strain identity give

 U[KP]=c[KP](-x,y)+O(r^3).

There is no constant or quadratic term. Its smooth remainder and the
finite angular expansion satisfy the corresponding cofactor bounds.
For all sufficiently small r, gfar=0 and

 yKP=[U[KP]+c[KP] X/3].grad rho.

The coefficient of p from the linear velocity acting on p is

 c[KP](-2+1)+c[KP](3/3)=0.

The remaining terms of yKP/p are O(r^2), with every fixed number of
cylinder derivatives. Therefore zeta/p=O(r^2) with the same derivative
bounds. After division by A=e^(delta t), these quotients and all fixed
cylinder derivatives decay like e^((2-delta)t) at the negative end.

## Far-field cancellation and bounds

The exact finite outer expansion gives

 rho=r^k Theta+O(r^(2k-1)),
 U[rho]=O(r^k),

with all fixed cylinder derivatives and with the finite angular
cofactor estimates furnished by (1). There may be faster decaying
power-log terms, which obey the displayed bounds.

The canonical velocity of KP is O(r^k(1+log r)), with all fixed
cylinder derivatives. To check the full-plane assertion rather than
just a formal homogeneous ansatz, apply the finite modal Green formula
to each odd density mode. Outside the cutoff region the particular
solution is a linear combination of r^k and r^k log r. The denominators
are k+n+2 and k-n+2 for odd angular n. None is zero because 0<k<1.
The cutoff changes only decaying exterior homogeneous multipoles.
The canonical condition excludes growing exterior homogeneous terms.
This proves the stated estimate for the actual cutoff profile.

At large r, chi0=0 and chiinf=1. Since ell k=1,

 (ell r partial_r-1)KP=ell r^k Theta=ell Phi,
 gfar=Gbar-k r^k Theta=O(r^(2k-1)),
 yKP=U[rho].grad KP+U[KP].grad rho
     =O(r^(2k-1)(1+log r)).

The cofactor orders are therefore

 gfar/p=O(r^(2k-4)),
 yKP/p=O(r^(2k-4)(1+log r)),
 zeta/p=O(r^(2k-4)(1+log r)).                             (2)

They hold for all fixed cylinder derivatives. Dividing by
A=e^((gamma-3)t) makes (2) decay at the positive end like
(1+t)e^((2k-1-gamma)t). The exponent is strictly negative by hypothesis.

## Fractional regularity through all finite knots

On each finite radial piece, rho, its velocities and the displayed
expressions have smooth coefficients with finite one-sided derivatives
of every fixed order. Across each knot rho and U[rho] are C6; the
expressions above use at most one derivative of rho or KP. Their
cofactors are consequently C5 across every knot. The smooth cutoffs
introduce no jumps. The weighted cofactors have the same properties.

There are finitely many knots and finitely many angular modes. Each
radial coefficient is therefore globally H6, with a sixth derivative
that is piecewise smooth and may have finitely many jumps. A jump lies
in H^alpha_loc for every alpha<1/2: the only potentially singular
cross-knot double integral is bounded by a constant times

 integral_0^a integral_0^a (u+v)^(-1-2alpha) du dv,

which is finite exactly when alpha<1/2. Away from knots all derivatives
are locally bounded, and the endpoint estimates above are exponential,
with at most polynomial factors. They control the remaining global
fractional double integrals. It follows that each weighted cofactor
lies in H^sigma(R times S1) for every sigma<13/2. Negative orders are
not needed. No assertion at sigma=13/2 is made.

## Membership of the strong low target

Let B=f/p for any of the three functions, and set beta(t)=B(t,pi/2).
The finite angular polynomial and evenness imply the exact factor

 B(t,theta)-beta(t)=cos(theta)^2 C(t,theta),

where C has finite bandwidth and the same radial orders as B. Thus
f=E beta+u, u=p cos(theta)^2 C. The angular integral in the R norm is
bounded by a constant times integral |cos(theta)|^(-1/2)sin(theta)^2
dtheta, which is finite at both axes. Its radial factor before C^2 is
e^(-t/2) at the negative end and e^(27t/4) at the positive end. These
are also precisely the weights in the G norm of beta.

At the negative end B,C=O(e^(2t)), so both squared norm integrands are
O(e^(7t/2)). At the positive end they are bounded by a constant times
(1+t)^2 e^((4k-5/4)t), which is integrable since 4k<5/4 for the exact k.
All finite intervals are harmless. Hence beta in G and u in R, proving
f in Y. This proof is independent of any high-space embedding theorem.

Finally c is a bounded linear functional on the actual strong Z by
proof 76 and its referenced strain estimate. Multiplying its scalar
value by the fixed zeta gives the asserted bounded rank-one map.

## Dependencies

Topics04 and50: normalized finite modal construction and global C6 joins.
Proof 31: strain identity, bordering algebra, actual d>=3ell>0.
Topics71 and75: high-base convention and fractional knot argument.
Proof 76: actual strong graph domain and bounded central strain.
Proof 81: finite homogeneous modal coefficients (the far-field check also
follows directly from the original modal Green formulas).
