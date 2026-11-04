# Numerical audit at the mid-campaign checkpoint

Recorded 2026-11-03T08:35:11Z, actual UTC. This is an immutable snapshot for the coordinator's next exchange. Later dated entries in [AUDIT_LEDGER.md](../AUDIT_LEDGER.md) govern any subsequent result.

No complete stationary existence theorem has been certified. The numerical audit has established exact structural constraints, complete local source bounds and several concrete failures of earlier diagnostic claims. For the current certification center, C2-N1-009, the remaining numerical work is a complete finite-annulus calculation followed by whole-plane assembly and a global background cover. None of those pending computations is a premise of the results below.

## Fixed source and established constraints

The parameter remains exactly

    c = 4076476460239181 / 2251799813685248.

The authoritative Candidate 007 file has SHA256 `ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21`. Its complete residual is F=(cX+u).grad(rho)-rho. Independent exact reconstruction and containing analytic integration gave

    0.3766893247058942619446457 < ||F_007||_2
                                  < 0.3766893247058942619446458,
    7.8281155856563372424543013 < ||r F_007||_2
                                  < 7.8281155856563372424543014.

All 160 positive odd residual modes through 319 were included. These are whole-plane certificates for the reference, not for a fitted correction. The full argument and retained evidence are in [the Candidate 007 proof](../research/candidate007/PROOF.md), with dated verdict AN-005 in the audit ledger. Its exact origin normalization and eleven forbidden far-field sectors were independently checked in AN-001. The 1,060 null directions in its original coefficient representation are coordinate redundancies; they are not a kernel theorem for the PDE.

The current center is rho_009=rho_007-Delta(phi), with all 11,025 elementary atoms of its frozen correction retained. The raw correction SHA256 is `a04eb34fb51df70756faf2761bd9d6ab332566cbe3d361c92e70746f38c6b48c`; the independently equivalent elementary representation has SHA256 `1784016e1a8796587eecaa12b4e9c2d8193f218f39bb42b2b94d385892bbddf8`. The exact constraint A+3B=0 holds, hence the correction has ell=0. The origin slope lies strictly between 10.297317139577998823917123 and 10.297317139577998823917126. The eleven forbidden sectors remain zero. The complete leading allowed circle norm is nonzero and lies between 0.000202164530645166655885 and 0.000202164530645166655888. The source identity and proof are in [the registered 009 structural result](../research/reference_b14s_audit/RESULT_PROOF.md).

These checks distinguish an exactly preserved cancellation from a small soft-penalty row. They also prevent transferring a bound from an older correction merely because its file name or sampled loss is similar.

## Complete local bounds for Candidate 009

Write W1=(1+4r^2)^(1/2) and W2=(1+r^2)^(7/10), the registered P-S1 and P-S2 weights. Ordered derivative tensors use the full Frobenius multiplicities. On the closed disk r<=1/50, the following strict upper bounds are certified:

| j | ||D^j(W1 F_009)||_2 | ||D^j(W2 F_009)||_2 |
|---:|---:|---:|
| 0 | 2.954172025376e-8 | 2.953021642675e-8 |
| 1 | 4.448606804475e-6 | 4.446237457149e-6 |
| 2 | 6.012662370960e-4 | 6.010371854681e-4 |
| 3 | 1.222369836935e-1 | 1.222148783019e-1 |

The [origin result](../research/reference_b14s_origin/RESULT_PROOF.md) also gives containing lowers, local integer energies and complete analytic errors. It constructs the full nonlinear source from the exact base and correction, integrates the retained polynomial exactly, and bounds every omitted term. A separate 2048-bit calculation recomputes the disk integrals and checks endpoint directions. The theory auditor independently confirmed the two applications and their publication. These are local integrals; they are not whole-plane H^3 bounds.

For r>=10,000, the [complete signed exterior calculation](../research/reference_b14s_source/TAIL_RESULT_PROOF.md) proves

    0.00067824438670 < ||W1 F_009||_2 < 0.00067862501582,
    0.017286029316 < ||W2 F_009||_2 < 0.017293688771.

These intervals include the full infinite remainder. The proof retains all 76 source branches, 234 merged nonzero powers and every signed Fourier pair. It uses an analytic compactified integral, not sampled radial quadrature. In particular, the P-S2 tail alone is above 0.01. A P-S2 whole-plane source norm target below 0.01 is therefore impossible for this exact center, although that says nothing about another center or another sufficient criterion.

The complete P-S1 exterior derivative calculation gives the following uppers for

    [sum_(j=0)^m binom(m,j) ||D^j(W1 F_009)||_(L2(r>=10000))^2]^(1/2):

| m | Upper |
|---:|---:|
| 0 | 0.00067862501582 |
| 1 | 0.00849360179196 |
| 2 | 0.01199581272757 |
| 3 | 0.01468793288946 |

The [operator exterior proof and result](../research/exterior_operator_bound/RESULT_PROOF.md) retain every analytic remainder. A separate reconstruction checks the radial shifts, complete coefficient rows, errors and endpoint squares. These conservative bounds make a full P-S1 H^3 assembly possible once the missing annulus is supplied. Overlapping exteriors must never be added, and these integer derivative integrals must not be interpreted as fractional norms of sharply truncated functions.

The [finite background result](../research/reference_b14s_source/BACKGROUND_RESULT_PROOF.md) encloses the least eigenvalue of the registered background matrix at five exact points and both weights. All ten values lie above the origin cap c+1-21/10. At the recorded P-S2 off-axis point, this refutes the screen's claim of a value below that cap. It does not prove that no other point dips below it. The infimum over the plane is at most any point value, so a global lower bound requires the pending cover.

## Evaluation findings and their consequences

The audit identified missing tensor multiplicities in an early strong-norm evaluator, incomplete angular mode coverage in an early localization table, large cancellation near the origin, and unreliable direct residual evaluation in the far field. Each verdict applies to a frozen version and named claim. Later repaired diagnostics do not retroactively make the older computation valid.

N1 has withdrawn its noise-inflated P-S2 mesh value 0.0852 for 009 after replacing the far-field base evaluation with its sector representation. Its revised mesh value near 0.05779 agrees with N2's polar value near 0.05775. This resolves that reported discrepancy at the FLOAT level. It does not replace the analytic tail or a whole-plane certificate. Likewise, N2's repaired local origin energies agree with the certified disk values to roughly 0.235 to 0.455 percent, when matching the local integer-energy convention. Their domains differ. The [new finite comparison](../research/updated_strong_sampling_audit/RESULT_PROOF.md) confirms the ratios without assigning all remaining error to quadrature or the omitted disk.

The fractional-energy narrative also needed a notation repair. For 009 at P-S1, the saved plain second-derivative energy accounts for about 34.82 percent of the saved N_(21/10)^2. The fractionally weighted second-derivative contribution accounts for about 93.37 percent. Those are different quantities. The [independent accounting result](../research/fractional_component_labels/RESULT_PROOF.md) reconstructs both from the frozen records. This corrects the interpretation without refuting the numerical optimization direction.

At (alpha,delta,sigma)=(1/2,2/5,7/4), the latest strong-norm records give:

| Center | Sampled sum | Interpolation formula using grid maxima |
|---|---:|---:|
| 007 | 110.69043 | 157.16118 |
| 009 | 0.03173080 | 0.03642828 |
| 011 | 0.02323438 | 0.02781588 |
| 012 | 0.01155335 | 0.01387824 |

These are FLOAT diagnostics, not a containing interval. The independent check confirms the arithmetic for all twenty saved parameter records. Filtering out pairs separated by fewer than eight grid steps reduces the sampled set; it supplies no certified node error. With node errors epsilon_x and epsilon_y, a rigorous sampled lower must subtract (epsilon_x+epsilon_y)/|x-y|^theta. An interpolation upper needs global derivative uppers, rather than grid maxima. A flagged short pair could reflect a node error or an unresolved derivative peak. The [sampling proof](../research/updated_strong_sampling_audit/PROOF.md) makes these distinctions explicit.

The newer 010, 011 and 012 candidates are promising numerical inputs. Their FLOAT improvements do not authorize reusing the 009 source certificate. The coordinator's current decision keeps 009 in the running chain through the next allocation review. No certificate for those newer candidates is claimed in this report.

## Pending chain and the next decisive evidence

The disk and exterior leave the finite annulus 1/50<=r<=10,000. The full planner uses 114 panels, the original polynomial majorant and an order cap of 2048. At the latest saved log entry used here, 62 panels had completed by 08:33:35Z. The primary Taylor calculation and its independent reducer have not started. Their production runtime and conditioning are unmeasured; the order-eight benchmark is not a completion-time guarantee.

The exact compact representation has already been checked independently: 706,920 rational coefficient slots agree with a separate reconstruction, and finite order-eight jets agree with the older evaluator. The table is compressed to stay within the agent's disk limit. A first uncompressed attempt exceeded the storage threshold and was stopped; its failed execution and retirement record are retained. The [compact-table result](../research/compact_radial_jets/RESULT_PROOF.md) documents what passed. The [geometry comparison](../research/scheduling_comparison/RESULT_PROOF.md) explains why the current six-panel-per-doubling policy is retained: it is favored by the linear work score, while a different policy is favored by a quadratic score and would require another full plan.

After a successful annulus and independent reduction, the prepared assembly will sum disjoint regional integer energies for the identical source and weight. The whole-plane identity H_m^2=sum_(j=0)^m binom(m,j)e_j then supplies H^2 and H^3 bounds. Log convexity gives N_(21/10)<=H_2^(9/10)H_3^(1/10). This is a bound on the full smooth field, not a sum of regional fractional norms. The independently reviewed rational-division method will recover an unweighted L2 interval from the same P-S1 integrands. Both remain conditional on successful source computations.

A separate, independently reviewed multiplier m=sqrt((1+r^2)/(1+4r^2)) has ordered derivative bounds (1,3/5,17/4,20). Together with complete P-S1 energies, it gives a conservative unit-radius S_F(alpha,delta,1) upper when 0<alpha+delta<1, using only scalar postprocessing. [The transfer proof](../research/ps1_unit_weight_transfer/PROOF.md) has independent review AT618-620, with all nine bindings checked. It supplies neither sigma=7/4 nor a source-specific upper before the energy inputs exist.

The global cover follows the source chain and targets the background matrix, gradient and strain together. Tighter strain thresholds can be tested on the same containing leaf ranges. Further refinement cost is unknown. The exact target for gain at least 2 is s_*<=c-20/21, approximately 0.85793826; the rounded threshold 0.858 falls slightly short. None of these conditional gains proves a far-form bound or the invariant-ball inequality.

A theorem still requires compatible certified source norms, global background estimates, the full inverse and domain hypotheses, an explicit weak high-regularity bound, and the invariant-ball closure at one frozen center. The numerical audit will mark each new item only after its source-specific computation, complete remainder, independent reduction and endpoint checks pass.
