# Whole assembled-report review at the 16:18 snapshot

## 1. Exact object and scope

The object is the immutable in the team records, captured at the real time in the team records, with SHA256 44143c343b0fe18a9b52290caea3ef55ce81806b00fc1cdf95c6cf94480db8c9. It has 6124 lines. The complete front matter, Sections 0-1, and Sections 2 and 3-10 were read in this pass. All nine changes from the preceding 16:11 snapshot were read completely. The full appendices were read in A1272-A1287; intervening changes were read in the subsequent report-repair audits through A1632. This review uses that cumulative reading, not a claim that all 6124 lines were freshly read again.

The exact baseline is div U=0 and

    (1-c)U+DU[(cI-omega J)x+U]+omega JU+grad P=0,
    Jx=(-x2,x1,0),

on R3. Each theorem retains its own regularity, c-range and decay conditions. In particular the unrestricted question remains OPEN for 2/5<c<1/2 and omega nonzero. The smooth helicity-sign theorem is an additional-hypothesis theorem. The C2 coverage question remains conditional. Local stress examples and exact nondecaying profiles are not counterexamples to the target question.

## 2. Complete-proof continuity and earlier repairs

The four complete proof sections 2A-2D are byte-for-byte identical to the full versions freshly read in A1217-A1220. in the team records records the independent string comparisons and hashes. The different displayed line counts in that file include separator blank lines. No mathematical computation is involved in this file comparison.

Thus their existing confirmations remain valid: the energy proof uses exactly Hb and its canonical pressure gradient; the dynamical proofs use complete carrier flow and compact backward trapping; smooth basin coverage retains all smoothness and external dynamical dependencies; the helicity-sign proof retains coverage, recurrence, its pressure gauge and the final sublinear-energy virial bound. No unproved finite-regularity improvement has been inserted into these bodies.

The latest repairs pass at their stated scopes: the resonant pressure example uses mu=x3/|x|; the continuous-pressure theorem cites A1622-A1624; the enstrophy referent is unambiguous; Theorem 8's table groups bounded vorticity with each alternative; C52's converse concerns an already specified invariant set; endpoint stress-only examples are identified as not divergence free. Theorem 8's actual union of strict linear and weak polynomial bounds is correct. Four remaining presentation errors are addressed below.

## 3. Incorrect tensor in the CO63 row

The Appendix A row identifies the stress for A1611 as T=H I-V tensor V, where H=|V|²/2-P. This formula is false. For divergence-free V and the pressure Poisson equation, the double-divergence-free tensor is

    T=-(V tensor V+P I)=(H-|V|²/2)I-V tensor V.          (1)

Indeed div div(V tensor V)=tr((DV)²), which cancels Delta P. In contrast the displayed tensor in the report has double divergence Delta(|V|²)/2.

An exact local algebra test is V=Jx and P=(x1²+x2²)/2-1. Then div V=0, tr((DV)²)=-2, Delta P=2 and H=1. The incorrect tensor has double divergence 2; (1) has double divergence zero. On a sufficiently small ball |V|²/H<2/3. This example tests the tensor calculation, not the flatness conclusion: its velocity is not infinitely flat.

The eigenvalues of (1) are H-3|V|²/2 in the V direction and H-|V|²/2 in its orthogonal complement. Consequently the confirmed uniform-definiteness condition is exactly |V|²<=Rstar H with Rstar<2/3. Replacing the tensor formula repairs the row without changing that theorem. The same correction is needed in coordinator Note 90's suggested tensor.

## 4. The crossover must be exact

Put tstar=(15sqrt(7)-20)/42. Solving the actual inequality gives

    sqrt(3)(1-3c/2)>sqrt(tstar)
       if and only if c<cstar=(2/3)(1-sqrt(tstar/3))

for 0<c<2/3. The report instead asserts that it holds only for c<0.40315 in the target range. That rounded rational endpoint is too small.

An exact witness is c0=8063/20000=0.40315. Here 1-3c0/2=15811/40000 and

    3(1-3c0/2)²=749963163/1600000000
                 >6152/13125>tstar.

For the first strict inequality cross multiplication gives the positive numerator 66514375. For the second, sqrt(7)<2.64576 because (2.64576)²=7.0000459776>7; substituting this strict upper bound gives tstar<6152/13125. No floating-point computation is used. Therefore the printed 'only for' sentence fails even at c0. Use the exact cstar and, if desired, say it is approximately 0.40315. The correctly stated union of criteria in Theorem 8 remains valid.

## 5. Gauge in Remark 7.1

The report defines the original Bernoulli function by

    H=P+|U|²/2+[(cI-omega J)x].U,
    Q=P-Pinf-|U|²/2.

On the regular nodal manifold M it correctly states H=Pinf. Its next sentence says that Q vanishes to order q in H. The variable centered at the zero set must be H-Pinf. Adding any constant C to P changes H and Pinf by C and leaves Q, M, and all profile equations unchanged. Thus the uncentered wording depends on an arbitrary pressure gauge. Replace 'in H' by 'in H-Pinf'. The ensuing Hessian identity is unaffected. This is the same gauge issue already repaired in the critical-leaf rows by A1209 and A1277; it survives here in the regular-leaf paragraph.

## 6. Theorem 3's scope table

Theorem 3(f) correctly assumes either globally smooth U, or C2 U with vorticity nonvanishing on the whole core, for its topological entropy bound. Theorem 3's row in Section 3.1 lists U=C2 and only part (i)'s annular integrability premise in the extra-hypothesis column. Since the table expressly promises the exact hypotheses theorem by theorem, it omits part (f)'s extra alternative. Add 'part (f): C-infinity, or no zero of curl U on the core'. The explanatory prose in Section 3.2 and the actual theorem already state this correctly.

This is a refuted scope transcription, not a counterexample to an unconditional C2 entropy bound. The latter broader assertion is not established by the cited proof. No new dynamical claim is made here.

## 7. Whole-report verdict and dependencies

Whole-report approval remains OPEN pending the four concrete repairs in Sections 3-6. No further error was found in the freshly read Sections 0-1 and 3-10 or in the nine changes. The complete proof bodies retain their confirmations under exactly their written hypotheses and cited dependencies. A repair-only next version can be checked by reading every change and its surrounding statement; a fresh reading of unchanged complete proofs is unnecessary.

This does not certify that the main conjecture has been solved, that every external theorem has been newly retrieved, or that every appendical research direction is proved. The report must retain its OPEN and CONDITIONAL labels and the explicit distinction between smooth and C2 coverage. The earlier complete-proof, appendix and repair audits are the dependencies of this report-level conclusion. Existing configured model agent-file exchange supplies the requested model collaboration; provider runtime identity remains unattested. No mathematical computation or new model client was used in this pass.
