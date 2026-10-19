You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

Please look for a rigorous nonexistence argument (or a rigorous reason why the natural arguments fail) for stationary
self-similar IPM profiles of the following type. Background files (self-contained; read SPEC.md and notes/analysis.md fully):
  SPEC.md
  analysis.md
  FINAL_REPORT.md   (section 3 lists results already checked by referees)

Problem. Find rho on R^2 and c_l real with (c_l X + U).grad rho = rho, U = (-psi_y, psi_x), -Laplace psi = d_x rho, U given
by the canonical law (U = o(|X|), equivalently the symmetric truncation of the Biot-Savart integral), rho even in x and odd
in y, rho = x^2 y a(x,y) near 0 with a continuous, even/even, a(0) = 1, rho in C^{2,alpha}, and the growth bound
|rho| + (1+|X|)|grad rho| <= C (1+|X|)^gamma with gamma < 1 (class A_2). Known (checked): c_l > 1, rho = O(r^{1/c_l});
3 c_l - c = 1 with c = psi_xy(0) = (1/pi) int rho sin(3 theta) r^{-3} dX; the origin is a saddle of W = c_l X + U with
eigenvalues 1 - 2c_l (x-axis) and 4c_l - 1 (y-axis); P = (x*, 0), the first positive zero of w(x) = W_1(x,0), is a source with
d_x W_1(P) = 2c_l - 1 and d_y W_2(P) = 1; weighted identities (1 + (2 - d) c_l) int rho phi + int rho U.grad phi = 0 for phi
homogeneous of degree -d, 1/c_l + 2 < d < 5; under the hypothesis (Hmin) that the zeros of W in the closed first quadrant
are exactly 0 and P, rho > 0 in the open first quadrant Q. By oddness in y the problem is equivalent to IPM in the upper half
plane with the wall y = 0, psi = 0 on the wall, and density trace rho(x, 0) = 0; the wall gradient g(x) = rho_y(x,0) solves
w g' = (1 - h) g with h = d_y W_2(x,0) = 2c_l - w'(x), and g ~ x^2 at 0, g > 0 on (0, x*].

Motivation (numerical, not proved). Four independent solvers (a dynamic rescaling in time, two Newton/least-squares
spectral solvers, and a characteristics-based fixed-point iteration that enforces d_y W_2(P) = 1 and 3c_l - c = 1 exactly)
all drift toward c_l <= 1 or c_l -> 1+, and none has produced a profile with c_l > 1. This suggests (it does not show)
that there may be no profile in the class.

Tasks.
1. Try to prove c_l <= 1 (equivalently c = psi_xy(0) <= 2) for every profile in A_2, possibly under (Hmin) and positivity,
   which would contradict c_l > 1 and give nonexistence. Natural tools to test, with a verdict on each (works / fails, and
   why, with a concrete counterexample function where it fails):
   (a) the weighted identities above for harmonic phi (for phi = sin(3 theta)/r^3 they give
       int rho U.grad(phi) dX = pi (c_l - 1)(3 c_l - 1), so a proof that this quadratic form is <= 0 for profiles would
       suffice); other homogeneous or non-homogeneous weights, including weights centred at P, and weights adapted to Q;
   (b) the half-plane Poisson representation on the wall, w(x) = c_l x + (2/pi) int_{y'>0} y' (x - x') rho(x',y')
       / ((x - x')^2 + y'^2)^2 dx'dy' (check this formula and its convergence), together with w(x*) = 0, w'(x*) = 2c_l - 1,
       w'(0) = 1 - 2c_l, w < 0 on (0, x*), rho > 0 in Q;
   (c) the invariant density div(W |rho|^{-2 c_l}) = 0 on {rho != 0} and the resulting global first integral on Q;
   (d) energy-type identities (the potential energy int rho y and the Dirichlet energy of psi), localized or weighted so
       that they converge for growth r^{1/c_l};
   (e) any comparison or maximum-principle argument along the wall segment [0, x*] or along the y-axis.
2. If no bound is obtained: is there a formal or rigorous reason that profiles must degenerate as c_l -> 1+ (far field
   rho ~ r^{1/c_l} becomes linear, the canonical velocity law becomes borderline)? Describe the c_l -> 1+ limit: what a
   normalized sequence of profiles could converge to (for example a homogeneous degree-1 stationary IPM state such as
   rho = y, with an inner layer where rho ~ x^2 y), and whether an asymptotic family for c_l = 1 + eps can be written down
   to leading order. State clearly what is proved and what is formal.
3. Check this physical remark: for 0 < c_l < 1 the self-similar solution rho_phys(t,x) = (T-t)^alpha P(x/(T-t)^beta),
   alpha = 1/(c_l - 1), beta = alpha + 1, is not a blowup (its gradient at the centre tends to 0 as t -> T when
   c_l > 1/3), so profiles with c_l < 1 obtained with a renormalized velocity law would not describe singularity formation.
Give each item a verdict: PROVED (with complete proof), FAILS (with the reason and a counterexample), CONDITIONAL (state
the condition), or FORMAL. Plain precise mathematics, no em-dashes.
