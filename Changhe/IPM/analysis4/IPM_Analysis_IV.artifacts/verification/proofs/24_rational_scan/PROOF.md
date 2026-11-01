# Independent finite scan of rational compatibility coefficients

Status: both finite scans completed. No density theorem for incompatible rational parameters is inferred from a finite scan.

## Exact claim and parameters

The numerical experiments reports that every reduced rational `delta` in the open interval `(2/5,1/2)` whose first stream resonance has order at most 60 has a nonzero compatibility coefficient when `f_1=sin(theta)`. It reports a smaller scan for the exactly extracted Candidate 007 profile.

For `delta=a/b` in lowest terms, write `q_0=2b/gcd(a,2)`. The first stream resonance is `n_0=q_0`, unless `q_0 delta=2`, in which case it is `n_0=2q_0`. Its angular index is `j_0=n_0 delta/2-1`. At that order define `kappa` as the coefficient of `sin((2j_0-1)theta)` in `f_(n_0)`. The pure stream equation is solvable exactly when `kappa=0`, as proved in topic 03.

## Independent method

The checker enumerates the rational set with exact fraction comparisons. It reads a fixed snapshot of the reported values, then recomputes every density coefficient through the first resonance with exact rational Laurent polynomials. Cartesian differentiation uses the operators `X,Y` derived in topic 21, restricted to log degree zero. If `A=i rho` and `B=i psi`, the nonlinear coefficient is `(X B)(Y A)-(Y B)(X A)`. The stationary equation divides its ordered sum at order `n` by `(n-1)(c-1)`.

For the stream, compute the Cartesian derivative `X A`; divide its Laurent frequency `k` by `k^2-P_n^2`, where `P_n=2-n delta`. Every preceding stream order is nonresonant in the sine space. Check the resulting stream by independent Cartesian application of `-Delta`, rather than only by the diagonal quotient. At the last order do not divide by zero: extract `kappa` from the density and check that the Cartesian forcing at frequency `2j_0` is exactly `-2j_0*kappa`.

The checker compares the exact rational values, retains the final density polynomials and records code and source hashes. A zero/nonzero verdict is made using exact numerators. Candidate leading data are read from the independent authoritative extraction in topic 02.

## What the finite conclusion proves

Each completed nonzero case is an obstruction to that exact pure density/stream ansatz. The coefficient scales by the `n_0`th power of a nonzero leading amplitude, so the obstruction persists under such scaling. A successful complete scan proves the finite universal statement over the enumerated rational set. It cannot prove that incompatible rationals are dense in any interval, cannot settle an irrational parameter, and cannot decide convergence of logarithmic repairs.

The dependencies are the exact Cartesian identities in topics 01 and 21 and the resonance theorem in topic 03. No theorem prover is used.

## Completed finite scans

The independent single-sine scan completed all 55 enumerated cases at 2026-10-31T03:18:11Z. Every exact compatibility coefficient matched and was nonzero. The Candidate-profile scan completed all four cases in its open interval and order range at 2026-10-31T03:15:53Z, again with exact agreement and nonzero coefficients. The complete lists and hashes are in `verification/sin1_summary.json`, `verification/cand007_summary.json`, and the per-case certificates. The single-sine scan ran in resumable chunks; a summary's elapsed time refers only to that chunk, not the entire computation. No missing time is inferred or padded.
