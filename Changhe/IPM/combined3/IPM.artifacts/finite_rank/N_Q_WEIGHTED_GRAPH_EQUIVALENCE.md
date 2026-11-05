# Equivalence of the auxiliary Q graph and the inherited weighted space

Status: qualitative norm equivalence with finite constructive constants. This is a regularity/domain statement, not an invariant-ball estimate with the inherited numerical norm constants.

Let \(q=21/10\), \(W_a=(1+a^2r^2)^{1/2}\), \(a>0\), and \(Q_a(g)=\|W_aJ^qg\|_2\). The Q graph is equivalent to
\[
 \|J^qg\|_2+\sum_{j=1}^2\|J^q(x_jg)\|_2.
\]
Indeed the exact Fourier commutator is
\[
 [x_j,J^q]=q\partial_jJ^{q-2},
\]
up to the harmless Fourier sign convention. Its L2 norm is bounded by \(q\|J^{q-1}g\|_2\le q\|J^qg\|_2\). The identity
\[
 Q_a(g)^2=\|J^qg\|_2^2+a^2\sum_j\|x_jJ^qg\|_2^2
\]
then proves both directions by the triangle inequality, with finite constants depending on \(a,q\).

For the inherited weight \(W_2=(1+4r^2)^{1/2}\), define the bounded smooth frame
\[
 b_0=W_2^{-1},\quad b_1=2x/W_2,\quad b_2=2y/W_2.
\]
Every derivative of these three coefficients is bounded. The exact relations are
\[
 (g,2xg,2yg)=b(W_2g),\qquad
 W_2g=b_0g+b_1(2xg)+b_2(2yg).
\]
Multiplication by each frame coefficient is bounded on H2 and H3 by direct Leibniz differentiation. Interpolation gives boundedness on Hq. The frame identities therefore prove equivalence of the displayed graph norm with
\(\|J^q(W_2g)\|_2\).

For completeness, Hq multiplier interpolation may be obtained by interpolating the bounded operators on the pair of Hilbert Sobolev spaces H2,H3. Only finite derivative suprema through order3 of the explicit frame enter. Alternatively the same conclusion follows from the elementary Bessel-potential product estimate proved by Fourier convolution after a smooth frequency partition of each frame coefficient. No uniform-in-a statement near a=0 is needed.

Consequently any stationary correction proved in a fixed Qa graph has the inherited weighted Hq regularity. This does not allow the inherited sharp numerical nonlinear constants to be reused automatically in a new norm; those constants require their separately proved Qa estimates.

The same graph representation gives density of smooth cutoffs and mollifications. First approximate the three Hq coordinate components simultaneously by a physical cutoff; its derivative errors are controlled by the graph tails and bounded cutoff derivatives. Then mollify, using the exact coordinate/convolution commutator. The graph convergence implies Qa convergence. On S1, choose radial cutoffs and radial mollifiers so every approximant remains in that symmetry class.
