## Note 49 (2026-10-28T12:52Z): lead-side evaluation of the V195 savings on the accepted D endpoints, for comparison with your numerical_values run

To the verification work. Thanks for V190, V194, V195, V196 and the V192 correction (adopted verbatim in v30). A correction to my Note 48
item 7 remark: at the local radius of Section 3 (s = 1/2) the savings are about 1e-4, not below 1e-6; only the J_D radii
(rho about 0.299) give 1e-7 to 1e-6. Your numerical_values/PROOF.md setup is exactly the one I used, so here are my
values as an independent comparison (scratch/eta_apply/eta_apply.py, sha cf39d022..., output eta_apply.json, 256-bit arb,
J and K from the closed forms 653/288 - (63/8)L and 56627/138240 - (729/512)L, L = log(4/3); new upper = old upper minus
the lower endpoint of eta_2 + eta_4, ceiling at 10 decimals):

| alpha | source | old upper D | eta_2 + eta_4 | new upper D |
|---|---|---|---|---|
| 1/1000 | J_D, rho = 149392602419/500000000000 | 637.4272979383 | 1.35383e-7 | 637.4272978029 |
| 1/100 | J_D, rho = 74612527943/250000000000 | 64.4954580509 | 1.33956e-6 | 64.4954567113 |
| 1/20 | exterior circles n768, s = 1/2 | 13.6146872781 | 2.24579e-5 | 13.6146648203 |
| 1/10 | exterior circles n768, s = 1/2 | 7.2859601007 | 4.25267e-5 | 7.2859175740 |
| 1/5 | V190, s = 1/2 | 4.1827417136 | 7.55168e-5 | 4.1826661968 |
| 3/10 | V190, s = 1/2 | 3.2168671631 | 9.90074e-5 | 3.2167681557 |
| 1/2 | V190, s = 1/2 | 2.6453267957 | 1.176250e-4 | 2.6452091707 |
| 3/4 | V190, s = 1/2 | 3.0975797394 | 8.80171e-5 | 3.0974917224 |
| 9/10 | V190, s = 1/2 | 5.4690226815 | 4.21963e-5 | 5.4689804852 |
| 99/100 | V190, s = 1/2 | 42.6817720410 | 4.63842e-6 | 42.6817674026 |

At 1/1000 the saving does not change the 6-decimal table entry; at the other nine it lowers the D column by one to two
units in the 4th to 6th decimal. If your run agrees and is CONFIRMED, v30 or v31 will use these as Table 1 D values
(with a short theorem statement of the savings, Theorem 3.9, citing the parent lemmas), and the cross4096 recombination
(Note 50, after 13:40Z) will be reported both with and without the saving.

## Note 48 (2026-10-28T12:43Z): cross-reads of V180, general radius, V183, V185, V186, V188, V191 (fourth moment), V184 and the near-zero separation note: all pass
