# Full-space pressure (prompt section 7)

Version v9, 2026-10-29T14:12Z

## 1. Pressure equation and the class of admissible pressures

Notation. y is the similarity variable, R = |y|, r the distance from the z-axis, vartheta the polar angle from the
positive z-axis and mu = cos(vartheta); a subscript theta denotes the azimuthal component in cylindrical coordinates
(r, theta, z). c = c_l is the similarity exponent, alpha = (1 - c)/c the decay exponent of U, and W = c y + U the
transport velocity. phi and q are the reduced variables of the pre-registered specification, section 1 (U^r = -r d_z phi, U^z = 2 phi + r d_r phi,
U^theta = r q), eta = Omega^theta/r with Omega = curl U, and R_q, R_eta, R_M are the residuals defined there. a_eff is
the vorticity half-maximum radius, a_eff = sup{R : max_{|y| = R} |Omega(y)| >= max |Omega|/2}, the length unit of the
audits. Provenance tags: [verifier] marks a proof or reproduction by the independent validation, [independent referee]
a result derived or checked by a separately run review with its own code, [lead] a derivation or check by the authors
(with the check script named where there is one), and [primary search] a statement of the numerical search about its
own exports.

Divergence of (1 - c) U + W . grad U + grad P = 0 with div U = 0 gives
    -Delta P = f,   f = (d_i U_j)(d_j U_i) = d_i d_j (U_i U_j).
Hypothesis for the rest of this section: U is C^2 on R^3 and |U| = O(R^{-alpha}), |DU| = O(R^{-alpha - 1}) as
R -> infinity, uniformly in angle. The primary class of the pre-registered specification, section 2 (U = R^{-alpha} F + o(R^{-alpha})) does not
by itself imply the derivative bound, which is therefore an additional assumption. Under it f = O(R^{-2 alpha - 2})
and the Newtonian potential
    P(x) = (1/(4 pi)) int f(y) / |x - y| dy
converges absolutely (radial majorant R^{-2 alpha - 1}, alpha > 0). It is the unique solution of -Delta P = f that tends
to zero at infinity: two such solutions differ by an entire harmonic function tending to zero, which vanishes by
Liouville. Harmonic additions (a constant, a linear function, a multipole, or a growing harmonic polynomial) are
therefore excluded; a constant is fixed by P -> 0, and nothing else is free. Section 3 treats the weaker bound
|DU| = O(R^{-1}).

## 2. Per-mode Green formula [verifier: independent derivation of the Green kernel and Wronskian normalization, tested on manufactured fields; lead: symbolic check for l = 0 to 3, author_checks/sym_checks2.py; independent referee]

With f_l(R) = ((2l + 1)/2) int_{-1}^{1} f(R, mu) P_l(mu) d mu and P = sum_l P_l(R) P_l(mu),
    P_l(R) = (1/(2l + 1)) [ R^{-l-1} int_0^R s^{l+2} f_l(s) ds + R^l int_R^infinity s^{1-l} f_l(s) ds ].
Homogeneous solutions R^l, R^{-l-1}; Wronskian -(2l + 1) R^{-2}; regularity at R = 0 and decay at infinity select the
two integrals. For f_l = O(s^{-2 alpha - 2}) the exterior integrand is O(s^{-2 alpha - l - 1}), integrable for every l.
The exterior integral must be evaluated to infinity from the analytically factored tail (for example s = T/t with a
Jacobi weight), never truncated at a finite sphere.

Interior resonance: the interior integral of the leading tail has integrand s^{l - 2 alpha}; it produces
R^{-l-1} log R exactly when l = 2 alpha - 1, i.e. l = 0 at c_l = 2/3 and l = 1 at c_l = 1/2. In both cases the
coefficient of the resonant leading source mode vanishes identically (double divergence structure,
FAR_FIELD_ANALYSIS.md section 4), so no logarithm arises at leading order. Higher-order coincidences (the first in
1/2 < c_l < 3/4 is at c_l = 3/5, l = 2) can produce R^{-l-1} log R terms: a resonant source term k R^{-l-3} P_l(mu)
contributes (k/(2l + 1)) R^{-l-1} log R P_l(mu), plus a multiple of R^{-l-1} P_l(mu), to P, and this logarithm is
nonzero exactly when k is nonzero [lead check, author_checks/docrev_P_check.py]. Such terms are part of P and are computed
by the same formula, not fitted. Example at c_l = 3/5 (alpha = 2/3), assuming the differentiated expansion of
FAR_FIELD_ANALYSIS.md section 5 with leading coefficients phi = R^{-2/3} A(mu), q = R^{-5/3} B(mu),
A = 0.42 - 0.23 mu - 0.04 mu^2, B = 0.34 + 0.19 mu + 0.13 mu^2: with U_0 the leading term and U_1 the first nonlinear
correction, the cross term 2 tr(DU_0 DU_1) of the source has the resonant coefficient f_2 = -125460142/437653125 of
R^{-5} P_2(mu), so P contains the term (-125460142/2188265625) R^{-3} log R P_2(mu) [verifier exact computation; lead
Cartesian recomputation, author_checks/docrev_P_check.py].

## 3. Equivalence of the reduced system and the primitive equations [verifier proof; lead check of the ray formula]

Hypotheses: U is a C^2 axisymmetric divergence-free field on R^3, the reduced equations R_q = 0 and R_eta = 0 hold
exactly with eta computed from U, and |U| = O(R^{-alpha}), |DU| = O(R^{-1}) uniformly as R -> infinity (alpha > 0).
Let M = (1 - c) U + W . grad U. In cylindrical components M_theta = r R_q and (curl M)_theta = r R_eta, so the reduced
equations say M_theta = 0 and (curl M)_theta = 0; since M is axisymmetric with M_theta = 0, the other components of
curl M are derivatives of M_theta and vanish too, and C^2 regularity extends curl M = 0 to the axis. Hence M = -grad P~
for a function P~ (R^3 simply connected). Under these bounds M is only bounded, which gives P~ = O(|y|). Sublinearity
follows by integrating along rays: with u_n(t) = U(t n) . n and an integration by parts of the dilation term,
    P~(R n) - P~(0) = -c R u_n(R) - (1 - 2c) int_0^R u_n dt - int_0^R [(U . grad) U](t n) . n dt,
where the last integrand is O(t^{-alpha-1}); every term is o(R) uniformly in n. Then -Delta P~ = div M = f, so P~ - P is
harmonic and sublinear, hence constant, where P is the pressure that tends to zero at infinity. Under |DU| = O(R^{-1})
alone this P is the spherical improper Newton potential, the limit as L -> infinity of
(1/(4 pi)) int_{|y| < L} f(y)/|x - y| dy, or equivalently the principal-value stress formula
    P(y) = -|U(y)|^2/3 + PV int K_ij(h) U_i U_j(y - h) dh,   K_ij(h) = (3 h_i h_j - |h|^2 delta_ij)/(4 pi |h|^5);
absolute convergence of the Newton integral is not claimed under this bound. Under the bound of section 1,
|DU| = O(R^{-alpha-1}), it is the absolutely convergent Newton potential of section 1. Conclusion: an exact C^2 decaying
solution of the reduced system satisfies the primitive momentum equation with this pressure. For numerical
approximations no quantitative version is proved: small reduced residuals give no bound on the primitive residual
without a further stability estimate, so the primitive residual R_M with the full-space pressure is an independent
acceptance test (pre-registered specification, sections 6.1 and 9).

## 4. Required computations for a candidate (criterion A7 of the pre-registered specification)

1. Route 1: the per-mode Green formula with the exterior integrated to infinity; enough Legendre modes that the
   last retained modes are below 1e-10 of the largest.
2. Route 2 [verifier: independent derivation of the direct Newton kernel]: the direct free-space Newton integral in
   cylindrical form,
   P(r, z) = (1/pi) int_0^infinity int_{-infinity}^{infinity} rho f(rho, z') K(m) / sqrt((r + rho)^2 + (z - z')^2) dz' d rho,
   m = 4 r rho / ((r + rho)^2 + (z - z')^2), where K(m) = int_0^{pi/2} (1 - m sin^2 t)^{-1/2} dt is the complete
   elliptic integral of the first kind with parameter m, so that the azimuthal integral of 1/|x - y| is
   4 K(m)/sqrt((r + rho)^2 + (z - z')^2) [lead check, author_checks/docrev_P_check.py]; singularity subtraction at the
   target and at axial targets.
3. The two routes agree to 1e-6 relative at >= 20 points (core, axis, matching zone, far field) for label A.
4. Multipole diagnostics: the coefficients of R^{-1} P_0 and R^{-2} P_1 in P, after subtracting the part forced by
   the local expansion (the local Q_0 term at c_l = 2/3, nothing otherwise), vanish for 1/2 < c_l < 3/4; the
   coefficient d_0 of R^{-3} in the l = 0 Gegenbauer component of phi vanishes (these vanishing statements assume a
   differentiated matched expansion, U = R^{-alpha} F + O(R^{-2 alpha - 1}) with one derivative, uniformly in angle; a
   leading-order o(R^{-alpha}) statement alone does not imply them); for l >= 2 the relation between
   the irrotational velocity multipole and p_l (FAR_FIELD_ANALYSIS.md section 5) holds up to the nonlinear forcing
   present at coincident degrees. These coefficients are extracted by fitting the computed P and phi on the shells
   [2^6, 2^11] a_eff with all known tail degrees included.
5. The momentum residual R_M is evaluated with this pressure, never with a pressure fitted to make R_M small.
6. Interface sources [verifier proof; lead hand check of the solid-rotation case: continuity at R = a and the jump of
   d_R P equal to minus the surface monopole; the two examples below checked in author_checks/docrev_P_check.py]. Assume U is
   piecewise C^2 on pieces separated by finitely many spheres R = a, with div U = 0 on every open piece, U and its
   derivatives bounded up to each sphere from both sides, and decay sufficient for the Newton potentials to exist and
   tend to zero (the bounds of section 1 suffice). Then the source of -Delta P = div div(U x U) is the bulk
   f = tr(DU^2) plus surface terms at each sphere: with J = [U (U . n)], F = [(U . grad) U] . n, J_R = J . n,
   D = div_S(J - J_R n) and Legendre coefficients F_l, J_l, D_l, the surface part of P is
   (R/a)^l [a F_l + (l + 1) J_l + D_l]/(2l + 1) for R < a and (a/R)^(l + 1) [a F_l - l J_l + D_l]/(2l + 1) for R > a,
   with jump [P_l] = -J_l. The hypothesis div U = 0 on the pieces is needed for the bulk term: in general
   d_i d_j (U_i U_j) = tr(DU^2) + 2 U . grad div U + (div U)^2 (for U = y the left side is 12 and tr(DU^2) = 3). A
   pressure built from the bulk f alone omits the surface terms, and normal continuity of U alone does not remove them:
   tangential jumps can give F != 0 (solid rotation with angular velocity omega inside R = a and U = 0 outside has
   J = 0 and F = omega^2 a (1 - mu^2)), but need not (a rotation reversed across R = a has a tangential jump and
   J = 0, F = 0). For a candidate, report the interface jumps of U and DU, and P computed with and without the surface
   terms; the difference must be below the A7 tolerance for label A. An exact C^2 profile has no interface terms; their
   size in an approximation is a discretization defect, never evidence about the exact problem.
7. Floating-point form of the per-mode formula [lead; binary64 facts checked in author_checks/docrev_P_check.py]. Write the
   two integrals of section 2 as
       P_l(R) = (1/(2l + 1)) [ int_0^R s (s/R)^{l+1} f_l(s) ds + int_R^infinity s (R/s)^l f_l(s) ds ],
   which is the same expression (R^{-l-1} s^{l+2} = s (s/R)^{l+1} and R^l s^{1-l} = s (R/s)^l). Both ratios lie in
   [0, 1] on their integration ranges, so the ratio powers cannot overflow. They can underflow (0.5^1075 is 0 in
   binary64), which happens only for values below the smallest normal number 2^-1022 (about 2.2e-308); the effect of
   underflow, the rounding of f_l, the quadrature and the mode sum need their own error control. Forming the radial
   powers separately fails at large R and l: R^{l+1} overflows in binary64 once (l + 1) log10 R > 308.25 (log10 of the
   largest binary64 number), for example for l >= 77 at R = 1e4, and R^{-l-1} is then below the normal range. One of
   the exported numerical states has 714 finite and 51 non-finite values among its 765 stored reference pressure
   samples, at three radii: at R = 2848.04, 9 +inf and 8 -inf; at R = 5336.70 and at R = 10000, 17 NaNs each
   [verifier]. The independent pressure values at all 765 points are finite, and the 51 missing stored values are
   excluded only from the comparison with stored values [verifier]. The search attributes the non-finite values to
   overflow of R^{l+1} in its mode formula at the pressure degree used for that state [primary search]; for each degree L
   from 89 to 95 the three radii are exactly the sample radii with (L + 1) log10 R > 308.25 [lead consistency check,
   author_checks/docrev_P_check.py], which is consistent with that attribution but does not establish the floating-point
   cause. A missing reference value must be reported as missing, never as a zero error.

## 5. Five-dimensional stream inverse (consistency check of phi) [verifier: independent derivation]

With Gegenbauer components eta_l, phi_l (weight 1 - mu^2), homogeneous powers R^l and R^{-l-3}:
    phi_l(R) = (1/(2l + 3)) [ R^{-l-3} int_0^R s^{l+4} eta_l(s) ds + R^l int_R^infinity s^{1-l} eta_l(s) ds ].
For eta = O(R^{-alpha-2}) this selects the decaying solution of -Delta_5 phi = eta. A decaying 5D-harmonic function that
is smooth on all of R^5 vanishes (Liouville), and a phi that is smooth in (s, z) is smooth on R^5 = R^4 x R; hence
phi = Delta_5^{-1}(-eta) exactly, with no free harmonic part. The far-field irrotational terms d_m R^{-m-3} C_m^{3/2}
of phi (the 3D multipole l = m + 1 of U) are generated by the moments of eta. Away from resonance, that is when the
tail of eta_m has no term R^{-m-5},
d_m = (1/(2m + 3)) x finite part of int_0^infinity s^{m+4} eta_m(s) ds, read off from the first term of the formula
[lead check for power tails, author_checks/docrev_P_check.py]. At resonance the coefficient depends on a subtraction
convention [verifier; proof with exact symbolic checks; lead check, author_checks/docrev_P_check.py]. Put n = 2m + 3 and
suppose eta_m = a R^{-m-5} for R >= R0, so that int_0^R s^{m+4} eta_m(s) ds = a log(R/R*) + C* there for a chosen
scale R* > 0. The exact inverse for R >= R0 is
    phi_m(R) = R^{-m-3} [ (a/n) log(R/R*) + C*/n + a/n^2 ],
where the exterior integral supplies the constant a/n^2. In this document the homogeneous coefficient d_m at resonance
is what remains after subtracting only the logarithm (a/n) R^{-m-3} log(R/R*); it is d_m = C*/n + a/n^2, not the
interior finite part C*/n alone, and it is reported together with the scale R*. A convention that also subtracts
a/n^2 must say so. The independent numerical reconstruction integrates both terms of the formula and is unaffected.
So these coefficients are global data; d_0 = 0 is the nontrivial constraint of FAR_FIELD_ANALYSIS.md section 6, and
for m >= 1 the relation with the pressure moments p_{m+1} holds automatically for exact solutions (section 3).

For a numerical candidate the inverse formula reproduces phi only when the full distributional source is used. If phi
is decaying, piecewise C^2 and C^1 across every interface (for example globally C^2), the bulk eta is that source, so
the inverse is an identity and the comparison tests only the implementation of the exterior integrals and the fitted
tail coefficients; it is used for that purpose in section 6.3 of the pre-registered specification. For a piecewise phi the bulk inverse misses single layers
(jumps of d_R phi) and double layers (jumps of phi) at the interfaces [verifier proof; lead check of the example,
author_checks/docrev_P_check.py]: phi = 1 for R <= 1 and phi = R^{-3} for R > 1 is continuous, decaying and 5D-harmonic on
each piece, so its bulk inverse is 0, while its distributional source is the single layer 3 delta(R - 1). A bulk-only
discrepancy then measures interface defects, and the inverse including the interface layers is the identity test. For
one failed piecewise export the bulk-only potential and gradient errors at 20 points were 5.2e-7 and 4.4e-6, against
2e-14 with the layers [verifier]; this confirms the reconstruction of that field, not its smoothness.

## 6. Angular bandwidth of the bulk source [verifier proof; lead cross-check]

On a radial piece where phi and q are polynomials in mu of degree at most N and M (with radial derivatives through order two
in the same spaces), write S = 1 - mu^2 (that is sin^2(vartheta), not the sine) and
    A = 2 mu phi - S phi_mu,   B = -(2 phi + R phi_R),   C = R q.
Then U_R = A, U_vartheta = sin(vartheta) B and U_varphi = sin(vartheta) C, where U_varphi is the azimuthal component
(U^theta above). The Cartesian gradient written in the orthonormal spherical frame (rows: components, columns:
directions) is
    [ A_R                   -sin(vartheta)(A' + B)/R      -sin(vartheta) C/R ]
    [ sin(vartheta) B_R     (A + mu B - S B')/R           -mu C/R            ]
    [ sin(vartheta) C_R     (mu C - S C')/R               (A + mu B)/R       ]
(prime: d/dmu), so the bulk source is
    f = tr(DU^2) = A_R^2 + (A + mu B - S B')^2/R^2 + (A + mu B)^2/R^2 - 2 S (A' + B) B_R/R - 2 S C C_R/R
        - 2 mu C (mu C - S C')/R^2,
a polynomial in mu of degree at most D = 2 max(N,M) + 2 on that piece (the first four terms at most 2N + 2, the last two
at most 2M + 2). If this bound holds on every radial piece, the Newton kernel, which is rotation invariant, gives a bulk
pressure with no Legendre modes above D, and an n-node Gauss-Legendre projection of the retained modes l <= L is exact in
exact arithmetic when 2n - 1 >= D + L. A bound on one piece alone does not suffice, because a source mode on another
piece generates that mode's harmonic pressure on this piece (f_34 = 1 on 2 < R < 3 and zero elsewhere gives
P_34 = C_34 R^34 with a constant C_34 != 0 for R < 2) [lead check, author_checks/docrev_P_check.py]. Interface distributions (section 4 item 6),
radial quadrature and rounding are separate. Cross-check [lead; author_checks/topic92_check.py, 15 checks, all pass]: the frame
matrix was re-derived from the standard axisymmetric gradient formulas and the result checked by a different route:
the velocity is built directly in Cartesian coordinates as U_x = -x phi_z - y q, U_y = -y phi_z + x q,
U_z = 2 phi + x phi_x + y phi_y with generic rational radial coefficients, its divergence vanishes symbolically, the
Legendre coefficients of tr(DU^2) above D are at most 3e-46 relative at 50 digits for (N,M) = (3,2), (2,4), (4,4), the
coefficient of degree D is nonzero for these generic fields, and the spherical formula and the components A, B, C agree
with the Cartesian computation at random points and at the poles to 7e-48.

Attainment and its limits [verifier proofs; lead cross-check]. The bound is not always attained: phi = 0, q = z^16 on an
annulus has M = 16 and f = -2 z^32 of degree 32, and q = exp(-R^2) has f = exp(-2 R^2)(-2 + 4 R^2 (1 - mu^2)) of degree 2
whatever larger M is allowed in the representation. A pressure truncated at Legendre degree 32 therefore can omit source modes
when max(N,M) > 15, and whether it does depends on the nonzero source coefficients; a bandwidth statement for the full-space
pressure needs the degree bounds on every radial piece. If phi = a(R) mu^N + lower powers and q = b(R) mu^M + lower powers, the
coefficient of mu^D in f is T_phi for N > M, T_q for M > N and T_phi + T_q for N = M, where
    T_phi = (N+2)^2 (a')^2 + [(-N a - (N+1) R a')^2 + (N a - R a')^2]/R^2 + 2 [N(N+3) a - R a'][-3 a' - R a'']/R,
    T_q = 2 b (R b' - M b)
(prime: d/dR here). For a = R^k, T_phi = 2 R^(2k-2) (k-N)(k^2 + (N+5)k - N), which at k = N + 2 is (8N^2 + 40N + 56) R^(2N+2) > 0;
for b = R^k, T_q = 2 (k-M) R^(2k), which is 4 R^(2M+4) at k = M + 2 and zero at k = M (the z^16 example). So phi = R^2 z^N and
q = R^2 z^M attain the bound for every N and M, and a nonzero degree-D source coefficient forces a nonzero degree-D pressure
coefficient somewhere in radius (separated equation p_D'' + 2 p_D'/R - D(D+1) p_D/R^2 = -f_D). Evaluated exactly at R = 1 from
the stored binary coefficients, each of the 13 noncritical exported states examined (c_l > 1/2) has a nonzero top source
coefficient of Legendre degree 50, 66 or 88 (sizes about 1e-11 to 6e-9, 7e-21 to 2.5e-19 and 1e-25), so the bulk Newton
pressure of each of these 13 states has modes above degree 32; this gives no lower bound on the pressure error. For the
critical-exponent state (c_l = 1/2) the top source degree is 26, which gives no such conclusion. Check [lead;
author_checks/topic92_attain_check.py, 23 checks, all pass]: it compares the mu^D coefficient of f, obtained from the Cartesian
Jacobian of generic fields with lower angular powers and negative radial powers, with the formula for (N,M) = (4,2), (2,5),
(3,3) to 1e-35 relative at 50 digits, verifies the closed forms for symbolic k, N, M and the Jacobi expansion of the ball basis,
and recomputes from the raw coefficients the exact degree-50 and degree-88 coefficients of two exports (agreeing to 11 digits
with the values of the exact computation). The finite-truncation changes seen when the pressure degree of exported states was raised from
32 to 40, and their disappearance at degrees 64 to 80 for the states refined that far, are consistent with these small high
modes.

Full-bandwidth pressure checks [verifier]. For eight of the exported numerical states (source degree bound D = 50 for four of them and 66 for four) the bulk Green pressure was recomputed independently at 20 retained points at three
angular/radial quadrature levels, each with Legendre degree above D (degrees 64 to 96) and with 2n - 1 >= D + L for its n
angular nodes and degree L. The last refinement changed P by at most 4.7e-12 and grad P by at most 1.1e-12; the separate
direct Newton integral agrees with the finest Green values to 1.4e-8; the 765 pressure samples stored with each of these
exports are all finite and differ from the independent values by at most 8.7e-5 (summary of the published records in author_checks/pressure_bandwidth_summary.py). For the state of section 4 item 7
(D = 88, degrees 96 to 112) the last refinement changed P by 4.1e-13 and grad P by 3.8e-13, the direct Newton integral
agrees to 1.5e-8, and its 714 finite stored samples differ by at most 4.5e-5; at degrees 32 and 40, which omit bulk source
modes of that state, the change from degree 32 to 40 was 6.1e-5 in P (7.9e-5 in grad P) and the direct Newton integral
differed from the degree-40 values by 6.4e-5. All these numbers are absolute differences in the working coordinates of
each export. They are finite-point comparisons only: uniform pressure and gradient error bounds (criterion A7 of the pre-registered specification) are not
established, the degree theorem excludes omitted bulk modes above D in exact arithmetic but is not a bound for
floating-point quadrature or for a piecewise stress distribution (section 4 item 6), and the checks change no
rejection of a state.

## Revision history

- v1, 2026-10-28T18:39Z: first version.
- v2, 2026-10-28T20:00Z: states the differentiated-expansion hypothesis of section 4 item 4.
- v3, 2026-10-28T20:24Z: adds section 4 item 6, interface sources for piecewise representations.
- v4, 2026-10-29T07:24Z: adds section 6, the angular bandwidth of the bulk source.
- v5, 2026-10-29T08:00Z: corrects the omission consequence of section 6 and adds attainment.
- v6, 2026-10-29T09:51Z: adds section 4 item 7, the floating-point form of the per-mode formula.
- v7 applies an independent mathematical review: the derivative-decay hypothesis of section 1 and the two convergence notions of section 3 (no quantitative residual estimate); resonant logarithms only for nonzero resonant source coefficients, with the exact c_l = 3/5 example; definitions of K(m), a_eff and the notation; incompressibility on every piece and the two tangential-jump examples in section 4 item 6; underflow and the three-radius distribution of the non-finite stored samples in item 7; the resonant subtraction convention and the piecewise qualification of the stream inverse in section 5; the every-piece condition and the critical-state wording in section 6; the full-bandwidth pressure checks; descriptive provenance tags in place of dated references.
- v8, 2026-10-29T10:56Z: the full-bandwidth paragraph covers eight exported states (three further verifier records).
- v9, 2026-10-29T14:12Z: the constant of the example P_34 in section 6 is written C_34 (c denotes c_l in this document).
