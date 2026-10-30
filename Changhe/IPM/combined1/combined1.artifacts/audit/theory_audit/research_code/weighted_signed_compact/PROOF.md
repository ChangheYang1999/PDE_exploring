# A compact signed-energy correction for regularized power weights

## 1. Statement and status

This is an independent alternative for the weighted low-space obstruction. It is a conditional low inverse theorem, not a high-space or nonlinear existence theorem. It is new T4 work and remains CLAIMED until independently reviewed.

Work with real centrally odd functions on R²; the S1 subspace can be imposed throughout. Put U=(-R1R2,R1²), where R_j has Fourier symbol i xi_j/|xi|. Let

w_R(x)=(1+|x|²/R²)^(-a/2), R>0, 0<a<2.

Let A=(rho_x,rho_y) be centrally even and C1. Assume, for some delta>0 and constants C0,C1,

|A(RX)| <= C0 <X>^(-delta),
|R DA(RX)| <= C1 <X>^(-1-delta), <X>=(1+|X|²)^(1/2).       (1)

The derivative norm in (1) is the Euclidean operator norm. Define Q=A.U, Q_w=w_R Q w_R^-1, initially on compact smooth odd functions. Q_w extends to a bounded operator on real odd L2. The symmetric difference

D_R=Sym Q_w-Sym Q

is Hilbert-Schmidt on that subspace. A kernel representing its extension to all L2, with zero action on even functions, is

D_R(x,y)=(1/4) B_R(x,y).[u(x-y)-u(x+y)],                 (2)
B_R(x,y)=(w_R(x)/w_R(y)-1)A(x)
          +(w_R(y)/w_R(x)-1)A(y),
u(z)=(-2z1z2,z1²-z2²)/(2pi |z|⁴).

The diagonal and antidiagonal are measure-zero sets; arbitrary finite values there give the same operator. Equation (2) is symmetric in x,y and odd in each variable under central reflection.

For an explicit finite bound, define

B_near=a(4/3)^(2+delta) C1+a²(4/3)^(2+a+delta) C0,
C_near=B_near/(4pi),
C_away=(4/pi)(2^a+1)(1+2^delta)C0,
C_comp=max(C_near,C_away), C_far=64C0/(3sqrt(3)pi).

Then

||D_R||_HS² <= 4pi² C_comp²/delta
 +2 C_far² pi² 4^(a-2)/[(2-a)delta(delta+1)].             (3)

This crude bound proves compactness. It is not expected to give a useful numerical inverse constant by itself. The exact kernel (2), rather than the coarse right side of (3), is available for a finite-rank certificate.

## 2. The weighted canonical operator and contact term

The nonlocal kernel of U is u above. Its second component also has the contact term -(1/2)I. To see the sign, differentiate the two-dimensional fundamental solution -(log|z|)/(2pi) of -Delta. The trace of its Hessian is -delta_0, so each diagonal contact term is -(1/2)delta_0. The first component -R1R2 has no contact term. Conjugating by w_R does not change the local multiplier -(1/2)rho_y. It cancels exactly from D_R.

For completeness, boundedness of Q_w at a<2 can be seen directly from the odd angular blocks, without applying the ordinary unrestricted Muckenhoupt range. If B=(partial_x-i partial_y)/(partial_x+i partial_y), then on a real input U2+iU1=-(I+B)/2. For angular mode m, write n=m-1, t=log r and F(t)=r f_m(r). The radial block of B is

F(t)-2n int_0^infinity exp(-nv)F(t+v)dv, n>0,
F(t)+2n int_0^infinity exp(nv)F(t-v)dv, n<0,
F(t), n=0.

These formulas follow by solving g'-ng/r=f_m with the regular endpoint at zero for n<0 and the decaying endpoint at infinity for n>0, then applying the other first-order derivative. For odd m, nonzero |n| is at least2. The weight ratios obey w(t)/w(t+v)<=exp(av) and w(t)/w(t-v)<=1. The forward block norm is at most 1+2n/(n-a)<=1+4/(2-a), the backward block norm is at most3, and the remaining block is the identity. Angular orthogonality and the real identity for U therefore give

||w_R U[w_R^-1 phi]||_2 <= [1+2/(2-a)]||phi||_2.         (4)

The scalar-to-vector norm is meant in (4). Finite angular sums on compact annuli are dense, defining the canonical extension. The limit agrees locally as a distribution with the ordinary canonical transform of the compact approximants. Multiplication by bounded A proves boundedness of Q_w.

Away from x=y, Sym Q_w has kernel (1/2)[t A(x)+t^-1 A(y)].u(x-y), where t=w_R(x)/w_R(y). Subtracting Sym Q gives (1/2)B_R.u(x-y). The coefficient satisfies B_R(x,-y)=B_R(x,y), because A and w_R are centrally even. On an odd input, antisymmetrizing in y therefore gives (2). This also proves symmetry, since B_R is symmetric in x,y and u is even. The estimates below justify the manipulations first with compact smooth inputs and then on L2.

## 3. Quantitative Hilbert-Schmidt proof

Scaling x=RX,y=RY and applying the unitary dilation phi(x)->R phi(RX) reduces the proof to R=1 with coefficient A_R(X)=A(RX). The kernel u has degree -2, and the R^-2 kernel factor cancels the four-dimensional measure in the squared Hilbert-Schmidt norm. We consequently use x,y for the rescaled variables.

The vector kernel satisfies exactly

|u(z)|=1/(2pi|z|²), ||Du(z)||_op=1/(pi|z|³).             (5)

The derivative identity follows by differentiating its polar form r^-2(-sin2theta,cos2theta)/(2pi); its radial and angular derivative columns are orthogonal and have the same length.

First suppose <x>/2 <= <y> <= 2<x>. Set d=min(|x-y|,|x+y|). If d<=<x>/4, replace y by -y if necessary to make |x-y|=d. This changes neither B nor any coefficient bound. Along the segment from x to y the bracket norm is between (3/4)<x> and (5/4)<x>. Since t=(<y>/<x>)^a,

|t-1| <= (4a/3)d/<x>, t^-1 <= (4/3)^a,
|A(x)-A(y)| <= C1(4/3)^(1+delta)d <x>^(-1-delta).

Use the exact second-order cancellation

B=(t-1)(A(x)-A(y))+[(t-1)²/t]A(y).

It yields |B|<=B_near d²<x>^(-2-delta). Each of the distances |x-y| and |x+y| is at least d, so (2),(5) give |D_R(x,y)|<=C_near<x>^(-2-delta). The estimate remains valid where the two small-distance regions overlap near the origin. It does not bound only one singularity while ignoring the other.

If d><x>/4, then t and t^-1 are at most2^a. Hence |B|<=(2^a+1)(1+2^delta)C0<x>^-delta. Both kernels in (2) are at most8/(pi<x>²), so |D_R|<=C_away<x>^(-2-delta). Combining these estimates and bounding the admissible y area by4pi<x>² gives a squared integral over the comparable region of at most

4pi C_comp² int_R² <x>^(-2-2delta)dx
=4pi² C_comp²/delta.                                    (6)

Next suppose <x>>2<y>. Then |x|>=sqrt(3), |y|<|x|/2 and <x>/|x|<=2/sqrt(3). The mean-value estimate using (5) gives

|u(x-y)-u(x+y)| <=16|y|/(pi|x|³).

Also |B|<=2C0<x>^a<y>^(-a-delta). Consequently

|D_R(x,y)| <= C_far |y|<x>^(a-3)<y>^(-a-delta).          (7)

For fixed y, direct radial integration gives

int_(<x>>2<y>) <x>^(2a-6)dx
=pi 4^(a-2)<y>^(2a-4)/(2-a).

The remaining y integral is

int_R² |y|²<y>^(-4-2delta)dy=pi/[delta(delta+1)].

The transposed far region contributes the same amount. Adding it to (6) proves (3). Here a<2 comes from far input-output separation, while delta>0 comes from decay along the comparable region. Without the odd kernel difference, the factor |y|/|x| would be absent and the same proof would stop at a<1. Thus parity is used quantitatively at the large-distance step as well as at the origin.

## 4. The signed principal matrix after weighting

Assume now that rho is a smooth S1 reference, u=U[rho] is smooth and globally Lipschitz, V=cx+u is complete and at most linear, div V=2c, and c>0. Define the bounded even scalar

b_R=-V.Dlog w_R=a(c|x|²+x.u)/(R²+|x|²).                 (8)

Suppose b_R-b_infinity is in C0 and Db_R is in L2 for some constant b_infinity. For the sublinear reference asymptotics u=O(r^(1-delta)), Du=O(r^-delta), one has b_infinity=ac and these hypotheses hold.

Define the unweighted signed remainder

K_rho=(1/2)[R1,[R1,rho_y]]-(1/2)[R1,[R2,rho_x]],
P_rho=R1 rho_y R1-(R1 rho_x R2+R2 rho_x R1)/2.

The double-commutator argument in ../double_commutator/PROOF.md shows that K_rho is Hilbert-Schmidt under (1). Under the gradient approximation hypotheses in ../gradient_commutator_audit/PROOF.md its exact Hilbert-Schmidt norm is the separately audited formula there. In all cases needed here, bounded coefficients tending uniformly to zero and L2 first derivatives suffice for a finite bound.

For the scalar weight term put

K_b=(1/2)sum_(j=1)^2 [R_j,[R_j,b_R]],
S_b=-sum_(j=1)^2 R_j b_R R_j.

Since sum R_j²=-I, direct expansion gives K_b=S_b-b_R, so b_R=S_b-K_b. This sign matters. Constants commute, so K_b depends only on b_R-b_infinity. It is self-adjoint and Hilbert-Schmidt. A direct proof of finiteness is to write its Fourier kernel

-[|v(xi)-v(eta)|²/(2(2pi)²)] hat b_R(xi-eta), v(xi)=xi/|xi|.

For q=xi-eta, the integral of |v(eta+q)-v(eta)|⁴ over eta is finite and bounded by68pi|q|²: use the bound2 on |eta|<=2|q| and 2|q|/|eta| outside. Plancherel gives ||K_b||_HS²<=(17/(4pi))||Db_R||_2². The exact integration in ../double_commutator/PROOF.md sharpens this to the identity

||K_b||_HS²=(4log2-1)/(8pi)||Db_R||_2².                  (9)

The crude finite bound already suffices for the theorem. To extend from compact coefficients, cut off b_R-b_infinity and mollify. The coefficient converges uniformly; its derivative converges in L2, since the cutoff gradient error is bounded by a constant times the coefficient supremum on an escaping annulus. Thus the Hilbert-Schmidt and operator limits agree.

For phi=w_R h, the symmetric energy of L=V.D-1+Q is now exactly

Re <w_R L w_R^-1 phi,phi>
=-(c+1)||phi||_2²+< (S_b+P_rho)phi,phi>
  +<K_eff phi,phi>,
K_eff=K_rho+D_R-K_b.                                    (10)

The local contact term of Q has already been retained in the identity Sym Q=P_rho+K_rho. It is not discarded or counted twice in (10). The principal quadratic form is

int [R1phi,R2phi] M_R(x) [R1phi,R2phi]^T dx,
M_R=[[b_R-rho_y,rho_x/2],[rho_x/2,b_R]].

Its largest eigenvalue is

lambda_R(x)=b_R(x)+(sqrt(rho_x²+rho_y²)-rho_y)/2.         (11)

Unlike separate supremum bounds, (11) charges the weight drift and the signed coupling at the same spatial point. At infinity lambda_R tends to ac; at a positive-slope S1 origin it equals zero. These limiting observations do not certify the global supremum.

## 5. Conditional low inverse certificate

Let K_F be a finite-rank self-adjoint operator on S1 L2 with a certified error ||K_eff-K_F||<=epsilon. Let Lambda_F be an upper bound on its spectrum as an operator on the entire S1 space; in particular Lambda_F must be at least zero, because it acts by zero off a finite-dimensional subspace. Suppose a certified bound Lambda_pr>=ess sup lambda_R is available and

beta=c+1-Lambda_pr-Lambda_F-epsilon>0.                  (12)

Then the maximal distributional realization of L on the real S1 space L2(w_R²dx) generates a strongly continuous semigroup of norm at most exp(-beta t). It is bijective from its generator domain onto that weighted space, and ||L^-1||<=1/beta.

Indeed the complete Lipschitz flow supplies the transport generator; conjugation adds the bounded scalar b_R. Equation (4) makes Q_w a bounded perturbation. The compact smooth S1 core is a graph core by spatial cutoff and mollification; no derivative norm of an arbitrary low-space input is assumed. Equations (10)-(12) bound its energy by -beta||phi||² and extend in graph norm. The semigroup estimate follows by differentiating smooth-domain orbits and density. The negative time integral of the semigroup converges in operator norm, is a right inverse into the domain by the closed generator property, and is a left inverse there by orbit differentiation. A kernel vector would have a constant orbit subject to strict decay and hence vanish.

The Hilbert-Schmidt results ensure existence of finite-rank approximants. They do not certify a useful particular K_F. For example, approximate an L2 kernel by a finite rectangular simple-function kernel and symmetrize; projection onto S1 preserves finite rank and does not increase the error. A computable application must certify the full kernel error, including the exterior and near both singular sets, and the finite matrix eigenvalues. A finite Galerkin matrix without an operator error does not establish (12).

## 6. Perturbation, membership and open high-space work

If W is an S1-compatible globally Lipschitz odd divergence-free field with ||DW||_infinity<=D, conjugating W.D adds only the scalar -W.Dlog w_R. Since W(0)=0 and |W(x)|<=D|x|, its absolute value is at most aD. The same low theorem then has rate beta-aD when positive.

For a correction z and a differentiable g with ||Dg||_infinity<=D, (4) gives

||w_R U[z].Dg||_2 <= [1+2/(2-a)]D||w_R z||_2.

This would yield a low contraction constant at most [1+2/(2-a)]D/(beta-aD) if an independent high inverse, invariant high ball, trace control and completeness argument were established. None of those high-space steps is asserted here.

A nonzero smooth exterior power r^q belongs to the weighted L2 space exactly when q<a-1. For the original leading residual q=2gamma-1, gamma=1/c, this requires a>2gamma. Positive far-field principal decay requires ac<c+1, or a<1+gamma. Thus the open interval

2gamma<a<1+gamma

is compatible with both conditions when gamma<1. For state131, a=7/5 lies in this interval. The original coarse low inverse T4-022 imposed a<beta0/c after separately subtracting the two worst constants. The local principal test (11) does not impose that additional bound. It also does not prove that any R, including R=1, actually satisfies (12).

The practical next tasks are a global bound for (11), a finite-rank certificate for K_eff if that bound leaves room, and a compatible weighted high-space estimate. A numerical principal screen alone is insufficient for an inverse or an existence claim.
