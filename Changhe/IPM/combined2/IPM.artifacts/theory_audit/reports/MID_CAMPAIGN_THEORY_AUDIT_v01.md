# Theory audit at the mid-campaign checkpoint

Recorded 2026-11-03T08:50:03Z, actual UTC, 14 hours, 44 minutes and 33 seconds after the logged start. This immutable snapshot is for the coordinator's next exchange. Later entries in [AUDIT_LEDGER.md](../AUDIT_LEDGER.md) govern subsequent results. The source bindings are in [the input manifest](mid_campaign_inputs_v01.json).

**No complete stationary IPM existence theorem has been certified.** The campaign has proved qualitative full regularity for the reference background and several conditional routes to a fixed point. It has also replaced some numerical diagnostics with complete regional certificates. For the active corrected center, three quantitative parts are still missing: complete source bounds, a global background cover, and a same-background weak energy coefficient small enough for the invariant-ball test. A small sampled residual does not supply any of these by itself.

## What is proved about the full inverse

The fixed parameter and authoritative reference remain

    c = 4076476460239181 / 2251799813685248,
    SHA256(007) = ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21.

For a real scalar, S1 means even in x and odd in y. Write J=(1-Delta)^(1/2), W=(1+|X|^2/r0^2)^(sigma/2), and N_q(h)=||J^q(Wh)||_2. The new [full O1 theorem](../research/o1_full_inverse_audit/PROOF.md), AT031, uses the actual variable-coefficient operator, its weighted semigroup and graph core, and the imported full L2 inverse. Its assumptions include all-order background decay, 2<q<3, sigma<1+gamma, a positive signed L2 rate, and a positive global principal-matrix margin. Under those assumptions it proves weighted Hq regularity of the unique L2 solution and a weighted C^(1,alpha) estimate for 0<alpha<=q-2. The weak remainder constant is finite but unpriced.

Complete background certificates activate this theorem for unchanged Candidate 007 at four tuples. The [restricted Sobolev O2 theorem](../research/restricted_sobolev_inverse/PROOF.md), AT058, also supplies a uniform full inverse on a nonzero symbolic small ball at these tuples.

| Tuple | q | sigma | r0 | Certified matrix margin | Maximum alpha | Audit |
|---|---:|---:|---:|---:|---:|---|
| P-BG1 | 13/5 | 7/5 | 1/4 | 1/10 | 3/5 | AT056, AT058 |
| P-BG2 | 5/2 | 7/5 | 1/2 | 1/4 | 1/2 | AT074 |
| P-BG3, also P-S1 | 21/10 | 1 | 1/2 | 3/5 | 1/10 | AT097 |
| P-BG4, also P-S2 | 21/10 | 7/5 | 1 | 3/5 | 1/10 | AT172 |

These are qualitative full-operator results. They do not give numerical inverse constants, a full arbitrary Holder-ball O2 theorem, or invariance of one of the balls needed for a fixed point. They apply to 007. A changed center needs its own hypotheses. The frozen-origin references retain their strict condition delta>alpha/(2c-2) and all their other restrictions whenever they are invoked. The Sobolev route does not weaken those restrictions.

## The precise conditional route at the corrected center

For the following closure route fix P-S1: q=21/10, sigma=1 and r0=1/2. The active certification center is C2-N1-009, with correction hash

    a04eb34fb51df70756faf2761bd9d6ab332566cbe3d361c92e70746f38c6b48c.

Its elementary representation has hash 1784016e1a8796587eecaa12b4e9c2d8193f218f39bb42b2b94d385892bbddf8. Let U=(-R1 R2,R1^2), where Rj has Fourier symbol i xi_j/|xi|, and let L_rho h=(cX+U[rho]).grad h-h+U[h].grad rho. Define ell(h) as partial_y U2[h] at X=0, and a_0*=partial_y rho_*(0). Write rho_*=rho_007+h_* and

    F_* = F_007 + L_007 h_* + U[h_*].grad h_*.

The [re-centering framework](../research/recenter_framework_audit/PROOF.md), AT123, and exact class results AT162, AT386 and AT387 establish the normalized correction class, all-order qualitative decay, old graph-domain membership, and the source's weighted membership. Here ell(h_*)=0, and

    10.297317139577998823917123 < a_0*
                              < 10.297317139577998823917126.

The source is nonzero by its separately certified leading coefficient. Weighted membership alone would not prove that fact. The exact origin conditions imply F_*,y(0)=0; they do not certify a global matrix margin.

The [G2 bridge and Lemma KB](../research/kball_margin_audit/PROOF.md), AT598-600, reduce the remaining inverse prerequisites to concrete bounds, while retaining the full R1/R2 coefficient class and domains for every h_*+k. A certified ||grad h_*||_infinity<=1/4 and the reference rate beta_0>2.00215453 would give a new full L2 rate beta_0*>7/4. A certified global background matrix margin beta_*>=3/5, together with a certified source upper f<=2.8476e-6, permits the fixed reference ball

    Rbar = 1017/625000000 = 2.8476e-6/(7/4),   Mbar = 1/2.

On that ball KB bounds the additional matrix loss strictly below 0.150314. Thus beta_K>0.449686. This supplies the qualitative weighted inverse part of the bridge once its stated source and cover premises are verified. It does not supply a numerical weak coefficient. The cover with beta_*=3/5 supports this reduction only for H4 rates at most 3/5; higher-rate budget rows require a stronger background margin. Nor does equality with a matrix margin itself provide a finite weak coefficient at the endpoint rate.

The [all-quadratic perturbation theorem](../research/ceps_v02_integration/PROOF.md), its [general-weight version](../research/general_weight_hfq_audit/PROOF.md), and the admitted P-S1 graph comparison give the following direct scalar test. The reference ball must contain the normalized trial ball, and the full inverse must already have qualitative weighted membership. For one chosen b0>0, an H4 certificate must establish

    Re <J^q(W L_* h), J^q(Wh)> <= -b0 N_q(h)^2 + C0 ||h||_2^2

for the actual same-background operator and every real S1 test in its stated core, with a finite C0>=0. These tests are not restricted by ell(h)=0. The accepted domain argument extends the form to the required graph domain. If f>=||F_*||_2, n>=N_q(F_*), R=f/beta_0*, M>0, and an admitted graph bound K is chosen, put b=b0-L(R,K), where L is the exact perturbation loss in the [scalar budget proof](../research/x5_budget_audit/PROOF.md). The sufficient condition is

    b > 0,                 C0 R^2 <= M(b M-n).

Together with the inverse, normalization and compactness assumptions, this gives a self-map and the imported fixed-point consequence. A selected positive lower D for M(b M-n)/R^2 is a sufficient allowable C0. It is not the globally optimal cutoff, and failure of a search for D is not an exclusion.

## Completed source certificates and the remaining ledger

The numerical auditor's [mid-campaign report](../../numerical_audit/reports/MID_CAMPAIGN_AUDIT_v01.md) records the exact source calculations and their independent reductions. This audit has confirmed the 009 disk applications for both weights and the complete P-S1 exterior application. For W1=sqrt(1+4r^2), the [independently directed local integer-energy uppers](../research/source009_origin_application/RESULT_PROOF.md) on r<=1/50 are

    [2.954172025375e-8, 4.448704891769e-6,
     0.0006012991509633, 0.1222414201696].

The index m in these arrays denotes the square root of sum_(j=0)^m binom(m,j) times the regional integral of |D^j(W1 F_*)|^2. It does not denote only the pure derivative norm. The corresponding complete exterior uppers on r>=10000 are

    [0.00067862501582, 0.00849360179196,
     0.01199581272757, 0.01468793288946].

These are complete regional bounds with analytic remainders, not norms of sharply truncated functions. The missing annulus prevents whole-plane assembly. At 2026-11-03T08:49:31Z the original planner had completed 81 of 114 panels. Planning is not the energy computation, and production runtime has not been established by the small-order benchmark.

| Requirement | Present status | What must still be supplied |
|---|---|---|
| G1: actual ||F_*||_2 and N_(21/10)(F_*) | OPEN; disk and exterior inputs complete | Complete finite annulus, independent reduction and disjoint whole-plane assembly |
| G2: exact correction class and normalization | CONFIRMED for 009 | Preserve its source identity in each application |
| G2: gradient, global matrix and strain bounds | OPEN | Complete global cover; no sampled supremum is substituted |
| G2: reference-ball margin | CONFIRMED conditional method | Certified radius and global margin satisfying KB |
| G3: finite admissible C0 in H4 | OPEN | Same-center continuum energy certificate at the chosen rate, then a passing scalar test |
| Original strong norm S_F | Conditional transfer proved; actual endpoint OPEN | Complete energy supplier and audited rational postprocessing |
| Stationary existence and any smooth bootstrap | OPEN | All required premises simultaneously, at one unchanged center and parameter tuple |

The new [unit-radius strong-norm transfer](../research/ps1_unit_transfer_audit/PROOF.md) and [application audit](../research/unit_application_audit/PROOF.md), AT618-620 and AT635-637, convert complete P-S1 H3 energy bounds to S_F(alpha,delta,1) for 0<alpha+delta<1. The multiplier derivative bounds are (1,3/5,17/4,20). Exact root-power and input-binding checks are complete. No actual S_F upper has yet followed, and this transfer does not supply sigma=7/4 or the missing H4 coefficient.

## What the exclusions and diagnostics establish

Several sufficient criteria at unchanged 007 fail with certified inputs. The registered earlier b7 centers also fail specific source ceilings. These conclusions concern named criteria, sources and tuples. They do not prove nonexistence of a stationary solution, and they do not exclude all possible weak energy estimates.

The current near/far work makes that distinction particularly important. The accepted TII-0 lower concerns the sum of prices in one construction. The universal oscillation constant is sharp, but that does not give a lower for the actual 009 coefficient. The corrected SC-LB theorem uses the even-even part of the coefficient for S1 tests. A finite periodic eigenvalue is not a continuum certificate. Increasing the continuum frequency band approaches the full form supremum, which can exceed the high-frequency floor SC. Separate closeness of two coefficient norms is also insufficient to transfer an operator bound between 007 and 009. These restrictions are proved or refuted by explicit arguments in AT451-452, AT544-554, AT609-614 and AT621-623.

The frozen T2_FAR_v01 table calculations have been independently reproduced at their stipulated inputs, AT615-617 and AT624-627. Their far constants remain FLOAT and their near prices remain HEURISTIC. No continuum all-rate exclusion follows. A usable far certificate would need complete coefficient and Fourier-moment uppers, compatible strain, and the same-background near and remaining weak terms. The resulting admissible C0 must then be compared with D, not merely with a necessary upper U.

The [X5 and 012 budget audit](../research/x5_budget_audit/PROOF.md), AT628-634, confirms 216 positive sufficient cells and 72 necessary cells at their exact stipulated inputs. It corrects an upward forcing header and a claimed equivalence for a selected cutoff. Sufficient rows need upper source bounds; necessary rows need lower bounds and the stated inverse-rate upper. N2<=Nq permits transfer of a lower on N2, not an upper. The value .0161 is a stipulated input, not a certified rounding of a FLOAT .016107. Every new trial M is at most .495, so the reference radius 1/2 still contains those witnesses.

## Immediate continuation and audit provenance

The coordinator retains the 009 certificate chain through X5 and has designated 012 as the next candidate for that decision. The audit priority is unchanged: inspect actual G1 records as soon as they appear, then the global cover and any proposed complete H4 bound. A new freeze must retain the exact input hashes. The forthcoming theory_v09 and ledger should incorporate the sufficient-cutoff correction, the latest radius bounds, and the distinction between completed applications and conditional methods. The completed THEORY_NEW_RESULTS version 8 integration is AT638-639; its four new analytic entries retain the accepted premises.

All results have standalone informal proofs and named evidence in the [reading-order index](../research/README.md). Verification uses local exact rational or Arb calculations and frozen inputs; no Lean or Lake build has been run. Failed checker and preparation receipts remain in their topic folders. Collaboration continues through the existing theory and coordinator agents configured as the main model. The actual provider response model identity has not been inspected. No outside model client, server, JavaScript tool, cluster workload, or online posting was used for this audit snapshot.
