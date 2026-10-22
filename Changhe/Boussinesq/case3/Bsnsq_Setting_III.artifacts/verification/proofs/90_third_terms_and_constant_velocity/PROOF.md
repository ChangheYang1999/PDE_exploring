# Third scalar tails and the determined constant velocity for 2 < beta < 3

Written: 2026-10-20T23:45:37Z. Status: CONFIRMED by the independent verifier as a necessary finite-order theorem. Lead audit pending; actual Opus availability is recorded below.
This is a necessary asymptotic theorem for hypothetical exact profiles. It is not a solution or an exclusion of the open class.

## 1. Exact statement, hypotheses, and dependencies

Let beta > 2 and let (Theta, Omega, V) be a smooth exact Setting B2 profile in the power-decaying class A of the team specification. Thus, on the entire plane,

    (beta X + V).grad Theta = (beta - 2) Theta,
    (beta X + V).grad Omega + Omega = partial_x Theta,
    div V = 0, partial_y V_1 - partial_x V_2 = Omega,
    V(X) = integral [K(X-Y) - K(-Y)] Omega(Y) dY,
    K(Z) = (Z_2, -Z_1)/(2 pi |Z|^2).

The integral is the absolutely convergent relative inverse, so V(0) = 0. No harmonic strain or freely adjustable constant is allowed. Omega is odd and Theta is even in x, Theta vanishes on the vertical axis, and the nontrivial center normalization is Theta_xx(0) = 2 a0 with a0 != 0. Class A includes a positive power of decay for Omega and DV, sublinear growth for V, and polynomial growth for Theta and its first derivative. These assumptions have the stronger consequences listed next; they, rather than any assumed asymptotic series, are the input to this proof.

The dependencies are the proved leading-tail and nonvanishing results of packets 14 and 33, spatial regularity and the first scalar correction of packet 36, and the second velocity term for beta > 2 in packet 38. Explicitly, write s = 1/beta, m = 1 - 2s, X = r e(theta), e = (cos theta, sin theta), e_perp = (-sin theta, cos theta). They give homogeneous smooth functions off zero

    omega_0 = r^(-s) A_0(theta), theta_0 = r^m H_0(theta),
    u_0 = K_rel omega_0,
    omega_1 = u_0.grad omega_0 - partial_x theta_0,
    theta_1 = u_0.grad theta_0, u_1 = K_rel omega_1.

A_0 and H_0 are not identically zero. Here omega_1 has degree -2s and theta_1 has degree m-s. Define physical fields for tau > 0 by

    u_tau(z) = tau^(beta-1) V(tau^(-beta) z),
    omega_tau(z) = tau^(-1) Omega(tau^(-beta) z),
    theta_tau(z) = tau^(beta-2) Theta(tau^(-beta) z).

For each compact subset of the punctured plane and each finite spatial derivative order j, these dependencies prove

    u_tau = u_0 + tau u_1 + o_Cj(tau),
    omega_tau = omega_0 + tau omega_1 + o_Cj(tau),
    theta_tau = theta_0 + tau theta_1 + o_Cj(tau).           (1)

All subsequent little-o statements have this same local meaning after rescaling, equivalently uniform bounds on fixed-ratio large annuli with one factor r^(-1) for each Cartesian derivative.

For every beta > 2 there are third scalar coefficients

    omega_2 = (u_0.grad omega_1 + u_1.grad omega_0
                                      - partial_x theta_1)/2,
    theta_2 = (u_0.grad theta_1 + u_1.grad theta_0)/2        (2)

such that

    Omega = omega_0 + omega_1 + omega_2 + o_Cj(r^(-3s)),
    Theta = theta_0 + theta_1 + theta_2 + o_Cj(r^(m-2s)).  (3)

Here omega_2 has degree -3s and theta_2 has degree m-2s.

If additionally 2 < beta < 3, there is a uniquely determined vertical constant C and a homogeneous velocity u_2 of degree 1-3s such that

    V = u_0 + u_1 + C + u_2 + o_Cj(r^(1-3s)),             (4)
    Omega = omega_0 + omega_1 + omega_2
               + (C.grad omega_0)/beta + o_Cj(r^(-s-1)),
    Theta = theta_0 + theta_1 + theta_2
               + (C.grad theta_0)/beta + o_Cj(r^(m-1)).   (5)

The precise definitions are

    eta = Omega - omega_0 - omega_1,
    U_eta(X) = integral K(X-Y) eta(Y) dY,
    C = -U_eta(0), u_2(X) = integral K(X-Y) omega_2(Y) dY, X != 0. (6)

The first ordinary integral converges absolutely for all X, including X = 0. The second converges absolutely for X != 0; it need not be defined at X = 0. In particular,

    C_1 = 0,
    C_2 = -(1/(2 pi)) integral [Y_1/|Y|^2]
                              [Omega(Y)-omega_0(Y)-omega_1(Y)] dY. (7)

No assertion that C is nonzero for every exact profile is made. If C is nonzero, both displayed C-transport coefficients in (5) are nonzero functions. The interval 2 < beta < 3 is strict; this proof does not dispose of the resonance at beta = 3 or establish an all-orders series.

## 2. Third scalar coefficients require no time derivative of velocity

The exact physical equations, with t = -tau, are

    partial_tau omega_tau = u_tau.grad omega_tau - partial_x theta_tau,
    partial_tau theta_tau = u_tau.grad theta_tau.          (8)

Insert (1), using spatial convergence one derivative higher whenever needed. Products of bounded C^(j+1) fields and o_C^(j+1)(tau) remainders are o_Cj(tau). The resulting right sides are

    omega_1 + tau (u_0.grad omega_1 + u_1.grad omega_0
                                      - partial_x theta_1) + o_Cj(tau),
    theta_1 + tau (u_0.grad theta_1 + u_1.grad theta_0) + o_Cj(tau).

Integrate from epsilon to tau and then let epsilon decrease to zero. The endpoint limits and locally uniform remainders in (1) justify the limit. The integral of o_Cj(tau) is o_Cj(tau^2). Consequently

    omega_tau = omega_0 + tau omega_1 + tau^2 omega_2 + o_Cj(tau^2),
    theta_tau = theta_0 + tau theta_1 + tau^2 theta_2 + o_Cj(tau^2). (9)

Each term in (2) has the stated degree by homogeneity. Taking tau = r^(-s) on the unit circle, or rescaling any fixed compact annulus, proves (3). This argument neither differentiates u_tau in time nor assumes its second time derivative exists.

For explicit angular formulas put k_i = 2-(i+1)s, omega_i = r^(-(i+1)s) A_i and theta_i = r^(m-is) H_i, for i = 0,1,2. For i = 0,1 let F_i be the unique smooth periodic solution of

    -(F_i'' + k_i^2 F_i) = A_i,
    u_i = r^(1-(i+1)s) [-F_i' e + k_i F_i e_perp].

Both k_0 and k_1 lie strictly between 1 and 2, so no periodic resonance occurs. Formula (2) reads

    2 A_2 = k_0 F_0 A_1' + 2s F_0' A_1
          + k_1 F_1 A_0' + s F_1' A_0
          - (m-s) cos(theta) H_1 + sin(theta) H_1',
    2 H_2 = k_0 F_0 H_1' - (m-s) F_0' H_1
          + k_1 F_1 H_0' - m F_1' H_0.                  (10)

Primes are angular derivatives. These are exact finite-order consequences, not equations for independently selectable third tails.

## 3. The integrable remainder when 2 < beta < 3

Now 1/3 < s < 1/2, so 2s < 1 < 3s < 3/2. Smoothness of Omega at zero and (3) at infinity give

    |eta(Y)| <= C_0 |Y|^(-2s),       0 < |Y| <= 1,
    |eta(Y)| <= C_0 |Y|^(-3s),       |Y| >= 1.            (11)

The same large-radius bounds hold with the appropriate additional powers for derivatives. For U_eta(0), the local radial integral is bounded by integral_0^1 rho^(-2s) d rho, and the exterior one by integral_1^infinity rho^(-3s) d rho. Both converge. For a fixed X != 0, the source singularity at Y = 0 is locally integrable because 2s < 2, the kernel singularity at Y = X is locally integrable against a smooth bounded source, and the exterior estimate is unchanged. Thus U_eta exists absolutely everywhere. Oddness in the first coordinate makes its first component at zero vanish and gives (7) with the displayed sign of K(-Y).

All three relative inverse integrals for Omega, omega_0 and omega_1 converge absolutely. Linearity and the absolute convergence of both terms of K_rel eta now give the exact identity

    V = u_0 + u_1 + U_eta - U_eta(0).                    (12)

This identity fixes C without a cutoff or a gauge choice. In particular, the constant cannot be changed by changing an absolute observer velocity, since V is unchanged by that operation.

A split into |Y| < r/2, r/2 < |Y| < 2r, and |Y| > 2r shows U_eta(re) = O(r^(1-3s)) uniformly in e. The first bound is r^(-1) integral_0^(r/2) rho |eta| d rho = O(r^(1-3s)), with the fixed core contributing O(r^(-1)); the middle bound uses |eta| <= C r^(-3s) and integral_{|Z|<3r} |K(Z)| dZ = O(r); the last uses integral_(2r)^infinity rho^(-3s) d rho. In particular U_eta tends to zero, so C is also the unique limit of V-u_0-u_1 at infinity.

## 4. The decaying third velocity and derivative control

The homogeneous source omega_2 = r^(-3s) A_2 has locally integrable singularity at zero because 3s < 2. For evaluation at X != 0 the ordinary inverse in (6) converges at infinity because 3s > 1 and at Y = X because its source is smooth there. Scaling its absolutely convergent integral makes u_2 homogeneous of degree 1-3s.

For R tending to infinity define eta_R(Y) = R^(3s) eta(RY). Bound (11) implies the global estimate |eta_R(Y)| <= C_0 |Y|^(-3s) for R >= 1: in R|Y| <= 1, the sharper factor (R|Y|)^s is at most one. By (3), eta_R converges to omega_2 locally smoothly off zero. The product |K(X-Y)| |Y|^(-3s) is integrable at zero and infinity for any fixed X != 0. Thus

    R^(3s-1) U_eta(RX) = integral K(X-Y) eta_R(Y) dY -> u_2(X). (13)

The convergence is uniform on compact annuli. To see this, remove uniformly small neighborhoods of Y = 0 and Y = X and a uniformly small exterior, then use uniform convergence on the remaining compact region. Near evaluation points the sources are uniformly bounded; near zero and infinity the displayed dominating power has uniformly small integrals. This also covers a general compact set away from zero.

Derivatives follow from local interior elliptic estimates rather than formal differentiation of the singular kernel. The velocity difference in (13) has divergence zero and negative curl eta_R-omega_2. On nested balls away from zero its Laplacian is (partial_y(eta_R-omega_2), -partial_x(eta_R-omega_2)), which converges locally in every C^j norm. Its velocity tends uniformly to zero by (13). Interior W^(j+2,p) estimates and Sobolev embedding therefore give convergence in every fixed spatial C^j norm on smaller balls. A finite covering handles each compact annulus. Combining with (12) proves (4) with its derivative interpretation.

For an angular description, k_2 = 2-3s lies strictly between 1/2 and 1. There is no periodic resonance. The unique periodic solution -(F_2''+k_2^2 F_2)=A_2 gives u_2 = r^(1-3s)[-F_2' e+k_2 F_2 e_perp]. To identify it with the ordinary inverse, both satisfy div-curl off zero and distributionally on the whole plane: their velocities are locally integrable, and boundary terms from a circle of radius epsilon are O(epsilon^(2-3s)), which tend to zero. Their difference is an entire harmonic vector field, decays at infinity, and hence vanishes. No point vortex, harmonic strain, or constant is left unspecified.

## 5. Integration of the fractional velocity term

In physical variables (4) becomes

    u_tau = u_0 + tau u_1 + tau^(beta-1) C
                                + tau^2 u_2 + o_Cj(tau^2). (14)

Since 1 < beta-1 < 2, the C term lies strictly between the first and second integer corrections to velocity. Equations (9) and (14), substituted into (8), imply

    partial_tau omega_tau = omega_1 + 2 tau omega_2
                      + tau^(beta-1) C.grad omega_0 + o_Cj(tau^(beta-1)),
    partial_tau theta_tau = theta_1 + 2 tau theta_2
                      + tau^(beta-1) C.grad theta_0 + o_Cj(tau^(beta-1)). (15)

Indeed every remaining product from the first two integer scalar terms and (14) is O_Cj(tau^2), which is o_Cj(tau^(beta-1)); the scalar remainders in (9) are o_Cj(tau^2) after using one more spatial derivative. Products involving C and higher scalar terms are O(tau^beta), smaller still. Integrating (15) from zero to tau gives

    omega_tau = omega_0 + tau omega_1 + tau^2 omega_2
                  + tau^beta (C.grad omega_0)/beta + o_Cj(tau^beta),
    theta_tau = theta_0 + tau theta_1 + tau^2 theta_2
                  + tau^beta (C.grad theta_0)/beta + o_Cj(tau^beta). (16)

Scaling back gives (5). The coefficients agree with the first translation correction to a homogeneous field evaluated at X+C/beta; that observation is an algebraic interpretation, not permission to move the prescribed material center.

## 6. Nonvanishing and the endpoint representation

Suppose C != 0. Since C is vertical, C.grad theta_0 could vanish identically only if partial_y theta_0 = 0. Then on either open half-plane theta_0 depends only on x, and homogeneity makes it c_+ x^m on x > 0 or c_- |x|^m on x < 0. Here 0 < m < 1/3. Smoothness across x = 0 at each nonzero y, together with theta_0(0,y) = 0, forces c_+ = c_- = 0: a nonzero such power has an unbounded first x derivative. This contradicts H_0 not identically zero. Likewise, partial_y omega_0 = 0 would give c_+ x^(-s) or c_- |x|^(-s), which cannot extend continuously across that axis unless both constants vanish. This contradicts A_0 not identically zero. Thus both translation coefficients in (5) are nonzero whenever C is.

For the finite last-knot-interval r2 spline representation with basis exponent beta, the relative radial exponents generated by a polynomial in z = (L^2/(r^2+L^2))^(1/(2 beta)), its specified exterior envelopes x^2 z^(beta+2) for Theta and x z^(beta+1) for Omega, and the factors sqrt(1-z^(2 beta)) are j/beta+2n with nonnegative integers j,n after extracting the actual leading powers r^m and r^-s, respectively. More generally the same conclusion applies whenever this exponent support is explicitly assumed through relative order one; arbitrary unspecified exterior envelopes are not included. In the strict interval 2 < beta < 3, the order 1 is absent: j/beta+2n = 1 would require n = 0 and j = beta, impossible for integer j. Therefore any exact nontrivial class A profile in such a finite endpoint family would have to satisfy C = 0. This conclusion uses (5), not an assumed infinite series. It concerns the finite radial endpoint family even if its angular coefficient functions are allowed to be smooth rather than finitely supported. A finite angular family is already excluded by the separate theorem of packets 83 and 84.

Neither C = 0 nor a vanishing A_2 is ruled out here. The statement supplies a necessary additional tail condition; it does not give a residual lower bound for a refining sequence or an existence/nonexistence endpoint. Packet 25 supplied only conditional constant-tail algebra and a manufactured inverse. The new point is that (3)-(7) and the fractional correction are proved for every exact class A profile with 2 < beta < 3, conditional only on the already proved finite-order dependencies (1).

## 7. Verification record

The informal proof was written before any new symbolic or numerical check. Verification artifacts and actual-model audit records are stored in verification/. No Lean or Lake execution is authorized or used. No formalization is claimed.

## 8. Independent inverse manufacture for checking (6) and (7)

This paragraph supplies smooth inverse test fields only, not solutions of the coupled equations. Fix 2 < beta < 3, sigma_j = j/beta for j = 1,2,3, a_j = (1-sigma_j)/2 and weights w_1 = 1, w_2 = 2/7, w_3 = -3/11. Set

    Psi = x sum_(j=1)^3 w_j [(1+r^2)^(a_j)-1],
    V = (-Psi_y, Psi_x), Omega = -Delta Psi.

V is smooth, sublinear, zero at the center, and has the required x parity. The relative inverse is exactly V by entire harmonic uniqueness. Its first three homogeneous streams are sum w_j r^(2-sigma_j) cos(theta); its constant velocity is therefore C = (0,-sum w_j) = (0,-78/77). The next smoothing correction decays as r^(-1-sigma_1), strictly faster than r^(1-sigma_3). For any prescribed a0, the selected velocity and vorticity center identities c=1+beta/2 and Omega_x(0)=4a0/beta can be imposed by adding (cxy+d0 x^3) exp(-r^2), with c = 1+beta/2 and d0 = [-4a0/beta-8 sum w_j a_j]/6. The previous formula was the a0=1 specialization, now explicit. This adds no far-field constant and has zero relative velocity at zero. Temperature is not specified.

For a single stream x(1+r^2)^a, its vorticity is cos(theta) q_sigma(r), where

    q_sigma(r) = -r[8a(1+r^2)^(a-1)+4r^2 a(a-1)(1+r^2)^(a-2)],
    q_sigma,tail(r) = -(1-sigma)(3-sigma) r^(-sigma).

For sigma < 1 subtract the homogeneous tail. The integral of the difference over r in (0,infinity) is exactly 2. To prove this, put P=r(1+r^2)^a-r^(2-sigma). Then q_sigma-q_sigma,tail = -(P''+P'/r-P/r^2), whose integral is -[P'+P/r]_0^infinity. The endpoint at zero is 2 since 1-sigma>0, and the endpoint at infinity is zero since P=O(r^(-sigma)). For sigma > 1 use P=r(1+r^2)^a without subtraction; the same endpoints are 2 and zero. These integrals converge absolutely in the ranges used here. Angular integration of K_2(-Y) cos(theta) contributes a factor 1/2, so (7) yields C_2=-sum w_j exactly. A Gaussian center correction contributes zero to this moment, since its stream and velocity decay and its velocity at zero is zero. Numerical integration of these three ordinary radial integrals checks the origin and infinity thresholds independently of the scalar PDE algebra.

Audit update 2026-10-20T23:51:41.051995+00:00: the independent Cartesian checker passed 40 exact algebraic identities over beta = 7/3, 5/2, 8/3, 4 in 12.138813 seconds. The ordinary moment manufacture ran in .002965 seconds; its maximum numerical error against the exact integral 2 was 2.30e-13 and the largest error in C_2 was 3.25e-14. These checks support the formulas; the theorem rests on the complete argument above. Actual Opus requests 98 and 99 returned model claude-opus-5-5 with stop_reason=refusal and no written audit, after 97.718959 and 7.420591 seconds. No endorsement or substituted model is claimed. The full argument has been exposed to the lead for independent review.

Audit update 2026-10-21T00:12:11.314658+00:00: read the full independent lead referee90 audit. Its finite-order theorem check is sound; adopted explicit leading-envelope support and general-a0 center-jet clarifications. The referee reported failed credential retrieval for its own Opus request, so no additional Opus endorsement is claimed.
