# Shell-local Gaussian test


## V421 | 2026-10-29T19:10:19.102066+00:00 | Shell-local Gaussian test: one range failure, rescaled modal comparison

Claim. The shell-local manufactured-pressure construction proposed at 19:02:50Z can evaluate all 23 production shells and degrees 0 through 36 at eps_test=1e-4.

Method. Capture the in-progress record_63a v5 source, SHA256 8c372940984cd0b49a8e76ef0387699ee227db9d38ec3a848d97635ef901e80d, and execute only construction_test on the independently reconstructed P1 geometry. Supply spherical harmonics from associated Legendre functions, with angular Gram defect below 1e-12. Compare every case to long-double modal norms with scaled sums of squares. Also evaluate the exactly rescaled radial pressure (r/a)^l exp(-(r/a)^2) in binary64 using stable modal RMS. The scale-invariance argument and the core-ball convention were written in research/modal_pressure_laplacian/PROOF.md before execution. This is a captured development version, not an announced admission candidate.

Result. All 7 structural controls pass. The source returns passed=false and skips exactly (shell22,degree36), on [16384,32768]. Its other 850 ratios agree with the independent modal values at max(1e-9,1e-7 times reference). The outer degree-36 exact coefficient has maximum 7.47686515105909e154 and radial RMS 2.842139501301446476e154. Squaring these finite values exceeds binary64 range, so the source's unscaled RMS denominator is not finite. This is a range failure in the test, not an Euler pressure inconsistency.

The long-double modal maximum over all 851 cases is 5.0721416082657365e-6. All 851 normalized binary64 comparisons agree at the same tolerance; their maximum is 5.072140671507741e-6, below the 1e-4 gate. The source's finite maximum is 5.0721546044283475e-6. The observed maximum is above the lead's rough expected value of 3e-6; that estimate is not the registered threshold and its failure does not change the gate.

The core shell uses a=b/8, following HoldoutGrid.rmid, because its actual endpoint geometric mean is zero. This positive convention must be stated explicitly. The source tests the available m=0 and m=l harmonics together for each degree, subject to even-m parity. The independent modal ratio is unaffected by their count because the radial coefficient and its error are shared and the harmonics are orthonormal.

Verdict. CONFIRMED for the 850 finite source comparisons, the one reproduced overflow, and all 851 finite rescaled modal comparisons. REFUTED for complete finite coverage by this captured unscaled implementation and for the rough 3e-6 estimate. OPEN for a repaired production implementation, actual-state rho_P, any pressure error bound, and candidate clearance. Replace r^l by (r/a)^l or otherwise stabilize the norm, then recheck the actual implementation. Exact scale invariance justifies the mathematical test; this audit does not certify every floating-point implementation of that replacement.

Evidence. artifacts/local_shell_construction_v1/audit.json, SHA256 573f4ac98be53cf1ed7465fd96273f5c646d374ccb1d4fcb15f646720e94da74; completed 2026-10-29T19:09:36.604670+00:00, elapsed 6.509545928 seconds. The P2 worker's serial pause lasted 8.550994171 seconds and it resumed at19:09:36.959950Z. All source, proof, plan and geometry captures are retained.
