# Coverage requirements for margin replacement

## Claims and scope

The finite-section accounting defect of proof 176 does not occur in the inspected run_section.py, run_section_l2.py or run_norms.py reductions. Each sums only the final worker files, with a fixed worker index set. In run_section.py, a resumed worker loads its own cumulative checkpoint and skips its recorded cells before writing its complete final file; the final reduction does not add that checkpoint again. This is a source-code statement about the specific duplicate-sum mechanism. It is not a fresh certification of all numerical outputs or of every possible restart configuration.

The inspected outer_merge.py, however, does not prove coverage of the region it replaces. Its endpoint assertion is insufficient. It also does not require every angular box in that region to have a finite new bound. A claim that its current checks alone certify the new global minimum is refuted by the following exact counterexamples. No particular completed margin certificate is invalidated here: this helper was listed as an optional future run, and the already accepted original-data certificates were independently checked.

## A radial gap that passes the endpoint check

Let the original radial partition consist of [0,1], [1,2], [2,3]. Let new computations cover only [0,1] and [2,3]. Their minimum left endpoint is0 and maximum right endpoint is3. The helper sets its replacement range to that convex hull, removes all three original cells, and checks only that the minimum and maximum endpoints of the removed original cells equal0 and3. Both assertions hold. The new cells nevertheless omit the open interval(1,2).

Take a function equal to10 on the first and third cells and equal to-100 on the middle cell. The two new lower bounds10 are exact on their cells. The helper's minimum after replacement can be10, whereas the actual infimum is-100. Thus its returned value need not be a lower bound. Continuity can be imposed without changing the example's conclusion by using a negative smooth bump supported strictly inside(1,2).

## An angular gap that passes selection

The helper selects a new radial cell if any entry of its MA_ref row is finite. It then uses a nan-minimum of that row or the selected block. Consider one radial cell with two angular boxes and a row [10, NaN]. Selection succeeds and the nan-minimum is10. No estimate has been supplied for the second angular box, where the function may again equal-100. Consequently the selection and nan-minimum do not prove an all-angle lower bound.

The same logical issue arises if the field used for selection is finite but a different reported field is missing on some boxes. Each asserted quantity needs its own complete finite cover or a retained valid old bound at the missing positions.

## Sufficient replacement conditions

For each replaced original radial cell, the new intervals must have a union containing that entire cell. This can be checked with exact rational endpoints by sorting and verifying that each next left endpoint is no larger than the current covered right endpoint, and that the final covered endpoint reaches the original cell's right endpoint. Endpoints of half-lines must be treated as such, not as a finite sentinel. For every angular box and every reported quantity, the new estimates must be finite on this cover. Alternatively, retain the original valid bound wherever no new estimate is supplied. A replacement is then justified by taking the minimum of valid bounds over a complete cover.

The inspected family_combine.py does not sum overlapping estimates. It takes the maximum of old and refined lower bounds at each matching box, then a minimum. This operation is mathematically valid when all entries refer to the same object, parameter pair, radial cell and angular box, and when its floating slack is verified. Duplicate input of a valid bound cannot change the answer because max(a,a)=a. The script does not itself authenticate all this metadata; this audit makes no new certification of its fixed floating slack.

The inspected merge_margin.py uses the repaired all-angular-entry cell mask, rejects overlapping cells and reports missing cells. Its warning for an incomplete cover must be respected. None of these source-code observations supplies a missing off-basis or complement estimate.
