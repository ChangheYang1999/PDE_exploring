# Case 2: the finite-axis, zero-swirl ancient Euler branch of axisymmetric Navier-Stokes

**Status: UNRESOLVED_NOT_ACCEPTED**.

**Final status.** Neither endpoint of the prompt was reached. No complete exclusion of Case 2 on one fixed trajectory was proved,
and no fixed-datum counterexample was constructed or proposed, so neither COMPLETE_THEOREM_VERIFIED nor
COMPLETE_FIXED_DATA_COUNTEREXAMPLE_VERIFIED applies. The first missing implication is an upper bound, valid along every Case 2 record
sequence of the fixed solution, on the signed self-compression of the swirl by the strain of the vorticity the swirl has itself produced:
limsup_n nu_n int_0^{t_n} Pi_s dt < 2 m_phi/(3P), equivalently limsup_n nu_n (Sigma(t_n) + int_0^{t_n} D_Sigma dt) < 2 m_phi/P
(R2.18 (a); the notation is defined below, in Theorem 9 and in R2.16). The proved lower bound
nu_n int_0^{t_n} Pi_s dt >= (2 m_phi/(3P)) (1 - o(1)) shows that any independent proof of this inequality excludes Case 2; no such
proof is available, and none of the proved bounds on the whole history that bear on it is better than critical.

**Run times.** This round of research on the case began at T0 = 2026-10-17T19:11Z and ended at T_end = 2026-10-19T19:15Z (UTC), an elapsed time
of 48 h 4 min, so the prompt's minimum of 24 hours of research on this case was met. An earlier round had worked on the case from
2026-10-15T23:25Z to 2026-10-17T03:04Z (about 27.7 hours) and published a report with the same status.

**What this round added to the earlier report.** The earlier report already contained the reductions and the bounded, nonconstant,
swirl-free ancient Euler limit (Theorem 1), the persistence window (Theorem 2), the production P_n -> m_phi > 0 (Theorem 3), the
localization and adjoint estimates (Theorems 5, 6 and 8 and Proposition 7), the forward self-compression bound (Theorem 9) and the constructions of
Appendices A to C. This round (items R2.1 to R2.18 below, and additions to Sections 1 to 5 and the appendices) added the following.
(1) The open problem reduced to the one signed inequality above and to its stored-plus-dissipated-swirl form, with proved necessary
conditions: B_n = Sigma(t_n) + int_0^{t_n} D_Sigma dt = o(S_n), hence nu_n S_n -> infinity; liminf nu_n B_n >= 2 max(||(eta_U(., 0))_+||_{L^1}, ||(eta_U(., 0))_-||_{L^1});
and, by a cited regularity criterion of Chen, Fang and Zhang (statement read, proof not checked), int_0^{T_*} D_Sigma dt = infinity
at every singular time (R2.16, R2.18 (a)).
(2) A kinematic window for the Hessian constant (F2): for C_* < 0.2700... hypothesis (A) fails for every solution with D(t) > 0; for
C_* < 7^{1/2}/8 the nonconstant swirl-free Case 2 limit is impossible; for C_* > Q_core suitably scaled thin vortex rings have all the
properties of the limit listed in Theorem 1, so those properties alone cannot exclude Case 2 there. The bound Q_core < 0.452 rests on
computer-assisted interval enclosures whose programs are not reproduced here.
(3) Proved tools that do not exclude Case 2 (among them forward non-burst on a short record window, energy-Casimir budgets for a swirl
cell core, and supply and enhanced-dissipation lemmas; the proved parts of R2.1 to R2.15, as marked there), a count-level comparison of
one band scenario with the necessary conditions of this report, conditional on numerical ring-model inputs, that finds no obstruction
growing as nu_n -> 0 (R2.17), and the share bound of Appendix C, C.11 (in the prescribed-swirl model only).
(4) Numerical evidence in reduced cell models, which are not results about the solution: an isolated saturated swirl core was not
sustained in the runs made, while an axial strain with enough power near twice its first Kelvin frequency pumped it in the runs tested; the
candidate mechanism (Q) of R2.18 (c) describes how a Case 2 history could violate the inequality in that scenario, and is not proved
necessary or sufficient.
(5) Repairs of the earlier text found in independent audits: a gap in the proof of the last assertion of Theorem 6 (d) (now proved by a
penalization argument), the barrier in the maximum principle of the proof of Theorem 2 (now quartic), and the further corrections listed
in Section 5.
The first missing implication is of the same kind as in the earlier report (an upper bound along the actual history that contradicts the
forced production), now reduced to the single signed inequality stated above.

**Summary for the reader.** The object is the maximal smooth solution of the three-dimensional Navier-Stokes equations from one fixed smooth, decaying,
axisymmetric datum u_0 in H^infinity with finite energy and finite circulation bound G (both defined below), which is assumed to become
singular at a finite time, under the branch hypotheses (A) (the velocity Hessian is controlled by the square of the gradient at all
sufficiently late times, M H <= C_* D^2, with M, D and H the historical suprema of |u|, |grad u| and |grad^2 u| and C_* > 0 a
constant) and NO-SWIRL-EXTRACTION, both stated in Section 1. Case 2 is the branch in which genuine
first-crossing records of the velocity gradient lie at a bounded distance from the axis in units of the record length l_n = M_n/D_n
(M_n, D_n the values of M, D at the record time t_n; alpha_n = r_n/l_n -> alpha_* < infinity, r_n the distance of the record point
from the axis); Theorem 1 shows that a subsequence of the rescaled flows then converges to a bounded, nonconstant, swirl-free
ancient solution of the Euler equations. The task was to exclude this branch on such a trajectory or to construct a fixed datum that
realizes it. Neither is achieved.
Notation for these pages (restated in Section 1). The viscosity is 1, the datum u_0 has energy E_0 = ||u_0||_2^2, and
G = ||r u_0^theta||_infty bounds the circulation Gamma = r u^theta for all time. In cylindrical coordinates (r, theta, z) about the
symmetry axis, q = u^theta/r and eta = omega^theta/r, omega the vorticity. M, S, D and H are the historical suprema over [0, t] of
|u|, |u^theta|, |grad u| and |grad^2 u| (Cartesian Frobenius norms), and M_n, S_n, D_n are their values at the record time t_n. At
a record (x_n, t_n), r_n is the distance of x_n from the axis, l_n = M_n/D_n is the record length and nu_n = D_n/M_n^2; the rescaled
flows are U_n(y, tau) = u(a_n + l_n y, t_n + tau/D_n)/M_n, a_n the point of the axis at the height of x_n, U is their limit along a subsequence on which the convergence of Theorem 1 holds (fixed once and for all and relabelled by n, so that all later limits in n are taken along it) and eta_U its eta. For fixed delta, L, kappa > 0, a packet is a fixed smooth axisymmetric phi >= 0, not identically 0, supported in a solid torus in {R > delta, |Z| < L} (R, Z the
rescaled cylindrical coordinates of y) on which eta_U(., 0) >= 2 kappa > 0 (if necessary after replacing u by Q u(Qx, t), Q = diag(1, 1, -1), which satisfies the same hypotheses and reverses the sign of eta; Theorem 3); m_phi = int eta_U(y, 0) phi(y) dy and P = ||phi||_infty. Psi_n solves the backward adjoint
drift-diffusion problem of Theorem 3 with terminal value phi((x - a_n)/l_n) at t_n, and P_n = - nu_n int_0^{t_n} int q^2 d_z Psi_n dx dt
is the normalized production of the packet. Q_4(I) = int_I int q^4 dx dt for a time interval I; A_max(n) = c (C_* max(G, 1) nu_n)^{-1/2}
is the persistence window of Theorem 2 (c > 0 independent of n, reduced once the packet is fixed, as in Theorem 3); the normalized dissipation of a time set is nu_n times the space-time integral of
|grad_y U_n|^2 over its rescaled image (Theorem 8 (a)). The cell models (here G > 0; for G = 0 there is no swirl source and the branch is empty) use the length unit delta_n = (G nu_n/C_*)^{1/3} and the time
unit delta_n^2/nu_n (one cell time), both in record units; the interpolation cap is the bound |q_n| <= 2 G kappa_c, q_n = U_n^theta/R the record-unit q (q = D_n q_n at corresponding
points) and kappa_c = nu_n/delta_n^2, which the Hessian bound of (A) and the circulation bound imply (R2.17); the cell computations monitor a cap of this form, and whether the cap of a computation coincides with this bound once the core is embedded with the circulation margin it needs is not checked.
What is proved. (i) Reduction and persistence (Theorems 1, 2): the swirl and the viscosity become negligible at the record scale
(S/M -> 0, nu_n = D_n/M_n^2 -> 0), and the sup norm of the gradient at the rescaled age A (time t_n - A/D_n) is at least c' (1 + A)^{-1/2} D_n, c' > 0 a constant,
over the growing window 0 <= A <= A_max(n). (ii) Production (Theorems 3, 5, 6, 8 and Proposition 7): tested against a fixed packet phi with
m_phi > 0, the vorticity of the limit must be produced by the swirl source d_z(q^2) of the eta equation, with normalized production
P_n -> m_phi; the production at ages up to K l_n^2 (K fixed) comes, up to an o(1) error, from a tube of radius o(l_n) around the axis,
the compression work int_0^{t_n} int (u^r/r)_- q^2 r dx dt (x_- = max(-x, 0)) is at least of order 1/nu_n (Theorem 9 (b)),
production at ages much larger than the viscous time l_n^2 of the record length is penalized unless the older history carries
correspondingly more int int q^4 dx dt, and nothing proved makes the band of ages between nu_n^{1/2} l_n^2 and l_n^2 negligible.
(iii) Forward form (Theorem 9, R2.16): the same production forces the swirl to compress itself through the vorticity it has produced;
with Sigma = int (u^theta)^2/r dx, D_Sigma = 2 int |grad q|^2 r dx + int q^2/r dx its dissipation, a = u^r/r split as a = a_r + a_s (a_s from the vorticity the swirl has produced, |a_r| bounded by a constant C_0 of the data, Theorem 9 (d)) and Pi_s = -int a_s q^2 r dx, one has d Sigma/dt = -D_Sigma + 3 Pi_s - 3 int a_r q^2 r dx and nu_n int_0^{t_n} Pi_s dt >= (2 m_phi/(3P)) (1 - o(1)).
(iv) The open problem in one statement (R2.18 (a)): an independent proof of
limsup_n nu_n int_0^{t_n} Pi_s dt < 2 m_phi/(3P) along every Case 2 sequence would exclude Case 2.
Why this is open. None of the proved bounds on the whole history that bear on this inequality is better than critical (none gains a power of nu_n over the order 1/nu_n; the bounds of R2.16 on restricted record windows gain powers of nu_n but leave the rest of the history uncontrolled), and the circulation bound G and the Hessian constant C_* enter only as fixed constants; the comparisons of sizes, budgets and numbers of structures made
for one model scenario give no obstruction that grows as nu_n -> 0 (R2.17), and
the identities and functionals tried fail for the reasons recorded in Sections 3 and 4 and in the Round 2 items. Constructions with
prescribed fields (Section 4 (x), Appendices A to C) show, in prescribed or model settings, that parts of the pointwise record bounds do not by themselves imply two estimates bearing on the closure: the four pointwise velocity bounds do not imply the small-variation bound for the adjoint of Theorem 8 (b) for all fixed smooth terminal data (one prescribed swirl-free family and one fixed nonnegative terminal function, which need not be a positive limiting-vorticity packet, violate it: Section 4 (x), Appendix A, Open (5); exclusion through it also needs control of the older history), and the three spatial velocity bounds with the circulation bound do not imply the bound nu_n int (Pi_s)_+ dt -> 0 when the swirl is prescribed, with or without transport of the sourced vorticity (Appendices B and C, Open (6), which would suffice).
Model evidence (not results about the solution). In reduced models of a swirl-saturated core with a prescribed axial strain
(R2.8 to R2.14) an isolated core was not sustained in the runs made, while an axial strain oscillating near twice the core's first
Kelvin frequency amplifies it in the runs tested (no general spectral criterion is established; in the linear model of R2.14 a spatially uniform random multitone strain over a broad
frequency band, with root-mean-square size about five to nine times that of a tuned forcing (prescribed axial strain a_0 + beta Omega cos(d Phi), a_0 the constant mean strain of the strained column, with phase Phi' = Omega, Omega the drifting inertial sum frequency and d a
detuning factor, with beta = 0.03; R2.14 (a)) that gives only transient amplification, also amplifies it over
the run in half or more of the sampled realizations at G = 5000); in a thin-ring model a finely tuned pair of coaxial vortex rings in an almost strain-free
surrounding supplies such a strain, and in one nonlinear cell run (G = 3000, single-wavenumber seed) it pumps the core to the interpolation cap of that computation in about thirteen exchanges, 0.025 cell times in all, an exchange being one period of the axis strain signal of the leapfrogging pair (whether that cap corresponds to the cap of (A) for an embedded core is not checked). The candidate mechanism (Q) of R2.18 (c) asks whether a Case 2 history supplies such strains where and as long as Case 2 needs them and delivers the eta produced there to the packet; (Q) is not proved to be necessary or sufficient for the failure of the open inequality.
Layout. Round 2 additions (a brief, then items R2.1 to R2.18, the newest); Section 1, Result (setting and theorems); Section 2, Method;
Section 3, Findings; Section 4, Limitations and open questions; Section 5, Verification (how each statement was checked);
Appendices A to C (complete proofs of the constructions). The paragraphs below, to the start of the Round 2 additions, are the
detailed status statement.

First missing implication: an upper estimate, valid along every Case 2 record sequence of the fixed solution, that contradicts the convergence P_n := - nu_n
int_0^{t_n} int q^2 d_z Psi_n dx dt -> m_phi > 0 of the normalized production of the limiting vorticity packet (Theorem 3(b), (d); Psi_n is
the backward adjoint of Theorem 3 with terminal packet phi and m_phi = int eta_U(y,0) phi(y) dy), for example limsup_n P_n < m_phi. Sufficient
conditions and related questions are listed in Section 4, Open (1) to (6) (items (1) to (3) and (6) suffice, the estimate of F10 (d) in (6) provided its formal identity holds along the solution, (5) together with control of the older history; (4) is a structural question); none is proved, and no equivalence between them is asserted.

The estimates prove that a definite positive part of the
production of the limiting vorticity packet comes from the middle history (rescaled times between a growing recent window
A_max(n) ~ nu_n^{-1/2} and any early epoch [0, s_n] with Q_4([0, s_n]) = o(D_n M_n)), and also from the part of the middle history inside a tube
{r < lambda_n} around the axis with physical radius lambda_n -> 0, and that this part carries int int q^4 dx dt >= c D_n M_n
(Theorem 3(e), (f), the latter combined with the exterior part of the Cauchy-Schwarz bound (c)); these lower bounds do not assert that the complementary contributions are o(1). The positive excess (eta - kappa D_n^2/M_n)_+ of the packet is produced after the last time sigma_n
at which sup eta <= kappa D_n^2/M_n, inside {eta > kappa D_n^2/M_n} (within distance C l_n of the axis), at times when the Hessian is within a
fixed factor of its record (this concerns the excess, not the full signed pairing).

By the decay of the adjoint, our estimates penalize
production at ages t_n - t much larger than l_n^2 = M_n^2/D_n^2 unless the older history carries correspondingly more int int q^4. In the
band of ages between the proved window A_max(n)/D_n ~ nu_n^{1/2} l_n^2 and l_n^2 only persistence-or-production alternatives are proved;
nothing makes the contribution of that band negligible. For fixed K >= 1 the production at ages up to K l_n^2 comes, up to an o(1) error
in the normalized pairing, from a tube of radius nu_n^{1/6 - epsilon} l_n = o(l_n) (0 < epsilon < 1/6) around the axis, and the same holds
with a tube of radius o(l_n) up to ages Lambda_n l_n^2 whenever Lambda_n nu_n^{1/2} -> 0 (Theorem 8(a), for nu_n L <= Lambda_n <= t_n/l_n^2). Let Vbar_n be the average over the
rescaled ages [0, Lambda_n/nu_n] of the axial total variation of the adjoint, averaged radially with a weight concentrated at the swirl
crossover radius (G nu_n/C_*)^{1/3} l_n/2^{1/2} (the quantity V_nu(s) = int_0^infty w_nu(R) int |d_Z psi_n(R, Z, -s)| dZ dR of Theorem 8(b), psi_n the rescaled adjoint,
w_nu(R) = min(R/r_c^2, r_c^2/R^3) and r_c = delta_n/2^{1/2}). The contribution of ages up to Lambda_n l_n^2 is negligible if
Lambda_n nu_n^{1/3} Vbar_n -> 0 (Theorem 8(b)); for fixed Lambda_n = K this is the condition Vbar_n = o(nu_n^{-1/3}). Over
the whole history the same rescaled quantity, integrated in age, must be at least of order nu_n^{-4/3} (Theorem 8(b), all ages). The required
bound has not been proved for the Case 2 adjoints.

Section 4 (x), with the complete proof in Appendix A, gives a prescribed swirl-free construction
showing that the four pointwise velocity bounds (|U| <= 1, |grad U| <= 1, |grad^2 U| <= C_*, d_t U bounded; G enters only as a parameter of the weight) do not imply it for all fixed smooth terminal data: its weighted variation is at
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
the production there from above by less than the required amount, and none proves TARGET-2 (the decay condition liminf_{A -> infinity} sqrt(1+A) limsup_n D(t_n - A/D_n)/D_n = 0 of Theorem 1 (d), which would exclude Case 2) or any other substitute. Case 2 is not settled here for arbitrary C_* >= 7^{1/2}/8 = 0.3307... (for C_* < 0.2700... hypothesis (A) fails for every solution with D(t) > 0, and for C_* < 7^{1/2}/8 the nonconstant Case 2 alternative is impossible because its limit is swirl-free, F2), and no fixed-datum counterexample is proposed. For C_* > Q_core, a constant of F2 that is at least 7^{1/2}/8 and, by a computer-assisted enclosure whose programs are not reproduced here, less than 0.452, the properties of the limit listed in Theorem 1 cannot exclude Case 2 by themselves, since suitably scaled thin vortex rings have them; the interval 7^{1/2}/8 <= C_* <= Q_core is not fully classified here (the kinematic hypotheses used in F2 alone cannot exclude Case 2 at any C_* > 7^{1/2}/8 in it), and every Case 2 record sequence with C_* < 2^{1/2}/3 = 0.4714... has alpha_* > 0 (F2), which covers the whole interval if the enclosure Q_core < 0.452 is accepted.

On the forward side (Theorem 9) the same production forces the swirl to do compression work on itself, through the vorticity it has
generated: the positive part of the self-compression rate in the scale-invariant functional int (u^theta)^2/r dx has time integral at least
c/nu_n (no matching upper bound is proved). A bound o(1/nu_n) for this integral would exclude Case 2, and so would the weaker requirement limsup_n nu_n int_0^{t_n} e^{3 C_0 (t_n - t)} Pi_s(t) dt < 2 m_phi/(3P) on the time-weighted
signed rate (Theorem 9(d); by R2.16 it is equivalent to the unweighted bound of (iv) above). In a drift-free model with prescribed
swirl, a smooth axially periodic steady example (F10 (c)) disproves a universal nonnegative critical-weight work identity, and a localized
whole-space family started from zero sourced vorticity (Appendix B) obeys the three Case 2 spatial velocity bounds and the circulation
bound and has self-compression nu_n int (Pi_s)_+ dt >= c > 0, the order that Theorem 9 requires; so in that model those bounds alone do not imply nu_n int (Pi_s)_+ dt -> 0. The
same holds, for a sufficiently small fixed amplitude, when the sourced vorticity is transported by its own poloidal velocity (Appendix C). Both
families prescribe the swirl and have zero limiting velocity; whether the smallness holds for the coupled evolution remains open. Their
nonzero steady localized swirl solves the unforced swirl equation for no smooth incompressible meridional velocity, even a time-dependent
one (Section 4, superlevel-set argument).

Separately, suppose the swirl solves its unforced equation and the radial strain not sourced by the swirl obeys the Case 2 bounds. For
cores satisfying the positivity, curvature and persistence hypotheses of Open (6), with curvature constant sigma, persistence over the
rescaled record time 1/nu_n (physical time l_n^2) is excluded for all sufficiently large n if ||a_s||_infinity <= (sigma/2 - epsilon) D_n kappa_n throughout (kappa_n = nu_n/delta_n^2 the cell rate in record units, so that D_n kappa_n is the physical cell rate, delta_n = (G nu_n/C_*)^{1/3}), for some
epsilon > 0 independent of n; no such conclusion is proved for all coupled families. In the coupled critical balance of F10 (d) (a
formal identity, derived under additional integrability and boundary hypotheses) the stretching cancels exactly and the balanced functional is at least of order nu_n^{-2} at the record time (because the limit is nonconstant), and, provided the identity holds along the solution, Case 2 would be
excluded by an absorption of the remaining commutator and cubic transport terms by a fraction epsilon < 1 of the dissipation of that balance, with a remainder of time integral o(nu_n^{-2}); the cubic
term admits no instantaneous bound by a small multiple of the meridional part of that dissipation over arbitrary amplitudes, and whether an integrated estimate holds along the
histories that actually arise is open.

## Round 2 additions (status unchanged)

References in this part. Theorem, Corollary, Proposition and F numbers refer to Sections 1 to 3 of this report. The setting, the branch
hypotheses (A) and NO-SWIRL-EXTRACTION, Case 2 and the record scalings are stated in Section 1 (Setting), and class (C) denotes the
record-scale bounds |U| <= 1, |grad U| <= 1, |grad^2 U| <= C_* of Theorem 1 (b), which the record limits inherit (the Hessian bound almost everywhere). Cell units (length delta_n = (G nu_n/C_*)^{1/3}, rate kappa_c = nu_n/delta_n^2 = C_* delta_n/G in record units, also written kappa_n, viscosity 1) are used in many items. Strain letters are defined item by item (a = u^r/r, a = -u^r/r or a = d_z u^z); on the axis d_z u^z = -2 u^r/r.

Round 2 in brief (details and the status of each statement in the items below).
1. The target in its simplest form (R2.16, proved). With Sigma = int (u^theta)^2/r dx, D_Sigma = 2 int |grad q|^2 r dx + int q^2/r dx its dissipation and B_n = Sigma(t_n) +
   int_0^{t_n} D_Sigma dt, Case 2 forces nu_n B_n >= (2 m_phi/P)(1 - o(1)), and the bound limsup nu_n B_n < 2 m_phi/P would exclude Case 2. Since the argument applies to every axisymmetric test function phi in C_c^infty({R > 0}) with 0 <= phi <= 1 and to the reflected solution of Theorem 3 (R2.16), also liminf nu_n B_n >= 2 max(||(eta_U(., 0))_+||_{L^1}, ||(eta_U(., 0))_-||_{L^1}), so nu_n B_n -> infinity when the limit's eta is not integrable, and in that sub-branch limsup nu_n B_n < infinity would suffice.
   Proved brackets: B_n <= Sigma(0) + (3/4) E_0 S_n and B_n = o(S_n) (S_n the historical swirl maximum), so Case 2 needs nu_n S_n -> infinity;
   the compression work 3 int int (u^r)_- q^2 dx dt on record windows of duration A_n/D_n and axial half-length L_n l_n (all radii) is o(1/nu_n) whenever A_n L_n nu_n^{2/3} -> 0. The stronger
   requirement that B_n stay bounded would imply regularity by a known swirl criterion (R2.16), so it asks more than the exclusion of Case 2 and is not pursued.
2. Proved tools that do not exclude Case 2: forward non-burst on a short record window (R2.1 (a)); axis-silent outer flows (exact construction and initial-time identities; the time
   their silence lasts rests on a numerically evaluated, uncertified coefficient) (R2.2); a drift-free sign lemma of narrow scope (R2.3); a Casimir identity resolved by circulation level, a local bound on the swirl work and an impulse-exchange identity (R2.6); linear tools for a swirl cell (R2.7, the parts stated there as proved); an energy-Casimir budget for a cell core on the free and on the
   uniformly strained column (R2.10) and on a uniform strain of either sign, with a compression-action bound (R2.15; it covers self-generated breathing, so in that model only phases of axial compression of the imposed strain can raise the functional); enhanced-dissipation
   and supply lemmas for a core in a parabolic jet (R2.12); a lower bound on the supply needed to renew cells (R2.13 (b)).
3. Numerical evidence about model problems (not proofs). Unforced coupled runs, resonantly forced cores and swirl-strained cores showed
   no sustained maintenance (R2.4, R2.8, R2.9), and the self-compression of an unforced modulated column has no sign (R2.13 (a)). In
   prescribed forced models, a coherent drive (a jet whose curvature oscillates at an inertial sum frequency of the core, R2.12; an axial
   strain oscillating near twice an inertial frequency, R2.14) pumps a cell and gives self-compression of the critical order while the
   drive stays in resonance, over the forced intervals computed (persistence over the band is unproved), and most of the gain decays once
   the drive is removed (a locked drive of fixed log-stretch amplitude turned over after about 0.4 cell time with the drive still on, and
   one of fixed strain amplitude raised the gain throughout the one run made, as the stretched core's falling frequency increased its
   log-stretch amplitude, R2.14 (c)).
   In a thin-ring model, a tuned pair of coaxial rings (radius R_0), the simplest exterior candidate, keeps an axis fluid point in its
   strain-reversing window for only a bounded number of periods once the core's holding strain acts on the pair as well. Without that
   strain the tuned pair is periodic to numerical accuracy in the thin-ring model and carries the axis point at its centre on a
   numerically near-neutral orbit over the computed exchanges (an exchange is one period of the axis strain signal of the leapfrogging pair), and in one nonlinear
   cell run (G = 3000, single-wavenumber seed) its axis strain pumps the cell model to the interpolation cap of that computation in 12.8
   exchanges (0.025 cell times) with no loss of coherence before the cap (a model-level reading; the same impulse reaches the cap at
   G = 10000 but not at G = 1000, and whether this cap corresponds to the cap of (A) once the core is embedded with the circulation margin
   it needs is not checked). In the single-wavenumber runs made some weaker drives are detuned by the core's spreading before reaching
   the cap while a weaker tuned pair (separation 0.8 R_0) reaches it after about 20 exchanges, and, in a run reported from a separate computation and not checked here, with a seed of 160 axial wavenumbers a drive of half the tuned impulse on a mean axial stretching strain of 4 in cell units stays at a low sub-cap level over the 60 exchanges computed, with negligible signed self-compression (R2.14 (c), (d)).
   By a heuristic production count, episodes at a rate of at least one per 19 to 190 cell times at each axial point of the saturated
   core would match the order of the production budget that Case 2 requires (at the G = 3000 yield, for C_* between 1 and 10, for a
   saturated core L_z record lengths long and a production requirement c_0 over a band of K/nu_n record times with L_z K = c_0, R2.14 (d);
   roughly independent of G in the cell model if an episode lasts a fixed number of exchanges); the count does not show persistence,
   delivery to the packet or realization by a fixed-datum solution.
   The profile-scale estimates of such a pair are compatible with the record-unit kinematic bounds as delta_n -> 0 (certified bounds
   and joint admissibility with the core and the outer flow are not checked), but the pair is far larger than the cell. In the ring
   model with the tested quadratic background, a background axial strain gradient h shortens its neutral window to about 0.56 |h|^{-1/4}
   exchanges (a short-range fit over 1e-5 <= |h| <= 1e-3, h in units of the ring circulation divided by R_0^3); computed directly, with the release at the tuned centre, the window of h around 0 in which the accumulated axial strain integral along the released axis point (ring-induced and background parts together) stays at most 0.5 in modulus at the ends of all thirteen exchanges of the episode is -3.0e-6 < h < 2.6e-6 in these units, which in that configuration is an axial
   strain gradient between about -8e-15 C_* and 7e-15 C_* in record units along the path of the pair at the smallest ring radius
   allowed by the scale estimates of R2.14 (d), and smaller in modulus for larger rings (a measured sensitivity, not a necessary bound). Re-tuning the core size of the pair absorbs the tested constant
   coefficients W_2 of a steady background axial velocity W_2 r^2 (radial curvature 2 W_2; W_2 in the same units as h) except
   W_2 = +0.1, where the scan found no tangency (R2.14 (d)). Whether a Case 2 history can supply such a drive is not known.
4. Open. A bound along the actual history on the stored plus dissipated swirl, as in item 1. By a proved per-length count (R2.16, end),
   Case 2 needs an axial space-time integral of the local record circulation, with a logarithmic weight, at least of order 1/C_*, which at the circulation bound means a record-unit measure in axial position and time at least of order 1/(G C_* nu_n ell_n), ell_n = 1 + log^+(R_1/delta_n) (log^+ x = max(log x, 0)) with R_1 = E_0 D_n^2/(epsilon M_n^3) for a fixed small epsilon > 0 (smaller circulation over a larger measure is not excluded; for example a record length of axis over a time of order l_n^2/(G C_* ell_n), a fraction of order 1/(G C_* ell_n) of the parabolic time l_n^2 before t_n), or terminal swirl
   over nu_n^{-2/3} record lengths; this necessary condition is weak, the pointwise bounds allow it, and nothing available bounds this
   measure at that order. A count-level comparison of the episodic scenario of item 3 with the necessary conditions of this report (caps, pointwise bounds, source mass, the eta-mass inequality, impulse, survival, the per-length count and the measured ring-model tolerances) finds no obstruction that grows as nu_n -> 0, for pairs of radius proportional to delta_n and a datum with large G: the source-mass count for freshly sourced pairs needs G above a threshold between about 3.5e6 and 1.6e8 for an assumed pumped length per pair, and between about 7.4e7 and 1.5e9 for the much shorter pumped length measured in a model; the numbers of episodes and of pairs diverge as nu_n -> 0; it compares scale estimates and gross budgets only and does not show that the scenario is compatible with Case 2 (R2.17). In the ring scenario of R2.17 (e), a uniform holding strain of the survival size contracts a retained pair by a factor between e^{-37} and e^{-374} between episodes, so it is incompatible with the passive reuse of pairs tested there (a mechanism that re-expands or re-tunes a retained pair is neither constructed nor excluded). In a prescribed-strain model, with axial diffusion neglected, the uniform holding strain also lets at most about 10^{-2} of the produced absolute eta-mass escape annihilation at the axis for an assumed production profile matching the measured pumped length, and at most about 5 to 14 per cent if that mass is distributed uniformly in z over the assumed pumped segment, centred at the holder's stagnation point; if the count is made with delivered vorticity, this raises the second threshold range at least about 100-fold and the first at least about 7- to 19-fold. The comparison leaves open, among other things, the assembly of tuned exterior structures from sourced vorticity, the holding of cores between episodes, the repetition over the band and the delivery of the produced eta to the packet. Additional
   inputs such as the non-resonance conditions (N1), (N1') of R2.12 and R2.14 would serve parts of the argument; none is implied by
   the available estimates, and their sufficiency for the full closing argument is not established.

The status remains UNRESOLVED_NOT_ACCEPTED and the first missing implication is unchanged: an upper bound, along the actual Case 2
history, on the weighted signed self-compression of Theorem 9(d), or on its unweighted form; the two are equivalent to each other (R2.16) and to the bound limsup nu_n (Sigma(t_n) + int_0^{t_n} D_Sigma) < 2 m_phi/P on the stored plus dissipated swirl, D_Sigma the dissipation of the swirl balance (R2.16; the dissipation-normalized condition R2.16 (ii) amounts to a uniform bound on the stored plus dissipated swirl, and already the divergence of the total swirl dissipation at every singular time (a consequence of a known swirl regularity criterion, R2.16) shows that (ii) can hold only if there is no singularity; below, (SC) denotes the weighted or the unweighted bound) (a bound on the production P_n itself would also suffice; the energy input and the unweighted swirl work of the models below are diagnostic analogues of these quantities, not established equivalents). Verification
methods are stated item by item (most proofs were checked by hand, some identities by computer algebra, and outlined arguments are marked as such); items marked numerical are evidence about specific model families, not proofs. For an argument through the energy-Casimir budget of the ideal column (R2.10), the terms that budget leaves uncontrolled at a cell core are the jet Reynolds stress (R2.12), the non-uniformity of the outer strain at first order, and the negative part of a spatially uniform strain (R2.15); controlling them has not been shown necessary or sufficient for the missing estimate. In the linearized model with a prescribed jet, a jet whose curvature oscillates at the drifting inertial sum frequency of the core pumps the cell energy parametrically over many cycles (computed over the forced intervals; in the frozen inviscid two-mode reduction the growth continues for as long as coherent forcing above threshold lasts), so that reduction has no amplification bound uniform in the duration of coherent forcing, and the diffusing-column runs show large amplification over the displayed finite intervals (the duration-uniform statement is not established for the full diffusing-column equations), although the energy multiplier per cycle stays bounded (R2.12 (h)). In the nonlinear runs (unrefined finite-time evidence in a prescribed forced model) the pumped waves compress the swirl through the vorticity of the perturbation (the model analogue of the sourced vorticity of Theorem 9 (d), not identified with it) at a rate comparable with the initial swirl integral of the reference column per cell time (the compression term 3 Pi_s of the swirl balance averaging 1.13 times the initial swirl integral of the reference column on the computational domain R < 8 (which omits about 12 per cent of its infinite-radius value) per cell time over 0.3 <= t <= 0.6 in the run reported; sustained over the band, a rate of this scaling gives work of the order that Theorem 9 (d) requires, but the model does not determine the constant), over the reported forced intervals, while the coherent jet is supplied (persistence over the band is unproved; R2.12 (i)); when the prescribed jet is set to zero, most of the gain of the core decays with the waves over the observed interval. These are statements about a forced model; their transfer to the coupled record flow is unproved. The amplitude used in most runs, 0.3 G, is about twice the largest sinusoidal oscillating curvature that a smooth no-swirl Euler field (eta conserved along paths, including the axis; the record limits of Theorem 1 are only C^{1,1}, so applying the cap to them needs an additional argument) can carry along an axial path under the Frobenius Hessian bound (0.158 G, R2.12 (i); for the finite-n Navier-Stokes fields this cap needs additional estimates); at 0.15 G, below that drive-only cap (joint admissibility of drive and core is not established), the forced core is still pumped in the runs made, with growth close to the two-mode formula, once G rho^3 exceeds about 1690 for the core radius rho in cell units (a frozen-coefficient estimate), and at G = 1000 its saturated self-compression is again of the critical order (over [0.6, 0.9] 1.6 times the free decay of the reference); on the strained (Burgers) column of the survival window the same amplitude gives only a weak transient at G = 3000, close to its threshold, and pumps the core at G = 5000 with cumulative self-compression of the same order (numerical, saturated phases not refined, R2.12 (i)). The present argument does not supply the required history-wide bound. A non-resonance property of the actual record-scale flow along the core path ((N1) of R2.12 (h), (i), in the chirp-matched primitive form stated in R2.12 (i)) is one possible additional sufficient input for the two-mode reduction on fixed cell intervals (uniformly over subwindows, with one baseline per interval and the stated modal-coefficient and matrix bounds; it does not by itself control accumulation over the band); nothing available implies it, and its sufficiency for the full closing argument is not established. A second prescribed forcing couples differently: in an idealized unbounded model, a Z-uniform axial strain oscillating along the core path (in record units of amplitude and angular frequency of order delta_n, with zero Hessian, so it adds nothing to the Hessian of the column and is compatible with a fixed velocity-gradient bound for small delta_n) amplifies the linearized cell in bands near twice an inertial frequency, the response being consistent with a half-frequency response over the short window tested; growth continues over the tested interval from a log-stretch amplitude of about 0.04 at G = 3000 and 5000 (transient amplification at about 0.02), and without frequency tracking an amplitude of about 0.08 gives large amplification of the tested material modes during their passage through the band, followed by decline where computed (numerical, linear, R2.14; these levels depend on the seed, mode, forcing and interval tested and are not uniform thresholds). This amplification takes of order G/(C_* delta_n) = G^{2/3} C_*^{-2/3} nu_n^{-1/3} record times, shorter than the persistence window A_max(n) of Theorem 2 for large n; whether the record flow keeps a suitable core and a coherent strain of this kind along the core path for that long, and the realization of such a strain history in a finite-energy record flow, are open; a non-resonance input would also have to cover the log-stretch history along the core path ((N1') of R2.14, a proposed condition whose sufficiency is unproved). On such a strain of either sign the energy-Casimir budget still closes: the functional grows at most by the factor exp(3 int a_-), a_- the negative part of the imposed axial strain a = d_z u^z (here a is not the radial strain u^r/r of Theorem 9), so this channel draws only on compression of the core, and lifting the functional by a factor F needs accumulated compression of at least (1/3) log F (proved, R2.15; for a strain bounded by B in record units this takes at least log F/(3B) record times); this requirement is logarithmic and does not exclude the channel. Supply from inside the cell scale is limited by its reservoir: on the free Oseen column, under the hypotheses of the production link (axial periodicity, finite relative functional, no external input, the circulation, swirl and Hessian bounds), an unforced perturbation of any amplitude (for example a train of coaxial rings) whose accumulated production over T cell times has the critical size satisfies T <= C E~(0)/(G^2 L), E~(0) its energy-Casimir functional and L the axial period in cell units (R2.12 (i), end, from the bounds of R2.10). A blanket kinematic no-increase statement fails: there are small volume-preserving rearrangements of the Oseen profile, with nontrivial radial displacement inside the core, that raise its Eulerian-mean core integrals at second order (R2.12 (i)). Nor is there numerical support for a cell-scale sign law: for an unforced modulated Oseen column at G = 1000 with no initial meridional flow, the accumulated (unweighted) self-compression changes sign on the inertial time scale and at the first inertial time is positive, with ratio to the production budget 1.01 and 1.80 for the two data (numerical, R2.13 (a); the three-code cross-check concerns the self-compression, not the production budget or the ratios); this determines neither the sign of the weighted work of Theorem 9 (d) nor a lifetime bound. Replacing pumping by repeated re-creation of such cells does not lower the supply requirement: under the hypotheses of the production link, critical production over T cell times needs initial functional plus cumulative positive input into E~ of at least a constant times G^2 L T (R2.13 (b), proved by hand from the bounds of R2.10).

R2.1 Forward non-burst (part proved, part conditional, route closed). (a) Proved (this is Corollary (iv) read forward): for
0 <= tau < 1/(C(1+C_*)), D(t_n + tau/D_n) <= D_n/(1 - C(1+C_*) tau), so T_* - t_n >= c/D_n, and on every interval 0 <= tau <= tau_0 < 1/(C(1+C_*))
the velocity amplitude satisfies M(t_n + tau/D_n)/M_n = 1 + O(tau) (this does not locate a velocity maximum). (b) The extension to every fixed K (limsup D(t_n + K/D_n)/D_n < infinity, with an eternal swirl-free Euler limit)
reduces (an outlined reduction: the uniform bounds, the pressure normalization and a possible escape of the maxima to spatial infinity have to be handled in it and are not written out here), by compactness and the uniqueness theorem of Cozzi and Kelliher for bounded velocity and vorticity with canonical pressure, to an
a priori bound: there is Lambda_E(K, C_*) < infinity such that every bounded Lipschitz swirl-free axisymmetric Euler solution on an interval [0, T], T <= K, whose pressure is the canonical one, p = sum_{i,j} R_i R_j (U_i U_j) in BMO modulo functions of time (R_i the Riesz transforms), and with ||U_0|| <= 1, ||grad U_0|| <= 1,
||grad^2 U_0|| <= C_*, satisfies ||U(t)|| + ||grad U(t)|| <= Lambda_E(K, C_*) for 0 <= t <= T (without the pressure condition this fails: U = N t e_Z, p = -N Z solves the Euler equations with U_0 = 0 and ||U(K)|| = N K for every N > 0). Persistence of the Hessian bound itself is false in
general (strong C^2 ill-posedness of Bourgain and Li, after adding a constant axial velocity), but in the Navier-Stokes application (A)
supplies the forward Hessian bound, so only the Lipschitz-level bound is needed. That bound is not available: the global theorems
for this class that we know of assume integrability of the initial data, for example eta_0 in the Lorentz space L^{3,1} (with omega_0 in L^{3,1} and in L^infinity; Danchin), or finite energy together with eta_0 in weak L^3 and a further weighted bound on the vorticity (Shao, Wei and Zhang), and the class-(C) pipe flow U = b e^{-R^2} e_Z has infinite energy and eta_0 = 2b e^{-R^2}, which is
bounded but in no finite L^p(R^3) and not in weak L^3, since it does not depend on Z. The scalar estimates do not close: transport of eta gives ||omega(t)|| <= ||omega(0)|| + sqrt2 C_* int_0^t V,
the low-frequency (Serfati) identity gives V^2 <= C (V(0)^2 + ||omega|| int_0^t V^2), and this system admits finite-time divergent solutions: with c = sqrt2 C_*, V(t) = (1-t)^{-2}, A(t) = int_0^t V = t/(1-t) and ||omega(t)|| = 1 + c A(t) (so ||omega(0)|| = V(0) = 1), both inequalities hold on [0, 1) with C = 4 max(1, 1/c), because C >= 4 and C ||omega(t)|| >= 4/(1-t) reduce the second to 12 s^4 - 4 s^3 + 1 >= 0, s = 1 - t, whose minimum on [0, 1] is 63/64. Even granted the bound, for C_* > 1/2 the statement does not exclude Case 2, since suitable smooth pipe flows are eternal and satisfy the limiting
spatial bounds, and suitable thin vortex rings with velocity of class C^{2,alpha} also do whenever C_* > Q_core, the infimum of the planar core quotients of F2, a range that contains every C_* >= 0.452 by the computer-assisted enclosure Q_40 < 0.45194 of F2 (iv), whose programs are not reproduced here, so that this endpoint cannot be checked from the report (F2; classical Norbury rings have discontinuous vorticity and are not in the class).
An isolated self-propelled vorticity packet couples only weakly to a later record: a vorticity packet of axial impulse I = (1/2) int r^2 eta dx
(I = pi Gamma rho^2 for a thin ring of circulation Gamma and radius rho) at axial distance d induces on the axis the radial strain u^r/r (the axial strain is -2 times it) of absolute value
(3/2)(|I|/(2 pi)) d^{-4} + O(M_1 d^{-5}). Here d is the distance from the evaluation point to a point x_c of the axis, the packet is supported in the ball of radius d/2 about x_c, and M_1 = (1/2) int r^2 |eta| |x - x_c| dx is its absolute first moment about x_c; the remainder comes from the bound O(d^{-5}) for the gradient of the on-axis kernel on that ball. For a packet of one vorticity sign supported within distance rho <= d/2 of x_c, M_1 <= rho |I| and the strain is (3/2)(|I|/(2 pi)) d^{-4} (1 + O(rho/d)); for a packet of both signs there is no such relative bound, since M_1 is not controlled by |I|. For |I| and M_1 bounded independently of nu and T, and an axial distance d comparable to the flight time T (speed of order one), this strain is below
kappa_c ~ nu^{1/3} once T >> nu^{-1/12}. This does not control interactions between actual consecutive records.

R2.2 Axis-silent outer flows (exact construction and evolution identities proved; quadrature values and the resulting break-time coefficient numerical). (a) The swirl-free profile eta = h(R) cos(kZ), h = (1 - beta R^2) e^{-R^2}, k = 1,
beta defined by int K_1(kR) h(R) R^2 dR = 0 (numerically beta = 1.3409501583320) has stream function g(R) cos(kZ) with g = -R^2/8 + O(R^4), hence
identically zero axis strain, while eta is of order one at R ~ 1. Its axis silence is not dynamically persistent, given the numerically evaluated (not certified) value G_2(0) > 0 below: the Euler evolution gives
d_tau eta = -(k/2) sin(2kZ) F with F = R g h' - 2 g h - R g' h, and the axis strain starts to grow at the rate
d_tau a(0, Z) = k^2 cos(2kZ) G_2(0), G_2(0) = k int K_1(2kR) F(R) R^2 dR = 0.0048679 (independent quadrature; max |U| = 0.161).
The rate is quadratic in the amplitude, so for a small threshold silence at the level kappa_c breaks after
tau_b = kappa_c/(k^2 G_2(0)) + O(kappa_c^2) ~ 205 nu^{1/3}
record times for the unscaled profile, with kappa_c = nu^{1/3} (G = C_* = 1). The unscaled profile does not satisfy the Hessian bound with C_* = 1 (u^Z = (2g + R g') cos Z = -(R^2/2) cos Z + O(R^4), so on the axis d_xx u^Z = d_yy u^Z = -cos Z and the Frobenius norm of the Hessian of u^Z there is sqrt2 |cos Z|, with maximum sqrt2); an admissible multiple c U, c <= 2^{-1/2} (smaller if the full Hessian requires it), multiplies the initial strain-growth rate by c^2 and the leading small-threshold term of the break time by c^{-2}. For the unscaled profile and for each fixed admissible c > 0, independent of n, the break time is therefore a vanishing fraction of one cell time 1/kappa_c (no uniformity is asserted for amplitudes c = c_n -> 0). (b) For C_* > 1/2, axis silence and the limiting spatial bounds alone
cannot exclude a nontrivial limit: pipe flows U = W(R) e_Z are steady Euler solutions (constant pressure) in class (C) with max |grad U| = 1 for suitable W (F2), with a = 0
everywhere and eta = -W'(R)/R nonzero, and W_tau = nu (W_RR + W_R/R) gives the Navier-Stokes version. In this range an exclusion of Case 2 must therefore use
further information from the prelimit solution or its history (for example the swirl cells: core swirl, its self-strain, circulation
supply); the examples do not determine which information is necessary.

R2.3 Drift-free quasi-steady sign lemma (proved; narrow scope). Let the source profile of q^2 be frozen in the separable form
Q = Q_0(R) + f(R) alpha(Z) with f >= 0 (f in L^2(R^2 dR), alpha in L^2(dZ)), and let eta_s solve the drift-free equation
d_tau eta_s = nu Delta_5 eta_s + d_Z Q from zero, with stream function phi_s = (-Delta_5)^{-1} eta_s. Then the self-compression
Pi_s(tau) = int d_Z phi_s Q R dx is <= 0 for every tau, provided the background pairing with Q_0 is integrable (it then
vanishes); without that hypothesis the statement holds for the background-subtracted quantity int d_Z phi_s (Q - Q_0) R dx. Proof: d_Z phi_s(tau) = - int_0^tau K_{tau-s} Q ds with
K_sigma = (-Delta_5)^{-1} e^{nu sigma Delta_5} (-d_ZZ), so Pi_s(tau) = -2 pi int_0^tau int int Q R^2 (K_{tau-s} Q) dR dZ ds. The part
Q_0 drops out (K Q_0 = 0, and the Z-integral of K(f alpha) vanishes), and in Fourier variables in Z what remains is
int k^2 |alpha^(k)|^2 int f R^2 (B_{k,sigma} f) dR dk with B_{k,sigma} = (-Delta_{5,k})^{-1} e^{-nu sigma (-Delta_{5,k})}, whose integral
kernel in R is positive (a radial four-dimensional heat kernel damped by e^{-k^2 ...}); with f >= 0 every term is nonnegative.
Scope: one separable one-signed radial profile, frozen source, no drift. The pairing uses the weight R^2 dR, not the measure R^3 dR in which
B is self-adjoint, so the form is not positive definite: for sign-changing radial profiles it can be negative, which gives positive self-compression, though only through the heat factor (at sigma = 0, with the kernel c I_1(k R_<) K_1(k R_>)/(R_< R_>), c > 0, of (k^2 - Delta_4)^{-1} in the measure R^3 dR, the symmetrized kernel of f -> int f R^2 (B_{k,0} f) dR is (c/2) R^2 R'^2 I_1(k R_<) K_1(k R_>) (1/R_< + 1/R_>), a sum of two kernels of the form a(R_<) b(R_>) with a, b > 0 and a/b nondecreasing, each positive semidefinite, so that form is nonnegative for every f; for sigma > 0 the kernel of B_{k,sigma} is bounded near the axis, and a 2 x 2 minor of the symmetrized kernel becomes negative as one of the two points tends to the axis), and for time-dependent
alpha the time-integrated form is not positive definite either, in agreement with the periodic counterexample F10 (c) of Section 3. In the energy
weight R^2 dx (pairing in R^3 dR) the form is nonnegative for every frozen profile, one-signed or not, because K_sigma is a positive
operator there; that weight is not the critical one. The lemma does not imply (SC).

R2.4 Coupled unforced numerical experiments (numerical, evidence only). The exact unforced axisymmetric Navier-Stokes system for
(Gamma, eta) was integrated in record units with the whole-space five-dimensional Biot-Savart law (no body force, no prescribed
reservoir), for nu between 1e-2 and 1e-3 and cell Reynolds numbers G between 1 and 30. Families: isolated
axially modulated swirl filaments at the cap radius; prepared trains of cells phased to compress the core (initial compression 3 kappa_c,
0.56 of the critical rate); a filament compressed by a passing swirl-free ring; a Rayleigh-unstable swirl shell; a filament inside the
axis-silent outer flow of R2.2(a). In every run the cumulative self-compression int Pi_s was negative at the sampled times; the cumulative production was
between 1e-3 and 5e-3 of the critical budget in the other families and 8e-3 with the silent outer flow; the prepared trains dispersed with an e-folding time
of about 0.15 cell times; the ring gave 0.07 of the critical rate for about one cell time, through its own (external) strain, while the
self-compression stayed negative. Resolution, viscosity, wavelength and G scans changed none of these signs. Negative cumulative signed work at the
sampled times does not bound the positive part of the self-compression or the weighted work of Theorem 9 (d). An independent review found
two discretization defects (the five-dimensional mass of the axis cell and a ghost-cell mismatch for the stream function); after
correction the results changed by less than 3 percent. Not yet tested over long times: a core inside a record-scale axial jet, and an
outer flow organized at the cell scale. These signs concern localized filaments at G <= 30; on a modulated Oseen column at G = 1000 the accumulated self-compression
changes sign and is positive, of the order of the production, at the first inertial time (numerical, R2.13 (a)).

R2.5 The core inside the record-scale axial jet (identity and one sign proved; the rest numerical, linear, frozen base). In cell units
(length delta, velocity nu/delta, viscosity 1) the Hessian bound of (A) reads |grad^2 U| <= G, and a pipe-like record flow W_0 - b R^2 near
the axis has curvature b_cell = b G/C_*; its Cartesian Hessian has Frobenius norm 2 sqrt2 |b|, so (A) allows the jet alone |b_cell| <= G/(2 sqrt2) = 0.354 G (joint admissibility with the core is stated next):
the axial shear across the core is of the same order as the swirl, so the drift-free results above do not apply to it. The base core used
below, Gamma_0 = G(1 - e^{-R^2}), has maximal Hessian 1.495 G, so it is the admissible core for the constant 1.495 C_* (equivalently, the
admissible core of radius 1.495^{1/3} delta = 1.1434 delta). Core and jet share one Hessian budget, and their Hessians have orthogonal components, so a core
enlarged by the factor lambda together with the jet satisfies the local Hessian constraint exactly when (C_O/lambda^3)^2 + 8 (b_cell/G)^2 <= 1, C_O the exact normalized core Hessian maximum (numerically 1.495; with a certified upper bound in place of C_O the condition is sufficient). This concerns the Hessian constraint only, not global class (C) admissibility of an unbounded quadratic jet (at
the jet limit b_cell = G/(2 sqrt2), about 0.354 G, the unscaled combined norm is (C_O^2 + 1)^{1/2} G, about 1.80 G). Core radius and jet curvature must therefore be chosen jointly; the scans below
treat them separately, and the effect on their numerical thresholds has not been computed. The quadratic jet is a local model
(W = -b R^2 is unbounded globally).
(a) Identity: for perturbations of a columnar base (Gamma_0(R), W(R) e_Z) with Gamma_0' > 0, the linearized swirl equation is
(d_t + W d_Z) q_1 = Delta_5 q_1 - a_1 Gamma_0'/R, and the second-order self-compression Pi_s^(2) = -2 int a_1 q_0 q_1 r dx equals the
strain part of d/dt F, F = int (Gamma_0/Gamma_0') q_1^2 dx, for a time-independent frozen base, perturbations with finite F (the weight
(e^{R^2} - 1)/(2R) grows fast, so this is a restriction) and boundary conditions that remove the boundary terms, and for every jet profile W (the jet term integrates to zero because W does not
depend on Z). The diffusive part of dF/dt has no sign outside the core (the weight grows like e^{R^2} for a Lamb-Oseen core), so the
identity gives no sign.
(b) For the frozen base Gamma_0 = G(1 - e^{-R^2}), W = -b R^2 the axisymmetric (m = 0) linear spectrum, computed by finite differences in
R with zero flux at the axis, had no unstable eigenvalue at the sampled values of G in [30, 1000] (and G = 10 at k = 0.5, 1, 2), b/G in [0, 0.7] (the jet alone satisfies the Hessian constraint for
b/G <= 1/(2 sqrt2) = 0.354, a jet-only bound, not joint admissibility with the core) and axial wavenumbers
k in [0.05, 5] (a finite scan, not a proof of stability on these ranges); the least damped modes are slow diffusive modes at small k, and the jet increases the damping. Leading eigenvalues agree to
three digits between 240 and 480 radial points and to 3 percent between outer radii 8 and 12. The non-normal transient energy gain is
large at large G (up to about 370 at G = 1000, reached within 1.5 cell times).
(c) Sign of the mean self-compression of forced waves. Force the swirl equation by the axis strain of an outer poloidal flow whose
vorticity lies away from the core, a_ext = A (2 I_1(kR)/(kR)) cos(kZ + omega t) (A = 1 is an oscillation of amplitude kappa_c), and
average over Z and t. Without jet (b = 0) the vorticity response is the retarded diffusive response to the source d_Z(2 q_0 q_1), so the
self-strain is a_1 = K(omega) f with f = 2 q_0 q_1 and K(omega) = k^2 A_k^{-1}(i omega + A_k)^{-1}, A_k = -Delta_{5,k} self-adjoint in
L^2(R^3 dR). Its Hermitian part in that space is k^2 (A_k^2 + omega^2)^{-1} >= 0, hence the energy-weighted mean self-compression
-int a_1 q_0 q_1 R^2 dx is <= 0 for every frequency and every profile (proved). In the weight of Theorem 9 (R dx) the pairing is <K f, R^{-1} f>, which has no sign when f changes sign, and the coupled
response does change sign: numerically the mean Sigma-weighted self-compression of the forced response is positive near the core's
m = 0 inertial-wave frequencies (|omega| about 0.3 G k) for G >= 300 already at b = 0, and at G = 100 with a weak jet (b/G = 0.03 to 0.1),
while it is negative at G = 10 and 30 and for b/G >= 0.2. The energy-weighted quantity was negative in every computed case (proved for b = 0; numerical for b != 0).
The positive value at G = 300, k = 1, b = 0 was reproduced by an independent check with two other discretizations (finite volumes with
exact cell masses up to 2560 cells, and Chebyshev collocation up to degree 144): 2.355e-3 Sigma_0 per unit squared axis-strain amplitude,
identical at outer radii 8 and 12 once normalized by the infinite-domain Sigma_0. That check also gave an explicit analytic family
without sign in the Sigma weight: phi = chi(R) e^{icR} with c < 0 and real chi of compact support, f = k^{-2}(A_k + i omega) A_k phi,
so that K f = phi and Re <phi, f>_{R^2 dR} = k^{-2}(Re <phi, A_k^2 phi>_{R^2 dR} + omega c int R chi^2 dR) < 0 for large omega > 0.
So a universal linear-response sign inequality in the critical weight is false beyond the one-signed scope of R2.3 (a sign estimate under additional restrictions on the dynamically realized profiles is not excluded); the weight in
which the sign holds belongs to the swirl kinetic energy, which is not critical.
(d) Size (linear, frozen base). Normalize by the infinite-domain value Sigma_0 = int q_0^2 R dx = 2 pi sqrt(pi)(2 - sqrt2) G^2 per unit
length (1.038 G^2 after dropping 2 pi). The freely diffusing core q = G(1 - e^{-R^2/(1+4t)})/R^2 has Sigma(t) = Sigma_0 (1+4t)^{-1/2}
exactly, so Sigma'(0) = -2 Sigma_0 and, by the balance Sigma' = -(diffusion) + 3 Pi, balancing the initial dissipation of the reference profile needs a mean total compression
Pi = (2/3) Sigma_0 (the critical order of Theorem 9(e) in cell units); this is a benchmark: in general maintenance on a domain without boundary flux requires 3 <Pi> = <D_Sigma>, and the dissipation of a modulated core need not stay 2 Sigma_0. The linear forced responses reach this order only at large
amplitude when the compression is done by the core's own response: at G = 300, k = 1, b = 0 and the frequency maximizing the
self-compression, the self part is 2.35e-3 Sigma_0 and the direct part of the outer strain 2.37e-3 Sigma_0 per unit squared axis-strain
amplitude, with relative swirl modulation 0.10 per unit amplitude, so linear extrapolation gives maintenance at modulation about 1.19 using the self and direct parts together (about 1.68 with the
self part alone), both outside small-modulation linear theory;
for an outer strain profile localized on the core (e^{-R^2/4}), maximizing the total over the frequency, the extrapolated modulation is 1.2
to 1.5 for G in {100, 300, 1000} and k in {0.5, 1, 2}. An unrestricted amplitude bound is false: for the harmonic outer profile at low
frequency the total reaches the critical order at modulation 0.01 to 0.04 (G = 100 to 1000, k = 1), but there the self part is negative,
the compression is done by the outer strain on the outer skirt of the core (R between 2 and 6 cell radii, where the rotational stiffness is
weak and the harmonic strain has grown by the factor 2 I_1(kR)/(kR), 2.6 at R = 3), and for the localized profile the same quasi-steady
response cancels to three digits (self part = -direct part), so that, taking the residual at face value (no error estimate for it was made), maintenance would need an axis strain of order 10 G,
outside (A).
So among the tested frozen profiles and frequencies the critical order is reached at small modulation only by compression from an
outer strain, which in Case 2 must itself be sourced
(the axial strain of the data part of the vorticity is o(delta_n) on the axis, R2.18 (b), hence negligible where the total axial strain is of order delta_n or larger). Whether a saturated, resonantly forced wave field, or a sourced outer strain, can maintain the core is a
nonlinear question; no sustained maintenance was observed for the prescribed outer-strain forcing tested in R2.8, while the prescribed-jet runs of R2.12 (i) show finite-time amplification and positive accumulated self-compression; neither establishes band-length maintenance or its exclusion, and the sourced version is open. Not covered: other jet
profiles, nonaxisymmetric modes, and a base core held by compressive strain.

R2.6 Two further approaches give no contradiction (proved identities, negative conclusions). (a) Casimir-adjoint identity resolved by
circulation level: for f smooth and the band adjoint Psi = R^2 chi (chi the backward adjoint of Section 2.6, -d_tau chi - div_5(U chi) = nu Delta_5 chi,
so Psi is a constant multiple of the window adjoint psi there; the identity is linear in Psi), with gamma = Gamma_hat/(nu G), where Gamma_hat = R U_n^theta = nu Gamma is the circulation in record units (Gamma the physical circulation, |Gamma| <= G, so |gamma| <= 1),
d/dtau int eta f(gamma) Psi dy = nu int eta [2 f'(gamma) L gamma Psi + f''(gamma) |grad gamma|^2 Psi + 2 f'(gamma) grad gamma . grad Psi] dy -
nu^2 G^2 int R^{-4} K_f(gamma) d_Z Psi dy, K_f(s) = int_0^s 2 t f(t) dt, which splits the production by circulation level. The viscous level
diffusion obeys, for nonnegative terminal adjoint data (so Psi >= 0, the adjoint flow preserving positivity) and vanishing boundary terms, 2 nu int int |grad gamma|^2 Psi <= int gamma^2 Psi(start) + 4 nu int int gamma^2 |d_R Psi|/R, an upper bound whose size depends on the band
geometry, its duration and the normalization of chi; it supplies no smallness of the level diffusion, so no contradiction (and no lower
bound is claimed). (b) Swirl work and impulse: in a fixed record-scale
cylinder and over a band of duration O(1/nu) the spatial bounds give the absolute bound O(nu G^2 (1 + log(1/delta))) -> 0 for the work
done by the swirl on the meridional field (this does not extend by itself to the whole prelimit history); these bounds do not quantify the energy supplied by the larger-scale meridional flow. The
sourced vorticity carries no conserved impulse of its own: d/dt int r^2 eta_s dx = 2 int r u^r eta_s dx, whose self-transport part
vanishes while transport by the remaining poloidal field exchanges impulse between the two components; only the total impulse is
conserved (when the impulse moments are finite and boundary terms vanish). Neither gives an upper bound on the self-compression.

R2.7 Tools for the cell dynamics (proved unless stated; checked by hand except where (c) states a computer-algebra check; none excludes Case 2). Cell units (length delta, viscosity
1) except in (d); dX = r^3 dr dz is the five-dimensional measure in which Delta_5 is self-adjoint.
(a) Conservative coupling (identity). Linearize about a columnar swirl q_0 = Gamma_0(R)/R^2 with no meridional flow:
q_1' = Delta_5 q_1 + (Gamma_0'/R) phi_{1,Z}, eta_1' = Delta_5 eta_1 + 2 q_0 d_Z q_1, -Delta_5 phi_1 = eta_1. If Gamma_0 Gamma_0' > 0 put
w = 2 Gamma_0/(R Gamma_0') and E = (1/2) int w q_1^2 dX + (1/2) int eta_1 phi_1 dX. The two coupling terms cancel in dE/dt (integration by
parts in Z), so without viscosity E is conserved; with viscosity the weight produces the term (1/2) int (w'' + 3 w'/R) q_1^2 dX, of no sign
for a frozen weight. For the Lamb-Oseen core w = (e^x - 1)/x, x = R^2/(4s).
(b) Linear decay on the freely diffusing Oseen column (a priori estimate for classical, Gaussian-localized solutions of the exact
linearization, axial wavenumber k != 0). With the evolving weight of (a), the identities Delta_5 w + w_t = w/s and
int w |q'|^2 dX = int w |q' + R q/(2s)|^2 dX + s^{-1} int (w + 1) |q|^2 dX give E' <= -2 k^2 E: every axial mode of the coupled
(swirl modulation, meridional cell) perturbation has E(t) <= e^{-2 k^2 t} E(0) (so sqrt E decays at least like e^{-k^2 t}), with no dependence on the circulation.
(c) The same balance on the Burgers column (steady strain U = -(a/2) R e_R + a Z e_Z, k(t) = k_0 e^{-at}; E is the energy of the Fourier
amplitude, that is, per unit physical axial length):
E' = -int w (|q'|^2 + k^2 |q|^2) dX + (a/2) Q - ||eta||^2 - (3a/2) int |phi'|^2 dX, Q = int w |q|^2 dX, w = (e^x - 1)/x, x = a R^2/4.
The term (a/2) Q is absorbed for every k: from x w_x = (x - 1) w + 1 one gets (w R^4)_R = R^3 (2 x w + 2 w + 2), and integrating the cross
term by parts gives int w |q'|^2 dX = int w |q' + (a/2) R q|^2 dX + a Q + a int |q|^2 dX (checked by hand). Hence
E' = -int w |q' + (a/2) R q|^2 dX - (k^2 + a/2) Q - a int |q|^2 dX - ||eta||^2 - (3a/2) int |phi'|^2 dX <= 0 for every wavenumber and
every circulation, and E' <= -2 k(t)^2 E. Since k(t) -> 0 this alone gives no decay to zero; if the initial cells also have finite
homogeneous H^{-1} norm (eta(0) in the radial space H^{-1}(R^4)), decay of the energy like e^{-a t} with a G-dependent prefactor is expected, but the estimate deriving it from this hypothesis is not written out here and the decay is not used. Not covered: a change of the total circulation
(infinite Q; the neutral k = 0 direction), and transient transfer from swirl to meridional energy, which does occur (so the inequalities say only that the energy E of a linear cell on the Burgers column never increases; they do not give decay to zero and say nothing about transient compression). Hypotheses for (a) and (c): a > 0 in (c), finite displayed weighted energies and dissipations, regularity at the axis and vanishing radial and axial integration-by-parts fluxes (bounded fields in class (C) alone do not guarantee the exponentially weighted integrals). In the first identity the strain acting on the meridional energy gives -(3a/2) int |phi'|^2 dX - a k^2 int |phi|^2 dX, and the second term is cancelled exactly by the time dependence of k(t) in the Green's function of E (d/dt of (1/2) <eta, (k(t)^2 - Delta_4)^{-1} eta> contributes + a k^2 ||phi||^2); with k frozen this cancellation is missed. The first identity of (c) was checked by computer algebra and later re-derived by hand in an independent check; the completed square was checked by hand.
(d) Depletion ahead of a persistent compression (record units, (A) through the caps |q| <= 2 G kappa_c and |Gamma| <= nu G and the Hessian bound). Along a
meridional path X(tau) with local compression a = -U^R/R, |Gamma(X(tau_0), tau_0)| <= nu G min{1, 2 (R(tau_0)/delta)^2 exp(-2 int a ds)} +
sqrt3 nu C_* int_{tau_0}^{tau_1} R(s) ds (because L Gamma = R (Delta U)^theta exactly). So for a path that stays within the core radius (R <= delta) of
the controlled segment and has compression a >= a_0 > 0 along it for a time h, |Gamma(X(tau_0), tau_0)| <= 2 nu G e^{-2 a_0 h} +
sqrt3 nu C_* delta/a_0, which is O(kappa_c/a_0) nu G once h >= log(1/kappa_c)/a_0 (C_* delta = G kappa_c). Compression on the axis of a
fixed Eulerian segment alone does not give this: paths may leave the segment, and axis compression does not bound the compression
across the core.
(e) Stretched axis segments cannot hold circulation (a proposed comparison estimate, not established: the implication below is unproved, see Status). If |grad^2 u| <= H, d_z u^z(0, z, t) >= gamma on |z - Z(t)| < l_z for t in
[t_1, t_2], 0 <= Gamma <= G on the cylinder of radius rho_* = min(gamma/(4H), l_z/2), Gamma(rho_*, z, t) >= m there, and
gamma (t_2 - t_1) >= 2 log(1 + gamma rho_*^2/8), gamma l_z^2 >= max(4, 16 log(4 gamma (t_2 - t_1))), then q(0, Z(t_2), t_2) >= e^{-2} m gamma/8,
hence (axis cap q(0) <= (27/16)^{1/3} (G H^2)^{1/3}) m <= 70.4 G^{1/3} H^{2/3}/gamma. Status: a conditional comparison claim. The intended proof is
an explicit Burgers-type radial subsolution times the first even Dirichlet eigenfunction of the strained segment, and comparison; the
subsolution for the actual moving-cylinder drift (which needs a specified relation between Z'(t) and u^z(0, Z(t), t)) has not been
verified, so the axis lower bound is not established. If it holds, the circulation estimate follows with the constant
8 e^2 (27/16)^{1/3} = 70.3764. The nonnegativity of Gamma is needed. This
constrains sustained one-signed stretching only, not an oscillating strain.
(f) Fill-in of hollow cores (a proposed heat-kernel estimate with incomplete hypotheses and no proof supplied; it would rest on a lower bound for the Dirichlet Green function of
parabolic equations with bounded drift, and the geometry, norms and buffer it needs are not specified here). If q >= 0 on a moving cylinder of size Lambda rho around the axis over a time Lambda^2 rho^2, then q on the axis is at least
c_0 exp(-C_0 (1 + P)^2) exp(-2 K_+) times the mean of q over the annulus rho < r < 2 rho three diffusion times earlier, with P the Peclet number
of the drift relative to the axis velocity and K_+ the time integral of the positive part of the stretching. A uniform fill-in conclusion (a hollow
core filling within three cell times on quiet axis segments) needs in addition uniform bounds on P and K_+.
(g) Drift-free sign for time-dependent one-signed profiles. In the drift-free model with q^2 = Q_0(R, t) + f(R) alpha(Z, t), eta_s from zero
by d_t eta_s = Delta_5 eta_s + d_Z(q^2), the time integral of the Sigma-weighted self-compression is
W(T) = -(1/2) int dk k^2 int_0^T int_0^T Re[alpha^(k, s) conj(alpha^(k, t))] G_k(|t - s|) ds dt, G_k(tau) = <R^{-1} f, L_k^{-1} e^{-tau L_k} f>_{dX},
L_k = -d_RR - (3/R) d_R + k^2. If f >= 0 is radially nonincreasing then W(T) <= 0 for every T and every alpha (under decay and integrability of f and alpha sufficient for the transforms and integrations by parts used; the Z-independent part Q_0 pairs to zero with the Z-mean-free sourced flow when that pairing is integrable, and is otherwise background-subtracted as in R2.3). Proof: g_k = -G_k' equals
e^{-k^2 tau} (2 pi^2)^{-1} int_{R^4} (f/|x|) (e^{tau Delta_4} f) dx; the heat flow keeps f radial and nonincreasing, and with phi = f/R (nonincreasing)
d/dtau int phi e^{tau Delta_4} f = -int phi' d_R(e^{tau Delta_4} f) |S^3| R^3 dR <= 0, so g_k is nonnegative and nonincreasing, its sine
transform is nonnegative, hence the cosine transform of G_k (equal to 2 <R^{-1} f, (L_k^2 + omega^2)^{-1} f>) is nonnegative and G_k(|.|) is
positive definite. So neither time modulation nor travelling renewal of a fixed solid profile produces critical self-compression in this
model; what is not covered is a modulation whose radial shape changes sign, which includes a radially varying phase
(Re[F(R) e^{i(kZ + omega t)}] with complex F), and that is the form of the resonant forced response of R2.5(c). Numerically the same sign
held for the selected one-signed profiles tested and for Burgers profiles whose compression oscillates in time by up to 90 percent;
the two-ring computation of R2.9 (c)(ii) gives numerical evidence that one-signedness alone is not sufficient (its nonnegative, radially non-monotone profile gives the opposite sign numerically; a certified enclosure is not supplied).
(h) Energy weight with transport (identity). For eta_s(0) = 0 and under integrability hypotheses, int_0^T (-int a_s q^2 r^2 dx) dt
= -2 pi [(1/2) int |grad phi_s(T)|^2 dX + int_0^T int eta_s^2 dX dt + int_0^T int phi_s b_r . grad eta_s dX dt], with b_r the meridional
velocity not sourced by the swirl: the self-transport does no work because div_5(phi b(phi)) = 0 pointwise. The energy weight is not the
critical one, and comparing it with the Sigma weight through the single factor R ~ delta fails by a power of M_n along every Case 2 sequence.
(i) Reading (a synthesis, not a theorem). A saturated core of radius about delta persisting for a time of order 1/nu in record units,
with axial modulation of q^2 of relative size one at the scale delta, is one conditional scenario compatible with the production budget
of Section 1 (a scale count); neither this geometry nor the order-one modulation has been proved necessary. In that scenario a Z-uniform
compression holds radius delta only at rate 2 kappa_c (Gaussian profile, exact), (d) limits strong compression along paths that stay in
the core, and of the tools above (b) proves linear decay of the cell energy on the Oseen column, (c) supplies energy inequalities on the Burgers column, (g) supplies a sign of the cumulative work for a prescribed modulation (it does not show that the modulation decays), and the coupled runs show decay for their tested data; they do not establish
nonlinear no-regeneration or a universal depletion threshold, and positive self-compression does occur in other settings (proved in the drift-free prescribed-swirl model of F10 (c) and Appendix B, numerical in R2.9 (c) and R2.13 (a)). The remaining gap is the first missing implication stated at the top.

R2.8 No sustained maintenance of a resonantly forced cell core was observed in the tested runs (numerical, model statement). Cell units; axisymmetric Navier-Stokes for the
swirl and the self-induced meridional flow, axially periodic (period 2 pi), radial domain (0, 8); Lamb-Oseen core G = 300 diffusing freely;
prescribed zero-mean forcing by the outer axis strain A e^{-R^2/4} cos(Z + omega t), A in {1, 3, 10, 30} (A in units of kappa_c), omega in
{-90, -159} (the frequencies maximizing the linear response). Exact budget (with q = 0 at the outer radius R = 8; otherwise the boundary flux int [2 R^2 q q_R + R q^2 - R^2 u^R q^2]_{R=8} dZ is added): dSigma/dt = -D + 3 Pi, D = 2 int |grad q|^2 r^2 dr dz +
int q^2 dr dz >= 0 (per period, 2 pi dropped), Pi the total compression; for the whole-space Oseen benchmark with s_0 = 1/4, D = 2 Sigma at t = 0,
q(0, 1) = 0.2 G and the core R < 1.5 keeps 0.0889873 of its Sigma at t = 1 (on the computational domain truncation and the boundary
condition modify these values). Results (Fourier
in Z with dealiasing, second-order finite volumes in R, integrating-factor Runge-Kutta, validated against the linear response at small A
and against exact free diffusion at A = 0; at A = 10, omega = -90 the integrated quantities over the first quarter cell time change by
less than 0.5 per cent under a 1.5-fold radial and 2-fold axial refinement and not at all under a smaller time step; the A = 30 run was
not refined): Sigma/Sigma_unforced <= 1.03 for A <= 10 and <= 1.06 at A = 30 (axis-strain amplitude 30 kappa_c, which is 0.1 G in cell units; joint admissibility of the prescribed forcing and the core has not
been established); dSigma/dt/Sigma stays close to the free-diffusion value in every window up to one cell time (within 0.1 with the window means
first computed; with the revised largest compression input quoted below the difference in that window is 0.13, so a uniform 0.1 bound is
not established). Two mechanisms are
measured. Dissipative compensation: the compression input 3 Pi/Sigma reaches 1.10 (1.07 with the coarser sampling; about half of the initial free-diffusion value 2; maintenance would need it to match the
contemporaneous D/Sigma), but D/Sigma rises from 1.62 to
2.59 in the same window, because the axial modulation through which a zero-mean strain does net work dissipates. Sign reversal: the
self part of the compression is positive only during the first quarter cell time at A = 10, omega = -90 (0.05 Sigma), and at relative
modulation of order one it is negative and grows with the amplitude (-0.13 Sigma at A = 10, omega = -159; -0.24 Sigma at A = 30). All
compression of order 0.1 Sigma is done by the prescribed outer strain. The window means were confirmed by reruns sampled every 0.001
cell times (agreement within 0.013 for A <= 10, except the largest compression input, 1.10 instead of 1.07). The total Sigma hides a
redistribution towards the axis: the Sigma inside R < 1.5 is 1.15 (A = 3) and 1.34 to 1.36 (A = 10) times the unforced value at one
cell time, and the axis value of q is 0.25 to 0.32 G against a computed unforced value 0.205 G, 2.5 per cent above the whole-space benchmark 0.2 G (with a zero outer condition on q the comparison principle bounds the unforced axis value by 0.2 G, so the excess is a discretization or setup effect that was not traced); but the core still loses 88 to 90 per cent of its Sigma in that
time (91 per cent unforced), so a prescribed strain slows the decay of the core and does not stop it. Not covered: other wavenumbers
and forcing profiles, G other than 300, a strain sourced by swirl elsewhere (the Case 2 situation: the axial strain of the data part of the vorticity is o(delta_n) on the axis, R2.18 (b), while exterior sourced vorticity is not excluded as a cell-scale drive), nonaxisymmetric modes.

R2.9 No sustained maintenance of a cell core strained only by swirl was observed in the tested runs (numerical, model statement), and
the computations give evidence against a universal sign law for the self-compression. (a) Model: the system of R2.8 with no forcing; a Lamb-Oseen core G = 300 plus a coaxial outer swirl whose circulation is
G2 (1 - e^{-R^2/r0^2}) + eps G2 (1 - e^{-R^2}) e^{-(R - r0)^2/w^2} cos Z (monotone in R on average, no initial meridional flow), with
(G2, r0, w) = (160, 2.5, 0.8) and (300, 2, 0.7), eps from 0.15 to 0.9, run for one cell time and compared with eps = 0 (then the flow
stays Z-independent). All strain at the core is produced by swirl, mainly by the axial modulation of the outer component. The
data are locally Rayleigh-stable (circulation nondecreasing in R) for eps below 0.195998 (first configuration) and 0.209093 (second), so
eps = 0.2 is Rayleigh-stable only in the second configuration and marginally non-monotone in the first, where it is reported together with the
stable runs below but is not Rayleigh-stable; for eps >= 0.5 they are locally Rayleigh-unstable.
(b) Results (core quantities restricted to R < 1.5). No maintenance: at one cell time the axis value of q is at or below the
unmodulated value (by up to 5 per cent) and the core Sigma is 0.92 to 0.997 of it; in no run does the core Sigma rise more than 2.9 per
cent above its initial ratio to the unmodulated value. Compression at the critical rate occurs only for the Rayleigh-unstable data at
the larger annulus circulation, and only as a burst: at eps = 0.9 the time integral of 3 Pi_core/Sigma_core over the first tenth of a
cell time is 0.33, close to the logarithmic loss of the unmodulated core in the same time (0.35), and the axis value reaches 2.27 times the
unmodulated one at t = 0.05; the burst consumes the modulation (below 0.1 G at a quarter cell time in every run), the dissipation D/Sigma
is 1.6 times the unmodulated value during it (1.23 times at eps = 0.5), and the core Sigma is 13 per cent below the unmodulated value at a quarter cell time. For
Rayleigh-stable data the time integral of 3 Pi_core/Sigma_core over a quarter cell time is at most 0.03, against the logarithmic loss 0.76 of
the unmodulated core over that time (a benchmark, not a closed maintenance criterion: the restricted core also changes its dissipation and
its radial boundary flux). The total self-compression Pi_s of all swirl oscillates with the inertial period of the annulus (about 0.02 to
0.03 cell times) and changes sign within each period; its time mean over the first tenth of a cell time is positive in every run at the
larger annulus circulation, including the Rayleigh-stable ones (+0.001 to +0.030 Sigma), and negative at the smaller one (-0.003 to
-0.074 Sigma). All time means quoted here use values every 0.001 cell times (doubling the interval changes the mean of Pi_s/Sigma by at
most 0.003 and the other means by less than 0.5 per cent); means formed from values every 0.01, reported earlier, overstated the mean
of Pi_s/Sigma by up to a factor 5. Numerics as in R2.8; the strongest case changes by at most about 1.5 per cent under
a 1.5-fold radial and 2-fold axial refinement. The condition q = 0 at the outer radius R = 8, where the outer swirl has circulation G2,
creates a centrifugally unstable wall layer, which acts as a boundary forcing; it grows only after half a cell time and carries less
than 1e-3 of the fluctuation energy inside R < 1.5, so the core quantities are used to one cell time and the totals to half a cell time; no domain-enlargement test or estimate of
the induced core strain was made, so these remain observations for the finite-domain problem.
(c) No sign law. The following construction and numerical tests, of different status (stated in each), indicate that the self-compression is not sign-definite outside the fixed-shape class of R2.7(g); they are not three self-contained certified counterexamples.
(i) Pointwise in time (a construction checked here but not written out, so for the reader it is an unverified report, not used as a proved fact): a narrow intense swirl at one axial position plus a broad weak swirl
at another has Pi_s > 0 (the broad swirl is compressed by the strain of the narrow one). (ii) Cumulatively, in the drift-free model of
R2.7(g) with a fixed nonnegative but radially non-monotone profile (two thin rings at radii 1e-5 and 6, masses 7e-5 and 1 in R^3 dR,
k = 1/10, omega = 1): the quadratic form <R^{-1} f, (L_k^2 + omega^2)^{-1} f> evaluates numerically to -0.0011997 for point rings (independently recomputed as -0.00119974193, and again here at 50 digits), with no certified error bound (a smoothed-ring interval enclosure was also computed, but its smoothing specification is not recorded, so it is not used). If this sign is certified, then, since the kernel H below is continuous for R, S > 0 (including the diagonal), sufficiently narrow smooth rings keep it, and a modulation alpha = v(Z) cos t with v-hat concentrated near k = 1/10 does cumulative self-compression at a positive rate; as it stands this is numerical evidence. The kernel was checked by hand: H(R, S) = -omega^{-1} Im[I_1(m min(R,S)) K_1(m max(R,S))
/(R S)], m^2 = k^2 + i omega, Re m > 0. (iii) For two nonincreasing profiles with independent
modulations (f_i = e^{-R^2/(2 sigma_i^2)} with sigma_1 = 0.3 and sigma_2 = 4, k = 0.1, omega = 0) the 2 x 2 matrix version of the kernel has a
negative eigenvalue after symmetrization and normalization to unit diagonal (-0.148342; numerical, two
independent computations), i.e. a weak broad swirl in antiphase with the narrow core is compressed
cumulatively. The positive transients of Pi_s in the runs of (b) are consistent with these mechanisms; no decomposition establishing that attribution is supplied.
(d) Reading. In the tested runs, as in R2.8, the work that would maintain a core is done by an axial modulation that dissipates and is
consumed within a fraction of a cell time, and the reported net effect on the core is a loss. One possible proof strategy would seek to bound, over each renewal
cycle, the compression work by the extra dissipation and radial exchange of the modulation that produces it; no such inequality is known, and its necessity and sufficiency for excluding Case 2 are not established.
Not covered: renewal of the modulation (the periodic box cannot test supply), other annulus shapes, wavenumbers and circulations,
nonaxisymmetric modes.

R2.10 An energy-Casimir budget for a cell core on the free and on the uniformly strained column (proved; a budget, not an exclusion).
Every identity below was checked by hand; the
numerical diagnostics of (f) check consistency with the dissipative inequality, not closure of the exact radial term. Cell units (length delta, viscosity 1). Gamma = R u^theta, b = (u^R, u^Z), eta = omega^theta/R,
-Delta_5 psi = eta, u^R = -R psi_Z, u^Z = 2 psi + R psi_R, dx = 2 pi R dR dZ; the equations are Gamma_t + b.grad Gamma = L Gamma with
L = d_RR - R^{-1} d_R + d_ZZ, and b_t + b.grad b + grad p = Delta b + Gamma^2 R^{-3} e_R.
(a) Functional. Reference columns: the Burgers vortex in the uniform strain U^s = -(a/2) R e_R + a Z e_Z, Gamma_B = G (1 - e^{-x}),
x = a R^2/4 (exact and steady), and the Oseen column Gamma_0 = G (1 - e^{-R^2/(4s)}), s = t + t_0, b = 0 (the same profile with a = 1/s);
here G > 0 and t_0 > 0, and the constant Burgers strain a is positive. For a smooth reference Gamma_* with Gamma_*' > 0 for R > 0 and q_* = Gamma_*/R^2 decreasing (both reference columns qualify), define phi_* on the range of Gamma_* by phi_*'(gamma) = -q_*(R_*(gamma)) (R_* the inverse
of Gamma_*; for the two reference columns the extension to negative circulation is given in (b)) and Phi_*(gamma, R) = phi_*(gamma) + gamma^2/(2 R^2). Then Phi_*(., R) is strictly convex with its minimum at Gamma_*(R), with
second derivative m = phi_*'' + R^{-2} > 0. The available potential energy A = int [Phi_*(Gamma, R) - Phi_*(Gamma_*(R), R)] dx is >= 0,
with equality only at Gamma = Gamma_*; K_1 = (1/2) int |b - U^s|^2 dx (K for the Oseen column). Notation: g = Gamma/G,
ell = -log(1 - g), h = (e^ell - 1 - ell)/ell^2, J(ell) = int_0^ell (1 - e^{-s}) e^{-s} s^{-1} ds, M = 1 + x h.
(b) Radial inequality. For every radial profile with 0 <= g <= 1 (monotone or not), g(0) = 0, g -> 1 at infinity and a locally finite
gradient integral, put Delta I[g] = lim_{X -> infinity} int_0^X {[M g_x^2 - J(ell(g))] - [the same at g_B]} dx. Then
  Delta I[g] >= (1/4) int_0^infinity (g - g_B)^2 dx (in the extended reals), with equality, when Delta I[g] is finite, only at g = g_B,
because (g, v) -> M v^2 - J is jointly convex (this reduces to h'' >= 0, to -j''(g) = h >= 1/2 for j(g) = J(ell(g)), derivatives in g, and to h h'' - 2 h'^2 >= 0, the last being
e^{2 ell} ell^{-6} N(ell) for a power series N whose coefficients vanish up to degree 5 and are positive from degree 6 on). The sharp
form also holds: with A_0 the available potential energy per unit axial length (measured with dx = 2 pi R dR),
  pi a G^2 Delta I[g] = a A_0 + pi a G^2 Kc[g],  Kc[g] = int_0^infinity [ M (g_x - (1 - g) ell/x)^2 + x^{-2} int_x^ell 2 s (s - x) e^{-2s} ds ] dx >= 0,
with equality only at g_B. The proof is an exact pointwise calibration: for F(g, v, x) = M v^2 - g^2/(2x),
F = (S_0)_x + (S_0)_g v + M (v - f)^2 + W with S_0 = 2 J + P_ell/x - (2g - g^2), f = (1 - g) ell/x, W = (T - x P_ell)/x^2,
P_ell = (1 - (1 + 2 ell) e^{-2 ell})/2, T = (1 - (1 + 2 ell + 2 ell^2) e^{-2 ell})/2; one checks (S_0)_g = 2 M f, (S_0)_x = -P_ell/x^2 and
d_ell W = 2 ell (ell - x) e^{-2 ell}/x^2, so W(ell, x) - W(x, x) >= 0 with equality only at ell = x; at g_B the square vanishes
(f = g_B'); the boundary terms vanish (S_0 -> 2 log 2 - 1 at infinity for both profiles, S_0 -> 0 at the axis since g^2/x <= int_0^x g_x^2).
The coefficient of a A_0 in this inequality is sharp (profiles 1 - e^{-cx}, c -> 0). Values g = 1, where ell is singular, are read as limits, and the axis term uses finiteness of int_0^x g_x^2 up to the axis. The calibration is pointwise in x, so a radial cutoff costs only a boundary term
proportional to the deviation on the support of the cutoff's derivative. For sign-changing circulation (Gamma <= G) the convex
extension phi(gamma) = -(aG/4) gamma + (a/16) gamma^2 for gamma < 0 keeps the weak form Delta I >= 0; the sharp form is proved only
for 0 <= Gamma <= G.
(c) Exact balances. They hold as a priori identities for classical solutions with axis regularity, finite relative energy and
dissipation, and either axially localized perturbations (background integrals subtracted on axial cutoffs) or perturbations periodic in
the material coordinate Z e^{-at}. Burgers column, with b_1 = b - U^s, D_1 = int eta_1^2 R^2 dx and E~ = e^{-at} (A + K_1):
  dE~/dt = -e^{-at} { D_1 + (3a/2) int (b_1^Z)^2 dx + int m Gamma_Z^2 dx + pi a G^2 int Delta I[g(., Z, t)] dZ };
Oseen column: d(A + K)/dt = -{ D + int m Gamma_Z^2 dx + (pi G^2/s) int Delta I_s[g(., Z, t)] dZ }, Delta I_s being Delta I with a = 1/s.
The centrifugal exchange int (Gamma^2 - Gamma_*^2) b_1^R R^{-3} dx (b_1 = b for the Oseen column; the unsubtracted integral int Gamma^2 b^R R^{-3} dx diverges on the Burgers background) appears with opposite signs in the swirl and in the meridional part and cancels
exactly; the radial terms at each Z combine into the expression of (b). For a spatially uniform strain a(t) >= 0 the balance holds
exactly with the reference G (1 - e^{-kappa R^2/4}), kappa' = a kappa - kappa^2 (an exact solution of the swirl equation), the weight
exp(-int_0^t a) and the radial term pi kappa G^2 int Delta I_kappa dZ.
(d) Consequences and non-claims. The functional is nonincreasing; for each finite T, int_0^T e^{-at} D_1 dt <= E~(0) and
int_0^T e^{-at} int Gamma_Z^2 dx dt <= (8/a) E~(0), with constants independent of G (E~(0) itself depends on G); along the
Z-independent relaxation A_0' <= -a A_0 (Burgers) and (t + t_0) A_0 is nonincreasing (Oseen), both for 0 <= Gamma <= G, where the sharp form of (b) is proved. No nontrivial perturbation with 0 <= Gamma <= G is periodic in time in the stretched frame (Burgers), and no nontrivial perturbation is periodic in time (Oseen). For Burgers put Z' = Z e^{-at} and v = e^{-at} b_1^Z, the axial velocity in the material coordinate. If Gamma, b_1^R and v are periodic in t as functions of (R, Z'), then dx = 2 pi e^{at} R dR dZ' and A >= 0 give E~ >= pi e^{2at} int v^2 R dR dZ', so E~ <= E~(0) forces int v^2 R dR dZ' -> 0, hence v = 0 by periodicity; incompressibility (d_R(R b_1^R) = -R d_Z' v) and axis regularity then give b_1^R = 0, so E~ = e^{-at} A is periodic and nonincreasing, hence constant, and the vanishing of the radial term pi a G^2 int Delta I dZ gives Gamma = Gamma_B by (b). If instead b_1^R and b_1^Z are periodic as functions of (R, Z', t), E~ itself is periodic, hence constant, and the vanishing of (3a/2) int (b_1^Z)^2 dx and of the radial term gives b_1 = 0 and Gamma = Gamma_B in the same way. For the Oseen column, whose reference depends on time, monotonicity alone does not give this; but int_0^infinity D dt <= A(0) + K(0) (D = int eta^2 R^2 dx, the meridional dissipation) forces a time-periodic meridional part to vanish, and then (Gamma - Gamma_0)/R^2 solves the heat equation in five dimensions (four for R, one for Z) with ||(Gamma - Gamma_0)/R^2||_2^2 <= 2 pi A at each time (the norm in five dimensions, or over one axial period; this follows from Phi_*(Gamma, R) - Phi_*(Gamma_*(R), R) >= (Gamma - Gamma_*)^2/(2 R^2), since phi_*'' >= 0), so heat smoothing makes it tend to zero uniformly as t -> infinity and it vanishes if it is periodic. These are weighted L^2 bounds on Gamma_Z only: they do not bound
the centrifugal source d_Z(q^2) = 2 q Gamma_Z/R^2 near the axis; they do not forbid transient creation of meridional motion by a swirl
deviation (zero meridional data with an axially modulated swirl give d_t eta = d_Z(q^2) != 0 at t = 0); and the reservoir E~(0) can
be large. So the statement is a budget, not a no-regeneration theorem.
(e) The record-scale jet. With the parabolic axial flow W = W_0 - b R^2 added (with the Burgers swirl an exact steady solution, the
base pressure containing int_0^R Gamma_B^2 r^{-3} dr), the transport of Gamma by W drops out of the balance and exactly one new term
appears when the perturbation is redefined as b_1 = b - U^s - W e_Z (so that the jet is not part of K_1): dE~/dt acquires + e^{-at} 2 b int R b_1^R b_1^Z dx (integrable under weighted decay of the perturbation, or on axial and radial cutoffs with their fluxes). It cannot be absorbed by the dissipation for any b != 0 on the whole
column: a stream-function test field of size L near the radius L, with the correlation of its radial and axial derivatives of the sign opposite to b (so that the Reynolds-stress term is positive), has a Reynolds-stress term of order |b| L^4 against dissipation of order L and a positive strain term of order L^3 (for psi = F(R/L, Z/L)). It is absorbed for perturbations supported in R <= R_0 when
|b| R_0^2 <= (3a/2)^{1/2} (an instantaneous estimate; viscosity does not preserve compact support). The static parabolic jet alone satisfies the Hessian constraint for |b| <= G/(2 sqrt 2) = 0.354 G in
cell units (R2.5; a jet-only bound, not joint admissibility with the core); the two bounds are stated without comparing their sizes, which depend on G, a and R_0 (the jet bound is the larger one when G R_0^2 >> (3a/2)^{1/2}).
(f) Independent numerical consistency check of (c), Oseen case. A second solver (Fourier in Z with 2/3 dealiasing, second-order flux form in R,
integrating-factor Runge-Kutta) with an independently built Casimir table was run from an axially modulated core (relative modulation
0.5 to 0.9 of the core swirl) with and without initial cells, at G = 30, 300 and 1000. The measured defect -(dE/dt + D + int m Gamma_Z^2)
stayed nonnegative throughout, its ratio to D + int m Gamma_Z^2 being at least 0.0185 at every sample, and E decreased monotonically,
while the self-compression Pi_s changed sign throughout (at G = 1000 between -6.4e7 and +4.7e7 in cell units). These diagnostics check consistency with the dissipative inequality;
they do not quantify closure of the exact radial identity.
(g) What this changes. On the ideal columns the full nonlinear perturbation obeys a closed budget with no smallness assumption, within the stated circulation
range, regularity, finite-relative-energy and boundary hypotheses: regeneration of cell-scale structure at a Case 2 core beyond what its initial reservoir and the time weight allow has to draw
its energy from terms the ideal column lacks (this budget alone does not show that such supply is needed in Case 2): the jet
Reynolds stress of (e); the spatial non-uniformity of the outer strain across the core, which enters at first order in the deviation
(through -2 int Gamma_B (Gamma - Gamma_B) V^R R^{-3} dx, V the difference between the outer flow and U^s), so smallness of the
non-uniformity alone does not absorb it; a uniform strain that takes negative values, where (3a/2) int (b_1^Z)^2 changes sign (R2.15 bounds the growth of the functional on such a strain by exp(3 int a_-), so this channel needs accumulated imposed axial compression; controlling that action along the actual history is open). The last
case includes a fast oscillation of the outer strain about a mean in the admissible window (amplitude and frequency of order one in record
units; a separate, untested possibility: the pumping models of R2.12, R2.14 and R2.18 use strain and frequency of order C_* delta_n in record units, and realization of either history in the record flow is unproved), which a band can contain: averages over a cell time do not bound the pointwise strain, and for (log kappa)' = a - kappa a positive periodic inverse-width
parameter kappa has the same period mean as a (this keeps the mean inverse width, not the time-averaged core profile, since G(1 - e^{-kappa R^2/4}) is strictly concave in kappa for R > 0). Then there is the bookkeeping of a core cut out of the
band: localization fluxes, the size of the initial reservoir, the link from the weighted modulation bound to the signed production, and
the time measure (the Burgers bound is weighted by e^{-at}). Only the link is controlled, and only for perturbations of the free Oseen column under the hypotheses of R2.13 (b): without renewal the production over T cell times is at most C ||phi||_infty G^{3/2} L^{3/4} E~(0)^{1/4} T^{3/4}, which is C' G^2 L T^{3/4} when E~(0) <= C_0 G^2 L (through the pointwise bound |q_Z| <= G from (A) and a split inequality; derived at the end of R2.12 (i) and in R2.13 (b)); with renewal (R2.12 (h) shows that a jet renews the functional) R2.13 (b) replaces E~(0) by E~(0) plus the cumulative positive input into the functional, which is a necessary supply bound and not an exclusion; the same unweighted link has not been derived for the weighted Burgers budget. The rest is not controlled. Literature: inviscid energy-Casimir methods
for swirling flows (Szeri and Holmes, Phil. Trans. R. Soc. A 326 (1988); Wang, Phys. Fluids 21, 084104 (2009), finite pipe, with the same
inverse-profile Casimir), viscous Arnold-type and relative-entropy methods for the planar Oseen vortex (Gallay and Wayne 2005; Gallay
and Sverak, arXiv:2110.13739), small-data stability of Burgers vortices (Gallay and Maekawa, Comm. Math. Phys. 302 (2011)). These contextual
citations do not settle whether the convex radial inequality combined with the exact viscous swirl-meridional cancellation is already in the
literature; novelty is not certified.

R2.11 Mean-fluctuation split of the Sigma budget (identity and a lemma proved by hand; measurements numerical; the conjectured comparison is false as stated). Cell
units, axially periodic cell (period 2 pi), radial domain (0, R_w) with q = 0 at R_w, swirl equation q_t + b.grad q = Delta_5 q - 2 a q,
a = u^R/R; Sigma = int q^2 R^2 dR dZ, dSigma/dt = -D + 3 Pi with D = 2 int |grad q|^2 R^2 + int q^2 >= 0 and Pi the compression work.
(a) Identity. Split q = qbar(R, t) + qtil with qbar the Z-mean. Then Sigma = Sigbar + Sigtil, D = Dbar + Dtil, and
  dSigbar/dt = -Dbar + T,   dSigtil/dt = -Dtil + 3 Pi - T,   T = 2 int R^3 u^R qtil d_R(qbar/R) dR dZ = 2 int R u^R Gtil d_R(qbar/R) dR dZ,
Gtil = R^2 qtil. Proof: the cross terms vanish on Z-averaging; u^R and a have zero Z-mean, so in T = 2 int qbar R^2 N (N the nonlinear
terms) only the parts linear in qtil survive, and for a function f(R), div(R b f) = R u^R f_R, which with f = R qbar converts the transport
part. Integrated, int_0^t T = int_0^t (3 Pi - Dtil) + Sigtil(0) - Sigtil(t). Where qbar/R decreases (every monotone core) the mean
profile gains Sigma from the fluctuations only through an inward mean flux of circulation fluctuation (u^R Gtil < 0).
(b) Initial centrifugal sorting (lemma). If qbar > 0 with d_R(qbar/R) <= 0, qtil(0) = f(R) cos Z with f one-signed and nonzero, and the
initial meridional flow vanishes, then T(t) = t T_1 + O(t^2) with T_1 = 2 pi int R^4 g f d_R(qbar/R) dR <= 0, where (-Delta_5 + 1) g = 2 qbar f
(so g has the strict sign of f by the maximum principle; g is the decaying solution on (0, infinity), or on the bounded radial domain (0, R_w) the solution regular at the axis with g(R_w) = 0 (the impermeable wall for the first axial mode of the stream function, for which the Green's function of -Delta_5 + 1 is positive), which the lemma assumes together with classical regularity up to t = 0; at first order the first Fourier mode is psi_1 = -t g sin Z, u^R_1 = t R g cos Z, while the second harmonic -t h sin 2Z of psi, (-Delta_5 + 4) h = f^2, coming from the term -f^2 sin 2Z of d_Z(q^2), is orthogonal to f cos Z and does not enter T_1; int cos^2 Z dZ = pi over a
period), with T_1 < 0 unless f vanishes almost everywhere on {d_R(qbar/R) < 0}: the first-order meridional flow moves the high-swirl part of the modulation outward.
For radially sign-changing f the quadratic form is not one-signed in general, and the lemma does not extend (see (d)).
(c) Measurements (the solver of R2.8, diagnostics every 0.001 cell times, semi-discrete identities closing to 2.5e-4 Sigma(0) or better).
In all seven unforced runs of R2.9 (both annulus configurations, Rayleigh-stable and locally Rayleigh-unstable modulations) int_0^t T <= 0
at every sampled time up to t = 0.5, its value at t = 0.5 being -0.001 to -0.020 Sigma(0), and Sigbar(t) < Sigbar_ctrl(t) at every sampled t > 0
(the Z-independent run from the same mean data; the largest ratio over t > 0 is 1 - 1.0e-5 in the weakest modulated run
and 1 - 1.3e-3 in the strongest). In the strongest case int_0^{0.5} 3 Pi dt = +0.011 Sigma(0),
Sigtil decreases by 0.035 Sigma(0) and int_0^{0.5} Dtil dt = 0.051 Sigma(0), so that int_0^{0.5} T dt = -0.005 Sigma(0). Inside R < 1.5 the direct transfer is positive (up to 0.27 of
the control core by t = 0.5), but the reshaped mean core diffuses more, and the mean core never exceeds 1.0104 times the control.
Under the prescribed zero-mean strain of R2.8 the transfer is positive (up to 0.18 Sigma(0) by t = 0.5) and the reshaped mean
dissipates 0.17 Sigma(0) of it again.
(d) The mean-field comparison MFC is false as first conjectured. Statement: for the unforced axially periodic problem with Z-independent
mean data qbar(0) > 0, d_R(qbar(0)/R) <= 0, and zero initial meridional flow, Sigbar(t) <= Sigbar_ctrl(t) for all t. Counterexample
(proved by hand from (b), whose first-order computation does not use the sign of f): take qtil(0) = (p - eps n) cos Z with p, n >= 0
smooth, nonzero, of disjoint supports, small enough that q stays positive, and qbar(0) with d_R(qbar/R) = 0 on supp p and
d_R(qbar/R) = -R^{-2} on supp n. With g_p, g_n the solutions of (b) for p and n, T_1 = 2 pi eps (A - eps B), A = int R^2 g_p n dR > 0,
B = int R^2 g_n n dR > 0, so T_1 > 0 for 0 < eps < A/B. Since the meridional flow vanishes at t = 0, qbar and the control differ by
O(t^2), hence so do their dissipations, and Sigbar(t) - Sigbar_ctrl(t) = T_1 t^2/2 + O(t^3) > 0 for small t > 0. A restricted comparison, for example for one-signed f, would need further hypotheses
and is open. Further limits: kinematically such a comparison is false (an exchange of an inner and an outer ring of circulation raises
Sigbar), so a proof must use the available energy of the modulation; Sigma and the energy weight Gamma^2
differently (by a factor R), which is the criticality of the problem; with initial meridional energy the statement fails in general; and in
Case 2 there is no axial period, so a windowed mean has commutator errors of the order of the inverse window length. A valid restricted
comparison would be a quantitative no-regeneration statement in the periodic cell; Case 2 would also need the localization and a supply bound.

R2.12 The core inside a parabolic jet: an exact enhanced-dissipation lemma and the Orr supply of the energy-Casimir functional (Lemma K
proved by hand; Lemma P proved by hand; the sign rule (b) is a leading-order computation for strongly tilted data with slowly varying
envelope and is not universal; the remaining parts contain further identities and estimates, leading-order reductions, numerical observations and heuristic comparisons, each with its status stated). Cell units, axial mode e^{ikZ}, k > 0,
jet W = -b R^2 with b > 0, Delta_5 = d_RR + (3/R) d_R + d_ZZ.
(a) Lemma K (exact Gaussian solutions of the passive jet operator). f = A(t) exp(-alpha(t) R^2) e^{ikZ} solves f_t + W f_Z = Delta_5 f
with A nowhere zero iff alpha' = -4 alpha^2 - i k b and (log A)' = -8 alpha - k^2 (compare the coefficients of R^2 and R^0, using
Delta_5 f = (4 alpha^2 R^2 - 8 alpha - k^2) f). With alpha_inf = (kb/8)^{1/2} (1 - i) (alpha_inf^2 = -i k b/4, Re alpha_inf > 0) and
u(t) = cosh(4 alpha_inf t) + (alpha_0/alpha_inf) sinh(4 alpha_inf t) one has alpha = u'/(4u) and A(t) = A_0 e^{-k^2 t} u(t)^{-2}; for
Re alpha_0 > 0, u never vanishes (J = Re(u' conj(u)) satisfies J' = |u'|^2 because u'' = -4 i k b u, and J(0) = 4 Re alpha_0 > 0),
alpha(t) -> alpha_inf, and |A(t)| = 4 |A_0| |1 + alpha_0/alpha_inf|^{-2} exp(-(k^2 + 2 (2kb)^{1/2}) t) (1 + O(exp(-8 Re(alpha_inf) t))):
the decay rate is k^2 + 2 (2kb)^{1/2}, with a data-dependent prefactor. Moreover
phi_n = L_n^{(1)}(2 alpha_inf R^2) exp(-alpha_inf R^2) (generalized Laguerre polynomials) are eigenfunctions of the radial operator
d_RR + (3/R) d_R - k^2 + i k b R^2 with eigenvalues lambda_n = -k^2 - 8 (n + 1) alpha_inf, Re lambda_n = -k^2 - 2 (n + 1) (2kb)^{1/2}
(substitution reduces this to the Laguerre equation x y'' + (2 - x) y' + n y = 0 at x = 2 alpha_inf R^2): the four-dimensional radial
complex harmonic oscillator. These are the whole spectrum in L^2(R^3 dR) (axis-regular realization): for T = -(d_RR + (3/R) d_R) + k^2 -
i k b R^2 one has Re(e^{i pi/4} <f, T f>) = 2^{-1/2} int (|f'|^2 + k^2 |f|^2 + k b R^2 |f|^2) R^3 dR, so T has compact resolvent, and
writing f = e^{-alpha_inf R^2} y(x), x = 2 alpha_inf R^2, the axis-regular solution of (T - mu) f = 0 is y = M(a(mu), 2, x) (Kummer), which
grows like e^{alpha_inf R^2} unless a(mu) is a nonpositive integer, i.e. unless -mu is one of the lambda_n. (The exact Gaussian evolution is an instance of the non-self-adjoint Mehler formula; Boulton, J. Operator Theory 47 (2002)
413-429.) Checks: the residuals vanish symbolically (n = 0 to 3), and the real parts of the rightmost eigenvalues of a second-order
finite-difference discretization (512 cells, R <= 8, k = 1) are -16.4919, -30.1204 at b = 30, 106 against -(2 (2kb)^{1/2} + k^2) =
-16.4919, -30.1204, the next two agreeing with lambda_1, lambda_2 to three or four digits. Reading: the jet raises the decay rate of an
axial mode at the axis from k^2 to k^2 + 2 (2kb)^{1/2} on the radial scale (kb)^{-1/4} (dimensionally a rate proportional to
(nu k b)^{1/2}, the enhanced-dissipation rate expected for a shear profile with a nondegenerate critical point); the operator is far
from normal, which is the source of transient growth. It is the transport-diffusion part of both the swirl and the vorticity equations.
(b) Sign of the jet term. In the balance of R2.10 (e) the jet contributes RS = 2 b int R u^R u^Z dx. For a meridional stream function
psi_1 = Re(p(R) e^{i(kZ + l R^2)}) one has exactly <u^R u^Z>_Z = -k l R^3 |p|^2 - (k R^2/2) Im(conj(p) p') (the part 2 psi_1 of u^Z does
not correlate with u^R). When the envelope varies slowly against the phase (|l| R >> 1), RS has the sign of -b l, and in the inviscid
approximation the jet shears the phase as l(t) = l_0 + k b t: the jet untilts back-tilted data (b l < 0) with RS > 0, and strongly
forward-tilted data give RS < 0 (the Orr mechanism). The rule is not universal. Counterexample (k = 1): the untilted datum
psi_1 = e^{-R^2} cos Z, eta_1 = (9 - 4 R^2) e^{-R^2} cos Z (its radial amplitude changes sign) has RS(0) = 0 and
dRS/dt(0) = b^2 [(1/2) <B p, H^{-1} B p> - 2 int R^5 p^2 dR] > 0, with p = e^{-R^2}, B = 4 R d_R + 8, H = -d_RR - (3/R) d_R + 1, the
inner product in the weight R^3 dR, and RS normalized as 2 b int R^2 <u^R u^Z>_Z dR. The trial function f = (R^2 - 3/5) p gives
<B p, f> = -1/2 and <f, H f> = 37/80, so <B p, H^{-1} B p> >= 20/37, and with int R^5 p^2 dR = 1/8 the bracket is at least 3/148; numerically
it equals 0.183 (two radial resolutions). So untilted data can feed the functional at first. For the swirl-modulation runs of (d) the
cumulative jet term was negative at every sample; that is an observation about those runs, not a rule.
(c) Passive Orr gain. For a passive vorticity datum A exp(-alpha R^2) e^{ikZ} the meridional kinetic energy is
K = c |A|^2 |alpha|^{-4} I(s), s = Re(1/alpha)/2, I(s) = (1/2)(1/s - k^2 e^{s k^2} E_1(s k^2)) (four-dimensional Fourier transform of a
Gaussian), so with (a) K(t) is explicit. Maximizing K(t)/K(0) over t and the tilt l_0 for data exp(-(1/4 - i l_0) R^2), k = 1: 1.96, 3.79,
8.38, 16.3, 35.8, 73.7, 163 at b = 10, 30, 106, 300, 1000, 3000, 10000 (c = pi/32 for a real mode on the axial period 2 pi; the value
8.38 at b = 106 was reproduced independently from the exact formula: 8.3834 at l_0 = -1.8535, t = 0.01709; between 0.35 and 0.42 times
b^{2/3}, the Orr scaling of plane
Couette flow; optimal tilt growing like b^{1/3}, time of the maximum like b^{-2/3}). Wider data gain more (about 46.7 at b = 106 for data exp(-(0.01 - i l_0) R^2), maximized over t and l_0 in the same way, at l_0 = -0.712,
t = 0.0067; the untilted datum exp(-0.01 R^2) has no gain) because the shear 2bR of the parabolic profile grows with R; the parabolic profile is only the near-axis expansion of the
record-scale flow, so for the core the relevant data sit at R = O(1). This is a size indication, not a bound for the coupled problem.
(d) Coupled runs. On the exact solution formed by the freely diffusing Oseen column G (1 - e^{-R^2/(4s)}), s = 1/4 + t, and the steady
jet (axial pressure gradient -4b), axially periodic (period 2 pi), G = 300 with b in {0, 30, 106} (b = 106 is b/G = 0.35, inside the
drive-only static-curvature range b <= G/(2 sqrt2), about 0.354 G; admissibility of the combined column and jet is not established) and G = 1000 with b = 354, the energy-Casimir functional E of R2.10 was followed with the solver of R2.8 (jet
transport in the exact integrating factor of each Fourier mode). The balance dE/dt + D + int m Gamma_Z^2 - RS <= 0 holds at every sample
except at the first sample (a one-sided difference), the first samples of the most strongly tilted data (at most +0.018 relative for t > 0,
a quadrature effect at radial wavenumber up to 16 that decreases as the data untilt) and below E/E(0) = 1e-4. Results:
  - Untilted swirl modulation (relative amplitude 0.5 and 0.9, no meridional flow): E decreases monotonically and the cumulative jet
    term int_0^t RS is <= 0 at every sample, reaching -0.16 E(0) (b = 30), -0.44 E(0) (b = 106) and -0.52 E(0) (G = 1000, b = 354). The
    core Sigma (R < 1.5) never rises above its initial ratio to the reference column.
  - Back-tilted meridional data eta_1 = B R^2 e^{-R^2} cos(Z - 2 R^2), b = 106: E grows to 3.92 E(0) at t = 0.023 (near the untilting
    time 2/b), the cumulative jet term reaches 3.85 E(0); the same at three times the amplitude (linear regime) and at twice the radial
    resolution (3.95 against 3.92). With b = 30 the cumulative jet term reaches 0.42 E(0) without growth of E; with tilt -4 at b = 106,
    1.16 E(0) without growth; forward or no tilt gives RS < 0. By t = 0.1 the functional is below 2 per cent of E(0) in every tilted run.
  - Back-tilted swirl modulation (tilt -2, amplitude 0.5, b = 106): E grows to 1.05 E(0), cumulative jet term up to 0.44 E(0).
  - Core Sigma against the reference column: meridional data raise it quadratically in the amplitude (by 1.4 per cent at b = 0 and by
    0.7 per cent at b = 106 with tilt -2 for B = 100; by 5.9 per cent for B = 300), back-tilted swirl modulation by 0.8 per cent above the
    initial ratio; untilted swirl modulation leaves it below.
  Resolution: 1.5-fold radial and 2-fold axial refinement of the b = 106 swirl run changes the cumulative jet term from -0.4441 to
  -0.4425 E(0) and the core Sigma by 1e-4 relative.
(e) What this changes. The jet term cannot be absorbed (R2.10 (e)) and now has an explicit witness: no inequality E(t) <= E(0) holds
on the jet-plus-column solution, and any bound must carry a transient factor; the passive Gaussian-family optimizations are consistent with growth of order b^{2/3} for the passive meridional part at fixed
data width over the sampled range (no general gain law is proved), which is of order G^{2/3} in the Case 2 range. In the runs of (d) the supply is transient and is carried by back-tilted data;
in those runs the untilted data were tilted forward and then lost energy to the jet; (b) shows that this is not an unrestricted sign rule. One possible no-regeneration argument through R2.10 would seek a
cycle bound of the form int RS dt <= C b^{2/3} K_in, charging the Orr supply to the meridional energy K_in present at the start of a cycle
(for the coupled operator, not only the passive one), together with a bound on K_in, which must come from the record-scale flow. Neither
is available, and this particular estimate has not been shown necessary or sufficient for the full closing argument. Literature: transient growth and the Orr mechanism in pipe and Couette flows (Schmid and Henningson, Stability and
Transition in Shear Flows, 2001), the pseudospectra of the complex harmonic oscillator (Davies, Proc. R. Soc. Lond. A 455 (1999)), and
enhanced dissipation for shear flows with critical points (Bedrossian and Coti Zelati, Arch. Ration. Mech. Anal. 224 (2017)); Lemma K is
an elementary explicit instance and no novelty is claimed.
(f) The Orr supply is bounded by the enstrophy in the passive problem, and the swirl coupling feeds the enstrophy at the critical rate
(proved by hand). Write ||f||^2 = int f^2 R^3 dR dZ, K = (1/2) <eta, (-Delta_5)^{-1} eta> (the meridional energy up to 2 pi), D = ||eta_1||^2.
Lemma P: for eta_t + W(R, t) eta_Z = Delta_5 eta with any axial profile and any time dependence, axial wavenumbers >= k, and RS defined by
dK/dt = -D + RS (for W = -b R^2, RS = 2 b int R^2 u^R u^Z dR dZ), and no axial mean mode, one has
int_0^t RS dt <= ||eta(0)||^2/(2 k^2) - K(0) for all t; the upper bound and the sharpness of the constant 1/2 (by escaping packets) are proved below. Proof: Delta_5 is self-adjoint and nonpositive in
the weight R^3 and W d_Z is antisymmetric, so dD/dt = -2 Q with Q = int |grad eta|^2 R^3 dR dZ >= k^2 D; hence
int_0^t D <= (D(0) - D(t))/(2 k^2), and K(t) <= D(t)/(2 k^2); in int_0^t RS = K(t) - K(0) + int_0^t D the two D(t) terms cancel.
Sharpness: for W = -b R^2 take h_N(R) = c_N h((R - N^4)/N) with a fixed smooth bump h and ||h_N|| = 1 (so ||h_N'|| = O(1/N)), l_N = N^{-3}, and
real data 2^{1/2} h_N(R) cos(kZ - l_N R^2), all norms and pairings being taken over one axial period (so D(0) = 1). The inviscid evolution untilts them at t_N = l_N/(kb); along it Delta_5 has norm O(N^2) (the radial phase gradient is at most 2 l_N R = O(N)),
so by contractivity and Duhamel's formula the viscous solution differs from it by O(N^{-1}) at t_N, and K(t_N) = (1/2) <h_N, H_k^{-1} h_N> + O(N^{-1}) -> 1/(2 k^2) with
H_k = -d_RR - 3R^{-1} d_R + k^2. Writing the initial phase factor as a radial derivative gives K(0) = O(N^{-2}), and int_0^{t_N} D <= t_N D(0) = O(N^{-3}).
Hence int_0^{t_N} RS / (D(0)/(2 k^2)) -> 1; they escape to large radius, so the sharp constant for data confined to the core is not known.
So a passive jet, steady or reversing, cannot supply more than half the initial enstrophy over k^2. At the optimal datum of (c) at b = 106
the gain 8.38 is well below the ceiling D(0)/(2 k^2 K(0)) = 31.2 of the lemma, so the lemma does not explain the b^{2/3} law. For the coupled perturbation of the column plus jet the jet drops out of the enstrophy balance (its radial velocity vanishes
and its eta is constant), and
  (1/2) d/dt ||eta_1||^2 = -int |grad eta_1|^2 R^3 dR dZ + 2 int eta_1 q_ref d_Z q_1 R^3 dR dZ + int a eta_1^2 R^3 dR dZ + int eta_1 d_Z(q_1^2) R^3 dR dZ,
where a = u_1^R/R is the radial strain of the meridional perturbation (the jet has zero radial velocity), the linear centrifugal source is at most (G/(2s)) ||eta_1|| (int Gamma_{1,Z}^2 R^{-1} dR dZ)^{1/2} (q_ref <= G/(4s)), and the last
factor is controlled by the modulation dissipation of R2.10. In the linearized problem (in the nonlinear problem the stretching and cubic
terms are not sign-definite and the next estimate is not available) this gives ||eta_1(t)|| <= ||eta_1(0)|| +
G (1 - 1/(4 s(t)))^{1/2} (int_0^t int Gamma_{1,Z}^2 R^{-1} dR dZ dt)^{1/2}, so an enstrophy route to the supply bound of (e) carries the factor G^2 and closes only for
G small against k. The two available norms fail in complementary ways: the energy-Casimir norm makes the swirl-meridional coupling skew but
not the jet transport (its meridional part is nonlocal in R), the enstrophy makes the jet transport skew but not the coupling.
(g) No mixed functional E + eps (1/2)||eta_1||^2 is an instantaneous Lyapunov functional (numerical witness with analytic cross-checks,
G = 300, b = 106, column at s = 1/4, axial period 2 pi). State 1: no swirl perturbation, eta_1 = R^2 e^{-R^2} cos(Z - R^2) (back-tilted).
Then dE/dt = RS - D exactly, measured 5.559, while d/dt (1/2)||eta_1||^2 = -6.865, so the functional decreases only if eps >= 0.810.
State 2: eta_1 = -R^2 e^{-R^2} sin Z, Gamma_1 = lam chi(R) R^4 e^{-R^2}(1 - e^{-R^2}) cos Z, chi a smooth cutoff with 0 <= chi <= 1, equal to 1 for R <= 4 and to 0 for R >= 5 (untilted, RS = 0; for 0 < lam <= 0.48 the cutoff keeps Gamma_ref + Gamma_1 < G everywhere, as the closed-form Casimir used below requires, whereas without it the circulation would exceed G where lam R^4 (1 - e^{-R^2}) cos Z > G, for example at R = 6, Z = 0 when lam = 0.3). Then d/dt (1/2)||eta_1||^2 =
-2.160 + 125.45 lam (both constants by hand: pi (1/2 + 3/16) and the centrifugal source 2 pi int eta-profile x q_ref x Gamma-profile R dR,
which is proportional to G; computed without the cutoff, which changes it by less than 1e-8) and dE/dt = -3 pi/16 - c2 lam^2 with c2 = 13.6 measured (the term linear in lam cancels, as the energy-Casimir
weight requires); at lam = 0.3 this forces eps <= 0.051. The two requirements are incompatible, and eps = 0 fails on state 1. The scaling
is general: the jet forces eps of order b, the centrifugal coupling forces eps of order 1/G, so for b of order G the window is empty at
large G. The derivatives were computed as directional derivatives of the discretized functionals along the exact discrete right-hand
side (no time stepping), with the swirl part of E evaluated by a closed-form Casimir and Gauss quadrature; radial refinement by a factor 4 moves the two thresholds by less than 0.7 per cent, and the derivatives on state 2 with and without the cutoff agree to the six digits printed at 128, 256 and 512 radial points. The obstruction is analytic for every functional of this type whose coefficients do not
depend on G (checked by hand): for F = E_2 + eps int w eta_1^2 R^3 dR dZ, with E_2 the quadratic part of E and
eps > 0, w = w(R) >= 0 locally integrable, independent of G and positive on a set of positive measure, take a smooth compactly supported real h(R) for which the integral displayed below is positive (possible since Gamma_ref > 0 for R > 0) and eta_1 = h cos(kZ), Gamma_1 = h sin(kZ). The jet Reynolds stress and
the weighted jet transport vanish, the centrifugal exchanges inside E_2 cancel, and the centrifugal source of the extra term contributes
4 eps G k int w (Gamma_ref/G) h^2 cos^2(kZ) R^{-1} dR dZ > 0 to dF/dt, while every other contribution is independent of G. So no such F
satisfies dF/dt <= C F with C independent of G. This excludes one family of instantaneous functionals, not cycle (time-integrated)
bounds or functionals with G-dependent or time-dependent weights. Reversing jets: with b(t) = 106 cos(omega t) or 106 sign(cos(omega t)) and swirl-generated data, the jet pumps when the reversal
period is comparable with the Orr time (cumulative jet term up to +0.074 E(0) over 0.3 cell times at omega = 300, against -0.44 E(0) for the
steady jet; negative at omega <= 100 and about 0 at omega = 1000), and E never exceeded E(0); integrated balance satisfied at every sample.
(h) Parametric pumping: a prescribed chirped jet renews the cell energy (Case 2 admissibility not established: the amplitude 0.3 G exceeds the Euler sinusoidal cap of (i)) (the resonance is a leading-order two-mode calculation, reproduced
by a separate Floquet computation; the rest numerical, linear). Frozen column, inviscid, in the variables tau = G t, d = b/G (column width s = 1/4, k = 1):
the two leading inertial waves of the core have speeds s_1 = 0.5309 and s_2 = 0.2996, and the Z-independent jet curvature, which acts by
multiplication with R^2, couples them; for d(tau) = eps cos(k (s_1 + s_2) tau) the linearized column has a sum-frequency parametric
resonance with leading-order amplitude growth rate eps kappa per tau, kappa = 0.0551 (a drive eps cos(phi) has complex Fourier coefficient eps/2). A Floquet computation (monodromy matrix of the linear
system) gives 0.005504 per tau at eps = 0.1 and 0.002754 at eps = 0.05, and no growth at 0.9 or 1.1 times the
resonant frequency. On the freely diffusing Oseen column (exact base, viscosity 1, physical cell time) the computed resonance persists in the tested runs when the jet
frequency follows the drifting sum frequency G k (c_1(s) + c_2(s)) of the spreading core (a chirp), with |b| = 0.3 G, inside the
range |b| <= G/(2 sqrt2) that the Hessian bound admits for a static parabolic jet (for a smooth no-swirl Euler flow the calculation in (i) gives the smaller sinusoidal cap 0.158 G along an axial path under the Frobenius norm; applying it to the C^{1,1} record limits or to the finite-n Navier-Stokes fields requires additional arguments). (A time-dependent Z-independent jet W = -b(t) R^2 is a Navier-Stokes flow only with the axial body force -b'(t) R^2 and the axial pressure gradient -4 b(t), since the radial equation forbids an R-dependent axial pressure gradient; the body force does not enter the perturbation equations. So the jet here is a prescribed forcing.) Starting from a pure swirl perturbation (the leading inertial mode, no meridional flow) the
quadratic energy-Casimir functional E behaves as follows at t = 0.1 cell time (ratio E(t)/E(0)). Without a jet it falls to 0.24 at G = 300,
1000 and 3000, and a steady jet takes it to about 0.03. A jet at the fixed initial resonant frequency gives 0.28, 0.32 and 0.57 (with a
maximum of 2.83 at G = 3000). The chirped jet gives 0.37, 2.30 and 2285. At G = 1000 the chirp reaches 788 by t = 0.3, and at G = 3000
an amplitude |b| = 0.1 G already grows (2.04 at t = 0.1). Refining the radial grid by 1.5, enlarging the domain from R < 8 to R < 10 or
halving the time step changes the G = 3000 value by at most 1.3 per cent. The late growth exponent at G = 3000 (93 per cell time) is close
to the inviscid value 2 eps kappa G = 99. The growth sits in the core: at G = 3000 (in the run with 128 time steps per period, sampled at t = 0.099, where E/E(0) = 2344; its value at t = 0.1 is 2291), E restricted to R < 2 accounts for 2340 of the 2344
units of E(0), and the weight-free norm of the swirl perturbation int |q|^2 R^3 dR grows by the factor 2166. (On the frozen viscous
column the quadratic E is not a Lyapunov functional even without a jet: b = 0, eta = 0, q = e^{-3R^2/5} give E(0) = 25/24 and
E'(0) = 65/12. On the diffusing column the time dependence of the weight restores the sign, E'(0) = -15.4 for the same datum, and every
zero-jet control decays; all runs above use the diffusing column.) Reading. (1) On a bounded radial domain, as in the computations, or for a jet of bounded shear, a Gronwall bound E(T) <= C E(0) holds for a fixed observation time, with C depending on T, the amplitude, the domain and the model parameters (on the unbounded parabolic jet the stress carries the unbounded multiplier R and no such bound is claimed); uniformity in the forcing duration fails for the frozen inviscid two-mode reduction and has not been decided here for the full diffusing-column equations. The frozen inviscid resonant reduction has no amplification bound uniform in the forcing duration, and the diffusing-column runs show large amplification over the displayed finite intervals, so for the frozen two-mode reduction the positive part of the jet term admits no bound that uses only the jet amplitude and is uniform in the forcing duration; the corresponding conclusion for the full diffusing-column equations is not established here (per cycle, normalized by the current energy, the multiplier stays bounded; see below). This is a forced-model obstruction to supply bounds of the kind sought in (e) that use only the jet amplitude, and it motivates controlling the jet history or using other restrictions of the coupled dynamics; its transfer to the coupled viscous problem is unproved. It extends the
fixed-functional obstruction of (g) to time-integrated bounds in the model, and it shows that the no-renewal hypothesis under which an energy-Casimir
reservoir bounds the production of a single core (production at most C ||phi||_infty G^{3/2} L^{3/4} E~(0)^{1/4} T^{3/4} over T cell times on the Oseen column, of the form
C' G^2 L T^{3/4} when E~(0) <= C_0 G^2 L, against the critical size G^2 L T) is a genuine restriction. In the reported runs a Z-independent jet with chirped
time dependence also renews, so renewal is not limited to Z-dependent outer strain. (2) In record units the cell time is G/(C_* delta_n) record times (delta_n^3 = G nu_n/C_*), so the resonant
frequency is (c_1 + c_2) C_* delta_n k per record time, which tends to 0, and the e-folding time 1/(2 eps kappa C_* delta_n) record
times is long in record units but short compared with the band, which lasts of order delta_n^{-2} cell times. A record-scale oscillation
with period of order one record time is far from resonance. A record-scale jet of critical curvature that varies on the record time
scale 1/delta_n, coherently with the drifting core frequency, is resonant, and neither (A) nor NO-SWIRL-EXTRACTION constrains the time
dependence of the record-scale flow on that scale. (3) Two candidate additional estimates for this approach (their sufficiency for the full closing argument is not established, and the list is not exhaustive) are: (N1) a non-resonance
property of the actual record-scale flow along the core path, motivated by the requirement that the axial-velocity curvature at the core should not oscillate
coherently at the drifting inertial sum frequency for many periods, and defined as the chirp-matched coupling-primitive condition formulated in (i), uniformly over subwindows of each fixed parent interval, with one baseline per parent interval and the stated modal-factor and coefficient bounds (R2.14 proposes adding the Z-mean axial strain along the core path near twice an inertial frequency, (N1')); or (N2) a nonlinear no-regeneration statement, namely that pumped
cell energy does not raise the core's swirl integral Sigma (or the axis-weighted production) above that of the reference column. (N1) is unproved; the blanket kinematic reading of (N2) is false by (i), and the forced runs show
increases over the reference column, so (i) proposes the restricted lasting-gain and production condition (N2') instead; no conclusion for actual
Case 2 histories is established. All simulations reported in (h) are linear; the nonlinear runs, including saturation, are reported in (i).
(i) Nonlinear pumping, the second-order mean response, and an axis identity (numerical observations and proved identities, each labelled). The test of
(h) was repeated with the full axisymmetric Navier-Stokes equations for the perturbation of the diffusing Oseen column inside the same
prescribed chirped jet (axially periodic with fundamental wavenumber k = 1, the generated axial harmonics retained by the Fourier discretization in Z, |b| = 0.3 G, initial data the leading inertial mode with swirl amplitude
amp G, amp from 0.003 to 0.1; E denotes the energy-Casimir functional of the perturbation, APE plus kinetic energy, per axial period). At the listed parameters and times the nonlinear energy amplification is close to the linear one for the smaller seeds: 779 against 788 (G = 1000, amp 0.01, t = 0.3) and 2273
against 2285 (G = 3000, amp 0.003, t = 0.1). The larger seeds depart more (2037 against 2285 at G = 3000,
amp 0.01, where the largest swirl fluctuation max |q - q_ref| is 0.47 G, q_ref(0) = G initially; 687 against 788 at G = 1000, amp 0.03). In every pumped run listed here the swirl integral
of the core, Sigma_core = int over r < 1.5 of q^2 r^2 dr dz, its axial-mean part and the mean axis swirl rise above the jet-free control.
At G = 1000, amp 0.03 their maxima over the growth phase (t <= 0.3, all at t = 0.286) are 1.074, 1.039 and 1.30 times the reference column, against 1.00005, 1.00004 and 1.0085 without the jet (the physical and discretization parts of the last value were not separated). At t = 0.286, Sigma_core/reference - 1 is 0.0090 and 0.074 at amp 0.01 and 0.03, where E/G^2 is 0.0020 and 0.0166: the ratio, about 4.5, is the same at both amplitudes, consistent with a quadratic
response in the wave amplitude but not establishing one. The core quantities oscillate with the beat of the two waves (from 1.074 down to 1.027 within 0.014 cell
time). The rise is compatible with a kinematic second-order expansion (derived by hand, remainder O(alpha^3) for smooth displacements of size alpha, the algebra checked numerically); it does not derive the viscous evolution. Displace the circulation
surfaces of an increasing profile Gamma_ref(rho) to nested graphs R = rho + xi(rho, Z) by a volume-preserving map. Volume conservation
gives exactly 2 rho <xi> + <xi^2> = 0, with <.> the axial mean. To second order the axial-mean circulation is
Gamma_bar - Gamma_ref = (1/(2R)) d_R(R Gamma_ref' <xi^2>), and the swirl integrals per unit length change by
Sigma_tot - Sigma_ref = 3 int <xi^2> Gamma_ref Gamma_ref' R^{-3} dR and Sigma_bar - Sigma_ref = - int <xi^2> R Gamma_ref' d_R(q_ref/R) dR.
Both formulas are for integrals over all R; over an Eulerian core 0 < R < c each acquires the endpoint term <xi^2> Gamma_ref Gamma_ref' R^{-2} at R = c (the term at the axis vanishes), which is non-negative for a non-negative non-decreasing profile, so the sign statements below hold for the core integrals too. The first is non-negative for every non-negative non-decreasing profile; the second is non-negative whenever q_ref/R = Gamma_ref/R^3 decreases, which holds for the Oseen profile but not for every increasing profile (Gamma_ref = R^4 on the support of <xi^2> makes it negative). Near the axis write lambda(Z) = lim (rho + xi)/rho for the stretch; volume conservation gives <lambda^2> = 1, the mean axis swirl is q_ref(0) <lambda^{-2}>, which is at least q_ref(0) by Jensen's inequality with equality only for lambda = 1 when q_ref(0) > 0 (the inequality uses q_ref(0) >= 0) (for example for a displacement supported away from the axis), and for the volume-preserving form xi/rho = alpha cos Z - alpha^2/4 + O(alpha^3) it rises by the factor 1 + 2 alpha^2 + O(alpha^3). (Sigma_tot >= Sigma_ref holds exactly on a cylinder of finite radius for every rearrangement of the circulation that is equimeasurable with respect to R dR dZ, whenever the integrals are finite, by the Hardy-Littlewood inequality, since
Sigma_tot is the integral of Gamma^2 R^{-3} in the three-dimensional measure and an increasing Gamma_ref^2 is oppositely ordered to the decreasing weight R^{-3}. On the infinite cylinder ordinary equimeasurability is not enough: the profiles 1 - e^{-a R^2}, a > 0, have the same superlevel distribution (every superlevel set at a level in (0, 1) has infinite measure), while their swirl integrals are a^{1/2} times that of a = 1. There the inequality holds for rearrangements that also preserve the measures of the sublevel sets {Gamma^2 < t}, by the bathtub principle applied to the truncated weights min(R^{-3}, M) and monotone convergence as M -> infinity.) So, for small volume-preserving rearrangements of the Oseen profile, the second-order changes of the Eulerian-mean core integrals are non-negative, and positive for a nontrivial first-order displacement inside the integration region; these are integrated statements (the mean axis swirl is unchanged when the displacement vanishes near the axis, and Gamma_bar - Gamma_ref need not be positive pointwise). This is a kinematic rearrangement lemma: viscous evolution relative to a freely diffusing reference is not itself such a rearrangement, and the lemma does not by itself prove the dynamical increases seen in the forced runs. These rearrangements rule out the no-regeneration statement (N2) of (h) as a blanket kinematic inequality ("pumped energy does not raise the
core Sigma above the reference column"), and the forced viscous runs show computed increases over their reference column; neither observation by itself disproves a statement restricted to actual Case 2 histories. Axis identity (proved): near the axis of a smooth axisymmetric no-swirl flow
write U^Z = W_0(Z, t) - b(Z, t) R^2 + O(R^4) and a_B = d_Z W_0. Then eta_axis = 2b - (1/2) d_ZZ W_0, so b = eta_axis/2 + (d_Z a_B)/4.
For Euler, eta_axis is constant along the axial path (for Navier-Stokes it changes by the viscous term (Delta_5 eta)_axis), D a_B/Dt = -a_B^2 - P_ZZ, and D(d_Z a_B)/Dt = -3 a_B d_Z a_B - P_ZZZ. Along an Euler axial path the
oscillating part of the jet curvature is therefore a quarter of that of d_ZZ U^Z. The Hessian bound caps its amplitude at C_*/4
in record units if the bound controls each second derivative, and at C_*/40^{1/2} = 0.158 C_* for the Frobenius norm (on the axis the
Frobenius norm squared is 8 b^2 + 2 (d_Z a_B)^2); in the cell units of a core of the Hessian-limited radius these caps are G/4 and 0.158 G (the drive measured alone against the whole bound; see the remark on the column's own Hessian below). They bound the half-range of b along the path, not its background value: with d_Z a_B = 4b - 2 eta_axis the Frobenius bound reads H^2 >= 40 (b - 2 eta_axis/5)^2 + (8/5) eta_axis^2, so b stays in an interval of half-width H/40^{1/2} centred at 2 eta_axis/5. A sinusoidal oscillation therefore has amplitude at most 0.158 C_*, while the first harmonic of a nonsinusoidal oscillation can reach (4/pi) 0.158 C_* = 0.201 C_* (approached by square-wave forms, for example in the unbounded potential flow U = B(t)(-2zx, -2zy, 2z^2 - x^2 - y^2), whose Hessian has Frobenius norm squared 40 B^2 everywhere). Since (A) bounds the Frobenius norm, 0.158 G is the relevant cap for a sinusoidal oscillation (the first harmonic of a nonsinusoidal history obeys the larger bound above), about half of the amplitude 0.3 G used in the runs. This
does not exclude pumping. The two-mode approximation of
the sum resonance predicts the viscous threshold |b| = eps_c G with eps_c G = (g_1 g_2)^{1/2}/kappa (the neutral value at exact resonance), minimal at axial wavenumber about 1 to
1.5 core radii^{-1}, where eps_c G = 253.4 (g_1 = 7.86 and g_2 = 24.81 are the viscous decay rates of the two waves, kappa = 0.0551); in the
numerical spectral scan other wave pairs were weaker and the computed self-coupling of a single wave was zero to the precision of the scan. The unperturbed reference column is self-similar: in its own units (radius
(4s)^{1/2}) the jet curvature is b (4s)^{3/2}, so the effective pump strength grows like the cube of the core radius as the core spreads (at a fixed physical axial wavenumber the wavenumber in core radii grows with the radius, so the damping, coupling and frequency change with it).
This two-mode formula reproduces the diffusing-column runs of (h) to within about 0.4 in ln E over the growth phase (for example 0.372
against 0.370 at G = 300). In record units, at exact resonance, the frozen two-mode approximation predicts growth for a core of radius rho and circulation G nu_n when a coherent sinusoidal component of the on-axis
jet curvature exceeds about 254 nu_n/rho^3, independent of G, at the frequency 0.83 G nu_n/rho^2 per record time (for the Oseen profile at axial wavenumber about one inverse core radius; in general b_crit = (nu_n/rho^3) F(k rho) and omega = (G nu_n/rho^2) f(k rho) with modal functions F and f, and 253.4 and 0.8306 are the values of the quoted modal calculation, which change as the core spreads at fixed physical wavenumber). The
componentwise cap C_*/4 is compatible with this once rho^3 >= 1014 nu_n/C_*, the Frobenius cap 0.158 C_* once rho^3 >= 1603 nu_n/C_*; for a core of the Hessian-limited radius (rho^3 = G nu_n/C_*) this means G above about 1014 or 1603. Compatibility is not existence of pumping, which also needs the coherent component, resonance tracking, survival and a seed. These conditions measure the drive alone against the whole Hessian bound; the initial Oseen column Gamma = G(1 - e^{-r^2}) has Frobenius Hessian 1.495 G at r = 0.72 (zero on the axis), the same value as the Burgers column below, so for the column and the drive together a strictly admissible example needs a combined Hessian calculation and a consistent radius normalization (the column alone is admissible only for an initial core radius at least 1.495^{1/3} = 1.14 times the radius used for the caps above, and a larger core changes both the cap expressed in its cell units and the part of the bound left for the drive; this calculation was not carried out, so the quoted thresholds are for the drive measured alone). Nothing in (A) fixes the time scale on which d_ZZ U^Z varies at the
core. Reading: two candidate additional estimates for this
cell-scale approach (sufficiency for the full closing argument not established; not an exhaustive list) are (N1), the non-resonance of the actual record flow (no coherent slow component of the axial-velocity curvature at the core, and, as proposed in R2.14, no coherent component of the log-stretch along the core path near twice an inertial frequency), or
(N2'), a bound of smaller order than the critical size G^2 L T on the lasting gain of the core (the part that outlives the waves) and on the time-integrated
production.
Saturation (numerical, G = 1000, |b| = 0.3 G, amp 0.03, run to t = 0.6; the saturated phase is not yet checked under grid refinement).
Once the swirl fluctuation is of order G the wave energy levels off: it reaches 2574 E(0) at t = 0.364, has reported samples between about 1500 and 2100 E(0) at output times 0.35 to 0.55 (not a bound over that interval), and falls to 744 E(0) by t = 0.6.
The cumulative jet Reynolds-stress input is 984 E(0) at t = 0.3 and 1.26 x 10^4 E(0) at t = 0.6, on average 3.9 x 10^4 E(0) per cell time over [0.3, 0.6] but only 8.6 x 10^3 E(0) per cell time over [0.55, 0.6]. Of the input over [0.3, 0.6], 46 per cent is accounted for by the computed viscous terms D_1 + int m Gamma_Z^2 of the energy-Casimir budget and 0.5 per cent by the change of E; the remainder is what the budget assigns to its non-negative radial deficit term, which was not evaluated separately. Over the simulated interval the accumulated production keeps increasing after the wave energy first levels off; these runs do not establish unbounded production as the forcing duration tends to infinity. In the unrefined nonlinear stage the core integral temporarily exceeds the contemporaneous diffusing reference by up to 63 per cent: Sigma_core reaches 1.63 times the reference and its axial mean 1.48 times (t = 0.54), the mean
axis swirl 6.2 times; at t = 0.6, with the waves partly decayed (largest swirl fluctuation 0.24 G), Sigma_core is still 1.31 times the
reference. Over the reported forced intervals the time-integrated production per cell time is of the critical order; this challenges a no-production mechanism, but it does not disprove the band-length version of (N2'), which concerns durations of order delta_n^{-2} cell times, and energy-Casimir production is not the self-compression work of Theorem 9 (d) (whether that work reaches the constant of Theorem 9 (d) is not decided by the model); the switch-off tests below show that most of the gain of the core decays after the forcing stops, over the observed intervals. (In these switch-off tests the prescribed jet is set to zero at the switch time: they are jet-removal tests, not the natural decay of a jet whose maintaining force is removed.) A first switch-off test (same run, jet removed at t = 0.25, before the main growth, when Sigma_core was 1.010 times the reference) loses almost all of the gain with the waves: Sigma_core falls to 1.002 by t = 0.3 and is 1.001 times the reference at t = 0.6, the whole-domain Sigma 1.0002 times. Switching the jet off at t = 0.3 (end of the growth phase) gives a short further rise (Sigma_core 1.117 times the reference at t = 0.306), after which the gain decays with the waves (1.008 at t = 0.6, whole-domain Sigma 1.0011). Switching it off at t = 0.4 (saturated, Sigma_core 1.25) leaves a residual gain at the observation time: 0.3 cell times later Sigma_core is 1.045, its axial mean 1.035 and the whole-domain Sigma 1.0045 times the reference (the last samples, 1.0404, 1.0442, 1.0450 for Sigma_core at t = 0.6, 0.65, 0.7, do not show monotone decay of the relative gain), while the wave energy has fallen from 1822 to 66 E(0); the net whole-domain gain, 0.0020 times the initial reference integral, is about 1.3 per cent of the signed self-compression work done (3 int Pi_s = 0.158 times the initial reference integral, accumulated every fourth time step, 0.157 of it before t = 0.45). A refinement to 192 radial and 96 axial points reproduces the growth phase (to t = 0.3) to within one per cent; the saturated phase was not refined. The signed self-compression Pi_s = -int a_s q^2 r^2 dr dz, the
model analogue of the quantity the closing argument of Case 2 has to bound (here it is the compression by the perturbation velocity; the prescribed jet has no radial velocity, so it is the whole radial compression), has a positive accumulated value by the developed amplification stage of the reported pumped episodes (the instantaneous value need not be positive, and the accumulated value can be slightly negative in the initial transient): in this model dSigma_tot/dt = -D + 3 Pi_s + F_R, where F_R is the flux of the swirl integral through the outer boundary R = 8 (the jet is Z-independent and has no radial velocity, so it neither transports Sigma in R nor compresses it radially; its shear enters the energy budget through the jet Reynolds stress); the cumulative self-compression is integrated directly, not inferred from this balance; and at G = 1000, |b| = 0.3 G, initial swirl amplitude 0.1 G, the cumulative
3 int_0^t Pi_s reaches +0.235 Sigma_ref(0) by t = 0.4 (time integral accumulated every fourth step; it is never below -0.0003 Sigma_ref(0)), while the net gain of Sigma_tot over the
reference is about 0.022 Sigma_ref(0) (the initial perturbation contributes 0.0002): the difference corresponds to a net sink of about 91 per cent of the work, excess dissipation and the change of the boundary flux together (not evaluated separately; conditional on closure of the swirl balance). (Here and below Sigma_ref(0) is the swirl integral of the reference column on the computational domain R < 8, which omits about 12 per cent of the infinite-radius value, the tail of G^2/R^2 beyond R = 8.) With a prescribed zero-mean
outer strain instead of the jet (R2.8) the self part was negative at order-one modulation; the jet-pumped wave field reverses that sign. At amplitude 0.03 with the jet kept on to t = 0.6, the cumulative 3 int Pi_s is 0.009, 0.069, 0.124, 0.219, 0.287, 0.326, 0.347 Sigma_ref(0) at t = 0.30, 0.35, ..., 0.60 (time integral accumulated every fourth time step; a sum over the output times, every 0.002 cell times, resolves the oscillatory integrand poorly and may alias its higher-frequency components; here it exceeds the in-loop value by 12.5 per cent at t = 0.3 and differs by less than one per cent afterwards; all quantitative budgets here use the in-loop integrals unless stated), on average 1.13 Sigma_ref(0) per cell time over [0.3, 0.6], while the whole-domain Sigma stays below 1.10 times the reference. This approximately equals the free decay rate of the reference column at age 0.15 cell time (1.123 Sigma_ref(0) per cell time), and it is 1.1 to 3.7 times the free decay of the reference over the successive intervals of 0.05 (aggregate ratio 2.25 over [0.3, 0.6]); the free decay has a finite total, at most Sigma_ref(0), so this ratio is only a benchmark. A rate of order Sigma_ref(0) per cell time, that is of order G^2 L per cell time for an axial length L in cell units, sustained over the band of about delta_n^{-2} cell times gives work of the critical size G^2 L delta_n^{-2} = G C_* L_rec/nu_n (L_rec the axial length in record units; Sigma and the work are invariant under the Navier-Stokes scaling, which relates the cell units to the original variables of Theorem 9, both of viscosity one; in the record frame, of viscosity nu_n, both carry the factor nu_n^2, as in Theorem 9 (e)), which is the order required by Theorem 9 (d). The comparison of constants with 2 m_phi/(3P), including the weight e^{3 C_0 (t_n - t)}, the number of cells and the contribution of all sourced vorticity over the whole history, is not determined by the model. So on the reported intervals the computed self-compression rate is comparable to Sigma_ref(0) per cell time, and maintaining such a rate over the band would give work of the critical scaling; neither that persistence nor the identification with the full sourced component of Theorem 9 (which in the record frame contains nearly all vorticity, including that of the record flow itself) or with its weighted constant has been established, and the model says nothing about the persistence of the forcing over the band. The body force that maintains the jet U^Z = -b(t) R^2 is f^Z = -b'(t) R^2 + 4 nu b (viscosity nu; the uniform part can be absorbed in a uniform axial pressure gradient); its quadratic part is of order G^{1/3} C_*^{5/3} nu_n^{1/3} R^2 in record units, so it vanishes in the record frame on bounded sets (G is fixed, so G nu_n -> 0); it is not negligible in cell units, and this is the criticality of the cell scale again, not an estimate. The same sign and order were found independently, with a different solver, on the strained (Burgers) column in the survival window at G = 3000, |b| = 0.3 G: the cumulative 3 int Pi_s is 0.19 and 0.34 Sigma_ref(0) by 0.3 cell times (initial swirl amplitudes 0.01 G and 0.03 G), growing at 1.4 to 1.5 Sigma_ref(0) per cell time in the saturated phase, with core gain up to 1.11 to 1.12 and net whole-domain gains of 0.019 and 0.023 Sigma_ref(0). The instantaneous self-compression there changes sign in about half of the samples; what is positive is the accumulated value during the developed episode. That computation reports that its swirl-moment balance then requires an excess dissipation (net of the boundary flux and the background-strain terms) of 93 to 104 per cent of the accumulated self-compression; the displayed pairs alone give 90 and 93 per cent before the background-strain terms, and the full strained balance was not reconstructed here. Those saturated runs violate the maximum principle for the circulation by 2 to 4 per cent of G, so their nonlinear budgets are indicative only. There, too, the gain decreases after the forcing stops: with the jet removed at 0.3 cell times from the saturated state, the cumulative self-compression grows by only about 4 per cent more (0.189 to 0.197 Sigma_ref(0)) by 0.5 cell times, and the core and whole-domain Sigma fall to 1.0024 and 1.0010 times the reference and are still falling. The observed finite-time amplification transition of the modulation eps_b G on that column, under that computation's protocol (transient amplification can occur below an asymptotic threshold, so these are not Floquet thresholds), lies between 350 and 500 at a_0 = 4 (between a run with a 0.8 per cent transient followed by decay at 350 and one with transient tenfold growth at 500), between 600 and 900 at a_0 = 6, and between 1200 and 2000 at a_0 = 8. This is roughly 22 a_0^2, a descriptive fit; the two-mode values are 312, 618 and 1036, and the two-mode ingredients scale like a_0^{1.73}. In the leading model the threshold is independent of G in cell units, while the Hessian bound admits a static parabolic jet up to 0.35 G and a sinusoidal Euler oscillation of the curvature along an axial path up to 0.158 G (Frobenius; half-range). So the threshold is the fraction of about 22 a_0^2/(0.158 G) of the admissible oscillating curvature. The a_0 = 4 Burgers column itself has Frobenius Hessian up to 1.5 G (at R = 0.72), so a strictly admissible example needs the Hessian bound to be read for the column and the jet together; the thresholds quoted are therefore provisional for this family: an admissible example needs the Hessian calculation for the column and the drive together (the static and oscillating maxima cannot be allocated independently), a rescaling if necessary, and the threshold constants recomputed. Here the circulation of a selected core in viscous units is at most the datum's G_0 = ||r u_0^theta||_infty, so large circulation cannot be obtained by taking n larger (it may vary along the sequence while bounded, and a large G_0 does not by itself give selected cores above the threshold): with the descriptive fit, the fraction is below one only for G above about 140 a_0^2, that is about 2200 to 9000 over the survival window a_0 = 4 to 8 (with the static cap 0.35 G about 1000 to 4000; at G = 3000 and a_0 = 8 the measured threshold exceeds even the static cap). For such data the two-mode model predicts growth under a coherent oscillation at the sum frequency above the threshold, provided the coherent interval is long enough for the growth to lift the seed to order one; these are approximate model comparisons, not sharp necessary conditions.
Two further points limit what the pumping says about Case 2 (both verified by hand). First, in the frozen inviscid resonant reduction the
energy multiplier per forcing cycle is exp(4 pi eps kappa/(k (c_1 + c_2))), about 1.28 at |b| = 0.3 G and independent of G (with the viscous damping of the two-mode system it is exp(4 pi lambda_+/omega), about 1.035 at G = 1000 and 1.19 at G = 3000 at |b| = 0.3 G), so what
fails is a cumulative bound over many cycles, not a bound per cycle. Second, the axis identities cannot give non-resonance by
themselves: Phi = g(tau) (Z^3/6 - Z R^2/4) is harmonic, U = grad Phi solves the Euler equations with pressure -Phi_tau - |grad Phi|^2/2,
and at the origin it has a = 0, eta_axis = 0, b = g/4 and P_ZZZ = -g' for an arbitrary smooth g(tau), so an arbitrary curvature chirp
is realized locally by an exact (infinite-energy) Euler flow. The same example shows that a realizable oscillating curvature carries
companion terms g Z^2/2 in U^Z and -g Z R/2 in U^R (g = 4b for the oscillating parts), of the same cell order as b R^2 at an axial
distance of one core radius, which the axially homogeneous jet omits. So the pumping is a statement about a prescribed forcing; whether
a finite-energy record flow can supply it is open. Two further facts bear on this. First (exact, checked by hand): near the axis an irrotational axisymmetric meridional field has a potential
phi_0(Z) - phi_0''(Z) R^2/4 + O(R^4), so U^Z = phi_0' - phi_0''' R^2/4 + O(R^4) and its axis curvature is b = phi_0'''/4, whose mean
over an axial segment [Z_1, Z_2] of length L is (phi_0''(Z_2) - phi_0''(Z_1))/(4L), at most ||grad U||_infty/(2L). So the part of the field induced by vorticity outside a simply connected tube containing
the axis segment (smooth and irrotational in the tube) cannot maintain a fixed nonzero mean curvature over arbitrarily many cells
under a bound on its gradient uniform in the length (a quantitative restriction; over an axial period of a periodic irrotational
field the mean is exactly zero). An axially uniform curvature over many cells is carried by vorticity near the axis: on the axis
b = eta_axis/2 + (d_Z a_B)/4 (eta = omega^theta/R, omega^theta = d_Z U^R - d_R U^Z, and a_B = d_Z U^Z on the axis as in the axis identity above), so the mean of b over the segment is the mean of eta_axis/2 plus (a_B(Z_2) - a_B(Z_1))/(4L), and eta obeys transport, diffusion and the swirl source d_Z(q^2) (not a closed law for b).
In the free axially periodic problem a jet of this kind generated by the swirl belongs to the finite-energy perturbation and is
included in the energy-Casimir budget of R2.10, provided its hypotheses continue to hold; it is not a new input, and the budget gives
no pointwise bound on the curvature. In a non-periodic history, vorticity carried into the segment and the localization fluxes are
not covered. Second (numerical, from a separate computation at two resolutions whose specification is not reproduced here; not checked, and not used as evidence): on the strained
column at G = 5000, a_0 = 4, |b| = 0.15 G, with a localized, kinematically admissible companion strain added, a tangent-linear seed
on the forced base grows with an energy e-folding time of about 0.0004 cell times from t of about 0.0025 (an energy growth rate of
about 2500 per cell time, against 31 under the axially uniform jet alone); the same computation finds faster growth when the forcing
frequency is detuned to 0.8 or 1.2 times the resonant one, and attributes the growth to broadband amplification by the companion
strain (of order G in cell units), not to the tuned resonance. With the jet switched off at t = 0.3 in the pumped G = 5000 run the
excess of Sigma_core over the reference falls from 1.07 to 0.03 per cent by t = 0.5. A deterministic form of (N1) that suffices in the two-mode reduction: on each fixed parent cell interval choose one constant baseline curvature and the corresponding base evolution; if the
oscillatory primitive of the complete interaction matrix (the record curvature against the resonant phase, multiplied by the record-to-cell time ratio, with the modal factors) tends to zero
uniformly over the subwindows of that interval, with uniformly bounded full and base coefficient matrices, then on that interval the pumped two-mode evolution converges to the base one (integration by parts and
Gronwall; a scalar curvature condition replaces the matrix condition only after the required control of the modal factors); under these coefficient bounds its failure is necessary for an order-one departure from the chosen baseline evolution on that fixed interval; excluding amplification also requires control of the baseline. The conversion to record time is delta_n int b_rec e^{-i phi} dt_rec for the coupling primitive (time and curvature conversions together), multiplied by the modal coupling 2 kappa when, as here, the integral is the complex Fourier coefficient (a drive B cos(phi) has complex coefficient B/2 and leading amplitude exponent kappa B). An explicit sufficient form on the record histories (checked by hand): write h_n(t) = b_n(X_n(t), t) - beta_n for the on-axis curvature along the core path minus a constant and N_n = sup_{s<t} |int_s^t h_n| over the available past (N_n is not the velocity maximum M_n). Integration by parts against F = int h_n gives |(1/T) int_I h_n e^{-i phi}| <= N_n (1/T + (1/T) int_I |phi'|) on every window I of length T (h_n integrable, phi absolutely continuous). The resonant period has record length of order 1/(C_* delta_n), a fixed cell interval has record length of order G/(C_* delta_n) and int_I |phi'| of order G on it, so the coupling primitive is O((1 + G) delta_n N_n) on every fixed cell interval, and G delta_n N_n -> 0 (with G fixed: delta_n N_n -> 0) makes the two-mode coupling small on every such interval; excluding the accumulated work over the band needs in addition an argument for the coupled flow over the whole history (the same crude estimate over delta_n^{-2} cell times is O(G N_n/delta_n)). sup_n int |h_n| <= K over the past implies the condition, since G delta_n K -> 0. This constant-baseline form is stronger than non-resonance for general curvature histories: any slow drift of the curvature along the path by an amount of order C_* over the band violates it while being far from resonance (for a constant frequency on a window of whole periods its Fourier coefficient at the resonant frequency is at most 2 sup|d_t b|/omega; a chirped phase adds endpoint and phase-variation terms), and a smooth Euler example of such a drift within the three derivative bounds with energy tending to 0 appears possible (sketch, not verified: a compactly supported swirl-free blob, scaled to the Hessian bound and slowed so that it evolves once over the band; an axis point outside the blob sees a curvature that starts at 0 and changes at the rate -(1/4) d_ZZZ p of the exterior pressure; the datum, a nonzero derivative and the bounds have not been checked). The form of (N1) this suggests is a chirp-matched primitive condition: for each fixed cell duration, delta_n int_I (b_n(X_n(t), t) - beta_{n,J}) e^{-i phi_n(t)} dt is small uniformly over the subwindows I of each fixed parent interval J, with phi_n the drifting resonant phase and one constant baseline beta_{n,J} for each fixed parent interval (the same for all its subwindows, so that one comparison evolution is defined), together with analogous control of the modal coefficients and uniform bounds on the reduction. No admissible record flow has been constructed that separates the constant-baseline form from non-resonance. A small coefficient over one whole window can hide coherent forcing on subwindows, and being below a frozen threshold does not by itself make the accumulated production negligible, so a separate argument would still be needed over the delta_n^{-2} cell times of the band. No derivation of either form from the conservation laws, the derivative bounds or compactness is available, and the C^1 record convergence cannot see the relevant scale: an Euler structure of size L at the Hessian bound (velocity C_* L^2, gradient C_* L, frequencies of order C_* L) vanishes in C^1 as L -> 0 while keeping curvature of order C_*, and for L comparable with delta_n its scales (frequency of order C_* delta_n, curvature of order C_*, cell Reynolds number of order G) are compatible with the resonance, subject to the constants, the mode structure, coherence and survival; at the initial Oseen radius the two-mode threshold is compatible with the cap only for G above about 1014 (componentwise) or 1603 (Frobenius). Whether a record flow contains such a structure next to the core, coherently over the required number of periods (about 2.4/eps periods per amplitude e-fold in the frozen inviscid leading-order estimate: about 10 at eps = 1/4, about 15 at the Frobenius cap; with the viscous damping of the two-mode system, amplitude exponent -(g_1 + g_2)/2 + (((g_1 - g_2)/2)^2 + (kappa B)^2)^{1/2} for a sinusoidal curvature amplitude B in cell units, it is about 40 initial forcing periods at G = 3000 and B = 0.15 G and about 36 at the cap, and it diverges at the threshold), is the realizability question. (N1) is an unproved hypothesis.
Locking (numerical, G = 1000, |b| = 0.3 G, swirl amplitude 0.03 G unless stated). If the jet frequency is held fixed, with continuous phase, instead of following the drift of the core (the core frequency here is the prescribed sum frequency computed from the freely diffusing reference, not a measured frequency of the nonlinear core), the held-frequency tests give the following finite-time work increments; they suggest that an already pumped core keeps gaining until the reference sum frequency has drifted by about 10 per cent from the held value, but establishing locking or a detuning tolerance would need modal phase, frequency and energy-transfer diagnostics, which were not computed: held from t = 0.3, the cumulative 3 int Pi_s is 0.115 at t = 0.4 (0.124 with the chirp) and 0.135 at t = 0.6 (0.347 with the chirp); held from t = 0.4, it is 0.271 at t = 0.5 (0.287 with the chirp) and stays at 0.29 from t = 0.55 to t = 0.7 (the held runs use the sum over output times; on the chirp run that sum agrees with the step-wise integral to within one per cent after t = 0.35, which does not bound its error for a different forcing history). From a small seed the two fixed frequencies tested gave much less self-compression than the chirp at this G: at swirl amplitude 0.1 G, a fixed jet frequency equal to the initial sum frequency, or to the one the spreading core passes at t = 0.1, gives cumulative 3 int Pi_s below 0.002 by t = 0.4 (sum over output times), against 0.235 with the chirp (the spreading core crosses a fixed line in a few hundredths of a cell time, too fast for the growth). The residual whole-domain gains at the end of the held runs are 1.7 to 3.4 per cent of the cumulative work. These tests do not show that frequency tracking is necessary for every start-up protocol (other frequencies, phases, seeds and windows were not tried). A steady strain holding the core at a steady radius removes the drift of the radial profile, but axial stretching still changes the wavenumber of a material disturbance and with it the sum frequency: on the strained (Burgers) column the cells are stretched and the sum frequency drifts with the axial wavenumber k = e^{-a_0 t}, so a stationary frequency would need a mechanism that maintains the axial wavenumber; an independent computation (G = 3000, a_0 = 4, |b| = 0.3 G, linear amplitude, forcing frequency fixed at 0.9, 1.0 and 1.1 times the initial sum frequency) gives energy gains of at most 4.9, 1.6 and 1.0 over 0.1 cell times, against about 110 with the chirp, consistent with a tolerance of about 10 per cent (three frequencies; not a resonance-width measurement), a fixed line amplifying mainly while the drifting frequency crosses it (a few hundredths of a cell time at a_0 = 4). Translating patterns (proved by hand). Suppose the record flow near the core path is a steady pattern translating axially, U = Ubar(r, z - c t), and write v(xi) = Ubar^z(0, xi) - c for the relative axis speed. Along the axis path a = v', d_ZZ U^Z = v'', 4 (b - eta_axis/2) = d/dt(a/v) + a^2/v, and int_{t_1}^{t_2} a dt = log(v(t_2)/v(t_1)) exactly. Integration by parts gives, on a window of length T on which |a| <= eps and |v| >= m (m a lower bound on the speed), |(1/T) int (b - eta_axis/2) e^{-i phi} dt| <= eps/(2 m T) + eps (eps + sup |phi'|)/(4 m), so a Fourier coefficient A of b - eta_axis/2 at frequency omega over complete periods needs m <= eps (omega + eps + 2/T)/(4 A) (this uses a pointwise bound on the strain along the path; for no-swirl Euler eta_axis is constant along the path, so over complete periods at constant frequency this is also the coefficient of b, which need not hold for Navier-Stokes or for a chirped finite window). Independently of any strain bound, consider a single-harmonic pattern v = v_0 + V cos(K xi) without stagnation (V < v_0, v_0 the mean relative speed). The particle traverses a period in time 2 pi/(K Delta), Delta = (v_0^2 - V^2)^{1/2}, so its frequency is Omega = K Delta (not v_0 K), and along its path b - eta_axis/2 = K^2 (v_0 - Delta)/4 - (K^2 Delta/2) sum_{j >= 1} zeta^j cos(j Omega t) with zeta = V/(v_0 + Delta) < 1 (checked by hand from v(xi(t)) = Delta (1 + 2 sum zeta^j cos(j Omega t))). The real fundamental amplitude is K Omega zeta/2 < K Omega/2, so a real sinusoidal amplitude c_0 C_* at the resonant frequency 0.83 C_* delta_n (record units) needs K > 2.41 c_0/delta_n, a wavelength below about 2.6 delta_n/c_0. So for this single-harmonic nonstagnating family a record-scale translating pattern sampled slowly by the core cannot supply the coherent curvature (more general translating patterns need a separate argument); a cell-scale pattern is not excluded, and it lies outside the Z-independent jet model. Two further facts, checked by hand, concern the stated classes. Under the Euler scaling U(x, t) = lambda L v(x/L, lambda t) with L = lambda H_0/C_* (which keeps the Hessian bound at C_*), the ratio of path strain to frequency and the ratio of curvature amplitude to Hessian bound are invariant, so realizability is a scale-free question: does some Euler flow give a material axis particle an oscillating curvature of a fixed fraction of the Hessian bound, over the required number of periods, while the mean strain along its path is smaller than the frequency by a factor of order 1/G? And for an isolated smooth ring of radius L whose vorticity lies in a tube of thickness d << L with uniformly bounded profile, a scaling estimate (axis curvature of order Gamma_r/L^3 against the Hessian Gamma_r/d^3 inside the tube, Gamma_r the ring circulation) gives axis curvature of order (d/L)^3 times the Hessian bound, so such thin rings cannot supply a fixed fraction (an estimate, not a theorem for arbitrary ring configurations).
Forced runs below the axial Euler amplitude cap (numerical, same forced model, 128 by 48 points unless stated; the growth phase at G = 3000 was refined, the saturated phase at G = 1000 was not; the cap is a necessary condition for an Euler drive, and satisfying it does not make the axially homogeneous jet realizable). The runs above use |b| = 0.3 G, about twice the cap 0.158 G on an Euler oscillation of the axis curvature. At |b| = 0.15 G, within that cap, the chirp still pumps, and the growth follows the two-mode self-similar formula. At G = 3000 (swirl amplitude 0.01 G) the wave energy grows by the factors 2.0, 5.6, 8.3 and 13.4 over the successive intervals of 0.05 cell times up to t = 0.2 (two-mode prediction 3.5, 5.9, 9.3 and 14.0; the first interval starts from a single mode rather than the growing combination), to 1249 E(0) at t = 0.2 (160 by 64 points, time integrals accumulated every fifth step; 128 by 48 points give the same factors and 1241 E(0)), with cumulative 3 int Pi_s = 0.0034 Sigma_ref(0), Sigma_core 1.012 and the whole-domain Sigma 1.0032 times the reference; without the jet the same seed decays to 0.05 E(0) by t = 0.25 and the whole-domain Sigma stays within 3 x 10^{-5} of the reference. After t = 0.2 the saturated state is not resolved. At 128 by 48 the energy-Casimir inequality fails and the circulation leaves [0, G] by about one per cent of G; at 160 by 64 the circulation leaves [0, G] by up to 9 per cent of G (between t = 0.24 and 0.28); at 224 by 80 points (time integrals accumulated every fifth step) it stays within 2 x 10^{-4} G of [0, G] at all output times up to t = 0.3 except at t = 0.268, where it reaches -0.021 G. The 160 and 224 grids agree to about one per cent through t = 0.25 (wave energy 1.355 and 1.366 x 10^4 E(0) at t = 0.25; largest Sigma_core over [0.24, 0.26] 1.240 and 1.246, largest whole-domain Sigma 1.058 and 1.060 times the reference); on the finer grid the wave energy peaks at 1.67 x 10^4 E(0) at t = 0.254, and at t = 0.3 the two grids differ by 17 per cent in the wave energy. On the finer grid the cumulative 3 int Pi_s, accumulated every fifth step, is 0.066 and 0.143 Sigma_ref(0) at t = 0.25 and 0.3 (sums over the output times, spaced 0.002, about one sample per forcing period, give 0.019 and 0.127 and are not reliable in this phase). These saturated values come from one grid with one circulation excursion and are not used as quantitative results. At G = 1000 the chirp at 0.15 G is below threshold for the initial core and crosses it near t = 0.1 (the predicted growth rate changes sign there), when the spreading core satisfies the radius condition above, (1 + 4t)^{3/2} >= 1690/G = 1.69 at the amplitude 0.15 G, that is t >= 0.105 (the cap-compatibility condition 1603/G would give t >= 0.092). The wave energy then grows by the factors 3.9, 10.4 and 23 over [0.1, 0.3], [0.3, 0.45] and [0.45, 0.6] (predicted 3.9, 12.2 and 33; the last interval is entering saturation), to 470 E(0) at t = 0.6, where the cumulative 3 int Pi_s is 0.0085 Sigma_ref(0) and Sigma_core is 1.076 times the reference. Continued to t = 0.9 (time integrals accumulated every fourth step), the run saturates: the wave energy peaks at 2109 E(0) at t = 0.72, Sigma_core reaches 1.81 and the whole-domain Sigma 1.095 times the reference near t = 0.75, the circulation stays in [0, G], and the cumulative 3 int Pi_s is 0.057, 0.115 and 0.150 Sigma_ref(0) at t = 0.7, 0.8 and 0.9. Over [0.6, 0.9] that is 0.47 Sigma_ref(0) per cell time, 1.6 times the free decay of the reference over the same interval (at |b| = 0.3 G the same seed gave 0.347 Sigma_ref(0) by t = 0.6, 2.25 times the free decay over [0.3, 0.6]). So for these two runs at G = 1000 and amp 0.03, halving the amplitude to below the axial Euler cap delays the amplification (energy peak at t = 0.72 against 0.36) without removing it, and once the core is pumped its computed self-compression is again of the critical order (nonlinear-stage budgets unrefined). Freezing the quoted modal coefficients gives the onset estimate G rho^3 > 1689 (the modal threshold 253.4 divided by 0.15) for the core radius rho in cell units, that is t > 0.105 at G = 1000; the tabulated energy begins to increase between the output times 0.10 and 0.15 (the threshold along the actual fixed-wavenumber trajectory involves the modal functions F(k rho); the estimate also assumes resonance tracking, an effective seed and enough duration). The strained (Burgers) column in the survival window behaves differently at this amplitude: an independent computation at G = 3000, a_0 = 4, |b| = 0.15 G, swirl amplitude 0.03 G, chirped, to t = 0.4, gives only a weak transient (wave energy at most 2.5 times its initial value and 0.65 times at the end, Sigma_core within 0.07 per cent of the reference, cumulative 3 int Pi_s at most 0.001 Sigma_ref(0)); there |b| = 450 lies inside the observed transition bracket 350 to 500 and the drift of the cells ends the transient by t = 0.2, so, if the transition amplitude is independent of G as in the leading model, these runs place it between 450 and 500 at a_0 = 4, and at this amplitude the channel would open for G between about 3000 and 3300 (whether the cap amplitude 0.158 G at G = 3000, |b| = 474, gives a developed episode was not tested). At G = 5000 (|b| = 750, same column, amplitude and seed, chirped, to t = 0.3) the same computation shows pumping: the wave energy grows 258-fold to a nonlinear plateau, Sigma_core rises to 1.069 and the whole-domain Sigma to 1.031 times the reference, the circulation stays within [-0.0002 G, G], and the cumulative 3 int Pi_s, averaged over one forcing period, rises from 0.038 to 0.087 Sigma_ref(0) over [0.2, 0.3] (it oscillates by about 0.01 within each period; sums over output times at spacing 0.0002, about seven samples per forcing period, change by less than 0.005 when every second sample is dropped), about 0.5 Sigma_ref(0) per cell time, the same order as at G = 1000. This changes nothing in the reading above: it is still a statement about a prescribed coherent forcing, and whether a finite-energy record flow supplies one is the open question. The cap 0.158 is the best case for a sinusoidal curvature history. For a kinematic model of a periodic train of coaxial vortex rings with Gaussian cores (ring radius L, spacing lambda, core e-folding radius d, frozen and translating at the circulation-centroid speed; not an Euler solution, since the axis value of eta varies while the axis fluid moves relative to the train), an independent computation over lambda/L from 0.5 to 3 and d/L from 0.2 to 0.5 gives a largest real first-harmonic amplitude of b along the axial path, over the sampled grid, of 0.045 times the maximal Frobenius Hessian (at lambda/L = 2, d/L = 0.5; the scan does not establish a global maximum; the maximum sits inside the ring cores, and the axis vorticity of the Gaussian tails cancels part of the curvature: without it the ratio would be 0.079); for lambda/L = 3 the axis has stagnation points relative to the train. I checked the axis velocity of the best case (0.5861 and 0.4194 at the ring plane and midway) by direct Biot-Savart quadrature. If this amplitude ratio were realizable and frequency matching held, the frozen amplitude comparison would move from G rho^3 of about 1603 at the cap to about 5600 (253.4/0.045; not an onset result); whether the passage frequency can also be matched to the sum resonance of the core was not examined. Whatever the frequency, an unforced train is part of the perturbation of the ideal column, so the production link of R2.10 limits what it can supply (derived here from the bounds stated there, under the same restrictions: free Oseen column, axially periodic with period L in cell units, no jet, no inflow, |q_Z| <= G from (A), |Gamma| <= G and the swirl cap). Slice by slice in Z, for |f| <= H_0, int f^2 R dR <= sqrt2 H_0 (int f^2 R^3 dR)^{1/2}; with f = q_Z, H_0 = G, Cauchy-Schwarz in Z and in t, and the Lyapunov bound int_0^T int m Gamma_Z^2 dx dt <= E~(0) (m >= R^{-2}, E~ the energy-Casimir functional of the whole perturbation, which contains the kinetic energy of the train), int_0^T int q_Z^2 dx dt <= C G L^{1/2} T^{1/2} E~(0)^{1/2}, and with int q^2 dx <= C G^2 L the band production of the core over T cell times (pairing localized to the core, as there) is at most C ||phi||_infty G^{3/2} L^{3/4} E~(0)^{1/4} T^{3/4}. Production of the critical size G^2 L T therefore lasts at most of order E~(0)/(G^2 L) cell times: a train acts as a finite reservoir, whatever its frequency, and sustaining the band (of order delta_n^{-2} cell times) needs either a reservoir of order G^2 delta_n^{-2} per unit length or renewal through the terms the ideal column lacks. The Hessian bound does not exclude such a reservoir by itself: a perturbation of radial extent rho_s cell lengths has velocity at most of order G rho_s^2 and kinetic energy per unit length at most of order G^2 rho_s^6, so at rho_s of order delta_n^{-1/3}, still far below the record scale delta_n^{-1}, the kinetic-energy upper bound has the required scaling (this constructs no such perturbation; the potential-energy part and the weight at large R were not estimated). Over times long compared with the initial Oseen time the column widens, so cell times here refer to the initial width; on the Burgers column the same bound holds per current material period only, as stated in R2.10.

R2.13 Fresh modulated columns and the price of renewal (a numerical observation, the self-compression W reproduced with an independent solver; a corollary
proved by hand). (a) Observation. Unforced axisymmetric Navier-Stokes equations with swirl in cell units (viscosity 1, axial period
2 pi, no external flow, zero initial meridional velocity), solved numerically on a truncated radial domain; Oseen column with an axial
modulation of q of parameter 0.3: q_0 = G (1 - e^{-R^2}) R^{-2} (1 + 0.3 f(R) cos Z), G = 1000, with f = e^{-R^2} (maximum
fractional modulation 30 per cent; the circulation increases in R at every Z and stays below G) or f = R^2 e^{-R^2} (maximum
fractional modulation 0.3/e, about 11 per cent; the circulation is not monotone in R far out and exceeds G there by up to 0.4 per
cent). The unmodulated reference is Rayleigh-stable; no stability statement is made about the modulated data. Neither datum is a
meridional equilibrium (eta_t = d_Z(q_0^2) is nonzero at t = 0), and neither is claimed to satisfy every hypothesis of (b) (the Oseen
column of circulation G has Frobenius Hessian up to 1.495 G in these units, R2.5). Measures: Sigma = int q^2 R^2 dR dZ and
Pi_s = -int (u^R/R) q^2 R^2 dR dZ, for which Sigma' = 3 Pi_s - D on the full radial domain with vanishing boundary flux (on a truncated domain the balance contains an outer-boundary term; the boundary convention of the reported budgets is not stated in their source); W(t) = int_0^t Pi_s is the accumulated self-compression and
P(t) = int_0^t int |d_Z(q^2)| R dR dZ dt the production budget (physical measure, as in (b)); T_2 = 12.1254/G cell times is a
reference inertial time of the column. W is not of one sign. At the sampled quarter periods t/T_2 = 0.25, 0.5, ..., 3 the ratios W/P
are -13.2, +0.35, -3.9, +1.01, -2.1, +0.48, -1.2, -0.05, -0.9, -0.08, -0.7, -0.07 for f = e^{-R^2} and -9.7, -1.52, -1.75, +1.80,
-0.99, +0.83, +0.20, +0.21, -0.23, +0.19, +0.14, +0.36 for f = R^2 e^{-R^2}. So at t = T_2 (0.0121 cell times) W/P = 1.01 and 1.80:
the accumulated self-compression is positive and comparable to the production budget at these early times. For the first datum the
values at multiples of T_2/2 exceed those at the neighbouring odd multiples of T_2/4 through 3 T_2; no pattern of later extrema is
claimed (P grows, so W/P at different times does not compare the depths of W). These values were obtained by two separate
computations (up to 640 radial points) and reproduced with a third code (radial finite differences on
[0, 8], Fourier collocation in Z with two-thirds dealiasing, integrating-factor fourth-order Runge-Kutta, 960 steps per T_2, time
integrals accumulated inside the time loop, 128 by 48 and 192 by 64 radial by axial points): W agrees with the other computations to
within 1 per cent through 1.5 T_2 for both data and through 2 T_2 for f = e^{-R^2}, and to within 2.3 per cent at 3 T_2 at 192 by 64
(6 per cent at 128 by 48); these comparisons concern W, not P or W/P, and are not error bounds for the infinite column. Not checked
here: longer times and G = 3000. Reported from separate computations whose specification is not reproduced here (not checked, not used as evidence): at G = 3000, W is positive at the sampled
times through 10 T_2 for f = R^2 e^{-R^2} and negative from 6 T_2 for f = e^{-R^2}; a second-order (Kelvin-wave) calculation, compared
there with the nonlinear runs, estimates the lifetime ratio W/P as eps c, with c = -0.15 and -0.12 at G = 1000 and 3000 for
f = e^{-R^2} and c = +0.34, +0.60 and about +0.8 at G = 1000, 3000 and 10^4 for f = R^2 e^{-R^2} (at eps = 0.3: W/P about -0.045,
-0.036 and +0.10, +0.18, +0.24); within that quadratic frozen-background calculation each single radial Kelvin mode has nonpositive
work, so positive work needs cross-mode terms. The same source reports nonlinear lifetime runs of ring-shaped long-wave modulations at eps = 0.3 and G = 3000 (axial wavenumbers 1/4 and 1/8 of that of the runs above), where the second-order estimate had suggested values above 1/3: the accumulated W/P is 0.31 (wavenumber 1/4) and 0.325 (wavenumber 1/8) at t = 1.5 and 0.313 (wavenumber 1/8) at t = 5, decreasing at the end of both runs; for wavenumber 1/8 the second-order estimate is 0.39 there, larger because the nonlinear production is about 26 per cent above its quadratic value. No isolated column tested at eps = 0.3 reaches 1/3 in these nonlinear runs. At larger amplitude (G = 10^3, ring shape, k = 1; reported, validated there by positivity checks of the circulation along the whole history and one grid comparison, not checked here) W/P at t = 1.5 is 0.225 at eps = 0.6 and 0.88 at eps = 1.0, while 3 W over the accumulated swirl dissipation is 0.0132 and 0.059: up to that time (W/P and 3 W/P = 2.64 at eps = 1.0 compare distinct quantities and are not a conversion efficiency) a cell with an order-one modulation regains only a few per cent of the Sigma it dissipates, which diagnoses the stronger dissipation-normalized condition (ii) of R2.16, not the target inequality of R2.18 (a). These are finite-time values (at t = 1.5 the eps = 1 run still holds 37 per cent of its initial Sigma); no lifetime ratio, amplitude saturation or tail bound is established by them, so they do not show that the required Sigma cannot come from isolated cells. At G = 3 x 10^3 the same source reports (short prefixes only, not checked here) larger early values: 3 W over the accumulated swirl dissipation is 0.158 at t = 0.05 for eps = 0.6, 2.835 times the G = 10^3 value at the same time, and 0.96 at t = 0.00598, the end of the passing prefix (about 1.5 inertial periods), for eps = 1.0; whether the ratio later approaches the small finite-time values observed at G = 10^3, and its lifetime value at G = 3 x 10^3, are undetermined (the recorded history is not monotone). The same source reports (not checked here) that in the first inertial period of such an unforced column, with the ring-shaped modulation at eps = 0.3, the maximum of 3 W over the accumulated swirl dissipation among samples taken every eighth of T_2, attained near t = T_2, is 0.16, 0.51, 1.73, 5.2 and 16.7 at G = 10^3, 3 x 10^3, 10^4, 3 x 10^4 and 10^5, empirically about 1.7 x 10^{-4} G (the stepwise maxima are larger, 2.03 at 0.9475 T_2 for G = 10^4 and 20.6 at 0.945 T_2 for G = 10^5, in a recomputation; the value at 10^4 was confirmed by grid refinement to 0.07 per cent and by an independent second-order computation to 0.2 per cent, and the reconstruction error of the accumulated dissipation is 0.06 to 0.4 per cent for G <= 10^4 but 1.1 and 3.8 per cent at 3 x 10^4 and 10^5), with Sigma(T_2)/Sigma(0) between 1.002 and 1.005 for G >= 10^4; a Gaussian-shaped modulation gives 0.095, 0.37, 1.30 and 3.9 at G = 10^3 to 3 x 10^4, and the dependence on eps beyond 0.6 at G = 3 x 10^3 is not established (the computations at eps = 1 were not resolved well enough). The excess is lost within the next half period and the small lifetime ratios appear only after about ten periods. The growth in G has an elementary explanation (checked here): Sigma = int r q^2 dx is not conserved by the inviscid axisymmetric dynamics, since its weight changes as particles move radially, and in cell units the inviscid evolution of a fixed shape does not depend on G once time is rescaled by 1/G, so if the rescaled inviscid evolution of the data has a positive excursion of relative size of order eps^2 (scaling alone gives Sigma_G(t) = G^2 S(G t) for a fixed shape, not the existence or size of the excursion) and the viscous evolution follows it over that interval, Sigma oscillates with a relative amplitude of order eps^2 independent of G, while the dissipation over one inertial period is about 24 Sigma(0)/G (for the Oseen column Sigma(t) = Sigma(0)(1 + 4t)^{-1/2}, so D = 2 Sigma(0) at t = 0, and T_2 is about 12.1/G). Under that proviso the first-period ratio grows like eps^2 G and records a reversible oscillation, not a trend. So these computations are numerical evidence, for the tested model data, against an unmodified monotonicity or sign estimate bounding the accumulated self-compression by the accumulated dissipation with a constant below 1 over a single inertial period (not a rigorous counterexample, and not on data satisfying every hypothesis relevant to Case 2); they do not prescribe the form of every proof (a corrector, an error term or a different functional is not excluded), and in an environment varying on the inertial time scale an average over many periods can be biased, as in the forced computations of R2.14. It also reports a long-wave modulation of the circulation (relative amplitude 0.3, axial wavenumber 1/8 of the cell wavenumber) imposed on a train of such cells at G = 10^3: the early accumulated self-compression is negative (3 W over the accumulated dissipation -0.60 at t = 0.05, with a resolution check there), as for the long-wave modulation alone, so in that test the long wave acts as one long cell and does not hold the short cells in stretching strain. A related initial-time fact is proved (checked by hand): if eta = 0 at t = 0 and q_0^2 = h_0(R) + sum_{n>=1} h_n(R) cos(n k_0 Z) with every h_n >= 0 (smooth, decaying, Z-periodic), then Pi_s(0) = 0 and Pi_s'(0) = -(1/2) sum_n (n k_0)^2 int R^2 h_n (G_n h_n) dR per unit axial length, which is negative unless every h_n with n >= 1 vanishes; here G_n = (-d_RR - (3/R) d_R + (n k_0)^2)^{-1} is the radial resolvent of the five-dimensional Laplacian, whose kernel is positive. Proof: the meridional velocity vanishes at t = 0, so Pi_s'(0) = -int int (d_t u^R) q_0^2 R dR dZ; d_t eta = d_Z(q_0^2) at t = 0, and with the five-dimensional stream function phi (-(d_RR + (3/R) d_R + d_ZZ) phi = eta, u^R = -R d_Z phi) this gives d_t u^R = R sum_n (n k_0)^2 (G_n h_n) cos(n k_0 Z). The statement is about t = 0 only (ring-modulated columns turn to positive accumulated self-compression within the first inertial period, as above). In the frozen model, in which q^2 is prescribed and independent of time, eta(0) = 0, d_t eta = Delta_5 eta + d_Z(q^2) and the meridional velocity is obtained from eta as above without transport, the same positivity gives the sign for all times (checked by hand): Pi_s(t) = -(1/2) sum_n (n k_0)^2 int R^2 h_n (G_n int_0^t e^{-s L_n} h_n ds) dR per unit axial length for t > 0, with L_n = G_n^{-1}, because the radial heat semigroup e^{-s L_n} also has a positive kernel; so in that model a column whose q^2 has one-signed axial harmonics is expulsive for all time, and steady compression in this frozen model requires at least one nonzero axial harmonic of q^2 to change sign in R (if only the fundamental harmonic is present, that harmonic must change sign; a sign change is not proved sufficient) (a two-profile computation, reported and not checked here, finds such a steady compression at a feasible wavelength, but with a reservoir modulation about seven times the core's, that is with a far circulation varying along the axis in antiphase with the core; it was found at each tested period for a reservoir of four core radii (about 100, 200 and 400 core radii) and at about 200 and 400 but not at about 100 core radii for a reservoir of eight core radii, which establishes the sign at those periods only, not on intervals of wavelengths, and in the full dynamics a datum with uniform far circulation, which is frozen-expulsive, shows a validated early expulsion, 3 W over the accumulated dissipation -0.60 at t = 0.05, followed by small positive values that finer grids could not confirm). The negative cumulative self-compression of R2.4 concerns localized filaments at
G <= 30 and does not extend to such columns, and whether the sign is governed by Rayleigh stability is not established (on the same
reference column it depends on the radial shape of the modulation).
(b) Corollary (the price of renewal; proved by hand from the bounds of R2.10 and R2.12 (i)). Here dx = R dR dZ. Hypotheses: a
perturbation of the Oseen column, axially periodic with period L, smooth at the axis, 0 <= Gamma <= G, the full Cartesian Hessian
bound of (A) normalized as |D^2 u| <= G (it gives |q_Z| <= G; applied to u^theta = q R along a radial ray it gives |q_R| <= G/2,
hence q <= 3G/2 for R <= 1 and q <= G R^{-2} for R >= 1, so int q^2 dx <= (13/8) G^2 L), and core pairing with a bounded test
function phi. Let P_phi(T) = int_0^T int |phi| |d_Z(q^2)| dx dt and D_T = int_0^T int m Gamma_Z^2 dx dt. Since Gamma_Z = R^2 q_Z and
m >= R^{-2}, D_T >= int_0^T int R^2 q_Z^2 dx dt; splitting at R = rho, int_0^T int q_Z^2 dx dt <= G^2 L T rho^2/2 + rho^{-2} D_T;
optimizing in rho and applying Cauchy-Schwarz, P_phi(T) <= C ||phi||_infty G^{3/2} L^{3/4} T^{3/4} D_T^{1/4}. Suppose the
perturbation energy-Casimir functional E~ (A + K for the Oseen column) obeys dE~/dt <= -int m Gamma_Z^2 dx + I(t) between renewal
events, for the same nonnegative functional, domain and reference, with I collecting every term the free column lacks (forcing, jet
Reynolds stress, non-uniform strain, inflow, localization and reference-change terms; transfers between parts of A + K are not
input), and that E~ jumps by J_k = (E~(t_k+) - E~(t_k-))_+ at isolated times (a re-created modulated cell). Then
D_T <= E~(0) + int_0^T I_+ dt + sum_k J_k. Hence band production of the critical size c_1 G^2 L T over T cell times requires
E~(0) + int_0^T I_+ dt + sum_k J_k >= kappa G^2 L T, kappa = (c_1/(C ||phi||_infty))^4, so the cumulative positive input satisfies
int_0^T I_+ dt + sum_k J_k >= [kappa G^2 L T - E~(0)]_+, whether it pumps an existing cell (R2.12 (h), (i)) or re-creates fresh
ones. This is a cumulative lower bound; it prescribes no instantaneous supply rate or renewal frequency.
(c) Reading. (a) is numerical evidence (W compared across three codes, P and W/P not compared; not a certified counterexample, and on data that do not satisfy every hypothesis
of (b)) against a sign law W(t) <= 0 for all t for the accumulated self-compression of an unforced cell on the Oseen column, so an
argument for the missing estimate cannot rest on such a sign without addressing it. (a) does not determine the sign of the weighted
quantity of Theorem 9 (d): with lambda = 3 C_0, int_0^t e^{lambda (t - s)} Pi_s ds = W(t) + lambda int_0^t e^{lambda (t - s)} W(s) ds,
so W(t) > 0 at some t does not make the weighted integral positive (earlier negative values of W can dominate), while W(s) <= 0 for
every s <= t would make it nonpositive. (b) shows that replacing pumping by repeated re-creation does not lower the cumulative supply
requirement. A fresh datum of (a) is out of balance (an order-one swirl modulation with no meridional flow), and a history that
renews its core by re-creation would have to meet the budget of (b); where that input comes from at the core is the same open
question as for pumping ((N1) and realizability, R2.12 (i)).
R2.14 The Z-uniform breathing pump (numerical, linear, prescribed strain history in an idealized unbounded model; solver details and parameter tables are not given, so all numerical statements of R2.14 are model-level estimates; computed
here; the nonlinear values of (c) come from a separate computation whose specification is not reproduced here; where its diagnostics were recomputed here from its records this is said where they are used, and nothing else from it is checked). (a)
Model. Cell units. The Burgers column sits in the axisymmetric irrotational strain u^R = -a(t) R/2, u^Z = a(t) Z, with a(t) = a_0 +
beta Omega(t) cos(d phi(t)), phi' = Omega(t) = (s_1 + s_2)(k_m(t)) G k_m(t), k_m(t) = e^{-a_0 t}, where s_j(k) G k are the two
largest m = 0 inertial frequencies of the column Gamma = G (1 - e^{-R^2}) at axial wavenumber k (frozen inviscid spectrum; s_1 =
0.5309, s_2 = 0.2996 at k = 1, as in R2.12 (h)); so Omega is the drifting sum frequency of the material mode of initial wavenumber
1 on the steadily strained column, the reference wavenumber k_m labels the forcing and not the computed mode, and d is a detuning
factor; a_0 = 4. With A(t) = int_0^t a, the Lagrangian radius r = R e^{A/2} and the axial wavenumber k = k_0 e^{-A} of a material
Fourier mode, the base Gamma_0 = G (1 - exp(-r^2/(4 s))) with s' = e^A, s(0) = 1/a_0 = 1/4 (the squared physical core radius B = 4
s e^{-A} obeys B' = 4 - a B, B(0) = 1) is an exact Navier-Stokes solution for every smooth a(t), with pressure (a'/4 - a^2/8) R^2 -
(a' + a^2) Z^2/2 + int_0^R Gamma_0^2 rho^{-3} d rho up to a function of time. It is an unbounded affine strain with quadratic
pressure around a column whose energy per unit length diverges logarithmically, not a finite-energy flow. The linearized
axisymmetric perturbation of one material mode (circulation, azimuthal vorticity and stream function) obeys a linear system in (r,
t) with time-dependent coefficients. Exactly, A(t) - a_0 t = (beta/d) [sin(d phi(t)) - sin(d phi(0))], and with phi(0) = 0 (the convention of the computations made here), A - a_0 t = (beta/d) sin(d phi):
the log-stretch oscillation has amplitude beta/d.
(b) Linear results (fixed-step fourth-order Runge-Kutta, second-order finite volumes on 0 < r < 10 with 400 cells, regular at the
axis, homogeneous conditions at the outer boundary, which is fixed in material radius and so moves in physical radius; time step
10^{-5}; G = 5000 unless stated; seed X = gamma/r^2 = e^{-r^2} at k_0 = 1, that is circulation perturbation gamma = r^2 e^{-r^2},
with no initial meridional perturbation; E is proportional to the axially averaged perturbation kinetic energy per unit physical
axial length. Quoted values are the largest sampled E/E(0), samples spaced 0.0002 cell times, in the last 0.003 cell times up to
and including the stated time; at G = 5000 and t = 0.04 that window spans between about half a forcing period (d = 0.3) and 3.5 periods (d = 2), 2.2
periods at d = 1.27 (fewer at later times, since the chirp lowers the frequency, and more at larger G). Since E/E(0) does not change when the seed is scaled, large values are amplification factors, not absolute
production.) (i) Unforced (beta = 0): E/E(0) = 0.63 at t = 0.04 and 0.19 at t = 0.1. (ii) Detuning scan at beta = 0.2, t = 0.04:
growth by 2.1 x 10^4 to 2.4 x 10^7 at d = 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8 and by 1.4 x 10^6 to 3.8 x 10^7 at d = 1.2, 1.25,
1.3; at d = 0.85, 0.9, 0.95, 1.05, 1.1, 1.15, 1.4, 1.6, 1.8, 2.0 the value at t = 0.04 is at most 1.4, after early transients
(largest sample before t = 0.04: 22 at d = 1.15, 15 at d = 1.4, 6.8 at d = 0.85, at most 4.6 at the others); at d = 1, the sum
frequency itself, 0.74 at t = 0.04 and 0.71 at t = 0.1 (unforced 0.63 and 0.19; at beta = 0.35 and d = 1 a transient to 9.1 at t =
0.037 and 1.8 at t = 0.1). The principal parametric resonance lines 2 s_n G k lie at d = 2 s_n/(s_1 + s_2) = 1.2785, 0.7215,
0.5009, 0.3833 for n = 1 to 4 at k = 1 (eigenvalue computation of the frozen m = 0 frequencies, s_3 = 0.2080, s_4 = 0.1592); on
the unmodulated column the first ratio drifts from 1.2785 to 1.2953 by t = 0.1, so a fixed d follows such a line only
approximately, and the frequencies of the breathing profile itself differ from these reference values. A signed probe of the
circulation perturbation near r = 0.5 over 0.03 < t < 0.04 (an independent check) gives response to forcing frequency ratios
0.5002 (beta = 0.05, d = 1.27), 0.5001 (beta = 0.2, d = 1.27) and 0.5001 (beta = 0.2, d = 1, initial wavenumber 2): over that
short window (about 3.7 response cycles at d = 1.27 and 2.9 at d = 1) the response is consistent with a response at half the forcing frequency (a short-window estimate; persistent locking is not shown). So the leading band, near d =
1.28, is consistent with principal parametric resonance at twice the first inertial frequency, and the low-d growth lies near the
corresponding lines of n = 2 to 4; but the low-d range also contains higher-order resonance locations of the leading mode
(1.2785/m = 0.64, 0.43, 0.32 for m = 2, 3, 4), and there the log-stretch amplitude beta/d is not small (0.67 at d = 0.3, against
0.16 at d = 1.27), so the low-d bands are not classified. The tested sum-frequency cases, s_1 + s_2 (d = 1) and s_1 + s_3 (d =
0.89: 0.41 at t = 0.1), give no large amplification for k_0 = 1 up to beta = 0.2 by t = 0.1; other resonance mechanisms are not
excluded. (iii) The 2 omega_1 band (d = 1.27), E/E(0) at t = 0.1: G = 5000: beta = 0.02: 0.67 (largest sample 2.7 at t = 0.043,
then decline); 0.03: 10.2 (11.9 at t = 0.081, then decline); 0.05: 1821; 0.1: 1.8 x 10^8. G = 3000: beta = 0.03: 3.1 (3.4 at t =
0.072); 0.05: 52; 0.1: 4.9 x 10^4. G = 1000: beta = 0.05: 1.3; 0.1: 10.2; 0.2: 671. On the 2 omega_2 band (d = 0.72, G = 5000):
beta = 0.02: 0.30; 0.05: 184; 0.1: 2.6 x 10^7. So, for this seed, detuning and interval, at G = 3000 and 5000 beta = 0.03 gives
transient amplification followed by decline and beta = 0.05 gives continuing growth through t = 0.1; at G = 1000 the corresponding
change lies between beta = 0.05 and 0.1. No sharp or asymptotic threshold is established. The initial strain amplitudes beta (s_1 +
s_2) G at beta = 0.03 and 0.05 are about 125 and 208 at G = 5000 and 75 and 125 at G = 3000 (cell units). The initial column of
circulation G has Frobenius Hessian up to 1.495 G (about 4500 and 7500 for G = 3000 and 5000 in cell units); at core width B(t) the maximum
scales as 1.495 G B(t)^{-3/2}, and the affine strain adds none, so a fixed Hessian bound for the evolving column and perturbation over the
interval needs a separate check, which was not made. (iv) Checks at d = 1.27, beta =
0.05, t = 0.1: 1821 with 400 cells at time steps 10^{-5} and 5 x 10^{-6}, 1818 with 600 cells on 0 < r < 14 and 1809 with 800
cells on 0 < r < 10 (both at 5 x 10^{-6}), a spread of 0.7 per cent; at d = 1.2, beta = 0.2, t = 0.04: 1.433 x 10^6 with 400 cells
at both time steps and 1.432 x 10^6 with 600 cells on 0 < r < 14. In an independent check the meridional energy computed from the
identity e^{-A} Re int conj(P) H r^3 dr (P = psi/r^2, H = eta) differs from the diagnostic used here by at most 1.5 per cent at
400 cells and 0.4 per cent at 800 cells over the run at d = 1.27, beta = 0.05. (An earlier version quoted 1762 against 1821 for
the first check; that difference came from the end time being included in the sampling window in one run and not in the other, and
all values in (b) were regenerated with consistent inclusion.) (v) Other wavenumbers, chirp still following the sum frequency of
the mode of initial wavenumber 1, d = 1, beta = 0.2: the modes of initial wavenumber 2 and 3 grow to 2.3 x 10^9 and 2.5 x 10^9
E(0) by t = 0.1, and over the short window of the probe of (ii) the wavenumber-2 mode responds near half the forcing frequency: a forcing that does
not resonate with one material wavenumber can fall in a principal band of another. (vi) Fixed frequency (no chirp): the forcing
frequency is held at 2 s_1 G, the 2 omega_1 line of wavenumber 1 at t = 0 (d = 1.2785 with Omega fixed at its initial value), and
the mode of initial wavenumber 1.3, whose 2 omega_1 drifts down through that line near t = ln(1.3)/4 = 0.066, is computed. At G =
5000 and beta = 0.05 nothing grows (0.025 E(0) at t = 0.15, unforced 0.055); at beta = 0.1, 0.15 and 0.2 the energy, between 0.4
and 1.6 E(0) at t = 0.04 to 0.05, rises during the passage to largest samples 413, 1.7 x 10^5 and 6.0 x 10^7 E(0) at t = 0.088 to
0.101 and then falls (56, 3.0 x 10^4 and 1.2 x 10^7 at t = 0.15); at G = 3000 and beta = 0.1 it rises from 0.43 (t = 0.04) to 37
(t = 0.090). The mode of initial wavenumber 2 passes the same line near t = ln(2)/4 = 0.17 and gains a factor of about 250 (from
0.043 E(0) at t = 0.15 to 11 E(0) at t = 0.196; beta = 0.1, G = 5000). So in this model, at beta of about 0.1 and above
(log-stretch amplitude about 0.08), no frequency tracking is needed for transient amplification: an oscillation at a fixed frequency sweeps the bands of
successive material wavenumbers, and the two tested ones (initial wavenumbers 1.3 and 2) gain by a large factor during a passage of a few
hundredths of a cell time (tens of periods), the first then declining after its passage; no statement for every wavenumber is made.
(vii) Untuned broadband strain (same linear model, computed here; the energy ratios quoted in (vii) are sampled values at the stated times, not the window maxima defined at the start of (b)). Replacing the forcing by a(t) = a_0 + sigma Omega(t) xi(phi),
xi = (2/J)^{1/2} sum_j cos(d_j phi + theta_j) with J = 400, d_j uniform in [0.64, 3.84] (half to three times the line d = 1.2785) and
theta_j uniform random phases (so sigma Omega is the root-mean-square of the oscillatory strain), gives at G = 5000 and t = 0.1: E/E(0) = 0.031 and 12 at
sigma = 0.1 (two random draws of the frequencies and phases), 9.4 and 746 at sigma = 0.15 (and, to t = 0.2, 1.9, 181, 0.038 and 0.010 for four further
realizations), 1.0e3 and 3.1e4 at sigma = 0.2; at G = 20000, sigma = 0.05 decays in both realizations and sigma = 0.1 grows in one
(8.7e3) and turns from decay to growth in the other; at G = 1000 the endpoints are 0.94 at sigma = 0.2 (late slope positive), 3.3 and 2.8 at 0.3 and 95.5 at 0.5. Halving the
time step (checked at G = 5000, sigma = 0.2, one realization) changes none of the printed values. So in the linear model a narrow frequency tuning is not needed: a spatially uniform multitone strain with random frequencies and phases, spread over
half to three times the line frequency, gives E/E(0) > 1 at the stated endpoints in one of two realizations at rms 0.1 Omega, in four of six at 0.15 Omega (at their endpoints, t = 0.1 for two and t = 0.2 for four; three of six exceed 1 at t = 0.1) and in both at
0.2 Omega (G = 5000), the rms values 0.15 and 0.2 Omega being about 7.1 and 9.4 times the rms 0.021 Omega of the tuned forcing at beta = 0.03 (transient amplification followed by decline, (iii)); the outcome depends
strongly on the realization (at 0.15 Omega the six endpoints, two at t = 0.1 and four at t = 0.2, span 0.010 to 746). Endpoint amplification occurs in some draws at every sigma sampled in the twelve-draw ensembles below (sigma = 0.2 to 0.5 at G = 1000, 0.1 to 0.2 at G = 5000 and 0.05 to 0.1 at G = 20000), although the single earlier draw at sigma = 0.2 for G = 1000 (0.94) and both earlier draws at 0.05 for G = 20000 (0.31 and 0.031) ended below 1. No empirical break-even of the long-time growth rate has been determined (the heuristic estimate below gives a break-even sigma proportional to G^{-1/2}; an endpoint comparison over twelve draws follows it). No
spectral criterion has been established for the pumping of the drifting column by the multitone forcing simulated here (the frozen-coefficient results stated below do not cover it). In record units the rms values 0.15 to 0.2 Omega are about 0.12 to 0.17 k C_* delta_n at
G = 5000. The band also contains sums omega_i + omega_j of two distinct inertial frequencies of the column at the same axial wavenumber (d = 1 is the sum frequency of the first two modes, omega_1 + omega_3 lies at d = 0.89, and the sums omega_1 + omega_j accumulate at d = s_1/(s_1 + s_2) = 0.639 as j grows, since the m = 0 inertial frequencies accumulate at zero; 2 omega_2 lies at d = 0.72). In a weak-noise stochastic averaging description such pair (three-wave) parametric resonances can contribute at order sigma^2, as the subharmonic resonance of the first mode does. Their coherent couplings are small: in the modal reduction of this linear model (eigenfunctions psi_j normalized in the energy, S_ij their Gram matrix in L^2(r^3 dr)) the coherent coupling per unit amplitude of the oscillatory axial log-stretch (whose time derivative is the oscillatory axial strain) is h_j = (3/4) omega_j (1 - k^2 S_jj) for the subharmonic resonance of mode j and h_ij = (3/4) k^2 (omega_i omega_j)^{1/2} |S_ij| for the pair (i, j); at k = 1 the pair-to-first-subharmonic ratios are 0.097 (1, 2), 0.053 (1, 3), 0.035 (1, 4), 0.042 (2, 3), 0.027 (2, 4) and 0.023 (3, 4), against 0.64, 0.47 and 0.36 for the subharmonic resonances of the second, third and fourth modes (per unit relative strain amplitude beta of (a), whose log-stretch amplitude at frequency d is beta/d, each coupling is divided by its own resonant frequency in units of Omega, (omega_i + omega_j)/Omega or 2 omega_j/Omega, and the ratios become 0.12 for the pair (1, 2) and 1.14 for the second mode). These numbers were reproduced here by rerunning the separate modal computation at k = 1 and G = 3000 at two radial resolutions (its omega_j/(G k) agree with the values of s_1 and s_2 above to four significant digits); the matrix-element formula was taken from that computation and not rederived here, and these are coherent couplings. In the frozen-coefficient mean-energy formula (N-C) of the same computation, quoted below (stationary weak noise, fixed modal frequencies; its channel sum was checked here algebraically, not rederived), the coefficient of the strain spectral density at omega_1 + omega_j (one-sided, per unit angular frequency in time) in the growth rate of the mean first-mode energy is, at leading order and without the broadening, 4 pi h_1j^2/(omega_1 + omega_j)^2 for the pair (1, j) (at a damping difference gamma_j - gamma_1 > 0 the channel samples a Lorentzian-broadened S_F, not S_xi, near omega_1 + omega_j, and a complex coupling product adds a dispersive term), which is 0.77, 0.29 and 0.14 per cent of the mean-energy first-subharmonic coefficient (9 pi/8)(1 - k^2 S_11)^2 for j = 2, 3 and 4 (checked here: the ratio is half the square of the strain-normalized coupling ratio, 0.1245 for the pair (1, 2), squared 0.0155); pairs not containing the first mode do not enter the first-mode rate at this order, and no typical-energy coefficient of a distinct-mode pair is established (the typical rate of the coupled system is only bounded above by the mean rate). The typical-energy subharmonic coefficient of the j-th mode taken alone, (9 pi/16)(1 - k^2 S_jj)^2 = 4 pi h_j^2/(2 omega_j)^2 (identity checked here), is 1.30 times that of the first for the second mode; the damping-rate ratio of the second to the first mode is 2.7 in the loss accounting of the same computation on the Burgers base (3.16 for the frozen operator) and 2.58 to 2.71 here (unforced decay of single-mode seeds of this linear model, the inviscid eigenfunctions at k = 1, with energy decay rates 20.6 to 21.0 for the first mode and 53.8 to 55.7 for the second over subintervals of [0, 0.03], at G = 3000 and 5000 and two radial resolutions, ratios taken on matched subintervals), so that, if the isolated-mode weak-noise balance between damping and this growth applies, the threshold strain spectral density of the second mode is about 2.0 to 2.1 times that of the first (2.43 with the frozen dampings). Status of that formula (reported from the same separate computation, where independent checks confirmed it after corrections; checked here as stated below). For frozen coefficients (fixed base width, no Burgers drift) and a log-stretch epsilon F(t), the noise classes there are: F a real, nonzero, centred observable of a stationary irreducible finite-state continuous-time Markov chain (the chain class), or the output of a linear filter with Hurwitz matrix driven by such an observable (the filtered class); S_F is the one-sided spectral density of F and S_xi(z) = z^2 S_F(z) the normalized strain spectrum (in the chain class xi = F' is impulsive, not a mean-square derivative; the strain epsilon xi has spectrum epsilon^2 S_xi). (N-A) (both classes) For one complex mode, z' = (-gamma + i omega) z + epsilon F(t)(alpha z + beta conj z) with omega > 0 and beta != 0, there are epsilon_0 > 0 and C such that for |epsilon| <= epsilon_0 and every z(0) != 0, almost surely every limit point of t^{-1} log|z(t)|^2 lies within C |epsilon|^3 of -2 gamma + pi epsilon^2 |beta|^2 S_F(2 omega), and the lower and upper exponential rates of the mean of any positive definite quadratic energy lie within C |epsilon|^3 of -2 gamma + 2 pi epsilon^2 (|beta|^2 S_F(2 omega) + (Re alpha)^2 S_F(0)). For the affine one-mode approximation of the first mode of the column with the leading inviscid coupling |beta| = (3/2) omega_1 (1 - k^2 S_11), the typical-energy bounds are centred at -2 gamma_1 + alpha_1 epsilon^2 S_xi(2 omega_1), with alpha_1 = (9 pi/16)(1 - k^2 S_11)^2; the cubic remainder does not control the error of this approximation to the column. (N-C) (chain class only) For the Galerkin truncation of the column to N inviscid modes, writing A(h) = A_0 + h A_1 + h^2 A_2 + O(h^3) for the Galerkin matrix at log-stretch h (analytic in h), if the first eigenvalue pair of the damped matrix A_0 is simple and less damped than every other eigenvalue by a gap (verified numerically there for N up to 12 only), there is a real-analytic s(epsilon) = -2 gamma_1 + epsilon^2 s_2 + O(epsilon^3) such that, for every c > 0, initial data with |ell_1 x_0| >= c |x_0| > 0 (ell_1 and e_1 the corresponding left and right eigenvectors of A_0, normalized by ell_1 e_1 = 1, and the first-mode energy |ell_1 x|^2) have mean first-mode energy with exponential rate s(epsilon), provided |epsilon| <= epsilon_1(c) and the chain is stationary; for all other nonzero data s(epsilon) is an upper bound for the mean, and for every initial condition and every initial law of the chain, almost surely limsup t^{-1} log |x(t)|^2 <= s(epsilon). Here s_2 contains a variance term (Var F) d_2, with d_2 = 2 Re(ell_1 A_2 e_1), the zero-frequency and self-resonance terms, and all sum-frequency and difference-frequency channels. The quoted theorems give no typical-energy formula for distinct-mode pairs; the pair coefficients stated above are the leading terms of the sum-frequency channels omega_1 + omega_j of s_2. (N-D) (both classes) For one block with C^1 coefficients on [0, T], z' = (mu(t) + i nu(t)) z + epsilon F(t)(alpha(t) z + beta(t) conj z), with nu bounded below by a positive constant and beta(t) != 0, and every z(0) != 0, exactly log|z(T)/z(0)| = int_0^T (mu + epsilon^2 (pi/2)|beta|^2 S_F(2 nu)) dt + B_T - M_T, where M_T is a square-integrable martingale with mean zero and |B_T| is at most twice the supremum of a frozen-coefficient corrector of order epsilon plus T times bounds on the time derivatives of the correctors and on a remainder of order epsilon^3; so for such a block the exponential of the expected value of log(|z(T)|^2/|z(0)|^2) is exp(int_0^T (2 mu + pi epsilon^2 |beta|^2 S_F(2 nu)) dt) up to the factor e^{2 E B_T}, the passage form used below, while the scatter of the realizations about it is not small in general. Checked here: the leading coefficients of (N-A), by a formal second-order averaging computation in the frame rotating at omega; the column value of |beta| (3089.69 at G = 5000 and k = 1 in that computation, 3089.55 on a finer radial grid, and 3089.59 from (3/2) omega_1 (1 - k^2 S_11) with its unrounded values, against 3089.5 from rounded inputs); the identity for one complex mode (real dimension 2) s_2 = 4K + 4K_0 + (Var F) d_2, with K = (pi/2)|beta|^2 S_F(2 omega) and K_0 = (pi/2)(Re alpha)^2 S_F(0), which reduces to the mean-energy coefficient of (N-A) for the affine family of (N-A) (A_2 = 0, so d_2 = 0; in the column d_2 = -24.4 at G = 5000 and k = 1 in that computation); the decomposition of (N-D) (the frozen corrector identity and Dynkin's formula; its corrector bounds were not rechecked); and the passage from the mean bound to the almost-sure upper bound (Chebyshev's inequality and the Borel-Cantelli lemma at integer times, with bounded growth between them). The proofs were not otherwise rechecked. Not covered: the untruncated column (perturbations far from the core decay at the bare viscous rate k^2, slower than gamma_1; in the unweighted energy space the essential spectrum of the frozen operator, in the Fredholm sense (which for this non-self-adjoint operator is stable under relatively compact perturbations), is (-infinity, -k^2], since its coupling terms are relatively compact with respect to the viscous part (each, composed with the resolvent of the viscous part, is a coefficient decaying away from the core times a function of the viscous operator vanishing at infinity, hence compact; checked here), so that, by products of Weyl sequences, the essential spectrum of the second-moment generator at zero noise contains (-infinity, -2 k^2], hence -2 gamma_1, and the isolated-eigenvalue perturbation argument does not apply; the Rayleigh-weighted case was not determined), the drifting base (the frozen amplitude dampings of the first two modes, 7.86 and 24.8 at k = 1, omit the strain work and width drift of the Burgers base, which the measured rates above include; at t = 0 the separate computation gives instantaneous energy decay rates of about 21.002 (mode 1; terms 15.725, about 1.28 and 4.00) and 55.763 (mode 2; terms 49.685, about 2.08 and 4.00), the three terms being the viscous quotient of the inviscid seed, the loss through the time dependence of the energy metric of the frozen modes along the drift (rerun here) and a_0 = 4 from the time-dependent stretch prefactor carried by the meridional kinetic part of the physical energy, against the finite-window rates 20.35 to 21.24 and 53.8 to 55.7 measured here; this is a consistency at one instant, not an error bound, and these terms do not correspond one by one to the strain work and width drift named above; (N-D) holds for one block with C^1 coefficients, with small error terms when they vary slowly, but the reduction of the drifting column to one such block, with its conjugate coupling, leakage to other modes, second-order term in the log-stretch and drift of the material width, is not proved), nonzero band-limited strain spectra (not realized in either class), and finite multitones such as the forcing of these runs. The estimate below is therefore outside every proved case. A heuristic consistency estimate (not a spectral criterion, and outside the stationary fixed-frequency setting of that formula): with Omega frozen and averaged over the frequency draws and phases, the multitone has one-sided strain spectral density sigma^2 Omega/3.2 in time (variance (sigma Omega)^2 spread uniformly over a band of width 3.2 Omega), so the first-subharmonic coefficient alpha_1, the frequencies and the first-mode energy decay rate 2 gamma_1, all evaluated along the reference path k = k_m(t) = e^{-a_0 t} (which ignores the oscillatory part of the log-stretch), give a heuristic local rate alpha_1 sigma^2 Omega/3.2 - 2 gamma_1 for the typical energy, with alpha_1 = 1.06, 1.18 and 1.28, Omega/G = 0.83, 0.70 and 0.59 and 2 gamma_1 = 20.35 to 21.24, 19.53 to 19.87 and 18.75 to 18.99 at k = 1, e^{-0.2} and e^{-0.4} (t = 0, 0.05 and 0.1; finite-window decay rates of single-mode seeds started at these wavenumbers, measured as above, at k = 1 for G = 1000, 3000, 5000 and 20000 and at the other two for G = 5000 and 20000, with differences between G = 5000 and 20000 of at most 0.23 on matched subintervals at these two wavenumbers). Its zero gives a heuristic break-even sigma of 0.12 to 0.13 at G = 5000, about 0.06 at G = 20000 and 0.27 to 0.28 at G = 1000 (it scales as G^{-1/2}, so the break-even rms strain sigma Omega scales as G^{1/2}; in the frozen estimate averaged over the random frequency draws it is the one-sided strain spectral density 2 gamma_1/alpha_1 at 2 omega_1, about 19.1 to 20.0 at k = 1 and 14.6 to 14.8 at k = e^{-0.4} in cell units, strain and angular frequency both measured in cell rates, approximately independent of G in the runs tested, G = 1000 to 20000), each within the sampled range of sigma, where the outcomes are mixed; no empirical break-even of the long-time growth rate has been determined. For this non-modal seed, as a further unproved ansatz, the gain exp(int_0^{0.1} alpha_1 sigma^2 Omega/3.2 dt) (Simpson's rule on the three values) multiplies the unforced energy ratio of the same seed at t = 0.1 (0.182, 0.158 and 0.144 at G = 1000, 5000 and 20000, computed here). This gives 0.51, 1.9 and 116 at G = 1000 and sigma = 0.2, 0.3 and 0.5 (observed 0.94, then 3.3 and 2.8, then 95.5); 0.58, 2.9 and 28 at G = 5000 and sigma = 0.1, 0.15 and 0.2, where the observed values at t = 0.1 (0.031 and 12; 0.27, 0.28, 0.29, 2.0, 9.4 and 746; 1.0e3 and 3.1e4) spread over about 1.5 to 3.4 orders of magnitude, with geometric means (the sample analogue of the typical energy) 0.62, 2.6 and 5.6e3, and at sigma = 0.2 both values exceed the estimate, by factors of about 37 and 1100 (the two draws at sigma = 0.2 are the same frequency and phase draws as the two largest of the six at sigma = 0.15, 9.4 and 746 at t = 0.1, so they come from draws that were favourable at sigma = 0.15 and need not be typical at sigma = 0.2; the unproved extrapolation 0.1582 (R/0.1582)^{16/9}, with R = E(0.1)/E(0) at sigma = 0.15, 0.1582 the unforced ratio and 16/9 = (0.2/0.15)^2 as in the weak-noise form, gives about 220 and 5.4e5); and 0.52 and 25 at G = 20000 and sigma = 0.05 and 0.1 (observed 0.31 and 0.031, then 0.37 and 8.7e3). Ensembles of twelve draws (draw indices 0 to 11, the same draws at every sigma and including the draws above; T = 0.1) give geometric means of E(0.1)/E(0) of 0.41, 0.90, 5.2 and 30.5 at G = 1000 and sigma = 0.2, 0.3, 0.4 and 0.5 (estimate 0.51, 1.9, 11 and 116; E(0.1) > E(0) in 4, 5, 9 and 11 of the 12 draws), 0.76, 1.6, 6.9 and 72 at G = 5000 and sigma = 0.1, 0.125, 0.15 and 0.2 (estimate 0.58, 1.2, 2.9 and 28; 6, 6, 8 and 10 of 12) and 0.43, 3.1 and 77 at G = 20000 and sigma = 0.05, 0.075 and 0.1 (estimate 0.52, 2.6 and 25; 3, 10 and 11 of 12), the standard error of the sample mean of log(E(0.1)/E(0)) being 0.41 to 1.07. A least-squares line through these sample means against sigma^2 (free intercept) has slope 0.021 G, 0.031 G and 0.035 G at G = 1000, 5000 and 20000, against 0.0258 G in the estimate (marginal 5 to 95 per cent bootstrap ranges, resampling the twelve draws jointly over sigma: 0.014 G to 0.029 G, 0.022 G to 0.040 G and 0.025 G to 0.045 G), and the sigma at which the fitted geometric mean equals 1 is 0.295, 0.108 and 0.062 (ranges 0.23 to 0.34, 0.08 to 0.13 and 0.053 to 0.070), against 0.257, 0.120 and 0.061 from the estimate. The slope and crossing of the estimate thus lie within these marginal ranges at each G (with the intercept fixed at the unforced ratio instead, the G = 1000 slope range, 0.0153 G to 0.0256 G, narrowly excludes the estimate); the fitted crossing decreases by a factor of 4.8 from G = 1000 to G = 20000 (4.2 in the estimate), while the fitted slope per unit G increases by a factor of about 1.65. These are exploratory comparisons based on twelve draws and descriptive linear fits in sigma^2 on a finite horizon; they do not establish the full endpoint curve or a scaling law in G. The four earlier runs to T = 0.2 at sigma = 0.15 and G = 5000 give at t = 0.1 values within 0.86 per cent of the corresponding ensemble runs to T = 0.1 (the grids on which Omega and the strain are tabulated depend on the horizon). The mean tone spacing 3.2 Omega/J (the d_j are random) is 5 to 7 at G = 1000, 24 to 33 at G = 5000 and 95 to 133 at G = 20000, against an amplitude decay rate gamma_1 of about 10, so at G = 5000 and above the tones sample the resonance sparsely on the scale of the damping rate, a possible source of the strong realization dependence there (not established). Coherent forcing at the two pair sums tested in (b)(ii) (d = 1 and 0.89) gave no large amplification for k_0 = 1. A channel-separation run used six independent random draws per band at G = 5000 and T = 0.1, with full-band reference amplitude sigma = 0.2 and sub-band amplitude sigma ((d_hi - d_lo)/3.2)^{1/2} on a sub-band [d_lo, d_hi], where xi is now the unit-rms multitone of the same form with the d_j uniform in [d_lo, d_hi], so that the forcing (amplitude times xi) has the same ensemble spectral density in the phase variable phi of (a) as the full-band forcing (Omega drifts, so this is not a stationary spectral density in time). On the sub-band [1.05, 3.84], which contains 2 omega_1 and no sum of two distinct positive m = 0 inertial frequencies at this k, E(0.1)/E(0) > 1 in four of six draws (3.02 to 221 among those four), and the least-squares slope of log E over [T/2, T] ranges from -33.6 to 83.6 (positive in four draws, three draws satisfying both criteria). On the sub-band [0.64, 1.05], which contains 2 omega_2 and those sums omega_1 + omega_j (j >= 2) that lie at or above d = 0.64, this slope lies between -27.1 and -19.0 in all six draws, against -20.3 unforced (energy ratios at T = 0.1 from 0.133 to 3.0 against 0.158 unforced; the draw ending at 3.0 reached 13 at t = 0.04). At 7.8 times that spectral density the lower sub-band alone grows strongly (energy ratios 8.4 x 10^5 to 3.3 x 10^9 at T = 0.1 in three draws); the subharmonic resonance of the second mode is a candidate driver suggested by the couplings above, but these runs do not distinguish its contribution from that of the pair sums. So at these parameters and the matched spectral density the upper sub-band produced endpoint amplification in four of six draws and the lower sub-band in one of six (with negative late slopes in all six of its draws); these independent samples do not determine the contributions of individual resonances to full-band growth. This says nothing about saturation, about the ring supplier of (d), or about delivery.
(c) Reported from a separate computation, not reproduced here, used only as model-level evidence, and checked only where its diagnostics are said to be recomputed (nonlinear axisymmetric computation in the same material coordinates, same forcing, seeds in both circulation and meridional flow). Its numerical diagnostic for E~ omits the available-potential-energy integrand where the reference circulation is within e^{-20} G of G and keeps the kinetic part throughout the computational domain. For some of the runs quoted below (not all: for example not the control with only the modes 0 and +-1 kept) that computation checked the omitted part at the saved final checkpoint of each run checked; intermediate fields were not saved. That check evaluates the available-potential-energy integrand with the circulation ratio Gamma/G replaced by 10^{-14} where it is smaller and by 1 - 10^{-14} where it is larger, in the omitted and the retained region alike. At those checkpoints, excluding the fixed-frequency run at log-stretch amplitude 0.157, whose only saved state lies after its numerical blow-up, the omitted available-potential-energy contribution is smaller in absolute value than 10^{-4} times the absolute value of the retained one, and that region carries less than 10^{-15} of each of two grid sums: the squared swirl perturbation (the circulation deviation divided by the squared radius) weighted by the radius, and the squared perturbation of eta weighted by the cubed radius, both in the material coordinates of that computation (a rerun of that check here gives the same values). Several of these checkpoints come after failures of the circulation or pointwise-q checks, and none of them bounds the omitted part at the earlier quoted times. The omitted part need not be small in general (for the linearized frozen column at G = 3000 and axial wavenumber 1, the separate computation reports, not checked here, that the initial state of largest growth over half a cell time of the ordinary perturbation kinetic energy, swirl plus meridional, carries about three quarters of its initial swirl kinetic energy in that region; this is a kinetic-energy fraction, not a measured fraction of the omitted available potential energy). That computation later audited its runs against the circulation
maximum principle (0 <= Gamma <= G for these data) and the pointwise cap q <= 2G of the cap window, and withdrew every figure from the
developed (saturated) states: there Gamma/G leaves [0, 1] (down to -0.16 to -0.89, up to 1.19) and q exceeds the cap by factors 10 to
35, so those states violate the circulation maximum principle of the model (a numerical failure) and the pointwise cap of the cap window. What remains, within the phases reported to pass the circulation and pointwise-q checks (other hypotheses not checked): at d = 1.27,
beta = 0.05 (log-stretch amplitude 0.039, G = 5000) the functional E~/E~(0) grows to 338 (period maximum; 336 at the first sample past the cap; mean logarithmic rate log 338/0.0708 = 82 per cell time) when q first exceeds
2G (t = 0.0708; Gamma/G stays in [0, 1] to t = 0.08), with cumulative 3 int Pi_s = +0.031 Sigma_ref(0) and core swirl integral 1.09 times
the reference there; two reported radial and axial resolutions give, for example, E~/E~(0) 155 and 156 at t = 0.06 (other values were not compared here;
the linear value of (b) at t = 0.06 is 192, but (b) measures the perturbation kinetic energy and this is a truncated numerical diagnostic of the energy-Casimir functional, so the two
are not a quantitative linear-nonlinear comparison). At d = 1 there is no growth at beta = 0.1 and 0.15; at beta = 0.2 the gain at the first sample above the cap (t = 0.0756) is 88 (91 at the last sample below it, maximum 118 before the cap), attributed by
that computation to the nonlinearly generated mode of twice the initial wavenumber (with only the modes 0 and +-1 kept, no sustained growth: largest value of E~/E~(0) 1.83 and value 0.67 at t = 0.1, in line with the absence of net amplification at t = 0.1 in (b)(ii)); at G = 3000, d = 1.2, beta = 0.2 the gain at the first sample above the cap (t = 0.0402) is 3936 (3955 at the last sample below it, maximum 3989 before the cap), and at G = 1000 with the same forcing the whole run passes those two checks, with gain 135 by t = 0.1. Growth was also
reported at d = 0.5, 0.8 and 1.2 (the fastest near d = 1.2) and none at 1.5 and 2.0 (not retained as cap-valid evidence, since their valid time intervals are not specified). With
the forcing frequency held fixed (no chirp) the same seeds give at most 4.2 E~(0) at log-stretch amplitude 0.039 (passing both checks
throughout) and 328 E~(0) at the first sample above the cap (t = 0.0132; 337 at the last sample below it, maximum 360 before the cap) at 0.157, in line with (b)(vi). The same computation reports that
log(E~/E~(0)) <= 3 int a_- (R2.15 (b)) holds at every sample of these runs, with a margin of at least a factor 1.7 in the exponent over the admissible samples with E~ > E~(0) of the two G = 5000 runs for which the ratio was recomputed (the action integrated from at least 6 samples per forcing period: 6 to 7 at G = 5000, about 10 to 30 at G = 3000 and 1000). Connecting the linear amplification to nonlinear swirl production and
to the supply requirement of R2.13 (b) needs separate evidence; within the phases reported to pass the circulation and pointwise-q checks the accumulated self-compression stays
a few hundredths of Sigma_ref(0).
A later run of the same computation (G = 3000, d = 1.27, log-stretch amplitude 0.047, seeds as above, chirped forcing over about 94 cycles to t = 0.3, the forcing frequency and strain amplitude falling to about a third of their initial values over the run) passes the circulation and pointwise-q checks at every recorded sample (Gamma/G in [1.8e-5, 1], q_max/(2G) in [0.48, 0.85]). Its diagnostics were recomputed here from the run records (not with an independent solver; a second model audited the same records and the solver source and found the same values): E~/E~(0) peaks at 1982 at t = 0.233 and is 1089 at t = 0.3 (sample value; the maximum over the last full forcing period, which has lengthened to about 0.0057 under the chirp, is 1197); the core swirl integral averages 1.021 times the reference over [0.15, 0.3] (peak 1.057) and the swirl integral over the whole computational domain 1.009 times; the cumulative 3 int Pi_s over the whole computational domain is +0.0254 Sigma_ref(0) at t = 0.3, accumulating at 0.16 to 0.17 Sigma_ref(0) per cell time over [0.1, 0.2] and [0.15, 0.3]. A second resolution (400 radial and 96 axial points against 275 and 48) changes E~ by at most 0.9 per cent, the swirl-integral ratios by at most 1.1e-3 and the cumulative self-compression by at most 1.7e-4. The turnover after t = 0.233 is consistent with a loss of resonance (tracking error) rather than a saturation inside the two checks: the chirp does not track the evolving wavenumber exactly (the ratio of the forcing frequency to twice the first inertial frequency of the frozen reference falls from 0.993 to 0.950) while the strain amplitude weakens, and a rerun at the same log-stretch amplitude whose phase is advanced at twice the first inertial frequency computed for the current axial wavenumber and core width (otherwise the same computation; diagnostics recomputed here from its records) grows monotonically, with E~/E~(0) equal to 279, 2845 and 8881 at t = 0.1, 0.15 and 0.2 against 159, 636 and 1618 for the chirped run (growth rate about 50 per cell time over [0.05, 0.15]), and leaves the pointwise-q class at t = 0.153 (q_max = 2G; circulation outside [0, G] from t = 0.188); at t = 0.153 the core swirl integral is 1.087 times the reference, the whole-domain one 1.038 times, and the cumulative whole-domain 3 int Pi_s is +0.035 Sigma_ref(0), accumulated at 0.63 Sigma_ref(0) per cell time over [0.1, 0.153]. So no saturated pumped state satisfying the two checks was found in this family: the long phase of the chirped run is an episode limited by imperfect tracking. With the forcing removed at t = 0.3 the functional decays at about 17 per cell time and the swirl integrals return to within 2e-3 of the reference over [0.45, 0.5] (1.0001 at t = 0.5; cumulative self-compression +0.020 Sigma_ref(0)); no lasting excess is measured. The same holds for the tracked run at G = 1000, log-stretch amplitude 0.1, with the forcing removed at t = 0.4 (E~/E~(0) about 2000 there): decay at about 17 per cell time and the swirl integrals back to within 4e-4 of the reference at t = 0.6 (recomputed from the records); the swirl dissipation over the whole computational domain after switch-off was reported to equal that of the strain-held reference column to within a few per cent (not recomputed here). A rerun of that tracked case with the forcing kept on to t = 0.8, its phase carried through the restart (diagnostics recomputed here from its record), stays inside both checks (circulation in [0, G], q_max at most 0.784 of the pointwise cap); the running maximum of E~/E~(0) over the last 0.01 cell time is 29, 391, 1459, 2039, 1435, 517, 166 and 39 at t = 0.1, 0.2, ..., 0.8. The energy peaks at 2059 E~(0) at t = 0.377 and then decays with the forcing still on, at about 11 per cell time over [0.42, 0.8] and 12 over [0.5, 0.8], while the oscillating strain amplitude, locked at fixed log-stretch amplitude to the falling frequency of the stretched core, drops from about 78 at t = 0.1 to about 25 at t = 0.4 and about 10 at t = 0.6; the cumulative whole-domain self-compression is +0.016 and +0.030 Sigma_ref(0) at t = 0.42 and 0.8. In a reduced two-mode model of the stretched core, with coupling proportional to k d omega/dk, a forcing of fixed log-stretch amplitude has a finite supercritical window (estimated to end near t = 0.42 at G = 1000 with log-stretch amplitude 0.1, and near 0.51 and 0.60 for the G = 3000 and G = 5000 runs above), because the coupling of the stretched mode decays; this estimate was not recomputed here; the G = 1000 rerun above turns over between t = 0.38 and 0.42, consistent with it, and the G = 3000 and 5000 windows were not tested. This window concerns a core seeded at one axial wavenumber. In a computation reported and not checked here, the same cell model, seeded at 160 axial wavenumbers with random phases and driven by the axis strain history of a ring pair of half the tuned impulse on the mean stretching a_0 = 4 (axial stretch factor 1.54 over 60 exchanges), showed no closing of the resonance window over the run (60 exchanges): the resonant physical wavenumber stays fixed while the stretching carries material wavenumbers through it, and the energy settles in a sub-cap oscillation well below the cap (the maximum of q at most about 0.6 of the pointwise cap; of order 1 per cent of the cap-level energy of that box), with negligible signed self-compression (+0.0003 Sigma_ref(0) over 0.118 cell times). So the turnover of the single-wavenumber runs is not evidence of a finite window on a long core; at that forcing strength it is replaced by a plateau without signed production. For a forcing of fixed strain amplitude the log-stretch amplitude (strain amplitude over forcing angular frequency) grows as the core's frequency falls and the reduced coupling does not decay. A run of this kind (G = 3000, oscillating strain amplitude fixed at 50 around the mean a_0 = 4, phase advanced at twice the first inertial frequency of the current wavenumber and core width, log-stretch amplitude rising from about 0.016 (50 over the initial frequency 3185), below the onset 0.035 to 0.047 found at fixed log-stretch amplitude, to 0.039 at t = 0.3; diagnostics recomputed here from its records) stays inside both checks to t = 0.3 (circulation in [0, G], q_max at most 0.571 of the pointwise cap) and grows progressively: the running maximum of E~/E~(0) over the last 0.01 cell time is 1.44, 2.61, 5.28, 11.4, 27.0 and 67.4 at t = 0.05, 0.10, ..., 0.30, at exponential rates of about 10, 15 and 18 per cell time over successive tenths, against the bound 3 times the mean of a_-, about 42 per cell time, of R2.15 (b); the cumulative whole-domain self-compression is only +4.6e-4 Sigma_ref(0) at t = 0.3. So in the one run made in this model an exterior of fixed strain amplitude locked to the core was not limited to one bounded generation of cells up to t = 0.3: its log-stretch amplitude and the growth rate increased throughout, and no stopping mechanism other than the tracking requirement appeared before the run was stopped at t = 0.3 (whether the pointwise check later fails or the log-stretch amplitude ceases to be small was not tested). A breathing uniform in z cannot be produced inside one axial period: averaging (1/r) d_r(r u^r) + d_z u^z = 0 over a period makes r times the period mean of u^r independent of r, hence zero; in a z-periodic model the breathing must therefore be imposed, and in a Case 2 history it would have to come from structure that is not periodic on the cell scale. The decay of the unforced cells is qualitatively consistent with the known asymptotic stability of Burgers vortices under small three-dimensional perturbations at every circulation Reynolds number, with possibly large transient amplification at large Reynolds number (Gallay and Maekawa, Comm. Math. Phys. 2011, arXiv:1002.2489; abstract read, function spaces and the size of admissible perturbations not checked): in the perturbation class and stability neighbourhood of that theorem unforced perturbations decay; the computed cells have not been verified to lie in that neighbourhood, whose size may depend on the circulation and on the norm. The initial column at full circulation G has Frobenius Hessian 1.49 G, so it meets a Hessian bound only when read as a column of circulation G inside a datum whose circulation bound is at least 1.5 G; the Hessian of the pumped state was not monitored. So, in this prescribed-forcing model, breathing near the resonance gives positive signed self-compression of a fraction of Sigma_ref(0) per cell time while it stays in resonance (about a sixth under the imperfectly tracking chirp, about 0.6 with tracking until the pointwise-q check fails), with no retained gain after switch-off; this is model evidence about an externally forced core, not about the coupled record flow.
(d) Scale. With cell length delta, one cell time is tau = G/(C_* delta) record times and record strain is a/tau, so the
oscillating strain has record amplitude beta (s_1 + s_2)(k_m) k_m C_* delta (0.0415 C_* delta initially at beta = 0.05) and record
angular frequency d (s_1 + s_2)(k_m) k_m C_* delta; the log-stretch amplitude beta/d (0.039 at d = 1.27, beta = 0.05) does not
depend on delta. The amplification found takes the record duration T G/(C_* delta), that is 200/(C_* delta) to 500/(C_* delta) for
T = 0.04 to 0.1 at G = 5000 (about 31 forcing periods by t = 0.04 and 71 by t = 0.1 at d = 1.27). On a record time interval of
fixed length an oscillation of record frequency O(delta) completes vanishingly few periods and an O(delta) strain accumulates only
O(delta) log-stretch as delta -> 0; the required duration is of order nu_n^{-1/3} record times for fixed G and C_*, shorter than the persistence window A_max(n) of Theorem 2 for large n, but that the record flow keeps a suitable core and a coherent strain of this kind for that long is not established. The affine strain
has gradient diag(-a/2, -a/2, a) (operator norm |a|) and zero Hessian: it adds nothing to the Hessian of the column, and an
O(delta_n) record amplitude is compatible with a fixed velocity-gradient bound for small delta_n; these spatial bounds neither
prescribe nor exclude its temporal coherence. In the runs beta Omega exceeds a_0 = 4 by far (initially 125 to 208, and about 89 to 148 at t = 0.1, across the tested bracket from beta = 0.03, transient, to beta = 0.05, continuing growth, at G = 5000, as Omega falls from about 4150 to 2960 over 0 < t < 0.1), so a(t) reverses sign every period, and the
proposed one-signed comparison of R2.7 (e), which is unproved, would not apply directly over the complete oscillatory history even if it were proved (the mean stretch stays
positive; estimates on parts of the history are not examined). The channel needs coherence: in the chirped runs the oscillation
follows twice an inertial frequency of the drifting core within the band width (d between about 1.2 and 1.3 at beta = 0.2) for the
growth time, 0.04 to 0.1 cell times, tens of forcing periods; at beta of about 0.1 and above a fixed frequency held for one
passage through the band suffices ((b)(vi)). An exterior oscillator of the required size (heuristic scale analysis with thin-ring kinematics; not a solution). Two coaxial vortex filaments of circulation Gamma_r, centred on the circle of radius s/2 about (R_r, Z_c) and rotating about each other at the leapfrogging angular velocity Omega_r = Gamma_r/(pi s^2) (the point-vortex approximation, s << R_r), induce on the axis the exact filament velocity sum_i Gamma_r R_i^2/(2 (R_i^2 + (Z - Z_i)^2)^{3/2}); at Z = Z_c its axial derivative is -(9 Gamma_r s^2/(8 R_r^4)) sin(2 Omega_r t) to leading order in s/R_r, with mean zero, so the log-stretch amplitude is 9 pi s^4/(16 R_r^4), a function of the geometry alone (direct evaluation over a period agrees with these leading-order values within 3 per cent for s/R_r <= 0.5; 0.03 needs s/R_r of about 0.36). Matching 2 Omega_r to twice the first inertial frequency, 2 s_1 k C_* delta_n = 1.06 k C_* delta_n in record units, fixes Gamma_r = 0.53 pi k C_* delta_n s^2, so the rings are weak (vorticity and energy tend to zero with delta_n for fixed R_r), and the axis signal has the required scalings of size, frequency and gradient (a smooth realization is not verified). Coherence is the restrictive part. Along the axis the pair's own time-mean strain is about -3 Gamma_r zeta/R_r^3 at distance zeta ahead of the centre, so a saturated core, which needs a mean strain within about a_0 of its holding value, must stay within an axial window of width about (3/8)(a_0/A) s^2/R_r around the point where the mean strain has that value (A the oscillation amplitude; about 0.004 R_r for A = 12.5 a_0 and s = 0.36 R_r), and staying there for N breathing periods requires the axial speed of the fluid at the core to match the translation speed of the pair to a relative accuracy of about 3 a_0/(8 pi^2 N A) (about 1e-4 for N = 30 and A = 12.5 a_0), in thin-ring terms a tuning of the ring core radius, which enters that speed logarithmically. A background axial strain of order A could compensate a larger mismatch, but it changes the pair's radius and with it Omega_r by a fraction of order A pi/Omega_r = 2 pi alpha per breathing period (alpha the log-stretch amplitude), well outside the tongue width of a few per cent at the tested amplitudes, so the neighbourhood holding core and pair must be quiet: background velocity gradients there small compared with 0.01 Omega_r/N, so that the frequency drift over N periods stays inside the tongue, that is of order 0.01 k C_* delta_n/N in record units. Within this heuristic the exterior breathing is therefore not excluded by size, smoothness or energy, but it needs a tuned weak structure in a quiet neighbourhood, and nothing here decides whether a Case 2 history can produce one, or a family of them, along the band. A thin-ring computation tests the coherence part (standard thin-core ring model: each ring moves with the circular-filament Biot-Savart field of the other plus the self-induced speed (Gamma/(4 pi R))(log(8R/a_c) - 1/4), core radius a_c with R a_c^2 constant, and a Burgers background u^R = -a_0 R/2, u^Z = a_0 Z acts on the rings and on the fluid; not an Euler solution; reported from a separate computation and reproduced here with an independent code). Two rings of circulation Gamma, radius R_0 and axial separation R_0, with core radius a_c = 7.56e-4 R_0 at R = R_0, exchange at the period 5.40 R_0^2/Gamma, the period of the axis strain signal (angular frequency omega_lf = 1.164 Gamma/R_0^2). With a_0 = 0 an axis fluid point released at the centre of the pair stays within 0.080 R_0 of the moving centre for every period computed, the strain along its path reverses sign for half of each period, int a_- = 0.512 per period (R2.15 allows at most a factor e^{1.54} = 4.6 per period) and the half-range of the log-stretch is 0.26. With a_0 > 0 the rings shrink and their separation stretches, the point drifts behind the centre, where the pair's own mean strain is extensional, and is then left behind: at a_0/omega_lf = 4.3e-4, 1.7e-3 and 6.9e-3 the strain along the path reverses sign during 9, 5 and 3 periods, int a_- per period falling from 0.51 to zero and summing to 3.4, 1.9 and 1.1, and at 1.7e-3 the period mean of the strain along the path is 8 a_0 in the second period and 45 a_0 in the fourth. In a small scan at 1.7e-3, releasing the point 0.15 or 0.3 R_0 ahead of the centre gives at most 7 reversing periods; releasing it behind the centre, or taking a_c = 1e-5 R_0 or separation 1.4 R_0, loses the point within about one period; with a_c = 1e-2 R_0 or separation 0.7 R_0 the point is carried at an off-centre station where the pair's mean strain is compressive throughout (period mean -0.4 to -0.7 Gamma/R_0^2, hundreds of times a_0), which compresses the core instead of making it breathe. Tuned to omega_lf = 2 omega_1, the cell computations above have a_0/omega_lf = 4/3185 = 1.3e-3 (G = 3000, a_0 = 4), a ratio fixed by the cell parameters and independent of n. So in this model a single passive tuned pair gives a bounded number of coherent periods (about five for the centred release, fewer if the secular stretch along the drifting path is allowed to shift the core's frequency, which was not computed) and, for that release, an R2.15 gain bound of about e^{5.7}, about 300, at the scanned ratio 1.7e-3 (at 4.3e-4 the action 3.4 gives e^{10.2}, about 3e4; the cell ratio 1.3e-3 lies between and was not scanned), that does not grow with n (a separately reported prescribed-strain cell computation at the pair's material impulse 0.23, with a pure sinusoid, gives a factor of about 50 in E~ over five periods; not checked here). The strain along the material path is not a pure oscillation: its period mean exceeds a_0 by 0.0017, 0.014, 0.041, 0.089 and 0.194 Gamma/R_0^2 in periods 1 to 5 at a_0 = 0.002 Gamma/R_0^2, an accumulated extra stretch of about 1.9 by period 5 (reproduced here). Driven by the actual strain history along the material path at the cell ratio (separately reported; seed and resolution checks reported, not rerun here), the cells gain a factor 1.2, 2.1, 3.6, 5.6 in E~ at the ends of periods 1 to 4, with a peak of 10.4 in period 5, and the base column, stretched by this mean strain, crosses the interpolation cap in period 5 (by its radial compression, not by the pumping); so for this pair and this release the mean strain, not the window length, is the binding defect. The defect depends on the release: along a passage through the tangency log P' is about 2 gamma zeta (gamma = -2.7 R_0^{-1}), so a path that starts ahead of the centre is compressed first and stretched later; at the cell ratio a_0 = 0.00146 Gamma/R_0^2, releases 0.1 and 0.15 R_0 ahead keep the accumulated excess stretch int (a - a_0) dt between -1.04 and +0.75 and between -1.52 and -0.12 over seven periods, with int a_- per period falling from 0.76 and 0.88 to 0.14 and 0.20 and summing to 3.6 and 4.1 (computed here); the cell response to these histories is reported below (the functional peaks at 6.2 and 4.2 and then decays). A numerically fitted normal form of the material return map, x_{n+1} - x_n = -6.05 a_0 (n + 1/2) - 2.66 x_n^2 in ring units (x the offset from the centre after n exchanges), gives about 0.79 (a_0/omega_lf)^{-1/3} periods before escape, and a longer scan down to a_0 = 5e-7 supports the exponent -1/3 (numerical evidence, not a theorem); the coefficients -2.66 and, at n = 0, -3.03 a_0 (-6.05e-3 at a_0 = 0.002) agree with the period map computed here (-2.7 and -6.3e-3 at a_0 = 0.002). Sustaining the band by this mechanism needs a renewal of independently tuned pairs, of order one every few periods, and nothing above decides whether a Case 2 history supplies such a sequence. Two exact facts sharpen this. First, for any smooth axisymmetric velocity field with a globally defined axis flow (for instance with bounded axial velocity gradient on the axis) that is periodic in time with period T in a frame translating along the axis: axis fluid points move with the axial velocity on the axis, a one-dimensional equation, so their period map P in that frame is an increasing diffeomorphism of the line; hence for an axis point whose orbit stays bounded in that frame the stroboscopic positions P^n(z) converge to a fixed point of P (the continuous trajectory approaches the corresponding periodic orbit) (an increasing homeomorphism of the line has no periodic orbits of period greater than one), at a fixed point log P' is the integral over a period of the axial strain a along the periodic orbit, and a fixed point that attracts the releases on one side of it has that integral at most zero. So a trapped axis point that is stretched over each period, which is what holding means here, sits at a repelling fixed point, which traps only its own orbit (there may be several such points), while an open set of releases can only be trapped at a point that is not stretched on average. Second, for axisymmetric Euler flow, with or without swirl, in a uniform background strain u^r = -S(t) r/2, u^z = S(t) z, with perturbation vorticity of finite absolute impulse (int r^2 |eta| dx < infinity) and enough decay that the weighted fluxes arising in the differentiation of I vanish (compactly supported vorticity suffices; decay of the velocity alone does not, since psi = (1 + r^2 + z^2)^{-7/5}, eta = -Delta_5 psi gives finite energy but eta of order rho^{-24/5} > 0 and int r^2 eta dx = infinity): the axial impulse I = (1/2) int r^2 eta dx satisfies dI/dt = -S I, because the source d_z(q^2) of eta contributes (1/2) int r^2 d_z(q^2) dx = 0, the background radial velocity contributes -S I, and the self-induced part vanishes by the kinematic identity int r u^r eta dx = 0 that underlies conservation of impulse for axisymmetric flow. So in a constant nonzero strain no configuration of nonzero impulse is time-periodic, even in a translating frame, and a leapfrogging pair necessarily drifts.

In the ring model the period map shows the structure behind the windows. With a_0 = 0 and separation R_0 the centred point lies close to a tangency, P(zeta) - zeta being about -3.4e-5 R_0 - 2.7 zeta^2/R_0 near the centre, so there is no fixed point and the point only passes slowly; at separations 0.95, 0.9 and 0.8 R_0 there are two fixed points, a repelling one behind and an attracting one ahead of the centre, at about 0.14, 0.19 and 0.23 R_0 from it, images of each other under the reflection and time-reversal symmetry of the pair, so that the strain history on one is minus the time reverse of that on the other; at 0.9 R_0 the repelling orbit is stretched by a factor e^{1.06} per period and its strain reverses for 13 per cent of each period. The holding strain moves the pair through this family toward the tangency. The repelling orbit, where a held core would sit, therefore keeps the core longer than the centred release, but still for a bounded number of periods. At a_0 = 0.002 Gamma/R_0^2 and separation 0.85 R_0 (a_0/omega_lf from 1.3e-3 to 1.6e-3 over the window; the orbit computed by integrating the axis point backward in time, in which the repelling orbit attracts), the strain along it first reverses in period 8, int a_- per period passes 0.1 in period 15 and reaches 0.54 in period 22, while the period mean of the strain falls from 0.29 to 0.014 Gamma/R_0^2 (145 a_0 to 7 a_0), the strain amplitude stays near 0.41 Gamma/R_0^2 and omega_lf falls from 1.50 to 1.27 Gamma/R_0^2; the orbit leaves the pair between t = 120 and 136 R_0^2/Gamma (periods 26 to 29), and int a_- is 3.1 over the first 22 periods and about 4.4 through period 25 (the last periods are affected by the end condition of the backward computation). At a_0 = 0.0005 Gamma/R_0^2 and separation 0.9 R_0 the same rise of int a_- per period, from 0.009 to 0.18, takes four to five times as many periods as at a_0 = 0.002, consistent with a window proportional to omega_lf/a_0. So for a fixed strain ratio the window of a passive pair is bounded independently of n; on the repelling orbit it is longer, about 11 periods with int a_- above 0.1 at the cell ratio, but it comes after a strong mean stretch: the strain integrated along the orbit is 8.3 after 7 periods, 16.1 when int a_- first exceeds 0.1 per period and 18.3 after 22 periods, so a saturated core sitting there would have been stretched through the interpolation cap (crossed at an accumulated stretch of about 2 in the computation above) long before its reversal window opens. Combining the lemma with the requirement used above that a saturated core see a period-mean strain within about a_0 of its holding value gives the following heuristic picture: a held saturated core can only sit near a nearly neutral fixed point of the period map, |log P'| of order a_0 T or less; in a family of maps drifting with the strain such points occur only near a tangency, where the two fixed points at distance (alpha/|gamma|)^{1/2} from it have log P' = -+2 (alpha |gamma|)^{1/2} to leading order for P(zeta) - zeta = alpha + gamma zeta^2, so they exist with the required near-neutrality for a parameter range of width of order (a_0 T)^2/|gamma|, crossed in a fraction of a period, after which the passage through the tangency gives the window of order (omega_lf/a_0)^{1/3} periods found for the centred release. The genericity of the tangency and the drift rate are assumed, not proved, and the frequency drift (about 15 per cent over the repelling window above) and the renewal question remain.
Free pair. Without background strain (a_0 = 0) the pair of the ring model is periodic in a frame translating with it to the accuracy of the integrations over the computed exchanges (exact relative periodicity is not proved here), and with the core size tuned the period map of its centre is numerically tangent to the identity (with the core used above the maximum of P(zeta) - zeta is -3.4e-5 R_0; a second integration with the core tuned further reports -1.6e-13 R_0). The axis point released at the centre then has strain integral zero over each exchange to two decimals for twelve exchanges and compression integral 0.51 per exchange (0.512 in three independent integrations, which also agree on the exchange period 5.3999 R_0^2/Gamma and on the maximal axis excursion 0.081 R_0 from the centre). Releases ahead of it approach it slowly with net compression (accumulated strain integral -1.9 and -2.9 after twelve exchanges for releases 0.05 and 0.1 R_0 ahead), and releases behind leave with net stretch (+2.0 after twelve exchanges for 0.02 R_0 behind; lost after about seven exchanges for 0.05 R_0 behind), which is consistent with a semi-stable fixed point of the period map (the lemma above does not give the rate of approach). With time scaled so that the exchange frequency equals 2 omega_1 of the k = 1 mode of the Oseen column Gamma = G (1 - e^{-R^2}) at G = 3000 (3185 per cell time, so one exchange lasts 0.002 cell times), this history multiplies the energy of the linearized column by about 2.0 per exchange (3.1e3 after twelve exchanges; changed by less than 10 per cent by an added uniform strain of 4 per cell time and not at all by halving the time step; still 1.5 to 2.3 per exchange at frequency ratios 0.9, 0.95 and 1.05, so in the linear model the frequency tolerance is wide), below the factor exp(3 x 0.51) = 4.6 per exchange that R2.15 allows for E~ (a different functional, so this compares sizes only). In the nonlinear cell model (one run, not repeated independently; its linear growth is the one just reproduced) the same history gives E~/E~(0) = 2398 after twelve exchanges with the circulation in [0, G] and the maximum of q at most 0.83 of the interpolation cap, and it crosses the cap at exchange 12.8, 0.025 cell times after the start, with 3 int Pi_s = 0.040 Sigma_ref(0) at the last sample below the cap (0.041 at the first sample above it); the Oseen spreading of the core over this time lowers 2 omega_1 by 4.6 per cent and the pumping continues through this drift without any frequency adjustment (this is one run of a strong short pump, not a measured tongue width). In the same model a pump to at least 500 times the initial functional within thirteen exchanges needs the relative core size of the pair within about -3e-3 to +3e-4 of the tuned value and the release point within about -0.006 R_0 to +0.008 R_0 of the centre (accumulated strain integrals 2.35, 0.85, -0.59 and -1.05 for releases at -0.02, -0.01, +0.01 and +0.02 R_0); outside these windows the failure is the net stretch or compression, not the oscillation. Across 0.015 R_0 the strain differs by up to 30 per cent of the oscillation amplitude, so the axially uniform cell model describes sub-packets of the entrained fluid, not a blob of size 0.1 R_0. For the pair in the holding strain at the cell ratio a second identical passage after a gap of one to two exchanges multiplies the functional again (by 4.7 to 13.5, depending on the phase), but the cap is crossed during the second passage in every case tested, at an accumulated axial stretch of about 0.85 in the runs tested, so the gain compounds but the admissibility does not renew; releases 0.10 and 0.15 R_0 ahead of the held pair stay below the cap for six exchanges but the functional peaks at 6.2 and 4.2 and then decays, because the compression dilutes the column and changes the mode. So the tested thin-ring family contains numerically tuned trajectories that supply this channel, with one tuned parameter of the pair, a release point near its centre and no mean strain, and the pumping episode ends at the interpolation cap, not by loss of coherence: in the model a tuned free pair can pump an entrained core only until the cap is reached, which from the seed used takes about thirteen exchanges (a model-level reading; that the actual flow could not continue the episode would need estimates for the coupling and for the approximations made). Exact neutrality (a tangency of the period map to the identity) would be a codimension-one condition in the model family under a nondegeneracy condition that is not verified here, but finite-duration near-neutral behaviour occupies an open set of parameters, of the sizes just given. In record units the tuned pair has Gamma = 0.913 C_* delta R^2 (R the ring radius, from 1.1636 Gamma/R^2 = 2 omega_1 = 1.062 G nu/delta^2 = 1.062 C_* delta) and core radius 7.56e-4 R, so its velocity, velocity gradient and Hessian are about 192 C_* delta R, 2.5e5 C_* delta and 3.4e8 C_* delta/R; by these scale estimates they are within |u| <= 1, |grad u| <= 1 and |grad^2 u| <= C_* when 3.4e8 delta <= R <= 1/(192 C_* delta) and 2.5e5 C_* delta <= 1, which holds for delta below about 3.9e-6 min(C_*^{-1/2}, C_*^{-1}), so it is no restriction as delta_n -> 0 (these are scales of the chosen profiles, not certified bounds; the base column itself needs a circulation margin of about 1.5 for the Frobenius Hessian: the full-circulation column of the cell runs has record Hessian about 1.495 C_*, so embedding a column of circulation g needs a circulation parameter G_tot >= 1.495 g, with further margin for its evolution, and the record conversions and cap tests would then use G_tot in place of g; no full admissibility check was made). The energy of the pair, of order C_*^2 delta^2 R^5, is small near the lower end of the admissible interval of R but not uniformly over it (at the upper end it grows like C_*^{-3} delta^{-3}). Two caveats remain. First, the pair is far larger than the cell (R >= 3.4e8 delta) and samples the record flow over its own scale. In the ring model with the exact irrotational background u^Z = h Z^2/2 - h r^2/4, u^r = -h r Z/2 (axis strain h Z, zero at the initial centre of the pair; h in units of Gamma/R_0^3; a local model, since this background is unbounded at large distances) the release at the tuned centre does not stay neutral. The pair translates along the strain gradient (about 61 R_0 in thirteen exchanges) and its impulse changes: for any axisymmetric vorticity in a background potential flow u^Z = w(z) - r^2 w''(z)/4, u^r = -r w'(z)/2 with w quadratic, the impulse I = (1/2) integral of (omega^theta/r) r^2 dx obeys dI/dt = -a I - h J for w'(z) = a + h z, with J = (1/2) integral of z (omega^theta/r) r^2 dx (finite absolute first moments and vanishing fluxes assumed as above), that is, when I is not 0, dI/dt = -w'(Z_I) I, where Z_I = J/I is the axial centroid with weight r^2 (omega^theta/r), because omega^theta/r is transported (in the swirl-free model; with swirl the source d_z(q^2) contributes zero, as shown above), the self-induced flow conserves I, and w' is affine (the ring computation reproduces this to 1e-9, an independent one to 1e-13); the identity holds for Navier-Stokes as well, because the viscous term nu (d_rr + (3/r) d_r + d_zz) of the equation for omega^theta/r integrates to zero against r^2, given regularity at the axis and vanishing of the weighted fluxes r^3 d_r(omega^theta/r) and r^3 d_z(omega^theta/r) at infinity. Here I/I_0 = 0.979 and 1.021 after thirteen exchanges at h = +1e-5 and -1e-5, and the centre point is either lost behind with net stretch (h > 0) or carried forward with net compression (h < 0), as in a frozen-map reading in which the tangency splits. The modulus of the accumulated strain integral along it at the end of an exchange (within an exchange it swings by the compression integral 0.51 even for the free pair, so all strain counts in this passage are taken at exchange ends) first exceeds 0.5 at exchange 3 to 4, 4 to 5, 6, 7 to 8 and 10 for |h| = 1e-3, 3e-4, 1e-4, 3e-5 and 1e-5, alike for both signs, and the background strain contributes 2 to 6 per cent of it for |h| <= 1e-4 and up to 19 per cent at |h| = 1e-3; over this range the windows are fitted by 0.56 |h|^{-1/4} exchanges (a short-range fit; the fitted exponents are 0.26 for h > 0 and 0.20 for h < 0), which is the scaling the tangency normal form behind the a_0^{-1/3} law gives when the splitting grows quadratically in time (through the impulse drift) instead of linearly (a heuristic reading, not derived). Computed directly, the window of h around 0 in which the strain integral stays at most 0.5 in modulus at the ends of all thirteen exchanges is -3.0e-6 Gamma/R_0^3 < h < 2.6e-6 Gamma/R_0^3, that is, in record units, for this background and this release, an axial strain gradient between -3.0e-6 x 0.913 C_* delta/R and 2.6e-6 x 0.913 C_* delta/R, so between about -8.1e-15 C_* and 7.0e-15 C_* along the path of the pair (the last step uses R >= 3.4e8 delta; the window is narrower for larger R); releases or cores re-tuned to the drifting background were not searched, so this is a measured sensitivity, not a necessary bound for every background history. In the potential background the radial curvature of the axial velocity is tied to the axial one (d_rr u^Z = -h/2); an independent radial curvature was tested in the exact steady background u^Z = W_2 r^2, u^r = 0 (uniform omega^theta/r = -2 W_2, so the problem stays invariant under axial translation, omega^theta/r minus its background value is transported by the total flow, and the background only changes the tuning). With the core re-tuned, the period map is again tangent to the identity and the accumulated strain integral at the centre point stays below 0.01 in modulus for thirteen exchanges at W_2 = -0.1, -1e-2, -1e-3, 1e-3 and 1e-2 Gamma/R_0^3 (tuned core sizes 0.31, 0.89, 0.989, 1.011 and 1.12 times the value for W_2 = 0; at W_2 = +0.1 the re-tuning scan used found no tangency, so the positive range was not determined). With the core kept at its W_2 = 0 value, thirteen exchanges survive at |W_2| = 1e-4 Gamma/R_0^3 (accumulated strain integral 0.29 in modulus) but not at 3e-4 (first exceeding 0.5 at exchange 10 for W_2 > 0 and 11 for W_2 < 0) or 1e-3 (exchange 6 for both signs). So the constant part of this component is absorbed by the one tuned parameter of the pair, and for the core kept at its W_2 = 0 tuning the constant-offset tests give a sensitivity scale of about 2e-4 Gamma/R_0^3 (between 1e-4 and 3e-4; a static sensitivity, not a necessary bound on a change of W_2 during an episode, and time-dependent changes were not tested), about 70 times the coefficient tolerance for the axial strain gradient (velocity derivatives differ from these coefficients by factors such as d_rr u^Z = 2 W_2) (an independent integration gives the same fixed-core window, 6 exchanges at W_2 = 1e-3). An axial dependence of it was computed independently in the prescribed kinematic background u^Z = (beta_0 + beta_1 Z) r^2, u^r = -beta_1 r^3/4 (zero axis velocity and strain; not a steady Euler flow), with the tuned core and the centre release (reported, not repeated here): the strain integral first exceeds 0.5 in modulus at exchange 13, 9, 6, 4 and 3 for |beta_1| = 1e-5, 3e-5, 1e-4, 3e-4 and 1e-3 Gamma/R_0^4, with almost no impulse drift (I/I_0 = 0.9996 at 1e-5), the mechanism being the differential axial push beta(Z_i) R_i^2 on the two rings; so thirteen exchanges need |beta_1| below about 1e-5 Gamma/R_0^4, about 8e-23 C_*/delta in record units at the smallest admissible R (a third derivative of the velocity, which (A) does not bound). Two further independent integrations of the same model reproduced these windows (10, 7, 6, 4 and 3 exchanges at h = 1e-5, 3e-5, 1e-4, 3e-4 and 1e-3 in both, and 10, 8, 6, 5 and 4 at the negative values in one) and the impulse law. Second, a core held against Oseen spreading by a mean strain of the survival size, a_0 = 4 per cell time (1.46e-3 Gamma/R^2 at the conversion above), puts the pair into the drifting family above, with its shorter window and mean-strain defect, provided the holding strain acts on the pair as a uniform background (a holding flow confined near the core was tested only in the thin-ring model, with two small opposite coaxial rings ahead of and behind the centre, of strength giving the survival strain there; it gives transient holding that depends strongly on the placement: placed 0.2 or 0.3 R_0 from the centre, the rings are moved apart by the pair's own oscillating axial strain, of amplitude about 0.27 Gamma/R_0^2, within one or two exchanges and push the centre point off the tangency, and placed inside the neutral window they hold longer, but in both cases the contracting small ring leaves the thin-core regime (core-to-radius ratio 1.44 at exchange 2 for one placement at 0.2 R_0, about 1 by exchange 11 inside the window), so these computations establish no lifetime of localized holding in either direction; no holding is needed during one episode of 0.025 cell times, so between episodes the holding must be approximately uniform, renewed after each episode, or supplied otherwise). Computed in the ring model with the uniform background u^Z = a_0 Z, u^r = -a_0 r/2 acting on the pair and the centre point released as above, the pair-induced accumulated strain at that point first exceeds 0.5 in modulus at exchange 10, 7, 5 and 4 for a_0 = 1e-4, 3e-4, 1e-3 and 1.46e-3 Gamma/R^2, close to 0.47 (a_0 R^2/Gamma)^{-1/3} exchanges (the a_0^{-1/3} law); for compression along the axis (a_0 < 0) the windows are 11 and 7 exchanges at |a_0| = 1e-4 and 3e-4, and at |a_0| = 5e-5 they are 12 (a_0 > 0) and 13 (a_0 < 0) exchanges, and the direct boundary for a_0 > 0 is a_0 = 3.9e-5, so thirteen exchanges need |a_0| below about 4e-5 Gamma/R^2. (Reading the core-size window above through the impulse law, with cores of fixed volume, would give 6e-6 to 6e-5; the direct count is the upper value, because a detuning that grows during the episode costs less than a fixed one.) Since the survival strain is about 4.4/G in these units, a pair acting on a held core keeps its window for about 0.29 G^{1/3} exchanges (a fit): four at G = 3000, and thirteen only near G = 1.1e5 (the direct boundary at the survival strain). At G = 3000 the holding strain must therefore fall to about a thirty-seventh of the survival value (a_0 <= 3.9e-5 Gamma/R^2, about 3.6e-5 C_* delta in record units) during an episode of thirteen exchanges; in the one nonlinear cell run above, which includes the Oseen spreading, a single episode of 0.025 cell times reached the cap without mean strain, but heuristically a core that keeps producing at the cap over many cell times needs one on average. Duty cycle (heuristic; one G, one seed, one mode, figures of the nonlinear run). The weighted production of R2.15 (c) over the episode is about 6.3e-3 G^2 L, dominated by the last one or two exchanges, where its rate is about 0.92 G^2 L per cell time; after an episode the state decays at 11 to 27 per cell time. A chain of episodes, each restarting from a level F below the cap, keeps cells at the near-cap rate for a fraction of the time between about 0.0065 (F = 5000, the seed) and 0.04 (F = 4). In record units such a cell produces about 0.92 G C_* nu_n per unit record length and time (integrated record production is nu_n times integrated cell production, so per unit record length and record time the factor is nu_n^2/delta_n^3 = nu_n C_*/G, using G nu_n = C_* delta_n^3), so over a band of duration of order 1/nu_n a record length L_z of cells producing at that rate for a fraction f of the time gives about 0.92 f G C_* L_z, and a requirement of order m_phi/P (the Scale reading of R2.16) needs f of order 1/(G C_* L_z), about 4e-4/(C_* L_z) at G = 3000. Counted per episode instead, with the production of one episode above, j_ep G^2 per unit cell length (j_ep = 6.24e-3), a requirement c_0 over a band of duration K/nu_n is met if every axial point of a record length L_z of saturated core is pumped at least once every j_ep G C_* L_z K/c_0 cell times, which is 18.7 to 187 cell times at G = 3000 for C_* between 1 and 10 and L_z K/c_0 = 1 (a coverage frequency at axial points). In the cell model this spacing is roughly independent of G for episodes of a fixed number of exchanges: with the pair's history rescaled to the exchange frequency 2 omega_1(G) at fixed strain impulse, each exchange takes 2 pi/(1.06 G) cell times and the mean unsigned production rate is about 0.25 G^2 L per cell time at G = 3000 and 0.23 to 0.31 G^2 L per cell time at G = 10000, so j_ep is roughly proportional to 1/G at a fixed number of exchanges per episode (reported runs, not recomputed here); the number of exchanges to the cap itself depends on G and on the impulse (above). In the same runs the energy growth per exchange at fixed strain impulse (the quantity converged in time step and sampling) depends only moderately on G (least-squares gains 1.73, 2.05 and 2.12 per exchange at G = 1000, 3000 and 10000 for strain impulse 0.233, and 2.12, 1.70 and 1.47 at G = 10000 for impulses 0.233, 0.159 and 0.116), while the Oseen drift of the core per exchange is proportional to 1/G (1.2, 0.4 and 0.12 per cent at G = 1000, 3000 and 10000), so in these tests the strain impulse needed to reach the cap decreases as G grows (not shown to be a universal monotone threshold): with single-wavenumber seeds the cap is reached at impulse 0.233 for G = 3000 and 10000 but not for G = 1000, and at 0.116 only for G = 10000 (interpolated crossings at G = 10000 after about 11.85, 16.74 and 22.74 exchanges for impulses 0.233, 0.159 and 0.116; the first converged in time step, output cadence and radial resolution, where the coarse sampling had given 12.67, the other two unchanged under a finer output cadence); an episode that reaches the cap gives signed self-compression 3 int Pi_s of about +0.03 to +0.04 Sigma_ref(0) at the last sample below the cap (G = 3000: +0.040 at the original sampling and +0.041 at a finer one, converged in time step and sampling to 2 per cent; G = 10000: +0.033, +0.035 and +0.032 for the three impulses at the finer sampling, the last two within about 1 per cent of their values at the original sampling, while for impulse 0.233 the original sampling had given +0.057), comparable across G but not a scaling law. The linear computations above are consistent with this trend (at the tuned detuning the change from transient amplification to continuing growth through t = 0.1 lies between beta = 0.05 and 0.1 at G = 1000 and between 0.03 and 0.05 at G = 3000 and 5000, (b)(iii)). Conditional on these saturated states, yields and resets, and on the conversion of these model diagnostics into the adjoint-weighted supply that Case 2 needs (not shown), the production count would ask only for a small occupancy fraction and would not limit this channel, given saturated cores, seeds and tuned exterior structures along the band. Excluding the channel would need a statement that a Case 2 history cannot contain tuned exterior structures at that rate, or the failure of another ingredient (held saturated cores, seeds, or the compatibility of the exterior structures and their surroundings with the record bounds); nothing proved here addresses these. In the runs reported for these models (not repeated here) no episode stopped below the cap at a producing level: weaker tuned pairs, or the same drive scaled down in amplitude, give a transient growth that ends when the Oseen spreading of the core has lowered the frequency ratio to about 0.91 to 0.93, with signed self-compression below 0.003 Sigma_ref(0); the free pair's strain history scaled down to strain impulse 0.116 (the fundamental amplitude of the axial strain at the centred axis point divided by its angular frequency; 0.233 for the tuned pair above) detunes before reaching the cap, as does the tuned pair at the closer separation 0.6 R_0 (impulse 0.087, peak energy gain about 30), while the tuned pair at separation 0.8 R_0 (impulse 0.159) reaches it after about 20 exchanges and the pair above (impulse 0.233) reaches it; the scaled histories and the tuned pairs at different separations are different families, so these runs bracket a cap-reaching threshold only within each family (between 0.116 and 0.233 for the scaled history, between 0.087 and 0.159 for the tuned pairs; single-wavenumber seeds, G = 3000). These runs seed a single axial wavenumber. On a long core seeded at 160 axial wavenumbers with random phases (total amplitude 1 per cent; one seed realization) the amplification passes from the seeded wavenumber to its neighbour as the core spreads (the resonant wavenumber drifted by 35 per cent over 60 exchanges; time-resolved spectra show a clean hand-over from the seeded mode, dominant to exchange 20, to the next one, dominant from exchange 24, and later an alternation between two neighbouring modes rather than a continued walk), each mode gaining while it stays in resonance: at impulse 0.116 the per-mode gain over about 30 exchanges was e^{10.4}, the peak energy was about 6 per cent of the cap level of the long core (about 1.5 per cent on the strained column), and the signed self-compression was about 0.001 Sigma_ref(0); whether the window on a long core is finite was not determined (these runs end at 0.118 cell times); and at impulse 0.233 the cap was reached after 17.7 exchanges (12.8 with the single-wavenumber seed of 16 times larger amplitude per mode). At G = 1000 the same strong pump with broadband seeds did not reach the cap through 40.5 exchanges (a finite discrete broadband seed; peak energy 405 times its initial value, about 9 per cent of the cap level); there the drift of about 1.2 per cent per exchange limits each mode's residence in resonance to 8 to 10 exchanges. In the same runs the unsigned source mass ||d_z(q^2)||_1 is, to leading order, linear in the modulation amplitude (for q = q_0 + eps f, d_z(q^2) = 2 eps q_0 f_z + 2 eps^2 f f_z): per unit length a 1 per cent random-phase seed gives about 5 per cent of the rate of a core held at the cap, and a 10 per cent random-phase modulation with no pump gives about the cap-held rate for one to three exchanges, 0.4 of it over exchanges 3 to 6 and 0.1 by exchanges 15 to 20, as the rough modes diffuse. So unsigned production is first order in the modulation, but sustaining it needs renewal of the modulation against diffusion, on admissible histories and over the held-core measure; the adjoint pairing of this production was not measured. The pump's own signed self-compression replaces 29 per cent of the column's swirl dissipation up to the last admissible exchange and 96 per cent at the cap, and averaged over a chain at the rate above only 0.1 to 1 per cent. This is not a further constraint. By R2.16, Case 2 forces 3 int Pi_s >= (1 - o(1)) int D_Sigma whatever the mechanism (the production bound of Theorem 9 (b), ||d_z(q^2)||_1 <= D_Sigma and the Sigma identity), so the swirl that held cores dissipate between episodes must be regained by other compression, in the record frame by the sourced strain that holds them (first reading of R2.16; per unit length the Burgers column compresses three times what it dissipates), not by the pump. The low ratio restates that the channel needs held saturated cores over the measure of the Scale reading of R2.16. Sliding material. Material that slides through an exterior pattern, instead of being trapped by it, is not subject to the period-map obstruction above, but the pattern tested is fragile in another way (from a separate computation; the identity checked here by hand, the ring-row instability reproduced here in three runs). If the axis velocity U(Z, t) = u^z(0, Z, t) is steady in a frame of constant velocity W_p, U = W_p + v(Z - W_p t), and v does not vanish along the path of a material axis point, then zeta = Z - W_p t obeys zeta' = v(zeta) and the axial strain along the path is a = v'(zeta) = (log |v(zeta)|)', so int_0^T a dt = log(v(zeta(T))/v(zeta(0))): for a spatially periodic pattern the accumulated strain returns to zero at each traversed period, with no tuning of the mean (over other windows an endpoint term of modulus at most log(max |v|/min |v|), extrema over a spatial period, remains, and the identity concerns the signed strain only, not its negative part or the spreading of the core). Without steadiness, write w(zeta, t) = U(zeta + W_p t, t) - W_p in the moving coordinate; if w does not vanish along the path, zeta' = w and d/dt log|w(zeta(t), t)| = (d_t w)/w + a with d_t taken at fixed zeta (in laboratory coordinates (d_t + W_p d_Z) w), so int_0^T a dt = log(w(zeta(T), T)/w(zeta(0), 0)) - int_0^T (d_t w)/w dt, which again controls only the signed strain. A periodic row of identical thin coaxial rings is such a pattern in the thin-ring model (a relative equilibrium); for rows whose axis fluid is not trapped (spacing below about 1.8 to 2.2 ring radii, depending on the core radius) the half-range (1/2) log(max v/min v) of the log-stretch is about 0.03 at spacing equal to the ring radius and 0.22 to 0.40 at 1.5 radii (core radius 0.05 to 0.2 ring radii; v is positive on the whole axis there; this half-range is not the resonant Fourier amplitude), and the angular passage frequency 2 pi/(passage time) equals 2 omega_1 for a ring circulation of 0.4 to 2 times C_* delta_n times the squared ring radius in record units (a frequency match only; resonant pumping of the core by the row was not computed). The row is unstable to pairing: a relative perturbation 1e-3 of the radii and positions grows by a factor of about 4 to 6 per passage at spacing equal to the radius and about 8 to 11 at 1.5 radii and destroys the row within 3 to 4 passages (reproduced here at core radius 0.1 ring radii, with six and with twelve rings per periodic cell), so, extrapolating a constant amplification q per passage, keeping the growing component of the perturbation below a tolerance eta for thirteen passages (the length of the capped episode of the free pair above) needs an initial component of at most about eta q^{-13}, between 1.5e-8 eta (q = 4) and 2.9e-14 eta (q = 11) (a heuristic extrapolation from these short runs). Like the Hessian tolerance of the tuned pair, this is a fixed small number in the model, not a condition that tightens as n grows, and it neither excludes nor realizes such a drive in a Case 2 history. (e) Consequence. Within the prescribed-strain model this channel couples through an affine velocity gradient of size O(delta_n) in
record units and needs no axial curvature of that affine component, unlike the curvature channel of R2.12. Its realization in a
finite-energy record flow is open: it needs a localization of the strain (which brings curvature outside the affine region), a
pressure history that generates it, and the record duration of (d). It is therefore not claimed to ask less of the record flow
than R2.12. These computations motivate an additional control on amplification driven by the strain history, for example (N1') (a
proposed coherence exclusion): along every active core path, the accumulated axial strain A_n(t), with its mean trend removed, has
no coherent component near twice an inertial frequency of the active cell with log-stretch amplitude above the levels at which
continuing growth is seen here (about 0.04 at G = 3000 and 5000, with transient amplification at about 0.02, (b)(iii); about 0.08
for one passage at fixed frequency, (b)(vi)) over the growth time. A mathematical version would have to fix the observation
window, the removal of the trend, the definition of coherent amplitude, the phase, the modes, the detuning tolerance and the
growth criterion; the quoted levels are specific to the tested histories and are not uniform thresholds, and excluding components
near twice a single frequency is not shown to exclude combination or higher-order resonances or other finite-time amplification.
The sufficiency of (N1') and any implication from the record hypotheses are unproved, and it is not necessary: a suitable supply
estimate could exclude the outcome by another route. The affine strain contributes (a/2) int (|v^R|^2 + |v^theta|^2 - 2 |v^Z|^2)
dV to the rate of change of the perturbation kinetic energy, a term of no fixed sign. The energy-Casimir budget extends exactly to this
breathing reference for either sign of the strain (R2.15): the functional grows at most by exp(3 int a_-), so, if the channel supplies
weighted production of the critical size, the cumulative supply requirement of R2.13 (b) applies to this input with I = 3 a_- E~, and
the strain history must supply a compression action int a_- of at least (1/3) [log(kappa_1 G^2 L T/E~(0))]_+, a logarithmic
requirement that does not exclude the channel.

R2.15 The energy-Casimir budget on a uniform strain of either sign, and a compression-action bound (identity and corollary proved by
hand; the quadratic form of the identity checked numerically in the linearized model of R2.14;
a budget, not an exclusion).
Setting. The equations of R2.10 in cell units with the outer flow U^s = -(a(t)/2) R e_R + a(t) Z e_Z, where a is a C^1 function of
time of either sign (C^1 so that U^s_t and the base pressure are classical; the formula for kappa below needs only continuity), and base
pressure (a'/4 - a^2/8) R^2 - (a' + a^2) Z^2/2 + int_0^R Gamma_kappa^2 r^{-3} dr. Put Lambda(t) = int_0^t a(s) ds. The reference is
Gamma_kappa = G (1 - e^{-kappa R^2/4}) with kappa' = a kappa - kappa^2, kappa(0) > 0. It solves the swirl equation exactly for either sign
of a: with x = kappa R^2/4, Gamma_t + U^R Gamma_R - (Gamma_RR - R^{-1} Gamma_R) = G x e^{-x} (kappa'/kappa - a + kappa). Explicitly
1/kappa(t) = e^{-Lambda(t)} (1/kappa(0) + int_0^t e^{Lambda(s)} ds), so kappa > 0 on every forward time interval (in R2.14, kappa = e^{Lambda}/s
with s' = e^{Lambda}, s(0) = 1/a_0). Circulation range: Gamma < G at every point, of either sign (the reference satisfies 0 <= Gamma_kappa < G).
With g = Gamma/G and the notation of R2.10 (a), put j(g) = J(ell(g)) = int_0^g s/ell(s) ds for 0 <= g < 1 and j(g) = g - g^2/4 for g < 0;
j is C^2 (j'(0) = 1, j''(0) = -1/2 from both sides), and h(g) = -j''(g) is the h of R2.10 for 0 <= g < 1 and equals 1/2 for g < 0.
Define phi_kappa(gamma) = -(kappa G^2/4) j(gamma/G), Phi_kappa(gamma, R) = phi_kappa(gamma) + gamma^2/(2 R^2). For 0 <= gamma < G this is
the definition of R2.10 (a) with the reference Gamma_kappa (phi_kappa' = -kappa G g/(4 ell), the value of -Gamma_kappa/R^2 where
Gamma_kappa = gamma), normalized by phi_kappa(0) = 0; for gamma < 0 it is the convex extension of R2.10 (b), -(kappa G/4) gamma + (kappa/16) gamma^2.
Phi_kappa(., R) is strictly convex (m = phi_kappa'' + R^{-2} > 0) with its minimum at Gamma_kappa(R). With the relative density
H = Phi_kappa(Gamma, R) - Phi_kappa(Gamma_kappa(R), R) >= 0, A = int H dx, K_1 = (1/2) int |b_1|^2 dx with b_1 = b - U^s, D_1 = int eta_1^2 R^2 dx (eta_1 = (d_Z b_1^R - d_R b_1^Z)/R, and u_1^R = b_1^R)
and E~ = e^{-Lambda} (A + K_1). Integrals are over one material period (perturbations periodic in Z e^{-Lambda}, period L e^{Lambda} in Z),
in the regularity class of R2.10 (c) (classical, axis regularity, finite relative energy and dissipation); there the radial cutoffs
that justify the integrations by parts below, and the vanishing of the pressure work (by incompressibility, periodicity in Z and the radial cutoff limit), are removed as in R2.10 (c), and
the computation is written without them.
(a) Identity.
  dE~/dt = -e^{-Lambda} { D_1 + (3a/2) int (b_1^Z)^2 dx + int m Gamma_Z^2 dx + pi kappa G^2 int Delta I_kappa[g(., Z, t)] dZ },
where Delta I_kappa is Delta I of R2.10 (b) with x = kappa R^2/4, J(ell(g)) replaced by j(g) and M = 1 + x h(g) (the same functional for
0 <= g < 1, its extension for g < 0), and the Z integral runs over the period. R2.10 (c) states this balance for a(t) >= 0; here it is
proved for either sign. Only the strain term depends on the sign of a; a enters the other terms only through kappa > 0.
Proof. (i) Transport: div U^s = 0 in R^3 and the period moves with U^s, so d/dt int F dx = int (d_t + U^s.grad) F dx for the densities
used; b_1 is divergence free and periodic, so int b_1.grad H dx = 0. (ii) Swirl part. phi_kappa = kappa times a function of gamma alone,
so d_t phi_kappa = (kappa'/kappa) phi_kappa = (a - kappa) phi_kappa. The explicit R dependence of Phi_kappa gives (d_R Phi_kappa) U^R =
a gamma^2/(2 R^2). With (d_t + U^s.grad) Gamma = L Gamma - b_1.grad Gamma, (d_t + U^s.grad) Gamma_kappa = L Gamma_kappa and
d_gamma Phi_kappa(Gamma_kappa, R) = 0,
  dA/dt = int d_gamma Phi_kappa(Gamma, R) (L Gamma - b_1.grad Gamma) dx + a int (Gamma^2 - Gamma_kappa^2)/(2 R^2) dx
          + (a - kappa) int [phi_kappa(Gamma) - phi_kappa(Gamma_kappa)] dx.
The weight subtracts a A, which removes the second term and the a part of the third:
  e^{Lambda} d(e^{-Lambda} A)/dt = int d_gamma Phi_kappa(Gamma, R) (L Gamma - b_1.grad Gamma) dx - kappa int [phi_kappa(Gamma) - phi_kappa(Gamma_kappa)] dx.
Since d_R Phi_kappa(gamma, R) = -gamma^2 R^{-3} and d_gamma Phi_kappa(Gamma_kappa, R) = 0, d_gamma Phi_kappa(Gamma, R) b_1.grad Gamma =
b_1.grad H + (Gamma^2 - Gamma_kappa^2) R^{-3} u_1^R, so by (i) the drift term equals -int (Gamma^2 - Gamma_kappa^2) R^{-3} u_1^R dx. The axial
part of L gives -int m Gamma_Z^2 dx. The radial part of L together with the kappa term is, at each Z, the radial expression of the
Burgers case of R2.10 (c) with a replaced by kappa (that reduction uses only the profile at one time and the coefficient of the phi
term; with j it reads d/dx (g - x j'(g)) = (1 + x h(g)) g_x - j'(g)), so it equals -pi kappa G^2 Delta I_kappa. (iii) Meridional part.
U^s is linear, so its vector Laplacian vanishes, and the base pressure balances U^s_t + U^s.grad U^s and Gamma_kappa^2 R^{-3} e_R;
subtracting, b_{1,t} + U^s.grad b_1 + b_1.grad U^s + b_1.grad b_1 + grad p_1 = Delta b_1 + (Gamma^2 - Gamma_kappa^2) R^{-3} e_R. Since
b_1.(b_1.grad U^s) = -(a/2) (b_1^R)^2 + a (b_1^Z)^2, the pressure work vanishes and int b_1.Delta b_1 dx = -D_1,
  e^{Lambda} d(e^{-Lambda} K_1)/dt = (a/2) int (b_1^R)^2 dx - a int (b_1^Z)^2 dx - (a/2) int |b_1|^2 dx - D_1 + int (Gamma^2 - Gamma_kappa^2) u_1^R R^{-3} dx
                                 = -(3a/2) int (b_1^Z)^2 dx - D_1 + int (Gamma^2 - Gamma_kappa^2) u_1^R R^{-3} dx.
(iv) In the sum the centrifugal terms of (ii) and (iii) cancel exactly.
(b) Corollary (compression-action bound). A >= 0, K_1 >= (1/2) int (b_1^Z)^2 dx, and every other term in the braces is nonnegative
(m > 0, kappa > 0, Delta I_kappa >= 0 by R2.10 (b): sharp form for 0 <= Gamma < G, weak form with the convex extension of R2.10 (b) for Gamma < G: for g < 0 the integrand M v^2 - j(g) with j(g) = g - g^2/4 and h = 1/2 has second derivatives 2M, 1/2 and 0 in (v, v), (g, g) and (g, v), its g-derivative has a nonnegative jump across g = 0 (x v^2/6 at the point x, since h'(0+) = 1/6 and h'(0-) = 0) while its v-derivative is continuous there, so it is jointly convex on the extended range, and g_B is unchanged).
With a_- = max(-a, 0) and Q = e^{-Lambda} { D_1 + int m Gamma_Z^2 dx + pi kappa G^2 int Delta I_kappa dZ } >= 0 (the braces without the
strain term), dE~/dt + Q = -(3a/2) e^{-Lambda} int (b_1^Z)^2 dx <= 3 a_- e^{-Lambda} K_1 <= 3 a_- E~, so
  E~(T) + int_0^T exp(3 int_t^T a_-) Q(t) dt <= E~(0) exp(3 int_0^T a_-),
and in particular E~(t) <= E~(0) exp(3 int_0^t a_-) and
  E~(T) + int_0^T e^{-Lambda} { D_1 + int m Gamma_Z^2 dx + pi kappa G^2 int Delta I_kappa dZ } dt <= E~(0) exp(3 int_0^T a_-).
So only the negative part of the strain can raise the functional, at most at the exponential rate 3 a_-; if E~(0) = 0 the
perturbation vanishes for all t. The identity is nonlinear in b_1 = b - U^s, so a breathing generated by the perturbation itself (for
example the component at twice the inertial frequency of q^2 for a standing cell under a long-wave envelope) is part of b_1, not of the uniform strain: when a >= 0, E~ does not increase, whatever the length of the period,
so within this model a gain requires phases of axial compression (a < 0) of the imposed strain. The integrating-factor structure is that of Theorem 9 (a), but the strain variables differ: here a is the imposed axial strain d_Z U^{s,Z}, while Theorem 9 uses the radial strain u^r/r weighted by q^2 r; there, Sigma' = -D_Sigma - 3 Abar Sigma and the two integrating factors are at least e^{-3 Act(t)} on [0, t], so Sigma(t) + int_0^t ||d_z(q^2)||_{L^1} ds <= Sigma(t) + int_0^t D_Sigma ds <= e^{3 Act(t)} Sigma(0), with the
compression action Act. For the breathing history of R2.14, a = a_0 + beta Omega cos(d phi) with phi' = Omega > 0 (Omega may vary), constant beta >= 0, d > 0 and a_0 >= 0, each forcing period (phi increasing by 2 pi/d) contributes int a_- dt <= beta int (cos d phi)_- d phi = 2 beta/d. So the functional grows by at most the factor exp(6 beta/d) per forcing period. If beta Omega <= a_0 at all times, a >= 0 and E~ does not increase; if instead the strain amplitude A = beta(t) Omega(t) > a_0 is fixed (so beta = A/Omega), then for constant Omega the functional grows over one forcing period by at most exp(6A/(d Omega)) = exp(3 A Tp/pi), Tp = 2 pi/(d Omega) the period length, so the exponential rate averaged over periods is at most 3A/pi; if 0 < Omega_min <= Omega <= Omega_max on a complete forcing period, that rate is at most (3A/pi) Omega_max/Omega_min (there int a_- dt <= 2A/(d Omega_min), and the period lasts at least 2 pi/(d Omega_max)); and for any frequency history it is at most 3A. For constant beta, the per-period factor exp(6 beta/d) at fixed beta/d does not depend on the frequency
history Omega, on G or on the seed; it does not determine the amplification actually attained, which also depends on dissipation, on
the initial perturbation and on the coupling to the axial velocity.
(c) Consequence for the supply requirement (conditional on a weighted production lower bound). Under the hypotheses of R2.13 (b)
(in particular 0 <= Gamma <= G and the cell-unit Cartesian Hessian bound |D^2 u| <= G, which give |q_Z| <= G, 0 <= q <= 3G/2 for R <= 1 and q <= G R^{-2}), with m >= R^{-2}, the same split at R = rho
and Cauchy-Schwarz give P^w_phi(T) <= C ||phi||_infty G^{3/2} L^{3/4} T^{3/4} (D^w_T)^{1/4} with an absolute constant C (the measure here is
2 pi R dR dZ, so the numerical constant differs from that of R2.13 (b)), where P^w_phi(T) = int_0^T e^{-Lambda} int |phi| |d_Z(q^2)| dx dt and
D^w_T = int_0^T e^{-Lambda} int m Gamma_Z^2 dx dt (the weight turns integrals over the stretched period into L times averages per unit
axial length, so the changing period costs no further factor). By (b), D^w_T <= E~(0) exp(3 int_0^T a_-). Hence: if the channel supplies
weighted production P^w_phi(T) >= c_1 G^2 L T over T cell times and E~(0) > 0, then
  3 int_0^T a_- dt >= [log(kappa_1 G^2 L T/E~(0))]_+,   kappa_1 = (c_1/(C ||phi||_infty))^4.
A lower bound on unweighted production does not give this hypothesis by itself: for the same integrand,
e^{-max Lambda} P_phi(T) <= P^w_phi(T) <= e^{-min Lambda} P_phi(T), the extrema over [0, T]. Under the hypothesis, this is the input
condition of R2.13 (b), with I = 3 a_- E~, derived for this channel; at fixed E~(0) and L the requirement on the strain history is
logarithmic in T, so it does not exclude the channel. It becomes linear in T for a saturated core (proved by hand from (b) and the same production bound): integrating dE~/dt + Q <= 3 a_- E~ instead of using the exponential bound gives D^w_T <= E~(0) + 3 M_T int_0^T a_- dt with M_T = max over [0, T] of E~, so the same production hypothesis forces int_0^T a_- dt >= (kappa_1 G^2 L T - E~(0))/(3 M_T). If the functional stays below mu G^2 L, the strain must therefore compress the core at a time-averaged rate (1/T) int_0^T a_- of at least (kappa_1 - E~(0)/(G^2 L T))/(3 mu) per cell time, that is a fixed fraction of the cell rate kappa_n = nu_n/delta_n^2 in record units; a pumped core that saturates and keeps producing at the critical rate needs an accumulated compression action growing at least linearly in T, not a logarithmic amount at the start (this cumulative statement does not bound the gaps between compression phases). The constants kappa_1 and mu are not computed, so the condition is not compared with the breathing runs of R2.14 (time-averaged a_- about 14 per cell time in the fixed-strain-amplitude run of R2.14 (c)); it is a necessary condition on the strain history, not an obstruction. In that run (recomputed with the weighted diagnostics) the inequality D^w_T <= E~(0) + 3 M_T int_0^T a_- is far from tight: 3 M_T int_0^T a_- exceeds D^w_T by factors of about 109, 362 and 1351 at T = 0.1, 0.2 and 0.3, and D^w_T stays below E~(0) throughout; the weighted production there is P^w_phi(T)/(G^2 L T) = 2.5e-3, 2.8e-3 and 3.4e-3, and the bound P^w_phi(T) <= C ||phi||_infty G^{3/2} L^{3/4} T^{3/4} (D^w_T)^{1/4} above holds with ratio 0.064 to 0.073 at C = 1 (integrals over R dR dZ without the azimuthal factor; with dx = 2 pi R dR dZ the ratio is (2 pi)^{3/4} times larger). Duration in record units: int a_- dt is invariant under a fixed rescaling of time,
so it has the same value in record units. If a_- <= B_max in record units, lifting the functional by a factor F > 1 (from E~(0) > 0)
takes at least log F/(3 B_max) record times. If the uniform strain stands for the local axial strain rate of the record flow at the
core (a = d_z u^z on the axis), the gradient bound (C) gives B_max = 1, so at least (1/3) log F record times. In the breathing family of
R2.14 the oscillatory amplitude beta Omega, which bounds a_- since a_0 >= 0, is at most B_max = beta (s_1 + s_2)(1) C_* delta = 0.04153 C_* delta in record units at beta = 0.05 (R2.14 (d); the frequencies s_1, s_2 are computed numerically and Omega decreases in time in the runs, so this is a numerical value, not a certified bound), which gives at least log F/(0.1246 C_* delta) record times. Splitting the phase interval into complete forcing periods and a remainder
shorter than one period, whose contribution is at most that of a full period (the phase advances by at most B_max T_rec/beta over
T_rec record times; this uses the amplitude bound beta Omega <= B_max, not only a_- <= B_max), int a_- dt_rec <= B_max T_rec/pi + 2 beta/d, so also
T_rec >= (pi/(3 B_max)) (log F - 6 beta/d)_+. The mean of (cos)_- over a full period, 1/pi, does not bound averages over partial periods,
so the factor pi holds only in this corrected form. This makes the duration remark of R2.14 (d) quantitative within the model.
(d) Numerical check (of the quadratic identity only). With Gamma = Gamma_kappa + eps gamma and b_1 = eps v, both sides of (a) were compared at
order eps^2 in the linearized model of R2.14: the functional E~_2 = (1/2) e^{-Lambda} int (m_kappa gamma^2 + |v|^2) dx, m_kappa = (kappa/4)(h(x) + 1/x), where h(x) denotes h at the reference, h(1 - e^{-x}) = (e^x - 1 - x)/x^2,
per unit material length, and the radial term computed directly from the fields as the quadratic radial contribution (equivalently
-pi kappa G^2 times the coefficient of eps^2 in Delta I_kappa at Gamma_kappa + eps gamma). This does not test the nonlinear terms, the extension to
negative circulation or general strain histories. Discretization: one axial Fourier mode of unit wavenumber in the material
coordinate, the material radius R e^{Lambda/2} on [0, 10] with second-order finite volumes and a zero condition at the outer radius
(the seeds and the core are Gaussian-localized well inside it), the classical fourth-order Runge-Kutta scheme with time step 1e-5, and the
rate of change of the functional by central differences with the same spacing. The residual, relative to the sum of the absolute
values of the four terms on the right of (a), was 1.5e-3 to 3.1e-3 with 800 radial cells at G = 5000, beta = 0.05, d = 1.27 (times 0.02
to 0.04; with 400 cells 6e-3 to 1.2e-2 at the same times, so it decreases under radial refinement). At 400 cells, halving the time step left the functional
unchanged to five digits and changed the residual by at most 5 per cent, and enlarging the outer radius from 10 to 15 at the same cell
size changed the computed terms in the sixth digit, so the residual is set by the radial resolution. There a ranges from -189 to -59 at the sampled times and the strain term is the dominant input. With 400 cells at
G = 3000, beta = 0.2, d = 0.72, started from a purely meridional seed, a ranged from -419 to +362 at the samples and the residual was
2.8e-3 to 1.1e-2. At three of the six samples the absolute residual is comparable with or larger than the radial contribution (the strain term
dominates), so there the full comparison tests mainly the strain and dissipation terms. The radial contribution was therefore also
compared directly with the closed quadratic form: per unit length, with the measure R dR for the radial contribution, it should equal -(kappa G^2/2) I_2[xi],
xi = gamma/G, I_2[xi] = int_0^infinity [M_B |xi_x - ((1 - x)/x) xi|^2 + (h(x)/2 + 3/(2x)) |xi|^2] dx, M_B = 1 + x h(x), where x = kappa R^2/4, so that R dR = 2 dx/kappa (for real xi a formula for the coefficient of eps^2 in
Delta I_kappa at the reference, half the second derivative, stated without derivation and used only for this numerical comparison; for complex xi its Hermitian extension). Here gamma is the complex radial amplitude of the single axial mode, and both quadratic forms are evaluated on it without axial average; both scale by |c|^2 under gamma -> c gamma, so their ratio does not depend on how the amplitude is normalized, and for the real field Re[gamma(R) e^{i k Z'}], Z' the material axial coordinate, averaging over an axial period multiplies both by 1/2; the measured radial contribution divided by kappa G^2 I_2[xi] was -0.501 to -0.495 at all six samples with 400 cells, against the
predicted -1/2.
The radial contribution to the rate of change was negative at every sample (I_2 > 0).
For the corollary, over 0 < t <= 0.08 (at times where int_0^t a_- > 0), log(E~(t)/E~(0)) divided by 3 int_0^t a_- was 0.32 to 0.44 at
G = 5000, beta = 0.05, d = 1.27 (log growth 0.07 to 0.10 per forcing period against a measured 3 int a_- of 0.22 to 0.23 per period, below
6 beta/d = 0.236), 0.45 to 0.56 at beta = 0.1 (0.20 to 0.26 per period against 0.45 to 0.47, below 0.472), and -0.08 to 0.26 at G = 3000,
beta = 0.2, d = 0.72 (6 beta/d = 1.667). These ratios test the growth inequality E~(t) <= E~(0) exp(3 int_0^t a_-), not the inequality
with the accumulated dissipation included.
(e) Scope. The identity is exact only for the idealized unbounded affine strain. A localized strain brings back curvature and the
first-order non-uniformity term of R2.10 (g), and the jet term of R2.10 (e) is separate. The result is a budget: it allows exponential
growth at rate 3 a_-; the lower bound it gives for the required compression action is logarithmic without further hypotheses and linear under the saturation hypothesis of (c) (a lower bound, which does not show that this action is achievable); and it bounds production through the strain sign history, not through
the strain amplitude alone. It therefore neither excludes the breathing channel nor supplies the missing implication. It supplies the energy-Casimir
extension cited in R2.14 (e); the production consequence remains conditional on the weighted production lower bound in (c).

R2.16 Unweighted and dissipation-normalized forms of the missing implication (necessary compression bounds and sufficient exclusion criteria, proved from Theorem 9 (a), (b), (d), Theorems 1 (a), (b) and 3 (a), (b) (with (B1) and (B2) of Theorem 1 (a)), the hypothesis (A), the energy and circulation bounds and one cited regularity criterion, each step checked twice by hand; none of the sufficient bounds is established for Case 2).
Let D_Sigma(t) = 2 int |grad q|^2 r dx + int q^2/r dx, so that Sigma' = -D_Sigma - 3 int a q^2 r dx (Theorem 9 (a)). With a = a_r + a_s as in
Theorem 9 (d), int a_s q^2 r dx = -Pi_s and |int a_r q^2 r dx| <= C_0 Sigma because ||a_r||_infty <= C_0 (Theorem 9 (d)); and
int_0^t Sigma ds <= int_0^t (||grad u||_2^2 + ||u||_2^2) ds <= E_0 (1/2 + t) by the energy inequality (E_0 = ||u_0||_2^2). Hence, for t < T_*,
  Sigma(t) + int_0^t D_Sigma ds = Sigma(0) + 3 int_0^t Pi_s ds + rho(t),   rho(t) = -3 int_0^t int a_r q^2 r dx ds,   |rho(t)| <= 3 C_0 E_0 (1/2 + T_*).
Since 2 |q| |d_z q| <= (d_z q)^2 r + q^2/r pointwise for r > 0, ||d_z(q^2)||_{L^1} <= D_Sigma (the constant can be improved: 2 (d_z q)^2 r + q^2/r >= 2^{1/2} |d_z(q^2)| pointwise; better, with Y = r^{1/2} q and the form D_Sigma = 2 ||grad Y||_2^2 + (3/2) ||Y/r||_2^2 derived below, d_z(q^2) = 2 Y d_z Y/r and the pointwise inequality 2 (d_z Y)^2 + (3/2) Y^2/r^2 >= 2 3^{1/2} |Y d_z Y|/r give D_Sigma >= 3^{1/2} ||d_z(q^2)||_{L^1}, which would multiply the constants of the first two lower bounds below by 3^{1/2}, so that already limsup nu_n B_n < 2 3^{1/2} m_phi/P would exclude Case 2; the weaker form is kept), so Theorem 9 (b) gives in Case 2
  int_0^{t_n} D_Sigma dt >= (2 m_phi/P) nu_n^{-1} (1 - o(1)),   nu_n int_0^{t_n} Pi_s dt >= (2 m_phi/(3P)) (1 - o(1)),
  3 int_0^{t_n} Pi_s dt >= (1 - o(1)) int_0^{t_n} D_Sigma dt
(the last because Sigma(t_n) >= 0, Sigma(0) + rho is bounded and int_0^{t_n} D_Sigma -> infinity). The packet is arbitrary here: the identity of Theorem 3 (b) and the bound |int d_z(q^2) Psi_n dx| <= (P/2) ||d_z(q^2)||_{L^1} used for Theorem 9 (b) need only an axisymmetric phi in C_c^infty({R > 0}) with 0 <= phi <= P, and then int eta_n(y, 0) phi(y) dy -> m_phi by the locally uniform convergence of grad U_n away from the axis. Taking the supremum over such phi with P = 1, and applying the same bound to the reflected solution Q u(Qx, t) of Theorem 3, gives liminf_n nu_n int_0^{t_n} D_Sigma dt >= 2 max(||(eta_U(., 0))_+||_{L^1}, ||(eta_U(., 0))_-||_{L^1}), the norms taken in dy and possibly infinite. Hence, if eta_U(., 0) is not integrable (for example if it is nonzero and independent of Z), Case 2 along that sequence forces nu_n B_n -> infinity and nu_n int_0^{t_n} Pi_s dt -> infinity, so in that sub-branch any bound limsup_n nu_n B_n < infinity excludes it; no such bound is known. Each of the following therefore excludes
Case 2: (i) the unweighted signed bound limsup nu_n int_0^{t_n} Pi_s dt < 2 m_phi/(3P), which needs no Gronwall weight because int Sigma dt is
bounded by the energy; (ii) the dissipation-normalized bound 3 int_0^{t_n} Pi_s dt <= theta int_0^{t_n} D_Sigma dt + C with a fixed theta < 1
and C independent of n (then (1 - theta) int D_Sigma stays bounded, against the first display); (iii) the weighted bound
limsup nu_n int_0^{t_n} e^{3 C_0 (t_n - t)} Pi_s dt < 2 m_phi/(3P) of Theorem 9 (d). Write B_n = Sigma(t_n) + int_0^{t_n} D_Sigma dt. Since
nu_n (Sigma(0) + rho) -> 0, the identity turns (i) and (ii) into statements about the stored and dissipated swirl:
  (i) holds if and only if limsup nu_n B_n < 2 m_phi/P;
  (ii) holds for some fixed theta < 1 if and only if sup_n B_n < infinity, that is, if and only if int_0^{T_*} D_Sigma dt < infinity and
  sup_n Sigma(t_n) < infinity
((ii) gives Sigma(t_n) + (1 - theta) int D_Sigma <= Sigma(0) + C + |rho|; conversely B_n <= K gives 3 int Pi_s <= K + |rho|, which is (ii) with
theta = 0). These two equivalences are between the displayed criteria, not with the exclusion of Case 2, and they do not use Case 2; they use only t_n -> T_* < infinity, nu_n -> 0, Sigma(0) < infinity and the bound on rho. The weight in (iii) does not matter in the limit either: with w_n(t) = e^{3 C_0 (t_n - t)}, which lies in [1, e^{3 C_0 T_*}] on [0, t_n], multiplying Sigma' + D_Sigma = 3 Pi_s - 3 int a_r q^2 r dx by w_n and integrating by parts gives 3 int_0^{t_n} w_n Pi_s dt = Sigma(t_n) + int_0^{t_n} w_n D_Sigma dt + O(1), with |O(1)| <= e^{3 C_0 T_*} (Sigma(0) + 6 C_0 E_0 (1/2 + T_*)) by the bound on int Sigma dt; since nu_n int_0^{s_0} w_n D_Sigma dt -> 0 for each fixed s_0 < T_* and 1 <= w_n <= e^{3 C_0 (T_* - s_0)} on [s_0, t_n], letting n -> infinity and then s_0 -> T_* gives limsup 3 nu_n int_0^{t_n} w_n Pi_s dt = limsup nu_n B_n, so (iii) holds if and only if (i) holds. Since ||d_z(q^2)||_{L^1} <= D_Sigma, (i) implies the production bound
limsup nu_n int_0^{t_n} ||d_z(q^2)||_{L^1} dt < 2 m_phi/P, which excludes Case 2 directly by Theorem 9 (b). So (ii) implies (i), (i) and (iii) are equivalent, and (i) implies
the production bound. Of these three conditions (ii) is the strongest: it asks that B_n stay bounded, while (i) allows B_n to diverge provided
nu_n B_n stays below 2 m_phi/P by a fixed margin, and Case 2 forces nu_n int_0^{t_n} D_Sigma >= (2 m_phi/P)(1 - o(1)). So (ii) fails for every
history whose total swirl dissipation diverges or whose stored swirl Sigma(t_n) is unbounded, whatever the mechanism, and it is not an
independent route. More holds, independently of Case 2: the total swirl dissipation diverges at every singular time (here and below, the finite maximal time of an axisymmetric solution with H^2 data and bounded initial circulation). Put Y = r^{-1/2} u^theta = r^{1/2} q. Since Y vanishes on the axis, integrating the cross term by parts in r gives D_Sigma = 2 ||grad Y||_2^2 + (3/2) ||Y/r||_2^2 (also checked symbolically on test profiles), so Sobolev's inequality ||f||_6 <= C_Sob ||grad f||_2 on R^3 gives ||Y||_6^2 <= C_Sob^2 D_Sigma/2. With |Gamma| <= G (maximum principle) and |u^theta| = |Gamma|^{1/3} |Y|^{2/3}, ||u^theta||_9^3 <= G ||Y||_6^2. So int_0^{T_*} D_Sigma dt < infinity would put u^theta in L^3(0, T_*; L^9), with 2/3 + 3/9 = 1, and the swirl criterion of Chen, Fang and Zhang (Discrete Contin. Dyn. Syst. 37 (2017), Theorem 1.1 (1) with d = 0, for H^2 data; statement read, proof not checked; an independent reading of the statement confirms that the endpoint 2/p + 3/q = 1 with q = 9 is included and that smallness is needed only at the corner q = 3, p = infinity), applied to u as a Leray-Hopf weak solution on [0, T_*] (the energy bound and the equation give a weak L^2 limit of u(t) as t -> T_*: for a smooth compactly supported divergence-free test field phi, d<u, phi>/dt = int u (x) u : grad phi dx + int u . Delta phi dx is bounded by E_0 ||grad phi||_infty + E_0^{1/2} ||Delta phi||_2, so <u(t), phi> converges, and density with the energy bound gives the weak limit; the solution so extended to [0, T_*] is a Leray-Hopf weak solution, the energy inequality passing to t = T_* by weak lower semicontinuity, and it coincides with the smooth one before T_*), would make u smooth on (0, T_*], against the definition of T_*. Hence int_0^{T_*} D_Sigma dt = infinity at every singular time, so (ii) fails at every singular time: proving (ii) is the same as proving regularity, by a known criterion. Since Sigma(t) + int_0^t D_Sigma ds <= e^{3 Act(t)} Sigma(0) (the integrating-factor form of Theorem 9 (a)), the same holds for the compression action when Sigma(0) > 0 (if Sigma(0) = 0 the swirl vanishes for all time by the linear homogeneous swirl equation, and the flow is swirl-free and regular): Act(t) tends to infinity as t tends to every singular time, whatever the record structure (this is the member j = 2 of the family in Section 3, F10). An averaged form also holds for 0 <= t < T_* (Abar and D_Sigma are integrable on [0, t], since |Abar| <= ||u^r/r||_infty <= ||grad u||_infty and u is in L^2(0, t; H^3) for H^2 data, and Sigma is absolutely continuous there): with I(s) = int_0^s (- Abar(tau)) d tau (so Act(t) = sup_{0 <= s <= t} I(s)), B(t) = Sigma(t) + int_0^t D_Sigma ds and, when Sigma(0) > 0, the probability measure mu_t = (D_Sigma(s) ds + Sigma(t) delta_t)/B(t) on [0, t], delta_t the unit point mass at t, the integrating factor gives e^{-3 I(t)} Sigma(t) + int_0^t e^{-3 I(s)} D_Sigma(s) ds = Sigma(0), that is, int e^{-3 I} d mu_t = Sigma(0)/B(t), so Jensen's inequality gives int I d mu_t >= (1/3) log(B(t)/Sigma(0)); in Case 2, where B_n = B(t_n) >= (2 m_phi/P)(1 - o(1))/nu_n, the mu_{t_n}-average of the accumulated action I(s) is at least (1/3) log(1/nu_n) - C for all large n (C independent of n), which refines the supremum bound of Theorem 9 (b), since int I d mu_{t_n} <= Act(t_n). The atom Sigma(t) delta_t is needed for the displayed equality; separately, when B_D(t) = int_0^t D_Sigma ds > 0, the probability measure D_Sigma(s) ds/B_D(t) satisfies int_0^t e^{-3 I} D_Sigma ds/B_D(t) = (Sigma(0) - e^{-3 I(t)} Sigma(t))/B_D(t) <= Sigma(0)/B_D(t), so Jensen's inequality gives int_0^t I D_Sigma ds/B_D(t) >= (1/3) log(B_D(t)/Sigma(0)), and the Case 2 lower bound nu_n B_D(t_n) >= (2 m_phi/P)(1 - o(1)) gives the same bound (1/3) log(1/nu_n) - C for this dissipation average, without any estimate on Sigma(t_n). The same identity gives a level-set form: since e^{-3 I} >= e^{-3L} where I <= L, int_{0 <= s <= t, I(s) <= L} D_Sigma ds <= e^{3L} Sigma(0) for every real L, so in Case 2 at most the fraction (P Sigma(0)/(2 m_phi)) e^{-3 lambda} (1 + o(1)) of int_0^{t_n} D_Sigma ds is spent at times s with I(s) <= (1/3) log(1/nu_n) - lambda, for every real lambda (the o(1) does not depend on lambda). (The weaker statement that sup_t Sigma < infinity and int D_Sigma dt < infinity together give continuation is contained in the proof of Theorem 3.1 of Shahmurov, arXiv:2604.21213, with the weight r^{-1/2}.) (Without Sobolev: |u^theta|^5 = |Gamma|^3 (u^theta)^2/r^3 and int (u^theta)^2/r^3 dx = int q^2/r dx <= D_Sigma give int_0^T ||u^theta||_5^5 dt <= G^3 int_0^T D_Sigma dt, and the same criterion applies with exponents 5, 5.) Both Sigma and int D_Sigma dt are invariant under the Navier-Stokes scaling, so these are critical quantities. An elementary upper bound brackets B_n. The angular part ((u^r)^2 + (u^theta)^2)/r^2 of |grad u|^2 gives ||q||_2^2 <= ||grad u||_2^2, so int_0^t ||q||_2^2 ds <= E_0/2 by the energy equality; since 3 int a q^2 r dx = 3 int u^r q^2 dx and |u^r| <= M(t), Sigma(t) + int_0^t D_Sigma ds <= Sigma(0) + (3/2) E_0 M(t) for t < T_*. In Case 2 (1/nu_n = M_n l_n) this gives (2 m_phi/P) M_n l_n (1 - o(1)) <= B_n <= Sigma(0) + (3/2) E_0 M_n, so (i) asks to improve this upper bound by a factor of order l_n/E_0, which tends to 0 (||u||_infty <= C ||u||_2^{2/5} ||grad u||_infty^{3/5} gives l_n <= C E_0^{1/5} D_n^{-2/5}); the bound itself does not exclude Case 2. With unit viscosity E_0 and l_n are both lengths, so the upper bound is M_n times the energy length E_0, while (i) asks for M_n times a multiple of the record length l_n with constant below 2 m_phi/P. An instantaneous inequality for Sigma alone does not give this: since Sigma = ||Y||_2^2 and int u^r q^2 dx = int (u^r/r) Y^2 dx, Hoelder, ||u^r/r||_2 <= ||grad u||_2, ||Y||_4^2 <= ||Y||_2^{1/2} ||Y||_6^{3/2} and Sobolev give 3 |int u^r q^2 dx| <= ||grad Y||_2^2 + C ||grad u||_2^4 Sigma, hence only Sigma(t) <= Sigma(0) exp(C int_0^t ||grad u||_2^4 ds), whose exponent diverges at every singular time (||grad u(t)||_2 >= c (T_* - t)^{-1/4}). Localizing the same majorant to the last record time does not help either: from any s < t_n the same steps give Sigma(t_n) + int_s^{t_n} D_Sigma <= Sigma(s) + (3/2) M_n (E(s) - E(t_n)), and the energy dissipated over the last record time alone satisfies int_{t_n - 1/D_n}^{t_n} ||grad u||_2^2 dt >= c_R M_n l_n^2 (1 - o(1)), c_R = int_{-1}^0 int_{|y| < R} |grad U|^2 dy dtau > 0 for R > alpha_*, by the change of variables to record units and the local uniform convergence of grad U_n to grad U (Theorem 1 (b), |grad U(y_*, 0)| = 1). Since E(s) - E(t_n) = 2 int_s^{t_n} ||grad u||_2^2 dt, that part of the majorant is at least 3 c_R M_n^2 l_n^2 (1 - o(1)) (a lower bound on the majorant, not on the actual compression), larger than 1/nu_n = M_n l_n by a factor of order 1/nu_n. The loss sits in the two pointwise steps ||q||_2^2 <= ||grad u||_2^2 and |u^r| <= M, which ignore that the swirl is small (B1), not in the length of the history. Keeping the swirl factor improves the bracket, though not to the required order. Pointwise |u^r| q^2 = |u^theta| |u^r/r| |q| <= (|u^theta|/2)((u^r/r)^2 + q^2) <= (s_theta(t)/2) |grad u|^2 (s_theta(t) = ||u^theta(t)||_infty, so that S(t) = sup over s <= t of s_theta(s) and S_n = S(t_n) is the historical swirl maximum), because (u^r/r)^2 + (u^theta/r)^2 is part of |grad u|^2; hence 3 |int u^r q^2 dx| <= (3/2) s_theta(t) ||grad u(t)||_2^2 and B_n <= Sigma(0) + (3/2) int_0^{t_n} s_theta(t) ||grad u(t)||_2^2 dt <= Sigma(0) + (3/4) E_0 S_n, smaller than the previous majorant by the factor S_n/(2 M_n), which tends to 0 by (B1). In Case 2 the lower bound on B_n forces S_n -> infinity; since 0 <= s_theta(t)/S_n <= 1 on [0, t_n], s_theta(t)/S_n -> 0 for each fixed t < T_*, and ||grad u||_2^2 is integrable on [0, T_*), dominated convergence gives int_0^{t_n} s_theta ||grad u||_2^2 dt = o(S_n), so B_n = o(S_n), and with the lower bound Case 2 forces nu_n S_n -> infinity, in scale-invariant form S_n E_0/(M_n l_n) -> infinity (proved). This is a necessary condition, not an exclusion: the scalar power laws nu_n = h, l_n = h^3, M_n = h^{-4}, D_n = h^{-7}, S_n = h^{-3}, H_n = h^{-10} (h -> 0) satisfy (A) with C_* = 1, (B1), (B2), S^2 <= G D, S^3 <= G^2 H and D^3/M^5 >= 1, and have nu_n S_n = h^{-2} (a consistency check of scalar constraints, not a solution). In this form (i) follows from limsup nu_n int_0^{t_n} s_theta(t) ||grad u(t)||_2^2 dt < 4 m_phi/(3P), which no available estimate gives; the pointwise form limsup nu_n int_0^{t_n} int |u^theta| |grad u|^2 dx dt < 4 m_phi/(3P) also suffices, but the available estimates do not show that it is o(1/nu_n) even on a single record window: in record units (u^theta = M_n nu_n gamma_n/R) the part of int int |u^theta| |grad u|^2 dx dt over [t_n - 1/D_n, t_n] x {|z - z_n| < l_n, r < l_n} equals nu_n^{-1} int int |gamma_n| |grad U_n|^2 R^{-1} dy dtau, which the bounds above estimate only by 4 pi G/nu_n (|gamma_n| <= G, |grad U_n| <= 1); no lower bound is claimed, but nothing here makes it o(1/nu_n), because the bracket replaces the small record-scale size of q, which the window estimate below uses, by the circulation bound, which is not small. On fixed record windows the compression is negligible. Let v = u^theta e_theta; the reflection in a meridional plane fixes the poloidal part and reverses v, so v is half the difference of u and its reflection and ||grad^2 v||_infty <= ||grad^2 u||_infty. The interpolation ||grad v||_infty <= C (||v||_infty ||grad^2 v||_infty)^{1/2} on R^3 and |q| <= ||grad v||_infty (v vanishes on the axis) give, with (A), |q| <= k_n D_n on [0, t_n], k_n = C (C_* S_n/M_n)^{1/2} -> 0 by (B1); with |q| <= G/r^2, in record units |q_n| <= min(k_n, G nu_n/R^2), so int_{|Z| < L} q_n^2 dy <= 4 pi L G nu_n k_n, all radii included. For fixed A and L the compression over [t_n - A/D_n, t_n] x {|z - z_n| < L l_n} is therefore at most 3 M_n (4 pi A L G l_n k_n) = 12 pi A L G k_n/nu_n = o(1/nu_n). Using |u^r| <= r D_n instead of |u^r| <= M_n, and int_0^infty min(K, G/r^2)^2 r^2 dr = (4/3) G^{3/2} K^{1/2} (K = k_n D_n; checked by quadrature), the same window carries compression at most 16 pi A L G^{3/2} k_n^{1/2} nu_n^{-1/2} <= C A L C_*^{1/3} G^{5/3} nu_n^{-1/3}, so windows of record duration A_n and axial half-length L_n l_n are negligible whenever A_n L_n nu_n^{2/3} -> 0 (proved; the same steps with |u^theta| <= min(r ||grad v||_infty, G/r) give S^3 <= C G^2 H, so S_n/M_n <= C (C_* G^2)^{1/3} nu_n^{2/3}). Since B_n = Sigma(0) - 3 int_0^{t_n} int u^r q^2 dx dt <= Sigma(0) + 3 int_0^{t_n} int (u^r)_- q^2 dx dt, the positive compression of at least order 1/nu_n that Case 2 requires must occur outside every fixed record window, indeed outside every window with A_n L_n = o(nu_n^{-2/3}) (ages beyond such multiples of 1/D_n, the window clipped at t = 0, or axial distances beyond such multiples of l_n), as for the production in Section 1; this localizes the compression, not the storage or the dissipation, since swirl compressed earlier or elsewhere may dissipate inside a window; the tightness statement lim_{A, L -> infinity} limsup_n nu_n int int (u^r)_- q^2 dx dt = 0, the integral taken outside the window, would suffice and is not proved. In words, Case 2 forces the swirl to dissipate, and therefore by the identity to regain by compression through the
sourced vorticity, an amount of Sigma of at least order 1/nu_n with a definite constant (no upper bound of that order is proved). In Case 2,
3 int Pi_s = (1 + o(1)) int D_Sigma holds if and only if Sigma(t_n) = o(int_0^{t_n} D_Sigma), which is not proved (the bound
Sigma(t_n) <= ||grad u(t_n)||_2^2 + E_0 does not give it). Criterion (ii) is evaluated by the equivalence above.
Two readings. First, in the record frame the regular part of the vorticity is negligible: |eta_r| <= ||eta_0||_infty by the
maximum principle, which in record units is O(M_n/D_n^2) (as in Theorem 3 (b)), and its part a_r of the radial strain u^r/r is O(1/D_n) in record units (Theorem 9 (d) bounds a_r, not the whole velocity gradient of the regular part away from the axis). So the radial strain u^r/r acting on a core near the record, and on the axis the axial strain -2 u^r/r, are, up to these terms, those of the sourced vorticity, and "self-compression" includes compression of
a core by the record flow's own strain. Second, a steady core held in an imposed stretching strain compresses more than it dissipates; this is a property of the steady Burgers profile, not of every core (for a profile q = A f(r/delta) out of equilibrium D_Sigma/Sigma is of order delta^{-2} while the compression rate is 3 a_B/2, so a narrow profile dissipates faster than it compresses). For the
Burgers column with axial strain a_B > 0 (u^r = -a_B r/2, u^z = a_B z), with this strain counted as sourced as in the first reading (a modelling hypothesis: a linear strain is not recovered from its own azimuthal vorticity by the decaying Biot-Savart law, so it stands for a strain supplied by exterior sourced vorticity), the steady
swirl equation gives per unit axial length, over the whole radial profile, dissipation (a_B/2) Sigma and compression 3 Pi_s = (3 a_B/2) Sigma,
a ratio of 3. In a fixed axial window the excess a_B Sigma leaves through the window ends with the axial flow; on a material axial segment,
whose length grows like e^{a_B t}, it accumulates and Sigma grows like e^{a_B t}. The ratio 3 uses the whole radial profile (on a disc r < R
well inside the core it is about a_B R^2/2, and radial fluxes enter), and the column has infinite energy, so this is a local balance that
neither tests nor decides the global criteria. In the global identity the fluxes between a core and its exterior cancel, and the exterior
contributes its own storage, dissipation and signed strain work (expansion, where a > 0, reduces Sigma); a local ratio of compression to
dissipation therefore does not determine the global signed budget. A ratio formed from one cell's perturbation budgets is not the ratio of the
global quantities in (i)-(ii). What (i) asks is a bound, below (2 m_phi/P)/nu_n by a fixed factor, on the total Sigma that the whole history dissipates
or stores up to t_n.
Scale reading (constants omitted; the count of Theorem 9 (e) read for B_n). In record units, with the record time t_n placed at tau = 0,
nu_n B_n = Sigma~(0)/nu_n + int_{-t_n D_n}^0 D~ dtau (Sigma~(0) the record-unit storage at the record time tau = 0, not the initial storage), where Sigma~ = int q_n^2 R dy and D~ = 2 int |grad q_n|^2 R dy + int q_n^2/R dy are
the record-unit forms of Sigma and D_Sigma (Sigma = nu_n^{-2} Sigma~, D_Sigma = M_n^2 D~). The record circulation R U^theta_n equals
nu_n Gamma, so it is bounded by g_n = G nu_n, and the interpolation cap gives |q_n| <= C C_*^{2/3} g_n^{1/3}: the circulation reaches a
fixed fraction of g_n only at radii of order delta_n = (g_n/C_*)^{1/3} or more. The per-length contributions are bounded as follows
(proved). Let v = U^theta_n e_theta, so |grad^2 v| <= C_* (reflection, as above); let gamma(Z, tau) be the supremum of |R U^theta_n| over
R > 0 and |Z' - Z| <= 1, and delta = (gamma/C_*)^{1/3}. At fixed Z, |U^theta_n(R)| >= |q_n(0, Z)| R - C_* R^2/2 (Taylor expansion of sgn(q_n(0, Z)) U^theta_n along a radius), and the
circulation bound at R = |q_n(0, Z)|/C_* gives |q_n(0, Z)| <= (2 gamma C_*^2)^{1/3}, hence |grad v| <= C C_* delta for R <= 3 delta. For R >= 3 delta and n large (delta_n <= 1/2),
interpolation on the ball of radius (4 gamma/(R C_*))^{1/2}, which is at most min(R/2, 1), on which |v| <= 2 gamma/R, gives |grad v|^2 <= C C_* gamma/R.
Since 2 R^2 |grad q_n|^2 + q_n^2 <= 5 |grad v|^2, D~ <= 10 pi int int |grad v|^2 dR dZ, and Sigma~ = 2 pi int int (U^theta_n)^2 dR dZ. So,
per unit record length, Sigma~ is at most C C_*^{1/3} gamma^{5/3}, the disc R <= 3 delta contributes at most C C_* gamma to D~, and so
does each dyadic shell rho <= R <= 2 rho with rho >= 3 delta; the radial tail R >= R_1 contributes to int D~ dtau at most (5/R_1) int int |grad U_n|^2 dy dtau (|grad v| <= |grad U_n|, the toroidal and poloidal parts of grad U_n occupying disjoint entries in the Frobenius norm) <= (5/2) E_0 D_n^2/(M_n^3 R_1) by the energy equality. With R_1 = E_0 D_n^2/(epsilon M_n^3) and
ell_n = 1 + log^+(R_1/delta_n),
    nu_n B_n <= C C_*^{1/3} nu_n^{-1} int gamma(Z, 0)^{5/3} dZ + C C_* int int gamma (ell_n + log(g_n/gamma)) dZ dtau + 3 epsilon
(with gamma log(g_n/gamma) = 0 where gamma = 0; the right side may be infinite).

So, for a fixed epsilon <= m_phi/(3P) and each sufficiently large n, Case 2 needs either terminal swirl with int gamma(Z, 0)^{5/3} dZ at least of order nu_n/C_*^{1/3} (at saturation, an axial extent of
order nu_n^{-2/3} record lengths), or int int gamma (1 + ell_n^{-1} log(g_n/gamma)) dZ dtau at least of order 1/(C_* ell_n) (at saturation, a
measure of order 1/(G C_* nu_n ell_n), for example a record length of axis over 1/(G C_* nu_n ell_n) record times; in physical units
an axial length times a time of order l_n^3/(G C_* ell_n)); which alternative holds may depend on n, and along a further subsequence one of them holds for every n. These necessary conditions are weak: they are met whenever the
radially maximized circulation stays comparable to G over a set of axial positions and times of that physical measure, which tends to 0
(l_n <= C(C_*) E_0 nu_n^2, since |grad U_n| = 1 at the record point and |grad^2 U_n| <= C_* give |U_n| >= c(C_*) on a ball of radius
c(C_*), so E_0 >= c(C_*) M_n^2 l_n^3 = c(C_*) l_n/nu_n^2); meeting them says nothing about the actual budget. The shell bound requires U^theta_n to vary by its own size
over meridional distances of order h = (gamma/(C_* rho))^{1/2}, radially or axially (with a small fixed factor k, the axial oscillation
U^theta_n = k (gamma/rho) chi(R/rho) sin(Z/h) attains it), which the pointwise bounds allow at every radius; a profile of fixed radial
shape at scale rho, constant in Z, contributes about gamma^2/rho^3 instead, and a saturated column of fixed shape at radius delta_n contributes the
orders above with ell_n replaced by 1 (exact integration for an Oseen profile R U^theta = gamma (1 - exp(-R^2/d^2)): Sigma~ = 6.52 gamma^2/d and
D~ = 13.05 gamma^2/d^3 per unit length, exactly 4 pi^{3/2} (1 - 2^{-1/2}) gamma^2/d and 8 pi^{3/2} (1 - 2^{-1/2}) gamma^2/d^3). For that column the dissipation integral reaches the storage
term Sigma~/nu_n after the viscous time d^2/(2 nu_n), with d of order delta_n, and the axial
strain that holds it steady in the Burgers sense is of order nu_n/delta_n^2 = (C_*/G)^{2/3} nu_n^{1/3}, far below the record gradient. Material sets obey the same count. Along a particle path a = U^R/R = d(log R)/dtau, so the signed compression int (-a) dtau =
log(R(tau_0)/R(tau_1)) is O(1) while R stays within fixed factors of its initial value. For a material set P_tau whose particles keep R
and |q_n| within fixed factors of delta and C_* delta (delta = (gamma/C_*)^{1/3}) on [tau_0, tau_1], and which initially lies in an axial
interval of length L (so its volume is at most C delta^2 L), the identity D_tau (q_n^2 R) = -3 a q_n^2 R + 2 nu_n R q_n Delta_5 q_n and
|Delta_5 q_n| <= 3^{1/2} C_*/R (since Delta v = R (Delta_5 q_n) e_theta) give
  nu_n^{-1} int int_{P_tau} (-a) q_n^2 R dy dtau <= C C_*^{1/3} gamma^{5/3} L/nu_n + C C_* gamma L (tau_1 - tau_0),
the stored amount and the rate C_* gamma per unit length of the count above (proved). Both statements are signed: they do not bound
int (-a)_+ dtau, since compression and expansion can cancel along a path, and they do not control Eulerian windows, since parcels enter
and leave. The window bound above (negligibility when A_n L_n nu_n^{2/3} -> 0, A_n the record duration and L_n the axial half-length in record
lengths) is sharp as an estimate from the pointwise bounds alone: a smooth, compactly supported, time-independent field whose saturated
core sits in a fixed uniform compression U^R = -c R (record units) (for example the streamfunction c R^2 Z near the core, giving U^R = -c R and U^Z = 2 c Z, cut off smoothly at a fixed distance, with U^theta = s C_* delta R chi(R^2/delta^2) zeta(Z) for fixed smooth cutoffs chi, zeta and small fixed c, s, so that the circulation is O(C_* delta^3) and the Hessian O(C_*)) meets all the pointwise bounds and carries physical compression 3 int int (-u^r) q^2 dx dt of order 1/nu_n (record-unit compression
int int (-a) q_n^2 R dy dtau of order nu_n) over a fixed axial length and nu_n^{-2/3} record times. It does not solve the equations (at the core centre, where the advection vanishes, the steady swirl equation would require 2 c q + nu_n Delta_5 q = 0, impossible for large n since nu_n Delta_5 q = O(nu_n C_*/delta_n) while 2 c q is of order c C_* delta_n and nu_n/delta_n^2 -> 0), so this is sharpness of the window estimate, not of the swirl budget.
No estimate established in this report bounds the resulting global budget below the Case 2 threshold.

R2.17 A count-level comparison for one band scenario (the balances in (a) are proved under the stated integrability; (b) to (e) are conditional estimates built on the numerical ring-model inputs of R2.14 (d) and on the assumptions stated there; neither an exclusion nor a construction, and not a proof that the scenario is compatible with Case 2).
Question. Do the necessary conditions collected in this report already exclude the scenario suggested by R2.14 (d): saturated swirl cores in the age band, held between episodes and pumped episodically by tuned exterior ring pairs, each episode being assumed to stop before the interpolation cap |q| <= 2 G kappa_c of (A) is violated (no mechanism that stops it is supplied)? Units: record units, nu = nu_n, delta = delta_n with G nu = C_* delta^3, kappa_c = C_* delta/G; one cell time is delta^2/nu = 1/kappa_c, and the band of K/nu record times is K delta^{-2} cell times. In this item a_c denotes a core radius and a_0 the background axial strain of R2.14 (d).
(a) Proved facts used (for eta smooth, even in r, with M finite, the source and the axis trace integrable in time, and decay at infinity sufficient for the boundary fluxes to vanish; for the impulse also int r^2 |eta| dx finite). (i) Let M(t) = int |eta| dx, dx = 2 pi r dr dz. Transport preserves M; by Kato's inequality for the three-dimensional Laplacian and int sign(eta) (2/r) d_r eta dx = -4 pi int |eta|(0, z) dz, M(t) + 4 pi nu int_0^t int |eta(0, z, s)| dz ds <= M(0) + int_0^t int |d_z(q^2)| dx ds. Per unit height this is only a balance with an axial flux (advective and diffusive), so a segment can import eta produced elsewhere; the source budget used below assumes that an axial interval of length L_z contains all the source material used, otherwise the imports across its ends must be added. (ii) The source d_z(q^2) integrates to zero against every function of r alone for which the integral converges absolutely (its z-integral vanishes at each r), so it contributes neither to Q = int eta dx nor to the impulse P_z = pi int eta r^3 dr dz. The impulse is conserved by the full equation: the viscous term integrates to zero against r^3, since r^3 (eta_rr + (3/r) eta_r) = d_r(r^3 eta_r), and the transport contribution 2 pi int r u^r omega^theta dr dz equals pi int r d_z((u^r)^2 - (u^z)^2) dr dz = 0 when u is the velocity of omega^theta. Q obeys Q' = -4 pi nu int eta(0, z) dz. (iii) The source mass per unit height and unit time is at most 8 pi C_* G nu (Section 2.1), so the integrated absolute source over the band is at most 8 pi K C_* G per unit height; this bounds neither the production from below nor the part converted into coherent rings. (iv) Split eta = eta_r + eta_s as in Theorem 9 (d); a_r, the value of u^r/r for eta_r, satisfies ||a_r||_infty <= C_0/D_n in record units, and the axial strain of eta_r on the axis is -2 a_r(0, z). Since nu_n = D_n/M_n^2 and D_n^3 >= c M_n^5 (the energy inequality), D_n delta_n = (G/C_*)^{1/3} D_n^{4/3} M_n^{-2/3} >= c D_n^{14/15} -> infinity, so the data vorticity contributes o(delta_n) to the axial strain on the axis, uniformly, while the pumping strain is of order C_* delta_n: the axial strain on the axis is that of sourced vorticity up to an error that is small against the pumping amplitude (this is not a relative error at zeros of the pumping strain). This bound does not control the axial gradient of the data strain.
(b) Sizes. In the ring model of R2.14 (d) each ring of the tuned pair has radius R, circulation Gamma_p = 0.9127 C_* delta R^2 and core radius a_c = 7.56e-4 R. The core-scale quantities Gamma_p/(pi a_c^2) = 5.08e5 C_* delta, Gamma_p/(pi a_c^3) = 6.7e8 C_* delta/R and Gamma_p/(2 pi a_c) = 192 C_* delta R suggest, for a smooth core profile, the scale restrictions B delta <= R <= 1/(192 C_* delta) with B between 3.4e8 and 6.7e8 (depending on the profile and on the Hessian norm), compatible for small delta; class (C) itself (a specified smooth profile, the gradient bound, and the full field of both rings throughout the exchange) is not verified here. The pair has eta-mass 4 pi Gamma_p and impulse 2 pi Gamma_p R^2 (1 + O((a_c/R)^2)) (R the circulation-weighted mean radius of each core); thirteen exchanges take 77/(C_* delta) record times, that is 77/G cell times; the nominal diffusion time of its cores is (a_c/delta)^2 cell times, about 6.6e10 at R = 3.4e8 delta, and no operating lifetime preserving the tuning is established.
(c) Provenance. A pair pumps only the axis segment gathered at its centre, of length c_p R, where c_p is an effective pumped fraction, taken between 0.1 and 0.24 in the count below as an assumption. A model measurement gives a much smaller value: in the ring model combined with the cell model (each of 55 release points on [-0.1 R, 0.1 R] followed along its own axis-strain history over about thirteen exchanges, G = 3000, one seed, one wavenumber), the production yield 3 int Pi_s/Sigma_ref(0), accumulated to the cap time of the central release or to the last admissible sample of the release if that is earlier, is at least half its central value (+0.040) only for the sampled releases from 0.004 R behind to 0.005 R ahead of the centre, the yield-weighted width is 0.011 R, releases behind the centre leave the admissible class through the stretch of the base column, releases between 0.014 R and 0.06 R ahead yield less than 1.3 per cent of the central value, and releases 0.07 R to 0.1 R ahead leave the admissible class after strong compression (yields at the last admissible sample up to about 10 per cent of the central value; the exit states are not pumped states) (the release window for E~/E~(0) to reach at least 500 within thirteen exchanges is about 0.014 R wide, R2.14 (d)); with c_p = 0.011 the threshold A below would lie between about 7.4e7 and 1.5e9. Assume that the production requirement c_0 (of order m_phi/P) of the coverage count of R2.14 (d) is met by pumped episodes, each with the per-episode production of the cell model, j_ep G^2 per unit cell length. The number of episodes is then fixed by the requirement, whatever their arrangement in space and time: it is the number obtained when every axial point of a record length L_z is pumped once every T_e cell times over the band, T_e = j_ep G C_* L_z K/c_0, between about 19 and 190 for C_* between 1 and 10 and L_z K/c_0 = 1 (in the cell model j_ep G, and so T_e, is roughly independent of G at a fixed number of exchanges per episode, R2.14 (d)); non-overlapping episodes on a segment require 77/G <= T_e. The per-length count of R2.16 (at saturated circulation, a measure of order c_m/(G C_* nu ell) in record length times record time, c_m > 0 proportional to m_phi/P, ell the logarithm there; smaller circulation over a larger measure is not excluded) is a weaker occupancy condition, met by cores held over L_z throughout the band when c_m/(G C_* ell) <= K L_z; it does not reduce the number of episodes (an earlier version of this count multiplied the need by the occupancy fraction c_m/(G C_* ell K L_z), which is inconsistent with the calibration of T_e, and is withdrawn). If every episode uses a pair of newly sourced vorticity, about K L_z/(delta^2 c_p R T_e) pairs are needed (ignoring overlaps, start and end effects, failed episodes and transport costs), of total eta-mass 4 pi (0.9127) C_* K L_z (R/delta)/(c_p T_e), while the source supplies at most 8 pi K C_* G L_z during the band (vorticity sourced before the band and imports across the ends of the interval are further inventories, not counted here). Both signs of the source can be used, since reflection in z reverses the ring circulation and preserves the axial strain history at the reflected trajectory (whether both signs can be assembled and delivered is not shown). The ratio of need to supply is A/G with A = 0.9127 (R/delta)/(2 c_p T_e). For the family R = B delta with B in [3.4e8, 6.7e8], A lies between 3.5e6 and 1.6e8 (twice that if only one sign could be used), independent of delta, and with the other quantities fixed (T_e roughly independent of G in the cell model) the ratio falls like 1/G: the need does not exceed the source ceiling when G >= A, a threshold between 3.5e6 and 1.6e8 (this does not show that the mass is supplied). The number of fresh pairs, K L_z C_*/(c_p B T_e G nu), diverges as nu_n -> 0, while their total eta-mass stays bounded. For larger fresh pairs the ratio grows like R/delta. In the ring model a pair can be reused for a while: under a slow background strain of zero time mean, fresh material released near the centre received windows of 12 to 19 exchanges once per background period (windows judged at exchange endpoints), and no second full window for the same material appeared within the 150 exchanges inspected (an independent ring-model computation, reproduced in a second computation; sustained reuse is not established, and restored impulse alone does not restore the tangency); if a pair supplied one useful episode per T_e cell times for an operating time T_eff, reuse would divide the number of distinct pairs by about T_eff/T_e, with T_eff <= min(T_op, K delta^{-2}), T_op an operating lifetime that is not established (a long lifetime alone does not give useful repeated coverage).
(d) Assembly and impulse. The instantaneous source is supported where d_z(q^2) is nonzero and has zero signed eta-integral and zero impulse; calling it a dipole describes its sign structure, not a decomposition into coherent rings. In the thin-core energy approximation (energy of order Gamma_ring^2 R (log(b/a_c) + O(1)) for rings of circulation +Gamma_ring and -Gamma_ring, with the cores intact and separated, the circulation fixed, the energy not increasing and the logarithm bounded below) two opposite coaxial rings can raise their radius by their own motion only by a factor of order log(b_0/a_c0) (separation b_0, initial core radius a_c0); this is a model estimate, not a theorem. A radial outflow of the surrounding flow is one assembly mechanism: for a radially uniform axial strain a(t), d log R/dt = -a/2, and expansion from delta to 3.4e8 delta needs -int a dt = 2 log(3.4e8) = 39.3, which the pointwise strain bound permits within the band; it is not shown to be necessary, and other assembly processes are not excluded. Impulse gives no local constraint: the source adds none, but transport exchanges impulse between parts of the vorticity (the transport contribution in (ii) vanishes only for the whole field), so conservation of the total impulse does not exclude compensation by the outer flow that expands a pair (that such a flow carries it is not shown). If instead the compensation is a parked opposite ring of total circulation 2 Gamma_p at radius about R on the axis, its on-axis field Gamma_c R^2/(2 (R^2 + z^2)^{3/2}) for a ring of circulation Gamma_c stays inside the measured tolerances of R2.14 (d) at the pair (a_0 below 3.9e-5 Gamma_p/R^2, gradient below 2.6e-6 or 3.0e-6 Gamma_p/R^3 according to its sign) when its distance exceeds about 22 R (about 17 R for the uniform part alone); this checks the on-axis strain and its axial gradient at the pair centre at one instant (not the whole interaction region, joint perturbations or the later evolution), a freshly sourced partner doubles the eta-mass charged to each pair in (c), and the self-propulsion velocities of the two point away from each other only when the partner is placed on the appropriate side.
(e) Holding. In the survival model of R2.14 (d), between episodes a saturated core needs a mean axial stretching of about 4 kappa_c, that is 4 per cell time (the survival size of R2.14 (d)). Applied as a constant background on the interaction region of the pair, it must meet a_0 < 3.9e-5 Gamma_p/R^2 = 3.56e-5 C_* delta, which gives the nominal condition G >~ 1.12e5. If it varies on the scale R with gradient C_h 4 kappa_c/R, the gradient tolerance gives G >~ 1.69e6 C_h for either sign (1.46e6 C_h for the less restrictive sign); if it varies on a fixed record length the gradient part vanishes as delta -> 0 for R = B delta, but the condition on the uniform amplitude remains. A uniform holding strain of 4 per cell time over the region of a retained pair also contracts the pair (d log R/dt = -a/2, that is -2 per cell time), by a factor e^{-2 T_e} (between e^{-37} and e^{-374}) between episodes; so uniform holding is incompatible with the passive reuse of pairs in (c) (whose test used a background of zero time mean), and with uniform holding the count of (c) takes every pair fresh, assembled against this contraction (a mechanism that re-expands or re-tunes a retained pair is neither constructed nor excluded). In the ring model the restoration that the zero-mean background provides is already lost for a much smaller positive mean: adding to the zero-mean background a mean ambient strain of about a quarter of the uniform tolerance
3.9e-5 Gamma_p/R^2 shortens the windows of fresh material at successive background periods to 14, 7 and 5 exchanges (11, 3 and 2 at the
full tolerance), so these tests suggest that in this geometry reuse without re-tuning needs the time integral of the ambient strain along the pair to stay near zero between episodes (one geometry, ring model; exact restoration of the impulse needs it to vanish, the tolerance for finite reuse was not determined, and other ways of re-tuning were not examined). These thresholds extrapolate the cell runs, which go up to G = 10^4. Holding flows made of two small opposite coaxial rings near the pair's centre give, in the thin-ring model, transient holding with strong dependence on the placement, and the model loses validity as the small rings contract (R2.14 (d)); no lifetime of localized holding is established in either direction. Holding between episodes therefore needs a background that is approximately uniform over the interaction region, or renewal of a localized holder after each episode, or another mechanism; none is constructed, and others are not excluded. An episode lasts 77/G cell times, much less than one cell time for large G; neglecting holding during it is a model approximation, conditional on the pumping trajectory maintaining the core. Holding also acts on the product (two proved statements about prescribed fields, then a model reading; two further comparison bounds under a radial-drift hypothesis follow the numerical test below). First, in the uniform strain b = -2 kappa r e_r + 4 kappa z e_z, the bounded mild solution of d_t eta + b.grad eta = nu Delta_5 eta with eta(0) in L^1(R^3), L^1(R^5) and L^infty satisfies int eta(t) dx = int eta(0) H_t dx with H_t(r) = 1 - exp(-kappa r^2/(nu (e^{4 kappa t} - 1))) (for each fixed T > 0, h(x, u) = H_{T-u}(r) solves -d_u h = b.grad h + nu L h with terminal value 1 for r > 0 and value 0 on the axis for u < T; in three-dimensional measure L is the adjoint of Delta_5 on functions vanishing on the axis, and div b = 0); since the equation preserves positivity, ||eta(t)||_{L^1} <= int |eta(0)| H_t dx, which for kappa = kappa_c and eta(0) supported in r <= C delta is at most C^2 ||eta(0)||_{L^1}/(e^{4 kappa_c t} - 1). Second, for a smooth axisymmetric divergence-free U with U and grad U bounded (only the poloidal part (U^R, U^Z) enters) and a region Omega on which U^R/R <= -kappa throughout an age window [s_0, s], the density chi = psi/R^2 of the rescaled adjoint psi of Theorem 8 satisfies |chi(x, s)| <= E[e^{-2 kappa (s - tau)} |chi(X_tau, tau)|], where X is the associated diffusion started at x and run in physical time (age decreasing) and tau is the age at which it first leaves Omega, or s_0 if it does not leave (the Feynman-Kac formula for the equation of chi, whose zeroth-order coefficient is 2 U^R/R, with stopping at the exit; an inflow on a whole infinite cylinder is impossible for bounded divergence-free U, so the exit term cannot be dropped). Within the survival model, with the holding strain 4 kappa_c prescribed and uniform on an axial interval |z| < Z_h about its stagnation point, vorticity produced in a held core therefore reaches the packet only in the part that leaves the holder axially before it is annihilated at the axis, plus the part still inside at the end of the holding phase, which for product within C delta of the axis and a holding phase of T_e cell times ending before the packet is weighed is at most the fraction C^2/(e^{4 T_e} - 1) of its absolute mass by the first statement: neglecting axial diffusion, a thin ring of product at radius r_0 and signed offset z_0, 0 < |z_0| < Z_h, escapes axially with the fraction 1 - exp(-(kappa_c r_0^2/nu) |z_0|/(Z_h - |z_0|)), at most (r_0/delta)^2 |z_0|/(Z_h - |z_0|) (with axial diffusion the exact fraction is E[H_{tau}(r_0)], tau the first exit of dZ = 4 kappa_c Z dt + (2 nu)^{1/2} dB from |Z| < Z_h started at z_0, and the fraction escaping before the end of a phase of length t_h is E[1_{tau <= t_h} H_{tau}(r_0)]). Neglecting axial diffusion in the same way, for a holder uniform over the interaction region of the pair (Z_h >= R/2), product initially supported in r <= delta and |z| <= 0.005 R about the stagnation point (an assumption on the production profile, suggested by, but not a consequence of, the measurement in (c)) and T_e >= 19, the delivered fraction satisfies f_del <= 1 - exp(-1/99) + 1/(e^{76} - 1), about 10^{-2}; this profile goes with the measured pumped length c_p = 0.011 of (c). For the assumed c_p between 0.1 and 0.24, suppose instead that the absolute eta-mass of the product is distributed uniformly in z over |z| <= c_p R/2, centred at the stagnation point of the holder, and supported in r <= delta; under the same holding assumptions this gives f_del <= -1 - log(1 - c_p)/c_p + 1/(e^{76} - 1), between about 0.054 and 0.144. If the count in (c) is made with delivered instead of produced vorticity, its threshold G >= A becomes G >= A/f_del, so at least about 100 times larger for the measured pumped length and at least about 7 to 19 times larger for the assumed one: a larger necessary condition, not an exclusion, and no sufficient condition on G follows. Compact holders of axial extent a few delta, if they can be renewed after each episode, may avoid this factor when production occurs at radii and axial offsets comparable to delta; survival through successive holders and delivery to the packet remain unproved. In the same prescribed-flow model the return flow of a compact holder of radius rho delta exceeds the diffusive velocity nu/r only out to a radius of order rho^2 delta (thin-ring far-field order estimate, not proved for smooth holders); this balance radius is not a transport cutoff. If product released with radial support in r <= c rho^2 delta were then evolved by the pure 5D heat flow for T cell times, the exact no-flow law of that flow (the three-dimensional mass of eta at time t is int eta_0 (1 - e^{-r^2/(4 nu t)}) dx) would bound its delivered fraction by min(1, c^2 rho^4/(4T)). The comparison with pure diffusion is not proved for the holder flow (where U^r > 0 the pure-diffusion weight w_0 = 1 - e^{-r^2/(4 nu t)} is not a supersolution, its residual being -U^r d_r w_0 < 0, so this comparison supplies no upper bound and a drift below nu/r can still change the law; several renewed holders are not one holder), and identifying T with the production age is a further assumption; so nothing is established about delivery by compact holders, and no need for phases of radial outflow follows (re-concentrating the swirl by inflow would also bring back product not separated from it first). In one numerical test of the adjoint in a prescribed holder flow (cell units nu = delta = kappa_c = 1; a stream function with C^1 cutoffs, supported in radius 3 and axial half-length 3, with axial stretching 4 in its inner region, alone or in an axial array of five; a packet concentrated at radii 6 to 8 and |Z| <= 3; an explicit first-order scheme), the weight at radius about 1, on the finest grids used (at ages 4 and 16), was lower than without flow by a factor of at most about 1.5 at the centre of a single holder and higher by factors of about 3.5 to 4 near its ends and of about 6 to 10 near the ends of the central holder of the array; across the grids used the enhancement factors decrease (by up to about a factor 2.1 between the two coarser grids), the reduction at the centre strengthens at age 4, and at age 16 a mild enhancement on the coarsest grid (factor 1.1) becomes a mild reduction (factor 1.1); the probe points move slightly with the grid, and none of these factors is converged. At these points and ages the computed reduction is modest compared with the suppression predicted by the survival weight H_t of the first statement above for a uniform strain with the same axial rate (for phi = 1, at radius 1 and age 4, about 10^{-7} against about 0.06 without flow), in line with the remark that compact holders may avoid that factor; this does not determine the delivered fraction, and it is model evidence for one parameter set at a few points, not a bound. For the actual rescaled adjoint, if R U^R <= theta nu on {R < R_*} for all Z and ages up to s (0 < theta < 2) and phi is supported in {R >= R_*}, comparison with ||phi||_infty (R/R_*)^{2-theta}, whose residual is (2 - theta) ||phi||_infty R_*^{theta - 2} R^{-theta} (theta nu - R U^R) >= 0, gives |psi| <= ||phi||_infty (R/R_*)^{2-theta} there. The same hypothesis, now with 0 <= theta < 2, gives an age law: w(R, s) = P(1 - theta/2, R^2/(4 nu s)), with P the regularized lower incomplete gamma function (the probability that a Bessel process of dimension theta with diffusivity nu started at R has not reached 0 by time s), solves d_s w = nu (w_RR + (theta - 1) w_R/R), increases in R, equals 1 at s = 0 for R > 0, and has residual w_R (theta nu - R U^R)/R >= 0 for the adjoint equation (checked by computer algebra), so for any bounded phi comparison with ||phi||_infty (w + (R/R_*)^{2-theta}) (on {epsilon < R < R_*}, starting at an age s_0 > 0 with w(R, s' - s_0) at age s', and a constant of order epsilon^2, depending on s_0 and s, added for the inner boundary; first epsilon, then s_0 go to 0) gives |psi(R, Z, s)| <= ||phi||_infty (min(1, (R^2/(4 nu s))^{1 - theta/2}/Gamma(2 - theta/2)) + (R/R_*)^{2-theta}) on {R < R_*}, without the second term if the hypothesis holds for all R. For theta = 0 the hypothesis excludes outward radial velocity on {R < R_*}, and when it holds for all R the bound is the pure-diffusion upper bound; if the hypothesis holds for all R and all ages, the bound decays at fixed R like s^{-(1 - theta/2)} instead of s^{-1}, while for finite R_* the term (R/R_*)^{2-theta} does not decay (for the line-source drift U^R = theta nu/R, U^Z = 0, divergence-free off the axis but unbounded, the radial operator is that of the Bessel process, which does not reach the axis when theta >= 2). The hypothesis can fail where the return flow of a holder has R U^R > theta nu, so this does not turn the conditional model estimate into a statement about Case 2. The delivery estimates for a uniform holder assume a holding strain uniform in space and time over the holder, whereas the requirement above concerns only its mean, and they do not cover histories with phases of radial outflow; the two comparison bounds just stated need only their stated hypotheses, not a uniform strain. None of these gives an exclusion.
(f) Reading. For the family R = B delta, the scalar budget ratios evaluated in (b) to (e) have no adverse power of 1/nu_n: with the other parameters fixed, each is met as delta_n -> 0 or is a finite nominal threshold on G (with fresh pairs) or on reuse (which uniform holding excludes for passive pairs, (e)). The numbers of episodes and of fresh pairs and the strain accumulated by a uniform holder diverge as nu_n -> 0; these are not budget contradictions, but they are what the open questions below must supply. The calculation compares scale estimates and gross budgets with necessary conditions: it does not verify the interpolation cap along an evolving solution, a lower bound on the actual production of an episode, the signed self-compression, or the delivery with the adjoint weight, it does not certify the measured tolerances jointly or for time-dependent perturbations, and it does not show that the scenario is compatible with all Case 2 requirements. It has not produced an exclusion. Open questions for this scenario include (i) the assembly of sourced vorticity into tuned pairs of radius R = B delta_n, with B between about 3.4e8 and 6.7e8 by the scale estimates of (b), with pair parameters close enough to the tuned values to keep the measured pumping, (ii) the holding of saturated cores between episodes, (iii) the repetition of episodes over K delta_n^{-2} cell times, and (iv) the delivery of the produced eta to the packet with the adjoint weight. The list is not exhaustive, an obstruction could also come from stronger quantitative or geometric estimates, and excluding this scenario alone would not exclude Case 2. Nothing here constructs a history realizing (i) to (iv).

R2.18 The open problem in one statement (a summary of the reductions proved in R2.16 and Theorem 9 and of the model evidence of R2.8 to R2.14, together with one order-of-magnitude estimate and one further unpumped run reported in (c5); no new theorem).
(a) Exact form. Fix a finite-energy axisymmetric solution satisfying (A) and NO-SWIRL-EXTRACTION and a record sequence with alpha_n -> alpha_* < infinity along which the rescaled flows converge to a bounded, nonconstant, no-swirl ancient Euler flow with packet phi, m_phi > 0 and P = ||phi||_infty. By R2.16, Case 2 along this sequence forces nu_n int_0^{t_n} Pi_s dt >= (2 m_phi/(3P)) (1 - o(1)), and the bound limsup_n nu_n int_0^{t_n} Pi_s dt < 2 m_phi/(3P), equivalently limsup_n nu_n (Sigma(t_n) + int_0^{t_n} D_Sigma dt) < 2 m_phi/P, excludes it. Excluding Case 2 on the trajectory therefore amounts to proving this one inequality, for every such sequence, by an argument independent of the lower bound: together with the lower bound it is a contradiction, so it can hold for every such sequence only if there is none (a reformulation, not a quantitative theorem), and along every such sequence of a counterexample trajectory it fails. The inequality concerns a single signed quantity, the time-integrated compression of the swirl by the strain of the vorticity the swirl has itself produced, measured against a definite constant times 1/nu_n; the dissipation-normalized condition (ii) of R2.16 is sufficient but stronger: it is equivalent to bounded stored plus dissipated swirl, which fails at every singular time because int_0^{T_*} D_Sigma dt is then infinite (R2.16), so it would exclude every singularity of the trajectory and is not an equivalent formulation of this target.
(b) Where the inequality can fail (a proved circulation count and a conditional Burgers-core reading). By the per-length count of R2.16, Case 2 needs an axial space-time integral, of order 1/C_*, of the record circulation gamma of that count (maximized in R and over unit axial distance) weighted by ell_n + log(g_n/gamma), with ell_n the logarithm of that count and g_n = G nu_n, or terminal swirl over an axial extent of order nu_n^{-2/3} record lengths; at saturated circulation (comparable to G nu_n) the first is a measure of order 1/(G C_* nu_n ell_n) in record length times record time, and smaller circulation over a larger measure is not excluded. For a core saturated in the sense of the interpolation cap and read as a Burgers core, the radius is of order delta_n = (G nu_n/C_*)^{1/3} and the holding strain of order nu_n/delta_n^2 in record units (a_B = a_0 = 4 per cell time, the survival strain of the reference core of the runs, R2.14 (d)). The strain of the data part of the vorticity on the axis is o(delta_n) (R2.17 (a)), so at axis points where the total axial strain is at least c delta_n in modulus (c > 0 fixed independently of n), as for the pumping strains on the axis in (c), it is that of the sourced vorticity up to a relative error that tends to 0 uniformly.
(c) Model form (evidence, not an equivalence). In the cell models of R2.8 to R2.14 an isolated saturated core is not sustained in the runs tested, while in the runs tested a core is pumped by axial strain with enough power near twice its first Kelvin frequency, 2 omega_1 = 1.06 k C_* delta_n in record units at k = 1, k the axial wavenumber of the core mode in units of 1/delta_n, in the two forms (c1) and (c2) below (no general spectral criterion is established). Here Omega = omega_1 + omega_2 is the sum of the first two Kelvin frequencies of the same core, 0.83 k C_* delta_n in record units at k = 1, so that 2 omega_1 = 1.28 Omega.
(c1) Coherent strain. In the linear model of R2.14 at G = 5000 a peak strain amplitude beta Omega with beta = 0.03 gives transient amplification of a core and beta = 0.05 growth continuing over the tested interval (no threshold is established); the tuned ring pairs of R2.14 (d) supply strain impulse 0.087 to 0.233 (0.159 to 0.233 for the pairs that reach the cap), and in one nonlinear cell run a single episode reaches the interpolation cap within 0.025 cell times.
(c2) Broadband strain. In the linear model a core is also pumped by spatially uniform multitone strain with random frequencies and phases of root-mean-square size sigma Omega with sigma about 0.1 to 0.2 at G = 5000 (realization-dependent), with a heuristic weak-noise break-even sigma of about 0.12 to 0.13 at G = 5000 scaling as G^{-1/2}, equivalently, within that frozen estimate averaged over the random frequency draws, a one-sided strain spectral density near 2 omega_1 of about 15 to 20 kappa_c in record units, the coefficient being approximately independent of G in the runs tested (R2.14 (vii); no empirical break-even of the long-time growth rate has been determined; for twelve-draw ensembles, unweighted fits of the sample mean of log(E(0.1)/E(0)) against sigma^2 give unit crossings 0.295, 0.108 and 0.062 at G = 1000, 5000 and 20000, and the corresponding values of the estimate, 0.257, 0.120 and 0.061, lie within their marginal 90 per cent bootstrap ranges).
(c3) Further resonances under broadband strain. For such broadband strain, pair resonances at sums of two distinct Kelvin frequencies of the core can also contribute in a weak-noise description, with coherent couplings (pairs among the first four modes, k = 1) at most about a tenth of that of the first subharmonic resonance per unit log-stretch amplitude (in the mean first-mode energy rate of the frozen-coefficient theorem quoted in R2.14 (vii), the unbroadened leading coefficients of the pairs (1, j), j = 2, 3, 4, are at most about 0.77 per cent of the first-subharmonic coefficient (not a bound on the broadened contributions for arbitrary spectra), and pairs without the first mode do not enter it at that order; typical-energy pair coefficients are not established), while the subharmonic couplings of modes 2, 3 and 4 (0.64, 0.47 and 0.36 of the first) exceed every pair coupling among the first four modes. In the channel-separation runs of R2.14 (vii) (matched ensemble spectral density, G = 5000, T = 0.1) E(T)/E(0) exceeded 1 in four of six draws on the sub-band containing 2 omega_1 and in one of six on the sub-band containing 2 omega_2 and the pair sums omega_1 + omega_j at or above 0.64 Omega, where all six late slopes were negative; these independent samples do not resolve the individual channels.
(c4) Candidate mechanism. These models suggest the following candidate mechanism for the failure of the inequality of (a), without establishing its necessity or sufficiency: (Q) the sourced vorticity of the trajectory produces, on a set of saturated cores of the measure in (b), an axial strain whose power near twice the local first Kelvin frequency (and, for broadband strain, near twice the higher local Kelvin frequencies and near sums of two distinct local Kelvin frequencies, where these lie in the band considered) exceeds the model break-even, while (A), the circulation bound and the interpolation cap hold, and the eta produced there reaches the packet with the weight of the backward adjoint. The required oscillating strain is of order 0.02 to 0.25 C_* delta_n in the models at k = 1 (peak beta Omega about 0.025 at the tested transient-amplification level beta = 0.03 of R2.14, root-mean-square 0.08 to 0.17 for the multitone ensembles, and log-stretch impulse times 2 omega_1 about 0.09 to 0.25 for the tuned ring pairs; these are scales, not pointwise bounds), at frequencies of order C_* delta_n in record units, far below the velocity-gradient bound |grad U_n| <= 1 in amplitude; its compatibility with the Hessian bound |grad^2 U_n| <= C_* depends on the spatial scale of the straining vorticity (a strain of size C_* delta_n varying on the record-unit scale l has Hessian of order C_* delta_n/l, of order C_* at the cell scale), joint admissibility with the core and the outer flow is not established, and none of the bounds proved here decides (Q). (Q) becomes a mathematical condition only once the frequency band, the time window, the normalization and the growth criterion are fixed; in the models they are those of R2.14, with frequencies drifting as the core spreads.
(c5) Pumping between segments. One collective reading of (Q), in which separated
saturated segments pump each other through the vorticity produced by their own swirl sources, was estimated to order of magnitude in the
cell model (an estimate, not a theorem): that vorticity is an axial derivative of a localized field, so it has zero ring impulse and its
on-axis strain at distance d decays like its first axial moment divided by d^5, and its component at twice the Kelvin frequency is
quadratic in the cell amplitude; under these localization, zero-impulse and direct-response assumptions the induced strain at a segment
separated by at least twice the segment length is more than three orders of magnitude below the imposed strains with which pumping was
observed in the models. The estimate does not bound the coupled response of a nonuniform base and does not exclude pumping between
segments by other means. In one further unpumped run of the cell model on a long periodic column (G = 3000), a localized packet of cell
perturbations (seeded with nonzero impulse) spread along the column at the inertial group velocity (first-arrival speeds 1240 to 1550 cell lengths per cell time against the
computed group velocity 1236, about 0.4 G), so cell energy propagates along one continuous column on the inertial time scale (no inference about coupling between separate segments is drawn); the axis strain at the stations had RMS 50 to 114 per cell time, with lock-in amplitude 11 to 79 at the first Kelvin
frequency and 0.5 to 12 at twice that frequency, against initial oscillating strain amplitudes of about 75 and 125 per cell time in the G = 3000 runs of R2.14 (b)(iii) (beta = 0.03 gives transient amplification and beta = 0.05 gives growth continuing through t = 0.1; at d = 1.27 the corresponding log-stretch amplitudes beta/d are about 0.024 and 0.039, and the initial value of 2 omega_1 is about 3186)
(one run, its diagnostics rechecked independently from the recorded data; the origin of the twice-frequency content is not separated; the periodic box cannot resolve the free-space decay law used in the estimate above).
(d) What a resolution needs. One model-motivated input for an exclusion, absent from this report, is an upper bound, below the model break-even (for a stated spectral normalization, time window and growth criterion), on the time-integrated power near 2 omega_1 (and near twice the higher Kelvin frequencies and near sums of two distinct ones, where these lie in the band considered) of the self-produced strain at saturated cores (its sufficiency for the full exclusion argument is not proved); others would use the localization, back-reaction or admissibility of the straining vorticity; or the inequality of (a) may be proved directly by another route. A counterexample requires a fixed datum whose solution is shown to become singular with a record sequence of the stipulated branch; in the model scenario this means realizing (Q) over K delta_n^{-2} cell times (ages up to K/nu_n, K fixed) for every n, with delivery of the produced eta to the packet, a requirement of that scenario, not a proved requirement for every counterexample. Neither is available. (Q) is not proved to be necessary or sufficient for the failure of the inequality in (a): it depends on the cell models, which do not contain the collective dynamics of the sourced vorticity.

## 1. Result

**Setting.** u is the maximal smooth solution of the 3D Navier-Stokes equations (viscosity 1) on R^3 x [0,T_*), 0 < T_* < infinity,
with one fixed smooth axisymmetric decaying datum u_0 in H^infinity, E_0 = ||u_0||_2^2 < infinity, G = ||r u_0^theta||_infty < infinity.
Notation: Gamma = r u^theta, q = u^theta/r, eta = omega^theta/r, b = u^r e_r + u^z e_z, Delta_5 = d_rr + (3/r) d_r + d_zz,
L = d_rr - (1/r) d_r + d_zz, dx = 2 pi r dr dz. M, S, D, H are the historical suprema over [0,t] of |u|, |u^theta|, |grad u|,
|grad^2 u| (Cartesian Frobenius norms). Branch hypotheses: (A) M H <= C_* D^2 for late times (by F2, (A) at a late time t with D(t) > 0 requires C_* >= 0.2700..., and the nonconstant Case 2 alternative requires C_* >= 7^{1/2}/8 = 0.3307...); NO-SWIRL-EXTRACTION: no sequence of
first-crossing swirl records (x_n, t_n) (t_n -> T_*, x_n = (r_n, 0, z_n), |u^theta(x_n, t_n)| = S(t_n) =: S_n > S(t) for t < t_n), and no
subsequence of one, admits both witnesses (W1) |W_n| <= K on every fixed normalized cylinder (intersected with the rescaled history, where W_n is defined), with one K for all cylinders and all n, and
(W2) lim_{L -> infinity} limsup_n sup_{-A <= tau <= 0} int_{|y| > L} |W_n(y, tau)|^2 |y|^{-4} dy = 0 for every A < infinity, where
W_n(y, tau) = S_n^{-1} u(r_n y', z_n + r_n y_3, t_n + (r_n/S_n) tau), y = (y', y_3); Case 2: genuine first-crossing
gradient records (x_n,t_n) (t_n -> T_*, x_n = (r_n,0,z_n), |grad u(x_n,t_n)| = D(t_n) =: D_n > D(t) for t < t_n, so D_n -> infinity), with
alpha_n = r_n/l_n -> alpha_* < infinity, l_n = M_n/D_n, nu_n = D_n/M_n^2. The energy inequality gives E_0 >= (pi/768) M_n^5/D_n^3 (Section 3,
F5), so l_n <= C(E_0) D_n^{-2/5} -> 0 and M_n/D_n^2 <= C(E_0) D_n^{-7/5} -> 0.
Rescaled fields U_n(y,tau) = u(a_n + l_n y, t_n + tau/D_n)/M_n with a_n = (0,0,z_n); eta_n, gamma_n, q_n are the
corresponding rescaled quantities, so that eta = (D_n^2/M_n) eta_n, Gamma = gamma_n, q = D_n q_n, U_n^theta = nu_n gamma_n / R. Here M_n = M(t_n), D_n = D(t_n),
H_n = H(t_n), y_n = (alpha_n, 0, 0) is the rescaled record point and y_* = (alpha_*, 0, 0).

**Theorem 1 (reduction, proved).** Under these hypotheses:
(a) S(t)/M(t) -> 0 (B1) and D(t)/M(t)^2 -> 0 (B2).
(b) Let p be the canonical physical pressure and put p_n(y, tau) = M_n^{-2} p(a_n + l_n y, t_n + tau/D_n). For all sufficiently large n, on the whole available rescaled past (-t_n D_n <= tau <= 0), |U_n| <= 1,
|grad U_n| <= 1, |grad^2 U_n| <= C_* and |grad p_n| + |d_tau U_n| <= C(1+C_*), and along a subsequence U_n and grad U_n converge locally
uniformly on R^3 x (-infinity,0] (terminal time included) to a bounded, C^{1,1}_x, nonconstant, axisymmetric, swirl-free Euler solution U
with |grad U(y_*,0)| = 1 (U is Lipschitz in time and d_tau U + U.grad U = -grad p_E almost everywhere, with grad p_E bounded and curl-free, the distributional limit of grad p_n).
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
Put Q_4(I) = int_I int q^4 dx dt, Q_4(t) = Q_4([0,t]) and, for a space-time set E, Q_4(E) = int int_E q^4 dx dt. Once B, kappa and phi are fixed,
the constant c in A_max(n) of Theorem 2 is decreased, and N increased, depending on them (as 2.6 and 2.7a require: the source term on the
window is at most C C_* G nu_n A_max(n)^2 + o(1) <= C c^2 + o(1)); A_max(n) denotes this reduced window here and in Theorems 5 and 6. Then:
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
    the part of I_n x {r < lambda_n} alone carries at least (3/2) kappa m - o(1) of the pairing in (b) and has
    Q_4 >= (25/8) kappa^2 m^2 D_n M_n / ||phi||_2^2 (1 - o(1)); consequently
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
    Hence the middle history of Theorem 3(e), and its tube in 3(f), carry int int q^4 w_n^{-alpha} >= c_alpha D_n M_n. By (a) and the energy identity (the weighted bound gives only the exponent -alpha/2),
    the part of the pairing older than h is at most C (Q_4([0, t_n - h])/(D_n M_n))^{1/2} (1 + h/l_n^2)^{-3/4}.
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
W(t) = int_0^t int a_- q^2 r dx ds (a_- = max(-a, 0)), Abar(t) = int a q^2 r dx / Sigma(t) (Abar = 0 where Sigma(t) = 0) and Act(t) = sup_{0 <= s <= t} int_0^s (- Abar) (scale invariant).
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
(e) In rescaled variables W(t_n) = nu_n^{-2} int int (U_n^R/R)_- q_n^2 R dy dtau over the rescaled history, so (b) asks for rescaled work of order nu_n.
    This is the order produced by cells of radius delta_n = (G nu_n/C_*)^{1/3} with saturated swirl |q_n| ~ C_* delta_n and compression nu_n/delta_n^2 (the cell units of the Round 2 items)
    over a fixed axial length and a rescaled time 1/nu_n: the reduction is critical in the sense of this conditional scale count (it does not
    show that such cells persist or are realized by a solution).
In the rescaled frame a_r = O(1/D_n) (its integral over the rescaled history of length t_n D_n is controlled by the Gronwall step of (d)), so by (d)
Case 2 requires the swirl to compress itself through the vorticity it has generated, in the sense int_0^{t_n} (Pi_s)_+ dt >= c/nu_n, where (Pi_s)_+
is the positive part of the spatial integral Pi_s (no matching upper bound is proved). Any bound nu_n int_0^{t_n} (Pi_s)_+ dt -> 0 for the coupled
solution would exclude Case 2, and so would the weaker signed bound limsup nu_n int_0^{t_n} e^{3 C_0 (t_n - t)} Pi_s(t) dt < 2 m_phi/(3P),
which tolerates compression of order 1/nu_n provided it is sufficiently offset by expansion carrying the same weight. By R2.16 the weight can be dropped: this signed bound is equivalent to limsup nu_n int_0^{t_n} Pi_s dt < 2 m_phi/(3P) and to limsup nu_n (Sigma(t_n) + int_0^{t_n} D_Sigma dt) < 2 m_phi/P, D_Sigma the dissipation of the swirl balance (R2.16). In a drift-free model with prescribed swirl, F10 (c) gives an axially periodic steady example with negative
critical-weight work, and Appendix B a localized whole-space family, started from zero sourced vorticity and obeying the three spatial
velocity bounds of Theorem 1(b) and |Gamma| <= G, with nu int (Pi_s)_+ dt >= c; so in that model the three spatial velocity bounds and the
circulation bound do not imply nu int (Pi_s)_+ dt -> 0. Appendix C proves the same when eta_s is transported by its own poloidal
velocity, with q still prescribed. In both families the velocity and its gradient tend uniformly to zero and there is no normalized gradient record; neither solves the Navier-Stokes system. This does not settle the signed weighted threshold under the Case 2 hypotheses. The question for the
coupled evolution remains open.

**Proposition 4 (conservation structure, proved under the additional solution hypothesis (DEC): eta, grad eta,
r^2 eta, |u||omega|, Gamma grad Gamma are in L^1(R^3) locally uniformly in time, and int |eta(0,z,t)| dz is locally integrable in time).**
(a) For every f in C^2, t -> int eta f(Gamma) dx is locally absolutely continuous on [0, T_*), and for almost every t,
    d/dt int eta f(Gamma) dx = int eta f''(Gamma) |grad Gamma|^2 dx + 2 int eta f'(Gamma) L Gamma dx
    - 4 pi f(0) int eta(0,z,t) dz. The swirl source drops out exactly, because f(Gamma) d_z(q^2) = r^{-4} d_z K(Gamma), K' = 2 s f.
(b) int r^2 eta dx (twice the axial impulse) is conserved.
(c) ||eta(t)||_{L^1} <= ||eta_0||_{L^1} + int_0^t ||d_z(q^2)||_{L^1} ds.

**Corollaries (proved).** In Case 2:
(i) sup_{s < t_n} D(s)(T_* - s) >= c (C_* max(G,1) nu_n)^{-1/4} -> infinity: the gradient blow-up is of Type II at a quantified rate.
(ii) ||eta(t_n)||_{L^1(R^3)} >= c/nu_n -> infinity (the norm may be infinite), and int_0^{T_*} ||d_z((u^theta/r)^2)||_{L^1(R^3)} dt = infinity
(a scale-invariant quantity; by Theorem 9(b), without (DEC)); any regularity mechanism bounding this time integral excludes Case 2.
(iii) The whole-history source budget 16 pi P G nu_n int_0^{t_n} H(t) (l_n L + int_t^{t_n} M(s) ds) dt >= m_phi - o(1) holds (P = ||phi||_infty,
phi supported in |Z| < L, Section 2.7d); in particular int_0^{t_n} H(t) (l_n L + int_t^{t_n} M + sqrt(t_n - t)) dt >= c M_n^2/(G D_n).
(iv) ||grad^2 p(t)||_infty <= C(1+C_*) D(t)^2 under (A), so D' <= C(1+C_*) D^2 a.e.; this is a lower bound on the past gradient only.
(v) Q_4(t_n) = o(D_n M_n) along the Case 2 sequence would exclude Case 2 (Theorem 3(d)).
(vi) There is y_0 with R_0 = |y_0'| > 0 and U(y_0,0) != 0; then (R_0 l_n) |u(a_n + l_n y_0, t_n)| >= c/nu_n -> infinity, so
sup_x r|u(x,t_n)| >= c/nu_n. (At the record point itself r_n |u(x_n,t_n)| = (alpha_n/nu_n)|U_n(y_n,0)| is at most alpha_n/nu_n, which is o(1/nu_n) if alpha_* = 0; by F2, alpha_* = 0 can occur only when C_* >= 2^{1/2}/3.)

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

2.3 Compactness. (A) at the single time t_n (a late time once n is large) bounds grad^2 U_n on the whole past since H is historical; the bound on d_tau U_n also uses nu_n <= 1, true for large n by (B2). The canonical pressure is
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
only bilinear terms in (U_n, omega_n), all converging locally uniformly; the swirl source enters its azimuthal component as R d_Z(q_n^2),
and the source d_Z(q_n^2) of the eta equation itself tends to zero uniformly, the axis included, since |d_Z(q_n^2)| <= 4 C_*^{5/3} (G nu_n)^{1/3} (Section 2.1). Since omega_U is Lipschitz in space-time, the Lagrangian form gives
D_tau (omega^theta/R) = 0 along almost every off-axis path, hence along every one by continuity of eta_U and of the flow in the initial point; |U^R| <= R keeps particle paths off the axis (no axis trace of eta_U is claimed).
Nontriviality: omega_U(.,0) = 0 would make U(.,0) a bounded harmonic gradient, hence constant.

2.5 LOWER. Transport a solid torus where |eta_U(0)| >= 2 kappa backward by the measure-preserving flow; it stays in
|Z| < L + A; at most half of its 3D volume v fits in {R < rho} if 2 pi rho^2 (L+A) = v/2; on the remaining portion, where R >= rho, |omega| >= 2 kappa rho.
Then |grad U(y,-A)| <= d(A) pointwise gives c_U (1+A)^{-1/2} <= sqrt2 d(A).

2.6 WINDOW. Lift eta_n to R^5 (R = |w|, w in R^4), where it solves d_tau eta + U.grad_5 eta = nu Delta_5 eta + d_Z(q^2) with
smooth coefficients and div_5 U = 2U^R/R. Solve the backward adjoint -d_tau chi - div_5(U chi) = nu Delta_5 chi with
chi(0) = phi/(pi R^2). Then psi = pi R^2 chi satisfies
   int eta_n(0) phi = int eta_n(-A) psi(-A) + int_{-A}^0 int d_Z(q_n^2) psi,
with psi >= 0, int psi = int phi (5D mass conservation, no axis flux), psi <= ||phi||_infty (psi solves a drift-diffusion
equation with operator d_RR - (1/R) d_R + d_ZZ and no zeroth order term, vanishing on the axis). Axial tails are controlled by comparison. Write Phi = ||phi||_infty and s = -tau >= 0 for the age; phi is supported in {|Z| < L}, and psi satisfies d_s psi = nu_n L psi + U_n.grad psi. Since |U_n^Z| <= 1, the function g_s(Z) = Phi exp(-((|Z| - L - s)_+)^2/(4 nu_n s)) is a supersolution: it is C^1 in Z and independent of R, so L g = g_ZZ; on {|Z| <= L + s} it is constant; and with x = |Z| - L - s > 0 one has d_s g - nu_n g_ZZ - |g_Z| = g/(2s) > 0. The maximum principle (psi vanishes on the axis; replacing s by s + epsilon in the denominator of g gives the ordering at s = 0, and epsilon -> 0 afterwards) yields 0 <= psi(R, Z, -s) <= g_s(Z). In detail: the comparison is run on the outer region {|Z| > L + s}, where g is smooth and a strict supersolution, with boundary values psi <= Phi = g on |Z| = L + s (plain maximum principle for psi), psi = 0 < g on the axis, and psi = 0 at s = 0 there; this avoids the kink of g at |Z| = L + s. The axis condition is legitimate because psi = pi R^2 chi with |chi| <= e^{2A} ||chi(0)||_infty on the window (the zeroth-order coefficient 2 U^R/R of the chi equation is bounded by 2 |grad U| <= 2), so psi -> 0 as R -> 0 uniformly, and |psi| <= pi e^{2A} ||chi(0)||_infty R^2 grows at most quadratically. The maximum principle on the unbounded region, used for psi >= 0, for psi <= Phi and for psi <= g_s, holds for functions of at most quadratic growth by adding the barrier epsilon' e^{lambda s} (1 + rho)^2, rho = R^2 + Z^2, with lambda > 12 nu_n + 4: L applied to (1 + rho)^2 gives 4 (1 + rho) + 8 rho <= 12 (1 + rho)^2, and since |U_n| <= 1 (Theorem 1 (b)) the drift term is at most |grad (1 + rho)^2| = 4 (1 + rho) rho^{1/2} <= 4 (1 + rho)^2. The difference of the two functions minus the barrier then tends to -infinity at spatial infinity, uniformly for s in [0, A], so a positive maximum would be attained at an interior point, where the strict supersolution inequality fails; epsilon' -> 0 afterwards. Thus 0 <= psi <= g_s, with int g_s dZ = 2 Phi (L + s + (pi nu_n s)^{1/2}) <= 2 Phi (L + s + 1) whenever pi nu_n s <= 1; this holds for all s <= A <= A_max(n) once n is large, since nu_n A_max(n) -> 0. The source term is therefore at most int_0^A int g_s(Z) (2 pi int_0^infty |d_Z(q_n^2)| R dR) dZ ds <= 8 pi C_* G nu_n int_0^A int g_s dZ ds <= 16 pi Phi C_* G nu_n A (L + A + 1), by the radial source mass. For the past term put f(Z) = 2 pi int_0^infty psi(R, Z, -A) R dR, so int f dZ = m; since 0 <= psi(-A) <= g_A(Z), the bathtub principle gives 2 pi int_0^infty psi(R, Z, -A) dR <= 2 (pi f(Z) g_A(Z))^{1/2}, and with |eta_n(-A)| <= ||omega^theta_n(-A)||/R and Cauchy-Schwarz in Z, |int eta_n(-A) psi(-A)| <= ||omega^theta_n(-A)|| int psi(-A) R^{-1} dy <= 2 ||omega^theta_n(-A)|| (pi m int g_A dZ)^{1/2} <= 2 sqrt(2 pi) ||omega^theta_n(-A)|| sqrt((L+A+1) m Phi). Comparing with int eta_n(0) phi >= (3/2) kappa m gives Theorem 2 as long as C_* G nu_n A (L + A + 1) is small, which holds on the window for c small and n large.

2.7 Whole-history adjoint (Theorem 3). The same adjoint, now in physical variables on the entire interval [0,t_n], is
Psi_n = r^2 chi with -d_t chi - div_5(b chi) = Delta_5 chi; its rescaling is exactly the psi of 2.6 on every recent window.
Multiplying the backward equation by Psi_n and integrating in dx: the drift term vanishes (div b = 0), and for L = Delta_3 - (2/r) d_r
the extra term is -2 pi int [Psi^2]_{r=0}^{infinity} dz = 0 because Psi_n vanishes on the axis, so
(1/2) d/dt int Psi_n^2 = int |grad Psi_n|^2, which integrates to the energy bound (a). The integration by parts formula
int (Delta_5 eta) g dx = int eta L g dx - 4 pi int eta(0,z) g(0,z) dz (radial part: int (eta_rr + 3 eta_r/r) g r dr =
-2 eta(0) g(0) + int eta (g_rr - g_r/r) r dr) with g = Psi_n, g(0,z) = 0, gives d/dt int eta Psi_n = -int q^2 d_z Psi_n, hence (b).
The scaling identities nu_n l_n^3 = M_n/D_n^2 and nu_n^2 l_n^3 = 1/(D_n M_n) turn (b) and Cauchy-Schwarz into (c) and (d).
For (e), the left side of (b) tends to m_phi >= 2 kappa m and the first term on the right of (b) tends to 0. The recent part [t_n - A_n/D_n, t_n] equals the source term of 2.6 and, after the reduction of c, is at most kappa m/4 + o(1) uniformly in 0 <= A_n <= A_max(n); the early part [0, s_n] is at most ||phi||_2 (Q_4([0, s_n])/(2 D_n M_n))^{1/2} = o(1) by (c). Hence I_n carries at least m_phi - kappa m/4 - o(1) >= (7/4) kappa m - o(1) (the full lower bound m_phi >= 2 kappa m is needed here), and (c) on I_n gives Q_4(I_n) >= 2 D_n M_n ((7/4) kappa m)^2 ||phi||_2^{-2} (1 - o(1)), which is the stated (49/8).
For (f), |q| = |Gamma|/r^2 <= G/r^2 and q^2 <= |grad u|^2 give int_{I_n} int_{r >= lambda} q^4 <= G^2 lambda^{-4} e_n. At lambda = lambda_n this is
at most G^2 D_n M_n/K^4, so the Cauchy-Schwarz step of (c), applied on the set I_n x {r >= lambda_n} (it uses only the set, as in
Theorem 6(b) with alpha = 0), bounds the pairing there by ||phi||_2 G/(2^{1/2} K^2) <= kappa m/4; subtracting from (e) gives the pairing
statement, and Q_4 of the tube is at least (49/8 - 1/8) kappa^2 m^2 D_n M_n/||phi||_2^2 (1 - o(1)), more than the stated (25/8).
For (g), the source term of the window identity is bounded by (c) instead of the radial source mass, and the tails by the
Gaussian moment bound with h = L + A_n + 1 + C (nu_n A_n)^{1/2} (for lambda > 0 and either sign, int e^{+-lambda Z} psi(-A_n) dy <= m e^{lambda L + (lambda + nu_n lambda^2) A_n}, so the mass of psi(-A_n) in {|Z| > h} is at most 2 m e^{-C^2/4}; since |eta_n| <= sqrt2 C_* everywhere, the tail contributes at most kappa m/4 for C = C(C_*, kappa)). The L^2 identity for eta (transport drops out since div b = 0, and
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
For (c), sigma_n exists: sup_x eta(x, 0) < k_n for n large, and t -> sup_x eta(x, t) is continuous on [0, t_n] since
|eta(x, t) - eta(x, s)| <= sqrt2 ||grad^2 (u(t) - u(s))||_infty (as above, applied to u(t) - u(s)), so the set of times where it is at most k_n is closed. The excess vanishes at sigma_n, so all of it is produced on (sigma_n, t_n] by the source restricted to
{eta > k_n}, and the radial source mass bound of 2.1 converts the production into int Z_n dt >= c l_n^3/G.

2.7b Decay of the adjoint (Theorem 6) and compression (Proposition 7). The adjoint conserves int Psi_n dx = l_n^3 m and satisfies
(1/2) d/dh ||Psi_n(t_n - h)||_2^2 = -||grad Psi_n||_2^2; the Nash inequality ||f||_2^{5/3} <= C ||f||_1^{2/3} ||grad f||_2 turns this into
||Psi_n(t_n - h)||_2^2 <= C l_n^3 (1 + h/l_n^2)^{-3/2}. The L^infinity bound follows by duality: the forward homogeneous eta operator
d_t + b.grad - Delta_5 preserves int g Psi_n, does not increase the L^1 norm (int Delta_5 g dx = -4 pi int g(0,z) dz), and dissipates the
L^2 norm (int g Delta_5 g dx = -||grad g||_2^2 - 2 pi int g(0,z)^2 dz), so it obeys the same Nash bound; splitting [t_n - h, t_n] at the
midpoint gives ||Psi_n(t_n - h)||_infty <= C m l_n^3 h^{-3/2}. Integration by parts in h gives the weighted energy
int w_n^alpha ||grad Psi_n||_2^2 dt <= C_alpha l_n^3 for alpha < 3/2, and the weighted Cauchy-Schwarz inequality gives the displayed inequality of Theorem 6(b). For the older-history assertion of Theorem 6(b) (0 <= h <= t_n), the energy identity gives
int_0^{t_n - h} ||grad Psi_n||_2^2 dt <= (1/2) ||Psi_n(t_n - h)||_2^2 <= C l_n^3 (1 + h/l_n^2)^{-3/2}, and Cauchy-Schwarz on [0, t_n - h] with nu_n^2 l_n^3 = 1/(D_n M_n) gives the stated bound.
The first two assertions of Theorem 6(d) repeat the proof of Theorem 5(c) with the decaying sup bound of Psi_n: by 2.1,
int_{eta > k_n} |d_z(q^2)| dx <= 8 pi G H(t) Z_n(t) with H(t) <= C_* D_n^2/M_n, and the integral of w_n^{-3/2} over ages at least h is
2 l_n^2 (1 + h/l_n^2)^{-1/2}, while nu_n (D_n^2/M_n) l_n^2 = 1/l_n. The last assertion cannot be obtained by integrating the restricted
source by parts against Psi_n itself, since the indicator of {eta > k_n} would produce a level-set boundary term; a killed adjoint is used
instead, constructed by penalization so that no regularity of the level set is needed. Set E_n = {(x, t): sigma_n < t < t_n, eta(x, t) > k_n}
(an open set) and h_n = (eta - k_n)_+. For lambda > 0 let Psi^lambda solve -d_t Psi^lambda = b.grad Psi^lambda + L Psi^lambda - lambda 1_{E_n^c} Psi^lambda
on [sigma_n, t_n] (E_n^c the complement of E_n in R^3 x (sigma_n, t_n)) with the terminal datum phi((x - a_n)/l_n) and zero axis trace; the killing
term is a bounded nonnegative potential, so Psi^lambda = r^2 chi^lambda, with chi^lambda solving the equation of 2.7 with the added potential, exists in
C([sigma_n, t_n]; L^2) intersect L^2((sigma_n, t_n); H^1) and vanishes on the axis like Psi_n, and the weak maximum principle gives
0 <= Psi^lambda <= Psi_n and Psi^lambda nonincreasing in lambda. Let Psi^E be the almost-everywhere monotone limit along integers lambda -> infinity; domination by Psi_n gives
convergence in L^2((sigma_n, t_n) x R^3), and with the gradient bound below Psi^E lies in L^2((sigma_n, t_n); H^1), the weighted gradients converging weakly. By Theorem 6(a),
||Psi^lambda(t)||_2^2 <= ||Psi_n(t)||_2^2 <= C l_n^3 w_n(t)^{-3/2}; the energy identity
(1/2) d/dh ||Psi^lambda||_2^2 = -||grad Psi^lambda||_2^2 - lambda int_{E_n^c(t)} (Psi^lambda)^2 dx, multiplied by w_n^alpha and integrated by parts in h as
above, gives int_{sigma_n}^{t_n} w_n^alpha (||grad Psi^lambda||_2^2 + lambda int_{E_n^c(t)} (Psi^lambda)^2 dx) dt <= C_alpha l_n^3 for 0 <= alpha < 3/2, uniformly in
lambda. Hence Psi^E = 0 almost everywhere on E_n^c, int_{sigma_n}^{t_n} w_n^alpha ||grad Psi^E||_2^2 dt <= C_alpha l_n^3 (weak lower semicontinuity),
and, since at almost every time the spatial gradient of a Sobolev function vanishes almost everywhere on its zero set (then Fubini), grad Psi^E = 0 almost everywhere on E_n^c. Next take
the truncations f_e of 2.7a with a smooth nondecreasing step theta equal to 0 on (-infinity, 0] and to 1 on [1, infinity), centred at k_n, so that H_e = f_e(eta)
vanishes where eta <= k_n (in particular at sigma_n, where sup eta <= k_n, and wherever the killing acts) and
(d_t + b.grad - Delta_5) H_e = f_e'(eta) d_z(q^2) - f_e''(eta) |grad eta|^2 <= f_e'(eta) d_z(q^2). Pairing with Psi^lambda >= 0 as in 2.7 gives
int H_e(t_n) phi((x - a_n)/l_n) dx <= int_{sigma_n}^{t_n} int f_e'(eta) d_z(q^2) Psi^lambda dx dt. Let e -> 0 (f_e' -> 1_{eta > k_n}) and then
lambda -> infinity, by dominated convergence with the integrable majorant |d_z(q^2)| Psi_n; with the two almost-everywhere statements above and
an integration by parts in z at almost every time,
int h_n(t_n) phi((x - a_n)/l_n) dx <= int int 1_{E_n} d_z(q^2) Psi^E dx dt = - int int q^2 d_z Psi^E dx dt = - int int_{E_n} q^2 d_z Psi^E dx dt.
Only this inequality is needed. For large n the terminal packet lies inside the terminal super level set, since eta_n(., 0) -> eta_U(., 0) >= 2 kappa
uniformly on B, so the normalized terminal excess nu_n int h_n(t_n) phi((x - a_n)/l_n) dx = int (eta_n(., 0) - kappa)_+ phi tends to
int (eta_U(., 0) - kappa) phi >= kappa m, and the weighted Cauchy-Schwarz inequality with nu_n^2 l_n^3 = 1/(D_n M_n) gives (kappa m/2)^2 <= C_alpha (D_n M_n)^{-1}
int int_{E_n} q^4 w_n^{-alpha} for large n, which is the last assertion, including its restriction to the super level set. For Proposition 7, (d_t + b.grad) q^2 =
Delta_5 q^2 - 2|grad q|^2 - 4 (u^r/r) q^2, the axis term vanishes against Psi_n, and the source pairing is - nu_n int q^2 d_z Psi_n = 2 nu_n int q (d_z q) Psi_n (integration by parts in z; the square below removes the sign).
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
|q_n| <= G nu / R^2 (from |Gamma| <= G), int 1/W dZ <= e^2 pi S/2 and int_{R > R_0} q_n^4 dy <= (pi/3)(G nu)^4 R_0^{-6} per unit length give (a)
with S = K/nu, and its extension with S = Lambda/nu (for n so large that nu_n <= L, Lambda >= nu_n L gives S >= max(L, nu_n), so the
weighted inequality applies and cosh(L/S) <= cosh 1; pi e (cosh(1)/6)^{1/2} = 4.3307... < 4.4). The growing weight is justified by first
using W_N = e^{-2s/S} min(2 cosh((Z - Z_0)/S), N), whose distributional second Z-derivative is at most W_N/S^2 and whose first is at most
W_N/S in absolute value, and letting N -> infinity by monotone convergence. The dissipation form of (a): for axisymmetric fields the swirl part of grad u in the cylindrical frame contains the
entry -u^theta/r, so q^2 <= |grad u|^2 pointwise and int_I int q^2 dx dt <= e_I; with |q| <= G/r^2 on {r > R_0 l_n} and Theorem 3(a),
nu_n int_I int_{r > R_0 l_n} q^2 |d_z Psi_n| <= nu_n G (R_0 l_n)^{-2} e_I^{1/2} (l_n^3/2)^{1/2} ||phi||_2, and nu_n l_n^{-1/2} = (D_n^3/M_n^5)^{1/2}. For (b), |q_n| <= 2 C_*^{2/3} (G nu)^{1/3} (rescaling, with (A), the physical bound |q| <= 2 (G H^2)^{1/3}, which follows from |u^theta(r,z) - a r| <= H r^2/2, a = d_r u^theta(0,z), and
|Gamma(|a|/H, z)| <= G, which give |a| <= (2 G H^2)^{1/3}, |q| <= (2^{1/3} + 1/2)(G H^2)^{1/3} for r <= (G/H)^{1/3} and |q| <= G/r^2 beyond) and |q_n| <= G nu/R^2
give int q_n^2 2 pi R dR <= 4 pi C_*^{2/3} (G nu)^{4/3} after optimizing the split radius. (c) is comparison with the supersolution
G (1 - e^{-k(t) r^2}) of the Gamma equation, written in s = r^2 as d_t + 2 (u^r/r) s d_s + u^z d_z - 4 s d_ss - d_zz: its residual is
2 G k r^2 e^{-k r^2} (A + u^r/r) >= 0 when k' = 2 A k - 4 k^2, and m = 1/k solves m' = -2 A m + 4, m(s) = 0; the stationary
supersolution 2 G (1 - e^{-k_0 r^2}), k_0 = max(A_*/2, (log 2) ||q(s)||_infty / G), gives the second bound. For the Case 2 consequence, Theorem 3(f) (with s_n as in Proposition 7) gives
sup_{I_n} ||q||_infty^2 >= c D_n M_n/e_n, and the additional condition on ||q(s_n)||_infty excludes the second alternative of the bound just proved. (d) is comparison with ||psi(-s_0)||_infty (1 - e^{-k R^2}), k = 1/(2 nu (1 - e^{-2h})), whose
residual 2 k (1 - U^R/R) R^2 e^{-k R^2} is nonnegative because |U^R/R| <= |grad U| <= 1, combined with Theorem 6(a).

2.7d Corollary (iii). With h = t_n - t, Y_n(h) = l_n L + int_{t_n - h}^{t_n} M(s) ds and g_h the one-dimensional heat kernel, the function
V(z, h) = int_{-Y_n(h)}^{Y_n(h)} g_h(z - z_n - y) dy satisfies V_h - V_zz = M(t_n - h) [g_h(z - z_n - Y_n(h)) + g_h(z - z_n + Y_n(h))] >= M(t_n - h) |V_z| >= u^z V_z.
Since V does not depend on r, P V is a supersolution of the backward adjoint equation d_h Psi = b.grad Psi + L Psi; it dominates Psi_n at h = 0
(the terminal datum is at most P on the slab |z - z_n| < l_n L; approximate the slab indicator by smooth barriers), and Psi_n - P V <= 0 on the
axis and at infinity. The maximum principle gives Psi_n <= P V, hence int sup_r Psi_n(r, z, t) dz <= P int V dz = 2 P Y_n(t_n - t). With the radial
source mass 2 pi int_0^infty |d_z(q^2)| r dr <= 8 pi G ||grad^2 u(t)||_infty of 2.1 and Theorem 3(b),
m_phi - o(1) <= nu_n int_0^{t_n} int |d_z(q^2)| Psi_n dx dt <= 16 pi P G nu_n int_0^{t_n} H(t) Y_n(t_n - t) dt.

2.8 Conservation structure (Proposition 4). eta solves d_t eta + b.grad eta = Delta_5 eta + d_z(q^2) and Gamma solves
d_t Gamma + b.grad Gamma = L Gamma. In d/dt int eta f(Gamma) the transport terms combine into a divergence, the source is
r^{-4} d_z K(Gamma) and integrates to zero in z for each r, and the diffusion terms follow from the integration by parts formula
of 2.7 with g = f(Gamma), Gamma(0,z) = 0; with cutoffs justified by (DEC) this gives the identity integrated over every compact time interval, hence the absolute continuity and the identity for almost every t (the axis term is only locally integrable in time). The convex approximations sqrt(s^2 + e^2) - e of |s| give (c) (the axis term has the
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
and p = infinity follows from the maximum principle); eta_0 is in L^2 and L^infinity because |eta| <= |grad(omega^theta e_theta)| <= |grad omega| pointwise and u_0 is in H^infinity (here |grad(omega^theta e_theta)|^2 = |grad omega^theta|^2 + (omega^theta/r)^2, and for axisymmetric fields |grad omega|^2 = |grad(omega^theta e_theta)|^2 + |grad(omega^r e_r + omega^z e_z)|^2; the first inequality need not hold with |d_r omega^theta| in place of the full vector gradient); the kernel bound
|u^r/r|(x) <= (3/(4 pi)) int_{R^3} |x - y|^{-2} |eta(y)| dy (related estimates appear in Shirota and Yanagisawa, Proc. Japan Acad. Ser. A 70 (1994); this form
is proved below) and Lorentz duality give ||u^r/r||_infty <= C ||eta||_{L^{3,1}}, and with ||f||_{L^{3,1}} <= 9 ||f||_2^{2/3} ||f||_infty^{1/3} this bounds
a_r once the velocities are identified. Identification: by (Delta_3 - 1/r^2)(r g) = r Delta_5 g and b.grad (r g) = r b.grad g + u^r g, and since b has no theta component, w_r = r eta_r e_theta solves the Cartesian equation d_t w_r + b.grad w_r = Delta w_r + a w_r with w_r(0) = omega_0^theta e_theta in L^2 (this linear equation is solved first in L^2, and its quotient by r e_theta is the bounded five-dimensional solution eta_r by uniqueness). On every [0, T] with T < T_* the coefficient a is bounded and (1/2) d/dt ||w_r||_2^2 + ||grad w_r||_2^2 = int a |w_r|^2 dx <= ||a(t)||_infty ||w_r||_2^2, so w_r(t) and w_s(t) = omega^theta e_theta - w_r(t) are divergence-free and in L^2, and the whole-space Biot-Savart law gives divergence-free velocities v_r, v_s in L^6 with curl v_r = w_r, curl v_s = w_s. Then v_r + v_s - b is divergence-free and curl-free, hence harmonic, and lies in L^6 + L^2, so it vanishes; this is a = a_r + a_s. Proof of the kernel bound, for smooth rapidly decaying axisymmetric eta: since
Delta_3 (x_1 g(r, z)) = x_1 Delta_5 g, the canonical vector potential of r eta e_theta is r psi e_theta, where psi = N_5 * eta is the Newtonian
potential of eta regarded as a function on R^5 = R^4 x R, so u^r/r = - d_z psi and |u^r/r|(x) <= (3/(8 pi^2)) int_{R^5} |X - Y|^{-4} |eta(Y)| dY.
With a = r^2 + rho^2 + (z - y_3)^2, b = 2 r rho and s = (a^2 - b^2)^{1/2}, the average of |X - Y|^{-4} over the 3-sphere {|y'| = rho} of R^4 is
2/((a + s) s) and the average of |x - y|^{-2} over the circle of radius rho is 1/s; since dY = 2 pi^2 rho^3 d rho dy_3 and dy = 2 pi rho d rho dy_3,
the 5D integrand is at most 2 pi rho^2/(a + s) <= 2 pi times the 3D one, and 2 pi (3/(8 pi^2)) = 3/(4 pi). The Biot-Savart recovery is essential: u^r = c r, u^z = - 2 c z has eta = 0 and u^r/r = c. For eta_r(t) itself (smooth, and in L^2 and L^infty of dx), apply the bound to eta^k = chi(x/k) eta_r, chi a smooth radial cutoff equal to 1 on the unit ball: by the interpolation bound above, ||eta_r - eta^k||_{L^{3,1}} <= 9 ||eta_r 1_{|x| > k}||_2^{2/3} ||eta_r||_infty^{1/3} -> 0, so the values u^r/r of the velocities recovered from r eta^k e_theta converge uniformly, while chi(x/k) w_r -> w_r in L^2 makes these velocities converge to v_r in L^6; the uniform limit is therefore a_r, and ||a_r(t)||_infty <= C ||eta_r(t)||_{L^{3,1}} <= C_0. Finally Y = Sigma + int_0^t ||d_z(q^2)||_{L^1}
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

F2. For C_* > 1/2, the properties of the Euler limit listed in Theorem 1 imply no Liouville rigidity (the thin vortex rings of the third part below give the same conclusion for C_* > Q_core, a constant defined there and below 1/2 by the computer-assisted enclosures of (iv) there, whose programs are not reproduced here): steady swirl-free pipe flows U = f(R) e_Z with f nonzero, with a smooth even extension across R = 0 and rapidly decaying together with all its derivatives are bounded, smooth, nonconstant, axisymmetric, swirl-free Euler solutions with |grad U| maximal at tau = 0 and ||omega(-A)||_infty constant in A (the flows are steady; their L^p vorticity norms with p < infinity are infinite), and, normalized so that |U| <= 1 and max |grad U| = 1, suitable ones satisfy |grad^2 U| <= C_* exactly when C_* > 1/2. For example, for 0 < c <= 1, f(R) = c e^{-R^2/s^2} has this normalization when s = c (2/e)^{1/2}; for c = 1 the Hessian has Frobenius norm at most 2^{1/2} e, attained on the axis, so this example satisfies |grad^2 U| <= C_* when C_* >= 2^{1/2} e; the profile f(R) = exp(-(R/m)^4), m = 4 (3/4)^{3/4} e^{-3/4}, approximately 1.5228, has the same normalization and the supremum of its Hessian norm is approximately 1.683914 (1.6839 to four decimals, a rounding, not an upper bound). The threshold: over such f, compactly supported or not, with |f| <= 1 and max |f'| = 1 the infimum of the Hessian bounds is 1/2, and it is not attained, not even by profiles of class C^{1,1} (with the Hessian bound understood almost everywhere). Indeed |grad^2 U|^2 = f''^2 + (f'/R)^2, and Landau's inequality (sup |g'|)^2 <= 2 sup |g| sup |g''| on the line, applied to the even extension of f, gives sup |f''| >= 1/2; equality forces, by the equality case of its Taylor argument, f' = +-(1 - |s|/2) at R_* + s for |s| < 2, R_* a point where |f'| = 1, so |f''| = 1/2 almost everywhere there while f' does not vanish, and |grad^2 U| > 1/2 on a set of positive measure with R > 0. Conversely, two parabolic arcs of curvatures -1/2 and 1/2 joining the values 1 and -1 at distance R_0 from the axis, preceded by the constant 1, followed by a slow return to 0, mollified after even extension by a nonnegative even kernel of integral 1 and width epsilon(R_0) -> 0, and
rescaled radially to max |f'| = 1, give Frobenius Hessian bounds tending to 1/2 as R_0 -> infinity, the azimuthal term |f'/R| being at most about 1/R_0 where f' is not 0. These statements were checked by hand and the two numerical values by direct evaluation. Hence, for C_* > 1/2, these properties alone do not exclude Case 2; an exclusion in this range needs further information, which in the arguments here comes from the
prelimit Navier-Stokes dynamics. The WINDOW argument of Section 2.6 controls the prelimit only for A <~ (G nu_n)^{-1/2}, where its source
estimate, of order G nu_n A^2 including axial spreading, is small; beyond that range the arguments here give the localization statements of Theorems 3, 5, 6 and 8 and the necessary compression bounds of Theorem 9 and R2.16, none of which excludes Case 2.

For C_* <= 1/2 no pipe flow is admissible. Three facts bear on this range. First, for every solution, (A) at a late time t with D(t) > 0 forces C_* >= c_div = 0.2700..., a constant defined below that exceeds c_S := 10^{1/2}/12 = 0.2635...; so for C_* < c_div the inequality of (A) fails at every late time with D(t) > 0, for every solution, and in particular the nonconstant Case 2 alternative is impossible. This fact and its companions occupy this paragraph and the six that follow: a sharp Landau inequality in Frobenius norms, (LF) below, which gives c_S and, in the plane, the constant 8/7^{1/2}; its refinement for divergence-free fields on R^3, which gives c_div; an on-axis bound, which forces alpha_* > 0 when C_* < 2^{1/2}/3; a swirl-free floor c_ax = 7^{1/2}/8 = 0.3307... for the limit of Theorem 1, proved in two steps; and kinematic rings with quotients tending to 7^{1/2}/8, which show that this floor is sharp for these kinematic hypotheses.

Let F be a bounded map of class C^{1,1} from R^n to R^m (n, m >= 1) with A = sup |F| and C = ess sup |grad^2 F| finite, in Frobenius norms (grad F has the entries d_i F_alpha and grad^2 F the entries d_i d_j F_alpha). Then the inequality (LF), |grad F(x)|^2 <= 4 n (3 n + 1)^{-1/2} A C at every point x, holds, and the constant is attained when m >= n. For n = 1 this is Landau's inequality; the constant is 8/7^{1/2} = 3.0237... for n = 2 and 12/10^{1/2} = 3.7947... for n = 3. Proof. Mollification with a nonnegative normalized smooth kernel does not increase A and C (the norms are convex), converges in C^1 locally uniformly and gives a smooth map whose derivatives of every order are bounded, so we may assume F of this kind, and by translation x = 0. If C = 0, F is affine and bounded, hence constant, so we may assume C > 0 and grad F(0) not 0. Let E denote the average over the unit sphere S^{n-1} with its normalized surface measure (for n = 1, the average over the two points 1 and -1), and for r > 0 let M(r) be the m x n matrix (n/r) E[F(r omega) omega^T]. (a) For an m x n matrix T of unit Frobenius norm, <T, M(r)> = (n/r) E[F(r omega) . T omega] <= (n A/r) (E |T omega|^2)^{1/2} = n^{1/2} A/r, since E[omega omega^T] = I/n; so |M(r)| <= n^{1/2} A/r. (b) The function r -> E[F(r omega) omega^T] is smooth and odd on the real line (replace omega by -omega), so M extends to a smooth even function of r, and Taylor's formula gives M(0) = grad F(0). (c) The map F_1(x) = M(|x|) x is smooth, and on each sphere |x| = r it is the component of F in the spherical harmonics of degree 1, since n omega . eta is the reproducing kernel of these harmonics on S^{n-1} (for n = 1, F_1 is the odd part of F). The Hessians of the components of F in different eigenspaces of the spherical Laplacian are orthogonal in L^2 of each sphere: for f(r) Y(omega) with Delta_S Y = -lambda Y the Hessian has, in an orthonormal frame, the radial entry f'' Y, the mixed entries (f/r)' grad_S Y and the tangential block (f/r^2) grad_S^2 Y + (f'/r) Y g_S, and for L^2-orthogonal eigenfunctions Y, Y' the sphere integrals of Y Y', grad_S Y . grad_S Y', Y Delta_S Y' and grad_S^2 Y : grad_S^2 Y' vanish, the last by the Bochner identity int grad_S^2 Y : grad_S^2 Y' = int Delta_S Y Delta_S Y' - (n - 2) int grad_S Y . grad_S Y' (the unit sphere has Ricci curvature (n - 2) g_S). For n >= 2, smoothness on compact annuli implies that the spherical harmonic expansion of F and its derivatives through order two converge in L^2 on each sphere, so this orthogonality gives E |grad^2 F_1(r omega)|^2 <= E |grad^2 F(r omega)|^2. For n = 1, F_1(x) = (F(x) - F(-x))/2 and E |F_1''(r omega)|^2 = |F''(r) - F''(-r)|^2/4 <= (|F''(r)|^2 + |F''(-r)|^2)/2. Thus E |grad^2 F_1(r omega)|^2 <= E |grad^2 F(r omega)|^2 <= C^2 for every n >= 1 and r > 0. (d) A direct computation from d_j d_k (M_{alpha i}(r) x_i) gives E |grad^2 F_1(r omega)|^2 = (|2 M' + r M''|^2 + 3 (n - 1) |M'|^2)/n. (e) With y = |M'|^2, the bound 4 r <M', M''> <= |2 M' + r M''|^2 - 4 |M'|^2 and (c), (d) give 2 r y' + (3 n + 1) y <= n C^2; since (r^{(3n+1)/2} y)' = r^{(3n-1)/2} (2 r y' + (3 n + 1) y)/2, integration from 0 gives |M'(r)|^2 <= n C^2/(3 n + 1) for r > 0. (f) Hence |M(r)| >= |grad F(0)| - beta r with beta = (n/(3 n + 1))^{1/2} C, and by (a) n^{1/2} A >= r (|grad F(0)| - beta r) for every r > 0; the choice r = |grad F(0)|/(2 beta) gives |grad F(0)|^2 <= 4 n^{1/2} beta A = 4 n (3 n + 1)^{-1/2} A C. For the sharpness, let m >= n, regard R^n as a subspace of R^m, and given a > 0 and C > 0 let gamma = (3 n + 1)^{-1/2} C, r_* = a/(2 gamma) and W(x) = g(|x|) x with g(r) = a - gamma r for r <= r_* and g(r) = a^2/(4 gamma r) for r >= r_*. Both branches give g(r_*) = a/2 and g'(r_*) = -gamma; the gradient of W extends continuously to the origin, with grad W(0) = a I (I the inclusion of R^n in R^m, as in M = g I below), and agrees from both sides of the sphere |x| = r_*, and the Hessian computed below is bounded on the regions 0 < |x| < r_* and |x| > r_*, so grad W is globally Lipschitz and W is of class C^{1,1}; sup |W| = r_* g(r_*) = a^2/(4 gamma), |grad W(0)|^2 = n a^2, and since |grad^2 W|^2 is radial, (d) with M = g I gives |grad^2 W|^2 = (3 n + 1) gamma^2 = C^2 for 0 < r < r_* and 3 (n - 1) a^4/(16 gamma^2 r^4) <= 3 (n - 1) gamma^2 < C^2 for r > r_*; so (LF) holds with equality at x = 0. For n = 2, composing W with the rotation by a right angle gives the circular vortex v(rho) e_phi with v = a rho - gamma rho^2 for rho <= r_* and v = a^2/(4 gamma) beyond, which is divergence-free; with a = 1 and C = 7^{1/2}/2 it is the profile v = rho - rho^2/2 (rho <= 1), v = 1/2 (rho >= 1) of the second part below. For n = 3 the field W is not divergence-free (div W = 3 g + r g' is not 0), and the next paragraph gives a smaller constant for divergence-free fields on R^3. At a late time t with D(t) > 0 choose, for 0 < epsilon < 1, s <= t and x with |grad u(x, s)| >= (1 - epsilon) D(t); (LF) with n = m = 3 for u(s), with sup |u(s)| <= M(t) and sup |grad^2 u(s)| <= H(t), gives (1 - epsilon)^2 D(t)^2 <= (12/10^{1/2}) M(t) H(t) <= (12/10^{1/2}) C_* D(t)^2, and C_* >= c_S as epsilon -> 0. (Landau's inequality along the line of the largest singular pair of grad u gives only C_* >= 1/6. Earlier versions of this report used ball-average and singular-value forms of an averaging argument, with the weaker floors 2 30^{1/2}/45 = 0.2434..., 0.2545... and 0.2610...; (LF) supersedes them.)

For divergence-free fields on R^3 the constant 12/10^{1/2} of (LF) can be lowered. Let F be a bounded divergence-free vector field of class C^{1,1} on R^3 with A = sup |F| and C = ess sup |grad^2 F| finite. Then |grad F(x)|^2 <= K_div A C at every point x, where K_div := 4 ((7 p_div + 50 q_div)^3/(6125 q_div))^{1/2} = 3.7025..., with theta_div = arcsin (2/3)^{1/2}, p_div = (7^{1/2}/112)(11 + 19 theta_div/2^{1/2}) = 0.5630... and q_div = (7^{1/2}/24)(5 theta_div/2^{1/2} - 3) = 0.0416...; so K_div < 12/10^{1/2} = 3.7947..., and c_div := 1/K_div = 0.2700... exceeds c_S. Proof. Mollification preserves the divergence condition, so as in the proof of (LF) we may assume that F is smooth with bounded derivatives of every order, that x = 0, that C > 0 and that grad F(0) is not 0; we use E, M(r) and F_1 as in that proof, with n = m = 3. Let B = grad F(0)/|grad F(0)|, so that |B| = 1 and tr B = div F(0) = 0, and put mu_B(r) := <B, M(r)> = (3/r) E[F(r omega) . B omega] and w_B := E |B omega|. For a 3 x 3 matrix N and omega in S^2 let K_N(omega) be the tensor with entries (K_N)_{alpha i j} = N_{alpha i} omega_j + N_{alpha j} omega_i + delta_{ij} (N omega)_alpha - omega_i omega_j (N omega)_alpha, the Hessian at omega of the map x -> |x| N x. (a') By (b) of that proof, mu_B is smooth and even with mu_B(0) = |grad F(0)|, and mu_B(r) <= (3/r) A E |B omega| = 3 A w_B/r. (b') The components of x -> |x| B x are, on each sphere |x| = r, r^2 times spherical harmonics of degree 1, and its Hessian at r omega is K_B(omega); the computation in step (c) of that proof applies equally to two fields f(r) Y and f_2(r) Y' with different radial factors, so with the convergence stated there, E[grad^2 F(r omega) : K_B(omega)] = E[grad^2 F_1(r omega) : K_B(omega)]. Differentiating F_1(x) = M(|x|) x twice gives grad^2 F_1(r omega) = K_{M'(r)}(omega) + T_2(r, omega), where T_2 has the entries r (M''(r) omega)_alpha omega_i omega_j; a direct computation gives K_N(omega) : K_B(omega) = 2 <N, B> + 4 (N omega) . (B omega) and omega_i omega_j (K_B)_{alpha i j} = 2 (B omega)_alpha, and with E[omega omega^T] = I/3 this yields E[grad^2 F(r omega) : K_B(omega)] = (2 r mu_B'' + 10 mu_B')/3. (c') For tensors T with entries T_{alpha i j} symmetric in i and j let Tr T be the vector with entries sum_alpha T_{alpha alpha j}; its adjoint Tr^* satisfies Tr Tr^* = 2 I, so the orthogonal projection Pi_0 onto the kernel of Tr satisfies |Pi_0 T|^2 = |T|^2 - |Tr T|^2/2. Since Tr grad^2 F = grad div F = 0, grad^2 F : K_B = grad^2 F : Pi_0 K_B >= -C |Pi_0 K_B| pointwise, so 2 r mu_B'' + 10 mu_B' >= -3 C k_B with k_B := E |Pi_0 K_B(omega)|. As (r^5 mu_B')' = r^4 (2 r mu_B'' + 10 mu_B')/2 and mu_B'(0) = 0, integration from 0 gives mu_B'(r) >= -(3/10) C k_B, and with (a'), |grad F(0)| - (3/10) C k_B r <= 3 A w_B/r for every r > 0 (so k_B > 0); the choice r = 5 |grad F(0)|/(3 C k_B) gives |grad F(0)|^2 <= (18/5) A C w_B k_B. (Without the divergence condition the same argument, with the bound -C |K_B| in place of -C |Pi_0 K_B| and with w_B <= 3^{-1/2} and E |K_B| <= (E |K_B|^2)^{1/2} = (10/3)^{1/2}, returns (LF) for n = 3.) (d') Let B_s = (B + B^T)/2 and s = |B_s|^2, so 0 <= s <= 1. Then |K_B|^2 = 2 + 4 |B omega|^2, so E |K_B|^2 = 10/3; since tr B = 0, Tr K_B = 2 B_s omega - (omega . B_s omega) omega, so |Tr K_B|^2 = 4 |B_s omega|^2 - 3 (omega . B_s omega)^2, and the sphere moments E |B_s omega|^2 = s/3 and E (omega . B_s omega)^2 = 2s/15 (tr B_s = 0) give E |Tr K_B|^2 = 14 s/15. Hence k_B^2 <= E |Pi_0 K_B|^2 = 10/3 - 7s/15 = (50 - 7s)/15. (e') The skew part of B has a unit null vector e, so B e = B_s e, and the smallest eigenvalue lambda_1 of B^T B satisfies lambda_1 <= |B_s e|^2 <= 2s/3 (each eigenvalue mu_1 of the traceless symmetric B_s, with mu_2 and mu_3 the other two, satisfies mu_1^2 = (mu_2 + mu_3)^2 <= 2 (s - mu_1^2)). In a frame diagonalizing B^T B, with eigenvalues lambda_1, lambda_2, lambda_3 (sum 1), w_B = E (lambda_1 omega_1^2 + lambda_2 omega_2^2 + lambda_3 omega_3^2)^{1/2} is, at fixed lambda_1, a concave function of (lambda_2, lambda_3) on the segment lambda_2 + lambda_3 = 1 - lambda_1, symmetric under their exchange, hence at most its value at lambda_2 = lambda_3 = (1 - lambda_1)/2; since omega_1 is uniformly distributed on [-1, 1], this value is f_div(lambda_1) with f_div(y) := int_0^1 ((1 - y)/2 + (3y - 1) z^2/2)^{1/2} dz. The function f_div is concave on [0, 1], and elementary antiderivatives give f_div(1/7) - f_div'(1/7)/7 = p_div and (2/3) f_div'(1/7) = q_div > 0; so w_B <= f_div(lambda_1) <= f_div(1/7) + f_div'(1/7)(lambda_1 - 1/7) <= p_div + q_div s. (f') With v = p_div + q_div s, (c') to (e') give |grad F(0)|^4 <= (18/5)^2 A^2 C^2 v^2 (50 - 7s)/15 = (324/(375 q_div)) A^2 C^2 v^2 (7 p_div + 50 q_div - 7v), and the maximum of v^2 (7 p_div + 50 q_div - 7v) over v > 0, attained at v = 2 (7 p_div + 50 q_div)/21, is 4 (7 p_div + 50 q_div)^3/1323; this gives |grad F(0)|^2 <= K_div A C. At a late time t with D(t) > 0 the argument given above for c_S, with this bound in place of (LF), gives C_* >= c_div for every solution: when C_* < c_div the inequality of (A) fails at every late time with D(t) > 0. The constant K_div is not claimed sharp, and the sharp constant for divergence-free fields on R^3 is not determined here. (The identities of (b') and (d') were checked by hand, those of (d') also by exact sphere quadrature for random trace-free B and that of (b') numerically on a random polynomial field; the closed forms of p_div and q_div and the value of K_div were checked by 40-digit computation; K_div < 3.703.)

On the axis the symmetry gives more. Let V be a smooth axisymmetric divergence-free field on R^3 with finite velocity and Hessian suprema, in coordinates in which the axis is the third coordinate axis, and put g(z) = V_3(0, 0, z). At each axis point grad V commutes with the rotations about the axis and its trace vanishes, so its diagonal entries are -g'/2, -g'/2 and g'; if V is also swirl-free, grad V also commutes with the reflections in planes containing the axis, so grad V = diag(-g'/2, -g'/2, g') and |grad V|^2 = (3/2) g'^2 there. Differentiating the diagonal entries along the axis gives d_1 d_3 V_1 = d_3 d_1 V_1 = d_2 d_3 V_2 = d_3 d_2 V_2 = -g''/2 and d_3 d_3 V_3 = g'', so |grad^2 V|^2 >= 2 g''^2 on the axis, with or without swirl, and Landau's inequality for g gives g'^2 <= 2 sup |V| sup |g''| <= 2^{1/2} sup |V| sup |grad^2 V| at every axis point. For all sufficiently large n apply this to V = U_n(., 0), which is smooth with |U_n| <= 1 and |grad^2 U_n| <= C_* on all of space (Theorem 1 (b)), at the axis point 0 of the rescaled coordinates: (d_3 (U_n)_3(0, 0))^2 <= 2^{1/2} C_*. If alpha_* = 0, then y_* = 0, and the local uniform convergence of grad U_n and the absence of swirl in U give 1 = |grad U(0, 0)|^2 = (3/2) (d_3 U_3(0, 0))^2 = (3/2) lim_n (d_3 (U_n)_3(0, 0))^2 <= (3/2^{1/2}) C_*, that is C_* >= 2^{1/2}/3 = 0.4714...; so for C_* < 2^{1/2}/3 every Case 2 record sequence has alpha_* > 0. More precisely, the same limit gives |grad U(0, 0)| <= (3 C_*/2^{1/2})^{1/2} whatever alpha_* is, and |grad U_n(y_n, 0) - grad U_n(0, 0)| <= C_* alpha_n gives in the limit 1 <= (3 C_*/2^{1/2})^{1/2} + C_* alpha_*, so alpha_* >= (1 - (3 C_*/2^{1/2})^{1/2})/C_* (on c_ax <= C_* <= 2^{1/2}/3 the right side decreases in C_*, from 0.4910... at C_* = c_ax = 0.3307..., the swirl-free floor proved below, to 0 at C_* = 2^{1/2}/3). Likewise, a field with the properties listed in Theorem 1, mollified with a nonnegative normalized smooth radial kernel (which preserves the symmetry, the divergence condition and the bounds |V| <= 1 and |grad^2 V| <= C_*, the latter for the almost everywhere defined Hessian), satisfies |grad V|^2 <= (3/2^{1/2}) C_* at every axis point in the limit of the mollification, so it does not attain |grad V| = 1 on the axis when C_* < 2^{1/2}/3 (the on-axis formulas were also checked symbolically on a test field; the bound is not claimed sharp).

Off the axis the absence of swirl raises the floor for the limit. Let V be a bounded divergence-free axisymmetric swirl-free field of class C^{1,1} with A = sup |V|, B = sup |grad V| and C = ess sup |grad^2 V| finite. Then A C >= B^2/K, where B_2 = 8/7^{1/2} is the planar constant of (LF), K = B_2 + t_0^2 = 3.1217... and t_0 = 0.3130... is the unique positive root of 144 t^4 - 112 2^{1/4} t^3 + (32 B_2 - 40) t^2 - 3 (B_2 - 4)^2 (the value at 0 is negative, and the derivative t (576 t^2 - 336 2^{1/4} t + 64 B_2 - 80) is positive for t > 0, its quadratic factor having negative discriminant). The next paragraph lowers K to B_2, which raises the floor from 1/K = 0.3203... to the sharp value c_ax = 1/B_2 = 7^{1/2}/8; the present paragraph is the first step. Mollification with a nonnegative normalized smooth radial kernel preserves the symmetry, the absence of swirl (the kernel is invariant under the reflections in planes containing the axis) and the divergence condition, does not increase A and C, and converges in C^1 locally uniformly, so we may assume V smooth. If C = 0, V is constant; otherwise A > 0, and since A C/B^2 does not change under V -> lambda V(mu x) (lambda, mu > 0), we may take A = C = 1 and must show |grad V(x)|^2 <= K at every point x. Four bounds are used. (Landau) If f is a C^2 function of one variable with |f| <= 1 and |f''| <= L, then f'(0)^2 <= 2 L (1 - |f(0)|): if L = 0, boundedness makes f constant, so assume L > 0, and replace f(s) by -f(s) or f(-s) as needed so that f(0), f'(0) >= 0, and evaluate 1 >= f(s) >= f(0) + f'(0) s - L s^2/2 at s = f'(0)/L. (L) For every unit vector e, (e . grad V(x) e)^2 <= 2^{1/2} A C, and this holds for every divergence-free V: rotate so that e = e_3; differentiating div V = 0 in x_3 gives d_1 d_3 V_1 + d_2 d_3 V_2 = - d_3 d_3 V_3, so |grad^2 V|^2 >= 2 (d_1 d_3 V_1)^2 + 2 (d_2 d_3 V_2)^2 + (d_3 d_3 V_3)^2 >= 2 (d_3 d_3 V_3)^2, and Landau's inequality for V_3 on the line through x in the direction e_3 gives the claim (at axis points this is the bound above). At x = (r, 0, z) with r > 0, grad V(x) has the rows (p, 0, q), (0, b, 0) and (h, 0, t), where p = d_R V^R, b = V^R/R, q = d_Z V^R, h = d_R V^Z and t = d_Z V^Z at x, and p + b + t = 0; replacing V by -V if necessary, b >= 0. (P) The planar field W(x_1, x_3) = (V_1, V_3)(x_1, 0, x_3) satisfies |W| <= 1 and |grad^2 W| <= 1 (its second derivatives are among those of V), and S := |grad W(x)|^2 = p^2 + q^2 + h^2 + t^2 = |grad V(x)|^2 - b^2, so S <= B_2 by (LF) with n = m = 2 (which does not use the divergence condition: W need not be divergence-free in the plane, its divergence at x being p + t = -b). The bound (Landau) for V_3 on the line through x in the direction (h, 0, t) of its gradient (if this vector is not 0) gives h^2 + t^2 <= 2, and for V_1 on the line through x in the direction (p, 0, q) (if it is not 0), along which its derivative at x is (p^2 + q^2)^{1/2} and its value at x is V^R = r b >= 0, it gives (p^2 + q^2)/2 + r b <= 1. (H) |grad^2 V(x)|^2 >= G^2/r^2 with G^2 = (11/3)(p - b)^2 + (8/3) q^2 + h^2, so G <= r. Indeed, |grad^2 V(x)|^2 = sum over F = V^R, V^Z of (F_RR^2 + 2 F_RZ^2 + F_ZZ^2) + (3 (p - b)^2 + 2 q^2 + h^2)/r^2 at x, and the R- and Z-derivatives of the divergence condition give d_RR V^R + d_RZ V^Z = - (p - b)/r and d_RZ V^R + d_ZZ V^Z = - q/r, so the minimum 2 X^2/3 of x_1^2 + 2 x_2^2 under x_1 + x_2 = X, applied to the pairs (d_RR V^R, d_RZ V^Z) and (d_ZZ V^Z, d_RZ V^R), adds at least (2/3)((p - b)^2 + q^2)/r^2. Using t = - p - b, G^2 = (8/3)(p^2 + q^2) + (h^2 + t^2) - (28/3) p b + (8/3) b^2 = (8/3) S - (5/3)(h^2 + t^2) - (28/3) p b + (8/3) b^2; (L) in the direction e_3 gives |t| <= 2^{1/4}, so p = - t - b <= 2^{1/4} - b, and with h^2 + t^2 <= 2 and b >= 0, G^2 >= (8/3) S - 10/3 + 12 b^2 - (28/3) 2^{1/4} b. Moreover p^2 + q^2 = S - (h^2 + t^2) >= S - 2, so b G <= b r <= 1 - (p^2 + q^2)/2 <= 2 - S/2, which is positive since S <= B_2 < 4. Hence f(S) := b^2 ((8/3) S - 10/3 + 12 b^2 - (28/3) 2^{1/4} b) - (2 - S/2)^2 <= 0 (immediately when the bracket is negative), and f increases in S for S < 4. Suppose |grad V(x)|^2 = S + b^2 > K. Then b^2 > K - B_2 = t_0^2 and K - b^2 < S, so f(K - b^2) < 0. But 12 f(K - b^2) = P_K(b) := 109 b^4 - 112 2^{1/4} b^3 + (38 K - 64) b^2 - 3 (K - 4)^2, P_K(t_0) = 0 is the defining equation of t_0, and P_K'(b) = b (436 b^2 - 336 2^{1/4} b + 76 K - 128) > 0 for b > 0 (negative discriminant, as K > 3), so P_K(b) > 0, a contradiction. So |grad V(x)|^2 <= K at every point off the axis, and by continuity on the axis, which gives A C >= B^2/K. (The bounds and the case analysis were checked by hand; the Hessian identity used in (H) by symbolic computation on generic polynomial fields; the identity for 12 f(K - b^2), the defining equation of t_0, the root t_0, the constants B_2 and K and the two discriminants by symbolic and 40-digit numerical computation.)

The constant K can be lowered to B_2 itself, and this value is sharp. That is, every field V as in the preceding paragraph satisfies A C >= c_ax B^2 with c_ax := 1/B_2 = 7^{1/2}/8 = 0.3307... (equivalently B^2 <= B_2 A C), and by the rings of the next paragraph c_ax is the infimum of A C/B^2 over the nonconstant fields of this class. The new ingredient is a form of (LF) for n = 2 that retains the value of the map. (LF_0) If F is a map of class C^{1,1} from R^2 to R^m with sup |F| <= 1 and ess sup |grad^2 F| <= 1, then |grad F(x)| <= B_2^{1/2} (1 - |F(x)|^2/14) at every point x. Proof. As in the proof of (LF) we may assume that F is smooth with bounded derivatives of every order and that x = 0, and we use E (the average over the unit circle), M(r) and F_1 of that proof with n = 2; put a(r) = E[F(r omega)], the component of degree 0 on the circle of radius r. (a'') The components of F(r omega) of different degrees are orthogonal on the circle, and F_1(r omega) = r M(r) omega with E[omega omega^T] = I/2, so |a(r)|^2 + (r^2/2) |M(r)|^2 <= E |F(r omega)|^2 <= 1. (b'') By the orthogonality of step (c) of that proof, applied to the components of degrees 0 and 1, E |grad^2 F(r omega)|^2 >= e(r) + E |grad^2 F_1(r omega)|^2, where e(r) := |a''(r)|^2 + |a'(r)|^2/r^2 is the squared Hessian of x -> a(|x|) at |x| = r; with (d) for n = 2 this gives e + (|2 M' + r M''|^2 + 3 |M'|^2)/2 <= 1. (c'') With y = |M'|^2, |2 M' + r M''|^2 >= 4 y + 2 r y', so 2 r y' + 7 y <= 2 (1 - e); since (r^{7/2} y)' = r^{5/2} (2 r y' + 7 y)/2 and y is bounded near 0, y(r) <= kappa^2 - v(r) with kappa^2 = 2/7 and v(r) = r^{-7/2} int_0^r s^{5/2} e(s) ds, which lies in [0, kappa^2]. As (kappa^2 - v)^{1/2} <= kappa - v/(2 kappa) there, Fubini's theorem and int_s^r sigma^{-7/2} d sigma = (2/5)(s^{-5/2} - r^{-5/2}) give int_0^r |M'| ds <= kappa r - (1/(5 kappa)) int_0^r (1 - (s/r)^{5/2}) e(s) ds. (d'') a is smooth and even, so a'(0) = 0 and a(r) - a(0) = int_0^r (r - s) a''(s) ds; the Cauchy-Schwarz inequality with the weight 1 - (s/r)^{5/2} >= 1 - s/r and int_0^r (r - s)^2/(1 - s/r) ds = r^3/2 gives, as a(0) = F(0), |a(r) - F(0)|^2 <= (r^3/2) int_0^r (1 - (s/r)^{5/2}) e(s) ds. (e'') By (b) of that proof M(0) = grad F(0), and by (a''), |M(r)| <= 2^{1/2} (1 - |a(r)|^2)^{1/2}/r <= 2^{1/2}/r - |a(r)|^2/(2^{1/2} r); with |M(0)| <= |M(r)| + int_0^r |M'| ds, (c'') and (d''), |grad F(0)| <= 2^{1/2}/r + kappa r - |a(r)|^2/(2^{1/2} r) - 2 |a(r) - F(0)|^2/(5 kappa r^3). At r = 7^{1/4} one has kappa r^2 = 2^{1/2}, so 2^{1/2}/r + kappa r = 2^{3/2} 7^{-1/4} = B_2^{1/2}, and the subtracted terms are (|a(r)|^2 + (2/5) |a(r) - F(0)|^2)/(2^{1/2} r); minimizing over the value of a(r) (the minimum is at a(r) = 2 F(0)/7) bounds them below by (2/7) |F(0)|^2/(2^{1/2} r) = B_2^{1/2} |F(0)|^2/14. This proves (LF_0); at F(0) = 0 it is (LF) for n = 2. Proof of B^2 <= B_2 A C. We keep the reductions of the preceding paragraph (V smooth, A = C = 1, a point x = (r, 0, z) with r > 0, the entries p, b, q, h, t with p + b + t = 0 and b >= 0, S, G and the bounds (Landau), (L), (P) and (H)), put Y = h^2 + t^2, and use three further bounds. (i) For unit vectors v and e, |v . grad^2 V(y)[e, e]| <= (1 - (v . e)^2/2)^{1/2} at every point y (for v = e this is the bound used in (L)). Indeed, for tensors T with entries T_{alpha i j} symmetric in i and j let Tr T be the vector with entries sum_alpha T_{alpha alpha j}; then Tr Tr^* = 2 I, so the orthogonal projection Pi_0 onto the kernel of Tr satisfies |Pi_0 T|^2 = |T|^2 - |Tr T|^2/2, which equals 1 - (v . e)^2/2 for the tensor T with entries v_alpha e_i e_j; since Tr grad^2 V = grad div V = 0, v . grad^2 V[e, e] = grad^2 V : T = grad^2 V : Pi_0 T, and the Cauchy-Schwarz inequality gives the claim. (ii) Y <= 250/117 - (6/13) t^2. If Y > 0, (Landau) for V_3 on the line through x in the direction e = (h, 0, t)/Y^{1/2}, with the bound (1 - t^2/(2Y))^{1/2} of (i) for the second derivative (v = e_3), gives Y <= 2 (1 - t^2/(2Y))^{1/2}, that is Y^3 <= 4 Y - 2 t^2, which also holds if Y = 0; and (Y - 5/3)^2 (Y + 10/3) = Y^3 - 25 Y/3 + 250/27 >= 0. (iii) (r b)^2 <= 14 (1 - (S/B_2)^{1/2}): the planar field W of (P) satisfies the hypotheses of (LF_0), |grad W(x)|^2 = S, and W(x) = (r b, V^Z(x)). Suppose now that |grad V(x)|^2 = S + b^2 > B_2; since S <= B_2 by (P), b > 0 and S > B_2 - b^2. Step 1: b < 1/2. The steps of the preceding paragraph that lead from S + b^2 > K to P_K(b) < 0 use only K < 4, and the identity 12 f(K - b^2) = P_K(b) holds for every value of K; with K = B_2 they give P_{B_2}(b) < 0, while P_{B_2} increases on b > 0 (the discriminant argument there uses only K > 3) and P_{B_2}(1/2) > 0.029. Step 2: G^2 > 237/100. The identity for G^2 of the preceding paragraph, with p = - t - b, reads G^2 = (8/3) S - (5/3) Y + (28/3) b t + 12 b^2, and with (ii) it gives G^2 >= (8/3) S - 1250/351 + (10/13) t^2 + (28/3) b t + 12 b^2. If b <= 1/5, then (10/13) t^2 + (28/3) b t + 12 b^2 = (10/13)(t + 91 b/15)^2 - (734/45) b^2 and S > B_2 - 1/25 give G^2 > (8/3)(B_2 - 1/25) - 1250/351 - 734/1125 > 3.7. If 1/5 < b < 1/2, the derivative (20/13) t + (28/3) b of (10/13) t^2 + (28/3) b t is positive for t >= - 2^{1/4} (as (20/13) 2^{1/4} < 28/15), and |t| <= 2^{1/4} by (L), so this expression is at least its value (10/13) 2^{1/2} - (28/3) 2^{1/4} b at t = - 2^{1/4}; with S > B_2 - b^2 this gives G^2 > (8/3) B_2 - 1250/351 + (10/13) 2^{1/2} + (28/3)(b^2 - 2^{1/4} b), and since b^2 - 2^{1/4} b decreases for b < 2^{-3/4}, G^2 > L_0 := (8/3) B_2 - 1250/351 + (10/13) 2^{1/2} + 7/3 - (14/3) 2^{1/4} = 2.3735... > 237/100. Step 3: contradiction. By (H), b G <= r b, so (iii) gives b^2 G^2 <= 14 (1 - (S/B_2)^{1/2}) = 14 (B_2 - S)/(B_2 + (B_2 S)^{1/2}) < 14 b^2/(B_2 + (B_2 S)^{1/2}), and S > B_2 - b^2 > B_2 - 1/4 gives G^2 < 14/(B_2 + (B_2 (B_2 - 1/4))^{1/2}) = 2.3649... < 237/100, against Step 2. So |grad V(x)|^2 <= B_2 at every point off the axis, and by continuity on the axis, which gives A C >= c_ax B^2. Applied to the limit of Theorem 1 at tau = 0, which is swirl-free with |U| <= 1, |grad U(y_*, 0)| = 1 and |grad^2 U| <= C_* almost everywhere, it gives C_* >= c_ax: for C_* < c_ax the nonconstant Case 2 alternative is impossible. The fields U_n may carry swirl, so for (A) itself only c_div is available. (The bound (LF_0) and the three steps were checked by hand step by step, and the identity (d) for n = 2 also numerically for random matrices; the numerical facts P_{B_2}(1/2) > 0.029, the bound 3.7 in Step 2, L_0 > 237/100, the value in Step 3 and the negative discriminant of P_{B_2}'(b)/b by exact rational arithmetic with rational bounds for 2^{1/2}, 7^{1/2} and 2^{1/4}.)

The kinematic hypotheses just used cannot exclude a normalized candidate limit for any C_* > 7^{1/2}/8, as the following construction shows. Let v(rho) = rho - rho^2/2 for rho <= 1, v = 1/2 for 1 <= rho <= 2, v = (1 - 3 tau^2 + 2 tau^3)/2 with tau = (rho - 2)/2 for 2 <= rho <= 4, and v = 0 for rho >= 4; v and v' are continuous (this is the core profile of the second part below, cut off so that the ring constructed next vanishes near the axis). The planar circular vortex V_0 = v(rho) e_phi has |grad V_0|^2 = v'^2 + (v/rho)^2 and |grad^2 V_0|^2 = v''^2 + 3 (v' - v/rho)^2/rho^2 (two kinematic identities for circular vortices, stated in the second part below); these equal 2 - 3 rho + 5 rho^2/4 and 7/4 for rho < 1, are at most 1/4 and 3/4 for 1 < rho < 2, and, since |v'| <= 3/8, |v''| <= 3/4 and v/rho <= 1/4 for 2 < rho < 4, at most 13/64 and 9/16 + 3 (5/8)^2/4 = 219/256 there. So V_0 is a compactly supported C^{1,1} field with sup |V_0| = 1/2, sup |grad V_0| = 2^{1/2} and ess sup |grad^2 V_0| = 7^{1/2}/2 (these values were checked by hand and, from the two formulas, by symbolic computation). For R_0 > 4 let V_{R_0} be the axisymmetric swirl-free field with meridional components (V^R, V^Z)(R, Z) = (R_0/R) V_0(R - R_0, Z). It is divergence-free (R^{-1} d_R(R V^R) + d_Z V^Z is R_0/R times the planar divergence of V_0), of class C^{1,1}, and zero where (R - R_0)^2 + Z^2 >= 16, in particular near the axis. At azimuth 0 its gradient consists of the planar gradient of the meridional components and the entry V^R/R, and its Hessian satisfies the identity used in (H); the terms carrying 1/R are O(1/R_0) on the support, and R_0/R and its derivatives differ from 1 and 0 by O(1/R_0) there. So sup |V_{R_0}|, sup |grad V_{R_0}| and ess sup |grad^2 V_{R_0}| tend to 1/2, 2^{1/2} and 7^{1/2}/2, and the quotient A C/B^2 of V_{R_0} tends to 7^{1/2}/8 as R_0 -> infinity. Regarded as time-independent fields, these rings are not steady Euler solutions. Hence, with the preceding paragraph, the infimum of A C/B^2 over nonconstant bounded divergence-free axisymmetric swirl-free fields of class C^{1,1} equals c_ax = 7^{1/2}/8 = 0.3307... (whether it is attained is not determined here), and an exclusion for C_* > c_ax requires information beyond these kinematic hypotheses. Such information could come from the Euler equation, another property of Theorem 1, or the prelimit Navier-Stokes dynamics.

Second, the pipe-flow threshold 1/2 is not a threshold for steady Euler fields in
general. After the scaling U(x) -> A_scale U(lambda_scale x) that makes the suprema of |U| and |grad U| equal to 1, the Hessian bound of a field is the
scale-invariant quotient sup |U| sup |grad^2 U| / (sup |grad U|)^2. For a planar circular vortex v(rho) e_phi, a steady solution of
the two-dimensional Euler equations, |grad U|^2 = v'^2 + (v/rho)^2 and |grad^2 U|^2 = v''^2 + 3 (v' - v/rho)^2/rho^2; for
v = rho/(1 + rho^2) one has sup |v| = 1/2, |grad U|^2 = 2 (1 + rho^4)/(1 + rho^2)^4 with maximum 2 at the centre, and
|grad^2 U| = 4 rho (rho^4 + 3)^{1/2}/(1 + rho^2)^3, so the quotient is the maximum of rho (rho^4 + 3)^{1/2}/(1 + rho^2)^3, which is
0.4513... (at rho = 0.4547...; checked by computer algebra and direct evaluation). The quotient is about 0.4770 for Gaussian
vorticity, v = (1 - e^{-rho^2})/rho, and about 0.4793 for the core whose vorticity is compactly supported and equal to a constant
multiple of (chi - b)_+^2, chi the planar stream function and b a constant (velocity of class C^{2,1}); these values are numerical approximations, and the last one is enclosed by the computer-assisted computation of (iv) in the third part below, whose programs are not reproduced here. For
every nonconstant bounded planar field of class C^{1,1}, divergence-free or not, the quotient (with the essential supremum of the Hessian) is at least 7^{1/2}/8 = 0.3307..., by (LF) with n = m = 2, and this bound is attained by a divergence-free field, the case n = 2 of the extremal of the first part: the circular vortex with v(rho) = rho - rho^2/2 for rho <= 1 and v(rho) = 1/2 for rho >= 1 has
velocity of class C^{1,1}, sup |U| = 1/2, |grad U|^2 = 2 - 3 rho + 5 rho^2/4 for rho <= 1 and 1/(4 rho^2) for rho >= 1 (so
sup |grad U| = 2^{1/2}, attained only at the centre), and |grad^2 U|^2 = 7/4 for 0 < rho < 1 and 3/(4 rho^4) for rho > 1 (checked by
computer algebra from the Cartesian field). Its mollifications by nonnegative normalized radial mollifiers of width tending to zero are
smooth circular vortices, hence steady planar Euler flows, with sup |U| <= 1/2, sup |grad^2 U| <= 7^{1/2}/2 (the Frobenius norm is
convex) and |grad U| at the centre tending to 2^{1/2}, so the limit superior of their quotients is at most 7^{1/2}/8. Hence
the infimum of the quotient over nonconstant smooth bounded divergence-free planar fields with bounded first and second derivatives,
and also over smooth circular vortices, equals 7^{1/2}/8. The extension of a
nonzero circular vortex independent of a third coordinate is a columnar vortex, which has nonzero swirl and does not belong to the
limit class of Theorem 1.

Third, for each p >= 2 and every C_* > Q_p (the quotient defined next), sufficiently thin swirl-free vortex rings with compactly supported cores of this kind have the properties listed in Theorem 1, and the computer-assisted enclosures of (iv), whose programs are not reproduced here, give Q_p < 1/2 for the listed p (a planar core alone does not show this: the axisymmetric divergence condition contains the additional term U^R/R, and the bounds
must hold globally). For p >= 2 let chi_p be the radial solution of -Delta chi = chi^p, chi > 0 in the unit disk B_1 of the plane, chi
= 0 on its boundary (it is unique, since every positive radial solution is a rescaling of the solution with value 1 at the centre),
extended by chi_p(y) = chi_p'(1) log|y| for |y| >= 1, so that -Delta chi_p = (chi_p)_+^p on the plane; let V_p = (-d_2 chi_p, d_1
chi_p), a circular vortex whose vorticity Delta chi_p = -(chi_p)_+^p is compactly supported and of class C^{1,1}, so that V_p is of
class C^{2,alpha} for 0 < alpha < 1, and let Q_p be its quotient (for p = 2 this is the core of the previous paragraph); put Q_core = inf_{p >= 2} Q_p.
(i) Existence. With L psi = psi_RR - psi_R/R + psi_ZZ = -R omega^theta for the stream function psi in the frame at rest at infinity
(U^R = -psi_Z/R, U^Z = psi_R/R), psi_c = psi - W_ring R^2/2 the stream function in the frame moving with speed W_ring, and k_ring a
constant, de Valeriola and Van Schaftingen (Desingularization of vortex rings and shallow water vortices by a semilinear elliptic
problem, arXiv:1209.3988, Arch. Ration. Mech. Anal. 210 (2013), 409-450, Theorem 1) and Cao, Wan, Wang and Zhan (Asymptotic behavior of
global vortex rings, Nonlinearity 35 (2022), 3680-3705) construct steady rings with eta = omega^theta/R = epsilon_ring^{-2} (psi_c -
k_ring)_+^p (the theorem of de Valeriola and Van Schaftingen gives circulations tending to a prescribed kappa; the fixed-circulation
form is used here). In the form stated by Cao, Lai, Qin, Zhan and Zou (Uniqueness and stability of steady vortex rings for 3D
incompressible Euler equation, arXiv:2206.10165v2, Math. Ann. 394 (2026), article 9; numbering of the arXiv version), Proposition 1.4:
for kappa, W > 0 and p >= 2 there is, for every sufficiently small epsilon_ring > 0, such a ring with circulation int int eta R dR dZ =
kappa, speed W_ring = W log(1/epsilon_ring), psi vanishing on the axis and at infinity, a constant k_ring that may depend on
epsilon_ring, meridional vorticity support Omega of diameter at most C epsilon_ring, and Omega converging, after an axial translation,
to the point (kappa/(4 pi W), 0) of the meridional half-plane. For p >= 2, eta is of class C^{1,1}, and elliptic regularity gives a
velocity of class C^{2,alpha} for 0 < alpha < 1, with bounded second derivatives (for finite p it is not of class C^infinity: for thin
rings h = psi_c - k_ring vanishes with nonzero gradient on the boundary of Omega, by (ii) below, so the vorticity R eta e_theta =
epsilon_ring^{-2} R h_+^p e_theta is not of class C^infinity there). Each axial Galilean frame of such a ring gives a bounded eternal
Euler solution whose suprema of |U|, |grad U| and |grad^2 U| do not depend on time (only the moving frame is steady; a uniform velocity
at infinity is allowed, as for pipe flows), and, after the Euler normalization performed in that frame (described after (iv)), it has
the properties listed in Theorem 1 whenever C_* is at least its quotient.
(ii) Core profile. Let h = psi_c - k_ring, z_ring = (R_ring, Z_ring) a maximum point of h, d_ring half the diameter of Omega and A_ring
= (epsilon_ring/(d_ring R_ring))^{2/(p-1)}. Proposition 3.2 of Cao, Lai, Qin, Zhan and Zou, with its proof, gives: the functions w(y) =
h(z_ring + d_ring y)/A_ring converge to chi_p in C^1 on compact sets as epsilon_ring -> 0 (along the whole family), d_ring/epsilon_ring
and A_ring have positive limits ((3.10) there), and R_ring -> kappa/(4 pi W). Two steps of the printed proof need repair. The energy
bound of Lemma 3.4 there is inferred from an inequality of the form X^2 <= C X^{p+1}, which gives only a lower bound for X. The upper bound follows from the energy identity E := int R^{-1} |grad h_+|^2 dR dZ = epsilon_ring^{-2} int R h_+^{p+1} dR dZ, h_+ = max(h, 0) (test the equation -div(R^{-1} grad h) = epsilon_ring^{-2} R h_+^p with h_+), the bound int h_+^p dR dZ <= C epsilon_ring^2 from the circulation (the radial weights are comparable to constants on Omega), and the two-dimensional Gagliardo-Nirenberg inequality int h_+^{p+1} <= C ||grad h_+||_2 int h_+^p, as in Proposition 3.7 of de Valeriola and Van Schaftingen: together they give E <= C epsilon_ring^{-2} E^{1/2}
epsilon_ring^2 = C E^{1/2}, so E <= C. And the identification of the limit must exclude the zero limit. The function w_+ vanishes
outside B_2; with lambda(y) = R(y)/R_ring, w satisfies -div(lambda^{-1} grad w) = lambda w_+^p, so E_w := int lambda^{-1} |grad w_+|^2
= int lambda w_+^{p+1} > 0, and the Poincare inequality on B_2 gives E_w <= C (sup w_+)^{p-1} E_w; hence w(0) = sup w >= c > 0
uniformly in epsilon_ring. The limit is then radial and decreasing (by the moving-plane argument there), with positivity set a disk
B_rho outside whose closure it is strictly negative, and rho = 1: the closures of the normalized supports {w > 0} contain 0 and have
diameter 2, hence contain points y with |y| >= 1, at which w >= 0, so rho >= 1; and they contain each compact subset of B_rho when
epsilon_ring is small, so rho <= 1.
(iii) From the profile to the global quotient (proved here). With R(y) = R_ring + d_ring y_1, w satisfies Delta w - (d_ring/R(y)) d_1 w
= -(R(y)/R_ring)^2 w_+^p. Since s_+^p is of class C^{1,1} on bounded sets for p >= 2, interior W^{2,q} and Schauder estimates give, for
every compact set N of the plane and 0 < alpha < beta < 1, bounds for w in C^{3,beta}(N) uniform in epsilon_ring, so w -> chi_p in C^{3,alpha}(N).
In the moving frame (U^R, U^Z)(z_ring + d_ring y) = (A_ring/(d_ring R(y))) J grad w(y) with J(a, b) = (-b, a), so the field b_ring U,
b_ring = d_ring R_ring/A_ring, has meridional components (R_ring/R(y)) J grad w, which converge to V_p in C^{2,alpha} on compact sets.
At each point, in the orthonormal frame e_R, e_theta, e_Z, the entries of d_ring^j D^j (b_ring U), j = 0, 1, 2 (Cartesian derivatives),
are the planar derivatives of order j of these meridional components together with terms that carry factors d_ring/R(y) (they come from
the rotation of the frame, for example the entry b_ring d_ring U^R/R of the gradient); so their Frobenius norms converge, uniformly on
compact sets of y, to those of D^j V_p. Outside the solid torus T generated by the meridional disk of radius L d_ring about z_ring (L >
2 fixed, so that T contains the vorticity; T does not meet the axis once L d_ring < R_ring), the velocity, which is the Biot-Savart
field of the compactly supported vorticity plus the constant velocity of the frame, is smooth (also on the axis), divergence-free and
irrotational, so every Cartesian component of U and of its derivatives is harmonic, Delta |D^j U|^2 = 2 |D^{j+1} U|^2 >= 0, and |D^j U|
tends at infinity to W_ring for j = 0 and to 0 for j = 1, 2; by the maximum principle on large balls, the supremum of |D^j U| outside T
is at most the larger of its supremum on the boundary of T and this limit, while on T, the solid torus generated by rotating about the axis the meridional image of the closed disk |y| <= L, the Frobenius norms converge uniformly, by the uniform convergence above on that disk and axisymmetry. Outside B_1,
|V_p|, |grad V_p| and |grad^2 V_p| are constant multiples of |y|^{-1}, |y|^{-2} and |y|^{-3}, so their values on |y| = L are below
their suprema, and b_ring W_ring = O(epsilon_ring log(1/epsilon_ring)). Hence b_ring d_ring^j sup |D^j U| -> sup |D^j V_p| for j = 0,
1, 2, and the quotient of the ring tends to Q_p as epsilon_ring -> 0. The suprema of |grad U| and |grad^2 U| are attained, since these
tend to 0 at infinity. A constant axial velocity changes no derivative and changes sup |U| by at most its modulus, so the same limit
holds in every axial frame whose speed relative to the moving frame is O(W_ring), in particular in the frame at rest at infinity.
(iv) Computer-assisted enclosures (the programs are not reproduced in this report, so the numerical endpoints below cannot be checked from it; the analytic statements of (i) to (iii) and the bound Q_core >= 7^{1/2}/8 do not depend on them). In the normalization in which the core stream function equals 1 at the centre, let g be its radial profile on [0, a], a its first zero; put v = -g' (the azimuthal speed) and f = g^p (the vorticity magnitude) in the core, v = a v(a)/rho and f = 0 for rho > a, and, for rho > 0, t = v/rho = rho^{-2} int_0^rho s f(s) ds, with t(0) = 1/2 by continuous extension. Since f is nonincreasing,
f/2 <= t <= 1/2, and |grad V|^2 = (f - t)^2 + t^2 is convex in t with value at most 1/2 at both ends, with equality at the centre; so
sup |grad V| = 2^{-1/2} and Q_p = 2 sup v sup |grad^2 V|. For each listed integer p >= 2 these suprema were enclosed by a validated
computation: interval Taylor integration of g' = -v, v' = g^p - v/rho in outward-rounded arithmetic with 200-bit mantissas (order 22;
on each step an a priori enclosure of the solution and a Lagrange remainder evaluated over it; exactly representable step points),
started at rho = 2^{-27} from elementary enclosures of g and v, with the bounds v <= rho/2 and |grad^2 V| <= 12^{1/2} p rho/4 on a
short initial interval ending at a step point (they follow from the equation, 0 < g <= 1 and the monotonicity of g there) and the exact
exterior formulas v = a v(a)/rho and |grad^2 V| = 4 a v(a)/rho^3 beyond the enclosed first zero a of g (to enclose a, the equation with
g^p is continued through the zero; it agrees with the core equation up to a, and beyond a only the exterior formulas are used). With
decimal endpoints rounded outward, it gives Q_2 in [0.479269, 0.479327], Q_3 in [0.465090, 0.465160], Q_4 in [0.460013, 0.460095], Q_5
in [0.457520, 0.457611], Q_6 in [0.456074, 0.456175], Q_8 in [0.454497, 0.454617], Q_10 in [0.453673, 0.453805], Q_20 in [0.452271,
0.452460] and Q_40 in [0.451684, 0.451936]; independent floating-point integrations for p = 2, 3, 10 and 40 fall inside these
intervals. A second, independently written validated computation for p = 2, 3 and 40 uses G(s) = g(e^s) and W(s) = e^s g_rho(e^s), so
that dG/ds = W and dW/ds = -e^{2s} G^p, with interval Taylor steps of order 36 in 160-bit outward-rounded arithmetic; at s = -32, with
R = e^{-32}, it starts from G in [1 - R^2/4, 1 - R^2/4 + p R^4/64] and W in [-R^2/2, -R^2/2 + p R^4/16] (from rho/2 - p rho^3/16 <= v
<= rho/2, which follows from v <= rho/2, 1 - g <= rho^2/4 and Bernoulli's inequality), with endpoints rounded outward; on the initial
interval it uses |grad^2 V| <= 7^{1/2} p rho/4 (for 0 < rho <= a put A = p g^{p-1} v and B = (2t - f)/rho; then 0 <= A <= p rho/2 by v <= rho/2, and 0 <= B <= (1 - f)/rho <= p (1 - g)/rho <= p rho/4 by f <= 2t <= 1, 1 - g^p <= p (1 - g) and 1 - g <= rho^2/4; moreover v'' = -A + B and (v' - v/rho)/rho = -B, so |grad^2 V|^2 = (B - A)^2 + 3 B^2 <= 7 p^2 rho^2/16); and it encloses the suprema on the
rest of the core over subintervals by branch and bound. It gives Q_2 in [0.479298018535999972783197097109401903,
0.479298018535999972783197097109401904], Q_3 in [0.465124851537398930978937248079634247, 0.465124851537398930978937248079634248] and
Q_40 in [0.451810057182066661308631214009201124, 0.451810057182066661308631214009201126], inside the intervals above (agreement between independently written implementations is a mutual consistency check; it does not establish the correctness of either, and the two use the same multiple-precision interval library, so a rounding defect in it could affect both). The explicit numerical sufficient conditions below
for C_* < 1/2 depend on the correctness of these computer-assisted enclosures; the floating-point integrations are consistency checks
only. The enclosures are strictly ordered as p increases through the listed values; they suggest that Q_p decreases, as p -> infinity,
to the quotient 0.4513... of the vortex v = rho/(1 + rho^2) above, whose vorticity magnitude 2/(1 + rho^2)^2 is, after rescaling, the
formal limit of the core vorticity magnitudes, but these computations establish neither the monotonicity of Q_p over all integers p >= 2 nor the convergence of Q_p to this quotient.
Consequently, for every C_* > Q_40 (in particular, if the enclosures of (iv) are accepted, for every C_* >= 0.452), sufficiently thin rings of the family with p = 40, after the
scaling U(x, t) -> U((M/D) x, t/D)/M (M and D the suprema of |U| and |grad U|), performed separately in each frame, have the properties
listed in Theorem 1, in the moving frame and in the frame at rest at infinity, so these properties alone do not exclude Case 2. In detail, for a fixed such ring: after the scaling, |U| <= 1 and |grad U| <= 1, with |grad U| = 1 at some point (the derivatives tend to 0 at infinity, so the supremum of |grad U| is attained), which an axial translation and a rotation about the axis move to (alpha_*, 0, 0) at tau = 0 with alpha_* finite, and |grad^2 U| <= C_* once the quotient is below C_*; the field is of class C^{2,alpha}, steady in the moving frame and a uniformly translating profile in the frame at rest, so it is a classical eternal Euler solution, with d_tau U = 0, respectively |d_tau U| <= W_ring/M (the normalized translation speed, which tends to 0 as epsilon_ring -> 0 because b_ring W_ring -> 0 while b_ring M -> sup |V_p| > 0), and |grad p_E| <= |d_tau U| + |U| |grad U| (p_E the Euler pressure), so |d_tau U| + |grad p_E| <= 2 for thin rings, within the bound of Theorem 1 (b) (whose constant C may be taken at least 2); before the scaling, eta = epsilon_ring^{-2} h_+^p is a function of the moving-frame stream function, hence transported by the moving-frame field; the scaling multiplies eta by M/D^2 and rescales its arguments, and neither this nor the passage to the frame at rest affects the transport equation, so eta is constant along particle paths in either frame, and the field is smooth and irrotational near the axis, so (c) holds; and ||omega(-A)||_infty is a positive constant, so (d) holds with c_U equal to it. These examples are compatible with the stated properties of the limit; they are not shown to arise as limits of a Navier-Stokes record sequence. More generally, they do not exclude it for any C_* > Q_core (choose p with Q_p < C_*, then a sufficiently
thin ring); the interval c_ax <= C_* <= Q_core is not fully classified here (by the kinematic rings of the first part, the kinematic hypotheses used there exclude no C_* > c_ax in it; if the enclosures of (iv) are accepted, this range lies below 2^{1/2}/3, so by the on-axis bound above only limits with alpha_* > 0 remain in question there; for each finite p >= 2, V_p is a bounded nonzero
circular vortex of class C^{2,alpha} with bounded first and second derivatives, so Q_p >= 7^{1/2}/8 by (LF) with n = m = 2,
and Q_core >= 7^{1/2}/8). Discrete steady rings with p = 2, computed by two independent discretizations (Fourier modes in Z on a
periodic ring train with finite volumes in R; finite differences on a box around the core with boundary values from the free-space
Green's function), have steady-frame quotients 0.498, 0.485 and 0.483 for support half-widths about 0.059, 0.023 and 0.014 R_0 (R_0 the ring radius; 0.540, 0.500 and 0.495 in the frame at rest at infinity); these uncertified values (maxima over the computational domains; the periodic train is a different problem from the isolated ring and approximates it only when the period is large compared with the ring) decrease as the relative core width
decreases and are qualitatively consistent with the limit Q_2 in (iii).

F3. Case 2 forces a quantified Type II scenario in which the critical quantity ||eta||_{L^1} (which may be infinite, in which case the bound below is vacuous), which is nonincreasing for
swirl-free flows, is at least of order 1/nu_n = M_n^2/D_n at t_n (no matching upper bound is claimed), and in which a fixed nonzero part of the terminal vorticity pairing is produced by the swirl source in the middle
history (Theorem 3(e)) within distance o((D_n M_n)^{-1/4}) of the axis when the times s_n of Theorem 3(e) (with Q_4([0, s_n]) = o(D_n M_n)) also satisfy s_n -> T_* (Theorem 3(f)). The required production
is measured by the physical quantity int int q^4 >= c D_n M_n; in rescaled variables int int q_n^4 dy dtau >= c nu_n over the
rescaled middle history.

F4. The swirl source is invisible to every Casimir int eta f(Gamma) dx (Proposition 4(a)): its product with any function of
Gamma is an exact axial derivative, f(Gamma) d_z(q^2) = r^{-4} d_z K(Gamma) with K'(s) = 2 s f(s) and K(0) = 0 (the primitive of Proposition 4(a)), so its z-integral
vanishes for each r and its pairing with f(Gamma) vanishes. Only the viscous terms change the Casimirs. The integrated Casimir
statements use (DEC); the local source cancellation does not. Signed Casimir
pairings cannot bound ||eta||_1, because they vanish when Gamma is even and eta odd in z; and a global sign of eta is not
preserved (a pure-swirl datum with z-dependent q_0 has eta_0 = 0 and d_t eta(0) = d_z(q_0^2), which takes both signs).
Three further exact forms of the circulation balance, none of which bounds it (all under (DEC)). (a) Nodal form. Write
C(t) = ||eta(t)||_{L^1(R^3)} = 2 pi int int |omega^theta| dr dz. At differentiability times t at which the zero set of eta(t) is a
regular surface of finite area carrying no zero plateau, the boundary traces exist and the entropy (coarea) limit of
int phi_eps(eta) dx can be passed (this is a hypothesis at such t, not a consequence of regularity alone; in general the identity
holds only as the inequality below), C' = P_nod - D_nod - A_ax with P_nod = int sgn(eta) d_z(q^2) dx, D_nod = 2 int_{eta = 0} |grad eta| dS (three-dimensional area) and A_ax = 4 pi int |eta(0,z)| dz; on a vertical line with finitely many simple sign changes z_i, int sgn(eta) d_z(q^2) dz
= - sum_i [sgn eta]_{z_i} q^2(r, z_i), so net production sits on the sign changes of eta, and one sign change crossing all radii produces
at most 4 pi int_0^infty r min(Q^2, G^2 r^{-4}) dr = 4 pi G Q, Q = ||q||_infty. (Creation from a zero plateau is not captured with
sgn(0) = 0; in general only C(t) <= C(0) + int_0^t ||d_z(q^2)||_1 holds.) A bound of P_nod by a constant multiple of D_nod + A_ax is false under all the normalized bounds: in rescaled variables (viscosity nu, delta = nu^{1/3}) take a fixed nonnegative background ring and, near the axis,
N ~ 1/(4 delta) disjoint cells q = delta Q_0(R/delta, (Z - Z_j)/delta), eta = delta^2 d_zeta(Q_0^2)(R/delta, (Z - Z_j)/delta),
Q_0 = F(rho) g(zeta) with smooth bumps F supported in (1, 2) and g in (-1, 1); then |U|, |grad U|, |grad^2 U| <= C, |Gamma| <= C nu,
P_nod >= c nu, nu D_nod <= C nu^{5/3} and A_ax = 0 at the initial time (in rescaled variables the nodal dissipation and the axis term carry the factor nu, so what is refuted there is a bound of P_nod by a constant multiple of nu (D_nod + A_ax)). This is a changing-datum, instantaneous statement only. (b) Label form.
With xi = r^2/2 the meridional transport is area preserving and D eta/Dt = {Gamma^2, h} + Delta_5 eta, h = 1/(4 xi), {f, g} =
f_xi g_z - f_z g_xi, a Boussinesq-type system with unequal diffusions for eta and Gamma; inviscidly, on a regular level Gamma = s off the axis
(h is undefined at xi = 0) the coarea coordinate mu (d mu = d sigma/|grad Gamma| in the (xi, z) plane, oriented so that
d_mu X = (-Gamma_z, Gamma_xi)) is material and eta = eta_0 + 2 s d_mu int_0^t h(X(mu, tau)) d tau,
so growth of C requires variation of the r^{-2}-weighted residence time along swirl levels, which nothing here controls. (c) Half-plane
form. C_>(z_0) = int_{z > z_0} int_0^infty omega^theta dr dz satisfies d/dt C_> = int_0^infty (u^z omega^theta - d_z omega^theta - r q^2)(r, z_0)
dr - 2 int_{z_0}^infty eta(0, z) dz. The swirl flux K_sw = int_0^infty r q^2 dr is nonnegative, at most G Q, and int_0^T int K_sw dz dt =
(2 pi)^{-1} int_0^T ||q||_2^2 dt <= ||u_0||_2^2/(4 pi) (as |q| <= |grad u|), but the transport flux u^z omega^theta is not controlled.

F5. Literature (checked against the arXiv abstracts where marked). None of the criteria checked here has been shown to exclude Case 2:
Chen-Strain-Tsai-Yau II (Comm. PDE 34 (2009) 203-232; abstract checked) assume |u| <= C|t|^{-1/2} or |u| <= C r^{-1+eps}|t|^{-eps/2},
which Case 2 violates (the first because a uniform bound |u| <= C (T_* - t)^{-1/2} gives |grad u(t)| <= C'/(T_* - t) by local smoothing of
mild solutions on intervals of length comparable to T_* - t, contradicting Corollary (i); the second because at the point of Corollary (vi), r = R_0 l_n and
|u| >= c M_n, while the condition with T_* - t_n >= c/M_n^2 would give r|u| <= C (r^2/(T_* - t_n))^{eps/2} <= C nu_n^{-eps}, which
is incompatible with r|u| >= c/nu_n for 0 < eps < 1 as nu_n -> 0); Lei-Zhang (arXiv:1505.02628; abstract checked) assume
|r u^theta| <= C|ln r|^{-2} near the axis, and Wei (arXiv:1508.03318; abstract checked) |r u^theta| <= |ln r|^{-3/2}; neither
follows from |Gamma| <= G. The same abstract states global regularity when the supremum of |r u^theta|, initially or near the axis, is small relative to
dimensionless quantities of the datum. The initial version requires the initial circulation, hence G, to lie below a datum-dependent
threshold; the near-axis version requires uniform smallness of the circulation in a region near the axis and need not make the global G
small, but that smallness does not follow from the Case 2 hypotheses either (|Gamma| <= G and Gamma = O(r^2) at each fixed time give no
smallness uniform in time near the axis). Neither smallness condition has been established here. The weighted swirl criterion of Chen, Fang and Zhang (Theorem 1.1 (1): r^d u^theta in L^p(0, T; L^q) with 0 <= d < 1, 2/p + 3/q <= 1 - d, 3/(1 - d) < q <= infinity and 2/(1 - d) <= p <= infinity) is used in R2.16 only with d = 0; its
statement was read and its proof was not checked. Further criteria (Pan on log-log bounds for b; Lei-Zhang on BMO^{-1} potentials;
Kang-Miura-Tsai epsilon-regularity; Seregin's Type II classification) were not checked against the journal texts here and are not used. In the Seregin summaries that follow, m is the scaling parameter of those papers (not the packet quantity m_phi), v is the prelimit velocity and x' = (x_1, x_2, 0), so that |x'| = r. Seregin, arXiv:2402.13229 (v3, read in full) extracts an ancient Euler limit from a potential Type II point by the Euler scaling v -> lambda^alpha v(lambda x, lambda^{alpha + 1} t), alpha = 2 - m, lambda -> 0 (Proposition 1.1, stated for suitable weak solutions in general and applied there to axisymmetric ones), under three hypotheses: a nonvanishing condition r_k^{-2 m_0} int_{-r_k^2}^0 int_{|x| < r_k} |v(x, t)|^3 dx dt >= c_1 > 0 along a sequence r_k -> 0, with m = 3 m_0/(2 + m_0) and 1/2 <= m < 1; uniform bounds on scaled local energy, dissipation and pressure quantities, with powers of the radius fixed by m; and uniform bounds on scaled mixed norms L^{l_1}_t L^{s_1}_x on parabolic cylinders of both the second spatial derivatives and the time derivative of v, with s_1, l_1 > 1 and 3/s_1 + 2/l_1 = 4. It shows (Proposition 2.2) conservation, for the limit, of the integral of |omega^theta/r|^{l_1/2}
under further hypotheses (a pointwise bound |v| <= c |x'|^{-alpha} on the prelimit solution and l_1 <= s_1, as in Lemma 2.1 there,
the exponent restriction (2.11) relating m and l_1, and finiteness of the moment at one time), and (Proposition 2.3, Corollary 2.4) excludes the singularity if in addition ess sup_t int |v|^{3/(2-m)} dx or
ess sup_t int |curl v|^{3/(3-m)} dx is finite on a fixed cylinder (the finite critical trace forces the limit to vanish at the final
time, and conservation propagates this backward); Sections 3 and 4 treat self-similar and discretely self-similar limits respectively. These weighted or critical bounds
have not been established for Case 2, and its record-time limit is not the terminal-trace limit used there. Seregin's papers arXiv:2507.08733v2 and arXiv:2606.29468v1 were also read (statements and the axisymmetric sections checked). In arXiv:2507.08733v2, Seregin uses power-weighted bounds corresponding to f(r) = r^{1-m}. In arXiv:2606.29468v1, he allows increasing weights f with f(0+) = 0 and f(1) = 1, including logarithmic and power-logarithmic examples, and assumes F(a) > 0 for every a > 0, with F defined below. Both papers extract nontrivial ancient Euler limits under their nonvanishing, weighted local energy, dissipation, pressure and parameter hypotheses (Theorem 3.1 in each paper). Their axisymmetric limits have zero swirl. For the conservation arguments, scaled mixed-norm bounds on both second spatial derivatives and the time derivative are additional hypotheses: on the Euler limit in 2507.08733, Proposition 4.2, and on the prelimit in 2606.29468, Section 4. Together with further hypotheses, these yield conservation of int |omega^theta/r|^{l_1/2}
(in 2606.29468, Proposition 4.1: l_1 <= s_1 with 3/s_1 + 2/l_1 = 4, a decay bound |v| <= c/(|x'| f(|x'|)) on the prelimit solution, the growth
condition a^{2 - 3 l_1/2}/F(a)^{(l_1 + 1)/2} -> 0 as a -> infinity on the limiting weight F(a) = liminf_{lambda -> 0} f(lambda a)/f(lambda), and a finite moment at one time; since these
exponent conditions force l_1 <= 5/4, the growth condition fails for the pure logarithmic example, where F = 1); exclusions are obtained only under an extra Ladyzhenskaya-Prodi-Serrin type condition
(2507.08733, Theorem 5.1) or for parameter ranges where the weighted bounds force the limit to vanish. The full set of hypotheses of
these criteria has not been established for Case 2, and no exclusion is obtained from them here. The a priori bound
|u| <= C r^{-2} |ln r|^{1/2} of Lei-Navas-Zhang (arXiv:1309.6625; abstract checked) gives no information at the record scale: at r of
order l_n it allows |u| of order l_n^{-2} |ln l_n|^{1/2}, while |u| <= M_n and, by the energy bound of the setting,
M_n l_n^2 = M_n^3/D_n^2 <= C(E_0) M_n^{-1/3} -> 0.
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
int_0^{R_0} q_n^2 R^3 dR <= (G nu_n)^2 (1/4 + log(R_0 (G nu_n)^{-1/2})); on the fixed lifted cylinder Omega_0 = {|w| < R_0, |Z| < L} in R^5 (R = |w|, w in R^4, as in Section 2.6)
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
scalar weighted functional tried here. Both
2606.07869 (Remark 10.8: the theorem does not "exclude the meridional Type-II record") and 2605.09797 (Section 7: such records are
"receiving branches rather than contradictions") state that their class of meridional Type-II records is not excluded there; Case 2
records appear to be of this type, but the record conventions of these papers were not compared with those of Section 1 in detail.
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
their argument uses decay of the limiting potential vorticity along backward meridional trajectories, with the decay supplied by
their matched bounds. With l(t) = M(t)(T_* - t) and (A), the global version of their Hessian bound,
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
(arXiv:2609.20803; the statements of Theorems 1.1 and 1.3 and of Remarks 1.2 and 1.4, and the proof outline of their Section 1, read) has two forms. Theorem 1.1 concerns suitable weak solutions on B(1) x (-1, 0), smooth on compact subsets, with a force whose spatial C^2 norm is bounded uniformly in time and which is real analytic in space, locally uniformly on compact subcylinders. It assumes exact axisymmetry on a ball of positive radius at each preterminal time and imposes anisotropic bounds on the angular mean. It is reduced to Theorem 1.3 for axisymmetric suitable weak solutions on the same cylinder, smooth on compact subsets, with a force uniformly bounded in the spatial C^2 norm. The zero force satisfies the force conditions of both theorems (Remark 1.2). After translation and parabolic rescaling, Case 2 solutions satisfy the solution-class and force hypotheses of Theorem 1.3; its regularity conclusion additionally requires the anisotropic bounds stated next, which have not been established here. Theorem 1.3 assumes on the fixed parabolic
cylinder |d_r^a d_z^b u^r| <= C (-t)^{-1/2-a/2-(1/2-h)b} and the same bounds with an extra factor (-t)^{-h} for u^z and u^theta (by Remark 1.4 (c) the bounds on u^theta can be dropped)
(a + b <= 2, 0 < h < 1/2; radial length (-t)^{1/2}, axial length (-t)^{1/2-h}). These are again matched pointwise bounds in -t, and, according to the proof outline of their Section 1, the
proof uses the decay of the limiting scalar in the remote past that these bounds supply, together with a comparison principle for
drift-diffusion equations with diffusion in only some of the variables. No implication from (A) or the Case 2 structure to these
componentwise bounds on a fixed parabolic cylinder has been established here (if they held there, Theorem 1.3 would make the point
regular), and the mechanism gives no bound on the middle-history production. None of the
published results examined here has been shown to apply to Case 2 and exclude it.

F7. Theorem 5 sharpens the localization of Theorem 3: the positive excess of the record vorticity above k_n is produced only at times when the instantaneous
Hessian is within a fixed factor of H(t_n), and only inside the super level set {eta > k_n}, near the axis. In the Euler limit
sup eta_U is constant in time, and Theorem 5(a) is its prelimit form on growing windows; it bounds the Hessian, not the gradient,
and is consistent with a slow decay of the gradient if the near-maximisers of eta approach the axis (it is not consistent with
TARGET-2, and by Theorem 1(d) TARGET-2 would already exclude Case 2). Theorem 5(c) leaves two alternatives: a super level set much longer than l_n along the
axis, or a production time at least of order l_n^2/G (rescaled (G nu_n)^{-1}); no upper bound on that time follows. The power-law
diagnostic of Section 4 is compatible with the second alternative at the level of scalar sizes, since there (G nu)^{-1} = G^{-1} eps^{-1/6} (G fixed)
is much smaller than D (T_* - t) = eps^{-1/3} and the Hessian stays comparable to H(t_n) over a production time C l_n^2/G.

F8. The adjoint forgets the terminal datum on the viscous time l_n^2 of the profile scale (Theorem 6), so production much older than
l_n^2 contributes little unless the older history carries correspondingly more q^4 or longer super level sets. Together with
Theorems 2, 3 and 5, the part of the signed pairing that no proved estimate makes small comes from ages between
A_max(n)/D_n = c (C_* max(G,1) nu_n)^{-1/2}/D_n (the window of Theorem 2; its contribution is at most C c^2 + o(1), small for small c,
without an o(1) bound for fixed c) and l_n^2 times a power of Q_4/(D_n M_n) (Theorem 6), near the axis in the sense of Theorem 3(f). Proposition 7 forces radial compression of
the swirl where it overlaps the adjoint somewhere in the middle history I_n; it does not locate that compression in this band. On that band only persistence-or-production alternatives are proved:
Theorem 5(b) throughout the band, and Theorem 3(g) on its part with |tau| <= nu_n^{-1}. This is the range that the present estimates leave open. In rescaled time it is the band A_max(n) <= |tau| <= min{t_n D_n, C nu_n^{-1} Lambda_Q}, where Lambda_Q = (Q_4([0, t_n])/(D_n M_n))^{2/3} >= c (the exponent for which
the bound of Theorem 6(b) makes the part of the pairing older than a large multiple of l_n^2 Lambda_Q small), which is not
shown to be bounded,
where the rescaled flow is no longer close to the Euler limit in any proved sense and where the time-integrated rescaled source mass per
unit axial length over [tau, 0] has the upper bound 8 pi C_* G nu_n |tau|, which grows from order G nu_n A_max(n) (comparable to (G nu_n)^{1/2} for G >= 1) to order one at |tau| of order nu_n^{-1}, and to
order min{nu_n t_n D_n, Lambda_Q} at the upper end of the available band (G and C_* fixed).

F9. Near the axis the obstruction takes a sharp form (Theorem 8). Far from the axis the swirl angular velocity is at most G nu_n/R^2 in
rescaled units, and a weighted adjoint energy (weight cosh((Z - Z_0)/S) e^{-2s/S}) shows that over ages up to Lambda/nu_n it produces at most C Lambda G^2 nu_n^{1/2} R_0^{-3} ||phi||_2 outside a tube of radius R_0
(Theorem 8(a), with C < 4.4 and nu_n L <= Lambda <= t_n/l_n^2), hence o(1) outside a tube of radius nu_n^{1/6 - epsilon} for fixed Lambda and outside any fixed tube for Lambda = o(nu_n^{-1/2});
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
number C_* delta^3/nu_n is of order G as well. In cell variables the coupled equations contain no coefficient that tends to zero with n (the viscosity coefficient
is nu_n/delta^3 = C_*/G, fixed for fixed G and C_*), and the dimensional
count permits production of order delta^3 = O(nu_n) per cell event (no construction is given here); order-one production would need of
order nu_n^{-1} such events with a positive signed mean, for instance about delta^{-1} cells along a unit length of axis renewed over about
nu_n^{-2/3} cell lifetimes of the inertial cell time delta^{-1} (the diffusive time is T_c = (G/C_*) delta^{-1}). Since d_Z a = eta + c exactly and the axial integral of d_Z a over a unit segment is the change of a, which is
O(delta) where |a| <~ delta at the endpoints, positive tilt of order one on a set of fixed measure must be compensated by negative tilt elsewhere
(a = delta sin(Z/delta) has d_Z a >= 1/2 on a set of measure about 1/3); this gives no smallness of either sign set, and a proof would have to show
that the swirl and the adjoint cannot weight the two signs unequally over ages of order 1/nu_n.
Two exact restrictions are known. If the velocity and the initial circulation are axially periodic with period at most L_0 delta and share
the reflection symmetry (U^R, U^Z, Gamma)(R, -Z) = (U^R, -U^Z, Gamma)(R, Z), the production P_w over ages K/nu_n is O(delta^j) for every integer j
(the auxiliary forced scalar h with (d_tau + U.grad - nu Delta_5) h = d_Z(q_n^2), h = 0 at the start of the window, age K/nu_n, satisfies
P_w = int h(0) phi, is odd and periodic in Z, and ||h||_infty <= 4 C_*^2 delta K/nu_n = 4 K C_* G delta^{-2} by the maximum principle, since
|d_Z(q_n^2)| <= 4 C_*^2 delta; an odd periodic function has zero axial mean, so, the period being at most L_0 delta, successive mean-zero axial primitives H_m of h satisfy
||H_m||_infty <= (L_0 delta)^m ||h||_infty <= C_m delta^{m-2}, with C_m depending on m, K, C_*, G and L_0, and m = j + 2 axial integrations by parts against the fixed smooth packet give
|P_w| <= C_j delta^j ||d_Z^{j+2} phi||_{L^1}); for
general axially periodic velocities the axial mean of h obeys d_tau hbar + R^{-1} d_R(R mean(U^R h)) = nu (d_RR + 3 R^{-1} d_R) hbar, so only
the radial eddy flux of h creates a mean. Weighted versions of the (J, eta) energy (weights R^alpha, functions of Gamma, of q, of the 5D
adjoint), pressure trades, the energy of the axial derivative of the velocity, and a Lagrangian (label) form of the production with its
exact viscous corrections were also tested; these calculations have not yielded the needed bound (each leaves a remainder that is critical
at the crossover radius or has no sign).

Core supply and cell relaxation. Several exact facts constrain the cells but do not bound their number. (a) Without flow, a saturated core
Gamma = B(1 - e^{-R^2/d^2}) (B = G nu_n) evolves in time s into Gamma = B(1 - e^{-R^2/(d^2 + 4 nu_n s)}), so q(0, s) = B/(d^2 + 4 nu_n s): the core
retains the fraction d^2/(d^2 + 4 delta^2) after one core time T_c = delta^2/nu (one ninth for a core at the cap, d^2 = delta^2/2), and
q(0, s) ~ G/(4s) as s -> infinity (an exact diffusion model). (b) Under the additional hypothesis Gamma >= 0 (not part of Case 2),
u^theta >= 0 and |d_ZZ u^theta| <= C_* give |d_Z u^theta|^2 <= 2 C_* u^theta, hence J^2 <= 2 C_* q/R with J = -d_Z q (without the sign
hypothesis this fails: U^theta = eps R exp(-R^2 - Z^2) sin Z has q = 0 and J != 0 at Z = 0); the eta generated by the source in
one core time from zero initial value is at most 2 ||q|| ||J|| T_c <= 4 C_* G (this does not bound the total eta); eta is Lipschitz in Z with constant 2 C_*/R; and for the decaying induced velocity
||d_Z a||_{L^2(R^5)} <= ||eta||_{L^2(R^5)} (the multiplier k_z^2/|k|^2), with the corresponding L^2(R^4) estimate for each axial frequency. (c) In the stochastic representation of
Gamma (backward paths with Bessel-0 radial noise, killed at the axis), Gamma(x) = E[Gamma(X_h) 1(alive at h)]; with only |Gamma| <= B this gives
q(x) >= (B/R_0^2)[(1 + theta) P(rich landing) - P(alive)] (rich: Gamma >= theta B at the landing point, 0 < theta <= 1). In the globally linear
strain model U^R = a(tau) R, R_s exp(int_0^s a(tau - v) dv) (backward time s, as in (f)) is a time-changed Bessel-0 process and the survival probability from radius R_0 over a horizon h is
1 - exp(-R_0^2/(4 nu I_h)) with I_h(tau) = int_{tau - h}^tau exp(2 int_s^tau a) ds. Under the additional hypothesis Gamma >= 0 and with
p_h = liminf_{R_0 -> 0} P(rich landing | alive), this gives q(0, tau) >= theta G p_h/(4 I_h(tau)), and, from |Gamma| <= B alone,
|q(0, tau)| <= G/(4 I_h(tau)) for every horizon 0 < h <= tau + t_n D_n within the available history. These probabilities constrain circulation survival; they do not imply that every contributing path has seen radial
compression (Gamma survives a finite interval with a = 0, see (a)), and for spatially varying strain the random time change cannot be inserted
into the deterministic-time law without further analysis. Under a quantified supply hypothesis giving exactly q(0) >= theta G A/2 for a sustained
radial compression a = -A, the cap gives A <= 4 C_* delta/(theta G); an asymptotic version needs an error estimate on the same scale, and brief
strong compression of circulation-rich fluid is not excluded. These calculations suggest studying adjoint-weighted histories of J and d_Z a;
a precise sufficient estimate of that kind and a proof connecting it to the production pairing are not available. (d) Exploratory computations (axisymmetric Navier-Stokes with swirl at the cell scale in a prescribed meridional background; not
independently reproduced here, and their specification is not included) suggested relaxation to the Burgers state under spatially uniform
strain, and a nonzero mean production against a cell-scale weight under a maintained axial variation of the strain (externally imposed,
axially periodic, zero spatial mean); under a reflection symmetry with an even weight on a symmetric domain the signed export vanishes
exactly. This suggests that Burgers relaxation alone will not give P_w = o(1) and that the question is whether the coupled flow can maintain
cell-scale strain variation; no numerical lower bound, convergence certificate or conclusion about the Case 2 pairing is asserted. (e) No theorem
from the Burgers-vortex stability literature (Gallay-Wayne, Gallay-Maekawa, Maekawa-Miura-Prange) is applied here: to use one, its prescribed
strain, perturbation class, norm and size assumptions would have to be verified for the forced and possibly renewed cores considered here,
which has not been done. If a nonnegative functional of the swirl alone (such as int J^2, or a relative entropy of q or Gamma with respect to
that profile) vanishes at the initial Burgers profile and becomes strictly positive when an allowed meridional perturbation generates J, it
cannot be nonincreasing for every such perturbation, because a small meridional perturbation creates J at once; this does not rule out every
monotone functional of the swirl (||Gamma||_infty, and nondecreasing functions of this norm, are nonincreasing); if a
coupled perturbation energy such as E = int (eta^2 + J^2) d^5x can be proved to satisfy E' <= -(2A - C_cpl) E (A > 0 the radial compression rate of the Burgers profile, U^R = -A R) with a specified constant
C_cpl < 2A, it decays exponentially; no such estimate with coefficients controlled by the Case 2 assumptions is proved here. A
unit-scale irrotational background U^R = (-a_0 + beta Z) R, U^Z = 2 a_0 Z - beta Z^2 + beta R^2/2 (eta = 0, d_Z a = beta) contributes beta(2q + R q_R)
to the J equation, of amplitude G beta/C_* in the diffusive cell normalization (r = R/delta, s = nu tau/delta^2, q/(C_* delta), J/C_*), so smoothness
of the background yields no factor of delta (this and the harmonic field below are local polynomial fields; a localization must preserve the divergence, for example by cutting
off a stream potential).
(f) A supplied-compression bound and exploratory fold computations. Write the backward circulation path started at radius R_0 at time t, absorbed at the axis, as
dR = (-a R - nu/R) ds + (2 nu)^{1/2} dW (W a standard Brownian motion, s the backward time, coefficients at time t - s). Then R_s^2 = exp(2 I_s) F(H_s) with I_s = -int_0^s a, H_s = int_0^s exp(-2 I_v) dv and F a squared Bessel process
of dimension 0 (dF = (8 nu F)^{1/2} dbeta), whose law at a fixed time u > 0 is 4 nu u times a Poisson(R_0^2/(4 nu u)) sum of unit exponentials. Hence,
under the additional hypothesis Gamma >= 0 at the landing time, q(x) >= (theta G nu / R_0^2) P_x(the path lands in {Gamma >= theta G nu} unabsorbed);
with only |Gamma| <= G nu the lower bound is (G nu/R_0^2)[(1 + theta) P_x(rich landing) - P_x(alive)], as in (c). For a constant compression a = -A, R_0^2 = nu/A and a window h
with A h >= max(log 2 / 2, log(rho (A/nu)^{1/2})), the landing probability beyond radius rho is at least c_0 = e^{-1}(1 - e^{-1/2}) > 0.144, so if Gamma >= 0 and the
probability of rich, surviving landings is at least p_* > 0 (p_* = c_0 when every landing beyond rho is rich), then A <= 2 nu/(p_* theta delta^2): a persistent, circulation-supplied compression of the core cannot exceed a fixed multiple of lambda_c.
For a general flow the time change H depends on F; a bound of the same kind would need in addition a stopped comparison of the radial path with the constant-compression diffusion up to the exit from the compression region, with the probabilities of that exit and of landing outside the rich set subtracted from p_* and the remainder bounded below by a positive constant independent of nu (this comparison is not carried out here); the bound does not say that rich fluid can never be strongly compressed later. At a simple axis zero z_0(t) of
a with k = d_Z a and V = U^Z(0, z_0(t), t) - z_0'(t), the axis identity gives p_RR = q^2 + nu Delta_5 a - V k there, and, if nu ||D^3 U||_infty = O(nu^{1/2} + nu^{alpha/2})
(any 0 < alpha < 1) after one unit of past time under the bounds of Theorem 1(b) and the canonical pressure (argued from a parabolic estimate for
D U with C^alpha forcing D^2 p, not proved here as a lemma), then p_RR -> 0 at a material zero; a zero need not be material. A harmonic exterior field (stream potential c_h (Z^2 - R^2/4), c_h a constant, eta = 0) supplies the constant d_Z a = -2 c_h near the axis, so cell-scale
strain variation need not be self-induced. Exploratory steady computations (cell units, finite cylinder, exact background fold a = A_f Z, axial velocity
U_0 - A_f Z^2, circulation supplied on inflow, self-induced flow included; not independently reproduced here, and their discretization and resolution are not given here) suggested that a
boundary-maintained fold can sustain nonzero production against a fixed smooth weight, as the counts allow; no numerical lower bound is asserted. Finally the cap gives sup_{Z, tau} int q^2 2 pi R dR <= 4 pi C_*^2 delta^4, so
|P_w| <= 4 pi C_* G nu delta int_0^{K/nu} V_nu(s) ds with the weight w_nu(R) = min(R/r_c^2, r_c^2/R^3), r_c = delta/2^{1/2}: an independent derivation of
the form of Theorem 8(b), with the same missing estimate.
(g) Supply comparison and multiscale escape. If U^R <= -A R on a cylinder {R < b, Z in I} during [t_0, t_0 + T] and Gamma >= g on its parabolic
boundary, where g = theta G nu (1 - exp(-R^2/h(t))) and h' = 4 nu - 2 A h (so that g is a subsolution of the circulation equation, since g_R >= 0),
then q(0, Z, t_0 + T) >= theta G nu / h(t_0 + T); once h has relaxed to within a factor 1 + eps of 2 nu/A this gives q(0) >= theta G A/(2(1 + eps)) and the
cap forces A <= 4 (1 + eps) lambda_c/theta. This is a statement about maintained, supplied compression; the bounds allow a short compression pulse
of order one on a circulation-rich core, so no instantaneous restriction follows. For the radial escape of the circulation and adjoint
paths across the octaves between R ~ delta and R ~ 1, the formal calculation below suggests that zero net radial flux need not determine an
effective radial process: the field with stream
function alpha eps^3 R cos(Z/eps), nu = eps^3, has zero net flux over every axial period and obeys the derivative bounds for small alpha, but on a
fixed annulus the formal two-term corrector calculation predicts for each path family the radial operator kappa_r f'' + (kappa_r - 2) f'/R, kappa_r = 1 + alpha^2/2, hence exit probabilities in both directions of a Bessel process of dimension 2 - 2/kappa_r rather than of dimension 0
(convergence of the stopped processes and of their exit probabilities is not proved, the streamfunction needs a further modification near
R = 0 to define a smooth axisymmetric field, and nothing is claimed uniformly down to R ~ delta).
The formal calculation thus suggests that net flux alone need not determine the effective radial dynamics; pointwise drift bounds do give barriers
(R^{2-d} is a supermartingale barrier when the radial drift is bounded accordingly), and instantaneous streamline topology gives no material
bundle count for unsteady flow. A heuristic sufficient condition (norms, damping inequality and patch overlaps not specified here): if the active region is covered by O(1/delta) cell patches whose cell
energies N_i = ||eta_i||^2 + ||J_i||^2 (cell units) satisfy a damped inequality with total supply (initial plus forcing, over K/delta^2 cell times)
o(delta^{-3}), then Cauchy-Schwarz would give P_w = o(1), provided also an estimate relating the cell energies to the adjoint-weighted production (not established here); such supply bounds are not available for forced or renewed cells.
(h) Closed cells, strong strain and monotone moments. Three further mechanisms were examined. First, in a closed axially periodic cylinder
{R < b} of period L with U^R = 0, d_R U^Z = 0 and Gamma = G_b on the wall, the perturbation w = U - Omega_b R e_theta - V e_Z of the solid rotation Omega_b = G_b/b^2 (V the conserved mean axial velocity) satisfies the exact identity E' = -nu int |grad w|^2 dx for E = (1/2) int |w|^2 dx (in the frame
rotating with Omega_b the Coriolis force does no work and every wall term vanishes), hence E(t) <= E(0) exp(-2 nu t/C_P) with a Poincare constant C_P of
order max(b^2, L^2); the period-mean eddy flux F = <U^R eta> obeys the exact identity F = -R^{-2} d_R(R <U^R (U^Z - V)>) and
int_0^T int_0^b |F| R dR dt <= C E(0)/(L nu) for every T. In a closed cell the perturbation energy therefore decays exponentially and the cumulative period-mean eddy flux is bounded,
for every G and uniformly in the history length (these are the two controlled quantities; no pointwise bound on gradients or on
the adjoint-weighted production follows). The argument uses the impermeable wall: in the open near-axis region the local energy balance
contains boundary work, pressure work and incoming vorticity, and no cumulative bound on these is available, so it does not transfer. (A related
inviscid available potential energy relative to a profile with Gamma_0^2 increasing in R is exact, but viscosity adds terms of indefinite sign.)
Second, a strong-strain statement for the production holds only conditionally: the Feynman-Kac representation of q, whose equation is
(d_tau + U.grad - nu Delta_5) q = -2 a q, gives the factor exp(-2 m_s) when every contributing path accumulates strain at least m_s over the window,
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
vector of the constraint matrix. For instance, with W = Z e^{-R^2} and the Stokes stream function Psi = R^4 exp(-R^2 - Z^2/(2 L^2)) (U^R = -Psi_Z/R, U^Z = Psi_R/R) the form equals
pi^{3/2} (3 - 16 L^2)/(27 L) while the squared L^2 norm is pi^{3/2} (L + 3/(16 L)) and the moment and the impulse vanish, so suitably normalized fields with
equal energy and equal nonzero swirl have opposite moment derivatives. These are instantaneous statements; a time-integrated inequality
along histories whose vorticity is generated by the swirl is not excluded by them. None of the three mechanisms yields the missing estimate. An exploratory time-dependent computation in the closed cylinder (not independently reproduced here; its discretization and resolution are not given here) relaxed to solid rotation, as the closed-cell identity predicts; its initial data were
symmetric under Z -> -Z, which makes the flux densities U^R eta and U^R (U^Z - V) odd in Z (V = 0 under this symmetry), so their period means vanish identically, so it carries no information about
asymmetric layers.
(i) A multiscale cascade as a sharpness test. One way to show that the missing estimate cannot follow from kinematic information alone (bounds on the
poloidal field and a passive circulation 0 <= Gamma <= G nu) would be a prescribed poloidal field with cells at the octaves r_k = 2^k delta that
carries production of order one. The natural candidate fails. A cell of Stokes stream function A r_k R^2 sin(Z/r_k) has velocity, gradient and Hessian of
sizes A r_k, A and A/r_k, so the Hessian bound fails as r_k -> 0; with Stokes stream function A r_k^2 R^2 sin(Z/r_k) and fixed A the cell Hessian is uniformly
bounded, which permits C^{1,1} limits and does not imply C^2 compactness (a particular assembled limit is not constructed here). (Tapered strengths A 2^{-eta k} are not excluded by this.) Nor does a product of octave-wise exit probabilities estimate radial
escape: for the one-dimensional diffusion nu kappa_r f'' + nu (kappa_r - 2) f'/R on (0, 1), killed at 0 (p > 0, 0 < delta < 1), with kappa_r = 1 for R <= delta and kappa_r = (R/delta)^p for R >= delta, the scale density is R for R <= delta and (delta^2/R) exp[(2/p)(1 - (delta/R)^p)] for R >= delta, so the
probability of reaching 1 before 0 from R = delta lies between 1/(1 + 2 e^{2/p} log(1/delta)) and 1/(1 + 2 log(1/delta)) and tends to zero,
although the product of the octave-wise factors 2^{-2/kappa_{r,k}}, where kappa_{r,k} = kappa_r(2^k delta) = 2^{kp} for the integers k >= 0 with 2^k delta <= 1, stays above exp(-2 log 2/(1 - 2^{-p})): a path returning inward meets every inner
octave. Eventual escape gives in any case no lower bound for the adjoint. Arrays symmetric under Z -> -Z give exactly zero signed
production against an even weight on a symmetric domain; against a general terminal weight reflection symmetry alone gives no exact
cancellation (for pure-swirl data u^theta = r e^{-r^2 - z^2} the source d_z(q^2) = -4 z e^{-2(r^2 + z^2)} is odd but pairs nontrivially with
a nonnegative weight supported in z > 0). Profiles such as sin(zeta) + beta cos(2 zeta) with suitable nonzero beta remove that parity
obstruction, but their signed production requires a separate calculation. Production per unit length then has the form C_* G nu pbar; exploratory runs with one to three octaves (not independently reproduced here; their discretization and resolution are not given here) gave nonzero values of pbar and no bound uniform in the number of octaves. Whether kinematic information
alone can give the missing estimate therefore remains open.

F10. The forward side of the production and its obstruction in a model (Theorem 9). Theorem 9 moves the difficulty to the forward dynamics
of the swirl. Using no information on the adjoint beyond 0 <= Psi_n <= P, Case 2 forces two things: a time integral at least c/nu_n of the
positive part of the self-compression rate in the scale-invariant functional Sigma, and the lower bound (1/3) log(1/nu_n) - C at t_n for the running supremum Act(t_n) = sup_{0 <= s <= t_n} int_0^s (- Abar)
of the Sigma-averaged signed compression action (an endpoint bound for int_0^{t_n} (- Abar) itself is not claimed). Shahmurov (arXiv:2604.21213v3, Theorem 3.1, Corollary 3.5, Theorem 7.1(i)) proves that a first singularity of the maximal
H^2 solution with bounded circulation forces the critical signed compression actions of his family (indexed by j >= 3/2; for 3/2 <= j < 2 under an
additional finite critical mass) to be unbounded above (the supremum over t of the action up to t is infinite); the proof uses the weighted swirl criteria of Chen, Fang and Zhang (DCDS 37 (2017)). The action of
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
Theorem 6.1 (for smooth rapidly decaying axis-compatible profiles and alpha > 1, when the displayed integrals converge, as they do for
1 < alpha <= 5, his form is int |grad phi|^2 r^alpha dr dz + ((3 - alpha)(alpha - 1)/2)
int phi^2 r^{alpha - 2} dr dz, nonnegative for 1 < alpha <= 5 by the Hardy inequality, with no positive full-gradient gap at alpha = 5; at
alpha = 1 his formula contains a separate axis term int |phi(0, z)|^2 dz); it concerns the frozen instantaneous response, not the subsequent evolution.
(c) Memory, Sigma weight: a negative periodic example and a localized drift-free prescribed-swirl family with critical self-compression. Let k = 1/20, L_k = - d_rr - (3/r) d_r + k^2, g(r) = r^{1/2} exp(-(log r)^2/4)
(flat at the axis), h = L_k^2 g, B = (h^2 + g^2)^{1/2} and f = B(r) + h(r) cos(k z) >= 0. The steady response is a_s = K (-Delta_5)^{-1} f
= k^2 g(r) cos(k z). The Sigma-weighted work per unit axial length is 2 pi avg_z int a_s f r^2 dr = pi k^2 I_k, where
I_k = int_0^infty r^2 h g dr = (2 pi)^{1/2} (-1/8 + e^2/200 + e^8/160000), approximately -0.17402 < 0. (The substitution r = e^s turns the three terms of
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
Appendix C avoids both limitations: it expands around a modulated approximation built from transported periodic solutions rather than around the drift-free localized solution of Appendix B (the periodic steady states themselves are expanded around the epsilon = 0 periodic state), and it bounds the velocity error directly in the velocity formulation, without a bound on the vorticity
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
by differentiating the convection coefficient are needed for the cancellation (checked here by hand and by symbolic computation, Section 5 (11)).
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
f(R) e_Z, so for C_* > 1/2 even E_n -> 0 would not by itself exclude a nonconstant limit (F2). The Hou-Shi-Wang blowup results concern different operators or
boundary problems and inviscid or partially viscous equations, and the Hou-Li class consists of special exact solutions of infinite
energy; neither settles the fixed-datum whole-space Case 2 problem. These models motivate seeking a convection-dependent estimate; they
neither prove nor refute the bound in item (6) of the open questions (Section 4) for the actual whole-space solution.
(d) A coupled critical balance (a formal identity). Let psi be the canonical stream
function (a = - d_z psi, - Delta_5 psi = eta), A = - Delta_5, F = (1/2) int |grad psi|^2 r dx (critical, like Sigma), I = int a q^2 r dx,
D_q = 2 int |grad q|^2 r dx + int q^2/r dx, D_psi = int [psi_rr^2 + 2 psi_rz^2 + psi_zz^2 + (7 psi_r^2 + psi_z^2)/(2 r^2)] r dx >= 0,
h = A^{-1}(psi_r/r^2 + psi/r^3), chi_1 = psi/r - h = A^{-1}(eta/r + psi_r/r^2), C = pi^{-1} int h_z q^2 dX and T = - pi^{-1} int chi_1 b.grad(eta) dX.
The following identity holds for smooth axis-compatible fields for which the canonical inverses exist, all displayed integrals are finite,
differentiation under the integral is valid, and the boundary terms in the integrations by parts vanish as the radial, axial and axis cutoffs
are removed; the derivation is under these additional hypotheses, and their verification from the standing Case 2 assumptions (including the
construction of chi_1, the cancellation at r = 0 and the estimates at infinity) is an additional step not supplied here.
Then F' = pi^{-1} int chi_1 d_t eta dX, and for every kappa, (Sigma + kappa F)' = - (D_q + kappa D_psi) + (kappa - 3) I + kappa (C + T). The source
contributes I + C, the diffusion - D_psi and the transport T. With kappa = 3 the stretching cancels. In Case 2 the critical
poloidal functional is large at the record. With K_b = int |b|^2 r^{-1} dx, the inequality (2 psi + r psi_r)^2 <= 8 psi^2 + 2 r^2 psi_r^2 and the Hardy
inequality int_0^infty psi^2 dr <= 4 int_0^infty r^2 psi_r^2 dr give K_b <= 68 F; rescaling about the axis point (0,0,z_n) gives K_b(t_n) >= nu_n^{-2} int_B |U_n^p(y,0)|^2 R^{-1} dy for any ball B, and by the uniform convergence of Theorem 1 the right side is
c_B nu_n^{-2} (1 - o(1)) with c_B = int_B |U(y,0)|^2 R^{-1} dy > 0 when B contains a neighbourhood of the record point. Hence
F(t_n) >= (c_B/68) nu_n^{-2} (1 - o(1)), and, if the identity holds along the solution on [0, t_n] (the additional step described above), integrating it with kappa = 3 and using Theorem 9(b) gives
int_0^{t_n} (C + T) dt >= (c_B/68) nu_n^{-2} (1 - o(1)) + (2 m_phi/(3P)) nu_n^{-1} (1 - o(1)) - (Sigma(0) + 3 F(0))/3. So any estimate
3 (C + T) <= epsilon (D_q + 3 D_psi) + e(t), with epsilon < 1 and int_0^{t_n} e = o(nu_n^{-2}), would exclude Case 2, provided the identity
holds along the solution (the verification described above, not supplied here). The bound on F(t_n) uses only
the nonconstancy of the limit (F of order (M_n l_n)^2 is the size of an Euler-strength structure of velocity M_n at scale l_n); by
F' = - D_psi + I + C + T it forces int_0^{t_n} (I + C + T) dt >= (c_B/68) nu_n^{-2} (1 - o(1)) - F(0), and by itself it says nothing about how
the swirl enters. C is the part of the source response that survives because r^{-1} does not
commute with A^{-1} (in the drift-free model T = 0 and C carries the indefiniteness of (c)); for a weight w the correction vanishes identically
only if w is constant, and r^{-1} is the only critical radial power. T is cubic and D_psi quadratic in psi: for the swirl-free datum
psi_* = z e^{-(r^2 + z^2)}, T[psi_*] = pi^2 (35299/82944 - (645 sqrt 2/2048) arctan sqrt 2), approximately 8.2523e-4 > 0, and since T[c psi_*] = c^3 T[psi_*] and
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
diagnostic of the quantifiers, not a solution). The arguments below make no use of that additional information. Since the rescaling W_n subtracts no axial drift, unboundedness
of |u^z|/S_n on a fixed normalized cylinder along the sequence already defeats the local witness (a fixed large value of the normalized
drift does not), so its failure carries little information on the swirl itself.
For every reading of the witnesses discussed above, a uniform velocity packet in the witness window forces every subsequence of a swirl
record sequence to fail at least one witness, so for such sequences NO-SWIRL-EXTRACTION adds no restriction beyond the Case 2 estimates
(derived by the second model of Section 5, a language model, and checked here; the existence of such swirl record sequences is not asserted). Let t_n be the gradient record
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
H = C_* eps^{-23/12}, G and C_* fixed. Then M H = C_* D^2, nu = D/M^2 = eps^{1/6} -> 0, M <= C E_0^{1/5} D^{3/5} for small eps, M >= eps^{-1/2}
(Leray), and d(A) = 1 for every fixed A because A/D_n = o(eps_n). WINDOW holds trivially, TARGET-2 fails, and the budgets of
Corollaries (ii), (iii) are met. With ||grad u(t)||_2^2 ~ eps^{-1+delta} (0 < delta <= 1/12: integrable, and above the lower bound
D^5/H^3 = C_*^{-3} eps^{-11/12} that follows from ||grad u||_infty^5 <= C ||grad u||_2^2 ||grad^2 u||_infty^3) and ||q||_infty ~ (G H^2)^{1/3}, the size bound for int q^4 dx is ~ eps^{-23/9 - 1 + delta}, so the resulting upper budget for Q_4 over the
middle history is of order eps_n^{-23/9 + delta}, far above the requirement D_n M_n = eps_n^{-25/12} of Theorem 3. The listed
scalar growth and budget inequalities are mutually compatible in this diagnostic. It is not a Navier-Stokes solution or a simultaneous spatial
realization of all the estimates, and it does not rule out deriving a stronger bound from the kinematic assumptions; it shows only that a proof
of TARGET-2 or of Q_4 = o(D_n M_n) cannot come from these scalar inequalities alone and must use further structure (signs, transport
geometry, the coupling between Gamma, eta and the adjoint). The same exponents are compatible
with the scalar size consequences of Theorems 5 and 6 and Proposition 7 when the production sits at ages of order l_n^2 (this does not verify their signed identities, the adjoint evolution or the spatial localization, and no simultaneous realization of these is asserted; a non-NS spatial
model of this, a long truncated pipe flow with a swirl core of radius (G/H)^{1/3}, was examined as a consistency check; it is not a solution).
The exponent bookkeeping of all constraints was checked by exact arithmetic.

Time geometry of records. Two elementary facts hold. First, D(t)^2 <= 6 M(t) H(t) (symmetric Taylor expansion along a line, and the
largest singular value of a 3 x 3 matrix is at least its Frobenius norm divided by sqrt3; F2 gives the sharper constant K_div = 3.7025... in place of 6, which is not needed here), so with m_n, d_n, j_n the ratios of M, D, H at
time t_n - l_n^2 to their values at t_n, (A) at both times gives m_n j_n/(6 C_*) <= d_n^2 <= 6 C_* m_n j_n: along a subsequence either all
three ratios stay bounded below over the whole band of ages up to l_n^2 or one of m_n, j_n tends to 0; the dichotomy and the scalar
estimates used here do not select an alternative. Second, with g(t) = ||grad u(t)||_infty (instantaneous) and J_n = [t_n - l_n^2, t_n - sqrt(nu_n) l_n^2], a ball of radius
g(t)/(2 H_n) around a maximum point gives
int_{J_n} ||grad u||_2^2 dt >= (pi/(24 C_*^3)) (M_n^5/D_n^3) Xi_n, Xi_n = l_n^{-2} int_{J_n} (g(t)/D_n)^5 dt.
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
hypothesis nor the signed production identity. The exponents and limits were checked by exact symbolic computation.

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
These models (checked by exact symbolic computation) are tests of single implications; none realizes the production of Case 2.

Limitations of the estimates developed here: backward ODE integration of D gives only lower bounds; the
properties of the Euler limit listed in Theorem 1 imply no Liouville rigidity when C_* > Q_core, where Q_core is the infimum over p >= 2 of the planar core quotients Q_p of F2 (Q_core >= 7^{1/2}/8 is proved, Q_core <= Q_40 follows from the definition, and Q_40 < 0.45194 rests on the computer-assisted enclosure of F2 (iv), whose programs are not reproduced here; the examples are pipe flows when C_* > 1/2 and thin vortex rings with velocity of class C^{2,alpha} for every C_* > Q_core, F2), and the interval 7^{1/2}/8 <= C_* <= Q_core is not fully classified here (these properties exclude Case 2 for every C_* < 7^{1/2}/8 = 0.3307..., the sharp swirl-free floor of F2, and a limit whose record point lies on the axis whenever C_* < 2^{1/2}/3; the kinematic hypotheses used in F2 alone cannot exclude Case 2 for any C_* > 7^{1/2}/8, F2); sup-norm control of the adjoint gradient loses to transport stretching; the
Casimir cancellation (F4) is exact but its viscous terms have no sign, and no bound on them sufficient for the closure is available; the L^2 energy of q obeys
(1/2) d/dt ||q||_2^2 + ||grad q||_2^2 + 2 pi int q(0,z)^2 dz = -2 int (u^r/r) q^2 dx, whose right side (radial compression) is not controlled by the estimates here at the strength the closure needs; an unweighted rescaled gradient integral int int |grad_y U_n|^2 dy dtau of order log(1/nu_n) over a window corresponds to a
physical dissipation O(D_n^{-1/5} log D_n), which tends to zero (the physical dissipation of the window is (M_n^3/D_n^2) int int |grad_y U_n|^2 dy dtau,
M_n^5 <= C E_0 D_n^3 by the energy bound, and nu_n >= c D_n^{-1/5}; the normalized dissipation of Theorem 8(a) carries the further factor nu_n), so
this per-window estimate alone gives no contradiction with finite total dissipation, and no argument controlling the number, disjointness
or cumulative cost of such windows has been established.

Why the small-variation bound for the adjoint required in Theorem 8(b) is not available (all checked here). (i) There is no total-variation contraction: f = d_Z psi_n solves
f_s = U^R f_R + d_Z(U^Z f) + nu L f + (d_Z U^R) d_R psi_n, and the last term creates axial variation from radial variation, already in the exact
leading near-axis model U^R = -(1/2) b_Z(Z, tau) R, U^Z = b(Z, tau). (ii) The near-axis variation T_rho = int_{R < rho} |d_Z psi_n| dy has, besides the
flux through R = rho, the interior source |d_Z U^R| |d_R psi_n|. (iii) The axis does not shield the crossover radius: for the radial operator
nu (d_RR - R^{-1} d_R) + A R d_R the harmonic profile is (1 - e^{-A R^2/(2 nu)})/(1 - e^{-A rho^2/(2 nu)}) for A != 0 and R^2/rho^2 for A = 0, and an outward strain A of order
nu/delta^2 = (C_*/G)^{2/3} nu^{1/3} already removes the factor delta^2/rho^2; a compressive strain gives an exponentially small factor only if it extends over radii much
larger than (nu/|A|)^{1/2}; the Lipschitz bound |a(R, Z) - a(0, Z)| <= C_* R guarantees a compression of size |A|/2 out to radius |A|/(2 C_*)
but gives no upper bound on its radial extent, and nothing in the bounds forces either an outward or a compressive strain. (iv) The heuristic that the
Hessian bound limits the stretching near a swirl core to (C_*/G)^{2/3} nu^{1/3} is true for a stationary Burgers core whose circulation is comparable to G nu (a weaker core allows a larger strain, since the swirl Hessian of a Burgers core of circulation Gamma_c and strain A is of order Gamma_c (A/nu)^{3/2}), but it does not follow from the circulation bound alone and it is false in general for time-dependent cores:
an order-one strain pulse of unit duration on a wide circulation-saturated core is compatible with the pointwise bounds up to fixed factors (kinematically: a cut-off uniform axial stretching of rate at most 1/4 for unit time contracts the core radius by at most the factor e^{-1/8} and so multiplies the Hessian of the swirl velocity by at most e^{3/8}; this checks the bounds, it is not a coupled Navier-Stokes example). (v) The material and residence-time reformulations of the production considered here (flux of q^2 through material surfaces, the time the fluid ending in supp phi spends near the axis) led, in the forms examined, back to the same requirement and gave no additional upper bound on the signed production (a report on these attempts, not a proved equivalence). (vi) A restricted straight-channel estimate (proved). Fix
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
(vii) A local modulation example and an averaged strain constraint (proved). In units of length delta and time 1/(C_* delta) (1/G of the cell time of the Round 2 items; the viscosity is 1/G in these units), with z of period 2 pi, let chi be a smooth radial cutoff equal to 1 for r <= 1
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
{R >= R_B} with 0 < R_B <= 1, and put M_phi = sup_R int |d_Z phi(R, Z)| dZ. Then for every bounded smooth circulation gamma on the window (in units of nu_n: R U^theta_n = nu_n gamma and q_n = nu_n gamma/R^2)
that vanishes on the axis, solves the circulation equation d_tau gamma + v d_Z gamma = nu_n (gamma_RR - R^{-1} gamma_R + gamma_ZZ) and
satisfies |gamma| <= G (a freely prescribed bounded function is not covered), the production of the window, P_win = int_0^{K/nu_n} int q_n^2(y, -s) d_Z psi_n(y, -s) dy ds (the window's contribution to the pairing of Theorem 8 (b); its negative is the window part of the production P_n), satisfies |P_win| <= pi M_phi G^2 nu_n R_B^{-2} (1 + (1/2) log(2K)). Proof: since v does not
depend on Z, d_Z psi_n solves the adjoint equation, so |d_Z psi_n| is at most the solution with data |d_Z phi|, whose axial integral
H(R, s) solves H_s = nu_n (H_RR - R^{-1} H_R) with zero axis value; since 1 and R^2 are stationary supersolutions,
int |d_Z psi_n(R, Z, -s)| dZ <= M_phi min(1, R^2/R_B^2) <= M_phi R_B^{-2} min(1, R^2) at every age. Without radial velocity,
G (1 - exp(-R^2/(4 nu_n t))), t the time elapsed since the start of the window, is an exact Z-independent solution of the circulation
equation, and |gamma| <= G (1 - exp(-R^2/(4 nu_n t))) by the killed-diffusion representation: since v does not depend on Z, the radial
component of the diffusion generated by nu_n (d_RR - R^{-1} d_R + d_ZZ) - v d_Z is a Bessel process of dimension 0 run at speed 2 nu_n,
absorbed at the axis, where gamma vanishes, so gamma at time t is the expectation of its value at the start of the window on the event
that the axis has not been hit, and that event has probability 1 - exp(-R^2/(4 nu_n t)) (no uniform initial bound O(R^2) is needed). Insert both bounds in |P_win| <= int int nu_n^2 gamma^2 R^{-4}
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
V_nu question of Open (5) that assumes only the four pointwise velocity bounds and a fixed smooth terminal function; it does not address
the question for the actual Case 2 adjoints. Fix C = C_* > 0 and
G > 0 as upper-bound parameters, put mu = C/G and nu = mu delta^3, so that r_c = delta/2^{1/2} and w_nu are those of Theorem 8(b).
Admissible fields are prescribed smooth, axisymmetric, swirl-free and divergence-free fields on R^3 with the Cartesian bounds |U| <= 1,
|grad U| <= 1, |grad^2 U| <= C for all times and d_t U bounded (for the fields below d_t U -> 0 uniformly, so any fixed cap such as that of
Theorem 1(b) holds for small delta). This is a kinematic class: no pressure equation, normalized gradient record or positive limiting-vorticity
packet is imposed. The adjoint is psi_s = U(., -s).grad psi + nu L_ad psi (L_ad = d_RR - R^{-1} d_R + d_ZZ, the operator L of Theorems 3 and 8; L below is a length constant), psi(., 0) = phi, the bounded solution vanishing on the axis;
equivalently psi(x, s) is the expectation of phi at physical time 0 for the diffusion started at x at physical time -s, with time-dependent
generator U(., -s + u).grad + nu L_ad and absorption at the axis. V_nu(s) = int_0^infty w_nu(R) int |d_Z psi(R, Z, s)| dZ dR. Claim: there are K in (0, 1) and c > 0
depending only on C and G, a terminal function phi = Phi(R^2) xi(Z) in C_c^infinity independent of delta with 0 <= phi <= 1, supported in
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
and the occupation density of the uncut autonomous axial comparison process, G_occ(x, y) <= 2 d_delta(y)/b, applied to the radial estimates
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
For a positive C^2 transition speed B on a finite interval, from the jet speed to a pool speed nu b_p, put f = nu/B, T = int f dZ and
E = int (f')^2/f dZ, both integrals over that interval; then E T >= (f(end) - f(start))^2 (Cauchy-Schwarz). For fixed lambda and fixed b_p > 0 the endpoint values tend to 0 and 1/b_p, so T -> 0
forces E -> infinity. For the profile B = nu b_p + (lambda delta - nu b_p) e^{-1/(Z_c - Z)} on a fixed interval Z_c - d_0 < Z < Z_c
next to the pool, the contribution E_near of that interval to E satisfies E_near = (log a_delta)^2/(2 b_p) + O(log a_delta) = (2/b_p)
log^2(1/delta) + O(log(1/delta)), a_delta = (lambda delta - nu b_p)/(nu b_p); the full E is at least E_near, and the rest of the transition,
which is not specified, can contribute more. Suppose
further that B is nonincreasing on the transition interval [Z_e, Z_c], constant upstream of Z_e, and equal to nu b_p on [Z_c, Z_c + l_p],
l_p > 0. Let the axial comparison process dZ_tau = f(Z_tau)^{-1} dtau + 2^{1/2} dW^Z_tau start at Z_0 <= Z_e, stop at its first hitting
time tau_p of Z_c + l_p, and be continued independently of radial absorption, and put M_f(t) = -2^{1/2} int_0^{min(t, tau_p)}
1_[Z_e, Z_c](Z_tau) (f'/f)(Z_tau) dW^Z_tau. Before radial absorption M_f is the transition part of the axial martingale term of
log(X/f(Z)) (in the construction above f = d_delta/b on the transition, so X/f(Z) = b Q there). Its expected quadratic variation up to
tau_p is at least 2 (1 - e^{-b_p l_p}) E, since the occupation density of the stopped process at every y in [Z_e, Z_c] is at least
f(y) (1 - e^{-b_p l_p}) (f is nondecreasing and f <= 1/b_p). These facts obstruct the small-distortion argument used here; they
do not exclude a nonperturbative transmission mechanism or a window beginning at ages o(1/nu). Scope. U^delta and grad U^delta tend to 0
uniformly, so the family is not a model of the nonconstant Euler limit, it has no normalized gradient record, and phi is not a packet on
which a limiting vorticity is positive as in Theorem 3; it carries no swirl and no production (q = 0), and it is not a Navier-Stokes solution
(G is an upper-bound parameter here, not the circulation norm of a datum). A proof of the small V_nu bound for the actual Case 2 adjoints
must use information beyond the four pointwise velocity bounds and a fixed smooth terminal function, for example their
coupled evolution or the structure of the limiting-vorticity packet. A proof that estimates the signed production directly could instead
use cancellations discarded by V_nu. An attempted extension with swirl in this geometry (a source pool for the circulation
upstream of the jet and ordered cos and sin strain pulses on it) gives a positive quadratic jet-production coefficient in an inviscid
single-pass model with a suitably chosen compact terminal ring (algebra and sign checked, Section 5 (19)). This reduced-model algebra
does not give a viscous family: its extension needs an unproved representation with uniform weighted mixed derivative estimates, control of
the signed contribution of the rest of the history and the full velocity bounds for the swirl, and it is not established for the particular
terminal function used above. A further coupling restriction is precise: for any meridional velocity and any smooth axisymmetric test function phi supported off the axis,
int eta phi dy = 2 pi int (U^Z d_R phi - U^R d_Z phi) dR dZ (from eta = (d_Z U^R - d_R U^Z)/R and integration by parts), so a family whose
meridional velocity tends uniformly to 0 near the support of phi cannot have a nonzero limiting pairing of its own eta with phi. No positive
full-history viscous pairing or coupled realization is established by this attempt.
(xi) A formal scenario study (conditional scale balances, not a construction). Put eps = T_* - t and assign
M ~ eps^{-2/3}, D ~ eps^{-5/4}, H ~ D^2/M (the persistent scalar history, (a, b) = (5/4, 2/3), of the paragraph on the time geometry of records above), nu = D/M^2, l = M/D,
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
would still have to be handled. The scale count does not determine the sign of the pairing of Theorem 3(b). Two exact facts hold. First, at a
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
of Theorem 8(b) or the old-age bound of Theorem 6). On growing windows 0 <= s <= Lambda_n/nu_n a sufficient condition for the contribution of the
window to vanish is Lambda_n nu_n^{1/3} Vbar_n -> 0, Vbar_n the average of V_nu over that window, and the older history must again be
controlled. By Section 4 (x) and Appendix A, the
four pointwise velocity bounds do not suffice for all fixed smooth terminal data: for one fixed smooth nonnegative terminal function the construction has V_nu >= c/delta
on a fixed fraction of each fixed larger window. The construction has zero limiting velocity and its terminal function does not satisfy the positive limiting-vorticity condition of Theorem 3; a proof of the small V_nu criterion for Case 2 must therefore use additional information. For the signed production itself no admissible kinematic family with a fixed terminal packet and an order-one positive lower bound over the required full history is constructed here or known to us; cancellation may permit
a production estimate even where the V_nu criterion fails, and whether such an estimate requires the coupled dynamics remains open.
The local modulation example of Section 4 (vii) shows that, with prepared radial endpoint data, the local order of Theorem 8(b) occurs
during one modulation time; supplying those profiles, linking the adjoint to the fixed terminal packet, renewing the mechanism and
controlling signed contributions of the rest of the history are not achieved by it, and it does not show that every proof must address
renewal in this form. (6) A bound nu_n int_0^{t_n} (Pi_s)_+ dt -> 0 for the self-compression of Theorem 9(d), or the unweighted signed bound limsup nu_n int_0^{t_n} Pi_s dt < 2 m_phi/(3P), equivalently limsup nu_n (Sigma(t_n) + int_0^{t_n} D_Sigma dt) < 2 m_phi/P (R2.16), or the weighted signed bound
limsup nu_n int_0^{t_n} e^{3 C_0 (t_n - t)} Pi_s(t) dt < 2 m_phi/(3P) of the same theorem (equivalent to the unweighted one, R2.16), or an upper bound Act(t_n) <= (1/3 - epsilon)
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
at z and z + p gives - p d_z Q_1 = 0, so no z-dependent steady periodic swirl perturbation about this single affine Burgers column exists; and a steady profile Q_1 = w(r) cos(k z), with fixed k != 0 and a fixed nonzero radial profile w, across a column of axial span delta^{-1}
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
swirl of Appendices B and C does not meet the requirement: if Gamma is smooth, localized, time-independent, vanishes on the axis and is not identically zero
(replaced by - Gamma if necessary, so that it has a positive maximum), then for any smooth incompressible B, possibly time-dependent, a
compact regular superlevel set {Gamma > c}, c > 0, has int_{Gamma > c} B.grad Gamma dx = 0, while nu int_{Gamma > c} L Gamma dx is - nu
times the integral of |grad Gamma| over its boundary, which is negative (L Gamma = Delta_3 Gamma - 2 Gamma_R/R, and the last term integrates
to zero over each radial interval of the superlevel set, at whose ends Gamma = c).
In Case 2 the field not sourced by the swirl has small radial strain: a_r = O(1/D_n) in the rescaled frame, which is o(kappa_n) for
the cell rate kappa_n = nu_n/delta^2 (by the lower bound D_n^3/M_n^5 >= pi/(768 E_0) of Section 1, nu_n >= c D_n^{-1/5} and
D_n kappa_n >= c D_n^{14/15}), and its integrated action is bounded (over a window of record length 1/nu_n it is at most a constant times D_n^{-4/5}). Under
this restriction the following conditional persistence obstruction holds. In the drift-free model started from eta_s(0) = 0, with
whole-space Biot-Savart recovery and the normalization q = alpha C delta Q of Appendix B, write Q^2 = F_0 + F_1 in cell coordinates, with
F_0 independent of z and |F_1| <= E_env(r), where the radial lift of E_env lies in L^1 and L^infinity of R^4 uniformly in the family. Then ||a_s||_infinity <= alpha^2 G^2 K_env kappa with K_env = (||E_env||_infinity ||E_env||_{L^1(R^4)})^{1/2}/(2 pi), uniformly in time and without
periodicity. If q > 0 along an axial characteristic, Delta_5 q/q <= - sigma/delta^2 there and q(T)/q(0) >= c_*, with sigma > 0 and c_* > 0
independent of delta, the swirl equation gives int_0^T (- a_e) d tau >= (sigma/2 - alpha^2 G^2 K_env) kappa T + (1/2) log c_*;
if sigma/2 - alpha^2 G^2 K_env >= epsilon > 0 uniformly in the family, then at the record time T = 1/nu (where kappa T = delta^{-2}) the external
compression action is at least epsilon delta^{-2} + (1/2) log c_*, contradicting the Case 2 action bound for sufficiently small delta (the
inequality is one-sided; no matching upper bound is asserted). A stationary core Gamma = A (1 - e^{-gamma R^2/(4 delta^2)}) with fixed
A != 0 and fixed gamma > 0 needs a = - gamma kappa/2 wherever that profile holds on a spatial neighborhood, so a_e = - gamma kappa/2 at a genuine
initial time with zero sourced vorticity and whole-space Biot-Savart recovery. These statements are separate. The exact steady swirl of
Appendices B and C, which vanishes on the axis, is excluded by the superlevel argument, not by the characteristic estimate, which applies
only to cores satisfying its curvature, persistence and sourced-strain hypotheses. The drift-free heat estimate does not give the
sourced-strain bound for transported histories, evolving cores outside this class remain undecided, and vorticity sourced before an
observation window must be kept in the sourced field.
The question for the coupled evolution remains open. Conditional on the formal identity of F10 (d) holding along the solution, a further sufficient condition is an estimate 3 (C + T) <= epsilon (D_q + 3 D_psi) + e with epsilon < 1 and
int_0^{t_n} e = o(nu_n^{-2}) for the remainder of the coupled critical balance (the order nu_n^{-2} comes from F(t_n) >= c nu_n^{-2}); its cubic
part T admits no instantaneous bound T <= epsilon D_psi over arbitrary amplitudes, and the identity itself is formal (F10 (d)).

How to resume. Items (1), (2), (3) and the bounds on the self-compression and on the compression action in (6) are sufficient
conditions for excluding Case 2; the estimate of F10 (d) in (6) is sufficient provided its formal identity holds along the solution; (5) is sufficient together with control of the older
history; (4) is a structural question whose positive answer would not by itself exclude Case 2. Apart from the equivalence of the signed forms of the self-compression bound in (6) (R2.16), no equivalence between these conditions is asserted. The model results indicate where further information must enter: the four pointwise velocity bounds do not give the small V_nu
criterion of (5) for all fixed smooth terminal data (Appendix A), and the three spatial velocity bounds and the circulation bound alone do not give the first bound of (6) when the swirl is
prescribed, with or without transport of eta_s (Appendices B and C). These model families have zero limiting velocity and no
normalized gradient record; they are not Case 2 Navier-Stokes histories. The next step suggested by these results is an upper bound for the
signed self-compression of Theorem 9(d) along histories in which the swirl obeys its own equation, or a coupled model family showing
that such a bound fails in which the swirl evolves without forcing, both transported equations use the same total velocity, the sourced
field contains all vorticity generated since the initial time, the remaining part eta_r of the vorticity solves the homogeneous transported equation and its Biot-Savart velocity has a_r = O(1/D_n) in the rescaled frame and bounded integrated action, and every reservoir and boundary flux is stated. For comparison, in Appendix C the self-compression pays at most a share of the swirl dissipation bounded by a constant multiple of alpha^2 G^2, and the residual of the swirl equation pays the rest (C.11), whereas along a Case 2 history the self-compression pays, up to o(1) in the normalization of R2.18 (a), all of the normalized swirl dissipation and the final storage. An
unrestricted external field does not test this decomposition: for a prescribed swirl history admitting an admissible smooth inverse B it can
be chosen as B - b_s (Open (6)). The persistence obstruction under the inherited bounds applies only to the class specified in Open (6); it
does not exclude arbitrary evolving cores.

## 5. Verification

How the results were checked. The arguments of Sections 1 to 3 were derived or rederived by hand. The printed proofs and derivations (Section 2, the Round 2 items and Appendices A to C), together with the explicitly cited theorems under
their stated hypotheses, are the mathematical evidence; routine steps are stated concisely rather than
written out in full. Symbolic checks test algebraic identities; quadrature and discretized calculations test selected examples and do not
prove PDE estimates. Exploratory cell simulations were in general not independently reproduced; where a numerical quantity was reproduced or recomputed, the item concerned says so. Unverified citation locations and conditional model
constructions are identified where they occur.

Second-model contributions and adversarial review. Statements were tested by a second model (a language model) instructed to find errors. Its answers were
treated as claims and are not proof dependencies. Returned arguments and objections were checked against the printed derivations and
selected symbolic and numerical calculations.
Several arguments first appeared in its answers and were then checked by hand: the production identity of Theorem 3 and the proof of Theorem
3(g); the truncated-energy proof of Theorem 5(b); the weighted adjoint energy of Theorem 6(b) and Proposition 7; the compression memory and
axis barrier of Theorem 8(c), (d), the weighted envelope form of Theorem 8(b) and the (J, eta) identity; the negative findings (i) to (iv)
and the items (vi) to (xi) of Section 4, including Appendix A; most cell-scale statements of F9; the memory profile of F10 (c), Appendices B
and C, the single-column example and the inverse-design and persistence statements in Open (6); the balance of F10 (d); and the
barrier proof of Corollary (iii) (Section 2.7d). Separate adversarial audits by the second model examined the numbered results, the findings, each appendix and finally the whole manuscript, each
within a stated scope. Within their stated scopes and the versions examined, they reported no false statement among the numbered results (Theorems 1, 2, 3, 5,
6, 8 and 9, Propositions 4 and 7 and Corollaries (i) to (vi)) and no fatal error; a gap of proof in the last assertion of Theorem 6 (d),
found in the second round and repaired, is described in (26). The auxiliary errors and gaps of proof, scope and wording that they identified are
corrected at the affected statements, where the remaining limitations are stated; examples are a comparison factor in a remark on Theorem 6,
the fixed-z integration by parts formula of F1, a reversed inference in Section 4 (iii) and the leading coefficient of the near-pool part of the distortion action
in Section 4 (x). The whole-manuscript audit that ended the first round (of the version then examined, which excluded the paragraph on swirl records in Section 4, audited separately) found
only two wording problems, the notation for the rescaled pressure in Theorem 1(b) and the missing uniformity of epsilon in the action bound
of Open (6), both corrected, and a narrow audit of the repairs found no error. Gaps closed by adding proofs include Theorem 1(a) (Section
2.2), the deduction of the two compression bounds of Proposition 7 (Section 2.7b), the kernel estimate of Theorem 9(d) (Section 2.9), the
variable-in-time barrier of Corollary (iii), Corollary (iv), the last assertion of Theorem 6(d) (by the penalization argument of (26)) and Proposition 4(b); the identity of F10
(d) is stated as formal. These reviews are not a single independent reconstruction of every assertion, and agreement between model runs is
not a proof or a formal verification.

Individual checks (calculation; method; result; limitation).
(1) 5D lift, adjoint transformation, radial integral constants, bathtub value, radial integration by parts formula, Casimir source
cancellation; exact symbolic computation, and high-precision numerical evaluation at sample inputs where the symbolic simplification
did not close (these instances check the identity only at the inputs tested); all confirmed; these check identities, not the estimates
built on them.
(2) Theorem 9(a) and the adjoint-weighted identity behind Theorem 9(c); high-precision numerical quadrature on explicit smooth fields (prescribed q and
Psi, divergence-free poloidal field built from a streamfunction); the integrals agree to working precision while the integrands differ
pointwise; the weight used changes sign, so this checks the identity and not the inequality, which uses Psi_n >= 0. The identity of
Theorem 9(a) was also compared by hand with Shahmurov's balance (3.9) with the parameter q of that balance equal to 2 (not the
swirl variable q of this report).
(3) Kernel bound of Section 2.9; symbolic computation for Delta_3(x_1 g) = x_1 Delta_5 g and for |S^4| = 8 pi^2/3, high-precision numerical quadrature for the S^3 and S^1
averages, and a brute-force comparison of the five-dimensional majorant with the three-dimensional bound at sample points; all agree;
these are sample checks accompanying the analytic proof of Section 2.9, not general proofs.
(4) Constants of Theorem 8 (pi e (cosh(1)/6)^{1/2} < 4.4, the barrier coefficient k = 1/(2 nu (1 - e^{-2h})) of Section 2.7c (nu k = 1.2707... at h = 1/4), the supersolutions of the Riccati inequalities (checked by substitution), the (J, eta) cancellation), the
constants of Theorem 6 and Proposition 7 (the restriction alpha < 3/2 and the constants 1/16 of the two compression bounds at the end of Section 2.7b) and the constants of Theorem 9(b) to (d); by hand,
and confirmed in audits.
(5) Memory profile of F10 (c); closed form against high-precision numerical quadrature (difference about 1.4e-15), steady response and positivity of the
energy-weighted work symbolically; confirmed; the localization at the saturation scale is proved in Appendix B (see (21)), and its
transported version, with q still prescribed, in Appendix C (see (22)); the coupled evolution remains open.
(6) Balance of F10 (d); variational derivative of F, source term I + C and diffusion term by hand, the two forms of D_psi and the
variational derivative compared numerically on two explicit fields (numerical quadrature, agreement about 1e-13 relative); confirmed as a
formal identity; the axis behaviour of h and chi_1 was checked only to leading order and the boundary terms were not verified. The bound
K_b <= 68 F and F(t_n) >= (c_B/68) nu_n^{-2} (1 - o(1)) were derived by hand.
(7) The value T[psi_*] in F10 (d); an independent second-order finite-volume solve of - Delta_5 u = b.grad(eta), for which T = - pi^{-1} int (eta/r + psi_r/r^2) u dX by the symmetry of
A = - Delta_5 (grid sizes 0.1, 0.05,
0.025 give -6.5e-4, 4.58e-4, 7.335e-4, Richardson value 8.25e-4, in agreement with the closed form; the coarsest grid has the wrong sign);
agreement of the closed form with the representation (3 pi^2/2) int_0^1 x^6 (4 x^6 - 36 x^4 + 11 x^2 + 5)(1 + 2 x^2)^{-6} dx to 30 digits;
and an exact rational sign certificate: arctan sqrt2 = pi/4 + arctan(3 - 2 sqrt2), 1.41421 < sqrt2 < 1.41422, pi < 355/113 and
arctan v <= v - v^3/3 + v^5/5 for 0 < v < 1 bound the bracket 35299/82944 - (645 sqrt2/2048) arctan sqrt2 below by 7.8e-5 > 1/14000.
The closed form, first supplied by the second model, was derived independently by exact symbolic computation: A^{-1} = int_0^infty e^{t Delta_5} dt;
with f = - b.grad(eta) = - z (28 + (16 s - 80) z^2) e^{-2s}, s = r^2 + z^2, and d = 1 + 8t, the explicit Gaussian expression for e^{t Delta_5} f
(a polynomial in r, z, d^{-1} times d^{-5/2} e^{-2s/d}) is checked to solve the heat equation in R^5 with initial value f; the pairing
pi^{-1} <eta/r + psi_r/r^2, e^{t Delta_5} f>_{dX} equals J(d) = 6 pi^2 (5 d^3 + 11 d^2 - 36 d + 4)/(d^{3/2} (d + 2)^6) by exact Gaussian moments;
T = (1/8) int_1^infty J(d) dd becomes the integral above under x = d^{-1/2}; and an exact antiderivative gives the closed form.
D_psi[psi_*] = 15 pi^2/8 was obtained by the same moments.
(8) F9; the irrotational example of (e), the survival law of the time-changed Bessel-0 process, the landing constant, the cap integral and the
production bound of (f), the comparison subsolution and corrector expansion of (g) (by symbolic computation), the closed-cell energy identity, flux
identity, slope count and weighted moment identity of (h) (the last also numerically on explicit fields; the divergence-free sign
statements were checked by hand and the explicit example, its energy, moment, impulse and swirl source by exact symbolic computation), and the derivative scalings,
scale density, hitting-probability bounds and symmetry cancellation of (i); by hand unless stated; confirmed under the hypotheses
stated; not checked: the Poincare constants of (h) and the parabolic
third-derivative estimate of (f) beyond the level of the argument. The coupled decay estimate considered in "Core supply" (E' <= -(2A - C_cpl) E
with C_cpl < 2A controlled by the Case 2 assumptions) is not proved, as stated there.
(9) Exponent bookkeeping of the scalar diagnostic in Section 4, by exact arithmetic; it concerns scalar inequalities only. The record
dichotomy, the occupation bound and the band bound of the time-geometry paragraph were checked by hand, the exponents and band limits of the
two scalar histories by exact symbolic computation. The fields, trajectories, Jacobian and pipe-flow identities of the material-properties paragraph were
checked by exact symbolic computation, the cutoff bounds of (a) by hand.
(10) The numerical cell and fold computations quoted in F9 (d), (f), (h), (i) were performed by the second model and not rerun; no
conclusion of this report depends on them.
(11) The axis evolution of E and its reduction in the Hou-Li exact class (F10, literature paragraph): exact symbolic computation with truncated
even expansions in r and d_z u^z = - 2 a on the axis; it checks the identity only. The off-axis equations for (d_z q, d_z a) and the value
d_t E = 4 alpha r^2 k^2 for the polynomial core were checked by exact symbolic computation, the complex form of the (q, a) equations and the cutoff
construction by hand.
(12) Geometric criteria of F5: the rotation and distance identities, the energy constant pi/768, the three scale identities and both length
exponents were checked symbolically. This checks algebra only; the hand arguments carry the qualifications stated in F5.
(13) The three forms at the end of F4: the conservative form of the omega^theta equation, the axis flux 2 eta(0, z), the swirl source and
the xi-form of source, transport and swirl energy density were checked by exact symbolic computation, the vertical-line identity numerically. The label
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
R^2/2)); the radial integrals 1/2 + (1/4) log(2K) (K >= 1/2) and (for r_c <= 1) r_c^2 (3/4 + log(1/r_c)) were checked by high-precision numerical quadrature
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
numerical constants (exp(2/5) comparisons, log(4/3) > 1/4, the coefficient sums) were checked by symbolic computation and high-precision numerical evaluation. Two adversarial audits
by the second model rederived the arguments. The first found an error that the hand check had missed (the leading coefficient of
log^2(1/delta) in the near-pool contribution E_near to the distortion action of the exponential profile is 2/b_p, not 1/(2 b_p), since log a_delta = 2 log(1/delta) + O(1)) and
asked for the specified step profile, the stopping conventions, the restriction of the scope to the prescribed-field class and a lower-bound
reading of the order nu^{-1/3}; the second found no mathematical error and corrected one sentence after (A64) that understated (A63). All of
these are incorporated. The cited textbook editions were not inspected in these audits. For a separate, incomplete attempt to add swirl to the kinematic construction, the check is limited to the
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
(B56). Checked by symbolic computation and high-precision numerical evaluation: the factorization h = g p of (B3), the three Gaussian integrals (B6) and the value I = -0.174019...,
the rational bound (B7), the kernels (B10)-(B12), the transverse and axial integrals of (B13) and (B21), the intertwining identity (B28),
the divergence and azimuthal vorticity of the field (B22) for a concrete potential, the powers in (B34), (B36), (B51) and (B54), the maximum
of g, the heat-kernel integrals in (B44) and (B46), and the cutoff integrals of (B9). An adversarial audit by the second model rederived
(B2)-(B55) with its own symbolic and numerical checks and found no error in the construction; its corrections (the radius in the
introductory definition of b_s, R eta_s e_theta in record coordinates; the description of the limit as the zero Euler solution; the scope
wording, the three spatial velocity bounds rather than every estimate of Theorem 1(b)) are included, and it supplied (B56). Appendix B is
cited in Section 1, in the discussion after Theorem 9 (e), for the model statement that the three spatial velocity bounds and the circulation bound do not imply nu int (Pi_s)_+ dt -> 0; that statement rests on it, but no numbered result of Section 1, in particular none of Theorem 9 (a) to (e), depends on it. The two limitations stated after F10 (c) were supplied
by the second model; the logarithmic example there was rederived by hand and its heat formulas and constant checked by symbolic computation.
(22) Appendix C (the transported family with prescribed q; the coupled evolution remains open) was derived by the second model in two
answers (the periodic transported theory, the modulated approximation, its residual and its work; then the delta-uniform estimate for the
exact error in the velocity formulation) and written in report form here with three changes: the envelope (C7) is the weighted sum of the
axial suprema of single entries (the axial supremum of the weighted sum of entries, used in the answer, also satisfies (C34) with constant
one), the identification of the fixed point with the transported solution is the argument of C.9, and the work bound does not use the
drift-free solution. Checked by hand: the cell form and the work identity (C5)-(C6), the periodic contraction, stability and scaling
(C8)-(C17), the derivative bounds (C18), the decomposition (C20) and the residual identity (C22) with its signs, the averaging bound (C25)
and the work of the approximation (C26), the velocity identities (C27)-(C30), the kernel bounds (C31)-(C33), the residual response
(C35)-(C38) with its counts, the bilinear and linear estimates (C39)-(C42), and the contraction, the constants and the work budget
(C43)-(C49). Checked by symbolic computation and high-precision numerical evaluation: the kernel norm formula of (C33), the optimization in (C36), the Gaussian maxima of (C37), the
time integrals (C38), the counts and margins of (C35) and the integrals in N_P, the splitting constant 8 of (C39), the conversion
inequalities in delta and ell, the contraction budget of (C43), the work scaling (C6) and the budget of (C48). The constants C_O, A_b, C_R
and C_a are finite suprema that were not evaluated numerically. An adversarial audit by the second model of Appendix C (cell form and work;
periodic theory and approximation; velocity equation and residual; kernel and envelope inequality; residual response; bilinear and linear
estimates; fixed point and identification; constants, pointwise bounds and work) rederived the identities of (C5)-(C30) by symbolic computation, gave
elementary proofs of the time inequalities (C38), checked the 39 entry counts, and found no fatal error and no gap in the proof of (C3); its
wording corrections are included, and a narrow audit of the corrected lines confirmed the upper bound W_s/nu <= 2 pi alpha^4 C G^3 A_F M_b
at the end of C.10. Both Appendices B and C prescribe q, have velocity and gradient tending uniformly to zero and no normalized gradient
record, and do not solve the coupled Navier-Stokes system.
(23) The single-column example and the averaged circulation identity in Open (6) were derived by the second model. Checked here by exact symbolic computation: that Q_B solves the steady swirl equation T Q_B = 0, the formula for D_B, the first-variation identity (the O(eps) part of the
steady swirl residual is - T Q_1 + D_B v_1^r), the Gaussian moments int r^2 e_a e_b dr, int r^2 e_a L_0 e_b dr, int r^2 e_a L_0^2 e_b dr
(e_a = e^{-a r^2}), the moment formula for J, the closed form of J and the rational sign certificate (sqrt2 < 10/7, 498003/102400 < 49/10,
sqrt101 > 10 and 2513093451/3329932832 > 3/4 give J/pi < 7 - 15/2 = -1/2), and the derivative identity behind the averaged circulation
identity; J also by direct symbolic double integration of r^2 f (- d_zz V), compared in floating point (J = -2.2207). Checked by hand: the
drift-free response a = - eps d_zz V and the vanishing of its pairing with Q_B^2, the periodicity obstruction, the averaging argument for
the resupply statement, the scaling to order delta nu and the amplitude restriction eps = O(delta).
(24) The inverse-design reduction, the superlevel obstruction for the swirl of Appendices B and C and the persistence bound in Open (6) were
derived by the second model, in answer to a request to check a reduction proposed here, which it corrected (the aggregate superlevel
condition is necessary but not sufficient, and a saddle with S = 0 can obstruct). Checked here: the identities Gamma_t + b.grad Gamma =
nu L Gamma and b.grad Gamma = {psi, Gamma}/R, and the deficit rate int_0^infinity (L Gamma_B) R dR = - 2 Gamma_infinity for the Burgers profile, by symbolic computation; the superlevel argument, the Taylor-coefficient obstruction at a saddle and the envelope bound by hand, with
int_0^infinity min(M, N/u^2) du = 2 (M N)^{1/2} by symbolic computation and ||d_zz G_u||_1 = (2/(pi e))^{1/2}/u <= 1/u for the one-dimensional heat kernel G_u (coefficient
approximately 0.483941), by hand and by quadrature; the characteristic inequality by hand and the Burgers axis strain
a = - gamma kappa/2 - A'/(2A) by symbolic computation; the exponent count D_n kappa_n >= c D_n^{14/15}. The symbolic checks supplied by the second model were rerun here and passed. A narrow audit of the
first version of this text by the second model found that it overstated the scope of the persistence bound (applying it to the swirl q of
Appendices B and C, which vanishes on the axis, and to all coupled families) and omitted the periodicity, sign and transport qualifications;
these were checked and corrected.
(25) The tail computation for swirl records near the limiting packet in Section 4 (Use of the branch hypotheses) was derived by the second
model, in answer to a request for new mechanisms outside the failed approaches; it found no new route. Its derivation already used
terminal-inclusive convergence to obtain the off-axis packet; the uniform lower bound for all d_n > 0 extends its crossover and
intermediate-radius estimates. Checked here: the change of variables and the case split by hand; the values of d/b^2 at the crossover and at
intermediate radii and the crossing of the caps b <= min(2 C_* delta_n d, G nu_n/d) at d = delta_n/2^{1/2} with value 2^{1/2} C_* delta_n^2,
by symbolic computation; the 26 exact symbolic checks supplied by the second model were rerun here and passed. A narrow audit of the first version of this text by the second
model found that it did not restrict the swirl record times to s_n <= t_n, where the caps of F9 in the units of t_n apply, stated the packet
condition loosely and overstated the limitation to earlier times; that audit also verified seven exact algebraic identities. These points
were checked here and corrected; a second narrow audit of the corrected text found no error.

(26) Round 2 (the Round 2 brief and the items R2.1 to R2.18). The round-2 arguments were derived or rederived here, except analytic results taken from a separate computation (in R2.14: the modal matrix-element formula, the mean-energy formula (N-C), whose channel sum was checked algebraically, and the weak-noise theorems quoted in (vii)), which are identified as such together with the checks made on them. Numerical results reported from separate computations are marked in the items as checked here (with what was rerun or recomputed), as model-level evidence not reproduced here (with any diagnostics recomputed here specified), or as not checked and not used as evidence. The items were then audited adversarially by the second model, each audit within a stated scope: R2.1 to R2.6; R2.7 to R2.11;
R2.12 in several successive versions, including its pumping claims; R2.13; R2.14 with its linear breathing derivation; R2.15; Theorem 9 together
with R2.16, followed by three audits of the rewritten R2.16; the free tuned-pair passage of R2.14 (d) and the question whether a strain-held core can be driven by a passive outer
structure; the count-level
comparison behind R2.17, and R2.17 itself; the consistency of the round-2 brief with R2.1 to R2.16; the literature on regularity criteria and
a priori bounds for the swirl functional and its dissipation; and finally a sectionwise audit of the status header, the brief and Section 1,
of R2.14, of R2.15 and R2.16, of R2.17, and of Section 4 with R2.18; and a second sectionwise pass: the consistency of R2.1 to R2.11 and
of R2.12 and R2.13 with the brief and R2.18, the status header with R2.18 and Sections 1 and 2 (statements and proofs), and Section 3.
The answers were treated as claims: each finding was checked here by
hand, and identities and numbers also symbolically or numerically, before any change was made; findings that could not be confirmed were not
applied and are not quoted. Most changes concerned wording, scope or a missing definition. The changes of substance were these: the axial
impulse of the sourced vorticity in R2.6 (b) is not zero, and that claim was withdrawn; the mean-field comparison conjectured in R2.11 (d) is
false (a counterexample is given there); the sign rule for the jet Reynolds stress in R2.12 is not universal (a counterexample is given
there); the comparisons in R2.13 concern the ratios W/P at the sampled quarter periods, which do not order W itself at different times, and the ordering of neighbouring sampled values is stated only for the first datum; a time-window error in one computation of R2.14
was found and the values were regenerated; the provenance count of R2.17 had applied an occupancy factor that the calibration already contained; after the correction the
ratio of need to supply falls like 1/G rather than 1/G^2, and the need does not exceed the source ceiling when G is above a number between about 3.5e6 and 1.6e8 (for an assumed pumped length per pair); the heading of
R2.16 claimed more than is proved and now names only necessary bounds and sufficient criteria; one step of the proof in Section 4 (viii), a
comparison that needed an initial bound not available there, was replaced by the killed-diffusion argument with the same conclusion; and
R2.18 no longer states that the pumping mechanism is necessary. In the second pass: the radius used in R2.5 violated the printed admissibility
inequality and is now 1.1434 delta; the profile of R2.2 needed a normalization factor to be admissible for C_* = 1 (the conclusion is
unchanged); the first-order flow of R2.11 (b) omitted a second harmonic, which does not change the result there or its counterexample;
the decay asserted in R2.7 (c) is now expected and not used; the duration-uniform obstruction of R2.12 (h) is proved only for the frozen
two-mode reduction, and two Orr gains in R2.12 were recomputed (35.8 and 73.7, previously 34.0 and 72.4); the proof of the last assertion
of Theorem 6 (d) had a gap (an unjustified restriction of the adjoint to the super level set) and was replaced by a penalization argument with
the same conclusion, which a further hostile check of each step (existence and axis behaviour of the killed adjoint, the bound uniform in the penalty, the zero set of the limit, the signs in the pairing, the limits) found complete; the Case 2 setting now states the record-time quantifiers explicitly; and in Section 3 the summary of Seregin's
conservation results lists their additional hypotheses, the lower bound in F10 is stated for the running supremum of the compression action,
as in Theorem 9, and the closed-cell paragraph of F9 (h) names the two quantities it controls; a check of these changes clipped the age band of F8 at the available history and fixed the exponent of Lambda_Q there. A last pass covered the additions to R2.14 (vii), R2.16 and R2.18 (c), (d): readings of the channel-separation runs that attributed the growth to particular resonances were replaced by descriptive statements, the pair-sum resonances were restored in (Q), a clause stating that the dissipation-only average of the action in R2.16 needs Sigma(t_n) = o(1/nu_n) was withdrawn (that average holds without it), the averaged and level-set forms of the action bound in R2.16 were found correct, and a stated upper bound on the weak-noise pair coefficients (1.5 per cent; the computed maximum is 1.55) and the description of a consistency check of their diagonal form were corrected; a check of these corrections as applied fixed one rounding (0.36, not 0.37, for the subharmonic coupling ratio of the fourth mode) and stated that the sub-band runs preserve the spectral density of the forcing, not of the unit-rms multitone; the damping-rate ratio of the second to the first mode, used there for a conditional threshold ratio and earlier taken unchecked from the separate computation, was measured here from the unforced decay of single-mode seeds (2.58 to 2.71). The pair coefficients were afterwards identified, against the mean-energy theorem of the separate computation, as coefficients of the mean first-mode energy rate (unbroadened leading coefficients at most about 0.77 per cent of its first-subharmonic coefficient; pairs without the first mode do not enter), not of the typical energy rate, and the frozen damping ratio (3.16) was stated beside the loss-accounting one. A heuristic weak-noise consistency estimate for the broadband runs was then added to R2.14 (vii); two checks of it confirmed its arithmetic and led to stating it as heuristic (the multiplication by the unforced decay of a non-modal seed as an unproved ansatz, no empirical break-even claimed, the endpoint horizons of the runs stated, the time-step claim restricted to the one run checked). Twelve-draw ensembles then compared endpoint geometric means with the estimate at G = 1000, 5000 and 20000, and the frozen-coefficient results of the separate computation (one-mode typical and mean rates; a Galerkin mean-rate theorem with an almost-sure upper bound) were recorded with their noise-class, gap and initial-data hypotheses and their exclusions. Later checks of R2.16 and R2.17 (e) as rewritten corrected the scope of the radial-velocity hypothesis in R2.17 (e) (the radial-velocity bound R U^R <= theta nu is imposed only on {R < R_*}), the list of inputs in the heading of R2.16 and the Oseen case of R2.10 (d), where the pointwise bound first used needed a bound on Gamma that the sign-changing extension does not supply and an L^2 bound replaces it; they also added the equivalence of the weighted and unweighted forms of the compression criterion in R2.16. A third, full-text pass then audited Sections 1 and 2 (statements and proofs), the proved parts of R2.1 to R2.15, and Sections 3, 4 and 5. Its changes of substance: Theorem 1 (b) is stated for all sufficiently large n, and Section 2.6 gives an explicit axial supersolution with its source and bathtub bounds; the strain of an axial packet in R2.1 has an additive remainder controlled by the absolute first moment about an axis point, with a relative form only for packets of one sign (the relative form fails, for instance, when the impulse vanishes); the synthesis sentence of R2.7 (i) wrongly counted the prescribed modulation of (g) among the examples of decay; the rearrangement inequality of R2.12 (i) on the infinite cylinder used equimeasurability, which is not enough there, and is now proved for rearrangements that also preserve the sublevel measures; the weight in R2.12 (g) must be radial; the zero-impulse centroid statement in R2.14 (d) was false (dI/dt = - a I - h J for w' = a + h z, so the centroid form holds only when I is not 0), and four numerical statements there that had been stated as exact are now stated as numerical; in Section 3 the pipe flows of F2, which show that the properties of the Euler limit listed in Theorem 1 imply no Liouville rigidity, lie in the limit class only under a condition on C_* (the Gaussian example needs C_* at least 2^{1/2} e, and such flows exist exactly when C_* > 1/2, by Landau's inequality and an explicit approximating family; F2 has since been extended by the floors 10^{1/2}/12 = 0.2635..., 0.2700... (divergence-free fields) and 7^{1/2}/8 = 0.3307... (swirl-free limits, sharp), the kinematic rings, the thin-ring range C_* > Q_core and the on-axis bound, item (27)), F8 no longer locates the compression of Proposition 7 in the age band, and the far-field bound of F9 carries the packet norm, the constant and the range of Theorem 8(a); in Section 4 a conversion between rescaled and physical dissipation in the limitations paragraph used the wrong normalization (its conclusion holds for the unweighted rescaled gradient integral), the harmonic profile of (iii) now covers A = 0, and in (x) the distortion action of the exponential profile is that of its part next to the pool, a lower bound for the whole transition; and the audit summaries in Section 5 and the accounts of literature checking in the Literature paragraph, F5 and R2.10 contained
several misstatements of constants, identities, the scope of claims or checking status. A fourth, full-text pass then audited R2.1 to R2.18 again. Its changes of substance: the second test state of the energy-Casimir model in R2.12 (g) took the circulation above the level at which the closed-form Casimir is defined, at radii inside the computational domain, and is now cut off radially (the computed derivatives with and without the cutoff agree to the six digits printed at 128, 256 and 512 radial points); the axis identity of R2.12 (i) had a wrong derivative term; the cumulative self-compression at a positive rate in R2.9 (c) (ii) is now conditional on certifying the sign of a numerically evaluated quadratic form; and an undefined comparison of energies in R2.6 (b) was removed. A fifth pass then audited every part of the report again, section by section (Appendix B by an independent hostile reading and through its uses in Appendix C), and found no fatal error. Its changes of substance: in the proof of Theorem 2 (Section 2.6) a quartic barrier replaces a quadratic one in the maximum principle for psi, whose a priori bound grows quadratically; in the proof of Theorem 3 (e) (Section 2.7) the deduction of the constant 49/8 is written out; in the proof of Theorem 9 (Section 2.9) the decomposition a = a_r + a_s is now justified (an L^2 energy estimate for the remainder vorticity and the vanishing of a harmonic field in L^6 + L^2), and a density remark extending the kernel bound is replaced by an explicit cutoff argument; the integrated balance of F10 (d) is stated as conditional on the identity holding along the solution; the compatibility test of Section 4 now keeps M H = C_* D^2 for every C_* (H = C_* eps^{-23/12}), and its agreement with Theorems 5 and 6 and Proposition 7 is restricted to their scalar size consequences; in Section 4 (iv) the statement that the Hessian bound limits the stretching near a swirl core is restricted to stationary Burgers cores whose circulation is comparable to G nu; the existence of the weak limit of u(t) as t -> T_*, used in R2.16, is now proved from the equation (finite energy alone gives only subsequential limits); in R2.1 (b) the proposed a priori bound for the Euler equations now requires the canonical pressure (without it the spatially uniform accelerating flow U = N t e_Z violates it); in R2.10 (c) the centrifugal exchange is taken relative to the reference column (the unsubtracted integral diverges on the Burgers background); in R2.15 (b) an unquantified clause on slowly varying forcing frequency is replaced by a proved bound; in the summary of the persistence criterion for swirl cores in the opening part the strain threshold now carries the factor D_n that converts the cell rate to physical units; in R2.12 (c) the Orr gain quoted for a wide datum is now that of the tilted datum exp(-(0.01 - i l_0) R^2) (about 46.7), the untilted datum exp(-0.01 R^2) having no gain; the remark of Section 4 (x) on a general transition speed is restated for the stopped axial comparison martingale M_f, which before radial absorption is the transition part of the axial martingale term of log(X/f(Z)), with the hypotheses that its occupation bound uses; and in F2 every use of the computer-assisted enclosures outside (iv) now either states that their programs are not reproduced or makes the numerical conclusion conditional on accepting the enclosures. Its other corrections concern displays, signs, quantifiers, parameter domains, checking status and the scope of statements (among them the fixed amplitude in R2.2, the almost-everywhere form of Proposition 4 (a), the attribution of proof strategies to the works compared in F6, the terminal function of Appendix A, which need not satisfy the positivity condition of a packet, and the report on attempted reformulations in Section 4 (v)). A sixth reading of every part, again section by section, found no error of substance; it made exact the descriptions in this paragraph of the enclosure qualifications and of the martingale of Section 4 (x), added the disclosure that the enclosure programs are not reproduced to the paragraph of Section 4 on the limitations of the estimates, and stated the convention (the Stokes stream function) in two examples of F9. During the fifth pass the value-sensitive bound (LF_0) and the sharp swirl-free floor 7^{1/2}/8 were entered in F2 from a separate derivation, as recorded in (27). The round-2 audits amended several numbered statements
of Sections 1 to 3 to make quantifiers, domains and hypotheses explicit, and replaced one proof. The works cited in R2.10 and R2.12 place those
results in the literature and are not used in any proof; the swirl regularity criterion of Chen, Fang and Zhang used in R2.16 was checked against its statement only, as noted there.
(27) Round 2 additions to F2. The Landau inequality (LF) in Frobenius norms and its extremal were taken from a separate derivation and checked here step by step by hand; the formula for the sphere average of the Hessian of the degree-one part (step (d) of its proof) was also checked by exact quadrature on generic data, the orthogonality inequality of step (c) numerically on test fields, and the constants 8/7^{1/2}, 12/10^{1/2}, 10^{1/2}/12 and 7^{1/2}/8 by 40-digit computation; the quotients of the planar extremal and of its smooth mollifications were also computed directly. The divergence-free constant K_div was taken from a separate derivation and checked here step by step by hand (the reduction to the degree-one part, the projection bound, the moment identities, the bound on w_B through a null vector of the skew part and the concavity of f_div, and the final maximization); the moment identities were also checked by exact sphere quadrature and the reduction identity numerically on a random polynomial field, the closed forms of p_div and q_div and the value of K_div by 40-digit computation, and an adversarial check of the derivation with its own exact arithmetic found no error. (LF) supersedes the bounds of earlier versions of F2: a ball-average Landau inequality and its divergence-free form (floors 2 30^{1/2}/45 and, in the plane, 3 3^{1/2}/16), a singular-value form of the averaging argument and its divergence-free form (floors 0.2545... and 0.2610...), and a direct proof of the bound 7^{1/2}/8 for circular vortices of class C^2 (a first version of its step at the centre assumed a limit that can fail for profiles with only C^{1,1} regularity, and was corrected before (LF) replaced it); these had been proved or rederived by hand and checked by exact and numerical computation. For the thin rings of (i) to (iii) the existence statements and the core-convergence proof of the works cited there were read (Literature paragraph below); two steps of the printed core-convergence proof (the energy bound and the exclusion of the zero limit) were found incomplete and are reproved in (ii); the passage from the core profile to the global quotient, the verification, for the scaled rings, of the properties of the Euler limit listed in Theorem 1 (no realization of these rings as limits of a Case 2 sequence of Navier-Stokes solutions is asserted) and the scaling of eta were derived by hand and checked again in adversarial audits. The enclosures of (iv) come from two independently written validated integrations (outward-rounded interval Taylor integration with 200-bit mantissas and order 22 for every listed p; in the logarithmic radial variable with 160-bit mantissas and order 36 for p = 2, 3 and 40), which use the same multiple-precision interval library, so that a rounding defect in that library could affect both; separately written floating-point integrations for p = 2, 3, 10 and 40 fall inside the enclosures of the first. The discrete ring quotients quoted in F2 come from the two discretizations named there, are uncertified, and no grid-refinement study of them is reported. The on-axis bound and the resulting lower bound on alpha_* were derived by hand, the on-axis formulas were checked by symbolic computation on a test field, and an adversarial check found one error in the first version (the swirl-free form of grad V had been applied to the prelimit fields, which may carry swirl), which was corrected before the bound was entered. The swirl-free floor 1/(B_2 + t_0^2) was taken from a derivation made for a related problem and rederived here by hand, first with the singular-value constant 3.0918... in the role of B_2 (floor 0.3158...) and then with B_2 = 8/7^{1/2} from (LF) (floor 0.3203...); the case analysis uses B_2 only through S <= B_2 < 4, K > 3 and the definition of t_0, and the identity for 12 f(K - b^2) and the form of the defining equation of t_0 do not depend on the value of B_2. An intermediate refinement (floor 0.3281..., through a determinant argument and two further Landau bounds, which discarded the value of the planar field W) is superseded by the sharp floor 7^{1/2}/8: the value-sensitive bound (LF_0) and the three steps of the second paragraph on swirl-free fields were taken from a separate derivation and rederived here by hand step by step; their numerical facts were checked by exact rational arithmetic, and an adversarial check of that derivation with its own exact arithmetic found no error. The Hessian bound (H) was checked by exact symbolic minimization, the Hessian identity it uses by symbolic computation on generic polynomial fields, and the identity for 12 f(K - b^2), the defining equation of t_0, the root t_0, the constants B_2 and K and the discriminants by symbolic and 40-digit numerical computation. An earlier version of the floor, 55 6^{1/2}/512 = 0.2631..., used the ball-average bound in place of the singular-value bound and a coarser case split; it is superseded. The kinematic rings were checked by hand.

Literature. The texts of Shahmurov (arXiv:2604.21213v3: Proposition 2.1, the balance (3.9), Theorem 3.1, Corollary 3.5, Theorems 6.1
and 7.1), the statements of the later Shahmurov papers cited in F5 (their proofs were checked only by the second model, where used), Seregin (arXiv:2402.13229v3, 2507.08733v2, 2606.29468v1), Constantin-Ignatova-Vicol (arXiv:2609.20762; arXiv:2609.20803, statements and proof outline only), Zhang
(arXiv:2604.07785), Nobili-Seis (arXiv:1906.07400), Hou (arXiv:2107.06509v2, Section 3.4.1) and Hou-Shi-Wang (arXiv:0912.1316v2: the
model, Theorem 1.1 and the statement of Section 4; the blowup proofs were not checked) and Hou-Li (arXiv:math/0608295v1: the 1D model,
its exact-solution property and the maximum principle as stated in Section 1; the differential identity behind it was rederived here,
the remaining proofs were not checked) were read here, as were the statements of Dascaliuc-Grujic (arXiv:1205.7080v1, Section 1),
Grujic (arXiv:1111.0217, Section 4) and Barker-Fernandez-Dalgo-Prange (arXiv:2302.06509v2, Theorem A) used in F5 (the criterion of Grujic and Guberovic is quoted as recorded by Dascaliuc and Grujic; the original paper was not consulted); the
Hou-Lei paper was not read here and is cited as described by Hou, Shi and Wang. The statements of
Koch-Nadirashvili-Seregin-Sverak used in B2 (Acta Math. 203 (2009)) were checked here against the arXiv version (arXiv:0709.3599v1:
Theorems 5.1 and 5.2, Remark 6.1, Proposition 4.1, Lemmas 4.1 and 6.1, whose numbering is used here); the journal text was not consulted. The results of Chen-Strain-Tsai-Yau, Lei-Zhang, Wei and Lei-Navas-Zhang in F5 were checked against abstracts
only and serve as literature leads. The locations of the kernel estimate of Section 2.9 in the papers of Shirota and Yanagisawa and of
Abidi, Hmidi and Keraani, and a further antecedent (Lei and Zhang, Pacific J. Math. 289 (2017), Section 4), were not checked against the
originals; the estimate is proved in Section 2.9 and does not depend on them. For F2 (i) and (ii) the texts of de Valeriola and Van Schaftingen (arXiv:1209.3988: Theorem 1 and Proposition 3.7), Cao, Wan, Wang and Zhan (Nonlinearity 35 (2022), arXiv:1910.07493: the hypotheses on the vorticity function and the existence statement, Theorem 2.1) and Cao, Lai, Qin, Zhan and Zou (arXiv:2206.10165v2: Proposition 1.4, Proposition 3.2 with its proof, the limits (3.10) and Lemma 3.4, whose energy bound is reproved in F2 (ii)) were read here; the journal data of the last (Math. Ann. 394 (2026), article 9) were checked on the publisher's page. No theorem from the Burgers-vortex literature is applied. The works cited for context in R2.10 and R2.12 (Szeri and Holmes; Wang;
Gallay and Wayne; Gallay and Sverak; Boulton; Schmid and Henningson; Davies; Bedrossian and Coti Zelati) and in Section 3
(Maekawa, Miura and Prange) were not checked against their texts here and are not used in any proof; of Gallay and Maekawa only
the abstract was read, as stated in R2.14. For R2.1 (b), Theorem 1 of Cozzi and Kelliher (Incompressible Euler equations and the effect of changes at a distance) was checked against the authors' preprint of 31 July 2015: it holds in R^d, for velocity and vorticity bounded on [0, T], with each pressure equal to sum_{k,l} R_k R_l (u^k u^l) in BMO; of Bourgain and Li (arXiv:1405.2847) only the abstract was read; the global theorems of Danchin and of Shao, Wei and Zhang are quoted with the hypotheses recorded in the introduction of Shao, Wei, Zhang and Zhang (arXiv:2605.19716v2), and their texts were not consulted. The theorem of Cozzi and Kelliher enters only the outlined reduction of R2.1 (b); none of these works is used in a completed proof.
A decay theorem for global axisymmetric solutions (Y. Liu, arXiv:2103.11200, Theorem 1.1) is reported to assume global existence and to give no uniform
relaxation time; it is not used, and no check against its text is recorded here. The other numerical candidates in F11 were not checked against the papers.

The audit records and the computations themselves are not reproduced here. The computations check the specified identities, constants and examples;
they do not replace the analytic proofs or establish any of the open implications.

## Appendix A. Proof of the claim of Section 4 (x)

Fix C > 0 and G > 0, and put mu = C/G. All constants chosen below are independent of delta. In this appendix the letters A, b, D, H, K and L denote the constants fixed in (A8), P = ||Phi'||_infinity is the constant defined just after (A8), P applied to an event denotes probability and E applied to a random variable expectation, the letters S, q and theta have local meanings defined below, Q denotes the radial transmission variable defined before (A44), and G_occ, G_j are an occupation kernel
and an event; none of them is a quantity of Sections 1-2 (historical suprema, Q_4 or the circulation bound), and U is the prescribed field
of Section 4 (x), not a limit of Navier-Stokes rescalings. Norms of vectors are Euclidean, and norms of derivative tensors are Frobenius
norms. Spatial derivatives and their sup norms are Cartesian unless another variable is specified. An integral without limits in the
variable z, v or y is over the real line. The letters B (an axial speed), gamma (a Lipschitz constant) and kappa (an inner radius in the
argument after (A24), and a tolerance after (A42)) and the martingale M_u of (A35) are also local; this kappa is not the positivity
threshold of the packet, and M_u is not a historical supremum. A killed process has terminal payoff zero after absorption.

We prove the following precise statement. There are K in (0, 1), L > 0 and alpha > 0, depending only on the fixed profiles and C, G, such
that, for every sufficiently small delta > 0 and nu = mu delta^3, the field constructed below is smooth, compactly supported in space,
axisymmetric, swirl-free and divergence-free, and satisfies, at every physical time t,

(A1) |U| <= 1, |grad U| <= 1, |grad^2 U| <= C, |d_t U| <= C(1 + C).

For the fixed terminal function phi specified below (a fixed smooth nonnegative test function, see (A6); no positive limiting-vorticity condition is imposed on it, and since U is swirl-free the circulation bound holds trivially), let psi be the bounded solution, continuous with value zero on the axis, of

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

Define the terminal function and the axial test envelope by

(A6) Phi(X) = (X/8) h(8X - 1) [1 - h((X - 4)/2)], xi(z) = h(z + 2) [1 - h(z - 19)], phi(R, z) = Phi(R^2) xi(z), g_0(z) = h(4(z + 4))
h(4(-3 - z)).

In particular, 0 <= Phi(X) <= min(1, X/8) for X >= 0, Phi = X/8 on [1/4, 4], and phi is a smooth Cartesian terminal function supported in {1/8 <= R^2
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
P(X_u=0 | axial path) = exp(-X_0/(4nu I_u)) for u > 0;
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

Its kernel is locally integrable in five dimensions. For the periodic profile f of B.1, the potential convolution Phi * f diverges logarithmically as the axial integration cutoff tends to infinity, and S f is defined by the absolutely convergent convolution K * f, justified in the paragraph after (B16). For d > 0,

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

This proves (B1). It also gives the asymptotic coefficient displayed in F10 (c):

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
(C46); it need not coincide with the alpha of (B30). Every other letter is defined in this appendix and has no meaning outside it; for example ||.||_X, ||.||_(X_-) and ||.||_(Xv) are norms (X is also the space completed in (C8)), env(v) is an envelope and Y_3, Y_infinity are envelope norms, P_R is a majorant, and K_t is an axially integrated
kernel.

We prove the following statement. For every C > 0 and G > 0 there are constants alpha > 0, delta_1 > 0 and c > 0, specified in C.10 as finite constants (not all evaluated numerically, C.11), such that, for every 0 < delta <= delta_1, with nu = (C/G) delta^3, the time-independent swirl

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
(C.5 to C.9). Neither limitation noted after F10 (c) applies: the localized error is controlled around the transported modulated approximation, not by a perturbative estimate around the drift-free localized solution of Appendix B (only the periodic steady states are expanded in epsilon, around the epsilon = 0 periodic state, in (C16)), and no velocity bound is derived from a bound on the vorticity ratio.

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

let ||.||_(X_-) be the same sum with |beta|+j <= 3 (both formulas are used with the same meaning for functions with only nonzero axial
modes that are not radial or not odd, such as a(H) and the derivatives in (C10)), and let X be the completion in (C8) of the smooth odd functions with finitely many
modes and rapidly decreasing transverse derivatives. Let G_n(t,.) denote the heat kernel of R^n (the subscript distinguishes it from the parameter G) and define

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
      a(h_delta) - [a(H^lambda)]_(theta = z, lambda = E(delta z)) = -delta E' Psi_lambda - d_z chi_delta,

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
      C_a = sup delta^(-1) |a(h_delta) - [a(H^lambda)]_(theta = z, lambda = E(delta z))|,

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

The unknown of (C27) is also denoted b; the next sentence shows that it is b(H) for the corresponding H. If b is a smooth solution of (C27), axisymmetric without swirl and tending to zero at infinity together with its derivatives, then
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

(C37) |(x_i - y_i) d_j G_5(xi, x - y)| <= 32 G_5(2 xi, x - y),   |d_j G_5(xi, x - y)| <= 32 xi^(-1/2) G_5(2 xi, x - y),

(for x, y in R^5 = R^4 x R with transverse parts x', y'; valid constants, enlarged to 32 in (C37), are 2^(5/2) times the maxima of (w/2) exp(-w/8) and of (w^(1/2)/2) exp(-w/8) over w > 0, that is 2^(5/2) 4/e < 8.4 and 2^(5/2) e^(-1/2) < 3.5) and
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

The exact solution is identified as follows. For fixed delta the force P_3(r F_delta e_r) is smooth and belongs to the Sobolev space W^{m,2}(R^3) for every m,
since r F_delta e_r = (x_1, x_2, 0) F_delta is smooth, axially compact and rapidly decreasing. By the classical local theory for the
Navier-Stokes equations with forcing (the energy method of A. J. Majda and A. L. Bertozzi, Vorticity and Incompressible Flow, Cambridge
University Press, 2002, Chapter 3, which applies with an added forcing term), (C27) has a unique solution b in C([0, s_*); W^{m,2}(R^3)) for every
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

Work. By (C45), the mass bound (B39) (int int r^2 F_delta dr dz <= A_F/delta) and the window length delta^(-2),
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
time-derivative, gradient-record and nonconstant-limit conditions of Case 2 are not part of the construction. In this model the share of the swirl dissipation paid by the self-compression is at most a constant multiple of alpha^2 G^2, and the residual of the swirl equation supplies the difference. Write D_1 = int_0^infinity (B(r) - |h(r)|) dr; it is positive and finite, since B - |h| = g^2/(B + |h|) lies in (0, g] for r > 0. Since f >= B - |h|, the change of variables R = delta r gives int q^2/R dy >= 2 pi alpha^2 C^2 delta^3 D_1 int chi(Z)^2 dZ at every time, so the swirl dissipation over the window, int_0^(1/nu) (2 int |grad q|^2 R dy + int q^2/R dy) dtau, is at least 2 pi alpha^2 C G D_1 int chi^2 dZ, while 3 W_s/nu <= 6 pi alpha^4 C G^3 A_F M_b by C.10. Since q does not depend on tau, the swirl balance of Theorem 9 (a), with the residual of the swirl equation as an additional source, gives this: the self-compression supplies at most the fraction 3 A_F M_b epsilon/(D_1 int chi^2 dZ) of the swirl dissipation, with epsilon = alpha^2 G^2 <= epsilon_1 as in C.10. Along an unforced evolution with negligible initial storage and remainder strain, 3 W_s/nu instead equals the normalized swirl dissipation plus the normalized final storage up to o(1), as in R2.18 (a). The constants C_O, A_b, C_R
and C_a are defined as finite suprema and are not evaluated numerically, and neither are alpha and delta_1. The existence of the smooth
solution in C.9 relies on the classical local theory and continuation criterion for the forced Navier-Stokes equations, cited and not
reproduced here.
