# Forcing norms and distances of the normalized tail repairs

Status: complete informal argument written before the new computation.
This theorem concerns the exact trials of topics 15, 103, 104, 105 and
106. It is not a stationary-profile theorem or a decisive endpoint.

## 1. Exact objects, hypotheses and conclusions

Let rho0 denote the normalized modal trial of modal_repair/PROOF.md,
including its canonical velocity U0 and c0=1/k. The exact input is
k=1615536043799051/9007199254740992, so 0<k<1/4. Set beta=2k-1.
The fully audited far_residual_obstruction theorem, including its
mandatory addendum, gives, uniformly on the circle,

 epsilon0=(c0 X+U0).grad rho0-rho0
          =r^beta Epsilon(theta)+o(r^beta),
 rho0=r^k Theta0(theta)+o(r^k),  grad rho0=O(r^(k-1)).             (1)

Epsilon is a finite sine polynomial. Its coefficient of sin(theta),
with normalization E0=(1/pi) integral Epsilon sin(theta) dtheta, lies
strictly between -0.03688201144 and -0.03688201143. These numbers are
outward bounds on the same exact E0, not its definition. In particular
Epsilon is nonzero. The two-method data audit for (1) is a dependency.

Write rho_T^(1) for the single-tail repair of normalized_tail_repair,
and rho_T^(3) for the three-tail repair of hminus1_tail_repair. Their
PROOF.md files and mandatory addenda are dependencies. Both are defined
for T>=max(R_b,L,1), with the same exact c0. Put

 q_T^(j)=rho_T^(j)-rho0,
 epsilon_T^(j)=(c0 X+U[rho_T^(j)]).grad rho_T^(j)-rho_T^(j).

The first residual is in L2 for every such fixed T. The second satisfies
r epsilon_T^(3) in L2 and hence is in L2 and dot H^-1 for every fixed T.
Here the inhomogeneous H^1 norm is (||phi||2^2+||grad phi||2^2)^(1/2),
H^-1 is its dual, and dot H^-1 has the test-functional definition

 ||f||dotH^-1=sup{|<f,phi>|:phi in C_c^infty,||grad phi||2<=1}.

Then:

(a) epsilon0 is in neither L2, H^-1 nor dot H^-1. In the weighted space
L2(<r>^(-2sigma)dX), it belongs exactly when sigma>2k.

(b) For either j=1 or j=3, and any fixed 0<a<b<1,

 T^(-2k)||epsilon_T^(j)||L2(aT<r<bT)
   -> [integral_a^b s^(2beta+1)ds integral_0^(2pi) Epsilon^2 dtheta]^(1/2)>0.
                                                                    (2)

There are explicit constants C_L,C_D>0 below, depending only on k and E0,
such that for both repairs

 liminf_(T->infinity) T^(-2k)||epsilon_T^(j)||L2 >= C_L,
 liminf_(T->infinity) T^(-2k)||epsilon_T^(j)||H^-1 >= C_L,           (3)

and for the three-tail repair

 liminf_(T->infinity) T^(-(2k+1))||epsilon_T^(3)||dotH^-1 >= C_D.    (4)

Thus neither qualitative forcing membership nor small weighted factor
change supplies a small forcing norm for this outward-moving family.
These are asymptotic lower bounds, without an evaluated finite T threshold,
a global norm asymptotic equality, a monotonicity claim, or an upper bound.
No dot H^-1 membership assertion is made here for the single-tail repair.

(c) For either repair and each fixed T,

 q_T^(j) in L2(<r>^(-2sigma)dX) iff sigma>2k,
 X3-rho_T^(j) in L2(<r>^(-2sigma)dX) iff sigma>1+k.                 (5)

In particular X3 belongs to no affine unweighted H^s class about either
repair with s>=0. The repairs retain their previously proved weighted
factor convergence to rho0. These facts do not exclude any justified
weighted neighborhood of X3.

(d) The kinematic P2 conditions for rho0 itself were proved in topic15,
modal_repair/PROOF.md, section Admissibility and residual scope. The center
factor is continuous with value one; the density is C^(2,alpha)_loc for
every alpha<1, the parities and canonical velocity hold, and the density
and first derivative have growth exponent k<1. Its equation is not proved,
so membership in the stationary class P2 is not asserted.

## 2. Exact canonical scaling and the unchanged annulus

Use b(s), chi(s) and J_b exactly as defined in topics105 and106. For any
one of their angular corrections H_i at exponent a_i, define the fixed
function, with Y=(u,v) and s=|Y|,

 Q_i(Y)=chi(s)s^a_i H_i(arg Y)
             -(4 I_i J_i/J_b) u^2 v b(s),                       (6)
 I_i=(1/pi) integral sin(3theta)H_i(theta)dtheta,
 J_i=integral_1^infinity chi(s)s^(a_i-2)ds.

These are well-defined canonical densities for the finite angular modes
and powers in question. They vanish for s<=1 and have sublinear growth.
Their canonical velocities V_i are smooth on every compact subset of
s<1. Substitution of the exact lambda_T formulas proves

 q_T^(1)(X)=T^beta Q_1(X/T),
 q_T^(3)(X)=sum_(i=1,2,d) T^a_i Q_i(X/T),
 a_1=beta, a_2=3k-2, a_d=k-2.                                  (7)

Q_1 here is the correction formula at unit scale. It is not an assertion
that the complete trial construction meets its T>=R_b hypothesis at T=1.

To verify velocity scaling, if -Delta psi_i=partial_u Q_i and
V_i=(-partial_v psi_i,partial_u psi_i), then
T^(a_i+1) psi_i(X/T) solves the stream equation for T^a_i Q_i(X/T).
Its velocity is T^a_i V_i(X/T). It has the required parity and sublinear
spatial growth for each fixed T. Any difference from the canonical
velocity is an entire harmonic sublinear vector field, hence constant;
the required component parities force that constant to vanish. This is
the canonical uniqueness statement proved in the dependencies. Therefore

 U[q_T^(1)](X)=T^beta V_1(X/T),
 U[q_T^(3)](X)=sum_i T^a_i V_i(X/T).                             (8)

On the fixed scaled annulus a<=|Y|<=b<1, every density correction and its
first derivatives vanish. Since a_2,beta and a_d obey a_2<beta, a_d<beta,
and the V_i are bounded there, (8) is O(T^beta). By (1), uniformly there,

 epsilon_T^(j)(TY)=epsilon0(TY)+U[q_T^(j)](TY).grad rho0(TY),
 T^(-beta)epsilon_T^(j)(TY)
       =|Y|^beta Epsilon(arg Y)+o(1)+O(T^(k-1))
       -> |Y|^beta Epsilon(arg Y).                              (9)

All constants are for this fixed annulus. Uniform convergence and the
change of variables dX=T^2 dY give (2), because beta+1=2k.
No estimate of the velocity in a moving transition layer is needed.

## 3. Tests for negative norms and explicit lower constants

Choose a=1/4, b=1/2 and

 g(s)=(s-a)^2(b-s)^2 on [a,b], zero elsewhere,
 phi(Y)=g(|Y|)sin(arg Y).

This compactly supported C1 function is in H^1. It can be approximated
in H^1 by smooth functions with support in a fixed slightly larger
annulus. Every residual in use is locally L2. Hence its pairings with
these approximations converge, and the dual norm inequalities for
smooth tests apply to phi and its scaled versions. This also suffices
for the contradiction arguments when assuming a finite negative norm.
Define the exact positive numbers

 A=integral_a^b g(s)^2 s ds,
 B=integral_a^b [g'(s)^2 s+g(s)^2/s]ds,
 J=integral_a^b g(s)s^(2k)ds,
 C_L=sqrt(pi)|E0| J/sqrt(A),
 C_D=sqrt(pi)|E0| J/sqrt(B).                                    (10)

The angular integrals of sin^2 and cos^2 are pi, so
||phi||2=sqrt(pi A) and ||grad phi||2=sqrt(pi B). Put
Phi_T(X)=phi(X/T) and Psi_T(X)=T^(-1)phi(X/T). Their norms are exactly

 ||grad Phi_T||2=sqrt(pi B),
 ||Psi_T||H1=sqrt(pi A+T^(-2)pi B),
 ||Psi_T||2=sqrt(pi A).                                         (11)

For the original residual, (1) yields

 <epsilon0,Phi_T>=pi E0 J T^(beta+2)+o(T^(beta+2)),
 <epsilon0,Psi_T>=pi E0 J T^(beta+1)+o(T^(beta+1)).                (12)

Both exponents are positive. The first formula contradicts boundedness
on dot H^1, while the second contradicts boundedness on H^1 or on L2.
The tests have zero integral by angular oddness; no constant gauge
ambiguity is used in the homogeneous claim.

For either repaired residual, (9) gives exactly the same limits in (12)
with epsilon0 replaced by epsilon_T^(j). Applying the dual norm
inequalities and (11), dividing by the appropriate power of T, and
taking liminf proves (3),(4). Finiteness of the norms in (3) follows
from L2 membership. Finiteness in (4) is the topic106 result. The exact
annular limit in (2) may give a larger lower bound than this one test;
no equality of C_L with that limit is claimed.

The new finite computation will enclose A,B,J,C_L,C_D twice. One method
uses exact rational polynomial antiderivatives followed by Arb balls.
The other uses mpmath.iv composite Simpson integration of g(s)s^(2k),
with the proved remainder below and independent exact moment formulas.
For N even subintervals of width h=(b-a)/N, the Simpson remainder is at
most (b-a)h^4 sup|F''''|/180 for F(s)=g(s)s^(2k). To justify it, the
one-panel functional annihilates polynomials of degree three; integrating
the fourth-order Peano kernel on the symmetric two-subinterval panel
gives magnitude h^5/90 and one sign. Summing N/2 panels gives the stated
constant. The fourth derivative is bounded by the full Leibniz sum
sum_(j=0)^4 binom(4,j)|g^(4-j)| |(2k)...(2k-j+1)| s^(2k-j).
All interval endpoints and remainder directions must be retained.

## 4. Sharp weighted thresholds and regularity scope

For fixed T the compact compensators vanish outside2T. By the exact
formulas of the two constructions,

 q_T^(1)=r^beta H1,
 q_T^(3)=r^beta H1+r^(3k-2)H2+r^(k-2)Hd   for r>=2T.             (13)

H1=k Epsilon/(1-k) is nonzero. Thus r^(-beta)q_T^(j) tends uniformly
to the same continuous nonzero H1. At infinity <r> is comparable to r,
and a uniform nonzero angular limit gives a positive angular L2 lower
bound as well as a finite upper bound for all sufficiently large r.
The weighted radial integral is therefore comparable to
integral r^(2beta+1-2sigma)dr. It converges exactly when
sigma>beta+1=2k, including divergence at equality. Compact integrability
is automatic for these continuous corrections. The same argument with
(1) proves the original residual threshold in(a).

Topic103 proves uniformly that r^(-k)(X3-rho0) tends to a continuous
nonzero angular function Delta. Equation(13) and beta<k show that the
same Delta is the limit for X3-rho_T^(j). Compact integrability is
unchanged. The radial test now gives exactly sigma>1+k. Since an
inhomogeneous H^s function for s>=0 is in L2, the Sobolev statement follows.

For completeness, the topic15 kinematic argument needs no regular
Cartesian factor at the center. Each nonconstant homogeneous core
factor has degree at least2 and is smooth on the circle. Multiplication
by x^2 y gives degree at least5, so the density has locally Lipschitz
second derivatives there and is C^(2,alpha) for every alpha<1. The inner
logarithmic rows have still higher orders. Away from the origin, exact
joins and simple spline knots give C6. The finite exterior representation
gives |rho0|+(1+r)|grad rho0|<=C(1+r)^k. The separately proved canonical
inverse supplies its unique sublinear velocity, with no harmonic xy
freedom. None of these kinematic statements proves stationarity.

## 5. Evidentiary and endpoint scope

Dependencies are the exact normalized trial, the independently certified
nonzero E0 and exterior expansion, the two exact normalized tail
constructions, and the X3-modal leading-profile separation. Their current
hashes and whole evidence maps must be checked. A fresh coefficient of a
higher residual row is not assumed known. In particular this theorem
proves no necessity of either added counterterm in topic106, nor failure
of dot H^-1 membership for the topic105 residual.

The new interval constants are asymptotic lower bounds only. A fixed
large T for which a particular lower bound already holds is not supplied.
All finite full-grid audits, the global inverse, nonlinear estimates,
and every decisive endpoint remain separate open obligations.
