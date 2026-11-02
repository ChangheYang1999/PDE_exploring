# Exact equilibrium set of the recorded frr1 matrix

Prepared at 2026-10-31T22:20:47.936610+00:00. Provenance qualification finalized at 2026-10-31T22:21:36.764457+00:00. This is a finite matrix-game proof over exact rational entries. Its empirical input is the retained frr1 standard-start tournament, whose parsing and source audit are separate from the algebraic theorem.

## Statement, hypotheses and notation

There are ten pure strategies, in this fixed coordinate order:

`best_v9e, best_v9f, af2g, P5TNUBM, v41, V29, g1, guard00, threat_defender, AS1C`.

For distinct strategies i and j, define M[i,j] as +1, 0 or -1 according to the recorded win, draw or loss of i against j. The two physical-seat assignments give the same outcome from i's perspective in all 45 pairs. We impose M[i,i] = 0. These ten diagonal entries are a symmetric empirical-matrix convention; frr1 contains no measured self-play games. The table below completely defines the mathematical object to which the theorem applies.

| Row / column | best_v9e | best_v9f | af2g | P5TNUBM | v41 | V29 | g1 | guard00 | threat_defender | AS1C |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| best_v9e | 0 | 0 | 0 | 0 | 1 | 1 | 1 | -1 | 1 | -1 |
| best_v9f | 0 | 0 | 0 | 0 | 1 | 1 | 1 | -1 | 1 | 0 |
| af2g | 0 | 0 | 0 | 0 | 1 | 1 | 1 | -1 | 1 | -1 |
| P5TNUBM | 0 | 0 | 0 | 0 | 0 | 1 | 1 | -1 | 1 | 0 |
| v41 | -1 | -1 | -1 | 0 | 0 | 1 | -1 | -1 | 1 | -1 |
| V29 | -1 | -1 | -1 | -1 | -1 | 0 | 1 | -1 | 1 | -1 |
| g1 | -1 | -1 | -1 | -1 | 1 | -1 | 0 | 1 | 1 | -1 |
| guard00 | 1 | 1 | 1 | 1 | 1 | 1 | -1 | 0 | 1 | 1 |
| threat_defender | -1 | -1 | -1 | -1 | -1 | -1 | -1 | -1 | 0 | -1 |
| AS1C | 1 | 0 | 1 | 0 | 1 | 1 | 1 | -1 | 1 | 0 |


Let Delta be the simplex of nonnegative real ten-vectors with coordinate sum 1. The row player's payoff is x^T M y for x,y in Delta. The row max-min value is

\[
 v=\max_{x\in\Delta}\min_j (x^T M)_j.
\]

The column player minimizes the same payoff. Here M is skew-symmetric, M^T = -M. The game is symmetric in the game-theoretic sense that both players have the same pure strategies and exchanging their roles negates the payoff. The numerical matrix is not a symmetric matrix.

**Theorem.** The value is v = 0. The complete set of row max-min mixtures is

\[
 S=\{(0,d,0,p,0,0,\tfrac13,\tfrac13,0,c):
      c,d,p\geq 0,\quad c+d+p=\tfrac13\}.
\]

Thus every optimal row mixture puts exactly 1/3 on g1, exactly 1/3 on guard00, distributes the remaining 1/3 arbitrarily over AS1C, best_v9f and P5TNUBM, and puts zero on best_v9e, af2g, v41, V29 and threat_defender. The column minimax set is also S. Consequently the complete set of Nash equilibrium profiles is S x S, with the two players free to choose different points of S.

## Exact primal and dual certificate for the value

Let z put weight 1/3 on each of AS1C, g1 and guard00 and zero elsewhere. Direct multiplication in the stated coordinate order gives

\[
 z^T M=(\tfrac13,0,\tfrac13,0,1,\tfrac13,0,0,1,0),
 \qquad
 Mz=(-\tfrac13,0,-\tfrac13,0,-1,-\tfrac13,0,0,-1,0)^T.
\]

All coordinates of z^T M are nonnegative, so z guarantees payoff at least 0 against every column mixture. All coordinates of Mz are nonpositive, so the column mixture z guarantees payoff at most 0 against every row mixture. These feasible primal and dual strategies have the same bound 0. Therefore the value is exactly 0. This argument needs no numerical optimization or appeal to an approximate solver.

## Necessity, using the strict dual entries

Let x be any row max-min mixture. Since the value is 0, x^T M has no negative coordinate. In particular x^T Mz is nonnegative, because z is a probability vector. But the displayed dual vector gives

\[
 x^T Mz=-\tfrac13 x_{best\_v9e}-\tfrac13 x_{af2g}
         -x_{v41}-\tfrac13 x_{V29}-x_{threat\_defender}\leq 0.
\]

Each weight is nonnegative. Equality is possible only if all five displayed weights are zero. This proves exclusion, including exclusion of best_v9e, without relying on the general and insufficient observation that it is weakly dominated.

Write a = x[g1], b = x[guard00], and t = x[AS1C] + x[best_v9f] + x[P5TNUBM]. Then a+b+t = 1. Against the columns guard00, g1 and AS1C respectively, the remaining mixture scores a-t, t-b and b-a. Optimality makes all three nonnegative. Hence

\[
 a\geq t\geq b\geq a.
\]

All three are equal, and their sum is 1. Therefore a = b = t = 1/3. There is no further restriction yet on how t is split among its three coordinates.

## Sufficiency for every split, including the boundary

Take any c,d,p >= 0 with c+d+p = 1/3, and the mixture x in the theorem. Direct multiplication gives

\[
 x^T M=(c,0,c,0,1-p,\tfrac13,0,0,1,0).
\]

The coordinate 1-p is at least 2/3 because 0 <= p <= 1/3. Every other coordinate is visibly nonnegative, and several coordinates are zero. Thus the worst pure-column payoff is exactly 0 and x is max-min. This verifies every point of S, including cases where one or two of c,d,p vanish. It proves that the optimal set is exactly S rather than just that three example mixtures are optimal.

For any y in Delta, M y = -(y^T M)^T. It follows that y has every dual row payoff at most 0 exactly when y is a row max-min strategy. Thus the dual set is also S. Any x,y in S form a saddle point with payoff 0, and every zero-sum equilibrium must use a strategy from each player's optimal set. This proves the final assertion about all equilibrium profiles.

## Independent check of the report's three-column proof

The report avoids the strict-dual step. Its inequalities are also correct. For an arbitrary candidate optimal x, let a = x[g1], b = x[guard00], t = 1-a-b, r be the total weight on best_v9e, af2g, v41, V29 and threat_defender, and u = x[v41] + x[threat_defender]. The matrix columns guard00, g1 and AS1C give, respectively,

\[
 a-t\geq0,\qquad t-2u-b\geq0,\qquad b-a-r\geq0.
\]

Since r,u >= 0, these imply the full chain

\[
 a\geq t\geq b+2u\geq b\geq a+r\geq a.
\]

The endpoints agree, so every inequality is an equality. In particular r=u=0 and a=b=t=1/3. This reproduces the report's claimed necessity from the independently reconstructed matrix.

## Weak dominance claim

The AS1C row minus the best_v9e row is +1 in the columns AS1C, best_v9e and af2g and 0 elsewhere. The best_v9f row minus the best_v9e row is +1 in the AS1C column and 0 elsewhere. Thus both weak-dominance statements in the report are exact for this matrix. Weak dominance alone would not suffice to prove zero equilibrium weight; the strict dual certificate or the three-column argument supplies that necessity.

## Dependencies and empirical scope

The fixed result input is `bot_research/runs/lead/frr1/results.jsonl`, SHA256 `2df0933ba2f8872c064d5edbfd1640d07713c3335a107b4e2aa0de9350113b00`. The audit retained all 90 log hashes in `verification/independent_audit_001.json`, SHA256 `118f08bc7d87f3ff536368a60c51e6879bf273c6bd7e5c431d56ad1a2fbbd08d`. The checker source is `verification/check_frr1_matrix.py`, SHA256 `7d56bde0fb3a62a785d80d5913a8850d8e94c9d7a35738ba56e396e964071e8f`.

The checker imports only the Python standard library. It reconstructs the matrix from exact full specification strings, checks all 45 unordered pairs in both physical seats, parses each complete raw log, checks the standard initial state and bundled rules, checks source identities, and evaluates the three vertex primal/dual certificates using `fractions.Fraction`. The necessity proof is the argument above; checking vertices alone would not establish it. No policy imports, constructors, decisions, games or engine replays were performed in this review.

The record audit found 90 complete games, 7,772 records, 651,202 accepted action events and no rejected actions, bot errors, scenario errors, reported source changes, missing logs or orphan logs. The source audit found one recorded version per full specification, seven distinct source-closure versions for the ten parameterized specifications, 66 consistently recorded loaded Python sources, and 66 current static-digest sources. Their union contains 76 files; every checked current source matches the recorded hash or closure digest. The JSON rules in every initial record equal the current `td_game/balanced.json` object. The artifact receipt records the exact hashes and checks.

These Python comparisons follow the harness's source-digest definition only. They do not authenticate transitive runtime JSON data. In particular, `EarlyWallGuard.__init__` reads `bot_research/bots/counters/data/early_wall_guard_001.json`; this audit did not compare that witness file with an earlier runtime-data pin. Its historical bytes, and those of other runtime data not embedded in the logs, remain outside the provenance claim. The matrix theorem is conditional on the retained payoffs and does not require that missing claim.

These are checks on the retained artifacts, not an engine replay or an independently authenticated process history. The tournament has no separate durable attempt journal, so absence of erased or never-recorded attempts is not established. Source identities at retained checkpoints do not prove that no temporary historical edit occurred between them.

The theorem is exact for the displayed W/D/L matrix with its imposed zero diagonal. It makes no claim about an HP-difference payoff matrix, another start, a new opponent, repeated execution under changing wall-clock cutoffs, or the optimal strategy of the full tower-defense game. It does not justify changing the published bot. A randomized implementation that selects a member at the opening would inherit this matrix-game value only under the additional premise that the selected executions reproduce the recorded payoffs.
