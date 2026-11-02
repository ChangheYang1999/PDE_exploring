# Transfer of the screened-roster guard

## Exact empirical claims

Fix the unchanged balanced engine, standard starts, both player assignments and the six opponent specifications in screened-guard-transfer-campaigns-001.json. They are AS1C, AS1, best_v9f, Fortress41, V29 with attack_from=7, and V29 with r1_guard=60. AS1C and AS1 use the frozen best_v9e source with the parameters named in the declaration. The V29 base parameters are copied from the economy lane's fixed g1 specification; the guard60 variant replaces attack_from=7 with r1_guard=60.

The guarded candidate is screened_roster_guarded with its default Fortress38 continuation. The matched control is screened_roster_continuation with order=screen and continuation=fortress38. Both were implemented and tested against best_v9e before this declaration. The only policy change between these two candidates is the additional round-six wall proposal, subject to the guarded policy's existing legality check.

H1: the guarded candidate wins both assignments against AS1C. H2: on every one of the twelve opponent-and-seat conditions, the guarded candidate's result is at least its control's in the order loss < draw < win. Both claims are OPEN before the 24 new games. These predictions are separate from the lead's H14 gate. A failure here does not silently redefine that gate.

## Reasoning and necessary checks

The policies request the same actions through round five. If their decisions are deterministic on the reached histories, the identical start and engine transition give identical histories through that round by induction. A legal extra wall package changes later routing, income and observations. Therefore a favorable local damage result against best_v9e proves neither H1 nor H2 against these other policies. Full games are required. The control is rerun against each declared opponent; no best_v9e game is counted again.

Every game starts fresh. Source and exact JSON dependencies are pinned before calls. Strict checks account for every condition and failed attempt. Complete original-engine replay checks the recorded transitions. Fresh instances of both factory policies must regenerate all submitted actions without changing observations and with legal submissions. Both assignments are retained, with normalized history equality reported separately. If reproduction fails, the empirical claim remains OPEN until the discrepancy is explicitly resolved; failed attempts are preserved.

## Scope and dependencies

This is transfer across a selected set of known development policies, including the lead's newly proposed attack-budget change. It is not held-out evaluation, a random sample, or a proof of global strength. The existing Fortress38 and Fortress41 time cutoff remains a limitation outside the verified executions. The installed best.py is not edited; pool D remains unused. Dependencies are the exact candidate and opponent source closures, the screened guard JSON, the immutable rules, and the declared runner and audit programs. Reproduction uses the existing Python environment with bytecode disabled, the research temporary directory, assigned CPU affinity, low priority and one numerical thread.
