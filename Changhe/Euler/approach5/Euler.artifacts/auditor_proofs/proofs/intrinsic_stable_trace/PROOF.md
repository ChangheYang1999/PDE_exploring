# Intrinsic noncompactness of nontrivial periodic stable traces

## Exact statement

Let f be a C1 diffeomorphism of a finite-dimensional manifold, let p be a hyperbolic periodic point of period k, and let K be a compact fully f-invariant set containing p. Give the global stable manifold W^s(p) its injectively immersed manifold topology. If q in K intersect W^s(p) differs from p, then f^(-nk)(q) escapes every intrinsically compact subset of W^s(p). In particular K intersect W^s(p) is not intrinsically compact.

This is a dynamical-topology statement. It has no Euler or decay hypothesis.

## Complete proof

Set F=f^k. The stable-manifold theorem supplies an intrinsically open local neighborhood V of p such that F(V) is contained in V, F iterates converge uniformly to p on V, and every point of W^s(p) eventually enters V. One may choose V as a small stable-coordinate ball in an adapted contracting norm. Thus W^s(p) is the increasing union of the intrinsically open sets F^(-j)(V), j>=0.

Every intrinsically compact L lies in one F^(-J)(V), by the increasing open cover and compactness. Consequently F^n tends uniformly to p on L: first apply F^J, then use local contraction for the remaining iterates.

For every n, q_n=F^(-n)(q) belongs to K intersect W^s(p). If infinitely many q_n lay in a fixed intrinsically compact L, uniform convergence on L would give F^n(q_n) tending to p along those n. But F^n(q_n)=q differs from p. This contradiction proves escape and noncompactness.

## Independent topological cross-check

If an injectively immersed stable line has an intrinsically compact totally disconnected trace C, its inclusion restricted to C is a continuous injection from a compact space to a Hausdorff manifold. It is a homeomorphism onto its compact, hence closed, image. If that image is dense in a compact basic component K, then it equals K. It cannot do so when K contains an unstable arc, since K would then be totally disconnected. Thus dense global stable traces in a nontrivial expanding basic component cannot have both properties asserted in the printed compact-Cantor description.

## Actual source check and its limits

The actual Grines-Zhuzhoma 2005 manuscript in the team records was checked via its text extraction. Section 1 defines global stable manifolds as immersed submanifolds and uses their intrinsic topology. Printed page 625, Lemma 1.10, asserts intrinsic compactness of the global stable trace, and its first proof sentence infers this from ambient compactness of the attractor. This inference is false.

The earlier Lemmas 1.4-1.5 give a periodic boundary point p and nontrivial stable trace through p, to which the theorem above applies. Independently, the Section 1 C-dense decomposition and Lemma 1.8 provide the dense-trace cross-check. The error is not a claim that a closed trace in a compact local stable plaque fails to be compact: such local traces are compact. The global trace is intrinsically closed, but generally not compact.

The stable-gap statement of Lemma 1.9 precedes Lemma 1.10 and does not use its compactness inference. No verdict refuting that gap statement, the later global classification, or the underlying DA examples follows from this check. The source application uses the explicitly stated earlier periodic-boundary-point facts; the general noncompactness proof itself is independent of that source.

## Audit scope

This independently confirms LIT33. It does not settle the Euler regular-attractor case. No computation or formalization was used.

Audit written: 2026-11-02T20:46:53Z
