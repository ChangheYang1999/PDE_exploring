# Candidate data

Exact parameters and leading Fourier data of the best candidates, and the exact compatibility polynomials of the tuned
profiles. All coefficients are exact rationals unless stated otherwise.

- `cand007_f1.json`: Candidate 007 at its stored parameter, exact c_l = 4076476460239181/2251799813685248, delta, gamma and the exact odd-sine coefficients of the leading profile f_1 (input of the numerical runs, copy of `numerics/notes/cand007_f1.json`).
- `candidate007_leading_exact.json`: the independently extracted exact leading data of Candidate 007 (c, gamma, delta, density, potential and stream harmonics up to frequency 19, with source hashes); identical to `theory_code/tuned/candidate007_leading_exact.json` and to the data of the Candidate 007 extraction proof `verification/proofs/02_candidate007/PROOF.md`.
- `c007_p2048_coeffs_n100.json`: Fourier coefficients a_(n,k) of the far-field series for Candidate 007's profile, orders n <= 100, 2048-bit ball run, float64 mantissas with a log10 scale per order (copy of `numerics/ckpt/c007_p2048_coeffs_n100.json`).
- `tuned_b1_p1024_coeffs_n100.json`: the same export for the tuned series at delta = 2/3, c = 3, f_1 = sin theta + b sin 3 theta with b at the root 0.28066... of the first obstruction (copy from `numerics/ckpt/`).
- `P18_Q9_primitive.txt`: the primitive compatibility polynomial P_18 at Q = 9 (delta = 2/9) for f_1 = sin theta + b sin 3 theta, integer coefficients in descending order.
- `P20_Q10_primitive.txt`: the primitive compatibility polynomial P_20 at Q = 10 (delta = 1/5), integer coefficients in descending order.
- `tunedQ9_poly.json`: P_18 of `P18_Q9_primitive.txt` stored with ascending coefficients (input of the Q = 9 numerical root check).
- `tuned13_poly.json`: P_12 at delta = 1/3 (Corollary T_6), ascending integer coefficients and approximate real roots.
- `tuned35_poly.json`: P_10 at delta = 3/5 (Q = 10, h = 3), ascending integer coefficients and approximate real roots.
- `tuned49_poly.json`: P_9 at delta = 4/9 (Corollary T_{9,2}), ascending integer coefficients and approximate real roots.
- `tunedQ5_roots.json`: the six real roots of P_10 at Q = 5 (delta = 2/5) to 30 digits.
