# Similarity equations and residual identities

Status: proved informal identities under the hypotheses below. These identities do not establish existence of a nonzero profile. Dependencies: elementary differentiation, change of variables, and the vector product rule. Numerical verification is separate. No formal verification is claimed.

Let c>0, tau=T-t>0, and x_* lie on the fixed z-axis. Assume U is C^3 and P is C^2 on the region under discussion. Write J_ij=partial_j U_i, H_ijk=partial_j partial_k U_i, delta=div U, and Omega=curl U. The matrix convention is output component first and coordinate index second.

## Stationary velocity and vorticity equations

Set y=(x-x_*)tau^{-c}, u=tau^{c-1}U(y), and p=tau^{2c-2}P(y). At fixed x, partial_t tau=-1 and partial_t y=c y/tau. Consequently

    partial_t u = tau^{c-2}[(1-c)U+c(y.grad)U],
    (u.grad_x)u = tau^{c-2}(U.grad)U,
    grad_x p = tau^{c-2}grad P,
    div_x u = tau^{-1}div U.

Dividing Euler's momentum equation by tau^{c-2} gives

    R_m = (1-c)U+(cy+U).grad U+grad P=0,  delta=0.

The curl gains one spatial factor tau^{-c}, so omega=tau^{-1}Omega. With y=(x-z_c(t)e_z)tau^{-c}, the additional term in partial_t y is -z_c'(t)tau^{-c}e_z. The choice z_c'=-C tau^{c-1} gives the additional term C partial_z U after the same factorization. Integrating with limiting center z_* gives z_c=z_*+(C/c)tau^c. Define Y=y+(C/c)e_z and U_hat(Y)=U(Y-(C/c)e_z). Then cy+Ce_z=cY, which removes C without adding a physical force.

For any smooth U, not necessarily divergence free,

    curl[(y.grad)U] = Omega+(y.grad)Omega,
    curl[(U.grad)U] = (U.grad)Omega-(Omega.grad)U+delta Omega.

The first identity follows by differentiating y_j partial_j U_i; the derivative of y contributes one curl. For the second, use (U.grad)U=grad(|U|^2/2)-U cross Omega and div Omega=0 in the curl product rule. Hence with V=cy+Ce_z+U,

    curl R_m = R_omega+delta Omega,
    R_omega = Omega+(V.grad)Omega-J Omega.

Only when delta=0 is curl R_m=R_omega. This correction is necessary when auditing direct velocity networks.

Taking the divergence and applying the product rule gives

    div[(cy+Ce_z+U).grad U]
        = c delta+V.grad delta+sum_ij(partial_i U_j)(partial_j U_i).

Thus, defining the prompt's pressure residual,

    R_P = -Delta P-tr(J^2),
    div R_m = delta+V.grad delta-R_P.

This identity is valid even for nonzero delta. A small momentum residual at isolated points does not control its derivatives and therefore does not imply small R_omega or R_P. Local pressure Poisson consistency also leaves harmonic pressure additions undetermined; a whole-space check needs tail information.

## Cylindrical components

At r>0 write e_r=(cos theta,sin theta,0), e_theta=(-sin theta,cos theta,0), and U=U^r e_r+U^theta e_theta+U^z e_z. Along V the scalar derivative is

    D=(cr+U^r)partial_r+(U^theta/r)partial_theta+(cz+C+U^z)partial_z.

Since partial_theta e_r=e_theta and partial_theta e_theta=-e_r,

    (V.grad)U = [DU^r-(U^theta)^2/r]e_r
               +[DU^theta+U^r U^theta/r]e_theta+(DU^z)e_z.

Adding (1-c)U and grad P gives the three cylindrical momentum equations in PROMPT.md. Divergence is partial_r U^r+U^r/r+partial_theta U^theta/r+partial_z U^z. The volume element is r dr dtheta dz. These identities are asserted only for r>0; Cartesian derivatives define the axis limits without an arbitrary radius cutoff.

## Rotation, axis smoothness, and gauges

Let Q=diag(-1,-1,1). Q is a proper rotation. For a smooth vector field F define S F(y)=[F(y)+Q F(Qy)]/2; for a scalar p define S p(y)=[p(y)+p(Qy)]/2. Substituting Qy and using Q^2=I proves equivariance of S F and invariance of S p. The proper-rotation transformation of curl is curl[Q F(Qy)]=Q(curl F)(Qy), as follows from the Levi-Civita identity for an orthogonal matrix with determinant one. Thus S commutes with curl, and U=curl S A is exactly divergence free and Q-equivariant as an analytic representation.

For a smooth Q-equivariant field, at each fixed z the horizontal components are odd in the pair (x,y) and the vertical component is even. Taylor expansion in that pair gives

    U_1=a(z)x+b(z)y+O(r^3),
    U_2=c_0(z)x+d_0(z)y+O(r^3),
    U_3=w(z)+O(r^2).

Divergence on the axis is a+d_0+w'=0. Smoothness does not constrain the 2 by 2 transverse matrix to a dilation plus rotation. To see the Fourier restrictions, note U_x+iU_y=e^{i theta}(U^r+iU^theta) and U_x-iU_y=e^{-i theta}(U^r-iU^theta). A smooth scalar angular mode k vanishes to order at least |k| at the axis, by its Cartesian Taylor expansion. The cylindrical n modes therefore satisfy the orders |n+1|, |n-1|, and |n| for the two combinations and for U^z or P, respectively. They also obey the coupled Taylor compatibility conditions; vanishing orders alone are only necessary conditions. In particular cylindrical n=2 horizontal content may occur at order r.

For a>0 let U_a(y)=aU(y/a), P_a(y)=a^2P(y/a), C_a=aC. Direct substitution gives R_m[U_a,P_a,C_a](y)=a R_m[U,P,C](y/a) and div U_a(y)=div U(y/a). Also grad U_a(y)=grad U(y/a) and Omega_a(y)=Omega(y/a). Thus a changes spatial scale and velocity amplitude together, but not the vorticity supremum. A pressure additive constant is a distinct gauge. Axial translation is represented by C as above. Rotation about the z-axis can fix a phase when a nonzero angular coefficient is present. No arbitrary extra derivative or amplitude constraints follow from these symmetries.

The correct axisymmetric projection is the vector group average of R_{-alpha}U(R_alpha y). Averaging Cartesian components without rotating them back does not implement this projection. Equivariance under Q alone means cylindrical pi-periodicity and permits every even angular mode, including a free mean. Quadratic advection generally generates n=4 from n=2, so an n=0,2 truncation is not closed.

## Energy, matching powers, and coordinate maps

For an exact ansatz, changing variables on the shrinking physical ball gives

    integral_{|x-x_*|<R tau^c}|u|^2 dx
       = tau^{5c-2} integral_{|y|<R}|U|^2 dy.

If physical kinetic energy is uniformly bounded and the rescaled velocity converges strongly in local L^2 to a profile with positive mass on some fixed ball, the right-hand side cannot diverge. Hence c>=2/5 under these hypotheses. This argument does not require U in L^2 of the whole space. It is not an application of the distinct vorticity-gradient theorem in R3.

For a homogeneous leading velocity of degree d, the linear similarity operator is multiplication by 1-c+cd. Its kernel has d=1-1/c. The convection of that velocity and the gradient of a degree-2d pressure both have degree 2d-1. A velocity correction of that degree has linear coefficient 1-c+c(2d-1)=-1. Such a correction can cancel a nonzero leading nonlinear defect. Requiring exact homogeneity outside a finite radius could rule out this necessary correction.

For U=R^d[A_r(n)n+A_T(n)] with n=y/R and tangential A_T, spherical divergence is R^{d-1}[(d+2)A_r+div_{S^2} A_T]. This follows by differentiating the radial flux R^{d+2}A_r and the tangential divergence. Its vanishing is the leading angular incompressibility condition. Neither this condition nor the leading exponents proves that the full tail solves Euler.

For independent Cartesian asinh coordinates q_i=asinh(y_i/L_i), set a_i=(L_i^2+y_i^2)^{-1/2}. Then partial_{y_i}=a_i partial_{q_i}, partial_{y_i}^2=a_i^2 partial_{q_i}^2-y_i(L_i^2+y_i^2)^{-3/2}partial_{q_i}, and mixed derivatives use a_i a_j when i differs from j. The physical Jacobian is product_i L_i cosh q_i. A computational MSE with uniform q sampling is not a physical-volume L^2 norm.

## Viscous scaling

For s=-log tau and u=tau^{c-1}v(y,s), partial_t s=1/tau. Dividing the Navier-Stokes momentum equation by tau^{c-2} gives the rescaled left side partial_s v+(1-c)v+(cy+v).grad v+grad P. The viscous side is nu tau^{1-2c}Delta v=nu exp[-(1-2c)s]Delta v. It decays for c<1/2 if curvature remains controlled. This scaling identity does not establish viscous blowup, stability, outer matching, or construction from one physical initial condition.
