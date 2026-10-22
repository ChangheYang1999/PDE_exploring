# Independent verifier result

Mathematical verdict: **UNRESOLVED**. Neither decisive endpoint in PROMPT.md has been established. In particular, there is no verified a posteriori existence theorem near X3 and no verified exclusion of a nontrivial numerical-uncertainty neighbourhood of X3, in P_2, an intermediate P_m, or P_infty. The verifier does not authorize a decisive YES or NO.

This is the final mathematical reading guide. The observed run end and elapsed time are recorded separately in `notes/verifier_run_close/terminal_record.json` when that record exists. Before it exists the run is still active. A report's last-update timestamp is not, by itself, evidence that research has ended. The chronological findings, methods, dates and verdicts are in `VERIFY_REPORT.md`; topic reading order is in `research/CURRENT_INDEX.md` and `research/INDEX.md`.

## Completed results that bear directly on the endpoint

The canonical Green law, its sign, the centre strain and the normalization `3 c_l - psi_xy(0) = 1` were reconstructed independently. The numerical candidate X3 is reconstructible from the actual coefficient data. Its nonzero normalization and transport defects do not exclude nearby exact solutions. The separate exactly joined, exactly normalized canonical modal trial has its own immutable exact JSON data, proofs and certificates. It must not be identified with the stored floating modal representation or with the published X3 ansatz.

For this exact modal trial, write `D = X.grad`, `epsilon = (c_l X + U).grad rho - rho`, `K = rho - D rho`. The accepted scaling identity is `L K = epsilon - D epsilon`, where L is the stated normalized linearization. The diagnostic norm is

    ||f||_X^2 = integral_R2 (f^2 + r^2 |grad f|^2)
                          L0^6 r^-6 (1+r^2/L0^2)^(3/2-k) dX.

Here `L0` denotes the spatial scale called L in the certificate; it is not the linearized operator. Its exact value is `8614738245908811/1125899906842624`, and `k = 1615536043799051/9007199254740992`.

The strongest completed independent derivative-norm composition gives the strict whole-plane bounds

    ||epsilon||_X < 1.49546805188731021373656,
    ||L K||_X    < 2464.68293019825564964515.

These bounds include both infinite tails. They use the complete 7,809-cell middle certificate, 44 refined inner cells and the inner tail, and 89 refined outer cells and the outer tail. The two arithmetic paths use Arb balls and mpmath interval arithmetic, with exact rational data and independent scalar reductions. Counts and individual replay coverage are stated in the parent verdicts; a complete sum is not a claim that every cell was replayed a second time. Read `research/derivative_norm_regional_composition/PROOF.md` and `research/derivative_norm_regional_composition/evidence/both/verdict.json`, with all mandatory parent and postreview records.

A separate three-annulus computation gives

    ||K||_X > 170.953964620623929217261.

The annuli are the full selected spans 7, 620 and 1564. Their omitted complement is nonnegative. This is not a completed integration over all middle spans. The supplemental literal comparison checked 6,264 coefficients each for density, K and D K, totaling 18,792, and three exact square integrals. Read `research/scaling_selected_application/PROOF.md`, its mandatory `COEFFICIENT_COMPARISON_CORRECTION.md`, and `evidence/verdict.json`.

Consequently, a same-norm estimate on a domain containing K, or the specified normalized graph approximants, would require

    C > 0.069361443018.

This is a necessary lower bound on a possible constant. It is not an inverse bound. K has centre functional J=-2; the normalized statement uses graph approximants, not the false assertion J(K)=0. On span{K}, the finite best constant is `||K||_X / ||L K||_X`. The stronger failure of every finite constant concerns domains containing the independently constructed quasimodes. Read `research/scaling_domain_scope/PROOF.md` with its timestamp correction, `research/center_weighted_quasimodes/PROOF.md`, and their final verdicts. An obstruction transfers to any extension agreeing on the obstructed set with the same norms. The mandatory clarification of the late review dialogue is `notes/numerics_late_norm_audit/FINAL_EXTENSION_ADJUDICATION.md`.

## What remains unproved

There is no accepted choice of complete spaces and operator realization for which the required inverse or alternative stability result, admissible normalized domain, nonlinear estimate and strict closing inequality have all been established for this candidate. The conditional two-norm iteration theorem does not supply those missing hypotheses. Same-space quasimodes, failures of compactness or graph-norm nonlinear continuity, and obstructions in the stated factor or axis norms rule out specific proposed approaches. They do not classify every possible topology or exclude the requested PDE branch.

The tighter numbers `0.385656000027` and `585.874000000002` remain conditional on the numerics lane's physical derivative majorants. The independent complete norm certificates above do not discharge those hypotheses. A floating mixed-trial quotient, sampled residual maximum, finite-section singular value, or small coefficient discrepancy is not a rigorous transfer or closing estimate.

The verified local trial-centred exclusions do not supply a proved meaningful uncertainty ball containing X3. The distinction between finite centre regularity and smooth factorization remains essential. No nearby P_infty conclusion follows from a P_2-compatible trial.

## Evidence and report limits

Each accepted topic has an informal proof, its stated assumptions, exact source bindings, numerical or analytic verification records, and a dated verdict. Mandatory corrections accompany preserved earlier texts. A successful byte-hash check certifies byte correspondence only. It does not replace mathematical verification, prove an unexecuted calculation, or authenticate a timestamp externally.

Actual Claude Opus 5.5 review requests and responses are preserved under `notes/reviews/`, with the returned model, request ID, exact input hash and stop reason. Advice was checked independently; arithmetic, domain and scope errors were rejected and followed up. Earlier incomplete or failed requests are not counted as completed reviews. The original pre-Astra verifier record is archived and is not treated as independent Astra work.

Saved-report acceptance applies only to the named snapshot and stated changes. The last report-delta adjudication, when finalized, is `notes/terminal_report_deltas/verdict.json`. It does not convert unreviewed historical numerics claims into certificates. The terminal record identifies whether the live reports still match those saved bytes and separates report cutoffs from observed lane endings.
