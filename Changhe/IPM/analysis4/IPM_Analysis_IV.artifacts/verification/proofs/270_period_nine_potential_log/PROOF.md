# The first potential logarithm at period nine

Status: the finite potential-logarithm statement is PROVED in V550. Infinite convergence requires the separate267 admission.

## Statement and hypotheses

Let delta=2/9 and c_l=9/7. Let P_18 be the primitive first stream-compatibility polynomial for f_1(theta)=sin(theta)+b sin(3theta), as defined in267. Assume that the independent exact checks in267 establish that P_18 is irreducible of degree18. Let a_9(b) be the sin(theta) coefficient of the uniquely determined f_9, and assume the exact check below establishes that a_9 is a nonzero polynomial of degree at most9.

For every real root b of P_18 and every real epsilon nonzero, the common-potential expansion for the leading density epsilon[sin(theta)+b sin(3theta)] requires a nonzero correction

    epsilon^9 r^2 log(r)[alpha_9(b)+beta_9(b)cos(2theta)].

This is a finite-order obstruction to a pure finite-cosine common potential. It does not assert convergence of the later tuned series unless the separate267 hypotheses are admitted. If that convergence is admitted, this finite logarithmic term leaves its sufficient radius unchanged. No assertion is made that the second permitted logarithmic correction at order18 is nonzero.

## Proof

All positive sine Poisson multipliers before order9 are nonzero. At order9 the only formal resonant frequency is zero, which is absent. Thus f_9 and g_9 are determined by f_1, independent of every later free stream harmonic. The quadratic recursion implies that a_9 is a rational polynomial of degree at most9 in b.

For a pure common potential r^2 c_m cos(2m theta), direct differentiation gives

    -partial_y Delta[r^2 c_m cos(2m theta)]
      =4m(1-m^2)c_m r^-1
        [sin((2m+1)theta)+sin((2m-1)theta)].

The columns m=0 and m=1 vanish. Every remaining column has frequency at least3, so no finite sum of pure columns produces a nonzero sin(theta) coefficient. Since P_18 is irreducible of degree18 and a_9 is nonzero of degree at most9, they have no common root. Therefore a_9(b) is nonzero at every real compatibility root and a pure degree-two potential is impossible.

For completeness, eliminate successively the highest density frequencies with the displayed pure columns. The residual has the form a_9 sin(theta)+d_9 sin(3theta). The identities

    -partial_y Delta(r^2 log r)=-4r^-1 sin(theta),
    -partial_y Delta(r^2 log r cos(2theta))
       =4r^-1[sin(theta)+sin(3theta)],
    partial_x partial_y(r^2 log r)=sin(2theta),
    partial_x partial_y(r^2 log r cos(2theta))=-sin(4theta)/2

then give alpha_9=(d_9-a_9)/4 and beta_9=d_9/4. Their difference beta_9-alpha_9=a_9/4 is nonzero. The reconstructed and prescribed streams solve the same Poisson equation at radial degree zero, where every positive sine multiplier is nonzero, so they agree. Homogeneity multiplies this order by epsilon^9. The reconstruction theorem132 controls the finite logarithmic correction whenever the later series converges.

## Verification and dependencies

Compute the positive-frequency polar prefix independently through order9, and compare every coefficient with267's signed Cartesian exact prefix. Extract a_9, check its degree and nonvanishing, and verify a rational Euclidean remainder chain against P_18. Carry out the pure-column elimination and check every reconstructed density and stream coefficient using the Cartesian derivative operators and the four exact logarithmic identities.

Dependencies:01,132,258,267. The recorded result must distinguish this finite potential statement from an all-order convergence admission.

## Completed finite verification

V550 at 2026-10-31T19:40:26+00:00 verifies all hypotheses of the finite statement. The independent polar prefix agrees with180 signed-Cartesian density/stream coefficients, using36 ordered products. Its nonzero degree-nine a_9 agrees with all ten coefficients of the theory part's independent exact polynomial. A rational Euclidean chain ends in a unit, and all36 reconstructed density and stream coefficients agree exactly. The computation took1.91844seconds. Thus all ten real P_18 roots require the stated nonzero order-nine potential logarithm, regardless of whether the later all-order tuning certificate is eventually completed.
