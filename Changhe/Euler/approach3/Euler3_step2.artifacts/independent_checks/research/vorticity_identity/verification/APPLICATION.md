# Application conditions from the lead review

The implemented field is a finite sum over the fixed real homogeneous harmonics. Each radial twist rotates the cosine and sine pair; after this rotation its two coefficients are radial functions of q. The Cartesian formula is applied to these two terms separately, so the third radial derivative includes the twist derivatives. Main and damped correction envelopes are smooth at q=0 because R0 and R1 are positive. Homogeneous singular closure fields are not evaluated at the origin by this code.

The stable branch requires amplitude derivatives through order three to reconstruct its velocity Jacobian. Its fourth derivative is not supplied, so a stable velocity Hessian is explicitly unavailable. A second-order jet with a zero third entry is not used.

A small pressure-independent vorticity residual is only a necessary condition. Numerical divergence, pressure-Poisson consistency and the curl of the reconstructed pressure gradient are checked separately before attributing a mismatch with a momentum calculation.
