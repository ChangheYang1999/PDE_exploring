# Equivalence with the lead's all-candidate option

## Statement and assumptions

Compare the frozen source of UntruncatedInsurer from v24 with the lead's
v27 Insurer, robust_k=None. Use identical common parameter values, and
v27 passive_ratio=None, passive_defend=True, passive_turret=True. Give
fresh instances the same sequence of valid observations. Assume shared
planning functions return identical results on identical arguments,
including any time-limited planner calls, and that calls terminate.
Then both instances return the same action lists and have the same common
private state after each call. Their parameter dictionaries differ only
by the additional options stated above.

## Argument

The two source versions have the same defaults on every common key.
Outside _decide, _passive and _attack, the class methods and external
helpers are unchanged. In _passive, the new turret test is enabled by
passive_turret=True, and the factory-relative extension is disabled by
passive_ratio=None. Thus the returned predicate equals the v24 predicate.
It only reads its inputs and does not change private state.

In _decide, passive_defend=True leaves mandatory visible-roster defense
enabled under exactly the original condition. Moving the pure _passive
query before that defense does not change its argument, because that query
reads the original observation and the defense modifies only the local
constructed observation. Both insurance branches therefore see the same
predicate and make the same planning calls.

In _attack, the non-robust branches coincide. For robust mode both compute
the same current-map damage increment for every tier, the same affordable
count and eligibility ratio, and sort the same tuples. Both now evaluate
every eligible tier in that sorted order against the same response
routine, retain the same response-ratio passers and sort by the same tuple.
They therefore return the same purchase list and predicted damage. The
single-list and comprehension spellings do not alter those values.

Induction on calls now proves the statement: the constructors agree on
common state, and each pair of calls takes equal branches and updates
common state equally. The hypothesis about planning results matters:
this argument does not turn a clock-limited planner into a deterministic
one. Fresh shadow runs check equality on the recorded finite histories.

## Verification scope

The checker compares shared defaults and the ASTs of unchanged methods,
then shadows v27 on all twelve complete UntruncatedInsurer histories from
the six-opponent development matrix, replaying every original transition.
It checks input immutability and full action equality. These are reused
histories, not twelve new independent strength samples. No proof-assistant
formalization is claimed.
