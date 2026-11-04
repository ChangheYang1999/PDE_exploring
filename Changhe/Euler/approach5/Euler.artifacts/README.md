# Accompanying artifacts: nonexistence of decaying rotating self-similar Euler profiles

These files accompany the report Euler.report.md, published beside this folder. The report is the primary deliverable; its opening summary states what is proved, what is conditional and what remains open.

## Problem

Rotating self-similar profiles of the three-dimensional incompressible Euler equations are pairs (U, P) on R^3 with

    (1 - c)U + [(cI - omega J)y + U].grad U + omega J U + grad P = 0,    div U = 0,

where J(y1, y2, y3) = (-y2, y1, 0), c = c_l > 0 is the similarity exponent and omega is the logarithmic rotation rate, together with the boundary condition U(y) -> 0 as abs(y) -> infinity. The conjecture studied is that for 2/5 < c < 1/2 and every real omega, every smooth divergence-free decaying solution is U = 0. Its status at the end of the run is UNRESOLVED; the report gives the proved partial results (an energy law for every omega, nonexistence for 0 < c < 2/5 and for omega = 0, structure theorems and, at C-infinity regularity, a coverage theorem for a hypothetical nonzero profile) and conditional nonexistence theorems for 2/5 <= c < 1/2 and every omega.

## Contents

- LITERATURE_REVIEW.md: precise statements of the relevant existing theorems (Constantin, Ignatova and Vicol; Pineau and Vicol; Chae and Shvydkoy; Chae's Liouville theorems; related results), their assumptions and their applicability to rotating profiles.
- PREPRINT_AUDIT.md: the independent audit of the Liu preprint (Zenodo record 23461703), in two parts: the audit of the literature and counterexample agent and the separate audit of the auditor.
- EXACT_IDENTITIES.md: checked derivations of the profile equation, the pressure Poisson equation, the vorticity equation, the rotating Bernoulli identity, the circulation formula, the energy identities and the Fourier system.
- THEOREM_ATTEMPTS.md: proof attempts, including the unsuccessful ones, with the exact steps that fail.
- COUNTEREXAMPLE_AUDIT.md: explicit examples, candidate counterexamples and tests of proposed inequalities.
- PROOF_OBSTRUCTIONS.md: a prioritized record of the unresolved obstacles.
- AUDIT_LEDGER.md: the auditor's ledger, verdicts A001-A3270, with the claim, method and verdict (CONFIRMED, REFUTED or OPEN) of each. Verdict numbers in the report refer to this ledger. Claim numbers C (theory agents A and C), B (theory agent B), LIT (literature agent) and CO (coordinator) are the identifiers of the claims it audits.
- scripts/: symbolic checks, exact-arithmetic spot checks, numerical diagnostics and SHA256SUMS.
- auditor_proofs/: the auditor's written proofs and reviews (928 files in the subfolders proofs and reviews). The ledger cites their paths relative to this folder; the report identifies the corresponding proofs in the accompanying artifacts by verdict number.

References to "the team records" in these files point to other working files of the run (agents' proof files, comparison notes, referee answers) that are not published; the verdicts based on them are recorded in AUDIT_LEDGER.md. Entries of the ledger and of the agents' files are historical records written during the run: a statement there carries the scope and verdict stated with it, and later verdicts may supersede earlier ones. The report gives the final state.

## References

- A. P. Constantin, M. Ignatova, V. Vicol, On putative self-similarity for incompressible 3D Euler, arXiv:2602.17570 (2026).
- B. M. Pineau, V. Vicol, On rotated backwards self-similar solutions of the incompressible 3D Navier-Stokes equations, arXiv:2607.09619 (2026).
- C. D. Chae, R. Shvydkoy, On formation of a locally self-similar collapse in the incompressible Euler equations, arXiv:1201.6009.
- D. D. Z. Liu, A Liouville theorem below the half-scaling exponent for three-dimensional Euler profiles, Zenodo record 23461703 (2026).
- Further literature, including the Liouville theorems of D. Chae, is cited with exact statements in LITERATURE_REVIEW.md.

## Reproducing the checks

Requirements: Python 3 with sympy (and mpmath, which sympy installs). No GPU, network or other data is needed. Run from this folder:

    cd scripts
    sha256sum -c SHA256SUMS
    python3 verify_identities.py
    python3 verify_identities2.py
    python3 check_c2_local_family.py
    python3 check_gamma_kinematic.py
    python3 check_helicity_sign_basin.py
    python3 check_vortical_horseshoe.py
    python3 check_local_saddle_model.py
    python3 check_abstract_cex.py
    python3 check_prong_meridian.py
    python3 check_lit150.py
    python3 check_jet.py

Pass criterion: exit status 0, no failed checks, and a last line "ALL PASS", except for the following output conventions: check_c2_local_family.py ends with "all identities hold"; check_jet.py ends with "PASS: all seven exact endpoint-jet checks."; check_lit150.py prints the expected flux exponents [5 - 4/c, 5 - 6/c, 5 - 4/c], energy coefficient 1 - 5*c/2 and final cancellation tr(DU A) + omega tr(J DU) = 0. Its other nonzero output values are displayed algebraic quantities, not failed residuals. Exit status alone is insufficient because some scripts print a failure without setting a nonzero exit status. Part 1 of verify_identities.py uses a high-precision numerical residual tolerance, and the parameter grid in check_abstract_cex.py is numerical. The evaluations in check_helicity_sign_basin.py are exact-arithmetic spot checks at selected points. These finite tests do not prove identities for arbitrary inputs. All eleven scripts passed in the final check of the run, each in under one minute on one core. What each script checks:

- verify_identities.py, verify_identities2.py: numerical spot checks of the rotating change of variables and symbolic checks of the vorticity, Bernoulli, circulation and related identities for generic smooth fields (EXACT_IDENTITIES.md).
- check_c2_local_family.py: the explicit nondecaying C^2 family of exact profiles used in report section 3 (it satisfies the equation but not decay).
- check_gamma_kinematic.py: bracket identities of the kinematic example of report Appendix B.
- check_helicity_sign_basin.py: the local saddle model and the formal tail field with sign-changing helicity (report Appendix B).
- check_vortical_horseshoe.py: the explicit formulas of the vortical horseshoe example (report Appendix B).
- check_local_saddle_model.py: the local saddle model with a periodic orbit of zero circulation (THEOREM_ATTEMPTS.md).
- check_abstract_cex.py: the parameter algebra of the abstract kinematic bracket example (PROOF_OBSTRUCTIONS.md).
- check_prong_meridian.py: the prong-slope filling of the punctured cat-map bundle used in a topological proof attempt (THEOREM_ATTEMPTS.md).
- check_lit150.py: the algebraic steps of the axis-pressure argument for a pure-swirl tail (THEOREM_ATTEMPTS.md).
- check_jet.py: exact finite-jet checks of a bounded-endpoint tail germ (AUDIT_LEDGER.md); it is not an existence proof for an Euler germ.

These are checks of identities and local models. None of them is a nonexistence proof. The full coefficient inputs for the rational vorticity-threshold certificates are not included: their audit descriptions are in AUDIT_LEDGER.md and the associated proof reviews, and the commands above do not reproduce those certificates. The supplied scripts do not search for full Euler profiles.
