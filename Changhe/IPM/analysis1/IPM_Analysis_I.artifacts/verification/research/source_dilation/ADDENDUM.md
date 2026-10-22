# Review clarifications and audit scope

The actual Opus 5.5 proof review accepted every identity and the domain
argument. Its five requested edits are supplementary clarifications:
none changes a hypothesis, identity or claimed inverse bound.

For vector f, B_j in(5) is the supremum of the entire vector-valued
derivative tensor in Frobenius norm, including all output components.
For scalar f it is the ordinary ordered-derivative tensor. A separate
componentwise bound may be inserted only with the corresponding sum
of component squares. P is arbitrary in the auxiliary theorem, including
P=0. R_s depends on w,q and s, not on a separate location P.

The same norm comparison also gives the optional estimate

 ||exp(t A_s)||_(Hs->Hs)
 <=ell^(-s)(1+R_ell/d_s)^s exp(-a_s t).

Its absence from the original statement is not a gap in the asserted
inverse estimates. In the continuity argument, for0<ell<=1 the Fourier
weights are bounded by the original weights; the prefactors ell^(-1)
and ell^(-2) are bounded and continuous on every[epsilon,1]. This is
the domination used in the proof. The V31 label names the lead request;
the complete independently proved content is stated explicitly in the
Exact statement section, so no external question is needed to use it.

The arithmetic checker uses Fourier-annulus examples, not the trial or
compact coefficients. These L2 examples directly test the norm identity,
which holds for every Hs function; they are not used to apply the inverse
theorem. Arb512 computes the rescaled Fourier support integral, while
mpmath.iv180 computes the original mass-weighted integral times the
scaling factor. Both outputs are enlarged outward by an exact dyadic
relative-plus-absolute pad of2^(-400). A third exact-integer root method
uses768-bit dyadic enclosures with cross-multiplied defining inequalities,
and a Machin alternating-series pi enclosure, to check containment in
both saved outputs. Positive integrands justify the directed subtractions
and products. Twelve exact polynomial Wiener integrals and homogeneous
symbol tests supplement the analytic proof. No floating norm is imported.

The first checker run stopped at an API typo iv.pi(), before producing
checks.json. Its source and traceback are retained as v1_failed files.
The repaired code uses the interval constant iv.pi. This did not change
a formula or output enclosure.
