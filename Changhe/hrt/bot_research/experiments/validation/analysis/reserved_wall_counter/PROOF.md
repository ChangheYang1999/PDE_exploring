# Reserving the round-four heavy purchase after a delayed wall opening

Written 2026-10-31T21:13:13.942821+00:00, before the proposed Q implementation or any Q decisions. P's four games against B/N have completed; P against O/L/G has not begun. The source hypothesis is based on the observed P/B opening and the exact income rule, not on unseen P/O outcomes.

## Definitions, hypotheses and dependency

G is EarlyWallGuard(guard00), P is DelayedWallGuard, O is WallPrefixSelector, and L is WallSignalRepair. Q follows P except for its round3 factory count. At round3 it keeps P's non-factory construction and buys the largest prefix of P's trailing factory actions that leaves projected round4 gold at least the tier4 cost. If even buying no factories fails this bound, it buys none and records infeasibility. It then resumes P unchanged. The projection uses only its public own gold, buildings, factory count and the authoritative path/income rules; it assumes zero outgoing-hit bounty. No opponent action is read or predicted.

For the numerical claim below use the bundled standard start and valid consecutive observations, with no external state alteration. Assume the game survives through round4 and Q has no outgoing roster through round3, as its specified opening ensures. Incoming attacks may change HP but do not remove buildings, factories or gold under these rules. Imports, the guard00 witness and the engine are fixed. The common-prefix and public-branch proofs in wall_prefix_selector/PROOF.md and delayed_wall_counter/PROOF.md are dependencies; Q has P's first move, so O selects L at round2.

## Exact reservation calculation

The straight empty-board path has22 edges. The20-wall opening blocks row1 at x=0 through9 and row3 at x=2 through11. Any route must cross row1 at x>=10, then row3 at x<=1, before reaching base x=11. It therefore needs at least10+9+10 horizontal and11 vertical steps, totaling40. This is attained by crossing at x=10 and x=1. Adding the splash at (1,3) forces the row3 crossing to x=0, raising the horizontal lower bound to10+10+11 and the total to42; crossing at x=10 and x=0 attains it. Thus the quoted shortest-path lengths follow without a tie-breaking assumption.

P's observed first three completed states against B have97,177,254gold and5,8,13factories. Their paths have22,40,42edges. These numbers are reproduced directly from the source: round1 buys five20-gold factories and receives22+5*15=97 income. Round2 pays20 for walls, buys three factories for60, retains17, and receives40+8*15=160, giving177. Round3 buys the60-gold splash, leaving117 before factories. If it buys k factories, it finishes that round with

    g4(k) = 117 - 20k + 42 + 15(8+k) = 279 - 5k.

The outgoing roster is empty, so hit bounty is exactly zero. k is an integer from0 through5. The tier4 costs260. Thus g4(k)>=260 exactly when k<=3. Buying three factories is the largest feasible choice, yields264 gold and11 factories, and preserves the planned round4 tier4 purchase. Buying the original five yields254, six short; buying four yields259, still one short. At least two factory purchases must therefore be withheld within this otherwise fixed opening. This proves both sufficiency and minimality among prefixes of P's round3 factory actions, not optimality over other openings.

Changing factory count leaves the map and round3 combat unchanged. At round4 Q submits one tier4 for260 and has4gold left before settlement, so no additional factory is bought in that decision. P's parent rule makes this purchase before attempting factories. Q's round1 remains five factories with empty buildings/roster; therefore O's L selection is unchanged. These arithmetic and branch conclusions do not imply that the attack wins.

## Prospective empirical checks

Pin Q, this proof, its prose dependencies, all source/data inputs and exact specifications before decisions. Run Q against O,L,G,B,N in both assignments:10new standard games. Compare with the completed P campaign after it is available. H1: Q wins against O in both seats. H2: O takes L and the complete Q/O histories equal Q/L controls in corresponding seats. H3: each opponent's two role-normalized full histories agree. H4: Q has264 gold and11 factories after round3 and submits exactly one tier4 in round4 in all10 games. H4 tests the arithmetic under actual incoming attacks and ensures no hidden bounty or construction difference was overlooked. No B/N/G outcome prediction is made.

Every game requires strict source/action checks, complete original-engine replay with explicit terminal boundary, and fresh decisions by both external policies. The O/L comparison also checks the selected logical private values, excluding the already documented global/alias/clock limitations. Record failures without editing inputs or reclassifying conditions. Any signal-plus-reservation effect is attributed to both changed opening decisions; no pure signaling claim is made. The final candidate and reserved D inputs remain unchanged. These are selected development cases, not independent random samples or unseen-family validation.

The reservation calculation and round2 branch claim are proved under the above hypotheses. H1-H4 are OPEN before Q execution. No formal proof-assistant source is claimed.
