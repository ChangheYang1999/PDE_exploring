# Low-energy compactness does not identify the IPM quadratic term

## Exact statement

Let H be the S1 homogeneous H^-1 space, and let U have the canonical IPM multiplier
\((\xi_1\xi_2/|\xi|^2,-\xi_1^2/|\xi|^2)\). There is a sequence of real smooth compactly supported S1 densities h_n such that

- every h_n is zero in a common neighborhood of the origin;
- c[h_n]=0 exactly;
- h_n is bounded in L2 and converges weakly to zero there;
- h_n converges strongly to zero in H;
- nevertheless \(U[h_n]\cdot Dh_n\) does not converge to zero as a distribution.

More precisely, for any nonzero smooth S1 amplitude A supported in an annulus, the sequence can be chosen so that

\[
U[h_n]\cdot Dh_n\longrightarrow -\frac12\partial_y(A^2)
\quad\hbox{in distributions}.\tag{1}
\]

The right side is nonzero for such a nonzero compactly supported A. This result does not rule out weak existence. It rules out passing to the nonlinear equation from just these particular compactness statements without an additional argument.

## Construction and Fourier limit

Begin with f_n=A(X)cos(nx). It has S1 parity and the same support as A. The two Fourier translates of A escape to infinity, so f_n converges weakly to zero in L2. Its norms converge to \(\|A\|_2/\sqrt2\).

Along both x-frequency rays the IPM multiplier converges to (0,-1). By Plancherel and dominated convergence on the translated Fourier variables,

\[
\|U[f_n]+(0,f_n)\|_2\longrightarrow0.\tag{2}
\]

There is no singularity problem at xi=0: the multiplier is bounded almost everywhere, and its value at one point is immaterial in L2.

## Strong convergence in H^-1

The elementary identity

\[
f_n=\frac1n\partial_x(A\sin nx)-\frac1n A_x\sin nx
\]

gives the first term an H norm at most \(\|A\|_2/n\). The second term is centrally odd. For every centrally odd compactly supported f,

\[
\|f\|_H\le\||X|f\|_2.\tag{3}
\]

To prove (3), it is enough in the dual norm to test against centrally odd functions phi. Their angular Fourier series has no zero mode, so the circle Poincare inequality gives
\(\int |\phi|^2/r^2\le\int|\nabla\phi|^2\). Cauchy-Schwarz now bounds \(\int f\phi\) by \(\|rf\|_2\|\nabla\phi\|_2\). Therefore

\[
\|f_n\|_H\le\frac{\|A\|_2+\|r A_x\|_2}{n}\longrightarrow0.\tag{4}
\]

## Quadratic defect

Incompressibility gives \(U[f_n]\cdot Df_n=\operatorname{div}(f_nU[f_n])\). From (2) and the bounded L2 norms,
\[
\|f_nU[f_n]+(0,f_n^2)\|_{L^1}\longrightarrow0.
\]
But
\[
f_n^2=\tfrac12 A^2+\tfrac12 A^2\cos(2nx)
 \longrightarrow\tfrac12 A^2
\]
against every smooth compact test, by integration by parts in x. Taking distributional divergences proves (1) for f_n.

If \(\partial_yA^2\) were identically zero, A^2 would be independent of y. Compact support would then force A=0. Thus the limit is nonzero.

## Exact strain and origin constraints

Because A is supported away from zero, the contact term is zero and
\[
c[f_n]=\frac1\pi\int \frac{\sin(3\theta)}{r^3}A(X)\cos(nx)\,dX.
\]
Repeated integration by parts gives \(c[f_n]=O(n^{-N})\) for every N. Choose a fixed smooth S1 function phi supported away from zero, with nonzero strain, for example
\(\phi=\eta(r)(3x^2y-y^3)\) with nonnegative nonzero annular eta. Its strain is \(\int\eta(r)r\,dr>0\). Set

\[
h_n=f_n-\frac{c[f_n]}{c[\phi]}\phi.
\]

The correction tends to zero in L2 and H, and preserves the common zero neighborhood after shrinking it if necessary. It gives c[h_n]=0 exactly. Since U is bounded on L2, the difference between h_nU[h_n] and f_nU[f_n] tends to zero in L1. Thus (1)-(4) survive unchanged.

## Scope for weak-space closure

A Galerkin or vanishing-viscosity sequence controlled only in the baseline low energy \(E_0^2=\|h\|_2^2+(20/21)\|h\|_H^2\), with strong H convergence, can retain the quadratic defect (1). Energy cancellation of the transport term at each finite approximation does not fix this problem. The explicit example also satisfies the exact strain and all origin-jet constraints, so those finite constraints do not restore nonlinear compactness.

Any proposed low-energy existence proof must additionally supply strong local L2 compactness, enough regularity for a justified nonlinear stability argument, or another mechanism that actually excludes this defect. The counterexample does not apply to a sequence strongly convergent in local L2 with suitable tail control.

## Dependencies and verification

Only boundedness and the explicit multiplier of U, Plancherel, elementary oscillatory integration, angular Poincare, and the separately proved contact formula are used. There is no numerical input or PDE existence theorem hidden in the argument. No formal build was run.
