# Compact interval certificates for every rational response

Status: PROVED. All exact interval covers were replayed in V295; the theory part independently reviewed the compact formula at11:52Z, recorded in V306. The convergence theorem145 is also PROVED.

## Statement and notation

Fix positive coprime h,Q with Q>2h, an even bandwidth B, and exact finite leading amplitudes. Let delta=2h/Q. Assume the low fields F_1,...,F_Q and G_1,...,G_(Q-1) are defined by the rational stationary recurrence. They are independent of all later free harmonics. At a resonant order n=kQ let q=2hk-2. The Q-step response sigma_k is defined in144. If q>=BQ, its positive and negative carrier supports remain disjoint throughout the response calculation.

Put t=1/q and encode the positive carrier as z^q times a Laurent polynomial in the bounded offset variable. For a high field whose radial degree is -q-alpha, define the scaled Cartesian operators

    X_t z^v = t(v-alpha)z^(v-1)/2 - [1+t(v+alpha)/2]z^(v+1),
    Y_t z^v = t(v-alpha)z^(v-1)/2 + [1+t(v+alpha)/2]z^(v+1).

These are exactly q^(-1) times the Cartesian derivatives, with the common carrier retained. A high density at step s has alpha=1+delta s; its stream has alpha=delta s. Ordinary low Cartesian operators use their actual radial degrees.

Let U_r be the positive-carrier density response at step r and V_r its particular stream response for r<Q. Start with the free harmonic's positive amplitude e=1/2, alpha=0. Then

    U_r=(1-delta)/(1+[2+delta(r-1)]t)
         * { T_t(e,F_r)
               +sum_(s=1)^(r-1)[T_t(V_s,F_(r-s))+T_t(G_(r-s),U_s)] },

where T_t(A,F)=X_t A YF-Y_t A XF when the first field is high, and T_t(G,A)=XG Y_t A-YG X_t A when the second is high. The stream inverse acts on a high density coefficient a_v by the two contributions

    V_(v+1) += -a_v/[2(v+1-delta s)],
    V_(v-1) += t a_v/[2(2+(v-1+delta s)t)].                 (1)

The first denominator is nonzero for1<=s<Q. For q>=BQ, the second denominator stays positive on the relevant t interval. The desired response is

    sigma(t)=2[z^(2h-1)]U_Q,
    sigma_k=sigma(1/(2hk-2)).                              (2)

At t=0, the second contribution in(1) vanishes and these identities reduce exactly to144's limiting-response operator.

## Proof of the compact recurrence

The high radial degree and angular mode are -q-alpha and q+v. Substitution in the Cartesian formulas gives X_t,Y_t immediately. Also

    lambda_(n+r)/q=[1+(2+delta(r-1))t]/(1-delta),

because delta n=q+2. Dividing every linear response equation by q gives the stated recurrence.

For a stream output at offset u, the divided Laplace denominator factors as

    ((q+u)^2-(-q-delta s)^2)/q
        =(u-delta s)[2+(u+delta s)t].

The density input at offset u+1 has divided x-derivative coefficient t(u-delta s)/2. The input at offset u-1 has coefficient -[2+(u+delta s)t]/2. Cancelling the respective nonzero factors gives(1). No large carrier powers are represented in the computation. Support separation ensures that the other carrier cannot contribute to the requested frequency, so(2) holds for all integers in the stated range.

## Interval coverage certificate

Enclose each exact leading amplitude by a rationally certified interval. Compute the finite low fields with outward-rounded interval arithmetic, then evaluate the compact recurrence on closed rational t intervals. Each result encloses sigma(t) simultaneously for every real t in that interval. If its absolute-value enclosure is bounded below by a prescribed rational s>0, all relevant integer responses in the interval satisfy |sigma_k|>=s.

A binary partition begins at [0,1/(2hK-2)] with K large enough for support separation. At any node, a successful lower-bound check closes the node. Otherwise split at its rational midpoint. A node may also be closed without evaluating the response when it contains no point t=1/(2hk-2) with integer k>=K. For a node [a,b] with b>0, the possible integers satisfy

    ceil((1/b+2)/(2h)) <= k <= floor((1/a+2)/(2h)),

where a=0 removes the upper bound. These inequalities are tested in exact rational arithmetic. Thus a finite tree of accepted or empty nodes covers every integer k>=K, including the unbounded tail at t=0. Responses k<K are checked by the full two-carrier Cartesian response recurrence. This proves an explicit uniform lower bound.

Every saved node stores its exact interval and status. Accepted nodes additionally store the response as exact dyadic midpoint and radius in the files ending coverage_exact.json. The earlier decimal display alone is insufficient when Arb prints a wide signed interval as a symmetric enclosure. Replaying its parent splits verifies coverage independently of floating-point display. A failure to close a node is a failed certificate attempt, not evidence of a zero response.

## Dependencies and scope

The Cartesian encoding is01; the affine response is119/130/144. Root intervals and compatibility are supplied by exact algebraic certificates, not inferred from interval residuals. Interval induction gives finite and infinite-tail enclosures. Applying them to the majorant145 still requires that theorem's independent review. No improved convergence radius is inferred from finite root-test plots.

## Completed four-ninths certificates

For the five real roots in increasing order, the exact uniform lower bounds are

    2^-29, 2^-24, 2^-25, 2^-14, 1.

All finite responses k=1,...,16 pass. The tail starts at k=10 and is covered by1772,163,757,2007,567 exact dyadic leaves, respectively. Of these,780,90,280,1053,270 are accepted response intervals; all others contain no relevant integer index. The independent replay reconstructs every interval from its binary address, checks all integer exclusions, checks that adjacent leaves meet exactly, and verifies abs(midpoint)-radius>s in rational arithmetic. Thus every integer k>=1 is covered.

The initial interval calculation took374.3803240088746 actual seconds. Its decimal serialization was too coarse for independent lower-bound replay. Recomputing all2473 accepted leaves on the unchanged partition and retaining exact midpoint/radius pairs took101.94462103908882 seconds. The original files and failed replay are retained in the evidence. The exact replay and majorant checks in150 then passed. This correction changed the representation of the certificate, not its mathematical lower bounds.
