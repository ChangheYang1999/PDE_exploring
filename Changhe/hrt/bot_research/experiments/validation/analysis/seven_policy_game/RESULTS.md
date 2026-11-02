# A finite table after public response selection

Checked 2026-10-31T19:26:16.644411+00:00.

The earlier uniform G/H/I mixture has payoff -2/3 against J. Its nonnegative guarantee therefore does not extend to this seventh policy. This does not invalidate the earlier certificate on its six original columns.

B is frozen best_v9e. C and I are the same round-three tier2 attack procedure with fixed private D and H models respectively. D is the adaptive Fortress38 continuation, G the early-wall guard, and H the HP-triggered grower. J chooses between H and I after their common first move using the public round-two wall count and roster. The exact specifications and checked source bytes are retained in the parent receipts.

| Row | B | C | D | G | H | I | J |
|---|---:|---:|---:|---:|---:|---:|---:|
| B | 0 | 1 | -1 | -1 | -1 | 1 | 1 |
| C | -1 | 0 | 1 | -1 | -1 | 0 | 0 |
| D | 1 | -1 | 0 | 0 | 0 | -1 | -1 |
| G | 1 | 1 | 0 | 0 | -1 | 1 | -1 |
| H | 1 | 1 | 0 | 1 | 0 | -1 | -1 |
| I | -1 | 0 | 1 | -1 | 1 | 0 | 0 |
| J | -1 | 0 | 1 | 1 | 1 | 0 | 0 |

Payoffs are +1 for a win, 0 for a draw and -1 for a loss. This table reuses all 56 games from the two completed studies. No new match, replay or policy call was made for this arithmetic analysis. All 28 assignment pairs had identical normalized histories in their original checks. All parent receipt inputs are rechecked here, using exact decompression for archived replays.

An exact optimal mixture for this table is B=1/3, C=0, D=0, G=0, H=1/3, I=0, J=1/3. Its column payoffs are 0, 2/3, 0, 1/3, 0, 0, 0. The finite value is zero.

The proof is direct. If p is this probability vector and q is any opposing distribution on these seven columns, p^T A q is nonnegative because it averages nonnegative column payoffs. Skew symmetry gives A p = -(p^T A)^T, so using the same p as the opposing mixture holds every row distribution to at most zero. These two inequalities meet at zero. The exact solver proposes p; the receipt separately checks every inequality with rational arithmetic.

Pure policies nonnegative against every column: none. Directed three-policy cycles: B > C > D > B; B > I > D > B; B > I > H > B; B > J > D > B; B > J > G > B; B > J > H > B; G > I > H > G.

This is a selected development table. A private mixture draw would occur before a match and remain hidden until revealed by play. J is itself a fixed policy, although its decisions depend on observed play. The certificate covers only these fixed policies, the measured standard start and their observed decisions. It gives no guarantee against an eighth policy, changed starts or different wall-clock-bounded planner choices. It is not a statistical confidence statement or a replacement for the final reserved evaluation.

Reproduce with check_seven_policy_arithmetic and publish_seven_policy_game after restoring the pinned parent receipts and their inputs. The declaration and verification/full_games.json contain every required path and hash.
