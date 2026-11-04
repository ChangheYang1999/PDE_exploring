# Continuous strong plaques for a C2 hyperbolic flow

## Exact statement

Let X be a C2 vector field on a smooth finite-dimensional manifold without boundary. Let K be a compact invariant set on which X never vanishes, with continuous invariant splitting

    T_K M = R X direct-sum E^u direct-sum E^s.

Assume uniform exponential contraction of E^s forward and E^u backward. The flow is defined for every real time on K and on the nearby finite-time domains needed below. Then local strong stable and unstable disks can be chosen on uniform small domains, with their parametrizations continuous in the base point in the C1 topology, in local continuous bundle frames. Weak plaques obtained by adjoining a short flow interval have the same continuity.

No orientability, transverse differentiability, local maximality, transitivity or attractor property is asserted. The result is confined to nonsingular compact hyperbolic sets.

## Primary-source input checked

The actual manuscript Semyon Dyatlov, Notes on hyperbolic dynamics, arXiv:1805.11660v1, is retained in the literature agent as in the team records. Section 4.6, Definition 4.6 and Theorem 5 give strong C1 disks for a C2 vector field, with uniform domains, tangencies, one-step invariance and a dynamical characterization. Theorem 5(7) requires both backward closeness and backward convergence to identify a strong unstable disk; closeness alone is insufficient because of the flow direction.

Equation (4.67) gives uniform exponential contraction for all real times in the relevant half-line. Sections 2.3 and 3.2-3.6 construct the graphs in a uniformly bounded C^{N,1} class. Equation (2.29) is the explicit bound; N=1 gives the required C1,1 control. Section 3.6 allows the neutral direction in the complementary block, and the proof of Theorem 5 applies this with lambda=1 and mu>1. These passages were read directly. Continuity in C1 is reconstructed below, rather than attributed to a nonexistent explicit clause of Theorem 5.

## Proof

Fix x in K and continuous local frames for E^u and its complement R X plus E^s. A smooth ambient chart, translation to each base point and these frames give spatially smooth charts whose coefficients depend continuously on that point. Compactness and uniform transversality permit a common small graph domain. The source construction gives local unstable graphs F_z with F_z(0)=0, derivative zero at zero, and uniformly bounded C1,1 norms on a smaller closed domain.

For any sequence x_j tending to x, Arzela-Ascoli yields a subsequence of the graphs converging in C1 to a graph F. For a fixed parameter v, write q_j for its point on the graph through x_j and q for its limit on F. Uniform contraction gives

    d(Phi_-t(q_j),Phi_-t(x_j))
        <= C exp(-nu_0 t) d(q_j,x_j),   t>=0,

with constants independent of j. For each fixed t, continuous dependence of the flow passes this inequality to the limit. Choose the graph domain so small that the right side is always below the local characterization radius. The limiting point stays uniformly close to x backward and its orbit distance tends to zero. Theorem 5(7) therefore places q on the strong unstable disk through x. Since that disk is a graph over the same domain, F equals its graph. Every convergent subsequence has this same limit, so compactness implies convergence of the entire sequence in C1.

Apply the argument to the reversed vector field for stable plaques. For weak plaques use the parametrization (s,v) -> Phi_s(q_x(v)) on a uniform short time interval. C2 flow dependence and the established graph continuity give continuous first derivatives in s and v. Transversality of the flow direction and strong direction gives an embedded plaque after shrinking the domains.

In particular every interior point of a plaque through x is approximated by points of plaques through x_j. This is the continuity consequence used in the compact saturation arguments of A115.

## Verification and scope

This verifies the literature agent's auxiliary reconstruction. It neither replaces A115's separate closing argument with an unread book theorem nor supplies any result at a zero of X. No computation is required.
