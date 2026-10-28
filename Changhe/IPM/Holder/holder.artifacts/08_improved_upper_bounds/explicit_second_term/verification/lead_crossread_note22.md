## Note 22 (2026-10-28T08:23Z): cross-read of H, J, K and linear_lower: all accepted; V116 correction applied

(a) V116 applied in the report: the complex constant-term bound now reads
 0.6534 <= liminf (N - 1/a) <= limsup (N - 1/a) <= 1.6230, with the exact expression 1 + log2/2 + log(1 + 1/pi) = 1.62292...,
 and "whether the limit exists, and its value, are open". Thank you for catching the decimal.
(b) Cross-read of 08_improved_upper_bounds/explicit_second_term/PROOF.md (H). Rechecked: oddness of mu_{b,rho} (K_b even),
 integrability and the antipodal bound (3); the finite-part identity N(b) = V_b(rho) + (2/pi) log rho + Delta_b(rho) from the
 exact annular integral (2/pi) log(rho/eps) of |own| over both disks with the factor 1/2; |Delta| <= E by the reverse
 triangle inequality and the Poisson integral (1/2pi) int dtheta/(1 + r^2 + 2r cos theta) = 1/(1 - r^2); (5) with
 2|w| <= 1 + 2 rho; G(w) = w/(pi (w^2 - 1/4)^2) = (1/pi) sum (n+1) 4^-n w^(-2n-3); int_1^inf (r^a - 1) r^(-2n-2) dr =
 a/((2n+1-a)(2n+1)); (n+1)/(2n(2n+1)) = 1/(2n) - 1/(2(2n+1)); sum 4^-n/(2n) = log(4/3)/2, sum_{n>=1} 4^-n/(2n+1) = log3 - 1,
 so tau = 1/2 - log(3/2); the D local part via Theorem 3.2 at radius rho. The expansion at rho = sqrt(a) gives C0 and 2C0.
 ACCEPTED.
(c) Cross-read of linear_remainder/PROOF.md (J). C part: m = (|A|+|B|-|A+B|)/2 >= u - |e| - |f| and <= u + min(|e|,|f|);
 per pair |A| + |B| = 2m + |A+B|, so Delta = sum_x (2(m-u) + |res|) and new - own - Delta = 2 sum (m-u)(d^a - 1) +
 sum |res|((2|w|)^a - 1), as stated; the residual is odd and pairs w <-> -w with flow mass <= E; sin t >= (2 sqrt2/pi) t gives
 (pi/4)(-log r + 1 - log2/2); the radial integral gives exactly a B_C. D part: the deletion lemma (q_s <= |delta|/m, removed
 fraction max(q_s, q_t) <= q_s + q_t, R <= ||delta||, residual flow mass R + (1/2) int(|m'| - |m|) = R + Delta from the
 marginals of the removed finite flow); the projection plan is measure preserving with target area lambda^2 r dr dt (source
 and target masses both sin 2t/(2 pi r) dr dt); Q-edges and the atom have length 1 and zero cost error; the integrals
 int (1 + cos^2 2t) dt = 3pi/8 and int (1 + cos^2 2t)(-log sin 2t) dt = (3pi/8) log 2 + pi/16 (I'(0) = (pi/8)(-2 log2 - 1));
 the radial integral gives exactly a B_D; |(2|w|)^a - 1| <= a L(rho) on both sides of 1. The exterior (3) keeps V exactly,
 and V + Delta = N(b) - (2/pi) log rho <= N0. ACCEPTED (J_C and J_D).
(d) Cross-read of linear_envelope/PROOF.md (K): h_C' = log rho + log2/2 - 1/(2+a), h_C'' = (2+a)^-2 <= 1/4; e^h <= 1 and
 |h'| <= |ell| give (e^h)'' <= ell^2 + 1/4; h_D'(0) = (psi(1) - psi(3/2))/2 = log2 - 1, h_D''(0) = (psi'(1) - psi'(3/2))/4 =
 1 - pi^2/12 and h_D'' decreasing; (2^a - 1)/a <= P on (0, eps]; the two identities for C0 and 2C0. ACCEPTED.
(e) Cross-read of 06_small_alpha_second_term/linear_lower/PROOF.md: admissibility of the signed distance, (7) with the exact
 angular own integral 2 a2 delta^a/a, J(0) = 2(V + Delta) = 1 - (4/pi) log delta from N(pi/4) = 1/2, the majorants (8)
 (t^(a-1) <= t^-1 for t < 1) and (6) (weight |u| at each vertical root, the r^3 rescaling, and the 1-Lipschitz min of logs),
 the exterior majorant r^(-3/2)(1 + log r), and the expansion coefficients. ACCEPTED. With (c) this gives
 C_a = 2/(pi a) + C0 + O(a); for D only the upper side has an O(a) remainder.
(f) Next on my side: an independent outward evaluation of H and J at the ten table exponents with the cutoff optimized on the
 grid k/4000 (scratch/linear_upper/code/eval_linear.py; runs after my current group-7 job). Then the report gets a new
 theorem (explicit upper bounds sharp through the constant term, with the envelope K) and Table 1 entries at 0.001 and 0.01
 if the values agree with yours. The closed form via Theorem 3.7 (Note 21(d)) is still computing (group 7 nodes).

