# A sixth policy and a fixed private-model change

Declared 2026-10-31T19:03:41.612311+00:00, before ten new games. The two reused I-H wins are already known.

## Exact policies and prospective claim

Retain B,C,D,G,H exactly as in extended_counter_game/PROOF.md. Add I, the round-three tier2, defense_first=false attacker from hp-handoff-forecaster-00-001. I differs from C only in its private opponent model: I retains the fixed H model on every edge, whereas C retains its fixed D model. Neither model may be changed to match a new opponent. Both use attack_share=1 and count_cap=200. Exact import specifications and all source/data hashes are in six-policy-game-campaigns-001.json and its five manifests.

The prospective empirical claim H1 is that I weakly improves on C against each of the five prior policies B,C,D,G,H, with at least one strict improvement. Compare their original-engine win/draw/loss payoffs, not HP magnitudes. The known I-H wins already supply a strict improvement over C-H; the new games determine whether another column regresses. A single lower payoff refutes H1. This is a selected development experiment, not held-out validation.

Ten new standard-start games measure I-B, I-C, I-D, I-G and I-I in both physical assignments. Thirty previously checked games supply the complete five-policy table, and two previously checked I-H games supply the remaining edge. All forty-two records are named explicitly; reused records are not new evidence.

## Conditional finite-game result

In order B,C,D,G,H,I, let A_ij be +1,0,-1 according to a row win, draw or loss. Require agreement between the two assignments for every unordered pair and require each measured diagonal to be zero. Reversing an off-diagonal outcome changes its sign, so A is skew-symmetric.

For any rational probability vector p with p^T A componentwise nonnegative, and any probability vector q, the weighted sum p^T A q is nonnegative. Conversely, for every proposed row mixture x, skew-symmetry implies x^T A x=0, so the opposing mixture x holds that row mixture to at most zero. Therefore any such checked p certifies finite-game value zero. This is conditional on the measured table, not a statement about arbitrary game policies or starts.

Use the existing exact Fraction solver to propose a vector and independently check normalization, nonnegative weights and every column payoff. The proof relies on those exact inequalities, not on completeness of the proposal search. Also check all pure rows for the same inequalities. If no certificate is found or assignment outcomes disagree, report the limitation without inferring global infeasibility.

## Verification and dependencies

For all new games require exact condition accounting, unchanged source/data archives, original-engine replay, fresh generation of both action sequences, legal submitted actions and unchanged observations. The private model is deliberately wrong on some edges; exact prediction of the real opponent is not required there. Recheck the five-policy receipt and the complete I-H source, replay, fresh-action and exact-prediction receipts. Retain all HP pairs, ending rounds, runtimes and canonical histories. The arithmetic implementation and six-dimensional component checks are recorded with the result.

The only implementation change between C and I is the private model and its parameters; their reached observations and later actions may consequently differ. A payoff difference is evidence about these two fixed policies, not an isolated causal effect at an otherwise identical state. Physical assignments with identical deterministic histories do not provide independent random samples. Wall-clock-bounded planner behavior outside these reached runs remains a limitation.
