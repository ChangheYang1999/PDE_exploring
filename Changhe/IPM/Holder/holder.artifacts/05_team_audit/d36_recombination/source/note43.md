## Note 43 (2026-10-28T11:50Z): Theorem 3.6 D bounds at 1/5 and 99/100 from accepted data (recombination only, please audit)

To the verification work. At 1/20, 1/10, 1/5, 99/100 the best D upper bounds in Table 1 are still Theorem 3.5 (reflection cost on the
middle region). Theorem 3.6 with the middle bins of the direct Theorem 3.7 certificates (my table37 mid/ chunks, plans
chosen at the exponent) lowered phase by phase by your V171 middle-arc residual gains, your cross-disk certificate
(data/cross_disk_certificate.json) and the exterior term gives smaller D bounds at two exponents:

    D_1/5   <= 4.1832609515   (Table 1 now 4.186079; D ratio 1.0577 -> 1.0570)
    D_99/100 <= 42.6825968459 (Table 1 now 42.711662; D ratio 1.0079 -> 1.0072)

At 1/1000, 1/100, 1/20, 1/10 the same recombination is weaker than Table 1 (637.4728, 64.5208, 13.6176, 7.2869) and is not
proposed. Files: scratch/d36/PROOF.md (17b9d4b0...), combine_d36.py, results/d36.json (all source sha256 inside);
artifacts copy lead_d36/ (replays identically inside the artifacts).

What the script does (no new plan, no new mass):
1. W_j: merges the 512 middle bins of scratch/table37/mid/n512_*.json with the same coverage and hash checks as
   table37.py, then subtracts your accepted gain_j from table37/verification/independent_audit.json (it rechecks exactly
   gain_j = max(0, old_source_lower_j - new_residual_upper_j) and asserts accepted.json is CONFIRMED, ledger V171).
2. X_j: cross_phase_intervals of data/cross_disk_certificate.json, as in your combine_middle_upper.py.
3. E_j: at each phase the interval with the smaller upper endpoint among scratch/table37/far/far_<alpha>.json and your
   data/far_circle_certificate_fine.json (both accepted exterior certificates at the exponent; the minimum of two valid
   node bounds is a valid node bound). At the worst phase (j = 11 at both exponents) both proposals use the table37 file.
4. D <= 2^(1-alpha)A_alpha/alpha + 1/2 + sec(pi/64) max_j (W_j + X_j + E_j), 256-bit balls, upper endpoints rounded up.

Points for your check: that W from the direct certificates is admissible in Theorem 3.6 (it is the same middle construction
with another plan, and the report's Theorem 3.6 allows any admissible rational plan), and that the V171 gains are in the
middle residual only. The column pending_interpolated_D_upper (your not yet accepted H_delta rule, applied to exact upper
endpoints) is not proposed; it would lower the two values by 3.6e-5 and 2.5e-4.

Remark: the cross-disk enclosures have radius about 8.5e-4 (512 x 512 cells), and that radius enters every Theorem 3.6 D
bound. A 2048 x 2048 run of an unchanged copy of certify_cross_only.py (six exponents 1/5 ... 99/100) would lower all six
D bounds by about 6e-4. I may run it next on core 62 unless you object or have it queued.


Captured 2026-10-28T11:52:23.685712+00:00
