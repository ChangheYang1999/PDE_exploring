# Integer regularity in the final report

Rechecked 2026-11-04T14:43:32.740538+00:00. This is a narrow report-scope verification, not a new fractional-regularity theorem.

## 1. Exact claim and fixed reports

The transitions ba9283f0 to da36a8d0 and da36a8d0 to3407dec6 add seven integer-regularity qualifiers to previously confirmed statements or their summaries. At the exact hypotheses of those statements, each change is valid. No other mathematical premise or conclusion changes. The fixed complete reports, SHA256 values, exact normal diffs and simultaneous current-copy comparison are in the capture.

The first transition has21 lines and5 hunks: status, Theorem D4(i), the componentwise form in2D.1.2, the Section8 strain-sum row, and history. The second has25 lines and6 hunks: status, Theorem C_strain, its finite-r equivalence class and Liouville remark, the Appendix A strain-sum row, and history. Both complete differences were independently generated and read, and equal the coordinator's retained differences byte for byte.

## 2. Source hypotheses and proof of the seven checks

For the finite-regularity coverage statements, let c lie in(0,1/2), omega be any fixed finite real number, U in C^r(R3;R3), P in C1(R3), and assume div U=0 and the full rotating profile equation. Require uniform sublinearity of U. Write a=1-2c and B=(cI-omega J)y+U, where J(y1,y2,y3)=(-y2,y1,0). These common hypotheses are retained in the report and its explicitly referenced setup.

The A430 statement takes r>=2 an integer. Its componentwise condition is Lambda_E<r a for every connected component E of{curl U!=0}, equivalently Gamma_E<r a with the zero-stratum rate defined there. Its report setup at line4002 now matches this exact regularity. The change does not supply the growth condition or a gap uniform over components. See the complete componentwise proof, Section1.

A312 takes r>=3 an integer and uses a radial cutoff rho. With Y=-rho(cy+U), L=sup||sym DY||, its sufficient condition is(r-1)a>3L. A373 takes the same integer regularity and improves the sufficient condition to(r-1)a>Lplus+Lminus, with Lplus=max(0,sup lambda_max(sym DY)) and Lminus=max(0,sup -lambda_min(sym DY)). Thus the changed strain-sum rows at lines5595 and6575 match A373, while the changed Theorem C_strain at4125 matches A312. The exact source statements are in [A312](auditor_proofs/proofs/finite_regularity_vortical_coverage/PROOF.md) and [A373](auditor_proofs/proofs/strain_sum_vortical_coverage/PROOF.md).

The changed A312 finite-r class at4766 retains(r-1)a>3L, decay, P in C1 and c in the open interval(2/5,1/2). Its equivalence relates nonexistence in that restricted class to absence of a sign-changing essential basin in that class. The changed remark at4813 retains the same strain condition, decay, P in C1 and2/5<=c<1/2; its Liouville conclusion retains one helicity sign per essential domain. Adding integer r>=3 gives exactly the source regularity for both deductions. Neither change asserts unrestricted C2 coverage or an automatic helicity sign.

Theorem D4(i) now restricts its stated C^r class to integers r>=2. Its existing A055 conclusion is1-2c<=h_top(F|Lambda)+R(F')/r under H0, uniform sublinearity and nonconstancy, with the specified compactification F'. Restriction to integer r is a subcase of the previous wording and matches the derivative order used in the displayed argument. The detailed four-step report proof was read; no printed Yomdin or Gromov source was newly read in this check. Thus this verdict licenses the narrowing only and makes no claim about fractional smoothness or a new independent proof of A055.

## 3. Collaboration and historical scope

All of existing A's notes A170-A172 and coordinator notes271-272 were read and checked against the seven actual changed contexts. Their complete retained passages are A170-A172 and coordinator271-272. A and coordinator are configured with the primary model; provider execution is independently unattested. No new model client or agent was used.

The history records A3262 only for the earlier repair and A3263 only for the classical pressure/energy recheck. It does not attribute these seven new qualifiers to either verdict. Appendix B historical wording is unchanged and receives no collective approval. Statements using r later within an explicitly integer setup inherit that setup; no global convention extending to fractional r is inferred.

## 4. Conclusion and limits

All seven integer qualifiers are valid and preserve every extra hypothesis. This proof certifies the two listed report deltas only. It does not certify the entire3407dec6 assembly, reopen historical appendices or prove the main arbitrary-omega nonexistence conjecture. The planned current-build comparison about15:30Z remains separate. No computation, formal build or new numerical evidence is needed.
