You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

# Audit: an identity relating two measurements of a fractional coefficient B_3 on an approximate profile

Setting. On R^2, rho is even in x and odd in y. W = c_l X + U, X = (x, y), U = (-psi_y, psi_x) for a stream function psi
(for the problem, -Delta psi = d_x rho, but below only div U = 0 is used). A profile solves W.grad rho = rho. A "trial" is
a smooth explicit rho for which the residual W.grad rho - rho is small but nonzero; U is computed from it. Constants:
c_l > 1 (about 5.575 in the application), A = 2 c_l - 1, beta = 2/A in (0, 2), p_3 = 6 + beta, which lies in (6, 8)
and is never an even integer. On the positive x-axis the field W has zeros at 0 and at a single point x* > 0 (w < 0 on
(0, x*), w has a simple zero at x*).

Axis expansions (at (x, 0), x in (0, x*]):
  rho = y g(x) + y^3 G3(x) + O(y^5),  W_1 = w(x) + y^2 a2(x) + O(y^4),  W_2 = y h(x) + y^3 b3(x) + O(y^5).
The y^1 and y^3 coefficients of W.grad rho - rho on the axis are
  T1 = w g' + (h - 1) g,
  T3 = w G3' + (3h - 1) G3 + a2 g' + b3 g.
For an exact profile T1 = T3 = 0. Normalization a(0) = 1 where rho = x^2 y a, so g = x^2 (1 + O(x^2)); w = -A x (1 + O(x^2))
near 0 (this uses c_l = (1 + psi_xy(0))/3, satisfied by the trial to about 3e-9; take it as exact).

Known result for exact profiles (call it R10). With H = N g^(3+beta) |w|^(-beta), N = A^beta (so H ~ x^(p_3) at 0), the
coefficient B_3 of the homogeneous solution x^(p_3)(1 + ...) in G3 is
  B_3 = (1/(3N)) f.p. int_0^{x*} (a2/g^3)' m^(beta - 1) dx,   m = |w|/g,
where f.p. is the Hadamard finite part at 0 (the integrand has an expansion x^(-p_3 - 1)(k0 + k2 x^2 + k4 x^4) + O(x^(5 - p_3))
... in powers x^(2j - 1 - p_3) plus an integrable remainder; the finite part removes the divergent powers). For an exact profile
the derivation uses T1 = 0 (so H is the homogeneous solution of the G3 equation), w' + h = 2 c_l and a2' + 3 b3 = 0.

Claims to audit (all are about a TRIAL, where T1, T3 != 0):

(1) For every trial, w' + h = 2 c_l and a2' + 3 b3 = 0 hold exactly (orders y^0 and y^2 of div W = 2 c_l, since div U = 0).

(2) Pointwise on (0, x*), with H = N g^(3+beta) |w|^(-beta) (R10's function built from the trial's g and w) and
    F3 = -a2 g' - b3 g:
      -F3/(w H) = -(G3/H)' + (T3 - (3 + beta) (G3/g) T1)/(w H).
    Proof sketch: H'/H = (3 + beta) g'/g - beta w'/w; g'/g = (1 - h)/w + T1/(g w); w' = 2 c_l - h; 2 c_l beta = 2 + beta; so
    w H'/H = 1 - 3h + (3 + beta) T1/g, and (G3/H)' = (w G3' + (3h - 1) G3 - (3 + beta) G3 T1/g)/(w H).

(3) Using b3 = -a2'/3: -F3/(w H) = (1/(3N)) (a2/g^3)' m^(beta - 1). So R10's formula evaluated on the trial's axis data
    (g, w, a2) equals f.p. int_0^{x*} -F3/(w H) dx.

(4) Suppose G3 = E(x) + B_own x^(p_3) (1 + o(1)) near 0 with E having an even expansion c2 x^2 + c4 x^4 + c6 x^6 + O(x^8), G3
    finite at x*, and the defect integrand (T3 - (3 + beta)(G3/g) T1)/(w H) having a finite-part expansion at 0 in the same
    family of powers. Then
      [R10's formula on the trial's axis data] = B_own + f.p. int_0^{x*} (T3 - (3 + beta)(G3/g) T1)/(w H) dx,
    because f.p. int_0^{x*} -(G3/H)' dx = B_own (G3/H = c2 x^(2 - p_3) + c4 x^(4 - p_3) + c6 x^(6 - p_3) + B_own + o(1) at 0,
    G3/H -> 0 at x* since beta > 0).

(5) Consequently the wording "the estimator from the trial's axis data equals its own coefficient plus the finite part of
    int_0^{x*} D/(w H) dx, where D = T3 is the defect in the y^3 coefficient and H is R10's function" is WRONG when T1 != 0;
    the correct statement needs the combination T3 - (3 + beta)(G3/g) T1, i.e. the defects in both the y^1 and the y^3
    coefficients. (An alternative correct statement uses instead the homogeneous solution H_h of the trial's own equation,
    H_h'/H_h = (1 - 3h)/w, H_h ~ x^(p_3); then only T3 appears, but H_h is not R10's function when T1 != 0, and R10's formula
    is not f.p. int -F3/(w H_h).)

Please check (1) to (5) line by line, including signs (w < 0 on (0, x*)), the normalization N = A^beta for g0 = 1, the claim
that H ~ x^(p_3) exactly to leading order, the finite-part step in (4) (are there hidden assumptions, e.g. about o(1) terms,
logarithms, or the behaviour at x*, where |w|^(beta - 1) is integrable since beta - 1 > -1?), and whether the alternative in
(5) is also correct. Also: is the finite part in (4) independent of how the divergent powers are removed (it is a sum of
powers with exponents 2 - p_3, 4 - p_3, 6 - p_3, all non-integer)? State for each claim CORRECT / WRONG / CONDITIONAL (with
the condition). Give a corrected statement where needed. A short symbolic check (sympy) is welcome.
