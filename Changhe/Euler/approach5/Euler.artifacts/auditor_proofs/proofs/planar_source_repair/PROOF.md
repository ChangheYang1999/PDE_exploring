# Two source corrections in the planar recurrence argument

Auditor verdicts: A390 and A391 REFUTE the literal source assertions; A392 CONFIRMS the specific repair. Full independent audit completed 2026-11-03T01:52:53Z.

## 1. Source, statement and scope

The actual manuscript is Jairo Bochi and Ian D. Morris, *A Poincare-Bendixson theorem for Bebutov shifts and applications to switched systems*, arXiv:2601.05863v1, January 9, 2026. The local copy is in the team records, SHA256 `77103cc3d1e9a9fc33aaa269b560b92026c2cbdfda76580a733a9f87094927fa`. Sections 2.1-2.4 and 3.1, including their proofs, were read. Definition 2.3 was also checked on the rendered page 6.

Theorem 3.1 asserts that a recurrent point of a continuous semiflow on a compact subset of the sphere or real projective plane is fixed or periodic. In A360 it is applied to a unique continuous angular flow on the whole sphere. The needed regularity is continuity of the flow, not differentiability of its generating field. Two corrections are required when following the source literally. They concern Definition 2.3 on page 6 and Proposition 2.12 on page 10. The rest of this note verifies the corrections and the graph step affected by the second one. The source's remaining topological and compactness arguments remain cited inputs; this is not a new independent proof of its entire theorem.

## 2. The switching formula

The displayed switching axiom in Definition 2.3 continues a spliced path by the constant value `phi_2(tau)` for times `t >= tau`. The proofs and the claimed semiflow example require continuation by `phi_2(t)` instead. This is not an OCR issue: the constant argument is printed in the PDF.

The literal constant-continuation axiom does not hold for the path space of a nonstationary deterministic semiflow. For example, take rigid rotation of a circle embedded in the sphere. A path stopped at a positive time and then held fixed is not an orbit of that semiflow. Indeed, the literal axiom, applied with the two paths equal and stopping times tending to zero, would force the constant path at each initial point into the compact path space. It would make the existence of constant paths in Theorem 2.4 immediate, but would exclude the nonstationary semiflows to which Section 3 applies it.

With continuation `phi_2(t)`, the semiflow path space satisfies the axiom: equality at the joining time and the semigroup law imply equality of both future orbit segments. This is the interpretation used in the proof of Theorem 3.1. No extra Euler hypothesis is needed for this correction.

## 3. A counterexample to the printed graph hypotheses

Proposition 2.12 assumes that a plane graph is connected and that each vertex has degree at least two. It asserts, among other conclusions, that each face has a cycle as its boundary and that each edge borders exactly two faces. Both assertions are false under those hypotheses.

Take the boundaries of the two squares with vertex sets

    {(0,0), (1,0), (1,1), (0,1)}
    {(3,0), (4,0), (4,1), (3,1)},

and join `(1,0)` to `(3,0)` by the straight segment. This is a finite connected plane graph of the source's permitted type. Six vertices have degree two and the two bridge endpoints have degree three. The joining edge belongs only to the boundary of the unbounded face. That boundary is the union of the two square boundaries and the bridge, so it is not a cycle graph. Euler's face-count formula, the third assertion, remains correct.

Replacing the assumption by **2-connected** repairs the first two assertions. Here 2-connected means that the graph has at least three vertices and remains connected after any one vertex is deleted. A bridge is impossible in such a graph, so each edge lies on a cycle and has different faces on its two local sides. A repeated vertex in the boundary walk of a face would also contradict 2-connectivity: join two distinct occurrences by an arc in the face and close that arc to the repeated vertex through their two incident sectors. The resulting Jordan curve meets the graph only at that vertex and separates some incident edges from others. A path joining those edges in the graph with that vertex deleted would have to cross the Jordan curve. Thus a face boundary cannot repeat a vertex. The connected plane graph has one boundary walk for each face, so that boundary is a cycle. These facts justify the source's oriented-face arguments under the repaired hypothesis.

## 4. Repair of the particular graph used in Lemma 2.17

Retain all assumptions and notation of source Lemma 2.17. Thus `Gamma_1, Gamma_2, Gamma_3, Theta` are cycle subgraphs of a plane graph; the bounded faces `D_i` of the first three have pairwise disjoint closures; every vertex of `Theta` belongs to at least one `Gamma_i`; and `Theta` is oriented. Suppose that `I` and `J` are distinct oriented edges of `Theta`, each going from `Gamma_1` to `Gamma_2`. Their tails are distinct and their heads are distinct, since an oriented cycle has one incoming and one outgoing edge at each vertex.

Let

    G_1 = Gamma_1 union Gamma_2 union I union J,
    G_* = Gamma_1 union Gamma_2 union Theta.

Both graphs are 2-connected. For `G_1`, deleting a vertex from one boundary cycle leaves that cycle connected and attached to the other by at least one of the two joining edges; deleting any other vertex cannot disconnect the graph. For `G_*`, use the following elementary fact: the union of two 2-connected graphs sharing at least two distinct vertices is 2-connected, because after deleting any vertex their connected remainders still share a vertex. Start with `Theta`, attach `Gamma_1` at the two distinct tails, then attach `Gamma_2` at the two distinct heads.

The graph `G_1` has four faces. Two are `D_1,D_2`. The closed disk bounded by `Gamma_3` lies inside one of the other two: it is disjoint from `G_1`, since any crossing of `I` or `J` with `Gamma_3` would be an additional graph vertex in the interior of an edge. Let `F'` be the fourth face. Its closure is disjoint from `Gamma_3`. By 2-connectivity its boundary is a cycle. Orient it with `F'` to the left. Its only edges outside `Gamma_1 union Gamma_2` are `I,J`, and their orientations along this cycle are opposite as transitions between the two vertex labels. Rename them if needed so that `I` agrees with the orientation of `Theta`.

Let `E` be the face to the left of the oriented cycle `Theta`. In **`G_*`**, let `F` be the face to the left of `I`. The elementary inclusion of left faces for subgraphs gives

    F subset E intersect F'.

All face boundaries used here are cycles because the three relevant graphs `Theta,G_1,G_*` are 2-connected. The fourth cycle `Gamma_3` has been omitted precisely because its connectivity to `Theta` was not assumed in the source. This omission does not change the relevant face: `Gamma_3` is disjoint from the closure of `F'`.

Orient the boundary cycle of `F` with `F` to the left. Every vertex on this boundary lies on `Gamma_1` or `Gamma_2`. For vertices originating on `Theta`, this follows from the source's vertex hypothesis and the absence of `Gamma_3` from the closure of `F'`; other vertices already lie on one of the first two cycles. The boundary contains `I`, a transition from label 1 to label 2. A cyclic list of these two labels must also contain a transition from label 2 to label 1. Let `K` be that oriented edge. It cannot belong to either `Gamma_1` or `Gamma_2`, so it belongs to `Theta`.

The face of `Theta` to the left of this orientation of `K` contains `F`. It intersects `E`, hence equals `E`, because distinct faces of `Theta` are disjoint. Therefore the orientation of `K` agrees with `Theta`. It is the required edge from `Gamma_2` to `Gamma_1`.

This proves precisely the conclusion of source Lemma 2.17 under its original hypotheses while using the repaired face-boundary theorem. It also covers the polygonal graphs used in the proof of Proposition 2.10. There is no need to add transversality, connectedness of the fourth cycle to the other cycles, or a new premise on the Euler angular flow.

## 5. Consequence for the literature citation

The literal general graph proposition is false, and the literal switching formula does not describe semiflow path spaces. The displayed correction and the specific 2-connected subgraph argument remove these two issues from the route to Theorem 3.1. They are not evidence that recurrent aperiodic orbits exist for a continuous flow on the sphere. The independent audit of this narrow repair is complete (A392). A360's other ingredients, including Dini scattering, the Jacobian cocycle, exclusion of closed actual vortex lines and the countable saturation, are separate from this source check.

Dependencies: elementary Jordan separation for polygonal plane graphs; the indicated actual Bochi-Morris manuscript. No numerical computation or formal build is used. The graph example is an explicit counterexample to a source lemma, not an Euler field.


## Independent source and proof checks

The actual PDF pages6 and10 were independently rendered and read. The retained images show the constant argument in Definition2.3 and the connected, minimum-degree-two hypotheses in Proposition2.12. The source text of the proof of Theorem3.1 uses time t for the continuation, confirming the needed correction. No claim that the entire source proof has now been independently reconstructed is made.

For the barbell graph, V=8 and E=9, so Euler gives three faces. The bridge has the unbounded face on both sides; its membership in only one distinct face contradicts the printed item(ii). Its outer boundary has degree three at the bridge endpoints, contradicting item(i). For the local repair, the distinct directed tails and heads make G1 2-connected after deletion of every vertex. Attaching each boundary cycle to Theta along two vertices makes Gstar 2-connected as well. Pairwise disjoint closed disks and the graph-edge intersection rule put the third closed disk wholly in one open face of G1, disjoint from the closure of the selected other face. Thus all face boundaries actually used in the repaired argument are cycles. The cyclic label change supplies the reverse directed edge.

A389 gives a separate elementary proof of exactly the sphere-flow recurrence statement used by A360. This source correction therefore adds no Euler regularity or dynamical premise. These are source-level counterexamples, not counterexamples to the target Euler conjecture. Rendering was solely to distinguish printed statements from extraction errors; no numerical experiment was performed.
