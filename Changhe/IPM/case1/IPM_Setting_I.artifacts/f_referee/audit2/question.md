You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

Please referee new analytic claims about stationary self-similar IPM profiles on the whole plane. Read these two files fully; they are
self-contained:
  SPEC.md            (problem, admissible class, velocity law, lemma statements)
  analysis.md  (arguments; each item carries a status tag)
and the script
  b3_diag.py (numerical evaluation of the coefficient B_3).
Problem: (c_l X + U).grad rho = rho on R^2, U = (-psi_y, psi_x), -Laplace psi = d_x rho, rho even in x and odd in y,
rho = x^2 y a(x,y) near 0 with a(0) = 1, c_l unknown, 3 c_l - psi_xy(0) = 1, U given by the canonical sublinear law (SPEC section 3).
A previous referee already checked SPEC v1 (velocity law, Lemma 1, Lemma 3, fixed-W rigidity, exponents, weighted identity); those
items are tagged AUDITED-1 and you need not redo them unless you see an error. Focus on the items NOT yet audited:

1. analysis.md 2.2 (center relation and saddle; the rescaling proof) and 2.3 (no cycles; alpha-limits; index count): correct?
   Exactly which hypotheses are used?
2. analysis.md 2.5 (positivity rho > 0 in the open first quadrant under the hypothesis Hmin): check every step, in particular
   (i) "alpha(X) = 0 would put X on the y-axis", (ii) the use of the fixed-W rigidity on the basin of P, (iii) the y-axis
   statements rho(0,y) = 0 and d_x^2 rho(0,y) > 0, and the regularity they need.
3. analysis.md 3.2 (B_3 as a finite-part integral over [0, x*]): is G_3 = H(x) int_x^{x*} [-F_3/(w H)] dt the unique solution
   bounded at P? Is B_3 = f.p. int_0^{x*} [-F_3/(w H)] dt exactly the coefficient of x^{p_3} in G_3 (with H ~ x^{p_3} at 0)?
   Is the finite part free of logarithms when p_3 is not an even integer (including p_3 = 7, i.e. c_l = 3/2)? Check that F_3
   is even and that -F_3/(wH) = x^{1-p_3} (even series) near 0. Check the script b3_diag.py: its manufactured test, the exact
   Beta-function value of B_3, and the finite-part algorithm (FFT Taylor coefficients on a circle plus Gauss-Jacobi). Run it
   (timeout 540 python3 b3_diag.py; copy it to your directory first).
4. analysis.md 3.3 (transversal formulation): with C^infinity symmetric linearizing coordinates (xi, eta), is every solution
   vanishing on the x-axis of the form rho = |xi|^{-1/|lambda1|} Fhat(eta |xi|^{lambda2/|lambda1|})? Is "rho in C^infinity near
   0 iff F_j = 0 for every j >= 3 with p_j not an even integer" right? Is the claim that a nonzero F_3 produces a singularity
   of type |x|^{p_3} along the WHOLE positive y-axis (not only at 0) correct? If the linearization is only C^k (W in C^N with
   N finite, which is the realistic case because U inherits the singularity of rho along the y-axis), what can be said about
   the 2D regularity of rho: is it true that B_3 != 0 implies rho in C^{floor(p_3)} but not in C^{ceil(p_3)} near 0? A proof
   or a counterexample would be very valuable.
5. analysis.md 3.4 (counting heuristic) and section 5 (problem variants): is the heuristic stated honestly? Is there a
   structural reason (symmetry, conservation law, an identity of the coupled problem) that would force B_3 = 0 for every
   C^4 profile? Try to find one or explain why none is apparent.
6. analysis.md 4.2 and 4.4 and anything else that is wrong, unjustified, or relies on a hidden assumption.
Give each item a verdict: CORRECT, CORRECT WITH REPAIR (give the repair), CONDITIONAL (state the condition), or WRONG (give a
counterexample). Use numerical or symbolic checks where useful (python3 with numpy/scipy/sympy is available).
