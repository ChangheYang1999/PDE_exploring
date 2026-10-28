# An explicit high residual norm and a variation majorant

Status: analytic derivation complete; numerical evaluation and independent audit pending. This file fixes a new, equivalent high norm. It does not assign a numerical value to the unspecified norm choices in earlier topics.

## Statement and norm choices

Let rho be the exact normalized C6-joined modal trial of topics15 and68, reconstructed from the read-only original with SHA256 a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874. Write F=(ell X+U[rho]).grad rho-rho, ell=1/k, and k=1615536043799051/9007199254740992. Put t=log r, p(theta)=cos(theta)^2 sin(theta), sigma=25/4, delta=9/5, gamma=-1/2 and nu=53/10. Define

 a_*(t)=exp(delta t)(1+exp t)^(-nu), b_*(t)=exp(3t)a_*(t).

Use the order s of proof 130, which equals sigma on |cos(theta)|<=1/2. Put h(u)=exp(-1/u) for u>0 and h(u)=0 otherwise, S(u)=h(u)/(h(u)+h(1-u)), and

 chi(theta)=S((16-144 cos(theta)^2)/7).

Thus chi=1 on |cos(theta)|<=1/4 and chi=0 on |cos(theta)|>=1/3. Fix any smooth nonnegative inhomogeneous Fourier resolution (Delta_j) on the cylinder with sum_j phi_j(Lambda)^2=1, Lambda=(1+xi^2+n^2)^(1/2), support 2^(j-1)<=Lambda<=2^(j+1) for j>=1 and 1<=Lambda<=2 for j=0. Define the variable-order norm by sum_j ||2^(j s)Delta_j v||_2^2. Lebesgue measure is dt dtheta, theta in[0,2pi), and the scalar Fourier transform is unitary.

Write g=F/(r^3 p a_*), g_axis(t)=g(t,pi/2), and define

 eta_*^2=||g_axis||_{H^sigma(R)}^2
       +sum_j ||2^(j s)Delta_j[p(g-g_axis)]||_2^2
       +||chi(g-g_axis)||_{H^sigma(C)}^2.                 (1)

This is the Y_full target norm of proof 173 with the displayed choices. Its space is the same as there, with equivalent norm: a_*/a_H and its inverse have all derivatives bounded, and the two angular cutoffs differ only in a region of constant order sigma. Consequently the qualitative inverse and conditional existence theorems transfer, with their constants changed. No numerical bound for those changed constants is asserted.

The cofactor g is an even trigonometric polynomial of angular frequency at most N=1044. Write g=sum_n q_n(t)cos(2n theta). Let

 A=sum_n ||q_n||_{L1(R)}, B=sum_n |D_t^7 q_n|(R),
 R^2=(2^sigma/pi)(A^2+2B^2), C_L^2=2pi(1+L^2)^sigma R^2. (2)

Here D_t^7 q_n is a finite signed measure. The formulas below give finite computable majorants for A and B. With C_chi defined below,

 eta_*^2 <= R^2 + 2^(2sigma) C_(N+3)^2 +4 C_chi^2 C_N^2. (3)

## Fourier proof, including the knot contributions

The density is C6 across every join. Its residual is C5 and piecewise analytic, so the sixth derivative of each q_n is piecewise smooth and its seventh distributional derivative consists of the classical seventh derivative and the jumps of the sixth derivative. No derivative of a Dirac mass occurs. The endpoint bounds below show that all derivatives through order6 tend to zero at infinity. Thus integration by parts in the measure sense gives

 |qhat_n(xi)| <= (2pi)^(-1/2) min(||q_n||_1, |xi|^(-7)|D^7 q_n|(R)).

Split the Sobolev integral at |xi|=1. Since integral_1^infinity xi^(2sigma-14) dxi=2, this gives ||q_n||Hsigma^2 <=(2^sigma/pi)(||q_n||_1^2+2|D^7q_n|^2). The triangle inequality, first in the two-dimensional vector of these two bounds and then for the finite angular sum, proves ||g_axis||Hsigma<=R and ||g||Hsigma(C)<=C_N. Subtracting g_axis at most doubles the coefficient majorants. The Fourier coefficient l1 norm of p=(sin theta+sin3theta)/4 is1/2, so ||p(g-g_axis)||Hsigma<=C_(N+3). Finally 2^(j s)<=2^(j sigma)<=2^sigma Lambda^sigma on every band. The exact square partition proves the middle bound in(3), without an unspecified overlap factor.

For the last term, let M_8 bound ||chi^(8)||infinity. Its Fourier coefficients obey |chihat_n|<=M_8/|n|^8 for n!=0 and |chihat_0|<=1. Since sum_(n>=1)n^(-7/4)<=7/3, put

 C_chi=2^(sigma/2)[1+2^(1+sigma/2)(7/3)M_8].             (4)

The inequality <(xi,n+m)>^sigma <=2^(sigma/2)<(xi,n)>^sigma<m>^sigma and Young's inequality prove the multiplier bound with this constant.

Here is an entirely explicit M_8. Set H_0=1 and H_j=j!(9j)^j for1<=j<=8. Cauchy's formula on the complex disk of radius u/2 about u>0 gives |h^(j)(u)|<=j!(2/u)^j exp(-2/(9u)); maximizing the right side gives the stated larger bound H_j. On0<=u<=1 the denominator d=h(u)+h(1-u) is at least exp(-2), while |d^(j)|<=2H_j. Put R_0=exp2 and recursively

 R_j=exp2 sum_(l=1)^j binom(j,l) 2H_l R_(j-l),
 S_j=sum_(l=0)^j binom(j,l) H_l R_(j-l).

These bound the derivatives of1/d and S. Outside[0,1], S is constant and the derivatives vanish. The inner angular function equals -56/7-(72/7)cos2theta, and its kth derivative is bounded by Q_k=(72/7)2^k for k>=1. Faà di Bruno's formula therefore permits

 M_8=sum_(l=1)^8 S_l B_(8,l)(Q_1,...,Q_(9-l)),           (5)

where B_(n,l) is the partial exponential Bell polynomial, defined by B_(0,0)=1 and B_(n,l)=sum_(j=1)^(n-l+1) binom(n-1,j-1)Q_j B_(n-j,l-1).

## Radial and angular coefficient majorants

Let m=1/a_*. If z=exp t/(1+exp t), define P_0(z)=1 and

 P_(j+1)=(-delta+nu z)P_j+z(1-z)P_j'.

Then m^(j)=m P_j(z). Let C_j be the sum of the absolute rational coefficients of P_j. For t<=0, m<=2^nu exp(-delta t); for t>=0, m<=2^nu exp((3-gamma)t).

Write H=r^(-3)rho, with sine coefficients H_j(t), and use the canonical radial velocity coefficients P_n,Q_n of proof 68. The raw residual is

 (3ell-1)H+ell H_t -(sum_n P_n cos2n theta)(3H+H_t)
                   +(sum_n Q_n sin2n theta)H_theta.    (6)

There are262 density sine slots and261 velocity modes, so its odd sine index is at most522. Dividing by sin theta has coefficient l1 norm at most2*522+1. On cosine polynomials of degree at most522 vanishing at the vertical axis, division by cos^2 theta has coefficient l1 norm at most2*522^2: its constant coefficient is2 sum_(m>=1)(-1)^(m-1)m A_m, and its jth coefficient is4 sum_(m>j)(-1)^(m-j-1)(m-j)A_m. Summing each input column gives2m^2. Thus

 C_div=2*522^2*(2*522+1)                                (7)

bounds the exact cofactor division and every radial derivative. No angular modes are dropped.

## The finite spline interval

Let t_-,t_+ be the exact first and last knots, L=t_+-t_-, and h_min the smallest positive knot gap. The original representation is sum_m S_m(t)Phi_m(theta), with Phi_m=cos^2(theta)sin(theta)cos(2m theta) and coefficient l1 norm at most1/2. Set

 H_j^*= (1/2)sum_m max_i|S_(m,i)| * 2^j*7!/(7-j)! *h_min^(-j), 0<=j<=7,
 H_8^*=0.

The nonnegative partition of unity for B-splines gives j=0. Each derivative replaces controls by a difference times the current degree divided by a positive knot span; that span is at least h_min. Induction proves the bounds on every open knot interval.

Let I_0=sum_n|I_n(t_-)|+H_0^*/6 and J_0=exp(2L)sum_n|J_n(t_+)|+H_0^*(exp(2L)-1)/2. The canonical Green integral equations give these bounds throughout the finite interval: their forward decay rates are at least6, and the largest backward growth rate is2. Multiply both by exp(2t_+) to bound the scaled Green coefficients. Define

 R_j=exp(2t_+)sum_(l=0)^j binom(j,l)2^(j-l)H_l^*,
 I_j=524 I_(j-1)+R_(j-1), J_j=520 J_(j-1)+R_(j-1), j>=1,
 P_j^*=261(I_j+J_j), Q_j^*=261(I_j+J_j)+R_j.

The first two recurrences use (e^(2t)I_n)'=-(2n+2)e^(2t)I_n+e^(2t)H_(n-1) and (e^(2t)J_n)'=(2n-2)e^(2t)J_n-e^(2t)H_n. Let

 F_j^*=|3ell-1|H_j^*+ell H_(j+1)^*
 +sum_(l=0)^j binom(j,l)[P_l^*(3H_(j-l)^*+H_(j-l+1)^*)+523Q_l^*H_(j-l)^*].

For0<=j<=7 set

 M_j=C_div 2^nu max(exp(-delta t_-),exp((3-gamma)t_+))
                   *sum_(l=0)^j binom(j,l) C_l F_(j-l)^*.

The finite interval contributes at most L M_0 to A and L M_7 to the classical part of B. The total middle-side contribution to all jumps of the sixth derivative is at most2*1558 M_6, including its two outer endpoints.

## The two ends and the exact cancellations

Every end coefficient is an exact finite sum exp(e tau)p(tau), with interval enclosures for its coefficients and exact rational e. For tau<=0 and e>v, the bound |tau|^j exp((e-v)tau)<=j!/(e-v)^j proves the left majorant. For tau>=0 and e<v the corresponding right bound is j!/(v-e)^j. Terms with e=v are allowed only for constant p. Apply this rule after taking each required derivative.

At the inner end take v=19/10. The density constant is (sin theta+sin3theta)/4, and the velocity constants are P_1=Q_1=c=3ell-1 with all others zero. The constant part of(6) is exactly zero: -c cos2theta*3p+c sin2theta*p'=-c p. Remove these constants algebraically. All remaining exponents are at least2. Let h_j,p_j,q_j denote their derivative coefficient majorants at rate v. The constant density has sine l1 norm1/2 and its angular derivative l1 norm1. Thus a rate-v bound for the jth raw residual derivative is

 S_j=|3ell-1|h_j+ell h_(j+1)+|c|(3h_j+h_(j+1)+523h_j)
 +sum_(l=0)^j binom(j,l){p_l[ (3/2)1_(j=l)+3h_(j-l)+h_(j-l+1)]
                         +q_l[1_(j=l)+523h_(j-l)]}.

Products of two rate-v remainders satisfy the same bound because tau<=0. The weighted cofactor derivative is at most

 M_j^-=C_div 2^nu exp(-delta t_-)sum_(l=0)^j binom(j,l)C_l S_(j-l)

times exp((v-delta)(t-t_-)). Its contributions to A and the classical part of B are M_0^-/(v-delta) and M_7^-/(v-delta). Its endpoint jump contribution is M_6^-.

At the outer end use rate k-3 for H, rate k-1 for P,Q, and rate 2k-4 for (3ell-1)H+ell H'. In the last expression the leading density exponent k-3 cancels exactly because (3+k-3)/k-1=0; the next exponent is2k-4. Form the derivative coefficient majorants by the right-end rule, then the product bound in(6), with its linear part already combined. This gives S_j^+. Define

 M_j^+=C_div 2^nu exp((3-gamma)t_+)sum_(l=0)^j binom(j,l)C_l S_(j-l)^+.

The remaining rate is2k-1/2<0. The outer contributions are M_0^+/(1/2-2k), M_7^+/(1/2-2k) and M_6^+. Therefore the fully explicit bounds used in(2) are

 A <= L M_0+M_0^-/(v-delta)+M_0^+/(1/2-2k),
 B <= L M_7+M_7^-/(v-delta)+M_7^+/(1/2-2k)
                         +2*1558 M_6+M_6^-+M_6^+.       (8)

All operations in(4)-(8) can be evaluated by directed Arb arithmetic, starting from exact binary rationals in the read-only original and the previously audited scalar normalization and Green boundary enclosures. The bound deliberately sacrifices sharpness. It proves neither residual smallness nor a bound for an inverse, and it does not remove the two conditions of proof 174.
