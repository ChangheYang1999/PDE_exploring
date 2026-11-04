# The critical weighted vorticity energy criterion

## 1. Exact theorem and energy dependency

Let 2/5<c<1 and omega be any finite real number. Let U in C1(R3;R3), P in C1(R3) solve

    (1-c)U+[(cI-omega J)y+U].grad U+omega JU+grad P=0,
    div U=0, Jx=e3 cross x.

Assume Hb: U is bounded and U(R.) tends to zero in distributions on R3 as R tends to infinity. Put W=curl U, alpha=5-2/c and m0=alpha-2=3-2/c. If

    integral <y>^(-m0)|W|² dy < infinity,

then U=0 and P is constant. The same conclusion holds with any weight exponent m<=m0. No global bound on W or DU is assumed. Here <y>=(1+|y|²)^(1/2).

The precise energy input is A040/A052: at this C1 regularity and under Hb, E(R)=integral_(B_R)|U|² has R^(-alpha)E(R)->L>=0, with L>0 unless U=0. Its source Sections0-5, including its pressure representation, flux estimate and positivity iteration, were freshly read. Its canonical pressure is a consequence of the full equation and Hb, not an added normalization in this theorem. We use this established dependency only after proving a strictly smaller energy rate.

## 2. An absolute Biot-Savart integral

For locally bounded f with K=integral<z>^(-m)|f|²<infinity and m<1, set

    BS(f)(y)=(4pi)^(-1) integral f(z) cross(y-z)/|y-z|³ dz.

This integral is absolutely convergent at every y. Near y the kernel |y-z|^(-2) is locally integrable and f is bounded. Away from y Cauchy-Schwarz leaves integral<z>^m|y-z|^(-4), which is finite at infinity exactly when m<1.

Write A0=B1, Ak={2^(k-1)<=|z|<2^k} for k>=1, fk=f1_Ak and Nk=||fk||2. Absolute convergence permits summing the corresponding integrals. Let C1=sqrt(35/3), C2=16/3. Then

    ||BS(fk)||_(L2(R3))<=C1 2^k Nk,
    ||BS(fk)||_(L2(B_R))<=C2 R^(3/2)2^(-k/2)Nk
                  if R>=1 and 2^(k-2)>=R.

For the first bound, inside B_(2^(k+1)) Young's inequality uses the truncated kernel on B_(3 times2^k), whose norm after the factor1/(4pi) is3 times2^k. Outside, |y-z|>=|y|/2 gives squared norm at most(8/3)4^k Nk². Adding the disjoint contributions gives35/3. For the second bound use |y-z|>=2^(k-2), |Ak|<=(4pi/3)8^k and |B_R|=(4pi/3)R³. These yield exactly16/3. Minkowski then gives

    ||BS(f)||_(L2(B_R))
      <=C1 sum_(2^k<4R) 2^k Nk
          +C2 R^(3/2) sum_(2^k>=4R) 2^(-k/2) Nk.       (1)

The convergent majorants below justify the norm of the infinite sum.

## 3. The endpoint little-o bound

Suppose additionally -2<m<1. Let Kk=integral_Ak<z>^(-m)|f|². Then sum Kk=K and Nk<=2^(|m|/2)2^(km/2)sqrt(Kk). Put s=(m+2)/2>0 and t=(1-m)/2>0. Divide(1) by R^s. Apart from the fixed factor2^(|m|/2), the two sums become

    C1 sum_(2^k<4R)(2^k/R)^s sqrt(Kk),
    C2 sum_(2^k>=4R)(R/2^k)^t sqrt(Kk).

Since Kk->0, choose a fixed index beyond which sqrt(Kk)<=epsilon. The two geometric sums on this tail are bounded by

    epsilon[C1 4^s/(1-2^(-s))+C2 4^(-t)/(1-2^(-t))].

The finitely many earlier terms are O(R^(-s)). Let R tend to infinity and then epsilon to zero. Thus

    integral_(B_R)|BS(f)|²=o(R^(m+2)).                (2)

Both strict endpoint restrictions on m have been used. The campaign's m0 lies in(-2,1), so this applies at the critical weight without loss.

## 4. Removing the harmonic remainder directly from Hb

For compactly supported C1 vector F, the Helmholtz identity is

    F=BS(curl F)+Q(div F),
    Q(g)(y)=(4pi)^(-1) integral g(z)(y-z)/|y-z|³ dz.

Indeed BS=curl(Gamma*f), Q=-grad(Gamma*g), Gamma=1/(4pi|x|), and -Delta F=curl curl F-grad div F. Mollification extends the C2 identity to C1 with uniformly convergent compact-support integrals.

Apply it to F_N=chi(y/N)U(y), where chi is smooth, equals1 on B1 and is supported in B2. At each fixed y and large N,

    U(y)=BS(chi_N W)(y)+BS(grad chi_N cross U)(y)
                                  +Q(grad chi_N.U)(y).

The first term tends to BS(W) by Section2. In the remaining terms set z=Nx. Kernel homogeneity exactly cancels the factors N^(-1), N³ and N^(-2). On the fixed annulus supporting grad chi, replace (y/N-x)/|y/N-x|³ by -x/|x|³. The error is bounded by C||U||infinity |y|/N, because the kernel derivative is uniformly bounded on the intervening segments. Each remaining integral is U_j(Nx) paired with one fixed smooth compactly supported test function. Hb sends it to zero. Therefore U=BS(W) everywhere. This argument uses no boundedness of DU and no unjustified limit of an arbitrary harmonic function.

## 5. Liouville conclusion and pointwise consequences

If the vorticity hypothesis holds with m<=m0, it also holds at m0 because <y>^(-m0)<=<y>^(-m). Sections3-4 give E(R)=o(R^(m0+2))=o(R^alpha). The positive-energy dependency forces U=0, and the full equation then gives grad P=0.

In particular, a bound |W|<=C<y>^(-gamma), gamma>1/c, suffices: the radial integrability exponent is m0+2gamma>3. The critical logarithmic improvement

    |W(y)|<=C|y|^(-1/c)(log|y|)^(-beta), |y|>=2,
    beta>1/2,

also suffices because the remaining radial integral is bounded by a constant times integral_2^infinity dr/[r(log r)^(2beta)]. Smoothness controls the inner ball. These are sufficient conditions only; no statement at beta=1/2 is derived.

## 6. Exact quantitative subsequence

Let U be nonzero under Section1's profile and Hb hypotheses, without assuming weighted integrability. Let L>0 be its energy constant and set

    bk=2^(-k(alpha-2)/2)||W||_(L2(Ak)),
    C4=C1 4^(alpha/2)/(1-2^(-alpha/2))
                   +C2 4^(-(3-alpha)/2)/(1-2^(-(3-alpha)/2)).

If limsup bk is infinite the desired bound is immediate. Otherwise each eventual bound bk<=beta makes the vorticity integral finite at every m in(alpha-2,1), by a convergent geometric series. Section4 then gives U=BS(W), and(1) yields

    E(R)^(1/2)<=C3+C4 beta R^(alpha/2).

Consequently sqrt(L)<=C4 beta. Decrease beta to limsup bk to obtain

    limsup bk²>=L/C4².

Infinitely many k have bk²>=L/(2C4²). Using |Ak|<=(4pi/3)8^k gives

    sup_Ak |W|>=sqrt(3L/(8pi)) C4^(-1)2^(-k/c)

on that subsequence. This is a limsup conclusion, not a lower bound on every shell.

## 7. Composition with weighted enstrophy and pointwise limits

Under the additional C2 profile, bounded W and velocity bound |U|<=C<y>^(-a), a>=0, A1429 gives finite weighted W² and DU² integrals for every

    m>max(1-2a,3-(2/c)(1-w_inf/sqrt(3))),
    w_inf=limsup_(|y|->infinity)|W|.

Section5 gives divergence for m<=m0 in every nonzero profile satisfying Hb. If w_inf=0 and a>=1/c-1, the infimum of admissible m is exactly m0 and is not attained. The energy law already excludes a>1/c-1, so only its equality case can remain here. C56 removes a in this composition through the energy bound, checked separately.

These integral statements alone give no pointwise derivative decay. For an explicit functional test, let U0=<y>^(-1/c)Jy and add disjoint smooth divergence-free bumps epsilon r_n phi((y-2^n e1)/r_n), with r_n=2^(-n²) and Dphi(0)!=0. Then Hb holds, the added field is L2, and

    integral_(B_R)|U0|²~[8pi/(3alpha)]R^alpha.

The added cross term is o(R^alpha) by Cauchy-Schwarz. Every weighted derivative integral with m>m0 is finite, but derivatives at the bump centers tend to epsilon Dphi(0)!=0. This is not a profile and refutes only the functional implication that these mass bounds control pointwise values. Uniform continuity of DU, together with DU in L2, would give decay by disjoint fixed-radius balls.

## 8. A correction to the failed-step wording

The source's FS-VL2 says that bk may grow like2^(k epsilon) with epsilon>epsilon0, where its preceding FS-VL1 requires sum2^(-k delta)bk² finite for every delta>epsilon0. Taken as an actual growth assertion this is false: choose epsilon0<delta<2epsilon, and such growth makes the series diverge. The valid statement is that the weighted conclusions permit unbounded sparse spikes or subexponential growth. For example bk=log(k+2) satisfies the weighted summability for every delta>0 while remaining unbounded. This repairs the failed-step explanation without changing any theorem or constant in Sections1-7.

## 9. Evidence and remaining scope

All submitted sections were read, and the stated constants, cutoff remainder and endpoint limits were reconstructed directly. The original check log was not treated as proof and no computation was rerun. The literature paragraph in the submission explicitly remains unverified there; no novelty or theorem-number claim from it is endorsed by this audit. All mathematical conclusions above retain the full profile equation and Hb where indicated. No helicity or symmetry is required, and omega cancels from the energy and norm calculations. The unrestricted decay-only conjecture remains open. Existing configured model comparison is requested, with provider runtime unattested and no new model client or formal build.
