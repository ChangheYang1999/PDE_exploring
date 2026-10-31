# Segment-three curvature-width replay

Claim: the reported physical curvature widths and their log-omega conversions are widths about the quadratic model minimizer.

Method: use the independently replayed V395 reduced systems, independently reconstruct physical column scaling from the bound complete factors, and check both 1% and 10% fractions. Compare current-point roots separately. Prove the logarithmic center rule in research/reduced_sensitivity/PROOF.md and test an exact positive-definite counterexample.

Result: all 110 controls pass. Physical curvature displacements and both current-point roots agree with the lead output within the inherited 1e-4 relative tolerance. Current-point log conversions agree. However, about_model_minimizer_halfwidth.d_log_omega uses the current omega as denominator. The actual quadratic minimizing omega is 1.52788460659 at P1 and 0.378483789176 at P2. The two log displacements must use these centers and are asymmetric. At 1% the values are:

| State | Direction | Absolute d c_l | Absolute d omega | Log displacement + | Log displacement - |
|---|---:|---:|---:|---:|---:|
| P1 | 0 | 0.0191101025 | 0.0241605501 | -0.015939433 | 0.0156893485 |
| P1 | 1 | 3.01696311e-06 | 0.0726639544 | 0.0464622525 | -0.0487266285 |
| P2 | 0 | 0.0159454459 | 0.00895261668 | 0.0233784786 | -0.023938142 |
| P2 | 1 | 3.75503352e-07 | 0.109847905 | 0.254821634 | -0.342816372 |

Here plus/minus follows the saved eigenvector orientation, not increasing/decreasing omega. Reversing the eigenvector exchanges the two values.

Verdict: CONFIRMED for physical curvature widths and the stated current-point roots. REFUTED for identifying the saved minimizer log conversions with log widths about the model minimum. OPEN for agreement with the nonlinear objective. P1's unconstrained minimizing c_l is outside the permitted interval, so these are model quantities rather than admissible updates. The exact counterexample uses S=diag(1/50,1/50), g=(0,-1/50), omega=1, reference objective1 and fraction1/100: the minimum is at omega2, giving log(3/2) and -log2, while the source reports log2 for the positive curvature displacement.

Evidence: artifacts/segment3_widths_v1/audit.json SHA256 3b82248b32a41361be76ac62e6fa79ae5b48259ef303e916bb45392ef10aebc8; completed 2026-10-29T17:54:13.763295+00:00, elapsed 0.238626 s. The serial holdout pause/resume took 0.398956 s.
