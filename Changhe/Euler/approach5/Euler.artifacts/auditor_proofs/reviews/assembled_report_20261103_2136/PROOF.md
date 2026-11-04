# Notes126-127: historical scope, a topology erratum and the flat-field transfer

## 1. Exact object and evidence

This is an audit of coordinator report pin f4522a08e3ac97f0aa3f3f8433c42061327a2c43d30a59f7549cbb01ead6d7c8, 6767 lines, assembled21:35Z on2026-11-03. The predecessor is pin02789ff7, approved at its stated scopes by A2384. The five complete report and companion differences were read. The report difference has26866 characters, ASSUMPTIONS23023, THEOREM_ATTEMPTS8843, PROOF_OBSTRUCTIONS3383 and README0. Their full source bytes, hashes and differences are retained in verification. The complete foundation blocks2A,2B,2C,2D are byte-identical to the approved predecessor, as recorded in the team records.

The front, main text and AppendixA occupy lines1-5190 of this pin. AppendixB begins5191, C6588 and D6733. The new rows are reviewed below at their exact hypotheses. This does not issue blanket approval of AppendicesB-D or of unrestricted nonexistence. Two topology wording corrections are necessary for an unqualified restatement. The old auditor proof has also been corrected openly, with its original bytes pinned in the team records. No computation was needed.

## 2. The C19 topology statement and the auditor's erratum

Let c>0, omega be real, U be C1 on R3, divergence free and uniformly o(|y|). Put B=(cI-omega J)y+U, J(x,y,z)=(-y,x,0), and let Phi be its flow. Let N be a nonempty compact domain with C1 boundary strictly outward for B, with Phi_-t(N) contained in intN for every t>0. Set A=intersection_(t>=0)Phi_-t(N), and V=union_(t>=0)Phi_t(intN). Let E be the points of boundaryN whose positive orbits are bounded.

B has linear growth, so its flow is complete. Outside a sufficiently large ball, y.B>=c|y|^2/2; a positive orbit that reaches that exterior escapes radially. On boundaryN minus E, the first-hit map Q to a sufficiently large sphere is C1 and locally a diffeomorphism by transversality. A boundary orbit cannot reenter N, since Phi_t(x) in N would imply x in Phi_-t(N) subset intN. This also makes Q injective. Its domain is open, so E is closed and Q is an open embedding.

For each positive-genus component Sigma of boundaryN, the image of H1(Sigma minus E;Z/2) in H1(Sigma;Z/2) is isotropic: two compact curves in Sigma minus E have the same intersections after Q, while the intersection pairing on the sphere vanishes. If E intersect Sigma lay in an open disk, its compactness would put it in a closed disk inside it; the complement contains intersecting homology generators. This contradicts isotropy. A finite set lies in an open disk by thickening an embedded finite tree. Hence E intersect Sigma is infinite and is contained in no open disk of Sigma. This conclusion is componentwise and conditional on positive genus. There is no general assertion that E is infinite for spherical boundaries.

The trace V intersect S_R equals Q(boundaryN minus E), by following a point in V backwards to its boundary crossing. If Q covered S_R, its domain would be compact, open and closed in boundaryN and connected, and thus a spherical boundary component. Therefore, if NO component of boundaryN is a sphere, the trace is proper. Since divB=3c and V is nonempty, open and invariant, volume(Phi_tV)=exp(3ct)volume(V) forces volume(V)=infinity. This gives nonempty traces on every large sphere. Properness and connectedness of the sphere then make boundaryV meet every such sphere. The complement is closed and invariant in all cases; its unboundedness here uses the no-sphere hypothesis. No positive-volume conclusion for the complement follows.

The original item5 in auditor_proofs/proofs/basin_boundary_topology/PROOF.md omitted that hypothesis before asserting unboundedness. It was false as written. Take U=0, P=0, c>0 and any omega. The exact profile equation holds, Phi_t(y)=exp(ct)exp(-omega tJ)y, and a closed ball N centered at0 traps the backward flow with A={0}. Every boundary point escapes, so E is empty, V=R3 and its complement is empty. This counterexample satisfies even decay. It refutes the unconditional topology sentence, not the nonexistence conjecture about nonzero profiles.

The old full proof is pinned as in the team records. The corrected standalone statement and volume paragraph now repeat the no-sphere hypothesis, and include this counterexample. Source Proposition2.2 and the original A189 ledger already had the hypothesis. The source Sections1-2 were read again; the correction does not change their actual theorem. In the new report row, write explicitly: for every positive-genus component Sigma, E intersect Sigma is infinite and lies in no open disk of Sigma.

## 3. C21 needs the entire regular-attractor family

Assume a C2 Euler profile with uniformly sublinear U, 0<c<1/2 and arbitrary omega. Let calA be the nonempty family of ALL regular basic hyperbolic backward attractors in the exact A115/CO9 class, and K=R3 minus union_(A in calA)W(A). The class, its basin disjointness and its almost-everywhere alternative are dependencies, not assertions about arbitrary attractors.

Each W(A) is open and fully invariant; different basins are disjoint. Hence K is closed and invariant. A boundary point of W(A) belongs to no other basin, because that open basin is disjoint from W(A). Thus K contains every basin boundary. A087 supplies a torus trapping boundary for one chosen A, and Section2 makes its basin boundary meet every sufficiently large sphere. So K does too.

Backward orbits are bounded by radial trapping. Their limit sets are nonempty compact invariant subsets of K for points starting in K. Every regular attractor lies in its own basin, so these limits meet no A in calA. A115 says that, outside a null set of vortical points, a regular backward limit lies in one of the regular basins, or one has the carrier-zero or vorticity-zero alternative. Exhaustiveness excludes the first alternative on K. Thus almost every vortical point of K has the latter two alternatives. K may be null or contain no vortical points.

The row's phrase a nonempty family can be read as an arbitrary subfamily. Under that reading the last inference is unsupported: a basin of an omitted regular attractor would lie in K and retain the regular alternative. This is a logical loss of a hypothesis, not an exhibited Euler profile with several such attractors. Therefore the arbitrary-subfamily version is OPEN, not declared false by an unconstructed example. Restore ALL regular basic hyperbolic backward attractors in the stated class. The auditor's original standalone proof referred to the exact A115/CO9 family; ALL is now explicit, with the old bytes preserved.

## 4. The other historical rows

For C23(c), let U be C1, bounded, divergence free and tending uniformly to0, c>0, and F open or closed and invariant under the full flow. The already proved continuous scattering map S satisfies S(Phi_t x)=exp(t(cI-omega J))S(x), |S(x)-x|<=M/c, a vanishing sharper error at infinity, and |S^-1(E)|=|E|. Put K0=S^-1(0), C_F=S(F minus K0), Pi_F=C_F intersect S2. The nonzero linear orbits meet S2 once; C_F is its twisted cone. These sets are sigma compact and measurable. The bounds on |S(x)-x| give the two vanishing absolute-distance errors. For lambda>1, the F annulus from rho to lambda rho maps into the cone annulus from rho-M/c to lambda rho+M/c. Its volume is area(Pi_F) times the difference of the cubed radii, divided by3. The preimage identity gives upper annular density at most area(Pi_F)/(4pi). If this area is0, the cone and its preimage are null; K0 is null too. Strictly positive large radii are retained. No infinite-jet conclusion for merely C2 U is added.

For B16, let U be C2 and P be C1 satisfying the profile equation; it implies P is C2. Put S=symDU, Omega=curlU, n=Omega/|Omega|, sigma=n.Sn and beta=Sn-sigma n on {Omega!=0}. Differentiating the profile and using the skew part of DU annihilating Omega gives

    B.grad sigma=|beta|^2-sigma^2-sigma-n.D2P n,
    B.grad log|Omega|=sigma-1.

For a compact invariant probability giving full measure to {Omega!=0}, bounded truncations of log|Omega| prove int sigma=1 without assuming its logarithm integrable. All other displayed integrands are bounded on the compact support. Invariant integration therefore yields

    int (|beta|^2-n.D2P n)=2+int(sigma-1)^2.

The componentwise equation for S also integrates to int[S+S^2+A^2+omega(JS-SJ)+D2P]=0, with A=skewDU. Variation of n has no role in this Cartesian matrix integration. The source's contrary remark was correctly REFUTED by A120. Axial affine solutions with nonzero constant vorticity attain the scalar equality but do not decay. The complete standalone directional-moment proof, including the truncation justification, was reread and pinned.

For LIT04, C1 divergence-free uniformly sublinear U and c>0 give complete B-flow and bounded negative orbits. If C1 w satisfies div(Bw)=0, then w(x)=exp(-3ct)w(Phi_-t x); boundedness on the compact orbit closure forces w=0. Signed w is allowed. This is not a result about singular invariant measures or other adjoint eigenvalues.

For A033, R_t=exp(omega tJ) and V(t,y)=R_t U(R_t^-1 y) solve the nonrotating, time-dependent similarity equation. For omega!=0 its period T=2pi/|omega| need not be minimal. Writing a similarity characteristic as R_t eta(t) gives eta'=B(eta), so its period map is Phi_T^B. Periodicity of coefficients does not imply almost-everywhere convergence to a fixed or periodic characteristic. The Liu Theorem7.3 dynamical condition remains necessary in the quoted conditional implication. The report now correctly rejects the opposite inference, already REFUTED by A012. The unchanged original manuscript audit remains the dependency for the exact Liu theorem, not a new claim to have reread its entire manuscript here.

Finally A105 left completeness of the scalar-moment test-vector list OPEN. The new historical parenthesis preserves that status rather than asserting exhaustion of Euler coupling identities.

## 5. The Theory Agent C C65 transfer and R3 sentence

The new C65 row is checked against A2375-A2379 and the complete standalone audit, pinned here. For every0<c<1/2 and real omega it constructs smooth local axisymmetric carrier fields flat at a specified off-axis point with polar angle in(0,pi/2). Both satisfy divV=0, k=0, X.gradV=-LV and X cross W=aV. Their one-sided functions exp(-1/|theta-theta0|), set to0 on the other side, have respectively T=tr((DV)^2)>=0 and <=0, strictly on their nonzero sides. They give endpoint sharpness of sqrt2 for the reverse strain estimate for every finite C0>=0, because |W|/|symDV| tends to sqrt2 while |V|/|symDV| tends to0.

Neither S nor P is supplied. These are flat points of V, not realized common-flat-orbit configurations satisfying the full C60 setting. The negative-sign field cannot satisfy all the additional hypotheses of C61; the positive-sign full setting remains OPEN. The AppendixA row, Section10, O12 and T38 retain these exclusions. Thus their mathematical transfer is correct. The prior O12 precision request still applies: the endpoint equivalence with T>=0 is for C0=0, as explicitly stated in the main text and table.

The rewritten R3 sentence retains 2/5<c<1/2, both natural bounds, C1_loc convergence to the tail, and C^(2,1) regularity near the scattering direction of an escaping lower-window W2 trace. Under the already audited B59-B61 and B63-B64 statements that direction is a finite-jet T0 point. The edit changes no premise, conclusion or open status.

## 6. Verdict and limits

The corrected C19 componentwise and no-sphere conclusions, the exhaustive-family C21 theorem, the other historical rows at Section4's scopes and the C65/R3 transfer are confirmed. The old auditor's unconditional complement-unboundedness sentence is refuted by U=0; its correction is proved in Section2 and preserved transparently. The arbitrary-subfamily C21 classification is not established.

Unqualified assembly approval for pinf4522a08 is withheld pending the explicit C19 and C21 wording corrections. The rest of its delta agrees with the approved predecessor at the scopes above. No general common-flat-point exclusion, local Euler realization of the new carrier fields, blanket historical appendix approval or unrestricted smooth decaying arbitrary-helicity, arbitrary-rotation theorem follows. This is an audit of a changing report, not evidence that the main conjecture has been resolved.
