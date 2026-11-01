# The first potential logarithm at period ten

Status: PROVED finite statement, admitted V583. Infinite convergence is a separate claim.

## Statement and hypotheses

Let delta=1/5 and c_l=5/4. Let P_20 be the primitive first stream-compatibility polynomial for f_1(theta)=sin(theta)+b sin(3theta), as defined in281. Assume that the independent exact checks in281 establish that P_20 is irreducible of degree20. Let a_10(b) be the sin(theta) coefficient of the uniquely determined f_10, and assume the exact check below establishes that a_10 is a nonzero polynomial of degree at most10.

For every real root b of P_20 and every real epsilon nonzero, the common-potential expansion for the leading density epsilon[sin(theta)+b sin(3theta)] requires a nonzero correction

    epsilon^10 r^2 log(r)[alpha_10(b)+beta_10(b)cos(2theta)].

This is a finite-order obstruction to a pure finite-cosine common potential. Convergence of the later tuned series requires a separate all-order admission; the finite-algebra result281 alone is insufficient. If the separate tuned convergence theorem is admitted, this finite logarithmic term leaves its sufficient radius unchanged. No assertion is made that the second permitted logarithmic correction at order20 is nonzero.

## Proof

All positive sine Poisson multipliers before order10 are nonzero. At order10 the only formal resonant frequency is zero, which is absent. Thus f_10 and g_10 are determined by f_1, independent of every later free stream harmonic. The quadratic recursion implies that a_10 is a rational polynomial of degree at most10 in b.

For a pure common potential r^2 c_m cos(2m theta), direct differentiation gives

    -partial_y Delta[r^2 c_m cos(2m theta)]
      =4m(1-m^2)c_m r^-1
        [sin((2m+1)theta)+sin((2m-1)theta)].

The columns m=0 and m=1 vanish. Every remaining column has frequency at least3, so no finite sum of pure columns produces a nonzero sin(theta) coefficient. Since P_20 is irreducible of degree20 and a_10 is nonzero of degree at most10, they have no common root. Therefore a_10(b) is nonzero at every real compatibility root and a pure degree-two potential is impossible.

For completeness, eliminate successively the highest density frequencies with the displayed pure columns. The residual has the form a_10 sin(theta)+d_10 sin(3theta). The identities

    -partial_y Delta(r^2 log r)=-4r^-1 sin(theta),
    -partial_y Delta(r^2 log r cos(2theta))
       =4r^-1[sin(theta)+sin(3theta)],
    partial_x partial_y(r^2 log r)=sin(2theta),
    partial_x partial_y(r^2 log r cos(2theta))=-sin(4theta)/2

then give alpha_10=(d_10-a_10)/4 and beta_10=d_10/4. Their difference beta_10-alpha_10=a_10/4 is nonzero. The reconstructed and prescribed streams solve the same Poisson equation at radial degree zero, where every positive sine multiplier is nonzero, so they agree. Homogeneity multiplies this order by epsilon^10. The reconstruction theorem132 controls the finite logarithmic correction whenever the later series converges.

## Verification and dependencies

Compute the positive-frequency polar prefix independently through order10, and compare every coefficient with281's signed Cartesian exact prefix. Extract a_10, check its degree and nonvanishing, and verify a rational Euclidean remainder chain against P_20. Carry out the pure-column elimination and check every reconstructed density and stream coefficient using the Cartesian derivative operators and the four exact logarithmic identities.

Dependencies:01,132,258,281. The recorded result must distinguish this finite potential statement from an all-order convergence admission.


## Completed verification

Admitted 2026-10-31T21:01:30+00:00. All220 prefix coefficient comparisons and40 reconstruction comparisons pass. All11 coefficients of a10 agree with the theory part independent polynomial. The degree10 polynomial a10 is nonzero and coprime to the compatibility polynomial; beta10-alpha10=a10/4. The computation used45 ordered products and took1.533226seconds.
