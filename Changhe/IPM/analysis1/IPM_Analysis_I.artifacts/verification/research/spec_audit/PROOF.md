# Audit of SPEC version 1: the proposed inverse is not a missing numerical constant

Date: 2026-10-20. This note audits the immutable SPEC snapshot in evidence/SPEC.md, SHA256 5ee50b95b732f4a5f08fe4552f56f1a3c1ee8e6fe7fa2dbb1b92374294159cd6. It does not exclude an IPM solution. The claims below concern the stated domain and codomain of its proposed inverse.

## Notation and hypotheses

Write k in (0,1), c_l=1/k, and rho_0=r^k Theta_0(theta)+O(r^(2k-1)) on closed angular intervals inside a quadrant, with the corresponding differentiated expansions. Let U be the canonical order-zero IPM velocity. Set G=X dot grad(rho_0) and

L h=(c_l X+U[rho_0]) dot grad(h)-h+U[h] dot grad(rho_0)+(sigma[h]/3)G,

where sigma[h]=psi[h]_{xy}(0). The intended far weight m is a positive constant times r^k to leading order. SPEC allows arbitrary h with |r^j grad^j h| bounded by m(1+log(1+r/L)), j<=4. Its proposed residual space Y consists of functions bounded by m(1+r/L)^(-delta), with corresponding derivatives, plus span(G), for delta>0. At ordinary points in a disc around the source, X controls C^{4,alpha} and Y controls C^{3,alpha}.

All test functions below have the required parity. Compactly supported tests are supported away from both axes and the origin, so h=x^2y b with b identically zero near zero. Thus the center normalization does not remove them.

## 1. The logarithmic far space is not mapped into the proposed Y

Choose a nonzero smooth angular function Phi, supported in the interior of a quadrant and extended with even-x, odd-y parity. Choose it not proportional to Theta_0. Let chi be a smooth radial cutoff equal to zero for r<R and one for r>2R. Define

h=chi(r) r^k log(r) Phi(theta).

This belongs to the stated far part of X and has no center normalization defect. Direct differentiation gives

(c_l r partial_r-1)h=c_l r^k Phi(theta), r>2R.

For this growing density, define the canonical velocity by the local term -h e_2/2 plus the principal-value integral of [K(X-Y)-K(-Y)]h(Y), as derived in ../trial_regularities/PROOF.md. The subtraction has zero symmetric annular integral by parity. Split at |Y-X|=r/2 and |Y|=2r. The local Holder subtraction gives O(r^k log r), the remaining interior region gives O(r^k log r), and the exterior is bounded by C r integral_{2r}^infinity t^(k-2) log(t) dt=O(r^k log r). Thus U[h]=O(r^k log r). Therefore both coupling terms containing U and a density gradient are O(r^(2k-1) log r). Since k<1, they are o(r^k). Also G=k r^k Theta_0+o(r^k). It follows that

r^(-k)Lh -> c_l Phi+(sigma[h]k/3)Theta_0.

For an element of Y, this limit must be a scalar multiple of k Theta_0; its decaying part tends to zero. The displayed limit is not such a multiple. Hence L is not even a map X -> Y with the stated arbitrary-angular logarithmic weight. No bound on its inverse can repair this domain/codomain mismatch.

Restricting the logarithmic coefficient to the single direction Theta_0 repairs this particular linear mismatch, but not the next nonlinear issue.

## 2. A logarithmic tangent weight does not contain an open family of exponents

Fix a ray with Theta_0 nonzero and let Delta>0. Then

|(r^(k+Delta)-r^k)Theta_0|/[r^k(1+log r)]
=|Theta_0|(r^Delta-1)/(1+log r) -> infinity.

Thus arbitrarily small positive changes of k leave the proposed fixed space. Negative changes belong to the space, but differentiability fails on that side as well. Indeed, putting Delta=-a<0, the difference between the normalized difference quotient (1-r^(-a))/a and log r, divided by 1+log r, tends in absolute value to 1 as r tends to infinity, for each a>0. The difference quotients therefore do not converge in norm to the pointwise derivative. A two-sided differentiable exponent parameter is not represented by this affine function space.

The scalar part of the quadratic remainder also exhibits the mismatch: (sigma[h]/3)X dot grad(h) has an r^k log r term when sigma[h] is nonzero and h has a nonzero logarithmic tail. This is not in Y+span(G). An exponent parameter with an exactly exponentiated tail, or a different fixed weight with positive slack, is needed; a finite logarithmic linearization alone does not justify the nonlinear map.

## 3. A first-order transport inverse cannot gain one isotropic derivative

Here is a local obstruction independent of the source resonance. Let q>=1, 0<alpha<1. Let V and the background be sufficiently smooth on a neighborhood of a compact flow box B away from the origin and axes, with V nonzero there. Suppose X controls the ordinary C^{q,alpha}(B) norm and Y on compact sets is C^{q-1,alpha}. Suppose the remaining terms of L are order zero, bounded from C^{q-1,alpha} compactly supported inputs to Y with their usual weighted tails. These are the bounds relevant to the canonical IPM coupling in SPEC; their elementary localization justification is given below.

Place B inside D_P away from P and both axes, with its closure contained between the finitely many radial joins if necessary. Take smooth flow coordinates (s,t) on B with V dot grad=partial_s. The parity of V makes all reflected supports equivalent flow boxes. Choose a smooth cutoff eta supported in B, equal to one in a smaller rectangle. Set

h_n=n^(-q-alpha) eta(s,t) cos(nt),

then reflect the support into the other quadrants with the required signs. Coordinate composition has fixed bounded C^{q,alpha} norms. The q-th transverse derivative of h_n has oscillations of amplitude comparable to n^(-alpha) at separations comparable to n^-1 on the smaller rectangle. Consequently

0<c<=||h_n||_X<=C,   ||h_n||_{C^{q-1,alpha}}<=C/n.

The first inequality is witnessed by the Holder seminorm of that q-th derivative; all lower derivatives are bounded above by the same elementary scaling. The transport does not differentiate the phase:

(V dot grad-1)h_n=n^(-q-alpha)(partial_s eta-eta)cos(nt).

It follows that its C^{q-1,alpha} norm is O(1/n). All order-zero terms obey the same bound, including the normalization functional. Hence

||Lh_n||_Y -> 0, while inf_n ||h_n||_X>0.

A bounded inverse Y -> X would imply ||h_n||_X<=K||Lh_n||_Y, which is impossible. The same argument applies with q=4 to the default isotropic spaces in SPEC. Moving from C^{2,alpha} to C^{4,alpha} at the source does not remove this obstruction.

For clarity about the nonlocal terms, a compactly supported h has canonical U[h] given by its order-zero singular integral and local term. On a fixed compact set, Holder boundedness at order q-1 follows by subtracting the value at the singularity, splitting distances at the Holder comparison scale, and using the degree-minus-two kernel and its derivatives. The support stays a fixed positive distance from the origin, so sigma[h] is an integral against a smooth fixed kernel and is bounded by C||h||_infinity. Outside a large fixed disc, differentiating the kernel gives |grad^j U[h](X)|<=C_j||h||_L1 r^(-2-j); the reflected density has zero integral, which can improve this rate but is unnecessary. Multiplication by grad(rho_0)=O(r^(k-1)) puts the tail in every residual weight r^(k-delta) with delta<1-k. Near zero, U[h] is analytic. Write U_1=x u and U_2=y v, with u,v even and u(0)=-sigma[h], v(0)=sigma[h]. Since rho_0=x^2y a, both U[h] dot grad(rho_0) and G retain the x^2y factor. Their constant factor coefficients cancel in U[h] dot grad(rho_0)+(sigma[h]/3)G. With a=1+O(r^2) and its corresponding differentiated bounds for the explicit trial, the remaining factor is O(r^2), with the weighted derivative bounds required by the stated weak origin weight. Parity removes every fourth-degree density monomial. Thus the nonlocal tail and scalar functional do not restore the lost derivative.

This proof needs the flow-box coordinate regularity required by its C^{q,alpha} composition estimates. It applies to the smooth interior regions of the explicit trials. It does not assert a Fredholm index on every conceivable graph or anisotropic domain.

## 4. What the frozen-source packet does and does not show

The scalar equation (A s partial_s+y partial_y-d)h=0 has solutions |y|^d F(s/|y|^A), with d=1+g_*. Differentiation in s costs A powers of y. This explains the formal threshold d/A. It does not by itself prove that a solution of the full frozen nonlocal equation exists, or that the variable-coefficient full-plane operator has an infinite-dimensional kernel. Replacing its multiplier M by 1 is an approximation requiring norm estimates. F1's full non-Fredholm and kernel claims therefore remain OPEN on a specified same-regularity or graph domain. The preceding derivative-gain obstruction is a separate, proved objection to the literal SPEC spaces.

## 5. Conditional iteration bookkeeping

The iteration's algebra is correct when c_l(h)=c_l+sigma[h]/3. However its velocity increment is U[h]+(sigma[h]/3)X, not U[h] alone. Its contraction difference contains

[U[h-g]+(sigma[h-g]/3)X] dot grad(h_next).

Thus the constants in a valid theorem must bound the full velocity increment and both terms of this bilinear expression. The listed bound on U[h] and the listed bound on U[h] dot grad(g) alone do not supply those constants. The scalar term also retains a logarithmic tail whenever g does, so its claimed Y_low membership fails for the same reason as in item 2. A norm for X dot grad(g), a specified scalar-velocity component in X_V, compatible embeddings, a complete closed iteration ball, and a justified limit passage are required. Weak-star compactness in an unspecified Holder-type space cannot replace these hypotheses.

## Scope and dependencies

Items 1 and 2 are explicit far-field counterexamples. Item 3 is the standard flow-box oscillation argument, spelled out here including parity and nonlocal tails. They refute the indicated function-space claims, not existence of a nearby IPM profile. The frozen-source kernel/index and an inverse in a correctly specified domain remain open. No numerical singular value can prove the contradicted isotropic derivative-gain estimate.

## SPEC v2 far-weight translation, 2026-10-20

This is an additional convention audit, independent of the preceding v1 counterexamples. Let m(r)=u^3(1+u^2)^((k-3)/2), u=r/L, so m(r) is asymptotic to u^k. A common allowed growth power gamma on corrections and forcing corresponds to the divisor m(r)(1+u)^(gamma-k). Thus the associated zero-order seminorm is

sup_r W(r)/[m(r)(1+u)^(gamma-k)].

The expression in numerics `cert_summary.py` and the lead's task note instead multiplies W/m by (1+u)^(gamma-k). It is equivalent at infinity to sup W u^(gamma-2k), so its allowed growth is 2k-gamma, not gamma. For gamma=1/2 and k about0.17936, this is the negative power about-0.14128. The positive scalar forcing G=X dot grad(rho) with a nonzero r^k leading angular term is excluded by this stronger norm: its weighted size grows like r^(gamma-k).

This observation does not falsify an upper bound computed with the stronger weight. Since gamma>k, such a bound implies the weaker norm bound using the divisor. It does mean that the stronger expression cannot be adopted as the full forcing space for the scalar-feedback operator without repairing the same far-field membership issue already identified. Exact power comparison proves all these statements; no numerical sampling is used. The lead must specify the divisor/multiplier convention consistently before quantitative inverse constants can be interpreted.
