# Independent smooth negative-slope trial family

Result255 methodology. Written 2026-10-21 before implementation. No numerical run or profile existence is asserted here. This is a finite search in a named subclass, using a separately implemented generator, derivatives and canonical inverse. The full-plane PDE is the target, not the auxiliary hydrostatic equation.

## Statement and scope

Fix c_l>1 and p=1/c_l. Let m=0,...,M-1, n=2m+1, j=0,...,J-1, and beta=(n-p)/2+j. For r>0 set

    f_nj(r)=r^n(1+r^2)^(-beta),
    rho(r,theta)=sum a_mj f_nj(r) sin(n theta).

Here a_mj are finite real coefficients. At the origin define rho by its smooth extension. Every field in this family is C-infinity on the plane, even in x and odd in y, with density and first derivative satisfying the prompt growth bound with gamma=p. The following formulas give its canonical full-plane stream function and velocity, with no freely optimized velocity or harmonic strain.

The search imposes the far-axis coefficient K=-1 and requires a0=rho_y(0)<0, while a0 remains a variable. It fixes c_l only as a search parameter, never as a normalization. Finite angular support excludes an exact solution by the already established finite-angular theorem; these finite fields are approximation trials. Only convergence with increasing radial and angular dimensions, independent residual checks, and all prompt safeguards could support a limiting candidate. A low residual alone is insufficient.

## Smoothness, symmetry and far field

The quantity r^n sin(n theta) is the imaginary part of (x+i y)^n, a homogeneous polynomial. Multiplication by the smooth positive function (1+x^2+y^2)^(-beta) preserves C-infinity. For odd n it is even in x and odd in y. At infinity

    f_nj(r)=r^(p-2j)(1+O(r^(-2))).

Differentiation gives symbol bounds of order p-2j. Thus the finite sum and its first derivative meet the prompt bound. The leading angular trace is

    Theta(theta)=sum_m a_m0 sin((2m+1)theta),
    K=Theta(pi/2)=sum_m (-1)^m a_m0.

The origin slope is a0=sum_j a_0j. Higher m vanish to order at least three at the origin. The construction permits both signs and sign changes of rho away from the origin. It does not assume a global monotonicity property.

## Canonical inverse for a single density mode

For rho=f(r) sin(n theta),

    rho_x=(f'-nf/r) sin((n+1)theta)/2
             +(f'+nf/r) sin((n-1)theta)/2.

The n-1 term is absent for n=1. For k>0 the full-plane inverse of the k-th sine source q is

    g_k(r)=[r^(-k) int_0^r s^(k+1)q(s) ds
                 +r^k int_r^infinity s^(1-k)q(s) ds]/(2k),

so -Delta[g_k sin(k theta)]=q sin(k theta). Integration by parts gives

    g_+(r)=-r^(-n-1) A(r)/2,
    A(r)=int_0^r s^(n+1)f(s) ds,

and, for n>=3,

    g_-(r)=r^(n-1) B(r)/2,
    B(r)=int_r^infinity s^(1-n)f(s) ds.

The endpoint terms used in these integrations vanish: f=O(r^n) at zero and f=O(r^p), p<1, at infinity. In particular r^(-n)f tends to zero for n>=1, and r^(2-n)f tends to zero for n>=3. Thus the single-mode stream is

    psi=g_+ sin((n+1)theta)+g_- sin((n-1)theta),

with the second summand omitted at n=1.

For the present basis,

    A_nj(r)=1/2 int_0^(r^2) u^n(1+u)^(-beta) du,
    B_nj(r)=(1+r^2)^(1-beta)/[2(beta-1)]  (n>=3).

The second formula converges because beta>1 for n>=3. One formula useful for small and moderate r is

    A_nj=r^(2n+2) 2F1(beta,n+1;n+2;-r^2)/[2(n+1)].

An independent expression, obtained by expanding u^n=((1+u)-1)^n, is

    A_nj=1/2 sum_{ell=0}^n (-1)^(n-ell) binom(n,ell)
                 L_(ell-beta+1)(1+r^2),

where L_a(T)=(T^a-1)/a for a!=0 and L_0(T)=log T. Cancellation in this finite expression at small r requires a separate evaluation rule or increased precision. No truncation at a finite exterior radius occurs in these formulas.

The radial derivatives can be computed without differentiating quadrature:

    g_+'=-(n+1)g_+/r-f/2,
    g_-'= +(n-1)g_-/r-f/2.

For each stream mode g(r) sin(k theta),

    U_r=-k g cos(k theta)/r,  U_theta=g' sin(k theta),
    U_x=U_r cos(theta)-U_theta sin(theta),
    U_y=U_r sin(theta)+U_theta cos(theta).

These equations fix all signs in U=(-psi_y,psi_x). The corresponding density derivatives are

    f'=(n/r-2 beta r/(1+r^2))f,
    rho_x=f' cos(theta)sin(n theta)-(nf/r)sin(theta)cos(n theta),
    rho_y=f' sin(theta)sin(n theta)+(nf/r)cos(theta)cos(n theta).

Near zero g_+=O(r^(n+1)) and g_- has a harmonic term proportional to r^(n-1), followed by smooth terms. At infinity both streams are O(r^(p+1)) and their derivatives are O(r^p). Consequently U=o(r). Its divergence vanishes, its curl is -rho_x, and its parities are the required ones. The difference from any other admissible velocity is an entire harmonic divergence-free and curl-free sublinear field; its derivatives vanish by interior harmonic estimates, so it is constant, and the required parities remove that constant. The stream's additive constant is set by odd parity. A harmonic xy term is excluded by the sublinear velocity condition.

## Origin and gauge identities

The n=1 mode contributes g_+=-a0 r^2/8+O(r^4), so its contribution to c=psi_xy(0) is -a0/4. Only the n=3 lower mode contributes any other quadratic stream term. For its j-th basis function,

    int_0^infinity s^(-2) f_3j(s) ds=1/(1-p+2j).

Thus the exact center strain in this finite family is

    c=-a0/4+sum_j a_1j/(1-p+2j).

The target center relation is c_l+c=1. It is a scalar residual condition, not an identity of the basis. A subsequent validation must recompute c by another route, not merely repeat a constrained row.

For the actual PDE spatial scaling rho_lambda(X)=lambda rho(X/lambda), a0 and c_l do not change, while a nonzero homogeneous coefficient of degree p transforms as K_lambda=lambda^(1-p)K. Hence K=-1 is attainable on every orbit for which K<0, at lambda=(-K)^(-1/(1-p)). This search is restricted to that named negative-far-axis subclass. It does not discard or classify the K>=0 or absent-trace cases by an unsupported normalization argument. The full exact-profile axis results, if used to identify this with the entire negative-slope branch, must be cited and checked separately; the solver does not need that implication.

Use a0 as a linear coordinate. For J>=2, choose all coefficients except a_00 and a_01 as independent coordinates, together with a0. Set

    a_00=-1-sum_(m>=1) (-1)^m a_m0,
    a_01=a0-a_00-sum_(j>=2) a_0j.

Then K=-1 and sum_j a_0j=a0 identically, while c remains a nontrivial linear functional. A negative a0 bound excludes the zero-density and affine degeneracies within this finite search. Any approach to a bound, zero slope, or unsettled coefficients must be reported, not interpreted as convergence.

One smooth starting family takes only a_00=-1, a_01=a0+1, and a_11=z nonzero, where

    z=(1-c_l+a0/4)(3-p).

It then has the exact center relation and far coefficient K=-1. This is only a start; the transport residual is generally nonzero. No sign property on the whole axis is inferred without checking it.

## Residual and derivative of the finite map

At each point R=(c_l X+U[rho]).grad rho-rho. Since the inverse is linear, the derivative with respect to a density perturbation h is exactly

    DR[h]=(c_l X+U[rho]).grad h+U[h].grad rho-h.

All sampling points, weights and row scaling must be saved. Training rows and an independent validation set must be distinguished. Normalized residuals N_f and N_v use the prompt definitions. Relative residuals at r=0 and on the x-axis are undefined if both numerator and denominator vanish; they are not reported as zero by a 0/0 convention. Origin derivatives and small off-axis probes supply the corresponding safeguards.

Every fixed finite field has R=O(r^(2p-1)) from nonlinear transport plus lower radial terms, while N_f is typically O(r^p). Thus a small relative far-field residual can be automatic and is not an absolute residual bound. Absolute defects, center defects, sign changes, parameter drift and separate angular/radial refinement remain part of the audit.

## Planned verification and evidence

Before solving: verify the radial formulas against direct multiprecision quadrature, differentiate the stream independently to check Poisson and velocity signs, check symmetry and center strain, test the affine coefficient/gauge map, and compare the analytic residual Jacobian against independent directional finite differences. The primary numerical inverse is implemented from these formulas, without importing numerics-lane code. Store coefficients as exact JSON numbers or binary-float hexadecimal strings, together with parameters and command provenance. No candidate or endpoint is claimed until actual outputs exist and have been independently checked.
