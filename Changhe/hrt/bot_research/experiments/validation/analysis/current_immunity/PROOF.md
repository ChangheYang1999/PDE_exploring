# A current-route splash certificate with optional guns

## Statement, notation and hypotheses

Use the unchanged bundled balanced combat rules. Let P=(p_0,...,p_L)
be the selected legal route on the defender's map after all construction for
this round has been applied. The map may contain walls, standard guns and
splash turrets. It is fixed during combat. Every minion moves one step per
tick after its spawn tick. All damage values are nonnegative.

For 0 <= i < L, let s_i be the sum of the configured damage of every splash
turret at Chebyshev distance one from p_i. Define S=sum_i s_i and let H be
the largest configured HP of any allowed minion type. If S >= H, no finite
attacking roster deals base damage in this combat. Guns may be present.
The base index L is excluded from S because arrival precedes targeting.

The same conclusion holds in every subsequent combat if its map and route
remain unchanged, or more generally if its newly evaluated S still satisfies
S >= H. This is a conditional safety statement, not an optimal spending rule.

## Argument

Fix an arbitrary attacking copy. If its spawn tick plus L is outside the
combat horizon, it cannot arrive, regardless of damage. Otherwise suppose
for contradiction that it arrives. It must have survived every earlier
attack phase at p_0 through p_(L-1). During each of those phases, every
adjacent splash applies its full damage to this copy. Splash damage is not
shared among copies, and none of the guns can subtract that damage or heal
the copy. The total damage to the supposed survivor before arrival is at
least S. Its initial HP is at most H <= S, so at or before the last such
phase its HP is nonpositive. Death removal precedes the following movement
step, contradicting arrival.

The argument applies to every copy, including copies sharing a spawn tick
when the roster exceeds 250 entries. Thus no copy arrives and base damage
is zero. Repeating the same argument proves the stated future-combat
conclusion whenever its map satisfies the same inequality.

## Limits for policy use

Permanent buildings do not by themselves make the selected route permanent:
adding another building can remove the previously selected path. The
certificate must refer to the map after this round's final construction.
A policy may safely test S anew each round without proving route persistence.

Safety also does not prove that spending all remaining gold on an attack is
optimal. Factories and conserving gold can change later offensive options.
Nor does safety prove that an attack will damage an opponent who constructs
new defenses in the same round. An attack rule that assumes no response
still requires empirical evaluation or a separate offensive argument.

## Dependencies and source review

The argument uses td_game/combat.py (spawn, movement, arrival, simultaneous
nonnegative damage, death removal), td_game/config.py and the bundled
balanced catalog. It extends the sufficient direction of
analysis/splash_threshold/PROOF.md to maps that also contain guns. Unlike
that pure-splash result, it does not characterize exactly which copies
arrive when S < H.

In the source reviewed during shift 1, experiments/lead/v15.py evaluates
_immune(o2, rules). With walls_first=True, o2 includes the current proposed
construction. With walls_first=False, the later plan_walls actions are
appended without rebuilding o2 before this test. Therefore that nondefault
branch tests the earlier proposed map, and this proof alone cannot certify
its final map. This is a source-level scope finding, not a demonstrated
match loss or a finding about the default configuration.

This is an informal proof. No proof assistant was used.
