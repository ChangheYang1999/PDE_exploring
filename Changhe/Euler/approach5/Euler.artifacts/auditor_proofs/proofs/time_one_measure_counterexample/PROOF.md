# A time-one entropy-formula measure need not be physical

## Exact statement

There is a smooth nonsingular volume-preserving flow on a compact smooth three-manifold and a family of ergodic invariant probabilities for its time-one map such that each probability has Lyapunov exponents {log(lambda),0,-log(lambda)}, satisfies the entropy formula and has absolutely continuous unstable conditional probabilities, but its statistical basin has zero ambient volume. Here lambda=(3+sqrt(5))/2. None of these probabilities is invariant under the whole flow.

This confirms LIT16. It is a counterexample to an abstract inference, not an Euler profile or a construction in R^3.

## Construction and proof

Let A=[[2,1],[1,1]] act on the torus T^2, and form the smooth mapping torus

    M=(T^2 x R)/((x,s+1) equivalent to (Ax,s)).

The flow Phi_t[x,s]=[x,s+t] is smooth and has no zero. Since det A=1, ordinary product volume in these charts gives a smooth invariant volume on M. The smooth phase map pi([x,s])=s modulo one is well-defined. The time-one map f sends [x,s] to [Ax,s]. Let mu_theta be normalized torus area on the fiber pi=theta.

The measure mu_theta is f-invariant and ergodic. To check the latter directly, an invariant square-integrable function on the torus has Fourier coefficients constant on each orbit of A transpose on Z^2. Every nonzero lattice orbit is infinite: otherwise a positive power of A transpose fixes a nonzero vector, although its eigenvalues are lambda^n and lambda^(-n), neither equal to one. Square summability forces all nonconstant Fourier coefficients to vanish. Applying this to indicators proves ergodicity.

On a fixed phase fiber, the derivative in the two horizontal eigendirections has rates log(lambda) and -log(lambda); the flow direction has rate zero. Smooth metrics on compact M are uniformly comparable, so these rates are intrinsic. Unstable leaves are horizontal straight eigenlines in local charts. Disintegration of torus area along them gives one-dimensional length conditional probabilities, up to positive smooth densities and normalizing constants. Ledrappier-Young Part I, Theorem A, therefore gives h_mu_theta(f)=log(lambda). Its hypotheses allow the zero center exponent and do not require a positive-volume statistical basin.

If the empirical probabilities of an f-orbit converge to mu_theta, their integrals against cos(2*pi*pi(z)) and sin(2*pi*pi(z)) converge to the corresponding values at theta. Both functions are constant along an f-orbit. Therefore its phase is theta. The statistical basin is contained in the two-dimensional fiber pi=theta, which has zero smooth three-dimensional volume. Finally (Phi_t)_*mu_theta=mu_(theta+t), so mu_theta is not invariant under the entire flow.

## Dependencies and scope

The only substantive entropy theorem is Ledrappier and Young, Annals of Mathematics 122 (1985), Part I, Theorem A, printed page 513. The actual manuscript was read and its theorem page visually checked. Source: in the team records. Our rendered page is in the team records when read from this proof's directory.

The example does not rule out positive-volume continuous-time basins after flow averaging. It only prevents replacing that separate argument by the entropy formula for a merely time-one invariant probability. It does not reproduce the unequal Euler exponents or claim any target counterexample.
