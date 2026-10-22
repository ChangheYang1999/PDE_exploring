# A normalized tail repair with an unweighted L2 residual

Status: complete informal argument before the new finite norm computation.
This constructs explicit improved trial functions. It proves neither an
exact stationary solution nor a small unweighted residual bound.

## 1. Statement, dependencies and exact definitions

Let rho0 be the exact normalized modal trial in modal_repair/PROOF.md,
with its canonical full-plane velocity U0 and c0=1/k. The exact dyadic
k satisfies 0<k<1/3. Set beta=2k-1, beta2=3k-2<-1, R_b=exp(tplus).
Topic104 (far_residual_obstruction, including its mandatory addendum)
proves the uniform exterior expansion

 epsilon0=(c0X+U0).grad rho0-rho0
          =r^beta Epsilon(theta)+o(r^beta),

with Epsilon a finite odd-sine polynomial and nonzero. The more precise
finite exterior representation of outer_leading_cancellation and
outer_majorant gives an error bounded by
O(r^beta2(1+log r)^q) for some finite integer q. This is justified in
Section4, rather than inferred from the o term alone. Define exactly

 H(theta)=k Epsilon(theta)/(1-k).                                  (1)

The angular function has a factor

 H(theta)=cos(theta)^2 sin(theta) Q(cos(2theta)),                    (2)

where Q is a polynomial of degree at most520. All its coefficients are
exact real expressions in the input dyadics, exponential radial factors
and the exactly defined normalization scalar z. Certified intervals for
those coefficients are enclosures, not their definitions.

Put b(s)=(s-1)^8(2-s)^8 for 1<s<2 and b(s)=0 otherwise. Let

 B=integral_1^2 b(s)ds=(8!)^2/17!,
 J_b=integral_1^2 s b(s)ds=3B/2,
 chi(s)=B^(-1)integral_1^s b(t)dt  for 1<s<2,
 chi(s)=0 for s<=1, chi(s)=1 for s>=2,
 J_chi=integral_1^infinity chi(s)s^(beta-2)ds.                       (3)

Then b is C7, chi is C8, 0<=chi<=1, J_b>0, and
0<J_chi<=1/(1-beta). Define the signed angular scalar

 I_H=(1/pi)integral_0^(2pi) sin(3theta)H(theta)dtheta,               (4)

which is precisely the sin(3theta) coefficient of H. For any
T>=max(R_b,L,1), define

 h_T^tail=chi(r/T) r^beta H(theta),
 g_T=x^2 y b(r/T),
 lambda_T=4 I_H J_chi T^(beta-3)/J_b,
 h_T=h_T^tail-lambda_T g_T,
 rho_T=rho0+h_T.                                                   (5)

Every value is given by exact finite formulas or an explicitly specified
convergent integral. No approximate strain value is substituted for
lambda_T. The claim is:

(a) rho_T preserves the parity, local factorization and center value a(0)=1.
It equals rho0 on r<=T and has the same raw canonical strain at zero,
so 3c0-psi[rho_T]_xy(0)=1 exactly. It has a canonical sublinear velocity.
Its global local regularity is at least that of the task's P2 trial class;
its center regularity is exactly unchanged by the correction. This does
not assert that rho_T is stationary, or promote P2 to P_infty.

(b) Its residual F(rho_T,c0) belongs to unweighted L2(R2).

(c) Let N be any rigorous upper bound for ||Q||_(L_infinity[-1,1]) and
let I be any upper bound for |I_H|. With alpha=(3-k)/2 set

 C=L^(k-3){2^alpha N
       +[4 I 2^(-16)/((1-beta)J_b)]5^alpha}.                      (6)

For the factor weight W(r)=(1+(r/L)^2)^((k-3)/2),

 sup_X |h_T/(x^2 y W(r))| <= C T^(k-1).                            (7)

The quotient is interpreted through its continuous factor on the axes.
Consequently these exactly normalized repairs are arbitrarily close to
rho0 in the weighted factor norm. Since H is nonzero, h_T is not in
unweighted L2. Thus the affine obstruction of104 does not prohibit them.
No finite-radius L2 residual estimate or closing inequality is claimed.

## 2. Angular factorization, canonical signs and finite coefficient data

Write P0(zeta)=sum_(m=0)^259 (A_m0+z delta_m0) T_m(zeta), and
P1(zeta)=sum_(m=0)^259 A_m1 T_m(zeta), with zeta=cos(2theta).
The T_m are the Chebyshev cosine polynomials; z without the suffix is
the exact scalar normalization and is a different variable. Let d_j be
the sine projection of cos^2(theta)sin(theta)P0(cos(2theta)). For
n=1,...,261 put m=2n, a=k+1,

 F_n=((a-m)d_(n-1)+(a+m)d_n)/2,
 v_n=-m F_n/(m^2-a^2), w_n=a F_n/(m^2-a^2),
 V(zeta)=sum_n v_n T_n(zeta),
 Z(zeta)=sum_n w_n U_(n-1)(zeta),                                 (8)

where d_261=0 and U_j are the second Chebyshev polynomials. Then the
leading polar angular velocity coefficients are V(cos2theta) and
sin(2theta) Z(cos2theta). Direct differentiation gives

 Epsilon(theta)/(cos^2 theta sin theta)
 =R_b^(3-beta)(beta/k-1)P1(zeta)
 +R_b^(5-beta){k V(zeta)P0(zeta)
    +Z(zeta)[(3zeta-1)P0(zeta)-2(1-zeta^2)P0'(zeta)]}.             (9)

For example, differentiate cos^2 theta sin theta P0(cos2theta)
and multiply the derivative by sin2theta Z. Division by cos^2 theta
sin theta leaves the bracket in (9); both sides are trigonometric
polynomials, so the identity extends to the axes. The degrees of V,P0,Z
are at most261,259,260 respectively. The bracket has degree at most260.
Thus the degree bound520 and the factorization (2) follow algebraically.

Let e_j, j=0,...,521, be the coefficient of sin((2j+1)theta)exp(beta tau)
in epsilon0, tau=log(r/R_b). Then the sine coefficient of H is

 h_j=[k/(1-k)]R_b^(-beta)e_j.                                     (10)

The complete two-method 522-frequency certificate in topic42 supplies
independent enclosures for all these exact coefficients. A new pair of
small computations will bound Q in different ways from those respective
certified vectors. It does not recompute or change the old trial.

One reconstruction is a backwards signed Fourier recurrence. Write
Q(cos2theta)=sum_(m=0)^M q_m cos(2m theta), M=520, and extend q_m=0
for m>M. The upper sine equations give

 q_M=8h_(M+1),
 q_(j-1)=8h_j-q_j+q_(j+1)+q_(j+2), j=M,...,2,
 q_0=(8h_1-q_1+q_2+q_3)/2.                                      (11)

The remaining sine equation h_0=(2q_0-q_2)/8 is guaranteed by (9).
Interval containment of zero in that compatibility relation is only a
diagnostic, not a proof of exact divisibility. The bound N=sum|q_m|
is valid on the entire circle and on [-1,1].

A distinct reconstruction sets w=exp(2i theta), shifts the Laurent
series of 2iH to obtain a polynomial of degree2M+3, and divides by
(w-1)(w+1)^2/4. To verify the divisor directly,

 2i cos^2(theta)sin(theta)
   =(exp(3i theta)+exp(i theta)-exp(-i theta)-exp(-3i theta))/4.

After the respective shifts, the quotient has degree2M and symmetric
coefficients q_m/2 at indices M+m and M-m, and q_0 at index M.
Three synthetic divisions therefore give a separate interval route.
Again exact divisibility is justified by (9), not by a zero-containment
test. The first reconstruction uses the prior Arb convolution enclosures;
the second uses the prior independent iv direct-product enclosures.

The raw canonical strain of a function vanishing near zero is

 sigma[h]=integral K_s(Y)h(Y)dY,
 K_s(Y)=y(3x^2-y^2)/(pi r^6)=sin(3theta)/(pi r^3).                 (12)

The plus sign follows from -PV(K_s*h)(0) and oddness of K_s, as explicitly
reconstructed in topic104's corrected addendum. For x^2 y b(r), this is
+(1/4)integral r b(r)dr. Equations(4),(5),(12) give exactly

 sigma[h_T^tail]=I_H J_chi T^(beta-1),
 sigma[g_T]=T^2 J_b/4,
 sigma[h_T]=0.                                                    (13)

The strain integrals converge absolutely. They vanish locally near zero,
and their far radial exponent is beta-2<-1. This proves the center
normalization assertion without an uncontrolled numerical cancellation.

## 3. Regularity, exact formula for the scalar and weighted cost

The joins of b and chi have the stated differentiability because b has
zeros of order8 at both endpoints. Their factors vanish identically on a
neighborhood of zero, so the powers of r and angular polynomial create
no new center singularity. The correction is C7 globally, piecewise
smooth, with finitely many angular modes, and is O(r^beta) with derivative
O(r^(beta-1)) at infinity. Its finite-mode canonical Green integrals
converge. The exterior particular velocity is O(r^beta); homogeneous
decaying terms are O(r^-3). The interior velocity is analytic and finite.
Consequently rho_T and its velocity obey sublinear growth. Although the
density agrees with rho0 inside T, the nonlocal velocity changes there;
only its strain at zero has been fixed exactly.

Symmetry of b about3/2 gives J_b=3B/2, and b(s)<=2^-16. Integrating by
parts in J_chi, using beta-1<0, gives

 J_chi=[(1-beta)B]^(-1) integral_1^2 b(s)s^(beta-1)ds
       <=1/(1-beta).                                            (14)

This is also a convenient exact reproducible integral for lambda_T.
For a finite-expression alternative, expand b as a degree16 polynomial,
integrate each s^(j+beta-1) over [1,2], and divide by (1-beta)B;
terms with j+beta=0 use log2. For the exact input k none of these
finitely many denominators is zero. Coefficients can be stored in exact
JSON if that evaluation is used. No numerical quadrature is needed for
the upper bound in (14).

On r>=T, the tail factor divided by W satisfies

 r^(beta-3)|Q|/W(r)
 =L^(k-3)r^(k-1)(1+L^2/r^2)^alpha |Q|
 <=L^(k-3)T^(k-1)2^alpha N,                                     (15)

since T>=L and k-1<0. The compact compensator is supported in T<=r<=2T.
Using (5),(14), b<=2^-16 and T>=L gives

 |lambda_T| b(r/T)/W(r)
 <=[4I 2^-16/((1-beta)J_b)] T^(beta-3)
                  (1+4T^2/L^2)^alpha
 <=L^(k-3)T^(k-1)[4I 2^-16/((1-beta)J_b)]5^alpha.                 (16)

Equations(15),(16) prove(7). For any prescribed epsilon>0, taking
T at least max(R_b,L,1,(C/epsilon)^(1/(1-k))) gives cost at most epsilon.
The constants in a printed numerical specialization will be enclosed by
two interval methods and independently audited before use.

## 4. Why the repaired residual is square integrable

The original exterior density powers are
k-j(1-k)-2l for (j,l)=(0,0),(1,0),...,(5,0),(0,1),(1,1),(2,1),(0,2),
and the exponentially joined term with power3-bo and a finite polynomial
in log(r/R_b). After k and beta, every density exponent is at most
beta2=3k-2; the (0,1) power k-2 is smaller, and bo>120.
The c0 r^k linear contribution vanishes. Every particular velocity-density
product has exponent beta_i+beta_j-1. The sole exponent beta is (i,j)=(0,0).
Every remaining such product is at most k+beta-1=beta2. Canonical
homogeneous products are at most k-4<beta2. Polynomial logarithms at
strictly smaller powers can be bounded by r^beta2 times a finite power
of 1+log r. This proves the more precise original residual remainder.

For r>=2T, h_T=r^beta H exactly, with its derivative given by that
homogeneous formula. Its canonical velocity is r^beta times a finite
angular function plus finitely many decaying homogeneous modes. No
growing homogeneous stream term occurs in the canonical inverse.
At fixed c0 the exact change in the residual is

 F(rho_T,c0)-epsilon0
  =(c0 E-1)h_T+U0.grad h_T+U[h_T].grad rho0+U[h_T].grad h_T.        (17)

The first term at exponent beta is (beta/k-1)r^beta H, which cancels
r^beta Epsilon by (1). The next two terms have exponent at most beta2;
the last has exponent2beta-1=4k-3<beta2. Homogeneous contributions
decay faster. Thus

 F(rho_T,c0)=O(r^beta2(1+log r)^q)                               (18)

for some finite q and constants depending on T. Since beta2<-1,
its squared polar radial integral converges at infinity. On every compact
set the residual is bounded by the stated local regularity and canonical
velocity, so it is in L2 globally. There is no numerical claim about the
size of that finite norm. Moving the repair farther outward can make the
weighted profile change smaller while leaving a larger unweighted
residual contribution inside the repair radius.

Finally, H is nonzero by topic104's nonzero frequency-one coefficient.
On some angular interval it is bounded away from zero. Hence h_T has
infinite unweighted L2 norm, since its tail gives integral r^(2beta+1)dr
and beta+1=2k>0. This explicitly places the improved trial outside the
excluded affine class while remaining arbitrarily close in the weighted
factor topology. Leading Theta0 stays fixed; this construction alone
does not establish an uncertainty class around X3, control the source
point, prove a global inverse, or solve the nonlinear equation.
