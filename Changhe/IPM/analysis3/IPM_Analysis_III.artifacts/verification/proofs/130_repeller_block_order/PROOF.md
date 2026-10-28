# A uniformly smooth order from a strict repeller block

## Statement and actual inputs

Let V be the exact normalized case1 modal field, P=(p,0) its positive source, and W=(q,vartheta) its field in the cylinder C=R_t times S^1, with t=log r. Put A=2ell-1, D=4ell-1, Sigma=A+D, s_0=41/20 and sigma=25/4. The accepted certificates give the following properties.

1. W is C1 with two bounded weak derivatives, is bounded, respects both coordinate reflections and is tangent to the axes.
2. At the origin end, q tends uniformly to -A cos^2(theta)+D sin^2(theta), and d_theta vartheta tends uniformly to Sigma cos(2theta). The required coefficient convergence also holds in C1, with error O(exp(2t)).
3. V_1(x,0)<0 for0<x<p. On the source rectangle Q=[p_- -1/2,p_+ +1/2] times[-1/2,1/2], the symmetric part of DV is at least0.1801 times the identity. Here p belongs to the exact bracket[p_-,p_+] of proof 15.

**Theorem.** There is a reflection-invariant real C-infinity function s on C, with every derivative bounded, such that s_0<=s<=sigma, W.grad s>=0, and

 s=sigma on |cos(theta)|<=1/2 and on t>=T_inf;
 s=s_0 on |sin(theta)|<=beta_0, t<=t_c,
       and on |X-P|<=1/8 and |X+P|<=1/8,

for some beta_0>0, with t_c=log(p-1/8) and a finite T_inf. It can also be chosen so that s(t,.) converges in every angular C^j norm as t tends to minus infinity, while every positive t derivative tends uniformly to zero. The limiting order is nondecreasing on the first quadrant.

The source discs, strip and sector are fixed geometric sets in this assertion. No numerical value for beta_0, T_inf, a derivative bound or an escape minimum is asserted. This verifies the direct construction in the theory author's H2_ord.md. Proof 128 already gives a separate complete escape construction and a compatible order. Neither theorem is a high inverse estimate.

## A block whose boundary is strictly outward

Work near theta=0 and reflect at the end. Set rho=1/4 and x_c=p-rho/2. The whole physical disc |X-P|<=rho lies strictly inside Q. Choose t_1<t_c so that, for t<=t_1 and |theta|<=pi/8,

 q<0,  d_theta vartheta>=Sigma[cos(pi/4)-1/4]>0.4 Sigma.

The last inequality uses the accepted origin limit. Oddness then gives vartheta(t,theta)>=0.4 Sigma theta for theta>=0 in this region. On the compact interval[t_1,t_c], property3 gives q(t,0)<=-2q_m<0 for some q_m. Write a(t)=d_theta vartheta(t,0), and choose finite constants C_1,C_2 with

 |q(t,theta)-q(t,0)|<=C_1|theta|,
 |vartheta(t,theta)-a(t)theta|<=C_2 theta^2.

The second estimate follows from the bounded weak second derivative, using its Lipschitz first derivative representative. Zero constants cause no difficulty and impose no restriction in the corresponding upper bounds below. Put M=2(||a||_infinity+1)/q_m. Choose a nonnegative smooth psi with psi=0 on t<=t_1-1, psi'=1 on t>=t_1, and0<=psi'<=1. Set beta(t)=beta_* exp(M psi(t)). The positive beta_* can be chosen so small that, on t<=t_c,

 beta<=min(pi/8,q_m/C_1,1/(2C_2)),
 x_c beta(t_c)<=rho/4,
 p(1+2M) beta(t_c)^2<rho.

Define B_T={t<=t_c, |theta|<=beta(t)} and B_P={|X-P|<=rho}. On the upper lateral boundary of B_T the outward conormal is(-beta',1). For t<=t_1,

 W.(-beta',1)>=0.4 Sigma beta_*.

For t_1<=t<=t_c, beta'=M beta and q(t,beta)<=-q_m, so

 W.(-beta',1)>=beta[a-C_2 beta+M q_m]>=beta_*.

Since beta and beta' are uniformly bounded, dividing by sqrt(1+beta'^2) preserves a positive uniform unit-normal bound. Reflection gives the lower boundary.

The circle boundary also has a strict exit bound. Its physical unit normal is n_p=(X-P)/rho. Integrating the lower symmetric-gradient bound along the segment from P to X gives V.n_p>=0.1801 rho. If F(X)=|X-P|-rho, then its gradient in(t,theta) coordinates has length r. Therefore its cylindrical unit-normal derivative is at least0.1801 rho/(p+rho). This coordinate factor must not be omitted when quoting a numerical cylindrical bound.

The end cap of the strip lies strictly inside the disc because

 |r e^(i theta)-p|^2<=(rho/2)^2+x_c p beta(t_c)^2<rho^2

at r=x_c. To check the actual crossing, along the upper lateral curve write

 d(r)=r^2+p^2-2rp cos(beta(log r)).

On p-rho<=r<=x_c, using beta_t<=M beta and elementary sine and cosine bounds,

 d'(r)<=2(r-p)+p(1+2M)beta(t_c)^2<0.

At r=p-rho, d(r)>rho^2, while d(x_c)<rho^2. Thus there is exactly one intersection and its derivative is nonzero. The two smooth curves cross transversally. The reflected lower intersection has the same property.

For completeness, the rounding of the reentrant corners can be made by smooth defining functions. Near one intersection, let f_1 and f_2 define the strip and disc with negative sign inside, and with W.grad f_i>0. The union is locally min(f_1,f_2)<=0. Replace min by

 m_e(a,b)=[a+b-j_e(a-b)]/2,

where j_e is smooth, convex, equals |.| outside(-e,e), lies above |.|, and has derivative between-1 and1. Its gradient is a convex combination of the two original gradients. On the new zero set, both f_i are within O(e) of zero, so both directional inequalities persist. In particular the new defining gradient cannot vanish. This expands the union only in arbitrarily small neighborhoods of its corners. Outside these neighborhoods the old boundary remains exactly unchanged. Smooth local choices or a smaller supported regularization give a C-infinity boundary. Reflect the same construction at all corners.

Choose the corner neighborhoods small enough to preserve the half-radius source discs and the half-width strip, and to stay within |theta|<pi/8 and t<log(p+rho). The resulting closed block B contains B_T union B_P and its reflection at the negative source, and is contained in those angular sectors and t<=log(p+rho). Its smooth boundary has a uniform cylindrical exit bound W.n>=kappa_B>0. Uniformity follows from compactness on the finite part and the constant-width origin strip on the remaining end. It also has a uniform tubular neighborhood: the finite part is compact and smooth, and the distant end consists of straight lines.

## Backward exit time and regularity

The field is globally Lipschitz and bounded, so its flow Phi_u exists uniquely for every real u. The strict outward boundary inequality implies backward invariance of B, and no forward orbit starting outside B can enter B. For X outside B define

 tau(X)=inf{a>=0:Phi_(-a)(X) belongs to B},

with infinity if the set is empty. Then tau(Phi_u X)=tau(X)+u for u>=0, with the same convention at infinity. Every finite hitting point lies on the smooth boundary and is transversal. The implicit function theorem therefore gives a C1 hitting time on the open finite-time set, with

 W.grad tau=1, |grad tau(X)|<=exp(tau(X)||DW||_infinity)/kappa_B.

The bound follows by differentiating a unit signed-distance defining function at the hit. Also tau(X)>=dist(X,B)/||W||_infinity. For every finite c, the set{tau>c} is open: on the compact time interval[0,c] the continuous backward orbit avoids the closed set B by a positive distance.

Near the boundary, a uniform signed-distance collar has W.grad dist>=kappa_B/2. A backward orbit from sufficiently close to B reaches it in time at most2dist/kappa_B while staying in the collar. This upper bound, rather than the preceding lower bound, proves that tau tends to zero at the boundary. It is the detail needed to justify making a function of tau constant on a neighborhood of B.

Fix0<tau_1<tau_2<tau_3<tau_4. Choose a smooth nondecreasing G which is0 on a<=tau_1,1 on a>=tau_4, and whose derivative is at least kappa_1>0 whenever1/4<G(a)<3/4. Such a choice can be made with the middle transition in[tau_2,tau_3]. Define g=G(tau) outside B, g=0 on B and g=1 at infinite hitting times. Then g is C1 globally and

 0<=g<=1, W.grad g>=0,
 ||grad g||_infinity<=||G'||_infinity exp(tau_4||DW||_infinity)/kappa_B,
 W.grad g>=kappa_1 on1/4<g<3/4.

At B, g is constant on a neighborhood by the collar estimate. At infinite times it is constant on the open set{tau>tau_4}. At the two finite transition endpoints, the smooth cut G is constant to every order on one side, so the C1 pieces agree. Furthermore g=1 whenever dist(X,B)>=tau_4||W||_infinity.

## Fixed-scale smoothing preserves the required sign

Convolve on the flat cylinder with a compactly supported smooth reflection-invariant probability mollifier of radius e. Put g_e=g*rho_e and L=||grad g||_infinity. Every derivative of g_e is bounded. If eL<1/24 and1/3<=g_e(X)<=2/3, then every Y in the convolution ball obeys

 |g(Y)-g_e(X)|<=2eL<1/12,

so1/4<g(Y)<3/4. Consequently

 W(X).grad g_e(X)
 =int[W(Y).grad g(Y)+(W(X)-W(Y)).grad g(Y)]rho_e(X-Y)dY
 >=kappa_1-e||DW||_infinity L>0

for e sufficiently small. Take a smooth nondecreasing F equal to0 below1/3 and1 above2/3, and put s=s_0+(sigma-s_0)F(g_e). The derivative of F vanishes everywhere the preceding strict inequality is unavailable. Therefore W.grad s>=0 everywhere.

Choose tau_4 and then e so that tau_4||W||_infinity+e<pi/24. Then s=sigma at distance at least this quantity from B. The prescribed vertical sector has angular distance at least pi/3-pi/8=5pi/24 from B. The far region t>=log(p+rho)+pi/24 has enough distance as well. Thus T_inf=log(p+rho)+pi/24 is a possible qualitative cutoff.

Make e smaller than the positive distances of the half-radius source discs and of a strip |theta|<=beta_*/2, t<=t_c, from the complement of B. These distances are positive uniformly: far to the left beta is constant; the remaining part is compact, and the cap is inside the source disc. The lower bound e<beta_*/2 by itself is not a complete distance estimate on a steeply sloping strip, so this uniform-distance choice is used instead. The physical half-radius disc has cylinder distance at least rho/[2(p+rho)] from its outer circle, and B contains that circle's interior. Finally choose beta_0>0 so that arcsin(beta_0)<beta_*/2. This proves all stated exact low-order sets.

## The origin limit of the constructed order

The limiting order also exists, although the main block argument does not require it. Translate t by a sequence tending to minus infinity. On any bounded translated t strip, the block B is exactly the fixed angular strip |theta|<=beta_* and its reflection. The translated fields tend in C1 on compact sets to W_0=(q_0,vartheta_0), uniformly in theta. On every bounded time interval their flows and first spatial derivatives converge by the integral flow equation and Gronwall's inequality. The common strict transversality bound persists at the two fixed boundary lines. On finite hitting-time ranges, the implicit formula then makes the translated hitting times converge uniformly to those of W_0. The limit is independent of t. Since G is already constant for times outside[tau_1,tau_4], these facts and the openness of{tau>tau_4} give uniform convergence of the translated g to a continuous function g_-(theta). A compactness argument covers the angular circle; at transition endpoints use the continuity and constant extension of G.

Fixed-scale convolution now gives convergence of every derivative of g_e by differentiating its smooth kernel, using only this uniform convergence on enlarged compact strips. The limiting function depends only on theta. Composing with F proves the asserted convergence of s and the vanishing of its positive t derivatives. Passing to the limit in W.grad s>=0 yields vartheta_0 d_theta s_->=0. Since vartheta_0>0 on(0,pi/2), s_- is nondecreasing there. The endpoint constant neighborhoods survive the same fixed-scale construction.

## Verdict and limitations

The exit inequality, transversal union, hitting-time construction and mollification in H2_ord are valid with the explicit coordinate, collar, rounding and interior-distance details above. The order has the uniform specifications needed for the accepted H1 and H2 theorems. The finite-frequency angular normal theorem of proof 129 can use its limiting order. No uniform normal inverse, propagation estimate, H3 estimate, low injectivity or nonlinear solution is inferred.
