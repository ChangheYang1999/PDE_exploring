# P229: beta>2 entire-axis separated-temperature exclusion

UTC: 2026-10-22T00:04:57.241018+00:00. CONFIRMED by the independent verifier, with external review availability limitation.

No smooth B2 profile at beta>2 in the broad polynomial-vorticity/sublinear-velocity target can satisfy Theta(x,y)=H(x/rho(y)) on an open neighbourhood of the entire vertical axis, with rho>0 everywhere. No regularity of the initial functions is required: the nonzero quadratic center jet supplies it. The exact theorem with explicit derivative bounds(S), its complete proof, and the dependency-checked broad-target corollary are in PROOF.md.

Method: axis transport gives rho with exponent1/2+1/beta at both ends. Symbol bounds make H's Taylor jet quadratic and C(k)=W2(k,0)'s jet a finite polynomial. This does not make the original germs analytic. The comparison field has a finite polynomial vorticity residual whose every jet vanishes, forcing a highest-degree Riccati identity. It would make a positive function tending to zero at both ends solve a constant-coefficient second-order ODE, which is impossible.

Verification: 53 own exact controls,14.323970s; 23 rescaling/dependency controls,0.745758s. Seven dependency proofs frozen. Actual Opus5.5 returned no written audit on four attempts, recorded without endorsement. Separate lead-lane audit pending. This is only a representation exclusion; the full B2 target remains OPEN.
