# Final theory audit, version 2

Frozen 2026-11-04T15:20:47.401054+00:00, with mathematical evidence through AT2933, exchange v888, published 2026-11-04T15:16:49Z. This replaces version 1 as the current theory auditor's Part VII handoff. Version 1 remains immutable. Later dated audit supplements may add corrections or new results. This report does not claim that the remaining campaign time has elapsed.

No complete fixed-parameter stationary IPM existence certificate has been obtained at the present cutoff. The campaign has proved conditional full-operator estimates, certified the residual and several background quantities at a corrected center, and narrowed the remaining quantitative closure problem. The missing hypotheses are explicit. Failure of a particular sufficient estimate does not disprove existence.

## Fixed center and certified numerical inputs

The fixed parameter remains c = 4076476460239181/2251799813685248. The authoritative Candidate 007 is unchanged. The center used for the strongest current bounds is its exact potential correction C2-N1-013-phi-007-sector-d8-leg24-lat-nf2, b18s2. Its density and velocity are rho_star = rho_007 - Delta phi and u_star = u_007 + (-phi_xy, phi_xx). The exact source identities are recorded in SOURCE013_CHAIN_CONDITIONS_v05.json and the companion FINAL_THEORY_AUDIT_v02.json. Here F_star=(cX+u_star).grad rho_star-rho_star and L_star k=(cX+u_star).grad k-k+U[k].grad rho_star.

For q = 21/10 and W(X) = sqrt(1 + 4|X|^2), write N(f) = ||(1-Delta)^(q/2)(Wf)||_2, with the registered unitary Fourier and ordered Cartesian derivative conventions. The existing complete certificates give

    0.0000007959400186993612 <= ||F_star||_2 <= 0.0000007961206656880281,
    0.0035510975483434412497 <= N(F_star) <= 0.0055545729030073655758.

Thus the P-S1 target 0.006 is certified; 0.0055 is not decided by this interval. This weighted Sobolev norm is distinct from the strong Holder norm S_F of the prompt. Floating-point moment and FFT screens supply no replacement certificate.

For V=cX+u_star, the complete background cover gives

    (c+1+V.X/(1/4+|X|^2))I - q Sym DV
      + [[(rho_star)_y,-(rho_star)_x/2],[-(rho_star)_x/2,0]]
      >= (704955805507/10^12)I.

It also gives |grad h_star|<=1/4 for h_star=-Delta phi and ||Sym Du_star||_op<=137/125. The stronger correction-gradient upper 71/500 is regional only: four radial indices remain outside that stronger certificate. It cannot be inserted as a global input.

## What the theory results establish

The weighted commutator, Garding and semigroup arguments establish the k = 0 full-operator lifting theorem under their stated regularity, domain, core, semigroup and decay hypotheses. For the corrected center, every 0 < beta_1 < 704955805507/10^12 gives the conditional estimate

    N(k_0) <= N(F_star)/beta_1 + C_1 ||F_star||_2,
    L_star k_0 = -F_star.

Here C_1 is finite but uncomputed. The associated conditional L2 inverse norm is below 0.570726. This is a full-generator conclusion within those hypotheses. It is not obtained by substituting the full operator into a frozen-origin formula. It supplies no numerical strong-norm radius by itself.

Restricted small-perturbation weighted inverse results and the Sobolev invariant-ball framework are also proved within their respective hypotheses. Their common domains, full inverse assumptions and perturbation constants must be preserved. A symbolic restricted radius is not a certified self-map radius. Any return to the prompt's stronger Holder lifting route retains alpha/(2c-2) < delta < 1, 1 < nu < 2 and all other stated weight, decay and source restrictions.

A separate full-operator example proves that an L2 gap and smooth forcing alone cannot guarantee the desired local regularity over a class that includes the zero background. For c X.grad - 1 on its maximal L2 distributional domain, the full inverse has norm 1/(c+1), while a smooth annular source can produce a solution locally in H^s exactly for s < 1+1/c, with failure at the endpoint. This example is unnormalized. It does not contradict the Candidate 007 or Source013 theorems and does not classify all sufficient regularity hypotheses.

The campaign supplies further audited tools for the quantitative step: Fourier-moment and derivative-energy estimates, exact low/high-frequency identities, kernel upper bounds, a radial-core decomposition, far-field absorption estimates and lower restrictions on named sufficient charges. These tools retain their own premises. They do not by themselves establish H4 or a stationary solution.

## The simultaneous closure conditions

The H4 principal rate is the certified whole-plane matrix rate, not automatically its origin ceiling. Put J=(1-Delta)^(1/2) and g=J^q(Wh). On the admitted common domain, if the near form costs e||g||_2^2 + P||h||_2^2 and all remaining forms cost eps_rest||g||_2^2 + C_rest||h||_2^2, the required conditions include

    e + eps_rest <= 704955805507/10^12 - b_0,
    C_0 >= P + C_rest.

Under all retained far-route assumptions, the certified strain upper fits the far absorption test with exact free margin 71675071190082633/5629499534213120000. This is conditional on the analytic transfers used in that route.

The current coherent pair is NEAR_CHECK_v09 and closure version 8. The following exact budgets use the certified whole-plane derivative uppers and set the unknown remainder entries to zero:

| Case (b_0, mu) | Near loss e | Room for eps_rest | Near price P | CE allowance D_out | D_out-P |
|---|---|---|---|---|---|
| (11/20, 72) | 152627111489/10^12 | 2328694018/10^12 | 113428316345 | 123369792300 | 9941475955 |
| (103/200, 68) | 180101237602/10^12 | 9854567905/10^12 | 451198667779/5 | 99695324090 | 47277952671/5 |

A positive room does not bound the actual missing forms. The fallback also needs its mu=68 kernel certificates. The program's printed price rooms 9941475900 and 9455590500 are conservative lower displays. The separate near-table allowances 122000000000 and 98693500000 are different quantities and must not replace D_out.

Closure version 7 with NEAR_CHECK_v08 has rate rooms 925591681/10^12 and 8091034531/10^12. Closure version 6 used unproved derivative targets. Those historical calculations and their cutoff exclusions retain only their stated parameter scope. The current direct NR-25 moment upper enlarges the rate rooms without changing the price rooms.

The full real S1 reference ball is

    B={k: ||k||_2<=17/8750000, N(k)<=1/2},

with no ell restriction. The existing beta_0>2.00215453 and the certified correction-gradient upper 1/4 support beta_0_star=7/4, subject to the full inverse hypotheses. With f=0.0000007961206656880281, its output radius is R=f/(7/4)<=0.000000454926094679. The proposed beta_0_star=93/50 needs a global gradient upper that has not been certified.

Two different sufficient losses enter the theorem. Lemma KB gives a reference-ball matrix loss

    ell_KB = q S(A) + V(B) < 0.152070,
    beta_K >= beta_star - ell_KB > 0.

The HF-Q/CE-B self-map estimate instead uses the nonlinear loss L_B(R,Kbar;B,A). For a strong radius 0 < M <= 1/2 it requires

    C_0 R^2 <= M[(b_0 - L_B(R,Kbar;B,A))M - n],
    b_0 - L_B(R,Kbar;B,A) > 0,

where n>=N(F_star), R=f/beta_0_star is supplied by the full L2 inverse, and Kbar is an admitted strict CE-B graph witness. These conditions must hold together with the full generator and fixed-point hypotheses. The current scalar witnesses use M=387/1000 at the plan and M=361/1000 at the fallback, with nonlinear upper displays 0.3651689966 and 0.3412910741. Every recentering, compactness and common-domain hypothesis must hold for the same center, norms and parameters.

The smaller KB number cannot replace this nonlinear loss. The positive core term of the specified sufficient formula alone gives L_B>(9/20)Kbar>(9/20)M, hence the lower values 0.17415 and 0.16245 at the current witnesses. This is a lower bound on that sufficient formula, not on an optimal operator loss. AT2917 refutes the conflation and AT2918 confirms the corrected conditional statement and unchanged scalar arithmetic. Theory version 25, E-v24-1, repairs the inherited theorem and table wording; AT2930 confirms that repair. The older AT978 conclusion is retained only in the scope of its standalone proof with the exact nonlinear loss and positive slacks.

The numerical norm-input obligation H-NEARU and the complete background condition are supplied. The remaining Sobolev obligations are:

| Open row | Required statement for the same corrected center and reference ball |
|---|---|
| H-RC | RC-1 through RC-10 of the full recentering theorem, including the structural potential, quantitative bounds and common-domain conditions. The exact structural constraints alone do not supply all ten. |
| H1 | The actual closed generator, common smooth core, weighted semigroup and graph comparison needed to identify the weighted solution with the unique L2 solution. |
| H2 | The uniform full L2 inverse of L_star+U[k].grad on the prescribed ball, with the stated beta_0_star and output radius. |
| H-BALL | The full real S1 reference-ball hypotheses and center-matrix premise of Lemma KB; the certified matrix bound alone does not supply the whole premise. |
| H4-REST | An estimate for the remaining forms, including the transport, mixed and Riesz commutator terms, within the simultaneous rate and price rooms above. |
| H-N1 | The analytic near-estimate hypotheses for the actual coefficient, the whole-plane core split and the noncompact erfc-log cutoff. |

These rows are the obligations of the invoked theorem, not claims that every possible existence proof needs them. Their exact versions are in T2_CLOSURE_CHECK_v08 and the full recentering theorem cited there. The q=21/10, mu=72, nu=1/40 kernel bounds apply only at their audited parameters. H-REG is an additional open row for the stronger Holder conclusion V11-2(d), not for the Sobolev conclusions V11-2(a),(b). It requires the imported exterior and uniform lifting hypotheses, with the stated weight and source restrictions. The near parameter nu=1/40 is distinct from the 1<nu<2 source weight in the ordinary frozen Holder estimate.

## Interpretation limits and audit corrections

For S=Sym Du_star, the exact Source013 point P=(0,167/4000) gives

    2.561605274583231 <= ||Delta S(P)||_op <= 2.561605274583232,
    u_3 = 2 m_2(S) >= 5123210549166463/10^15.

The first statement is an independently replayed point enclosure. The second uses a sharper internal rational endpoint, not doubling a rounded display, and requires the ordinary Fourier differentiation, inversion and finite-moment hypotheses with no unaccounted zero-frequency polynomial. It strengthens the earlier origin lower. The separate lower M_S >= 10529.58564315332 remains valid in its own admitted moment convention. Neither lower bounds an actual signed quadratic form.

For the specific sufficient high-frequency charge phi K_* u_3/mu_r^2, with phi=(1+sqrt(5))/2, the current closure-version8 rate rooms give K_half cutoff enclosures [151.855500860944,151.855500860945] for the plan and [73.818964551323,73.818964551324] for the fallback. The least integer cuts passing the necessary lower-charge test are:

| Case | K | K_q | K_half |
|---|---|---|---|
| Plan | 195 | 164 | 152 |
| Fallback | 95 | 80 | 74 |

Here K_* is 4[sinh(q log 2)-q sinh(log 2)]/(log 2)^3 plus respectively 5q/2, q or q/2. The plan trials 208,224,241 now pass all three necessary tests. At K_half the fallback trial 72 fails, whereas 74 and 76 pass. A passed test gives no moment upper, low-frequency price or H4 estimate. The remainder cutoff mu_r may differ from the near cutoff mu. The older K_half cutoffs near 240.87 and 81.47, and their trial exclusions, belong to the old rate rooms. Comparisons with unproved low-frequency prices remain FLOAT and EXTRAPOLATED under open band separation.

The unwindowed FFT screen has exact discrete normalization N^-2 sum|F| and a discrete Plancherel identity, but neither supplies a continuum error bound. Independent complete-source point calculations prove that h=Delta^2 partial_x(partial_y chi+phi) satisfies

    h(8,16) in [-0.008183924976268348,-0.008183924976268347],
    h(16,32) in [-0.003315170023150601,-0.003315170023150600].

Its exact odd parity in y gives a nonzero jump across the opposite y-edges of each square. The admitted boundary theorem therefore proves divergence of ideal exact-sample absolute FFT sums under unlimited refinement on either fixed square of half-width 16 or 32. This conclusion is about the periodic extension on a fixed square. It gives no finite-grid bias magnitude or direction, no whole-plane moment upper, and no divergence result for the whole-plane moment. The production arrays also use interpolation whose error has not been bounded. Ideal exact-sample divergence alone does not imply divergence of those production values. In particular, the inference made in three passages of theory_v23 is refuted at AT2882; its corrected scope is confirmed at AT2883. Agreement between two grids is not an error bar.

The audited cos-squared taper is C1 and piecewise smooth, but not C2 at its transition interfaces. It makes opposite-edge values match. For the ideal window W_L and A(f)=(2pi)^(-2)||fhat||_1, finite ordinary Fourier moments give

    |A(h)-A(W_L h)| <= A((1-W_L)h).

A rigorous windowed calculation would therefore need both a numerical error bound for A(W_L h) and a bound for the omitted-window term. The seven saved FFT diagnostics supply neither. Their approximately 3.001280 percent spread is a sensitivity observation; opposing trends in the windowed and unwindowed data do not prove a bracket. The two windowed points also change the grid spacing. The exact scalar comparisons and conditional window inequality are confirmed at AT2811 and AT2812. AT2813 keeps the true moment OPEN.

The homogeneous scaling lemma for the far-field model is valid on a dilation-invariant class with finite positive weighted integral. Its criterion and optimization are independently checked at AT2838. The asserted transfer from exterior agreement to all global model dilations is false in general (AT2839): a smooth cutoff of the singular multiplier |X|^(-alpha), zero near the origin and equal to it outside a fixed disk, has a finite rate-only bound, while the uncut homogeneous multiplier has no such bound on all dilations. A strict obstruction for the actual far form needs an exterior test at a controlled scale and a quantitative comparison error below its margin. The one-dilate comparison FS-1 in T2_ROUTE1_v02 is independently confirmed at AT2859: a strict model margin transfers to the true form if the form and price errors at that same dilate total less than the margin. The conditional price comparison is now supplied by Lemma E, independently confirmed at AT2876 and AT2877. For nonzero real f with f,Delta f in L2 and finite M(f)^2=integral f^2/(4|X|^2), it gives ||W^(-1)J^(-q)f||_2 <= M(f)+(q/2)||Delta f||_2. Hence eps=2t+t^2, t=(q/2)||Delta f||_2/M(f), and t scales as the inverse dilation length. The continuous test, its Laplacian bound and the form-side comparison error remain unproved. The saved discrete epsilon is FLOAT. The model and discretization numbers remain FLOAT. AT2861 also corrects the pointwise P=0 wording: the zero-price estimate must fail somewhere on the dilation orbit of each positive-form test; it need not fail at the original test.

The direct/core-split moment minimum NR-35 and the version-specific scalar tables are confirmed at AT2905 through AT2907. TNR28 repairs the curvature word flagged at AT2908: 1-(1+u)^(-q/2) is concave for q>0 and u>=0, since its second derivative is -(q/2)(q/2+1)(1+u)^(-q/2-2). TNR29 corrects two downward displays to 151.8555 and 73.8189 without changing the exact enclosures. AT2921 through AT2923 confirm both revisions and their unchanged conditional scope. Theory version 25, E-v24-2, also repairs the producer citation: NEAR_CHECK_v08 used near_check_v03.py and NEAR_CHECK_v09 used near_check_v04.py. AT2931 confirms the distinct program identities; AT2932 confirms the later verdict inventory.

T2_PART7_v14/v15 are confirmed at AT2913 through AT2915. Their updated homogeneous-model and low-frequency diagnostics use the current rate rooms. The fallback trial 76 passes the necessary lower-moment test; its low-frequency price near 0.91 times the room is EXTRAPOLATED and the band separation is OPEN. The model calculations remain FLOAT diagnostics, not certified continuous tests, an actual far-form obstruction or a bound on the relevant supremum. AT2916, AT2924 and AT2933 leave the full existence claim OPEN.

## Remaining verification and continuation

All five middle-region blocks have distinct independent actual reviews and AN adoptions. Together they cover all 561 middle annuli. The global assembly is independently confirmed at AT2869 through AT2871, adopted by AN917, and its actual adoption is authenticated at AT2885. AT2872 keeps full closure OPEN. Its complete near coefficient is a(X)=[(4u(X).X-c)/(1+4|X|^2)] erfc(log(|X|/sqrt(8))/L)/2, L=log(8)/(2sqrt(pi)), with the admitted smooth extension at zero. For the full ordered Cartesian derivative tensors, D4 is in [444.194167252431246601983284,444.194167252431246601983285), D5 in [4186.352092180269533722245141,4186.352092180269533722245282), and D6 in [63050.392730580225839237008532,63050.392730580225839237053713). NR25 gives M4(a)<2691.963673338907009954203108 in its stated Fourier convention. All source-containment, analytic-remainder and decay premises are retained. Regional Laplacian energies become ordered Cartesian norms only through the admitted complete whole-plane identity. Missing annuli, endpoints or actual adoption records cannot be filled by a stored passing flag or a floating-point aggregate.

The smallest useful next step is to certify the remaining quantitative H4 form estimates and complete their source-specific inputs, then verify all self-map hypotheses simultaneously. No definitive closure ratio is reported while the theorem threshold is conditional.

The evidence package must retain the owner files targeted by approved relative links. PS1, PS2, C5 and the historical origin-baseline replacement have separately checked actual postconditions. In particular, this agent must retain research/node_disk_region_targets/disk_primary.json as the unchanged independent regular owner of the C5 input, SHA256 9df8ce6c1c870930f4bcd436933faadaf97221d85d3965edcffb4c50fc87fc2c, 40493229 bytes. The undertakings continue through the campaign end and thereafter as published evidence. Packaging must preserve the relative layout or materialize verified identical bytes. These actions do not repair the earlier unrelated deletion of the distinct Source009 artifact; that historical defect remains separately recorded.

The collaboration used the theory and coordinator agents configured as the main model, with repeated audit findings and corrections exchanged through immutable files. Actual provider-response model identity remains unverified. No JavaScript or TypeScript, servers, cluster use, remote computation or proof-assistant build is used by this agent.


## Reading order and evidence

1. [The current certificate chain](SOURCE013_CHAIN_CONDITIONS_v05.md) fixes the exact center, norm conventions, background cover, near assembly and theorem hypotheses.
2. [The two-loss correction](../research/final_draft_loss_audit/PROOF.md) distinguishes the matrix and nonlinear estimates; [theory version 25 review](../research/theory_v25_audit/PROOF.md) confirms the repaired statement and producer citation.
3. [The final new-results revisions](../research/tnr_v28_v29_audit/PROOF.md) and [the T2 final summary review](../research/t2_part7_v14_v15_audit/PROOF.md) bind the latest theory accounts.
4. [The closure calculation review](../research/closure_v07_v08_audit/PROOF.md) checks the coherent version 8 tuple, common inputs and conditional scalar inequalities.
5. [The chronological verdicts](../AUDIT_LEDGER.md) and [topic index](../research/README.md) give claim-level results and standalone proofs. A later entry can repair an earlier statement; an earlier OPEN or REFUTED entry is never silently relabelled.

The companion JSON binds the report, the selected verdict entries and the complete dependency maps through version 1 and the directly changed dependencies through AT2933. All its paths are relative to the theory auditor agent directory. These are offline mathematical and arithmetic audits, with exact rational and Arb checks where applicable. No Lean or Lake verification was run.
