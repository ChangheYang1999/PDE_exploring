# Extending the finite counter-policy game

Declared 2026-10-31T18:34:13.857030+00:00, before the ten new games.

## Policies, hypotheses and conditions

Keep the three policies B, C and D from latest_counter_game/PROOF.md without changing their source or parameters: B is frozen best_v9e, C is the round-three tier2 attacker with its fixed private D model, and D is the adaptive Fortress38 continuation. Add G, the fixed early-wall guard00, and H, the fixed HP-triggered grower with lead_from=8 and deadline=12 from early_wall_transfer. The exact specifications and all old result paths are in extended-counter-game-campaigns-001.json. These are standard starts under the received engine and configuration. Each unordered pairing and each self-play is measured in both physical assignments.

H1 is the empirical claim that the old uniform B/C/D mixture still has nonnegative expected win/draw/loss payoff against each of G and H. H2 is the empirical claim that G weakly improves on D against all five fixed policies, with at least one strict improvement. Both remain OPEN until all rows are verified. Ten new games complete the five missing pairings C-G, B-H, C-H, G-G and H-H. Twenty old games supply the other ten pairings, including measured self-play. The new opponents were chosen after earlier counter results and are development data.

C keeps its private D model even against G and H. An incorrect private forecast does not invalidate the policy or permit changing it. D's omitted mode means adaptive by its fixed constructor. All other parameter identities are checked after JSON parsing. Physical names may differ, but none of the five policies uses a displayed name to choose actions.

## Conditional finite-game certificate

Let A be the five-by-five matrix in B,C,D,G,H order, with A_ij equal to +1 for a row win, 0 for a draw and -1 for a loss. The two assignments must agree before assigning an integer payoff, and each measured diagonal must be zero. Off-diagonal reversal changes the sign, so A is skew-symmetric. Reused conditions are not new observations.

Let p be any rational vector with p_i>=0, sum_i p_i=1 and p^T A>=0 componentwise. For every probability vector q over these five policies, p^T A q>=0 by a nonnegative weighted sum. Conversely, for any proposed row mixture x, skew-symmetry gives x^T A x=0, so the opponent can hold it to at most zero by choosing x. Hence a verified p is optimal with value exactly zero in this finite game. This proves only a conditional finite-table statement, with no claim about the full game or unlisted policies.

A small exact rational search may propose p by solving systems formed from normalization and active nonnegativity/payoff constraints. Every returned weight and matrix inequality is then checked with Fraction arithmetic. The proof uses the checked inequalities, not completeness of that search. If no vector is found, publish that limitation rather than infer infeasibility. All matrix entries, rational weights and arithmetic are retained as JSON.

The old p0=(1/3,1/3,1/3,0,0) is checked directly against both new columns. For H2, compare every G-row entry with its D-row counterpart and require at least one strict inequality. A single negative p0 column refutes H1; a single G<D entry or complete equality refutes H2.

## Verification and scope

Require exact condition accounting, source/data archives, original-engine replay and fresh generation of both policies for all ten new games. Reverify the original receipts and source archives for all twenty reused games, including the earlier exact-forecast and handoff checks where applicable. Record every HP pair, final round, timing and canonical history hash. If assignment outcomes disagree, report both and leave the integer-matrix claims unresolved.

A policy mixture means a hidden draw before a match, not an adversary allowed to select after observing the branch. Each selected policy may still adapt to ordinary observations. No randomized bot or new random samples are introduced here: this is exact arithmetic over the fixed measured table. Future-load stability of bounded planners and performance against unseen policies remain unproved.
