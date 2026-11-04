# Retained periodic volume obstruction

Audited 2026-11-02T20:54:35Z.

## Statement

Let M be an oriented three-dimensional smooth manifold, m a positive C1 volume form, and Y0 a C1 vector field preserving m. Let Q be a nonconstant periodic orbit. If a C1 field Y1 agrees with Y0 on a neighborhood of Q, and Q is retained in the domain, then no positive C1 time change of Y1, followed or preceded by a C2 coordinate diffeomorphism, has constant nonzero divergence near Q with respect to any positive C1 volume form.

Consequently a local DA perturbation of a volume-preserving toral suspension that leaves one original periodic orbit untouched cannot be converted by these operations into the backward carrier field of a profile with c>0. This conclusion requires the untouched orbit, not just the orbit-topological type of a DA attractor.

## Proof

Let T>0 be the period of Q under Y0. The derivative of the time-T map has eigenvector Y0 with eigenvalue one. Its full determinant is one because the volume at the initial and final point is the same preserved volume. The transverse Poincare derivative therefore has determinant one.

Y1 has the same vector field and derivative along Q and hence the same variational equation and transverse return determinant. Positive multiplication changes the clock but not the first-return map on a fixed local section. A coordinate diffeomorphism conjugates that map; at a periodic point the derivative determinants agree.

If the resulting field has constant divergence d relative to a positive volume form near its periodic orbit of new period S>0, Liouville's formula gives full time-S determinant exp(dS). The flow eigenvalue remains one, so its transverse determinant is exp(dS). The previously invariant value one forces d=0. The volume density cancels at the returning point; choosing a different smooth positive density cannot change this conclusion.

For a determinant-one integral hyperbolic toral automorphism, every rational point is periodic because its action is invertible on each finite denominator lattice. There are infinitely many periodic orbits, since each finite orbit is finite and there are infinitely many rational points. Choose two distinct suspension orbits and make the local perturbation and subsequent removal near one, disjoint from the other. The second orbit retains determinant one. A backward carrier has divergence -3c, giving the contradiction for c>0.

## Source and scope check

The actual Beguin-Bonatti-Yu manuscript, Building Anosov flows on 3-manifolds, Geometry and Topology 21 (2017), Section 8.1.1, printed pages 1896-1898, defines the perturbation to vanish outside its chosen tube. Section 8.1.3 states the reversed, repelling version used for an attracting plug. The read-only evidence is in the team records. Its preliminary general structural perturbation must not silently be assumed to preserve every original periodic derivative. For the linear toral suspension the chosen orbit is already locally linear, or any preliminary change can be kept disjoint from the test orbit. The theorem above explicitly assumes agreement near that orbit.

No detailed DA realization theorem enters the determinant proof. Arbitrary derivative changes, nonsmooth orbit equivalence and constructions without an untouched periodic orbit remain outside its scope. It overlaps A161/A164 but does not need the vorticity bracket or the Euler period lower bound.
