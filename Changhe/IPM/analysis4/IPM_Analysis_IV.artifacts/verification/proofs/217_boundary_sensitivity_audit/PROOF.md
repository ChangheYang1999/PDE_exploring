# Boundary-sample sensitivity of the midpoint continuation

Status: the finite norm differences are CONFIRMED inV451; monotonic contraction and uniform1e-8 accuracy on330 through340 are REFUTED inV452. The complete selected-input replay is CONFIRMED inV453. No stability theorem for the canonical series is asserted.

## Objects and scope

Fix the canonical polynomial-log recurrence at delta = 2/3, with leading density sin(theta). The certified checkpoint through order 329 assigns a real interval to every density and stream coefficient. Two subsequent computations choose different inputs from these intervals: the midpoint continuation uses the centers; the perturbed continuation, with random seed 20261031, chooses a sign for each nonzero input radius and uses the corresponding endpoint. Both then run the complete recurrence.

The intended endpoint is defined from the ball after loading it at 512-bit working precision. Loading can round a radius outward. Floating ball addition can also enclose the chosen endpoint in a small interval instead of storing a zero-radius point. These representation effects must be checked explicitly; they do not restore the uncertainty that was discarded when choosing a single input configuration.

Let M_n and N_n be the sums of absolute values of all density and stream coefficients, including every logarithmic column. A superscript p denotes the perturbed continuation and a superscript m the midpoint continuation. The reported differences are

    dM_n = log10(M_n^p/M_n^m),
    dN_n = log10(N_n^p/N_n^m),
    dR_n = dN_n - dM_n.

For each density logarithmic column q, let C_(n,q) be its absolute coefficient sum. The largest column difference is max_q |log10(C_(n,q)^p/C_(n,q)^m)|, over columns with nonzero norms. These are logarithmic differences, not relative errors of individual coefficients. Their conversions to relative norm differences are 10^dM_n - 1 and 10^dN_n - 1.

## Independent arithmetic procedure

The input audit reconstructs the frozen order-329 checkpoint, checks its recorded hash, and iterates through coefficients in the producer's stated order. It resets the same pseudorandom generator and verifies that each selected endpoint lies in the corresponding perturbed input ball. It records whether a selected input still has a nonzero radius while the earlier reset-provenance audit records the midpoint input. Agreement establishes which two input configurations were used; it does not establish that either one is the original exact coefficient sequence.

The finite norm audit independently decodes the two saved checkpoints, sums absolute coefficients in directed arithmetic, and evaluates the displayed differences with directed logarithms. At every audited order it compares the resulting intervals with the rounded table. The checks are conditional on the two saved input configurations and on the already audited recurrence implementation. No source checkpoint is modified.

A claim of decreasing differences at every consecutive order requires comparison of each consecutive pair. A claim of accuracy better than 10^(-8) throughout orders 330 through 340 requires that bound at every order in that range, in the specified norm. Endpoints alone do not establish either statement.

## Why one input sample is not a uniform error bound

For a map Phi from the input coefficient vector to later coefficients, observing a small difference Phi(x+v)-Phi(x) controls only that particular displacement. It need not bound displacements in other directions. Even for a linear map on R^2, take v = (1,0) and Phi_K(x,y) = K y. Then Phi_K(v)-Phi_K(0) = 0 for every K, although a displacement (0,1) is amplified by K. Thus a successful single-sample diagnostic supplies no operator norm, no bound over the input box, and no tail stability theorem.

The actual recurrence has special structure that this example does not analyze. To obtain a rigorous stability conclusion for it, one needs a verified enclosure for all relevant input displacements or a proved bound on the propagating difference equation. This audit claims neither.
