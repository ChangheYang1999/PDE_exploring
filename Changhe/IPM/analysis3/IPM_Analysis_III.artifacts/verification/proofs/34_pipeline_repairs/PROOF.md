# Repaired scalar enclosures and the remaining tail-arithmetic obligations

This audit concerns only the fixed Python snapshots in `code_snapshot`. It does not certify a matrix, a margin value or an infinite-dimensional inverse. The dependency V033 is proof 30. The executable check uses the installed Arb binding but imports no pipeline driver.

## 1. Directed endpoint conversion

Let x be a finite Arb ball and let u be its exact dyadic upper endpoint. Start with the nearest binary64 value f of u. Repeatedly replace f by the next binary64 value toward positive infinity while the exact comparison f<u holds. The returned finite value is at least u. The lower procedure is identical with reversed inequalities. Overflow to infinity is not a finite certificate and must be rejected separately.

The snapshotted `fup` and `flo` implement this procedure. Conversion of a tiny positive endpoint below half the least positive subnormal initially gives zero, but the loop then advances to the least positive subnormal, which is an upper bound. Negative underflow is handled by the lower procedure. The executable check covers this case, negative endpoints, midpoint ties, interval inputs and large finite values. `finite_or_raise` rejects both infinities and NaN.

For a finite list of finite balls, comparing their exact upper endpoints selects a ball with the largest upper endpoint. Thus `max_upper` repairs the row-maximum defect of V033. This does not turn the chosen ball into an exact norm: its upper endpoint is the norm bound used in the subsequent estimate.

## 2. Gradient, angular quotient and Hessian bounds

If r and t enclose the polar components of the density gradient, set R=upper(|r|), T=upper(|t|). These are nonnegative exact dyadic points. Then sqrt(R^2+T^2) bounds the gradient norm above. Subtracting a lower bound for rho_y and dividing by two bounds b_+=(|grad rho|-rho_y)/2 above. Taking the lower endpoint after insertion into the margin therefore yields a valid lower bound. The repaired margin code follows this order.

The anisotropic term is

    tan(theta) V.grad(theta)
      = sin(theta) sum_n Qe_n(t) sin(2n theta)/cos(theta).

The isotropic dilation contributes zero. For each n>=1,

    sin(2n theta)/cos(theta)
      = 2 sum_{j=1}^n (-1)^(n-j) sin((2j-1)theta),

including the continuous extension at theta=pi/2. Multiplying by cos(theta), using twice the product-to-sum identity and cancelling adjacent terms proves the formula. The absolute value is at most2n. The code's exact low-mode identity and higher-mode bound are valid. Its hull of both slopes at t=0 is also valid. An anisotropic global certificate requires **every** box to have a finite bound; taking `nanmin` after an exception gives only a bound on the boxes that succeeded. The output's `aniso_nan_boxes` must therefore be zero before a global assertion is made.

For the velocity derivative, use the orthonormal polar Hessian entries

    H_rr=psi_rr,
    H_rtheta=psi_rtheta/r-psi_theta/r^2,
    H_thetatheta=psi_r/r+psi_thetatheta/r^2.

Every Cartesian Hessian entry is bounded by the sum of their absolute values. The code's sum of bounds for psi_tt/r^2, twice psi_t/r^2, twice psi_ttheta/r^2, psi_thetatheta/r^2 and psi_theta/r^2 is larger than this sum. It is thus a valid entrywise bound, and twice it bounds the Frobenius norm. The finite-cell and half-line enclosures still depend on the exact background and the already audited exponential-polynomial sup bounds. They are not independently recomputed here.

## 3. Corrected velocity decomposition

The new part(c) calls the canonical plain-B `ColumnFix.green_on_cell` using the column's existing data. Its formula uses the same Green endpoints and source pieces, with no strain-subtracted linear velocity. Part(d) adds the radial strain term and the exponent-column transport remainder. This is exactly the decomposition derived in V033, so the formerly missing c(-x,y).grad rho term is now supplied inside part(c). The signed aggregate angular coefficients `Pcol` are retained. This repairs the algebra, not the rounding proof.

## 4. Surviving failures and unresolved finite arithmetic

The nested `offbasis.t_of` still tests positivity by `float(v.upper())>0`. With exact v=2^-1200, that float is zero and the routine returns0. The correct positive square root is2^-600. This is an exact counterexample to the routine as an unconditional upper bound. Compare the dyadic endpoint with0 instead. Reject nonfinite endpoints. The last sum of squares should likewise use nonnegative exact upper endpoints if the intermediate balls can straddle0.

The tail accumulator still uses nearest floats for some coefficients, uninflated `np.add.at`, uninflated final additions and a final factor1+1e-8. A multiplicative factor alone does not cover underflow: the positive binary64 number2^-600 has a squared product that rounds to0. No multiplicative inflation recovers a positive bound. This refutes an unrestricted arithmetic claim; it does not establish that the actual data underflow. A proof for the actual finite data needs operation counts, a bound for every relative rounding error, and control of any underflow/overflow. Alternatively use outward operations throughout.

One implementable outward route is to round each positive sum and product upward with `nextafter`, including subnormals, and to convert all scalar coefficient bounds with `fup`. In each `np.add.at` call here the absolute-value frequency map has multiplicity at most2. Two upward steps after that call bound its at-most-two successive nonnegative additions, because the ulp cannot decrease along a nonnegative accumulation. A final positive sum can be accumulated in Arb or with a proved directed summation routine. This paragraph describes a sufficient repair, not code already in the snapshot.

## 5. Verdict and scope

CONFIRMED: directed finite scalar conversion, exact row maximum, repaired gradient and anisotropic quotient formulas, plain-B decomposition. REFUTED: unconditional upper-bound status of the current `t_of` and unrestricted multiplicative treatment of underflow. OPEN: actual matrix entries, numerical margin, full tail arithmetic and the complement inverse. No numerical output from the active jobs is promoted to a certificate by this audit.
