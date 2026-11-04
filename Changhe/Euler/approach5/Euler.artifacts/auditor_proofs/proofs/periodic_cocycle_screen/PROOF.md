# Periodic multiplier ratios survive time and norm changes

## Statement

Let U in C2 and P in C1 solve the rotating Euler profile equation on a neighborhood of a nonstationary periodic orbit of B=(cI-omega J)y+U, where div U=0, 0<c<1/2 and omega is any finite real number. Suppose Omega=curl U is nonzero on that orbit. For the backward flow of -B, whose minimal period is T, the transverse multipliers are

    exp(-(1+c)T), exp((1-2c)T).

Their logarithmic ratio is -(1+c)/(1-2c). A positive C1 time change of a nonsingular vector field preserves its local Poincare return map and these multipliers. A change of positive continuous norms on invariant one-dimensional bundles also preserves periodic expansion factors.

## Proof

Put b=1+c and a=1-2c. The audited bracket [B,Omega]=-b Omega gives D Phi_T Omega=exp(bT)Omega at the periodic point. The nonzero flow vector B is an eigenvector with eigenvalue one. These eigenvalues are distinct, so the two vectors are independent. Constant divergence 3c gives det D Phi_T=exp(3cT). The third eigenvalue is therefore exp((3c-b)T)=exp(-aT). Inverting the derivative gives the displayed backward multipliers. Quotienting by the flow line identifies the two noncentral multipliers with those of the transverse return map.

For a positive time change, oriented orbits and their order of intersection with a sufficiently small transverse section do not change. The first-return map on that section is the same map of points. Its derivative and spectrum therefore do not change, although the elapsed period can change.

If a bundle norm is multiplied by a positive continuous q(x), logarithmic expansion along a time t segment changes by log q(Psi_t x)-log q(x). This vanishes at a periodic return. The argument applies to norms on unoriented real lines as well, where the expansion factor is absolute value.

## Dependencies and scope

Only the exact bracket, div B=3c, Liouville's determinant formula and elementary flow geometry are used. Global decay and completeness are not required for this local statement. This confirms LIT34 and overlaps the periodic part of A161. A candidate whose periodic ratios fail this test cannot be repaired by these operations alone. Passing the test is not sufficient for a smooth global eigenfield, exact divergence, global gluing or the Euler curl relation. No universal failure of DA models is proved.

Audit written: 2026-11-02T20:46:53Z
