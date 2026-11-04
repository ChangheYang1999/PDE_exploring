# Topology of a regular trapping neighborhood

## Exact statement

Let B be a complete C1 vector field on R3 with div B=d>0 constant. Let N be a nonempty compact C2 three-dimensional submanifold with boundary, and assume B.n>0 on its boundary, where n is the outward unit normal. Let

A=intersection_{t>=0} Phi_{-t}(N).

Suppose A contains no zero of B. Then each connected component N_i has connected boundary diffeomorphic to a torus, and

H_1(N_i;R)=R, H_2(N_i;R)=0.

For the backward flow, the basin W(A) is the union of the forward images of int N and strongly deformation retracts onto N. In particular W(A) is a proper subset of R3.

Connectedness of N is required to conclude that the entire boundary is a single torus. The statement here makes no classification of the knot type of N. For the Euler application, completeness follows from uniformly sublinear U, and d=3c.

## Proof

Strict outward transversality implies Phi_{-t}(N) is contained in int N for t>0. A zero p of B in N would belong to every Phi_{-t}(N), hence to A. Therefore B has no zero on N. The outward form of the Poincare-Hopf theorem gives chi(N_i)=0 for each component. Doubling N_i across its boundary gives a closed orientable three-manifold. Its Euler characteristic is zero by Poincare duality, whereas the gluing formula gives

0=2 chi(N_i)-chi(boundary N_i).

Thus chi(boundary N_i)=0.

The complement of N_i has no bounded component. If V were such a component, its boundary consists of some boundary components of N_i. The normal pointing out of V is the negative of the corresponding normal pointing out of N_i. The divergence theorem would give

d vol(V)=integral_boundary V B.n_V < 0,

which is impossible. The complement is consequently connected: outside any ball containing N_i there is only one unbounded component. Alexander duality in S3 now gives H^2(N_i;R)=0, and hence H_2(N_i;R)=0.

Write k for the number of boundary components. The long exact homology sequence of (N_i,boundary N_i), together with orientability and connectedness, contains

0=H_3(N_i;R) -> H_3(N_i,boundary N_i;R)=R
  -> H_2(boundary N_i;R)=R^k -> H_2(N_i;R)=0.

Therefore k=1. A closed connected orientable surface of Euler characteristic zero is a torus. Finally chi(N_i)=0, H_0=R and H_2=H_3=0 give dim H_1=1.

Put W=union_{t>=0} Phi_t(int N). Every point of W has backward orbit eventually in N and approaches A, by nested compactness. Conversely every orbit approaching A eventually enters int N, since A lies strictly inside N. Thus W=W(A).

For x outside N but in W, let tau(x)>0 be its first entrance time into N under Phi_{-t}, and put tau(x)=0 for x in N. The entrance exists by definition of W, is unique because N is backward invariant, and is continuous by strict transversality and the implicit function theorem. It remains continuous at boundary N with value zero. Then

H(s,x)=Phi_{-s tau(x)}(x), 0<=s<=1,

is a continuous deformation in W, fixes N pointwise, and ends in N. This proves the strong deformation retraction. Since N has at least one nonzero first homology group, W cannot be all of R3.

## Audit scope

The coordinator's paragraph omitted connectedness and boundary regularity. The precise version above is confirmed. Its assertion that boundary N is a single torus is not certified for arbitrary disconnected N. The solid-torus versus knot-exterior classification is not needed here and has not been included. These topological facts do not rule out a proper backward attractor.
