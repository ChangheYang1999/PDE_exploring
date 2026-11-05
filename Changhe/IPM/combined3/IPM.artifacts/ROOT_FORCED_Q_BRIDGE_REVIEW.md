# Independent review of the forced Q-evolution bridge

Reviewed: operator_theory/Q_FORCED_EVOLUTION_BRIDGE_v02.md, together with the actual L2-generator/domain construction already reviewed in this campaign. Verdict: the analytic implication is valid. Its numerical exterior-energy, forcing and contraction inputs must still be assembled from complete certificates.

The equivalence of Q and the coordinate Sobolev space follows from the exact coordinate commutator, without a quantitative conversion loss in the self-map argument. For a smooth frozen input, the complete smooth flow preserves compactly supported smooth functions and gives finite-time weighted H²/H³ bounds. Composition and multiplication interpolate to H^2.1. The bounded derivatives of the actual background and its at-most-linear drift suffice; a uniform high-norm decay rate is not assumed.

The joint weighted velocity bound applies after Jq because Jq preserves central oddness. The smooth bounded source coefficient multiplies the coordinate Hq space boundedly. Therefore the bounded-perturbation construction on Q is legitimate. Its Dyson expansion agrees in L2 with the actual transport/source semigroup, by uniqueness and the continuous embedding Q into L2.

The transport core argument is precise: for a compactly supported smooth input, a time-truncated resolvent integral is smooth and has compact support, since the union of finite-time inverse flow images of a compact set is compact. The terminal orbit gives an exponentially vanishing graph error for resolvent parameter above the Q growth rate. Density of those inputs makes this a core. Adding the bounded source preserves its domain and core.

For F in Q, the finite-time semigroup integral g(t)=integral_0^t exp(sA)F ds belongs to the Q-generator domain and is C1 as a Q-valued function; it solves g'=Ag+F. Its limit is -A^-1F, with the correct sign. The L2 radius is strict at every finite positive time. On any interval Q(g)>M, graph-core approximation consequently preserves the two strict test inequalities eventually. The exterior energy estimate passes to that trajectory. The polynomial b z²-n z-C R² is strictly positive for z>M whenever b M²>=nM+C R². Continuity excludes crossing the boundary even if the displayed scalar inequality is non-strict.

Weak compactness of the bounded weighted derivatives and strong L2 convergence identify the actual stationary inverse in Q. This is a direct barrier proof and does not assume that the high stationary inverse exists before applying the energy inequality.

Smooth in-ball S1 approximants exist by approximation of Jqk in weighted L2, radial Bessel inversion and simultaneous rescaling of both radii. The full ball has no origin-strain constraint. Q convergence implies convergence in Hq and therefore in the velocity C1 norm. The maximal L2-domain characterization and the difference equation identify the rough-input inverse; the uniform Q radius passes by weak compactness.

The ball is complete in the L2 metric by closedness of the weighted derivative in distributions. The contraction uses the vector L2 norm of U, bounded by one, and the explicit Fourier gradient embedding. It does not infer an operator norm from a finite matrix.

Finally, normalization is derived at the fixed point. S1 and C1 regularity allow the first-order stationary expansion on the y axis, without requiring a second derivative of the density at the origin. The exact normalized background gives ell(k)(rho*_y(0)+k_y(0))=0. The total slope is positive on the stated radius, so ell(k)=0 follows. It was not required of the frozen iterates.

This removes the old N-norm Garding, high matrix-margin, compactness, exterior lifting, and graph-witness premises from this particular bridge. It does not remove the need for a fully verified exterior Q energy inequality or the actual L2, source and scalar inputs.
