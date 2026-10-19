You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

Please try to COMPUTE a numerical solution of the following problem with a method of your own design, and deliver working code,
data and an honest assessment. Full specification (read it first; it is self-contained):
  SPEC.md   (sections 0-6: conventions, admissible class, velocity law, required
  numerical formulation, diagnostics). Background arguments: analysis.md.

Problem: find rho on R^2 and a scalar c_l with
   (c_l X + U).grad rho = rho,  U = (-psi_y, psi_x),  -Laplace psi = d_x rho,
rho even in x, odd in y, rho = x^2 y a(x,y) near 0 with a even/even and a(0) = 1, and c_l = (1 + psi_xy(0))/3 (not fitted freely).
The velocity must be the canonical sublinear one (SPEC section 3, law V1): for d_x rho = sum_n f_n(r) sin(2n theta),
psi = sum_n psi_n(r) sin(2n theta) with psi_n(r) = (1/(4n)) [ r^{-2n} int_0^r s^{2n+1} f_n ds + r^{2n} int_r^inf s^{1-2n} f_n ds ],
no harmonic term added. Proved facts (SPEC section 4) you may use to design the method and initial guess: c_l > 1 for every
nonzero admissible profile, |rho| <= C (1+r)^{1/c_l}, the origin is a saddle of W = c_l X + U with eigenvalues 1 - 2c_l (x
direction) and 4c_l - 1 (y direction), the first zero x* > 0 of W_1(x,0) is a source with d_x W_1 = 2c_l - 1 and d_y W_2 = 1
there, and rho_y(x,0) > 0 on (0, x*]. Expected: rho > 0 in the open first quadrant, far field rho ~ r^{1/c_l} Theta(theta).
Expected difficulty: smoothness at the origin is probably finite (a term |x|^{p_3} y^3, p_3 = 6 + 2/(2c_l-1), may be present,
singular along the whole y-axis), so do not insist on spectral accuracy in angle near theta = pi/2.

What another team member has tried (all failed so far, for information): Newton on rho = x^2 y w(r) b(r,theta) with Chebyshev in a
compactified radius and sine/cosine modes in angle, continued by a homotopy from a manufactured source term (branch folds,
aliasing); dynamic rescaling rho_tau = rho - (c_l X + U).grad rho with c_l(tau) = (1 + c(tau))/3 started from b = 1 (amplitude
grows, sign changes, blow-up by tau = 5). Ideas not yet tried: (a) dynamic rescaling with BOTH scalings free (fix a numerical
c_l^d, set c_rho(tau) = 3 c_l^d - c(tau) in rho_tau = c_rho rho - (c_l^d X + U).grad rho, which preserves a(0); a stationary state maps
to a profile with c_l = c_l^d / c_rho via rho -> L rho(X/L)/c_rho with L^2 = 1/c_rho, if c_rho > 0); (b) the fixed-W iteration: given
rho_n, compute U_n and c_l = (1 + c_n)/3, solve the LINEAR transport W_n.grad rho = rho (for fixed W its solution space on the
basin of P is one-dimensional, rho = C y exp(-int_{-inf}^0 [W_2/y - 1](Phi_t X) dt)), fix C by a(0) = 1, possibly with damping;
(c) Newton with a good initial guess built from these structural facts; (d) anything else you think better.

Deliverables (in your directory): the script(s); the final candidate as an .npz with grid, rho values and c_l; a short table of
c_l, psi_xy(0) computed two ways, x*, the eigenvalues at P, the transport residual max|W.grad rho - rho| normalized by
max(|rho| + |X.grad rho| + |U.grad rho|) on r <= 2 and on 2 <= r <= 10, at two or more resolutions. If nothing converges, report
precisely what you tried and what happened (numbers), since negative information is also useful. Budget: you have about 100
minutes of wall-clock; single-threaded numpy/scipy, under 2 GB RAM; wrap every shell command in timeout 540 and run longer jobs
in several chunks with checkpoints.
