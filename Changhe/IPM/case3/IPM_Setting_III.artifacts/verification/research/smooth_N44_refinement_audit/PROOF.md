# Third common-budget smooth refinement: N44 M40

Written 2026-10-21 before launch. This is the mathematical definition and verification protocol for a finite numerical experiment on the original full-plane Setting III equation. No claim about its output is made before the output exists.

## Exact finite field and its scope

Fix ell=5/2, L=1 and the saved binary number p=float(1/ell). Put alpha=(1-p)/2, w=(1+r^2)^(-alpha), sigma=r^2/(1+r^2), t=1-2w, and

    rho(x,y)=y w sum_{k=0}^{39} sigma^k B_k(t) cos(2k theta),
    B_k(t)=sum_{j=0}^{44} z_{kj} T_j(t).

The coefficients z are to be supplied by the saved NPZ file. The expression sigma^k cos(2k theta) equals Re((x+i y)^(2k))/(1+r^2)^k. Consequently the formula is real, smooth on the entire plane, even in x and odd in y, including at the origin and both axes. Its density and first derivatives have growth O(r^p) and O(r^(p-1)). Since0<p<1, it belongs to the required growth class whenever its measured nonzero center slope is retained. The formula itself imposes no x^2 factor. These conclusions hold for any finite real coefficients and are independent of optimization.

The velocity is the canonical full-plane inverse of this density, never an additional optimizer variable. The independent density-moment inverse and its full exterior integral are described and tested in the earlier inverse topics. The center strain is a convergent angular-mode functional that retains the leading-mode local term. The exact defining transport equation, its residual, and the origin safeguards are those of PROMPT.md; this is not the hydrostatic limiting problem.

The constraint K=a0 uses the verified positive K/a0 reporting chart from the scaling topic. It removes a spatial representative only in that chart; it cannot fix a0 or ell. Fixing ell=5/2 here is a parameter experiment, not a without-loss-of-generality choice. The solver also constrains the canonical strain c=1-ell. Independent evaluation must remeasure this constraint. The literal binary exponent need not satisfy ell*p=1 as an exact rational equality; its exact leading far-field defect must be reported, as in results148 and164. An exact rational-exponent modification is a separately defined field, if needed.

A finite angular representation need not be an exact solution. The finite-angular exclusion theorem does not rule out convergence of such approximations or the numerical YES standard. Conversely, small sampled errors and formula-level smoothness alone do not establish that standard.

## Controlled comparison

Use the same independent N24 M20 seed as the N36 M32 and N40 M36 experiments, with coefficient padding and projection onto the two linear constraints. Keep1000 maximum function evaluations, jet weight1, common squared-slope scale368.7801401458402, no optional right preconditioner, the density-moment full-plane inverse with composite order108, length1, and the solver's default resolution-dependent training grid. The common two cubic compatibility residuals are retained. Only the finite basis and its prescribed grid change. The older runs using another inverse are not part of this controlled three-resolution comparison.

The canonical inverse and analytic Jacobian code are unchanged. Their source hashes, seed hash, command, environment, start time, matrix-cache identity and checkpoint progress are recorded. An optimizer stopping at its evaluation budget has not demonstrated stationarity. Same evaluation budgets do not mean same wall time or a proof that basis error is isolated; unresolved optimization error must remain explicit.

The N44 basis has1800 coefficients, and the prescribed91 by81 training grid has7371 points. Its two cached velocity matrices require212,284,800 numeric bytes, plus metadata. This fits the lane's2GB cap at preparation time. Keep all coefficient files and summaries. Any later removal of regenerable matrices must be logged and leave their identities intact.

## Verification after the run

Reconstruct the saved field with the independent reader, exact rational center and Taylor functionals, and scalar multiprecision primitives. Repeat the N40 audit with unchanged physical sample sets: wide and local between-node grids, complementary angular charts, at least three physical extents, changed infinite-tail quadratures, and selected75/110-digit comparisons. A separate physical-space inverse with Cartesian finite differences checks selected points; its parity-aware treatment near axes must be compared with direct high-precision derivatives rather than trusting cancellation-dominated quotients.

Report sampled absolute R, both prompt denominators and their pointwise ratios by region and location. A zero denominator is undefined, with its numerator recorded; there is no arbitrary denominator floor. Check parity, canonical center, a0, both cubic identities, higher center jets, far-field defects, all apparent equilibria found on the audited domains, and coefficient sensitivity. Compare all three common-budget runs using the same evaluator, including shifts in a0 and higher jets. Do not identify small coefficient singular values with a physical gauge tangent without an independent norm and tangent calculation.

The conclusion is confined to the tested fields, finite samples and observed sensitivities. Numerical YES requires the complete prompt evidence to be convincing; a uniform global residual enclosure or an exact-existence proof is not an extra requirement for that numerical endpoint. Until the comparison and its independent review are complete, the endpoint remains UNRESOLVED.

## Dependencies and evidence order

Read research/smooth_N36_refinement_audit/PROOF.md and N40_PROTOCOL.md, research/smooth_N40_refinement_audit/PROOF.md and verification/SUMMARY.md, then the present protocol and its verification outputs. The independent inverse, scaling, exact-parameter and finite-angular proofs are linked in research/INDEX.md. No producer evaluation code is imported into this experiment. Actual Opus5.5 collaboration is recorded through the lead-lane exchange, and its conclusions are checked independently.
