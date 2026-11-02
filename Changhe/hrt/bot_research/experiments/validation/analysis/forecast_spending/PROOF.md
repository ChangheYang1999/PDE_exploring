# What zero damage implies for repeated purchases

## Statement and hypotheses

Fix a complete, original-engine-verified game history with terminal round T.
Let H be the first round in which the forecast-handoff defender switches.
Let d(r) be its incoming base damage in round r and let C(r) be the sum
of the balanced-config prices of the attacker's accepted minion purchases
in that round. All purchased copies are active no earlier than their
purchase round. Every arriving copy deals a nonnegative amount of base
damage, and the combat record sums exactly those arrival contributions.
Assume d(r)=0 for every r from H through T. Then the minion purchases
from H through T spend exactly the sum of C(r) over those rounds and
produce no base damage during any remaining played round. This conclusion
is about the recorded trajectory, including the defender's actual responses.
It is not a claim that removing these purchases leaves that trajectory,
the defender's spending, or the final outcome unchanged.

If two full games begin with the same state and differ only in the defender's
fixed choice of predicted versus visible incoming roster after H, their
different outcomes measure that complete policy intervention. Provided the
recorded policies reproduce, this is a matched comparison, not an isolated
one-action or one-round causal estimate.

## Proof

Sequentially accepted purchases each deduct the configured minion price.
Summing these individual deductions gives the displayed expenditure,
regardless of subsequent factory income or other purchases. A copy bought
in round r cannot arrive before r. At any played round s at least r, its
arrival contribution is one of the nonnegative terms summed in d(s). Since
d(s)=0, that term is zero. Apply this argument to every purchased copy and
every remaining played round. It makes no assertion about unplayed rounds
after T, and does not assign the defender's construction cost to any copy.

For the comparison, the two controllers have the same code, parameters,
initial state and opponent except for their forecast flag. Both advance
the same private public-policy model once per round; the flag only selects
the roster supplied to defensive planning after the switch. Thus the
comparison changes that policy rule. Different subsequent public histories
can change both players' later decisions, so a single-round interpretation
does not follow. Paired seats and repeated identical histories are not new
independent samples.

## Dependencies and empirical scope

Dependencies are the bundled purchase and combat semantics, the forecast
handoff controller, proof65's observation and legality argument, proof66's
standard-start synchronization hypotheses, and the original-engine replay
and fresh-policy checker. Source and result hashes accompany the evidence.
This is an informal argument; no proof-assistant claim is made.

The registered 48-game development experiment includes eight P5TNUB games,
with forecast on/off, deadlines9/10 and both seats. The spending analysis
uses only these eight prespecified games after all eight original replays
and fresh public-model histories pass. Zero-damage and exact-forecast
conditions are checked rather than assumed. All eight conditions remain
in the output, including controls that fail the zero-damage hypothesis.
The check may support repeated blocked purchases, not economic worthlessness,
optimal defense, broad opponent robustness or reserved validation strength.
