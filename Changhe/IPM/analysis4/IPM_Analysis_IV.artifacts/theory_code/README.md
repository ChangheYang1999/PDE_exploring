# Code index (theory part)

All scripts are Python 3 (numpy, sympy, mpmath), single thread, run from this `theory_code/` directory unless a
sub-README says otherwise (the scripts in `tuned/` run from `tuned/`). Paths below are relative to `theory_code/`. Each
subdirectory with its own README lists inputs, outputs and run times there.

## Subdirectories

- `tuned/` (see `tuned/README.md`): the tuned pure series of Theorem T, T_Q and T_{Q,h} and Corollaries
  T_4 to T_10: exact compatibility polynomials and their irreducibility (`o6_sym.py`, `irr.py`, `tq_sym.py`,
  `tq_cert.py`), exact response functions and all-index response bounds (`sigma_*.py`, `tq_bounds_radius*.py`), the
  majorant radii, the top-sector necessary radii (`rh_top_Q*.py`), the order-Q potential logarithm (`aQ_poly.py`), and
  the double-precision tuned runs with their fits (`hh_float.py`, `fit_hhf.py`). The detached queues
  `run_after_queue*.sh` record the exact command lines used (their operational progress logs are not included; the
  outputs they produced are).
- `review/` (see `review/README.md`): independent reproductions of results reviewed in the theory (the
  polynomial-log 1-edge recurrence at delta = 2/3, the top-mode radius R_H, the zero-delta endpoint check).
- `modscan/`: `mod_scan.py`, the first compatibility coefficient at delta = 2h/Q over GF(ell) (a nonzero residue
  proves the coefficient nonzero); outputs `scan_sin1_Q120.*`, `scan_cand007_Q120.*` (all Q <= 120).
- `oddnum/`: the first compatibility coefficient at delta = a/p with a odd (`kappa_odd.py`), its p-adic digits
  (`kappa_odd_digits.py` -> `digits_sin1.out`), the p-adic pattern of f_n (`pattern_odd.py`) and a pattern guesser
  (`guess.py`).

## Top-level scripts

- `constants.py [../numerics/notes/cand007_f1.json]` -> `constants_out.json`, `brjuno.py`: Brjuno sums and the explicit constants of Theorem A.
- `rational_finite_order.py [tuned/candidate007_leading_exact.json]` -> `logs/rational_finite_order.json`: constants of Theorem E (geometric bound below the first resonance at rational delta).
- `prime_kappa_check.py PMAX` (e.g. 23): exact check of the prime-denominator congruence of Theorem P.
- `check_chi.py`: low-order consistency of the recurrence with direct substitution into the potential equation.
- `quick_float.py`: exploratory double-precision recursion (not evidence).
- Logarithmic series at rational delta (Section 14): `logseries.py` (double), `logseries_ld.py` (x87 long double),
  drivers `run_logseries_amp.py`, `run_logseries_ld.py`, diagnostics `logseries_diag.py`, `logseries_tprofile.py`,
  `analyze_logs.py`, `analyze_logs2.py`, `analyze_tprofile.py`, `deficit_rates.py`, `diag_decomp.py`,
  `poisson_transfer.py`, `exptype_norm.py`, `feedback_term.py`, `stream_ratio_modes.py`, `weighted_loss.py`. Their
  outputs (about 13 MB of per-order logs and diagnostics) are not included in the published folder; rerunning a script
  writes them to `logs/` (create the directory first).

## Reproducing

Restart commands for the whole folder are in the top-level `README.md`. `final_repro/README.md` records the final light
reproductions (fresh reruns of the main scripts in a separate directory; none disagrees with a stored result apart from
timing lines).
