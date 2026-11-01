# The final selected perturbation through order350

Status: completed finite audit, V506-V507. No stability theorem or bound for an input box is claimed.

## Exact quantities and hypotheses

Use the producer's two saved delta2/3,512-bit continuations initialized at order329. One reloads the certified centers and discards their prior radii. The other uses the single seeded boundary selection checked in217, with seed20261031. The latter is one selected configuration with tiny arithmetic enclosures, not the whole certified input box. All subsequent claims are conditional on these saved inputs.

For each density or stream coefficient array x_n and corresponding selected array y_n, let

    D_n=||y_n-x_n||_1/||x_n||_1,
    E=max_(1<=n<=329, field in {density,stream}) D_n.

Here the norm sums absolute values of all stored angular and logarithmic coefficients. The finite output amplification is D_n/E. A zero denominator is allowed only if the difference also vanishes, in which case its relative difference is defined as zero. The triangle inequality gives

    abs(||y_n||_1/||x_n||_1-1)<=D_n.

The norm-change metric can therefore underestimate full-vector displacement. Separately, log10 norm differences and maximum column differences are those defined in217.

## Audit argument

Load the two producer checkpoints as frozen byte strings, hash them, and verify their parameter, ring and precision metadata. Recompute every absolute coefficient norm and difference in directed768-bit arithmetic. Record both input and output differences and their normalized ratios, checking the triangle inequality enclosure. For the log-norm metric, independently recompute all column sums and compare any available published decimal table with its stated rounding precision.

These operations verify finite arithmetic for the selected arrays through350. They do not enclose the response to every point in the original interval input, establish monotone damping, or prove convergence of the canonical series. The input replay in217 provides the selected-input interpretation. The earlier amplification counterexample at330 and331 remains part of this audit, regardless of later attenuation.

Dependencies:217 selected boundary input and log-norm audit;224 full-vector amplification metric;01 Cartesian recurrence convention. No asymptotic inference is made.

## Completed result

The maximum selected input displacement is3.576017323058629551e-6. The stream displacement exceeds it at330 and331, by factors1.2284477612 and1.9183745652, and every output after331 through350 lies below it. At350 the density and stream displacements are7.1469987452e-10 and3.7707633742e-11. The density displacement increases from349 to350, so even late attenuation is not monotone. These are finite conditional observations.

The84 printed log-norm differences reproduce the saved binary-float calculation. Four are not the exact three-significant-digit roundings of the directed norms: dM347,dR348,dM349,dN350. Their correct rounded values are3.49e-11,1.05e-11,-8.89e-12,-4.65e-12. The maximum absolute float error across all entries is below4.489e-14. The directed arrays, exact dyadic enclosures and source hashes are retained in verification.
