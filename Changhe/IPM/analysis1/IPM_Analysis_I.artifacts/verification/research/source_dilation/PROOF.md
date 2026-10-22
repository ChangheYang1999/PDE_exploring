# Isotropic dilation of the auxiliary source inverse

## Exact statement and scope

Let s in [61/20,31/10]. Use the unitary Fourier transform
fhat(xi)=(2pi)^(-1) integral exp(-i X.xi) f(X)dX on R^2 and the
inhomogeneous norm ||f||Hs^2=integral (1+|xi|^2)^s |fhat(xi)|^2 dxi.
Let P in R^2, D=diag(A,mu), 10<=A<=51/5, 99/100<=mu<=101/100,
and 29<=g<=30. For real compact C4 vector fields w,q define

 b(X)=D(X-P)+w(X),
 A_s u=b.grad u-u-g M u+q.U[u],
 Mhat(xi)=xi_1^2/|xi|^2,
 Uhat(xi)=(xi_1 xi_2,-xi_1^2)/|xi|^2.

The multiplier values at xi=0 do not matter. Define

 kappa(s)=1301/200-(101/100)s,
 E_s=||div w||infinity/2+s||Dw||infinity,F+||q||infinity,
 a_s=kappa(s)-E_s,
 d_s=1+(A+mu)/2-kappa(s)+s||Dw||infinity,F,
 W_r(f)=(2pi)^(-1) integral (1+|xi|^2)^(r/2)|fhat(xi)|dxi,
 alpha_r=1/[2 sqrt(pi(r-1))],
 beta_r=1/[2 sqrt(pi(r-1)(r-2))],
 P_s(f)=s 2^(s-2)[W_1(f)+alpha_(s-1)||f||Hs],
 T_s(w)=s(s-1)2^(s-4) sum_i[W_2(w_i)+beta_(s-1)||w_i||Hs],
 R_s(w,q)=T_s(w)+sum_i P_s(q_i).

Assume E_s<kappa(s). Topic92, with its mandatory addendum, proves that
A_s on the maximal domain {u in Hs:b.grad u in Hs in distributions}
generates a strongly continuous semigroup with bound
(1+R_s/d_s)^s exp(-a_s t), and has a two-sided inverse of norm at most
(1+R_s/d_s)^s/a_s. Topic78 supplies the explicit domain and core proof.
We import those proved theorems, not their numerical illustrations.
In particular d_s>=(101s-1)/100>0. At s=31/10 this is topic78 directly.

Fix any 0<ell<=1. For Y in R^2 put

 (D_ell u)(Y)=u(P+ell Y),
 w_ell(Y)=ell^(-1)w(P+ell Y),
 q_ell(Y)=q(P+ell Y),
 b_ell(Y)=DY+w_ell(Y).

Then D_ell A_s D_ell^(-1) is exactly the same differential and multiplier
expression with P=0 and coefficients w_ell,q_ell. Its E_s,a_s,d_s are
unchanged. It satisfies all hypotheses of the imported theorem. Put
R_ell=R_s(w_ell,q_ell), and define on the original X-plane

 N_lambda(u)^2=integral (lambda^2+|xi|^2)^s |uhat(xi)|^2 dxi.

The original operator, with its same maximal domain as a set, obeys

 ||exp(t A_s)||_(N_(1/ell)->N_(1/ell))
       <=(1+R_ell/d_s)^s exp(-a_s t),
 ||A_s^(-1)||_(N_(1/ell)->N_(1/ell))
       <=B_N(ell):=(1+R_ell/d_s)^s/a_s,
 ||A_s^(-1)||_(Hs->Hs)<=B_H(ell):=ell^(-s) B_N(ell).       (1)

These are auxiliary inverse bounds. They omit the physical rank-one
strain feedback, the outer region and the global IPM realization. No
floating R_ell, residual norm, scalar denominator or nonlinear closing
constant is certified by this corollary.

## Fourier change of variables and operator conjugation

For Schwartz u a direct change X=P+ell Y gives

 (D_ell u)hat(eta)=ell^(-2) exp(i P.eta/ell) uhat(eta/ell). (2)

If m is either component of U or M, m(eta)=m(eta/ell) away from zero,
so (2) proves m(D_ell u)=D_ell(m u). The equality extends to Hs by
boundedness and density. Translations introduce the phase in (2), which
cancels in every Fourier norm below. There is no extra factor ell in
these order-zero multipliers.

The chain rule gives grad_X u(P+ell Y)=ell^(-1)grad_Y D_ell u, hence

 (b.grad_X u)(P+ell Y)=(DY+ell^(-1)w(P+ell Y)).grad_Y D_ell u.

Combining these identities proves conjugation on Schwartz functions.
The transport identity holds in distributions by testing and changing
variables. Compact C4 coefficient products are interpreted on the
Sobolev spaces at issue; no multiplication on arbitrary distributions
is asserted. This extends conjugation to the maximal domain.

Precisely, (2) and eta=ell xi imply

 ||D_ell u||Hs^2
  =ell^(-2) integral (1+ell^2|xi|^2)^s |uhat(xi)|^2 dxi
  =ell^(2s-2) N_(1/ell)(u)^2.                             (3)

For fixed positive ell, N_(1/ell) is equivalent to Hs. Therefore D_ell
is a bounded invertible map from Hs as a set to Hs, and the transport
identity shows

 b.grad u in Hs iff b_ell.grad D_ell u in Hs.

This proves equality of the conjugated maximal domains, including both
directions. The scalar factor ell^(s-1) in (3) cancels between domain
and range in each operator norm.

## Coefficient norms, hypotheses and inverse transfer

The ordinary chain rule gives

 Dw_ell(Y)=Dw(P+ell Y),
 div w_ell(Y)=div w(P+ell Y).

The change of coordinates is onto R^2. Thus the supremum of each of
these Euclidean or Frobenius norms is exactly unchanged, as is
||q_ell||infinity. This proves equality of E_s, a_s and d_s, not just
an upper bound. The fields w_ell,q_ell remain real C_c^4. Their support
may become large. Topics78 and92 impose no support-radius bound, no
coefficient cutoff scale and no restriction 3delta<P/2 on this auxiliary
operator theorem. Those conditions occur only when constructing actual
local coefficients or localizing the physical IPM equation. They are not
needed to reapply the global auxiliary theorem to w_ell,q_ell.

In particular all commutator constants remain finite: C_c^4 is contained
in H4, W_2<=alpha_2||.||H4, W_1<=alpha_3||.||H4, and s<4. The linear
coefficient DY is unchanged. Reapplying the theorem and then using (3)
proves the first two inequalities in (1). The norm comparisons

 ||u||Hs<=N_(1/ell)(u)<=ell^(-s)||u||Hs

prove the last one. B_N(ell) bounds a different norm for each ell, so
one cannot minimize B_N(ell) alone and label the result an Hs bound.
The Hs bound to minimize is B_H(ell).

For completeness the exact B_H has a minimum over 0<ell<=1. On every
closed interval epsilon<=ell<=1, dominated convergence in the formulas
below proves continuity of R_ell. The dominating functions are the
finite W_r and Hs integrands of the compact C4 fields, times bounded
powers of ell^(-1). Thus B_H is continuous. Moreover B_H(ell)>=ell^(-s)/a_s
tends to infinity as ell decreases to zero. A sufficiently small epsilon
has B_H(ell)>B_H(1) for ell<epsilon, and continuity on [epsilon,1]
attains the minimum. This proves existence of an optimal bound, not its
location. With certified constants at finitely many scales, only the
minimum of those finitely many bounds is immediately certified.

## Exact formulas used to recompute the constants

For f_ell(Y)=f(P+ell Y), (2) and eta=ell xi give

 W_r(f_ell)=(2pi)^(-1) integral (1+ell^2|xi|^2)^(r/2)|fhat(xi)|dxi,
 ||f_ell||Hs=ell^(-1)
       [integral (1+ell^2|xi|^2)^s|fhat(xi)|^2 dxi]^(1/2). (4)

Both right sides acquire one further factor ell^(-1) for a component
of w_ell. These identities apply for the finite weighted integrals in
the theorem. They do not assert that replacing the integrals by FFT
sums without a tail estimate is rigorous. If f is supported in a disc
of radius R and ||D^j f||infinity,F<=B_j for 0<=j<=4, the useful exact
integer-order majorant is

 ||f_ell||H4^2<=pi R^2 ell^(-2)
           sum_(j=0)^4 binom(4,j) ell^(2j) B_j^2.         (5)

This follows by expanding (1+|eta|^2)^4 and Parseval, summing all ordered
Cartesian derivatives for each Frobenius tensor. For w_ell add ell^(-2)
to the right side. Formula(5) can supply conservative certified R_ell
without any new PDE or FFT calculation. It is an upper bound, not an
identity for a coefficient field from its derivative suprema.

## Anisotropic changes and numerical scope

For L=diag(ell_1,ell_2), u(P+LY) has Fourier transform
det(L)^(-1) exp(i P.L^(-T)eta) uhat(L^(-T)eta). The transformed M symbol is

 ((eta_1/ell_1)^2)/[(eta_1/ell_1)^2+(eta_2/ell_2)^2].       (6)

For ell_1=1, ell_2=2 and eta=(1,1), it is4/5 rather than1/2. Thus the
same imported theorem cannot simply be invoked for anisotropic dilation.
The U symbols change as well; the frozen coercivity and commutator
estimates must be rederived. In addition Dw_L=L^(-1)(Dw)L in general,
so its Frobenius supremum need not be preserved. Constant diagonal D
commuting with L does not fix either problem.

The lead's reported floating values at ell=1,0.0165,0.01,0.0035 concern
a different smooth cutoff and are not checked here. The strong scale
sensitivity is compatible with(4): a field supported at a small scale
has substantial high-frequency mass. Consistency with a scaling law
is not certification of any reported number. The present result proves
(a)-(e) of V31, with the stated scope and the correct distinction between
N_(1/ell) and Hs. It does not make an IPM endpoint available.
