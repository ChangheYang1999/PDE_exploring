# Audit of Note106 and the subsequent source clarifications

Status: the scoped transfers below are confirmed. The whole assembly remains open. The immutable four-file pin and independent differences are in the team records. No new computation is used.

## 1. Pin, dependencies and statement of the audit

The report and its publication copy were identical at capture: 6475 lines, SHA256 2ec8e4b290f913f0a30bbc34265d3e2cd7b5152f507822e11825de6227a0edc6. The four independent differences from Note105 contain 115, 12, 37 and 17 lines respectively. All were read, including the full long summary rows and surrounding Theorem7(f)-(g), T41 and O12 context. Notes106 and A52 were read completely. The source correction to STRAIN_FORMS_NW was independently diffed and read in full.

This is a proof of the exact scope of the changes, using the complete independent reconstructions in upper_pressure_removal_20261103, isotropic_axis_rank_20261103, arbitrary_axial_hessian_rank_20261103, w2_lipschitz_mixed_type_20261103, strain_forms_20261103 and mixed_strain_instances_20261103. It is not a replacement for the unchanged report's full proof inventory.

Throughout, actual profiles satisfy div U=0 and

    ((cy-omega Jy+U).grad)U + (1-c)U + omega JU + grad P=0

on R3. Decay means U(y) tends to0 as |y| tends to infinity. Additional hypotheses remain additional even when their resulting theorems have complete proofs.

## 2. Summary rows and the common-flat-point contrapositive

Rows6 and8 preserve the distinction between regularity, decay and structural conditions. Theorem5 still requires smoothness and one helicity sign per essential basin. Theorem7 still requires zero helicity, the derivative bound and the stated tail condition; its k=0 alternative separately states W.grad S=0 when helicity is dropped. Theorem8 still requires a smallness or integral condition. Their CONDITIONAL labels are appropriate. The shortened constants in row6 are the previously confirmed constants, and the strain alternative imposes no bound on W.

The exact contrapositive in row10 follows as follows. In the helicity-free C2 profile class of Theorem7, assume the derivative bound and that V is smooth on a neighborhood of every point of T0. If U were nonzero and every point of T0 had finite velocity order, Theorem7(e) would give U=0. Thus some point has infinite velocity order. The local theorem used in7(f) excludes any such supported point where S has finite order. Hence at least one point of T0 has both V and S of infinite order. This does not assert that each finite-order point is individually impossible. No smoothness at T0 follows from the derivative bound. The reference to section10(1), rather than10(2), is correct.

The remaining sector sentence in row10 still needs the original global two-sided comparison before it invokes LIT271. Merely dropping the global rank relation from the localized-lower version of7(g) has not been shown to force such a sector. This is the previously requested A2066 qualification, not a new extension of LIT271.

## 3. Axial rank jets and the resonant example

Here are the hypotheses behind the LIT283 insertion. Let 1/3<c<1/2, omega be any finite real number, A=cI-omega J, X=Ax, a=1-2c and b=2(1-c). Let f and Q be analytic harmonic germs near e3 satisfying X.grad f=-af, X.grad Q=-bQ, f(e3)=1 and f_1(e3)=f_2(e3)=0. Put E=|grad f|^2/a^2, S=Q-E and F=grad f cross grad S. In the isotropic transverse case, the independent proof of A2055-A2057 shows that derivatives of F through order5 cannot all vanish. Through order4 they cannot all vanish except at c=5/11, omega=0.

At that exceptional pair the convergent construction A2058 has Q(e3)=22/25 and exact rank order5. With phi=-f/a+Q, U=grad phi and P=Q-|U|^2/2, the scalar homogeneities make the profile momentum equation hold on the invariant exterior cone. The harmonicity gives div U=0. This is the exact local construction A2059. It cannot extend to a whole-space C1 decaying profile: at omega=0 the separately rechecked Theorem2 applies for0<c<1/2 and forces U=0, whereas the germ is nonzero. Thus the coordinator's parenthetical use of Theorem2 is valid.

Combined with LIT282 this proves the negative-definite transverse-Hessian statement in Note106. The later A2093-A2097 proof removes the transverse-Hessian restriction entirely, but preserves every other displayed hypothesis. The report has not yet integrated that subsequent result. In all versions the explicit scalar homogeneities, normalization and axial point must be stated somewhere the short entries unambiguously inherit. Analytic harmonic germs alone are not the confirmed class. No argument produces such an axial point on an arbitrary matching interface.

## 4. Lipschitz Hessians and the Bernoulli normalization

The new C^(2,1) sentences correctly refer to the escaping lower-window W2 trace in the helicity-free profile class with the natural bounds and C1_loc tail convergence. The supported direction is automatic in that class. If V has a Lipschitz Hessian near that direction, the differentiated rank identity and its difference quotient give the contradiction for a nonflat strict-rate trace, while the equality-rate case was already excluded at C2. This proves the finite-jet T0 conclusion for every rate. The argument gives no infinite-order vanishing. Its reduced symbol has opposite-sign eigenvalues on the approach; this rules out an elliptic bootstrap of that displayed system, without excluding other regularity mechanisms. The new wording preserves this distinction. The natural bounds should remain explicit wherever the shortened R3 sentence is read independently.

The two Bernoulli functions differ by a scalar quadratic term. Write X0=cy+U, B=Ay+U, Omega=curl U, h=U.Omega and

    H=P+|U|^2/2+(Ay).U,
    H0=H-c(1-2c)|y|^2/2.

The momentum identity for H0 gives grad H0=-aX0-Omega cross B. Adding acy gives grad H=-aU-Omega cross B. Taking products with Omega and B proves

    B cross Omega=grad H+aU,
    Omega.grad H=-ah,
    B.grad H=-a U.B.

These equations are valid for every omega and require no pressure normalization. The A52 proposed citation to the H0 translation is correct. In particular the report's H must not silently be substituted for H0 in a formula involving X0.B.

## 5. Strain repairs and the precise proposed replacement

The source now lists both SF.5 and SF.6 as certified and explicitly says that a finite grid cannot prove a nonlinear weight necessary. These are the two A2084 repairs. Nothing in the source correction changes a proof or certifies the numerical region beyond those two instances.

The A52 proposed replacement preserves the exact C63 hypotheses and conclusions: U in C2, P in C1, Hb, all omega, both bounds everywhere; either0<c<=9/20, |sym DU|^2<=363/200 and |curl U|<=1, or0<c<=1/2, -lambda_min(sym DU)<=4/5 and |curl U|^2<=7/10. The comparison windows19/45<c<=9/20 and22/45<c<=1/2 are those checked in A2083. This is a comparison with the other specified sufficient criteria, not an optimality theorem.

The proposed SF.2 text restores g in C1, g>=0, g(0)=0, constant a,b, a compact trace-free strain set containing a neighborhood of0 and with maximal positive eigenvalue at least1, and the universal test over every W. At W=0 and arbitrarily small S, nonnegativity forces a>=0; when a=0, the opposite cubic signs force b=0. Testing a direction with quadratic form1 then forces g=0. For a>0 the previously verified logarithmic average yields the stated three necessary thresholds. These statements describe this algebraic family only.

The proposed SF.3 text restores a>0, compact K, M>0, g in C1([0,M^2]), g>=0, g(0)=0 and g'(0)>a/(4(1-3c/2)), with strict positivity on the entire compact product away from(0,0). Near0 its quadratic part is positive; away from0 compactness supplies a uniform lower bound by |DU|^2. The already confirmed cutoff iteration proves U=0. Retain0<c<2/3 and the full Hb profile class. The proposed section3.1 rewrite correctly separates the strain criteria from bounded-vorticity criteria.

## 6. Remaining report qualifications and verification limits

The repairs requested in A2066-A2070 and A2077 are not yet present in this pin: global two-sided comparison before LIT271; the complete SF.2/SF.3 family; the correct location of the C58 power law; full structural hypotheses before the upper-removal closedness assertion; explicit scalar homogeneities for axial germs; and the section3.1 strain row. The new T41 paragraph likewise needs to inherit the full tail equations of its actual-profile setting explicitly if it is quoted as an abstract lemma. The Sobolev range is1<=t<1/(1-rho).

One further useful qualification concerns integrability of the Harnack coefficient. Upper comparison gives a positive lower bound on w=R^(-tau), but does not prove local integrability at common zeros. The Harnack lemma applies on a ball where w is locally integrable. The extremal-set argument shows precisely that this fails near any extremal boundary of a nonconstant potential. Thus write "Harnack applies wherever this weight is locally integrable", rather than wording that could assert this integrability as a conclusion of the upper bound. The local lower comparison supplies boundedness near the common zero set in the vanishing corollary.

Whole-report approval remains OPEN pending these repairs and a complete coverage ledger of unchanged sections. The report's independent foundational rechecks of nonrotating Liouville, smooth coverage and the helicity-sign theorem this shift remain valid. No whole-space nonexistence theorem for unrestricted helicity and arbitrary omega is proved here. Existing configured model collaboration is through the coordinator and theory-owner files; actual provider execution remains independently unattested.
