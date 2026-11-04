# The angular trace and a local pure-rotation tail

Status: independent audit of coordinator CO48 and its focused comparison of LIT198-LIT199. These are a local identity and a local countermodel to an overbroad tail-only exclusion. They do not construct a global Euler profile.

## 1. Hypotheses and the trace identity

Let 2/5<c<1/2, omega be any finite real number, A=cI-omega J with Jx=(-x2,x1,0), X(x)=Ax, a=1-2c, and p=(1-c)/c. On an open twisted cone in D=R3 minus {0}, let V be C^(1,alpha), 0<alpha<1, divergence free, with the degree -p twisted homogeneity and k=X.V=0. Let W=curl V, and assume the tail identity grad k=X cross W-aV. On the corresponding sphere patch define

    Y(w)=V(w)-(w.V(w))w,
    f(w)=w.W(w)/c,
    Z(w)=W(w)-f(w)Aw,
    R_w h=w cross h, h in T_w S2.

If V(w0)=0 and W(w0)=lambda Aw0!=0, then Z is C^(1,alpha) near w0 and

    tr D_S Z(w0)=a lambda.                              (1)

To prove this, k=0 gives aV=X cross W=X cross Z. Since Jw and Z are tangent to S2, their cross product is normal. Tangent projection therefore yields aY=cR_w Z, or

    Z=-(a/c)R_w Y.                                      (2)

The right side is C^(1,alpha), although W itself is only C^alpha. At a zero of Y the derivative of R_w multiplies zero, so D_S Z=-(a/c)R_w D_S Y. In an oriented orthonormal tangent frame, tr(RN)=-(N21-N12). The surface curl of the tangential projection of V is w.curl V. This can be checked at the point in normal coordinates: derivatives of the tangent frame only contribute terms involving V, which vanish here. Hence

    tr D_S Z=(a/c)curl_S Y=(a/c)w0.W(w0)=a lambda.

For an actual tail the quotient transfer A1019 gives spectrum {-lambda rho,lambda(a+rho)}, whose sum is also a lambda. This independent local calculation verifies its scalar normalization. It does not alone determine the determinant or exclude a zero.

## 2. A smooth local example at omega=0

Set omega=0. Use cylindrical coordinates (r,phi,z), restrict to z>0, and put m=2p+2 in (4,5). Define

    F(r,z)=sum_(n>=0) b_n r^(2n) z^(-m-2n),
    b_0=1,
    b_n=-(m+2n-2)(m+2n-1)b_(n-1)/(4n(n+1)).              (3)

The ratio of successive coefficient magnitudes tends to 1. The series and all of its derivatives converge uniformly on smaller cones r<=theta z, z bounded above and away from zero, whenever theta<1. Its use of r^2 makes it smooth through the axis. Termwise differentiation gives

    F_rr+(3/r)F_r+F_zz=0, F(0,z)=z^-m.                  (4)

Indeed the coefficient of r^(2n-2)z^(-m-2n) is 4n(n+1)b_n+(m+2n-2)(m+2n-1)b_(n-1), which is zero by (3). By continuity of F(r,z)=z^-m F(r/z,1), F is positive on a sufficiently narrow cone around the positive axis.

On that cone set

    h=r sqrt F, V=h e_phi=sqrt F(-x2,x1,0),
    P_loc=|V|^2/2, S=P_loc-|V|^2/2=0.

These fields are smooth, including through the positive axis. V has homogeneous degree 1-m/2=-p, is divergence free, has V.curl V=0, and is tangent to spheres. Thus k=cx.V=0. For an axisymmetric azimuthal field,

    W=-h_z e_r+(h_r+h/r)e_z,
    tr((DV)^2)=-2hh_r/r.

The second identity follows from div((V.grad)V)=tr((DV)^2) and (V.grad)V=-(h^2/r)e_r. Euler homogeneity r h_r+z h_z=-p h gives

    X cross W=-c(rh_r+h+zh_z)e_phi=c(p-1)V=aV.

So the gradient-k identity also holds. Finally, direct differentiation gives

    Delta(r^2F/2)-2hh_r/r
       =(r^2/2)(F_rr+(3/r)F_r+F_zz)=0.

Hence -Delta P_loc=tr((DV)^2). The equations W.grad S=0 and grad k cross grad S=0 hold because S=0. This verifies the displayed local tail equations, including their differential constraint, not merely the sign of a jet.

On the axis,

    V=0, DV=z^(-p-1)J, W=2z^(-p-1)e3.

At w0=e3 on the unit sphere, lambda=2/c and D_S Y=R_w0. This is a nondegenerate index +1 pure-rotation zero. Equation (2) gives D_S Z=(a/c)I, consistent with (1). The example shows why the original-profile endpoint and equilibrium restriction in A1018-A1021 are essential. It is not a global smooth decaying profile, and its P_loc has not been identified with a globally canonical pressure.

## 3. Why this ansatz cannot extend globally

Suppose this same smooth azimuthal form were defined on R3 minus {0}, with a nonnegative nonzero F solving (4), and extended smoothly across the axis away from the origin. Regarding r as the radial variable in R4 makes F a nonnegative harmonic function on R5 minus {0}, homogeneous of degree -m. Write F(R theta)=R^-m g(theta) on S4. The polar-coordinate Laplacian gives

    Delta_S4 g+m(m-3)g=0.

Integrating over S4 gives m(m-3) integral g=0. Since m>4 and g is nonnegative, g=0, a contradiction. Smoothness across the axis is part of this extension statement; it is satisfied by the local even series. This argument rules out this globally nonnegative harmonic ansatz, not every global zero-k tail or every profile with flat zeros.

## 4. Source comparison and verification scope

The entire five-section coordinator source in the team records was read. Its Sections 2-3 explicitly reconstruct the local LIT198 jet argument and the LIT199 actual endpoint and C1 quotient transfer. Every step agrees with A1012-A1015 and A1018-A1021. The source carefully obtains C1 flow-box coefficients from a smooth initial disk, and differentiates C1 pushforwards only where the fields vanish. Its trace and series claims have been rederived above.

This is a received focused comparison through an existing agent configured as the primary model. The coordinator also cites an answer of the external referee (a second model) whose attempted second-model consultation did not run. These are distinct provenance claims: the recorded coordinator hand-check is available; that failed nested consultation is not counted as an additional model review. Provider runtime is not independently attested. This source predates A1022 and does not supply a focused check of the new exact-rate refinement or a new check of the full A963 stable-contraction proof.

No numerical computation is needed. The theoretical test was to verify the local trace, convergence and differential identities, plus the precise local/global distinction. The entire proof and source were postread; source bytes and hashes are retained. No formal build was attempted.
