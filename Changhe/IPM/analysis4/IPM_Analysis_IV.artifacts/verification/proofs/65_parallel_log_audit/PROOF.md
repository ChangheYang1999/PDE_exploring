# Pair-partition audit of the logarithmic recurrence

Status: CONFIRMED for the finite coefficient checks and the partition/serialization argument below. This is an implementation audit, not an infinite convergence theorem.

## Claim and conditions

The numerical experiments' new Arb `step_fast_parallel(workers)` computes an enclosing version of the same ordered quadratic sum as its serial logarithmic recurrence. The audited source is retained in sources/. The mathematical claim concerns its arithmetic and data partition; process scheduling and operating-system fault tolerance are outside this audit.

For order n, the worker with index w receives precisely those velocity indices i in {1,...,n-1} congruent to 1+w modulo the positive worker count. These sets are disjoint and their union is the complete index set. Each worker takes j=n-i and computes

    ((P_i+partial_t)G_i) partial_theta F_j
       - (partial_theta G_i) ((p_j+partial_t)F_j).

The existing packed product implementation supplies these two products; its signs and reflected frequencies were independently checked in topics33 and45. Summing the workers' results therefore includes each ordered pair once, with no additional factor of two. The parent then applies exactly the existing triangular density inverse and Poisson inverse. Both are linear algebraic operations on coefficient enclosures, already independently derived from Cartesian differentiation.

Serialization stores the exact dyadic midpoint and radius. Reconstruction first raises precision sufficiently to recover the midpoint exactly and then adds the recorded radius with outward rounding. Thus changing addition order can enlarge an interval or alter its midpoint, but cannot discard the exact coefficient enclosed by the arithmetic.

## Independent finite check

The audit calls the actual worker function and actual parent arithmetic while replacing only `Pool.map` with sequential calls. No process or listener is created. It alternates worker counts2,4,7 and verifies45 pair partitions. It independently recomputes the complete Cartesian Laurent-log recursion for:

- delta2/3, f_1=sin(theta), through order24;
- delta4/9, f_1=sin(theta), through order24;
- delta1/2, f_1=(2/3)sin(theta)-(1/5)sin(3theta)+(1/11)sin(5theta), through order18.

All12187 exact rational coefficients, including expected zeros and all log columns, lie inside the computed Arb intervals. Containment is checked using exact rational dyadic endpoints, not by converting the target rational to another rounded ball. Another45 serialization cases cover three precisions, five exponent scales and negative, zero and positive centers. All preserve the input enclosures. Actual execution time was2.7328464929014444 seconds.

The first version of the test used `arb.contains(fmpq)`. That operation tests inclusion of the internally rounded target ball and can reject an interval that contains the exact rational point. The retained first-attempt log records this test limitation. Replacing only the comparison with exact endpoint arithmetic resolves it; no peer recurrence code was changed.

Dependencies: topics10,21,33 and45. Sources, the exact case conditions and every checked partition are retained beside this proof.
