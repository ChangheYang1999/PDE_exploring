# Light reproductions for the final hours (2026-10-31, 23:53Z to 23:57Z)

Fresh copies of the scripts were run here (single thread) so that the stored outputs in `theory_code/` and `theory_code/tuned/` are not
overwritten. Each new output was compared with the stored one by `diff`.

| Script (copy in this directory) | Result |
|---|---|
| `constants.py` (input `cand007_f1_copy.json`) | `constants_out.json` identical to `../constants_out.json` |
| `prime_kappa_check.py 23` | `prime_kappa_23.out`: every prime p <= 23 matches the sign pattern (-1)^((a-4)/2); full_pattern True |
| `check_chi.py` | `check_chi.out`: residual/R^p tends to 18.25, against the predicted coefficient 18.2407 (low-order consistency only) |
| `rational_finite_order.py` (input `../tuned/candidate007_leading_exact.json`) | `logs/rational_finite_order.json` identical to the stored file (the stored copy belonged to the per-run logs, which are not published; this rerun is the published copy) |
| `tuned/o6_sym.py 3` | `tuned/o6_sym_3.out`: the compatibility polynomial agrees with the theory; real roots 0.28066166273196640400 and 0.64635228988093464431 |
| `tuned/sigma_check.py` | `tuned/sigma_check.json` identical |
| `tuned/sigma_inf_check.py` (after `sigma_check.py`) | `tuned/sigma_inf_check.out` identical |
| `tuned/component_box_check.py` | `tuned/component_box_check.out` identical |
| `tuned/tq_cert.py 4` | `tuned/tq_cert_Q4.out` identical except the timing line (16.9 s against 15.8 s); diff in `tuned/tq_cert_Q4.diff` |
| `tuned/tq5_bounds_radius.py` | `tuned/tq5_bounds_radius.out` identical except the timing line (37.1 s against 83.7 s); diff in `tuned/tq5b.diff` |

No reproduction disagreed with a stored result. These are reruns of the same code, not independent checks; the independent
checks are those recorded in the theory.
