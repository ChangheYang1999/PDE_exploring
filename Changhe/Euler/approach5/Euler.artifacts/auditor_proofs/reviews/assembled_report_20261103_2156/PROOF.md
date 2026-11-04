# Repair of the harmonic and spiral-sector descriptions

## 1. Exact scope and source comparison

This is the audit of coordinator Note 133, at this report SHA256 f42d627cb8bacb49d478697f5487bf96481695f7007d009443fe721e6a09c0d1, 6792 lines. The baseline is the qualified mathematical approval A2420 of pin 3f495bd8. The complete five-file comparison was read: the only nonempty difference is the report itself; in the team records, THEOREM_ATTEMPTS.md, PROOF_OBSTRUCTIONS.md and in the team records are unchanged. The four foundation blocks are byte-identical, with checks retained in the team records. The source snapshots and exact hashes are in the team records.

The current audit covers the mathematical front matter, Sections 0-10 and Appendix A, lines 1-5209. Historical Appendix B retains its individual audit scopes. This revision repairs precisely the excluded reference sentence A2412 and makes the interpretation of A2411 explicit. No new global nonexistence result is added.

## 2. Harmonic-gradient identity and the new Appendix A row

Let c,omega be any real numbers, Jx=e3 cross x, X=(cI-omega J)x and L=(1-c)I+omega J. For any smooth harmonic potential phi on an open subset of R3 put U=grad phi and a=1-2c. The full profile system is

    div U=0,
    LU+DU(X+U)+grad P=0.

Take P=-a phi-X.grad phi-|U|^2/2. Since DU is the symmetric Hessian of phi,

    grad(X.grad phi)=(cI+omega J)U+DU X,
    grad(|U|^2/2)=DU U,
    aI+(cI+omega J)=L.

These equations prove full momentum directly, and harmonicity gives divergence freedom. The report writes exactly this pressure as

    P=-(1-2c)phi-c y.grad phi+omega(Jy).grad phi-|U|^2/2.

For phi=y1/R^3, R=|y|>0, harmonicity follows from phi=-partial_1(1/R). Its velocity and squared magnitude are

    U=e1/R^3-3y1 y/R^5,
    |U|^2=R^(-6)+3y1^2 R^(-8).

Euler homogeneity gives y.grad phi=-2phi, and (Jy).grad phi=-y2/R^3. Hence the exact pressure is

    P=(4c-1)y1/R^3-omega y2/R^3
        -(R^(-6)+3y1^2 R^(-8))/2.

This matches the new row. The field is nonzero, decays, and is singular at the puncture. It is not axisymmetric about the specified third axis: U(e1)=-2e1 whereas U(e2)=e1, which do not transform into one another under its quarter-turn. The phrase refers to that rotation axis; no assertion denies symmetry about the dipole axis.

If such a gradient field is smooth on all R3 and tends to zero at infinity, each component is a bounded entire harmonic function, and the harmonic Liouville theorem makes it constant and then zero. Thus the general identity allows whole-space harmonic fields, while the nonzero decaying dipole example fails the whole-space regularity requirement. The scope column's puncture language refers to this example, as the row's own entire-field clause makes clear.

The newly added Appendix A row now contains the harmonic identity, dipole pressure and entire-field conclusion. Consequently the Section 9 reference to Appendix A for its last four rows is true at this exact pin. A2412 remains an accurate refutation of the earlier snapshot and is not erased.

## 3. Complete sectors and exterior matching

The new Section 9 cell and summary row say that none of the three complete invariant-sector formulas extends smoothly across the origin. This is exactly the conclusion established independently in A2411. For clarity, in those formulas one writes U=V+grad Q, with harmonic scalar data f,Q and

    X.grad f=-(1-2c)f,
    X.grad Q=-2(1-c)Q,
    V=-grad f/(1-2c).

Along the explicit invariant flow F_t=exp(t(cI-omega J)), the exact vector scaling is

    U(F_t x)=exp(-(1-c)t)exp(-omega tJ)
               [V(x)+exp(-t)grad Q(x)].

For LIT273, Q=0 and a nonzero V gives divergence in norm as t tends to minus infinity, while F_t x tends to zero. For LIT279 and LIT281, Q is nonzero. Choose x with Q(x)!=0; its scalar homogeneity forces grad Q(x)!=0. The exp(-t) term dominates the fixed V(x) in the bracket for sufficiently negative t, again giving divergence. Each complete invariant-sector formula therefore fails even continuous extension at zero.

The formula does not apply to an extension problem in which only the portion outside a fixed ball is prescribed and a different vortical interior is permitted. Its trajectory eventually leaves that prescribed exterior. No contradiction is obtained from continuing the original formula after it has ceased to be a hypothesis. That matching problem remains OPEN at the scopes stated in A2415 and A2421.

The revised text also explicitly states that infinite exterior energy is not excluded by the target hypotheses. This is necessary: velocity decay alone does not impose finite energy. The example's failure of smooth extension at the origin, rather than its infinite energy, is the relevant obstruction to treating its complete formula as a target profile.

## 4. Verdict and evidence limits

The two corrections are CONFIRMED. The earlier A2412 reference exclusion is resolved at pin f42d627c, and the complete-sector scope is now expressed explicitly in the report. The mathematical front/main/Appendix A approval transfers from A2420 without that editorial exclusion, with every theorem retaining its individual assumptions and every open problem its status. All five complete source differences and this entire four-section proof were read. No numerical computation, new model client or formal build was run.

The comparison uses the existing configured model coordinator's written response and the independent A2410-A2411 derivations. Actual provider execution is not independently attested. Neither unrestricted smooth decaying rotating profiles nor exterior-sector matching, the common-flat endpoint or complete off-axis scalar corrections are settled here.
