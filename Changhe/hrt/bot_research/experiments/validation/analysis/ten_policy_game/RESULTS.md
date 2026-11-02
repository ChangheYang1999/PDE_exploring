# Ten fixed policies after the screened counter

Checked 2026-10-31T20:45:06.265174+00:00. See PUBLISHER_AMENDMENT.md for the retained first-publisher failure and the explicit-default correction.

M is the guarded screened-order counter with frozen Fortress38 continuation. N is AS1C, frozen best_v9e with attack_share=1.0 and catch_up_share=0.5. B,C,D,G,H,I,J,L retain the exact definitions in the preceding eight-policy table.

H1, the earlier uniform B/G/H/J/L mixture remains nonnegative against both additions: REFUTED. Its M and N column payoffs are -1/5 and -3/5.
H2, N weakly improves on B against every old column and strictly improves somewhere: CONFIRMED. N minus B on B,C,D,G,H,I,J,L is [1, 0, 0, 0, 2, 0, 0, 0].

| Row | B | C | D | G | H | I | J | L | M | N |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| B | 0 | 1 | -1 | -1 | -1 | 1 | 1 | 1 | -1 | -1 |
| C | -1 | 0 | 1 | -1 | -1 | 0 | 0 | 0 | -1 | -1 |
| D | 1 | -1 | 0 | 0 | 0 | -1 | -1 | -1 | 1 | 1 |
| G | 1 | 1 | 0 | 0 | -1 | 1 | -1 | 1 | 1 | 1 |
| H | 1 | 1 | 0 | 1 | 0 | -1 | -1 | -1 | 1 | -1 |
| I | -1 | 0 | 1 | -1 | 1 | 0 | 0 | 0 | -1 | -1 |
| J | -1 | 0 | 1 | 1 | 1 | 0 | 0 | -1 | -1 | -1 |
| L | -1 | 0 | 1 | -1 | 1 | 0 | 1 | 0 | -1 | -1 |
| M | 1 | 1 | -1 | -1 | -1 | 1 | 1 | 1 | 0 | -1 |
| N | 1 | 1 | -1 | -1 | 1 | 1 | 1 | 1 | 1 | 0 |

The table contains34 new games and76 reused records. All55 physical-assignment pairs have identical normalized complete histories. The new games pass strict accounting, unchanged-source/data checks, original-engine replay and 1732 fresh policy calls. Parent receipts and their inputs are rechecked, including exact decompression of older replays.

A verified rational certificate in B,C,D,G,H,I,J,L,M,N order is ['0', '0', '0', '1/3', '0', '0', '1/3', '0', '0', '1/3']. Its exact column payoffs are ['1/3', '2/3', '0', '0', '1/3', '2/3', '0', '1/3', '1/3', '0']. The finite value is zero. The proposal search is not claimed complete or the certificate unique.

Pure policies nonnegative against every column: none.
Directed three-policy cycles: B > C > D > B; B > I > D > B; B > I > H > B; B > J > D > B; B > J > G > B; B > J > H > B; B > L > D > B; B > L > H > B; C > D > M > C; C > D > N > C; D > M > I > D; D > M > J > D; D > M > L > D; D > N > I > D; D > N > J > D; D > N > L > D; G > I > H > G; G > L > H > G; G > L > J > G; G > M > J > G; G > N > H > G; G > N > J > G; H > M > I > H; H > M > J > H; H > M > L > H.

This is selected development evidence on one start. Its34 new games are not34 independent population samples. Wall-clock cutoffs in some policies limit extrapolation from exact observed reproduction. A failure to extend an old mixture does not invalidate its earlier restricted certificate. No unrestricted equilibrium, general bot dominance or held-out claim follows. Final best.py and reserved pool D are unchanged.
