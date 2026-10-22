# Topic149. Angular projection nesting and a reported fraction

Written before the independent field evaluation, 2026-10-21. This result concerns angular Hilbert-space geometry and the interpretation of specific floating artifacts. It does not certify a singular value, an infinite-dimensional inverse, or physical weak-H1 membership of the encoded columns.

Let t=log r, let w(t)>0 be a measurable radial weight, and consider real fields h=r^3 sum_N C_N(t) sin((2N+1)theta) with the finite energy

E(h)=pi integral w(t) sum_N [(1+(2N+1)^2)C_N(t)^2+(3C_N(t)+C_N'(t))^2] dt.

The coefficients and their derivatives can either define genuine functions in this Hilbert space or piecewise jets in the direct sum of the corresponding piecewise energy spaces. In the latter case E is a broken energy and makes no assertion about distributional jumps. The same argument applies to any positive finite quadrature of these jets, after quotienting the nullspace. The IPM source weight is w=L^6 exp(2t)(1+exp(2t)/L^2)^(3/2-k), with L>0. The constants k and L do not affect the angular decomposition.

Let Q select N=0,1 and annihilate the other sine harmonics. Let S be any closed subspace consisting of fields b(t)Phi_0(theta)r^3, where Phi_0=cos(theta)^2 sin(theta)=(sin(theta)+sin(3theta))/4. Then S is a subspace of the range of Q. If P_S denotes the orthogonal projection onto S, every nonzero h satisfies

0 <= E(P_S h)/E(h) <= E(Qh)/E(h) <= 1.

Proof. Orthogonality of the sine functions gives integral sin(qtheta)sin(ptheta) dtheta=pi delta_(pq). Their derivatives are orthogonal cosines with squared norm pi q^2. Radial differentiation does not mix harmonics. Thus the displayed energy is an orthogonal sum over N, and Q is its orthogonal projection onto N=0,1. The trigonometric formula for Phi_0 shows S is contained in this range. Consequently h-Qh is orthogonal to S, so P_S h=P_S Qh. Orthogonal projection is a contraction: Qh=P_S Qh+(I-P_S)Qh is an orthogonal sum, hence E(P_S h)<=E(Qh). Dividing by E(h)>0 proves all inequalities. The same computation is pointwise in the radial variable, so positive quadrature and piecewise integration preserve it. A finite collection of radial columns has a finite-dimensional, hence closed, image after quotienting null vectors. This proves the claim in that case also.

For independently evaluating the angular modes, product-to-sum gives

Phi_m=(sin((1+2m)theta)+sin((1-2m)theta)+sin((3+2m)theta)+sin((3-2m)theta))/8.

A negative sine frequency contributes with a negative sign to the corresponding positive odd frequency. Repeated frequencies add. This gives an exact rational, sparse transformation without numerical angular quadrature. The coefficients are used with direct piecewise evaluation of the saved original-coordinate vector and its radial derivative. A separate angular sampling calculation can check the energy identity numerically, but is not its proof.

The independently evaluated radial integral will use finite Gauss-Legendre rules and a finite radial interval. Results from it are floating consistency evidence only, with neither rigorous rounding enclosures nor a bound for the omitted infinite intervals. Exact comparisons of decimal or dyadic scalars stored in source JSON certify only what the saved artifacts say. Such comparisons must not be promoted to physical energy inequalities without certified integration and an admissible function space.

The text claim to audit is NUM_REPORT section7.4b's smallest M24/s8 H1-row direction, said to have an m=0 squared projection about0.86 but a frequency1,3 fraction about0.81. Compare the same saved vector, section, H1m norm and row mode. The analogous H1q-row direction is a different vector. No value from one row mode may be transferred to the other. A report correction is accepted only if the source artifacts and a fresh independent field evaluation agree on which value belongs to which vector.
