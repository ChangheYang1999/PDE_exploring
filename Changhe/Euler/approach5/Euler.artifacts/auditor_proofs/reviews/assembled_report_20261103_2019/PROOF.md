# Citation-status repairs and a new overstatement in report 76789bd5

## 1. Exact object and scope

This review concerns the coordinator report with SHA256 76789bd5c781ff44c53b811a25f30273817dfba33306ec63b2ec4ec783f110aa, frozen in this report, and its complete 16670-character delta from a245258a. All four retained companion files are byte-identical to their prior audited versions. The four main proof sections 2A-2D are also byte-identical, checked using exact heading boundaries and a four-block assertion. An initial two-hash heading pattern produced an empty list and was repaired before any verification conclusion.

The current front matter, Sections0-10 and AppendixA occupy lines1-5105. Historical AppendixB and revision AppendixC do not receive blanket approval. This delta does not repair the three already identified issues A2242, A2244 and A2252. A fourth defect introduced here is identified in Section3 below. Hence no whole-assembly approval is given for this pin.

## 2. Infinite flatness: an open conclusion, not a counterexample

The W2 contact results A1729-A1737 and A2035-A2038 establish, under their exact actual-tail and regularity assumptions, the indicated finite-jet vanishing. A1740 explicitly leaves unrestricted flatness unresolved. In particular the finite-jet argument supplies no example of an actual escaping W2 trace which is not infinitely flat.

The earlier sentence "it need not be infinitely flat" asserted more than those proofs established. Its corrected sentence "the argument does not show that it is infinitely flat, A1740 OPEN" describes the logical status accurately. This correction restricts the earlier assembly approval: A2224 must not be read as independently proving the existential interpretation of that earlier sentence. No contrary universal-flatness theorem is asserted here either. The source's complete scope discussion in Section11 was reread, together with the exact A1740 entry.

## 3. The LIT266 field satisfies several tail identities

The new wording says that LIT266 uses "a field that satisfies none of the tail equations". This literal claim is false. Fix 2/5<c<1/2 and put

    eta=(1-2c)/(2-2c), gamma=1-2eta=c/(1-c),
    b=(1+gamma)/2.

For x>0 set f(x)=exp(-1/x^2), t(x)=exp(b/x^2), S(x)=-f(x)^2(2+sin t(x)) and V(x,y,z)=f(x)e2; extend V,S by zero for x<=0. The whole four-section independent LIT266 proof has been reread. Direct differentiation gives

    div V=0, curl V=f'(x)e3,
    V dot curl V=0, (curl V) dot grad S=0.

These identities hold also on the zero plane, since f is smooth and S is C2. Thus incompressibility, zero helicity and the scalar vorticity transport identity do hold. The ledger A1843 expressly confirms incompressibility and that transport law.

What fails is the complete tail system. For X=(cx+omega y,cy-omega x,cz),

    X dot V=(cy-omega x)f(x),

which is not identically zero on any open crossing box. Twisted homogeneity also fails: if omega!=0 the e1 component of the vector equation cannot hold where f!=0, and if omega=0 it would require cxf'=-(1-c)f, whereas cxf'/f=2c/x^2>0. The normalized form has component f^gamma(2+sin t)^(-eta), which is nonconstant and has curl along e3, so it is not closed on the positive half-box.

There is no pressure making this V a full rotating similarity profile: a necessary vorticity residual is [f'+(cx+omega y)f'']e3. If omega!=0 its y coefficient is nonzero near the plane. If omega=0 it is f[(2-6c)x^(-3)+4c x^(-5)]e3, again nonzero for all sufficiently small x>0. These are the failures confirmed by A1845. They do not imply failure of every identity in the tail list.

Both new occurrences should say "by a field that does not satisfy the full tail system", or list the specific missing equations. The corrected clause preserves the actual counterexample: S is C2 and comparable with |V|^2, but |S|^(-eta)V is not W^(1,1). Indeed under t=exp(b/x^2) its nonzero component is t^(-a)(2+sin t)^(-eta), where a=gamma/b lies in(0,1). Its total variation dominates a positive multiple of integral t^(-a)|cos t|dt minus an integrable term, and is infinite. None of this proves failure of a C2 extension theorem using the full tail equations. That question remains OPEN A1846.

## 4. The remaining citation changes

Each following edit agrees with the exact corresponding verdict, all of which were reread:

1. A1309 refutes exclusion of a supported common flat pole from the reduced identities alone; the separate positive construction is A1304-A1308,A1310.
2. A1340 refutes derivation of the global rank equation from local momentum and zero helicity, by an exact local shear. It is correctly removed from a bracket labelled CONFIRMED and retained as the failure verdict.
3. A1384 refutes a bound on negative component constants from smoothness and rank alone; A1382-A1383,A1385 give the construction and its scope.
4. A1406 concerns arbitrary axial dependence beyond the translation-invariant theorem and belongs in the OPEN list.
5. A1459 refutes deleting the identically-zero alternative. The revised text explicitly refers to its corrected wording, while retaining nontriviality or the zero-or-nowhere-zero dichotomy.
6. A1243 is OPEN for the actual tail with drift, so removing it from the weighted local-model confirmation bracket is correct.
7. The mixed-status A989 is explicitly a failed printed sign together with a confirmed corrected formula. The phrase "CONFIRMED with repairs" may cite it without claiming that the incorrect sign was confirmed.

These are status and scope changes. They do not create any additional local-to-global implication or discard any regularity, support, helicity, pressure or decay assumption of the cited positive results.

## 5. Coverage and limits of approval

The complete changed text was read, with all exact ledger entries needed for its status edits and the complete four-section LIT266 proof. Unchanged mathematical text transfers from the previous audited pin only at its stated scope. The four long foundation proofs are exactly unchanged. Companion-file equality is recorded in the manifest and empty diff files.

The proper conclusion is confirmation of the repaired A1740 reading and the precise citation edits, with the newly false "none of the tail equations" wording excluded, and the prior A2242,A2244,A2252 exceptions retained. No full assembly approval is issued. An actual C2 counterexample obeying the complete tail system, an actual nonflat trace satisfying the stronger W2 conclusions, and unrestricted smooth rotating-profile nonexistence are not supplied by these edits.
