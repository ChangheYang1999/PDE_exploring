You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 4 GB RAM (export OMP_NUM_THREADS=1). Write files only in your current directory. Do not modify any other file.

Question: why does a fitted self-similar profile carry an angular band-edge oscillation next to the x-axis just left of the stagnation point P, and what representation (or what value of the scaling exponent) removes it?

Problem. Find rho on R^2 and c_l with (c_l X + U).grad rho = rho, U = (-psi_y, psi_x), -Laplace psi = d_x rho, U = o(|X|),
rho even in x, odd in y, rho = x^2 y a near 0 with a(0) = 1; the identity c_l = (1 + psi_xy(0))/3 holds. W = c_l X + U.
On y = 0, W_2 = 0; W_1 has a zero P = (x*, 0), x* about 8.6008 (in the physical units below). At P (a source), W = (A xi, h y)
+ ..., xi = x - x*, A = 2 c_l - 1 about 10.15, and h = h(P) = 1 is required for C^1 at P (notes 13.1, 13.6). Along the axis
between P and the origin the flow goes from P toward 0 (0 is a saddle: incoming along the x-axis, outgoing along the y-axis).
Read for the setting: analysis.md sections 13 (13.1, 13.5a, 13.6,
13.14, 13.15) and FINAL_REPORT.md sections 1 to 3.

Trial. H = log(rho / (x^2 y)) = sum_m sum_j c_mj B_j(q(r)) chi(r)^(m-1) cos(2 m theta) + (centre singular terms), splines
B_j in a mapped radius, m <= 100 or m <= 150; c_l is a free parameter (or held fixed). Fitted by least squares of the
residual res = c_l (3 + r H_r) + L^2 Uadv - 1 (Uadv the velocity terms) on a 20480 x 720 grid; the flux-normalized
residual R / (|W_1 rho_x| + |W_2 rho_y| + |rho|) is the quoted norm. Code (read-only for you; you may import it):
stationary.py, centre_fit.py (load_shape(path, nr, nt) returns
(s, z); s.evaluate(z) returns (_, fields, L2, res, den)); example evaluator
strip_signed.py and strip_radial.py (physical r = s.p.r * sqrt(L2)).
Shapes (read-only): c6f_seg1_shape.npz (m <= 150),
c6d_seg1_shape.npz (m <= 100), fixc_c6f_m1.0e-03_shape.npz (c_l held 1e-3 lower, refitted), and the unrefitted shifted
trials trd_{-3e-3,-1e-3,+1e-3}_shape.npz (c6d plus d t along the soft
c_l direction t). A 2048 x 720 evaluation takes about 1 GB; 8192 x 1440 a few GB.

Measured facts (lead notes 13.15; verifier VERIFY_REPORT G61, G63 at VERIFY_REPORT.md):
 (1) The global maximum of the normalized residual (2.4e-6; elsewhere near P 4e-7 to 7e-7, bulk 1e-7 to 7e-7) sits in
     theta < 0.08, physical r 8.4 to 8.6 (just left of P), as an oscillation in theta whose zero spacing is that of
     cos(2 M theta) with M about 0.9 times the angular cap (0.0117 on m <= 150, 0.0170 on m <= 100).
 (2) Raising the cap 100 -> 150 lowers the near-axis residual by 3 to 5 times for 6.6 <= r <= 8.3 and leaves it at 2.2e-6
     to 2.4e-6 for 8.4 <= r <= 8.6: the unresolved zone moves toward P (from |xi| < 1 to |xi| < 0.2) without decreasing.
 (3) The H content the cap step added is confined to theta < 0.08, has nearly the same angular profile at every r in
     7.6 to 8.56, grows toward P and changes sign at P. The angular spectrum of H at r 8.47 decays roughly like m^-3.4;
     right of P it decays much faster.
 (4) The amplitude depends on c_l along the soft direction: lobe 2.9e-6 / 2.2e-6 / 1.8e-6 at c_l offsets +1e-3 / 0 / -1e-3
     (unrefitted), the alternating pattern breaks up at -3e-3; a refit with c_l held at -1e-3 gives 1.5e-6 after 250 LSQR
     iterations (control pending). The L2 objective prefers the higher c_l (5.57636); the max norm and the characteristic
     defect J (notes 13.4) prefer c_l 1e-3 to 2e-3 lower.
 (5) The one far-field label whose backward characteristic reaches P along the axis from the left is the outlier of J.

What I ask:
 (a) For an exact solution in the class with h(P) = 1 and rho C^1 at P (so Phi constant in 13.1): is H smooth near P and
     on the axis segment left of P? Derive the expansion of H near P and near the axis left of P from the transport
     structure (resonances between A and 1, possible log or |xi|^(k/A) terms, the role of the axis being the incoming
     separatrix of the saddle at 0). State precisely what regularity in (r, theta) the exact H has at r in (x* - 0.3, x*),
     theta -> 0, and what that implies for the decay of its cos(2 m theta) coefficients.
 (b) Explain facts (1) to (5). Candidate mechanisms to confirm or refute (or replace): (i) a complex or real singularity
     of the trial (not of the solution) at P seen from circles r < x*; (ii) the fit using non-smooth-at-P content
     (Phi-mode-like, notes 13.1 to 13.3) because it is cheap in the least-squares objective, with an amplitude that
     depends on c_l and vanishes near the c_l of the smooth solution; (iii) something in the trial's angular basis near
     theta = 0 (the factor chi^(m-1), the polar coordinates) that makes an otherwise smooth near-axis structure hard to
     represent. Use the shapes: compute the signed angular profile of H (or of its change between the files) next to the
     axis left and right of P and fit its local form (for example as a function of y / |xi|^(1/A), of theta / |xi|, or of
     log|y|). Give testable predictions with numbers.
 (c) Propose a concrete change of the trial (functions or coordinates near the axis next to P; for example angular
     functions in a stretched angle concentrated at theta = 0 for r near x*, or near-axis layer functions in
     (xi, y)) that would let a least-squares fit lower the strip below 1e-6, or argue that a fixed c_l offset is the
     remedy. Estimate what resolution it needs.
 (d) Is there an identity-free criterion for c_l from this structure (for example the c_l at which the non-smooth
     near-axis content vanishes)? How sharp would it be, given facts (4)?
Answer in plain mathematics. Separate what you proved, what you computed (with the numbers), and what is heuristic.
