# Result331: a quadratic step bound for the auxiliary vertical inverse

Written 2026-10-22T08:58:44.871296+00:00 before numerical tests. This is a conditional analytic result for an auxiliary inverse. It does not imply a full-plane IPM existence or nonexistence endpoint.

## Exact hypotheses and notation

Let 0<p<1, 0<epsilon0<1, and let g be C4 on R2, even in x and odd in y. Put F=g_x and H=g_xx. Suppose |g_xxxx(x,s)|<=M(1+sqrt(x2+s2))^(p-4) for a finite M. Assume explicitly that for every compact interval I of x values, integral_0^infinity sup_(u in I)(|F(u,s)|+|H(u,s)|)ds is finite. This domination permits differentiation of integral F with respect to x. The C4 hypothesis is sufficient, not claimed sharp. These last conditions hold for the saved finite representation below; they are explicit hypotheses for a general g.

For0<epsilon<=epsilon0 set h=epsilon(1+sqrt(x2+s2)) and

D_epsilon F(x,s)=[F(x+h,s)-F(x-h,s)]/(2h),
D_0 F=H.

The same central h is used in the two shifted arguments. For y>=0 let

V1=-integral_y^infinity F(x,s)ds,
V2_epsilon=integral_0^y s D_epsilon F(x,s)ds+y integral_y^infinity D_epsilon F(x,s)ds.

Extend V1 evenly and V2 oddly in y. Set K=M/[6(1-epsilon0)^(4-p)]. Then all perturbed tails converge and the following bounds hold for every real x,y:

|D_epsilon F(x,s)-H(x,s)|<=K epsilon2(1+sqrt(x2+s2))^(p-2),

|V2_epsilon(x,y)-V2_0(x,y)|<=K epsilon2 [(1+|y|)^p-1]/[p(1-p)],

|div V_epsilon(x,y)|<=K epsilon2 (1+|y|)^(p-1)/(1-p).

The displayed first derivatives exist under these hypotheses. At y=0, V2 is differentiable in y with derivative integral_0^infinity D_epsilon F(x,s)ds, and the divergence formula holds there as well. No higher smoothness of the perturbed evaluator at the origin is asserted. At x=0 the central vertical strain satisfies

|cH_epsilon-cH_0|<=K epsilon2/(1-p),
cH_epsilon=lim_(y->0) V2_epsilon(0,y)/y.

At each fixed point x and y>=0, the leading coefficient is

lim_(epsilon->0+) [V2_epsilon-V2_0]/epsilon2
= (1/6) integral_0^infinity min(s,y)(1+sqrt(x2+s2))2 g_xxxx(x,s)ds.

The analogous leading coefficient of cH is the same integral at x=0 with min(s,y) replaced by1. These are exact analytic statements with M unspecified; they are not numerical error enclosures for a computed state.

## Complete proof

For a C3 function F of its first argument, the fundamental theorem of calculus gives D_epsilon F as the average of H on [x-h,x+h]. Applying the theorem twice to H, cancelling its odd linear term, and interchanging integrals over finite intervals yields the Peano-kernel identity

D_epsilon F-H(x,s)
= (h2/4) integral_(-1)^1 (1-|t|)2 g_xxxx(x+t h,s)dt.

One can verify the coefficient by integrating the kernel: integral_(-1)^1(1-|t|)2dt=2/3, giving h2/6 for constant g_xxxx. Every integral in this step is over a compact interval with a continuous integrand, so the interchange is justified.

Write r=sqrt(x2+s2) and r_t=sqrt((x+t h)2+s2). The triangle inequality gives 1+r_t>=1+r-|t|h>=(1-epsilon)(1+r)>=(1-epsilon0)(1+r). Because p-4<0,

|g_xxxx(x+t h,s)|<=M(1-epsilon0)^(p-4)(1+r)^(p-4).

Insert this in the kernel identity and use h2=epsilon2(1+r)2. This proves the first bound without a small-r exception. Since r>=s>=0 and p-2<0, its right side is at most K epsilon2(1+s)^(p-2), an integrable function of s. The assumed convergence for H therefore gives convergence for D_epsilon F.

Subtract the two V2 definitions to get

V2_epsilon-V2_0=integral_0^infinity min(s,y)[D_epsilon F-H]ds.

The majorant is integrable because y is fixed and p<1. Its elementary integral is

I(y)=integral_0^infinity min(s,y)(1+s)^(p-2)ds
=[(1+y)^p-1]/[p(1-p)].

For example I(0)=0 and I'(y)=integral_y^infinity(1+s)^(p-2)ds=(1+y)^(p-1)/(1-p), which proves the formula by integration. This establishes the second bound. The divergence equals integral_y^infinity(D_epsilon F-H)ds: differentiation of V1 in x gives -integral H; differentiation of V2 in y cancels the two endpoint terms and leaves integral D_epsilon F. Only a y derivative of V2 is taken, so no x derivative of h is needed. The same majorant proves the divergence bound.

Continuity and domination yield cH_epsilon=integral_0^infinity D_epsilon F(0,s)ds. Applying the first bound and integrating (1+s)^(p-2) gives the strain estimate. Parity gives the claims for negative y. At y=0 the one-sided expression for the y derivative of V2 agrees from both sides; the x derivative of V1 remains the canonical derivative already assumed.

For fixed x,s, continuity of g_xxxx and the kernel identity give (D_epsilon F-H)/epsilon2 tending to (1+r)2 g_xxxx/6. The uniform majorant just proved is integrable against min(s,y), or against1 at x=0. Dominated convergence gives both leading-coefficient formulas. This is a pointwise-in-(x,y) limit; no uniform relative error for a normalized residual is asserted. Such a denominator can be small or zero.

## Application to the saved finite family and its limits

For the saved state, r=L sqrt(sigma)/(2w)^P, sigma=(1+t)/2, w=(1-t)/2, P>1, p=1-1/P, and g=y w B(t,theta), where B=sum_(k=0)^(M_modes-1) sigma^k P_k(t) cos(2k theta), each P_k a finite polynomial in t. In the saved local basis, P_k is a finite Chebyshev polynomial in the affine argument (2t-1-t_k)/(1-t_k), with fixed t_k<1. It is consequently a polynomial in t, not a polynomial in r with odd powers. This is the exact representation in independent_code/scalar_mp_hydrostatic_density.py and the own Cartesian evaluator. The map is a global bijection because d(log r)/dt=1/(4sigma)+P/(2w)>0, with endpoint limits0 and infinity. Near0, sigma is analytic in r2 by the implicit function theorem; sigma^k cos(2k theta) is a smooth polynomial angular factor times a smooth radial function. Thus g is smooth on each compact set.

Squaring gives r2=L2 sigma/(2w)^(2P). At infinity w is comparable to r^(-1/P). The exact identity (r*d/dr)w=-2w(1-w)/[w+2P(1-w)] expresses this derivative as w times a function analytic near w=0. If (r*d/dr)^j w=w A_j(w) with A_j analytic, the next derivative is w A_1(w)[A_j(w)+w A_j_prime(w)], again of that form. Induction proves all iterated scaled radial derivatives are O(w). The finite radial-angular factors and all their required derivatives are bounded. Repeated Cartesian differentiation, each costing a factor r^(-1), gives |D^j g|=O(r^(p-j)) for each fixed finite j, in particular j=4. Compact smoothness then supplies a finite global M of the required kind. These facts also give H=O(r^(p-2)). Since g is even in x, F(0,s)=0 and F(x,s)=integral_0^x H(u,s)du, so F=O_I(s^(p-2)) on compact x intervals. F and H have the locally uniform integrable tails required above.

This proves applicability to each individual finite representation, without an explicit M or a constant uniform in resolution. The primary admissible IPM class assumes a first-derivative growth bound only; it does not supply this weighted fourth-derivative bound. Therefore the lemma must not be extended to that whole class or to a limit of trial states without additional estimates.

## Gaussian cross-check

For g=y exp(-x2-y2), the exact strain is cH_epsilon=-2 integral_0^infinity s exp(-s2) exp(-epsilon2(1+s)2)ds. Hence

cH_epsilon=-1+(2+sqrt(pi))epsilon2+E_epsilon,
-(9+5sqrt(pi))epsilon4/2 <= E_epsilon <=0.

Indeed0<=exp(-z)-1+z<=z2/2 for z>=0, by two integrations of0<=exp(-z)<=1. Apply this with z=epsilon2(1+s)2 and integrate. The coefficients follow from integral_0^infinity s^n exp(-s2)ds: integration by parts yields I_n=(n-1)I_(n-2)/2, with I_1=1/2 and I_0=sqrt(pi)/2. Expansion of (1+s)2 gives2+sqrt(pi), and expansion of (1+s)4 gives(9+5sqrt(pi))/2. This is an analytic bound, not an inference from sampled ratios.

## Dependencies and evidence

The auxiliary inverse and parity conventions are derived here and in result327 PROOF.md. The saved representation and Cartesian smoothness are derived in the independent_hydrostatic_evaluator proof and the Cartesian evaluator. Verification consists of exact polynomial kernel identities, an independent integral evaluation of the primitive, the Gaussian closed formula at increased precision, and actual Claude Opus5.5 review followed by independent resolution. No Lean build is permitted in this run. Until these checks finish the new result remains OPEN.

## An explicit Gaussian constant

Added 2026-10-22T09:00:16.637499+00:00, before tests. For the Gaussian, g_xxxx=(16x4-48x2+12)y exp(-r2). For0<p<1 its weighted magnitude is at most(16r5+48r3+12r)(1+r)4 exp(-r2). When r<=1 this is at most1216. When r>=1 it is at most1216 r9 exp(-r2). Differentiation gives sup_(r>=0) r9 exp(-r2)=(9/(2e))^(9/2)<(9/4)^5, since e>2 and9/4>1. Therefore M=1216(9/4)^5=1121931/16 is sufficient simultaneously for all0<p<1. This coarse exact analytic bound is not estimated from a numerical grid.

Revision 2026-10-22T09:10:15.125700+00:00: the tail domination and finite polynomial form were made explicit after actual review3b54143a. The original proof and218-check output are preserved. The review accidentally wrote exponent P after squaring the map; the correct exponent is2P, used in this proof and the implementation. Its statement that the monomial check differentiates g four times also changes variable roles: the checked monomial is F=g_x and its third derivative is used. These two review transcription errors do not alter the checked theorem. No constant uniform in resolution is established.
