# Maximal entropy measures: the exact conditional conclusion

## Statement

Let 0<c<1/2, omega be finite, U in C^infinity(R^3;R^3), and P in C^1(R^3) solve

    (1-c)U + B dot grad U + omega J U + grad P = 0,
    div U=0, B=(cI-omega J)y+U, U=o(|y|) uniformly.

Assume U is nonconstant. Put a=1-2c, b=1+c, Omega=curl U. Let Phi_t be the complete B-flow and Lambda its compact set of bounded forward orbits. There is a probability nu on Lambda which is ergodic under the entire flow and maximizes the entropy of F=Phi_-1:

    h_nu(F)=h_top(F|Lambda)>=a.

It gives zero mass to {B=0}. Either nu({Omega=0})=1, or nu({Omega=0})=0. In the latter case its backward spectrum is exactly {a,0,-b}, h_top(F|Lambda)=a, and its conditional probabilities on unstable manifolds are absolutely continuous. This is the unstable-conditional meaning of SRB. No positive-volume basin or elimination of the irrotational alternative is asserted.

This confirms LIT17 with its exact hypotheses. Smoothness is an additional hypothesis beyond the target C^2 class.

## Dependencies

A055 supplies a smooth compactification to S^3 and h_top(F|Lambda)>=a. All invariant probabilities for the compactified map are supported on Lambda together with the fixed point at infinity, so its entropy is the same. A037 supplies the exact spectrum on compact flow-ergodic measures for which B and Omega are nonzero almost everywhere.

The external inputs are the variational principle, affinity of metric entropy on invariant probabilities, upper semicontinuity for a fixed smooth compact-manifold map, the compact-convex extreme-point theorem, the characterization of ergodicity by extremality, Ruelle's inequality, and Ledrappier-Young Theorem A. The precise smooth upper-semicontinuity assertion is printed as Theorem 1.1 in Buzzi's actual 2009 research manuscript, arXiv:0902.2624, page 1. This audit does not claim to have read the original Newhouse 1989 manuscript or its correction. The actual Ledrappier-Young theorem allows zero exponents and an arbitrary invariant Borel probability.

## Existence and full-flow ergodicity

Use the smooth compactification from A055. Its derivative is bounded on the compact manifold, so its entropy is finite by the elementary finite-dimensional Lipschitz entropy bound. Let h=h_top(F|Lambda). The F-invariant probabilities supported on Lambda form a nonempty weakly compact set. The variational principle and upper semicontinuity give a maximizing probability mu.

For every real t, mu_t=(Phi_t)_*mu is F-invariant and has entropy h, since Phi_t commutes with F and is an invertible measure-system conjugacy. Finite convex averages of the mu_t have entropy h by affinity. Weakly continuous dependence on t makes their Riemann sums converge to

    mu_bar=integral_0^1 mu_t dt.

Upper semicontinuity gives h_mu_bar(F)>=h; the definition of h gives equality. Since mu is Phi_1-invariant, mu_t is one-periodic as a measure-valued function. Shifting its integration interval proves that mu_bar is invariant under the whole flow.

Consider the set of all flow-invariant probabilities on Lambda with entropy h. It is nonempty, compact by upper semicontinuity, and convex by affinity. It is a face of the compact convex set of all flow-invariant probabilities: if a nontrivial convex combination has entropy h, the two individual entropies are at most h and affinity forces both to be h. An extreme point nu of this face is consequently extreme in the full flow-invariant set. Thus nu is flow-ergodic. This argument never assumes that a time-one ergodic measure is flow-invariant.

## Support and exact entropy in the vortical case

The sets {B=0} and {Omega=0} are invariant under the entire flow. Flow ergodicity makes their nu-masses zero or one. If nu({B=0})=1, F is the identity almost everywhere and h_nu(F)=0, contrary to h>=a>0. Hence B is nonzero almost everywhere.

If Omega is nonzero almost everywhere, A037 applies. Its recurrence proof uses the time-one map only for recurrence and the multiplicative ergodic theorem; it does not assume time-one ergodicity. In brief, recurrence to sets on which the transported vectors B and Omega are bounded below, together with

    D Phi_n B = B composed with Phi_n,
    D Phi_n Omega = exp(b*n) Omega composed with Phi_n,

forces exponents zero and b for these two nonzero vectors. They are independent because their exponents differ. The determinant exp(3c*n) supplies the third exponent 3c-b=-a. Reversing time gives {a,0,-b}.

Ruelle's inequality now gives h_nu(F)<=a. Together with h_nu(F)=h>=a this proves equality. Ledrappier-Young Part I, Theorem A, applies to the smooth diffeomorphism of compact S^3 and nu. The entropy formula is exactly saturated, so the unstable conditional probabilities are absolutely continuous.

If Omega vanishes almost everywhere, this exponent computation does not apply. Nothing in maximal entropy existence excludes that alternative. Positive metric entropy excludes measures on the stationary set, not measures on all vorticity zeros.

## Limits of the result

The theorem proves neither that the profile is zero nor that an entropy-maximizing measure sees nonzero vorticity. It does not establish a statistical basin statement. LIT16, independently audited in A064, shows why a merely time-one entropy-formula argument would not suffice for that assertion. A continuous-time physicality theorem needs its own flow, Pesin-block and absolute-continuity argument.
