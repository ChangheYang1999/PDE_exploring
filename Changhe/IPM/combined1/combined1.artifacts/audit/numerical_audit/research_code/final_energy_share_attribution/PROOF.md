# Energy shares in the frozen final report

## Statement and hypotheses

Let F be the exact residual of C1-N1-007 at the fixed c in N4-180. Retain its full-plane quantities G0=||F||_2, G1=||grad F||_2 and P2=||omega D^2 F||_2, where omega=(1+4r^2)^(2/5) and the Hessian is the complete ordered Cartesian tensor. Use the positive containing intervals accepted in N4-139, N4-153 and N4-166 and retained by N4-180. The exact inputs and frozen report are bound by verification/PROOF_FIRST.json.

Define E_*^2=P2^2+2^14 G1^2+2^18 G0^2 and E_w^2=P2^2+2^15 G1^2+2^20 G0^2. These are energies of the unregularized residual F. The registered sharpw norm is X=E_w(J^s F), with J^s=(1-Delta)^(s/2) and s=1/5184. Its accepted upper comparison in N4-180 bounds X from above.

The E_* shares round to 14%,72%,14% in the order P2,G1,G0. The frozen report SHA256 7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743 attributes these shares to X^2 at lines 226-227 and 993-994. That attribution is false: the actual weighted G0 share of X^2 is strictly greater than 1/4. No actual fractional P2 or G1 share is computed here.

## Proof

For positive component intervals [a_i,b_i] and positive weights w_i, define A_i=w_i a_i^2, B_i=w_i b_i^2. Then

    A_i / sum_j B_j <= w_i C_i^2 / sum_j w_j C_j^2 <= B_i / sum_j A_j.

Both denominator sums are strictly positive. This gives exact rational enclosing intervals for the shares of E_*^2 and E_w^2. These intervals need not preserve correlations to be valid. They establish the rounded E_* percentages by containment in the appropriate half-percent rounding cells. They also permit direct comparison with N4-180's independently stored E_star_energy_shares.

In Fourier space, (1+|xi|^2)^(s/2)>=1. Plancherel therefore gives ||J^s F||_2>=||F||_2. If U is the upper endpoint of N4-180's positive sharpw upper-comparison ball, then X<=U. Consequently the actual sharpw G0 share satisfies

    2^20 ||J^s F||_2^2 / X^2 >= 2^20 a_0^2 / U^2 > 1/4.

The final strict inequality is checked with integer arithmetic after rational squaring. It is incompatible with the asserted approximately 14% share. This uses the accepted norm comparison and component certificates, not a fresh fractional-norm evaluation.

## Correction and scope

Replace both disputed descriptions by: "In the unregularized comparison energy E_*^2=P2^2+2^14 G1^2+2^18 G0^2, the weighted G1 term contributes about 72 percent, and the G0 and P2 terms about 14 percent each (N4-180)." This is not a decomposition of the registered fractional sharpw norm. The observation still does not identify an operator direction or establish an optimization floor. All accepted norms, ratios, distances and candidate verdicts remain unchanged. The present work is a finite postfreeze audit of prefreeze quantities; no source integral or candidate computation is performed.

## Verification

The standalone proof is saved before the checker. Every decimal center and radius is interpreted as an exact rational. Input files are hashed, frozen-report line numbers are checked, and all arithmetic is performed with fractions. Complete component derivations and the multiplier/norm comparison are dependencies, not re-proved by byte agreement.
