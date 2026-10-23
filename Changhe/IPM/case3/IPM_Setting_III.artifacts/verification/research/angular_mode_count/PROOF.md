# Diverging angular mode count and approximation with adaptively chosen frequencies

Written 2026-10-21 before supporting checks. Status: complete independently checked informal proof; actual lead Opus5.5 hand review04:39 confirmed the proof with the scope clarification recorded in verification/opus_20261021T0439. This is a necessary condition for the primary IPM class. It is not a full nonexistence theorem.

## 1. Statement, hypotheses and notation

Let rho be an exact primary SettingIII profile on the full plane with ell>1 and canonical velocity U. Thus rho is smooth, even in x and odd in y, rho_y(0)!=0, obeys |rho(X)|+(1+|X|)|grad rho(X)|<=C(1+|X|)^gamma for some 0<gamma<1, U=o(r), and

    (ell X+U).grad rho=rho,  -Delta psi=rho_x,
    U=(-psi_y,psi_x).

Put p=1/ell, delta=1-p and D=ell-1. By the independently proved symbol theorem (report3.23, ../local_ipm_continuation/PROOF.md) and nonzero trace theorem (report3.7, ../nonzero_far_field/PROOF.md),

    rho,U are in S^p,
    r^{-p}rho(r,theta) -> Theta0(theta) uniformly,
    Theta0!=0.                                             (1)

Here S^b means that every Cartesian derivative of order j is O(r^{b-j}) outside a disc. The parities imply that the only possible density frequencies are positive odd sine modes. Define

    rho_j(r)=(1/pi) int_0^{2pi} rho(r,theta)sin(j theta)dtheta,
    theta_j=(1/pi) int_0^{2pi} Theta0(theta)sin(j theta)dtheta,
    C(r)=#{j positive odd: rho_j(r)!=0},                    (2)

where C(r) can be infinite.

Theorem. For every nonnegative integer M there is R_M such that C(r)>M for every r>R_M. Equivalently, C(r) tends to infinity as r tends to infinity, with the extended-integer meaning of that assertion. There is no sequence r_i tending to infinity along which C(r_i) is bounded by a fixed M. In particular a bounded number of modes per exterior circle is impossible, even if the frequencies can change with r.

For a sharper approximation statement, let V_M be the class of real sums of at most M distinct positive odd sine modes, with arbitrary real coefficients and arbitrary frequency indices. Put

    E_(M,q)(r)=inf_{P in V_M} ||rho(r,.)-P||_{L^q(0,2pi)},
    q=2 or infinity.                                       (3)

The selected frequencies and coefficients of P can depend on r. The following lower bounds hold.

(a) If J is any set of M+1 distinct positive odd frequencies with theta_j!=0 for every j in J, then

    liminf r^{-p} E_(M,infinity)(r) >= (pi/4) min_(j in J)|theta_j|,
    liminf r^{-p} E_(M,2)(r) >= sqrt(pi) min_(j in J)|theta_j|. (4)

In particular these positive bounds apply to every M when Theta0 has infinitely many nonzero coefficients.

(b) If Theta0 is a finite nonzero trigonometric polynomial, let n be its largest frequency and a=theta_n!=0. Define

    n_k=(k+1)(n+1)-1,  s_k=p-k delta,
    A_0=a,
    kD A_k=sum_(i+j=k-1) c_ij A_i A_j,
    c_ij=(1/4)[1-2(j+1)(n+1)/((i+1)(n+p)+2)].             (5)

Then every A_k is nonzero, and for every M>=0,

    liminf r^{-s_M} E_(M,infinity)(r) >= (pi/4)|A_M|,
    liminf r^{-s_M} E_(M,2)(r) >= sqrt(pi)|A_M|.             (6)

There is no assertion that C(r) is infinite at any particular finite radius, or that C(r) is monotone. No existence or convergence of an infinite expansion is assumed. The statements use the actual all-order symbol theorem, not merely a bound on rho itself.

## 2. A projection bound for arbitrary chosen frequencies

For an integrable g on the circle, let g_j=(1/pi) int g sin(j theta). For positive integer j,

    |g_j| <= (4/pi)||g||_infinity,
    |g_j| <= ||g||_2/sqrt(pi).                             (7)

The first inequality uses int_0^{2pi}|sin(j theta)|dtheta=4. The second follows from Cauchy-Schwarz and int sin^2(j theta)=pi. These constants correspond to the unnormalized Lebesgue L2 norm on (0,2pi).

Fix any M+1 distinct positive odd frequencies J and any P in V_M. At least one j in J is missing from P. Orthogonality gives (rho-P)_j=rho_j for that j. Therefore

    ||rho-P||_infinity >= (pi/4) min_(j in J)|rho_j|,
    ||rho-P||_2 >= sqrt(pi) min_(j in J)|rho_j|.             (8)

The right sides do not depend on P. Taking the infimum proves (8) with E_(M,q) on the left. There is no requirement that a minimizing P exist, or that the same frequency be missing at different radii. The finite set J is fixed during this argument.

## 3. Infinite or sufficiently large leading support

Uniform convergence in (1) and (7) imply r^{-p}rho_j(r)->theta_j for each fixed j. For a fixed finite set J, all these convergences hold simultaneously, and the minimum of their absolute values converges to min_J|theta_j|. Applying (8) proves (4).

If Theta0 has infinitely many nonzero Fourier coefficients, choose such a J for each M. All M+1 selected rho_j(r) are nonzero once r is sufficiently large. This proves the theorem in that case. The same observation applies for every M smaller than the finite number of nonzero coefficients of a finite Theta0.

## 4. Finite leading support

The finite-leading-trace cascade is proved in ../finite_far_field_cascade/PROOF.md. Its general S^b inverse lemma allows arbitrarily many angular modes in every remainder. With exactly the hypotheses (1) and the canonical exterior equation, it gives, for each fixed k,

    rho_(n_k)(r)=A_k r^{s_k}+O(r^{s_k-epsilon_k}),
    epsilon_k>0,  A_k=(-1)^k a^{k+1} b_k,  b_k>0.           (9)

This dependency is a theorem about finite asymptotic depth, not a formal series ansatz. Its actual lead Opus5.5 hand review and exact supporting checks are preserved alongside that proof.

Take J={n_0,...,n_M}. These indices are distinct. Formula (9) implies that all M+1 coefficients are nonzero at every sufficiently large radius, proving the mode-count assertion in the finite-leading case. Moreover s_k-s_M=(M-k)delta>0 when k<M. Consequently

    r^{-s_M}|rho_(n_k)(r)| -> infinity for k<M,
    r^{-s_M}|rho_(n_M)(r)| -> |A_M|.

Because J is finite, its scaled minimum tends to |A_M|. Apply (8) to obtain (6). When M=0 this just uses the highest nonzero leading coefficient; there are no k<M cases.

The two cases exhaust the nonzero leading traces. If a sequence r_i tends to infinity and C(r_i)<=M, it eventually contradicts C(r)>M for all r>R_M. This proves all assertions of the theorem.

## 5. Why this does not prove infinite support on each circle

The distinction can be realized by smooth functions satisfying the same symbol bounds and every individual cascade asymptotic. No function in this paragraph is claimed to satisfy the IPM transport equation. The initial construction has zero origin slope for convenience; a compactly supported addition restores any prescribed nonzero slope without changing the far-field assertions. Thus the missing ingredient is the coupled equation, not the origin slope alone.

Fix p in (0,1), an odd n, and the nonzero real sequence A_k from (5), or indeed any prescribed nonzero real sequence. Let chi be smooth on [0,infinity), zero on [0,1] and one on [2,infinity). Choose an increasing sequence R_k tending to infinity, with R_(k+1)>2R_k and R_0>=2, as specified below. Define

    f(r,theta)=sum_(k>=0) A_k chi(r/R_k) r^{s_k}sin(n_k theta),
    f=0 near the origin.                                 (10)

Only finitely many summands are active at each finite r. Thus this defines a smooth Cartesian function on the whole plane with the required parities, finite angular support on each circle, and f_y(0)=0. This initial zero slope will be removed below if desired. The formula r^{s_k} sin(n_k theta) is used only away from zero, so noninteger exponents cause no origin regularity issue.

To choose R_k, use the conormal fields E=r d_r and d_theta. For each total derivative order j there is C_j, depending only on chi and j, such that every conormal derivative of order at most j of the k-th summand is at most

    |A_k| C_j(1+|s_k|+n_k)^j r^{s_k}                    (11)

on its support r>=R_k. This follows by Leibniz' rule: E^i chi(r/R_k) is bounded independently of R_k, and the radial power and trigonometric factor contribute powers of s_k and n_k. Increase C_j to cover all derivative orders up to j. For k>=1 choose R_k so large that, for every j<=k,

    |A_k| C_j(1+|s_k|+n_k)^j R_k^{-k delta/2} <= 2^{-k}. (12)

There are finitely many conditions for each k, and kdelta/2>0, so this is possible along with the strict growth of R_k. For j<=k and r>=R_k, (11)-(12) give the bound

    2^{-k} r^{p-k delta/2}.                              (13)

Fix any K>=0 and any conormal derivative order j. For k>=max(j,2K+2), (13) is at most 2^{-k} r^{s_(K+1)} when r>=1. The geometric sum converges, uniformly with that weighted derivative bound. The finitely many remaining terms with k>K have degrees s_k<=s_(K+1), so they obey the same symbol order with constants depending on j and K. Once r>=2max(R_0,...,R_K), the first K+1 cutoffs equal one. Hence

    f-sum_(k=0)^K A_k r^{s_k}sin(n_k theta) is in S^{s_(K+1)}. (14)

In particular f is in S^p, r^{-p}f tends uniformly to A_0 sin(n theta), and each individual coefficient is exactly A_k r^{s_k} for r>=2R_k. Its canonical velocity exists and belongs to S^p by the general inverse lemma at b=p, so it is o(r). Formula (10) still has only finitely many modes at every finite radius. The sum is locally finite; no exchange of a conditionally convergent series with a derivative is used.

For any prescribed nonzero a_*, take a smooth compactly supported radial eta that equals one near zero and replace f by f+a_* y eta(r). The added term has only the first sine mode, its slope at zero is a_*, and it vanishes outside a fixed disc. It preserves smoothness, parity, finite angular support on each circle and all displayed asymptotics. Its canonical velocity remains in S^p by the same inverse lemma. No transport equation is claimed for this modified function either.

This example verifies that the stated symbol information and cascade asymptotics permit a finite mode count on every circle while that count tends to infinity, even with a prescribed nonzero origin slope. It is not a counterexample to the primary theorem: the coupled transport equation has not been established. To exclude this behavior for exact primary solutions requires an additional use of that equation.

## 6. Scope and verification

This theorem strengthens a fixed-exterior-frequency exclusion to exclusion of a uniform bound on the number of frequencies. It gives lower bounds for best approximation using adaptively selected frequency indices. The bound can decay at a high algebraic rate when the leading trace is finite; it does not preclude accurate approximation on a fixed finite region. The proof does not provide a radius uniform over profiles, a rate of growth of C(r), or control of the dependence of R_M on M. The primary existence question remains open.
