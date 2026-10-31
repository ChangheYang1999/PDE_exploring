# Independent segment-three sensitivity results

Recorded 2026-10-29T17:49:58.202503+00:00. V395 and V396 confirm the numerical table and incomplete labels of the two complete-Jacobian segment-three endpoint records. The independent calculation uses the qualified Householder/SVD implementation, with four coefficient cutoffs and explicit gauge handling. Evidence: ../../../artifacts/segment3_sensitivity_v1/audit.json (f70ea653f390df34f9b7dd108eb88e92ca829c5fdc31e54f9f399be425d545a3); ../../../artifacts/segment3_progress_v1/audit.json (2b942d4ad5d81b3841c44cebc243c9fb855a6686a18f7a59db6f3f0a0f654cb2).

| Quantity | P1 FREE, 409 | P2 FREE, 466 |
|---|---:|---:|
| eta(1e-8) | 0.829025489 | 0.588214160 |
| Q-complement share | 0.168569336 | 0.393508758 |
| Complete scaled gradient / residual norm | 0.034642583 | 0.044587619 |
| c_l unabsorbed fraction | 5.557768446e-6 | 5.307919650e-6 |
| omega unabsorbed fraction | 2.420309814e-4 | 3.112270161e-4 |
| Reduced predicted relative decrease | 0.134521421 | 0.057546618 |
| Last-50-transition relative decrease | 0.017525849 | 0.040060935 |

Both states fail stationarity conditions (a), (b) and (d). Both parameter directions at both states meet the <1e-3 warning predicate. The P1 reduced c_l step lies outside the admissible interval. These are finite-dimensional statements about the saved linearized problem and saved objectives. They establish neither a stationary nonlinear branch nor exact numerical rank nor an Euler solution. Curvature widths and checkpoint/QR-summary endpoint binding are separate audits.
