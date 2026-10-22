# Projection energy and distance in the saved finite-section experiment

Written 2026-10-21T20:08:38.557454+00:00 before the new artifact audit.

## Exact statement and notation

Let H be a real or complex Hilbert space, K a nonzero vector, S a closed subspace, and P the H-orthogonal projection onto S. Put eta=||PK||^2/||K||^2. Then 0<=eta<=1 and ||K-PK||/||K||=sqrt(1-eta). Capturing exactly99.5percent of the squared norm means a relative norm distance sqrt(0.005), between7.07and7.08percent. It does not mean0.5percent distance. A claimed eta>1 cannot be the exact energy ratio of an orthogonal projection in one consistently defined Hilbert norm.

The additional finite artifact statement is that the exact dyadic values in the frozen version2 Kproj2 NPZ files yield relative distance diagnostics about1.81765percent(NJ0),1.81777percent(NJ1),1.76199percent(free,NJ1) at the stated threshold. These will be recomputed from stored PK_norm2 and K2_gram, not merely copied from dist_rel or cos2_full. The old files contain inconsistent full-energy ratios above1; their lower-mode ratios cannot be substituted for a full-K distance. This audit does not validate any Gram, cross block, quadrature, whole-plane tail, exact projection, or image under the IPM linearized operator.

## Proof

Orthogonality gives inner_product(K-PK,PK)=0. Expanding the squared norm of K=(K-PK)+PK gives ||K||^2=||K-PK||^2+||PK||^2. Both terms are nonnegative; divide by ||K||^2>0 and take the nonnegative square root. The stated7.07to7.08percent interval follows by squaring: (707/10000)^2<1/200<(708/10000)^2. For0.5percent distance the corresponding missing energy is(1/200)^2=1/40000, so one needs eta=0.999975, which differs from0.995.

The scalar artifact computations will use exact binary64 interpretation of stored positive energies. Their difference must be strictly positive before a square root is permitted. Clipping a negative energy difference to zero cannot establish a distance. An independent manual NPY scalar decoder and exact integer ratios will check the NumPy import. Arb and mpmath.iv will each enclose the square roots and compare the stated rounded intervals. This validates arithmetic of saved numbers only.

The frozen current c2_Kproj.py first stage now computes all260 modes of K and includes the KP and TAU columns. Its second stage still reads cos2_low from the projection NPZ, although the version2 first stage saves no such member. That schema mismatch will be checked on the actual frozen source AST and actual version2 member lists. The older KprojB JSON files name older projection files and are not images of the revised version2 projections. No speculative physical conclusion is drawn from those older rows.

## Dependencies and scope

All source files are read-only snapshots of the numerics lane at the recorded time. They are floating experiment artifacts. The Pythagorean theorem above is exact; the existence and accuracy of a physical orthogonal projection represented by these files remain OPEN. Different quadratures or mode subsets cannot be mixed to infer a distance. Even a small H distance provides no graph-norm bound for an unbounded operator without an additional estimate. The residual, inverse, X3 neighbourhood and every decisive IPM endpoint remain OPEN.
