Addendum (general cut set; same proof). The line X = 0 can be replaced by any closed set Z with dist(x, Z) >= 1/2 and
dist(y, Z) >= 1/2. Put h_Z = 2^(alpha-1) dist(., Z)^alpha. On each component O of R^2 \ Z take F_O with [F_O] <= 1 on O
(F_O = +inf or -inf allowed) and put f = max(-h_Z, min(h_Z, F_O)) on O, f = 0 on Z. Then [f] <= 1 on R^2 (pairs in different
components: the segment meets Z, and 2^(alpha-1)(d_p^alpha + d_q^alpha) <= (d_p + d_q)^alpha <= |p-q|^alpha); h_Z(x) >= 1/2,
so F(x) <= -1/2 and F(y) >= 1/2 give f(x) = -1/2, f(y) = 1/2 and D >= |int nu f| + 1/2. The polygon witness of Theorem 4.5
is the case Z = Z_a, F_O = +-inf (but there dist(x, Z) = 0). Why it matters: with Z = {X = 0} the clamp forces f -> 0 on the
whole bisector, which in the far field kills the middle sector of the polygon witness (there |cos theta| < sin of the angle to
the nearest zero ray), so for alpha near 1 the line cut loses part of the 1/(1-alpha) term. A cut that follows the polygon
zero set outside the two disks B(x,1/2), B(y,1/2) and closes up near them keeps the far field. Near x the best one-sided
profile is F = -1/2 + dist(z, N)^alpha with N the closed negative sectors of nu at x: it has seminorm 1 (a segment from a
positive to a negative point meets the zero set) and keeps the fraction 2^(-alpha) of the local C value (not 1/2, which is
what F = g - 1/2 keeps).

