# Weighted L2 tail reduction and decimal output audit

This is a conditional integration theorem and an independent scalar arithmetic audit. It does not validate the physical residual majorants from which its scalar inputs were reported. No full-plane residual norm, inverse, existence or exclusion is established here.

## Statement, hypotheses and notation

Let L, R_i, R_o and delta be positive real numbers. Let m(r)>0 for r>0, and let epsilon be a measurable function on the plane. Suppose that nonnegative constants C_i and C_o satisfy, for almost every angle and radius in the indicated regions,

    |epsilon(r,theta)|/m(r) <= C_i,                         0<r<=R_i,
    |epsilon(r,theta)|/m(r) <= C_o(1+r/L)^(-delta),         r>=R_o.

Write U_o=R_o/L. Define the weighted squared tail integrals using planar Lebesgue measure dX by

    I_i = integral_(|X|<=R_i) |epsilon(X)/m(|X|)|^2 dX/(1+|X|^2/L^2),
    I_o = integral_(|X|>=R_o) |epsilon(X)/m(|X|)|^2 dX/(1+|X|^2/L^2).

Then

    I_i <= B_i := pi C_i^2 R_i^2,
    I_o <= B_o := pi C_o^2 L^2 U_o^(-2 delta)/delta.

If a nonnegative number F bounds the same squared integral on R_i<|X|<R_o, and R_i<R_o, then the full norm is at most sqrt(F+B_i+B_o). F must refer to the same epsilon and m and a complete finite-annulus cover. This last statement is conditional on all these hypotheses.

## Proof

Tonelli's theorem and polar coordinates apply because the integrands are measurable and nonnegative. On the inner disk, use 1/(1+r^2/L^2)<=1. The angular integral is 2pi and the radial integral of r is R_i^2/2, giving I_i<=pi C_i^2 R_i^2.

For the outer integral, set u=r/L. The stated majorant gives

    I_o <= 2pi C_o^2 L^2 integral_(U_o)^infinity
                   (1+u)^(-2 delta) u/(1+u^2) du.

For every u>0 and delta>0, (1+u)^(-2 delta)<=u^(-2 delta) and u/(1+u^2)<=1/u. The integral is therefore at most

    integral_(U_o)^infinity u^(-1-2 delta) du = U_o^(-2 delta)/(2 delta).

This proves B_o and shows exactly why positive delta is required. The weighted measure alone has infinite mass outside every disk: its radial antiderivative is (L^2/2)log(1+r^2/L^2). A constant pointwise bound without decay does not supply a finite outer norm by multiplication by that measure.

The two boundary circles have planar measure zero. Additivity on the three regions proves the conditional full-norm assertion. This argument needs no differentiability, Poisson formula or stationarity, and in particular proves none of their hypotheses.

## Exact data and independently reproducible scalar application

The numerical lane reports its constants and tail boundaries for the stored modal trial. Copy the particular source files into this topic's sources folder and retain their hashes and original paths. Extract k, L, a and b from the exact binary64 entries in its literal trial NPZ, recording those rational numbers in exact JSON. Define delta=1/2-k, R_i=exp(a-5), R_o=exp(b+17). Do not replace these boundaries by printed decimal radii. Confirm positive delta and R_i<R_o from interval enclosures.

A printed ball [c +/- r] is used only through the exact decimal rationals c and r. Its endpoint c+r is a chosen nonnegative majorant constant. The physical validity of the ball remains an explicit external hypothesis. In particular the scalar computation does not turn its source's description of a residual majorant into a proof.

For F, record separately the exact binary64 values obtained by JSON decoding the three stored finite-region L2 numbers, matching the arithmetic input to r2_tails.py. Their sum is an exact rational. Its relation to the true finite-region integral is not verified by this scalar audit. A result for those three numbers is only an arithmetic conditional statement.

Compute B_i and B_o by Arb balls at 512 bits from exact rational inputs. Independently compute by mpmath.iv at 220 decimal digits using the equivalent exterior expression

    B_o = pi C_o^2 L^(2+2 delta) exp(-2 delta (b+17))/delta.

The second expression eliminates U_o and uses a different multiplication and power sequence. Retain exact dyadic lower and upper endpoints of both calculations. Require overlap as a consistency check. For any accepted decimal upper ceiling q, require q to exceed both interval upper endpoints, using rational comparisons. Comparing an unrounded endpoint with a decimal string determines whether that particular decimal is inward or outward; a nearest-rounded decimal is not automatically a directed upper endpoint. A rigorous arithmetic counterexample to such a label consists of both computed lower endpoints strictly exceeding the labelled value.

Also evaluate the two enlarged constants explicitly printed in NUM_REPORT, C_o=1.75412e-6 and C_i=2.13842e-6, before judging the displayed ceilings 6.504e-16 and 3.819e-20. Replacing an exact scalar by a larger printed constant increases the corresponding bound quadratically.

All code and exact JSON inputs must be saved and hashed before the numerical check. The numerical instance remains OPEN until actual Claude Opus 5.5 reviews the proof, code and complete outputs, its actual recorded model/end condition are checked, and a later own adjudication resolves the findings. Recompute every scalar in both interval systems. No large field, GPU or heavy process is needed.
