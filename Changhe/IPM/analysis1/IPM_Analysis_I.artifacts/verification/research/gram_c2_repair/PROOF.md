# Exact C2 repair of the compact spline columns

## Statement fixed before computation

Let a_0<...<a_n be rational numbers and let P_i(t-a_i) be real polynomials with rational coefficients on [a_i,a_{i+1}], extended by zero outside [a_0,a_n]. The original piecewise section need not be continuous. For q=0,1,2 define target qth t-derivative traces

    beta_(0,q)=beta_(n,q)=0,
    beta_(i,q)=(P_(i-1)^(q)(a_i-a_(i-1))+P_i^(q)(0))/2

at every internal endpoint. On piece i let d_i be the unique polynomial of degree at most5 whose first three endpoint jets are

    d_i^(q)(0)=beta_(i,q)-P_i^(q)(0),
    d_i^(q)(w_i)=beta_(i+1,q)-P_i^(q)(w_i),  q=0,1,2,
    w_i=a_(i+1)-a_i>0.

Set Bhat=P_i+d_i on each piece and zero outside. Then Bhat is C2 on the real line, with locally Lipschitz second derivative. It is compactly supported. If the first piece of P has a nonzero coefficient of degree at least6 and degree strictly above every nonzero correction coefficient, Bhat is nonzero on every sufficiently small interval immediately to the right of a_0. A finite family with distinct support starts and such first pieces is linearly independent.

For an integer m>=0 let Phi_m(theta)=cos(theta)^2 sin(theta)cos(2m theta) and hhat=r^3 Bhat(log r)Phi_m(theta), with hhat=0 at the origin. Then hhat is C^{2,1} on the plane, supported in a compact annulus, even in x and odd in y. Its factor ahat=hhat/(x^2 y), initially defined off the axes, extends to a C^{2,1} even-even function which vanishes near the origin. Thus this repair does not change a central coefficient when added to an admissible density. It supplies the requested local C^{2,alpha} regularity for every 0<alpha<1. It need not be smooth to all orders.

Let L>0 and k<3/2. Put

    m(r)=(r/L)^3(1+r^2/L^2)^((k-3)/2),
    w(r)=m(r)^(-2)(1+r^2/L^2)^(-3/2),
    ||h||_X^2=integral_R2 (h^2+r^2|grad h|^2)w(r) dX.

X uses weak derivatives. The broken norm ||.||_b uses classical derivatives inside each original piece. Write

    W(t)=e^(2t)(1+e^(2t)/L^2)^(3/2-k),
    E_i=integral_0^w_i [d_i^2+(3d_i+d_i')^2] ds,
    V_i=integral_0^w_i P_i^2 ds,
    U=sum_i W(a_(i+1))E_i,
    V=sum_i W(a_i)V_i.

For each nonzero original radial column, V>0 and for every single angular mode

    ||hhat-h||_b / ||h||_b <= sqrt(U/V).                    (1)

This is not an X distance from the potentially discontinuous original h. The repaired hhat itself belongs to X. If h0 is the topic132 C0 repair and both raw relative bounds are strict, ||h0-h||_b<delta0||h||_b and ||hhat-h||_b<delta2||h||_b, with delta0<1, then

    ||hhat-h0||_X / ||h0||_X < (delta0+delta2)/(1-delta0).  (2)

Equation(2) is a true X distance between continuous functions. It is still only a single-column estimate. No uniform relative bound on arbitrary linear combinations or any operator-image difference is asserted.

## Exact Hermite interpolation and regularity

At width1 the six polynomials

    H00=1-10s^3+15s^4-6s^5,
    H01=s-6s^3+8s^4-3s^5,
    H02=(s^2-3s^3+3s^4-s^5)/2,
    H10=10s^3-15s^4+6s^5,
    H11=-4s^3+7s^4-3s^5,
    H12=(s^3-2s^4+s^5)/2

have respectively the six unit endpoint jets (value, first derivative, second derivative at0, then at1). Direct differentiation verifies all36 Kronecker conditions. If e_(L,q),e_(R,q) are the desired physical t-jets of d at width w, then

    d(t)=sum_(q=0)^2 w^q [e_(L,q)H0q(t/w)+e_(R,q)H1q(t/w)].

This gives existence with rational coefficients. If two such interpolants existed, their difference would be divisible by t^3(t-w)^3, of degree6, while having degree at most5. The difference is therefore zero. Adding d to P gives exactly the prescribed shared jets, including zero exterior jets at the two support endpoints. The resulting function and its first two derivatives are continuous. On a bounded interval the piecewise third derivatives are bounded, so integration along the finite subdivision proves that the second derivative is Lipschitz. Outside the finite support it vanishes. This proves C^{2,1} regularity.

The correction has degree at most5. Hence a nonzero leading coefficient of degree at least6 in the first piece cannot change. That repaired polynomial cannot vanish on an open interval. To prove independence, order the distinct support starts. Immediately after the earliest start and before the next, only its function can be nonzero. A vanishing linear combination must have its first coefficient zero. Repeating proves all coefficients zero. Replication over finitely many Phi_m preserves independence: off the common angular zeros, a finite cosine polynomial vanishes only when all its coefficients vanish. Apply radial independence to each angular coefficient.

Because every support lies in a compact annulus, polar coordinates are smooth local coordinates there. The function cos(2m theta) is a smooth single-valued function away from the origin: it is the real part of (x+iy)^(2m)/r^(2m). The real part is unchanged under either coordinate reflection. Multiplication by the C^{2,1} radial factor therefore gives the even-even factor ahat=Bhat(log r)cos(2m theta), including on the axes, and hhat=x^2 y ahat. It vanishes near the origin. The zero extension and the matched endpoint jets preserve C^{2,1} across support circles. Compact support and these derivatives give finite X norm because all weights are bounded on its support.

Under the explicit background assumptions of topic135, these repaired functions also have linearized images in H1 locally. Indeed their first derivative traces agree, so the topic135 circle-jump criterion applies. This does not by itself establish a finite global weighted image norm or smallness of the image change. In particular the topic132 image may fail H1, and there is no H1-distance to such an image.

## Proof of the norm estimates

Let A0=integral_0^(2pi)Phi_m^2 and A1=integral_0^(2pi)(Phi_m')^2. They are nonnegative and A0>0. Polar differentiation gives radial derivative r^2(3B+B')Phi_m and angular derivative component r^2 B Phi_m'. The area measure is r^2 dt dtheta, so the exact broken square norm is

    L^6 integral W(t)[(A0+A1)B^2+A0(3B+B')^2] dt.       (3)

Here r^8 w(r)=L^6 r^2(1+r^2/L^2)^(3/2-k). This checks the full-plane norm factor without an external convention. Since k<3/2, W is strictly increasing: both e^(2t) and the positive-power factor are positive and strictly increasing. Dropping the nonnegative derivative term from the original norm in (3) and using the left endpoint weight gives

    ||h||_b^2 >= L^6(A0+A1)V>0.

For the correction use A0<=A0+A1 and the right endpoint weight to get

    ||hhat-h||_b^2 <= L^6(A0+A1)U.

Dividing proves(1). No angular cutoff enters this estimate.

The broken space on the common subdivision is a Hilbert direct sum of weighted H1 spaces on open annuli. It satisfies the triangle inequality. Both repaired functions are continuous, so their norms and the norm of their difference agree with X. The triangle and reverse triangle inequalities give

    ||hhat-h0||_X <= ||hhat-h||_b+||h0-h||_b
                       < (delta2+delta0)||h||_b,
    ||h0||_X >= ||h||_b-||h0-h||_b > (1-delta0)||h||_b>0.

The resulting strict ratio bound is(2).

## Verification plan and limits

Use exactly the frozen 90 and187 radial columns audited in topics130-135, with their rational binary64 interpretation. Check every original first-piece degree and distinct support start. Compute all endpoint jets and all polynomial integrals exactly. A first engine will solve the physical-width endpoint linear system and use Arb512 endpoint weights. A separate engine will decode binary64 bits, use the explicit width1 Hermite basis, integrate by independent double monomial sums, and use mpmath.iv with exp/log for endpoint weights. The engines must agree on every repaired coefficient and every rational integral, and both must verify strict outward ceilings before a numerical claim is made. Confirm the inherited source pins and actual model-review provenance separately.

All results concern a newly defined repaired trial family. Historical raw matrices, discarded directions, whitening, quadrature, operator rows, global bounds, inverse estimates, nonlinear closure and the IPM endpoints remain OPEN. The C2 repair does not authorize using an old floating spectrum as its spectrum, and it does not prove the fully smooth setting.
