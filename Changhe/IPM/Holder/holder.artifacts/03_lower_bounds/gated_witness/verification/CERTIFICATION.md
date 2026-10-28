# Interval certificate

From the artifacts root, run:

```sh
python3 code/certify_gated_lower.py --cells 262144
```

This writes `data/gated_lower_intervals.json`. All alpha inputs are exact rationals. The arithmetic uses 160-bit Arb balls. There are 262144 cells on each of three segments: the two analytic branches of K, and the tail function R. Each complete cell is evaluated as an interval and multiplied by its exact positive power weight. The adjacent PROOF.md proves both the integral identity and the enclosure method. The rational values under `safe_decimal_lower_10_places` are rounded down from the lower interval endpoint and may be used directly as certified lower bounds. The displayed decimal endpoint strings are approximations to endpoints and should not replace these safe rational bounds.

Independent high-precision diagnostics are in `code/check_gated_reduction.py`, `code/explore_unbounded_gate.py`, and their output JSON files. Those diagnostics are not part of the certificate.
