# The uniform mixture in a three-policy counter cycle

## Exact statement and scope

Let E, G and B be three policies. Fix one game ruleset and initial state. Define the row player's empirical payoff to be 1 for a win, 0 for a draw and -1 for a loss, averaged over both player assignments. Suppose the recorded payoff matrix, in the order E, G, B, is

```
       E   G   B
E      0  -1   1
G      1   0  -1
B     -1   1   0
```

Then the uniform distribution assigning probability 1/3 to each policy has value zero against every distribution over this same list. It is the unique maximin distribution in this three-policy game. Every pure policy loses with payoff -1 to another listed policy.

These conclusions are conditional on this exact empirical matrix. They do not assert a game-theoretic solution of tower defense, robustness to an unlisted opponent, or invariance under a different initial state. The opponent must select its listed policy without observing the randomly selected component, though that policy may adapt to public observations during the game.

## Proof

Each column of the matrix sums to zero. Consequently the uniform row distribution has expected payoff zero against each column and, by linearity, against every mixture of columns.

For an arbitrary row distribution p = (e,g,b), its three column payoffs are g-b, b-e and e-g. Their sum is zero. At least one is therefore nonpositive, so no distribution guarantees strictly positive payoff. The uniform distribution attains zero and is maximin.

If a distribution guarantees zero, each of its three column payoffs must be nonnegative. Thus g >= b >= e >= g. All three probabilities are equal, and normalization forces each to be 1/3. This proves uniqueness. The negative off-diagonal entries establish the final statement about pure policies.

## Empirical application and dependencies

The proposed application uses E = frozen economy13, G = gun1 at (3,1), one tier1 and two factories in round one followed by economy13, and B = factories through round six, a gun1 at (0,11) in round three, then tier5 purchases. The exact specifications are registered before the fresh matrix in `bot_research/experiments/validation/counter-cycle-001.json`.

Independent source, legality and full original-engine replay checks must support every matrix entry. Repeated controls check reproducibility; they are not independent strength samples. The exact matrix and rational certificate are JSON artifacts. `check_metagame_certificate.py` checks all matrix products using rational arithmetic. `verification/evidence.json` records the completed evidence when available. This is an informal proof, not a proof-assistant formalization.
