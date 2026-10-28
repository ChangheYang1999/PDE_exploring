# The vertical angular margin is not an all-covector energy margin

## Exact frozen statement

Let D,Sigma>0, delta>0 and sigma>1. On R_t x R_z consider

 P=D partial_t-Sigma z partial_z+a, a=delta D.

Use the ordinary isotropic inhomogeneous H^sigma norm. Choose a nonzero real smooth compactly supported function phi(t,z), even in z, with support separated from z=0 and contained in an arbitrarily small strip |z|<epsilon. Put

 u_N=N^(-sigma) exp(iNt) phi(t,z).

Then

 ||u_N||_H^sigma^2 -> ||phi||_2^2,
 Re <P u_N,u_N>_H^sigma -> (a+Sigma/2)||phi||_2^2>0.      (1)

For every fixed exponential t weight and every fixed power weight in z, the low norm of u_N is O(N^(-sigma)) and its low P graph norm is O(N^(1-sigma)). In particular both tend to zero.

Consequently no estimate

 -Re <P u,u>_H^sigma >= c ||u||_H^sigma^2-C ||u||_low^2  (2)

can hold with c>0 and finite C, even if the low graph norm replaces the low norm. The same conclusion holds with any quadratic error defined by a compact operator on H^sigma on the right.

## Proof

The Fourier transform of u_N is N^(-sigma) phihat(xi-N,zeta). Translation xi=N+eta and dominated convergence prove the first assertion of (1).

The term D partial_t is skew-adjoint and commutes with the Bessel potential. For the dilation term, Fourier integration by parts gives the exact identity

 Re <P u,u>_H^sigma
 =integral [a+Sigma/2-sigma Sigma zeta^2/(1+xi^2+zeta^2)]
            (1+xi^2+zeta^2)^sigma |uhat(xi,zeta)|^2 dxi dzeta.

After the same translation, its last quotient tends to zero, with a bounded integrand dominated by a Schwartz majorant. This proves the second assertion. The low statements follow from the fixed compact support and the explicit derivative of exp(iNt). The normalized u_N converge weakly to zero in H^sigma, so every compact quadratic error also tends to zero. This proves the counterexamples to(2).

Real-valued tests can be obtained by replacing exp(iNt) by cos(Nt); the two separated frequency packets have the same limits after multiplying by sqrt(2).

## Relation to the IPM vertical end

The frozen vertical cofactor equation of proof 102 is precisely this P, with a=delta D. The positive number in V088 is

 m_y=Sigma(sigma-1/2)-delta D,

which corresponds to an angular covector (xi=0, |zeta| large). The full leading negative-energy expression at the vertical endpoint is instead

 -delta D-Sigma/2+sigma Sigma zeta^2/(xi^2+zeta^2).        (3)

For a tangential covector (zeta=0) it is negative. For the exact original k and delta=9/5, the magnitude delta D+Sigma/2 is greater than54. Taking sigma=25/4 makes the angular value positive but leaves that tangential value unchanged.

The tests meet the remainder zero-axis condition because their normal support is separated from zero. Their parity can be imposed by the even normal extension and the physical reflections. In a fixed small vertical sector, the polar and vertical projective charts are smooth changes of variables; at the endpoint their principal symbols converge to the displayed ones.

For the actual profile, move the radial support sufficiently far into the origin end and shrink the vertical angular support. The cylinder field, cofactor zero-order term and their relevant derivatives approach the frozen coefficients. The local principal coupling is O(r^2). The strain and exact axis-row terms are compact on such high-frequency packets, by the already proved row compactness and separated kernels. The negative sign in (3) therefore persists. A smooth bounded escape multiplier on the blown-up compactification has V.grad log(weight) tending to zero at this endpoint, so a fixed such multiplier cannot repair an all-covector positive-energy claim there.

This last observation concerns a scalar smooth escape multiplier of the proposed form. It does not exclude more general graph estimates or microlocal symmetrizers.

## The norm estimate can still be true

This is not a counterexample to an a priori estimate involving ||P u||_H^sigma. For these packets, that norm grows like D N ||u_N||_H^sigma. They are noncharacteristic. A plausible H3 proof splits phase space: use the first-order ellipticity where |V.xi| is bounded below by a fixed multiple of |xi|, and use a positive negative-energy coefficient on the complementary characteristic cone. At the vertical endpoint the characteristic covectors are angular, exactly the directions covered by the verified positive V088 margin.

Thus an angular frozen margin cannot be promoted to a full energy theorem. The selected-low frozen regularization theorem V104 is unaffected; it uses the equation to recover the tangential derivatives after controlling normal derivatives.
