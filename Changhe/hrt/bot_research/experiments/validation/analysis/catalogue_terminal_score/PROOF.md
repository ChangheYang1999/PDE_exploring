# Terminal-round score scope for the catalogue attack policy

## Statement and notation

Use the fixed-round hypotheses and notation of
`../catalogue_attack_selection/PROOF.md`. In particular, the actual opponent
is a retained deterministic catalogue member, forecasts and combat values
are exact, construction is fixed, and the finite affordable purchase set P
contains the empty sequence. Let

    g(p) = min over retained a of [d_a(p) - d_a(empty)].

In the final configured round, `AdaptiveCatalogue` uses g(p) as its utility,
rather than the nonterminal utility w*g(p) - c(p). Among purchases without
a forecast safe-lethal outcome it maximizes this final-round utility before
its cost and length tie breakers. Therefore its selected purchase has
g(p) >= 0 if no safe-lethal purchase is selected. Under the true retained
member, the selected purchase then causes at least as much outgoing damage
as the empty purchase on the fixed post-construction map.

The safe-lethal implication of the preceding proof is unchanged in the
final round. Neither this implication nor g(p) >= 0 implies that the policy
chooses the best terminal result against every retained member.

## Proof

For every retained a, d_a(empty) - d_a(empty) = 0, hence g(empty) = 0. If no
safe-lethal purchase is selected, no purchase has the higher first ranking
entry that would displace the empty purchase. The next ranking entry is g,
so the selected value is at least zero. The minimum defining g is no larger
than the actual member's marginal damage, which proves the outgoing-damage
comparison. Cost and length tie breakers occur after g and cannot weaken
that comparison.

The safe-lethal conclusion uses only the current incoming and outgoing
damage inequalities and the engine's simultaneous destruction rule. It
does not use the utility formula, so it applies unchanged.

## A limitation of the ranking rule

Here is an abstract exact-forecast table illustrating why nonnegative gain
is weaker than optimal terminal outcome. This is an algebraic example; no
claim is made that these numbers arise in a reachable bundled-game state.
Suppose own HP and opponent HP are both 10, and incoming damage is 20 under
each of two retained members A and B. Consider three equal-map purchases:

| purchase | outgoing under A | outgoing under B | minimum marginal gain |
| --- | ---: | ---: | ---: |
| empty | 0 | 9 | 0 |
| p | 10 | 10 | 1 |
| q | 9 | 100 | 9 |

Assume p and q are both affordable. Own survival is false for both models,
so neither purchase is classified safe lethal. The implemented final-round
ranking prefers q to p because 9 > 1. If the true member is A, q loses:
own HP becomes -10 while the opponent retains 1 HP. Purchase p would instead
destroy both bases and draw. Under B, both purchases draw. Thus maximizing
the worst marginal outgoing gain need not maximize the worst terminal
result when baseline outgoing damage differs across retained members.

This example also explains why the fixed-round proof does not certify a
best response even within the enumerated purchase set. The current policy
has a safe-win priority, not a complete outcome ordering that also protects
available simultaneous-destruction draws.

## Dependencies and evidence scope

Dependencies are `../catalogue_attack_selection/PROOF.md`,
`../stateful_catalogue/PROOF.md`, and the original engine's simultaneous
terminal settlement. The source under review is
`bot_research/bots/counters/adaptive_catalogue.py`; its initial development
manifest freezes the original source and preceding proof. This addendum
does not change those declared inputs or their pending experiments.

The attack audit independently recomputes selected damage with original
combat and explicitly uses g in the final configured round. Full-game
traces, when completed, can establish how often this branch is reached;
they cannot turn the abstract table above into a reachable game fixture.
No formal proof assistant or exhaustive game search is claimed.
