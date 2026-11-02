# A paired empirical game for five current policies

Written: 2026-10-31T11:35:05.514297+00:00

## Exact statement and notation

Fix five policy specifications, their source hashes, the bundled balanced rules,
and the standard initial state. For every unordered pair of different policies
run two games, one for each assignment to the physical players. Let u_ij^s be
policy i's recorded payoff against policy j in assignment s: 1 for a win, 0 for
a draw, and -1 for a loss. The engine's winner determines the payoff; HP margin
is supplementary. Define A_ij=(u_ij^0+u_ij^1)/2 for i<j, A_ji=-A_ij, and A_ii=0.
The reverse entries use these same games, not additional samples. The diagonal
is the stipulated zero payoff of this symmetric empirical policy game; it is
not a measured self-play result.

Assume all twenty games satisfy their declared specifications and sources,
contain no rejected actions or bot errors, and pass original-engine replay.
If a rational probability vector p has p_i >= 0, sum p_i=1, and
sum_i p_i A_ij >= 0 for every column j, then p guarantees at least zero against
every mixture of the five listed columns in this empirical game. Its maximin
value is exactly zero.

## Proof

For every probability vector q, p^T A q is a nonnegative weighted sum of the
nonnegative column payoffs, so it is nonnegative. By construction A is
antisymmetric. For every real x, the scalar x^T A x equals its own transpose,
which equals x^T A^T x=-x^T A x; hence it is zero. In particular, against any
proposed row distribution x the column can use the same x and obtain zero.
No row distribution guarantees a strictly positive value. The given p attains
zero, proving the claim. All entries are half-integers or integers, so exact
rational arithmetic suffices to check a proposed certificate.

## Dependencies and scope

This is an application of ../finite_metagame/PROOF.md. No new game-theoretic
assumption is added. The probability vector is selected before the opponent
knows its realized component. This is a statement about a finite table,
not about all legal bots, unknown opponents, changed maps, or best.py revisions.
The fortress policy retains a wall-clock-limited gun planner, so the two
recorded assignments need not have identical histories and the table is not
asserted to be its exact future expected payoff. The checker reports both
histories, their equality or difference, and every outcome. It does not turn
twenty deterministic or partly clock-dependent games into independent trials.

The five specifications and all ten pairs are declared before execution in
current-policy-game-001.json. A separate builder binds the table to strict
source checks and replay evidence. A numerical optimizer may propose a
mixture, but a separate exact Fraction checker must verify it. An infeasible
proposal or incomplete campaign leaves the certificate open. No formal proof
assistant or theorem-prover check is claimed; formal/ remains empty.
