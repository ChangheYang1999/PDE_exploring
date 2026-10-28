# Reproducing the certificate

Run from the artifacts root:

```sh
python3 code/check_homogeneous_lower.py
```

The exact rational alpha inputs and Arb enclosures are retained in `data/homogeneous_lower_intervals.json`. The code sets 256-bit Arb precision. Its finite-series truncation uses the proved one-sided remainder in the adjacent PROOF.md. A separate mpmath quadrature is a diagnostic only. The Arb enclosures certify the explicitly defined lower-bound formula, while admissibility and the singular-integral identity are established analytically in PROOF.md.
