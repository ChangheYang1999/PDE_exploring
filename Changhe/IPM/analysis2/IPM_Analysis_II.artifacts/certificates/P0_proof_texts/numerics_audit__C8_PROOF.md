# Independent annular audit of the numerics C8 certificate

Status: CONFIRMED after independent exact reconstruction and256-bit arithmetic. The principal lower bounds are confirmed. Producer endpoint diagnostics are audited separately from its published downward bounds.

## Statement and exact test

Let F be the residual of the exact accepted state131, reconstructed from the read-only checkpoint, and let w(r)=(1+r^2/2^70)^(-11/10). Write L(F)=||wF||_(dot H^-1). For T>0 use

    phi_T(r,theta)=cos^2(pi log(r/T)/(2 log2)) sin(theta),

on T/2<=r<=2T, extended by zero. This centrally odd compact C1 function belongs to dot H1. Duality gives L(F)>=|<wF,phi_T>|/||Dphi_T||2. With l=log2, direct integration of sine and cosine squares gives the exact identity

    ||Dphi_T||2^2=(pi/4)(pi^2/l+3l).

Indeed the radial logarithmic derivative contributes pi^2/(4l) and the angular derivative contributes3l/4 before multiplication by pi. The norm is independent of T.

## Exact sector reconstruction and remainder

The script independently reconstructs all860 rational canonical coefficients from the binary hexadecimal checkpoint coordinates and the stored frozen Legendre normalizations. It expands each potential branch to binomial orderQ=3, differentiates its angular polynomial and forms the linear and quadratic residual sectors. It retains only sectors with descendant indexq<=3. No code or exact sector file produced by the numerical work is imported.

Let gamma=1/c, delta=1-gamma and qlead=2gamma-1. For a canonical generator indexed(j,m,k), the radial parameter is p_j-k, where p_j=(3+gamma-jdelta)/2. The source verification gives |p_j-k|<26 and every angular derivative factor in orders3 and4 is bounded by2a+32 at binomial ordera. Hence

    |binom(p_j-k,a)| <= binom(a+25,a).

For derivative orderd=3 or4, the omitted series afterQ is bounded by the first majorant at a=Q+1 times a geometric sum. Its term ratio is at most

    ((a+26)/(a+1))((2a+34)/(2a+32))^d R0^-2,

which decreases with a. All normalized exponents are negative for r>=R0. Let T3,T4 be these normalized tail bounds and M3,M4 the corresponding finite-series derivative bounds, so that |D^d chi_tail|<=Td r^(3+gamma-d). Componentwise differentiation then gives

    |F-F_fullQ|/r^qlead
      <=(2sqrt(2)c T4+2T3)R0^delta
        +4(T3M4+M3T4+T3T4).

The R0^delta factor is valid because each omitted term also contains r^-2a and a>=4. The discarded quadratic sectors with q>3 contribute the sum of their exact angular coefficient absolute values times R0^(alpha-qlead). Adding this finite contribution defines Ctail and proves |F-F_Q|<=Ctail r^qlead uniformly for r>=R0. The proof is the same direct component argument as in the independently checked topic17 annular certificate; it does not rely on asymptotic sampling.

## Pairing and rigorous integration

Let e_(h,q),1 be the exact sin(theta) coefficient of the retained sector and alpha=gamma-hdelta-2q. Set u=log2(r/T), so u ranges from-1 to1. Angular orthogonality gives

    <wF_Q,phi_T>
      =pi log2 int_(-1)^1 w(T2^u) cos^2(pi u/2)
         sum_(h,q) e_(h,q),1 (T2^u)^(alpha+2) du.

The omitted contribution has absolute value at most

    4 Ctail log2 int_(-1)^1 w(T2^u) cos^2(pi u/2)
                           (T2^u)^(qlead+2) du.

The4 is the exact integral of |sin(theta)| around the circle. The script encloses both integrals using complex ball quadrature at256bits. Its analytic callback uses the checked analytic logarithm for the weight, so boxes crossing a branch cut are not treated as analytic. Every accepted integral is finite and its imaginary part contains zero. Division by the exact enclosed gradient norm yields a rigorous lower bound. Final lower bounds are rounded down to integers, and ball strings preserve uncertainty. Binary64 output alone is not an outward interval certificate.

## Scope

The audit confirms only the stated duality lower bounds for the exact original reference. No upper norm or repaired-reference lower bound follows. It also checks which advertised decimal roundings are supported by this particular test. A rounded-up claimed test value is an error of certification even if a different test proves the true norm larger.

## Verified values and historical rounding audit

The independent lower bounds are

| T | strict lower bound for L(F) | strict lower bound for N_(s,2^35)(F) |
| --- | --- | --- |
| 2^20 | 8254901318 | 130573642877133558 |
| 2^30 | 18730797419875790 | 296278339214129575742327 |
| 2^35 | 11221534985305196289 | 177498996671201117552150089 |

The N comparison uses L(J^-s g)<=6L(g) and the2^(53/2) coefficient, for0<s<=2^-12. All three independently enclosed finite-sector pairings overlap the producer's pairing balls. Our deliberately coarser uniform tail bounds are valid replacements for that calculation; we do not claim to have reproduced its sharper tail constants digit for digit.

In the producer record audited at06:39Z, before the producer rewrote its JSON at06:41:47Z, the exact gradient norm lies in(3.5799916157028380685,3.5799916157028380686). The producer's saved binary64 normDphi_upper happens to be an upper bound: its exact binary value is3.5799916157028381924... . However, its printed decimal is not an outward decimal endpoint. More seriously, all three saved binary64 L_lower numbers exceed the entire independently enclosed range of the corresponding test quotient, due to rounding at conversion. They therefore are not valid lower endpoints of that quotient. This does not disprove these numbers as lower bounds on the full norm, which is much larger by the already verified combined-mode test.

In the textual C8 summary,1.873080e16 is above the2^30 test value1.87307974198757909...e16, and1.775e26 is above its2^35 high-norm comparison1.77498996671201117...e26. Safe downward decimals are1.873079e16 and1.77498e26, or the integer bounds above. The main claims L(F)>1.122153e19 and N(F)>1.77498e26 are confirmed by this test alone. The stronger topic16 and17 combined-mode bounds remain the current results.


## Historical decimal schema and endpoint scope (07:46 audit)

The subsequent audit snapshots the producer bytes once, records their SHA256 and verifies that the producer file has not changed before completion. Its current normDphi_ball encloses our independent exact norm. Its L_lower_pub and L_lower_times_2^26.5_over_6_pub fields are downward decimal claims; each is compared directly with our independent lower ball. The field named L_lower_exact_binary contains decimal strings, not binary64 values or outward interval endpoints. It is therefore treated as a separate diagnostic.

At T=2^35 its value11221534985305196289.5884870264 exceeds the upper endpoint of this exact test by about1.596e-11, so it is not a valid lower endpoint of the test. At T=2^30 the stored diagnostic is below the independently proved test lower bound. At T=2^20 our deliberately coarser error interval straddles that diagnostic, so this audit leaves that diagnostic OPEN. These classifications concern the test quotient alone. All six current published downward lower bounds are independently supported. The stronger C9 lower bounds for the full norm remain valid.


## Exact binary schema after the08:04 producer update

The producer replaced its decimal diagnostic by L_lower_exact_binary_man_exp=[m,e], representing the exact rational number m times2^e. The audit reconstructs this rational without any floating-point conversion. The three pairs of published downward claims remain the primary certified results. Each exact binary candidate is additionally compared with this independent test enclosure: below the independent lower bound is confirmed, above the independent upper bound is refuted, and an overlap remains open at the finer endpoint level. An open endpoint comparison does not affect the published lower bounds. The producer bytes are snapshotted once, hashed, and required to remain unchanged during the audit. The07:46 findings above apply only to the superseded decimal schema.
