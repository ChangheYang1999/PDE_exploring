# Independent finite audit of stream-to-density feedback

Status: finite interval audit CONFIRMED in V174. No all-order lower bound or cancellation estimate is claimed.

## Statement and notation

Fix delta=2/3, c=3 and f_1=sin(theta), with the canonical polynomial-log stationary recursion. Put t=log r, p_j=1-2j/3, P_i=2-2i/3 and lambda_n=2(n-1). Write M_n=||F_n||_* and N_n=||G_n||_* for the sum of the absolute values of every sine and monomial coefficient.

For i+j=n define the density contribution

    X_(n,i)=(lambda_n-3D)^(-1)[(P_i+D)G_i partial_theta F_j
                                -partial_theta G_i (p_j+D)F_j],
    D=partial_t.

Then F_n=sum_(i=1)^(n-1) X_(n,i). The feedback term is X_(n,n-1); the leading-stream term is X_(n,1). For n>=8 the edge sum uses i=1,2,3,n-3,n-2,n-1, and the remaining density polynomial is the sum of products with4<=i<=n-4.

The finite audit recomputes these quantities at precisely the orders listed in its artifact. Norms of the individual terms do not give a lower bound on the norm of their sum, because the contributions may cancel. The suggested cap on N_n/M_n is therefore a heuristic unless an additional cancellation estimate is proved.

## Independent algebra and inverse

The polar identity u.grad rho=(psi_r rho_theta-psi_theta rho_r)/r, with u=(-psi_y,psi_x), gives the displayed forcing after matching i+j=n. Its linear part is -(lambda_n-3D)F_n, so the sign in the definition of X is positive.

As in topic84, encode iF and iG by signed real Laurent polynomials in z with positive coefficients half the sine amplitude and opposite negative-frequency coefficients. Angular differentiation becomes the Euler operator z partial_z in the transformed forcing. The independent forcing is therefore

    (P_i+D) mathcal G_i E mathcal F_j
       - E mathcal G_i (p_j+D) mathcal F_j.

Kronecker substitution at output order n uses stride4n+1 and angular offset2i for an order-i input. Products have angular offset2n and no carry into the log exponent. Ordinary Arb polynomial multiplication then computes every angular and log convolution coefficient without using the theory part's trigonometric product routine.

For a polynomial S=sum_q s_q t^q, the inverse is computed by descending substitution,

    x_q=[s_q+3(q+1)x_(q+1)]/lambda_n,

starting beyond the highest degree with zero. This proves (lambda_n-3D)X=S and uniqueness on polynomials, because lambda_n is nonzero for n>=2. It is algebraically identical to the finite Neumann inverse but uses a different evaluation order from the theory part's implementation.

## Verification scope and evidence

The input checkpoint contains dyadic coefficient balls. The audit decodes them at640 bits, preserves outward rounding, compares the selected full nonlinear low orders coefficient by coefficient, and computes norms and ratios by intervals. It retains the frozen peer table, source code, input digest, every comparison and the real elapsed time. A matching interval calculation establishes a finite consistency check. It cannot prove the infinite sequence is geometric or that a feedback term survives cancellation.

Dependencies: the polar derivation in topic01, the polynomial-log recursion in topic17, and the independent Laurent identities and non-aliasing proof in topic84. The exact low-order recurrence was verified separately before these high-order checks.

The completed audit covers14 selected orders through290, with183 peer comparisons and235 complete low-order nonlinear coefficient checks. All pass. The full intervals and actual time are retained in verification/20261031T072709Z/checks.json and summary.json.
