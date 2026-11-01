# Convergence after a fixed angular projection

Status: CONFIRMED after independent theory-part review at 2026-10-31T04:36Z and verifier recheck. Written on 2026-10-31. This result concerns a projected equation. It does not assert convergence or stationarity for the full IPM equation.

## Statement and notation

Fix a real parameter 0 < delta < 1, put c = 1/(1-delta), d = c-1, and let L be a positive odd integer. Set M = L+1. Let Pi_L be the Fourier projection onto the real span of sin(theta), sin(3 theta), ..., sin(L theta). Fix a nonzero f_1 in this space. For n >= 1 put p_n = 1-n delta and P_n = 2-n delta. The density and stream terms are r^(p_n) F_n(t,theta) and r^(P_n) G_n(t,theta), with t = log r.

Define F_1 = f_1. At every order solve the exact angular Poisson equation

    [-(partial_theta)^2 - (P_n + partial_t)^2] G_n
      = [(p_n + partial_t) cos(theta) - sin(theta) partial_theta] F_n.       (1)

The cosine multiplication in (1) acts after the t derivative. All stream functions are sums of even sine modes of frequency at most M. At an exact resonance, the polynomial solution is normalized by setting the constant coefficient of its resonant stream mode equal to zero. Define the higher density polynomials by

    [(n-1)d - c partial_t] F_n = Pi_L S_n,                              (2)
    S_n = sum_(i+j=n) [(P_i+partial_t)G_i partial_theta F_j
                       - partial_theta G_i (p_j+partial_t)F_j].

Then this recursion is uniquely defined at every order. There are constants C,A,T > 0, depending only on delta, L and f_1, such that

    deg_t F_n <= n-1,       deg_t G_n <= n,
    ||F_n||_T <= C A^(n-1), ||G_n||_T <= C A^(n-1) C_P/n,               (3)

where ||H||_T = sum_q T^q ||[t^q]H||_A0 and A0 is the Fourier Wiener norm. The density and stream series converge absolutely and uniformly with their respective leading radial weights on some r >= R, as do all appropriately weighted spatial derivatives.

If delta is irrational, every coefficient is constant in t and the two ordinary series in z = r^(-delta) have positive radii of convergence. This holds for every irrational delta, including Liouville parameters. If delta is rational, the canonical polynomial-log series still converges on some exterior region.

The sum satisfies the exact Poisson relation and the angularly projected stationary density equation. It generally has a nonzero unprojected stationary residual.

## 1. Existence and degrees

The right side of (1) contains only even sine modes through M. At such a mode m >= 2 the scalar polynomial operator is

    m^2 - (P_n + partial_t)^2.

When P_n != +/-m, its inverse on polynomials is a finite derivative series and preserves degree. When P_n = +/-m, one factor is a nonzero constant plus a derivative and the other is a derivative. Integrating once gives a polynomial solution with at most one additional degree; the prescribed constant fixes its unique ambiguity. Since P_n < 2 and m >= 2, only P_n = -m can resonate. This requires n delta = m+2 <= M+2. In particular there are only finitely many resonant orders under the fixed projection.

The operator on the left of (2) has nonzero constant term and a finite inverse on polynomials, preserving degree. Inductively, deg F_i <= i-1 and deg G_i <= i. Thus each product in S_n has degree at most i+j-1 = n-1. This proves the degree bounds and existence at every order. At n=1 the Poisson inverse is nonresonant and G_1 is constant. Irrational delta precludes every resonance, so induction then gives degree zero throughout.

## 2. Uniform inverse estimates

Take T >= 16/delta. The norm ||.||_T is submultiplicative, Pi_L has norm at most one, and partial_t on polynomials of degree at most k has norm at most k/T. On a Fourier band through m, partial_theta has norm at most m.

Let N_* = ceil(4(M+2)/delta). For n >= N_* and every stream frequency 2 <= m <= M,

    |m +/- P_n| >= n delta - 2 - M >= 3n delta/4.

On input polynomials of degree at most n-1 each linear factor in the Poisson operator has inverse norm at most 2/(n delta), by its finite geometric inverse and the derivative bound n/T <= n delta/16. The two factors commute. Also the right side of (1) has norm at most

    (n delta + 1 + n/T + L) ||F_n||_T <= 2n delta ||F_n||_T.

It follows that

    ||G_n||_T <= 8/(n delta) ||F_n||_T,               n >= N_*.          (4)

For each of the finitely many smaller n, let C_n be the operator norm of the canonical map (1), from the density band through L with log degree at most n-1 to the stream band through M with log degree at most n. These are finite-dimensional linear maps; their existence was just proved, including at a resonance. Define

    C_P = max(8/delta, max_(1<=n<N_*) n C_n).

This is a finite positive constant, and (4) holds at every n with 8/delta replaced by C_P.

On polynomials of degree at most n-1, the inverse in (2) has norm at most

    1/[(n-1)(d-c/T)] <= 2/[(n-1)d],                                  (5)

because c/d = 1/delta and T >= 16/delta.

## 3. Catalan majorant

Put a = 2+delta+1/T and X_n = ||F_n||_T. The degree bounds give

    ||(P_i+partial_t)G_i||_T <= ai ||G_i||_T,
    ||(p_j+partial_t)F_j||_T <= aj ||F_j||_T.

Both angular derivative bounds are at most M. Equations (2) and (5), n/(n-1) <= 2, and the bound for G_i yield

    X_n <= K_0 sum_(i+j=n) X_i X_j/i
        <= K_0 sum_(i+j=n) X_i X_j,
    K_0 = 4a M C_P/d.                                                  (6)

With F = ||f_1||_A0 > 0, the scalar Catalan recursion gives

    X_n <= F^n K_0^(n-1) Catalan_(n-1)
         <= F(4K_0 F)^(n-1).                                         (7)

Thus (3) holds with C = F and A = 4K_0 F. No Diophantine estimate entered the proof. The constants may deteriorate without bound when L tends to infinity.

## 4. Convergence in the exterior variable

For any polynomial H of degree k and t >= 0,

    ||H(t)||_A0 <= max(1,t/T)^k ||H||_T.

Choose R >= exp(T) so large that q_R = A R^(-delta) log(R)/T < 1. For r >= R set Q(r) = log(r)/T and q(r) = A r^(-delta) Q(r). The function r^(-delta) log r decreases for log r >= T, so q(r) <= q_R. The nth density term, divided by r^gamma with gamma = 1-delta, is bounded by F q_R^(n-1). This proves the claimed weighted uniform convergence of density.

For stream the leading weight is r^(1+gamma), and the bound is

    r^(-n delta+delta) ||G_n(log r)||_A0
       <= C_P F Q(r) q(r)^(n-1)/n.                                   (8)

For n >= 2 the function t^n exp(-delta(n-1)t) decreases on t >= T, since n/t <= n/T < delta(n-1). Therefore the right side of (8) has its maximum at r=R and is at most C_P F Q(R) q_R^(n-1)/n. The first stream term is constant after its leading weight is factored out. This proves the stream assertion without incorrectly treating Q(r) as uniformly bounded.

Each application of r partial_r or partial_theta costs at most a fixed constant times n in the polynomial norm, using the radial exponents, the fixed angular bandwidth, and the derivative estimate. Cartesian derivatives of order k are r^(-k) times finite combinations of these operators with bounded smooth trigonometric coefficients. For fixed k the preceding tail estimates acquire only a factor bounded by C_k n^k. Their geometric sums still converge. The same monotonicity in t proves uniformity on r >= R. Thus every weighted spatial derivative converges, and termwise differentiation and multiplication justify the projected stationary equation and the exact Poisson equation.

For irrational delta the log degrees vanish, so already A R^(-delta) < 1 suffices; equivalently the weighted z-series are analytic on |z| < 1/A.

## 5. Why the projection cannot certify the full series

At a finite order, full Fourier recursion starting with sin(theta) has density bandwidth at most 2n-1 and stream bandwidth at most 2n. Hence its first n coefficients agree with those of the projected recursion once L >= 2n-1. Nevertheless, the confirmed universal divergent parameter class of topics46 and49 contains irrational delta for which the full sin(theta) series has radius zero. At each of these parameters every fixed L projection has a positive radius by the theorem above.

There can therefore be no family of the weighted projected solutions that is uniformly bounded on a common positive complex z disk for all L: Cauchy's coefficient estimate and coefficientwise agreement would give a positive radius for the full series. This does not assert that the individual radii themselves tend to zero. Bounds as well as radii matter.

The team's sparse computations let the supported angular band grow with n. The warning here applies to a different approximation that holds the angular band fixed.

## Dependencies and scope

Sections1-4 use only the independently derived polynomial-log Poisson and stationary equations and elementary finite-dimensional norm estimates. Section5 additionally uses the confirmed divergence theorem for sin(theta). The local projected theorem is not a theorem about canonical whole-plane stationary solutions, and it does not settle convergence of the rational logarithmic series without angular projection.

Independent finite checks and source snapshots are stored in verification/ and sources/ alongside this proof. Their role is to verify signs, projection placement, resonant normalization and the fact that the discarded residual is generally nonzero; finite tests are not the proof of convergence.
