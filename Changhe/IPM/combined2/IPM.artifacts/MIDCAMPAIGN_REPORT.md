# Mid-campaign report (combined2), the coordinator

Written 2026-11-03T09:35:35Z (hour 15.5 after T0 = 2026-11-02T18:05:30Z; the mid-campaign window is hours 12 to 24).
Sources: ledger v04 (JOINT_CLOSURE_LEDGER.md as of 2026-11-03T05:40:08Z, SHA256 5cccf545...; read-only copy
coordinator/ledger_history/JOINT_CLOSURE_LEDGER_v04.md) and the items after it: theory_v08 (the exchange, 06:05:46Z, SHA256
3493ded5...; integration CONFIRMED conditionally in AT-466 and AT-467, broader readings OPEN in AT-468), theory_v09
(the exchange, 08:52:58Z, SHA256 e9c5378d...; integration CONFIRMED within its scope in AT-644, one literal radius upper
REFUTED in AT-645, broader readings OPEN in AT-647), numerics_v04 (05:01:14Z, SHA256 6f63bf17...), numerics_v05
(08:07:09Z, SHA256 aafb8b71...; integration unaudited), the theory auditor AUDIT_LEDGER through AT-680 (09:33:47Z), the numerical auditor
AUDIT_LEDGER through OBS-ANNULUS-TIMING-001 and audit_v144 (09:33:00Z), agent notes through 2026-11-03T09:26Z. Paths
are relative to the combined2 root. Labels as in WORKSPACE_CONTRACTS.md section 3: PROVED and CONFIRMED only with a the theory auditor entry
(theory) or a the numerical auditor entry (numerics); "conditionally" means under the retained hypotheses named in the entry; FLOAT
numbers are floating-point values without an enclosure; HEURISTIC marks a planning reading. No closure ratio is
computed in this report.

## 1. Verdict at mid-campaign

COMPLETE EXISTENCE THEOREM CERTIFIED: NO.

First unresolved condition: O3, the closure inequality of the invariant ball. No center, corrected or not, has a
certified invariant ball. At the working center 009 the actual-generator and uniform-ball hypotheses (G2) are also
unverified; at stipulated values of the other items they reduce conditionally to G1, L, B and G3 (AT-600).

Remaining gap on the working route. The current working route is route Q with the CE variant (HF-Q-CE) at the tuple
P-S1 = (q, sigma, r0) = (21/10, 1, 1/2) (Section 2) and the lead center C2-N1-009 (Candidate 007 plus the exact
correction b14s), both chosen heuristically. HF-Q has the smallest audited k-dependent loss so far; no smallest
complete closure gap and no optimal weight is established (theory_v08). On this route a stationary solution would
follow once five items are certified:

| item | what is needed | status at mid-campaign |
|---|---|---|
| G1 | a certified whole-plane upper of N_(21/10)(F_*) at P-S1 below the passing level | OPEN; the FLOAT whole-plane N_(21/10) 0.02192 (the second numerics agent, per-mode Hankel transforms, no error enclosure) lies below the CONFIRMED necessary CE levels 0.096618 to 0.135848 (a stipulated comparison, Section 5); the complete P-S1 exterior derivative energies through order 3 beyond r = 1e4 are certified (OBS-009-EXTERIOR-OPERATOR-001, AT-499; zeroth order also OBS-009-TAIL-001), and their substitution into the assembly is CONFIRMED conditionally (AT-505); the origin disk bounds of the complete source 009 on |X| <= 1/50 through order 3 are CONFIRMED at P-S1 and P-S2 (the numerical auditor OBS-009-ORIGIN-PS1-APPLICATION-001 and OBS-009-ORIGIN-001; the theory auditor AT-529, AT-530, AT-537, AT-538); the wide-annulus endpoints on 1/50 <= r <= 1e4 and the assembly are outstanding (annulus preparation CONFIRMED conditionally, AT-527, AT-528; source-bound request and both policy targets CONFIRMED, AT-542, AT-543; the order cap 512 is REFUTED as sufficient for the current full trial and the algebraic cap-replay method is CONFIRMED, the numerical auditor OBS-009-ANNULUS-CAP-METHOD-001, 07:24:49Z; the cap-only selection is CONFIRMED conditionally and the saved partial-trial orders are CONFIRMED, AT-555, AT-556; the completed original 36-row trial admits all three original policies under the computational cap 2048, the numerical auditor OBS-009-ANNULUS-COMPLETE-TRIAL-001, 07:38:00Z; three additional smaller-disk geometries satisfy the analytic panel hypotheses, CONFIRMED conditionally, AT-561, AT-562, and the numerical auditor's scheduling probe found orders 259/274/203, 180/175/132 and 144/130/106 at radii 2, 8 and 32 for 16, 32 and 64 panels per doubling, the numerical auditor audit_v119; the complete-trial selection of six panels per doubling among the three original policies is CONFIRMED conditional on the accepted source majorants, AT-572, with no endpoint or measured run time, AT-573 (the numerical auditor's crude extrapolation puts planning alone near 76 minutes, audit_v118); the full P-S1 planner with that policy started at 07:53:56Z, audit_v121; the compact radial-jet method is CONFIRMED on the admitted adapter domain, AT-568, AT-569, AT-577, AT-578, its application OPEN, AT-571, AT-579; the compact annulus pipeline and the compact whole-plane adapter CONFIRMED conditionally, AT-583, AT-584, AT-595, AT-596, and queued after the planner together with the assembly, the cover and the strain refinement, audit_v123; the full planner completed all 114 panels at 09:16:34Z (every retained analytic remainder within its budget, orders 56 to 682 below the reviewed cap 2048; the plan CONFIRMED conditionally on the saved complete source majorants, AT-668, and the compact request CONFIRMED, AT-669), and the 1024-bit primary integration started at 09:16:42Z as the only busy computation (the numerical auditor OBS-009-ANNULUS-START-001, audit_v139); its first panel (1/50 <= r <= 7/300, order 156) completed at 09:21:59Z and passed the independent 1536-bit reduction with small containing widths and negligible arithmetic error, which does not test the later orders up to 682 (OBS-009-FIRST-PANEL-001, audit_v140, CONFIRMED for this panel only); from the first three panels (active wall times 236.0 s, 207.8 s and 189.9 s at orders 156, 135 and 121) the numerical auditor's two HEURISTIC full-primary predictions are 10.31 h and 25.55 h, that is an end of the primary alone near 2026-11-03T19:35Z or near 2026-11-04T10:50Z, hour 25.5 or hour 40.7 (coordinator arithmetic from the 09:16:42Z start; OBS-ANNULUS-TIMING-001, finite arithmetic and observed timings CONFIRMED, extrapolation OPEN, the two predictions not a certified range); the theory auditor CONFIRMS the first-panel intervals and its whole-plane lowers, among them N_(21/10) >= 0.000498 (AT-671, AT-672), and no upper follows (AT-673, OPEN); the queue v80 (26 stages) adds an unweighted-energy quotient calculation after the P-S1 assembly, audit_v124, whose method and code are CONFIRMED conditionally, AT-603, AT-604; endpoints OPEN, AT-507, AT-543, AT-556, AT-562, AT-573, AT-585, AT-597, AT-605); whole-plane assembly method CONFIRMED conditionally (AT-397 to AT-399); radius 1e4 annulus cover CONFIRMED conditionally (AT-456, AT-457); the P-S1 assembly needs no P-S2 annulus (AT-484, CONFIRMED conditionally) and the one-weight application is prepared (AT-485); no endpoint yet (AT-486, OPEN) |
| L | certified lower and upper bounds of ||F_*||_2 (they fix the ball radius R = ||F_*||_2/beta_0) | OPEN; FLOAT 2.84e-6 to 2.86e-6 (the first numerics agent repaired background 2.8476e-6); the unweighted bracket comes from the same regional certificates as G1 (AT-484); the exact quadratic-division method that gives a containing unweighted panel and whole-plane energy from the complete P-S1 zeroth-integrand coefficients, and its code, are CONFIRMED conditionally (AT-603, AT-604; bindings, the numerical auditor OBS-009-UNWEIGHTED-REVIEW-BINDING-001) and queued after the P-S1 assembly; the 009 endpoint is OPEN (AT-605) |
| B | a certified rate b0 <= beta, that is a global background gap BG-6 at the center | OPEN; at five exact points both weight-specific eigenvalue intervals (ten in total) lie above the origin cap c + 1 - q, with field-evaluation dependencies (AT-443); global gap OPEN (AT-445); a seven-field global cover theorem for the background matrix, the correction gradient and the strain is CONFIRMED conditionally and its application prepared (AT-508, AT-509), no completed cover (AT-511, OPEN) |
| G3 (H4) | an explicit upper of the base weak-energy constant C^opt(b0) at P-S1 below a sufficient budget D for compatible certified inputs; at the stipulated triple (||F||_2, beta_0, N(F)) = (2.76e-6, 209/100, 0.0152) D = 1.59e10 to 2.85e10 (AT-383), and at l = 2.76e-6, beta_0 = 209/100 with the hypothetical N_(21/10) inputs 0.0141 (motivated by the FLOAT N_2 of 009, not an observed N_(21/10)) and 0.022 (about the FLOAT N_(21/10) 0.02192), D = 1.62e10 to 2.88e10 and 1.44e10 to 2.66e10 for b0 = 0.60 to 0.7103 (AT-563); all sufficient at stipulated inputs, and their use at 009 needs certified forcing and N_(21/10) uppers and a certified rate; 209/100 lies above the certified base bound 2.00215453 and is not available by the RC-3 rule (theory_v09 V9-3 (a)) | OPEN; no complete H4 construction is priced (details in Section 3). (i) TII-0: excluded at cutoff radius rho <= 10 for b0 >= 3/5 (AT-423, AT-449). Over every rho, Proposition TII0-RHO (AT-549, CONFIRMED conditionally) with the first theory agent's FLOAT screen on unchanged 007 coefficient data at the source lower l = 2.76e-6 leaves no rate unexcluded for the N lowers 0.01, 0.0141 and 0.022 (FLOAT decisions reproduced on [0.15, 0.7103], AT-551, AT-559; endpoint rate intervals covered, AT-558, CONFIRMED conditionally); at the stipulated source lower input l = 1.5e-6 (about the FLOAT size of 011; the FLOAT norms of 012 and 013, 1.4294e-6 and 9.949e-7, lie below it, and no certified lower of a candidate norm is cited; the necessary level is nonincreasing in l, AT-519, so a smaller l does not strengthen the exclusion), the FLOAT exclusion threshold lies between n = 0.022 and 0.03, so middle rates (at least [0.32, 0.45)) are not excluded at that size (theory_v09 V9-4; the screen is reproduced as a FLOAT observation only, AT-642, and its necessary-budget cells are CONFIRMED conditionally, AT-640); a rate that is not excluded is no evidence that TII-0 closes, and the point-only certification rule for a TII0-RHO cell is REFUTED, a certified positive-area integral lower being needed (AT-646); the actual-source exclusion is OPEN (AT-643). (ii) The J^(-1)-energy construction (Lemma TII-1 and the C_aw bound, AT-473, AT-474, CONFIRMED conditionally) is not excluded: for 008 and 009 some large rho pays the far TII and C_aw terms from the free gain q(c - s_*) if a certified global s_* < c exists (AT-476, qualitative; AT-479 OPEN). The target s_* <= 3/2 would guarantee a gain of at least Gbar, between 0.6516 and 0.6517, and with Gbar as the conservative budget a combined far charge at most Gbar suffices (AT-510, AT-513, CONFIRMED conditionally); the origin value gives only G <= q. The far constants of the complete 009 source, the radius and the near-field price are OPEN (AT-483, AT-518). (iii) A valid even-even far charge bounded by G needs SC_q(a_f) <= G (AT-545, AT-553, AT-548; necessary only); at P-S1, for a real coefficient with an ordinary integrable Fourier transform and finite second Fourier moment, whose joint-form upper holds for every real Schwartz test even in x and odd in y, agreement with atil near zero forces the joint charge to be at least 4[q^2(2c - 1) + 1], a constant in (50.228061735855931, 50.228061735855933) (AT-547, AT-553). The inference C^opt >= P from constructed prices is REFUTED (AT-552). (iv) the second theory agent's FLOAT far charges and HEURISTIC HF-1 near prices for the complete 009 coefficient (07:41Z note) exceed the necessary budget U at every sampled rate with a budget for every scanned split with A_a <= G, even at G = q; they are CONFIRMED as finite model arithmetic only (AT-574), the sampled near Hessian maxima lie below the exact floor 8(2c - 1) and are not certified uppers (AT-575, CONFIRMED under the accepted normalization and near-cutoff hypotheses), and they exclude neither the construction at every rate nor the optimized constant (AT-576, OPEN). The updated tables of the frozen T2_FAR_v01 (08:29:12Z) are CONFIRMED in the finite FLOAT/HEURISTIC scope (AT-615, AT-616): the sampled minima of P_A/U are 8.9314 and 7.7777 at Gbar (log 32, rho 3) and 2.6896 and 2.3422 at G = q, at N 0.022 and 0.0141; on such a fixed finite scan with gain-independent prices and budgets, failure at G = q implies failure at every G <= q (AT-613, CONFIRMED in the stated finite-model scope). Certified complete far inputs and a certified global strain bound give the far condition (FG1) when the explicit TII-1 + CAW scalar charge fits the certified gain (AT-624, CONFIRMED); rounded or interpolated FLOAT values alone do not meet it, and no source-009 far certificate or all-rate exclusion is supplied (AT-614, AT-617, AT-623, AT-627, OPEN). |
| G2 | the actual-generator inverse, domain and uniform-ball hypotheses at the center | OPEN; at 009 conditionally reduced: Lemma KB (the first theory agent research/recenter_g2/KBALL.md) bounds the strain and velocity of U[k] on the P-S1 weighted reference ball (AT-598, CONFIRMED), and on the ball with Mb = 1/2 and Rb = 2.8476e-6/(7/4) the matrix loss is below 0.150314 (AT-599, CONFIRMED at stipulated inputs); with certified ||F_*||_2 <= 2.8476e-6, correction gradient g_* <= 1/4, global matrix rate beta_* >= 3/5 and the certified base rate beta_0 > 2.00215453 (AN-010), the full re-centered inverse holds uniformly on that ball and the route-Q bridge reduces to the H4 inequality and the scalar source test (AT-600, CONFIRMED in conditional form; the inverse constants are finite but qualitative); these premises are not supplied, and a larger certified source upper or a smaller certified rate needs a recomputed ball or witness (AT-602, OPEN); for unchanged 007 only, qualitative O1 and restricted Sobolev O2 on the specified small coefficient balls are CONFIRMED at the listed tuples (full Holder-ball O2 and the numerical inverse constants OPEN); at corrected centers the qualitative parts of RC-1 and RC-2 and the RC-3 transfer rule are proved, the quantitative and uniform-ball hypotheses are not verified |

Of these, G3 is the item without a priced construction. The oscillation constant that blocks the TII-0 construction
at rho <= 10 is universally sharp (AT-451, AT-460, AT-464), so an improvement must use structure of the actual source
(AT-452). Over every cutoff radius, Proposition TII0-RHO with the first theory agent's FLOAT screen on unchanged 007 coefficient data
at the source lower l = 2.76e-6 leaves no rate unexcluded for the N lowers 0.01, 0.0141 and 0.022 (AT-549, AT-558,
AT-559); this is a FLOAT screen and the actual-source all-rate exclusion remains OPEN. At l = 1.5e-6 the FLOAT
threshold lies between n = 0.022 and 0.03, so at that stipulated input the unchanged-007 FLOAT screen leaves middle
rates unexcluded (theory_v09 V9-4, AT-642); candidate-specific norm bounds and exclusions remain OPEN (AT-641,
AT-643). Coordinator decision of 07:37Z: defer further TII-0 work until the X6 review at 2026-11-03T18:05Z; the
requested point, positive-part integral and residual lower certificates remain queued after the 009 annulus, assembly
and global cover (Section 8). The remaining construction is the J^(-1) energy: for the 008 and 009 sources the far
TII and C_aw terms can be paid at some large rho from the free gain q(c - s_*), provided a certified global bound s_*
< c on the largest strain eigenvalue of the center exists (AT-473, AT-474, AT-476). Certified constants, an
admissible certified radius and a complete H4 price remain OPEN; the gain is at most q (about 2.1) because s = c - 1
at a normalized origin (AT-479, AT-513). The 07:41Z the second theory agent update supplies preliminary complete-009 FLOAT radius
estimates and HEURISTIC HF-1 near prices, for example a log-cut lambda = 8 threshold interpolated at rho about 6.1
for Gbar, with first passing scanned radius 8; at every sampled rate with a budget its model price exceeds the
necessary budget U for every scanned split with A_a <= G, even at G = q (Section 3). These calculations are neither
bounds nor a certified construction exclusion (AT-574, AT-576, AT-617). In the second theory agent's frozen T2_FAR_v01 (08:29:12Z) the
best scanned split under Gbar is log 32 at rho 3, with sampled minima of P_A/U 8.93 and 7.78 at N 0.022 and 0.0141
(AT-616: 8.9314 and 7.7777), and on that fixed finite scan failure at G = q implies failure at every smaller gain
(AT-613, finite-model scope); in the coordinator's reading (HEURISTIC) a sharper strain bound alone therefore cannot
make that scan pass, and the lever is a sharper far upper. The numerical auditor's prepared cover targets s_* <= 3/2, which would
guarantee a gain of at least Gbar, between 0.6516 and 0.6517 (AT-510). Coordinator reading of AT-513, AT-547, AT-548
and AT-553: for a real coefficient with an ordinary integrable Fourier transform and finite second Fourier moment,
whose joint-form upper holds for every real Schwartz test even in x and odd in y, agreement with atil near zero
forces the joint charge to be at least 4[q^2(2c - 1) + 1] > 50 (AT-547, AT-553). It therefore cannot be absorbed
entirely into G <= q. In the planned TII-1 decomposition the near field is priced in the base constant; other
full-energy decompositions are not excluded. The radius at which the far charge fits depends on the certified gain,
which the second theory agent tabulates in its 07:41Z note; the coordinator note of 08:10Z reads a sharper certified far upper of the
complete 009 far form near rho = 1 as the first lever (HEURISTIC). G1, L and B are certification tasks whose FLOAT
values do not contradict the passing levels; in the coordinator's reading the wide-annulus run is the schedule risk
of G1, since its order cap had to be raised (Section 8). G2 remains incompletely certified at every corrected center:
some qualitative domain and regularity components and conditional inverse-transfer rules are proved (RC-1 to RC-3 of
the ledger), while the quantitative and uniform-ball hypotheses are unverified. At 009, Lemma KB and the conditional
bridge (AT-598 to AT-600) reduce G2 to certificates of G1, L, B and G3 at stipulated values (a source upper at most
2.8476e-6, a correction gradient at most 1/4 and a global matrix rate at least 3/5); these premises are not supplied
(AT-602). The gap is therefore not a single inequality with a known margin, and no closure ratio is defined.

## 2. The conditional theorem of the working route

Route Q (the second theory agent's notes/T2_CEPS_v02.md, Theorem HF-Q and its bridge; CONFIRMED in AT-227 to AT-230, AT-234 to AT-238 and
AT-243 under the retained hypotheses), with the CE input (the second theory agent's notes/T2_X4_v01.md, Theorem CE and Corollary
HF-Q-CE; CONFIRMED in AT-272 to AT-275 and AT-283) and the transfer to P-S1 (AT-303 to AT-308).

Setting: weight W = (1 + |X|^2/r0^2)^(sigma/2), N(k) = ||J^q(W k)||_2, a center rho_* = rho_bar + h_* with h_* in the
exact correction class of AT-119 (composites as in AT-174), source F_* of the center, and the ball K(R, M) = {k real
S1 : ell_R3(k) = 0, ||k||_2 <= R, N(k) <= M}, where ell_R3 is the R3 normalization functional of AT-114 (the second theory agent
notes/T2_CEPS_v02.md).

Retained hypotheses of the bridge (the second theory agent's notes/T2_CEPS_v02a.md section 1, as retained in AT-237), for one specified
center and weight: (H1) the actual closed-generator, core, weighted-semigroup and graph-comparison hypotheses of
AT-066, AT-069, AT-114 and AT-178 on a reference ball that contains K(R, M); (H2) the imported L^2 inverse gives z =
-A_k^(-1) F_* with ||z||_2 <= R = ||F_*||_2/beta_0 for every k in K(R, M), and N(z) is finite; (H3) the normalization
conditions (F_* real and in the S1 class, that is even in x and odd in y, F_y(0) = 0, N(F_*) finite, ell(z) = 0
preserved); (H4) the base weak energy at k = 0, Q_0(u) <= -b0 ||g||_2^2 + C0 ||h||_2^2 with b0 > 0 and a finite C0 >=
C^opt(b0); (H5') with the CE input, b = b0 - L_B(R, Kbar(R, M)) > 0, Kbar from Corollary CE-B.

Conclusion: if N(F_*) <= b M - C0 R^2/M, the map k -> z = -A_k^(-1) F_* sends K(R, M) into itself. A stationary
solution then follows by the invariant-ball (Schauder) argument of the re-centered framework, whose continuity and
compactness conditions are among RC-1 to RC-10 (AT-123). H4 asks for an explicit C0, that is an explicit upper bound
of C^opt(b0); this is the deciding item G3.

Ceilings (CONFIRMED, independent of the center): at P-S2 the original test needs N(F) < 0.1451547 (AT-271) and the CE
test N(F) < 0.2160192 (AT-274); at P-S1 the original test needs N(F) < 0.1022925 (c_W = 9619/5000) and the CE test
N(F) < 0.1967903 at every radius and < 0.141102 once R > 1e-7 (AT-304, AT-307, AT-335). These are necessary conditions
for this criterion, not for existence.

## 3. What is proved (the theory auditor CONFIRMED)

Background and framework:
- For Candidate 007, qualitative O1 and restricted Sobolev O2 on the specified small coefficient balls at the cover
  tuples P-BG1 to P-BG3 (AT-056, AT-058, AT-074, AT-097) and at P-BG4 = P-S2 with beta = 3/5 (AT-172, AN-056); full
  Holder-ball O2 and the numerical inverse constants are OPEN. These do not transfer to a corrected center.
- The re-centered framework FW-C2-HqK-RC-v1 as an implication under RC-1 to RC-10 (AT-060, AT-123, AT-183).
- The exact correction class of odd-sine potentials with the origin conditions (AT-119), the exact normalizer (AT-125),
  composite corrections (C - 007) + h_phi (AT-174), the origin cap beta <= c + 1 - q at every normalized center
  (AT-070, AT-123, AT-167).
- Weight constants c_W at P-S1 and P-S2 (AT-135, AT-169, AT-170).
- A seven-field compactified cover theorem for C2-N1-009: containing ranges and passing full-cover predicates imply
  M >= beta I, |grad h| <= g and s_* <= sbar < c (requested tuple q = 21/10, sigma = 1, eta = 1/4, beta = 3/5,
  g = 1/4, sbar = 3/2), CONFIRMED conditionally as a theorem, not a source certificate (AT-508); the application is
  prepared (AT-509); no completed cover (AT-511, OPEN).

Inverse and transport estimates:
- The all-quadratic transport bound L_Q(R, M) with no frequency cutoff and the conditional self-map test (AT-227 to
  AT-229, AT-234), the frozen theorem and bridge (AT-237, AT-243), Theorem CE (AT-272), and the transfers to P-S1
  (AT-303, AT-306).
- The weak-coefficient reduction CB-ZERO (AT-175 to AT-178) and the rate ceiling HF-NEC: a finite weak constant at
  rate b0 needs b0 <= beta of the same background (AT-211).

Exclusions of sufficient criteria (none is a nonexistence statement):
- At the uncorrected center 007 the listed Sobolev criteria fail at their audited tuples: (NT2-F) by a factor of at
  least 9.305, the gradient-only criterion (6) by a factor of at least 33, KP-W absorption because c_1 >= q (AT-063,
  AT-075, AT-080, AT-088, AT-124). The Hoelder route is not excluded; it stays conditional on the OPEN uniform tame
  inverse H1.
- At the two registered b7 centers (C2-N1-006 = C5 + b7, C2-N1-007 = 007 + b7) all five named route-Q tests are
  excluded: the two P-S2 tests (AT-260, AT-287), the two original-input P-S1 tests and the CE P-S1 test (AT-317,
  AT-324, AT-335, AT-352). The cause is the far field: certified whole-plane lowers 28.9924 (P-S2) and 0.231239
  (P-S1) for C5 + b7 and 18.7377 and 0.149564 for 007 + b7 (AT-350, AT-351). Each lies above the level of the test
  it excludes; for the CE P-S1 test at 007 + b7 that level is the envelope 0.141102 valid once R > 1e-7, which the
  certified ||F||_2 lower forces (AT-352), and not the radius-free ceiling 0.1967903.
- H4 constructions: the TII-0 construction is excluded for 0.7091 <= b0 < cap at the stipulated 009 size (AT-408);
  the TII-0/H4-R construction is excluded for 009 and 008 at every cutoff 0 < rho <= 10 when b0 >= 3/5, and at rho <=
  2 for every b0 > 0 (AT-423; the obstruction persists under Lemma OSC pricing, AT-449). These exclude constructions,
  not finiteness of C^opt(b0). For source 009 specifically, with the low-rate necessary levels (AT-501, AT-502), a
  passing CE test through TII-0/H4-R at rho <= 10 needs N_(21/10)(F) < 0.017807475098, and the original-input test <
  0.009256406642, at certified ||F||_2 >= 2.76e-6 and under all full-test hypotheses (AT-503, CONFIRMED
  conditionally); an actual exclusion needs certified lower bounds (AT-504, OPEN). Over every cutoff radius,
  Proposition TII0-RHO (the first theory agent's note 35) gives, under the premises of AT-408, pointwise lowers of the TII-0 price and a
  finite radius-cell rule (AT-549, CONFIRMED conditionally; a particular source needs every coefficient and scalar
  premise); the necessary budget cells and exact-cap budget uppers at l = 2.76e-6 are CONFIRMED for stipulated source
  lowers (AT-550); the saved FLOAT decisions on unchanged 007 reproduce on b0 in [0.25, 0.7103], the actual-source
  exclusion is OPEN (AT-551); and the price lower P bounds only the constructed constant, C_constr >= P, not C^opt
  (AT-552 REFUTES the draft inference C^opt >= P). In the extended screen the 342 necessary budget cells and six
  exact-cap uppers are CONFIRMED conditionally (AT-557); on [0.7103, cap) the origin-only TII-0 price lower exceeds
  3.9e14 and hence U for every N lower n >= 0, and for n >= 0.0075 the source-only scalar test at b0 = 0.15 excludes
  every lower rate (AT-558, CONFIRMED conditionally under the same scalar and construction premises); the 336 saved
  FLOAT decisions on [0.15, 0.7103] reproduce, with worst ratios 0.58363913, 0.78937307, 0.91757666, 1.06883121,
  1.37796633 and 2.26051665 for n = 0, 0.005, 0.0075, 0.01, 0.0141 and 0.022, so no rate stays unexcluded in this
  screen for the last three; the data are FLOAT on unchanged 007, the threshold between 0.0075 and 0.01 belongs to
  the screen and not to the real construction, and the actual-source all-rate exclusion is OPEN (AT-559); the wording
  that no necessary budget exists at n = 0.01 for every b0 < 0.20 is REFUTED (AT-560).

H4 at P-S1 (reductions, not closure):
- The second theory agent's reduction of H4 to the estimates N0, NE-lo, NE-vs, N2 and N3 (T2_H4_v01, CONFIRMED conditionally in AT-361
  to AT-366), the principal and double-commutator identities (AT-332, AT-333), the IMS identity and CAW-0 (AT-420,
  AT-421), the HF-1 bound with C_D = 80127/40000 (AT-427, AT-428) and the three-zone tail (AT-436, AT-437).
- Lemma OSC has the sharp universal constant 1 (AT-451); it stays sharp under arbitrarily small finitely specified
  positive-order moment and derivative budgets when no support bound or positive test-frequency floor is fixed
  (AT-460) and within the S1 symmetry class (AT-464; it gives no 008 or 009 lower bound, AT-465 OPEN); its
  consequence for an actual source is OPEN (AT-452). The high-frequency commutator bound for Q_a (AT-459), the
  homogeneous-limit lemma for the low-frequency supremum (AT-461, conditional on uniform tail convergence) and the
  decay of the TII-0 far oscillation as rho grows for the 008 and 009 sources (AT-462, with accepted
  source-regularity dependencies) are CONFIRMED; a useful numerical rho is OPEN (AT-463).
- J^(-1)-energy route for the far part: Lemma TII-1, Q_a(g) <= lambda_max([[O(1 + nu^2), beta], [beta, beta/4]])
  ||J^(-1) g||_2^2 with O = osc(a), beta = 2(1 + nu^(-2)) M2(a) (AT-473), and |C_aw(a)(g)| <= (q^2/2) M_(2,q-1)(a)
  ||J^(-1) g||_2^2 (AT-474), both CONFIRMED conditionally on their Fourier-moment hypotheses; for the 008 and 009
  sources, with the accepted all-order velocity decay and a fixed C^infinity cutoff scaled with rho, M_t(a_f, rho) =
  O(rho^(-gamma - t)) for each fixed t >= 0, with gamma = 1 - 1/c (this all-moment statement does not apply to P7,
  see below), so the coefficient of TII + C_aw tends to zero and a certified global s_* < c would let some large rho
  pay both terms (AT-476, CONFIRMED qualitatively). A priced inverse or closure from this is OPEN (AT-479); the second theory agent
  far probe used unchanged 007, not 009 (AT-477, REFUTED for 009 provenance), and the C^3 cutoff P7 does not supply
  the all-moment argument (AT-478). For P7 the interface trace condition holds for 007, 008 and 009 (AT-480,
  CONFIRMED); M4 and M_(2,q), q >= 2, of its near and far pieces are infinite, so P7 cannot meet the M4 hypothesis of
  HF-1 (AT-481, REFUTED as finite); for the far piece a_f the weaker M_(2,11/10) is finite with an explicit bound by
  derivative energies and interface jump integrals, and is O(rho^(-gamma-2)) (AT-482, CONFIRMED conditionally; the
  near piece, a localized coefficient, keeps M2 >= 16c at P-S1, AT-403). No numerical far gain or H4 price follows
  (AT-483, OPEN). If the strain target s_* <= 3/2 is certified, the available gain is at least Gbar =
  14674311533937489/22517998136852480, a constant between 0.6516 and 0.6517 (AT-510, CONFIRMED conditionally); with
  Gbar as the conservative budget it suffices that the combined far charge A_far is at most Gbar, and every further
  charge shares G - A_far (AT-513); this is not necessary under a stronger gain certificate. A sufficient C_aw bound
  with the smaller moment weight w_new(d) = H_q(asinh(d/2)) is CONFIRMED as a component lemma (AT-514).
- High-frequency floor of the far forms (the second theory agent draft SC-LB): for an even-even coefficient, or for the even-even
  projection a_e of a general one (the general statement is REFUTED, AT-544), the joint far form needs A >= SC_q(a_e)
  := (1/2) sup_X [(q^2 - 1) lambda_max Hess a_e(X) + tr Hess a_e(X)] for q >= 1, and the Q-only form (1/2) sup_X
  lambda_max Hess a_e(X) under M2 (AT-545, CONFIRMED under the exact ordinary Fourier L1, moment and test-space
  hypotheses; AT-546 repairs the remainder argument). At P-S1 (q = 21/10), for coefficients agreeing with atil near
  zero, the joint origin floor is 4[q^2(2c - 1) + 1], in (50.228061735855931, 50.228061735855933), against the HF-1
  formula floor in (56.710615417455916, 56.710615417455918) (AT-547). A valid even-even far charge bounded by G needs
  SC_q(a_f) <= G; only this necessary implication is CONFIRMED (AT-548). With ordinary Fourier L1 and M2 alone on the
  actual real S1 test space the joint lower A >= (1/2) sup_X [(q^2 - 1) lambda_max Hess a_e(X) + Delta a_e(X)] is
  CONFIRMED, so no higher Fourier moment is needed for this necessary bound (AT-553); finite-band FLOAT eigenvalues
  are not certified lower bounds of the continuum constant (AT-554, OPEN).
- Mellin-angular analysis of the far form (the first theory agent): the multipliers and the degree-zero direct-integral formula are
  CONFIRMED (AT-487); at tau = 0 the top fiber value is 1/sqrt(2) for cos(theta) and 1 for cos(k theta), for each
  integer k >= 2, whole-plane lower bounds (AT-488); the compression-based continuum bound of the sampled log-radius
  spectrum is REFUTED (AT-489); a source-009 far-form upper is OPEN (AT-490).

Far field:
- Lemma TAIL and the weighted tail law of a sector r^a A(theta) + E under remainder hypotheses (AT-290, AT-295), the
  sector budget rule (AT-311, sufficient, not necessary, AT-339), leading far-field cancellation in the enlarged class
  (AT-276, AT-277), the whole-plane assembly theorem (AT-319) and its method for 009 (AT-397 to AT-399).

Necessary levels and budgets at the size of the lead center (scalar statements under the retained full-test
hypotheses):
- With a certified lower l = 2.76e-6 of ||F||_2 and 0 < beta_0 <= c + 1, a passing CE test at P-S1 needs N(F) below
  0.096618, 0.113565, 0.131893 and 0.135848 at b0 = 0.60, 0.65, 0.70 and the cap (AT-382); the original-input test
  at P-S1 needs N(F) below 0.050223, 0.059032, 0.068559 and 0.070615; at P-S2 the CE levels are 0.10369 to 0.145749
  and the original-input levels 0.069675 to 0.097937 (AT-390).
- H4 budgets at P-S1, at the stipulated triple (||F||_2, beta_0, N(F)) = (2.76e-6, 209/100, 0.0152): C^opt(b0) <= D =
  1.59e10, 2.11e10, 2.71e10 and 2.85e10 (b0 = 0.60, 0.65, 0.70 and 0.7103) is sufficient with the other retained
  hypotheses (AT-383); C^opt(b0) < U = 1.75e10, 2.3e10, 2.95e10 and 3.09e10 (b0 = 0.60, 0.65, 0.70 and the cap) is
  necessary (AT-395). Their use at 009 needs compatible certified inputs or a new calculation; the stipulated N(F) =
  0.0152 lies below the FLOAT whole-plane value 0.02192 (Section 5). The first theory agent's Arb budgets at hypothetical N_(21/10)
  inputs (note 35, 07:25Z; CE, l = 2.76e-6, beta_0 = 209/100): D lowers 1.62e10, 2.13e10, 2.74e10 and 2.88e10 at N
  0.0141 and 1.44e10, 1.94e10, 2.52e10 and 2.66e10 at N 0.022 for the same four rates; all 48 sufficient cells are
  CONFIRMED at their exact inputs l = 2.76e-6 or 2.8476e-6 (AT-563), and the 24 necessary U uppers at l = 2.76e-6
  (beta_0 = c + 1 and 209/100) are CONFIRMED, with printed CE D/U in the 209/100 block between 0.9056603773 and
  0.9201277956, the last ratio comparing D(0.7103) with U(cap) (AT-564). The rounded header 2.85e-6 is not a valid
  exact input for the printed witnesses (AT-565, REFUTED; the source used was 2.8476e-6; the reused witnesses lose 13
  printed D and five Z inequalities, replacement pairs are recorded, and different witnesses are not excluded), and
  the printed N 0.0152 lowers exceed the N 0.022 lowers by 10.42, 8.76, 7.54 and 7.14 percent, not by 7 to 9 percent
  (AT-566, REFUTED). These remain budgets at stipulated inputs: D needs certified forcing and N_q uppers, U certified
  lowers (AT-567, OPEN). The budgets use hypothetical N_(21/10) inputs 0.0141 and 0.022. The former is motivated by
  the observed FLOAT N_2, not an observed N_(21/10); the latter approximates the FLOAT N_(21/10) 0.02192. The
  sufficient witnesses require certified forcing and N_(21/10) uppers before application to 009. The first theory agent's later tables
  009o and 009p (research files, no note yet) add beta_0 = 187/100 and 7/4 at the forcing inputs 2.8476e-6 and
  1.52e-6: all 136 positive cells are CONFIRMED conditionally (AT-591), the literal 2.85e-6 reading is REFUTED
  (AT-593), and the recentering formula transfers a stipulated base inverse lower beta_base > 2.00215453 to beta_* >
  1.87 with a correction gradient g_* <= 0.128 and to beta_* > 7/4 with g_* <= 1/4 (AT-592, conditional arithmetic;
  the gradient premises OPEN). The displayed 011 sizes lie below the FLOAT observations and are not certified, and no
  invariant ball follows (AT-594, OPEN). The first theory agent's table 012a at the stipulated forcing input 1.4114e-6 (an upward
  rounding of the first numerics agent's FLOAT mesh value 1.41127e-6), beta_0 = 187/100 and 7/4 and N 0.0099, 0.0155 and 0.022 has 68
  positive D and Z cells CONFIRMED at stipulated inputs, while four unsuccessful searches are not exclusions
  (AT-606); the header rounding, the conditional rate transfers (a certified g_* <= 0.13215453 suffices for beta_* >
  187/100 and g_* <= 1/4 for beta_* > 1.75215453 > 7/4) and the fit of every trial ball in the KB ball are CONFIRMED
  in conditional form (AT-607). The X5 necessary-level tables at l = 1.3e-6 and 1.5e-6, the U tables at the
  stipulated N lower 0.0161 and the D tables at the stipulated N upper 0.0161 and forcing uppers 1.5e-6 to 2.76e-6 (D
  is nonincreasing in N, so these D rows apply at any certified N(F_*) <= 0.0161, theory_v09 V9-3 (b)) and the tables
  012b (beta_0 = 93/50, permitted by a certified g_* <= 0.14215453) and 012c (beta_0 = 7/4 at 1.5216e-6) have 216
  positive D and Z cells, 36 U uppers and 36 necessary levels CONFIRMED at stipulated inputs (AT-628 to AT-630,
  AT-633); the literal 2.85e-6 header reading of 012b is REFUTED (AT-631), and an exact equivalence between passing
  the test and a printed Z cutoff in the evolving theory_v09 item V9-3(d) is REFUTED, the sufficient form remaining
  valid (AT-632). None of these tables supplies an actual source bound, inverse or fixed point (AT-608, AT-634,
  OPEN). theory_v09 (frozen 08:52:58Z) integrates them: the integration is CONFIRMED within its scope (AT-644); its
  literal auxiliary graph-radius upper 0.497 is REFUTED (the exact maximum is 0.49729448368455, below 0.498; every
  trial radius is at most 0.495, so the reference-ball containment is unchanged, AT-645); no completed G1, global
  cover or H4 coefficient appears in it (AT-647, OPEN). Its rate reading (V9-3 (a), by the RC-3 rule beta_0* = beta_0
  - g_* with the certified beta_0 > 2.00215453): 209/100 is not available; under the retained RC-3 hypotheses a
    certified g_* <= 0.13215453 suffices for beta_0* > 187/100 (the sampled FLOAT g_* of 0.1356 to 0.1385 lies above
    that threshold), g_* <= 0.14215453 suffices for beta_0* > 93/50 and g_* <= 1/4 for beta_0* > 7/4; D at 93/50 is
    about 1.13 times D at 7/4. Its necessary budgets at l = 1.5e-6 (budnec_tii0d
  and budnec_tii0e, 342 cells) are CONFIRMED conditionally (AT-640; no actual source bound, AT-641, OPEN).
- The second theory agent's FLOAT far charges and HEURISTIC HF-1 near prices for the complete 009 coefficient (notes 07:41Z; files in
  theory_agent_2/research/h4/far009/runs; budgets of the first theory agent's note 35 at l = 2.76e-6; nothing is a bound). The far charge A_a
  (Lemma TII-1 with Lemma CAW-F) meets Gbar at log-log interpolated radii between 4.01 (log cut, lambda 16) and 18.7
  (linear cut, lambda 2), first passing scanned radii 6 and 20, and meets G = q at 1.85, 2.78 and 3.23 (log 16, log
  8, linear 4; first passing scanned radii 2, 3 and 4). The 07:41Z interim figures at the linear-4, rho-8 split (P_A
  = 26.9 D at b0 0.60; minimum P_A/U 12.8 and 11.1 at Gbar) are superseded (the second theory agent 08:30Z). In the frozen T2_FAR_v01
  (08:29:12Z, 829 lines, SHA256 8c37f0d7...) the best scanned split with A_a <= Gbar is log 32 at rho 3, with P_A =
  18.8 D at b0 0.60 and minimum P_A/U over the sampled rates b0 = 0.25, 0.30, ..., 0.70 of 8.93 at N 0.022 and 7.78
  at N 0.0141, at b0 0.55; at G = q the minima are 2.69 and 2.34; every sampled rate with a budget has model price
  above U. AT-574 confirmed 8.9279031753 and 7.7747156819 in the frozen 07:47:23Z snapshot, and the replay of the
  updated tables (N4096 substitutions) gives 8.931362205028748 and 7.777727920212534 at Gbar and 2.6895511726 and
  2.3421508128 at G = q (AT-615, AT-616, CONFIRMED in the finite FLOAT/HEURISTIC scope). The log-64 split at rho 2
  fits under Gbar with the N2048 far box (A_a 0.635) but not with N4096 (0.661). For log 16, Table F4 gives log-log
  interpolated FLOAT threshold radii of about 4.02, 2.92, 2.25, 1.9 and 1.85 for G = Gbar, 1, 1.5, 2 and q
  (interpolated thresholds, not evaluated passing radii; for Gbar the first passing scanned radius is 6, the theory auditor
  research/far_scaling_audit), and Table F9 the HEURISTIC minimum model P_A/U at those interpolated thresholds as
  7.89, 4.82, 3.23, 2.49 and 2.39 at N 0.022 (6.87, 4.19, 2.81, 2.17 and 2.08 at N 0.0141); the derivative-energy
  route makes these radii 19 to 60 percent larger. In the files rerun at 08:12Z the log-32 and log-64 far charges
  meet Gbar at interpolated radii 2.81 and 2.02 and G = q at 1.31 and 0.966 (table F4). At rho = 1 (log 8) the near
  price is about D (1.1 D at N 0.022 and 0.979 D at N 0.0141, b0 = 0.60) while A_a = 19.4 against the FLOAT floor
  SC(a_f) 0.968 of the complete 009 far piece; over the scanned rows and sampled rates the smallest far charges with
  a near price within D are 23.1 q and 9.22 q, and within U 3.46 q and 3.19 q, at N 0.022 and 0.0141 (the second theory agent table F8
  of the 08:12Z files; its interpolated crossings lie lower). The sampled near Hessian maxima lie below the exact
  floor 8(2c - 1), so they are not certified uppers (AT-575, CONFIRMED under the accepted normalization and
  near-cutoff hypotheses). The screen excludes neither the construction at every real rate nor the optimized operator
  constant (AT-576, OPEN). On a fixed finite scan with gain-independent prices and budgets, failure at G = q implies
  failure at every G <= q (AT-613, CONFIRMED in the stated finite-model scope). Table F10 states targets for a
  sharper far upper (FLOAT SC(a_f); HEURISTIC rho_U, the radius at which the model near price meets U at the best
  sampled rate): at rho_U = 1.51, 1.07 and 0.73 for log 8, 16 and 32 (1.64, 1.17 and 0.80 at N 0.0141), SC(a_f) =
  0.445, 0.367 and 0.386 (0.371, 0.308 and 0.326); the FLOAT target factors are Gbar/SC(a_f) = 1.46, 1.78 and 1.69
  and q/SC(a_f) = 4.72, 5.73 and 5.45 at N 0.022 (1.76, 2.12 and 2.0, and 5.66, 6.82 and 6.43 at N 0.0141), so in
  this FLOAT comparison a far upper fits under Gbar there if it lies within the Gbar/SC factors of SC(a_f), and under
  q if it lies within the q/SC factors, while Lemmas TII-1 and CAW-F give model factors A_a/SC(a_f) of 16 to 19 on
  these rows (the log-4 row at N 0.0141 has Gbar/SC 1.03 and the log-64 row A_a/SC 20.3); in strain terms a far upper
  of k SC(a_f) at log 8, rho 1.51 needs sbar <= c - 0.445k/q, 1.598 for k = 1 and 1.386 for k = 2. The coordinator's
  08:10Z figure s_* <= 1.349 is for log 8 at rho 1, below rho_U; there the model near price is P_A = 1.10 D and P_B =
  2.11 D at N 0.022 (0.98 D and 1.87 D at N 0.0141), b0 0.60. At that split the FLOAT floor SC(a_f) = 0.968 exceeds
  Gbar, so no far upper fits under Gbar there, and at G = q a far upper must lie within a factor 2.17 of the floor
  (theory_v09 V9-10, FLOAT reading). The theory auditor's review of the second theory agent's evolving draft CONFIRMS a perturbation theorem for the
  difference d = a_f,009 - a_f,007 (ordinary integrable Fourier transform, finite moments, common test domain): the
  change of a common test-space far-form supremum is at most the infimum over nu > 0 of lambda_max [[O_d (1 + nu^2),
  beta_d], [beta_d, beta_d/4]] + (q^2/2) Mnew(d), with O_d = ess sup d - ess inf d and beta_d = 2(1 + nu^(-2)) M2(d)
  (AT-609). It REFUTES three inferences of the draft: relative accuracy of the 007 band value for 009 from small
  relative changes of separate oscillations and moments (AT-610), exclusion under Gbar by the low-block oscillation
  floor alone (AT-611; five of the eight printed floors leave positive model room) and the direction of the continuum
  error from two resolution values (AT-612); no source-009 transfer accuracy or exclusion is certified (AT-614,
  OPEN). The nested band suprema A_K converge to the full far-form supremum A_* (AT-621, CONFIRMED), but the
  band-limited best constants need not converge to SC(a): for sufficiently large dilation A_* > SC(a), so the general
  identification in section 5.6 of T2_FAR_v01 is REFUTED (AT-622), and no source-009 equality, gap or upper follows
  from the periodic band calculations (AT-623, OPEN). The far and near scaling readings hold under their stated
  hypotheses (AT-625, CONFIRMED); on the frozen log-16 data the local near price varies roughly as 1/G (inverse-gain
  product spread 6.7343 percent, endpoint exponent 1.02151; AT-626, finite FLOAT/HEURISTIC statements CONFIRMED); the
  sufficient rule (FG1) holds when the explicit TII-1 + CAW scalar charge built from certified complete far inputs
  and a certified global strain bound fits the certified gain (AT-624, CONFIRMED), and rounded or interpolated FLOAT
  values alone do not meet it (AT-627, OPEN).

## 4. What is certified numerically (the numerical auditor CONFIRMED, audited by the theory auditor where stated)

| center | ||F||_2 | weighted source norm | background | structure |
|---|---|---|---|---|
| 007 (reference) | in (0.37668932470589, 0.37668932470590) (AN-005) | P-S2 whole plane in (261.62, 285.56) (AN-059, AT-188); P-S1 > 9.699 (AN-033) | beta >= 3/5 at P-BG3 and P-BG4 (AN-036, AN-056); P-S2 infimum in [3/5, 0.6588410) (AN-068, AT-199) | AN-001 |
| C2-N1-003 (existing basis) | in (0.110743313086205, 0.110743313086206) (AN-054) | P-S2 whole plane in (200.26, 216.88) (AN-060) | not certified | AN-053 |
| C2-N1-006 (C5 + b7) | > 7.65e-7 (AT-351) | lowers 28.9924 (P-S2), 0.231239 (P-S1) | finite axis points above the cap (AN-092, AT-326) | AN-076, AT-245 |
| C2-N1-007 (007 + b7) | > 4.90e-7 (AT-351) | lowers 18.7377 (P-S2), 0.149564 (P-S1) | finite axis points above the cap (AN-092, AT-326) | AN085, AT-270 |
| C2-N1-009 (007 + b14s) | not certified | complete zeroth exterior norm beyond r = 1e4: P-S1 in (0.00067824438670, 0.00067862501582), P-S2 in (0.017286029316, 0.017293688771) (OBS-009-TAIL-001; AT-430, AT-431); complete P-S1 exterior derivative energies through order 3: for L_m = (sum_(j=0)^m binom(m,j) I_j)^(1/2), with I_j the squared order-j derivative tensor integral of W F_* over r >= 1e4, uppers 0.00067862501582, 0.00849360179196, 0.01199581272757 and 0.01468793288946 for m = 0 to 3, all lowers above 0.00067824438670 (OBS-009-EXTERIOR-OPERATOR-001; AT-495 to AT-499); complete origin disk bounds on |X| <= 1/50 through order 3, at P-S1 strict uppers of E_m^(1/2) 2.954172025375e-8, 4.448704891769e-6, 0.0006012991509633 and 0.1222414201696 for m = 0 to 3, with E_m = sum_(j=0)^m binom(m,j) ||D^j(W F_*)||^2 on the disk (OBS-009-ORIGIN-PS1-APPLICATION-001, OBS-009-ORIGIN-001 for both weights; AT-529, AT-530; P-S2 disk endpoints AT-537, publication AT-538; the m = 3 local lower is not an H^(21/10) lower); certified complete-circle rms values of F_* at finite radii (OBS-009-CIRCLE-001; AT-411, AT-412) | ten eigenvalue intervals (five exact points, both weights) above the cap (OBS-009-BACKGROUND-001; AT-443 with field-evaluation dependencies) | exact structure, normalization and origin cap (OBS-009-STRUCTURE-001; AT-386, AT-387) |

The P-S2 tail of 009 beyond 1e4 alone is 0.0173, so a P-S2 tail target of 0.01 at that radius is REFUTED for this
source (AT-430, AT-431). The same lower endpoints are whole-plane lowers of the weighted L^2 and H^(21/10) norms of
009 (AT-431). No whole-plane upper of a weighted source norm is certified for either b14s center (008, 009), and no
global background gap is certified for any corrected center; C2-N1-003 has a certified P-S2 whole-plane interval
(AN-060, AT-189).

Accuracy finding: the numerical auditor OBS-007-ORIGIN-POINTS-001 (audit_v99; CONFIRMED by the theory auditor in AT-453, AT-454) shows that
the second numerics agent's frozen base evaluator has large derivative errors near the origin (the mixed (2,1) derivative at radius 0.001
is 314.73 against an exact value of about 3.87e-6; 12 order-2 and 32 order-3 errors above 1/10000 at eight points).
The second numerics agent's disk N_3 terms of 007 and 009 below r = 0.02 are therefore unreliable; the integrated effect is OPEN
(AT-455). The follow-up OBS-007-CONDITIONING-001 (audit_v102) shows that two specified exact input roundings change
each derivative by less than 1/10^11 (AT-469), that one frozen radial-derivative contraction has condition ratio
above 10^16 (AT-470), and that three recorded producer interventions do not repair the point (AT-471); it gives no
operation-error bound or integrated correction (AT-472, OPEN). The second numerics agent's repaired FLOAT origin disk of 009 (base Taylor
route on 0.001 <= r <= 0.02) agrees with the numerical auditor's certified closed-disk values to ratios 0.9954475963 to 0.9976487870
at every order and both weights (the second numerics agent 08:30Z); the numerical auditor CONFIRMS the ratios as finite arithmetic, over different
domains, and leaves the attribution of the deficit to the omitted disk and the quadrature OPEN
(OBS-UPDATED-STRONG-ACCOUNTING-001, audit_v129). The numerical auditor's consolidated snapshot of its audit at this checkpoint is
numerical_audit/reports/MID_CAMPAIGN_AUDIT_v01.md (08:35:11Z); later dated entries of its AUDIT_LEDGER govern.

## 5. Numerical progress (FLOAT unless labelled)

||F||_2 of the center, in the order the teams reached it: 007 0.3767 (certified) -> C2-N1-003 0.1107 (certified;
existing basis) -> C2-N2-001 and C5 about 0.025 (expanded basis) -> grid corrections 8e-7 (grid functions, not
admissible centers) -> exact b7 corrections 1.36e-5 (C5 + b7) and 1.25e-5 (007 + b7) -> exact far-field-first fits
1.40e-5 (C5 + b14s, C2-N1-008) and 2.84e-6 to 2.86e-6 (007 + b14s, C2-N1-009).

The b7 corrections lowered the FLOAT ||F||_2 by factors of about 1.85e3 (C5 + b7) and 3.01e4 (007 + b7) but left
far-field sectors that the certified annulus lowers expose; the far-field-first fits impose the far classes as
budget-weighted rows before the near field. For 009:
- P-S1: whole-plane N_(21/10) 0.02192 and N_2 0.01411 by per-mode Hankel transforms of the analytic derivative
  fields (the second numerics agent 06:33Z; range 1e-3 <= r <= 1e4 plus the zeroth-order exterior tail, finite far model beyond r = 300,
  no error enclosure or remainder bound; the polar N_2 agrees). The earlier FFT-box values (0.0105 at cutoff 80)
  are superseded: the second numerics agent reports float noise of 5 to 40 percent in sampled values of F_* (a five-order cancellation),
  which makes Fourier norms of sampled values unreliable beyond |k| of about 200 to 300. The 05:36Z finite-box
  estimate 0.022 and the interpolation diagnostic 0.0234 are consistent with the new value; none is a bound.
- P-S2: whole-plane N_(21/10) 0.06220 and N_2 0.06031 by the same method (the second numerics agent 06:51Z, final; 06:33Z gave 0.06222);
  polar N_2 0.05775 on 0.02 <= r <= 1e4; the first numerics agent's mesh value 0.0852 is withdrawn as base-evaluation noise beyond r of
  about 3000 (the first numerics agent 05:59Z, erratum E26); on the repaired background the first numerics agent finds ||F_*||_2 2.8476e-6 and N_2 0.01408
  / 0.05779, in agreement with the second numerics agent (the first numerics agent 06:38Z).
- Background: sampled BG-6 minimum at the origin cap c + 1 - q = 0.71032 at both tuples, interior minima 0.71744
  (P-S1) and 0.71102 (P-S2) (the second numerics agent 04:49Z).
- Error budget (the second numerics agent 07:05Z and 07:18Z): a producer estimate that combines measured comparisons (frequency cutoff,
  interfaces, tails, field accuracy, far model) with a heuristic omitted-disk allowance. The completed doubled-radial-
  resolution run changes the P-S1 value from 0.021918 to 0.021920 (about 1e-4 relative; P-S2 0.062200 to 0.062201).
  The second numerics agent puts the total at a few 1e-4 relative. This is not an enclosure.
- Strain (the second numerics agent 07:05Z; grid values, not a bound): the sampled maximum of s = lambda_max Sym D ubar is 0.8103188519
  at r = 1e-3; the origin value is s(0) = c - 1 by the second numerics agent's normalization identity; sampled angular maxima decrease
  with r (0.38594 at the inner edge of the band [8, 16), 0.10108 at [300, 1e3)). The second numerics agent reads the supremum as c - 1,
  reached only at the origin; this is not certified.
- New candidate C2-N1-010 (007 plus a D8 correction; the first numerics agent 07:05Z; FLOAT on the regional mesh 0.02 <= r <= 1e4):
  ||F_*||_2 1.8772e-6, N_2 0.01333 at P-S1 and 0.02725 at P-S2. The second numerics agent's whole-plane FLOAT values (07:37Z, the
  method used for 009): N_(21/10) 0.021637 at P-S1 against 0.021918 for 009 (1.3 percent lower) and 0.032903 at P-S2
  against 0.062200; at P-S1 E_0 falls from 3.11e-5 to 3.20e-6 while E_2 rises from 1.673e-4 to 1.764e-4; the plain
  E_2 values are 34.8 and 37.7 percent of N_(21/10)^2 for 009 and 010 (the second numerics agent's 07:39Z 95 percent does not describe
  the plain E_2; see below), and its radial breakdown places most of this energy on 0.1 <= r <= 0.7; the sampled band
  maxima of the strain coincide with those of 009 to the printed digits for r >= 0.1. The numerical auditor
  (OBS-FRACTIONAL-COMPONENT-LABELS-001, 08:16:03Z) REFUTES the reading of the second numerics agent's 93 to 95 percent (07:39Z, 07:51Z)
  as plain-E_2 shares and CONFIRMS, as finite ratios of the saved FLOAT records, plain-E_2 shares of 34.8, 37.7 and
  37.3 percent and shares of the fractional-weight second-derivative part J_2 (binomial weights 1, 2, 1) of 93.4,
  99.2 and 98.7 percent of N_(21/10)^2 for 009, 010 and 011 at P-S1; no continuum norm is certified. A Cartesian FFT
  gives FLOAT fractional-energy FFT/Hankel ratios 0.99930 and 0.99649 at P-S1 (0.99891 and 0.99501 at P-S2) for 009
  and 011 (finite arithmetic CONFIRMED); the second numerics agent's attribution of the discrepancies to box truncation remains HEURISTIC
  (OPEN, the numerical auditor OBS-FRACTIONAL-FFT-ACCOUNTING-001). The second numerics agent (08:28Z) states that its percentages were shares of the
  weighted second-derivative part E_2^(1/10), defined with the same binomial weights: 93.4 percent for 009 and 98.7
  percent for 011, as in the numerical auditor's records, but 95 percent (4.44e-4) for 010 against the numerical auditor's 99.2 percent; that
  difference is not yet reconciled. 009 stays the reference until X5 (Section 7). With the same evaluator and Hankel
  route, the second numerics agent's FLOAT whole-plane values for 007 + b7 (0.663 at P-S1, 97.1 at P-S2) lie above the certified lowers
  0.149564 and 18.7377 of AT-351.
- New candidate C2-N1-011 (the first numerics agent 07:25Z; two more damped SVD steps from the 010 coefficients; snapshot MANIFEST
  16e84e55...; FLOAT on the same mesh): ||F_*||_2 1.52e-6, N_2 0.00992 at P-S1 and 0.02571 at P-S2. The first numerics agent proposes it
  for certification; it replaces 010 as the candidate reviewed at X5 (Section 7). The second numerics agent's whole-plane FLOAT values
  (07:51Z, same method as for 009): ||F_*||_2 1.5435e-6 on 0.02 <= r <= 1e4; N_(21/10) 0.016107 at P-S1, 27 percent
  below 0.021918 for 009, and 0.029769 at P-S2 against 0.062200; N_2 0.010010 / 0.027440 and N_3 1.599 / 1.514; the
  zeroth-order tail beyond 1e4 at P-S2 9.59e-3 against 1.729e-2 for 009 (finite far model); E_2 at P-S1 falls from
  1.673e-4 to 9.68e-5, about 37.3 percent of the printed N_(21/10)^2 (the second numerics agent states 93 percent); the sampled strain
  band maxima are those of 009 and 010. In the second numerics agent's 07:54Z reading the continuation steps roughly halve the near-field
  second-derivative content except on 0.1 <= r <= 0.2 and in the modes 17 to 31 (it rises beyond r = 3, by small
  absolute amounts). The FLOAT ||F_*||_2 of 011 lies below 2.76e-6, so these observations do not justify the forcing
  lower l = 2.76e-6 of the necessary levels and U for 011 (they certify neither direction); a sufficient D with a
  forcing upper 2.76e-6 stays usable if that upper is certified. AT-522 confirms less than 5 percent variation of the
  necessary levels at b0 = 0.60, 0.65, 0.70 and c + 1 - q between l = 1e-6 and 1e-5.
- New candidate C2-N1-012 (the first numerics agent 08:08Z, numerics_v05; D8 plus near-field P-S1 Sobolev rows on r <= 1; FLOAT on the
  fixed mesh ||F_*||_2 1.4113e-6, N_2 0.00602 at P-S1 and 0.02163 at P-S2). The second numerics agent's whole-plane FLOAT values (08:20Z,
  same method as for 009, no enclosure): ||F_*||_2 1.4294e-6 on 0.02 <= r <= 1e4; N_(21/10) 0.009516 at P-S1 (41
  percent below 011 and 57 percent below 009) and 0.024271 at P-S2; N_2 0.006152 / 0.023365; N_(11/5) 0.015084 /
  0.026501; N_3 0.8266 / 0.7780; zeroth-order tail beyond 1e4 3.81e-4 / 8.81e-3; E_2 at P-S1 3.53e-5 (011: 9.68e-5);
  sampled strain maximum 0.8103188 at r = 1e-3, band maxima as for 009; sampled sup |grad h| 0.1378 and sup |DU[h]|
  0.0953, unchanged from 010 and 011. In the second numerics agent's 08:32Z localization 50, 75 and 90 percent of the remaining P-S1 E_2
  of 012 lie inside r = 0.43, 1.66 and 4.26, and the band 1 <= r <= 8, outside the Sobolev rows, carries 31 percent;
  the second numerics agent suggests extending the rows to r <= 4 with weight on the modes n <= 7. Coordinator reading (HEURISTIC):
  the second numerics agent's FLOAT ||F_*||_2 1.4294e-6 exceeds the stipulated forcing input 1.4114e-6 of table 012a and of the 1.4114e-6
  rows of 012b, so those allowances would not apply at a certified upper near the second numerics agent value, while the forcing
  upper 1.5e-6 of the X5 D rows lies above both FLOAT values (theory_v09 V9-9); the FLOAT correction gradient
  (0.13556 on the first numerics agent's mesh, as cited in budget_012a, 0.1378 in the second numerics agent's evaluation, and 0.138453 after the first numerics agent's local
  refinement near r = 0.69 at about 78 degrees, the same for 012 and 013, the first numerics agent 09:04Z; an exact sampled maximum
  would be a lower bound of the supremum; these FLOAT evaluations are not certified bounds) lies above the threshold
  0.13215453 sufficient for 187/100 and below the thresholds 0.14215453 and 1/4 sufficient for 93/50 and 7/4, with a
  FLOAT margin of about 0.0037 to 0.14215453; at 012's size the TII0-RHO screen leaves middle rates unexcluded
  (theory_v09 V9-4). The first numerics agent published the exact far table of 012 as SUPPLEMENT-01 (08:48Z) and snapshotted its
  continuation b18s2 as C2-N1-013-phi-007-sector-d8-leg24-lat-nf2 (08:55Z, MANIFEST SHA256 615f09c5...): fixed-mesh
  FLOAT ||F_*||_2 9.54e-7, N_2 0.0035 at P-S1 and 0.0183 at P-S2 (MID 32 x 256), P-S1 E_2 1.05e-5, a_0* 10.297367
  (cap PASS; the numerical auditor CONFIRMS 013's exact normalization, forbidden sectors and origin cap, cap margin about 6.894, and
  its nonzero leading residual circle norm about 1.638e-4, OBS-013-STRUCTURE-001, and the theory auditor CONFIRMS the structural
  applications of 012 and 013, AT-674 to AT-676; the same structure checks pass for 010, 011 and 012,
  OBS-010-STRUCTURE-001 to OBS-012-STRUCTURE-001; full residual, background and closure OPEN, AT-677); the first numerics agent states
  that 013 supersedes 012 on every FLOAT metric it reports and that the numerical auditor decides the chain (the first numerics agent 08:57Z). An N_2
  value does not bound N_(21/10) from above (N_2 <= N_q for q > 2, the theory auditor research/source012_budget_audit), so the second numerics agent
  evaluated 013 on the whole plane (09:12Z; same method as for 009 to 012, FLOAT, no enclosure): ||F_*||_2 9.949e-7
  on 0.02 <= r <= 1e4 (4 percent above the first numerics agent's mesh value; the second numerics agent reads its polar value as the better one, the
  near-field structure of 013 being finer than the MID 32 mesh); N_(21/10) 0.005404 at P-S1 (43 percent below 012 and
  a factor 4.1 below 009) and 0.020217 at P-S2; N_2 0.003702 / 0.019917; N_3 0.3677 / 0.3415; zeroth-order tail
  beyond 1e4 3.39e-4 / 7.86e-3; P-S1 E_2 1.18e-5; at P-S2 the zeroth-order far field beyond r = 300 carries 97
  percent of N_(21/10)^2. Its Hoelder strong norm S_F at P-H is about 0.00665 (sampled) to 0.0081 (interpolated),
  half of 012's. The strain map and the gradient maximum are unchanged: the grid maximum of |grad h| is the same to
  five digits for the 007 corrections 009 to 013 (the second numerics agent 09:07Z, 09:12Z), the first numerics agent's nested refinement converges to
  0.138453 (09:10Z), and the numerical auditor reads the same local patch maximum 0.13845 for 009 as a FLOAT observation
  (audit_v136). The first theory agent's HEURISTIC permitted size at G = q, from the model prices of the 009 coefficient, is about
  9.6e-7 (theory_v09 V9-3 (d)); 013's polar value lies about 4 percent above it, and its FLOAT P-S1 N_(21/10) lies
  well below the N upper 0.0161 of the X5 D tables.
- Hoelder strong norm S_F at P-H = (1/2, 2/5, 7/4) (the second numerics agent 08:28Z; FLOAT sampled sums and interpolation values from
  grid maxima): 007 110.7 / 157.2 (certified lower 112.785, AN-012), 009 0.03173 / 0.03643, 011 0.02323 / 0.02782,
  012 0.01155 / 0.01388. The numerical auditor CONFIRMS the arithmetic of the twenty updated records as finite arithmetic
  (OBS-STRONG-SAMPLING-ACCOUNTING-001, audit_v127; OBS-UPDATED-STRONG-ACCOUNTING-001, audit_v129): neither value is a
  bound, a rigorous sampled lower must subtract the node errors, and an interpolation upper needs global derivative
  uppers rather than grid maxima. The ratio m = sqrt((1 + r^2)/(1 + 4r^2)) has ordered derivative bounds 1, 3/5, 17/4
  and 20 through order 3 (AT-618, CONFIRMED), so complete P-S1 energies through order 3 give a unit-radius C^(1,beta)
  strong upper for 0 < beta < 1 (AT-619, CONFIRMED conditionally; the numerical auditor OBS-PS1-UNIT-WEIGHT-METHOD-001); it gives no
  bound at sigma = 7/4 and no source-specific value before the energies exist (AT-620, OPEN). Its rational
  application and code are CONFIRMED conditionally on complete P-S1 energy uppers (AT-635, AT-636; the numerical auditor
  OBS-UNIT-STRONG-ARITHMETIC-001, OBS-UNIT-STRONG-REVIEW-BINDING-001), and the actual 009 application records are
  absent (AT-637, OPEN). At doubled radial resolution the second numerics agent's FLOAT S_F interpolation sums for 012 change by +0.39,
  +1.06 and +0.15 percent (the second numerics agent 08:50Z; the numerical auditor audit_v138). The numerical auditor REFUTES the second numerics agent's claim that grid maxima can only
  increase under this refinement (the 1541- and 3084-point log grids share only their endpoints) and its regional
  partition of the saved 012 values (the saved inner norm on 0.001 <= r <= 0.02 exceeds the total by factors 46.2 and
  46.9, a mask defect that does not affect the overall L2, E_j and N_k values), and labels the second numerics agent's local quadratic
  fit a diagonal estimate (OBS-REFINED-SAMPLING-001; finite arithmetic CONFIRMED, exact-field norms and gradient
  extrema OPEN).

Reading (HEURISTIC). The CONFIRMED necessary CE levels at P-S1 (0.096618 to 0.135848) are 4.4 to 6.2 times the FLOAT
value 0.02192 and the original-input levels (0.050223 to 0.070615) 2.3 to 3.2 times it; at P-S2 the CE levels
(0.10369 to 0.145749) are 1.67 to 2.34 times 0.06220 and the original-input levels (0.069675 to 0.097937) 1.12 to 1.57
times it. theory_v08, written before the Hankel values, quotes 2.1 to 6.2 at P-S1. A necessary level that is not
violated is not a passing sufficient test (AT-382), and the values compared are FLOAT without an enclosure. For
C5 + b14s (008) the FLOAT P-S1 value 0.1426 (the second numerics agent 06:33Z) lies above 0.131231, the level that AT-368 makes necessary
for a passing CE P-S1 test at certified ||F||_2 >= 1.4e-5, while its FLOAT ||F||_2 is 1.4002e-5. This FLOAT screen,
not a certified exclusion, is why 009 is the only lead and 008 gets no further certification effort.

## 6. What failed or was withdrawn through the report cutoff

- Uncorrected-center routes: the listed Sobolev criteria at 007 (Section 3); the Hoelder route is not excluded but
  depends on the OPEN uniform tame inverse H1.
- The b7 centers as route-Q centers (Section 3). The early FLOAT P-S2 values about 0.09 to 0.15 for these centers
  missed the far field; the certified lowers are more than 100 times larger.
- Numerical readings withdrawn by their producers or REFUTED: the 0.086 P-S2 level (00:44Z), the b7 FFT value 0.091
  at P-S2 (02:08Z), the second numerics agent's box-only band split, near-origin background dips 0.7097 and 0.7102 (float artifacts,
  the second numerics agent 03:06Z; four named dips REFUTED at their exact axis points, AT-326), the second numerics agent's base disk N_3 accuracy (AT-425),
  the first numerics agent's mesh P-S2 values for 008 and 009 (E26), the second numerics agent's 93 and 95 percent as plain-E_2 shares (REFUTED, the numerical auditor
  OBS-FRACTIONAL-COMPONENT-LABELS-001; corrected by the second numerics agent 08:28Z), the below-cap reading at the second numerics agent's P-S2 point 4
  (AT-444), and the second numerics agent's FFT-box N_(21/10) values of 009 (superseded by the Hankel values, the second numerics agent 06:33Z).
- Theory statements REFUTED in audit and corrected by their authors, for example: 0.869 as a universal loss
  coefficient (AT-243), the raw P-S1 upper 0.1022924724 (AT-337), 0.19478 as the R -> 0 limit of the CE envelope
  (AT-344), global monotonicity of kappa_q (AT-406), the theory_v07 necessity of lattice atoms at P-S2 (AT-433), the
  TII-0 disk nonpositivity condition for 009 and 008 (AT-419) and the four-to-six-digit Gaussian agreement claim of
  the oscillation probe (AT-448); in the second theory agent's evolving far draft three inferences (AT-610 to AT-612) and, in the
  frozen T2_FAR_v01, the identification of band-limited constants with SC(a) in its section 5.6 (AT-622).
- Coordinator statements corrected after referee passes and audits: the 03:02Z far-field orientation (REFUTED as an
  inference, AT-302), the C5 + b14s bracket of 04:23Z (withdrawn 04:32Z, AT-356), and the draft wording items of
  AT-416 and AT-417; the 08:10Z note's use of the second theory agent's superseded 07:41Z interim figures (26.9 D, 12.8 and 11.1; the second theory agent
  08:30Z) and of the older values 0.978 D and 3.01 q, and its rounding of c - 2/q to 0.858 (the exact target for gain
  2 is c - 20/21, about 0.857938, and 0.858 gives a gain of 1.99987, the numerical auditor audit_v126), all clarified in the
  2026-11-03T09:35Z note. Each correction is a dated note in team notes.

## 7. Reallocation decisions so far (dated; reasons)

| time (notes header) | decision | reason |
|---|---|---|
| 2026-11-02T23:01Z | primary tuple P-S2, P-S1 kept as a target | HEURISTIC break-even of the weight constants |
| 23:19Z | admit composite corrections (C - 007) + h_phi; background stays 007 | C5 is the best exact basis candidate |
| 2026-11-03T02:29Z, 02:42Z | whole-plane P-S2 objective with analytic far part; exact leading far-field rows | C5 + b7 excluded by a distant annulus (AT-260) |
| 03:02Z, 03:15Z | far field first: degree inventory, exact sector rows, near field after | far-field sectors dominate the certified lowers |
| 04:11Z, 04:23Z | P-S1 with the CE test for new centers; b7 centers closed for the named tests | AT-335, AT-352 |
| 04:52Z | 007 + b14s preferred over C5 + b14s (HEURISTIC) | FLOAT P-S1 values further below the necessary levels |
| 05:40Z (X3) | The numerical auditor: 009 applications and whole-plane assembly; the second theory agent: N0 to N3 and C^opt | G1 and G3 at the lead center |
| 06:06Z | The numerical auditor G1 at P-S1 first, then the ||F_*||_2 lower, then the BG-6 gap; the second numerics agent repairs the base near-origin evaluation; the second theory agent decides the rho dependence of the oscillation obstruction | AT-423, AT-449, AT-451, AT-452 and audit_v99 |
| 06:36Z | a certified global s_* < c for 009 to the numerical auditor after G1, with the BG-6 stage; a FLOAT map of s to the second numerics agent; the second theory agent prices the TII-1 and C_aw coefficients with the AT-482 moment bound; no further effort on 008 | AT-476, AT-479, AT-481 to AT-483; the second numerics agent 06:33Z |
| 07:16Z | 009 stays the reference center of the certificate chain; C2-N1-010 is reviewed at X5 from the second numerics agent's whole-plane FLOAT values and the G3 status; the second theory agent prices the far charge against Gbar first | coordinator status reading: the remaining P-S1 certification stages for G1 are the wide-annulus endpoints and the whole-plane assembly (AT-499, AT-529, AT-530 done); whether the assembled upper satisfies the sufficient closure inequality is OPEN; the FLOAT P-S1 N_2 of 010 is only about 5 percent lower |
| 07:37Z | C2-N1-011 replaces 010 as the X5 candidate, 009 stays the chain center; further TII-0 work deferred to the X6 review; the second theory agent tabulates the fitting far radius against the certified gain; the numerical auditor posts a run-time estimate for the revised annulus plan | coordinator reading: a switch restarts the numerical auditor chain while D gains only 8 to 13 percent between N 0.022 and 0.0141 (the first theory agent's note 35, CLAIMED at the time; the D lowers were CONFIRMED at their stipulated inputs afterwards, AT-563); TII-0 fails at every rho in the first theory agent's FLOAT screen at l = 2.76e-6 (AT-549, AT-551; at l = 1.5e-6 middle rates are not excluded, theory_v09 V9-4) and C^opt >= P is REFUTED (AT-552); cap 512 REFUTED as sufficient (the numerical auditor OBS-009-ANNULUS-CAP-METHOD-001) |
| 08:10Z | The second theory agent freezes T2_FAR_v01 and works on the far side at rho in [1, 2]; the first theory agent seeks a sharper far upper near rho = 1 and an auditable near price before further budget tables; C2-N1-012 replaces 011 as the X5 candidate, 009 stays the chain center; the numerical auditor scores the smaller-disk geometries next to the running six-panel plan | coordinator reading (HEURISTIC): on the TII-1 + CAW-F + HF-1 route the smallest sampled P_A/U is 2.69 and 2.34 even at G = q (the second theory agent 07:41Z; finite model arithmetic CONFIRMED, AT-574; no exclusion, AT-576); among the scanned rows of table F8 the near price fits D only at rho <= 1, with smallest associated far charges 23.1 q and 9.22 q at N 0.022 and 0.0141; the numerical auditor's 009 chain is running (audit_v121) |
| 2026-11-03T09:35Z (with this report) | The first theory agent moves its effort from G2 to the theory side of G3 (the theory_v10 deliverables of theory_v09 V9-10: a far upper of the complete 009 far form on rho in [1, 2], or a stated reason why the route cannot reach the needed factor, and the HF-1 near price at rho about 1 as a proposition for audit) and adds D rows at the forcing uppers 1.0e-6 and 1.1e-6 for X5; TII-0 stays deferred, and X5 decides whether a TII-0 price at the smaller size earns a slot; the second theory agent continues the far side at rho in [1, 2] with the theory_v09 V9-9 budgets and corrects section 5.6 of T2_FAR_v01; the numerical auditor keeps its order and uses the strain target 0.85793 in place of 3/2 if the cover cost allows; the second numerics agent evaluates each new snapshot on the whole plane (013 done at 09:12Z) and reconciles its 010 share with the numerical auditor; the first numerics agent extends the near-field rows; 009 stays the chain center until X5, which reviews 012 or 013 | coordinator reading (HEURISTIC): G2 at 009 is conditionally reduced to the other items (AT-600); on the fixed far scan no gain up to q passes (AT-613, AT-616); for the log-8 split at rho = 1 the FLOAT floor SC(a_f) 0.968 exceeds Gbar, so for that split a larger certified gain and a far upper within a few times the floor are both needed (Table F10, theory_v09 V9-10; at log 16 and log 32 the floor at rho = 1 lies below Gbar); the X5 D rows at f = 1.5e-6 cover 012 if its norm and N uppers are certified; at l = 1.5e-6 the TII0-RHO screen leaves middle rates unexcluded (V9-4); 013's whole-plane FLOAT N_(21/10) at P-S1 is 0.0054 and its polar ||F_*||_2 9.95e-7 (the second numerics agent 09:12Z); the first theory agent's 1.23 ceiling for absolute-kernel far bounds is REFUTED as a general bound (AT-650); the full planner completed and the annulus primary started at 09:16:42Z (OBS-009-ANNULUS-START-001) |

## 8. Plan for hours 24 to 48 and fallbacks

Effort is set by the gap table of Section 1.
1. G1 (the numerical auditor, audited by the theory auditor; the second numerics agent and the first numerics agent supply FLOAT targets): certified regional energies of 009 at P-S1 on
   the disk, the annuli up to 1e4 and the exterior, assembled into a whole-plane upper of N_(21/10). The exterior
   through order 3 is done (AT-499); the origin disk bounds are CONFIRMED at both weights (AT-529, AT-530, AT-537,
   AT-538); the wide annulus (request and policy targets CONFIRMED, AT-542, AT-543; the order cap 512 is REFUTED as
   sufficient, the numerical auditor OBS-009-ANNULUS-CAP-METHOD-001; the cap-2048 repair and three smaller-disk geometries are
   CONFIRMED conditionally, AT-555, AT-561, and the numerical auditor's scheduling probe found orders 259/274/203, 180/175/132 and
   144/130/106 at radii 2, 8 and 32 for 16, 32 and 64 panels per doubling, audit_v119; the full P-S1 planner with the
   original six-panel policy started at 07:53:56Z, audit_v121, and completed all 114 panels at 09:16:34Z in about
   4956 s, maximum order 682, audit_v139; the 1024-bit primary started at 09:16:42Z, OBS-009-ANNULUS-START-001) and
   the whole-plane assembly follow. Coordinator reading: the annulus run time is the G1 schedule risk; the planner
   finished about 19 minutes after the numerical auditor's HEURISTIC estimate of 08:20:09Z (28.83 s per panel and a finish near
   08:57:38Z, audit_v126; about 43 s per panel on average), and the first primary panel (order 156) completed at
   09:21:59Z with negligible arithmetic error in its independent reduction, which does not test the later orders up
   to 682; the numerical auditor's HEURISTIC full-primary predictions from three panels are 10.31 h and 25.55 h
   (OBS-ANNULUS-TIMING-001, extrapolation OPEN; audit_v139, audit_v140, MID_CAMPAIGN_AUDIT_v01, AT-573). The numerical auditor
   retains the six-panel policy, which the linear work score favors, while a quadratic score favors 32 panels per
   doubling and a switch would need a new plan (OBS-SCHEDULING-SCORES-001); the probe orders of the smaller-disk
   geometries are CONFIRMED conditionally on the saved source majorants (AT-586; runtime and energies OPEN, AT-587).
   The numerical auditor has also prepared a method that extracts global lower bounds, not uppers, from a completed, independently
   verified prefix of source-bound annulus energy panels (OBS-PARTIAL-ANNULUS-METHOD-001, audit_v135; method
   CONFIRMED under the exact-source and containing-panel hypotheses, AT-658, its code CONFIRMED conditionally,
   AT-659; at 09:13:28Z no actual prefix publication existed, AT-660). Its first application, the first panel 1/50 <=
   r <= 7/300, gives the global lowers N_2 >= 0.000498 and N_3 >= 0.08416 for G = sqrt(1 + 4r^2) F_* and ||F_*||_2 >=
   3.207e-8 (OBS-009-PREFIX-source009_first_panel_v01, CONFIRMED global lower bounds only); lower bounds do not
   certify small forcing, and the queue is unchanged. Target: by hour 30 (2026-11-04T00:05Z) under the shorter timing
   model; under the longer one the primary alone ends near hour 40.7, so the target and the place of the joint cover
   in the queue are reviewed at X5 with the numerical auditor's next timing update. P-S2 second.
2. L and B (the numerical auditor): a certified two-sided bound of ||F_*||_2 (the unweighted bracket of the same assembly, AT-484, by
   the exact quadratic-division method CONFIRMED conditionally, AT-603, AT-604) and the joint global cover of 009
   (BG-6, the correction gradient, which the G2 bridge needs at g_* <= 1/4, and s_* <= 3/2; AT-508 to AT-511,
   AT-600). The numerical auditor has costed the strain targets: sbar = 1.5, 1.349 and 0.858 give gains 0.651670, 0.968770 and
   1.999870; gain 2 needs s_* <= c - 20/21, about 0.857938, for which the rational 0.85793 suffices; the numerical auditor's default
   was the 3/2 cover (audit_v126); the 2026-11-03T09:35Z note asks for 0.85793 in place of 3/2 if the cover cost allows,
   since at rho = 1 no far upper fits under Gbar (item 3). The numerical auditor's exact correction-gradient refinement from
   completed cover leaves (method CONFIRMED under its complete-cover and source-representation hypotheses, AT-652,
   and its frozen code conditionally, AT-653, OBS-GRADIENT-REFINEMENT-REVIEW-001; the 009 application OPEN, AT-654)
   can test the threshold 0.14215453 for the rate 93/50 on the same completed cover without a new field evaluation
   (audit_v134, audit_v136); the second numerics agent names the annulus 0.6 <= r <= 0.8 within 30 degrees of the y-axis as the region to
   refine first (09:07Z, FLOAT). In the second numerics agent's FLOAT band table of max s (08:32Z) the binding bands of a Lipschitz cover
   for 0.858 are 0.03 <= r <= 2, with margins 0.05 to 0.2, and the margin to 3/2 is at least 0.69 everywhere. Target:
   by hour 36.
3. G3 (the second theory agent, the first theory agent; the theory auditor audits; the numerical auditor for s_*): the rho question of 06:06Z is answered qualitatively (AT-462,
   AT-476). Next: a certified global s_* < c at 009 (the numerical auditor, with the background stage), explicit far-moment constants
   of the complete 009 source (not of unchanged 007, AT-477) with a sufficiently smooth cutoff (AT-478; for the P7
   far piece M4 and M_(2,q), q >= 2, are infinite, AT-481, and the conditional M_(2,11/10) bound of AT-482 applies),
   the smallest rho at which the TII-1 and C_aw coefficients fit under the conservative budget Gbar (between 0.6516
   and 0.6517, a lower bound of the gain for the target s_* <= 3/2, AT-510), and the price of the near-field and
   remaining H4 contributions at that rho, compared as one complete weak coefficient with a sufficient budget
   recomputed for compatible certified ||F_*||_2, beta_0 and N(F_*) (the displayed D values are stipulated
   comparisons only). Coordinator decision of 07:37Z: defer further TII-0 work until the X6 review at
   2026-11-03T18:05Z (FLOAT readings: AT-503 at rho <= 10; for every rho the first theory agent's screen with Proposition TII0-RHO at
   l = 2.76e-6, AT-549, AT-551); the requested point, positive-part integral and residual lower certificates remain
   queued after the 009 annulus, assembly and global cover, and the actual-source all-rate exclusion remains OPEN.
   The second theory agent tabulates the fitting rho as a function of the certified gain (its 07:41Z note, as the coordinator's 07:37Z
   note requested), which decides how sharp the certified strain upper must be. Coordinator reading of AT-513,
   AT-547, AT-548 and AT-553: under the hypotheses of AT-547 and AT-553 (a real coefficient with an ordinary
   integrable Fourier transform and finite second Fourier moment whose joint-form upper holds for every real Schwartz
   test even in x and odd in y), agreement with atil near zero forces the joint charge to be at least 4[q^2(2c - 1) +
   1] > 50, so it cannot be absorbed entirely into G <= q; in the planned TII-1 decomposition the near field is
   priced in the base constant, and other full-energy decompositions are not excluded. The 08:10Z note sets the
   HEURISTIC priorities: a sharper far upper for the complete 009 far form near rho = 1, a compatible certified
   strain bound, and a certified near price within a sufficient budget. The frozen T2_FAR_v01 sharpens this
   (coordinator reading, HEURISTIC): on its fixed finite scan failure at G = q implies failure at every smaller gain
   (AT-613, AT-616), so a sharper strain bound helps only together with a sharper far upper; for the log-8, log-16
   and log-32 rows at N 0.022, a certified far upper within factors 1.46 to 1.78 of the FLOAT floor SC(a_f) would fit
   under Gbar at the HEURISTIC radius rho_U where the model near price meets U, and within 4.72 to 5.73 under q
   (Table F10), against model factors of 16 to 19 for Lemmas TII-1 and CAW-F; for the log-8 split at rho = 1 the
   floor exceeds Gbar, so for that split only a larger certified gain helps (theory_v09 V9-10); this is not a
   cutoff-independent necessity, since at rho = 1 the FLOAT floors at log 16 and log 32 are 0.419 and 0.210, below
   Gbar (T2_FAR_v01 Table F1). The first theory agent's order of levers (theory_v09 V9-6, V9-10) is therefore: a certified strain
   upper that raises the gain from Gbar toward q (gain at least 2 when s_* <= 0.85793, the numerical auditor audit_v126; the sampled
   strain maximum of 009 is 0.8103, FLOAT), then a far upper of a kind different from Lemma TII-1, then the near
   price. On the far upper, the theory auditor CONFIRMS the double-commutator identity for the far form Q_a of the first theory agent's note 36 item
   6 (AT-648) and, conditionally on the stated Fourier moment and high-frequency support, a frequency-dependent
   absolute-kernel bound of the complete Q_a + C_a high-high block that is no larger than the separate TII-1 and
   CAW-F block and tends to q^2 M2/2 (AT-649); the first theory agent's orientation that a Schur test on the exact kernel gains at
   most about 1.23 over TII-1 + CAW-F, so that a factor 2.5 needs sign information, is REFUTED as a general bound
   (for a smooth radial Fourier-annulus coefficient at q = 2.1 and nu = 100 the absolute-kernel improvement exceeds
   3.71515; the 1.23 ceiling holds only for the separately qualified principal-symbol comparison, AT-650); no
   improved far upper of the complete 009 form follows yet (AT-651, OPEN). One route to a far upper is AT-609 applied
   to a certified upper of the complete 007 continuum far form and a certified difference-form bound on the same full
   test space; starting from a band value additionally needs certified control of the gap to the complete continuum
   supremum (AT-621 gives convergence from below without a remainder), and AT-610 refutes the transfer without a
   difference bound; the theory auditor REFUTES the unqualified implication from a certified band upper and an exact
   difference-form bound to the complete continuum upper (a radial Schwartz coefficient with Fourier support in 3 <
   |zeta| < 4 has A_1 = 0 but A_* > 0.3083330269, AT-661) and CONFIRMS, under its exact continuum, source and block
   hypotheses, the common-space transfer A_T(b) <= B + E and the complete-block bound A_*(a) <= lambda_max[[B, C],
   [C, H]] (AT-662); no actual complete-009 far upper is supplied (AT-663, OPEN); the theory auditor CONFIRMS the first theory agent's
   Hessian-principal plus weighted-Schur (HS) far bound under its exact hypotheses and a finite certified Schur cost
   (AT-664; the first theory agent research/far_hh/HS_DERIVATION.md) and proves an oscillation-plus-moment bound |Q_a(g) + C_aw[a](g)|
   <= [osc(a) + M2(a) + (q^2/2) Mw(a)] ||J^(-1) g||_2^2 whose Q constant osc + M2 is no larger than any old TII-1
   split-matrix constant (AT-665, CONFIRMED under ordinary Fourier L1 and the displayed finite moments); recombined
   from the printed FLOAT Table F1 inputs, its charges are 1.589 at log 8, rho 2.5 (old 2.54), 0.622 at log 16, rho 3
   (old 0.958) and 4.95 at log 16, rho 1 (old 7.27), FLOAT arithmetic and not bounds; two unqualified readings of the
   HS draft, an exclusion of HS closure from the floor alone and Lipschitz Schur rows from the stated weight
   hypotheses, are REFUTED (AT-666), and no actual full-009 upper follows (AT-667, OPEN); the frozen HS scans
   reproduce as finite FLOAT arithmetic (AT-678) and their positive radial weights are admissible (AT-679), but the
   sampled HS tables give no continuum far upper (AT-680, OPEN); band constants need not converge to SC(a) (AT-622),
   so SC(a_f) is a scale for the target, not a value the band calculations are known to approach. At the stipulated
   forcing upper 1.5e-6 and beta_0* = 7/4 the first theory agent reads the HF-1 model price at G = q as about 2.0 to 2.1 D and at Gbar
   as 6.6 to 6.8 D, and the near price at rho = 1 as about 0.41 D (theory_v09 V9-9 (d), V9-10; HEURISTIC model prices
   of the 009 coefficient, not bounds). TII-0: at l = 2.76e-6 the screen excludes every rate for n >= 0.01, but at
   the stipulated input l = 1.5e-6 middle rates are not excluded even at n = 0.022 (V9-4, AT-642; a FLOAT screen of
   unchanged 007, candidate-specific bounds OPEN); the 07:37Z deferral stands, and at X5 the coordinator decides with
   the first theory agent's input whether a TII-0 price at the smaller size earns a slot before X6. The numerical auditor's exact method for D = X.u
   on fixed rational circles is CONFIRMED in its formulas (AT-655) and its frozen code conditionally (AT-656); the
   actual circle extrema and any far operator upper are OPEN (AT-657), and no stage is placed ahead of G1 or the
   cover (OBS-D-CIRCLE-METHOD-001, audit_v133). Checkpoint at X6 = 18:05Z.
4. G2 (the first theory agent): at 009 the G2 checklist is CONFIRMED as a conditional reduction to certificates of G1, L, B and G3 at
   stipulated values (Lemma KB and the bridge, AT-598 to AT-600); the first theory agent recomputes the reference ball and the KB
   witness if the certified source upper or rate differ from the stipulated ones, and the premises come from items 1
   to 3 (AT-602, OPEN).
5. Hours 44 to 48: no redesigns; final ledger, the five Part VII reports and restart instructions.

Fallbacks (decided now so that they need no later discussion):
- If G1 at P-S1 fails for 009 (a certified lower above the necessary level), move to the next far-field-first fit
  that lowers the P-S1 FLOAT N_(21/10), keeping c_l and Candidate 007 fixed.
- If G3 stays open at hour 40, the final report states the conditional theorem with every condition that is still
  unresolved at that time as a hypothesis. Only if G1, L and B have been certified with compatible inputs can the
  remaining hypotheses be H4 and G2 (G2 then reduces conditionally to H4 and the scalar source test if the certified
  values meet the stipulated ones of AT-600); certified items are recorded either way.
- If the far charge fits at a usable rho only with a gain above Gbar, the numerical auditor applies the strain refinement (AT-539,
  AT-540; application OPEN, AT-541) to the first completed cover.
- P-S2 at 009 stays a second tuple: its FLOAT N_(21/10) 0.06220 lies below the CE levels 0.10369 to 0.145749 (AT-390,
  FLOAT comparison), but the H4 analysis exists only at P-S1.
