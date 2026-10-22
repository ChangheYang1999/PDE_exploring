# Independent adjudication of the draft inner derivative engines

UTC 2026-10-22T01:04:25.012240+00:00. Verdict CONFIRMED for source-level consistency with the conditional analytic theorem and the separate finite algebra checks. Numerical application remains OPEN. No cell of result181 has been evaluated. No preparation gate, source freeze, complete-cell audit or numerical result is accepted here.

I read the complete actual responses from claude-opus-5-5 for the draft source review and both precision follow-ups. Each ended end_turn. Their binding metadata are recorded in evidence/ENGINE_ADJUDICATION.json. These model comments were checked against the source and my own derivations; they are not substituted for an executed certificate.

I checked the exact ODE defect and derivative equations, both Green formulas, the direct Bhat1 primitive, product truncation derivative terms, the linear strain signs at frequency1, and the source placement of the frequency523 linear term. In engine_arb.py lines77–81 the low coefficient changes sign only for nu=1. The separate engine_iv.py sine folding implements the same exact map. This is a source inspection, not a runtime check. The saved finite matrix checker compares two independent algebraic expressions inside that checker, not the engine functions themselves. Source digests alone do not establish implementation equality.

The final review identified four documentation corrections, all accepted here. This paragraph supersedes the stronger wording in REVIEW_PRECISION_RESOLUTION.md, which is retained unchanged as actual review input. First, code/linear_angular_checks.py is the saved replay version, with a added read/assertion against the initial JSON; it cannot be the exact original inline program. The initial inline source was not retained as a standalone artifact. Its output was preserved and every mathematical field was reproduced by the saved checker. Second,2086,1044,33 and the degree bound are stated constants, not computed checker results. Their arithmetic follows separately: the primary product support has center1043 and slots0 through2086, with radial degree at most32 and stride33, hence degree at most68870. Third, the external checker supplies finite algebra evidence; the source inspection and eventual runtime comparisons are separate obligations. Fourth, the shifted linear-only slots run from520 to1566. The range0 through2086 belongs to the product, not to the linear term.

The compressed secondary encoding has center521.5 and maximum slot1043. This differs from the primary signed center1043. The assertion in the first source review that both are below1044 strides is too broad and is corrected by these explicit ranges. Neither correction changes the actual engine bytes. I independently re-read their allocation and extraction indices.

Exact diagnostic results are36720 ODE/truncation coefficient identities,3654 manufactured physical/density Green identities,136764 external linear angular matrix entries including implicit zeros, and8908 injective signed linear positions. These are finite manufactured or symbolic checks. The original and replay matrix outputs agree, including their matrix digest. I checked the recorded source and initial-output digests directly during this adjudication. No full residual, interval norm or runtime input-count claim follows.

The numerical obligations remain: canonical and tail pin checks, all44 prescribed cells, rigorous enclosures from both implementations,62688 derivative input-jet overlaps and17226 residual-coefficient overlaps per cell at Q16, complete output coverage and norm aggregation, actual maximizing-cell replay, complete actual result review, and later independent adjudication. The mathematical overlap tests support consistency but do not replace either remainder proof. No historical19389-cell W target, inverse theorem, fixed point or decisive endpoint is discharged.

Review inner_derivative_cells_engines_draft: request 02b4ad7c-0ec5-4678-aa35-45c7bb78e3dd; input SHA256 1fcc784ec694f90569bfd251c9af2ae67492daf7e3c0ef3764bc62f9de556942; raw response SHA256 d92b4bb14fee0b5366785bf560fe1557c38432b25e565b892fc622a2eea92331; ended 2026-10-22T00:59:56.370303+00:00.

Review inner_derivative_cells_engines_precision: request 7c8ede28-8605-4b2e-83d5-1afb9f0138e0; input SHA256 1ad453e93ffed44465e068667ac83fe69447190a315ef73c759da8e46bc445ce; raw response SHA256 ab1e5c227ee9452ca9dce3bd617b6bda50be0cd4fcd3afb54fbd40816f4d8587; ended 2026-10-22T01:01:09.761775+00:00.

Review inner_derivative_cells_engines_precision_resolved: request 6cbcedf6-3d98-430c-a9c0-23fe58237ac2; input SHA256 f6c0a665d38b2b909814090bbdc544abc391f3d8ab5f24263c0198e39024429e; raw response SHA256 8bf07ed6637ce2f3e1ad3a4fc4fbeff263e3297887b007bded3eb0f907f37f60; ended 2026-10-22T01:02:29.448011+00:00.

Source engine_arb.py: SHA256 1c81c3a7e0bb82f3c4a675030d2de202ea46d6b0fddd4ea59b39fda4a4cb8c0a.

Source engine_iv.py: SHA256 78233c2fc3d6b2b995b6d407a205978ff1300bb3bbce0d94447a8993d5729832.

