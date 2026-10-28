# Binding clarifications after the independent audit

Recorded 2026-10-28T16:41:33.870208+00:00. Read this file together with the unchanged PROOF.md. The actual model was a separate model instance in the theory author team. Its complete audit is copied in evidence/opus_audit.md. The verifier read it in full and independently checked every remark. No numerical computation was run for this review.

1. The parameter window is exactly 2k-1<beta<k. In the historical derivation manifest, the letter p in "strictp<beta<k" meant 2k-1, not the source abscissa P=(p,0). The corrected scope is recorded in audit_record.json; the original derivation record is retained.

2. Global flow boxes in the uniqueness proof are C1. Global C1 and Lipschitz regularity of V suffices. Pull the weak equation back in such a box, apply the one-dimensional distributional fundamental theorem for almost every transverse parameter, and use continuity to recover every trajectory. Proof 223, clarification4, gives this precise argument. No globally smooth field is assumed across the radial joins.

3. The bound |h(X)|<=C||h||Z |X|^beta is a direct consequence of the target norm definitions in topics228 and236. For the actual field V, the radial flow comparison r_t comparable to exp(ell t) follows from proof 223(3)-(4), or from the integrable error argument in the present proof. It uses both comparisons when beta is negative. Proof 228's time-changed flow is not being substituted for the actual V flow.

4. Choose the conjugacy chart and the cutoff support strictly inside the certified analytic disk of radius1/1000 about P in proof 209. Then V and the local chart are smooth throughout this construction, and f_phi is smooth. Reflection to -P commutes with transport because V1 is odd in x and V2 is even in x. Reflection across y=0 uses the chart equivariance stated in the proof. Since the cutoff derivative is supported away from the cusp point and phi is supported in the two intervals away from zero, f_phi has compact support separated from both physical axes. Both target and maximal transport-domain membership follow.

5. The weak-derivative assertion may also be checked by removing a disk of radius epsilon about the conjugated source. The cusp is bounded and smooth off that point, and its classical gradient is locally integrable by the displayed estimates. The integration-by-parts cutoff error is bounded by C epsilon sup|u_phi| and tends to zero. Thus the classical and weak derivatives agree; no point distribution or interface measure occurs. This verifies the exact homogeneous equation before the compact cutoff is applied.

6. The actual strict inequality b<a follows from the certified mu_s<1, despite its small margin. It is used to prove the sharp positive assertion u_phi in C^a through the bounded y derivative. The obstruction at alpha>a uses the exact homogeneous equation, continuity, local weak derivatives and the two-point quotient. The theorem here retains all actual source hypotheses; no extension to other source spectra is asserted.

7. Traceability now includes topics15,52,60,223 and all clarification files relevant to the use of209,228 and236. Existing hashes in derivation.json are rechecked. The exact source constants and source conjugacy remain previously verified inputs, not new certificates from this review.

Verdict: CONFIRMED for transport alone on the stated maximal domains in Z2 and Z3, for 1/A_s<alpha<1, 2k-1<beta<k and gamma>4k. The algebraic cokernel is infinite-dimensional, with smooth compact physical-parity representatives having exact c=J=0. Neither closed range nor a bounded quotient projection is assumed. The full coupled operators, the actual residual's range, alpha<=1/A_s and profile existence are outside this conclusion.
