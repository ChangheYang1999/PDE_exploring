# Exact harmonic-potential profiles on an open domain

## Statement

Let `D` be an open subset of `R^3`, let `phi` be a smooth harmonic scalar on `D`, and let `c,omega` be arbitrary finite real numbers. Then

\[
 U=\nabla\phi,\qquad
 P=-(1-2c)\phi-c\,y\cdot\nabla\phi
       +\omega(Jy)\cdot\nabla\phi-\tfrac12|\nabla\phi|^2
\]

solve the full rotating profile equation on `D`, with `div U=0`. Nonzero decaying examples on punctured space can be non-axisymmetric, but no such example is a smooth decaying whole-space field.

This is an independent check of LIT10 in the team records.

## Proof

Harmonicity gives divergence zero. Since the Hessian of `phi` is symmetric,

\[
 (U\cdot\nabla)U=\nabla(|U|^2/2),\qquad
 (y\cdot\nabla)U=\nabla(y\cdot\nabla\phi)-U.
\]

For the skew matrix `J`, the product rule gives

\[
 \nabla((Jy)\cdot\nabla\phi)
       =-JU+(Jy\cdot\nabla)U.
\]

Consequently all momentum terms except `grad P` sum to

\[
 \nabla\big((1-2c)\phi+c\,y\cdot\nabla\phi
        -\omega(Jy)\cdot\nabla\phi+|U|^2/2\big).
\]

This proves the exact equation. If `D=R^3` and `U->0`, each component of `U` is a bounded entire harmonic function, hence constant; its limit makes it zero.

For a non-axisymmetric punctured example, put `R=|y|` and `phi=y_1/R^3`. This is minus the first derivative of `1/R`, and is harmonic away from zero. Direct differentiation gives

\[
 U=e_1/R^3-3y_1y/R^5,\qquad
 |U|^2=R^{-6}+3y_1^2R^{-8}.
\]

Euler homogeneity and angular differentiation give `y dot grad phi=-2phi` and `(Jy) dot grad phi=-y_2/R^3`. Thus

\[
 P=(4c-1)y_1/R^3-\omega y_2/R^3
          -\tfrac12(R^{-6}+3y_1^2R^{-8}).
\]

This field decays as `R^-3` and has a singularity of that order at zero. It proves that an exterior nonzero angular mode is compatible with the exact PDE at every rotation rate. It does not prove that it can be extended through the interior. A cutoff would destroy the harmonic-gradient calculation.

## Scope

Whole-space regularity is the failed target hypothesis of the nonzero example. No finite-mode approximation, asymptotic expansion, or numerical evidence is used.
