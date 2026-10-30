# Fixed-norm sharpw scalar maximum and repaired report arithmetic

## Statement, spaces and scope

Fix s=1/5184, w1=32768 and w2=1048576. Let J=(1-Delta)^(1/2), omega=(1+4r^2)^(2/5), and let X_(s,w) be the completion of smooth compactly supported real functions even in x and odd in y for the norm

 X(h)^2=||omega D^2 J^s h||_2^2+w1||D J^s h||_2^2+w2||J^s h||_2^2.

The scalar closure estimate has mu0=97/250, C=397, A=(8/5)/sqrt(s), mu=mu0-Cs and c_s=(4 pi s(1+s))^(-1/2). For r>0 the admitted nonnegative residual sizes eta obey beta=mu-Ar>0, eta<=beta r, c_s r/2<1 and 7/10-c_s r>0. Under these conditions, the exact largest eta is

 eta*=40722836401/193491763200000,
 r*=201799/149299200.

This statement maximizes the specified scalar estimate over r in this one fixed norm. It does not optimize all proofs, weights or norms. Using it for the IPM existence theorem still requires the already audited T4-019 (A) to (D) reference, origin normalization, tail, signed L2 margin, weighted matrix, commutator, realization and inverse hypotheses and F in X_(s,w). Those hypotheses are not established for a candidate here. The frozen T2 sharp and T4 defect proofs give their exact definitions and are dependencies, not numerical premises silently discharged by this audit.

## Complete argument

mu=201799/648000>0 and A=576/5>0. For every real r, expand the right hand side to obtain the polynomial identity

 (mu-Ar)r=mu^2/(4A)-A(r-mu/(2A))^2.

The negative square proves the global bound eta<=mu^2/(4A), with equality only at r*. At r*, beta=mu/2=201799/1296000>0. To verify that the maximum is admissible, use pi>314159/100000. It gives

 (c_s r*)^2 < 40722836401/54043470895104 < (2746/100000)^2.

Thus c_s r*/2<1373/100000<1 and 7/10-c_s r*>67254/100000>0. The first inequality for pi can also be checked independently by a 1024-bit Arb pi enclosure. Every scalar condition therefore holds at the asserted maximum. No numerical sampling in r is used to prove maximality.

At the selected old radius r0=1351/1000000, beta=63092119/405000000, and beta*r0=85237452769/405000000000000. Exact comparisons give

 4207/20000000 < 21046/100000000 < beta*r0 < eta* < 21047/100000000.

The conservative beta floor 1557/10000 also admits 4207/20000000. Therefore the old sufficient test remains correct, while its unrestricted maximality attribution is false. The audited defect formula epsilon_max=((mu-Am-B)^2-4ABm)/(4A) at g=0, m=B=0 agrees with eta*. The zero trial satisfies every domain and multiplier requirement without a numerical solve.

For comparison, if s varies and the same scalar rate is assumed, the envelope is f(s)=(5/32)(mu0-Cs)^2 sqrt(s) for 0<s<mu0/C. Its derivative has the sign of (mu0-Cs)(mu0-5Cs), hence its unique maximum occurs at s0=97/496250. Its exact square is (25/4) C^4 s0^5 and its positive value is (5/2) C^2 s0^(5/2). This changes the norm. It supplies no ordering of norms or balls.

Finally retain N4-180's accepted full-component lower comparison X(F007)>756.5312630768 in this same norm. Positive exact division gives X(F007)/eta*>3594606 and X(F007)/(4207/20000000)>3596535.57. These are failures of sufficient smallness, not nonexistence or correction-distance comparisons.

## Source and report checks

Freeze T4-479's proof and result, T4-065's defect proof and result, both T2 maximum/repair reviews and their programs, logs and outputs, the original sharp proof and the saved repaired report excerpt. Inspect peer programs but do not execute them. Recompute polynomial coefficients and every rational comparison independently. Bind the accepted N4-180 full-component result and its exact input hashes. Verify the three repaired report blocks against the exact fractions and distinguish the excerpt from a changing live report. Preserve exact source hashes and real timestamps. A numerical source integral is not recomputed in this finite composition audit.

Both available Opus theory lanes contributed the already read theory and review artifacts. Their configured model is us.anthropic.claude-opus-5-5; the actual provider response is not observable from these files. No replacement model or remote client is used. All no-JavaScript/TypeScript, no-server and no-RLScience-cluster restrictions remain in force.
