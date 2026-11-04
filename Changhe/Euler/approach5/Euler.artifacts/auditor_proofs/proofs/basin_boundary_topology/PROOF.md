# The topology of a backward-attractor basin at infinity

## Statement and assumptions

Let B(y)=(cI-omega J)y+U(y) on R3, where U is C1, uniformly o(|y|), c>0 and omega is real. Let Phi be the complete B-flow and Psi_t=Phi_{-t}. Let N be a compact domain with C1 boundary, B strictly outward there, and Psi_t(N) contained in int N for t>0. Set A=intersection_{t>=0} Psi_t(N) and let V be its backward basin. Fix R0 such that |U(y)|<=c|y|/2 for |y|>=R0, and choose R>R0 with N inside B_R.

Let E be the points of boundary N with bounded forward B-orbit. For x outside E on that boundary, let Q(x) be the first crossing of S_R by its forward orbit. Then:

1. E is closed and Q is a C1 embedding onto an open subset of S_R.
2. On any genus-g boundary component Sigma, g>=1, the image of H_1(Sigma minus E; Z/2) in H_1(Sigma; Z/2) is isotropic for intersection and has dimension at most g. Thus E intersect Sigma is infinite and is contained in no open disk of Sigma.
3. V intersect S_R equals Q(boundary N minus E). If no boundary component of N is a sphere, this is a proper open subset of S_R for every such R. If also div U=0, it is nonempty and boundary V meets every such sphere. In particular boundary V is then unbounded.
4. Every x in E has a nonempty compact forward limit set contained in boundary V and disjoint from N.
5. If additionally div U=0, V has infinite volume. Its complement is closed and invariant. If no boundary component of N is a sphere, the complement is unbounded. No positive-volume assertion about that complement is made.

## Radial escape and boundary holonomy

For |y|>=R0,

    d/ds |Phi_s y|^2=2 Phi_s y dot B(Phi_s y)>=c|Phi_s y|^2.

Every forward orbit reaching this exterior region escapes, crossing each larger sphere exactly once and transversally. Backward orbits are bounded. Linear growth of B gives completeness in both directions.

A forward orbit starting on boundary N never enters N again: if Phi_s x belonged to N for s>0, then x would belong to Psi_s(N) subset int N, a contradiction. Therefore two such boundary starting points cannot lie on the same forward orbit. The crossing time is C1 on boundary N minus E by the implicit-function theorem and sphere transversality. The complement of E is open, so E is closed. Holonomy between the transverse boundary and sphere is a local C1 diffeomorphism; injectivity just proved makes it an open embedding Q.

## Intersection obstruction

Two transverse closed curves in Sigma minus E have exactly the same intersections as their Q-images on S_R. The mod-two intersection pairing on S2 vanishes, so every such pair has even total intersection. Every homology class in the open surface Sigma minus E can be represented by a finite union of closed curves, and representatives can be perturbed inside that open surface to be transverse. Hence their images form an isotropic subspace in the 2g-dimensional symplectic vector space H_1(Sigma; Z/2), of dimension at most g.

If E intersect Sigma were contained in an open disk, compactness would put it in a closed disk inside that disk. The complement is a genus-g surface with one boundary circle, containing two curves with intersection one. This contradicts the previous paragraph. Every finite subset of a connected surface lies in an open disk: join its points by an embedded finite tree and take a small disk neighborhood. Therefore E intersect Sigma is infinite.

## Basin traces and boundary limits

The nested trapping domains converge uniformly to A in the following sense: every neighborhood of A contains Psi_t(N) for all sufficiently large t. Otherwise a compactness argument gives a point in their intersection outside that neighborhood. Thus V=union_{t>=0} Phi_t(int N), an open set invariant under the full B-flow; it contains N.

For z in V intersect S_R, follow its backward orbit to its first crossing x of boundary N. Its intervening forward orbit has no earlier S_R crossing because radial escape prohibits a return. Thus Q(x)=z. Conversely every Q(x) belongs to V by invariance. This proves the trace equality.

If Q covered the whole sphere, boundary N minus E would be homeomorphic to the compact connected sphere. It would be both open and closed in boundary N and would be one whole boundary component, a sphere. This is impossible under the no-sphere hypothesis. Nonemptiness of the trace under div U=0 follows from the volume argument below. No claim of nonemptiness without that extra hypothesis is needed here.

For x in E, its forward orbit is bounded and is disjoint from N for positive time. Its forward limit K_+(x) is nonempty, compact and invariant and is contained in closure V. If some q in K_+(x) belonged to V, then a backward iterate of q would be in int N. That iterate still belongs to K_+(x); the forward orbit of x would consequently enter int N at large times, a contradiction. Thus K_+(x) is contained in boundary V, which is disjoint from N.

Now assume div U=0, as in C19. Then div B=3c>0 and volume(Phi_s V)=exp(3cs) volume(V). Since V is open, nonempty and invariant, its volume is infinite. For every R it has a point outside B_R, whose backward orbit enters N. The intervening crossing of S_R lies in V. If no boundary component of N is a sphere, the trace is proper; since S_R is connected, S_R then meets boundary V. The complement of V is closed and invariant in all cases, and meets every large sphere under this no-sphere hypothesis.

For an Euler regular basic backward attractor, A087 supplies a connected trapping domain with one torus boundary. All these conclusions apply. They do not exclude a basin whose complement is a single proper line; the conditional completion A181 has precisely that form if its plug hypothesis is supplied.

## Exact invariant-region distribution identity

Let now V be any measurable full-flow invariant set and assume div B=d constant. For f in C1_c(R3), change of variables gives

    integral_V f(Phi_s y) exp(ds) dy=integral_V f(y) dy.

Differentiation at s=0 yields integral_V(B.grad f+d f)=0. Hence

    div(1_V B)=d 1_V,     B.grad(1_V)=0

as distributions. In particular div(1_V B)=0 is false when d>0 and V has positive volume. The example V=R3, B=cy already refutes it.

For a smooth Euler profile set q=|U|^2/2, A0=cI-omega J and d=3c. The local energy identity is

    div(Bq+PU)=(5c-2)q.

Using U=B-A0 y and the preceding invariant-region identity, for every compactly supported C1 cutoff chi one obtains exactly

    integral_V [(5c-2)q+dP+(A0 y).grad P] chi
      = -integral_V (q+P) B.grad chi.

No regularity of boundary V is needed for this formula, since all differentiated products are locally integrable and chi is compactly supported. Letting chi approach one globally would require convergence and control of the right side. It does not follow just from invariance.

## Audit result and limits

The two topology propositions in Theory Agent C in the team records Section 2 are CONFIRMED as A189 under their submitted divergence-free hypotheses. The false zero-divergence equation in Section 3.3 is REFUTED as A190 and replaced by the exact identity above. Its following energy integrand is consistent with the corrected formula. The formal tail-to-basin correspondence in Section 3.5 is not a theorem established by this audit.

## Statement erratum, 2026-11-03T21:40:29.641112+00:00

The original item5 omitted the no-sphere hypothesis before asserting that the basin complement is unbounded. That unconditional sentence was false: U=0, P=0 and B=(cI-omega J)y with c>0 have complete flow Phi_t=e^(ct)exp(-omega tJ)y. For a closed ball N centered at0, the backward attractor is0, E is empty and V=R3. Its complement is empty. The corrected item5 and volume paragraph now state the missing hypothesis. A189's original ledger and the source Proposition2.2 already retained this hypothesis. The original full proof is preserved in the team records. This erratum does not supply or require a nonzero Euler profile.
