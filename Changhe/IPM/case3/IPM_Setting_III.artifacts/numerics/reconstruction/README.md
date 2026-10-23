# Reconstruction package for the saved states cited in the report (lead 07:40Z request; shift 4)

Contents
- `states/*.pt`: the saved coefficient files (torch pickles; keys documented in `load_state.py`).  `SHA256SUMS.txt` lists their SHA-256 hashes
  (verify with `sha256sum -c SHA256SUMS.txt` from this directory).  The first eight hex digits are the hash prefixes used in the report.
- `load_state.py`: standalone loader / evaluator.  It rebuilds the discretisation from the saved parameters (imports the solver modules from `../src`),
  recomputes the canonical velocity with the modal Green-function inverse (the archived copies in ../src, SHA-256 in SHA256SUMS_SRC.txt), and prints a0 = rho_y(0), c = psi_xy(0), the centre defect c_l + c - 1, the
  y-axis far-field amplitude K, the cubic origin coefficients b, e (Q states), the between-node sampled maxima of |R|, |R|/N_f, |R|/N_v by region with
  the maximising coordinates, and rho, rho_x, rho_y, U_1, U_2, psi, R, N_f, N_v at requested points (x, y).  Definitions are in the docstring and in
  NUM_REPORT section 7.  Usage:
      python3 load_state.py states/r1C_cl3.0_N128.pt                          # default points (0.5,0.5), (3,0), (0,3), (6,8), (30,40)
      python3 load_state.py states/r1C_cl3.0_N128.pt --points '1,2;-0.5,0.5;0.1,0.3' --json out.json --device cuda   # any quadrant; parities applied
- `RECONSTRUCTION_OUTPUT.txt`: the output of `load_state.py` for every state in `states/` (produced by `run_all.sh`), i.e. the reproduced a0, c, K, b, e
  and sampled residual maxima that the report tables quote (NUM_REPORT 4L(c12)-(c14), (c18), 4O(l); FINAL_REPORT 4.3(b), 4.7(a)-(c)).
- `run_all.sh`: the loop that produced `RECONSTRUCTION_OUTPUT.txt`.

States (see SHA256SUMS.txt for full hashes)
- fixed c_l = 3 chain (NUM_REPORT 4L(c12)-(c14), FINAL_REPORT 4.7(c)): r1C_cl3.0_N64.pt, _N96, _N128, _N160, _N192 (smooth Q basis, least-squares
  collocation at 3M angles, gauge gK = 20, forcing width Lf = 0.25 inherited from the start; produced by src/q_free.py with fixcl=3.0, see artifacts/README.md
  "Shift 3").
- fixed c_l = 2.5 chain: r1C_cl2.5_N64.pt, _N96, _N128.
- forced sheet-1 states of FINAL_REPORT 4.3(b) (ipm3 representation, forcing mu y phi(r), phi = (1 + r^2)^-2, gauge: far-field angular mean of b):
  (c_l, beta, eps) = (3, 1, 1) at 96 x 48: rf_s1_cl3.0_N96M48.pt (mu = 1.9806606230, a0 = 1.1384875215, c = -0.2602702396 in the report);
  (1.5, 4, 1) at 96 x 48: rf_s1_cl1.5_b4_N96M48.pt (mu = 0.3427813925, a0 = 2.1236082776; NUM_REPORT 4F 'State B').  For forced states the loader
  reports R_f = R - mu y phi.
- the four rebuilt-map free-c_l iterates of FINAL_REPORT 4.7(a): e861227a = qfree_cl1.5_N64_Lf0.25.pt, 4fa3641d = qfree_cl1.5_N96_Lf0.125.pt,
  06f24d76 = qfree_cl1.5_N96_Lf0.25.pt, 709d48d4 = qfree_cl1.5_N128_Lf0.25.pt;
- the six further states of 4.7(a): c3f17dc2 = qfixF_cl1.2_N64.pt, 31bcc7b5 = qfixF_cl1.2_N96.pt, 1083cfed = qfixF_cl1.1_N64.pt,
  548d12fe = qfixF_cl1.2_N128.pt, 777ccdba = qfreeF_cl1.5_N64.pt, 48d5cecb = qfreeF_ref2_N96.pt.

Caveats.  The evaluations are the producer's (discrete inverse of the saved density, evaluated through its Chebyshev-trigonometric representation);
the verifier's canonical evaluations of the same densities are larger by factors 3 .. 11 near the x-axis at the maximisers for the unconverged fixed-c_l
states (NUM_REPORT 4L(c14), verifier result 143).  Hashes of the source code at the time of the historical optimizer runs were not recorded; the
reproduction here is of the evaluation of the saved coefficients, not a bitwise replay of the runs.  Software: Python 3.9.25, numpy 2.0.2, scipy 1.13.1,
torch 2.8.0+cu128.

Scope notes (verifier result 181 and referee dr3, 08:1xZ): the printed maximising coordinates belong to max |R| (or |R_f|) only; the point rows print the
UNFORCED residual R and, for forced states, an extra column R_f = R - mu y phi; the printed c_l + c - 1 is the unforced centre defect, the forced origin
defect a0 (c_l + c - 1) - mu is printed separately for forced states; the sample set is finite (midpoints in t and in angle, four near-axis angles, the y-axis;
radii beyond 1e120 discarded), so the maxima are sampled maxima, not suprema or tail bounds; the inverse's angular oversampling M2 is taken from the saved
options when present (3M for the fixed-c_l chains), otherwise the default M + 2; frozen-map Q states report their effective far-field exponent; the output
supplies a0, K, b, e in the ORIGINAL gauge (the re-gauged table of NUM_REPORT 4O(l) divides b, e by l^2 with l = (a0/K)^(1/(1-gamma))); run_all.sh's DONE
marker does not certify that every evaluation succeeded (check RECONSTRUCTION_OUTPUT.txt for tracebacks); torch.load uses map_location='cpu'.
