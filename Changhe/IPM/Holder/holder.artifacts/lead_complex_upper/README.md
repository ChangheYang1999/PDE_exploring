# Upper values of the complex-input bound at the exponents of Table 1

`check_complex_upper.py` evaluates the explicit upper bound of Theorem 1.4 (ii),
N_alpha <= 2 b_2 s^alpha/(alpha(1-alpha)), in 200-bit ball arithmetic at the ten exponents of Table 1 and rounds the
upper endpoint up at four decimals. Output: `complex_upper.json`. The proof of the bound is in
`16_beurling_complex_norm/optimized_upper/PROOF.md`; the lower values of Theorem 1.4 are in
`16_beurling_complex_norm/glued_witness/verification/formula_checks.json` (field `safe_M_lower`).

Reproduction: `python3 check_complex_upper.py` (python-flint, under one second).
