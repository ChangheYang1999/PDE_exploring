# Two indistinguishable opening rounds

Checked 2026-10-31T21:48:19.045046+00:00.

H1 identical normalized public prefixes: CONFIRMED.
H2 the declared two-by-two payoff table in both physical seats: CONFIRMED.
H3 retained R/L state and complete-control checks: CONFIRMED.

Twelve previously recorded games were replayed to their exact terminal boundaries on the unchanged engine: eight G/L baselines against H/S and four R controls. No policy was instantiated and no new match was run. Exact specifications, source/data hashes and recorded legal actions were checked. The first three observations and both completed early rounds were compared in each fixed physical seat after changing only player snapshot names; H1 above gives the outcome of that comparison.

| Member | H, seat0 | H, seat1 | S, seat0 | S, seat1 |
| --- | ---: | ---: | ---: | ---: |
| G | -1 | -1 | 0 | 0 |
| L | 1 | 1 | -1 | -1 |

The conditional theorem applies to this measured table: a selector restricted to committing to G or L by round three has value -1/3, uniquely at probability 2/3 of G, provided its selected continuation is coupled to reproduce the corresponding baseline payoff. The dual mixture puts probability 1/3 on H and 2/3 on S. These are exact rational equalities.

The public-prefix comparison uses direct engine replay. Logical member-state equality is evidence from the earlier R audits, whose retained bytes are checked here; it was not freshly rerun in this calculation. General continuation coupling is an explicit hypothesis, not an unconditional property established by these twelve histories. Wall-clock planning, extra shadow work or other scheduling changes may affect future decisions.

The result is restricted to the stated opening, information set, two members and commitment deadline. Later commitment, a different opening, a third response, identity side channels or reselection falls outside the claim. Nothing here changes best_v9e or uses reserved D. Read PROOF.md, then PROTOCOL.md and verification/full_check.json.
