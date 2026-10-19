You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

# Question: a non-C^3 mode at the source point P of a self-similar IPM profile

Setting. On R^2, with rho even in x and odd in y, solve (c_l X + U).grad rho = rho, U = grad^perp psi, -Delta psi = d_x rho,
rho = x^2 y a, a(0) = 1, c_l = (1 + psi_xy(0))/3. Write W = c_l X + U (div W = 2 c_l, curl W = -rho_x). The profile has
a hyperbolic-free source point P = (x*, 0), x* about 8.6009, where W(P) = 0, W = (A xi, y) + O(|xi|^2 + y^2), xi = x - x*,
A = 2c_l - 1 about 10.1527 (h(P) = d_y W_2(P) = 1). The class of interest is P_2: rho in C^(2,alpha)_loc, rho = x^2 y a near
0 with a continuous (no regularity above C^(2,alpha) is required). Numerically computed profiles (least-squares fits of
a smooth trial: cubic B-splines in a compactified radius times cos(2 m theta), m <= 150) are in the files below.

Local analysis so far (heuristic; please check). With rho = y q(x) + O(y^3), W_1 = w(x) + a_2(x) y^2 + ..., W_2 = y h(x) +
O(y^3), the O(y) parts of the three equations are w q' = (1 - h) q, w' + h = 2 c_l, h' + q' = 2 a_2. At P, with
v = q - g*, g* = rho_y(P), u = 1 - h, F_1 = 2 int_{x*}^x a_2: w v' = u (g* + v), u = v - F_1, linearized A xi v' = g* (v - F_1).
Homogeneous solutions C_+ xi^lam (xi > 0), C_- |xi|^lam (xi < 0), lam = g*/A, h_sing = -q_sing. On the computed profile
g* = 29.7538, A = 10.15272, lam = 2.9306: C^(2,0.93), not C^3. (Your earlier answer on the strip gave the local example
W = (w(xi), y(1 - v(xi))), rho = y(g* + v(xi)), which is the case a_2 = 0.)

Measurement. On every computed profile (five bases, c_l moved along the soft direction by up to 1e-2, and a fit with
c_l fixed at 5.60), H = log a on the axis has a jump of the third x-derivative at x* of about 0.12, measured by separate
polynomial fits on the two sides (windows 0.05 to 0.5, 0.1 to 0.8, 0.2 to 1.2 in |xi|) extrapolated to x*; the same
method gives at most 0.0014 at x* +- 0.8 and x* +- 1.5. From the exported velocity, [q'''] = +3.5 to +3.8 and
[h'''] = -3.0 to -3.4 (ratio -0.79 to -0.95). The trial has no knot at P (nearest knot 0.0065 away; knot spacing
0.0158 near P). Single-window fits of a polynomial plus a |xi|^lam pair do not determine lam (any non-integer lam in
(2.2, 3.5) fits equally well).

Questions.
(a) Check the axis system and the lam-mode, including the claim h_sing = -q_sing at leading order. In the plane: is there
    a consistent local structure, a |n|^lam layer across the weak unstable manifold of P (the characteristic that leaves
    P vertically), with the nonlocal Biot-Savart law (a_2 not 0)? Along that manifold, how does the amplitude evolve, and
    does lam stay fixed? Which precise regularity excludes it (C^3? C^(2,alpha) with alpha > lam - 2?).
(b) Global count. Could these modes give the linearized operator at a P_2 solution extra kernel, so that P_2 solutions
    near the computed one form a family along which c_l varies? Or are C_+ and C_- fixed by global conditions (for
    instance by continuation along the weak manifold to the far field or to the centre)? The fits show a very soft
    direction in c_l (the least-squares objective changes by about 3.6e-3 relative per unit change of c_l, rising to
    twice its minimum only at offsets of about 1e-2), and the c_l value agrees to six digits across bases only because
    the fits descend from one another.
(c) Could the measured jump be an artefact of least squares at P, where w = 0 and the transport residual is weakly
    sensitive to q' (a cubic jump costs about A [q'''] xi^3 / 2 in the residual)? Is the measured ratio [h''']/[q''']
    evidence either way? Propose a decisive numerical test that uses the existing solver (for example a refit from a
    start with the structure removed, or a fit with an extra knot exactly at P).
(d) If the mode is real, how should the trial represent it (singular functions across the weak manifold, with which
    exponent and which cutoff), and what does that predict for the residual next to P? The current near-P residual
    maximum is 2.4e-6 (normalized), located near the axis just left of P (r 8.4 to 8.6, theta < 0.08), oscillating in
    theta at the angular band edge; it did not fall when the angular cap rose from 100 to 150. Is it plausible that this
    strip is the trial's response to the lam-mode, or is it unrelated?

Files (read only): c6d_seg1_shape.npz, c6f_seg1_shape.npz,
c6d_seg1_fields.npz (export: r, theta, x, y, rho, rho_x, rho_y, psi, U1, U2, W1, W2, H, residual, denominator, axis_*),
the soft-direction files tan_c6b_tan{-3e-03,-1e-03,+1e-03,+3e-03}_shape.npz, fixc_c6b_560_shape.npz; the measurement
script axisjump.py (H on the axis from a shape file;
see axis_H). The shape evaluation is in work/c6/stationary.py and centre_fit.py. Please state which statements you
prove and which are heuristic.
