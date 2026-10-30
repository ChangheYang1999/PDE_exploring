# The correction forced by the first integrable residual tail

This note gives a conditional asymptotic theorem and an exact reference-design
operation. It does not construct a stationary IPM solution or an inverse. The
candidate application uses the independently checked sector identities in
../weighted_tail_candidate_audit/PROOF.md. That topic, together with
../weighted_forced_tails/PROOF.md, is the dependency chain.

## 1. A weighted pointwise velocity estimate with the contact term

Let -3<q<0. Let h be a real, centrally odd C1 function on R2 and define

    H_q(h)=max{sup_X (1+|X|)^(-q)|h(X)|,
                 sup_X (1+|X|)^(1-q)|grad h(X)|} < infinity.

Use the canonical IPM velocity with multiplier
(xi_1 xi_2,-xi_1^2)/|xi|^2. In physical space this is

    U[h](X)=(0,-h(X)/2)+PV int K(X-Y)h(Y)dY,
    K(Z)=(-z_1 z_2, (z_1^2-z_2^2)/2)/(pi |Z|^4).       (1)

In particular the local/contact term is retained. For every r=|X|>=2,

    |U[h](X)| <= C_q H_q(h) r^q,                       (2)
    C_q = 1/2 + 2^(-q) + 2^(1-q)/(q+3)
                + 2^(3-q) + 2^(q+2)/(-q).

Proof. The kernel has zero angular mean,
|K(Z)|=1/(2 pi |Z|^2), and ||DK(Z)||_op=1/(pi |Z|^3).
Split the plane into the following four disjoint regions, ignoring
measure-zero boundaries:

(a) |Y-X|<r/2. Subtract h(X) in the principal value. On this ball the
line segment from X to Y stays outside radius r/2. Thus
|grad h|<=H_q(h) 2^(1-q) r^(q-1). Integrating |K(Z)||Z| over
|Z|<r/2 gives r/2. The contribution is at most
2^(-q)H_q(h)r^q.

(b) |Y|<r/2. This is disjoint from (a). Central oddness gives
int_(|Y|<r/2) h(Y)dY=0. Subtract K(X), apply the derivative bound on
X-tY, and use (1+rho)^q<=rho^q. The contribution is at most

    [8/(pi r^3)] 2pi H_q(h) int_0^(r/2) rho^(q+2)drho
      = [2^(1-q)/(q+3)] H_q(h)r^q.

(c) r/2<=|Y|<=2r and |Y-X|>=r/2. Bound the kernel by 2/(pi r^2),
the density by H_q(h)(r/2)^q and the area by4pi r^2. This gives
2^(3-q)H_q(h)r^q.

(d) |Y|>2r. Bound the kernel by2/(pi |Y|^2). The integral is at most

    4H_q(h) int_(2r)^infinity rho^(q-1)drho
       = [2^(q+2)/(-q)]H_q(h)r^q.

The contact term is at most H_q(h)r^q/2. Summing proves (2).
Local C1 regularity justifies the principal value, q<0 makes the far
integral absolutely convergent, and q>-3 makes the estimate in(b) finite.

## 2. A stationary correction has a forced leading coefficient

Fix c>1, gamma=1/c and delta=1-gamma. Let R be a real C1 S1 reference
with canonical velocity. Suppose for r>=R0>=2 that

    |U[R](X)|<=V r^gamma, |grad R(X)|<=G r^(gamma-1),
    |F(R)(r,theta)-r^q A(theta)|<=E r^(q-epsilon),        (3)
    F(R)=c X.grad R-R+U[R].grad R,

where -3<q<0, epsilon>0, V,G,E>=0 and A is continuous. Suppose h is
centrally odd C1, H=H_q(h)<infinity, and R+h is a stationary solution
at the same c with velocity U[R]+U[h]. Then for r>=R0,

    h(r,theta)=r^q A(theta)/(1-cq)+e(r,theta),            (4)

with the explicit uniform estimate

    |e| <= E r^(q-epsilon)/[1-c(q-epsilon)]
       + H(V+C_q G)r^(q-delta)/[1-c(q-delta)]
       + C_q H^2 r^(2q-1)/[1-c(2q-1)].                  (5)

Every denominator is positive. This theorem assumes weighted C1 decay
of h; an L2 correction alone is not asserted to have that decay.

Proof. Subtract the reference equation from the stationary equation:

    c r d_r h-h=-F(R)-U[R].grad h-U[h].grad R-U[h].grad h.

By (2)-(3), the three nonlinear/transport terms have absolute sum at
most H(V+C_qG)r^(q-delta)+C_qH^2r^(2q-1). Since q<gamma,
r^(-gamma)h(r,theta) tends uniformly to zero at infinity. Multiply the
radial equation by r^(-gamma-1)/c and integrate from r to infinity.
The identity

    r^gamma/c int_r^infinity t^(p-gamma-1)dt
       = r^p/(1-cp), p<gamma,

gives(4)-(5), including the sign. No derivative of U[h] is taken, so
this argument introduces no unmentioned second derivative of h.

If A=(cq-1)Theta, formula(4) reads h=-r^q Theta+lower powers. Thus
an admissible correction must cancel that reference density sector.
This is a necessary asymptotic statement, not a sufficient condition.

## 3. Exact cancellation of the reference descendant

For the canonical campaign c=4076476460239181/2251799813685248,
set q=1-4delta-2=-1-4delta. Then -3<q<0. The exact candidates007,013
and014 have nonzero first residual sector(K,L)=(4,1). Their density
and stream sectors with L=1 and K<=3 vanish. Their leading ladder
residuals vanish for K<=8. Hence the residual coefficient at(4,1)
is exactly(cq-1)Theta_(4,1), without nonlinear cross terms.
The conditional theorem above forces h=-r^q Theta_(4,1)+lower powers.
The polynomial candidates satisfy the reference growth assumptions in
(3), with some finite V,G,E and epsilon>0; these constants are not
numerically evaluated here and are not used in a closure inequality.

There is also an explicit smooth correction direction that cancels
this descendant at the level of the reference. In the j=3 potential
branch, write

    chi_3=(1+r^2)^p sum_m P_m(t)cos(2m theta),
    p=(3+gamma-3delta)/2, t=r^2/(1+r^2),
    A1_m=pP_m(1)-P'_m(1).

Add the potential

    eta_chi=-(1+r^2)^p sum_m A1_m t^(m+4)(1-t)cos(2m theta).
                                                               (6)

Define eta=-d_y Delta eta_chi and eta_psi=d_x d_y eta_chi.
All coefficients A1_m are exact rationals in data. Formula(6) has
zero leading-potential coefficient at infinity and first descendant
-A1_m. It therefore cancels both the density and stream sectors(4,1),
while changing no leading ladder sector. It changes no L=1 sector
with K<=3. The residual of R+eta consequently has every sector of
exponent >=-3 equal to zero. Terms with K>=10 or L>=2 have exponent
below -3; the only other sector labels near that cutoff are checked
explicitly in the exact arithmetic. Thus the residual is
O(r^(-3-epsilon_1)) for some epsilon_1>0 and belongs to E_a at infinity
for every a>-2. This statement is about residual membership, not
smallness or invertibility.

At the origin, t^(m+4)cos(2m theta) is smooth and vanishes to order
2m+8. Hence eta_chi has zero derivatives through order7, eta has zero
derivatives through order4, and U[eta] has zero derivatives through
order4. In particular it preserves all density Taylor normalizations
through cubic order and the origin velocity strain. At infinity,
eta_chi=O(r^(q+3)), eta=O(r^q), and U[eta]=O(r^q). The velocity
obtained from eta_psi is canonical: it is a smooth decaying solution
of the same divergence/curl equations, and its difference from the
canonical velocity is a decaying entire harmonic vector field, hence
zero. This also follows in distributions from the Fourier multipliers.
The correction is S1 and belongs to L2, so it preserves the affine
L2 class and the fixed-c leading profile. Its nonzero leading density
sector means eta is in E_a exactly when a>q+1. At a=q+1 the tail
integral diverges logarithmically. Thus the operation changes the
tighter weighted affine class in precisely the range previously
excluded; it is not an evasion of that exclusion theorem.

The new reference may have a larger residual in the interior, and its
L2 distance from an exact solution is not controlled by this tail
operation. The direction is an analytic design input for a subsequent
constrained optimization, not a new accepted campaign snapshot.

## 4. Verification and review status

The checker reads only frozen exact sector tables and canonical files
already in this lane. It stores the finite potential correction in
exact JSON, checks the leading and first-descendant moment identities,
checks all relevant residual coefficients after cancellation, and
checks the origin orders symbolically. It reports exact exponents
and an Arb enclosure of C_q. No generated numeral-filled proof source
or numerical quadrature is used. This new general theorem and the
reference-design construction require independent Opus review before
being labelled AUDITED.
