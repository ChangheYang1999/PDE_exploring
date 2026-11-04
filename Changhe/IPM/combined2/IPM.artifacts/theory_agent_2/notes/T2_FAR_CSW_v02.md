# T2_FAR_CSW_v02: Theorem CS-B transferred to the windowed far piece a_W of route F-a: S_h^B(a_W) <= 0.05970055144902641 at Rw = Ww = 200 (Corollary CS-W and Proposition DW, CONFIRMED conditionally by the theory auditor AT-1594 to AT-1596); errata to v01

Agent the second theory agent, written 2026-11-03 from 22:01:23Z. Supersedes notes/T2_FAR_CSW_v01.md (SHA256
45e8788e72aceaa76bbe62b1b7b6406c1a526c439c15e5279d7098b60bc961bb, unchanged). Recipients: the first theory agent (route F-a, notes 44
and 48), the coordinator (ledger row G3, X7 note item 5(d)), the theory auditor (audit_v486 follow-up). Code and run paths are relative to
research/h4/far009/ of agent the second theory agent, and notes/ paths to the agent directory. FLOAT numbers are sampled values used only for
comparison; no bound depends on them.

## 0. Summary

- Corollary CS-W (item 1; CONFIRMED, AT-1594): the certificate of Theorem CS-B depends on the field a only through the
  five energies D_s(a), s = 1, ..., 5, and is homogeneous of degree 1 in them. So D_s(a) <= lambda D_s^+ for every s
  gives S_h^B(a; 2 pi, 8 pi, h) <= lambda S^+, with the same h = <min(|xi|, 63/10)>^-1 and S^+ = 0.059699233948103884.
  The coefficients c_s of Lemma CS-S used here depend on |xi| only (qualification of AT-1481).
- Proposition DW (item 2; CONFIRMED, AT-1595, AT-1596): for the window of route F-a, a_W = a_f (1 - Sinf((r - Rw)/Ww))
  at Rw = Ww = 200, D_s(a_W) <= lambda^+ D_s^+ with lambda^+ = 1.0000220689753518 = 4503699017199667/4503599627370496.
  Hence S_h^B(a_W; 2 pi, 8 pi, h) <= S_W^+ = 0.05970055144902641 (binary64 upper of lambda^+ S^+).
- Both are conditional on the numerical application of Theorem CS-B (AT-1540, OPEN) and on the B1 records D_s^+
  (T2_FAR_CS_v02 item 2, CLAIMED; the theory auditor: "under containing-data assumptions", AT-1595).
- Route F-a at erflog 8, rho 1, Rw = Ww = 200 (item 3). The Hessian input is already certified for this window:
  SC(a_W) <= SC^+ = 4194197216881219/9007199254740992 = 0.46564943200002806 (Lemma SC-W, the second theory agent's notes 17:15Z; CONFIRMED,
  AT-1366, AT-1367; applies to this exact window, AT-1598). With OMF^+(a_t) = 0.11403919054571054 (CONFIRMED, AT-1336
  to AT-1338) the far condition at a certified strain bound s^+ = 137/125 is
      A_E^+ <= q (c - 137/125) - 0.17373975,   i.e.  A_E^+ <= 1.3263305,
  since SC^+ is below that bound. The open inputs of the row are A_E^+ (a certified upper of the band value A_E(a_W);
  FLOAT 1.1342736), the CS-B numerical application (AT-1540) and the strain bound s^+ (AT-1599, OPEN).

## 0a. Errata to v01

- E1 (the theory auditor's notes 21:35Z, AT-1598; X7 note item 5(d)). v01 section 3 lists "SC^+(a_W): OPEN (the C1 value
  0.46564943200002806 is for a_f and does not transfer, AT-1238)", section 4 lists "a transfer of SC^+ from a_f to a_W
  (AT-1238 stands)" among the things not given, and section 0 adds "and also SC^+(a_W) <= the same bound" as a
  condition. These are wrong. AT-1238 states that the oscillation upper survives any window but that no windowed
  Hessian estimate follows from it; Lemma SC-W (the second theory agent's notes 17:15Z) supplies that estimate, and the theory auditor CONFIRMS
  SC(a_W) <= 4194197216881219/9007199254740992 at the six windows of the tail table, Rw = Ww = 200 among them
  (AT-1366, AT-1367; transition bound T_W^+ = 0.000565214 there), and its application to this window (AT-1598). Only
  the outward display of the 17:15Z table was refuted (AT-1368; the stored JSON bounds are valid). The correct
  far condition is the single inequality A_E^+ <= 1.3263305 of item 3. The second theory agent's notes entry of 21:25Z repeats the
  error ("A_E^+, SC^+(a_W) (AT-1238) and s^+ stay OPEN"); the correct reading is "A_E^+ and s^+ stay OPEN", with the
  CS-B numerical application.
- E2 (AT-1597, REFUTED). The helper sinf_sup of code/c1/ds_window.py skipped the series piece when the clipped
  interval [max(tlo, d0), min(thi, 1 - d0)] is a single point and then returned 0 for every derivative (at t = 1/2,
  where Sinf'(1/2) = 2). code/c1/ds_window_v2.py evaluates that piece also when the interval is one point (the
  series is then taken at the one-point ball) and asserts sinf_sup(1/2, 1/2)[1] >= 2 at start-up. All five v01 runs
  were repeated with it at 21:58Z: the rows, lambda_upper, the G_j maxima and the cell counts are identical to the v01
  outputs at every window (Rw, Ww) = (200, 200), (50, 50), (100, 100), (200, 40), (8e6, 8e5); the JSON files differ
  only in the "code" field and, in two of them, in the recorded run time (0.1 s). So no window cell of these runs has
  a singleton t-range, as the theory auditor found for the 5120 cells (AT-1597), and every number of v01 stands.
- E3 (AT-1481; X7 note item 5(d)). v01 item 1 did not say that the coefficients c_s of Lemma CS-S are radial. They
  are: Theorem CS-B fixes them on each cell t0 <= |xi| <= t1 and on the tail |xi| >= 200 (T2_FAR_CS_v02 item 1), so
  they depend on |xi| only, which is the case in which the theory auditor CONFIRMS that the kernel integral and the CS upper are
  radial (AT-1479, AT-1481; AT-1480 REFUTED the reduction for direction-dependent coefficients).

## 1. Corollary CS-W (CONFIRMED, AT-1594)

Setting of Theorem CS-B (notes/T2_FAR_CS_v02.md item 1): K = 2 pi, K' = 8 pi, r_B as in T2_FAR_v02 section 2.3,
h(xi) = (1 + min(|xi|, 63/10)^2)^(-1/2), Sigma = {1, 2, 3, 4, 5}, D_s^+ the values of runs/ds_upper_1926.json
(SHA256 7e226057667bd1c3c2b6fd2e50d796133bde803ec5cdd2e858aff3dff62f57f5), S^+ = 0.059699233948103884.

Statement. Let a be real with a^ a function, and let lambda >= 0 with D_s(a) <= lambda D_s^+ for s = 1, ..., 5
(D_s = ||(-Delta)^(s/2) a||_2). If the CS-B certificate holds as stated (its cell uppers K^+ and the Lemma KT tail
upper; AT-1540 OPEN), then S_h^B(a; 2 pi, 8 pi, h) <= lambda S^+.

Proof. Lemma CS-S (T2_FAR_CS_v01 item 2) needs only that a is real, a^ is a function, h > 0 is measurable and
radial, and the D_s are finite; all hold. For every xi it gives
    rho_h^B(xi) <= (1/(4 pi)) (sum_s c_s(|xi|) D_s(a)^2)^(1/2) K(xi)^(1/2)
for any c_s(|xi|) >= 0, not all 0, depending on |xi| only (AT-1481). K(xi) depends on r_B, h and c only, not on a.
Take, on each |xi|-cell of the CS-B certificate and on its tail |xi| >= 200, the coefficients c_s of that cell (radial)
and the upper K^+ of K used there (cell file or Lemma KT). Then
    rho_h^B(xi) <= lambda (1/(4 pi)) (sum_s c_s D_s^+2)^(1/2) (K^+)^(1/2),
and the right side without lambda is the cell bound of CS-B, which is at most S^+ (CS-B item 4: S^+ is the largest
of these bounds). So rho_h^B(xi) <= lambda S^+ for every xi, and S_h^B(a) = sup_xi rho_h^B(xi) <= lambda S^+. QED.

## 2. Proposition DW (CONFIRMED, AT-1595, AT-1596): the energies of a_W

a_W = w(r) a_f with w(r) = 1 - Sinf((r - Rw)/Ww), Sinf(t) = e0/(e0 + e1), e0 = exp(-1/t), e1 = exp(-1/(1 - t)) on
0 < t < 1, Sinf = 0 for t <= 0 and Sinf = 1 for t >= 1 (code/hsb_far.py). a_f is the complete 013 far piece at
erflog 8, rho 1 (unwindowed, every angular mode), as in code/c1/ds_upper.py. a_W is bounded with compact support,
so a_W^ is a continuous function and every D_s(a_W) is finite.

Bound. For m = 1, ..., 5:
    D_m(a_W)^2 <= E_I,m + sum_(inner cells) Phi_m,c^+ A_c + sum_(window cells) (sum_(j=0..m) binom(m, j) G_j,c
                  (Phi_(m-j),c^+)^(1/2))^2 A_c,
with A_c = pi (e^(2 yhi) - e^(2 ylo)) the area of the y-cell [ylo, yhi] (y = log r), and:
- E_I,m: the region r <= e^-4 of runs/ds_upper_1926.json (w = 1 there).
- Phi_k,c^+: the cell uppers of the angular mean of |grad^k a_f|_F^2 in runs/tail_deriv_1905.jsonl (-4 <= y <= 3.75)
  and runs/tail_deriv_1557.jsonl (3.75 <= y <= 16), the records of D_s^+. They cover [-4, 16] without gaps or
  overlaps (asserted), and e^16 > Rw + Ww.
- Inner cells: e^yhi <= Rw (w = 1). Window cells: the others with e^ylo < Rw + Ww. Cells with e^ylo >= Rw + Ww and
  the region r >= e^16 carry w = 0. The comparisons are decided in arb.
- Leibniz: d_(i_1 ... i_m)(w a) = sum over subsets S of {1, ..., m} of (d_(i_S) w)(d_(i_(S^c)) a). Each term is an
  index permutation of grad^|S| w (x) grad^(m-|S|) a, whose Frobenius norm is |grad^|S| w|_F |grad^(m-|S|) a|_F. So
  |grad^m (w a)|_F <= sum_j binom(m, j) |grad^j w|_F |grad^(m-j) a|_F pointwise, and Minkowski on each cell gives
  ||grad^m (w a)||_(L^2(c)) <= sum_j binom(m, j) G_j,c (Phi_(m-j),c^+ A_c)^(1/2) with G_j,c >= sup_c |grad^j w|_F.
- G_0,c = 1 - Sinf(t_lo) >= sup_c w (Sinf is increasing: Sinf = 1/(1 + exp(1/t - 1/(1 - t))) and 1/t - 1/(1 - t)
  is decreasing), with t_lo a lower end of (r - Rw)/Ww on the cell.
- For j >= 1 (Faa di Bruno for w(|x|), x != 0): d_(i_1 ... i_j) w(r(x)) = sum over set partitions pi of {1, ..., j}
  of w^(|pi|)(r) prod_(B in pi) d_(i_B) r, and each product is a permuted tensor product. So
      |grad^j w|_F <= sum_pi |w^(|pi|)(r)| prod_(B in pi) n_|B| r^(1 - |B|),
  where n_b = |grad^b |x||_F at |x| = 1 (grad^b |x| is homogeneous of degree 1 - b and rotation covariant):
  n_b^2 = 1, 1, 3, 33, 765 for b = 1, ..., 5 (exact, sympy). The partition counts 1, 2, 5, 15, 52 are asserted.
  w^(k)(r) = -Ww^(-k) Sinf^(k)(t), and r is replaced by the cell ball [e^ylo, e^yhi].
- sup |Sinf^(k)|, k = 1, ..., 5, on the t-range [t_lo, t_hi] of a cell (clipped to [0, 1]; all derivatives vanish
  outside):
  - on [d0, 1 - d0], d0 = 2^-10: arb_series of Sinf with the constant term a ball of width at most 2^-12; the k-th
    coefficient times k! encloses Sinf^(k) at every point of the ball. The piece [max(t_lo, d0), min(t_hi, 1 - d0)] is
    evaluated whenever it is nonempty, including when it is one point (v2; erratum E2);
  - on (0, d0]: Sinf is analytic on the closed disc |z - t| <= t/2, where Re(1/z) >= 2/(9t) (Re z >= t/2,
    |z| <= 3t/2) and |1 - z| >= 1 - 3t/2, so |e0(z)| <= exp(-2/(9t)) < exp(-1/(1 - 3t/2)) <= |e1(z)| and
    |Sinf(z)| <= exp(-2/(9t))/(exp(-1/(1 - 3t/2)) - exp(-2/(9t))). Cauchy's estimate gives
        |Sinf^(k)(t)| <= k! (2/t)^k exp(-2/(9t))/(exp(-1/(1 - 3t/2)) - exp(-2/(9t))).
    For t < 2/(9k) the factor t^(-k) exp(-2/(9t)) increases, and the denominator decreases, so the value at
    t = d0 bounds the whole interval (asserted: d0 < 2/45). These values are below 1.8e-80 for k <= 5;
  - on [1 - d0, 1): the same, since Sinf(1 - t) = 1 - Sinf(t).
Arithmetic: arb balls (python-flint 0.9.0, 160 bits), uppers rounded up to binary64. Every number is finite and every
*_upper is >= 0 (checked before serialization).

Result at Rw = Ww = 200 (code/c1/ds_window_v2.py, SHA256
2fb5c6a64a9a0225f960c6cbadbbf7355e6ef31f9091807f9f9fa5c8828c9807; command
`python3 code/c1/ds_window_v2.py 200 200 runs/ds_upper_1926.json runs/ds_window_v2_2158.json
runs/tail_deriv_1905.jsonl runs/tail_deriv_1557.jsonl`, 21:58:23Z, 0.4 s, core 41; output runs/ds_window_v2_2158.json,
SHA256 e26aeb71eadadf209a0140d50d8e9339aa1c8a3985e96cb8862893c3377abf6a; log runs/ds_window_v2_2158.out). The v01
run (code/c1/ds_window.py, runs/ds_window_2118.json, 21:18:55Z) gives the same rows. Cells: 2380 inner, 178
window, 2562 outside.

| m | D_m^+(a_W) | D_m^+(a_f) (record) | ratio upper | window part of D_m^2 | FLOAT FFT D_m(a_W) |
|---|---|---|---|---|---|
| 1 | 2.10745911935 | 2.1163361261353364 | 0.995805484 | 0.0831 | 2.0965 |
| 2 | 1.08113872959 | 1.0811148704835174 | 1.000022069 | 7.47e-5 | 1.0772 |
| 3 | 1.38998259614 | 1.3899825385469313 | 1.000000042 | 1.79e-7 | 1.38302 |
| 4 | 3.34556428149 | 3.34556428129887 | 1.000000001 | 1.31e-9 | 3.32147 |
| 5 | 12.48188668592 | 12.481886685910556 | 1.000000001 | 5.57e-11 | 12.3026 |

The certified columns are the binary64 uppers of the JSON rounded up to the printed digits. lambda^+ =
1.0000220689753518 (m = 2). The last column is the FLOAT FFT of a_W at N 6912, Rw 200, Ww 200 (8 modes;
T2_FAR_CS_v01 item 3); every entry is below the certified upper.

Other windows (code/c1/ds_window_v2.py, outputs runs/ds_window_v2_2159_<Rw>_<Ww>.json, identical rows to the v01
outputs runs/ds_window_2119_<Rw>_<Ww>.json): lambda^+ <= 1.00130449608 (Rw = Ww = 50), 1.00016908141 (Rw = Ww = 100),
1.00538389962 (Rw 200, Ww 40; all rounded up). Check run with Rw = 8e6, Ww = 8e5 (w = 1 on almost all of the record):
lambda^+ = 1, and D_m^+(a_W) equals D_m^+(a_f) for m = 2 to 5 to all printed digits and is below it for m = 1 (the
region r >= e^16 is dropped).

Proof of Proposition DW. Each term of the bound is an upper of the corresponding part of D_m(a_W)^2 by the items
above, the parts cover R^2, and the run evaluates the bound in arb with outward rounding. QED.

## 3. Consequence for route F-a (AT-911; corrected, erratum E1)

AT-911 (CONFIRMED) gives A_*(a_W + a_t) <= max(SC^+, A_E^+) + S^+ + OMF(a_t) with S^+ any certified upper of the
Schur remainder S_h^B(a_W) of Lemma HSB at K = 2 pi, K' = 8 pi with h measurable and positive; the theory auditor CONFIRMS that
the weight h of CS-B is admissible there (AT-1598, conditionally). The inputs of the row at Rw = Ww = 200 are:
- S^+ = S_W^+ = 0.05970055144902641: Corollary CS-W with Proposition DW (CONFIRMED conditionally, AT-1594 to AT-1596;
  conditional on AT-1540);
- SC^+ = 4194197216881219/9007199254740992 = 0.46564943200002806 >= SC(a_W): Lemma SC-W (CONFIRMED, AT-1366,
  AT-1367, AT-1598);
- OMF^+(a_t) = 0.11403919054571054 (CONFIRMED, AT-1336 to AT-1338);
- A_E^+ >= A_E(a_W) (route (a) band upper; needs a certified majorant of |a_W^|): OPEN; FLOAT 1.1342736;
- the strain bound s^+ (item B): OPEN (AT-1599).
S_W^+ + OMF^+ = 0.17373974199473695 < 0.17373975, so the far condition is max(SC^+, A_E^+) <= q (c - s^+) -
0.17373975; at s^+ = 137/125 (q (c - s^+) = 1.50007034141999...) it is max(SC^+, A_E^+) <= 1.3263305, and since
SC^+ < 0.4657 it reduces to A_E^+ <= 1.3263305 (the theory auditor: the sufficient budget, AT-1596, AT-1598). With the FLOAT
A_E = 1.1342736 the far value is 1.3080133 (FLOAT), margin 0.192057 to G(137/125), level c - A/q = 1.18746.

## 4. What this does not give

- Row C2 of Proposition F (a certified A_low^+(8 pi)) and every other band upper: Corollary CS-W bounds only the
  Schur remainder S_h^B. In particular A_E^+ is not given.
- The numerical application of CS-B (AT-1540, OPEN), on which S_W^+ depends.
- Any bound at strain 3/2 on route F-a: at Gbar = 0.65167 the FLOAT far value 1.308 fails.
- Closure of O3 at source013 (AT-1593, AT-1599, OPEN).

## 5. Audit status (the theory auditor audit_v486, 21:43:29Z, and earlier)

| item | verdict |
|---|---|
| Corollary CS-W (transfer through D_s(a) <= lambda D_s^+) | CONFIRMED, AT-1594 |
| Proposition DW (five energies of a_W from the origin and cell data) | CONFIRMED, AT-1595, under containing-data assumptions |
| DW scalar output (lambda^+, S_W^+) and the sufficient far budget | CONFIRMED, AT-1596 (copied 160-bit replay and independent 256-bit assembly, 15837 checks) |
| helper sinf_sup on singletons (v01) | REFUTED, AT-1597; fixed in v2 (erratum E2), outputs identical |
| admissibility of h in HSB and SC-W for this window | CONFIRMED, AT-1598 |
| unconditional Schur, far or existence certificate | OPEN, AT-1599 |
| radial coefficients in Lemma CS-S | CONFIRMED, AT-1481 (AT-1480 REFUTED the direction-dependent case) |

## 6. Files

- code/c1/ds_window_v2.py 2fb5c6a64a9a0225f960c6cbadbbf7355e6ef31f9091807f9f9fa5c8828c9807
- runs/ds_window_v2_2158.json e26aeb71eadadf209a0140d50d8e9339aa1c8a3985e96cb8862893c3377abf6a
- runs/ds_window_v2_2158.out 79c2423e294632f0fbd2f3f2cdf843ff7d17ee86d6e0c7008c83c165f510c3bf
- runs/ds_window_v2_2159_50_50.json 6bcc07f7f9d0cc893bf1bbe3639d43524df180e4f6460c2f11b0cbf0525d9d66
- runs/ds_window_v2_2159_100_100.json 604bc729616a6b2c7f1eae5a8242baaecfd83686f5b730feff53de2eb42ed3cf
- runs/ds_window_v2_2159_200_40.json 39e55861d0356c0a46c7211b72c05db8256fc53f065a68ede4b72ece7c8ec706
- runs/ds_window_v2_2159_8000000_800000.json a346ed09c072ca1af90f0cab4df44b977080beff549afe3969af8a87593d020d
- runs/ds_window_v2_2159_others.out 3ce7463981f4df171a095113f43cd5c4f7f5deab74783be9791a87d49b7a4a79
- code/c1/ds_window.py ff2ec815d694db9e252cb178224237738273af2369fd79c892efcacb457d9d07 (v01, kept)
- runs/ds_window_2118.json 09e8dea1d990a85c9b6d6535e4618fcfeb0226baa4873a1a0c02816e713e437a (v01 output)
- runs/ds_upper_1926.json 7e226057667bd1c3c2b6fd2e50d796133bde803ec5cdd2e858aff3dff62f57f5
- runs/tail_deriv_1905.jsonl e483c240360adad7a0fb2712826c43c2765832676ce324e14fc08e3e466526ec
- runs/tail_deriv_1557.jsonl ae179b9d78296b694b7006a45d329d3a83bc41258c3e2c3310b00b602c99a98d
