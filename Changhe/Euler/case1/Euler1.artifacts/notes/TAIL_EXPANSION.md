# Far-field expansion versus the tail representation (notes from astra consultation 'tailexp1', 2026-10-23 07:20Z)

Source: astra/tailexp1/answer.md and astra/tailexp1/euler-tail/PROOF.md (independent referee, GPT-6 astra). These are CLAIMS
to be checked (the verifier lane may audit them); they are used here only to choose representation branches.

Claims (formal expansions, not asymptotic theorems; assume U = O(R^d), grad U = O(R^(d-1))):
1. With delta = 1/c_l in (2, 2.5), the admissible formal velocity degrees are 1 - w with w in {q delta + s : q >= 1, s in {0} or
   s >= 5} together with the integers w >= 5; pressure degrees 2 - w (w != delta). Pure nonlinear branch: U degrees d, 2d-1,
   3d-2, ...; P degrees 2d, 3d-1, 4d-2, ... with U_{n+1} = (F_n + grad P_n)/(n+1), F_n = sum_{i+j=n} (U_i.grad) U_j.
2. Homogeneous decaying solutions of the linearized exterior problem: degree d (angular freedom A_0 with div_S2 A_0T + (d+2) A_0r = 0,
   constant pressure) and harmonic multipole pairs with pressure R^(-l-1) Y_lm and velocity degree -l-2. Global smoothness and
   decay kill the monopole and dipole (l = 0, 1), so the first such pair has velocity degree -4 (quadrupole), then -5, ...
   Q symmetry requires even m; odd l is allowed. These coefficients are free exterior matching data, fixed by the whole profile.
3. R^(d-2) and R^(2d-3) are NOT genuine terms. The smooth envelope rho^a N(xi) produces an extraneous R^(d-2) velocity coefficient
   unless d_r N_0 = (d+1) N_0 on |xi| = 1; its residual, normalized by R^(2d-1), GROWS like R^(delta-2). The network must learn the
   cancellation (the nonlinear-scale loss penalizes it strongly at large R).
4. Logarithms: at resonant exponents (first: c_l = 3/7 ~ 0.4286 with pressure degree -5, l = 4; next 4/9 ~ 0.4444) a pure-power
   expansion is inconsistent and R^p log R terms are forced; near these values pure-power coefficients have small denominators.
5. Representation consequences for the target 1e-5 nonlinear-scale residual at R <= 1e3:
   - omitting BOTH members of a multipole pair costs only O(R^(delta-5)) (1e-9 .. 3e-8 at R = 1e3): not needed;
   - omitting the third pure term U_2 (degree 3d-2) leaves E / R^(2d-1) = O(R^(d-1)) = O(R^(-delta)): 6e-3 at R = 10, 4e-5 at
     R = 100, 2.5e-7 at R = 1e3. So a third potential term of degree 3d-1 (pressure 4d-2) is needed for R in [3, 100].
   - trainable c_l: d/dc of rho^(alpha d + beta) = (alpha / c^2) log(rho) rho^(...): sensitivity grows like log R (no singularity).

Decision for the campaign: the v2 sweep keeps n_tail = 2 (degrees d+1, 2d for A; 2d, 3d-1 for P); the refinement series uses
n_tail = 3 (adds A degree 3d-1 and P degree 4d-2; euler_ss/model.py produces exactly these for n_tail = 3). The comparison
n_tail = 2 vs 3 is the prompt's 'tail-model refinement' test. Multipole terms (integer degrees) are not added unless a branch
shows a residual plateau between R = 3 and 100 that the n_tail = 3 model cannot remove.
