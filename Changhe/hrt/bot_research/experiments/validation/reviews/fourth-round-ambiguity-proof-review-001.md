# Independent review of the fourth-decision ambiguity proof

Prepared UTC: 2026-10-31T22:28:35.509831+00:00.

Verdict: READY for use as a conditional source theorem. The shared-prefix argument and matrix calculation are CONFIRMED under their stated hypotheses. The numerical empirical application is OPEN. No material mathematical or state-information defect was found, and no proof edit is requested.

The reviewed proof is analysis/fourth_round_ambiguity/PROOF.md at SHA256 e2beead506f57753d722fff5f0724bdf1e66d9068311823df9b1945c05fec757. I read the full proof and index, checked its eight direct source/proof hashes against the preparation receipt, and separately inspected the H inheritance chain, persistent public model, U/G decision rules and engine observation construction. The V specification is supplied by its previously checked standalone proof. This review did not import a policy, construct a bot, call a decision, replay a game or evaluate an outcome. The only arithmetic execution used exact rational numbers for the three declared matrix cases.

The common first-three prefix is correct. G and U both submit W F^4, F^5 and X F^5 because U submits its retained G member through three, even when L4 proposes a different third list. H's empty MazeGrower has no bait, guard or handoff in those rounds; V explicitly buys factories only. Both opponent lists are F^5, F^4 and F^8. These lists give selector balances100,175,267 and opponent balances97,174,291, with factory counts4,9,14 and5,9,17 respectively. W has40 edges and W+X has42; the opponent map remains empty with22 edges. Empty rosters give zero damage and bounty. Builds, names excepted, full ordered building lists and all other public fields therefore agree, not merely the displayed income totals.

Engine.observation exposes the next round number, fixed physical player index, two completed snapshots and rules. It does not include pending submissions or record metadata. At decision four, the newly planned H splash and V walls are still absent. Raw snapshot names are an actual distinguishability channel, so the explicit identity normalization and exclusion of source labels, timing/process information and other opponent-correlated side channels are necessary. The proof includes these restrictions. They must also be enforced by any later selector implementation or evidence interpretation; equal economic tables alone would not suffice.

The state condition is also explicit enough. U owns its own correctly advanced G and L4. Discarded L4 proposals are retained only as private transitions, while each next decision consumes the actual common observation. Its persistent H wrapper receives consecutive rounds once each. Choosing U after a G prefix therefore requires this advanced U state, including its internal model, rather than a fresh U/L4 constructor at four. A selector can commit earlier and stop calling the unused arm without changing the shared submitted opening. The proof's private-transition coupling excludes information leaked by differing hidden clocks or globals. Against coupled H/V prefixes the same selection stopping rule and realized random choice occur. Thus one common probability p of choosing G applies to both opponents.

Independently deriving the two conditional expected payoffs gives u_H=1-2p and u_V=(q+1)p-1. For q>-1, one decreases strictly and the other increases strictly. Below p=2/(q+3) the second is the smaller; above it the first is smaller. Their intersection is the unique optimal probability and has value(q-1)/(q+3). For q=-1, u_V=-1 identically, so all p in[0,1] are optimal with value-1. The claim of uniqueness is correctly restricted to q>-1 and to the probability, not the implementation. Both deterministic endpoints have worst payoff-1.

| q | Optimal probability of G | Restricted worst expected payoff | Dual probability of H / V |
| ---: | --- | ---: | --- |
| -1 | any p in[0,1] | -1 | 0 / 1 |
| 0 | 2/3, unique | -1/3 | 1/3 / 2/3 |
| 1 | 1/2, unique | 0 | 1/2 / 1/2 |

The dual distribution is correct: H has mass(q+1)/(q+3), V has mass2/(q+3), and either pure arm earns(q-1)/(q+3). All masses are nonnegative and sum to one, including the degenerate case. This proves both attainment and an upper bound for the stated fixed-opponent, private-randomization objective. It would not justify averaging a minimum after the adversary learns the realized choice. The proof distinguishes those objectives.

The table entries G/H=-1, U/H=+1 and U/V=-1 are hypotheses, as is G/V=q. The proof makes no unmeasured V outcome assertion. Full-game arm/opponent payoff reproduction after commitment is a further premise, not a consequence of the shared prefix. Frozen Fortress34 and Fortress38 planners contain wall-clock deadlines. Shadow work can change later searches even when no policy call fails. The explicit continuation-coupling premise correctly protects the mathematical statement; a finite set of matching replays cannot remove it. A failed V payoff or fresh audit must leave the intended empirical application OPEN or refute its proposed table, without changing the conditional theorem.

The fixed-seat analysis and both-seat corollary are correct when the same q/table and continuation premise hold in both seats. If q differs by seat, the two matrices must be evaluated separately before taking a combined worst case. The stated uniqueness across both seats applies only when their common optimum is the same. This remains a theorem about selecting these two complete responses with commitment by decision four. A new opening, new arm, fifth-round observation or repeated reselection can escape the restricted class. No unrestricted game value, infinite counter cycle, universal deadline-independent equivalence or empirical strength claim follows.

All reviewed input identities follow. The source-only inventory supplements the proof's receipt; it is not a runtime closure certificate or an experimental declaration.

| Project-relative input | SHA256 |
| --- | --- |
| `bot_research/bots/counters/blind_fourth_round.py` | `2a064ba6d912c8ac177263b552b4c19e030f9e9168e3575704ac20c7e41cfea7` |
| `bot_research/bots/counters/data/early_wall_guard_001.json` | `ba73f1f9dd50b5c199d6c6e89f2c1555f6baed35f082fc2f242e13108a256334` |
| `bot_research/bots/counters/early_wall_guard.py` | `5c5e8eba684eecafc8f1267036866d57319a6932d187ca479564b7cbf0387811` |
| `bot_research/bots/counters/forecast_timing.py` | `31e73f1a98f8cb70b9ddacfd2067a34e752450c53648a42482d934fcc92be78a` |
| `bot_research/bots/counters/hp_handoff.py` | `c5baa3d7af48508d0cf10cbac0950a018673c45e3b3cba3f0522324da5ea8ee6` |
| `bot_research/bots/counters/maze_grower.py` | `d541a6f2de7b44e6280c7296b58f6844bb2bebf574dcf8f0f32e7c1a7dbfd5f0` |
| `bot_research/bots/counters/screened_guard_maze.py` | `d0df94929a24405a959a0f686a4dadf16da8317176b3bf9074fd82562afe4cc4` |
| `bot_research/bots/counters/shared_prefix_selector.py` | `7b2c2a0c570f140cf84a5908293bc7835718652a4c71ec2071745e3e61c1c5e7` |
| `bot_research/bots/counters/staged_guard_maze.py` | `32778c35fda27c0432aa9f4931756bde33f156adabf44306e2548c773a977351` |
| `bot_research/bots/counters/stateful_public.py` | `c2cde121ecf8c1475daee2958f97a1a1b9c08794bee4cf6ead7a05924b4c2c7b` |
| `bot_research/bots/counters/wall_signal_timing.py` | `63d7681bec8ac9fb5c3855d172be8c2e3a6b3a591bdf8e746efc1d9b4e754146` |
| `bot_research/bots/defense/frozen/v34/plan.py` | `6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f` |
| `bot_research/bots/defense/frozen/v38/plan.py` | `6b288feb47314c4b28c918c3100b750a0072d1ca657c6e1fc3a5138373a10b2f` |
| `bot_research/experiments/validation/analysis/blind_fourth_round/PROOF.md` | `878f134149895df9d5672a93142a9533df3bdf9d0b9cca387c5ad77b564b3d2f` |
| `bot_research/experiments/validation/analysis/fourth_round_ambiguity/INDEX.md` | `29f44821a296a615f2f392a4456ae89778454692070958773d7cda90a4e61519` |
| `bot_research/experiments/validation/analysis/fourth_round_ambiguity/PROOF.md` | `e2beead506f57753d722fff5f0724bdf1e66d9068311823df9b1945c05fec757` |
| `bot_research/experiments/validation/analysis/fourth_round_ambiguity/verification/source_inputs_001.json` | `183f56134f6506545de66041032fb82d9c4f30cfbd4d2abc8858305a91d58892` |
| `bot_research/experiments/validation/analysis/fourth_round_wall_counter/PROOF.md` | `d963f2d9cf20e6c764a37258b145970fbe137d4beec0c80c8850a94b1011f93f` |
| `td_game/balanced.json` | `2f9a761870c38dc162522fd9fbafe8ff989a1098506fcdc4780047cfa35154b1` |
| `td_game/engine.py` | `c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d` |

No JavaScript/TypeScript, server/listener, RLScience or other cluster, remote compute, GPU, Lean/lake, protected-file write, git commit/push or online posting was used. Reserved D parameters were not inspected. The proof and all reviewed sources remain unchanged.
