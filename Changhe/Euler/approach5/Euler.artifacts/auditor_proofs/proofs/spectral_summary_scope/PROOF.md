# Two limits on the spectral summary

## 1. Anisotropic component energy retains rotation

Let \(U\in C^2(\mathbb R^3)\), \(P\in C^1(\mathbb R^3)\) be a
divergence-free rotating Euler profile, with any real \(c,\omega\).
For an axisymmetric \(\phi\in C_c^1(\mathbb R^3)\), put
\(D=y\cdot\nabla\) and \(N=(U\cdot\nabla)U\). Then
\[
 \omega\int\phi U_1U_2
 =\int\left((1-\tfrac52c)\phi-\tfrac c2D\phi\right)U_1^2
   +\int\phi U_1(N_1+\partial_1P).                         \tag{1}
\]
All integrals are over \(\mathbb R^3\). Compact support is the only
boundary condition needed. Thus rotation survives in quadratic
component balances as well as in the angular-multiplier balance.

To prove (1), write the equation as
\[
 (1-c)U+cDU+N+\nabla P=\omega LU,\qquad
 LU=(Jy\cdot\nabla)U-JU.
\]
Its first component on the right is
\(\omega((Jy\cdot\nabla)U_1+U_2)\). Multiply by \(\phi U_1\).
The angular derivative integrates to zero because
\(\operatorname{div}(Jy)=0\) and \(Jy\cdot\nabla\phi=0\).
Also
\(\int\phi U_1DU_1=-\frac12\int(3\phi+D\phi)U_1^2\).
Substitution gives (1).

The rotation term is not an identically zero functional on profiles
without decay. For \(U=(1,1,0)\), take
\[
 P=-((1-c)-\omega)y_1-((1-c)+\omega)y_2 .
\]
This is an exact constant profile and
\(\omega\int\phi U_1U_2=\omega\int\phi\), nonzero for
\(\omega\ne0\) and a nonnegative nonzero weight.
This example is only a test of the alleged identity classification.
It has no decay and supplies no counterexample to nonexistence.

The density \(U_1^2/2\) is not rotation-equivariant. Consequently (1)
does not refute the precise equivariant-density theorem A043.
It does refute the literal unqualified sentence that the
angular-multiplier identity is the only quadratic balance retaining
rotation. The safe replacement is: it is an explicit such balance,
and its right side has no established sign.

## 2. Smooth angular data restrict modal energy distributions

Let \(F\in C^\infty(S^2;\mathbb R^3)\). Use the unitary rotation action
\(\mathcal R_\theta F(n)=R_\theta F(R_{-\theta}n)\) on vector fields
on the sphere, and write \(F_m\) for its complex Fourier projections.
For \(E_m=\|F_m\|_{L^2(S^2)}^2\), one has
\[
 E_{-m}=E_m,\qquad
 \sum_{m\in\mathbb Z}|m|^{2N}E_m<\infty
 \quad\hbox{for every integer }N\ge0.                     \tag{2}
\]
Indeed complex conjugation exchanges \(F_m\) and \(F_{-m}\).
The infinitesimal rotation generator is a smooth first-order
differential operator, so every power applied to \(F\) belongs to L2.
Parseval gives (2).

For example \(E_m=(1+|m|)^{-2}\) has finite total energy and the
required reality symmetry, but violates (2) for \(N=1\).
It therefore cannot be the modal energy distribution of smooth
spherical data. The same restriction holds for smooth tangential
data and for the full smooth tails they determine.

A075/A077 identify the admissible divergence-free leading tails with
arbitrary smooth tangential fields when \(c\ne1/3\).
They do not license every nonnegative sequence of modal energies.
One may say that no fixed finite angular-support restriction is imposed
by the linear tail equation. One must retain smoothness and reality
when describing freedom of the data.

## Dependencies and scope

Part 1 uses compactly supported integration by parts only.
Part 2 uses Fourier orthogonality for the rotation action on S2.
The existing exact tail parametrization is
A075/A077; it does not assert
extension of a tail to a global nonlinear profile.
A382 and A383 distinguish the confirmed identities from the refuted
unqualified summaries.
