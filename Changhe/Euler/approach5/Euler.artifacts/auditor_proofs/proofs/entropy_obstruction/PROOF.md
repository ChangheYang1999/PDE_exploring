# Circulation forces positive entropy for smooth nonconstant profiles

## Statement and hypotheses

Let 0<c<1/2 and omega be any finite real number. Let U in C^r(R^3;R^3), r an integer at least two, and P in C^2 solve

    (1-c)U + B dot grad U + omega J U + grad P = 0,
    div U = 0,  B=(cI-omega J)y+U,
    U(y)=o(|y|) uniformly as |y| tends to infinity.

Let Phi_s be the complete flow of B and let Lambda be the compact invariant set of points with bounded forward B orbit. If U is not constant, construct the compactified backward map F on S^3 as below. Then

    1-2c <= h_top(Phi_1 restricted to Lambda) + R(F)/r,
    R(F)=lim_n n^(-1) log max(1,sup ||D F^n||).

In particular, if U is C^infinity, then

    h_top(Phi_1 restricted to Lambda) >= 1-2c > 0.

Consequently, a C^infinity sublinear profile with zero entropy on Lambda is constant. If also U tends to zero, it is zero. No restriction on omega is used. For finite r, the R(F)/r loss must be retained; R(F) depends on the chosen compactification.

## Dependencies

The exact Kelvin law, completeness and backward trapping are independently proved in the foundation audit (A004, A006). Curl-free entire sublinear divergence-free fields are constant by harmonic Liouville. The only substantive entropy estimate used is Yomdin's volume-growth bound. It was checked against M. Gromov, *Entropy, homology and semialgebraic geometry*, Asterisque 145-146 (1987), expose 663, Theorem 2.2, printed pages 228-229, with proof in Sections 3.1-3.8. The actual source is retained by the literature agent as in the team records; its formula pages have been visually checked. This audit does not claim access to the unavailable original Yomdin 1987 journal manuscript.

We also use the variational principle for entropy of continuous maps on compact metric spaces and equality of forward and inverse entropy for a homeomorphism. No maximal-entropy measure is assumed to exist.

## 1. A loop with nonzero circulation

If curl U were zero everywhere, harmonic Liouville would make U constant. Choose a point with Omega=curl U nonzero and a sufficiently small smooth disk normal to Omega there. Its boundary gamma has nonzero circulation Gamma by Stokes and continuity of Omega. Kelvin's exact identity gives

    integral_(Phi_-t gamma) U dot dl = exp((1-2c)t) Gamma.

Choose a radius R0 with |U(y)|<=c|y|/2 for |y|>=R0, enlarging R0 if necessary. The closed ball K of radius R0 is invariant under the backward flow. Every compact set enters the interior of K after a uniform finite backward time: outside K, the radial derivative along backward time is at most -c|y|/2, while a strictly larger starting ball provides a uniform entry bound. Thus for some T, the embedded curve sigma=Phi_-T gamma lies in int K. All its subsequent backward images remain in K. Write M=sup_K|U|. Nonzero circulation implies M>0, and

    length_Euclidean(Phi_-n sigma)
       >= |Gamma| exp((1-2c)(T+n))/M.                 (1)

This is a length estimate for one fixed curve, not a claim inferred from the growth of a single derivative or Lyapunov exponent.

## 2. Compactification without changing the relevant dynamics

Choose R1>R0 and a smooth scalar cutoff chi with 0<=chi<=1, equal to one on the ball of radius R1 and zero outside the ball of radius 2R1. Set

    B'=(cI-omega J)y+chi(y)U(y).

For |y|>=R0 one has B' dot y >= c|y|^2/2. On K the fields agree. At large radius B'=Ay, A=cI-omega J. In the inversion chart z=y/|y|^2, the push-forward of Ay is

    A z - 2c z = -(cI+omega J)z.

Thus B' extends to a C^r vector field on the smooth one-point compactification S^3, and is linear in the infinity chart. Its flow exists for all times by compactness. Let F be its time-minus-one diffeomorphism. On K, F^n=Phi_-n for every nonnegative integer n. A smooth metric on S^3 and the Euclidean metric are uniformly comparable on K, so (1) gives the same exponential length rate for this metric.

The cutoff need not preserve divergence. The volume formula is not used for B' away from K.

## 3. All invariant probability mass is on Lambda or infinity

One has F(K) subset K. Every point of R^3 enters K under some F iterate, hence

    union_(n>=0) F^(-n)K = S^3 minus {infinity}.

Moreover,

    intersection_(n>=0) F^n K = Lambda.

To check the second identity, membership in every F^n K means that the entire forward orbit remains in K at integer times. Once a forward orbit leaves K, its radius increases strictly and it never returns. Hence it remains in K at all times. Conversely, a bounded full forward orbit cannot ever leave K, by the same radial inequality. The backward orbit is already trapped. The decreasing intersection is nonempty by compactness.

For any F-invariant probability nu, all the sets F^n K and F^-n K have mass nu(K). Continuity of measure along these nested sequences gives

    nu(Lambda)=nu(K)=1-nu({infinity}).

An ergodic invariant probability is therefore supported on Lambda or is the fixed-point mass at infinity. The variational principle, or ergodic decomposition followed by it, gives

    h_top(F)=h_top(F restricted to Lambda)
            =h_top(Phi_1 restricted to Lambda).      (2)

The last equality uses equality of the entropy of a homeomorphism and its inverse. No assertion about entropy outside a compact set is substituted for this compact argument.

## 4. Exact Yomdin input and conclusion

In Gromov's statement, for a compact C^r submanifold Y of dimension ell, the exponential growth of the volume of the graph of F^n restricted to Y is at most

    ent(F|Y)+(ell/r) log^+(Rad DF),
    Rad DF=limsup_n sup||DF^n||^(1/n).

The restricted entropy here is orbit complexity of initial points in Y; it is bounded by h_top(F). It does not require F(Y) subset Y. Projection of the graph to its second factor is 1-Lipschitz, so for a curve its graph length is at least the length of F^n(Y). For the embedded curve sigma and ell=1, this proves

    limsup_n n^(-1) log length(F^n sigma)
       <= h_top(F)+R(F)/r.

The sequence log max(1,sup||DF^n||) is subadditive, so the indicated limit exists. All quantities are finite on S^3. Combining with (1) and (2) proves the finite-r claim. For C^infinity data the same fixed F and sigma meet every integer r hypothesis, so r tends to infinity and removes the loss.

## Scope and excluded inferences

This confirms the core of coordinator CO3 and its zero-entropy conditional Liouville corollary. It does not prove that the entropy is zero, that the main conjecture holds, or that a maximal-entropy measure exists. It does not locate the support of a high-entropy measure inside {Omega!=0}. In particular, the exact Lyapunov spectrum on vortical nonstationary measures does not automatically bound all invariant measures.

The original curve must be moved inside the unchanged trapping region before the compactified map is used. This correction is incorporated above and in the coordinator's revised proof. The theorem is an obstruction for all finite omega, not an omega-independent bound on R(F) in finite regularity.

Audit recorded: 2026-11-02T18:51:05Z
