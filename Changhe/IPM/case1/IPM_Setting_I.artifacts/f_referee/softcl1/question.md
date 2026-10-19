You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

Please referee a heuristic about how well a numerical self-similar profile determines its scaling exponent c_l, and say
how its c_l uncertainty can be estimated and stated honestly. Background (read section 13 of the analysis file fully;
sections 2 and 3 for the setting):
  analysis.md   (section 13, in particular 13.1, 13.6, 13.9, 13.10)
  FINAL_REPORT.md       (sections 1 to 3: problem, class, proved results)
  VERIFY_REPORT.md       (items G37 and G38 near the end: the soft direction)

Problem. Find rho on R^2 and c_l with (c_l X + U).grad rho = rho, U = (-psi_y, psi_x), -Laplace psi = d_x rho, U = o(|X|)
(canonical law), rho even in x, odd in y, rho = x^2 y a near 0 with a(0) = 1, rho in C^{2,alpha}, growth below |X|^1.
Proved: 3 c_l - c = 1 with c = psi_xy(0); the origin is a saddle of W = c_l X + U; P = (x*, 0) (first positive zero of
W_1(x,0)) is a hyperbolic source with eigenvalues A = 2 c_l - 1 (x direction) and h(P) = d_y W_2(P) = 1 (y direction);
every characteristic of the open first quadrant leaves P; C^1 regularity at P forces rho = C eta near P in linearizing
coordinates (no label-dependent factor; analysis 13.6).

Numerical situation (all numbers numerical, none proved). Trials rho = x^2 y exp(H) (splines in a compactified radius,
cos(2 m theta), m <= 100), with c_l tied to the trial by 3 c_l - c = 1 through an exact scaling, fitted by damped LSQR on
normalized transport rows plus a row for h(P) - 1 and two centre rows. c_l is about 5.57636, A about 10.15.
- Two fits whose c_l differ by 3.1e-5 have the same near-P residual maximum (1.8e-5 normalized) to 1 percent; they differ
  by a smooth global deformation with |d log rho|/|d c_l| of order 1 (VERIFY_REPORT G37).
- Halving the radial knot spacing near P lowers the near-P maximum by about 5 per halving, together with the label spread
  of the characteristic defect J (J(X0) = int_{-inf}^0 (R/rho)(Phi_s X0) ds along the backward characteristic of the
  trial's own W, R = W.grad rho - rho; spread over 8 start points on r = 20: 1.7e-5 at 215 radial functions, 3.9e-6 at
  244). The fits' c_l moves by only 1e-7 per segment: LSQR does not move along the soft direction.
- An independent solver (other discretization) finds the cheapest c_l direction costs 3.2e-3 in its residual 2-norm per
  unit c_l against a floor 6e-4, and characteristic rows have sensitivity about 0.01 per unit c_l along that direction.

The heuristic (analysis 13.10): at c = c* + d there is a nearby equation solution rho_d smooth away from P with a
label-dependent factor at P of size s|d|; a smooth trial can remove that factor over a transition window of time T along
each characteristic, at residual cost s|d|/T, and T can grow (logarithmically in the resolution near P, plus the path
length), so residual norms pin c_l only to about (floor) T/s. The label part of J is independent of where the residual is
placed along a path, so c_l - c* is estimated to first order by <J - mean J, S>/<S, S>, S = dJ/dc_l along the soft
direction, measured on shapes along a computed tangent (linearized fixed-c least squares).

Tasks (give a verdict on each: correct / wrong / conditional, with the reason and, where wrong, a concrete counterexample):
1. Is the construction of 13.10 (a) sound: does it produce smooth admissible trials at c* + d with sup-norm residual
   O(s|d|/T)? What does the nonlocal feedback (the change of U caused by exp(-phi)) do to that estimate: can it be
   absorbed by the linear tangent problem, or does it give an O(|d|) residual that no choice of phi removes?
2. Does this make the range of the linearized operator non-closed in the c direction (so that c_l is not determined by
   residual minimization in the limit of infinite resolution), or does the log growth of T only make the problem badly
   conditioned? Relate it to the order-zero symbol remark of G38 (b) if relevant.
3. Is the J-pattern estimator of 13.10 (c) a sound first-order estimate of c_l - c* under the hypotheses of 13.9
   (nondegenerate exact profile)? Its failure modes? Is a better c_l estimator available from data we have (exported
   fields: rho, W, R on a polar grid; the characteristic integrator), e.g. a dual-weighted residual for the functional c_l?
4. What can honestly be claimed about c_l in a report that presents numerical evidence (not a proof) for a profile:
   which numbers (spread of fits, J/S estimate, residual-curve bounds, identity-free determinations) count as evidence of
   accuracy, and which only as consistency checks?
Keep the answer self-contained; state what you checked by calculation and what you only argued.
