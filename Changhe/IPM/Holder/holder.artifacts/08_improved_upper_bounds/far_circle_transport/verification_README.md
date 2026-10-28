# Verification and reproduction

The analytic certificate is in `PROOF.md`. The following implementation uses Arb160 with finite angular and radial partitions, exact integer model masses, and an exact integer transport matrix. The floating search selects a plan only; it never supplies a feasibility or error bound.

- `code/certify_far_circles.py`: encloses every selected cell mass, bounds the residual antipodal transport, and integrates the exterior radial cells with exact power weights.
- `code/circle_transport_plan.py`: builds candidate integer plans and checks every row and column sum exactly.
- `code/check_far_circle_cells.py`: independent direct Cartesian density and adaptive quadrature tests. This is diagnostic evidence, not the proof.
- `data/far_circle_certificate_fine.json`: 512 angular cells, 128 radial intervals, 17 phase nodes, and ten exact rational exponents. Source and input hashes are recorded.
- `data/far_circle_cell_diagnostic.json`: 7776 cell checks across angular resolutions, phases and moving-zero parameter intervals. No mass, sign, total-variation or conservation discrepancy was found.
- `code/combine_circle_upper.py`: combines the audited compact-region intervals with the exterior certificate, keeping the uniform local contribution outside phase interpolation.
- `data/circle_composite_upper_fine.json`: complete upper bounds, not merely an exterior contribution.

All paths above are relative to the artifacts root. Reproduce from that root with the supplied Python 3.12 environment, without a server:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 code/certify_far_circles.py --angles 512 --radial 128 --alphas 1/1000,1/100,1/20,1/10,1/5,3/10,1/2,3/4,9/10,99/100 --out data/far_circle_certificate_fine.json
PYTHONDONTWRITEBYTECODE=1 python3 code/check_far_circle_cells.py
PYTHONDONTWRITEBYTECODE=1 python3 code/combine_circle_upper.py
```

The composite certificate has its own provenance hashes. A displayed ball's lower endpoint describes this particular upper-bound formula and is not an operator lower bound. The `safe_upper_C` and `safe_upper_D` fields are ceilings of the internal interval upper endpoints.
