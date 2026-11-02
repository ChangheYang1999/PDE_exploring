# The factory-relative exemption also preserves the no-bait guard loss

## Exact claim

Let P be the exact v24 Insurer with passive_until=5 and all other defaults.
Let Q be the exact v25 Insurer with passive_until=5, any nonnegative integer
passive_bait, a nonnegative finite passive_ratio or None, either Boolean
passive_defend, and all other defaults. Use the same initial engine state,
assignment, deterministic opponent and initial private states. Suppose that
on P's reached decision observations in rounds1 through5, whenever the
opponent owns no turret, its roster list is empty. Assume every shared
planning routine is deterministic and has no hidden shared-state effect.
Then P and Q produce identical submitted actions and complete trajectories.

## Proof

Compare the two pinned source programs. Apart from documentation and the new
parameter defaults, v25 changes only the passive predicate, its placement as
a local value before mandatory defense, and the condition enabling mandatory
defense. All other executable statements and planning routines agree.

In rounds through5 with an opposing turret, both passive predicates are
false. Without a turret, the hypothesis gives a zero roster-cost sum. The
v24 predicate accepts zero at threshold40. The v25 threshold is its
nonnegative passive_bait or the maximum of that value and a nonnegative
multiple of the opponent's factory count, so it also accepts zero. After
round5 both predicates return false before calculating any threshold.

Mandatory defense in v24 runs only with a nonempty active opposing roster.
When passive is false, v25 has the same condition regardless of
passive_defend. When passive is true, the hypothesis makes the roster empty,
so neither program invokes mandatory defense. Computing the passive Boolean
earlier changes no state: that predicate only reads the observation and
stored parameters. The two programs therefore take the same insurance,
attack, factory and private-state updates on every stipulated observation.

Induction on rounds now proves the claim. Initially their relevant private
state and the engine agree. Equal decisions give equal opponent observations
and equal opposing decisions, hence the next engine state agrees. The stated
roster condition continues to hold because this is the baseline trajectory.
Terminal outcomes and full recorded histories are consequently equal.

## Application and verification scope

The no-bait staged grower with growth through round6 buys no minion through
round6, so it satisfies the hypothesis irrespective of the guard rounds.
In particular, the staged guards in rounds4 and6 preserve the recorded P5
520:755 loss at round50. A factory-relative threshold or skipping mandatory
defense only in passive rounds cannot change that result.

The development check uses the lead's exact proposed R5, R5D and B100
parameter strings, both player assignments, and compares each full engine
history with the previously validated P5 history. These six runs verify
implementation transfer on one fixed opponent, not six independent tests of
general strength. Input and output hashes are recorded in verification/.
No proof-assistant formalization is claimed.
