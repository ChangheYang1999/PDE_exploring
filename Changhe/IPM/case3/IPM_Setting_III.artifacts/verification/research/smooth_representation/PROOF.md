# A smooth coefficient representation with a natural far-field coordinate

Status: representation and center functional derived independently. The representation is not asserted to contain an exact solution at any finite dimension.

## Definition

Fix 0<p<1, L>0, a=(1-p)/2, radial degree N and angular count M. Put

    w=(1+r^2/L^2)^(-a), sigma=r^2/(L^2+r^2), t=1-2w,
    rho=y w sum_{k=0}^{M-1} sigma^k B_k(t) cos(2k theta),
    B_k(t)=sum_{j=0}^N z_{kj} T_j(t).

The unknowns z are polynomial coefficients, not values of B_k at near-origin fitting nodes. All operations defining the canonical inverse are independent of the numerics lane.

## Smoothness and growth

For k>=0,

    sigma^k cos(2k theta)=Re((x+i y)^(2k))/(L^2+r^2)^k.

This is smooth on the whole plane. The functions w and t are smooth functions of x^2+y^2 at every finite point. Hence every finite coefficient array gives a C-infinity density, even in x and odd in y. No x^2 factor is imposed. The center slope is a0=B_0(-1), which is free.

At infinity w= L^(1-p)r^(p-1)(1+O(r^-2)), 1-t=2w, and sigma=1+O(r^-2). Expanding the polynomials B_k at t=1 gives

    rho=r^p Theta_0+r^(2p-1)Theta_1+o(r^(2p-1)),
    Theta_0=L^(1-p) sin(theta) sum_k B_k(1)cos(2k theta),
    Theta_1=-2 L^(2(1-p))sin(theta)sum_k B_k'(1)cos(2k theta).

The terms from sigma and the correction to w occur at degree p-2<2p-1 and therefore do not affect Theta_1. This encodes the powers of the first expected nonlinear correction, but does not impose the PDE's angular compatibility relation. That relation must be checked after solving. The density and its first derivative obey the required p-growth bound. Its canonical velocity is defined by the full-plane inverse, with no harmonic strain parameter.

## Explicit center strain and reporting constraint

The strain is c=-a0/4+integral rho_3(r)r^-2 dr. Only B_1 and B_2 enter rho_3, since multiplication by sin(theta) sends cos(2k theta) to adjacent odd sine modes. Thus

    c=-B_0(-1)/4+(1/2) integral_0^infinity (w/r)[sigma B_1(t)-sigma^2 B_2(t)]dr.

An absent angular coefficient is interpreted as zero. Substitute u=w. Since sigma=1-u^(1/a) and dr/r=-du/[2a u sigma],

    c=-B_0(-1)/4+(1/(4a)) integral_0^1
         [B_1(1-2u)-(1-u^(1/a))B_2(1-2u)]du.

This is an explicitly known linear functional of the unknown coefficients, independent of L. The y-axis far-field amplitude is

    K=L^(1-p) sum_k (-1)^k B_k(1).

At a fixed c_l=1/p, both c=1-c_l and K=a0 are linear constraints on the coefficients. The latter is the primary reporting slice L_axis=1, provided K/a0>0 and a0 is nonzero. At any exact primary profile in this slice, its derivative along the scaling orbit is (1-p)K, which is nonzero. Fixing c_l in a numerical experiment labels a separately tested parameter value; it is not a normalization of c_l and does not prove coverage of other values.

## Scope

The representation is finite in angular modes, so the restricted theorem in ../finite_angular/PROOF.md excludes any nonzero exact profile at a fixed finite M. It may still approximate an infinite-mode profile. Solver residuals, limiting regularity, convergence, nontriviality, and the far-field compatibility all remain independent requirements. Smoothness by formula alone does not establish existence or a uniform global residual bound.

## Cubic and nonlocal quartic coefficient functionals

Put D_k=B_k(-1), E_k=B_k'(-1). The exact degree-three density coefficients are

    b=[a(-D_0+2E_0)+D_1]/L^2,
    e=[a(-D_0+2E_0)-D_1]/L^2.

This follows by w=1-a r^2/L^2+O(r^4), t=-1+2a r^2/L^2+O(r^4), sigma=r^2/L^2+O(r^4). Only k=0,1 contribute. The canonical quartic stream difference H=q1-q2 is

    H=-D_1/(4L^2)+(1/(a L^2)) integral_0^1 u^(1/a)
             [B_2(1-2u)-(1-u^(1/a))B_3(1-2u)] du.

Missing angular coefficients are zero. To derive this without differentiating a density table, write the sin(3 theta) center coefficient beta3=(b-e)/4=D_1/(2L^2), and integrate the sin(4 theta) Poisson source once by parts:

    H=-beta3/2+4 integral_0^infinity b5(r) r^(-4) dr,
    b5=(r w/2)[sigma^2 B_2-sigma^3 B_3].

Both endpoints converge because the basis is smooth at zero and sublinear at infinity. Substitution u=w gives the displayed functional. Consequently T1=(a0-2A)b-6e and T2=(a0-4A)b-3a0 H are explicit quadratic coefficient tests. These formulas do not force T1 or T2 for arbitrary coefficients; they provide independent conditions for a solver and audit.
