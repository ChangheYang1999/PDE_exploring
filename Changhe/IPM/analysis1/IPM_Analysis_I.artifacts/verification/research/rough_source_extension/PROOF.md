# Rough coefficients, origin jets, and the local source estimate

Status at proof writing: independent analytical reconstruction, not yet a
final verifier verdict. The evolving lead r3 note is frozen in source/lead_r3.md.
Its completion argument as written has a missing term. The corrected results
below are proved before any diagnostic code. They are conditional local and
auxiliary results. They do not construct the physical IPM inverse.

## 1. Precise hypotheses, notation, and dependencies

Use the unitary transform fhat(xi)=(2pi)^(-1) integral exp(-i X.xi)f(X)dX
on R2, J^r=(1-Delta)^(r/2), and ||f||Hr=||J^r f||2. Restriction Sobolev
norms are infima of whole-plane extension norms. Vector norms and derivative
tensor norms are Euclidean and Frobenius. Fix

 61/20<=s<=31/10, t=s-1, sigma>=s, sigma>3,
 10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30,
 P=(p,0), p>0, 0<delta<=1, 3delta<p/2, D=diag(A,mu),
 kappa(s)=1301/200-(101/100)s.

For compact coefficients set

 W_r(f)=(2pi)^(-1) integral <xi>^r |fhat(xi)| dxi,
 alpha_r=1/[2sqrt(pi(r-1))], beta_r=1/[2sqrt(pi(r-1)(r-2))],
 P_s(f)=s 2^(s-2)[W_1(f)+alpha_(s-1)||f||Hs],
 B_s(f)=||f||infinity+P_s(f), M_r(f)=2^(r/2)W_r(f),
 T_s(w)=s(s-1)2^(s-4) sum_i[W_2(w_i)+beta_(s-1)||w_i||Hs].

The bounded canonical multipliers are

 Uhat=(xi1 xi2,-xi1^2)/|xi|^2, Mhat=xi1^2/|xi|^2.

Their values at zero are immaterial. In particular ||Uu||_(Hr;R2)<=||u||Hr
and M is positive on L2. Raw strain sigma0[u]=psi[u]_xy(0) uses the canonical
sign verified in topic80. Its Fourier evaluation symbol is
-i xi1^2 xi2/|xi|^2, with modulus at most |xi|, hence

 |sigma0[u]|<=beta_s||u||Hs.                              (1)

The prompt's scaling functional is sigma0/3. Here sigma denotes only a
Sobolev regularity exponent; sigma0 denotes strain.

Dependencies are the already verified Fourier energy, commutator and
localization identities in topic77, the C4 auxiliary inverse in topic78,
the sign correction in topic80, their order-s extension in topic92, the
conditional moving-source bounds in topic94 and the smooth-coefficient
dilation formulas in topic96. We restate exactly the parts used below.
No finite-dimensional numerical inverse or compactness assertion is used.

## 2. Product bounds and a replacement for e_A

For r>=1, <xi+eta><=<xi>+<eta>, so convexity gives

 <xi+eta>^r<=2^(r-1)(<xi>^r+<eta>^r).

The convolution formula and the L1*L2 Young inequality prove

 ||fg||Hr<=2^(r-1)(||f||Hr W_0(g)+W_0(f)||g||Hr).         (2)

The inequalities extend from smooth functions by approximation whenever the
right side is finite. Polar integration gives

 integral <xi>^(-2m) dxi=pi/(m-1), m>1.

Thus, for sigma>r+1,

 W_r(f)<=alpha_(sigma-r)||f||Hsigma.                      (3)

In particular W_2 is continuous in Hsigma when sigma>3. W_1 is continuous
in Hr when r>2, with constant alpha_(r-1). These are inhomogeneous weights:
beta_r controls the homogeneous integral of |xi||fhat|, not W_1.

Let pcut be the smooth fixed annular cutoff of topic77 (24). For every
whole-plane Hs extension H of h on the source annulus, (2) implies

 ||pcut V_i partial_i H||Ht
 <=2^(t-1)[alpha_t||pcut V_i||Ht+W_0(pcut V_i)]||H||Hs.

Here ||partial_i H||Ht<=||H||Hs and (3) at r=0 controls its W_0. Therefore

 e_A'=sum_i 2^(t-1)[alpha_t||pcut V_i||Ht+W_0(pcut V_i)]   (4)

can replace sum_i M_t(pcut V_i). Direct inspection of the full equations
(19),(24),(25),(26) of topic77 shows e_A occurs only in the annular transport
term of (25), and then in

 K2=[B_s(V.grad chi)+P_s(chi)e_A]/(kappa-E).               (5)

No other occurrence is suppressed. The replacement changes K2, not K1,
K3 or K4. When sigma=s, finiteness of W_t(V) does not follow from (3), since
that would require sigma>s. Formula (4) avoids this strict-endpoint problem.
The original formula is available when all its W_t quantities are finite.

## 3. The auxiliary inverse with Hsigma coefficients

Let w,q be real compactly supported Hsigma vector fields. Put

 b=D(X-P)+w, Aop u=b.grad u-u-gM u+q.Uu,
 E=||div w||infinity/2+s||Dw||infinity,F+||q||infinity,
 R=T_s(w)+sum_i P_s(q_i), a_s=kappa-E,
 a0=1+(A+mu)/2-||div w||infinity/2-||q||infinity,
 d=a0-a_s=1+(A+mu)/2-kappa+s||Dw||infinity,F.

Assume E<kappa. All quantities are finite by (3) and the Fourier embeddings.
On the stated box,

 d>= (101/100)s-1/100 >=6141/2000>0.                     (6)

Then Aop is a bijection from its maximal domain

 D(Aop)={u in Hs: b.grad u belongs to Hs as a distribution}

to Hs, and

 ||Aop^(-1)||_(Hs->Hs)<=(1+R/d)^s/a_s.                  (7)

Proof. Choose a nonnegative smooth compact mollifier of integral1. Let
w_n=j_n*w, q_n=j_n*q. They are real smooth and compactly supported. They
converge in Hsigma and, by (3), in W_2 for w, W_1 for q, Hs, and C1. The
suprema defining E and d converge: the difference between sup norms is at
most the sup norm of the difference. Thus E_n,R_n,d_n and the bound B_n
in (7) converge to E,R,d and B. Eventually E_n<kappa.

The verified C4 theorem at order s gives u_n=Aop_n^(-1)f and
||u_n||Hs<=B_n||f||Hs for each f in Hs. A subsequence converges weakly in
the Hilbert space Hs to u, with ||u||Hs<=B||f||Hs. Against any smooth compact
phi, integration by parts gives

 <b_n.grad u_n,phi>=-<u_n,div(b_n phi)> -> -<u,div(b phi)>.

Indeed div(b_n phi) converges strongly in L2 on the fixed support. The
terms u_n and Mu_n converge weakly in L2. For the last term, uniform
convergence q_n->q and boundedness of Uu_n imply
(q_n-q).Uu_n->0 in L2, and q.U(u_n-u) converges weakly in L2. Consequently
Aop u=f distributionally. Formula (2), with r=s, proves q.Uu belongs to Hs;
for example its norm is at most
2^s alpha_s(sum_i||q_i||Hs)||u||Hs. Therefore
b.grad u=f+u+gMu-q.Uu belongs to Hs. This proves surjectivity into the
specified domain with (7).

For uniqueness take u in that domain with Aop u=0. Then u is in H1,
b.grad u is in L2, b is C1 and has linear growth. Choose a smooth real
cutoff chi_R equal1 on B_R and0 outside B_(2R). The weak product rule for
|u|^2 gives

 Re integral (b.grad u)conj(u)chi_R
 =-1/2 integral div b |u|^2 chi_R
  -1/2 integral b.grad chi_R |u|^2.

The last integrand is supported in R<=|X|<=2R and |b.grad chi_R|<=C for
R>=1. Its integral tends to0 by the L2 tail. The other integrals converge
because div b is bounded and (b.grad u)conj(u) is L1. Positivity of M and
||Uu||_(L2;R2)<=||u||2 now give

 Re<Aop u,u>2<=-a0||u||2^2.

Since a0=a_s+d>0, u=0. This proves (7) and bijectivity. It does not assert
that a semigroup has been constructed for rough coefficients.

The topic77 energy inequality also passes to rough coefficients for every
fixed smooth compact u, by (2):

 Re<Aop u,u>Hs<=-a_s||u||Hs^2+R||u||Ht||u||Hs.           (8)

Its extension to the whole maximal domain is unnecessary for this proof
and is not asserted here.

## 4. Local velocity extension and the divergence qualification

Let B' be a bounded ball containing the closed source ball of radius3delta.
On B', suppose V=V0+W with V0 in C4(B'), W in Hsigma(B'). Let rho be C5 on
the source ball. Assume

 V(P)=0, DV(P)=D, grad rho(P)=(0,g).

Choose the smooth cutoffs chi,tau,theta,zeta,pcut from topic77, with supports
strictly inside their specified balls. Define a=grad rho, ell=X.a/3,

 Lh=V.grad h-h+a.Uh+ell sigma0[h],
 w=theta(V-D(X-P)), q=theta(a-(0,g)).

Define E,R,a_s with these coefficients. Assume E<kappa. With the actual E,
the local estimate of topic77 holds for this V, with (4) in K2:

 ||chi h||Hs<=K1||tau Lh||Hs+K2 A_h+K3 H_h+K4 N(h),       (9)
 K1=1/(kappa-E), A_h=||h||Hs(B_(2delta)(P)\B_delta(P)),
 H_h=||h||Ht(B_(3delta)(P)),
 N(h)= integral_(|X-P|>=5delta/2) |h(X)|/|X-P|^2 dX
      +integral_(R2\B_(3delta)(P)) |h(X)|/|X|^3 dX.        (10)

K3 and K4 are exactly topic77 (19),(24),(26); the fixed rho, cutoffs and
remote-kernel constants are retained. Initially h is smooth compact with
h(0)=grad h(0)=0.

There is a logical qualification in invoking topic77. Its hypothesis (1)
includes div V=A+mu. Its proof uses that equality only in the Taylor bound
(13) for an explicit upper bound on E. The frozen energy (6), perturbed
energy (11), localization identity (20), remote estimates (15)-(18) and
forcing localization (23)-(26) do not use it. In those lines div w is
retained in the actual E. Repeating these identities, without the separate
bound (13), proves the C4 local estimate (9) with arbitrary divergence.
This directly justifies the slight enlargement of the smooth theorem used
in the following approximation. It does not enlarge the explicit E budget.

Choose one whole-plane Hsigma extension Wext of W; the restriction norm
convention supplies it. Let Wtilde_n=j_n*Wext and choose a smooth compact
zeta0 equal1 on B'. Put

 W_n=Wtilde_n-[ (Wtilde_n-Wext)(P)
                  +D(Wtilde_n-Wext)(P)(X-P)]zeta0.

Then W_n(P)=W(P), DW_n(P)=DW(P). Global Hsigma convergence of the mollifier,
and continuity of value and first-derivative evaluations for sigma>2,
show W_n-Wext->0 in Hsigma, since the finitely many correction coefficients
tend to0 and the fixed polynomial-cutoff functions are smooth compact.
The convergence is also C1. Consequently V_n=V0+W_n is C4, preserves the
point data exactly, and all its V-dependent constants converge. Specifically
these are E, R, B_s(V.grad chi), e_A' and ||tau V||infinity. Fixed smooth
cutoff multiplication is bounded in Hsigma; the V0 terms have compact C4
regularity, and s<4, so all their Hs and W_2 quantities are finite. Formula
(3) controls the differences from W_n-W. There is no need to assume V0 in
Hsigma if sigma>4.

For fixed admissible smooth h,
||tau(L[V_n]-L[V])h||Hs=||tau(V_n-V).grad h||Hs->0 by (2).
Eventually E_n<kappa, and all denominators and constants converge. Applying
the enlarged C4 estimate and passing to the limit proves (9).

For the explicit topic94 budget one must additionally retain

 div V=A+mu on B_(3delta)(P).                            (11)

The approximation above need not preserve (11). This causes no gap because
only the actual E was used in passing to the limit. At the limit V is C2
(by sigma>3 and V0 in C4), so Taylor's integral formula and (11) yield,
with Ctheta=delta||grad theta||infinity,

 E<=[3s+(9/2)(s+1/2)Ctheta] M_V delta+3M_rho delta,
 M_V=sup||D2V||F, M_rho=sup||D2rho||F.                   (12)

This is precisely the original estimate. Without (11), an additional
||theta div(V-D(X-P))||infinity/2 term must be retained, or E must be
computed directly. Constant-divergence numerical ceilings do not extend
silently to arbitrary rough velocities.

## 5. The origin term and a counterexample to the written approximation

For any f in Hs with f(0)=grad f(0)=0, Fourier inversion and Cauchy-Schwarz
give

 ||D2 f||infinity,F<=gamma_s||f||Hs,
 gamma_s=1/sqrt[2pi(s-1)(s-2)(s-3)].                     (13)

Indeed the squared norm of the Fourier derivative tensor is |xi|^4, and
integral |xi|^4<xi>^(-2s) dxi=2pi/[(s-1)(s-2)(s-3)],
by polar substitution and two integrations by parts. Cauchy-Schwarz,
including the (2pi)^(-1) factor, proves (13). It also proves absolute
Fourier convergence of the second derivatives and their continuity.

For every R>0, Taylor's formula |f(X)|<=||D2 f||infinity,F |X|^2/2 gives

 integral_(|X|<=R) |f(X)|/|X|^3 dX<=pi R||D2 f||infinity,F.

On the complement, Cauchy-Schwarz and
integral_(|X|>R)|X|^(-6)dX=pi/(2R^4) give

 integral_(|X|>R)|f(X)|/|X|^3 dX<=sqrt(pi/2)R^(-2)||f||2.

Combining these with the other term of (10) proves

 N(f)<= [2sqrt(pi)/(5delta)+pi R gamma_s+sqrt(pi/2)R^(-2)]
          ||f||Hs.                                     (14)

The set excluded in the second term only decreases the positive integral.
Thus N is continuous on the closed zero-jet subspace of Hs. It is not
controlled by the first integral alone, and not by Hs on arbitrary functions.

The defect in lead r3 L5(ii),(v) has an explicit parity-preserving example.
Choose h(x,y)=y^3 eta(x,y), where eta is a radial smooth compact cutoff
identically1 on B1. Then h is even in x, odd in y, and h(0)=grad h(0)=0.
Let j be a nonnegative even radial mollifier supported in B1 with
m2=integral y^2 j(x,y)dxdy>0. For eps<1/4 and |X|<1/2,

 (j_eps*h)(x,y)=y^3+3eps^2 m2 y.

Its absolute value is at least3eps^2 m2 |y|. Because the source ball is
away from zero, the omitted origin integral contains a small punctured
ball and dominates a positive multiple of integral_0^r0 dr/r=infinity.
Hence N(j_eps*h)=infinity although N(h)<infinity and j_eps*h->h in Hs.
The correction g which subtracts the linear origin jet also has N(g)=infinity.
This refutes those two continuity claims as written, not the corrected
density theorem below.

## 6. Correct graph approximation in the full norm N

Suppose h is in Hs(R2), h(0)=grad h(0)=0, and tau' Lh belongs to Hs for
some smooth compact tau' equal1 on a neighbourhood of supp tau, with
supp tau' strictly inside B_(5delta/2)(P). Then h belongs to the completion
class of the smooth test functions in (9), including both terms of N.
In particular (9) holds for h with the same constants.

First the order-zero part of tau' L is bounded Hs->Hs: tau', tau'a_i and
tau'ell have compact C4 regularity, so the topic77 B_s multiplication
bound applies, and (1) controls strain. Thus G=tau' V.grad h is in Hs.
Choose smooth compact tau'' equal1 on a neighbourhood of supp tau', with
support in B_(5delta/2)(P), and let v=tau''V. Its components are in Hs and
have finite W_1, by (3). Choose the mollifier above and write J_eps h=j_eps*h.
For sufficiently small eps, on supp tau locality gives

 tau V.grad J_eps h=tau J_eps G+tau K_eps h,
 K_eps h=v.grad J_eps h-J_eps(v.grad h).                 (15)

We prove K_eps h->0 in Hs without assuming a hidden extra derivative of h.
Let jhat0 be the ordinary convolution multiplier of j, normalized to1 at0,
and put c0=sup|jhat0|, c1=sup_z |z||grad jhat0(z)|; both are finite.
In the Fourier integral write k=xi-eta. If |k|>=|eta|/2 then

 |eta||jhat0(eps eta)-jhat0(eps xi)|<=2c0|eta|,
 <xi><=3<k>.

If |k|<|eta|/2, the line segment from eta to xi has norm at least|eta|/2.
The mean value integral gives

 |eta||jhat0(eps eta)-jhat0(eps xi)|<=2c1|k|,
 <xi><=(3/2)<eta>.

At eta=0 the integrand is zero. Applying these two bounds to the respective
regions, then enlarging each positive convolution integral to all k, gives

 ||K_eps h||Hs<=sum_i[2c0 3^s||v_i||Hs W_1(h)
                    +2c1(3/2)^s W_1(v_i)||h||Hs]
 <=C_K||h||Hs,                                          (16)

where C_K is finite by W_1(h)<=alpha_(s-1)||h||Hs. The Fourier identity
and bound first hold for smooth inputs and extend by continuity; v.grad h
is well-defined in H^(s-1) by (2), so this extension is the distributional
commutator in (15). For h' in H^(s+1), (2) shows v.grad h' belongs to Hs,
and both terms of K_eps h' tend to it in Hs. Such h' are dense in Hs, so
(16) proves strong convergence K_eps h->0 for every h in Hs. Equation (15)
therefore proves tau L J_eps h->tau Lh in Hs. No N estimate has yet been
applied to J_eps h.

Now impose the jets before using N. Choose a smooth compact eta0 equal1
near0, with support in B_(p/2)(0), disjoint from the source ball. Define

 v_eps=J_eps h-[J_eps h(0)+grad J_eps h(0).X]eta0.

It is smooth with zero value and gradient at0, and converges to h in Hs,
since the jet errors tend to0. The correction is supported away from
supp tau. Its local transport part vanishes there; its remaining contribution
to tau L tends to0 by the order-zero bound. Consequently

 v_eps->h in Hs, tau L v_eps->tau Lh in Hs,
 N(v_eps-h)->0 by (14).                                 (17)

Finally multiply v_eps by a smooth compact cutoff chi_R(X)=chi1(X/R),
identically1 on the source ball and near0 for large R. This preserves the
zero jets. For fixed eps, chi_R v_eps->v_eps in Hs as R->infinity. One
proof uses that v_eps has every integer Sobolev derivative: Leibniz's rule
and the L2 tails prove convergence in H^m for any integer m>s, which
implies Hs convergence. The change is supported away from supp tau, so
its tau L image converges by the order-zero bound. Formula (14) applies
to the zero-jet difference and proves N convergence as well.

Choose a diagonal eps_n->0 and R_n->infinity to make these errors tend to0.
The resulting h_n=chi_(R_n)v_(eps_n) are smooth compact with exact zero jets.
Their local restriction norms converge since each restriction norm of a
difference is at most its global Hs norm. Smooth fixed multiplication gives
chi h_n->chi h in Hs. All four right-hand quantities of (9) converge,
including the full N, so (9) passes to the limit. Even/odd symmetry can be
retained with radial mollifiers and cutoffs; the surviving origin-jet
correction has the same symmetry. This proof covers global Hs corrections.
It makes no approximation claim for a larger weighted space not contained
in global Hs.

## 7. Conditional moving-source consequence and dilation

For h in Hs, the physical increment W[h]=U[h]+sigma0[h]X/3 is locally Hs.
Its second derivative is D2U[h]. The vector symbol of U has norm at most1,
so the same tensor argument as in (13) gives

 ||D2W[h]||infinity,F<=gamma_s||h||Hs.                    (18)

This bound includes the whole plane only when h is globally Hs. The field
has constant divergence 2sigma0[h]/3, since div U[h]=0 as a Fourier identity.
Thus V0+W[h] retains constant divergence when V0 has it; at an actual source
with diagonal jet D this divergence equals trace D=A+mu. Subject to all
topic94 source-location, box and Hessian-budget hypotheses, its transported
estimate follows from sections4 and6 for global Hs corrections. These
hypotheses are not consequences of Sobolev membership.

With the same delta', M_V' and M_rho', Ctheta<=2, the budget is
C_src(s)=(12s+9/2)M_V'+3M_rho'. At s=153/50 versus31/10, exact subtraction gives

 [kappa(153/50)-delta'C_src(153/50)]
 -[kappa(31/10)-delta'C_src(31/10)]
 =101/2500+(12/25)delta'M_V'>0.                          (19)

Therefore the topic94 K1 ceilings also hold at3.06, conditionally on the
same budgets, with rough H^3.06 corrections and the completion class just
proved. This monotonicity is not asserted for R, B, K2, K3 or K4.

The auxiliary dilation statement also extends to the rough coefficients
of section3. For 0<ell<=1 define D_ell u(Y)=u(P+ell Y),

 wtilde(Y)=w(P+ell Y)/ell, qtilde(Y)=q(P+ell Y).

Compact support and Hsigma regularity are preserved for each fixed ell>0.
Homogeneity of the degree-zero Fourier symbols and the distributional
chain rule prove

 D_ell Aop D_ell^(-1)=Aoptilde,
 D_ell D(Aop)=D(Aoptilde).                               (20)

In particular no generator-domain identification is imported. The maximal
domains in (20) follow directly from the identity for b.grad u and the
bounded invertibility of D_ell on Hs. Derivatives of wtilde of order1 have
the original sup norms, and qtilde has the original sup norm. Hence E,
a_s and d are unchanged, while R becomes the value Rtilde for the new
coefficients. Fourier change of variables gives

 ||D_ell f||Hs=ell^(s-1)N_(1/ell)(f),
 N_lambda(f)^2=integral(lambda^2+|xi|^2)^s|fhat(xi)|^2 dxi.

Applying (7) to the conjugate gives inverse bound
(1+Rtilde/d)^s/a_s in N_(1/ell), and at most ell^(-s) times it in Hs,
since ||f||Hs<=N_(1/ell)(f)<=ell^(-s)||f||Hs. This proves the rough
version of the analytic dilation, with no new evaluated numerical constant.

## Scope

The inverse in section3 is the auxiliary cut-off operator only. The local
estimate keeps rho C5; it changes the velocity regularity. For the operator
L u+W[h].grad u, rho is the fixed smooth trial. This theorem does not silently
replace it by a rough perturbed density in the coefficients a and ell.
There is no proof of a global physical inverse, a rank-one denominator,
outer matching, a weighted-space completion, a certified high-norm residual,
a Newton contraction, or an IPM Analysis I decisive endpoint. The specific
continuity claims in lead r3 L5(ii),(v) are false as written; the corrected
zero-jet construction above proves the intended global-Hs density result.
