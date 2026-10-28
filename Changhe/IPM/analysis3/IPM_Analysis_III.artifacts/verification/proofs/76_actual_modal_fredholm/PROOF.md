# Fredholm index zero for the normalized modal background

## Background and exact statement

Let rho be the exactly joined and exactly normalized modal density
constructed from the original trial_v2_h0.008.npz in proof 04. Its input
SHA-256 is a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874.
The original binary64 numbers are interpreted as exact dyadic rationals;
the endpoint corrections match derivatives through order six exactly.
The scalar outer correction is the unique exact real normalization
correction, not a chosen midpoint of its enclosure. This specifies the
background by its data and the construction proved in topics04 and50.
It is not the raw X3 density and is not a stationary solution.

Set

 k=1615536043799051/9007199254740992, ell=1/k,
 A=2ell-1, D=4ell-1, a=17/4, eta=5/4.

The canonical stream and velocity satisfy -Delta psi=partial_x rho and
U[rho]=(-partial_y psi,partial_x psi). Put V=ell X+U[rho]. All function
spaces below use even-x, odd-y parity, denoted by P, and Lebesgue measure
unless another measure is displayed. Let T=V.grad-1.

There are two distinct Fredholm assertions.

1. Define mu_R(0)=0 and prescribe its a.e. derivative by successive
values

 (4,17,28,27,25,18,4,-10,-17,-19,-20)/16

on intervals cut at 3/2,7/4,3,4,5,6,7,8,9,10. On
H_R=L2_P(exp(mu_R(log r))dX), give

 D_rad={h in H_R:T h in H_R in distributions}

the graph norm. The operator

 Lfix h=T h+U[h].grad rho : D_rad -> H_R

is Fredholm of index zero.

2. Set

 w=|x|^(-17/2)max(1,r)^(29/4), R=L2_P(w dX),
 G=L2(exp(-t/2)dt on t<0; exp(27t/4)dt on t>=0), t=log r.

Let d(t)=V2(0,exp(t))/exp(t), b(t)=D-d(t)-2d'(t),

 H(t)=exp(-integral_(-infinity)^t b(s)/d(s) ds),
 omega(t)=exp(-t/2) for t<0, exp(2(k+3/8)t) for t>=0.

The scalar Hilbert space B consists of beta=H z, with z locally
absolutely continuous, z(+infinity)=0 and finite norm

 ||beta||_B^2=|J|^2+||z'||_L2(omega)^2
       +||z-J||_L2(omega,t<0)^2+||z||_L2(omega,t>=0)^2,
 J=z(-infinity).

Let E beta=x^2 y beta(log r), D_R={h in R:T h in R} with its
maximal graph norm, Z=E B direct-sum D_R, and Y=E G direct-sum R,
with the Hilbert product norms. Fix any smooth radial chi0 equal to1
near0 and0 outside a compact set. On the dense smooth class define

 c[h]=(1/pi) integral sin(3theta)r^(-3)h(X)dX,
 C h=[U[h]+chi0 c[h]X/3].grad rho,
 Lren=T+C.

The bounded extension Lren:Z->Y is Fredholm of index zero. For every
fixed zeta in Y, Lren+c[.]zeta:Z->Y is also Fredholm of index zero.
This includes the tail-bordered Lred of topics31 and44, with its
specified cutoff, nonzero scalar denominator and Y-valued border.
The direct sums are unique and c is bounded on Z.

These are index statements. In either case invertibility is equivalent
to injectivity. No injectivity or numerical inverse norm is asserted.
The strong-space coordinate J is continuous, but an arbitrary member
of Z need not have a classical Taylor expansion at the origin.

## Verified coefficients and regularity

The independent original-data calculation in proof 68 and its separate
640-bit audit give, with the decimal numbers interpreted as exact
rationals,

 d(t)>=5.5752 for all real t,
 kappa_a(X)-bplus(X)>=0.53072 for almost every X,
 kappa_R(X)-bplus(X)>=1.78605 for almost every X,

where

 bplus=(|grad rho|-partial_y rho)/2,
 q=V_r/r, v=V_theta/r,
 kappa_a=1+ell+(mu_a'/2)q+a tan(theta)v,
 mu_a'=-17/2 on t<0, -5/4 on t>0,
 kappa_R=1+ell+(mu_R'/2)q.

The angular quotients extend by parity. The finite cover has3276 radial
cells and128 angular cells, with both infinite ends treated analytically.
The exact rational lower endpoints and input hashes are in the audit.
No claim here uses the numerics team's sharper anisotropic margin.

Topics50 and52 establish that V is globally Lipschitz and C1,
div V=2ell, V(0)=0, and that grad rho is continuous and tends to0 at
both ends. They also prove

 d-D,d'=O(exp(2t)) as t tends to minus infinity,
 d-ell,d'=O(exp(-(1-k)t)) as t tends to plus infinity.

Together with positivity and continuity these give all of condition(A)
in proof 44, including a finite upper bound on d. The exact axis
subtraction identities and endpoint expansions give finite constants
in its two angular coefficient bounds. No numerical values for those
constants are needed for an index theorem.

## Proof of the radial assertion

The weight has Lipschitz logarithm with ||mu_R'||_infinity=7/4<2.
The weighted Riesz operators are bounded and their coefficient
commutators are compact after conjugation; the detailed proof, including
its maximal domain, core and adjoint, is proof 21 with the Lipschitz
extension of proof 28. Its remaining coefficient hypotheses were checked
above. The positive margin1.78605 therefore gives the compact-defect
estimate for Lfix and its adjoint. The path T+s U[.].grad rho,
0<=s<=1, is norm-continuous from the fixed transport graph domain to
H_R, and the same positive estimate holds along it because bplus>=0.
At s=0 the transport and its adjoint are coercive and T is invertible.
The Fredholm index is constant along the path, hence is zero at s=1.

## Proof of the strong assertion

The scalar operator beta -> d beta'+b beta is an isomorphism B->G
by the exact Hardy construction in proof 38; G and the corresponding
intrinsic scalar target have equivalent norms. The positive margin
also makes T:D_R->R invertible. The exact lift identity yields a
bounded lower off-diagonal block from B toR, so T:Z->Y is invertible.

Topics46-49 prove the three coupling facts used in proof 44: C:Z->Y is
bounded; its jet row is compact; and its remainder-to-remainder block
C_R extends boundedly on R and satisfies the Gårding estimate

 Re<C_R h,h>_R <= integral (bplus+epsilon)|h|^2 w dX
                         +Re<K_epsilon h,h>_R

with K_epsilon compact on R, for every epsilon>0. These facts include
the cubic strain cancellation and the singular-axis subtraction. They
do not follow from an A2 theorem for the angular weight.

For0<=s<=1, S_s=T+sC_R on D_R has a compact-defect lower bound with
any constant less than0.53072. Thus it is upper semi-Fredholm. The
norm-continuous fixed-domain path begins at the isomorphism T, so the
semi-Fredholm index is zero throughout and S_1 is Fredholm of index0.
The full operator Lren is a bounded lower triangular operator with
isomorphic scalar diagonal and Fredholm remainder diagonal, plus the
compact jet row. Its index is therefore0. The strain is bounded onZ;
adding c[.]zeta for zeta inY is finite rank and preserves the index.
This is precisely the proof of proof 44 with every previously conditional
background hypothesis now supplied.

## Dependencies and limits

Dependencies: topics04,21,28,31,38,43,44,46-50,52 and68. Each analytic
lemma has a standalone proof and the numerical dependency has its own
original-data reconstruction, interval evidence and acceptance audit.
No finite-section singular value is used to infer the infinite-domain
index or injectivity. No solution of the nonlinear stationary equation
is obtained by this theorem.
