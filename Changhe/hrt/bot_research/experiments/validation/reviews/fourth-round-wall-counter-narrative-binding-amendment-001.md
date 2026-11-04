# Protocol163 narrative scope clarification

Prepared UTC: 2026-10-31T22:41:05.469388+00:00.

This GPT-6 Astra author amendment preserves the initial narrative and adds the independent reader's requested audit-accounting detail. The additional private audit constructed four cold reference F38 instances and made zero reference F38 decision calls. These are separate from the 696 ordinary fresh external decisions. The declared protocol and completed mechanism audit support this sentence; no policy, constructor, game, replay or checker call was performed to write or check the clarification.

Original narrative SHA256: `ad0be087de1cf266833e1bb3ca0bccbd80394ef236d7f60d8a0d3f736cacd0a7`, written 2026-10-31T22:38:27.677791+00:00, 844 whitespace-delimited words. The original [author binding receipt](fourth-round-wall-counter-narrative-binding-001.md) remains unchanged at SHA256 `a7439e3c17f21a14d5ce7490bf0eed6028e52640e856e8f72187cb3349d57f19`. It describes the original narrative bytes.

Clarified [EXPLANATION.md](../analysis/fourth_round_wall_counter/EXPLANATION.md) SHA256: `a4a53b0a6e37858ff38f60b5667e54ea36ede26baea518a50caf361ed166edd8`,868 whitespace-delimited words. Its only changes are the dated clarification metadata and one factual sentence. The original experimental source, proof, protocol, declaration and all results remain unchanged. The independent reader should bind the clarified identity in its completed review. A coordinator publication receipt should name this amendment together with the earlier author receipt and final independent review; neither author receipt is a prospective game declaration.

The unchanged result receipt remains [verification/full_games.json](../analysis/fourth_round_wall_counter/verification/full_games.json), SHA256 `1d200095e79e23b5179ccca59911ea2eb878835ab479b67c2e6b0e92d7f92aa8`. The unchanged [PROTOCOL.md](../analysis/fourth_round_wall_counter/PROTOCOL.md) is SHA256 `e168138b5cb77a8f51e411e83a91565a54c2f17dee55d44e37e31652e94d4aec`. Five relative narrative links still resolve, and the narrative contains no em dash or absolute local path.

No JavaScript/TypeScript, servers/listeners, RLScience or other cluster, remote compute, GPU, Lean/lake, protected writes, git commit/push or online posting was used. No D parameters or results were inspected, and its waiter was untouched.

The exact original narrative UTF-8 text, including its final newline, is retained between the following fences. Its SHA256 is the ad0be087de1cf266833e1bb3ca0bccbd80394ef236d7f60d8a0d3f736cacd0a7 identity above.

```markdown
# Protocol163: forecasting the wrong fourth-round policy

Written UTC: 2026-10-31T22:38:27.677791+00:00. Audit completed UTC: 2026-10-31T22:37:11.017297+00:00.

At decision four, V has an empty map, 291 gold and 17 factories. Its first three rounds match the factory opening of H, the policy modeled by its opponents. H's next action would leave six tier2 attackers alive. V's actual next action kills all six combat copies. The forecast has the correct public state and model chronology; its assumed policy differs from V's policy. The [opening proof](PROOF.md) derives this mismatch under the unchanged balanced rules, and the [completed audit](verification/full_games.json) checks it in all four declared T/U games.

T, ThirdRoundWait, initially submits guard00 policy G while also advancing L4, a repaired forecaster using one persistent H model. Through rounds one to three, G and L4 each consume the actual observation; L4's proposals are discarded. Its third-round factory proposal therefore changes neither engine gold nor buildings, but its model advances. T commits to L4 at decision four when V still shows no buildings or roster. U, BlindFourthRound, commits to L4 at four unconditionally. Both decide before V's same-round walls become visible. T's commitment persists when those walls appear in the next observation.

Here is the exact opening in either physical assignment. F means one factory; W is the twenty ordered guard00 walls, X is splash(1,3), and T2/T4 are tier2/tier4 purchases. Lists execute left to right. Closing figures are gold / factories / base HP. Both rosters are empty through three; T/U has map W through two and W+X thereafter, while V stays empty through three and has W+X thereafter.

| Round | V actions | T/U actions | V closing | T/U closing |
| ---: | --- | --- | --- | --- |
| 1 | 5F | W, 4F | 97 / 5 / 800 | 100 / 4 / 800 |
| 2 | 4F | 5F | 174 / 9 / 800 | 175 / 9 / 800 |
| 3 | 8F | X, 5F | 291 / 17 / 800 | 267 / 14 / 800 |
| 4 | W, X, 10F | 6T2, F | 458 / 27 / 800 | 274 / 15 / 800 |
| 5 | T4, 9F | 13F | 605 / 36 / 800 | 476 / 28 / 740 |

At four, H forecasts splash(10,1), called Y, followed by eleven factories. The Y-only shortest route has 22 edges and five splash exposures. Each tier2 has 70 HP, takes 50 damage, and would hit for 12: six predicted hits give 72 base damage. V instead builds W+X, making a 42-edge route with seven exposures. Each tier2 takes 70 damage and dies. The six purchased roster entries persist and respawn next combat; killing their combat copies does not remove those entries.

At five, H receives V's actual 458 gold, 27 factories and W+X, rather than its earlier hypothetical Y map. It predicts 22 factories and no incoming roster. T/U buys thirteen factories without another timed attack or repair. V instead buys a 260-gold tier4 with 560 HP. It survives 70 splash damage, hits for 60, and earns a five-gold bounty. V closes with 458-260-180+42+540+5=605 gold. The renewed tier2 copies again die. These are the [prospectively specified](PROTOCOL.md) five-round mechanics, now confirmed by the audit.

From decision six, V delegates once per round to its retained default frozen Fortress38. The [implementation](../../../../bots/counters/fourth_round_wall.py) constructs that callable once with literal no-argument `make()`. It receives no opening observations or decisions, preserving default attack_share=0.25 and its initial private history. Its first actual input includes V's 605 gold, 36 factories, W+X and one tier4. The scripted walls were not placed by that private history, so its foreign-map handling remains relevant.

The ten selected development conditions all start empty with 100 gold and 800 HP under the standard balanced rules. Each table cell is one fresh game, reported as V's outcome, V:opponent final HP, and ending round. G is guard00; B is frozen best_v9e; N is the same source with attack_share=1.0 and catch_up_share=0.5.

| Opponent | V seat 0 | V seat 1 |
| --- | --- | --- |
| T | W, 800:-546, r12 | W, 800:-546, r12 |
| U | W, 800:-546, r12 | W, 800:-546, r12 |
| G | L, 680:740, r50 | L, 680:740, r50 |
| B | L, 755:800, r50 | L, 755:800, r50 |
| N | L, 755:800, r50 | L, 755:800, r50 |

The [results](RESULTS.md) retain all ten conditions: 4W/0D/6L. Ten complete engine replays and 696 fresh external decisions reproduced the recorded actions; the additional private audit covers only the first five rounds of the four T/U histories. Those matched T/U canonical histories also agree through termination in each V seat. The theorem's continuation requires equal decision-relevant inputs and deadline outcomes; later Fortress34/Fortress38 searches have time cutoffs. These observed histories do not prove unconditional clock coupling or later private-state equivalence. V targets disclosed T/U behavior, and its six G/B/N losses limit the strength claim to that targeted success. Reserved D contributes no evidence here.
```
