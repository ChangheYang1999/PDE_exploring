# Certified longer prefixes at period nine

Status: PROVED in V574 after all ten Cartesian prefixes, independent polar replays and exact rational box replays passed. The proof preceded computation.

## Statement

Fix Q=9, delta=2/Q, c=Q/(Q-2), and one of the ten real roots b of the corresponding compatibility polynomial certified in267. Let f_1=sin(theta)+b sin(3theta). Let f_n,g_n be the unique tuned pure density and stream coefficients from those results. Their radial exponents are p_n=1-2n/Q and P_n=2-2n/Q. The nth density frequencies are odd and at most4n-1; the stream frequencies are positive even and at most4n.

At n=kQ, k>=2, the free stream coefficient is H_n sin((2k-2)theta). Let sigma_k be the response of the next forbidden density coefficient to a unit change in H_n. Use the already proved lower bound |sigma_k|>=s>0 for this root. Choose N=M Q with M>=2 and rational upper bounds

    d_n >= n ||f_n||_1 > 0, 1<=n<=N,
    e_1=0, e_a >= aQ |H_(aQ)|, 2<=a<M.

Here ||.||_1 is the sum of the absolute sine coefficients. Put

    L=3Q^2/[4(3Q-1)],
    kappa=4[2-delta+max(delta,1-delta)](1-delta)/delta * (N+1)/N.

Let Phi, J, Y0 and G be the finite nonnegative residue system below. If a rational vector v>=Y0 satisfies G(2^-q,v)<=v for an integer q, then the density, stream and common-potential series, with every fixed appropriately weighted spatial derivative, converge absolutely and uniformly on each closed exterior

    r>=R>2^(q/2).

For leading amplitude epsilon!=0, the sufficient radius becomes 2^(q/2)|epsilon|^(Q/2). This certifies only a sufficient exterior. It asserts neither a sharp threshold nor a global stationary extension. The common potential retains the finite logarithms proved in132 and270.

## Finite prefix determination

The polar recurrence is lambda_n f_n=sum_(i+j=n) T(g_i,f_j), where lambda_n=(n-1)delta/(1-delta) and T(g_i,f_j)=P_i g_i f_j'-p_j g_i' f_j. The equivalent signed Laurent Cartesian calculation is (Xg_i)(Yf_j)-(Yg_i)(Xf_j), where the artificial Y derivative represents partial_y/i. The Poisson equation is -Delta psi=partial_x rho.

At a resonance n=kQ, compatibility sets the sin((2k-3)theta) coefficient of f_n to zero. To choose H_n, provisionally continue with H_n=0 and let R_n be the next forbidden density coefficient at n+Q. The response identity130 gives that coefficient as R_n+H_n sigma_k, because two changed high-order factors cannot enter before n+Q. Thus H_n=-R_n/sigma_k. Its denominator is nonzero by the previously admitted response bound. Induction determines every requested finite coefficient uniquely. Projection of a resonant interval to exact zero uses this identity or the initial algebraic compatibility polynomial; mere interval inclusion does not supply the identity.

Compute the finite prefix using directed rational interval arithmetic. Compare its first2Q density coefficients and the streams before2Q with exact Cartesian polynomials evaluated at the independently refined root. Independently recompute each sigma_k from its low-order linear response, and compare the first direct two-continuation difference with it. Check every Poisson coefficient and every structural projection. Upward rational rounding of the interval norms and free harmonics gives valid d_n and e_a. A separate positive-frequency polar calculation at2048 bits repeats the entire prefix, derives every response from two provisional continuations, and checks every archived norm and free harmonic against its Cartesian enclosure and rational majorant input.

## Majorant and complete application argument

The certified-prefix theorem175 applies with B=4 and the displayed L=243/104 and kappa. For clarity, its scalar recurrence after N is the following. Initialize x_n=d_n through N, eta_(aQ)=e_a for a<M, and all nonresonant eta_n=0. At n>=N divisible by Q, set for r<Q

    u_(n,r)=kappa [L sum_(i+j=n+r, i,j>=r) x_i x_j
                 +sum_(i+j=n+r, j>=Q+1) eta_i x_j
                 +2L sum_(j=1)^(r-1) d_j u_(n,r-j)],

and define eta_n by the same expression at r=Q divided by s. After each base order set

    x_(n+1)=kappa sum_(i+j=n+1) (L x_i+eta_i)x_j.

Every right-hand side uses previously defined quantities. The Poisson column bound is L, and the advection bound after weighting by total order is kappa. The provisional-continuation and response identity therefore prove by induction that x_n>=n||f_n||_1 and eta_n>=n|H_n|.

Group x_(N+r+kQ), eta_(N+kQ), and u_(N+kQ,r) into ordinary generating series in w=z^Q. Their order is Y=(V_1,...,V_(Q-1),E,X_1,...,X_Q). Projection of the scalar recurrence defines the polynomial map Phi(w,Y) of175. At w=0 its unknown-dependent part J is nonnegative and strictly lower triangular. Thus T=(I-J)^(-1) is the finite sum of powers of J, Y0=T Phi(0,0), and

    G(w,Y)=Y0+T[Phi(w,Y)-Phi(0,Y)].

The nonconstant part has nonnegative coefficients and positive w degree. Iteration from zero stabilizes coefficient by coefficient. The exact rational inequality G(2^-q,v)<=v bounds every iterate, proving convergence of all residue majorants at that positive point. Their coefficient growth is at most geometric with base 2^(q/Q). Since z=r^(-2/Q), every strict radius R>2^(q/2) absorbs all fixed polynomial derivative factors. The finite bandwidth likewise permits a small angular analytic strip. Termwise differentiation and multiplication are then justified, so the stationary equations hold in that exterior. The potential reconstruction132 has the same geometric base. Homogeneity supplies the factor |epsilon|^(Q/2).

This proves the claimed implication using the admitted theorem175. The new work is to supply valid longer-prefix inputs and exact supersolutions. The replay reconstructs J,Y0,G from the rational inputs, compares the residue map to the independently indexed scalar recurrence through at least two w coefficients, and checks every box inequality without floating-point optimization assumptions.

## Dependencies and evidence

Dependencies:01,130,132,169,172,175,267,270,277,278. Retain input certificate hashes, root intervals, norm and harmonic enclosures, actual operation counts and elapsed time, exact rational box data, and a separate replay receipt. Full large coefficient arrays need not be archived because the finite recurrence and all root data are deterministic and retained.

## Period-nine input specialization

The exact compatibility polynomial has degree18 and ten real simple roots, as established in267. The low-order reference coefficients are the independently derived Cartesian polynomials through18. The all-index lower response bounds may be the old bounds from267, or rational numbers strictly below the global infima from278. In the latter case the receipt must name the278 certificate, prove the rounded lower bound is smaller than its directed infimum, and require278 to be admitted before using the new radius. Each root retains a separate bound and no claim is made between these isolated profiles except the already proved local genericity theorem.

A separate polar recurrence uses two full provisional continuations for every tuned harmonic, so it does not depend on the compact-response formula used by the Cartesian producer. It verifies overlap of the density and stream norms at every order and verifies the rational bounds used by every majorant box. This is a new execution of the previously audited261 protocol at Q=9; it does not introduce a different convergence mechanism.

## Completed period-nine applications

Admitted 2026-10-31T20:45:25+00:00. For roots in increasing order, the best q values are 127, 135, 144, 144, 143, 142, 142, 139, 140, 130, attained at the smallest retained prefix orders 36, 36, 54, 72, 36, 36, 36, 36, 36, 54. The sufficient exteriors are R>2^(q/2)|epsilon|^(9/2), with common exponent 72. These are sufficient bounds, without an optimality claim.

| Root | Response lower bound | Prefix N | q | Radius exponent |
|---|---:|---:|---:|---:|
| 1 | 4575000 | 36 | 127 | 127/2 |
| 2 | 9287/10000 | 36 | 135 | 135/2 |
| 3 | 671/2000000 | 54 | 144 | 72 |
| 4 | 173/400000 | 72 | 144 | 72 |
| 5 | 789/500000 | 36 | 143 | 143/2 |
| 6 | 857/200000 | 36 | 142 | 71 |
| 7 | 6837/1000000 | 36 | 142 | 71 |
| 8 | 4997/50000 | 36 | 139 | 139/2 |
| 9 | 49/400 | 36 | 140 | 70 |
| 10 | 2006 | 54 | 130 | 65 |

The checks comprise 6480 exact low-prefix comparisons, 1440 independently recomputed norm comparisons, 70 harmonic and response comparisons, and 2160 exact scalar identities across forty boxes. Actual summed runtimes are 525.464829 seconds for Cartesian prefixes, 585.258004 seconds for polar replays and 9.452386 seconds for rational replays. These sums are job times, not campaign wall time.
