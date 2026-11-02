# Review of economy entry 18.35's foreign-gate explanation

Prepared 2026-10-31T23:57:47.390999+00:00. Reviewer: GPT-6 Astra.

The parenthetical “no attack, finish or doom purchase before foreign_attack_from=11” is inaccurate as a description of frozen econ29's control flow. **Verdict: REFUTED for the claimed shared guard.** The ordinary attack helper checks `hold`; finishing and doom do not. A legal gameplay history that exploits this distinction is **OPEN in this review**. Source inspection alone does not establish such a history.

**Method.** Read the complete frozen AF5/g1 constructor and decision bodies, resolve their exact recorded specifications against literal constructor defaults, and inspect every minion-purchase append and its enclosing predicates. Preserve the captured economy entry, source, specifications and existing record identities in [EVIDENCE.json](EVIDENCE.json). The [standalone proof](PROOF.md) states the conditional result and all relevant branch ordering.

| Purchase path | Foreign `hold` check | Other relevant control flow |
| --- | --- | --- |
| Ordinary attack, including open-case attack | Immediate return while held | Also requires `round >= attack_from`, budget and roster room |
| Finishing attack | No `hold` test | Runs before the open case; requires `round >= attack_from`, budget, room and a modeled killing package |
| Doom attack | No `hold` test | Requires `not attacked`, `round >= attack_from`, remaining budget, modeled loss, room and a package |
| Round-one poke | No `hold` test | Separate round-one branch |

AF5 and g1 use `attack_from=5` and `7`, respectively; both use `foreign_attack_from=11`, `finish="opt"` and `doom="next"`. Their income and idle exceptions to the ordinary foreign hold are disabled. The open-case branch sets `attacked=True` after calling the ordinary helper even if it returned because of `hold`. That assignment can prevent doom. Finishing precedes that assignment. Reservation filtering accepts minion actions, and there is no final foreign-map filter. Thus rounds 5 to 10 for AF5 and 7 to 10 for g1 are not excluded from finish or doom by a shared round-11 gate, but the remaining predicates can still prevent all purchases there.

**Retained-record check.** The 120 completed scnaf5 result rows have 17 retained logs and 103 unavailable histories. I scanned the candidate's accepted actions after each scripted opening and through round 10, or termination if earlier, in those 17 logs and all 28 frr7 logs. None contains a minion purchase in that interval. **Verdict: CONFIRMED for those 45 retained histories only.** This observation neither establishes the parenthetical as a universal policy invariant nor refutes entry 18.35's separately stated 120-condition outcome comparison. That complete comparison was not reproduced here.

The scenario adapter calls the underlying policy during the overridden opening rounds and retains its private effects, while discarding its proposals. Accepted scripted purchases therefore cannot be attributed to the policy's attack branches. The scan excludes those scripted rounds, and no internal finish/doom branch labels exist in the ordinary retained events. No policy, constructor, engine, replay, existing game checker or new experiment was executed.

Suggested replacement: “A possible explanation is the ordinary attack's separate foreign-map hold before round 11. Finishing and doom retain their `attack_from` checks and bypass that hold, subject to their other predicates. This mechanism was not checked game by game.” The narrower wording preserves the conjectural explanation without asserting an unsupported common guard. All earlier review seals remain unchanged.
