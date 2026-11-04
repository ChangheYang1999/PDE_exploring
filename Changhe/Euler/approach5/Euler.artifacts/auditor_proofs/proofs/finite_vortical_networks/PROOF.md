# Finite hyperbolic vortical networks have null backward basins

## Statement

Let U in C2(R3;R3), P in C1 solve the full rotating Euler profile equation with div U=0, 0<c<1/2 and finite omega. Assume the carrier flow is complete; uniform U=o(|y|) is sufficient. Put B=(cI-omega J)y+U and Omega=curl U.

Let Gamma be a compact invariant set on which Omega never vanishes. Assume Gamma consists of finitely many hyperbolic zeros of B and finitely many full nonstationary orbits, each of which converges at both time ends to zeros in that finite set. Then every precompact backward carrier orbit whose limit set is contained in Gamma converges to one of its zeros. Its basin is contained in the finite union of their global backward stable manifolds and is Lebesgue-null.

This confirms the revised vortex-foliation proof of Theory Agent B B20. The earlier proof using only eigenvalue ratios is insufficient: a general three-dimensional transition map need not preserve the scalar transverse coordinate. Here that preservation follows from the exact vorticity bracket. No inequality lambda_2<1+c is assumed.

## Exact transverse form

Write X=-B, Psi_t=Phi_-t, a=1-2c>0, b=1+c, and define

    w2=i_Omega vol,       alpha=i_X w2.

The divergence-free property of Omega and the bracket [X,Omega]=b Omega give

    d w2=0,       L_X w2=a w2,
    d alpha=a w2, L_X alpha=a alpha,
    alpha(X)=alpha(Omega)=0,       L_Omega alpha=0.       (1)

The signs can also be checked from div X=-3c: L_X w2=i_[X,Omega] vol+(div X)w2=(b-3c)w2=a w2.

At every regular point of Gamma, X and Omega are independent by A130. Choose a small section Sigma transverse to X, saturated by local Omega segments. On this section w2 restricts to zero, so alpha restricts to a closed nonzero one-form. Its kernel is the Omega direction. There is therefore a local transverse coordinate r, constant along those segments, with

    alpha|Sigma=dr.

A local Poincare map P from such a section to another, with positive flight time T(x), satisfies the exact variable-time formula

    P^*(alpha|Sigma_out)=exp(a T(x)) alpha|Sigma_in.     (2)

Indeed the derivative of P is D Psi_T plus X dT, and the second term is killed by alpha. The map preserves the Omega segments because Psi_t psi_tau=psi_(exp(-bt)tau) Psi_t. Consequently it induces a scalar C1 map g in the coordinates r, and

    |g'(r)|=exp(a T(r)).                              (3)

Changing the orientation of one scalar coordinate only changes the sign. The flight time is constant along local Omega fibers, since both sections are saturated. These facts require only C1 sections and the C1 vorticity foliation; the C2 carrier flow supplies C1 Poincare maps.

## Local quotient at an incoming node

Suppose a nonstationary orbit in Gamma converges to p under X. A147 and hyperbolicity imply

    spec DB(p)={b,lambda,-lambda-a},       lambda>0.

Thus X has two stable eigenvalues -b,-lambda and one unstable eigenvalue lambda+a. The two stable rates need not be ordered. In particular the Omega direction need not be the strongest stable direction.

The nonzero C1 field Omega defines a local one-dimensional foliation through p. The bracket makes X project to a planar C1 vector field. One way to check its regularity is to choose a smooth transverse plane, project X along Omega onto it, and use the C1 coefficients of Omega; the projected coefficients are C1. In a flow-box parameter z for Omega the lifted field has the form

    q'=F(q),       z'=-bz+h(q).

The quotient equilibrium is a hyperbolic saddle with rates -lambda and lambda+a. The local stable manifold of X is saturated by Omega segments: if Psi_t x tends to p, then Psi_t psi_tau x=psi_(exp(-bt)tau)Psi_t x also tends to p for sufficiently small tau. Thus its intersection with an incoming saturated section is precisely the r=0 fiber.

For either outgoing saddle branch, the local quotient passage is defined on a one-sided interval 0<|r|<delta and extends continuously to r=0, mapping it to the outgoing separatrix. This is the elementary local passage property of a planar C1 hyperbolic saddle: the stable and unstable invariant curves divide a small rectangle into sectors, and trajectories approaching the stable curve spend arbitrarily long near the equilibrium before exiting near the unstable curve. No smooth linearization is required. In particular T(r) tends to infinity as r tends to zero. The latter also follows from continuous dependence: bounded flight times could not take the limiting stable trajectory to an outgoing section.

Append the finite regular segment along an outgoing connection to the next selected section. The scalar map still extends with g(0)=0, when each section coordinate is based at its connecting orbit, and still satisfies (3) with total positive time. There are only finitely many nodes, connections and branches. Hence one common delta>0 makes every relevant transition satisfy

    |g'(r)|>=2,       |g(r)|>=2|r|,       0<|r|<delta.    (4)

The second inequality follows by integrating the first from the continuous endpoint g(0)=0. It remains valid if the derivative is unbounded at zero: integrate from epsilon>0 and pass to the endpoint. This is the exact replacement for the unaudited generic heteroclinic ratio argument.

## Finite itineraries and capture

Let K be the limit set of a precompact X-orbit and assume K is contained in Gamma. If the orbit eventually remains in one sufficiently small hyperbolic neighborhood of a node, the local stable-manifold theorem makes it converge to that node.

Otherwise it has infinitely many passages between node neighborhoods. Choose disjoint small node neighborhoods and finite thin tubes around the remaining compact connection arcs, with one saturated section in each tube. Outside the node neighborhoods X is bounded away from zero, and the finite connection arcs are disjoint. An orbit whose distance to Gamma tends to zero must, at all sufficiently late times, follow these tubes between node neighborhoods. Its visits therefore define an infinite itinerary among finitely many incoming and outgoing connection sections.

Nodes with no incoming connection in the limit set cannot be visited infinitely often without convergence. To see this directly, take last entrance points into a small hyperbolic ball during increasingly close visits. The times spent inside before approaching the node diverge by a Lipschitz bound on X. A convergent subsequence of entrance points then belongs to K and its forward X-orbit stays in the ball, giving a nontrivial incoming stable orbit in K. Since K is a union of nodes and complete connection orbits, this is an incoming connection of Gamma. Thus every node used in a late nonconvergent itinerary has the saddle quotient just described.

Let r_n be the scalar coordinate at the successive selected sections. Distance to Gamma tending to zero gives r_n tending to zero. Equation (4) gives |r_(n+1)|>=2|r_n| for every sufficiently late transition. This is impossible unless one r_n is zero. In that case the point is in the stable manifold of the next node and converges to it, contrary to nonconvergence. Hence every orbit under consideration converges to a node.

At any hyperbolic vortical node DB has eigenvalue b>0 and its other two eigenvalues have real parts summing to -a<0. Therefore X has at least one unstable direction. Its stable manifold has dimension at most two. Each global stable manifold is a countable union of C1 images of local stable disks, so has three-dimensional Lebesgue measure zero. A finite union remains null.

## Dependencies and scope

The proof uses the full vorticity transport relation, div Omega=0, A130's compact-vortical-set geometry, local hyperbolic stable manifolds and the scalar quotient passage. It does not use a generic Krupa-Melbourne criterion, a strong/weak ordering of the stable rates, a pressure normalization or a far-field decay rate. It does not cover nonhyperbolic nodes, infinitely many connections, singular chaotic attractors, or limit sets touching Omega=0. It is also valid for an independent divergence-free bracket field that is nowhere zero on Gamma; the curl coupling is used only to establish those identities.
