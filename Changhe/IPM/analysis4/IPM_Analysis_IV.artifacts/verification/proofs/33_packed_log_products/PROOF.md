# Packed polynomial-log products reproduce Cartesian transport

Status: confirmed for the stated exact identities, retained implementation, and finite recurrence prefix.

## Claim and representation

Let G_i(t,theta) be a finite even-sine polynomial with polynomial dependence on t, and F_j(t,theta) a finite odd-sine polynomial. Let their radial factors be r^(P_i) and r^(p_j), where P_i=2-i delta and p_j=1-j delta. The updated numerical routine packs the angular and t indices into ordinary polynomial coefficients to compute

\[
 [(P_i+\partial_t)G_i]\partial_\theta F_j
 -[\partial_\theta G_i](p_j+\partial_t)F_j.
 \tag{1}
\]

This is the coefficient of Cartesian transport at radial exponent P_i+p_j-2. The claim concerns the finite arithmetic operation, not a convergence property.

## Why the packing has no aliases

Write J for the greatest even-sine index of either stream array and K for the greatest odd-sine index of either density array. Every direct angular polynomial product has index between zero and J+K. The reversed density product also has index between zero and J+K, since its index is J_stream+K-K_density. The chosen stride S=J+K+2 is larger than every possible product index. Therefore packing a coefficient of t^q at index qS+angular_index permits exact recovery of both indices after multiplication. No angular contribution can spill into the next t block.

The direct product encodes the sum angular frequency, while reversal encodes the difference. If the difference index corresponds to d=j-k, the even-sine times odd-cosine product contributes to odd index d-1 for d>=1 and to index -d with a negative sign for d<=0. The even-cosine times odd-sine product has the opposite difference sign. Both product identities carry a factor 1/2. These are exactly the four branches in the retained routine. Multiplying the appropriate arrays by 2j or 2k+1 accounts for angular differentiation. Differentiation in t is performed before packing, with coefficient (q+1) at degree q.

## Independent exact checks

The checker uses a different representation: rational Laurent polynomials in the angular variable, with Cartesian X and Y operators and explicit polynomial t coefficients. It compares the packed result against `(X G_i)(Y F_j)-(Y G_i)(X F_j)`. Eighty seeded random cases vary rational delta, radial indices, t degrees, ragged angular widths, signs and rational amplitudes. Every Cartesian identity is exactly zero after subtraction.

The checker then executes the packed recurrence at delta=4/9, F_1=sin(theta), with total resonant stream constant zero. Every density and stream coefficient through order 73 equals the exact prefix already independently verified by Cartesian differentiation in topic 21. Including zero padding, this compares 15,885 density scalars and 16,550 stream scalars. The complete run took 112.38766820821911 seconds on one permitted CPU core.

## Evidence and scope

`verification/checks.json` records the random seed, dimensions, all prefix orders, scalar counts, timestamps and source hashes. The exact executed numerical source snapshots are in `sources/`; the checker is `code/packed_log_audit.py`. The reference prefix and its independent Cartesian proof are retained in topic 21. No float comparison is used for this verdict.

The algebraic packing argument holds for every finite array with the specified parity conventions. The executable checks establish the recorded implementation's results on the stated cases and prefix. They do not certify unrelated statistics routines, later checkpoint precision, the original potential at every high order, or convergence of an infinite logarithmic series.
