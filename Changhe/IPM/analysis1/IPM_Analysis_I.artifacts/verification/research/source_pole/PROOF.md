# Coupled source inversion without a resonance pole

Date:2026-10-20. Status: CONFIRMED as a conditional frozen-model theorem, after actual Claude Opus 5.5 review and follow-up. This is an exact frozen-operator counterexample to an inference from the small transport coefficient mu-1. It is not an inverse theorem for the full variable-coefficient IPM linearization.

## Statement

Use the unitary Fourier transform in two dimensions with prefactor (2pi)^(-1), and define ||h||_(H^s)^2=integral (1+|zeta|^2)^s |hat h(zeta)|^2 dzeta. Let M be the bounded multiplier with symbol m(xi,eta)=xi^2/(xi^2+eta^2), with any value at zero. Set s=31/10 and

10 <= A <= 51/5,  99/100 <= mu <= 101/100,  29 <= g <= 30.

On the maximal distributional graph domain D_(A,mu)={h in H^s: L_(A,mu,g) h in H^s}, define

L_(A,mu,g) h = A x h_x + mu y h_y - h - g M h.

This operator is bijective D_(A,mu) -> H^s and satisfies, uniformly on the displayed closed parameter box,

||L_(A,mu,g)^(-1) f||_(H^s) <= (500/1687)||f||_(H^s).

The same statement holds on the real subspace of functions even in x and odd in y. The inverse also has a uniformly bounded source derivative, namely

|partial_y L^(-1) f(0)| <= (500/1687) [8pi(s-1)(s-2)]^(-1/2) ||f||_(H^s).

In particular, there is no necessary factor 1/|mu-1| in either bound. The parameter box contains the independently enclosed A, mu and g of the normalized modal trial, but the theorem concerns the frozen operator only.

## Fourier energy and an exact uniform margin

Write B=diag(A,mu), r=|zeta|, w=(1+r^2)^(s/2), and F=w hat h. Integration by parts in the Fourier transform gives

w Fourier(L h) = D_0 F + C F,

D_0=-A xi partial_xi-mu eta partial_eta-(A+mu)/2,
C=s(A xi^2+mu eta^2)/(1+r^2)-b-gm,
b=1+(A+mu)/2.

The term D_0 is the generator of the unitary dilation group G(t)F(zeta)=exp(-(A+mu)t/2)F(exp(-Bt)zeta). Since A>mu>0 and r^2/(1+r^2)<=1,

C <= s mu-b+[s(A-mu)-g]m
   = -(b-s mu)(1-m)-(b+g-s A)m.

Both endpoint margins are positive. On the whole parameter box,

b-s mu=1+A/2-(13/5)mu >= 1687/500,
b+g-s A=1+g+mu/2-(13/5)A >= 159/40 > 1687/500.

Consequently C<=-delta for delta=1687/500. This is an ordinary H^s estimate, including low frequencies; no homogeneous norm or missing zero-frequency condition is being used.

## Domain and inversion

We identify the maximal graph domain rather than assuming a realization. On each open Fourier quadrant put xi=sign(xi) exp(q_1), eta=sign(eta) exp(q_2). The unitary coordinate map F -> exp((q_1+q_2)/2)F(sign(xi)exp(q_1),sign(eta)exp(q_2)) turns D_0 into the constant directional derivative -A partial_(q_1)-mu partial_(q_2). The coordinate axes have measure zero and the flow preserves each quadrant. Fourier transformation in q identifies the maximal domain of this derivative with those L^2 functions whose product by A omega_1+mu omega_2 lies in L^2. It is closed. Smooth compactly supported functions are a core: first multiply by expanding smooth cutoffs, whose directional derivatives are O(1/R), then convolve with a smooth approximate identity. Both operations converge in the derivative graph norm. Thus D_0 is exactly the maximal distributional generator of the unitary group above. There is no hidden distribution supported on the Fourier axes in this identification. To see this, take a smooth cutoff chi_R(q_1,q_2) that equals1 on [-R,R]^2, vanishes outside [-2R,2R]^2 and has each first derivative bounded by C/R. Viewed on the open quadrants and extended by zero near the axes, it is a smooth Fourier-space cutoff. Its directional derivative (A xi partial_xi+mu eta partial_eta)chi_R is bounded by C(A+mu)/R. For an L^2 function whose quadrant directional derivatives are in L^2, test the derivative identity against chi_R times a compact smooth global test function. The cutoff error tends to zero by Cauchy-Schwarz, and the other terms converge by dominated convergence. The resulting identity holds on the full plane. Thus the quadrant maximal domain is the global distributional domain. Adding the bounded real multiplication C preserves this domain. Multiplication by w and its inverse then identifies it with the stated maximal domain of L.

An explicit semigroup for D_0+C is

S(t)F(zeta)=exp(-(A+mu)t/2)
 exp(integral_0^t C(exp(-Bu)zeta)du) F(exp(-Bt)zeta),  t>=0.

The cocycle identity verifies S(t+u)=S(t)S(u). The formula gives strong continuity first on compactly supported smooth functions, then on L^2 by density and the uniform norm bound. Differentiation on the core gives generator D_0+C, whose closed maximal realization was just identified. Changing variables zeta -> exp(-Bt)zeta and using C<=-delta proves ||S(t)||<=exp(-delta t).

For any F in L^2, the Bochner integral H=-integral_0^infty S(t)F dt therefore converges with ||H||_2<=delta^(-1)||F||_2. The identity

S(a)H-H=integral_0^a S(t)F dt

shows that H lies in the generator domain and (D_0+C)H=F. If (D_0+C)H=0, then S(t)H=H for every t, and the exponential norm decay forces H=0. This proves surjectivity, injectivity and the inverse bound on the exact graph domain.

The multiplier, dilation field, Fourier weight and semigroup commute with both coordinate reflections and preserve real-valued physical functions. Projection to the real even-x odd-y subspace therefore preserves the inverse and the bound.

## The source jet does not isolate transport

The Fourier Cauchy-Schwarz inequality gives

|h_y(0)| <= (2pi)^(-1) [integral eta^2(1+r^2)^(-s) dzeta]^(1/2) ||h||_(H^s)
         = [8pi(s-1)(s-2)]^(-1/2)||h||_(H^s).

For the integral, the angular integral of sin^2(theta) is pi, and the radial integral is integral_0^infty r^3(1+r^2)^(-s)dr=1/[2(s-1)(s-2)]. The same Cauchy-Schwarz argument for derivatives up to order2, with the increment bound |exp(i zeta dot X)-exp(i zeta dot Y)|<=2|zeta|^alpha |X-Y|^alpha, yields H^(31/10) contained in C^(2,alpha) for every 0<alpha<1/10. Thus h and M h have pointwise first derivatives and sufficient regularity to differentiate L h at the source.

Take f(x,y)=y exp(-x^2-y^2), which belongs to H^s and has f_y(0)=1. Its solution h=L^(-1)f is real, even in x, odd in y, and satisfies

1=(mu-1)h_y(0)-g(Mh)_y(0).

At mu=1, (Mh)_y(0)=-1/g. The coupled equation is solvable for this forcing, and the solution has the uniform norm and derivative bounds above. The transport resonance is absorbed by the nonlocal term. Dividing this identity by mu-1 while treating the coupled term as independent forcing cannot establish a lower bound for the inverse of L.

## IPM sign and normalization

For the canonical Poisson equation -Delta psi=partial_x h, Fourier transformation gives hat psi=i xi hat h/r^2 away from zero. Therefore U_2[h]=partial_x psi has multiplier -xi^2/r^2=-m, while U_1[h]=-partial_y psi has multiplier xi eta/r^2. At an axis point P with density gradient (0,g), the frozen nonlocal term is U[h] dot grad rho(P)=-g M h. There is no additional factor1/2: the local -h e_2/2 and the principal-value kernel together yield this full multiplier. The scalar normalization term is a separate finite-rank expression and is expressly absent from the present frozen model.

## Application and limits of the objection

SPEC v3 section3.5 states that any inverse solving for h_y(P) costs at least 1/|mu-1| and attributes this to the source identity. The statement is valid for the isolated jet equation of pure transport when the other terms are prescribed independently. The displayed fully coupled frozen family is a counterexample to the asserted implication for a coupled inverse. A full IPM inverse could still be large for other reasons; this theorem neither proves nor disproves that. The moving source, normalization functional, saddle, far field and variable coefficients are absent here and require their own analysis. No a posteriori existence or exclusion endpoint follows.

Dependencies: the Fourier transform, elementary integration, the explicitly proved generator and semigroup argument, and boundedness of degree-zero multipliers on H^s. No unverified numerical input is needed for the theorem. The association with the modal trial uses the separately confirmed scalar enclosures only to place that trial's frozen coefficients inside the rational parameter box.

## Verification record

Actual review model: claude-opus-5-5, recorded by Bedrock response metadata. The first review requested a global distributional stitching argument across the Fourier axes and an explicit reconstruction of the IPM multiplier sign. Both were added. The final review accepted the complete theorem at2026-10-20T16:25:33.166800+00:00; see notes/reviews/source_pole_closure_response.md and its metadata at the lane root. Exact rational arithmetic checked all eight parameter corners in code/check_margins.py. The separate code/check_membership.py checked the rational endpoints of the already independently confirmed modal source result SHA256 51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691 against the displayed box. The theorem itself has no numerical dependency; that input is used only for modal-trial association.
