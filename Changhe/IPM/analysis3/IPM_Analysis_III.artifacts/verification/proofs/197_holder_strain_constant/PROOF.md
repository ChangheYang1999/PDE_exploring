# The angular factor cannot be deleted from the Holder strain bound

## Claim and corrected inequality

For p>=0 and0<alpha<1, let C^alpha_p be the bounded parity class of functions even in x and odd in y, with finite global x-Holder seminorm and

 [h]_(y,p)=sup_(x,y!=y') |h(x,y)-h(x,y')|/(|x|^p |y-y'|^alpha).

At x=0 the quotient is interpreted by the vanishing trace when p>0. Define the absolutely convergent local strain

 c_<R[h]=(1/pi) integral_(|X|<R) sin(3theta) r^(-3) h(X) dX.

For p+alpha>1 the valid elementary bound from proof 25 is

 |c_<R[h]| <= [h]_(y,p) R^(p+alpha-1)
                /(pi(p+alpha-1)) A_(p,alpha),
 A_(p,alpha)=integral_0^(2pi) |sin3theta| |cos theta|^p |sin theta|^alpha dtheta.

Oddness gives |h(x,y)|<=[h]_(y,p)|x|^p|y|^alpha. Polar integration proves this bound, with no velocity or inverse assumption. In particular the simpler constant4 is always sufficient, since A_(p,alpha)<=integral|sin3theta|=4.

The version printed in S2_CALPHA_THEORY section6 that deletes A_(p,alpha) is false. We construct a counterexample with p=1,alpha=1/100 andR=1. Smooth compactly supported examples with the S2 parity, zero origin jet and the same strict violation also exist. This concerns the functional bound, not a claimed inverse domain or any global image norm.

## Explicit angular function and its seminorm

Define an odd piecewise-linear function f on R by its values for q>=0:

 f(q)=20q                    for0<=q<=1/20;
 f(q)=1                      for1/20<=q<=3/2;
 f(q)=7-4q                   for3/2<=q<=2;
 f(q)=-1                     for2<=q<=10;
 f(q)=q-11                   for10<=q<=11;
 f(q)=0                      forq>=11.

The pieces agree at their endpoints. Thus ||f||_infinity=1 and Lip(f)<=20. Interpolating |f(q)-f(q')|<=min(2,20|q-q'|) gives

 [f]_C^alpha <= 2^(1-alpha)20^alpha=2*10^alpha=:L_alpha.

Take a smooth even cutoff chi(x) with0<=chi<=1,chi=1 for|x|<=1 andchi=0 for|x|>=2. For x!=0 put

 h(x,y)=chi(x)|x|^(1+alpha) f(y/|x|),

and define h(0,y)=0. The function is bounded and compactly supported, since f vanishes for|q|>=11. It has the required parity. For fixed x, dilation in y proves [h]_(y,1)<=[f]_C^alpha<=L_alpha.

It also has finite global x-Holder seminorm. On each linear angular piece its x-derivative is bounded by a constant times |x|^alpha, with q confined to[-11,11]; the cutoff derivative is bounded and compactly supported. Across the finitely many interfaces h is continuous, so this proves a global Lipschitz bound. A bounded Lipschitz function is globally C^alpha. Thus h belongs to the stated space. Near0 it is O(r^(1+alpha)), ensuring absolute convergence of c_<1.

On the unit disk chi=1. The polar formula is therefore

 pi*alpha*c_<1[h]=I_alpha,
 I_alpha=4 integral_0^(pi/2) sin(3theta) cos(theta)^(1+alpha) f(tan theta) dtheta
        =4 integral_0^11 q(3-q^2) f(q)/(1+q^2)^(3+alpha/2) dq.

We show I_alpha>L_alpha, which contradicts the factor-free inequality because [h]_(y,1)<=L_alpha.

## Explicit lower bound with only scalar arithmetic

At alpha=0 the ideal odd sign profile f_ideal(q)=sign(3-q^2) for q>0 gives

 4 integral_0^(pi/2) |sin3theta| cos theta dtheta=5/2.

For example, set z=sin theta and integrate4 z|3-4z^2| from0 to1, splitting atsqrt(3)/2. Our f differs from this ideal only on[0,1/20],[3/2,2] and[10,infinity). Every loss is nonnegative. The following upper bounds are deliberately loose.

On[0,1/20], |f-f_ideal|<=1 and the kernel q|3-q^2|/(1+q^2)^3<=3q, so the loss is at most6(1/20)^2=3/200.

On[3/2,2], |f-f_ideal|<=2, q<=2, |3-q^2|<=1 and(1+q^2)^3>=(13/4)^3. Thus the kernel is at most128/2197, and the loss is at most4*2*(1/2)*(128/2197)=512/2197.

On[10,infinity), |f-f_ideal|<=1 and the kernel q(q^2-3)/(1+q^2)^3<=q^(-3), so the loss is at most4 integral_10^infinity q^(-3)dq=1/50.

Consequently

 I_0 >= 5/2-3/200-512/2197-1/50=:B_0.

For0<=q<=11, the additional factor(1+q^2)^(-alpha/2) lies in[122^(-alpha/2),1]. Since|f|<=1 and the total absolute ideal integral is5/2,

 |I_alpha-I_0| <= (5/2)(1-122^(-alpha/2)).

It follows that

 I_alpha >= B_0-(5/2)(1-122^(-1/200))=:B_alpha.

There is also a purely rational way to prove the strict comparison, independent of elementary-function software. The positive exponential series gives

 exp(5)>sum_(j=0)^7 5^j/j!>122,
 exp(5/2)>sum_(j=0)^4 (5/2)^j/j!>10.

Thus log122<5 andlog10<5/2. The elementary inequalities exp(-x)>=1-x for x>=0 and exp(x)<=1/(1-x) for0<=x<1 give

 B_alpha > B_0-1/16,
 L_alpha < 80/39.

The exact rational difference B_0-1/16-80/39 is positive. These inequalities already prove the counterexample. A separate512-bit directed scalar evaluation sharpens the separated bounds to I_alpha>2.17 andL_alpha<2.05; it uses no quadrature or profile data.

## Smooth S2 test functions

The preceding example already refutes the inequality on its printed space. It can also be approximated by smooth compactly supported parity functions vanishing near0 without increasing the seminorm bound L_alpha.

First convolve f with a smooth nonnegative even mollifier of sufficiently small support. This preserves oddness, the bounds||f||_infinity<=1 andLip(f)<=20, and gives uniform convergence to f. Keep the same x-only cutoff. The resulting angular functions give convergent strain integrals by dominated convergence, uniformly bounded by Cr^(alpha-1) in the radial integral. Their local strain therefore retains the strict gap for small enough mollifier radius.

Next multiply by a smooth even x-only cutoff chi_epsilon that is zero for|x|<=epsilon, one for|x|>=2epsilon and takes values in[0,1]. This does not increase [h]_(y,1). It makes the resulting density smooth everywhere, including x=0, and zero in a neighborhood of0. The finite x-Holder seminorm need not be uniformly bounded in this last parameter and is not on the right side of the claimed inequality. Dominated convergence again preserves the strict violation for sufficiently small epsilon. These functions have J=0, are even in x and odd in y, and are compactly supported. Their local strain is positive. No image-membership assertion beyond these functional hypotheses is used.

## Verdict scope

The omission of the angular factor changes an actual valid bound into a false one. The threshold p+alpha>1 and the corresponding boundedness conclusion of proof 25 remain valid with A_(p,alpha), or with the simpler upper bound4. The counterexample does not affect the independently proved strain constants in the weighted Hilbert spaces.
