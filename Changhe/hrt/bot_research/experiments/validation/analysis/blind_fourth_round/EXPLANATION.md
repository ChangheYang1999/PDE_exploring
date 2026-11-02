# Waiting one more round, and checking whether the wait helps

Two opponents can look identical until the action that distinguishes them is already underway. In this experiment H buys factories through round three; S buys the same factories in rounds one and two, then builds its maze in round three. At decision three the observer cannot see S's pending construction. At decision four it can. T waits for that observation before choosing a permanent continuation. The unconditional control U uses the same opening and private models but always chooses the attacking continuation.

The completed comparison gives a concrete benefit for that choice on these two opponents. Both policies beat H. Against S, T draws and U loses. Each row below was checked in both physical player assignments on the unchanged standard-start engine. HP is candidate first; these are selected deterministic conditions, not independent random samples.

| Opponent | T, chooses at decision four | U, always chooses L4 |
| --- | --- | --- |
| H, the exact empty-map HP handoff policy | Win, 800:656, round50 | Win, 800:656, round50 |
| S, the exact late reserved wall guard | Draw, 740:740, round50 | Loss, -246:800, round12 |

The H comparison is stronger than agreement of these final scores: the complete canonical U/H and T/H histories match in each seat. The S comparison has a different trajectory beginning at round four. The full-game receipts are [T RESULTS.md](../third_round_wait/RESULTS.md) and [U RESULTS.md](RESULTS.md). Exact H parameters and source-level hypotheses are in [PROOF.md](PROOF.md).

## What is being kept while T waits?

T owns two fresh members: G, the fixed guard00 early-wall policy, and L4, the wall-signal repair policy with its one attack moved to round four. L4 itself owns a persistent model of H. While uncommitted, T calls G and then L4 once each on separate copies of the actual public observation, submits G's actions and keeps both private states. It does not run two imagined games. In particular, L4 proposes eight factories in round three, but the real policy instead buys G's splash and five factories. At decision four the selected member receives the resulting real gold and map, not the state that L4's discarded proposal would have produced. Both members retain their private states from the actual earlier observations; only the selected member advances again.

U has the same member construction, call order and submitted first three rounds against H and S. Its difference is the round-four choice: U always retains L4. T retains G when it sees any enemy building or roster entry; otherwise it retains L4. T can also commit earlier on such a signal, but neither of these opponents produces one before decision four. These experiments therefore do not exercise those earlier branches.

## Why thirteen factories can accompany a loss

Both T and U reach decision four with267 gold, fourteen factories and the guard00 maze plus splash. S has261 gold, eleven factories and the same maze and splash. T recognizes this public presence and chooses G, which buys one tier4 for260 gold. S also buys one tier4. Both copies hit, leaving the bases at740:740 that round.

U instead asks its L4 member what the modeled H would do from S's actual state. The model proposes a second splash at(10,1) and ten factories. That proposed splash creates a44-edge route with seven adjacent cells. Each proposed tier2 has70 HP and would take at least70 splash damage before arrival. The forecast therefore cancels the attack. Since modeled H also sends no attackers, U builds no new defense and buys thirteen factories with its267 gold.

That forecast is a legal calculation from public information, and the private model has been advanced correctly. It is still a forecast of the wrong opponent. Actual S buys its tier4 rather than the modeled splash and factories. The copy reaches U, and S takes no damage. Closing round-four states are:

| Policy against S | Own gold | Own factories | Own HP | S HP |
| --- | ---: | ---: | ---: | ---: |
| T | 264 | 14 | 740 | 740 |
| U | 454 | 27 | 740 | 800 |

U has190 more gold and thirteen more factories at this point. The opening calculation does not prove that this trade loses. The complete matches establish the separate later loss at round12. The mechanism audit verifies the actual and predicted actions, member call order, private-state agreement, map paths, income, rosters and HP through round four; it does not replace the full-game evidence.

## What this comparison establishes

Protocol161 used four new T games and two retained G/S controls. Protocol162 used four new U games and the four completed T controls. The respective fresh-policy checks regenerated400 and248 external decisions. A separate U component audit made124 U,12 G-reference and124 L4-reference calls; nested model calls are recorded as subsets. These checks found legal submissions, unchanged input observations and exact required histories. Reused controls and regeneration calls are not counted as new strength samples.

This is evidence that the observation-based choice matters on this fixed H/S pair. It is not a claim that T identifies arbitrary opponents, that a building signal is generally reliable, or that more factories are generally harmful. T is also outside protocol159's restricted early-commitment class: it commits later and uses L4, whose discarded round-three proposal differs from the earlier L member. Its improvement does not contradict that conditional bound.

Later planners use wall-clock cutoffs. Private-state snapshots omit clocks, module globals and alias identity. The measured history agreements therefore apply to the retained executions; a general equivalence theorem would need the stronger coupling hypotheses stated in the proofs. The selected final best_v9e and the reserved final-validation conditions are unchanged by this experiment.
