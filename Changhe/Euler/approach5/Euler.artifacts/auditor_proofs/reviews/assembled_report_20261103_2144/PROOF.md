# Audit of report Notes 128 to 130

## 1. Sources, statements and scope

This audit checks the mathematical changes from the report pinned as f4522a08 in the preceding audit to d29e24e2, and then to 59817261. The complete SHA256 values, source locations, actual capture times and five source-file deltas for each stage are in the team records and in the team records. Source files are preserved, not replaced by this commentary. The predecessor is auditor_proofs/reviews/assembled_report_20261103_2136/PROOF.md. Its outstanding C19 and C21 wording qualifications are part of the present audit.

The report is about classical rotating Euler profiles on R3. Put Jx=e3 cross x, A=cI-omega J, X=Ax, L=(1-c)I+omega J and a=1-2c. The equation is

    div U=0, LU+DU(X+U)+grad P=0.                  (E)

The target is 2/5<c<1/2, arbitrary real omega, smooth U with U(x) tending to zero at infinity. This audit proves no unrestricted nonexistence theorem. In particular it does not impose finite energy or infer any derivative bound from velocity decay.

The conclusions below are: the harmonic-potential row is correct, the complete invariant-sector formulas cannot extend continuously across the origin, the finite-order compatibility and fixed-product weight rows keep their hypotheses, and the Note130 C19/C21 repairs retain the correct topology assumptions. One reference sentence is false as written: the LIT10 row has no description in Appendix A in either pinned version. The mathematical review of front matter, Sections 0 to 10 and Appendix A of 59817261 is confirmed at the individual scopes, excluding that reference sentence. Appendix B is covered only by the separately cited audits of its components, not by blanket acceptance of its historical text. Newer unpinned edits have no approval from this check.

## 2. Harmonic gradients and the dipole example

Let D be an open subset of R3 and let phi be any real harmonic function on D. Harmonic functions are smooth in D. Set U=grad phi. For every real c and omega define

    P=-a phi-X.grad phi-|grad phi|^2/2.           (1)

Then div U=Delta phi=0, DU is symmetric, and

    grad(X.grad phi)=A^T U+DU X,
    grad(|U|^2/2)=DU U,
    aI+A^T=L.

Differentiating (1) therefore proves (E) term by term. No decay hypothesis, pressure normalization, integration by parts or boundary condition enters this local identity. Adding a constant to phi only changes the pressure by a constant.

For r=|x|>0 take phi=x1/r^3=-partial_1(1/r). This is harmonic away from zero, and

    U=e1/r^3-3x1 x/r^5,
    |U|^2=r^(-6)+3x1^2 r^(-8),
    P=(4c-1)x1/r^3-omega x2/r^3-|U|^2/2.         (2)

To check the rotation sign, Jx=(-x2,x1,0), so (Jx).grad phi=-x2/r^3, while x.grad phi=-2phi. Substitution in (1) gives (2). Thus U decays as r^(-3) and is nonzero, but its norm diverges along every ray toward the puncture. It is not axisymmetric about e3. For example U(e1)=-2e1 and U(e2)=e1, which are not related by the quarter-turn about e3 required by axisymmetry. The dipole is axisymmetric about e1; the Note130 phrase specifying the rotation axis is appropriate. At omega=0, e3 is the fixed reference axis in this statement, not a uniquely determined physical rotation axis.

If a field of this form is defined on all of R3 and tends to zero, every component of U is a bounded entire harmonic function. Harmonic Liouville makes each component constant, and the decay makes the constants zero. This proves exactly the local/exterior example and the entire irrotational conclusion of A038. It does not exclude a whole-space field with vorticity outside a region where it agrees with a harmonic gradient. The Theory Agent A Note A66 independently gives the same calculation; that agreement was checked against (1), not treated as proof by authority.

## 3. Complete invariant sectors and the origin

Here c is in the target interval unless the larger LIT281 range is explicitly stated. Put d=1-c and b=2d. Let D be invariant under F_t=exp(tA) for all real t, and suppose real harmonic f,Q on D satisfy

    X.grad f=-af, X.grad Q=-bQ.

Let V=-grad f/a, U=grad(-f/a+Q) and P=Q-|U|^2/2. Since b-a=1, formula (1) gives precisely this P, so (E) holds exactly. With R_t=exp(-omega tJ), differentiation of both scalar homogeneities gives

    U(F_t x)=exp(-dt)R_t[V(x)+exp(-t)grad Q(x)].  (3)

For LIT273, Q=0 and V is nowhere zero. Hence at any fixed x in its complete invariant sector, |U(F_t x)|=exp(-dt)|V(x)| tends to infinity as t tends to minus infinity. But |F_t x|=exp(ct)|x| tends to zero. There can be no continuous extension of that entire sector field across zero.

For LIT279 and LIT281, Q is nonzero and has negative degree -b. At a point with Q(x)!=0, the identity X.grad Q=-bQ implies grad Q(x)!=0. Fix such a point. As t tends to minus infinity, the norm of the bracket in (3) is at least

    exp(-t)|grad Q(x)|-|V(x)|,

which is at least exp(-t)|grad Q(x)|/2 for all sufficiently negative t. Thus the left side of (3) is at least a positive constant times exp(-(d+1)t) and also diverges toward the origin. This excludes a continuous whole-space extension agreeing with either complete invariant-sector formula. The argument applies also throughout 1/3<c<1/2 for the LIT281 construction. It permits every fixed finite omega: R_t is orthogonal, and no bound uniform in omega is used.

The separate exterior results remain those already proved in A1920-A1923, A1989-A1992 and A2028-A2032. LIT279 has the tail scalar S=Q-|V|^2, not P-|U|^2/2 at finite radius, and the comparison (2/3)|S|<=|V|^2<=2|S| is a tail statement. LIT281 is nonplanar and has every derivative through order four of grad f cross grad S zero at the stated point; no open rank identity follows from that finite jet. For the target range, p=d/c is between 1 and 3/2. The lower bound |U|>=C r^(-p) on a fixed positive angular aperture makes the exterior energy infinite, since the radial lower integral is a positive multiple of integral r^(2-2p) dr.

Infinite exterior energy is consistent with the original target assumptions. The obstruction in this section is origin regularity for the complete invariant-sector formula. It is not a proof that an exterior restriction cannot be matched to a different smooth interior or to vorticity in missing directions. Such a matching remains OPEN. The report phrase "no whole-space extension" must be read with this distinction; the recommended replacement states it explicitly. Earlier descriptions saying no extension is asserted are compatible with this direct origin calculation.

## 4. The reference error in Section 9

At the pinned report's Section 9 table preamble, the report says that full descriptions of its last four lines occur in Appendix A. The first of these four lines is the newly added LIT10 harmonic-potential line. Searching the entire pinned report and inspecting Appendix A shows that LIT10 and its A038 proof are present only in Section 9. The relevant full description is the independent proof at auditor_proofs/proofs/harmonic_potential/PROOF.md and the present Section 2, not an Appendix A entry. Therefore that reference sentence is false for this row. This is an editorial reference defect, not a failure of the harmonic-gradient theorem. It can be corrected by a direct reference to the audit proof, a narrower preamble, or an added Appendix A row with the same assumptions.

The other three new rows retain their established scopes. C63 concerns local fields with no common flat point; they do not settle the flat-point problem. C65 concerns identities that do not involve S or P. No pressure completion was constructed there. The separately completed C66 audit A2404-A2408 now excludes both particular C65 fields from the full setting F, but that result has not yet been inserted in the pinned report. Historical non-construction is not a false statement merely because a newer exclusion is available. No general common-flat-point exclusion is inferred.

## 5. Finite-order compatibility and linear weights

The LIT299 row concerns each 0<c<1/2, integer n>=4, and v>0 outside an explicit set E(c,n) with at most one element. Its transverse pressure gradient (g,0) has g<0. The carrier is the affine coordinate expression X=(cx-vz,cy,1+vx+cz) centered at an equatorial point off the rotation axis. The analytic leading-system functions and the next scalar satisfy the transport equations exactly, while their Poisson residual has transverse order at least n+1. The zero arc is an exact X-orbit arc, the transverse order of V and W is n-1, and the relative support of W is the full neighbourhood. Neither compatibility nor incompatibility at E(c,n) is concluded. These are A2386-A2389 and the proof auditor_proofs/reviews/generic_rotation_compatible_20261103/PROOF.md.

The LIT300 row removes that possible exception for every v>0 by allowing a nonzero g of either sign, with the sign chosen as part of the construction. It does not prescribe an arbitrary negative g or prove negative-gradient compatibility at all rates. The determinant/root-collision proof and the separate c=2/5 case are A2391-A2395, auditor_proofs/reviews/all_rotation_compatible_20261103/PROOF.md. The report explicitly keeps the lack of a full next scalar, all-order convergent correction, zero-rotation construction and global extension. Rotating coordinates permits any prescribed axis at fixed magnitude v; it does not permit an arbitrary position relative to the axis while retaining the equatorial normal form. The appended row and Section 10/O12 text respect these limitations.

The fixed pair of pointwise bounds in the nonlinear-weight row remains lambda_min(sym DU)>=-6/5 and |curl U|^2<=103/100. At this fixed product set, strict positivity of the linear density with a>0 is possible exactly when 0<c<c_lin; the number c_lin is the unique stated root of the explicit irreducible degree-nine polynomial and is approximately 0.447220574. At c_lin there is a nonnegative linear density, unique up to positive scale, but it is zero at nonzero product points and therefore fails the strict-positivity hypothesis of SF.3. For c_lin<c<2/3 even nonnegativity is impossible for this family. These facts are A2291-A2295, A2341-A2345 and A2372-A2373. Renaming this threshold avoids a collision with the different c* elsewhere. It does not change the analytic profile theorem or derive either bound from velocity decay. The report correctly closes only the former fixed-product linear-weight question, not optimality for nonlinear weights or other pairs.

The restored C0=0 endpoint in O12 agrees with the reverse-ratio hypothesis. The restored q!=0 in the historical constant-vorticity discussion agrees with the bracket argument. No new computation was needed: the exact calculations in the separately verified dependency packages were not rerun merely to audit the summary.

## 6. The repaired attractor statements

For C19, U is C1, divergence free, and uniformly sublinear, c>0 and omega is arbitrary. N is a compact backward-trapping neighbourhood with C1 boundary on which B=Ay+U is strictly outward. E is the closed set of points on the boundary whose forward trajectories are bounded. The correct componentwise statement is that E intersect Sigma is infinite and lies in no open disc of Sigma for each positive-genus component Sigma of the boundary. It is not an assertion about positive-genus topology of a union of unrelated components. The no-spherical-component hypothesis is needed for the conclusion that the basin boundary meets every sufficiently large sphere. Infinite basin volume follows independently from div B=3c. The Note130 row now states the componentwise clause and retains the no-sphere clause, agreeing with A2398.

The incorrect unqualified sentence in the auditor's old standalone A189 proof was refuted in A2397 by U=0 and a ball N. The original source theorem and its ledger statement had the no-sphere condition. That erratum and the archived original bytes remain visible. It is not a new counterexample to the correctly qualified theorem.

C21 now uses the family of ALL regular basic hyperbolic backward attractors in the CO9/A115 class, when this family is nonempty. Removing their full basins gives the closed invariant set K containing their basin boundaries and meeting every sufficiently large sphere. Almost every vortical point remaining in K has the stated alternatives beta or gamma. The quantified conclusion uses removal of every regular basic attractor, so the former phrase "a nonempty family" was insufficient. The corrected row agrees with A2399 and explicitly leaves an arbitrary proper subfamily OPEN A2400. It does not assert that K has positive volume or contains any vortical point. C23(c) retains the positive-large-radius and absolute-distance interpretations checked in A2401.

## 7. Verification and exact approval boundary

Both stages' complete five-file deltas were read. THEOREM_ATTEMPTS and README have zero differences. The four foundational blocks 2A to 2D are compared byte for byte with their already audited versions. All nonempty report, ASSUMPTIONS and PROOF_OBSTRUCTIONS deltas were read without skipping the long status histories. The full harmonic-potential proof and the full LIT273/LIT279 independent proofs were read again; the relevant statement, convergence and domain/decay portions of the LIT281 proof were checked against its earlier complete audit. The whole LIT281 middle-jet argument was not newly rerun for this table review. The C63, C65, C66, finite-order and weight conclusions retain their separately completed proofs and evidence.

The mathematical content of front matter, Sections 0 to 10 and Appendix A of SHA256 5981726119ec2242aa910595e7e706fe3cb94e3b2f394ec86e68e531221c1922 is approved at those individual scopes, with Section 9's false Appendix A reference excluded and the exterior-matching distinction in Section 3 explicit. This is a cumulative delta review based on the preceding pinned approvals, not a claim that every historical paragraph was proved anew. The unrestricted conjecture and the listed global extension problems remain OPEN. No approval attaches to a later hash without review.

No numerical job, formal build, network client, server or model invocation was launched for this audit. Collaboration used the existing configured model coordinator and theory-working files, whose provider runtime identity is not independently attested.
