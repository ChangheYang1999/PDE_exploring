# Frozen source inversion, the pointwise row, and origin matching

Topic61. The results below are exact conditional theorems about explicitly defined operators. They verify the requested V17(a,d) claims and the necessary matching qualifications. They are not a global inverse theorem for the modal trial.

## 1. Frozen operator and precise domain

Use the unitary Fourier transform in two dimensions with prefactor (2pi)^-1. Write zeta=(xi,eta), r=|zeta|, and define

    ||h||_(H^sigma)^2 = integral (1+r²)^sigma |hhat(zeta)|² dzeta.

M is the bounded multiplier m=xi²/r², with an arbitrary value at the single point r=0. Suppose

    10<=A<=51/5, 99/100<=mu<=101/100, 29<=g<=30,
    3<sigma<2373/680.                                         (1)

The variables (s,y) are coordinates centered at a source, s=x-L. Set

    L_P h=A s h_s+mu y h_y-h-gMh,
    D_max={h in H^sigma: L_P h in H^sigma as a distribution}.

Let

    kappa_y=6-(sigma-1/2)101/100,
    kappa_x=30+99/200-(sigma-1/2)51/5,
    kappa=min(kappa_y,kappa_x)>0.                             (2)

Then L_P is bijective D_max -> H^sigma and

    ||L_P^-1 f||_(H^sigma)<=kappa^-1 ||f||_(H^sigma).          (3)

The output norm here is H^sigma, not the graph norm. With the sum graph norm the bound is 1+kappa^-1. The result also holds on any invariant real coordinate-reflection parity subspace, including functions even in s and odd in y. This local reflection in s is not the original global reflection x->-x around the origin.

At sigma=31/10 the margins are (kappa_y,kappa_x)=(1687/500,159/40), giving inverse bound500/1687. At sigma=13/4 they are (1289/400,489/200), giving inverse bound200/489. All numbers here are exact rationals.

### Fourier conjugation and the parameter window

Put B=diag(A,mu), b0=1+(A+mu)/2, W=(1+r²)^(sigma/2), and F=W hhat. Integration by parts, initially on Fourier functions smooth and compactly supported away from the coordinate axes, gives

    W (L_P h)^hat = D0 F+C F,
    D0=-A xi partial_xi-mu eta partial_eta-(A+mu)/2,
    C=sigma(A xi²+mu eta²)/(1+r²)-b0-gm.                      (4)

D0 is skew symmetric in L2. Positivity of A,mu,sigma gives

    C <= -(b0-sigma mu)(1-m)-(b0+g-sigma A)m.

Since sigma>1/2, minimization over the rational parameter box gives exactly (2): the y margin is minimized at A=10,mu=101/100, and the x margin at g=29,mu=99/100,A=51/5. Thus C<=-kappa. The x margin vanishes at sigma=2373/680; the y margin vanishes later at sigma=1301/202. This proves the stated window. The inverse proof also applies when1/2<sigma<2373/680; positivity of kappa remains required. The lower bound sigma>3 in(1) is imposed for the intended C2,alpha regularity. The upper bound in (4) is the homogeneous high-frequency rate, not an equality at low frequencies. At fixed parameters, sup C equals minus the smaller of those two fixed-parameter margins, approached along the corresponding direction as r tends to infinity. The kappa in(2) then takes the minimum over the entire parameter box. No low-frequency exclusion is needed.

The IPM coupling sign is also fixed directly: -Delta psi=partial_s h gives psihat=i xi hhat/r², hence Uhat=(xi eta,-xi²)hhat/r². With the background gradient (0,g), U[h].grad rho=-gMh. There is no extra factor1/2. The normalization functional and variable coefficients are absent from L_P.

### Maximal domain, including the Fourier axes

The unitary dilation group on L2 is

    G(t)F(zeta)=exp(-(A+mu)t/2) F(exp(-Bt)zeta).

For completeness, its generator has exactly the maximal distributional domain of D0. On each Fourier quadrant put xi=epsilon1 exp(q1), eta=epsilon2 exp(q2). The unitary coordinate map

    F -> exp((q1+q2)/2)F(epsilon1 exp(q1),epsilon2 exp(q2))

turns D0 into the constant derivative -A partial_q1-mu partial_q2. Fourier transformation in q identifies its maximal domain with those L2 functions whose Fourier transform multiplied by A omega1+mu omega2 lies in L2. This is closed. Multiplication by expanding smooth cutoffs in q and then convolution with a smooth approximate identity approximates every vector in the graph norm: cutoff derivative errors are bounded by C(A+mu)/R times the L2 norm, and convolution commutes with the constant derivative. Thus compact smooth functions are a core in each quadrant.

There is no extra distribution supported on a Fourier axis. Let chi_R(q1,q2) equal1 on[-R,R]², vanish outside[-2R,2R]², and have first derivatives bounded by C/R. The corresponding function of zeta, extended by zero near the axes, is smooth there and has |(A xi partial_xi+mu eta partial_eta)chi_R|<=C(A+mu)/R. Test the quadrant derivative identity against chi_R times an arbitrary compact smooth global test function. Dominated convergence handles the principal terms. Cauchy-Schwarz bounds the cutoff error by C(A+mu)/R times the L2 norms of F and the test function. Sending R to infinity yields the global distributional identity. Conversely a global maximal-domain vector restricts to each quadrant maximal domain. This proves the domain identification and the core statement on the whole plane.

C in (4) is bounded and real. Consequently D0+C is closed on the same domain, and the same core works, since multiplication by C is bounded. Conjugation by W and the Fourier transform identifies this domain with D_max.

### Evolution and two-sided inverse

Define for t>=0

    S(t)F(zeta)=exp(-(A+mu)t/2)
       exp(integral_0^t C(exp(-Bu)zeta)du)F(exp(-Bt)zeta).    (5)

Splitting the integral proves the cocycle and semigroup identity. The exponential is bounded by exp(-kappa t). The dilation is unitary, so ||S(t)||<=exp(-kappa t). Dominated convergence first for compact smooth functions and then density proves strong continuity. Differentiation on the above core yields D0+C.

Here is the domain justification for that differentiation. The explicit S(t) derivative tested against compact smooth functions on a quadrant shows that its generator is contained in the maximal distributional realization of D0+C. The cutoff argument above extends the identity across the axes. Conversely the generator is closed and contains the core, so it contains the graph closure D0+C. Hence these domains and operators agree, not merely their action on test functions.

For F in L2 the Bochner integral H=-integral_0^infinity S(t)F dt converges and has norm at most||F||/kappa. Moreover

    S(a)H-H=integral_0^a S(t)F dt.

Division by a and strong continuity show that H belongs to the generator domain and (D0+C)H=F. If H is in that domain and (D0+C)H=0, differentiating S(t)H gives0, so S(t)H=H. Exponential decay forces H=0. Surjectivity, injectivity and (3) follow. Reflection and complex conjugation commute with the dilation and real even multiplier, proving the parity assertion.

### A derivative-evaluation corollary and its arithmetic

For sigma>2, Fourier Cauchy-Schwarz and polar integration give

    |h_y(0)| <= [8pi(sigma-1)(sigma-2)]^-1/2 ||h||_(H^sigma).

Indeed integral eta²(1+r²)^(-sigma) dzeta equals pi/[2(sigma-1)(sigma-2)], since the angular integral is pi and substitution u=r² gives one half integral_0^infinity u(1+u)^(-sigma)du. The latter integral is1/[(sigma-1)(sigma-2)], by one integration by parts. Combining with(3) gives this evaluation constant times kappa^-1 as an upper bound for |partial_y L_P^-1 f(0)|/||f||. It is not asserted to be the exact norm of that composition.

For independent numerical evaluation of pi, the computation may use pi=16 arctan(1/5)-4 arctan(1/239). Here is a direct verification. If a=arctan(1/5), then tan(2a)=5/12 and tan(4a)=120/119. The tangent subtraction formula gives tan(4a-arctan(1/239))=1. The difference lies in(0,pi/2), using arctan t<t and arctan t>=t-t³/3 for0<t<1, so it equals pi/4. The alternating series for arctan q has error between0 and the first omitted term, with its sign. Exact rational partial sums thus enclose pi without relying on a floating pi constant. The two constant computations use this enclosure and the Arb pi ball separately.

## 2. The P-row of the full equation

This part concerns a full variable-coefficient equation, not L_P. Let P=(L,0). Suppose V is C1 and rho is C2 nearP, V(P)=0, rho is even in x and odd in y, V1 is even in y, V2 is odd in y, and

    partial_y V2(P)=mu_P, G1(x)=partial_y rho(x,0),
    g=G1(L), gprime=G1'(L).

For perturbations and forcing assume h,f are locally H^sigma nearP with sigma>2, h odd in y, and that the chosen global domain makes U[h] C1 nearP and makes S[h]=psi[h]_xy(0) a defined scalar. These nonlocal hypotheses do not follow from a disc norm. Use the normalization c_l[h]=S[h]/3. Define

    L h=V.grad h-h+U[h].grad rho+(S[h]/3)X.grad rho.

Assume Lh=f distributionally nearP. Then

    (mu_P-1)h_y(P)+g U2[h]_y(P)+gprime U1[h](P)
          +(S[h]/3)(g+L gprime)=f_y(P).                     (6)

This is an implied row, not an additional boundary condition.

To check the regularity, a local cutoff and Fourier Cauchy-Schwarz give continuous first derivatives from H^sigma for sigma>2: integral r²(1+r²)^(-sigma) d zeta is finite. Thus h,f are C1. No pointwise second derivative of h is needed. For Z->0,

    V(P+Z).grad h(P+Z)=DV(P)Z.grad h(P)+o(|Z|).

The product is differentiable atP, and its y derivative is mu_P h_y(P), because V1_y(P)=0. The derivative of U[h].grad rho contributes g U2_y+gprime U1. Here h_x(P)=0, rho_x(P)=0 and U2[h](P)=0 by parity. The canonical full-plane operator preserves the required velocity parity. Terms involving rho_x(P) or U2(P) therefore vanish. Finally partial_y(X.grad rho)(P)=g+L gprime. All terms in Lh have continuous representatives nearP, so the distributional equality is pointwise; those representatives are differentiable atP. Differentiating there proves (6).

At an exact profile with positive g and the source identities mu_P=1, (6) reduces to the nonlocal row without h_y(P). At a trial it retains the term(mu_P-1)h_y(P). Division by this small coefficient while treating the coupling as prescribed forcing is not justified for the coupled operator. The uniformly bounded frozen inverse in section1, which includes mu=1, is a concrete counterexample to a necessary pole inferred by such division. Neither (6) nor that frozen counterexample proves global surjectivity, or an upper bound for the variable-coefficient inverse.

For sigma>3 the same Fourier argument yields local C2,alpha for every0<alpha<min(1,sigma-3), by using |exp(i zeta.Z)-1|<=2|zeta.Z|^alpha. Thus the frozen window is compatible with that particular local regularity requirement.

## 3. Incoming trace and the origin matching equation

Suppose, on 0<x<=x1<L,

    w(x)<0, mu(x)=2c_l-w'(x), A=2c_l-1>0,
    w=-Ax+O(x³), w'=-A+O(x²).

Assume w is C1 and has no zero there. Let D=4c_l-1=2A+1. Then mu=D+O(x²). For a solution h with the needed differentiable traces along the open axis, put b(x)=h_y(x,0), and let R(x)=f_y(x,0)-Jh(x), where

    Jh=G1' U1[h](x,0)+G1 U2[h]_y(x,0)
           +(S[h]/3)(xG1'+G1).

Assume explicitly that b is locally absolutely continuous and R is locally integrable on(0,x1]. Differentiating the equation along that open axis requires the corresponding trace regularity, assumed here. It gives

    w b'+(mu-1)b=R.                                         (7)

This is a representation for an already coupled solution; R depends on h. Define

    a0=(mu-1)/w,
    Phi(x)=x² exp(-integral_0^x(a0(t)+2/t)dt).

The integrand is O(t), so Phi>0, Phi/x²=1+O(x²), and Phi'/Phi=-a0. Given b(x1)=b1, integration of (b/Phi)'=R/(wPhi) gives

    b(x)=Phi(x)[b1/Phi(x1)+integral_x1^x R(t)/(w(t)Phi(t))dt]. (8)

This is unique on each compact subinterval by the elementary first-order identity. If

    integral_0^x1 |R/(wPhi)|dt < infinity,                   (9)

then

    beta=b1/Phi(x1)-integral_0^x1 R/(wPhi),
    b(x)=beta Phi(x)+Phi(x)integral_0^x R/(wPhi),
    b(x)/x² -> beta.                                        (10)

A sufficient condition is R=O(x^(2+nu)),nu>0. In that case b=beta x²+O(x^(2+min(nu,2))). A Dini bound |R|<=x² omega(x), integral_0^x1 omega(t)dt/t<infinity, also suffices. These conditions are additional target-space requirements.

For the exactly linear local model w=-Ax,mu=D, the forcing R=r2 x² gives b/x²=constant-(r2/A)log x. Even R/x²->0 does not suffice: on0<x<=1, R=x²/log(e/x) has solution

    b=x²[b1+(1/A)log log(e/x)],

whose b/x² diverges. Both examples follow by direct differentiation and require no claim about a PDE profile.

If h=x²y a_h near0 with a_h continuous and h_y defined on the axis, then b(x)=x²a_h(x,0). Hence beta=gamma h:=a_h(0), under (9). The normalized condition gamma h=0 is exactly the matching equation

    b1/Phi(x1)=integral_0^x1 [f_y(t,0)-Jh(t)]/[w(t)Phi(t)]dt. (11)

It cannot be discarded when b1 and the forcing are prescribed independently. At an exact profile, TG1=0 and G1/x²->1 imply Phi=G1. At a trial, G1 need not solve that equation and Phi must be used instead. On the interval ending at fixed x1<L, no expression divides by mu_P-1. The resulting norm constants may still depend on the interval, w, the coupling and matching maps. No bound for those constants is asserted here.

## 4. Scaling and what normalization does prove

Let the canonical profile scaling be rho_lambda(X)=lambda^-1 rho(lambda X), lambda>0. Direct differentiation of the Poisson equation and the canonical sublinear condition gives

    U[rho_lambda](X)=lambda^-1 U[rho](lambda X),
    psi[rho_lambda](X)=lambda^-2 psi[rho](lambda X)

up to an irrelevant additive stream constant. The central strain and c_l do not change. Therefore

    F(rho_lambda)(X)=lambda^-1 F(rho)(lambda X).

Assume that this curve is differentiable in the chosen operator domain, that F is differentiable there with derivative L, and that its tangent K=X.grad rho-rho belongs to that domain. Differentiating atlambda1 proves

    LK=(X.grad-1)F(rho), gamma K=2.                          (12)

The coefficient identity follows also from the scaling of x²y, which is multiplied bylambda². Moreover K_y(x,0)=xG1'(x).

At an exact solution, if the linear domain is closed under adding K and gamma is a continuous functional, any already existing solution Lh=f has a normalized representative

    h_normalized=h-(gamma h/2)K.                            (13)

This removes the scaling direction and preserves Lh=f. Its incoming trace and coupling change together, so (11) remains valid. It does not prove that the kernel consists only of scaling, that the operator is onto, or that a prescribed far-field amplitude permits K. At a trial, (12) is generally nonzero, so (13) changes the forcing. An inverse on the normalized space then requires a quantitative full-operator argument.

## 5. Verification and scope

All analytic claims are derived above. The earlier source_pole result supplies a cross-check of the sigma31/10 specialization, not a substitute for the maximal-domain proof. axis_jets and scaling_index supply separate cross-checks of signs and normalization. No numerical residual, tail estimate or candidate-specific inverse is used in (1)-(3).

The executable checks are to verify exact parameter-box extrema at both sigma values and the window endpoints, symbolic Fourier conjugation and evolution cocycle identities, symbolic point-row and matching/scaling identities, and two independent interval routes for illustrative frozen inverse constants. They must not label an illustration a profile enclosure. The fixed transverse extension multipliers and the transition collar are separate questions, not conclusions of this note.

OPEN: variable-coefficient disc estimates, bounded nonlocal tail maps for the chosen global domain, all coupled matching and global onto estimates, the normalization at a trial, and every decisive PDE endpoint.
