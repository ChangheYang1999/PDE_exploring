# Ten convergent tuned profiles at delta=2/9

Status: PROVED in V549 and V551 after exact obstruction algebra, ten complete response and box replays, and the theory part's independent protocol review.

## Exact statement and hypotheses

Set delta=2/9, c_l=9/7, p_n=1-2n/9 and P_n=2-2n/9. Let the leading density be f_1(theta)=epsilon[sin(theta)+b sin(3theta)], with real epsilon nonzero. Work first at epsilon=1. For n>=2 the stationary coefficient is the sum of all ordered products Xg_i Yf_j-Yg_i Xf_j, i+j=n, multiplied by7/[2(n-1)]. Here X and Y are the Cartesian Laurent derivative operators of01, with Y representing partial_y/i. The stream inverse divides the frequency-m coefficient of Xf_n by m^2-P_n^2.

Let O_18(b) be the sin(theta) coefficient of f_18 computed through f_18 and g_17 with zero resonant harmonic. Define P_18 to be its primitive integer polynomial with positive leading coefficient. Every real root b with a uniform nonzero tuning response and a verified scalar supersolution as specified below gives a unique tuned exterior solution. The arithmetic must establish these hypotheses separately for each root. The exact algebra gives ten simple real roots of an irreducible degree18 polynomial. All ten satisfy the response and majorant hypotheses, with the constants recorded below.

## Compatibility and continuation

The positive sine stream resonances occur at n=9k and mode2k-2 for k>=2. At n=9 the formal resonant mode is zero and is absent by sine symmetry. Consequently all coefficients through f_18 and g_17 are fixed by f_1, and compatibility at18 is exactly O_18(b)=0. An exact rational Cartesian recurrence computes this polynomial without a trigonometric product convention. Its independent Poisson check is -XXg+YYg=Xf. A rational Sturm chain establishes all real roots. Squarefree, degree-preserving modular factorizations with independently certified factors can prove irreducibility when their possible proper factor degrees have empty intersection.

At n=9k choose the free coefficient H_(9k) in the sine mode2k-2. The next forbidden density coefficient is R_k+sigma_k H_(9k), where the nine-step linear response sigma_k depends only on f_1 through f_9 and g_1 through g_8. This affine identity follows because a perturbation at order9k enters the quadratic convolution linearly through the next nine orders. If sigma_k is nonzero, H_(9k)=-R_k/sigma_k enforces the next compatibility. Induction constructs the unique tuned formal series.

For bandwidth B=4, the compact positive-carrier response applies when2k-2>=36, hence k>=19, and has variable t=1/(2k-2) in[0,1/36]. The finite response values at k=2,...,26 are computed directly; the last eight must overlap their compact evaluations. A complete closed dyadic partition of[0,1/36], with exact integer membership, certifies a positive bound s on every integer-tail response. Empty leaves contain no integer index. Singleton leaves are evaluated directly. On each remaining closed leaf, degree-three Taylor coefficients at the center and an interval enclosure of the third derivative bound the entire leaf. The leaf touching zero includes the limiting response. Independent higher-precision evaluation and reconstruction of all endpoints are required.

## Majorant implication

Use the certified-prefix comparison of175 with N=18, density bounds d_n>n||f_n||_1 for1<=n<=18, and initial harmonic e_1=0. Its Poisson and advection constants specialize to

    L=3*9^2/[4(3*9-1)]=243/104,
    kappa=4*(2-2/9+7/9)*(7/2)*(19/18)=3059/81.

The factor19/18 bounds the first as-yet-uncontrolled total order; the response estimate divides only by the admitted positive s. These inequalities dominate every later density and harmonic coefficient by induction on order and resonance period. The nonnegative residue map Phi, triangular affine part J and inverse T=(I-J)^(-1) are exactly those of175 with these rational inputs. For Y0=T Phi(0,0), define G(w,Y)=Y0+T[Phi(w,Y)-Phi(0,Y)]. If a nonnegative rational vector v satisfies Y0<=v and G(2^-q,v)<=v, iteration bounds the sum of each nonnegative residue series at w=2^-q. Every scalar identity and every supersolution inequality is checked in rational arithmetic, separately from the interval response calculation.

Since w=z^9=r^-2, this implies absolute and uniform weighted convergence on each r>=R>2^(q/2). The angular bandwidth bound |m|<=4n absorbs every fixed derivative on a strict exterior, and gives a positive angular analytic strip there. The common-potential reconstruction of132 has the same geometric base with at most two finite logarithmic corrections, at orders9 and18. The convergent derivatives justify the density-potential identity, velocity reconstruction, multiplication and the stationary equation. Homogeneity multiplies the physical radius by|epsilon|^(9/2), while responses scale byepsilon^9. Thus the sufficient exterior is R>2^(q/2)|epsilon|^(9/2). No sharp radius, global canonical extension, nonzero logarithmic coefficient or open interval of c_l follows from this certificate alone.

Dependencies:01,131,132,169,172,175,232,234. Source code, exact polynomial data, interval covers and replay evidence are retained alongside this proof. The theory part's separate polar obstruction computation and accepted protocol review are retained in sources and verification.

## Exact finite algebra admitted

V549 at 2026-10-31T19:40:26+00:00 establishes that P_18 has degree18, is irreducible over the rationals and has exactly ten simple real roots. Independent signed-Cartesian and positive-frequency polar computations agree on all19 coefficients and the obstruction scale. The five modular degree patterns are (19:1,3,5,9), (23:1,1,4,12), (37:1,2,3,3,4,5), (47:3,4,11), (53:2,16); their proper subset-degree intersection is empty. Every root is isolated to width at most1e-60. The exact calculation used153 ordered nonlinear products, checked Poisson identities through17 and took987.30026seconds. The separate exact coefficient comparison took0.07869seconds. This finite admission alone does not establish infinite convergence; that conclusion is supplied by V551 below.

## Completed convergence certificates

The ten roots are ordered increasingly in the exact obstruction receipt. For each root the 768-bit construction and 1024-bit replay check 25 finite responses,8 full/compact comparisons, all 1,978 signed exact-prefix coefficients, a complete closed Taylor cover, and 54 exact rational scalar identities. The replay sums Taylor terms separately while sharing the audited jet algebra. Each row gives a unit-amplitude response lower bound and a sufficient exterior R>2^(q/2)|epsilon|^(9/2).

| Root | Response lower bound | q | Radius exponent |
|---|---:|---:|---:|
| 1 | 1048576 | 130 | 65 |
| 2 | 1/8 | 139 | 139/2 |
| 3 | 1/16384 | 148 | 74 |
| 4 | 1/16384 | 148 | 74 |
| 5 | 1/4096 | 147 | 147/2 |
| 6 | 1/1024 | 145 | 145/2 |
| 7 | 1/1024 | 146 | 73 |
| 8 | 1/64 | 143 | 143/2 |
| 9 | 1/64 | 144 | 72 |
| 10 | 256 | 134 | 67 |

The common sufficient radius is 2^(74)|epsilon|^(9/2). All weighted derivatives converge on every strict closed exterior, and the common-potential expansion solves the stationary equation exactly there. Topic270 separately proves that its order9 potential logarithm is nonzero at every root. These conclusions do not assert a sharp radius, a pure potential, or a whole-plane stationary extension. All certificate hashes are recorded in verification/admission.json.
