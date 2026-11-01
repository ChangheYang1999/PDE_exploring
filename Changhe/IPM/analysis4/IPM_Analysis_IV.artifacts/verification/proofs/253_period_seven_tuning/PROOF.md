# Ten candidate tuned profiles at delta=2/7

Status: PROVED. V526 confirms the complete algebraic prefix and ten roots. V527 admits all ten complete response covers, exact boxes and independent1024-bit replays, following the theory part's18:23Z specialization review.

## Statement and normalization

Set delta=2/7, c=7/5, p_n=1-2n/7 and P_n=2-2n/7. Let f_1(theta)=epsilon(sin(theta)+b sin(3theta)), with real epsilon nonzero. All numerical response bounds and boxes use epsilon=1; responses for general amplitude scale by epsilon^7. Define P14 as the primitive integer polynomial with positive leading coefficient proportional to the sin(theta) coefficient of f_14 from the fixed recurrence. The polynomial P14 has ten simple real roots, and each root determines a uniquely tuned convergent exterior density, stream and common-potential series. Quantitative sufficient radii require separate exact boxes. No whole-plane extension is asserted.

## Independent recurrence and first compatibility

Use the signed Laurent Cartesian derivatives of01. At each n>=2, sum every ordered product Xg_i Yf_(n-i)-Yg_i Xf_(n-i), and multiply by5/[2(n-1)]. For each stream coefficient at frequency m divide Xf_n by m^2-P_n^2, checking the Poisson identity exactly. The zero-frequency resonance at n=7 has no sine coefficient. Thus all coefficients through f_14 and g_13 are fixed without a free stream harmonic. The first compatibility is the sin(theta) coefficient of f_14.

An exact rational Sturm chain proves the number and isolation of real roots. Optional modular irreducibility certificates preserve the degree, verify each finite-field factor by Frobenius and gcd tests, and intersect possible rational-factor degrees. They corroborate the algebraic structure but are not needed if every root has its own complete response cover.

## Full response and infinite tail

For k>=2, the free stream mode at order7k is sin((2k-2)theta). Its response sigma_k is the coefficient of sin((2k-1)theta) in the density at order7(k+1). The affine-response formula144 depends only on f_1,...,f_7 and g_1,...,g_6 and is independently implemented by Cartesian differentiation. The compact identity149 applies when2k-2>=4*7, hence k>=15. Direct responses cover2<=k<=14. The compact samples for k>=15 lie in[0,1/28].

A finite dyadic partition with directed Taylor bounds, singleton checks and integer exclusions, as in232 and234, must establish one s_i>0 for every root. Every finite response, leaf and root enclosure is to be replayed at higher precision. Finite samples or a nonzero limit alone do not imply this statement.

## Majorant and reconstruction

At each certified root, compute a directed prefix through N=14, setting the exact first compatibility coefficient to zero only after the root identity has been proved. The initial free harmonic at order7 is zero by sine symmetry. For the prefix majorant172 and175 use

    L=3*7^2/[4(3*7-1)]=147/80,
    kappa=4*(2-2/7+5/7)*(5/2)*(15/14)=1275/49.

A nonnegative exact supersolution at w=z^7=r^-2=2^-q_i proves a sufficient exterior R>2^(q_i/2)|epsilon|^(7/2). The exact map and every component inequality must be reconstructed independently, including scalar recurrence comparisons. Strict exterior margin absorbs derivative factors. The common potential follows from132, with only the finite exceptional logarithms allowed at orders7 and14; this does not force either logarithmic coefficient to be nonzero. The leading density changes sign because it is a nonzero odd trigonometric polynomial.

Dependencies:01,131,132,144,149,172,175,232,234.

## Completed finite algebraic audit

V526 proves that P14 is irreducible of degree14 and has exactly ten simple real roots. The exact obstruction and its normalization agree between the independent Cartesian and polar recurrences. The rational Sturm variations are12 and2 at the two infinities. The modular factor-degree intersections become empty at primes29,43,67, with all finite-field factor certificates replayed independently.

The ten roots in increasing order are approximately -0.6736263357624939, -0.05670761975848361, 0.01505351502811877, 0.03055360415736273, 0.06593298065118259, 0.1007255318291284, 0.1356654310578601, 0.1797781928116298, 0.2517896667205710, 0.4751674513195204. The proof inputs are the exact rational intervals in verification/obstruction_checks.json, each narrower than10^-60. The complete response certificates and exact boxes are admitted separately below.

## Admitted sufficient exteriors

For each root in increasing order the complete response cover and fresh exact box are replayed independently. Each replay compares1202 signed coefficients with the exact polynomial prefix, recomputes21 finite responses, checks8 full/compact comparisons, covers every remaining integer index, verifies all42 scalar recurrence identities and reconstructs every exact box inequality.

| Root | Unit response lower bound s | Box exponent q | Sufficient radius exponent q/2 | Taylor leaves | Singleton leaves |
|---:|---:|---:|---:|---:|---:|
| 1 | 256 | 95 | 95/2 | 1 | 0 |
| 2 | 1/512 | 101 | 101/2 | 1 | 0 |
| 3 | 1/4194304 | 113 | 113/2 | 2 | 6 |
| 4 | 1/131072 | 109 | 109/2 | 1 | 0 |
| 5 | 1/32768 | 107 | 107/2 | 1 | 0 |
| 6 | 1/16384 | 107 | 107/2 | 1 | 0 |
| 7 | 1/4096 | 106 | 53 | 2 | 0 |
| 8 | 1/1024 | 104 | 52 | 2 | 0 |
| 9 | 1/8192 | 109 | 109/2 | 2 | 0 |
| 10 | 1 | 99 | 99/2 | 2 | 0 |

Thus R>2^(113/2)|epsilon|^(7/2) is a common sufficient exterior for all ten profiles. The unit-amplitude bounds scale by |epsilon|^7. The response bounds and radii are sufficient, and no optimality is asserted. Exact inputs, partitions, boxes and replay hashes are recorded separately for each root.
