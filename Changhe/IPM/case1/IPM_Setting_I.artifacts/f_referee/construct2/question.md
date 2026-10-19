You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

You are an independent numerical analyst, consulted by another researcher. Be skeptical, concrete and complete; say plainly
when something fails or is only indicative. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node,
npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap every shell command in `timeout 540` (run long computations as bounded,
checkpointed chunks); single-threaded computations (OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1) under 2 GB RAM each, at most
two at once. Write files only in your current directory; you may READ the files listed below. Keep your directory under 3 GB.

Problem (self-contained statement; details in the files). Find rho on R^2 and c_l > 0 with
  (c_l X + U) . grad rho = rho,   U = (-psi_y, psi_x),   -Laplace psi = d_x rho,
U given by the canonical law (U = o(|X|); equivalently the symmetric truncation of the Biot-Savart integral), rho even in x
and odd in y, rho = x^2 y a(x,y) near 0 with a(0) = 1, sublinear growth |rho| + (1+|X|)|grad rho| <= C(1+|X|)^gamma, gamma < 1.
Necessary relations: 3 c_l - c = 1 with c = psi_xy(0); P = (x*, 0), the first positive zero of w(x) = W_1(x,0), is a source with
d_x W_1(P) = 2c_l - 1 =: A and d_y W_2(P) = 1. At the center, rho generically contains B_3 |x|^{p3} y^3 with p3 = 6 + 2/A.

Files to read first:
  SPEC.md                (spec; diagnostics D1-D11)
  analysis.md      (sections 3, 7.2, 7.3, 9.4: axis equations, B_3)
  REPORT.md, README.md, PROOF.md and its code
      (stationary.py, solver.py, linearized.py, diagnose.py, axis_checks.py, ...), final_shape.npz, final_candidate.npz.
  b3_ls.py, b3_diag.py (finite-part B_3 from axis traces),
      resid_bands.py, axis_layer.py, jet_check.py (lead diagnostics; run them on your exports).
You may copy any of this code into your directory and modify it.

Status of the previous candidate (construct1, c_l = 5.5763219, x* = 8.60088). Lead findings on final_candidate.npz:
 (1) Pointwise residual: max |residual/denominator| = 3.3e-5 next to P (r = 8.68, theta = 0.25), 1.7e-5 in the band
     theta < 0.05 near P, 1e-6 to 3e-6 elsewhere; with the normalization |W1 rho_x| + |W2 rho_y| + |rho| it is 1.2e-4 next
     to P. Under basis refinement (radial degree 120, 160, 200) the near-P maximum went 1.4e-4, 6.0e-5, 3.3e-5 and c_l went
     5.5763606, 5.5763231, 5.5763219.
 (2) Jet defect: write rho = y g(x) + y^3 G3(x) + O(y^5), W1 = w + y^2 a2 + ..., W2 = y h + y^3 b3 + ... on the x-axis.
     The y^3 coefficient of W.grad rho - rho is T3 = w G3' + (3h - 1) G3 + a2 g' + b3 g, which must vanish. For the
     construct1 exports T3 / (scale of its terms) is 2e-2 to 9e-2 on (0, x*): the trial function's y^3 jet is wrong by
     several percent in a thin layer along the x-axis, which the least-squares objective barely sees (the residual
     divided by rho sees T3 only as y^2 T3 / g).
 (3) B_3 inconsistency: the finite-part value computed from w, h, a2, b3, g alone (scripts/b3_ls.py) is
     B_3 = (3.7 +- 0.3)e-5, stable over the three bases; the trial function's own singular coefficient is
     B3_ansatz = 5.5e-6. For an exact solution these coincide. The disagreement is the jet defect (2).
 (4) D9 (int_0^{x*} (1/g - 1/x^2) dx = 1/x*) has relative defect 8.6e-4, dominated by near-center accuracy.

Task: produce an improved candidate, starting from construct1's final_shape.npz, and report honestly.
 A. Objective. Keep the canonical velocity law and the c_l / scale construction of construct1 (no added harmonic terms).
    Add to the least-squares objective, with weights you justify:
    (i) the axis equations on the x-axis at orders y^1 and y^3 (and y^5 if cheap), i.e. the G1 equation
        w g' + (h - 1) g = 0 and T3 = 0, normalized by the size of their terms, on a dense set of points in (0, R);
        and the analogous x^2 and x^4 orders on the y-axis;
    (ii) extra transport rows on a local grid around P (for example polar about P, radii 1e-3 to 2), and rows for the
        gradient of the normalized residual there, to penalize the nearly-null non-smooth modes at P
        (homogeneous solutions |xi|^{1/A} G(eta/|xi|^{1/A}) of the linearization at P, xi = x - x*, eta = y);
    (iii) keep the source condition d_y W_2(P) = 1 and the six singular |x|^{p3} y^3 functions free.
 B. Convergence study in the trial space: at least three successively larger bases (radial and angular), each optimized
    to stagnation, giving for each: c_l, x*, h(P), B3_ansatz, the finite-part B_3 from scripts/b3_ls.py (delta 0.4 and 0.5,
    degree 10 to 14), the T3 defect profile, D9, and the pointwise and regional residuals (both normalizations) by region
    (r <= 2, 2 <= r <= 10, 10 <= r <= 1000, |X - P| < 1, theta < 0.05). For the final basis, the construct1-style
    quadrature/domain study (3 grids x 3 domains, two tails) and the FD elliptic residual.
 C. Targets (report which are met): pointwise normalized residual <= 1e-6 everywhere including near P; T3 defect
    <= 1e-4 relative; B3_ansatz and the finite-part B_3 agreeing to 5 percent, or a clear statement that they do not;
    D9 defect <= 1e-5. If B_3 converges to a nonzero value with both measurements agreeing, say so with error bars; if
    it tends to 0, say so. Never call the result a proof.
 D. New diagnostic D13 (claim to check): with Z = X - P and a circular principal value about P,
    PV int rho |Z|^{-3} sin(3 arg Z) dX = pi (1 - c_l + g(P)/4), g(P) = rho_y(x*, 0). Evaluate both sides.
 E. Exports in your directory, same array names and conventions as construct1's final_candidate.npz (including all
    axis_* arrays) for each basis of B (name them basis1_fields.npz, basis2_fields.npz, ...; keep the largest files
    compressed and delete intermediate field files you do not need), the final global trial function as final_shape.npz,
    and a REPORT.md with tables. Write REPORT.md incrementally (update it after each basis) so that partial results
    survive if you run out of time.
State in the answer, for every number, which file and which command produced it.
