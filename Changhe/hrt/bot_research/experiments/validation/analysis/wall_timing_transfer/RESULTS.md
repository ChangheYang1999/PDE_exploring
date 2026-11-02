# Wall timing transfer on eight fixed opponents

Checked 2026-10-31T22:06:51.577576+00:00.

Audit completion: COMPLETE. Verified records: 32/32. H1 CONFIRMED; H2 CONFIRMED; H3 CONFIRMED.

H1 compares S and Q separately in each of 16 opponent/seat conditions. H2 compares the two complete normalized histories for each of 12 new policy pairs. H3 requires all 32 games to reach round four and satisfy the declared opening. An early terminal result refutes H3, while a missing or unaudited result leaves its condition open.

| Opponent | Seat | Q WDL, HP | S WDL, HP | S WDL at least Q | Evidence |
| --- | ---: | --- | --- | --- | --- |
| F44 | 0 | W 780:740 | W 780:740 | CONFIRMED | new |
| F44 | 1 | W 780:740 | W 780:740 | CONFIRMED | new |
| F45 | 0 | W 780:740 | W 780:740 | CONFIRMED | new |
| F45 | 1 | W 780:740 | W 780:740 | CONFIRMED | new |
| V29 | 0 | W 785:740 | W 785:740 | CONFIRMED | new |
| V29 | 1 | W 785:740 | W 785:740 | CONFIRMED | new |
| V29_g1 | 0 | L 686:740 | L 686:740 | CONFIRMED | new |
| V29_g1 | 1 | L 686:740 | L 686:740 | CONFIRMED | new |
| V31_g1f | 0 | W 790:620 | W 790:620 | CONFIRMED | new |
| V31_g1f | 1 | W 790:620 | W 790:620 | CONFIRMED | new |
| H | 0 | L 240:500 | L 100:500 | CONFIRMED | new |
| H | 1 | L 240:500 | L 100:500 | CONFIRMED | new |
| G | 0 | D 740:740 | D 740:740 | CONFIRMED | retained |
| G | 1 | D 740:740 | D 740:740 | CONFIRMED | retained |
| N | 0 | W 770:740 | W 770:740 | CONFIRMED | retained |
| N | 1 | W 770:740 | W 770:740 | CONFIRMED | retained |

Fresh external decisions verified in the new campaign receipts: 2400. This checker made zero policy calls and separately replayed recorded actions on the unchanged engine. The eight prior G/N controls retain their original source archives and receipts; they are not new games.

Per-case opening violations, early terminal games, computational failures, audit errors and first paired-history divergences are retained in verification/full_games.json. A refuted hypothesis does not make a completed engine audit fail, and completed audits do not prove a hypothesis.

The source proof establishes conditional opening arithmetic only. Opponent reactions, HP differences and later wall-clock cutoffs prevent an unconditional full-game equivalence theorem. These selected conditions establish no unseen-strength or global-optimality claim. The final candidate and reserved D inputs are unchanged.
