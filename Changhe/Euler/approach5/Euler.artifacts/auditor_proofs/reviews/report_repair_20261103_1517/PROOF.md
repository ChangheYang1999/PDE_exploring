# Report repair audit at the 15:16 snapshot

## 1. Exact object and scope

This audit concerns the immutable report in the team records, SHA256 d375a9681355a07f91d507e61d84b0d6cb9048892d61756d95bdd43733ca34be, captured at 2026-11-03T15:16:53.570626Z. It has 748806 bytes and 5986 lines. The comparison is the complete earlier snapshot in the team records. Every one of the 22 change groups, serialized in fourteen bounded chunks, was read in full. Outputs that were truncated were reread separately. This is a complete change audit on top of the previous full proof-body and appendix audits, not a claim to have freshly reread all 5986 lines during this check.

The mathematical class remains the one attached to each individual theorem. In particular the new tail statements generally concern globally helicity-free C2 profiles with the natural bounds, not every decaying profile. The unrestricted target for 2/5<c<1/2 and every finite omega remains open.

## 2. All five requested repairs are present

A1363: line4283 now distinguishes V=0 for pure swirl or open k=0 from the conclusion that only the swirl component F vanishes under the zero-helicity hypotheses of LIT226. Full polar-cap vanishing cites LIT229 and retains the rank relation and V=W=0 at the pole.

A1364: line4294 supplies the missing antecedent for the transverse rank-one alternative: a supported zero of W with k>0, or with k=0 and S<0. It does not classify arbitrary vorticity zeros.

A1365: the assertion that none of the tail criteria implies another has been removed. The report explicitly states that Theorem7(e) implies7(f). This follows because the finite-order premise at every point leaves no point where the additional scalar-order requirement of7(f) has to be tested.

A1366: lines4064-4065 preserve connectedness and the alternative V identically zero in the constant-S statement. Otherwise the zeros are simple and have projected index+1.

A1367: line4775 uses the jets of H-Pinf, including the value jet. The adjacent critical-leaf sentence at4771 has the same corrected normalization. Derivatives of positive order do not change with the gauge; order zero does.

These repairs are confirmed. The previous body and appendix repairs remain present in the changed text.

## 3. An incorrect equality at common flat points

The current C50 account inside line4777 says: "p1 >= 0 on T0, with p1 = 0 where DW != 0, in particular at every common flat point". The last clause does not follow and reverses the relevant distinction.

In the exact class and with c!=3/7, the audited orbit formulas are, writing a=1-2c and sigma1=p1-2V.grad P2,

    exp((a+2)t) Q(y_t) -> sigma1,
    exp((a+2)t) H(y_t) -> -(a/2)sigma1,
    exp((a+2)t) g(y_t) -> -((a+2)/2)sigma1.

At T0, V=0, hence sigma1=p1. Nonpositive work on the orbit gives p1>=0. The stronger condition that X lies in the range of DW makes g identically zero and gives p1=0. At T0 a nonzero DW has that range. At a smooth infinitely flat zero of V, however, D2V=0, hence DW=0. The equality argument therefore does not apply there. Indeed the orbit signs are consistent with p1>0, in which case H and g are strictly negative for sufficiently large t. This is a compatibility check, not an existence example.

Replace the quoted clause by: "p1 >= 0 on T0, including every common flat point; equality holds wherever DW != 0, and also on an orbit with identically zero work." The attribution of equality at all common flat points to A1415 is refuted. Whether the full equations imply that extra equality by a different argument is open.

## 4. The zero-field alternative in local classifications

Lines304-305 and4056-4058 describe fixed-direction or axially invariant tails as having no velocity zero. The literal statement needs the nontriviality qualifier. LIT233-LIT235 prove the dichotomy: on the stated connected local domain, V is identically zero or nowhere zero. The smooth pair V=0, P2=0 satisfies every local identity and has zeros everywhere. It directly refutes deletion of the zero alternative.

This does not affect exclusion of a supported vorticity zero, since V identically zero on the connected neighborhood has no such supported point there. For precise summaries insert "nontrivial" or retain the full dichotomy. The detailed rows4289-4291 already do so. The historical ledger lines5859-5860 should use the same qualifier if edited.

## 5. A missing hypothesis in the C50 summary row

At line4295, the phrase "sigma1 < 0 forces V != 0 and rank-one DW transverse to X" omits its local hypothesis. A1416 proves this at a supported zero of W with k=S=0. Its proof uses the derivative classification and the work-sign law at that vorticity zero. The start of the row assumes only k=S=0. That is insufficient to invoke those inputs. Insert "at a supported zero of W with k=S=0" before the sign condition. The longer paragraph at4777 already has this condition. The broad attribution to A1416 is refuted; no counterexample to the full profile equation is asserted.

## 6. Other changed statements and pending additions

The derivative-growth gap retains bounded exterior vorticity, the velocity exponent and the strict growth threshold. The R2 estimates are labeled limits of one method, with the sufficient coefficient unchanged. The SRB-preprint implication is explicitly conditional. The first-integral row has the corrected c range. The pressure gauge, vector rotation generator and ambient-ball quantifiers are retained. Theorem7(f), its all-points premise and its relation to7(e) remain accurate.

CO57 and CO58 are marked SUBMITTED in this snapshot and have not been promoted to proved statements. The newer LIT236-LIT238 conclusions were completed after this report revision and are not yet incorporated. The old CO56 open interval should be updated when those results are added: a positive bounded W1,2 transverse ratio is now excluded at an isolated flat orbit with one strict scalar sign, while unrestricted ratios and extra scalar zeros remain open.

## 7. Verdict and dependencies

The five repairs A1363-A1367 are confirmed. Three further wording/scope corrections in Sections3-5 are required. Whole-report approval remains open until the current text is repaired and checked. The underlying confirmed results are not withdrawn. No statement here proves the bare-decay conjecture.

Dependencies are the complete independent proofs in the team records, in the team records, in the team records, in the team records, in the team records, in the team records and in the team records. No computation or external model request was made for this audit.
