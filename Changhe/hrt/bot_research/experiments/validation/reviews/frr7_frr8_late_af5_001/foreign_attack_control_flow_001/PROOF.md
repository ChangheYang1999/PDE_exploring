# Scope of the frozen AF5 and g1 foreign attack gate

Prepared 2026-10-31T23:57:47.390999+00:00. Reviewer: GPT-6 Astra.

This is a conditional source-control-flow result, not a reachable-game counterexample. The exact frozen source and resolved specifications are archived in [EVIDENCE.json](EVIDENCE.json). The source SHA256 is `0c71ec9bc7b772313cc302ed1296b586cdcf98ea3bc2cdf1044e60f5220c855c`.

**Statement and hypotheses.** Consider a successful decision of that frozen `econ29.make` closure with the exact AF5 or g1 specification. Let `r` be the observed round, `h` the local `hold` value and `a` the `attack_from` parameter. AF5 has `a=5`; g1 has `a=7`. Both have `foreign_attack_from=11`, `foreign_open=True`, `hold_income=None`, `lift_idle=None`, `finish="opt"`, `doom="next"`, `none_from=4`, `none_first=True` and `none_frac=1.0`. A successful decision here means that every reached helper returns and the decision itself returns its action list without an exception.

The ordinary attack helper cannot append a minion purchase while `h` is true. The finishing and doom branches do not test `h`; they instead have separate predicates that include `r >= a`. If either branch reaches its `add` with a nonempty purchase list, those minion actions are appended despite `h`. This statement does not assert that such a branch is reachable with `h=True` in a legal game.

**Proof.** Once a building is observed at a coordinate absent from the retained requested-coordinate set, the own foreign flag latches. For these specifications, lines 563 to 575 give `h = foreign and r < 11`: the optional income and idle exceptions are disabled. This is a decision-local boolean, not a wrapper around the remainder of the decision.

The nested `attack` function begins at line 668 with `if hold: return`. Its only minion append is below that return. Both the open-case ordinary attack and the final ordinary attack call this helper.

The finishing branch at line 740 is directly inside `decide`, after visible defence. It tests `finish`, `r >= a` and sufficient remaining gold, then roster room and a nonempty modeled killing-package list. It calls `add` directly and sets `attacked=True`. Its complete enclosing branch contains no `hold` test.

The open-case branch follows finishing. If no finishing attack was selected, no opposing turret has ever been observed, and the open-case round and parameter conditions hold, it calls `attack(none_frac)` and then sets `attacked=True` unconditionally. Thus it can suppress doom even when `hold` made the helper return without buying. This effect matters: absence of a direct doom guard does not imply that doom is reached in every held decision.

After unseen-purchase defence and saturation, the doom branch at line 806 tests `doom`, `not attacked`, `r >= a` and remaining gold. It further requires the current- or next-round modeled-loss test to set `fire`, positive roster room and a nonempty search result. It also calls `add` directly. None of its enclosing predicates tests `hold`. With these defaults and `r >= a >= 5`, reaching doom requires that the open-case branch did not set `attacked`; an already observed opposing turret prevents that open-case branch.

The shared `add` filters reserved cells only for building actions. `allowed` immediately accepts non-building actions, including minion purchases. There is no final foreign-map purchase filter: after factories and requested-coordinate bookkeeping, `decide` returns `actions`. Therefore the stated conditional append behavior follows. The separate round-one poke also bypasses these attack-round predicates; it is not a finishing or doom purchase.

**Dependencies and scope.** This argument reads the complete `make`/`decide` bodies, the literal frozen specifications and the recorded source identity. It does not execute the policy, its model searches, an engine or a replay. Whether a legal game reaches a nonempty finishing or doom append while `hold=True` remains an empirical or separate reachability question. The retained-history inspection in [REVIEW.md](REVIEW.md) supplies no such witness. No code defect or required policy change follows from an inaccurate prose description of the intended exceptions.
