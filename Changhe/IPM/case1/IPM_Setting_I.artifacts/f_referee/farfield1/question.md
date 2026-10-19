You are an independent mathematical researcher and referee, consulted by another researcher working on the problem described below. Be skeptical, concrete and complete; check every step you rely on; say plainly when something is wrong, unproved, or only conditional. Your final message is your answer: make it self-contained.

Machine rules (no exceptions): never start a server or anything that listens on a port; never run JavaScript tooling (node, npm, npx, pnpm, yarn, vite, playwright); no GPU; wrap shell commands in `timeout 540`; single-threaded computations under 2 GB RAM. Write files only in your current directory. Do not modify any other file.

Question:

# Audit: first-order far-field consistency of a trial density for a self-similar IPM profile

Setting. On R^2, with rho even in x and odd in y, solve W.grad rho = rho with W = c_l X + U, X = (x, y), U = grad^perp psi
= (-psi_y, psi_x), -Delta psi = d_x rho (psi the canonical full-plane inverse; U = O(r^k) at infinity, no added harmonic
polynomial), rho = x^2 y a, a(0) = 1, c_l = (1 + psi_xy(0))/3. Write k = 1/c_l. For the trial below c_l = 5.5753626106,
k = 0.17936053, L = 7.6514246. Polar coordinates (r, theta), theta in [0, pi/2] in the first quadrant (extended by the
symmetries); U_r = -(1/r) psi_theta, U_theta = psi_r. The transport residual of a trial density is R = W.grad rho - rho
with U computed from the trial density itself. Normalization N_v = |rho| + |X.grad rho| + |U.grad rho|.

Trial family. u = r/L, q = 1 - (1 + u^2)^(-(1-k)/2), s = u^2/(1 + u^2), chi = u^2/(u^2 + r_0^2), r_0 = 0.02,
p_3 = 6 + 2k/(2 - k),
   rho_h = x^2 y exp(H),
   H = ((k - 3)/2) log(1 + u^2) + sum_{m=0}^{200} chi^max(m-1,0) b_m(q) cos(2 m theta) + s^(p_3/2) cos(theta)^(p_3 - 2)
       sin(theta)^2 T(2q - 1),
b_m clamped splines in q on [0, 1] (degree 7), T a Chebyshev polynomial. The last interior spline knot is at
q = 0.99330416 (r = 446 L). Residual rows of the fits are r < 900 L; the velocity is computed on r <= 1000 L with a
two-term far-field closure beyond. Coefficients (read-only, optional spot checks):
c6g_shape.npz, read by
trial.py (class Trial); the computation below is
far1.py. Read-only; write only in your own directory.

Claims to audit.

C1 (formal far-field orders). Assume rho = r^k Theta_0(theta) [1 + r^(k-1) Theta_1(theta) + O(r^(2k-2))] and
psi = r^(k+1) F(theta) + O(r^(2k)), differentiable term by term. Then
 (a) -[(k+1)^2 F + F''] = g := k cos(theta) Theta_0 - sin(theta) Theta_0', and with F = sum F_n sin(2 n theta),
     g = sum G_n sin(2 n theta): F_n = G_n / (4 n^2 - (k+1)^2), n >= 1;
 (b) order r^k of the transport equation gives c_l = 1/k with Theta_0 free;
 (c) order r^(2k-1) gives (c_l - 1) Theta_0 Theta_1 = (k+1) F Theta_0' - k F' Theta_0, so Theta_1 is forced by Theta_0;
 (d) every higher order j is algebraic in the j-th term: j (1 - c_l) rho_j + [U.grad rho]_j = 0; the core enters U only at
     O(r^(-3)); for this k there is no resonance (log term) in the first three orders.
 Please check signs, the parity of F, whether the excluded harmonics are excluded correctly, (d), and whether the
 right side of (c) vanishes at theta = 0 and pi/2 to the order of Theta_0 (Theta_0 ~ cos^2 near pi/2 times the T factor).

C2 (formula side). For the trial family, 1 - q = u^(k-1) (1 + O(u^(-2))), so
   Theta_0 = L^(3-k) cos^2 sin exp(sum b_m(1) cos 2m theta + T(1) sin^2 cos^(p_3-2)),
   Theta_1 (formula) = -L^(1-k) (sum b_m'(1) cos 2m theta + 2 T'(1) sin^2 cos^(p_3-2)),
 with T' the derivative in the Chebyshev variable. Is this right, including the factor 2 and the claim that the chi, s and
 (1 + u^2) corrections enter only at relative O(u^(-2))?

C3 (leading far residual). Writing Theta_1e for the Theta_1 of C1(c) evaluated on the formula's Theta_0 and Theta_1f for
the formula's, R = (c_l - 1) r^(2k-1) Theta_0 (Theta_1e - Theta_1f) + O(r^(3k-2) Theta_0) and
R / N_v = C(theta) r^(k-1) / (1 + k) + O(r^(2k-2)), C = (c_l - 1)(Theta_1e - Theta_1f). Is this right? Does it need
U - U_0 = O(r^(2k-1)) with U_0 = (-r^k F', (k+1) r^k F) for the trial's own velocity, and is that implied by C2?

C4 (numbers and reading). Computed: max over theta of |Theta_1e - Theta_1f| = 4.083e-3 at theta = 1.5696 (Theta_1f
= -42.3 there), at most 7.9e-4 for 0.05 < theta < 1.4, the same to 4 digits for 2^14, 2^15, 2^16 FFT points;
C(1.565) = +0.0186; the same within 6 percent on six other fits of the same family (including one with rows only to
90 L). On an independent export of this trial (velocity from the trial itself, r to 1e4 L): (U - U_0) relative to
max |U_theta,0| is 1.84e-3, 7.47e-4, 4.91e-4 (U_theta) and 2.84e-2, 1.16e-2, 7.60e-3 (U_r) at 1000, 3000, 4999 L; on the
column theta = 1.5681, R / N_v = 1.99e-7, 7.37e-7, 1.09e-6, 1.00e-6, 9.45e-7 at 1000, 2000, 4701, 7998, 9503 L against
the leading term C r^(k-1)/(1+k) = 1.03e-5, 5.82e-6, 2.89e-6, 1.87e-6, 1.62e-6 (same sign); at theta = 0.818,
-2.2e-7 vs -3.1e-7 (4701 L) and -1.8e-7 vs -1.8e-7 (9503 L). The far-band maximum of R/N_v of the trial is 1.1e-6 next
to the y-axis at r about 3.6e4 (4700 L).
 Proposed reading: inside the fit rows the fit balances the leading term against higher orders; beyond them the residual
 turns toward C r^(k-1)/(1+k); the far band is a first-order far-field inconsistency of the representation (relative 1e-4
 in Theta_1), common to all fits because the slopes b_m'(1), T'(1) belong to the polynomial on the last knot interval
 (r > 446 L), which no fit constrains beyond 900 L, and it decays at infinity. Is the reading supported? Is the slow
 approach (ratio 0.02 to 0.58 over 1000 to 9500 L) consistent with a second term of relative order r^(k-1), or does it
 point to something else (for example, the velocity closure at 1e4 L in the export)? Is the agreement of C across fits,
 including the 90 L fit, consistent with the explanation?

C5 (fix and prediction). (a) Is imposing C1(c) at q = 1 a constraint linear in (b'(1), T'(1)) for given (b(1), T(1)),
and is Theta_1e representable in that span (cos 2m theta, m <= 200, plus the single singular term) to 1e-5 near the
axis? (b) Prediction fixed before a fit with rows to 9000 L is read: on that fit, N_v over r > 1e4 L changes against
the trial by the same factor as max |Theta_1e - Theta_1f| next to the axis, within 30 percent. Is this a sound
prediction, or should the factor be compared with something else?

For each claim give a verdict line first (CORRECT / CORRECT WITH QUALIFICATION / WRONG), then the reasoning, then the
corrected statement if any. Spot checks on the npz file are welcome where they decide something; say what you computed.
Nothing here is claimed as a theorem about a solution; C1 is formal under the stated expansion.
