# Conditional scalar cover from the origin inverse floor

## Statement and hypotheses

Let c=4076476460239181/2251799813685248, d=c-1 and A=1+1/c.
The exact reference is C1-N1-007-d2w-j7-e2bal, with canonical potential
SHA-256153c1adc6f48b28ab34c8e4aa670dcfdcb7c6faae8c13490a942e9a2319fa316.
Its verified origin coefficient is a0. Assume a0>=5c-4, 1<c<2, and
all domain, coefficient, input-hyperplane and dyadic norm hypotheses
of the proposed T4 origin inverse theorem, copied into source/.
That theorem is a separate OPEN analytic input until independently
reviewed. It proposes, for the actual inverse used in the registered
FW-T-DYADIC-Y-v1 scheme,

    0<s<c-1,   M>=1/(c-1-s).                             (1)

Assume also the already audited low-rate ceiling beta<=1+c-ca and
velocity constant lower bound C_U>=1. The proposed stronger necessary
condition is

    Y(F) < H(d) (1+c-ca)/(1+a),    0<a<A,
    H(d) = max_(0<s<d) (d-s) sqrt(4 pi s(1+s)).          (2)

The calculation below combines this conditional ceiling with the
independently confirmed two-mode lower bounds of N4-113. It asserts no
unconditional application of (1) before that analytic review.

## Derivation and exact maximum

The scheme gives M Y(F)<=R and the strict absorption inequality
C1 R(C_U+a)<beta, with C1=1/sqrt(4 pi s(1+s)). Combining this with
(1), beta<=1+c-ca, and C_U>=1 gives (2) before maximization.
For 0<s<d, the square divided by 4 pi is

    f(s)=(d-s)^2 s(1+s),
    f'(s)=(d-s)[d+(2d-3)s-4s²].

The bracket is positive at zero and negative at d; its two roots have
opposite signs because their product is -d/4. Thus f increases then
decreases on [0,d], with its unique maximum at

    s_star=(2d-3+sqrt((2d-3)^2+16d))/8.

Both endpoints give zero. This proves the formula for H(d), without
a numerical optimization assumption. Outward evaluation of s_star
and of the displayed expression encloses the exact maximum.

## Lower bound and finite cover

Let J_n(a)=||(1+r²)^((2-a)/2) Delta Pi_n F||2 for the full-circle sine
projection Pi_n. The N4-113 certificate and its independent peer check
give rigorous J_1 and J_3 at quarter points 0 through7/4. Set
J_13=(J_1²+J_3²)^(1/2). The reviewed plateau inequality gives

    Y(F)>=5^((a-2)/2)J_13(a).

J_13 decreases with a, and (1+c-ca)/(1+a) decreases on [0,A].
For a cell[l,h], evaluate J_13 at e>=h. The strict outward inequality

    5^((l-2)/2)J_13(e) > H(d)(1+c-cl)/(1+l)             (3)

therefore excludes (2) throughout the cell. Use quarter cells up to
3/2 and the final cell[3/2,A] with e=7/4. These cover [0,A]. For
A<=a<2 the registered positive low-rate condition already fails.
The endpoint zero is used only as a comparison bound for the open
admissible parameter range.

Every input is rehashed and its exact candidate identity checked.
The origin coefficient is independently recomputed from the canonical
potential, rather than substituted as a rounded decimal. The resulting
finite scalar inequalities are new N4 arithmetic and await peer
reproduction. If all pass, they establish a conditional full-parameter
obstruction to this scheme. They neither prove nonexistence of the
profile nor dispense with the proposed origin theorem's review.
