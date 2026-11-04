# Audit of the 00:21 report delta

Status: the energy and jet transfers are CONFIRMED at their exact scopes. Cumulative approval is pending the two source-precision edits in Section 4. The global arbitrary-helicity conjecture remains OPEN.

## 1. Snapshot, hypotheses and reading boundary

The report snapshot is in the team records, SHA256 8155336d96f6d956fb2ebe36142d27caab8f8fe5c016844e604e6cd6b80877ce, 1016462 bytes. Its declared audit cutoff is A2629. All seven complete changed blocks relative to the 47ecb24d snapshot were read, including the full B67 row. The earlier eight-block delta from the approved 4936b8a2 snapshot is audited in auditor_proofs/reviews/assembled_report_20261104_0016/PROOF.md, relative to this agent root. Only the front, main text and Appendix A are in the cumulative approval boundary. Historical Appendix B and future edits are outside it.

## 2. Energy references

The changes add A2619-A2621 to the energy summary and Theorem 1 header, and A2619 to the pressure-normalization hypothesis entry. The standalone reconstruction auditor_proofs/reviews/energy_foundation_20261104/PROOF.md checks the C1 canonical-pressure argument, the energy trichotomy, and the critical exterior estimate. The report retains C1 velocity and pressure, bounded velocity and distributional decay under dilation for that theorem. It does not use the new audit to infer vanishing in the open supercritical range.

The citations are correct for Theorem 1 and Proposition 2.7. The phrase rechecked in full in the Theorem 1 header refers to that theorem. A2619-A2621 do not independently recheck every embedded weak extension or every endpoint corollary in Section 2A; those keep their earlier audit dependencies. No foundation proof was changed in this delta.

## 3. Reduced example and full scalar quadratic jet

The reduced analytic construction and its first jets are verified in auditor_proofs/reviews/reduced_system_nonzero_curl_jet_20261103/PROOF.md, A2623-A2626. The report correctly names c=3/7 and omega=0, keeps the missing equation W.grad S=0 explicit, and makes no actual-tail counterexample claim. The precise expansion is

    (W.grad S)(1,0,z)=5z^2+O(z^3) as z tends to zero,

and the reference point is w=(1,0,0). Thus the row's unqualified expression W.grad S=5z^2+O(z^3) should be anchored to this line. This is a precision correction to the report, not a gap in the source example or its failure of W.grad S=0.

The full-scalar necessary jet is verified in in the team records, A2627-A2629. It requires the local carrier and scalar transport identities, X.V=0 nearby, V=DV=S=0 at w and grad S(w) nonzero. In the specified oriented frame, with eta=(1-2c)/(2(1-c)), it is

    Q=K[(x^2-(1-eta)y^2)e1-2xy e2],
    DW(w)[h]=-2eta K y e3.

Hence DW(w)grad S(w)=0, and DW(w)=0 if and only if D2V(w)=0. For K nonzero the transverse zero is isolated with index -2 and the local flowbox zero set is the central orbit. The report transfers these as necessary local statements and leaves higher-order realization, pressure compatibility and the actual-tail DW question open. It does not claim the polynomial is a full solution.

## 4. Remaining changes before cumulative approval

The broad C69 Volterra-factor conclusion is now mathematically supplied by auditor_proofs/reviews/general_radial_completion_20261104/PROOF.md, A2643-A2645. That theorem covers every positive nondecreasing derivative-flat radial factor, without a bound on r f'/f or the condition r f'>=f. It concerns the specified Volterra construction, not every conceivable carrier with a radial factor. The current report still cites only A2615-A2616 for this broader clause; add the new verdict so the dependency is explicit.

The B67 row should write w=(1,0,0) and (W.grad S)(1,0,z)=5z^2+O(z^3). With these edits the two outstanding precision issues are removed. The old C65 phrase about what a full-F exclusion must use is supported only relative to the reduced premises named in that row; a clearer formulation is that those premises alone cannot exclude the sign and a stronger conclusion needs an additional property. This last wording suggestion does not overturn the scoped A2378 audit.

The changed history and status lines are bookkeeping, not an enlargement of mathematical scope. A new exact snapshot is needed for cumulative approval after the edits. No external computation, formal build or literature claim is part of this delta audit.
