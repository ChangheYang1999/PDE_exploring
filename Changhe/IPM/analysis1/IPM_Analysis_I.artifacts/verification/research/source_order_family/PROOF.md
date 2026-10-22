# Source estimates for Sobolev orders from 3.05 to 3.1

## Statement and scope

Let s be any real number in [61/20,31/10] and let t=s-1. On R^2 use
J^s=(1-Delta)^(s/2), the H^s norm ||J^s u||_2, and the unitary Fourier
transform (2pi)^(-1) integral exp(-i X.xi)u(X)dX. Derivative tensors have
Frobenius norms, vectors Euclidean norms. Let D=diag(A,mu), where

 10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30.

For real w,q in C_c^4(R^2), define b=D(X-P)+w and

 A_s u=b.grad u-u-g M u+q.U[u],
 Mhat(xi,eta)=xi^2/(xi^2+eta^2),
 Uhat(xi,eta)=(xi eta,-xi^2)/(xi^2+eta^2).

The differential expression is independent of s; its space and domain
vary with s. Values at the single frequency zero are immaterial. Put

 kappa(s)=1301/200-(101/100)s,
 E_s=||div w||infinity/2+s||Dw||infinity,F+||q||infinity,
 a_s=kappa(s)-E_s,
 a0=1+(A+mu)/2-||div w||infinity/2-||q||infinity,
 d_s=a0-a_s=1+(A+mu)/2-kappa(s)+s||Dw||infinity,F.

For compact coefficients set

 W_r(f)=(2pi)^(-1) integral <xi>^r |fhat(xi)|d xi,
 alpha_r=[2sqrt(pi(r-1))]^(-1), r>1,
 beta_r=[2sqrt(pi(r-1)(r-2))]^(-1), r>2,
 P_s(f)=s 2^(s-2)[W_1(f)+alpha_(s-1)||f||Hs],
 T_s(w)=s(s-1)2^(s-4)sum_i[W_2(w_i)+beta_(s-1)||w_i||Hs],
 R_s=T_s(w)+sum_i P_s(q_i).

If E_s<kappa(s), the maximal distributional realization

 D(A_s)={u in Hs: b.grad u in Hs}

generates a strongly continuous semigroup satisfying

 ||exp(tau A_s)||_(Hs->Hs)
 <=(1+R_s/d_s)^s exp(-a_s tau), tau>=0,
 d_s>=(101/100)s-1/100>=6141/2000.

It is invertible onto Hs, with norm at most

 (1+R_s/d_s)^s / a_s.                                   (1)

This is the auxiliary cut-off source operator. It is not the complete
normalized IPM linearization. The source-local estimate (26) of topic77,
with its stated cutoffs, norms and graph completion, also holds at each
such s, with t=s-1, kappa replaced by kappa(s), and every explicitly defined
constant in that formula evaluated at s. In particular its forcing
coefficient is K1(s)=1/a_s; it is not the inverse norm in (1).

For the actual normalized trial and delta=33/2000, topic89 provides the
exact source P, this A,mu,g box, constant divergence A+mu, C4 velocity and
C5 density on B_(3delta)(P), and 3delta<p/2. Topics84 and85 give on that ball

 M_V=sup||D^2 V||F<743/2500,
 M_rho=sup||D^2 rho||F<5059/10000.

Choose 0<=theta<=1, theta=1 on B_(2delta), support strictly inside
B_(3delta), C_theta=delta||grad theta||infinity<=2, and let
w=theta(V-D(X-P)), q=theta(grad rho-(0,g)). Then throughout this s interval

 E_s<C_*(s)delta,
 C_*(s)=(12s+9/2)(743/2500)+3(5059/10000),
 K1(s)<1/[kappa(s)-delta C_*(s)]<3181/10000.               (2)

At s=153/50=3.06 the exact kappa is2134/625 and the multiplier of M_V
in C_V is2061/50=41.22. The exact arithmetic checker supplies C_*, E_*,
a_*=kappa-E_*, their outward decimal ceilings, and a sharper K1 ceiling.
No value for R_s, no rank-one denominator, no outer inverse and no
contraction is certified here.

## Frozen Fourier calculation and the uniform box minimum

For Schwartz u, Fourier integration by parts gives the Hs energy density

 -1-(A+mu)/2+s(A xi^2+mu eta^2)/(1+xi^2+eta^2)
                   -g xi^2/(xi^2+eta^2).

The positive transport fraction is bounded above by its homogeneous
version because A,mu,s are positive. Writing v=xi^2/(xi^2+eta^2), the
negative homogeneous density is the affine interpolation of

 kslow=1+A/2+(1/2-s)mu,
 kfast=1+(1/2-s)A+mu/2+g.

Since s>1/2, exact minimization over the box gives

 min kslow=1301/200-(101/100)s,
 min kfast=7119/200-(51/5)s.

Their difference is2909/100-(919/100)s, decreasing in s. Its smallest
value on our interval is601/1000>0. Thus kappa(s) is precisely the uniform
box margin, not merely a bound from sample frequencies. Also kappa(s)
is decreasing, with minimum1687/500 at s=31/10. The fast minimum remains
strictly larger. At frequency zero the exact energy is more negative;
that singleton does not affect integration.

## Commutator and perturbation proof for the full interval

All inequalities used here are valid for every real s in the specified
closed interval. The mean value theorem gives

 |<eta+k>^s-<eta>^s|
 <=s2^(s-2)(|k|<eta>^(s-1)+|k|^s).

The Hessian of <eta>^s has norm at most s(s-1)<eta>^(s-2). Its integral
Taylor remainder is bounded by

 s(s-1)2^(s-4)|k|^2[<eta>^(s-2)+|k|^(s-2)].

The convex power inequalities used here require s>=3 for the second
estimate and s>=2 for the first; both hold. Convolution and the elementary
polar integrals integral <xi>^(-2r)=pi/(r-1),
integral |xi|^2<xi>^(-2r)=pi/[(r-1)(r-2)] then imply

 ||[J^s,f]u||2<=P_s(f)||u||Ht,
 [J^s,w.grad]u=-s sum_ij (partial_j w_i)partial_ij J^(s-2)u+R_w u,
 ||R_w u||2<=T_s(w)||u||Ht.

The first leading transport term has Hs operator norm at most
s||Dw||infinity,F, since the sum of squares of its Fourier multipliers
is bounded by <xi>^(2s). The symbol of U has vector norm at most1.
Integration by parts and pointwise Cauchy-Schwarz therefore give

 Re <A_s u,u>Hs
 <=-a_s||u||Hs^2+R_s||u||Ht||u||Hs.                       (3)

All constants are finite: s-1>=41/20>2 keeps both alpha_(s-1) and
beta_(s-1) finite; W_2(w) is bounded by alpha_2||w||H4, W_1(q) by
alpha_2||q||H3, and ||f||Hs<=||f||H3^(4-s)||f||H4^(s-3).
Compact C4 coefficients have these integer Sobolev norms. No fifth
coefficient derivative or limiting claim at s=3 is being made.

For the trial coefficients, Taylor's integral formula gives on the ball

 |V-Dz|<=M_V|z|^2/2, ||DV-D||F<=M_V|z|,
 |grad rho-(0,g)|<=M_rho|z|,

where z=X-P. Constant divergence makes div(V-Dz)=0. The cutoff product
rule thus yields

 ||Dw||infinity,F<=[3+(9/2)C_theta]M_V delta,
 ||div w||infinity<=(9/2)C_theta M_V delta,
 ||q||infinity<=3M_rho delta.

Hence E_s<=delta([3s+(9/2)(s+1/2)C_theta]M_V+3M_rho).
For C_theta<=2 this is bounded by the expression in(2). Its coefficients
are positive, so the strict derivative ceilings give a strict bound.
C_* increases and kappa decreases with s; the worst denominator in(2)
is at s=31/10, where topic86's exact value is314446949/100000000.
That denominator exceeds zero and its reciprocal is below3181/10000.
It also gives E_s<kappa(s)/2 uniformly.

## Maximal domain, decay, and inversion

The core and generator construction of topic78 is used as an explicit
analytic dependency, with the change of s justified as follows. The vector
field b is globally Lipschitz with at most linear growth. Its global flow
generates on L2 the transport group u->u composed with Phi_tau. Its maximal
domain is {u in L2:b.grad u in L2}; cutoff, mollification, and the bounded
Friedrichs commutator prove that C_c^infinity is a graph core. This argument
has no s parameter. Conjugation by J^s gives

 J^s b.grad J^(-s)=b.grad+C_s,

where the frozen linear part has bounded symbol and the variable part is
bounded by the just proved commutator with ||u||Ht<=||u||Hs. Likewise
J^s(-1-gM+q.U)J^(-s) is bounded. The bounded perturbation Dyson series on
L2 therefore yields the Hs semigroup with precisely the domain in(1);
topic78 proves the domain identification by resolvents. Its graph core
J^(-s)C_c^infinity is Schwartz for every real s here. Thus(3) extends to
the full domain. Every premise of that construction, including the
multiplier bound and compact C4 regularity, has been checked above.

On that domain the L2 energy inequality is

 Re<A_s u,u>2<=-a0||u||2^2,

because M is nonnegative. Let x(tau)=||exp(tau A_s)u||Hs,
y(tau)=||exp(tau A_s)u||2. Then y<=exp(-a0 tau)y(0), and Fourier Holder
interpolation ||v||Ht<=||v||Hs^(1-1/s)||v||2^(1/s) gives

 x'<=-a_s x+R_s x^(1-1/s)y^(1/s).

Until x first vanishes, integrating the inequality for x^(1/s) yields

 x(tau)^(1/s)<=exp(-a_s tau/s)
 [x(0)^(1/s)+(R_s/d_s)y(0)^(1/s)(1-exp(-d_s tau/s))].

After a zero the semigroup trajectory remains zero. The stated lower
bound for d_s follows by using A>=10,mu>=99/100 and ||Dw||>=0:

 d_s>=1299/200-kappa(s)=(101/100)s-1/100.

Since y(0)<=x(0), this proves the claimed semigroup bound on domain data,
then all Hs data by density. Its negative strong integral on[0,infinity)
converges. For finite upper limit T the generator applied to the integral
is exp(T A_s)u-u; closedness and decay give a right inverse. A null vector
would be fixed by the semigroup and decay, hence is zero. This proves(1).

## Local estimate and normalization

Use exactly the cutoff arrangement and local norms in topic77 sections1,
5-7. Initially h is smooth and compactly supported with h(0)=grad h(0)=0.
The local operator is

 Lh=V.grad h-h+grad rho.U[h]+(X.grad rho/3)sigma[h],
 sigma[h]=psi[h]_xy(0), -Delta psi=partial_x h,
 U=(-partial_y psi,partial_x psi).

The correct physical strain is the one in topic80; this supersedes the
opposite stream-function convention in the old77/78 addenda. All strain
absolute bounds remain unchanged. The raw rank-one denominator for the
auxiliary operator is1+sigma[A_s^(-1)ell_delta]. It is not evaluated.

To check the entire localization argument at variable s: the U cutoff
commutator estimate with C_U=2*3^s uses s>=1; the remote kernel derivatives
and strain split do not depend on s; the integer H4 remote bounds dominate
Hs because s<4. The off-diagonal J^s heat representation with two scalar
subtractions needs2<s<4. Its integrable off-diagonal kernel bound is
D_s|X|^(-2-s), D_s=2^s Gamma(1+s/2)/(pi|Gamma(-s/2)|). All these hold on
the specified interval. The annular transport estimate uses t=s-1>1.
Thus every estimate in topic77 sections5-7 holds with its displayed
constants evaluated at s, and substitution into(3) gives its exact K1-K4
formula. This reference imports those explicitly proved definitions and
localization identities, not an assertion about an unspecified domain.
The same graph completion in its addendum is taken with the current s,t.
For uniformly smooth rescaled cutoff shapes, its scaling exponents remain
K2=O(delta^(3-2s)), K3=O(delta^(3-3s)), K4=O(delta^(-s-2)).

The conclusion concerns each fixed s. It does not prove equivalence of
these domains, an outer escape estimate, Fredholmness, the physical
rank-one denominator, or a contraction near X3. There is no decisive
endpoint. This proof was written before its new arithmetic checker.
