# Domain, source-binding and scope clarifications

2026-10-21. Read with PROOF.md.

For the general jump calculation assume, as in topic135, that h is continuous and compactly supported in an annulus, piecewise C2 up to finitely many circular interfaces and zero in both end regions. Then h is globally H1 and L2, U[h] is globally H1 by its bounded Fourier multiplier, and Sigma(h) is finite because h vanishes near the center. Mere local L2 membership would not imply H1 regularity of U[h]. The lower-order term has matching Sobolev traces across the circle; H1 in two dimensions alone does not give a continuous pointwise representative. The jump formula is a distributional trace statement, and a classical trace description is used only when separately available. These corrections to the review's wording do not change the proof.

The frozen report attributes the bound2.5e-14 to the saved pieces. Topic135 actually concerns the exactly C0-repaired selected columns, including their support joins. It is not a bound for the raw saved functions or their retained combinations. The report supplies no evaluated amplification factor or repaired operator matrix difference with that assertion. The independent fixture refutes only the context-free inference from that scalar bound alone. Its L and k equal the captured exact diagnostic weight parameters, but its background, R, spacing and coefficients are deliberately a model example. It neither proves nor disproves the actual10^-11 assertion with the actual grid and coefficient map. That assertion remains OPEN, as does the claim that repair preserves printed spectra.

The stronger source-binding checker compares the complete weighted_rows function body, excluding only its docstring, with an independently written AST specification. This includes the quad conditional selecting sqrt(dtv) versus ones, dtv=diff(t_eval), dt=diff(t_eval), the branches selecting values only, the reshape, angular weights, both row products and the final concatenation. It separately binds uu, mr, w_i, t_eval and the call constructing Aw_all. Thus the algebraic function of any supplied coefficient array Xu is identified. It does not prove that the raw file Mat contains physical sine coefficients of Lh, authenticate execution of any numerical job, or validate the grid. The interpretation of Xu as those image coefficients is an explicit hypothesis of the mathematical row formula, not a newly certified input fact.

Exact C1 matching means value AND first derivative matching at every interface. With the compact annular and background hypotheses this suffices for local H1 images. The C2,1 repair is sufficient and stronger. Global weighted image membership and exact retained-vector matching need further evidence.

The transfer inequality in PROOF concerns the smallest generalized singular value on a fixed coefficient section and consistent original/repaired column coordinates. Both row matrices must use the same row discretization. Q is assumed to be an exact whitening of the exact original Gram, not a floating output declared exact by a residual check. Arbitrary consistent column scalings can be used; topic133's application uses original column norms. No version of the theorem has evaluated epsilon or eta for the actual retained section. No all-singular-value transfer, rounding bound, grid convergence or continuum assertion is claimed.

The review offered to strengthen the fixture to the whole model row. That strengthening is not needed here and is not adopted as a new quantitative result. The independently verified enclosures concern the defined jump contributions only. The exact common bounds are

    9.9378689e-8 < H1 jump contribution < 9.9378690e-8,
    1.4054269e-8 < H1q jump contribution < 1.4054270e-8.

All displayed endpoints are exact decimal rationals rounded strictly outward. Source-only checks and the model fixture give no verdict on an actual finite spectrum or an IPM endpoint.
