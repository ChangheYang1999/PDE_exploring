# Review of the ten-policy and wall-routing certificates

Review completed 2026-10-31T20:50:08.909569+00:00. This is an independent source and retained-artifact review. It ran no games, policy calls, engine replays, native recompilation, or full routing rescan. The small read-only check completed at 2026-10-31T20:49:00.735984+00:00 in 6.333410 seconds on one assigned low-priority CPU. Its source and receipt are `bot_research/experiments/validation/reviews/certificate_review_2050/check.py` and `bot_research/experiments/validation/reviews/certificate_review_2050/result.json`.

No mathematical or evaluation defect was found that invalidates the exact restricted conclusions below. This finding does not validate an unrestricted game equilibrium or certify every future execution of the included policies.

## 1. The finite table is correctly oriented and complete

**Claim.** The retained records determine the published 10-by-10 payoff table for B,C,D,G,H,I,J,L,M,N, with both physical player assignments checked for every unordered pair, including self-play. **Verdict: CONFIRMED for the retained artifacts.**

The independent script read all 110 raw result files and their corresponding job files, checked candidate and opponent specifications against the declared policy labels, checked the two physical bot slots, and required a standard development start without prescribed prefixes. It reconstructed win/draw/loss from each engine winner field, checked candidate-first HP and round counts, and rebuilt the matrix. All 55 assignment pairs have one record per physical side and matching normalized complete replay hashes. All ten self-pairs draw. The rebuilt matrix equals the published matrix. The new-record count is 34, the reused-record count is 76, and twice the summed new-game rounds is 1,732, matching the fresh-call receipt.

The normalization removes the match identifier, snapshot display names and the global interleaved action-order number, then remaps player and winner identifiers and sorts the two player records within each round. It retains each player's event-list order, submitted actions, acceptance results, snapshots and terminal result. Removing the global action-order number is appropriate for exchanging physical player slots. The original replay checker separately compares the unnormalized records with the unchanged engine, including this field. Thus the normalization does not replace the legality or original-engine check.

The review recomputed every pinned hash in the three main receipts, including exact decompression of archived inputs. There were 6,697 distinct hashed inputs after adding directly inspected result and job artifacts. The retained source closures, native executables, binary wall records and parent evidence match their recorded hashes. This verifies continuity of these artifacts; the review did not execute the old engine and fresh-policy audit pipelines again.

## 2. The rational certificate proves the stated restricted value

**Claim.** Uniform weights on G, J and N certify value zero for the measured ten-policy matrix. **Verdict: CONFIRMED.**

The checked vector in B,C,D,G,H,I,J,L,M,N order is

`[0,0,0,1/3,0,0,1/3,0,0,1/3]`.

Independent exact `Fraction` arithmetic gives column payoffs

`[1/3,2/3,0,0,1/3,2/3,0,1/3,1/3,0]`.

These weights are nonnegative and sum to one. Every column payoff is nonnegative. Skew symmetry gives opposing row payoffs equal to their negatives, so the same mixture used by the column player bounds every row mixture above by zero. The two bounds establish value zero without relying on completeness of the proposal search. The verifier explicitly checks dimensions, integer payoff entries, skew symmetry, probability constraints and both payoff bounds. The stated absence of a completeness or uniqueness claim is correct.

The old uniform B/G/H/J/L mixture has payoffs -1/5 against M and -3/5 against N, so extension hypothesis H1 is refuted. N minus B on the eight old columns is `[1,0,0,0,2,0,0,0]`, so the stated restricted H2 is confirmed. Neither conclusion changes the validity of an earlier certificate on its own smaller matrix.

## 3. The publisher amendment preserves policy identity

**Claim.** Explicit `continuation="fortress38"` and the omitted default identify the same pinned M constructor. **Verdict: CONFIRMED.**

The retained first publisher stopped at specification equality before publishing results. The amended publisher adds only the exact screened-counter default to its normalization, checks the constructor signature, tests equivalence with the explicit default, and tests inequality with `continuation="econ20"`. The reviewed `make` passes keyword arguments directly to `ScreenedRosterGuarded`, whose pinned constructor has the claimed default. No outcome, original declaration or policy source was changed by this correction. All original and amendment pins passed the independent artifact check. This is a justified literal-default correction, not a general equivalence rule for distinct policies.

## 4. Reverse distance descent has the engine's shortest-path tie break

**Claim.** On this undirected unweighted grid, breadth-first distances from the base followed by the first distance-decreasing neighbor in right/down/left/up order recover exactly the engine's route. **Verdict: CONFIRMED by source argument.**

At every vertex on a shortest route, the next vertex must have distance to the base one smaller. Choosing the first eligible direction and repeating produces the least direction word among shortest routes. In forward FIFO breadth-first search, all retained least words at a fixed depth are processed in lexicographic order; extending these words in neighbor order preserves that order. Discarding a later visit to an endpoint cannot remove its least shortest word. Each prefix of a shortest spawn-to-base route is shortest to its endpoint, so the first base parent chain is the same least word.

The original Python router, forward native enumerator and backward native checker respect these hypotheses. Tower and wall cells are blocked, while spawn and base are excluded from the wall domain. The backward search uses reverse neighbor order when computing distances, which cannot alter the distances; its descending traversal uses the engine's order. Both score calculations include spawn and exclude the base. No tie-break discrepancy was found.

The retained backward audit reports zero score mismatches across all 14,901,218 binary records and exact full-path equality on the parent's 11,097 retained original-router cases. This review verified the pinned bytes, native checker source and aggregate receipt consistency. It did not rerun that all-record comparison or those path fixtures.

## 5. Coverage and the minimum-five-wall reduction are valid at the fixed state

**Claim.** Five walls are the minimum additional defensive cost at the specified C02 round-six state, while retaining the fixed 180-gold screened attack and fixed opposing action. **Verdict: CONFIRMED under the stated source and ordinary-execution dependencies.**

The inspected witness has exactly the four stated splash towers, no walls, 190 gold and no prior attacking roster for the defender at the end of round five. The fixed opposing round-six action leaves incoming entries tier1,tier1,tier1,tier3. Current prices leave 10 gold after the fixed tier2,tier2,tier3 purchases. A turret costs at least 30 and a factory costs 20, so neither is affordable from this remainder.

There are 138 available wall cells. Within each shard, the Python audit validates membership in this domain, distinct increasing cells, canonical padding, cardinality, the prescribed first-cell-index shard, and strictly increasing `(cardinality, wall tuple)` keys. Therefore no record duplicates another within or across shards. Counts `[1,138,9453,428536,14463090]` equal the corresponding binomial coefficients. A duplicate-free subset of each finite cardinality domain with its full cardinality is the whole domain. Count agreement alone would not suffice, but these domain and uniqueness checks supply the missing premises.

The combat reduction also matches source. All splashes damage every adjacent copy with no target competition. Each surviving copy receives the summed route exposure once per non-base path cell, including spawn. At most 140 unblocked cells and latest birth tick three put every surviving arrival before tick 250. The tier3 dies exactly when exposure damage reaches 180, which also kills the tier1 copies. A legal final wall set can be built in any order since every intermediate obstacle set preserves its final path and costs no more than the affordable final set.

The independent receipt check confirms disconnected counts `[0,3,410,27813,1248613]`, per-cardinality maximum damage `[100,100,100,100,150]`, histogram totals, and agreement between forward and reverse receipts. All maxima for zero through four walls are below 180. The retained legal five-wall original-engine witness has damage exposure 190 and zero incoming damage. These establish the claimed minimum under the exact fixed conditions.

## Remaining limits

The native computations use an ordinary compiler and runtime. Agreement between two implementations strengthens the evidence but does not remove their shared dependence on the fixed board, exposure model and unchanged engine rules. The native full-record audit compares scores; full path equality with the engine is computationally sampled and supported for the remaining cases by the routing argument. No formal proof-assistant or verified-compiler result is claimed.

The finite-game table is selected development evidence at one standard start. Its 110 records and the additional fresh action calls are not independent population samples. Some policies use wall-clock cutoffs, so source identity and observed action reproduction do not prove identical behavior under every machine load. The certificate concerns the measured payoff matrix and simultaneous selection among its ten fixed policies. It gives no bound against an eleventh policy or a changed start. It is not validation of whichever implementation is finally installed as `bot_research/bots/best.py`.

The five-wall result concerns only the selected state, fixed attack purchases, fixed opposing action and additional wall construction. It does not optimize openings, attack composition, a different opposing response, or future rounds. This review did not inspect reserved final opponents or change their selection.
