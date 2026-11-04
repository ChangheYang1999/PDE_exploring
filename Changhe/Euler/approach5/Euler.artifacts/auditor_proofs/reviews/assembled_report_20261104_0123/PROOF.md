# Audit of report2eab7ba5 and its pressure-example scope

## 1. Exact assembly and comparison

The candidate SHA256 is 2eab7ba57b22f4f91b881677b278e8218402c67da3698bffaf7b45100342211d, with 1035336 bytes. Its front matter gives assembly time 2026-11-04T01:18Z and cutoff A2720. The coordinator announced the pin in Note171 at 01:19Z. The baseline is report5639599f290387dd7b178922e334342ef188a6abb34d1dd2009890a8ca2a46c9, approved in A2717 at cutoff A2691.

All fifteen independently generated contextual delta blocks were read in full, including the entire new pressure row and the surrounding long rows. The change files and snapshot hashes are in verification. There are 7009 newline-terminated lines, or 7010 entries if the terminal empty string after the final newline is counted. The latter is the coordinator's build convention; this is not a content discrepancy.

The static check finds nine actual Markdown tables with 597 rows including headers and separators, with no column-count mismatch, absolute local path or em dash. No browser, renderer or mathematical computation was used. This is not a rendered-page check.

## 2. D4-D6 precision changes

Blocks3-12 implement the already confirmed A2711-A2713 findings. D4(i) gives the disk radius and separates its center from its normal. D4(ii) consistently writes the scalar exponent1-2c, chooses S as a graph over the transverse coordinate of its corresponding larger box, and explicitly uses its own smaller box at time zero. Thus the backward plaque induction ends with two points of S on the same plaque of that larger box. Their equality now follows from the stated graph choice, exactly as reconstructed in the earlier independent audit.

The local neighborhood names N_G, W_y, N_A and V_N are consistently distinguished from the equilibrium set N; the local entrance ball D_p is distinguished from the trapping ball D. The parenthesis after CorollaryD5.12 now distinguishes the cited half-line escape fact from the immediately proved LemmaD5.13. TheoremD6 explicitly allows a nonhyperbolic saddle when lambda2=0.

The entrance lemma now defines K as the actual omega-limit of the stated precompact orbit. Its proof has last-entry times s_n tending to infinity and residence times t_n-s_n tending to infinity, so the boundary limit lies in this same K and its entire positive orbit stays in the local ball. The stable-manifold contradiction is therefore at precisely the scope of A2712. No new assumption is added in the application.

The Bowen-Ruelle and Ledrappier-Young remarks now state the compactified ambient setting. This is the already checked scope clarification, not a new certification of those external theorems. Block13 accurately summarizes these changes without claiming a fresh whole-D0-D6 audit. Blocks1-2 and15 correctly update the cutoff, cite the earlier A2717 assembly approval and record the verdict history. A2714 and A2715 are identified as source-only changes outside this report.

## 3. Pressure row: statements (a)-(d)

The new row first states the common full-ball divergence, Poisson and center-normalization hypotheses. Part(a) keeps C2 velocity and C1 pressure, the pointwise whole-ball inequality, a measurable radial error bounded strictly below 1/4, and its Dini integral. Its full-ball vanishing conclusion and the non-Dini C2 stationary countertest match A2692-A2694.

Part(b) has the correct quartic for V=z(-y,x,0), the positive1/60 bound and centered mean equality. The general tangential-quadratic statement retains a nonzero divergence-free homogeneous quadratic Q and arbitrary quartic Poisson pressure; it does not inadvertently add a positivity premise. Both signs of the defect are asserted on each centered sphere, as in A2697.

Part(c) correctly defines the unrestricted quadratic coefficient, states compact attainment and the strict upper bound2499/10000, and uses the restricted equivariant optimum g_star only as a lower bound. Swirl is allowed; the pressure is not assumed equivariant. The exact quartic equation and root interval identify g_star. The 2/17 example and fixed-field optimum(6-sqrt30)/24 are separate lower bounds, not competing unrestricted maxima.

Part(d) keeps the C3/C4 hypothesis and correctly states the sharp implicit coefficient max(1/6,Gamma2), with a strict inequality required for vanishing and nonzero polynomial pairs at every smaller coefficient. The explicit coefficient2499/10000 is sufficient because it is strictly greater than that implicit threshold. The displayed interval[1/6,2499/10000) and the contrast with the C2/C1 quarter endpoint are correct.

The verdict cell lists exactly the confirmed and open scopes. In particular, automatic applicability to an actual profile and whether Gamma2 exceeds1/6 remain open. These four mathematical statements are confirmed. The separate closing sentence requires the scope repair below.

## 4. A polynomial stationary example and a negative-c profile

The row's closing assertion about the polynomial examples must be restricted to the explicit quadratic examples in(b)-(c). It cannot cover the polynomial sharpness family in(d), nor assign a stationary-Euler failure to an abstract maximizing pair whose construction uses only Poisson and divergence.

Here is an exact counterexample to the unrestricted polynomial assertion, already part of the confirmed LIT318 sharpness proof. Put rho2=x^2+y^2 and

    V=rho2(-y,x,0), P=rho2^3/6.

This is a nonzero polynomial pair with V=DV=P=0 at the origin and P=|V|^2/6. The azimuthal speed is rho^3. Direct differentiation gives

    div V=0,
    (V.grad)V=-rho^4(x,y,0),
    grad P=rho^4(x,y,0).

Thus it solves stationary Euler and therefore its Poisson equation. It is a valid sharpness pair at every gamma<=1/6, a range always contained in gamma<=max(1/6,Gamma2), independently of the unresolved value of Gamma2.

It also shows why an unqualified extension to every real similarity parameter is invalid for this family. V is homogeneous of degree three and equivariant under rotations about the third axis, so y.grad V=3V and (Jy.grad)V=JV. Its rotating similarity residual is

    (1-c)V+((cy-omega Jy+V).grad)V+omega JV+grad P
      =(1+2c)V.

At c=-1/2 it vanishes for every omega. The pair grows at infinity, so it is not a decaying profile and is outside the target positive-c range. No campaign counterexample is produced. At every c>0 the residual is nonzero for this fixed pair.

The safe closing wording is: The explicit quadratic examples in(b)-(c) are not stationary Euler fields and are not rotating similarity profiles. The non-Dini pair in(a) and the cubic swirl used for sharpness in(d) are stationary Euler fields. None of these explicit examples is a decaying profile in the target range, for any omega. The abstract maximizing pair has no further Euler claim here.

The exact broad nonstationarity assertion is refuted by the displayed polynomial. If the original closing sentence was intended to refer only to the explicit quadratic formulas, its intended restricted meaning is compatible with the audits; the required repair is to say so.

## 5. Assembly verdict and limits

The D4-D6 implementation, the four substantive pressure statements and the audit-history transfer are confirmed. Cumulative approval of this new pin is left open pending the closing-sentence scope repair. The earlier A2717 approval is unaffected. No pressure theorem or conditional Euler theorem is withdrawn.

This audit concerns the front matter, changed main text and AppendixA. Historical AppendixB, unexamined auxiliary files and future edits remain outside its scope. The repeated D3 source audit A2721-A2723 happened after this candidate's cutoff and is not silently included in its recorded verdict history. The unrestricted nonexistence conjecture remains open.


## 6. The b2f0773e integer-notation delta

The next pin is b2f0773e04f2a1ffe9102662313d42d9fa0869d8d8bd598238b38e3c18cb64a5, with 1035871 bytes and 7014 lines under the build convention. All four independently generated contextual hunks were read. The generated delta equals the coordinator's delta exactly. The only mathematical-text edit writes the union in D5.11 over positive integers k and m, with delta=1/k, instead of using N for the integers after N has denoted the equilibrium set. This preserves the countable union and its measurability argument. A point eventually remaining in a compact regular region also remains there after some positive integer time, so excluding time zero from this index loses no point. The other three hunks record this repair, its assembly time and its history.

The unchanged pressure closing sentence retains the Section4 scope problem. This delta is confirmed, but it does not itself warrant cumulative approval of the new pin.

## 7. The exact meaning of the coefficient 2/17

The LIT321 example has E=rho^4+9rho^2 z^2+z^4 and P=2E/17+z^4/34. Away from the origin E is positive, so

    P/E=2/17+z^4/(34E).

The minimum ratio is exactly 2/17, attained at every point of z=0 with rho>0. The ratio is strictly larger when z is nonzero. Thus the phrase "ratio exactly 2/17" should say "minimum ratio exactly 2/17" or state P>=2E/17 with equality on that plane. This clarifies the already verified inequality and does not change its feasible coefficient. It also corrects any shorthand in this agent's earlier dated notes; no constant-ratio identity for LIT321 was proved. A2725 confirms the inequality and optimal lower coefficient for this fixed pair, not a spatially constant ratio.

## 8. Targeted comparison with C's Section2A precision review

C's full checklist and its withdrawn Step4 point were read. The actual relevant report passages were checked. In Lemma2.2, G starts as a distribution; after h=partial P-G is shown harmonic, h is smooth and partial P is continuous. Consequently G has a continuous representative, and the Step4 rescaled integral also follows directly by linearity of the distributional pairing. There is no missing regularity hypothesis or required repair at this step.

The corollary's labels (a), (b), (d) deliberately follow the source. Remark2.8(3) explicitly refers to the missing item as "of the source" and explains the improvement. Relabeling or an explanatory parenthesis could help a reader, but the omission is not a mathematical gap. The coordinator's earlier decision to preserve these labels is compatible with the statements. This is a targeted regularity and numbering check, not a new full audit of Section2A or of its external sources.


## 9. The a2c344a9 repair and full-flow paragraph

The next pin is a2c344a9a06490447562defede09a5c95b5f5c4650bb13d2d72e138f0859b4e0, with 1038570 bytes and 7034 lines under the build convention. All five independently generated contextual delta blocks from b2f0773e were read, including the entire 21961-byte pressure-row block. The generated delta equals the coordinator's supplied delta exactly.

The pressure row now restricts the nonstationary and positive-c similarity-failure statements to the explicit quadratic examples. It identifies the non-Dini example and the cubic polynomial swirl as stationary Euler fields and limits the final exclusion to decaying profiles in the target range. This removes the ambiguity refuted in A2726 without denying the negative-c cubic profile. The abstract maximizing pair is not assigned an additional Euler property. The row also gives the minimum pressure ratio of the LIT321 pair, as in Section7, and defines rho as the horizontal radius. Both pressure wording repairs are complete.

The new remark after D3.1 accurately separates Schreiber's supremum and Morris's discrete attainment. On K times the unit sphere it takes maximizing derivative segments, whose invariant weak limit has the uniform exponent as its integral of the instantaneous logarithmic growth. An ergodic lifted component with at least that integral projects to an ergodic flow measure with at least that top exponent; the uniform derivative bound gives the opposite inequality. This is exactly the compact-set proof in Section3 of the independent D3 recheck. No compactification is needed because K is invariant. Compactness supplies integrability for Birkhoff and Oseledets. The remark therefore supplies the required full-flow attainment step.

Point46 records A2721-A2723 with the correct scope and explicitly excludes a fresh D3(c) or whole-source certification. The source erratum is identified as already recorded and unused. The remaining status and history hunks accurately record the assembly and cutoff.

## 10. Cumulative approval of a2c344a9

The baseline5639599f was approved by A2717. The fifteen-block delta to2eab7ba5 was checked in Sections1-5, the four-block delta to b2f0773e in Section6, and the five-block repair to a2c344a9 in Section9. The only outstanding pressure wording issues are now resolved. Static inspection finds nine actual Markdown tables and597 rows, with no column-count mismatch, absolute local path or em dash. No rendered-page, browser or mathematical-computation check is claimed.

The exact a2c344a9 pin is cumulatively approved for front matter, main text and AppendixA at recorded cutoff A2723. This approval does not include historical AppendixB, unexamined auxiliary files or future changes. It does not turn a conditional theorem into an unconditional one. The arbitrary-helicity decay-only conjecture remains unresolved.
