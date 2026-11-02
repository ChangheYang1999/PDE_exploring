# The measured game after adding a public-response policy

Declared 2026-10-31T19:26:11.343070+00:00. This is an exact reanalysis of already observed outcomes, not a prospective experiment.

## Statement, notation and hypotheses

Let A be the seven-by-seven payoff matrix in B,C,D,G,H,I,J order. The first six policies and all their exact import specifications are fixed by six_policy_game/PROOF.md and its completed verification receipt. J is fixed by shared_prefix_response/PROOF.md. Each entry is +1, 0 or -1 for the unchanged engine's win, draw or loss on the standard start. Require that both physical assignments of every unordered pair agree in outcome and complete normalized history, and every measured self-play outcome is a draw. The table consists of 42 old six-policy records plus 14 old J records, with no new game.

The arithmetic claim is conditional: if a rational vector p has nonnegative coordinates summing to one and p^T A is componentwise nonnegative, then this seven-policy finite zero-sum game has value zero, and p is an optimal mixture for either role. The inherited claim that the former G/H/I uniform mixture remains nonnegative is checked, rather than assumed. Report all pure rows satisfying the same inequalities and all directed three-policy cycles.

## Complete argument

By reversing the role of the two players, each off-diagonal payoff changes sign; the checked assignment equality and draw diagonal give A^T=-A. For any opposing probability vector q, the quantity p^T A q is a convex combination of the nonnegative components of p^T A, hence is nonnegative. On the other side, A p=-(p^T A)^T is componentwise nonpositive, so every row probability vector x satisfies x^T A p<=0. Thus p guarantees at least zero as row player and at most zero as column player. These matching guarantees prove the asserted value and optimality without a general minimax theorem or any assumption about completeness of the search for p.

A pure policy satisfies the guarantee exactly when every entry of its row is nonnegative. A directed three-cycle is a triple of distinct indices i,j,k with A_ij=A_jk=A_ki=1; list each cyclic rotation once. The former mixture's payoffs are computed by its same coordinates padded with a zero at J.

## Verification, dependencies and scope

Read the two completed parent receipts only after all their checks pass. Verify every input hash, using decompressed replay bytes if the original file has been archived, and record the compressed storage hash separately. Reconstruct the seven-by-seven table directly from the 56 receipt cases, reject duplicate result paths, and recheck each pair's physical assignments and canonical-history equality. No simulator or fresh policy call is performed here: those are the parent studies' evidence. The independent arithmetic check requires normalization and every primal and opposing inequality with exact Fraction values. Seven-dimensional zero, dominant-first and replicated-cycle fixtures check the proposal solver before use.

The strategies are fixed programs and include J's public-history adaptation. Randomization in the finite game means privately selecting one program before play. The conditional certificate makes no statement about policies outside these seven, changed starts, alternative wall-clock planner outcomes, statistical generalization, or pool D. The public wall-signal attack is a separate study and its strategies are not silently included as columns here. The original six-policy certificate remains valid on its original columns even if its mixture fails against J.
