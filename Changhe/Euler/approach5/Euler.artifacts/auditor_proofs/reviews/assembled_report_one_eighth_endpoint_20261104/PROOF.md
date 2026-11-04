# Report transfer audit: one-eighth pressure bound and weak-L2 endpoint steps

## 1. Exact snapshot and inherited scope

The captured report has SHA256 12edd78d578dd82a2dc7f8291f3234755268476f51690047dc272b3e5501062d, 1071905 bytes and 7109 newline characters, with verdict cutoff A2862. Both coordinator copies matched at capture. The announced intermediate snapshot 992a0d13 advanced before this agent captured it; this review does not claim to possess or approve that intermediate snapshot. The actual six-hunk delta is against retained d3e7e741. Every complete hunk was read, including the entire 55953-character third block. The separately copied coordinator delta for 992a0d13 is not the delta for this snapshot.

The last cumulative approval A2843 covers front matter, sections 0 to 10 and Appendix A of 05d561ba. The intervening d3e7e741 transfer was checked in A2850-A2851 and had one explicit-weight condition. Historical appendices are not collectively certified here.

## 2. Correct transfers and completed repairs

Section 10 now explicitly writes the second integrand as |W|/(|V||y|). This is the same weighted annular quotient as the first, and resolves A2851. The new reference to punctured local square integrability has exactly the scope A2852-A2853: it applies to the conditional carrier criterion, while the full system already supplies the stronger local boundedness used by A2832.

The pressure row correctly states the attained bound g_star <= Gamma_2 < 1/8. Its adaptive parameter is tau=1/7-(144/35)(abd)^2/s^3, with diagonal weights tau+(1-3tau)a_i^2/s. For s>0, a+b+d=0, these lie at least at 1/15. Subtracting I/300 places the test in the strict positive-functional range. Both equality types of the one-eighth test are retained, and tightness of the test is not claimed to evaluate Gamma_2. The exact local smooth threshold remains 1/6; the center-Holder threshold remains 1/(4+2alpha). The pressure premise on the whole ball and all local regularity hypotheses are unchanged. One definition at s=0 must be added, as Section 3 explains.

The annular row correctly adds the punctured-L2 theorem, its full containment of the mixed L2+C/r coefficient class, and the anti-holomorphic off-center countertest. Its part (e) transfers the finite-order zero isolation, allowed winding indices, charge and negative-index budgets, no-isolated-flat-point theorem, and localized carrier consequence of A2859-A2861. It does not claim that LIT341 excludes a perfect flat set. The separate LIT342 assertion is absent, as appropriate at cutoff A2862. One nonzero alternative in part (d) must be explicit, as Section 3 explains.

The three exact historical replacements specified in A2849 are all present and their old strings are absent. This resolves those particular label repairs only. The new historical entries preserve OPEN and REFUTED verdicts instead of promoting them.

## 3. Two remaining literal-scope repairs

First, the displayed adaptive weight formula contains division by s and s^3. Here s is the squared coefficient size of the tangential projection, which can be zero for a nonzero solenoidal quadratic. For example, take the harmonic cubic H=z(x^2-y^2) and Q=grad H=(2xz,-2yz,x^2-y^2). Its divergence is zero. It is sphere-orthogonal to every tangential field T=x cross Mx with symmetric M: T is tangent and has zero spherical divergence, so integration by parts gives integral Q.T=integral grad_S H.T=0. Thus its tangential projection is zero. The formula is undefined for this Q, although the underlying source proof handles the case by B=I/3. The precise repair is to qualify the formula by s>0 and add B=I/3 for s=0. Stating a+b+d=0 beside the eigenframe coefficients would also expose a hypothesis already entailed by the tangential representation. No counterexample to the one-eighth theorem is asserted.

Second, the assertion that an off-center zero of f is not flat requires f not to be identically zero. The function f=0 on the disc with b=0 satisfies every smoothness, differential-inequality, weak-L2 and punctured-L2 condition, and every point is flat. It directly refutes the unqualified sentence. For a nonzero f the assertion is exactly the proved local-continuation step: a flat point away from the center forces local vanishing by the L2 theorem, and open-closed propagation on the punctured connected disc forces f=0 throughout. The leading polynomial statement then applies to the remaining finite-order zeros. Add “if f is not identically zero” to part (d); the source theorem needs no change.

These are explicit-domain and explicit-alternative repairs. The substantive bounds and continuation arguments remain valid at their confirmed hypotheses. Cumulative approval of this exact snapshot stays pending until both repairs appear in the report.

## 4. Independent comparisons and static evidence

The complete Theory Agent C 03:39 comparison of intermediate 992a0d13 was read. It independently identifies the missing s=0 case and agrees with the repaired weight, both equality types, the punctured-L2 transfer and exact historical replacements. Its approval concerns its own captured intermediate bytes; it is not substituted for this agent's full delta read of 12edd78d. Its off-center-zero discussion also explicitly proves the zero-function alternative, which is why that alternative should appear in the row.

The static checker read all 2862 verdict entries through the cutoff and found 222 positive lists with 2428 distinct positive report references, no missing references and no improperly positive status. All nine tables pass, with 582 data rows and 600 total table lines; four norm-display blocks are correctly excluded. No absolute local paths or em dashes occur in the snapshot. Both changed rows match the captured ASSUMPTIONS file exactly. The row hashes, cutoff correction, exact replacement check and all six delta blocks are retained in verification. These checks concern text consistency, not proof validity. No mathematical computation was run for this transfer audit.
