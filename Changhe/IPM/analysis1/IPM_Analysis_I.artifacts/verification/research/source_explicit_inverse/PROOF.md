# An explicit compact cutoff and a numerical auxiliary source inverse

## Statement, exact data and scope

Use the exact normalized modal_v2 trial, canonical velocity, source P=(p,0),
D=DV(P)=diag(A,mu), g=rho_y(P), and delta=33/2000. The independently
checked topics84,85,89 give on B_(3delta)(P)

 M_V=743/2500 > sup||D^2V||_F,
 M_rho=5059/10000 > sup||D^2rho||_F,
 A in[10,10.2], mu in[.99,1.01], g in[29,30].

All tensors use the full ordered Frobenius norm. The canonical density
moment archive in topic85 supplies the exact polynomial boxes and moment
anchors on seven original knot spans covering this disc's radial range.
These are imported audited dependencies; no second whole-plane Green
integration is claimed here. The following finite computation independently
bounds D^j rho, j=3,4,5, and D^j U, j=3,4, on this disc. Its analytic bounds
are also stated for arbitrary admitted interval polynomial/moment inputs.

Use the unitary Fourier transform on R^2 and J^s=(1-Delta)^(s/2).
For s in[61/20,31/10], define w=theta(V-D(X-P)),
q=theta(grad rho-(0,g)), and the auxiliary whole-plane operator

 A_s u=(D(X-P)+w).grad u-u-gM u+q.U[u],
 Mhat=xi_1^2/|xi|^2, Uhat=(xi_1 xi_2,-xi_1^2)/|xi|^2,
 D(A_s)={u in H^s:(D(X-P)+w).grad u in H^s in distributions}.

The cutoff below makes w,q compact C^4. The theorem of topics78,92 applies
with kappa(s)=1301/200-101s/100 and

 E_s <= delta [(12s+9/2)M_V+3M_rho] =: E_s^*,
 a_s=kappa(s)-E_s^*>0,
 d_s >= (101s-1)/100 =: d_s^*>0.

A computed finite R_s^* from the formulas below gives the actual bound

 ||A_s^(-1)||_(H^s->H^s) <= (1+R_s^*/d_s^*)^s/a_s.       (1)

This is the auxiliary operator only. Its compact cutoff changes the trial
away from the source. It omits the physical scalar strain rank-one term.
No global IPM inverse, outer matching, residual closure or endpoint follows.
We make no claim that the necessarily coarse bound is small enough to use
in a nonlinear existence argument. The local forcing constant 1/a_s remains
distinct from the inverse norm in(1).

## 1. An explicit C^4 cutoff with the required gradient bound

Put S(t)=35t^4-84t^5+70t^6-20t^7 on[0,1]. It has
S(0)=0,S(1)=1 and its first three derivatives vanish at both ends.
Also S'(t)=140t^3(1-t)^3>=0, so0<=S<=1; symmetry gives
S(1-t)=1-S(t) and integral_0^1 S=1/2.
Define a C^3 function b on the line by zero outside[0,1] and

 b(t)=(4/3)S(4t),                 0<=t<=1/4,
 b(t)=4/3,                       1/4<=t<=3/4,
 b(t)=(4/3)S(4(1-t)),            3/4<=t<=1.

The zero derivatives through order3 match at every join, including outside.
Its integral is(4/3)(1/8+1/2+1/8)=1. Therefore
chi(t)=1-integral_0^t b(v)dv is1 for t<=0,0 for t>=1,
C^4, decreasing, and between0 and1. Set

 a=273/64, R_c=23delta/8,
 theta(P+z)=chi((|z|^2/delta^2-4)/a).

It equals1 on B_(2delta)(P) and has support inside the closed disc of
radius R_c<3delta, hence compactly inside B_(3delta)(P). It is C^4
also across each circular join, by the matching of chi derivatives.
The gradient bound is

 delta||grad theta|| <= (4/3)(2*(23/8)/a)=1472/819<2.      (2)

For a finite bound on higher derivatives set L_0=1,L_1=4/3 and, for
j=2,3,4, let

 L_j=(4/3)4^(j-1) sum_(k=j-1)^7 |S_k| k!/(k-j+1)!.

Because0<=t<=1 on each ramp, L_j bounds |chi^(j)| everywhere. Define
u=2*(23/8)/a, v=3/a; since2sqrt(2)<3, the quadratic cutoff coordinate
has first derivative norm<=nu/delta and second derivative norm<=v/delta^2.
Its higher derivatives vanish. For j=1,...,4, the chain rule by singleton
and pair partitions gives the valid tensor bound

 C_j=sum_(l=0)^floor(j/2) j!/[2^l l!(j-2l)!]
                  L_(j-l) nu^(j-2l) v^l,
 ||D^j theta||_F <= C_j delta^(-j).                      (3)

Use the sharper C_1=1472/819 from(2); C_0=1. Formula(3) follows by
counting partitions with l pairs and j-2l singletons. Each symmetrized
product is bounded by the product of Frobenius norms. All constants in(2)
and(3) are rational. No unbounded smooth-step derivatives are hidden.

## 2. Canonical polynomial and moment envelopes

On one original span[a,b], with center t_c=(a+b)/2 and L=b-a, the imported
H_j(t) are degree7 polynomials in t-t_c with interval coefficients. There
are262 rows, with row261 zero. The canonical moments satisfy

 I_n'=-(2n+4)I_n+H_(n-1),       I_n(a) in the saved left box,
 J_n'=(2n-4)J_n-H_n,          J_n(b) in the saved right box.

They determine rho and psi by

 rho=r^3 sum_(j=0)^260 H_j(t)sin((2j+1)theta),
 psi=(r^4/2)sum_(n=1)^261 (J_n(t)-I_n(t))sin(2n theta).

For every derivative order0,...,4, bound each polynomial derivative
on the entire span. One engine uses Bernstein coefficients on[a,b]; the
other uses absolute monomial coefficient sums on[-L/2,L/2]. Both enclose
the full supplied boxes, not just midpoint polynomials.

For I evolve from a, with lambda=-(2n+4); for J evolve backwards from b,
with lambda=4-2n and positive forcing H_n. If |y0|<=Y0, |forcing|<=M,
variation of constants gives, uniformly for0<=u<=L,

 |y(u)| <= max(Y0, exp(lambda L)Y0+E(lambda,L)M),
 E(lambda,L)=(exp(lambda L)-1)/lambda for lambda!=0,
 E(0,L)=L.                                               (4)

Indeed the scalar majorant solves y'=lambda y+M, has nonnegative initial
value, and is monotone or constant, so its maximum is at an endpoint.
A second, independent bound is exp(|lambda|L)(Y0+L M), obtained by
bounding the integrand before integration. Both are valid regardless of
the signs of the actual functions.

Differentiating the ODE gives, for j>=1,

 D_t^j I=lambda_I^j I+sum_(l=0)^(j-1)lambda_I^(j-1-l)D_t^l H_(n-1),
 D_t^j J=lambda_J^j J-sum_(l=0)^(j-1)lambda_J^(j-1-l)D_t^l H_n.

Taking absolute values with the whole-span envelopes bounds derivatives
through order5. This uses polynomial derivatives only through order4.
Moment endpoints are independent admitted boxes; correlation is unnecessary
for an upper bound. D_t^j(J-I) is bounded by the sum of both magnitudes.

## 3. Cartesian derivatives, independently reconstructed two ways

For f=r^beta F(t)exp(i m theta), put D_+=partial_x+i partial_y,
D_-=partial_x-i partial_y. Direct differentiation in polar coordinates gives

 D_+^u D_-^v f = r^(beta-u-v)exp(i(m+u-v)theta)
   product_(j=0)^(u-1)(D_t+beta-m-2j)
   product_(j=0)^(v-1)(D_t+beta+m-2j)F.                  (5)

The two Cartesian operators commute, and applying them successively proves
(5) by induction. Because each Cartesian derivative is a sum of D_+,D_-
with total absolute coefficient1, every order-k Cartesian component is
bounded by the maximum over u+v=k of the polynomial in(5), with each
D_t^jF replaced by its certified magnitude. The same bound holds for the
sine term by taking imaginary parts. Negative m gives the same maximum,
by interchanging u and v. Summing modes and using |exp(i m theta)|=1 gives
an all-angle bound. Multiplication by2^(k/2) bounds the ordered tensor
norm, since it has2^k components.

The second implementation instead differentiates the actual Cartesian
expression recursively. Represent a term by angular frequency ell and a
polynomial Q(D_t), with common radial power beta-k. The next x derivative
produces half of(D_t+beta-k-ell)Q at ell+1 and half of
(D_t+beta-k+ell)Q at ell-1. The next y derivative produces those same
terms with coefficients1/(2i), -1/(2i), respectively. Combining each
identical angular frequency before taking absolute values yields direct
bounds for every mixed derivative partial_x^u partial_y^(k-u). Then the
exact ordered tensor sum has binomial(k,u) copies of that component.
This second algorithm uses no ladder product from(5).

Use beta3,m=2j+1,F=H_j for rho. Use beta4,m=2n,F=J_n-I_n and the factor1/2
for psi. Orthogonality of the constant rotation U=grad_perp psi gives

 ||D^j U||_F=||D^(j+1)psi||_F.

This supplies the required rho orders3,4,5 and velocity orders3,4. For
rho order5 its H polynomial derivatives through order5 are needed and
are available exactly (this is separate from the order4 requirement for
moment forcing). All radial powers take their maximum over the span's
full exact radial interval. The seven spans cover the source disc radially,
and the estimates hold at every angle, so the whole disc is covered.
All endpoint exponentials and square roots use directed arithmetic.

## 4. H^4, Fourier moments and the auxiliary inverse constant

Let r0=3delta. Write v0=V-D(X-P), q0=grad rho-(0,g). The mean-value theorem
and the independently certified Hessians give pointwise tensor bounds

 B_v,0=M_V r0^2/2, B_v,1=M_V r0, B_v,2=M_V,
 B_v,3=sup||D^3U||_F, B_v,4=sup||D^4U||_F,
 B_q,0=M_rho r0, B_q,1=M_rho,
 B_q,j=sup||D^(j+1)rho||_F, j=2,3,4.

For z=w or q put

 B_w,j=sum_(k=0)^j binom(j,k) C_k delta^(-k) B_v,j-k,
 B_qcut,j=sum_(k=0)^j binom(j,k) C_k delta^(-k) B_q,j-k.

The ordered Leibniz rule and tensor Cauchy-Schwarz prove these bounds.
For a compact vector field z supported in B_(r0), Plancherel and the
binomial expansion of(1+|xi|^2)^4 give

 ||z||_H4^2=sum_(j=0)^4 binom(4,j)||D^jz||_L2,F^2
             <=pi r0^2 sum_(j=0)^4 binom(4,j) B_z,j^2.    (6)

C^4 compact fields have all four weak derivatives square-integrable;
there are no surface delta terms at the joins since the derivatives match.
Put the square-root bounds in(6) equal to H_w,H_q. For r=1,2, Fourier
Cauchy-Schwarz on R^2 gives

 W_r(z_i)=(2pi)^(-1)int <xi>^r |z_i_hat|
 <=alpha_(4-r)||z_i||_H4,
 alpha_t=[2sqrt(pi(t-1))]^(-1), t>1.

Also ||z_i||_Hs<=||z_i||_H4 for s<=4 and
sum_i||z_i||_H4<=sqrt(2)||z||_H4. Thus the exact commutator constant from
78,92 is bounded by

 R_s^*=sqrt(2) s(s-1)2^(s-4)(alpha_2+beta_(s-1)) H_w
       +sqrt(2) s2^(s-2)(alpha_3+alpha_(s-1)) H_q,
 beta_t=[2sqrt(pi(t-1)(t-2))]^(-1), t>2.                 (7)

All factors are finite on s in[3.05,3.1]. Equations(6),(7), the coefficient
smallness and the maximal-domain semigroup theorem of78,92 give(1).
The exact coefficient boxes, knots, normalization and data hashes are
registered dependencies. The numerical checker writes actual outward
rational bounds and compares both independent methods. It cannot promote
a failed comparison or a floating display to a theorem. This proof is
written before its implementation.
