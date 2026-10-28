# Coupling distinct radial intervals

## Statement and hypotheses

Use the real homogeneous Holder space, kernels, circular principal values
and quotient extension of ../../../../01_setup/PROOF.md. Fix0<a<1 and
0<delta<1/2. Retain the signed cell masses, residual estimate, two identity
atoms and exact nonnegative transport plan of ../PROOF.md. All hypotheses
on certified cell signs and lower masses in that theorem remain in force.
The present result only specifies a smaller admissible support cost for
edges between different radial intervals. It does not assert an improved
numerical operator norm.

Let a source cell have radial interval [r0,r1] and unit-circle arc A,
and a destination cell have interval [s0,s1] and arc B. Both cells lie
in one of the two disks of radius1/2 centered at x=(1/2,0) and y=-x.
Their parametrizations are x+r*u and -(x+s*v), respectively, after
central reflection for a left-disk cell, with u in A and v in B.
For cells at the same pole put

    M_same = max over r in{r0,r1}, s in{s0,s1}
             sup over u in A,v in B |r*u-s*v|.

For cells at opposite poles put

    M_opposite = max over r in{r0,r1}, s in{s0,s1}
                 sup over u in A,v in B |1+r*u+s*v|.

An edge between different radial intervals may be assigned the cost
M_same^a or M_opposite^a according to its poles. Any outward upper
enclosures for these two quantities are also valid costs. In particular,
if U,V are complex rectangles containing A,B, the maximum of the four
rectangle-norm upper bounds provides such an enclosure.

With these edge costs the entire bound (1) of ../PROOF.md, and its
small-disk, middle, exterior and phase completion, remain valid.

## Proof

For fixed u and v, the norm of either affine expression is convex in
r with s fixed. Thus its supremum over r lies at r0 or r1. With r at
an endpoint the expression is convex in s as well, so its supremum
over s lies at s0 or s1. Taking the supremum over u and v yields the
displayed four-corner bounds. No joint convexity assumption is needed.
A complex rectangle that contains an arc also contains every endpoint
expression obtained by its substitution; outward complex arithmetic
therefore encloses the required norm. The function t to t^a is
increasing on the nonnegative reals, so raising an upper norm bound
to a preserves the bound.

The extraction construction in ../PROOF.md assigns a nonnegative
measure of mass m to each incident portion of a cell. For an edge of
mass q between distinct radial intervals, couple the two portions by
the product of their normalized measures, multiplied by q. Its support
is contained in the product of the two cells. Its cost for the metric
|z-z'|^a is therefore at most q times the stated edge cost. Summing over
the finitely many edges gives precisely the extracted part of (1).
The remaining variation is still paired with its central reflection,
so the residual estimate and all singular-integral limits are unchanged.

## Computational use and scope

A floating sparse linear program may include candidate edges between
any chosen radial rows and choose a flow. Its candidate cost may use
midpoint distances. Neither its objective nor numerical feasibility is
a certificate. The retained flow must be rounded to integer units,
all leftover units explicitly paired, and every integer marginal
checked exactly. Every edge actually used, including a repaired edge
between distant rows, receives one of the outward costs proved above.
No restriction on row separation is part of the mathematical theorem;
a row window only limits the candidate search.

This theorem concerns the local contribution to D_a with the full
identity atoms present. A number from one phase is not an operator
bound. The completion requires every necessary phase and the separate
middle/exterior costs, with the phase correction stated in ../PROOF.md.
The implementation and a pilot remain to be checked independently.
