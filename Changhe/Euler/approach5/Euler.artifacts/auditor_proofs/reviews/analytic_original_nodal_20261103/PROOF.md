# Analytic original vorticity and the nodal condition

Status: full independent audit of LIT208, with its external component-finiteness input checked in the actual primary manuscript. This theorem does not assume a smooth tail.

## 1. Exact hypotheses and conclusions

Fix 2/5<c<1/2 and finite real omega. Write Jx=(-x2,x1,0), A=cI-omega J, p=(1-c)/c, a=1-2c, q=2(1-c)/a>6. Let U in C2(R3;R3), P in C1(R3), with a finite constant C, satisfy

    div U=0, (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    U.Omega=0, Omega=curl U,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1).

Let Xi:E -> D=R3 minus0 be the actual C1 scattering diffeomorphism. For the actual tail set W=curl V, k=(Ax).V, S=P2-|V|^2/2, Z=int_D{k=0}. Supports and closures below are relative to D.

Local theorem: if V(x0)=0, x0 in supp W, and x0 is outside closure Z, then Omega is not real analytic on any neighborhood of Xi^(-1)(x0).

Global conditional theorem: if Omega is real analytic on R3 and the additional nodal condition k=0 implies W=0 holds on D, then U=0. No restriction on omega, angular modes or symmetry is imposed. The helicity and both natural bounds remain hypotheses.

## 2. Verified primary analytic-set input

The primary source is E. Bierstone and P. D. Milman, Semianalytic and subanalytic sets, Publications mathematiques de l IHES67(1988),5-42. Definition2.1 is on printed10. Theorem2.6 on printed11-12 completes a finite analytic family, after shrinking around a point, to one with connected joint sign cells. Corollary2.7 on printed13 and its proof give exactly the needed form: for each ambient point, some neighborhood has only finitely many connected components of its intersection with a semianalytic set.

The actual manuscript was independently downloaded. Section2 through Corollary2.8, including the complete proofs of Theorem2.6 and Corollary2.7, was read. The induction uses analytic preparation, finite root partitions and the one-dimensional sign lemma. Those earlier algebraic and preparation inputs remain external mathematics. This is not a claim to have independently proved the whole paper. The PDF, extraction, hash and actual retrieval time are in the team records.

## 3. From analyticity to finitely many original vortical components

Suppose Omega is analytic on a connected original-coordinate neighborhood M of y0, and not identically zero there. The set T={Omega!=0} is semianalytic: it is the positivity set of the analytic scalar sum_i Omega_i^2. The analytic identity theorem makes T dense in M.

The primary local theorem provides an open neighborhood N of y0 contained in M such that T intersect N has finitely many connected components. Replacing N by its connected component containing y0 preserves the finite count: every connected component of T intersect N lies in exactly one component of N. Open subsets of Euclidean space are locally path connected, so this chosen component of N is open. Density also persists.

The exact identity W(Xi(y))=DXi(y)Omega(y) and invertibility of DXi say that Xi maps T onto the nonzero-W set in its image. A homeomorphism preserves openness, density and connected components. Semianalyticity is used only in original coordinates. No semianalytic preservation or analytic regularity of Xi is asserted.

## 4. The local contradiction, with every pressure hypothesis checked

Suppose the local theorem failed. Choose a connected original ball M inside E, inside the analytic neighborhood, with Xi(M) outside closure Z. Since x0 is supported, Omega cannot be identically zero on M, as that would make W zero on the image neighborhood. Section3 gives a connected smaller N with dense vortical set and finitely many components.

By the confirmed A963 zero-region theorem, k=0 implies W=0 outside closure Z. On each connected open vortical component in Xi(N), k is therefore nonzero. The exact rank and homogeneity identities give

    grad k cross grad S=0, X.grad k=-ak, X.grad S=-qaS,
    grad(S |k|^(-q))=0.

Hence S=D_j |k|^q with one finite constant for each component. The finite maximum of |D_j| and density extend this identity as the bound |S|<=C0|k|^q throughout Xi(N). Since X is bounded on a smaller closed ball, |S|<=C1|V|^q there.

At x0, V=0 makes k=0 and therefore W=0. The actual regularity gives V in C^(1,1/2) locally and the pressure equation -Delta P2=partial_i partial_j(V_i V_j). Since q>2, shrink the ball so C1|V|^(q-2)<=1/8. The full-ball pressure rigidity theorem A1006 applies with alpha=1/2 and epsilon=1/8<1/6. It forces V=0 on a neighborhood, hence W=0 there, contradicting x0 in supp W.

This checks A1008 directly again. The pressure inequality holds on the full ball by density, not merely on selected angular sectors. No pressure normalization beyond the actual P2 is changed, and S(x0)=0 follows from the bound.

## 5. The global contradiction

Assume the global hypotheses and suppose U!=0. If Z were nonempty, the nodal condition would give W=0 on a nonempty open set. The scattering identity then gives Omega=0 on a nonempty original open set. Real analyticity on connected R3 forces Omega=0 everywhere.

Divergence and curl zero imply Delta U=0 componentwise. The velocity bound makes each component bounded harmonic, so the harmonic Liouville theorem makes U constant. Its decay makes that constant zero, a contradiction. Thus Z is empty.

The common supported flat zero theorem A1057 now supplies x0 in S2 intersect supp W with V(x0)=0. It is outside closure Z, so Section4 contradicts analyticity at its preimage. This proves U=0.

## 6. Comparison, limitations and evidence

All six LIT208 sections and its four-section source note were read, together with the complete independent A1005-A1008 proof. Every implication above respects the low C1alpha tail regularity. There is no use of a tail-vorticity flow's completeness or a second derivative of Xi, and no new boundary integral at infinity.

A1165 gives a different local sufficient condition: analytic original vorticity near T0 preimages plus smooth V near T0, without the nodal condition. The present proof instead uses the nodal condition. Correction A1213-A1214: when Omega is globally analytic, the earlier A309 smooth helicity-sign theorem already gives U=0, because Delta U=-curl Omega makes U globally smooth. Thus the global theorem here remains true but has unnecessary premises. The local theorem in Section4 retains its separate value and exact scope.

The primary theorem is an explicit external dependency. No numerical computation, formal build or new model client was used. A focused comparison from the existing configured model agents remains requested; their runtime provider identity is unattested. The main bare-decay arbitrary-helicity conjecture is open.
