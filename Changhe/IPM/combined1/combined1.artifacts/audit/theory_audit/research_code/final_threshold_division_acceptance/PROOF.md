# Acceptance of the exact threshold divisions for candidate007

## Statement

For the immutable candidate007 lower-comparison records frozen by N4-429, the integer factors 84699685 and66246337 are supported by division by the exact thresholds1/163840 and3/327680, respectively. The prior84699902 is not the floor of the same X3 comparison divided by its exact threshold. No upper bound for the unknown actual norm is inferred from this transcription error. The rebalanced prior threshold decimal errs in the conservative direction. These are finite arithmetic and source-identity claims; no integral, inverse or existence conclusion is newly established.

## Exact data and argument

The two positive lower comparisons are

    LX=5169658564469929616848857/10^22,
    LN=30325166845552152737989/(5*10^19).

Their thresholds are tauX=1/163840 for FW-T-T4L2-v1 at s=2^-17 and tauN=3/327680 for FW-T-TB-rebal-v1 at s=2^-16. These registrations agree with the previously accepted framework proofs. For a nonnegative quantity Q with Q>L>0 and tau>0, division preserves the strict inequality Q/tau>L/tau. Hence any integer m with m<L/tau is a valid strict lower factor. Direct positive-denominator cross multiplication gives

    84699685 < LX/tauX < 84699686,
    66246337 < LN/tauN < 66246338.

The saved ratio balls use more precise underlying lower values. Their lower endpoints are above the ratios of the rounded printed L, by less than10^-15. This is consistent with the rounding direction. The ball need not contain the ratio formed from printed L. Both independently support the displayed integer lower factors.

The old decimal dX=0.0000061035 satisfies dX-tauX=-1/64000000000<0. Therefore LX/dX>LX/tauX. The old84699902 lies between these two quotients. It is an unsupported transcription from the exact-threshold quotient, not a bound on the actual norm in the reverse direction. The other old decimal dN=0.0000091553 satisfies dN-tauN=17/640000000000>0, so LN/dN<LN/tauN.

The revised summary's lower displays are no greater than their stored lower comparisons, its upper displays no smaller than the stored upper comparisons, and its thresholds equal the registered exact fractions. Its integer factors equal the floors just derived. Source identity checks establish that the old and new records have identical candidate hash, components, derived values and lower/upper comparisons. Only threshold divisions and displays change.

The named old spellings are absent from the three frozen final documents. This proves absence only of those spellings at those hashes. Later revisions require their own checks, and literal absence is not an audit of all mathematical prose.

## Dependencies and verification scope

The accepted original integral and framework records are premises, explicitly bound in the data manifest. N4-429's code is read as text; this lane writes its own exact rational checker. The checker verifies all source bindings, two divisions, rounding directions, ball endpoints, summary cells and finite spelling counts. Every original producer input is frozen or represented by its verified hash. The proof precedes this checker. Complete verification evidence lives beside it in `verification/`; no peer code, server or research integration is executed.
