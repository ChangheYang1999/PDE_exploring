# Residual derivative bounds on selected cells by analytic continuation

## Exact statement and inherited inputs

Use the exact normalized modal trial of modal_repair/PROOF.md, the canonical moment input certificates of residual_samples/PROOF.md, and the exact polynomial binding of residual_point_jets/PROOF.md with its mandatory addenda and final verdict. The point construction has thirteen exact centers t_c and original cell endpoints l<t_c<r with t_c=(l+r)/2. Set h=(r-l)/2>0 and z=(t-t_c)/h. Every selected cell lies in one original middle polynomial span. The trial has C6 radial joins, as proved in modal_repair/PROOF.md. Therefore the residual has the derivatives through order five used here, including their continuous endpoint limits.

This result concerns only these selected closed cells, not their complement and not a complete cover. Moment boxes are inherited canonical input certificates; neither method below performs another integration. For each cell define the entire analytic continuation in the complex variable z by continuing its local density polynomial and solving the moment ODEs with those exact center values. This continuation need not agree with the physical density outside the original span. It agrees with the true canonical moments and residual on the selected real cell by uniqueness of the first-order ODEs. A complex disk crossing a spline knot causes no difficulty because it is the continued local function, not the physical piecewise function, on that disk.

Write w_j=2j+1, m_n=2n, H_261=0 and rho=exp(3t)sum_{j=0}^{260} H_j(t)sin(w_j theta). Let epsilon_N(t), 0<=N<=521, be the full odd residual coefficients, including the highest possible mode1043. For i+j<=5 the goal is an outward upper bound for

    sup_{l<=t<=r} sum_N (2N+1)^j |D_t^i epsilon_N(t)|.

That bound controls the indicated differentiated Fourier-Wiener quantity on the entire real cell. A comparison to a producer W_i_j remains separate: a larger independent upper bound does not refute a smaller valid upper bound. No finite point lower bound is promoted to a cell maximum location.

## Analytic coefficient and derivative tail theorem

Let f_N(z) be analytic on a neighborhood of the closed disk |z|<=4, with Taylor coefficients a_Nq, and assume

    sum_N w_N^j sup_{|z|<=4}|f_N(z)| <= B_j.

Cauchy's coefficient formula and the triangle inequality imply

    sum_N w_N^j |a_Nq| <= B_j / 4^q.

Let N0=64. On |z|<=1 the polynomial contribution to the i-th t derivative is bounded by

    h^(-i) sum_N w_N^j sum_{q=i}^{N0} (q)_i |a_Nq|,

where (q)_i=q!/(q-i)! and (q)_0=1. For q>=N0+1 the ratio of successive positive terms (q)_i/4^q is

    (q+1)/(4(q+1-i)) <= (N0+2)/(4(N0+2-i)) = eta_i < 1.

Consequently the omitted derivative tail is at most

    T_ij = B_j h^(-i) (N0+1)_i / [4^(N0+1)(1-eta_i)].

The finite polynomial contribution plus T_ij is the asserted bound. The tail is derived from the analytic function itself, not by differentiating a uniform remainder. All sums are finite except the explicitly bounded geometric tail. The Cauchy estimate is applied mode by mode before summation, so the premise must bound the sum of modal suprema, not merely the supremum of a summed angular function.

## Explicit disk majorants from the density moments

For a polynomial P in s=t-t_c define |P|_R=sum_q |P_q|R^q, with R=4h. On the continued disk |s|<=R, define C_j=|H_j|_R and C_j^+=|(D_t+3)H_j|_R. The density modal bounds are

    D_j=exp(3t_c+3R) C_j,
    E_j=exp(3t_c+3R) C_j^+.

The moment ODEs I_n'=-(m_n+4)I_n+H_{n-1} and J_n'=(m_n-4)J_n-H_n imply, by integration along the straight segment from0 to s,

    Ibar_n=exp((m_n+4)R)(|I_n(t_c)|+R C_{n-1}),
    Jbar_n=exp(|m_n-4|R)(|J_n(t_c)|+R C_n).

These inequalities follow because the segment has length at most R, the polynomial is bounded by C, and the exponential propagator is bounded by exp(|lambda|R). They also cover m_n=4, when the second propagator is constant.

The full velocity amplitudes satisfy

    p_n=-(m_n/2)exp(2t)(J_n-I_n),
    q_n=exp(2t)[m_n(J_n+I_n)-H_{n-1}-H_n]/2.

Thus take

    pbar_n=(m_n/2)exp(2t_c+2R)(Ibar_n+Jbar_n),
    qbar_n=exp(2t_c+2R)[m_n(Ibar_n+Jbar_n)+C_{n-1}+C_n]/2.

For angular order j, a valid sum of modal disk suprema is

    B_j = |c| sum_a w_a^j E_a + sum_a w_a^j D_a
          + sum_{n,a}(m_n+w_a)^j [pbar_n E_a+qbar_n w_a D_a],

where c=1/k. To prove it, use the sum and difference sine identities. Each product gives half its amplitude at each of two frequencies, and |w_a-m_n|^j <= (w_a+m_n)^j. The two halves sum to at most the displayed term, also when a negative sine frequency is folded. Summing over n and a gives the bound for the sum of coefficient suprema. The binomial expansion of (m+w)^j permits evaluation by products of one-dimensional weighted sums, without a quadratic modal loop.

## Independent disk majorants from physical Green modes

Set S_n=(H_{n-1}+H_n)/2 and

    g_n(t)=exp(4t)[S_n'+4S_n+(m_n/2)(H_n-H_{n-1})].

From A_n'= -m_n A_n+g_n and B_n'=m_n B_n-g_n, put

    G_n=exp(4t_c+4R)|S_n'+4S_n+(m_n/2)(H_n-H_{n-1})|_R,
    Abar_n=exp(m_n R)(|A_n(t_c)|+R G_n),
    Bbar_n=exp(m_n R)(|B_n(t_c)|+R G_n).

Then both full velocity amplitudes are bounded by

    exp(-2t_c+2R)(Abar_n+Bbar_n)/2.

Using this common upper bound in the preceding B_j formula gives another valid disk majorant. The two majorants need not agree. Each is proved independently, and their minimum is valid after both computations have passed their own outward-arithmetic checks.

## Taylor coefficients and independent arithmetic

Use the scaled variable z to compute coefficients through degree64. The moment recurrence is

    (q+1) I_{q+1}=h[-(m+4)I_q+H_q],
    (q+1) J_{q+1}=h[(m-4)J_q-Hnext_q],

where H_q now denotes the coefficient of H(t_c+hz). The physical recurrence replaces I/J by A/B and their displayed forcing g. Multiplication by exp(beta h z) is a finite coefficient convolution with (beta h)^q/q!; discarded coefficients cannot affect those of degree<=64. Compute the two residual products from rho_t, rho_theta and the full p,q amplitudes.

Both angular and radial products can be encoded into an ordinary polynomial. Store signed angular frequency f at index offset+f and radial power q at index (offset+f)*129+q. Input radial degrees are at most64, so products have radial degree at most128, strictly below129. Thus no radial carry can corrupt the angular frequency. The largest product angular index is2086 and all extracted odd modes must be retained. Ordinary polynomial multiplication is noncyclic.

The first calculation uses Arb physical Green coefficients and ball polynomial multiplication. The second uses iv density moments and exact integer polynomial multiplication after outward dyadic quantization. The integer product radius is |m1|r2+r1|m2|+r1r2, as proved in the point-derivative result. Input coefficient intervals and all exponential operations must be rounded outward. Compare every retained coefficient, and compare factorial-scaled coefficients0..5 with the accepted direct-scatter point jets. Intersect only proved valid overlapping coefficient enclosures. Reconstruct the finite sums and all tails independently from saved exact intervals and positive scalar bounds.

No cell result is accepted until the exact partition inputs, all comparisons, analytic majorants, Cauchy tails, saved-output hashes and final mathematical scope have been independently audited. This proof does not establish complete derivative coverage, a global forcing norm, a global inverse, a nonlinear estimate or an IPM endpoint.
