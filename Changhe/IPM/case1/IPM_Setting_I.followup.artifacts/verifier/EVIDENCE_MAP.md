# Evidence map for the requested verifier checks

Recorded 2026-10-21T00:42:14.832939+00:00. This is a reading guide to existing results, not a new proof or numerical audit. Begin with [the final findings](FINAL_VERIFIER_FINDINGS.md); the report contains the dated verification timeline. Each topic proof states its hypotheses and dependencies; its code and verification files are adjacent. [INDEX.md](INDEX.md) gives all87topics in reading order.

| Requested check | Evidence entry | Scope of the recorded verdict |
|---|---|---|
| Independent full-plane inverse and manufactured fields | [inverse/PROOF.md](inverse/PROOF.md) | CONFIRMED formula under its hypotheses; numerical interior quadrature remains an approximation. |
| Parity, center velocity, normalization, transport and elliptic residuals | [fifth-grid/RESULTS.md](fifth-grid/RESULTS.md) | CONFIRMED for the fixed108 field in AV150. This is a worked recent audit, not the only candidate checked. |
| Exact center regularity | [center-regularity/PROOF.md](center-regularity/PROOF.md) | CONFIRMED necessary compatibility test. Fixed represented fields fail it; this does not exclude smooth limits. |
| Canonical center identity, first rigorous method | [center-moment/PROOF.md](center-moment/PROOF.md) | CONFIRMED exact represented-field interval computations with stated input contract. |
| Canonical center identity, second rigorous method | [center-moment-trapezoid/PROOF.md](center-moment-trapezoid/PROOF.md) | CONFIRMED separately justified radial and angular formula with rigorous error bound. |
| Harmonic gauge and distant omitted tail | [exterior-tail/PROOF.md](exterior-tail/PROOF.md) | CONFIRMED exact tail bounds under the stated field hypotheses. No free harmonic strain is permitted by the canonical law. |
| Finite-region artifacts | [compact-extension/PROOF.md](compact-extension/PROOF.md) | CONFIRMED exact canonical manufactured construction solving transport on any prescribed bounded region but failing elsewhere. |
| Zero and polynomial limits | [compactness/PROOF.md](compactness/PROOF.md) | CONFIRMED counterexamples and additional uniform-tail condition. Fixed normalization alone does not give compactness. |
| Physical residuals across domains | [domain-states/PROOF.md](domain-states/PROOF.md) | CONFIRMED finite diagnostics for L=4 and L=16, compared with L=8. No continuum residual enclosure. |
| Physical residuals across resolutions | [five-grid-comparison/RESULTS.md](five-grid-comparison/RESULTS.md) | CONFIRMED AV153 common58-point five-state comparison. Neither maxima nor RMS establish convergence. |
| Independent correction attempts | [fixed-cl-correction/PROOF.md](fixed-cl-correction/PROOF.md) | CONFIRMED finite corrections with withheld tests. No branch or solution construction. |
| Kernel, conditioning and isolation | [sampled-physical-actions/PROOF.md](sampled-physical-actions/PROOF.md) | Finite actions CONFIRMED within their stated norms and error limits. Continuum kernel and Q1 remain OPEN. |
| Analytic claims in lead and numerical reports | [report-audits/PROOF.md](report-audits/PROOF.md) | Use the dated AV entries for the exact report bytes and repairs. Final accepted report hashes are in AV148/155/157. |
| All smooth axis traces versus joint regularity | [noncompact-packet-all-traces/PROOF.md](noncompact-packet-all-traces/PROOF.md) | CONFIRMED explicit frozen-packet result, AV156, using AV152/154. No coupled-profile conclusion. |

The actual ending is recorded in [END_OF_RUN.md](../END_OF_RUN.md) after it occurs. The final frozen-file entrypoint is [artifacts/CATALOG.json](../artifacts/CATALOG.json). Archived bytes preserve the audit record; they do not certify the PDE claims. No additional work is implied by this index.
