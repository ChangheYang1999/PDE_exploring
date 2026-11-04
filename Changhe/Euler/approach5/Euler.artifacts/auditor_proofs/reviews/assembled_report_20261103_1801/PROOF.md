# Note 102 assembly audit

## 1. Scope and pin

The retained manifest pins the 6355-line report at sha256 2c1aef355f9425575c3452f61d6913044e91a641fc7909c6213f8b3a2e3e790e. Its mathematical changes relative to Note100 were read. README, THEOREM_ATTEMPTS and PROOF_OBSTRUCTIONS are byte-identical to Note100. This is a delta audit, not a new audit of every unchanged proof. The long appended historical revision paragraph is not fully reread and receives no new certification. The manifest records the actual capture time.

The exact statement conventions are those of the separately audited results cited below. In the tail notation c is the similarity exponent, a=1-2c, b=2-2c, X=(cI-omega J)y, E=|V|^2, k=X.V and S=P2-E/2. The unrestricted question remains open.

## 2. Confirmed new conditional material

The new LIT270 countertest is explicitly distinguished from a profile. Its comparison constants, momentum residual and failure of the rank relation agree with A1880-A1885. LIT271's original-profile sector and relative-vorticity-density consequence retain helicity freedom, the full equation, natural bounds and the global two-sided tail comparison. LIT272's supported contact and two interface conditions retain these hypotheses. Its formula grad S=-bSV/k is obtained from grad S=lambda V and lambda k=-bS, with k nonzero at that contact.

The LIT274 matching result explicitly retains global C2 tail regularity and the actual rank relation on supported vorticity; these are essential. The CO65 row retains omega=0 and the vanishing weighted period, including the sufficient polynomial full-circle maximum-ratio condition. These transfers agree with the topic proofs, not with an unrestricted Euler nonexistence theorem.

## 3. Sector potential and contraction are different

For LIT273 put f=Re(B z^lambda), lambda=-a/(c-i omega), and scalar velocity potential phi=-f/a. The field is U=grad phi=-grad f/a. Harmonicity gives div U=curl U=0; Xf=-af gives X.U=f=-a phi. Thus the new table sentence that k=X.U is equal to the potential -Re(B z^lambda)/a is false. It must say k=Re(B z^lambda), or k=-a times the velocity potential. Since a>0, the factors cannot be suppressed.

The audited construction uses B=i and a sufficiently small quotient-sphere disk around e1. There, grad f cross grad(-E)=-2E(|lambda|^2-Re lambda)e3 at e1, which is nonzero. Continuity and the homogeneous flow propagate this to the entire invariant domain over that disk. For a general nonzero B one must choose a disk avoiding the rank-zero set. The main text also needs B nonzero. Nonzero rank throughout an arbitrary spiral domain does not follow: the LIT274 formula exhibits simple rank zeros. The correct statement is existence of a suitably chosen invariant domain, with the specified nonzero coefficient. All six sections of the independent LIT273 proof were reread.

## 4. The C57 threshold is uniform over a class

For 0<delta<1/2, N_delta=Y intersect {S<0} intersect {R<1/(1/2-delta)}. Hence delta<=1/2-1/q guarantees N_delta is contained in the elliptic region R<q. For larger delta, particular solutions may still have all their N_delta in R<q. The analytic example A1928 has R=0 at its supported common zero and R<2 on a sufficiently small neighborhood. Since q>2 in the class considered, that neighborhood supplies such a counterexample to the individual-solution converse for every delta in the allowed interval. The row's literal "exactly when" is therefore false. Replace it by "this containment is guaranteed uniformly over the reduced local class exactly when" and cite A1948-A1949. The uniform sharpness counterexamples of A1931 are unaffected.

## 5. Positive epsilon and its numerical size

The new C60 exact positive-epsilon formula and conditional vanishing conclusion agree with A1886-A1890. C61's integral estimate and far-field L4 consequence agree with A1891-A1892. A1893 concerns the invalid assertion that the fraction consequence is equivalent to the integral estimate with its stated constant. The main-text parenthetical "only this consequence of the fraction bound is proved" misdescribes that verdict. The estimate itself is proved; the fraction bound is its consequence. Also write "this argument alone does not prove U=0" in place of "but not U=0".

The source gives floating-point illustrations at c=0.4,0.45,0.5 only. It does not prove epsilon(c) has uniform order 1e-15 throughout 0<c<2/3. In fact the displayed exact formula excludes a positive uniform lower bound of that order. Write tau=T*(c)^2, so 0<tau<=3, L>=1/(4-6c), C_*>=2tau L^2, delta_0<=(4096tau L^2)^(-2), and Delta<=2tau^3 delta_0/3. Rationalizing the square-root difference gives epsilon<=Delta/sqrt(tau)<=C sqrt(tau)L^(-4), with an absolute finite C. It tends to zero as c approaches 2/3. Numerical illustrations should be labeled by their specific c values and as observations; no new numerical verification was performed here.

## 6. Spatial weights

The new table accurately retains the universal pointwise-density-test quantifier and the restrictions on product weights and explicit plateaus. The main sentence "Weights depending on y do not extend the method" is broader than the confirmed statement. Only the particular sufficient pointwise positivity test and the analyzed product or plateau families have been obstructed. Replace the sentence by "The spatial-weight variants analyzed in F37 do not remove these global hypotheses" and explicitly retain the universal algebraic positivity test for the core restriction. A1903 leaves other spatial weights open. Neither the existence of a remainder of unknown sign nor a failure of this test is a theorem excluding all spatially weighted arguments.

## 7. Unchanged required repairs

The summary's k=0 branch of Theorem7(g) still omits W.grad S=0. Its full theorem retains this premise. The standalone T41 in THEOREM_ATTEMPTS still needs the full profile system and divergence equation: smooth compactly supported nonzero divergence-free U with P=0 refutes its literal equation-free reading, as in A1941. The LIT268 density shortcut still needs an actual helicity-free tail, or an independently imposed vortical rank identity; the LIT270 countertest refutes the reduced-identity shortcut. C43 must call the scalar K zero on the equator, not the full V; the explicit velocity there is nonzero. See A1940-A1943 for the complete arguments. Byte equality of the companion files does not certify the missing repairs.

## 8. Verdict and evidence limits

The new correctly scoped conditional transfers in Section2 and the exact C60-C61 estimates in Section5 are confirmed. The literal potential identification and individual C57 converse are refuted. The unqualified numerical-size and universal spatial-weight readings are not certified. The report as a whole remains OPEN pending repairs and subsequent assembly verification. No new PDE computation, numerical test, formal build, external model request or literature search was required. Model collaboration remains through existing working files, with configured model identity only, not an independently attested provider runtime.
