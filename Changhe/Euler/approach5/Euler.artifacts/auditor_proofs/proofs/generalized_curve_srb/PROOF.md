# A given generalized unstable curve measure is SRB in dimension three

Date: 2026-11-02T22:06:14Z. Verdict: CONFIRMED as A216. This implication does not assert existence of the measure.

## Statement and notation

Let X be a C2 vector field on a closed smooth Riemannian three-manifold, with flow Theta and F=Theta_1. Let mu be an ergodic F-invariant probability supported on a compact invariant set K. Suppose a smooth positive volume form near K satisfies div X=-d for a constant d>0. Suppose mu is a measurable mixture of probabilities mu_gamma, each absolutely continuous with respect to arclength on a compact regular embedded C1 curve gamma. For almost every gamma and mu_gamma-almost every regular point x, assume gamma lies in the full Pesin unstable manifold W^u(x).

Then mu has spectrum (chi,0,-d-chi), with chi>0 and all multiplicities one. Its conditional probabilities on full Pesin unstable plaques are absolutely continuous with respect to arclength. Consequently h_mu(F)=chi. The full-flow average nu=int_0^1 (Theta_s)_*mu ds is flow-ergodic, has this spectrum and entropy, has absolutely continuous unstable conditionals, and has a positive-volume continuous-time basin.

This is the precise content of the literature agent LIT44. There is no Euler coupling assumption and no C2 measure-existence assertion.

## Proof

Each mu_gamma is nonatomic, so their mixture is nonatomic. The equilibrium set of X is F-invariant. If mu gave it full mass, F would be the identity almost everywhere and ergodicity on a compact metric probability space would force mu to be a point mass. Thus X is nonzero almost everywhere.

At a two-sided Oseledets-regular point, DF^n X=X composed with F^n is bounded for every integer n because K is compact. If X had a positive-exponent component, forward iterates would be unbounded; if it had a negative-exponent component, backward iterates would be unbounded. Tempered Oseledets projections justify these conclusions without a uniform angle bound. Hence X lies in the zero-exponent subspace. No integrability assumption on log|X| is needed.

Disintegration gives a regular base point on almost every incoming curve. Since that curve is nondegenerate and lies in its Pesin unstable manifold, at least one positive exponent exists. The determinant formula gives the sum of all three exponents as -d. There must therefore be exactly one positive exponent chi, one zero exponent, and one negative exponent -d-chi. The full unstable manifold is one-dimensional.

Here is the step from a curve mixture to unstable conditional absolute continuity. Choose a countably generated measurable partition xi subordinate to full unstable manifolds. Suppose a measurable set A has zero leaf arclength in xi(x) for mu-almost every x. Let G be a full-measure set on which this holds and xi(x) contains a leaf neighborhood of x. Almost every incoming conditional gives G full measure. Fix such a curve gamma and a regular base point x0 satisfying gamma subset W^u(x0). Exponential backward equivalence identifies all unstable leaves through points of gamma with the same leaf L.

For each x in gamma intersect G choose an intrinsically open segment I_x containing x and contained in xi(x). Each A intersect I_x has zero leaf arclength. The immersed one-manifold L is second countable, so a countable subfamily of these segments covers their union. On compact leaf charts, immersion is Lipschitz and Riemannian arclength is equivalent to coordinate length. Thus every A intersect I_x has zero ambient one-dimensional Hausdorff measure, and so does their countable union. Arclength on the embedded regular gamma is its ambient one-dimensional Hausdorff measure. Absolute continuity of mu_gamma therefore gives mu_gamma(A)=0. Integration gives mu(A)=0.

The preceding null-set property is equivalent to absolute continuity of the conditional probabilities on xi: one may normalize the measurable leaf-arclength kernels on bounded plaques, take their measurable Lebesgue decomposition against the conditional probability kernels, and select the measurable supports of their singular parts. A nonzero singular part would supply precisely a measurable A violating the property. This proves the required conditional absolute continuity. In particular, no assertion that a globally immersed leaf has its ambient subspace topology is needed.

Ledrappier-Young Part I, Theorem A, now gives the entropy formula chi; its statement allows zero exponents. Flow averaging preserves the spectrum and entropy because each bounded-time flow map is a smooth conjugacy for F. Entropy is affine under invariant probability mixtures. A full-flow invariant set is F-invariant, has mu-measure zero or one, and has the same measure under every flow translate; hence nu is flow-ergodic. The entropy formula, or the transported conditional representations, gives its unstable conditional absolute continuity.

Finally take a positive-length set of continuous-time generic regular points on an unstable plaque, restricted to a compact Pesin block away from X=0. Its short flow strip is a two-dimensional transversal to the one-dimensional strong stable direction. Absolute continuity of strong stable holonomy between such transversals and Fubini give positive three-dimensional volume to the stable saturation. Stable approach and bounded time shifts preserve continuous-time empirical limits. This yields the asserted positive-volume basin. The neutral flow direction is included in the two-dimensional transversal; no absolute continuity of an arbitrary one-dimensional holonomy is assumed.

## Dependencies and scope

The exact standard inputs are two-sided Oseledets, Pesin unstable manifolds and subordinate partitions, measurable conditional Lebesgue decomposition, Ledrappier-Young Part I Theorem A, and the Blumenthal-Young stable-holonomy theorem with a negative spectral cutoff. The last application was checked in A198/A201, including its flow-strip dimension and regularity.

For the compactification used in A198, a generalized curve measure already has a positive exponent by the curve hypothesis. The transition annulus is nonrecurrent. Outside it the time-one map and its derivative are the identity. Therefore an ergodic such measure is supported in the original compact core before applying any entropy assertion. Thus A198 can use the Ben Ovadia-Burguet Theorem A, Definition 1.2 and Claim A.1, without Theorem B. The existence construction and the endpoint-topology issue A202 remain unreviewed external dependencies. Neither unconditional existence nor vortical basin coverage follows from this reduction.

## Verification evidence

Read the complete LIT44 proof, including its intrinsic-leaf clarification. Independently checked the spectrum, conditional-null-set argument, flow average and support localization. Source details are retained in sources/empirical_entropy and in A198/A201. No computation was needed.
