# A quantitative log-degree improvement from an eventually zero cycle

Status: CONFIRMED after the independent theory-part review dated2026-10-31T05:25Z and verifier recheck. This statement depends on the triangular deficit structure of topic67 and the exact frequency-gap cancellation of topic68.

## Statement

Let Q>=3 be odd, delta=2/Q, c=Q/(Q-2). Let f_1 be a nonzero finite real S1 sine polynomial whose nonzero frequencies are odd multiples of an odd M>Q. Let L be its highest frequency. Use the canonical polynomial-log recurrence with every resonant stream constant zero. Put

    K_* = floor((Q(L+1)+2)/4)+1,
    A = K_*+3,
    B(k) = max(0, k-ceil((k+3)/A)).

Then, with t=log r,

    deg_t F_n <= B(floor((n-1)/Q)),
    deg_t G_n <= B(floor(n/Q)).                         (1)

A zero polynomial satisfies any displayed degree bound. In particular the limiting upper log-degree slope is at most (1-1/A)/Q, strictly smaller than the universal slope1/Q. This theorem bounds polynomial degree only. It does not by itself improve the coefficient Gevrey estimate or prove convergence.

## Definitions

A density block k consists of F_(Qk+r),1<=r<=Q, and a stream block k consists of G_(Qk+r),0<=r<Q. Their universal degree bound is k-1, except for the finitely many low orders. A deficit-d column has degree q=k-1-d>=0. Let C_d be an upper bound for the block indices of all nonzero deficit-d columns, in either field and all positions.

The two prerequisites give:

1. At fixed deficit d there is one unknown resonant scalar per block. Its transfer to the next block is kR(k)/(k-d), and R(k)=0 for every k>=K_*.
2. All other contributions at deficit d use strictly lower deficits. A product with two child indices greater than Q has child deficits a,b satisfying a+b<=d-1. A linear contribution with one low-order child uses one smaller deficit unless it is already included in the homogeneous cycle.
3. Partial_t terms use smaller deficits. The polynomial triangular inverses use only the finitely many columns above the target degree.

## Block arithmetic and support recurrence

For a stream child i=Qu+r,0<=r<Q, and a density child j=Qv+s,1<=s<=Q, the output density block at i+j is u+v or u+v+1. A final resonant stream integration advances the block by at most one. Thus a known quadratic forcing built from columns supported at u<=C_a and v<=C_b cannot reach beyond block C_a+C_b+2. A product with one low child cannot reach beyond C_a+2. Log differentiation, nonresonant Poisson inversion and density inversion do not change the order; their above-target columns are already among the smaller deficits. At the initial resonant stream of a block, a density coefficient can come from the immediately previous density block, costing at most one further block.

Using the deliberately loose total shift3 gives the following sufficient recurrence:

    C_0 <= K_*,
    C_d <= max(K_*, d+1,
               max_(a<d)(C_a+3),
               max_(a,b>=0,a+b<=d-1)(C_a+C_b+3)).       (2)

To justify the first term K_*, a known forcing at a block below K_* can propagate homogeneously only as far as K_*. Beyond that, the next homogeneous transfer is zero. A forcing at a later block can reach the next scalar and its finite within-block linear cycle, already covered by the shift3. The term d+1 includes the first block in which the target degree is nonnegative. Deficit0 receives only finitely many low-low initial interactions; their first stream log is at2Q, or block2. Since K_*>=2, the zero transfer beyond K_* proves C_0<=K_*.

This is a support bound, so arbitrary real sizes and signs of the coefficients cause no difficulty. Zero coefficients only reduce the support.

## Solving the recurrence

Set

    D_d=A(d+1)-3,  A=K_*+3.

Then D_0=K_*. If a<d, D_a+3<=Ad<=A(d+1)-3 because A>=3. If a+b<=d-1,

    D_a+D_b+3 = A(a+b+2)-3 <= A(d+1)-3.

Also K_*<=D_d and d+1<=D_d. Induction in (2) gives C_d<=D_d for every d.

If a deficit-d column in block k is nonzero, then

    k <= A(d+1)-3,
    d >= ceil((k+3)/A)-1.

Its degree q=k-1-d is therefore at most k-ceil((k+3)/A). Including the finitely many constant low-order blocks proves (1).

For example, Q=3 and f_1=sin(5theta) give K_*=6 and A=9. At stream block k the bound is max(0,k-ceil((k+3)/9)); the first strict improvement over k-1 occurs at k7, or stream order21.

## Verification and limitations

The finite verification uses the independent exact Cartesian polynomial-log recurrence and records all actual degrees for selected pure high harmonics. It also checks the block and deficit arithmetic as integer identities. Finite agreement is a test of the statement, not a replacement for the support proof.

The factorial norm estimate in topic17 used inequalities between the generic child and parent degree bounds. Those inequalities cannot simply be assumed for (1), because the improved degree uses cancellation in the resonant projection. Accordingly no improved Gevrey coefficient bound is asserted here. Full rational logarithmic convergence remains OPEN.

## Verification closure, 2026-10-31T05:29:25Z

The independent theory-part review is retained in sources/lead_review_20261031T0525Z.md. Its index and sign checks agree with the argument above and the independent exact computations. The stated theorem is CONFIRMED. No convergence of the complete rational logarithmic series is inferred.
