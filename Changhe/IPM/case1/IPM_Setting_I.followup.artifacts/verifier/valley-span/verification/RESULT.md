# Valley-span audit

Date: 2026-10-20T18:55:18.541165+00:00. Verdict: stored central-difference arithmetic CONFIRMED; the positive-slope exclusion argument REFUTED; nonlinear family status and the underlying physical measurements OPEN.

All central and second differences were recomputed from the saved scalar values. At120x48 the signed combination of modes0,1 with coefficients(-0.16752723,0.38483517) matches the supplied grid change delta_c=+0.00154562825253635 and delta_xstar=-0.00158680041345960. At96x40 the corresponding coefficients are(+0.11542024,-0.34228346). Both examples refute the sign-based assertion that no combination can produce opposite changes.

Using all three120x48 modes matches delta_c,delta_xstar,delta_C with coefficients(-2.36998787,3.55297251,0.41498929), but these are much larger than the tested step0.05. Other observables disagree: predicted delta_gP=0.00309306 versus0.00226165, predicted delta_d3=0.000548223 versus-0.0000193526. These statements concern the supplied scalar finite-difference columns, not the true derivative of a canonical profile. No conclusion about the full grid-to-grid state or a nonlinear family follows from the two-observable match.

The measured120x48 mode1 displacement is |delta_c|=0.0006337814, with residual norm increases1.68% and1.74%. This does not verify a width0.001 within2%. At96x40 mode1 the tested displacement is only0.0002592818 and the increases are20.07% and19.99%. The two-grid broad flat-width wording is unsupported by these particular directional samples. Separate reoptimized fixed-c_l runs are different data.

The reported96x40 mode1 d3 slope is-0.0334241 per unit c, hence a first-order change-3.34241e-5 over delta_c=0.001. Thus the statement that these slopes yield at most1e-5 is also incorrect even at the linear level.

Recommended replacement: the saved directional observations do not establish that the grid difference is outside the soft span. Direct span projection in a common state norm and nonlinear checks are needed. The sampled120x48 mode1 changes c by approximately0.000634 with less than1.8% norm increase; the corresponding96x40 mode1 sample is about20% above its base norm at delta_c approximately0.000259. These are diagnostics at discrete stagnation fields, not a family of profile solutions.
