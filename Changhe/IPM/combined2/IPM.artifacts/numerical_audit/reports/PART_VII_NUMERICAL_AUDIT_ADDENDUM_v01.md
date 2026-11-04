# Numerical audit addendum: final integration and corrections

Frozen 2026-11-04T15:15:12.846605+00:00. This supplements [the Part VII contribution](PART_VII_NUMERICAL_AUDIT_v01.md) and [guide version 7](AUDIT_READING_GUIDE_v07.md). Its evidence cutoff is AN941. The earlier frozen reports remain unchanged.

The numerical conclusion remains unchanged: no complete stationary existence theorem is certified. The fixed Source 013 residual, whole-plane background bounds and near derivative norms retain their admitted status. The current conditional scalar budgets use near-check version 9 and closure-check version 8. Six Sobolev obligations remain open: H-RC, H1, H2, H-BALL, H4-REST and H-N1. H-REG is additional for the stronger Holder conclusion.

The most important correction is the distinction between two losses. The reference-ball matrix estimate is

$$
\beta_K\geq\beta_*-\ell_{\mathrm{KB}}>0,
\qquad \ell_{\mathrm{KB}}<0.152070
$$

on the admitted rectangle $\|k\|_2\leq17/8750000$, $N(k)\leq1/2$. The nonlinear self-map condition is instead

$$
C_0R_*^2\leq M\bigl[(b_0-L_B(R_*,\overline K;B,A))M-n\bigr],
\qquad b_0-L_B>0.
$$

Here $R_*=f/\beta_{0*}$, $f\geq\|F_*\|_2$, $n\geq N(F_*)$, and $\overline K$ must be an admitted CE graph witness. All source, full-generator, domain, inverse and H4 hypotheses remain. Substituting the smaller matrix-loss upper for $L_B$ is invalid. The [independent loss check](../research/closure_loss_distinction/PROOF.md), AN940, proves that the positive core term alone is greater than $(9/20)\overline K>(9/20)M$. At the two current witnesses this exceeds 0.17415 and 0.16245, respectively, both greater than 0.152070. This is a lower bound on the chosen sufficient-loss formula, not on an optimal operator constant.

Independent 768-bit evaluation of the full $L_B$ formula confirms its stored upper bounds 0.3651689966 and 0.3412910741. The closure program already uses the separate losses correctly, so its numerical outputs do not change. The ambiguity occurred in inherited theory-exchange prose and coordinator drafts. T1 accepted the correction in its dated 15:05Z note and plans an immutable erratum. TNR29 already keeps the losses distinct. At this addendum's cutoff the corrected theory exchange and final coordinator text have not yet received their final audit.

| Current case | $M$ | Upper bound for $L_B$ | Exact rate room | Exact remaining price room |
| --- | ---: | ---: | ---: | ---: |
| Plan, $b_0=11/20$, $\mu=72$ | 0.387 | 0.3651689966 | 0.002328694018 | 9941475955 |
| Fallback, $b_0=103/200$, $\mu=68$ | 0.361 | 0.3412910741 | 0.009854567905 | 47277952671/5 |

These rates and prices have different roles. Both remainder stand-ins remain zero placeholders; neither positive room supplies its missing analytic estimate. The fallback's kernel constants and allowance still require their own audit.

The [current Part VII integration check](../research/t2_part7_current_integration/PROOF.md), AN937, verifies T2_PART7_v15 and independently evaluates all sixty printed NE-lo price rows and ten scale/slack rows. The fallback cut 76 is not excluded by the current necessary $K_{\mathrm{half}}$ test. Its proposed price near 0.91 times the remaining room uses an EXTRAPOLATED kernel formula and an open frequency-separation argument. No combined sufficient estimate follows. The old exclusion of this cut must retain its old rate.

The [far-model arithmetic check](../research/far_model_current_budget/PROOF.md), AN935, verifies the saved decimal calculations for twelve tests, twenty-four rate rows and thirty-two price rows. The largest sampled current ratios $\Gamma/c_*$ are approximately 0.586883389596 and 0.193694376689. They are model diagnostics with unvalidated quadrature, not upper bounds on a continuous supremum or estimates for the actual far form. The earlier ratio near 1.201 used the old plan rate. Its diagnostic exclusion does not transfer to the larger current room.

The [theory-version-24 integration check](../research/theory24_numerical_integration/PROOF.md), AN941, authenticates the separate theory reviews and compares all twelve current cut intervals, thirteen moment intervals and thirty-nine decisions with the independent numerical calculations. Its forty-four dated inventory entries contain thirty CONFIRMED, two REFUTED and twelve OPEN labels. One source-program citation requires correction: near-check version 8 used near_check_v03.py, whereas version 9 used near_check_v04.py. This citation error does not change either execution. The inherited loss identification above is excluded from the integration verdict.

TNR28 corrects the curvature explanation from convexity to concavity; TNR29 rounds the necessary cutoff displays downward to 151.8555 and 73.8189. The [complete text comparison](../research/tnr28_correction_audit/PROOF.md) and [display-repair check](../research/final_citation_display_repairs/PROOF.md), AN934 and AN939, confirm that no mathematical table or conclusion otherwise changes. The same latter topic confirms N1's repaired citations of N2_FINAL_SUMMARY_v05 and its correct sections. The [strong-norm wording repair](../research/strong_final_account_audit/REPAIR_PROOF_v01.md), AN933, preserves all six admitted Candidate 007 lower bounds. Corrected-center FLOAT diagnostics still supply no certified upper bound for the prompt's $S_F$ norm.

The [chain integration](../research/chain_v05_numerical_integration/PROOF.md), AN931, and [final theory-handoff integration](../research/final_theory_numerical_integration/PROOF.md), AN936, agree with the numerical evidence and retain all analytic hypotheses. Their frozen source cutoffs precede the later corrections; later dated audits supplement them rather than rewriting history. The [dated numerical ledger excerpt](AUDIT_LEDGER_AN931_AN941.md) gives each claim, method, result and verdict.

This addendum introduces no new field integration or existence claim. Computations used one permitted CPU worker with one thread. The model collaboration continued through the configured theory agents; the actual provider model identifier is unavailable. The previously stated owner-file retention commitments and the campaign stop times remain in force.
