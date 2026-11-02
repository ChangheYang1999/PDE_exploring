# Forecasting a deterministic policy with public observation history

## Statement

Fix the bundled engine rules and a deterministic opponent policy P with
private state initialized to a known state q_1. Assume P's action list and
next private state are functions only of its current private state and its
current observation. Assume no wall-clock limits, external randomness,
mutable files, process identifiers or shared opponent state affect P.
Assume the observer can reconstruct every observation P receives by copying
the same public player snapshots and rules, setting the player field to P's
player index, and retaining the public round number.

Let an observer keep a separate local instance Q of P, initialized to q_1.
In each reached round, invoke Q exactly once on a private copy of the
reconstructed observation. Then Q returns exactly the actual action list
of P on that round. Q's subsequent private state equals P's subsequent
private state. This conclusion holds even if P adapts to earlier public
observations and even if the observer's own actions change those later
observations.

## Proof

The local and actual instances have the same state before the first round
by initialization. Suppose their states agree before a reached round r.
They receive equal observations by the reconstruction hypothesis. Since
the policy's transition function is deterministic on these two inputs,
the returned action lists and subsequent states agree. This is the
induction step. The actual public state of the next round can depend on
the observer's actions, the opponent's actions and combat. The proof does
not predict that state in advance: the observer reads the resulting public
observation and reconstructs P's actual next input. Thus no assumption
about the observer's chosen strategy is required. Induction proves the
claim at every reached round.

## Scope and implementation

The bundled protocol gives both sides the same public snapshots and rules,
with only the player field changed. The local model uses copied observations
and a separate policy object. It does not read P's actual private state,
pending action list, live engine objects or call stack. The proof concerns
forecast correctness, not whether the observer can afford a sufficient
defense or choose a winning attack.

bots/counters/stateful_forecast.py uses one local IdentifyingCounter object
as the forecast model inside a one-round timing attacker. The actual target
is a distinct IdentifyingCounter object. Neither depends on wall time.
A prescribed prefix that skips target calls, model exceptions, different
initial parameters or multiple forecast calls without restoring model state
would violate the hypotheses. Those cases are not covered.

## Verification

Authoritative match evidence and per-round comparisons are registered in the
neighboring verification directory. This is an informal proof; no theorem
prover is used.

## Generic factory application

The same proof applies to `bots/counters/stateful_public.py` when its explicit
factory and parameters describe the target policy. `PersistentFactoryModel`
constructs one independent policy instance. It rejects a first call after
round 1, a repeated or skipped round, and a changed player assignment. These
checks enforce call order; they do not establish the target's determinism or
that its factory parameters are correct. Those remain hypotheses.

For the frozen Lead10 application, the relevant initial private state is
`pending = None` and `failed = 0`. The policy derives a failure update from the
next public observation. Its adaptive attack mode uses that failure count.
Retaining the private clone therefore fits the induction above. Reconstructing
a fresh clone on every call does not fit it: the updated failure count is lost.
The latter can still happen to predict some actions correctly, but this proof
does not certify those predictions.
