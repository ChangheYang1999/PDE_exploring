# Generic physical-radius unit-ball refinement

Prepared before execution of the generic v3 scripts. The numerical algorithm and12/24/48-node refinement are unchanged from qualified v2. V3 accepts a completed independent holdout report and a new output path, retains the input identity, and records its own base report and source hashes. The corresponding auditor accepts the new report and compares against its own base report. It recomputes the same momentum, vorticity, positive-volume moments and pressure differences from saved arrays.

Qualify the generic auditor against the already-completed S01 v2 report before use. Compare the AST of all helper functions, and verify that changes in the evaluator main function are confined to arguments, completed-input validation and metadata. No tolerance, radial panel, angular grid, pressure rule or field formula is changed. Keep the patch and source hashes.

Next input: the exact S09 d6w field in artifacts/holdout_S09_v6_cpu.json, once complete and audited. Use the same physical unit ball, panels beginning at zero and r_core/32 and then doubling to1;12,24,48 Gauss nodes in each panel;48-by-96 angles at phase.293; pressure radial/angular rules16/48 and24/64 at phase.677. Evaluate U, DU, Omega, DOmega, stable linear terms and pressure synthesis in long double; source projection stays binary64. Preserve all three rules even if they agree. Report the observed changes and all unresolved numerical limitations. No continuum error enclosure, Tier acceptance or exact Euler result follows.

Run on CPU35, one busy computation, CUDA_VISIBLE_DEVICES empty. Start only if total projected side use remains under9.5GiB and the filesystem has at least20GiB free. Do not alter the inherited queue's bound sources.
