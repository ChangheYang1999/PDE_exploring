# EQUATIONS.md: conventions, derivations, gauges, symmetry, axis regularity, tails, normalization, false solutions

Version: v1.5 (2026-10-23 07:29Z, shift 1). v1.5: section 9.3 summary wording (negative-real-part eigenvalue; closed
subset of a C^2 arc; nonconstant/nonzero-decaying; sublinear growth is covered; the floor implication needs an
absolute global residual) and the 7.2 spectral parentheticals, after the verifier's v1.4 audit. v1.4 (07:19Z): section 9.3 adds Theorem L2 (no hypothesis on the stagnation
set; THEORY_NOTES.md section 7) and corrects the 'nontrivial' qualifier and the numerical consequence. v1.3: section 9.3 updated after the L1 audits (L1 confirmed; the
residual-floor prediction of v1.2 was false and is removed). v1.2: corrections from the independent referee audit (Fourier
classification, Parseval n=0, axial-vector remark, scale gauges with D^2 U, pressure multipoles, R3 Thm 4.3/4.5
statements, centering V(0)=0, seed cylindrical formulas, sampling density, tail facts). v1.1 changes from v1: sections 6.2 (pressure gauge options), 7.1 (complete
affine family, no overall factor), 7.2 (constant solution wording), 8.5 (exact Chae hypothesis), 9.1 (no quantitative
n = 2 bound), after the verifier's first audit. Status of each statement is marked:
[D] derived here by hand, [S] additionally checked symbolically by the script `verify/check_equations.py` in the lead's
artifacts (see section 13), [A] audited by an independent referee, [OPEN] not yet verified.
The numerics and validation codes follow this file. Where this file and the task prompt differ, the prompt's
mathematical statements win and this file must be corrected; please report suspected errors in your NOTES files.

Notation. c_l is the physical spatial-collapse exponent (written c_l throughout; the letter c alone is never c_l).
y in R^3 are physical similarity coordinates, R = |y|, r = sqrt(y_1^2+y_2^2), z = y_3.
The velocity-gradient matrix is G = grad U with entries G_ij = d_j U_i, so (a·grad)U = G a for a vector a.
S = (G+G^T)/2 (strain), W = (G-G^T)/2, W a = (1/2) Omega x a, Omega = curl U.
tr(G^2) = sum_{i,j} (d_i U_j)(d_j U_i). d = 1 - 1/c_l (far-field degree of U).

---------------------------------------------------------------------------------------------------------------------

## 1. Similarity ansatz and the profile equations

### 1.1 Canonical system (E) [D,S]
Let tau = T - t > 0, x_* on the z-axis, y = (x - x_*)/tau^{c_l}, and

    u(x,t) = tau^{c_l-1} U(y),   p(x,t) = tau^{2c_l-2} P(y),   omega(x,t) = tau^{-1} Omega(y),  Omega = curl_y U.

Derivation. d tau/dt = -1 and d y/dt = c_l y / tau. Hence
    d_t u = tau^{c_l-2} [ (1-c_l) U + c_l (y·grad)U ],
    (u·grad_x)u = tau^{c_l-1} tau^{-c_l} tau^{c_l-1} (U·grad)U = tau^{c_l-2} (U·grad)U,
    grad_x p = tau^{2c_l-2} tau^{-c_l} grad P = tau^{c_l-2} grad P,
    div_x u = tau^{-1} div U.
Dividing the Euler equations d_t u + (u·grad)u + grad p = 0, div u = 0 by tau^{c_l-2}:

    (1-c_l) U + (c_l y + U)·grad U + grad P = 0,     div U = 0.                       (E)

All derivatives act on physical similarity coordinates y. The vorticity scaling follows from curl_x = tau^{-c_l} curl_y.

### 1.2 Axial recentering (E_C) [D,S]
With a moving center y = (x - z_c(t) e_3)/tau^{c_l}, d y/dt = c_l y/tau - z_c'(t) e_3 / tau^{c_l}. The extra term in d_t u is
-tau^{c_l-1} tau^{-c_l} z_c' d_3 U = tau^{c_l-2} [ -z_c' tau^{1-c_l} ] d_3 U. With z_c'(t) = -C tau^{c_l-1}, i.e.
z_c(t) = z_* + (C/c_l) tau^{c_l} (check: d/dt of (C/c_l) tau^{c_l} is -C tau^{c_l-1}), this gives

    (1-c_l) U + (c_l y + C e_3 + U)·grad U + grad P = 0,     div U = 0.               (E_C)

Removal of C: Y = y + (C/c_l) e_3 is the canonical variable (x - z_* e_3)/tau^{c_l}, and c_l y + C e_3 = c_l Y, so
U_hat(Y) = U(Y - (C/c_l) e_3), P_hat(Y) = P(Y - (C/c_l) e_3) solve (E). C is a representation freedom, not physics.
Conversely, translating a canonical profile by h along e_3 produces (E_C) with C = -c_l h. Hence, in the canonical
frame C = 0 there is NO residual axial-translation freedom (see section 6).

Define the transport field V = c_l y + C e_3 + U (C = 0 in the canonical frame). Then (E_C) reads
(1-c_l)U + (V·grad)U + grad P = 0, i.e. (1-c_l)U + G V + grad P = 0.

### 1.3 Derived identities used for validation [D,S]
Let delta = div U (zero for an exact profile, but kept here so that numerical defects are accounted for) and let
R_m = (1-c_l)U + G V + grad P be the momentum residual.

(a) Divergence of momentum (pressure Poisson):

    div R_m = delta + V·grad delta + tr(G^2) + Delta P.

  (Uses d_i V_j = c_l delta_ij + d_i U_j.) Therefore, with R_P := -Delta P - tr(G^2),

    R_P = -div R_m + delta + V·grad delta.

  For an exact profile, -Delta P = tr(G^2) = sum_{ij}(d_i U_j)(d_j U_i).

(b) Curl of momentum (vorticity equation). Using curl[(y·grad)U] = Omega + (y·grad)Omega and
curl[(U·grad)U] = (U·grad)Omega - (Omega·grad)U + delta Omega,

    curl R_m = R_omega + delta Omega,   R_omega := Omega + V·grad Omega - (Omega·grad)U.          (V)

  So R_omega = curl R_m - (div U) Omega. A divergence defect contaminates the vorticity identity through delta Omega.

(c) Bernoulli form. With H = |V|^2/2 + P + c_l(c_l-1)|y + (C/c_l)e_3|^2/2,

    (1-2c_l) V + Omega x V + grad H = R_m        (exactly, for any U, P),
    V·grad H = (2c_l-1)|V|^2 + V·R_m.

  For an exact profile with c_l < 1/2, H strictly decreases along every non-stationary trajectory of dY/ds = V(Y)
  (this is [R3, eq. (3.29)-(3.33)] in our notation; see section 9).

(d) Stretching identity at a vorticity maximum. Dot (V) with Omega: |Omega|^2 + (1/2)V·grad|Omega|^2 = Omega·S Omega.
  At an interior maximum y_max of |Omega| (so grad|Omega|^2 = 0) of an exact profile,

    Omega(y_max)·[G(y_max) Omega(y_max)] = |Omega(y_max)|^2,  i.e. Xi·S Xi = 1 with Xi = Omega/|Omega|.

  This is scale invariant and independent of c_l and C. It is a check, not a normalization.

### 1.4 Scaling symmetry [D,S]
If (U,P,C) solves (E_C) then U_a(y) = a U(y/a), P_a(y) = a^2 P(y/a), C_a = aC solve (E_C) for every a > 0, and
G_a(y) = G(y/a), Omega_a(y) = Omega(y/a). Multiplying U by a constant WITHOUT rescaling its argument is NOT a symmetry.

---------------------------------------------------------------------------------------------------------------------

## 2. Independent cylindrical formulation [D,S]

y = (r cos(theta), r sin(theta), z), e_r = (cos, sin, 0), e_theta = (-sin, cos, 0).
U^r = cos(theta) U_1 + sin(theta) U_2, U^theta = -sin(theta) U_1 + cos(theta) U_2, U^z = U_3.
B^r = c_l r + U^r, B^z = c_l z + C + U^z, D = B^r d_r + (U^theta/r) d_theta + B^z d_z (note: c_l y has no e_theta component).

    (1-c_l) U^r     + D U^r     - (U^theta)^2/r   + d_r P       = 0,
    (1-c_l) U^theta + D U^theta + U^r U^theta/r   + d_theta P/r = 0,
    (1-c_l) U^z     + D U^z                       + d_z P       = 0,
    d_r U^r + U^r/r + d_theta U^theta/r + d_z U^z = 0.

These are exactly e_r·R_m, e_theta·R_m, e_3·R_m and div U. The geometric terms come from d_theta e_r = e_theta and
d_theta e_theta = -e_r. Cylindrical vorticity: Omega^r = d_theta U^z/r - d_z U^theta, Omega^theta = d_z U^r - d_r U^z,
Omega^z = (1/r) d_r(r U^theta) - d_theta U^r/r.

Cross-check recipe (validation): evaluate the network at y(r,theta,z) and differentiate with respect to (r,theta,z)
directly (an independent chain of derivatives), form the four cylindrical residuals, and compare with the Cartesian
residual rotated into (e_r,e_theta,e_3), on points with r >= r_min (for example r_min = 1e-2 times the core scale).
Do not evaluate the cylindrical form on the axis; on r = 0 use the Cartesian residual (smooth there). Never divide
by a small arbitrary cutoff r.

---------------------------------------------------------------------------------------------------------------------

## 3. The m = 2 symmetry class

### 3.1 Definition [D,S]
Q = diag(-1,-1,1) (rotation by pi about e_3, det Q = +1). Require

    U(Qy) = Q U(y),   P(Qy) = P(y).

Equivalently U_1, U_2 are odd and U_3, P even under (y_1,y_2) -> (-y_1,-y_2) at fixed y_3. No separate reflection
parity in y_1 or y_2, no z-parity, no theta-reflection, no no-swirl condition, no full inversion parity.
(E_C) is invariant under this symmetry for any C (Q e_3 = e_3, Q commutes with y -> c_l y).

### 3.2 Fourier content [D]
Since Q e_r(theta) = -e_r(theta) = e_r(theta+pi) and likewise for e_theta, the symmetry is equivalent to
U^r, U^theta, U^z, P being pi-periodic in theta: frequencies n in {0, ±2, ±4, ...}, both cosine and sine content.
The Cartesian combinations U_1 ± i U_2 = (U^r ± i U^theta) e^{±i theta} have ODD frequencies; scalar pi-periodicity
must NOT be imposed on U_1 or U_2. Nonlinearity couples all even n; an n in {0,±2} truncation is not invariant.

### 3.3 Group average and non-axisymmetric part [D]
U_axi(y) = (1/2pi) int_0^{2pi} R_{-alpha} U(R_alpha y) d alpha, U_nonaxi = U - U_axi.
In cylindrical components U_axi = (U^r)_0 e_r + (U^theta)_0 e_theta + (U^z)_0 e_z, the n = 0 modes of the
CYLINDRICAL components. (Averaging Cartesian components U_1, U_2 over theta is wrong: it kills the axisymmetric
radial and swirl parts.) Modal coefficients: f_n(r,z) = (1/2pi) int f e^{-i n theta} d theta.
Energy of |n| on an axisymmetric region D: E_0(D) = 2pi int_D (|U^r_0|^2+|U^theta_0|^2+|U^z_0|^2) r dr dz and, for
|n| > 0, E_|n|(D) = sum over the two signs ±n of 2pi int_D (|U^r_n|^2+|U^theta_n|^2+|U^z_n|^2) r dr dz, so that
int_D |U|^2 dy = sum_{|n| >= 0} E_|n|(D) (Parseval; n = 0 counted once). Report e_n(D) = E_n(D)/sum_m E_m(D) for
n = 0,2,4,6,8,... and the same for P and for Omega, on several core balls and shells.
Classification (exact statements): a field is axisymmetric iff every mode n != 0 vanishes; it is four-fold
(invariant under rotation by pi/2) iff every occupied frequency is divisible by 4. E_2 = 0 alone does not imply
four-fold symmetry (n = 4 and n = 6 together have fundamental period pi). The task's search criterion is a
resolvable E_2 well above the error level; report all e_n so that other two-fold patterns are visible.

### 3.4 Other symmetries of the equations (equivalences, not constraints) [D]
For any orthogonal O with O e_3 = ± e_3 (rotations R_beta about e_3, the z-reflection Sigma_z = diag(1,1,-1), vertical
mirror planes), U -> O U(O^T y), P -> P(O^T y) maps solutions of (E_C) to solutions of (E_{C'}) with C' = (O e_3·e_3) C, and
preserves the m = 2 class because O commutes with Q. Candidates related by these maps are the same candidate.
R_beta acts on modes by f_n -> e^{-i n beta} f_n.

### 3.5 Extra symmetries carried by the seed [D,S]
The seed of section 10 satisfies U(Oy) = O U(y) for every orthogonal O commuting with M; this includes -I (full
inversion parity, U odd) and Sigma_z (U_3 odd in z, U_1, U_2 even in z) and therefore Q = -Sigma_z. These two extra
parities must be released: the network must not be built from features that are even/odd in z or in y, and the
initial fit should be followed by training in the full m = 2 class (optionally with a small random z-asymmetric
perturbation), with the z-parity defect ||U(Sigma_z y) - Sigma_z U(y)|| / ||U|| and the inversion defect reported.

---------------------------------------------------------------------------------------------------------------------

## 4. Axis regularity

### 4.1 Cartesian form [D,S]
Fix z. U_h = (U_1,U_2) is odd in y_h = (y_1,y_2), so its Taylor series in y_h has only odd terms; U_3, P are even:

    U_1 = a(z) y_1 + b(z) y_2 + O(r^3),   U_2 = c(z) y_1 + d(z) y_2 + O(r^3),
    U_3 = w(z) + O(r^2),                   P = p_0(z) + O(r^2),
    div U = 0 on the axis:  a(z) + d(z) + w'(z) = 0.

The transverse 2x2 matrix [[a,b],[c,d]] is general (dilation + rotation + traceless symmetric strain). Its traceless
symmetric part is pure n = ±2 content, so genuinely n = 2 horizontal velocity can be O(r) at the axis.
In particular grad U on the axis has the block form [[a,b,0],[c,d,0],[0,0,w']] and V_1 = V_2 = 0 on the axis: the
axis is invariant under the flow of V, and V_3(0,0,z) = c_l z + C + w(z).

### 4.2 Fourier conditions [D]
With f = sum_n f_n(r,z) e^{i n theta}: U_1 + i U_2 = sum_n (U^r + i U^theta)_n e^{i(n+1)theta}, and a smooth complex
function of (y_1,y_2) has its k-th angular mode equal to r^{|k|} times a smooth function of r^2. Hence

    (U^r + i U^theta)_n = r^{|n+1|} g_n(r^2,z),  (U^r - i U^theta)_n = r^{|n-1|} h_n(r^2,z),  U^z_n, P_n = r^{|n|} k_n(r^2,z),

with g, h, k smooth. For n = 0: U^r_0, U^theta_0 = O(r); for n = 2: (U^r + i U^theta)_2 = O(r^3) but
(U^r - i U^theta)_2 = O(r); for n = -2 the roles swap. These conditions are automatic for a smooth Cartesian
representation; a cylindrical-Fourier representation must enforce them (including the parity in r of g, h, k).

### 4.3 Numerical regularity checks [D]
Smooth activations do not prove a smooth limit. Report, under refinement (capacity, sampling, domain), the axis
coefficients a,b,c,d,w,w' at several z, the sampled max of |grad U|, |grad^2 U|, |grad Omega| on the core and on the
near-axis tube r < 0.05 L_core, and their changes between refinement levels.

---------------------------------------------------------------------------------------------------------------------

## 5. Parameterization and exact constraints

### 5.1 Hard symmetry projection [D,S]
For raw networks F (vector) and p_raw (scalar): (S F)(y) = [F(y) + Q F(Qy)]/2, (S p)(y) = [p_raw(y) + p_raw(Qy)]/2.
S is a projection (S^2 = S) onto Q-equivariant fields.

### 5.2 Projection commutes with curl [D,S]
For any proper rotation O (det O = 1) and smooth F, curl_y[O F(O^T y)] = O (curl F)(O^T y). With O = Q = Q^T this
gives curl S F = S curl F. (For an improper O the right side acquires the factor det O = -1: projecting
the potential and the velocity with the same polar-vector law fails for reflections. Reflection-equivariant
velocities can still be built if the potential transforms as an axial vector, A -> det(O) O A(O^T y). Not needed
here since Q is a rotation.) Hence U = curl(S A) is Q-equivariant and exactly
divergence free. The gauge freedom A -> A + grad phi does not need to be fixed.

### 5.3 Cutoffs and tail factors [D]
If U is divergence free, chi U is not (div(chi U) = grad chi · U). Apply envelopes at the potential level,
U = curl(chi A), or correct the divergence explicitly. Coordinate maps that commute with Q (odd componentwise maps
such as asinh(y_i/L), radial maps such as y/sqrt(1+|y|^2)) allow the projection to be applied before or after the
map; in all cases derivatives are with respect to physical y (chain rule through the map).

### 5.4 Representations to compare (campaign branches) [D]
R-flex: A = S NN_A(features(y)), P = S NN_P(features(y)), U = curl A, smooth activations (tanh or similar),
  features built from bounded maps of y that do not impose z- or inversion parity.
R-tail: A = S[ rho^{d+1} N_1(xi) + rho^{2d} N_2(xi) + A_core(y) ], P = P_inf + S[rho^{2d} N_P(xi) + P_core(y)], with
  rho = (1+|y|^2)^{1/2}, xi = y/rho. The second family is needed because the subleading velocity degree 2d-1 differs
  from d by the non-integer d-1 = -1/c_l (section 8); a single network in xi alone yields only integer steps. If c_l
  is optimized, d = 1 - 1/c_l moves with it inside these factors.
R-seed: U = U_seed + curl(S A_corr), P = P_seed + S P_corr (section 10), with the seed fully released (section 3.5).
A direct (U,P) network with a divergence penalty is acceptable for exploration only; then div U must be reported and
driven down separately during refinement.

---------------------------------------------------------------------------------------------------------------------

## 6. Freedoms, gauges and normalization

### 6.1 Continuous symmetries preserving the m = 2 class [D]
(i) scaling U_a(y) = a U(y/a), P_a = a^2 P(y/a), C_a = a C (one parameter);
(ii) pressure constant P -> P + const (one parameter);
(iii) rotation phase U -> R_beta U(R_{-beta} y) (one parameter);
(iv) only if C is optimized: axial translation y -> y + h e_3 together with C -> C - c_l h (one parameter).
There is no horizontal translation (it breaks m = 2) and no Galilean boost compatible with a time-independent
profile. With C = 0 fixed, (iv) is absent: the canonical frame is unique and needs no centering condition.

### 6.2 Normalizations to use (exactly one per freedom) [D]
Scale: fix ONE scale-covariant quantity. Recommended: N_inf[U] := max over a fixed dense core grid of |U| equal to 1
(soft penalty (N_inf - 1)^2, with the location of the max logged and checked to be resolved and interior), or a
smooth surrogate N_p = (int |U|^p w dy / int w dy)^{1/p} with large p and a fixed weight w that covers the transition
layer of the core. Do not use a weight concentrated where U is nearly linear: there N_w[U_a] hardly changes with a and
the gauge degenerates. Log the core size (radius of max |U|, radius of max |Omega|, half-width of |U|) every
checkpoint; reject runs whose core drifts toward the domain boundary or below resolution.
Pressure: ONE constant gauge. Either P(infinity) = 0 built into a representation whose pressure part decays
(for example a decaying envelope with no free additive constant), or P(0) = 0 (or mean of P on a fixed core shell
= 0) with a free additive constant in the representation. Never impose both. Asymptotic tests use grad P or P - P_inf.
Phase: either leave free (a flat direction; harmless for first-order methods) or add a soft gauge
Im[ int P_2(r,z) w(r,z) r dr dz ] = 0. For comparing runs, rotate post hoc to make that quantity real and positive.
Center: canonical C = 0 needs none. If C is optimized, impose V_3(0) = U_3(0) + C = 0 (an axis stagnation point at
the origin). This is always achievable because c_l z + w(z) changes sign along the axis when U decays. Report the
canonical profile via Y = y + (C/c_l) e_3.

### 6.3 Conditions that are NOT gauges [D]
Under scaling, D^k U_a(y) = a^{1-k} (D^k U)(y/a). First derivatives (grad U, Omega, S, and their values at any
point) are scale invariant, so ||Omega||_inf = 1, a prescribed value of d_1 U_1(0), Omega_3(0) = 1, or several fixed
first-derivative amplitudes are genuine constraints on the solution, not gauges. Second and higher derivatives
(k >= 2) are scale covariant, so 0 < ||D^2 U||_inf < infinity permits the valid scale gauge ||D^2 U||_inf = 1 (used
in [R3, (3.7)]); likewise ||U||_inf = 1 (k = 0). A max over a fixed finite grid, or a norm with a fixed spatial
weight, is only approximately scale covariant: these are numerical surrogates whose nondegeneracy must be checked
(log the core size). Some first-derivative components (for example the phase of the n = 2 part of the transverse
strain at the origin) can fix the rotation phase, which is a legitimate use. In the canonical frame (C = 0), U(0) = 0 is also a genuine constraint
(it asserts that the blowup point is a stagnation point of V); it must not be imposed together with another
center condition. Imposing the derivative identities of section 9.2 as constraints is likewise not a gauge.

---------------------------------------------------------------------------------------------------------------------

## 7. False solutions and automated acceptance checks

### 7.1 Exact affine family [D,S]
For any matrix M with tr M = 0 and M + M^2 symmetric, U = M y, P = -y·(M+M^2)y/2 solves (E) exactly for EVERY c_l:
(1-c_l)My + M(c_l y + My) + grad P = (M + M^2) y + grad P = 0. With m = 2 symmetry M commutes with Q, so
M = [[N,0],[0,m_33]] with a 2x2 block N and m_33 = -tr N. By Cayley-Hamilton N^2 = (tr N) N - det(N) I, so
N + N^2 = (1 + tr N) N - det(N) I is symmetric iff N is symmetric or tr N = -1. The complete Q-equivariant affine
family is therefore (i) M symmetric and trace free (irrotational strain), or (ii) tr N = -1, m_33 = 1, N arbitrary,
i.e. M = [[a,b,0],[c,-1-a,0],[0,0,1]]. Family (ii) is NOT invariant under M -> tM for t other than 0, 1: the skew
part of tM + t^2 M^2 is (t - t^2) skew M. Both families can carry n = 2 content. They are unit tests
for every residual code and must be REJECTED as answers: they grow at infinity.

### 7.2 Artifacts to reject for the main target [D]
zero or tiny-amplitude fields; constants (U = u_0 e_3 with P = -(1-c_l) u_0 z is an exact solution of the
equations with a pressure growing linearly at infinity; it is excluded by decay, zero vorticity and the target class); globally affine fields and fields that are affine on the whole
training region with the transition pushed outside it; irrotational fields; axisymmetric fields (every mode n != 0 vanishes, section 3.3);
purely four-fold fields (every occupied frequency divisible by 4; E_2 = 0 alone does not imply this); fields whose structure is supported at the outer boundary of the sampled domain;
effectively two-dimensional fields (negligible d_3 dependence in the core); fields with a growing harmonic pressure
or velocity component (imposed strain); candidates whose residual improves only because the core moves outward or
shrinks below resolution.

### 7.3 Required diagnostics for every candidate checkpoint (automated) [D]
(a) residuals of section 11 on untouched holdout sets, region by region;
(b) e_n(D) for velocity, pressure, vorticity, several D;
(c) non-affinity on core balls B_L: fit b + K y (b = b_3 e_3, K block diagonal by symmetry) in L^2(B_L) and report
    ||U - b - K y||/||U||, ||Omega - mean(Omega)||/||Omega||, ||grad^2 U||·L/||grad U|| on B_L;
(d) far-field decay: fitted local exponents of |U|, |grad U|, |P - P_inf| along many rays (section 8);
(e) 3D dependence: ||d_3 U||/||grad U|| and the distribution of Xi·S Xi on the core;
(f) amplitude: max|U| (gauge), max|Omega|, core sizes;
(g) z-parity and inversion defects (section 3.5);
(h) stagnation set of V with classification (section 9.3).
The affine family 7.1 must pass every residual check and FAIL the decay check, as a test of the acceptance code.

---------------------------------------------------------------------------------------------------------------------

## 8. Far field, finite energy and pressure

### 8.1 Leading behavior [D,S]
For U homogeneous of degree q, (1-c_l)U + c_l (y·grad)U = (1-c_l + c_l q) U. This vanishes for q = d = 1 - 1/c_l.
Candidate matching class (an assumption to TEST, not a theorem):

    U ~ R^d A_inf(y/R),  grad U, Omega = O(R^{d-1}) = O(R^{-1/c_l}),  P - P_inf ~ R^{2d} B_inf(y/R).

For 0.4 < c_l < 0.5: d in (-3/2, -1), d - 1 in (-5/2, -2), 2d in (-3, -2), 2d - 1 in (-4, -3).
A_inf, B_inf are unknown angular functions (not prescribed axisymmetric). Velocity must decay; growing affine
backgrounds are excluded.

### 8.2 Incompressibility of the leading tail [D,S]
With A_inf = A_r n + A_T (n = y/R, A_T tangent): div(R^d A_inf) = R^{d-1}[ (d+2) A_r + div_{S^2} A_T ], so

    div_{S^2} A_T + (d+2) A_r = 0,   and consequently  int_{S^2} A_r = 0 (zero net flux, as for every sphere).

### 8.3 Subleading structure (formal) [D]
Convection of the leading term and the matching pressure gradient have degree 2d-1. On degree q the linear
similarity operator is multiplication by (1-c_l+c_l q); at q = 2d-1 this factor is -1, so a correction U_1 of degree
2d-1 is determined by -U_1 + (U_0·grad)U_0 + grad P_1 = 0 with div U_1 = 0 (a Leray-projected angular problem).
Iterating gives the formal degree sequence d + k(d-1), k = 0,1,2,..., with non-integer spacing -1/c_l; this is not
an exhaustive expansion. Pressure harmonic multipoles: tr(G^2) = d_i d_j (U_i U_j), so int_{B_R} tr(G^2) = O(R^{2d+1})
and int_{B_R} y_k tr(G^2) = O(R^{2d+2}); the monopole vanishes for d < -1/2 and the dipole for d < -1, both true here.
No degree -2 or -3 potential-flow velocity is forced. Higher multipoles can add other degrees (a matched pressure
quadrupole R^{-3} Y_2 gives a velocity correction of degree -4), and the second moments of the source need not
converge in this exponent range, so such coefficients need tail subtraction or matching. Do not insist that the profile is exactly homogeneous outside a finite radius, and do not assume
analyticity in 1/R at a compactified infinity (it would forbid the non-integer subleading powers).

### 8.4 Finite-energy interpretation [D]
int_{|x-x_*|<R tau^{c_l}} |u|^2 dx = tau^{5c_l-2} int_{|y|<R}|U|^2 dy. In a FIXED physical ball |x - x_*| < rho the
natural tail gives int|u|^2 ~ rho^{2d+3} tau^{5c_l-2-c_l(2d+3)} = rho^{2d+3} (exponent of tau is exactly 0), and
u(x,t) -> |x-x_*|^d A_inf((x-x_*)/|x-x_*|) as t -> T: the tail is the time-independent outer field, locally in L^2
iff 2d+3 > 0 iff c_l > 2/5. U itself is not in L^2(R^3) for c_l > 2/5 and this must NOT be required.
Consistency: for c_l < 1/2 the limit |x|^d is not in L^3_loc (3d+3 < 0), as required by [R3, Remark 2.2(b)].

### 8.5 Liouville guardrails on the tail [D, OPEN literature check]
Chae (Comm. Math. Phys. 273 (2007) 203-215, arXiv:math/0601661) proves: if a self-similar profile has
Omega in L^p(R^3) for ALL p in (0, p_1), for some p_1 > 0, then Omega = 0. (Hypothesis taken from the arXiv text;
the published version should be compared.) The natural tail Omega ~ R^{-1/c_l} lies in L^p near infinity only for
p > 3 c_l, so it is not covered. Vorticity decaying faster than every power (exponential decay, compact support)
satisfies Chae's hypothesis and is excluded. Therefore never force a super-polynomially decaying vorticity (for
example an exponential or compactly supported tail on Omega). Keep the leading angular profile A_inf free.
Two further facts [D, referee-checked]: (i) a nonzero smooth angular tail R^d A_inf cannot be both divergence free
and irrotational (its potential would be a harmonic function homogeneous of degree d+1 in (-1/2, 0), which is not
an allowed degree l or -l-1); (ii) multiplying the vorticity equation by p|Omega|^{p-2}Omega and integrating (when
justified) gives (1 - 3c_l/p) int |Omega|^p = int (Xi·S Xi)|Omega|^p, so Omega in L^p with p < 3c_l/(1+K),
K = sup|S|, forces Omega = 0. The natural tail has Omega in L^p only for p > 3c_l, consistent with both.

### 8.6 Pressure is nonlocal: whole-space consistency [D]
On a bounded or truncated domain, P is determined by U only up to a harmonic function; a growing harmonic part
(for example a quadratic harmonic polynomial) acts as an imposed external strain. For an exact decaying profile,
grad P -> 0 and P - P_inf = N[tr(G^2)] with N the Newtonian potential, (N f)(y) = (1/4pi) int f(y')/|y-y'| dy'
(convergent since tr(G^2) = O(R^{2d-2}), 2d-2 < -4). Validation for serious candidates: compare grad P with
grad N[tr(G^2)] (with the tail included in the integral), and compare U with the Biot-Savart velocity of Omega.
Both are owed checks; if not done, report them as unfinished.

---------------------------------------------------------------------------------------------------------------------

## 9. Theoretical guardrails and local geometry

### 9.1 Audit of [R3] (Constantin-Ignatova-Vicol, arXiv:2602.17570v3, 20 Jul 2026) [D; A pending]
Their gamma is our c_l, their ansatz is (E) with C = 0. Results and hypotheses:
- Thm 2.1: finite-energy C^1 data, blowup at T, sup (T-t)^{1+gamma} ||grad omega||_inf < inf  =>  gamma >= 2/5.
  Remark 2.2: if also u in L^inf_t L^p, p >= 2, then gamma >= p/(p+3) (so u in L^inf L^3 forces gamma >= 1/2).
- Thm 3.4: lower bound on a scale-invariant norm of Omega (uses Prop. 3.3: Xi·S Xi = 1 at max |Omega|).
- Thm 3.8: at a zero y_* of V with Omega(y_*) != 0, the local outgoing inequality V(y)·(y-y_*) >= c_*|y-y_*|^2 near y_*
  forces gamma >= c_* + 1/2.
- Thm 3.9: a nontrivial C^2 profile with the decay (3.8) [|U| <= C|y|<y>^{-1/gamma}, |Omega|+|grad U| <= C<y>^{-1/gamma}],
  normalized ||grad^2 U||_inf = 1, whose stagnation set N_V is FINITE and which is locally outgoing at EVERY point of
  N_V, has gamma >= 1/2.
- Thm 4.3: a C^2 AXISYMMETRIC profile with a meridional fixed point (a point (r,z), r > 0, where the meridional
  transport vanishes: c_l r + U^r = 0 and c_l z + U^z = 0) at which the swirl U^theta is nonzero has gamma = 1/2
  (self-similar Kelvin circulation on the invariant loop). Such a point is not a zero of the full field V.
- Thm 4.5: a nontrivial C^2 AXISYMMETRIC profile satisfying (3.5) [U(0) = 0, U = o(|y|)] and (3.8) has gamma >= 1/2.
  Remark 4.6: no nontrivial swirl-free axisymmetric C^2 profile satisfying (3.5), (3.8) exists for any gamma > 0.
Their standing assumption U(0) = 0 in (3.5) ("Galilean symmetry") is, in the canonical frame, a restriction (see
6.3). With C free, the analogous centering is V(0) = U(0) + C e_3 = 0 (not U(0) = 0); it is attainable for a decaying
profile but need not be unique. The proofs of 3.8/3.9 use only zeros
of V and the far-field bound.
Consequences for us: (1) never impose local outgoing at stagnation points as a stabilizer for c_l < 1/2 (Thm 3.9 would
then exclude the target); (2) the axisymmetric branch is excluded for c_l < 1/2 by Thm 4.5, so a c_l < 1/2 candidate
that is nearly axisymmetric deserves extra scrutiny (no quantitative lower bound on the n = 2 part follows from
[R3]; require a resolved n = 2 signal well above the error level, as the task specifies); (3) do not
transplant Thm 4.5 to the m = 2 class.

### 9.2 Local checks [D,S]
At an axis stagnation point (shifted to y = 0, V(0) = 0) with Omega(0) != 0: G(0) = [[a,b,0],[c,d0,0],[0,0,e]] by
symmetry, Omega(0) = (0,0,c-b), the vorticity equation at 0 gives G(0)Omega(0) = Omega(0), so e = 1, and div U = 0
gives a + d0 = -1. The transverse block of grad V = c_l I + G has trace 2c_l - 1 < 0: an incoming transverse direction
is forced. More generally at any zero y_* of V with Omega(y_*) != 0: S(y_*)Omega = Omega and G(y_*)Omega = Omega (since
W Omega = 0), so grad V(y_*) has the eigenvalue 1 + c_l along Omega and two further eigenvalues with sum 2c_l - 1 < 0.
Do not impose Omega(0) != 0 on all branches.

### 9.3 Stagnation-set obstruction (Theorems L1 and L2; informal proofs, each checked by independent audits)
Claim L1. Let 0 < c_l < 1/2 and let (U,P) be a C^2 solution of (E) on R^3 with U(y) = o(|y|) and U -> 0 at infinity.
If the zero set N_V of V = c_l y + U is countable (in particular finite), then U = 0.
Sketch. (1) Backward trajectories of dY/ds = V(Y) stay in a fixed ball (V·y >= c_l|y|^2/2 outside it).
(2) By 1.3(c), H is a strict Lyapunov function, so every alpha-limit set is a connected compact subset of N_V,
hence a single point y_* when N_V is countable. (3) If lambda_max(S) < 1 near the alpha-limit set, then
d|Omega|^2/ds <= -2 eta |Omega|^2 along the backward orbit and Omega(a) = 0. (4) Otherwise grad V(y_*) has an
eigenvalue with negative real part (9.2 if Omega(y_*) != 0; c_l + lambda_min < 0 if Omega(y_*) = 0 and
lambda_max >= 1), so the set of points with alpha-limit y_* lies in countably many images of a local Lipschitz graph of
dimension <= 2 and has measure zero. (5) Hence Omega = 0 almost everywhere, so U is a decaying harmonic field, U = 0.

Theorem L2 (supersedes L1). Same hypotheses without any assumption on N_V, and with U = o(|y|) only: Omega = 0 and
U is constant (U = 0 if it decays). Additional steps (THEORY_NOTES.md section 7): grad H = -[(1 - 2c_l) I + Omega x] V,
so Hess H and grad V have the same kernel at zeros; at points of E = {V = 0, lambda_max(S) >= 1} grad V has rank >= 2,
a positive eigenvalue and an eigenvalue with negative real part (when the rank is 2, two nonzero real eigenvalues of
opposite signs), so near such a point N_V is an isolated point or a closed subset of a C^2 arc; a connected
nonsingleton alpha-limit set meeting E contains a subarc of equilibria (by connectedness), and an orbit returning near an interior point
of that subarc is captured and converges, a contradiction; so every alpha-limit set meeting E is a point of E; a finite
cover of the compact set E and countably many flow times give a null set containing {Omega != 0}.
Consequence: for 0 < c_l < 1/2 there is no nonconstant exact profile of (E) or (E_C) on R^3 that is C^2 with
sublinear velocity, and no nonzero one that decays at infinity, whatever its symmetry, stagnation set or tail
(nonzero constants U = b with P = -(1 - c_l) b·y are exact sublinear solutions). Not covered: c_l >= 1/2, regularity
below C^2, velocity without sublinear growth (including affine backgrounds), other ansatzes (anisotropic, discretely
self-similar, rotating), approximate solutions.
Numerical consequence. L2 does NOT give a quantitative residual floor: U = eps W with W compactly supported and
divergence free, P = 0, has residual -> 0 with limit U = 0. A qualitative floor holds on classes with uniform derivative
and tail bounds and a fixed scale gauge (THEORY_NOTES.md section 8; constant not computed). Hence a sequence of
normalized approximations at fixed c_l < 1/2 whose true whole-space absolute L^infinity momentum residual -> 0 must
leave every such class: derivative bounds blow up, the normalization or the tail envelope fails, or the core drifts.
A relative residual gives this only with a specified uniformly bounded denominator and a global norm; finite-sample
relative training or holdout residuals are insufficient, and a residual may also decrease toward a positive floor.
Track these quantities along every branch. The
c_l = 1/2 control is not constrained by L2.
Full text and audit: THEORY_NOTES.md.

### 9.4 Peak-vorticity identity [D]
See 1.3(d). Check Xi·S Xi = 1 at a carefully located interior maximum of |Omega| (Newton refinement of the max).

---------------------------------------------------------------------------------------------------------------------

## 10. Seed family (initialization only; NOT a profile) [D,S]

M = [[a,b,0],[c_M,-1-a,0],[0,0,1]], chi(y) = (1+|y|^2)^{-1/(2c_l)}, A_seed = -(chi/3) y x (M y), U_seed = curl A_seed,
P_seed = -(chi^2/2) y·(M+M^2) y.
Facts: tr M = 0. The horizontal block N satisfies N^2 + N = -det(N) I (Cayley-Hamilton with tr N = -1), so
M + M^2 = diag(k,k,2) with k = a + a^2 + b c_M: symmetric (and P_seed is axisymmetric).
curl[-(1/3) y x (M y)] = M y for tr M = 0. Explicitly
    U_seed = chi M y + (chi / (3 c_l (1+|y|^2))) [ (y·M y) y - |y|^2 M y ],
which is smooth, divergence free, Q-equivariant, M y + O(|y|^3) at 0, and homogeneous of degree d at infinity with
A_inf(n) = (1 - 1/(3c_l)) M n + (n·M n) n / (3c_l). P_seed has degree 2d.
n = 2 content. For the linear field M y: U^r = r f, U^theta = r g, U^z = z with
f = -1/2 + (a+1/2) cos 2theta + ((b+c_M)/2) sin 2theta, g = (c_M-b)/2 + ((b+c_M)/2) cos 2theta - (a+1/2) sin 2theta.
For the localized seed, with eta = 1/(3 c_l (1+R^2)): U^r = chi r[(1 - eta z^2) f + eta z^2],
U^theta = chi r (1 - eta R^2) g, U^z = chi z [1 + eta r^2 (f - 1)] (symbolically checked). Nonzero n = 2 iff
(a+1/2, b+c_M) != (0,0).
Default a = 0.2, b = -0.4, c_M = 0.7, c_l = 0.45: n = 2 amplitude sqrt(0.49+0.0225) = 0.716 per unit r; k = -0.04;
transverse block of grad V at 0 is a saddle (det = -0.2075).
Extra symmetries to release: see 3.5. The unlocalized U = M y is the exact affine test of 7.1.
Other seeds to use: different (a,b,c_M) including strongly non-axisymmetric strain (a+1/2 large), seeds with zero
axis vorticity (b = c_M), seeds with off-axis Q-paired vortex structures (for example curl of a Q-symmetric pair of
localized vector-potential blobs at (±y_0, 0, z_0)), and z-asymmetric seeds.

---------------------------------------------------------------------------------------------------------------------

## 11. Residuals and normalized metrics for validation

    R_m = (1-c_l)U + V·grad U + grad P,   R_div = div U,
    R_omega = Omega + V·grad Omega - (Omega·grad)U,   R_P = -Delta P - tr(G^2),
with the identities R_omega = curl R_m - R_div Omega and R_P = -div R_m + R_div + V·grad R_div (1.3).
Relative momentum residual on a region D (physical L^2, dy = r dr dtheta dz):
    eps_m(D) = ||R_m||_D / [ (1-c_l)||U||_D + c_l||(y·grad)U||_D + |C| ||d_3 U||_D + ||(U·grad)U||_D + ||grad P||_D ].
eps_div(D) = ||div U||_D / ||grad U||_D. eps_omega(D) = ||R_omega||_D / [||Omega|| + ||(V·grad)Omega|| + ||(Omega·grad)U||]_D.
eps_P(D) = ||R_P||_D / [||Delta P||_D + ||tr(G^2)||_D]. A near-zero denominator is a degeneracy flag.
Far field: the linear terms (1-c_l)U and c_l(y·grad)U cancel at leading order; also report
||R_m||_D / ||(U·grad)U||_D on shells (the nonlinear scale R^{2d-1}). Report region RMS, 99% and 99.9% quantiles
and sampled maxima (never called rigorous bounds). With sampling density q (a probability density with respect to PHYSICAL volume dy on D;
a density in computational coordinates must include the Jacobian), ||f||_D^2 ~ (1/N) sum |f(y_i)|^2/q(y_i).
Validation must reconstruct fields from the saved parameters and metadata alone, include finite-difference or
interpolation cross-checks of the autodiff derivatives at selected points, and check unresolved angular modes and
nonlinear aliasing (for example by evaluating e_n on finer theta grids and comparing).
Regions: core balls B_L, near-axis tube, shells L < R < 2L, 2L..10L, 10L..100L, ..., up to the largest sampled radius,
low-transport regions (|V| small), and neighborhoods of all zeros of V.
Screening targets (not proof thresholds): regional eps_m < 1e-3; strong candidate 1e-5 or better with eps_div
substantially smaller.

## 12. Navier-Stokes diagnostic [D]
With s = -log(tau), canonical rescaled NS: d_s v + (1-c_l) v + (c_l y + v)·grad v + grad P = nu e^{-(1-2c_l)s} Delta v.
For the best candidate report ||Delta U||_D relative to the retained terms on core and tail regions, and its
growth under refinement. No NS claim follows from an Euler profile.

## 13. Unit tests the numerics code must pass (and the validation code independently)
T1 affine family 7.1: R_m = R_div = R_omega = R_P = 0 to round-off for several M and c_l; decay check fails.
T2 seed facts of section 10 (divergence, equivariance, small-|y| expansion, tail degree by fitted slopes).
T3 manufactured field: pick smooth Q-equivariant U_mf = curl(S A_mf), P_mf; compute R_m analytically (symbolic) and
   compare with the code's R_m; check identities 1.3(a),(b) with nonzero div if a non-curl field is used.
T4 Cartesian versus cylindrical residuals on random off-axis points (section 2).
T5 symmetry: R_m(Qy) = Q R_m(y), R_div(Qy) = R_div(y) for a random network.
T6 scaling: residual of (U_a, P_a) equals a times the residual of (U,P) at y/a.
T7 recentering: (E_C) residual of the shifted canonical profile equals the (E) residual (section 1.2).
T8 dtype: all tensors, parameters, optimizer states FP64.
The lead's symbolic checks are in verify/check_equations.py with output verify/check_equations.out.

## 14. Further requirements carried over from the task (added v1.2 after the referee audit)
(a) Domains and angular discretization. If a wedge of angle pi is used (for example a cylindrical-Fourier or sector
    representation), identify theta and theta + pi periodically (rotation by pi, vector components rotated with the
    basis). Never use wall, reflection or slip conditions on the wedge edges. The default Cartesian network with the
    projection S needs no wedge.
(b) Temporary anti-axisymmetry penalties. If a penalty or constraint pushing away from axisymmetry is used early, run
    several strengths, then remove it completely and check that the n = 2 content persists against validation and
    refinement error. Results that need the penalty are artifacts.
(c) Outgoing assessments. Eigenvalues of the nonsymmetric grad V at a zero do not establish a quadratic outgoing
    inequality V·(y - y_*) >= c_*|y - y_*|^2; check the symmetric part c_l I + S(y_*) and nearby trajectories.
(d) Derivative cost. With U = curl A, the momentum residual needs second derivatives of A and the vorticity
    residual third derivatives; the pressure Poisson residual needs second derivatives of P and first of U (second
    of A). Budget autodiff memory accordingly and do not drop R_omega from validation because it is expensive.
(e) Stagnation-set diagnostic (from THEORY_NOTES.md, claim L1, conditional): locate all zeros of V in the sampled
    region, classify them (|Omega|, eigenvalues of grad V and S), and test isolation. Report the result for every
    candidate. A finite root list from a root finder is not a proof that N_V is countable.
