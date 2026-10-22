# Observed angular bands and the limits of a cutoff comparison

Written 2026-10-21 before this topic's arithmetic. Dimensions below are positive integers. This is a result about finite saved arrays and finite quadratic forms.

## Statement and notation

Use the four exact row energies E_R of topic154, with n>=2 nodes t_i strictly increasing, positive weights w_i, angular indices0<=N<40 and a real image f_iN. For a subset S of angular indices, let E_R(S) be the same sums restricted to N in S, including both nodal and edge terms. If E_R({0,...,39})>0, define the observed high-band fraction

 b_R=E_R({32,...,39})/E_R({0,...,39}).

Then 0<=b_R<=1 and E_R({0,...,31})=(1-b_R)E_R({0,...,39}). For any fixed positive denominator g, the ratio of the corresponding cutoff32 and cutoff40 quotients on THIS SAME image is sqrt(1-b_R). The denominator cancels. No coefficient with N>=40 occurs in this statement.

Separately let G be a positive definite quadratic form on a nonzero finite dimensional real vector space, and A,B nonnegative quadratic forms on that same space. Let alpha^2=min_(G(x)=1) A(x) and beta^2=min_(G(x)=1)(A(x)+B(x)). These minima exist, beta>=alpha, and every minimizer y of A+B with G(y)=1 satisfies B(y)<=beta^2-alpha^2. Closeness of alpha and beta does not bound B on a minimizer of A. In particular for G=I, A=diag(1,1+delta), B=diag(K^2,0), with 0<delta<K^2, alpha=1 with unique minimizing line span(e1), beta=sqrt(1+delta) with unique minimizing line span(e2), but B(e1)=K^2. Arbitrarily large K and arbitrarily small positive delta are possible together.

## Complete proof

All nodal and edge summands in each E_R are nonnegative. Splitting their finite angular index set into0..31 and32..39 proves additivity, positivity and the fraction bounds. Taking the increasing square root after division by g proves the same-image quotient ratio. The trapezoid identity sum_i omega_i v_i=sum_i Delta_i(v_i+v_(i+1))/2, proved by collecting each interior node's two coefficients, supplies an independent edge evaluation of both quadrature energies. No quadrature limit is invoked.

The G-unit sphere is compact: positive definiteness gives a positive smallest eigenvalue after choosing Euclidean coordinates, hence the sphere is closed and bounded. Both quadratic forms are continuous, so their minima are attained. For each G-unit vector x, A(x)+B(x)>=A(x)>=alpha^2. Minimize the left side to obtain beta^2>=alpha^2. For a minimizing y, beta^2=A(y)+B(y)>=alpha^2+B(y). This proves the high-cutoff minimizer bound. In the two-dimensional example, the eigenvalues of A are1 and1+delta, and those of A+B are1+K^2 and1+delta. Their strict orderings give the two distinct unique minimizing lines and all claimed values.

Thus exact close minima WOULD bound the observed added energy on an exact high-cutoff minimizer, provided the same space, same G and exact additive form identity have been proved. Saved floating singular-value summaries do not establish those hypotheses or certified minima. The example forbids transferring that conclusion to a low-cutoff minimizing vector. Arbitrary extra nonnegative angular energy beyond the largest observed cutoff is compatible with all four finite arrays and all finite statements above.

## Fixed source selection and independent computation

Before arithmetic, select index0 of the M24/s16/o40 ppc4 NJ1 Fminus saved images from rowsL2q and rowsH1q, already frozen in topic154. Compute all four total and high-band energies and their fractions. A new Arb nodal sum reads the exact JSON exported in topic154. A separate mpmath.iv computation manually decodes every selected original IEEE754 binary64 scalar, checks the exact JSON, uses reverse angular and radial summation and the trapezoid edge identity. All16 energy pairs and8 fraction pairs must overlap. Literal data only, no continuous weight, operator image, denominator norm or admissibility claim.

Freeze the three numerics H1q summaries M24/s16/o32, M24/s16/o40 and M24/s8/o32. Export their five smallest reported Fminus numbers as exact binary64 rationals. Compute every relative change |a-b|/|b| exactly with Fraction and independently with fmpq and manual binary decoding. Check the stated metadata but do not treat matching labels as proof of identical assembled spaces or forms. The exact saved changes are observations. Any printed decimal window is rounded outward by integer arithmetic.

## Dependencies and scope

Topic154 supplies the definitions, exact finite arrays and immutable source snapshots; all selected binary imports are checked again here. This topic supplies no full singular spectrum, matrix verification, continuous norm, convergence theorem, bound on unobserved modes, inverse estimate or IPM endpoint. A nonzero saved change refutes only a literal claim that those saved numbers are equal. It does not by itself prove or refute mathematical convergence of an underlying method.
