# Hardy-endpoint premise in the report table

## 1. Exact object and comparison

The candidate report has SHA256 cd6d637c8f087e1d863d59549fdc1d34035293c55a7a5d11c5e087969f485a32 and records verdicts through A3236. Its predecessor is the A3236-approved report 3a7625dbaa9ecb752014860e39a2c7e733df1d090a81bf82173e71f8a2a13847. The independently generated normal diff agrees byte for byte with the declared diff: 38 lines, 28 changed-content lines, five hunks, SHA256 4c38a38d4e171b4a5fd2f7522dbd3ea80225df031f7fc67420f0d40559195438. Every diff line, including both full table rows, was read. The detailed Theorem 8(o) is byte-identical. The candidate has 8349 lines and 1337121 bytes.

The mathematical change is confined to the premise cell for Theorem 8(o) in Section 3.1. It explicitly adds the endpoint gradient-budget assumption for the endpoint moment limits and D >= D_*. Other changes are status, approval history and the explanation of this repair. This review confirms those changes. A newly identified source-return omission in the same table and the coordinator README is reviewed separately; complete current handoff consistency is pending that repair.

## 2. The two different amplitude conclusions

Let U be a real C1 divergence-free vector field on R3. Suppose E(R)=integral_(|y|<R)|U|^2 satisfies E(R)/(L R^beta)->1 for L>0 and 0<beta<1. Set t=(beta-3)/2, k=(beta+1)/2, H_beta=t^2(k^2+4)/(k^2+2), and

    G_a(R)=integral_(1<|y-a|<R)|y-a|^(2-beta)|DU(y)|_F^2,
    D=limsup_(|y|->infinity)|y|^((5-beta)/2)|DU(y)|_F,
    D_H^2=beta L H_beta/(4pi),
    D_*^2=9 beta L t^2/[4pi(k^2+2)].

The limit superior D may be infinite. The endpoint statement A3149 assumes, about one fixed center a,

    limsup_(R->infinity) G_a(R)/(beta L log R)<=H_beta.

Only under this added assumption do its specified moment limits and D>=D_* follow. That premise transfers between fixed centers by the existing endpoint proof. The new table states it explicitly and identifies this as a kinematic result. It does not claim that every Euler profile has an endpoint gradient budget.

The strict inequality D>D_H under the energy ratio alone follows separately. If D<=D_H were finite, then for each epsilon>0 the full spatial limit superior bounds |DU| by (D+epsilon)|y|^((beta-5)/2) at all sufficiently large points. Radial integration gives limsup G_0/(beta L log R)<=4pi D^2/(beta L)<=H_beta. The endpoint result would give D>=D_*>D_H, a contradiction, since D_*^2/D_H^2=9/(k^2+4)>1. Infinite D already satisfies the strict bound. A3179 separately supplies an explicit positive improvement under the energy ratio alone; that improvement does not require the endpoint premise. For nonzero full Euler profiles in 2/5<c<1/2 the confirmed energy theorem gives beta=5-2/c and L>0. This is how the two kinematic statements apply to profiles, for every fixed finite omega.

## 3. Evidence, collaboration and scope

The detailed endpoint paragraph, the exact premise of the endpoint reconstruction, the separate quantitative-gap statement, and the complete new C comparison were read. C's existing configured model note of 12:33:55Z agrees with the distinction above; provider execution is independently unattested. The complete literature-agent note of 12:28:05Z that requested this precision was also read. No diagnostic or new model client was used.

The endpoint-table change is confirmed. Historical appendices and the full README are not collectively certified. The separate source-return summary review identifies an omitted nonzero translation vector and a missing replacement for uniform decay in the README; these do not refute the correctly stated detailed theorems. No theorem changes after the mathematical freeze, and the main arbitrary-omega conjecture remains OPEN.
