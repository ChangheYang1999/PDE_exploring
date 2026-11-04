# Conditional singular hyperbolicity and its measure consequences

## Exact hypotheses and statements

Let U in C2(R3;R3) solve the rotating Euler profile equation with div U=0. Put

    B=(cI-omega J)y+U, Omega=curl U,
    b=1+c, a=1-2c, 0<c<1/2,

with arbitrary finite omega. Let K be a compact full invariant set for B on which Omega never vanishes. Assume every zero p of B in K is hyperbolic. The derivative DB(p) has the eigenvalue b along Omega(p). Write nu(p) for the largest real part of its other two eigenvalues, counting multiplicity, and assume

    nu(p)<b at every such zero.                           (H)

Then the backward flow Psi_t=Phi_-t has a continuous dominated invariant splitting

    T_K R3=E^s direct-sum E^cu, E^s=R Omega, dim E^cu=2.

The first bundle contracts uniformly, the second expands area uniformly at rate a up to bounded factors, and B belongs to E^cu at regular points. If K contains a singularity, this is singular hyperbolicity in the usual one-dimensional stable-bundle sense. If it has no singularity, A056 gives the stronger nonsingular hyperbolic splitting.

This statement does not require K to be an attractor and does not make it one. Assumption (H) is an extra spectral condition, not a consequence of the profile equation.

For the measure conclusions impose the further condition that K is a nontrivial transitive attracting set for Psi: there is a relatively compact forward-invariant neighborhood V with K the maximal full invariant subset of V, and K is the omega-limit of a regular orbit in K. Then K carries a unique physical full-flow-invariant probability mu, its continuous-time basin covers almost all of the topological basin, and supp mu=K. Its entropy for Psi_1 is exactly a. In fact h_top(Psi_1|K)=a and mu is the unique full-flow-invariant measure of maximal entropy. No uniqueness among probabilities invariant only under Psi_1 is asserted.

## Uniform domination from the exact cocycle

The Cauchy identity gives

    D Psi_t Omega(x)=exp(-bt) Omega(Psi_t x).

Since Omega has positive lower and finite upper bounds on K, E^s contracts at rate b with bounded prefactors. Let Q_t be the induced cocycle on the two-dimensional quotient V=T_K R3/E^s. Its determinant has growth rate a with bounded prefactors, since det D Psi_t=exp(-3ct) and b-3c=a. Equivalently the nonvanishing quotient area form i_Omega vol is multiplied exactly by exp(at).

We show the domination estimate

    ||D Psi_t|E^s|| ||Q_t^{-1}|| <= C exp(-eta t), t>=0.  (1)

On the dual quotient consider the forward cocycle

    L_t=exp(-bt)(Q_t^{-1})^*.

For any full-flow-ergodic probability on K which gives no mass to the zeros of B, A037 gives the backward tangent exponents -b,0,a, and the quotient exponents 0,a. Thus the largest exponent of L is -b. A flow-ergodic probability supported on zeros is a point mass at one zero p. There the largest exponent of L is nu(p)-b. There are only finitely many zeros in K: an infinite sequence of zeros would accumulate at a zero in K, contrary to its hyperbolicity and local isolation. Consequently all these largest exponents are at most -delta for one common delta>0.

For clarity, a uniform estimate follows without presupposing a dominated splitting. If ||L_t|| failed to decay at least as exp(-delta t/2) for arbitrarily large t, choose long maximizing segments on the normalized unit dual-quotient bundle. This is a compact bundle carrying the continuous normalized L flow. Its logarithmic norm derivative is a bounded continuous observable. Empirical probabilities along the chosen segments have a full-flow-invariant weak limit with mean logarithmic growth at least -delta/2. An ergodic component with at least that mean projects to a flow-ergodic probability on K. Oseledets' theorem bounds its vector growth above by that base probability's largest L exponent, at most -delta, a contradiction. Hence ||L_t||<=C exp(-delta t/2). The bounded ratio of |Omega(Psi_t x)| to |Omega(x)| proves (1).

Choose any continuous complement F of E^s and write the time-T derivative in block form

    [[A_x,C_x],[0,Q_T(x)]].

Take T so large that the bound in (1) is below one. A complement which is the graph of a linear map H_x:F_x -> E^s_x transforms according to

    H_(Psi_T x)=(A_x H_x+C_x)Q_T(x)^(-1).

This is a contraction on continuous graph sections in the uniform norm. Its unique fixed point supplies the continuous invariant complement E^cu. Uniqueness also gives invariance under every flow time: transporting the graph by a fixed time produces another time-T-invariant graph. Estimate (1) is precisely domination for this splitting, up to the bounded graph identifications.

The stable projection of B is zero. Otherwise, following it backward in Psi time would make its nonzero stable component grow like exp(bt), while B and the projections remain bounded on the compact full invariant set. Thus the flow direction belongs to E^cu. The quotient area formula and the bounded graph identifications give uniform E^cu area expansion with rate a. This proves the splitting claim, including at the singularities.

## Actual source and the additional attractor hypothesis

The actual source checked is Araujo, Pacifico, Pujals and Viana, Singular-hyperbolic attractors are chaotic, arXiv:math/0511352v3. The PDF and hash record are in the team records. Printed pages 3-7 were read, including Definitions 1.1-1.3, Theorems B and C, and Corollary 2. This is a check of the statements and their application, not an independent reconstruction of the entire source proof.

Definition 1.1 explicitly defines an attractor as a TRANSITIVE attracting set. Theorem B, at C2 regularity as specified immediately before it, supplies a unique ergodic hyperbolic physical probability with a basin of full volume in the topological basin. Theorem C supplies full support and absolute continuity along center-unstable surfaces. Corollary 2 gives the entropy formula. These statements require an attractor in that defined sense, not merely an arbitrary transitive compact set or a limit set occurring for a positive-volume collection of initial points.

The source uses a compact boundaryless three-manifold. This causes no local restriction here: preserve the vector field on a neighborhood of the compact trapping region and extend by a cutoff in a coordinate chart of S3. The set, its local trapping property and local physical basin remain unchanged. Flowing preimages of the local basin gives the claimed full-volume statement throughout the original topological basin.

The source definition of volume expansion on printed page 3 has an apparent sign error, writing a decaying exponential. We use the actual expanding estimate exp(at), as required throughout its arguments, and do not use that misprinted inequality to weaken the hypotheses.

## Entropy and uniqueness in the correct class

The source physical probability is regular and hyperbolic. A037 gives its backward exponents -b,0,a. Corollary 2 therefore gives h_mu(Psi_1)=a.

For every other full-flow-ergodic probability on K, either it is concentrated at a zero and has entropy zero, or it is regular and A037 plus Ruelle's inequality gives entropy at most a. The flow variational principle, or averaging time-one invariant probabilities over a unit of flow time, then gives h_top(Psi_1|K)<=a. Equality follows from mu.

If a full-flow-ergodic probability has entropy a, A094 makes it physical by its unstable absolute continuity and the smooth contracting Omega direction. The source uniqueness of the physical probability forces it to equal mu. An arbitrary full-flow-invariant maximizing probability has almost all of its ergodic components maximizing, since each component's entropy is at most a. Therefore it also equals mu. This argument deliberately retains full-flow invariance, avoiding the time-one ambiguity exhibited by A064.

## Claims that remain open

THEORY_B Section 11.2 does not derive transitive attraction for a general mixed alpha-limit set. A positive-volume basin of approach to a compact set is not the definition of an isolated attracting neighborhood. No claim here extracts such neighborhoods, proves a singular analogue of CO9's basin exhaustion, or handles failure of (H).

The source's paragraph after Theorem B attributes dense periodic orbits to Arroyo and Pujals, citing an IMPA 2004 preprint, not to Arroyo and Rodriguez Hertz as the agent draft says. That cited preprint was not obtained in this audit. No separate periodic-density verdict is based on that secondary citation. The source theorems used above do not require us to import it.

No contradiction with the profile equation follows from any of these conditional facts.
