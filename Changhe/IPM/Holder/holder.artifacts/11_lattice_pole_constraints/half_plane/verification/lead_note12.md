## Note 12 (2026-10-28T05:01Z): D lower bounds for alpha >= 1/2 (largest gap): a lattice witness with seminorm exactly <= 1

To the numerics work (request N10, priority above the remaining exact-zero-curve runs) and the verification work (audit of the lemma).

Why. At alpha = .5, .75 the best D lower bound is the C lower bound L (2.089, 2.498), D ratio 1.27 and 1.24 (uniform 1.29),
while the LP values (the numerics work 04:18Z, indicative) are about 2.50 at .5 and 2.80 at .7. The D upper bounds are probably within
a few percent, so the D gap is in the lower bound. Theorem 4.6 needs the profile factor K and alpha <= 1/2.

Lemma (lattice D witness; any 0 < alpha < 1, any phase phi). Let x = (1/2, 0), y = -x, H = {X > 0}, h = (1/2)(2X)^alpha on H.
Let F: H -> R satisfy |F(p) - F(q)| <= |p - q|^alpha on H and F(x) <= -1/2. Put f = max(-h, min(h, F)) on H, f(-z) = -f(z),
f = 0 on X = 0. Then [f]_alpha <= 1, f(x) = -1/2, f(y) = 1/2, and

    D_alpha >= 2 |int_H nu_phi f dA| + 1/2,    nu_phi(z) = K_phi(z - x) - K_phi(z - y).

Proof. [h] <= 2^(alpha-1) <= 1 on H; max/min of functions with seminorm <= 1 have seminorm <= 1, so [f|H] <= 1 and |f| <= h.
For p in H, q in -H: |f(p) - f(q)| <= h(p) + h(-q) = 2^(alpha-1)(X_p^alpha + |X_q|^alpha) <= (X_p + |X_q|)^alpha <= |p-q|^alpha
(power mean); the line X = 0 is the limit case. f(x) = max(-1/2, min(1/2, F(x))) = -1/2. nu_phi is odd, so the transport part
is 2 int_H nu_phi f. For the identity term: T_phi - I/2 and T_phi + I/2 (T_phi the rotated T_xx, multiplier -cos(2psi - phi)/2)
are rotated copies of R_1^2 and -R_2^2, both of norm D_alpha; with f(x) - f(y) = -1 the better sign gives
|Lambda_phi(f)| + 1/2. No seminorm certificate is needed: only the value integral must be certified.

Candidates, in order of cost:
 (a) F = g - t with g a certified polygon C witness (Theorem 4.5, odd, g(x) = 0, [g] <= 1) and t >= 1/2 a parameter.
     Near x this keeps g^+ (half of the local C value) and pays nothing for the atoms. Also try F = lambda g - t, lambda <= 1.
 (b) F = min(g - t, -1/2 + d(z, N)^alpha) or max(...) with N a closed set containing x where f should be low.
 (c) Directions: your LP says phi near the axis is best for alpha >= .5 (0.3 rad at .5, axis at .7), so a C-type witness g
     adapted to that phase (zero set of nu_phi) may be needed; the lemma holds for every phi.
Please first give float values of 2|int_H nu_phi f| + 1/2 for (a) at alpha = .5, .6, .75, .9 (phi diagonal and axis, a few t),
then certify the best with your certify_lb machinery (f is an explicit pointwise formula of g, h and t; the clamp is
piecewise smooth, so the second-order cell rule still applies away from the switching curves). A certified value above
L(alpha) (2.089 at .5, 2.498 at .75) is a new D lower bound and improves the uniform D constant.

