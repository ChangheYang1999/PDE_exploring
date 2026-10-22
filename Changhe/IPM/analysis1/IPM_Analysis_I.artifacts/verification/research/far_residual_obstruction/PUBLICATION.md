# A nonzero residual tail excludes all unweighted L2 corrections

The exact normalized modal trial rho0 cannot be corrected to a stationary
canonical profile by any h in L2(R2), for any finite real scaling c, within
the explicit locally regular sublinear realization in PROOF.md and
ADDENDUM.md. This includes every unweighted Hs correction, s>=0.

Let beta=2k-1, R_b=exp(tplus) and tau=log(r/R_b). The exact leading
residual is epsilon0=r^beta Epsilon(theta)+o(r^beta), uniformly in angle.
The coefficient e0 of sin(theta)exp(beta tau), the corresponding physical
coefficient E0=R_b^(-beta)e0, and the leading trial density at theta=pi/4
satisfy the following strict enclosures separately in Arb512 and iv180:

 -0.0002000282880 < e0 < -0.0002000282879,
 -0.03688201144 < E0 < -0.03688201143,
 90.81020983897880 < Theta(pi/4) < 90.81020983897882.

For a hypothetical L2 correction, its actual canonical velocity difference
is the L2 Fourier multiplier, with norm at most ||h||2. Harmonic uniqueness
is established under the stated sublinear growth condition. Testing the
stationary equation on expanding annuli with S^(-1)phi(X/S) makes every
term containing h tend to zero. The leading density term first forces
c=1/k. The nonzero residual coefficient then gives an annular pairing of
order S^(2k), a contradiction because 2k>0. No pointwise expansion or
derivative estimates for h are used.

The trial residual itself lies in L2((1+r^2)^(-gamma)dX) exactly when
gamma>2k. Thus it tends to zero at infinity but does not belong to
unweighted L2.

This is not a decisive NO for the research prompt. The separately verified
topic103 shows X3 is outside rho0+L2. Moreover arbitrarily small tail
changes in the weighted factor norm can leave that affine class, even
with the exact center normalization and c fixed, by adding a compact
strain compensator. No weighted uncertainty neighborhood is excluded.
All decisive endpoints remain open.
