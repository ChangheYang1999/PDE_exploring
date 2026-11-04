# EXISTING_PROOFS_REFERENCE (agent the first theory agent), version 5

Version 1 written 2026-11-02T18:53Z (the header said 18:55Z; the file modification time was 18:53:36Z, see work log).
Version 2 written 2026-11-02T19:09Z: wording repairs of the theory audit exchange audit_v14 and the [S1P] P5.2 note in section 0
item 9; no source reading changed. Version 3 written 2026-11-03T22:01Z: the section "Targeted audit notes (version
3)" is appended at the end; it records the audit notes on uses of R1 to R11 filed after version 2 and changes nothing
above it. Version 4 written 2026-11-04, started 11:56Z (the completion time is in the last line): the section "Part
VII freeze (version 4)" is appended at the end; it states the freeze, the sweep of the audit records filed after
version 3, a notation note and the uses at the freeze, and changes nothing above it. Version 5 written 2026-11-04,
started 12:13Z (the completion time is in the last line): the theory auditor CONFIRMS version 4 in its reference-usage scope
(AT2732, AT2733, AT2735; audit_v827; research/epr_v4_integration_audit of agent the theory auditor) and REFUTES one citation date
(AT2734): the coordinator's correction list with the labels R1 to R5 is its note of 2026-11-03T22:20Z, while its note
of 22:03Z has the labels C1 to C5. Version 5 replaces only that date in the sweep paragraph of the Part VII section
and adds "corrected at version 5" to the heading of that section; nothing else changes. Versions 2 to 4 are kept as
history/EXISTING_PROOFS_REFERENCE_v2.md to history/EXISTING_PROOFS_REFERENCE_v4.md in the first theory agent agent. Owner: the first theory agent.
Scope: the Part II references R1 to R11 of PROMPT.md. For each reference this file gives the status of the located
source, the exact hypotheses under which the source proves it, the source files and line numbers, the audit status
recorded in the sources, and the differences from the prompt's statement. Nothing here is re-proved (run rule: do not
re-prove Part II). Where no detailed source was located, the entry says "no detailed source located; the prompt's
Part II statement is the reference", and the result is IMPORTED from the prompt only (tag [prompt] in the ledger).
Paths are relative to the combined2 root.

Status convention. "Source located" and "no detailed source located" describe what was found on this box. Both kinds
of reference are IMPORTED (WORKSPACE_CONTRACTS.md section 1); neither is re-proved or rejected here.

Method. The source map was produced by a read-only reading pass over source/ (grep, sed and cmp; 10816 .md, .txt and
.tex files searched for the negative results). The first theory agent then re-checked these quoted lines directly at 18:52Z: [L2] 7-27,
50-58, 72-90, 140-178; [VL] 160, 353, 1223; [LRT] 17; [NVL] 975-982; [TF] 1565-1569; [S1P] 2356-2358; [S1C] 48-49.
All matched the quotations below.

## 0. Consequences for combined2 (the first theory agent reading, no new mathematics)

These points govern how the imported results may be used in FW-C2-main-v1 and the other frameworks of theory_v01.

1. R1 is proved for compact smooth S1 tests under [L2] (A) and (B) only (section 2 of [L2]); (C) and (D) are not used
   there. The source theorem assumes the rate 2 (inequality (2)); a general rate beta_L in (0, c+1-theta-kappa] is the
   corollary [LRT] (combined1 T4-113, CONFIRMED conditional). For 007, (B) is certified (rate > 2.00215, HISTORICAL)
   but the (A) items that eq (7) needs (bounded D rho, Lipschitz V, the decay |D^j rho| = O(r^(gamma-j)), j <= 2,
   behind the Hilbert-Schmidt extension) are recorded in [TF] 1565-1566 as "not checked". In combined2 these are the
   hypotheses BG-1 to BG-3 of theory_v01. The qualitative decay statements of numerical_audit/research/background_regularity
   cover them; the theory auditor independently CONFIRMED that proof as AT-013 (qualitative, constants unspecified).
2. R2: the source proves the L2 inverse for k in X_s ([L2] 50, 86), where U[k] is Lipschitz because X_s controls
   H^(2+s). The L2 argument itself ([L2] 90) uses only three properties of W_k = V + U[k]: global Lipschitz bound,
   at most linear growth and divergence 2c. So R2 applies to any k for which these three are known. For k in a
   weighted C^(1,alpha) ball K_{R,M}, the Lipschitz bound of U[k] is the prompt's R4.3, which has no located source
   (R4 row). In combined2 this is hypothesis FW-C2-main-v1:H(LIP).
3. R3 (eq (11)) is proved for h in the high domain D_s(A_k) and k in X_s with c[k] = 0. The strain formula in [S1C]
   48-49 is stated for C^(1,a) functions near 0 with sublinear growth. The identity F_y(0) = (c_l + ell - 1) a0 is
   CONFIRMED in this campaign (AT-005).
4. R5: the Schauder-Tychonoff mechanism (convex weakly compact K_{R,M}, weak continuity of T) has no located source.
   combined1 used the Banach contraction (12) on an X_s ball ([L2] 178). The pieces R5.2 (the Picard map T(k) = -A_k^(-1) F) and R5.4
   (the L2 Lipschitz estimate ||T(k)-T(l)||_2 <= (c_s r/2)||k-l||_2) are located ([L2] 68, 170-176).
5. R6: the L2 bound 2/(b+3) and the H^m unboundedness for (b+3)/2 < m < b+1 are located in [S1P] P5.2 and P5.4
   under the hypotheses 2 < lambda < 3 and sigma_src = a/d > lambda+2 of those propositions (sources' notation; for 007,
   lambda = b = 2.62 and sigma_src about 6.36, FLOAT). P5.x carry no status label in [S1P]. The weighted C^(1,alpha)
   statements R6.3 (angular damping a0 > b(1+alpha)-1) and R6.4 (delta > kappa_ang) have no located source.
6. R4, R7, R9, R10 and R11 have no located detailed source. In particular the exterior lifting R9.4 has a
   non-explicit constant C_R in the prompt itself, so no quantitative threshold can rest on it until its constant is
   made explicit.
7. Notation: the prompt's gamma = 1 - 1/c is the sources' delta; the sources' gamma is 1/c. The prompt's ell(h) is the
   sources' c[h].
8. The located proofs live in the Sobolev space X_s (H^(2+s) with weights, s <= 1/1024), not in the prompt's weighted
   Hoelder space. Any statement of R1 to R3 for the weighted Hoelder classes of combined2 uses only the three W_k
   properties in item 2 plus the C^1 regularity at the origin needed by the trace formula.
9. Frozen Sobolev rate (located, added in version 2). [S1P] P5.2, eq (3)-(4) (lines 2030-2075) gives the exact
   homogeneous-Sobolev decay rate of the frozen semigroup, delta_s = (lambda+3)/2 - s - (lambda-1) max(s - sigma_src, 0),
   with lambda = b and sigma_src = a0/d in the present notation. For s <= a0/d this is c + 1 - s. Its infinitesimal
   form, <|D|^s L_fr h, |D|^s h> = (s - c - 1)|| |D|^s h ||^2 + (s d - a0)||R1 |D|^s h||^2, is therefore a restatement
   of a located source and is not a new result of combined2. [S1P] P5.4 records the H^m unboundedness of the frozen
   resolvent for (b+3)/2 < m < b+1. THEORY_NEW_RESULTS.md NR-3 item 2 uses both only as sharpness remarks.

## Abbreviations

- [P] theory_agent_1/PROMPT.md (Part II is lines 203 to 1500)
- [L2] source/IPM/combined1/combined1.artifacts/audit/theory_audit/research_code/l2_closure/PROOF.md (198 lines). It is
  byte-identical (checked with cmp) to source/c1_full/combined1_theory_agent_4/research/l2_closure/PROOF.md.
- [ADD] source/c1_full/combined1_theory_agent_4/research/l2_closure/ADDENDUM.md
- [T2R] source/c1_full/combined1_theory_agent_4/research/l2_closure/source/T2_REVIEW_T4_019.md. This is the independent review of T4-019.
  [ADD] and [T2R] exist only in the c1_full copy. [IDX] line 26 cites them.
- [LRT] source/IPM/combined1/combined1.artifacts/audit/theory_audit/research_code/low_rate_trade_audit/PROOF.md
- [HS] source/IPM/combined1/combined1.artifacts/audit/theory_audit/research_code/gradient_commutator_audit/PROOF.md
- [OSF] source/IPM/combined1/combined1.artifacts/audit/theory_audit/research_code/origin_semigroup_floor/PROOF.md
- [IDX] source/IPM/combined1/combined1.artifacts/audit/theory_audit/research_code/INDEX.md
- [VL] source/IPM/combined1/combined1.artifacts/audit/theory_audit/VERDICT_LEDGER.md
- [NVL] source/IPM/combined1/combined1.artifacts/audit/numerical_audit/VERDICT_LEDGER.md
- [CR] source/IPM/combined1/combined1.report.md
- [TF] source/IPM/combined1/combined1.artifacts/reports/THEORY_FINAL.md
- [S1P] source/IPM/analysis2/IPM_Analysis_II.artifacts/S1_PROOFS.md
- [S1C] source/IPM/analysis2/IPM_Analysis_II.artifacts/S1_CLOSURE.md
- [A4] source/IPM/analysis4/IPM_Analysis_IV.report.md

## Conventions shared by the sources

- Riesz transforms, symmetry and U.
  - [L2] line 7: "All functions are real and S1, meaning even in x and odd in y. R_j has multiplier i xi_j/|xi|,
    U[h]=(-R1R2 h,R1²h)".
  - [S1P] line 535: "Thus R_1^2 has multiplier -xi_1^2/|xi|^2."
  - The symbol of U is therefore (xi1 xi2/|xi|^2, -xi1^2/|xi|^2). This is the prompt's m(xi) at [P] 967-971.
  - The same symbol is written out in source/c1_full/combined1_theory_agent_4/research/localized_low_audit/PROOF.md line 5: "Let U have
    Fourier symbol m(xi)=(xi_1 xi_2/|xi|^2,-xi_1^2/|xi|^2)".
  - All signs therefore agree with the prompt.
- Strain. ell(h) in the prompt is the sources' c[h].
  - [L2] line 66: "c[h]=partial_y U2[h](0)".
  - [S1C] line 49: "c[h] = d_y U_2[h](0)".
- Exponent names.
  - The prompt's gamma = 1 - 1/c ([P] 1150) is the sources' delta.
  - The sources' gamma is 1/c:
    - [A4] line 23: "Notation: $c=c_l>1$, $\delta=1-1/c$, $\gamma=1/c$".
    - [S1C] line 61: "gamma = 1/c_l".
    - [S1P] line 15122: "Write c=1/gamma, delta=1-gamma".
  - In [L2] (A), "gamma<1" is a growth exponent of rho. With gamma = 1/c, the bound |D rho| = O(r^(gamma-1)) is the
    decay O(r^(-delta)) that the prompt writes as <X>^(-gamma).

## Summary table

| R | Status | Main source | Audit status in source |
|---|---|---|---|
| R1 | source located | [L2] section 2, eq (7), lines 72-90; [HS] | T4-019 AUDITED conditional via T4-035 ([VL] 353); HS identity T4-016 CONFIRMED ([VL] 160) |
| R2 | source located | [L2] lines 58, 86, 90, section 5 lines 140-152; [ADD] 7-15 | as R1 |
| R3 | source located | [L2] lines 156-166, eq (11); [S1C] 48-49, 56-57; [S1P] P1.2, P2.1 | AUDITED (T4-035); [S1C] labels THEOREM |
| R4 | no detailed source located | only the L2 contraction of U ([L2] 174, [T2R] 88) | none |
| R5 | no detailed source for the Schauder-Tychonoff mechanism | R5.2 and R5.4 only: [L2] 68, 170-178, eq (12) | R5.4 part AUDITED with T4-019 |
| R6 | partly located | R6.1: [S1P] P5.4 2356-2358, P5.3 2190-2191, [OSF] 45-49; L2 bound: [S1P] P5.2 (4) at s=0 | P5.x carry no status label (see R6); [OSF] AUDITED with T4-145 ([IDX] 141, [VL] 1669) |
| R7 | no detailed source located | nearest [S1P] 2224 | none |
| R8 | R8.1 and R8.2 located only as the case l=0 of [L2] (12); R8.3 not located | [L2] 170-176 | with T4-019 |
| R9 | no detailed source located | nearest [S1P] P13.1 6382-6384, [A4] | none |
| R10 | no detailed source located | nearest [S1P] 1331, localized L2 audits in the previous campaign's theory agent 4 | none |
| R11 | no detailed source located | nearest frozen_adjoint_strip line 17 | none |

---

## R1. Signed L2 coercivity ([P] 211-314)

**Status.** Source located.
- [L2] section "## 2. Signed L2 estimate and inverse", lines 72-90. The estimate is eq (7) at line 88.
- Hypotheses: [L2] (A) and (B), lines 14-27.
- Hilbert-Schmidt input: [HS] lines 5-19.
- Variable-rate version: [LRT] lines 10-17 and 61-65.

**Hypotheses (verbatim).**
- [L2] 14: "Let rho be a smooth S1 reference, u=U[rho] its canonical velocity, V=cX+u, a0=rho_y(0)>0. Assume the
  following conditions."
- [L2] 16: "(A) Structure and normalization. 9/5<c<37/20; c+partial_y u2(0)=1. The fields in Analysis II(B0) are
  bounded: D rho, <r>D²rho, <r>²D³rho, <r>²D⁴rho, Du, <r>D²u and <r>D³u. In addition, for some gamma<1,
  |D^j rho|=O(r^(gamma-j)), j=0,1,2, outside a ball. The canonical u is smooth, divergence free and at most sublinear.
  These assumptions specify the background at the origin and infinity and make V globally Lipschitz and complete."
- [L2] 20-21:
  - "theta=ess sup (sqrt(rho_x²+rho_y²)-rho_y)/2,"
  - "kappa²=[(log2-1/2)||D rho_x||_2²+(3log2-2)||D rho_y||_2²]/(16pi)."
- [L2] 25: "c+1-theta-kappa >=2.                                     (2)"
- [L2] 27: "The seminorms are finite by(A). This condition replaces the baseline low negative-norm coercivity. It is a
  global condition, not a sampled one."
- [L2] 50: "For k in X_s define L=V.D-1+U[.].D rho and A_k=L+U[k].D."
- [HS] 5: "Let R_j be the real Riesz operator with Fourier multiplier i xi_j/|xi|. ... For real rho in
  C_c^infinity(R²), set a=rho_x, b=rho_y and"
- [HS] 7: "K=(1/2)[R1,[R1,b]]-(1/2)[R1,[R2,a]]."
- [HS] 11-12: "||K||_HS² = (log2-1/2)/(16pi) ||D rho_x||_2²" / "+ (3log2-2)/(16pi) ||D rho_y||_2².                 (1)"
- [HS] 19, the extension: "The identity extends to any smooth rho admitting compact smooth approximations whose
  Hessians converge in L² and whose gradients converge uniformly. This includes each smooth sublinear profile with
  |D^j rho(X)|=O(|X|^(gamma-j)), j=0,1,2, outside a ball, where gamma<1."

**Proof steps (verbatim).**
- [L2] 74: "Write a=rho_x, b=rho_y and Q=-aR1R2+bR1². Direct expansion gives"
- [L2] 76-78:
  - "Sym Q=P0+K,"
  - "P0=R1 b R1-(R1 a R2+R2 a R1)/2,"
  - "K=(1/2)[R1,[R1,b]]-(1/2)[R1,[R2,a]]."
- [L2] 82: "<P0 h,h>=integral[-b|R1 h|²+a(R1 h)(R2 h)]<=theta||h||_2²."
- [L2] 84: "Here sum_j||R_jh||²=||h||² and the largest eigenvalue of the two-by-two integrand matrix is theta pointwise.
  The independently audited gradient-structured identity gives ||K||<=||K||_HS=kappa. Its cutoff extension applies
  by(A)."
- [L2] 86: "The field V+U[k] has divergence2c, is globally Lipschitz and has at most linear growth: X_s controls
  H^(2+s), hence U[k] and DU[k] are bounded. Therefore, on compact smooth tests,"

**Conclusion (verbatim).**
- [L2] 88: "Re<A_k h,h> <= -(c+1-theta-kappa)||h||² <=-2||h||².        (7)"
- [T2R] 52-54: "4. Signed L2 estimate (7). div V = 2c and div U[k] = 0 (the symbol of div U is i xi1 (xi1 xi2) - i xi2
  xi1^2 = 0 over" / "|xi|^2) give Re<(V + U[k]).Dh, h> = -c ||h||^2, so Re<A_k h, h> = -(c + 1)||h||^2 + <Sym Q h, h>"
  / "<= -(c + 1 - theta - kappa)||h||^2. The U[k] term drops out, so the L2 bound is uniform in k. Checked."
- Variable rate:
  - [LRT] 17: "the signed low rate satisfies c+1-theta-kappa>=beta_L>0."
  - [LRT] 61: "The signed L2 decomposition and maximal transport argument of ../l2_closure/PROOF.md use the numerical
    value 2 only as a lower rate. With beta_L replacing 2, the same exact decomposition gives"
  - [LRT] 63: "Re<A_k h,h>_L2 <= -beta_L ||h||_2^2."

**Answer to question (a).**
- Hypotheses used in eq (7) and in the L2 semigroup bound (section 2, lines 72-90):
  - From (A):
    - V globally Lipschitz and complete (last sentence of line 16).
    - D rho bounded, which makes Q bounded on L2 (line 90).
    - The sublinear decay |D^j rho|=O(r^(gamma-j)), j=0,1,2. This is the condition under which the HS identity
      extends from C_c^infinity to the profile (line 84 "Its cutoff extension applies by(A)"; [HS] 19).
    - Finiteness of ||D rho_x||_2 and ||D rho_y||_2 (line 27 "The seminorms are finite by(A)").
  - From (B): the definitions of theta and kappa, and the inequality (2) that turns the rate into 2.
  - Section 2 does not cite (C) or (D). They enter the high-norm rate (5) in sections 3 to 5.
  - Section 2 also does not invoke the parts of (A) that fix the origin: the range 9/5<c<37/20 and the normalization
    c+partial_y u2(0)=1.
- theta and kappa: exact formulas at [L2] 20-21 as quoted. The constants are (log2-1/2)/(16pi) and (3log2-2)/(16pi);
  [HS] 11-12 states the same identity.
- Transport identity. [L2] never displays <V.Dh,h> = -c||h||^2. It is implicit in line 86 ("The field V+U[k] has
  divergence2c"). It is written explicitly only in [T2R] 52-53, as Re<(V + U[k]).Dh, h> = -c ||h||^2.
- Core. The estimate is proved "on compact smooth tests" (line 86), that is, compact smooth S1 functions (line 7). It is
  then extended to the maximal L2 domain (line 90: "The core estimate(7) extends to that domain").

**Differences from the prompt.**
1. Rate.
   - R1.1 asks only for beta_0 = c+1-theta-kappa > 0.
   - [L2] (7) displays the rate c+1-theta-kappa, but the theorem assumes (2), c+1-theta-kappa >= 2, and records the
     bound as -2||h||^2.
   - A general positive rate is the separate corollary [LRT] (T4-113). [LRT] still lists the full hypotheses 1 to 4,
     including the derivative caps.
2. kappa.
   - The prompt says kappa comes from "an explicit Riesz-kernel estimate".
   - In the source, kappa is the exact Hilbert-Schmidt norm of the double commutator K, with an exact closed form.
     ||K|| <= ||K||_HS is the only inequality used.
3. Space.
   - All functions in the source are S1.
   - The estimate is proved on compact smooth S1 tests, not for "sufficiently regular, decaying h".
4. Extension to A_k.
   - The prompt says "For any sufficiently regular k". The source requires k in X_s (line 50), because U[k] must be
     Lipschitz (line 86).
   - No smallness of k is used ([T2R] 54). This matches the prompt's line 312.
5. Bound for the nonlocal term. The bound <U[h].grad rho, h> <= (theta+kappa)||h||^2 at [P] 250-251 is exactly
   <Sym Q h,h> = <P0 h,h> + <K h,h> with Qh = U[h].D rho ([L2] 74, 82, 84). Its form and constants match.
6. theta. The prompt's formula at [P] 258-261 is the same as [L2] 20. The source stresses that it is a global
   essential supremum ([L2] 27; [T2R] 118).
7. Status for Candidate 007.
   - [TF] 1565: "| :H1 decay (A) | far-field decay of D^j rho, j <= 2 | not checked | closure matrix row 56 |"
   - [TF] 1566: "| :H1 list | A2 (B0n) boundedness list | not checked | row 56 |"
   - So for 007 only (B) is certified ([TF] 1567).
   - The (A) items that eq (7) needs (bounded D rho, Lipschitz V and the decay behind the HS extension) are recorded
     as not checked.

**Audit status.**
- T4-019, [VL] header 182, verdict line 188: "Verdict: CONFIRMED by the author; CLAIMED under coordinatorv03 until an
  independent Opus theory agent reviews this new theorem."
- T4-035, [VL] header 348, line 353: "Result and verdict: CONFIRMED. T4-019 is now AUDITED as a conditional theorem
  under (A)-(D), F in X_s and X_s(F)<=1/163840."
- [IDX] 26: "AUDITED conditional theorem".
- [ADD] 5: "The framework is now AUDITED under the campaign contract."
- [L2] line 198 still reads "It remains CLAIMED until an independent Opus theory agent checks". The entries above
  supersede it.
- HS identity, T4-016, [VL] header 153, line 160: "Verdict: CONFIRMED by independent cross-agent proof audit; eligible
  for AUDITED under coordinator amendment v03."
- [LRT] T4-113, [VL] header 1218, line 1223: "Result and verdict: CONFIRMED conditional on all stated background,
  residual membership and smallness hypotheses."

---

## R2. Existence of the frozen L2 inverse ([P] 318-392)

**Status.** Source located.
- [L2] lines 58, 86 and 90.
- High-space realization and maximal domain: [L2] section 5, lines 140-152.
- L2 consistency argument: [ADD] 7-15.
- Review: [T2R] 55-56.
- Variable rate: [LRT] 43 and 65.

**Hypotheses (verbatim).**
- [L2] 50: "For k in X_s define L=V.D-1+U[.].D rho and A_k=L+U[k].D. The maximal domain is"
- [L2] 52: "D_s(A_k)={h in X_s: A_k h in X_s as a distribution}."
- [L2] 86, as quoted under R1 ("X_s controls H^(2+s), hence U[k] and DU[k] are bounded").
- X_s:
  - [L2] 12: "For0<s<=1/1024 let X_s be the corresponding completion in X_s(h)=E(J^s h)."
  - [L2] 9-10: "E(h)²=P(h)²+2^14 a(h)²+2^18 b(h)²," / "P=||omega D²h||_2, a=||Dh||_2, b=||h||_2.                  (1)"
  - [L2] 7: omega=(1+4|X|²)^(2/5).

**Conclusion (verbatim).**
- [L2] 58: "On L² its consistent maximal-domain inverse has norm at most1/2, independent of k."
- [L2] 90: "The complete Lipschitz transport flow defines a strongly continuous L² group. Its generator is maximal
  distributional transport, by mollification and radial cutoff. Q is a bounded L² operator because D rho is bounded.
  Bounded perturbation defines A_k on the same maximal domain. The core estimate(7) extends to that domain and gives
  semigroup norm at most exp(-2t). The integral -integral_0^infinity exp(tA_k)f dt is therefore in the generator domain
  and is the inverse with norm at most1/2. A kernel element has a constant, exponentially decaying orbit and is zero.
  This proves both onto and one-to-one statements, without a trace assumption on general L² inputs."
- [T2R] 55-56: "The L2 realization (Lipschitz complete flow of V + U[k], whose generator is maximal transport; Q bounded
  on L2 since" / "D rho is bounded; Lumer-Phillips) is standard and correct as stated."
- [LRT] 65: "The divergence-free transport U[k].D contributes zero. The complete Lipschitz flow and bounded coupling
  generate the maximal L2 semigroup with decay exp(-beta_L t); its integral gives the inverse bound."

**Answer to question (b).**
- What is assumed about U[k]: k in X_s (line 50). The Lipschitz bound and linear growth of V+U[k] are derived from
  "X_s controls H^(2+s), hence U[k] and DU[k] are bounded" (line 86) together with (A) for V.
- Core: compact smooth tests (line 86).
- Domain:
  - In L2, the maximal distributional transport domain (line 90).
  - In X_s, the maximal domain D_s(A_k) (line 52). It is identified with the restriction of the L2 generator in lines
    148-152, with the L2 consistency step supplied in [ADD] 7-15.
- Independence of k: the L2 inverse bound is independent of k ([L2] 58; [T2R] 54).
- Form of the bound: the semigroup bound is stated as exp(-2t), not as exp(-beta_0 t). With [LRT] it is
  exp(-beta_L t) for any 0 < beta_L <= c+1-theta-kappa.

**Differences from the prompt.**
1. Rates. The source states the rate 2 and the inverse bound 1/2, not beta_0 and 1/beta_0. The beta_L form is [LRT]
   (T4-113).
2. Source of the Lipschitz property.
   - The prompt assumes W_k globally Lipschitz with at most linear growth.
   - The source obtains this from k in X_s. For k only in the prompt's weighted C^{1,alpha} set K_{R,M}, the source
     does not state that U[k] is Lipschitz.
   - The L2 argument in line 90 uses only these properties of W_k: Lipschitz, linear growth and divergence 2c.
3. Domain. The prompt's natural domain D_k = {h in L2: W_k.grad h in L2} is the source's "maximal distributional
   transport" domain, because the remaining part is bounded on L2.
4. Sign. The source's inverse "-integral_0^infinity exp(tA_k)f dt" solves A_k h = f. The prompt's R2.1 solves
   A_k h = -F. The two agree.
5. Detail. The semigroup construction is asserted in a few sentences: line 90 says "by mollification and radial
   cutoff", and [T2R] calls it "standard". No longer written proof of the generator identification exists in these
   files.

**Audit status.** Same as R1: T4-019 AUDITED through T4-035 ([VL] 353). [LRT] is T4-113 CONFIRMED conditional
([VL] 1223).

---

## R3. Origin normalization is preserved ([P] 396-500)

**Status.** Source located.
- [L2] lines 156-166, eq (11).
- [S1C] lines 48-49 (strain functional) and 56-57 (center identity).
- [S1P] P1.2, lines 527-595 (U(0), DU(0) and DV(0)), and P2.1, lines 599-640 (strain formula).
- Review: [T2R] 82-86.

**Hypotheses (verbatim).**
- [L2] 156: "The Fourier embedding gives X_s subset H^(2+s) subset C^(1,alpha) for every0<alpha<s. It also gives
  |c[h]|<=c_s X_s(h), so c is a continuous functional on X_s."
- [L2] 162: "If k has c[k]=0 and h in D_s(A_k) solves A_k h=f, first-order expansion at the origin yields"
- [S1C] 48: "- Strain functional: for h in C^(1,a) near 0 with sublinear growth,"
- [S1C] 56: "- Center identity (THEOREM): for C^1 functions k, h in the classes below and f = (L + U[k].grad) h,"
  - "the classes below" are the completions E_2, X and N_s of [S1C] section 2, lines 65-80.
- [S1P] 531: "Start with a real smooth density h on R^2, even in x and odd in y, which is Schwartz."
- [S1P] 603: "Let h be a real Schwartz function on R^2, even in x and odd in y."

**Conclusion (verbatim).**
- [L2] 164: "f_y(0)=(c+c[rho]-1+c[k])h_y(0)+a0c[h]=a0c[h].            (11)"
- [L2] 166: "Thus the high inverse maps the zero-forcing-jet hyperplane into ker c, and conversely. The actual normalized
  residual satisfies F_y(0)=0 by the same expansion of V.D rho-rho. Parity makes U[h](0)=0, so no constant term was
  omitted."
- [S1C] 57: "f_y(0) = (c_l + c[rho_tilde] - 1 + c[k]) h_y(0) + a_0 c[h], a_0 = d_y rho_tilde(0)."
- [T2R] 84-85: "d_y(A_k h)(0) = (c + d_y u2(0) - 1 + c[k]) h_y(0) + rho_y(0) c[h]. With c + d_y u2(0) = 1 and c[k] = 0
  this is" / "a0 c[h]. Also F_y(0) = (c + d_y u2(0) - 1) a0 = 0. Checked."
- R3.2: [S1P] 537: "DU[h](0)=diag(-c[h],c[h]),      c[h]=psi_xy(0)."
- R3.1:
  - [S1P] 545: "Put d=c[rho]. The background field has derivative diag(c_l-d,c_l+d) at zero."
  - With c_l+d=1 this is diag(2c_l-1,1). [OSF] 12 takes "DV(0)=diag(2c-1,1)" as an explicit hypothesis. [OSF] 14
    says these "follow from the usual parity, divergence and normalized vertical strain conditions".
- R3.4 in frozen form: [S1P] 2242: "the transport-minus-identity part has zero y-jet, while (aR1^2 h)_y(0)=a c[h]."
- Strain formula:
  - [S1C] 49: "c[h] = d_y U_2[h](0) = -h_y(0)/4 + (1/pi) PV int sin(3 theta) h(X) r^-3 dX (THEOREM)."
  - [S1P] 605: "c[h] = -b/4 + (1/pi) lim_{epsilon -> 0} integral_{|X|>epsilon} sin(3 theta) h(X)/r^3 dX.       (1)",
    with b=partial_y h(0) ([S1P] 603).
  - [L2] 158: "c[h]=-h_y(0)/4+(1/pi)PV integral sin(3theta)h(X)|X|^-3 dX."

**Answer to question (c).**
- Identity: [L2] 164, quoted above. It is proved for k in X_s with c[k]=0 and h in D_s(A_k), which is a subset of X_s
  inside H^(2+s) and C^(1,alpha) for alpha<s<=1/1024.
- [S1C] states the same identity as a THEOREM for C^1 functions in its correction classes.
- The strain formula is at [S1C] 48-49, with hypothesis "h in C^(1,a) near 0 with sublinear growth".
  - Its proof is [S1P] P2.1, for Schwartz S1 h ([S1P] 603).
  - [S1P] 640 gives the extension: "Extension to the growing numerical profile needs a tail condition and the same
    canonical inverse. For h=O(r^beta) with beta<1 and appropriate derivative decay, the center kernel is absolutely
    integrable at infinity".
- The T4-019 proof does not use the contact formula:
  - [ADD] 17: "R3 does not independently audit the contact formula; that formula is not used for the inverse,
    normalization or contraction argument. The Fourier trace bound and origin identity suffice."
  - [T2R] 115 says the same.

**Differences from the prompt.**
1. Space. The prompt states R3 for k, h in C^{1,alpha}. The audited source proves it in X_s, which embeds in
   C^(1,alpha) only for alpha < s <= 1/1024. [S1C] states it for C^1 functions in its classes E_2, X and N_s. No
   source states it for the prompt's weighted C^{1,alpha} class. Existence of c[k] for C^{1,a} with sublinear growth is
   [S1C] 48.
2. Form.
   - The source identity is for f = A_k h, with the coefficient (c + c[rho] - 1 + c[k]).
   - The prompt's R3.5 is the same identity with f = -F, after using the normalization c + c[rho] = 1 from (A).
   - [L2] 164 then uses c[k]=0 to get f_y(0) = a0 c[h].
3. F_y(0)=0. The prompt assumes F_y(0)=0. The source derives it for the actual residual ([L2] 166; [S1P] 551
   "partial_y F(0)=a(c_l+d-1)").
4. Normalized chart. [S1P] P1.2 also uses a normalized-chart operator, line 559: "L h = Vbar dot grad h-h + (U[h]-c[h]X)
   dot grad rhobar." For it, partial_y(Lh)(0)=0 (line 577). That operator has a rank-one term and is not the prompt's
   L; the prompt's L has none. The prompt's R3.4 matches the unnormalized operator, as in [VL] T4-146 line 1587
   ("use (Lh)_y(0)=a0 c[h]").
5. No second derivative. The prompt's remark that no second derivative is needed agrees with the "first-order
   expansion" of [L2] 162.

**Audit status.**
- [L2] (11) is part of T4-019, AUDITED via T4-035 ([VL] 353). [T2R] step 10 (line 85) is marked "Checked".
- [S1C] marks the strain functional, the automatic normalization and the center identity as THEOREM (lines 49, 53,
  56). Per [S1C] 37, THEOREM means "proof checked by an independent verification".
- [S1P] 640 calls P2.1 "classical/distributional identities, with a complete informal proof".

---

## R4. L2 to C^{1,alpha} interpolation ([P] 504-607)

**Status.** No detailed source located.
- No source contains the first-moment identity on a ball, A = 2/sqrt(pi) together with B_alpha =
  16/(pi(1+alpha)(4+alpha)), or the bounds R4.2 and R4.3.

**What was searched.** grep over all .md, .txt and .tex files under source/ for:
- "first-moment" and "first moment". Many hits, all about multipole or annular moments, for example
  source/c1_full/combined1_coordinator/FINAL_REPORT.md lines 2595-2599. None is in an interpolation context.
- "16/(pi", "(4+alpha)", "4 + alpha", "H_{sigma,alpha}", "H_(sigma,alpha)". No hits.
- "2/sqrt(pi)". Only unrelated product estimates, [S1P] 17368, 17438 and 17577.

**Nearest items.**
- The one ingredient that is located is ||U[k]||_2 <= ||k||_2:
  - [L2] 174: "Since U is an L² vector contraction".
  - [T2R] 88: "||U[h]||_2^2 = int xi1^2/|xi|^2 |h^|^2 <= ||h||_2^2".
- Sobolev-to-Lipschitz embeddings, not interpolation:
  - [S1C] 78-79: "||grad h||_inf and ||DU[h]||_inf are at most c_s N_s(h) with c_s = [2 (pi s (1 + s))^(1/2)]^-1".
  - [L2] 156.
- Other interpolation inequalities in [S1P]:
  - P44.1, line 11501: "||f||_infinity <= (1/2) sqrt(||f||_2 ||D2 f||_2).      (2)"
  - P48.1, lines 12088-12090: "||f||_infinity <= C ||f||_(Hdot^-1)^(1/3)" / "||D2 f||_2^(2/3)," /
    "C=2^(-5/6)3^(-1/4).". Neither is L2 to C^{1,alpha}.
- [L2] 184-188, eq (13): a weighted Bessel/Fourier interpolation for the forcing norm, a different statement.

**Differences / audit status.** Not applicable. The prompt's statement that "The interpolation estimates are
established" ([P] 603) has no detailed earlier source in this workspace; R4 is IMPORTED from PROMPT Part II, which is the reference.

---

## R5. Conditional nonlinear fixed-point theorem ([P] 611-794)

**Status.** No detailed source located for the Schauder-Tychonoff mechanism of [P] 673-750. That covers the set
K_{R,M}, weak compactness, weak continuity and Schauder-Tychonoff, cited at [P] 746. The following parts are located:
- R5.2: [L2] 68 and 170.
- R5.4: [L2] 172-176, eq (12); [T2R] 87-89; [LRT] 84.

**What was searched.** "Tychonoff", "Tychonov", "Schauder", "K_{R,M}", "K_(R,M)", "weakly compact", "weakly
continuous".
- "Schauder" occurs only in literature files and prompts: source/IPM/Holder/holder.report.md, the Holder
  04_literature files, source/IPM/analysis2/IPM_Analysis_II.prompt.md, and Euler references in c1_full.
- The other patterns returned nothing.
- combined1 used the Banach contraction theorem:
  - [L2] 178.
  - source/IPM/combined1/combined1.artifacts/audit/theory_audit/research_code/transient_low_closure/PROOF.md line 143:
    "so the contraction theorem proves existence and uniqueness in B".
  - nonlinear_audit/PROOF.md line 108 (same directory) uses weak compactness only for completeness of the ball.

**Hypotheses and context of eq (12) (verbatim), answering question (e).**
- [L2] 66: "B={h in X_s: X_s(h)<=r, c[h]=partial_y U2[h](0)=0}"
- [L2] 62: "s=2^-17, r=2^-14, eta=1/163840=r/10.                      (6)"
- [L2] 168: "The ball B is complete in L²: an L² Cauchy sequence in B has a weak X_s convergent subsequence, whose image
  in distributions is the given L² limit. Lower semicontinuity preserves the radius and continuity of c preserves the
  constraint. This also proves uniqueness of the high limit as a distribution."
- [L2] 170: "Let beta=1/4-4800s-5r/sqrt(s). Under(6), beta>1/10 by the exact/Arb calculation supplied separately.
  Therefore T(k)=-A_k^-1F maps B into itself by(5),(11) and X_s(F)<=r/10. For k,l in B, common L² domains give"
- [L2] 172: "A_k(T(k)-T(l))=U[l-k].D T(l)."
- [L2] 174: "Since U is an L² vector contraction and ||D T(l)||_infinity<=c_s r,"
- [L2] 176: "||T(k)-T(l)||_2 <=(c_s r/2)||k-l||_2.                    (12)"
- [L2] 178: "The right side is an L² product; no unbounded high nonlinear map is invoked. With(6), c_s r<0.006234, so the
  ratio is less than0.00312. The contraction theorem on B gives the unique fixed point and hence the exact stationary
  equation. Conversely, any stationary h in B belongs to D_s(A_h), because A_h h=-F is in X_s, and high inverse
  uniqueness makes it a fixed point."
- [T2R] 87-89: "11. Fixed point. A_k(T(k) - T(l)) = -U[k - l].D T(l) (both T(k), T(l) lie in the L2 maximal domain of
  A_k because" / "A_k T(l) = -F + U[k - l].D T(l) is in L2). ||U[h]||_2^2 = int xi1^2/|xi|^2 |h^|^2 <= ||h||_2^2, and" /
  "||D T(l)||_inf <= c_s X_s(T(l)) <= c_s r, so the L2 Lipschitz constant is c_s r/2 by the uniform L2 inverse."
- [LRT] 84: "Subtracting the two equations gives A_k(T(k)-T(l))=U[l-k].D T(l). The low inverse, the L2 contraction of U
  and the gradient bound imply contraction factor c_s r/beta_L<1. Banach's theorem proves existence and uniqueness in
  the ball."

**Differences from the prompt.**
1. Fixed-point theorem. The source proves existence by the Banach contraction in the L2 metric on an X_s ball. The
   prompt's statements "Existence does not require contraction" ([P] 762) and "This entire conditional fixed-point
   mechanism is established" ([P] 766) have no detailed earlier source here; they are IMPORTED from PROMPT Part II.
2. Invariant set.
   - Source: an X_s ball, a weighted H^(2+s)-type norm with radius r = 2^-14, plus c[h]=0.
   - Prompt: K_{R,M}, an L2 ball intersected with a weighted C^{1,alpha} ball.
   - The source proves invariance from the high semigroup bound (5) and X_s(F) <= r/10 (line 170). It does not
     assume an analogue of R5.3.
3. R5.4.
   - Sign: [L2] 172 writes U[l-k].D T(l), which equals the prompt's -U[k-l].grad T(l) ([T2R] 87).
   - Constant: the source has ||D T(l)||_inf <= c_s r from the X_s bound, and 1/2 from the rate 2, giving c_s r/2.
     The prompt has ||grad T(l)||_inf/beta_0. [LRT] has c_s r/beta_L.
4. Weak closure. Weak lower semicontinuity and completeness of the ball appear only in the form of [L2] 168: weak X_s
   compactness in a Hilbert high space. The prompt's local C^{1,beta} compactness argument for a weighted Holder ball
   does not appear.

**Audit status.** The R5.2 and R5.4 parts are inside T4-019, AUDITED via T4-035 ([VL] 353). The Schauder-Tychonoff
part: no detailed earlier source located; IMPORTED from PROMPT Part II (R5), which is the reference. A missing earlier
source file does not remove the authority the run specification assigns to the Part II statement (wording of the theory audit exchange audit_v12).

---

## R6. Exact frozen-origin inverse ([P] 798-956)

**Status.** Partly located. Each of P5.1, P5.2, P5.3, P5.4 and P5.5 below states its scope verbatim.
- R6.1: located in an equivalent form with the same normalization.
- The L2 bound 2/(b+3): located.
- The identity R6.2 with the term a0||R_1 h||^2: not written in any source.
- Same-order unboundedness: located for H^m and for C^(2,delta), not for L2 intersected with C^{1,alpha}.
- R6.3 and R6.4: not located.

**Parameter map.** The sources write lambda = b = 2c_l - 1, a = a0, d = lambda - 1 = b - 1 and sigma = a/d. The source
L0 = lambda x partial_x + y partial_y - 1 + a R1^2 is the prompt's L_fr ([P] 805-811).

**Answer to question (d): statements (verbatim).**

P5.1 ([S1P] header 1886: "### P5.1. A direct Holder inverse with a contractive heat norm"):
- 1890: "Fix lambda>1, a>0 and sigma=a/(lambda-1)>4. Let 0<alpha<1 and put r=sigma-alpha>0. On the real Schwartz core
  S_ann with smooth compact Fourier support away from zero define"
- 1892: "N_heat(h)=sup_(t>0) t^(r/2) ||exp(t Delta) Lambda^sigma h||_infinity."
- 1896: "L0=lambda x partial_x+y partial_y-1+a R_1^2."
- 1900: "N_heat(L0^(-1)f) <= (1-alpha)^(-1) N_heat(f).                  (1)"
- 1902: "Its domain is precisely the set of h in X_heat for which the strong derivative at zero of the semigroup
  exists. The norm N_heat is equivalent on S_ann to the homogeneous C^alpha seminorm. Thus (1) is a same-order inverse
  for h itself. It is not an inverse for the normalized full operator, and it does not impose or control a center
  derivative trace."
- 1998-1999: eq (8), "[L0^(-1)f]_C^alpha <= A_(sigma,alpha) B_(sigma,alpha)" / "(1-alpha)^(-1) [f]_C^alpha."
- 2005: "The normalized frozen rank term -a c[h]y is absent and globally linear y is outside this completion."

P5.2 ([S1P] header 2007: "### P5.2. The complete fixed-coefficient operator in Sobolev and Hoelder spaces"):
- 2011: "Let lambda>1 and a>0, let sigma=a/(lambda-1), and put"
- 2013-2015: "D=lambda x partial_x+y partial_y," / "L0=D-1+a R_1^2," / "Lambda=(-Delta)^(1/2)."
- 2017: "This L0 is the fixed-coefficient principal part. It does not include the normalized rank-one term -a c[h]y."
- 2019: "Let S_ann be the real Schwartz functions whose smooth Fourier transforms have compact support away from zero.
  We may restrict to functions even in x and odd in y".
- 2029: "Lambda^sigma L0=(D+sigma-1)Lambda^sigma.                         (1)"
- 2040: "Put A_t=diag(exp(lambda t),exp(t)) and T_t f(X)=f(A_t X). Formula (1) yields"
- 2042: "S_t h = exp((sigma-1)t) Lambda^(-sigma) T_t Lambda^sigma h,       (2)"
- 2052-2054: "For real s let Hdot^s be the Hilbert completion of S_ann in the norm" /
  "||h||_Hdot^s^2=(2 pi)^(-2) integral |xi|^(2s)|hhat(xi)|^2 dxi."
- 2058: "||S_t|| = exp([s-(lambda+3)/2+(lambda-1)max(s-sigma,0)]t).        (3)"
- 2064: "delta_s=(lambda+3)/2-s-(lambda-1)max(s-sigma,0)."
- 2068-2069: "L0^(-1)f=-integral_0^infinity S_t f dt," / "||L0^(-1)f||_Hdot^s <= delta_s^(-1)||f||_Hdot^s. (4)"
- 2093: "Take 0<alpha<min(1,sigma), and set beta=alpha-sigma<0."
- 2097: "It is a little homogeneous Hoelder realization: norm (5) is equivalent to the ordinary homogeneous C^alpha
  seminorm on the core. In particular it controls h itself and does not require h_x as a primary unknown."
- 2160: "It does not control c[h], which is unbounded on an ordinary C^alpha space for alpha<1. It also does not include
  the normalized rank-one term, variable coefficients, tail coordinates, phase conditions, forcing compatibility, or the
  nonlinear derivative loss."

P5.3 ([S1P] header 2162: "### P5.3. Frozen inverse: the strain trace, finite regularity and a singular normalization
matrix"):
- 2172: "Assume 2<lambda<3 and sigma>lambda+2, as holds for both exact checkpoint parameter sets. Let R0 be the inverse
  already constructed in section P5.1. For every Schwartz forcing f with density parity, R0 f is bounded and belongs to
  C^(2,delta) for every 0<delta<lambda-2."
- 2174: "c[R0 f]=partial_y f(0)/a.                                 (1)"
- 2178: "For the analytic Schwartz forcing f=y exp(-r^2), h=R0 f fails to belong locally to C^(2,delta) for every
  delta>lambda-2. In particular it is not C^3."
- 2190-2191: "S_t f(X)=(2pi)^(-2) exp((sigma-1)t)" / "integral exp(i X.A_t xi) |xi|^sigma |A_t xi|^(-sigma) fhat(xi)
  dxi.  (2)"
- 2197: "F_k(f)=integral_0^infinity r^(k+1) sup_theta |fhat(r cos theta,r sin theta)| dr."
- 2207-2209: "Whenever m<=sigma-2," / "||D^m S_t f||_infinity <= (2pi)^(-1) exp((m-lambda)t) F_m(f). (4)"
- 2213: "||D^m R0 f||_infinity <= F_m(f)/[2pi(lambda-m)].             (5)"
- 2219-2222: "If k=m+delta<lambda and k<=sigma-2," / "[D^m R0 f]_(C^delta)" /
  "<= 2^(1-delta) F_(m+delta)(f)/[2pi(lambda-m-delta)].       (6)"
- 2224: "Multiplying (2) by either velocity multiplier changes these upper bounds by at most one in Euclidean vector
  norm, because the vector velocity symbol has length at most one."

P5.4 ([S1P] header 2295: "### P5.4. Schwartz forcing, H3 regularity and an unbounded outgoing H3 inverse"):
- 2299: "Let L0=lambda x partial_x+y partial_y-1+a R1^2, d=lambda-1>0, sigma=a/d, with the exact checkpoint parameters.
  Thus 2<lambda<3 and sigma>lambda+2."
- 2301: "Every Schwartz density-parity forcing has R0 f in H^3. Nevertheless this outgoing inverse has no bounded
  extension H^3 to H^3. These are compatible statements: the first estimate uses a stronger angular Fourier-supremum
  norm."
- 2303-2311: "More generally, if 0<=m<lambda+1 and m<=sigma-1, define" / "G_m(f)=integral_0^infinity r^(2m+1)" /
  "sup_theta |fhat(r cos theta,r sin theta)|^2 dr." / "Then" / "||Lambda^m R0 f||_2" /
  "<=sqrt(G_m(f)/(2pi))/(lambda+1-m).                   (1)"
- 2313-2315: "The outgoing H^m inverse is unbounded whenever" / "(lambda+3)/2<m<lambda+1,  m<=sigma-1.  (2)"
- 2348-2350: the test sequence is supported at near-vertical frequencies: "For T>=1 set epsilon=e^(-dT), and let" /
  "fhat_T(xi)=-i epsilon^(-1/2) A(xi_1/epsilon) B(xi_2)."
- 2356-2358: "(S_t f_T)hat(eta)" / "=e^((sigma-lambda-2)t)|A_t^-1 eta|^sigma |eta|^-sigma" / "fhat_T(A_t^-1 eta)."
- 2367: "      >=[ell 2^-sigma/(10pi)] e^((m-(lambda+3)/2)T).        (4)"
- 2389: "These conclusions concern the complete coupled frozen operator and its specified outgoing inverse. They do not
  automatically transfer to the variable-coefficient normalized operator."

P5.5 ([S1P] header 2391: "### P5.5. Endpoint regularity and the leading nonclassical center term"):
- 2397-2400: "L0 = lambda x partial_x + y partial_y - 1 + a R1^2," / "d = lambda - 1,  sigma = a/d," /
  "with 2 < lambda < 3 and sigma >= 5."
- 2402-2403: "F_j(f) = integral_0^infinity r^(j+1) sup_theta |fhat(r,theta)| dr," / "C_j = F_j(f)/(2 pi)."
- 2405-2408: "Then h = R0 f and its canonical velocity belong to C^(2,lambda-2) on the full plane, with the explicit
  endpoint bound" / "[D^2 h]_(C^(lambda-2))" / "<= C_3/(3-lambda) + 2 C_2/(lambda-2).                 (1)"
- 2410: "It uses regularity of the forcing; it is not a bounded inverse theorem on the corresponding Hoelder space of
  arbitrary inputs."
- 2412-2426: for f = y exp(-x^2-y^2), "partial_y h(0,y) - partial_y h(0,0)" "= C_(d,sigma) |y|^d + o(|y|^d)" with
  C_(d,sigma) > 0 (eq (2), (3)).

**Does R6.1 appear with the same normalization?** Yes, in equivalent form.
- Check of [S1P] 2356-2358. With A_t = diag(e^(lambda t), e^t) we have
  |A_t^-1 eta|^sigma = e^(-sigma t)(e^(-2dt) eta1^2 + eta2^2)^(sigma/2). The factor
  e^((sigma-lambda-2)t)|A_t^-1 eta|^sigma|eta|^-sigma therefore equals
  e^(-(lambda+2)t)((e^(-2dt) eta1^2 + eta2^2)/|eta|^2)^(a/(2d)).
- With lambda = b and a = a0, this is the R6.1 integrand e^{-(b+2)t}(...)^{a_0/(2d)} hat F(e^{-bt}xi1, e^{-t}xi2).
- The source's R0 = -integral S_t solves L0 h = f. So h = integral S_t F dt solves L_fr h = -F, exactly as in R6.1.
- [S1P] 2190-2191 is the same semigroup in physical space.
- [OSF] 45-49 gives the forward evolution in Fourier variables:
  "what(t,xi)=exp(-(2c+1)t-a0 integral_0^t p(exp(-sD)xi) ds)" / "what0(exp(-tD)xi)," / "p(eta)=eta_x^2/|eta|^2."
  Here 2c+1 = b+2. Integrating p along the flow gives the same factor ((e^(-2dt)xi1^2+xi2^2)/|xi|^2)^(a0/(2d)).
- [OSF] 53 gives the Fourier equation: "partial_t what=-(Dxi).grad_xi what-(2c+1)what-a0 p(xi)what." This matches the
  operator at [P] 828-835.
- The check above is my algebra on the quoted formulas, not a new result.

**What P5.4 proves.** The outgoing inverse R0 has no bounded extension H^3 to H^3. More generally it is unbounded on
H^m for (lambda+3)/2 < m < lambda+1 and m <= sigma-1 (2313-2315). The test packets are concentrated near the vertical
frequency axis (2348-2350). Individual Schwartz forcings still give R0 f in H^3, controlled by the angular
Fourier-supremum norm G_m (2301-2311). The space is H^m, not L2 intersected with C^{1,alpha}.

**R6.2 and the L2 bound.**
- The identity -Re<L_fr h,h> = ((b+3)/2)||h||^2 + a0||R_1 h||^2 is not written in any source.
- The prompt's consequence ||h||_2 <= 2/(b+3)||F||_2 is P5.2 (4) at s = 0. There max(-sigma,0) = 0, so
  delta_0 = (lambda+3)/2, and Hdot^0 with the (2 pi)^(-2) normalization of 2054 is L2.
- P5.2 (3) at s = 0 gives the exact semigroup norm exp(-(lambda+3)t/2) on L2. So the a0||R_1 h||^2 term does not
  improve the L2 rate.

**Differences from the prompt.**
1. Same-order unboundedness ([P] 880-890).
   - The prompt places it on L2 intersected with C^{1,alpha}.
   - The sources prove it on H^m, for (lambda+3)/2 < m < lambda+1 (P5.4).
   - They also give a regularity ceiling C^(2,lambda-2) for smooth forcing (P5.3 line 2178; P5.5).
   - The Holder results P5.1, P5.2 (Holder part), P53.1 ([S1P] 12791) and P66.2 / P67.2 ([S1P] 14961, 15104) give
     bounded same-order inverses on C^alpha for h itself, not on C^{1,alpha}.
   - No source states C^{1,alpha} unboundedness.
2. R6.3 (a0 > b(1+alpha)-1), kappa_ang = alpha/(b-1), and R6.4 (<X>^nu F in C^{1+alpha+delta}, with the choice
   alpha=1/2, delta=0.4, nu=7/4): not found.
   - Nearest is P5.3 (5)-(6) with m=1 and delta=alpha. It bounds ||D R0 f||_inf and [D R0 f]_(C^alpha) by the
     angular-supremum Fourier moments F_1(f) and F_(1+alpha)(f).
   - Its hypotheses are 1+alpha < lambda and 1+alpha <= sigma-2 (2219), inside the standing assumption 2<lambda<3,
     sigma>lambda+2 (2172).
   - The source condition is on sigma = a0/(b-1), not a0 > b(1+alpha)-1. The source norm is a Fourier moment, not a
     weighted physical Holder norm.
   - In P5.2 (3) the competition between damping and horizontal stretching enters through the term
     (lambda-1)max(s-sigma,0), on Hdot^s.
3. The P5.3, P5.4 and P5.5 statements need 2<lambda<3 and sigma>lambda+2, and sigma >= 5 for P5.5. P5.1 needs sigma>4.
   - The sources do not check these for Candidate 007.
   - For orientation only: with c_l = 4076476460239181/2^51 ([NF] source/IPM/combined1/combined1.artifacts/reports/
     NUMERICS_FINAL.md line 9) and the FLOAT value a_0 = 10.3120 ([NF] line 33), lambda is about 2.62 and sigma is
     about 6.36. This is my FLOAT arithmetic, not a certificate.
4. The prompt's "unique L2 solution" in R6.1 is not stated as such in P5.x. P5.2 (4) gives L0^(-1) on the completed
   Hdot^s realization, and P5.1 gives bijectivity on X_heat.

**Audit status.**
- P5.1 to P5.5 carry no status line in the headers read.
  - P5.2 line 2156 cites certificate file cutoff_constant.json for the Holder constant 81038.
  - [S1P] P2.1 line 640 is the model for informal-proof scope statements.
- Related items:
  - P22.1 ([S1P] header 8904, status line 8906), on optimality of the P5.1 constants: "Status: CONFIRMED check 98 by
    independent analytical derivation and proof audit."
  - P53.1 ([S1P] header 12791, status line 12793): "Status: complete analytical argument; independent review and
    elementary verification are pending."
  - P66.2 (header 14961, line 14963) and P67.2 (header 15104, line 15106): "Verified ... independent check 162" and
    "independent check 163".
- [OSF] line 122 says "OPEN pending independent T1/T2 review". [IDX] 141 records it as "AUDITED as part of the
  stronger T4-145 origin theorem". T4-145/146 became AUDITED at [VL] 1669 (T4-154, header 1664).

---

## R7. The IPM velocity cancels part of the angular loss ([P] 960-1054)

**Status.** No detailed source located.

**What was searched.** "kappa_ang", "kappa ang", "angular loss", "angular damping", "angular Fourier norm", "angular
frequency localization", "special source", "special-source", "velocity source", "velocity-source", "W_(s,lambda)",
"W_{s,lambda}". All returned nothing. "[a,U" and "a U_i" returned only Euler hits.

**Nearest items.**
- [S1P] 2224, quoted under R6: the velocity multiplier changes the frozen bounds "by at most one". No angular gain is
  claimed.
- [S1P] P5.4 2301-2311: the angular Fourier-supremum norm G_m.
- The prompt's m(xi) matches the source symbol (see Conventions).

**Differences / audit status.** Not applicable.

---

## R8. Good unknown and existing low-norm perturbation estimate ([P] 1058-1137)

**Status.**
- R8.1 and R8.2: located only as the special case l = 0 of the [L2] fixed-point step.
- R8.3: no detailed source located.

**Source and conclusion.**
- With l = 0, T(0) = -L^-1 F = h0 and 0 lies in B.
- [L2] 172 then reads A_k(T(k)-h0) = -U[k].D h0, which is R8.1.
- [L2] 176 gives ||T(k)-h0||_2 <= (c_s r/2)||k||_2, which is R8.2 with ||grad h0||_inf <= c_s r and beta_0 replaced by
  2.
- Hypotheses: as R5 (k in B; F in X_s with X_s(F) <= r/10).

**Differences from the prompt.**
- The source has no "good unknown" z_k and no separate statement of R8.1 or R8.2.
- The gradient bound comes from the X_s ball (h0 in B), not from an assumption grad h0 in L-infinity.

**R8.3: what was searched.** "weak expansion", "weak-direction", "weak direction", "principal-symbol" in an IPM
context. The only "weak-direction" and "weak direction" hits are case4 numerics. One example is
source/IPM/case4/IPM_case4.artifacts/outputs/g3/g3_v1/t4_interpretation_sidecar.md line 20, "## 2. The weak-direction
rows (E-T4.5w)", which is about singular vectors of a feasibility matrix.

**Audit status.** R8.1 and R8.2 come with T4-019 (AUDITED via T4-035). R8.3 has none.

---

## R9. Exterior weighted C^{1,alpha} lifting ([P] 1141-1290)

**Status.** No detailed source located.

**What was searched.** "mu_infty", "mu_inf", "sigma-1-alpha", "Neumann-series", "<X>^nu", "C^(1,alpha) inverse",
"1+alpha+delta". All returned nothing. I also read the headings of [A4] and of [S1P] after line 5700 for an exterior
weighted Holder lifting and found none.

**Nearest items.**
- [S1P] P13.1 (header 6359), "#### 2. Uniform outward characteristics" at 6382.
  - 6384: "The full velocity field B=cX+u+W is globally Lipschitz, hence has a complete flow X_t. Outside the unit
    disk, |u+W|<=C' r^gamma for some finite C'. Fix an initial point X_0=R e_theta and let delta=1-gamma."
  - It gives outward characteristics with r_t ~ R e^(ct). This is part of a non-existence statement for a decaying
    affine class, not a lifting estimate.
- [S1P] P68.1 (header 15116): "Logarithmic weights and asymptotic coordinates at the critical exponent", with
  line 15118: "Status: analytical proof, with no numerical inverse or profile existence claim." This is a far-field weighted
  space, not R9.
- [A4]: convergence of the stationary far-field series on exteriors ("Theorem A (PROVED; independently confirmed)",
  line 1092). This is a nonlinear exterior construction, not a lifting of the global L2 solution.
- [L2] 16: decay |D^j rho|=O(r^(gamma-j)). Matches the prompt's background envelope for grad rho once the sources'
  gamma = 1/c is used (see Conventions).

**Differences / audit status.** Not applicable.

---

## R10. Finite-annulus propagation ([P] 1294-1365)

**Status.** No detailed source located.

**What was searched.**
- "flow tube", "flow-tube" and "nested cutoff": nothing.
- "Phi_{-t}": Euler files only.
- "Phi_(-t)": [S1P] 1331-1332 only.
- "chi_t" and "chi_0": residual-cutoff proofs, not flow-adapted cutoffs.

**Nearest items.**
- [S1P] P4.2 (header 1271), line 1331: "<T_t h,phi>=exp(-(1+2c)t)<h,phi composed with Phi_(-t)>,". This is a transport
  semigroup duality for a negative-energy inverse, not a localization.
- source/c1_full/combined1_theory_agent_4/research/localized_low_audit/PROOF.md (title line 1, "# Audit of the localized low-energy
  estimate"). This is an L2 localized estimate.
- source/c1_full/combined1_theory_agent_4/research/annular_symmetric_coupling/PROOF.md line 3: "Status: new T4 result, OPEN pending
  independent Opus review." This is an L2 operator estimate on an exterior annulus.

**Differences / audit status.** Not applicable.

---

## R11. Local geometry and the remaining obstruction ([P] 1369-1441)

**Status.** No detailed source located. The search found none of: the weak-direction coordinate
Y = lim e^t Psi_{t,2}, the triangular form R11.1, the conjugated Riesz C^{1,alpha} estimate, or the angular-norm
counterexample after a coordinate change.

**What was searched.** "weak-direction", "weak direction", "triangular", "angular Fourier norm", "Psi_{t", "Psi_(t",
"Psi_t", plus the R8.3 terms.
- "triangular": numerics matrices only.
- "Psi_{t" and "Psi_(t": no hits.
- "Psi_t" (case-insensitive): 87 files.
  - Most hits are psi_theta in polar Jacobian formulas, for example
    source/c1_full/combined1_coordinator/artifacts/audit/theory_audit/research_code/angular_rule_audit/PROOF.md line 15.
  - The only flow-map uses are Euler files, for example
    source/Euler/approach3/Euler3.artifacts/docs/MATHEMATICAL_FORMULATION.md line 770.

**Nearest items.**
- source/IPM/combined1/combined1.artifacts/audit/theory_audit/research_code/frozen_adjoint_strip/PROOF.md:
  - line 17: "## Proof by straightening transport".
  - line 3: "Status: independent confirmation of the T2 theory worker the review of T4-145 Remark R1 for the natural
    frozen realization only. No transfer to a variable-coefficient adjoint domain is asserted."
  - [VL] header 1820, T4-171. This is a frozen strip-spectrum result.
- The "old angular Fourier norm" of [P] 1429 is most likely the angular Fourier-supremum norm of [S1P] P5.4
  (G_m, 2301-2311) or P5.3/P5.5 (F_k, 2197, 2402). This is my identification; the prompt names no file.

**Differences / audit status.** Not applicable.

---

## Candidate 007: certified signed rate and ||F||_2 (item 4)

- kappa_HS = 0.72816468018232542728.
  - [NVL] N4-092, header 975. Result line 980: "kappa_HS=0.72816468018232542728".
  - Verdict line 982: "OPEN pending independent peer reproduction".
  - Confirmed by [VL] T4-111, header 1195, line 1200: "Result and verdict: CONFIRMED. ... The complete Hilbert-Schmidt
    bound is kappa=0.72816468018232542728."
- theta <= 2/25 and the signed rate.
  - [NVL] N4-111, header 1171, claim line 1174: "theta=sup(sqrt(rho_x^2+rho_y^2)-rho_y)/2<=2/25, giving
    c+1-theta-kappa_HS>2.00215453001767."
  - Result line 1176: 223 cells, "signed rate2.00215453001767265836".
  - Verdict line 1178: OPEN pending peer.
- Theory confirmation: [VL] T4-162, header 1738, line 1743: "CONFIRMED. All232 closed cells pass ... signed low rate
  greater than2.00215453, hence (B-L2) with rate2. With T4-161's reviewed radial compression the available rate
  exceeds2.02568."
- Numerical acceptance: [NVL] N4-140, header 1463.
  - Line 1468: rate "[2.00215453001767265835874296227538627948196885619781716731168080867 +/- 2.93e-66]".
  - Line 1470: "Verdict: CONFIRMED."
- Compression: [VL] T4-161, header 1729, line 1734. The compressed commutator bound for 007 is
  "0.7046357876834905475325", and the theta allowance at rate 2 is "0.105683422516507538".
- Reports:
  - [CR] 205 and 831-837.
  - [CR] 2802: "kappa_007 < 0.728164680182325428", N4-268.
  - [TF] 757-758: "(C3) Values: 007 kappa_HS = 0.72816468018232542728 (N4-092 with T4-111, CONFIRMED) and (B-L2) holds
    for the exact 007" / "with rate > 2.00215 (N4-111, T4-162)."
  - [TF] 1567.
  - [IDX] 145.
- ||F||_2 = 0.3766893247.
  - [CR] 210: "||F||_2 = 0.3766893247 and G1 = 3.4391037868 alone (CONFIRMED by numerical audit 139 and numerical
    audit 153)".
  - [NVL] N4-139, header 1454, claim line 1457: "L2 norm 0.3766893247058942619446457668744382516530".
  - Verdict line 1461: "CONFIRMED as a complete whole-plane L2 norm."
- Other 007 hypotheses in the combined1 L2 framework ([TF] section 9.1, lines 1560-1572):
  - (A) decay, the boundedness list, (C) and (D) are "not checked" (1565, 1566, 1568, 1569).
  - The smallness condition fails ([TF] 1571).

---

## Searches with no hits

All searches below were case-insensitive fixed-string greps over every .md, .txt and .tex file under source/ (10816
files). Each returned 0 files:

"Tychonoff", "Tychonov", "16/(pi", "(4+alpha)", "4 + alpha", "kappa_ang", "kappa ang", "angular loss", "b(1+alpha)",
"flow tube", "flow-tube", "near-vertical", "near vertical", "mu_infty", "mu_inf", "good unknown", "K_{R,M}",
"K_(R,M)", "H_{sigma,alpha}", "H_(sigma,alpha)", "angular Fourier norm", "angular damping", "weak expansion",
"nested cutoff", "Neumann-series", "weakly compact", "weakly continuous", "C^(1,alpha) inverse", "1+alpha+delta",
"<X>^nu", "angular frequency localization", "W_(s,lambda)", "W_{s,lambda}", "special source", "special-source",
"velocity source", "velocity-source", "sigma-1-alpha", "Psi_{t", "Psi_(t".

Earlier in this reading, these patterns also returned nothing: "4+alpha", "q^(-kappa", "[a,U" (IPM files), and regex
forms of (1+alpha)(4+alpha).

Searches whose hits were all irrelevant:
- "Schauder": literature files and prompts only (Holder, analysis2 prompt, Euler references).
- "Tikhonov": numerical regularization and Euler.
- "first-moment" and "first moment": multipole and annular moments.
- "weak-direction" and "weak direction": case4 numerics.
- "Phi_{-t}": Euler.
- "Phi_(-t)": [S1P] 1331-1332 only.
- "2/sqrt(pi)": [S1P] 17368, 17438, 17577, all product estimates.
- "triangular": numerics matrices.
- "chi_t" and "chi_0": residual cutoffs.
- "commutator gains": Chen-Hou Euler references.
- "a U_i": Euler.
- "Psi_t" (case-insensitive): psi_theta in polar formulas, and Euler flow maps.

## Targeted audit notes (version 3)

Scope. This section records the audit notes on uses of R1 to R11 that were filed after version 2, in four sources:
theory_audit/AUDIT_LEDGER.md, exchange/theory_requirements/theory_v14.md, the coordinator team notes with
WORKSPACE_CONTRACTS.md, and theory_agent_2/notes/T2_O2O3_FINAL_v02.md. A read-only search pass swept the four sources (finished
about 2026-11-03T21:41Z; its notes are research/epr_v3/sweep_part2_audit_notes.md in the first theory agent agent, with paths
relative to that file). The first theory agent then re-read, from 21:57Z to 22:00Z, the claim and verdict lines of the 32 AT entries
cited below by number, checked that their 28 proof files and the cited audit directory exist, and re-read the quoted
lines of theory_v14, WORKSPACE_CONTRACTS.md and T2_O2O3_FINAL_v02. The notes line numbers in the sweep had moved because the
coordinator adds new notes at the top; notes items are therefore cited by section heading.

Finding. No entry asserts an error inside any of R1 to R11. Every note is one of four kinds: a scope restriction on a
new use, a missing premise of a new use, a convention or constant correction in a new statement, or a confirmation of
a use in qualified form. Every REFUTED verdict below is aimed at a new claim, not at an imported result. Four entries
say so explicitly: AT-007 ("The original full-Hölder R5 statement remains IMPORTED and unaffected"), AT-021 ("No
imported theorem is refuted"), AT-032 ("No imported R9 result is refuted") and AT-041 ("No imported reference
inconsistency is asserted"). Sections 0 to R11 and the summary table above are unchanged, and nothing here is
re-proved. The governing rule is WORKSPACE_CONTRACTS.md lines 33 to 36: "A use outside the stated hypotheses is not IMPORTED: it is
a new claim."

Proof files cited as "research/NAME" are theory_audit/research/NAME/PROOF.md.

### R1 and R2 (L^2 generator, energy identity, inverse)

- AT-029 (CONFIRMED, conditional): Lemma WG uses the R1 Hilbert-Schmidt identity as a premise together with BG-reg and
  global BG-q. research/weighted_garding_audit.
- AT-030 (CONFIRMED with the stated hypotheses): identifying the weighted H^q semigroup with the R2 L^2 semigroup
  inherits R2's closed-generator, Schwartz-domain and generation hypotheses. research/weighted_semigroup_audit.
- AT-103 (CONFIRMED, counterexample): a small normalized real S1 C^1 coefficient need not have a Lipschitz velocity.
  The Lipschitz premise on U[k] used with R2 (and supplied in R5 by R4.3) is therefore not implied by C^1 smallness; a
  positive Hölder exponent suffices but is not the only repair. research/coefficient_c1_counterexample.
- AT-123 and AT-142 (corrected forms CONFIRMED; the three-derivative-to-all-order inference of AT-123 and three
  incomplete attributions of AT-142 REFUTED): at a re-centered background rho_* = rho_bar + h_*, the R1/R2 hypotheses
  must be retained for each h_* + k, uniformly. research/recenter_framework_audit, research/theory_v02_scope.
- theory_v14 lines 8349 and 8377 to 8380 (RC-1, RC-3): R1 and R2 must hold at rho_* for each h_* + k, and R5 is
  applied with background rho_*.
- T2_O2O3_FINAL_v02 lines 57 to 58: the L^2 inverse bound ||A_k^(-1) G||_2 <= ||G||_2/beta_0 is used only "whenever
  R1.2 and R2 apply to V + U[k]".
- notes section "2026-11-02T18:18Z: where Part II has detailed sources": R1 to R3 are proved in [L2] inside the
  Sobolev framework k in X_s under hypotheses (A) to (D); this agrees with section 0 items 1 to 4 above.

### R3 (normalization)

- AT-036 (CONFIRMED with qualifications): Theorem D-S inherits every R3 normalization hypothesis, including the
  normalized background and a0 > 0; F = 0 is handled separately. research/sobolev_closure_audit.
- AT-042, AT-061, AT-066 and AT-114 (CONFIRMED, conditional): each keeps every R3 premise (with R1, R2 and R5 where
  used). research/radial_decomposition_audit, research/sobolev_necessary_test_audit,
  research/pointwise_inverse_closure, research/sharp_full_garding.
- theory_v14 line 8265 (AN-044, CONFIRMED): (F_*)_y(0) = (a_0 + h_y(0)) ell(h), so an unnormalized center breaks
  F_y(0) = 0 and R3 does not apply to it as stated.
- T2_O2O3_FINAL_v02 lines 59 to 60: R3 is used with a normalized background, a0 > 0 and F real S1 with F_y(0) = 0.

### R4 (interpolation and velocity constants)

- AT-018 (CONFIRMED independently): C_I is the scalar optimizer of R4.1. The constant proved for ||Df||_inf does not
  by itself give a weighted-gradient bound; the bound ||w_sigma Df||_inf <= max{1, sigma/2} H(f) is the one to use.
  research/tame_weight_constants_audit.
- AT-024 (OPEN under an implicit Frobenius convention; both transfers CONFIRMED), resolved for v02 by AT-040
  (CONFIRMED): the R4.3-based constant C_eps = C_I C_U^(1-theta) holds in operator norm. Under a Frobenius convention
  a sufficient constant is 2^((1-theta)/2) C_I C_U^(1-theta). AT-040 makes the operator norm explicit.
  research/velocity_norm_transfer, research/hoelder_revision2_audit.

### R5 (weak fixed point, K_{R,M}, R5.4)

- AT-006 (identification REFUTED; contract topology OPEN), AT-007 (REFUTED for the replacement only) and AT-008
  (CONFIRMED): replacing R5's full weighted C^(1,alpha) space by the Hölder-norm closure of smooth compactly supported
  S1 functions gives a strictly smaller space whose normalized balls need not be weakly closed in L^2 (counterexample
  chi(X) y|y|^alpha). Amendment v02 A2.2 restores the full space, now WORKSPACE_CONTRACTS.md lines 262 to 265. The original R5
  statement is unaffected. research/function_space_contract, research/normalized_function_space_contract,
  theory_audit/audit/contracts_amendment_v02.
- AT-037 (CONFIRMED, conditional on invariance and the retained R1/R2/R3/R5 assumptions): the Hilbert-ball form is the
  new Proposition R5-S, with L_K = C_GN R^theta (c_W M)^(1-theta)/beta0; R5 itself is imported, not redone.
  research/sobolev_ball_audit. T2_O2O3_FINAL_v02 line 61 cites it the same way.
- AT-040 (CONFIRMED): the R5.4 uniqueness factor as used in the v02 revision is correct.
  research/hoelder_revision2_audit.
- notes section "2026-11-02T19:13Z: addendum to 19:12Z item 3": only the Schauder-Tychonoff mechanism, the L^2
  Lipschitz bound R5.4 and the trace continuity of ell are IMPORTED from R5; the weak compactness and weak continuity
  statements of the H^q ball "are new results, not R5".

### R6 (frozen-origin estimates)

- AT-002 (CONFIRMED for the parameter inequalities only): (alpha, delta_s, sigma) = (1/2, 2/5, 7/4) satisfies the
  strict exponent conditions of R6, R7 and the pure-dilation limit of R9. The origin condition stays a separate input.
  research/parameter_contract.
- AT-004 (CONFIRMED, dependency AN-001): for Candidate 007 the R6.3 damping inequality holds for every 0 < alpha < 1,
  and ||<X>^sigma F||_{C^s} < infinity exactly when sigma <= 5 - 4/c_l. research/strong_norm_membership_audit.
- AT-009 (classification CONFIRMED; R6.4 eligibility of three rows REFUTED): the rows (alpha, delta) = (3/4, 2/5)
  violate delta > alpha/(2c - 2) at all three weights. For sigma = 9/4 a separate nu < 2 and the weight-multiplier
  constant are needed. research/parameter_grid. notes section "2026-11-02T18:29Z: S_F grid correction (AT-009)"
  records that those rows "cannot feed R6.4".
- AT-016 (CONFIRMED): weight conversion goes only from a heavier to a lighter weight (sigma >= nu); the reverse fails.
  R6.4 still requires its source gap, delta < 1 and 1 < nu < 2. research/weight_conversion.
- AT-021 (REFUTED, new heuristic coefficient only) and AT-044 (CONFIRMED for the repaired interval): the vertical
  Fourier-axis coefficient. research/frozen_coefficient_audit, research/frozen_axis_revision_audit.
- AT-087 (identities CONFIRMED; inferences REFUTED): the sigma = 1 source tuple does not meet the strict R6.4
  requirement nu > 1 when nu = sigma. research/numerics_exchange_v01_theory_audit. theory_v14 lines 2537 to 2539
  restate it: sigma = 1 is valid in the Sobolev route but cannot be inserted as nu = 1 in the frozen theorem.
- AT-116 and AT-117 (CONFIRMED): no frozen estimate family keeps both coefficients bounded as alpha + delta tends to
  0; R6 is composed only under its strict assumptions, with the corrected plus sign and unweighted C^(1,alpha) output.
  research/joint_loss_limit, research/frozen_compact_leading.
- Retention notes (CONFIRMED): AT-050, AT-056, AT-089 and the later integration audits keep delta > alpha/(2c - 2),
  delta < 1, 1 < nu < 2 and the noninteger restriction. theory_v14 line 9777: "A frozen-origin estimate is never a
  full inverse."

### R9 (exterior estimates)

- AT-032 (OPEN as written; CONFIRMED once corrected): Corollary O1-R9 needs an explicit bound
  ||<X>^sigma9 F||_{C^(1,alpha)(|X|>R)} < infinity and every finite-radius R9 hypothesis, including mu_R > 0 and its
  absorption. research/o1_corollary_scope.
- AT-087: the asymptotic coefficients are not valid finite-radius constants C9, C9'.
- theory_v14 line 2533: T1.3 needs every R9.4 hypothesis at sigma_9 for the 013 background; mu_R has a FLOAT screen
  only, and only for Candidate 007.
- AT-094 (qualified CONFIRMED; necessity claims REFUTED): the BG-L4 mu_R perturbation does not replace R9's
  regularity, envelope and nonlocal-smallness assumptions. research/lk_scoping_audit.

### R10 and R11

- AT-041 (OPEN for that inference): R10's unspecified dependence on Lambda gives no polynomial growth bound for H1(p).
  research/hoelder_variant_audit.
- theory_v14 line 7353: the strong LK route needs the joint stationary origin estimate of R11, which is OPEN.

### R7 and R8

No new audit note. notes section "2026-11-02T18:18Z" records that R7, R8.3 and the R6.2 to R6.4 forms were not located
and that R8.1 appears only as a proof step ([L2] 170 to 176); this agrees with the R7 and R8 entries above.

## Part VII freeze (version 4; corrected at version 5)

Freeze. This section states the use of R1 to R11 at the cutoff of THEORY_NEW_RESULTS version 24 (the first theory agent agent; its
section S.7 is the dependency table), extended to the theory audit exchange audit_v815 (AT2698, published
2026-11-04T11:52:44Z). Later work is pending and is not counted here. Sections 0 to R11, the summary table, the
Candidate 007 section, the searches with no hits and the version 3 notes above are unchanged, and nothing is
re-proved.

Sweep. On 2026-11-04 from 11:54Z to 11:56Z the first theory agent searched, read-only with grep, the records filed after the version 3
sweep: the theory audit exchange files audit_v484 to audit_v815 (published 2026-11-03T21:43:29Z to 2026-11-04T11:52:44Z), the
coordinator's notes from 2026-11-03T22:03Z to 2026-11-04T11:38Z and the second theory agent's notes/T2_PART7_v09.md, for the names R1
to R11 with their numbered subitems, "Part II" and "IMPORTED". The coordinator's labels R1 to R5 in its
2026-11-03T22:20Z correction note are item labels, not references (the date is corrected at version 5, AT2734; its
22:03Z note uses the labels C1 to C5). Only one entry names an imported reference: AT2423 (audit_v741, CONFIRMED;
the theory auditor research/t2_closure_program_v03_audit) checks that the second theory agent's closure program version 3 keeps the strict
restrictions of its regularity branch H-REG, namely every R9.4 premise, or R6.4 with alpha/(2c - 2) < delta < 1 and
1 < nu < 2; the printed delta > 0.0617041 at alpha = 1/10 is a sufficient rounded condition, and the low cut nu =
1/40 of the H4-REST pieces is a different parameter from the lifting exponent nu. This is a retention note of the
kind recorded under R6 above (AT-050, AT-056, AT-089). No record of the sweep asserts an error inside R1 to R11.

Notation. In the near check, the closure checks and their audits after version 3, "(R1)" to "(R4)" are the four
requirements of the mu 72 window in theory_v14 V14-4 (b) 4: (R1) certified whole-plane uppers of D4, D5 and D6 of
a_n, (R2) the kernel uppers at mu 72, (R3) the K0 tails of a_c, (R4) the sups, ||a_+||_1 and the other HF1-NEAR
inputs. "Proposition R4", "R4 version 1" and "R4 version 2" (the second theory agent's T2_NEAR_R4 notes; AT2477 to AT2479, AT2520 to
AT2522) are the second theory agent's certified uppers of the (R4) inputs. None of these is R1 or R4 of Part II; Part II's R4 (L2 to
C^{1,alpha} interpolation) is used by no result of THEORY_NEW_RESULTS (its S.7).

Uses at the freeze. THEORY_NEW_RESULTS version 24, section S.7, lists every use of R1 to R11 by its results. The
conditional k = 0 application at 013 (its NR-31; AT2541, AT2599) uses R1 and R2 only through the framework
FW-C2-O1Hq-v1 (its NR-1, with the steps in NR-2): the base L2 gap beta_0 > 2.00215453 of BG-2 (the signed rate of the
Candidate 007 section above) and the L2 semigroup of Lemma SG; the perturbation by grad h_* and the bound 1/(beta_0 -
G) are new steps of NR-31, not imported. NR-32 to NR-34 use no Part II reference; NR-33 and NR-34 use Lemmas HI' and
MOM, the KER identity and Proposition FG, which are results of other agents with their own audit entries. Any return
to the prompt's Hoelder lifting route keeps the R6.4 and R9.4 hypotheses stated above (AT2423; the theory auditor's unfrozen final
theory audit draft states the same restriction).

Completed: 2026-11-04T12:14:41Z.
