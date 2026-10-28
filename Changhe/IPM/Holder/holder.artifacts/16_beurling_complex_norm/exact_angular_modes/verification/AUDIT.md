# Independent proof audit

Checked 2026-10-28T07:30Z. The convexity direction for log cosh, the
monotonicity in u, the affine normalization of the two radii, and the
folding of the angular interval are correct. Equal radii attain the
bound, so this is an exact seminorm calculation, not only a sufficient
bound. Differentiating in s=sin(t) gives the displayed Q2 and Q3.
The Fourier coefficient identity introduces exactly 2 sin(nt), so its
constant is the reciprocal of the exact angular-mode seminorm.
The cubic operator coefficient was independently checked in V102.
The direct compact radial contraction preserves the vector seminorm
and avoids an unsupported general vector extension theorem.

The script formula_checks.json evaluates elementary formulas with
192-bit Arb balls and 100 positive terms of J, with the entire remaining
tail enclosed. Every endpoint is stored as an exact rational. The ten
comparisons use the accepted exact safe C upper endpoints. The 2800
65-digit point-pair tests are diagnostics supporting the algebra, not
proofs of a continuum inequality. All passed.

Verdict: CONFIRMED. Exact mode norms and angular functional constants;
stronger cubic lower bound; ten strict complex-versus-real comparisons.
No exact finite-exponent operator norm is claimed.
