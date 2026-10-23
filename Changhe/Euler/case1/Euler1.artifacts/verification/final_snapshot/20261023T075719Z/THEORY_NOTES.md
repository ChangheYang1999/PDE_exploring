# THEORY_NOTES.md (lead): stagnation-set obstruction for c_l < 1/2

Status: v3.1, 2026-10-23 07:27Z (v3 07:14Z; v3.1 adds the 7.3/7.4 presentation repairs and the 7.8/8 scope
corrections from the audits, section 6). NEW in v3: Theorem L2 (section 7) removes the countability hypothesis of L1. For
0 < c < 1/2 every C^2 solution of the profile equations on R^3 with U = o(|y|) has Omega = 0 and U constant; there
is no hypothesis on the stagnation set. Three checks agree (section 6): the verifier's own proof (written before it
saw the referee's), the referee proof (question uncount1), and the lead's line-by-line check of both. Section 8 gives
the resulting compactness statement for approximate solutions (question floor1). Sections 3 and 5 of v2 are kept for
the record and are superseded where marked. v2 is archived as archive/THEORY_NOTES_v2.md.

v2 status (kept): Theorem L1 and Corollary L1' were derived by the lead and CONFIRMED by two independent
audits (section 6), each with its own proof of the delicate Step 6. Section 3(d) of v1 was wrong and is replaced.
The result is informal (not machine checked). No novelty is claimed; the argument refines the proof of Theorem 3.9 of
Constantin-Ignatova-Vicol, "On putative self-similarity for incompressible 3D Euler", arXiv:2602.17570v3 (20 Jul 2026),
called [CIV] below, by replacing their local outgoing hypothesis with a measure argument.

Notation as in EQUATIONS.md, canonical frame C = 0, c := c_l in (0, 1/2).
V(y) = c y + U(y), G = grad U (G_ij = d_j U_i), S = (G + G^T)/2, Omega = curl U, N_V = {V = 0}.
Flow: d/ds Y(a,s) = V(Y(a,s)), Y(a,0) = a. (Physical particle paths x(t) correspond to y = (x - x_*)/tau^c with
s = -log tau, so s increases with physical time.) Phi_s(a) = Y(a,s).

## 1. Statement

Theorem L1 (confirmed by two audits, section 6). Let 0 < c < 1/2. Let U in C^2(R^3), P in C^2(R^3) solve
(1-c)U + (c y + U)·grad U + grad P = 0, div U = 0 on R^3, with U(y) = o(|y|) as |y| -> infinity.
If N_V is countable, then Omega = 0 identically, so U is constant; if in addition U -> 0 at infinity, U = 0.

Corollary L1'. Under the same hypotheses but with N_V arbitrary, let E := {y in N_V : lambda_max(S(y)) >= 1}.
Then Omega(a) = 0 for every a whose alpha-limit set alpha(a) does not meet E. At every point of E, grad V has an
eigenvalue with negative real part.

## 2. Proof

Step 0 (regularity and global flow). V is C^2 with |V(y)| <= C(1 + |y|) (U is continuous and o(|y|)), so Phi_s
is a global C^2 flow of diffeomorphisms. The equation gives grad P = -(1-c)U - G V in C^1, so P is C^2 and the curl
of grad P vanishes pointwise. Using curl[c (y·grad)U] = c Omega + c (y·grad)Omega and
curl[(U·grad)U] = (U·grad)Omega - (Omega·grad)U (div U = 0), the curl of the equation is the vorticity equation
    Omega + V·grad Omega = G Omega = S Omega   (pointwise; G Omega = S Omega because W Omega = Omega x Omega / 2 = 0).

Step 1 (backward orbits are trapped). Since U = o(|y|), there is R_b with |U(y)| <= c|y|/2 for |y| >= R_b, hence
V(y)·y >= (c/2)|y|^2 there and d|Y|^2/ds >= c|Y|^2 while |Y| >= R_b. So every backward orbit enters the closed ball
B := {|y| <= R_b} in finite backward time and stays there for all earlier times. In particular alpha(a) is a nonempty,
compact, connected, invariant subset of B, and N_V is a closed subset of B (compact).

Step 2 (alpha-limits lie in N_V). Let H = |V|^2/2 + P + c(c-1)|y|^2/2. Rewriting the equation as
(1-2c)V + Omega x V + grad H = 0 [CIV (3.29)] and dotting with V gives V·grad H = (2c-1)|V|^2 [CIV (3.31)], so
s -> H(Y(a,s)) is nonincreasing and strictly decreasing unless V(Y) = 0. On (-infinity, s_0] the orbit lies in B
where H is bounded, so H(Y(a,s)) has a finite limit h as s -> -infinity, and H = h on alpha(a). By invariance of
alpha(a), for z in alpha(a) the orbit of z stays in alpha(a), so H is constant along it, so V(z) = 0. Hence
alpha(a) is a subset of N_V. If N_V is countable, alpha(a) is a connected compact countable set, hence one point y_*.
Then Y(a,s) -> y_* as s -> -infinity.

Step 3 (self-similar Cauchy formula). Let J(a,s) = grad_a Y(a,s), so dJ/ds = (cI + G(Y)) J, J(a,0) = I.
Let Z(s) = e^{(1+c)s} Omega(Y(a,s)). By the vorticity equation, d/ds Omega(Y) = (V·grad Omega)(Y) = (G - I)Omega at Y, so
dZ/ds = (cI + G(Y)) Z, Z(0) = Omega(a). By uniqueness Z(s) = J(a,s) Omega(a), i.e.
    Omega(a) = e^{(1+c)s} J(a,s)^{-1} Omega(Y(a,s))   for all s   [CIV (3.22) in our notation].
Let s = -t with t >= 0 and B(t) := J(a,-t)^{-1}. Then dB/dt = B (cI + G(Y(a,-t))), so for any fixed vector eta,
w = B^T eta satisfies dw/dt = (cI + G^T) w and d|w|^2/dt = 2 w·(cI + S)w <= 2 (c + lambda_max(S(Y(a,-t)))) |w|^2.
Therefore
    |Omega(a)| <= exp( int_0^t [ lambda_max(S(Y(a,-t'))) - 1 ] dt' ) * |Omega(Y(a,-t))|.        (*)

Step 4 (vorticity-free basins). Let alpha(a) be contained in {y in N_V : lambda_max(S(y)) < 1} (for countable N_V:
lambda_max(S(y_*)) < 1). By compactness of alpha(a) and continuity of S there are eta > 0 and a neighborhood O of
alpha(a) with lambda_max(S) <= 1 - eta on O, and Y(a,-t) is in O for t >= t_1. Since Omega is bounded on B, (*) gives
|Omega(a)| <= C e^{-eta t} for all large t, so Omega(a) = 0. This proves the first part of Corollary L1'.
Remark: if Omega(y_*) != 0 at y_* in N_V, the vorticity equation at y_* gives S(y_*)Omega(y_*) = Omega(y_*), so
lambda_max(S(y_*)) >= 1. Thus points of N_V with lambda_max(S) < 1 automatically have Omega = 0.

Step 5 (contracting direction at points of E). Let y_* in N_V with lambda_max(S(y_*)) >= 1, and A := grad V(y_*) = cI + G(y_*),
tr A = 3c.
(i) If Omega(y_*) != 0: G(y_*)Omega(y_*) = Omega(y_*) (Step 0 at a zero of V), so A Omega = (1+c) Omega and the other two
eigenvalues of A have sum 3c - (1+c) = 2c - 1 < 0; at least one has negative real part.
(ii) If Omega(y_*) = 0: A = cI + S(y_*) is symmetric with eigenvalues c + lambda_i. Since tr S = 0 and lambda_max >= 1,
lambda_min <= -1/2, so c + lambda_min <= c - 1/2 < 0.
This proves the second part of Corollary L1'.

Step 6 (measure-zero basins at points of E, countable case). Let y_* be in E and let A have k >= 1 eigenvalues with
negative real part (counted with multiplicity), so the center-unstable spectral subspace E^{cu} (eigenvalues with
real part >= 0) has dimension 3 - k <= 2. For a C^1 (here C^2) vector field there is delta > 0 and a C^1 (at least
Lipschitz) local center-unstable manifold W^{cu}_delta of y_*, a graph over E^{cu}, with the property that every
backward orbit of V that remains in the closed ball B_delta(y_*) for all s <= 0 lies in W^{cu}_delta.
(Construction: modify V outside B_delta(y_*) by a cutoff so that the nonlinear part has small Lipschitz constant;
the global center-unstable manifold of the modified field is the set of points whose backward orbits grow at most
like e^{-eta s} as s -> -infinity, for a rate eta between 0 and the smallest |Re| of the stable eigenvalues; such
orbits include all bounded backward orbits; see Vanderbauwhede, "Centre manifolds, normal forms and elementary
bifurcations", Dynamics Reported 2 (1989), or Chicone, "Ordinary Differential Equations with Applications", 2nd ed.,
Ch. 4, for the center-manifold version; the center-unstable version is the same construction applied to the
dichotomy stable / center-unstable. Audit note: E^{cu} must be the sum of generalized eigenspaces for eigenvalues
with real part >= 0. A citable discrete-time form is the stable-center manifold theorem (Shub 1987, Thm III.7, restated
as Lee-Simchowitz-Jordan-Recht, COLT 2016, Thm 7) applied to the C^1 diffeomorphism F = Phi_{-1}: the center-stable
manifold of F at y_* has dimension 3 - k and contains every point whose forward F-orbit stays in a small ball. The
manifold need not be unique; the argument uses only existence and the trapping property.)
If Y(a,s) -> y_* as s -> -infinity, then there is an integer K >= 0 with Y(a,s) in B_delta(y_*) for all s <= -K, so
Y(a,-K) is in W^{cu}_delta and a = Phi_K(Y(a,-K)). Hence the basin {a : alpha(a) = {y_*}} is contained in the
countable union over K of Phi_K(W^{cu}_delta), each a C^1 image of a Lipschitz manifold of dimension <= 2, hence of
Lebesgue measure zero.

Step 7 (conclusion). If N_V is countable, R^3 is the countable disjoint union of the basins of the points of N_V
(Step 2). Basins of points with lambda_max(S) < 1 carry no vorticity (Step 4); basins of points of E have measure zero
(Steps 5, 6). So Omega = 0 almost everywhere, hence everywhere by continuity. Then curl U = 0 and div U = 0, so each
component of U is harmonic; U = o(|y|) gives U constant by Liouville; U -> 0 gives U = 0. QED.

Where c < 1/2 is used: Step 2 needs strict monotonicity of H (c != 1/2; strict decrease for c < 1/2); Step 5 needs c < 1/2 in both cases. For c > 1/2
Step 5(i) fails (the two remaining eigenvalues sum to 2c - 1 > 0), consistent with the absence of an obstruction
there. At c = 1/2 Step 2 fails (H is conserved along trajectories).
Hypotheses not used: no axisymmetry, no m = 2 symmetry, no local outgoing property, no finite energy beyond U = o(|y|),
no bound on ||grad^2 U||, no condition U(0) = 0 (the origin is not distinguished).

## 3. Remarks toward the uncountable case (v2, heuristic; SUPERSEDED by Theorem L2, section 7)

(a) A smooth curve Gamma in N_V: the tangent t satisfies A t = 0. If Omega != 0 at a point, the spectrum of A is
{0, 1+c, 2c-1} (Omega is not tangent since 1+c != 0). If Omega = 0 and lambda_max(S) >= 1, then A = cI + S is
symmetric and S t = -c t, so S has eigenvalues {-c, lambda_max, c - lambda_max} (trace zero) and A has
{0, c + lambda_max, 2c - lambda_max}, with 2c - lambda_max < 0. In both
cases, on a small compact regular patch of Gamma where these spectral conditions hold uniformly, Gamma is normally
hyperbolic with a one-dimensional stable normal bundle, and orbits whose alpha-limit set lies in that patch lie
locally in a two-dimensional center-unstable manifold: measure zero. This is local only: a global statement needs
uniformity along Gamma, control of the transition between the parts of Gamma with lambda_max(S) >= 1 and < 1, and
(for Step 4) the whole alpha-limit set to lie in the part with lambda_max(S) < 1.
(b) A smooth surface Sigma in N_V: A has two zero eigenvalues (tangent), so the third is tr A = 3c. If Omega != 0
somewhere on Sigma then 1 + c would be an eigenvalue, impossible for c < 1/2. So Omega = 0 on Sigma, S has eigenvalues
{-c, -c, 2c}, lambda_max = 2c < 1, and Step 4 applies: vorticity-free basins.
(c) Remaining gaps for a full obstruction: (i) degenerate points of N_V where normal hyperbolicity fails or the zero
set is not a manifold (cusps, crossings, accumulation points, Cantor-like zero sets of a C^2 field); (ii) alpha-limit
continua that meet E and also the set where lambda_max(S) < 1; (iii) uniformity of the local manifolds along
non-compact strata. If U were real analytic, N_V would be a compact semianalytic set with a finite Whitney
stratification, which removes (i) partially but not the degenerate points. The full search class of the task is not
covered.
(d) Numerical meaning (corrected in v2). L1 says nothing directly about residual floors. Counterexample to the v1
claim: U_eps = eps W with W divergence free, compactly supported away from 0, P = 0; V_eps has the single
nondegenerate zero 0 and the residual tends to 0 in every C^k norm, with the exact limit U = 0. What L1 does imply:
if a sequence of candidates at fixed c_l < 1/2 has relative residuals tending to zero, a fixed nontriviality
normalization, and enough compactness (uniform C^{2,alpha} bounds on compact sets, uniform tail bounds keeping
U = o(|y|) and decay, core location bounded), then a subsequence converges to an exact C^2 profile, which by L1 is
either trivial (excluded by the normalization if it passes to the limit) or has an uncountable stagnation set. So an
improving sequence must show at least one of: loss of compactness (derivative growth, core drift to infinity or
shrinking below resolution, amplitude escaping to the tail), or degeneration of the stagnation structure (zeros of
V merging into curves or surfaces, grad V becoming singular at zeros). These are the diagnostics to monitor. A
quantitative residual floor would need further estimates that are not proved.
(e) Affine example (from the referee): U = (-y_1/2 - a y_2, a y_1 - y_2/2, y_3), P = (1/8 + a^2/2)(y_1^2+y_2^2) - y_3^2
solves (E) for every c, has Omega = (0,0,2a), N_V = {0}, spec(grad V) = {c - 1/2 ± i a, c + 1}. It violates only the
sublinearity hypothesis, which shows that Step 1 is needed.

## 4. Relation to the literature (checked by the referee audit; bounded search)
- [CIV] Thm 3.9 assumes N_V finite and the local outgoing property at every point of N_V; the outgoing property forces
  lambda_min(S) >= -c, hence lambda_max(S) <= 2c < 1 at every zero, after which Step 4 applies globally. L1 drops the
  outgoing hypothesis and handles zeros with contracting directions by the measure argument of Step 6.
- [CIV] Thm 3.8 is Step 5(i) read in the outgoing case.
Exponent conversion for older papers: u = (T-t)^{-alpha/(1+alpha)} v((x-x_*)/(T-t)^{1/(1+alpha)}) gives
c = 1/(1+alpha); c < 1/2 iff alpha > 1; c = 2/5 iff alpha = 3/2.
- Chae, Comm. Math. Phys. 273 (2007) 203-215 (arXiv:math/0601060): Omega in L^p for every 0 < p < p_1 implies
  Omega = 0. Uses vorticity transport and the back-to-label map (so the transport mechanism is not new), but needs
  small-p integrability, which L1 does not assume. Does not imply L1.
- Chae-Shvydkoy, Arch. Ration. Mech. Anal. 209 (2013) 999-1017 (arXiv:1201.6009): velocity exclusions under L^p
  assumptions; vorticity theorem assumes strain -> 0 and Omega in L^p for some 0 < p < 3c. Does not imply L1.
- Bronzi-Shvydkoy, Indiana Univ. Math. J. 64 (2015) 1291-1302 (arXiv:1310.8611): triviality or matching energy
  growth under annular L^p growth assumptions for 0 < alpha < 3/2. Does not imply L1.
- Chae, maximum-principle paper (arXiv:1308.1051): needs grad U = o(1) and vorticity decay O(|y|^{-k}), k > 1/c.
- Chae-Wolf, Comm. Math. Phys. 376 (2020) (arXiv:1706.02020): discretely self-similar exclusion at c = 2/5 under
  finite energy and Type I bounds. Chae-Wolf, J. Nonlinear Sci. 33, 115 (2023): spatial constancy for alpha >= 3/2
  (c <= 2/5) allowing sublinear growth; only the abstract was accessible to the referee; its range does not cover
  2/5 < c < 1/2.
- Constantin-Ignatova-Vicol Thm 3.9 is the closest verified predecessor (finite N_V, local outgoing, (3.7), (3.8)).
- No checked result implies L1 under exactly its hypotheses (a bounded search, not a novelty certification).

## 5. Use in the campaign
v3: Theorem L2 (section 7) is a rigorous obstruction for the whole specified search class: time-independent,
single-center similarity profiles of the incompressible Euler equations on R^3, C^2 at every finite point, with
decaying velocity, for any 0 < c < 1/2 and any symmetry, stagnation-set geometry or tail structure. Its exact scope,
including what it does NOT cover, is in section 7.8. It predicts that no numerical branch at fixed c_l < 1/2 can
converge, under refinement with uniform derivative and tail control, to a nontrivial exact profile; section 8 states
the precise compactness consequence. It does not give a numerical value for any residual floor.

v2 text (kept): L1 is a "rigorous obstruction under explicit assumptions" (countable stagnation set, C^2, U = o(|y|), U -> 0;
informal proof, two independent audits). It does not cover the whole search class (uncountable stagnation sets are
not excluded), so it does not end the campaign. It changes what the numerics must test: the stagnation-set structure
of every c_l < 1/2 candidate (isolated zeros versus curves or surfaces, lambda_max(S) at each zero), and, for any
sequence with decreasing residual, the compactness diagnostics of section 3(d). It does NOT predict a residual floor
(section 3(d)).

## 6. Audit log
- 2026-10-23 06:31Z: the verifier wrote an independent proof (CONFIRMED under exactly C^2, U -> 0, 0 < c < 1/2,
  countable N_V), proving the measure-zero basin step by a weighted contraction for a Lipschitz graph.
- 2026-10-23 06:48Z: independent referee audit (question stagobs1): PROOF CORRECT for L1 and L1'. Corrections:
  Cauchy formula citation is CIV (3.22); Step 6 should be stated with generalized eigenspaces and the trapping
  property (reference: the stable-center manifold theorem, Shub, Global Stability of Dynamical Systems (1987),
  Thm III.7, as restated in Lee-Simchowitz-Jordan-Recht, COLT 2016, Thm 7, applied to F = Phi_{-1}); non-uniqueness
  of center-type manifolds does not matter; section 3(a) needs local qualifications (normal hyperbolicity only on
  small regular patches; Step 4 needs the whole alpha-limit set in the good part); section 3(d) of v1 was false
  (replaced above). Literature as in section 4.
- 2026-10-23 07:02Z: the verifier wrote, before seeing any referee answer, an independent proof removing the
  countability hypothesis (capture near an equilibrium arc by stable/unstable variation of constants; section 7.4,
  second argument). Its verdict was OPEN until a second proof existed.
- 2026-10-23 07:04Z: referee answer to question uncount1: a full proof of the same statement with a different capture
  argument (Bernoulli gradient inequality of exponent 1/2; section 7.4, first argument) and an elementary proof of
  the local null-graph lemma. The referee could not reach the internet; its literature remarks are limited to the
  notes it was given.
- 2026-10-23 07:08Z: the verifier cross-audited the referee proof step by step: CONFIRMED for the exact C^2 sublinear
  theorem (both capture arguments, the topology lemma, the finite cover, the graph lemma, scope at c = 1/2).
  Literature priority OPEN (no exhaustive search).
- 2026-10-23 07:03Z: referee answer to question floor1: the compactness corollary is correct with a fixed modulus of
  continuity for D^2 U; counterexample without it; no explicit epsilon_0. Used in section 8 (where L2 removes the
  stagnation-margin hypothesis that floor1 still needed).
- 2026-10-23 07:14Z: lead check of both L2 proofs, line by line (identities, rank lemma, topology lemma, both capture
  estimates, graph lemma with the weighted norm, finite cover, vorticity elimination, Liouville). No gap found. The
  write-up in section 7 is the lead's; it is sent for a further adversarial audit (question l2adv1) and a scope audit
  against the task text (question l2scope1).
- 2026-10-23 07:19Z: presentation repairs flagged by l2adv1 while running: 7.3 shrinks the chart to exclude a second
  point of alpha(a); 7.4 chooses q near p so that the simple real eigenvalue pattern of A(p) persists (q need not be
  in E); the parenthetical remark on rank 2 zeros outside E is now argued case by case.
- 2026-10-23 07:24Z: scope audit l2scope1: L2 covers the entire primary exact-profile class (smooth, globally decaying,
  m = 2, 2/5 < c_l < 1/2, constant axial drift removed), and c_l = 2/5; it does not decide c_l = 1/2 or c_l > 1/2.
  Permitted status: RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS, with the scope stated. Corrections applied 07:25Z:
  7.8 rewritten (unbounded sublinear growth is covered; total energy, not local energy; primary versus secondary
  targets; raywise decay is not global decay); "this argument gives no obstruction" at c >= 1/2; section 8: the
  D^3 U bound is a sufficient compactness control, not the only one, and the numerical meaning keeps its quantifiers.
- 2026-10-23 07:25Z-07:26Z: an editing error by the lead briefly truncated this file (sections 2 end to 7.7 missing
  for about one minute); restored at 07:26Z by replaying the recorded edits on the archived v2. Readers of the file
  during that minute saw an incomplete version.
- 2026-10-23 07:28Z: hostile referee audit l2adv1 (read the 07:19Z text, after the 7.3/7.4 repairs): PROOF CORRECT WITH
  REPAIRABLE GAPS; no counterexample, no missing hypothesis on the stagnation set; all exact families tested
  (rotating strain, stagnation line, rank-one affine, shears, Beltrami, periodic and 2D three-component fields,
  singular axial fields) are consistent with L2. Its two repairs are applied: 7.5 now fixes the direct-sum norm
  |z|_* (the projections need not be orthogonal), and the second argument of 7.4 has an explicit thin box and
  first-exit argument. The second argument is redundant; the first (Bernoulli) argument is complete as written.

## 7. Theorem L2: arbitrary stagnation sets (v3)

Theorem L2. Let 0 < c < 1/2. Let U in C^2(R^3; R^3) and a function P solve
    (1-c)U + (c y + U)·grad U + grad P = 0,    div U = 0    pointwise on R^3,
with U(y) = o(|y|) as |y| -> infinity. Then Omega = curl U = 0 everywhere and U is constant. If U -> 0 at infinity,
then U = 0 and P is constant.

Remarks on the hypotheses. P is automatically C^2, because grad P = -(1-c)U - G V is C^1. A constant axial drift C e_3
in the transport is removed by the shift Y = y + (C/c) e_3 (EQUATIONS.md 1.2), which preserves C^2 and sublinearity,
so L2 holds for (E_C) too. Nothing is assumed about the zero set N_V of V = c y + U (its cardinality, regularity or
stratification), about symmetry, analyticity, finite energy, the decay rate, or the angular structure of the tail.

Notation as in section 2: A := grad V = cI + G, tr A = 3c; E := {p in N_V : lambda_max(S(p)) >= 1}; x(t) := Y(a,-t),
t >= 0, the backward orbit; alpha(a) its backward limit set; kappa := 1 - 2c > 0; C_w v := w x v.

Steps 0-3 of section 2 and Corollary L1' do not use countability. They give: a complete C^2 flow; every backward
orbit is eventually in the ball B and stays there; alpha(a) is nonempty, compact, connected, invariant, contained in
N_V, and H = h(a) on alpha(a), where h(a) = lim H(x(t)); and Omega(a) = 0 unless alpha(a) meets E. Put
    W := {a : alpha(a) meets E},    Z := {Omega != 0}.
Then Z is a subset of W. The proof shows that W has Lebesgue measure zero. Z is open, so Z is empty.

7.1 (Bernoulli gradient). The Bernoulli form of the equation [CIV (3.29); EQUATIONS.md 1.3(c) with R_m = 0] is
    grad H = -B V,    B := kappa I + C_Omega.
The symmetric part of B is kappa I, so v·Bv = kappa|v|^2, B is invertible, and
    kappa |V| <= |grad H| <= (kappa^2 + |Omega|^2)^{1/2} |V|.
Hence {grad H = 0} = N_V. At p in N_V, differentiating grad H = -B V (B is C^1, V(p) = 0) gives
D^2 H(p) = -B(p) A(p), so ker D^2 H(p) = ker A(p) and the two ranks agree.

7.2 (rank at E). Let p in E. Then rank A(p) >= 2, and A(p) has a positive eigenvalue and an eigenvalue with negative
real part. Proof: if Omega(p) != 0, A Omega = (1+c) Omega and the other two eigenvalues sum to 2c - 1 != 0, so 0 has
algebraic multiplicity at most 1, and one of the two has negative real part. If Omega(p) = 0, A = cI + S(p) is
symmetric with largest eigenvalue >= 1 + c and smallest <= c - 1/2 < 0 (tr S = 0), so again 0 has multiplicity at
most 1. If rank A(p) = 3, p is an isolated point of N_V (inverse function theorem). If rank A(p) = 2, two rows of
A(p) are independent; the common zero set of the two corresponding components of V is, in a neighborhood O of p, an
embedded C^2 arc gamma through p, and N_V ∩ O is a closed subset of gamma. Shrinking O, rank A >= 2 on O (lower
semicontinuity of rank).

7.3 (topology lemma). Suppose alpha(a) contains p in E and is not {p}. A connected set with two points has no
isolated points, so rank A(p) = 2. Then alpha(a) contains a nondegenerate subarc J of gamma with endpoint p.
Proof: take a tubular chart Psi(xi, z) of a neighborhood of p in O, xi in (-delta, delta), z in a disk, with
Psi(xi, 0) = gamma(xi), gamma(0) = p; fix r in alpha(a) with r != p and shrink the chart (a neighborhood of p)
so that r lies outside its closure. If neither [0, eps) nor (-eps, 0] maps
into alpha(a) for any eps > 0, choose xi_- < 0 < xi_+ with gamma(xi_±) not in alpha(a) and a thin tube
D = Psi((xi_-, xi_+) x D_rho) whose closure lies in the chart. Points of N_V near p lie on gamma, so the lateral boundary
of D misses N_V, and the end caps meet N_V at most in gamma(xi_±). Hence alpha(a) ∩ (boundary of D) is empty, and
alpha(a) ∩ D is nonempty (it contains p), relatively open and closed, and misses r. This contradicts connectedness.
No local connectedness of alpha(a) is used.

7.4 (capture: a nonsingleton alpha-limit set cannot meet E). Let J be as in 7.3 and q an interior point of J, chosen
so close to p that the spectral picture of A(p) persists: at p (rank 2) A(p) has three simple real eigenvalues, one
positive, one negative and 0 (7.2: the nonzero ones are 1 + c and 2c - 1 if Omega(p) != 0; if Omega(p) = 0, A(p) is
symmetric). Simple real eigenvalues of a real matrix depend continuously on it and stay real, and V = 0 on J gives a
zero eigenvalue at q; so A(q) has simple real eigenvalues lambda_s < 0 = lambda_0 < lambda_u. (q need not lie in E;
only this sign pattern is used below.) Near q,
N_V coincides with J (it lies on gamma, and J is a subset of N_V), J is a C^2 arc, rank A = 2 on J, and
ker A(y) = T_y J (V = 0 along J gives A t = 0 for the tangent t). H = h(a) on J, since J lies in alpha(a).
First argument (referee). For y near q let pi(y) be the nearest point of J; y - pi(y) is normal to J at pi(y). A(pi)
is injective on the normal plane with a uniform lower bound 2m > 0 near q, and V(y) = A(pi)(y - pi) + O(|y - pi|^2)
uniformly (V in C^2), so |V(y)| >= m|y - pi(y)|. Since grad H(pi) = 0 and H(pi) = h, Taylor gives
|H(y) - h| <= C|y - pi(y)|^2. With 7.1:
    |H(y) - h|^{1/2} <= C_0 |grad H(y)|  and  |grad H(y)| <= M |V(y)|   on a closed ball B_{r0}(q).
Let e(t) = h - H(x(t)) >= 0; e decreases to 0 and e' = -kappa|V(x)|^2 = -kappa|x'|^2. Wherever e > 0 and x(t) is in
B_{r0}(q), -(e^{1/2})' = kappa|x'|^2 / (2 e^{1/2}) >= (kappa / (2 C_0 M)) |x'|, so any orbit segment [t_0, t_1] inside
that ball has length at most (2 C_0 M / kappa) e(t_0)^{1/2}. Since q is in alpha(a), there is t_0 with
|x(t_0) - q| < r0/4 and (2 C_0 M / kappa) e(t_0)^{1/2} < r0/4. Then the orbit never leaves B_{r0/2}(q) after t_0, has
finite length, and converges; its limit is q, so alpha(a) = {q}, which contradicts J being a subset of alpha(a). (If e
vanishes at some time, the orbit is an equilibrium from then on: same conclusion.) No analyticity is used; an
indefinite transverse Hessian is allowed.
Second argument (verifier). In C^2 coordinates (s, u, z) flattening J to the z-axis, with s, u along the stable and
unstable eigenvectors of A(q) (eigenvalues lambda_s < 0 < lambda_u from the first paragraph of 7.4), the field is C^1 with s' = lambda_s s + f_s, u' = lambda_u u + f_u, z' = g,
|f_s| + |f_u| <= eps(|s| + |u|), |g| <= K(|s| + |u|). On any time segment inside a small box with |s|, |u| <= eta,
variation of constants (stable part forward from the left end, unstable part backward from the right end) gives
int (|s| + |u|) dt <= 2 eta / (beta - 2 eps), beta = min(-lambda_s, lambda_u), so the drift along J is at most
2 K eta / (beta - 2 eps), independent of the segment length (in backward time the roles of s and u are interchanged;
the bound is the same). Trapping: take the box |s|, |u| < eta, |z| < delta with closure inside the chart of 7.3, where
the only zeros are on the axis; choose eps < beta/2 and then eta with 2 K eta / (beta - 2 eps) < delta/2. The compact
transverse boundary max(|s|, |u|) = eta has positive distance from N_V, and dist(x(t), N_V) -> 0, so late points do
not lie on it; a late return with |z| < delta/4 cannot first leave through a z-face, since its total axial drift is
< delta/2. So the tail is trapped; the speed is at most a constant times |s| + |u|, so the tail has finite length and
converges to q, and alpha(a) = {q}. Same contradiction.
Conclusion of 7.3-7.4: for every a in W, alpha(a) = {p} for one p in E, i.e. Y(a,s) -> p as s -> -infinity.
(Not needed for L2: a nonsingleton alpha-limit set contains no zero with rank A >= 2. Rank 3 zeros are isolated.
At a rank 2 zero outside E, Omega = 0 (a vortical zero is in E), so A is symmetric with eigenvalues 0, mu_1, mu_2,
mu_1 + mu_2 = 3c > 0: if one mu is negative the second argument applies verbatim; if both are positive, the same
variation-of-constants bound with both normal coordinates treated as unstable applies. So such a set lies in
{rank A = 1}, where tr A = 3c forces spec A = {0, 0, 3c}, hence Omega = 0 (1 + c != 3c), spec S = {-c, -c, 2c} and
lambda_max(S) = 2c < 1.)

7.5 (local null graph; Step 6 restated without manifold theory). For each p in E there is an open neighborhood B_p
of p such that T_p := {b : Y(b,s) in B_p for all s <= 0} lies in a Lipschitz graph over a subspace of dimension
<= 2, hence has Lebesgue measure zero. Proof (referee; the verifier's L1 proof uses the same weighted contraction):
for X = -V, L = DX(p) = -A(p) has an eigenvalue with positive real part; split R^3 = E^cs + E^u (real generalized
eigenspaces, dim E^cs <= 2) and use the norm |z|_* = |z_cs| + |z_u| (Euclidean on each summand), so both spectral
projections have norm <= 1 (with the Euclidean norm on R^3, keep the projection constants instead); all norms below
are |.|_*; choose beta below the smallest positive real part, eps = beta/4, eta = beta/2, M_0 with
|e^{-tL_u}| <= M_0 e^{-beta t}, |e^{tL_cs}| <= M_0 e^{eps t} (t >= 0); on a small convex neighborhood the nonlinear
part has Lipschitz constant l. For two forward X-orbits w = z - z~ staying in the neighborhood, the cs part by
variation of constants from 0 and the u part by the terminal formula w_u(t) = -int_t^infinity e^{(t-s)L_u} r_u ds give,
for D_* = sup e^{-eta t}|w(t)|, D_* <= M_0|w_cs(0)| + M_0 l (1/(eta - eps) + 1/(beta - eta)) D_*. For l small,
|w_u(0)| <= D_* <= 2 M_0 |w_cs(0)|: projection to E^cs is injective on T_p with Lipschitz inverse.

7.6 (finite cover). E is compact (closed in the compact N_V). Choose open U_p with closure in B_p and p_1, ..., p_k
with E covered by U_{p_1}, ..., U_{p_k}. For a in W, its backward limit p lies in some U_{p_i}, so there is an integer
n >= 0 with Y(a,s) in B_{p_i} for all s <= -n; then Y(a,-n) is in T_{p_i} and a = Phi_n(Y(a,-n)). Hence
    W is contained in the union over i <= k and n >= 0 of Phi_n(T_{p_i}),
a countable union of null sets (each Phi_n is a C^2 diffeomorphism). So W is null. Uncountably many points of E cause
no difficulty: only finitely many neighborhoods and countably many flow times are used.

7.7 (conclusion). Z is open and contained in the null set W, so Z is empty and Omega = 0. With div U = 0, every
component of U is harmonic; the interior gradient estimate |grad u(x_0)| <= (3/R) sup_{B_R(x_0)} |u| and U = o(|y|)
give grad U = 0. If U -> 0, U = 0 and grad P = 0. QED.

Where c < 1/2 is used: kappa > 0 (Step 2, 7.1, 7.4) and the contracting direction at points of E (7.2, 7.5). At
c = 1/2, kappa = 0, H is a first integral and B = C_Omega is singular: this argument gives no obstruction, consistent
with the numerical profile at c = 1/2 reported in the literature (arXiv:2609.10867; not checked here). For c > 1/2, on
a vortical stagnation arc spec A = {0, 1 + c, 2c - 1} has no contracting direction and 7.5 fails: this argument gives
no obstruction. (Failure of the argument is not evidence that profiles exist there.)

7.8 Scope (rewritten 07:25Z after the scope audit l2scope1). L2 applies to exact time-independent solutions of (E), or
of (E_C) after removal of the constant axial drift, on all of R^3, with 0 < c < 1/2, U in C^2(R^3) and U(y) = o(|y|).
It concludes that U is constant; if U -> 0, then U = 0 and P is constant.
These hypotheses include the entire primary exact-profile class of the task: smooth, globally decaying, genuinely
two-fold (m = 2) profiles with 2/5 < c_l < 1/2, the prescribed isotropic stationary similarity ansatz centered on the
z-axis, and the permitted constant axial recentering. The same exclusion holds at c_l = 2/5 and for every 0 < c < 2/5.
No extra assumption is needed on the stagnation set (isolated points, curves, surfaces, Cantor-like sets, off-axis
pairs), axis vorticity, paired off-axis peaks, angular tail structure, algebraic decay rate (any global decay, however
slow, implies sublinearity), analyticity at infinity, or total profile energy (every C^2 field has finite energy on
bounded sets; U in L^2(R^3) is not required). Decay along rays only, without uniformity in the direction, is not global
decay and need not imply sublinearity; the task requires global decay.
L2 does NOT decide the c_l = 1/2 calibration or candidates with c_l > 1/2, which the task treats as possible secondary
results. It is a complete obstruction to the primary exact-profile target, not to every secondary possibility.
Outside the hypotheses: profiles failing C^2 at some finite point (e.g. only C^{1,alpha}; such a field is also not a
smooth profile in the sense of the task); velocity not o(|y|), e.g. nonconstant affine backgrounds (unbounded sublinear
growth IS covered); time-dependent, discretely self-similar, rotating, anisotropic or multi-center ansatzes.
L2 gives no numerical acceptance threshold for approximate profiles; section 8 gives a nonconstructive positive floor
only under additional uniform bounds and normalization. Neither establishes stability, a construction from
finite-energy data, or a general obstruction to Euler or Navier-Stokes blowup by other mechanisms.

## 8. Approximate solutions: a non-quantitative floor (from floor1, simplified by L2)

Fix 0 < c < 1/2, d = 1 - 1/c, K >= 1. Let F(c, K) be the set of U in C^3(R^3) with div U = 0,
|D^j U(y)| <= K <y>^{d-j} for j = 0, 1, 2, ||D^3 U||_inf <= K, and the scale gauge ||D^2 U||_inf = 1 (admissible:
U_a = aU(y/a) has ||D^2 U_a||_inf = ||D^2 U||_inf / a). Claim: there is eps_0(c, K) > 0 with
||(1-c)U + (cy + U)·grad U + grad P||_inf >= eps_0 for every U in F(c, K) and every P in C^1.
Proof: otherwise a sequence with residual -> 0 has, by Arzela-Ascoli, a C^2_loc limit U that is divergence free and
satisfies the envelopes; the pressure is reconstructed from the curl-free limit of (1-c)U_n + G_n V_n; the
normalization survives because |D^2 U_n| <= 1/2 outside the fixed radius (2K)^{1/(2-d)}; so U is a nonzero exact C^2
decaying profile, contradicting L2. (floor1 proved the same statement before L2 under an extra uniform stagnation
margin |V| + |det A| >= delta on the trapping ball; L2 makes that margin unnecessary.)
Notes from floor1, checked by the lead: (i) some uniform compactness control on D^2 U cannot be omitted (a bound on
D^3 U, a common Hoelder modulus, or any common modulus of continuity of D^2 U suffices; these are sufficient, not the
only possible, conditions). Without it the floor fails:
U_l = l^2 W(y/l), W smooth, compactly supported, divergence free, P = 0, has ||D^2 U_l|| = 1, all envelope bounds for
a fixed K, and residual O(l^2) -> 0, while ||D^3 U_l|| -> infinity; (ii) eps_0 is not computed; the proof gives no
numerical value; (iii) a joint floor holds for ||R_m||_inf + ||div U||_inf if exact incompressibility is dropped.
Numerical meaning (quantifiers as in l2scope1). A sequence of normalized divergence-free fields at one fixed c < 1/2
whose whole-space L^inf momentum residual tends to zero must eventually leave every class F(c, K), K fixed: its derivative bounds, tail envelope or normalization must degenerate (small scales, amplitude
escaping to the far field or collapsing, growth toward an affine field). A decreasing residual alone proves nothing:
it may approach a positive floor whose value is unknown. The statement does not apply directly to sampled residuals,
truncated-domain losses or exponent sequences approaching 1/2, and it does not say which bound fails.
