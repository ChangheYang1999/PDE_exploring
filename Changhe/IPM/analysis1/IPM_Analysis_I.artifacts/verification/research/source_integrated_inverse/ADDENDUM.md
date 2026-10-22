# Actual input linkage and proof-review obligations

The complete actualOpus5.5 proof review accepted the analytic argument,
subject to the mechanical obligations stated in PROOF. All tensor ceilings
are the full ordered Frobenius norms from topics84,85,89,95. They are not
componentwise bounds. The canonical source equalities, spline regularity
and seven-span coverage are imported and hash-checked.

The cutoff is literally the one in topic95: differentiating T gives its
exact S polynomial, and differentiating each Q piece in tau gives minus
the b piece there. The checker verifies C4 matching at all four radial
joins. The output audit checks these derivative identities as exact
polynomial identities, not a plot or a comparison of sample values.
The support is closed radius23delta/8, strictly inside B_(3delta).
The unchanged divergence estimate follows from div(V-Dz)=0:
|div w|=|grad theta.(V-Dz)|<=C_theta M_V(9/2)delta, so its half in E_s
combines with s||Dw|| to give exactly the a^* used in the proof.

All15 weighted cutoff moments were evaluated by two exact-rational
methods. The first uses the explicit radial tensor list and power
antiderivatives; the second differentiates (x^2+y^2)^n and integrates
its squared tensor via Bernstein means. Arb512 and mpmath.iv180 then
compute the scalar bounds independently. Their exported intervals are
enlarged outward by(1+max(|lower|,|upper|))*2^(-400), which is negligible
for the published ceilings but permits strict higher-precision audits.
No floating approximation is imported into a rigorous inequality.

The scales are exactly{1} union{j/4000:1<=j<=80}. There are81, including
33/2000,1/100,7/2000 and1/500. Each is checked at s=61/20,153/50,31/10,
and with the uniform interval formula(10). The minimum is over upper
bounds for these81 scales, not over the actual inverse norm or all scales.
The same physical operator is being bounded, in different equivalent
norms. The ell^(-s) conversion is retained whenever an Hs bound is quoted.

No lower bound on the actual inverse norm is inferred from these figures.
No scalar strain feedback or residual multiplier is included. In particular,
these constants should not be combined with an unvalidated forcing norm
to assert a rigorous local or global nonlinear conclusion.
