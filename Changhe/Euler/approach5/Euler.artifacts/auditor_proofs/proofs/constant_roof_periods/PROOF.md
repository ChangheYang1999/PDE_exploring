# Constant-roof periods and the missing return-count factor

## Statement

Let 0<c<1/2, a=1-2c, and let a C2 Euler profile with single-valued C1 pressure have a regular backward attractor with a global return section whose return time is the positive constant T. Suppose its quotient by stable vortex fibres is an expanding finite Markov graph map F, with the flux coordinate on each smooth branch. Then each branch has absolute slope

    lambda=exp(aT).

For every periodic orbit of F of least return count n whose fibre contracts to a periodic return point, the corresponding carrier orbit has period nT. Hence, if omega!=0,

    n log(lambda) >= 2 pi a/|omega|.                       (1)

At omega=0 no such orbit can occur for an Euler profile. In particular a fixed quotient point whose contracting fibre is invariant gives n=1. Without that premise, (1) must retain n.

For a fixed template, write n0 for its smallest realized return count. Its necessary rotation condition is

    |omega| >= 2 pi a/(n0 log(lambda)).                    (2)

Thus the denominator in the version without n0 is justified only when a period-T carrier orbit is known to exist.

## Proof of the flux and Euler statements

The exact one-form law on a vortex-saturated section is F*alpha=exp(aT)alpha. Choose flux coordinates in which alpha is the coordinate differential. Differentiation of the return map gives the displayed slope; with constant T each smooth coordinate branch is affine. A periodic quotient fibre whose return map is a contraction has a unique periodic point, and its least quotient return count is the number of section returns in that orbit. This is the precise lifting assumption used here; it is automatic in the usual compact stable-fibre realization of the Markov return model.

For any nonconstant carrier periodic orbit Y of period L, Euler's circulation identity gives

    integral_0^L |Y'|^2 + omega integral_0^L JY.Y'=0.

Subtract the mean of Y. Cauchy-Schwarz and periodic Wirtinger bound the absolute value of the second integral by L/(2pi) times the first. The first is positive, so omega cannot be zero and L>=2pi/|omega|. Setting L=nT proves (1) and (2). No decay assumption or global profile construction is needed for this local period restriction.

## Entropy and a precise bounded-complexity version

For completeness assume the Markov partition has m edges, each with positive finite flux length ell_i, and each edge image is a finite union of whole partition edges. Let M_ij count its traversals of edge j, including multiplicity. Length expansion gives

    M ell=lambda ell.

Since ell is strictly positive, the spectral radius of the nonnegative matrix M equals lambda. The symbolic coding of an expanding Markov graph map gives topological entropy log(lambda); the constant-roof suspension has entropy log(lambda)/T=a.

If the maximum row sum of M is at most S, then lambda<=S. A directed graph with m vertices and a cycle has a simple cycle of length at most m. If its cycles lift to periodic return points, n0<=m. Consequently (1) implies the precise estimate

    |omega| >= 2 pi a/(m log S),                           (3)

provided S>1. Thus a family with fixed c<1/2 and uniform bounds on m and S cannot satisfy the Euler period restriction as omega tends to zero. This is a valid meaning of bounded combinatorial complexity. A bound only on the number of named graph edges, with no multiplicity or branch bound, is insufficient for this argument.

## Refuted inference: the slope itself must diverge

The period restriction alone does not imply lambda tends to infinity as omega tends to zero, because n0 may grow. An explicit return-map example has n disjoint unit circles and

    F(i,z)=(i+1 modulo n,z^2), |z|=1.

Its derivative in arclength has constant positive magnitude 2. Every periodic point has return count divisible by n, and (i,1) has least return count exactly n. Its entropy is log2. Give the suspension the constant roof T=log2/a. Its minimum orbit period is n log2/a, so all its periodic orbits satisfy the necessary Euler period inequality when

    |omega| >= 2 pi a/(n log2).

For increasing n the slope remains 2 while the right side tends to zero. This is a counterexample to the inference from the period inequality, not a constructed Euler profile. Its Markov complexity grows, consistently with (3).

Similarly, a kinematic model with independent transported W is not required to obey Euler's U-circulation restriction, but it may happen to obey the numerical inequality for sufficiently large |omega|. The statement that the inequality does not hold in such a model must mean it is not forced by its equations, not that it fails at every parameter.

## Scope of the B25 audit

B25's main fixed-point inequality is correct with its explicit period-T premise, and the n-period qualification in its section2 is correct. The general fixed-template conclusion in section3(a) must carry n0 unless the template's fixed orbit is separately verified. The literal claim in section3(b) that the required slope tends to infinity is not implied; the bounded-complexity conclusion can instead use (3). The DA numerical threshold is conditional on a realized period-T orbit in that particular template; its quoted value 2pi/log((3+sqrt5)/2) is approximately6.53. No all-omega exclusion follows.

Dependencies are the already audited exact flux law and period bound in the team records. No numerical computation, formal build or new model construction was performed for this audit.
