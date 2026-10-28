# Clarifications after the independent audit

Date: 2026-10-28T14:26:52.653034+00:00. The bound proof SHA256 is unchanged.

At a boundary t0, write the radial transport coefficient as q(t,theta)=q(t0,theta)+(t-t0)Q(t,theta), with Q in W^(6,infinity) locally. For the i=6 column, the function (t-t0)b_6'(t) has its first jump in derivative6, so it is locally H^6. Multiplication by Q preserves H^6. The remaining b-times-coefficient terms and q b_7' are also H^6; the coefficients are W^(7,infinity) by proof 126. The leading term q(t0,theta)b_6'(t)F(theta) has a nonzero fifth-derivative jump on an open angular interval and is not H^(11/2). These facts justify the no-cancellation argument. Merely saying the other terms are C5 would not by itself justify it.

The computation's check.json records the proof revision before the exact-result paragraph was added. final_certificate.json binds the final PROOF.md, check.json and check.py. No computed data changed between those proof revisions.

The 66-column subspace is the high INPUT subspace; the 60-column subspace is the OPERATOR GRAPH subspace. The theorem classifies exactly the 78 pure columns, and no other columns. The audit's phrase “169-column S1M4P” is a naming slip: S1M4P is the 78-column pure run. The 169-column jet-joined section is a separate section. Its q=3 endpoint joins guarantee C3, not C6. This naming slip does not affect any proof or calculation in the audit.
