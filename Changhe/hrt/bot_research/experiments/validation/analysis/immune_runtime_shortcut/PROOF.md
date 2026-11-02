# A response-preserving shortcut after splash immunity

Written 2026-10-31T20:51:56.831684+00:00, before implementation and evaluation.

## Exact statement

Use the bundled rules and frozen best_v9e with its unmodified default parameters. Consider a valid public observation and identical legitimate policy state immediately before its native _decide method. If the round is greater than5, the current map has splash exposure at least1500, and the stage-zero plan_walls call returns no action, then the defense and insurance portion of _decide returns no actions and has exactly one potentially observable policy-state operation: _fortress. Replacing that portion with its _fortress call, while retaining the pending-attack update, attack choice and factory purchases, gives the same returned actions and subsequent policy state. Outside this predicate, delegate to the unchanged parent implementation. The enclosing __call__ and foreign-map delegate remain inherited. By induction on a valid observation sequence that stays in native execution, this shortcut preserves the default policy's actions and legitimate persistent state. Extending this induction through foreign delegation requires the additional premise that the two delegate executions take the same deadline branches.

The implementation must accept no parameter overrides: this argument uses the default round thresholds, positive big_threat and false splash_insurance. It is a research variant in the worker's owned directory. It does not change the installed final candidate or its reserved validation.

## Argument

The empty stage-zero wall plan leaves the map, gold and action list unchanged. Every catalog minion has HP at most1500. The visible-roster defense calls plan_defense only with these types. Its required adjacency is at most150; the existing map's adjacency is at least150, so its explicit early return is an empty action list.

Each sampled insurance composition contains only catalog types. The same plan_defense early return applies for any budget and any nonempty composition. All splashes damage every adjacent copy independently, including its spawn cell and excluding the base. At speed1, any copy reaching the base receives the full summed exposure and dies before arriving if that exposure reaches its HP. Copies not reaching the base within the250-tick round also cause no damage. Therefore _worst_leak returns zero for all sampled rosters; zero is below the default big_threat100, so the full-budget fallback and its nested gun alternative are not entered. The default poke_until3 and mid_until5 both exclude the present round, so neither remaining insurance branch runs.

The parent computes its insurance options even when the composition list is empty. With default splash_insurance false this evaluates _fortress, which can set its sticky Boolean. The replacement must execute exactly that same call. The planners, composition builders and simulators above do not mutate legitimate policy state or the observation. Cache contents and elapsed time are excluded from policy state; the native default path has no clock cutoff.

The pending-attack update is retained exactly, including failure increments and clearing pending. The map is immune and default immune_attack is true. Round greater than5 reaches the default attack_from6 threshold. Thus the parent uses the current attack mode with its default attack budget. Invoke the same _attack with the same observation, rules and gold; retain its returned purchases, the pending record and the same factory cap and last-factory-round check. This gives identical actions and fields. The inherited __call__ then updates requested cells identically. On foreign observations, that inherited method installs or invokes the same foreign delegate before _decide, so the optimization cannot interfere with it.

For native-only induction, start from the same constructor fields. At every call the fast predicate either applies the proved transition or calls the parent. Equal action and state transitions preserve equality at the next observation. The inherited foreign code has the same source in both versions, but its frozen planner receives a finite plan_time of 1e6 seconds. Source identity alone does not prove equal branch decisions under all possible scheduling delays. Induction through that code is therefore conditional on matching deadline branches, and the foreign-history comparisons below are finite empirical checks. This argument concerns valid bundled-rule observations and default parameters, not arbitrary malformed dictionaries, altered catalogs or unspecified parameter variants.

## Falsifiable evaluation

H1: fresh parent and shortcut instances have identical actions and legitimate state after every actual policy call across exactly74 retained histories: the two high-factory histories used by protocol150 and all72 selected C histories. Both generated actions must also equal the retained candidate actions, and every complete record stream must replay through the original Engine. The120 prescribed prefix turns per implementation are skipped. The expected actual calls are1204 per implementation,2408 total. These are reused development histories, not new games or new held-out samples.

H2: at least one call takes the shortcut. H3: the largest shortcut call is below3 process-CPU seconds on the two high-factory histories. Measure wall and process CPU time for both implementations in each fresh per-history process, alternating which runs first each round. Report the shared-cache limitation and avoid portable speed claims. The unchanged parent is called on exactly the same public observations. Check observations for mutation, generated actions for legality, and each persistent field including the foreign function's closure state. Foreign-history equality remains an empirical finding, not an unrestricted deadline-independent theorem.

Before executing calls, pin this proof, the implementation, checker, exact input records and full import closure. Any discrepancy refutes H1 until separately explained; do not overwrite a failed attempt. Request an independent review of the argument and code.

## Dependencies and scope

Source dependencies: frozen best_v9e _decide, _fortress, _attack and __call__; frozen v7 plan_walls and plan_defense; unchanged splash combat and current catalog. Formal sources: none. Verification receipts will be retained in verification/. The informal transition proof and empirical checks have separate scopes. This does not improve game strength, change the sampled threat model, or make the final candidate a different artifact.

## Scope amendment, 2026-10-31T20:54:59.630889+00:00

Before any shortcut policy call or protocol151 input pin, independent review identified that the original induction sentence was too broad for the foreign delegate's finite clock cutoff. PROOF_INITIAL.md retains the exact original text. This amendment narrows the theorem to native execution, or matching foreign deadline branches, and fixes the prospective empirical corpus at74 histories. No implementation change was needed.
