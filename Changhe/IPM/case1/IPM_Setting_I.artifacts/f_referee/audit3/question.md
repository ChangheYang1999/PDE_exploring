You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

Please referee two new analytic claims about stationary self-similar IPM profiles on the whole plane, and then try one
constructive question. Read these files fully; they are self-contained:
  SPEC.md            (problem, admissible class, velocity law, lemmas)
  analysis.md  (arguments; sections 7.3 and 8 are the new items)
and the test scripts
  test_b3_wonly.py
  test_b3_compatible.py
  b3_diag.py   (imported by the tests; copy all three to your directory)

Problem: (c_l X + U).grad rho = rho on R^2, U = (-psi_y, psi_x), -Laplace psi = d_x rho, rho even in x and odd in y,
rho = x^2 y a(x,y) near 0 with a(0) = 1, c_l unknown, 3 c_l - psi_xy(0) = 1, A = 2 c_l - 1 > 1, P = (x*, 0) the first
positive zero of w(x) = W_1(x,0), W = c_l X + U. Axis data: h = d_y W_2(x,0), a2 = d_y^2 W_1(x,0)/2, b3 = d_y^3 W_2(x,0)/6,
g = rho_y(x,0); G_3 = d_y^3 rho(x,0)/6 solves w G_3' + (3h - 1) G_3 = F_3 := -a2 g' - b3 g, and B_3 is the coefficient of
|x|^{p_3}, p_3 = 6 + 2/A, in the solution bounded at P (analysis.md 3.2; a previous referee found 3.2 correct for smooth
axis data). The axis constraints w' + h = 2 c_l, a2' + 3 b3 = 0, h' - 2 a2 = -g' (from div W = 2 c_l and curl U = -rho_x)
were confirmed by that referee.

1. analysis.md 7.3. Check: (a) H := N g^{3+2/A} |w|^{-2/A} solves w H' + (3h - 1) H = 0 given g'/g = (w' - A)/w; its
   normalization H ~ x^{p_3} at 0 with N = A^{2/A}/g0^{3+2/A}; (b) the identity -F_3/(wH) = (1/(3N)) (a2/g^3)' m^{2/A-1},
   m = |w|/g; (c) the resulting finite-part formula for B_3 in terms of c_l and w only, its special case at A = 2, and the
   integration-by-parts form for 1 < A < 2 (boundary terms at 0 and at x*, finite part, absence of logarithms). Run the two
   test scripts (timeout 540 python3 ...) and say whether they test what they claim.
2. analysis.md section 8 (Lemma 8: the limit c_l -> infinity is degenerate). Check the rescaling F = rho/c_l, the limit
   problem (X + U[F]).grad F = 0 with psi_xy[F](0) = 3, and the proof that it has no C^1 solution with U = o(|X|) and
   finitely many zeros of X + U[F]. In particular: the Poincare-Bendixson step for alpha-limits on the whole plane with
   finitely many equilibria; the flux argument excluding periodic orbits and graphics (including figure-eight type graphics);
   continuity at the limit equilibrium. Also state precisely what kind of convergence of a sequence of solutions with
   c_l -> infinity would let one pass to the limit (U[F_n] -> U[F] and psi_xy[F_n](0) -> psi_xy[F](0)), given that rho grows
   like r^{1/c_l} at infinity.
3. Constructive. Using the formula of 7.3 and any further exact relation of the coupled problem you can derive (the
   transport equation and the Biot-Savart law restricted to the x-axis, the identity 3 c_l - psi_xy(0) = 1, positivity of
   g on (0, x*] and of rho in the open first quadrant, h(P) = 1, sign of w on (0, x*)), is there an argument that B_3 != 0
   for every profile in the class, or at least a sign for B_3 in a range of c_l? If not, explain what extra information
   would be needed. If you find a new exact relation among the axis data (for example one coming from the Biot-Savart law,
   which is nonlocal), state it with proof.
Give each item a verdict: CORRECT, CORRECT WITH REPAIR (give the repair), CONDITIONAL (state the condition), or WRONG (give a
counterexample or the error). Plain precise mathematics, no em-dashes.
