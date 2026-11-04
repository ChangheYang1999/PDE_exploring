# T2_ROUTE1_v03: route (1), near order and far scaling of the C_vs price (orientation), third version

Agent the second theory agent, 2026-11-04, a work session; written 2026-11-04 from about 13:30Z on the text of v02; frozen 2026-11-04T13:32:05Z. It
supersedes notes/T2_ROUTE1_v02.md (frozen 2026-11-04T13:17:44Z, SHA256
c1d8b99b90233e401de217940563e1448991d8a1612a784553f766f6af052d32) and notes/T2_ROUTE1_v01.md (written
2026-11-04T12:57:17Z, SHA256 5c7e488122f908c239f4106a483fc5c1aca49b67c60f9af33869cb1fe79a416e), which stay unchanged. To
the first theory agent (publication) and the coordinator; cc the theory auditor (a review of the changes against v02, section 9, is requested; the rest stays
HEURISTIC and FLOAT).

Status. HEURISTIC orientation with FLOAT numbers (binary64 grid and quadrature computations; no number here is a bound).
Lemma FS (section 3.2) is CONFIRMED by the theory auditor (AT2838, audit_v862) on its domain: nonzero L^2 tests with finite int
g^2/(4|X|^2), all positive dilations, 0 < alpha < 2, r > 0, P >= 0 and exact homogeneous scaling. The step of v01
section 3.3 item 2, from far agreement to the model estimate on the whole dilation class, is REFUTED (AT2839); here it
is replaced by a comparison at one dilate (Remark FS-1, elementary; CONFIRMED as a conditional statement at
one specified dilate, AT2859, audit_v869). Every conclusion about the true far
forms, including that no far term can be charged to a rate alone, is OPEN (AT2840); the use of the model for them is
HEURISTIC. The near-symbol count of section 2 and the weighted Riesz sketch of section 5.3 are not audited. Nothing here
changes a verdict: H4-REST stays OPEN and O3 stays unresolved. This is the work on route (1) of theory_v22 V22-1 (g),
which the second theory agent took (T2_H4REST_v02 section 6; the first theory agent agrees, theory_v22).

## 0. Summary

1. Near part (section 2). In the near-check form the joint coefficient M = atil I - K of Lemma MX costs 199.0 times the
   closure room (C) at the plan of record (T2_H4REST_v02, FLOAT). The braces of Lemma MX vanish to second order at high
   frequency (Remark MX-HF of T2_H4REST_v01). That suggests a price two orders lower, 2 kappa_1.1(mu)^2 sup chi_n
   Sig[M_n] W^2. Its value is 1.448e-3 x (C) at the plan and 1.347e-3 x (C) at the fallback (HEURISTIC: formal
   symbol, no remainder, sampled sups). Four pieces are missing for a proof (section 2.4).
2. Far part (section 3). For coefficients homogeneous of degree -alpha, alpha = 1 - 1/c = 0.447611231, Lemma FS says
   that a far estimate F(g) <= r ||g||^2 + P ||g/W||^2 holds for all tests if and only if Gamma(g) = c(g)/w(g)^(alpha/2)
   <= c*(r, P) for all tests. Here c* = (2r/(2 - alpha)) (P (2 - alpha)/(alpha r))^(alpha/2). With P = 0 no rate r is
   enough as soon as one test has c(g) > 0 (AT2838). For the true far forms they give a conclusion only through a
   comparison at one dilate where the true form is close to the model (section 3.2, Remark FS-1; AT2839).
3. Grid tests (section 4, FLOAT). The largest Gamma found is 1.5606 for C_vs2 + C_vs3 at J^q = 1 and 0.3774 for C_vs3
   alone. Each value is the discretized form at one admissible test, so it is a lower value for sup Gamma up to the
   discretization error. Halving dx changes Gamma by at most 0.019 in the resolution pairs of section 4.4, and the finer
   grid gives the larger value in each pair. The CF values still rise with the scale range of the grid, and these data
   do not determine their limit.
4. Reading (section 5; HEURISTIC, in the model of section 3.3, with the far homogeneity EXTRAPOLATED beyond r = 1.6e5).
   For the true far form an item that excludes an estimate needs Remark FS-1 at its dilate, and an item that leaves room
   needs a certified upper of sup Gamma and a comparison of the forms; both are OPEN (AT2840).
   - At the plan of record, the far C_vs2 + C_vs3 cannot be charged to the rate room (A) alone. That would need a price
     of at least 2.26 x (C).
   - With all of (C), it needs a rate of at least 1.26 x (A). The excess over (A) has to come from the free
     gain (B): at least 0.019 x (B) if all of (A) and all of (C) go to this term, and 0.27 x (B) with (C)/100.
     Charged to (B) alone, it needs at least 0.092 x (B) with all of (C), and 0.347 x (B) with (C)/100.
   - At the fallback, (A) alone is enough for this test family, at a price of at least 1.29e-3 x (C).
   - C_vs3 alone fits (A) at both tuples.
   - In the model no rate alone (P = 0) suffices, since the grid tests have c(g) > 0. For the true far forms this does
     not follow: a form whose coefficient vanishes inside the near cut can have a rate-only bound (AT2839). At r = (A)
     the model failure for CF reaches dilates of mean |X| up to 2.2e7, so a true-form version needs Remark FS-1 at such
     a dilate; OPEN (AT2840).
   So route (1) is not excluded by these orientations, but none of its pieces is certified.


## 1. Target and budgets

The rest term of C2-N1-013 is charged to three budgets. They are the same as in theory_v22 V22-1 and in the first theory agent's
theory_v23 draft table (f):
- (A), the rate room: 185113337/200000000000 (about 9.255667e-4) at the plan of record (11/20, 72), and
  8091005267/10^12 at the fallback (103/200, 68);
- (B), the free gain: 71675071190082633/5629499534213120000 (about 0.0127320502923) at both tuples;
- (C), the price allowance against D_out (closure check v06): 9941475955 at the plan, and 47277952671/5 (about
  9.4555905e9) at the fallback.

(A) and (B) multiply ||g||^2 (or ||J^(-1) g||^2, which is the same at low frequency). (C) multiplies ||h||^2 with
h = W^(-1) J^(-q) g; for tests of low frequency this is close to ||g/W||^2.

Route (1) asks for a price of the matrix coefficient of C_vs whose coefficient is not sup |M| W^2 or sup |K| W^2. The
current state, by piece (theory_v22 V22-1 (f), (h)):
- C_vs1 + C_vs3 near, in the near-check form: FLOAT 199.0 x (C) at the plan;
- the far C_vs1 and C_vs3: OPEN; window existence OPEN (AT2585);
- C_vs2: the form is defined (T2_H4_v01 section 2), but no usable certified H^q pricing estimate exists (AT2634).
This note treats the near part by order counting (section 2) and the far part by scaling (sections 3 and 4).

## 2. Near part: the order of the joint form (HEURISTIC)

2.1 The current price. The near check prices a coefficient a at 2 kappa_0 kappa_2q sup |a| W^2, plus a kappa_j part at
sup a_+ W^2 (the first theory agent NEAR_CHECK_v07; kernel constants of near_params_v05.json). Put the joint coefficient chi_n M in place
of a_n. With the sampled sup chi_n |M| W^2 = 151.91 and sup chi_n lambda_max(M_n)_+ W^2 = 147.984 (FLOAT,
research/h4rest/fields_rest.out), this is 1.9779e12 at the plan, 199.0 x (C), and 166.4 x (C) at the
fallback (near_orient.out; the same values as T2_H4REST_v02 section 4).

2.2 The mechanism. The entries of K are first derivatives of rhobar, so K^(zeta) carries a factor zeta. The braces of
Lemma MX vanish to second order in zeta at high frequency: the order 1/|xi| cancels, and the order |xi|^(-2) term is
(P zeta)^T M^(zeta) (P zeta) (Remark MX-HF). So the bilinear form behaves like a second-order commutator. Its kernel
weight <xi>^(2q) drops to <xi>^(q-1) <eta>^(q-1). The coefficient sup |M| W^2 is replaced by the formal symbol
    Sig[M] = (1/2) [d_e^2 (e^T M e) - 2q d_e d_omega (e^T M omega) + q^2 d_omega^2 (omega^T M omega)],
which contains second derivatives of M, i.e., third derivatives of rhobar. In the kernel constants, kappa_0 kappa_2q
becomes kappa_(q-1)^2.

2.3 Size (near_orient.out; FLOAT).
- Plan, mu = 72: kappa_1.1(72) = 401.766, which agrees with research/h4rest/kappa_rest.out. Then kappa_1.1^2 =
  1.61416e5, which is 2.375e-5 times 2 kappa_0 kappa_2q.
- Fallback, mu = 68: kappa_1.1(68) = 377.917.
- The sampled sup chi_n Sig[M_n] W^2 is 44.6004, at the sampled origin. The scalar part sup chi_n Sig[a_n] W^2 is
  50.2272, so at the formal level the joint rate symbol stays below the scalar one (T2_H4REST_v01).
- The order -2 price is 2 kappa_1.1^2 sup chi_n Sig[M_n] W^2. It is 1.4398e7 = 1.448e-3 x (C) at the plan
  and 1.347e-3 x (C) at the fallback. That is a factor of about 690 below (C) at the plan; that factor is left
  for the constants that the missing pieces below would add.

2.4 What a proof needs (none of it exists).
1. A matrix localization (rate) lemma of AT-428 type for Q[M_n]. The rate side of the joint form is formal only
   (AT2582).
2. A band price lemma with an explicit remainder for the second-order expansion. The remainder needs the Peetre factor
   <zeta>^q and Fourier moments of M (in effect, of rhobar up to third derivatives).
3. The terms where derivatives fall on chi_n.
4. Certified sups of chi_n Sig[M_n] W^2 and of the moments, in place of the FLOAT samples.

## 3. Far part: a scaling condition

3.1 Setting. At large |X| the coefficients are close to homogeneous of degree -alpha, alpha = 1 - 1/c = 0.447611231.
r^alpha grad rhobar changes by 1.06e-2 (relative) from y = log r = 9 to 10.5, and by 5.43e-3 from 10.5 to 12 (FLOAT,
research/route1/far_profile.out). The change halves per step of 1.5 in y; beyond r = e^12, about 1.6e5, homogeneity
is EXTRAPOLATED. At large scale and low frequency J^q is close to 1, and W is close to 2|X|. The model forms, with
grad rhobar = |X|^(-alpha) (P_x, P_y)(theta) (the y = 12 profile), are:
    C3(g) = Re<grad rhobar.U[g], g> - int (Rg)^T K (Rg)            (C_vs3 of T2_H4_v01 section 2),
    CF(g) = Re<grad rhobar.W U[W^(-1) g], g> - int (Rg)^T K (Rg)   (C_vs2 + C_vs3 at J^q = 1, W = 2|X|),
where U[g] = (-R_1 R_2 g, R_1^2 g) and the tests are S1 functions (even in x, odd in y).

Under g_l(X) = l^(-1) g(X/l), with l > 0 the dilation factor:
- ||g|| and the S1 class are kept;
- R_j and W U[W^(-1) .] commute with the dilation, so C3(g_l) = l^(-alpha) C3(g) and CF(g_l) = l^(-alpha) CF(g);
- int g_l^2/(4|X|^2) = l^(-2) int g^2/(4|X|^2).

3.2 Lemma FS (elementary; CONFIRMED, AT2838, on the class of the status paragraph). Let F be a real quadratic form
on a dilation-invariant class of tests with F(g_l) = l^(-alpha) F(g) for all l > 0, where 0 < alpha < 2. Let r > 0
and P >= 0. Write
- c(g) = F(g)/||g||^2,
- w(g) = int g^2/(4|X|^2) / ||g||^2,
- Gamma(g) = c(g)/w(g)^(alpha/2) when c(g) > 0, and c*(r, P) = (2r/(2 - alpha)) (P (2 - alpha)/(alpha r))^(alpha/2).
Then F(g) <= r ||g||^2 + P int g^2/(4|X|^2) holds for every test g if and only if Gamma(g) <= c*(r, P) for every test
with c(g) > 0. In particular, for P = 0 the estimate fails somewhere on the dilation orbit of every test
with c(g) > 0: it fails at the dilates g_l with l < (c(g)/r)^(1/alpha) (AT2861; it may hold at g itself).
Proof.
- Fix g with c = c(g) > 0 and w = w(g), and put s = 1/l. The estimate at g_l reads
  f(s) = r + P w s^2 - c s^alpha >= 0.
- If P = 0, then f(s) < 0 for s^alpha > r/c.
- If P > 0, then f tends to r as s -> 0 and to +infinity as s -> infinity, because 2 > alpha. Its only critical point
  on s > 0 is s_0 with s_0^(2 - alpha) = alpha c/(2 P w). There P w s_0^2 = (alpha/2) c s_0^alpha, so
  f(s_0) = r - (1 - alpha/2) c s_0^alpha.
- Hence the estimate holds for all l if and only if c s_0^alpha <= 2r/(2 - alpha). Inserting s_0 and raising to the
  power (2 - alpha)/2 gives c <= (2r/(2 - alpha))^(1 - alpha/2) (2 P w/alpha)^(alpha/2) = c*(r, P) w^(alpha/2).
- Tests with c(g) <= 0 satisfy the estimate trivially, and the class is closed under dilation. QED.
Consequences, since c* is proportional to r^(1 - alpha/2) P^(alpha/2):
- (a) the least price for a given r is P_min = P (Gamma/c*(r, P))^(2/alpha);
- (b) the least rate for a given P is r_min = r (Gamma/c*(r, P))^(1/(1 - alpha/2));
- (c) at the binding (r, P), the minimum sits at l_c = ((2 - alpha) c(g)/(2r))^(1/alpha). So the critical dilate has
  mean |X| equal to l_c times the mean |X| of g.

(a) and (b) are statements for one orbit with a positive reference price P; for the whole class, Gamma is replaced by
sup Gamma (AT2838).

Remark FS-1 (one dilate; elementary, from the proof above; CONFIRMED as a conditional statement, AT2859).
Fix g with c = c(g) > 0 and w = w(g), and
(r, P) with P > 0. Put rho = Gamma(g)/c*(r, P), let s_0 be the critical point of the proof and l_0 = 1/s_0. Then
c s_0^alpha = (2r/(2 - alpha)) rho^(2/(2 - alpha)), P w s_0^2 = (alpha/(2 - alpha)) r rho^(2/(2 - alpha)) and
f(s_0) = -r (rho^(2/(2 - alpha)) - 1). Let F_true be another quadratic form (the true far form) and N, Q nonnegative
weights with N(h) <= ||h||^2, and suppose that at the single dilate h = g_(l_0) one has
|F_true(h) - F(h)| <= delta ||g||^2 and Q(h) <= (1 + eps) int h^2/(4|X|^2). If rho > 1 and delta + eps P w s_0^2 < r
(rho^(2/(2 - alpha)) - 1), then F_true(h) <= r N(h) + P Q(h) fails at h. Proof: F_true(h) >= (c s_0^alpha - delta)
||g||^2, and r N(h) + P Q(h) <= (r + (1 + eps) P w s_0^2) ||g||^2; the difference of the two right sides is
(-f(s_0) - delta - eps P w s_0^2) ||g||^2 > 0. QED. For the true budgets, N is ||h||^2 or ||J^(-1) h||^2 and
Q(h) = ||W^(-1) J^(-q) h||^2 <= int |J^(-q) h|^2/(4|X|^2), because W^2 >= 4|X|^2. That inequality alone does
not compare the right side with int h^2/(4|X|^2), which is what eps measures; that comparison is item (iii) below and
is OPEN (AT2840, AT2862).

At the row that decides section 5.1 (CF, plan of record, r = (A), P = (C), the test of far_cvs_s3; FLOAT): rho is 1.2010
and rho^(2/(2 - alpha)) is 1.2662, so -f(s_0) is about 0.266 (A), the form value c s_0^alpha about 1.63 (A) and
P w s_0^2 about 0.365 (A), all per ||g||^2. With eps = 0 the contradiction holds as long as the true form at that dilate
differs from the model by less than about 16 percent of the model value. The dilate has l_0 about 2.7e6 and mean |X|
about 7.3e6. A true-form obstruction there needs bounds, at that one dilate, for (i) the coefficient against the
homogeneous model at the radii that carry the dilated test (the FLOAT profile is checked to r = 1.6e5 only), (ii) the
share of the dilated test inside the near cut, through the nonlocal Riesz transforms, (iii) eps, from J^(-q) against 1
at frequencies of order 1/l_0, and (iv) the grid error of c(g) and w(g) for a continuous test (the resolution pairs of
section 4.4 changed Gamma by up to 0.019, against Gamma - c* = 0.261). None of these is bounded here (AT2840 OPEN). The
numbers are binary64 arithmetic on the row of far_table.out by the formulas above (research/route1_v02/fs1_numbers.py
and .out; SHA256 in research/route1_v02/SHA256SUMS).

3.3 Use for the true far forms (HEURISTIC; AT2839, AT2840). Lemma FS is a statement about the model on the whole
dilation class. For the far C_vs2 + C_vs3 (and for C_vs3 alone) it is used only through Remark FS-1 at one dilate, for
these reasons:
1. The true coefficient is homogeneous only asymptotically. The dilates that matter sit at the critical mean |X| of
   (c). In the row that decides section 5.1 (CF, plan of record, r = (A)) that radius is 1.2e7, and it is
   2.6e5 for C3 at r = (A). So the near region and the zone where homogeneity is checked (r <= 1.6e5) carry a
   vanishing share of the dilated test there, and the use rests on the EXTRAPOLATED homogeneity. In the other CF rows
   the radius is at least 1.1e4. For C3 with r = (A) + (B) at the fallback it goes down to 250, where
   homogeneity is not checked (r^alpha grad rhobar changes by 1.06e-2 from y = 9 to 10.5); these rows are far from
   binding (Gamma/c* below 0.04) and no conclusion is drawn from them.
2. v01 inferred from W^2 >= 4|X|^2, and from h = W^(-1) J^(-q) g being close to g/W at low frequency, that an estimate
   in the true budgets implies the model estimate with the same (r, P) on the whole dilation class. That inference is
   REFUTED (AT2839): a form whose coefficient vanishes on |X| <= R and equals the homogeneous one beyond 2R has a
   rate-only bound with rate of order R^(-alpha), while the model has none; the dilates where the model fails can lie
   inside the cutoff. What remains is Remark FS-1: an estimate in the true budgets gives the model inequality at one
   dilate up to the errors delta and eps there. At the row that decides section 5.1 that dilate has mean |X| about
   7.3e6, and the margin allows a relative form error of about 16 percent (FLOAT); no bounds for the errors there are
   available.
3. In the model, the condition holds for the totals of rate and price that any splitting spends on the far
   C_vs2 + C_vs3 at large scale. A window or a coefficient split only redistributes these totals.
4. It does not cover a joint estimate of a sum of far forms. If another far form with the same scaling is estimated
   together with C_vs (the far T_II part has the coefficient atil, also of degree -alpha), the relevant Gamma is that of
   the sum. This note computes C3 and CF only.
5. The sampled Gamma is a lower value for sup Gamma up to the grid error ((iv) of Remark FS-1). It can show that an
   estimate is impossible, never that it holds; for that one would need a certified upper of sup Gamma (section 5.3).


## 4. Grid tests (FLOAT)

4.1 Method (research/route1/far_cvs.py).
- Grid. A periodic N x N grid on [-L, L)^2 with dx = 2L/N. R_j is applied by FFT, with symbol i omega_j and the Nyquist
  mode set to 0.
- Coefficients. The y = 12 profile (far_profile.json, conjugate-pair modes) times max(|X|, dx/2)^(-alpha). The
  coefficients are projected on their parities: rho_x odd in x and in y, rho_y even in both. W = (dx^2 + 4|X|^2)^(1/2).
- Operators. The S1 operators A of C3 and CF are formed symmetrically. Checks printed by every run:
  - symmetry (relative): at most 1.2e-13 in every reported run;
  - constant coefficients: with a constant grad rhobar, C3 vanishes to at most 5.5e-16 of max |g|.
  - S1 preservation: in window mode the printed "S1 preserved" number also measures the low pass, so it is not a
    parity check. The parity check is the penalty-mode run far_cvs_c1.out: S1 preserved 1.6e-15 (C3) and 6.7e-16 (CF).
- Eigenproblem. For each kappa, the top eigenvalue of P1 (A - kappa/W^2 - penalties) P1 (scipy eigsh). P1 is the S1
  projection, composed in window mode with the sharp low pass Q onto |xi| <= xi_c. The reported numbers c, w and Gamma
  are those of the form A itself at one test. Only kappa = 1 is reported; kappa = 4 changed Gamma by about 1 percent
  in the development runs (dev/far_cvs_t2.out).

4.2 Artifacts and controls (development runs, research/route1/dev/README.md).
- The plain top eigenvectors are grid artifacts: C3 3.88, CF 23.4. They sit at grid scale near the origin and at the
  periodic seams, where the odd rho_x jumps and the periodic W has kinks.
- A smooth taper of the coefficients (projection mode) is a negative control. The commutator forms gain on the varying
  coefficient, and the eigenvector moves into the taper (C3 4.07, CF 6.41, with 97 percent of the mass beyond 0.6 L).
- Spatial and frequency penalties remove both effects (C3 0.213, CF 1.308 at xi_c 1.5) but converge slowly.

4.3 Window mode (reported).
- Q is the sharp low pass; the spatial penalty is 30 (1 - m)^2, with m = 1 on |X| <= 0.3 L, m = 0 on |X| >= 0.45 L,
  and a C^1 ramp in between. There is no frequency penalty.
- For the top eigenvector g, the reported test is g_w = P_S1(m g), the S1 projection of m g without the low pass.
  g_w is supported in |X| <= 0.45 L, so it does not meet the seams.
- g_w keeps 0.9989 to 0.999988 of ||g||^2. Its spectral mass outside |xi| <= xi_c is 1.3e-6 to 8.0e-5.
- c, w and Gamma are evaluated at g_w.

4.4 Results (research/route1/far_table.out). Gamma is invariant under dilation. So on these grids the test found depends
on the scale range L xi_c, on the resolution dx xi_c and, through the term kappa/W^2 of the eigenproblem (which does not
scale like the form), on L. Two kinds of pairs (far_table.out) separate the last two effects:
- resolution pairs, the same L, xi_c and kappa with dx halved: r1 to s5 +0.0124; s1 to s6 +0.0190 (CF);
- dilation pairs, the same N, L xi_c and dx xi_c with L doubled: s5 to r3 -0.0322; s2 to s1 -0.0027 (CF).
So the discretization changes Gamma by at most 0.019 in these pairs, and the finer grid gives the larger value. The
choice of L moves the test that the eigenproblem finds by up to 0.033. Each value is still the form at one test, so only
the largest matters.

    C3:
    file            | N    | L   | dx     | xi_c | L xi_c | dx xi_c | c(g_w)    | w(g_w)    | Gamma     | mean |X|
    far_cvs_r1.out  | 256  | 32  | 0.2500 | 3    | 96     | 0.75    | 0.1270196 | 0.0132382 | 0.3343612 | 5.3361
    far_cvs_r2.out  | 256  | 32  | 0.2500 | 6    | 192    | 1.5     | 0.1725552 | 0.0319603 | 0.3729103 | 3.6803
    far_cvs_s4.out  | 512  | 64  | 0.2500 | 6    | 384    | 1.5     | 0.1728888 | 0.0305403 | 0.3774511 | 3.9371

    CF:
    file            | N    | L   | dx     | xi_c | L xi_c | dx xi_c | c(g_w)    | w(g_w)    | Gamma     | mean |X|
    far_cvs_s5.out  | 512  | 32  | 0.1250 | 3    | 96     | 0.375   | 0.9152412 | 0.1284103 | 1.4488916 | 2.8522
    far_cvs_r1.out  | 256  | 32  | 0.2500 | 3    | 96     | 0.75    | 0.8983151 | 0.1227579 | 1.4364964 | 2.8761
    far_cvs_r3.out  | 512  | 64  | 0.2500 | 1.5  | 96     | 0.375   | 0.6832801 | 0.0384584 | 1.4167256 | 5.1714
    far_cvs_r2.out  | 256  | 32  | 0.2500 | 6    | 192    | 1.5     | 1.0947783 | 0.2395313 | 1.5073996 | 2.3780
    far_cvs_r4.out  | 512  | 64  | 0.2500 | 3    | 192    | 0.75    | 0.9217564 | 0.1162207 | 1.4921448 | 3.4346
    far_cvs_s2.out  | 512  | 32  | 0.1250 | 12   | 384    | 1.5     | 1.1480020 | 0.2708091 | 1.5378565 | 2.2844
    far_cvs_s6.out  | 1024 | 64  | 0.1250 | 6    | 384    | 0.75    | 1.1250236 | 0.2360016 | 1.5541996 | 2.7176
    far_cvs_s1.out  | 512  | 64  | 0.2500 | 6    | 384    | 1.5     | 1.0999286 | 0.2254264 | 1.5352025 | 2.7813
    far_cvs_s3.out  | 1024 | 64  | 0.1250 | 12   | 768    | 1.5     | 1.1486760 | 0.2542284 | 1.5606723 | 2.6543

For CF the largest Gamma at a fixed resolution dx xi_c rises with the scale range L xi_c. With dx xi_c = 0.75: 1.4364,
1.4921, 1.5541 at L xi_c = 96, 192, 384 (increments 0.056, 0.062); with dx xi_c = 1.5: 1.5073, 1.5378, 1.5606 at L xi_c
= 192, 384, 768 (increments 0.030, 0.023). The ratio of the last two increments is 1.12 (dx xi_c = 0.75) and 0.75 (dx
xi_c = 1.5), so these data do not determine the limit; sup Gamma may lie well above the largest value. Every conclusion
of section 5 is drawn from the largest computed value, 1.5606. The conclusions that an estimate is impossible only get
stronger if sup Gamma is larger. The statements that the condition leaves room (Gamma/c* < 1) are not conclusions about
sup Gamma; they could fail.

Evaluation of Lemma FS at the largest Gamma per form. The table gives:
- Gamma/c*(r, (C)) for r = (A), (B) and (A) + (B);
- P_min/(C);
- the critical mean |X|;
- the largest mean |X| at which a rate-only charge (P = 0) still fails;
- r_min for P = (C), (C)/10, (C)/100 and (C)/1000.

| form | case | r | c*(r, (C)) | Gamma/c* | P_min/(C) | critical mean abs(X) | P = 0 fails up to mean abs(X) |
|---|---|---|---|---|---|---|---|
| C3 | plan of record | (A) | 1.29938 | 0.2905 | 0.003992 | 2.653e+05 | 4.673e+05 |
| C3 | plan of record | (B) | 9.94089 | 0.03797 | 4.495e-07 | 7.591e+02 | 1.337e+03 |
| C3 | plan of record | (A) + (B) | 10.4974 | 0.03596 | 3.524e-07 | 6.489e+02 | 1.143e+03 |
| C3 | registered fallback | (A) | 6.91393 | 0.05459 | 2.277e-06 | 2.090e+03 | 3.681e+03 |
| C3 | registered fallback | (B) | 9.83003 | 0.0384 | 4.726e-07 | 7.591e+02 | 1.337e+03 |
| C3 | registered fallback | (A) + (B) | 14.4008 | 0.02621 | 8.58e-08 | 2.529e+02 | 4.455e+02 |
| CF | plan of record | (A) | 1.29938 | 1.201 | 2.268 | 1.230e+07 | 2.166e+07 |
| CF | plan of record | (B) | 9.94089 | 0.157 | 0.0002553 | 3.519e+04 | 6.198e+04 |
| CF | plan of record | (A) + (B) | 10.4974 | 0.1487 | 0.0002002 | 3.008e+04 | 5.299e+04 |
| CF | registered fallback | (A) | 6.91393 | 0.2257 | 0.001293 | 9.690e+04 | 1.707e+05 |
| CF | registered fallback | (B) | 9.83003 | 0.1588 | 0.0002684 | 3.519e+04 | 6.198e+04 |
| CF | registered fallback | (A) + (B) | 14.4008 | 0.1084 | 4.874e-05 | 1.173e+04 | 2.065e+04 |

| form | case | P | r_min | r_min/(A) | r_min/(B) |
|---|---|---|---|---|---|
| C3 | plan of record | 1 (C) | 1.8825e-04 | 0.2034 | 0.0148 |
| C3 | plan of record | 1/10 (C) | 3.6565e-04 | 0.3951 | 0.0287 |
| C3 | plan of record | 1/100 (C) | 7.1024e-04 | 0.7674 | 0.0558 |
| C3 | plan of record | 1/1000 (C) | 1.3796e-03 | 1.4905 | 0.1084 |
| C3 | registered fallback | 1 (C) | 1.9099e-04 | 0.0236 | 0.0150 |
| C3 | registered fallback | 1/10 (C) | 3.7097e-04 | 0.0459 | 0.0291 |
| C3 | registered fallback | 1/100 (C) | 7.2058e-04 | 0.0891 | 0.0566 |
| C3 | registered fallback | 1/1000 (C) | 1.3996e-03 | 0.1730 | 0.1099 |
| CF | plan of record | 1 (C) | 1.1720e-03 | 1.2663 | 0.0921 |
| CF | plan of record | 1/10 (C) | 2.2765e-03 | 2.4596 | 0.1788 |
| CF | plan of record | 1/100 (C) | 4.4218e-03 | 4.7774 | 0.3473 |
| CF | plan of record | 1/1000 (C) | 8.5890e-03 | 9.2797 | 0.6746 |
| CF | registered fallback | 1 (C) | 1.1891e-03 | 0.1470 | 0.0934 |
| CF | registered fallback | 1/10 (C) | 2.3096e-03 | 0.2855 | 0.1814 |
| CF | registered fallback | 1/100 (C) | 4.4862e-03 | 0.5545 | 0.3524 |
| CF | registered fallback | 1/1000 (C) | 8.7140e-03 | 1.0770 | 0.6844 |


## 5. Reading for route (1) and for the H4-REST table (HEURISTIC; in the model of section 3.3)

5.1 Plan of record (11/20, 72).
- Near part: the order -2 price is 1.448e-3 x (C) (section 2), against 199.0 x (C) in the near-check form. If the four
  pieces of section 2.4 could be supplied with moderate constants, the near C_vs would no longer be the obstruction.
- Far part: with the largest CF test, Gamma/c*((A), (C)) = 1.201 > 1.
  - So in the model no estimate of the far C_vs2 + C_vs3 by (A) alone exists with P <= 2.26 (C). For the true far form
    this needs Remark FS-1 at the dilate of mean |X| about 7.3e6 (with P = (C)); OPEN (AT2840).
  - With P = (C), the rate must be at least 1.26 (A). At P = (C)/100 it must be at least 4.77 (A),
    which is 0.347 (B).
  - Hence at the plan the far C_vs2 + C_vs3 needs part of the free gain (B): at least 0.019 (B) even with all
    of (A) and all of (C), and at least 0.092 (B) if it is charged to (B) alone.
- theory_v22 V22-1 (f) and the theory_v23 draft already charge the far C_vs1, C_vs3 and T_IS to (B), and C_vs2 to no
  budget. The test above says that the far C_vs2, priced together with C_vs3, cannot go to (A) alone. In (B), the
  scaling condition leaves room: Gamma/c* is 0.157 with r = (B) and P = (C). Since P_min scales like
  (Gamma/c*)^(2/alpha), sup Gamma would have to be about 1/0.157 times the largest value found to close that room.
- C3 (C_vs3 alone) fits (A) with P >= 4.0e-3 (C) on this test family.

5.2 Fallback (103/200, 68).
- With r = (A) alone, Gamma/c* = 0.226 for CF, and P_min = 1.29e-3 (C).
- The scaling condition leaves room at both tuples once r includes (B).
- The near price is 1.347e-3 x (C) (HEURISTIC).

5.3 What would turn this into estimates.
1. A certified upper Gamma^+ of sup Gamma for the far model forms. Lemma FS then gives the far estimate with any
   (r, P) satisfying Gamma^+ <= c*(r, P). Gamma is finite by the following sketch (not audited). |X|^(2 - alpha) and
   |X|^(-alpha) are A_2 weights on R^2, because -2 < -alpha < 2 - alpha < 2. So the Riesz transforms are bounded on the
   weighted L^2 spaces, and both forms are bounded by a constant times int |X|^(-alpha) g^2 (for CF write
   u = g/|X|). By Hoelder, int |X|^(-alpha) g^2 <= ||g||^(2 - alpha) (int g^2/|X|^2)^(alpha/2). No explicit constant
   is computed here.
2. A comparison of the true far coefficient with the homogeneous one. This needs certified decay of
   r^alpha grad rhobar - (P_x, P_y) and of its first derivatives, for r beyond the near cut (for an obstruction,
   only at the dilate of Remark FS-1). The available data are
   FLOAT samples to r = 1.6e5.
3. The passage from J^q = 1 to the H^q forms. At high frequency the far forms must be priced by another mechanism (the
   weight ||h||^2 is small there), which this note does not touch.
4. For the near part, the four pieces of section 2.4.
None of these exists. A certified result before the team stop is not expected (HEURISTIC).

## 6. What this note does not show

- No price is proved. The near number is an order count with a formal symbol. The far numbers are lower values on
  grid tests.
- Section 5.1 shows only that one charge is impossible in the model: the far C_vs2 + C_vs3 cannot go to (A) alone at the
  plan. For the true far form it is conditional on Remark FS-1 at one dilate, with the errors (i) to (iv) bounded there,
  which is OPEN (AT2839, AT2840).
- It does not say that the H4-REST rest term closes, and it does not touch T_IS NE-lo, the HI' cuts or C_tr.
- It does not touch the budgets themselves. It does not vary c_l and does not change Candidate 007.

## 7. Files and runs (research/route1/; SHA256 in research/route1/SHA256SUMS)

- far_profile.py, far_profile.out, far_profile.err, far_profile.json: the far profile (FLOAT).
- far_cvs.py: the grid forms. Outputs far_cvs_r1 to r4, s1 to s6 and c1 (.out, .err).
- Drivers (one job at a time on core 41, nice 19, one thread, each run under a timeout), with logs:
  - run_far.sh, run_far.log: far_cvs_r1 to r4;
  - run_far2.sh, run_far2.log: far_cvs_s1 to s4;
  - run_far3.sh, run_far3.log: far_cvs_c1, the penalty-mode parity check;
  - run_far4.sh, run_far4.log: far_cvs_s5 and s6, the resolution pairs of r1 and s1.
- far_table.py, far_table.out, far_table.err: the tables of section 4.4.
- near_orient.py, near_orient.out, near_orient.err; run_near.sh, run_near.log: section 2.
- dev/: development runs of script versions that were not kept (README.md).

Run times (seconds, per form, kappa 1): c1 17.6 s (C3) and 0.9 s (CF); r1 87.6 s (C3) and 14.3 s (CF); r2 71.1 s (C3)
and 15.4 s (CF); r3 79.2 s (CF); r4 119.1 s (CF); s1 87.8 s (CF); s2 104.7 s (CF); s3 491.7 s (CF); s4 400.6 s (C3); s5
136.7 s (CF); s6 476.2 s (CF); near_orient 26.3 s.

## 8. Changes against T2_ROUTE1_v01

- Title, header and status paragraph: AT2838 CONFIRMS Lemma FS on its class; AT2839 REFUTES the step of v01 section 3.3
  item 2; AT2840 OPEN (the theory auditor audit_v862, 13:09:01Z). The second theory agent accepts AT2839.
- Section 0 items 2 and 4: the P = 0 statements are restricted to the model and to tests with c(g) > 0; the true-form
  reading needs Remark FS-1.
- Section 3.2: the domain of AT2838 is named; the per-orbit scope of (a) and (b) is stated; Remark FS-1 (new;
  elementary, not audited) with its numbers at the binding row (FLOAT).
- Section 3.3: the heading, item 2 (the refuted inference and what replaces it), item 3 (in the model) and item 5 (grid
  error).
- Section 5: the heading (in the model); in 5.1 and in section 6 the impossibility of charging the far C_vs2 + C_vs3 to
  (A) alone is stated in the model, and for the true form as conditional on Remark FS-1; 5.3 item 2 names the dilate of
  Remark FS-1.
- New files: research/route1_v02/fs1_numbers.py, .out, .err and SHA256SUMS (the numbers of Remark FS-1).
- Review requested (the theory auditor): Remark FS-1 and that these changes state AT2838 to AT2840 with their scopes. No number of
  v01 is changed; sections 1, 2, 4 and 7 are unchanged.

## 9. Changes against T2_ROUTE1_v02

- The theory auditor audit_v869 (13:24:16Z): AT2859 CONFIRMS Remark FS-1 as a conditional statement at one specified dilate; AT2860
  CONFIRMS the revised exterior qualification and its integration in T2_PART7_v11, apart from the P = 0 sentence; AT2861
  REFUTES the pointwise reading of that sentence, which v02 Lemma FS shares (for alpha = 1, c(g) = 1 and r = 2 the bound
  holds at g; by Lemma FS it fails at g_l for l < 1/2); AT2862 OPEN. The second theory agent accepts AT2861.
- Header and status paragraph: v03 supersedes v02; Remark FS-1 is CONFIRMED as a conditional statement (AT2859).
- Section 3.2: the P = 0 sentence of Lemma FS states the failure on the dilation orbit (the wording of AT2861);
  Remark FS-1 is marked CONFIRMED, and its last sentence says that W^2 >= 4|X|^2 alone does not give eps.
- Review requested (the theory auditor): that these changes state AT2859 to AT2862 with their scopes. No number of v02 is changed,
  and no other text. Section 8 is the list of changes of v02 against v01, unchanged.
