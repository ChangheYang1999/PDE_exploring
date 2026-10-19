You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

Please referee a small set of analytic statements that will appear in the final report of a numerical study of stationary
self-similar IPM profiles on the whole plane. Read these files (they are self-contained; read the parts named below fully):
  FINAL_REPORT.md        sections 1, 2 and 3 (problem, class, velocity law,
                                                                          rigorous results R1 to R12, already refereed)
  final_sec4_draft.md  (draft of section 4, the numerical deliverable)
  analysis.md       sections 13.1, 13.6, 13.7 only
  trial.py        (the explicit trial density, class Trial)
  c4_r1_shape.npz  (one trial: keys k, L, degree,
                                                                          angular, origin_radius, spline_order, spline_knots,
                                                                          singular, z; load with numpy)
Problem: (c_l X + U).grad rho = rho on R^2, U = (-psi_y, psi_x), -Laplace psi = d_x rho, rho even in x and odd in y,
psi odd in x and y, rho = x^2 y a(x,y) near 0 with a even/even and a(0) = 1, c_l = (1 + psi_xy(0))/3, U given by the
canonical sublinear law (V1)-(V3) of FINAL_REPORT section 2, growth (A3) |rho| + (1+|X|)|grad rho| <= C (1+|X|)^gamma,
gamma < 1. W = c_l X + U. The intended endpoint is "YES, strong numerical evidence, for the explicitly distinguished problem
P_2" (FINAL_REPORT section 1: rho in C^{2,alpha}_loc(R^2), rho = x^2 y a near 0 with a only continuous). Results R1 to R12
were refereed before; do not redo them unless you see an error. For each item below give a verdict (correct / correct
with stated repair / wrong / unproved), the exact hypotheses used, and a corrected statement where needed.

1. Inclusions. FINAL_REPORT section 1 defines P_inf by "a is C^infinity near 0" and P_2 as above, both with "the same
   equation, parities, velocity law and growth class". The draft section 4.1 says "P_2 contains every profile of the strong
   setting P_inf". (a) Is that true as P_inf is written, given that section 1 states no regularity of rho away from 0 for
   P_inf? If not, what is the minimal wording (e.g. requiring rho in C^infinity(R^2), or C^{2,alpha}_loc(R^2), in P_inf as
   well) that makes it true, and is that wording faithful to a prompt whose strong setting says only "rho = x^2 y a(x,y)
   near (0,0), a(0,0) = 1, with a smooth and even in both x and y"? (b) Check "P_2 implies rho = x^2 y + o(|X|^3) and is
   strictly stronger than this jet condition (rho = x^2 y + y^5 satisfies the jet condition but is not of the form x^2 y a
   with a continuous)". (c) Is the identity 3 c_l - c = 1 valid in P_2 (a only continuous)? A proof sketch by rescaling
   rho_l(X) = l^-3 rho(lX) -> x^2 y was given by a verifier; check it.

2. Regularity of W. For rho in P_2, is W in C^{2,alpha}_loc (Schauder for -Laplace psi = d_x rho with d_x rho in
   C^{1,alpha}_loc, plus the far-field law)? Is this enough for a C^1 linearization of the flow of W at the hyperbolic
   source P = (x*, 0) of R5 (eigenvalues A = 2c_l - 1 > 1 along x and h(P) = 1 along y), e.g. by Hartman's theorem? Which
   exact version of the C^1 linearization theorem applies (planar case, or the case of a contraction for the backward flow)?

3. The lemma of analysis 13.6 (as audited by a verifier): if rho is C^1 near P, W is C^2 near P, and P is a hyperbolic
   source with A > 1, h(P) > 0, then h(P) = 1 and rho = C eta in C^1 linearizing coordinates (xi, eta). The argument writes
   rho = |xi|^{1/A} F(t), t = eta |xi|^{-h/A}, and uses d_xi rho = (1/A) sgn(xi) |xi|^{1/A - 1} (F - h t F'). Check every
   step, including the case h < 1 (which uses the axis ODE w g' = (1 - h) g, g = rho_y(x, 0), and g ~ x^2 at 0), the case
   h > 1, and whether C = 0 is excluded. State how it relates to R5 and R6 (is it implied by them?).

4. Consistency checks used for a trial (an approximate profile, not an exact one), draft 4.4a and 4.4b:
   (a) for a trial rho odd in y with rho_y(x*, 0) != 0 and W_1(x*, 0) = 0, the transport residual R = W.grad rho - rho
       satisfies R/rho -> h(P) - 1 as X -> P along x = x* (or along any path? state precisely);
   (b) the characteristic defect J(X0) = int (R/rho)(X(s)) ds along the backward characteristic of the trial's own W from
       X0 to the sphere |X - P| = eps diverges like (h(P) - 1) log(1/eps) / (slow eigenvalue) as eps -> 0 when
       h(P) != 1, and has a finite limit when h(P) = 1 (with what regularity of R/rho near P?);
   (c) J(X0) = log rho(X0) - log rho_tr(X0) where rho_tr solves W.grad rho_tr = rho_tr with the trial's W and matches rho
       at P to first order. Is the statement correct, and what is "match at P to first order" precisely?

5. Analysis 13.7 (an identity-free c_l at fixed rho): with rho, hence U, fixed and c_l varying in W = c_l X + U, show or
   refute d h(P)/d c_l |_rho = 1 - h'(P) x*/A with h(x) = d_y W_2(x, 0), h' its x-derivative, A = d_x W_1(x*, 0), and that
   the root of h(P; c_l) = 1 gives a determination of c_l that does not use 3 c_l - c = 1. Is the first-order formula
   c_l^h - c_l = -(h(P) - 1)/(1 - h'(P) x*/A) right?

6. Trial membership (draft 4.1 and (iii)): from trial.py and the npz, rho = x^2 y exp(H) with
   H = ((k - 3)/2) log(1 + r^2/L^2) + sum_m b_m(q) chi^{max(m-1,0)} cos(2 m theta) + (singular term), q = 1 - (1 + r^2/L^2)^{-(1-k)/2},
   chi = r^2/(r^2 + r0^2) (check the code for r units), b_m clamped B-splines of order spline_order in q with first
   coefficient 0, and the singular term s^{p3/2} T(2q - 1) max(cos theta, 0)^{p3 - 2} sin^2 theta, s = r^2/(1 + r^2)
   (check units), p3 = 6 + 2k/(2 - k). Check: (a) a(0) = 1 and a continuous (indeed C^{4,alpha}) at 0; (b) rho in
   C^{4,alpha}_loc(R^2) for some alpha > 0, including along the whole y-axis where the factor |cos theta|^{p3 - 2} is not
   smooth, and at r = 0 for every mode m (is the factor chi^{m-1} times b_m(q) = O(r^2) enough to make
   b_m chi^{m-1} cos(2 m theta) smooth at 0?); (c) the growth (A3) with gamma = k; (d) is rho in P_2 and in A_4? Whether
   the trial lies in P_2 matters because the numerical claim is "an exact P_2 profile exists near the trial". You may
   load the npz and evaluate, e.g., the interior knot multiplicities and spline_order, but keep any computation under
   2 GB and 540 s.

7. Anything in the draft section 4 (final_sec4_draft.md) that states or implies more than is proved, or that is
   logically wrong, e.g. "P_2 contains every profile of P_inf, so a YES for P_2 is not a YES for P_inf", the statement
   of (ii) about B_3, and 4.7.

Please write the answer as a numbered list matching the items, then a short list of the exact text changes you recommend.
