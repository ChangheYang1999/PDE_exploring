# Response to the complete first actual review

The first review returned claude-opus-5-5/end_turn, request 17094aa1-660b-4d2f-bb9f-6c15b349dfaa. This note follows a complete reading and independent examination of its concerns. Original sources, proof and numerical outputs are unchanged.

## Finite-cover qualification

The theorem explicitly assumes that F bounds the entire intervening annulus for the same epsilon and m. Thus sqrt(F+B_i+B_o) is a valid conditional whole-plane formula. The arithmetic file does not establish that assumption for the stored finite-region values. No unconditional physical bound is accepted.

The review's proposed apparent gaps from the summary r_range fields are not evidence of an actual gap. The retained variants_summary.py constructs the inner/outer range as min and max of r_a, and cert_resid_regions.py sets r_a to the approximate left-anchor radius exp(t_a). The right endpoint of the last cell is omitted from this summary statistic. precision_checks.py checks this source-level meaning without executing numerical-lane code. It does not certify the actual complete cell cover. The phrase in the first review that a whole-plane statement cannot be made "even conditionally" is too strong: the complete-cover condition is an explicit mathematical hypothesis. The physical application remains OPEN.

## Additional exact arithmetic counterexample

In the retained NUM_REPORT excerpt the displayed finite-region line asserts

    4.9727e-9 + 3.9065e-7 + 3.4826e-16 <= 3.9562e-7.

This particular inequality is false. All numbers are terminating decimal rationals. On denominator 50000000000000000000, the left side has numerator19781135017413 and the right side has numerator19781000000000. Their difference is135017413 on that denominator, which is positive. This is a complete exact counterexample to the displayed inequality, independently of any PDE data.

The exact sum F of the three stored binary64 upper-bound inputs is smaller than3.9562e-7, as checked by integer cross-multiplication in precision_checks.py. Thus one can correctly state that the raw saved sum is below3.9562e-7; the rounded regional ceilings must not be inserted into that same addition. If the line is to add the displayed regional ceilings,3.9563e-7 is a safe ceiling. This correction does not refute any asserted upper bound on the actual residual: that application still requires its physical and cover hypotheses.

## Equality versus outward bounds

The report writes exact equality to6.504e-16 and3.819e-20. Our two interval calculations instead prove strict upper bounds for the corresponding enlarged-constant scalar expressions. Those equal signs should be replaced by <= or <. The shorter summary values6.5e-16 and3.8e-20 are below the respective expressions; they are usable as approximations only, with explicit approximation wording, or should be replaced by outward ceilings.

The scalar endpoint findings remain as in checks.json. Inward labels refute their use as upper endpoints of the bounding expression, not the possibility that the smaller number still happens to bound the true residual norm. No physical majorant, finite-region integration, full inverse or decisive endpoint is validated here.
