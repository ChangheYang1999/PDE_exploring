# Exact source-return hypotheses in the final summaries

## 1. Claim and objects

The coordinator README's Theorem 8(j) summary and Section 3.1's 8(d)-(p) row omit the condition that the translation vector a is nonzero. In addition, the README says uniform decay is unnecessary without stating the retained boundedness and distributional blow-down hypotheses. Its surrounding Theorem 8 summary assumes decay until this explicit exception. The detailed Theorem 8 header and part (j), and the current report's later conditional-results table, state the correct hypotheses. Thus this is a summary-scope repair, not a refutation of the detailed theorem.

The report reviewed is cd6d637c8f087e1d863d59549fdc1d34035293c55a7a5d11c5e087969f485a32. The captured coordinator README is identified in the team records; all its 208 lines were read. The review does not recertify every result it references. The source-return proof used below is A3084-A3085, whose exact statements and bounded-overlap proof were reread.

## 2. Correct statement and why a must be nonzero

Let U be a C1 divergence-free vector field on R3 with E(R)=integral_(|y|<R)|U|^2=o(R). Let q=tr((DU)^2), with matrix multiplication before taking the trace. Fix a nonzero vector a and a set D of positive integers with positive upper natural density. If q(.+na)->q in distributions as n tends to infinity within D, then U=0. No Euler equation or pressure is needed for this kinematic statement.

For a compactly supported smooth test phi supported in B_r, write I_n=<q(.+na),phi>. Distributional integration by parts gives I_n=integral U_i U_j partial_i partial_j phi(. -na). Each point belongs to at most 1+2r/|a| of the balls B_r+na, up to rounding. Therefore

    sum_(n=1)^N |I_n| <= C_(phi,a) E(N|a|+r)=o(N).

If <q,phi> is nonzero, convergence along D and its positive upper density give a subsequence on which this sum is bounded below by a positive multiple of N. This is impossible. Hence q=0 distributionally. Test q=partial_i partial_j(U_i U_j) against sqrt(1+|y|^2) chi_R, where chi_R is a smooth nonnegative cutoff equal to one on B_R and zero outside B_(2R). The positive Hessian term bounds E(L)/(1+L^2)^(3/2) for every fixed L<R. All cutoff errors are bounded by C E(2R)/R, tending to zero. Thus E(L)=0 for every L and U=0.

At a=0 the convergence assumption is an identity for every q, and the overlap estimate instead has N-fold multiplicity. A nonzero smooth compactly supported divergence-free field supplies a counterexample to that kinematic extension: choose a nonconstant compactly supported smooth psi and U=(partial_2 psi,-partial_1 psi,0). It has E=O(1)=o(R), while q(.+n0)=q exactly. This is not an Euler-profile counterexample. Removing a!=0 from a full-profile statement would assert an unproved unconditional nonexistence result.

## 3. What replaces uniform decay for profiles

For a C1 full rotating profile with U bounded and U(R.)->0 in distributions, and 0<c<1/2, the confirmed energy theorem gives E(R)=o(R). Consequently the previous source-return theorem applies for every fixed finite omega. The boundedness and blow-down pair is the report's Hb hypothesis. Uniform decay implies Hb but is not required separately.

Removing Hb as well is false even for full profiles. For any nonzero constant b, put U=b and P=-[(1-c)b+omega Jb].y. These are smooth, divergence-free, and solve the full profile equation because DU=0. The source q=0 returns for every nonzero a and every integer n. Yet U is nonzero; it fails distributional blow-down and E=o(R). Thus the README's no-uniform-decay exception must retain Hb, or explicitly use E=o(R) as the sufficient energy condition.

## 4. Concrete repair and verdict

In Section 3.1, change the (j) premise to: "for some a != 0, q(. + na) -> q in D' as n -> infinity along a set of positive integers of positive upper density". Keep Hb in the row's common velocity cell.

In the README, state (j) as: "0 < c < 1/2, U, P in C1, U bounded with U(R.) -> 0 in D', and, for some a != 0, q(. + na) -> q in D' along a set of positive integers of positive upper density; no uniform decay is needed". Alternatively say directly that the field has E(R)=o(R). The wider label before the results list can mention source, work, return and gradient premises in addition to helicity, tails and smallness.

Current verdict: OPEN as an unqualified summary until these premises are restored. The detailed Theorem 8(j) remains CONFIRMED at A3084-A3085. The new endpoint premise in the same table is separately confirmed. Existing configured model coordinator/C collaboration is continued through these files for comparison; actual provider execution remains independently unattested. No new computation, model client or theorem direction is introduced.
