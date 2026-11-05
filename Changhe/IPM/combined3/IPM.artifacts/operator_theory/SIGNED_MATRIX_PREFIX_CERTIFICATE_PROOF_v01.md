# Exact signed exterior and frozen core prefix

This note proves the assembly rule implemented in
`assemble_matrix_prefix_signed_far_v01.py`. The prefix is a whole-plane
matrix certificate only when that script reports
`CERTIFIED_ACTUAL_MATRIX_PREFIX_SIGNED_FAR` and the independent replay
reports `INDEPENDENT_MATRIX_PREFIX_AUDIT_PASS`. A pending prefix proves no
global matrix bound. The original 898-panel producer is left unchanged.

All fields are the exact 007-plus-013 fields, with the fixed rational
parameter specified in `structure013_result.json`. Put

\[
q=21/10,\quad W^2=1+4r^2,\quad
d=c+1+(cX+u_*)\cdot\nabla\log W,
\]
\[
S=\operatorname{Sym}Du_*,\quad
K=\begin{pmatrix}-\rho_{*,y}&\rho_{*,x}/2\\
\rho_{*,x}/2&0\end{pmatrix},\qquad
M=(d-qc)I-qS-K.
\]
The required assertion is the actual matrix inequality
\(M\ge(7/10)I\), including the full background source matrix.

For every radius, the largest eigenvalue of \(K\) is exactly

\[
\theta=\frac{|\nabla\rho_*|-\rho_{*,y}}2.
\]
Moreover

\[
d-qc\ge 1+(2-q)c-\frac{c}{1+4r^2}-\frac{|u_*|}{r}.
\]
Consequently

\[
M\ge\left[1+(2-q)c-\frac{c}{1+4r^2}
-\frac{|u_*|}{r}-q\|S\|_{\rm op}-\theta\right]I.\tag{1}
\]

The existing independently verified signed L2 far expansion proves
\(\theta\le n_\theta r^p\) uniformly beyond its published starting
radius, where
\(p=-1824676646553933/4076476460239181<0\).
The new exact far expansion bounds \(|u_*|/r\) and \(\|S\|_{\rm op}\)
by sums of nonnegative coefficients times strictly negative powers.
Every power, including every analytic remainder power, is checked to be
strictly negative in the independent reconstruction. Thus evaluating the
right side of (1) at \(r=30000\) bounds it from below for every larger
radius. The containing lower is

\[
0.720066108588564173\ldots>7/10.
\]

The price, its source/code bindings, and the independent reconstruction
are recorded in `signed_matrix_far_price_v01.json`,
`../ROOT_SIGNED_MATRIX_FAR_REPLAY.json`, and
`../independent_closure_audit/signed_matrix_far_audit.json`.

At the origin, the exact constant harmonic checks give
\(u_{*,1x}=c-1\), \(u_{*,2y}=1-c\),
\(u_{*,1y}=u_{*,2x}=\rho_{*,x}=0\), and a constant positive
\(\rho_{*,y}\). Hence the center matrix is diagonal. Its smaller
eigenvalue is bounded below by
\(0.710319210199998\ldots\).
The degree-12 containing expansion on \(0\le r\le10^{-5}\), including
all remainder terms, subtracts at most
\(1.6800964\cdot10^{-9}\), leaving
\(0.710319208519901651\ldots>7/10\).
All powers in the perturbation bound are nonnegative, so its outer-radius
evaluation is uniform on that disk. The cached endpoint result is bound
to the complete original configuration, evaluators, prefix assembler,
structural certificate, and signed far price.

The frozen geometric core has
\(r_i=10^{-5}(33/32)^i\). The first 711 complete base panels cover
\([10^{-5},r_{711}]\), and the exact rational comparison verifies
\(r_{711}>30000\). On every used radial/angular leaf, the original
containing computation gives nonnegative diagonal entries and determinant
of \(M-(7/10)I\); these are precisely the two-dimensional positive
semidefinite criterion. Complete prefix-free binary leaf covers are
checked separately for every base panel. The assembler checks all 711
indices, every leaf flag, finite nonnegative minors, exact source and
configuration equality, and SHA256 bindings of every used raw chunk.

The origin disk, complete frozen core prefix, and signed exterior overlap
and exhaust the plane. Their conjunction proves the stated whole-plane
matrix inequality. No far-field assumption, sampled minimum, unfinished
core panel, or stationary existence assertion is substituted for this
conjunction.
