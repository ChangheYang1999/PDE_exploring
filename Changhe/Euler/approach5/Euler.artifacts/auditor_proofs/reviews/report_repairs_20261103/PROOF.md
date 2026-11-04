# Focused recheck of the current report corrections

Status: focused audit completed at 2026-11-03T08:01:00.229129+00:00; no new mathematical theorem. This recheck covers the named repairs, not every line of the changing report.

## 1. Sources and prior scope

The actual current `this report` was read at Lemma20, the proof of TheoremC item6, the corresponding 2D Lemma11(b), the entropy references, and the paragraphs and table rows identified by the coordinator label audit. The label-audit source was read in full. The earlier mathematical audits A479 and A490 remain the governing full-section verdicts; no expanded regularity or global coverage conclusion is added.

## 2. Lemma20 and positive densities

The revised null-set argument is correct. Incoming curve measures are absolutely continuous on regular embedded curves. A leaf-null set on almost every subordinate plaque is null on each relevant incoming curve: all relevant unstable leaves coincide, intrinsic open subsegments cover its good points, and a countable leaf-chart subcover converts leaf arclength zero to ambient one-dimensional Hausdorff measure zero. Integration gives the claimed global null-set property.

The Radon-Nikodym replacement is valid. Choose the subordinate partition with measurable finite positive plaque arclength, refining bounded local Pesin charts if necessary; normalized arclength then gives a measurable probability kernel lambda_s. With rho_s=mu_s+lambda_s and m=integral rho_s dq, the global densities f=dmu/dm and g=d(integral lambda_s dq)/dm disintegrate into f rho_s and g rho_s. Their quotient projections are q, so these are probability conditionals for almost every s. Uniqueness gives mu_s=f rho_s and lambda_s=g rho_s. The measurable set {g=0} is lambda_s-null almost everywhere, hence mu-null by the preceding argument. Therefore mu_s=(f/g)lambda_s almost everywhere. The ratio is only used on {g>0}.

The entropy citations now separate the lower bound from Ledrappier-Strelcyn and the upper bound from Ruelle, at the compact C2-diffeomorphism scope already imported and checked in the earlier audit. The proof no longer attributes both directions to the part of Ledrappier-Young proved in PartI.

The proof of TheoremC item6 now explicitly invokes the positive plaque densities from Ledrappier-Young Corollary6.1.4, with Corollary6.2 for the nonergodic version. The matching 2D Lemma11(b) explains positivity and finite plaque arclength. No assertion that a density positive only at almost every regular point automatically stays positive on an entire plaque is used. The whole-flow basin and compactification premises remain explicit in the surrounding theorem.

## 3. Label corrections verified in the current report

The report now separates axisymmetric pressure, which only removes the azimuthal velocity at A034 scope, from axisymmetric velocity, for which the rotation terms cancel and the nonrotating theorem applies. The associated summary and section8 citations were changed to the A046 cancellation method with A010.

TableA now states that additional hypotheses in column2 are conditional, and its stray blank line was removed. The flat-periodic row cites A536-A537 for the two confirmed statements, adds nonzero U to the periodic statement, and leaves the further single-component accumulation assertion unaudited. The literal label 'middle clause' at the row end is an obsolete positional description because the unaudited clause is now last; its mathematical status is nevertheless explicit.

The B26 row annotates the A311/A314 refuted side statements and the A315 open single-basin claim. The A344 row identifies A342 as refuted and A343 as open. The jet row now uses local C^k for the k-jet statement. The CO16 rows now state compact trapping. The A317 equivalence is confined to its earlier C-infinity and A312 finite-regularity scopes. The historical status line explicitly marks A519 open and the A520-A523 claim helicity-free.

These changes repair the flagged scope errors. Two presentation precautions remain: choose finite measurable local plaques when introducing normalized arclength, and avoid treating the entire result table as unconditional. The current table caption does the latter correctly. This audit does not certify later CO29/CO30 additions or the entire continuously changing report.

## 4. Verification

No computation or new external source was needed. Actual configured-model coordinator revision and referee files were compared with the prior independent audit.
