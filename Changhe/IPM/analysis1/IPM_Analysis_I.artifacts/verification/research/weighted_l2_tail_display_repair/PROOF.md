# Directed decimal repair for the conditional weighted L2 tail expressions

Date 2026-10-22T02:24:45.430028+00:00. This proof is written before the new numerical repair check. The theorem and arithmetic application remain OPEN until the two checks, actual model review and later own adjudication complete.

## Statement and scope

Use the exact scalar inputs and conditional integration theorem of weighted_l2_tail_reduction/PROOF.md, with its accepted evidence/verdict.json. Write B_i=pi C_i^2 exp(2(a-5)), B_o=pi C_o^2 L^(2+2delta) exp(-2delta(b+17))/delta, delta=1/2-k>0, and F for the exact sum of the three recorded binary64 finite-region values. Write Q=sqrt(F+B_i+B_o).

The numerical lane has replaced three-digit/nearest-rounded labels with directed decimal labels in a new version of src/r2_tails.py and runs/r2_tails.json. This result checks that the five saved upper labels (B_i, B_o, F, sqrt(F), Q) are above independent outward enclosures of the corresponding EXACT SCALAR expressions. It also checks the revised report's arithmetic statement that the sum of its three separately printed finite-region ceilings is below3.9563e-7, while the exact binary64 sum F is below3.95619e-7. These are different sums and must remain distinct.

The new code extracts a dyadic upper endpoint u=m*2^e from an Arb ball. It converts that exact rational to Decimal at precision80 using ROUND_CEILING, obtaining d>=u, then quantizes d toward positive infinity to a decimal place selected for10 or12 significant digits. The emitted decimal v therefore satisfies v>=d>=u. A change of place caused by an exponent carry does not affect this inequality. The check will replay this code path at200-bit Arb precision, capture u exactly, and independently verify v>=u with integer rational arithmetic. This proves outwardness of the applied labels; no nearest-rounded printed ball is treated as an endpoint.

## Proof of the arithmetic statements

For any real u>0 and decimal lattice spacing s>0, ceiling quantization gives s*ceil(d/s)>=d. Correct directed conversion gives d>=u. Composing these two inequalities proves the stated algorithm. All intermediate Decimal operations in the source must retain ROUND_CEILING and sufficient precision for the quantization to exist. The applied digits10,12 and context precision80 meet that requirement, and replay must finish without an exception.

Independently of that source algorithm, let [l_A,u_A] and [l_I,u_I] be the Arb512 and iv220 enclosures of a target scalar. If the saved decimal q, parsed as an exact rational, exceeds both u_A and u_I, it is a strict scalar upper ceiling. Overlap of the two intervals is a consistency check; each implementation uses a separately justified arithmetic path. The first path evaluates the direct expression in exp(a-5), exp(b+17)/L and powers. The second uses separated logarithms and an exp(log/2) square root. Positivity ensures all logarithms and roots exist. The exact binary64 finite sum requires no transcendental evaluation, and an additional rational comparison will check both its report ceiling and the sum of the three printed finite-region ceilings.

The tail constants in the report are slightly enlarged terminating decimals. The corresponding B_i and B_o increase quadratically, so they must be evaluated separately when checking6.504e-16 and3.819e-20. Check the report's6.2899e-4 also against the square root after these enlarged tail terms, in addition to Q formed from the exact original scalar constants. This is a conditional scalar bound in either case.

## Dependencies and limits

Snapshot the new foreign source, result and report before checking them, and record all original paths and hashes. Rehash the complete accepted parent and preserve the original rejected labels. No source in the numerics lane is executed or modified. Two independent exact parsers and numerical paths will check the saved decimal comparisons and the corrected printed sum. A complete actual Claude Opus5.5 review and a later independent adjudication are required before an accepted verdict.

This result does not verify that C_i,C_o bound a physical residual, that F bounds finite-region integrals, that those cells cover the intended annulus, or that all quantities refer to the same normalized trial. The accepted parent's physical hypotheses remain OPEN. It proves repair of saved scalar/display arithmetic only. No full-plane physical norm, inverse estimate, distance to X3, nonlinear closure or PDE endpoint follows.
