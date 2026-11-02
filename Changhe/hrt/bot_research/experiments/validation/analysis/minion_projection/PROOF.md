# When only the forecast minion purchases affect the timing controller

## Exact statement and hypotheses

Use the current bundled game rules and the fixed `ForecastTiming` controller
in `bot_research/bots/counters/forecast_timing.py`, with defense_first=False.
Compare two copies with equal parameters and the same standard initial state.
The full copy applies every action predicted by its private opponent model.
The projected copy applies only the ordered buy_minion subsequence of the same
prediction, as in `projected_forecast.py` with projection="minions".

Assume both private models start in the same state, receive only the same
public observations, advance once per reached round, and are deterministic.
Every predicted full action list is legal on its reconstructed opponent state.
All planning calls terminate, succeed, and return equal outputs on equal
inputs. The real opponent is also deterministic with equal initial state in
the two games. The action catalogs contain only the four current operations,
and every action cost is nonnegative.

Let r be the controller's single attack_round. Until round r, both games have
equal states and submissions. If the game ends before r, their full game
states and submissions agree. Otherwise evaluate both copies on their common
observation in round r. Let m be the common affordable proposed attack count.
If m=0, or if the full and projected extra-damage simulations are either both
strictly positive or both nonpositive, the two games have equal states and
submissions through termination.

Equality here concerns actions and game states, after exchanging player labels
when required. It does not require equal forecast traces, model execution time,
or display metadata. The extra-damage values themselves may differ.

## Proof

First fix one common observation and one legal full prediction. Delete every
operation other than buy_minion. Before each retained operation, the projected
state has spent the same amount on earlier minion purchases and no amount on
the deleted operations. Its gold is therefore at least the full state's gold.
The retained minion has the same valid type and affordable cost in both states.
No current action other than buy_minion changes the roster or the next roster
identifier. Induction through the retained operations shows that they are all
accepted and create equal ordered roster entries, including purchase rounds
and expiry rounds. The two resulting active minion-type lists are equal.

The controller uses predicted construction only in the extra-damage simulation
at its single attack round. It never uses predicted factory count in spending
or defense. Outside that attack calculation, its decisions depend on the common
public observation, own gold and buildings, and the equal active incoming list.
Thus its defensive plan, optional saturation plan and factory purchases agree
on a common observation in every round other than r.

Induct on rounds strictly before r. Initial states and private model states
agree. On the common observation, determinism gives the same full prediction
and the same real opponent submission. The preceding roster argument and the
controller's control flow give the same counter submission. The deterministic
engine produces the same next states. Both private models have advanced on the
same input, so their states also remain equal. This proves the pre-r claim.

If round r is reached, the counter has the same own gold in both games. Because
defense_first=False, its proposed count m is computed from that gold before
any defensive spending, with the same share, unit cost and cap. When m=0,
neither copy attacks. When m>0, each copy keeps m exactly when its extra-damage
simulation is strictly positive; otherwise it changes the count to zero. The
stated sign hypothesis therefore makes their purchased counts equal. The same
attack cost leaves equal gold. Their incoming lists are still equal, so all
subsequent defense, saturation and factory actions in that round agree.

The next game states consequently agree. In every later round the one-time
attack branch is inactive. The same induction as before r proves equality
through termination. Appended trace entries do not enter later decisions.

## Dependencies, checks and scope

This is an informal source argument, not a proof-assistant formalization.
The engine operation cases are in `td_game/actions.py`; the controller and
projection sources are named above. The adjacent verification receipt pins
source hashes and the independent strict, forecast, replay and paired-history
artifacts.

In the recorded V4 study, tier3 at rounds 3 and 5 and tier4 at round 5 satisfy
the condition: all six full/projected games, including both assignments, have
identical normalized histories. The tier4 round-6 pair fails the condition:
the full forecast predicts zero extra damage and buys nothing, while the
minion-only forecast predicts 120 and buys two copies. Those two games still
both draw 800:800, but their actions diverge in round 6. Outcome equality is
therefore weaker than trajectory equality.

This statement does not show that incoming purchases can be forecast without
an opponent model. It does not say that construction predictions are always
irrelevant, or that additional construction can only reduce attack damage.
It gives no strength guarantee against a different opponent or initial state.
