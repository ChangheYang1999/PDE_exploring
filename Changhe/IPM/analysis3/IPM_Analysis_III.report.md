# S2 theory report: the full-plane IPM self-similar profile with x^2 y leading term (case 1, candidate X3)

Status: PARTIAL, NOT SOLVED. No unconditional existence theorem was reached. A conditional existence theorem and the
linear theory it rests on are proved and confirmed by the independent verifier; its two hypotheses remain open.

Run record: start T0 = 2026-10-28T00:20:16Z (logged), end T_end = 2026-10-28T18:22:05Z, elapsed 18 h 01 min 49 s. The
planned 18-hour window ran to its cap; actual session times are in section 8.

## Summary

Verdict. No complete rigorous a posteriori existence theorem near the S2 profile (normalization 3 c_l - c[rho] = 1) is
established by any of the four avenues, and no sharp global inverse constant is claimed. Nothing proved here suggests nonexistence;
every obstruction found concerns a particular norm or method. Record numbers V001, V002, ... cite the verifier's record.

Proved (THEOREMS unless marked; constants finite but qualitative unless a number is given):
- Linear theory. The full normalized linearization in the moving-tail chart (nonlocal coupling, strain normalization, free cubic coefficient)
  is Fredholm of index 0 from the jet-plus-remainder space Z (weight |cos theta|^(-2a) e^(mu_a(t)), a = 17/4) to Y
  (Theorem C', V047, V049 to V053, V077, V086) and on high variable-order domains of order between 41/20 and 25/4
  (V151, V152); so it is invertible if and only if it is injective. For the exact moving-tail family the low and high
  inverses are uniformly bounded on a small ball once the base low operator is injective (V170); the nonlinear term
  satisfies the two-norm product and difference bounds (V073, V076, V176).
- Theorem E (CONDITIONAL THEOREM, V178): (I) base low injectivity and (S) K_H eta_0 <= r <= r_*, K_L C K_H eta_0 < 1
  give an exact profile, C^(1,alpha) off the origin for alpha < 1/20, with cubic jet (1 + J) x^2 y and far field
  r^(1/ell) Theta + O(r^(-1/2)); if |J| < 1 a scaling makes the leading term exactly x^2 y.
- Local inverses: origin saddle with the sharp constant 1/kappa_0 (Theorem O); ||T_R^(-1)|| <= 2/5 for the remainder
  transport; localized inverses onto C^alpha_2 at the origin for every alpha < 1 with the complete normalized coupling,
  whose norm is comparable to delta^2, sharp (V203 to V207, V219); the actual source operator on C^alpha_b intersected
  with L^2 for every 0 < alpha < 1 (V213 to V215).
- Obstructions, by explicit counterexamples: isotropic C^alpha at the saddle for alpha > 1/D (about 0.0469); a fixed
  cubic coefficient (index -1); semilinear fixed-point maps in the Hoelder norms considered (a quasilinear scheme is
  not excluded); any global Hoelder inverse onto C^alpha_2 intersected with L^2(w_gamma), gamma > 4k (V241, V247),
  onto Z_sc (V243, V249), onto Z_2 for alpha > 1/2 (V256, V262, V257, V265); transport alone onto Z_2 or Z_cof for
  alpha >= 1/10 (V266, V272). On Z_cof a global inverse is OPEN.

Certified numbers (ball arithmetic from the original data, independently recomputed): 15.726087821623500282 < c[X3]
< 15.726087821623500289 (V018); axis rate >= 5.5752 (V077); margins m_a >= 3 (V259), radial >= 5/2 (V086), decoupled
family (4, 0.3) >= 1.2501 (V191); residual 6049.11 < ||F||_Y < 8601.42 (V164), 3.270 < ||F||_(Y_a) < 485.632 (V174,
V179), and 3.866e10 < eta_* < 6.321e129 in one fixed high norm (V192, V182; the upper end is a loose majorant).
Finite-section bounds sigma_min >= 4.3337e-7 (V066), >= 0.020685 (V200), >= 0.510914 (V081) hold only if the exported
entry balls enclose the exact pairings, and bound finite sections, not the continuum operator.

Remaining gap. The first missing inequality is (I): a certified injectivity, with a quantitative bound
||h||_Z <= K_L ||L h||_Y, of the explicit base low operator. Then (S) needs explicit r_*, K_H, K_L, C and a trial whose
high residual eta_0 is small; the lower bound 3.866e10 gives no smallness, and with uncomputed constants it neither
verifies nor refutes (S). Constant-free necessary tests (CONDITIONAL THEOREMS, V184, V185, V194): one exact iteration
step must reduce the low residual, and ||R_d|| > 1956082280 |c[d]| for every admissible direction with c[d] != 0; a
heuristic estimate, not a bound, indicates that the archived trial fails them. Closest route: Avenues I and III, with
Avenue IV only for the complement (6.5). Section 0 answers each question of the task; 6.2 lists every open item.

## Reading guide

This report is self-contained. Proofs, computations, code and data are in the accompanying artifacts listed in
section 7. Verification records are cited by number (V001, V002, ...); they are the entries of the accompanying
verification record, each with claim, method, result, verdict and evidence. Some results were also checked by an
independent audit or by an external referee (a second model); those checks are described where they are used.

Labels used throughout:
- THEOREM: a complete proof exists and the independent verifier has CONFIRMED it (record number given; in the short
  answers of section 0 the record numbers are in the section cited in parentheses).
- CONDITIONAL THEOREM: a checked implication whose hypotheses are named and not all verified.
- DERIVED: a proof written by the theory author or by the verifier, with independent checking pending (for a
  verifier proof: confirmed by its own derivation, outside audit pending).
- NUMERICAL: a floating-point observation. It is never a bound.
- OPEN: not established.
- REFUTED: shown false, with the counterexample.
A statement is called a theorem in this report only if it has a CONFIRMED verdict.

## 0. Verdict

A complete nonlinear existence theorem is NOT established. What is established is a conditional existence theorem
(Theorem E, CONDITIONAL THEOREM, V178): if the base low linearization of the exact moving-tail family is injective and
one smallness inequality between the high norm of the residual and the (qualitative) inverse, radius and difference
constants holds, then an exact self-similar profile with cubic jet (1 + J) x^2 y exists near the trial, and after a
scaling its leading term is exactly x^2 y provided |J| < 1. Neither hypothesis
is verified, so this is not an unconditional existence proof for the actual trial. Nothing found in this work proves or
suggests that no exact solution exists near X3. Every obstruction found is an obstruction to a particular norm or
method.

In brief:
1. Unconditional (THEOREMS, for the actual normalized modal trial). The full normalized linearization, with its
   nonlocal coupling, the strain normalization and a free cubic coefficient, is Fredholm of index 0 in a low
   anisotropic weighted L^2 realization (V047 to V055, V077, V086) and in a high realization of variable Sobolev order
   between 41/20 and 25/4 (V151, V152). The same holds uniformly for the operators of the exact moving-tail family on
   a small ball of corrections, and their low and high inverses are uniformly bounded as soon as the base low operator
   is injective (V170; for the decoupled low weights V175). The nonlinear term satisfies the low/high product and
   difference bounds of a two-norm iteration (V073, V076, V176), and the moving-tail iteration theorem holds (V062).
   The residual of the trial is enclosed in the low norm: 6049.11 < ||F||_Y < 8601.42 (V164), and 3.270 < ||F||_(Y_a) < 485.632
   in the decoupled weights (V174, V179).
2. Conditional (CONDITIONAL THEOREM, V178). Theorem E (section 6.2 item 6): (I) base low injectivity and (S) the
   smallness condition K_H eta_0 <= r <= r_*, K_L C K_H eta_0 < 1 imply an exact profile, C^(1,alpha) off the origin
   for alpha < 1/20, with cubic jet (1 + J) x^2 y and far field r^(1/ell) Theta + O(r^(-1/2)); if |J| < 1 a scaling gives
   leading term exactly x^2 y with the same speed and far exponent.
3. Open. (I), and every number in (S): the radius r_*, the inverse constants K_H and K_L and the difference constant C,
   which come from compactness arguments, and a useful value of the high residual norm eta_0: in an explicitly fixed
   equivalent high norm the certified enclosure is 3.866e10 < eta_* < 6.321e129 (V192, V182). The upper end is a
   deliberately loose majorant; the lower end comes from the fifth derivatives of the weighted axis trace at two points.
4. Ruled out, each by an explicit counterexample confirmed by the verifier: bounded inverses in
   isotropic and radial weighted formulations, the isotropic C^alpha inverse of the frozen saddle for
   alpha > 1/D (about 0.0469), the transfer of the frozen Hoelder estimate by a conjugacy, semilinear perturbative
   fixed-point maps in the Hoelder solution norms considered, in which the explicit packets are bounded (a
   quasilinear Hoelder scheme is not excluded), a fixed
   cubic coefficient (index -1), the integer axis order and the
   sharp cone-sum high space, a one-order smoothing of the coupling, a forward isomorphism of equal orders, and
   variable-order Kato-Ponce commutator bounds, and a global Hoelder inverse (even surjectivity) on the common
   target C^alpha_2 intersected with L^2(w_gamma), by two far-field mechanisms (the second also for every
   gamma > 4k and on E_2 itself), on the scaled isotropic target Z_sc, by a third, and on the scaled quadratic-axis
   target Z_2 for every alpha > 1/2, by a simple turning height of the axis rate; also the surjectivity of the
   transport T alone onto Z_2 and onto the joint-cofactor target Z_cof for every alpha >= 1/10, by cusps at the
   source (this is not a statement about A_0), and the continuity at 0 of the semilinear map in the graph norms on
   Z_cof (sections 2 to 4 and 6.6).
5. Closest route: Avenues I and III together (section 6.5). What separates it from a proof is a certified injectivity
   of one explicit low operator, with explicit constants for the radius, the inverses and the difference bound, and a
   trial whose residual is small in the high norm; the present residual is pointwise small but concentrated in a thin
   angular layer at the vertical axis. A necessary condition needs no constant: one exact step of the iteration must
   reduce the low residual norm, since the ratio bounds the contraction factor from below (CONDITIONAL THEOREM, a
   necessary test under (I) and (S), V184, section 6.5). Two sharper tests of this kind need no constant either
   (CONDITIONAL THEOREMS, V185, V194);
   a heuristic estimate, not a bound, indicates that the archived trial fails them because its high residual norm is
   dominated by the knot-scale structure of the spline background (section 6.5 item 10).

Answers to the required questions (labels as above; the details and proofs are in the sections cited).

Avenue I (L^2-based; section 2).
- Strongest rigorously valid weighted inverse estimate. For the full normalized linearization: Fredholm of index 0
  from the jet-plus-remainder space Z to Y (Theorem C', THEOREM, V047 with V049 to V053, V077, V086), and on the high variable-order graph domains
  (THEOREM, V152), so it is invertible if and only if it is injective; injectivity is OPEN and no quantitative inverse
  bound for the full operator is proved. Quantitative inverses hold for the frozen and partial operators: the origin
  saddle with the sharp constant 1/kappa_0 (Theorem O), the frozen coupled source, and the remainder transport with
  ||T_R^{-1}|| <= 2/5 (THEOREMS; 2.1).
- Older obstructions. The degree-2 centre quasimodes and the nonclosed cubic coefficient are evaded by making the
  y-axis jet a coordinate with angular exponent a > 5/2; the radial moment gap, the non-closability of the strain on
  radial graphs, the negative saddle energy, the source Sobolev window (order below about 3.5785) and the rule that a finite
  section residual is not an inverse bound still apply to the methods they concern (table in 2.2).
- Consistent domain. Yes: Z = E B (+) D_R with the weight |cos theta|^(-2a) e^(mu_a(t)), a = 17/4, a free cubic
  coordinate and the strain bordering; the residual lies in the target, the nonlinear term satisfies the low/high
  bounds, and the high space embeds in the low one (THEOREMS; 2.3, 2.4).

Avenue II (C^alpha-based; section 3).
- Direct C^alpha control of h. At the origin saddle and the source points, yes, in anisotropic classes (THEOREMS);
  at infinity in scaled weighted classes (DERIVED for the frozen far window; for the actual exterior operator on
  Z_sc, Z_2 and Z_cof, THEOREMS, see below). At the origin this includes the complete normalized localized
  coupling and the actual transport inside a small disk: the localized whole-plane operator is invertible from its
  maximal domain onto C^alpha_2 for every alpha < 1 and small delta (THEOREMS; the cubic coordinate is not closable
  in that graph norm). Globally, both local inverses, after their cutoffs, act on a common target Y, C^alpha_2
  intersected with L^2 of the weight (1 + |X|^2)^(-gamma/2), gamma > 4k, which contains the residual; for every
  gamma > 4k, and on E_2 itself, the complete coupling is bounded and the full chart operator is closed on its
  maximal domain (THEOREMS), but the cutoff parametrix error of the specified single patch is not compact (THEOREM;
  cancellation in a sum of patches is not excluded by it), and the full operator is not even onto Y, with an
  infinite algebraic cokernel (THEOREM, two independent far-field mechanisms), so Y is not
  a valid global target. On a candidate target Z_sc with scaled far norms the complete coupling is bounded and the
  full operator is closed (THEOREM), and the exterior operator is invertible (THEOREM). But the full operator is not
  onto Z_sc either (THEOREM, V243 with its independent audit V249): transverse powers
  |x|^sigma along the outgoing vertical axis are not in its range. On a second candidate Z_2 with scaled quadratic
  control on every annulus the residual lies in it, the complete coupling is bounded, the full operator is closed
  and the exterior operator is invertible (THEOREM, V245, V254). At a simple turning height of the axis rate,
  however, T, A_0 and L_ren are not onto Z_2 for alpha > 1/2 (THEOREM: V256, a verifier proof with an
  original-data interval certificate, independent audit recorded as V262, gives alpha > 1/2 for T and alpha > 2/3
  for A_0 and L_ren; a stronger divided velocity bound, V257: U_1[x^2 g]/x is jointly C^alpha on bounded x-strips for g compactly supported, even in x, bounded and
  uniformly C^alpha in y, verifier proof, independent audit recorded as V265, extends the statement for A_0 and L_ren
  to every alpha > 1/2; alpha <= 1/2 OPEN for A_0 and L_ren). A third candidate Z_cof, h = x^2 g with g in a scaled joint C^alpha, carries the mapping,
  the residual, closed domains and an actual exterior inverse for every alpha < 1, and excludes the turning-height
  forcings (THEOREM, V261, verifier proof, independent audit recorded as V268); the nonlinear derivative loss persists on it
  (THEOREM, V264, V271). Transport alone is not onto Z_2 or Z_cof for alpha > 1/A_s (A_s, about 10.15, the expanding rate
  of V at the source), so for every alpha >= 1/10, by cusps at the source (THEOREM, V266, verifier proof, independent audit recorded as V272; this concerns T only, not
  A_0 or L_ren). A global inverse on Z_2 or Z_cof, the
  matching across the middle annuli, and hence a global Hoelder inverse, are OPEN, and the
  transfer of the frozen estimate by a conjugacy is REFUTED (3.1).
- Admissible exponents. Isotropic alpha < 1/D (about 0.0469) at the saddle, sharp; with the axis weight |x|^p every
  alpha < (1 + pA)/D, so every alpha < 1 for p >= 2; every alpha < 1 with the complete normalized localized coupling
  and the actual transport near 0 in C^alpha_2 (an earlier barrier (1 + A)/D, about 0.5227, for the localized coupling is REFUTED); every
  0 < alpha < 1 at the source; the conditional profile of Theorem E is C^(1,alpha) off the origin for alpha < 1/20
  (table in 3.2). Globally no Hoelder target with an inverse is known: on Z_2, T, A_0 and L_ren are not onto for
  alpha > 1/2 (THEOREM, V256, V262, V257, V265); T alone is not onto Z_2 or Z_cof for alpha > 1/A_s (THEOREM, V266, V272);
  Z_cof carries the mapping theory and an exterior inverse for every alpha < 1 (THEOREM, V261, V268), and its global
  inverse is OPEN.
- Riesz coupling and source. The coupling is one operator of order 0 with an explicit local part; at the source it is
  inverted together with the transport (H^s with the sharp threshold, about 3.5785, and C^alpha; THEOREMS), also, for
  every alpha < 1, as a whole-plane inverse from the maximal transport domain onto C^alpha_b intersected with L^2 of
  an explicit extension that equals the actual variable unnormalized source operator on B_(delta/2) (THEOREM, V213 to
  V215), and globally it enters the Garding estimate of Theorem C'. Globally the complete coupling is bounded on the
  common target Y (THEOREM), on the scaled target Z_sc (THEOREM) and on the scaled quadratic-axis target Z_2 (THEOREM,
  V245, V254) and on the joint-cofactor target Z_cof (THEOREM, V261, V268); on E_2 and Y its far tail decays exactly
  like R^(2k-1) log R (on E_2) and R^max(2k-1, 2k-gamma/2) log R (on Y), and like R^(k-1) log R on the strain-zero
  inputs of those same spaces (THEOREMS, V276, V286, V278, V287; these sharp rates are not claimed on Z_sc, Z_2 or
  Z_cof); a global Hoelder inverse is OPEN (3.3).
- Is C^alpha(h_x) unnecessary? For the low-order linear theory, yes at the origin and the source (THEOREMS) and at
  infinity (DERIVED for the frozen far window; THEOREMS for the actual exterior inverses on Z_sc, Z_2 and Z_cof, V242,
  V254, V268), including the coupled localized origin problem for every alpha < 1, where no derivative of h
  enters the norm. For the nonlinear closure by the explicit semilinear perturbative map, no: Hoelder solution norms
  that control C^alpha of h and U[h] and the strain, and in which the explicit packets are bounded, do not close it
  (Lemmas N and N', THEOREMS; no statement about every scheme or about profile existence), nor does the C^alpha_2 graph of
  the localized origin inverse (Lemma N'', THEOREM, V211, V218), nor, by the same mechanism, the graphs on the
  joint-cofactor target Z_cof (THEOREM, V264, V271); a quasilinear iteration that absorbs U[h].grad into
  the transport is not excluded; a Lipschitz velocity suffices (DERIVED), and its equivalence with d_x h in C^alpha
  is REFUTED (3.4).

Avenue III (the strain functional c[h]; section 4).
- Saddle-adapted local weighted estimate. Yes for the frozen saddle, globally (Theorem O) and on boxes for every
  p >= 1 (Prop M), with the explicit frozen strain bound C_c0 < 0.017231 at a = 17/4 (THEOREMS); for the actual field
  on boxes NUMERICAL only, and the box estimate does not close by iteration (4.1).
- Absorbing the nonlocal velocity remainders. Yes, with finite but uncomputed constants: the strip estimate with an
  explicit O(R) rate and the global estimates (E0), (E-J), (E-G) for the modal background (THEOREMS; 4.2). In the
  Hoelder class C^alpha_2 the exact normalization makes the localized origin coupling quantitatively small: its E_2 -> E_2
  operator norm is comparable to delta^2, which is sharp, against delta^(1-alpha) without the term c[h] X/3 (THEOREM,
  V219; 4.2). The L^2 box version of this rate is not proved.
- Reducing the rank-one term. Yes, exactly: bordering with denominator d >= 3 c_l > 0, a unique scalar normalization,
  Fredholm index 0 (THEOREMS). The quantitative bound |c[h]| <= C_c ||L h|| is OPEN; the obstruction is the missing
  quantitative inverse (injectivity), not the adjoint weight, the inflow fluxes or the elimination of the tail
  coordinate (4.3).

Avenue IV (basis certification; section 5).
- Conforming basis. Yes for the low realization, in its repaired form (5.1). For the high realization of Theorem E,
  the 78-column pure spline section is low-conforming and meets the high input space in 66 columns and the high graph
  domain in 60 (THEOREM, V210, V220; 5.2); the 38-column far-junction section meets them in dimensions 32 and 29
  (THEOREM, V269, V275), and the strain-zero subspaces of its 38-column span and of these two intersections have
  dimensions 37, 31 and 28 (THEOREM, V282, V291, input side only). The high conformity of the 169-column jet-joined sections, whose exact jet joins are C^3 at
  the two junctions, is not classified.
- Certified finite inverse. For finite sections only, and only conditional on the exported entry balls enclosing the
  exact pairings: sigma_min >= 4.3337e-07 for the first exact section S0 (V066),
  sigma_min >= 2.0685e-02 for the same section without TAU (V200), and sigma_min >= 0.510914 for a section in the realization where the complement lemma applies (V081), each reproduced
  independently from the exported matrices; the input Grams of the pure spline section are certified from the
  original (V202), and so is the complete input Gram of the 38-column far-junction section (V267), but no output
  pairing (the floating smallest value 4.7481 of the far-junction section is an output observation of unresolved accuracy,
  NUMERICAL, V277, V279); no continuum inverse is certified, and floating sections are not bounds,
  neither those in the strong spaces nor the 78-column three-mode section of the remainder block, whose floating
  smallest value 2.766 decreases as angular modes are added and is not bounded below by these runs (NUMERICAL, V252)
  (5.2).
- Off-basis residual bounds. The method is DERIVED (its algebraic ingredients are confirmed in V020 and V027); no
  off-basis bound has been computed at this version (5.3).
- Complement. Not controlled. In the realization used for the first section S0 it cannot be (Prop IV.O, THEOREM, V039); in a
  consistent realization it reduces to checkable items (Lemma IV.1 and INJ-Q, CONDITIONAL THEOREMS) whose finite-rank
  part is estimated, for the chosen proposed method, at about 1e4 low modes (NUMERICAL planning estimate, not a
  proved necessary dimension) (5.4).
- Genuine inverse theorem from the combination. No (5.5).

Final closure (section 6).
- Complete nonlinear existence theorem. No. A conditional one is proved: Theorem E (CONDITIONAL THEOREM, V178).
- Already proved. The unconditional THEOREMS are summarized in item 1 of the verdict above, the conditional Theorem E
  in item 2; the full list with record numbers is in 6.3.
- Missing estimates. (I) a certified injectivity of the base low operator, with a quantitative inverse; (S) explicit
  values of r_*, K_H, K_L and C together with a residual small in the high norm, for which the certified enclosure
  3.866e10 < eta_* < 6.321e129 in a fixed equivalent norm (V192, V182) gives no smallness; and, before constants are
  certified, the tests, necessary for (I) and (S) together, that one exact iteration step reduces the low residual
  norm (V184) and that
  ||R_d|| > 1956082280 |c[d]| for every high-domain direction with c[d] != 0 (V185, V194), which a heuristic estimate suggests the
  archived trial fails (6.5 item 10; no certified direction violates them) (6.2, 6.5).
- Constants requiring numerical certification. The finite-rank split constant delta, the adjoint defects and witness
  norms of INJ-Q, the axis suprema M_20, M_21, M_40, M_41 and the lift bounds, r_*, K_H, K_L, C_B, C_V and a realistic
  high residual norm eta_0; the constants and radii of the localized Hoelder inverses are qualitative (table in 6.4).
- Closest avenue. Avenues I and III together, with Avenue IV used only for the complement (item 5 above; 6.5).

What is established:
- exact frozen inverses at the origin saddle and the source points, with explicit constants (THEOREMS), and a frozen
  far window at infinity (DERIVED);
- a global Fredholm theorem of index 0 for the full nonlocal fixed-strain operator in radial weights, for the actual
  background: its pointwise margin hypothesis is certified over the whole plane by an independent original-data
  ball-arithmetic computation (margin >= 1.78605, V077, raised to >= 5/2 by its refinement, V086); a second code gives
  >= 1.0298 (its coverage and aggregation verified conditional on its exported cell enclosures, V072), refined by that
  code to >= 2.482724, computed once;
- the exact structure of the normalization (the strain functional c), with a bounded realization, an exact rank-one
  bordering by the log variation of the far exponent, a positive denominator, and a unique scalar normalization; the
  cubic coefficient is kept free, since fixing it gives index -1, and a solution is normalized afterwards by a scaling
  that preserves the speed and the far exponent (V087);
- a series of sharp negative results, each with an explicit counterexample, that rule out isotropic and radial
  formulations and the explicit semilinear perturbative fixed-point map in every Hoelder solution norm of the stated
  kind in which the explicit packets are bounded, including the C^alpha_2 graph of the localized origin inverse
  (V030, V211); a quasilinear Hoelder scheme that absorbs U[h].grad into the
  transport is not excluded (V048, V218);
- the inverse of the scalar y-axis row on explicit spaces and the inverse of the pure transport on the full
  jet-plus-remainder spaces (V041, V046; their hypotheses, a positive axis rate, two finite angular coefficient bounds
  and a positive transport margin, hold for the actual background by V047, V055 and V077), and membership of the
  background residual in the matching anisotropic jet target (V042);
- a Fredholm theorem of index 0 for the full normalized linearization on these jet spaces, for the exact modal
  background, without remaining hypotheses (THEOREM, V047, V049 to V053, V055, V077, V086): its two pointwise
  inequalities, a positive axis rate and a positive anisotropic margin, are certified over the whole plane by an
  independent original-data computation (axis rate >= 5.5752, margin >= 0.53072, V077; margin >= 5/2 after its
  refinement, V086), and a second code gives [5.575203, 21.301451] and >= 0.965918 (V072, conditional on its exported
  cell enclosures; refined to >= 2.9270, which an independent whole-plane refinement confirms, V197, and to >= 3, independently
  certified on the whole plane, V259); every nonlocal coupling estimate it needs is proved, with finite but uncomputed
  constants. So the linearization at the background is invertible if and only if it is injective;
- the low/high bilinear bound for the nonlinear term and a Lipschitz bound for the velocity perturbation, in explicit
  high-regularity spaces, with finite but uncomputed constants, including a space of fractional order 25/4 that fits
  under the regularity ceiling of the background (V073) and whose target contains the background residual (V076);
- an abstract two-norm iteration theorem whose hypotheses are listed as concrete constants, and its exact form for the
  moving-tail problem: the scalar normalization is eliminated, the equation becomes a fixed-forcing quasilinear equation
  f_0 + A_h h = 0, and A_h1 - A_h0 is bounded from the high space to the target by the low norm of h1 - h0, so existence
  follows from uniform inverse bounds; for the exact moving-tail family these uniform high and low inverses are proved
  conditional only on injectivity of the base low operator, with qualitative radii and constants (V166, V168 to V170);
- the flow portrait of the transport field for the actual background (orbits from the source to infinity, the x-axis
  segment into the origin; THEOREM, V063 with V080): the only zeros of the field are the origin and the two source
  points (V070, V080, with |V|/r >= 0.00024 away from a rectangle around the source); and a sharp frozen Sobolev
  threshold, about 3.5785, at the source;
- localized Hoelder inverses near the origin, from the maximal domain onto C^alpha_2 for every alpha < 1, with the
  complete normalized coupling and the actual transport on B_(delta/2) (V203 to V207), where the normalized coupling
  has E_2 operator norm comparable to delta^2 (V219), and a whole-plane inverse from the maximal transport domain onto
  C^alpha_b intersected with L^2 of an extension equal to the actual unnormalized source operator on B_(delta/2)
  (V213 to V215); constants qualitative, no global Hoelder inverse. After their cutoffs both act on one common
  target, C^alpha_2 intersected with a weighted L^2 space, which contains the residual and on which the complete
  coupling is bounded and the full operator is closed (V222, V224, V228; for every gamma > 4k and on E_2 itself,
  V241, V247).

A structural finding (THEOREM for the frozen operator, V067): the frozen origin saddle maps a smooth, compactly
supported source to an exact solution -C x^4 sgn(y)|y|^{2 - 1/D}, so no frozen inverse reaches order 5/2 - 1/D (about 2.4531)
across the x-axis (and for general weighted data even in x the limit is the energy value, about 2.334). Together with the
flow portrait this indicates that a high norm with an inverse must have order below these values across the x-axis
segment between the origin and the source, while it may be higher elsewhere; for the true operator this transfer is
OPEN. A high space of this shape is a proved mapping space for the nonlinear term (V065); its inverse theorem is OPEN
(section 2.4). The background itself limits the order from above (THEOREM, V069): the spline background is only C^6
across a knot circle that every orbit crosses, so the residual is not locally H^(13/2) there, and every order used on
that circle and upstream of it must be below 13/2. The mapping bounds hold at the fractional order 25/4 (V073), and the
residual lies in that target (V076). The high theorem has to be an inverse-regularity estimate: a bounded forward
isomorphism between spaces of the same order is false, because the transport differentiates (V074). It must also keep
the full order-zero nonlocal coupling in its energy: a one-order smoothing of that coupling is false (V085); the
normalization profile does lie in the high target (V084). In the cylinder
norm used near the origin the corner threshold is 3/2 + delta A/(A+D), delta the origin exponent (THEOREM for the
frozen operator, with an explicit counterexample, V079); so the order near the x-axis segment is at most 2.1455, and
delta = 9/5 with order 41/20 is an admissible choice.
The low-to-high regularization step is proved for the frozen operators in both corner charts (THEOREM, V103 at the
x-axis in the cylinder norm, with constant 1/kappa_s = 1.02816 at delta = 9/5, order 41/20; V104 for the frozen
vertical remainder cofactor, every finite order s >= 2). A spectral-parameter continuation lemma is CONFIRMED as an
abstract theorem, and its direct application to the spaces with a free cubic coordinate is REFUTED (V106); its
restatement for the remainder block, with the jet row split off by the triangular form, is a CONDITIONAL THEOREM
(V108) that reduces the variable-order regularization step to a large-parameter transport resolvent bound, a high a
priori estimate with a compact error and three conditions on the jet row (section 2.4); the jet row itself cannot be
shifted, since the shifted scalar row changes index at D/4 (THEOREM, V109). The three jet-row conditions are now
proved on explicit spaces (THEOREM, V112 to V118). The scalar target is Gamma_H = a H^(25/4) on the line t = log r,
with a = e^(9t/5) at the origin end and e^(-7t/2) at infinity, and B_H = {beta in B : A beta in Gamma_H}, which
consists of the beta = J chi + a v with v in H^(29/4) (V117). The remainder target R_H is the sum of the factored
axis-zero space of order 25/4 and a cone-bulk space of order 41/20 supported in |cos theta| >= epsilon. Then the
lower block maps B_H into the factored part (J1), the complete axis row maps E B_H (+) R_H compactly into Gamma_H (J2),
and the bordering profile lies in E Gamma_H (+) R_H (J3) (V118). J2 rests on a fractional trace gain (V116), on four
sector dilation derivatives of the remainder, which a critical angular Hardy inequality supplies (V114), and on the
dilation commutation of the axis trace (V112, V113). The integer axis order H^6 is not compatible with the remainder
order 25/4 (REFUTED, V115). On this cone-sum space the remainder-block hypotheses (H1) to (H3) are not available.
For this sharp cone sum, (H1) fails: wave packets just inside the low-order cone have bounded graph norm (even with one transport
derivative) while the sixth derivative of their coupling on the high-order side grows like tau^(-59/20) (REFUTED as a
choice, exact-kernel counterexample, V119). A smooth variable order of the kind in section 2.4 is not affected by
this counterexample. On the smooth variable-order space X_s (order s between 41/20 and 25/4, uniformly smooth,
reflection invariant, equal to 25/4 on a fixed sector around the y-axis and used in the factored variable there),
C_R : X_s -> X_s is bounded and the three jet-row conditions hold (THEOREM, V126). This is (H1). If in addition s is
nondecreasing along the flow (W.grad s >= 0), the transport resolvent bound (H2) holds with M = 1 in a dyadic
Littlewood-Paley norm (THEOREM under this order hypothesis, V129, with the seven-derivative coefficient regularity that
the actual field has; five derivatives do not suffice, REFUTED, V127). An order function with all these properties,
equal to 41/20 near the closed x-axis segment and the sources, exists for the actual field (THEOREM, V130 by a
blow-up construction with a smooth escape function, and V132 for the direct construction of section 2.4 (f') from the
exit time of a repeller block around the segment and the sources). So (H1) and (H2) hold on an actual X_s, and of the
hypotheses of Corollary H-spec only (H3) remains, apart from low injectivity. For (H3): a pure energy estimate is
impossible at the vertical-axis end (V128), and the energy margin is needed only on the characteristic set; the exact
origin normal family is bijective for every real frequency and Re lambda > -0.9726 because of the axis zero and the
parity (THEOREM, V131), with a bound uniform in the frequency (THEOREM for the exact normal operator, V133); the
selected principal end inverses at the vertical, horizontal and far ends survive the actual small coefficient errors
(THEOREM, V135, V137; constants qualitative), but not by a perturbation argument, since a small first-order
coefficient error is unbounded on the normal graph (counterexample for the actual coefficients, V138); the actual
inner end estimate holds with a finite annular error, and the coupling tails vanish in the X_s operator norm, which
reduces the full equation to a compact core with a high-norm error (THEOREM, V139, V140). (H3) on X_s is reduced to a
single high-frequency estimate (Hs_eps) modulo a lower-order norm, by an exact weighted L^2 energy identity for the
actual field whose weight, the bulk weight divided by cos^8 theta, has positive energy at both ends (CONDITIONAL
THEOREM, V141, section 2.4 (g)). The global symbol inequality m + N W.grad Lambda + L_0 (W.nu)^2 >= mu on the
compactified cosphere bundle holds for every mu < 0.9726 (THEOREM, V144, a compactness argument from the confirmed
margins and escape function). (Hs_eps) follows from it and four finite-regularity calculus inputs, and all four are
now proved for the actual coefficients (THEOREMS, V146 to V150): the order reduction with a lower-norm error and the
sector support correction (V146), the coupling modulo compact and arbitrarily small errors (V147), the
noncharacteristic penalty through the equation with an arbitrarily small high error (V148), and the principal
transport commutator for the W^(7,inf) field by a kernel Taylor expansion, with the exact logarithmic coefficient,
on the maximal domain (V149, V150); the scalar positive quantization holds at the actual finite regularity (THEOREM,
V145), and the positivity step is pointwise because the symbol is a quadratic form in the covector. The assembly of
(Hs_eps) from these inputs is CONFIRMED, so (Hs_eps) and (H3) hold on X_s for the actual operator (THEOREM, V151).
Consequently the remainder block S_1, the renormalized operator L_ren and the bordered linearization L_red are
Fredholm of index 0 on their high graph domains in X_s (THEOREM, V152; all constants qualitative). A high null vector
is a low null vector, so low injectivity, if proved, gives a bounded high inverse that agrees with the low inverse.
The joint source margin at order 41/20 is 4.52536 (THEOREM, V134; an earlier value of about 14.8 was wrong). Low
injectivity is OPEN. For uniformity over a ball of perturbed backgrounds, the fixed order s of V132 satisfies
W.grad s >= kappa_s |grad s| with kappa_s > 0, so the same order is monotone along every field W + B with
||B||_inf <= kappa_s/2, and the matrix margin loses an explicit amount bounded by C^1 norms of B (THEOREM, V154); the
logarithmic positivity holds for a C^(1,alpha) coefficient (THEOREM, V155); the variable-order Kato-Ponce bound for the
full transport commutator, proposed for this step, is false (REFUTED, V153: it misses the term -(B.grad s) log<D>).
The tame estimate that replaces it holds in square-summed form: with a dyadic partition sum_j psi_j^2 = 1 and
A_j = Op(e^(N Lambda) <xi>^s psi_j), the coefficient commutators satisfy (sum_j ||sum_l [A_j, B_l] d_l v||^2)^(1/2) <=
C (||DB||_inf ||v||_{H^s} + ||B||_{H^s} ||Dv||_inf) (THEOREM, V157), the perturbation velocity of an IPM perturbation g
in the high coefficient space G_s splits as B[g] = c[g] E_0 + Z[g] with |c[g]| + ||Z[g]||_{H^s} + ||B[g]||_{C^(1,alpha)}
<= C ||g|| for alpha < 1/20 (THEOREM, V156), and the dyadic energy carries the background estimate over (THEOREM, V158). Consequently,
for the transport perturbations S_g = (V + U[g] + c[g] X/3).grad - 1 + C_R with frozen coupling and ||g|| <= r_*, the
high estimate with a compact error holds uniformly on the exact maximal domains D_g, T_g generates a C_0 semigroup,
S_g - lambda is Fredholm of index 0, and, if S_0 is injective, ||h|| + ||T_g h|| <= C ||S_g h|| uniformly on a smaller
ball (THEOREM, V159, V160; r_* and C qualitative). A second proof with the single operator A and a tame bound for
sum_l [A, B_l] d_l is also CONFIRMED (V161, V163), after the correction of a sign in an auxiliary weighted energy
(V162). The remaining structural pieces of a uniform inverse are now also proved. The axis velocity trace of a high
perturbation g gains 3/2 derivatives once the strain c[g] chi_0 is split off, so the perturbed scalar axis row is a
small bounded perturbation on the fixed scalar domain with its free cubic coefficient, and an isomorphism on a small
ball (THEOREM, V166; the leading axis multiplier of the trace has the sign +2/eta^2, V167). The full scalar and
remainder block with fixed coupling is Fredholm of index 0 on the varying graph domains, with one fixed compact error
map, in the high realization (THEOREM, V168) and in the low realization (THEOREM, V169). The exact scalar-normalized
moving-tail family, whose background rho_ell = rho_0 + chi_inf(r) (r^(1/ell) - r^k) Theta(theta) moves with the
dilation rate, satisfies the same compact estimates in both realizations, its coupling and rank-one vector change by
small bounded maps, and if the base low operator is injective it has uniform low and high inverses on a ball
(THEOREM, V170; radii and constants qualitative). Combined with the moving-tail iteration theorem (V062) and
continuous embeddings of the high spaces into the low spaces and into the high space of the bilinear bound, this gives
a conditional existence theorem (Theorem E, section 6.2 item 6; CONDITIONAL THEOREM, V178, with the embeddings of
Lemma Emb, THEOREM, V177): injectivity of the
base low operator and a smallness condition K_H eta_0 <= r <= r_*, K_L C K_H eta_0 < 1, with eta_0 the high norm of
the residual, imply a self-similar profile with cubic jet (1 + J) x^2 y (leading term exactly x^2 y after a scaling if
|J| < 1). Neither hypothesis is verified: low injectivity is OPEN,
and the smallness condition involves qualitative constants and a high residual norm, which is enclosed as 3.866e10 < eta_* < 6.321e129 in an explicitly fixed equivalent norm (THEOREMS, V192, V182); the upper
end is a deliberately loose majorant.

The residual of the archived trial is not small in the strong norm. A directed original-data computation gives
||F(rho~)||_Y > 933.47 from the remainder energy on 9.9 <= log r <= 10.1 alone (THEOREM, V110; six point densities,
V107), and a complete interval computation over all angular modes, 1860 radial cells on -40 <= log r <= 20 and both
analytic tails encloses the norm: 6049.11 < ||F(rho~)||_Y < 8601.42 (THEOREM, V164). All-mode point densities at 81
radii, computed once, gave about 7.2e3 (NUMERICAL), consistent with the enclosure, with 95 percent of the energy lying
beyond the outer join at log r = 8.135 and the exact far decay rate 4k - 5/4 of the energy density.
Pointwise the residual is small (sup |F| / sup |rho~| between 2e-8 and 3e-7 on the sampled circles), but its strong
energy lies in a thin angular layer at the vertical axis (94 to 99.7 percent within 0.01 rad for 4 <= log r <= 10),
where the angular spectrum of the residual quotient is nearly flat up to the resolution of the trial. The value
depends strongly on the weight: angular exponent a = 3.6 and the far radial exponent lowered by 0.6 give about 13
(NUMERICAL). For this decoupled family (inner radial exponent unchanged, far radial weight lowered by 0.6, angular
exponent a in [18/5, 4]) the transport margin is at least 1.10534 (THEOREM, V171 with the
affine interpolation of V172), the low mapping, compactness and
Fredholm theory of the jet-plus-remainder realization hold with a closed scalar normalization (THEOREM, V172), and the
residual satisfies 3.270 < ||F(rho~)||_(Y_a) < 485.632 uniformly in a (THEOREM, V174 for the upper and V179 for the
lower bound; the lower bound comes from eight disjoint radial windows and is deliberately partial). These are low norms; for the high forcing
norm that the closure needs, the enclosure 3.866e10 < eta_* < 6.321e129 is certified in an explicitly fixed equivalent
norm (THEOREMS, V192, V182). With the present weight and global constants the
closure inequalities need C_V K_H < 10/(51 eta), below 3.25e-5 by V164 (section 6.2, item 5).

The missing items, in order (section 6.2): (I) injectivity of the base low operator, which Theorem E needs only
qualitatively but for which no qualitative argument has been established here, so a certified finite-dimensional
check is the selected quantitative route (not a proved unique route); then, for
(S), explicit values of the radius r_* and of the constants K_H, K_L and C, which are now produced by compactness
arguments (V152, V170, V175) and would need explicit compact parts and Garding constants; and a residual that is small
in the high closure norm, for which 3.866e10 < eta_* < 6.321e129 is certified in a fixed equivalent norm (V192, V182; the archived trial is not small even in the low norm of the present
weight, V164; section 6.2, item 5).
For the injectivity certificate the abstract criteria that convert a finite-rank split into an inverse bound are proved
(V082); block elimination reduces the certificate to the remainder block S_1 on the plain weighted space plus a system
in one variable with one scalar (Lemma INJ-S, THEOREM, V092); the principal energy error at frequencies above Lambda is
of second order, (S2mat(B) + S2(b_eta))/(2 Lambda^2) in the second Fourier moments (THEOREM on a regular cylinder,
V096), and stays of second order for the full regular Mellin velocity with variable coefficients (V098); the paired
weight-conjugation difference is Hilbert-Schmidt with an explicit bound on a regular patch (V097); the axis-strip
constant is explicit in four background derivatives, with universal constants 39 and 25 (V095, V099); the conditional
algebra of the split is confirmed (V094); and the target norm has an exact angular reduction without angular
quadrature (V100), which prepares a certified residual. The certificate is now one explicit conditional statement
(INJ-Q, CONDITIONAL THEOREM, V102): with the exact margin m = 5/2, a certified high-frequency bound eps for the
symmetric defect on the complement of a finite projection, a finite-rank approximation of error delta_F of its
projection blocks, and non-orthonormal columns with Gram bounds e, p, d, the remainder block S_1 is bijective with
||S_1^{-1}||_R <= (1 + e p)/(5/2 - eps - delta_F - e d) when the denominator is positive; every localization, tail,
lift and norm-comparison error is listed as an input. Real transport energy localizes without error under a square
partition of unity, and the coupling defect is a paired double commutator with explicit Hilbert-Schmidt bounds on
regular patches (V101); the axis trace functionals and the radial lift have explicit majorants (V105). Grid estimates of the number of low modes the split needs (NUMERICAL, section 5.4): about
3.4e4 to 5.2e4 per parity class with the second-order rule and global moments, 1.3e4 to 2.8e4 with radial localization
or with the vertical-axis strip removed (localization errors not included), against 4.7e6 with the first-order rule;
local sup-norm proxies, which are not bounds, give about 1e2 (second order) and 1.7e3 (first order). These counts are
planning estimates, not proved necessary dimensions. For the chosen proposed method, a certified split of an
estimated order of 1e4 modes is beyond the computing limits of this work; with that method a feasible certificate
needs phase-space localized error bounds that approach the local proxies.

## 1. Problem, accepted state and exact equation

1.1 Equation. F(rho) = (c_l X + U[rho]).grad rho - rho on R^2, with U = (-psi_y, psi_x) and -Lap psi = d_x rho. The
density rho is even in x and odd in y, and rho = x^2 y a with a continuous and a(0) = 1. The canonical velocity is the
one given by the Riesz kernels with the standard subtraction for profiles growing slower than r. No harmonic velocity
is added.

1.2 Normalization. If F(rho) = 0 in this class (in the distributional sense when the factor a is merely continuous),
then 3 c_l - c[rho] = 1 with c[rho] = psi_xy(0). Consequently DV(0) = diag(-A, D) with A = 2 c_l - 1 and
D = 4 c_l - 1 = 2A + 1. THEOREM (derived independently twice; V002).

1.3 Accepted state and the rigorous background.
- The accepted numerical state is the published candidate X3, with c_l = 1/k and k = 1615536043799051/2^53, so
  c_l = 5.575362610641546..., A = 2 c_l - 1 (about 10.15073), D = 4 c_l - 1 (about 21.30145) and b_0 := c_l + 1
  (about 6.57536). No newer accepted state exists:
  the later collocation solves stagnated at a 2-norm residual of about 2e-4 (NUMERICAL).
- X3 is not exactly normalized: 3/k - 1 - c[X3] lies in (1.0301137738456e-8, 1.0301137743913e-8) (THEOREM, V018). With
  the normalized exponent, F(X3) therefore contains a term that grows like r^k, and X3 cannot itself be the rigorous
  background.
- Every rigorous statement below uses the exactly joined, exactly normalized explicit modal trial rho~ instead. Its
  strain before repair is c0 in [15.7260878319246786225638146971829, 15.7260878319246786225638146971831], and a scalar
  repair z in [-1.198605236453734890460334164888e-20, -1.198605236453734890460334164887e-20] makes c[rho~] = 3/k - 1
  exactly (THEOREM, V005). An independent ball-arithmetic recomputation by three formulas gives
  c[rho~] - (3/k - 1) in [-1.62e-43, 1.62e-43] (computed once, not separately verified; V005 is the certified statement).
- rho~ is C^{4,1} and not C^5 at the origin: the degree-5 inner term contains sin(521 theta) (THEOREM, V036). Every
  local estimate below uses at most four derivatives of rho~ at 0.
- rho~ has a source point x_P in (4841405518533377, 4841405518533711)/2^49, unique in this certified interval
  (and, by the global zero set of V080, the only source point on the positive x-axis), with transverse rate mu in
  (0.99999997745, 0.99999997750) and g = d_y rho~(P) in (29, 30) (THEOREM, V017). So rho~ is not stationary at P, and
  mu = 1 must not be substituted.

1.4 Full linearization and exact expansion (formulation N: c_l[rho] = (1 + c[rho])/3 is built in). For every background
with 3 c_l_bar - c[rho_bar] = 1,
    F(rho_bar + h) = F(rho_bar) + L h + N(h),   L h = V.grad h - h + W[h].grad rho_bar,   N(h) = W[h].grad h,
with V = c_l_bar X + U[rho_bar] and W[h] = U[h] + (c[h]/3) X. There are no cubic terms. Equivalently
F(rho_bar + h) = F(rho_bar) + A_h h with A_h g = (V + W[h]).grad g - g + W[g].grad rho_bar. Only the transport field
of A_h depends on h; its divergence is 2 c_l_bar + 2 c[h]/3, and its linear part at 0 is diag(-A', D') with
D' = 2A' + 1, so the normalization structure is preserved along an iteration. L = L_fix + (c[.]/3) X.grad rho_bar, where
L_fix h = V.grad h - h + U[h].grad rho_bar. The last term is a rank-one perturbation by a function that grows like r^k.
(THEOREM, V038, fixed-background expansion.)

1.5 Strain functional. c[h] = (1/pi) PV int sin(3 theta) r^{-3} h dX - (1/4) h_y(0). The local term vanishes in the
class above. THEOREM (V002, V008).

1.6 Scaling direction and the centre coordinate. The scaling tangent K = rho~ - X.grad rho~ has J(K) = -2, c[K] = 0 and
L K = eps~ - X.grad eps~ with eps~ = F(rho~) (THEOREM for these formal identities, V198; scaling covariance V087); here J(h) is the x^2 y coefficient of h at 0. For the archived spline trial these identities are formal: the seventh t-derivative of the vertical-axis cofactor of rho_0 jumps at an interior knot (t = 2.2021...), so the axis cofactor of K has a jump in its sixth derivative and K, even multiplied by a smooth annular cutoff equal to 1 near that knot, is not locally in H^(13/2), while the high correction space requires local H^(29/4) (THEOREM for the local nonmembership, V198). K is therefore not an admissible high-space test direction. The constraint J(h) = 0
removes the scaling direction only if J is continuous on the correction space. In the diagnostic norm of the earlier
analysis of this case, and in its graph norm even at fixed strain, J is not continuous and {J = 0} is dense relative to
that specified pointwise-jet domain with its graph norm (THEOREM, V012, zero-strain packets); this is not a density
statement in the entire maximal Hoelder graph of section 3, where the graph closure of the smooth core is a proper
subset of the maximal graph (V217, V240).
J is a continuous coordinate of the jet-plus-remainder spaces of section 2. On these spaces
the restriction of the full normalized linearization to {J = 0} is Fredholm of index -1 (THEOREM, V087), so J is kept
free and the solution is normalized at the end by a scaling (section 4.3).

1.7 Moving far exponent (THEOREM, V025 and V038). An exact solution with c[h] != 0 has far exponent 1/c_l[rho], which
differs from k. A fixed background plus a correction in any of the weighted spaces used here cannot contain such a
solution, and every smooth parameterization of the tail has a log^2 r second variation. The consistent formulation is
parametric: background family rho_bar_ell = rho~ + chi_inf (r^{1/ell} - r^k) Theta_0, unknowns (ell, h), and the scalar
equation 3 ell - c[rho_bar_ell + h] = 1 (section 4.3). d rho_bar_ell/d ell at ell = c_l is -k^2 KP, with
KP := chi_inf r^k log r Theta_0, the log variation of the far exponent.

## 2. Avenue I: weighted L^2 and Sobolev theory

2.1 The strongest rigorously valid weighted inverse estimates.
Answer: the strongest statement for the full problem is Theorem C' of 2.3: the full normalized linearization of the
modal background is Fredholm of index 0 from the jet space Z to Y (THEOREM, V047 with V049 to V053, V077, V086), so it is invertible if and only if it is
injective, and injectivity is OPEN. The strongest quantitative inverse bounds are those of the frozen and partial
operators: Theorem O at the origin (sharp constant 1/kappa_0), the frozen source inverse (bound 1/delta_s), and the
remainder transport on R, ||T_R^{-1}|| <= 1/kappa_* <= 2/5 (Lemma C'2 with kappa_* >= m_a >= 5/2, V046, V086), with
the explicit triangular inverse of the pure transport on Z (V046). No quantitative inverse bound for the full
linearization is proved. For the high norm that the nonlinear step needs (the smooth variable-order space X_s, order
41/20 to 25/4), the mapping and jet-row conditions (H1), (J1) to (J3) and the transport resolvent bound (H2) are
THEOREMS (V126, V129, V130), the reduction of the high a priori estimate (H3) to one high-frequency estimate is a
CONDITIONAL THEOREM (V141), and that estimate follows from a verified global symbol inequality (V144) and four
finite-regularity calculus inputs, all of which are THEOREMS (V146 to V150, with V140, V142, V143, V145); the assembly
is CONFIRMED, so (H3) holds on X_s (THEOREM, V151); see 2.4 (g). Hence S_1, L_ren and L_red are Fredholm of index 0 on
their high graph domains (THEOREM, V152), and invertibility again reduces to injectivity.

(a) Frozen origin saddle, Theorem O (THEOREM, V022). T_0 := -A x d_x + D y d_y - 1. Fix 5/2 < a < 9/2 and 0 <= b < 3/2
with a + b > 4. Put w = |x|^{-2a} |y|^{-2b}, kappa_0 := b_0 + A a - D b and sigma := a + b - 4.
- Domain: Z_0 = {h = x^2 y (J + beta_t(log r)) + h_R}, with beta_t' in G := L^2(e^{-2 sigma t} dt), beta_t(-inf) = 0,
  h_R and Y_0 h_R in R_w := L^2(w dX), Y_0 = -A x d_x + D y d_y. Range: Y = {x^2 y gamma(log r) + F_R : gamma in G,
  F_R in R_w}. The decomposition is unique because x^2 y is not in R_w for a > 5/2.
- On R_w, T_0 (maximal domain) is bijective with T_0^{-1} F = -int_0^inf e^{-s} F(Phi_s X) ds and
  ||T_0^{-1}|| = 1/kappa_0, sharp. The same holds on the conormal spaces generated by x d_x and y d_y, which commute
  with T_0.
- T_0 : Z_0 -> Y is bounded and onto, with kernel span{x^2 y}; J is a continuous coordinate; the right inverse with
  J = 0 has explicit norm.
- The strain functional extends continuously to Z_0 restricted to r < 1:
  |c[h 1_{r<1}]| <= |J|/8 + 0.069735617396310252 ||beta_t'||_G + 0.045183183318774124 ||h_R||_{R_w} at a = 7/2,
  b = 6/5. The constants depend on (a, b): the sharp jet constant is C_v = 1/[8 sqrt(sigma (sigma + 1)(sigma + 2))],
  attained by an explicit h with J = 0; at a = 17/4, b = 0 it is 0.14907119849998597976... (V048).
- At a = 7/2, b = 6/5: kappa_0 = 16.54116035405294722844...; at a = 17/4, b = 0: kappa_0 = 49.7159.
- No approximate kernel exists modulo x^2 y. The degree-2 centre quasimodes and the jet packets that obstruct the
  earlier norms are excluded or have unbounded image norm.
- The pointwise reading of the strain extension is REFUTED: a thin flow-tube sum in Z_0 is not continuous at 0, so c
  on Z_0 is the continuous extension from a core.

(b) Frozen source (THEOREM, V011, V021, V024). L_P = A s d_s + mu y d_y - 1 - g M with M = -R_1^2, on the maximal
full-plane H^s graph domain. With delta_s = min(1 + (A + mu)/2 - s mu, 1 + (A + mu)/2 + g - s A) > 0 the operator is
bijective on H^s with inverse norm at most 1/delta_s. On the box A in [10, 10.2], mu in [0.99, 1.01], g in [29, 30]
and s = 31/10 the bound is 500/1687, and every s < 2373/680 is admissible. mu = 1 is not a pole. At the actual source
the threshold is s_fast = (b_0 + g)/A with 3.57854758171660 < s_fast < 3.57854758172942, and it is sharp: a fixed
smooth forcing has no H^s solution for s >= s_fast, with the Riesz coupling retained (THEOREM for the frozen maximal
realization, V064). An auxiliary
variable-coefficient version has an explicit bound and a sharp strain norm (V021), and the neighbourhood of the actual
source satisfies the perturbation margin kappa - E >= 44699521/14000000 (V024).

(c) Global Fredholm theorem for the full nonlocal fixed-strain operator, Theorem R (THEOREM, V023 and V031 as a conditional statement; its margin hypothesis certified for the actual background, V077).
- Hypotheses: V globally Lipschitz and C^1 with V(0) = 0 and div V = 2 c_l; the coupling coefficients continuous and
  tending to 0 at 0 and at infinity; the weight w = e^{mu(log r)} with mu Lipschitz and Lip(mu) < 2; and the margin
     (H_m)   m_* := inf_{X != 0} [ b_0 + (1/2) mu'(log|X|) q(X) - b_+(X) ] > 0,
  with q = X.V/|X|^2 and b_+ = (|grad rho~| - d_y rho~)/2, the top of the symbol of the coupling U[.].grad rho~.
- Domain: the maximal domain D_w = {h in L^2_P(w) : V.grad h in L^2_P(w)}. Range: L^2_P(w) (P: the parity class).
- Conclusion: L_fix : D_w -> L^2_P(w) is Fredholm of index 0, and there is a compact K with
  m_* ||h|| <= ||L_fix h|| + ||K h|| (no eps loss). L_fix is invertible if and only if it is injective.
- The hypotheses other than (H_m) hold for rho~. For the piecewise affine weight mu~ (sup|mu~'| = 7/4, e^{mu~} ~ r^{1/4}
  at 0 and r^{-5/4} at infinity) the grid minimum of the margin is 2.590 (NUMERICAL). An independent ball-arithmetic
  computation from the original data (all 1558 spline spans and 261 stream modes rebuilt, 512-bit Green moments,
  3276 radial times 128 angular cells, the outer continuation, both infinite ends bounded analytically, a separate
  640-bit audit; it shares no code with the second computation below) gives m_* >= 1.78605 (THEOREM, V077), and its
  refinement gives m_* >= 5/2 (THEOREM, V086); a second code gives m_* >= 1.029821 (aggregation verified conditional on
  its exported cell enclosures, V072), refined by that code to 2.482724 (computed once). So Theorem R holds for L_fix and rho~ without remaining hypotheses.
- Limits (THEOREM, V032): on this graph the strain c is not closable. Rescaled annular packets h_n with c[h_n] = 1 have
  h_n -> 0 and L_fix h_n -> 0 in L^2(w) (for weights comparable to r^eta near 0 with eta > -4, which includes the
  selected one; at the endpoint eta = -4 a single rescaled packet keeps an input norm bounded below, and the proof uses
  averages of packets at disjoint geometric scales). So Theorem R covers L_fix and not the normalized operator L. Injectivity is
  OPEN; no kernel element is known.

(d) Necessary conditions for any space that carries the normalization (THEOREM, V025).
- N1: for product-conic weights r^{-2 beta_r} |cos theta|^{-2a} |sin theta|^{-2b} near 0, coercivity of the frozen
  saddle on every ray holds if and only if beta_L(b) < beta_r < beta_U(a), and beta_L(3/2) = beta_U(5/2) = 4 exactly.
  So if the frozen saddle is coercive in L^2(w) and x^2 y is not in L^2(w), then a >= 5/2 (endpoint allowed; the word
  "strictly" of the first version is REFUTED). This statement is for the coercive product-weight mechanism. Continuity
  of J alone does not force anisotropy (V035).
- N2: along the outgoing y-axis the angular exponent a(t) must be nondecreasing. Conditional on the positive axis rate
  q(0, y) > 0, which holds for rho~ (V_2/y >= 5.5752, THEOREM, V077; a second code gives
  5.575203 <= V_2/y <= 21.301451, V072).
- N3: in such a space the x^2 coefficient along the whole y-axis is a separate unknown. Its row (the jet row of L) is
  V_2(0, y) g' + (2u - 1) g + 2 rho_2 (d_x U_1[h](0, y) + c[h]/3) + rho_2' (U_2[h](0, y) + c[h] y/3) = f_2(y),
  and the strain term cancels the leading coupling as y -> 0.
- N4: at infinity a far factor r^{-2 gamma} needs 2k < gamma < 1 + k (coercivity, exclusion of the homogeneous tails
  r^k Theta, and membership of the residual r^{2k-1} Eps).
- N5: the fixed-background obstruction of 1.7.

2.2 Older obstructions and whether they still apply.

| Obstruction (earlier record) | Applies to | Status in the present spaces |
|---|---|---|
| Degree-2 centre quasimodes (V006) | diagnostic norm with r^{-6} weight | excluded for a > 5/2; no approximate kernel (Theorem O) |
| Pointwise cubic coefficient of L h not controlled by C^{2,alpha} regularity and J = 0 (V007) | pointwise centre conditions | applies; the centre is handled by weighted L^2 conditions with J as a coordinate |
| Non-smooth homogeneous centre solutions below the integer modes (V009) | continuous-factor classes | no effect on Z_0: Theorem O gives a bounded remainder inverse, so cut-off homogeneous solutions are not approximate kernels |
| Radial local moment gap (V010) | radial or isotropic moment estimates | applies; no radial argument is used at 0 (N1) |
| J nonclosed, also at fixed strain (V012) | norms without a jet coordinate | evaded: J is a coordinate of Z_0 and Z |
| Negative potential energy at the saddle (V003) | energy pairing | applies to energy methods; not to the transport-weighted estimate |
| Mapping obstruction for a >= 5/2 without jets | conic weights without jets | consistent with N1 to N3: the y-axis jet is a required coordinate |
| No constant weight (b_+ reaches 10.14 > b_0) | constant or slowly varying weights | applies (NUMERICAL); avoided by the radial Lyapunov factor of Theorem R |
| Source Sobolev window | H^s at the source | applies: s < s_fast (about 3.5785) at the actual source, sharp (V064); s < 2373/680 uniformly on the coefficient box (V011); not binding, the corner value (about 2.4531) is smaller (section 2.4) |
| Weak graph norm discontinuity of N (V019) | the diagnostic graph norm | applies; a high norm is needed (section 3.4) |
| Strain not closable on the radial graph (V032) | every A_2 radial weight | applies; the normalization needs the origin part of section 2.3 |
| Finite-section residuals are not inverse bounds (V014) | every finite section | applies; section 5 |

2.3 A consistent domain.
- Spaces (definitions; all functions with the IPM parity, t = log r, a = 17/4).
  - Weight w_a = |cos theta|^{-2a} e^{mu_a(t)}, mu_a' = -2a for t < 0 and -5/4 for t >= 0, mu_a(0) = 0. In r < 1 this is
    exactly |x|^{-2a}, the weight of Theorem O with b = 0. R := L^2_P(w_a).
  - Jet lift E gamma := x^2 y gamma(log r), and the scalar space G with
    ||gamma||_G^2 = int_{t<0} |gamma|^2 e^{-t/2} dt + int_{t>0} |gamma|^2 e^{27t/4} dt (the radial factor of |x^2 y|^2 w_a).
  - Target Y := E G (+) R (direct, since |cos theta|^{4-2a} is not integrable).
  - Axis row (THEOREM, V041, for every field that satisfies the axis hypothesis (A) below; (A) holds for the modal
    background, V055, V077). With d(t) := V_2(0, e^t)/e^t and
    D = 4 c_l - 1, the y-axis component of the transport acting on g = y beta(log y) is
    A beta = d beta' + (D - d - 2d') beta. Put H := exp(-int_{-inf}^t (D - d - 2d')/d), beta = H z, and let B be the space
    of such beta with z' in L^2(omega), omega = e^{-t/2} (t < 0), e^{2(3/8 + k) t} (t > 0), z(+inf) = 0, normed by
    |J|^2 + ||z'||^2 + the two Hardy terms, where J := lim_{t -> -inf} beta(t) is the cubic coefficient. Then A is an
    isomorphism of B onto Gamma (||gamma||_Gamma = ||gamma/(d H)||_{L^2(omega)}, equivalent to G), with
    beta(t) = -H(t) int_t^inf gamma/(d H), J = -int gamma/(d H), and explicit constants. J is an output of the far
    condition; imposing J = 0 as well restricts the range to a closed hyperplane.
    Hypothesis (A): d_min <= d <= d_max with |d - D| + |d'| <= C e^{2t} (t <= 0) and |d - c_l| + |d'| <= C e^{-(1-k)t}
    (t >= 0). The endpoint orders hold for the modal field and d >= 5.5752 (THEOREM, V055, V077). A second code (V072,
    conditional on its exported cell enclosures) gives d in [5.575203, 21.301451] with the constants listed under the
    Answer below.
  - Domain Z := E B (+) D_R, with D_R the maximal domain of T = V.grad - 1 in R and the graph norm.
    In the parametric formulation the tail coordinate is ell.
- Membership checks: x^2 y chi_0 is in Z (J = 1); r^k Theta is not in Z; c is bounded on Z (Lemma C'4 below); the
  residual of the modal background lies in Y, with up to five conormal derivatives (THEOREM, V042: F(rho~) = x^2 y B,
  gamma = B(r, pi/2) in G, and the rest carries cos^4(theta) sin(theta); B = O(r^2) at 0 by the exact normalization
  and O(r^{2k-4}) at infinity); the parametric residual F(rho_bar_ell; ell) - nu(ell, 0) H_0 lies in Y, smoothly in
  ell, for max(q, k) < 5/16 (THEOREM, V042). These are membership statements (V042); values of the residual norm are
  certified separately: the low enclosures of V164, V174 and V179 and the high enclosure of V192 and V182
  (section 0).
- Every necessary condition of 2.1(d) is met: a = 17/4 lies in [5/2, 9/2); the angular factor is constant along the
  y-axis; the axis jet is a coordinate; the far exponent 5/8 lies in (2k, 1 + k).
- Margin: inf (kappa_{w_a} - b_+) has grid minimum 3.0908 (NUMERICAL), attained in the far field, with
  kappa_{w_a} = b_0 + (mu_a'/2) q + a tan(theta) V.grad(theta). The independent original-data computation gives
  m_a >= 0.53072 (V077) and, refined, m_a >= 5/2 (THEOREM, V086). A second code gives m_a >= 0.965918 (weakest box near
  the x-axis at r about 52; V072, conditional on its exported cell enclosures), refined by that code to 2.871539 and
  then 2.9270; the value m_a >= 2.9270 is confirmed by an independent whole-plane refinement from the original data
  (THEOREM, V197). A finer outer cover by the numerics team gives 3.000000, and an independent original-data refinement
  (512-bit production, 640-bit replay, complete cover audit) certifies m_a >= 3 on the whole plane (THEOREM, V259, at the
  coefficient-margin scope). These are lower bounds, consistent with the grid value.
- Theorem C' (CONDITIONAL THEOREM as stated, V047; its three coupling hypotheses are THEOREMS for the modal background,
  V049 to V053, and its two pointwise hypotheses are certified, V077, V086, so the conclusion below is a THEOREM for the
  modal background). The first version ("if (E) and the margin hold, L : Z -> Y is Fredholm by the proof of Theorem R") did not
  specify the lifting, the cross couplings, the remainder domain or the homotopy (V041). The present version does:
  - Lemma C'1 (CONDITIONAL THEOREM on (A) and (L), V046, V047; both hold for the modal field, V047, V055, V077): T(E beta) = E(A beta) + x^2 y cos^2(theta)
    [a_1 beta' + a_0 beta], where cos^2(theta) a_1 = q - d and cos^2(theta) a_0 = 2V_1/x + V_2/y - 1 - b(t) are the
    differences between the transport coefficients and their values on the y-axis (q = V.X/r^2). Under the lift
    coefficient bounds (L) |a_1| <= M_1 and |a_0| <= M_0 min(r^2, 1), the lift error is bounded from B to R by
    I_a^{1/2} (M_0 ||min(e^{2t}, 1) beta||_G + M_1 ||beta'||_G), I_a = int |cos theta|^{8-2a} sin^2 theta = 6.99215...
    The modal field satisfies (L) with finite constants (V047: near 0, V = (-A x, D y) + cubic terms + O(r^5 log r),
    so a_1 = -(A + D) + O(r^2) and a_0 = O(r^2); at infinity a_1, a_0 = O(r^{k-1})). The sizes of M_0 and M_1 are not
    computed. The error is not compact at 0, and the proof does not need it to be.
  - Lemma C'2 (THEOREM, V046): if kappa_* := ess inf kappa_{w_a} > 0 and kappa_{w_a} is bounded, the remainder transport
    T_R on its maximal domain D_R is bijective onto R with ||T_R^{-1}|| <= 1/kappa_* (characteristic formula through the
    weighted flow group).
  - Lemma C'3 (CONDITIONAL THEOREM, V046; the hypotheses hold for the modal field, V047, V055, V077): under (A), (L) and kappa_* > 0, T : Z -> Y is an isomorphism
    with the exact lower-triangular form [A, 0; Err, T_R] and the explicit inverse E gamma + f -> E A^{-1} gamma +
    T_R^{-1}(f - Err A^{-1} gamma). J is continuous on Z, and restricting to J = 0 leaves a closed range of codimension
    one (for the full normalized linearization the restriction to J = 0 has index -1, V087; see 1.6).
  - Lemma C'4 (THEOREM, V047): c[E beta + h_R] = (1/4) int e^{2t} beta dt + (1/pi) int sin(3 theta) r^{-3} h_R dX,
    bounded on Z. On R the sharp Cauchy-Schwarz constant is
    c_R = (1/pi)(int |cos theta|^{2a} sin^2(3 theta) dtheta)^{1/2}(2/9 + 4/11)^{1/2} = 0.2075698661066814348... < 0.207570
    (evaluated at 384 and 768 bits).
  - Why the strain term belongs to the coupling (THEOREM, V044). The fixed-strain operator L_fix = T + U[.].grad rho~
    does not map Z into Y: for h = x^4 y eta_0(r) with eta_0 >= 0 supported in 2 < r < 3 (so h is in R, J = 0 and
    c[h] = (3/16) int r^3 eta_0 dr > 0), L_fix h = -c[h] x^2 y + O(r^5) near 0, and a constant axis factor is not in G.
    The profile H_0 is not in Y either, so c[.] H_0 is not a bounded perturbation into Y. With the strain term in the
    coupling the image of this h is in Y. Theorem C' therefore cannot be read off from Theorem R plus a rank-one term.
  - The coupling and its three hypotheses. C h := [U[h] + chi_0 (c[h]/3) X].grad rho~, with chi_0 a fixed cutoff equal
    to 1 near 0. When C h is in Y, write C h = E gamma_C[h] + C_R h. (E0): C maps Z boundedly into Y. (E-J): the jet
    part h -> gamma_C[h] is compact from Z to G. (E-G): C_R is bounded on R and, for every eps > 0, there is a compact
    K_eps with Re <C_R h, h> <= int (b_+ + eps)|h|^2 w_a + Re <K_eps h, h>, where b_+ = (|grad rho~| - d_y rho~)/2 >= 0.
  - (E-J) (THEOREM under (A), V049). With rho~ = x^2 rho_2(y) + O(x^4), alpha(t) := rho_2(e^t) e^{-t} and
    T_h(y) = U_2[h](0, y), the jet row is Gamma h = (alpha + alpha') T_h/y - 2 alpha T_h' + c[h] chi_0 (alpha + alpha'/3). It is
    Hilbert-Schmidt from E B (+) R to G. Near 0, T_h - c[h] y = O(y^3), because a > 4 makes the third derivative of the
    trace a bounded functional on R. At infinity the functional norms of T_h^{(j)}(y) on R decay like y^{eta/2 - 1 - j}.
  - (E0), jet inputs (THEOREM, V050): beta -> C(E beta) is Hilbert-Schmidt from B to Y.
  - (E0), remainder inputs (THEOREM, V051). With the radial lift, D h := U[h].grad rho~ - x^2 y gamma_U[h](log r) is
    bounded on R. It is the sum of a part D_near whose output on the annulus r_0 <= r < 2 r_0 is bounded by
    C min(r_0^2, r_0^{k-1}) times the norm of the input on r_0/8 < r < 8 r_0, and a Hilbert-Schmidt part (separated
    scales). Outer sources acting near the origin need the exact cancellation of the linear strain and a > 4. C_R - D
    is bounded of rank one. The separated outside-to-inside strip piece proved first (V045) is a special case.
  - (E-G) (THEOREM, V052). The output tails at 0 and at infinity are small in operator norm. On a fixed annulus, the
    output near the axis is small: input in a strip |x| < eps_0 contributes O(eps_0) by the strip estimate (V026), and
    the separated input contributes O(delta^{1/4}) on |x| < delta, with delta -> 0 taken first. On the remaining compact
    set away from the axis, the weight conjugation and the jet subtraction are compact, and the exact quadratic form of
    the Riesz products has the bulk matrix [[-d_y rho~, d_x rho~/2], [d_x rho~/2, 0]], whose largest eigenvalue is b_+.
    No weighted singular-integral theorem for the non-A_2 weight |cos theta|^{-2a} is used.
  - Background hypotheses of V049 to V052, and their verification (THEOREM, V053). They are uniform C^5 bounds of
    rho~(r_0 X)/d(r_0) on the annulus 1/32 <= |X| <= 32 for all r_0 > 0 (d = r_0^3 for r_0 <= 1 and r_0^k for r_0 >= 1),
    and endpoint bounds of the cofactor rho~/(x^2 y). V053 verifies them for the exact normalized modal density from the
    original data: an independent exact-rational recomputation of the inner and outer matching of all 260 modes (3640
    join equations at orders 0 to 6), the scalar repair identities, the outer exponents and the strict logarithmic gaps.
    rho~ is not C^5 at 0 (V036), which the scaled annular bound allows. All constants in V049 to V053 are finite and
    uncomputed.
  - Conclusion (THEOREM: V047 with its coupling hypotheses supplied by V049 to V053 and its two pointwise hypotheses
    certified by V077). For the exact
    normalized modal background, assume (A) and (M) m_a := ess inf (kappa_{w_a} - b_+) > 0. Then:
    (i) L_ren = T + C : Z -> Y is Fredholm of index 0;
    (ii) the bordered operator L_red := L_ren + c[.] zeta of 4.3 is Fredholm of index 0 from Z to Y (zeta is in Y,
         V047), so L_red is invertible if and only if it is injective;
    (iii) for each eps in (0, m_a) there is a compact K_eps with (m_a - eps)||h|| <= ||P_R L_ren h|| + ||K_eps h|| on D_R.
    Proof: the homotopy T_R + s C_R, 0 <= s <= 1, is upper semi-Fredholm along the whole path by (E-G) and the transport
    energy identity, and starts at the isomorphism T_R, so its index stays 0. The operator is block lower-triangular
    plus the compact jet coupling; it factors through the isomorphism A of the axis row, and the lower off-diagonal block
    need only be bounded. The bordering is rank one because c is bounded on Z. No adjoint estimate is needed.
    The two remaining hypotheses are pointwise inequalities for the explicit background: (A) is an enclosure of
    d = V_2(0, y)/y and d' along the axis with the endpoint expansions, and (M) is the anisotropic margin. (M) implies
    kappa_* >= m_a > 0, because b_+ >= 0.
- Answer: a domain exists that is consistent with every necessary condition found, on which the normalization is
  continuous and the modal residual lies in the target. On it the full normalized linearization of the exact modal
  background is Fredholm of index 0 (THEOREM, V047 with V049 to V053, V055 and V077). The two pointwise hypotheses are
  certified by an independent original-data ball-arithmetic computation (V077): d >= 5.5752 on the whole y-axis and
  m_a >= 0.53072, raised to m_a >= 5/2 by its refinement (V086); with the qualitative endpoint
  estimates of V055 this closes (A) and (M). A second box
  computation (1569 radial cells times 64 angular boxes, every cell computed, no negative or nonfinite box) gives the
  quantitative endpoint values used for constants: d lies in
  [5.575203, 21.301451] on the whole y-axis, with sup_{t <= 0} |d - D| e^{-2t} <= 0.100883,
  sup_{t <= 0} |d'| e^{-2t} <= 0.202073, sup_{t >= 0} |d - c_l| e^{(1-k)t} <= 89.3342 and
  sup_{t >= 0} |d'| e^{(1-k)t} <= 73.3113 (t = log y), m_a >= 0.965918 (refined by that code to 2.871539, computed
  once; the best certified value is 3, V259, superseding 2.9270, V197; the earlier 5/2, V086, remains true) and kappa_* >= 3.037693. The method of
  this computation is confirmed (V061, V068; the first script for (A) had coverage and underflow defects, V054). V072
  confirms complete coverage of all 100416 boxes, retention of every refined array and the directed
  aggregation, reproducing the exact dyadic minima 0.9659182260060386 (m_a) and 5.575203976688894 (d), conditional on the
  exported cell enclosures (V072); these sharper values keep that one-computation status.
  Invertibility, that is injectivity, is OPEN. The compact operators in (E-J), (E0) and (E-G) are
  qualitative, so a quantitative inverse bound needs new explicit estimates (section 6.2).

2.4 Above L^2: which high norm can be inverted.
- Frozen thresholds (DERIVED, with grid evidence). For an H^s energy, the commutator symbol s nu^T DV nu and the
  coupling symbol p(X, nu) = nu^T [[-d_y rho_bar, d_x rho_bar/2], [d_x rho_bar/2, 0]] nu must be maximized jointly over
  directions nu; at the source this reproduces the verified window s < 2373/680 (V011), while bounding them separately
  fails there. At the actual source the frozen threshold is about 3.5785 and it is sharp (V064). At the origin, conormal derivatives x d_x, y d_y cost nothing. Ordinary y-derivatives across the x-axis
  cost s D, which gives s < (b_0 + aA)/D (about 2.334) for a = 17/4 in the w_a energy method. At infinity scaled derivatives
  r grad cost nothing.
- Prop F4 (frozen corner singularity; THEOREM, V067, where it is called H0; it is unrelated to the Hoelder statement H0
  of section 3). For L_00 h = -A x h_x + D y h_y - h
  and f = x^4 chi(x) psi(y), with psi smooth, odd, supported in 1/2 <= |y| <= 2 and positive on (1/2, 2), and chi
  smooth, even, equal to 1 on [-1, 1], the solution h = -int_0^infinity e^{-s} f(x e^{-As}, y e^{Ds}) ds is exactly
  -C x^4 sgn(y)|y|^beta with beta = (1 + 4A)/D = 2 - 1/D and C > 0, wherever 0 < |y| < 1/2 and |x|(2|y|)^{A/D} <= 1
  (substitute u = |y| e^{Ds}). This is the next-order analogue of the verified singularity of S(b) (V028), where a source
  term without the factor x^4 produces |y|^{1/D}. Consequences: h is C^{1, 1 - 1/D} across the x-axis but not in H^s
  there for s >= 5/2 - 1/D (about 2.4531), and its cofactor h/(x^2 y) is not in H^sigma in the angle for
  sigma >= 3/2 - 1/D (about 1.4531). A source term |x|^m psi(y) gives the threshold (1 + mA)/D + 1/2. Parity alone does not
  single out m = 4: the even data |x|^m chi psi with a - 1/2 < m < 4 lie in L^2(w_a), and their thresholds decrease to the
  energy value (1 + (a - 1/2)A)/D + 1/2 = (b_0 + aA)/D = 2.33392298496953... (a = 17/4) as m decreases to a - 1/2 (V067).
  So the energy method is sharp for general weighted data even in x, and 5/2 - 1/D (about 2.4531) is the limit for the x^4 term of data
  smooth across the y-axis.
- Where the singularity lives (Lemma H1; CONDITIONAL THEOREM on (Z), V063, and a THEOREM for the actual background, since (Z)
  is certified, V080). Assume (A), the regularity of V proved in V055,
  div V = 2 c_l (exact), and (Z): V has no zero on the closed quadrant other than 0 and P, and P is a hyperbolic
  repeller. Then there are no periodic orbits or separatrix cycles in the open quadrant (Bendixson-Dulac), every interior
  orbit runs from P to infinity, and the segment (0, x_P) of the x-axis flows into the origin. The singularity of
  Prop F4 lies on the stable manifold of the origin, the segment [0, x_P), and reaches P from the left. So the binding
  order near the closed segment [0, x_P] x {0} is the corner value, and the source threshold (about 3.5785) is not binding.
  Without (Z), every compact set free of zeros of V carries a smooth, compactly supported, even escape function phi with
  V.grad phi >= 1 on it (V063, by Hahn-Banach separation and the planar limit-set theorem). Positive divergence and the
  endpoint expansions do not imply (Z) (V063), so (Z) needs its own certificate. It now has one (THEOREM, V080, details
  below), so Lemma H1 holds for the actual background. Lemma Z (THEOREM, V071)
  reduces (Z) to finite checks: at P the certified source data (V017: DV(P) = diag(w', mu), 10 < w' < 10.2,
  mu > 0.99999997; V024: ||D^2 V||_F < 0.308 on the disc of radius 99/2000 about P) give |V(X)| >= 0.992|X - P| on
  that disc, so P is its only zero and a hyperbolic repeller; near 0 a bound ||DV - diag(-A, D)|| <= delta_0 < A gives
  |V(X)| >= (A - delta_0)|X|; elsewhere positive box lower bounds of |V|/r are needed. A larger source region is
  certified independently (THEOREM, V070): on the rectangle Q = [p_- - 1/2, p_+ + 1/2] x [-1/2, 1/2], with [p_-, p_+]
  the certified bracket of x_P, ||D^2 V||_F < 1.159484 and the symmetric part of DV exceeds 0.1801 I, so
  |V(X)| >= 0.1801|X - P| on Q and P is the only zero in Q. The production box computation gives |V|/r >= 10.0988 on the
  inner half-line boxes (so no separate estimate at the origin is needed) and |V|/r >= 0.100068 on every box outside 255
  boxes near P (r about 8.4 to 9.2, theta <= 0.27); 77 boxes with a zero lower bound were not contained in Q (V072). The
  independent original-data cover settles (Z) (THEOREM, V080): 512-bit enclosures on 3276 radial times 128 angular
  boxes and both analytic half-lines, exact refinement of the 108 unresolved boxes, and a separate 640-bit audit of
  coverage, partitions and exclusions leave no unresolved box; 47 terminal boxes lie in the exact Q, and outside Q, in
  the closed first quadrant away from 0, |V|/r >= 3/12500. So the zeros of V in the plane are exactly 0 and the two
  source points. No quantitative escape constant follows. The rescaling estimate for the transfer from the frozen saddle to the
  full operator is correct (near 0 the coupling and the rank-one term are O(lambda^{-2}) at scale 1/lambda), but it does
  not control the globally selected inverse or its corner coefficient, so the transfer is OPEN (V067). It is not on the
  critical path: the order proposed below is under the frozen thresholds whatever the outcome.
- The corner threshold in the cylinder norm (THEOREM for the frozen operator, V079). Near the origin the high space
  measures v = r^{-(3+delta)} h in H^s(dt dtheta), t = log r, delta the origin exponent. Conjugation gives
  r^{-(3+delta)} L_00 r^{3+delta} = a d_t + b d_theta + (3 + delta) a - 1 with a = -A cos^2 + D sin^2,
  b = (A + D) sin cos, and the energy of theta-derivatives of order s at the x-axis direction has the constant
  (A + D)(s - 3/2 - delta A/(A + D)) (using 3A + 1 = A + D). So the cylinder threshold is
  s_x(delta) = 3/2 + delta A/(A + D), attained by the homogeneous solutions x^{2 + delta D/(A+D)} y^{1 + delta A/(A+D)}.
  It is sharp for the low-domain inverse: a cone-supported forcing x^{3+delta+tau} chi(x) phi(y/x), in the target with
  every finite cylinder order, has as its unique low-domain solution a nonzero multiple of x^{B - nu} sgn(y)|y|^nu near
  an x-axis segment, nu = 1 + (delta + tau) A/(A + D), whose Sobolev threshold at delta = 3/2, tau = 1/10 is
  2.0164 < 21/10. The Cartesian threshold (about 2.334) above belongs to a different norm and does not imply this one
  (REFUTED as an implication, V079). Since the mapping side needs delta < 2, the order near the segment is 2 + eps with
  eps < 2A/(A+D) - 1/2 = 0.14547 and delta > (A + D)(1/2 + eps)/A; delta = 9/5 with order 41/20 passes with energy margin
  0.97. The earlier choice delta = 3/2, order 21/10 is excluded. No transfer to the nonlocal operator is claimed.
- Frozen regularization (THEOREM, V103, V104). Below the threshold the frozen low solution is regular, not only a
  priori bounded. In t = log x, z = y/x, h = x^(3+delta) u the frozen x-axis operator is P = -A d_t + (A + D) z d_z -
  (1 + A(3 + delta)); its exact transport group contracts H^s at the rate kappa_s = 1 + A(3 + delta) + (A + D)/2 -
  s(A + D), and the truncated resolvent integrals converge both in the selected low space and in H^s, so the low
  solution satisfies ||u||_{H^s} <= ||F||_{H^s}/kappa_s; at delta = 9/5, s = 41/20, kappa_s = 0.97260878 and
  1/kappa_s = 1.02816263 (V103). For the vertical remainder cofactor (t = log y, z = x/y, h = x^2 y^(1+delta) u) two
  normal derivatives of the resolvent converge at the rate 3(A + D)/2 - D delta = 8.83565 at delta = 9/5, the low weight
  forces u(0) = u_z(0) = 0, and a regularized Fourier argument recovers tangential derivatives: the low solution with
  an H^s cofactor right side is locally H^s on bounded vertical strips for every finite s >= 2, with the two-normal-
  derivative bound 1/8.83565 and a finite uncomputed full constant (V104). Both need the complete localized right
  side, including (V.grad chi) h, in the stated space; transition propagation, the free jet and the variable nonlocal
  operator are not covered.
- Consequence for the high space (Theorem H, DERIVED outline, OPEN). The order must vary: 2 + eps (eps < 0.14547, with
  the origin exponent delta in ((A+D)(1/2 + eps)/A, 2)) on a neighbourhood, in the polar blow-up of the origin, of the
  closed segment [0, x_P] x {0}, conormal order N near the y-axis and scaled order N at infinity,
  nondecreasing along the flow. A Conley-Lyapunov function with values 0 at P, 1 and 2 at the two directions of the
  blown-up origin and 3 at infinity orders the transitions, an escape function absorbs the losses away from these
  critical elements, and the nonlocal coupling is triangular between nested regions because commutators of cutoffs with
  the Riesz operators have order -1. Order 2 + eps gives grad h in C^eps, which suffices for a Lipschitz velocity.
  The statement must be an inverse-regularity estimate: for f in Y_H the low solution h = L_red^{-1} f lies in the
  high space with ||h|| <= K_H ||f||_{Y_H}, or equivalently L_red is an isomorphism from the graph domain
  {h : h high, L_red h in Y_H} onto Y_H. A bounded forward map between spaces of the same order is false: a compact
  packet N^{-s} eta e^{i N xi.X} at a regular point has bounded H^s norm and an image of H^s norm about N (REFUTED,
  V074). The graph domains may also depend on the velocity: the maximal H^s domains of d_x - 1 and d_x + eps d_y - 1
  differ for every eps != 0 (V074). The two-norm iteration needs only the solution operators and the low comparison.
  Further hypotheses that the proof needs (DERIVED requirements, not verification records): (i) global
  weighted high-order control of the combined coupling and normalization terms; smoothness of the normalization
  profile is not enough, since for u = -Delta v with v on annuli tending to infinity, high angular frequencies, u in the
  low space but not in the high one and c[u] = 0, the operator L_0 + eps c[.] L_0 u has the low inverse
  L_0^{-1} f - eps c[L_0^{-1} f] u, with the same frozen data and no high regularity; for L_red the normalization part
  holds, since zeta lies in Y intersect H_base^sigma for 0 < delta < 2, gamma > 2k - 1, sigma < 13/2 (THEOREM, V084),
  while a one-order gain of the full coupling is false (REFUTED, V085: parity-symmetric packets N^{-s} phi cos(N x) on a
  regular patch with rho_y > 0, bounded in H^s, zero cubic and tail coordinates, whose images have localized H^{s+1}
  norms growing at least linearly in N; order-zero multiplier (rho_x xi_1 xi_2 - rho_y xi_1^2)/|xi|^2), so the high
  energy must keep the full order-zero principal coupling (joint symbol), with smoothing only for commutators and
  separated-support pieces; (ii) the regularization step from the low
  domain to the high space, which an a priori estimate does not give. A spectral-parameter continuation (Lemma H-spec;
  the weighted Hilbert-space theory in the accompanying artifacts, section 6.6) is CONFIRMED as an abstract theorem (V106): if C maps a high space X_H boundedly
  into Y_H, ||(T - lambda)^{-1}||_{Y_H -> X_H} <= M/(lambda - omega) for lambda > omega, and the high a priori estimate
  with a compact error holds for T + C - lambda, 0 <= lambda <= omega + 1 + 2M||C||, then T + C is Fredholm of index 0
  on the high graph domain (Kato's stability of the semi-Fredholm index along lambda, from the isomorphism at the
  large end). Its direct application with the physical identity shift on the spaces with a free cubic coordinate is
  REFUTED (V106): the cubic direction x^2 y chi_0 lies in the intended high domain but not in the target, and
  subtracting the cubic coordinate kills that direction, so no O(1/lambda) inverse bound holds. The restated form
  (CONDITIONAL THEOREM, V108) applies the lemma only to the remainder block S_1 = T_R + C_R of Theorem C',
  for which the characteristic formula gives the resolvent bound when the order is nondecreasing along the flow, and
  splits the jet row off by the triangular form of Theorem C' (Corollary H-spec): with the jet domain
  B_H := {beta in B : A beta in Gamma_H}, the lower off-diagonal block bounded into the high target, the jet coupling
  compact into Gamma_H and zeta in the high target, L_red is Fredholm of index 0 on the high domain, and injectivity
  on Z makes it an isomorphism whose inverse is the low inverse. The jet row cannot be shifted with the remainder: a
  cutoff cubic profile H chi (chi = 1 near the origin end) is in B and not in Gamma, and on {J = 0} the shifted scalar
  row A - lambda has index -1 for 0 <= lambda < D/4, is an isomorphism for lambda > D/4 and has dense nonclosed range
  at D/4, which lies in [5.325362610641, 5.325362610642] (THEOREM, V109), so a full shift would cross a non-Fredholm
  point. The hypotheses of the
  restated form (the resolvent bound, the high a priori estimate and the three jet-row conditions) are not proved for
  the actual spaces, so the regularization step is OPEN. By the dilation commutation (y d_y)^j T_h = T_{(X.grad)^j h}
  of the axis trace and the majorants of V105, the jet-row conditions reduce to radial conormal regularity of the
  remainder in a sector around the y-axis, with only the base norm outside it (DERIVED). This reduction is now proved,
  and all three jet-row conditions hold on one explicit candidate (THEOREM, V112 to V118). (a) The dilation identity
  (y d_y)^j T_h = T_{(X.grad)^j h} holds on the exact X.grad graph domain. For N <= 6 the remainder axis row is compact
  from R_(max(N-2,0),s) into H_g^N, where R_(m,s) requires m dilation derivatives of the remainder in a vertical
  sector (V112), and the free-jet row is Hilbert-Schmidt on {beta in B : A beta in H_g^N} (V113). (b) The base order
  25/4 supplies the four sector derivatives, by the even-function Hardy inequality
  || |x|^(-9/4) (f - f(0)) ||_2 <= C_H || |D|^(9/4) f ||_2 with C_H^2 about 4.14643 (V114). (c) The integer target H^6
  is too weak for J1 when the remainder target has local order 25/4: beta_n = n^(-7) chi(t) cos(nt) is bounded in the
  scalar domain, and the derivative term of the lower block grows like n^(1/4) (REFUTED as a choice, V115). (d) The
  trace has the exact weighted gain a - 1/2 = 15/4 in the angular weight, so the full axis row is compact into the
  uniformly localized space of order 25/4 (V116). With the endpoint weights e^(9t/5) at the origin end and
  e^(-7t/2) at infinity, the scalar target Gamma_H = a H^(25/4) has the graph domain {J chi + a v : v in H^(29/4)}, while
  the unweighted localized space fails the lower block at the origin end (beta = r^(1/2) chi_-; V117). (e) With
  R_H = R_base + Q, where R_base = {x^2 y a u : u in H^(25/4), u = 0 on the y-axis} and
  Q = {r^3 a v : v in H^(41/20), supp v in |cos theta| >= epsilon}, and a sector cutoff inside |cos theta| < epsilon,
  J1 (into R_base), J2 and J3 hold (V118). Remaining for the high inverse: (H1) to (H3) for the remainder block and
  low injectivity. For the sharp sum R_H, (H1) fails. A first argument, through a one-sided conormal singularity
  (|cos theta| - epsilon)_+^m of v and a supposedly two-sided order -1 commutator term, is false: the coupling of a
  one-sided conormal power is smooth on the other side, because the principal normal multiplier is 1/xi (REFUTED,
  V124). The failure is proved instead with packets of scale tau and amplitude
  tau^(41/20) inside the cone: their R_H plus T_R graph norm is bounded, and the sixth derivative of the coupling on
  the high-order side is of size tau^(-59/20) (REFUTED as a choice, V119). A smooth order function s = F(Lambda), with Lambda the Conley-Lyapunov
  function of 6.4, s = 25/4 on a fixed sector around the y-axis and s <= 41/20 near the x-axis segment and the source,
  gives a variable-order space on which order-zero pseudodifferential operators are bounded. It contains R_base and
  makes the transport resolvent a composition bound with order nondecreasing along the flow. J1 to J3 carry over
  (DERIVED). (f) (H2) on the variable-order space (DERIVED, not yet checked). Let H_var be normed by
  ||Op(<xi>^(25/4)) psi_1 u|| + ||Op(<xi>^(s(x))) psi_2 v|| (plus L^2 terms) on the cylinder (t, theta), with
  u = h/(x^2 y a) on a sector psi_1 around the y-axis, v = h/(r^3 a) elsewhere, s smooth, 41/20 <= s <= 25/4, s = 25/4 on
  the sector and V.grad s >= 0. Then R_base is in H_var, H_var is in R, J1 to J3 hold with target H_var, and there is a
  finite omega_H such that T_R - lambda maps D_H = {h in H_var : T h in H_var} onto H_var with inverse norm at most
  (lambda - omega_H)^(-1) for lambda > omega_H. Proof: energy estimate with the regularized operators
  Op(<xi>^(s(x)) <delta xi>^(-8)) and a radial weight cutoff, uniformly in delta; the commutator with the transport has
  symbol s nu^T DV nu - 8 delta^2 xi^T DV xi/<delta xi>^2 - (V.grad s) log<xi>, whose last term is nonpositive (sharp
  Garding); the low solution of Lemma C'2 is then in H_var by weak compactness. The sign condition is the only place
  where the order function enters, and it is stable under small C^1 perturbations of the field if F' vanishes near the
  critical values. omega_H is not computed. Verification: with only five coefficient derivatives the
  regularized calculus and the uniform regularizer estimate fail (REFUTED, V127); the repaired proof uses the dyadic
  norm sum_j ||2^(j s(x)) Delta_j v||^2 + sum_j 2^(2 j sigma)||Delta_j w||^2, in which the flow derivative of 2^(j s(x))
  is the exact nonpositive term -j log 2 (W.grad s), no sharp Garding step, and the W^(7,infinity) regularity of the
  actual cylinder coefficients (THEOREM under W.grad s >= 0, V129). (H1) on the same space X_s is a THEOREM (V126:
  the identity U_1[x^2 w]/x = x U_1[w] + 2 [U_1, x] w + x^(-1) [[U_1, x], x] w, six radial Schur estimates, the
  normalized strain paired with U before the inner annuli are summed). (f') Existence of the order function (THEOREM, V132; an
  independent construction by radial blow-up with a smooth escape function, V130). Let B be a closed reflection-invariant repeller block: a strip {|theta| <= beta(t)} around the x-axis
  segment, of constant width as t -> -infinity and widening toward P, joined to the disc |X - P| <= 1/4 and rounded.
  W points strictly out of B: near the origin because d_theta vartheta -> (A + D) cos 2theta, along the segment because
  V_1(x, 0) < 0 there (the width grows fast enough to dominate any sign of d_theta vartheta), and on the circle
  because the symmetric part of DV exceeds 0.1801 there (V070). The backward exit time tau_B satisfies W.grad tau_B = 1.
  With G(tau_B) for a smooth step G, mollified at a small fixed scale, and s = 41/20 + (25/4 - 41/20) F(g_e), one gets
  W.grad s >= 0, s = 41/20 on a uniform neighbourhood of the closed segments and the sources, and s = 25/4 at distance
  > pi/24 from B, in particular on |cos theta| < 1/2 and for large t. The only dynamical inputs are the three
  verified facts just named. (g) The structure of (H3) on H_var
  (DERIVED outline; the frozen computation in it is submitted for checking; the impossibility of a pure energy
  estimate is CONFIRMED independently, V128). The plain energy form fails: at the
  vertical-axis end of the origin, the energy coefficient of the order-sigma factored equation in the frequency direction
  nu = (nu_t, nu_theta) is -(A + D)/2 - delta D + sigma (A + D) nu_theta^2, which is -54.07 for radial frequencies at
  every order (V088 is the angular case, 142.51). Those directions are elliptic for the transport, so the high-frequency
  condition is a positive margin on the characteristic set only. The ends need the normal families. At the origin end,
  after Fourier transform in t, the frozen family vartheta_0 d_theta + c + i xi q_0 - lambda on the angular space is an
  ODE on the quarter circle; it is bijective for every real xi when Re lambda > max(-m_x, -m_y, delta D - 2(A + D)) =
  -0.9726, so for every lambda >= 0 (m_x = 0.9726 and m_y = 142.51 are the margins of V079 and V088). The axis zero and the
  parity are both needed: without them the Taylor points lambda = delta D = 38.34 (the jet) and delta D - (A + D) = 6.89
  would lie on the path of Lemma H-spec. The far end is invertible for Re lambda > -3.7877. With the radial-source
  estimate at P below threshold (joint margin 4.52536 at 41/20, V134) and the escape weight elsewhere, the standard
  variable-order propagation argument then gives (H3) with a compact error for every lambda >= 0. The coercive and
  elliptic cones at the vertical end must overlap (the energy is -4.92 at |nu_theta| = 1/2 and vanishes at 0.52445).
  Verified since: the normal family is bijective for each fixed frequency (V131) and uniformly in the frequency for the
  exact normal operator (V133), and the selected principal inverses at the vertical, horizontal and far ends are stable
  under the actual small coefficient errors (V135, V137). A first-order coefficient error is not small in the graph
  norm (R_eps = eps d_theta against d_t - 1 on n^(-s) chi(t) e^(i n theta)), so these end inverses are proved by
  energy arguments, not by a Neumann series. Proposition H3-red (CONDITIONAL THEOREM, CONFIRMED conditional on
  (Hs_eps), V141): with
  N_0(h) = ||h/(b cos^4 theta)||_{L^2(dt dtheta)} (near the origin N_0(h)^2 = int |h|^2 |x|^(-8) r^(-18/5) dX), the
  identity -Re <T_R g, g>_{N_0} = int kappa |g/(b cos^4 theta)|^2 dt dtheta holds exactly for the actual field, with
  kappa = 1 + c_l - (1 + (log b)') q + 4 vartheta tan theta (from div V = 2 c_l); kappa tends to
  (3 Sigma/2 + delta A) cos^2 theta + (3 Sigma/2 - delta D) sin^2 theta = 65.45 cos^2 theta + 8.84 sin^2 theta at the
  origin and to 1 + c_l/2 = 3.79 at infinity. With Hardy at the axis, interpolation, and the tail bound of the coupling
  in N_0 from the annular estimates of V126, this shows that (Hs_eps): ||h||_s <= C (||(S - lambda) h||_s + ||h||_{s-eps})
  on D_H implies (H3) with K compact into X_{s-eps} (+) N_0. The single and the unweighted factors fail: the
  vertical limit energy is -116.97 + a Sigma for the weight cos^(-2a) theta, positive only for a > 3.719, and Hardy
  needs a < 9/2. Lemma Hs-sym (THEOREM, V144): with the escape function Lambda of V130 (values 0, 1, 2, 3 at the
  sources, the horizontal and vertical origin points and infinity, W.grad Lambda > 0 elsewhere) and the energy
  symbols m_v = 1 + c_l - (1 + beta) q - s nu^T DW nu - p_0 of the bulk (p_0 the coupling symbol) and m_u (two more zeroth-order terms, order
  sigma) of the cofactor, for every mu < m_x = 0.9726 there are N and L_0 with m + N W.grad Lambda + L_0 (W.nu)^2 >= mu
  on the compactified cosphere bundle. The proof is a compactness argument from the five characteristic margins over
  the critical set: 4.52536 at the sources (all covectors), 0.9726 at the horizontal origin points, 79.60 (bulk at
  order 25/4) and 142.51 (cofactor) at the vertical origin points, 3.79 at infinity. At the vertical origin points
  L_0 >= 0.258 + mu/D^2 suffices, replacing the overlapping cones. Every term of
  the inequality is a quadratic form in the covector, so it is the pointwise matrix inequality M(X) >= mu I, and its
  quantization through the Riesz vector R = grad <D>^(-1) (R^* R = I - <D>^(-2)) is <M R w, R w> >= mu ||w||^2 minus a
  lower norm, with no Garding inequality; the logarithmic term is handled by splitting log<D> as a square plus a
  low-frequency remainder. Independently, the scalar positivity and logarithmic steps hold with an H^(-1/32) form
  remainder for the actual symbols at their finite regularity (THEOREM, V145, positive smoothing and sharp Garding).
  Proposition Hs (THEOREM, V151, with the inputs V144 to V150). The four calculus inputs are proved for the
  actual coefficients: (Q0) the order reduction A_v = Op(e^(N Lambda) <xi>^(s(X))), ||v||_{H^s} <= C (||A_v v|| +
  ||v||_{H^(s-eps)}) without invertibility of the bare quantization, negative-order bounds, and the sector support
  correction (R A_u u is not supported where u is; its part outside a larger sector is smoothing) (V146); (Q2) the
  coupling forms equal <P R w, R w> and <P R z, R z> modulo eta ||h||^2 and a compact seminorm, by smooth
  approximation of the H^(51/8) coefficients in multiplier norm (V147); (Q5') ||W.R w|| + ||W.R z|| <= C ||f|| +
  a ||h||_{X_s} + C_a ||h||_{X_(s-eps)} for every a > 0, and C_R bounded on X_(s-eps) (V148); (Q1) -Re <A P v, A v> >=
  <M_B R A v, R A v> - eta ||v||^2 - C_eta ||v||_{H^(s-eps)} ||v||_{H^s} for P = B.grad + c with W^(7,inf) coefficients,
  by a Taylor expansion of the coefficients to degree 6 inside the kernel (the C^(6,1/2) remainder times the
  order-25/4 kernel is O(|z|^(-7/4)), integrable in two dimensions), with the logarithmic coefficient B.grad s >= 0 kept
  exact (V149), on the maximal domain {v, P v in H^s} by Friedrichs regularization of the conjugated equation (V150).
  Then the bulk estimate, the cofactor estimate (triangular in the bulk through the cutoff term) and the penalty
  bounded through the equation give (Hs_eps) with an added compact term, once L_0 is fixed before the small
  parameters a, eta. With V139 and
  V140 (THEOREMS) the ends are controlled at full order with a core error, which is consistent with but does not
  replace (Hs_eps), since a local core estimate would be circular along the flow through the inner end. The assembly
  is CONFIRMED (V151, with the explicit order of the small choices: N and L_0 first, then a, eta and theta), and
  H3-red retains the added compact term. High Fredholm theorem (THEOREM, V152): on the exact maximal domain
  D_s = {h in X_s : T h in X_s}, S - lambda : D_s -> X_s is Fredholm of index 0 for every lambda >= 0; with the scalar
  domain B_H = {J chi_0 + a v : J in R, v in H^(29/4)}, a = e^(-3t) b, and Gamma_H = a H^(25/4), the operators
  L_ren and L_red = L_ren + c[.] zeta (zeta the actual moving-tail vector) are Fredholm of index 0 from B_H (+) D_s to
  Gamma_H (+) X_s. If the low realization is injective, the high one is bijective and its inverse is the restriction
  of the low inverse. Not covered: low injectivity, every constant (C_s, the compact maps, the inverse norm).
  (iii) Tame dependence on the perturbation for uniformity (C^1 control of the coefficients does not bound high-order
  constants). Status: the order of V132 is robustly monotone, W.grad s >= kappa_s |grad s|, so (W + B).grad s >= 0
  for ||B||_inf <= kappa_s/2, and the matrix margin of Lemma Hs-sym loses at most (1 + sigma) ||DB||_inf + ||d||_inf +
  N ||grad Lambda||_inf ||B||_inf + L_0 (2 ||W||_inf ||B||_inf + ||B||_inf^2) with N and L_0 fixed, d the change of the
  zeroth-order coefficient (THEOREM, V154); Re <ell log<D> w, w> >= -C ||w||^2_{H^(-alpha/64)} for ell >= 0 in
  C^(1,alpha) (THEOREM, V155); the full variable-order Kato-Ponce bound for [A, B.grad] is false, by a localized
  packet with bounded H^s norm and commutator of size log n (REFUTED, V153). A uniform version of Proposition Hs
  therefore keeps (W + B).grad s as one logarithmic coefficient and needs a tame bound for the coefficient
  commutators and global weighted bounds for the perturbation velocity. Both are now proved: the velocity bounds
  (THEOREM, V156), the square-summed commutator bound (THEOREM, V157) and the dyadic energy (THEOREM, V158) give the
  uniform compact-error estimate for the frozen-coupling family S_g on the maximal domains D_g (THEOREM, V159), and
  generation, index 0 and, under injectivity of S_0, a uniform inverse (THEOREM, V160); the single-operator route with
  the tame bound of Lemma K is a second CONFIRMED proof (V161, V163; one sign in an auxiliary N_0 energy corrected,
  V162). The bordered block, the low uniform estimate and the moving background are proved as well (THEOREM, V166,
  V168 to V170; the uniform inverses are conditional on injectivity of the base low operator). Given a uniform estimate
  ||h||_H <= C_1 ||A_g h||_{Y_H} + C_2 ||h||_Z, the low bound gives ||h||_H <= (C_1 + C_2 K_L)/(1 - C_2 K_L C_prod C_E r_V)
  ||A_g h||_{Y_H} (DERIVED); surjectivity still needs the graph-domain construction. The cubic term -c[h] x^2 y that the Riesz
  velocity of a distant perturbation produces at the origin is already cancelled by the strain term inside the
  coupling (V044). Verified pieces: the principal Cartesian high-energy symbol kappa_w - p(X, nu) - s nu^T DV nu, with
  the metric caveat of the record, is CONFIRMED (V088): at delta = 9/5 the factored y-axis condition holds for orders
  above 1.71907658 (energy margin 142.5074 at 25/4), the cylinder x-axis condition for orders below 2.08092342 (margin
  0.97261 at 41/20; the value 2.0807 used earlier is corrected), and the margin at infinity is 3.78768 at gamma = -1/2.
  The rank-one construction in (i) is a valid non-implication, not a failure for the actual zeta (V089). For every
  parity-preserving C^1 field W with sup ||DW|| <= 1e-5, V + W has exactly the three zeros of V, the same saddle and
  source types, the same quadrant flow and the qualitative escape; its speed divided by r is at least 0.00023 outside
  the source rectangles, and the source moves by at most 1/1801 (THEOREM, V090). So the geometric clause of uniformity
  holds once C_V r <= 1e-5. Geometry alone does not give the uniform high inverse: T_n = (1 + n^{-beta} sin(ny)) d_x - 1,
  1 < beta < s, has L^2 inverse norm at most 1 and C^1-convergent coefficients, while ||T_n^{-1} e^{ix}||_{H^s} grows
  like n^{s - beta} (exact torus counterexample, V091). The uniform high estimate must therefore be tame in the high
  norm of the perturbation.
- The mapping side (THEOREMS). The low/high bilinear bound ||W[d].grad h||_Y <= C ||d||_{Z} ||h||_high, with the full
  velocity and exact axis subtraction, and ||D W[h]||_infinity + |c[h]| <= C_V ||h||_high hold for an explicit Hilbert
  space with cylinder-H^7 regularity of the cofactor (V057), and for a refinement that admits smooth quintic corrections
  and allows ordinary H^s, s > 2, on compact sets away from the y-axis (V060). Constants are finite and not computed.
  By Prop F4 these spaces cannot be the range of the frozen corner inverse: at the corner along the x-axis they demand
  cofactor regularity 7 > 1.4531. The same two bounds hold for a cone-local space (V065): the factored H^7 control is
  kept only near the vertical axis, and on |cos theta| >= eps, which contains the closed x-axis segment and the origin,
  a cylinder H^s bulk with any s > 2 (s = 21/10 admissible) is used. This is the mapping side of the variable-order
  space; whether the inverse maps into it is OPEN.
- A ceiling from the background (THEOREM, V069). The modal coefficients of the cofactor r^(-3) rho~ are degree-7
  splines in t = log r with C^6 joins. At the knot
  t = 4958764014967233/2^51 (r about 9.04) the seventh derivative of the exact spline coefficients jumps in the angular
  modes 0 and 1 (exact rational check), so F(rho~) and its axis-jet remainder have jumps of their sixth derivatives on a
  nonempty part of every open arc of that circle away from the axes. They lie in H^s near those arcs only for s < 13/2.
  Every orbit from the source to infinity crosses this circle and the order is nondecreasing along the flow, so every
  order used on the circle and upstream of it must be below 13/2, and the factored H^7 control near the vertical axis is
  lowered to a fractional order in (6, 13/2), which still embeds the cofactor in C^5. The mapping bounds (product,
  Lipschitz velocity, embedding into Z, classical J) hold for every factored order above 6 (THEOREM, V073); the order
  25/4 with any origin exponent in (1/4, 2), far exponent -1/2 and bulk order above 2 is admissible, so the choice
  delta = 9/5, bulk order 41/20 that the corner threshold allows is covered. The actual normalized residual
  lies in this target for every origin exponent in (0, 2) (THEOREM, V076): by the exact cofactor identity F/p = (2V_1/x + V_2/y - 1) a + q a_t + v a_theta,
  which extends across both axes, F/p = O(r^2) at the origin and O(r^{2k-4}) at infinity, and the cofactor is C^5 and
  piecewise analytic across the knot interval, hence in H^sigma for every sigma < 13/2. Membership is not a norm bound.
  This ceiling comes from the trial and is not intrinsic: a smoother spline background raises it.
- Answer: the strongest high norm compatible with the frozen conditions and with Prop F4 has variable order, about 2
  near the x-axis segment from the origin to the source and higher elsewhere (below 13/2 for the present spline
  background; 25/4 is admissible for the mapping side and for the residual, V073, V076). Near the x-axis segment the
  order is at most 2.1455 in the cylinder norm (V079); order 41/20 with origin exponent 9/5 is consistent with all
  verified constraints. Its inverse theory, in the inverse-regularity form, is proved up to injectivity: on the
  variable-order space X_s (orders 25/4 and 41/20) the remainder block, L_ren and L_red are Fredholm of index 0
  (THEOREM, V152), uniformly over small transport perturbations and over the exact moving-tail family (THEOREM, V159,
  V160, V168 to V170), and a high null vector is a low null vector, so low injectivity (OPEN) gives the high inverses;
  all constants are qualitative.

## 3. Avenue II: direct Hoelder theory

3.1 Can h be controlled directly in C^alpha?
- At each end of the flow, yes, in the right anisotropic class.
- Globally, no Hoelder inverse of L is established. Near 0 the actual (non-frozen) transport is handled by a direct
  estimate for a localized whole-plane operator (S(e) below, V206, V207); on a disk with boundary conditions it is
  OPEN. On the natural common target Y (the last bullet of 3.1) the full operator is closed but not onto (THEOREM,
  V232, V234; for every gamma > 4k and on E_2 itself, V241, V247); on the scaled far target Z_sc it is closed
  (THEOREM, V235, V244) and its exterior part is invertible (THEOREM, V236, V242), but it is not onto Z_sc either
  (THEOREM, V243, V249); on the scaled quadratic-axis target Z_2 it is closed and its exterior part is invertible
  (THEOREM, V245, V254), it is not onto Z_2 for alpha > 1/2 (THEOREM, V256, V262, V257, V265); on the joint-cofactor target Z_cof
  it is closed and its exterior part is invertible (THEOREM, V261, V268), and the global inverse is OPEN. The proposed transfer of the frozen estimate by a conjugacy was REFUTED (V028, Remark 2.1 of
  the accompanying Hoelder document); the direct estimate of V206 does not use it.
- Frozen saddle (THEOREM, V028), on the whole-plane maximal domains:
  - S(a), S(b): isotropic C^alpha has an inverse only for alpha < 1/D (about 0.0469), and this is sharp. For alpha > 1/D a
    smooth compactly supported forcing gives the bounded solution an exact |y|^{1/D} singularity along the whole
    incoming x-axis.
  - S(c): in the class C^alpha_p, whose y-Hoelder seminorm carries the weight |x|^p, T_0^{-1} is bounded if and only
    if 1 + pA > D alpha, with explicit constants and equality in the sharpness. At p = 2, the natural x^2 structure,
    every alpha < 1 is admissible.
  - H0: the weighted-sup analogue of N1. Within its weighted-sup exclusion construction, coercivity together with
    exclusion of x^2 y forces |x|^a weights with a > 2, so the y-axis jet is a coordinate in the Hoelder setting too.
    This does not classify all norms that carry a continuous cubic trace.
  - S(d), smooth-cutoff form: T_0 plus the coupling localized by a smooth cutoff chi_delta is invertible on the
    whole-plane class C^alpha_1 for alpha < (1 + A)/D (about 0.5227) and delta small. This uses the frozen T_0, excludes the
    strain column, and needs rho~ in C^4 near 0 (V036). The indicator-cutoff form is REFUTED. A statement of the
    first version, that above (1 + A)/D an x-derivative of h must enter the norm, is REFUTED by S(e).
  - S(e), the sharper local theory (THEOREM, V203 to V207; the proofs were also cross-audited independently, with no
    gap found, V212 for V203 to V206 and V216 for V207 and V208). Let E_p = C^alpha_p, 0 < alpha < 1. (i) For
    1 <= p <= 2, U_1[h]/x and U_2[h] are uniformly C^alpha in y on |x| <= 1, with norm at most C ||h||_{E_p}, without
    any derivative of h (V203 for U_1/x, V207 for U_2 and the endpoint p = 2: Fourier transform in y, the
    exponentially localized x-kernels of the y-frequency bands, and integration from x = 0 by oddness). (ii) With
    d_x rho~ = x a_1 and d_y rho~ = x^2 a_2, the complete normalized localized coupling
    chi_delta (U[h] + c[h] X/3).grad rho~ has norm O(delta^(3-p-alpha)) on E_p, 1 <= p <= 2 (V203, V204, V207), and
    on E_2 in fact norm comparable to delta^2, which is sharp (V219, by the exact strain cancellation; 4.2); the
    strain functional obeys |c[h]| <= (4/pi) max(1, 1/(p + alpha - 1)) ||h||_{E_p}, and DU[h](0) = c[h] diag(-1, 1)
    holds on E_p (V205). (iii) Since 1 + 2A - D alpha = D(1 - alpha) > 0, the frozen saddle plus this coupling is
    invertible from its maximal domain onto E_2 for every alpha < 1 and delta small (V207). (iv) The same holds when the
    frozen transport is replaced by the actual one on B_(delta/2), interpolated by a cutoff to the frozen saddle
    outside B_delta (V206, V207: after division by the x-speed the flow has x_t = e^(-t) x exactly, and the variable
    y-speed is controlled by a delayed entry time into B_delta; the factorization error is O(delta^2), V226). (v) Scope: localized operators only, qualitative
    constants, no disk realization and no global inverse; the cubic coordinate J is not closable in the E_2 graph
    norm (smooth compact k_eps with J = 1, c = 0 and graph norm O(eps^(1-alpha)), V208).
- Source (THEOREM, V013 for mu = 1 and V029 for the actual rate mu < 1): the frozen coupled source inverse maps compact
  C^alpha input to C^alpha for every 0 < alpha < 1. Above order 1 the loss is sharp (V013, at mu = 1): C^sigma maps into
  C^{sigma - (sigma - 1)/A} and no better, for 1 < sigma < g/(A - 1), and the regularity ceiling for fixed smooth
  forcing is (1 + g)/A.
- Source, the sharper local theory (THEOREM, V213 to V215). Let X_alpha = C^alpha_b intersected with L^2, with the
  maximal transport domains. (i) The frozen coupled source inverse is bounded on X_alpha for 0 < alpha < min(1, 1/mu),
  with no support restriction on the forcing; at the actual modal source (mu < 1) this is every alpha < 1, and the
  exact L^2 bound 1/[1 + (A + mu)/2] is kept (V213: first annular branch only, dyadic bounds N^(-alpha) ||f||_{C^alpha}
  at high frequency and the Bernstein bound N ||f||_{L^2} at low frequency). (ii) The actual source flow is smoothly
  conjugate near P to its linearization diag(A, mu): the Taylor degrees 2 to 11 are removed by explicit homological
  denominators, all 150 of absolute value above 0.1507, and the O(r^12) remainder by a backward-flow limit, since
  12 x 0.99 > A, the essential one being the degree-10 denominator 10 mu - A; a radial cutoff gives a global
  diffeomorphism id + O(delta^2), bounded on X_alpha, with exact transfer of the maximal transport domain (V214, with
  an original-data check of the denominators and of a disk of radius 1/1000 inside one spline span, where the trial is
  analytic). (iii) The Riesz coupling is conjugated by the pulled-back weak Poisson equation, w = P[j a_k h - (G - I) w],
  G = j A A^T, with commutator O(delta^(1-alpha)) on X_alpha; with (i) and (ii) this gives a whole-plane inverse on
  X_alpha, for every alpha < 1, of an explicit extension that equals the actual variable unnormalized source operator
  on B_(delta/2) (V215; delta depends on alpha). Scope: unnormalized; the full strain functional is unbounded in the X_alpha norm (smooth
  packets with c[h_eps] = eps^(alpha-1) c[H]; boundedness relative to the source graph norm is not decided), so only
  a prescribed scalar times the localized strain column is admissible forcing; the velocity is the L^2 multiplier
  velocity, which is the canonical one on the parity class; constants qualitative; no global patching. Independent
  cross-audits of V213 and of V214 and V215 found no gap (V221 for V213, V223 for V214 and V215).
- Strain (THEOREM, V028): c is bounded on C^alpha_p if and only if p + alpha > 1.
- Common target and global realization (THEOREM, V222, V224, V227, V228, V232, V234, V241; independent cross-audits
  found no gap, V231, V233, V237, V247; in (vi) the mapping theory on Z_sc and on Z_2, the exterior inverses, the
  range obstruction on Z_sc and the patch noncompactness are THEOREMS, V235, V236, V239, V242 to V246, V249, V254,
  the turning-height obstruction on Z_2 and its extension to every alpha > 1/2 are THEOREMS, V256, V262, V257, V265,
  the mapping theory and exterior inverse on Z_cof and the nonlinear derivative loss there are THEOREMS, V261, V268,
  V264, V271, the transport cokernel at the source on Z_2 and Z_cof is a THEOREM, V266, V272,
  and the rest is DERIVED). Fix 0 < alpha < 1 and gamma > 4k. Let E_2 be C^alpha_2 with the parity
  class and h(0, y) = 0, Y = E_2 intersected with L^2(w_gamma), w_gamma = (1 + |X|^2)^(-gamma/2), with norm
  ||h||_inf + [h]_x + [h]_(y,2) + ||h||_{L^2(w_gamma)}, where [h]_(y,2) is the y-seminorm with the global weight x^2,
  and let D_Y be the maximal transport domain. (i) Y is a Banach space, |c[h]| <= (4/pi) ||h||_Y, the residual F0 lies
  in Y (in L^2(w_gamma) exactly when gamma > 4k, not in unweighted L^2), and the cut-off origin inverse and the paired
  reflected source construction are bounded Y -> Y (V222). (ii) The renormalized coupling U[h].grad rho0 + c[h] H0 (H0
  the compact cut-off strain column; the raw column grows like r^k and is not in Y) is bounded on Y and L_ren is
  closed on D_Y: for 4k < gamma < 2 with tail C R^(k-1)(1 + log R) outside B_R (V224), and for every gamma > 4k and on
  E_2 itself with output tails of negative exponent (V241, V247; the weighted velocity theorem itself is not extended;
  the rate R^(k-1)(1 + log R) holds for every gamma > 4k and on E_2 and is sharp from below, also on the strain-zero
  inputs: THEOREM, V278 with sign clarification V281, verifier proof, independent audit recorded as V287); the
  cubic coordinate J is not closable on this graph (V224). Both exponents of C^alpha_2 are sharp for this realization
  (V229, V230, V238): for every vertical power p > 2 there is a smooth compact input with c = J = 0 and transport
  image in the p-weighted class whose coupling image is not in it, and at alpha = 1 graph-bounded source inputs have
  coupling norm of order log(1/epsilon), although there the cubic coordinate would be continuous. (iii) The
  moving-tail column m0 lies in Y (the far r^k terms cancel exactly), so
  the full chart linearization A_0 is closed on D_Y, with coupling tail O(R^(2k - gamma/2)(1 + log R)) for
  4k < gamma < 2 (on E_2 and every Y with gamma > 4k, O(R^max(2k - 1, 2k - gamma/2)(1 + log R)), V241, V247); the
  actual-variable origin extension containing the exact column costs O(delta^(3-alpha)), so the total
  factorization error stays O(delta^2) (V228, with V226). (iv) The cutoff commutator and the parametrix error
  L_ren K - chi eta are bounded but not compact on the maximal graph (flow-box packets with c = J = 0; the embedding
  of D_Y into Y is not compact), so this particular patch gives no Fredholm patching of the local inverses (V227);
  cancellation in a complete sum of patches, or another Fredholm construction, is not excluded by it, and the
  failure of surjectivity in (v) is proved by other arguments. (v) The full operator
  is not onto Y, so Y is not a valid global target (THEOREM, V232, V234; both independently cross-audited, no gap).
  First (V234): for every bounded linear B on Y whose part outside B_R tends to 0 in norm, T + B is not surjective
  from D_Y onto Y (surjectivity alone would give bounded solution choices by the open mapping theorem, so no
  injectivity is assumed); this covers L_ren and A_0. The far flow is a dilation at rate ell = 1/k, along which
  x^2 |Delta y|^alpha grows like e^((2 + alpha) ell tau), and (2 + alpha) ell > 1; a forcing concentrated near the
  x-axis at radius X0, of bounded Y norm, would produce at a fixed radius a y-quotient of order X0^(2 + alpha - k).
  Second (V232, a different mechanism): smooth forcings x^2 phi(x) y^(-b), 1/2 < b < 1, on a strip along the vertical
  axis at large height lie in D_Y and have forward characteristic integrals of size x^(k+b) at a fixed height, while
  every element of Y is O(x^2) there and the complete coupling contributes only O(x^2 log(1/x)); hence A_0, L_ren and
  T have algebraic cokernel of continuum dimension on D_Y and are not Fredholm there. This second argument uses only
  E_2, so the infinite algebraic cokernel of T, L_ren and A_0 holds on E_2 itself and on Y for every gamma > 4k
  (THEOREM, V241, independent audit V247). Neither argument concerns
  whether F0 is in the range, other targets, condition (I) of Theorem E, or existence. (vi) A candidate target with
  scaled far norms (verifier proofs V235, V236, V243, V245 and V256; called Z in the accompanying Hoelder document, 3.4(g)). Let
  Z_sc carry the E_2 norm only on a fixed disk around the origin, the scaled annular norms
  sup_j 2^(-j beta)(||h||_(L^inf(A_j)) + 2^(j alpha) [h]_(C^alpha(A_j))) on the dyadic annuli A_j, with the ordinary
  Hoelder seminorm, and the L^2(w_gamma) norm, with 0 < alpha < 1 and gamma > 4k. THEOREM (V235, independent audit
  recorded as V244): for 2k - 1 <= beta < k the residual lies in Z_sc
  (beta >= 2k - 1 is necessary, by its leading far term of degree 2k - 1), c is bounded, and the renormalized
  coupling is bounded with tail C (R^(k-1) + R^(beta + k - gamma/2)). For 2k - 1 < beta < k the moving-tail column
  lies in Z_sc and the full operator A_0 is closed on its maximal domain. At beta = 2k - 1 the column is not in Z_sc,
  because it has the far term r^(2k-1) log r S_M(theta) with a sin(1043 theta) coefficient that is positive by exact
  signs (about 4e-21, so not visible numerically); so A_0 does not map the entire transport domain into Z_sc (a
  nonmapping statement, which does not exclude a restricted closed realization), and A_0 h lies in Z_sc, for h in the
  maximal transport domain, exactly when c[h] = 0 (DERIVED in the independent audit). THEOREM (V236, independent audit recorded as V242): on the exterior {|X| > R}, R large,
  with no inner boundary condition, the actual transport has the exact inverse -int_0^inf e^(-t) f(Phi_t X) dt
  along the actual flow, with a bound uniform in R (the scaled seminorm costs k/(k - beta)). The exterior operator
  with the complete coupling, inserted through a cutoff extension, is invertible by a Neumann series. It agrees
  with A_0 only outside radius 2R. Neither obstruction mechanism of (v) transfers to Z_sc (DERIVED): the orbit argument gives
  an amplification only for beta > k, and the strip argument needs the x^2-weighted vertical seminorm at infinity.
  THEOREM (V243, independent audit V249): Z_sc is nevertheless not a valid global target. For every
  0 < alpha < 1, 2k - 1 < beta < k and gamma > 4k, T, L_ren and A_0 have infinite algebraic cokernel on their
  maximal domain in Z_sc. The forward characteristics from (x, 1/2), x small, follow the outgoing vertical axis,
  with x_t comparable to x e^(ell t) and y_t to e^(ell t). Along them the complete coupling contributes
  O(x^(1+alpha)) to the characteristic integral, because U_1[h] is odd in x. A compact forcing
  |x|^sigma phi(x) g(y) at large height, with alpha < sigma < 1 + alpha and corrected to c = J = 0, contributes
  a_sigma x^sigma with a_sigma > 0. The local E_2 factor, however, forces O(x^2) at (x, 1/2). The forcings are not
  globally smooth, and nothing is claimed about the range of the residual or about Z_2. A next target must keep scaled quadratic
  control along the whole outgoing vertical axis. THEOREM (V245, independent audit V254, at its qualitative scope): the candidate Z_2
  keeps the local E_2 factor and L^2(w_gamma) and uses on the annuli the rescaled C^alpha_2 norms
  2^(-j beta)(||h||_(L^inf(A_j)) + 2^(j alpha) [h]_x + 2^(j (2 + alpha)) [h]_(y,2)), with the horizontal quotient at
  fixed y and the x^2-weighted vertical quotient at fixed x, 2k - 1 < beta < k. Its elements are O(x^2 r^(beta - 2))
  near the vertical axis, so the forcings above are excluded. The residual lies in Z_2, the complete coupling is
  bounded with small tails, and the full operator is closed on its maximal domain. On the exterior, with no inner
  boundary condition, the actual transport is a closed bijection onto the exterior version of Z_2 for large R, with
  inverse bounded uniformly in R, and so is the exterior operator with the complete coupling inserted through the
  cutoff extension. The exterior inverse uses the positive time change a = V_1/x, along which x_t = e^t x exactly, so
  vertical pairs keep a common abscissa. THEOREM (V256, a verifier proof with an original-data interval certificate;
  independent audit recorded as V262): Z_2 is not a valid global target for larger alpha. The axis rate a(0, y) = d_x V_1(0, y),
  which goes from -A at the origin to ell at infinity, has a simple zero at a height y_* in (9.1465, 9.1468), with
  y d_y a in (7.1952, 7.1954) there. Near this turning height the near-axis orbits run parallel to the axis to second
  order, so a horizontal oscillation is sampled coherently and the x^2-weighted vertical seminorm of the preimage is
  lost. For every 2k - 1 < beta < k and gamma > 4k, T is therefore not onto Z_2 for alpha > 1/2, and A_0 and L_ren are
  not onto Z_2 for alpha > 2/3 (non-surjectivity by the open mapping theorem, not an infinite-cokernel statement, and
  nothing about the range of the residual). THEOREM (V257, verifier proof, independent audit recorded as V265): for h = x^2 g
  with g compactly supported, even in x, bounded and uniformly C^alpha in y, the divided velocity U_1[h]/x is in
  the full joint C^alpha on bounded x-strips, with no
  horizontal regularity of g; this bounds the coupling difference by C N q^2 delta^alpha and gives the same
  conclusion for A_0 and L_ren for every alpha > 1/2. Degenerate zeros are not covered; alpha <= 1/2 is OPEN for A_0 and
  L_ren (for T alone see V266 below). One remedy, alpha <= 1/2, is heuristic. The other, a divided
  horizontal seminorm near the vertical axis, is the joint-cofactor target Z_cof (THEOREM, V261, verifier proof, independent audit recorded as V268): h = x^2 g with g in the
  full joint C^alpha locally and sup_R R^(2-beta)(||g||_inf + R^alpha [g]_(C^alpha)) on the dyadic annuli, plus
  L^2(w_gamma). For every 0 < alpha < 1 and 2k - 1 < beta < k the complete coupling is bounded with a small tail,
  the residual lies in Z_cof, T, L_ren and A_0 are closed on their maximal domains, and the actual auxiliary exterior
  operator is invertible; J is not closable. The turning-height forcings are unbounded in this norm, so V256 and V257
  do not apply to it; its global inverse is OPEN. Transport alone is not onto Z_2 or Z_cof near the source (THEOREM, V266, verifier proof, independent audit recorded as V272): with DV(P) = diag(A_s, mu_s) at the source P, 10 < A_s < 51/5, the cusp profiles s_+^a phi(y/s_+^b), a = 1/A_s, b = mu_s/A_s, of the conjugated transport give smooth compact forcings with c = J = 0 that span an infinite-dimensional subspace of the cokernel of T on either target for alpha > 1/A_s, so for every alpha >= 1/10. This excludes a Neumann series around T; it says nothing about A_0 or L_ren, since the full source coupling changes the equation. The nonlinear derivative loss persists on Z_cof (THEOREM, V264, verifier proof, independent audit recorded as V271): there are smooth
  inputs h_n with c = J = 0, supported in a fixed compact set away from both axes and bounded in the graph norms of T,
  L_ren and A_0, with ||N(h_n)|| >= b n for N(h) = (U[h] + (c[h]/3) X).grad h; so N has no continuous extension at 0
  in these graph topologies. This does not exclude a quasilinear scheme, stronger derivative norms or a profile.
  A global inverse on Z_2 is OPEN. Matching an exterior inverse and the cut-off local
  inverses across the middle annuli is also OPEN. The complete error of the specified cut-off origin patch is not
  compact on Z_sc either (THEOREM, V239, independent audit V246, under the flow-box hypothesis of that patch),
  although cancellation in a sum of patches is not excluded. A
  parametrix with error of norm below 1 would give surjectivity only, and injectivity needs its own estimate. The
  middle region has no small parameter.

3.2 Admissible exponent range.

| Piece | Admissible alpha | Class | Status |
|---|---|---|---|
| frozen saddle, isotropic | alpha < 1/D, about 0.0469 (sharp) | C^alpha | THEOREM (V028) |
| frozen saddle, axis-weighted | alpha < (1 + pA)/D (sharp); every alpha < 1 for p >= 2 | C^alpha_p | THEOREM (V028) |
| saddle plus localized coupling | alpha < (1 + A)/D (about 0.5227) on C^alpha_1; every alpha < 1 on C^alpha_p, 1 <= p < 2, 1 + pA > D alpha | C^alpha_p | THEOREM (V028, V203) |
| saddle plus complete normalized localized coupling, frozen or actual transport near 0 | every 0 < alpha < 1 (J not closable in the graph norm, V208) | C^alpha_2 | THEOREM (V204 to V207) |
| normalized localized coupling alone, actual background | operator norm comparable to delta^2, every 0 < alpha < 1 | C^alpha_2 | THEOREM (V219) |
| strain functional bounded | p + alpha > 1 | C^alpha_p | THEOREM (V028) |
| coupled source at the actual rate | every 0 < alpha < 1 | compact C^alpha input | THEOREM (V029) |
| coupled source, frozen, no support restriction | 0 < alpha < min(1, 1/mu), so every alpha < 1 at the modal source | C^alpha_b intersected with L^2 | THEOREM (V213) |
| actual variable unnormalized source operator on B_(delta/2), whole-plane extension | every 0 < alpha < 1 (strain column only as prescribed forcing) | C^alpha_b intersected with L^2 | THEOREM (V214, V215) |
| pure transport at the source (no coupling), frozen | alpha < 1/A_s (about 0.0985) | illustration | DERIVED |
| infinity | weighted classes with 2k - 1 <= beta < k (beta the far scaling exponent; beta > 2k - 1 once the moving-tail column is included) | scaled C^alpha | DERIVED |
| common target Y, bounded complete coupling, closed full operator A_0 | every 0 < alpha < 1, every gamma > 4k, and E_2 itself (first proved for 4k < gamma < 2) | C^alpha_2 intersected with L^2(w_gamma) | THEOREM (V222, V224, V228; V241, V247) |
| bounded complete coupling on the transport domain, vertical weight \|x\|^p | p = 2 only (fails for every p > 2) | p-weighted C^alpha | THEOREM (V229) |
| bounded complete coupling at alpha = 1 | none (logarithmic blow-up at the source) | Lipschitz analogue of C^alpha_2 | THEOREM (V230) |
| surjectivity, hence a bounded inverse, of T, L_ren or A_0 onto Y | none (infinite algebraic cokernel, also on E_2 and for every gamma > 4k) | C^alpha_2 intersected with L^2(w_gamma) | THEOREM (V232, V234; V241, V247) |
| scaled target Z_sc: residual, bounded complete coupling, closed full operator | every 0 < alpha < 1, 2k - 1 < beta < k, gamma > 4k (at beta = 2k - 1 the column is not in Z_sc, so A_0 does not map the entire transport domain into Z_sc) | local C^alpha_2, scaled far C^alpha, L^2(w_gamma) | THEOREM (V235, V244) |
| surjectivity of T, L_ren or A_0 onto Z_sc | none (infinite algebraic cokernel) | local C^alpha_2, scaled far C^alpha, L^2(w_gamma) | THEOREM (V243, V249) |
| scaled quadratic-axis target Z_2: residual, bounded complete coupling, closed full operator, exterior inverse | every 0 < alpha < 1, 2k - 1 < beta < k, gamma > 4k | local C^alpha_2, scaled far C^alpha_2, L^2(w_gamma) | THEOREM (V245, V254) |
| surjectivity of T, L_ren or A_0 onto Z_2 | none for alpha > 1/2 (T) and for alpha > 2/3 (A_0, L_ren), by the simple turning height of the axis rate | local C^alpha_2, scaled far C^alpha_2, L^2(w_gamma) | THEOREM (V256, V262) |
| surjectivity of A_0 or L_ren onto Z_2 for 1/2 < alpha <= 2/3 | none, by the joint C^alpha bound for U_1[x^2 g]/x and the same construction | as above | THEOREM (V257, V265) |
| global inverse on Z_2; surjectivity of A_0 or L_ren for alpha <= 1/2, of T for alpha <= 1/A_s | OPEN | local C^alpha_2, scaled far C^alpha_2, L^2(w_gamma) | OPEN |
| mapping, residual membership, closed domains and actual exterior inverse on Z_cof (h = x^2 g, g in scaled joint C^alpha), every alpha < 1 | yes; turning-height forcings excluded; J not closable | x^2 times scaled joint C^alpha, L^2(w_gamma) | THEOREM (V261, V268) |
| surjectivity of T alone onto Z_2 or Z_cof | none for alpha > 1/A_s, so for every alpha >= 1/10 (source cusps, infinite algebraic cokernel; A_0, L_ren not covered) | as above | THEOREM (V266, V272) |
| global inverse on Z_cof | OPEN | as above | OPEN |
| nonlinear closure in the graphs of T, L_ren, A_0 on Z_cof | none (N not continuous at 0, J = c = 0) | Z_cof graph norms | THEOREM (V264, V271) |
| exterior inverse of the full operator on {\|X\| > R}, R large | every 0 < alpha < 1, 2k - 1 < beta < k, gamma > 4k | exterior scaled far C^alpha and L^2(w_gamma) | THEOREM (V236, V242) |
| nonlinear closure, perturbative | none for the inputs of Lemma N | solution norms controlling C^alpha of h, U[h] on a compact set and c | THEOREM (V030) |
| nonlinear closure in the localized origin graph of S(e) | none (N discontinuous at 0 from the graph norm to C^alpha_2, even with J = c = 0) | C^alpha_2 graph of L_delta | THEOREM (V211) |
| grad h across the x-axis segment from the origin to the source, data even in x | alpha > 1 - 1/D (about 0.9531) ruled out; the explicit frozen example lies in C^{1, 1 - 1/D}, so equality is attained by it (no endpoint inverse claimed) | C^{1,alpha} | THEOREM for the frozen example (Prop F4, V067); for the true operator OPEN |

Explicit constants in 3.1 and 3.2: the bound S(c), with equality in the sharpness; |c[h]| <= (4/pi) max(1,
1/(p + alpha - 1)) ||h||_{E_p} and |c[h]| <= (4/pi) ||h||_Y; the scaled exterior seminorm cost k/(k - beta); the
source L^2 bound 1/[1 + (A + mu)/2]. The other constants and radii of the localized and global statements are
qualitative (6.4).

3.3 The Riesz coupling and the source.
- Answer: at the source the coupling is not a perturbation and has to be inverted together with the transport; this is
  done for the frozen source in H^s (THEOREM, V011, V064, with a sharp threshold) and in C^alpha (THEOREM, V013,
  V029), for the actual variable source transport and coupling near P in C^alpha_b intersected with L^2, every alpha <
  1, unnormalized (THEOREM, V213 to V215; 3.1), and globally in L^2 inside the Garding estimate of Theorem C' (V052).
  Globally the renormalized coupling is bounded on the common target Y of 3.1, with tail O(R^(k-1)(1 + log R)) for 4k
  < gamma < 2 (THEOREM, V224; this tail rate holds for every gamma > 4k and on E_2 and is sharp, R^(k-1) log R from
  below as well, also on the strain-zero inputs, where C0 = C_ren: THEOREM, V278 with sign clarification V281,
  verifier proof, independent audit recorded as V287), and the complete coupling C0 = C_ren + c[.](M0 - H0) is bounded
  for every gamma > 4k and on E_2 itself, with tail O((R^(k-1) + R^(k-gamma/2) + R^(2k-1) + R^(2k-gamma/2))(1 + log
  R)) (THEOREM, V241, V247; all exponents negative; this rate is sharp, R^max(2k-1, 2k-gamma/2) log R from below as
  well, by the exact nonzero r^p log r coefficient of M0, so the faster rate of C_ren does not hold for C0: THEOREM,
  V276, verifier proof, independent audit recorded as V286); the full operator is not onto Y (THEOREM, V232, V234,
  V241); on the scaled target Z_sc of 3.1 the complete coupling is bounded with small tails (THEOREM, V235, V244), the
  full operator is not onto Z_sc either (THEOREM, V243, V249); on the scaled quadratic-axis target Z_2 the complete
  coupling is bounded, the full operator is closed and the exterior operator is invertible (THEOREM, V245, V254), the
  full operator is not onto Z_2 for alpha > 1/2 (THEOREM, V256, V262, V257, V265); on the joint-cofactor target Z_cof
  the complete coupling is bounded and the exterior operator is invertible (THEOREM, V261, V268), and a global Hoelder
  inverse is OPEN.
- Exact form (DERIVED): U[h].grad rho_bar = -(d_y rho_bar/2) h + [d_y rho_bar T_xx - d_x rho_bar T_xy] h, with T_xx, T_xy the
  principal-value convolutions with cos(2 theta)/(2 pi r^2) and sin(2 theta)/(2 pi r^2). The two Riesz factors are
  never estimated separately: this is one operator of order 0 with an explicit local part.
- Its symbol ranges over [-(d_y rho_bar + |grad rho_bar|)/2, b_+] (DERIVED; the bulk matrix is the one used in V052), with b_+ = (|grad rho_bar| - d_y rho_bar)/2. The
  local part damps where d_y rho_bar > 0, in particular at the source, where d_y rho~ = g is in (29, 30).
- Near 0 (|grad rho~| = O(r^2)) and at infinity (O(r^{k-1})) the coupling is a small perturbation (DERIVED). At the source it is
  not small, and the coupled frozen operator must be inverted as a whole. The coupling is essential there: without it
  the pure transport inverse loses Hoelder regularity above 1/A.
- The C^alpha operator norm of the principal-value part is not its symbol supremum. No Hoelder analogue of the sharp
  Garding inequality is proved or used in this work (OPEN), so the global Lyapunov argument of Theorem R has no Hoelder counterpart with the same
  constants.

3.4 Is C^alpha(h_x) genuinely unnecessary?
- For the low-order linear theory, yes at each end: the frozen saddle and the source (THEOREM, V028, V013, V029) and
  the far window (DERIVED) bound h in C^alpha (or
  C^alpha_p) by the forcing in the same class, without h_x; so do the actual exterior inverses on Z_sc, Z_2 and Z_cof
  (THEOREMS, V242, V254, V268), whose norms contain no derivative of h. At the origin this includes the complete normalized
  localized coupling and the actual transport for every alpha < 1 (S(e), THEOREM, V203 to V207); an explicit
  h = -Delta P with unbounded d_x U_1[h], for which h and the localized coupling lie in every C^alpha_p, shows that a
  bounded d_x U_1 is not needed there (V203).
- For the nonlinear closure by the explicit semilinear perturbative map, no. Lemma N (THEOREM, V030): fix 0 < alpha < 1 and a compact set K near a regular axis
  point, and let a solution norm X control ||g||_{C^alpha(K)} + ||U[g]||_{C^alpha(K)} + |c[g]|. There are smooth compact
  inputs h_n with zero strain and zero cubic coordinate, bounded in C^alpha, such that every solution of L g = N(h_n)
  has X norm tending to infinity. A map defined on X-balls fails only if these h_n are also bounded in X; a stronger
  norm can make them unbounded, so the lemma does not refute a stronger quasilinear norm (V048). Two
  crossing plane waves of amplitude n^{-alpha} interact exactly into -n^{1 - 2 alpha} sin(2 n y), and the transport
  inverse does not regain y-derivatives where V is parallel to e_1. Lemma N' (THEOREM, V030): inputs with bounded
  C^alpha graph norm can have ||N||_{C^alpha} >= c n, and so do the solutions.
- Lemma N'' (THEOREM, V211): the same failure holds in the actual graph of S(e). For both localized operators L_delta
  of S(e)(iii) and (iv) there are smooth h_n supported in a fixed compact set inside B_(delta/2), away from both axes,
  with J(h_n) = c[h_n] = 0 and bounded E_2 graph norm, but ||N(h_n)||_{E_2} >= c_1 n and
  ||L_delta^{-1} N(h_n)||_{E_2} >= c_2 n, N(h) = (U[h] + c[h] X/3).grad h. After rescaling by n^(-1/2), N is
  discontinuous at 0 from the graph norm to E_2. The construction uses a compact potential P whose velocity
  U[-Delta P] = (-P_xy, P_xx) is a constant transverse vector with zero strain on a box, characteristic strips on which
  V_delta.grad z = 0 (so the large derivative does not enter the transport term), and a two-trajectory identity for
  the inverse. This concerns these graphs only; it is not a statement about every stronger Hoelder norm. It rules out
  the semilinear perturbative fixed-point map on balls of this graph; a quasilinear iteration in which U[h].grad is
  absorbed into the transport is not excluded by it (V218).
- In the weak graph norm of the earlier diagnostic space, N is not even continuous at the certified modal source
  (THEOREM, V019).
- A sufficient high-norm requirement for a quasilinear scheme is a Lipschitz transport velocity V + W[h], that is
  D U[h] in L^infinity; the entries of D U[h] are Riesz products applied to d_x h. d_x h in C^epsilon with decay is
  sufficient (DERIVED). Necessity of a Lipschitz velocity is not claimed, and the equivalence with d_x h in C^alpha is REFUTED by
  a compact parity-compatible C^1 counterexample (V025, V038).
- Since W_1 = 0 on {x = 0} and W_2 = 0 on {y = 0}, W.grad h = (W_1/x)(x d_x h) + (W_2/y)(y d_y h). A product
  estimate, a Lipschitz bound for W and a classical continuous cubic coordinate J are now THEOREMS in explicit
  Hilbert high spaces (V057, V060; section 2.4). Those spaces demand more regularity at the corner than an inverse can
  give (Prop F4); the Hoelder exponent of grad h across the x-axis segment is limited to alpha <= 1 - 1/D for the
  frozen saddle (the explicit example lies in C^{1, 1 - 1/D}, with equality attained, and rules out every
  alpha > 1 - 1/D).

## 4. Avenue III: the singular functional c[h]

4.1 A saddle-adapted local weighted estimate.
- Answer: yes for the frozen saddle, globally in the plane at p = 2 (Theorem O, THEOREM, V022) and on boxes for every
  p in [1, inf) (Prop M, THEOREM, V034); for the actual field on boxes the sign conditions and the coercivity constant
  are NUMERICAL only, and the box estimate does not close by iteration in y (below).
- Characteristic geometry: the flow of the frozen field is Phi_s(x, y) = (x e^{-As}, y e^{Ds}), with invariant
  |x|^D |y|^A. The x-axis is incoming and the y-axis outgoing. On a box the sides x = +-R_x are inflow and the sides
  y = +-R_y are outflow. This is the opposite of an expanding model, where every side is outflow.
- Prop M (THEOREM, V034, with the domain conditions stated in the accompanying proof). For p in [1, inf), the product weight
  w = |x|^{-ap} |y|^{-bp} and an outflow cutoff phi(y), with kappa_w = 2 c_l/p + 1 - a V_1/x - b V_2/y,
     int kappa_w |h|^p w phi = - int ((V.grad - 1) h) |h|^{p-2} h w phi + (1/p) Flux_in + (1/p) int |h|^p w (-V_2 phi'),
  with Flux_in <= 0. If V_1/x < 0, V_2/y > 0 and Delta := inf kappa_w > 0 on the box, then
     N <= Delta^{-1} ||(V.grad - 1) h|| + (2 Vhat/(p Delta))^{1/p} ||h||_{L^p(S_R, w)},
  where S_R is the outflow shell. kappa_w(0) = kappa_0(p) = 2 c_l/p + 1 + A a - D b is the adjoint weight.
- The inflow flux has the good sign. The outflow flux is not small; after y-averaging it is a shell norm along the
  outgoing axis. Iterating in y does not close, because the flux is transported to the next block. The global answer
  at p = 2 is Theorem O.
- Explicit frozen strain bound, Corollary C1 (THEOREM, V034): for h with J = 0 and T_0 h = x^2 y gamma(log r) + f,
  |c_<[h]| <= 0.0027316 ||f||_R + 0.0136875 ||gamma||_G, so the constant is C_c0 < 0.013958 at a = 7/2, b = 6/5, and
  C_c0 < 0.017231 at a = 17/4, b = 0.
- Radial and isotropic moment estimates cannot be coercive at the x^2 y scale (THEOREM, V010: smooth compact packets
  with J = c = 0, unit moment norm, image moment tending to 0 and H^s norm tending to 0).
- NUMERICAL: with the actual field of rho~ on boxes Q_{2R}, the sign conditions hold and Delta stays within 26 percent of
  kappa_0 up to R = 1 (for example Delta = 13.03 at p = 2, a = 7/2, b = 6/5, R = 1). This is not yet a certified bound.

4.2 Absorbing the nonlocal velocity remainders.
- Exact strain cancellation (DERIVED, exact algebra; the counterexample below is V048): U[h] = c[h](-x, y) + U^(2)[h] near 0, and (c[h](-x, y) + (c[h]/3) X).grad(x^2 y) = 0
  exactly. Only the linear part cancels: for a compact h = x^2 y chi(r) with chi = 1 near 0 the full product contains
  x^2 y [(-1/6 + H) x^2 + (5/6 + 5H) y^2], which is never identically zero (V048, exact counterexample).
  On the y-axis the x^2 coefficient of the strain terms also cancels to leading order: with traces
  U_2[h](0, y) = c y + O(y^3) and d_x U_1[h](0, y) = -c + O(y^2), the combination is O(y^3) (THEOREM, V049, for
  inputs in the jet-plus-remainder spaces of 2.3, where a > 4 makes the third derivative of the trace bounded; these
  remainders are not claimed for the E_2 Hoelder realization of section 3, which has only weaker pointwise bounds).
- Quantitative form of the cancellation in a Hoelder class (THEOREM, V219). On E_2 = C^alpha_2 (3.1, S(e)), for the
  actual background (C^(4,1) near 0) and fixed alpha < 1, the complete normalized localized coupling satisfies
      c_0 delta^2 <= ||chi_delta (U[h] + c[h] X/3).grad rho~||_{E_2 -> E_2} <= C delta^2
  for small delta, against order delta^(1-alpha) for the same coupling without the normalization term (DERIVED:
  the two differ by the rank-one operator c[h] chi_delta X.grad rho~/3, whose E_2 norm is of exact order
  delta^(1-alpha); V207 had given delta^(1-alpha) as an upper bound for the normalized coupling). Proof idea: subtract from every y-frequency band its own strain (the band strains are absolutely
  summable to c[h]); then U_2 - c y has local y-Hoelder size C M delta^2 and U_1/x + c size C M delta, where M is the
  E_2 norm of h; the leading strain terms cancel algebraically against the divided background remainders before
  anything is estimated. Compact potentials with c = J = 0 whose x-wavelength is much shorter than their y-wavelength
  give the matching lower bound. So in this norm the exact normalization improves the earlier upper bound by the factor delta^(1+alpha); the
  Neumann error of the frozen local inverse is O(delta^2), and that of the actual-variable one is also O(delta^2)
  (THEOREM, V226: the multiplier 1/A_delta - 1/A0 has supremum O(delta^2) and gradient O(delta), and the
  supported-endpoint product estimate turns this into an E_2 operator bound O(delta^2); an independent cross-audit
  found no gap).
  Constants are qualitative; the L^2 box version of the same rate (the corner estimate (E2) in the singular-functional discussion in the accompanying
  artifacts) is not proved. An independent cross-audit found no mathematical gap (V225); its remarks are cosmetic, except that the constants are not uniform in alpha and that the sharp part of the norm is the x-seminorm.
- Parity Mellin subtraction: U_1 is odd in x and U_2 even. Subtracting x d_x U_1(0, y) and U_2(0, y) moves the
  admissible weight windows to (3/2, 7/2) and (1/2, 5/2), which is exactly 5/2 < a < 9/2 for the coupling (DERIVED,
  one-dimensional model).
- Strip estimate (THEOREM, V026, local-strip scope, 5/2 < a < 9/2, no weight in y). For inputs supported in |x| < R
  and a background with d_x rho = 2x rho_2(y) + x^3 r_1 and d_y rho = x^2 rho_2'(y) + x^4 r_2,
     ||U[h].grad rho - x^2 (2 rho_2 d_x U_1[h](0, .) + rho_2' U_2[h](0, .))|| <= eta(R) ||h||,
     eta(R) = 2 C_a R ||rho_2|| + C_a R^2 ||rho_2'|| + D_a R^3 ||r_1|| + D_a R^4 ||r_2||,
  with explicit C_a (C_a = 1759/6 at a = 7/2, about 593 at a = 17/4 in V026, sharpened at a = 17/4 to C_A < 38.436,
  V099) and D_a. The axis traces are bounded and the
  localized jet coupling is compact. So the remainder is absorbed on thin strips, with an explicit O(R) rate.
- The global version, lemma (E), with its parts (E1) the weight in y and the coupling of dyadic y-blocks, (E2) the
  origin corner with the traces near y = 0, (E3) input outside the strip with output inside it, and (E4) the Garding
  part for the angular factor times e^{mu}, is proved for the modal background in the form (E0), (E-J), (E-G) of
  section 2.3 (THEOREMS, V049 to V053): dyadic radial annuli, the strip estimate on comparable scales, Hilbert-Schmidt
  bounds for separated scales, and a Garding argument that does not use any weighted singular-integral theorem for the
  non-A_2 angular weight. Its constants are finite and not computed.

4.3 Reducing the rank-one term.
- Answer: yes, exactly. The rank-one term becomes a bordered operator L_red = L_ren + c[.] zeta with an explicit
  profile zeta in the target and a denominator d >= 3 c_l > 0 (Prop B, V034), the scalar normalization is eliminated
  with a unique ell(h) (V038), and L_red is Fredholm of index 0 on Z (Theorem C'). What is not obtained is a
  quantitative bound |c[h]| <= C_c ||L h||, which needs the inverse (OPEN, end of this section).
- c is bounded on a domain that carries the normalization (Prop C2, THEOREM, V034). With Z_cap := {h : chi_1 h in Z_0,
  h in L^2(e^{mu~})} and the norm of the sum,
     |c[h]| <= |J|/8 + C_v ||v||_G + C_R ||u||_R + C_> ||h||_{mu~} <= C_cap ||h||_{Z_cap},
  C_> < 0.273629, C_cap < 0.312093 at a = 7/2, b = 6/5 and C_cap < 0.359253 at a = 17/4, b = 0. The origin part cannot
  be dropped (V032).
- Rank-one bordering by the log direction (Prop B, CONDITIONAL THEOREM, V034, on an operator domain X embedded in
  Z_cap with L_ren : X -> Y; on the jet spaces the bordering is used in the form of Theorem C' (ii), V047). Write (1 - chi_0) X.grad rho~ = k Phi_hat + g_far with Phi_hat = chi_inf r^k Theta_0 (not in
  the target) and g_far in the target. For h = h_0 + kappa KP, L h lies in the target if and only if
  kappa (3 c_l + k c[KP]) = -k c[h_0]. Then
     L h = L_red h_0 := L_ren h_0 + c[h_0] zeta,   zeta = (c_l g_far - k y_KP)/d,   d := 3 c_l + k c[KP],
  where L_ren carries the strain only near 0, combined with the coupling as in 4.2.
- Denominator (THEOREM, V034): 37.63077494715565 < s_3/pi < 37.63077494715567 for the far angular moment
  s_3 = int sin(3 theta) Theta_0, so c[KP] >= 0 and d >= 3 c_l > 0 for every smooth cutoff 0 <= chi_inf <= 1 supported
  in r >= 1.
- What d != 0 gives and does not give (THEOREM, V038): it permits the exact elimination of the tail coordinate. It
  does not invert L_red. If L_ren is invertible, L_red is invertible if and only if 1 + c[L_ren^{-1} zeta] != 0. If
  L_ren is Fredholm of index 0, so is L_red.
- Scalar normalization (THEOREM, V038). In the parametric form, nu(ell, h) := 3 ell - 1 - c[rho_bar_ell] - c[h] has
  d nu/d ell >= 3, so for every finite c[h] there is exactly one ell(h) > 1 with nu = 0, and
  |ell(h) - c_l| <= |c[h]|/3. At h = 0, d nu/d ell = k d. For independent (ell, h) the residual contains the forbidden
  origin jet (1 + J(h)) nu x^2 y; the augmented map (F - (1 + J(h)) nu H_0, nu), H_0 = chi_0 X.grad rho~/3, removes it,
  and its derivative at the base point is exactly the bordered system above (V038 for J = 0; V042 for a free cubic
  coordinate J, where subtracting only nu H_0 leaves J nu x^2 y outside the target).
- J free and the final normalization (THEOREM for the index and scaling statements, V087). The restriction of L_red to
  {J = 0} is Fredholm of index -1; if L_red is invertible on Z, its range on {J = 0} is the hyperplane
  J[L_red^{-1} f] = 0, so an onto theorem does not carry over to J = 0 unchanged (REFUTED, V087). The problem is
  therefore solved with J free. A classical solution rho_* with cubic coefficient 1 + j > 0 gives the normalized profile
  rho_norm(X) = lambda rho_*(X/lambda), lambda = (1 + j)^{1/2}, with cubic coefficient 1; the speed c_l and the far
  exponent are unchanged and the far angular profile is multiplied by (1 + j)^{(1 - q)/2}. This final scaling is
  distinct from the fixed-tail correction chart.
- Dual criterion (THEOREM, V035): |c[h]| <= C ||L h|| holds if and only if c = L^* phi with ||phi|| <= C (Hahn-Banach).
  It does not need an inverse of L. If ||c - L^* phi|| <= delta and ||h|| <= A' ||L h|| + B' |c[h]| with delta B' < 1,
  then |c[h]| <= (||phi|| + delta A')/(1 - delta B') ||L h||. Actual adjoint solvability is OPEN.
- Status of |c[h]| <= C_c ||L h||_Y for the full operator: OPEN. The obstruction is quantitative: (E) holds in the form
  (E0), (E-J), (E-G) of section 2.3 with finite but uncomputed constants, and no quantitative inverse of L_red is
  available (injectivity is OPEN, section 5.4). It is
  not the adjoint weight (explicit, kappa_0 > 0), not the inflow fluxes (good sign) and not the elimination of the tail
  coordinate (exact).

## 5. Avenue IV: finite-basis certification

5.1 Is the finite basis conforming? Yes, in its repaired form (V027).
- The columns are degree-7 splines in t = log r, C^6 at the interior knots, joined to the inner and outer power laws
  by exact rational solves of the 3-jet (so C^3 at the two junctions, enough for the C^1 conformity of V014), times
  cos(2m theta), with the factor x^2 y. The coordinates J (x^2 y times an exact C^6 cutoff),
  KP and TAU (the truncated tail product) are explicit columns.
- Conformity criterion (THEOREM, V014): at an interface the image jumps by (V.n)[d_n h], so H^1-type conformity needs
  exact cancellation of the derivative jumps; rounded joins do not suffice. The earlier archived basis failed this
  (jumps 1e-22 to 1e-14), and its tail column omitted the nonzero mode-260 coefficient (V015). The repaired basis is
  confirmed in its test-space interpretation (V027).
- Exact objects: the trial in exact rational spline form, Green boundary data for 261 modes at all 1559 cell
  boundaries in 320-bit ball arithmetic, exact operator images of the columns with the origin cancellation built in and
  the compensated far column phi + dk KP, dk = -k c[phi]/d (V020 confirms the formula). A 42-mode identity test
  reproduces the expected image to 1.7e-46 (NUMERICAL); it checks the machinery and bounds nothing.

5.2 Is the finite inverse certified? For a finite section only; no continuum inverse is certified.
- The exact section S0 (4 angular modes, 169 conforming columns plus TAU, KP compensation, 12 output modes, 69 test
  splines per mode, 256-bit balls) has the lower bound sigma_min >= 4.3337e-07, and sigma_min >= 2.0685e-02
  without the TAU column, both certified conditional on the exported entry balls enclosing the exact pairings. The value with TAU was reproduced independently from the exported matrices, conditional on
  the exported entry enclosures (V066; exact dyadic s = 4093149700530291/2^73 = 4.33379e-07); the value without TAU was
  reproduced independently by a direct 384-bit test-Gram inversion under the same condition (V200). With TAU the weakest direction is the TAU column, whose compensated image lies mostly beyond the last
  test knot; without it, the far power columns of modes 0 and 1. A first attempt failed because the Gram midpoints were
  rounded to binary64 before the high-precision Cholesky (V054); with exact midpoints the whitened 170 x 170 Gram is
  positive definite, ||T^T G T - I||_inf < 1.754e-27 (V056). The certificate method (sigma_min(Q_M L P_N) >= s if
  K - s^2 G is positive definite, K = B^T (Z + Z^T - Z^T G_Y Z) B for any real Z) is confirmed (V020). By Prop IV.O
  (V039) these numbers cannot bound a continuum inverse in the S0 norms. The strain values of its two tail columns and
  the bordering denominator are independently enclosed: c[KP_shifted] = 0.07037233698866423364..., c[TAU] =
  0.06854755426283814823..., 3/k + k c[KP_shifted] = 16.73870985167530795... (THEOREM, V043, 34-digit balls). The
  column uses the shifted logarithm log r - t_+; the unshifted log r column has strain 0.56103503149402952743...
- A second exact section, of L_fix in the realization of Theorem R (L^2(e^{mu~}) on both sides; 169 conforming columns,
  angular modes m = 0 to 3, 69 test splines times 12 output modes, exact integration at 256 bits), has the lower
  bound sigma_min >= 0.510914, certified conditional on the exported entry balls enclosing the exact pairings (both Grams whitened exactly, positivity residual 4.4e-12; reproduced from the
  exported entries by independent code at 384 bits, conditional on those entries enclosing the exact pairings, V081). Its
  weakest directions are the inner power columns of modes 0 and 1, supported at r < 0.0077. This is the first finite
  section in a realization where Lemma IV.1 below applies. It is still a finite statement: without the split (S) and the
  adjoint certificates it bounds no continuum inverse.
- The earlier production sections have smallest singular values 0.41312, 0.52004, ... (H^1 rows) and 0.16978, ...
  (L^2 rows), reproduced to the printed digits (NUMERICAL). They are not continuum bounds (V014, V015).
- Sections in the strong spaces (the jet realization of L_red, and S_1 on L^2(w_a)) are computed in floating
  point; they are not bounds. Their angular output map (truncation of the raw sine coefficients, jet extraction, then a
  Euclidean least-squares division by cos^4(theta)) is not a contraction in Y: the input cos^4(theta) sin(37 theta),
  whose true jet is 0, is amplified by more than 5037.58 at sine cutoff 19 (5037.63 with the false jet it creates);
  REFUTED as a contraction, by exact rational algebra (V111). Truncation also breaks the x^2 vanishing on the axis. A
  certificate must use a conforming orthogonal target projection or a proved norm of this test map. The exact repair
  of the compensated far column (the Arb quotient kept through the cancellation) is confirmed (V111). In the strong
  target the residual needs all cosine modes up to the resolution of the trial: at log r = 8, raw truncation at sine
  index 120 retains less than 1e-4 of its remainder energy (NUMERICAL; the truncated values are not monotone in the
  cutoff, because truncation creates false jets), so a residual computed from a few dozen modes misses most of eta.
- Floating core section of the remainder block S_1 = T_R + C_R on R = L^2(w_a), both sides in the R norm, with the
  complete angular output (all 531 sine modes, numerically evaluated jet split and cos^4 quotient; the non-contraction of V111 does
  not arise because no mode is dropped) (NUMERICAL, double precision with the generalized eigenproblem solved at 50
  digits). The 42 columns are x^2 y b_i(t)(cos 2 theta + 1) for the radial functions b_i of the S0 basis, i.e. only the
  first angular remainder mode. Smallest generalized singular values 4.155, 6.08, 23.3, 51.6, 53.1, ... (from the
  per-worker final blocks, each cell counted once; the verifier confirmed this cell coverage for the completed run,
  V180). An earlier assembly also added the retained cumulative checkpoints
  and so counted most cells twice (accounting defect found by the verifier: the default assembler is REFUTED as a once-per-cell sum, V180, with exact
  two-cell counterexamples showing that duplicate or omitted cells change singular values); it gave 4.136, 6.09, 23.3, ..., and its
  values on the subspace c[h] = 0 (4.44, 6.09, 23.3, ...) were withdrawn; recomputed from the correct sum they are 4.456,
  6.084, 23.31, 51.70 (NUMERICAL). The Gram of the columns has condition number 1.5e13; for the value 4.155 the
  computed direction has an approximate Rayleigh value in [4.137, 4.174], an interval that covers accumulation
  rounding only (it is not a rigorous bound in either direction); this direction is concentrated in the coordinates of the outer power columns, which live just beyond the
  outer junction (r about 3400); 6.08 and 23.3 are not resolved by the rounding estimate; after removing the seven
  nearly dependent directions the values are 10.1, 13.6, 51.0, ..., and the 33 pure spline columns give 50.3, 51.6,
  .... A TRUE complete-image Rayleigh quotient would bound the infimum over its subspace, and over the full domain,
  from above; floating values with uncontrolled image errors, and singular values of sections with a projected
  output, do not. None of this proves anything about injectivity; the floating values are
  consistent with the margin 5/2 of INJ-Q and show no small value in the bulk. Certifying it would need rigorous
  R-norm Grams of the 531-mode images on 1569 cells, estimated at about 18 hours on four cores for this basis, beyond
  this run. The input quotients by cos^4(theta) of these runs were formed with a padded pseudoinverse instead of the
  exact integer templates Q_m(theta) = 2 sum_(j=0)^(m-1) (-1)^(m-1-j) (2m - 2j - 1) sin((2j + 1) theta) of the m-th mode
  (V189); this changes the domain Gram by about 1e-7
  relative (9.31e-8 for the first mode, V187), and the division error of the image quotients is not covered by any
  error model, so "resolved" above means resolved with respect to accumulation rounding only (V187: REFUTED as a total
  error bound, CONFIRMED for the floating observations). The exact angular bandwidth of the images is 264 to 266 raw odd
  sine slots, J + M (V193). For a far-junction section, five shifted outer columns h_q = r^3 p(theta)(cos 2 theta + 1)
  b_q(log r), b_q an outer exponential minus its interpolant on the four leading outer exponents beyond t_+ + 1, are
  exact C^3 low inputs; their span meets the high input space in dimension 3 and the high graph domain in dimension 2
  (THEOREM, V260, V263); the exact low input Gram has a closed form. The complete exact input Gram of all 38 input
  columns of this section (inner-extended splines, extra inner powers, pure splines, shifted outer columns) is
  enclosed from the original data, with disjoint-support blocks 33 and 5 and positive definiteness proved (VERIFIED,
  V267). The whole 38-column span meets the high input space in dimension 32 and the high graph domain in dimension
  29, cut out by the fourth and fifth (for the graph also the sixth) derivative jumps at the three joins t_-, t_+ and
  t_+ + 1 (THEOREM, V269, verifier proof with exact ranks, independent audit recorded as V275). This certifies inputs
  and subspaces only; the output values of the section are floating.
  The completed far-junction section itself (NUMERICAL, floating outputs; complete projected core images of S_1 after
  the exact jet split, not full A_0 images, in the low input and output norms; all 1569 cells counted once; the input
  form is certified against the exact Gram with relative error below 0.000431058, V277, which does not control the
  output uncertainty) has the smallest generalized singular values 4.7481, 15.142, 34.29, 44.21, ..., and about 4.7481
  on the hyperplane defined by the stored binary strain row (V267 bounds the error of that row; the exact strain-zero
  subspaces of the 38-column span and of its 32- and 29-dimensional high subspaces have dimensions 37, 31 and 28, and
  in the low input metric, within each of these spaces, the exact kernel of the stored binary row lies within relative
  distance 6.244e-16 of the exact kernel of the strain functional: THEOREM, V282, verifier proof, independent audit
  recorded as V291; this is an input statement only, it does not cover the floating basis used for the value, and no
  exact constrained output value follows). The weakest direction is concentrated in the shifted outer power columns
  (-0.79 out9 + 0.56 out5 + 0.25 out8, normalized Gram eigenvalue 9.0e-12); its Rayleigh quotient lies in [3.74, 5.59]
  under the accumulation-only rounding model, which is not a certified enclosure, and 15.1 and 34.3 are not resolved.
  Without the five outer columns the 33 remaining columns give 50.32, 51.58, 53.16 (the 26 pure splines 50.3201).
  Restricted to the exact 32-dimensional high input subspace the value is 5.8703, and to the exact 29-dimensional high
  graph subspace 7.4692 (both floating, from the same S_1 core images in the low norms, not high-norm values). Moving
  the outer attachment from t_+ to t_+ + 1 changes the far value from about 4.16 to about 4.75. These observations
  show only that the small floating values are concentrated in the outer-column coordinates, persist after its
  attachment is moved, and give way to larger values once that subspace is removed; they do not show that the small
  value is spurious (an
  exact two-column example with arbitrarily bad Gram conditioning has a genuine small minimum that disappears after
  deleting a column, V279). Its accuracy and exact operator meaning are unresolved. No output value is certified,
  none is a high-norm value, and no inverse or complement bound follows.
- The same section with the first two angular remainder modes (84 columns: the 42 radial functions times
  p (cos 2 theta + 1) and p (cos 4 theta - 1), p = cos^2(theta) sin(theta); complete images; never resumed; each cell
  counted once) (NUMERICAL): smallest values 2.344, 2.921, 3.501, 3.829, 3.910, 4.700, ...; all except 3.501 are below
  the rounding estimate of their computed directions, which are near-null combinations of the outer power columns at
  the far junction. The first-mode sub-block reproduces the values above; the second mode alone gives 3.668, 4.341, 12.44.
  The well-conditioned subspace of the 52 pure spline columns (no inner or outer power law; rounding estimates about
  1e-9 relative) gives 3.456, 4.248, 5.460, 6.942, against 50.3 for the first mode alone and 25.5 for the second mode
  alone. Its weakest vector mixes the two angular modes with comparable weights on the coarse splines centred at
  r = 18 to 360, the region where the transport margins have their minima. So the coupling of angular modes in the bulk
  lowers the section value from 50 to 3.46; whether the exact value keeps falling as modes are added bears on the size of the
  finite-rank part that a certificate of Lemma INJ-S needs, which finite floating observations do not decide. The section with three angular modes on the pure spline
  columns (78 columns: b_i, i = 4 to 29, times the first three angular remainder modes; S_1 on L^2(w_a), complete
  images) was computed with an assembler that checks equality of the covered and expected cell sets
  (the earlier check of cardinality only is REFUTED as a generic guarantee, V188, and CONFIRMED for the runs above;
  the repaired assembler is CONFIRMED, V196, while the inputs of the runs above keep their padding error). Its
  accounting is verified (V252): all 1569 cells are counted exactly once, and the 1531 retained checkpoint cells are
  duplicate prefixes and are excluded. Its smallest floating values are 2.7655, 3.2685, 4.3913 (2.7662 on c[h] = 0,
  with the stored floating strain row); the sub-block of the first two modes reproduces 3.4557, 4.2477, 5.4604, and
  the single modes give 50.32, 25.47 and 12.11 (NUMERICAL, V252). Against the angular cutoff the smallest value is
  50.32, 3.456 and 2.766 for one, two and three modes: it decreases as modes are added, has not converged, and is not
  bounded below by these runs. The 60 high-graph-conforming columns (7 <= i <= 26) give 2.8648 in the LOW norms; this
  is not a high-norm value. Only the input side is rigorous: for every nonzero coefficient vector the stored input
  quadratic form differs from the exact one (the input Gram of V202, recomputed independently at 640 bits) by a
  relative error below 2.688e-6 (V252). The output pairings, the image division and the quadrature are not certified
  (only the accumulation rounding model of V187 applies), so these values are NUMERICAL, give no exact operator bound
  and are not a certificate. The input
  norms of the pure-spline columns are now certified independently (V202): the stored input Gram of the 52-column
  section satisfies |v^T (G_float - G_exact) v| < 2.37e-6 v^T G_exact v, and the stored strain coefficients have
  relative error below 2.71e-16; output pairings and image-side division errors are still uncertified. All 78 columns
  are low-conforming, but only part of the section lies in the high realization of Theorem E (THEOREM, V210, with an
  exact check of the original endpoint jets and of all 884 interior C^6 joins): the coarse splines b_i, extended by zero
  outside the spline interval, are C^6 at the interior knots; at the left end the first nonzero jump has order i for
  i = 4 to 7 (exactly C^(i-1) there), at the right end order 33 - i for i = 26 to 29 (exactly C^(32-i) there), and
  every other column vanishes near the respective endpoint and is smooth there (C^3 for i = 4 and i = 29). The section meets the high input space in the 66 columns with 6 <= i <= 27 and
  the maximal high graph domain of the normalized operator in the 60 columns with 7 <= i <= 26. For i = 6 and 27 the
  transport image has a jump of the fifth radial derivative, multiplied by the vertical radial speed (at least 5.5752),
  which no bounded coupling term can cancel. A statement involving the high image of this section must use the 60-column subspace.
  A TRUE complete-image Rayleigh quotient bounds the infimum over its subspace from above only; floating values with
  uncontrolled image errors do not, and none of these values proves anything about injectivity.

5.3 Off-basis residual bounds.
- Method (DERIVED, structure confirmed in V020 and V027): with R such that E = R^{-T} G R^{-1} - I has ||E||_inf < 1,
  ||(I - Q_M) L P_N|| <= |t^|_2/(1 - ||E||_inf)^{1/2}, t^_i = sum_j |(R^{-1})_{ji}| t_j, t_j a bound for
  ||(I - Q_M) L u_j||. A naive bound with absolute coordinates is invalid (2 x 2 counterexample). Every image has finite
  angular bandwidth (the trial has 260 angular modes), so nothing is truncated (DERIVED).
- The interval code has been audited three times. Defects found and repaired: wrong density lookups (V027), a
  zero-straddling product before a square root, nearest-float conversions, discarded small positive endpoints and a
  missing velocity term (V033); the repairs are confirmed (V037), and the two remaining arithmetic obligations of V037
  were repaired in the code afterwards, and that repair has not been re-audited (OPEN).
- No off-basis bound has been computed at this version.

5.4 Is the complement controlled? No.
- In the realization used for S0 it cannot be (Prop IV.O, THEOREM, V039). There the input space X has the variable
  h/(x^2 y) with angular H^1 norm, the target Y has f/r^3, and L acts on the maximal domain
  D_max = {h in X : L h in Y distributionally}, L : D_max -> Y. (i) L maps D_max, through a weak axis trace, into the
  closed subspace {f(0, y) = 0} of infinite codimension, so it is not onto. (ii) Zero-strain angular packets h_eps = x^2 y beta(t) phi((pi/2 - theta)/eps) in D_max, with
  int e^{2t} beta = 0, satisfy ||L h_eps||/||h_eps|| <= C eps^2. So no uniform inverse bound holds in these norms, and a
  certified sigma_min of a finite section in this realization cannot be uniform in the angular dimension. Enlarging the
  basis cannot repair this.
- A complement estimate in a consistent realization reduces to checkable items (Lemma IV.1, CONDITIONAL THEOREM,
  V040). Let L : D(L) -> H be closed and densely defined, with
  (G) m ||g|| <= ||L g|| + ||K g||, (S) K = K_S + sum_{i<=n} <., phi_i> e_i with ||K_S|| <= delta and e_i orthonormal,
  (A) psi_i in D(L^*) with ||L^* psi_i - phi_i|| <= eps_i.
  If delta + eps < m (eps, Psi the l^2 norms of eps_i and ||psi_i||), then ||g|| <= (1 + Psi)/(m - delta - eps) ||L g||,
  and if L is Fredholm of index 0 this is a bound for the inverse. For transport perturbations A = L + W.grad in the
  weight with angular factor |cos theta|^{-2a}, the adjoint defects grow by at most
  p_i = dW ||r grad psi_i|| + (2|c|/3 + (M + 4a) dW) ||psi_i||, dW = ||DW||_infinity, M = sup|mu'|. One set of psi_i
  then serves the whole correction ball, provided each psi_i lies in the common adjoint domain with r grad psi_i square
  integrable, the perturbed operators have the same compact error K and a positive margin m_W,
  delta + eps + (sum p_i^2)^{1/2} < m_W, and the index is 0 (V040, V048). In the jet-plus-remainder realization the
  adjoint has extra jet rows, which this plain-L^2 formula does not cover; Lemma INJ-S below removes them from the
  two-dimensional part.
- In L^2(e^{mu~}) on both sides (the realization of Theorem R), (G) is Theorem R (unconditional, V077). The
  finite-rank split (S) with an explicit delta is OPEN; it is an analytic high-frequency statement, and a generic
  commutator gain does not give it. The adjoint defects (A) are a finite computation of the kind the exact pipeline
  does. This realization covers L_fix only (V032). For the normalized operator the realization must be the jet space of
  2.3 with its jet rows.
- Size of the split (THEOREMS on a regular periodic cylinder, V082, and NUMERICAL estimates; the finite-basis discussion in the accompanying artifacts, section 6.1). On a
  periodic cylinder window, with S_1(a) the first Fourier moment of a coefficient a, a multiplier commutator restricted to
  frequencies |p| >= Lambda has norm at most max(2 M_1, 4 M_0) S_1(a)/Lambda, and the principal coupling
  sum B_ij S_i S_j (B the polar form of the coupling matrix of grad rho~, S_j = p_j/|p|) satisfies
  Re <C_pr v, v> <= int b_+ |v|^2 + [eta/2 + (4/Lambda)(sum S_1(B_ij) + 2 S_1(b_eta))] ||v||^2 on that range, with
  b_eta = (sqrt(|g|^2 + eta^2) - g_2)/2. Both statements are THEOREMS on a regular periodic cylinder (V082), and the
  difference between the exact Mellin multipliers of the homogeneous velocity and their principal part is at most
  max(|sigma + 1|, 1)/(Lambda - |sigma + 2|) there (V083; sigma = 13/4 near 0 and -3/8 at infinity for the radial
  isometry of w_a). The singular angular conjugation, cutoffs, axis terms and jet rows of the actual operator are not
  covered (OPEN). Grid values: sum S_1(B_ij) + 2 S_1(b_eta) is about 1.65e3, the coupling is
  significant (|grad rho~| > 0.3) only for log r in [-0.66, 9.06], and the largest derivative of B in (log r, theta) is
  about 140, at log r = 4. With a quarter of the margin 0.966 (the second code before its refinements) assigned to the frequency error, the global
  commutator bound needs Lambda about 2.7e4 and a rank of order 1e9; a global cutoff at the pointwise derivative scale
  needs about 4.8e5 modes (5.0e4 at margin 3); a cutoff adapted locally to the derivative of B needs about 1.2e4 (1.2e3 at
  margin 3), and about 150 with the local grid margin of w_a. These are scale estimates, not bounds. They show that a
  certificate must use phase-space localized cutoffs and local margins, that the margin had to be refined (it
  now is, see below), and that compressing the positive part of the compact energy defect may reduce
  the number of adjoint witnesses further. A finite-dimensional homotopy gives no shortcut (DERIVED): index 0 along a path
  does not exclude a kernel at its endpoint, so every step of a continuation needs its own inverse certificate.
  The best certified margins are m_a >= 3 (THEOREM, V259, superseding 2.9270, V197; the earlier bound m_a >= 5/2, V086,
  remains true) and
  m_* >= 5/2 (THEOREM, V086; m_* is the radial margin of Theorem R; a second code gives 2.500023 and 2.471224, and after a
  second refinement 2.871539 and 2.482724, computed once). At the margin 5/2 the inverse-square scaling brings the
  locally adapted first-order count to about 1.7e3.
- Second-order principal energy (THEOREM on a regular periodic cylinder, V096). For a real symmetric matrix field B and
  the self-adjoint direction multipliers S_i, sym(sum M_(B_ij) S_i S_j) = sum S_i B_ij S_j + (1/2) sum [S_i, [S_j, B_ij]],
  and the comparison of sum S_i b S_i with b is also a double commutator up to the zero mode. Hence for u = Q_Lambda u
     Re <C_pr u, u> <= int b_+ |u|^2 + [eta/2 + (S2mat(B) + S2(b_eta))/(2 Lambda^2)] ||u||^2,
  with S2mat(B) = sum_q |q|^2 ||B^(q)||_op <= sum_ij S2(B_ij) and S2(b) = sum_q |q|^2 |b^(q)|; four derivatives bound
  S2 (S2(a) <= C_L D4(a), C_L^2 <= 1 + pi/2 + 3L/4, D4 an explicit L^2 norm of the derivatives of orders 2 to 4). A
  budget E > eta/2 is met by Lambda^2 >= [S2mat(B) + S2(b_eta)]/[2(E - eta/2)]. This replaces the first-order error
  (4/Lambda)(sum S_1(B_ij) + 2 S_1(b_eta)) of V082. For the full regular Mellin family U_sigma with real bounded
  coefficients g_1, g_2 (THEOREM on a regular cylinder, V098) the symmetric part of U_sigma - U_pr is of order -2 by an
  exact midpoint cancellation of the shifted adjoints, and the error becomes
     eta/2 + (S2mat(B) + S2(b_eta))/(2 Lambda^2) + G_0 E_0 + 6 K G_1/(Lambda - 2 - |sigma + 2|)^2,
  K = max(|sigma + 1|, 1), G_0 = ||g_1||_inf + ||g_2||_inf, G_1 = S_1(g_1) + S_1(g_2),
  E_0 = (sigma + 1)^2/((Lambda - 1)^2 - (sigma + 1)^2) + 1/((Lambda - 1)^2 - 1);
  this is a quadratic-form statement, and U_sigma - U_pr itself is still of order -1. On a compact regular patch with a
  bounded positive weight f = e^q the paired conjugation difference has kernel
  (K(X - Y)/2)[b(X)(f(X)/f(Y) - 1) + b(Y)(f(Y)/f(X) - 1)], bounded at the diagonal, and is Hilbert-Schmidt with
  squared norm at most 2 pi A (C_0^2 R^2 + C_far^2/R^2) (THEOREM, V097; A the area of the support, C_0 and C_far the
  explicit constants of the record). The singular angular weight of w_a, localization, tails and jets are not included.
- Explicit axis-strip constant (THEOREM with stated coefficient bounds, V095, V099). The near-strip error of the defect
  construction is at most A_ax s with A_ax = sqrt(W_max)[39 M_20 + (25 s_0/2) M_21 + (39 s_0^2/6) M_40 +
  (25 s_0^3/24) M_41] (the universal strip constants at a = 17/4 are C_A < 38.436, C_B < 24.534, D_A < 38.762,
  D_B < 24.724, V099, replacing 593 and 612 of V095; trace constants below 0.134331, 0.230829, 0.718533), where M_20, M_21 are the axis suprema of rho_xx and rho_xxy and M_40, M_41 those of rho_xxxx and
  rho_xxxxy on the compact Taylor rectangle (W_max/W_min for a localized radial input). These four suprema are not yet
  enclosed; the radial-lift and separated-input pieces are additional. The conditional algebra of the finite-rank
  construction (projection blocks, Hilbert-Schmidt errors, triangular norm conversion, exact rank-one bordering, cutoff
  commutators) is CONFIRMED (V094); a pointwise reflected-kernel bound must keep the reflected distances. No actual
  defect norm, rank, adjoint witness or inverse is certified.
- INJ-Q (CONDITIONAL THEOREM, V102). Let S := sym(C_R) - M_(b_+), P an orthogonal finite-rank projection on R and
  Q = I - P with <S Q u, Q u> <= eps ||Q u||^2. Put S_F = P S + S P - P S P (all three blocks that involve P). For
  columns e_i, phi_i in R and psi_i in D(S_1^*) with synthesis maps E, Phi, Psi and D = Phi - S_1^* Psi, assume
  ||S_F - E Phi^*|| <= delta_F, E^*E <= e^2, Psi^*Psi <= p^2, D^*D <= d^2 (actual Hilbert pairings). If
  a = 5/2 - eps - delta_F > e d, then S_1 is bijective, ||S_1^{-1}||_{R -> R} <= k_1 = (1 + e p)/(a - e d), and
  ||S_1^{-1}||_{R -> D_R} <= (k_1^2 + (1 + M_C k_1)^2)^{1/2} when ||C_R|| <= M_C. A sufficient form of the
  high-frequency hypothesis: localizations J_j with sum ||J_j u||^2 <= c_loc^2 ||u||^2, regular-patch bounds E_j (the
  Mellin formula above) above the cutoffs Lambda_j, S <= sum J_j^* H_j J_j + E_small + sum K_l with ||E_small|| <=
  eps_small and finite-rank F_l within delta_l of K_l, ran P containing the low modes and the columns of the F_l; then
  eps = c_loc^2 max E_j + eps_small + sum delta_l. Every localization, tail, lift and norm-comparison error must
  appear in E_small or the K_l; none is removed by compactness. The jet system and the scalar border still need
  their own certificate (Lemma INJ-S). Exact localization (THEOREM, V101): for real cutoffs with sum chi_j^2 = 1 the
  real transport energy localizes with no error, and C - sum chi_j C chi_j = (1/2) sum [chi_j, [chi_j, C]], whose
  kernel on a compact regular weight extension is Hilbert-Schmidt with explicit near and far constants (the far
  constant doubles for signed cutoffs). Trace and lift constants (THEOREM for the analytic bounds, V105): closed
  majorants N_j(y) of ||h -> d_y^j U_2[h](0, y)||_{R^*}, j = 0, ..., 3, with I_a = 2 B(19/4, 1/2); the axis-row
  derivative gamma_t = (alpha'' - alpha) T/y + (alpha - alpha') T' - 2 alpha y T''; and the radial-versus-vertical
  lift bound (2 W_max (1/Y_0 - 1/Y_1))^{1/2} M_gamma d^{1/4} on |x| < d, Y_0 <= |y| <= Y_1, with M_gamma the supremum
  of |alpha'' - alpha| N_0/y + |alpha - alpha'| N_1 + 2 |alpha| y N_2 on the window. The actual alpha bounds are not
  yet enclosed.
- Revised scale (NUMERICAL, float64 grid data; the rank-estimate computations in the accompanying
  artifacts). On the window log r in [-3, 11] with eta = 0.1, sum_ij S2(B_ij) is about 2.15e4 and
  S2(b_eta) about 3.46e4 (2.1e4 at eta = 1, so the regularization is not the main cost). The second-order rule gives
  Lambda about 172 at E = 1 and 139 at E = 3/2, about 5.2e4 and 3.4e4 low modes per parity class, against about 4.7e6
  for the first-order rule with the same budget. Radial localization in unit cells gives 2.8e4 and 1.8e4, without the
  localization errors. A local proxy with |D^2 B| in place of the Wiener moments gives about 130. The moments are
  dominated by an angular layer at the vertical axis for log r in [3, 8] (d_theta^2 B about 250 to 350 near
  theta = pi/2), which lies in the singular strip of w_a where the strip estimate replaces Fourier counting; removing
  that strip by a smooth angular cutoff of half-width 0.3 lowers the global count only to 1.3e4 to 1.9e4, because the
  cutoff adds moments. For the chosen proposed method, with the rigorous tools now available, a certified split is
  estimated to need of order 1e4 low modes (a planning estimate from uncertified moments and incomplete localization,
  not a proved necessary dimension), which is
  beyond the computing limits of this work; with that method a smaller certificate needs phase-space localized error bounds close to the
  local proxies.
- Sufficient criteria (CONDITIONAL THEOREMS, V082). Finite adjoint witnesses give the inverse bound
  (1 + Psi)/(m - delta - eps) when m - delta - eps > 0 (Lemma IV.1). For a bounded Fredholm operator A of index 0 on a
  Hilbert space, an orthogonal finite-rank projection P and Q = I - P, with Q A Q bijective on ran Q and
  ||(Q A Q)^{-1}|| <= 1/d, ||P A Q|| <= b, ||Q A P|| <= c and ||P A P p|| >= a ||p||, the condition s = a - b c/d > 0 gives
  invertibility and ||A^{-1}|| <= (p_0^2 + ((1 + c p_0)/d)^2)^{1/2} with p_0 = (1 + (b/d)^2)^{1/2}/s. Without the
  finite-rank orthogonal P and index 0 these bounds give only injectivity and a lower bound, not an inverse (exact
  counterexample: the unilateral shift direct sum the identity on R, whose range has codimension one, V250).
- Lemma INJ-S (reduction to the remainder block; THEOREM, V092, with the norm correction stated at the end of this item;
  the nonlinear-closure discussion in the accompanying artifacts, section 3.5(b)). In
  the jet-plus-remainder spaces Z = E B (+) D_R, Y = E Gamma (+) R (section 2.3, R = L^2(w_a)) write
  L_red(E beta + h_R) = E[(A + Gamma_B) beta + Gamma_R h_R + c[h] zeta_J] + [X beta + S_1 h_R + c[h] zeta_R], with A the
  axis row, Gamma_B, Gamma_R the compact jet couplings, X bounded, S_1 = T_R + C_R : D_R -> R Fredholm of index 0 and
  c[h] = c_B beta + c_R h_R. If S_1 is injective (hence bijective, s_1 := ||S_1^{-1}||_{R -> D_R}), then with s := c[h]
  the equation L_red h = E phi_J + phi_R is equivalent to h_R = S_1^{-1}(phi_R - X beta - s zeta_R) together with
     A' beta + s (zeta_J - Gamma_R S_1^{-1} zeta_R) = phi_J - Gamma_R S_1^{-1} phi_R,
     (c_B - c_R S_1^{-1} X) beta - s (1 + c_R S_1^{-1} zeta_R) = -c_R S_1^{-1} phi_R,
  where A' := A + Gamma_B - Gamma_R S_1^{-1} X : B -> Gamma. This system M_J on B x R is (A (+) (-1)) plus a compact
  operator, hence Fredholm of index 0; ker L_red is in bijection with ker M_J; and if A' is invertible (equivalently,
  L_ren is), M_J is invertible if and only if 1 + c[L_ren^{-1} zeta] != 0 (the criterion of V038 in reduced form).
  So the two-dimensional certificate is needed only for S_1 on the plain space R, where Lemma IV.1 applies with the
  Garding inequality of Theorem C' (iii) at margin 5/2 - eps, without jet rows and without the rank-one term; the jets,
  the cubic coordinate and the normalization form a system for functions of one variable plus one scalar, whose
  compact part needs explicit tail bounds (OPEN). Norms (V092): with Hilbert product norms the bound for the system reads
  (||beta||_B^2 + |s|^2)^{1/2} <= ||M_J^{-1}|| (1 + (||Gamma_R|| + c_R) s_1) ||f||_Y (with the sum ||beta||_B + |s| a
  factor sqrt(2) is needed), and a certified L^2 inverse bound k_1 of S_1 gives the graph-norm bound
  s_1 <= (k_1^2 + (1 + ||C_R|| k_1)^2)^{1/2}. Gamma_B is compact, not of rank one in general. The strain functional on
  R has norm ||c_R|| = ((58/99)(6618/725) B(3/2, 19/4)/pi^2)^{1/2} < 0.20757, with the same bound on D_R in the graph
  norm (THEOREM, V093). The actual split, witnesses and scalar remain OPEN.

5.5 Does the combination give a genuine inverse theorem? No. A genuine inverse in this avenue needs, in addition to the
pending finite certificates, the split constant delta and certified adjoint solutions psi_i for the remainder
operator S_1 on R (Lemma INJ-S removes the jet rows from this part), explicit bounds for the compact jet couplings
and the scalar of the reduced system M_J, and explicit constants for (E0), (E-J) and (E-G).

## 6. Final closure

6.1 Is a complete nonlinear existence theorem established? No. A conditional one is (Theorem E, 6.2 item 6,
CONDITIONAL THEOREM, V178); its two hypotheses, base low injectivity and one smallness inequality, are OPEN.

6.2 The precise missing estimates.
The nonlocal coupling estimates that were the first missing step at earlier versions are proved: (E-J), (E0) and (E-G)
of Theorem C' hold for the exact modal background, with finite but uncomputed constants (V049 to V053). The remaining
items, in order:
1. (Done at this version.) The two pointwise hypotheses of Theorem C' for the explicit background, (A), the axis rate
   d = V_2(0, y)/y between two positive constants with the endpoint orders, and (M), the margin
   m_a = ess inf (kappa_{w_a} - b_+) > 0 on R^2 \ {0}, are certified by an independent original-data computation
   (V077: d >= 5.5752, m_a >= 0.53072; the radial margin of Theorem R is >= 1.78605; both margins are at least 5/2
   by its refinement, V086). A second code gives
   d in [5.575203, 21.301451] with the endpoint constants of 2.3 and m_a >= 0.965918 (V072, conditional on its exported cell enclosures; refined by that code to
   2.871539 and then 2.9270, the latter confirmed by an independent refinement, V197, and later m_a >= 3, V259; its first script had coverage and underflow defects, V054, repaired with a confirmed method, V061, V068). So Theorem C'
   holds for the modal background: L_red : Z -> Y is Fredholm of index 0 (THEOREM, V047 with V049 to V053, V077, V086).
2. Injectivity of L_red on Z, with a quantitative inverse bound. Index 0 reduces invertibility to injectivity, and no
   qualitative argument for injectivity has been established here. The selected quantitative route is Lemma IV.1 (V040), applied by Lemma INJ-S (5.4,
   THEOREM, V092) to the remainder block S_1 on R without jet rows, followed by the one-variable system M_J: the
   compact operator K_eps of Theorem C' (iii) must be split into a part of explicit small norm delta and an explicit
   finite-rank part, and approximate adjoint solutions psi_i with certified defects must be computed. The compact
   operators of V049 to V052 are produced by limiting arguments (output tails, strip widths, approximation of a compact
   operator by finite rank), so each step needs explicit constants. The S0 finite sections are in a
   realization where no continuum bound is possible (Prop IV.O, V039); the L_fix sections and the full-image floating
   sections of S_1 use different, consistent low realizations that this mechanism does not cover, but they give no
   certificate, and their complement remains OPEN. The principal energy error is of second order in the
   cutoff (V096, V098) and the axis-strip constant is explicit (V095, V099); the certificate is assembled as one
   conditional statement with every input listed (INJ-Q, V102; localization V101; trace and lift constants V105); but
   the Fourier moments of the background are large:
   grid estimates of the required number of low modes (section 5.4, NUMERICAL) are of order 1e4 to 5e4 with these
   rigorous tools and about 1e2 to 2e3 for local proxies that are not bounds.
3. The high-norm inverse in a space with Lipschitz velocity, compatible with the low-norm inverse. By Prop F4 and
   Lemma H1 (section 2.4) its order must vary: 2 + eps near the closed x-axis segment from the origin to the source
   (ordinary derivatives; in the corner, angular derivatives of h/r^3), conormal order N near the y-axis, scaled order
   N at infinity, nondecreasing along the flow (Theorem H, DERIVED outline). Hypothesis (Z) of Lemma H1 is certified
   (V080), so the flow portrait is a theorem for the actual background. Every order must be below 13/2 on a knot circle
   of the spline background and upstream of it (V069); the order 25/4 is admissible (V073) and the residual lies in the
   target (V076). In the cylinder norm the order near the segment must be below 3/2 + delta A/(A+D) (V079), so
   eps < 0.14547 and the origin exponent delta must exceed (A+D)(1/2 + eps)/A; delta = 9/5 with order 41/20 is
   admissible. The estimate must be stated in inverse-regularity form (V074), and it needs global weighted high-order
   control of the coupling with its full order-zero principal part kept (a one-order gain is false, V085; the
   normalization profile is in the high target, V084), the regularization step from the low domain (the spectral-parameter
   continuation of Lemma H-spec is CONFIRMED as an abstract theorem and REFUTED in its direct form on the free-cubic
   spaces, V106; its restatement for the remainder block with the jet row split off, a CONDITIONAL THEOREM (V108),
   reduces the step to a
   large-parameter resolvent bound for the remainder transport, a high a priori estimate with a compact error and
   three jet-row conditions; on the smooth variable-order space X_s the jet-row conditions and the mapping bound (H1)
   are THEOREMS (V126), the resolvent bound (H2) is a THEOREM under the monotone-order hypothesis (V129), an order
   function with that property exists (THEOREM, V130, V132), and the a priori estimate (H3) is a THEOREM (V151), by a
   reduction to one high-frequency estimate (Hs_eps), section 2.4 (g), verified end inverses V131, V133, V135, V137,
   the reduction to a compact core V139, V140, the reduction H3-red CONFIRMED conditional on (Hs_eps) (V141), and the
   symbol inequality (THEOREM, V144) from which (Hs_eps) follows given four finite-regularity calculus inputs, all
   THEOREMS (V146 to V150); hence S_1, L_ren and L_red are Fredholm of index 0 on X_s, THEOREM, V152), and tame
   dependence on the perturbation (section 2.4; the robust order sign V154 and the C^(1,alpha) logarithmic positivity
   V155 are THEOREMS, the full Kato-Ponce route is REFUTED, V153; the uniform high theory for small frozen-coupling
   transport perturbations, with generation, index 0 and a uniform inverse under base injectivity, is a THEOREM,
   V156 to V161 and V163, with the sign correction of V162; its bordered, low and moving-tail versions are THEOREMS, V166, V168 to V170, with the inverses
   conditional on injectivity of the base low operator).
4. The bilinear and Lipschitz-velocity bounds in that space. They are THEOREMS, with finite uncomputed constants, for
   the cone-local space of V065 (order s > 2 near the x-axis segment and the origin, factored H^7 near the vertical
   axis), which has the shape required in item 3, and for its fractional version with factored order 25/4 (V073).
   Explicit constants are missing.
5. A residual that is small in the closure norm, with a certified enclosure. Membership, axis jet included, is
   THEOREM in Y (V042) and in the fractional target of order 25/4 (V076). The size in Y: 6049.11 < ||F(rho~)||_Y < 8601.42
   (THEOREM, V164: interval integration of the original data over all angular modes, 1860 radial cells on
   -40 <= log r <= 20 and both analytic tails; it supersedes the lower bound 933.47 of V110); about 7.2e3 by quadrature of all-mode directed point densities (NUMERICAL; 81 radii on
   0 <= log r <= 20 at spacing 1/4, the exact far rate 4k - 5/4 beyond; doubling the spacing changes the energy by 1
   percent). The quadrature arithmetic is reproduced independently (V122, CONFIRMED as arithmetic only;
   coarser nodes give 7202, trapezoids 7253; no interpolation or tail bound). The far tail is certified: the full Y
   energy beyond log r = 20 lies in (203443.34, 203445.56), beyond 25 in (14192.84666678, 14192.84666680) and beyond 30
   in (990.0012675088110412, 990.0012675088110415), axis and remainder parts and all angular modes included (THEOREM,
   V125; V123 gives cruder bounds beyond 40 and 45). The quadrature put about 2.04e5 (0.39 percent) beyond 20, in
   agreement to 0.5 percent. The quadrature itself does not certify the energy on 0 <= log r <= 20; the enclosure of V164 does. Energy shares: 0.07 percent for
   log r < 4, 4.7 percent on [4, 8.135], 69.8 percent on [8.135, 12], 25 percent on [12, 20], 0.4 percent beyond; the
   axis energy is about 123.4 of 5.24e7 (axis norm about 11.1). The far rate is exact: the residual has a nonzero term
   of physical degree 2k - 1, so its strong remainder energy density decays at the rate 4k - 5/4 (THEOREM, V120). Relative to the profile the residual is small: the
   ratio of strong densities is 5e-3 at log r = 1, about 4e-4 at 3 to 4, 1.2e-5 at 8, 8e-6 at 10, then decreasing like
   r^(k-1); the pointwise ratio sup |F| / sup |rho~| is below 3e-7 at log r = 0, 4, 8, 10, 12, 20. The strong energy lies in
   an angular layer at the vertical axis: 94 to 99.7 percent within 0.01 rad of it for log r in [4, 10], 55 percent at
   log r = 15 and 20, against 40 percent for the profile; the cosine spectrum of the residual quotient is nearly flat up
   to mode 160, while that of the profile decays; in an unweighted angular H^(25/4) proxy the residual exceeds the
   profile at log r = 2 and 4 (ratios 165 and 14; 0.11 at 8). All of this is NUMERICAL, computed once from the original
   data in directed arithmetic. Consequences (DERIVED):
   (a) Global constants. The margin perturbation bound (V075) keeps the certified margin 5/2 positive only while
   (51/4) ||D W[h]||_infinity < 5/2, so K_H eta <= r and C_V r <= r_V with r_V < 10/51 require C_V K_H < 10/(51 eta):
   below 10/(51 x 6049.11) < 3.25e-5 by V164. If K_H were of the order of the inverse of the
   transport energy rates (between about 1/50 and 2/5) and C_V an embedding constant of order one for functions at r = 1, the
   closure inequalities with global constants would fail by orders of magnitude for this trial in this weight. This is a
   heuristic concern only: neither guess is a proved lower bound for the actual constants in compatible high and low
   norms, so failure of (S) is OPEN, and the valid necessary tests (V185, V194, V199) are violated by no certified
   direction.
   (b) The weight is a design parameter. Write a for the angular exponent and lower the far radial exponent by 2 Delta
   (an extra factor r^(-2 Delta) in w_a for r >= 1). The remainder part of eta is then about 7.2e3 (a = 17/4, Delta = 0),
   1.8e3 (a = 4), 4.0e2 (a = 3.6), 4.4e2 (a = 17/4, Delta = 0.3), 32 (a = 3.8, Delta = 0.3), 13 (a = 3.6, Delta = 0.3)
   (NUMERICAL). The weighted margin changes exactly by (a - 17/4)[tan(theta) V.grad(theta) - q 1_{r<1}] - Delta q 1_{r>=1},
   q = V.X/r^2, so its far limit becomes 1 + 3 c_l/8 - Delta c_l, which vanishes at Delta = k + 3/8, the value at which
   r^k Theta_0 enters the space; the order across the x-axis segment is limited by (1 + c_l + a A)/D, which is 2.02 at
   a = 3.6 and 2.12 at a = 3.8; the coefficient 51/4 of (a) becomes 3a. The variation formula and its far limit are
   CONFIRMED (V121). In this tied family the inner scalar weight is e^((8 - 2a)t), and for a <= 4 the finite-J scalar
   inverse is lost: a constant inner forcing (a < 4) or 1/(1 + |t|) (a = 4) lies in the target and forces an infinite
   cubic trace (V121). The finite-J realization needs a > 4 and Delta < k + 3/8. Because r < 1 carries 0.07 percent of
   the residual energy, the useful variant keeps the inner radial exponent at 17/4 and lowers only the angular exponent
   and the far exponent; the far values of eta above are unchanged in that variant. It needs its own mapping proofs
   (the jet-row results use the angular trace gain a - 1/2, V116) and a recomputed margin (both now THEOREMS, below). In this variant the
   margin changes by (a - 17/4) tan(theta) V.grad(theta) - Delta q 1_{r>=1}. Box lower bounds from the per-box data of
   the refined margin map, in floating arithmetic, are 1.38, 0.73, 0.07 at a = 4 and Delta = 0.2, 0.3, 0.4; 1.13, 0.48,
   -0.18 at a = 3.8; 0.88, 0.22, -0.45 at a = 3.6. The minimum sits at r about 180 to 210 next to the vertical axis
   (85.8 degrees), where the bound on tan(theta) V.grad(theta) has not been refined, so the true minima are probably
   higher (FLOATING). A positive but small margin enlarges the inverse transport constant, so the gain in eta is partly
   paid back in K_H. The variant is now proved at Delta = 0.3 for every a in [18/5, 4]: the margin is at least 1.10534
   (at least 1.2501 at a = 4 by an independent refinement, V191; THEOREM, V171 with V172), so the floating box bounds above were pessimistic; the low mapping, the
   closed scalar normalization, the Hilbert-Schmidt axis row, the Garding estimate and index 0 hold, with remainder
   strain norms < 0.239392 at a = 18/5 and < 0.230190 at a = 4 (THEOREM, V172); the uniform third axis derivative bound
   of the old weight fails for a <= 4 (REFUTED, V173), and the proof replaces it by a source-scale split; the residual
   is certified, ||F(rho~)||_(Y_a) < 485.632 for every a in [18/5, 4] (THEOREM, V174). The analogue of (a) in that
   family, with margin 1.10534 and coefficient 3a, would read C_V K_H < 1.10534/(3a eta), about 2.1e-4 at a = 3.6 with
   485.632 in place of eta; this is indicative only, since the margin perturbation bound of (a) is not proved for the
   new weight and eta is a high norm.
   (c) Localized constants. For h concentrated at log r = T the constants C_V and C_B, measured against the local strong
   norm, scale like e^{-11T/8}, and the transport inverse carries information inward with decaying weight; a closure
   argument with location-dependent constants fits a residual concentrated at large r better than one with global
   constants (proposal, OPEN).
   (d) A trial with angular resolution adapted to the vertical axis would reduce eta directly, and the high target
   needs it (OPEN).
6. The moving-tail formulation is settled (V062): with the scalar normalization eliminated, the exact equation is
   f_0 + A_h h = 0 with ||(A_h1 - A_h0) g||_Y <= C ||h1 - h0||_low ||g||_high, and existence follows from uniform right
   inverses into the high space (bound K_H), a low estimate (K_L) and K_H eta <= r, K_L C K_H eta < 1. These are items
   2, 3 and 5 for the family A_v, with the ell-dependence of the compact part of the Garding estimate bounded.
   For the transport part of A_v with the background frozen at rho_ell0 (the frozen-coupling remainder family S_g),
   the uniform high theory is proved (V156 to V161 and V163, with the sign correction of V162: uniform estimate, generation, index 0, and a uniform inverse if S_0
   is injective). The bordered and moving-background versions are now proved. The perturbed scalar axis row
   A_g beta = A beta + (tau_g + c/3) beta' + (c - tau_g - 2 tau_g') beta, with the axis trace tau_g = c[g] chi_0 + e_g and
   e_g, chi_- e_g/a in H^(31/4), is a small bounded perturbation on the fixed scalar domain and an isomorphism on a small
   ball (THEOREM, V166); the full block with fixed coupling is Fredholm of index 0 on B_H (+) D_g, with the fixed
   compact error map (Gamma_C h, c[h], K_R u), and has a uniform high inverse if the base operator is injective
   (THEOREM, V168); the same holds in the low realization (THEOREM, V169); and for the exact moving-tail family
   rho_ell = rho_0 + chi_inf(r) (r^(1/ell) - r^k) Theta(theta), ell in a fixed interval with max(k, 1/ell) < q_* < 1/4,
   the tail velocity satisfies all the coefficient estimates although the tail density is not in the coefficient space,
   the changes of coupling and of the rank-one vector are small bounded maps in both realizations, A_h = T_total +
   C_ren,0 + c[.] zeta_0 + D_h with ||D_h|| <= C ||h||, the family is Fredholm of index 0, and injectivity of the base
   low operator gives uniform low and high inverses (THEOREM, V170). Radii and constants are qualitative.
   Assembly (Lemma Emb THEOREM, V177; Theorem E CONDITIONAL THEOREM, V178). Lemma Emb: Gamma_H embeds in G and B_H in B (radial weights
   e^(31t/10) at the origin end and e^(-t/4) at infinity), X_s embeds in R and in every perturbed maximal low domain
   (on the vertical sector u_X = cos^2(theta) u~ by evenness and the zero trace, so the angular weight becomes
   |cos(theta)|^(-1/2) sin^2(theta)), and H_full = B_H (+) X_s embeds in the high space of the bilinear bound, of orders
   25/4 and 41/20, through h = x^2 y [a (chi' u_X)] + b [(1 - chi') v]. Hence the difference bound of the iteration theorem
   holds with H = H_full. Theorem E (conditional existence): assume (I) the base low operator A_0 is injective and (S)
   K_H eta_0 <= r <= r_* and K_L C K_H eta_0 < 1, with eta_0 = ||f_0||_(Y_full), K_H and K_L the uniform inverse bounds of
   V170 and C the difference constant. Then there are ell and h in H_full with ||h|| <= K_H eta_0 and
   F_ell(rho_ell + h) = 0; h is the low-norm limit of h_(j+1) = -A_(h_j)^(-1) f_0. The profile rho = rho_ell + h is
   C^(1,alpha) on compact subsets of the punctured plane for every alpha < 1/20 and solves the equation pointwise there,
   has cubic jet (1 + J) x^2 y at the origin and far field r^(1/ell) Theta(theta) + O(r^(-1/2)) (every high correction is
   O(r^(-1/2)) and 2k - 1 < -1/2). If |J| < 1 (sufficient: ||J||_(H*) K_H eta_0 < 1), the rescaling lambda rho(X/lambda),
   lambda = (1 + J)^(1/2), has leading term exactly x^2 y with the same ell and speed and tail amplitude lambda^(1 - 1/ell).
   The correction h is unique in the closed r ball of the fixed moving-tail chart if K_L C r < 1 (uniqueness before the
   rescaling only). The same implication holds with the low spaces of the decoupled family, for each fixed angular
   exponent a in [18/5, 4] (uniform perturbed inverse framework, THEOREM, V175; low/high product and difference bound,
   THEOREM, V176). Status: (I) is OPEN; (S) cannot be checked, since r_*, K_H, K_L and C come from compactness arguments
   and the certified residual sizes (V164, V174) are low norms, not eta_0. The high norm is finite (the residual is
   locally of order 25/4) and is enclosed in an explicitly fixed equivalent norm, 3.866e10 < eta_* < 6.321e129
   (THEOREMS, V192, V182). The upper end comes from global coefficient and derivative majorants and is not an estimate
   of its size. The lower end uses only the axis summand of the norm, so it holds for every choice of the angular cutoff
   and of the Littlewood-Paley partition with this weight and order; it is driven by knot-scale structure (6.5 item 9).
   In this norm (S) requires K_L C K_H < 1/eta_* < 2.6e-11. That is not a refutation: K_H, K_L and C are not computed,
   and they change with the equivalent norm, as does eta_*; the equivalence does not change the theorem. Two necessary
   consequences of (I) and (S) need no inverse constant: eta_0 |c[d]| <= N4 ||A_0 d|| with 0 < N4 < 9.06 for every
   nonzero high-domain direction (CONDITIONAL THEOREM, V185), and its residual-subtracted form
   ||R_d|| > 1956082280 |c[d]| for every such direction with c[d] != 0 (CONDITIONAL THEOREM, V194); neither has been tested with a certified bound, and a heuristic estimate suggests that both fail for the
   archived trial (6.5 item 10). Theorem E is therefore a conditional existence theorem and not an
   unconditional existence proof for the actual trial; it states exactly what remains.

6.3 What is proved (THEOREMS; record numbers in brackets).
- Conventions and normalization: canonical velocity and normalized expansion [V002]; normalization and strain of the
  modal background [V005]; X3 defect [V018]; origin regularity C^{4,1} [V036]; exact quadratic expansion [V038].
- Origin: Theorem O with sharp constant 1/kappa_0, continuous J and continuous strain extension [V022]; frozen local
  strain adjoint K_A < 0.032162163072022018 [V016]; strip remainder and trace estimates [V026]; Prop M and
  Corollary C1 [V034].
- Source: a source unique in its certified interval, with mu != 1 [V017]; frozen nonlocal source inverse on H^s, s < 2373/680 [V011];
  sharpness of the frozen threshold s_fast (about 3.5785) at the actual source, with the Riesz coupling retained [V064];
  auxiliary source inverse and strain norm [V021]; source neighbourhood margin [V024]; Hoelder source inverse at mu = 1
  and at the actual rate [V013, V029].
- Global: Theorem R for L_fix in radial weights [V023, V031], with (H_m) certified for the actual background,
  m_* >= 1.78605 [V077], refined to m_* >= 5/2 [V086]; c not closable on that graph [V032]; necessary conditions N1 to N5 [V025].
- Normalization: Prop C2 (c bounded on Z_cap) and Prop B (bordering, conditional on the operator domain), with
  d >= 3 c_l > 0 [V034]; dual criterion [V035]; unique scalar normalization ell(h), |ell(h) - c_l| <= |c[h]|/3, and the
  augmented map [V038].
- Hoelder: H0 and S(a) to S(d), sharp thresholds [V028]; Lemmas N and N' [V030]; corrected strain factor [V201];
  S(e) [V203 to V207, cross-audits V212, V216]; sharp normalized rate [V219, cross-audit V225]; J not closable in the
  E_2 graph, relative density [V208, V216, V217]; Lemma N'' [V211, V218]; source inverses on C^alpha_b intersected
  with L^2 [V213 to V215, cross-audits V221, V223]; the common target Y with the residual in it, bounded cut-off local
  inverses, bounded complete coupling and closed full operator A_0 [V222, V224, V228, cross-audits V231, V233]; the
  noncompact error of the specified cutoff parametrix, which does not exclude cancellation in sums of patches [V227]; the actual-variable origin factorization error O(delta^2) [V226, V231];
  the far obstructions on Y, non-surjectivity for every bounded linear coupling with vanishing tails [V234] and an
  infinite algebraic cokernel of T, L_ren and A_0 [V232, cross-audit V237]; on E_2 itself and on every Y with gamma > 4k,
  the bounded complete coupling, the closed maximal realization and the infinite algebraic cokernel of T, L_ren and A_0,
  without an extension of the weighted velocity theorem [V241, V247]; the sharp far tails of the coupling on E_2 and
  Y: R^(2k-1) log R for C_0 on E_2 and R^max(2k-1, 2k-gamma/2) log R on Y [V276, V286], R^(k-1) log R for C_ren on both
  and for C_0 on the strain-zero inputs [V278 with V281, V287], not claimed on Z_sc, Z_2 or Z_cof; the sharpness of the vertical power 2 and
  the exclusion of alpha = 1 [V229, V230, cross-audit V238]; the actual exterior inverse in scaled far Hoelder norms
  with the complete coupling [V236, cross-audit V242]; on Z_sc the noncompactness of the specified single origin patch
  under its flow-box hypothesis, which does not exclude cancellation in sums of patches (a norm-small right error
  would give onto only) [V239, V246]; the completion of the smooth graph with the cubic label as G_sm (+) R with a
  scalar invisible to A_0, G_sm being only the smooth graph closure [V240, V246]; the infinite algebraic cokernel of
  T, L_ren and A_0 on Z_sc [V243, V249]; on Z_2 the mapping, the complete small tail, the residual membership, the
  closed full maximal domain and the actual auxiliary exterior inverse, with the global inverse OPEN [V245, V254].
  On Z_2, T is not onto for alpha > 1/2 and A_0 and L_ren are not onto for alpha > 2/3, by the certified simple turning
  height of the axis rate [V256, V262]; by the joint C^alpha bound for U_1[x^2 g]/x, A_0 and L_ren are not onto
  Z_2 for every alpha > 1/2 either [V257, V265]. On the joint-cofactor target Z_cof the mapping, the residual
  membership, the closed maximal domains and the actual auxiliary exterior inverse for every alpha < 1, with the global
  inverse OPEN [V261, V268]; on Z_cof the semilinear map N(h) = (U[h] + (c[h]/3) X).grad h is not continuous at 0 in
  the graph norms of T, L_ren and A_0, even with c = J = 0 [V264, V271]; T alone is not onto Z_2 or Z_cof for
  alpha > 1/A_s, so for every alpha >= 1/10, by cusps at the source, with infinite algebraic cokernel [V266, V272].
- Finite basis: conformity criterion and complement requirement [V014]; Prop IV.O [V039]; Lemma IV.1 with the
  transport extension, as a conditional statement [V040]; the confirmed parts of the code audits [V020, V027, V033, V037];
  the S0 section without TAU, a matrix lower bound conditional on the exported entries [V200]; the exact input Gram
  and strain of the pure-spline sections, recomputed from the original data, which certify inputs only and no output
  pairing or complement inverse [V202]; the cell accounting of the 78-column three-mode section and its input-form
  inequality, relative error below 2.688e-6, with its floating values NUMERICAL only [V252]; the conformity classes of the pure spline
  section [V210, V220]; the exact C^3 shifted outer columns of a far-junction section, their high intersections of
  dimensions 3 and 2 and their exact input Gram [V260, V263]; the complete exact input Gram of the 38-column
  far-junction section, input side only [V267]; the high intersections of that whole section, dimension 32 in the
  high input space and 29 in the high graph domain, statements about subspaces only [V269, V275]; the exact strain-zero
  subspaces of the section span and of these two intersections, of dimensions 37, 31 and 28, and the comparison of the exact kernel of the stored
  binary strain row with them (relative distance at most 6.244e-16 in the low input metric), input side only, with no
  statement about a floating nullspace basis or an output value [V282, V291].
- Abstract two-norm theorem [V038]: let X_H be reflexive and embedded in X_L, A_0 : X_H -> Y_L bounded,
  B : X_L x X_H -> Y_L bilinear with ||B(d, h)|| <= C_B ||d||_{X_L} ||h||_{X_H}, and for each v in the r-ball of X_H a
  compatible solution operator R_v of A_v = A_0 + B(v, .) with ||R_v||_{Y_L -> X_L} <= K_L, ||R_v||_{Y_H -> X_H} <= K_H
  and ||g||_{X_L} <= K_L ||A_v g||_{Y_L}. If K_H eta <= r and K_L C_B K_H eta < 1, with eta = ||f||_{Y_H}, then
  A_0 h + B(h, h) = -f has a solution with ||h||_{X_H} <= K_H eta, unique in the ball if K_L C_B r < 1.
- Axis row and target: the scalar y-axis row is an isomorphism B -> Gamma with explicit constants, conditional on a
  positive axis rate with endpoint bounds [V041]; the pure transport T = V.grad - 1 is an isomorphism from
  Z = E B (+) D(T_R) onto E Gamma (+) L^2_P(w_a) with the explicit triangular inverse, conditional on (A), the angular
  coefficient bounds (L) and kappa_* > 0 [V046]; L_fix does not map Z into Y and c[.] H_0 is not a bounded perturbation
  into Y [V044, counterexample]; the separated outside-to-inside strip coupling is compact in w_a [V045]; the modal residual and the parametric residual lie in the jet target
  Y = E G (+) L^2_P(w_a), and the augmented map with a free cubic coordinate subtracts (1 + J) nu H_0 [V042].
- Coupled Fredholm theory on the jet spaces: Theorem C' with Lemmas C'1 to C'4 as a conditional theorem on (A), (L),
  (M), (E0), (E-J), (E-G), with the sharp strain constant c_R = 0.2075698661066814348... and zeta in Y [V047]; the jet
  row is Hilbert-Schmidt under (A) [V049]; the jet-input coupling is Hilbert-Schmidt [V050]; the remainder-input
  coupling is bounded on R, a near-diagonal part with vanishing radial tails plus a Hilbert-Schmidt part [V051]; the
  Garding inequality (E-G) [V052]; the exact modal density satisfies the annular C^5 and endpoint hypotheses of these
  proofs, and (L) holds with finite constants [V053, V047]. (A) and (M) hold for the actual background: d >= 5.5752,
  m_a >= 0.53072 (independent original-data computation) [V077], refined to m_a >= 5/2 and m_* >= 5/2 [V086], and m_a >= 2.9270 and then m_a >= 3 by further independent refinements [V197, V259]. Hence, for the exact modal background, L_red : Z -> Y
  is Fredholm of index 0, and it is invertible if and only if it is injective.
- Transport regularity of the modal field (V globally Lipschitz C^1, V_1/x and V_2/y bounded, the endpoint bounds of
  d, finite lift constants) and the exact energy limits kappa_0 = (19/2) c_l - 13/4 = 49.7159... at 0 and
  kappa_inf = 1 + 3 c_l/8 = 3.0908... at infinity [V055]. With the coupling records above, Theorem C' needs only (A)
  and (M).
- High spaces: an explicit Hilbert space with cylinder-H^7 cofactor that embeds in Z with classical J, the low/high
  bilinear bound with the full velocity and exact axis subtraction, and the Lipschitz-velocity bound [V057]; the
  refinement with origin exponent delta in (1/4, 2) and a compact H^s component, s > 2, away from the y-axis [V060].
  Constants finite, not computed. Not ranges of the frozen corner inverse (Prop F4, V067). The same bounds for the
  cone-local space with a cylinder H^s bulk, s > 2, on |cos theta| >= eps (covering the x-axis segment and the origin)
  and factored H^7 near the vertical axis [V065]; the same with any factored order above 6, so 25/4 below the knot
  ceiling [V073]. Global membership of the normalized residual in the target of order 25/4 [V076]. No bounded forward
  isomorphism between high spaces of equal order, and no common graph domain for small Lipschitz perturbations
  (counterexamples) [V074]. The margin perturbation: for the fixed background kappa_w - b_+ decreases by at most
  |c[h]|/3 + (51/4)||D W[h]||_infinity for a = 17/4, plus ||grad h||_infinity when the coupling background moves [V075].
- Frozen corner: Prop F4, the exact singular solution -C x^4 sgn(y)|y|^{2 - 1/D}, both Sobolev endpoints and the
  exclusion of the old high spaces for the frozen inverse [V067]; the cylinder corner threshold 3/2 + delta A/(A+D) with
  an explicit low-domain counterexample at delta = 3/2, order 21/10 [V079]; low-to-high regularization of the selected
  frozen inverses in the x-axis cylinder chart (constant 1/kappa_s = 1.02816 at delta = 9/5, order 41/20) [V103] and in
  the vertical remainder cofactor chart (every finite order) [V104].
- Moving-tail formulation: the fixed-forcing quasilinear operator A_h with the exact scalar elimination, its mapping
  into Y, the identity F = f_0 + A_h h, the low/high difference bound, the general free-J augmented residual, and the
  conditional iteration theorem, assuming the positive axis rate [V062].
- Flow: under (Z), every interior orbit runs from the source to infinity and the x-axis segment from the origin to the
  source flows into the origin; on every compact set without zeros there is a smooth compactly supported escape
  function, without (Z); (Z) does not follow from the divergence and endpoint data [V063]. Lemma Z: (Z) follows from
  a bound near the origin, the source data and positive box lower bounds of |V|/r elsewhere [V071]; the source is the
  only zero of V in the rectangle Q = [p_- - 1/2, p_+ + 1/2] x [-1/2, 1/2], with |V(X)| >= 0.1801|X - P| there [V070];
  (Z) holds for the actual background, the zeros being 0 and the two source points, with |V|/r >= 3/12500 outside Q in
  the closed first quadrant away from 0 [V080]; so the flow statement above holds without condition. The exclusions of
  a second refinement lie in Q, and its leaf count was misreported [V078].
- Regularity of the background: the exact spline has a nonzero seventh-derivative jump at an interior knot, so the
  residual and its axis-jet remainder are locally H^s there exactly for s < 13/2 [V069].
- Numerical methods: exact-midpoint whitening of the S0 Gram [V056]; a float interval union REFUTED by an exact
  counterexample [V058]; stable Green moment formulas near resonance [V059]; the repaired exact-dyadic union with
  resonance merging [V061]; the S0 matrix bound with TAU, conditional on the exported entries [V066]; the revised range
  method and adaptive angular refinement, with the archived merge of production parts REFUTED [V068]; complete coverage,
  retention and directed aggregation of the production margin and axis-rate runs, conditional on their exported cell
  enclosures [V072]; the independent original-data certificates of the axis rate and the two margins [V077] and of the
  zero set [V080]; the L_fix finite section in L^2(e^{mu~}), conditional on the exported entries [V081].
- Inverse criteria: the finite adjoint-witness and Schur criteria with explicit inverse bounds, and the commutator and
  principal Garding estimates on a regular periodic cylinder [V082]; the homogeneous velocity formulas and the Mellin
  comparison bound on a regular cylinder [V083].
- High-order data and normalization: the bordering profile lies in the high base target for 0 < delta < 2,
  gamma > 2k - 1, sigma < 13/2 [V084]; the restriction of the normalized linearization to {J = 0} has index -1, and a
  free-J solution is normalized by the scaling of 4.3 [V087]; the abstract spectral-parameter continuation
  (Lemma H-spec as an abstract theorem, with lambda_* = omega + 1 + 2M||C||) [V106] and in the remainder-block form
  with the unshifted jet row (Corollary H-spec, conditional on the high-space hypotheses) [V108]; the index change of
  the shifted zero-jet scalar row at D/4 [V109]; the strong residual lower bound ||F(rho~)||_Y > 933.47 [V110], superseded by the
  enclosure 6049.11 < ||F(rho~)||_Y < 8601.42 [V164], with six
  directed point densities [V107]; the high axis row: dilation commutation, separated sectors and compactness of the
  remainder axis row R_(max(N-2,0),s) -> H_g^N for N <= 6 [V112], the Hilbert-Schmidt free-jet row on B_N [V113], and
  the critical angular Hardy inequality with the embedding of the base order 25/4 remainder into R_(4,s) [V114]; the
  mismatch of the integer scalar target H^6 with the remainder order 25/4 (counterexample) [V115]; compactness of the
  full axis row into the localized order 25/4 space by the fractional trace gain [V116]; the weighted scalar graph
  Gamma_H = a H^(25/4) with endpoint weights e^(9t/5) and e^(-7t/2) and its endpoint counterexample [V117]; J1, J2 and J3
  for the explicit candidate R_H = R_base + Q [V118]; the failure of (H1) for that sharp sum, even with one transport
  graph derivative (counterexample) [V119]; the nonzero far residual term of degree 2k - 1 and the exact energy rate
  4k - 5/4 [V120]; the exact margin variation in the weight family and the loss of the finite-J scalar inverse when the
  tied exponent a drops to 4 or below (counterexamples) [V121]; the arithmetic of the numerical residual quadrature
  [V122, numerical only]; directed far-tail enclosures of the residual energy beyond log r = 40, 45, 60 [V123] and,
  with all regular powers retained, beyond 20, 25, 30 [V125]; the one-sided smoothness of the coupling of a conormal
  power [V124]; (H1) and J1 to J3 on the smooth variable-order space X_s [V126]; the insufficiency of five
  coefficient derivatives for the high transport inverse (counterexample) [V127]; the failure of all-covector energy
  coercivity at the vertical-axis end (counterexample) [V128]; (H2) on X_s under the monotone-order hypothesis [V129];
  existence of a smooth monotone order and a smooth escape function for the actual field [V130], and the direct
  repeller-block construction [V132]; the exact origin normal family for each fixed frequency [V131] and uniformly in
  the frequency [V133]; the sharp joint source margin 4.52536 at order 41/20 (the value 14.8 REFUTED) [V134]; stable
  selected principal end inverses at the vertical [V135], horizontal and far [V137] ends; the stable residual Green-ODE
  integration algorithm [V136, algorithm only]; the unboundedness of a small actual first-order coefficient error on
  the normal graph (counterexample; the perturbation justification REFUTED) [V138]; the actual inner end estimate with
  a finite annular error [V139]; vanishing coupling tails in the X_s operator norm and the reduction of the full
  equation to a compact core [V140]; Proposition H3-red, conditional on (Hs_eps) [V141]; the axis row from the
  lower-order space X_(s-eps), 0 <= eps <= 1/4 [V142]; compact commutators [C_R, M_phi] on X_s, compact escape
  conjugation and the common local principal symbol of the coupling in the bulk and cofactor variables [V143]; the
  global symbol inequality Lemma Hs-sym, after one decimal correction [V144]; finite-regularity positive
  quantization of the energy symbols and of the logarithmic term, with an H^(-1/32) form remainder [V145]; the order
  reduction with a lower-norm error and the sector support correction [V146]; the variable-order coupling modulo
  compact and arbitrarily small errors [V147]; C_R bounded on X_(s-eps) and the penalty bound with an arbitrarily
  small high error [V148]; the finite Taylor transport commutator for W^(7,inf) coefficients [V149]; its
  maximal-domain passage [V150]; Proposition Hs and (H3) on X_s for the actual operator [V151]; the high Fredholm
  theorem: S - lambda (lambda >= 0), L_ren and L_red are Fredholm of index 0 on the high graph domains, and low
  injectivity gives the high inverse [V152]; the robust monotonicity W.grad s >= kappa_s |grad s| of the fixed order
  and the explicit matrix-margin loss under perturbation [V154]; the logarithmic positivity for C^(1,alpha)
  coefficients [V155]; the global weighted bounds for the perturbation velocity [V156]; the square-summed coefficient
  commutator [V157]; the dyadic energy [V158]; the uniform compact-error estimate for small frozen-coupling transport
  perturbations on their maximal domains [V159]; generation, index 0 and the uniform inverse under base injectivity
  [V160]; the single-operator tame commutator and product bounds [V161]; the single-operator route to the uniform
  estimate, with a corrected sign [V163]; the finite-band division of the actual angular velocity by sin(theta) and
  cos(theta) without loss of radial regularity [V165]; the weighted axis velocity trace with a gain of 3/2 derivatives
  and the perturbed scalar axis isomorphism [V166]; the full fixed-coupling scalar and remainder block under small high
  transport perturbations, Fredholm of index 0 with a fixed compact error map and a uniform high inverse under base
  injectivity [V168], and its low version [V169]; the exact moving-tail family with uniform low and high compact
  estimates, index 0 and both uniform inverses under base low injectivity [V170].
- Decoupled weight family (inner radial exponent unchanged, far radial weight lowered by 0.6, angular exponent a in
  [18/5, 4]): transport margin at least 1.10534 [V171, V172] (at least 1.2501 at a = 4 [V191]); low mapping, closed scalar
  normalization, Hilbert-Schmidt axis row, Garding estimate and index 0, remainder strain norms < 0.239392 (a = 18/5)
  and < 0.230190 (a = 4) [V172]; residual ||F(rho~)||_(Y_a) < 485.632 for every a in the interval [V174] and > 3.270 for every a in the interval
  (eight disjoint windows, all residual sine modes, exact beta-Chebyshev angular moments, 384 and 640 bit replays)
  [V179]; for each fixed
  a, the fixed-coupling and exact moving-tail operators on the new low spaces are Fredholm of index 0 on their maximal
  graph domains with fixed compact estimates, and base low injectivity gives consistent uniform low and high inverses
  [V175]; the low/high product ||W[d].grad f||_(Y_a) <= C_a ||d||_(X_a) ||f||_(H_full) and the low-Lipschitz operator
  difference of the moving-tail family, without a third axis derivative [V176].
- Conditional existence: Lemma Emb, the continuous embeddings Y_full in Y, H_full in X0 and in every perturbed low
  maximal graph domain, and H_full in the high product space, for both the original and the decoupled low spaces
  [V177]; Theorem E, existence of an exact self-similar profile with leading term (1 + J) x^2 y under base low
  injectivity and the smallness inequality (S), with uniqueness in the fixed correction ball, C^(1,alpha) regularity off
  the origin for alpha < 1/20, far field r^(1/ell) Theta + O(r^(-1/2)), and unit normalization when |J| < 1
  (CONDITIONAL THEOREM) [V178].
- High residual norm: with a_* = e^(9t/5)(1 + e^t)^(-53/10), an explicit angular cutoff and an explicit
  Littlewood-Paley normalization of the variable-order norm (an equivalent norm on the high target of Theorem E), the
  exact normalized trial satisfies ||F/(r^3 p a_*)||_(H^(25/4)) < 1.195e93 and eta_* < 6.321e129, from the exact
  angular division, the radial L^1 norm and the total variation of the sixth derivative across all 1559 joins, exact
  origin and far cancellations and integral Green bounds, at 512 and 768 bits with a separate 1024-bit scalar audit
  [V182]. These are upper bounds only and do not test (S).
- High residual norm, lower bound: in the same norm eta_* > 38666592266 [V192], from the difference inequality
  |f^(5)(t) - f^(5)(u)|^2 <= [8/(3 sqrt(2 pi))] |t - u|^(3/2) ||f||^2_(H^(25/4)(R)) (unitary Fourier transform, exact
  integral of (1 - cos x) x^(-5/2)) applied to g_axis at t = 8 and u = 1001/125; the pair crosses a C^5 join, which
  the membership theorem permits, and the two fifth derivatives, certified at 1024 bits by two algorithms, differ by
  1.0668240e9 [V186, which gives 36400585492 with the elementary constant sqrt(8 sqrt2/(3 pi))]. A separate floating check by
  central differences gives g_axis^(5)(1001/125) = -6.188399e8 (NUMERICAL). The bound uses only the axis summand, so it
  is independent of the angular cutoff and of the Littlewood-Paley partition. It strengthens the one-point bound
  eta_* > 1906360017, from the Sobolev point inequality
  eta_* >= |g_axis^(5)(t)|/C_5, C_5^2 = Gamma(11/2) Gamma(3/4)/(2 pi Gamma(25/4)), at t = 8, with the fifth derivative
  of the weighted axis trace computed from the original data by two algorithms (full-angular Green-ODE jets at 640
  bits; exact B-spline controls, explicitly differentiated exponential-polynomial velocities and a binomial weight
  series at 1024 bits) [V183]. A separate floating check by central fifth differences inside one spline span agrees to about ten
  digits (NUMERICAL). None of these bounds refutes (S).
- Necessary test of (S) [V184]: under (I) and (S) the exact residual of the j-th iterate satisfies
  ||F_(ell(h_j))(rho_(ell(h_j)) + h_j)||_Y <= q_0^j ||f_0||_Y, q_0 = K_L C K_H eta_0, so the exact first-step residual ratio
  is a lower bound for every admissible q_0 (CONFIRMED as a conditional necessary test; a finite-section iterate
  cannot test it without a certified error bound).
- Scalar-radius test of (S) [V185]: n is increasing with n' >= 3 and every admissible ell exceeds 4, so every
  admissible smallness ball satisfies K_H eta_0 ||c||_(H*) <= N4 = -n(4); hence eta_0 |c[d]| <= N4 ||A_0 d||_(Y_H) for
  every nonzero d in the high graph domain, and 0 < N4 < 9.06 for every admissible chart cutoff (exact rational upper
  expression about 9.04503). The test is invariant under scaling of the high target norm and needs no inverse
  constant. Whether it is violated is OPEN (a heuristic estimate is in 6.5 item 10).
- Target membership of the rank-one split [V190, REFUTED for a separate norm diagnostic]: M_0 = x^2 y + O(r^5) and,
  for a compact annular d with c[d] nonzero, L_fix d = -c[d] x^2 y + O(r^5), so neither belongs to the strong zero-jet
  Sobolev targets of Theorem E, high or low, although A_0 d does (in the Hoelder targets Y, Z_sc and Z_2 of section 3
  both columns are legitimate); in those Sobolev targets norms of A_0 d must use the finite split A_0 d = L_ren d + c[d] m_0, L_ren = L_fix +
  c[.] H_0, with m_0 in Y_H.
- Residual-subtracted test of (S) [V194, CONFIRMED as a conditional necessary test]: with alpha_0 = 1/(ell_0 n'_0),
  Q = rho_0 - U[rho_0].grad rho_0 - k L_fix KP and Q_ren = Q - ell_0 n'_0 H_0, the identities ell_0 n'_0 M_0 = f_0 + Q,
  Q_ren = ell_0 n'_0 m_0 - f_0 and R_d := A_0 d - alpha_0 c[d] f_0 = L_ren d + alpha_0 c[d] Q_ren hold, every term on
  the right is in Y_H (the cubic coefficient of Q is 1 + c[rho_0] + k c[KP] = ell_0 n'_0, and the leading far term of
  k L_fix KP is r^k Theta), and (I) and (S) imply ||R_d||_(Y_H) > 1956082280 |c[d]| for every high-domain direction with
  c[d] nonzero (exact rational threshold (50/453 - k/3) times 38666592266). No upper bound of ||R_d|| is certified.
- Relative form of the same test [V199, CONFIRMED as a conditional necessary test]: the scalar-radius analysis also
  gives the sharper bound N4 <= B = 9.0450253607..., hence 1/N4 - alpha_0 >= 1/B - k/3 = 0.0507711... > 0.0507, and a
  certified ||R_d||_(Y_H) <= 0.0507 eta_0 |c[d]| for one actual high-domain direction with c[d] != 0 would refute
  (S) under (I).
  An explicit admissible direction is given in the next item.
- Explicit test direction [V273, V283]: the Gaussian density d = -Delta v of 6.5 item 10 has c[d] = 1 and J[d] = 0,
  lies in the remainder space with zero scalar input and in the high graph domain D_H(A_0), and the summands of
  A_0 d = L_ren d + m_0 and R_d = L_ren d + m_0 - f_0/(ell_0 n'_0) lie in Y_H. No upper bound of its two norms is
  certified, so the tests of V194 and V199 are not decided for it.
- Scaling tangent [V198, REFUTED for high-space admissibility, CONFIRMED for the exact knot jump and the local
  nonmembership]: K = rho_0 - X.grad rho_0, even after a smooth annular cutoff, is outside the high correction space,
  because the sixth derivative of its axis cofactor jumps at the interior knot t = 2.2021... An independent
  interval evaluation of the original spline data gives a jump of about -9.3e8 in the seventh derivative of the axis
  cofactor of rho_0 there, while the jumps of orders 0 to 6 vanish within the enclosures (cross-check).
- Finite-section accounting: summing final blocks together with the retained cumulative checkpoints counts cells twice,
  and a resumed run assembled from final blocks alone omits cells; the parts-only assembly of the completed, never
  resumed S_1 run covers every cell exactly once [V180, REFUTED for the default assembler, CONFIRMED for the coverage].
  The endpoint and finite-entry checks of the outer margin merge do not suffice for a global replacement bound (exact
  radial and angular counterexamples); no accepted original-data certificate depends on them, and the section, L^2
  section and norm reductions use final blocks only [V181, REFUTED for sufficiency, CONFIRMED for the counterexamples].
- High-energy symbol and uniformity geometry: the principal joint high-energy symbol and its margins at delta = 9/5
  (orders 25/4 and 41/20) and at infinity (gamma = -1/2) [V088]; the velocity radius sup ||DW|| <= 1e-5 that preserves
  the zero set, the types, the quadrant flow and the escape [V090].
- Injectivity reduction: Lemma INJ-S with the Hilbert-norm correction and the graph-norm conversion [V092]; the exact
  norm of the remainder strain functional, < 0.20757 [V093]; the conditional algebra of the finite-rank split [V094];
  the explicit axis-strip constant in four background derivatives [V095], with universal constants 39 and 25 [V099];
  the second-order principal real energy on a regular cylinder [V096] and for the full regular Mellin velocity [V098];
  the Hilbert-Schmidt bound of the paired weight conjugation on a regular patch [V097]; the exact angular reduction of
  the target norm [V100]; exact energy localization with the paired double-commutator defect [V101]; the conditional
  quantitative injectivity certificate INJ-Q for the remainder block [V102, CONDITIONAL]; explicit trace-functional
  majorants and the radial-lift bound [V105].
- The confirmed parts of the report audit [V048].
- Obstructions with explicit counterexamples: V006, V007, V009, V010, V012, V019, V030, V032, V039, V074, V079, V085,
  V201, V203, V208, V210, V211, V213, V217, V224 (J not closable on Y), V227, and
  the refuted parts of V025, V028, V038, V087, V106, V115, V119, V121 and V124, the endpoint counterexample of V117, V153 (the variable-order
  Kato-Ponce bound for the full transport commutator), V162 (a sign in an auxiliary weighted energy), V165 (an unrestricted
  angular Hardy average does not give positive isotropic regularity), V167 (the sign of the leading axis multiplier is
  +2/eta^2, not -2/eta^2), V173 (no uniform third axis derivative bound in the new angular weights for a <= 4), and V111 (the truncated raw-sine angular projection is not a
  contraction); non-implications with explicit examples: V089 (high regularity does
  not follow from the low inverse and frozen data), V091 (C^1 convergence with uniform low inverses does not give
  uniform high inverses), V092 (the sum-norm form of the INJ-S bound).

6.4 Constants and inequalities that require numerical certification.

| Quantity | Needed for | Status |
|---|---|---|
| c[rho~] = 3/k - 1 | every rigorous statement | THEOREM (V005); a separate ball recomputation agrees (computed once) |
| source x_P, mu, g; neighbourhood margin | source inverse | THEOREM (V017, V024) |
| s_3/pi, hence d >= 3 c_l | bordering | THEOREM (V034) |
| C_cap, C_c0, C_> | c bounded | THEOREM (V034) |
| c_R = 0.2075698661066814348... | c bounded on Z (Lemma C'4) | THEOREM (V047) |
| kappa_0, K_A, C_a | origin | THEOREM (V022, V016, V026) |
| m_* for mu~ in (H_m) | Theorem R unconditional for L_fix | THEOREM (V086): m_* >= 5/2 (independent refinement; first 1.78605, V077); a second code gives m_* >= 1.029821 (aggregation verified, V072), refined to 2.471224 and then 2.482724 (computed once); grid value 2.590 |
| m_a for w_a, hypothesis (M) | Theorem C', scheme | best certified value m_a >= 3 (THEOREM, V259; before that 2.9270, V197); earlier THEOREM (V086): m_a >= 5/2, still true (independent refinement; first 0.53072, V077); a second code gives m_a >= 0.965918 (1569 radial cells times 64 angular boxes, aggregation verified, V072), refined to 2.500023, then 2.871539 and, with a finer cover of the first outer sub-cell, 2.9270 (THEOREM, V197, by an independent whole-plane refinement); grid value 3.09 |
| axis rate d = V_2(0, y)/y > 0 with endpoint bounds, hypothesis (A) | N2, axis row (V041), Theorem C' | THEOREM (V077): d >= 5.5752 on the whole axis, with the qualitative endpoint estimates of V055; a second code gives d in [5.575203, 21.301451], sup abs(d') <= 5.6012 and endpoint constants 0.100883, 0.202073 (t <= 0) and 89.3342, 73.3113 (t >= 0) (aggregation verified, V072; its first script was REFUTED in coverage and underflow, V054) |
| lift constants M_1 = sup abs(a_1), M_0 = sup min(r^2,1)^{-1} abs(a_0) of (L) | Lemmas C'1 to C'3, Theorem C' | finite for the modal field (V047, V055); box bounds M_1 <= 337.66, M_0 <= 1075.52 (computed once; the sizes come from the slow angular decay of the far modes near the y-axis) |
| energy limits kappa_0 = 49.7159..., kappa_inf = 3.0908... of w_a | (M) near 0 and infinity | THEOREM (V055); the cutoff radii and the bound on the compact annulus are not certified |
| hypothesis (Z): no zeros of V except 0 and P, P a hyperbolic repeller | Lemma H1 (THEOREM under (Z), V063), Theorem H | THEOREM (V080, with Lemma Z, V071, and the source rectangle Q, V070): the zeros are 0 and the two source points; abs(V)/r >= 3/12500 outside Q in the closed first quadrant away from 0; abs(V(X)) >= 0.1801 abs(X - P) on Q |
| constants of the coupling proofs (operator norms in V049 to V052, the compact K_eps and a finite-rank split of it) | quantitative inverse | finite (V049 to V053), not computed; OPEN |
| norm of the remainder strain functional c_R on R | bounds of Lemma INJ-S | THEOREM (V093): ((58/99)(6618/725) B(3/2, 19/4)/pi^2)^{1/2} < 0.20757 |
| second Fourier moments S2mat(B), S2(b_eta), first moments S_1(g_j); axis suprema M_20, M_21, M_40, M_41 | principal and Mellin errors (V096, V098) and strip constant (V095, V099) of the split | grid values sum S2(B_ij) about 2.15e4, S2(b_eta) about 3.46e4 at eta = 0.1 (NUMERICAL); enclosures OPEN |
| principal high-energy symbol margins | Theorem H | THEOREM for the principal symbol (V088): 142.5074 (y-axis, order 25/4), 0.97261 (x-axis cylinder, order 41/20), 3.78768 (infinity, gamma = -1/2), all at delta = 9/5 |
| velocity radius of the geometric clause | uniformity of the flow portrait | THEOREM (V090): sup ||DW|| <= 1e-5 keeps the three zeros and the flow; speed/r >= 0.00023 outside the source rectangles; source shift <= 1/1801 |
| transport margin kappa_* = ess inf kappa_{w_a} | Lemma C'2 (V046) | THEOREM: kappa_* >= m_a >= 5/2, since b_+ >= 0 (V086); the independent finite-cell computation also gives kappa_* >= 1.6377 directly (a note accompanying V077, not part of its verdict); a second code gives kappa_* >= 3.037693 (V072, conditional on its exported cell enclosures; far limit 3.0908); hence ||T_R^{-1}||_{R -> R} <= 2/5 (Lemma C'2) |
| S0 tail-column strains and denominator 3/k + k c[KP_shifted] | S0 bordering | THEOREM (V043) |
| Delta on boxes near 0 (Prop M) | local strain estimate | NUMERICAL |
| sigma_min of finite sections, off-basis bounds | finite statements only | S0: sigma_min >= 4.3337e-07, reproduced independently as a conditional matrix certificate (V066); >= 2.0685e-02 without TAU, reproduced independently as a conditional matrix certificate (V200); Gram whitening confirmed (V056); off-basis bounds not computed |
| floating values of the three-mode pure-spline section of S_1 (78 columns) | size of the finite-rank part of a split (Lemma INJ-S) | NUMERICAL (V252): smallest values about 2.7655, 3.2685, 4.3913 (about 2.7662 on c[h] = 0); about 50.32, 3.456 and 2.766 for one, two and three angular modes, so they decrease with the angular cutoff, have not converged and are not bounded below by these runs; about 2.8648 for the 60 high-graph-conforming columns, in the LOW norms only. Cell accounting and the input-form relative error below 2.688e-6 are verified (V252); output pairings, image division and quadrature are not certified, so no exact operator bound, finite singular value or complement inverse follows |
| split constant delta, adjoint defects eps_i, norms of psi_i (in INJ-Q form: eps, delta_F, e, p, d, c_loc, eps_small, delta_l, M_C) | Lemma IV.1, INJ-Q (V102), K_L | OPEN |
| axis coefficient bounds alpha, alpha', alpha'' on the lift window; N_j(y) | lift error M_gamma of INJ-Q (V105) | formulas THEOREM (V105); values OPEN |
| eta (residual in the forcing norm, with axis jet) | closure inequalities | membership THEOREM (V042); exact angular reduction of the norm, ||f||_Y^2 = int omega(t)[gamma^2 + 2 B(1/4, 3/2) H(q)] dt with a rational Gram matrix H for the cosine coefficients q of (B - gamma)/cos^2(theta) (THEOREM, V100); six directed point densities (V107); enclosure 6049.11 < ||F(rho~)||_Y < 8601.42 (THEOREM, V164; earlier lower bound 933.47, V110); ||F(rho~)||_(Y_a) < 485.632 in the decoupled family, a in [18/5, 4] (THEOREM, V174); value about 7.2e3 in the present weight and about 13 at a = 3.6 with the far exponent lowered by 0.6 (NUMERICAL, 6.2 item 5); these are low norms; the high norm of Theorem E is enclosed as 3.866e10 < eta_* < 6.321e129 in an explicitly fixed equivalent norm (THEOREMS, V192, V182; the upper end is a deliberately loose majorant), and a realistic value is OPEN; the truncated-sine section output is not a contraction (V111) and cannot be used for it |
| K_H, K_L | closure inequalities | OPEN |
| C_B, C_H, origin cutoff radius delta (S(e), V203 to V207, V219); source radius delta (V215) | localized Hoelder inverses | qualitative, not computed; OPEN |
| C_B, C_V | closure inequalities | finite for the cylinder-H^7 spaces (V057, V060) and for the cone-local space with order s > 2 near the x-axis segment (V065), not computed |
| r_V, from the margin perturbation bound stated below the table | ball radius | the perturbation bound is THEOREM (V075); the margin is certified (V077, V086); r_V is explicit once the high-space constants C_c, C_W (and C_g for a moving background) of abs(c[h]), norm(D W[h]) and norm(grad h) are computed |
| simple turning height of the axis rate a(0, y) = d_x V_1(0, y): y_* in (9.1465, 9.1468), y d_y a in (7.1952, 7.1954) there | turning-height obstruction on Z_2 (3.1) | THEOREM (V256, V262; original-data interval certificate) |
| homological denominators of the source conjugacy (degrees 2 to 11), all 150 above 0.1507 in absolute value; analyticity disk of radius 1/1000 | actual source operator and its conjugacy (3.1) | THEOREM (V214; original-data check) |
| source data 10 < A_s < 51/5 and the source rate mu_s | transport cokernel at the source (V266) | THEOREM (V017, V214); the cokernel statement THEOREM (V266, V272) |

The closure inequalities are K_H eta <= r, K_L C_B K_H eta < 1 and C_V r <= r_V. Here C_V bounds
||D W[h]||_infinity + |c[h]| by ||h||_{X_H}, and r_V is the perturbation size that keeps the weighted margin above half
its value. For w_a and the fixed background the margin kappa_w - b_+ decreases by at most
|c[h]|/3 + (1/2)(sup|mu_a'| + 4a) ||D W[h]||_infinity, with (1/2)(sup|mu_a'| + 4a) = 51/4 for a = 17/4 (THEOREM, V075;
the angular term uses tan(theta) W_theta/r = (y^2/r^2)(-W_1/x + W_2/y), bounded by 2||D W|| through parity). b_+ is
built from the background gradient and does not change; when the coupling background moves, as in the moving-tail
family, b_+ changes by at most ||grad h||_infinity and the full change of the background enters every term. This is a pointwise statement. It does not give the global flow portrait, which the Garding argument does not need.

6.5 The closest avenue and why.
The closest route combines Avenues I and III and uses Avenue IV only for the complement: the anisotropic jet space Z
with weight w_a, the coordinate J and the y-axis jet, the parametric tail ell with the augmented map, and a certified
finite-dimensional injectivity check (Lemma IV.1) for the compact part of the Garding estimate. Reasons:
1. Every frozen piece has explicit constants: Theorem O at the origin and the source inverses are proved (THEOREMS),
   and the far window is DERIVED.
2. The global Fredholm mechanism is proved for radial weights (Theorem R) and, on the jet spaces with the anisotropic
   weight w_a, for the full normalized operator of the modal background under (A) and (M) (Theorem C', V047 with V049
   to V053), and the finite pointwise certificates that make it unconditional are verified independently (V077, V086).
3. The normalization is handled exactly: c is bounded on Z_cap, the origin part is necessary (V032), the tail
   coordinate is eliminated exactly with d >= 3 c_l > 0, and the scalar normalization ell(h) is unique with an explicit
   Lipschitz bound. The reduced operator still needs its own inverse.
4. The margins have room: both are certified >= 5/2 (V086), the angular one >= 3 (V259; grid values 3.09 for w_a and 2.59 for mu~, NUMERICAL),
   against a perturbation cost that is linear in ||D W[h]||_infinity (V075).
5. For a fixed background the compact part of the Garding estimate does not depend on h (DERIVED), so uniformity over the
   correction ball reduces to the h = 0 complement estimate plus the explicit transport defect of V040. In the
   parametric form the ell-dependence of the compact part must also be bounded; this is now proved for the exact
   moving-tail family, together with uniform high and low inverses under base low injectivity (V170).
6. The residual is small pointwise and relative to the profile, and its strong norm depends on the weight by orders
   of magnitude (6.2, item 5), so the weight, the margin and the residual can be balanced within this route: in the
   decoupled family the certified low norm drops from 6049.11 < ||F|| < 8601.42 (V164) to below 485.632 (V174), with a
   certified margin of at least 1.10534 (V171, V172) and the full low Fredholm theory (V172).
7. The assembly is explicit: Theorem E (6.2 item 6, CONDITIONAL THEOREM, V178) reduces existence exactly to injectivity of the base low
   operator and one smallness condition, so a certified injectivity with a quantitative inverse, explicit radii and
   constants, and a high residual norm are precisely what remains.
8. The route can be tested before any constant is certified (CONDITIONAL THEOREM, a necessary test under (I) and (S), V184). For j >= 1 the iterate h_j solves
   A_(h_(j-1)) h_j = -f_0, so the exact identity F_ell(h)(rho_ell(h) + h) = f_0 + A_h h shows that the residual of the
   j-th iterate is (A_(h_j) - A_(h_(j-1))) h_j. The difference bound, ||h_j||_H <= K_H eta_0, the contraction of the
   differences and ||h_1||_X <= K_L ||f_0||_Y give
        ||F_(ell(h_j))(rho_(ell(h_j)) + h_j)||_Y <= q_0^j ||f_0||_Y,   q_0 = K_L C K_H eta_0.
   Hence every choice of constants that satisfies (S) has q_0 >= nu_1, where nu_1 is the ratio of the low residual
   norm after the first step h_1 = -A_0^(-1) f_0 to the low residual norm of the trial. If one exact step of the
   iteration does not reduce the low residual norm (nu_1 >= 1), (S) fails for every admissible r_*, K_H, K_L and C
   (the step h_1 itself presupposes (I), so this tests (S) under (I)).
   The ratio needs one linear solve and one residual evaluation and no inverse constant. A value computed from a
   finite section would be NUMERICAL evidence only, and it cannot refute (S) without a certified error bound for the
   step; it has not been computed in this run. The positivity of the low residual norm that the ratio needs is
   certified (V164, V179).
9. What the trial must improve (NUMERICAL heuristic, not a proof). The high norm eta_0 uses order 25/4 on the vertical
   sector, and that is where the residual sits: for t between 2 and 10, 88 to 99.7 percent of its strong angular energy
   lies within 0.01 rad of the vertical axis, against 13 to 40 percent for the profile, and its order-25/4 proxy
   exceeds that of the profile by factors of about 165 at t = 2 and 14 at t = 4 (6.2 item 5). For this trial, K_H eta_0
   <= r_* is therefore unlikely with any realistic radius. At infinity the residual divided by the high weight decays
   only like r^(2k - 1/2), about r^(-0.14), because the trial carries the far power law without its first correction.
   The far operator ell X.grad - 1 multiplies r^m Theta_m(theta) by ell m - 1, which is 1 - ell and 2 - 2 ell for the
   degrees m = 2k - 1 and 3k - 2 of the far self-interaction, so these corrections are obtained algebraically, with
   one angular derivative lost per order; after the first, the weighted far residual decays like r^(3k - 3/2), about
   r^(-0.96). Since Theta is a finite sum of the modes cos^2(theta) sin(theta) cos(2m theta) and the IPM velocity of a
   homogeneous density shifts angular modes by at most 2 with explicit factors, these corrections are again finite
   trigonometric sums with the parity of the problem, and they vanish to second order at the vertical axis because the
   velocity is tangent to it (DERIVED, not verified). The route needs a trial refined in the axis layer for t between about 2 and 10 and carrying these far corrections, with its
   residual measured in the high norm, before (S) can be tested. The certified high lower bound points the same way
   and adds a second requirement. At t = 8, just inside the outer join, the weighted axis trace g_axis of the residual
   has the value 0.158 and the fifth derivative 4.48e8 (V183), and central differences with steps from 1/256 to
   2^-20 give 1.5e8 to 4.48e8 (NUMERICAL): the fifth derivative varies on the knot scale (spacing 0.008 there), so in
   that region the residual in the order-25/4 norm appears (a numerical diagnostic, not a decomposition theorem) to be
   dominated by the spline approximation error of a C^6 background, whose residual can have jumps of the sixth
   derivative at the joins; a nonzero jump is certified at the interior knot t = 2.2021... (V069), not at every join.
   A trial for the high closure probably needs joins of higher continuity, or an analytic representation, in the region
   the high norm weights most, not only a smaller residual in the low norm (a heuristic conclusion; no necessity among
   all trial constructions is proved).
10. A sharper test without constants, and why the archived trial probably fails it (CONDITIONAL THEOREMS for the test, V185 and
   V194; the failure is a DERIVED heuristic with NUMERICAL input, not a bound). Since n is increasing with n' >= 3 and
   every admissible ell exceeds 4, (I) and (S) imply eta_0 |c[d]| <= N4 ||A_0 d||_(Y_H) for every nonzero d in the high
   graph domain, with N4 = -n(4) in (0, 9.06) (V185). The two parts of the rank-one split, M_0 and L_fix d, are not
   separately in the strong zero-jet Sobolev targets of Theorem E for c[d] nonzero (their cubic coefficients are 1 and
   -c[d], V190; in the Hoelder targets Y, Z_sc and Z_2 of section 3 both columns are legitimate), so the residual itself is subtracted:
   with alpha_0 = 1/(ell_0 n'_0) and Q_ren = ell_0 n'_0 m_0 - f_0, R_d = A_0 d - alpha_0 c[d] f_0 = L_ren d +
   alpha_0 c[d] Q_ren, every term lies in Y_H, and (I) and (S) imply ||R_d||_(Y_H) >= (1/N4 - alpha_0) eta_0 |c[d]|
   > 1956082280 |c[d]| whenever c[d] != 0, in the norm of the enclosure above (V194; the constant is 50/453 - k/3 times the certified lower
   bound of eta_*). One certified upper bound ||R_d|| <= 1956082280 |c[d]|, or ||R_d|| <= theta eta_0 |c[d]| with
   theta <= 0.0507 (V199, using the sharper bound N4 <= 9.0450253607...; the bound 9.06 alone gives 50/453 - k/3 =
   0.050588...), for a single actual direction with c[d] != 0 would refute the conjunction of (I) and (S), hence (S) under (I) (not
   (S) alone while (I) is open). Neither is certified. An exact admissible direction is available: with g(y) = -(y^3/6) exp(-y^2), a_g = 2g - g'', b_g = g'''' - 12 g'' + 12 g and
   v = exp(-x^2)(g + x^2 a_g/2 + x^4 b_g/24), the Gaussian density d = -Delta v equals x^4 y P(x^2, y^2) exp(-r^2) for
   a rational polynomial P; its canonical velocity is (-v_xy, v_xx), c[d] = 1 and J[d] = 0, it lies in the
   remainder space with zero scalar input and in the high graph domain D_H(A_0), and A_0 d = L_ren d + m_0 and
   R_d = L_ren d + m_0 - f_0/(ell_0 n'_0), each summand in Y_H (THEOREM, V273, verifier proof, independent audit
   recorded as V283; exact polynomial data in the accompanying
   artifacts). Each test therefore reduces to one certified upper bound of an explicit high norm; none is computed.
   The heuristic reason to expect a violation: floating central differences of the weighted axis trace at every fourth
   span midpoint (accompanying artifacts) place its knot-scale structure in two zones, (a) t in [1.92, 2.62] (r about
   7 to 14), where the knot gaps go down to 0.0019 and |g_axis^(5)| reaches 6.06e9 with sign changes between neighbouring
   samples, and (b) t in [7.9, 8.135] next to the outer junction, up to 1.93e9; elsewhere |g_axis^(5)| <= 2.1e6, and
   beyond t_+ it falls to about 30 at t = 8.5 (NUMERICAL).
   What the knot-scale part is (NUMERICAL; interval evaluation of the exact spline polynomials span by span,
   accompanying artifacts). On each span the modal cofactor r^(-3) rho_0 of each sine mode, as a function of t, is a
   polynomial of degree 7 (the physical density rho_0 itself is not), so its seventh t-derivative is constant there. In both zones these constants alternate in sign from span to span: near
   t = 2.2 the seventh derivative of the axis cofactor A of r^(-3) rho_0 is 3.6e8, -5.7e8, 5.8e8, -4.4e8 on four
   consecutive spans while A = 0.52, and its jump at the knot t = 2.2021 is -9.3e8 (the jump of V198; these values
   and the alternation are reproduced from exact rational spline coefficients in V209, to 2e-4 relative). Read as a
   component of period two knot gaps, the alternation has amplitude about (h/pi)^7 times the alternating part of the
   seventh derivative. Relative to the largest mode of the profile this amplitude is about 4e-16 (median) for t in
   [3.5, 7] and 1e-16 for t in [-4.5, 1], the level of binary rounding; it is 3e-12 (median) and up to 4.7e-10 (mode
   2 at t = 2.18) for t in [2, 2.4], where the knot gaps are 0.0019, with partial cancellation to 1.4e-14 in A; and
   next to the outer junction it grows towards t_+, from rounding level at t = 7.9 to 4.9e-13 of A on the last span
   (V209; over the last 30 spans the growth factor per three spans has median 2.5 and ranges from 1.5 to 21.5, so it
   is not uniform). The certified lower bounds of eta_* (V183, V186, V192, all evaluated at t = 8 and 8.008) and the
   zone values of g_axis^(5) sit where this component is large. The heuristic reading is that they are produced by a
   component of relative size 1e-13 to 1e-10 of the profile, which the high norm amplifies by about (pi/h)^(25/4 + 1)
   together with the transport speed and the weight. This is a numerical diagnostic of the archived trial only: it is
   not a spectral decomposition, not a failed test of (S), and it says nothing about whether an exact profile near
   the trial has such a component (V209 confirms the numbers, not this reading). A trial that differs from rho_0 by such an amount and lacks this component would
   have far smaller high-norm values in the zones (heuristic; outside the zones |g_axis^(5)| is at most 2.1e6, about
   3e3 times smaller than in them). The B-spline coefficients cannot be cleaned by index differences: on these knots
   the coefficients of a smooth function are not smooth in the index (eighth differences up to about 2e-5 of the
   coefficient size), and the filter c - Delta^8 c / 256 on t in [1, 3.5] increased |g_axis^(5)| at almost every sample,
   by about five orders of magnitude near t = 2.2 and up to eight elsewhere (NUMERICAL, accompanying artifacts). The point and difference functionals of the lower bound near
   t = 2.23 give about 2.6e10 and 3.3e11 (NUMERICAL), so eta_* is probably far above its certified lower bound. Split
   rho_0 into a smooth part and its knot-scale part rho_knot. At the knot scale f_0 is (ell_0 + u) d_t rho_knot, with u
   the radial transport coefficient of U[rho_0]; the angular transport, -rho_knot and U[rho_knot] are of lower order in
   the knot scale. The chart direction M_0 is (1 - k^2 u[KP]) d_t rho_knot / n'_0 at the same scale, and L_fix d is
   u[d] d_t rho_knot. For a smooth direction d = x^2 y beta(t) with beta supported in t in [0, 1], u[KP] and u[d] are
   small in both zones by the decay of these velocities (floating order-of-magnitude estimate), so the knot-scale part
   of A_0 d is W f_0 with W about c[d] / (n'_0 (ell_0 + u)). The axis value ell_0 + u is 18.1 to 14.2 in zone (a) and
   5.71 to 5.69 in zone (b) (NUMERICAL). The first step is checked on the axis (NUMERICAL, accompanying artifacts): with
   q the weighted axis trace of X.grad rho_0, the central fifth differences at every eighth span midpoint satisfy
   g_axis^(5) = (ell_0 + u) q^(5) up to a relative l2 deviation of 1.6 percent over the 29 samples of zone (a) and
   0.8 percent over the 4 samples of zone (b), with pointwise ratios 0.97 to 1.06 wherever |g_axis^(5)| > 1e8; outside
   the zones the two differ, since there q^(5) is dominated by the smooth part of the profile, which the residual
   cancels. On these samples ||g_axis^(5)|| / ||q^(5)|| = 14.4 and ||q^(5) - g_axis^(5)/ell_0|| / ||g_axis^(5)|| = 0.117
   (l2 over the samples, a crude proxy of the axis summand, not of the norm). If the knot scale dominates the high
   norm, eta_0 |c[d]| / ||A_0 d|| is about n'_0 (ell_0 + u) >= 16.7 (14.4 n'_0 >= 43 on the axis proxy), against N4 < 9.06, and the knot-scale part of R_d is c[d] f_0 (1/(ell_0 + u) - 1/ell_0)/n'_0,
   which nearly vanishes in zone (b) and is 0.036 to 0.041 times |c[d]| f_0 in zone (a) for n'_0 = 3, below the
   threshold 0.0507 (for larger n'_0 the left side decreases and the threshold increases; 0.117/n'_0 <= 0.039 on the
   axis proxy).
   In words: at the knot scale the image of a strain direction is nearly parallel to the residual itself, with a
   ratio too small for the scalar-radius test. This does not determine the actual Newton step: an exact
   two-dimensional example shows that an image nearly parallel to the residual and a failed test are compatible with a
   Newton step whose scalar component is zero (V195, REFUTED as a general inference about the Newton step). A failed
   test would rule out (S) under (I), not existence. A rigorous version needs an upper
   bound for the high norm of R_d with its knot-scale part removed, and a check that the angular structure of the
   near-axis layer, which this axis test does not see, follows the same proportionality; the present tools (the
   cutoff constant C_chi and the factor 2^sigma of the partition behind the upper end of the enclosure) are far too
   coarse for that. The conclusion
   for the next trial is the one of item 9: its high residual norm must not be dominated by knot-scale structure.
Avenue II is farther: there is no Hoelder Garding inequality, the Hoelder theory of the actual transport near 0 is
established only for localized whole-plane operators (3.1, S(e)), in whose graph norm the cubic coordinate is not
closable (V208), and Lemmas N and N' show that Hoelder norms alone cannot close the nonlinear problem by a semilinear
perturbative map (in that very graph too, Lemma N'', V211, V218; a quasilinear scheme is not excluded). On the common
target Y the full operator is closed but the error of the specified cutoff parametrix is not compact (V227; sums of
patches are not excluded) and it is not onto Y (THEOREM, V232, V234; also on E_2 and for every gamma > 4k, V241,
V247), so a global Hoelder inverse needs a different far-field target. On the candidate Z_sc the
exterior operator is invertible (THEOREM, V236, V242), but Z_sc is not a valid global target either (THEOREM, V243,
V249); the next candidate Z_2 has the mapping theory, a closed maximal realization, residual membership and an actual
auxiliary exterior inverse (THEOREM, V245, V254), its global inverse is OPEN, and the middle annuli are not matched.
At a simple turning height of the axis rate T is not onto Z_2 for alpha > 1/2, and A_0 and L_ren are not onto it for
alpha > 2/3 (THEOREM, V256, V262; alpha > 1/2 for all three by V257, THEOREM, V265;
alpha <= 1/2 is OPEN for A_0 and L_ren). The joint-cofactor target Z_cof excludes these forcings and carries the
mapping, the residual and an exterior inverse (THEOREM, V261, V268); its global inverse is the next open step of
Avenue II, T alone is not onto it near the source for alpha > 1/A_s (THEOREM, V266, V272), and
the nonlinear step on it needs a quasilinear scheme or stronger derivative norms (THEOREM, V264, V271).
Avenue IV alone is farther:
a finite section is not an inverse bound without a complement estimate (V014), and in the S0 realization it
cannot be one (Prop IV.O, V039); the L_fix and S_1 floating sections use other, consistent low realizations not
covered by that mechanism, but they certify nothing and their complement is OPEN.

6.6 Checklist against the strict standards.

| Standard | Status |
|---|---|
| Every inverse states its domain and range | Theorem O (Z_0 -> Y); Theorem R (maximal domain D_w -> L^2_P(w)); source inverses (maximal H^s domains); axis row (B -> Gamma, V041); pure transport (Z = E B (+) D_R -> Y = E Gamma (+) L^2_P(w_a), V046; its hypotheses hold for the modal background, V047, V055, V077); Theorem C' (Z -> Y, THEOREM for the modal background, V047 with V049 to V053, V055, V077, V086); the high-domain form of Corollary H-spec (E B_H (+) D_H -> E Gamma_H (+) Y_H, DERIVED); the perturbed scalar row (B_H -> Gamma_H, V166); the full perturbed and moving-tail blocks (B_H (+) D_g -> Gamma_H (+) X_s in the high realization, V168, V170; B (+) D_L -> Y in the low realization, V169, V170); Prop IV.O (maximal S0 domain); the frozen Hoelder saddle inverses (S(a) to S(d), V028); S(e) (maximal domain -> E_2, V206, V207); the source on X_alpha (maximal transport domain -> X_alpha, V213, V215); the closed realizations L_ren and A_0 on the common target (maximal domain D_Y in Y, V224, V228; not onto Y, V232, V234); the exterior inverse in scaled far norms (maximal exterior domain D_R -> F_R, V236, V242), and its version for Z_2 (THEOREM, V245, V254; global inverse OPEN) |
| Membership of perturbations and images | checked: x^2 y chi_0 in Z (J = 1); r^k Theta not in Z; the modal residual and the parametric residual in Y (V042); c bounded on Z (Lemma C'4, V047); L_fix h not in Y for an explicit h in Z (V044), so the strain term is part of the coupling |
| Normalization meaningful and closed | J continuous on Z_0 (V022); c bounded on Z_cap (V034); c not closable on the radial graph (V032) and J not closed in weak norms (V012), so those spaces are not used for the normalization; ell(h) unique (V038); in the Hoelder realizations J is not closable in the E_2 graph (V208; the smooth kernel of J and c has the same graph closure as the smooth c = 0 domain but is not dense in the whole maximal graph, V216, V217) and c is unbounded on C^alpha_b intersected with L^2 (V213), so the Avenue II inverses carry no closed cubic normalization |
| Log variations of exponent perturbations | KP = chi_inf r^k log r Theta_0 carried explicitly; parametric family; log^2 second variation noted (V025) |
| No unproved finite rank, compactness or small residual used as invertibility | complied with; the Fredholm statements are labelled as such; the compact operators of V049 to V053 are qualitative and are not used as bounds; injectivity is OPEN |
| Counterexamples where a bound fails | V006, V007, V009, V010, V012, V019, V025, V028, V030, V032, V038, V039, V044; Prop F4 (V067: the explicit corner singularity that limits the frozen high inverse) and the parity-only threshold (V067); the knot jump of the spline background (V069: the residual is not locally H^(13/2)); the two-zero field for the product-only Jacobian test (V071); the oscillatory packet and the two transport graph domains (V074); the cone-supported frozen forcing whose low-domain solution leaves the cylinder high space at origin exponent 3/2, order 21/10 (V079); the oscillatory packets that refute a one-order gain of the coupling (V085); the rank-one perturbation with the same low inverse and no high regularity (V089); the torus family with C^1-convergent coefficients and growing high-order inverse norms (V091); the cubic direction that blocks the direct shifted continuation (V106) and the escaping sequence at the non-Fredholm point D/4 of the shifted scalar row (V109); the test input cos^4(theta) sin(37 theta) for the noncontractive raw-sine section (V111); the oscillatory scalar input that rules out the integer target H^6 (V115) and the endpoint input r^(1/2) chi_- for the unweighted localized scalar target (V117); the cone packets that refute (H1) for the sharp cone sum (V119), whereas the conormal-power mechanism for it is refuted (V124); the inner forcings with infinite cubic trace when the tied weight exponent is at most 4 (V121); the C^5 lacunary transport coefficient (V127); the t-frequency packets at the vertical-axis end (V128); the lacunary tangential function for the angular Hardy average (V165); the sign of the axis multiplier (V167); the concentrated smooth-core inputs with growing third axis derivative in the new angular weights (V173); the cubic coefficients that keep M_0 and L_fix d separately outside the strong zero-jet Sobolev targets of Theorem E (V190); the two-dimensional example in which a failed scalar-radius test coexists with a Newton step of zero scalar component (V195); the cutoff scaling tangent outside the high correction space (V198); the factor-free Hoelder strain bound (V201); the derivative necessity and the (1 + A)/D barrier (about 0.5227) for the localized Hoelder coupling (V203); the smooth packets on which the cubic coordinate is not closable in the local Hoelder graph norm (V208), and the |z|^alpha cusp showing that smooth inputs are not dense in that whole graph (V217); the smooth packets with c[h_eps] = eps^(alpha-1) c[H] on C^alpha intersected with L^2 (V213); the flow-box packets with c = J = 0 on which the error of the specified cutoff parametrix on the common target is not compact (V227) and the analogous single origin patch on Z_sc (V239, V246), neither excluding sums of patches; the far forcings near the x-axis and the far vertical strips x^2 phi(x) y^(-b) that have no preimage in the common target (V234, V232); the transverse powers |x|^sigma along the outgoing vertical axis that have no preimage in Z_sc (V243, V249); the turning-height forcings on Z_2 that have no uniformly bounded preimages (V256, THEOREM, V262); the compact input with nonzero third velocity moment for p > 2 and the logarithmic source packets at alpha = 1 (V229, V230); the strips on which the quadratic term is discontinuous in that graph norm (V211); the i = 6 and 27 pure spline columns, in the high input space but not in the high graph domain (V210); code defects V020, V027, V033, V037, V054, V058, V068, and the finite-section input division error (V187) and coverage check (V188) |
| Absence of a proof is not nonexistence | complied with (section 0) |

## 7. Accompanying artifacts

- Weighted Hilbert-space theory: Theorem O, N1 to N5, Lemmas G1 to G3 and Theorem R, the jet-compatible weight, the spaces Z and Y
  with Lemmas C'1 to C'4 and Theorem C', the high-order space (Prop F4, Lemmas H1 and H2, the threshold table and
  Theorem H), the obstruction audit.
- Direct Hoelder theory: the Hoelder theory (H0, S(a) to S(e), the sharp normalized origin rate, the source theory
  including C^alpha_b intersected with L^2, Lemmas N, N' and N'').
- Singular-functional estimates: Prop M, Corollary C1, Prop C2, the renormalized coupling, Prop B and the dual criterion.
- Finite-basis certification: Avenue IV, Prop IV.O and Lemma IV.1; a detailed companion document records the exact
  pipeline and its runs.
- Numerical certificates: every numerical inequality with its enclosure, method and status.
- Nonlinear closure: the nonlinear structure, the two-norm scheme, the missing estimates and the constants.
- Reproduction instructions: inputs and their hashes, reproduction steps, and how to continue.
- The code and data of the strong-residual study (original-data point densities with all angular modes, the
  quadrature for eta, the angular layer, truncation and weight-family diagnostics, and the axis-trace profile and
  knot-scale ratio check of 6.5 items 9 and 10, the span-by-span scan of the sign-alternating component, the
  seventh-derivative knot jump and the coefficient-filter experiment), with checksums; NUMERICAL.
- The conventions file, the code and data, and the verification report with proofs and
  evidence for every record cited.
- The accompanying artifacts include the seven companion documents and conventions; the verification record,
  final verification summary and theorem map; proofs with code, evidence and certificates; and the numerical
  report with its certificate and basis discussions, reproduction instructions, code and data. Verification evidence
  files larger than 2 MB are listed with their sizes and SHA-256 checksums instead of being copied. An omissions list
  identifies the few further files left out for size or because they are third-party texts or machine-specific
  file-identity receipts. Supporting high-norm arguments cover the variable-order lemmas, the high a priori estimate
  and conditional existence, with independent proof audits. Residual, margin, high-norm and rank-estimate scripts
  retain their outputs and checksums. Reproduction instructions describe the contents, and a manifest gives the
  checksum of every accompanying file.

## 8. Record of actual work time

All times are UTC on 2026-10-28 and are taken from the session logs. The run started at T0 = 00:20:16 (logged). The
planned 18-hour window ran to its cap at 18:20:16, when the run was stopped; the last research sessions ended at
18:20:07 (numerics team), 18:20:21 (theory author) and 18:20:32 (verifier), and automatic restarts after the cap
(18:20:37 to 18:21:16) did no work. The report and its artifacts were then finalized, without new research or
computation, from T_end = 18:22:05. Elapsed time from T0 to T_end: 18 h 01 min 49 s. Three roles worked concurrently and
communicated only through files: the theory author (mathematics, conventions, the reports), the numerics team (the
Avenue IV computations) and the verifier (every record V001, V002, ... cited here). Each ran in consecutive sessions of
at most six hours.

| Role | Sessions | Actual session time |
|---|---|---|
| theory author | 00:21:14 to 06:21:15; 06:21:45 to 12:21:45; 12:22:15 to 18:20:21 | 1078 min (17 h 58 min) |
| numerics team | 00:21:14 to 03:31:23 (the session ended early, after 190 minutes); 03:31:53 to 09:31:53; 09:32:23 to 15:32:23; 15:32:53 to 18:20:07 | 1077 min (17 h 57 min) |
| verifier | 00:21:14 to 06:21:14; 06:21:44 to 12:21:45; 12:22:15 to 18:20:32 | 1078 min (17 h 58 min) |

Computing resources were shared single-thread processes on one machine, without cluster, remote or paid compute. The
theory author and the verifier ran at most one computation each under the CPU limits; from about 04:20 they shared
three cores. The numerics team had a two-worker limit from about 01:50 and a four-worker limit from about 04:20. Long computations (the margin
certificates, the residual enclosures, the finite sections) ran detached and were checkpointed. Elapsed time is
reported here; it is not a measure of completed research, and the open items of section 6.2 remain open.
