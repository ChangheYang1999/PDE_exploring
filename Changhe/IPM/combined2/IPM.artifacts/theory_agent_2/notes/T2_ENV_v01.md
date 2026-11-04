# T2_ENV_v01: NEC-R envelope and screen curve for a new P-S1 source (theory_v06 T6.4 item 3)

Agent the second theory agent. Answer to theory_v06 T6.4 item 3, third bullet (the first theory agent): a check of the NEC-R levels at the AT-351 lowers
(the first theory agent research/qwg/v02/hfq_ps1/necr_at352/) and, for new centers, the envelope sup_M Phi as a function of a certified
radius lower and a rate, in a form that the first numerics agent can apply to a new fit. All times are real UTC times. Labels: CONFIRMED
(cited audit), CLAIMED (proved or computed here, audit requested), FLOAT, HEURISTIC, OPEN. P-S1 = (21/10, 1, 1/2),
cap c + 1 - q = 0.710319210199998, lambda_1 = 0.640978603636 (P-S1).

## 0. Summary

- All 20 necessary levels printed by the first theory agent in necr_at352 and necr_b14s (10 for the CE input, among them the AT-335
  level 0.141102 and the AT-344 value 0.19478, and 10 for the original input) and two further Table A2 levels of
  T2_H4A_v01 are re-enclosed by a second method: a branch-and-bound over M that uses only the monotonicity of each
  term of Phi on an interval, not the concavity tangents of ceil_R.sup_phi (Part 1, all 22 PASS). The two methods
  share the terms of Phi (ceil_R.terms); the check is independent in the supremum step only. This agrees with AT-352
  and with the first theory agent's note 23 item 2.
- Table E1: envelope L(b0, R), upper decimals of sup_M Phi(M; b0, R) on a grid of 9 rates and 10 radii (CE input).
  Lemma ENV gives the lookup rule: round the rate up and the radius down to grid values.
- Table E2: screen curve. For a source lower n of N(F), the radius R*(n) beyond which every b0 <= c + 1 - q is
  excluded, and l*(n) = (c + 1) R*(n) for a certified lower of ||F||_2 (beta0 <= c + 1). Each R* is sharp to two
  significant digits: one unit lower, the certified lower of sup Phi exceeds n.
- research/h4/necr_env.py screen <n> <l> <rate> applies the screen to one fit.
- Orientation (stipulated inputs; not certified; AT-356): at N = 0.0922 and ||F||_2 = 1.4e-5 the CE P-S1 test is not
  excluded at the cap, but a pass needs b0 > 0.5966837. Excluding by NEC-R alone at N about 0.092 would need a certified
  ||F||_2 >= 0.0031; at ||F||_2 = 1.4e-5 it would need N(F) >= 0.131231.

## 1. Setting and the two monotonicity facts

Phi(M; b0, R) = b0 M - sum_i c_i(R) M^(p_i) is the concave majorant of Proposition NEC-R (notes/T2_PS1_v01.md; code
research/ps1/ceil_R.py, terms(), with kf = 1 for the CE input, any uniform Kbar >= M (AT-274), and kf = c_W =
9619/5000 for the original test). The powers are p_i >= 1, and each c_i(R) is a positive constant times R^(e_i) with
e_i in {0, th, 1 - 1/q, 1/q, 1}, so c_i(R) is nondecreasing in R. A passing direct P-S1 test at rate b0 <= c + 1 - q
(origin cap, AT-211) and radius R, in the criterion form re-enclosed in AT-307 and AT-335, with positive gap, needs
N(F) <= sup_(M > 0) Phi(M; b0, R) (NEC-R). All exclusions below are exclusions of this test under these hypotheses,
not nonexistence statements.

Lemma ENV (CLAIMED). If b0 <= b and R >= r, then sup_M Phi(M; b0, R) <= sup_M Phi(M; b, r).
Proof. For each M > 0, b0 M <= b M and c_i(R) M^(p_i) >= c_i(r) M^(p_i). QED.

So with a table value L(b, r) > sup_M Phi(M; b, r), a source with a certified lower n of N(F) >= L(b, r), a certified
rate bound b0 <= b and a certified radius lower R >= r is excluded. If beta0 <= c + 1 (as in AT-352) and l is a
certified lower of ||F||_2, then R >= l/(c + 1).

## 2. Re-enclosure of the printed levels (research/h4/necr_env.out, Part 1)

Method. Phi(M) < 0 for M >= Mmax = (b0/(kf lambda_1)) (1.001), rounded up. On [Ma, Mb] with Ma > 0,
Phi <= b0 Mb - sum_i c_i Ma^(p_i); on [0, Mb], Phi <= b0 Mb. Start with 64 equal intervals; an interval is discarded
when its Arb upper is below the level and bisected otherwise. The run stops with NOT DECIDED if Phi at a midpoint is
certified above the level or after 400000 intervals. Every printed level was decided as PASS.

| input | R | level | source of the level | tangent lower |
|---|---:|---:|---|---:|
| CE | 1e-7 | 0.141102 | AT-335, necr_at352 | 0.1411012 |
| CE | 1.7e-7 | 0.139964 | necr_at352 | 0.1399635 |
| CE | 1.2e-9 | 0.149564 | necr_at352 (007 + b7 fails for R >= 1.2e-9) | 0.1495296 |
| CE | 1e-60 | 0.231239 | necr_at352 (C5 + b7 fails for R >= 1e-60) | 0.1965640 |
| CE | 1e-40 | 0.19478 | AT-344 | 0.1947798 |
| CE | 1e-6 | 0.135802 | necr_b14s | 0.1358011 |
| CE | 3e-6 | 0.132791 | necr_b14s | 0.1327909 |
| CE | 1.4e-5/(c + 1) | 0.131231 | necr_b14s, T2_H4A_v01 Table A2 | 0.1312303 |
| CE | 1.4e-5/(209/100) | 0.130255 | necr_b14s, T2_H4A_v01 Table A2 | 0.1302542 |
| CE | 1e-5 | 0.128843 | necr_b14s | 0.1288429 |
| CE | 1e-5/(c + 1) | 0.13228 | T2_H4A_v01 Table A2 | 0.1322800 |
| CE | 2e-5/(c + 1) | 0.130049 | T2_H4A_v01 Table A2 | 0.1300480 |
| original | 1e-6 | 0.070591 | necr_b14s | 0.0705900 |
| original | 1.4e-5/(c + 1) | 0.068215 | necr_b14s | 0.0682141 |
| original | 1e-5 | 0.066974 | necr_b14s | 0.0669731 |
| original | 1.7e-7 | 0.072754 | necr_at352 | 0.0727536 |
| original | 1e-40 | 0.101248 | necr_at352 | 0.1012474 |
| original | 1e-7 | 0.073346 | necr_at352 | 0.0733451 |
| original | 1e-60 | 0.149564 | necr_at352 (007 + b7 fails for R >= 1e-60) | 0.1021748 |
| original | 1e-60 | 0.231239 | necr_at352 (C5 + b7 fails for R >= 1e-60) | 0.1021748 |
| original | 3e-6 | 0.069026 | necr_b14s | 0.0690253 |
| original | 1.4e-5/(209/100) | 0.067707 | necr_b14s | 0.0677067 |

The tangent lower is a certified value of Phi at one M, printed as a float. For every row whose level is a printed
sup level (all rows except the source lowers 0.149564 and 0.231239), it shows that the level is sharp to the printed
digits. Since the AT-351 lowers 0.149564725... (007 + b7) and 0.231239122... (C5 + b7) exceed the levels at
R = 1.2e-9 and at every R, both registered b7 sources are excluded at every b0 for R >= 1.2e-9, in agreement with
AT-352 (R > 1e-7) and the first theory agent's note 23 item 2.

## 3. Envelope table (research/h4/necr_env.out, Part 2; CE input, kf = 1)

Table E1. Upper decimals of sup_M Phi(M; b0, R) (ceil_R.sup_phi, 6 decimals rounded up). Column "cap" is
b0 = c + 1 - q.

| R \ b0 | 0.55 | 0.58 | 0.60 | 0.62 | 0.64 | 0.66 | 0.68 | 0.70 | cap |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1e-9 | 0.089572 | 0.099672 | 0.106707 | 0.113983 | 0.121501 | 0.129260 | 0.137260 | 0.145502 | 0.149849 |
| 1e-8 | 0.087049 | 0.096872 | 0.103713 | 0.110790 | 0.118102 | 0.125649 | 0.133431 | 0.141449 | 0.145678 |
| 1e-7 | 0.084270 | 0.093790 | 0.100421 | 0.107281 | 0.114369 | 0.121685 | 0.129229 | 0.137002 | 0.141102 |
| 1e-6 | 0.081021 | 0.090194 | 0.096584 | 0.103195 | 0.110027 | 0.117080 | 0.124354 | 0.131848 | 0.135802 |
| 2e-6 | 0.079876 | 0.088929 | 0.095237 | 0.101763 | 0.108508 | 0.115470 | 0.122651 | 0.130051 | 0.133954 |
| 5e-6 | 0.078167 | 0.087046 | 0.093233 | 0.099634 | 0.106250 | 0.113081 | 0.120127 | 0.127388 | 0.131219 |
| 1e-5 | 0.076669 | 0.085398 | 0.091481 | 0.097776 | 0.104282 | 0.111001 | 0.117932 | 0.125075 | 0.128843 |
| 2e-5 | 0.074923 | 0.083480 | 0.089445 | 0.095618 | 0.102000 | 0.108591 | 0.115391 | 0.122400 | 0.126098 |
| 5e-5 | 0.072068 | 0.080352 | 0.086129 | 0.092110 | 0.098295 | 0.104684 | 0.111277 | 0.118075 | 0.121662 |
| 1e-4 | 0.069312 | 0.077340 | 0.082941 | 0.088742 | 0.094742 | 0.100942 | 0.107343 | 0.113944 | 0.117428 |

Use (Lemma ENV): take the smallest column b >= the certified rate bound used for b0 (cap if none is certified below
it) and the largest row r <= the certified radius lower (l/(c + 1) from a certified lower l of ||F||_2 when
beta0 <= c + 1). If the certified lower of N(F) is at least the entry, the CE P-S1 test is excluded at every rate up to
b and every radius from r. Between rows the table is conservative; necr_env.py screen evaluates the exact point.

At fixed R the level rises by about 0.0027 to 0.0042 per 0.01 of b0 (for example 0.096584 to 0.103195 from b0 0.60 to
0.62 at R = 1e-6). At fixed b0 it falls by about 0.0025 to 0.0114 per factor of 10 in R, more at larger R and larger
b0 (for example 0.141102 to 0.135802 from R = 1e-7 to 1e-6 at the cap).

## 4. Screen curve (research/h4/necr_env.out, Part 3; CE input, b0 = c + 1 - q)

Corollary SC (CLAIMED, Arb). Let n be a certified lower of N(F) = N_(21/10,1,1/2)(F), l a certified lower of
||F||_2, and beta0 <= c + 1. If l >= l*(n) of Table E2, the CE P-S1 test is excluded at every b0 <= c + 1 - q.
Proof. R >= l/(c + 1) >= R*(n), so by Lemma ENV sup_M Phi(M; b0, R) <= sup_M Phi(M; c + 1 - q, R*(n)) < n, the
last inequality certified by both methods (Arb tangent upper and branch-and-bound). QED.

Table E2. R*(n): the smallest two-significant-digit radius at which both methods certify sup Phi < n. At one unit
lower in the second digit, the certified tangent lower of sup Phi exceeds n (so R* is sharp to two digits).
l*(n) = (c + 1) R*(n), rounded up to two digits.

| n | 0.09 | 0.0911 | 0.0922 | 0.095 | 0.10 | 0.105 | 0.11 | 0.115 | 0.12 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R* | 1.2e-3 | 1.1e-3 | 1.1e-3 | 8.6e-4 | 6.1e-4 | 4.1e-4 | 2.6e-4 | 1.4e-4 | 6.7e-5 |
| l* | 3.4e-3 | 3.1e-3 | 3.1e-3 | 2.5e-3 | 1.8e-3 | 1.2e-3 | 7.4e-4 | 4.0e-4 | 1.9e-4 |

| n | 0.125 | 0.13 | 0.135 | 0.14 | 0.145 |
|---|---:|---:|---:|---:|---:|
| R* | 2.6e-5 | 7.3e-6 | 1.4e-6 | 1.7e-7 | 1.5e-8 |
| l* | 7.4e-5 | 2.1e-5 | 4.0e-6 | 4.8e-7 | 4.3e-8 |

For n >= 0.196790258489 (the every-R ceiling of T2_PS1_v01) every radius is excluded. For the AT-351 lowers this
reproduces the necr_at352 thresholds (0.149564: R >= 1.2e-9; 0.231239: every R).

## 5. Screen for one fit, and orientation for C5 + b14s

python3 research/h4/necr_env.py screen <n> <l> <rate> prints the upper and certified lower of sup_M Phi at
b0 = min(rate, c + 1 - q) and R = l/(c + 1). It reports EXCLUDED if the upper is below n. Otherwise, when the lower
exceeds n, it reports that NEC-R gives no contradiction. At the cap it also prints the B0-THR rate threshold (the
asserted bisection thr of b0_thr2.py). Examples in research/h4/screen_examples.out (stipulated inputs):

| n | l | rate | sup Phi | verdict |
|---:|---:|---:|---|---|
| 0.0911 | 1.4e-5 | cap | < 0.131231 | not excluded; excluded for b0 <= 0.5931582 |
| 0.0922 | 1.4e-5 | cap | < 0.131231 | not excluded; excluded for b0 <= 0.5966837 |
| 0.0922 | 1.4e-5 | 0.60 | < 0.093241 | not excluded at b0 = 0.60 |
| 0.11 | 1.4e-5 | 0.60 | < 0.093241 | EXCLUDED at every b0 <= 0.60 |
| 0.131 | 1.4e-5 | cap | < 0.131231 | not excluded; excluded for b0 <= 0.7097031 |
| 0.1313 | 1.4e-5 | cap | < 0.131231 | EXCLUDED at every b0 <= cap |

Reading for C5 + b14s (orientation only). The values N about 0.091 to 0.092 (polar N_2 and FFT-box N_(21/10), FLOAT,
the second numerics agent and the first theory agent's note 24; AT-356: not whole-plane bounds) and ||F||_2 = 1.4e-5 (FLOAT) are not certified. If they were
certified lowers, NEC-R would not exclude the CE P-S1 test, but a pass would need a rate b0 > 0.5931582 (N 0.0911)
or b0 > 0.5966837 (N 0.0922) (table above; compare Table A3 of T2_H4A_v01). By Corollary BUD-NEC of T2_H4A_v01 the
budget C^opt(b0) must then be below U(b0, R, n), which is small near the threshold (U < 2.92e7 at b0 = 0.60,
N = 0.091, ||F||_2 = 1.4e-5, beta0 <= c + 1; T2_H4A_v01 section 3). NEC-R alone excludes the test at these N values
only if a certified ||F||_2 >= 0.0031 is available (Table E2). The deciding inputs are
a certified whole-plane N(F), a certified P-S1 rate, and H4 (C^opt(b0)); H4 at P-S1 stays OPEN.

## 6. Requests

- The theory auditor: audit Lemma ENV, Corollary SC and Tables E1 and E2 (research/h4/necr_env.py; same terms as AT-335 and
  AT-352).
- The first numerics agent, the second numerics agent: for a new fit, apply Table E1 or the screen command with certified inputs only; with FLOAT inputs
  label the result as orientation.
- The first theory agent: Table E2 can replace the single-radius levels in theory_v06 T2.2 for new centers.
- The coordinator: ledger input. NEC-R levels at the AT-351 lowers re-enclosed by a second method (agrees with AT-352); the
  P-S1 CE screen for a new source is Table E1/E2 (CLAIMED, Arb); H4 at P-S1 remains OPEN.

## 7. Files and real run times (paths relative to the agent directory; core 40, nice 19, one thread)

| file | run (UTC, 2026-11-03) | exit | label |
|---|---|---|---|
| research/h4/necr_env.py, necr_env.out, run_env.log | 04:47:02Z to 04:50:41Z (last of five runs) | 0 | Arb |
| research/h4/screen_examples.out | 04:43:33Z to 04:43:34Z; 04:44:02Z (repeat); 04:45:01Z to 04:45:02Z | 0 | Arb |

- Earlier runs of necr_env.py: 04:42:38Z to 04:42:47Z (first version, with its own thr without asserts), 04:43:53Z to
  04:44:01Z (thr imported from b0_thr2.py), 04:44:09Z to 04:44:17Z (n = 0.0911 and 0.0922 added to Part 3), 04:44:27Z
  to 04:44:42Z (one source line rewrapped; output equal to the third run). The last run added the six remaining
  original-input levels to Part 1; most of its time is the branch-and-bound at the tight level 0.101248. Parts 2 and
  3 are unchanged code. Earlier outputs were overwritten.
- screen_examples.out: the first five examples ran with the first version and were repeated at 04:44:02Z with the
  imported thr (equal output, the repeat replaced the file); the last three were appended at 04:45:01Z.
- necr_env.py imports b0_thr.py and b0_thr2.py and through them research/ps1/ceil_R.py and ce_gen.py. The first theory agent's copies
  of ceil_R.py (necr_at352, necr_b14s) have the same SHA256 as research/ps1/ceil_R.py; their ce_gen.py differs from
  research/ps1/ce_gen.py only in one sys.path line.
