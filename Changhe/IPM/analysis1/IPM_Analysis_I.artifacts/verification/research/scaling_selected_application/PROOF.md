# A three-annulus lower bound for the canonical scaling field

Written 2026-10-22T11:05:05.255894+00:00, before this application code or numerical run. Application OPEN.

## Statement, hypotheses and exact object

Use the distinguished exactly joined and normalized modal trial rho of modal_repair/PROOF.md with the fixed exact data data_exact/modal_v2.json, and the norm X of scaling_norm_lower_bound/PROOF.md:

    ||f||_X^2 = integral (f^2 + r^2 |grad f|^2) L^6 r^-6 (1+r^2/L^2)^(3/2-k) dX.

The dyadic constants have L>0 and 0<k<1/2. Put D=r partial_r and K=rho-D rho. The accepted modal_graph_scaling theorem gives K in X and LK=epsilon-D epsilon in X, with its stated broad graph domain and normalization supplements. K has strain Sigma=0 and centre functional J=-2. It does not belong to J=0.

Select exactly the three full positive degree7 knot spans with zero-based indices7,620,1564 from scaling_norm_lower_bound/evidence/input_manifest.json. Their exact logarithmic endpoints must equal the manifest and be strictly ordered with disjoint interiors. This is a finite annular selection, not coverage of the entire middle annulus. No claims are made for uncomputed spans.

On each span [a_i,b_i], let d_i=b_i-a_i and x=(log r-a_i)/d_i. The exact middle density is rho=r^3 sum_j H_j(x) sin((2j+1)theta), j=0,...,260. Set B_j=-2H_j-H_j'/d_i and C_j=3B_j+B_j'/d_i, where prime differentiates x. Define the rational number

    Q_i = d_i integral_0^1 sum_j ((1+(2j+1)^2) B_j^2 + C_j^2) dx >= 0,
    v(t) = L^6 exp(2t)(1+exp(2t)/L^2)^(3/2-k).

If an actual dual arithmetic computation with full polynomial equality, exact square-integral equality, enclosure replay and later independent review proves q>0 and q^2 < pi sum_i v(a_i) Q_i, then ||K||_X>q. A number produced by a preparation run alone is not accepted without this additional complete application audit.

## Proof

Differentiation gives K=r^3 sum B_j sin((2j+1)theta) and DK=r^3 sum C_j sin((2j+1)theta). The angular derivative has cosine coefficients r^3(2j+1)B_j. Distinct positive integer sine and cosine frequencies are orthogonal with squared norm pi on [0,2pi]. Since r^2|grad K|^2=(DK)^2+K_theta^2 and dX=r^2 d(log r)dtheta, the exact integral over one annulus is

    pi d_i integral_0^1 v(a_i+d_i x) sum_j ((1+(2j+1)^2)B_j^2+C_j^2) dx.

Both factors in v(t) increase strictly and remain positive because3/2-k>0. The nonnegative bracket therefore gives the lower bound pi v(a_i)Q_i. The three annuli have disjoint interiors, and their boundary circles have measure zero. Summing their lower bounds and using nonnegativity on the complement proves ||K||_X^2 >= pi sum_i v(a_i)Q_i > q^2. Positivity of q permits taking square roots. The proof requires no far-tail estimate for this lower bound; membership K in X is independently inherited from modal_graph_scaling. The right-endpoint sum, if displayed, bounds only the three-annulus union from above.

## Reproducible arithmetic and optional consequence

Use the already frozen scaling_norm_lower_bound source. Its Cox/monomial and independent de Boor/shifted-Legendre calculations reconstruct all261 odd modes and all2088 density coefficients on every selected span from exact hexadecimal inputs. The exact Q_i results must agree. Arb512 and mpmath.iv220 evaluate the positive endpoint expressions by different weight formulas. Every selected span is replayed. An additional reverse FLINT rational sum and integer squared-endpoint checks verify strictly downward publication. The original gate keeps its three-span acceptance labelled preparation only. This application has its own actual review and postreview verdict, never relabels an unfinished1558-span run, and retains all source-provenance qualifications.

A same-trial FINAL bound ||LK||_X<=b with b>0 would imply C>q/b for any asserted estimate ||h||_X<=C||Lh||_X on a domain containing K. On the normalized J=Sigma=0 graph core of the modal_graph_scaling addendum, its sequence K_delta converges to K in X with LK_delta converging to LK in X; taking limits gives the same consequence if the estimate holds for every K_delta. This argument never asserts J(K)=0 and never extends to a fixed-leading-tail space excluding the required sequence. For b>0 the lower quotient follows from q<||K|| and ||LK||<=b. A zero image would instead contradict such an estimate directly. Any numerical quotient remains OPEN until the denominator, exact norm and trial identities are reviewed together. This is a necessary lower bound, not inverse existence, nonlinear closure, X3 distance or any decisive endpoint.

Dependencies: scaling_norm_lower_bound/PROOF.md, THEOREM_ADJUDICATION.md, WORKFLOW_ADJUDICATION.md and SOURCE_PROVENANCE_CLARIFICATION.md; its exact source freeze and external rehash; modal_graph_scaling/PROOF.md, ADDENDUM.md, REVIEW_RESOLUTIONS.md, NONZERO_IMAGE.md and FINAL_ADJUDICATION.md; the exact modal-repair certificate. All remain part of the application pin union.

Restrictions: write only this lane. No JavaScript/TypeScript, servers/listeners/tunnels, RLScience cluster, Lean/Lake, posts or human contact. One heavy nice19 job at a time; begin only after181 process group is gone.
