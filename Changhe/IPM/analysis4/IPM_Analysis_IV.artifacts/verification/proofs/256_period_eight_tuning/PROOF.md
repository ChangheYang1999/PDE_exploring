# Ten convergent tuned profiles at delta=1/4

Status: PROVED in V530 and V531 after exact algebra, ten independent response/box replays and the theory part review of18:35Z.

## Statement and normalization

Set delta=1/4, c=4/3, p_n=1-n/4 and P_n=2-n/4. Let f_1(theta)=epsilon(sin(theta)+b sin(3theta)), with real epsilon nonzero. Numerical response bounds and boxes are at epsilon=1 and general responses scale by epsilon^8. Let P16 be the primitive integer polynomial with positive leading coefficient proportional to the sin(theta) coefficient of f_16 in the fixed recurrence. Its ten simple real roots each give a uniquely tuned convergent exterior density and stream series and a convergent common potential. No whole-plane extension is claimed.

## Independent finite recurrence

Sum every ordered Cartesian product Xg_i Yf_(n-i)-Yg_i Xf_(n-i) and multiply by3/(n-1). For the stream, divide Xf_n at frequency m by m^2-P_n^2 and verify the Poisson identity. At n=8 the possible resonant sine mode is zero, so all coefficients through f_16 and g_15 are fixed. The first compatibility is the sin(theta) coefficient of f_16. An independent rational Sturm chain must isolate all real roots. Degree-preserving squarefree modular factorizations with independently checked irreducible factors can prove irreducibility by exclusion of every proper factor degree.

## Infinite response and majorant

For k>=2 the free stream mode at order8k is sin((2k-2)theta), and sigma_k is its effect on the sin((2k-1)theta) coefficient of f_(8(k+1)). The affine formula depends only on f_1 through f_8 and g_1 through g_7. With bandwidth B=4, the compact formula applies for2k-2>=32, hence k>=17. The integer tail lies in t in[0,1/32]. Finite direct responses and a complete directed Taylor/singleton cover must produce a positive uniform bound at each root, followed by independent higher-precision replay.

For the prefix through N=16, the majorant constants are

    L = 3*64/(4*23) = 48/23,
    kappa = 4*(2-1/4+3/4)*3*(17/16) = 255/8.

A verified nonnegative supersolution at w=z^8=r^-2=2^-q gives the sufficient exterior R>2^(q/2)|epsilon|^4. Every component of the exact map and every scalar recurrence identity must be independently reconstructed. The initial free harmonic at order8 is zero by sine symmetry. Potential reconstruction permits logarithms only at orders8 and16; neither logarithmic coefficient is asserted nonzero by this argument. The nonzero odd leading profile guarantees a sign-changing density on a sufficiently large exterior.

Dependencies:01,131,132,144,149,172,175,232,234.

## Completed certificates

All ten roots pass the768-bit constructor and 1024-bit replay with independent coverage and exact-prefix checks, sharing the audited Taylor enclosure routine. Every replay checks1,566 signed exact-prefix coefficients,23 finite responses,8 full/compact comparisons, a complete partition and48 scalar identities. The resulting sufficient bounds are R>2^(q/2)|epsilon|^4:

| Increasing root | Unit response lower bound | q | Radius exponent |
|---|---:|---:|---:|
| 1 | 4096 | 114 | 57 |
| 2 | 1/64 | 120 | 60 |
| 3 | 1/536870912 | 141 | 141/2 |
| 4 | 1/16384 | 127 | 127/2 |
| 5 | 1/16384 | 127 | 127/2 |
| 6 | 1/4096 | 126 | 63 |
| 7 | 1/2048 | 125 | 125/2 |
| 8 | 1/1024 | 125 | 125/2 |
| 9 | 1/16 | 121 | 121/2 |
| 10 | 16 | 116 | 58 |

The common sufficient exponent is141/2. The small finite response near k=10 at the third root is included explicitly in its bound. The exact polynomial and root certificates are recorded in V530. Admission hashes are retained in verification/admission.json.
