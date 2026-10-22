# Lower Sobolev orders: local obstructions and exact constants

Date: 2026-10-20. Topic70, independent audit of SPEC3.13 and the lead's dib3 response. Status: proof drafted before computation and corrected after adversarial review; see evidence/verdict.json for the final verification status. These are local counterexamples and conditional analytic facts. They neither exclude an exact IPM profile nor establish a global inverse.

## 1. Conventions and frozen source operator

Use coordinates (s,y) centered at a source, constants A>1 and real g, and the global Fourier multiplier M with symbol xi²/(xi²+eta²), assigned0 at frequency0. On L² it has norm at most1. Define

 L = A s partial_s + y partial_y -1-gM.

The two-dimensional unitary Fourier transform is fhat(zeta)=(2pi)^(-1) integral exp(-iX.zeta)f(X)dX. Put ||f||_(H^sigma)²=integral(1+|zeta|²)^sigma |fhat|². M is defined globally after a cutoff, not by arbitrarily selecting a local inverse Laplacian. The source identity mu=1 for a C¹ exact density with nonzero gradient is proved in ../pure_source/PROOF.md; it does not require a C² density.

Let n>=1 be odd, p=(g+1-n)/A>1 nonintegral, J=(n-1)/2, b0=1, and

 b_(j+1) = -[(g+2j(A-1))(n-2j)(n-2j-1)] /
 [2(j+1)(A-1)(p+2j+2)(p+2j+1)] b_j,  0<=j<J.

Set H_n(s,y)=sum_(j=0)^J b_j |s|^(p+2j)y^(n-2j). Choose a product cutoff chi(s,y)=chi_s(s)chi_y(y), smooth, compactly supported, even in each variable, and equal1 on an open rectangle about0. Then h=chi H_n has these properties:

1. Lh is a smooth harmonic function on that rectangle.
2. h belongs locally near0 to H^sigma exactly for sigma<p+1/2 (for sigma>=0). It fails at equality. The same threshold describes its global H^sigma membership for the chosen product cutoff.
3. If1<p<2, h is not C² near0. More generally its singularity is present on the line s=0 at every sufficiently small nonzero y.

Thus local smoothness of Lh does not imply high local Sobolev regularity for h. This holds with the nonlocal multiplier present and fixed, not just for pure transport.

### Proof of the differential identity and harmonicity

The multiplier identity is -Delta Mh=-partial_s²h. For w=|s|^q y^r and lambda=Aq+r, direct differentiation therefore gives the LOCAL expression

 -Delta Lw = (g+1-lambda)partial_s²w + (1-lambda)partial_y²w.

This formula can be read distributionally after a cutoff. Because q>=p>1, w and its first s derivative are continuous across s=0; the second derivative is locally integrable and has no delta mass. No global definition of M applied to the growing uncut polynomial is needed.

For term j, lambda_j=g+1+2j(A-1). The first s-second-derivative coefficient vanishes at j=0. At adjacent terms j and j+1, the coefficients of |s|^(p+2j)y^(n-2j-2) are

 -[g+2j(A-1)](n-2j)(n-2j-1)b_j
 -2(j+1)(A-1)(p+2j+2)(p+2j+1)b_(j+1),

whose sum is0 by the recurrence. The final y second derivative vanishes since its y power is1. If a numerator in the recurrence vanishes, all later coefficients vanish, which only truncates the same cancellation. Hence -Delta Lh=0 wherever chi=1, including across s=0. Lh is a distribution there, and is locally L² for these parameters. To see explicitly why it is smooth, mollify it on a smaller ball. Each mollification is harmonic. For a smooth radial averaging kernel supported in a still smaller ball and with integral1, the mean-value property gives w_delta=w_delta*psi. Passing to distributions gives w=w*psi locally, a smooth function. Its Laplacian remains0. This proves claim1.

### Proof of the exact Sobolev threshold

For a noninteger q>1 and an even smooth cutoff equal1 near0, the one-dimensional function chi_s(s)|s|^q has H^sigma threshold q+1/2. Here are the integrability details, including the endpoint. For sigma=m+theta, m integer and0<=theta<1, the mth derivative on s>0 is a nonzero constant times s^a, a=q-m, as long as the derivative is locally integrable. All lower derivatives are less singular. If a<=-1/2, the mth derivative is not L², including logarithmic divergence at a=-1/2. For larger m, nonmembership follows already at a smaller order.

If a>-1/2 and0<theta<1, on0<z<x<delta the fractional derivative integral reduces, by z=tx, to

 integral_0^delta x^(2a-2theta) dx
 times integral_0^1 (1-t^a)²/(1-t)^(1+2theta) dt.

The t integral is finite and strictly positive: near1 the numerator is O((1-t)²), and near0 the condition a>-1/2 suffices. It is not identically0 since a is noninteger. Thus the first integral is finite exactly when theta<a+1/2, with logarithmic failure at equality. Across the two half-lines the analogous factor has denominator(1+t)^(1+2theta) and numerator(1 +/- t^a)²; it is finite under the same condition. Terms where the cutoff varies are smooth and add finite integrals. The equality between this difference-integral criterion and Fourier H^theta follows directly from Plancherel and Tonelli: integrate |exp(i xi z)-1|²/|z|^(1+2theta) first in z, then scale z by |xi|. Its coefficient is finite and positive for0<theta<1. This is also Proposition3.4 of Di Nezza, Palatucci and Valdinoci, arXiv:1104.4345; the argument here needs no quoted constant.

A product with a smooth compactly supported y function has the same threshold. For the upper bound use (1+xi²+eta²)^sigma <= (1+xi²)^sigma(1+eta²)^sigma and factor the Fourier integral. For necessity, localize in a y interval on which y^n is nonzero and apply a smooth y averaging functional with nonzero integral against y^n. This maps H^sigma(R²) boundedly into H^sigma(R): Cauchy-Schwarz in eta and (1+xi²)^sigma <= (1+xi²+eta²)^sigma prove it. The averaged leading term is a nonzero multiple of |s|^p, while the remaining terms contain at least two additional powers of s. At sigma=p+1/2 all those other terms belong to H^sigma and cannot cancel the leading nonmembership. Larger sigma are excluded by nesting. For sigma below the threshold every term belongs. This proves claim2. Claim3 follows directly from the unbounded second s derivative of the leading term when1<p<2.

The singular forcing outside the rectangle must not be discarded. This example does not contradict an assumed global inverse from a high forcing space to a high domain. It supplies no membership of Lh in that global high forcing space. Also, source-centered reflection parity in s is only local; global x parity around the physical origin requires an additional construction and is not asserted here.

## 2. What a two-order bootstrap would actually require

A purely algebraic domain-transfer lemma is useful. Let D1 be a subspace of D0, Y1 a subspace of Y0, and A:D0->Y0 one fixed linear operator. Assume A is injective on D0 and maps D1 onto Y1. If u is in D0 and Au is in Y1, choose v in D1 with Av=Au. Injectivity yields u=v in D1. All of the phrases 'one fixed operator', the inclusions, and the global domains are hypotheses. Injectivity of one operator and surjectivity of a different operator do not prove this lemma.

For the nonlinear profile use the canonical equation -Delta psi[u]=partial_x u and U[u]=(-psi[u]_y,psi[u]_x). Let c[u]=psi[u]_xy(0)/3, Gamma u=U[u]+c[u]X, V[u]=X/3+Gamma u, and F(u)=V[u].grad u-u. Thus V is affine, with fixed drift X/3, and V[u+v]-V[u]=Gamma v. This is the normalized profile equation, with no additional source terms. Put rho=rho_tilde+h, f0=F(rho_tilde), and

 A_h u=(V[rho].grad-1)u+Gamma u.grad rho_tilde.

Expansion of F(rho_tilde+h)=0 gives A_h h=-f0. But

 DF(rho)h=A_h h+Gamma h.grad h=-f0+Gamma h.grad h.

Applying a high-order inverse for DF(rho) to this last expression already needs high-order control of the quadratic term. A high-order inverse at rho_tilde is not surjectivity of the same rough-coefficient operator A_h. A legitimate route needs a uniform tame/global regularity estimate for A_h, or another argument that supplies these exact domain hypotheses. The frozen example above refutes replacing that global step by local smooth-forcing regularity alone.

## 3. Exact strain functional norm and failure below order2

For Schwartz functions use -Delta psi[f]=partial_x f, so psihat=i xi fhat/(xi²+eta²), and let ell[f]=psi[f]_xy(0). Its Fourier formula is

 ell[f]=(2pi)^(-1) integral m(zeta) fhat(zeta) dzeta,
 m(xi,eta)=-i xi² eta/(xi²+eta²).

For every sigma>2 the exact norm of ell as a real functional on H^sigma(R²), also on its real even-x odd-y subspace, is

 C_sigma = 1/[8 sqrt(pi(sigma-1)(sigma-2))].

Consequently the norm of c=ell/3 is C_sigma/3. These are whole-plane unweighted norms with the specified Fourier convention. They are not constants for the weighted jet realization.

Proof: Cauchy-Schwarz gives the squared norm (2pi)^(-2) integral |m|²(1+r²)^(-sigma). In polar coordinates the angular integral of cos^4(theta)sin²(theta) is pi/8. One can obtain it by integration by parts twice, or the elementary trigonometric expansion. With u=r² the radial integral is

 integral_0^infinity r³(1+r²)^(-sigma)dr
 = 1/[2(sigma-1)(sigma-2)].

Integrating u(1+u)^(-sigma) directly proves the last identity for sigma>2. Multiplication gives C_sigma². Equality in the dual norm is attained by fhat proportional to conjugate(m)(1+r²)^(-sigma). This belongs to H^sigma, has the reality symmetry, is even in xi and odd in eta in the appropriate imaginary Fourier sense, and therefore corresponds to a real even-x odd-y function. Smooth Fourier cutoffs away from0 and infinity approximate it if one prefers Schwartz test functions. This proves the exact norm assertion.

The functional is unbounded on H², and hence on every H^t with0<=t<=2. To include the critical endpoint explicitly, choose0<=chi_R<=1 smooth radial, equal1 for1<=r<=R and zero outside1/2<r<2R, and take

 fhat_R=conjugate(m)(1+r²)^(-2)chi_R.

These are Fourier transforms of real even-x odd-y Schwartz functions. With N_R=||f_R||_(H²),

 N_R² >= (pi/8) integral_1^R r³/(1+r²)² dr >= (pi/32)log R,
 ell[f_R] >= N_R²/(2pi).

The second inequality uses chi_R>=chi_R². Thus ell[f_R]/N_R is unbounded. This endpoint sequence need not vanish near the physical origin.

For every0<=t<2 there is also a sequence whose members each vanish in a neighborhood of the origin and thus preserve any prescribed center jet. The neighborhood shrinks with the sequence index; no uniform neighborhood is claimed. Take the compact smooth parity-compatible phi from ../far_domain/PROOF.md, supported away from0 and with ell[phi]>0, and set e_eps(X)=eps^(t-1)phi(X/eps),0<eps<=1. Exact scaling gives

 ||e_eps||_(H^t)²=integral(eps²+|zeta|²)^t |phihat(zeta)|² dzeta <= ||phi||_(H^t)²,
 ell[e_eps]=eps^(t-2)ell[phi].

Both formulas follow by substitution in the Fourier integrals; m is homogeneous of degree1. This proves unboundedness even on smooth center-vanishing perturbations for t<2. It applies to the proposed unaugmented low space H^(s-1) when2<s<3.

It also invalidates a general estimate for the full product Gamma e.grad u in that low space. Choose a fixed smooth compact u supported away from0 with X.grad u not identically0. On its support, the canonical kernel gives ||U[e_eps]||_(C^k) = O(eps^(t+1)) for each fixed k: the kernel and its derivatives are bounded off the shrinking support, and ||e_eps||_1=eps^(t+1)||phi||_1. The other term is eps^(t-2)c[phi] X.grad u, which diverges in any fixed local Sobolev norm. The small kernel term cannot cancel it. This disproves such a uniform bilinear estimate for the unaugmented norm. Weighted origin/jet conditions or an explicit |c[e]| norm can remove this particular obstruction; those bounds must be supplied separately.

## 4. C2 regularity and H3.1 do not imply center factorization

Let0<epsilon<1 and chi(r) be smooth radial, compactly supported, equal1 near0. Put

 rho_epsilon(x,y)=chi(r)x²y r^(-epsilon), with value0 at0.

This function has the required parity and vanishes on both axes. It belongs to C^(2,1-epsilon) and H^sigma for every0<=sigma<4-epsilon, but rho_epsilon/(x²y)=r^(-epsilon) has no continuous extension at0.

For C² regularity, the uncut expression is homogeneous of degree beta=3-epsilon>2 and smooth on the unit circle. Its derivatives of orderj<=2 are O(r^(beta-j)), so its first two derivatives extend continuously at0 with value0 and agree with the distributional derivatives. Its second derivatives are alpha=1-epsilon homogeneous. Their alpha-Hölder bound follows by a two-case argument. For points at distance d at least half the smaller radius, both radii are at most3d and the size estimate suffices. Otherwise the joining segment stays away from0 and the derivative bound O(r^(alpha-1)) gives C d r^(alpha-1)<=C d^alpha. The cutoff adds smooth terms.

For Sobolev membership, use a smooth dyadic annular partition near0. Up to finitely many smooth outer terms, its pieces have the form2^(-j beta)F(2^jX), where F is fixed smooth and supported on an annulus. By the Fourier scaling calculation,

 ||2^(-j beta)F(2^j .)||_(H^sigma) <= 2^(-j(beta+1-sigma))||F||_(H^sigma).

The sum converges in H^sigma whenever sigma<beta+1=4-epsilon and equals rho_epsilon away from0, hence distributionally. For epsilon=1/4 this gives H^3.1 and C^(2,3/4), yet no continuous factor. Adding a smooth normalized x²y cutoff does not repair the divergent factor. This is a function-space counterexample, not a solution of IPM. Even the stronger high Sobolev order must retain center factorization as a separate domain condition.

## 5. Interpolation and cutoff costs

For v in H³(R²),0<=s<=3, Holder's inequality in Fourier space proves

 ||v||_(H^s) <= ||v||_2^(1-s/3)||v||_(H³)^(s/3)

with constant1. Explicitly the integrand is the product of |vhat|² to power1-s/3 and ((1+|zeta|²)³|vhat|²) to power s/3. If chi is a smooth compact cutoff, |f|<=epsilon on its support and ||chi f||_(H³)<=B3, then

 ||chi f||_(H^s) <= (epsilon||chi||_2)^(1-s/3) B3^(s/3).

The actual cutoff and its support enter this statement. A disc-only derivative table does not by itself provide B3 for an extension. For bounds |partial^beta f|<=M_beta throughout that support and genuine weak derivatives through order3,

 B3² <= sum_(|alpha|<=3) [3!/((3-|alpha|)! alpha!)]
 [sum_(beta<=alpha) binom(alpha,beta)||partial^(alpha-beta)chi||_2 M_beta]².

This is Leibniz, the triangle inequality, and the exact expansion of (1+xi²+eta²)³. Cellwise derivatives omit interface measures if derivatives jump. In the present modal trial the stated exact C6 matching must be checked from its definition before using a global H3 residual; this lemma supplies no independent residual bound.

## 6. Weight, jet and symbol conclusions with their hypotheses

For the linear saddle geometry set D=2A+1,c0=(A+3)/2. The inequalities a>9/2, a<13/2 and -c0-aA+sD<0 are jointly equivalent to

 max(9/2, 2s-1/2+(s-3/2)/A)<a<13/2.

For a specified2<s<3, this interval is nonempty exactly when s<(14A+3)/(4A+2). It is nonempty for every2<s<3 exactly when A>=3/2. For the trial's A>10 the condition holds strictly. At s=5/2,a=5 the local rate is1-A/2, negative exactly whenA>2.

The scalar row4 exponent p2=(4A+1)/D=2-1/D has Sobolev threshold p2+1/2, proved with its matching conditions in ../y_axis_matching/PROOF.md. Allowing the homogeneous coefficient changes an already proved Fredholm index by+1 only IF it enlarges the domain by exactly one dimension with the same target and graph realization. Local counting alone supplies neither Fredholmness nor that identification. For completeness, under this hypothesis the kernel/cokernel dimensions follow from the exact sequence0->ker T_old->ker T_new->D_new/D_old->coker T_old->coker T_new->0, whose maps are inclusion, quotient and induced T. Its alternating dimension sum proves the index change. None of these hypotheses has been established for the proposed full IPM realization.

For integer s, a nonzero homogeneous remainder r^m F(theta), with the differentiated angular weighted integral finite and positive, has weighted top spatial derivative in L² near0 exactly when m>a+s-1: its squared radial integral is a positive constant times integral_0^delta r^(2(m-s-a)+1)dr. The endpoint is logarithmically divergent. For noninteger s one must define the norm rather than assert fractional derivatives have that pointwise form. One precise annular model is the following. Fix a nonzero smooth radial cutoff chi_A supported in1/2<r<2, and set

 N_(a,s)(u)² = sum_(j>=j0) 2^(2j(a+s-1)) ||chi_A(Z)u(2^(-j)Z)||_(H^s_Z)².

For u=r^m F(theta) and0<||chi_A r^m F||_(H^s)<infinity, exact homogeneity reduces this to that fixed positive norm squared times sum_(j>=j0)2^(-2j(m-a-s+1)). Hence the same strict threshold holds for every real s>=0 in this explicitly defined annular norm. Additional angular weights can be placed in the fixed reference norm if it remains finite and positive. No equivalence with an unspecified fractional corner norm is asserted. Angular singular weights and jet subtraction remain separate requirements. At a=5,s=2.5 the threshold is6.5; a surviving degree5 component therefore fails this model norm. Transferring this obstruction to the proposed realization requires its norm to control this annular norm, and that the nonzero degree5 component survive the specified projections. The trial-center topic addresses the latter condition, not the former.

The frozen homogeneous energy directional values are beta_fast=sA-c0-g and beta_slow=s-c0. These follow by the Fourier commutator with transport and the multiplier -g xi²/|zeta|². More explicitly transport contributes -c0 plus s(A xi²+eta²)/|zeta|², and the multiplier subtracts g xi²/|zeta|². At the illustrative parameters below both endpoint values are negative for2<s<3, whereas deleting the multiplier makes the fast value positive throughout that interval. This is an energy sign calculation. It is not an inverse theorem, and the rough local solutions of section1 do not contradict it.

## 7. Numerical verification plan, fixed exact inputs and dependencies

The illustration uses k=1615536043799051/9007199254740992, A=2/k-1, and g=29749490663333/10^12. Here k is the exact dyadic stored exponent. g is an explicit nearby decimal rational for the frozen counterexample, NOT a claim that an exact profile has that exact derivative. No scalar interval for a true unknown profile is being invented. Verify the recurrence for n=1,7,11 by rational coefficient cancellation and an independent triangular system, then certify p, p+1/2, the weight bounds and energy signs. Compare C_sigma at sigma=5/2 and153/50 using Arb512 and interval rational series. Independently compute pi=16atan(1/5)-4atan(1/239) with alternating-series remainders; enclose square roots by integer square-root rational brackets. All interval comparisons must enclose exact inputs and use outward endpoints. For Machin's identity, if a=atan(1/5), then tan(2a)=5/12 and tan(4a)=120/119. The subtraction formula gives tan(4a-atan(1/239))=1. This angle lies in(0,pi/2), for example by0<x-x³/3<atan(x)<x at these arguments and pi>3, so it equals pi/4. Truncating the alternating arctangent series after N terms brackets atan(x) between the partial sum and that sum plus its next term. For a positive rational q, n=floor(sqrt(q 2^(2P))) computed by integer square root satisfies n/2^P<=sqrt(q)<(n+1)/2^P. These exact rational bounds supply the independent square-root enclosures.

Dependencies: elementary distributional differentiation, Plancherel, Tonelli, Holder, smooth cutoffs, and the proved local mean-value argument. The strain test phi uses ../far_domain/PROOF.md and its final verdict. Source C1 geometry uses ../pure_source/PROOF.md. Row4 matching uses ../y_axis_matching/PROOF.md. Numerical data and review records will be pinned in evidence/. Literature verification: arXiv1104.4345, Proposition3.4, primary-source PDF inspected2026-10-20; it supports the Fourier/difference-integral equivalence, whose short proof is included above. No external transport regularity theorem is assumed.
