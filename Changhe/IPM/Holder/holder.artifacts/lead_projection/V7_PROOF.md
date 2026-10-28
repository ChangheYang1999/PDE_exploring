# Sharper cell bounds for the positive Stieltjes sums of the projection cusp (certifier `cert_v7.py`)

## Setting

This note changes only the cell rule of the finite lower sum in
`11_lattice_pole_constraints/axis_projection_stieltjes/PROOF.md` (below: the Stieltjes proof). The witness, the admissibility
proof, the identity

    R_1^2 f(a,0) - R_1^2 f(-a,0) = 1 + 4 integral_{X>0,Y>0} V(X,Y) (-d_Y f) dX,   a = 1/2,

and the reduction to strips are taken from that proof without change. Notation: X = a + s d with s in {-1, 1} and
d in a strip [d_l, d_r] (for s = -1, d_r <= 1/2, so X >= 0). The ratio nodes are 0 < v_0 < ... < v_n and the vertical nodes are
Y_j = d v_j. The witness on X > 0 is

    f = max(-h, min(h, min(G, Pr))),   G = g + t,   Pr = -1/2 + P(X - a, Y)/K,   h = 2^(alpha-1) X^alpha,

where g = 2^(alpha-1) sigma dist(., Z)^alpha is the axis polygon signed distance. Here Z is the union of the vertical axis X = 0, the
segment S1 from (0, 1/2) to (1/2, 0), the segment S2 from (1/2, 0) to (1/2 + b, b) and the ray S3 from (1/2 + b, b) in
direction (sqrt 3, 1), together with their reflections. For X > 0 and Y > 0 the nearest point of Z lies on one of the four
pieces X = 0, S1, S2, S3 (reflection in the line Y = 0 or X = 0 does not decrease the distance from a point of the open
quadrant). sigma = +1 below the graph Y = B(X) and -1 above it, with B(X) = max(1/2 - X, min(X - 1/2, (X - 1/2 + (sqrt 3 - 1) b)/sqrt 3)).
These are the formulas of `witness()` in the verifier's `certify_axis_projection_stieltjes_v2.py`.
`cert_v7.py` evaluates them in the same way (function `branches`).

By the Stieltjes proof, a strip contributes at least (d_r - d_l) sum_j A_j B_j whenever, for every d in the strip,

    F_j(d) := f(X, d v_j) - f(X, d v_{j+1}) >= A_j >= 0   and   min(V(X, d v_j), V(X, d v_{j+1})) >= B_j >= 0.     (S)

The kernel bound B_j is the v2 rule (lower endpoints of ball enclosures over the strip). V is evaluated in the equivalent
form X v/(pi d (1 + v^2)((X + 1/2)^2 + d^2 v^2)), which is the same function. The new content is a choice of A_j: the
maximum of the finite candidates (a) to (d) and (f) below, replaced by 0 if negative. Each candidate is a lower bound for
F_j on the whole strip, so their maximum is one too. Cells with no finite candidate get A_j = 0.

## The candidates

**(a) v2.** The lower endpoint of the ball enclosure of F_j with d replaced by the ball [d_l, d_r].

**(e) Powers of balls touching 0.** Item (e) is a correction of the enclosure itself, not a candidate. In v2, x^alpha for a
ball x whose lower endpoint is 0 (the distance near Z, or X near 0 for s = -1) is computed as exp(alpha log x) and gives nan, so
the cell gets no bound. Here x^alpha is enclosed by [0, hi(x)^alpha] when x is not certainly positive. This is valid
because x >= 0 (it is an enclosure of a distance, or of max(0, X)) and t -> t^alpha is nondecreasing on [0, oo).

**(b) Exact profile scaling.** Suppose that at both nodes the strip enclosures prove Pr < G, Pr < h and Pr > -h. Then for
every d in the strip f = Pr at both nodes. P is positively homogeneous of degree alpha and even in each variable, so
P(s d, d v) = d^alpha p(v) with p(v) = P(1, v). Hence F_j(d) = d^alpha (p(v_j) - p(v_{j+1}))/K, and if p(v_j) >= p(v_{j+1}) this
is at least d_l^alpha (p(v_j) - p(v_{j+1}))/K.

**(c) First-order mean value.** For a node v put phi_v(u) = f(a + s u, u v) for u in the strip. Suppose the strip enclosures
determine the active branch of f at the node:

- the profile branch as in (b); or
- the upper clamp, h < min(G, Pr); or
- the lower clamp, G < -h or Pr < -h; or
- the distance branch. This requires G < Pr, G < h, G > -h and X > 0. The side of the graph must be certain (Y < B or
  Y > B, which fixes sigma). Exactly one of the four pieces must be certainly nearer than the other three; call its
  distance r. Finally r > 0 must be certain.

On the distance branch, dist(., Z) = r on a neighbourhood of the strip segment, and r is the distance to a closed convex set
(a line, a segment or a ray). Such a distance is C^1 off the set, with gradient (z - proj z)/r. With the direction
w = (s, v) of the segment, phi_v is C^1 on the strip, and the chain rule gives

    profile: alpha u^(alpha-1) p(v)/K;   upper/lower clamp: +- 2^(alpha-1) alpha X^(alpha-1) s;
    distance: sigma 2^(alpha-1) alpha r^(alpha-1) <grad r, w>.

`derivatives` encloses these on the strip ball. If both nodes have a certified branch, F_j is C^1 on the strip and F_j'
lies in the difference E of the two enclosures. For d_m = (d_l + d_r)/2 and every d in the strip,

    F_j(d) >= F_j(d_m) - sup|E| |d - d_m| >= lo F_j(d_m) - hi|E| (d_r - d_l)/2,

with F_j(d_m) enclosed by evaluating the witness at the point d_m (`mid`). This is candidate c_mv.

**(d) Second-order mean value.** Under the conditions of (c), phi_v is C^{1,1} on the strip. The second derivative exists
almost everywhere and lies in the following enclosures:

    profile: alpha(alpha-1) u^(alpha-2) p(v)/K;   clamps: +- 2^(alpha-1) alpha(alpha-1) X^(alpha-2);
    distance: sigma 2^(alpha-1) [alpha(alpha-1) r^(alpha-2) <grad r, w>^2 + alpha r^(alpha-1) w^T D^2 r w].

For the axis piece, and for a segment or ray piece whose projection parameter is certainly interior on the strip ball, r is
an affine distance to a line, so D^2 r = 0. Otherwise D^2 r exists a.e. and 0 <= D^2 r <= (I - grad r grad r^T)/r. This is
exact in the endpoint region, where r is the distance to a point, and it is 0 in the line region. The two regions meet along
a line, where r is C^{1,1}. Hence w^T D^2 r w lies in [0, (|w|^2 - <grad r, w>^2)/r]. Taylor's formula with integral
remainder, for a C^{1,1} function, gives

    F_j(d) >= F_j(d_m) - |F_j'(d_m)| |d - d_m| - sup|F_j''| |d - d_m|^2/2.

F_j'(d_m) is enclosed at the point d_m: the branch certified on the strip is the true branch at d_m, and the point
evaluation either certifies the same branch or none, because the tests are applied in the same order and the strip branch
satisfies strict inequalities at d_m. This gives c_mv2 = lo F_j(d_m) - hi|F_j'(d_m)| hw - hi|F_j''| hw^2/2 with
hw = hi((d_r - d_l)/2).

**(f) Refinement.** If no candidate (a) to (d) is finite, or the best one is (a), split [d_l, d_r] into M = 8 subintervals with
ball endpoints e_k (consecutive balls overlap, and the union of the M hulls contains the strip). Then
min_k lo F_j(ball of the k-th subinterval), with each F_j enclosed as in (a) and (e), is a lower bound for F_j on the strip,
because every d lies in some subinterval. The loop stops early when the running minimum is not finite or not above the
current best, in which case the candidate is not used.

## Pieces of one sign

A run covers d in [exp(left), exp(right)] with nx equal strips in log d. The default right end is log(1/2) for s = -1
and 24 for s = 1. Several runs of one sign with disjoint [left, right] give disjoint sets of strips. Omitting strips only
removes nonnegative contributions (Stieltjes proof). `combine_v7.py` checks the following:

- common alpha, b, t and K;
- once-only coverage of the nx strips of every piece, with equal grid parameters;
- disjointness of the pieces of each sign, and right <= log(1/2) for every explicit right end with s = -1;
- unchanged source hashes and the single certifier `cert_v7.py`;
- the profile certificate K >= [P]_alpha, with the same registry as `combine_lead.py`.

It then forms D >= 1 + 4 * (sum of the chunk lower enclosures).

## Relation to earlier variants

`cert_v4.py` is v7 without (c), (d), (e), (f); `cert_v5.py` adds (c); `cert_v6.py` adds (d). On the test at alpha = 3/10,
b = 3/2, t = 0, K = 1007/1000, s = +1, 4096 x 256 strips and nodes, log d in [-18, 12], log v in [-6, 3], the partial sums
1 + 4 * (strip sum) are 2.1762 (v4; default ranges), 2.2105 (v6) and 2.2970 (v7). The floating value of the same grid with exact
values at the strip endpoints, a diagnostic and not a bound, is 2.3118. Most of the v6 to v7 gain comes from the cells that cross
the zero set at large d, which v2 to v6 leave empty because of the nan in (e).
