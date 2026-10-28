# Interval defects and their repairs in the polar certifier

## Statement and scope

The analytic cell estimates in the parent PROOF.md remain valid when their interval inputs enclose the intended quantities. The source archived in ../sources does not meet that enclosure contract for arbitrary valid interval inputs. Three counterexamples below refute its generic implementation claim. They do not prove that any particular default-grid numerical enclosure is false. The separately archived ../sources_repaired_0700 fixes these counterexamples.

The corrected implementation remains conditional on the external witness seminorm bound, complete grid coverage and correct recombination. A successful finite diagnostic does not certify a full numerical run.

## Sign enclosure

On the right half-plane put w=x-1. The polygon boundary has height |w| for -1/2<=w<=b. The old code uses the expression w when the interval comparison w<=0 is undecidable and w<=b holds. This need not enclose |w|.

At 80-bit precision, take x=arb("0.995","0.01"), y=arb("0.01"). This x interval contains x0=arb("0.986"). The old sign function returns -1 for the whole interval and +1 at x0. The point sign is correct because |x0-1|=.014>.01. Thus the whole-interval sign assertion is false.

The repaired function uses abs(w) whenever w<=b and the ray formula when w>b; an undecidable branch boundary returns None. Since absolute value and the ray formula enclose the boundary on their certified domains, a strict comparison against |y| proves the chosen sign. The counterexample now returns None.

The informal argument in num Note 07:01(c) does not by itself establish unreachability. For an asymmetric interval w=[-2 epsilon,epsilon], |w| has upper endpoint 2 epsilon, not epsilon. Hence |y|>sup w does not imply |y|>sup |w|. A proof for actual grid centroids would have to use their additional geometric separation, not this invalid interval implication.

## Angular extrema

For the exterior midpoint grid, the exact condition outside both radius-one-half pole disks is |cos(theta)|<=rho. The extrema of |cos| must therefore be included whenever the angular interval may contain them.

The old chained Arb comparison theta1<=q<=theta2 can be false because a comparison is undecidable, even when the true extremum lies strictly inside the exact interval. The reproducible example in verification/old_counterexamples.json takes q=pi/2 at 80 bits, theta1=q.mid(), theta2=q.upper(), rho2=10^-26 and rho1=rho2/2. The old function discards the entire cell. At 160 bits one verifies that theta=pi/2+rho2/2 lies strictly between the endpoints and |cos(theta)|<3rho2/4. This is a strict exterior point, with an open neighborhood in the exterior. The discard is therefore invalid.

The repaired rule includes q unless q<theta1 or q>theta2 is certified. This may enlarge the range of |cos| but cannot exclude a possible extremum. The counterexample now returns a nonzero-width interval for one partial cell.

## Nonfinite partial bounds

For radii 5*10^-31 and 10^-30 and angular endpoints q.lower(), q.upper(), the old partial-cell path raises a mathematically nonnegative base to a fractional power using an interval whose lower endpoint is slightly negative. It returns NaN and does not reject the result.

The repaired code uses the nonnegative-power helper and checks finiteness at the partial cell, task total and final enclosure. The example now yields a finite symmetric interval. The same safe-power rule is applied to the midline witness branch. Replacing squares by products and using a nonnegative square-root helper in the profile Hessian only improves a previously safe fallback.

## Verification and consequences

code/check_note14_repairs.py was run separately against both immutable snapshots. Its source hashes and complete outputs are in verification/. All three old defects reproduced and all three repaired examples passed. The latter check establishes these repairs only; it is not an exhaustive proof of the software.

V094 is narrowed to its analytic method conclusion. Its generic implementation endorsement is superseded by this audit. V101's proposed numerical endpoint remains OPEN, so no accepted numerical constant is retracted. The accepted one-dimensional Stieltjes certificates use a different implementation and are unaffected.
