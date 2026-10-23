g, g_x, g_y of the saved hydrostatic trial states at the 19649 common points of hs_cauchy.py (X, Y arrays; 401 log radii 1e-3 .. 1e7 x 49 quadrant angles
including both axes), produced by src/hs_export_points.py from the states in ../hs/ (same sha256 as MANIFEST_STATES.md).  Purpose: independent recomputation of
the consecutive-state differences of NUM_REPORT 4P(b)(xvi) (max |g_a - g_b|/(1 + r)^p by region, p = 1/c).  Load: d = numpy.load(f); d['X'], d['Y'], d['g'], d['gx'], d['gy'].

Added 2026-10-22 (shift 7 / 8):
  *_nodes_maps.npz (src/hs_stationarity.py): node-level velocities of the solver's rebuilt standard maps and of the resolved evaluator at the collocation nodes
  of the 96x24 and continued 128x32 standard states (NUM_REPORT 4P(b)(xvi) item 15; checker 309 admitted the 96 export).
  *_nodes_resolved.npz / *_rows_resolved.npz (src/hs_node_check.py with HS_SAVE=...): x, y, V1, V2, g, g_xi, g_y, R_h, N_f of the resolved evaluator
  (32 inner Gauss points, >= 10 log panels per decade x 16 points, 400-point tail, exponent q = 2) at ALL collocation nodes of the standard 160x40 state (6400)
  and at all 12288 oversampled solve rows of the accurate-map 128x32 state hsQ_c2.0_N128_acc6_fine; scalar entries c, N, M, fine, rule, state_file, state_sha256,
  solver_nodes_Fmax.  R_h = (c x + V1) g_xi + (c y + V2) g_y - g and N_f = |(c x + V1) g_xi| + |(c y + V2) g_y| + |g| are recomputable from the saved arrays
  (exact agreement).  Purpose: direct checking of the two node sets whose maxima (NUM_REPORT item 14, ACC_FINAL item N / note 168) were otherwise record-only.
  hsQ_c2.0_N128_acc_scan_r3.npz, _r30.npz (src/hs_angular_scan.py with HS_SAVE, 2026-10-22T08:03Z): pointwise signed angular scan of the aliased accurate-map 128x32
  state hsQ_c2.0_N128_acc.pt at r = 3 and r = 30 on the 255 interior angles of the 257-point quadrant grid (theta, q = R_h/N_f, R_h, N_f, V1, V2, g, g_xi, g_y, x, y;
  default evaluator: 32 inner points, >= 10 log panels per decade x 16, 400-point tail with exponent 2, central-difference step 1e-5 (1 + r)).  Notes 178-179.
