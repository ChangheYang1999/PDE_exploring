# The nodal curl obstruction survives an angular metric factor

Status: CONFIRMED as A488 at the exact prescribed-metric and prescribed-vorticity scope below, 2026-11-03T05:32:48.087030+00:00. Full postwrite reading and the coordinator-supplied focused review are complete. General Euler periodic orbits are not reduced to this ansatz.

## 1. Exact local theorem

Use coordinates(theta,h,z), oriented volume r(h) dtheta dh dz, and metric

    ds^2=r(h)^2 dtheta^2+dh^2+dz^2,

where r is a positive C2 function on an open interval I. Vector components are contravariant coordinate components. Let w be C2 on a planar neighborhood of theta=b(h), where b is C2. Assume

    w(b(h),h)=w_theta(b(h),h)=0,
    w(theta,h)>0 for 0<theta-b(h)<epsilon.

Set W=w partial_theta-z w_theta partial_z. Suppose a C2 vector field V is defined near this whole zero curve at z=0 and satisfies, in the specified metric and orientation,

    curl V=W, div V=0, <V,W>=0.                       (1)

Then on a smaller positive strip there is a continuous ell(h) with

    r w_h+2r' w=ell(h)w^3,                            (2)

and b is locally constant. Thus a moving zero barrier cannot occur. No finite vanishing order is needed.

More strongly, if the scalar transport equation

    nu(h)w_theta+f(h)w_h=g(h)w                        (3)

holds with continuous real coefficients and nu(h) never zero, then no V satisfying (1) exists near the barrier at all. The coefficients may be arbitrary finite functions on a small compact h interval. For w=h^p F(theta+beta log h), beta!=0 and F nonnegative C2 with a zero adjacent to a positive interval, equation (3) holds with nu=beta, f=-h, g=-p. Hence all such angular nodal patterns are excluded for every real p.

The metric with r=1 is the product model. The metric with r=R+h, R>0, is a genuine Euclidean cylindrical annulus on any interval where R+h>0, with a choice of orientation. Thus this theorem does include that precise cylindrical geometry. It does not allow arbitrary theta,z dependent metric terms or extra components of W.

## 2. Curl, divergence and the C2 characteristic reduction

Write v=V^z and write V^theta,V^h for the other coordinate components. The metric dual of V is r^2 V^theta dtheta+V^h dh+v dz. The component curl equations in (1), obtained from d(V-flat)=i_(curl V)vol for this metric dual and the stated oriented volume, are

    partial_h v-partial_z V^h=r w,
    partial_z(r^2 V^theta)-partial_theta v=0,
    partial_theta V^h-partial_h(r^2 V^theta)=-r z w_theta.

The divergence equation is

    partial_theta(r V^theta)+partial_h(r V^h)
                                      +partial_z(r v)=0.

Helicity gives r^2 V^theta w=z w_theta v. On the positive strip, substitution into the second curl equation gives

    partial_theta v=(w_theta/w)(v+z partial_z v).      (4)

For fixed h the characteristics preserve I0=z w, and v/w is constant. Choose a reference section theta=b(h)+epsilon0 in the positive strip. The reference values of v/w with z=I0/w_ref define one C2 function R(h,I0) near I0=0. For each interior phase the segment to the reference has a positive minimum of w, so sufficiently small z characteristics stay in the domain. This yields

    v(theta,h,z)=w(theta,h)R(h,z w(theta,h))

near z=0 at every interior point. No uniform z width at the barrier is needed. Since b,w,v are C2, the reference formula is C2. With k(h)=R(h,0) and ell(h)=R_II(h,0),

    v(theta,h,0)=k(h)w(theta,h),
    v_zz(theta,h,0)=ell(h)w(theta,h)^3,                (5)

where k is C2 and ell continuous.

Differentiate divergence once in z and substitute the first two curl equations. This uses only second derivatives of V and gives

    v_hh+(r'/r)v_h+r^(-2)v_thetatheta+v_zz
                                      =r w_h+2r'w.   (6)

It avoids any assumption about a flat metric or a vector Laplacian in arbitrary coordinates. Applying (5) to (6), and writing

    L0=partial_hh+(r'/r)partial_h+r^(-2)partial_thetatheta,

gives the exact necessary equation

    k L0 w+(2k'-r)w_h+(k''+(r'/r)k'-2r')w
                                             +ell w^3=0.   (7)

## 3. A uniformly elliptic boundary argument forces k=0

Suppose k(h0)!=0. Shrink the h interval so |k| is bounded below and r is bounded above and away from zero. Divide (7) by k. It has the form

    Lw=r^(-2)w_thetatheta+w_hh+d(h)w_h+e(theta,h)w=0,

with bounded continuous lower coefficients. The boundary identities give w_h+b'w_theta=0 and therefore Dw=0 along theta=b(h).

The positive side of the C2 graph has an interior tangent disk at the chosen boundary point, of sufficiently small radius R0. Let x0 be its center. Its closure lies in the positive side except for tangency, and w>0 in its interior. Replace e by e_-=min(e,0), defining L_-. Since w is positive, L_-w<=0.

On the annulus R0/2<|x-x0|<R0 put

    phi=exp(-alpha|x-x0|^2)-exp(-alpha R0^2)>0.

Let lambda0>0 be a lower bound for both principal coefficients r^(-2),1; let T0 be an upper bound for their sum; let D0 bound |d| and E0 bound |e_-|. Direct differentiation gives

    L_-phi>=exp(-alpha|x-x0|^2)
            [alpha^2 lambda0 R0^2-2alpha T0
                                      -2alpha D0 R0-E0]>0

for sufficiently large alpha. Choose delta>0 so w>=delta phi on the inner circle; on the outer circle phi=0 and w>=0. Then f0=w-delta phi is nonnegative on the annular boundary and L_-f0<0 inside. A negative interior minimum would have zero gradient, nonnegative Hessian and e_-f0>=0, contradicting that strict inequality. Hence w>=delta phi throughout the annulus.

At tangency, the inward derivative of phi is 2alpha R0 exp(-alpha R0^2)>0. Thus w has strictly positive inward derivative, contradicting Dw=0 there. This proves k(h0)=0. Since h0 is arbitrary, k is identically zero and (7) reduces to (2). This explicit proof needs no derivative of the principal coefficients and includes infinitely flat zeros.

## 4. The barrier and transport consequences

By (2), on a fixed vertical line inside the positive strip,

    w_h=-2(r'/r)w+(ell/r)w^3.                         (8)

The coefficients are continuous and bounded locally; the right side is locally Lipschitz in w. If b'(h0)>0, the line theta=b(h0) lies inside the positive strip for h<h0 close enough, while w reaches zero at h0. A nonzero solution of (8) cannot reach zero in finite h: its logarithmic derivative is bounded while w stays bounded, or one may use uniqueness against the zero solution. The case b'(h0)<0 uses reverse h time. Thus b'=0 everywhere locally.

If (3) holds, substitute (8). At each fixed h,

    w_theta=[g+2f r'/r]w/nu-f ell w^3/(nu r).

This is an autonomous polynomial ODE in w, with locally Lipschitz right side. It cannot have a positive solution reaching zero at the finite endpoint theta=b(h). This proves the stronger nonreconstruction statement even before using b'=0.

For a nonnegative nonzero periodic F having a zero, choose a component of {F>0}. Its finite endpoint has F=F'=0 and supplies a smooth barrier theta=alpha-beta log h. The preceding argument applies for every h0>0 where r>0. Changing the sign of both w and V covers a negative one-sided interval as well. A left-side positive interval is covered by the reflected tangent disk.

## 5. Scope and verification requirements

This theorem controls a genuine change from the product model: an h dependent angular metric, including a Euclidean cylindrical annulus. It still prescribes W^h=0 and W^z=-z partial_theta W^theta exactly, with no nonlinear z dependence. A general adapted tube can have mixed metric coefficients, angular dependence and further terms in W. Neither A474 nor the global helicity identity has been shown to reduce an arbitrary flat periodic orbit to these hypotheses.

No pressure, velocity decay, carrier completeness or Euler momentum equation is assumed or inferred. No periodic witness of A471 is excluded in general. The entire proof is given above and uses no computation. The principal review points are the metric component factors in (6), C2 regularity of the characteristic reference, and the variable-coefficient barrier estimate. The focused coordinator review has been read in full and independently checked.

## 6. Sharpness of the nonzero angular transport hypothesis

For beta=0 let w=h^p F(theta) on h>0 and choose a positive C2 metric factor r with r(h)^2 h^p constant. The C2 field

    V0=-r z w partial_h

satisfies all three reconstruction equations for every C2 F, including one-sided infinitely flat nodes. Indeed its metric dual is -r z w dh; its exterior derivative has components partial_z(V0^h)=-r w and partial_theta(V0^h)=-r z w_theta, exactly the first and third curl equations of Section2, while the second is zero. Its divergence is -(z/r)partial_h(r^2 w)=0, and its inner product with W is zero because W^h=0. Thus one cannot omit the nonzero angular coefficient in the transport conclusion.

This theorem gives no whole-collar exclusion for a general r when the angular shape has no one-sided degenerate zero. For r=R+h those other shapes require the separate cylindrical analyses. It also does not control mixed metric terms or general adapted Euler tubes.

## Final audit record

A488, 2026-11-03T05:32:48.087030+00:00: all displayed mathematical arguments were independently reconstructed and the edited proof was read in full. The coordinator-supplied 212-line review was read in full and its findings independently checked. The coordinator is configured for the primary model; the review identifies a coordinator subagent without independent runtime model attestation. No new model client or remote computation was used. Earlier snapshots and metadata remain in verification; the current reconstruction record states the exact current scope.
