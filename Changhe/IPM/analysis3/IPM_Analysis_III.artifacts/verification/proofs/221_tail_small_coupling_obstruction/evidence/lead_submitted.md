# A far-field obstruction to a bounded inverse on the common Hoelder target

Status: DERIVED by the theory author, 2026-10-28 (a session); submitted for verification. Not yet confirmed.

## Setting

Fix 0 < alpha < 1 and gamma > 4k. Let Y = E_2 intersected with L^2(w_gamma) be the common target of V222 (proof 213):
bounded continuous functions, even in x, odd in y, with h(0, y) = 0, and

    ||h||_Y = ||h||_inf + [h]_x + [h]_(y,2) + ||h||_{L^2(w_gamma)},
    [h]_x = sup |h(x, y) - h(x', y)| / |x - x'|^alpha,
    [h]_(y,2) = sup |h(x, y) - h(x, y')| / (x^2 |y - y'|^alpha),   w_gamma = (1 + |X|^2)^(-gamma/2).

The weight x^2 of the vertical seminorm is global; at large |x| it is a weak requirement. Let V = ell0 X + U[rho0],
T = V.grad - 1, D_Y = {h in Y : V.grad h in Y distributionally}, and let beta_R = 1 - chi(X/R), with chi smooth,
radial, equal to 1 on B_1 and 0 outside B_2.

## Statement

Proposition (far obstruction). Let B : Y -> Y be bounded with eps(R) := ||beta_R B||_{Y -> Y} -> 0 as R -> infinity.
Then A = T + B, defined on D_Y, is not a bijection from D_Y onto Y. Equivalently (when A is closed on D_Y), there is
no constant K with ||u||_Y <= K ||A u||_Y for every u in D_Y together with surjectivity; A has no bounded inverse
Y -> D_Y.

In particular this applies to B = C_ren (V224: bounded on Y, eps(R) <= C R^(k-1)(1 + log R), 4k < gamma < 2) and to
the full chart linearization B = C_ren + c[.] m_0 (V228: eps(R) <= C R^(2k - gamma/2)(1 + log R)). So the closed
realizations L_ren and A_0 on D_Y have no bounded inverse on Y, for every 0 < alpha < 1 and 4k < gamma < 2.

Mechanism. The far flow is the dilation X -> e^(ell0 tau) X up to lower order. The transport inverse
u(X) = -int_0^inf e^(-tau) g(Phi_tau X) d tau samples g along forward orbits, on which x^2 |Delta y|^alpha grows like
e^((2 + alpha) ell0 tau). Since (2 + alpha) ell0 > 1, vertical oscillations of g that Y permits at radius X0 are
transported back to a fixed radius with an amplification X0^(2 + alpha - k). A seminorm with growth weight
|X|^(beta - alpha) at infinity in place of x^2 is compatible with the far transport only if beta < k; this is the far
window 2k - 1 <= beta < k of the scaled classes (DERIVED, 3.2 of the report).

## Proof

Step 1 (far orbits). From the exact far expansion (proof 117; also used in V228), |U[rho0]| <= C r^k and
|D U[rho0]| <= C r^(k-1) for r >= 1. On the sector S = {x >= R_1, 0 < y <= x} write
dx/dtau = x (ell0 + a), dy/dtau = y (ell0 + b). Here |a| <= |U_1|/x <= C x^(k-1), and, since U_2 is odd in y,
b = int_0^1 d_y U_2(x, t y) dt with every point of the segment at radius >= x, so |b| <= C x^(k-1). Choose R_1 so
large that C R_1^(k-1) <= ell0/2 and delta_1 := 4 C R_1^(k-1)/ell0 <= log(3/2)/8. For a starting point
X* = (R_1, y*) with 0 < y* <= R_1/4, the ratio y/x changes by at most the factor e^(2 delta_1) <= 2, so the orbit stays
in S, x_tau >= R_1 e^(ell0 tau/2), and int_0^inf (|a| + |b|) d tau <= delta_1. Hence for all tau >= 0

    x_tau = R_1 e^(ell0 tau + a~(tau)),  y_tau = y* e^(ell0 tau + b~(tau)),  |a~|, |b~| <= delta_1.          (1)

Step 2 (the forcing). Let phi be smooth on [0, infinity), supported in [1, 4], equal to 1 on [2, 3], 0 <= phi <= 1;
theta smooth, even, equal to 1 on [-1, 1], supported in [-2, 2], 0 <= theta <= 1; sigma smooth, odd, nondecreasing,
equal to 1 on [1, infinity). For X0 >= R_1 put

    f(x, y) = phi(|x|/X0) theta(X0 y) sigma(|x|^(2/alpha) y).

Then f is smooth, even in x, odd in y, zero near x = 0, and f >= 0 for y >= 0. Its Y norm is bounded uniformly in X0:
||f||_inf <= 1. On the support |x| is comparable to X0 and |d_x f| <= C/X0 (the sigma factor contributes
sigma'(.) (2/alpha) |x|^(2/alpha - 1) y, and sigma' is supported where |x|^(2/alpha) |y| <= 1), so
[f]_x <= C. In y, the sigma factor is Lipschitz with constant C |x|^(2/alpha), so its differences are at most
min(2, C |x|^(2/alpha) |Delta y|) <= C x^2 |Delta y|^alpha; the theta factor has differences at most
min(2, C X0 |Delta y|) <= C X0^alpha |Delta y|^alpha <= C x^2 |Delta y|^alpha; hence [f]_(y,2) <= C. Finally
||f||^2_{L^2(w_gamma)} <= C X0 X0^(-1) X0^(-gamma) <= C. So ||f||_Y <= C_0 with C_0 independent of X0.

Step 3 (the orbit sees the forcing). Choose y* = e^(2 delta_1) R_1 (2 X0)^(-1 - 2/alpha). By (1), x_tau runs
through [2 X0, 3 X0] during a time interval I of length at least (log(3/2) - 2 delta_1)/ell0 >= log(3/2)/(2 ell0),
entered at a time tau_0 with e^(-tau_0) >= c (R_1/X0)^k. On I, x_tau^(2/alpha) y_tau >= (2 X0)^(2/alpha) y*
(2 X0/R_1) e^(-2 delta_1) = 1 and y_tau <= C X0^(-2/alpha) <= 1/X0 for X0 large, so f(Phi_tau X*) = 1. Since
y_tau > 0 for all tau, f(Phi_tau X*) >= 0 throughout. Therefore

    int_0^inf e^(-tau) f(Phi_tau X*) d tau >= c_1 (R_1/X0)^k.                                                   (2)

Step 4 (representation). Suppose A is a bijection D_Y -> Y. Being closed (V224, V228, or by assumption), it has a
bounded inverse, ||u||_Y <= K ||A u||_Y. Let u in D_Y solve A u = f, so ||u||_Y <= K C_0, and put
g = T u = f - B u in Y. Along each orbit d/dtau u(Phi_tau X) = (V.grad u)(Phi_tau X) = u(Phi_tau X) + g(Phi_tau X)
(u and V.grad u are continuous and V is C^1, so a flow box makes this classical), and u is bounded, so

    u(X) = -int_0^inf e^(-tau) g(Phi_tau X) d tau.                                                              (3)

Step 5 (the coupling contribution is small). For every h in Y and every Z = (z_1, z_2), oddness in y gives
|h(Z)| <= [h]_(y,2) z_1^2 |z_2|^alpha, and |h(Z)| <= ||h||_inf. Let R = X0^(1/2) and let tau_2R be the time at
which |Phi_tau X*| = 2R. Before tau_2R use |B u(Z)| <= ||B|| ||u||_Y z_1^2 |z_2|^alpha; afterwards
B u(Z) = (beta_R B u)(Z), so |B u(Z)| <= eps(R) ||u||_Y min(1, z_1^2 |z_2|^alpha). With (1),
x_tau^2 y_tau^alpha <= e^(3 delta_1) R_1^2 y*^alpha e^((2 + alpha) ell0 tau) and (2 + alpha) ell0 > 1, so

    int_0^tau_2R e^(-tau) x_tau^2 y_tau^alpha d tau <= C (R_1/X0)^k (R/X0)^(2 + alpha - k),
    int_tau_2R^inf e^(-tau) min(1, x_tau^2 y_tau^alpha) d tau <= C (R_1/X0)^k,

the second because x_tau^2 y_tau^alpha reaches 1 only at a time tau_1 with e^(-tau_1) <= C (R_1/X0)^k, after which
the integrand is at most e^(-tau). Hence

    |int_0^inf e^(-tau) (B u)(Phi_tau X*) d tau| <= C K C_0 (R_1/X0)^k [ ||B|| X0^(-(2 + alpha - k)/2) + eps(X0^(1/2)) ].

The bracket tends to 0 as X0 -> infinity.

Step 6 (contradiction). By (2), (3) and Step 5, |u(X*)| >= (c_1/2)(R_1/X0)^k for X0 large. Since u is odd in y,
u(R_1, -y*) = -u(X*), and

    [u]_(y,2) >= 2 |u(X*)| / (R_1^2 (2 y*)^alpha) >= c (X0/R_1)^(2 + alpha - k) -> infinity,

whereas ||u||_Y <= K C_0. This contradiction proves the proposition.

## Remarks

1. The same construction with x-oscillations shows that the unweighted horizontal seminorm [h]_x is also
   incompatible with the far transport when alpha > k. The vertical seminorm fails for every alpha.
2. The obstruction is at infinity and is unrelated to the local cutoff noncompactness of V227; both are properties
   of the target Y, not of the operator. The realization theorems V222, V224 and V228 are unaffected.
3. Consequence for Avenue II. A global Hoelder inverse needs a target whose seminorms at infinity are scaled, with
   growth weight |X|^(beta - alpha) and beta < k (the far window), while keeping the E_2 structure near the origin
   and C^alpha near the sources. Whether the coupling is bounded on such a space, and whether the residual lies in
   it (it needs beta >= 2k - 1), is not decided here.
