# A response-preserving shortcut after splash immunity

Written 2026-10-31T20:51:56.831684+00:00, before implementation and evaluation.

## Exact statement

Use the bundled rules and frozen best_v9e with its unmodified default parameters. Consider a valid public observation and identical legitimate policy state immediately before its native _decide method. If the round is greater than5, the current map has splash exposure at least1500, and the stage-zero plan_walls call returns no action, then the defense and insurance portion of _decide returns no actions and has exactly one potentially observable policy-state operation: _fortress. Replacing that portion with its _fortress call, while retaining the pending-attack update, attack choice and factory purchases, gives the same returned actions and subsequent policy state. Outside this predicate, delegate to the unchanged parent implementation. The enclosing __call__ and foreign-map delegate remain inherited. By induction on any valid observation sequence, this shortcut preserves the default policy's actions and legitimate persistent state.

The implementation must accept no parameter overrides: this argument uses the default round thresholds, positive big_threat and false splash_insurance. It is a research variant in the worker's owned directory. It does not change the installed final candidate or its reserved validation.

## Argument

The empty stage-zero wall plan leaves the map, gold and action list unchanged. Every catalog minion has HP at most1500. The visible-roster defense calls plan_defense only with these types. Its required adjacency is at most150; the existing map's adjacency is at least150, so its explicit early return is an empty action list.

Each sampled insurance composition contains only catalog types. The same plan_defense early return applies for any budget and any nonempty composition. All splashes damage every adjacent copy independently, including its spawn cell and excluding the base. At speed1, any copy reaching the base receives the full summed exposure and dies before arriving if that exposure reaches its HP. Copies not reaching the base within the250-tick round also cause no damage. Therefore _worst_leak returns zero for all sampled rosters; zero is below the default big_threat100, so the full-budget fallback and its nested gun alternative are not entered. The default poke_until3 and mid_until5 both exclude the present round, so neither remaining insurance branch runs.

The parent computes its insurance options even when the composition list is empty. With default splash_insurance false this evaluates _fortress, which can set its sticky Boolean. The replacement must execute exactly that same call. The planners, composition builders and simulators above do not mutate legitimate policy state or the observation. Cache contents and elapsed time are excluded from policy state; the native default path has no clock cutoff.

The pending-attack update is retained exactly, including failure increments and clearing pending. The map is immune and default immune_attack is true. Round greater than5 reaches the default attack_from6 threshold. Thus the parent uses the current attack mode with its default attack budget. Invoke the same _attack with the same observation, rules and gold; retain its returned purchases, the pending record and the same factory cap and last-factory-round check. This gives identical actions and fields. The inherited __call__ then updates requested cells identically. On foreign observations, that inherited method installs or invokes the same foreign delegate before _decide, so the optimization cannot interfere with it.

For induction, start from the same constructor fields. At every native call the fast predicate either applies the proved transition or calls the parent, and foreign calls remain inherited. Equal action and state transitions preserve equality at the next observation. This argument concerns valid bundled-rule observations and default parameters, not arbitrary malformed dictionaries, altered catalogs or unspecified parameter variants.

## Falsifiable evaluation

H1: a fresh shortcut instance matches every recorded candidate action across the two high-factory histories used by protocol150, and each whole record stream replays through the original Engine. H2: at least one call uses the shortcut. H3: the largest shortcut policy call is below3 process-CPU seconds on those two histories. Compare measured totals and maxima with protocol150, naming the separate process executions and avoiding a portable speed claim. Additional C histories may be checked as explicitly reused development evidence; none becomes a new game or a new held-out sample.

Before executing calls, pin this proof, the implementation, checker, exact input records and full import closure. Any discrepancy refutes H1 until separately explained; do not overwrite a failed attempt. Request an independent review of the argument and code.

## Dependencies and scope

Source dependencies: frozen best_v9e _decide, _fortress, _attack and __call__; frozen v7 plan_walls and plan_defense; unchanged splash combat and current catalog. Formal sources: none. Verification receipts will be retained in verification/. The informal transition proof and empirical checks have separate scopes. This does not improve game strength, change the sampled threat model, or make the final candidate a different artifact.
