# An irrotational stagnation point can lose its contracting direction under rotation

## Exact claim refuted

For `0<c<1/2`, the implication

\[
 B(p)=0,\qquad \Omega(p)=0,\qquad
 \lambda_{\max}(\operatorname{sym}DU(p))\ge1
 \quad\Longrightarrow\quad
 DB(p)\text{ has an eigenvalue with negative real part}
\]

is false for rotating Euler profiles, even when the full momentum equation holds exactly.

The counterexample has linear growth. It is a local obstruction to transferring one step of the nonrotating proof, not a counterexample to the decaying-profile conjecture.

## Construction and verification

For any `0<c<1/2`, take

\[
 \omega=2,\qquad U(x,y,z)=(x,-y,0),\qquad P(x,y,z)=-x^2-4xy.
\]

The field is smooth and divergence-free, and `curl U=0`. Its derivative is `S=diag(1,-1,0)`, so its maximal strain eigenvalue is one.

For a general symmetric trace-free matrix `S`, the affine field `U(y)=Sy` solves the rotating equation with

\[
 P(y)=-\tfrac12 y^T N y,
 \qquad N=S+S^2+\omega(JS-SJ).
\]

Indeed, `N` is symmetric because `S` is symmetric and `J` is skew; substitution gives the nonpressure residual `Ny`. For the displayed `S` and `omega=2`,

\[
 N=\begin{pmatrix}2&4&0\\4&0&0\\0&0&0\end{pmatrix},
\]

which yields the stated pressure.

The origin is a stagnation point of `B`, and

\[
 DB=cI-2J+S
   =\begin{pmatrix}c+1&2&0\\-2&c-1&0\\0&0&c\end{pmatrix}.
\]

Its eigenvalues are

\[
 c+i\sqrt3,\qquad c-i\sqrt3,\qquad c.
\]

All have positive real part. This proves the claimed implication false.

## Consequence for the audit

The nonrotating proof uses `Omega(p)=0` to conclude that `DB(p)=cI+DU(p)` is symmetric. In the rotating equation, it is `DB(p)+omega J` that is symmetric. Eigenvalues of the strain do not directly control real parts of the nonsymmetric matrix `DB(p)`.

The example does not invalidate the generic null-graph theorem, nor the conditional contracting-two-form theorem. Those use the actual eigenvalues of `DB` or its period map. It invalidates using the old strain-threshold set as though its spectral conclusion were unchanged by rotation.

Hypotheses: H0 holds with smooth affine data; H1 and H1' fail; no extra pressure normalization is imposed. This is an exact algebraic counterexample and needs no numerical experiment.
