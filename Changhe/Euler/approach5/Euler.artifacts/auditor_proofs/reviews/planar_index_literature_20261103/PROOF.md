# What planar critical-point index results do and do not bound

Status: A2451-A2455 record the confirmed source scope, exact examples and conditional local-index consequence, with A2454 refuting a universal finite bound for arbitrary enclosing curves. A2456 keeps the actual flat accumulation and Euler problems OPEN. The existing configured model coordinator independently compared Sections3-5; its response is pinned. No claim about the common-flat Euler system is made.

## 1. Question and conventions

Let D be a planar disc, v a smooth real vector field, and C a counterclockwise simple closed curve on which v is nonzero. Its degree is the degree of v/|v|:C to the unit circle. The local index of an isolated zero is this degree on a sufficiently small surrounding circle. These notions must be distinguished: a curve enclosing several zeros has their sum of indices, not the index of one zero.

The remaining campaign question is whether a smooth quotient field with div v=B.v, B smooth, a flat central zero, and negative finite indices at all other zeros can have unbounded degrees on shrinking admissible circles. A2431 leaves this open. The stronger common-flat system F separately remains open under the same verdict. The results below do not answer that question.

## 2. Precise primary literature scope

Alessandrini and Magnanini, The index of isolated critical points and solutions of elliptic equations in the plane, Annali della Scuola Normale Superiore di Pisa, series 4, 19(4), 1992, pages 567-589, Lemma 3.1 and its immediate remark on page 577, concern a real C1 function u near an isolated critical point z0. The conclusion about the gradient index is I(z0)<=1. The Appendix, pages 586-588, proves it by separating finitely many positive and negative level sectors and computing the turns of the gradient on a suitably chosen boundary. The nonextremal case has index 1-L with a positive integer L; an isolated extremum has index 1.

The isolation hypothesis is explicit. It fails at the central zero when other critical points accumulate there. Nor can the index theorem be applied to an arbitrary planar field using only a divergence identity: a conservative field, or a Hamiltonian field after a fixed quarter turn, needs an actual local potential. In the nonzero-rotation carrier equation even a universal positive integrating density is an additional issue. The carrier proposal treats that issue separately.

The opening of Section 2 of the same paper, pages 570-571, concerns elliptic equations with Lipschitz leading coefficients, bounded first-order coefficients and uniform ellipticity, together with specific boundary conditions when counting critical points. It does not cover a degenerating weighted equation across the common-flat orbit without further work. In particular, the weight |S|^eta vanishes at that orbit, while grad log|S| has not been bounded there. The positive-S or negative-S off-orbit arguments already audited in LIT288 avoid this problem locally; they do not extend that elliptic input through S=0.

Only the cited introductory, Section 2, Lemma 3.1 and Appendix passages were read for this scope review, not every theorem of the paper. The scanned page 577 was also visually inspected. The Numdam original PDF and extracted text are retained. An earlier attempt to obtain the author's repository copy returned HTTP 403 and is recorded, rather than represented as a successful retrieval.

## 3. A divergence-free field of boundary degree two

Define f(x,y)=y^5+x^2 y^3-y and v=J2 grad f, where J2(p,q)=(-q,p). This polynomial field is smooth on the whole plane and divergence-free because mixed partial derivatives commute.

We have f_x=2xy^3 and f_y=5y^4+3x^2y^2-1. At a critical point y cannot vanish, hence x=0 and y=+/-5^(-1/4). These are the only two zeros. Their Hessians are diagonal with entries 2y^3 and 20y^3, both positive at the positive root and both negative at the negative root. Both zeros are nondegenerate and have index +1; the fixed orientation-preserving quarter turn preserves degree. Every circle centered at the origin with radius greater than 5^(-1/4) therefore has degree two.

This is Durfee's Example 2.4, The index of grad f(x,y), arXiv alg-geom/9506002. The retained downloaded manuscript is the version actually read, as identified by its hash. Its Example 2.4 exchanges the words minimum and maximum at the two roots. The direct Hessian calculation above corrects that labeling: the positive root is the minimum. This typographical issue does not affect the two positive indices or the degree. No general approval of Durfee's other results is asserted.

Thus divergence freedom does not bound the degree on every nonzero-boundary curve by one. This example has two positive-index zeros, no flat center, and does not contradict a proposed bound under the additional negative-index and flat-center hypotheses.

## 4. Arbitrarily large finite boundary degree, with a complete proof

For every integer K>=2 set

F_K(x,y)=product_{j=1}^K (y(x^2+j)-1), and v_K=J2 grad F_K.

Then v_K is a smooth divergence-free polynomial field on the plane with exactly K-1 zeros, all nondegenerate and of index +1. Consequently its degree on every centered circle of radius greater than one is K-1. The formula is Durfee's Example 2.5; the following argument independently checks its critical-point assertion.

Write s=x^2, a_j=y(s+j)-1, F=product a_j and T=sum_j product_{i!=j} a_i. Direct differentiation gives

F_x=2xy T, and y F_y=K F+T.

At y=0, F_y=(-1)^(K-1) sum_j(s+j), which is nonzero. At a point with x!=0 and y!=0, the equation F_x=0 gives T=0. The second equation then forces F=0 if F_y=0. But the factors a_j have distinct roots in y for fixed s>=0; exactly one factor could vanish, and then T is the product of the other factors, which is nonzero. This is a contradiction. Thus every critical point has x=0.

At x=0, F(0,y)=P(y)=product_{j=1}^K(jy-1). It has K distinct roots 1/K,...,1. Rolle's theorem gives one root of P' in each successive open interval. Since P' has degree K-1, these are all its roots and each is simple. Denote them y_l; all are positive and P(y_l)!=0.

At (0,y_l), F_xy=0, F_xx=2y_l T=-2K y_l P(y_l), and F_yy=P''(y_l). The logarithmic derivative identity, valid where P is nonzero, gives

P''(y_l)/P(y_l)=-sum_{j=1}^K j^2/(j y_l-1)^2<0,

because P'(y_l)=0. Thus both nonzero Hessian eigenvalues have sign opposite to P(y_l). Their product is positive. All critical points are nondegenerate extrema and the local degree of grad F, hence of v_K, is +1. The planar degree identity on a disc containing all zeros gives K-1. This completes the proof without a numerical computation.

The conclusion is a lack of a universal finite bound across all smooth divergence-free fields and enclosing curves. Each fixed example has finitely many zeros and bounded local degree; it does not produce one field with diverging degree at a flat accumulation point.

## 5. Conditional application and the missing premise

If a smooth divergence-free field on a disc has an isolated zero p, it equals J2 grad psi on a smaller simply connected disc: the one-form v_2 dx-v_1 dy is closed and the local Poincare lemma supplies psi. If a positive smooth density m instead satisfies div(mv)=0, the same construction applies to mv; multiplication by m preserves zeros and degree. The isolated critical-point index theorem then gives index_p v<=1.

These are conditional consequences with two necessary inputs: a suitable smooth density and isolation of the central zero. A bound derived after assuming isolation cannot then be used to prove that no other zeros accumulate at that same point. In the LIT301 dichotomy, isolation is precisely the branch not known in advance. Even the existence of a density for one field would not repair that logical circularity.

The independently proved examples in Sections 3-4 also show why replacing the isolated local index by the degree of any surrounding curve is invalid. They refute that broad replacement, not the narrower campaign conjecture about one flat accumulation point with only negative off-center indices.

## 6. Evidence and limits

in the team records records the original retrieval failure and both successful primary PDF hashes. The AM Appendix proof and specified source passages, and Durfee's introduction and Examples 2.4-2.5, were read. No full-paper audit is claimed. No numerical job, GPU, formal build, server or remote computation was used.

The exact polynomial calculations are elementary identities and a Rolle/degree argument. They do not require the carrier equation, scalar transport, pressure Poisson equation, a complete three-dimensional characteristic flow or any decay assumption. Therefore they cannot decide the original Euler nonexistence problem, or provide a counterexample to it. The actual bounded-divergence, flat-center, negative-index question remains OPEN.
