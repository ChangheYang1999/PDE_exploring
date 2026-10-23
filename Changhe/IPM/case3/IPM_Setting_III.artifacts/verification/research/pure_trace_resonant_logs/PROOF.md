# Pure first-mode trace: exact resonance test and conditional forced logarithms

Written 2026-10-21, verifier result 150. Status after exact arithmetic: the two recurrences agree at every computed degree, with 388 exact checks passing. Both resonant coefficients are nonzero. Actual Opus 5.5 lead hand review at05:32 confirmed the argument and independently recomputed both rational coefficients; its reasoning was rechecked here. External referee audit22 confirmed the formulas with two local wording repairs, applied here after independent rechecking: earlier means smaller deficit, and the first velocity log is already present in (8). Its additional high-mode claim is separate and not yet independently verified here. This is not an existence or nonexistence theorem for the principal problem.

## 1. Statement, hypotheses and notation

Let ell>1, p=1/ell, delta=1-p. Suppose rho and its canonical full-plane velocity U are smooth, have the Setting III parities, lie in S^p, and satisfy

    (ell X+U).grad rho=rho

outside a disc. Here S^p means that for every Cartesian multi-index alpha, |partial^alpha f(X)| <= C_alpha |X|^(p-|alpha|) for |X|>=1. Suppose the uniform angular trace is

    r^(-p) rho(r,theta) -> A sin(theta),   A!=0.

The expansion theorem in ../smooth_angular_far_field/PROOF.md supplies, at every finite depth, unique collected power-log expansions of the density and velocity, with S^b remainders for noncritical thresholds b. These are finite asymptotic expansions, not convergent infinite series. The present result is conditional on those explicit hypotheses and that proved theorem. No assumption about analyticity at infinity is made.

We test two cases: ell=3 and ell=5/2. In the first case set (k_*,m_*)=(5,2); in the second set (k_*,m_*)=(9,4). Here m denotes the positive even stream frequency, equal to twice the stream-mode index in the lead report. Define s_k=p-k delta. The finite recurrence (1)-(4) below uniquely determines real sine polynomials P_0,...,P_(k_*) and the coefficient

    g_*=[sin(m_* theta)] partial_x[r^(s_(k_*)) P_(k_*)(theta)] / r^(s_(k_*)-1).

Its amplitude is A^(k_*+1). The coefficients are nonzero, as evaluated below, and the actual canonical stream necessarily contains

    (g_*/(2m_*)) r^(-m_*) log(r) sin(m_* theta).              (L1)

The actual density then necessarily contains the nonzero logarithmic coefficient

    -A g_*/[4 ell (m_*+2)] r^(p-m_*-2) log(r)
       *[delta sin((m_*-1)theta)+(1+p)sin((m_*+1)theta)].      (L2)

In each case these are its first possible logarithmic stream and density terms. Their coefficients are unaffected by any globally determined constant harmonic multipole coefficients. Verifying g_*!=0 is a finite exact calculation; the verification directory records two independent implementations and all intermediate rational coefficients. The exact check gives

    ell=3:   g_* = -(177047/301056000000) A^6,

    ell=5/2: g_* = [26243642326438735772269905591088207
                   /4898218301752285282303033607434666157015040] A^10.

These nonzero rational numbers, combined with the proved recurrence, establish the two assertions. Every intermediate rational coefficient is recorded in verification/EXACT_CHECKS.json, so the arithmetic does not depend on a decimal comparison or an approximate cancellation threshold.

## 2. Derivation of the pure cascade

Put P_0=A sin(theta). At a pure deficit k delta write the density term as r^(s_k) P_k(theta). Before the first resonance the sine polynomials and stream coefficients obey the following recurrence. For a single odd positive frequency n,

    partial_x[r^s sin(n theta)] = r^(s-1)
       *[(s-n)/2 sin((n+1)theta)+(s+n)/2 sin((n-1)theta)].     (1)

For each k, let G_k be the even sine polynomial obtained by this formula from P_k. If no positive even m obeys m^2=(s_k+1)^2, set

    H_(k,m)=G_(k,m)/[m^2-(s_k+1)^2].                         (2)

Thus the particular stream is r^(s_k+1) sum_m H_(k,m) sin(m theta). In polar coordinates U_r=-(1/r)partial_theta psi and U_theta=partial_r psi. For one stream mode m and one density mode n, the advection coefficient with degrees s_i,s_j is

    H_(i,m) P_(j,n) r^(s_i+s_j-1)
    *{[-m s_j+(s_i+1)n]/2 sin((n+m)theta)
       +[-m s_j-(s_i+1)n]/2 sin((n-m)theta)}.                (3)

The convention is sin(-n theta)=-sin(n theta) and sin(0 theta)=0. The linear transport operator ell r partial_r-1 acts on r^(s_k) P_k as -ell k delta r^(s_k) P_k. Since s_i+s_j-1=s_(i+j+1), the equation yields, for k>=1,

    P_k = (1/(ell k delta)) sum_(i+j=k-1) B(H_i,P_j),        (4)

where B is (3) with its radial power removed. This includes every ordered interaction. All P_k and H_k are homogeneous in A, of degree k+1. Equations (1) and (3) follow directly from Cartesian differentiation expressed in polar coordinates and the elementary product-to-sum identities. Their signs can also be checked from the first correction:

    H_(0,2)=-A/[2(p+3)],
    P_(1,1)=-(3p+1) A^2/[4 ell delta (p+3)],
    P_(1,3)=-A^2/[4 ell (p+3)].                            (5)

For ell=3 this is P_1=-(3A^2/40) sin(theta)-(A^2/40) sin(3theta).

## 3. Why other globally determined sectors cannot change this test

The actual expansion need not consist only of this pure cascade. It also has velocities of degrees -m-1, with positive even m, from the full-plane harmonic multipoles. A density deficit t is changed by an induced interaction to delta+t_1+t_2, and by a harmonic interaction to m+2+t. Every generated density deficit therefore belongs to

    {k delta+2l: k>=0, l=0 or l>=2}.                        (6)

Indeed harmonic costs are 4,6,8,..., and sums of these costs can never be 2. This is a sharper containing set than the set with every l>=0 used for convenience in the general theorem. Induction over the finite-depth expansion proves (6); no assertion that every listed degree occurs is required.

For ell=3, delta=2/3. Resonant density degrees are s=-m-1, so their deficits are p+m+1=m+4/3. The first possible one is m=2, deficit 10/3, achieved by pure k=5. A nonpure deficit is at least4 and therefore cannot coincide. There is no smaller resonant deficit.

For ell=5/2, delta=3/5. The first candidate m=2 would need deficit17/5, which is not a multiple of3/5 and is below4. Thus it is absent. The next candidate m=4 needs deficit27/5. A coincidence k(3/5)+2l=27/5 requires 3k+10l=27. For l=0 the solution is k=9; for l=2 there is no integral k, and l>=3 makes k negative. Thus this resonant coefficient is also pure and is not affected by any harmonic sector. There were no earlier resonances, hence no earlier logarithms.

For ell=3, the recurrence through k=5 only needs streams through k=4; their denominators in (2) are nonzero. For ell=5/2 it only needs streams through k=8, also nonresonant. The singular denominator at k=k_* is never divided by: its numerator is the quantity being tested. In both cases P_(k_*) is therefore fixed solely by A and ell through (4).

This also proves that all terms of smaller deficit used to calculate this particular pure coefficient are given by (1)-(4). A term from a harmonic sector cannot first enter and then disappear from its deficit: all additional deficits in the recursion are positive. The explicit arithmetic above rules out an overlap at the target degree. Potential coincidences at other degrees must be collected, but they do not alter this target coefficient.

## 4. Resonant inversion and the next density logarithm

At s=-m-1 the resonant stream exponent is -m. For Q(z)=q z, z=log r, direct differentiation gives

    -Delta[r^(-m) Q(log r) sin(m theta)]
        =2m q r^(-m-2) sin(m theta).                       (7)

Consequently a source g r^(-m-2) sin(m theta) forces q=g/(2m), which proves (L1). The canonical stream may also have a constant multiple of r^(-m) sin(m theta). Such a harmonic term cannot cancel a logarithmic coefficient. The cutoff comparison and canonical uniqueness in the cited expansion theorem prove that this formal resonant inverse is the corresponding term of the actual full-plane inverse. We are not imposing a boundary value on a finite circle.

The highest-log part of the velocity from (L1) has the same coefficient as the velocity of r^(-m) sin(m theta), multiplied by (g/(2m))log r. Thus

    (U_r)_log = -(g/2) r^(-m-1) cos(m theta) log r,
    (U_theta)_log = -(g/2) r^(-m-1) sin(m theta) log r.      (8)

Its action on A r^p sin(theta), using product-to-sum, has highest-log coefficient

    -(A g/4) r^(p-m-2)
      *[delta sin((m-1)theta)+(1+p)sin((m+1)theta)].         (9)

There are no earlier density logarithms, and the first velocity logarithm is the one in (8), so (9) is the entire forcing at this first density log degree. Terms acting on a lower density degree are strictly lower. Constant harmonic coefficients can contribute logfree terms at the same density degree but cannot affect (9).

At a density degree t=p-m-2, the highest-log part of ell r partial_r-1 is ell(t-p)=-ell(m+2). The transport equation consequently divides the forcing (9) by ell(m+2), proving (L2). Differentiating the logarithm in the linear term affects only the logfree coefficient. A density-induced velocity of this same degree acting on the leading density has a strictly lower degree t-delta, so no same-order implicit term was omitted.

For ell=3, m=2, (L2) reads

    r^(-11/3) log r *[-A g_*/72 sin(theta)-A g_*/36 sin(3theta)].

For ell=5/2, m=4, it reads

    r^(-28/5) log r *[-A g_*/100 sin(3theta)-7A g_*/300 sin(5theta)].

Because A!=0 and delta>0, these are nonzero whenever g_*!=0. Their radial degrees agree with the next pure cascade degrees s_6 and s_10 respectively. At that order, harmonic interactions of cost m+2 also occur, but remain logfree and so cannot cancel the displayed log.

## 5. Independent exact arithmetic verification protocol

One implementation uses positive real sine coefficients and (1)-(4). A separately written implementation uses signed Laurent Fourier coefficients and Cartesian derivatives, with no trigonometric product-to-sum evaluation. Write a real odd sine polynomial as i sum_n D_n exp(i n theta), where D_n are real rationals and D_(-n)=-D_n; sin(n theta) corresponds to D_n=-1/2, D_(-n)=1/2.

Define real coefficient shift operators X_q,Y_q by

    X_q: n -> n+1 with (q-n)/2; n -> n-1 with (q+n)/2,
    Y_q: n -> n+1 with (n-q)/2; n -> n-1 with (n+q)/2.

These represent partial_x(r^q F)=r^(q-1) X_q F and partial_y(r^q F)=i r^(q-1) Y_q F. For stream i S and density i D, the nonlinear coefficient after removing the common i is

    Y_(s_i+1) S_i * X_(s_j) D_j
       - X_(s_i+1) S_i * Y_(s_j) D_j,                    (10)

where * is ordinary Laurent convolution. This directly represents (-psi_y)rho_x+psi_x rho_y. Divide (10) by ell k delta to compute the second recurrence. Compare every density and stream coefficient at every depth with the real sine implementation. Separately check each source against the Cartesian negative Laplacian and (7), and compare the first-log forcing with (L2). Use exact fractions with A=1; homogeneity restores every nonzero real A. No floating-point nonvanishing criterion is allowed.

The tests verify finite identities and provide reproducible arithmetic evidence for g_*. They do not replace the asymptotic theorem, do not prove convergence of an infinite series, and do not construct a solution.

## 6. Scope and open steps

A forced far-field logarithm is compatible with C^infinity local smoothness on the full plane: it is only an exterior asymptotic term. Thus the proved nonzero coefficient test does not exclude an exact smooth Setting III profile. It excludes a wholly logfree asymptotic expansion with this particular pure first-mode trace and ell, under the stated hypotheses. An arbitrary smooth angular trace can change the resonant forcing, and no nonvanishing assertion is made for it.

Finite-basis numerical candidates may have leading traces with many modes. This calculation alone therefore neither rejects such a candidate nor explains its observed center-jet drift. That requires separate coefficient and residual checks. The primary endpoint remains OPEN.
