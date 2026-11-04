# Remaining precision changes in the a5a3e2e8 report

## 1. Exact statement and scope

Let R be the frozen report this report, SHA256 a5a3e2e8b0ccc6034510e40d955561a1fc1439ca0b61fc84a37a24c7331f69ed. Relative to d0d9f21a, the mathematical precision changes outside the two defects of A2242 and A2244 preserve the previously confirmed scopes. This assertion covers the front matter, Sections 0-10 and Appendix A, lines 1-5083. It does not approve R as a whole: the finite-order sequence and general SF.8 weight clauses still require repair. Appendix B retains only the scopes of its individually cited historical verdicts; Appendix C is revision history, and the file map in Appendix D is unchanged.

The complete 55091-character report delta was read. README, ASSUMPTIONS and PROOF_OBSTRUCTIONS deltas were read in full; THEOREM_ATTEMPTS is unchanged. The generic SF.8 defect is repeated in ASSUMPTIONS. The two referee disposition notes were read, but each substantive change below was compared with its proof rather than accepted from a referee's judgment.

## 2. Differentiability and finite-order conditions

The report now states how DW is defined at a zero of W: if x=Xi(y), then DW(x)=DXi(y) D Omega(y) DXi(y)^(-1). The complete eight-section proof in the team records was reread. At Omega(y)=0, continuity of DXi and the first-order expansion of the C1 field Omega suffice to differentiate W o Xi=DXi Omega. A second derivative of Xi is not needed. Twisted homogeneity makes the spectrum of DW grow like exp(-(1+c)t) backward, whereas the similar matrix D Omega on the bounded original backward orbit stays bounded. All eigenvalues therefore vanish. Similarity norms are not bounded or needed. The report does not replace nilpotence by DW=0.

The full ten-section proof in the team records was reread. The report's log-convex weights with divergent sum M_(j-1)/M_j refer to the same exterior derivative bound as the immediately preceding factorial condition, with common constants and the natural factor |y|^(-p-j). After passing this bound to V, the one-dimensional estimate B_f(x+h)<=max(B_f(x),exp(-q))exp(e mu_q |h|), mu_q=M_q/M_(q-1), shows that a nonzero flat germ would require a finite segment to contain disjoint intervals of lengths at least 1/(e mu_q). Divergence forbids this. Thus these exact weight hypotheses supply finite order. Original vorticity analyticity is needed near every preimage of T0, as now stated; an arbitrary isolated analytic neighbourhood would not suffice. The separate power-sequence clause remains defective as recorded in A2242.

## 3. Quantitative flat-component criterion

The CO58 wording now requires (D_C)_- |V|^(q-2) to tend to zero uniformly at the point. This is the precise condition of in the team records, Section 6, which was reread. On vortical components with k!=0, S=D_C|k|^q and |k|<=K|V| locally. The uniform limit makes S>=-|V|^2/4 on a sufficiently small neighbourhood. On the complement the stated nonnegative-S premise gives the same bound. Consequently P2=S+|V|^2/2>=|V|^2/4. The established local positive-stress doubling bound is incompatible with infinite flatness unless V vanishes. Mere componentwise limits, or an unspecified small bound with no comparison to K, are not substituted for this uniform condition.

## 4. Other theorem and reduction clarifications

Theorem 3(f) explicitly labels the C2 attractor statement conditional on nonvanishing original vorticity on the attractor. This matches its existing compact vortical invariant-set proof. Theorem L now explicitly retains Theorem 5's range, decay and helicity premises. The finite-regularity expansion and contraction quantities refer to the symmetric derivative of the slowed carrier field and to the existing precise growth condition; they are not replaced by an unproved consequence of decay.

Section 0.2 identifies the escaping set as points with unbounded forward carrier orbit and its complement as the core. The R3 W2 sentence retains the target c range, natural bounds, C1 local tail convergence, lower-window escaping trace and local C^(2,1) regularity needed by A2038. The N3 index argument distinguishes the nonnegative index forced by the sphere count from the index -1 of actual vortical zeros. The flat-complexity statement retains the density and bounded-component-constant conditions. Global ratio comparisons are written as two-sided inequalities on the whole sphere, including their zero sets, and the lower-near-common-zeros variant is explicitly separated. The pressure constant is normalized where the cited ratio result requires it.

The local examples are described as satisfying the stated necessary tail equations without any assertion that they fail only one global equation. The kinematic examples have carrier B=Ay+U with decaying U. They exclude a deduction based only on the identities they satisfy; they are not decaying Euler profiles. The A1021 comparison is correctly called the stronger hypothesis. These changes narrow or clarify the formerly audited statements and add no arbitrary-omega or regularity extension.

## 5. New C65 and LIT292 insertions

Apart from the generic reduction clause separately refuted in A2244, C65 is inserted at its exact independently verified scope: C2 velocity and C1 pressure, Hb, every omega, 0<c<=1/2, and both global bounds -lambda_min(sym DU)<=6/5 and |curl U|^2<=103/100. The Frobenius alternative |sym DU|^2<=54/25 implies the strain bound. The four-term weight, rational subdivision, comparison with named sufficient criteria, and linear-family obstruction for 9/20<=c<=1/2 agree with A2205-A2210. No optimality or consequence of bare decay is added.

The LIT292 insertion excludes a zero transverse pressure gradient at a smooth finite-order N>=2 positive-pressure zero in an open k=0 region with the full next-scalar premises. Its actual-profile transfer retains helicity freedom, C2/C1 regularity, both natural bounds, supportedness and smooth local tail regularity; at c=3/7 it uses the averaged next scalar. Source H is report S. Axial zeros are already excluded by LIT290-LIT291. General nonzero transverse gradients and common-pressure-zero or boundary configurations remain open. This matches A2212-A2217, including the clarified order of the centralizer argument in A2226.

## 6. Coverage and verdict

The exact line map is in the team records. Every unchanged line in the fresh scope transfers the prior complete reading; every changed block was read directly. The four complete proof sections are byte identical to d0d9f21a: 2A now lines716-1198, 2B1199-1877, 2C1878-2946 and 2D2947-3951. Their hashes and the 0.010903466027230024-second identity check are retained in the team records. This check transfers a previously completed mathematical reading; byte equality alone is not a mathematical proof.

The remaining precision changes and the two new result insertions are CONFIRMED at the scopes just stated, excluding the finite-order sequence and generic SF.8 clauses. The complete a5a3e2e8 assembly remains unapproved pending those repairs. The unrestricted conjecture and all retained conditional gaps remain OPEN.
