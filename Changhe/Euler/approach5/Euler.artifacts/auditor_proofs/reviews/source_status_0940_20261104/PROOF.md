# LIT379 and LIT380 version changes and the later comparison

## 1. Exact versions and scope

This review compares retained source files with the versions underlying A3132-A3135 and A3139-A3141. The complete differences are in `verification`. LIT379 changes74ab8bf0 to764ee00a; LIT380 changes2056b6a9 to6fde407a. The A comparison changesa9b67436 to524dd668. All three differences were read in full. This is a version and argument audit, not a new computation or a new literature retrieval.

LIT379 changes only its status paragraph. The mathematical body is identical. It correctly records the core inequality A3132, separate radial and large-gradient refinements A3133, the correction to the independent reconstruction A3134, and the remaining scope A3135. Those verdicts transfer without a mathematical change.

LIT380 changes its status paragraph and one sentence before the transition-energy calculation. The sentence now states explicitly that equations(12)-(14) use the old block's index on the decreasing half and the new block's index on the increasing half. This is exactly the active-block interpretation used in A3139 and Section3 of the independent reconstruction. No formula or quantifier is strengthened. A3139-A3141 transfer to6fde407a at the same scope.

## 2. Later A comparison and the toroidal coefficient

The later A comparison has chronological and reference corrections, an added discussion of Section9 of the independent reconstruction, and present-tense descriptions of the now confirmed attainment theorem. It also changes a stated numerical tolerance. No diagnostic script, log, sampled value or numerical tolerance is certified here. Item10 calls the nine-section reconstruction an eight-section text; this is a count typo and does not affect its argument.

The new analytical argument in R4 concerns

    h_beta=(3-beta)^(3/2)/sqrt(5-beta),
    m=2-beta, C=m(1-beta), 0<beta<1.

It claims h_beta>C. This is correct. One direct exact verification is

    h_beta^2-m^2=(7-3beta)/(5-beta)>0.

Both h_beta and m are positive, and m>C>0. Thus h_beta>m>C. The comparison's two-interval proof is also correct: logarithmic differentiation gives h_beta'/h_beta=-3/[2(3-beta)]+1/[2(5-beta)]<0; h_(1/4)^2=1331/304>(209/100)^2; h_1=sqrt(2); and for beta>=1/4 one has C<=21/16<33/25<sqrt(2). These exact inequalities justify its decimal bounds without using a sampled calculation.

The following sentence, that the toroidal share therefore must tend to zero, needs its quantifier and premise stated. The displayed estimate(18) is an upper bound for the source of the chosen mixture. An upper bound with h_beta>C cannot by itself force its mixing coefficient to vanish. The confirmed construction chooses epsilon_j->0, so its own good-block shares do vanish. Independently, the general source lower bound forces the logarithmic tangential fraction to vanish for any exactly attaining field; a toroidal component contributes to that fraction. This excludes a fixed positive share in that average. It does not assert pointwise-in-radius convergence of every possible toroidal share. The literature agent note of09:36:43 makes the same distinction. The original A3140 confirmed the coefficient and the qualified growth conclusions, not this stronger inference from an upper bound.

## 3. Conclusions

The source status changes and active-block clarification are confirmed at the original scopes. The new inequality h_beta>C is confirmed analytically. The deduction from an upper bound alone to a necessary vanishing share is invalid as written; replace it with either the explicit construction choice epsilon_j->0 or the independently proved logarithmic-average conclusion. A claim of general pointwise vanishing is not established by these arguments.

The comparison's other mathematical content transfers from its fully read earlier version. The diagnostic and counting corrections are recorded without certifying the diagnostics. All statements concern kinematic controls unless the complete full-profile hypotheses are separately imposed. The unrestricted arbitrary-omega conjecture remains open.
