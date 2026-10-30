# A weighted L2 correction already fixes the similarity exponent

Status: new T4 argument, OPEN pending an independent theory review. No numerical inputs or existence claim.

## Exact statement

Let 0<gamma<1. Let rho be a smooth real S1 density on R2, with its canonical divergence-free IPM velocity u=U[rho]. Assume that for r>=1

    |u(X)| <= C_u r^gamma,
    |grad rho(X)| <= C_rho r^(gamma-1),
    rho(r,theta)=r^gamma Theta(theta)+o(r^gamma)          (1)

uniformly in angle, where Theta is a nonzero smooth real angular function with S1 parity. The constants C_u and C_rho are finite; their values do not enter the conclusion.

Set w_a=(1+r^2)^(-a/2), with 0<=a<=1+gamma. Suppose h is a real S1 distribution, both h and its canonical velocity v=U[h] belong to L2(w_a^2 dX), and the density rho+h is a distributional stationary solution at some real exponent c'. The equation is understood in the locally integrable divergence form

    c' div(X(rho+h))-(2c'+1)(rho+h)
                   +div((u+v)(rho+h))=0.               (2)

The canonical velocity is linear on this class, and div v=0. Products in (2) are locally integrable by the stated assumptions.

Then necessarily

    c' gamma=1.                                        (3)

No derivative or pointwise asymptotic expansion of h is assumed. In particular, if the reference has leading exponent gamma=1/c, then every stationary solution in this weighted affine correction class has exponent c, even if the definition of that class does not explicitly pin c. This includes the whole coercive low-weight interval a<1+1/c considered in this campaign and its endpoint.

If additionally rho+h and u+v are C1 near zero and (rho+h)_y(0) is nonzero, the audited origin identity gives c'+c[rho+h]=1. If the reference already has c+c[rho]=1, conclusion (3) therefore also forces c[h]=0. This last statement uses the genuine canonical contact term in the strain and does not construct a trace on weighted L2 alone.

## Proof by tests escaping to infinity

Choose a nonnegative smooth chi supported inside 1<r<2, with chi not identically zero, and put psi(Y)=chi(|Y|)Theta(arg Y). This is smooth and compactly supported away from zero. Then

    J=int |Y|^gamma Theta(arg Y) psi(Y) dY > 0.         (4)

For R>=1 define

    phi_R(X)=R^(-gamma-2) psi(X/R),
    A_R={R<|X|<2R},
    m_R=||w_a h||_(L2(A_R)), n_R=||w_a v||_(L2(A_R)).

Since the two global weighted norms are finite, m_R and n_R tend to zero as R tends to infinity. On A_R,

    w_a^(-1)<=5^(a/2)R^a.                              (5)

Test (2) with phi_R. Separate its six contributions: the linear background term, the background transport term u.grad rho, linear transport of h, u transport of h, v.grad rho, and the quadratic div(vh).

The linear background contribution converges to (c'gamma-1)J. To see this without assuming a differentiated remainder in (1), integrate by parts first and change variables X=RY. The factor R^(-gamma)rho(RY) converges uniformly on the fixed annulus to |Y|^gamma Theta. Dominated convergence leaves the distributional pairing of c'Y.grad-1 with this homogeneous function, which is (c'gamma-1)J by ordinary differentiation away from zero.

Every other contribution vanishes. The following explicit bounds establish that assertion; all norms of psi are on R2:

    |int (u.grad rho) phi_R|
        <=2^gamma C_u C_rho R^(gamma-1)||psi||1,

    |int h [(2c'+1)phi_R+c'X.grad phi_R]|
        <=5^(a/2)R^(a-gamma-1)m_R
             (|2c'+1| ||psi||2+|c'| ||Y.grad psi||2),

    |int h u.grad phi_R|
        <=2^gamma C_u 5^(a/2)R^(a-2)m_R||grad psi||2,

    |int phi_R v.grad rho|
        <=C_rho 5^(a/2)R^(a-2)n_R||psi||2,

    |int h v.grad phi_R|
        <=5^a R^(2a-gamma-3)m_R n_R||grad psi||infinity. (6)

The first bound uses (1), the support annulus and a change of variables. The next three are weighted Cauchy-Schwarz and (5). The last is weighted Holder for the locally integrable product hv and the supremum of grad phi_R/w_a^2. Each follows directly from the displayed scalings; no integration by parts involving a derivative of h or v is needed.

Since a<=1+gamma and gamma<1, the exponents a-gamma-1, a-2, and 2a-gamma-3 are respectively at most 0, gamma-1, and gamma-1. Thus (6) tends to zero, including at the endpoint a=1+gamma. Taking the limit in (2) yields (c'gamma-1)J=0. Equation (4) proves (3).

## Scope and sharpness of the correction-weight threshold

The upper threshold a=1+gamma is sharp for this assertion on the stated affine class. If a>1+gamma, then (1) puts rho and u themselves in L2(w_a^2 dX). Taking h=-rho gives the zero stationary density at every c', and v=-u also belongs to that weighted class. Hence the leading profile can then be removed by an admissible correction. This is a sharpness example for the integrability assertion; it does not claim the existence of a nonzero nearby profile with a different exponent.

The result does not prohibit changing the reference tail exponent or leading angular data in a separate numerical chart. Such a change can move the reference outside the original affine correction class. It also does not quantify the distance to solutions in another tail chart. In the campaign's fixed reference chart, however, allowing a free exponent cannot evade a necessary weak L2 correction-distance bound.

Dependencies: the canonical linear divergence-free velocity, elementary weighted Holder estimates, uniform leading-tail convergence, and the audited origin identity for the optional C1 consequence. No spectral, inverse or compactness theorem is invoked.
