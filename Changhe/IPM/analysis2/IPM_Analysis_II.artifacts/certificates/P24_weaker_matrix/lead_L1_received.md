# L1 (PROPOSED). The weighted low inverse needs only a position-dependent matrix floor far below 19/5

Status: PROPOSED by the lead, not yet independently checked. Written 2026-10-28T07:11Z.

## Statement

Let c, rho, u, M, sigma = 11/5, R, d, w_R = (1 + r^2/R^2)^(-sigma/2) and the decay constants C_rho, C_U, C_DU, C_D2U be
as in the weighted low inverse (07_weighted/LOW_INVERSE_PROOF.md for R = 2^200 and delta = 2/5; 17_weight_radius/PROOF.md
section 2 for d = 4/9; 20_real_velocity/PROOF.md section 4 for R = 2^31). Recall

    M = (2c+1) I + sym Du + [[rho_y, -rho_x/2], [-rho_x/2, 0]],
    b0 = -sigma c t,  t = r^2/(R^2 + r^2).

Replace the matrix part "M >= (19/5) I at every point" of hypothesis (W1) by

    (W1') lambda_min(M(X)) >= 2/5 + sigma c |X|^2/(R^2 + |X|^2)   for every |X| <= R.

Nothing is assumed about M on |X| > R beyond the decay constants already in (W1). Then every conclusion of the weighted
low inverse holds with the same margin formula: at R = 2^31 with the tuple (186, 22, 22, 56), the low margin is still

    2/5 - R^-d [22 + (1 + 21/2) 186 + (11/5)(9*22 + 2*22 + 56/sqrt(2))] > 14093/70000 > 1/5,

and hence Theorem D_w (topics 18 and 20: s = 3*2^-31, ball 5*2^-32, threshold 2^-35, high inverse 40, low inverse 6)
holds under (W0), (Wn), (W1'), the decay part of (W1), (W2), (W3), (Wm), (Ws) with unchanged constants.

A sufficient, position-free form of (W1') is lambda_min(M) >= 2/5 + (11/10) c on |X| <= R (2.3914 for state 131).
Near the core (W1') is essentially lambda_min(M) >= 2/5: at |X| <= R/1000 the extra term is below 2.2 c 10^-6.

## Proof

1. The only use of the matrix floor in the low-energy argument is the region r <= R of identity (3) of
   LOW_INVERSE_PROOF.md,

       -<w_R L_fix h, phi> = int q^T (M + b I) q - (1/2) int Delta b phi^2 - <D_R g, phi>,   b = b0 + b1.

   The b1 part (velocity part of the weight) and the commutator D_R are estimated there, and in the later radius
   reductions, without using M. The region r >= R uses M >= (2c + 1 - (C_DU + C_rho) R^-d) I, which follows from the
   decay constants alone, since |M - (2c+1) I| <= |Du| + |D rho| <= (C_DU + C_rho) r^-d.

2. On r <= R: t = 1 - R^2/(R^2 + r^2), and for f = (R^2 + r^2)^-1 one has Delta f = 4 (r^2 - R^2)/(R^2 + r^2)^3, so
   Delta t = 4 R^2 (R^2 - r^2)/(R^2 + r^2)^3 >= 0 and Delta b0 = -sigma c Delta t <= 0. Hence the b0 part of the
   integrand on r <= R is

       q^T (M + b0 I) q - (1/2) Delta b0 phi^2 >= (lambda_min(M) - sigma c t) |q|^2 >= (2/5) |q|^2

   pointwise under (W1'). The proof in LOW_INVERSE_PROOF.md bounds the same expression below by
   (19/5 - (11/10) c)|q|^2 and then only uses that this is at least (2/5)|q|^2 (the outer baseline 1 - (31/100) c is the
   binding one, and the stated margin is 2/5 minus the losses). So the margin formula, and every later step that uses
   only the margin (the generator, the graph core, the inverse integral, the fractional transfer of topics 17, 18, 20),
   is unchanged.

3. Consistency with the vertical-axis ceiling of 22_axis_constraints/PROOF.md: M(0) = diag(3c + a0, c + 2), so no
   reference has a global floor above c + 2 = 3.8103; (W1') asks for at most 2/5 + (11/10) c = 2.3914 < c + 2.

## Consequences (to be stated only after confirmation)

- The hypothesis that the two projected refits A2 and A3 were found to violate at (0, 1) (lambda_min(M) = 2.2225 and
  3.1352 < 19/5) is not needed for Theorem D_w: at |X| = 1 the floor in (W1') is 2/5 + sigma c 2^-62. The distance
  bounds of 22_axis_constraints remain true as stated but concern the stronger floor 19/5.
- The exact-profile axis condition of 22_axis_constraints (K <= c + 2 - kappa) weakens from K <= 0.0103 (kappa = 19/5)
  to K <= c + 2 - 2/5 - sigma c t, about 3.41 near the core.
- For the checkpoint nothing changes (it satisfies M >= 19/5). The unweighted Theorem D (variant b) and the quasilinear
  proof of 09_quasilinear use the floor 19/5 as a decay rate and are not affected by this proposal.
- (W1') is a pointwise condition on a bounded region: the decay bound gives lambda_min(M) >= 2c + 1 - (C_DU + C_rho) r^-d,
  which exceeds 2/5 + (11/10) c as soon as (C_DU + C_rho) r^-d <= 3/5 + (9/10) c; for the tuple (186, 22, 22, 56)
  this holds for r >= 27057, so a certificate is needed only on r <= 27057.

## What remains for a candidate reference

(W1') is one of several pointwise hypotheses. A candidate must still satisfy (W2) (the weighted principal matrices
M1, M2 >= I/2), the global derivative bounds (W3), the decay constants of (W1) and above all the smallness (Ws). For A2
and A3 the certified residual lower bounds N^w_s(F) > 13/10 and > 2/3 remain the decisive failure.
