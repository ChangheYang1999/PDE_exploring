# Independent derivation of the sharpened fractional constants

## Statement and status

This derivation independently checks the analytic constants and conditional closure box in T2-R2, frozen in `source/T2_sharp_constants_v02.md`. The central theorem and box are CONFIRMED under their stated background and candidate hypotheses. The exact target hash and limits of this audit are recorded in `verdict ledger`.

Work in two dimensions with J=(1-Delta)^(1/2), 0<s<=s0=1/1024 and omega(X)=(1+4|X|²)^(2/5). Scalar and vector functions are initially smooth with adequate decay; the estimates extend by completion. Tensor contractions use Euclidean pointwise norms unless coefficient bounds are explicitly component sums. Put

m=(sqrt(pi)/2) Gamma((1-s0)/2),
w=(8 sqrt(5)/5) 6^(-3/5),
k_u=m, k_w=m+8/5,
t_u=3m/2, t_w=3m/2+32/15,
b=1+3pi w/4, d=1+pi w/2.

For a smooth divergence-free coefficient field u, the commutator [J^s,u.D]J^-s has an unweighted bound

s (||Du||_Sigma+t_u||D²u||_Sigma),

and a weighted bound, with the second derivative weight on the coefficient,

||omega [J^s,u.D]J^-s h||_2
 <=s b ||Du||_Sigma ||omega h||_2
   +s t_w ||omega D²u||_Sigma ||h||_2.                 (1)

The distinction between weighted coefficient and weighted input in the second term is essential. Multiplication commutators cost s k_u||Da||_Sigma unweighted, or s k_w||omega Da||_Sigma with the output weight and an unweighted input. The dilation commutator has top weighted norm at most s d. These statements do not require a homogeneous negative norm.

Set q=1/(2sqrt(pi)),
p=2^s0 sqrt(1+s0)/(2sqrt(pi)), L=w m s0,
P=p(1+L)+qL, T=1+4L,
A=(4/5)q+qT+2P, B=(9/5)P.

Under the background coefficient caps and base energy hypotheses stated below, the proposed smooth and rough energy constants are respectively any upper bounds for the symmetric row sums of K and for A+B. The values402 and8/5 are certified by the exact rational calculation in `verification/ARITHMETIC_PROOF.md` and `verification/rational_certificate.json`. This theorem asserts no candidate residual certificate.

## 1. Kernel moments and weight ratios

The positive kernel representation is

J^s f=f+integral kappa_s(z)(f(X)-f(X-z)) dz,

kappa_s(z)=s/[2Gamma(1-s/2)] integral_0^infinity e^-t (4pi t)^-1 exp(-|z|²/(4t)) t^(-1-s/2) dt.

Gaussian polar integration gives, for k>s,

M_k=integral |z|^k kappa_s(z) dz
 =s 2^k Gamma(1+k/2) Gamma((k-s)/2)/[2Gamma(1-s/2)].

In particular M1/s<=m and M2=2s. The inequality uses Gamma(1-s/2)>=1 and the decreasing character of Gamma on(0,1]. These follow, for example, from log convexity and the negative logarithmic derivative at1, with monotonicity of that derivative. Since kappa_s is radial and decreasing, radial integration by parts also gives

integral |z|^k |Dkappa_s(z)| dz=(k+1)M_(k-1).

The endpoint terms vanish for k>1+s. Thus the two required moments are3M1 and4M2=8s.

The weight satisfies ||Domega||_infinity=w, omega>=1 and

omega(X)/omega(Y)<=(1+2|X-Y|)^(4/5)<=1+(8/5)|X-Y|.

The first inequality is the triangle inequality for(1,2X); the second is concavity. Differentiating omega shows that its radial derivative has its unique maximum at r²=5/4, giving w.

For a multiplication commutator, insert Da at X-tz in the mean-value formula and integrate t from0 to1. With the weight on Da, the remaining ratio is bounded by1+(8/5)t|z|. Hence the moment is

M1+(4/5)M2 <=s(m+8/5).

Without weights it is M1. Also the direct Lipschitz estimate for omega gives

||[J^s,omega]f||_2<=w M1||f||_2<=s w m||f||_2.          (2)

All sums of coefficient components are retained when this scalar estimate is applied to tensors.

## 2. Divergence-free transport remainder

Taylor-expand

u_j(X)-u_j(X-z)=sum_l partial_l u_j(X) z_l+R_j(X,z).

The first term gives exactly -s sum_(j,l) partial_l u_j partial_l partial_j J^-2 after composing with J^-s. In the remainder integrate the derivative off J^-s h. The term involving the derivative of R vanishes after summation, because

sum_j partial_(z_j) R_j=div u(X-z)-div u(X)=0.

Only Dkappa_s dot R remains. This cancellation is why the unweighted remainder coefficient is3m/2 instead of5m/2. It applies to u, not to an arbitrary non-divergence-free coefficient field.

The exact integral Taylor remainder has weight integral

integral_0^1 (1-t)[1+(8/5)t|z|]dt=1/2+(4/15)|z|.

Therefore its weighted L2 bound is

[3M1/2+(4/15)8s] ||omega D²u||_Sigma ||J^-s h||_2
 <=s t_w ||omega D²u||_Sigma ||h||_2.

No weighted J^-s norm is required here. Unweighted, the bound is s t_u||D²u||_Sigma||h||_2. The integration by parts is justified on annuli; the small-circle boundary is O(epsilon^(1-s)), and the large-circle boundary tends to zero on the initial core. Density gives the displayed extensions.

For the principal term, partial_l partial_j J^-2 has unweighted norm at most1. Its nonlocal kernel is partial_l partial_j G, with G=K0(r)/(2pi). Its local delta term commutes with the weight. The absolute first moments satisfy

integral |z| |partial_jj G| dz <=3pi/4,
integral |z| |partial_12 G| dz =3/2.

Indeed G''=(K0+K1/r)/(2pi) and G'/r=-K1/(2pi r). Integrate the elementary angular bounds and use integral r²K0(r)dr=pi/2 and integral rK1(r)dr=pi/2. These identities also follow directly from the positive heat representation of G and Gaussian moments. Since3/2<3pi/4, the Lipschitz commutator bound gives b. The same argument for I-J^-2 uses integral|z|G dz=pi/2 and gives d. This proves(1), including the local term.

## 3. Product estimate, with a direct proof of its constant

With the unitary Fourier convention in dimension2, Cauchy-Schwarz bounds multiplication H^(1+s) times H^s into H^s by(2pi)^-1 sqrt(sup_x I(x)), where

I(x)=integral <x>^(2s)/[<y>^(2+2s)<x-y>^(2s)]dy.

Write A=<y>² and B=<x-y>². Since <x>²<=2(A+B), and (1+t)^s<=1+st for0<s<=1,

I(x)<=2^s [integral A^(-1-s)dy+s integral A^-s B^-1dy].

The convolution of the two nonnegative radial decreasing functions A^-s and <.>^-2 is largest at zero. One elementary proof writes both as positive layer-cake integrals of centered-ball indicators; the intersection of any two balls is at most the smaller ball's volume, attained when their centers coincide. Truncation and monotone convergence cover the nonintegrable individual factors. Consequently the second integral is at most integral<y>^(-2-2s)dy=pi/s. The first integral has that same value. Thus

I(x)<=2^s pi(1+s)/s.

This proves the slightly stronger constant2^(s/2)sqrt(1+s)/(2sqrt(pi s)), and in particular T2's proposed constant2^s sqrt(1+s)/(2sqrt(pi s)). The argument handles Euclidean tensor contractions by taking the pointwise Fourier tensor norms before Cauchy-Schwarz; no dimension factor is lost.

The H^(1+s) to L-infinity constant is1/(2sqrt(pi s)). Commute J^s past omega on both sides of the product using(2). Since ||f||_2<=||omega J^s f||_2, the resulting weighted product constant, in units1/sqrt(s), is at most P defined above. Each positive expression used to majorize it increases with s, so evaluation at s0 is valid.

## 4. Rough transport energy

For W=U[k], the Fourier estimate gives

||DW||_infinity<=c_s||W||_(H^(2+s)),
||[J^s,W.D]f||_2<=c_s||W||_(H^(2+s))||J^s f||_2,
c_s=1/[2sqrt(pi s(1+s))].

The multiplier inequality behind the latter is |eta||<xi>^s-<eta>^s|<=|xi-eta|<eta>^s. The weighted commutator of omega with [J^s,W.D] has the exact divergence-free kernel Dkappa_s(z).(W(X)-W(X-z))(omega(X)-omega(X-z)). Its norm is at most3w M1||DW||_infinity. Combining this with(2) gives a weighted rough transport factor at most T.

Let E²=P2²+(128G1)²+(512G0)²+(512sqrt(20/21)H)², n=E(J^s k), and use the centrally odd weighted Riesz bound9/5. The ordered second-derivative expansion gives, in units n/sqrt(s), top energy at most

A P2²+B E P2.

The four contributions to A are the weight transport(4/5)q, the rough fractional commutator qT, and the two product terms2P. B is the final D²W.Dg term, using the weighted Riesz bound. No third derivative of W is used.

The gradient energy costs at most(q+p)(128G1)². The L2 term costs q(512G0)². The H term, from div J^s(Wg), costs at most p(512G0)(512sqrt(20/21)H), after discarding a factor sqrt(20/21)<=1. Hence the last two costs are bounded by(q+p/2) times the sum of those squared components. If A>=q+p, all lower components together cost at most A. Writing x=P2/E, the total is bounded by

A x²+B x+(q+p)(1-x²)<=A+B,

provided A>=q+p. That last scalar condition and A+B<8/5 are verified separately. Removing the H component does not change this argument or its constant.

## 5. Background matrix and conditional closure

Suppose the component-sum caps are

(C,U1,U2,U3,R1,R2,R3,R4)<=(2,6,24,160,22,32,80,2048),

where U1=||Du||_Sigma, Uj=||omega D^j u||_Sigma for j>=2, R1=||D rho||_Sigma and Rj=||omega D^j rho||_Sigma for j>=2. Under the same canonical velocity and parity hypotheses as Analysis II, the differentiated identities give the nonzero entries

K00=dC+bU1+(t_w+2k_w)U2+k_wR2,
K01=k_w(U3+2R3)/128, K02=k_wR4/512,
K11=C+U1+(t_u+k_u)U2+k_uR2, K12=k_uR3/4,
K22=C+U1+t_uU2+k_uR2,
K32=sqrt(20/21)k_u(U1+R1), K33=C.

The H row follows from exact divergence forms. The dilation is treated separately, so u remains divergence free. These estimates bound the absolute smooth commutator energy by s e^T K e. The largest symmetric row sum is a valid upper bound because e has nonnegative entries and2e_i e_j<=e_i²+e_j².

If a certified base energy rate mu is available, the same maximal-domain construction as the baseline gives rate mu-C_bg s-c_U n/sqrt(s), with C_bg and c_U bounded as above. The operator domains, normalized trace, complete low-metric ball and low inverse still require their original hypotheses. Replacing numerical constants in an energy estimate does not dispense with them. The scalar parameter box and candidate residual must be checked separately.

Dependencies are the positive Bessel kernel representation, elementary polar integrals and gamma identities, Fourier Plancherel and Cauchy-Schwarz, the proved centrally odd weighted Riesz bound, and the baseline generator construction. This result does not assert a small residual or an exact IPM solution.

## 6. Certified box and scope of the conclusion

For the A2 realization with its stated base energy inequalities, H decay19/5, canonical velocity, fixed-exponent normalization and origin hypotheses, set mu=297/1000, s=1/8192, r=43/50000 and eta=5289/50000000. The rate on the closed normalized N_s ball is greater than123/1000. The exact arithmetic proof gives derivative bound below0.02196 and low contraction below0.0059. Thus a residual satisfying N_s(F)<=eta, together with all the original background and realization hypotheses, gives the same conditional fixed-point conclusion as the baseline. The invariant normalization uses f_y(0)=a0 c[h], as in T4-001, and the low-metric completeness argument is unchanged. Replacing these constants neither changes the scaling chart nor removes a candidate hypothesis.

The audit does not certify T2's floating sensitivity studies or claim that any candidate has small residual. The component projections of N_s(F) are P2(J^s F), G1(J^s F), G0(J^s F), H(J^s F). For raw F, unweighted components contract under J^-s, but a weighted P2(F) implication requires the separately proved comparison E2(F)<=N_s(F)/(1-34s). In particular a statement P2(F)<=eta does not follow just by projecting the N_s definition. Decimal component bounds must also be rounded outward.

Dependencies: the A2 P7.5 base energy and P8.1/P8.4 realization, T4-012's independent audit of mu=297/1000, and the centrally odd weighted Riesz estimate. Every new constant is derived above; `verification/ARITHMETIC_PROOF.md` supplies an elementary rational enclosure without numerical special functions.
