# No smooth stationary density for the inviscid transport adjoint

## Statement

In dimension d>=1, let c>0, let K be a constant skew matrix, and let U be C^1, divergence-free and uniformly sublinear. Put B=(cI+K)y+U. If w is C^1 on R^d and div(Bw)=0, then w=0. No sign or integrability assumption on w is needed. Hypothesis tags: H1-prime and the stated regularity and divergence assumptions; the Euler momentum equation is not used.

## Proof

B has at most linear growth, so its flow Phi is complete. Skew symmetry gives B(y) dot y=c|y|^2+U(y) dot y, which is positive and at least c|y|^2/2 outside a large ball. Thus each backward orbit is contained in a compact ball. Since div B=dc, the equation becomes B dot grad w=-dc w. Along the flow,

\[
 w(\Phi_s y)=e^{-dcs}w(y),\qquad
 w(y)=e^{-dct}w(\Phi_{-t}y)\quad(t>0).
\]

Continuity bounds the last factor on the backward orbit closure. Letting t tend to infinity proves w(y)=0 for every y.

## Scope

This confirms LIT04. It rules out a nonzero C^1 density for the zero-eigenvalue adjoint -div(B times). It does not rule out compactly supported singular invariant measures, densities for another eigenvalue, viscosity-dependent weights, or distributional objects with unbounded singularities. The proof does not assume that the backward orbit converges.
