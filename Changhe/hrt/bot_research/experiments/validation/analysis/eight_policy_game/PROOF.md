# Extending the fixed policy game with the repaired signal attack

Declared 2026-10-31T19:44:55.890624+00:00, before any new extension game.

## Exact objects and claims

Use B,C,D,G,H,I,J with exactly the source bytes and parameters of the completed seven-policy table. Add L, the guarded free-planner signal attacker from wall_signal_repair/PROOF.md, including its pre-call full-action comparison clarification. No L parameter changes are allowed. Its six games against H,I,J have finished with four wins and two draws, but their fresh regeneration checks are still pending at this declaration. They count only after the full parent receipt passes.

Run L against B,C,D,G and L itself, both physical assignments, ten new standard-start games. Reuse all 56 seven-policy games and the six validated L-H/I/J games, for 72 total records and 36 assignment pairs. H1: L is nonnegative in W/D/L against every other included policy. H2: the previous equal B/H/J mixture remains nonnegative against L. Both questions are OPEN until complete records and checks are available. Publish all outcomes, even if H1 or H2 is refuted.

## Finite-game argument

For each unordered policy pair, require two complete legal games with matching normalized action/state histories after changing player perspective and names. Also require a drawn, symmetric self-pair for each policy. Define A_ij=1,0,-1 from the original engine's winner field for policy i against j, and A_ji=-A_ij. Under these checked conditions A is skew symmetric, with diagonal zero. Do not infer HP-sign outcomes when both bases die.

If a rational vector p has nonnegative entries, sum one, and every entry of p^T A is nonnegative, it guarantees payoff at least zero against any distribution q on these eight columns by weighted summation. Skew symmetry yields A p=-(p^T A)^T, so the same distribution p as the opponent limits every row mixture to at most zero. Hence the exact value on this fixed table is zero. A solver may propose p, but all these inequalities and the normalization must be checked independently with exact rational arithmetic. If no checked certificate is found, leave that certificate claim OPEN. H1 follows only from inspecting every entry of L's row; H2 follows from the exact average of the B,H,J entries in the L column.

## Dependencies and scope

Use the unchanged engine, strict job accounting, original-engine replay, source/data identity and fresh regeneration of both action streams for all ten new games. Recheck all immutable parent receipt inputs, decompressing retained replays where needed. Parent studies establish the reused games' checks; they are not new samples. Keep separate counts for new games and reused records.

This is a deliberately selected extension after an observed counterexample, not a random opponent sample or a held-out test. Some policy dependencies have clock limits; exact observed histories do not prove every future run is identical. The certificate applies only to these fixed entries, standard start and verified histories. It does not establish an unrestricted equilibrium or displace pool D. No installed best.py is used; B is its earlier frozen best_v9e copy.

Declaration completion 2026-10-31T19:45:21.868143+00:00: the first metadata helper read the three-opponent wall-signal dictionary and stopped with KeyError B before writing a manifest or calling a policy. The corrected helper reads the full seven-policy dictionary. The fixed opponent list and mathematical protocol are unchanged.
