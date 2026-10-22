Update 2026-10-22T09:02:50.011456+00:00: P326 now proves a common s disk for every coefficient. The older OPEN row below records the scope at P321 publication; bounds with order and convergence in x remain OPEN. P321 PROOF.md is unchanged.

# P321: all-order formal transverse compatibility

Checked 2026-10-22T08:45:54.952575+00:00. The standalone proof is PROOF.md, SHA256 85c17b14034cce8c3723585934c7408351c09536197f036df9fbc64962b536ad. This is a new local formal result in the tuned curved beta=2 family; general B2 remains OPEN.

For Ck nonzero, B=s+ks^2-(Ck/260)s^13 and H=-k^7/231, the two latest homogeneous constants at each order n>=2 can be chosen uniquely to remove the next thermal and vorticity residues. In the normalization delta theta_n=E t^n and delta omega_(n-1)=-2n E t^(n-1)YJ+F t^(n-1)Y, the residue matrix is

    [ 12Ck/[5(2n+1)],                     0 ]
    [ -k^8(2n+5)/[385(2n+1)], -9Ck/(10n) ].

Its determinant is -54C^2k^2/[25n(2n+1)], nonzero for every integer n>=2. Starting with P303/P306, induction therefore produces a formal x series whose coefficients are analytic germs in s, satisfying the transport and Poisson coefficient equations at every finite order.

| Item | Method and result | Verdict |
|---|---|---|
| Generic-n matrix and induction | Exact variation of the Cartesian coefficient recurrence; finite Laurent residue calculation with explicit curvature terms; nonzero triangular determinant; analytic primitive criterion. | CONFIRMED |
| Independent symbolic controls | 63/63, including generic-n identities, off-diagonal formula, determinant and supplemental finite-order substitutions. | CONFIRMED |
| Different exact series evaluator | 129/129 using a separately written Fraction Laurent class with propagated precision, direct physical forcing and primitive extraction; n=2,3,4,5,7,10,16 and three rational C,k pairs. | CONFIRMED |
| Formal series existence in the analytic-germ coefficient ring | Every earlier coefficient stays fixed after its compatibility step. No common germ domain is required for this formal statement. | CONFIRMED |
| Common s neighborhood, bounds with order, convergence in x or a PDE solution on an open set | Not established. | OPEN |
| Full-plane inverse, connection to the material center and global B2 endpoint | Not established. | OPEN |

The symbolic run was 2026-10-22T08:43:01.339498+00:00 to 2026-10-22T08:43:03.623750+00:00 (2.284250630 seconds), code SHA256 6e427ab50fbb3260977645583e9ea2b750611acc118f4cc3c1989421c9b4c83d. The rational-series run was 2026-10-22T08:40:11.453163+00:00 to 2026-10-22T08:40:12.946071+00:00 (1.492907732 seconds), code SHA256 212a96ad00bfe46dfa2206588f45cb0dc323741bae8ddeb5ef6035b2442ed42d. Total completed controls:192. Neither evaluator imports or executes lead or numerics code. No floating-point approximation is used in these checks.

The first symbolic harness returned17/60 because polynomial coefficient extraction was applied to an expression with an s-dependent rational denominator. Its source and results are preserved. Replacing that extraction with exact residues corrected the evaluator. Subsequent60/60 and62/62 versions are also retained before the final63/63 run. The proof-preparation log records an initial shell/Python quoting failure and the small algebra check that preceded the complete written draft.

Actual Opus5.5 collaboration is documented in verification/model_adjudication.md. Request553 gave no audit text;554 and555 completed. The second review's generic-n spot-check limitation and one omitted factor in the first review's explanatory line are recorded. The independent proof and controls settle these points.

This result supersedes any general claim that these tuned local data must encounter a finite formal-order obstruction. It does not supersede the global OPEN conclusion or prove the existence of a convergent local profile. T_end remains unset.
