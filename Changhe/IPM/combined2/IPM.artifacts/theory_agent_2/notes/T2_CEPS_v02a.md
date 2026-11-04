# T2_CEPS_v02a: audit status, errata and certified witnesses for T2_CEPS_v02

Addendum to notes/T2_CEPS_v02.md (frozen 2026-11-03T01:41:45Z, SHA256
62d86ab10ec6a910d45d18a297ce505b88a21c4dea471ad56184a7a0ea2016b3). Owner: the second theory agent. Written 2026-11-03T01:47Z to 01:48Z
after reading the theory audit exchange/audit_v89 to v91 (AT-231 to AT-239). Paths are relative to the combined2 root; files of
this agent relative to theory_agent_2/, files of the theory auditor relative to theory_audit/. It answers the theory auditor requests of audit_v91 (scope and
display corrections before theory_v04 and X2) and the second theory agent items (1) to (3) of the coordinator X2 planning (exact bridge
hypotheses, certified witnesses at b0 in {0.55, 0.60} and ||F||_2 in {1e-6, 1e-5, 3e-5}, T2_BUD relabel).

Labels. CONFIRMED items are cited, not re-proved. The witness tables of section 3 are CLAIMED: outward Arb arithmetic on
exact rational inputs, audit requested. Their inputs (b0, beta_0, ||F||_2, N(F)) are stipulated numbers, not certified
properties of any background or source, and no table is a closure.

## 1. Audit status of T2_CEPS_v02

the theory auditor audited a snapshot of the note taken at 2026-11-03T01:35:04Z during its revision (the theory auditor
research/ceps_v02_targets/T2_CEPS_v02.md, SHA256 146ec104e454d41a65510fc859b0ada80741c217f47abbe82fddb797dc154a49). The
frozen file states the same theorem, lemmas and closed-form constants. It differs from the snapshot in the header,
the decimal display (the upward replacements 0.450791, 0.241725 and 16.5433 of AT-239 are already in it), the removal
of the .077 and .0779 scalar exclusions, the comparison point (now R = 1.4e-5 throughout) and the time labels.

| item | status |
|---|---|
| Lemma CORE: core <= (53/100) S_core ||D^q U[k]||_2 G^2 | CONFIRMED (AT-234) |
| near-weight pairs (B, A) = (51/100, 40.919), (13/25, 18.959), (11/20, 6.73), (3/5, 2.96) | CONFIRMED (AT-235) |
| Theorem HF-Q, rough-coefficient extension | CONFIRMED with exact constants (AT-237) |
| Proposition S0 and Corollary HF-Q-B | CONFIRMED as conditional implications (AT-237, AT-229) |
| four-pair scalar maxima at the stipulated inputs | CONFIRMED (AT-236): 0.0654896..., 0.0770349..., 0.0895279... at b0 = 0.60, 0.65, 0.70, ||F||_2 = 1e-5, beta_0 = 2.09 |
| small-R limits | qualified (AT-238); see erratum E1 |
| display corrections | AT-239; the remaining ones are errata E2 to E5 |
| explicit C^opt(b0), fitted-center rate, fitted-source norms, invariant ball | OPEN |

Exact statement (AT-237). With S_core = 1/[2 sqrt(pi (q - 1)(q - 2))] (the S_1 of T2_CEPS_v02), for every B > 1/2,
    L_B(R, K) = q C_sym R^((q-2)/q) K^(2/q) + (53/100) S_core K + (sigma/2 + A0(B) L_0) C_a R^(1-1/q) K^(1/q)
                + B S_w [(sigma/2) K + q 2^(q-2) (L_1 R^(1/q) K^(1-1/q) + L_q R)],
    A0(B) = sup over x >= 0 of ([(1 + x)^q + (1 + x)^(-q) - 2]/2 - B x^q),
and |Re (J^q [W (U[k].grad h)], g)| <= L_B(||k||_2, ||D^q k||_2) G^2 for every real S1 k with both norms finite and
every real S1 Schwartz u. On K(R, M) substitute K = c_W M; every term is monotone in R and K.

Hypotheses of the self-map bridge, exactly as retained in AT-237 (the coordinator item (1)). One specified background and
the weight W satisfy all of the following.
- H1. The actual closed-generator, core, weighted-semigroup and graph-comparison hypotheses of AT-066, AT-069, AT-114
  and AT-178 hold on a reference ball that contains the trial ball K(R, M).
- H2. The imported L^2 inverse gives z = -A_k^(-1) F with ||z||_2 <= R = ||F||_2/beta_0 for every k in K(R, M), and
  the qualitative weighted inverse gives N(z) < infinity before the energy is tested.
- H3. Normalization R3/R5: F real S1, F_y(0) = 0, N(F) < infinity, and the conditions that preserve ell_R3(z) = 0.
- H4. Base weak energy at k = 0 for the same background and weight: Q_0(u) <= -b0 G^2 + C0 ||h||_2^2 for all real S1
  Schwartz u, with b0 > 0 and C0 >= 0 finite (C0 = C^opt(b0) is allowed, since the defining inequalities are closed
  under decreasing limits of C0).
- H5. b := b0 - L_B(R, c_W M) > 0.
Conclusion: b N(z)^2 <= N(F) N(z) + C0 R^2, so N(F) <= b M - C0 R^2/M (direct form) or
N(F) + (b0 C0)^(1/2) R <= b M (conservative form) gives the self-map T(K(R, M)) contained in K(R, M), including the
L^2 and normalization constraints. Existing frozen estimates keep their own restrictions (for example
delta > alpha/(2 c_l - 2)); HF-Q neither changes nor waives them.

What the bridge does not supply. For unchanged 007 the certified lower matrix margin 3/5 does not by itself supply
C^opt(3/5) (AT-237): the usual finite weak estimate uses a strictly smaller base rate. C^opt(b) = +infinity for
b >= 0.6588409179 (HF-NEC-1, AT-199, AT-211). For a corrected center, the rate is BG-6 and is OPEN.

## 2. Errata to the frozen T2_CEPS_v02

E1 (section 0 item 2 and the "Floor" paragraph of section 4; AT-238). The displayed bound
"l_Q > (0.4508 + 0.1331) c_W M = 0.869 M" is not valid as written: 0.4508 is an upward rounding used inside a lower
bound, and the exact coefficient is below 0.869. Correct statement: for every R > 0 and every B > 1/2,
    L_B(R, c_W M) > lambda_* M,   lambda_* = c_W [(53/100) S_core + S_w sigma/4] = 0.868992902989...,
because all other terms are nonnegative and B S_w sigma/2 > S_w sigma/4. For a fixed B the limit of L_B(R, c_W M)/M as
R -> 0 is lambda_B = c_W [(53/100) S_core + B S_w sigma/2] > lambda_*; for the smallest confirmed pair
lambda_(51/100) = 0.872955437553... The value lambda_* is the limit only when B is optimized over all B > 1/2 with
B(R) -> 1/2 (AT-238). The floor of eta in section 0 item 2 is therefore lambda_* M/b0, approached only in that limit.
The consequence drawn in the note survives with the exact constant: Phi_max < b0^2/(4 lambda_*) = 0.287689346069... b0^2,
so the displayed ceiling Phi_max < 0.2877 b0^2 and its values 0.104, 0.122 and 0.141 at b0 = 0.60, 0.65 and 0.70 are
valid upper decimals. The ceiling holds for every ||F||_2, and AT-238 shows that it is the R -> 0 limit of the
B-optimized capacity.

E2 (section 1, constants; AT-239). C_a = B_0/sqrt2 = 0.3453202951..., so its upper decimal is 0.345321, not 0.345320.
The coefficients 0.241725 = (sigma/2) C_a and 0.759399 = L_0 C_a displayed in Theorem HF-Q are valid uppers.

E3 (section 5, reading; AT-239). The sentence "The earlier C5 + h level (N(F) = 0.0765 at ||F||_2 = 2.8e-5) fails
(HFQ) at b0 = 0.60 and 0.65 even at C^opt = 0" is a FLOAT statement about the grid maximum over the six AT-230 pairs. It
is not a certified exclusion over all B > 1/2. The value 0.0765 is a FLOAT corrected-grid-center value (C5 + h). It
says nothing about unchanged 007, whose complete P-S2 source norm lies in (261.62, 285.56) (AN-059, AT-188). A
fitted-center source quantity and an old-background weak constant or rate cannot be combined without a transfer
argument (AT-239). In particular the b0 = 0.6588 column of tables 1 and 2 pairs the 007 rate envelope with
corrected-center source values and is orientation only.

E4 (section 5, rate admissibility). "b0 = 0.60 is the certified 007 lower margin" is correct, but C^opt(0.60) is not
supplied for 007 by that margin (section 1). Witnesses at b0 = 0.55 are added in section 3.

E5 (section 8, status table). Superseded by the table in section 1 of this addendum: Lemma CORE, Theorem HF-Q and
Corollary HF-Q-B are CONFIRMED in the conditional exact-constant scope of AT-234 and AT-237.

## 3. Certified witnesses (CLAIMED; research/hf/hfq_witness.py, output research/hf/hfq_witness.out)

Method. L_B is evaluated with the exact closed forms above in python-flint Arb at 200 bits, with exact rational
inputs q = 21/10, sigma = 7/5, c_W = 7441/5000, beta_0 = 209/100 and the four AT-235 pairs. For each case a float search
over M and the pairs selects M, which is rounded to a rational with three significant digits. The statement is then the
Arb evaluation at that rational M only. Each printed value is a decimal checked by an Arb comparison to lie strictly
below the enclosure. The run took 8 s on core 40 at nice 19, OMP_NUM_THREADS=1, at 2026-11-03T01:46Z.

Capacity P(M) = (b0 - L_B(R, c_W M)) M with R = ||F||_2/beta_0. Under H1 to H5 with C0 = 0, the self-map holds for
every N(F) <= P(M).

Table W1. Lower decimals of P(M) at the rational M shown, with the pair used.

| ||F||_2 | b0 = 0.55 | b0 = 0.60 | b0 = 0.65 | b0 = 0.6588 | b0 = 0.70 |
|---:|---:|---:|---:|---:|---:|
| 1e-6 | 0.0579378 (M 0.213, B 11/20) | 0.069081 (0.233, 13/25) | 0.0812282 (0.253, 13/25) | 0.0834687 (0.256, 13/25) | 0.0943685 (0.273, 13/25) |
| 1e-5 | 0.05489 (0.202, 11/20) | 0.0654893 (0.221, 11/20) | 0.0770347 (0.24, 11/20) | 0.0791648 (0.244, 11/20) | 0.0895278 (0.259, 11/20) |
| 3e-5 | 0.0529585 (0.196, 3/5) | 0.0631937 (0.214, 3/5) | 0.0743434 (0.232, 3/5) | 0.0764004 (0.235, 3/5) | 0.0864412 (0.252, 11/20) |

Consistency: at ||F||_2 = 1e-5 the witnesses lie below the AT-236 maxima 0.0654896, 0.0770349 and 0.0895279 by at
most 3e-7, and above the AT-230 witnesses for the old core (0.054218, 0.063757, 0.074077) by 0.0113 to 0.0155.

Table W2. Direct budget for C0: lower decimals of D(M) = M (P(M) - N(F))/R^2 at a rational M (shown with the pair).
Under H1 to H5 the self-map holds whenever C0 <= D(M).

| ||F||_2 | b0 | N(F) = 0.01 | N(F) = 0.0257 | N(F) = 0.05 |
|---:|---:|---:|---:|---:|
| 1e-6 | 0.55 | 5.17e10 (0.275, 13/25) | 3.34e10 (0.259, 13/25) | 7.62e9 (0.227, 13/25) |
| 1e-6 | 0.60 | 7.00e10 (0.303, 13/25) | 4.97e10 (0.288, 13/25) | 2.06e10 (0.261, 13/25) |
| 1e-6 | 0.65 | 9.18e10 (0.33, 13/25) | 6.97e10 (0.316, 13/25) | 3.73e10 (0.293, 13/25) |
| 1e-6 | 0.70 | 1.17e11 (0.357, 13/25) | 9.36e10 (0.345, 13/25) | 5.81e10 (0.323, 13/25) |
| 1e-5 | 0.55 | 4.60e8 (0.261, 11/20) | 2.86e8 (0.244, 11/20) | 4.41e7 (0.211, 11/20) |
| 1e-5 | 0.60 | 6.24e8 (0.287, 11/20) | 4.32e8 (0.272, 11/20) | 1.57e8 (0.244, 11/20) |
| 1e-5 | 0.65 | 8.21e8 (0.313, 11/20) | 6.11e8 (0.3, 11/20) | 3.05e8 (0.275, 11/20) |
| 1e-5 | 0.70 | 1.05e9 (0.339, 11/20) | 8.25e8 (0.327, 11/20) | 4.90e8 (0.305, 11/20) |
| 3e-5 | 0.55 | 4.72e7 (0.253, 11/20) | 2.86e7 (0.235, 3/5) | 2.84e6 (0.201, 3/5) |
| 3e-5 | 0.60 | 6.43e7 (0.278, 11/20) | 4.37e7 (0.263, 11/20) | 1.43e7 (0.234, 3/5) |
| 3e-5 | 0.65 | 8.48e7 (0.303, 11/20) | 6.22e7 (0.29, 11/20) | 2.95e7 (0.265, 11/20) |
| 3e-5 | 0.70 | 1.09e8 (0.329, 11/20) | 8.45e7 (0.316, 11/20) | 4.85e7 (0.294, 11/20) |

The b0 = 0.6588 rows are in the output file. Reading (HEURISTIC): the C0 budget scales like ||F||_2^(-2) (a factor
of about 100 per decade), while the capacity changes by about 0.004 per decade. At the fit target (||F||_2 about 1e-5,
N(F) about 0.026) the binding quantity is C0 = C^opt(b0) at a certified rate. C0 must then be at most a few times
1e8; at ||F||_2 = 1e-6 the limit rises to a few times 1e10.

Larger capacity. Optimizing B over (1/2, 0.8) with a numerically computed A0(B) raises the capacity by 6e-6 to 2e-5
at ||F||_2 = 1e-5 (optimal B about 0.555) and by 1.2e-4 to 2.2e-4 at 1e-6 (B about 0.53) and 3e-5 (B about 0.57).
These are FLOAT values (scratch/ceps2a/bopt_float.py, uncertified sup). This is too small to justify new pairs, so the
four confirmed pairs are used as they are. The radius is optimized to three significant digits.

## 4. Relabel of T2_BUD_v01 (the coordinator item (3); AT-202, AT-203, AT-199, AT-211, AT-215)

- Proposition S is a sufficient condition for AT-114 (6) at a trial-ball rate, not an equivalent one (AT-202).
- Table D of T2_BUD_v01 computes the sampled (6_l) budget, not the (S) budget (AT-203; corrected values in the theory auditor
  exchange/audit_v80.md).
- Rows at b = 0.6607 are not admissible for unchanged 007. At P-S2, C^opt(b) = +infinity for b >= 0.6588409179
  (AT-199, HF-NEC-1, AT-211).
- Rows at b = 0.7103 are finite-rate examples strictly below the corrected-center origin cap c_l + 1 - q. The positive
  gap of about 1.92e-5 is certified at AT-215. They need a certified corrected-center rate, which is OPEN (BG-6).
- For route choice, T2_BUD_v01 tables A to D (gradient tame term, T_1 >= 1) are superseded by HF-Q (no tame term) and
  section 3 above. Their numbers stay FLOAT orientation. A separate T2_BUD_v02 is not planned; this list is the relabel.
