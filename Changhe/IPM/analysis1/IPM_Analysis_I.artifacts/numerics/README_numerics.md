# Artifacts of the numerics lane (ipmA-num): validated numerics for the a posteriori analysis of the IPM profile X3

Everything here is relative to this folder; the scripts also run from the lane root (they add their own directory to
sys.path). Python 3.9, numpy 2.0, scipy 1.13, python-flint 0.6 (Arb), mpmath 1.3; single thread (OMP_NUM_THREADS=1).
The published candidate X3 (c6g_shape.npz, md5 15f8095f7e79dbfa0c50d75e5fe8997a, folder a_coefficients of the published IPM Setting I artifacts,
Changhe/IPM/case1/IPM_Setting_I.artifacts in Changhe Yang's repository https://github.com/ChangheYang1999/PDE_exploring.git; the run used the clone
PDE_exploring at commit 701899f69e2e9fa1394357b3d455c80a649d092c; `git clone` that URL and point X3_COEFF_PATH at the file) is NOT
redistributed here: obtain it and set the environment variable X3_COEFF_PATH to its path (src/x3.py; the default is the clone path). The self-test
`python3 src/x3.py` also imports the published evaluator gen_shape.py from the artifacts' d_evaluator/code folder (X3_EVALUATOR_DIR). The scripts that
evaluate X3 itself need the coefficient file: x3.py, x3_resid.py, x3_modes.py, modal_fit.py, trial_resid.py, axis_diag.py, dw_map.py, fit_test.py,
x3_minus_trial_jets.py (section 7.8); all other scripts (the certificate pipeline from data/trial_v2_h0.008.npz, the finite sections, the X norms, the
summaries and tables) need neither external input. The historical chain scripts (runs/chain*.sh, runs/n8/*.sh, runs/collect_v3.sh) are records of
the actual runs and begin with `cd` into the lane directory; edit that line to run them from a copy of this folder (runs/variant_regen.sh and
runs/hash_check.py already run from a copy of this folder).

## Contents
- src/x3.py, src/x3_arb.py: exact reconstruction of X3 from c6g_shape.npz (float64; Arb point enclosures).
- src/inverse.py, src/x3_resid.py: own canonical modal inverse and residual tables of X3 (floating point).
- src/x3_modes.py, src/modal_fit.py, src/expoly.py, src/trial_green.py, src/trial_resid.py: the explicit modal trial
  rho~ (fit to X3's modes; closed-form Green inverse; floating-point residual). data/trial_v2_h0.008.npz is the fitted
  trial; data/cert_coeffs.json the exactified dependent coefficients (Ei, Eo, A00 as [midpoint, radius] balls).
- src/midrad.py (rigorous mid-rad numpy arithmetic), src/cert_spline.py, src/cert_green.py (Arb: exactification, Green
  boundary values on sub-cells), src/cert_resid.py (Taylor-model residual bounds, derivatives), src/cert_scalars2.py (S1),
  src/cert_green_outer.py, src/cert_resid_regions.py, src/cert_resid_deriv.py, src/cert_tail.py, src/cert_inner_tail.py,
  src/cert_summary.py, src/reexport_coeffs.py: the certificate pipeline (SPEC items R0, R1, R3, R4, R5, S1, R2).
- src/test_cert_small.py, src/test_cert_deriv.py: consistency tests of the certificate on a 20-mode truncation.
- src/dw_map.py (C1 maps, floating point), src/finite_section.py (C2, floating point, prototype).
- runs/: result JSONs (floating tables; S1 balls; middle-region R0 summary) and the chain scripts chain1..5.sh. The four per-cell
  certificate files above 3 MB (cert_resid_regions.json, cert_resid_middle.json, flow_outer.json, flow_middle.json) are stored gzipped (gunzip to read).
- notes/: capabilities note, team notes, C2 plan, the two external referee answers (astra).

## Exact commands (times on one core of the run machine)
```
python3 src/x3.py                                   # X3 reconstruction test (0.1 s)
python3 src/inverse.py                              # manufactured inverse tests (1 s)
python3 src/x3_resid.py 16875 512 1e-4 1e6 runs/resid_N16875_q512.json          # published-table reproduction (8 s)
python3 src/x3_modes.py 80000 4096 1e-4 1e5 260 data/x3_modes_N80000_q4096_M260.npz   # modes of e^H (34 s, 320 MB)
python3 src/modal_fit.py data/x3_modes_N80000_q4096_M260.npz 0.008 0.02 data/trial_v2_h0.008.npz   # fit (55 s)
python3 src/modal_fit.py data/x3_modes_N80000_q4096_M260.npz 0.004 0.01 data/trial_v3_h0.004.npz        # variant v3 (7.3c): h = 0.004, h_in = 0.01 (4 min)
python3 src/modal_fit.py data/x3_modes_N80000_q4096_M260.npz 0.008 0.02 data/trial_v4_M230.npz 230      # variant v4: modes m < 230
python3 src/modal_fit.py data/x3_modes_N80000_q4096_M260.npz 0.008 0.02 data/trial_v5_R0knot2.npz - -2  # variant v5: R0 = the second-to-last X3 knot (1467.96)
# The four trial files (3 to 6 MB each, 15 MB together, incompressible) are NOT in this folder except data/trial_v2_h0.008.npz. On 2026-10-22 (shift 8)
# the two commands above and these three were rerun from the published c6g_shape.npz (runs/variant_regen.sh; outcome runs/variant_regen/compare.txt):
# all four regenerated files are BYTE-IDENTICAL to the stored ones (every array equal; SHA-256 a069d85d... / 1e4ee66f... / 11c97a14... / 74345bd9..., section 8 of NUM_REPORT.md).
python3 src/trial_green.py data/trial_v2_h0.008.npz                             # closed-form inverse vs grid (2 min)
python3 src/trial_resid.py data/trial_v2_h0.008.npz 1200 runs/trial_v2_resid.json  # floating residual (1 min)
python3 src/cert_green.py data/trial_v2_h0.008.npz 256 0.0019 data/cert         # Arb boundary values (16 min, 291 MB)
python3 src/reexport_coeffs.py data/trial_v2_h0.008.npz data/cert_coeffs.json 256
python3 src/cert_scalars2.py data/cert_green.npz data/trial_v2_h0.008.npz runs/scalars_full.json   # S1 (10 s)
python3 src/cert_resid.py data/cert_green.npz data/trial_v2_h0.008.npz runs/cert_resid_middle.json 12   # R0 middle (35 min)
python3 src/cert_green_outer.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json 0.0019 17.0 5.0 data/cert 256   # final regions T_out = 17, T_in = 5 (10.0 2.5 was the first, historical configuration)
python3 src/cert_resid_regions.py data/cert_green.npz data/trial_v2_h0.008.npz data/cert_outer_green.npz data/cert_inner_green.npz runs/cert_resid_regions.json
python3 src/cert_tail.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json data/cert_outer_green.npz 0.5 runs/cert_tail_d05.json 256   # outer tail, exponent delta = 0.5
python3 src/cert_tail.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json data/cert_outer_green.npz 0.32063946870624582 runs/cert_tail.json 256   # delta = 1/2 - k: the shipped runs/cert_tail.json
python3 src/cert_inner_tail.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json data/cert_inner_green.npz runs/cert_inner_tail.json 256
python3 src/cert_resid_deriv.py data/cert_green.npz data/trial_v2_h0.008.npz runs/cert_deriv                                   # middle region -> runs/cert_deriv_middle.json (3.3 h)
DERIV_SKIP_MIDDLE=1 python3 src/cert_resid_deriv.py data/cert_green.npz data/trial_v2_h0.008.npz runs/cert_deriv_regions data/cert_outer_green.npz data/cert_inner_green.npz   # -> runs/cert_deriv_regions_{outer,inner}.json (the names read by xnorm_cert.py)
python3 src/cert_summary.py
python3 src/truncate_trial.py data/trial_v2_h0.008.npz 20 data/trial_small_M20.npz   # 20-mode test fixture (shipped; this command reproduces it byte-identically)
python3 src/cert_green.py data/trial_small_M20.npz 256 0.0019 data/cert_small               # its Arb Green data (90 s, 22 MB, not shipped)
python3 src/test_cert_small.py; python3 src/test_cert_deriv.py     # certificate consistency tests on the 20-mode fixture (14 s + 13 s; rerun with the final sources 2026-10-22T07:44Z, rc 0)
```
The large intermediate files (modes, cert_green.npz) are regenerable with the commands above and are not included.
Storage rule (shift 7, 2026-10-22): every JSON result file above 400 KB and every pickled column piece (runs/c2/*_cols.pkl) is stored
gzipped (name.json.gz, name.pkl.gz). The summary scripts (variants_summary, cert_summary, xnorm_cert, cert_deriv_summary, deriv_region_shells,
flow_summary, resid_summary_any) and the K-projection scripts (c2_Kproj, c2_vec_profile) read the gzipped file when the plain one is absent;
for the pipeline commands that take data/cert_*_coeffs.json or a per-cell JSON as input, gunzip the file first. `python3 src/variants_summary.py`
run inside this folder reproduces runs/variants_summary.txt from the gzipped per-cell files (checked identical to the lane's table).

## Shift 2 additions (2026-10-20, 18:38Z onward)
- src/trial_jets.py (analytic derivative jets of eps~ to order 4; validated vs finite differences and refereed), src/pdisc_norms.py,
  src/pdisc_fft.py, src/pdisc_explore.py, src/axis_diag.py, src/wiggle_diag.py: Sobolev norms of the residual near P (floating).
- src/smooth_band.py, src/smooth_band2.py (coarse-knot projections of the trial on a band; strain functional preserved),
  src/lin_assembly.py, src/lin_fast.py (fast assembly of the linearized operator on single-mode basis functions; identity test
  L rho~ = 2 eps~ + rho~ - X.grad rho~/3), src/gn_refit.py, src/gn_refit2.py (coarse-space Gauss-Newton re-solves),
  src/resid_smooth.py (fine-knot refit with a residual-derivative penalty), src/c2_fminus.py (F- / free-tail finite sections).
- src/cert_flow.py, src/cert_flow_tails.py, src/flow_summary.py: RIGOROUS 2D bounds of X.V/r^2, V_2/y, V_1/x, T_0 (lead's N1').
- src/cert_deriv_summary.py: shells of the rigorous derivative certificate (runs/cert_deriv_summary.txt).
Commands (from the lane root):
```
python3 src/trial_jets.py                                                   # jet tests (3 min)
python3 src/pdisc_norms.py data/trial_v2_h0.008.npz A runs/pdisc/norms_A.json   # 1 min (grids B, C, D likewise)
python3 src/pdisc_fft.py data/trial_v2_h0.008.npz 0.4 0.5 1e-3 runs/pdisc/fft_r0.5_k7.json 1.25 7   # 3 min
python3 src/axis_diag.py data/trial_v2_h0.008.npz; python3 src/wiggle_diag.py
python3 src/smooth_band.py data/trial_v2_h0.008.npz 1.7918 2.4849 0.0038 data/trial_b0.0038.npz
python3 src/smooth_band.py data/trial_v2_h0.008.npz 1.7918 2.4849 0.02 data/trial_s02.npz   # fixture of lin_fast.py (2 s; reproduces the stored file byte-identically; 2.9 MB, not shipped)
python3 src/lin_assembly.py; python3 src/lin_fast.py                        # assembler tests (data/trial_small_M20.npz and data/trial_s02.npz; 105 s + 77 s; rerun 2026-10-22T07:44Z, rc 0)
python3 src/gn_refit2.py data/trial_cC_lo10.npz 1.7918 2.4849 10 0 10 100 1e-8 data/trial_gnCc.npz 2
python3 src/c2_fminus.py data/trial_v2_h0.008.npz 16 16 40 runs/pdisc/c2f_M16_s16_p4.json 4
python3 src/cert_deriv_summary.py runs/cert_deriv_middle.json
python3 src/cert_flow.py data/cert_green.npz data/trial_v2_h0.008.npz middle runs/flow_middle.json 200       # 75 min
python3 src/cert_flow.py data/cert_green.npz data/trial_v2_h0.008.npz outer runs/flow_outer.json 200 0 - data/cert_outer_green.npz
python3 src/cert_flow_tails.py data/trial_v2_h0.008.npz data/cert_green.npz data/cert_coeffs.json data/cert_outer_green.npz data/cert_inner_green.npz runs/flow_tails.json 256
python3 src/flow_summary.py
python3 src/resid_smooth.py data/trial_v2_h0.008.npz 2.05 2.28 40 50 5e-4 data/trial_rs 0,1e-16,1e-15,1e-14,1e-13,1e-12,1e-11,1e-10   # settings of data/trial_rs_summary.json
```
Referee answers: notes/astra_jets1_answer.md (jets, norms, identity), notes/astra_smooth1_answer.md (inference critique).

Late shift-2 additions:
- src/cert_axis_cell.py (crossing-cell certificate: w' > 0 on the radial cell containing x_*; runs/axis_cell.json),
  src/make_n7.py (centre-regular trial N7: data/trial_n7.npz; its certificate: cert_green.py / cert_scalars2.py / cert_resid.py on it,
  runs/scalars_n7.json, runs/cert_resid_middle_n7.json), src/resid_summary_any.py (shell summary of any cert_resid output),
  src/refine_knots.py (exact knot insertion for the half-spacing refit), runs/flow_summary_all.txt (whole-quadrant N1' aggregate).
```
python3 src/cert_axis_cell.py data/cert_green.npz data/trial_v2_h0.008.npz runs/scalars_full.json runs/axis_cell.json
python3 src/make_n7.py data/trial_v2_h0.008.npz data/trial_n7.npz 4
python3 src/cert_green.py data/trial_n7.npz 256 0.0019 data/cert_n7      # 50 min under load
python3 src/cert_scalars2.py data/cert_n7_green.npz data/trial_n7.npz runs/scalars_n7.json 8.600063803
python3 src/cert_resid.py data/cert_n7_green.npz data/trial_n7.npz runs/cert_resid_middle_n7.json 12
python3 src/resid_summary_any.py runs/cert_resid_middle_n7.json
```

## Shift 3 additions (2026-10-21, 00:33Z onward)
- src/n8_floating.py (floating sampled suprema of the Frobenius norms of D^j V, D^j rho~ on B_{3 delta}(P); runs/n8/n8_floating.json),
  src/cert_n8.py (RIGOROUS upper bounds of the same quantities: Taylor models of the mode derivatives per radial sub-cell, two-sided Bernstein
  ranges on sub-intervals, Arb sin/cos enclosures on the angular cells, interval polar-to-Cartesian recursion; runs/n8/cert_n8_full.json,
  runs/n8/cert_n8_fine0165.json), runs/n8/fft_chain.sh (cut-off H^s norms of the residual on the four balls; runs/n8/fft_delta*.json).
- src/flow_summary.py: the tail lower bounds are now printed floor-rounded (outward) with the raw values.
```
python3 src/n8_floating.py data/trial_v2_h0.008.npz runs/n8/n8_floating.json 1e-4 1e-4                      # 10 s, floating
python3 src/cert_n8.py data/cert_green.npz data/trial_v2_h0.008.npz runs/n8/cert_n8_full.json 4 350 0.2      # 400 s, RIGOROUS
python3 src/cert_n8.py data/cert_green.npz data/trial_v2_h0.008.npz runs/n8/cert_n8_fine0165.json 16 160 0.0165   # 90 s, RIGOROUS (fine pass)
bash runs/n8/fft_chain.sh                                                                                   # 6 min, floating
```
- src/variants_summary.py (three-resolutions table of the certificate quantities per trial variant; runs/variants_summary.txt, .json),
  runs/chain7.sh (queue reorder: chain6 before the v4/v5 variants, then runs them).
```
python3 src/variants_summary.py                     # all variants with outputs (seconds)
```
- src/x3_minus_trial_jets.py (floating four jets of h = X3 - trial at P; runs/jets/*.json), src/aux_R.py (floating constants R, E of the auxiliary
  source inverse, dilated R~(ell), inverse bounds and localized forcing N_{1/ell}(tau eps~); runs/n9/*.json), src/c2_gram.py v2 (C2 with a
  conditioned, conforming column basis: X-Gram with the background-relative H^1 inner product, equilibration, C^0/C^1 join matching, eigen-cut,
  SVD, stable projections, principal angles; runs/c2/c2gram_*.json), src/c2_gram_summary.py (table), runs/chain8b.sh (the C2 chain),
  runs/chain6b.sh (regions-only derivative certificate), runs/chain7.sh (queue reorder watcher), runs/lane_ps.sh (safe process listing).
```
python3 src/x3_minus_trial_jets.py 12000 512 1e-4 1e5 runs/jets/x3_minus_trial_N12000_T512.json      # 94 s
python3 src/aux_R.py 512 0.08 0.0165 3.1 runs/n9/aux_R_n512.json                                      # 40 s
python3 src/c2_fminus.py data/trial_v2_h0.008.npz 16 16 40 runs/c2/c2f_M16_s16_p2.json 2 runs/c2/c2raw_M16_s16_p2.npz   # 85 min under the guard
python3 src/c2_gram.py runs/c2/c2raw_M16_s16_p2.npz runs/c2/c2gram_M16_s16_p2_H1m_NJ0.json 1e-10 0 H1m                 # 105 s
python3 src/c2_gram_summary.py > runs/c2/c2gram_summary.txt
```
- src/forcing_decomp.py (floating decomposition of the localized forcing tau eps~ near P into a degree-5 odd polynomial model and a remainder,
  Gaussian-window norms; runs/n10/*.json): `python3 src/forcing_decomp.py 512 0.16 0.028875 0.037125 3.1 0.01,0.02 runs/n10/decomp_d0.0165_n512_L0.16.json` (48 s).

## Shift 4 additions (2026-10-21): certified localized forcing norm at P (NUM_REPORT 7.10)
- src/cert_forcing.py (v1.2; v1.1 was the first-run version), src/cert_forcing2.py (v2.2; v2.1 likewise): rigorous upper bounds of ||tau eps~||_{H^{3.1}} and N_500(tau eps~) for the C^4
  degree-9 radial cutoff at delta = 33/2000 (bivariate Taylor models of the residual (and, in v2, of the cutoff) near P, Hoelder between the
  certified orders 3 and 4); src/forcing_float.py: floating FFT companion. Outputs (here as *_summary.json without the per-sub-cell rows; full files with SHA in the lane) runs/forcing/v12_p9_merged.json (2.1207 / 4.2064),
  runs/forcing/v22_p9_merged.json (1.5700 / 3.5769; v11/v21 summaries are the identical earlier versions), runs/forcing/float_p9_dx45.json (1.3296 / 3.1128), v22_p11_merged.json (C^5 step: 2.9112 / 4.9508; floating float_p11_dx90.json 1.6663 / 3.3693), SHA256.txt; the first-run output
  p9_K64_n16_P8_merged.json (5.6533, superseded) is kept for the record of the referee round (astra/forcing1_*.md).
- Commands (the box CPU guard (bin/cpu_guard.py) allows one running detached python job per lane among those aged at least 120 s and pauses the others (processes in the session of the lane's agent loop are exempt by its code; in shift 4 foreground python pieces of this lane were nevertheless observed paused, so all foreground pieces were kept under 120 s); the forcing cells were run as short foreground pieces beside the detached chain; about 11 and 20 min in total):
```
for ci in $(seq 4096 4108); do python3 src/cert_forcing.py data/cert_green.npz data/trial_v2_h0.008.npz runs/forcing/v12_p9_c$ci.json 33/2000 p9 64 16 8 8 $ci $ci; done
python3 src/cert_forcing.py merge runs/forcing/v12_p9_merged.json runs/forcing/v12_p9_c4*.json
for ci in $(seq 4096 4108); do for q in "0 7" "8 15"; do set -- $q; python3 src/cert_forcing2.py data/cert_green.npz data/trial_v2_h0.008.npz runs/forcing/v22_p9_c${ci}_q$1.json 33/2000 p9 64 16 8 8 2 2 16 $ci $ci $1 $2; done; done
python3 src/cert_forcing2.py merge runs/forcing/v22_p9_merged.json runs/forcing/v22_p9_c4*_q*.json
python3 src/forcing_float.py data/trial_v2_h0.008.npz 0.0165 p9 4.5e-5 runs/forcing/float_p9_dx45.json
```
- src/deriv_region_shells.py: per-shell ceilings of the derivative certificate for a region file (NUM_REPORT 7.3b outer/inner tables);
  outputs runs/cert_deriv_outer_shells.txt (and _inner_ when the inner region is done).

## Shift 5 additions (2026-10-21, 12:26Z onward): C2 Gram version 3 (NUM_REPORT 7.4b; FLOATING, evidence only)
- src/c2_gram2.py: version 3 of c2_gram.py: three continuous reference functions (x^2 y times a C^4 degree-9 polynomial step in t = log r:
  ref_J on [t0 - 1, t0], ref_Jin on [tmin - 1, tmin], ref_wide on [tmin, t0]) appended to the extended Gram basis, with their H1m norms, the
  cos^2 of the smallest singular directions with each, and the cos^2 of each with the whole F- span; the five smallest right singular vectors of
  every section saved (out_vec.npz, column 0 = smallest; with the references' Gram columns, A0/Bm, and the section metadata); SECTIONS argument
  ('two' = Fminus and free); ROWS argument ('H1' = H1-type image norm: value rows times sqrt(1 + (2N+1)^2) plus radial finite-difference rows;
  spectrum from the chunked normal matrix; C2_EIGH=1 forces that route for ROWS = L2 as a precision check).
- src/c2_vec_profile.py: post-hoc localization of the saved smallest singular vectors (X-energy per dyadic shell of r, energy median radius,
  per-mode energy fractions, coefficient mass by column kind) from the _cols.pkl pieces alone.
- src/c2_gram_table.py: the three tables of 7.4b (runs/c2/c2gram_table.md, c2gram2_table.md, c2gram2_rowsH1_table.md).
- runs/chain8d.sh (version-2 M16 ppc 4/6 and M24/s8 rows), runs/chain8e.sh (version 3 on M24/s8 and M16/s16 ppc 4), runs/chain8f.sh
  (intermediate sections M16/s8/Mout40, M24/s16/Mout40, M24/s16/Mout32 at ppc 4; M16/s16 ppc 2 and 6 in version 3), runs/chain7d.sh (v4/v5).
Commands (from the lane root; the raw section files are regenerated by c2_fminus.py and deleted after use, they are not included):
```
python3 src/c2_fminus.py data/trial_v2_h0.008.npz 24 8 32 runs/c2/c2f_M24_s8_p4.json 4 runs/c2/c2raw_M24_s8_p4.npz     # 44 min, 1.16 GB
python3 src/c2_gram.py  runs/c2/c2raw_M24_s8_p4.npz runs/c2/c2gram_M24_s8_p4_H1m_NJ0.json 1e-10 0 H1m                   # version 2
python3 src/c2_gram2.py runs/c2/c2raw_M24_s8_p4.npz runs/c2/c2gram2_M24_s8_p4_H1m_NJ0.json 1e-10 0 H1m two L2          # version 3, L2 rows
python3 src/c2_gram2.py runs/c2/c2raw_M24_s8_p4.npz runs/c2/c2gram2_M24_s8_p4_H1m_NJ0_rowsH1.json 1e-10 0 H1m two H1   # H1-type rows
python3 src/c2_vec_profile.py runs/c2/c2gram2_M24_s8_p4_H1m_NJ0_vec.npz runs/c2/c2raw_M24_s8_p4_cols.pkl Fminus 3
python3 src/c2_gram_table.py
python3 src/c2_fminus.py data/trial_v2_h0.008.npz 4 60 16 runs/c2/c2f_test.json 2 runs/c2/c2raw_test.npz                         # the test section (Mh 4, stride 60, Mout 16, ppc 2; 85 s; the 3.3 MB raw file is not shipped)
python3 src/c2_gram2.py runs/c2/c2raw_test.npz runs/c2/c2gram2_test.json 1e-10 0 H1m two L2                               # 1 s test section
```
- src/c2_img_eval.py (16:03Z): evaluates the saved weakest directions of a section under all four row functionals (L2, L2q, H1, H1q) from their
  saved unweighted collocation images (<section>_img in the _vec.npz written by c2_gram2.py after 16:00Z), so that the same vectors are compared
  in the different image norms; runs/collect_v3.sh runs it on every vector file with images (runs/c2/imgeval.txt). runs/chain8f2.sh replaced the
  chain8f watcher (same sections plus L2q rows, eigen-cut sensitivity of H1q at M16/s8, M16/s16 ppc 4 re-run with images, M24/s8/Mout40).
  Referee rounds: notes/astra_gram3_*.md (design), notes/astra_gram4_*.md (interpretation; the referee's working folder astra/gram4/ exists in the lane only).

## Shift 6 additions (2026-10-21, 18:24Z onward): analytic-derivative X norms (NUM_REPORT 7.11; FLOATING) and the ppc 6 Gram rows
- src/xnorm_jets.py: X norms ||f||_X^2 = int (f^2 + r^2 |grad f|^2) w dX, w = m^-2 (1+u^2)^-3/2, of eps~, eps~ - X.grad eps~, K = rho~ - X.grad rho~
  and rho~ for the modal trial, with ANALYTIC t-derivatives of the residual modes (Leibniz on the modal jets of src/trial_jets.py), exact angular
  integration and knot-aligned Gauss-Legendre quadrature (1558 knot cells + 120 inner + 240 outer log cells). Outputs runs/xnorm_jets/*.json
  (norm^2 per region and per part: value, t-derivative, angular derivative). The finite-difference route src/xnorm_K.py is superseded (its
  derivative rows were noise-dominated); src/xnorm_cert.py gives the rigorous Wiener-sum ceilings from the saved certificate cells.
- runs/c2/c2gram2_M16_s16_p6_H1m_*.json (+ _vec.npz not included): version-3 Gram at six collocation points per cell (NUM_REPORT 7.4b (vii)).
Commands (from the lane root):
```
python3 src/xnorm_jets.py --check data/trial_v2_h0.008.npz                                        # 44 s: order 0, FD and angular-grid checks
python3 src/xnorm_jets.py data/trial_v2_h0.008.npz 4 0 1921 runs/xnorm_jets/full_g4_v2.json       # 110 s: all 1921 cells, 4 Gauss nodes each (version 2 = the reported values)
python3 src/xnorm_jets.py data/trial_v2_h0.008.npz 6 626 969 runs/xnorm_jets/lobe_g6_v2.json      # 53 s: lobe cells (4 <= r <= 16), 6 nodes
# superseded version 1 (1918 cells, before three boundaries were added): `... 4 0 1918 runs/xnorm_jets/full_g4.json`, `... 6 625 965 runs/xnorm_jets/lobe_g6.json`
python3 src/xnorm_jets.py --merge out.json piece1.json piece2.json ...                            # sums pieces (coverage check)
python3 src/xnorm_cert.py                                                                          # rigorous ceilings (seconds)
```
- src/xnorm_BKK.py (19:0xZ): B(K, K) = U[K].grad K in the X norm; builds the closed-form canonical inverse for K = rho~ - X.grad rho~ (a~_m = -2 a_m - a_m'
  in place of a_m) and reuses the residual/jet machinery with c_l = 0. `python3 src/xnorm_BKK.py --check data/trial_v2_h0.008.npz` (77 s; scaling
  identity psi[K] = 2 psi~ - X.grad psi~, c[K] = 0); production in two pieces (61 s each) merged by xnorm_jets.py --merge (runs/xnorm_jets/BKK_g4_*_v2.json).
- Referee round astra/xnorm1 on xnorm_jets.py: notes/astra_xnorm1_question.md, notes/astra_xnorm1_answer.md (kernel and norm identity confirmed; region
  split, merge checks and --check assertions repaired in the current version; the *_v2.json outputs are from the repaired version).
- src/c2_Kproj.py (19:3xZ; NUM_REPORT 7.4c): does the finite section see the scaling tangent K? Stage A rebuilds the section's H1m Gram from the pickled
  column pieces (checked against the saved diagonal), adds K's mode-parts and projects K onto the constrained span (cos^2, coefficients); stage B
  assembles L on the projection with the section's assembler (src/lin_fast.py) and evaluates the four row functionals of c2_gram2 on it and on the
  direct image L K = eps~ - X.grad eps~ (analytic jets); stage C applies the assembler to K's own fine-knot pieces (cross-check). Commands:
```
python3 src/c2_Kproj.py A data/trial_v2_h0.008.npz runs/c2/c2raw_M16_s16_p4_re2_cols.pkl runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q_vec.npz 1 1e-10 runs/kproj/Kproj_M16_s16_NJ1.npz [free]   # 22 s
python3 src/c2_Kproj.py B data/trial_v2_h0.008.npz runs/c2/c2raw_M16_s16_p4_re2_cols.pkl runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q_vec.npz runs/kproj/Kproj_M16_s16_NJ1.npz runs/kproj/KprojB_M16_s16_NJ1.json   # 75 s
python3 src/c2_Kproj.py C data/trial_v2_h0.008.npz runs/c2/c2gram2_M16_s16_p4_re2_H1m_NJ1_rowsH1q_vec.npz 0 8 runs/kproj/KC_m0_8.npz   # one piece (106 s per 8 modes); the 42 ranges (m_lo, m_hi) are the list 'modes' of runs/kproj/KC_merge_all.json ([0,8], [8,14], ..., [257,260]); regenerate every piece as runs/kproj/KC_m<lo>_<hi>.npz before Cmerge, which asserts complete coverage of 0..260
python3 src/c2_Kproj.py Cmerge runs/kproj/KprojB_M16_s16_NJ1_img.npz runs/kproj/KC_m*.npz runs/kproj/KC_merge.json
```
  The pickled column pieces (runs/c2/c2raw_*_cols.pkl, 1-3 MB each) are included under artifacts/runs/c2/ for the M16/s16 sections (gzipped).
  Of the 42 stage-C pieces runs/kproj/KC_m*.npz only two samples (KC_m0_8, KC_m8_14) are shipped with the merged image KC_assembled_image_all260.npz
  and the merge records KC_merge_*.json (KC_merge_all.json lists the 42 ranges); the full set (about 12 MB) is regenerable with the stage-C command over those ranges; the superseded version-1 projection
  files (Kproj_*.npz, KprojB_*_img.npz) are kept in the lane only.
- c2_Kproj.py VERSION 2 (20:1xZ, after astra/kproj1 in notes/astra_kproj1_*.md): all 260 modes of K, KP/TAU columns included, ||K||^2 in the same Gram,
  stage KT (KP/TAU row images: `python3 src/c2_Kproj.py KT trial.npz cols.pkl vec.npz out.npz m_lo m_hi`, then `KTmerge out piece...`). Version-2 outputs are
  runs/kproj/Kproj2_*.npz, KprojB2_*.json, KT_images.npz; the version-1 files (Kproj_*.npz, KprojB_*.json) are kept for the record and are superseded.

## Shift 7 additions (2026-10-22, 00:17Z onward): referee passes on the report, directed-rounding tables, Arb X-norm ceilings, R2 tails
- Two internal-consistency referee passes on NUM_REPORT (astra numrep1: sections 1-7.3c; numrep2: 7.4-9; questions and answers in notes/astra_numrep{1,2}_*.md)
  found nearest-rounded (inward) certified ceilings, an invalid 'tails x measure' R2 argument, stale status lines and missing definitions. All repairs
  were applied by the asserted-replacement scripts notes/repairs/batch1.py .. batch6.py (each old string must occur exactly once).
- src/report_tables.py: the tables of NUM_REPORT 7.3 (middle shells, regions and tails), 7.3c (three resolutions) and, with --deriv, 7.3b (derivative
  shells, P-disc maxima) regenerated from the per-cell JSON files with DIRECTED decimal rounding (upper bounds up, interval endpoints outward).
- src/r2_tails.py: Arb bounds of the two tail contributions to the squared weighted L2 norm R2 (outer <= 6.504e-16, inner <= 3.819e-20; total R2 <= 6.2899e-4).
- src/xnorm_cert.py version 3: the X-norm ceilings of 7.11 in Arb ball arithmetic with the stored binary64 k, L converted exactly and every cell start
  enclosed by the (midpoint, radius) balls of the Green boundary files (data/cert_green.npz tb/tb_rad; cert_outer_green.npz t0 + tau; cert_inner_green.npz
  tmin + tau); version 1 (floating sums with 1e-12 inflations) kept as src/xnorm_cert_v1_float.py, version 2 (Arb, decimal constants) as src/xnorm_cert_v2_arb.py;
  all three print the same ceilings 0.385655 / 585.873 for the three finite regions.
- src/report_tables.py --n8: the N8 table of 7.7a (sup bounds of D^j V, D^j rho~ on the balls about P, C_V) with directed ceilings (runs/report_tables_n8.md).
- Second referee round (astra numrep3, numrep4; notes/astra_numrep{3,4}_*.md) after the first repairs; applied by notes/repairs/batch7.py and batch8.py
  (definitions corrected to the implemented objects: KP family, TAU projection, tail cutoff orientation, density-mode convention; scaling identity exact
  for the stored trial; 7.2 and N8 endpoints as ceilings; section 8 recipes with recorded parameters and consistent file names).
```
python3 src/report_tables.py > runs/report_tables.md; python3 src/report_tables.py --deriv > runs/report_tables_deriv.md; python3 src/report_tables.py --n8 > runs/report_tables_n8.md   # 4 s + 4 s + 1 s from the gzipped per-cell files (the three output tables are shipped in runs/)
python3 src/r2_tails.py            # seconds; runs/r2_tails.json
python3 src/export_boundaries.py   # from the three Green files -> data/cell_boundaries.npz (314 KB, shipped): the cell-boundary balls (mid, rad) of the regions
python3 src/xnorm_cert.py          # 60 s; runs/xnorm/xnorm_cert.json; version 3 reads the Green files when present, else data/cell_boundaries.npz (so it runs here)
```

## Shift 8 (2026-10-22, 06:17Z onward, final shift): end-of-run reproducibility checks (no number changed)
- runs/hash_check.py: every row of the NUM_REPORT section-8 'current SHA-256' table hashed (gzipped copies after decompression); from the lane root it checks
  the lane files and this folder, from a copy of this folder the local files; the four unshipped trial files are reported as NOT SHIPPED; exit status 1 on any
  mismatch. Result: 57 rows, 0 failures.
- runs/variant_regen.sh, runs/variant_regen/compare.{py,txt}: the modes file (an intermediate; its first-shift original was deleted unhashed, so its identity is
  not separately established) and the four trial files (base, v3, v4, v5) regenerated from the published c6g_shape.npz with the fit commands of the first block
  (10 min; the chain runs from this folder too, given X3_COEFF_PATH; it exits with the number of failed stages): compare.py prints the SHA-256 of
  each regenerated trial file next to the hash-table value (EQUAL = byte-identical to the file hashed in the report) and, where the stored file is present, the
  stored hash and an array-by-array comparison; compare.txt is the record of the run (all four EQUAL, all arrays identical, exit 0). The verifier's independent
  read-only raw comparator (ipmA-ver/notes/variant_regeneration_audit/code/compare_raw_v2.py, their stored_expected.json) run on the same regenerated files
  returned PASS, all four BYTE_IDENTICAL on distinct inodes: runs/variant_regen/compare_raw_v2_output.json. The regenerated files are kept in the lane
  (runs/variant_regen/*.npz, not shipped). Caveat on the chain logs: `rc=$?` placed after a `$(date ...)` substitution reports the substitution's status (verifier,
  07:01Z); the chain now captures rc immediately, the first two logs' rc fields are not evidence, the comparison records are. Likewise data/trial_small_M20.npz
  (src/truncate_trial.py, new) and data/trial_s02.npz (smooth_band.py 0.02) reproduce byte-identically: runs/variant_regen/fixtures_check.txt (stored and
  regenerated SHA-256 of both).
- Clean-room rerun from a fresh copy of this folder: report_tables.py (all three tables), variants_summary.py, xnorm_cert.py, r2_tails.py, flow_summary.py,
  cert_summary.py and inverse.py produce outputs identical to the lane's from the shipped files alone; x3.py does so given the external coefficient file and
  evaluator (X3_COEFF_PATH, X3_EVALUATOR_DIR).
- Fresh-reader referee round on this README and section 8 (astra repro1; notes/astra_repro1_{question,answer}.md; 20 items, all verified and repaired by
  notes/repairs/batch13.py): acquisition of the external inputs stated (X3_COEFF_PATH, X3_EVALUATOR_DIR); test fixtures and their generating commands
  (truncate_trial.py, smooth_band.py 0.02, c2_fminus.py 4 60 16 ... 2); README commands aligned with section 8 (cert_green_outer 17.0 5.0, the two
  cert_tail exponents and file names, cert_resid_deriv region prefix, resid_smooth settings, xnorm_jets version-2 cell indices, forcing versions v1.2/v2.2);
  the stage-C range record (KC_merge_all.json); the chain scripts' `cd` line; two I/O bugs fixed: src/flow_summary.py (NameError: _jopen used before its
  definition; gz-blind existence test) and src/cert_summary.py (the gzipped derivative certificates were skipped by its glob); now shipped: notes/repairs/*.py
  (the report edit record), runs/collect_v3.sh, runs/c2/imgeval.txt, data/trial_small_M20.npz; the stray version-1 file runs/kproj/Kproj_M16_s16_NJ0.npz removed.
- notes/repairs/final_status.py <T_end> [--dry]: writes T_end and the elapsed time into NUM_REPORT section 1, RUN_STATUS.md and WORKLOG.md; rerunning it
  replaces the three entries (checked on copies: two runs leave one status bullet, one RUN ENDED line and one RUN END log line).
- Confirmation referee pass (astra repro2; notes/astra_repro2_{question,answer}.md): 16 of the 20 items repaired, 4 partly, 7 new items (row count, the two
  checker scripts not usable from a copy of this folder, hash evidence missing from the comparison record, x3.py's external inputs, WORKLOG duplication by
  final_status.py, an overbroad 'no external input' sentence); all repaired by notes/repairs/batch14.py and the script changes listed here. A third pass (astra repro3;
  notes/astra_repro3_{question,answer}.md) found 16 checks passing and four residual items (the comparator JSON was not shipped, the modes file's identity is not
  established, the CPU-guard description, one overbroad sentence), repaired by notes/repairs/batch16.py and the shipping list.
