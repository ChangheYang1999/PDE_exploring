# Independent review of the root's weighted-velocity and matrix lemmas

Reviewed files: `../WEIGHTED_ODD_VELOCITY.md` and `../FULL_MATRIX_CLOSURE.md`, read on 2026-11-04 during the combined3 campaign. Reviewer: operator-theory agent. The review checks the mathematical implications, not any uncomputed numerical input.

## Weighted velocity

Verdict: the displayed inequalities (1)--(5) and their stated scopes are correct.

For \(m=(\cos\theta\sin\theta,-\cos^2\theta)\), direct differentiation gives
\[
|m|^2=\cos^2\theta,\quad |m'|^2=1,\quad m\cdot m'=-\sin\theta\cos\theta.
\]
The cross term in \(|\partial_\theta(mF)|^2\) integrates to \(-\int(m\cdot m')'|F|^2\), including for complex F after taking real parts. Thus the remaining coefficient is \(1+\cos2\theta=2\cos^2\theta\), exactly as in identity (2). Central oddness removes every even angular mode, in particular mode zero, so the angular Poincare inequality used in (1) is valid. The near-origin product is H1 by that inequality; no point-supported derivative is left at the origin.

The adjoint estimate follows from \(|m'|=1\) and the vector version of the same angular Poincare inequality. The negative-weight estimates are exactly the Hilbert-space adjoints on the closed central-odd subspaces: \((W^{-1}UW)^*=WU^*W^{-1}\). All multiplications by W preserve those subspaces. For completion-space inputs, the extension must be understood as in the root note; the proof does not assert an unrestricted weighted Riesz theorem.

The source-form parities needed for application are also valid. A density in S1 is central odd, its gradient is central even, and \(G=J^q(Wg)\) is central odd for an S1 g. Therefore \((\nabla\rho_*)G\) is a central-odd vector, which may enter \(U^*\), while \(U[G]\cdot\nabla\rho_*\) is a central-odd scalar. Separating U into individual Riesz transforms would lose this justified scope.

## Full-matrix residual pairing

Verdict: the dual pairing and the scalar self-map implication are correct in their stated scope.

The vector Riesz transform is an isometry from scalar L2 into vector L2, so \(\langle H,G\rangle=\langle RH,RG\rangle\). Matrix Cauchy--Schwarz gives the asserted dual norm. For \(a\ge\beta N^2\), the function \(a-d_F\sqrt a\) is increasing once \(\sqrt a\ge d_F/2\), and the first radius restriction ensures this throughout the comparison range. Substitution then gives the stated upward quadratic in N. Its nonnegative root gives the bound, including the zero weak-price case. The effective scalar source is \(n_{\rm eff}=\sqrt\beta d_F\), so the original global Cauchy--Schwarz bound is recovered when \(d_F\) is replaced by \(\|H\|_2/\sqrt\beta\).

The argument requires the actual full energy inequality with all remainder and nonlinear losses included. It does not certify an evaluated d_F or any missing commutator constant. It can be inserted into the smooth-coefficient approximation bridge of `OPERATOR_BRIDGE_v01.md`, whose homogeneous semigroup part uses the same energy without the inhomogeneous source pairing.
