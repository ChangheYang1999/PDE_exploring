# Audit of the report assembled at 16:11 UTC

## 1. Version, reading scope and dependencies

The retained snapshot is in the team records, pinned at2026-11-03T16:12:28.897113+00:00:6114lines,788725bytes, SHA256 8e64e2e3ddfc4f66ce5cbb3324c6d3e2f5d613a4c1a764ed886d1c688e7ff006. It states assembly16:11 and verdicts throughA1608. All19changed chunks in the207line diff against the earlier1553audit snapshot were read. The full current Theorem8, its outline, the first87lines including the summary and assumptions, and the full changed vorticity paragraph were separately read. This is a version-difference audit, not a claim to have reread every unchanged line of this6114line artifact.

The earlier audit chain remains in the team records. Recent mathematical dependencies were independently proved and read in the smallness, normalized-form, coupled-system, global-pressure and work-crossing topic folders. The source CO62 zero-rotation conductivity proof was reread in full for the current scope check.

## 2. Repairs and new theorem statements that pass

The bare-decay statements now correctly say the extra smallness and integrability conditions are not known to follow from decay. The compact-core argument correctly uses bounded vorticity on a compact set, automatic under C1 regularity. The LIT244 row now excludes a nonzero flat germ. CO61 now limits its power law to one vortical component and says two distinct real characteristic lines in the strict hyperbolic region, while recording degenerate null directions at equality. CO62(c) now has omega=0; at this scope its scalar conductivity h^eta in conformal sphere coordinates is exact. The geometric-factor qualification concerns the nonzero-rotation p=2 exception, not this corrected zero-rotation case.

The explicit Theorem8 hypotheses pass, including its added nonlinear smallness criterion

    sup |curl U|^2<=tstar=(15sqrt(7)-20)/42

for0<c<=1/2. The proof is A1584-A1586. The old linear criterion remains strict unless its separately stated strict far-field condition holds. The strain statements retain bounded W in the introductory clause of part(a), with bounded S for their forms. The section3 table has restored bounded curl U; write this as a common premise followed by 'one of the following' to remove any ambiguity in the sequence of 'and' and 'or'.

The decimal0.68463 is a safe rounded-down sufficient bound. It is not exactly sqrt(tstar); replace the displayed equality by an approximation sign or 'about'. The combined-threshold sentence should retain the distinction between a weak inequality at sqrt(tstar) and a strict one at the larger linear threshold, unless the latter's separate far-field premise is also supplied. No new endpoint claim is certified merely by writing a maximum of two constants.

The added LIT244-LIT248, CO61-CO62, C52-C53 and Besov-scope rows otherwise reflect their confirmed local, global, regularity and additional-equation hypotheses. The C52 converse is more precisely 'such a forward-invariant set has nonpositive work under the stated hypotheses'; it does not construct a neighborhood at a common-flat orbit. The row itself keeps that existence question OPEN.

## 3. Incorrect pressure in the resonant counterexample

The LIT249 table row prints

    V=|x|^(-3/2)Jx,
    P=-(1+omega^2/2)/|x|.

Here omega is the rotation parameter defined by the report. This pair does not satisfy the Poisson equation. Its printed pressure is a constant multiple of1/r and is harmonic away from0. Direct differentiation of V gives

    tr((DV)^2)=r^(-3)(1-3mu^2), mu=x3/r,

which is not identically zero. This refutes the row's claim that the printed pair satisfies every kinematic and Poisson hypothesis, for every rotation value.

The already confirmed counterexample A1607 instead uses

    mu=x3/|x|,
    P=-(1+mu^2/2)/|x|.

Since Delta_S(mu^2)=2-6mu^2, its negative Laplacian is exactly the displayed trace. Its full momentum residual remains(3/2)x3^2x/r^5, so it is not a full similarity profile. Replace omega by mu and define mu in the row. The intended exponent counterexample and the global pressure theorem remain valid.

## 4. A changed referent in the vorticity paragraph

The paragraph now lists three alternatives in order: linear global vorticity smallness, nonlinear global vorticity smallness, and finite critical weighted enstrophy. Its next sentence still says 'The second condition sits just beyond the far field' and then discusses divergence of the weighted integral for a homogeneous tail. That explanation belongs to the third, weighted-enstrophy condition. Replace 'The second condition' by 'The weighted-enstrophy condition' and 'either condition' by 'any of these conditions'. No theorem changes.

## 5. Recent additions versus the snapshot cutoff

The LIT249 row already states continuous pressure but citesA1602-A1606, whose source version assumed C2 pressure. The continuous-pressure statement is now independently confirmed byA1622-A1624, after this snapshot's cutoff. Update the citations to those verdicts rather than treating the old audit as covering an unread revision. Its extended c range(2/5,1), c!=2/3 is the exact conversion of0<p<3/2,p!=1/2.

The snapshot correctly leaves LIT250 and CO63 SUBMITTED at its stated cutoff. They have since been confirmed byA1609 andA1614-A1617; A1610-A1612 provide a separate all-rotation tensor proof. Their pressure sign and uniform neighborhood premises remain essential. The exact stress-only endpoint models A1618-A1620 are not divergence-free and must not be promoted to Euler counterexamples.

Corollary NW.2's step table remains unaudited at this report check. Its numerical or symbolic success label is not used to prove Theorem8. The ODE optimization remains OPEN. These distinctions are correctly retained in the snapshot.

## 6. Verdict boundary

The report's explicit main-conjecture verdict remains UNRESOLVED, with the additional helicity sign, regularity, vorticity size and tail conditions visible. The confirmed repairs and theorem statements are approved only at the scopes in Section2. The printed resonant pressure and changed paragraph referent require repair. Whole-report final approval remains OPEN, both because of those errors and because new material continues to arrive.

No computation or formal build was used. Evidence is the pinned complete snapshot, full change diff and independent analytic dependencies. Comparison and corrections go through existing configured model working files; provider runtime remains unattested.
