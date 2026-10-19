# SPEC.md: admissible class, velocity law, normalization and checks (IPM Setting I)

Version v4.19, 2026-10-19T11:36:03Z (lead; v4.18 2026-10-19T06:18:36Z, v4.17 2026-10-19T04:11:33Z, v4.16 2026-10-19T03:55:00Z, v4.15 2026-10-19T03:46:06Z, v4.14 2026-10-19T03:14:02Z, v4.13 2026-10-19T01:47:15Z, v4.12 2026-10-19T01:26:50Z, v4.11 2026-10-19T01:07:30Z, v4.10 2026-10-19T00:26:16Z, v4.9 2026-10-18T21:46:58Z, v4.8 2026-10-18T17:43:51Z, v4.7 2026-10-18T08:19Z to 09:30Z, v4.6 2026-10-18T07:16Z, v4.5 2026-10-18T04:01Z, v4.4 2026-10-18T00:35Z, v4.3 2026-10-17T22:42Z, v4.2 2026-10-17T21:23Z, v4.1 2026-10-17T20:41Z, v4 2026-10-17T20:21Z). Supersedes v3 (2026-10-17T19:47Z), v2 (2026-10-17T18:13Z) and v1 (2026-10-17T17:54Z). Changes are logged at the bottom.
Status: the section 4 items are lead derivations. External referee audits: v1 (18:10Z), analysis v2 (audit2, 18:45Z), analysis
7.3 and 8 (audit3, 19:22Z); their corrections are incorporated. Verifier audit: Lemmas 1-5 confirmed (VERIFY_REPORT Parts
3, 4, 6); the positivity repair confirmed (E6), D9 checked as identities (G10) and evaluated on one early trial (G4); Lemma 6 is R11 of FINAL_REPORT section 3,
with a finite zero set of the limit field assumed (G107 item 5). The proved statements as finally worded are R1 to R12 of FINAL_REPORT
section 3, checked by the verifier and by an external referee. Full arguments: notes/analysis.md (lead lane).
Numerics and verifier lanes: follow sections 1 to 6. Section 7 lists out-of-class regimes that are not primary targets.

## 0. Conventions (checked symbolically, scripts/check_kernels.py in the lead lane)

- X=(x,y), r=|X|, x=r cos(theta), y=r sin(theta). Q = open first quadrant {x>0,y>0}.
- Profile system: W.grad(rho) = rho, W := c_l X + U, U = (-psi_y, psi_x), -Laplace(psi) = d_x rho.
  div U = 0, curl U := d_x U_2 - d_y U_1 = Laplace(psi) = -d_x rho, div W = 2 c_l.
- Fourier symbols: U_1 = (xi1 xi2/|xi|^2) rho^, U_2 = -(xi1^2/|xi|^2) rho^, i.e. U = (-R1R2 rho, R1^2 rho).
- Kernel form (G = -(1/2pi) log r): U_1(X) = PV int K1(X-Y) rho(Y) dY, K1(Z) = -(1/pi) z1 z2/|Z|^4;
  U_2(X) = -rho(X)/2 + PV int K2(X-Y) rho(Y) dY, K2(Z) = (1/(2pi)) (z1^2 - z2^2)/|Z|^4.
- Parity: rho even in x, odd in y  =>  psi odd/odd, U_1 odd in x even in y, U_2 even in x odd in y, U(0)=0.
  The two axes are invariant lines of W (W_1=0 on x=0, W_2=0 on y=0).
- Center: rho = x^2 y a(x,y), a even/even, a(0)=1. In polar coordinates x^2 y = (r^3/4)(sin(theta) + sin(3 theta)).
- c := psi_xy(0). Near 0, U = (-c x, c y) + O(r^2) and W = ((c_l - c) x, (c_l + c) y) + O(r^2).
  The x^2 y coefficient of the PDE gives 3 c_l - c = 1. The eigenvalues of DW(0) are
  lambda1 = c_l - c = 1 - 2 c_l (x direction) and lambda2 = c_l + c = 4 c_l - 1 (y direction).

## 1. Scaling facts (used to fix normalization)

- rho -> L rho(X/L) (L>0) maps solutions to solutions with the same c_l and multiplies a(0) by L^{-2}.
  So a(0)=1 fixes the scale, but the SIGN of a(0) is invariant: a(0)=+1 and a(0)=-1 are different problems.
  (L=-1 acts trivially on the parity class.) We study a(0)=+1 as the prompt says.
- Amplitude scaling: for (c_l X + U).grad rho = c_rho rho, the map rho -> lambda rho sends (c_l, c_rho) to (lambda c_l, lambda c_rho)
  [corrected in v2]. Setting c_rho = 1 removes this freedom.
- Physical meaning (dynamic-rescaling variables, d tau/dt = C_rho C_l, C_rho = e^{-tau}, C_l = e^{c_l tau}):
  c_l > 1: finite-time focusing, T - t ~ e^{(1-c_l) tau}, rho_phys = (T-t)^{alpha} rho(X/(T-t)^{1+alpha}), alpha = 1/(c_l-1).
  0 < c_l < 1: infinite-time focusing. c_l <= 0: no focusing.
  A profile with far field rho ~ r^k Theta(theta) matches an outer state |Z|^k Theta(theta); k = 1/c_l.

## 2. Admissible class A (primary target)

A profile (rho, c_l) is in class A_m (m >= 2 an integer, or m = infinity) if:
 (A1) rho in C^{m,alpha}_loc(R^2) for some alpha in (0,1), real, even in x, odd in y.
 (A2) rho = x^2 y a(x,y) near 0 with a continuous, even/even, a(0)=1 (for m = infinity, a smooth: the prompt's strong setting).
 (A3) Sublinear growth: there are C and gamma < 1 with |rho(X)| + (1+|X|) |grad rho(X)| <= C (1+|X|)^gamma.
 (A4) U is given by the canonical velocity law of section 3, and (c_l X + U).grad(rho) = rho holds pointwise on R^2.
The prompt's strong setting is A_infinity. Finite regularity at the center is possible (Lemma 5), so every candidate must report
its measured regularity. A candidate in A_m with finite m must be described as such and never as A_infinity.
Note on the numerical ansatz [v2]: (A2) imposes the x^2 y factor only near 0. A GLOBAL ansatz rho = x^2 y b(x,y) (b even/even)
also imposes rho = O(x^2) along the whole y-axis. This is automatic if W_2(0,y) > 0 for all y > 0 (transport along the invariant
y-axis, analysis.md 2.5); otherwise it is a restriction. Any candidate built on a global factor must therefore report
min over y>0 of W_2(0,y)/y, which must be > 0 for the restriction to be harmless.

## 3. Canonical velocity law (three equivalent descriptions)

For rho satisfying (A1),(A3):
 (V1) Modal Green function. Write d_x rho = sum_{n>=1} f_n(r) sin(2 n theta) and psi = sum_{n>=1} psi_n(r) sin(2 n theta)
      (odd/odd functions contain only sin(2 n theta); no constant mode). Then
        psi_n(r) = (1/(4n)) [ r^{-2n} int_0^r s^{2n+1} f_n(s) ds + r^{2n} int_r^inf s^{1-2n} f_n(s) ds ].
      Since |f_n(s)| <~ s^{gamma-1} and gamma < 1, every tail integral int_r^inf s^{1-2n} f_n ds converges absolutely
      (it needs gamma < 2n-1; n=1 is the binding case). No subtraction and no free constant appear.
      rho = sum_{m>=0} rho_m(r) sin((2m+1) theta) and
        d_x[rho_m sin((2m+1)theta)] = (1/2)[rho_m' - (2m+1) rho_m/r] sin((2m+2)theta) + (1/2)[rho_m' + (2m+1) rho_m/r] sin(2m theta).
 (V2) Symmetric truncation: U(X) = lim_{R->inf} [ -rho(X)/2 e_2 + PV int_{|Y|<R} (K1,K2)(X-Y) rho(Y) dY ] (the e_2 term only in U_2).
      For parity-symmetric rho the subtracted term int_{|Y|<R} K(-Y) rho(Y) dY vanishes identically, and the limit converges for gamma < 1.
      Moreover |U(X)| <= C (1+|X|)^gamma (no logarithm) and U in C^{m,alpha}_loc.
 (V3) Uniqueness characterization: U is the unique field with div U = 0, curl U = -d_x rho (distributionally), U_1 odd in x,
      U_2 odd in y, and |U(X)| = o(|X|) as |X| -> inf.
      Proof of uniqueness: a difference D is divergence-free and curl-free, so D is harmonic and D_1 - i D_2 is entire. The o(|X|)
      growth makes D constant (Cauchy estimate), and parity gives D(0)=0, so D = 0.
 Status: the external audit confirmed V1 = V2 = V3. It added one remark: convergence of the modal series comes from the elliptic
 construction, not from the individual tail integrals.
Gauge: psi -> psi + lambda x y adds U -> U + lambda(-x, y). This is linear growth, excluded by (V3), and in (V1) it is the
homogeneous solution r^2 sin(2 theta) of mode n=1, which the Green function excludes. Higher harmonic odd/odd polynomials
(r^{2n} sin(2n theta), n>=2) are excluded the same way. Consequently psi_xy(0) is a functional of rho. Under (A2):
   c = psi_xy(0) = (1/2) int_0^inf f_1(s)/s ds = int_0^inf rho_1(r) r^{-2} dr = (1/pi) int_{R^2} rho(X) sin(3 theta) r^{-3} dX,
where rho_1 is the sin(3 theta) coefficient of rho (absolutely convergent). Without (A2) the general formula is
   c = int_0^inf rho_1 r^{-2} dr - rho_y(0)/4.
[v2] The boundary term at the origin vanishes only because rho = O(r^3). For example, rho = y e^{-r^2} gives c = -1/4.
Physical justification [conditional]: suppose c_l > 1 and the physical outer strain is bounded. Then its contribution to the
rescaled strain is proportional to (T - t) and disappears in the self-similar limit, so no lambda x y term is present. This
assumes the outer strain is bounded and that the matching limit exists. It is a motivation, not part of the definition; the
definition is (V3).

## 4. Lemmas (lead derivations; external audit of v1 done, verifier audit pending; full arguments in notes/analysis.md)

Lemma 1 (forced regime) [audit: correct after repair; the repair is incorporated]. In class A_m (m>=2), every nonzero profile has
 0 < gamma < 1 and c_l >= 1/gamma > 1.
 - Along an escaping characteristic with rho(X0) != 0: e^{-c_l s} X(s) -> V != 0 and
   rho(X(s))/|X(s)|^{1/c_l} -> rho(X0)|V|^{-1/c_l}.
 - Bounded characteristics carry rho = 0.
 - Uniform bound: |rho(X)| <= C(1+|X|)^{1/c_l}.
 The proof uses the quantitative bound |U| <= C(1+r)^gamma. The qualitative statement U = o(r) is not enough.
Lemma 2 (no cycles) [audit: correct, conditional as stated]. div W = 2 c_l > 0, so W has no periodic orbit and no separatrix
 cycle bounding a region. Backward orbits are bounded.
 - IF the zero set of W is finite, every backward orbit converges to a zero of W.
 - If the zeros are isolated, their indices sum to +1; the origin is a saddle of index -1.
 Finiteness is a hypothesis, not proved.
Lemma 3 (first x-axis stagnation point) [audit: correct and strengthened]. Let w(x) = W_1(x,0), h(x) = d_y W_2(x,0) and
 g(x) = rho_y(x,0). Then w g' = (1-h) g and w' + h = 2 c_l. The first positive zero x* of w exists and g > 0 on (0, x*).
 For rho in A_2 the following holds AUTOMATICALLY, with no nondegeneracy assumption: w'(x*) = 2c_l - 1 > 1, h(x*) = 1 and g(x*) > 0.
 So P = (x*,0) is a hyperbolic source with eigenvalues (2c_l - 1, 1), and psi_xy(P) = 1 - c_l < 0.
Lemma 4 (sign and fixed-W rigidity at P) [audit: correct in this form]. Write W_2 = y b(X) (b(P) = 1) and
 eta_P(X) = y exp(-I(X)), I(X) = int_{-inf}^0 [b(Phi_t X) - 1] dt (convergent for X in the basin of P).
 - rho = C eta_P on the basin of P in the upper half plane, with C = rho_y(P) > 0.
 - In particular rho > 0 on every orbit in Q emanating from P.
 - Under the minimal configuration (Hmin: the zeros of W in the closed quadrant are exactly 0 and P), rho > 0 in all of Q.
 [v3, audit2: correct with repair, valid in A_2] Under (Hmin) also rho(0,y) = 0 and k(y) = d_x^2 rho(0,y)/2 > 0 for all
 y > 0 (k(y_t) J(t)^2 = e^t k(y_0) along the y-axis, J = exp int d_x W_1(0,y_s) ds; needs only C^2). Positivity is in Q.
 This is rigidity for the fixed field W. It does not by itself give uniqueness of the coupled profile.
Lemma 5 (regularity at the center) [audit: exponents correct; regularity inference qualified as below].
 G_j(x) := d_y^j rho(x,0)/j! solves w G_j' + (j h - 1) G_j = F_j, where F_j depends on the lower jets, their x-derivatives and
 the velocity jets. For example F_3 = -A_2 G_1' - B^W_3 G_1, with W_1 = w + A_2 y^2 + ... and W_2 = h y + B^W_3 y^3 + ... .
 Near x = 0 the homogeneous solution is |x|^{p_j} times a smooth even nonvanishing factor, with
 p_j = (j lambda2 - 1)/|lambda1| = 2j + (j-1)/(2c_l - 1).
 - p_1 = 2 (the x^2 y term).
 - p_3 = 6 + 2/(2c_l - 1) lies in (6,8) and is never an even integer for c_l > 1 (p_3 = 7 at c_l = 3/2).
 Proved:
 - If rho is C^infinity near the origin, then B_3 = 0, where B_3 is the coefficient of the homogeneous solution in G_3
   (Frobenius, non-resonant exponent). The same holds for every odd j with p_j not an even integer, which is infinitely many j.
 - (Trace) B_3 != 0 implies rho is not C^10 (if p_3 <= 7) or not C^11 (if p_3 in (7,8)).
 Not proved:
 - The sharper statement "C^6 but not C^7/C^8". It needs a uniform 2D expansion through the saddle (a saddle-passage argument),
   which has not been written.
 - That B_3 != 0 for actual profiles. There is no independence or transversality result.
 HEURISTICS: "smooth profiles are isolated in c_l" and "a generic candidate is in A_6 but not A_infinity".
 Numerics must MEASURE B_3 (section 6, D7).
 [v3] B_3 from the axis function w alone (notes 7.3; audit3: correct with repair). With A = 2c_l - 1, beta = 2/A, g0 = a(0):
   g'/g = (w' - A)/w on (0, x*),  H = N g^{3+beta} |w|^{-beta},  N = A^beta / g0^{3+beta},  a2 = (g' - w'')/2,
   B_3 = (1/(3N)) f.p. int_0^{x*} (a2/g^3)' m^{beta-1} dx,  m = |w|/g.
 The finite part requires smooth axis data or an explicit expansion of the integrand x^{1-p_3}(k0 + k2 x^2 + k4 x^4 + O(x^6));
 C^4 alone is not enough (audit2 counterexample with a log term). At A = 2: B_3 = a2(P)/(6 g(P)^3) = w''(P)(g(P) - 2)/(24 g(P)^3)
 (g0 = 1). Local constraints give no sign: compatible axis data realize every sign of B_3 for every A > 1 (audit3).
Lemma 6 (c_l -> infinity is degenerate) [v3; audit3: lemma correct, use for sequences conditional]. With F = rho/c_l the
 limit problem is (X + U[F]).grad F = 0, F odd in y, psi_xy[F](0) = 3. It has no C^1 solution with U[F] in C^1, U[F] = o(|X|)
 and finitely many zeros of X + U[F]. A sequence of profiles with c_l -> infinity converges to such a limit only under
 C^{1,alpha}_loc convergence, uniform tails lim_R sup_n int_{|Y|>R} |F_n|/|Y|^3 dY = 0, and a finite zero set of the limit
 field; without uniform tails distant mass can keep a nonzero strain (F_n = R_n f(X/R_n)).

## 5. Required numerical formulation

 (N1) Unknowns: rho (or a) and c_l. Enforce parity and the x^2 y factor analytically (e.g. rho = x^2 y a with a even/even, or
      polar modes rho = sum rho_m(r) sin((2m+1)theta) with the r^3 behavior built in). Enforce a(0)=1 analytically or as an
      exact constraint. Do not fit c_l freely: c_l = (1 + c)/3 with c computed from the velocity law (V1). Check it a second way
      with c = int_0^inf rho_1 r^{-2} dr or the kernel integral (section 3). See the note at the end of section 2 on global factors.
 (N2) Velocity: law (V1) (or (V2) with a separately verified equivalence). No extra harmonic term, ever.
 (N3) Far field: the expected behavior is rho ~ r^k Theta(theta), k = 1/c_l in (0,1), with Theta(0)=0 and (if no stagnation point
      on the y-axis) Theta(pi/2)=0 to second order. Corrections are in powers r^{k-1} (from U.grad rho) and multipole terms.
      Lemma 1 proves |rho| <= C r^k and convergence along each characteristic. It does NOT prove that a smooth limit Theta
      exists at fixed angle, or that the correction series exists; both must be checked numerically.
      Acceptable closures:
      (a) truncated disk r <= R with NO boundary condition for transport (W.n ~ c_l R > 0: outflow). For the velocity, use the
          homogeneous extension rho(r,theta) = (r/R)^k rho(R,theta) for r > R. Its tail integrals in (V1) are analytic:
          int_R^inf s^{1-2n} f_n(s) ds = F_n R^{1-2n}/(2n - k - 1)   [v2: corrected from R^{2-2n}]
          with F_n the sin(2n theta) coefficient of k cos(theta) Theta_R - sin(theta) Theta_R', Theta_R(theta) = rho(R,theta).
          Equivalently, f_n(R+) R^{2-2n}/(2n-k-1), with f_n(R+) the mode at r = R of d_x of the homogeneous extension (the
          exterior derivative, R d_x rho_ext = k cos(theta) Theta_R - sin(theta) Theta_R'). [v4.4] It is NOT the mode of the interior
          d_x rho(R-): r rho_r(R-) differs from k rho(R) unless rho is exactly homogeneous of degree k at R (numerics lane 00:03Z,
          item 3; using the interior derivative shifted their c_l by about -6e-6 at R = 3000).
      (b) a global compactified radial coordinate with an explicit far-field factor, e.g. rho = x^2 y (1+r^2/L^2)^{(k-3)/2} b.
      Either way, report the effect of the closure (vary R or L, and compare the homogeneous extension with a two-term one).
 (N4) Residuals: R = W.grad rho - rho and E = -Laplace psi - d_x rho, absolute and normalized.
      - Normalize R by |rho| + |X.grad rho| + |U.grad rho| pointwise. State the convention used where this vanishes; on the axes,
        for example, use the sup over the region or the first nonvanishing transverse derivative.
      - Normalize E by |d_x rho|.
      Report on fixed interior regions (e.g. r <= 2, 2 <= r <= 10, a strip near each axis) and on the whole computational domain.
      [v4] Normalizations in use, all to be reported for a candidate (they differ by up to a factor 4 near P):
      - pointwise "N4": |R| / (|rho| + |X.grad rho| + |U.grad rho|);
      - pointwise "FD": |R| / (|W_1 rho_x| + |W_2 rho_y| + |rho|) (no cancellation inside X.grad rho);
      - regional ("relsup"): max_region |R| / max_region (|rho| + |X.grad rho| + |U.grad rho|), regions as above plus
        |X - P| < 1 and the bands theta < 0.05, theta > pi/2 - 0.05;
      - an exporter's own normalization (e.g. |rho| (1 + |3 + r H_r| + |U.grad rho / rho|)) may be quoted only next to one
        of the above.
 (N5) At least three resolutions and three domain sizes (R or L), with convergence tables on fixed interior regions.
 (N6) Solver: free choice. Options include dynamic rescaling rho_tau = rho - W.grad rho with c_l(tau) = (1+c(tau))/3, which
      preserves a(0)=1 exactly, and Newton/collocation on the stationary system. Report which was used. Reject rho -> 0,
      a(0) -> 0, and polynomial or gauge artifacts.

## 6. Diagnostics and identities every candidate must report

 D1 c_l, c = psi_xy(0) by (V1) and by int rho_1 r^{-2} dr; |3 c_l - c - 1|. Expected c = 3c_l - 1 > 2.
 D2 Parity errors, a(0), U(0), max |rho| on both axes.
 D3 Stagnation points of W: all of them, with type and eigenvalues. In particular report:
    - P = (x*,0), mu1 = d_x W_1(P), mu2 = d_y W_2(P);
    - |mu2 - 1| and |mu1 - (2c_l - 1)| (Lemma 3 says both vanish for an exact C^2 profile);
    - min_{y>0} W_2(0,y)/y.
 D4 Sign structure of rho in Q (is rho > 0 in Q?), and rho_y(x,0) on (0, x*].
 D5 Far field: rho(r,theta)/r^{1/c_l} versus theta at several r; Theta(theta).
 D6 Weighted identity. It is exact for class A and valid for k+2 < d < 5 with k = 1/c_l, using the uniform bound of Lemma 1.
      For phi = r^{-d} sin((2m+1) theta):  (1 + (2-d) c_l) int rho phi dX + int rho U.grad(phi) dX = 0.
      With d=3, m=1 this reads pi (1 - c_l) c + int rho U.grad(sin(3theta) r^{-3}) dX = 0.
 D7 Regularity at the center: estimate B_3 and report the apparent Holder regularity of a. Two ways to estimate B_3:
      - fit d_y^3 rho(x,0)/6 near x=0 by an even polynomial plus B_3 |x|^{p_3};
      - better, export the axis data listed in NOTES_FOR_TEAM, so the lead can evaluate B_3 by the ODE/finite-part formula of
        analysis.md 3.2.
 D8 Check div U = 0 and curl U = -d_x rho by a different differentiation method, and confirm U = o(r): report U/r^k.
    The available a priori bound is U = O(r^k log r).
 D9 [v3] Exact axis identities (w = W_1(x,0), h = d_y W_2(x,0), a2 = d_y^2 W_1(x,0)/2, b3 = d_y^3 W_2(x,0)/6, g = rho_y(x,0)):
    w' + h = 2c_l,  a2' + 3 b3 = 0,  h' - 2 a2 = -g',  w g' = (1 - h) g,
    |w(x)|/g(x) = A int_x^{x*} dt/g(t) on (0, x*],  and  int_0^{x*} (1/g(x) - 1/(g0 x^2)) dx = 1/(g0 x*).
 D10 [v3] Scale-invariant form of D6 (d = 3, m = 1): q := Q3/c^2 with Q3 = int rho U.grad(sin(3theta) r^{-3}) dX must equal
    (pi/3)(1 - 2/c); in the class 0 < q < pi/3. (q is invariant under rho -> mu rho(X/lambda); Q3 has no sign on positive
    densities, so this is a residual check, not a constraint that excludes anything by itself.)
 D11 [v3] Far-field closure near c_l = 1: the relative size of U against c_l X decays only like r^{k-1}, k = 1/c_l
    (r^{-0.06} at c_l = 1.06). Closures that treat the far field as dominated by c_l X are then inaccurate on any practical
    domain. A candidate with c_l < 1.2 must show its c_l is stable under a change of the closure and of R or L by a factor
    of at least 10.

 D12 [v4] Jet test on the x-axis (necessary, sees what the 2D residual barely sees). Write rho = y g + y^3 G3 + O(y^5),
    W_1 = w + y^2 a2 + ..., W_2 = y h + y^3 b3 + ... at (x, 0). The y^1 and y^3 coefficients of W.grad rho - rho are
    T1 = w g' + (h - 1) g and T3 = w G3' + (3h - 1) G3 + a2 g' + b3 g. Report T1 and T3 divided by the sum of the absolute
    values of their terms on (0, x*] and beyond, and the same at orders x^2, x^4 on the y-axis. Near the x-axis the
    normalized 2D residual is about y^2 T3 / g, so a jet error of a few percent shows only as a thin band.
    Interpretation identity (lead, elementary): with H the homogeneous solution (H'/H = (1 - 3h)/w, H ~ x^{p3} at 0) and
    D = T3 of a trial function, -F3/(wH) = -(G3/H)' + D/(wH) with F3 = -a2 g' - b3 g. Hence
      f.p. B_3 computed from (w, h, a2, b3, g)  =  B_3 of the trial's own G3  +  f.p. int_0^{x*} D/(wH) dx.
    Correction [v4.12] (analysis.md 15; external referee b3def1, CONFIRMED with conditions): the H above is the homogeneous
    solution H_h of the trial's own G3 equation (after integration it needs lim G3/H_h = 0 at x*, guaranteed by h(x*) > 1/3).
    R10's formula uses H = N g^(3+beta) |w|^(-beta) (beta = 2/A, A = 2 c_l - 1, N = A^beta for g ~ x^2), which equals H_h
    only when T1 = 0. With R10's H, and w' + h = 2 c_l, a2' + 3 b3 = 0 (exact for every trial, div U = 0), the defect is
    D = T3 - (3 + beta)(G3/g) T1, and R10's formula on the trial's axis data = B_own + f.p. int_0^{x*} D/(wH) dx, under
    g > 0 on (0, x*], g(x*) > 0 and even expansions of g/x^2 and |w|/x at 0 (the finite part at 0 is then the constant term
    of G3/H; the coefficients of x^(4 - p3), x^(6 - p3) in G3/H are c4 - u2 c2 and c6 - u2 c4 + (u2^2 - u4) c2, H = x^p3 (1 +
    u2 x^2 + u4 x^4 + ...)). H/H_h = exp((3 + beta) int_0^x T1/(g w) dt).
    The two B_3 measurements (axis finite part, and the coefficient of the trial's own |x|^{p3} y^3 content) agree only if
    the weighted defect is small; report both, in natural units B_3 / x*^{2-p3}. The finite part must be computed by a
    noise-robust method (least-squares fit of the even function Phi(u) = (1-u)^{beta-1} phi(x* u), not interpolation
    at Chebyshev nodes, which amplifies 1e-8 data noise by orders of magnitude).
    Sensitivity [v4.1, 2026-10-17T20:41Z] (analysis.md 3.5(c), scripts/b3_wonly_perturb.py): B_3 is a very sensitive functional of
    w (a2 and b3 contain w'' and w'''). On construct1 a relative change 1e-6 of w at scale l moves the w-only value by
    about 1e-3 (l = 4), 2e-2 (l = 1.5), 0.08 to 1.8 (l = 0.5) natural units. A B_3 value is meaningful only together with
    an accuracy estimate of w near the center (for example the change of w between resolutions), and the decisive test is
    agreement of two independent solvers. Report the w-only value with that change.
 D13 [v4] P-centred strain identity (external referee claim, lead numerical check only; verifier rederivation pending):
    with Z = X - P and the circular principal value about P,
      PV int rho |Z|^{-3} sin(3 arg Z) dX = pi (1 - c_l + g(P)/4),   g(P) = rho_y(x*, 0).
    Evaluate with a smooth partition of unity around P (a sharp cutoff on a polar grid gives 1e-2 errors).

 D14 [v4] Degree-5 Taylor relations at the center (lead, scripts/taylor5.py). With a = 1 + delta x^2 + gamma y^2 + O(r^4)
    and psi = c x y + alpha x y^3 + beta x^3 y + O(r^6) (alpha + beta = -1/3 by the Poisson equation), the x^4 y and
    x^2 y^3 coefficients of W.grad rho - rho are beta - 2 A delta and (4A + 2) gamma - 5 alpha; both vanish for a solution
    (alpha is global, so these do not determine delta, gamma alone). Report both, divided by the sizes of their terms.
    Near the center residual/rho = r^2 [((4A+2) gamma - 5 alpha) sin^2 theta + (beta - 2 A delta) cos^2 theta] + O(r^4).
    A trial with a basis length scale near the center (e.g. suppression of angular modes inside a radius) must show the
    residual is free of a bump at that scale; such a layer contaminates the axis jets and hence B_3 (D12).

## 7. Out-of-class regimes (not primary; for completeness)

 - Lemma 1 shows that class A forces c_l > 1. For 0 < c_l <= 1 a nonzero profile must violate (A3): along characteristics where
   it is nonzero it grows at least like r^{1/c_l} >= r.
 - [v2] Density growth alone does NOT force a linearly growing velocity. Two examples:
   - rho = y^q, c_l = 1/q, U = 0 (q odd) are exact solutions, violating (A2);
   - an outer sin(5 theta) mode feeds only the sin(4 theta) and sin(6 theta) modes of d_x rho.
   But for general data with growth >= r the n=1 tail integral need not converge, and growth does not fix lambda x y. A velocity
   law would then need an extra gauge rule (e.g. Hadamard finite part).
 - Physically this is infinite-time focusing (c_l < 1) or the borderline c_l = 1. Not a primary target.
 - Choosing the strain constant so that 3c_l - c = 1 holds is NOT an admissible gauge rule: it amounts to fitting c_l.
 - For 1/4 < c_l < 1/2 the origin is a source, not a saddle, so the smoothness structure is different. The same gauge problem applies.
 - c_l <= 0: no nonzero class-A profile (Lemma 1).
 - [v3] For 0 < c_l < 1 a self-similar state is not a blowup (formal, notes 10.4): alpha = 1/(c_l - 1) < 0, beta = alpha + 1 < 0,
   and the gradient of rho_phys on a fixed ball is O((T-t)^{-1-2 beta}) -> 0 when c_l > 1/3. States found near c_l = 0.63 are
   therefore irrelevant to singularity formation as well as out of class.

## 8. [v4] Endpoint standards (agreed with the verifier, VERIFY_REPORT Part 10 F5)
 YES (strong numerical evidence, never called a proof) requires, for one candidate:
  - whole-box residual (all r in [r0, R], all angles) by region and pointwise, normalizations of N4, near 1e-6, recomputed by
    the verifier's own code from the exported rho;
  - at least three resolutions (radial and angular) and three domains (R or L varied by a factor of at least 10; also vary
    the far-field closure), with c_l, x*, h(P) stable, B_3 with its spread; c_l = (1 + psi_xy(0))/3 checked independently;
  - D1 to D13 reported; B_3 with the --singular 0 control;
  - an explicit class statement matching the measured B_3: if B_3 != 0, the profile is not smooth and the YES is for an
    explicitly distinguished finite-regularity class, not for the stated problem (a smooth); this must be said in the
    deliverable. The class must be stated only as far as it is proved: Lemma 5 gives "B_3 != 0 implies rho not C^10
    (p_3 <= 7) or not C^11 (p_3 in (7,8))"; the 2D Holder class of such a profile is open (VERIFY_REPORT Part 4 S4.5
    withdrawn), so the deliverable states the finite-regularity class by its defining expansion
    (rho = x^2 y a with a = smooth + B_3 |x|^{p_3 - 2} y^2 (smooth) near 0) and not by a Holder exponent.
  - [v4.3, replaces the v4.2 proposal P_B; VERIFY_REPORT G20 (a), G23] the explicitly distinguished problem is P_2 (P_m of
    FINAL_REPORT section 1 with m = 2): the profile equation, parity, velocity law and growth class of the strong setting,
    with "a smooth near 0" replaced by "rho in C^(2,alpha)_loc(R^2) and rho = x^2 y a near 0 with a continuous, even/even,
    a(0) = 1". No regularity above C^(2,alpha) is claimed. The deliverable is then "YES, strong numerical evidence, for the
    explicitly distinguished problem P_2" (wording pending verifier confirmation), and its first lines say: (i) the strong
    setting (a smooth and even) is not answered; (ii) the computed branch has B_3 = (value, variant spread) natural units,
    nonzero, and since C^infinity implies B_3 = 0 (proved) this is numerical evidence that the branch is not C^infinity, not
    a NO theorem, other branches not excluded; (iii) the class is stated only as far as proved. The expansion
    a = a_0 + B_3 |x|^{p_3 - 2} y^2 a_1 + ... (the structure forced by the centre analysis) is a remark, not the class.
  - [v4.3, G20 (b), binding] independent check: the verifier's residual evaluator (own differentiation, own inverse) on the
    exported rho, by fixed region and pointwise including the bands next to P, both axes and 0, with far-field truncation
    and inverse errors quantified separately, three resolutions and three domains, normalized residual about 1e-6
    including next to P with systematic improvement; c_l: the identity by the verifier's psi_xy(0), stability within one
    construction and spread across constructions (a variant spread, not an error bound), and at least one determination
    not using the identity with its accuracy (h(P) = 1 at fixed rho; the numerics map Psi); the numerics-lane spread
    reported; the characteristic defect J reported and decreasing under refinement; the report says the candidate comes
    from one construction family, is checked by a separate evaluator, and that the independent solvers did not converge
    to it. A second converged solver is desirable, not required.
  - [v4.5, 2026-10-18T04:01Z; VERIFY_REPORT G37, G41 (d), G45 (e), G46] c_l determinacy. The residual pins c_l only weakly (a soft
    direction: fits 3e-5 apart are equally good on the lead bases; in the numerics discretisation, at its near-P level,
    fixed-c_l fits over 5.52 to 5.71 are equally good or better on its clustered 256 x 64 grid, and its discrete
    L2 minimizer moves by about 0.06 between grids, the zero of h(P) - 1 by about 0.1 [v4.6, G62, G65 (e)]). Every quoted c_l comes with (1) the reproducibility
    sentence (the spread of fits is not an error bar); (2) the result of a nonlinear fixed-c_l test at the residual level
    of the quoted basis (c_l held fixed at an offset of at least 2e-2, same basis and grid as the free fit), read by the
    rule fixed before the result (lead NOTES_FOR_TEAM 2026-10-18T04:00Z item 4), or the statement that uniqueness at
    that level is untested; (3) the numerics-discretisation statement above. If the fixed-c test does not exclude the
    offset, c_l is quoted as an interval containing the tested values, and "c_l stable" in the YES standard means stable
    as an interval, not as a digit string.
  - [v4.7, 2026-10-18T08:19Z; CONFIRMED with amendments A0 to A5 by VERIFY_REPORT G67 (09:05Z), amendments entered 2026-10-18T09:15Z]
    Candidate at a fixed c_l. If a fit with c_l held fixed reaches
    a lower whole-box maximum than the free L2 fit in N_f, and a whole-box maximum in N_v that is not higher, the YES candidate may be that fixed-c_l fit, provided: (1) the free fit
    is reported next to it with its numbers (L2 objective, maxima by region, c_l); (2) the quoted c_l interval contains both
    c_l values and every tested value at which a fit reaches the standard; (3) the resolution and domain studies of the YES
    standard are done at the candidate's c_l (the same fixed value on every basis and domain, to 1e-7); (4) the identity
    c_l = (1 + psi_xy(0))/3 is checked by the verifier on the candidate (for a fixed-c_l fit it is a test of the fit, since c_l
    is an input of the transport equation and psi_xy(0) is computed from rho); (5) the identity-free determination
    (h(P) = 1 at fixed rho) is reported with its accuracy, and the report says that the fixed value was chosen from the
    max-norm comparison of fits, not determined by the equation.
    Amendments (G67 (g)): A0 the free fit of the entry test is the free continuation with the same LSQR budget from the
    same start (c6f segment 2 at the fixed fit's iteration count), measured by the verifier at the G20 (b) configurations;
    otherwise the report says that the budgets differ. A1 "N_v not higher" means not higher by more than the spread over
    the verifier's configurations, for r <= 1000 and for the far field separately, and the characteristic defect J is not
    higher either. A2 the report lists every fixed c_l that was tried, with its maxima and objective, including undecided
    ones (the 244-function fit at 5.60). A3 the report says that h(P) = 1 holds at the fixed value on the candidate and at
    the free value on the free fit, so it does not determine c_l at the 1e-3 level. A4 the resolution study includes J at
    each basis; the domain study is read by the rule of NOTES_FOR_TEAM 2026-10-18T08:17Z item 4 (fit convention). A5
    quoted maxima exclude evaluation points inside the verifier's evaluator floor next to the y-axis, and every such
    exclusion is stated.
    [v4.7 extension, 2026-10-18T09:05Z; conditions E1 to E5 and the drift reading from G68 (d) entered 2026-10-18T09:30Z] Several fits (fixed-c_l fits, free continuations started from them, reweighted free
    fits): the candidate is the fit with the lowest whole-box N_f maximum among those whose N_v maxima and J are not higher
    than the equal-budget free fit's in the sense of A1; conditions (1) to (5) apply to it, with (3) at its c_l and, if its c_l came from the
    identity during the fit (free formulation), (5) says from which start value the fit began and how far c_l moved.
    Extension conditions (VERIFY_REPORT G68 (d), entered 2026-10-18T09:30Z): (E1) A0 to A5 apply; (E2) the chosen fit carries
    its own resolution rows and domain columns at its own c_l before it is the candidate; (E3) all maxima are compared at
    the same verifier configurations; (E4) the report states how many fits were compared, since the minimum over several
    fits is a selection; (E5) for a reweighted fit the table names the weighted objective and gives its L2 objective too.
    Drift reading for a free continuation of a fixed-c_l fit (drift = c_l at the end minus c_l at the start): |drift| < 1e-4
    means the free solver does not resolve a slope of the objective in c_l within its budget (not that there is none);
    drift >= +3e-4 is reported as a resolvable slope; for 1e-4 <= drift < 3e-4 or drift <= -1e-4 the drift is reported as
    measured, the reading is undecided, and the interval contains the start and end values.
  - [v4.8, 2026-10-18T17:43:51Z; records reading rules fixed in NOTES_FOR_TEAM before the results they decided, and checked by the verifier
    (G72 (a), G73 (g), (h2), G74, G76 (h) 1)] Equal-budget pair rule (12:02Z): of a fixed-c_l fit and its free continuation
    with the same start, grid and LSQR budget, the fixed-c_l fit is kept if its whole-box N_f is lower, its N_v is not higher
    beyond the spread over the verifier's configurations (r <= 1000 and r > 1000 separately) and its 857-label J is not
    higher; otherwise the free fit is kept. The far band is all r > 1000; the band 1000 <= r <= 1000 L is reported next to it
    and does not decide (14:04Z). Candidate (14:02Z): the pair winner with the lowest whole-box N_f, read on the
    configurations with 16875 or more radial points (G73 (h2)). A5 applies in the near field, not in the far field (G73 (g)).
    Domain columns (08:17Z item 4): each fit in its own convention (two-term closure at its inverse radius), agreeing with
    the formula-global fit on the same basis if the 2-10 and 10-100 N_f maxima are within a factor 1.5 and |h(P) - 1| < 1e-7;
    J reported; a domain column is a stability observation in a closed problem, not a truncation bound. Fit rows: the
    formula-global fits have rows r < 0.9 R_shape = 900 L and inverse domain r <= 1000 L; a domain fit with fit radius
    R_f has inverse radius R_f / 0.9. Rows made after the candidate was fixed (domain fits, budget continuations, rows to
    9000 L) are not candidates unless a new equal-budget pair is run.
  - [v4.9, 2026-10-18T21:46:58Z; records reading rules fixed in NOTES_FOR_TEAM before the results they decide; the verifier applied
    the first two (G85, G89, G90); the others are fixed before their results and are checked when those results are read]
    Angular row (15:14:26Z item 4): at the fixed c_l and equal budget, the row m <= 100, 150, 200 (and the m <= 250 refinement
    row) improves systematically if none of whole-box N_f, N_f within 0.5 of P, N_v for r <= 1000, N_v for r > 1000 and the
    857-label J increases from one row to the next by more than the spread over the verifier's configurations; each row's
    values are reported either way. The m <= 250 pair (fixed c_l and its free control) is a refinement row, not a candidate:
    if it is lower than the candidate, the report says so and the deliverable does not change. Domain columns (G85; NOTES
    20:28:25Z item 4): the factor 1.5 of the 08:17Z rule is read two-sided; a column below 1/1.5 at some configuration is
    reported with its ratio and side, not as agreeing. Budget row (NOTES 17:42:41Z (45), 21:10:51Z item 3): X3 continued at
    the fixed c_l on its own rows for the same further budget as the domain fits; read against X3 by ratios of whole-box N_f,
    N_f within 0.5 of P, N_v for r <= 1000, 857-label J, far N_v and h(P) - 1; the domain columns are read against it (near-P
    N_f and J ratios in [0.8, 1.25]: the column's near-P gain over X3 is that of the budget; otherwise the ratio is stated);
    for the far band 1000 L to 9000 L (formula continued, N >= 16875) a ratio to X3 above 0.8 on some configuration
    attributes the fall of the 9000 L row to its rows, a ratio at most 0.5 on every configuration means the fall is not
    attributable to the rows, and a ratio in between is stated without attribution; the same thresholds apply to C at the
    axis. Control with R_shape 1e4 L and rows below 900 L (18:04:24Z item 5): ratios in [0.8, 1.25] on both N >= 16875
    configurations read as "about X3", at most 0.5 on both as "falls"; C at the axis computed as for the 9000 L row. Free control of the 9000 L row (20:41:00Z): a data row (c_l drift, C at the axis, pair ratios), no decision.
    None of these rows is a candidate.
  - [v4.10, 2026-10-19T00:26:16Z; reading rules fixed in NOTES_FOR_TEAM before the results they decide; presentation item from VERIFY_REPORT G105]
    Fixed-c_l profile on 375 x m <= 150 (NOTES 2026-10-19T00:25:51Z, rows 37 to 40: c_l = 5.5763624 + d nominally; the transplants carry 5.5763624 + d + 0.18 d^2, and the report quotes the
    stored values (G112 (a): 5.5743631, 5.5783631, 5.6004662 at d = -2e-3, +2e-3, +2.4e-2; 5.5723653, 5.5683739 at -4e-3,
    -8e-3; v4.14: 5.5604082 at -1.6e-2, row 54, run only if L2(53) < L2(52), NOTES 2026-10-19T03:13:52Z, same rule, and the
    verifier states for 53 and 54 whether L2 and whole-box N_f are below the preceding row's; v4.15: 5.5524653 at -2.4e-2,
    row 55, run only if L2(54) < L2(53), NOTES 2026-10-19T03:46:06Z, same rule; the lower end is called bracketed at this
    budget only if L2 and whole-box N_f of the lowest row are above the next row's on both configurations), d = -2e-3, +2e-3, +3e-3,
    +2.4e-2, 21500 iterations from F0 + d t, against F2, the free fit with the same start lineage, basis, grid and budget): "not
    determined at this level" if the L2 objective and the whole-box N_f (A5, each verifier configuration) are within 30 percent
    of F2's and |h(P) - 1| <= 1e-6; "excluded at this level" if the fit has flattened (< 2 percent over its last 1000
    iterations) and its N_f maximum within 0.5 of P is at least 2 times F2's on each configuration; otherwise undecided. By
    v4.5 the quoted c_l interval contains every tested value that is not excluded. The 13.17 (c) Q rule (4.8 wording only)
    is read only where the references Q(244) = 1.97 (as written) and 1.36 (after the 1500 free iterations) agree: (P2) if
    Q(375) >= 2.96, (P1) if Q(375) <= 0.91, otherwise undecided. Refinement row with rows to 9000 L on m <= 250 (c6h9000, NOTES
    2026-10-19T00:16:58Z): interior against the m <= 250 row (at most 1.1 in A5 whole-box N_f and within 0.5 of P on both N >=
    16875 configurations: "the interior gain of the cap is kept"), far band against the equal-budget 9000 L budget row ([0.8,
    1.25]: "the cap does not move the far band"); otherwise ratios stated; reported only if audited before the final
    presentation pass. Not a candidate. Residual norms (G105; PROMPT section 4): the report gives absolute maxima of |R| by
    region with the scale max |rho| next to the normalized maxima, and the elliptic check as a quotient of suprema with that
    meaning stated.
  - [v4.16, 2026-10-19T03:55:00Z; reading rule fixed in NOTES_FOR_TEAM 2026-10-19T03:54:45Z before the results] Nested pair on 375 x m <= 200:
    rows 39 (5.6004662) and 53 (5.5683739) continued on m <= 200 as X2 was continued to X3 (fixed c_l, 20480 x 960, 20750
    iterations; steps 56 nst24g, 57 nsn8g), read against F3 on the verifier's configurations. 56: Q_200 = L2 / L2(F3);
    if 56 has flattened (< 2 percent over its last 1000 iterations): Q_200 >= 3.05 reads "favours an isolated profile at
    the attained level", Q_200 <= 1.36 reads "favours a family"; otherwise, or if 56 has not flattened, undecided (4.8 and
    the section 5 gap paragraph only). 57: ratios to F3 and X3 stated, no decision. The
    v4.10 rule against F3 applies to both for the interval (v4.5). Neither is a candidate.
  - [v4.18, 2026-10-19T06:18:36Z; reading rule fixed in NOTES_FOR_TEAM 2026-10-19T06:18:36Z before the results] Budget continuations of rows 54
    and 55 (steps 58 fxn16gb, 59 fxn24gb): each row continued for 21500 further iterations at its stored c_l from its end
    shape with the same settings (20480 x 720, inner 2500, check 250, damping 1e-8), 43000 iterations in all. Read on the
    verifier's configurations (N11250 q384, N16875 q512): the v4.15 bracket is "kept at twice the budget" if the L2
    objective of 59 and its whole-box N_f on both configurations are above 58's; "not kept at twice the budget" if the L2
    objective of 59 is below 58's; otherwise (L2 above, a whole-box N_f below) "the objective and the maxima disagree".
    The change of each over its last 1000 iterations is stated (2 percent test). The single-budget profile, its readings
    and the interval of (iv) are unchanged (they are at 21500 iterations against F2 at equal budget); the continuations
    enter (iv) and 4.3 only as the persistence test of the bracket, and only if audited before the presentation pass.
    Not candidates. No change of standard.
  - [v4.11, 2026-10-19T01:07:30Z; reading rule fixed in NOTES_FOR_TEAM 2026-10-19T01:07:09Z before the results] Lower-end rows of the
    fixed-c_l profile on 375 x m <= 150: 52 (d = -4e-3, c_l 5.5723653) and, only if its L2 objective ends below row 37's
    3.944751e-6, 53 (d = -8e-3, c_l 5.5683739); same start construction, grid and budget as rows 37 to 40, read by the same
    (a) / (b) / (c) against F2. (a) and (c) widen the quoted c_l interval to the row's c_l; (b) brackets the lower end.
    Not candidates. No change of standard.
  - [v4.19, 2026-10-19T11:36:03Z] Outcomes of the rules above (verifier readings; no change of rule or standard). v4.10 rule against
    F2: row 39 (5.6004662) "excluded at this level" (G114); row 55 (5.5524653) undecided by the letter, "not determined"
    with h(P) at 16875 or more radial points (G126); the tested values not excluded span [5.5524653, 5.5793640] (G126),
    and the v4.15 lower end is bracketed at this budget. v4.16 nested pair: 56 flattened, Q_200 = 1.680, "undecided"; 56
    "excluded at this level" by the interval rule on m <= 200; 57 ratios only (G135). v4.18: "kept at twice the budget"
    (G147). Endpoint (G120 standard): YES, strong numerical evidence for P_2, with C1 to C4 and C7 met, C6 met on the
    interim tree (final check pending), C5 (presentation pass) done 2026-10-19T11:34Z, C8 (the verifier's DONE
    audit) open. The strong setting P_inf is not answered.
 NO (rigorous) requires a complete proof audited by the verifier and the external referee with no surviving gap.

## Change log
 - v1 2026-10-17T17:54Z initial.
 - v2 2026-10-17T18:13Z after the external referee audit of v1:
   - amplitude scaling corrected;
   - tail formula in N3(a) corrected (R^{1-2n}; was R^{2-2n});
   - classes start at m=2, with Holder regularity;
   - c formula stated with its (A2) hypothesis and its general form;
   - Lemma 1 proof repaired, and the uniform bound |rho| <= C r^{1/c_l} added;
   - Lemma 2 finiteness hypothesis made explicit;
   - Lemma 3 strengthened (nondegeneracy is automatic);
   - Lemma 4 replaced by the fixed-W rigidity rho = C eta_P;
   - Lemma 5 regularity claims qualified: C^infinity => B_3 = 0 is proved, B_3 != 0 => not C^10/C^11 is proved, and the sharper
     claims need a saddle-passage argument;
   - section 7 growth-to-velocity claim corrected;
   - note on the global x^2 y factor added;
   - physical gauge justification marked conditional.
 - v3 2026-10-17T19:47Z: positivity repair (audit2) in Lemma 4; w-only B_3 formula, its conditions and the A = 2 case (audit3) in Lemma 5;
   Lemma 6 (c_l -> infinity degenerate; conditional sequence use); diagnostics D9 (axis identities), D10 (scale-invariant
   weighted identity), D11 (closure accuracy near c_l = 1); section 7 remark that c_l < 1 states are not blowups.
 - v4 2026-10-17T20:21Z: N4 normalizations listed (N4, FD, relsup); D12 (jet test T1, T3 and the interpretation identity relating the
   two B_3 measurements; noise-robust finite part); D13 (P-centred strain identity, referee claim, check pending);
   section 8 endpoint standards (verifier F5); D14 (degree-5 Taylor relations at the center).
 - v4.1 2026-10-17T20:41Z: D12 sensitivity of B_3 to w (no change to any criterion; a B_3 value must come with an accuracy
   estimate of w and is decisive only when two independent solvers agree).
 - v4.2 2026-10-17T21:23Z: section 8: B_3 reported with its spread instead of required stable; proposed rule for an unmeasured B_3
   (problem P_B, pending verifier agreement).
 - v4.3 2026-10-17T22:42Z: section 8: the distinguished problem is P_2 (P_m with m = 2), replacing the P_B proposal (VERIFY_REPORT G20 (a),
   G23); the independent-check standard of G20 (b) recorded.
 - v4.4 2026-10-18T00:35Z: N3(a) tail formula: the 'equivalent' form uses the exterior derivative of the homogeneous extension, not the
   interior d_x rho(R-) (correction reported by the numerics lane, 2026-10-18T00:03Z). No change to any criterion.
 - v4.5 2026-10-18T04:01Z: section 8 c_l determinacy item (G37, G41 (d), G45 (e), G46): quoted c_l needs a fixed-c_l test or the
   statement that uniqueness is untested at that level.
 - v4.6 2026-10-18T07:16Z: section 8 c_l determinacy item: the numerics-discretisation sentence takes the grid qualifier of VERIFY_REPORT G62 (wording only; no change of standard).
 - v4.7 2026-10-18T08:19Z (proposed): section 8 item 'Candidate at a fixed c_l' (fixc_c6f_m1.0e-03 reaches 6.8e-7 in the lead scans, 3.6x below the free fit in N_f; 12 percent below in N4); 2026-10-18T08:23Z: the normalizations named in the item.
 - v4.7 extension 2026-10-18T09:05Z (proposed): candidate choice among several fits (free continuation of the fixed-c_l fit, reweighted free fit); NOTES_FOR_TEAM 2026-10-18T09:05Z item 3.
 - v4.7 2026-10-18T09:15Z: CONFIRMED by G67 with amendments A0 to A5 (entered in section 8); the extension (09:05Z) uses the A1 reading.
 - v4.7 extension 2026-10-18T09:30Z: G68 (d) conditions E1 to E5 and the completed drift reading entered.
 - v4.8 2026-10-18T17:43:51Z: section 8 reading rules of 12:02Z, 14:02Z, 14:04Z and 08:17Z item 4 recorded as applied; fit-row extent stated; new: rows made after the candidate was fixed are not candidates without a new equal-budget pair (NOTES 17:42:41Z).
 - v4.9 2026-10-18T21:46:58Z: section 8 reading rules fixed later recorded (angular row 15:14:26Z item 4; two-sided A4, G85; budget row 17:42:41Z (45) and 21:10:51Z item 3; R_shape 1e4 control 18:04:24Z; free 9000 L control 20:41:00Z). No change of standard.
 - v4.10 2026-10-19T00:26:16Z: section 8 reading rules for the fixed-c_l profile rows 37 to 40 (with the Q(244) settlement) and for c6h9000 recorded before their results; G105 absolute-norm presentation item. No change of standard.
 - v4.11 2026-10-19T01:07:30Z: section 8 reading rule for the lower-end fixed-c_l rows 52 and 53 (NOTES 01:07:09Z) recorded before their results. No change of standard.
 - v4.12 2026-10-19T01:26:50Z: D12 interpretation identity corrected for R10's H (defect T3 - (3 + beta)(G3/g) T1; analysis.md 15; external referee b3def1). No change of standard or criterion.
 - v4.13 2026-10-19T01:47:15Z: section 8 v4.10 item: the row exponents are quoted as stored (G112 (a)). No change of standard.
 - v4.14 2026-10-19T03:14:02Z: section 8 v4.10 item: conditional row 54 (d = -1.6e-2) with the same reading rule, fixed before its run. No change of standard.
 - v4.15 2026-10-19T03:46:06Z: section 8 v4.10 item: conditional row 55 (d = -2.4e-2) and the bracket rule for the lower end, fixed before the runs. No change of standard.
 - v4.16 2026-10-19T03:55:00Z: section 8: the nested pair 56 / 57 on m <= 200 and its reading rule, fixed before the runs. No change of standard.
 - v4.17 2026-10-19T04:11:33Z: section 8 v4.16 item: NOTES time 03:54:45Z cited; the flattening clause applies to both readings of 56 (G122 points (1), (2); the verifier read 56 by the NOTES text, which this matches). No change of standard.
 - v4.18 2026-10-19T06:18:36Z: section 8: budget continuations 58 / 59 of rows 54 / 55 and the persistence reading of the v4.15 bracket, fixed before the runs. No change of standard.
 - v4.19 2026-10-19T11:36:03Z: status lines brought up to date (positivity repair, D9, Lemma 6 = R11); section 8: the outcomes of the v4.10 to v4.18 rules and the endpoint state recorded. No change of rule or standard.
