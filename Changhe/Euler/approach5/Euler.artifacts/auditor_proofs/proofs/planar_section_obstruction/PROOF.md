# A regular vortical attractor has no compact planar global section

## Exact statements

(A) Let S be a compact smooth surface with boundary embedded in R2. It may have finitely many components. Let p:S->int S be a C1 embedding. Suppose every fixed point of every iterate p^n has two real derivative eigenvalues satisfying 0<lambda_s<1<lambda_u. Then the set of all periodic points is finite.

(B) Let 0<c<1/2, a=1-2c, kappa=1+c. On an open subset of R3 let B,W be C1, div B=3c, div W=0, and [B,W]=-kappa W. Write Psi for the reversed B flow. Let Lambda be a compact transitive nonsingular hyperbolic attractor, not a single periodic orbit, with one stable and one unstable dimension. Suppose B cross W is nowhere zero on Lambda and Lambda has a compact trapping neighbourhood N with Psi_t N contained in int N for t>0 and intersection Lambda. No compact planar surface S in N can be transverse to B, have a first-return map of Psi defined everywhere with p(S) contained in int S, and meet every periodic orbit in Lambda. For every straight line L disjoint from Lambda, the angular derivative B.grad theta_L has a zero on Lambda.

(C) If in addition U=B-(cI-omega J)y solves the rotating Euler profile equation near Lambda with a single-valued pressure, and W=curl U there, then for every b=(b1,b2,0), the function

    F_b(y)=|B(y)|^2+omega J(y-b).B(y)

has both a strictly positive and a strictly negative value on Lambda. The conclusion in particular precludes such an Euler attractor at omega=0. No nonexistence for nonzero omega follows.

## Proof of (A)

The fixed points of p^n are nondegenerate, have fixed-point index -1, and lie in the interior. They form a compact isolated set, hence are finite. The Lefschetz-Hopf formula gives

    -#Fix(p^n)=trace(p^n_*|H0(S;R))-trace(p^n_*|H1(S;R)).

There is no H2. The H0 trace is bounded by the number of components. To bound the H1 trace, choose one point in each bounded complementary component of R2 minus S. Winding numbers about these points identify H1(S;Z) with a finite-dimensional integer lattice. Choose a fixed basis represented by simple boundary curves. Since p^n is injective, the image of each basis curve is still a simple closed planar curve. Its winding number about each chosen point is -1, 0 or 1 by the Jordan curve theorem. Passing from these winding coordinates to the fixed homology basis uses one fixed matrix. Thus all entries of p^n_* and its trace are bounded independently of n.

The number of fixed points of every iterate is consequently bounded by one finite constant. If infinitely many periodic points existed, choose arbitrarily many distinct ones and take the least common multiple of their periods. That iterate would fix all of them, a contradiction.

The inputs here are the standard fixed-point index formula, Lefschetz-Hopf, and elementary planar winding homology. No area-preservation hypothesis is present.

## Proof of (B)

Define alpha=(B cross W).dy. The bracket and divergence identities imply

    D Psi_t W(x)=exp(-kappa t) W(Psi_t x),
    Psi_t^* alpha=exp(a t) alpha.

At a periodic orbit of period T, the induced derivative on the quotient by the flow direction has eigenvalue exp(-kappa T) in the W direction. Its other eigenvalue is exp(aT), because alpha annihilates the flow and W directions and is nonzero on their quotient complement. Both eigenvalues are positive, with one below and one above one.

Assume the stated S exists. First return to a transverse compact surface, with every return in its interior, is a C1 embedding. Smooth dependence of return time follows from transversality. Injectivity follows from uniqueness of the flow and the absence of an intermediate return. A periodic point of its return map yields a complete orbit in N, hence lies in Lambda. The derivative of the return map on the transverse plane is conjugate to the flow derivative on the quotient by B, so all its periodic points satisfy (A). Yet a nontrivial transitive locally maximal hyperbolic set has infinitely many periodic orbits, by the standard closing/density theorem. All meet S. This contradicts (A).

Now suppose L misses Lambda and B.grad theta_L never vanishes there. Lambda is connected, being the closure of a continuous dense orbit. The angular derivative therefore has one sign. Choose an open neighbourhood G of Lambda whose closure misses L and on which its absolute value is bounded below by epsilon>0. For sufficiently large t0, N'=Psi_(t0)N is contained in G and remains a compact strict trapping neighbourhood.

Let Sigma be one open half-plane with boundary L, and put U0=N' intersect Sigma. This is compact, because N' stays a positive distance from L. Along Psi orbits in N', angle changes strictly monotonically at rate at least epsilon. First return to Sigma after one full turn exists for every point of U0, takes time at most2pi/epsilon, and lands in the relative interior of U0 by strict trapping. The return map is C1 on an open neighbourhood of U0 in Sigma: transversality, the compact time interval, and uniform angular monotonicity give the usual implicit-function construction. It is injective.

Choose a compact smooth planar surface S with

    p(U0) contained in int S, and S contained in relative int U0.

Such an S exists because p(U0) is compact in that open planar set. Then p(S) is contained in p(U0), hence in int S. Every periodic orbit of Lambda crosses Sigma; moreover Lambda intersect Sigma is mapped onto itself, so all these intersections lie in p(U0) and hence in S. This contradicts the first part of (B).

## Proof of (C)

On the vertical axis L_b, F_b=|B|^2>0. If F_b were nonpositive everywhere on Lambda, the attractor would miss that axis, and

    omega r_b^2 B.grad theta_b=omega J(y-b).B<=-|B|^2<0

throughout Lambda. This is incompatible with (B), including omega=0. Thus F_b is positive on a nonempty relatively open subset of Lambda. Periodic orbits are dense, so one periodic orbit meets that subset.

The exact Euler circulation law on every periodic orbit is

    integral_0^T [|B|^2+omega Jy.B] dt=0.

Changing the axis adds -omega Jb.B, whose integral vanishes because the orbit closes. Therefore the same zero integral holds for F_b. If F_b were everywhere nonnegative on Lambda, its integral on the periodic orbit meeting the positive open subset would be positive. This contradiction supplies a negative value as well.

## Scope

This confirms Theory Agent C C27, Proposition5.10(i)-(iii). It does not assert that an arbitrary hyperbolic set has a planar section. The compact section and return hypotheses are precisely what make the Lefschetz count applicable. The regular independent bracket model already constructed elsewhere has sections of positive genus and is not excluded. This is a geometric restriction, not a general Euler obstruction at arbitrary nonzero rotation.
