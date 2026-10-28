Lemma H-spec (spectral-parameter continuation; DERIVED, submitted for verification; revised at 07:01Z: stated for the
remainder block, with the jet row split off by the triangular form of Theorem C', because the inclusion X_H in Y_H
fails on the jet coordinate; see the paragraph after the corollary). It replaces the regularization step of (e) and
the surjectivity construction of (f) by a large-parameter bound for the transport alone.
Setting. S = T + C with T := T_R and C := C_R, the remainder block S_1 of Theorem C' (step 2), so S : D_R -> R is
Fredholm of index 0. Let X_H and Y_H be Banach spaces with continuous inclusions X_H in Y_H (norm iota') and Y_H in R
(norm iota), and let D_H = {h in X_H : T h in Y_H}, T taken in distributions, with the norm ||h||_{X_H} + ||T h||_{Y_H}.
Assume
(H1) C maps X_H boundedly into Y_H;
(H2) there are omega >= 0 and M >= 1 such that for every lambda > omega the map T - lambda : D_H -> Y_H is bijective
     and ||(T - lambda)^{-1} f||_{X_H} <= M (lambda - omega)^{-1} ||f||_{Y_H};
(H3) there are C_1, a Banach space W and a compact K : X_H -> W with
     ||h||_{X_H} <= C_1 ||(S - lambda) h||_{Y_H} + ||K h||_W for all h in D_H and 0 <= lambda <= lambda_*,
     where lambda_* := omega + 2 M ||C||_{X_H -> Y_H}.
Then S : D_H -> Y_H is Fredholm of index 0, D_H is continuously included in D_R, and the kernel of S on D_H lies in
its kernel on D_R.
Proof. D_H is complete: if (h_n) is Cauchy in D_H, then h_n -> h in X_H and T h_n -> f in Y_H; both limits also hold
in R, so T h = f in distributions, f is in Y_H and h_n -> h in D_H. The inclusion D_H -> D_R is continuous, since
||h||_R + ||T h||_R <= iota iota' ||h||_{X_H} + iota ||T h||_{Y_H}. The map lambda -> S - lambda from [0, lambda_*] to
B(D_H, Y_H) is norm-continuous, with ||(S - lambda) - (S - lambda')|| <= iota' |lambda - lambda'|. At lambda_*,
S - lambda_* = (I + C (T - lambda_*)^{-1})(T - lambda_*) on D_H and ||C (T - lambda_*)^{-1}||_{Y_H -> Y_H} <=
||C|| M/(lambda_* - omega) = 1/2, so S - lambda_* is an isomorphism, of index 0. For lambda in [0, lambda_*], (H3) and
||T h||_{Y_H} <= ||(S - lambda) h||_{Y_H} + (||C|| + lambda iota') ||h||_{X_H} give ||h||_{D_H} <= c (||(S - lambda) h||_{Y_H}
+ ||K h||_W) with K compact on D_H, so S - lambda has finite-dimensional kernel and closed range (upper semi-Fredholm).
The index is locally constant on the open set of semi-Fredholm operators (Kato, Perturbation Theory, IV.5.17 and
IV.5.22), and [0, lambda_*] is connected, so ind (S : D_H -> Y_H) = ind (S - lambda_*) = 0. The kernel statement
follows from D_H in D_R. QED.
Corollary H-spec (the full operator L_red). Let Gamma_H be a Banach space continuously included in Gamma, let
B_H := {beta in B : A beta in Gamma_H} with the norm ||beta||_B + ||A beta||_{Gamma_H}, and put X_H^full := E B_H (+) D_H
and Y_H^full := E Gamma_H (+) Y_H. Assume (H1) to (H3) for S_1 and
(J1) the lower off-diagonal block X = Err + C_R E maps B_H boundedly into Y_H;
(J2) the jet coupling h -> gamma_C[h] maps X_H^full compactly into Gamma_H (the high-order form of (E-J));
(J3) zeta lies in Y_H^full (V084 gives membership in the base target of every order sigma < 13/2).
Then L_red : X_H^full -> Y_H^full is Fredholm of index 0 and its kernel lies in the kernel of L_red on Z. If L_red is
injective on Z, it is an isomorphism of X_H^full onto Y_H^full, and for f in Y_H^full the element L_red^{-1} f is the
low solution.
Proof. A : B_H -> Gamma_H is an isomorphism by the definition of B_H and V041. As in steps 1 and 3 of Theorem C',
L_red = M_H + K_1 + c[.] zeta on X_H^full, where M_H is block lower triangular with diagonal blocks A : B_H -> Gamma_H
and S_1 : D_H -> Y_H and off-diagonal block X, bounded by (J1); so M_H = [[1, 0], [X A^{-1}, 1]] diag(A, S_1) is
Fredholm of index 0 by the lemma. K_1 = E gamma_C is compact by (J2). X_H^full is continuously included in Z (B_H in B,
D_H in D_R), and c is bounded on Z (Lemma C'4), so with (J3) c[.] zeta is a bounded rank-one map into Y_H^full. Hence
L_red is Fredholm of index 0 on X_H^full, and X_H^full in Z gives the kernel statement. With injectivity on Z, L_red is
injective of index 0 on X_H^full, hence bijective, and its inverse is the restriction of the low inverse. QED.
Bound. If the high estimate takes the form ||h||_{X_H^full} <= C_1' ||L_red h||_{Y_H^full} + C_2' ||h||_Z (the compact
errors factoring through Z, with C_1' and C_2' explicit in C_1, ||A^{-1}||, ||X|| and the (J2), (J3) data), then
||L_red^{-1}||_{Y_H^full -> X_H^full} <= C_1' + C_2' K_L iota_Y, with K_L = ||L_red^{-1}||_{Y -> Z} and iota_Y the norm of
the inclusion Y_H^full in Y.
Why the jet row is split off and not shifted (DERIVED). The inclusion fails on the jet coordinate: beta = J H with
J != 0 is in B but not in Gamma, because ||beta||_Gamma = ||z/d||_{L^2(omega)} with z -> J and omega = e^{-2 sigma t} as
t -> -infinity (the same fact as H_0 not in Y, V044), so T - lambda does not map E B into Y for lambda != 0. Restricting
to B_0 = {J = 0} does not help. Write beta = H z and Phi' = 1/d; then (A - lambda) beta = H (d z' - lambda z), and with
