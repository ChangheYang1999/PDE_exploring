# Branch transfer against recently frozen teammate policies

Written 2026-10-31T17:29:15.539571+00:00, before any game in this matrix.

## Exact finite claim

The adaptive DelegatedRouteSelector with delegate='fortress38' avoids defeat against each of six fixed teammate policies in both physical assignments on the standard start. The targets are frozen Fortress40, frozen Fortress41, the fixed V33C specification, frozen economy29 with its round-one 60-gold guard, frozen best_v9e, and P5TNUBM. Their exact specifications and source hashes are recorded in the six manifests. This is a falsifiable empirical claim on twelve adaptive games. Thirty-six games are declared in total: every target also plays the existing mode='early' and mode='growth' controls in both assignments. No target or control is removed after outcomes are seen.

The broader transfer in delegated_transfer passed on 45 previous targets. This smaller test includes more recent policies and separates a poor branch choice from limitations shared by both fixed continuations. It is development work on disclosed policies, not reserved final validation. Fortress41 was recommended before this declaration; its own external review is separate.

## Policy argument, notation and hypotheses

Let H_r denote both players' complete public records through round r. The three modes instantiate the same two opening components and ignore their mode parameter before round four. On equal public observations they propose the same first-three-round actions, conditional on deterministic internal computations. Each target also receives the same own observations and name in these paired games. Induction on rounds therefore gives equal H_3 in all three modes, conditional on those computations being deterministic. This premise is checked empirically by complete record comparison, not assumed from the engine alone.

At round four, adaptive chooses the early branch exactly when its full gun1-plus-tier4 package is affordable, its projected own HP and HP lead are positive, and the opponent's route exceeds the unobstructed Manhattan length. Otherwise it chooses growth. Once selected, the branch does not change. A fixed mode with the selected value therefore has the same subsequent policy transitions, conditional on equal observations and deterministic computations. Check complete trajectory agreement between adaptive and that fixed mode. A disagreement is a reproducibility failure to investigate, not evidence that the branch-selection rule improved play.

Only the early branch can hand off to Fortress38. From round five, its first positive public HP lead or positive original-combat damage from the visible opposing roster starts the permanent delegate. Before that point it keeps the earlier early-policy actions. The handoff uses public information only. All three modes keep the original implementation and frozen defender, so this experiment does not silently substitute Fortress41 into the counter.

## Dependencies and verification

Dependencies are delegated_defense/PROOF.md, emergency_after_strike/PROOF.md, the unchanged original engine and configuration, the pinned counter implementation and its three exact JSON layout/guard inputs. The manifest closure includes each target, both independent checkers and the runner. Register every loaded source and data input and keep its archive.

For each six-game target partition, require strict completion, no rejected actions or bot errors, original-engine replay, archived-source/data agreement, fresh regeneration of every counter decision, and independent public handoff reconstruction. Retain both physical assignments. The publication compares complete first-three-round prefixes, each adaptive trajectory with its chosen fixed mode, outcomes, final HP, ending round, selection, handoff and actual decision times. Report every condition in which another fixed branch improves W/D/L and every condition in which both fixed branches lose. These are descriptive finite comparisons, not an optimality or generalization theorem.
