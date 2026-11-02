# frr1 equilibrium review

Prepared at 2026-10-31T22:20:47.936610+00:00. Verdict: CONFIRMED for the recorded ten-policy standard-start W/D/L matrix with a zero diagonal imposed by convention.

Read in this order:

1. [PROOF.md](PROOF.md): exact hypotheses, complete equilibrium set, primal and dual certificates, necessity and scope.
2. [Independent review](../../reviews/frr1-equilibrium-review-001.md): report wording, recorded-data checks and publication qualification.
3. [Audit receipt](verification/independent_audit_001.json): complete specifications, matrix, source pins, 90 log hashes and exact rational certificates.
4. [Reviewed input excerpts](verification/review_input_excerpts_001.json): exact report proposition, dated lead entry, queue log and supporting analysis-source bytes.
5. [Offline checker](verification/check_frr1_matrix.py): standard-library JSON/source audit and rational arithmetic; no policy or game imports.

The checker requires execution from the project root and a new receipt filename under this topic's `verification/` directory. Use the project Python with `-B`, `PYTHONDONTWRITEBYTECODE=1`, project `bot_research/tmp` as `TMPDIR`, the assigned CPU affinity and one thread. Its only write is the explicitly named receipt. No rerun was used as a new game observation.
