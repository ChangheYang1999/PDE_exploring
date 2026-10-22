# Sharp weighted threshold and source audit requirements

This supplements PROOF.md; all its definitions and scope restrictions apply.

The exact input audit also checks bi>0. In the modal inner representation,
each exp(2j tau) with j>=1 and each exp(bi tau) tau^i tend to zero as
tau tends to minus infinity. The angular factors are bounded finite sums.
Thus its factor is bounded near the origin, and rho0=O(r^3) there. The
finite spline pieces and exact joins are locally bounded away from zero.
X3 is locally bounded by its explicit formula: its splines and finite
angular factors are bounded, its fractional factor is bounded and tends
to zero at the origin, and its logarithmic term is bounded on each finite
radial interval. These assertions do not require seventh derivatives.

The uniform limits proved in PROOF.md show that both densities are O(r^k)
at infinity. Hence, for gamma>1+k, their squared difference times
(1+r^2)^(-gamma) is integrable outside the unit disc, by comparison with
integral_1^infinity r^(2k+1-2gamma) dr; it is integrable inside by local
boundedness. Combining this with PROOF.md gives the exact criterion

 X3-rho0 in L2(R2,(1+r^2)^(-gamma)dX) if and only if gamma>1+k.

Only D nonzero is needed for nonmembership; positivity supplies an easy
exact check. The numerical witness at pi/4 proves nonidentity independently
of the angular differentiability argument once the uniform tail limits
have been established. Neither argument specifies a finite radius beyond
which the lower bound holds. No finite-radius pointwise error or weighted
Sobolev estimate follows from the witness alone.

The output audit reads both original NPZ archives with pickle disabled.
It checks the hexadecimal JSON against every X3 z coefficient and knot,
every modal leading coefficient, every modal knot, and every relevant
scalar. It separately verifies the original spline endpoint convention,
the exact sum T(1), all ten outer exponent signs and the published brackets
for the exact real scalar repair. It then verifies each saved interval
endpoint and each printed strict enclosure with rational arithmetic. The
analytic formulas and the outward interval libraries remain trusted
mathematical and computational dependencies, respectively.
