# Exact hypotheses in the report summaries

Status: independent scope audit. The unqualified summary formulations below are OPEN pending repair. The previously confirmed underlying results are unchanged.

## 1. Setting and exact audited statements

Let 0<c<1/2, omega in R, U in C2(R3;R3), and P in C1 solve the full rotating incompressible Euler profile equation. Assume U=o(|y|) uniformly and U.curl U=0 everywhere. Set A=cI-omega J, B=Ay+U, W=curl U, a=1-2c, O={W!=0}, alpha=B cross W, H=P+|U|^2/2+(Ay).U and g=U.B. The carrier is complete because it has at most linear growth.

A470 proves g<=0 on a compact whole-flow-invariant set S contained in closure(O) intersect {W=0,Dalpha=0}. It proves g=0 if S is the support of an invariant probability. These conclusions have different hypotheses. For a compact ergodic invariant probability with mu(B=0)=0 and S=supp(mu) contained in closure(O) intersect {W=0,Dalpha=0}, A471 supplies a finite constant covector rate rho, backward spectrum (0,-rho,rho-3c), including the repeated zero case rho=0, and top exponent zero whenever the measure is aperiodic. Its periodic alternative is not excluded.

Both complete proofs are in the team records and in the team records. This audit checks faithful use of those theorems, rather than claiming an additional extension of them.

## 2. Why the vortical-closure hypothesis is used

A413 gives the C1 tensor dH wedge dg=0 on the open set O. Every first derivative of this tensor vanishes on O and, by continuity, on closure(O). At an irrotational point of closure(O) with Dalpha=0 and U!=0, the Lamb identity gives grad H=-aU and Hess H=-a DU. The value of the rank tensor gives grad g=rho U. Its ambient derivative gives

    Hess g-rho DU=tau U tensor U.

These are the two identities used to derive convexity of log g on a positive-work orbit and the covector cocycle on a zero-work support. Continuity provides neither identity in an open irrotational region disjoint from closure(O). Flatness DW=0 by itself does not give that closure membership.

For the nonflat ergodic case, DW!=0 almost everywhere at points where W=0 does imply membership in closure(O): if W vanished on a neighborhood then its derivative would be zero at the point. The closed set closure(O) then contains the entire support, by the definition of support and continuity. This reasoning does not apply to the flat alternative DW=0. Thus the phrase "a flat probability" following the nonflat classification must explicitly reintroduce supp(mu) subset closure(O), or restrict the discussion to probabilities on a component core K_E where this is automatic.

Section 1c presently omits this qualification. The same omission occurs in the flat-probability sentence of the summary ledger, the discussion preceding the componentwise criterion, and item 8. The resulting stronger assertions are not established by A470 or A471. No counterexample to that stronger global assertion is claimed here; its status is OPEN.

## 3. Why the two-witness reduction is unaffected

For a connected component E of O, put K_E=K intersect closure(E) and Z_E=K_E intersect ({B=0} union {W=0}), where K is the absorbing core. A probability on Z_E has support in closure(O). A470 and A471 therefore apply to its flat nonstationary alternative at their exact hypotheses. A467 bounds the nonflat nonstationary alternative by a/2. If an attained top exponent is at least2a, only a carrier-equilibrium atom or a flat periodic probability can witness it. The latter spectrum has top exponent max(0,-rho,rho-3c), which is at least2a precisely if rho<=-2a or rho>=3c+2a=2-c. This is the audited A471 reduction. Neither witness type has been excluded.

The hour-16 packet instead says zero work on compact invariant sets with W=Dalpha=0. It must retain closure(O) and distinguish g<=0 on such sets from g=0 on invariant probability supports. Invariance alone only gives the inequality by A470. Integration of BH=-ag against an invariant probability gives integral g=0, and nonpositivity and full support then give pointwise equality. That integration step requires the probability and cannot be applied to an arbitrary compact invariant set.

## 4. The nonzero-vorticity and attainment qualifications

The global identity Lambda_core=max(a,Gamma_Z) of A399 assumes W is not identically zero. The profile U=0, P constant, is an exact smooth decaying solution for every omega. Its backward carrier derivative is exp(-ct) times an orthogonal rotation. Hence max(1,sup_Q|D Psi_n|)=1 and Lambda_core=0. The only compact invariant ergodic probability for this linear carrier is the origin atom, whose top exponent is -c, so Gamma_Z=-c and max(a,Gamma_Z)=a>0. This gives an exact counterexample to the identity and lower bound without the nonzero-vorticity hypothesis.

The revised Section 2C and Section 2D already impose this qualification. Opening summary line 75, the global-coverage ledger row, ASSUMPTIONS rows for A398-A399, THEOREM_ATTEMPTS T27, and item 8 must preserve it as well. Coverage for W identically zero is vacuous, so the conditional coverage result is not harmed.

Gamma_E, and likewise Gamma_Z, is an attained maximum only when its set of degenerate invariant probabilities is nonempty. With the specified convention its value is minus infinity when the underlying compact invariant zero set is empty. The opening componentwise sentence should say this explicitly, as the repaired Section 2C does. No maximum-attainment claim is made over an empty family.

## 5. Verdict and verification

The independent summary audit finds missing hypotheses, not a new gap in A470, A471, A398-A399 or A430-A432. The exact componentwise two-witness reduction is intact. Unrestricted C2 coverage, arbitrary-sign nonexistence and both witness exclusions remain OPEN. Corrected text must be compared with these hypotheses before receiving a final summary verdict.

The source opening and complete hour-16 packet are pinned with timestamps and SHA256 digests in verification. The full A470 and A471 hypotheses and their rank and integration steps were read again for this audit. No computation is required. The configured-model coordinator is asked through the existing file exchange to repair or challenge these exact omissions; no new remote model call or other person is contacted.

## 6. Follow-up on the repaired summaries, 2026-11-03T05:49:37.814909+00:00

The opening summary, the hour-16 packet, the global-growth qualifications in T31 and O7(v), and the A430 assumptions row now contain the requested hypotheses. Their mathematical statements agree with Sections1-4. Three residual flat-spectrum summaries still need the exact premise stated explicitly:

- the report table A, the long nonflat-irrotational-measures row, introduces a new flat probability and gives its constant rate and spectrum. It has the vortical-closure premise but omits compact full-flow ergodicity and B nonzero almost everywhere. The antecedent nonflat probability does not supply these after a new probability is introduced.
- THEOREM_ATTEMPTS T32, the paragraph beginning Flat stratum, says compact ergodic flat probability in this class. The class is the global helicity-free class. It must additionally say support contained in closure of the vortical set and B nonzero almost everywhere, or restrict explicitly to the nonstationary probabilities on Z_E.
- PROOF_OBSTRUCTIONS O7(vi), the paragraph beginning On the flat stratum, needs the same explicit restriction before giving the covector rate and spectrum.

These are still faithful-statement issues, not gaps in the underlying A470-A471 proofs or the two-witness reduction. A494 leaves the complete summary certification OPEN until these small remaining repairs are read. The repaired individual statements listed above are confirmed at their existing scopes. Snapshots and source hashes are in the team records.

## 7. Final three qualifications present, 2026-11-03T05:56:50.837496+00:00

The actual updated table A nonflat-measures row, T32 flat-stratum paragraph and O7(vi) paragraph were reread. All now explicitly say compact ergodic flat probability, B nonzero almost everywhere and support contained in closure of the vortical set. They therefore invoke A470-A471 within their exact hypotheses. This closes A494's three specific repair requests. It is a certification of those formulations together with the previously checked A484 repairs, not an endorsement of every later addition to the evolving report. A496 now independently excludes the upper vortical-equilibrium range, which these historical sections had left open; that new result must be propagated separately. The main arbitrary-sign conjecture and unconditional C2 coverage remain OPEN.
