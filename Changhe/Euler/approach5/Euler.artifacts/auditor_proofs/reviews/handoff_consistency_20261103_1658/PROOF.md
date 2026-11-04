# Consistency of the literature handoff and coordinator summaries

## 1. Scope and source record

The eight files in the team records were pinned at the recorded UTC time and read completely. They are the literature review, preprint audit, counterexample audit, two short literature handoff files, and the coordinator's README, theorem attempts and proof obstructions. This is a consistency audit against the already checked mathematical proofs. It does not independently reprove every historical result mentioned in these long files. Supplementary pins record the exact CO6 and CO56 source statements and the earlier independent Kelvin proof.

The main conjecture, for decaying C2 profiles at every angular speed and 2/5<c<1/2 without a helicity premise, remains OPEN. Newly confirmed results require routine status updates; older, weaker valid theorems remain valid.

## 2. The actual Kelvin law cannot be retained by a nonzero compact-velocity model

Let O be a connected open subset of R3, U in C2(O;R3), c and omega real, J a fixed skew rotation generator, A=cI-omega J, B=Ax+U and q=|U|^2/2. Let Phi_t denote the local B flow. A single-valued C1 pressure satisfies

    (1-c)U+(B.grad)U+omega JU+grad P=0

if and only if every closed piecewise C1 curve gamma satisfies

    integral_(Phi_t gamma) U.dx = exp((2c-1)t) integral_gamma U.dx

on its intervals of existence. Indeed, for beta=U.dx,

    Lie_B beta-(2c-1)beta
      = [(B.grad)U+(1-c)U+omega JU+grad q].dx.

The equation makes this d(q-P). Conversely the circulation law makes every closed-curve integral of this form zero. Path integration gives a single-valued primitive F, and P=q-F. No incompressibility, completeness, decay, or simply connected domain is needed for this equivalence. If one tests only contractible curves, the conclusion is local and pressure periods must still be checked.

In particular, take c>0, U in C_c^infinity(R3;R3), div U=0. If U satisfies that circulation law, then U=0. To prove this additional statement, the equivalence gives the full profile equation. Its curl gives

    [B,Omega]=-(1+c)Omega,    Omega=curl U.

The field B has at most linear growth and bounded derivative, so its flow is complete in both directions. Cauchy transport preserves the open set E={Omega!=0}. Since div B=3c, its volume satisfies |E|=exp(3ct)|E| for every t. Compact support of Omega makes |E| finite, hence |E|=0 and Omega=0. Incompressibility then gives Delta U=0 componentwise. A harmonic compactly supported function vanishes. This proves the claim for every finite omega.

The pinned THEOREM_ATTEMPTS T9 says that the decoupled pair retains the circulation law. Read as the law for U.dx, this is REFUTED. The compactly supported nonzero U in the model cannot have that law. The already audited CO6 source makes the essential qualification described next.

## 3. The correct law for an independent transported vorticity

Let div B=3c and let an independent C1 field W satisfy div W=0 and [B,W]=-(1+c)W on R3. For the volume form vol put w=i_W vol. Then

    d w=0,    Lie_B w=(2c-1)w.

The first equality is incompressibility of W; the second follows from the bracket identity and Lie_B vol=3c vol. Since R3 is contractible, w=d beta for some one-form beta. Consequently

    d[Lie_B beta-(2c-1)beta]=0,
    Lie_B beta=(2c-1)beta+d g

for a scalar g. This gives the circulation law for beta, as well as the associated conformal and helicity form identities. It does not identify beta with U.dx. Such an identification would impose d(U.dx)=i_W vol, precisely the missing coupling W=curl U.

The pinned CO6 source states this qualification correctly, as does PROOF_OBSTRUCTIONS O4. Restore it in T9: use “the circulation and form identities for a primitive beta of i_W vol.” The energy identity for U still does not follow.

T9 also attributes a Lorenz-type backward attractor to the construction cited at A066. That audit established the constructive core and trapping region, not the stronger attractor assertion. Later B24/A252-A253 supplies the stronger construction for its stated parameter range, which includes the campaign interval. Thus either replace “attractor” by “trapping region” in the A066 sentence or cite the later theorem and its range. No new attractor theorem is certified here.

## 4. A cluster-set assertion is stronger than the proved ratio inequalities

Use the tail notation E=|V|^2, S=P2-E/2 and R=E/|S| where S is nonzero. Under the exact common-flat-point and punctured-neighborhood sign hypotheses of A1609-A1617, the strict uniform-margin exclusions imply the necessary conditions

    limsup_(x->x0, S(x)!=0) R(x) >= 2/3,
    liminf_(x->x0, S(x)!=0) R(x) <= 2.

For example, if the limsup were below 2/3, a number strictly between them would supply the excluded uniform upper bound on a small punctured neighborhood. The other implication is identical with liminf and a lower bound above 2.

These inequalities do not say that every cluster value belongs to [2/3,2]. On 0<r<exp(-1), the smooth punctured function

    R(r)=3/2+sin(log(log(1/r)))

has cluster set [1/2,5/2] and satisfies both displayed inequalities. This is a counterexample to the logical inference, not an Euler profile or a tail construction. The README and final priority paragraph of PROOF_OBSTRUCTIONS should state the two inequalities explicitly. A claim that the entire cluster set is contained in [2/3,2] is REFUTED as a consequence of the cited results.

## 5. The finite-jet set and the common-flat residual have different quantifiers

The tail set is

    T0={x in supp(curl V) intersect S2 : V(x)=DV(x)=P2(x)=0}.

A point of T0 is defined by finitely many equalities. This definition does not say that V or S vanishes to infinite order. Here infinite order means that every derivative at the point vanishes, with the corresponding smoothness hypothesis retained.

The verified global results used in the README imply the following. For an actual nonzero helicity-free profile in the natural tail class, assume V is smooth near all of T0. If all velocity zeros there have finite order, the finite-order theorem gives U=0, a contradiction. More generally, if S has finite order at each point of T0 where V vanishes to infinite order, the extended global theorem also gives U=0. Taking the contrapositive, a nonzero such profile has at least one point of T0 where both V and S vanish to infinite order.

This is an existence conclusion about a residual witness. It does not make every point of T0 common-flat, and it does not separately exclude each finite-order T0 point. Replace the final README identification by: “For a nonzero profile with V smooth near T0, at least one supported point of T0 must have both V and S vanish to infinite order. Excluding such witnesses remains open.” Retain the alternative where the requisite tail smoothness is unavailable. No pointwise strengthening is confirmed by this audit.

## 6. CO56 needs the derivative bound and punctured sign geometry

For the specific CO56 theorem write a=1-2c, b=2(1-c), q=b/a, eta=1/q. Work in its tail setting near a common-flat point x0, with k=X.V=0 on a flow box, Gamma the X orbit of x0, rho the distance to Gamma, and S<0 off Gamma. Put H=|S| and R=E/H. The verified flux identity is

    div(M_R grad H+H grad R)=0,
    M_R=((1-eta)R-1)I+eta(V tensor V)/H.

Its eigenvalues are R-1 in the V direction and (1-eta)R-1 in transverse directions. The CO56 exclusion assumes some delta>0 and M<infinity with

    rho |grad R| <= M,

and either R<=1-delta or q/(q-1)+delta<=R<=M on the punctured flow box. After a fixed sign change the principal matrix is uniformly elliptic. The derivative bound controls the rescaled drift H grad R on balls of radius comparable to rho. Harnack chains then contradict flatness of H. Thus the derivative hypothesis has an explicit role and cannot be silently removed from this argument.

The short README phrase “under a ratio bound” is insufficient as a theorem statement. Restore “under the stated ratio bounds, scaled derivative bound and S<0 off the common orbit.” Ratio-only exclusion by CO56 remains OPEN; the source's Section2 explicitly retains that gap. Later LIT259 supplies a different theorem with a positive bounded W1,2 extension on the full transverse disk. That additional full-disk hypothesis also must be stated when using the later theorem. Neither result is a bare-decay Liouville theorem.

## 7. Other handoff updates and limits

The pinned short literature handoffs already repair the earlier LIT253-LIT255 status, Hardy-pressure pending clause and coupled-UC solution spaces. LIT260-LIT262 were subsequently confirmed at A1756-A1767, so their labels may be refreshed at those exact scopes. The new actual-source Chae-Tsai bounded alpha=0 endpoint defect is proved separately in the team records; Section5.4 of the literature review needs that qualification. It supplies no target counterexample.

The README's nonlinear-weight constants are valid but have been improved by C58/A1720-A1728. Its former “optimality pending” wording can be updated for the strict-weight optimization only. The new closed-endpoint C59 submission has not been audited here. The report's other pending source-space and pressure-margin corrections remain A1705-A1706. New B and C integration notes require a separate current-file diff audit.

No further material mathematical inconsistency was found in this complete eight-file reading. This sentence certifies the review performed, not every theorem in the files independently. Source hypotheses, pressure normalization, actual-versus-independent vorticity, and global-versus-pointwise quantifiers remain explicit. The main conjecture is OPEN.
