# Quantitative return growth before a distant vortex escape

## Statement

Let U in C2(R3;R3), P in C1(R3), with U bounded, satisfy the full rotating Euler profile equation, div U=0, 0<c<1/2 and arbitrary finite omega. Write a=1-2c, B=(cI-omega J)y+U, Omega=curl U. Let Phi_t and psi_tau be the complete B and Omega flows. Choose R1>2||U||_infinity/c and set D_t=Phi_t(B_R1).

Let Sigma be a compact embedded C1 disk with Omega.n_Sigma>0 including its boundary. For a point x in Sigma whose forward vortex orbit is unbounded, let N_t(x) be the number of further crossings of Sigma before that orbit first reaches boundary(D_t), for all t large enough that Sigma is contained in D_t. Then for flux-almost every such x,

    liminf_(t->infinity) log(1+N_t(x))/t >= 1-2c.       (1)

The same assertion holds for backward vortex time. Flux measure and surface area are equivalent here. If N_R^ball counts crossings before first reaching the Euclidean sphere of radius R, then

    liminf_(R->infinity) log(1+N_R^ball(x))/log R
       >= (1-2c)/c = 1/c-2.                           (2)

No assertion about a bounded vortex half-orbit is included.

## Proof

A151 gives, with mu=(Omega.n_Sigma)dS and F0=int_boundary(D_0)|Omega.n|dS,

    mu{x in Sigma: first boundary hit exists and N_t(x)<=k}
       <= (k+1)F0 exp(-at).                           (3)

This estimate includes all finite first hits. Its proof and the treatment of tangencies are in the team records. Uniform transversality of the compact disk gives a positive lower time between successive crossings. Thus the number before any finite first-hit time is finite. Crossings of its boundary can be included; the flow saturation of that one-dimensional boundary has zero volume and zero transverse flux on any transverse disk, so either convention agrees almost everywhere.

Fix 0<epsilon<a and k_n=floor(exp((a-epsilon)n)). The sum over sufficiently large integers n of the right side of (3) is finite, bounded by a constant times sum exp(-epsilon n). The first Borel-Cantelli lemma therefore shows that, for mu-almost every x, only finitely many of the events in (3) with t=n and k=k_n occur. An unbounded forward orbit eventually exits every bounded D_n, so for almost every such x,

    N_n(x)>k_n

for all sufficiently large n. The domains D_t are increasing with t; consequently their first exit times and the crossing counts N_t are nondecreasing. For n<=t<n+1,

    log(1+N_t(x))/t >= log(1+N_n(x))/(n+1).

Taking a lower limit and then a countable sequence epsilon decreasing to zero proves (1). The exceptional set is measurable: unboundedness can be expressed using integer radii and rational times, and successive transverse hitting times are measurable. Applying the same argument to -Omega proves the backward version.

The radial carrier bound gives D_t contained in B_(C exp(ct)) for one fixed C and t>=0. For large R choose t=c^-1 log(R/C). A vortex orbit must leave D_t before reaching the sphere of radius R, so N_R^ball>=N_t. Since t/log R tends to 1/c, (1) gives (2).

## Scope

This is a direct quantitative consequence of the C18/A151 flux estimate, using only Borel-Cantelli and monotonicity. It establishes no contradiction with the complete conservative vortex flow and no automatic unboundedness of its half-orbits. It does not require a pressure limit, an asymptotic expansion, a regular attractor, or any symmetry. The consequence was sent to the model integral-estimates agent for a cross-check; that response is separate from this proof.

Audit written: 2026-11-02T20:42:34Z
