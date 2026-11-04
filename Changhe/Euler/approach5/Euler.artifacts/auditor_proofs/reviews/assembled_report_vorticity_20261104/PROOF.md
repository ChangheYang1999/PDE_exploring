# Audit of the report's central-vorticity additions

Status: the exact delta and cumulative assembly are confirmed at the scope below. The original decaying-profile conjecture remains open.

## 1. Exact object and coverage

The candidate is the report assembled at 2026-11-04T02:16Z, SHA256 0f6b2f60eb16b5fdf47815d132c847c3000aa73823384d8f88ca22a72a79bb29, 1048944 bytes. Both coordinator copies agree at capture. The predecessor is 7febf8bd2efe617d2c253a8c26f2a11f96746523e4bb2ef588dc5a4b48b4e14a, approved by A2757 through A2754.

The independent diff has four hunks and agrees exactly, apart from file labels, with the coordinator's submitted diff. All four hunks were read, including every part of the 22959-byte third hunk. That hunk changes one Appendix A row and preserves its surrounding rows. The fourth hunk updates the historical revision log; that change was checked individually.

Cumulative approval concerns the front matter, sections 0-10 and Appendix A through the candidate's stated cutoff A2762. It does not collectively recertify the historical appendices. It does not certify changes made after the pinned snapshot.

## 2. Mathematical transfer

The summary now names A2757's correct predecessor, cutoff and scope, and explicitly states that the earlier approvals do not cover the literal method readings refuted in A2742-A2744. Those passages were repaired before A2757. This accurately records the audit chain.

Part (e) of the pressure-minimum row transfers A2758-A2759: every permitted unit vorticity direction is realized by a full linear profile with positive definite pressure Hessian. The statement concerns existence of a full linear profile with that direction; it does not prescribe its magnitude or restrict the construction to the horizontal example in part (d). The proof is the oriented-frame construction and exact positive minors in auditor_proofs/reviews/vorticity_angle_20261104/PROOF.md.

Part (f) transfers A2760. Its definitions of u, v, a, tau and h agree with the complete central matrix and Schur complement in auditor_proofs/reviews/vorticity_magnitude_20261104/PROOF.md. For a full local profile with U(0)=0, nonzero W and semidefinite pressure Hessian, the prior strict-angle argument first gives u>2, so a and all displayed denominators are legitimate. The second branch has R<2v^2 and hence v is nonzero. At R=2v^2 both formulas agree. The two-branch expression is exactly the minimum of |y|^2+|h-2vy| plus tau/2.

The converse permits the two free strain parameters and the Hessian to vary. Positive definite realizations exist exactly above the magnitude threshold. At equality the row correctly restricts singularity to semidefinite Hessians, avoiding the comparison error A2761. That error is separately labeled as a refuted comparison sentence and is not included in a confirmation list.

The row retains all application limits. The global zero conclusion uses c>0 and a neighborhood pressure minimum. The local inequalities use only a semidefinite Hessian and are valid for all real c. A semidefinite Hessian does not replace the neighborhood minimum in the zero-ball argument. All converse examples grow linearly. Neither a central zero nor a pressure condition is derived from decay. The original arbitrary-omega conjecture therefore remains open.

## 3. Structural evidence and conclusion

The local standard-library checks are file bookkeeping, not mathematical experiments. They parse all 2762 verdicts through the cutoff without an unknown or conflicting status. All 220 explicit confirmation lists refer only to confirmed verdicts, and all 2355 distinct positive verdict references exist. A0 remains the already inspected mathematical notation, not an audit number.

There are nine Markdown tables, with 580 data rows and 598 rows including headers and separators. No table-column mismatch, absolute local path or em dash occurs. The four blocks beginning with norm bars remain mathematical displays, not Markdown tables; the unchanged separator-based recognition handles them correctly.

The four-hunk transfer is valid. Together with A2757, it gives cumulative approval of the pinned front matter, main text and Appendix A through A2762. The candidate makes no unconditional nonexistence claim from the newly added local pressure hypotheses. No numerical evidence, formal build, server, new model client or external publication is used.
