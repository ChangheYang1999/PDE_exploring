# Two new columns in the fixed counter game

Written 2026-10-31T20:39:16.442800+00:00, before the new matches or their declaration.

## Exact objects and empirical questions

Keep the eight policies B,C,D,G,H,I,J,L, with precisely the specifications and source bytes of the completed eight-policy table. Add M, the default screened_roster_guarded policy with the five-wall round-six package and frozen Fortress38 continuation. Add N, frozen best_v9e with attack_share=1.0 and catch_up_share=0.5 (AS1C). All games use the bundled balanced rules and the standard start.

There are already 72 checked records for the eight-policy table, two M-versus-B records in screened-roster-guarded-fortress38-001 and two M-versus-N records in screened-guard-transfer-00-001. Reuse those 76 records explicitly. Run the other 17 unordered pairs, including M and N self-play, in both physical assignments: 34 new games, 110 total records, 55 pairs. No policy parameter may change during this extension.

H1: the previously certified mixture, uniform on B,G,H,J,L, has nonnegative payoff against both M and N. H2: N weakly improves on B against all eight old columns and strictly improves against at least one. Both claims are OPEN before the new matches. Known M-versus-B wins and M-versus-N losses are prior selection evidence, not predictions. Every new result and failure must be retained.

## Finite-game statement and argument

For each unordered pair, first verify complete source-pinned, legal original-engine games in both physical assignments. The normalized full histories must agree. Self-play must draw. Define A_ij as +1 for a row win, 0 for a draw and -1 for a row loss using the engine winner field. The checked assignment symmetry and self draws justify a skew-symmetric 10-by-10 matrix with zero diagonal. If those conditions fail, do not publish the single-matrix certificate as established.

Suppose rational p_i are nonnegative, sum to one, and every entry of p^T A is nonnegative. For any opponent distribution q, p^T A q is a weighted sum of nonnegative column payoffs and hence is at least zero. Conversely skew symmetry gives A p = -(p^T A)^T, so every row distribution x has x^T A p at most zero. These two inequalities prove exact value zero on the ten fixed columns. A proposal algorithm does not need to be verified or complete: the independent exact checker verifies the matrix symmetry, dimensions, normalization, signs and both payoff inequalities. If no checked proposal is found, the certificate claim stays OPEN.

The proposal search enumerates candidate supports and solves rational linear systems for zero payoff on the support plus normalization. It may miss degenerate certificates; no completeness or uniqueness claim is made. Verification rejects deliberately invalid weights and matrices, and checks explicit small and embedded-ten-dimensional examples before the real table is assembled.

H1 is the conjunction of two exact column inequalities for the old weights extended by zeros. H2 compares N and B entry by entry on the first eight columns and requires at least one strict inequality. These algebraic conclusions are conditional on the validated empirical table.

## Verification dependencies and limits

New games require strict job accounting, unchanged source/data archives, original-engine replay and fresh reproduction of both action streams on every recorded observation. Parent receipts and all their pinned inputs are rechecked, using exact decompression where an earlier replay was archived. Counts separate the 34 new games from 76 reused records. Policy calls used for reproduction are checks, not more independent games.

This is a selected development extension after observed counters. It is not held out, a population estimate or an unrestricted game equilibrium. Some fixed policies use wall-clock cutoffs; matching histories establish these measured outcomes, not invariance under all computing loads. The final installed bot, its decision rules, and reserved pool D remain unchanged. The terminal pipeline is already waiting at its23:00Z gate and will not be duplicated.
