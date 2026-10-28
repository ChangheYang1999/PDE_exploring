# Direct trace-free upper certificates at six exponents

## Statement and current status

Let 0<a<1. Use the real homogeneous Holder seminorm
[f]_a=sup_{x!=y}|f(x)-f(y)|/|x-y|^a on the plane, modulo constants.
Let T_xx have circular principal-value kernel
(z_1^2-z_2^2)/(2 pi |z|^4), and let T_xy have kernel
z_1 z_2/(pi |z|^4). For inputs of possible growth |z|^a, define
increments by the convergent difference of kernels at infinity,
as in ../../01_setup/PROOF.md. The common seminorm operator bound
C_a satisfies the six certified inequalities

| a | C_a upper endpoint |
|---|---:|
| 1/1000 | 637.0404763100 |
| 1/100 | 64.0882805059 |
| 1/20 | 13.1843720067 |
| 1/10 | 6.8520467682 |
| 1/5 | 3.7444366045 |
| 99/100 | 42.2253356279 |

Status: CONFIRMED in V131. Source identity, exact coverage and independent
320-bit recombination pass at every exponent. The complete independent
geometric replay at a=1/5 also passes, including all 51 regional phase
comparisons. The 1/1000 row is weaker than the already accepted
linear-remainder upper bound and is retained only for comparison.

## Complete reduction to the finite checks

Fix an output increment of length one and transfer its direction
into the phase of the angular kernel. Let delta=1/64 and put

    a2(a)=2^(1+a/2)/(pi(a+2)),
    S_a=2 a2(a)delta^a/a
          +(1+2delta)^a delta^2/[2(1-delta)^2].

The local angular transport theorem bounds both singular disks by
S_a. Its first term is the exact circle-transport cost of the two
own-pole kernels; its second term bounds the two smooth cross terms
by central reflection. Neither principal value nor a local identity
term is omitted: these are the trace-free kernels, not R_1^2.

On each of the remaining three regions use the already proved
finite transport bounds: paired local circles outside radius delta,
the truncated middle circles, and exterior circles about the
midpoint. Denote their costs at phase phi_j=j pi/32 by L_j,M_j,E_j.
The exact phase interpolation theorem with 16 half-intervals gives

    C_a <= S_a + sec(pi/64) max_(0<=j<=16)(L_j+M_j+E_j).       (1)

For each spatial cell the code extracts only mass with certified sign
and a nonnegative certified lower bound. It moves that extracted mass
by a nonnegative integer transport plan whose marginals are checked
exactly. It pairs all remaining mass with its central reflection,
using an outward upper bound for its total variation. Distances and
radial moments are evaluated by ball arithmetic. Thus every extracted
edge and every residual contribution is an upper bound on the
functional on [f]_a<=1. The exterior's omitted part uses the already
proved positive angular series and its explicit remainder. These
arguments, including all singularity and infinity limits, are in
../../08_improved_upper_bounds and the frozen proof in
../closed_form37_lead/PROOF.md. They apply independently at each
exponent; no interpolation in a is being used here.

The local and middle geometric routines and all their transport
helpers are byte-identical to the previously audited V124 source.
The exterior routine differs from the previously audited version
only by its module search path. Here its reference exponent is the
same as its evaluation exponent. A floating optimizer only chooses
a candidate plan. The integer marginal check and ball cost evaluation
supply the inequality, regardless of optimality.

The independent auditor reads all 93 frozen files and checks their
hashes. At every exponent it proves that the 256 local radial rows
and all 17 phases occur exactly once, and that the 512 middle radial
rows occur exactly once with the specified reference exponent. It
checks the 128-row exterior parameters and the 17 returned phases.
It recomputes S_a and the right side of (1) at 320 bits without
importing the submitted aggregator or any optimizer. Each decimal
in the table is at least the exact rational upper endpoint of that
recombination. The complete records are in
verification/independent_audit.json.

## Reproduction and dependencies

Run code/audit_table37_lead.py from the artifacts root. Its source is local
to the verifier's working copy. source/snapshot_manifest.json binds the frozen files.
The selected a=1/5 geometric replay uses the verifier's original
local, middle and exterior programs, with outputs saved under
verification/replay_a20. It is performed one process at a time.
The result concerns homogeneous seminorms and fixed exponents only;
it is neither an exact norm nor a full supremum-plus-Holder bound.
