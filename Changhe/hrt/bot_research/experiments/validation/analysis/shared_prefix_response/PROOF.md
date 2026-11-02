# Responding after a common first move

Declared 2026-10-31T19:11:45.525042+00:00, before any selector game.

## Policies and claim

Retain the exact B,C,D,G,H,I specifications from six_policy_game/PROOF.md and its completed receipt. Define J with two private response objects H and I. On round one J calls both on copies of its own public observation and requires identical action lists, then submits that shared list. On round two J permanently selects H if the opponent has at least twenty walls and an empty roster; otherwise it selects I. It uses only the public observation, never a name, import specification, future action or live opponent object. There is no later branch change. The unselected response stops running after round one.

H1: on standard starts J has no loss against each of G,H,I in both assignments, and its mean win/draw/loss payoff against their uniform mixture is strictly positive. H2: J has no loss against any of the six prior policies B,C,D,G,H,I. Fourteen new games test J against all six and against itself. H1 and H2 are selected development hypotheses; the wall criterion and response pair were designed after inspecting those policies' first moves. No result is held out.

## Conditional shared-prefix argument

Assume H and I are deterministic stateful policies initialized as usual, their first action lists agree on J's first public observation, and the selected branch receives each later actual observation exactly once. After round one its internal state equals the state of the corresponding standalone response run on that same observation. Induct on rounds: identical internal states and observations imply identical next actions and next states. Thus J's actions equal the chosen response on the actual reached history, including the common first move. If the opponent is also deterministic, the whole subsequent game equals the standalone game with that response from the same start. This statement does not assert that a different initial action would have worked, or that the response choice is optimal.

The implementation has wall-clock-bounded dependencies, so full-history response equality must be checked rather than inferred from the conditional argument alone. In particular, selecting H after I's internal state has advanced would be invalid unless H had also processed the shared prefix; J explicitly processes it through both.

## Verification

Before full games, check J against G,H,I through round eight in both assignments. Independently run H as the reference for G and I for the other two, compare every action, check both observations unchanged and all submitted actions legal, and advance the unchanged original engine. Full games require frozen source/data archives, complete condition accounting, original-engine replays, independent fresh action regeneration for both players, and a separate full-history comparison of J with its selected fixed response. Report exact final HP, outcomes, branch decisions, actual call timings and identical assignment pairs. A failed or timed-out condition stays visible.

For payoff values +1,0,-1, linearity gives expected payoff (A_JG+A_JH+A_JI)/3 against a policy drawn independently and uniformly before the game. The average is exact finite arithmetic, not a statistical estimate. The six-policy certificate remains valid for its original six columns; an added policy can invalidate any extrapolation beyond that table. No claim covers arbitrary opponents, altered starts, adversaries choosing after J's branch, or a globally optimal game strategy.
