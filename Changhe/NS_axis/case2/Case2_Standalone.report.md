# Case 2: the finite-axis, zero-swirl ancient Euler branch of axisymmetric Navier-Stokes

**Status: UNRESOLVED_NOT_ACCEPTED**.

First missing implication: an upper estimate, valid along the actual Case 2 history, that contradicts the convergence P_n := - nu_n
int_0^{t_n} int q^2 d_z Psi_n dx dt -> m_phi > 0 of the normalized production of the limiting vorticity packet (Theorem 3(b), (d); Psi_n is
the backward adjoint of Theorem 3 with terminal packet phi and m_phi = int eta_U(y,0) phi(y) dy), for example limsup_n P_n < m_phi. Several
distinct sufficient conditions are identified (Section 4, Open (1) to (6)); none is proved, and no equivalence between them is asserted. The estimates prove that a definite positive part of the
production of the limiting vorticity packet comes from the middle history (rescaled times between a growing recent window
A_max(n) ~ nu_n^{-1/2} and any early epoch with negligible int int q^4), and also from the part of the middle history inside a tube
{r < lambda_n} around the axis with physical radius lambda_n -> 0, and that this part carries int int q^4 dx dt >= c D_n M_n
(Theorem 3(e), (f)); these lower bounds do not assert that the complementary contributions are o(1). The positive excess (eta - kappa D_n^2/M_n)_+ of the packet is produced after the last time sigma_n
at which sup eta <= kappa D_n^2/M_n, inside {eta > kappa D_n^2/M_n} (within distance C l_n of the axis), at times when the Hessian is within a
fixed factor of its record (this concerns the excess, not the full signed pairing). By the decay of the adjoint, our estimates penalize
production at ages t_n - t much larger than l_n^2 = M_n^2/D_n^2 unless the older history carries correspondingly more int int q^4. In the
band of ages between the proved window A_max(n)/D_n ~ nu_n^{1/2} l_n^2 and l_n^2 only persistence-or-production alternatives are proved;
nothing makes the contribution of that band negligible. For fixed K >= 1 the production at ages up to K l_n^2 comes, up to an o(1) error
in the normalized pairing, from a tube of radius nu_n^{1/6 - epsilon} l_n = o(l_n) (0 < epsilon < 1/6) around the axis, and the same holds
with a tube of radius o(l_n) up to ages Lambda_n l_n^2 whenever Lambda_n nu_n^{1/2} -> 0 (Theorem 8(a)). Let Vbar_n be the average over the
rescaled ages [0, Lambda_n/nu_n] of the axial total variation of the adjoint, averaged radially with a weight concentrated at the swirl
crossover radius (G nu_n)^{1/3} l_n (the quantity V_nu of Theorem 8(b)). The contribution of ages up to Lambda_n l_n^2 is negligible if
Lambda_n nu_n^{1/3} Vbar_n -> 0 (Theorem 8(b)); for fixed Lambda_n = K this is the condition Vbar_n = o(nu_n^{-1/3}). Over
the whole history the same rescaled quantity, integrated in age, must be at least of order nu_n^{-4/3} (Theorem 8(b), all ages). The required
bound has not been proved for the Case 2 adjoints. Section 4 (x), with the complete proof in Appendix A, gives a prescribed swirl-free construction
showing that the four pointwise velocity bounds do not imply it for every fixed smooth terminal packet: its weighted variation is at
least c nu_n^{-1/3} on a fixed positive fraction of the ages, and its average over every fixed window [0, K'/nu_n], K' >= 1, has the same
lower-bound order. The construction has zero
limiting velocity and does not satisfy the limiting-vorticity packet conditions of Case 2. Being swirl-free, it has no
production; no admissible family with order-one production over the required full history is known (a local example in Section 4, with
prepared radial endpoint data and axial periodicity, produces at the local order of Theorem 8(b) during one modulation time only). Our estimate makes ages
beyond K l_n^2 negligible if Q_4 of the older history is o((1 + K)^{3/2} D_n M_n), which is not known either. Outside {r <= R_0 l_n} the
absolute pairing nu_n int int q^2 |d_z Psi_n| over any time set is at most 2^{-1/2} G ||phi||_2 R_0^{-2} times the square root of its normalized dissipation
(Theorem 8(a)); so if sup_n D_n^3/M_n^5 < infinity (an additional hypothesis: the energy inequality gives only the lower bound
D_n^3/M_n^5 >= pi/(768 E_0)), then for every epsilon > 0 a fixed multiple R_epsilon l_n captures the whole-history production up to
epsilon, uniformly in n. No available estimate bounds
the production there, TARGET-2, or any other substitute from above. Nothing proved here excludes Case 2, and no fixed-datum counterexample
is proposed.
On the forward side (Theorem 9) the same production forces the swirl to do compression work on itself, through the vorticity it has
generated: the positive part of the self-compression rate in the scale-invariant functional int (u^theta)^2/r dx has time integral at least
c/nu_n (no matching upper bound is proved). A bound o(1/nu_n) for this integral would exclude Case 2, and so would the weaker requirement that a time-weighted integral of the
signed rate stay below an explicit multiple of 1/nu_n (Theorem 9(d)). In a drift-free model with prescribed
swirl, a smooth axially periodic steady example (F10 (c)) disproves a universal nonnegative critical-weight work identity, and a localized
whole-space family started from zero sourced vorticity (Appendix B) obeys the three Case 2 spatial velocity bounds and the circulation
bound and has self-compression of the critical order c/nu_n; so in that model those bounds alone do not imply nu_n int (Pi_s)_+ dt -> 0. The
same holds, for a sufficiently small fixed amplitude, when the sourced vorticity is transported by its own poloidal velocity (Appendix C). Both
families prescribe the swirl and have zero limiting velocity; whether the smallness holds for the coupled evolution remains open. Their
nonzero steady localized swirl solves the unforced swirl equation for no smooth incompressible meridional velocity, even a time-dependent
one. Separately, suppose the swirl solves its unforced equation and the radial strain not sourced by the swirl obeys the Case 2 bounds. For
cores satisfying the positivity, curvature and persistence hypotheses of Open (6), with curvature constant sigma, persistence over the
record time 1/nu_n is excluded for all sufficiently large n if ||a_s||_infinity <= (sigma/2 - epsilon) kappa_n throughout, for some
epsilon > 0 independent of n; no such conclusion is proved for all coupled families. In the coupled critical balance of F10 (d) (a
formal identity, derived under additional integrability and boundary hypotheses) the stretching cancels exactly, and Case 2 would be
excluded by an absorption of the remaining commutator and cubic transport terms with a remainder of time integral o(nu_n^{-2}); the cubic
term admits no instantaneous bound T <= epsilon D_psi over arbitrary amplitudes, and whether an integrated estimate holds along the
histories that actually arise is open.

## 1. Result

**Setting.** u is the maximal smooth solution of the 3D Navier-Stokes equations (viscosity 1) on R^3 x [0,T_*), 0 < T_* < infinity,
with one fixed smooth axisymmetric decaying datum u_0 in H^infinity, E_0 = ||u_0||_2^2 < infinity, G = ||r u_0^theta||_infty < infinity.
Notation: Gamma = r u^theta, q = u^theta/r, eta = omega^theta/r, b = u^r e_r + u^z e_z, Delta_5 = d_rr + (3/r) d_r + d_zz,
L = d_rr - (1/r) d_r + d_zz, dx = 2 pi r dr dz. M, S, D, H are the historical suprema over [0,t] of |u|, |u^theta|, |grad u|,
|grad^2 u| (Cartesian Frobenius norms). Branch hypotheses: (A) M H <= C_* D^2 for late times; NO-SWIRL-EXTRACTION: no sequence of
first-crossing swirl records (x_n, t_n) (t_n -> T_*, x_n = (r_n, 0, z_n), |u^theta(x_n, t_n)| = S(t_n) =: S_n > S(t) for t < t_n), and no
subsequence of one, admits both witnesses (W1) |W_n| <= K on every fixed normalized cylinder, with one K for all cylinders and all n, and
(W2) lim_{L -> infinity} limsup_n sup_{-A <= tau <= 0} int_{|y| > L} |W_n(y, tau)|^2 |y|^{-4} dy = 0 for every A < infinity, where
W_n(y, tau) = S_n^{-1} u(r_n y', z_n + r_n y_3, t_n + (r_n/S_n) tau), y = (y', y_3); Case 2: genuine first-crossing
gradient records (x_n,t_n), x_n = (r_n,0,z_n), with alpha_n = r_n/l_n -> alpha_* < infinity, l_n = M_n/D_n, nu_n = D_n/M_n^2.
Rescaled fields U_n(y,tau) = u(a_n + l_n y, t_n + tau/D_n)/M_n with a_n = (0,0,z_n); eta_n, gamma_n, q_n are the
corresponding rescaled quantities, so that eta = (D_n^2/M_n) eta_n, Gamma = gamma_n, q = D_n q_n, U_n^theta = nu_n gamma_n / R. Here M_n = M(t_n), D_n = D(t_n),
H_n = H(t_n), y_n = (alpha_n, 0, 0) is the rescaled record point and y_* = (alpha_*, 0, 0).

**Theorem 1 (reduction, proved).** Under these hypotheses:
(a) S(t)/M(t) -> 0 (B1) and D(t)/M(t)^2 -> 0 (B2).
(b) Let p be the canonical physical pressure and put p_n(y, tau) = M_n^{-2} p(a_n + l_n y, t_n + tau/D_n). On the whole past, |U_n| <= 1,
|grad U_n| <= 1, |grad^2 U_n| <= C_* and |grad p_n| + |d_tau U_n| <= C(1+C_*), and along a subsequence U_n and grad U_n converge locally
uniformly on R^3 x (-infinity,0] (terminal time included) to a bounded, C^{1,1}_x, nonconstant, axisymmetric, swirl-free Euler solution U
with |grad U(y_*,0)| = 1.
(c) eta_U = omega_U^theta / R is constant along every off-axis particle path, and the 3D vorticity equation holds through the axis.
(d) ||omega_U(-A)||_infty >= c_U (1+A)^{-1/2} for all A >= 0 (LOWER), hence TARGET-2,
liminf_{A -> infinity} sqrt(1+A) limsup_n D(t_n - A/D_n)/D_n = 0, excludes Case 2.
For fixed A >= 0 write d(A) = limsup_n D(t_n - A/D_n)/D_n (the times t_n - A/D_n are nonnegative for large n), so that TARGET-2 reads
liminf_{A -> infinity} sqrt(1+A) d(A) = 0.

**Theorem 2 (growing-window persistence, proved).** There are c, c', N depending on the subsequence such that for n >= N and
every 0 <= A <= A_max(n) := c (C_* max(G,1) nu_n)^{-1/2} (A may depend on n),
   ||grad u(t_n - A/D_n)||_infty / D_n >= c' (1+A)^{-1/2}.

**Theorem 3 (whole-history adjoint and history localization, proved).** Fix a solid torus B in {R > delta, |Z| < L} on which
eta_U(.,0) >= 2 kappa > 0 (if necessary after replacing the physical solution by Q u(Qx,t), Q = diag(1,1,-1), which satisfies
the same hypotheses and reverses the sign of eta), phi in C_c^infty(B) axisymmetric, phi >= 0, phi not identically 0, m = int phi.
Let Psi_n solve the backward problem -d_t Psi_n = b.grad Psi_n + L Psi_n on [0,t_n], Psi_n(t_n) = phi((x - a_n)/l_n).
Put Q_4(I) = int_I int q^4 dx dt and Q_4(t) = Q_4([0,t]). Then:
(a) 0 <= Psi_n <= ||phi||_infty, Psi_n = O(r^2) at the axis, int Psi_n(t) dx = l_n^3 m, and
    int_0^{t_n} int |grad Psi_n|^2 dx dt <= l_n^3 ||phi||_2^2 / 2.
(b) int eta_n(y,0) phi(y) dy = nu_n int eta_0 Psi_n(0) dx - nu_n int_0^{t_n} int q^2 d_z Psi_n dx dt, with no axis term, and the
    first term on the right is O(M_n/D_n^2) -> 0.
(c) For every interval I in [0,t_n]: nu_n |int_I int q^2 d_z Psi_n| <= ||phi||_2 (Q_4(I)/(2 D_n M_n))^{1/2}.
(d) Q_4([0,t_n]) >= 2 (m_phi/||phi||_2)^2 D_n M_n (1 - o(1)), where m_phi = int eta_U(0) phi >= 2 kappa m.
(e) For any times s_n with Q_4([0,s_n]) = o(D_n M_n) (for example any fixed s < T_*) and any 0 <= A_n <= A_max(n), the middle history
    I_n = [s_n, t_n - A_n/D_n] carries at least (7/4) kappa m - o(1) of the pairing in (b), and
    Q_4(I_n) >= (49/8) kappa^2 m^2 D_n M_n / ||phi||_2^2 (1 - o(1)).
(f) With e_n = int_{s_n}^{t_n} ||grad u||_2^2 dt and lambda_n = K (e_n/(D_n M_n))^{1/4}, K >= (2 sqrt2 ||phi||_2 G/(kappa m))^{1/2},
    the part of I_n x {r < lambda_n} alone has Q_4 >= (25/8) kappa^2 m^2 D_n M_n / ||phi||_2^2 (1 - o(1)); consequently
    sup_{t in I_n} ||q(t)||_infty^2 >= c D_n M_n / e_n.
(g) (Extension of Theorem 2.) If A_n >= 0, nu_n A_n <= 1 and Q_4([t_n - A_n/D_n, t_n]) <= kappa^2 m^2 D_n M_n / (8 ||phi||_2^2), then
    ||grad u(t_n - A_n/D_n)||_infty / D_n >= c (1 + A_n)^{-1/2}. So for each A_n <= 1/nu_n either the gradient lower bound of
    Theorem 2 persists to rescaled time -A_n or the recent window [t_n - A_n/D_n, t_n] carries Q_4 >= c D_n M_n.
Part (d) also follows, with the same constant, without the adjoint from the L^2 identity for eta (Section 2.7).

**Theorem 5 (truncated excess: persistence of the eta supremum and the production interval, proved).** With the notation of
Theorem 3, k_n := kappa D_n^2/M_n (physical level), and n large:
(a) For every 0 <= A <= A_max(n), sup_y eta_n(y,-A) > kappa; hence ||grad^2 u(t)||_infty > (kappa/sqrt2) D_n^2/M_n
    >= (kappa/(sqrt2 C_*)) H(t_n) for all t in [t_n - A_max(n)/D_n, t_n] (no decay in A, unlike Theorem 2).
(b) Put epsilon_1 = kappa^2 m/(2 ||phi||_infty). For every A in [0, t_n D_n], if sup_y eta_n(y,-A) <= kappa then
    Q_4([t_n - A/D_n, t_n] x {eta > k_n}) >= epsilon_1 D_n M_n.
(c) Let sigma_n be the last time t <= t_n with sup_x eta(x,t) <= k_n. Then sigma_n -> T_*, D_n (t_n - sigma_n) > A_max(n), and the
    whole record excess is produced in (sigma_n, t_n] inside the super level set {eta > k_n}, which lies in {r < (sqrt2/kappa) l_n}:
    int_{sigma_n}^{t_n - A_max(n)/D_n} int_{eta > k_n} |d_z(q^2)| Psi_n dx dt >= (kappa m/4 - o(1)) M_n^2/D_n, and
    Q_4({sigma_n < t <= t_n, eta > k_n}) >= epsilon_1 D_n M_n. On (sigma_n, t_n] the instantaneous Hessian exceeds
    (kappa/sqrt2) D_n^2/M_n, so D(t)^2/M(t) >= (kappa/(sqrt2 C_*)) D_n^2/M_n by (A). If Z_n(t) is the length of the projection of
    {eta(t) > k_n} on the axis, then (t_n - sigma_n) sup Z_n >= int_{sigma_n}^{t_n} Z_n dt >= c_5 l_n^3 / G with
    c_5 = kappa m/(64 pi C_* ||phi||_infty). (Here G > 0; for G = 0 there is no swirl source and the branch is empty.)
    The time sigma_n does not replace the early time of Theorem 3(e): Q_4([0, sigma_n]) = o(D_n M_n) is not known.

**Theorem 6 (decay of the adjoint and the age of the production, proved).** Put w_n(t) = 1 + (t_n - t)/l_n^2.
(a) ||Psi_n(t)||_2^2 <= C l_n^3 w_n(t)^{-3/2} and ||Psi_n(t)||_infty <= C w_n(t)^{-3/2}, with C depending only on m, ||phi||_2, ||phi||_infty.
(b) For 0 <= alpha < 3/2 and every measurable space-time set E: (nu_n int int_E q^2 |d_z Psi_n|)^2 <= C_alpha (D_n M_n)^{-1} int int_E q^4 w_n^{-alpha}.
    Hence the middle history of Theorem 3(e), and its tube in 3(f), carry int int q^4 w_n^{-alpha} >= c_alpha D_n M_n, and the part of the
    pairing older than h is at most C (Q_4([0, t_n - h])/(D_n M_n))^{1/2} (1 + h/l_n^2)^{-3/4}.
(c) nu_n int_0^{t_n - h} int |d_z(q^2)| Psi_n <= C (M_n/D_n^2) int_0^{t_n - h} ||d_z(q^2)(t)||_{L^1} (t_n - t)^{-3/2} dt (scale invariant).
(d) In Theorem 5(c): int_{sigma_n}^{t_n} Z_n w_n^{-3/2} dt >= c l_n^3/G, so sup_{(sigma_n, t_n]} Z_n >= c l_n/G; if 0 <= h <= t_n - sigma_n and
    nu_n int_{sigma_n}^{t_n - h} int_{eta > k_n} |d_z(q^2)| Psi_n dx dt >= delta > 0, then sup_{(sigma_n, t_n]} Z_n >= c delta (l_n/G)(1 + h/l_n^2)^{1/2};
    also, for 0 <= alpha < 3/2, int int_{sigma_n < t <= t_n, eta > k_n} q^4 w_n^{-alpha} dx dt >= c_alpha D_n M_n.

**Proposition 7 (radial compression is necessary, proved).** d/dt int q^2 Psi_n dx = -2 int |grad q|^2 Psi_n dx - 4 int (u^r/r) q^2 Psi_n dx,
and for any interval I = [s, t']: (nu_n int_I int q^2 d_z Psi_n)^2 <= 2 nu_n^2 (int_I int q^2 Psi_n)(int q^2(s) Psi_n(s) + 4 int_I int (u^r/r)_- q^2 Psi_n).
For a suitable choice of s_n -> T_* in Theorem 3(e), the middle history therefore has
int_{I_n} int (u^r/r)_- q^2 Psi_n >= c/(nu_n^2 e_n) and sup_{I_n} (u^r/r)_- >= c/(nu_n^2 e_n^2): the swirl must be compressed radially
where it overlaps the adjoint. (As a size condition this is weaker than Theorem 3: with a_- <= D_n it gives e_n >= c M_n^2 D_n^{-3/2},
smaller than the bound e_n >= c G^{-2/3} C_*^{-4/3} M_n^{7/3} D_n^{-5/3} that Theorem 3(f) gives with |q| <= 2 (G H_n^2)^{1/3} and (A), by the factor G^{-2/3} C_*^{-4/3} nu_n^{-1/6}.)

**Theorem 8 (localization at the axis, compression memory, axis barrier, proved).** Notation of Theorems 3 and 6; psi_n(R, Z, -s)
is the rescaled adjoint at rescaled age s (Psi_n(x, t) = psi_n(x / l_n, -(t_n - t) D_n) after centring), K >= 1 fixed.
(a) Far field. For R_0 > 0 the part of the normalized pairing nu_n int int q^2 d_z Psi_n coming from {r > R_0 l_n} x [t_n - K l_n^2, t_n]
    is at most C K G^2 nu_n^{1/2} R_0^{-3} ||phi||_2 with C < 4.4. So for R_0(n) = nu_n^{1/6 - epsilon} (0 < epsilon < 1/6) the production at ages up to K l_n^2
    comes from a tube of radius o(l_n) around the axis (the tube of Theorem 3(f) need not be thinner than a multiple of l_n).
    The same bound holds with K replaced by any Lambda = Lambda(n) with nu_n L <= Lambda <= t_n/l_n^2 (same proof, same C), so the production
    from {r > R_0 l_n} at ages up to Lambda l_n^2 is o(1) whenever Lambda R_0^{-3} = o(nu_n^{-1/2}); in particular it comes from a tube of
    radius o(l_n) at ages up to Lambda_n l_n^2 if Lambda_n nu_n^{1/2} -> 0, and a non-negligible contribution from outside a fixed tube needs ages at least of order nu_n^{-1/2} l_n^2.
    In this part the absolute pairing on a set E means nu_n int int_E q^2 |d_z Psi_n| dx dt; for E = {r > R_0 l_n} x I it bounds the absolute
    value of the signed source pairing over E, but it is not a bound on nu_n int int_E |d_z(q^2)| Psi_n.
    Over any measurable time set I in [0, t_n], with no restriction on ages, the absolute pairing on {r > R_0 l_n} x I is at most
    2^{-1/2} G ||phi||_2 R_0^{-2} (D_n^3 e_I / M_n^5)^{1/2}, where e_I = int_I ||grad u||_2^2 dt <= ||u_0||_2^2 / 2 (with
    I_n^tau = {D_n (t - t_n): t in I}, D_n^3 e_I / M_n^5 = nu_n int_{I_n^tau} int |grad_y U_n|^2 dy dtau is the normalized dissipation of I).
    Hence if A_* = sup_n D_n^3/M_n^5 < infinity (an additional hypothesis, equivalent to uniformly bounded normalized prelimit energies
    (D_n^3/M_n^5) ||u_0||_2^2; the energy inequality gives only D_n^3/M_n^5 >= pi/(768 ||u_0||_2^2), and finite energy of the limit has not
    been shown to imply it), the whole-history absolute pairing on the complement of {r <= R_0 l_n} is at most
    (1/2) G ||phi||_2 (A_* ||u_0||_2^2)^{1/2} R_0^{-2}, which tends to 0 as R_0 -> infinity uniformly in n; in general a signed
    contribution c from outside {r <= R_0 l_n} needs normalized dissipation at least 2 c^2 R_0^4 / (G ||phi||_2)^2 on the same time set.
(b) Tube reduction. The part from {r <= R_0 l_n} x [t_n - K l_n^2, t_n] is at most 4 pi C_*^{2/3} (G nu_n)^{4/3} int_0^{K/nu_n} TV_n(s) ds,
    TV_n(s) = int sup_{R < R_0} |d_Z psi_n(R, Z, -s)| dZ. More precisely, with r_c^2 = (G nu_n)^{2/3}/(2 C_*^{2/3}) and the probability density
    w_nu(R) = R/r_c^2 (R <= r_c), r_c^2/R^3 (R >= r_c), the whole pairing over ages up to K/nu_n (no tube restriction) is at most
    4 pi C_*^{2/3} (G nu_n)^{4/3} int_0^{K/nu_n} V_nu(s) ds, V_nu(s) = int_0^infty w_nu(R) int |d_Z psi_n(R, Z, -s)| dZ dR. Ages up to K l_n^2 are
    therefore negligible as soon as (nu_n/K) int_0^{K/nu_n} V_nu(s) ds = o(nu_n^{-1/3}).
    The same bound holds over the whole history, so Case 2 forces, for all large n,
    4 pi C_*^{2/3} G^{4/3} nu_n^{4/3} int_0^{t_n D_n} V_nu(s) ds >= m_phi - o(1) >= 2 kappa m - o(1), with m_phi = int eta_U(0) phi (one scale-invariant
    necessary condition for all ages; if int |d_Z psi_n(R, Z, -s)| dZ <= C (1 + nu_n s)^{-3/2} held uniformly in R, the left side would be
    O(nu_n^{1/3}), and O(nu_n log(1/nu_n)) under the bound C min(R^2, 1)(1 + nu_n s)^{-3/2}; neither bound is proved).
(c) Compression memory. With A(t) = ||(u^r/r)_-(t)||_infty, ||q(t)||_infty <= G / (4 int_s^t exp(-2 int_rho^t A) d rho) for s < t, and
    sup_{[s,t]} ||q||_infty <= max(G sup_{[s,t]} A, 2 (log 2) ||q(s)||_infty). In Case 2, for a suitable choice of s_n (as in Proposition 7, with in addition ||q(s_n)||_infty^2 e_n = o(D_n M_n), which holds when s_n -> T_*
    slowly enough), sup_{I_n} (u^r/r)_- >= (c/G) (D_n M_n / e_n)^{1/2}.
(d) Axis barrier. Psi_n(x, t) <= C min(1, D_n r^2) w_n(t)^{-3/2} for t_n - t >= 1/(4 D_n).
The vanishing conclusions for ages up to K l_n^2 are asymptotic statements for fixed K and n large (the prelimit history is finite). The
quantitative bound in (a) holds uniformly for every nu_n L <= Lambda <= t_n/l_n^2, including n-dependent Lambda, and its dissipation form
and the integral inequality in (b) hold over the whole available history; no vanishing conclusion for growing windows is asserted without
the corresponding smallness condition (for (b) over ages up to Lambda_n/nu_n it is Lambda_n nu_n^{1/3} Vbar_n -> 0, Vbar_n the age average
of V_nu over those ages). In rescaled form (c) says
that ||q_n(tau)||_infty >= Q forces int_{tau - h}^tau ||(U_n^R/R)_-||_infty >= (1/2) log(4 Q h / G) for G/(4Q) < h <= tau + t_n D_n; it does not say that compression
persists along one trajectory. The barrier (d) is pointwise: it gives no axial or temporal integrability and does not by itself make the source
in {R < nu_n^{1/2}} negligible.

**Theorem 9 (swirl functional, compression work, compression action and self-compression, proved).**
Put a = u^r/r, P = ||phi||_infty, Sigma(t) = int q^2 r dx = 2 pi int int (u^theta)^2 dr dz (scale invariant; Sigma(t) <= ||grad u(t)||_2^2 + ||u(t)||_2^2),
W(t) = int_0^t int a_- q^2 r dx ds (a_- = max(-a, 0)), Abar(t) = int a q^2 r dx / Sigma(t) and Act(t) = sup_{0 <= s <= t} int_0^s (- Abar) (scale invariant).
(a) For t < T_*, Sigma' = - 2 int |grad q|^2 r dx - int q^2/r dx - 3 int a q^2 r dx. This is the case p = 2, d = -1/2 of the weighted swirl
    balance of Shahmurov (arXiv:2604.21213v3, Proposition 2.1(a)). Consequently Sigma(t) + int_0^t ||d_z(q^2)||_{L^1} ds <= Sigma(0) + 3 W(t) and
    int_0^t ||d_z(q^2)||_{L^1} ds <= e^{3 Act(t)} Sigma(0).
(b) In Case 2, int_0^{t_n} ||d_z(q^2)||_{L^1} dt >= (2 m_phi/P) nu_n^{-1} (1 - o(1)) (without an additional hypothesis such as (DEC)),
    W(t_n) >= (2 m_phi/(3P)) nu_n^{-1} (1 - o(1)) - Sigma(0)/3, and Act(t_n) >= (1/3) log(1/nu_n) + (1/3) log(2 m_phi/(P Sigma(0))) - o(1).
(c) With the adjoint of Theorem 3 as weight, d/dt int q^2 r Psi_n dx <= - int (2 (d_z q)^2 r + q^2/r) Psi_n dx - 3 int a q^2 r Psi_n dx, and in Case 2
    int_0^{t_n} int a_- q^2 r Psi_n dx dt >= (2^{1/2} m_phi/3) nu_n^{-1} (1 - o(1)) - P Sigma(0)/3; the Psi_n-weighted action (Act with q^2 r Psi_n in
    place of q^2 r) is at least (1/3) log(1/nu_n) + (1/3) log(2^{1/2} m_phi/(P Sigma(0))) - o(1).
(d) Split eta = eta_r + eta_s, both transported by the actual b, with (d_t + b.grad - Delta_5) eta_r = 0, eta_r(0) = eta_0, and
    (d_t + b.grad - Delta_5) eta_s = d_z(q^2), eta_s(0) = 0; let a_r, a_s be the values of u^r/r of the velocities recovered from r eta_r e_theta and
    r eta_s e_theta by the whole-space Biot-Savart law (so a = a_r + a_s). Then ||a_r(t)||_infty <= C_0 := C ||eta_0||_2^{2/3} ||eta_0||_infty^{1/3}
    for all t < T_*, and with Pi_s(t) = - int a_s q^2 r dx (the self-compression rate), Case 2 forces the signed weighted bound
    int_0^{t_n} e^{3 C_0 (t_n - t)} Pi_s(t) dt >= (2 m_phi/(3P)) nu_n^{-1} (1 - o(1)) - e^{3 C_0 T_*} Sigma(0)/3, and in particular
    int_0^{t_n} Pi_s(t)_+ dt >= e^{-3 C_0 T_*} (m_phi/(3P)) nu_n^{-1} for all large n (the weights lie in [1, e^{3 C_0 T_*}]).
(e) In rescaled variables W(t_n) = nu_n^{-2} int int (a_n)_- q_n^2 R dy dtau over the rescaled history, so (b) asks for rescaled work of order nu_n.
    This is the order produced by cells of radius delta = (G nu_n/C_*)^{1/3} with saturated swirl |q_n| ~ C_* delta and compression nu_n/delta^2
    over a fixed axial length and a rescaled time 1/nu_n: the reduction is critical in the sense of this conditional scale count (it does not
    show that such cells persist or are realized by a solution).
In the rescaled frame a_r = O(1/D_n) (its integral over the rescaled history of length t_n D_n is controlled by the Gronwall step of (d)), so by (d)
Case 2 requires the swirl to compress itself through the vorticity it has generated, in the sense int_0^{t_n} (Pi_s)_+ dt >= c/nu_n, where (Pi_s)_+
is the positive part of the spatial integral Pi_s (no matching upper bound is proved). Any bound nu_n int_0^{t_n} (Pi_s)_+ dt -> 0 for the coupled
solution would exclude Case 2, and so would the weaker signed bound limsup nu_n int_0^{t_n} e^{3 C_0 (t_n - t)} Pi_s(t) dt < 2 m_phi/(3P),
which tolerates compression of order 1/nu_n provided it is sufficiently offset by expansion carrying the same weight. In a drift-free model with prescribed swirl, F10 (c) gives an axially periodic steady example with negative
critical-weight work, and Appendix B a localized whole-space family, started from zero sourced vorticity and obeying the three spatial
velocity bounds of Theorem 1(b) and |Gamma| <= G, with nu int (Pi_s)_+ dt >= c; so in that model the three spatial velocity bounds and the
circulation bound do not imply nu int (Pi_s)_+ dt -> 0. Appendix C proves the same when eta_s is transported by its own poloidal
velocity, with q still prescribed. In both families the velocity and its gradient tend uniformly to zero and there is no normalized gradient record; neither solves the Navier-Stokes system. This does not settle the signed weighted threshold under the Case 2 hypotheses. The question for the
coupled evolution remains open.

**Proposition 4 (conservation structure, proved under the additional solution hypothesis (DEC): eta, grad eta,
r^2 eta, |u||omega|, Gamma grad Gamma are in L^1(R^3) locally uniformly in time, and int |eta(0,z,t)| dz is locally integrable in time).**
(a) For every f in C^2, d/dt int eta f(Gamma) dx = int eta f''(Gamma) |grad Gamma|^2 dx + 2 int eta f'(Gamma) L Gamma dx
    - 4 pi f(0) int eta(0,z,t) dz. The swirl source drops out exactly, because f(Gamma) d_z(q^2) = r^{-4} d_z K(Gamma), K' = 2 s f.
(b) int r^2 eta dx (twice the axial impulse) is conserved.
(c) ||eta(t)||_{L^1} <= ||eta_0||_{L^1} + int_0^t ||d_z(q^2)||_{L^1} ds.

**Corollaries (proved).** In Case 2:
(i) sup_{s < t_n} D(s)(T_* - s) >= c (C_* max(G,1) nu_n)^{-1/4} -> infinity: the gradient blow-up is of Type II at a quantified rate.
(ii) ||eta(t_n)||_{L^1(R^3)} >= c/nu_n -> infinity, and int_0^{T_*} ||d_z((u^theta/r)^2)||_{L^1(R^3)} dt = infinity
(a scale-invariant quantity; by Theorem 9(b), without (DEC)); any regularity mechanism bounding this time integral excludes Case 2.
(iii) The whole-history source budget 16 pi P G nu_n int_0^{t_n} H(t) (l_n L + int_t^{t_n} M(s) ds) dt >= m_phi - o(1) holds (P = ||phi||_infty,
phi supported in |Z| < L, Section 2.7d); in particular int_0^{t_n} H(t) (l_n L + int_t^{t_n} M + sqrt(t_n - t)) dt >= c M_n^2/(G D_n).
(iv) ||grad^2 p(t)||_infty <= C(1+C_*) D(t)^2 under (A), so D' <= C(1+C_*) D^2 a.e.; this is a lower bound on the past gradient only.
(v) Q_4(t_n) = o(D_n M_n) along the Case 2 sequence would exclude Case 2 (Theorem 3(d)).
(vi) There is y_0 with R_0 = |y_0'| > 0 and U(y_0,0) != 0; then (R_0 l_n) |u(a_n + l_n y_0, t_n)| >= c/nu_n -> infinity, so
sup_x r|u(x,t_n)| >= c/nu_n. (At the record point itself r_n |u(x_n,t_n)| = (alpha_n/nu_n)|U_n(y_n,0)| may be small, e.g. alpha_* = 0.)

What is not proved: TARGET-2, Q_4(t_n) = o(D_n M_n), or any other exclusion. A power-law compatibility test (Section 4) shows
that the scalar growth and budget inequalities derived here, including Theorem 3, are mutually compatible with d(A) = 1 for every A
(this is not a simultaneous spatial realization of the estimates).

## 2. Method

The following paragraphs present the main arguments and constants.

2.1 Swirl facts. |Gamma| <= G (maximum principle for (d_t + b.grad) Gamma = L Gamma, which has no zeroth order term).
Pointwise, ((u^theta)^2 + (u^r)^2)/r^2 <= |grad u|^2 (from (e_theta.grad)u = -(u^theta/r) e_r + (u^r/r) e_theta), so S^2 <= G D;
the swirl and poloidal parts of an axisymmetric field have Frobenius-orthogonal gradients, which gives |d_z q| <= |grad^2 u|.
At a first-crossing swirl record the angular equation gives -r_n u^r >= 1, hence S_n/M_n <= G.
For fixed t with H = ||grad^2 u(t)||: |q| <= 2(G H^2)^{1/3} (Taylor at the axis plus |Gamma| <= G), |d_z q| <= H,
|d_z Gamma| <= sqrt(2 G r H) (Landau's inequality ||f'||^2 <= 2||f|| ||f''|| on the z-line). Splitting at r = (G/H)^{1/3},
   int_0^infty |d_z(q^2)| r dr <= (2 + 4 sqrt2/3) G H <= 4 G H for every z,
and ||d_z(q^2)||_infty <= 4 G^{1/3} H^{5/3}. After rescaling: radial source mass <= 8 pi C_* G nu_n per unit height, pointwise
source <= 4 C_*^{5/3} (G nu_n)^{1/3} and <= 2 C_*.

2.2 B1. If S/M does not tend to 0, choose t_j -> T_* with S(t_j) >= epsilon M(t_j) (so S(t_j) -> infinity, since M -> infinity at T_*)
and let s_j be the first time at which S reaches S(t_j)/2. Then s_j -> T_*, there is a first-crossing swirl record at time s_j, and
S(s_j) = S(t_j)/2 >= (epsilon/2) M(s_j); the normalized fields W_j are bounded by M(s_j)/S(s_j) <= 2/epsilon on their whole past, so they
satisfy (W1) with K = 2/epsilon and (W2) with tail at most 4 pi (2/epsilon)^2/L, contradicting NO-SWIRL-EXTRACTION. (Since S^2 <= G D,
B2 also implies B1 directly.) B2. If B2 fails, choose t_j -> T_* with D(t_j) >= epsilon M(t_j)^2 and let s_j be the first time at which D
reaches D(t_j)/2; then D(s_j) >= (epsilon/2) M(s_j)^2 and there is a first-crossing gradient record at s_j. Rescale about the record point
by m_j = M(s_j) (velocity by m_j, length by 1/m_j, time by 1/m_j^2). The normalized velocity is bounded by 1 on the whole normalized past;
bounded-data mild local existence extends it to a fixed normalized time c > 0 beyond the record with bound 2 (the solution exists past
s_j for a time >= c/M(s_j)^2); interior smoothing of bounded mild solutions gives uniform bounds on all spatial derivatives on compact
subintervals of the normalized existence interval, whose initial time tends to -infinity. Hence the record gradient, at least epsilon/2,
is attained at the interior time 0 of a uniformly smooth family. If the normalized distance from the record to the axis stays bounded,
centre on the axis: a subsequence converges to a bounded ancient axisymmetric mild solution on (-infinity, c/2], swirl-free by B1. If
that distance tends to infinity, centre at the record: the limit is independent of the angular coordinate, which becomes a translation
direction, and its component in that direction vanishes by B1, so it is a bounded ancient two-dimensional mild solution. In both cases
the limit is mild because the Duhamel formula passes to the limit (the uniform velocity bound controls the spatial tails of the Oseen
kernel, whose time singularity is integrable). By the Liouville theorems of Koch-Nadirashvili-Seregin-Sverak (Acta Math. 203 (2009),
Theorems 5.1 and 5.2 with Remark 6.1) such solutions are spatially constant, which contradicts the gradient of magnitude at least epsilon/2
retained at the limiting record point at time 0. Thus B2 holds.

2.3 Compactness. (A) at the single time t_n bounds grad^2 U_n on the whole past since H is historical. The canonical pressure is
split into a near part (Riesz transform of a compactly supported Lipschitz function) and a far part (kernel O(|x|^{-4}));
this gives |grad p_n| <= C(1+C_*). Interpolation in space gives the 1/2-Holder modulus of grad U_n in time, so convergence of
gradients holds through tau = 0 and the record |grad U_n(y_n,0)| = 1 survives.
Corollary (iv). At a late time t write M, D, H for the historical suprema at t and a = M/D. With f = sum_{i,j} (d_i u_j)(d_j u_i), so that
-Delta p = f = sum_{i,j} d_i d_j (u_i u_j), split the kernel of grad^2 (-Delta)^{-1} by a smooth radial cutoff at distance a. The local
distributional term is bounded by |f| <= C D^2. In the near principal-value integral subtract f(x) (the kernel has zero spherical means);
since ||grad f||_infty <= C D H this part is at most C a D H. In the far integral move both derivatives of d_i d_j (u_i u_j) onto the cut-off
kernel; the resulting kernel has L^1 norm at most C a^{-2}, so this part is at most C M^2/a^2. Hence ||grad^2 p(t)||_infty <=
C (D^2 + a D H + M^2/a^2) <= C (D^2 + M H) <= C (1 + C_*) D^2 by (A). The Cartesian gradient equation and the maximum principle bound the
upper Dini derivative of ||grad u(t)||_infty by ||grad u||_infty^2 + ||grad^2 p||_infty <= C (1 + C_*) D(t)^2; the historical maximum D
is locally Lipschitz before T_* and satisfies D' <= C (1 + C_*) D^2 almost everywhere. Integrating backward gives
D(t_n - A/D_n)/D_n >= 1/(1 + C (1 + C_*) A) whenever the interval lies in the late-time regime. This is a lower bound, not TARGET-2.

2.4 Euler limit. The 3D vorticity equation in components, d_tau omega_i + d_j(U_j omega_i - omega_j U_i) = nu Delta omega_i, has
only bilinear terms in (U_n, omega_n), all converging locally uniformly; the swirl source is one of its components and vanishes
in the limit because U^theta = 0, including at the axis. Since omega_U is Lipschitz in space-time, the Lagrangian form gives
D_tau (omega^theta/R) = 0 off the axis; |U^R| <= R keeps particle paths off the axis (no axis trace of eta_U is claimed).
Nontriviality: omega_U(.,0) = 0 would make U(.,0) a bounded harmonic gradient, hence constant.

2.5 LOWER. Transport a solid torus where |eta_U(0)| >= 2 kappa backward by the measure-preserving flow; it stays in
|Z| < L + A; at most half of its 3D volume v fits in {R < rho} if 2 pi rho^2 (L+A) = v/2; there |omega| >= 2 kappa rho.
Then |grad U(y,-A)| <= d(A) pointwise gives c_U (1+A)^{-1/2} <= sqrt2 d(A).

2.6 WINDOW. Lift eta_n to R^5 (R = |w|, w in R^4), where it solves d_tau eta + U.grad_5 eta = nu Delta_5 eta + d_Z(q^2) with
smooth coefficients and div_5 U = 2U^R/R. Solve the backward adjoint -d_tau chi - div_5(U chi) = nu Delta_5 chi with
chi(0) = phi/(pi R^2). Then psi = pi R^2 chi satisfies
   int eta_n(0) phi = int eta_n(-A) psi(-A) + int_{-A}^0 int d_Z(q_n^2) psi,
with psi >= 0, int psi = int phi (5D mass conservation, no axis flux), psi <= ||phi|| (psi solves a drift-diffusion
equation with operator d_RR - (1/R) d_R + d_ZZ and no zeroth order term, vanishing on the axis), and Gaussian axial tails.
The source term is <= C C_* G nu_n A (L+A) by the radial source mass; the past term is bounded, by the bathtub principle
applied to |eta_n(-A)| <= ||omega^theta_n(-A)||/R, by 2 sqrt(2 pi) ||omega^theta_n(-A)|| sqrt((L+A+1) m ||phi||). Comparing
with int eta_n(0) phi >= (3/2) kappa m gives Theorem 2 as long as nu_n A^2 is small.

2.7 Whole-history adjoint (Theorem 3). The same adjoint, now in physical variables on the entire interval [0,t_n], is
Psi_n = r^2 chi with -d_t chi - div_5(b chi) = Delta_5 chi; its rescaling is exactly the psi of 2.6 on every recent window.
Multiplying the backward equation by Psi_n and integrating in dx: the drift term vanishes (div b = 0), and for L = Delta_3 - (2/r) d_r
the extra term is -2 pi int [Psi^2]_{r=0}^{infinity} dz = 0 because Psi_n vanishes on the axis, so
(1/2) d/dt int Psi_n^2 = int |grad Psi_n|^2, which integrates to the energy bound (a). The integration by parts formula
int (Delta_5 eta) g dx = int eta L g dx - 4 pi int eta(0,z) g(0,z) dz (radial part: int (eta_rr + 3 eta_r/r) g r dr =
-2 eta(0) g(0) + int eta (g_rr - g_r/r) r dr) with g = Psi_n, g(0,z) = 0, gives d/dt int eta Psi_n = -int q^2 d_z Psi_n, hence (b).
The scaling identities nu_n l_n^3 = M_n/D_n^2 and nu_n^2 l_n^3 = 1/(D_n M_n) turn (b) and Cauchy-Schwarz into (c) and (d).
For (e), the recent part equals the source term of 2.6 and is bounded as there; the early part is controlled by (c).
For (f), |q| = |Gamma|/r^2 <= G/r^2 and q^2 <= |grad u|^2 give int_{I_n} int_{r >= lambda} q^4 <= G^2 lambda^{-4} e_n.
For (g), the source term of the window identity is bounded by (c) instead of the radial source mass, and the tails by the
Gaussian moment bound with h = L + A_n + 1 + C (nu_n A_n)^{1/2}. The L^2 identity for eta (transport drops out since div b = 0, and
int (Delta_5 eta) eta dx = -||grad eta||_2^2 - 2 pi int eta(0,z)^2 dz) is E'(t) + 2 ||grad eta||_2^2 + 4 pi int eta(0,z,t)^2 dz
= -2 int q^2 d_z eta dx, where E(t) = ||eta(t)||_2^2. Using 2 |q^2 d_z eta| <= 2 |d_z eta|^2 + q^4/2 and dropping the remaining
nonnegative terms gives E(t) <= E(0) + Q_4([0,t])/2. Cauchy-Schwarz against phi((x - a_n)/l_n) gives
E(t_n) >= D_n M_n (m_phi/||phi||_2)^2 (1 - o(1)). Since E(0) is fixed and D_n M_n -> infinity, this proves (d) with its stated
coefficient, without the adjoint. The adjoint is needed for the
recent-window part of (e), for (f), (g) and the signed identity (b). The backward operator with zero axis trace, its energy
estimate and its pairing with omega^theta/r were used before for swirl-free flows by Nobili and Seis (arXiv:1906.07400,
Section 6); the swirl-source pairing and the localization statements are new here as far as we know.

2.7a Truncated excess (Theorem 5). For every C^2 function f (convex in what follows), f(eta_n) satisfies
d_tau f + U.grad_5 f = nu Delta_5 f - nu f''|grad eta|^2 + f'(eta) d_Z(q_n^2). Pairing with the nonnegative adjoint chi of 2.6 gives
int (eta_n(0) - kappa)_+ phi <= int (eta_n(-A) - kappa)_+ psi(-A) + int_{-A}^0 int_{eta_n > kappa} |d_Z(q_n^2)| psi, after approximating
(s - kappa)_+ by f_e(s) = int_kappa^s theta((v - kappa)/e) dv with a smooth step theta and dominated convergence. On the WINDOW range
the source term is at most kappa m/4 + o(1) (the bound of 2.6 is for the absolute value), while the left side is at least
kappa m/2, so the super level set {eta_n(-A) > kappa} is nonempty; since omega^theta vanishes on the axis,
|eta| <= ||grad omega|| <= sqrt2 ||grad^2 u||. For (b), h = (eta_n - kappa)_+ obeys, in three dimensional measure,
d/dtau int h^2 <= -4 pi nu_n int h(0,Z)^2 dZ + (2 nu_n)^{-1} int_{eta_n > kappa} q_n^4 (the axis term comes from the (2/R) d_R part of
Delta_5, the source is integrated by parts in Z and absorbed by the dissipation), and int h(0)^2 >= kappa^2 m/(4 ||phi||_infty).
For (c), the excess vanishes at sigma_n, so all of it is produced on (sigma_n, t_n] by the source restricted to
{eta > k_n}, and the radial source mass bound of 2.1 converts the production into int Z_n dt >= c l_n^3/G.

2.7b Decay of the adjoint (Theorem 6) and compression (Proposition 7). The adjoint conserves int Psi_n dx = l_n^3 m and satisfies
(1/2) d/dh ||Psi_n(t_n - h)||_2^2 = -||grad Psi_n||_2^2; the Nash inequality ||f||_2^{5/3} <= C ||f||_1^{2/3} ||grad f||_2 turns this into
||Psi_n(t_n - h)||_2^2 <= C l_n^3 (1 + h/l_n^2)^{-3/2}. The L^infinity bound follows by duality: the forward homogeneous eta operator
d_t + b.grad - Delta_5 preserves int g Psi_n, does not increase the L^1 norm (int Delta_5 g dx = -4 pi int g(0,z) dz), and dissipates the
L^2 norm (int g Delta_5 g dx = -||grad g||_2^2 - 2 pi int g(0,z)^2 dz), so it obeys the same Nash bound; splitting [t_n - h, t_n] at the
midpoint gives ||Psi_n(t_n - h)||_infty <= C m l_n^3 h^{-3/2}. Integration by parts in h gives the weighted energy
int w_n^alpha ||grad Psi_n||_2^2 dt <= C_alpha l_n^3 for alpha < 3/2, and the weighted Cauchy-Schwarz inequality gives Theorem 6(b).
The first two assertions of Theorem 6(d) repeat the proof of Theorem 5(c) with the decaying sup bound of Psi_n: by 2.1,
int_{eta > k_n} |d_z(q^2)| dx <= 8 pi G H(t) Z_n(t) with H(t) <= C_* D_n^2/M_n, and the integral of w_n^{-3/2} over ages at least h is
2 l_n^2 (1 + h/l_n^2)^{-1/2}, while nu_n (D_n^2/M_n) l_n^2 = 1/l_n. The last assertion cannot be obtained by integrating the restricted
source by parts against Psi_n itself, since the indicator of {eta > k_n} would produce a level-set boundary term; a killed adjoint is used
instead. Set E_n = {(x, t): sigma_n < t < t_n, eta(x, t) > k_n} and h_n = (eta - k_n)_+. Let Psi_n^E be the backward adjoint on E_n with
terminal datum phi((x - a_n)/l_n), zero data on the moving level boundary and zero axis trace (the killed adjoint evolution on the open
parabolic set E_n, obtained by smooth domain approximation; the estimates below persist under exhaustion). For large n the terminal
packet lies inside the terminal super level set, since eta_n(., 0) -> eta_U(., 0) >= 2 kappa uniformly on B. In E_n, h_n = eta - k_n solves
the eta equation; h_n and Psi_n^E vanish on the level boundary, h_n vanishes at sigma_n, and Green's identity gives
int h_n(t_n) phi((x - a_n)/l_n) dx = - int int_{E_n} q^2 d_z Psi_n^E dx dt with no boundary contribution. By comparison 0 <= Psi_n^E <= Psi_n,
so Psi_n^E <= ||phi||_infty and its mass is at most l_n^3 m; on the moving domain (1/2) d/dh ||Psi_n^E||_2^2 = -||grad Psi_n^E||_2^2 (the
boundary terms vanish because Psi_n^E = 0 there), and the Nash argument above applied to Psi_n^E extended by zero gives
||Psi_n^E(t)||_2^2 <= C l_n^3 w_n(t)^{-3/2} and int_{sigma_n}^{t_n} w_n^alpha ||grad Psi_n^E||_2^2 dt <= C_alpha l_n^3 for 0 <= alpha < 3/2.
The normalized terminal excess nu_n int h_n(t_n) phi((x - a_n)/l_n) dx = int (eta_n(., 0) - kappa)_+ phi tends to int (eta_U(., 0) - kappa) phi
>= kappa m, and the weighted Cauchy-Schwarz inequality with nu_n^2 l_n^3 = 1/(D_n M_n) gives (kappa m/2)^2 <= C_alpha (D_n M_n)^{-1}
int int_{E_n} q^4 w_n^{-alpha} for large n, which is the last assertion, including its restriction to the super level set. For Proposition 7, (d_t + b.grad) q^2 =
Delta_5 q^2 - 2|grad q|^2 - 4 (u^r/r) q^2, the axis term vanishes against Psi_n, and the pairing is 2 nu_n int q (d_z q) Psi_n.
By Cauchy-Schwarz its square over I is at most 4 nu_n^2 (int_I int q^2 Psi_n)(int_I int |grad q|^2 Psi_n), and integrating the identity over
I gives 2 int_I int |grad q|^2 Psi_n <= int q^2(s) Psi_n(s) + 4 int_I int (u^r/r)_- q^2 Psi_n; this is the displayed inequality. For the
consequences choose s_n -> T_* so slowly that Q_4([0, s_n]) = o(D_n M_n) and nu_n^2 ||q(s_n)||_2^2 -> 0 (a diagonal choice: both quantities
are finite for each fixed s < T_*, while D_n M_n -> infinity and nu_n -> 0). Put P = ||phi||_infty, B_n = int_{I_n} int q^2 Psi_n, J_n = int
q^2(s_n) Psi_n(s_n) and W_n = int_{I_n} int (u^r/r)_- q^2 Psi_n. Since q^2 <= |grad u|^2 and I_n is contained in [s_n, t_n], B_n <= P e_n
and J_n <= P ||q(s_n)||_2^2. By Theorem 3(e) the absolute normalized pairing over I_n is at least p_0 = kappa m for large n, so p_0^2 <= 2
nu_n^2 P e_n J_n + 8 nu_n^2 P e_n W_n. As e_n <= E_0/2 by the energy inequality, the first term tends to 0, hence W_n >= p_0^2/(16 P nu_n^2
e_n) for large n, and W_n <= B_n sup_{I_n} (u^r/r)_- gives sup_{I_n} (u^r/r)_- >= p_0^2/(16 P^2 nu_n^2 e_n^2), the supremum being over space
and I_n.

2.7c Theorem 8. In rescaled variables (age s, viscosity nu = nu_n, d_s psi = U.grad psi + nu L psi, L = d_RR - (1/R) d_R + d_ZZ) put
W = 2 cosh((Z - Z_0)/S) e^{-2s/S}. Since W does not depend on R and psi vanishes on the axis, d/ds int psi^2 W = -2 nu int |grad psi|^2
W + int psi^2 (d_s W - U.grad W + nu d_ZZ W), and the bracket is at most W(-1/S + nu/S^2) <= 0 for S >= nu (|U| <= 1). Hence
2 nu int_0^S int |grad psi|^2 W <= 2 cosh(L/S) ||phi||_2^2 if phi is supported in |Z - Z_0| <= L. Cauchy-Schwarz with the weights 1/W and W,
q_n <= G nu / R^2 (from |Gamma| <= G), int 1/W dZ <= e^2 pi S/2 and int_{R > R_0} q_n^4 dy <= (pi/3)(G nu)^4 R_0^{-6} per unit length give (a)
with S = K/nu, and its extension with S = Lambda/nu (for n so large that nu_n <= L, Lambda >= nu_n L gives S >= max(L, nu_n), so the
weighted inequality applies and cosh(L/S) <= cosh 1; pi e (cosh(1)/6)^{1/2} = 4.3307... < 4.4). The growing weight is justified by first
using W_N = e^{-2s/S} min(2 cosh((Z - Z_0)/S), N), whose distributional second Z-derivative is at most W_N/S^2 and whose first is at most
W_N/S in absolute value, and letting N -> infinity by monotone convergence. The dissipation form of (a): for axisymmetric fields the swirl part of grad u in the cylindrical frame contains the
entry -u^theta/r, so q^2 <= |grad u|^2 pointwise and int_I int q^2 dx dt <= e_I; with |q| <= G/r^2 on {r > R_0 l_n} and Theorem 3(a),
nu_n |int_I int_{r > R_0 l_n} q^2 d_z Psi_n| <= nu_n G (R_0 l_n)^{-2} e_I^{1/2} (l_n^3/2)^{1/2} ||phi||_2, and nu_n l_n^{-1/2} = (D_n^3/M_n^5)^{1/2}. For (b), q_n <= 2 C_*^{2/3} (G nu)^{1/3} (rescaling, with (A), the physical bound |q| <= 2 (G H^2)^{1/3}, which follows from |u^theta(r,z) - a r| <= H r^2/2, a = d_r u^theta(0,z), and
Gamma(a/H, z) <= G) and q_n <= G nu/R^2
give int q_n^2 2 pi R dR <= 4 pi C_*^{2/3} (G nu)^{4/3} after optimizing the split radius. (c) is comparison with the supersolution
G (1 - e^{-k(t) r^2}) of the Gamma equation, written in s = r^2 as d_t + 2 (u^r/r) s d_s + u^z d_z - 4 s d_ss - d_zz: its residual is
2 G k r^2 e^{-k r^2} (A + u^r/r) >= 0 when k' = 2 A k - 4 k^2, and m = 1/k solves m' = -2 A m + 4, m(s) = 0; the stationary
supersolution 2 G (1 - e^{-k_0 r^2}), k_0 = max(A_*/2, (log 2) ||q(s)||_infty / G), gives the second bound, and Proposition 7 with the choice
of s_n there gives the Case 2 consequence. (d) is comparison with ||psi(-s_0)||_infty (1 - e^{-k R^2}), k = 1/(2 nu (1 - e^{-2h})), whose
residual 2 k (1 - U^R/R) R^2 e^{-k R^2} is nonnegative because |U^R/R| <= |grad U| <= 1, combined with Theorem 6(a).

2.7d Corollary (iii). With h = t_n - t, b(h) = l_n L + int_{t_n - h}^{t_n} M(s) ds and g_h the one-dimensional heat kernel, the function
V(z, h) = int_{-b(h)}^{b(h)} g_h(z - z_n - y) dy satisfies V_h - V_zz = M(t_n - h) [g_h(z - z_n - b) + g_h(z - z_n + b)] >= M(t_n - h) |V_z| >= u^z V_z.
Since V does not depend on r, P V is a supersolution of the backward adjoint equation d_h Psi = b.grad Psi + L Psi; it dominates Psi_n at h = 0
(the terminal datum is at most P on the slab |z - z_n| < l_n L; approximate the slab indicator by smooth barriers), and Psi_n - P V <= 0 on the
axis and at infinity. The maximum principle gives Psi_n <= P V, hence int sup_r Psi_n(r, z, t) dz <= P int V dz = 2 P b(t_n - t). With the radial
source mass 2 pi int_0^infty |d_z(q^2)| r dr <= 8 pi G ||grad^2 u(t)||_infty of 2.1 and Theorem 3(b),
m_phi - o(1) <= nu_n int_0^{t_n} int |d_z(q^2)| Psi_n dx dt <= 16 pi P G nu_n int_0^{t_n} H(t) b(t_n - t) dt.

2.8 Conservation structure (Proposition 4). eta solves d_t eta + b.grad eta = Delta_5 eta + d_z(q^2) and Gamma solves
d_t Gamma + b.grad Gamma = L Gamma. In d/dt int eta f(Gamma) the transport terms combine into a divergence, the source is
r^{-4} d_z K(Gamma) and integrates to zero in z for each r, and the diffusion terms follow from the integration by parts formula
of 2.7 with g = f(Gamma), Gamma(0,z) = 0. The convex approximations sqrt(s^2 + e^2) - e of |s| give (c) (the axis term has the
favourable sign); ||d_z(q^2)||_1 <= 2 ||grad u||_2 ||grad^2 u||_2 is finite at each time. For (b), test the eta equation with r^2,
with cutoffs justified by (DEC). Since L(r^2) = 0 and int r^2 d_z(q^2) dx = 0, the diffusion and the source contribute nothing, and the
transport term gives d/dt int r^2 eta dx = 2 int u^r omega^theta dx. With omega^theta = d_z u^r - d_r u^z and d_r(r u^r) + r d_z u^z = 0,
int u^r omega^theta dx = 2 pi int int [r d_z((u^r)^2)/2 - r u^r d_r u^z] dr dz = 2 pi int int [r d_z((u^r)^2)/2 - r u^z d_z u^z] dr dz = 0;
the axis boundary term of the radial integration by parts carries r u^r u^z and vanishes, and the terms at infinity vanish under (DEC).

2.9 Theorem 9. q solves (d_t + b.grad) q = Delta_5 q - 2 a q. Testing with 2 q r dx: transport gives + int a q^2 r dx (div b = 0, b.grad r = u^r),
stretching gives - 4 int a q^2 r dx, and radial diffusion gives - 2 int q_r^2 r dx - int q^2/r dx after radial integrations by parts
(int q q_rr r^2 dr = - int q_r^2 r^2 dr + int q^2 dr and int 3 q q_r r dr = -(3/2) int q^2 dr); the axis terms carry r^2 q q_r and r q^2 and vanish,
and the limits at infinity are taken with smooth cutoffs, using the integrability of r q^2, r |grad q|^2 and q^2/r (near the axis
q(r,z) = int_0^1 d_1 u_2(s r, 0, z) ds). Then 2 |q| |d_z q| <= (d_z q)^2 r + q^2/r. With B = 3 int_0^t Abar the identity reads
(e^B Sigma)' = - e^B (2 int |grad q|^2 r + int q^2/r), which gives the action bound. For (b): the source term of Theorem 3(b) equals
nu_n int int d_z(q^2) Psi_n; for each t, int d_z(q^2) dx = 0, so the positive and negative parts of d_z(q^2) have equal mass, and 0 <= Psi_n <= P gives
int d_z(q^2) Psi_n <= (P/2) ||d_z(q^2)||_{L^1}. For (c): Psi_n is transported by the same b, so the two drift terms combine into - int r b.grad(q^2 Psi_n) dx =
int a q^2 r Psi_n dx, which with the stretching gives the factor - 3; the extra diffusion term 2 int q^2 d_r Psi_n dx is integrated by parts in r and
completes a square, - 2 int r (d_r q + q/r)^2 Psi_n dx, which is dropped; and 2 |q| |d_z q| <= 2^{-1/2} (2 (d_z q)^2 r + q^2/r). For (d): ||eta_r||_{L^p(dx)} is nonincreasing
for 2 <= p <= infinity (the transport term vanishes, Delta_3 gives a negative term, the extra term (2/r) d_r gives -(4 pi/p) int |eta_r(0,z)|^p dz <= 0,
and p = infinity follows from the maximum principle); eta_0 is in L^2 and L^infinity because |eta| <= |grad omega| pointwise; the kernel bound
|u^r/r|(x) <= (3/(4 pi)) int_{R^3} |x - y|^{-2} |eta(y)| dy (known in this form, see Shirota and Yanagisawa, Proc. Japan Acad. Ser. A 70 (1994); a
proof follows) and Lorentz duality give ||u^r/r||_infty <= C ||eta||_{L^{3,1}}, and with ||f||_{L^{3,1}} <= 9 ||f||_2^{2/3} ||f||_infty^{1/3} this bounds
a_r. Proof of the kernel bound, for smooth rapidly decaying axisymmetric eta (the general case by density in L^{3,1}): since
Delta_3 (x_1 g(r, z)) = x_1 Delta_5 g, the canonical vector potential of r eta e_theta is r psi e_theta, where psi = N_5 * eta is the Newtonian
potential of eta regarded as a function on R^5 = R^4 x R, so u^r/r = - d_z psi and |u^r/r|(x) <= (3/(8 pi^2)) int_{R^5} |X - Y|^{-4} |eta(Y)| dY.
With a = r^2 + rho^2 + (z - y_3)^2, b = 2 r rho and s = (a^2 - b^2)^{1/2}, the average of |X - Y|^{-4} over the 3-sphere {|y'| = rho} of R^4 is
2/((a + s) s) and the average of |x - y|^{-2} over the circle of radius rho is 1/s; since dY = 2 pi^2 rho^3 d rho dy_3 and dy = 2 pi rho d rho dy_3,
the 5D integrand is at most 2 pi rho^2/(a + s) <= 2 pi times the 3D one, and 2 pi (3/(8 pi^2)) = 3/(4 pi). The Biot-Savart recovery is essential: u^r = c r, u^z = - 2 c z has eta = 0 and u^r/r = c. Finally Y = Sigma + int_0^t ||d_z(q^2)||_{L^1}
satisfies Y' <= 3 C_0 Y + 3 Pi_s, and Gronwall (valid for signed Pi_s) together with (b) gives the signed bound of (d); the positive-part
bound follows since the weights e^{3 C_0 (t_n - t)} lie in [1, e^{3 C_0 T_*}] and nu_n Sigma(0) -> 0.

## 3. Findings

F1. Several points in the reduction and the source estimates require care. (a) A nonzero axisymmetric test function cannot be supported in a
ball disjoint from the axis; solid tori are used instead. (b) Under (A), the near/far split of the pressure at the scale M/D proves the
pressure-Hessian bound and the differential inequality of Corollary (iv), but the latter is only a lower bound on the past gradient. (c) The
radial source mass is linear in G without logarithmic loss. (d) For the compactness reduction and the estimates using the normalized
historical Hessian bound, (A) is needed at the selected record times only (Theorem 5(c) and Corollary (iv) use (A) at all late times, as
assumed in the setting). (e) The fixed-z version of the integration by parts formula with the full Delta_5 is false (for eta = exp(-r^2 -
z^2), g = 1 at z = 0 the two sides are -3 and -2); only the radial version and its z-integral hold.

F2. The Euler limit carries no Liouville rigidity of its own: steady swirl-free pipe flows f(R) e_Z with f smooth and rapidly decaying
(for example f(R) = c e^{-R^2/s^2}, normalized so that |U| <= 1 and max |grad U| = 1) are bounded, smooth, nonconstant, axisymmetric,
swirl-free Euler solutions with |grad U| maximal at tau = 0 and ||omega(-A)|| constant in A. Hence an exclusion of Case 2 must use the
prelimit Navier-Stokes dynamics. The present WINDOW argument controls the prelimit only for A <~ (G nu_n)^{-1/2}, where its source
estimate, of order G nu_n A^2 including axial spreading, is small; beyond that range the arguments here give only the localization
statements of Theorems 3, 5, 6 and 8.

F3. Case 2 forces a quantified Type II scenario in which the critical quantity ||eta||_{L^1}, which is nonincreasing for
swirl-free flows, is at least of order 1/nu_n = M_n^2/D_n at t_n (no matching upper bound is claimed), and in which a fixed nonzero part of the terminal vorticity pairing is produced by the swirl source in the middle
history (Theorem 3(e)) within distance o((D_n M_n)^{-1/4}) of the axis when s_n -> T_* (Theorem 3(f)). The required production
is measured by the physical quantity int int q^4 >= c D_n M_n; in rescaled variables int int q_n^4 dy dtau >= c nu_n over the
rescaled middle history.

F4. The swirl source is invisible to every Casimir int eta f(Gamma) dx (Proposition 4(a)): its pairing with any function of
Gamma vanishes identically, and its z-integral vanishes for each r. Only the viscous terms change the Casimirs. The integrated Casimir
statements use (DEC); the local source cancellation does not. Signed Casimir
pairings cannot bound ||eta||_1, because they vanish when Gamma is even and eta odd in z; and a global sign of eta is not
preserved (a pure-swirl datum with z-dependent q_0 has eta_0 = 0 and d_t eta(0) = d_z(q_0^2), which takes both signs).
Three further exact forms of the circulation balance, none of which bounds it (all under (DEC)). (a) Nodal form. Write
C(t) = ||eta(t)||_{L^1(R^3)} = 2 pi int int |omega^theta| dr dz. At differentiability times t at which the zero set of eta(t) is a
regular surface of finite area carrying no zero plateau, the boundary traces exist and the entropy (coarea) limit of
int phi_eps(eta) dx can be passed (this is a hypothesis at such t, not a consequence of regularity alone; in general the identity
holds only as the inequality below), C' = P - D_nod - A with P = int sgn(eta) d_z(q^2) dx, D_nod = 2 int_{eta = 0} |grad eta| dS (three-dimensional area) and
A = 4 pi int |eta(0,z)| dz; on a vertical line with finitely many simple sign changes z_i, int sgn(eta) d_z(q^2) dz
= - sum_i [sgn eta]_{z_i} q^2(r, z_i), so net production sits on the sign changes of eta, and one sign change crossing all radii produces
at most 4 pi int_0^infty r min(Q^2, G^2 r^{-4}) dr = 4 pi G Q, Q = ||q||_infty. (Creation from a zero plateau is not captured with
sgn(0) = 0; in general only C(t) <= C(0) + int_0^t ||d_z(q^2)||_1 holds.) The bound P <= K (D_nod + A) is false under all the
normalized bounds: in rescaled variables (viscosity nu, delta = nu^{1/3}) take a fixed nonnegative background ring and, near the axis,
N ~ 1/(4 delta) disjoint cells q = delta Q_0(R/delta, (Z - Z_j)/delta), eta = delta^2 d_zeta(Q_0^2)(R/delta, (Z - Z_j)/delta),
Q_0 = F(rho) g(zeta) with smooth bumps F supported in (1, 2) and g in (-1, 1); then |U|, |grad U|, |grad^2 U| <= C, |Gamma| <= C nu,
P >= c nu, D_nod <= C nu^{5/3} and A = 0 at the initial time (D_nod and A now carry the factor nu). This is a changing-datum, instantaneous statement only. (b) Label form.
With xi = r^2/2 the meridional transport is area preserving and D eta/Dt = {Gamma^2, h} + Delta_5 eta, h = 1/(4 xi), {f, g} =
f_xi g_z - f_z g_xi, a Boussinesq-type system with unequal diffusions for eta and Gamma; inviscidly, on a regular level Gamma = s off the axis
(h is undefined at xi = 0) the coarea coordinate mu (d mu = d sigma/|grad Gamma| in the (xi, z) plane, oriented so that
d_mu X = (-Gamma_z, Gamma_xi)) is material and eta = eta_0 + 2 s d_mu int_0^t h(X(mu, tau)) d tau,
so growth of C requires variation of the r^{-2}-weighted residence time along swirl levels, which nothing here controls. (c) Half-plane
form. C_>(z_0) = int_{z > z_0} int_0^infty omega^theta dr dz satisfies d/dt C_> = int_0^infty (u^z omega^theta - d_z omega^theta - r q^2)(r, z_0)
dr - 2 int_{z_0}^infty eta(0, z) dz. The swirl flux K = int_0^infty r q^2 dr is nonnegative, at most G Q, and int_0^T int K dz dt =
(2 pi)^{-1} int_0^T ||q||_2^2 dt <= ||u_0||_2^2/(4 pi) (as |q| <= |grad u|), but the transport flux u^z omega^theta is not controlled.

F5. Literature (checked against the arXiv abstracts where marked). None of the criteria checked here has been shown to exclude Case 2:
Chen-Strain-Tsai-Yau II (Comm. PDE 34 (2009) 203-232; abstract checked) need |u| <= C|t|^{-1/2} or |u| <= C r^{-1+eps}|t|^{-eps/2},
which Case 2 violates (the first because a uniform bound |u| <= C (T_* - t)^{-1/2} gives |grad u(t)| <= C'/(T_* - t) by local smoothing of
mild solutions on intervals of length comparable to T_* - t, contradicting Corollary (i); the second because at the point of Corollary (vi), r = R_0 l_n and
|u| >= c M_n, while the condition with T_* - t_n >= c/M_n^2 would give r|u| <= C (r^2/(T_* - t_n))^{eps/2} <= C nu_n^{-eps}, which
is incompatible with r|u| >= c/nu_n for 0 < eps < 1 as nu_n -> 0); Lei-Zhang (arXiv:1505.02628; abstract checked) need
|r u^theta| <= C|ln r|^{-2} near the axis, and Wei (arXiv:1508.03318; abstract checked) |r u^theta| <= |ln r|^{-3/2}; neither
follows from |Gamma| <= G. The same abstract states global regularity when the supremum of |r u^theta|, initially or near the axis, is small relative to
dimensionless quantities of the datum. The initial version requires the initial circulation, hence G, to lie below a datum-dependent
threshold; the near-axis version requires uniform smallness of the circulation in a region near the axis and need not make the global G
small, but that smallness does not follow from the Case 2 hypotheses either (|Gamma| <= G and Gamma = O(r^2) at each fixed time give no
smallness uniform in time near the axis). Neither smallness condition has been established here. Further criteria (Chen-Fang-Zhang on r^d u^theta in L^p L^q with d < 1;
Pan on log-log bounds for b; Lei-Zhang on BMO^{-1} potentials; Kang-Miura-Tsai epsilon-regularity; Seregin's Type II
classification) were not checked against the journal texts here and are not used. Seregin, arXiv:2402.13229 (v3, read in full)
extracts an ancient Euler limit from a potential axisymmetric Type II point by a similar scaling under weighted energy, pressure
and second-derivative bounds on parabolic cylinders, shows (Proposition 2.2) conservation of the integral of |omega^theta/r|^{l_1/2}
in that class, and (Proposition 2.3, Corollary 2.4) excludes the singularity if in addition ess sup_t int |v|^{3/(2-m)} dx or
ess sup_t int |curl v|^{3/(3-m)} dx is finite on a fixed cylinder (the finite critical trace forces the limit to vanish at the final
time, and conservation propagates this backward); Sections 3 and 4 treat self-similar and discretely self-similar limits respectively. These weighted or critical bounds
have not been established for Case 2, and its record-time limit is not the terminal-trace limit used there. Seregin,
arXiv:2507.08733v2 and arXiv:2606.29468v1 (texts read; statements and the axisymmetric sections checked) work in the same class:
weighted local energy, pressure and second-derivative bounds with weight f(r) (r^{1-m} there, logarithmic in 2606.29468), an Euler
zoom producing a nontrivial ancient Euler limit, zero swirl of the axisymmetric limit, and conservation of int |omega^theta/r|^{l_1/2}
under a decay bound |u| <= c/(|x'| f(|x'|)); exclusions are obtained only under an extra Ladyzhenskaya-Prodi-Serrin type condition
(2507.08733, Theorem 5.1) or for parameter ranges where the weighted bounds force the limit to vanish. The full set of hypotheses of
these criteria has not been established for Case 2, and no exclusion is obtained from them here. The a priori bound
|u| <= C r^{-2} |ln r|^{1/2} of Lei-Navas-Zhang (arXiv:1309.6625; abstract checked) is weaker than (F3) at the record scale.
Exclusion of Case 2 is implied by global regularity of axisymmetric solutions with bounded Gamma, but no converse
(equivalence of Case 2 with the full axisymmetric problem) is known. Statements checked only against abstracts are literature leads
rather than verified applications.
Later papers of Shahmurov (arXiv:2606.07869v2, 2605.01875v4, 2604.03519v2, 2605.09797v3; texts read for the statements used) do not,
under the Case 2 hypotheses, supply upper bounds sufficient to exclude this branch through W, the L^1 production of eta, the pairing of
Theorem 3(b) or Q_4, and do not establish TARGET-2. Their applicable upper bounds concern other quantities. The pointwise swirl-energy
estimate (2606.07869, Proposition 10.1), together with |grad u(t_n)| <= D_n, bounds the swirl part of R^{-1} int_{B_R(a_n)} |u|^2 dx by
2 pi G^2 log(1 + 2 c^4/(3 G^2 nu_n^2)) = O(G^2 log(1/nu_n)) at R = c l_n (G > 0 and c > alpha_* fixed), while the total is of order nu_n^{-2},
consistently with the no-swirl limit; Theorem 10.2 there is the corresponding time-integrated occupation estimate. The source-free part of
Theorem 9(d) here is an L^2-L^infinity analogue of the fixed-tag strain estimate of 2606.07869, Theorem 7.1: for a source-free tag g that
theorem bounds the radial strain ||b_g^r/r||_infty (in its notation U = u^r/r) by C ||g(0)||_1^{1/3} ||g(0)||_infty^{2/3}, while Theorem 9(d)
bounds the source-free component a_r of u^r/r by C ||eta_0||_2^{2/3} ||eta_0||_infty^{1/3}; both concern radial strain, not velocity. The logarithmic
mechanism of 2604.03519, Proposition 7.2, has the following direct record-variable counterpart. For fixed G, K, L, R_0 > 0 and n large, the
caps |q_n| <= 1 and |R^2 q_n| <= G nu_n give, by splitting at R = (G nu_n)^{1/2},
int_0^{R_0} q_n^2 R^3 dR <= (G nu_n)^2 (1/4 + log(R_0 (G nu_n)^{-1/2})); on the fixed lifted cylinder Omega_0 = {|Y'| < R_0, |Z| < L} in R^5
consequently int_0^{K/nu_n} ||q_n^2||_{L^1(Omega_0)} ds <= C_{G,K,L,R_0} nu_n (1 + |log nu_n|), and the negative-norm argument of Lemma 7.3
there gives int_0^{K/nu_n} ||d_Z(q_n^2)||_{H^{-m}(Omega_0)} ds -> 0 for m > 7/2, H^{-m}(Omega_0) = (H_0^m(Omega_0))^* (a local estimate). This does not
control Theorem 3(b), whose pairing uses three-dimensional physical measure. In rescaled variables chi_n = psi_n/R^2 satisfies
d_s chi_n = b_n.grad chi_n + nu_n Delta_5 chi_n + 2 a_n chi_n (b_n = (U_n^R, U_n^Z), a_n = U_n^R/R, coefficients at rescaled time -s),
and no uniform H^m bound for this lifted test function on the growing age windows has been established. In the rescaled
three-dimensional measure the mass of q_n^2 is at most 4 pi C_*^{2/3} (G nu_n)^{4/3} per unit Z (F9); this yields the sufficient
axial-variation criterion of Theorem 8(b) but neither establishes that criterion nor gives another upper bound for the signed
differentiated-source pairing. The weighted families int |q|^p r^alpha dr dz (2605.01875,
Theorem 3.1) are free of the compression term only at alpha = 2p + 1 and scale critical only at alpha = 2p - 2 (Corollary 3.6), and
2606.07869 (Corollary 11.4) shows the same separation for circulation weights |Gamma|^p r^{-k}; this agrees with the failure of every
scalar weighted functional tried here. Case 2 records are meridional Type-II records in the terminology of these papers, and both
2606.07869 (Remark 10.8: the theorem does not "exclude the meridional Type-II record") and 2605.09797 (Section 7: such records are
"receiving branches rather than contradictions") state that this class is not excluded there.
Geometric criteria. None of the three sufficient conditions for regularity below has been established here from the Case 2
hypotheses. The elementary arguments given were checked here by hand; the three papers were read here for the statements used, and
their proofs were not checked. (a) Vorticity-direction coherence. Dascaliuc and Grujic (arXiv:1205.7080v1, Section 1) record the
local critical criterion of Grujic and Guberovic (Comm. Math. Phys. 298 (2010) 407-418): (x_0, t_0) is a regular point if
int_{t_0 - 4R^2}^{t_0} int_{B(x_0,2R)} |omega|^2 rho_{1/2,2R}^2 dx dt < infinity, where xi = omega/|omega| and
rho_{beta,L}(x,t) = sup {|xi(x,t) x xi(y,t)| |x - y|^{-beta} : 0 < |x - y| < L, omega(y,t) != 0}. In Case 2, curl U(.,0) is not
identically zero (otherwise each component of U(.,0) would be a bounded harmonic function, hence constant), and it vanishes on the
axis, so omega_U^theta(y_0, 0) != 0 at some y_0 with R_0 = |y_0'| > 0. By Theorem 1(b) there are d in (0, R_0/4) and h, c > 0 such
that, on the physical torus a_n + l_n {|R - R_0| < d, |Z - Z_0| < d} and for t_n - h/D_n <= t <= t_n, one has
c D_n <= |omega| <= sqrt(2) D_n and |xi^z| -> 0 uniformly as n -> infinity. If Q is the rotation by pi/2 about the axis, then
xi(Qx,t) = Q xi(x,t), |v x Qv|^2 = 1 - (v^z)^4 for every unit vector v, and |x - Qx| = sqrt(2) r <= C l_n. Since
l_n <= C(E_0) D_n^{-2/5} -> 0 (the ball of radius l_n/4 about a point where |u(s)| >= M_n/2, s <= t_n, carries |u(s)| >= M_n/4, so
E_0 >= (pi/768) M_n^5/D_n^3), one gets rho_{beta,L} >= c l_n^{-beta} on this packet for large n, and its contribution to the
integral with beta = 1/2 is at least c D_n^2 l_n^{-1} l_n^3 D_n^{-1} = c/nu_n -> infinity. Hence the integral over
R^3 x (T_* - delta, T_*) diverges for every delta > 0 and L > 0, and if a_n -> a_* along a subsequence, the local integral at
(a_*, T_*) diverges for every R > 0. (b) One-dimensional sparseness. Grujic (arXiv:1111.0217, Definition 4.1 and Theorem 4.2; the
vorticity form is stated there as a relabelling of the velocity form) excludes a singularity at T_* if, for every base time t close
to T_*, some sampling time s in [t + 1/(4 d_0^2 Omega(t)), t + 1/(d_0^2 Omega(t))] has the property that around every point x_0 the
super-level set {|omega(., s)| > d_0^{-alpha} Omega(t)} is linearly delta-sparse at some scale r <= 1/(2 d_0^2 Omega(t)^{1/2}) (it
occupies at most the fraction delta of some segment of length 2r centred at x_0); here Omega(t) = ||omega(t)||_infty, d_0 > 1 is an
absolute constant, delta = delta(x_0) is in (0,1), h = (2/pi) arcsin((1 - delta^2)/(1 + delta^2)) and alpha >= (1 - h)/h. On the
time windows of (a), Omega(t) lies between c D_n and sqrt(2) D_n and ||grad omega(t)||_infty <= sqrt(2) H_n <= sqrt(2) C_* D_n/l_n by
(A), so for fixed theta in (0,1) every point where |omega(t)| > (1 + theta) Omega(t)/2 is the centre of a ball of radius c_theta l_n
inside {|omega(t)| > theta Omega(t)}, while Omega(t)^{-1/2} <= C nu_n^{1/2} l_n; every segment through such a point of length
comparable to Omega(t)^{-1/2} therefore lies entirely in that super-level set. This refutes only a same-time version with a fixed
threshold fraction theta: the theorem uses a later sampling time, a threshold set by the earlier time, and a threshold fraction
d_0^{-alpha} tied to the sparseness constant delta, which may vary with the point. (c) Exterior critical control. Barker,
Fernandez-Dalgo and Prange (arXiv:2302.06509v2, Theorem A) prove that if (0,0) is a first-time singular point of an axisymmetric
finite-energy weak solution on R^3 x (-1,0), then limsup_{t -> 0} ||u(t)||_{L^{3,infty}(B(0, a^{1/2}) minus B(0, (-a t)^{1/2}))}
= infinity, where a = lambda_S(B(0,1)) > pi is the first Dirichlet-Stokes eigenvalue of the unit ball. After translation and
parabolic scaling, a uniform late-time weak-L^3 bound on B(a_*, r_*) minus B(a_*, (a (T_* - t))^{1/2}) therefore excludes a
singularity at (a_*, T_*). If a_n -> a_* and l_n (T_* - t_n)^{-1/2} -> infinity, take a bounded set K of positive volume at positive
distance from the axis on which |U(.,0)| >= v_0 > 0; for large n the set a_n + l_n K lies in that exterior region,
|u(t_n)| >= v_0 M_n/2 there, and the exterior weak-L^3 norm at t = t_n is at least c M_n l_n = c/nu_n -> infinity, as that theorem
requires. When the ratio does not diverge, this calculation supplies no uniform late-time bound for the exterior norm. The two
scalar diagnostics of Section 4 give l(eps) eps^{-1/2} = eps^{1/12} and eps^{-1/50}, so the scalar constraints permit both regimes.
A failure of a sufficient criterion is consistent with a singularity; none of (a) to (c) excludes Case 2.

F6. Recent literature (arXiv texts read). Constantin, Ignatova and Vicol (arXiv:2609.20762, Theorem 1.2) prove local
regularity for axisymmetric solutions with |u(t)| <= C l(t)/(-t) and |grad^2 u(t)| <= C/((-t) l(t)) for an Euler length l
(non-increasing, doubling, l -> 0, (-t)/l^2 -> 0). Their hypotheses imply the gradient Type I bound |grad u| <= C/(-t), and
their argument is the TARGET-2 mechanism (decay of the limiting potential vorticity along backward meridional trajectories),
with the decay supplied by that hypothesis. With l(t) = M(t)(T_* - t) and (A), the global version of their Hessian bound,
||grad^2 u(t)||_infty <= C/((T_* - t) l(t)), is equivalent, as a uniform late-time bound, to D(t)(T_* - t) <= C, which Case 2 violates by Corollary (i). So Case 2
cannot satisfy global versions of their matched bounds. Their theorem is local (bounds in a fixed ball, with an admissible Euler
length), and l(t) = M(t)(T_* - t) has not been shown to be non-increasing and vanishing; so this comparison does not decide whether
their local hypotheses hold or fail in some ball. Their potential-vorticity bound uses the Hessian hypothesis, not the gradient
bound alone. Zhang (arXiv:2604.07785, Theorem 1.1) proves regularity under the global one-sided bound u^r >= -C(T-t)^{-1/2} with
bounded r u_0^theta and regular finite-energy data. Case 2 provides no such bound; granting that theorem, any singular solution
must satisfy limsup_{t -> T_*} (T_* - t)^{1/2} ||(u^r(t))_-||_infty = infinity, which is consistent with the compression requirement
of Proposition 7. These are local suitable-weak and Leray-Hopf regularity theorems (CIV: axisymmetric suitable weak solutions on
B(1) x (-1, 0) with pressure in L^{3/2}, smooth on compact preterminal subsets; Zhang: global Leray-Hopf solutions with data in
L^2 cap L^infinity cap C^3 and bounded r u_0^theta). Smooth finite-energy Case 2 solutions fit those preterminal classes, but the required
matched local bounds or radial-velocity bound have not been proved. The anisotropic sequel of Constantin, Ignatova and Vicol
(arXiv:2609.20803, Theorem 1.3 and Remark 1.4; statements and the proof outline of their Section 1 read) assumes on a fixed parabolic
cylinder |d_r^a d_z^b u^r| <= C (-t)^{-1/2-a/2-(1/2-h)b} and the same bounds with an extra factor (-t)^{-h} for u^z and u^theta
(a + b <= 2, 0 < h < 1/2; radial length (-t)^{1/2}, axial length (-t)^{1/2-h}). These are again matched pointwise bounds in -t, and their
proof uses the decay of the limiting scalar in the remote past that these bounds supply, together with a comparison principle for
drift-diffusion equations with diffusion in only some of the variables. No implication from (A) or the Case 2 structure to these
componentwise bounds on a fixed parabolic cylinder has been established here (if they held there, Theorem 1.3 would make the point
regular), and the mechanism gives no bound on the middle-history production. As far as
checked, no published result excludes Case 2.

F7. Theorem 5 sharpens the localization of Theorem 3: the positive excess of the record vorticity above k_n is produced only at times when the instantaneous
Hessian is within a fixed factor of H(t_n), and only inside the super level set {eta > k_n}, near the axis. In the Euler limit
sup eta_U is constant in time, and Theorem 5(a) is its prelimit form on growing windows; it bounds the Hessian, not the gradient,
and is consistent with a slow decay of the gradient if the near-maximisers of eta approach the axis (it is not consistent with
TARGET-2, and by Theorem 1(d) TARGET-2 would already exclude Case 2). Theorem 5(c) leaves two alternatives: a super level set much longer than l_n along the
axis, or a production time at least of order l_n^2/G (rescaled (G nu_n)^{-1}); no upper bound on that time follows. The power-law
diagnostic of Section 4 is compatible with the second alternative at the level of scalar sizes, since there (G nu)^{-1} = eps^{-1/6}
is much smaller than D (T_* - t) = eps^{-1/3} and the Hessian stays comparable to H(t_n) over a production time C l_n^2/G.

F8. The adjoint forgets the terminal datum on the viscous time l_n^2 of the profile scale (Theorem 6), so production much older than
l_n^2 contributes little unless the older history carries correspondingly more q^4 or longer super level sets. Together with
Theorems 2, 3 and 5, the part of the signed pairing that no proved estimate makes negligible comes from ages between
A_max(n)/D_n ~ (G nu_n)^{-1/2}/D_n and l_n^2 times a power of Q_4/(D_n M_n) (Theorem 6), near the axis, with radial compression of
the swirl where it overlaps the adjoint (Proposition 7). On that band only persistence-or-production alternatives are proved
(Theorem 3(g), Theorem 5(b)). This is the range that the present estimates leave open. In rescaled time it is the band (G nu_n)^{-1/2} << |tau| <~ nu_n^{-1} (times the
same power of Q_4/(D_n M_n)),
where the rescaled flow is no longer close to the Euler limit in any proved sense and where the time-integrated rescaled source mass per
unit axial length over [tau, 0] has the upper bound 8 pi C_* G nu_n |tau|, which grows from order (G nu_n)^{1/2} to order one.

F9. Near the axis the obstruction takes a sharp form (Theorem 8). Far from the axis the swirl angular velocity is at most G nu_n/R^2 in
rescaled units, and a weighted adjoint energy (weight cosh((Z - Z_0)/S) e^{-2s/S}) shows that over ages up to Lambda/nu_n it produces at most C Lambda G^2 nu_n^{1/2} R_0^{-3} outside a tube of radius R_0
(Theorem 8(a)), hence o(1) outside a tube of radius nu_n^{1/6 - epsilon} for fixed Lambda and outside any fixed tube for Lambda = o(nu_n^{-1/2});
at older ages the same weighted estimate remains valid but need not be small at fixed R_0; the dissipation form of Theorem 8(a) gives an
age-independent far-field bound in terms of the normalized dissipation of the time set, uniformly bounded if D_n^3/M_n^5 is (an
additional hypothesis), and the age-weighted Q_4 estimates of Theorem 6 remain available. Inside, the swirl kinetic weight int q_n^2 2 pi R dR is at most 4 pi C_*^{2/3} (G nu_n)^{4/3} per unit length, so if the
ages up to K/nu_n carry a fixed fraction of the pairing, the age-integrated, w_nu-weighted axial total variation of the adjoint over those ages
must be at least of order nu_n^{-1/3} times the age range. One way to saturate this (a possible scenario, not a proved consequence) is an adjoint with
about nu_n^{-1/3} axial oscillations at the scale of the swirl core (G nu_n)^{1/3}, in phase with d_Z(q_n^2), over rescaled times of order
1/nu_n. The Hessian bound allows near-axis cells of that size (velocity nu_n^{2/3}, eta of order one) that are invisible at the profile scale.
Compression memory (Theorem 8(c)) ties a strong swirl core to recent radial compression, but only through the spatial supremum of
(u^r/r)_-; the axis barrier (Theorem 8(d)) controls the adjoint only for r < nu_n^{1/2} l_n, below the core. A coupled energy for
(J, eta) = (-d_z q, omega^theta/r) against the adjoint cancels the source but leaves -2 c d_Z(q^2) with c = d_R U^Z/R, the source again,
so it gains nothing; since the weighted (J, eta) energy is o(1) at the earliest time and at least 4 kappa^2 m - o(1) at t_n, an o(1) bound on
the adjoint-weighted whole-history integral of its full remainder, int_{-t_n D_n}^0 int [2 R (d_R a) J^2 + 2 R (d_R q)(d_Z a) J + 4 q c J] psi_n dy dtau
= o(1) (a = U^R/R), would exclude Case 2, but a bound on the last term alone would not.

A scale count makes the scenario concrete. From here to the end of F9 fix n, write nu = nu_n, U = U_n, q = U^theta/R,
eta = omega_U^theta/R, Gamma = R U^theta (so |Gamma| <= B := G nu), and set delta = (G nu / C_*)^{1/3} (the swirl crossover scale; not
the separation parameter of Theorem 3), Q_cap = 2 C_* delta, lambda_c = nu/delta^2 = C_* delta/G and T_c = 1/lambda_c, so that |q| <= Q_cap.
At the crossover radius delta the swirl velocity is of order delta^2 and
the Hessian is of order one also in cell units (lengths delta, velocities delta^2, times delta^{-1}); the rescaled circulation
|gamma_n| = |R U_n^theta|/nu_n is at most G, so the local swirl Reynolds number is bounded independently of n, and the poloidal cell Reynolds
number C_* delta^3/nu_n is of order G as well. In cell variables the coupled equations contain no small coefficient, and the dimensional
count permits production of order delta^3 = O(nu_n) per cell event (no construction is given here); order-one production would need of
order nu_n^{-1} such events with a positive signed mean, for instance about delta^{-1} cells along a unit length of axis renewed over about
nu_n^{-2/3} cell lifetimes. Since d_Z a = eta + c exactly and the axial integral of d_Z a over a unit segment is the change of a, which is
O(delta) where |a| <~ delta at the endpoints, positive tilt of order one on a set of fixed measure must be compensated by negative tilt elsewhere
(a = delta sin(Z/delta) has d_Z a >= 1/2 on a set of measure about 1/3); this gives no smallness of either sign set, and a proof would have to show
that the swirl and the adjoint cannot weight the two signs unequally over ages of order 1/nu_n.
Two exact restrictions are known. If the velocity and the initial circulation are axially periodic with period at most L_0 delta and share
the reflection symmetry (U^R, U^Z, Gamma)(R, -Z) = (U^R, -U^Z, Gamma)(R, Z), the production over ages K/nu_n is O(delta^j) for every integer j
(the auxiliary forced scalar h with (d_tau + U.grad - nu Delta_5) h = d_Z(q_n^2), h = 0 at the initial time, satisfies P = int h(0) phi, is odd
and periodic in Z, hence a j-fold axial derivative of a bounded periodic function, while |d_Z(q_n^2)| <= 4 C_*^2 delta); for
general axially periodic velocities the axial mean of h obeys d_tau hbar + R^{-1} d_R(R mean(U^R h)) = nu (d_RR + 3 R^{-1} d_R) hbar, so only
the radial eddy flux of h creates a mean. Weighted versions of the (J, eta) energy (weights R^alpha, functions of Gamma, of q, of the 5D
adjoint), pressure trades, the energy of the axial derivative of the velocity, and a Lagrangian (label) form of the production with its
exact viscous corrections were also tested; these calculations have not yielded the needed bound (each leaves a remainder that is critical
at the crossover radius or has no sign).

Core supply and cell relaxation. Several exact facts constrain the cells but do not bound their number. (a) Without flow, a saturated core
Gamma = B(1 - e^{-R^2/d^2}) (B = G nu_n) evolves into Gamma = B(1 - e^{-R^2/(d^2 + 4 nu_n h)}), so q(0, h) = B/(d^2 + 4 nu_n h): the core
retains the fraction d^2/(d^2 + 4 delta^2) after one core time T_c = delta^2/nu (one ninth for a core at the cap, d^2 = delta^2/2), and
q(0, h) ~ G/(4h) as h -> infinity (an exact diffusion model). (b) Under the additional hypothesis Gamma >= 0 (not part of Case 2),
u^theta >= 0 and |d_ZZ u^theta| <= C_* give |d_Z u^theta|^2 <= 2 C_* u^theta, hence J^2 <= 2 C_* q/R with J = -d_Z q (without the sign
hypothesis this fails: U^theta = eps R exp(-R^2 - Z^2) sin Z has q = 0 and J != 0 at Z = 0); the eta generated by the source in
one core time from zero initial value is at most 2 ||q|| ||J|| T_c <= 4 C_* G (this does not bound the total eta); eta is Lipschitz in Z with constant 2 C_*/R; and for the decaying induced velocity
||d_Z a||_{L^2(R^5)} <= ||eta||_{L^2(R^5)} (the multiplier k_z^2/|k|^2), with the corresponding L^2(R^4) estimate for each axial frequency. (c) In the stochastic representation of
Gamma (backward paths with Bessel-0 radial noise, killed at the axis), Gamma(x) = E[Gamma(X_h) 1(alive at h)]; with only |Gamma| <= B this gives
q(x) >= (B/R_0^2)[(1 + theta) P(rich landing) - P(alive)] (rich: Gamma >= theta B at the landing point, 0 < theta <= 1). In the globally linear
strain model U^R = a(tau) R, R e^{-int a} is a time-changed Bessel-0 process and the survival probability from radius R_0 over a horizon h is
1 - exp(-R_0^2/(4 nu I_h)) with I_h(tau) = int_{tau - h}^tau exp(2 int_s^tau a) ds. Under the additional hypothesis Gamma >= 0 and with
p_h = liminf_{R_0 -> 0} P(rich landing | alive), this gives q(0, tau) >= theta G p_h/(4 I_h(tau)), and, from |Gamma| <= B alone,
|q(0, tau)| <= G/(4 I_h(tau)) for every horizon h. These probabilities constrain circulation survival; they do not imply that every contributing path has seen radial
compression (Gamma survives a finite interval with a = 0, see (a)), and for spatially varying strain the random time change cannot be inserted
into the deterministic-time law without further analysis. Under a quantified supply hypothesis giving exactly q(0) >= theta G A/2 for a sustained
radial compression a = -A, the cap gives A <= 4 C_* delta/(theta G); an asymptotic version needs an error estimate on the same scale, and brief
strong compression of circulation-rich fluid is not excluded. These calculations suggest studying adjoint-weighted histories of J and d_Z a;
a precise sufficient estimate of that kind and a proof connecting it to the production pairing are not available. (d) Exploratory computations (axisymmetric Navier-Stokes with swirl at the cell scale in a prescribed meridional background; not
independently reproduced here, and their specification is not included) suggested relaxation to the Burgers state under spatially uniform
strain, and a nonzero mean production against a cell-scale weight under a maintained axial variation of the strain (externally imposed,
axially periodic, zero spatial mean); under a reflection symmetry with an even weight on a symmetric domain the signed export vanishes
exactly. This suggests that Burgers relaxation alone will not give P = o(1) and that the question is whether the coupled flow can maintain
cell-scale strain variation; no numerical lower bound, convergence certificate or conclusion about the Case 2 pairing is asserted. (e) No theorem
from the Burgers-vortex stability literature (Gallay-Wayne, Gallay-Maekawa, Maekawa-Miura-Prange) is applied here: to use one, its prescribed
strain, perturbation class, norm and size assumptions would have to be verified for the forced and possibly renewed cores considered here,
which has not been done. If a nonnegative functional of the swirl alone (such as int J^2, or a relative entropy of q or Gamma with respect to
that profile) vanishes at the initial Burgers profile and becomes strictly positive when an allowed meridional perturbation generates J, it
cannot be nonincreasing for every such perturbation, because a small meridional perturbation creates J at once; this does not rule out every
monotone functional of the swirl (||Gamma||_infty, and nondecreasing functions of this norm, are nonincreasing); if a
coupled perturbation energy such as E = int (eta^2 + J^2) d^5x can be proved to satisfy E' <= -(2A - C_cpl) E with a specified constant
C_cpl < 2A, it decays exponentially; no such estimate with coefficients controlled by the Case 2 assumptions is proved here. A
unit-scale irrotational background U^R = (-a_0 + beta Z) R, U^Z = 2 a_0 Z - beta Z^2 + beta R^2/2 (eta = 0, d_Z a = beta) contributes beta(2q + R q_R)
to the J equation, of amplitude G beta/C_* in the diffusive cell normalization (r = R/delta, s = nu tau/delta^2, q/(C_* delta), J/C_*), so smoothness
of the background yields no factor of delta (this and the harmonic field below are local polynomial fields; a localization must preserve the divergence, for example by cutting
off a stream potential).
(f) Sharp compression bound and a sustained fold. Write the backward circulation path started at radius R_0 at time t, absorbed at the axis, as
dR = (-a R - nu/R) ds + (2 nu)^{1/2} dW (W a standard Brownian motion, s the backward time, coefficients at time t - s). Then R_s^2 = exp(2 I_s) F(H_s) with I_s = -int_0^s a, H_s = int_0^s exp(-2 I_v) dv and F a squared Bessel process
of dimension 0 (dF = (8 nu F)^{1/2} dbeta), whose law at a fixed time u is c times a Poisson(R_0^2/c) sum of unit exponentials, c = 4 nu u. Hence,
under the additional hypothesis Gamma >= 0 at the landing time, q(x) >= (theta G nu / R_0^2) P_x(the path lands in {Gamma >= theta G nu} unabsorbed);
with only |Gamma| <= G nu the lower bound is (G nu/R_0^2)[(1 + theta) P_x(rich landing) - P_x(alive)], as in (c). For a constant compression a = -A, R_0^2 = nu/A and a window h
with A h >= max(log 2 / 2, log(rho (A/nu)^{1/2})), the landing probability beyond radius rho is at least c_0 = e^{-1}(1 - e^{-1/2}) > 0.144, so if Gamma >= 0 and the
probability of rich, surviving landings is at least p_* > 0 (p_* = c_0 when every landing beyond rho is rich), then A <= 2 nu/(p_* theta delta^2): a persistent, circulation-supplied compression of the core cannot exceed a fixed multiple of lambda_c.
For a general flow the time change H depends on F, and the bound holds only after subtracting the probabilities of leaving the compression
region and of landing outside the rich set; it does not say that rich fluid can never be strongly compressed later. At a simple axis zero z_0(t) of
a with k = d_Z a and V = U^Z(0, z_0(t), t) - z_0'(t), the axis identity gives p_RR = q^2 + nu Delta_5 a - V k there, and, if nu ||D^3 U||_infty = O(nu^{1/2} + nu^{alpha/2})
(any 0 < alpha < 1) after one unit of past time under the bounds of Theorem 1(b) and the canonical pressure (argued from a parabolic estimate for
D U with C^alpha forcing D^2 p, not proved here as a lemma), then p_RR -> 0 at a material zero; a zero need not be material. A harmonic exterior field (stream potential c_h (Z^2 - R^2/4), c_h a constant, eta = 0) supplies the constant d_Z a = -2 c_h near the axis, so cell-scale
strain variation need not be self-induced. Exploratory steady computations (cell units, finite cylinder, exact background fold a = A_f Z, axial velocity
U_0 - A_f Z^2, circulation supplied on inflow, self-induced flow included; not independently reproduced here) suggested that a
boundary-maintained fold can sustain nonzero production against a fixed smooth weight, as the counts allow; no numerical lower bound is asserted. Finally the cap gives sup_{Z, tau} int q^2 2 pi R dR <= 4 pi C_*^2 delta^4, so
|P| <= 4 pi C_* G nu delta int_0^{K/nu} V_nu(s) ds with the weight w_nu(R) = min(R/r_c^2, r_c^2/R^3), r_c = delta/2^{1/2}: an independent derivation of
the form of Theorem 8(b), with the same missing estimate.
(g) Supply comparison and multiscale escape. If U^R <= -A R on a cylinder {R < b, Z in I} during [t_0, t_0 + T] and Gamma >= g on its parabolic
boundary, where g = theta G nu (1 - exp(-R^2/h(t))) and h' = 4 nu - 2 A h (so that g is a subsolution of the circulation equation, since g_R >= 0),
then q(0, Z, t_0 + T) >= theta G nu / h(t_0 + T); once h has relaxed to within a factor 1 + eps of 2 nu/A this gives q(0) >= theta G A/(2(1 + eps)) and the
cap forces A <= 4 (1 + eps) lambda_c/theta. This is a statement about maintained, supplied compression; the bounds allow a short compression pulse
of order one on a circulation-rich core, so no instantaneous restriction follows. For the radial escape of the circulation and adjoint
paths across the octaves between R ~ delta and R ~ 1, the formal calculation below suggests that zero net radial flux need not determine an
effective radial process: the field with stream
function alpha eps^3 R cos(Z/eps), nu = eps^3, has zero net flux over every axial period and obeys the derivative bounds for small alpha, but on a
fixed annulus the formal two-term corrector calculation predicts for each path family the radial operator kappa f'' + (kappa - 2) f'/R,
kappa = 1 + alpha^2/2, hence exit probabilities in both directions of a Bessel process of dimension 2 - 2/kappa rather than of dimension 0
(convergence of the stopped processes and of their exit probabilities is not proved, the streamfunction needs a further modification near
R = 0 to define a smooth axisymmetric field, and nothing is claimed uniformly down to R ~ delta).
The formal calculation thus suggests that net flux alone need not determine the effective radial dynamics; pointwise drift bounds do give barriers
(R^{2-d} is a supermartingale barrier when the radial drift is bounded accordingly), and instantaneous streamline topology gives no material
bundle count for unsteady flow. A heuristic sufficient condition (norms, damping inequality and patch overlaps not specified here): if the active region is covered by O(1/delta) cell patches whose cell
energies N_i = ||eta_i||^2 + ||J_i||^2 (cell units) satisfy a damped inequality with total supply (initial plus forcing, over K/delta^2 cell times)
o(delta^{-3}), then P = o(1) by Cauchy-Schwarz; such supply bounds are not available for forced or renewed cells.
(h) Closed cells, strong strain and monotone moments. Three further mechanisms were examined. First, in a closed axially periodic cylinder
{R < b} of period L with U^R = 0, d_R U^Z = 0 and Gamma = G_b on the wall, the perturbation w = U - Omega R e_theta - V e_Z of the solid rotation
Omega = G_b/b^2 (V the conserved mean axial velocity) satisfies the exact identity E' = -nu int |grad w|^2 dx for E = (1/2) int |w|^2 dx (in the frame
rotating with Omega the Coriolis force does no work and every wall term vanishes), hence E(t) <= E(0) exp(-2 nu t/C_P) with a Poincare constant C_P of
order max(b^2, L^2); the period-mean eddy flux F = <U^R eta> obeys the exact identity F = -R^{-2} d_R(R <U^R (U^Z - V)>) and
int_0^T int_0^b |F| R dR dt <= C E(0)/(L nu) for every T. In a closed cell, sustained layers are therefore excluded
for every G and uniformly in the history length. The argument uses the impermeable wall: in the open near-axis region the local energy balance
contains boundary work, pressure work and incoming vorticity, and no cumulative bound on these is available, so it does not transfer. (A related
inviscid available potential energy relative to a profile with Gamma_0^2 increasing in R is exact, but viscosity adds terms of indefinite sign.)
Second, a strong-strain statement for the production holds only conditionally: the Feynman-Kac representation of q, whose equation is
(d_tau + U.grad - nu Delta_5) q = -2 a q, gives the factor exp(-2M) when every contributing path accumulates strain at least M over the window,
which does not follow from bounds on the instantaneous strain; and the alternating-slope count (if |f''| <= H on an interval I and f' takes, at N successive points of I,
values alternately >= sigma and <= -sigma, then 2 sigma (N - 1) <= Var_I(f') <= H |I|, so N <= 1 + H |I|/(2 sigma)) restricts dense trains of cells only once a cell-scale slope threshold has been
established independently. Third, for every smooth Cartesian-axisymmetric weight W(R, Z) (so W_R(0, Z) = 0) and every smooth axisymmetric divergence-free
field (swirl allowed) for which the displayed integrals converge absolutely, the integrations by parts are justified, all discarded
boundary terms at spatial infinity vanish, and the axis limits give precisely the axis term displayed (mere existence of the limits is not
enough: U = e_Z, W = (1 - e^{-R^2}) tanh Z gives 0 on the left and 4 pi for the displayed right side),
   int eta U.grad W dy = 2 pi int int [ (U^R)^2 (W_Z/R - W_RZ) + (U^Z)^2 W_RZ + U^R U^Z (W_RR - W_R/R - W_ZZ) ] dR dZ + pi int U^Z(0, Z)^2 W_Z(0, Z) dZ,
so that d/dtau int eta W dy equals this form minus int q^2 W_Z dy plus nu (int eta (W_RR - W_R/R + W_ZZ) dy - 4 pi int eta(0, Z) W(0, Z) dZ). For W = Z (assuming in addition a finite absolute axial moment of eta, which smooth finite-energy
data need not have, and the decay needed to differentiate it) the form is int a^2 dy + pi int U^Z(0, Z)^2 dZ >= 0: the swirl lowers the axial moment of eta and the poloidal flow raises it (the vortex-ring speed
identity). Pointwise positivity of the coefficient matrix forces W_Z to be nondecreasing in R, so no weight localized in R gives a pointwise
monotone moment, and the global moments involve energy-level integrals that do not see the blow-up scale. Restricting to divergence-free
fields does not help: the form is nonnegative for every smooth compactly supported axisymmetric divergence-free field if and only if the
coefficient matrix is positive semidefinite at every point with R > 0, since a negative direction e at an off-axis point x_0 is realized,
up to O(1/N), by the field with stream function R chi(R, Z) N^{-1} sin(N xi.((R, Z) - x_0)), xi perpendicular to e, chi a cutoff near x_0.
Among weights v(R) + Z w(R) the only sign-definite ones are c + d R^2 + a Z, and finitely many homogeneous linear constraints (for example
zero impulse, zero values of finitely many moments) do not restore a sign, by superposing disjointly supported such fields with a null
vector of the constraint matrix. For instance, with W = Z e^{-R^2} and the stream function R^4 exp(-R^2 - Z^2/(2 L^2)) the form equals
pi^{3/2} (3 - 16 L^2)/(27 L) while the squared L^2 norm is pi^{3/2} (L + 3/(16 L)) and the moment and the impulse vanish, so suitably normalized fields with
equal energy and equal nonzero swirl have opposite moment derivatives. These are instantaneous statements; a time-integrated inequality
along histories whose vorticity is generated by the swirl is not excluded by them. None of the three mechanisms yields the missing estimate. An exploratory time-dependent computation in
the closed cylinder (not independently reproduced here) relaxed to solid rotation, as the closed-cell identity predicts; its initial data were
symmetric under Z -> -Z, which makes the mean fluxes vanish identically, so it carries no information about
asymmetric layers.
(i) A multiscale cascade as a sharpness test. One way to show that the missing estimate cannot follow from kinematic information alone (bounds on the
poloidal field and a passive circulation 0 <= Gamma <= G nu) would be a prescribed poloidal field with cells at the octaves r_k = 2^k delta that
carries production of order one. The natural candidate fails. A cell of streamfunction A r_k R^2 sin(Z/r_k) has velocity, gradient and Hessian of
sizes A r_k, A and A/r_k, so the Hessian bound fails as r_k -> 0; with streamfunction A r_k^2 R^2 sin(Z/r_k) and fixed A the cell Hessian is uniformly
bounded, which permits C^{1,1} limits and does not imply C^2 compactness (a particular assembled limit is not constructed here). (Tapered strengths A 2^{-eta k} are not excluded by this.) Nor does a product of octave-wise exit probabilities estimate radial
escape: for the one-dimensional diffusion nu kappa f'' + nu (kappa - 2) f'/R on (0, 1), killed at 0 (p > 0, 0 < delta < 1), with kappa = 1 for R <= delta and
kappa = (R/delta)^p for R >= delta, the scale density is R for R <= delta and (delta^2/R) exp[(2/p)(1 - (delta/R)^p)] for R >= delta, so the
probability of reaching 1 before 0 from R = delta lies between 1/(1 + 2 e^{2/p} log(1/delta)) and 1/(1 + 2 log(1/delta)) and tends to zero,
although the product of the octave-wise factors 2^{-2/kappa_k} stays above exp(-2 log 2/(1 - 2^{-p})): a path returning inward meets every inner
octave. Eventual escape gives in any case no lower bound for the adjoint. Arrays symmetric under Z -> -Z give exactly zero signed
production against an even weight on a symmetric domain; against a general terminal weight reflection symmetry alone gives no exact
cancellation (for pure-swirl data u^theta = r e^{-r^2 - z^2} the source d_z(q^2) = -4 z e^{-2(r^2 + z^2)} is odd but pairs nontrivially with
a nonnegative weight supported in z > 0). Profiles such as sin(zeta) + beta cos(2 zeta) with suitable nonzero beta remove that parity
obstruction, but their signed production requires a separate calculation. Production per unit length then has the form C_* G nu pbar; exploratory runs with one to three octaves (not
independently reproduced here) gave nonzero values of pbar and no bound uniform in the number of octaves. Whether kinematic information
alone can give the missing estimate therefore remains open.

F10. The forward side of the production and its obstruction in a model (Theorem 9). Theorem 9 moves the difficulty to the forward dynamics
of the swirl. Using no information on the adjoint beyond 0 <= Psi_n <= P, Case 2 forces two things: a time integral at least c/nu_n of the
positive part of the self-compression rate in the scale-invariant functional Sigma, and a Sigma-averaged signed compression action of at least
(1/3) log(1/nu_n) - C. Shahmurov (arXiv:2604.21213v3, Theorem 3.1, Corollary 3.5, Theorem 7.1(i)) proves that a first singularity of the maximal
H^2 solution with bounded circulation forces the critical signed compression actions of his family (indexed by j >= 3/2; for 3/2 <= j < 2 under an
additional finite critical mass) to diverge; the proof uses the weighted swirl criteria of Chen, Fang and Zhang (DCDS 37 (2017)). The action of
Theorem 9(b) is the member j = 2 of that family, and Theorem 9(b) is a Case 2 quantitative refinement of this necessary condition along the record
times, obtained from the production identity and not from a continuation criterion; his family does not contain the adjoint-weighted action of
Theorem 9(c). Both statements are necessary conditions only. They would contradict nothing unless an upper bound on the action were available:
|Abar| <= ||u^r/r||_infty <= D(t), and in rescaled time the action can be collected over the whole rescaled history.
To test whether the sign structure of the swirl-to-strain map can bound the self-compression, drop the transport of eta_s (drift-free model).
Then a_s(t) = int_0^t K e^{(t-s) Delta_5} q^2(s) ds with K = - d_z (-Delta_5)^{-1} d_z, which on R^5 has symbol xi_z^2/|xi|^2 >= 0 (dX = pi r^2 dx).
(a) Energy weight. int_0^T int a_s q^2 dX dt = (1/2) int_0^T int_0^T <q^2(t), K e^{|t-s| Delta_5} q^2(s)>_{dX} ds dt >= 0, because e^{-lambda |tau|} is
positive definite. This is a centrifugal effect: from zero sourced data, the self-induced flow does net expansion work on the swirl kinetic energy
(int a (u^theta)^2 dx = pi^{-1} int a q^2 dX). It gives no sign on subintervals.
(b) Instantaneous response, Sigma weight. For frozen q, the immediate strain response to an increment d_z(q^2) of eta is K q^2. With
phi = (-Delta_5)^{-1} d_z f, int (K f) f r^2 dr dz = int |grad phi|^2 r^2 dr dz + (1/2) int phi^2 dr dz >= 0. This is the case alpha = 2 of Shahmurov's
Theorem 6.1 (for smooth rapidly decaying axis-compatible profiles and alpha > 1 his form is int |grad phi|^2 r^alpha dr dz + ((3 - alpha)(alpha - 1)/2)
int phi^2 r^{alpha - 2} dr dz, nonnegative for 1 < alpha <= 5 by the Hardy inequality, with no positive full-gradient gap at alpha = 5; at
alpha = 1 his formula contains a separate axis term int |phi(0, z)|^2 dz); it concerns the frozen instantaneous response, not the subsequent evolution.
(c) Memory, Sigma weight: a negative periodic example and a localized drift-free prescribed-swirl family with critical self-compression. Let k = 1/20, L_k = - d_rr - (3/r) d_r + k^2, g(r) = r^{1/2} exp(-(log r)^2/4)
(flat at the axis), h = L_k^2 g, B = (h^2 + g^2)^{1/2} and f = B(r) + h(r) cos(k z) >= 0. The steady response is a_s = K (-Delta_5)^{-1} f
= k^2 g(r) cos(k z). The Sigma-weighted work per unit axial length is 2 pi avg_z int a_s f r^2 dr = pi k^2 I_k, where
I_k = int_0^infty r^2 h g dr = (2 pi)^{1/2} (-1/8 + e^2/200 + e^8/160000) = -0.17402 < 0. (The substitution r = e^s turns the three terms of
L_k^2 = L_0^2 + 2 k^2 L_0 + k^4 into the Gaussian integrals -(2 pi)^{1/2}/8, 2 k^2 (2 pi)^{1/2} e^2 and k^4 (2 pi)^{1/2} e^8.) The energy-weighted work of
the same profile is pi^2 k^2 int (L_k g)^2 r^3 dr > 0.
The periodic statement above is proved. Placed at the saturation scale, q = alpha C_* delta chi(Z) f(R/delta, Z/delta)^{1/2} with a fixed axial
cutoff chi and a small fixed alpha, the profile satisfies the three spatial velocity bounds of Theorem 1(b) and the circulation bound in record variables
and gives, in the drift-free model started from zero sourced vorticity, rescaled self-compression work W_s >= c nu over the rescaled time 1/nu,
that is, physical self-compression nu int (Pi_s)_+ dt >= c, the order Theorem 9(b), (d) requires. This is proved in Appendix B: the whole-space
strain kernel, the error produced by the cutoff (including its action on the z-independent part B), uniform bounds on the induced poloidal
velocity, its gradient and its Hessian, the memory integral from zero data over the whole interval, and explicit constants; the work satisfies
W_s/nu = pi k^2 (-I_k) alpha^4 C_* G^3 (int chi^4) + O(delta).
The construction prescribes q and does not solve the swirl equation. Sustaining the profile would require forcing over about delta^{-2} cell
diffusion times. With transport, a_s also acquires a commutator term of no known sign. Under the cell assumptions of Theorem 9(e) the balance of
compression and diffusion gives a poloidal cell Peclet number of order one and the Hessian bound gives at most order G (in the localized model the
induced Peclet number is of order alpha^2 G^2 and can be small). The periodic steady example disproves a universal nonnegative
critical-weight work identity, and Appendix B shows that in the drift-free prescribed-swirl model the three Case 2 spatial velocity bounds
and the circulation bound alone do not imply the smallness nu_n int (Pi_s)_+ dt -> 0. Appendix C shows that they do not imply it either when
eta_s is transported by its own poloidal velocity, for a sufficiently small fixed amplitude alpha (q is still prescribed). In both families the velocity and its gradient tend uniformly to zero and there is no normalized gradient record; neither solves the Navier-Stokes system. The corresponding question
for the coupled evolution remains open.
Two limitations of the obvious method for the transported version. First, in cell variables the transport term of the Appendix B family
carries the fixed coefficient epsilon = alpha^2 G^2. A HEURISTIC count for a perturbative estimate around the drift-free solution with
growth epsilon s^{1/2} gives epsilon/delta at the terminal cell time delta^{-2}; keeping this estimate small would require alpha^2 <= c delta
for fixed G and a sufficiently small c, and with that amplitude the drift-free work is O(alpha^4 nu) = O(delta^2 nu) = o(nu). On a fixed
number of cell times the drift-free work is O(alpha^4 delta^2 nu). These counts do not prove a transported bootstrap, a transported work
lower bound, or the failure of other methods on the full window.
Second, a uniform bound on the vorticity ratio does not give a uniform velocity bound (PROVED): for L >= 1 put
Q_L = exp(-r^2) (z/L) exp(-z^2/L^2), H_L(s) = int_0^s exp(t Delta_5) Q_L dt and Psi_L = (-Delta_5)^(-1) H_L, with b^r = - r d_z Psi_L and
b^z = 2 Psi_L + r d_r Psi_L. The exact heat formulas give [exp(w Delta_5) Q_L](0, L/2) = (1/2)(1 + 4w)^(-2) (1 + 4w/L^2)^(-3/2)
exp(-1/(4(1 + 4w/L^2))) and sup ||H_L(s)||_infty <= (2e)^(-1/2) int_0^infty (1 + 4t)^(-2) dt = 1/(4 (2e)^(1/2)) for all L and s, while
Psi_L(L^2) = int_0^infty min(L^2, w) [exp(w Delta_5) Q_L] dw; restricting to 1 <= w <= L^2 gives, on the axis,
b^z(0, L/2, L^2) = 2 Psi_L >= [2 e^(-1/4)/(125 sqrt(5))] log L. This axially odd, transversally localized source has a primitive in z of size
L, unlike the source of Appendix B, so it obstructs only a velocity bound based on the vorticity ratio, not the transported statement.
Appendix C avoids both limitations: it expands around a modulated approximation built from transported periodic solutions rather than
around the drift-free solution, and it bounds the velocity error directly in the velocity formulation, without a bound on the vorticity
ratio.
Convection-free coupled model (literature). Deleting the convection terms b.grad from both the q and the eta equations, while keeping the
swirl feedback, gives the model of Hou and Lei (Comm. Pure Appl. Math. 62 (2009) 501-564, as described by Hou, Shi and Wang): in the notation here, d_t q = Delta_5 q - 2 a q,
d_t eta = Delta_5 eta + d_z(q^2), a = - d_z psi, - Delta_5 psi = eta. For the inviscid generalized version u_t = 2 u psi_z, - Delta psi_t = (u^2)_z,
with a Cartesian Laplacian, Hou, Shi and Wang (arXiv:0912.1316v2, Theorem 1.1, read here) prove finite-time blowup in a box under specified
mixed Dirichlet-Robin boundary conditions, a restriction on the Robin parameter, compatible H^2 x H^3 data with u_0 > 0 inside and u_0 = 0
on the boundary, and two weighted positivity conditions; their Theorem 4.1 proves blowup for a version with viscosity in the omega equation
only, on a semi-infinite cylinder, under additional boundary compatibility and parameter conditions and the requirement that the blowup
time furnished by the positivity conditions precede an explicit viscous time. Their mechanism is the alignment of
u with psi_z through (log u)_t = 2 psi_z, which is self-compression in the sense used here (2 psi_z = - 2 a). Returning to the axisymmetric
Hou-Lei model above, Gamma = r^2 q obeys d_t Gamma = L Gamma - 2 a Gamma (since r^2 Delta_5 q = L Gamma), so the bound |Gamma| <= G, which
in the full system comes from the convection term u^r d_r combining with - 2 a q into pure transport of Gamma, is lost (already at time 0:
at an interior maximum of Gamma_0 > 0 the rate d_t Gamma is positive where the compression - a is large enough). The circulation bound
enters many estimates here (for example S^2 <= G D, the source caps and the crossover radius (G nu_n)^{1/3} l_n of Theorem 8), though not
the Sigma balance or the bound C_0 on a_r; the scale count for the
critical cells of Theorem 9(e) saturates it without violating it, so at the level of that scale count the part of the convection effect
captured by |Gamma| <= G does not limit the self-compression. In the other direction, Hou and Li (arXiv:math/0608295v1, Section 1, read
here) give a rigorous depletion mechanism in which convection is essential, for the exact solutions u^theta = r u_1(z,t), omega^theta = r omega_1(z,t),
psi^theta = r psi_1(z,t) of the full axisymmetric Navier-Stokes equations (linear in r; the nontrivial members have infinite total
energy): with u~ = u_1 and v~ = - d_z psi_1 (the axis values of q and a) and their viscosity nu, the quantity E = (d_z u~)^2 + (d_z v~)^2
obeys E_t + 2 psi_1 E_z = nu E_zz - 2 nu ((u~_zz)^2 + (v~_zz)^2) in their periodic setting, hence a maximum principle; the terms produced
by differentiating the convection coefficient are needed for the cancellation (checked here by hand and in sympy, Section 5 (11)).
For the full equations put E = (d_z q)^2 + (d_z a)^2 on the axis, which reduces to the Hou-Li quantity in the exact class. The square
root of E has Hessian scaling: the rescaled quantity is E_n = (M_n^2/D_n^4) E, which Theorem 1(b) bounds by O(C_*^2), whereas a fixed-data bound
E <= sup E(0) would force E_n -> 0. Along the axis the swirl-strain terms cancel in the same way (using
d_z u^z = - 2 a there), but the evolution of E along the axis contains in addition 8 (d_z q)(d_z q_rr) + 8 (d_z a)(d_z a_rr) and the
pressure term - 2 (d_z a)(d_z p_rr), which vanish in the exact class (q and a do not depend on r there, and p_rr depends on t only) and
are not controlled by axis values; no estimate here makes them small. Off the axis, w = a + i q obeys
(d_t + b.grad - Delta_5) w = - w^2 - p_r/r, so the swirl-strain coupling still rotates (d_z q, d_z a) with angular speed 2q, but the
equation for d_z q acquires the term r((d_r a)(d_z q) - (d_r q)(d_z a)) and that for d_z a the pressure term - d_z(p_r/r). The direct
extension of the maximum principle to E = (d_z q)^2 + (d_z a)^2 taken at all points is false: take psi = (2 alpha - alpha r^2) z and q = k z near the origin (k > 0, alpha > 0 small),
cut off so that d_z a = 0 wherever d_z q is nonzero and sup E = k^2 is attained on {r < 1, |z| < 1}; this gives a smooth compactly
supported axisymmetric velocity, and on {0 < r < 1, |z| < 1} one has d_t E = 4 alpha r^2 k^2 > 0 at time 0 whatever the canonical
pressure, since d_z a = 0 there, so sup E(t) > sup E(0) for all sufficiently small t > 0.
After rescaling the datum to the crossover scale the relative growth rate is of the order of the local velocity gradient, the same order
as the other terms. Moreover E vanishes identically on the axis for every pipe flow
f(R) e_Z, so even E_n -> 0 would not by itself exclude a nonconstant limit. The Hou-Shi-Wang blowup results concern different operators or
boundary problems and inviscid or partially viscous equations, and the Hou-Li class consists of special exact solutions of infinite
energy; neither settles the fixed-datum whole-space Case 2 problem. These models motivate seeking a convection-dependent estimate; they
neither prove nor refute the bound in item (6) of the open questions (Section 4) for the actual whole-space solution.
(d) A coupled critical balance (a formal identity). Let psi be the canonical stream
function (a = - d_z psi, - Delta_5 psi = eta), A = - Delta_5, F = (1/2) int |grad psi|^2 r dx (critical, like Sigma), I = int a q^2 r dx,
D_q = 2 int |grad q|^2 r dx + int q^2/r dx, D_psi = int [psi_rr^2 + 2 psi_rz^2 + psi_zz^2 + (7 psi_r^2 + psi_z^2)/(2 r^2)] r dx >= 0,
h = A^{-1}(psi_r/r^2 + psi/r^3), chi = psi/r - h = A^{-1}(eta/r + psi_r/r^2), C = pi^{-1} int h_z q^2 dX and T = - pi^{-1} int chi b.grad(eta) dX.
The following identity holds for smooth axis-compatible fields for which the canonical inverses exist, all displayed integrals are finite,
differentiation under the integral is valid, and the boundary terms in the integrations by parts vanish as the radial, axial and axis cutoffs
are removed; the derivation is under these additional hypotheses, and their verification from the standing Case 2 assumptions (including the
construction of chi, the cancellation at r = 0 and the estimates at infinity) is an additional step not supplied here.
Then F' = pi^{-1} int chi d_t eta dX, and for every kappa, (Sigma + kappa F)' = - (D_q + kappa D_psi) + (kappa - 3) I + kappa (C + T). The source
contributes I + C, the diffusion - D_psi and the transport T. With kappa = 3 the stretching cancels. In Case 2 the critical
poloidal functional is large at the record. With K = int |b|^2 r^{-1} dx, the inequality (2 psi + r psi_r)^2 <= 8 psi^2 + 2 r^2 psi_r^2 and the Hardy
inequality int_0^infty psi^2 dr <= 4 int_0^infty r^2 psi_r^2 dr give K <= 68 F; rescaling about the axis point (0,0,z_n) gives
K(t_n) >= nu_n^{-2} int_B |U_n^p(y,0)|^2 R^{-1} dy for any ball B, and by the uniform convergence of Theorem 1 the right side is
c_U nu_n^{-2} (1 - o(1)) with c_U = int_B |U(y,0)|^2 R^{-1} dy > 0 when B contains a neighbourhood of the record point. Hence
F(t_n) >= (c_U/68) nu_n^{-2} (1 - o(1)), and integrating the identity with kappa = 3 and using Theorem 9(b),
int_0^{t_n} (C + T) dt >= (c_U/68) nu_n^{-2} (1 - o(1)) + (2 m_phi/(3P)) nu_n^{-1} (1 - o(1)) - (Sigma(0) + 3 F(0))/3. So any estimate
3 (C + T) <= epsilon (D_q + 3 D_psi) + e(t), with epsilon < 1 and int_0^{t_n} e = o(nu_n^{-2}), would exclude Case 2, provided the identity
holds along the solution (the verification described above, not supplied here). The bound on F(t_n) uses only
the nonconstancy of the limit (F of order (M_n l_n)^2 is the size of an Euler-strength structure of velocity M_n at scale l_n); by
F' = - D_psi + I + C + T it forces int_0^{t_n} (I + C + T) dt >= (c_U/68) nu_n^{-2} (1 - o(1)) - F(0), and by itself it says nothing about how
the swirl enters. C is the part of the source response that survives because r^{-1} does not
commute with A^{-1} (in the drift-free model T = 0 and C carries the indefiniteness of (c)); for a weight w the correction vanishes identically
only if w is constant, and r^{-1} is the only critical radial power. T is cubic and D_psi quadratic in psi: for the swirl-free datum
psi_* = z e^{-(r^2 + z^2)}, T[psi_*] = pi^2 (35299/82944 - (645 sqrt 2/2048) arctan sqrt 2) = 8.2523e-4 > 0, and since T[c psi_*] = c^3 T[psi_*] and
D_psi[c psi_*] = c^2 D_psi[psi_*] (D_psi[psi_*] = 15 pi^2/8), no instantaneous inequality T <= epsilon D_psi holds over arbitrary amplitudes, even
without swirl. This does not refute an estimate along normalized Case 2 histories or an integrated estimate with a separately controlled remainder. Whether such an absorption
holds along histories whose poloidal vorticity is generated by the swirl source is open: neither a proof nor a self-sustaining coupled
configuration is known. For the energy weight the coupled identity has no remainder, and from zero poloidal data the cumulative work
int_0^T int a q^2 dX dt = (1/2) int |grad psi(T)|^2 dX + int_0^T int eta^2 dX dt is nonnegative; but that weight is not critical.

F11. Published numerical candidates. One numerical candidate examined here is Hou's computation (arXiv:2107.06509v2) of a potential
singularity of the Navier-Stokes equations at an interior point of the symmetry axis. It uses a periodic cylinder with a no-slip wall at
r = 1, so it is not the whole-space finite-energy trajectory considered here, and its fitting interval has the fixed viscosity 5 x 10^{-3},
after a change from 5 x 10^{-4} at t_0 = 0.00227375. Section 3.4.1 (Figures 3.16 and 3.17) reports the qualitative fits
||u||_infty ~ (T - t)^{-1/2} and ||omega||_infty ~ |log(T - t)|/(T - t), and the author states that the resolution does not determine the
singular time, exponent and constant accurately enough to give a uniform velocity upper bound. If these were uniform asymptotic bounds of
the stated orders, they would give M(t)^2 <= C/(T - t) and D(t) >= ||omega(t)||_infty/sqrt2, hence D/M^2 >~ |log(T - t)| -> infinity,
incompatible with B2 (Theorem 1(a)); the computations do not establish those asymptotic bounds. Other numerical studies (Hou's Euler
computations, arXiv:2107.05870v2; the degenerate-viscosity model of Hou and Huang, arXiv:2102.06663v3; Hou's variable-viscosity models,
arXiv:2405.10916) were not checked here, and no classification of their branch properties is asserted. This comparison supplies no
verified example of Case 2 and no exclusion of Case 2.

## 4. Limitations and open questions

Use of the branch hypotheses. NO-SWIRL-EXTRACTION is used only to obtain B1 (Method 2.2), and B1 is used only to remove the swirl
of the unit-viscosity limit in the proof of B2 (it also gives U^theta = 0 in the Case 2 limit, which follows equally from
|U_n^theta| <= S/M <= (G nu_n)^{1/2}, a consequence of S^2 <= G D and B2). Later statements use NO-SWIRL-EXTRACTION only through nu_n -> 0; the scalar
diagnostics of this section list B1 among their constraints only to check consistency. In the reading of (W1) adopted in Section 1
(one K for all cylinders and all n), the union of the fixed normalized cylinders is the whole available past, so (W1) on a swirl record
sequence is equivalent to M(t_n) <= K S_n, and (W1) implies (W2) (the tail is at most 4 pi K^2/L). Hence NO-SWIRL-EXTRACTION is then
equivalent to B1: Method 2.2 gives one direction, and B1 gives M(t_n)/S_n -> infinity on every swirl record sequence, so no
subsequence satisfies (W1). In that reading the hypothesis carries no information beyond B1. If (W1) were read with
cylinder-dependent constants, or only for n beyond a cylinder-dependent index, the witness would be easier to satisfy, so
NO-SWIRL-EXTRACTION would be a stronger requirement; it still implies B1 (the witness built in Method 2.2 satisfies every such reading),
but the converse is not established by the argument above, and strict nonequivalence along actual trajectories has not been shown. In
such a reading every swirl record sequence, and every subsequence of one, must fail the chosen version of (W1) or fail (W2). With
cylinder-dependent constants, failure of (W1) means unboundedness on some fixed normalized cylinder. With one K but cylinder-dependent
starting indices, it means that for every K there is a fixed cylinder, possibly depending on K, on which the bound K fails for infinitely
many n; it need not mean unboundedness on one fixed cylinder (the time-independent fields n f/(n + f) e_Z, f = (1 + R^2)^{1/8}, are
bounded on each fixed cylinder uniformly in n, satisfy the tail condition with tail O(L^{-1/2}), and admit no such K; this is a
diagnostic of the quantifiers, not a solution). We found no use of that additional information. Since the rescaling W_n subtracts no axial drift, unboundedness
of |u^z|/S_n on a fixed normalized cylinder along the sequence already defeats the local witness (a fixed large value of the normalized
drift does not), so its failure carries little information on the swirl itself.
For every reading of the witnesses discussed above, a uniform velocity packet in the witness window forces every subsequence of a swirl
record sequence to fail at least one witness, so for such sequences NO-SWIRL-EXTRACTION adds no restriction beyond the Case 2 estimates
(derived by the second model and checked here; the existence of such swirl record sequences is not asserted). Let t_n be the gradient record
times and let s_n <= t_n be first-crossing swirl record times. In the record units of t_n write the swirl record radius and speed as d_n l_n
and b_n M_n, let c_n be its axis center in record coordinates, put sigma_n = D_n (s_n - t_n), and let theta be the swirl-normalized time of
the witness, so that the record time is tau_n(theta) = sigma_n + (d_n/b_n) theta and W_n(y, theta) = U_n(c_n + d_n y, tau_n(theta))/b_n (no
drift is subtracted in either rescaling). The change of variables X = c_n + d_n y gives int_{|y| > L} |W_n(y, theta)|^2 |y|^{-4} dy =
(d_n/b_n^2) int_{|X - c_n| > d_n L} |U_n(X, tau_n(theta))|^2 |X - c_n|^{-4} dX. On the whole past of t_n the caps of F9 give |U_n^theta|/R
<= 2 C_* delta_n and |R U_n^theta| <= G nu_n, with delta_n = (G nu_n/C_*)^{1/3}, so at the swirl record point b_n <= min(2 C_* delta_n d_n,
G nu_n/d_n). Since C_* delta_n^3 = G nu_n, this gives d_n/b_n^2 >= 1/(4 C_*^2 delta_n^2 d_n) >= 1/(4 C_* G nu_n) for d_n <= delta_n, and
d_n/b_n^2 >= (d_n/delta_n)^3/(C_* G nu_n) >= 1/(C_* G nu_n) for d_n >= delta_n. Suppose that there are A, m_0, rho, A_0, c_0 > 0 such that
for all large n some theta_n in [-A, 0] and a set E_n of volume at least m_0, with rho <= |X - c_n| <= A_0 on E_n, satisfy |U_n(X,
tau_n(theta_n))|^2 >= c_0 on E_n. Along a subsequence with d_n -> 0, for each fixed L eventually d_n L < rho, and the supremum over theta in
[-A, 0] of the tail is at least c_0 m_0/(4 C_* G A_0^4 nu_n), which tends to infinity, so (W2) fails. Along a subsequence with d_n >= d_0 >
0 (including d_n -> infinity) the packet lies in the fixed normalized ball |y| < R_0 for any R_0 > A_0/d_0, where |W_n| >= c_0^{1/2}/b_n >=
c_0^{1/2} d_0/(G nu_n), which tends to infinity, so (W1) fails even with cylinder-dependent constants and starting indices. Applying this
split to any further subsequence shows that none satisfies both witnesses. The packet condition holds for swirl records close to the
gradient records: by Theorem 1(b) and the continuity of U there are a closed ball E off the axis, a > 0 and h > 0 with |U| >= 2a on E x [-h,
0], hence |U_n| >= a there for all large n, so swirl record sequences with sigma_n in [-h, 0] and bounded centers c_n satisfy the condition
with theta_n = 0. Neither the existence of such swirl records nor a packet along growing backward ages or for escaping centers is
established, and the self-compression of Theorem 9 is not shown to occur at a swirl record.

Compatibility test (a non-NS diagnostic, not a solution). Put eps = T_* - t and D = eps^{-4/3}, M = eps^{-3/4},
H = eps^{-23/12}, G fixed. Then M H = D^2, nu = D/M^2 = eps^{1/6} -> 0, M <= C E_0^{1/5} D^{3/5} for small eps, M >= eps^{-1/2}
(Leray), and d(A) = 1 for every fixed A because A/D_n = o(eps_n). WINDOW holds trivially, TARGET-2 fails, and the budgets of
Corollaries (ii), (iii) are met. With ||grad u(t)||_2^2 ~ eps^{-1+delta} (0 < delta <= 1/12: integrable, and above the lower bound
D^5/H^3 = eps^{-11/12} that follows from ||grad u||_infty^5 <= C ||grad u||_2^2 ||grad^2 u||_infty^3) and ||q||_infty ~ (G H^2)^{1/3}, the size bound for int q^4 dx is ~ eps^{-23/9 - 1 + delta}, so the resulting upper budget for Q_4 over the
middle history is of order eps_n^{-23/9 + delta}, far above the requirement D_n M_n = eps_n^{-25/12} of Theorem 3. The listed
scalar growth and budget inequalities are mutually compatible in this diagnostic. It is not a Navier-Stokes solution or a simultaneous spatial
realization of all the estimates, and it does not rule out deriving a stronger bound from the kinematic assumptions; it shows only that a proof
of TARGET-2 or of Q_4 = o(D_n M_n) cannot come from these scalar inequalities alone and must use further structure (signs, transport
geometry, the coupling between Gamma, eta and the adjoint). The same diagnostic is compatible
with Theorems 5 and 6 and Proposition 7 when the production sits at ages of order l_n^2 (a non-NS spatial
model of this, a long truncated pipe flow with a swirl core of radius (G/H)^{1/3}, was examined as a consistency check; it is not a solution).
The exponent bookkeeping of all constraints was checked with a short script.

Time geometry of records. Two elementary facts hold. First, D(t)^2 <= 6 M(t) H(t) (symmetric Taylor expansion along a line, and the
largest singular value of a 3 x 3 matrix is at least its Frobenius norm divided by sqrt3), so with m_n, d_n, j_n the ratios of M, D, H at
time t_n - l_n^2 to their values at t_n, (A) at both times gives m_n j_n/(6 C_*) <= d_n^2 <= 6 C_* m_n j_n: along a subsequence either all
three ratios stay bounded below over the whole band of ages up to l_n^2 or one of m_n, j_n tends to 0; the dichotomy and the scalar
estimates used here do not select an alternative. Second, with g(t) = ||grad u(t)||_infty (instantaneous) and J_n = [t_n - l_n^2, t_n - sqrt(nu_n) l_n^2], a ball of radius
g(t)/(2 H_n) around a maximum point gives
int_{J_n} ||grad u||_2^2 dt >= (pi/(24 C_*^3)) (M_n^5/D_n^3) Lambda_n, Lambda_n = l_n^{-2} int_{J_n} (g(t)/D_n)^5 dt.
Since the left side tends to 0, instantaneous gradient persistence (g >= theta D_n on a fixed fraction of J_n) forces M_n^5/D_n^3 -> 0;
historical persistence alone need not imply instantaneous persistence (strict increase of D throughout the band is one sufficient
additional condition). In the other direction,
|q| <= |grad u|, int q^2 dx <= ||grad u||_2^2 and ||q||_infty <= 2 G^{1/3} H^{2/3} give
Q_4(J_n)/(D_n M_n) <= 4 G^{2/3} C_*^{4/3} (D_n^{5/3}/M_n^{7/3}) int_{J_n} (H(t)/H_n)^{4/3} ||grad u||_2^2 dt,
so the band contribution to Q_4 would be negligible if the weighted dissipation over J_n were o(M_n^{7/3} D_n^{-5/3}); finite dissipation
gives only o(1). Two fixed scalar histories (non-NS diagnostics, no spatial realization) show that these scalar facts do not decide the
band. With eps = T_* - t, T_* = 1, G = C_* = 1, put D = eps^{-a}, M = eps^{-b}, H = D^2/M, and assign scalar labels
e = 2 K_sc D^5/H^3 for ||grad u||_2^2, Q_2 = e/2 for int q^2 dx, Q_inf^2 = eps^{-(f - p)} (p = 3b - a) for ||q||_infty^2,
F = Q_inf^2 Q_2 for int q^4 dx and S = Q_inf^{1/2} for the historical swirl norm, with (a, b, f) = (5/4, 2/3, 37/12) (persistent: all three
ratios tend to 1 uniformly over the band, M^5/D^3 = eps^{5/12} -> 0) or (6/5, 18/25, 73/25) (intermittent: M^5/D^3 = 1, all three ratios at
age l_n^2 tend to 0). For each fixed K_sc >= 1, with a fixed energy budget E_0 > 100 K_sc + c_E chosen afterwards (c_E the constant of the
energy interpolation bound), these labels satisfy (A) (M H = D^2), B2, the lower blow-up bounds M^2 eps, D eps, H eps^{3/2} >= 1, D' <= 2 D^2,
the scalar energy balance E(t) = E_0 - 2 int_0^t e >= c_E M^5/D^3, the enstrophy bound e >= D^5/H^3, the swirl bounds
Q_inf <= D, Q_inf^2 <= 4 G^{2/3} H^{4/3}, S^2 <= G D, B1 (S/M -> 0) and WINDOW uniformly, and give Q_4(J_n)/(D_n M_n) -> K_sc and
25 K_sc/48 respectively, while int_{J_n} e -> 0. They are not spatial realizations and encode neither the full NO-SWIRL-EXTRACTION
hypothesis nor the signed production identity. The exponents and limits were checked exactly with a short script.

Inherited material properties of the Euler limit. The volume argument of 2.5 shows that a transported torus cannot lie entirely at a
uniform radius o(s^{-1/2}) at age s; it does not exclude radius of order s^{-1/2}, and three further facts block a material route.
(a) Locally uniform convergence on fixed windows does not identify prelimit material origins at growing ages. Let f(R) = -k R^2/2 (k > 0)
on a core R <= R_*, smoothly cut off; let g be smooth with g = 0 on (-infinity, 0], 0 <= g' <= 1, g' = 1 on [1, infinity), and
v_n(s) = n^2 + g(s - n^2), a_n = v_n'/(2 v_n). The stream functions int_0^R rho f(rho) d rho - a_n(s) R^2 Z chi(R) zeta(Z/v_n(s)), with fixed
cutoffs chi, zeta equal to 1 on the region swept by the trajectories, define a kinematic family (not NS) of smooth divergence-free fields
with bounds on velocity and two derivatives uniform in n and s (a_n v_n <= 1/2, each Z-derivative of zeta(Z/v_n) gains 1/v_n). It equals the
steady pipe flow f(R) e_Z (eta = k on the core) for ages s <= n^2, and carries every backward trajectory from a fixed off-axis torus to radius
n^{-1/2} R_0 at an age n^3 + O(1) (R^2 = n^2 R_0^2/v_n); with the assigned model parameter nu_n = n^{-4} this age is of order nu_n^{-3/4}, while
all limiting trajectories keep their radius. (b) Volume preservation, transport of eta, meridional Kelvin circulation and a uniform bound on
the kinetic energy inside a transported packet do not by themselves exclude axis approach: the polynomial field b^R = a(t) R,
b^Z = -2 a(t) Z - k R^2/2 (spatially unbounded, infinite total energy) solves Euler exactly (pressure -(a' + a^2) R^2/2 + (a' - 2 a^2) Z^2)
with eta = k, and for a = 1/(2(1 - t)) a torus keeps its volume (unit Jacobian), its eta values and its Kelvin circulation, and has bounded
packet energy, while every radius decays like s^{-1/2} and its axial extent grows like s. (c) Diffusion invalidates material tagging on the
relevant scales: the exact NS pipe flows u^Z = delta^4 (2w)^{-1} e^{-R^2/w}, w = delta^2 + 4 nu sigma (delta an independent initial width;
infinite axial extent), have eta = delta^4 w^{-2} e^{-R^2/w}, constant fluid radii, and physical eta-mass per unit length pi delta^4/w,
decreasing at the rate 4 pi nu eta(0) through the axis, while the four-dimensional (lifted) mass is constant. Conditional statements that
would close this route, neither established for the Case 2 packet: for a packet E of positive volume with backward flow X_s,
R(X_s(a)) -> 0 for almost every a in E together with lim_{L -> infinity} sup_{s >= 0} |X_s(E) cap {|Z| > L}| = 0 contradicts
|E| <= |{a in E: R(X_s(a)) >= rho}| + 2 pi L rho^2 + |X_s(E) cap {|Z| > L}|; and approach of each path to the axis along some sequence of
backward times together with lim_{rho -> 0} sup_{tau <= 0, Z, 0 < R < rho} |eta_U| = 0 forces eta_U = 0 on the packet.
These models (checked exactly in sympy) are tests of single implications; none realizes the production of Case 2.

Limitations of the estimates developed here: backward ODE integration of D gives only lower bounds; the
Euler limit has no Liouville rigidity (F2); sup-norm control of the adjoint gradient loses to transport stretching; the
Casimir cancellation (F4) is exact but its viscous terms have no sign and no available bound; the L^2 energy of q obeys
(1/2) d/dt ||q||_2^2 + ||grad q||_2^2 + 2 pi int q(0,z)^2 dz = -2 int (u^r/r) q^2 dx, whose right side (radial compression) is
uncontrolled; a normalized dissipation cost of order log(1/nu_n) corresponds to a physical cost O(D_n^{-1/5} log D_n), which tends to zero, so
this per-window estimate alone gives no contradiction with finite total dissipation, and no argument controlling the number, disjointness
or cumulative cost of such windows has been established.

Why the near-axis bound of Theorem 8(b) is not available (all checked here). (i) There is no total-variation contraction: f = d_Z psi_n solves
f_s = U^R f_R + d_Z(U^Z f) + nu L f + (d_Z U^R) d_R psi_n, and the last term creates axial variation from radial variation, already in the exact
leading near-axis model U^R = -(1/2) b_Z(Z, tau) R, U^Z = b(Z, tau). (ii) The near-axis variation T_rho = int_{R < rho} |d_Z psi_n| dy has, besides the
flux through R = rho, the interior source |d_Z U^R| |d_R psi_n|. (iii) The axis does not shield the crossover radius: for the radial operator
nu (d_RR - R^{-1} d_R) + A R d_R the harmonic profile is (1 - e^{-A R^2/(2 nu)})/(1 - e^{-A rho^2/(2 nu)}), and an outward strain A of order
nu/delta^2 = nu^{1/3} already removes the factor delta^2/rho^2; a compressive strain gives an exponentially small factor only if it extends over radii much
larger than (nu/|A|)^{1/2}; the Lipschitz bound |a(R, Z) - a(0, Z)| <= C_* R guarantees a compression of size |A|/2 out to radius |A|/(2 C_*)
but gives no upper bound on its radial extent, and nothing in the bounds forces either an outward or a compressive strain. (iv) The heuristic that the
Hessian bound limits the stretching near a swirl core to (C_*/G)^{2/3} nu^{1/3} is true for the stationary Burgers core but false in general:
an order-one strain pulse of unit duration on a wide circulation-saturated core satisfies all the bounds. (v) Material and residence-time
reformulations of the production (flux of q^2 through material surfaces, the time the fluid ending in supp phi spends near the axis) reproduce
the same requirement and add nothing. (vi) A restricted straight-channel estimate (proved). Fix
G > 0, put delta = (G nu_n/C_*)^{1/3}, and let U be smooth, axisymmetric and divergence-free with |grad U| <= 1 and |grad^2 U| <= C_*.
Fix 0 < a < b, c_0, l > 0 independently of delta, let 0 < rho <= c_0 delta < a and I = (z_0, z_0 + l delta), and suppose that throughout the ages considered
U^R >= 0 on [rho, b] x I and U^Z = 0 on the two fixed sides Z = z_0, z_0 + l delta for rho <= R <= b. Then at each time the flux
2 pi R int_I U^R dZ is independent of R and lies between 0 and (pi C_*/2) rho^4 (integrate incompressibility over {R < rho} x I and use
|d_R U^Z| <= C_* R), and U^R and |U^Z| are O(delta^2) on a <= R <= b. For the auxiliary adjoint problem on (a, b) x I with zero initial
data, zero side values, reflection at R = a and outer values in [0, 1] (rescaled age s, psi_s = U.grad psi + nu_n (psi_RR - psi_R/R + psi_ZZ)),
the value at R = a is at most 4 exp(-kappa (b - a)/delta) at every age, with kappa > 0 depending only on a, b, c_0, l, C_*, G. Proof: write
nu_n = mu delta^3, mu = C_*/G, and fix B (depending only on a, b, c_0, l, C_*) with |U^R|, |U^Z| <= B delta^2 on [a, b] x I. Put
beta = 1 + B/mu, cbar = 1/(2 (exp(beta l/2) - 1 - beta l/2)), f(x) = 1 - cbar (exp(beta |x|) - 1 - beta |x|) for |x| <= l/2 and
lambda = cbar mu beta^2. Then f is C^2, 1/2 <= f <= 1, and mu f'' + B |f'| = - cbar beta (mu exp(beta |x|) + B) <= - lambda (since
beta mu = mu + B). Choose kappa > 0 with B kappa + mu kappa^2 <= lambda/2 and put, with x = (Z - z_0)/delta - l/2,
W(R, Z) = 2 f(x) cosh(kappa (R - a)/delta)/cosh(kappa (b - a)/delta). Since W_R >= 0, |W_R| <= (kappa/delta) W and nu_n/delta^2 = mu delta,
U.grad W + nu_n (W_RR - W_R/R + W_ZZ) <= delta (2 cosh(kappa (R - a)/delta)/cosh(kappa (b - a)/delta)) ((B kappa + mu kappa^2) f + B |f'| + mu f'')
<= - delta lambda W/2 < 0. Moreover W_R(a, Z) = 0, W(b, Z) = 2 f >= 1, W >= 0 on the sides and at age 0, so the comparison principle on the
bounded domain (R >= a > 0, all coefficients bounded) gives psi <= W, and W(a, Z) <= 2/cosh(kappa (b - a)/delta) <= 4 exp(-kappa (b - a)/delta).
This excludes order-one
transmission in that auxiliary channel model only. It does not bound the unrestricted adjoint (already for U = 0 the side conditions
hold, and for a fixed nonzero terminal packet phi >= 0 the whole-space adjoint psi(s) = R^2 exp(nu_n s Delta_5)(phi/R^2) is positive at a
fixed point with R = a at ages s = t/nu_n, t > 0 fixed, independently of delta), and it does not exclude alternating contrasts in a
general comb: diffusion across and back through fixed straight material sides, excursions through the core, curved, tapering,
branching, recirculating or moving connections, and variation created inside the core remain uncontrolled.
(vii) A local modulation example and an averaged strain constraint (proved). In cell units
(length delta, time 1/(C_* delta), dimensionless viscosity 1/G, z of period 2 pi) let chi be a smooth radial cutoff equal to 1 for r <= 1
and to 0 for r >= 2, b_1 >= 0 a smooth pulse supported in (0, 1) with integral 1, b_2(t) = b_1(t - 2), and take the meridional field with
Stokes stream function (eps r^2/2) chi(r) (b_1(t) cos z + b_2(t) sin z), radial swirl data gamma(0) = F and radial terminal adjoint data
Psi(3) = H, where F = H = 1 - e^{-r^2} for r <= 3, cut off smoothly to 0 for r >= 4. Without viscosity the production
-2 pi int_0^3 int int gamma^2 r^{-3} d_z Psi dr dz dt equals 2 pi^2 J_chi eps^2 + O(eps^3), J_chi = int chi^2 F F' H' r^{-1} dr > 0: the first
variations are gamma_1 = (r chi F'/2) d_z W_p and Psi_1 = -(r chi H'/2) d_z W_f, where p_i = int_0^t b_i, W_p = p_1 cos z + p_2 sin z and
W_f = (1 - p_1) cos z + (1 - p_2) sin z are the past and future time primitives of f = b_1 cos z + b_2 sin z (the velocity is
u^r = -eps r chi d_z f/2, u^z = eps (chi + r chi'/2) f, so the axial displacement itself carries the factor chi + r chi'/2), the terms
F^2 d_z Psi_1 and F^2 d_z Psi_2 integrate to zero in z, int_0^{2 pi} d_z W_p d_zz W_f dz = pi (p_1 - p_2), and int_0^3 (p_1 - p_2) dt = 2. Weighted C^3 bounds for the lifted equations
of Q = gamma/r^2 and X = Psi/r^2 (with d = 1/G and a = u^r/r these are Q_t + u.grad_5 Q = d Delta_5 Q - 2aQ and
-X_t = u.grad_5 X + d Delta_5 X + 2aX; weight (1 + r^2)^3, maximum principle for sums of squared derivatives on the fixed interval
0 <= t <= 3, then a C^1 difference estimate with forcing d Delta_5 of the inviscid solutions) make the viscous change O(1/G), so the production is at least pi^2 J_chi eps^2 for G >= G_0. Rescaled to length
delta, with circulation lambda G nu_n and adjoint amplitude p (eps and lambda small and fixed), the field and the swirl satisfy
|U|, |grad U| = o(1), |grad^2 U| <= C_*, the Hessian bound for the swirl velocity and |Gamma| <= G nu_n, and the production is at least
c delta^2 per unit axial length over a time of order 1/(C_* delta), the same order in delta as the bound of Theorem 8(b) over that time.
So no estimate that uses only the pointwise bounds on one cell during one such time can improve the order of Theorem 8(b). The example is
axially periodic, its terminal adjoint is a radial profile at scale delta rather than the transported packet, nothing in it supplies or
renews its radial data, and it violates the eta equation (the prescribed pulses are not induced by the vorticity that the swirl generates).
For a fixed smooth periodic history f(z, t) on [0, T] with stream function (eps r^2/2) chi(r) f(z, t), the same radial data and no
viscosity, the quadratic coefficient of the production is eps^2 pi J_chi int (int_0^T W_p dt)_z d_zz W_T dz, where W_p(t) = int_0^t f and
W_T = W_p(T) (use W_f = W_T - W_p and int d_z W_p d_zz W_p dz = 0); it vanishes when W_T = 0, its size is governed by the time integral of
W_p, which can accumulate for time-varying histories as well as during a stationary hold, and no remainder estimate uniform over growing
histories is proved. Separately, every smooth axisymmetric divergence-free field with |grad^2 U| <= C_* satisfies
|l^{-1} int_I (a(R, Z) - a(0, Z)) dZ| <= C_* R^2/(4 l) on every interval I of length l (integrate d_R(R^2 a) = -R d_Z U^Z over I, use
|U^Z(R, Z) - U^Z(0, Z)| <= C_* R^2/2 and subtract the axis limit), so if, throughout a transfer, a is independent of Z on a fixed cylinder {R <= r_*} x I, |a(0, Z)| <= lambda delta there, and the
particle stays in that cylinder (r_*, l, c, lambda > 0 independent of delta), then |dR/dtau| <= R (lambda delta + C_* R^2/(4 l)) and the
transfer between radius c delta and r_* takes time at least (log(1/delta) + O(1))/(2 lambda delta); this does not constrain axially
varying transfers, paths that leave the cylinder, or overlapping transfers.
(viii) Axial shear histories (proved). Suppose that on the window -K/nu_n <= tau <= 0
(K >= 1) the rescaled meridional field is an axial shear, U = v(R, tau) e_Z with v smooth and bounded, that phi is supported in
{R >= R_B} with 0 < R_B <= 1, and put M_phi = sup_R int |d_Z phi(R, Z)| dZ. Then for every bounded smooth circulation gamma on the window
that vanishes on the axis, solves the circulation equation d_tau gamma + v d_Z gamma = nu_n (gamma_RR - R^{-1} gamma_R + gamma_ZZ) and
satisfies |gamma| <= G (a freely prescribed bounded function is not covered), the production of the window satisfies |P| <= pi M_phi G^2 nu_n R_B^{-2} (1 + (1/2) log(2K)). Proof: since v does not
depend on Z, d_Z psi_n solves the adjoint equation, so |d_Z psi_n| is at most the solution with data |d_Z phi|, whose axial integral
H(R, s) solves H_s = nu_n (H_RR - R^{-1} H_R) with zero axis value; since 1 and R^2 are stationary supersolutions,
int |d_Z psi_n(R, Z, -s)| dZ <= M_phi min(1, R^2/R_B^2) <= M_phi R_B^{-2} min(1, R^2) at every age. Without radial velocity,
G (1 - exp(-R^2/(4 nu_n t))), t the time elapsed since the start of the window, is an exact Z-independent solution of the circulation
equation that dominates |gamma| as t -> 0+, so |gamma| <= G (1 - exp(-R^2/(4 nu_n t))) (compare first with
(G + eps)(1 - exp(-R^2/(a + 4 nu_n t))), a small, and let eps, a -> 0). Insert both bounds in |P| <= int int nu_n^2 gamma^2 R^{-4}
|d_Z psi_n| dy ds, substitute t = a'/nu_n and use int_0^K (1 - exp(-R^2/(4 a')))^2 da' <= min(K, R^2/2); the radial integral
int_0^infinity min(1, R^2) R^{-3} min(K, R^2/2) dR equals 1/2 + (1/4) log(2K) (valid for K >= 1/2). The same comparison gives, for
delta = (G nu_n/C_*)^{1/3} <= 2^{1/2} (that is r_c <= 1, true for all large n),
V_nu(s) <= (1/2) M_phi R_B^{-2} delta^2 (3/4 + log(2^{1/2}/delta)) for every age 0 <= s <= K/nu_n of the window, far below the threshold of Open (5). The class is far from
Case 2: without radial velocity the near-axis circulation is depleted by diffusion (|q| <= G/(4t)), in line with the compression
requirement of Theorem 9, and the hypothesis concerns the prelimit histories, so it does not exclude a shear as the rescaled limit
(radial velocity at the cell scale is invisible in the limit). The arguments given here establish no comparable bound for general
steady or time-periodic meridional histories. A closed-streamline constancy argument of Prandtl-Batchelor type would need a separately
stated stationary problem with regular-limit hypotheses off the axis (no such lemma is stated or used here, and the classical literature
was not consulted); no quantitative rate, and no estimate reaching the core (whose dimensionless viscosity 1/G does not tend to zero), is
established here.
(ix) Higher derivative bounds (proved). Uniform bounds on
any fixed number of derivatives of U do not remove meridional structure at the cell scale. Let chi be smooth, equal to 1 on [0, 1] and
to 0 on [4, infinity) and independent of delta, fix eps > 0 and let 0 < delta < 1/4. The Stokes stream function S =
eps chi(R^2 + Z^2) (R^2 Z^2/2 + R^4/4 - delta^2 R^2/2) defines a smooth, compactly supported, axisymmetric, divergence-free field whose
Cartesian derivatives of each fixed order k are bounded by A_k eps, A_k = A_k(chi) independent of eps and delta (U^R = -R^{-1} d_Z S,
U^Z = R^{-1} d_R S); in R^2 + Z^2 < 1 it equals U^R = -eps R Z,
U^Z = eps (Z^2 + R^2 - delta^2), so grad^3 U = 0 there. It has axis stagnation points Z = -delta, delta and a meridional center at
(delta, 0); the arc R^2 + 2 Z^2 = 2 delta^2, R > 0, is a trajectory with the two stagnation points as limiting endpoints, and together
with the axis segment between them it encloses the center. With Psi(r, z, sigma) = psi(delta r, delta z, sigma/delta) and nu = mu delta^3,
mu = C_*/G, the adjoint equation becomes, in the rescaled core r^2 + z^2 < delta^{-2},
Psi_sigma = eps (-r z Psi_r + (z^2 + r^2 - 1) Psi_z) + mu (Psi_rr - r^{-1} Psi_r + Psi_zz), whose coefficients do not depend on delta.
So uniform derivative bounds on U do not exclude recirculation at the cell scale with an order-one dimensionless viscosity. The example
carries no swirl, gives no production and does not establish delivery of an order-one adjoint packet into the cell; whether such smooth cells produce at the
local order of Theorem 8(b) is not shown here. A related count is proved, but its relevance
is heuristic: if b = U^Z(0, .) satisfies |b_ZZZ| <= C_3 with C_3 > 0, and 8 delta < eps/C_3, let E be the set of points where
|b_Z| <= eps delta and |b_ZZ| >= eps, and call two points of E related when their distance is less than eps/C_3. Two related points
have curvatures of one sign (opposite signs force distance >= 2 eps/C_3), so |b_ZZ| > eps/2 with that sign between them, and the
bound on b_Z gives distance <= 4 delta; hence the relation is transitive, its classes (clusters) have diameter at most 4 delta and are
separated by at least eps/C_3, and an interval of length l meets at most 1 + l C_3/eps of them, against 1/delta modulation periods per
unit length in (vii). Relating clusters to recirculating cells and controlling their contribution to the adjoint variation over a
window are not done here; the suggested axial length of order 1/delta for an order-one production by such cells is a conditional scale
count only.
(x) A swirl-free kinematic family with V_nu >= c/delta on a fixed age window (proved in Appendix A, including the uniform probabilistic
error estimates). It addresses the version of the
V_nu question of Open (5) that assumes only the four pointwise velocity bounds and a fixed smooth terminal packet; it does not address
the question for the actual Case 2 adjoints. Fix C = C_* > 0 and
G > 0 as upper-bound parameters, put mu = C/G and nu = mu delta^3, so that r_c = delta/2^{1/2} and w_nu are those of Theorem 8(b).
Admissible fields are prescribed smooth, axisymmetric, swirl-free and divergence-free fields on R^3 with the Cartesian bounds |U| <= 1,
|grad U| <= 1, |grad^2 U| <= C for all times and d_t U bounded (for the fields below d_t U -> 0 uniformly, so any fixed cap such as that of
Theorem 1(b) holds for small delta). This is a kinematic class: no pressure equation, normalized gradient record or positive limiting-vorticity
packet is imposed. The adjoint is psi_s = U(., -s).grad psi + nu L psi, psi(., 0) = phi, the bounded solution vanishing on the axis;
equivalently psi(x, s) is the expectation of phi at physical time 0 for the diffusion started at x at physical time -s, with time-dependent
generator U(., -s + u).grad + nu L and absorption at the axis. V_nu(s) = int_0^infty w_nu(R) int |d_Z psi(R, Z, s)| dZ dR. Claim: there are K in (0, 1) and c > 0
depending only on C and G, a packet phi = Phi(R^2) xi(Z) in C_c^infinity independent of delta with 0 <= phi <= 1, supported in
{1/8 <= R^2 <= 6, -2 <= Z <= 20}, Phi(X) = X/8 for 1/4 <= X <= 4 and xi = 1 on [-1, 19], and for every small delta an admissible field U^delta
with V_nu(s) >= c/delta for K/(4 nu) <= s <= K/nu. Hence for every fixed K' >= max(1, K) the average of V_nu over the ages [0, K'/nu] is at
least 3 c K/(4 K' delta) = (3 c K/(4 K')) (C/G)^{1/3} nu^{-1/3}, so the sufficient condition o(nu^{-1/3}) of Theorem 8(b) fails in this
prescribed-field class, on windows with K' >= 1 included, although all the pointwise bounds hold. No matching upper bound for V_nu is asserted.
Construction. Let rho(x) = e^{-1/x} for x > 0, rho(x) = 0 for x <= 0, and h(x) = rho(x)/(rho(x) + rho(1 - x)) (h = 0 on (-infinity, 0],
h = 1 on [1, infinity)); this particular step satisfies |h^{(j)}| <= C' h (1 + |log h|)^{2j} for j = 1, 2, 3, which the logarithmic bound
below uses (smoothness and flatness alone would not give it). Put d_delta = delta^2 + (1 - delta^2) h(Z), b = 16/K and lambda = mu b. The
axial speed B = (nu b/d_delta(Z)) h(Z + 7) (1 - h(Z - 19)) equals lambda delta on the jet [-6, 0] and nu b on the slow pool [1, 19]; the base
stream function (R^2/2) B(Z) chi(R^2/64), chi(q) = 1 - h((4q - 1)/3), gives the radial-linear field U^R = -R B'/2, U^Z = B for R <= 4 and
vanishes for R >= 8, and the derivatives of 1/d_delta where h is of order delta^2 cost only logarithms:
||U_0||_{C^2} <= D lambda delta (1 + |log delta|)^6. On the jet a strain modulation with stream function
-eps L delta^2 R^2 zeta(Z) sin Theta chi_m(R^2/(L^2 delta^2)), chi_m(q) = 1 - h((q - 1)/3), Theta = (Z - lambda delta t)/(L delta),
zeta = rho(Z + 2) rho(-1 - Z) normalized to unit integral (supported in [-2, -1]), eps = alpha lambda, is radial-linear for R <= L delta and
vanishes for R >= 2 L delta (a cutoff at a fixed radius would violate the Hessian bound, since d_ZZ U^R would be of order eps R/(L^2 delta)); its
velocity, gradient, Hessian and time derivative are O(eps L delta^2), O(eps delta), O(eps/L) and O(eps lambda delta^2), and L is chosen
so large that the Hessian part is at most C/100. The constants are fixed in the order alpha, K, b, lambda, eps, L by (A8); the simultaneous
smallness conditions on delta are (A9). Mechanism. Use an axial comparison process whose coefficients are independent of R in a globally radial-linear field
U^R = a(Z, t) R, U^Z = w(Z, t). The jet comparison is time dependent, and the base comparison after jet exit is autonomous. The actual
bounded field is coupled to these comparisons until exit from the regions where their coefficients agree.
Conditionally on the comparison axial path, X = R^2 has in path law X_u = e^{2 A_u} beta(2 nu I_u), A_u = int_0^u a, I_u = int_0^u e^{-2 A},
beta a squared Bessel process of dimension zero started at X_0 and absorbed at zero. So a core element starting at R = delta r,
1 <= r <= 2^{1/2}, on the jet leaves it with X/delta^2 close to r^2 exp(2 alpha cos theta), theta its initial phase. In the transition and
the pool, in slow time tau = nu u, Q = X/d_delta(Z) satisfies the exact Ito identity
d log Q = (d'^2/d^2 - d''/d - 4/X) dtau + (8/X)^{1/2} dW^R - 2^{1/2} (d'/d) dW^Z (d = d_delta), in which the large convective terms cancel,
and the occupation density of the uncut autonomous axial comparison process, G(x, y) <= 2 d_delta(y)/b, applied to the radial estimates
stopped when Q first hits either 1/4 or 4 (the identity is used only up to that stopping time), makes the expected drift and quadratic variation small for b
large and K small. At residual slow times in [3/b, K] after a successful jet exit the element is in the pool with X = Q in [1/4, 4] except on
events of small probability (return to the jet, failure to reach the pool, upper pool exit, radial escape and absorption). Appendix A
gives the separate probability bounds, the stopping conventions and their accumulated error, proving the following uniform approximation:
|psi(delta r, z, s) - (r^2/8)(1 + 2 alpha cos((z + lambda delta s)/(L delta)))| <= alpha/100 for 1 <= r <= 2^{1/2}, -4 <= z <= -3 and
K/(4 nu) <= s <= K/nu. Testing d_Z psi against the bounded function 1_[delta, 2^{1/2} delta](R) g_0(Z) sin((Z + lambda delta s)/(L delta)),
g_0(Z) = h(4(Z + 4)) h(4(-3 - Z)) (so int g_0 >= 1/2 and ||g_0'||_1 = 2), and using w_nu(delta r) delta = 1/(2 r^3) on the tested annulus
(mass 1/8, r^2-weighted mass log(2)/4), the averaging error and the uniform value error give V_nu(s) >= alpha log 2/(256 L delta); this is
the bound with c = alpha log 2/(256 L). Window. Since h(Z) + h(1 - Z) = 1, the deterministic slow transit time across [0, 1] is
int_0^1 d_delta/b dZ = (1 + delta^2)/(2b), which tends to 1/(2b) = K/32 > 0, so the window begins at a fixed positive slow age.
For any positive transition speed B from the jet speed to a pool speed nu b_p, put f = nu/B, T = int f dZ and E = int (f')^2/f dZ; then
E T >= (f(end) - f(start))^2 (Cauchy-Schwarz). For fixed lambda and fixed b_p > 0 the endpoint values tend to 0 and 1/b_p, so T -> 0
forces E -> infinity. For the profile B = nu b_p + (lambda delta - nu b_p) e^{-1/(Z_c - Z)} near the pool,
E = (log a_delta)^2/(2 b_p) + O(log a_delta) = (2/b_p) log^2(1/delta) + O(log(1/delta)), a_delta = (lambda delta - nu b_p)/(nu b_p). For a
monotone decreasing speed extended by a constant pool of fixed length l_p > 0, the autonomous axial comparison process started upstream of
the transition, stopped on hitting Z_c + l_p and continued independently of radial absorption, accumulates expected axial quadratic
variation of log Q from the transition at least 2 (1 - e^{-b_p l_p}) E. These facts obstruct the small-distortion argument used here; they
do not exclude a nonperturbative transmission mechanism or a window beginning at ages o(1/nu). Scope. U^delta and grad U^delta tend to 0
uniformly, so the family is not a model of the nonconstant Euler limit, it has no normalized gradient record, and phi is not a packet on
which a limiting vorticity is positive as in Theorem 3; it carries no swirl and no production (q = 0), and it is not a Navier-Stokes solution
(G is an upper-bound parameter here, not the circulation norm of a datum). A proof of the small V_nu bound for the actual Case 2 adjoints
must use information beyond the four pointwise velocity bounds and a fixed smooth terminal packet, for example their
coupled evolution or the structure of the limiting-vorticity packet. A proof that estimates the signed production directly could instead
use cancellations discarded by V_nu. An attempted extension with swirl in this geometry (a source pool for the circulation
upstream of the jet and ordered cos and sin strain pulses on it) gives a positive quadratic jet-production coefficient in an inviscid
single-pass model with a suitably chosen compact terminal ring (algebra and sign checked, Section 5 (19)). This reduced-model algebra
does not give a viscous family: its extension needs an unproved representation with uniform weighted mixed derivative estimates, control of
the signed contribution of the rest of the history and the full velocity bounds for the swirl, and it is not established for the particular
packet used above. A further coupling restriction is precise: for any meridional velocity and any packet phi supported off the axis,
int eta phi dy = 2 pi int (U^Z d_R phi - U^R d_Z phi) dR dZ (from eta = (d_Z U^R - d_R U^Z)/R and integration by parts), so a family whose
meridional velocity tends uniformly to 0 near the packet cannot have a nonzero limiting pairing of its own eta with phi. No positive
full-history viscous pairing or coupled realization is established by this attempt.
(xi) A formal scenario study (conditional scale balances, not a construction). Put eps = T_* - t and assign
M ~ eps^{-2/3}, D ~ eps^{-5/4}, H ~ D^2/M (the persistent history of the compatibility test above), nu = D/M^2, l = M/D,
delta = (G nu/C_*)^{1/3} and r_c = delta l. The count additionally assumes an active tube of radius r_c and axial length l operating for a
generation of duration l^2, with axial cells of length r_c renewed on time scales r_c^2. With a fixed positive circulation level below G,
assign q of order r_c^{-2}, eta of order r_c^{-3} and compression of order r_c^{-2}. There are of order l^3/r_c^3 cell-events per generation.
These assumptions give Q_4 of order D M and absolute source and compression-work capacities of order 1/nu per generation (accumulated over
the continuously renewed history the source and work are of order eps^{-1/4}, larger than 1/nu ~ eps^{-1/12}). These exponents, and the
other exponent comparisons of the study (persistence windows, tube radii, energy and dissipation costs, Type II rates), are compatible with
the necessary size bounds of Section 1; some comparisons are saturated (H ~ D^2/M, and int Z_n w_n^{-3/2} dt ~ l^3 in Theorem 6(d)).
Constants, simultaneous realization, genuine records, the superlevel restriction, adjoint overlap, and the required signed pairing and
weighted work remain unverified. The count identifies no contradiction at the level of the checked exponents; it does not establish every
requirement of Section 1. Under the additional formal assignment that the meridional cell velocity has size r_c^{-1}, rescaling lengths by
r_c and times by r_c^2 gives coupled inner equations for q, eta and the stream function with unit diffusion and nonlinear coefficients, so
the assigned core problem has no small parameter. This is a balance of assigned cell scales, not a bound on the actual drift: an outer
axial component of size M has cell-unit size M r_c ~ nu^{-2/3}, and its constant part, its spatial variation and the inner/outer matching
would still have to be handled. The scale count does not determine the sign of the pairing of Theorem 3(b). Two exact facts came out of
the study. First, at a
first-crossing record of |u^theta| at a point with r_s > 0 one has -r_s u^r >= 1 there (at a positive maximum the angular equation
d_t u^theta + b.grad u^theta + u^r u^theta/r = Delta u^theta - u^theta/r^2 has d_t u^theta >= 0, grad u^theta = 0 and Delta u^theta <= 0;
the negative case is symmetric); in the units of Theorem 1 (lengths l_n, velocities M_n) this reads -R U^R >= nu_n, so it imposes no
order-one restriction. Second,
there is a restricted obstruction to coherent material export. Assume a core cell at radius of order r_c has radial and axial widths of
order r_c and eta-contrast of order D^2/M, with comparison constants independent of the small parameter. Suppose a locally diagonal
meridional material deformation takes its radius and radial width to order l while retaining this contrast and its axial interface.
Preservation of r dr dz then gives an axial width w_z of order r_c delta^2 = l delta^3 = (G nu/C_*) l. At the exported radius the
omega^theta contrast is of order D, so the mean value theorem forces |d_z omega^theta| >= c D/w_z, of order H/delta^3, which contradicts the
Cartesian Hessian bound of order H as delta tends to 0. The argument excludes this specified deformation with a retained interface. It does
not exclude general deformations, evolving contrast, simultaneous source and diffusion, or transfer involving many cells, and it does not
give a formula for what the packet receives. The width w_z has diffusion time of order nu^2 l^2, smaller than the time l/M = nu l^2 of
transport over distance l at speed M (advection across the width itself at speed M takes a time of the same order nu^2 l^2); this scale
comparison alone does not determine the transfer mechanism.
None of these is a fixed-datum Navier-Stokes counterexample, and no admissible kinematic family with the fixed terminal packet and an
order-one positive lower bound on the production over the required full history has been constructed.

Open: (1) TARGET-2. (2) Q_4(t_n) = o(D_n M_n), or an upper bound limsup_n P_n < m_phi for the signed normalized production
P_n = - nu_n int_0^{t_n} int q^2 d_z Psi_n dx dt, obtained from the coupled Gamma equation (Theorem 3(b) gives P_n -> m_phi, so either
would exclude Case 2); by Theorem 6(b) the part older than h is at most C (Q_4([0, t_n - h])/(D_n M_n))^{1/2} (1 + h/l_n^2)^{-3/4}, so it suffices to
find 0 <= h_n <= t_n with nu_n int_{t_n - h_n}^{t_n} int q^2 d_z Psi_n dx dt -> 0 and (Q_4([0, t_n - h_n])/(D_n M_n)) (1 + h_n/l_n^2)^{-3/2} -> 0
(then P_n -> 0), and by Proposition 7 (with its choice of s_n and the middle history I_n) it suffices to bound
int_{I_n} int (u^r/r)_- q^2 Psi_n dx dt by o(1/(nu_n^2 e_n)). A sufficient conditional statement (not available here): suppose
0 <= beta <= 2 and that constants C, r_0 > 0 independent of n satisfy |Gamma(r, z, t)| <= C r^beta for r < r_0 throughout the middle histories;
with the outer circulation bound this excludes Case 2 if e_n H_n^{2(2-beta)/(3-beta)} = o(D_n M_n); the case beta = 1 is a uniform bound on
u^theta on these histories. (3) A fixed-data bound int_0^{T_*} ||d_z(q^2)||_{L^1(R^3)} dt < infinity, or a bound
||eta(t_n)||_{L^1(R^3)} = o(nu_n^{-1}) along the records, for solutions with swirl; either contradicts Corollary (ii). (4) Whether D_n^3/M_n^5 is uniformly bounded, and whether the ancient Euler limit has finite energy. Uniform boundedness of the former
implies finite energy of the limit (Fatou) and, by Theorem 8(a), uniform smallness of the whole-history production outside sufficiently
large fixed multiples of l_n; finite energy of the limit alone has not been shown to imply that prelimit bound, and the remaining
near-axis production is not controlled in either case. (5) Whether the actual Case 2 adjoints satisfy the
bound o(nu_n^{-1/3}) for the age-averaged, w_nu-weighted axial total variation V_nu of Theorem 8(b) on each fixed window [0, K/nu_n], or
whether a construction satisfying the additional Case 2 conditions shows that this bound can fail. That bound makes the production of the
window negligible; exclusion by this route also requires control of the older history (for instance through the whole-history inequality
of Theorem 8(b) or the old-age bound of Theorem 6). On growing windows 0 <= s <= Lambda_n/nu_n the condition for the contribution of the
window to vanish is Lambda_n nu_n^{1/3} Vbar_n -> 0, Vbar_n the average of V_nu over that window, and the older history must again be
controlled. By Section 4 (x) and Appendix A, the
four pointwise velocity bounds do not suffice for every fixed smooth terminal packet: for one such packet the construction has V_nu >= c/delta
on a fixed fraction of each fixed larger window. The construction has zero limiting velocity and its packet does not satisfy the positive
limiting-vorticity condition of Theorem 3; a proof of the small V_nu criterion for Case 2 must therefore use additional information. For the signed production itself no admissible kinematic
family with a fixed terminal packet and an order-one positive lower bound over the required full history is known; cancellation may permit
a production estimate even where the V_nu criterion fails, and whether such an estimate requires the coupled dynamics remains open.
The local modulation example of Section 4 (vii) shows that, with prepared radial endpoint data, the local order of Theorem 8(b) occurs
during one modulation time; supplying those profiles, linking the adjoint to the fixed terminal packet, renewing the mechanism and
controlling signed contributions of the rest of the history are not achieved by it, and it does not show that every proof must address
renewal in this form. (6) A bound nu_n int_0^{t_n} (Pi_s)_+ dt -> 0 for the self-compression of Theorem 9(d), or the weaker signed bound
limsup nu_n int_0^{t_n} e^{3 C_0 (t_n - t)} Pi_s(t) dt < 2 m_phi/(3P) of the same theorem, or an upper bound Act(t_n) <= (1/3 - epsilon)
log(1/nu_n), for some fixed epsilon > 0 independent of n and all sufficiently large n, for the Sigma-averaged compression action Act of
Theorem 9(b) (with epsilon = 0 the additive constant in the lower bound of Theorem 9(b) can prevent a contradiction). The periodic steady
example of F10 (c) disproves a universal nonnegative critical-weight work identity, and by Appendix B the three Case 2 spatial velocity
bounds and the circulation bound alone do not imply the first bound in the drift-free prescribed-swirl model (a localized whole-space family
started from zero sourced vorticity has nu int (Pi_s)_+ dt >= c). By Appendix C the same holds in the prescribed-swirl model in which eta_s
is transported by its own poloidal velocity. Both families have velocity and gradient tending uniformly to zero and no normalized gradient
record, and neither solves the Navier-Stokes system. A proof must therefore use information absent from both models (the swirl equation or
the remaining Case 2 conditions).
The swirl equation does not by itself force the unfavourable sign in a single Burgers column (proved for the linear response). In cell units
(unit viscosity) let v_0 = (v^r, v^z) = (-r/2, z) and Q_B = (1 - e^{-r^2/4})/r^2, a steady solution of (d_t + v_0.grad) Q = Delta_5 Q - 2
(v_0^r/r) Q with circulation r^2 Q_B -> 1 at radial infinity. Put A = - Delta_5, T = Delta_5 + (r/2) d_r - z d_z + 1, D_B = Q_B' + 2 Q_B/r =
e^{-r^2/4}/(2r), g = e^{-r^2} - (1/2) e^{-100 r^2}, V = g(r) e^{-z^2/2}, f = A^2 V and Q_1 = f/(2 Q_B). Then q = Q_B + eps Q_1 solves the
steady swirl equation with the field v_0 + eps v_1 up to O(eps^2), that is, T Q_1 = D_B v_1^r, for the smooth divergence-free external
modulation v_1 with v_1^r = (T Q_1)/D_B and v_1^z(r, z) = - int_0^z (d_r v_1^r + v_1^r/r)(r, z') dz'. In the drift-free sourced-vorticity
equation of Appendix B the first-order source eps d_z f has the steady response a = - eps d_zz V, whose pairing with Q_B^2 vanishes after
axial integration, so the critical-weight expansion work int int r^2 q^2 a dr dz is eps^2 J + O(eps^3), with J = int int r^2 f (- d_zz V) dr
dz = pi^{1/2} (E_0/2 + 3 E_1/2 + 15 E_2/8), E_0 = int r^2 g L_0^2 g dr, E_1 = int r^2 g L_0 g dr, E_2 = int r^2 g^2 dr, L_0 = - d_rr - (3/r)
d_r. Exact Gaussian moments give J/pi = (498003/102400) 2^{1/2} - (2513093451/3329932832) 101^{1/2} = -0.70686... < -1/2, so the sourced
strain compresses. This is one localized cell in an unbounded affine background, without the feedback of the sourced velocity on q: with the
normalization of Appendix B (q of size alpha C_* delta) one such cell of fixed axial extent in cell units gives self-compression work of order delta nu
over the rescaled time 1/nu, not the critical order nu; if Q_1 and v_1 have a common axial period p > 0, subtracting T Q_1 = D_B v_1^r
at z and z + p gives - p d_z Q_1 = 0, so no z-dependent steady periodic swirl perturbation about this single affine Burgers column exists; and a steady profile Q_1 = w(r) cos(k z) across a column of axial span delta^{-1}
forces v_1^r to contain k z w(r) sin(k z)/D_B, so the Hessian bound limits its amplitude to eps = O(delta). Resupply is also constrained
(proved): if Gamma and v are smooth, axisymmetric and z-periodic, steady or time-periodic, with Gamma_t + v.grad Gamma = L Gamma, div v = 0,
Gamma = O(r^2) and v^r = O(r) at the axis, then averaging over the period(s) gives r (bar Gamma)' - 2 bar Gamma = r avg(v^r Gamma), and
since avg(v^r) = 0 no such flow has Gamma -> Gamma_inf > 0 uniformly with r avg(v^r (Gamma - Gamma_inf)) -> 0 at radial infinity ((bar
Gamma)' ~ 2 Gamma_inf/r is not integrable). The local calculation disproves a universal nonnegative-work assertion for the stated steady
linearized swirl response in the drift-free sourced-vorticity model. Separately, the resupply obstruction applies to the stated axially
periodic steady or time-periodic flows with uniform positive far-field circulation and vanishing weighted covariance. It leaves open axial
inflow and outflow, nonvanishing far-field covariance, and finite transients. These results do not construct a coupled family.
Inverse design and the restricted coupled model (derived by the second model and checked here, Section 5 (24)). With Gamma = R^2 q and
b = (- d_Z psi/R, d_R psi/R), the swirl equation for a given history is the linear first-order equation {psi, Gamma} = R S for the stream
function, where {psi, Gamma} = psi_R Gamma_Z - psi_Z Gamma_R and S = nu L Gamma - d_tau Gamma, to be integrated along the level curves of
Gamma. A prescribed smooth swirl history therefore solves its unforced equation for a smooth incompressible meridional field B exactly when
this equation has a solution smooth in space and time with the required axis, boundary and far-field conditions. On every closed regular
connected level curve C the integral of R S/|grad Gamma| over C must vanish, and the same holds over one period of a level curve closed
modulo an axial period when B is required to be periodic (periodicity of Gamma alone does not force this: the stationary Burgers column has
a nonperiodic meridional velocity). These conditions are necessary, not sufficient: the primitives along level curves must also match and
extend smoothly through the critical sets of Gamma (at a saddle, S = 0 there is not sufficient) and satisfy the endpoint conditions on open
level curves; for compact regular superlevel sets the aggregate condition int_{Gamma > c} S dx = 0 is likewise necessary but not sufficient.
Once an admissible B and the sourced field have been constructed (in a transported model the sourced equation is solved with the total
transport B), b_e = B - b_s makes the prescribed q an exact solution of the swirl equation with velocity b_e + b_s, the feedback of b_s
being absorbed. So a model with an unrestricted time-dependent external field adds to prescribed swirl only this solvability requirement,
provided the source evolution and the Biot-Savart recovery are well defined; the bounds on the total velocity must still be verified. The
swirl of Appendices B and C does not meet the requirement: if Gamma is smooth, localized, time-independent and not identically zero
(replaced by - Gamma if necessary, so that it has a positive maximum), then for any smooth incompressible B, possibly time-dependent, a
compact regular superlevel set {Gamma > c}, c > 0, has int_{Gamma > c} B.grad Gamma dx = 0, while nu int_{Gamma > c} L Gamma dx is - nu
times the integral of |grad Gamma| over its boundary, which is negative (L Gamma = Delta_3 Gamma - 2 Gamma_R/R, and the last term integrates
to zero over each radial interval of the superlevel set, at whose ends Gamma = c).
In Case 2 the field not sourced by the swirl is small: its radial strain is a_r = O(1/D_n) in the rescaled frame, which is o(kappa_n) for
the cell rate kappa_n = nu_n/delta^2 (by the lower bound D_n^3/M_n^5 >= pi/(768 E_0) of Section 1, nu_n >= c D_n^{-1/5} and
D_n kappa_n >= c D_n^{14/15}), and its integrated action is bounded (over a window of record length 1/nu_n it is at most a constant times D_n^{-4/5}). Under
this restriction the following conditional persistence obstruction holds. In the drift-free model started from eta_s(0) = 0, with
whole-space Biot-Savart recovery and the normalization q = alpha C delta Q of Appendix B, write Q^2 = F_0 + F_1 in cell coordinates, with
F_0 independent of z and |F_1| <= P(r), where the radial lift of P lies in L^1 and L^infinity of R^4 uniformly in the family. Then
||a_s||_infinity <= alpha^2 G^2 K_P kappa with K_P = (||P||_infinity ||P||_{L^1(R^4)})^{1/2}/(2 pi), uniformly in time and without
periodicity. If q > 0 along an axial characteristic, Delta_5 q/q <= - sigma/delta^2 there and q(T)/q(0) >= c_*, with sigma > 0 and c_* > 0
independent of delta, the swirl equation gives int_0^T (- a_e) d tau >= (sigma/2 - alpha^2 G^2 K_P) kappa T + (1/2) log c_*;
if sigma/2 - alpha^2 G^2 K_P >= epsilon > 0 uniformly in the family, then at the record time T = 1/nu (where kappa T = delta^{-2}) the external
compression action is at least epsilon delta^{-2} + (1/2) log c_*, contradicting the Case 2 action bound for sufficiently small delta (the
inequality is one-sided; no matching upper bound is asserted). A stationary core Gamma = A (1 - e^{-gamma R^2/(4 delta^2)}) with fixed
A != 0 and fixed gamma > 0 needs a = - gamma kappa/2 wherever that profile holds on a spatial neighborhood, so a_e = - gamma kappa/2 at a genuine
initial time with zero sourced vorticity and whole-space Biot-Savart recovery. These statements are separate. The exact steady swirl of
Appendices B and C, which vanishes on the axis, is excluded by the superlevel argument, not by the characteristic estimate, which applies
only to cores satisfying its curvature, persistence and sourced-strain hypotheses. The drift-free heat estimate does not give the
sourced-strain bound for transported histories, evolving cores outside this class remain undecided, and vorticity sourced before an
observation window must be kept in the sourced field.
The question for the coupled evolution remains open. A third sufficient condition (F10 (d)) is an estimate 3 (C + T) <= epsilon (D_q + 3 D_psi) + e with epsilon < 1 and
int_0^{t_n} e = o(nu_n^{-2}) for the remainder of the coupled critical balance (the order nu_n^{-2} comes from F(t_n) >= c nu_n^{-2}); its cubic
part T admits no instantaneous bound T <= epsilon D_psi over arbitrary amplitudes, and the identity itself is formal (F10 (d)).

How to resume. Items (1), (2), (3) and the bounds on the self-compression and on the compression action in (6) are sufficient
conditions for excluding Case 2; the estimate of F10 (d) in (6) is sufficient provided its formal identity holds along the solution; (5) is sufficient together with control of the older
history; (4) is a structural question whose positive answer would not by itself exclude Case 2. No equivalence between these conditions is
asserted. The model results indicate where further information must enter: the four pointwise velocity bounds do not give the small V_nu
criterion of (5) for every fixed smooth terminal packet (Appendix A), and the three spatial velocity bounds and the circulation bound alone do not give the first bound of (6) when the swirl is
prescribed, with or without transport of eta_s (Appendices B and C). These model families have zero limiting velocity and no
normalized gradient record; they are not Case 2 Navier-Stokes histories. The next step suggested by these results is an upper bound for the
signed self-compression of Theorem 9(d) along histories in which the swirl obeys its own equation, or a coupled model family showing
that such a bound fails in which the swirl evolves without forcing, both transported equations use the same total velocity, the sourced
field contains all vorticity generated since the initial time, the remaining Biot-Savart component solves the homogeneous transported
equation with a_r = O(1/D_n) in the rescaled frame and bounded integrated action, and every reservoir and boundary flux is stated. An
unrestricted external field does not test this decomposition: for a prescribed swirl history admitting an admissible smooth inverse B it can
be chosen as B - b_s (Open (6)). The persistence obstruction under the inherited bounds applies only to the class specified in Open (6); it
does not exclude arbitrary evolving cores.

## 5. Verification

How the results were checked. The arguments of Sections 1 to 3 were derived or rederived by hand. The printed arguments of Section 2 and the
appendices, together with the explicitly cited theorems, are the mathematical evidence; routine steps are stated concisely rather than
written out in full. Symbolic checks test algebraic identities; quadrature and discretized calculations test selected examples and do not
prove PDE estimates. Exploratory cell simulations were not independently reproduced. Unverified citation locations and conditional model
constructions are identified where they occur.

Independent review. Statements were tested by a second model (a GPT-6 model run through Codex) instructed to find errors. Its answers were
treated as claims and are not proof dependencies. Returned arguments and objections were checked against the printed derivations and
selected symbolic and numerical calculations.
Several arguments first appeared in its answers and were then checked by hand: the production identity of Theorem 3 and the proof of Theorem
3(g); the truncated-energy proof of Theorem 5(b); the weighted adjoint energy of Theorem 6(b) and Proposition 7; the compression memory and
axis barrier of Theorem 8(c), (d), the weighted envelope form of Theorem 8(b) and the (J, eta) identity; the negative findings (i) to (iv)
and the items (vi) to (xi) of Section 4, including Appendix A; most cell-scale statements of F9; the memory profile of F10 (c), Appendices B
and C, the single-column example and the inverse-design and persistence statements in Open (6); the balance of F10 (d); and the
barrier proof of Corollary (iii) (Section 2.7d). Separate adversarial audits by the second model examined the numbered results, the findings, each appendix and finally the whole manuscript, each
within a stated scope. They reported no false statement among the numbered results (Theorems 1, 2, 3, 5, 6, 8 and 9, Propositions 4 and 7
and Corollaries (i) to (vi)) and no fatal error. The auxiliary errors and gaps of proof, scope and wording that they identified are
corrected at the affected statements, where the remaining limitations are stated; examples are a comparison factor in a remark on Theorem 6,
the fixed-z integration by parts formula of F1, a reversed inference in Section 4 (iii) and the leading coefficient of the distortion action
in Section 4 (x). The last whole-manuscript audit (which excluded the paragraph on swirl records in Section 4, audited separately) found
only two wording problems, the notation for the rescaled pressure in Theorem 1(b) and the missing uniformity of epsilon in the action bound
of Open (6), both corrected, and a narrow audit of the repairs found no error. Gaps closed by adding proofs include Theorem 1(a) (Section
2.2), the deduction of the two compression bounds of Proposition 7 (Section 2.7b), the kernel estimate of Theorem 9(d) (Section 2.9), the
variable-in-time barrier of Corollary (iii), Corollary (iv), the last assertion of Theorem 6(d) and Proposition 4(b); the identity of F10
(d) is stated as formal. These reviews are not a single independent reconstruction of every assertion, and agreement between model runs is
not a proof or a formal verification.

Individual checks (calculation; method; result; limitation).
(1) 5D lift, adjoint transformation, radial integral constants, bathtub value, radial integration by parts formula, Casimir source
cancellation; sympy, and mpmath where sympy did not close; all confirmed; these check identities, not the estimates built on them.
(2) Theorem 9(a) and the adjoint-weighted identity behind Theorem 9(c); mpmath quadrature on explicit smooth fields (prescribed q and
Psi, divergence-free poloidal field built from a streamfunction); the integrals agree to working precision while the integrands differ
pointwise; the weight used changes sign, so this checks the identity and not the inequality, which uses Psi_n >= 0. The identity of
Theorem 9(a) was also compared by hand with Shahmurov's balance (3.9) at q = 2.
(3) Kernel bound of Section 2.9; sympy for Delta_3(x_1 g) = x_1 Delta_5 g and for |S^4| = 8 pi^2/3, mpmath quadrature for the S^3 and S^1
averages, and a brute-force comparison of the five-dimensional majorant with the three-dimensional bound at sample points; all agree;
these are sample checks accompanying the analytic proof of Section 2.9, not general proofs.
(4) Constants of Theorem 8 (pi e (cosh(1)/6)^{1/2} < 4.4, the barrier constant 1.2707, the Riccati supersolutions, the (J, eta) cancellation), the
constants of Theorem 6 and Proposition 7 (49/128, 49/64, the restriction alpha < 3/2) and the constants of Theorem 9(b) to (d); by hand,
and confirmed in audits.
(5) Memory profile of F10 (c); closed form against mpmath quadrature (difference about 1.4e-15), steady response and positivity of the
energy-weighted work symbolically; confirmed; the localization at the saturation scale is proved in Appendix B (see (21)), and its
transported version, with q still prescribed, in Appendix C (see (22)); the coupled evolution remains open.
(6) Balance of F10 (d); variational derivative of F, source term I + C and diffusion term by hand, the two forms of D_psi and the
variational derivative compared numerically on two explicit fields (scipy quadrature, agreement about 1e-13 relative); confirmed as a
formal identity; the axis behaviour of h and chi was checked only to leading order and the boundary terms were not verified. The bound
K <= 68 F and F(t_n) >= (c_U/68) nu_n^{-2} (1 - o(1)) were derived by hand.
(7) The value T[psi_*] in F10 (d); an independent second-order finite-volume solve of - Delta_5 u = b.grad(eta) (grid sizes 0.1, 0.05,
0.025 give -6.5e-4, 4.58e-4, 7.335e-4, Richardson value 8.25e-4, in agreement with the closed form; the coarsest grid has the wrong sign);
agreement of the closed form with the representation (3 pi^2/2) int_0^1 x^6 (4 x^6 - 36 x^4 + 11 x^2 + 5)(1 + 2 x^2)^{-6} dx to 30 digits;
and an exact rational sign certificate: arctan sqrt2 = pi/4 + arctan(3 - 2 sqrt2), 1.41421 < sqrt2 < 1.41422, pi < 355/113 and
arctan v <= v - v^3/3 + v^5/5 for 0 < v < 1 bound the bracket 35299/82944 - (645 sqrt2/2048) arctan sqrt2 below by 7.8e-5 > 1/14000.
The closed form, first supplied by the second model, was derived independently and exactly with sympy: A^{-1} = int_0^infty e^{t Delta_5} dt;
with f = - b.grad(eta) = - z (28 + (16 s - 80) z^2) e^{-2s}, s = r^2 + z^2, and d = 1 + 8t, the explicit Gaussian expression for e^{t Delta_5} f
(a polynomial in r, z, d^{-1} times d^{-5/2} e^{-2s/d}) is checked to solve the heat equation in R^5 with initial value f; the pairing
pi^{-1} <eta/r + psi_r/r^2, e^{t Delta_5} f>_{dX} equals J(d) = 6 pi^2 (5 d^3 + 11 d^2 - 36 d + 4)/(d^{3/2} (d + 2)^6) by exact Gaussian moments;
T = (1/8) int_1^infty J(d) dd becomes the integral above under x = d^{-1/2}; and an exact antiderivative gives the closed form.
D_psi[psi_*] = 15 pi^2/8 was obtained by the same moments.
(8) F9; the energy identity and irrotational example of (e), the Feller law, landing constant, cap integral and
production bound of (f), the comparison subsolution and corrector expansion of (g) (sympy), the closed-cell energy identity, flux
identity, slope count and weighted moment identity of (h) (the last also numerically on explicit fields; the divergence-free sign
statements were checked by hand and the explicit example, its energy, moment, impulse and swirl source exactly in sympy), and the derivative scalings,
scale density, hitting-probability bounds and symmetry cancellation of (i); by hand unless stated; confirmed under the hypotheses
stated; not checked: the Poincare constants of (h), the constants of the expansion inequality in "Core supply", and the parabolic
third-derivative estimate of (f) beyond the level of the argument.
(9) Exponent bookkeeping of the scalar diagnostic in Section 4, by exact arithmetic; it concerns scalar inequalities only. The record
dichotomy, the occupation bound and the band bound of the time-geometry paragraph were checked by hand, the exponents and band limits of the
two scalar histories exactly in sympy. The fields, trajectories, Jacobian and pipe-flow identities of the material-properties paragraph were
checked exactly in sympy, the cutoff bounds of (a) by hand.
(10) The numerical cell and fold computations quoted in F9 (d), (f), (h), (i) were performed by the second model and not rerun; no
conclusion of this report depends on them.
(11) The axis evolution of E and its reduction in the Hou-Li exact class (F10, literature paragraph): exact sympy computation with truncated
even expansions in r and d_z u^z = - 2 a on the axis; it checks the identity only. The off-axis equations for (d_z q, d_z a) and the value
d_t E = 4 alpha r^2 k^2 for the polynomial core were checked exactly in sympy, the complex form of the (q, a) equations and the cutoff
construction by hand.
(12) Geometric criteria of F5: the rotation and distance identities, the energy constant pi/768, the three scale identities and both length
exponents were checked symbolically. This checks algebra only; the hand arguments carry the qualifications stated in F5.
(13) The three forms at the end of F4: the conservative form of the omega^theta equation, the axis flux 2 eta(0, z), the swirl source and
the xi-form of source, transport and swirl energy density were checked exactly in sympy, the vertical-line identity numerically. The label
form and the cell construction were supplied by the second model and checked by hand (scalings, the constants of the cells, the shape ratio
of (A), the right derivative at a datum with flat support edges). An audit by the second model found no sign, factor or scaling error; the
two qualifications it asked for (the hypotheses under which the pointwise nodal identity holds, and the orientation and off-axis domain of
the label coordinate) are included.
(14) The four later Shahmurov papers of F5 were checked against the Case 2 hypotheses by the second model, which went through their numbered
results; its quotations of the scope statements were verified against the texts, and the source-mass bound and the reaction term of the
lifted test function were rederived by hand. Corrections from audits of the F5 text (the scope wording; Proposition 10.1 of 2606.07869 as
the pointwise swirl-energy estimate, with Theorem 10.2 as its time-integrated consequence; the local form of the negative-norm estimate;
Theorem 7.1 of 2606.07869 bounds the radial strain b_g^r/r, not a velocity, as its notation U = u^r/r and the Biot-Savart display in its
proof show) were checked against the texts and adopted. The proofs in those papers were checked only by the second model, where used.
(15) The flux identity, the O(delta^2) pointwise velocity bounds and the stationary supersolution for the auxiliary channel with absorbing
sides and a reflecting inner boundary (Section 4 (vi)) were derived by the second model and rederived by hand, including the inequality mu
f'' + B |f'| <= - lambda for the printed supersolution. They prove the restricted channel estimate only; no comparison with the unrestricted
adjoint, and no exclusion of general combs with alternating contrasts, has been established. The all-age extension of Theorem 8(a) (constant
pi e (cosh(1)/6)^{1/2}) and its dissipation form were checked by hand and in an audit by the second model, including the additional
hypothesis sup_n D_n^3/M_n^5 < infinity.
(16) The local modulation example and the averaged strain constraint of Section 4 (vii) were derived by the second model (its exact symbolic
checks were not rerun); an audit by the second model corrected the cutoff factors and the hypotheses of the general-history and transit
statements. Rederived by hand: the variations from the stream function, the axial integral pi (p_1 - p_2), the time integral int_0^3 (p_1 -
p_2) dt = 2, the coefficient 2 pi^2 J_chi, the per-unit-length scaling delta^2, the value J = 1/3 for uncut Gaussians (not asserted for
J_chi), the inviscid quadratic coefficient for a fixed general history, the lifted equations for gamma/r^2 and Psi/r^2 and the averaged
strain constant 1/4. The viscous continuity estimate (weighted C^3 bounds and a C^1 difference estimate on a fixed interval, error O(1/G))
was checked in its structure, by hand and in the audit; it gives no error bound uniform over growing histories.
(17) The axial shear bound of Section 4 (viii) was derived by the second model and rederived by hand (commutation of d_Z with the adjoint
operator, the radial supersolutions 1 and R^2, the exact circulation solution, F_K(R) = int_0^K (1 - exp(-R^2/(4 a')))^2 da' <= min(K,
R^2/2)); the radial integrals 1/2 + (1/4) log(2K) (K >= 1/2) and (for r_c <= 1) r_c^2 (3/4 + log(1/r_c)) were checked by mpmath quadrature
and by exact piecewise integration (the latter in an audit by the second model, which also supplied the restriction delta <= 2^{1/2}).
(18) The cell family of Section 4 (ix) was derived by the second model; its velocity, divergence (axisymmetric and Cartesian), the vanishing
of grad^3 U in the core, the center linearization, the separatrix and the rescaled adjoint equation were checked by exact symbolic
computation, and the one-dimensional axis-cluster bound was proved by hand. An audit by the second model rechecked these with its own
symbolic computation; the domain of the rescaled equation, the definition of clusters and the corrected sign statement in the cluster
argument that it asked for are included. No cell-count or production-length theorem is asserted.
(19) The kinematic family of Section 4 (x) and its proof in Appendix A were constructed and written by the second model. Appendix A was
checked analytically for the following estimates and constructions: the explicit constant hierarchy, the Cartesian bounds with the logarithmic loss from the
reciprocal transition, the killed representation and its justification by a lift to five dimensions, the jet passage (Ito formula for the
primitive of the envelope and the martingale e^{-2A} X/delta^2), the exact cancellation in d log(X/d_delta(Z)), the occupation kernel, the
radial transmission with its stopping convention, the return, pool-exit, escape and absorption probabilities, the accumulated error 413
alpha/400000 < alpha/100, the dual test and the age average. The symbolic identities (the derivatives of delta^2/d_delta, the divergence
cancellation, the Ito drift and quadratic variation, the Ito identity for log Q, the radial form 4X d_XX of L, the squared Bessel Laplace
transform, the five-dimensional lift, the annular integrals, the weight masses, the action coefficient and the final constant sum) and the
numerical constants (exp(2/5) comparisons, log(4/3) > 1/4, the coefficient sums) were checked with sympy and mpmath. Two adversarial audits
by the second model rederived the arguments. The first found an error that the hand check had missed (the leading coefficient of
log^2(1/delta) in the distortion action of the exponential profile is 2/b_p, not 1/(2 b_p), since log a_delta = 2 log(1/delta) + O(1)) and
asked for the specified step profile, the stopping conventions, the restriction of the scope to the prescribed-field class and a lower-bound
reading of the order nu^{-1/3}; the second found no mathematical error and corrected one sentence after (A64) that understated (A63). All of
these are incorporated. The cited textbook editions were not inspected in these audits. For the swirl attempt the check is limited to the
reduced-model production algebra and the sign of its compact-ring coefficient; the viscous representation, the complementary history and the
swirl velocity bounds remain unproved. No PDE simulation or formal verification is claimed. Section 4 (x) is not used in Section 1.
(20) The formal scenario study of Section 4 (xi) was done by the second model. Its exponent comparisons were checked with exact rational
arithmetic, and the swirl-record inequality and the restricted diagonal-export calculation by hand under their stated hypotheses; an audit
by the second model removed overstatements from its first version (exponent compatibility presented as verifying every scalar requirement,
the inner scaling as unconditional and the export obstruction as exhaustive). These checks do not verify profile constants, simultaneous
realization, signed production or a coupled evolution; the study neither constructs a fixed-datum Navier-Stokes scenario nor excludes one.
(21) Appendix B (the localized drift-free family of F10 (c)) was derived and written by the second model, in answer to a request for either
a rigorous localized version of F10 (c) or a proof that the induced field must violate a bound. Checked by hand: the sign conventions
(source d_z(q^2), a = - d_z psi_1, a = S F with S = - d_z^2 (-Delta_5)^(-2)), the kernel and cutoff estimates (B11)-(B17), the potential
bounds (B20)-(B26) including the tensor counting, the scaling (B32)-(B36) and the budget alpha S_v + 2 alpha^2 G B_v <= 1/2, the steady work
(B37)-(B42), the memory estimate (B43)-(B48), the constants (B49)-(B52), the change of variables (B53)-(B55) and the matching upper bound
(B56). Checked with sympy and mpmath: the factorization h = g p of (B3), the three Gaussian integrals (B6) and the value I = -0.174019...,
the rational bound (B7), the kernels (B10)-(B12), the transverse and axial integrals of (B13) and (B21), the intertwining identity (B28),
the divergence and azimuthal vorticity of the field (B22) for a concrete potential, the powers in (B34), (B36), (B51) and (B54), the maximum
of g, the heat-kernel integrals in (B44) and (B46), and the cutoff integrals of (B9). An adversarial audit by the second model rederived
(B2)-(B55) with its own symbolic and numerical checks and found no error in the construction; its corrections (the radius in the
introductory definition of b_s, R eta_s e_theta in record coordinates; the description of the limit as the zero Euler solution; the scope
wording, the three spatial velocity bounds rather than every estimate of Theorem 1(b)) are included, and it supplied (B56). Appendix B is
cited in Section 1 as a model result; no numbered result of Section 1 depends on it. The two limitations stated after F10 (c) were supplied
by the second model; the logarithmic example there was rederived by hand and its heat formulas and constant checked with sympy.
(22) Appendix C (the transported family with prescribed q; the coupled evolution remains open) was derived by the second model in two
answers (the periodic transported theory, the modulated approximation, its residual and its work; then the delta-uniform estimate for the
exact error in the velocity formulation) and written in report form here with three changes: the envelope (C7) is the weighted sum of the
axial suprema of single entries (the axial supremum of the weighted sum of entries, used in the answer, also satisfies (C34) with constant
one), the identification of the fixed point with the transported solution is the argument of C.9, and the work bound does not use the
drift-free solution. Checked by hand: the cell form and the work identity (C5)-(C6), the periodic contraction, stability and scaling
(C8)-(C17), the derivative bounds (C18), the decomposition (C20) and the residual identity (C22) with its signs, the averaging bound (C25)
and the work of the approximation (C26), the velocity identities (C27)-(C30), the kernel bounds (C31)-(C33), the residual response
(C35)-(C38) with its counts, the bilinear and linear estimates (C39)-(C42), and the contraction, the constants and the work budget
(C43)-(C49). Checked with sympy and mpmath: the kernel norm formula of (C33), the optimization in (C36), the Gaussian maxima of (C37), the
time integrals (C38), the counts and margins of (C35) and the integrals in N_P, the splitting constant 8 of (C39), the conversion
inequalities in delta and ell, the contraction budget of (C43), the work scaling (C6) and the budget of (C48). The constants C_O, A_b, C_R
and C_a are finite suprema that were not evaluated numerically. An adversarial audit by the second model of Appendix C (cell form and work;
periodic theory and approximation; velocity equation and residual; kernel and envelope inequality; residual response; bilinear and linear
estimates; fixed point and identification; constants, pointwise bounds and work) rederived the identities of (C5)-(C30) with sympy, gave
elementary proofs of the time inequalities (C38), checked the 39 entry counts, and found no fatal error and no gap in the proof of (C3); its
wording corrections are included, and a narrow audit of the corrected lines confirmed the upper bound W_s/nu <= 2 pi alpha^4 C G^3 A_F M_b
at the end of C.10. Both Appendices B and C prescribe q, have velocity and gradient tending uniformly to zero and no normalized gradient
record, and do not solve the coupled Navier-Stokes system.
(23) The single-column example and the averaged circulation identity in Open (6) were derived by the second model. Checked here exactly
in sympy: that Q_B solves the steady swirl equation T Q_B = 0, the formula for D_B, the first-variation identity (the O(eps) part of the
steady swirl residual is - T Q_1 + D_B v_1^r), the Gaussian moments int r^2 e_a e_b dr, int r^2 e_a L_0 e_b dr, int r^2 e_a L_0^2 e_b dr
(e_a = e^{-a r^2}), the moment formula for J, the closed form of J and the rational sign certificate (sqrt2 < 10/7, 498003/102400 < 49/10,
sqrt101 > 10 and 2513093451/3329932832 > 3/4 give J/pi < 7 - 15/2 = -1/2), and the derivative identity behind the averaged circulation
identity; J also by direct symbolic double integration of r^2 f (- d_zz V), compared in floating point (J = -2.2207). Checked by hand: the
drift-free response a = - eps d_zz V and the vanishing of its pairing with Q_B^2, the periodicity obstruction, the averaging argument for
the resupply statement, the scaling to order delta nu and the amplitude restriction eps = O(delta).
(24) The inverse-design reduction, the superlevel obstruction for the swirl of Appendices B and C and the persistence bound in Open (6) were
derived by the second model, in answer to a request to check a reduction proposed here, which it corrected (the aggregate superlevel
condition is necessary but not sufficient, and a saddle with S = 0 can obstruct). Checked here: the identities Gamma_t + b.grad Gamma =
nu L Gamma and b.grad Gamma = {psi, Gamma}/R, and the deficit rate int_0^infinity (L Gamma_B) R dR = - 2 Gamma_infinity for the Burgers profile,
in sympy; the superlevel argument, the Taylor-coefficient obstruction at a saddle and the envelope bound by hand, with
int_0^infinity min(M, N/u^2) du = 2 (M N)^{1/2} in sympy and ||d_zz G_u||_1 = (2/(pi e))^{1/2}/u <= 1/u for the one-dimensional heat kernel G_u (coefficient
approximately 0.483941), by hand and by quadrature; the characteristic inequality by hand and the Burgers axis strain
a = - gamma kappa/2 - A'/(2A) in sympy; the exponent count D_n kappa_n >= c D_n^{14/15}. The second model's own script was rerun (exit 0). A narrow audit of the
first version of this text by the second model found that it overstated the scope of the persistence bound (applying it to the swirl of
Appendices B and C, which vanishes on the axis, and to all coupled families) and omitted the periodicity, sign and transport qualifications;
these were checked and corrected.
(25) The tail computation for swirl records near the limiting packet in Section 4 (Use of the branch hypotheses) was derived by the second
model, in answer to a request for new mechanisms outside the failed approaches; it found no new route. Its derivation already used
terminal-inclusive convergence to obtain the off-axis packet; the uniform lower bound for all d_n > 0 extends its crossover and
intermediate-radius estimates. Checked here: the change of variables and the case split by hand; the values of d/b^2 at the crossover and at
intermediate radii and the crossing of the caps b <= min(2 C_* delta_n d, G nu_n/d) at d = delta_n/2^{1/2} with value 2^{1/2} C_* delta_n^2,
in sympy; the second model's own script was rerun (26 exact checks, exit 0). A narrow audit of the first version of this text by the second
model found that it did not restrict the swirl record times to s_n <= t_n, where the caps of F9 in the units of t_n apply, stated the packet
condition loosely and overstated the limitation to earlier times; that audit also verified seven exact algebraic identities. These points
were checked here and corrected; a second narrow audit of the corrected text found no error.

Literature. The texts of Shahmurov (arXiv:2604.21213v3: Proposition 2.1, the balance (3.9), Theorem 3.1, Corollary 3.5, Theorems 6.1
and 7.1), the statements of the later Shahmurov papers cited in F5 (their proofs were checked only by the second model, where used), Seregin (arXiv:2402.13229v3, 2507.08733v2, 2606.29468v1), Constantin-Ignatova-Vicol (arXiv:2609.20762; arXiv:2609.20803, statements and proof outline only), Zhang
(arXiv:2604.07785), Nobili-Seis (arXiv:1906.07400), Hou (arXiv:2107.06509v2, Section 3.4.1) and Hou-Shi-Wang (arXiv:0912.1316v2: the
model, Theorem 1.1 and the statement of Section 4; the blowup proofs were not checked) and Hou-Li (arXiv:math/0608295v1: the 1D model,
its exact-solution property and the maximum principle as stated in Section 1; the differential identity behind it was rederived here,
the remaining proofs were not checked) were read here, as were the statements of Dascaliuc-Grujic (arXiv:1205.7080v1, Section 1),
Grujic (arXiv:1111.0217, Section 4) and Barker-Fernandez-Dalgo-Prange (arXiv:2302.06509v2, Theorem A) used in F5; the Hou-Lei paper is cited
from that text. The statements of
Koch-Nadirashvili-Seregin-Sverak used in B2 (Acta Math. 203 (2009)) were checked here against the arXiv version (arXiv:0709.3599v1:
Theorems 5.1 and 5.2, Remark 6.1, Proposition 4.1, Lemmas 4.1 and 6.1, whose numbering is used here); the journal text was not consulted. The results of Chen-Strain-Tsai-Yau, Lei-Zhang, Wei and Lei-Navas-Zhang in F5 were checked against abstracts
only and serve as literature leads. The locations of the kernel estimate of Section 2.9 in the papers of Shirota and Yanagisawa and of
Abidi, Hmidi and Keraani, and a further antecedent (Lei and Zhang, Pacific J. Math. 289 (2017), Section 4), were not checked against the
originals; the estimate is proved in Section 2.9 and does not depend on them. No theorem from the Burgers-vortex literature is applied.
A decay theorem for global axisymmetric solutions (Y. Liu, arXiv:2103.11200, Theorem 1.1) assumes global existence and gives no uniform
relaxation time; it is not used. The other numerical candidates in F11 were not checked against the papers.

The audit records and the scripts are not reproduced here. The computations check the specified identities, constants and examples;
they do not replace the analytic proofs or establish any of the open implications.

## Appendix A. Proof of the claim of Section 4 (x)

Fix C > 0 and G > 0, and put mu = C/G. All constants chosen below are independent of delta. In this appendix the letters A, D, H, K, L and P
denote the constants fixed in (A8), Q denotes the radial transmission variable defined before (A44), and G_occ, G_j are an occupation kernel
and an event; none of them is a quantity of Sections 1-2 (historical suprema, Q_4 or the circulation bound), and U is the prescribed field
of Section 4 (x), not a limit of Navier-Stokes rescalings. Norms of vectors are Euclidean, and norms of derivative tensors are Frobenius
norms. Spatial derivatives and their sup norms are Cartesian unless another variable is specified. An integral without limits in the
variable z is over the real line. A killed process has terminal payoff zero after absorption.

We prove the following precise statement. There are K in (0, 1), L > 0 and alpha > 0, depending only on the fixed profiles and C, G, such
that, for every sufficiently small delta > 0 and nu = mu delta^3, the field constructed below is smooth, compactly supported in space,
axisymmetric, swirl-free and divergence-free, and satisfies, at every physical time t,

(A1) |U| <= 1, |grad U| <= 1, |grad^2 U| <= C, |d_t U| <= C(1 + C).

For the fixed packet phi specified below, let psi be the bounded solution, continuous with value zero on the axis, of

(A2) d_s psi = U(R, Z, -s).grad psi + nu (d_RR psi - R^(-1) d_R psi + d_ZZ psi), psi(R, Z, 0) = phi(R, Z).

With r_c = delta/sqrt(2), define

(A3) w_nu(R) = R/r_c^2 for 0 <= R <= r_c, and w_nu(R) = r_c^2/R^3 for R >= r_c; V_nu(s) = int_0^infinity w_nu(R) int |d_Z psi(R, Z, s)| dZ
dR.

Then the asserted lower bound holds with the constant in Section 4 (x):

(A4) V_nu(s) >= c/delta for K/(4 nu) <= s <= K/nu, where c = alpha log(2)/(256 L).

The integral defining V_nu may initially be interpreted as an extended nonnegative integral. The proof of its lower bound uses a compactly
supported dual test and requires no upper bound for it.

Here are the profiles, with their normalizations fixed. Define rho(x) = exp(-1/x) for x > 0 and rho(x) = 0 for x <= 0, and set

(A5) h(x) = rho(x)/(rho(x) + rho(1 - x)); I_zeta = int rho(v + 2) rho(-1 - v) dv; zeta(z) = rho(z + 2) rho(-1 - z)/I_zeta.

The denominator defining h is positive everywhere. Thus h is smooth, is zero on (-infinity, 0], is one on [1, infinity), and satisfies
h(x) + h(1 - x) = 1. On (0, 1), the derivative of log(h/(1 - h)) is 1/x^2 + 1/(1 - x)^2, so h is increasing. The number I_zeta is positive and
finite; zeta is nonnegative, smooth, supported in [-2, -1], and has integral one.

Define the packet and the axial test envelope by

(A6) Phi(X) = (X/8) h(8X - 1) [1 - h((X - 4)/2)], xi(z) = h(z + 2) [1 - h(z - 19)], phi(R, z) = Phi(R^2) xi(z), g_0(z) = h(4(z + 4))
h(4(-3 - z)).

In particular, 0 <= Phi(X) <= min(1, X/8) for X >= 0, Phi = X/8 on [1/4, 4], and phi is a smooth Cartesian packet supported in {1/8 <= R^2
<= 6, -2 <= z <= 20}. Also 0 <= xi <= 1 and xi = 1 on [-1, 19]. The function g_0 rises monotonically from zero to one on [-4, -15/4], equals
one on [-15/4, -13/4], and falls monotonically to zero on [-13/4, -3]. Consequently

(A7) 0 <= g_0 <= 1, supp g_0 subset [-4, -3], m_z := int g_0 >= 1/2, and int |g_0'| = 2.

We specify the entire constant hierarchy. All norms of one-variable profiles in the next display are over the real line. The integrand
involving h in H is evaluated on (0, 1):

(A8) H = 1 + ||h'||_infinity + int_0^1 (|h''| + h'^2/h) dz;
A = 2 + H + ||Phi'||_infinity
    + sum_(j=0)^3 (||h^(j)||_infinity + ||zeta^(j)||_infinity)
    + sum_(j=1)^3 sup_(0<z<1) |h^(j)(z)|/[h(z)(1 + |log h(z)|)^(2j)];
D = 10^12 A^20;
alpha = 1/(10^5 D), K = (alpha/(10^5 D))^2, b = 16/K;
lambda = mu b, eps = alpha lambda, L = 8 + 100 D eps/C.

These numbers are finite. To check the only endpoint issue, near zero write h(z) = exp(-1/z) a(z), where a is smooth and positive, with
bounded first three derivatives and with a bounded away from zero. Differentiation gives |h^(j)| <= constant times h z^(-2j), for j = 1, 2,
3, while log h = -1/z + log a. It also gives h'^2/h <= constant times exp(-1/z) z^(-4), which is integrable. Away from zero h is bounded
away from zero; flatness at one controls its derivatives there. These observations prove finiteness of every term in (A8). In particular A
>= 2, H <= A and P := ||Phi'||_infinity <= A. The numerical choices imply K < 1, b > 16, H/b < 1/2, 20 A alpha < 1/5, and D eps/L <= C/100.

Choose delta > 0 small enough that all of the following hold, and write l = L delta and ell = 1 + |log delta|:

(A9) delta <= 1/10; l <= 1/(10^5 D);
4 exp(-b/(2 delta^2)) <= alpha/1000;
D lambda delta ell^6 <= min(1/4, C/4);
D eps L delta^2 <= 1/4; D eps delta <= 1/4;
D eps lambda delta^2 <= C(1 + C)/2.

Each is an eventual smallness condition on delta with the preceding constants fixed, so they can all hold simultaneously. They imply l < 1
and l <= m_z/2.

Set

(A10) d(z) = d_delta(z) = delta^2 + (1 - delta^2) h(z);
B(z) = [nu b/d(z)] h(z + 7) [1 - h(z - 19)];
chi(q) = 1 - h((4q - 1)/3), chi_m(q) = 1 - h((q - 1)/3);
Theta(z, t) = (z - lambda delta t)/l;
S_0(R, z) = (R^2/2) B(z) chi(R^2/64);
S_1(R, z, t) = -eps L delta^2 R^2 zeta(z) sin(Theta(z, t)) chi_m(R^2/l^2).

Define U = U_0 + U_1 by the stream-function convention U^R = -S_Z/R, U^Z = S_R/R, U^theta = 0, using S = S_0 + S_1. This convention fixes
all signs. If S = R^2 T(R^2, z, t), its Cartesian expression, with x_h = (x_1, x_2), is

(A11) U_h = -x_h T_z, U^Z = 2(T + R^2 T_(R^2)).

This is smooth on the axis. Its horizontal divergence is -2T_z - 2R^2 T_(R^2)z, which cancels d_Z U^Z. Thus the field is divergence-free
everywhere. It vanishes for R >= 8 and outside -7 <= z <= 20. The modulation alone vanishes for R >= 2l and outside [-2, -1]. The base is
radial-linear for R <= 4; the modulation is radial-linear for R <= l.

We give Cartesian bounds including the cutoffs. Put k_0 = 1 - delta^2 and v_delta = delta^2/d. Its first three derivatives are

(A12) v_delta' = -delta^2 k_0 h'/d^2;
v_delta'' = 2 delta^2 k_0^2 h'^2/d^3 - delta^2 k_0 h''/d^2;
v_delta''' = -6 delta^2 k_0^3 h'^3/d^4 + 6 delta^2 k_0^2 h'h''/d^3 - delta^2 k_0 h'''/d^2.

Here is an explicit explanation of the logarithmic loss. A product in (A12) with total derivative order j and p differentiated h factors is
bounded, apart from its displayed numerical coefficient, by A^p delta^2 h^p d^(-p-1)(1 + |log h|)^(2j). If h >= delta^2, the fraction
delta^2 h^p/d^(p+1) is at most one and 1 + |log h| <= 2 ell. If h <= delta^2, put h/delta^2 = exp(-v), v >= 0. The same fraction is at most
exp(-pv) <= exp(-v), and 1 + |log h| <= 2 ell + v. Since delta <= 1/10 implies 2 ell >= 6, the function exp(-v)(2 ell + v)^m decreases for 0
<= m <= 6. This proves, including the regions where derivatives vanish,

(A13) ||v_delta||_infinity <= 1, ||v_delta'||_infinity <= 4 A ell^2,
||v_delta''||_infinity <= 48 A^2 ell^4,
||v_delta'''||_infinity <= 832 A^3 ell^6.

The derivatives of h(z + 7) are supported in [-7, -6], and those of 1 - h(z - 19) in [19, 20]. These sets are disjoint from [0, 1] and from
each other. On each of them v_delta is constant. Therefore no mixed product of derivatives from a cutoff and v_delta survives. Since nu b/d
= lambda delta v_delta, (A13) gives

(A14) sum_(j=0)^3 ||B^(j)||_infinity <= 1000 A^3 lambda delta ell^6.

For completeness, the radial cutoff costs are as follows. In R <= 8 put q = R^2/64, F = chi(q), E = chi(q) + q chi'(q), and p_i = x_i F.
Then |q_i| <= 1/4 and |q_ij| <= 1/32. For j = 1, 2, 3, |chi^(j)| <= 3A. Consequently the following componentwise bounds hold for horizontal
indices i, j, k:

(A15) |F| <= 1, |F_i| <= 3A/4, |F_ij| <= 9A/32;
|E| <= 4A, |E_i| <= 3A, |E_ij| <= 2A;
|p_i| <= 8, |d_j p_i| <= 7A, |d_jk p_i| <= 4A.

For example E'(q) = 2chi'(q) + q chi''(q) and E''(q) = 3chi''(q) + q chi'''(q), bounded by 9A and 12A. These give |E_ij| <= 12A/16 + 9A/32 <
2A. The bounds for p_i follow by differentiating x_i F twice. Now U_0^i = -B'p_i/2 and U_0^Z = BE. Every component of a derivative of order
at most two is at most 4A sum_(j=0)^3 ||B^(j)||_infinity. There are respectively 3, 9 and 27 components in the three tensors. Since
4(sqrt(3) + 3 + sqrt(27)) < 100, (A14) gives

(A16) sup_(x,t) (|U_0| + |grad U_0| + |grad^2 U_0|) <= 10^5 A^4 lambda delta ell^6 <= D lambda delta ell^6.

The modulation can be checked without cylindrical derivative estimates. Write y = x_h/l, q = |y|^2, v(z, t) = zeta(z) sin Theta, P_i(y) =
y_i chi_m(q), and E_m(y) = chi_m(q) + q chi_m'(q). On |y| <= 2, the componentwise bounds are

(A17) |P_i| <= 2, |d_j P_i| <= 9A, |d_jk P_i| <= 44A;
|E_m| <= 5A, |d_j E_m| <= 24A, |d_jk E_m| <= 124A;
|d_z^j v| <= 2^j A l^(-j) for 0 <= j <= 3;
|d_t v| <= A lambda/L, |d_zt v| <= 2A lambda/(Ll).

Indeed |chi_m^(j)| <= A for 1 <= j <= 3, |d_i q| <= 4 and |d_ij q| <= 2. Thus the first and second y derivatives of chi_m(q) are at most 4A
and 18A. Differentiating y_i chi_m(q) gives 9A and 44A. The q derivatives of chi_m + q chi_m' are at most 6A and 7A, giving 24A and 124A
after composition. The last two lines of (A17) follow by the product rule and |d_z Theta| = 1/l, |d_t Theta| = lambda/L.

In these variables the exact velocity is

(A18) U_1^i = eps L delta^2 l P_i(y) v_z, U_1^Z = -2 eps L delta^2 E_m(y) v.

For each mixed spatial derivative of order j <= 2, (A17)-(A18) bound each component by 250 A^2 eps L delta^2 l^(-j). For the horizontal
components the largest coefficient needed is 88A^2; for the vertical components it is 248A^2. For time derivatives the largest component
coefficient is 10A^2 eps lambda delta^2. Counting tensor components as above, and using 10^4 A^2 <= D, proves

(A19) ||U_1||_infinity <= D eps L delta^2, ||grad U_1||_infinity <= D eps delta,
||grad^2 U_1||_infinity <= D eps/L, ||d_t U_1||_infinity <= D eps lambda delta^2.

Outside the stated cutoff supports all these derivatives are zero. Equations (A9), (A16) and (A19) give |U| <= 1/2, |grad U| <= 1/2 and
|grad^2 U| <= C/4 + C/100 < C, as well as the time bound (A1). They also prove U -> 0, grad U -> 0 and d_t U -> 0 uniformly as delta -> 0.
The Hessian bound uses the cutoff at radius l; keeping that cutoff at a fixed radius would not give (A19).

We next fix the diffusion and the analytic meaning of (A2). The stochastic facts used below are Ito's formula; the Ito isometry E|int a
dW|^2 = E int |a|^2 for square-integrable adapted integrands; and the strong Markov property of Brownian motion, which says that increments
after an almost surely finite stopping time form Brownian motion independent of the information at that time. We also use Doob's inequality:
for a continuous square-integrable martingale N with N_0 = 0,

(A20) E sup_(0<=u<=T) |N_u|^2 <= 4 E|N_T|^2 = 4 E<N>_T.

These facts, including their stopped versions, are recorded in A. Etheridge, Continuous martingales and stochastic calculus (2018), in the
sections on the strong Markov property, martingale inequalities, stochastic integration and Ito's formula. Local stochastic integrals below
are first stopped where their integrands and processes are bounded. A finite expected quadratic variation then permits removal of this
localization by the Ito isometry and (A20).

For fixed s, start at (R, z) at physical time -s, and use elapsed physical time u. With independent one-dimensional Brownian motions W^R and
W^Z, run

(A21) dR_u = (U^R(R_u, Z_u, -s + u) - nu/R_u) du + sqrt(2nu) dW^R_u;
dZ_u = U^Z(R_u, Z_u, -s + u) du + sqrt(2nu) dW^Z_u.

The coefficients are locally Lipschitz on R > 0. Solve up to the first time tau_0 that R reaches zero, then absorb. There is no finite
escape to infinity: before absorption, R_u <= R_0 + u + sqrt(2nu) W^R_u and |Z_u - Z_0| <= u + sqrt(2nu)|W^Z_u|. The existence and pathwise
uniqueness assertion here is the local version of the Lipschitz SDE theorem, obtained by truncating coefficients on compact subsets; see
Etheridge, C8.2: Stochastic analysis and PDEs (2016), Section 3.2. Equivalently, X = R^2 satisfies, up to absorption and then with X = 0,

(A22) dX_u = 2R_u U^R(R_u, Z_u, -s + u) du + sqrt(8nu X_u) dW^R_u.

In particular there is no constant radial drift in the X equation. This cancellation is essential.

The representation of the adjoint is

(A23) psi(R, z, s) = E_(R,z) [phi(R_s, Z_s) 1_{tau_0>s}], 0 <= psi(R, z, s) <= min(1, exp(2s) R^2/8).

Here are details justifying both the singular boundary and classical interior regularity. We use the following textbook parabolic fact: a
uniformly elliptic Cauchy equation on Euclidean space, with smooth bounded coefficients and derivatives and a smooth bounded zeroth-order
coefficient, has a unique solution bounded on each finite time interval for smooth bounded initial data; the solution is classical in the
interior. See A. Friedman, Partial Differential Equations of Parabolic Type (1964), the Cauchy-problem and interior-regularity results.

In the present problem this fact can be applied without a singular coefficient. Write psi = R^2 v and lift R to the radius in four
horizontal dimensions, retaining the axial coordinate as a fifth dimension. Direct differentiation gives

(A24) [d_RR - R^(-1)d_R + d_ZZ](R^2 v) = R^2 (d_RR v + 3R^(-1)d_R v + d_ZZ v);
R^(-2) U.grad(R^2 v) = U.grad v + (2U^R/R)v.

The lifted drift is ((U^R/R)y, U^Z) for y in R^4. Formula (A11) shows that it and the potential 2U^R/R are smooth, with bounded derivatives
for each delta, including at y = 0. The drift is bounded. Moreover |U^R/R| <= 1, since the horizontal Cartesian velocity vanishes on the
axis and |grad U| <= 1. The initial v is phi/R^2, extended by zero at the axis; it is smooth and between zero and 1/8. To obtain its bound,
run the lifted diffusion from physical time -s to zero and apply Ito's formula to v at remaining age s-u, multiplied by exp(int_0^u (2U^R/R)
dv), with the potential evaluated along that diffusion. The drift cancels. On a fixed time interval the resulting local martingale is
bounded, because v is bounded and the potential has absolute value at most two. Removing spatial stopping and evaluating at u=s expresses v
as the expectation of its nonnegative initial value times this exponential. Hence 0 <= v <= exp(2s)/8. The lifted solution is rotationally
invariant by uniqueness.

Thus R^2 v solves (A2), is continuous with value zero on the axis, and has at most quadratic growth in R. Apply Ito's formula to (R^2
v)(R_u, Z_u, s-u), stopped at u=s, R=kappa, R=n, or |Z|=n. Its drift is zero, because the physical time in (A21) is -s+u. At R=kappa its
value is at most kappa^2 exp(2s)/8. The contribution from the other artificial boundaries tends to zero as n -> infinity: the pathwise
bounds following (A21) bound the stopped R^2 by an integrable random variable, and the probability of such an exit tends to zero. Dominated
convergence, followed by kappa -> 0, gives (A23). At absorption phi is zero. This argument also gives the bound by one.

For uniqueness, apply the same stopped Ito argument to the difference of any two bounded classical solutions continuous with zero axis value
and the given initial value. First let kappa -> 0 with the other spatial boundaries fixed; continuity gives uniform convergence to zero on
the compact axis-time boundary. Then let n -> infinity and use boundedness and the nonexplosion bounds. The difference is zero. This proves
the claimed analytic and probabilistic interpretation of (A2). The Feynman-Kac martingale argument in bounded domains is also stated in
Etheridge (2016), Section 7.3, especially Theorem 7.27.

We will compare (A21) with fields that are radial-linear everywhere. If U^R = a(z,t)R and U^Z = w(z,t), the axial process has coefficients
independent of R. It need not be autonomous in time. Given its entire axial path, the radial equation has deterministic coefficients. Put

(A25) A_u = int_0^u a(Z_v, -s+v) dv, I_u = int_0^u exp(-2A_v) dv.

Conditionally on that path, integration by a deterministic factor and change of time give the following equality of path laws:

(A26) X_u = exp(2A_u) beta(2nu I_u), where d beta_t = 2 sqrt(beta_t) dB_t, beta_0 = X_0, and beta is absorbed at zero.

For clarity, beta can be chosen independent of the axial path when forming this conditional law. This does not assert independence of an
arbitrary Brownian motion obtained from an unconditional random time change. To verify (A26), the process Y_u = exp(-2A_u)X_u has diffusion
coefficient sqrt(8nu exp(-2A_u)Y_u); the clock 2nu I_u changes this coefficient to 2sqrt(Y).

The absorption and moment normalizations can also be checked directly. For q >= 0 the function exp(-xq/(1+2tq)) solves d_t F = 2x d_xx F
with initial value exp(-qx). Stopped Ito's formula, bounded convergence, and then q -> infinity give

(A27) E exp(-q beta_t) = exp(-X_0 q/(1+2tq));
P(X_u=0 | axial path) = exp(-X_0/(4nu I_u));
E(X_u | axial path) = X_0 exp(2A_u);
Var(X_u | axial path) = 8nu I_u X_0 exp(4A_u).

The moment identities follow either by differentiating the Laplace transform at q=0, using monotone difference quotients, or by stopped
Ito's formula for beta and beta^2. This also supplies the nonexplosion and moment bounds needed for the radial comparison. All comparisons
below are coupled by the same driving Brownian motions until their coefficients cease to agree.

We now estimate passage through the jet. Fix 1 <= r <= sqrt(2), -4 <= z <= -3, and an age s in the interval of (A4). Start with X_0 =
delta^2 r^2, Z_0 = z, and put theta = (z + lambda delta s)/l. The globally radial-linear jet comparison uses

(A28) w(z,t) = lambda delta + w_1(z,t), w_1 = -2eps L delta^2 zeta(z) sin Theta(z,t);
a_1(z,t) = eps delta zeta(z) cos Theta(z,t) + eps L delta^2 zeta'(z) sin Theta(z,t).

Indeed a_1 = -d_z w/2. This process agrees with the actual field while -6 <= Z <= 0 and R <= l. Its axial coefficients are time dependent
but independent of R. Let tau_j be its first hitting time of Z=0, and define

(A29) T_j = 10/(lambda delta), rho_j = min(tau_j, T_j), A_u = int_0^(u cap rho_j) a_1(Z_v, -s+v) dv.

Here and below "cap" in a time limit means minimum. We have |w_1| <= 2A alpha lambda delta l <= lambda delta/4 and |A_u| <= 20A alpha <=
1/5. For the axial Brownian event

(A30) E_z = {sup_(u<=T_j) |sqrt(2nu) W^Z_u| <= 1/2}, P(E_z^c) <= 320 delta^2/b.

The probability follows from (A20), since E sup |sqrt(2nu) W^Z|^2 <= 8nu T_j = 80delta^2/b. On E_z the axial drift is at least 3lambda
delta/4, so Z_u >= z - 1/2 >= -9/2 up to tau_j. Also Z_(T_j) >= -4 + 15/2 - 1/2 = 3 if it has not hit zero earlier. Continuity therefore
implies tau_j <= T_j on E_z.

The phase estimate must retain the physical time dependence. Directly from (A28),

(A31) Theta(Z_u, -s+u) - theta = l^(-1) int_0^u w_1(Z_v,-s+v) dv + sqrt(2nu) W^Z_u/l;
E sup_(u<=rho_j) |Theta(Z_u,-s+u)-theta| <= 20A alpha + 9/(L sqrt(b)).

For the last term we used sqrt(80)/(L sqrt(b)) < 9/(L sqrt(b)). Define J(z) = int_(-infinity)^z zeta(v) dv. Its value changes from zero to
one between the initial point and Z=0. Ito's formula at tau_j, on the event H_j = {tau_j <= T_j}, gives the exact identity

(A32) lambda delta int_0^tau_j zeta(Z_u) du
= 1 - int_0^tau_j zeta(Z_u) w_1(Z_u,-s+u) du
    - nu int_0^tau_j zeta'(Z_u) du
    - sqrt(2nu) int_0^tau_j zeta(Z_u) dW^Z_u.

Its three error terms, in expected absolute value restricted to H_j, are bounded respectively by

(A33) 20A^2 alpha l, 10A delta^2/b, and 5A delta/sqrt(b).

For the last bound use the stochastic integral stopped at rho_j, whose variance is at most 2nu A^2 T_j = 20A^2 delta^2/b. Its value agrees
with the integral in (A32) on H_j. In particular no martingale is being conditioned on a future Brownian event.

Write a_delta for the following deterministic bound:

(A34) E[1_(H_j) |A_tau_j - alpha cos theta|] <= a_delta,
a_delta = 400A^2 (alpha^2 + alpha/(L sqrt(b)) + alpha l).

To check it, replace cos Theta by cos theta in the first term of a_1. The error is at most 10A alpha times the right side of (A31). The
second term of a_1 contributes at most 10A alpha l. The remaining error is alpha times the sum of (A33). These bounds sum to at most
a_delta: use l <= 1, delta <= 1/L, b >= 1 and A >= 2. This writes out both the phase error and the error from integrating the axial
envelope.

Control of the radial jet fluctuation is equally explicit. Extend the processes constantly after rho_j when necessary, and set

(A35) M_u = exp(-2A_u) X_(u cap rho_j)/delta^2, M_0 = r^2;
d<M>_u = (8nu/delta^2) exp(-2A_u) M_u 1_(u<rho_j) du.

This is a nonnegative square-integrable martingale. To justify that assertion without assuming the conclusion, stop also when M reaches n.
The stopped first moment equals r^2. The bracket formula, exp(-2A) <= exp(2/5), and r^2 <= 2 give a bound independent of n. The Ito isometry
then gives a uniform second-moment bound, which permits removal of this additional stopping and proves the martingale assertion. More
precisely,

(A36) E<M>_(T_j) <= 160exp(2/5)/b < 240/b;
E sup_(u<=T_j) |M_u-r^2|^2 <= 960/b.

If the jet comparison reaches R=l before rho_j, then M >= exp(-2/5)L^2, so |M-r^2| > 1, because L >= 8. Its probability is therefore at most
960/b.

Put q_theta = r^2 exp(2alpha cos theta). The choices in (A8) give 9/10 <= q_theta <= 9/4. On H_j define Q_0 = X_tau_j/delta^2. The moment
estimate and (A34) imply

(A37) E[1_(H_j)|Q_0-q_theta|] <= 24/sqrt(b) + 6a_delta.

Indeed the contribution of M_tau_j-r^2 is at most exp(2/5)sqrt(240/b) < 24/sqrt(b). The map a -> exp(2a) has derivative at most 2exp(2/5) <
3 on [-1/5,1/5]; multiplication by r^2 <= 2 gives the other term.

Define the successful jet event G_j by all four requirements: tau_j <= T_j; Z_u >= -9/2 for u <= tau_j; R_u < l for u <= tau_j; and 1/2 <=
Q_0 <= 3. This event is measurable at tau_j on {tau_j <= T_j}; it does not impose any condition on Brownian increments after tau_j. The
preceding arguments give

(A38) P(G_j^c) + E[1_(G_j)|Q_0-q_theta|] <= j_delta,
j_delta = 10^5 A^3 (alpha^2 + b^(-1/2) + alpha l).

For verification, the first two requirements fail with probability at most 320delta^2/b by (A30), and the radial requirement fails with
probability at most 960/b. Since q_theta is at distance at least 1/3 from the complement of [1/2,3], the endpoint requirement contributes at
most three times the right side of (A37). Adding the expected endpoint error contributes one more copy. Thus the left side of (A38) is at
most
320delta^2/b + 960/b + 4(24/sqrt(b) + 6a_delta).
Substitution of (A34), with delta <= 1, alpha/L <= 1 and A >= 2, bounds this by the displayed j_delta. Absorption in the jet has Q_0=0 and
is included in this failure estimate. On G_j the actual field and the jet comparison agree until tau_j.

After this successful exit, use slow time tau = nu(u-tau_j), reset Z_0=0 and X_0=delta^2 Q_0, and consider the uncut autonomous base
comparison. Its equations, with fresh independent Brownian drivers, are

(A39) dZ_tau = [b/d(Z_tau)] dtau + sqrt(2) dW^Z_tau;
dX_tau = [b d'(Z_tau) X_tau/d(Z_tau)^2] dtau + sqrt(8X_tau) dW^R_tau.

The second process is absorbed at X=0. Its axial equation continues independently of radial absorption. This continuation is used for all
occupation and return estimates.

We derive the occupation bound rather than presume it. Put f=d/b, F(x)=int_0^x 1/f(v) dv, and gamma=||f'||_infinity <= H/b < 1/2. Since f is
positive, increasing and Lipschitz, f(y+v) <= f(y)+gamma v for v >= 0. It follows, for gamma>0, that

(A40) F(y+v)-F(y) >= gamma^(-1) log(1+gamma v/f(y));
int_0^infinity exp(-(F(y+v)-F(y))) dv <= f(y)/(1-gamma) <= 2d(y)/b.

When gamma=0 the same integral is f(y), by direct integration. Define the occupation kernel by

(A41) G_occ(x,y) = exp(F(y)) int_(max(x,y))^infinity exp(-F(v)) dv <= 2d(y)/b.

Here the subscript distinguishes this kernel from the parameter G in mu=C/G. To verify that it is the occupation kernel, take a nonnegative
smooth compactly supported function k and put u(x)=int G_occ(x,y) k(y) dy. Formula (A40) makes u bounded. Differentiation under this
integral gives
u'(x) = -exp(-F(x)) int_(-infinity)^x exp(F(y))k(y)dy,
and hence u'' + f^(-1)u' = -k. Also u(x) -> 0 as x -> infinity, because k has compact support and int_x^infinity exp(-F) -> 0. Ito's
formula, first with compact spatial stopping and then with that stopping removed, gives
E int_0^T k(Z_tau) dtau = u(x) - E u(Z_T).
The removal is justified by bounded u and its bounded derivatives, and by nonexplosion for the bounded drift b/d. Pathwise Z_T >=
x+bT+sqrt(2)W_T, which tends to infinity almost surely. Bounded convergence and then monotone convergence prove

(A42) E_x int_0^infinity k(Z_tau) dtau = int G_occ(x,y) k(y)dy.

For completeness, the Brownian limit used here follows from (A20): for kappa>0, P(sup_(u<=2^n)|W_u|>kappa 2^n)<=4/(kappa^2 2^n). The sum
over n is finite, and the union bound on its tails implies that only finitely many such events occur, almost surely. Taking kappa through
the positive reciprocals of integers and placing T between successive powers of two proves W_T/T -> 0.

The formula extends to every nonnegative Borel k by equality of the locally finite occupation measures first tested on smooth compactly
supported functions. Their local finiteness follows by majorizing the indicator of any compact interval by such a test function in (A42).
Thus no occupation estimate below requires a radial survival condition.

We will use two consequences starting from Z_0=0. For y<0, F(y)=by/delta^2, so (A41) also gives G_occ(0,y) <= (2delta^2/b)exp(by/delta^2).
Since d'=d''=0 outside [0,1], and
int_0^1 (|d''|+d'^2/d) <= int_0^1 (|h''|+h'^2/h) <= H,
we obtain, for any deterministic T <= K,

(A43) E int_0^T (|d''|/d + d'^2/d^2)(Z_tau) dtau <= 2H/b;
E int_0^T (2d'^2/d^2)(Z_tau) dtau <= 4H/b;
E int_0^T 1/d(Z_tau) dtau <= K + 2/b + 2delta^2/b^2 <= K + 4/b.

For the last line, the part with Z<0 is bounded by
int_(-infinity)^0 (2/b) exp(by/delta^2)dy = 2delta^2/b^2.
The part with 0<=Z<=1 is at most int_0^1 2/b dy = 2/b, and the part with Z>=1 is at most T, because d=1 there. This accounts separately for
the transition, the upstream region and the pool.

The radial transmission variable is Q=X/d(Z). The generator of (A39), in variables (X,Z), is

(A44) A_base = d_ZZ + (b/d)d_Z + (b d' X/d^2)d_X + 4X d_XX.

Ito's formula, at X>0, gives the exact identity

(A45) d log Q = (d'^2/d^2 - d''/d - 4/X) dtau
                + sqrt(8/X) dW^R - sqrt(2)(d'/d) dW^Z.

For example d log X has drift b d'/d^2 - 4/X, while d log d(Z) has drift b d'/d^2 + d''/d - d'^2/d^2. This displays the cancellation of the
large convective term. The two noise terms have zero mutual quadratic variation.

The stopping convention is part of the estimate. For 1/2 <= Q_0 <= 3 define sigma to be the first time Q hits either 1/4 or 4, that is, the
first exit from the open interval (1/4,4). Use (A45) only up to tau cap sigma, and keep the stopped logarithm constant thereafter. The
identity is never used at X=0. Before sigma, X=Qd >= d/4 and X <= 4. Since d >= delta^2, the stopped identity has no singular integrand for
each fixed delta.

Using (A43) in its drift and bracket, and then (A20), proves

(A46) E sup_(0<=tau<=T) |log Q_(tau cap sigma)-log Q_0| <= e_*,
e_* = (2H+64)/b + 16K + 2sqrt(32K + (128+4H)/b)
    <= 200A (sqrt(K) + b^(-1/2)), for T <= K.

Indeed the expected integral of the absolute drift is at most 2H/b + 16(K+4/b). The expected martingale bracket is at most 32(K+4/b)+4H/b.
The expected supremum of that martingale's absolute value is at most twice the square root of its expected bracket by (A20) and
Cauchy-Schwarz. These are exactly the first expression for e_*. To check the last inequality, use H<=A, K<=1, b>=1,
sqrt(a+b)<=sqrt(a)+sqrt(b), and A>=2: the terms are at most 28sqrt(K) + (34A+2sqrt(68A))b^(-1/2), which is below the stated bound.

The smallest logarithmic distance from Q_0 in [1/2,3] to a stopping boundary is log(4/3)>1/4. Also the exponential function has derivative
at most four between log(1/4) and log(4). Consequently

(A47) P(sigma<=T) <= 4e_*, and E[1_(sigma>T)|Q_T-Q_0|] <= 4e_*.

Absorption before T requires crossing Q=1/4 and is included in the first probability. Reaching the base radial cutoff R=4 also requires a
preceding Q exit, since R<=2 before sigma. Thus (A47) controls both radial absorption and loss of radial coupling; it does not purport to
estimate log Q after absorption.

We still need axial return and endpoint estimates. The scale function for (A39) has derivative exp(-F). Solving v''+(b/d)v'=0 with values
one and zero at the endpoints of [a,n] gives the probability of hitting a before n:
int_x^n exp(-F(v))dv / int_a^n exp(-F(v))dv.
This follows directly by applying stopped Ito's formula to that bounded function. The exit time from a finite interval is almost surely
finite: on each time interval of length one, a sufficiently large positive Brownian increment forces an exit unless it has occurred already,
since the drift is positive; the strong Markov property then gives a geometric bound for remaining in the interval. Taking n -> infinity,
using Z_tau -> infinity, gives the probability of ever hitting a.

In particular, from x=0 and a=-1/2, (A40) and the exact negative-side value of F imply

(A48) P_0(inf_(tau>=0) Z_tau <= -1/2)
<= 2/[exp(b/(2delta^2))-1] <= 4exp(-b/(2delta^2)).

The denominator integral over [-1/2,0] is (delta^2/b)[exp(b/(2delta^2))-1]; the numerator is at most 2delta^2/b. The last inequality uses
b/(2delta^2)>=log 2. Avoiding -1/2 prevents return to the modulation, whose support ends at -1, and prevents reaching the lower axial cutoff
of B.

For a deterministic residual time 3/b <= T <= K, the pathwise inequality Z_T>=bT+sqrt(2)W_T and Chebyshev's inequality give

(A49) P_0(Z_T<1) <= 2T/(bT-1)^2 <= 4/b.

The function T/(bT-1)^2 decreases for T>1/b. At T=3/b the first bound equals 3/(2b), which is less than 4/b.

To bound upper pool exit, suppose Z first reaches 19 by time K, and let v be its last visit to 1 before that hit, at time u. On [v,u] it
stays in [1,19], where its drift is exactly b. Therefore, pathwise,
19 = 1+b(u-v)+sqrt(2)(W_u-W_v) <= 1+bK+2sqrt(2) sup_(tau<=K)|W_tau|.
Since bK=16, (A20) yields

(A50) P_0(sup_(tau<=K)Z_tau >= 19) <= P(sup_(tau<=K)|W_tau| >= 1/sqrt(2)) <= 8K <= 32K.

The last-visit time in this argument is used only in a pathwise equality. No stopping-time or independence claim is made about it. This
avoids a possible invalid use of the strong Markov property at a last exit.

There is also a direct radial tail bound for the actual field, although (A47) is sufficient for the coupling. It vanishes radially for R>=8.
If an actual trajectory starting below 8 has R_s>8+v, v>0, its last crossing of 8 before s is followed by radial drift -nu/R<=0. Thus
2sqrt(2nu) sup_(u<=s)|W^R_u|>v. At the ages considered here,

(A51) P(R_s>8+v, tau_0>s) <= 32nu s/v^2 <= 32K/v^2.

Together, (A38), (A47)-(A51) account for jet failure, absorption, radial escape, return, failure to reach the pool, and upper pool exit.

We combine the estimates at the random jet exit carefully. On G_j the remaining slow time is T=nu(s-tau_j). Since nu s lies in
[K/4,K]=[4/b,K] and nu T_j=10delta^2/b<=1/b, we have

(A52) 3/b <= T <= K.

Conditionally on the information at tau_j on G_j, T and Q_0 are fixed and the future Brownian increments are fresh independent Brownian
motions. Thus (A43)-(A50), which are uniform in T in this interval and Q_0 in [1/2,3], apply conditionally and hence after averaging. The
event G_j was deliberately defined without the future condition E_z.

Couple the actual process first to the jet comparison and then to (A39). They agree through the terminal time on the event consisting of
G_j, sigma>T, no return to -1/2, no hit of 19, and Z_T>=1. In fact along the base part we then have -1/2<Z<19 and R<=2, so both cutoffs are
inactive and the modulation is absent. At the terminal time 1<=Z_T<=19, d(Z_T)=1, xi(Z_T)=1, X_T=Q_T, and the payoff is Phi(Q_T). The same
coupling gives an explicit bound for the actual process: both its probability of absorption by age s and its probability of reaching R=4 by
that age are at most j_delta + 4e_* + 4exp(-b/(2delta^2)) + 32K. Indeed, on G_j and before a radial stopping, an axial return or an upper
pool exit, the actual radius stays positive and at most two after the jet, and below l during the jet. The four possible failures have
precisely the four bounds just listed.

Since 0<=phi<=1, 0<=Phi(q_theta)<=1, and Phi is P-Lipschitz, the union bound and the expected displacement estimates give

(A53) |psi(delta r,z,s)-Phi(q_theta)|
<= (1+P) j_delta + (4+4P)e_* + 4/b + 32K + 4exp(-b/(2delta^2)).

Indeed the bad jet event costs P(G_j^c), and the jet displacement costs P E[1_(G_j)|Q_0-q_theta|], both controlled by (1+P)j_delta. Radial
failure costs at most 4e_*, and the expected surviving radial displacement costs at most 4P e_*. Equations (A48)-(A50) control the other
three bad events. On their complement the Lipschitz bound applies to the sum |Q_T-Q_0|+|Q_0-q_theta|. Restricting these nonnegative errors
to a smaller good event can only decrease their expectations.

As q_theta is in [1/4,4], Phi(q_theta)=r^2 exp(2alpha cos theta)/8. Taylor's formula with integral remainder gives |exp(x)-1-x|<=x^2
exp(|x|)/2. Since r^2<=2 and alpha is as in (A8),

(A54) |Phi(q_theta)-(r^2/8)(1+2alpha cos theta)| <= alpha^2.

Substitute (A34), (A38) and (A46) into (A53). With P<=A, all coefficients of alpha^2, b^(-1/2), sqrt(K), and alpha l in (A53)-(A54) are at
most 10^6 A^4, hence at most D. For an explicit coefficient check, (1+P)j_delta is bounded by 2*10^5 A^4 times its parenthesis; (4+4P)e_* is
bounded by 1600A^2(sqrt(K)+b^(-1/2)); 4/b<=4b^(-1/2); 32K<=32sqrt(K); and (A54) contributes alpha^2. Therefore the accumulated uniform error
is at most

(A55) E_delta := D(alpha^2+b^(-1/2)+sqrt(K)+alpha l) + 4exp(-b/(2delta^2))
<= alpha(1/10^5 + 1/(4*10^5) + 1/10^5 + 1/10^5 + 1/1000)
= 413alpha/400000 < alpha/100.

Here we used Dalpha^2=alpha/10^5, Dsqrt(K)=alpha/10^5, Db^(-1/2)=alpha/(4*10^5), and (A9). This proves, with all errors uniform in the
initial phase and age,

(A56) |psi(delta r,z,s)-(r^2/8)(1+2alpha cos((z+lambda delta s)/(Ldelta)))| <= alpha/100
for 1<=r<=sqrt(2), -4<=z<=-3, K/(4nu)<=s<=K/nu.

It remains to turn this value estimate into an axial-variation lower bound. Put k=1/l and theta_s(z)=(z+lambda delta s)/l. On the tested
annulus R=delta r, 1<=r<=sqrt(2), formula (A3) gives

(A57) w_nu(delta r)delta = 1/(2r^3);
m_0 := int_1^sqrt(2) dr/(2r^3) = 1/8;
m_R := int_1^sqrt(2) r^2 dr/(2r^3) = log(2)/4.

Use the bounded test g_s(R,z)=1_[delta,sqrt(2)delta](R) g_0(z)sin theta_s(z). Integration by parts only in z, where the test is smooth and
compactly supported, gives

(A58) V_nu(s) >= |int_delta^(sqrt(2)delta) w_nu(R) int psi(R,z,s) d_z[g_0(z)sin theta_s(z)] dz dR|.

There is no radial integration by parts or derivative of the annular indicator. Interior smoothness of psi justifies the axial operation on
this compact set.

The constant term r^2/8 in (A56) integrates to zero. For the oscillating term, integration by parts gives exactly
int cos theta_s d_z(g_0 sin theta_s) dz = k int g_0 sin^2 theta_s dz.
Hence its contribution to the expression inside the absolute value in (A58) is

(A59) (alpha m_R k/4) int g_0(z) sin^2 theta_s(z) dz.

The oscillatory averaging estimate has an explicit error:

(A60) |int g_0 cos(2theta_s) dz| <= ||g_0'||_1/(2k) = 1/k;
int g_0 sin^2 theta_s dz >= m_z/2 - 1/(2k) >= m_z/4.

The first inequality follows by integrating cos(2theta_s)=(2k)^(-1)d_z sin(2theta_s). The last inequality uses l=1/k<=m_z/2.

The value error (A56) contributes in absolute value at most

(A61) E_delta m_0 (k m_z + ||g_0'||_1) <= 2E_delta m_0 k m_z.

Here 2<=k m_z follows again from l<=m_z/2. Also E_delta<=alpha/100 and
1/100 < m_R/(64m_0) = log(2)/32; the last strict inequality follows even from log(2)>1/2. Combining (A58)-(A61), the positive main term is
at least alpha m_R k m_z/16 and the error is at most alpha m_R k m_z/32. Therefore

(A62) V_nu(s) >= alpha m_R k m_z/32 >= alpha log(2)/(256Ldelta).

This is (A4), with precisely the constant asserted in Section 4 (x).

For any fixed K'>=max(1,K), integrate this bound over [K/(4nu),K/nu], an interval of length 3K/(4nu) contained in [0,K'/nu]. Nonnegativity
on the rest of the age interval proves

(A63) (nu/K') int_0^(K'/nu) V_nu(s) ds >= 3cK/(4K'delta)
= (3cK/(4K'))(C/G)^(1/3)nu^(-1/3).

The lower endpoint of the successful age interval is fixed and positive in slow time. Indeed symmetry of h gives int_0^1 h=1/2, and the
deterministic transition time for the base axial equation is

(A64) int_0^1 d_delta(z)/b dz = (1+delta^2)/(2b) -> 1/(2b)=K/32>0.

Thus this proof establishes the pointwise lower bound V_nu(s) >= c/delta for K/(4nu) <= s <= K/nu; it does not establish that bound on a
window whose lower endpoint is o(1/nu). Equation (A63) separately gives an age-averaged lower bound on every [0, K'/nu] with fixed
K' >= max(1, K). It proves failure of the indicated sufficient small-total-variation condition within the prescribed kinematic class. The field has no swirl, so its swirl-production quantity is zero. Its
velocity and gradient converge uniformly to zero, and its limiting vorticity is zero. Consequently it supplies neither a nonconstant Euler
limit, a normalized gradient record, nor a packet with positive limiting vorticity. No evolution equation for U beyond the stated kinematic
constraints has been used.

References for the textbook facts used: A. Etheridge, Continuous martingales and stochastic calculus, Oxford lecture notes, 2018; A.
Etheridge, C8.2: Stochastic analysis and PDEs, Oxford lecture notes, 2016, Sections 3.2 and 7.3; the same facts (Doob's inequality, Ito's
formula and isometry, the strong Markov property, existence and pathwise uniqueness for locally Lipschitz stochastic differential equations,
squared Bessel processes) are in D. Revuz and M. Yor, Continuous Martingales and Brownian Motion, Springer, third edition, 1999, Chapters
II, III, IV, IX and XI; A. Friedman, Partial Differential Equations of Parabolic Type, Prentice-Hall, 1964, Chapter 1 (Cauchy problem,
uniqueness of bounded solutions and interior regularity). The occupation kernel (A41) and all probabilistic estimates specific to this
construction are derived above, not imported from a citation.

## Appendix B. A localized drift-free family with critical self-compression (Section 3, F10 (c))

This appendix proves the localized whole-space version of the drift-free example of F10 (c). It concerns a model: the swirl q is
prescribed (it does not solve the swirl equation), and the sourced vorticity eta_s solves the drift-free equation
(d_tau - nu Delta_5) eta_s = d_Z(q^2) with eta_s(0) = 0, without transport by the velocity. It shows that the three spatial velocity
bounds displayed in (B1), together with the record-frame circulation bound, do not force nu int (Pi_s)_+ dt -> 0 (the smallness of
Theorem 9(d)) in this drift-free prescribed-swirl model. The canonical-pressure and time-derivative estimates of Theorem 1(b) and the
record and limiting-vorticity conditions of Case 2 are not part of this construction. Variables are those
of the record frame (viscosity nu, record length and velocity one); R, Z are its coordinates, r, z = R/delta, Z/delta are cell
coordinates, and C abbreviates C_*. The velocity u is the full field (R q) e_theta + b_s, where b_s is the whole-space Biot-Savart velocity
of R eta_s e_theta, and a_s = b_s^r/R. In this appendix the letters A, B, D_0, D_b, E, E_st, E_tot, H_mem, J, K, M, P, S, U, V denote the
objects defined in (B2)-(B47) (A = - Delta_5 on R^5, B a radial profile, K a kernel, M a radial integral, P a majorant, S the steady
strain operator, U and V constants); none of them is a quantity of Sections 1-2 (historical suprema, the constant P = ||phi||_infty of
Theorem 9, or a limit of Navier-Stokes rescalings), and they are unrelated to the letters of Appendix A. Norms of vectors are Euclidean and
norms of derivative tensors are Frobenius norms; spatial derivatives are Cartesian.

We prove the following statement. For every C > 0 and G > 0 there are explicit constants alpha > 0, delta_0 > 0 and c > 0 such that, for
every 0 < delta <= delta_0, with nu = (C/G) delta^3 and T_nu = 1/nu, the time-independent swirl q of (B32) (smooth, supported in
|Z| <= 1, rapidly decreasing in R, flat at the axis) and the sourced field started from eta_s(0) = 0 satisfy, for all tau in [0, T_nu],

(B1) |u| <= 1, |grad u| <= 1, |grad^2 u| <= C,
     |R^2 q| <= G nu <= G,
     W_s := int_0^(1/nu) int_R^3 (-a_s) q^2 R dy dtau >= c nu.

The circulation bound is the record-frame form of |Gamma| <= G (Gamma = gamma_n and U^theta_n = nu_n gamma_n/R, so |gamma_n| <= G is
|R^2 q| <= G nu). By (B55) below, W_s >= c nu is the order required by Theorem 9(d), (e): the physical self-compression of this family
satisfies nu int (Pi_s)_+ dt >= c. By (B35), u and grad u tend uniformly to zero as delta -> 0, uniformly over the stated time
interval; the Hessian bound C/2 need not tend to zero. The limiting velocity is the zero Euler solution; the family carries no gradient
record and does not realize the nonconstant Euler limit of Theorem 1(b). It is not a Navier-Stokes solution.

B.1 Profiles and the negative radial integral.

Set

(B2) k = 1/20,
     g(r) = r^(1/2) exp(-(log r)^2/4), r > 0; g(0) = 0,
     L_k = -d_rr - (3/r)d_r + k^2,
     h = L_k^2 g,
     B = sqrt(h^2 + g^2),
     f(r,z) = B(r) + h(r) cos(kz),
     F_*(r) = B(r) + |h(r)|.

The letters B and h here denote profiles, not display numbers or a velocity. Both g and h are flat at r = 0 and decrease faster than any
power at infinity, with the same properties for every derivative. For r > 0, write h = g p. Direct differentiation, with x = log r, gives

(B3) p(r) =
       r^(-4) (x^4/16 - x^3/4 - 11x^2/8 + 13x/4 + 17/16)
       + 2k^2 r^(-2) (-x^2/4 + 3x/2 - 3/4) + k^4.

In particular,

(B4) f = g [sqrt(1+p^2) + p cos(kz)] > 0 for r > 0,
     sqrt(1+p^2) + p cos(kz)
       >= 1/(sqrt(1+p^2)+|p|) >= 1/[2(1+|p|)].

Every derivative of the bracket in (B4), and every inverse power of that bracket, has at most polynomial growth in r, r^(-1), and |log r|.
The factor sqrt(g) decreases faster than any such polynomial at both ends. Consequently sqrt(f), extended by zero at r = 0, is smooth and
flat there, with rapid radial decay, uniformly in the periodic variable z. This also proves Cartesian smoothness after lifting r to a radius
in R^2 or R^4. The suprema and integrals of these profiles used below are finite.

The sign needed in the construction is exact:

(B5) I := int_0^infinity r^2 g h dr
        = sqrt(2pi) [-1/8 + exp(2)/200 + exp(8)/160000]
        < -(6239/160000) sqrt(2pi) < 0.

To verify the identity, let D = d/dx, x = log r. Then L_0 = -r^(-2)(D^2+2D), and L_0^2 g = r^(-4)(D^4-4D^2)g. The three integrals in I are

(B6) int r^2 g L_0^2 g dr = -sqrt(2pi)/8,
     int r^2 g L_0 g dr = sqrt(2pi) exp(2),
     int r^2 g^2 dr = sqrt(2pi) exp(8).

For the first integral, the polynomial on the first line of (B3) has Gaussian mean -1/8 under the standard normal law. For the second, the
polynomial -x^2/4 + 3x/2 - 3/4 has mean 1 under the normal law with mean 2 and variance 1; completing the square supplies exp(2). Completing
the square supplies exp(8) in the third integral. These computations prove (B6), hence (B5). The strict upper bound in (B5) uses only exp(1)
< 3:

(B7) -1/8 + 9/200 + 6561/160000 = -6239/160000.

The elementary inequality exp(1) < 3 follows by bounding 1/n! <= 2^(-(n-1)) for n >= 2, strictly for n >= 3.

Choose the fixed axial cutoff

(B8) chi(Z) = exp(1 - 1/(1-Z^2)) for |Z| < 1,
     chi(Z) = 0 for |Z| >= 1,
     E = chi^2,
     m_E = int_R E(Z) dZ,
     m = int_R E(Z)^2 dZ,
     L_E = ||E'||_infinity.

This is a smooth cutoff, flat at its two endpoints, with 0 <= chi <= 1. It is increasing on (-1,0) and decreasing on (0,1). In particular,

(B9) ||E||_infinity = 1,
     int_R |(E^2)'| dZ = 2,
     0 < m_E <= 2,
     exp(-4/3) <= m <= 2.

For the lower bound, chi >= exp(-1/3) on [-1/2,1/2]. Flatness and smoothness follow by differentiating exp(-1/s) at s = 0 from the positive
side.

B.2 The whole-space kernel and an explicit cutoff error.

Identify R^5 with R^4 x R, write X = (x',z), and let r = |x'|. Put A = -Delta_5. Its Newtonian and biharmonic kernels, respectively, are

(B10) N(X) = 1/(8pi^2 |X|^3),
      Phi(X) = 1/(16pi^2 |X|),
      A Phi = N, A N = the unit point mass.

Indeed, the area of the unit four-sphere is 8pi^2/3; the outward flux of -grad N is one, and -Delta_5 |X|^(-1) = 2|X|^(-3) away from zero.
There is no point mass in this last identity, since the corresponding boundary flux tends to zero.

The steady strain operator is

(B11) S F = -d_z^2 A^(-2) F = K * F,
      K(x',z) = (|x'|^2 - 2z^2) /
                [16pi^2 (|x'|^2+z^2)^(5/2)],
      |K(X)| <= 1/(4pi^2 |X|^3).

Its kernel is locally integrable in five dimensions. For d > 0,

(B12) int_R K(x',z) dz = 0 when |x'| = d,
      int_R |z| |K(x',z)| dz <= 1/(2pi^2 d).

The first identity follows by integrating -d_zz Phi, whose first derivative vanishes at both axial infinities. The second follows from (B11)
and int_R |z|(d^2+z^2)^(-3/2) dz = 2/d. The exceptional transverse point d = 0 has measure zero; the resulting d^(-1) bound is locally
integrable in R^4.

For any nonnegative H on R^4 with finite L^1 and L^infinity norms, splitting at |x'-y'| = 1 gives

(B13) sup_x' int_R^4 H(y')/|x'-y'| dy'
        <= (2pi^2/3)||H||_infinity + ||H||_1.

Here and below all norms in (B13) and other formulas for transverse profiles use four-dimensional Lebesgue measure, with the radial lift
understood.

For 0 < delta <= 1, define

(B14) F_delta(r,z) = E(delta z) f(r,z),
      C_cut = [L_E/(2pi^2)]
                [(2pi^2/3)||F_*||_infinity + ||F_*||_1].

The whole-space steady strain satisfies the uniform estimate

(B15) S F_delta(r,z)
        = E(delta z) k^2 g(r) cos(kz) + e_delta(r,z),
      ||e_delta||_infinity <= C_cut delta.

First, S B = 0 by the first identity in (B12). On the mode h(r) cos(kz), the operator S is k^2 L_k^(-2); therefore S[h cos(kz)] = k^2 g
cos(kz). This inverse can be checked without any boundary convention: on transverse Schwartz functions,

(B16) L_k^(-2) h = int_0^infinity t exp(-t L_k) h dt = g.

For h = L_k^2 g, integrate t d_tt[exp(-t L_k)g] twice in t. The terms at infinity vanish because k > 0, and the term at zero is g. To
justify the kernel/heat identification even for the periodic input, let H_t^d be the d-dimensional heat kernel. Direct integration gives
Phi(X) = int_0^infinity t H_t^5(X) dt. Differentiating twice in z gives the kernel in (B11). Furthermore, t||d_zz H_t^1||_1 <= 1, and
||exp(t Delta_4)F_*||_infinity <= min(||F_*||_infinity,(4pi t)^(-2)||F_*||_1).
Their product is integrable in t on (0,infinity). These bounds justify exchanging the heat, spatial, and time integrals for the periodic
input by absolute integrability. They give S[h cos(kz)] = k^2 int_0^infinity t exp(-t L_k)h dt cos(kz), as asserted. The kernel integral
itself is also absolutely convergent: integrating (B11) axially leaves a constant times |x'-y'|^(-2), which is locally integrable in R^4.

Subtract E(delta z) S f from S F_delta inside this absolutely convergent convolution. The remaining integrand contains

(B17) E(delta(z-w)) - E(delta z),
      |E(delta(z-w)) - E(delta z)| <= L_E delta |w|.

Apply (B12), (B13), and |f| <= F_*. This proves exactly (B15). In particular, the contribution of the cutoff applied to B is included in
C_cut delta. It has not been discarded or estimated by scaling.

B.3 Uniform bounds for the complete poloidal velocity.

The constants in this part involve only fixed profiles. Write e_j = ||E^(j)||_infinity for j = 0,1,2. For multiindices gamma in five
Cartesian variables, let gamma_5 be the axial entry, and let e_z denote the axial unit multiindex. Define the nonnegative function on R^4

(B18) P(x') =
       sum_(|gamma|<=2) sum_(0<=j<=gamma_5)
         binomial(gamma_5,j) e_j
         sup_z |d^(gamma-j e_z) f(x',z)|.

This finite sum is bounded and decreases faster than any power in |x'|. The same holds for |x'|P. The product rule and delta <= 1 give, for
every |gamma| <= 2,

(B19) |d^gamma F_delta(x',z)| <= P(x').

For a transverse nonnegative function H, define the explicit numbers

(B20) A_2(H) = pi[(2pi^2/3)||H||_infinity + ||H||_1],
      A_3(H) = 2[pi^2||H||_infinity + ||H||_1],
      U = A_2(P)/(16pi^2),
      D_b = A_3(P)/(4pi^2),
      V = [A_2(P) + A_3(rP)]/(4pi^2),
      B_v = 12(U + D_b + V).

The notation rP means |x'|P(x'). The estimates underlying these constants are

(B21) sup_X int_R^5 |X-Y|^(-j) H(y') dY <= A_j(H),
      j = 2,3.

For j = 2, the axial integral is pi/|x'-y'|, and (B13) applies. For j = 3, it is 2/|x'-y'|^2; splitting its transverse convolution at radius
one gives pi^2||H||_infinity + ||H||_1 before multiplication by 2.

Let

(B22) Psi_delta = d_z Phi * F_delta,
      beta_delta = (-x_1 d_z Psi_delta,
                    -x_2 d_z Psi_delta,
                    2Psi_delta + x_1 d_1 Psi_delta
                                + x_2 d_2 Psi_delta).

In the second formula restrict the radial R^4 function to x' = (x_1,x_2,0,0). Thus beta_delta is a three-dimensional vector field. It is the
curl of (-x_2 Psi_delta,x_1 Psi_delta,0), has divergence zero, and

(B23) curl beta_delta = r [A^(-1)d_z F_delta] e_theta,
      beta_delta^r/r = S F_delta.

These identities follow directly by differentiating: the azimuthal component of curl beta_delta is -r Delta_5 Psi_delta. The field is the
whole-space Biot-Savart field, since it has that vorticity, divergence zero, and decay at infinity. Indeed F_delta is Schwartz for each
fixed delta, and the differentiated potential in (B22) is O(|X|^(-2)) at infinity, while its first derivatives are O(|X|^(-3)). These decay
assertions follow by splitting each potential integral at |Y| = |X|/2 and using the Schwartz bounds on the complementary region. Its
vorticity is O(|x|^(-3)), so the three-dimensional Biot-Savart integral converges and tends to zero at infinity, by the same split. The
difference is a decaying harmonic vector field and is zero.

The first and second derivatives of Phi obey

(B24) |d_z Phi(X)| <= |X|^(-2)/(16pi^2),
      |d_j d_z Phi(X)| <= |X|^(-3)/(4pi^2).

For any |gamma| <= 2, transfer gamma derivatives onto F_delta and use (B19)-(B21). This gives

(B25) |d^gamma Psi_delta| <= U,
      |d_j d^gamma Psi_delta| <= D_b,
      |x_i d_j d^gamma Psi_delta| <= V, i = 1,2.

For the third estimate use |x_i| <= |X-Y|+|y'| in the convolution for d_j Psi_delta. The two terms are precisely A_2(P) and A_3(rP) in
(B20). All integrations by parts are justified by the decay of F_delta and the locally integrable potential kernels.

After differentiating (B22) up to order two, every horizontal component is bounded by V+2D_b, and the vertical component by 2U+2V+2D_b. A
derivative tensor of order j has 3^(j+1) entries. Since sqrt(3^(j+1)) <= 6 for 0 <= j <= 2, (B20) gives

(B26) ||d^j beta_delta||_infinity <= B_v, j = 0,1,2.

These bounds include the full cutoff and the full B contribution. There is no logarithm or negative power of delta hidden in B_v.

To start from zero sourced vorticity, use cell diffusion time s and define

(B27) eta_delta(s) = (1-exp(s Delta_5)) A^(-1)d_z F_delta,
      beta_delta(s) = beta_delta - exp(s Delta_3) beta_delta.

The first expression is exactly int_0^s exp(v Delta_5)d_z F_delta dv, so it solves the drift-free equation with viscosity one and initial
value zero. The second expression is its Biot-Savart velocity. One can verify the required heat intertwining componentwise:

(B28) Delta_3[x_i v(r,z)] = x_i Delta_5 v(r,z), i = 1,2,
      exp(s Delta_3)[x_i v] = x_i exp(s Delta_5)v.

The Laplacian identity is a direct Cartesian differentiation. The heat identity follows by applying it to the two heat convolutions with the
same initial value; uniqueness holds in the class with at most linear growth, by the maximum principle with a quadratic barrier. Apply (B28)
to the vector potential in (B22), then commute curl with the three-dimensional heat convolution. This proves (B27), including the choice of
the whole-space inverse.

Heat convolution is a contraction for the sup norm of a vector or a derivative tensor. Thus for every s >= 0,

(B29) ||d^j beta_delta(s)||_infinity <= 2B_v, j = 0,1,2,
      beta_delta^r(s)/r = (1-exp(s Delta_5)) S F_delta.

B.4 The constants, the prescribed q, and all pointwise bounds.

Define a smooth periodic vector field in three dimensions by

(B30) v(x_1,x_2,z) = (-x_2,x_1,0) sqrt(f(r,z)),
      S_v = (||chi||_infinity + 2||chi'||_infinity
                                  + ||chi''||_infinity)
              (||v||_infinity + ||grad v||_infinity
                                 + ||grad^2 v||_infinity),
      Gamma_v = sup_(r>=0) r^2 sqrt(F_*(r)),
      alpha = min(1, 1/[4(1+S_v)],
                      1/sqrt(8G(1+B_v)), 1/(1+Gamma_v)).

All these constants are finite, alpha is strictly positive, and none depends on delta. The product rule gives

(B31) ||d^j[chi(delta z)v]||_infinity <= S_v,
      j = 0,1,2, 0 < delta <= 1.

Here the factor 2 in the definition of S_v accounts for the two first-derivative terms in a Hessian. Now prescribe

(B32) q(R,Z,tau) = alpha C delta chi(Z)
                    sqrt(f(R/delta,Z/delta)),
      nu = (C/G)delta^3, T_nu = 1/nu,
      s = nu tau/delta^2.

This q is smooth, independent of tau, supported in |Z| <= 1, and rapidly decreasing as R tends to infinity. Its swirl vector equals alpha C
delta^2 chi(delta z)v in cell coordinates. The sourced poloidal velocity and its strain are exactly

(B33) b_s(R,Z,tau) =
        alpha^2 C G delta^2 beta_delta(nu tau/delta^2)
        evaluated at (r,z) = (R/delta,Z/delta),
      a_s(R,Z,tau) =
        alpha^2 C G delta
          (1-exp(s Delta_5)) S F_delta(r,z).

For completeness, the scalar vorticity ratio in the R,Z coordinates is

(B34) eta_s(R,Z,tau) =
        (alpha^2 C^2 delta^3/nu) eta_delta(s)(r,z).

Substitution in the equation verifies
(d_tau - nu Delta_5)eta_s = d_Z(q^2) and eta_s(0) = 0. The Biot-Savart scaling in (B33) follows either from its kernel or from the vector
potential (B22).

Combining (B29), (B31), and (B33), for j = 0,1,2,

(B35) ||d^j u||_infinity
        <= C delta^(2-j) [alpha S_v + 2alpha^2 G B_v]
        <= (C/2) delta^(2-j).

Moreover,

(B36) |R^2 q| <= alpha C delta^3 Gamma_v
                <= C delta^3 = G nu.

Therefore, whenever delta <= min(1,1/C,(G/C)^(1/3)), the three velocity bounds in (B1) and the two circulation bounds in (B1) hold uniformly
throughout the time interval. In fact the Hessian is bounded by C/2. The full field is smooth, axisymmetric and divergence-free. These
assertions include the axis and spatial infinity.

B.5 The localized steady work.

The following further constants, all independent of delta, fix the work estimate and its errors:

(B37) M = int_0^infinity r^2 F_*(r) dr,
      J_B = int_0^infinity r^2 g(r)B(r) dr,
      A_F = m_E M,
      D_0 = k^2 (-I) m/2,
      E_st = 2k[J_B + |I|/4] + C_cut A_F.

In particular D_0 > 0. Let

(B38) J_delta = int_R int_0^infinity
                 r^2 F_delta(r,z) S F_delta(r,z) dr dz.

The error term e_delta in (B15) contributes at most C_cut A_F in absolute value, since F_delta >= 0 and

(B39) int_R int_0^infinity r^2 F_delta dr dz <= A_F/delta.

Integration by parts and (B9) give

(B40) |int_R E(delta z)^2 cos(kz) dz| <= 2/k,
      |int_R E(delta z)^2 cos(2kz) dz| <= 1/k.

Thus the product of the main term in (B15) with F_delta has integral

(B41) k^2 J_B int_R E(delta z)^2 cos(kz) dz
        + k^2 I int_R E(delta z)^2 cos(kz)^2 dz.

Use cos(kz)^2 = [1+cos(2kz)]/2 in (B41), and then (B40). The exact error bound is

(B42) |J_delta + D_0/delta| <= E_st.

This estimate proves localization of the negative work, with an error constant that accounts for both axial oscillatory averaging and the
strain of the cutoff.

B.6 The zero-data memory integral.

It remains to compare the full solution starting at zero with the steady response over the actual time interval. Let g_max = exp(1/4), which
is the maximum of g. From (B15), heat contraction, and separation of the radial and axial heat convolutions,

(B43) ||exp(s Delta_5) S F_delta||_infinity
        <= k g_max/[sqrt(pi s)]
             + delta[k g_max L_E + C_cut], s > 0.

Here is a derivation that does not assume a spectral gap for the cutoff. In one axial dimension,

(B44) E(delta z) cos(kz)
        = (1/k)d_z[E(delta z) sin(kz)]
            - (delta/k)E'(delta z) sin(kz),
      ||d_z H_s||_1 = 1/sqrt(pi s),
      H_s(z) = (4pi s)^(-1/2) exp(-z^2/(4s)).

Apply axial heat convolution to (B44). Apply transverse heat contraction to g, multiply by k^2, and add the heat evolution of e_delta. This
is (B43). Its s^(-1/2) singularity is integrable at zero, so the estimate loses no part of the startup interval.

Define

(B45) H_mem = 2k g_max/sqrt(pi) + k g_max L_E + C_cut,
      E_tot = 1 + E_st + A_F H_mem.

The terminal cell time is S_delta = delta^(-2). Integrating (B43) to that time yields the explicit bound

(B46) int_0^(delta^(-2))
        ||exp(s Delta_5) S F_delta||_infinity ds
        <= H_mem/delta.

Introduce the full signed cell work without its angular factor,

(B47) J_time =
       int_0^(delta^(-2)) int_R int_0^infinity
         r^2 F_delta (1-exp(s Delta_5)) S F_delta dr dz ds.

By (B39), (B42), and (B46),

(B48) |J_time + D_0/delta^3|
        <= (E_st + A_F H_mem)/delta^2
        <= E_tot/delta^2.

Thus the startup and all subsequent memory are controlled on the whole interval [0,T_nu]. No replacement by steady data or by an
infinite-time average has been made.

Complete the constant hierarchy by setting

(B49) delta_0 = min(1, 1/C, (G/C)^(1/3), D_0/(2E_tot)),
      c = pi alpha^4 C G^3 D_0.

Every constant in (B49) is a specified finite integral, a specified supremum of an explicit fixed smooth profile, or an elementary
expression in C and G. There is no unspecified multiplicative constant. These definitions have no circular dependence: profiles and kernel
constants come first, then alpha, then the work constants, and finally delta_0 and c.

For 0 < delta <= delta_0, (B48) gives

(B50) J_time <= -D_0/(2delta^3).

In the three-dimensional volume element dy = 2pi R dR dZ, the extra weight R in W_s gives R dy = 2pi R^2 dR dZ. Substitute
(B32)-(B33), change variables R = delta r, Z = delta z, and use dtau = delta^2 ds/nu. Exactly,

(B51) W_s = -[2pi alpha^4 C^4 delta^12/nu^2] J_time
            >= pi alpha^4 C^4 D_0 delta^9/nu^2
            = c nu.

This proves (B1). It also gives the asymptotic coefficient that F10 (c) states as a scale count:

(B52) |W_s/nu - pi alpha^4 C G^3 k^2(-I)m|
        <= 2pi alpha^4 C G^3 E_tot delta.

The steady expansion work has coefficient pi k^2 I, which is negative. The compression work W_s has its opposite sign, as in (B51)-(B52).

B.7 Mapping to Theorem 9(d)-(e).

For clarity, temporarily distinguish physical variables with viscosity one from record variables. Write x = x_0 + l y, with x_0 on the
symmetry axis, t = t_0 + (l/M_0)tau, u_phys = M_0 U, D = M_0/l, and nu = 1/(M_0 l). Here M_0 is a velocity scale, unrelated to the radial
integral M in (B37). Then

(B53) q_phys = D q, a_phys = D a,
      r_phys dx_phys = l^4 R dy,
      dt_phys = D^(-1) dtau.

Consequently, for the corresponding signed self-compression integral on this time interval,

(B54) int Pi_s,phys dt_phys = nu^(-2) W_s,
      nu int Pi_s,phys dt_phys = W_s/nu >= c.

The scaling multiplier for the instantaneous spatial integral is positive. Therefore taking its positive part before integrating time gives

(B55) nu int (Pi_s,phys)_+ dt_phys
        = nu^(-1) int_0^(T_nu)
             [-int_R^3 a_s q^2 R dy]_+ dtau
        >= W_s/nu >= c.

This is the positive part of the spatially integrated rate, exactly as in Theorem 9(d); it is not a replacement by the integral of the
pointwise positive part. The record-variable interval T_nu = 1/nu corresponds to physical duration l^2. The physical circulation bound maps
to |R^2 q| <= G/(M_0 l) = G nu, which explains the stronger bound imposed in (B1).

The positive part is also bounded above at the same order. With m_delta(s) = int int r^2 F_delta exp(s Delta_5) S F_delta dr dz, the
instantaneous cell work is J_delta - m_delta(s), and int_0^(delta^(-2)) |m_delta(s)| ds <= A_F H_mem/delta^2 by (B39) and (B46). For
0 < delta <= delta_0, (B42) and (B49) give -J_delta >= D_0/delta - E_st > 0, and |[-J_delta + m_delta(s)]_+ - (-J_delta)| <= |m_delta(s)|.
Put P_delta = int_0^(delta^(-2)) [-J_delta + m_delta(s)]_+ ds. Then |P_delta - D_0/delta^3| <= (E_st + A_F H_mem)/delta^2 <=
E_tot/delta^2, the positive-leading-term counterpart of (B48). Changing variables as in (B52) gives

(B56) |nu int (Pi_s,phys)_+ dt_phys - pi alpha^4 C G^3 k^2 (-I) m|
        <= 2 pi alpha^4 C G^3 E_tot delta.

So the positive-part integral is of exact order 1/nu in physical units. This is a scaling comparison with Theorem 9(d)-(e), not an
application of its coupled-evolution hypotheses to this model.

Equations (B51), (B55) and (B56) show that, in the drift-free model with prescribed swirl, these bounds allow the critical amount of
positive self-compression. The model in which eta_s is transported by its own poloidal velocity is treated in Appendix C; the coupled
swirl equation is outside the hypotheses of both appendices.

References for the textbook facts used: the Newtonian and biharmonic kernels of the Laplacian on R^5, the heat kernel and its contraction
property, uniqueness of solutions of the heat equation with at most polynomial growth (maximum principle with a barrier), and the decay of
harmonic vector fields: A. Friedman, Partial Differential Equations of Parabolic Type, Prentice-Hall, 1964, Chapter 1; L. C. Evans, Partial
Differential Equations, second edition, AMS, 2010, Sections 2.2 and 2.3. All estimates specific to this construction are derived above.

## Appendix C. A localized transported family with prescribed swirl and critical self-compression (Section 3, F10 (c); Section 4, Open (6))

This appendix proves the transported version of Appendix B. It again concerns a model in which the swirl q is prescribed and does not
solve the swirl equation. Unlike Appendix B, the sourced vorticity is transported by its own poloidal velocity:

(C1) (d_tau + b_s.grad - nu Delta_5) eta_s = d_Z(q^2),   eta_s(0) = 0,

where b_s is the whole-space Biot-Savart velocity of R eta_s e_theta (the divergence-free field with that curl which tends to zero at
infinity), a_s = b_s^r/R, and the full field is u = (R q) e_theta + b_s. Record variables, cell variables and the conventions for norms are
those of Appendix B. The profiles g, h, B, f, F_* and the number k of (B2), the cutoff chi, E, m_E, m of (B8), the integral I of (B5), the
radial integral M and the numbers A_F, D_0 of (B37), and the field v and the numbers S_v, Gamma_v of (B30) are used unchanged; the operator
L_k is that of (B2), and A = -Delta_5. The Newtonian kernel N of (B10) is written N_5. The amplitude alpha of this appendix is defined in
(C46); it need not coincide with the alpha of (B30). Every other letter is defined in this appendix and has no meaning outside it; for example
X, X_- and Xv are norms, env(v) is an envelope and Y_3, Y_infinity are envelope norms, P_R is a majorant, and K_t is an axially integrated
kernel.

We prove the following statement. For every C > 0 and G > 0 there are explicit constants alpha > 0, delta_1 > 0 and c > 0 such that,
for every 0 < delta <= delta_1, with nu = (C/G) delta^3, the time-independent swirl

(C2) q(R,Z) = alpha C delta chi(Z) sqrt(f(R/delta, Z/delta))

(the form (B32), with the alpha of (C46)) and a solution eta_s of (C1) are smooth on [0, 1/nu] x R^3, and for all tau in [0, 1/nu]

(C3) |u| <= 1, |grad u| <= 1, |grad^2 u| <= C,
     |R^2 q| <= G nu <= G,
     W_s := int_0^(1/nu) int_R^3 (-a_s) q^2 R dy dtau >= c nu,

with c = pi alpha^4 C G^3 D_0. This is (B1) for the transported model. The derivation of (B53)-(B55) uses only the change of variables and
the positivity of the scaling multiplier, so it applies unchanged: the physical self-compression of this family satisfies
nu int (Pi_s)_+ dt >= c, the order required by Theorem 9(d), (e). As in Appendix B, u and grad u tend uniformly to zero as delta -> 0, the
limiting velocity is the zero Euler solution, the family carries no gradient record, and the canonical-pressure and time-derivative
estimates of Theorem 1(b) are not part of the construction. It is not a Navier-Stokes solution, because q does not solve the swirl
equation.

The proof expands the transported solution around a modulated approximation built from transported axially periodic solutions (C.2 to
C.4), and controls the error in the velocity formulation by envelopes in which the axial supremum is taken inside a transverse L^3 norm
(C.5 to C.9). Neither limitation noted after F10 (c) applies: the expansion is not around the drift-free solution, and no velocity bound
is derived from a bound on the vorticity ratio.

C.1 Cell form, work and envelopes.

Put r = R/delta, z = Z/delta, s = nu tau/delta^2, S_delta = delta^(-2), epsilon = alpha^2 G^2 and F_delta(r,z) = E(delta z) f(r,z). For
a scalar U on R^5 = R^4 x R that is radial in x', let b(U) be the whole-space Biot-Savart velocity of r U e_theta and a(U) = b(U)^r/r.
When U is a Schwartz function, the argument after (B23) shows that, with Psi = A^(-1)U the decaying Newtonian potential,

(C4) b(U) = (-x_1 d_z Psi, -x_2 d_z Psi, 2 Psi + x_1 d_1 Psi + x_2 d_2 Psi),
     a(U) = -d_z Psi,

restricted to x' = (x_1, x_2, 0, 0); and by (B28), b(exp(t Delta_5) U) = exp(t Delta_3) b(U).

Write eta_s(R,Z,tau) = alpha^2 C G H(r,z,s). Since q^2 = alpha^2 C^2 delta^2 F_delta, the Biot-Savart scaling gives
b_s = alpha^2 C G delta^2 b(H) and a_s = alpha^2 C G delta a(H), and (C1) becomes, after division by alpha^2 C^2 delta
= alpha^2 C G nu/delta^2,

(C5) d_s H - Delta_5 H + epsilon b(H).grad H = d_z F_delta,   H(0) = 0,   0 <= s <= S_delta.

With R dy = 2 pi R^2 dR dZ and dtau = delta^2 ds/nu, the work is exactly

(C6) W_s/nu = -2 pi alpha^4 C G^3 delta^3 J_tr[H],
     J_tr[U] = int_0^(S_delta) int_R int_0^infinity r^2 F_delta(r,z) a(U)(r,z,s) dr dz ds.

For the drift-free solution of Appendix B, J_tr is the integral J_time of (B47), by (B29); this is (B51). Negative J_tr means positive
compression work.

For a vector or tensor field v on [0, S_delta] x R^3 write x = (x', z) with x' in R^2, and define the envelope (a sum of axial suprema)
and the envelope norms

(C7) env(v)(x',s) = sum_(j=0)^2 (1/j!) sum_(a_1,...,a_j = 1)^3 sum_(entries i) sup_z |d_(a_1)...d_(a_j) v_i(x',z,s)|,
     Y_p(v) = sup_(0 <= s <= S_delta) ||env(v)(s)||_(L^p(R^2)),   p = 3 or p = infinity.

By the product rule, a derivative of order j of a product is a sum over the 2^j ways of distributing the j ordered derivatives; after
division by j! the terms with l derivatives on the first factor carry the coefficient 1/[l!(j-l)!]. Since the supremum of a product is at
most the product of the suprema, env(v tensor w) <= env(v) env(w) and env(v+w) <= env(v) + env(w). Also |v| + |grad v| + |grad^2 v|
<= 4 env(v) pointwise, with Euclidean and Frobenius norms.

C.2 The odd periodic problem.

This part works on R^4 x (R/T_k Z), T_k = 2 pi/k, with A^(-1) the inverse on nonzero axial modes. On this space b(H) and a(H) are defined by
(C4) with Psi = A^(-1)H the periodic inverse; b(H) is then the bounded divergence-free field with curl r H e_theta that decays
transversally. For H(x',z) = sum_(n != 0) H_n(x') exp(i n k z), radial in x', real and odd in z, put

(C8) ||H||_X = sum_(n != 0) sum_(|beta|+j <= 4) |nk|^j ||(1+|x'|)^8 d_x'^beta H_n||_infinity,

let ||.||_(X_-) be the same sum with |beta|+j <= 3, and let X be the completion in (C8) of the smooth odd functions with finitely many
modes and rapidly decreasing transverse derivatives. Let G_n(t,.) denote the heat kernel of R^n and define

(C9) w_0(t) = int_R^4 G_4(t,y)(1+|y|)^8 dy,
     w_1(t) = sum_(i=1)^4 int_R^4 |d_i G_4(t,y)|(1+|y|)^8 dy,
     w_2(t) = w_1(t) exp(-k^2 t) + t^(-1/2) w_0(t) exp(-k^2 t/2),
     w_3(t) = 127 [w_0(t) exp(-k^2 t) + w_2(t)],
     sigma = k^2/4,
     J_0 = int_0^infinity w_0(t) exp(-k^2 t) dt,   J_1 = int_0^infinity w_2(t) dt,
     J_sigma = int_0^infinity exp(sigma t) w_3(t) dt,
     C_sigma = sup_(t >= 0) w_0(t) exp(-(k^2 - sigma) t).

These are finite, since w_0(t) and t^(1/2) w_1(t) are bounded by Gaussian moments times 1 + t^4. Using
(1+|x|)^8 <= (1+|x-y|)^8 (1+|y|)^8, the gap |nk| >= k, the bound |nk| exp(-(nk)^2 t) <= t^(-1/2) exp(-k^2 t/2), and, for a derivative of
order four, moving one derivative onto the kernel or onto the axial multiplier (there are binomial(9,5) = 126 pairs (beta, j) with
|beta| + j <= 4), one obtains for t > 0

(C10) ||exp(-tA) U||_X <= w_0(t) exp(-k^2 t) ||U||_X,
      ||exp(-tA) U||_X <= w_3(t) ||U||_(X_-),
      ||A^(-1) U||_X <= J_0 ||U||_X,
      sum_(i=1)^5 ||d_i A^(-1) U||_X <= J_1 ||U||_X.

Let ||.||_(Xv) be the norm defined as in (C8), with weight (1+|x'|)^7, summed over the five components of the five-dimensional field
(-x' d_z Psi, 2 Psi + x'.grad_x' Psi), Psi = A^(-1)H. Its restriction to x' = (x_1, x_2, 0, 0) is b(H), so ||.||_(Xv) bounds every
derivative of b(H) of order at most four in sup norm, with the weight (1+r)^7. Differentiating a coordinate factor costs at most four
additional terms. With

(C11) B_per = 2 J_0 + 40 J_1,   N_tr = 8 B_per,   K_tr = N_tr J_sigma,

one has ||b(H)||_(Xv) <= B_per ||H||_X, ||a(H)||_X <= J_1 ||H||_X, and ||b(H).grad U||_(X_-) <= N_tr ||H||_X ||U||_X. The last estimate
uses the Fourier convolution inequality, product-rule coefficients summing to at most 8, and the weight placed on the differentiated
factor U. If H and U are odd in z, then Psi and b^z are odd and b^r is even, so b(H).grad U is odd and no zero mode arises.

Let H_bar = -k (L_k g) sin(kz); since A = L_k on the first mode and h = L_k^2 g, H_bar = A^(-1) d_z f. Put

(C12) A_0 = ||H_bar||_X,   L_0 = (1 + C_sigma) A_0,   R_0 = 4 L_0,   epsilon_P = min(1, 1/(8 K_tr R_0)).

For |lambda| <= 2 and 0 <= epsilon <= epsilon_P consider the steady and the zero-data problems with forcing lambda d_z f,

(C13) H_*^lambda = lambda H_bar - epsilon A^(-1)[b(H_*^lambda).grad H_*^lambda],
      H^lambda(s) = lambda (1 - exp(-sA)) H_bar
                    - epsilon int_0^s exp(-(s-t)A)[b(H^lambda(t)).grad H^lambda(t)] dt.

In the ball of radius R_0 in X, respectively in C_b([0,infinity); X), the linear terms have norm at most 2(1 + C_sigma) A_0 = R_0/2 by
(C10), and the nonlinear terms have norm at most epsilon K_tr R_0^2 <= R_0/8 and Lipschitz constant at most 2 epsilon K_tr R_0 <= 1/4.
(For the steady problem, A^(-1) = int_0^infinity exp(-tA) dt maps X_- to X with norm at most J_sigma.) Hence both problems have unique
solutions in these balls, defined for all s >= 0, and ||H_*^lambda||_X <= A_0 + R_0/8 <= 3R_0/8 for |lambda| <= 1. The difference
H^lambda(s) - H_*^lambda equals -exp(-sA) H_*^lambda minus epsilon times the Duhamel integral of
b(H^lambda).grad H^lambda - b(H_*^lambda).grad H_*^lambda. Multiplying its norm by exp(sigma s), taking the supremum over [0, T] and using
2 epsilon N_tr R_0 J_sigma <= 1/4 gives, after T -> infinity,

(C14) ||H^lambda(s) - H_*^lambda||_X <= 2 C_sigma exp(-sigma s) ||H_*^lambda||_X.

These solutions are smooth: the norm controls four spatial derivatives, the equation gives the time derivative, and higher derivatives
follow by differentiating the mild equations, where the highest derivative appears linearly with bounded coefficients and one derivative
on the kernel costs an integrable t^(-1/2). Their transverse decay is faster than any power: if H has weight p in (C8), then b(H) has
weight p - 1 and b(H).grad H weight 2p - 1, and the heat estimates (C10) at that weight (with the moments of order 2p - 1 in (C9)) place H
in it. The same argument with more derivatives in (C8) gives the corresponding bounds for all higher derivatives.

C.3 The periodic work.

Write H_* = H_*^1. At epsilon = 0 the potential, velocity and strain are Psi_bar = -k g sin(kz), b_bar^r = k^2 r g cos(kz),
b_bar^z = -k(2g + r g') sin(kz) and a_bar = k^2 g cos(kz). With g_1 = -k L_k g, direct multiplication gives

(C15) b_bar.grad H_bar = (k^2/2) [r g g_1' - (2g + r g') g_1] sin(2kz),
      H_1 = -A^(-1)[b_bar.grad H_bar],
      Wper(U) = avg_z int_0^infinity r^2 f(r,z) a(U)(r,z) dr,
      Wper(H_bar) = (k^2/2) I = -d_0,   Wper(H_1) = 0,   |Wper(U)| <= M J_1 ||U||_X,

where d_0 = k^2(-I)/2, so that D_0 = m d_0. The value of Wper(H_bar) is the average of (B + h cos(kz)) k^2 g cos(kz), integrated against
r^2. Wper(H_1) = 0 because a(H_1) is a multiple of cos(2kz), while f contains only the harmonics 0 and 1. The last bound uses
0 <= f <= F_* and ||a(U)||_infinity <= ||a(U)||_X. Subtracting the first iterate of (C13) and using bilinearity,

(C16) ||H_* - H_bar||_X <= epsilon K_tr R_0^2,
      ||H_* - H_bar - epsilon H_1||_X <= epsilon^2 K_tr^2 R_0^2 (R_0 + A_0),
      |Wper(H_*) + d_0| <= K_w epsilon^2,   K_w = M J_1 K_tr^2 R_0^2 (R_0 + A_0),
      epsilon_0 = min(epsilon_P, sqrt(d_0/(4 K_w))).

For 0 <= lambda <= 1, lambda times the steady state with parameter epsilon lambda is a fixed point of the first line of (C13) with norm at
most 3R_0/8, so by uniqueness it is H_*^lambda. Hence, with

(C17) Lw_epsilon(lambda, theta) = lambda int_0^infinity r^2 f(r,theta) a(H_*^lambda)(r,theta) dr,
      Lwbar_epsilon(lambda) = avg_theta Lw_epsilon(lambda, theta),
      |Lwbar_epsilon(lambda) + d_0 lambda^2| <= K_w epsilon^2 lambda^4,   0 <= lambda <= 1, 0 <= epsilon <= epsilon_0.

C.4 The modulated approximation, its residual and its work.

The solutions of (C13) depend smoothly on lambda: the map in (C13) is affine in lambda and a contraction, and differentiating (C13) j times
gives a linear fixed-point problem with contraction constant at most 1/4. Hence, for 0 <= epsilon <= epsilon_0,

(C18) sup_(s >= 0, |lambda| <= 1) ||d_lambda^j H^lambda(s)||_X <= kappa_j,   0 <= j <= 4,
      kappa_0 = R_0,   kappa_1 = 2 L_0,
      kappa_j = 2 epsilon_0 K_tr sum_(l=1)^(j-1) binomial(j,l) kappa_l kappa_(j-l)   (2 <= j <= 4),

and the same bounds hold for the steady states. The construction for |lambda| <= 2 justifies the differentiation at the endpoints of
[-1, 1]. Let theta be a fast axial variable of period T_k, put lambda = E(delta z), Psi^lambda = A^(-1) H^lambda, and

(C19) h_delta(r,z,s) = H^lambda(r,theta,s),   psi_app = Psi^lambda(r,theta,s),   v_app = b(H^lambda)(r,theta,s),
      evaluated at theta = z, lambda = E(delta z).

These functions vanish for |z| >= 1/delta, since H^0 = 0; h_delta(0) = 0, h_delta is odd in z, and for fixed delta it is a Schwartz
function, by the transverse decay of C.2. The chain rule d_z = d_theta + delta E'(delta z) d_lambda, applied twice, gives
A psi_app = h_delta - Q_delta, and hence, by uniqueness of decaying potentials,

(C20) A^(-1) h_delta = psi_app + chi_delta,   chi_delta = A^(-1) Q_delta,
      Q_delta = 2 delta E' Psi_(lambda theta) + delta^2 E'' Psi_lambda + delta^2 (E')^2 Psi_(lambda lambda),
      b(h_delta) = v_app + u_delta,
      u_delta^r = -r delta E' Psi_lambda - r d_z chi_delta,   u_delta^z = 2 chi_delta + r d_r chi_delta,
      a(h_delta) - a(H^lambda)|_(theta = z, lambda = E(delta z)) = -delta E' Psi_lambda - d_z chi_delta,

with E', E'' evaluated at delta z. For d = |x' - y'| > 0 the kernel N_5 satisfies

(C21) int_R N_5(x' - y', zeta) d zeta = 1/(4 pi^2 d^2),   int_R |grad N_5(x' - y', zeta)| d zeta <= 3/(16 pi d^3).

By (C18), Q_delta and its derivatives of order at most two are bounded by a fixed multiple of delta (1+|y'|)^(-8). Write chi_delta as
the integral of N_5 against Q_delta and its first derivatives as integrals of grad N_5 against Q_delta; move up to two further
derivatives onto Q_delta; use |x_i| <= d + |y'| for the coordinate factors, and (C21). This bounds u_delta and its derivatives of order
at most two by a fixed multiple of delta (1+r)^(-2), and the strain difference in (C20) by a fixed multiple of delta, uniformly in s,
0 < delta <= 1 and 0 <= epsilon <= epsilon_0. Substituting (C19) in (C5) and using the periodic equation (C13) in differential form gives
the exact residual identity

(C22) (d_s - Delta_5) h_delta + epsilon b(h_delta).grad h_delta = d_z F_delta + R_delta,
      R_delta = - delta E' f - 2 delta E' H_(lambda theta) - delta^2 E'' H_lambda - delta^2 (E')^2 H_(lambda lambda)
                + epsilon u_delta.grad_fast H^lambda + epsilon delta E' b(h_delta)^z H_lambda,

where grad_fast H^lambda = (d_r H^lambda, d_theta H^lambda) and everything is evaluated as in (C19). The first term of R_delta comes from
d_z F_delta = E(delta z) d_z f + delta E'(delta z) f; the last term contains both v_app and u_delta. Define the numbers

(C23) A_b = 1 + sup (1+r)^7 env(v_app) + sup delta^(-1) (1+r)^2 env(u_delta),
      C_R = 1 + sup delta^(-1) (1+|x'|)^8 max_(|gamma| <= 2) |d^gamma R_delta|,
      C_a = sup delta^(-1) |a(h_delta) - a(H^lambda)|_(theta = z, lambda = E(delta z))|,

where the suprema range over 0 < delta <= 1, 0 <= epsilon <= epsilon_0, s >= 0 and the spatial variables, and the envelope (C7) is taken
for each fixed s. They are finite by (C18), the chain rule and the potential bounds just stated: two derivatives of a composed periodic
function use at most two lambda-derivatives, two derivatives of R_delta use at most four, and the X and Xv norms control four spatial
derivatives; the term -delta E' f involves only the profile f, whose derivatives decrease faster than any power. These numbers are
defined by the approximation alone and do not involve the solution of (C5). With P_R(x') = C_R (1+|x'|)^(-8) on R^4,

(C24) |d^gamma R_delta(x', z, s)| <= delta P_R(x') 1_(|z| <= 1/delta),   |gamma| <= 2,
      env(v_app) <= A_b (1+r)^(-7),   env(u_delta) <= A_b delta (1+r)^(-2).

The work of the approximation is computed as follows. Let V(lambda, theta) be the T_k-periodic primitive in theta of
Lw_epsilon - Lwbar_epsilon that vanishes at theta = 0. Then V(0, theta) = 0, since Lw_epsilon(0, theta) = 0, and
|d_lambda V| <= 2 T_k sup |d_lambda Lw_epsilon| <= 2 T_k M J_1 (kappa_0 + kappa_1) by (C18). Since
d_z [V(E(delta z), z)] = (Lw_epsilon - Lwbar_epsilon)(E(delta z), z) + delta E'(delta z) d_lambda V and V(E(delta z), z) vanishes for
|z| >= 1/delta,

(C25) |int_R [Lw_epsilon(E(delta z), z) - Lwbar_epsilon(E(delta z))] dz| <= C_avg = 2 T_k ||E'||_1 M J_1 (kappa_0 + kappa_1).

In J_tr[h_delta], replace a(h_delta) by a(H^lambda) at theta = z (error C_a delta in sup norm, by (C23)), then H^lambda(s) by
H_*^lambda (error 2 C_sigma J_1 R_0 exp(-sigma s) in the strain, by (C14)); the result is int_0^(S_delta) int_R Lw_epsilon(E(delta z), z)
dz ds. Then replace Lw_epsilon by Lwbar_epsilon (by (C25)), and finally Lwbar_epsilon(lambda) by -d_0 lambda^2 (by (C17), with
int_R E(delta z)^4 dz <= m/delta). Since int int r^2 F_delta dr dz <= A_F/delta by (B39), int_R E(delta z)^2 dz = m/delta, and the window
has length delta^(-2),

(C26) |J_tr[h_delta] + D_0 delta^(-3)| <= m K_w epsilon^2 delta^(-3) + C_loc delta^(-2),
      C_loc = 1 + C_avg + A_F C_a + 2 C_sigma J_1 R_0 A_F/sigma,

for 0 < delta <= 1 and 0 <= epsilon <= epsilon_0. (The transient term is at most 2 C_sigma J_1 R_0 A_F/(sigma delta) and is bounded as
displayed.)

C.5 The velocity equation and the error equation.

Let P_3 be the Leray projection of R^3. The transported solution is constructed through its velocity, as the solution of the forced
axisymmetric Navier-Stokes system without swirl

(C27) d_s b - Delta_3 b + epsilon P_3 div(b tensor b) = P_3(r F_delta e_r),   div b = 0,   b(0) = 0.

If b is a smooth solution of (C27), axisymmetric without swirl and tending to zero at infinity together with its derivatives, then
H = (curl b)_theta / r solves (C5) and b = b(H). Indeed curl b = r H e_theta, [curl div(b tensor b)]_theta = b.grad(rH) - (b^r/r) rH
= r b.grad H, [curl(r F_delta e_r)]_theta = d_z(r F_delta) = r d_z F_delta, and Delta_3 (r H e_theta) = r (Delta_5 H) e_theta by (B28);
so the curl of (C27) is r times (C5) in the azimuthal direction, and b is the decaying divergence-free field with curl r H e_theta.
The approximate velocity b_app = b(h_delta) satisfies

(C28) d_s b_app - Delta_3 b_app + epsilon P_3 div(b_app tensor b_app) = P_3(r F_delta e_r) + b(R_delta).

For fixed delta, h_delta and R_delta are Schwartz functions, so all terms of (C28) are divergence free and tend to zero at infinity; by the
same identities and (C22), the difference of the two sides has zero curl. It is therefore a harmonic field tending to zero at infinity,
hence zero. Put

(C29) Bcal(v, w)(s) = int_0^s exp((s-t) Delta_3) P_3 div(v tensor w)(t) dt,
      Z_delta(s) = int_0^s exp((s-t) Delta_5) R_delta(t) dt.

By (B28), b(Z_delta)(s) = int_0^s exp((s-t) Delta_3) b(R_delta(t)) dt; this holds for the time-dependent residual. By Duhamel's formula
for (C28) and bilinearity, if e is a bounded field with bounded derivatives of order at most two that solves

(C30) e = -b(Z_delta) - epsilon [Bcal(b_app, e) + Bcal(e, b_app) + Bcal(e, e)],

then b_app + e solves the integral (mild) form of (C27):
b_app + e = int_0^s exp((s-t) Delta_3) P_3(r F_delta e_r) dt - epsilon Bcal(b_app + e, b_app + e).

C.6 The kernel and the envelope inequality.

Since P_3 = I + grad grad (-Delta_3)^(-1) and (-Delta_3)^(-1) exp(t Delta_3) = int_t^infinity exp(xi Delta_3) d xi, the operator
exp(t Delta_3) P_3 div acts on a tensor F by convolution, (exp(t Delta_3) P_3 div F)_i = sum_(j,k) O_ijk(., t) * F_jk, with

(C31) O_ijk(x, t) = delta_ij d_k G_3(t, x) + int_t^infinity d_i d_j d_k G_3(xi, x) d xi.

Let |O| be the sum of the absolute values of the 27 entries. Scaling gives O(x, t) = t^(-2) O(x/sqrt(t), 1), and so

(C32) |O(x,t)| <= C_O (|x| + sqrt(t))^(-4),   C_O = 1 + sup_x (1+|x|)^4 |O(x,1)|,
      ||O(., t)||_(L^1(R^3)) <= (4 pi C_O/3) t^(-1/2).

C_O is finite: the first term of (C31) is a Gaussian derivative; for the second, |d^3 G_3(xi, x)| <= c_G xi^(-3) exp(-|x|^2/(8 xi)) with a
fixed constant c_G gives a bounded integral for |x| <= 1 and, after the substitution w = |x|^2/(8 xi), the bound 64 c_G |x|^(-4) for
|x| >= 1. Let K_t(x') = int_R |O(x', z, t)| dz for x' in R^2. Since |x| + sqrt(t) >= (|x'| + |z| + sqrt(t))/sqrt(2),

(C33) K_t(x') <= C_K (|x'| + sqrt(t))^(-3),   C_K = 8 C_O/3,
      ||K_t||_(L^p(R^2)) <= c_p t^(-3/2 + 1/p),   c_p = C_K [2 pi/((3p-1)(3p-2))]^(1/p) for 1 <= p < infinity,   c_infinity = C_K.

The norm formula follows from int_0^infinity 2 pi r (r + a)^(-3p) dr = 2 pi a^(2-3p)/((3p-1)(3p-2)). For a tensor field F, an index i and
a derivative d^a of order at most two,

     sup_z |d^a (O * F)_i(x', z)| <= sum_(j,k) int_R^2 (int_R |O_ijk(x' - y', zeta)| d zeta) sup_z' |d^a F_jk(y', z')| dy',

because the inner axial integral does not depend on z. Summing over i, using sum_i int_R |O_ijk(x' - y', zeta)| d zeta <= K_t(x' - y'),
then summing over a with the weights of (C7) and using env(v tensor w) <= env(v) env(w), gives the envelope inequality

(C34) env(Bcal(v,w))(x', s) <= int_0^s (K_(s-t) * (env(v) env(w))(t))(x') dt.

The axial supremum is never moved outside a transverse integral. (The same argument, with |O| the sum of the absolute values of all 27 kernel entries, gives (C34) with
constant one also for the axial supremum of the weighted sum of entries; the envelope (C7) is used because it is convenient.)

C.7 The residual response.

The source of (C30) satisfies, with ell = 1 + log(1/delta),

(C35) Y_infinity(b(Z_delta)) <= C_src delta ell,   Y_3(b(Z_delta)) <= C_src delta^(1/3),
      C_src = 1 + 10^6 N_P,
      N_P = ||P_R||_infinity + ||P_R||_1 + ||r P_R||_infinity + ||r P_R||_1 = C_R [1 + pi^2/70 + (1/7)(7/8)^8 + 2 pi^2/105],

where the norms of P_R are taken on R^4 and r P_R means |x'| P_R(x'). The proof has four steps.

(i) Change of transverse dimension. For a nonnegative radial U on R^4 with A_U = ||U||_1 finite, put U_xi = exp(xi Delta_4) U and
M_xi = ||U_xi||_infinity, and measure U_xi on R^2 through its radial restriction. Splitting the R^2 integral at radius rho, and using
2 pi r dr <= (1/(pi rho^2)) 2 pi^2 r^3 dr for r >= rho together with conservation of the R^4 mass,

(C36) ||U_xi||_(L^3(R^2))^3 <= pi rho^2 M_xi^3 + A_U M_xi^2/(pi rho^2),
      ||U_xi||_(L^3(R^2)) <= 2^(1/3) A_U^(1/6) M_xi^(5/6),
      ||U_xi||_(L^3(R^2)) <= D(U) (1+xi)^(-5/3),   D(U) = 8 (||U||_1 + ||U||_infinity).

The middle line takes rho^4 = A_U/(pi^2 M_xi); the last uses M_xi <= min(||U||_infinity, A_U/(16 pi^2 xi^2)) and the weighted
arithmetic-geometric mean inequality, treating xi <= 1 and xi >= 1 separately. Similarly
||U_xi||_infinity <= 4 (||U||_1 + ||U||_infinity) (1+xi)^(-2).

(ii) Pointwise majorants. Fix a source time t and a heat age mu = s - t. By (B28) and A^(-1) exp(mu Delta_5) = int_mu^infinity
exp(xi Delta_5) d xi, the velocity b(exp(mu Delta_5) R_delta(t)) is given by (C4) with Psi = int_mu^infinity exp(xi Delta_5) R_delta(t) d xi.
Each Cartesian derivative of order at most two of a component of (C4) is a sum of at most four terms d^beta Psi with |beta| <= 2
(counting the coefficient 2 of Psi in the axial component) and at most two terms x_i d_j d^gamma Psi with |gamma| <= 2. Move the
derivatives of order at most two onto R_delta and use (C24); since int_R G_5(xi, (x', zeta)) d zeta = G_4(xi, x'),
|d^beta exp(xi Delta_5) R_delta| <= delta exp(xi Delta_4) P_R uniformly in z. For the coordinate terms, the elementary Gaussian bounds

(C37) |(x_i - y_i) d_j G_5(xi, X - Y)| <= 32 G_5(2 xi, X - Y),   |d_j G_5(xi, X - Y)| <= 32 xi^(-1/2) G_5(2 xi, X - Y),

(the constants are 2^(5/2) times the maxima of (w/2) exp(-w/8) and of (w^(1/2)/2) exp(-w/8) over w > 0, at most 8.4 and 3.5) and
|x_i| <= |x_i - y_i| + |y'| give |x_i d_j d^gamma exp(xi Delta_5) R_delta| <= 32 delta [exp(2 xi Delta_4) P_R + xi^(-1/2) exp(2 xi Delta_4)(r P_R)]
uniformly in z.

(iii) Time integrals. By (C36) and the bounds

(C38) int_mu^infinity (1+xi)^(-5/3) d xi = (3/2)(1+mu)^(-2/3),   int_mu^infinity xi^(-1/2)(1+xi)^(-5/3) d xi <= 5 (1+mu)^(-2/3),
      int_mu^infinity xi^(-1/2)(1+xi)^(-2) d xi <= 6/(1+mu),

each of the 39 entries of the envelope (3 components and 1 + 3 + 9 ordered derivatives) has L^3(R^2) norm of its axial supremum at most
delta [102 D(P_R) + 320 D(r P_R)] (1+mu)^(-2/3), and sup norm at most delta [272 N_1 + 1536 N_2]/(1+mu), with
N_1 = ||P_R||_1 + ||P_R||_infinity and N_2 = ||r P_R||_1 + ||r P_R||_infinity. Since D(P_R) + D(r P_R) = 8 N_P and N_1 + N_2 = N_P,
||env(b(exp(mu Delta_5) R_delta(t)))||_3 <= 39 x 320 x 8 N_P delta (1+mu)^(-2/3) = 99840 N_P delta (1+mu)^(-2/3), and the sup norm of the
same envelope is at most 39 x 1536 N_P delta/(1+mu) = 59904 N_P delta/(1+mu). No property of R_delta beyond (C24) is used, and R_delta may
depend on t.

(iv) Integration in the source time. Since the axial supremum of a time integral is at most the time integral of the axial suprema, the
envelope of b(Z_delta)(s) is at most the integral over mu in [0, s] of the envelopes above. For s <= S_delta,
int_0^s (1+mu)^(-2/3) d mu = 3[(1+s)^(1/3) - 1] <= 3 (2 delta^(-2))^(1/3) <= 4 delta^(-2/3) and
int_0^s (1+mu)^(-1) d mu = log(1+s) <= log(1 + delta^(-2)) <= 2 ell. This gives (C35) with the margins 399360 N_P < 10^6 N_P and
119808 N_P < 10^6 N_P.

C.8 Bilinear and linear estimates.

For fields v, w put x_v = Y_infinity(v) and y_v = Y_3(v). By (C34) and Young's inequality, with ||K_t||_(3/2) <= c_(3/2) t^(-5/6),
||K_t||_1 <= c_1 t^(-1/2) and ||K_t||_3 <= c_3 t^(-7/6),

(C39) Y_3(Bcal(v,w)) <= 6 c_(3/2) S_delta^(1/6) y_v y_w,
      Y_infinity(Bcal(v,w)) <= 8 c_1^(1/4) c_3^(3/4) (x_v x_w)^(1/4) (y_v y_w)^(3/4).

For the first line, env(v) env(w) belongs to L^(3/2) with norm at most y_v y_w, L^(3/2) * L^(3/2) maps to L^3, and
int_0^(S_delta) t^(-5/6) dt = 6 S_delta^(1/6). For the second, the integrand is at most min(c_1 t^(-1/2) x_v x_w, c_3 t^(-7/6) y_v y_w);
splitting at t_0 = [c_3 y_v y_w/(c_1 x_v x_w)]^(3/2) and integrating to infinity gives 2 c_1 x_v x_w t_0^(1/2) + 6 c_3 y_v y_w t_0^(-1/6),
which equals the stated bound. Define the delta-dependent norm and constant

(C40) |||v|||_delta = max{Y_infinity(v)/(delta ell), Y_3(v)/delta^(1/3)},   C_N = max{8 c_1^(1/4) c_3^(3/4), 6 c_(3/2)}.

Since S_delta^(1/6) delta^(2/3) = delta^(1/3) and (delta ell)^(1/2) (delta^(1/3))^(3/2) = delta ell^(1/2) <= delta ell, (C39) gives
|||Bcal(v,w)|||_delta <= C_N |||v|||_delta |||w|||_delta.

For the terms linear in e, let Iw(m,p) = ||(1+r)^(-m)||_(L^p(R^2)) = [2 pi/((mp-1)(mp-2))]^(1/p) for mp > 2, and

(C41) l_1 = A_b [4 c_1 + 2 c_infinity Iw(7,1)],   l_2 = 2 A_b c_infinity Iw(2,3/2),
      l_3 = A_b [2 c_1 (Iw(7,3) + Iw(2,3)) + 6 c_3 Iw(7,1)],   l_4 = 6 A_b c_3 Iw(2,3/2),
      C_L = max{l_1 + l_2, 2 l_3 + l_4}.

By (C24), env(b_app) <= A_b [(1+r)^(-7) + delta (1+r)^(-2)] <= 2 A_b. For heat ages t <= 1 use ||K_t * Phi||_p <= c_1 t^(-1/2) ||Phi||_p
with p = infinity and p = 3, ||env(b_app) env(v)||_infinity <= 2 A_b x_v and ||env(b_app) env(v)||_3 <= A_b (Iw(7,3) + Iw(2,3)) x_v; the
integral of c_1 t^(-1/2) over [0,1] is 2 c_1. For t >= 1 use ||K_t * Phi||_infinity <= c_infinity t^(-3/2) ||Phi||_1 and
||K_t * Phi||_3 <= c_3 t^(-7/6) ||Phi||_1, whose integrals over [1, infinity) are 2 c_infinity and 6 c_3, together with Hoelder's
inequality ||env(b_app) env(v)||_1 <= A_b [Iw(7,1) x_v + delta Iw(2,3/2) y_v]. This gives, for either order of the arguments,

(C42) Y_infinity(Bcal(b_app, v)) <= l_1 x_v + l_2 delta y_v,   Y_3(Bcal(b_app, v)) <= l_3 x_v + l_4 delta y_v,
      |||Bcal(b_app, v)|||_delta <= C_L |||v|||_delta,   |||Bcal(v, b_app)|||_delta <= C_L |||v|||_delta.

The norm conversion uses delta^(1/3)/ell <= 1, delta^(2/3) ell <= 2 and delta <= 1 for 0 < delta <= 1 (with delta = exp(-t), the middle
quantity is (1+t) exp(-2t/3), whose maximum is (3/2) exp(-1/3) < 2). The weight (1+r)^(-2) of u_delta is not integrable on R^2; it is
paired with the L^3 envelope through its L^(3/2) norm, which is why the transverse L^3 norm is used.

C.9 The fixed point, the exact solution and the strain.

Set

(C43) epsilon_* = min{epsilon_0, 1/[8 (C_L + 2 C_src C_N)]}.

Fix 0 < delta <= 1 and 0 <= epsilon <= epsilon_*. Let Y_delta be the space of vector fields v on [0, S_delta] x R^3 whose spatial
derivatives of order at most two are bounded and continuous on [0, S_delta] x R^3 and for which |||v|||_delta is finite. It is a Banach
space with the norm |||.|||_delta: a Cauchy sequence converges uniformly with these derivatives, and Fatou's lemma bounds the L^3 envelope
of the limit. The source b(Z_delta) belongs to Y_delta by (C35), and the right side of (C30) maps Y_delta into itself by (C40), (C42) and
dominated convergence with the kernel bound (C32). On the ball |||e|||_delta <= 2 C_src the right side of (C30) has norm at most
C_src + epsilon [4 C_src C_L + 4 C_src^2 C_N] <= 3 C_src/2 and Lipschitz constant at most epsilon [2 C_L + 4 C_src C_N] <= 1/4. Hence
(C30) has a unique solution e in this ball on the whole window [0, S_delta], and

(C44) Y_infinity(e) <= 2 C_src delta ell,   Y_3(e) <= 2 C_src delta^(1/3).

The exact solution is identified as follows. For fixed delta the force P_3(r F_delta e_r) is smooth and belongs to H^m(R^3) for every m,
since r F_delta e_r = (x_1, x_2, 0) F_delta is smooth, axially compact and rapidly decreasing. By the classical local theory for the
Navier-Stokes equations with forcing (the energy method of A. J. Majda and A. L. Bertozzi, Vorticity and Incompressible Flow, Cambridge
University Press, 2002, Chapter 3, which applies with an added forcing term), (C27) has a unique solution b in C([0, s_*); H^m) for every
m >= 3 on a maximal interval [0, s_*), smooth on [0, s_*) x R^3, and if s_* is finite then int_0^(s_*) ||grad b||_infinity ds is infinite.
By uniqueness and the invariance of (C27) under rotations about the axis and reflections in planes containing it, b is axisymmetric
without swirl. On every interval [0, s'] with s' < min(s_*, S_delta), and on [0, S_delta] if s_* > S_delta, both b and b_app + e are
bounded mild solutions of (C27). By (C32), their difference w satisfies ||w(s)||_infinity <= C' int_0^s (s-t)^(-1/2) ||w(t)||_infinity dt,
with C' a fixed multiple of epsilon C_O times the sum of the sup norms of b and b_app + e on that interval; a bounded solution of this
Volterra inequality vanishes, so w = 0. Hence ||grad b||_infinity <= 2 A_b + Y_infinity(e) on [0, min(s_*, S_delta)), so s_* > S_delta and
b = b_app + e on [0, S_delta]. By C.5, H = (curl b)_theta / r is a smooth solution of (C5), b = b(H), and e = b(H) - b(h_delta). Then
eta_s = alpha^2 C G H(R/delta, Z/delta, nu tau/delta^2) is a smooth solution of (C1) on [0, 1/nu], with eta_s(0) = 0.

Since e is smooth and axisymmetric without swirl, e^r(0, z, s) = 0, and the fundamental theorem of calculus along a radial segment gives

(C45) |a(H - h_delta)| = |e^r|/r <= ||grad e(s)||_infinity <= Y_infinity(e) <= 2 C_src delta ell.

No singular integral of an L^infinity vorticity bound is used.

C.10 Constants, pointwise bounds and work.

Choose

(C46) epsilon_1 = min{epsilon_*, sqrt(D_0/(8 m K_w))},   M_b = 8 (A_b + C_src),
      alpha = min{1, sqrt(epsilon_1)/G, 1/[4(1 + S_v)], 1/sqrt(4 G (1 + M_b)), 1/(1 + Gamma_v)},
      delta_1 = min{1, 1/C, (G/C)^(1/3), D_0/(8 C_loc), [D_0/(16 A_F C_src)]^2},
      c = pi alpha^4 C G^3 D_0.

These constants have no circular dependence: the profiles and the periodic constants (C9)-(C18) come first, then the approximation
constants (C23)-(C26), then the kernel constants (C32)-(C33), C_src, C_N, C_L and epsilon_*, then epsilon_1, M_b and alpha, and finally
delta_1 and c. None depends on delta or on the solution of (C5). With epsilon = alpha^2 G^2 <= epsilon_1, let 0 < delta <= delta_1.

Pointwise bounds. Since delta ell <= 1 for 0 < delta <= 1, (C24) and (C44) give env(b(H)) <= env(b_app) + env(e) <= 2 A_b + 2 C_src,
so ||b(H)||_infinity + ||grad b(H)||_infinity + ||grad^2 b(H)||_infinity <= 4 (2 A_b + 2 C_src) = M_b throughout the window. The swirl
vector (R q) e_theta equals alpha C delta^2 chi(delta z) v in cell coordinates, with v the field of (B30), and b_s = alpha^2 C G delta^2 b(H).
Record derivatives are delta^(-1) times cell derivatives, so by (B31), for j = 0, 1, 2,

(C47) ||grad^j u||_infinity <= C delta^(2-j) [alpha S_v + alpha^2 G M_b] <= (C/2) delta^(2-j),
      |R^2 q| <= alpha C delta^3 Gamma_v <= C delta^3 = G nu,

since alpha S_v <= 1/4, alpha^2 G M_b <= 1/4 and alpha Gamma_v <= 1. For delta <= min(1, 1/C, (G/C)^(1/3)) this gives the first two lines
of (C3) on [0, 1/nu]: |u| <= (C/2) delta^2 <= 1, |grad u| <= (C/2) delta <= 1, |grad^2 u| <= C/2, and G nu <= G because nu <= 1.

Work. By (C45), int int r^2 F_delta dr dz <= A_F/delta and the window length delta^(-2),
|J_tr[H] - J_tr[h_delta]| <= 2 A_F C_src delta ell delta^(-3). With (C26),

(C48) J_tr[H] <= delta^(-3) [-D_0 + m K_w epsilon^2 + C_loc delta + 2 A_F C_src delta ell].

Here m K_w epsilon^2 <= D_0/8 since epsilon <= epsilon_1; C_loc delta <= D_0/8 since delta <= D_0/(8 C_loc); and, since
delta ell <= 2 delta^(1/2) for 0 < delta <= 1 (the maximum of (1+t) exp(-t/2) is 2 exp(-1/2) < 2), 2 A_F C_src delta ell
<= 4 A_F C_src delta^(1/2) <= D_0/4. Hence J_tr[H] <= -D_0/(2 delta^3), and (C6) gives

(C49) W_s/nu = -2 pi alpha^4 C G^3 delta^3 J_tr[H] >= pi alpha^4 C G^3 D_0 = c.

This proves (C3). Taking the positive part of the spatially integrated rate before integrating in time can only increase the integral,
so (B55) holds for this family with the same c. The constant c is positive once alpha is fixed; no lower bound uniform as alpha tends to
zero is asserted, since the work carries the factor alpha^4. The order is exactly critical: |a(H)| <= ||grad b(H)||_infinity <= M_b
and the mass bound give |J_tr[H]| <= A_F M_b delta^(-3), so by (C6) W_s/nu <= 2 pi alpha^4 C G^3 A_F M_b, and the same bound holds with
the positive part of the spatially integrated rate.

C.11 Scope.

Appendix C shows that, in the prescribed-swirl model in which eta_s is transported by its own poloidal velocity, the three Case 2 spatial
velocity bounds and the circulation bound do not imply nu int (Pi_s)_+ dt -> 0. It does not concern the coupled evolution: q is
prescribed and does not solve the swirl equation (it is maintained by prescription, not evolved by transport and compression), and the canonical-pressure,
time-derivative, gradient-record and nonconstant-limit conditions of Case 2 are not part of the construction. The constants C_O, A_b, C_R
and C_a are defined as finite suprema and are not evaluated numerically, and neither are alpha and delta_1. The existence of the smooth
solution in C.9 relies on the classical local theory and continuation criterion for the forced Navier-Stokes equations, cited and not
reproduced here.
