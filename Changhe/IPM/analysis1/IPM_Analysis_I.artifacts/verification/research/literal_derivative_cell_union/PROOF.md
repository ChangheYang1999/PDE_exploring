# Exact union of the saved derivative-row intervals

2026-10-21. Written before the new exact geometry calculation. This is a supplement to weighted_derivative_scalar_norms, whose accepted files stay unchanged.

## Statement, hypotheses and notation

Let I_i=[a_i,b_i], 0<=i<n, be a finite family of nonempty closed real intervals, with b_i=a_i+h_i and h_i>0. The numbers a_i and h_i in this result mean the exact binary64 values stored in the frozen inner, middle and outer derivative rows. An addition performed after conversion to exact rational arithmetic defines b_i. It is not the rounded binary64 addition.

Put A=min_i a_i and B=max_i b_i. The open connected components of [A,B] minus union_i I_i are uniquely determined by these finite rational endpoints. A running-maximum merge and an independent endpoint event sweep calculate exactly the same components and total length. If the a_i and b_i are both strictly increasing in the given order, the components are precisely the positive adjacent gaps (b_i,a_(i+1)). Without the second monotonicity hypothesis that adjacent-gap inference need not hold.

## Proof of the merge algorithm

Sort intervals by increasing a_i, breaking ties arbitrarily. Keep the right endpoint R of the last component of the union of intervals processed so far. Initially R=b_0. If a_i<=R, the interval meets that last component and replaces its right endpoint with max(R,b_i). If a_i>R, no processed interval covers any point of (R,a_i), and no later interval can do so because all later starts are at least a_i. This is therefore exactly one open gap, and a new union component ends at b_i. Induction proves the algorithm and its completeness. Disjoint gaps have lengths equal to their right minus left endpoints, so finite additivity gives total missing length as their sum.

If both endpoint sequences are strictly increasing, R=b_(i-1) at every step. Thus the merge gaps equal the positive adjacent gaps. This conclusion applies only after both inequalities have been checked on all actual endpoints.

## Proof of the independent endpoint sweep

At each distinct endpoint x form the integer net event c(x)=number of starts at x minus number of ends at x. Sort the distinct endpoints x_0<...<x_m. On (x_j,x_(j+1)) the number of covering intervals is the sum of all events up to x_j, because no interval starts or ends in that open segment. Thus precisely the segments with count zero are the open gaps. An endpoint shared by ending and starting intervals belongs to the closed union; the net event correctly leaves no positive gap there. Isolated uncovered points cannot occur in the complement of a finite closed union within its hull: that complement is relatively open and contains neither hull endpoint. This proves that the sweep supplies all the same gaps. Count positivity outside zero segments and a final count of zero are checkable invariants.

Every binary64 datum is a rational with denominator a power of two. Multiplying all endpoints by a common sufficiently large power of two therefore turns the entire sweep into integer arithmetic without approximation. The first engine may instead use reduced rational arithmetic and the running-maximum algorithm. These are separate algorithms and separate import paths for the same exact source values.

## Dependencies, audit plan and scope

Use the immutable source rows and exact row export pinned by topic152. The first method checks every a_i,h_i against that export, computes b_i with flint fmpq, checks both endpoint monotonicities, and merges. The second method decodes IEEE754 bits directly from the original source JSON values, makes an integer common grid, performs the event sweep without using the first method's interval list, and compares all exact components, their count and total length. Record both within-region and all-region results, including joins.

These are claims only about the literal saved row intervals. They neither establish nor refute a producer's potentially wider intended certified interval without separately checking that producer. They provide no derivative bound on a gap, no weighted norm contribution estimate there, and no bound for either omitted infinite tail. In particular the conditional union norm theorem in topic152 is unchanged, and no global inverse estimate or decisive IPM endpoint follows. Numerical smallness of missing log-length is not permission to discard it.
