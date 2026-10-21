# First-investigation reproduction recipes

These are the original section 5 command recipes and their parameter descriptions.
They require the separately published first-investigation artifacts; that complete
bundle is not included in this staged follow-up. Follow the first-investigation
README for the working directories of parts (a) to (f). The follow-up README
gives commands for the programs and candidate data included here.

The accompanying artifacts of sections 4 and 5 are those of the first investigation, published as
IPM_Setting_I.artifacts/; those of the follow-up (section 6) are published separately as
IPM_Setting_I.followup.artifacts/ (6.0). The first investigation's accompanying artifacts are arranged in six parts, (a) to (f); the file README.md at their top level lists the
directories of each part, maps the names of the fits used here (X1, X2, X3, F0 to F3, the rows of 4.3 to 4.5) to the
coefficient files and gives the commands below with paths relative to the artifacts. The records of the research run
itself (work logs, job drivers and queues, per-run solver logs) are not included.
(a) Trial coefficient files. One file per trial named in section 4: the candidate X3 and every fit of the tables of 4.3
    (the nested pair included), the free fit of the same trial space, the resolution rows at the candidate's c_l, the
    free resolution study (215, 244, 302, 375 radial functions with m <= 100, 375 with m <= 150), the soft-direction and
    fixed-c_l studies (with the two continued fits of the fixed-c_l profile, 4.3), the budget row, the m <= 250 row, its
    free control and its continuation with rows to 9000 L (4.4), X3 continued with the inverse domain at 1e4 L (4.5),
    and the bounded-domain fits with the free control of the 9000 L row and the 9000 L row continued (4.4, 4.5). The
    candidate X3 is c6g_shape.npz (md5 15f8095f7e79dbfa0c50d75e5fe8997a) and its control F3 is c6gF_shape.npz (md5
    0398af3f08a2a4f75e42c846edbaa375). A file holds the spline knots and order, the coefficient of every
    radial x angular function, the fractional-power coefficients, k = 1/c_l, L, c_l and the origin radius. The files of
    the candidate, its control, X2, F2, F0, F1, X1 and the start of X1 are the verified files byte for byte; in the
    other files a solver restart vector that no evaluator reads was removed for size, every other field unchanged (the
    md5 of each file as published and as verified is listed with them). Start files of continued fits are not included:
    the m <= 200 starts are the m <= 150 ends with the new angular coefficients set to zero, and the shifted starts are
    made by the transplant scripts of (b). The generator that evaluates rho, psi, U and the residuals from a
    coefficient file is in the same part.
(b) The fit: the Gauss-Newton / LSQR solvers (free and fixed-c_l), the GPU driver and the scan and export programs.
    The solvers log the objective, c_l, h(P), x*, centre jet E_c and D2 at each check; these run logs are not included.
    The fits X2, F2, X3, F3, the m <= 100 rows, the domain columns, the free control of the 9000 L row and the 9000 L
    row continued (4.5), the budget row, the m <= 250 row, its free control and its continuation with rows to 9000 L
    (4.4), X3 continued with the inverse domain at 1e4 L (4.5), the fixed-c_l profile with its two continued fits and
    the nested pair of 4.3 were computed with the same iteration, and the solver-setting arms of 4.2 with their stated
    changes, with the matrix-vector products, the vector updates of LSQR and the column-scaling probes carried out on a
    GPU, the products by a port of the CPU operator. Every table of the port is copied from the CPU objects. On the full
    fit grid it agrees with the CPU operator to 3e-14 relative in the products and 1e-13 in the adjoint products. The
    linearization, the acceptance test at each check (the CPU objective) and the saved coefficient files use the CPU
    code. Started from the same shape, the first linearization reproduced the CPU objective to 5e-5 relative after 250
    iterations. LSQR paths differ at the 1e-4 level after hundreds of iterations, so "equal budget" means equal
    iteration counts at the same relinearization schedule on the same backend (on the GPU 2500 iterations per
    linearization, damping 1e-8, check every 250), with two departures. On the CPU X1 ran 750 iterations over two
    linearizations (500 + 250) and F1 750 iterations in one linearization (--inner 2500), both stopped by the 1.8 h cap;
    the pairs X1 / F1, and through their starts X2 / F2 and X3 / F3, are therefore equal in iteration count but differ
    in the relinearization schedule of their first 750 iterations. The fits of the fixed-c_l profile of 4.3 are compared
    with X2 and F2 at equal total count: each runs 21500 iterations on the GPU, while X2 and F2 are the 750 CPU
    iterations of X1 and F1 followed by 20750 on the GPU. The CPU logs record under "predicted" the LSQR estimate
    |phibar|, which omits the damping term. The linear residual of the damped problem is sqrt(phibar^2 + res2), with
    res2 the sum of the squared damping rotations; the GPU logs record that value for every run from F2 on (the log of
    X2 has |phibar| only). The acceptance test always used the true objective. In each linearization the three long-fit
    drivers (long_solve.py, long_solve_fixcl.py and gpu_long_solve.py) scale the LSQR columns by the inverse square root
    of a stochastic estimate of the squared column norms of the Jacobian from 24 Rademacher probe vectors (seed 8128
    plus the linearization count); a column whose estimate is below 1e-18 of the largest gets scale 0 and is not moved
    in that linearization, and with c_l held fixed the column of k = 1/c_l gets scale 0 in every linearization. Every
    residual quoted is evaluated from the saved files by the evaluators of (c) and (d).
(c) The lead's between-node evaluation (scans by radial band and strip, both normalizations; the scan program
    quick_scan.py is with the fit code of (b)), the characteristic-defect code and the original-form B_3 evaluator, with
    their outputs for every trial of (a) (the larger outputs xz-compressed); and the far-field diagnostic of 4.5 (the
    forced and the stored first far-field correction from a coefficient file, on seven fits and on the domain fit with
    rows to 9000 L, with its outputs).
(d) The separately written generator and residual evaluator (own differentiation, own full-plane inverse), its audit
    wrappers and auxiliary scripts, the far-field checks of 4.5 (far1_ver.py, far2_ver.py, farP.py), the reference
    outputs of steps 1 and 2 below on the candidate (runs/reference), and the verification record that the appendix
    summarizes, copied after its last entry.
(e) The independent discretization of 4.6: solver, report; and the velocity check of 4.5 by real-space quadrature of the
    analytic source (52 sample points), with its outputs.
(f) The specification of the problem classes and diagnostics, the analysis notes behind section 3 with their audit
    record, and the external referee questions and answers (including the answer on the far-field identity of 4.5).

Reproduction of the headline numbers. All commands are single-threaded on the CPU (OMP_NUM_THREADS=1; the GPU driver of
step 5 also uses one GPU), with the software versions of section 0 (Python 3.9.25, numpy 2.0.2, scipy 1.13.1, and
PyTorch 2.8.0 for the GPU driver); the times are on one core of the machine used for the run. The wrappers of steps 1
and 2 stop a step after 2400 s (vaudit.py in gen_audit.sh) or 1200 s (mk_traces.py, vd14.py and vzeros.py in
extra_checks.sh), so a slower machine may need larger limits. Peak resident memory of the commands of steps 1 to 3 on
the candidate: 13.8 GiB for gen_audit.sh at 16875 x 768, the configuration with the most evaluation points (12.3 GiB at
22500 x 512, 9.2 GiB at 16875 x 512 and at 22500 x 384, 7.0 GiB at 16875 x 384, 4.7 GiB at 11250 x 384), and at most 7.5
GiB for each command of steps 2 and 3. They ran under an address-space limit of 15.3 GiB (ulimit -v 16000000), and every
output for which an earlier one exists equals it in every number (file names and timings aside): for steps 1 and 2 the
earlier outputs are in runs/reference of (d), for step 3 they are the candidate's scan files in (c). Step 1 at
16875 x 384, which section 4 does not use, had no earlier output; runs/reference holds the one from this measurement.
<coef> is a coefficient file from (a), <tag> any label. Paths in the commands are relative to the named directory of the
accompanying artifacts.
1. Residual tables of 4.4 by the separate evaluator (maxima of R/N_f and R/N_v by region, J, h(P) - 1), in the code
   directory of (d):
     bash gen_audit.sh <coef> <tag> "7.652e-4 7.652e6 11250 384 479;7.652e-4 7.652e6 16875 384 479;7.652e-4 7.652e6 16875 512 639;7.652e-4 7.652e6 16875 768 959;7.652e-4 7.652e6 22500 384 479;7.652e-4 7.652e6 22500 512 639"
   Each group is one configuration (inner radius, outer radius R of the inverse, radial nodes N, angular nodes, maximal
   mode); 2 to 8 minutes each. Output: runs/audit/<tag>_N<N>_q<nq>_R<R>.json and .log in (d).
2. Identity c_l = (1 + psi_xy(0))/3, the identity-free root of h(P) = 1 at fixed rho, the centre relations E_c and D2,
   and the zeros of W on the axes, same directory:
     bash extra_checks.sh <coef> <tag> "7.652e-4 7.652e6 11250 384 479"
   about 2 minutes; output runs/audit/<tag>_extra.log. The verifier's B_3 estimator on the traces this step writes:
     python3 vb3ibp.py ../runs/gen4/<tag>_traces.npz
   (the wrapper deletes the generated field and keeps the traces).
   The characteristic defect on the 857-label set of 4.4b and the axis integral I(eps) with the profile q0, same
   directory (the generated field is 52 MB and is deleted afterwards):
     python3 gen_shape.py <coef> 7.652e-4 7.652e6 16875 384 ../runs/gen4/<tag>.npz
     python3 vaxis.py ../runs/gen4/<tag>.npz 479 ../runs/audit/<tag>_ax.json
     python3 vchar_dense.py ../runs/gen4/<tag>.npz 479 20 737 60 1e-4 ../runs/audit/<tag>_jd2.json
   about 7 seconds, 2 minutes and 6 minutes; the arguments of vchar_dense.py are the maximal mode, the label radius, the
   number of uniform labels, the number of labels next to each axis and the smallest geometric distance from the axis.
3. The lead's scans, in (b) with the generator of (a) on the path:
     python3 quick_scan.py <coef> 32768 640 out.json
     python3 quick_scan.py <coef> 24576 960 out960.json
   under 30 seconds each on the candidate. They read the trial in its fit's own convention (the two-term closure at
   1000 L, 4.4) and on the candidate print whole-box N_f maxima 6.94e-7 and 7.27e-7 next to P (4.1).
4. The lead's characteristic defect (185 uniform labels, a cross-check of step 2) and the original-form B_3 from an
   export (the export is about 1.4 GB and is not included; it is regenerated): with <name>_shape.npz in the working
   directory of (b),
     python3 export_fit.py <name> 24576 576
     python3 char_defect.py <name>_fields.npz 20 185
     python3 b3_ibp.py <name>_fields.npz mu1only
   (char_defect.py and b3_ibp.py are in (c)); on the candidate the export took about 80 seconds, b3_ibp.py under 15
   seconds and char_defect.py with 185 labels about 30 seconds. b3_ibp.py prints two forms per variant: "orig", the
   original form of R10, which is the lead value quoted in section 4, and "ibp", an integration by parts whose end piece
   does not converge in the quadrature order n (it moves by about +0.008 from n 40 to n 80 on the candidate); the "ibp"
   values are not quoted.
5. The fit itself, from its start file (the free fit moved by -1e-3 in c_l along its soft direction, also in (a)):
     python3 long_solve_fixcl.py <start> <out> --fix-cl --nr 20480 --nt 720 --hours 1.8 --inner 500 --check 250
   The free control F1 is segment 2 of the free run, from the free fit:
     python3 long_solve.py <free fit> <out> --nr 20480 --nt 720 --hours 1.8 --inner 2500 --check 250
   Both were stopped by the 1.8 h cap after 750 iterations, X1 over two linearizations (500 + 250) and F1 in one.
   The continuations X2, F2, X3, F3 use the GPU driver of (b):
     python3 gpu_long_solve.py <start> <out> --nr 20480 --nt 720 --hours 4.9 --inner 2500 --check 250 --fix-cl --max-its 20750 --damping 1e-8
   (--nt 960 for X3 and F3; without --fix-cl for F2 and F3). X2 and F2 were run with --hours 0.75 and no --max-its; the
   time cap stopped both at the check after 20750 iterations, the schedule that --max-its 20750 reproduces. The m <= 200
   starts are the m <= 150 ends with the new angular coefficients set to zero (make_angular.py in (b); the density is
   unchanged, residual difference 1.5e-15). The domain columns of 4.4 are the X3 end continued with the same driver and
   settings at --nt 960 with --fit-radius 90 or --fit-radius 300, and at --nt 960 on a 24576-point radial grid with
   --fit-radius 9000: the rows are then r < fit radius (in units of L) and the inverse domain is the fit radius / 0.9,
   with the two-term closure beyond; without the option the rows are r < 900 L and the inverse domain r <= 1000 L.
6. The velocity check of 4.5, in (e): an export of the coefficient file with the generator of (a)
     python3 export_fit.py <name> 24576 576
   (about 80 seconds; it writes <name>_fields.npz, regenerable and not included), then
     python3 raycheck.py cand <name>_shape.npz <name>_fields.npz out.json "Smax:1e18,smode:adapt,phimax:0.02,pcluster:1" full
   (about 32 minutes on X3 for the 52 points). It prints, per point, both velocities, their difference and the implied
   change of the normalized residual.
7. The far-field diagnostic of 4.5, in (c), with the generator of (a) on the path:
     python3 far1_axis.py <coef>            (axis limit of the forced and the stored first correction; seconds)
     python3 far1.py <coef>                 (the angular profile of both; seconds)
     python3 far1_check.py <coef> <export>; python3 far1_split.py <coef> <export>   (comparison with an export of step 6)
     python3 far2.py <coef>                 (the third-order series of R / N_v and its sums at the radii of 4.5; about 1 minute)
   and the measured far residual against that series, with the inverse continued to 1e7 L, run in the directory of the
   domain-fit code of (b) with ptest.py taken from (c) (it writes an export and deletes it afterwards; about 3 minutes):
     python3 <dir of (c)>/ptest.py <coef> 24576 576 1e7 out.json
   and, in the same way, the far-band maxima of |R| / N_v over 1000 L < r <= 9000 L, 9000 L < r <= 1e4 L and r > 1e4 L,
   with the inverse computed to <Rinv> L and the two-term exterior beyond (1e4 is the own convention of the domain fit
   with rows to 9000 L, 1e6 continues the formula; a cross-check of the band rows of 4.5 from (d); about 80 seconds, 4.8
   GB):
     python3 <dir of (c)>/band_nv.py <coef> 24576 576 <Rinv> out.json
Outstanding experiment (partly done). One refinement step of the experiment that would separate the two pictures of 4.8
was run: the fixed-c_l fits at 5.6004662 and 5.5683739 continued from m <= 150 to m <= 200 (4.3, 4.8); by the rule fixed
before the run its result is undecided (Q = 1.680 against the thresholds 1.36 and 3.05), so the two pictures are not
separated. Further nested discretizations at several separated exponents, with budgets large enough to estimate the
optimization error, were not run. The other rows of the fixed-c_l profile of 4.3 are on one basis (375 x m <= 150) at
one budget (21500 iterations), and the angular sequence m <= 150, 200, 250 at the candidate's c_l mixes approximation
and budget.

