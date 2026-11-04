# Entropy-saturating empirical measures under a zero-entropy irrotational hypothesis

## Statement

Let U be a smooth divergence-free rotating Euler profile on R3, with uniform sublinear growth, 0<c<1/2 and any real omega. Set B=(cI-omega J)y+U, Omega=curl U, k=1-2c, kappa=1+c, d=3c, and Psi_t=Phi_{-t}. Let Lambda be a compact full-flow invariant core containing all backward limits. Assume every ergodic full-flow invariant probability on Lambda intersect Z, Z={Omega=0}, has zero entropy.

For Lebesgue-almost every x with Omega(x)!=0, some full-flow empirical limit nu of x has

    nu(Z union {B=0})=0,    h_nu(Psi_1)=k.

Its conditional measures on unstable manifolds are absolutely continuous relative to one-dimensional leaf length. The zero-entropy assumption holds for nonconstant real-analytic profiles by A089. It has not been established for all smooth profiles.

## Spectrum and entropy bound for all invariant probabilities

Let eta be a full-flow ergodic probability on Lambda. The sets Z and {B=0} are full-flow invariant. If eta is supported on {B=0}, the time-one map is the identity there, so its entropy is zero. If eta(Z)=1, its entropy is zero by hypothesis. In the remaining case B and Omega are both nonzero eta-almost everywhere.

The derivative cocycle has the identities

    D Psi_t B(y)=B(Psi_t y),
    D Psi_t Omega(y)=exp(-kappa t)Omega(Psi_t y).

At an Oseledets-regular recurrent point, boundedness of each field on Lambda gives upper rate at most zero for its values along the trajectory. Recurrence to a set where its norm is bounded below supplies an unbounded sequence with rate zero. Oseledets' theorem ensures the corresponding derivative-vector exponential limit exists. Therefore the vector exponents are 0 for B and -kappa for Omega. They are distinct, so the vectors are independent. The determinant exp(-dt) forces the remaining exponent to be kappa-d=k. This calculation holds eta-almost everywhere even if eta is not ergodic for the time-one map.

Ruelle's inequality gives h_eta(Psi_1)<=k in this case. Decomposition over full-flow ergodic probabilities therefore yields, for any full-flow invariant probability nu on Lambda,

    h_nu(Psi_1)<=k nu(Lambda minus (Z union {B=0})).

Entropy is harmonic for this invariant decomposition; alternatively one may disintegrate further into time-one ergodic measures, for which the same almost-everywhere spectrum computation applies.

## Selection and equality

A186 supplies, for almost every vortical x, a full-flow empirical limit nu on K(x) subset Lambda with h_nu(Psi_1)>=k. Combining the two bounds forces nu(Z union {B=0})=0 and h_nu(Psi_1)=k. Its positive Lyapunov exponent is k almost everywhere, so it satisfies Pesin's entropy equality.

Cut off B outside a neighborhood of Lambda and extend smoothly to S3. This preserves the measure, derivative cocycle and entropy on Lambda. Ledrappier-Young, The metric entropy of diffeomorphisms, Part I, Theorem A, applies to this compact C2 time-one diffeomorphism. Its hypotheses do not require ergodicity or absence of zero exponents. Entropy equality is equivalent to absolute continuity of conditional measures along unstable manifolds. The source was independently read in the literature agent and checked in A065/A089; its retained original is in the team records.

## Scope

This verifies Section 5 of in the team records as A188. It asserts an empirical subsequence and unstable absolute continuity. It does not assert unique empirical convergence of x or that x belongs to the basin of a particular ergodic physical measure. The support of nu can meet Z even though nu(Z)=0. Thus mixed limit sets touching Z are not excluded.
