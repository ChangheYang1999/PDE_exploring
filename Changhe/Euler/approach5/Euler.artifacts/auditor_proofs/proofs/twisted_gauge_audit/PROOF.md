# Exact radial twist and its limitations

## Hypotheses and conventions

Take c>0 and finite omega. Let beta in C1((0,infinity)), r=|y|, e=y/r and R_theta=exp(theta J). The radial twist T(y)=R_beta(r)y is a C1 diffeomorphism of punctured R3, preserving radius and Euclidean volume. If U,P are defined on D, their transformed fields are defined on T(D), not necessarily on the same open set:

    V(y)=R_beta(r) U(T^-1 y), Q(y)=P(T^-1 y).

For a Cartesian vector field define L V=(Jy dot grad)V-JV. This is differentiation of cylindrical components with respect to the azimuth, not the full Cartesian directional derivative. For scalars write R f=(Jy dot grad)f.

Define

    grad_beta Q=grad Q+beta'(r)*e*R Q,
    div_beta V=div V+beta'(r)*R(V dot e),
    curl_beta V=curl V+beta'(r)*e cross L V,
    (V dot grad_beta)V=(V dot grad)V+beta'(r)*(V dot e)*L V.

## 1. Exact equation and vorticity covariance

A Cartesian chain rule, including the derivative of the output rotation, gives the transformed derivative tensor

    R_beta (DU)(T^-1 y) R_-beta
       =DV+beta'(r)*(L V) tensor e.

Taking its trace and antisymmetric part proves

    (div U)(T^-1 y)=div_beta V,
    R_beta (curl U)(T^-1 y)=curl_beta V.

The rotation on the left of the curl identity is required for Cartesian vectors. Multiplying the derivative tensor by V gives the convective formula above. Scalar differentiation gives the pressure gradient formula. The transformed profile equation is exactly

    (1-c)V+c(y dot grad)V
       -(omega-c*r*beta'(r))*L V
       +(V dot grad_beta)V+grad_beta Q=0,
    div_beta V=0.

Thus C12's equation is correct with its cylindrical-component convention and transformed domain understood.

For beta=(omega/c)log(r), the explicit L V term disappears from the linear velocity transport operator (1-c)+c*y dot grad. It does not disappear from the full linear system. The constraint div_beta V is linear in V and still contains (omega/(c*r))*R(V dot e). The pressure operator is also linear in Q and retains omega. This distinction refutes the literal claim that the twist removes omega from every linear term. For an explicit test, V=(y1/r)*e has

    div_beta V=(2*y1/r-(omega/c)*y2/r)/r.

The omega term is nonzero and linear in V. No claim that this test is a profile is needed: it directly tests the asserted transformed operator.

The alternative beta=(omega/(2c))*log(1+r^2/R0^2) is smooth at zero and leaves the explicit transport coefficient omega/(1+r^2/R0^2). For the logarithmic gauge with omega!=0, continuity at zero requires and is implied by the horizontal component of U(0) vanishing; when omega=0 the gauge is the identity. The pushed-forward characteristic vector field is

    cy-(omega-c*r*beta')Jy+V+beta'*(V dot e)*Jy.

All these statements are coordinate identities. They do not prove that every possible nonexistence mechanism is confined to the core or is nonlinear.

## 2. Leading divergence-free tail space

Set alpha=(1-c)/c and k=omega/c. The kernel of the displayed velocity transport operator has V=r^(-alpha)F(n), n=y/r. Decompose F=F_r*n+F_tan. Its exact transformed divergence is zero if and only if

    (2-alpha+k*R)F_r+div_(S2) F_tan=0.

If c!=1/3, then 2-alpha!=0. On spherical harmonics Y_l^m, the scalar inverse multiplier is 1/(2-alpha+i*m*k), of magnitude at most 1/|2-alpha|. It therefore preserves every Sobolev space and smoothness. Every smooth tangential F_tan determines exactly one smooth F_r, and conversely every such divergence-free tail arises this way. This proves the precise tail-space bijection in C12(b), including omega=0. It does not say that arbitrary three-component F is allowed, or that any tail extends to a global nonlinear profile.

Smoothness on the spherical axis is just smoothness of F as a global vector field on S2: the twist is a smooth diffeomorphism away from the origin. No finite angular truncation is assumed.

## 3. Sphere integrals and the scalar Mellin symbol

If a continuous scalar q obeys q(R_theta y,R_theta u)=q(y,u), then on each sphere the change of variables y->R_-beta(r)y gives

    integral_(S_r) q(y,V(y)) dS=integral_(S_r) q(y,U(y)) dS.

The analogous statement for tangential derivative tensors requires the same equivariance in those arguments. Radial derivatives do see beta'. In particular this identity is not a license to ignore the twist in vorticity or helicity estimates.

For the scalar mode operator (1-c-i*m*omega)+c*r*partial_r, the Mellin symbol is

    sigma_m(lambda)=1-c+c*lambda-i*m*omega.

On Re(lambda)=-b,

    inf_(gamma real)|sigma_m(-b+i*gamma)|=c*|alpha-b|.

The minimizing gamma is m*omega/c. If b>alpha and |g(r)|<=A*r^(-b), the unique O(r^(-b)) solution of the inhomogeneous scalar equation is

    f(r)=-(1/c)*r^lambda_m integral_r^infinity g(t)t^(-lambda_m-1)dt,
    lambda_m=-alpha+i*m*omega/c,

and |f(r)|<=A*r^(-b)/(c*(b-alpha)). The integral estimate is absolutely convergent and direct. These verify C12(c,d). They concern the scalar transport symbol, not the complete pressure-divergence operator of the Euler system.

## 4. Conditional terminal profile

Suppose a genuine profile has the uniform velocity expansion, in the rotating cylindrical frame,

    U_cyl(r,phi,theta)=r^(-alpha)F(phi,theta+k*log(r))+o(r^(-alpha)),

with continuous globally compatible spherical vector data F. This is an explicit extra tail hypothesis. The generated physical velocity is

    u(x,t)=exp((1-c)*s)R_omega*s U(exp(c*s)R_-omega*s x),
    s=-log(T-t).

In cylindrical components its phase is theta-omega*s+k*(log|x|+c*s)=theta+k*log|x|, and its radial prefactor is |x|^(-alpha), because c*alpha=1-c. The error tends uniformly to zero on every compact set away from zero. Therefore u tends there to the twisted homogeneous field with these same F data. For omega!=0 it is discretely homogeneous with scale exp(2*pi*c/|omega|). This confirms C14. The velocity-only expansion does not, without more argument, supply a derivative expansion or integrability of helicity.

## Audit scope

The exact twist, tail-space parametrization, invariant sphere integrals, scalar Mellin estimates and conditional terminal limit are confirmed. The phrase that every linear term is omega-free is false, and the broader assertion that far-field methods cannot obstruct profiles remains open. No derivative or pressure asymptotic is silently added to a uniform velocity tail.
