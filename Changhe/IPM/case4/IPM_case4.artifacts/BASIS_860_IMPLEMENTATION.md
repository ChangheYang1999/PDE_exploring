# BASIS_860_IMPLEMENTATION.md (numerics lane) — design text, version 2 (2026-10-24T04:02Z, pre-G2; aligned with SPEC v5)

Status: this is the implementation contract I will code and test once the lead releases G1 and G2. It follows
`c4-lead/SPEC.md` v5. Nothing in this document is evidence; the pre-G1 drafts under `work/research860` (basis860.py,
origin860.py, chart860.py, fields860.py, model860.py, integrate860.py and tests, written 03:21Z to 03:36Z and partly
executed before the lead's stop at 03:32Z) used a pure-power low block and exact sqrt(2n+1) normalizers; both are
superseded by the choices below. They will be rewritten, their file hashes recorded, and every gate rerun.

## 1. Family, canonical order, manifest

gamma = 1/c_l, lambda = 1 - gamma, p_j = (3 + gamma - j lambda)/2 (j = 0..3), R = 1 + r^2, t = r^2/R, H_m = Re (x+iy)^(2m).

    chi_{m,k,j} = r^(2k) R^(p_j - k) cos(2 m theta) = H_m q^(k-m) R^(p_j - k) = H_m R^(p_j - m) t^(k - m),
    m = 0..9,  k = m..25,  j = 0..3;  count 4 * sum_m (26 - m) = 860.

Canonical zero-based order j, then m, then k: I(j,m,k) = 215 j + 26 m - m(m-1)/2 + (k - m). The manifest
(`campaign860/seed/manifest_860.json`) lists all 860 triples with I, the formula string, the c_l binding of the seed,
the derivative version (d chi/d c_l = p_j' log R chi, p_j' = -(j+1)/(2 c_l^2), at fixed raw a), the T1 matrix version
and the 26 host-frozen N_n as hex strings.

## 2. Internal coordinates c (T1), a = T c, exact and c_l independent

Per (m, j) block, with v_m = max(m, 5):

- Low block (m <= 4, k = m..4; 15 per j, 60 total): raw monomials, c_{mkj} = a_{mkj}. Internal low-block order:
  L(j,m,k) = 15 j + (5m - m(m-1)/2) + (k - m); L = 0 is a_{000} (the center-eliminated coefficient).
- High block (k = v_m..25; 26 - v_m per (m,j), 200 per j, 800 total): E_{mnj} = R^(p_j) t^(v_m) N_n P_n(2t - 1) cos(2 m theta)
  = H_m R^(p_j - m) t^(max(5-m,0)) N_n P_n(2t - 1), n = 0..25 - v_m, so a_{m, v_m + h, j} = sum_n c_{mnj} N_n (-1)^(n-h) C(n,h) C(n+h,h).
  Internal high-block order: j, then m, then n (index 200 j + eoff(m) + n, eoff(m) = sum_{m'<m} (26 - v_{m'})).
  N_n are the frozen binary64 values of the old source expression (`spectral_basis._radial`: SciPy gammaln, math.log,
  math.exp; N_0 from the n = 0 branch) as computed on this host by the pinned environment (lead measurement
  `c4-lead/checks/source_Nn_pinned.json`: up to 25 ulps from sqrt(2n+1), N_0 = 1 exactly). Their exact real values
  (hex) enter the 85-digit identity tests; the production evaluator reproduces them because it calls the frozen
  `evaluate_modes` with mode dictionaries `{'family':'global','m':m,'n':n,'sigma':s_j}`, s_0 = 0.0 (float, byte-identical
  to the old modes) and s_1..3 = 'delta','2delta','3delta' (old `tail_exponent`: sigma = j (1 - 1/c_l)/2 with derivative
  j/(2 c_l^2), which is exactly p_0 - p_j).

T is block upper-triangular: low-block identity; high block per (m,j) the (26 - v_m) x (26 - v_m) Legendre-to-monomial
matrix with diagonal N_n C(2n,n) != 0. T^{-1} by back substitution in Decimal at 60 digits. Tests: T^{-1} T = I (max
entry) in Decimal 60 and 110 digits; every T1 generator equals its monomial expansion at random points in 85- and
110-digit arithmetic (Decimal; mpmath if the lead prefers, via the system interpreter) with tolerance
|difference| <= 1e-40 max(|value|, 1e-30) (SPEC section 9).

Why T1: raw monomial coordinates in one block are a power basis on [0,1] (Gram condition > 1e23 for 17 functions,
> 4e36 for 26; lead and astra agree); the accepted278 Global part maps to |a| up to 1.056e6 with block sums down to
1e-7 (lead check). In T1 the old 162 Global coordinates are literally internal coordinates (one to one) and the
Jacobian conditioning is that of the old Legendre family plus the new branches.

## 3. Old-to-new map B (from the actual old source), seed of the campaign

Old core b_{m,s}: generator H_m R^(p_0 - m - sigma_s), sigma = (0, 1, 2, lambda/2, lambda, 3 lambda/2), order (m,s)
m = 0..3, s = 0..4 then (m,5) m = 0..3 (`absolute_fields.CORE_ORDER`); index 0 is c0, analytic (90-digit value from
`_decimal_center`). Old Global g_{mn} from the saved `modes` of accepted278 (162 entries, (3,0) absent, (9,0) last).

1. s = 0, 1, 2: a_{m, m+h, 0} += b_{m,s} (-1)^h C(s,h), h = 0..s (uses (1-t)^s = R^{-s}).
   For (m,s) = (3,2) the h = 2 term is a_{3,5,0}, a high-block coefficient: in T1 it is c_{3,0,0} += b_{3,2} (N_0 = 1,
   old Global (3,0) was omitted from the 162 precisely because it equals this combination). So (3,2) is the three-term
   map a_{330} += b, a_{340} -= 2b, c_{300} += b. All other 23 old core functions are single low-block coordinates.
2. s = 3, 4, 5: a_{m, m, s-2} += b_{m,s} (branches j = 1, 2, 3, k = m).
3. Global: a_{m, v_m + h, 0} += g_{mn} N_n (-1)^(n-h) C(n,h) C(n+h,h); in T1 simply c_{m,n,0} = g_{mn}.

Identity to test (SPEC section 9): the eliminated a_{000} recomputed from the center condition equals b_00 + b_01 + b_02
to <= 1e-80 in >= 90-digit arithmetic; lead reference a_000 = -3.611632420753814241569187726598932770153,
low-block max |a| = 20.1129691482296 at (m,k,j) = (0,0,3), c_{300} = 2.71426820986126967911317153792e-4,
W_x = 2.7795669555872, W_y = 2.20529251441704. The manifest reproduces these to >= 40 digits.

Seed: `campaign860/seed/seed_860.json` (internal c as hex-exact floats, raw a as 50-digit decimal strings plus float64,
c_l, analytic a_000, source hashes, manifest hash) and `seed_860.npz` (c, a, and the Linux production residual on the
training mesh, which becomes the strict 64-eps replay reference per SPEC section 15). Immutable after writing (sha256
in the campaign state).

## 4. Field evaluation (production and independent)

Common: normalized coordinates xn = x/sqrt(R), yn = y/sqrt(R), t, u = 1/R, s = log R, as in the frozen code; harmonic
derivatives and analytic y-quotients from the frozen `_harmonics` (now m up to 9); assembly of f, f_x, f_y, psi, psi_x,
psi_y, psi_x/y from the radial jets F_0..F_4 (g^(j)(R) = R^(beta - j) F_j) by the frozen `_assemble`, then the factor
R^(beta_eff - order) with the orders (f 2, f_x 2.5, f_y 2.5, psi 1, psi_x 1.5, psi_y 1.5, ratio 2).

- High block: frozen `spectral_basis.evaluate_modes` unchanged (stable Legendre recurrence via `eval_jacobi`, analytic
  t-derivatives through the Stirling conversion, analytic d/dc_l including d sigma/d c_l). Production uses the private
  scalar-exp namespace of `stage13_stable_exp` for bitwise same-host replay; the independent evaluator uses the original
  NumPy namespace.
- Low block: radial function R^(p_j - m) t^h, h = k - m <= 4. Radial jets by the same route as the frozen `_radial` with
  the Legendre factor replaced by 1: t-power derivatives of t^h (`_t_power_derivatives`), Stirling conversion to
  R-derivatives (`_s_from_t`), then the beta-recursion with beta = p_j - m and d beta/d c_l = p_j'. This evaluates t^h
  directly (no (1-t)^i alternating expansion), so there is no cancellation near r = 0.02 where t is 4e-4.
- Origin (r <= 0.02): order-20 Decimal Cartesian polynomials for every field and raw derivative (production), orders
  20 and 24 for the independent origin integral, built with the frozen `potential_polynomial` (core_offset =
  (j lambda/2 + (k-m)... ) — note: for a monomial generator the polynomial is H_m q^(k-m) sum_l C(p_j - k, l) q^l, which
  the frozen routine produces for `core_offset` = (p_0 - p_j + k - m, derivative) applied to H_m R^(p_j - k) and then
  multiplied by q^(k-m); I will add a small exact wrapper) and `mode=` for the high block. Residual polynomial and the
  860 derivative polynomials exactly as in `highprecision_origin.residual_series` (analytic center chain included).
- Center: a_{000} = (1 - c_l - sum' s_i a_i)/(4 p_0 (p_0 - 1)) in Decimal at precision 90 from the exact binary inputs,
  strains s: (0,0,j) 4 p_j (p_j - 1); (0,1,j) 8 (p_j - 1); (0,2,j) 8; (2,2,j) -24; all others 0 (verifier and lead agree).
  q = c_l - 1 + psi_x/y is formed center-safely as sum_i a_i (ratio_i - s_i) over the low block plus the high-block
  ratio sum, as in the frozen `fields`.
- Residual R_f = w_x f_x + w_y f_y + q f; raw Jacobian columns [c_l, 59 low a (without a_000), 800 high c]; the c_l column
  carries d/dc_l of every generator, the a_{000} chain (d a_000/d c_l and -s_i/s_0 for the low coefficients) and the
  explicit x f_x + y f_y term; identical structure to `stage13_model._evaluate`.
- Cache: as `CachedAbsoluteProblem`: six field matrices and six c_l-derivative matrices (direct nodes x 860) at one exact
  c_l, q-core matrix, exact byte keys; memory 12 x 88,320 x 860 x 8 B = 7.3 GB on the training mesh (within the 40 GB
  lane policy). Point blocks 4096, mode blocks 64 (to be benchmarked). workers = BLAS threads (planned 8 of 12).

## 5. Chart (c_l + 59 low coefficients -> 55), feasible dimension 855

Mirror of `AbsoluteC5ChartV2`: jets (a,b,c,d,e,g; h,u,v,w,z,k) of the 60 low generators from the degree <= 8 part of
their binomial series (generalized `taylor_jet.series`, float/complex and Decimal); constraint values E_x, E_y, D_1, D_2,
D_3 of SPEC section 7; constraint Jacobian by complex step in all 60 raw parameters; row scaling by coefficient-row
norms; right-inverse normals from the SVD of the 5 x 59 coefficient block (zero c_l row, c_l bit pattern preserved by
the lift); 55 free seeds from the right null space of the row-scaled 5 x 60 matrix; tangent T = F - N (G N)^{-1} G F;
Newton lift with backtracking, target 3e-12, tolerance 1e-10; refuse on unresolved rank. Bounds 1.02 <= c_l <= 10 and
the declared safety box |a| <= 100 on the 60 low coefficients; no bound on the 800 high coordinates. Reported:
constraint rank 6 (center + C5 with the c_l column) and 5 after elimination, singular values with the gap, tangent
rank 55, complete rank 60, old 19 tangent directions inside the new 55 (via the embedding), feasible dimension
855 = 55 + 800 as the rank-based local count (SPEC section 7; exceptional c_l = 2, 3 audited by a rank scan).

## 6. Independent integration and acceptance (unchanged semantics)

Port of `stage13_integration_v2.independent_integral` and `EpochIntegrator.validate` to the new representation with the
stateless evaluator: origin orders 20/24 analytic disk integral, 85-digit overlap at r = 0.02 and angle 7 pi/32
(`basis_tests.Jet` point-centered Cartesian algebra over the 60 + 800 generators), outer envelope from absolute
coefficient sums (frozen `assembled_field_bounds` for the low block with power p_j - order, frozen `mode_field_constants`
for the high block), interval expansion from log r = 44 in steps of 8 until envelope < target/16, radial Gauss 16/32/64/128
until successive difference < target/2, 96-node Gauss against 128-interval trapezoid angular check, error budget =
radial + angular + origin + envelope + 256 eps |J|. Epoch policy from the frozen epoch record: absolute target 2.5e-15,
relative accuracy 2.5e-7, initial upper log radius 44; training/refined three-block comparison as in `validate`.
Acceptance exactly as SPEC section 11 (gain > 0.1, uncertainty <= 5% of prediction, independent decrease > uncertainty,
KKT <= 1e-8 else diagnosis stop, radius rules, 12-rejection stop, precision floor, stationarity-indicator stop).
Solver: frozen `stage13_solver.DenseTrustModel` (full thin gesdd SVD, all positive directions, secular bisection in
long double) applied to the column-scaled 90,624 x 855 matrix; column scales = inverse initial column norms, fixed per
epoch; LSMR comparison kept as a diagnostic only.

## 7. Campaign, durability, supervisor

`campaign860.py`: state.json, immutable snapshots (JSON + NPZ with c, a, residual), trial proposals saved before
validation, immutable outcome records, event commits with post-state, recover() with the strict 64-eps Linux replay,
SIGTERM/STOP-file graceful stop between trials, `--seconds` slice budget, per-trial wall/CPU/RSS, source hash binding of
`work/research860/*.py` and the frozen closure. Supervisor `supervise860.sh`: setsid nohup loop, each slice under
`hardware/guard.py run` with a dedicated policy (RSS ceiling 40 GB, 3500 s per slice), heartbeat file every slice and
every trial, backoff on failures, STOP file honoured, affinity inherited (CPUs 78-89), nice +15 from the guard.
Independent assessments (32 regions, refined maxima, near-origin bands, far-field E_1/E_2/E_3 and tail moments, C5 in
high precision, W_x, W_y) at the seed, at halvings of J_abs, every 100 accepted steps and at the end.

## 8. Gate plan and tolerances (fixed before the runs; SPEC sections 9, 10, 16)

G2: identities at 85 and 110 digits (<= 1e-40 relative with 1e-30 absolute floor); embedded seed production residual vs
181D on training and refined meshes (||dr|| <= 1e-9 ||r||, max |dR_f|/a_ref <= 1e-12); a_0 relative <= 1e-13; fields and
c_l derivatives at c_l in {accepted278, 1.5, 2.5, 4.0} with random old coefficient vectors, band-scaled <= 1e-11; raw C5
defects <= 1e-12; independent J_abs within 1e-9 J + (e_860 + e_181) with the integrals tightened until conclusive;
refined maxima within 1e-10 relative; Jacobian chain rule column by column <= 1e-9 relative plus 1e-13 absolute floor;
a_000 identity <= 1e-80; strict same-host replay of the seed.
G3: constraint singular values; FD at relative steps 1e-4, 1e-5, 1e-6 in c_l, low tangent, high (small/large k, all j),
weakest right singular vectors, projected dilation D (tangency compared with (0,0,-2E_x,-2E_y,-4D_1,-4D_2,-4D_3));
zero-step equality; full 855 spectrum.
G4/G5 as SPEC section 16 (benchmarks at 1/4/8/12 threads, pilot >= 10 trials, SIGTERM and SIGKILL restarts, disk
projection, verifier re-evaluation), then the detached long run with an ETA from measured throughput.

## 9. Amendments for SPEC v5 (04:02Z)

- u = 1/R is always formed directly as 1/(1 + r^2), never as 1 - t (the frozen code already does this: u = 1/R).
- High-precision references (identities, infinity-block spots, overlap at r = 0.02) use my own Decimal evaluator with the
  frozen binary64 N_n on both sides; the handoff's `highprecision_origin` and `basis_tests` helpers use the ideal
  sqrt(2n+1) and are not references for the 1e-40 gates. The production origin series (r <= 0.02) is likewise built with
  the frozen N_n (exact Decimal of the binary64 constant) so that the production potential is one consistent function;
  this differs from the old production origin series (ideal sqrt) by about 3e-15 relative in the Global part, far inside the
  G2 residual tolerance, and is recorded as a deliberate consistency choice.
- Infinity block: the production evaluator's accuracy at r > e^16 (training nodes r = e^16/u) is measured directly against
  the 181D code and against 50-digit spots at e^24, e^32, e^44 (EMBEDDING_TESTS T2.5, T2.6); raw low-block monomials may lose
  relative accuracy there while staying inside the absolute envelope, and the measured values are reported.
- Trial feasibility exactly as the baseline `feasible_trial`: converged C5 lift (target 3e-12), raw C5 maximum < 1e-10,
  bounds (c_l box and the declared |a| <= 100 low-block box), |a_0| > 1e-12, finite fields/residual/column norms; failures are
  rejections with reasons lift/C5/bound/a0/nonfinite and radius x0.25. KKT > 1e-8 and a nonpositive or precision-floor
  prediction are stops with a diagnosis record, not rejections.
- Dilation monitoring per SPEC section 6: W_x, W_y, l, eta logged at every acceptance with the ten-step drift warning as an
  event; the projected D, its k = 26 leakage and its column-scaled comparison with the singular vectors at the seed and at
  assessments.
- Supervisor: restarts only after process faults; never past a scientific or correctness stop (KKT diagnosis, precision
  floor, needs_mesh_refinement, 12 consecutive rejections, stationarity indicator); those stop the loop and leave a
  STOPPED_FOR_DIAGNOSIS marker for the lead.
- G5 release requires at least one accepted pilot state independently verified; disk growth projected over the configured
  remaining budget (at least 72 h) with a 2x margin.

## 10. Repair under SPEC v7 (2026-10-24T05:30Z): origin order 40, stable linear transport, extended-precision high block

Two production-accuracy defects of the first implementation were confirmed by the verifier (c4-ver NOTES 04:41Z to 05:12Z) and
are repaired, not tolerated (SPEC v7 section 5a):
- Origin series: production order 40 (potential degree 44), integrator disk orders 40/44 (origin860.ORIGIN_ORDER). The verifier's
  rational truncation certificate bounds the order-40 truncation by 5.5e-15 of the origin-band scale for all generators, fields and
  c_l derivatives at both c_l values.
- Stable linear transport: for nodes with r >= r_s = 2 (basis860.R_SWITCH, recorded in the manifest) the linear part of R_f and of
  every raw Jacobian column uses L F(chi_mkj) = -j (c_l-1) F(chi) + 2 c_l (k - p_j) F(u chi), u = 1/R. Low block: the remainder is the
  monomial with exponent lowered by one, coefficient (k - p_j). High block: remainder = H_m R^(p_j-m-1) t^w N_n [(w + m - p_j) P_n(z) + 2 t P_n'(z)],
  z = 2t - 1 (derivative form; the P_{n-1} - z P_n difference is not used). The c_l column of the stable form is the derivative of the
  identity: sum_i a_i [-j f_i - j(c_l-1) d f_i/dc_l + 2 f_rem,i + 2 c_l d f_rem,i/dc_l] plus the a_000 chain, where d f_rem/dc_l
  includes the coefficient terms (-p_j' for the low block, -p_j' T for the high block) and the exponent/log chain. Inside r_s the
  center-safe form is kept. The matrices f_rem and d f_rem/dc_l are cached next to the six field matrices (basis cache 14 x N x 860).
- Extended-precision high block: basis860.high_matrices evaluates the 800 T1 generators in numpy longdouble (own Legendre derivative
  recurrences from the differentiated Bonnet relation; frozen _harmonics, _s_from_t, _assemble accept longdouble arrays; frozen N_n;
  longdouble exp is deterministic), returning float64. Reason: the frozen float64 evaluate_modes misses the per-generator 1e-11
  band criterion for some high-(m,n) derivative fields (verifier: seven non-origin cases up to 1.9e-10). The low block keeps the
  frozen float64 route with the scalar-exp proxy (all 60 low generators passed).
- Consequence for the seed: the coefficients are unchanged; the production residual (Linux replay reference) is regenerated by the
  repaired evaluator and its difference from the g2_v1 vector is reported (SPEC v7 section 5a). Gates T2.7, T2.6b, T2.6c at the
  unchanged tolerance 1e-11 max(band_max, 1e-30), and an origin truncation monitor (order 40 vs 48 at r = 0.02) in every assessment.


## 11. SPEC v9 / v9.1 / v9.2 / v9.3 repair: extended-precision R_f, exact exponents, centered q (2026-10-24T06:43:11Z)
### 11.1 Exact exponent differences (v9.1)
p_j = (3 + gamma - j lambda)/2 with gamma = 1/cl, lambda = 1 - gamma gives p_j - s = ((3 - j - 2s) cl + (j + 1))/(2 cl) for integer or half-integer s (basis860.pdiff). At cl = 2 the branch j = 3 has p_3 = 1 and at cl = 3 the branch j = 2 has p_2 = 1; the numerator is then an exact integer zero, and next to it (cl = 2(1 +- 2^-k)) the difference keeps full relative accuracy because 2(1 +- 2^-k) cl - 4 is exact in binary floating point. Every exponent on the evaluation path (radial exponents beta - l, the R-power factors p_j - order, the strain factors p - 1, p - 2, the series exponents p_j - k in the Decimal origin polynomials and in the hp860 reference jets, the binomial factors of the Taylor jets) is formed this way. dp_j/dcl = -(j + 1)/(2 cl^2).
### 11.2 Radial jets by falling factorials (v9.1)
For g(q) = R^beta T(t), t = q/R, u = 1/R, d^a g/dq^a = R^(beta - a) F_a with F_a = sum_(l=0)^(a) C(a, l) (beta - l)_(a-l) u^l T^(l)(t) ((x)_n the falling factorial). Proof by induction: d/dq [R^(gamma) u^l T^(l)] = R^(gamma - 1) [(gamma - l) u^l T^(l) + u^(l+1) T^(l+1)], so the weights satisfy w_(a+1,l) = (beta - a - l) w_(a,l) + w_(a,l-1), and C(a,l)(beta-l)_(a-l) satisfies this recurrence because l C(a,l) = (a - l + 1) C(a, l-1). Each factor beta - l - i is pdiff(cl, j, m + l + i); the product and its beta-derivative are accumulated factor by factor (product rule), so no division by a possibly vanishing factor occurs and exact zeros are exact. The old route (Stirling conversion d_s^h = sum_l c_(h,l) u^l d_t^l followed by the recursion F_(a+1) = (beta - a) F_a + d_s F_a) formed u^2 T'' as (u T' + u^2 T'') - u T' and lost the leading term at integer exponents (verifier evidence, SPEC v9.1).
### 11.3 Field assembly and cancellations (v9.3)
Fields are assembled by the frozen integer-weighted combinations (absolute_fields._assemble) of F_0..F_4 and the harmonic derivatives of H_m in normalized coordinates xn = x/sqrt(R), yn = y/sqrt(R), t: f = -D(0) d0 - 2 h d1 with d0 = 4((2m+1) F_1 + t F_2), d1 = 4((2m+2) F_2 + t F_3) (the factored Laplacian Lap(H_m v) = 4 H_m [(2m+1) v' + q v'']), f_x and f_y with d2 = 4((2m+3) F_3 + t F_4), psi, psi_x, psi_y and ratio = psi_x/y from F_0..F_3 and the axis-safe quotients D(a) = d_x^a (d_y H_m / y). Since the exact zero factors sit inside every F_a term, a field whose leading radial parts cancel at an integer exponent is a sum of exactly zero terms. Structural zeros: at cl = 2 the generators (0,0,3), (0,1,3), (1,1,3) (R, q, H_1 at p = 1) and at cl = 3 the generators (0,0,2), (0,1,2), (1,1,2) have all seven fields exactly 0.0 (F_a = 0 for the orders that enter; psi = 4 xn yn F_2 for m = 0; hxy = H_xxy = D(2) = 0 for m = 1). Their cl derivatives are nonzero and come from dF_a.
### 11.4 Center-subtracted q (v9 (b))
q = cl - 1 + psi_x/y = sum_i c_i (ratio_i - s_i) because sum_i c_i s_i = 1 - cl exactly (analytic elimination; a_000 is carried from its Decimal value to the 64-bit significand, prepare: c_ld). For the strained generators (m,k) in {(0,0),(0,1),(0,2),(2,2)} with a = p - 2, S = log R, X2 = x^2/R, Y2 = y^2/R: ratio_i - s_i = s_i expm1(a S) + exp(a S) B_i with (own derivation from chi_xxy / y, m = 0: ratio = 4 g'' + 8 x^2 g''' for chi = g(q))
- (0,0): s = 4p(p-1), B = 8 X2 p(p-1)(p-2);
- (0,1): s = 8(p-1), B = 4(p-1)(p-2) t + 8 X2 (p-1)(p-2)(3u + p t)   [g'' = (p-1) R^(p-3)(2 + p q), g''' = (p-1)(p-2) R^(p-4)(3 + p q)];
- (0,2): s = 8, B = 4[4(p-2) t u + (p-2)(p+1) t^2] + 8 X2 (p-2)[6 u^2 + 6(p-1) t u + p(p-1) t^2]   [g'' = R^(p-4)(2 + 4(p-1) q + p(p-1) q^2), g''' = (p-2) R^(p-5)(6 + 6(p-1) q + p(p-1) q^2)];
- (2,2): s = -24, B = b C1 + b(b-1) C2 + b(b-1)(b-2) C3 with b = p - 2, C1 = -96 X2 - 16 Y2, C2 = -12 X2^2 - 104 X2 Y2 + 4 Y2^2, C3 = 8 X2 (X2^2 - 6 X2 Y2 + Y2^2)   [product rule on chi = H_2 g(q): the g', g'', g''' coefficients collected from chi_xxy/y].
All factors p, p-1, p-2, p+1 are exact exponent differences. The forms agree with the verifier's PROOF.centered-precheck.md and were checked against the 85-digit evaluator (dev check: identical to float64 rounding; the plain difference ratio_i - s_i loses up to 2e-13 relative at r = 0.03).
### 11.5 Residual assembly and switch (v9.2)
R_f is formed in longdouble: field sums sum_i c_i phi_i(X) as longdouble matrix-vector products (no BLAS), transport products in longdouble, one rounding to binary64. r <= 0.02: order-48 Decimal Taylor polynomial of R_f (exact Decimal a_000) with coefficients converted to longdouble through 31-digit strings and evaluated in longdouble, highest degree first. 0.02 < r < 1: w_x f_x + w_y f_y + q f with the centered q. r >= 1: sum_i a_i [-j_i (cl - 1) f_i + 2 cl frem_i] - psi_y f_x + psi_x f_y + ratio f (section 5a identity; frem_i the f-field of (k - p_j) u chi for the low block and of H_m R^(p_j-m-1)[t T' + (m - p_j) T] for the high block, both with exact factors). The Jacobian columns are binary64, assembled from the longdouble generator values rounded once and the rounded field multipliers, with the same switch r = 1 (recorded choice; v9.2 allows r_s = 2 for columns). Production (Model860 cache) and stateless (fields860) providers share generator_block and differ in blocking and assembly code; both are gated per configuration (T2.6b/c/d/x).
### 11.6 Origin order (v9.3)
Production order 48 (potential order 52) in the origin disk; the section 13 monitor compares order 48 with order 56; the integrator's disk integral and the r = 0.02 overlap check use orders 48 and 56 (longdouble evaluation).
