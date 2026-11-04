# A nodal transport pattern cannot be reconstructed as incompressible helicity-free velocity

Status: CONFIRMED at the exact product-metric and prescribed-vorticity scopes, A741-A742. This does not exclude a general flat periodic Euler orbit.

## 1. Local theorem and scope

Use ordinary Euclidean coordinates (theta,h,z) on a box, with oriented volume dtheta dh dz and the product metric. Let I be an open interval, F,G smooth real functions on I, F>0, and set

    chi=theta+G(h), w(theta,h)=F(h)sin^2 chi,
    W=(w,0,-z w_theta).

Suppose an open neighborhood of the curve (theta,h,z)=(-G(h),h,0), h in I, carries a C2 field V with

    curl V=W, div V=0, V.W=0.                         (1)

Then F and G are locally constant on I, and hence constant on each connected interval. Conversely, if F and G are constant, V=(0,-z w,0) satisfies (1). The necessity is local on every smaller box around one point of the zero curve. A shifted zero chi=k pi gives the same statement.

In particular the LIT111 pattern

    F(h)=h^p, G(h)=(nu/sigma)log h, h>0,
    p>0, sigma>0, nu!=0

has no such C2 reconstruction near any zero barrier at positive h. The same is true when nu=0 and p>0. These coordinates have the Euclidean product metric. Applying a nonlinear change of coordinates to an actual orbit does not preserve this metric or the displayed curl and Laplace operators. No coordinate reduction for arbitrary Euler orbits is asserted.

## 2. Potential regularity and a common characteristic function

The explicit field V0=(0,-z w,0) satisfies

    curl V0=W, V0.W=0, div V0=-z w_h.

If V as in (1) existed, the local Poincare lemma on a smaller simply connected box gives V-V0=grad q. Since V-V0 is C2, this potential is C3: each first derivative equals a C2 component. The remaining equations are

    w q_theta-z w_theta q_z=0, Delta q=z w_h.         (2)

Fix a small phase epsilon>0 less than pi/4. After shrinking the h interval, the region 0<chi<=epsilon/2 and its reference section chi=epsilon/2 lie in the box. On this side w>0 and increases as chi increases. The W-characteristics keep h and I0=z w fixed. Starting from phase 0<chi<epsilon/2 and sufficiently small |z|, follow increasing theta until chi=epsilon/2. Along this segment |z| can only decrease. Thus the segment stays inside the box. Its travel time is finite for each starting phase strictly above zero, although it need not be uniform as chi tends to zero.

Let w_ref(h)=F(h)sin^2(epsilon/2)>0 and define

    Q(h,I0)=q(epsilon/2-G(h),h,I0/w_ref(h)).

On a fixed smaller h interval, this is C3 on a common neighborhood of I0=0. Integrating the first equation in (2) gives

    q(theta,h,z)=Q(h,z w(theta,h))                   (3)

throughout a one-sided neighborhood of the barrier with sufficiently small |z|. This is one common Q, not unrelated characteristic functions at different theta. The reference-section construction establishes exactly the common domain needed for its derivatives at I0=0.

Put k(h)=Q_I(h,0), ell(h)=Q_III(h,0). Then k is C2, ell is continuous, and

    q_z(theta,h,0)=k(h)w(theta,h),
    q_zzz(theta,h,0)=ell(h)w(theta,h)^3.

Differentiate the second equation in (2) once with respect to z, at z=0. All third derivatives exist and commute because q is C3. It follows that

    (k w)_hh+(k w)_thetatheta+ell w^3=w_h.            (4)

No fourth derivative of q or third derivative of V is used.

## 3. The zero barrier forces the correction to vanish

On chi=0, w=w_theta=w_h=0, whereas

    w_thetatheta=2F(h), w_hh=2F(h)(G'(h))^2.

Taking the limit from chi>0 in (4) is legitimate since k is C2 and ell continuous. The terms containing w or w_h vanish, leaving

    2 k(h) F(h)(1+(G'(h))^2)=0.

Therefore k(h)=0 for every h in the smaller interval. Its h derivatives then vanish as well, and (4) reduces on the whole chosen side to

    ell(h) w^3=w_h
      =F'(h)sin^2 chi+2F(h)G'(h)sin chi cos chi.      (5)

For a fixed h, divide (5) by chi and let chi decrease to zero. The left side is O(chi^5), the first right term tends to zero, and the second tends to 2F(h)G'(h). Hence G'(h)=0. With that conclusion, divide the same equality by chi^2 and let chi decrease to zero. The left side is O(chi^4), while the right side tends to F'(h). Thus F'(h)=0. This proves necessity. If both derivatives vanish identically, w_h=0, so V0 is already divergence free and proves the converse.

The obstruction concerns every C2 helicity-free curl potential, not just the particular one obtained from the carrier Lamb identity. It uses the actual curl and divergence equations. It needs no pressure, carrier relation, boundary term or complete flow.

## 4. The campaign transport model at its exact reduced scope

For 2/5<c<1/2 define

    a=1-2c, d=3c, kappa=1+c,
    sigma=2a, lambda=d+sigma, p=kappa/sigma>7/2.

On the flat product (R/(2pi Z)) times R times R, take nu!=0 and w=h^p sin^2(theta+(nu/sigma)log h) for h>0, extended by zero for h<=0. Define

    B=(nu,-sigma h,lambda z), W=(w,0,-z w_theta),
    H=h, g=sigma h/a.

All h derivatives through order3 of w and w_theta are finite sums of h^(p-j) times bounded trigonometric functions, j<=3; theta differentiation does not lower the power. Their limits at h=0 are zero, so W is C3. The identity

    nu w_theta-sigma h w_h=-kappa w

gives div B=d, div W=0 and [B,W]=-kappa W. The explicit complete carrier flow is (theta+nu t,h exp(-sigma t),z exp(lambda t)). The circle Gamma={h=z=0} has period2pi/|nu|, transverse forward exponents -sigma,lambda, and W=DW=0 there. Its largest backward exponent is sigma=2a.

The W flow preserves h. At fixed h>0, theta'=w is nonnegative and zero at each barrier chi=k pi. A nonstationary trajectory stays between consecutive barriers by uniqueness, so it cannot make a nonconstant periodic orbit. Its angular velocity and w_theta are bounded for that fixed h. The z equation z'=-w_theta z therefore exists for every finite positive or negative time. The W flow is complete. At h<=0 it is stationary.

The map (theta,h) -> (chi modulo2pi,log h) is a diffeomorphism of the positive-h cylinder. Thus {W!=0} has exactly two connected components, chi in(0,pi) and chi in(pi,2pi), each times all z. Both are carrier-invariant because chi is constant along B. Given any theta0 on Gamma and either phase interval, choose chi0 inside the interval and integers k_n such that

    log h_n=(sigma/nu)(chi0-theta0+2pi k_n) -> -infinity.

Then (theta0,h_n,0) belongs to that fixed component and tends to the chosen point of Gamma. The entire orbit lies in the closure of each component. This verifies fixed-component accumulation, not merely accumulation from a changing family of components.

## 5. Curl potential, Kelvin law and the missing Euler structure

The vector field

    Ustar=(B cross W-grad H)/a
      =(sigma h z w_theta,
        lambda z w+nu z w_theta-1,
        sigma h w)/a

is C3, satisfies Ustar.W=0 and Ustar.B=g, and obeys grad H=-a Ustar+B cross W by construction. Differentiating the transport identity gives sigma h w_h=kappa w+nu w_theta and sigma h w_thetah=kappa w_theta+nu w_thetatheta. Substitution in the three components of curl Ustar gives W exactly, using kappa-d=a.

Let alpha be the metric one-form of Ustar. Then d alpha=i_W vol, and

    L_B alpha=i_B d alpha+d g
              =-B cross W+d g
              =-a alpha+d(g-H).

Consequently every smooth closed loop advected by the complete carrier flow has circulation C(t)=exp(-at)C(0). This is the full Kelvin law in the reduced model. It is not limited to the central orbit.

On Gamma, Ustar=-e_h/a and DUstar=0, while grad H=e_h, grad g=(sigma/a)e_h, and both scalar Hessians vanish. Thus the flat covector and second-order rank identities hold there with rho=-sigma. The covector identity also follows directly from the diagonal derivative of the explicit flow.

Nevertheless

    div Ustar=(z/a)[sigma h w_thetatheta+lambda w_h+nu w_thetah].

At chi=pi/2 this is (z/a)h^(p-1)[lambda p-2nu^2/sigma-2sigma h^2], which is not identically zero. Also B is not the Euclidean similarity field Ay+Ustar. Sections1-3 show that even replacing Ustar by an arbitrary local helicity-free curl potential cannot fix incompressibility near a positive-h barrier. The model satisfies many transport, recurrence and on-orbit rank tests but not the full profile system.

## 6. Dependencies, audit interpretation and remaining question

The complete LIT111 submission is pinned in verification. The proof above independently checks its regularity, common-Q domain, C3 mixed derivatives, barrier limit, component topology, flow completeness, exact curl and Kelvin signs. Sections1-3 strengthen its barrier calculation to arbitrary smooth positive amplitude F and phase G with this sine-squared pattern. No computation is needed or used.

This is not a universal classification of nodal vorticity near a periodic Euler orbit. In particular curved coordinates introduce metric coefficients and may mix the three curl components. The unresolved problem is whether an analogous obstruction survives those coefficients and the actual relation B=Ay+U. No high-growth witness from A471 is excluded by the present product-pattern theorem.
