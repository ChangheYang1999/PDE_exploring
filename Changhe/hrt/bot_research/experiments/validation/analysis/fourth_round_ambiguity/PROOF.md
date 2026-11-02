# A conditional bound for selection at the fourth decision

Prepared UTC: 2026-10-31T22:26:13.069893+00:00.

This argument is written before the prospective V games. It proves a source-level shared prefix and an exact conditional matrix theorem. It does not assert any unmeasured V payoff. The numerical application remains OPEN until compatible full-game evidence is checked. No policy or engine calls are made by this proof.

## Exact policies and hypotheses

G is EarlyWallGuard(witness='guard00'). U is BlindFourthRound() with no overrides. U owns fresh G and fresh WallSignalRepair with attack_round=4. It calls both on separate copies of each actual observation in rounds one through three, submits only G's list, retains both private transitions, and from round four calls only that same WallSignalRepair. U never pretends that its discarded proposals were played.

H is HPHandoff with the exact shared_prefix_selector.HP_PARAMETERS: empty layout, growth_rounds=6, no bait, bait_round=2, tier5, factory_cap=2000, purchase_cap=1000, replan_iters=5000, deadline=12, lead_from=8, with remaining constructor defaults. Its guards are scheduled for rounds four and six. V is the prospective policy of ../fourth_round_wall_counter/PROOF.md: buy all affordable factories in rounds one through three; build the guard00 walls and splash and fill factories at four; buy at most one affordable tier4 and fill factories at five; use its retained, previously uncalled, default Fortress38 from six. The prior V argument gives the complete specification, routing lemma and first-five-round calculations.

Use the unchanged standard bundled game: 100 initial gold, 800 HP, empty 12 by 12 maps, no factories or roster, factory cost20 and income15, wall cost1, path income1 per edge, round limit50. Calls start at round one, proceed consecutively at one fixed physical player index, succeed, and receive actual public observations. No external code mutates private state. Sources and data have the identities listed below. Modified scenarios, failed or repeated calls and midgame initialization are excluded.

Fix one physical selector seat. Normalize only the two player snapshot names to 'selector' and 'opponent'. The other indices, rules and public fields remain unchanged. Raw names can distinguish policies, so the theorem is explicitly about normalized observations. Benchmark metadata, opponent source labels, file names, private objects, pending actions, process identity, timing signals and other identity-correlated side channels are excluded from the selection information.

## Restricted selector class

A selector owns correctly advanced instances of G and U. Until commitment it submits their shared ordered list. It irrevocably chooses one arm no later than decision four, before either pending round-four list is visible, and subsequently submits that arm's entire list without modification or reselection. It may choose earlier or use a stopping rule. Every selected arm receives exactly the actual history needed to reach its corresponding standalone logical state. Calling both arms on copied observations before commitment is one implementation, but retaining U's discarded internal model state is essential.

Selection may depend on normalized observation history, past submitted actions, fixed prior knowledge of these four policies and private randomness independent of whether H or V was chosen. Decision-relevant private transitions on matched prefixes must agree under a coupling. External clocks, globals or randomness cannot supply extra information about the opponent. For the payoff theorem, conditional on selection of an arm, its entire continuation and the opponent must reproduce the stated baseline payoff. This last condition is additional to prefix equality: Fortress planners have time cutoffs, so extra shadow work need not preserve later choices under arbitrary load.

The adversary chooses fixed H or V without observing the realized private choice. The objective is the smaller of the two expected payoffs, not the expectation of a minimum after revealing that private choice. A new response, changed opening, late commitment, reset or repeated reselection is outside this class.

## Shared-prefix lemma

Against either H or V, G and U submit precisely the same first three ordered lists. After each completed round the public states, apart from the normalized names, are:

| Round | Selector gold / factories / path | H or V gold / factories / path | HP and roster |
| --- | --- | --- | --- |
| 1 | 100 / 4 / 40 | 97 / 5 / 22 | both800, empty |
| 2 | 175 / 9 / 40 | 174 / 9 / 22 | both800, empty |
| 3 | 267 / 14 / 42 | 291 / 17 / 22 | both800, empty |

Proof. Let W be the ordered twenty guard00 walls and X its splash at(1,3). The guard00 routing argument proves path length40 for W and42 for W+X, with all build prefixes legal. G submits W followed by four factories, then five factories, then X followed by five factories. Its closing balances are 40+4*15=100; 40+9*15=175; and175-60-5*20+42+14*15=267. U submits these same lists by definition. Its additional L4 calls and their discarded proposals mutate only private owned state.

H has no bait, guard before four, or possible handoff in the first three rounds. V's rule explicitly buys only factories. Both therefore submit five, four and eight factories in sequence. Their empty path remains22. Closing balances are22+5*15=97; 97-4*20+22+9*15=174; and174-8*20+22+17*15=291. Neither side buys a minion in these rounds. There is no damage or bounty, so both HP values remain800 and the game reaches decision four.

With the same actual lists, the unchanged deterministic engine produces the same completed public states in each comparison. The observer at decision four sees completed round three, not V's newly pending walls or H's newly pending guard. Therefore all permitted selection inputs through that decision agree. Corresponding G and U private states also agree, by induction over their copied actual observations and the stated transition coupling. In particular, U's H model has consumed three actual observations once each; its unused round-three factory proposal was never substituted for the actual X-plus-factories list. This proves the lemma.

## Conditional exact theorem

Assume the selected standalone payoffs, from the arm's perspective, are the following compatible table, with q in {-1,0,1}:

| Arm | H | V |
| --- | ---: | ---: |
| G | -1 | q |
| U | +1 | -1 |

Payoff is+1 for a win,0 for a draw and-1 for a loss, with terminal labels from the unchanged engine. These are hypotheses, not claims about the still unplayed V comparisons. The full-continuation coupling stated above is also assumed.

Then the best restricted worst expected payoff is (q-1)/(q+3). For q=0 it is-1/3, uniquely at probability2/3 of choosing G. For q=1 it is0, uniquely at probability1/2 of choosing G. For q=-1 it is-1 for every choice probability. Every deterministic selector has worst payoff-1 in all three cases.

Proof. Couple the private selection randomness between H and V. By the lemma every allowed input and corresponding private transition through the commitment deadline agrees. Thus the same commitment event and selected arm occur, even for an earlier stopping rule. There is one probability p in[0,1] of choosing G against either opponent. The conditional payoff premise gives

    u_H(p) = 1 - 2p,
    u_V(p) = (q+1)p - 1.

For q>-1 the second term is strictly increasing and the first strictly decreasing. Their unique intersection is p=2/(q+3), which lies in[0,1]. At this point both equal(q-1)/(q+3). Below the intersection u_V is strictly smaller; above it u_H is strictly smaller. This proves optimality and uniqueness of the probability. It does not claim uniqueness of the implementation or random seed representation.

For q=-1 the second term is identically-1 and the first is at least-1, so their minimum is-1 for every p. This separately treats the degenerate case, where the intersection calculation alone would not prove uniqueness. A deterministic selector has p=0 or1 and minimum-1 regardless of q.

Attainment uses independent private randomness to choose the required arm probability while preserving the common prefix and correctly advanced member state. An exact dual witness mixes H with probability(q+1)/(q+3) and V with probability2/(q+3). Either pure arm then has payoff(q-1)/(q+3). These probabilities are nonnegative and sum to one, including q=-1. This proves the theorem.

The theorem applies separately to each physical seat. If the same table and coupling hold in both, seat-dependent probabilities cannot improve the stated maximum of the minimum over both opponents and seats. For q>-1 attaining that value in both seats requires the displayed optimal probability in each.

## Evidence and scope

The source lemma is proved under the exact rules and definitions above. The payoff theorem is proved conditionally. A later application must extract G/H and U/H records plus both physical assignments of G/V and U/V, verify exact policy and data identities, and verify complete game outcomes. It must compare the first-three normalized public histories and retain any contrary payoff or failed audit. If U/V is not a loss, the displayed numerical application does not follow. If G/V has a different q in the two seats, each seat requires its own table before taking a combined worst case.

Finite replays can support compatibility of the displayed baseline traces; they cannot prove that all future time-limited planner executions reproduce them. This is not an impossibility result for arbitrary bots or all later commitment times, and it does not prove an infinite counter-strategy cycle. The theorem concerns selection between these two fixed responses after this common opening. A policy that attacks, builds or changes its response differently can escape the class.

No implementation of a new selector, no game and no formal proof-assistant verification is claimed here. This conditional argument does not use reserved D parameters and does not change the published best.py.

## Dependency identities

The following source and proof identities were read at preparation time. The prospective V implementation is not yet sealed; its reference is the previously checked specification proof. A later empirical application must bind the actual implementation and its complete source/data closure separately.

| Project-relative input | SHA256 |
| --- | --- |
| `bot_research/bots/counters/early_wall_guard.py` | `5c5e8eba684eecafc8f1267036866d57319a6932d187ca479564b7cbf0387811` |
| `bot_research/bots/counters/blind_fourth_round.py` | `2a064ba6d912c8ac177263b552b4c19e030f9e9168e3575704ac20c7e41cfea7` |
| `bot_research/bots/counters/shared_prefix_selector.py` | `7b2c2a0c570f140cf84a5908293bc7835718652a4c71ec2071745e3e61c1c5e7` |
| `bot_research/bots/counters/data/early_wall_guard_001.json` | `ba73f1f9dd50b5c199d6c6e89f2c1555f6baed35f082fc2f242e13108a256334` |
| `bot_research/experiments/validation/analysis/fourth_round_wall_counter/PROOF.md` | `d963f2d9cf20e6c764a37258b145970fbe137d4beec0c80c8850a94b1011f93f` |
| `bot_research/experiments/validation/analysis/blind_fourth_round/PROOF.md` | `878f134149895df9d5672a93142a9533df3bdf9d0b9cca387c5ad77b564b3d2f` |
| `td_game/engine.py` | `c911397bf419cd2f879de4f91dadb0f177b4c964e95a7cc90941af60f415267d` |
| `td_game/balanced.json` | `2f9a761870c38dc162522fd9fbafe8ff989a1098506fcdc4780047cfa35154b1` |
