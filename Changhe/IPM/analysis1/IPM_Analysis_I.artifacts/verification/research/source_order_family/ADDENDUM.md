# Norm clarification and exact published ceilings

The leading commutator term in the proof has operator norm at most
s||Dw||infinity,F from Hs to L2. After composition on the right with
J^(-s), it is bounded from L2 to L2. The phrase "Hs operator norm" in
that paragraph does not assert an Hs-to-Hs multiplier bound controlled
only by a coefficient supremum. This clarification is mandatory.

At s=153/50 the independent exact calculation gives

 C_*=3442071/250000=13.768284,
 E_*=113588343/500000000=0.227176686,
 kappa=2134/625=3.4144,
 a_*=1593611657/500000000=3.187223314,
 K1<500000000/1593611657<313753/1000000,
 d_s>=15403/5000=3.0806.

C_V and E are strictly below their ceilings because the imported actual
M_V and M_rho ceilings are strict. E is not asserted equal to E_*.
For the whole closed order interval, K1<3181/10000, d_s>=6141/2000.
The actual inverse norm includes (1+R_s/d_s)^s and R_s is not evaluated.

The code checks 16 vertices sufficient for the whole parameter box times
the s interval by multiaffinity, plus8 vertices at s=3.06. The elementary
monotonicity proof, not those extra vertices, treats every real order.
The three numerical beta_s checks are supplementary, with fresh full
Arb1536 enclosures inside both primary engine intervals.
