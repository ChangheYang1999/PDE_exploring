# Audit of the producer's finer three-quarter-exponent certificate

## Exact mathematical statement

Use the real homogeneous Holder seminorm of exponent 3/4, the circular principal-value trace-free operator T_xx, and R_1^2=T_xx-I/2. Use the globally admissible polygon-plus-projection witness with b=3/4, c=-3/10 and lambda=50/53 from ../pole_profile/PROOF.md and its cited global profile certificate. That proof gives [f]_(3/4)<=1 and an exact identity-term gain 1/2. The compact approximation theorem transfers its increment to the operator norm defined using smooth compactly supported test functions.

The positive lower endpoint obtained from this folder's task intervals and the independently proved omitted-region enclosures is therefore a lower bound for D_(3/4), provided the finite tasks satisfy the stated interval and coverage contract. No numerical endpoint is accepted until a completed acceptance record is written. This is an audit of producer task records plus selected independent replays, not a full independent evaluation of every fine-mesh cell. The separate delta=.005 full replay is V233.

## Source and task contract

The producer used delta=.0035, 80-bit directed arithmetic, full-circle angular loops, near-pole annuli from 10^(-6) to 1/2, and midpoint annuli from 1/100 to 10^16. The task sidecar carries every task's exact decimal radial endpoints, angular count, depth, witness parameters, midpoint ball, radius ball, cell count and error categories. The start and end source digests agree. The local snapshot must match both those digests and the sidecar's start digests.

The cell evaluator differs from the already audited refined snapshot only in provenance recording inside its main routine. An abstract-syntax comparison verifies equality of every other top-level statement and function; the two imported geometry modules have identical file digests. The full source diff is retained for inspection. The interval method is therefore the method audited in ../PROOF.md, ../repairs/PROOF.md and ../refined_cells/PROOF.md. Its first-order errors use the global Holder bound and optional certified Lipschitz bound. Its second-order errors apply only when one smooth branch is certified throughout a cell ball. Mixed and partial cells keep their fallback absolute error bounds.

For a serialized task midpoint ball [m_-,m_+] and nonnegative radius ball [r_-,r_+], the imported exact rational interval is

    [m_- - r_+, m_+ + r_+].

In particular, neither the uncertainty in the midpoint text nor the uncertainty in the radius text is dropped. The task import checks finite values and exact parameters for every record. It checks strictly increasing radial edges, matching adjacent endpoints with no gaps or overlaps, even positive angular counts, and exact endpoint coverage of both systems. It checks the total cell count against the producer summary. Full-circle coverage follows from the audited angular loop over indices 0,...,ntheta-1.

## Independent replay and recombination

A separate single-process driver re-evaluates selected complete tasks distributed over both near and midpoint systems, using the frozen cell formulas. Selection includes endpoint tasks and tasks around changes in angular count and region type. Every selected task's midpoint/radius enclosure and cell count are compared with the stored record; a mismatch blocks numerical acceptance. The selection, actual execution times and outcomes are recorded separately. This check is corroboration of the finite computation, not a proof that the unsampled tasks were independently rerun.

The imported task intervals are summed as exact rational endpoints. The original producer's inner disks, sliver and absolute exterior bounds are recomputed independently, giving a conservative comparison with its printed endpoint. The printed decimal alone is not used as an input bound.

For the stronger recombination, a finite prefix of the near-pole task system may be replaced by the quadratic pole theorem of ../pole_profile/quadratic_lower/PROOF.md; its explicit active-profile conditions are checked with outward arithmetic. The exterior uses ../homogeneous_tail/PROOF.md and its angular_error refinement, with all limiting-profile conditions checked. The midpoint sliver keeps its explicit absolute bound. These are exactly the analytic formulas used in V233. The imported task endpoints are not narrowed by the selected replays.

If the resulting trace-free increment enclosure is [L,U], then

    D_(3/4)>=1/2+max(0,L,-U).

The final ten-place decimal is rounded downward from that exact rational expression. The acceptance record identifies every dependency, selected task, source digest, omitted-region bound and final endpoint. All claims remain restricted to the exact witness and parameters stated here.
