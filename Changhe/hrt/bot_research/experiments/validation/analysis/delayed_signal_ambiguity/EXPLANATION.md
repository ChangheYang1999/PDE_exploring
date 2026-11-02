# What two empty opening rounds reveal

Written 2026-10-31T21:48:58.223996+00:00, after the retained-history checks.

The two-round selector R chooses its response at the start of round three. Against H, it chooses L and wins 800:656. Against S, it makes the same choice and loses, with L at -326 HP and S at 800. Both outcomes occur in both player assignments. The difference appears after R has committed: S builds its walls and splash in round three.

R's choice comes from a useful earlier rule. G is the fixed early-wall guard. L is the wall-signal policy with its repair continuation. They submit the same first two ordered action lists: twenty walls followed by four factories, then five factories. R advances both private policies while their actions agree. It can therefore retain either member's accumulated state when it chooses. Reconstructing a fresh L at round three would be a different experiment, because L has already advanced an internal model of the opponent.

H and S give this selector the same early public history. Each buys five factories in round one and four in round two. Their boards and rosters remain empty. At the start of round three, either opponent has 174 gold, nine factories, an empty board with path length 22, and 800 HP. The selector has 175 gold, nine factories, twenty walls with path length 40, and 800 HP. There is no third-round submission in the observation yet. The unchanged engine supplies the same fields in each fixed physical seat, after replacing only the player names consistently.

This equality has a precise boundary. The actual names can identify the policies, and the third completed round reveals S's construction. The argument concerns selectors using the normalized public history, with identity and timing side channels excluded, that permanently choose G or L by the start of round three. A later choice, a different opening or another response is a separate strategy.

The measured payoff table explains why the choice matters. Payoff is +1 for a win, 0 for a draw and -1 for a loss, from the member's perspective. The table holds separately in both physical seats.

| Chosen member | H | S |
| --- | ---: | ---: |
| G | -1 | 0 |
| L | +1 | -1 |

Suppose a randomized selector chooses G with probability p. Its random choice is independent of which opponent it faces. Because its permitted information is the same against H and S, it must use the same p in both comparisons. If each selected continuation reproduces its corresponding baseline payoff, its expected payoffs are 1-2p against H and p-1 against S.

Increasing p helps against S and hurts against H. The two expressions meet at p=2/3, where each equals-1/3. Below that probability, S gives a worse value; above it, H does. Thus -1/3 is the exact best worst-case expected payoff in this restricted selection problem. A complementary certificate mixes H with probability 1/3 and S with probability 2/3: either pure member then receives -1/3. A deterministic choice has worst payoff -1.

The continuation premise needs care. The twelve retained games establish the displayed outcomes, complete early public equality and the recorded R-to-L transfers. Some later planners stop according to wall-clock time. Extra shadow work or a different execution schedule can affect a later decision, even with the same logical prefix state. The theorem therefore states continuation coupling as a hypothesis; the finite replay check does not prove every future timing branch agrees.

This gives a concrete diagnosis of R's failure. Its information supports the same branch choice in two histories whose later payoffs favor different branches. The measured counterexample motivates changing the commitment rule or expanding the response set. It supplies no bound on unrestricted game play.

Read [the exact statement and proof](PROOF.md), [the checked result](RESULTS.md), and [the complete verification receipt](verification/full_check.json). Protocol 159 replays twelve existing games and makes zero new policy calls. The experiment does not change the final candidate or use reserved pool D.
