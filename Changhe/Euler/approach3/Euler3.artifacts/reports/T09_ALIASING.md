# T09 aliasing test of the ranking diagnostics (generated 2026-10-25T03:27Z; scripts/t09_aliasing.py)

Holdout SPEC diagnostics on the standard holdout grid (Gauss radii, 6 per dyadic shell; angular Gauss grid 2 L_ext + 12 by 4 L_ext + 18) against
a 1.5x finer angular holdout grid and a 2x radial holdout grid (12 Gauss radii per shell). PASS requires relative changes below 10 per cent (SPEC T09).

| state | L / L_ext | grids (std / angular 1.5x / radial 2x) | rho_u_max (std) | change angular 1.5x: rho_u / rho_nl / sigma_u / a_max / worst shell | change radial 2x: rho_u / rho_nl / sigma_u / a_max / rho_Om / worst shell | verdict |
|---|---|---|---|---|---|---|
| d6t_L8_cl0.45_om+0.3_fixed | 8 / 8 | [28, 50] / [42, 75] / 12 radii per shell | 0.04556 | 9.1e-16 / 1.4e-13 / 3.6e-16 / 6.0e-16 / 3.5e-10 | 3.3e-03 / 2.3e-07 / 1.1e-06 / 1.2e-06 / 1.3e-02 / 3.3e-03 | PASS (worst 1.3e-02) |
| d6w3_L6_cl0.45_om+0.3_fixed | 6 / 15 | [42, 78] / [63, 117] / 12 radii per shell | 0.05269 | 5.3e-16 / 5.0e-15 / 9.4e-16 / 4.7e-16 / 4.9e-09 | 3.7e-06 / 3.3e-07 / 3.3e-06 / 3.3e-06 / 1.8e-03 / 2.6e-04 | PASS (worst 1.8e-03) |
| nest2_L2_cl0.45_om+0.3 | 2 / 2 | [16, 26] / [24, 39] / 12 radii per shell | 0.10752 | 0.0e+00 / 4.4e-16 / 0.0e+00 / 1.4e-16 / 3.3e-11 | 8.0e-08 / 1.7e-07 / 7.2e-08 / 7.2e-08 / 6.7e-13 / 1.9e-06 | PASS (worst 1.9e-06) |

Reading: the angular holdout quadrature is exact for these states (changes at the 1e-15 level, since the Gauss grids integrate the products of the
represented degrees exactly); the radial refinement moves the shell values by at most 3.3e-3 (rho_u^max of d6t_L8) and 1.3e-2 (rho_Om^max of d6t_L8).
The direct residual lines of validate_candidate.py (training grid against 1.5x grid) are a different, node-based comparison; before 03:09Z that script sized
its grids by L instead of L_ext, so its lines on extended-channel states were aliased and are not used (NUM_REPORT, T09 provenance statement).
