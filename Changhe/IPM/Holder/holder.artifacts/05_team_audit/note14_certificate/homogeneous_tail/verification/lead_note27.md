## Note 27 (2026-10-28T09:39Z): cross-read of the homogeneous tail (note14_certificate/homogeneous_tail/PROOF.md): no defect
To the verifier. I read the whole PROOF.md (183 lines) and checked each step by hand; I found no error.
(a) Geometry. Zinf is the zero set of cos(3 theta), i.e. the vertical line plus the rays at +-30 and +-150 degrees. Each
    infinite ray of Z0(b) - m is the matching Zinf ray translated by (+-(b+1/2), +-b), of length H. The finite segments lie in
    the closed disk of radius H (the farthest point is (1/2+b, b)), and 0 lies in Zinf. So d_H <= H, which gives (4). For
    the signed bound (5), B0 agrees with the B of your Stieltjes certifier (max(1/2-X, min(X-1/2, (X-1/2+(sqrt3-1)b)/sqrt3))).
    For opposite signs the two distances are at most the vertical distances to (X, B0(X)) in Z0 and to (X, X/sqrt3) in Zinf.
    Their sum is |B0 - X/sqrt3|. This is piecewise linear with values 1/2, -1/(2 sqrt3) and b - (b+1/2)/sqrt3 (constant on the
    ray part), all at most H in absolute value. (6): p_a is 1-Holder by concavity, 2^(a-1)(s^a+t^a) <= (s+t)^a, and by
    |s^a-t^a| <= |s-t|^a.
(b) Branches. The rays are 60 degrees apart, so dist(w, Zinf) <= |w|/2; with the vertical line in Zinf, |ginf| <= h. On X > 0,
    ginf > 0 gives |theta| < pi/6 and cos 2theta > 1/2, so P(w) >= (1+2^-a)|w|^a/2 and lambda P >= |w|^a/2 >= ginf. If
    ginf <= 0, P >= 0 suffices, since P = (|w|^a + sign(cos 2theta)|cos 2theta|^a |w|^a)/2 >= 0. Hence (8). (9) follows from
    lambda[P]_a <= 1 and |e1/2| = 1/2. (10) follows because max and min are 1-Lipschitz in the sup norm of their arguments.
    Odd reflection and the oddness of vinf cover X < 0.
(c) Dipole. K(z) = Re z^-2/(2 pi), and (w-1/2)^-2 - (w+1/2)^-2 = 2w/(w^2-1/4)^2 = 1/(w^3(1-1/(4w^2))^2), which gives (11). D = Re
    1/(pi w^3) = cos 3theta/(pi r^3). In (12), |1-q| >= 1-q_R, and |(1-q)^-2 - 1| <= (1-|q|)^-2 - 1 = (2|q|-|q|^2)/(1-|q|)^2. The
    radial integrals are 2B/R and R^(a-3)/(2(3-a)), each times (1-q_R)^-2, which is (3). The main term: 12 half-lobes of width pi/6,
    dist(e^(i theta), ray) = sin t and |cos 3theta| = sin 3t, so the angular integral is 6 * 2^a * int_0^(pi/6) sin 3t sin^a t dt
    = 2 pi a3(a). The radial integral is R^(a-1)/(1-a).
(d) Series. The substitutions u = sin t and v = 2u give the integral form. The binomial series of (1-v^2/4)^(-1/2) gives
    (13), and the tail bound sum_{k>=N} 4^-k = 4^(1-N)/3 gives (14). Numerical check (mpmath, 30 digits; not part of the proof):
    the quadrature of the defining integral, the series (13) and the direct angular integral of cos(3 theta) ginf agree:
    a3(1/2) = 0.2510198682, a3(3/4) = 0.2268039392, a3(9/10) = 0.2143414335.
(e) Conditions. lambda(1+2^-a) >= 1 holds for every lambda in use (for example 10/11 at a = 9/10 gives 1.396). Absolute
    convergence: |K-difference| |f| = O(r^(a-3)), integrable at infinity in 2D. I did not re-run your prefix auditor. Once you
    record acceptance I will put the three conditional values (D_.5 >= 2.4389659544, D_.75 >= 2.8866494385,
    D_.9 >= 5.2405340577) into Table 1 through your registry.
(f) Report: V127 items (Section 10(2) ratios 1.0942 and 1.0864, the Theorem 5.7 title, "rho sufficiently small" and the
    infimum over q in H in 5.7(v), definition of the complex J_alpha) go into version 21.
(g) Lead computation: cert_v7.py (scratch/projcert). In your v2 Stieltjes certifier, x^alpha for a ball touching 0 (a
    distance ball near the zero set) evaluates to nan, so the cells that cross the zero set receive no mass. At alpha 3/10,
    nx 4096 these cells hold about 43% of the large-d mass. v7 encloses x^alpha by [0, hi(x)^alpha] there and refines v2 cells
    by splitting the strip into 8 subintervals (min over subintervals). The mean-value rules of v5/v6 are also kept. A test is
    running; a proof note follows with the production.

