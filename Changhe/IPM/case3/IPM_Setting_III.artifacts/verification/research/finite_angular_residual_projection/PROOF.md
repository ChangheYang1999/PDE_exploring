# Exact angular projection of finite-mode transport residuals

Date: 2026-10-20. Status: analytic derivation complete, independent computational checks pending. Scope: identities for finite angular density representations at positive radius, using their canonical full-plane velocity. These identities alone prove neither a small uniform residual nor an exact nearby profile.

## 1. Statement, notation and angular convolution

Fix a positive radius r. Write a finite odd-sine density and even-mode polar velocity as

    rho(r,theta)=r sum_(k odd) g_k(r)sin(k theta),
    partial_r rho=sum_(k odd) e_k(r)sin(k theta),
    U_r/r=sum_(m positive even) u_m(r)cos(m theta),
    U_theta/r=sum_(m positive even) v_m(r)sin(m theta),
    e_k=g_k+r g_k'.

All coefficients outside their finite index ranges are zero. With ell=c_l, define R=(ell X+U).grad rho-rho and its finite expansion R/r=sum_(l odd) C_l(r)sin(l theta). The coefficient array is called residual_modes in the implementation.

Start with C_k=ell e_k-g_k. For each pair (k,m), set

    A_(k,m)=u_m e_k/2,  B_(k,m)=v_m k g_k/2.

Add A_(k,m)+B_(k,m) to C_(k+m), and add sign(k-m)(A_(k,m)-B_(k,m)) to C_|k-m|. These operations give every residual mode exactly. The difference index never vanishes because k is odd and m is even.

Indeed polar differentiation gives

    R/r=sum_k(ell e_k-g_k)sin(k theta)
         +sum_(k,m)[u_m e_k cos(m theta)sin(k theta)
                    +v_m k g_k sin(m theta)cos(k theta)].

The product-to-sum identities

    cos(m theta)sin(k theta)=[sin((k+m)theta)+sin((k-m)theta)]/2,
    sin(m theta)cos(k theta)=[sin((m+k)theta)+sin((m-k)theta)]/2

give the stated rule. Orthogonality then implies, for every odd l,

    int_0^(2pi) R sin(l theta)dtheta=pi r C_l,
    int_0^(2pi) R^2 dtheta=pi r^2 sum_l C_l^2.               (1)

In particular the complete first-moment family of result87 examines just C_1(r). Its explicit formula is

    C_1=ell e_1-g_1
          +(1/2)sum_(k odd)[(u_(k-1)-u_(k+1))e_k
                            +k(v_(k+1)-v_(k-1))g_k],         (2)

with u_0=v_0=0. For a radial quotient g_1=f, u_2=J, v_2=J-f/2, equation(2) reduces to result88:

    C_1=(ell-J/2)r f'+(ell-1)f-f^2/4.

The exact coefficient triangle inequality also gives sup_theta |R|<=r sum_l|C_l|. Floating-point evaluation of the right side is only an estimated envelope unless the coefficient errors are enclosed. The ratio sqrt(sum C_l^2/sum g_k^2), when the denominator is positive, is the angular L2 residual relative to density. It is an additional diagnostic and does not replace either pointwise denominator required by the task.

## 2. Density coefficients and radial derivatives for the Q representation

Use the compact coordinate s in(0,1), w=1-s,

    r=L 2^(-kappa) sqrt(s)w^(-kappa),
    r ds/dr=2sw/[w+2kappa s],
    rho/r=w sin(theta)sum_(j=0)^(M-1) s^j B_j(2s-1)cos(2j theta).

Here B_j is the original saved Chebyshev polynomial; missing polynomials vanish. Define

    D_0=B_0-s B_1/2,
    D_j=(B_j-s B_(j+1))/2 for j>=1.

Then g_(2j+1)=w s^j D_j. Differentiate the original polynomials at t=2s-1, including dt/ds=2. The exact radial coefficient is

    e_(2j+1)=g_(2j+1)+(r ds/dr)
       [-s^j D_j+w j s^(j-1)D_j+w s^j partial_s D_j],         (3)

where the term with j=0 in the middle is zero. The canonical inverse from result86 returns psi/r^2=sum p_j sin(2j theta) and (partial_r psi)/r=sum d_j sin(2j theta). Thus

    u_(2j)=-2j p_j,  v_(2j)=d_j.                            (4)

Every exterior radial contribution is contained in that inverse. No harmonic strain or artificial angular closure is introduced here.

## 3. Density coefficients and derivatives for the smooth radial representation

Put z=(r/L)^2, sigma=z/(1+z), w=(1+z)^(-alpha), t=1-2w. The saved density is

    rho/r=w sin(theta)sum_j sigma^j P_j(t)cos(2j theta),
    dot sigma=2sigma(1-sigma), dot w=-2alpha sigma w,
    dot t=4alpha sigma w,

where dot means r d/dr. Define D_j by the same formulas as Section2 with s replaced by sigma and B_j replaced by P_j(t). Then

    g_(2j+1)=w sigma^j D_j,
    e_(2j+1)=(1-2alpha sigma)g_(2j+1)
            +w[j sigma^(j-1)dot sigma D_j+sigma^j dot D_j].  (5)

Here dot P_j=P_j'(t)dot t, and dot D includes both the derivative of P and of its explicit sigma factor. If result84 returns the scaled source integrals I_j,E_j with psi_(2j)/r^2=(I_j+E_j)/(4j), then

    u_(2j)=-(I_j+E_j)/2,  v_(2j)=(-I_j+E_j)/2.              (6)

These expressions evaluate the same stored density with analytic radial differentiation and the independently implemented canonical inverse.

## 4. Verification design, scaling and limitations

The independent manufactured check will compare equations(3) and(5) to scalar multiprecision differentiation of density sine coefficients, compare the convolution to Cartesian residual values at independent angles, and recover projections by a high-order periodic trapezoidal rule. For a finite trigonometric polynomial that rule is exact in exact arithmetic once the node count exceeds twice the highest mode. Its floating-point realization is supporting evidence, not an interval enclosure. A rational radial specialization checks equation(2) separately.

A represented density with M sine modes produces velocity frequencies at most2M and residual frequencies at most4M-1. Thus the projection has finitely many entries even though its radial inverse remains over the full plane. The absence of angular quadrature error in the formula does not eliminate radial inverse evaluation error, basis error or nonlinear optimization error. Finite radial sampling still cannot certify a continuum of radii.

Under rho_lambda(X)=lambda rho(X/lambda), the arrays g,e,u,v and residual_modes at r are their original arrays at r/lambda. Hence the dimensionless angular L2 diagnostic is invariant after the same radius change. The physical projection pi r C_l and the absolute angular envelope scale by lambda. No invariant parameter ell or a0 is normalized by these diagnostics.

Dependencies: results84 and86 provide the two full-plane inverse implementations and their written derivations; result87 identifies the first sine projection with the complete Mellin family; result88 provides the radial specialization. All angular algebra and both density derivative formulas are proved above. Manufactured gates and candidate tables must be read separately from this analytic statement.
