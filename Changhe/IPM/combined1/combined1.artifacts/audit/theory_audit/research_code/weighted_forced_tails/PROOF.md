# Weighted correction classes force the same nonlinear tail ladder

Status: proposed extension of audited T4-234, OPEN independent Opus
review. This is an analytic classification of finite power expansions.
It supplies no stationary inverse or existence theorem.

## Statement and definitions

Let 0<gamma<1, c=1/gamma, delta=1-gamma, and

    -2<a<=1+gamma,  w_a(X)=(1+|X|^2)^(-a/2),
    E_a=L2(R2,w_a^2 dX),  N_a=floor((2-a)/delta),
    e_j=1-(j+1)delta,  0<=j<N_a.

Densities are real and S1: even in x and odd in y. Let chi(r) be
smooth, zero for r<=1 and one for r>=2. Choose arbitrary smooth S1
angular profiles Theta_j and put R=sum_j chi r^e_j Theta_j. Let Psi_j
be the unique smooth sum of positive even sine harmonics solving

    [partial_theta^2+(e_j+1)^2]Psi_j
        =-e_j cos(theta)Theta_j+sin(theta)Theta_j'.       (1)

The canonical velocity of R is constructed below. On E_a the velocity
U[h] is the continuous extension of the compact smooth Fourier
multiplier with symbol (xi_1 xi_2/|xi|^2,-xi_1^2/|xi|^2). Define
U[R+h]=U[R]+U[h]. Suppose h belongs to the S1 subspace of E_a and
rho=R+h solves

    c div(X rho)-(2c+1)rho+div(U[rho]rho)=0              (2)

in distributions. Every product is locally integrable. Then, for
j=1,...,N_a-1,

    Theta_j=1/[j(c-1)] sum_(l+m=j-1) B_(l,m),
    B_(l,m)=-e_m Psi_l' Theta_m+(e_l+1)Psi_l Theta_m'.   (3)

Conversely, (3) holds if and only if the smooth residual F[R] belongs
to E_a. For each fixed gamma and entire leading profile Theta_0,
(1),(3) uniquely determine every lower profile. Theta_j is homogeneous
of degree j+1 in Theta_0. A nonzero coefficient at the threshold
 e_j=a-1 is included and cannot be absorbed by E_a.

There is also a finite-power extension. Suppose R instead has any
finite set of exponents E in [a-1,gamma], with smooth S1 profiles,
and the same distributional solution property. Then every nonzero
profile has exponent e_j for some 0<=j<N_a, and these profiles obey
(3), taking every absent profile to be zero. Thus introducing a finite
number of additional real powers does not give independent tail
parameters in this range. This statement does not cover logarithms,
infinite asymptotic expansions or remainders outside E_a.

## 1. The canonical weighted multiplier

The audited sharp odd Beurling estimate gives, for 0<b<2,

    ||B||_(L2(w_b^2), centrally odd)=(2+b)/(2-b),
    Bhat=(xi_1-i xi_2)^2/|xi|^2.

For the reciprocal weight w_-b, weighted L2 duality identifies the
norm of B with the norm of its unweighted adjoint B* on L2(w_b^2).
Reflection (x,y)->(x,-y) conjugates B to B* and preserves that radial
weight and the centrally odd subspace. The same norm therefore holds
for w_-b. This duality is first the ordinary integral pairing on
compact smooth odd functions; their density identifies the continuous
extensions. At b=0, Plancherel gives norm one.

For real h, U2[h]+i U1[h]=-(I+B)h/2. Consequently

    ||U[h]||_(E_a;R2)<=2/(2-|a|)||h||_E_a, |a|<2.       (4)

This includes the entire parameter range in the statement, since
1+gamma<2. The local identity term is retained. The extension preserves
divergence, curl and all S1 parities by convergence in local L2. In
particular curl U[h]=-partial_x h and div U[h]=0 distributionally.
No pointwise bound or derivative of h is assumed.

## 2. The compact curl defect and its moments

For every retained exponent, a<=e_j+1<=1+gamma<2 and a>-2. Thus
|e_j+1|<2. The eigenvalues (e_j+1)^2-m^2 for m=2,4,... are nonzero;
division of the rapidly decaying Fourier coefficients proves the
existence, smoothness and uniqueness in (1). This includes e_j=-1.

Put v=grad-perp sum_j chi r^(e_j+1)Psi_j, with
 grad-perp psi=(-partial_y psi,partial_x psi), and

    g=curl v+partial_x R, G(X)=log|X|/(2pi),
    W=grad-perp(G*g), U[R]=v-W.                         (5)

The polar Laplacian and (1) imply that g is smooth, supported in
1<=r<=2 and odd in both x and y. In particular

    integral g=integral x g=integral y g=0.             (6)

For example, xg is odd in y and yg is odd in x. Subtract the constant
and linear Taylor terms of grad-perp G(X-Y) in its convolution with g.
The second derivative of grad G is O(r^-3) when |X|>=4, |Y|<=2.
Taylor's formula with integral remainder and (6) give

    W=O(r^-3), grad W=O(r^-4),                         (7)

uniformly in angle. Higher fixed derivatives satisfy the corresponding
bounds. The constant and first moments in (6) are essential for the
negative-a part of this theorem. A mere O(r^-2) estimate is insufficient
there.

It follows that U[R] is smooth, has divergence zero, curl -partial_x R,
S1 velocity parities and growth O(r^gamma). Outside r=2,

    U[R]=sum_j r^e_j[-Psi_j' e_r+(e_j+1)Psi_j e_theta]
             +O(r^-3).                                (8)

## 3. Uniqueness, cutoff independence and distributional products

A distributional vector field with zero divergence and curl has
harmonic components. Suppose its components have the form d1+d2,
with |d1(X)|<=C(1+r)^gamma and d2 in E_a. The harmonic interior
L1 gradient estimate at a fixed point X0 gives

    |grad d(X0)|<=C L^-3 integral_(B_L(X0)) |d|
       <=C' L^(gamma-1)+C'' L^(max(a,0)-2)||d2||_E_a.

For the second term, use Cauchy-Schwarz and
w_a^-1<=C L^max(a,0) on that ball for L>=2(1+|X0|).
Both powers tend to zero since gamma<1 and a<2. Hence d is constant.
The S1 velocity parities force this constant to vanish. The estimate
follows by differentiating the harmonic mean-value formula; Weyl's
lemma applies to the locally integrable distributional field.

This proves uniqueness in the class O(r^gamma)+E_a. For two cutoffs
with the same tails, R-R_tilde is smooth and compact. The difference
U[R]-U[R_tilde]-U[R-R_tilde] belongs to that class and has zero
divergence and curl. It vanishes by uniqueness. Thus the definition
of U[R+h] is independent of the cutoff representation. Because E_a
embeds continuously in local L2 and the smooth fields are locally
bounded, the products in (2) belong to local L1.

## 4. Weighted residual classification and necessity

The homogeneous product formula gives, outside r=2,

    F[R]=sum_(j=1)^(N_a-1) r^e_j E_j + L,
    E_j=-j(c-1)Theta_j+sum_(l+m=j-1)B_(l,m).            (9)

Every omitted quadratic term has index at least N_a and exponent
below a-1. It therefore belongs to E_a. The error W.grad R has size
O(r^(gamma-4)), also in E_a, since gamma-4<a-1 for a>-2 and gamma<1.
The cutoff region is compact. Hence L belongs to E_a and is a finite
sum of strictly lower powers plus that uniformly smaller error.
A nonzero retained power r^e E belongs to E_a exactly when e<a-1,
as follows from integral r^(2e-2a+1)dr. Dominance of the largest
nonzero exponent proves F[R] in E_a if and only if every E_j=0.

For necessity under (2), suppose j is the first index with E_j!=0.
Let eta>=0 be nonzero, smooth and supported in (1,2), and set
phi_L=L^-1 eta(r/L)E_j(theta). Then

    integral F[R] phi_L=L^(e_j+1)(A+o(1)), A>0.

Write m_L=||w_a h||_(L<r<2L) and n_L=||w_a U[h]||_(L<r<2L).
Both tend to zero by (4). Testing the correction equation, integrating
its divergence terms by parts, and using weighted Cauchy-Schwarz gives

    linear dilation and zeroth order: O(L^a m_L),
    background velocity term: O(L^(a+gamma-1) m_L),
    U[h].grad R term: O(L^(a+gamma-1) n_L),
    quadratic divergence term: O(L^(2a-2) m_L n_L).

On the annulus w_a^-1<=C_a L^a; this holds also for a<0.
Since e_j+1>=a, gamma<1 and a<2, division by L^(e_j+1) makes
every correction tend to zero. This contradicts A>0. The endpoint
e_j+1=a is covered because m_L,n_L themselves vanish. No derivative
of h, finite-radius truncation or pointwise decay of h is used.

The denominator j(c-1) is positive. Induction in (3) now gives
uniqueness, smoothness and the asserted homogeneity of each profile.

## 5. Arbitrary finite real powers

For a finite input set E in [a-1,gamma], adjoin gamma with zero profile
if necessary. Define D={1-e:e in E}. Every element of D is at least
delta>0. Form all finite sums of elements of D that are at most 2-a.
There are only finitely many, because each sum has at most
floor((2-a)/delta) terms. Let Ebar consist of one minus these sums.
Then Ebar contains E and is closed under e+f-1 whenever that result
is at least a-1. Give its newly adjoined exponents zero profiles.

The construction (1),(5)-(8) applies to each exponent q in Ebar,
because a<=q+1<2 and a>-2. For each q the residual coefficient is

    (cq-1)Theta_q+sum_(e+f-1=q)B_(e,f).                 (10)

All products in this sum use e,f>q, since e,f<=gamma<1. The annular
argument forces every coefficient (10) to vanish. At q=gamma its
linear coefficient is zero and the product sum is empty. For q<gamma,
1-cq>0, so (10) determines Theta_q from the strictly larger powers.
Inductively every nonzero larger power lies on the ladder 1-k delta.
Their products again lie on this ladder. A non-ladder q therefore has
zero forcing and zero profile. At q=e_j, (10) is exactly (3).
This proves the finite-power statement, including missing ladder
profiles: their forced values must equal their prescribed value zero.

## Scope and application warning

The result is conditional only on the explicitly stated expansion,
canonical velocity convention and weak equation, not on a small norm.
It rules out an entire affine E_a class when its retained profiles
violate (3). It does not order distances between references and does
not establish that any compatible class contains a solution.

For a<0, regularized basis functions may contribute additional powers
such as e_j-2. A candidate's leading branch endpoints alone are then
insufficient to identify its E_a class. One must include every actual
power above a-1 and check its coefficients before applying Section5.
No negative-a claim about candidate007 is made here.

Dependencies: the audited odd Beurling estimate in
../sharp_weighted_velocity/PROOF.md, harmonic mean-value theory, the
explicit moment cancellation (6), and the annular argument of audited
T4-202. The a=0 ladder case is audited T4-234. No computation or
external theorem about IPM existence is used.
