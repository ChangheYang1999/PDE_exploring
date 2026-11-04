# Report transfer at the exact 23:37 assembly

Status: exact changes read; scoped mathematical transfers confirmed, one inherited-hypothesis phrase requires correction. This is a report audit, not a new Euler theorem.

## 1. Statement and reading boundary

The report pin is SHA256 8e779993f31e40b99b8a475b59963e3dc4065f63fa867db8860740d2c75a7c65, 1000432 bytes, assembled at 2026-11-03T23:37Z and recording verdicts through A2538. The complete line differences from the 02ab05b9 pin were read: the report 32256 characters, ASSUMPTIONS 40468, PROOF_OBSTRUCTIONS 7140 and THEOREM_ATTEMPTS 9926. The four exact files and differences are in verification, with their hashes in the team records. The earlier cumulative approval is A2488 for cace15a2, front matter, main text and Appendix A, at cutoff A2474. The intervening mathematical changes have the scoped checks A2497-A2499, A2513, A2528-A2530. Historical Appendix B has no blanket approval.

The present claim is that the new source-history and carrier rows correctly transfer the proved results, and the new B67 conclusions transfer correctly once their hypothesis cross-reference is made exact. All statements here concern these passages only. The unrestricted arbitrary-helicity decay-only theorem remains open.

## 2. Source history and entropy partitions

The C70 row in both the report and ASSUMPTIONS now says that the Pan-Zhang 2023 manuscript was read and that the earlier Pan 1992 Lemma 7 cited in its proof was not obtained. This is the exact correction requested in A2529. The independent smooth-flat proof remains the mathematical dependency; no unread primary proof is newly certified.

X5 now uses an increasing sequence of finite Borel partitions generating the sigma algebra. These are ordinary measurable partitions, not finite dynamical generators. The entropy conditioning cost is their entropy, independent of block length. This agrees with the fully checked arbitrary invariant-kernel proof A2491-A2495, including infinite entropy. No ergodic decomposition is introduced.

## 3. Arbitrary radial-envelope carrier transfer

Fix 0<c<1/2, finite real omega and a smooth transverse section through a nonzero point for X(x)=(cI-omega J)x. Let lambda(r) be positive, finite-valued and tend to infinity as r tends to zero. No measurability of lambda is needed. A2532-A2537 give a smooth local V satisfying div V=0, X.V=0 and DV X=-LV, L=(1-c)I+omega J, flat exactly on the central orbit. With W=curl V, both section ratios Q1=|W.X|/|V| and Q2=|W|/|V| satisfy

    Q1+Q2 <= Cstar + lambda(r)/r,
    Qj in Lp for every 0<p<2,
    (Qj-C0/r)_+ not in L2 for every finite C0>=0.

The geometry constant Cstar is fixed before lambda. The smooth minorant Lambda used in the factor exp(-G(log(1/r))), G'=Lambda, has bounded positive-order derivatives and grows sufficiently slowly. Its construction applies to the tail infimum of lambda and so does not require measurability. These are precisely the quantifiers in the new row. The C70 replacement statement is also correct: the constant Cstar is itself an L2 term on a small section disc, so a continuation criterion with B+lambda(r)/r would admit this nonzero flat counterexample.

This optimality concerns the specified pointwise radial envelopes. It is not a classification of arbitrary weak-L2, nonradial or oscillatory potentials. The row and main summary keep the result within the carrier system and explicitly retain full-F completion and the global conjecture as open. A later, separately confirmed LIT305 obstruction is not yet part of this exact pin and should be attributed to A2553-A2554 when added.

## 4. B67 transfer and the necessary hypothesis repair

The confirmed actual-tail statement is as follows. Let 2/5<c<1/2, omega be real, and let U in C2 and P in C1 solve the decaying rotating Euler profile system with zero helicity. Assume the natural velocity and first-derivative bounds and the established C1 local twisted tail limit V. Let w be the scattering direction of an escaping lower-window W2 trace, assume V is C2 near w, and retain the pressure and rank identities of the actual tail. B60 and B66 give w in supp curl V and V(w)=DV(w)=0. With W=curl V, k=X.V and S=P2-|V|^2/2, one also has W(w)=S(w)=0.

At the equality rate rho=-2(1-c), equivalently grad S(w)!=0 in this setting, B67 gives k=0 near w. At the strict rate grad S(w)=0, it gives D2S(w)=D2P2(w)=0 if nonzero-velocity points z_n tend to w with W(z_n)=DW(z_n)=0 and z_n in supp W, or if w is outside closure(int{k=0}). The first contact condition is an explicit extra hypothesis. The proof uses C2 harmonic pasting at boundary points of the irrotational interior and the scalar identity b S grad k=a k grad S, where a=1-2c and b=2(1-c). It does not assume DW(w)=0. The full standalone argument is in the team records, A2515-A2519.

The new row currently begins "under the hypotheses of the B66 row" and its scope column says "as the B66 row". Literally the B66 row assumes a supported NONFLAT direction and the strict rate grad S(w)=0. Neither premise can be carried into a theorem about the FLAT direction at both rates. In particular the equality clause would inherit both grad S(w)=0 and grad S(w)!=0. The B66 contradiction is used to obtain flatness, not as a nonflat premise of B67. This cross-reference is therefore not an exact statement of the confirmed theorem.

Replace the opening in both tables by:

    For an escaping lower-window W2 direction of an actual helicity-free tail under the natural bounds and C1 local tail convergence, with V in C2 near the direction (hence supported and flat by B60 and B66), ...

Replace the scope column by:

    actual helicity-free tail, natural U and DU bounds, C1 local tail convergence, V in C2 near the escaping lower-window W2 direction

This repairs the inherited hypotheses without changing the conclusion or adding an assumption. The report's new statements in Sections 1, 7 and 10 and the tracker T42 already use this intended scope correctly. For an unambiguous residual list, use T42's existing wording: equality-rate flat zeros in int{k=0}, and, at strict rate, D2S=0 or membership in closure(int{k=0}). The table's shorter phrase can be read as including equality in its second alternative, but should be expanded to remove the ambiguity.

The separate source sentence in Theory Agent B Proposition W2.21(a) still asserts DW(w)=0. It is not copied into this report row and is not supplied by A2516. Its removal or separate proof has been requested. This does not affect the confirmed k=0 conclusion.

## 5. Assembly verdict and limits

The Pan-Zhang correction, entropy wording, C71/C72 transfer, B67 conclusions with their correct actual-tail premises, short-segment repair in O9, and explicit residual list in T42 agree with their proofs. The table's B66 hypothesis inheritance needs the concrete repair in Section4 before cumulative approval of this new pin. The earlier cace15a2 approval remains unchanged.

No estimate uniform over all omega, no regularity upgrade from C1,alpha to C2, no infinite flatness, no removal of the W2 residual and no full arbitrary-helicity theorem follows. No numerical computation or formal build was needed. Existing configured model collaboration is through the coordinator's and theory agents' files; provider execution is not independently attested. No new client or agent was used.
