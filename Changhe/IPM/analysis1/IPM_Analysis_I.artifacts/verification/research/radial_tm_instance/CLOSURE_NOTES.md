# Final linkage bookkeeping and accepted scope

The actual Opus5.5 linkage review at2026-10-21T02:38:52Z accepts the exact
linear-image proof subject to dtype and identity assertions. The finalizer
checks that T_mid,T_rad,F_mid,F_rad have dtype float64 in each saved NPZ,
and that each saved NPZ hash is identical in the completed v3 calculation,
the exact linkage calculation, and the current file. Thus those conditions
are discharged explicitly, without modifying either reviewed checker.
Float64 inputs are converted to their exact dyadic rationals. (Float32
would also convert exactly to binary64, but is not used here.)

The input interpretation is a_m(u)=sum_k T_(k,m)u^k with
u=t-t_a, t=log r, cosine frequencies2m, and no halving of a_0. This is the
meaning of the finite input problem. The checker verifies the complete
T-box image in the F box under precisely that convention. Identification
of these T polynomials with the exact normalized spline at t_a remains
OPEN, as does all A/B canonical membership not separately audited.

The accepted wording is "local finite-input ODE enclosure verified on
cells0,4102,7808 for all261 modes" and "saved T-box image is contained in
saved F box, verified exactly (3cells*261modes*8orders)". The same-runtime
arrays and source are pinned. Every other whole-flow obligation remains
OPEN. The original limited proof, all addenda and this note must be read
together. No exact IPM solution or decisive endpoint is proved.
