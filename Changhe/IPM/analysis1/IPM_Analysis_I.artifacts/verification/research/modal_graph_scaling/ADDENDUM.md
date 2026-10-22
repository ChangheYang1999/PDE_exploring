# Precise domain and completed input checks

2026-10-21. Read with PROOF.md. This resolves the definition and finite-input conditions raised by the first actual Opus5.5 review.

The real linear domain D is exactly the set of real functions h satisfying all of the following clauses:

1. h is even in x and odd in y, and h belongs to C^{2,alpha}_loc for some 0<alpha<1.
2. On some disk about0, h=x^2 y b, with b continuous and even in both coordinates. Set J(h)=b(0). The radius and exponent may depend on h.
3. There exist gamma<1 and C<infinity such that |h(X)|+(1+|X|)|grad h(X)|<=C(1+|X|)^gamma for all X.
4. The canonical velocity U[h] is C1 locally, has the specified velocity parity, div U[h]=0 and curl U[h]=-partial_x h in distributions, and U[h](X)=o(|X|) at infinity. These conditions determine it uniquely by the harmonic Liouville argument in trial_regularities. The central strain is the finite real number Sigma(h)=-partial_x U[h]_1(0), equivalently psi[h]_xy(0) for the canonical stream.
5. h and the full linearized expression Lh in PROOF.md belong to the weighted weak H1 space X.

Finite sums preserve all these clauses, using a smaller common disk and alpha and a larger growth exponent below1. Canonical uniqueness makes U and Sigma linear. The continuous factors make J linear. This is a linear domain with its graph norm; it is not asserted to be complete or closed. The definition is for this fixed modal background.

K satisfies clause1 by its local C^{3,alpha} regularity; clause2 by K=x^2 y(-2a-Ea) and the exact center estimates; clause3 with gamma=k by the displayed end bounds and compactness; clause4 by U-EU, the Poisson identity, the far derivative bounds and local regularity; and clause5 by the two explicitly integrable radial powers. The C5 compact bumps satisfy clauses1-3 directly, clause4 by their finite canonical Green modes and decay, and clause5 by graph_center_norm. Thus the membership claims are literal statements about this D.

The fixed-tail exclusion is linear: K is outside the perturbation subspace in which the coefficient of r^k vanishes, and outside the subspace satisfying h=o(r^k) uniformly in angle. It is not a statement that K is outside every affine class with some nonzero prescribed leading coefficient.

Both input decoders agree on k,L,bi,bo, all knot counts and the finite exponent inequalities. The knots have1558 simple spans and eightfold ends; the260 degree-seven spline modes have1565 coefficients each. Two independent parsers give a strictly positive exact rational enclosure of the normalization-defined A_00. The lower and upper rational endpoints are in evidence/compute.json and evidence/independent.json. This completes the nonzero-Theta premise; no floating midpoint replaces the normalization-defined real coefficient.

The general far proof permits decaying resonances. As an additional check, the exact actual exponents have no resonance at either sign of any stream frequency2,4,...,522: all5742 comparisons are nonzero. This check is finite and pertains to these inputs; the general regularity argument does not require its conclusion. All inherited scalar, center and graph-theorem source/evidence pins are verified by the independent checker.

The coarser bounds U[K]=O(r) and LK=O(r^3) in PROOF.md are retained as sufficient upper bounds. U[K]=O(r^2) follows from C2 regularity, but no sharper bound is needed for the membership conclusion. NONZERO_IMAGE.md supplies a separate leading-term argument for the actual image, with its additional inherited center expansion and explicit derivative-remainder assumptions.
