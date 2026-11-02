# A fixed three-policy game after counter adaptation

Written 2026-10-31T17:33:34.729194+00:00, before the new edge or self-play games.

## Exact question and fixed policies

Use three fixed policies: B is frozen best_v9e; D is the adaptive DelegatedRouteSelector with the frozen Fortress38 continuation; C is the already tested StatefulPublicTiming attacker at round3/tier2, defense_first=false, attack_share=1, count_cap=200, keeping a private D model. C keeps that same model against B and itself. Retargeting it separately for every edge would define different policies and would not produce a three-policy game.

The observed C-over-D edge motivates the test, and D has beaten B in the earlier transfer. The claim under test is the directed cycle B>C>D>B. Declare both assignments of the missing C-versus-B edge and both assignments of all three self-play cases, eight new games. Reuse both assignments of C-versus-D from delegated-forecaster-fortress38-00-002 (case0000/0001) and D-versus-B from recent-transfer-04-001 (case0000/0001). The latter campaign was declared before this analysis and may still be completing. Keep all twelve rows, whether or not a cycle exists. Reuse adds no new experimental samples.

## Policy identity and public information

D's omitted mode parameter in the C-versus-D campaign means mode='adaptive' by its constructor. The other D specification writes this default explicitly. Both use identical source and delegate parameters. Check this semantic identity by parsing the specifications with their defaults. B is the same frozen module throughout. C's full factory specification is identical on every edge. Public displayed names differ across pairings, but these three policies and their invoked components do not branch on those names; the actual fresh action checks use each recorded observation including its unchanged names. No hidden opponent submission is provided to C's private model.

The original engine defines each outcome. Write A_ij=1 when fixed policy i wins against j, -1 when it loses, and 0 for a draw. First require agreement between both physical assignments for each pairing. Self-play is measured explicitly rather than inserted as an assumed zero. If those checks pass, orient the paired outcomes into a skew-symmetric three-by-three table with zero diagonal. This finite table describes the recorded conditions, not arbitrary future loads or unseen opponents.

## Conditional mixture proof

If the measured strict cycle B>C, C>D, D>B holds and all three diagonals are zero, then every row and column of A sums to zero. The uniform distribution p=(1/3,1/3,1/3) satisfies p^T A=(0,0,0) and A p=(0,0,0). Therefore it guarantees expected utility at least0 against every mixture over the same three policies, while an opponent using p holds every such mixture to at most0. The finite game's maximin value is exactly0, and p is optimal for both players. This is direct rational arithmetic, not a claim that p is strong against any fourth policy. If the cycle is absent, report the actual table and do not claim this certificate.

## Verification and scope

All new rows require strict condition accounting, archived sources/data, original-engine replay and fresh regeneration of both actual policies. An incorrect private opponent model is permitted on the C-versus-B and C-versus-C edges; its hypothetical predictions are not real opponent actions. The existing C-versus-D edge additionally has exact forecast checks. Rehash each reused result, source receipt and replay, and retain its original audit references. The D-versus-B edge has fresh counter and independent handoff checks. Report outcomes, final HP, round, reused/new counts, unique full histories, errors, legality and observed runtime.

This is a post-challenge empirical policy game. It is neither held-out validation nor evidence of a universally optimal policy. Clock-limited teammate planners make future load-independence an additional unresolved question even when all measured repeats agree.
