# Independent tabulation of the fortress-versus-lead comparison

## Statement and hypotheses

The finite data are the sixty x158_vs_lead games recorded by the defense lane: fortress v36, v37 and v38 against P5TNUBM and frozen best_v9e, on the standard start and four prescribed continuations, with both player assignments. The arithmetic claim is that the standard and continuation totals in this fixed table are respectively 12 and 48 games. For each retained replay, the separate claim is that its recorded outcome and final HP follow from its actions under the unchanged bundled engine. Twenty-four winning continuation rows have no retained log, so their outcomes cannot receive this replay check.

## Argument and verification

Check the recorded source hashes of the engine and both entry modules, absence of rejected actions and bot errors, and the complete initial records including the declared scenario metadata. Reconstruct each game with a retained log using the original Engine. Record every missing log explicitly; do not infer that it passed replay. For every round, recover both action lists from the events, play them, and require exact equality of every resulting record. Induction gives the same public state before each round and the same terminal winner and HP. Classify a game as a win only from the winner field and the fortress assignment, never from the sign of the HP difference. Count each recorded condition once and require the complete three-by-two-by-five-by-two grid.

For retained replays, total damage dealt is checked by adding the opposing defender's recorded base damage over all rounds and comparing it with the reported player total. In a standard game without healing, final HP also equals initial HP minus received damage. Thus equal terminal HP does not imply that no copy reached either base.

## Dependencies and scope

The result depends on the original engine, its bundled balanced configuration, and the fixed x158 result and replay bytes. The verification receipt hashes these inputs. This is a disclosed partial replay audit and a complete arithmetic audit of already counted games, not a fresh policy evaluation or a proof of strategic strength. The associated prose correction concerns the exact recorded sample and its mechanism claims only.
