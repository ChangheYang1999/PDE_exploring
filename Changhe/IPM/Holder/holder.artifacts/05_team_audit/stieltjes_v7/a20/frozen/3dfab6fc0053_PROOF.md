# A computable sharper constant for the projection profile

## Statement

Let 0<alpha<=1/4 and let g be the planar projection profile of
`../local_projection_profile/PROOF.md`. For 0<u<1 define

$$A(u)=(1-u)^{-\alpha},\qquad R=u^\alpha,\quad k=1/(1-\alpha),$$

$$B(u)=\left(\frac{1+R^k}{2}\right)^{1/k}
       +\frac{1-R}{2(1-u)^\alpha},$$

$$K_\alpha=\max\{1,\sup_{0<u<1}\min(A(u),B(u))\}.$$

Then [g]_alpha<=K_alpha. The finite witness of
`../finite_projection_witness/PROOF.md` therefore has seminorm at most K_alpha,
and its lower-bound denominator may be replaced by K_alpha. This statement
is exact; numerical upper enclosures of K_alpha require the endpoint and
compact-interval checks below. It does not assert the optimal norm of g.

## Proof

All pairs except opposite-sign quadrants with the negative point at smaller
radius have quotient at most one, by the complete local-profile proof. For
an exceptional pair, normalize the positive radius to one and write u for
the negative radius. The trivial bound g(p)<=1, g(q)>=0 and |p-q|>=1-u gives
A(u). The geometric inequality sin(2a)+sin(2b)<=2|p-q| and the exact weighted
power-mean maximization in that proof give B(u). This latter calculation
holds for every 0<u<1, without the auxiliary u>=alpha restriction used in
the coarser estimate. Taking the smaller bound and then the supremum proves
the assertion. The frozen planar profile is the minimum of g and a function
with seminorm at most one. The other cases in the global finite-witness
proof have seminorm at most one. Clamping and central odd extension preserve
max(K_alpha,1)=K_alpha.

## Endpoint enclosures and finite certification

Fix rational 0<epsilon<1/2. On 0<u<=epsilon, A(u)<=A(epsilon).
For 1-epsilon<=u<1, write v=1-u and

$$c=\frac{\alpha}{(1-\epsilon)^{1-\alpha}},\qquad
R_*= (1-\epsilon)^\alpha.$$

The mean value theorem gives 1-R<=cv. If
M=((1+R^k)/2)^(1/k), the elementary power-mean estimate already proved in
the local-profile theorem gives

$$M-(1+R)/2\le\frac{k-1}{8R_*}c^2\epsilon^2.$$

Moreover,

$$\frac{1-R}{2}(v^{-\alpha}-1)
\le\frac c2\epsilon^{1-\alpha}.$$

Consequently on this endpoint interval,

$$B(u)\le 1+\frac{k-1}{8R_*}c^2\epsilon^2
                +\frac c2\epsilon^{1-\alpha}.$$

The compact interval [epsilon,1-epsilon] may be partitioned into rational
closed cells. Outward interval evaluation of A and B on every cell bounds
their pointwise minimum by the minimum of the two upper endpoints. Taking
the maximum of these bounds and the two endpoint bounds gives a rigorous
upper bound for K_alpha. No sampling or assumed location of the maximum is
used.
