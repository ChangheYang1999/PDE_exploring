# S1 numerical certificates

Final version of 2026-10-28T17:48Z (end of the run). This file lists every certified number used by a statement labelled THEOREM in the
report, in S1_CLOSURE.md or in S1_PROOFS.md, with the certificate files that prove it, the method, the size of each
certificate and its independent recomputation. All files are in the folder certificates/, one subfolder per proof part;
certificates/MANIFEST.txt lists all 697 files (the certificates of parts P1 to P32, the records read by the
recomputation programs of the later parts, section 6h, and the records of the later global bounds, sections 6i and 6j) with their sizes and SHA-256 hashes. Restart instructions are in
S1_RESTART.md.

Rule. A number is called certified only if (i) it is produced by exact rational arithmetic or by outward-rounded ball
arithmetic (Arb, through python-flint) on exactly known inputs, (ii) every case of a domain partition is covered, with no
failed or pending case, and (iii) a separate program, written independently of the first, recomputed it from the exact
inputs at higher precision. Floating-point values (FLOAT) are never certificates; they appear only in the last section.

## 1. The exact reference

State 131, the latest accepted checkpoint of the case 4 run, is reconstructed exactly as a finite even-even potential
chi with rational coefficients, rho = -d_y Delta chi, stream function d_xy chi (proof: S1_PROOFS.md, P1.1 and P1.2).

| object | value | file |
|---|---|---|
| c_l | 4076476460239181/2251799813685248 = 1.810319210199998... | P1_source/state131_exact.json |
| gamma = 1/c_l | 2251799813685248/4076476460239181 = 0.552388... | same |
| a_0 = d_y rho(0) | 10.300294891831177... (exact rational stored) | same |
| canonical serialization hash | 4d80cf85ea1746d41c3fcfbdc622c74465cff5b9358e68614e521531ea78fb01 | same |
| hash of the original checkpoint file | 7ff9415cbbe66f9d4a105aa4a999704e67157d8376c969b7561a1c01b1de57bc | same |

Every certificate below records the canonical serialization hash 4d80cf85... of its input, so all of them refer to the
same exact object. The reconstruction program is P1_source/recover_state.py; P1_source/field_eval.py and
state131_field_points.json give independent point evaluations. State 88 (an earlier accepted checkpoint) has parallel
files and is used only as a cross-check.

## 2. Method of the matrix and coefficient certificates

All global inequalities on R^2 are proved on a compact rectangle. With t = r^2/(1 + r^2) in [0, 1], z = cos 2 theta in
[-1, 1], delta = 1 - gamma and w = (1 - t)^(delta/2), every derivative of a canonical potential generator is an exact
rational polynomial in (t, z) times powers of w and explicit positive radial and angular factors (an exact polar
recurrence; negative radial powers are checked to cancel exactly before any interval evaluation). The polynomials are
converted to a tensor Bernstein basis. On a binary subrectangle the range of a polynomial lies in the convex hull of its
Bernstein coefficients; w is treated on its exact monotone interval with a further Bernstein hull in w. A matrix
inequality is accepted on a leaf when the Bernstein lower bound of the smallest eigenvalue (or of the relevant scalar
numerator) exceeds the target in Arb ball arithmetic. Unresolved rectangles are split into their two midpoint children.
A certificate is COMPLETE when its accepted leaves form an exact binary partition of [0, 1] x [-1, 1], including t = 0
(the origin) and t = 1 (infinity), with no failed or pending leaf. Parity in x and y makes a quadrant bound global.

The search runs at 256 or 320 bits. Each independent audit regenerates the exact polynomials from the exact
coefficients, checks the binary partition and the hashes, recomputes every leaf at 384 bits, and compares the
polynomial formulas with Cartesian Taylor jets of the potential at several rational points.

## 3. Hypotheses (B0) to (B11) for state 131

Hypothesis labels are those of S1_CLOSURE.md section 3. Folder names are subfolders of certificates/. "Leaves" is the
number of accepted leaves; "margin" is the worst accepted value from the audit.

| hyp. | statement | certificate (folder/file) | leaves | margin (384-bit audit) | proof |
|---|---|---|---|---|---|
| (B0) | 9/5 < c_l < 37/20, a_0 > 0 | P1_source/state131_exact.json (exact rationals) | - | exact | P1.2 |
| (B0) | bounded D rho, <r>D^2 rho, <r>^2 D^3 rho, <r>^2 D^4 rho, D U, <r>D^2 U, <r>D^3 U | P6_P7_weighted/higher_coefficient_bounds.json, rough_symbol_bounds.json; exact generator sums | - | exact | P7.4, P8.1 |
| (B0n) | c_l + c[rho] = 1; c[rho] = -1824676646553933/2251799813685248 | P2_singular/state131_strain_beta.json (exact beta integrals; normalization defect exactly 0) | - | exact | P2.1, P2.2 |
| (B1) | M = (2c_l + 1)I + sym DU + A >= (19/5) I | P4_energy/state131_compact_certificate.json; audit compact_certificate_audit.json; further independent certificates: 48 Bernstein leaves, M >= 3.8103 I (P92); Taylor-box covering of 58640 polar cells, M >= 3.810156 I, audited by 51 + 4 Bernstein leaves (P93); sharp M >= (c_l + 2) I, equality only at 0 (P94) | 244 | 3.80064 | P4.3, P92 to P94 |
| (B2) | A >= -(1/20) I | P4_energy/state131_aux_A_factored_certificate.json; audit auxiliary_certificate_audit.json | 62 | -0.048962 | P4.5 |
| (B3) | N <= I | P6_P7_weighted/state131_N1_certificate.json; audit state131_N1_audit.json | 849 | I - N >= 0.00035275 | P7.3 |
| (B4) | M_1 = I - sym DU + A >= (9/10) I | P6_P7_weighted/state131_high_symbol_k1_adaptive_unweighted09.json; audit unweighted_M1_09_audit.json; independent full-plane recomputation from the exact original potential, M_1 >= (972875/1000000) I, 99 Bernstein leaves at 384 bits with a 448-bit direct recheck, P96_original_auxiliary_recomputation/B1_global.json and B1_global.recheck.json (P96) | 153 | numerator 4.32e-5 after target | P7.3, P96 |
| (B5) | M_2 >= (1/2) I, weight omega = (1 + 4r^2)^(2/5) | P6_P7_weighted/state131_high_symbol_k2_adaptive.json (k = 2, R_k = 1/2, sigma = 1/5); audit high_symbol_certificate_audit.json; independent full-plane recomputation, M_2 >= (293619/500000) I, 144 leaves, B2_global.json (P96) | 201 | numerator 3.78e-3 after target | P6.9, P96 |
| (B6) | M_3 >= -(5/4) I, same weight | P6_P7_weighted/state131_high_symbol_k3_adaptive_auxiliary.json (k = 3, R_k = 1/2, sigma = 6/5); same audit; independent full-plane recomputation, M_3 >= -(307719/250000) I, 164 leaves, B3_global.json (P96) | 282 | numerator 1.10e-3 after target | P6.9, P7.4, P96 |
| (B7) | ||D^2 rho|| <= 3, ||omega D^2 rho|| <= 8, ||omega D^3 rho|| <= 10, ||omega D^2 U|| <= 3, ||D(v grad rho)/omega|| <= 28, ||S|| <= 40 (also <r>|D^2 rho| <= 8, <r>^2|D^3 rho| <= 32, <r>|D^2 U| <= 3) | P6_P7_weighted/sharp_coefficient_certificate.json; audit sharp_coefficient_audit.json | 663 | e.g. max |D^2 rho| = 2.99954 | P7.3 |
| (B8) | ||D^2 U|| <= 35, ||D^2 rho|| <= 77 | P4_energy/state131_aux_DU_certificate.json and state131_coefficient_bounds.json; audit auxiliary_certificate_audit.json | 49 (DU partition) | - | P4.5 |
| (B8) | ||<r>D^3 U|| <= 2^14, ||<r>D^3 rho|| <= 2^14, ||<r>^2 D^4 rho|| <= 2^84 | P6_P7_weighted/higher_coefficient_bounds.json (exact generator sums with power-of-two rounding), with P4_energy/state131_coefficient_bounds.json on r <= 100 | - | exact | P6.10, P6.11, P7.4 |
| (B9) | omega|D^3 U|_F <= 10, omega|D^4 rho|_F <= 128 | P6_P7_weighted/extra_coefficient_certificate.json; audit extra_coefficient_audit.json | 315 | 9.89114 and 127.80648 | P7.3 |
| (B9) | component sums: 2 + 6 + 24 + 160 + 22 + 32 + 80 + 2048 = 2374 <= 4096 | P8_quasilinear/constants.json (with the Frobenius bounds above, multiplied by the number of ordered components, and the component bounds sum of sup |D_j U_i| <= 6, sup |rho_x|, sup |rho_y| <= 11 from the auxiliary certificates) | - | exact | P7.3, P8.1 |
| (B9c) | the separate bounds (C, U_1, U_2, U_3, R_1, R_2, R_3, R_4) <= (2, 6, 24, 160, 22, 32, 80, 2048) (C = |c|; U_j, R_j sums over ordered tensor entries of sup |omega D^j u| and sup |omega D^j rho|, unweighted for j = 1) | the same certificates as the (B9) component sums, used entrywise | - | exact | P8.4 |
| (B10m) | false for state 131 (residual not in L^2 or H) | P3_tails/state131_tail.json (exact leading residual sector, ||E_1|| = 0.0910) | - | exact | P3.1, P3.3 |
| (B11) | leading profile r^gamma Theta_0, Theta_0 != 0 | P3_tails/state131_tail.json (exact leading density angular coefficients) | - | exact | P3.1 |

Other matrix certificates of the energy hierarchy: sym DU <= (17/20) I (P4_energy/state131_aux_DU_certificate.json, 49
leaves; independently ||sym DU|| <= 101349/125000 = 0.810792 on the whole plane, 49 leaves, P96_original_auxiliary_recomputation/symDU_global.json) and N <= 100 I (state131_aux_N_certificate.json, 5 leaves), superseded by (B3) where both appear; M_1 >= (1/2) I
with weight (1 + r^2)^(-1/10) (state131_high_symbol_k1_adaptive.json, 131 leaves); the exterior energy matrix on
r >= 100, 300, ..., 10^4 (P4_energy/state131_farfield_matrix.json, exact Fourier coefficients and 320-bit Arb, P4.4).
The earlier checkpoint state 88 has a compact certificate with 255 leaves and auxiliary certificates with 57 (A) and 45
(DU) leaves.

## 4. Analytic constants evaluated in interval arithmetic

| quantity | value | file | proof |
|---|---|---|---|
| local term of the strain functional | -1/4 (symbolic and Gaussian Fourier checks) | P2_singular/check_kernel.json | P2.1 |
| weighted Riesz bounds for omega = (1 + 4r^2)^(2/5) | velocity <= 16/3 in general, <= 9/5 on centrally odd input; also 3/2 (beta = -1/5), 8/3 (beta = -6/5, odd) | P6_P7_weighted/mellin_riesz_constants.json | P7.2 |
| Route U constants at theta = 1/32 | gradient embedding 1.5714 < 2, Hoelder 4.4301 < 5, moment 4.3815 < 5, combined bound 240 | P6_P7_weighted/sharp_route_u_constants.json | P7.5 |
| fractional kernel and closure constants (s = 2^-28, r = 2^-27) | weighted kernel moments 16.045 <= 17 and 52.135 <= 54 (in units of s); background table sum 2777/4 <= 1024; c_s = 4621.84; rate >= 11/160; inverse <= 20; eta = 1/2684354560 = 3.7252902984619140625e-10; low inverse 0.26316; contraction 9.06e-6 | P8_quasilinear/constants.json | P8.1 |
| heat-semigroup Hoelder inverse of the frozen operator | 1/(1 - alpha); 486 in ordinary C^(1/2) | P5_frozen/heat_constants.json, optimized_kernel_bound.json | P5.1, P5.2 |
| Hoelder embedding for the earlier X_theta (theta = 1/122) | 8.788 < 9; inverse-to-Hoelder 360 | P4_energy/holder_embedding_constant.json | P4.7 |
| weighted realization X_W constants | inverse 40; velocity 2^35; weighted Hoelder and moment 2^46 | P6_P7_weighted/weighted_high_constants.json, h2_constants.json, bilinear_constants.json | P6.8 to P6.11 |
| component-resolved constants, version (b) (s = 2^-18, r = 2^-16) | symmetric energy-matrix row sums 19053/4, 17925/4, 4324, 240 <= 4800; rough constant 217/50 + (1049/5) s < 5 for s <= 1/1024; rate >= 873/20480 > 1/24; inverse <= 24; eta = 1/1572864 = 6.3578287760416...e-7; gradient bound c_s r = 0.0022039 < 1/400; contraction 5.803e-4 < 1/1000; moment p = 2^21, kappa = p + 4; combined constant 24 * 2^11 = 49152; optimal s = 1/240000 with eta = 6.5319726474e-7 | P8_quasilinear/sharp_constants.json (program sharp_constants.py, exact rationals and 384-bit Arb) | P8.4 |
| derivative-loss example | exact check | P9_closure/check_derivative_loss.json | P9.3 |
| frozen endpoint regularity (state 131) | endpoint Hoelder exponent lambda - 2 = 698776739711309/1125899906842624 = 0.62063...; center Hoelder coefficient C in [7.23975187141277, 7.23975187141278]; C/lambda in [2.76259090725982, 2.76259090725983]; Gaussian endpoint bound < 59.312; unit-disk p4 moment bound < 26.528 (512-bit Arb, two independent gamma-function forms overlap; state 88 also recorded) | P5_frozen/endpoint_constants.json (program endpoint_constants.py); P5_frozen/gaussian_asymptotic_probe.json is a FLOAT quadrature cross-check only | P5.5 |

The residual-conversion constants (2 Q^2 + 16410 E^2 and 34 s) are exact rational consequences of the proof in
P8.1, section 8; the threshold table of S1_CLOSURE.md section 8 is reproduced by the script closure_arithmetic.py
(interval arithmetic with mpmath; S1_RESTART.md).

## 5. Residual lower bounds for state 131

Whole-plane weighted Hessian lower bounds of the actual residual R = F(rho; c_l) with weight
omega_2 = (1 + 4r^2)^((1 - sigma)/2): exact finite potential through angular order 10, all 157 residual sectors, exact
radial integration over r >= 100 with explicit linear and nonlinear tail errors (below 1e-11), 384-bit Arb
(P3_tails/state131_residual_hessian_lower.json; program residual_derivative_lower.py; audit audit_residual_hessian.py
and .json; proof P3.4).

| sigma | lower bound for ||omega_2 D^2 R||_2 |
|---|---|
| 3/20 | 59.4444 |
| 1/5 | 25.1722 |
| 3/10 | 7.10845 |
| 7/20 | 4.14615 |
| 2/5 | 2.50924 |

The norm is infinite for sigma <= 2 gamma - 1. The truncated-sector files state131_residual_truncated_sectors*.json hold
the exact residual sector coefficients.

## 5b. Certified whole-plane residual norms (P12)

For an exact finite rational potential the residual F = F(rho; c_l) and its derivatives up to order 3 are exact rational
polynomials in t = r^2/(1 + r^2) and w = (1 - t)^((1 - gamma)/2), times explicit endpoint factors and trigonometric
polynomials. compact_norms.py extracts the exact factors (1 - t)^q, decides integrability of each angular sector exactly
(an exact nonresonance test excludes cancellation between different powers of w), and integrates with exact beta
integrals; the weight omega = (1 + 4 r^2)^(2/5) is enclosed by a degree-56 Taylor series with a rigorous remainder.
There is no floating-point quadrature. audit_norms.py recomputes everything independently at 640 bits (variable
u = 1 - t, direct monomial antiderivatives, all ordered cross terms) and compares all 10 third-order derivative
components with an independent order-7 potential-jet evaluator at seven rational points (all PASS).

| reference | ||grad F||_2 | ||omega D^2 F||_2 | ||omega D^3 F||_2 | ||F||_2, ||r F||_2 | files |
|---|---|---|---|---|---|
| state 131 | infinite | [25.1892236171285365, 25.1892236171285379] | [2.5042775321848363, 2.5042775321848366] | infinite | P12_residual_norms/state131_norms.json, state131_audit.json |
| refit m10 | [0.3444735104934888, 0.3444735104934889] | [5.0099247071386049, 5.0099247071386053] | [12.3311345810175309, 12.3311345810175319] | infinite | P12_residual_norms/n12_m10_norms.json, n12_m10_audit.json |

The intervals are rounded outward from the 512-bit and 640-bit enclosures in the files. The input hashes are recorded in
the files (canonical serialization 4d80cf85... for state 131, bce59292... for m10). The intermediate polynomial files
(28.7 MB and 83.9 MB) are not shipped: compact_norms.py regenerates them in about 8 s (state 131) and 42 s (m10), and the
regenerated files agree with the originals except for their time stamp field (checked for state 131). The audits take
about 26 s to 70 s (state 131) and 180 s (m10).

## 6. Improved references

- Exact refits (P10.1): P10_refits/n12_m4_audit.json, n12_m5_audit.json, n12_m10_audit.json and n12_m12_audit.json
  are exact rational audits of four refits, with their exact inputs in P10_refit_inputs/ (exact preservation of
  Theta_0, c_l and the center condition; E_(0,0) = E_(1,0) = 0; E_(2,0) != 0, with angular quarter norms 0.771, 0.596,
  0.29865 and 1.11081; center slopes 10.29706, 10.29584, 10.29563 and 10.28661). Programs audit_exact_refit.py (imports
  no fitting code) and point_fields.py. Each audit lists every residual sector (h, q) with exponent
  gamma - h(1 - gamma) - 2q > -5/2, with its exact angular coefficients.
- Refit m14 (P10.1, same programs): P10_refits/n12_m14_audit.json with exact input P10_refit_inputs/n12_m14_exact.json
  (2100 generators; c_l, Theta_0 and the normalization exact; a_0 in [9.925260921106630, 9.925260921106631]). The
  sectors (0,0), (1,0), (2,0) and (3,0) vanish exactly; the sectors (4,0), (0,1), (5,0) and (1,1), all of exponent
  >= -2, are nonzero, with angular quarter norms 172.836, 668.581, 131.356 and 8245.33. The leading one, (4,0), has
  exponent gamma - 4(1 - gamma) = -1.2381.
- Global matrix bound M >= (19/5) I for the refit n12_m5: P10_refits/n12_m5_matrix_certificate.json, 1346 leaves,
  worst recomputed 3.80038 at 384 bits, audit n12_m5_matrix_audit.json (also records its strain
  -1824676646553933/2251799813685248, the same as state 131). No other hypothesis is certified for any refit.
- Tail repair of state 131 (P10.2): P10_tail_splice/state131_splice.json (exact homogeneous potentials of the six
  stationary sectors, maximal potential frequencies 18, 38, 58, 78, 98, 118; exact derivative tables for orders 0 to 10)
  and the independent audit splice_audit.json (program audit_splice.py): every Fourier coefficient of density and
  stream function checked by repeated Cartesian differentiation; uniform exterior symbol bound 2^206; R = 2^1024;
  coefficient transfer with epsilon = 1/1024; exterior M_2 >= 4082593/6579200, M_3 >= -1011919/822400; original
  residual remainder |F - r^(p_2) E_1(theta)| <= 2^131 r^(p_3) for r >= 1; leading angular residual norm >= 1/8;
  N_s(F(rho_R)) >= 2^1028.

## 6b. Exponent conditions of the affine-class obstruction (P13)

P13_affine_obstruction/conditions.json (program check_conditions.py, exact rationals and 384-bit Arb) records, for state
88, state 131 and the refits m4, m5, m10, m12, the leading residual exponent q (2 gamma - 1 = 0.10478 for state 131,
3 gamma - 2 = -0.34283 for the refits), the exact checks q > gamma - 1, c_l q < 1, q > -1 used by P13.1, the response
denominator 1 - c_l q, and for the refits the angular quarter norm of the forced correction r^q E/(1 - c_l q) (0.18428
for m10). The weaker condition q >= -2 of P13.2 (Theorem E of S1_CLOSURE.md) follows from the same exact values.

## 6c. Algebraic tail repairs (P14)

P14_algebraic_repair/construct.py builds, from an exact base potential (state 131 or the refit m10) and an integer
K >= 3, a finite rational potential whose six leading tail potentials equal the exact stationary ones of
P10_tail_splice/state131_splice.json and whose first descendants in branches 0 and 1 vanish, with all Taylor
coefficients below degree 2K unchanged (P14.1). Files algebraic_<base>_k<K>.json for base in {state131, n12_m10} and
K in {4, 8, 16, 256, 4096} hold the exact coefficients, the added generators and the canonical hash.

- Membership, exact (THEOREM, P14.1). audit_repair.py (no construction code imported; FLINT rationals) checks for all
  ten repairs the exact moment identities, the unchanged center density slope and strain, the leading potential
  orders 1 to 6, the vanishing descendants, and lists the residual sectors; every sector with exponent >= -2
  vanishes, and the residual is O(r^(p_7)) with p_7 = -8696260065638350/4076476460239181 = -2.1333 < -2
  (repair_audit.json, verdict CONFIRMED). The first surviving sector, of exponent p_7, is the same for all repairs (it comes only from the
  exact stationary potentials); its full-circle angular L^2 norm is in [3081.27440111579, 3081.27440111580], with
  highest harmonic 139.
- Failure of (B1) and residual lower bounds (THEOREM for these repairs, P14.1 section 5). point_probe.py (Cartesian
  potential jets) and audit_points.py (independent polar differentiation with sparse radial powers), both 640-bit Arb,
  agree at all eight test points of each of the four repairs with K = 4, 16:

| base | K | least eigenvalue of M at (1,1) | certified lower bound for N_s(F), 0 < s <= 1/2 | files |
|---|---:|---|---:|---|
| state131 | 4 | [-395.204, -395.203] | 4564 | algebraic_state131_k4_points.json, _points_audit.json |
| m10 | 4 | [-315.676, -315.675] | 11919 | algebraic_n12_m10_k4_points.json, _points_audit.json |
| state131 | 16 | [-167.090, -167.089] | 2386 | algebraic_state131_k16_points.json, _points_audit.json |
| m10 | 16 | [-9.156, -9.155] | 289 | algebraic_n12_m10_k16_points.json, _points_audit.json |

    The same two programs, with the same independent audit, give the eight test points of the four repairs with
  K = 256, 4096 (algebraic_<base>_k<K>_points.json and _points_audit.json): the least eigenvalue of M is negative at a
  test point for state131 K256 only, and the certified lower bounds for N_s(F) are 230.8 (state131 K256), 107.58 (m10
  K256), 25.44 (state131 K4096) and 11.48 (m10 K4096), the last two from the point (30, 40).

- Matrix scan of all ten repairs (THEOREM for the listed points, P14.1 section 6). matrix_grid.py evaluates M and F on
  the 73 by 65 polar grid r = 2^(i/4), i = -24, ..., 48, and 65 angles in [0, pi/2], with 640-bit Cartesian jets
  (files algebraic_<base>_k<K>_matrix_grid.json, log matrix_grid.log); the grid only selects the point of least sampled
  eigenvalue. audit_grid_minima.py re-evaluates each selected point by an independent polar recurrence
  (matrix_grid_audit.json, verdict CONFIRMED). The certified values at the selected points are:

| base | K | point (log2 r, theta/pi) | least eigenvalue of M | F at the point |
|---|---:|---|---|---|
| state131 | 4 | (0, 0.234375) | [-821.5060, -821.5059] | [9281.822, 9281.823] |
| m10 | 4 | (0.5, 0.2734375) | [-354.6414, -354.6413] | [13448.288, 13448.289] |
| state131 | 8 | (0.75, 0.21875) | [-537.0872, -537.0871] | [-7618.480, -7618.479] |
| m10 | 8 | (1, 0.265625) | [-197.3201, -197.3200] | [4575.702, 4575.703] |
| state131 | 16 | (1.25, 0.2109375) | [-330.6047, -330.6046] | [-4825.234, -4825.233] |
| m10 | 16 | (1.5, 0.265625) | [-105.9231, -105.9230] | [1305.391, 1305.392] |
| state131 | 256 | (3.25, 0.2109375) | [-20.3545, -20.3544] | [-605.686, -605.685] |
| m10 | 256 | (3.25, 0.1796875) | [-0.18689, -0.18688] | [-208.333, -208.332] |
| state131 | 4096 | (4.75, 0) | [3.41663, 3.41664] | 0 |
| m10 | 4096 | (-6, 0.5) | [3.810453, 3.810454] | [5.27e-10, 5.28e-10] |

  Every repair with K <= 256 has a certified negative eigenvalue of M, and state131 K4096 has a certified eigenvalue
  below 19/5, so nine of the ten repairs violate (B1). For m10 K4096 no point below 19/5 is known and no global bound
  is certified. Combining both point sets with ||f||_infinity <= N_s(f), every one of the ten repairs has a certified
  lower bound N_s(F) >= 11.48 for 0 < s <= 1/2 (the smallest is that of m10 K4096). No statement between the
  evaluated points is made; the minimum over the plane is not certified.

- Whole-plane Hessian residual norm of a repair (THEOREM, P14.2). arb_hessian.py writes the residual Hessian of an exact
  finite potential as Arb polynomials (1024 bits) in t and (1 - t)^(delta/2) times trigonometric polynomials, integrates
  the angles exactly and the radial variable twice, by t-beta integrals and by independent ordered-pair monomial
  integrals in u = 1 - t, encloses the weight omega = (1 + 4 r^2)^(2/5) by a binomial series with a geometric remainder
  bound, and compares the Hessian components with Cartesian jets at seven points. There is no quadrature. For the
  repair m10 K8: ||omega D^2 F||_2 in [863401.82156127981, 863401.82156127986] (algebraic_n12_m10_k8_arb_hessian.json,
  canonical hash c6c4ac91..., 76 s). As a check of the program, the unrepaired refit m10 gives
  [5.00992470713860497, 5.00992470713860522] (n12_m10_arb_hessian.json, 12 s), inside the P12 enclosure of section 5b.
  Since E_2(F) >= ||omega D^2 F||_2, this gives E_2(F) > 8.6e5 for m10 K8.
- All residual norms of the repairs m10 K8 and K16 (P14.2 section 5). arb_norms.py extends arb_hessian.py to all
  components (1280 bits; endpoint orders from the audited sector zeros; two radial bases; all ten Cartesian components
  through order 3 checked at seven rational points); the runs reached the command time limit after saving partial
  records and were completed by resume_arb_norms.py, which re-verifies the exact coefficient hash and the stored rows.
  Results (algebraic_n12_m10_k8_arb_norms.json, algebraic_n12_m10_k16_arb_norms.json; outward intervals in the files):
  K8: ||r F||_2 = 35870.5784922..., ||F||_2 = 10040.6317488..., ||grad F||_2 = 40432.7262201...,
  ||omega D^2 F||_2 = 863401.821561..., ||omega D^3 F||_2 = 6366619.69398...; K16: 31813.8185481..., 5544.17335382...,
  17065.3808019..., 366729.212563..., 2153660.01623... . residual_gap.py (768 bits) combines them with the residual
  conversion (S1_CLOSURE.md section 2), the reverse comparison N_s >= (1 - 34 s) E_2 and ||F||_Hdot^-1 <= ||r F||_2:
  at s = 2^-18, N_s(F) in [7344656.42, 19372855.95] for K8 and [3600047.17, 16301198.10] for K16 (residual_gap.json),
  more than 1.155e13 and 5.662e12 times the threshold 1/1572864. Independent audit: an independent proof audit of
  the method and both records (status CONFIRMED in the shipped files); residual_gap.py is rerun by run_checks.py.

## 6d. Homogeneous weight for the negative-order norm (P15)

P15_homogeneous_weight/matrix_audit.json (program check_matrix.py, exact rationals and Arb, verdict CONFIRMED) evaluates
for state 131 at s = 11/5 the two-mode quadratic form of P15.1 (modes sin(theta), sin(3 theta)) with c = c_l and the
exact a_0 = 12102479225522702540364244077864789/1174964343508337542719888806641664: the real Rayleigh quotient is the
exact rational 2388437324574778245651437130523756199/187994294961334006835182209062666240, in [12.70483939, 12.70483940],
so Q_* > 12 and the energy -Re <L_0 h, h> in the homogeneous weighted negative-order norm is not coercive (P15.1
section 3). The file also records the Beurling norm 12 and the velocity bound 13/2 at s = 11/5, which are proved
analytically in P15.1 and P15.2 (formula (1) of P15.1); these two numbers are exact, not computed.

## 6e. Theorem D_w: weighted fractional closure (P17, P18, P19, P21)

Theorem D_w (S1_CLOSURE.md section 7a; proofs S1_PROOFS.md P17, with P6.12 to P6.16) has hypotheses (W0) to (Wt). For
state 131 the reference conditions are certified by the following files (all with source hash 4d80cf85...);
P17_weighted_fractional/reference_audit.json (program reference_audit.py) binds every listed input by its SHA-256 hash,
rechecks the exact arithmetic of the contract and records the status of each condition.

| condition | certified value | certificate (folder/file) | leaves |
|---|---|---|---|
| (W0) | 9/5 < c_l < 37/20, a_0 = 10.30029... >= 1, parity, sublinear growth, canonical velocity | P1_source/state131_exact.json (exact rationals) | - |
| (Wn) | c_l + c[rho] = 1 exactly | P2_singular/state131_strain_beta.json (as (B0n) of section 3) | - |
| (W1) matrix | M >= (19/5) I | P4_energy/state131_compact_certificate.json, compact_certificate_audit.json (as (B1)); sharp form M >= (c_l + 2) I (P94) | 244 |
| (W1) matrix, weakened (P24) | M >= (5/2) I, or M >= 2/5 + (11/5) c r^2/(R^2 + r^2), on r <= R = 2^31 suffices: interior baseline 5/2 - (11/10)(37/20) = 93/200, exterior baseline 853/2000, low margin 14093/70000 unchanged (exact rational check) | P24_weaker_matrix/check.json | - |
| (W1) decay, exponent d = 2/5 | sup r^d (|D rho| + r |D^2 rho|) <= 152 (interior 151.43, exterior 123.08), sup r^(d-1)|u| <= 18, sup r^d |Du| <= 18, sup r^(1+d)|D^2 u| <= 45; radial commutator factor 13.3383 <= 14; low decay margin above 0.2288 > 1/5 at R = 2^35 | P6_P7_weighted/radial_commutator_constants.json (512 bits) with state131_weighted_bounds.json | - |
| (W2), k = 1 | M_1 >= I/2 with omega_1 = <r>^(-1/5) | P6_P7_weighted/state131_high_symbol_k1_adaptive.json; audit high_symbol_certificate_audit.json | 131 |
| (W2), k = 2 | M_2 >= I/2 with omega_2 = (1 + 4r^2)^(2/5) | P6_P7_weighted/state131_high_symbol_k2_adaptive.json (as (B5)) | 201 |
| (W3) first derivatives | |Du| <= 14/5, |D rho| <= 16 | P4_energy/state131_coefficient_bounds.json, auxiliary_certificate_audit.json | - |
| (W3) second and third | |D^2 rho| <= 3, <r>|D^2 rho| <= 8, <r>^2 |D^3 rho| <= 32, <r>|D^2 u| <= 3 | P6_P7_weighted/sharp_coefficient_certificate.json, sharp_coefficient_audit.json (as (B7)) | 663 |
| (W3) fourth | <r>^2 |D^4 rho| <= 512 (maximum 324.713), <r>|D^3 u| <= 16 (maximum 8.0913) | P6_P7_weighted/r2_extra_audit.json (program r2_extra_audit.py, 384 bits, about 160 s) | 315 |
| (Wm) | residual degree q = 2 gamma - 1 = 427123167131315/4076476460239181 = 0.10478 in (0, 1/5) | P17_weighted_fractional/state131_weighted_gap.json (exact) | - |
| (Wt) | gamma = 1/c_l in (1/5, 1), leading profile Theta_0 != 0 | P3_tails/state131_tail.json (as (B11)) | - |
| (Ws) | REFUTED for state 131: see the two lower bounds below | P17_weighted_fractional/annular_residual.json | - |

The analytic constants of the theorem are exact rational or 384- to 512-bit Arb computations:
P17_weighted_fractional/constants.json (fractional embeddings: gradient 2^11, gradient Hoelder 2^12, growth 2^13, so
|h(X)| <= 2^13 max(1, r)^(1/5) N^w_s(h), product 2^14; Hoelder coefficient below 2623.45); P6_P7_weighted/
fractional_bilinear_constants.json (theta = 1/62, bilinear bound 872415297/2 <= 2^29); radial_commutator_constants.json;
sharp_weighted_h2_constants.json (E_1 and E^w semigroup rates 1/10 and 1/20, inverses 10 and 20, coefficients 2^31,
2^22, 2^53); sharp_weighted_high_constants.json; and P17_weighted_fractional/sharp_weighted_constants.json for
the closure arithmetic at s = 2^-30: background component sum 22257016/5 <= 2^23, rough component sum 1660928/5 <=
2^19, high rate at least 11/320 (inverse at most 32), low inverse at most 6, contraction 3/1024 in the low metric,
radius r_0 = 2^-41, threshold eta = 2^-46, combined inverse constant 2^68. The first, weaker version of the theorem
(s = 2^-104, r_0 = 2^-78, eta = 1/(3 * 2^81), high rate 859/20480, inverse 24) is recorded in
P17_weighted_fractional/rough_constants.json. The sharper constants (S1_CLOSURE.md section 7a, part P19 of
S1_PROOFS.md) are checked by P19_fractional_constants/constants.py (exact fractions and 512-bit Arb; it binds the
proof texts it implements by their hashes): localization 2595/2048, gradient 4, gradient Hoelder 8, growth 16,
product 16, weighted product 32, rough components 856/5, 664/5, 204/5 and 48 with total 1964/5 <= 400, low bilinear
constant 1820 <= 2^11, smooth component sum 22257016/5 <= 2^23; at s = 3 * 2^-31, r_0 = 5 * 2^-32, eta = 2^-35: high
rate 0.0258225... (rational bound 6283/245760 > 1/40, inverse at most 40), low rate 0.19850... (inverse at most 6),
slope change 1.2459e-4, contraction 0.38273... < 2/5, four-output bound 1.9612e17 <= 2^58. Gap exponents: 117
(R = 2^32) and 124 (R = 2^35).

Lower bounds for the actual residual of state 131 in N^w_s:
- Point bound (superseded). F(0, 1000) = 0.12530228283209130510... > 1/8, three independent 768-bit evaluations
  (Cartesian jets of order 4 and 7, polar form; state131_weighted_gap.json); with the growth embedding,
  N^w_s(F) > 2^-18, a factor 2^28 above eta.
- Annular duality bound. P17_weighted_fractional/annular_residual.py (768 bits; reconstructs the 860
  coefficients from the original checkpoint, whose hash 7ff9415c... it checks) computes the exact residual sectors
  on r >= R = 2^35 from the first two binomial orders of the four potential branches (the sector data are written to
  annular_residual_sectors.json), the uniform tail coefficient C_tail = 1.76139e-18 < 1.762e-18, and for each odd
  m = 1, ..., 39 the exact leading coefficient e_m, the bound of the lower sectors and the lower coefficient
  b_m = |e_m| - B_m - 2 C_tail; all twenty b_m are positive (for m = 1, b_1 = 0.0026439...). With the single test
  function of S1_CLOSURE.md section 7a it gives L(F) > 44839313343871924203 (4.4839e19) and
  N^w_s(F) > 709255297103759324984730490 (7.0925e26) > 2^89 for 0 < s <= 2^-12, hence N^w_s(F)/eta > 2^135 for eta = 2^-46 and > 2^124 for eta = 2^-35. Three
  full Cartesian-jet evaluations of F at radii R and 2R differ from the truncated sectors by less than the proved error
  (normalized difference 2.98e-34 at (0, R), for example). Runtime about 1.3 s.
- Smaller radius. P18_weight_radius/decay_radius.py (512 bits, from the original checkpoint) proves the
  decay bounds of (W1) with delta replaced by 4/9 (constants 190, 23, 23, 56; interior 185.83, exterior 151.03), the
  commutator factor 14.5723 <= 15 and a low margin above 0.2060571 (rational bound 9731/47500 > 1/5) at R = 2^32, so
  Theorem D_w holds with R = 2^32 and unchanged s, r_0, eta. P18_weight_radius/annular_residual.py repeats the
  annular bound at R = 2^32: C_tail < 2.846e-15, L(F) > 563055561251943055 (5.6306e17),
  N^w_s(F) > 8906250109564824650127350 (8.906e24) > 2^82, gap > 2^128 over 2^-46 and > 2^117 over 2^-35.
- Smallest radius (P21). P21_real_velocity/constants.py (exact fractions and 512-bit Arb; it reconstructs the 860
  coefficients and checks the hashes of the imported P18 enclosures and proof texts) checks the weighted Schur rows of the
  real angular pairing (row 1: 32701/1800, row 3: 7857869/420000 = 18.70921..., row 5: 2368763/176400, all below 75/4,
  so the weighted velocity constant is at most sqrt(75/4) < 13/3), the real commutator coefficient 10.338767... <= 21/2,
  the coefficient tuple (186, 22, 22, 56) against the P18 balls, and the low margin 0.2020292883... at R = 2^31
  (rational bound 14093/70000 > 1/5); the low bilinear constant becomes 3640/3. Theorem D_w therefore holds at
  R = 2^31 with the constants of P19 (s = 3 * 2^-31, r_0 = 5 * 2^-32, eta = 2^-35). P21_real_velocity/
  annular_residual.py (768 bits, from the original checkpoint) repeats the annular bound at R = 2^31: tail coefficient
  3.33974e-14, all twenty lower coefficients positive (b_1 = 0.0026407...), L(F) > 130848043650562055 (1.3085e17),
  N^w_s(F) > 2069716531185650706596364 (2.0697e24) > 2^80, gap > 2^115 over 2^-35. Runtime about 1 s each.

Independent recomputation. All D_w certificates above were produced in the independent verification and are re-run
from the shipped files by run_checks.py (S1_RESTART.md). The point value F(0, 1000) was evaluated by three independent
methods. For the annular bounds the internal cross-checks are the separate reconstruction of the coefficients from the
original checkpoint and the full-jet point comparisons. In addition, at R = 2^35 a lower bound of the same quantity was
obtained by two programs written independently of each other. A program of the numerical work, from its own exact
far-field sectors with rigorous binomial tail bounds and rigorous adaptive integration (256 bits), certifies with a
different test function (psi(r/T) sin(theta), psi = sin^2(pi (log_2(r/T) + 1)/2) on T/2 <= r <= 2T, mode m = 1 only)
L(F) >= 1.122153e19 at T = R = 2^35. The independent audit P11_audit/audit_c8.py (part P11.2 of S1_PROOFS.md)
reconstructs the 860 coefficients and the residual sectors afresh with its own differentiation, proves its own
omitted-series bound and recomputes the three pairings by 256-bit ball quadrature; it confirms the integer bounds
L(F) > 8254901318 (T = 2^20), 18730797419875790 (T = 2^30) and 11221534985305196289 (T = 2^35), hence
N^w_s(F) > 130573642877133558, 296278339214129575742327 and 177498996671201117552150089 (1.77498e26 > 2^87). The
corresponding gap over eta = 2^-35 is more than 2^122. (The producer's record was later rewritten in a new format. The audit was
updated to it, binds the shipped record numerics_data/wnorm_cert_131.json by its SHA-256 hash 58a9b6d8..., and confirms
all six published decimal lower bounds (for example 1.873079e16 at T = 2^30, which replaces an earlier upward-rounded
1.873080e16) and the integer bounds above. A further diagnostic decimal field of that record is a valid lower endpoint
at T = 2^30, is not decided by the audit's coarser remainder at T = 2^20, and at T = 2^35 exceeds the upper endpoint of
the exact test quotient by about 1.6e-11, so it is not a lower bound; no stated bound uses it.) The deduction from L to N^w_s uses the inequality
L(J^-s g) <= 6 L(g) for g = J^s F; part P21.2 checks that this growing input belongs to the space where that inequality
holds. One test mode recovers about a quarter of the twenty-mode value 4.4839e19.

Combined test, computed twice (P11.4). The program numerics_code/wnorm_cert_multi.py of the numerical work (written
separately from the verification programs; shipped with the four modules it imports and rerun by run_checks.py on the
exact input numerics_data/state131_exact.json with Q = 3 and R = 2^35, 2^32, 2^31) evaluates the combined test of all
leading modes with exact integration of the radial weight. The independent audit P11_audit/audit_c9.py (384 bits; fresh
reconstruction of the 860 coefficients from the original checkpoint, its own exterior sectors through Q = 3 and its
own tail majorant, log-coordinate quadrature) finds that the producer's pairings overlap its own balls, confirms every
published lower bound and certifies the strict integer bounds L(F) > 372474829674258475, 1602697408584840334 and
127617579877087467912, and N^w_s(F) > 5891699187235504891307708 (5.8917e24), 25351004329075412989160659 (2.5351e25)
and 2018617989023167178688648715 (2.0186e27), at R = 2^31, 2^32 and 2^35 respectively. The gaps over 2^-35 are
therefore more than 2^117, 2^119 and 2^125; these doubly computed values are the gaps quoted in the report, and the
twenty-mode bounds above (2^115, 2^117, 2^124) are consistent with them. Runtime about 3 s (audit) and 11 s (program).

Necessary residual scales (P30). P30_residual_targets/check.py checks the exact arithmetic of the corollary
N^w_s(F) <= 2^-35 => L(F) <= 6 * 2^(-123/2) < 2^-58 (36 < 128) and |F(X)| <= 2^-31 max(1, |X|^(1/5)), at
s = 3 * 2^-31, and binds the proof texts it uses by their hashes.

A FLOAT evaluation of the full
leading sector (mode-wise radial Green functions up to r = 3.7e32) gives L(F) about 8.8e20 and 2^(53/2) L(F) about
8.4e28 at R = 2^35, consistent with the certified lower bounds (section 8).

## 6f. Exactly admissible projected refits (P20)

Two finite rational references produced by projected least-squares fitting in the numerical work (files
nb_stableA2_exact and nb_stableA3_exact, each 2342 generators of the extended family of P14) were audited by programs
written independently of the fitting code. P20_nb_candidates/audit_exact.py expands every generator by exact integer
binomial formulas into 1282 canonical rational terms (hashes recorded), evaluates the origin derivatives rationally and
forms the exterior residual sectors by independent Laurent differentiation (512 bits for the displayed balls). For both
files: the exponent equals that of state 131 exactly, c_l + c[rho] = 1 exactly, the full leading angular profile and the
six stationary potential branches equal those of state 131, the first descendants of branches 0 and 1 vanish, and all
eight residual sectors of degree at least -2 vanish identically; the first nonzero sector has exponent
gamma - 6 delta = -2.1333 with full-circle angular L2 coefficient 3081.27440111... Hence the residual lies in both
residual spaces (necessary condition of Theorem E satisfied). Center slopes: a_0 = 7.19290788491380... (A2) and
8.77823087391110... (A3).

P20_nb_candidates/point_audit.py evaluates seven fields at eight rational points at 768 bits by two methods (Cartesian
Taylor jets of order 7 and the polar form), which overlap at every point:

| point | F (A2) | lambda_min(M) (A2) | F (A3) | lambda_min(M) (A3) |
|---|---|---|---|---|
| (0, 1/10) | -0.000355366 | 3.74461 | -0.001449554 | 3.68584 |
| (0, 1) | -11.1357299 | 2.22252637 | -6.1093834 | 3.13523976 |
| (1, 1) | -11.2584629 | 2.96042 | -6.2941279 | 3.35595 |
| (0, 2) | -26.5245206 | 2.46716 | -13.7569062 | 3.32537 |
| (3, 4) | -17.4232601 | 3.94369 | -14.4493592 | 4.12623 |
| (6, 8) | 11.3641756 | 4.40784 | -4.2881267 | 4.42407 |
| (30, 40) | 1.46904581 | 4.59808 | 0.70328879 | 4.59470 |
| (60, 80) | 0.29090241 | 4.60392 | 0.08400452 | 4.60349 |

(decimals truncated from the certified balls, whose radii are below 1e-18). Four points violate the matrix condition
M >= 19/5 for each file. With the growth embedding |F(X)| <= 16 max(1, r)^(1/5) N^w_s(F) of P19 (valid for
0 < s <= 2^-12 and the weight radii R = 2^32 and 2^35; at (0, 2) the factor is 16 * 2^(1/5) < 20), the value at (0, 2)
gives N^w_s(F) > 13/10 (A2) and N^w_s(F) > 2/3 (A3), so the threshold 2^-35 fails by a factor of more than 2^34 for
both (more than 2^35 for A2). These are certified failures of two sufficient conditions,
not nonexistence statements. The weaker matrix floors of P24 (section 6e) are not checked globally for these files;
section 6g gives larger residual gaps and a certified failure of the derivative bound |D^2 rho| <= 3 for both.

### 6g. Later candidates, uniform bounds and their limits (P25 to P29)

All programs below work on exact rational inputs and record the SHA-256 hashes of their inputs, proof texts and code.
They certify necessary conditions or their failure; none certifies a hypothesis of the existence theorem. Second
computations: the P28 point derivatives are computed twice, from Cartesian and from polar representations; the leading
residual vector of P25 is recomputed from the original checkpoint by P27_uniform_family_gap/audit_algebra.py and agrees
exactly; P27 and P29 each have a separate 512-bit audit program with different summation.

Annular residual bounds for A2 and A3 (P25). P25_admissible_tail_gap/annular_candidates.py rebuilds the exterior
residual sectors of each candidate exactly, and summarize.py combines the leading-sector lower bound with the weighted
norm (the leading angular L2 coefficient of the common first nonzero sector is 3081.27440111579815..., identical for
both files and equal to that of state 131). Strict integer bounds at weight radius R = 2^31:

| file | test radius T | L(F) > | N^w_s(F) > | gap over 2^-35 |
|---|---|---|---|---|
| A2 | 2^31 | 1 | 20014377 | > 2^59 |
| A2 | 2^35 | 0 | 39623 | > 2^50 |
| A3 | 2^31 | 1 | 20013535 | > 2^59 |
| A3 | 2^35 | 0 | 39623 | > 2^50 |

The program also regenerates two large intermediate records that are not shipped; regeneration is deterministic and
their SHA-256 hashes are nb_stableA2_exact.sectors.json 80aff38e5969974ed2410d9c5bba7d9d1b02718ec50c726efd0faec5bb845236
and nb_stableA3_exact.sectors.json a1536acd163bcfaf9e4a3c7757332cfe4e007389e25dfbf1d34fabb4688bb5fd. Runtime about
2 minutes per file.

Point tests of the derivative hypotheses (P26, P28). The derivative requirements (W3) are |Du| <= 14/5,
|D rho| <= 16, <r>|D^2 u| <= 3, <r>|D^3 u| <= 16, |D^2 rho| <= 3, <r>|D^2 rho| <= 8, <r>^2|D^3 rho| <= 32 and
<r>^2|D^4 rho| <= 512, with ordered tensor norms; a certified violation at one point disproves the global requirement.
P26_candidate_contract/check.py certifies rho_yy(0, 1/10) > 4.71760 (A2) and > 10.89908 (A3), so |D^2 rho| <= 3 fails
for both, and for A4 F(3, 4) = -2.0659746780..., which with the point bound of section 6f gives N^w_s(F) > 9/100 (gap
more than 2^31). P28_candidate_point_audit/point_contract.py, summarize.py, summarize_a6.py and summarize_mpen2.py
(768-bit point jets) certify:

| file | certified violations | N^w_s(F) > (point bound at (6, 8)) |
|---|---|---|
| A4 | |D^2 rho| > 3.05085 and <r>^2|D^4 rho| > 2001.17 at (0, 1/10); <r>|D^3 u| > 35.5797 and <r>^2|D^3 rho| > 49.6421 at (0, 1/5); <r>^2|D^3 rho| > 138.9647 at (0, 2/5) | 9/100 (P26) |
| A5 | <r>^2|D^4 rho| > 692.7879 at (0, 4/5) | 0.02036 |
| Mpen | <r>^2|D^4 rho| > 678.8363 at (0, 4/5) | 0.01781 |
| A6dpen | <r>^2|D^4 rho| > 551.5248 at (0, 1/5) and > 631.6766 at (0, 4/5) | 0.00732 |
| Mpen2 | none at the eight points: M > 19/5, M_1, M_2 > 1/2 and every bound of (W3) hold there (at (0, 1), 449.0303 < <r>^2|D^4 rho| < 512) | 0.0048729 (F(6, 8) = -0.123570900722...) |

For A6dpen the weighted matrix condition W2 holds at the selected points only; its global positivity is not decided.
For Mpen2 (exact source SHA-256 07bb884b96121b22ca099c3b9d3451d19a65d6af684422b595b305e48d918e05, canonical
0083c8377b84714b3ae29d2122eef35d66648a57c204410614d04c1309b7fed6; exact admissibility audited in P20_nb_candidates) the
point results do not prove any global condition. The residual gaps over 2^-35 are therefore more than 2^31 (A4), 2^29
(A5, Mpen) and 2^27 (A6dpen, Mpen2).

Uniform bound for the generator family (P27). P27_uniform_family_gap/muntz_bound.py (exact exponents, 384 bits)
treats every real coefficient choice in the potential family of P27 (branches j = 0, ..., 5, angular index m <= 59,
radial index k <= 75) that keeps the six leading stationary profiles of state 131 and the two vanishing first
descendants. With the 1852 exponents of the residual power representation it evaluates the Muntz-type constant
D = 4.97443659e-5 and C_D = 202394.3868 (C_D^2 recorded as an exact rational) and, summing over the 70 odd modes
m = 1, ..., 139 of the fixed residual sector, certifies ||F||_Hdot^-1 > 2.6775016e-7 for every member of the family;
hence N_s(F) > 1.33766919e-4 for the unweighted norm at s = 2^-18, which exceeds the unweighted threshold 1/1572864 by a
factor of more than 210.397. P27_uniform_family_gap/audit_algebra.py checks the exponent algebra independently (512
bits) and confirms that the canonical forms of the refit inputs lie in the family. This bound concerns the unweighted
norm; a uniform bound for the weighted norm N^w_s is not certified.

Sharper constants and higher radial degree (P31). For radial degree k <= K (K >= 59) the residual power set has
n_K = 12(2K + 5) - 8 exponents. P31_radial_degree_obstruction/degree_bound.py (384 bits) evaluates the bound of P31.1
(Volterra dilation constant C_K = (4 S_K^2/pi^2 + 1/4)^(1/2), S_K an exact rational): ratio to 1/1572864 more than 233
at K = 75, more than 1.0019782 at K = 349 and less than 0.9917770 at K = 350; audit_degree.py (512 bits, gamma-function
ratios per branch, three exact rational Gram tests of the compression identity) agrees in all 18 rows.
P31_logarithmic_derivative/constant_bound.py (384 bits, gamma-function products) evaluates the bound of P31.2
(cylinder constant Q_n = (2n(n^2 + 2) + 1)/3, exact; lower bounds rounded down, D_K rounded; at K = 780 the values in
parentheses are the values of the formula, which no longer exceed the threshold):

| K | n_K | D_K | Hdot^-1 lower bound | N_s lower bound | ratio to 1/1572864 |
|---|---|---|---|---|---|
| 59 | 1468 | 7.2111272e-5 | 3.4211716e-6 | 1.7092037e-3 | > 2688.34 |
| 75 | 1852 | 4.9744366e-5 | 1.6654948e-6 | 8.3207463e-4 | > 1308.74 |
| 349 | 8428 | 4.4122620e-6 | 1.5217226e-8 | 7.6024660e-6 | > 11.957 |
| 779 | 18748 | 1.2285318e-6 | 1.2770708e-9 | 6.3801954e-7 | > 1.0035179 |
| 780 | 18772 | 1.2260209e-6 | (1.2720175e-9) | (6.3549488e-7) | < 0.9995471 |

audit_derivative.py (512 bits, direct products over all exponents) agrees with all 21 rows and checks the basis,
trace and cylinder identities exactly on four rational exponent sets. A third computation (interval arithmetic in
mpmath, a different library, S_K in closed form) reproduces the ratios at K = 59, 75, 349, 350, 779 and 780 for both
bounds (scripts/check_p31_constants.py, output check_p31_constants.json and .log).


Limits of the linear relaxation (P29). P29_limits_of_tail_invariants/relaxation_bound.py constructs, at R = 2^31,
for 0 < s <= 1/2 and the 70 leading modes, a smooth function with the parity of a residual, the same fixed leading
sector, the eight preceding sectors zero and the finite power representation of P27 (not asserted to be the residual
of any potential), and certifies that its weighted norm is at most 3.4601960702e-13 = 0.011889 * 2^-35. audit_relaxation.py (512 bits, independent constants,
512 exact radial derivative identities) confirms the upper bound 3.460197e-13. Hence no argument that uses only these
linear invariants can prove a uniform weighted lower bound above 2^-35; this is a statement about the method, not
about the family.

### 6h. Later parts (P31 to P98): independent third computations

The primary certificate programs of the parts after P32 are not in certificates/, but every record that the third
computations below read is (MANIFEST.txt), so that S1_RESTART.md section 3 restores their layout and
scripts/run_recomputations.py reruns all thirty-two programs and compares each output with its shipped record. The
certified numbers of these parts rest on the primary computation, its independent audit, and the third computation
listed below. Each third computation was written
from the statement of the part only, imports no program of the primary computation or of its audit, reads the exact
source records by SHA-256 (recorded in its output) and exits with a failed assertion if any check fails. All rows below
passed. The programs are in scripts/ (check_*.py), each with its output JSON next to it. Times are on one core of the
loaded machine.

| part | program | what is recomputed, and by which route | result |
|---|---|---|---|
| P31 | check_p31_constants.py | B_K (P31.1) and Bnew_K (P31.2) in mpmath interval arithmetic, independent of python-flint | B_349 > 1.0019782, B_350 < 0.9917770, B_75 > 233; Bnew_779 > 1.0035179, Bnew_780 < 0.9995471, Bnew_75 > 1308 |
| P32 | check_p32_order7.py | seventh stationary order and the (7,0) residual invariant from the exact state 131 record | full-circle E7 coefficient sum 9679.96558019927435...; six-branch (6,0) invariant 6(c-1)Theta_7 = 3081.27440111579815... |
| P33, P35 | check_p33_p35_constants.py | recursive dilation family bounds, interval arithmetic | K = 75 bound > 22986; K = 3675 > 1.0004726, K = 3676 < 0.9997658; P35 at K = 69: eps0 < 7e-13, eps1 < 3e-12 |
| P36, P38, P40 to P42, P45 | check_jet_distance.py | necessary local distance tests and the b6 derivative values, bivariate interval Taylor arithmetic (320 bits) | every recorded test value enclosed |
| P39, P40, P45 | check_p39_p40.py | annular test coefficients rebuilt as exact rationals; leading moments of the nine refits | exclusion radius 2^-22 at T = 2^31, 2^32, 2^35; P45 radii 2^-14 (T = 2^31, 2^32) and 2^-15 (T = 2^35); all nine refits share the exponent and the leading moments |
| P43, P44, P46, P47 | check_p43_p47_constants.py | smooth-commutator constants (exact rationals; Bessel and heat moments in interval arithmetic) | value (11) 8.85398...; rate > 0.0258225; contraction < 0.382733; output constant < 4882781 |
| P46 to P49 | check_p48_p49.py | constants d_h, d_u, the centered square tests and the annular bounds of P48, P49 (180 s) | d_h = 8436585/8388608, d_u = 7604905/4194304; b_h < 1/190000, b_u < 1/60000; annular lower bound 1.7285e17 at T = 2^31; exclusion power 14 |
| P51 | check_p51.py | exterior transfer of the annular witnesses: weight Laplacian (sympy), cutoff integrals, the three rows | N_(s,R)(F) > 3.5350e25 (R >= 2^31), 1.5211e26 (2^32), 1.2112e28 (2^35) for state 131; every record value below the recomputed one |
| P52 | check_p52.py | canonical coefficients of nb_d2_exact (1322) and nb_Mpen2_exact (1282), annular residual bounds, Cartesian jet checks (688 s) | best lower bounds 1.7605e9 (d2) and 1.7599e9 (Mpen2), exclusion radius power 21, both agree with the record |
| P54, P58 | check_p54_p58.py | global W3 derivative tests at rational points, seventh order, interval arithmetic | every tested S_4 value exceeds its stated lower bound and the contract 512 (for example 592.78 at (7/16, 7/64) for d2) |
| P60 | check_p60.py | seven-branch weighted floor: exponents, moments, determinant, J_* | c_* = 1.46724..., J_* = 1.06419e-4 > 1/67200 |
| P62 | check_p62.py | finite power representation floors, Muntz and radial identities (25.5 s) | all twelve (J, K, epsilon) rows enclosed by the record; for example J = 6, K = 75: factor 6.0037e-55 above the stated floor 6e-55 |
| P63 | check_p63.py | constants of the conditional weighted inverse and nonlinear theorem at s = 3*2^-21, r0 = 5*2^-27, eta = 2^-30, exact rationals | 9/5 < c < 37/20; beta > 6283/245760 > 1/40; contraction 15/(16 sqrt 6) with square 75/512 < 4/25; output constant < 2^23; 40 eta = r0 |
| P66 | check_p66.py | Gaussian finite differences and the frozen ordinary C^(1/2) constant (0.8 s) | 96.0918 < 97 (state 88), 95.9070 < 96 (state 131) |
| P67 | check_p67.py | fractional Gaussian kernels: Laguerre polynomials, exact Sturm root isolation, reduction to the lower incomplete gamma function, incomplete beta series (2.2 s) | ordinary constant 86.716 < 87 (state 88) and 86.451 < 87 (state 131) |
| P69 | check_p69.py | strain-trace symbols, Gram matrix and norms (sympy) | exact norms 1/[8 sqrt(pi s(s+1))] and 1/[8 sqrt(2 pi s(s+1))]; 4.51297 and 3.19115 at s = 2^-12 |
| P70 | check_p70.py | envelope polynomials (Laguerre), D_1 = e E_1(1) by its alternating series, the H_1 norms (7.5 s) | 124/209 < D_1 < 100/167 (D_1 = 0.5963473623...); H_1 norms 0.0544609 < 1/18 and 0.0385097 < 1/25 |
| P71 | check_p71.py | moments of the kernel of Q_beta^(-1) by the Cartesian Laplacian of the Taylor polynomial of its multiplier, the coefficients of D_R from exact expansions, the integer floors by exact squared comparisons (0.8 s) | M_2 = 4 beta, M_4 = 32 beta(beta + 2), M_6 = 384 beta(beta^2 + 6 beta + 7); D_(2^31) = 3.818e-9 < 2^-27; logarithmic residual norms above 35350194988431047182367358 (state 131, R >= 2^31), 1935892101 (Mpen2) and 1936535199 (d2) |
| P72 | check_p72.py | the cutoff kernel identities (sympy), both sides of the averaging identity on two explicit Schwartz potentials at three radii with exact angular integrals and 40-digit radial quadrature, the pure first harmonic that fixes the contact coefficient 1/4 (95 s) | 30 checks; the circular cutoff equals the average of c + h_y/4 against 2(1 - r^2/eps^2)_+/(pi eps^2); the contact term is necessary when h_y(0) != 0 |
| P73 | check_p73.py | growth and amplitude constants of the logarithmic norm as exact squared comparisons, the weak identity as an exact divergence, heat-kernel moment facts (FLOAT) (24 s) | 40 checks; exclusion radii 2^57 (state 131) and 2^21 (Mpen2, d2) for 0 <= beta <= 1, R >= 2^31 |
| P74 | check_p74.py | Frullani and heat identities, the explicit density and its four scaling factors, support separation and the series bound (sympy); FFT diagnostics (FLOAT) (4.6 s) | 20 checks |
| P75, P77 | check_p75_p77.py | moments of the powers of (I + tau K)^-1 from a gamma mixture, the low-kernel coefficients at R = 2^31, the generating-function sums, the rate and conversion inequalities (13 s) | 31 checks; rate 1/29, inverse 29, conversion (841/7)(2 + 16/1024) < 256 |
| P76 | check_p76.py | the velocity of -Delta phi, the plateau construction, the frequency degrees of the cross term and the scaling exponents of the counterexample (sympy); FFT diagnostics (FLOAT) (6.2 s) | 19 checks |
| P78, P79 | check_p78_p79.py | constants of the half-logarithmic product, (7 + 1/sqrt 24)/sqrt(pi) < 5, Moser test functions, commutator constants a pi beta (sympy, exact); FFT ratios (FLOAT) (3.5 s) | 25 checks; product constant 5; the product estimate fails for beta < 1/2 |
| P80 to P85 | check_p80_p85.py | every rational comparison of the six parts, heat moments and commutator constants, the energy coefficients and first-order identity of the nonlinear theorem, the threshold arithmetic (3.4 s) | 76 checks; eta = 2^-25 tau^beta (2 beta - 1)^(1/2) < 2^-37 for every beta (maximum 2^-37 (24 e log 2)^(-1/2) = 1.08199e-12 < 1.083e-12 at beta = 0.5300..., display) |
| P86, P87 | check_p86_p87.py | conversion constant by integer tenth powers, the native residual floors from the stored witness records (hashes recorded), the constants of the four outputs, the contact formula for the strain against an exact Fourier evaluation on five Gaussian inputs (4.6 s) | 30 checks; M(F) > 35350195123413029343106947 (state 131), 1935892108 (Mpen2), 1936535207 (d2); contact formula exact on all five inputs |
| P88 to P92 | check_p88_p92.py | the audit constants of P88 (rows (11), normalized columns, loss 2^16 tau) and the rate of P89 on 400 random parameter choices, the hierarchy (6) as an integer cutoff (B3 = 4432 holds, 4433 fails; the theorem uses B3 <= 4096), the exclusion radii and floors of P90, the Faa di Bruno counts of P91 by enumerating set partitions, C_6 and C_7 recomputed from the exact coefficient ceilings for all three references with the dyadic Astar and tau, the origin values and the eigenvalue monotonicity of P92 (sympy, exact); sampled derivative comparisons and lambda_min(M) on 949 polar samples (FLOAT) (171 s) | 48 checks; U3 = B3 = 2^107, B4 = 2^114, Astar = 2^105, tau = 2^-126 (state 131); 2^191, 2^201, 2^189, 2^-210 (Mpen2, d2); M(0) = diag(3c + a0, c + 2) |
| P93, P94 | check_p93_p94.py | the four C10 matrix numbers as binary64 rationals and their order against c + 2, 38103/10000 and 19/5; the radial and angular grids regenerated from the producer formula; the padded sine at pi_float/2 (directed, mpmath interval arithmetic); the Bernstein restriction identity on random rational polynomials; the C10 record read directly (every expected cell exactly once, all accepted, minimum equal to the reported value); the exact quadratic Taylor coefficients of chi_xxyy and chi_xxxy at the origin and the determinant inequality of P94; the three bounds of P94 (1) on 338 polar samples of r <= 1/200 (FLOAT) (53 s) | 26 checks; 58640 cells, minimum 3.8103307933669193; d_t b(0, z) >= 0.57935 > 1/4, abs(d_t q(0, z)) = 0.60023 < 20, 2c - 2 + a0 = 11.9209 >= 10 |
| P95 | check_p95.py | the closed forms M = (2c + 1) I + [[-2 chi22 - chi04, chi31], [chi31, chi22]], M_1 = [1 - t(c + e)/5] I + [[-chi04, chi13], [chi13, -chi22]] and M_2 = [1 - c + (16/5) t(c + e)/(1 + 3t)] I + [[chi22 - chi04, (3 chi13 - chi31)/2], [., -2 chi22]] for a generic potential, with t = r^2/(1 + r^2) and e = u.X/r^2, the reflection x -> -x and the eigenvalue lemma (sympy, exact); c and delta of d2 and its 2382 generators from the source record (Legendre factors checked against sympy; 1322 canonical terms); the five fields chi22, chi04, chi31, chi13 and e recomputed by Wirtinger calculus as sums of w^(j+1) P_j(t, z) with exact rational P_j, and their center values (chi22(0) = 1 - c, chi31(0) = chi13(0) = 0, e(0) = (c - 1) cos 2 theta, lambda_min at the center c + 2, c and c - 1) (exact); the six records read directly (status, rectangles equal to their paths, complete binary trees of [0, 1] x [-1, 1] of total area 2, every leaf lower bound positive, the 640-bit rechecks bound by SHA-256 to the primary records and to the polynomial record, the audits and the status); the certified quantities from the recomputed fields in 512-bit Arb at nine points of every leaf, each at least the certified lower bound of its leaf, and on 1551 grid points of the compactified quadrant for each matrix (a sample, not a cover); the five fields against numerical derivatives of the exact potential at 10 points (FLOAT, relative difference 8.0e-29) (57 s) | 29 checks; 41, 79 and 119 leaves; smallest leaf lower bounds 0.0098635 (M, on t <= 1/8), 0.00025868 and 0.00013680 (M_1, M_2, on leaves at t >= 1 - 2^-18 and t >= 1 - 2^-11; for M_2 the certified quantity is (1 + 3t)(lambda_min(M_2) - 1/2)); sampled minima 0.010319 (M, at the center, where lambda_min(M) - 19/5 = c + 2 - 19/5), 0.13102 (M_1) and 0.31032 (M_2, at the center) |
| P96 | check_p96.py | the closed forms of B1 = M_1, B2 = M_2, B3 = M_3, sym DU and V.D log omega from the definitions for a generic potential (sympy); the eigenvalue lemma (2000 exact tests); the targets against 9/10, 1/2, -5/4 and 17/20; the four records read directly (status, every rectangle recomputed from its path, complete binary trees of total area 2, every leaf lower bound positive, the 448-bit rechecks bound by SHA-256 to the primary and polynomial records, which carry the hash of the exact source record); the 20 branch polynomials against numerical derivatives of the exact original potential at 28 points (FLOAT, relative difference 3.4e-25); the four quantities in Arb balls at 2911 grid points of the compactified quadrant (a sample, not a cover) (13 s) | 28 checks; 99, 144, 164 and 49 leaves; sampled extremes 0.99135, 0.61484, -1.20361 and 0.81032 against the targets 0.972875, 0.587238, -1.230876 and 0.810792 |
| P97 | check_p97.py | the remainder identities, B(s), the prefactor 1 and the limit 9/4^beta that fixes the threshold beta > 3/2 (sympy); the scaling and zero-moment identities on stand-ins, the annulus exponent 4^(-3|k - n|), ||K||_1 < 6/5, (1 + 1/n)^3 <= 27/8, the gap contribution 4 log 2 and the gap conditions (exact); C_beta at beta = 2, 5/2, 3, the growth of the truncated beta = 3/2 integral, the bound on three Gaussians, the nested construction with the smooth cutoff of the text on the gaps (FLOAT) (2.4 s) | 25 checks; C_2 = 1.4786, C_(5/2) = 0.65695, C_3 = 0.35875 (FLOAT); the gap lower bound of I(h_N) grows from 1.23 (N = 10) to 5.44 (N = 10^5) |
| P98 | check_p98.py | c, a0, delta and q_j = (j + 1) delta/2 in (0, 1) from the source record; the Taylor-division lemma (binomial series and the ratio (n - q)/(n + 1) symbolic in q; a_n > 0 decreasing for the four exact q_j; the tail bound at sample points in Arb); the stored tail coefficients a_13(q_j); the origin constants b from the degree-four Taylor part of the potential computed from the 860 source coefficients (rho_y(0) = a0, rho_x(0) = 0, Du(0) = diag(c - 1, 1 - c)); H = (1 - t)[sum_j W_j P_j - b]/t recomputed by exact division and equal to the stored H; the six fourth-derivative fields equal to combinations of the P96 polynomials branch by branch; the error constant E of every statement recomputed exactly (exact); the records read directly (47 statements: the 32 original targets as the exact binary64 values of the numerical record, the seven decimals of the numerical summary that an independent audit found rounded inward, each below the stored value it was displayed for, and the eight improved bounds at r <= 1/10; status, rectangles, complete binary trees of [0, t0] x [-1, 1], every leaf below its target, the 448-bit recheck, SHA-256 bindings); an independent adaptive cover of all 47 statements by the mean-value form of s^2 H^2 in 256-bit Arb with H recomputed here; the 32 branch polynomials against numerical derivatives of the exact potential at 28 points (FLOAT, relative difference 7.3e-25), the normalized remainders at r = 0.01, 0.03, 0.1 and sampled maxima (FLOAT) (18 s) | 26 checks; independent cover with 273 cells in all (at most 14 per statement); on r <= 1/10 its largest cell bounds are 3.0157, 1.2064, 0.6204, 0.5837, 0.6568, 0.6204, 0.2821, 0.2917 against 3.04, 1.24, 0.65, 0.59, 0.66, 0.65, 0.285, 0.293 |

Rows marked FLOAT inside these programs (quadrature diagnostics of asymptotic rates) are consistency checks, not
certificates.

P111 (direct exclusion radii) uses no number beyond the exclusion distances 2^57 and 2^21 of the row P73 and exact
rational comparisons: 2^57/(1 + 7 tau) >= 2^77/(2^20 + 7) > 2^56 and 2^21/(1 + 7 tau) >= 2^41/(2^20 + 7) > 2^20 for
0 < tau <= 2^-20, and r_0 < 2^-30. The independent review of the part checked these comparisons in exact arithmetic
(58 checks, including the source binding of the P73 records); that audit is not shipped.

Serialization convention for these programs. Every decisive comparison is made inside the program in exact rational
or outward-rounded interval arithmetic, and its outcome is stored as a boolean in the "checks" field of the output
file; the program fails unless all of them hold. Numbers written to the output files by ordinary float conversion
(rounded to nearest) are displays only, not directed endpoints, even where the field is named lower or upper. Where
an enclosure itself is part of a claim, the output stores exact binary-rational endpoints with directed decimal
bounds: check_p70.py does so for D_1 and the two H_1 norms (D_1 lies in [0.5963473623231940743410784,
0.5963473623231940743410785]; the norms are at most 0.0544608892100416640748345 and 0.0385096640698697380186415), and
check_p71.py stores D_R exactly and each integer floor with its exact rational bound.

### 6i. Global matrix, derivative and decay bounds of the exact refit d2 (P95, P105)

For the exactly admissible refit d2 (numerics file nb_d2_exact, 2382 generators, exponent equal to that of state 131)
the three matrix hypotheses of Theorem D_w hold on the whole plane:

| bound | certificate (folder P95_refit_global_hypotheses) | method | leaves | independent recheck |
|---|---|---|---|---|
| M = (2c + 1) I + sym Du + A >= (19/5) I | nb_d2_exact.M.correlated.json (11861 bytes) | compactified variables t = r^2/(1 + r^2), z = cos 2 theta, w = (1 - t)^(delta/2); exact branch polynomials; correlated Bernstein enclosures with a Taylor remainder for the powers of w, 512 bits | 41 | nb_d2_exact.M.correlated.recheck.json, direct power restrictions at 640 bits |
| M_1 >= (1/2) I, weight omega_1 = (1 + r^2)^(-1/10) | nb_d2_exact.M1.correlated.json (22810 bytes) | as for M | 79 | nb_d2_exact.M1.correlated.recheck.json, 640 bits |
| M_2 >= (1/2) I, weight omega_2 = (1 + 4r^2)^(2/5) | nb_d2_exact.M2.correlated.json (34110 bytes) | as for M, for the quantity (1 + 3t)(lambda_min(M_2) - 1/2) | 119 | nb_d2_exact.M2.correlated.recheck.json, 640 bits |

Each certificate is a complete binary subdivision of [0, 1] x [-1, 1], that is, of the closed first quadrant with t = 1
the point at infinity (the fields are even under X -> -X, and the reflection x -> -x only changes the signs of chi31 and
chi13, which leaves the eigenvalues unchanged), with a positive directed lower bound on every leaf and no failed or
pending cell. audit.json and audit_matrices.json bind the six files and the polynomial
record by SHA-256; status.json records the confirmation of the three matrix covers (the record that check_p95.py
reads), and status_final.json with audit_complete.json (104 hash and completion checks, rerun by consolidate.py)
records the final confirmation of all seven groups of this section, 733 leaves in all. The third computation is check_p95.py (section 6h). The leaf
lower bounds (smallest 0.0098635, 0.00025868 and 0.00013680) are bounds of the cover, not margins of the matrices: at
the center lambda_min(M) = c + 2, lambda_min(M_1) = c and lambda_min(M_2) = c - 1 exactly. 
The fixed derivative bounds and the decay bounds of the reference contract (R = 2^31, decay exponent d = 4/9) are
certified for d2 on the whole plane by four further covers of the same kind (512-bit correlated Bernstein enclosures in
the compactified variables; independent 640-bit recheck by direct power restriction, bound by SHA-256 to the primary
record and to the polynomial and derivative records; tensors are measured by the Euclidean norm of the ordered
Cartesian tensor):

| group | bounds | certificate (folder P95_refit_global_hypotheses) | leaves | independent recheck |
|---|---|---|---|---|
| first derivatives | abs(Du) <= 14/5, abs(D rho) <= 16, r^(4/9) abs(Du) <= 22, r^(4/9) abs(D rho) <= 93 | nb_d2_exact.fourth.correlated.json (23779 bytes) | 36 | nb_d2_exact.fourth.correlated.recheck.json |
| D^2 u | <r> abs(D^2 u) <= 3, r^(13/9) abs(D^2 u) <= 56 | nb_d2_exact.D2u.correlated.json (49879 bytes) | 121 | nb_d2_exact.D2u.correlated.recheck.json |
| D^2 rho | abs(D^2 rho) <= 3, <r> abs(D^2 rho) <= 8, r^(13/9) abs(D^2 rho) <= 93 | nb_d2_exact.D2rho.correlated.json (170965 bytes) | 314 | nb_d2_exact.D2rho.correlated.recheck.json |
| velocity | r^(-5/9) abs(u) <= 22 | nb_d2_exact.u.correlated.json (7075 bytes) | 23 | nb_d2_exact.u.correlated.recheck.json |

The density decay constant 186 of the contract is the sum of the two density bounds 93 + 93. audit_norms_<group>.json
binds each pair of records, the exact algebra audits nb_d2_exact.algebra.base.json and nb_d2_exact.algebra.higher.json
(shipped) and the programs norms_correlated.py, recheck_norms.py and recheck_norms_chunked.py (shipped) by SHA-256. The
exact polynomial record nb_d2_exact.polynomials.json (145 MB) and derivative record nb_d2_exact.derivatives.json
(165 MB) that the covers read are shipped; their hashes
e710cfd7da676e5cbd8431abf783d373e0424b8a5afb7eb45388826b0e924fee and
b568bace2b6e05b08af695d4bc82a2870dc5fd072a0d37159135ea34bdcc036d are stored in every certificate. The seven
independent rechecks are rerun from the bundle by scripts/run_late_rechecks.py (S1_RESTART.md section 3a); from a
fresh restore all seven reproduced the verdicts, leaf counts and leaf bounds of the shipped rechecks, and consolidate.py
reproduced audit_complete.json.

P105 (folder P105_refit_reference_contract: audit.py, audit.json, register.json, status.json) assembles the contract.
audit.py reads the exact source audit of d2, the leading-tail record, the seven P95 records with their rechecks, the
polynomial and algebra records and the audits of P90, P91 and P106, each by SHA-256, and makes 47 exact checks: the
canonical refit, c + (strain at the center) = 1, the center slope a_0 =
47238706681952399067752453371665/4589704466829443526249565650944 > 1, 9/5 < c < 37/20, the unchanged leading potential
and its nonzero density, completeness, independence and polynomial binding of each of the seven covers, the higher
derivative caps C_6 and C_7 of P91 at Astar = 2^189 and tau = 2^-210, the hierarchy with U3 = B3 = 2^191 and
B4 = 2^201, the low matrix threshold 2/5 + (11/10) c <= 487/200 < 19/5, 768 Kstar tau < 1, the two density decay
halves, membership of the residual in the forcing space (P106), and the residual comparison of P90: Mstar(F) >
2^178 * 1936535207 and Mstar(F)/eta > 2^243 for every 1/2 < beta <= 1. Every input of the program is shipped (the
exact source audit of d2, the leading-tail record, the P95 records, the audit records of P90, P91 and P106, and in
certificates/P0_proof_texts the six proof texts whose hashes it checks), and scripts/run_late_rechecks.py reruns it from a restore into a directory named
research (S1_RESTART.md section 3a), where it reproduced audit.json; its scalar comparisons were also recomputed independently in exact arithmetic, and a FLOAT sample of the ten caps is listed in section 8. P95 and P105 do not give
residual smallness: the residual floors of P52 and P90 exclude it for this reference.

### 6j. Independent global bounds for state 131 (P99, P101, P104)

Three further certificates for the exact state 131, each a complete directed Bernstein cover in z = cos 2 theta
and a compactified radial variable, bound by SHA-256 to the exact original coefficients, with an independent recheck
by direct power restriction at higher precision and no floating trigonometric input. P99 and P104 use
t = r^2/(1 + r^2) (t = 1 is the point at infinity); the exterior bounds of P99 are restricted to the stated radii.
P101 uses t = 300/r on r >= 300 (t = 0 is the point at infinity). M_1, M_2, M_3 below are the matrices of (B4) to (B6)
(B1, B2, B3 in the record names), not the weighted principal matrices of the weighted contract. All decimal targets
are exact rationals.

| part | bound | certificate (folder) | leaves | precision (primary, recheck) |
|---|---|---|---|---|
| P99 | A >= -(1/20) I on the whole plane | A_global.json (P99_original_global_signs) | 88 | 384, 448 bits |
| P99 | rho_y >= (1 + r^2)^(-delta/2) > 0 on the whole plane | rho_scaled_global.json | 6 | as above |
| P99 | for r >= 10^4: M >= 4.595633 I, M_1 >= 0.990775 I, M_2 >= 0.620899 I, M_3 >= -1.194644 I | M_r1e4.json, B1_r1e4.json, B2_r1e4.json, B3_r1e4.json | 9, 31, 35, 42 | as above |
| P99 | for r >= 10^6: M >= 4.61399 I, M_1 >= 0.99335 I, M_2 >= 0.62459 I, M_3 >= -1.18993 I | M_r1e6.json, B1_r1e6.json, B2_r1e6.json, B3_r1e6.json | 6, 5, 4, 4 | as above |
| P101 | abs(F(X)) <= (48707/200000) abs(X)^(2 gamma - 1) for abs(X) >= 300, binomial tail included | bound_0243535.json (P101_directed_far_residual) | 10 | 384, 512 bits |
| P104 | r^(2/5) abs(D rho) <= 19.94465, r^(2/5) abs(Du) <= 1.85619, r^(-3/5) abs(u) <= 0.97743 on the whole plane | Drho.json, Du.json, u.json (P104_original_decay_recomputation) | 50, 349, 33 | 448, 576 bits |

Each record has its recheck next to it (<name>.recheck.json); audit.json in each folder binds the records and the
programs (compute.py, recheck.py and the algebra audits, shipped) by SHA-256. P101 also ships its exact sector
reconstruction sectors.json and an exact residual algebra audit with 7192 checks (algebra_audit.json); P104 ships its
exact polynomial record polynomials.json and a third-derivative algebra audit with 3880 checks. These three parts
confirm, by programs independent of the earlier ones, the density sign, the matrix inputs and the three decay
constants used for state 131 (sections 3 and 6e) and give a directed version of the far-field residual bound of the
numerical work. The programs read the research layout of the verification, so they are not run by
run_recomputations.py; they are rerun by scripts/run_late_rechecks.py from a restore into a directory named research
(S1_RESTART.md section 3a), where all 17 rechecks and algebra audits of P99, P101 and P104 reproduced their records.

## 7. Audits of floating-point evaluators

P11_audit/check_grid_enclosures.py and check_series_cap.py (P11.1) record interval re-evaluations of floating-point
residual evaluators used by the numerical work, including a precision cap error found and corrected in a series
routine. They certify only the specific values listed in their JSON outputs.

P11_audit/audit_c8.py (P11.2) is the independent check of the single-mode annular lower bound of the numerical work
described in section 6e, and P11_audit/audit_c9.py (P11.4) that of the combined test of all leading modes computed by
numerics_code/wnorm_cert_multi.py. P11_audit/audit_c2_correction.py (P11.3) re-reads all 40081 saved cells of a floating-point
field-bound summary, checks every decimal upper bound and count, encloses the weighting factor of the origin square at
256 bits, and recombines the saved component upper bounds by exact sums of rational squares. It confirms the corrected
summary bounds (for example |D rho| <= 10.30040 and |D U| <= 1.14601 on the covered cells) conditional on the saved
component enclosures; it is not an independent field certificate and no THEOREM uses it. audit_c8.py and audit_c9.py are rerun by run_checks.py after a
restore with restore_layout.py --relocate; audit_c2_correction.py reads a large record of the numerical work that is not
shipped and is run by the manual procedure of S1_RESTART.md.

## 8. Floating-point data (not certificates)

The residual norms of the refits quoted in the report other than those of section 5b (for example
||<r>^0.7 D^2 F||_2 about 1.85 for the refit m10 and 3.61 for m5, the octave profiles of the weighted Hessian residual,
and the near-origin values |F| and |D^2 F| at r = 1) are FLOAT observations from quadrature on finite grids plus exact
far-field parts, without quadrature error bounds. They are not used in any THEOREM. Where they overlap with section 5b
they agree with the certified values to four or five digits.

The weighted low norm of the residual of state 131 (section 6e) has the FLOAT value L(F) = ||w F||_Hdot^-1 of about
8.807e20 at R = 2^35 (exact far-field sectors with exponent above -2.6 on r > 1, mode-wise radial Green function on a
logarithmic grid of step 0.002 from r = 1 to 3.7e32; the leading sector alone gives the same value to 1e-4; halving
the grid changes L by 2e-5), so 2^(53/2) L(F) is about 8.36e28 and the ratio to eta = 2^-46 about 5.9e42. A second
FLOAT evaluation with the upper cutoff R e^12 gave 7.9e28; the difference (about 10 percent of L^2) is the slowly
decaying part of the integrand beyond that cutoff. The certified lower bound 7.09e26 of section 6e is about 1/118 of
this FLOAT value.

The ten derivative and decay caps of d2 (section 6i) were also sampled by a separate evaluation of the exact generators
(Wirtinger derivatives of the 2382 generators, 400-bit Arb balls at the points of a polar grid of 129 radii from 1e-4
to 1e12, logarithmically spaced, times 91 angles in [0, pi/2]; field values checked against numerical derivatives of
the generator sum at three points, relative difference 6.1e-16). The sampled maxima are 0.05 to 0.87 times the caps:
r^(-5/9) abs(u) 1.0924 (cap 22), abs(Du) 1.1460 (14/5), r^(4/9) abs(Du) 2.4601 (22), abs(D rho) 10.2923 (16, the
value a_0 at the center), r^(4/9) abs(D rho) 27.3077 (93), <r> abs(D^2 u) 1.6438 (3), r^(13/9) abs(D^2 u) 12.9968 (56),
abs(D^2 rho) 2.5999 (3), <r> abs(D^2 rho) 5.2520 (8) and r^(13/9) abs(D^2 rho) 36.6869 (93). This is a FLOAT
consistency check of the certified covers (a sample, not a cover).
