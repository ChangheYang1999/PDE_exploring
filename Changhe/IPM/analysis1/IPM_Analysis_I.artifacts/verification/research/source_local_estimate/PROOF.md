# An explicit local source estimate in inhomogeneous Sobolev spaces

Status at proof writing: independent analytical reconstruction of V23/S1-S5.
The scalar arithmetic and external review are pending. Section 10 separately
states what has and has not been proved about an auxiliary inverse. Nothing
here supplies the global inverse required by IPM Analysis I.

## 1. Statement, normalization, and domain

All functions are on R^2. Use the unitary Fourier transform
fhat(xi)=(2pi)^(-1) integral exp(-i X.xi) f(X)dX and J^r=(1-Delta)^(r/2).
The H^r norm is ||J^r f||_2. For an open set Omega its restriction norm is
the infimum of whole-plane extension norms. Vector norms are Euclidean
sums of component squares; derivative tensors use the Frobenius norm.

Set s=31/10 and t=s-1=21/10. Let P=(p,0), p>0. Suppose, on B_(3delta)(P),
V is C^4, rho is C^5, and

    V(P)=0, DV(P)=D=diag(A,mu), grad rho(P)=aP=(0,g),
    div V=A+mu,
    10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30,
    0<delta<=1, 3delta<p/2.                                  (1)

No stationarity of rho is assumed. Let a=grad rho and ell=X.a/3.
The canonical order-zero velocity has vector Fourier symbol

    m(xi,eta)=(xi eta/(xi^2+eta^2), -xi^2/(xi^2+eta^2)).        (2)

Its arbitrary value at the single frequency zero is immaterial in L2.
Write sigma[h]=psi[h]_xy(0) for RAW strain. The normalized linearization
in this note is

    Lh=V.grad h-h+a.U[h]+ell sigma[h].                       (3)

Thus the scaling functional called c[h] in PROMPT.md is sigma[h]/3.
The source document's symbol c in ell*c must mean raw sigma. We use (3)
throughout to avoid a hidden factor of three.

Initially take h in C_c^infinity with h(0)=grad h(0)=0. This guarantees
absolute convergence of the strain kernel integral below. Conclusions
extend by limits in the explicitly displayed norms, with sigma and U
defined by those limits. No density claim about another IPM domain is made.

Choose smooth cutoffs valued in [0,1], centred at P:

    chi=1 on B_(5delta/4), supp chi inside B_(7delta/4),
    tau=1 on supp chi, supp tau inside B_(9delta/4),
    theta=1 on B_(2delta), supp theta inside B_(3delta),
    zeta=1 on B_(5delta/2), supp zeta inside B_(3delta).        (4)

All displayed inclusions are strict support inclusions, so products extend
smoothly by zero. Put

    w=theta(V-D(X-P)), q=theta(a-aP),
    Aop=D(X-P).grad-1-gM+w.grad+q.U,
    Mhat=xi^2/(xi^2+eta^2).                                 (5)

The theorem below is a local a priori estimate whenever E<kappa, with
kappa=1687/500 and E in (12). Every constant is defined here.

## 2. Frozen energy margin

For Schwartz u, Fourier integration by parts gives

 Re <(D z.grad-1-gM)u,u>_(H^s)
 = integral [-(A+mu)/2-1
       +s(A xi^2+mu eta^2)/(1+xi^2+eta^2)
       -g xi^2/(xi^2+eta^2)] |J^s uhat|^2.                  (6)

This follows from (z_i partial_i u)^hat=-partial_i(xi_i uhat),
with the constant translation P contributing an imaginary multiplier.
The positive transport fraction is no larger than its homogeneous value.
For nonzero frequency put theta0=xi^2/(xi^2+eta^2). The homogeneous
coefficient is affine in theta0. Its negative at theta0=0 and 1 is

    kslow=1+A/2+(1/2-s)mu,
    kfast=1+(1/2-s)A+mu/2+g.

Their exact box minima are respectively1687/500 and159/40. Therefore
(6)<=-kappa||u||_(H^s)^2. The zero frequency has measure zero.
The fast box margin at a variable s is35595/1000-(51/5)s;
its zero is2373/680. This does not extend the uniform box estimate to
the larger threshold of the exact central source parameters.

## 3. Explicit multiplication and transport commutators

For a compact coefficient f define

 W_r(f)=(2pi)^(-1) integral <k>^r |fhat(k)|dk,
 alpha_r=1/[2 sqrt(pi(r-1))], r>1,
 beta_r=1/[2 sqrt(pi(r-1)(r-2))], r>2,
 P_s(f)=s 2^(s-2)[W_1(f)+alpha_(s-1)||f||_(H^s)],
 B_s(f)=||f||_infinity+P_s(f), M_r(f)=2^(r/2)W_r(f).          (7)

Polar integration proves integral(1+|xi|^2)^(-r)d xi=pi/(r-1)
and integral|xi|^2(1+|xi|^2)^(-r)d xi=pi/[(r-1)(r-2)]. Cauchy-Schwarz
therefore gives (2pi)^(-1)||vhat||_1<=alpha_r||v||_(H^r),
and (2pi)^(-1)|| |xi|vhat||_1<=beta_r||v||_(H^r).

For s=3.1, the mean value theorem and the convex inequality
(a+b)^(s-1)<=2^(s-2)(a^(s-1)+b^(s-1)) give

 |<eta+k>^s-<eta>^s|
 <=s 2^(s-2)(|k|<eta>^(s-1)+|k|^s).

Apply the L1*L2 and L2*L1 forms of Young's inequality to the two terms,
including the (2pi)^(-1) convolution factor. This proves

 ||[J^s,f]v||_2<=P_s(f)||v||_(H^(s-1)),
 ||fv||_(H^s)<=||f||_infinity||v||_(H^s)
                      +P_s(f)||v||_(H^(s-1)),
 ||fv||_(H^r)<=M_r(f)||v||_(H^r), r>=0.                     (8)

The last bound uses <eta+k><=sqrt(2)<eta><k>. In particular B_s(f)
is a valid full H^s multiplier bound, because H^s controls H^(s-1).

To isolate the leading transport derivative, Taylor expand j_s=<eta>^s.
Its Hessian is s<eta>^(s-2)I+s(s-2)<eta>^(s-4) eta eta^T, with operator
norm at most s(s-1)<eta>^(s-2). Integral Taylor remainder and
<eta+vk><=<eta>+v|k| yield

 |j_s(eta+k)-j_s(eta)-Dj_s(eta).k|
 <=s(s-1)2^(s-4)|k|^2[<eta>^(s-2)+|k|^(s-2)].

Here integral_0^1(1-v)dv=1/2 and v^(s-2)<=1 explain the coefficient.
Multiplying by |eta_i| and using the two Young inequalities proves

 [J^s,w.grad]u=-s sum_(i,j)(partial_j w_i)partial_ij J^(s-2)u+Rw u,
 ||Rw u||_2<=T_s(w)||u||_(H^(s-1)),
 T_s(w)=s(s-1)2^(s-4) sum_i[W_2(w_i)+beta_(s-1)||w_i||_(H^s)]. (9)

The sign follows independently by the Fourier factor
(ik_j)(-eta_i eta_j) times -s. Moreover
sum_ij||partial_ij J^(s-2)u||_2^2<=||u||_(H^s)^2, so pointwise
Cauchy-Schwarz controls the leading term by s||Dw||_(infinity,F)||u||_(H^s).

All constants use finite derivatives. Indeed

 W_r(f)<=alpha_(n-r)||f||_(H^n), n-r>1,
 ||f||_(H^n)^2=sum_(|gamma|<=n) n!/[(n-|gamma|)!gamma!] ||D^gamma f||_2^2, (10)

by Cauchy-Schwarz and the multinomial expansion of(1+|xi|^2)^n.
Use support area and derivative suprema for the latter terms. Also
||f||_(H^s)<=||f||_(H^3)^(4-s)||f||_(H^4)^(s-3), with constant1 by Holder
in Fourier space. Coefficients w,q in compact C^4 have the required norms;
W2(w) uses H4, W1(q) uses H3, and Hs uses H4. The given rho C5 suffices.

## 4. Perturbed energy and its small coefficient

The transport part w.grad contributes -div w/2 after integrating the
principal term, and the commutator (9) contributes the remaining terms.
The vector U symbol has norm at most1. Apply (8) to each q_i U_i u, using
pointwise |q.U J^s u|<=|q| |U J^s u| for its leading term. Thus

 Re <Aop u,u>_(H^s)
 <=-(kappa-E)||u||_(H^s)^2+R||u||_(H^(s-1))||u||_(H^s),     (11)
 E=||div w||_infinity/2+s||Dw||_(infinity,F)+||q||_infinity,
 R=T_s(w)+sum_i P_s(q_i).                                   (12)

Write M_V=sup_B ||D²V||_F, M_rho=sup_B ||D²rho||_F,
C_theta=delta||grad theta||_infinity. Taylor's integral formula gives
|V-Dz|<=M_V|z|²/2 and ||DV-D||_F<=M_V|z|. Since div(V-Dz)=0,

 ||Dw||_(infinity,F)<=[3+(9/2)C_theta]M_V delta,
 ||div w||_infinity<=(9/2)C_theta M_V delta,
 ||q||_infinity<=3M_rho delta.

Consequently

 E<=C_V delta,
 C_V=[3s+(9/2)(s+1/2)C_theta]M_V+3M_rho.                   (13)

For C_theta=2 this is41.7 M_V+3M_rho. If delta<=kappa/(2C_V), then
(kappa-E)^(-1)<=1000/1687. At delta33/2000 the sufficient exact
threshold is C_V<=3374/33, approximately102.2424. Any actual use requires
certified coefficient bounds on that containing disc; none are supplied here.

## 5. Velocity commutator, remote kernel, and strain

The vector symbol m=(cos theta sin theta,-cos²theta) has norm<=1 and
angular derivative(cos2theta,sin2theta) of norm1. Thus ||Dm(xi)||<=1/|xi|.
For |eta|>=1, |k|<=|eta|/2, integrate this derivative along the segment:
|m(eta+k)-m(eta)|<=2|k|/|eta|. Also <eta+k><=(3/2)<eta> and
<eta>/|eta|<=sqrt2. The desired estimate follows because
sqrt2(3/2)^s<=3^s and |k|<=<k>^s. In the complement, if |eta|<1 then
<eta+k><=sqrt3<k>; if |eta|>=1 and |k|>|eta|/2 then
<eta+k><=3<k>. Using |m(eta+k)-m(eta)|<=2 proves in all cases

 <eta+k>^s|m(eta+k)-m(eta)|
 <=2*3^s <k>^s <eta>^(s-1).

Young's inequality therefore gives

 ||[U,chi]v||_(H^s)<=C_U W_s(chi)||v||_(H^(s-1)), C_U=2*3^s. (14)

The off-diagonal kernels are Im and Re of(2pi)^(-1)(x+iy)^(-2):
K1=-xy/(pi r4), K2=(x²-y²)/(2pi r4). Every real derivative of total
orderj is a unit-complex multiple of(-1)^j(j+1)!(x+iy)^(-2-j)/(2pi).
Thus |D^gamma K_i|<=(j+1)!/(2pi) r^(-2-j). The local term-rho e2/2
has no effect across separated supports.

Define

 N= integral_(|X-P|>=5delta/2)|h(X)|/|X-P|² dX
   +integral_(R²\B_(3delta)(P)) |h(X)|/|X|³ dX.              (15)

For hfar=(1-zeta)h and X in B_(9delta/4), source distance d=|Y-P|
is at least5delta/2, so |X-Y|>=d/10 and >=delta/4. Therefore

 |D^gamma U_i hfar(X)|<=k_j N,
 k_j=100(j+1)!/(2pi)(4/delta)^j.                            (16)

For f supported in B_(9delta/4) set

 T_m(f)=(9sqrt(pi)delta/4)
  *sqrt(sum_(|gamma|<=m) m!/[(m-|gamma|)!gamma!]
       [sum_(beta<=gamma) choose(gamma,beta)||D^beta f||_infinity
                                  k_(|gamma-beta|)]²).     (17)

Leibniz, (10) and the area of that ball give
||f U_i hfar||_(H^r)<=T_m(f)N for0<=r<=m.

The raw strain kernel away from zero is
Ksigma(X)=y(3x²-y²)/(pi r6)=sin(3theta)/(pi r3), up to the already
fixed convolution sign, which is positive in this displayed expression.
Thus its absolute value is at most1/(pi r3). The local contribution is
-proportional to h_y(0), which vanishes. Near0 the integral is absolutely
convergent because h=O(r²); at infinity h is compactly supported.
Split at B_(3delta)(P), use |X|>=p-3delta there and Cauchy-Schwarz to get

 |sigma[h]|<=C_c H_h+N/pi,
 C_c=3delta/[sqrt(pi)(p-3delta)^3],
 H_h=||h||_(H^t(B_(3delta)(P))).                            (18)

Restriction norms dominate the restricted L2 norm. Similarly, foru=chi h,
|sigma[u]|<=2delta/[sqrt(pi)(p-2delta)^3] ||u||_2, using its smaller support.
These bounds are for RAW sigma; they are three times as generous as needed
for the prompt's scaling functional sigma/3.

## 6. Localization with its natural forcing cutoff

Put S=||chi h||_(H^s), A_h=||h||_(H^s(B_(2delta)\B_delta)),
Z=M_t(zeta), C_chi=M_t(chi), Q=g+sum_i B_s(q_i),
b_chi=||chi ell||_(H^s), T=V.grad chi. Define

 d_A=B_s(T),
 d_H=R C_chi+Q C_U W_s(chi) Z+b_chi C_c,
 d_N=sum_i T_4(chi a_i)+b_chi/pi.                           (19)

The exact whole-plane identity is

 Aop(chi h)=chi Lh+Th+(aP+q).[U,chi]h-chi ell sigma[h].       (20)

Indeed theta=1 on supp chi, so the local coefficients agree there;
outside that support only the expressly retained nonlocal terms survive.
For the near commutator use v=zeta h in (14), multiply by aP+q via (8),
and use ||zeta h||_(H^t)<=Z H_h. For the far term,
[U,chi]hfar=-chi U hfar, and(aP+q)chi=chi a, so (17) applies.
The support of T lies inside the annulus; any H^s extension H of h from
that annulus gives TH=Th everywhere, so ||Th||_(H^s)<=B_s(T)A_h by
an infimum over extensions. The same argument with chi,zeta proves the
restriction estimates just used; no unstated extension constant occurs.
Use (18) for the rank-one term and (11) for u=chi h. Then

 (kappa-E)S<=||chi Lh||_(H^s)+d_A A_h+d_H H_h+d_N N.         (21)

This already gives a forcing coefficient B_s(chi)/(kappa-E) for||tau Lh||Hs.
Multiplication by chi is not assumed to have norm1 in Hs.

## 7. The forcing coefficient exactly 1/(kappa-E)

Choose smooth radial lambda_in equal1 on B_delta and supported in
B_(9delta/8), and lambda_out zero on B_(15delta/8), equal1 outsideB_(2delta).
They take values in[0,1] and have disjoint nonzero supports. Put
lambda_A=1-lambda_in-lambda_out, pcut=lambda_A tau, F=tau Lh.
Then pcut is supported inside the prescribed annulus (vanishes on its
boundary), and lambda_A F=pcut Lh.

For X!=0, the off-diagonal kernel of J^s has the heat representation

 K_J(X)=[4pi Gamma(-s/2)]^(-1)
   integral_0^infinity u^(-2-s/2) exp(-u-|X|²/(4u))du.

To justify it without using a divergent scalar heat formula, use
lambda^(s/2)=Gamma(-s/2)^(-1) integral_0^infinity
(e^(-u lambda)-1+u lambda)u^(-1-s/2)du, valid for1<s/2<2 by two integrations
by parts. The subtracted polynomial operators have diagonal support, so
vanish off the diagonal. The integral there is absolutely convergent.
Dropping exp(-u) and substituting v=|X|²/(4u) give

 |K_J(X)|<=D_s|X|^(-2-s),
 D_s=2^s Gamma(1+s/2)/(pi|Gamma(-s/2)|).                    (22)

Now [J^s,chi](lambda_in F)=(1-chi)J^s(lambda_in F), and
[J^s,chi](lambda_out F)=-chi J^s(lambda_out F). Their supports are
separated by at leastdelta/8. The L1 norm of the kernel bound outside a
radiusd is(2pi D_s/s)d^(-s). Each cutoff is bounded by1, so their sum is
bounded in L2 by J_delta||F||2, with

 J_delta=(4pi D_s/s)(8/delta)^s.

The remaining commutator is bounded by P_s(chi)||pcut Lh||_(H^t), using(8).
Since||chi J^s F||2<=||F||Hs, this proves

 ||chi F||Hs<=||F||Hs+P_s(chi)||pcut Lh||Ht+J_delta||F||2.    (23)

Strictly, the smooth partitions may meet the annular boundary while being
flat there. To apply an extension, their value and all derivatives vanish
on the complement. Products with any restriction extension then agree as
distributions, which is all the product estimate requires.

Define

 e_A=sum_i M_t(pcut V_i),
 e_H=M_t(pcut)+Z sum_i M_t(pcut a_i)+||pcut ell||Ht C_c,
 e_N=sum_i T_4(pcut a_i)+||pcut ell||Ht/pi,
 f_H=Z[||tau V||infinity+1+||tau a||infinity]+||tau ell||2 C_c,
 f_N=sum_i T_0(tau a_i)+||tau ell||2/pi.                    (24)

Here vector infinity norms are Euclidean, and scalar tau<=1. The transport
term in pcut Lh uses an Hs annular extension, whose first derivatives have
Ht norm at most its Hs norm. All other terms split h into zeta h+hfar and
use(8),(17),(18). Likewise tau grad h=tau grad(zeta h), sincezeta=1 on
supp tau with a strict buffer. The L2 transport norm is at most
||tau V||infinity ||zeta h||Ht, since t>1. Thus

 ||pcut Lh||Ht<=e_A A_h+e_H H_h+e_N N,
 ||F||2<=f_H H_h+f_N N.                                   (25)

Combining(21),(23),(25) gives the theorem

 S<=K1||tau Lh||Hs+K2 A_h+K3 H_h+K4 N,
 K1=1/(kappa-E),
 K2=[d_A+P_s(chi)e_A]/(kappa-E),
 K3=[d_H+P_s(chi)e_H+J_delta f_H]/(kappa-E),
 K4=[d_N+P_s(chi)e_N+J_delta f_N]/(kappa-E).                (26)

This is a priori, and conditional on E<kappa and the stated coefficient
regularity. It contains no claim that the residual is small in the displayed
forcing norm or that the outer norm and N,H_h can be controlled by Lh.

## 8. Shrinking-cutoff scaling and the necessary outflow term

For fixed shapes, f_delta(X)=delta^p fshape((X-P)/delta), change Fourier
variables to obtain W_r(f_delta)<=delta^(p-r)W_r(fshape) and
||f_delta||Hr<=delta^(p+1-r)||fshape||Hr, fordelta<=1,r>=0.
The same conclusions hold for uniformly bounded shape families.
Taylor vanishing gives amplitudesw=O(delta²),q=O(delta),V=O(delta),ell=O(delta)
in local rescaled coordinates. T=V.grad chi has amplitudeO(1), whilea has
amplitudeO(1). The exact formulas above yield

 P_s(chi)=O(delta^(1-s)), R=O(delta^(2-s)), Q=O(delta^(2-s)),
 Z,C_chi=O(delta^(1-s)), W_s(chi)=O(delta^(-s)),
 d_A=O(delta^(1-s)), e_A=O(delta^(2-s)),
 d_H=O(delta^(3-3s)), e_H=O(delta^(2-2s)), f_H=O(delta^(1-s)),
 d_N,e_N=O(delta^(-3)), f_N=O(delta), J_delta=O(delta^(-s)).

Here boundedp>0 keeps C_c=O(delta); the ell terms are of lower size.
When E<=kappa/2 the denominators stay bounded. For s=3.1 the largest
allowed powers in(26) are therefore

 K2=O(delta^(3-2s)), K3=O(delta^(3-3s)), K4=O(delta^(-s-2)). (27)

Uniform shape hypotheses include the needed derivatives; one cannot deduce
(27) for arbitrary delta-dependent coefficients from pointwise amplitudes.

If a trajectory leaves a compact cutoff's support in finite forward time,
V.grad chi>=-epsilon chi is impossible at every point of that trajectory
starting wherechi>0. The scalar differential inequality implies
chi(Phi_t X)>=exp(-epsilon t)chi(X)>0 up to exit, a contradiction.
For a frozen fast-axis orbit crossing a factor-two annulus, elapsed time is
log2/A, so integration of its drop from1 to0 gives
sup|V.grad chi|>=A/log2. This last numerical constant is for the frozen
orbit; no perturbed-orbit comparison is certified here.

## 9. Joining an outer estimate

If an outer norm O controls A_h<=C_A O, and two already proved estimates
read S<=aF+bO+dR0 and O<=cF+epsilon S+eR0, then b epsilon<1 implies

 S<=[(a+bc)F+(d+be)R0]/(1-b epsilon).

This is sufficient by substitution. In the sense of an inference from
these inequalities alone for arbitrary nonnegative S,O, it is also necessary:
when b epsilon>=1, F=R0=0 permits anyS>0 with O=epsilon S (if b>0).
It is not necessary for invertibility of a particular operator with other
information. The lower-order and tail quantity R0 remains to be controlled.
Ordinary Hs annular control cannot be replaced without proof by a weaker
order, a Holder norm, or a degenerate conormal norm. Partition and frame
conversion constants belong to the outer proof.

## 10. Auxiliary semigroup: a conditional comparison, not the global inverse

The energy inequality alone does not imply surjectivity. If Aop generates
a strongly continuous semigroup on Hs, if its trajectories satisfy(11) and
the L2 energy inequality, and if a_s=kappa-E>0, set

 a0=1+(A+mu)/2-||div w||infinity/2-||q||infinity,
 a0-a_s=1+(A+mu)/2-kappa+s||Dw||_(infinity,F)>0.

For x=||S_A(t)u||Hs,y=||S_A(t)u||2, one has
 y<=exp(-a0 t)y0,
 x'<=-a_s x+R x^(1-1/s)y^(1/s).
The interpolation inequality here has constant1. For positive x, apply it
to x^(1/s); atzero use(x+epsilon)^(1/s) and pass to a limit. Integration gives

 x(t)^(1/s)<=exp(-a_s t/s)[x0^(1/s)
   +R/(a0-a_s)y0^(1/s)(1-exp(-(a0-a_s)t/s))].

Since y0<=x0,

 ||S_A(t)||_(Hs->Hs)<=[1+R/(a0-a_s)]^s exp(-a_s t).        (28)

Under the stated semigroup hypotheses its generator has inverse
Aop^(-1)=-integral_0^infinity S_A(t)dt, of norm at most
[1+R/(a0-a_s)]^s/a_s. This follows from the generator identity on its domain
and density, with exponential convergence, and yields both-sided inversion.
For the rank-one perturbation Aop+ell_delta sigma, invertibility is equivalent
to1+sigma[Aop^(-1)ell_delta]!=0, provided sigma is bounded on Hs and
ell_delta belongs toHs. The formula follows by solving for that scalar.
Raw sigma is bounded for s>2, for example by beta_s through its Fourier
symbol magnitude<=|xi| and the Cauchy-Schwarz estimate in section3.

The comparison and rank-one algebra are proved here conditionally. A full
semigroup/domain construction for the displayed C4 coefficients, and
extension of the energy inequality to that domain, is left OPEN in this
initial version. Neither a Neumann series for the unbounded w.grad term
nor an energy estimate alone closes this point. Even a proved auxiliary
whole-plane inverse would not match prescribed outer data or prove the
assembled global IPM inverse.

## Evidence, dependencies, and scope

The arguments above are independent derivations of the supplied srcloc1
claims, with its raw-strain convention made explicit. The scalar audit will
use exact rationals, Arb512, mpmath.iv180 and a fresh Arb1536 calculation.
Finite tests illustrate pointwise estimates; their universal proofs are
sections3 and5. No test on a finite grid replaces them. D_s is independently
evaluated through positive Gamma factors and through the reflection formula.
The fixed source coefficients are abstract box inputs; no trial derivative
suprema are invented. V22's source residual identity is already independently
proved in topic76. Dong Li's fractional Leibniz paper is bibliographic context
only; none of its unspecified constants or theorems is used here.
