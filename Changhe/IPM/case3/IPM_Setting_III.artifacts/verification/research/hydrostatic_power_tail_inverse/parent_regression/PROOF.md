# Regression of the existing Cartesian hydrostatic evaluator

The parent evaluator acquired constructor-option validation after its original manufactured gate. Result219 correctly rejected that old gate hash before evaluating any state. Repeat the existing independent manufactured suite on the current module, in this separate evidence folder, without replacing the original gate or past evidence. The evaluator formula is unchanged. Original proof follows; this is a regression check, not a new theorem.

# Independent hydrostatic evaluator and exact center functional

Written 2026-10-21 before implementation. This result concerns the limiting operator, not the original full-plane IPM inverse, and cannot by itself establish an original IPM endpoint. Coordinates in this document are (x,y). The exponent of the radial map is P>1, the density exponent is p=1-1/P in (0,1), and ell denotes the transport coefficient. No identity p=1/ell is needed for the evaluator.

## Statement and density definition

Let L>0 and let beta_k be real polynomials of degree at most N-k, for 0<=k<M<=N+1. Define sigma=(1+t)/2, w=(1-t)/2 and

 r=L sqrt(sigma)/(2w)^P,  B(t,theta)=sum_k sigma^k beta_k(t) cos(2k theta),
 H=wB,  rho(x,y)=yH(t(r),theta).

Each beta_k may be supplied in ordinary or shifted Chebyshev coordinates; the actual shift and binary coefficients specify the polynomial. The radial map has a unique t in (-1,1) for r>0 because its logarithmic derivative is positive. Near zero, the implicit function theorem makes sigma an analytic function of r^2 with sigma=2^(2P)r^2/L^2+O(r^4). Thus sigma^k cos(2k theta) is analytic in (x,y) near zero. This formula defines a smooth even-in-x, odd-in-y density, and its slope is a=beta_0(-1). At infinity, differentiation of the compact map gives the bounds |rho|=O(r^p), |grad rho|=O(r^(p-1)), |rho_xx|=O(r^(p-2)). These estimates follow term by term for the finite polynomial and smooth angular sum. They permit the canonical hydrostatic inverse of result175; this assertion says nothing about its transport residual.

## Cartesian derivatives

Put z=log r, s=sin(theta), c=cos(theta), Q=w+2P sigma. Direct differentiation gives

 T=t_z=4 sigma w/Q,
 t_zz=8 sigma w [(1-2sigma)Q-sigma w(2P-1)]/Q^3.

Ordinary polynomial differentiation and trigonometric differentiation give H_t,H_tt,H_theta,H_ttheta,H_thetatheta. Set H_z=T H_t, H_zz=T^2 H_tt+t_zz H_t and H_ztheta=T H_ttheta. Applying partial_x=(c partial_z-s partial_theta)/r and partial_y=(s partial_z+c partial_theta)/r to rho=r s H gives

 rho_x=s c H_z-s^2 H_theta,
 rho_y=H+s^2 H_z+s c H_theta,
 rho_xx=(s/r)[c^2 H_zz+(s^2-c^2)H_z-2s c H_ztheta+s^2 H_thetatheta+2s c H_theta].

These identities hold for r>0; the origin values are (rho,rho_x,rho_y,rho_xx)=(0,0,a,0). To avoid replacing exact axis zeros with trigonometric roundoff, the implementation uses powers of c+i s for the angular functions and explicit axis values. First and second radial derivatives come from scalar polynomial recurrences, not the producer differentiation matrices. Repeated precision scalar differentiation of the density and Cartesian finite differences provide separate tests.

## Full vertical inverse and gauge

For y>=0 define

 Phi(x,y)=int_0^y t rho_x(x,t)dt+y int_y^infinity rho_x(x,t)dt,
 V1(x,y)=-int_y^infinity rho_x(x,t)dt,
 V2(x,y)=int_0^y t rho_xx(x,t)dt+y int_y^infinity rho_xx(x,t)dt.

Extend Phi odd in both variables, V1 odd in x/even in y and V2 even in x/odd in y. Because rho_x(x,t)=O(|x|t^(p-2)) at fixed x and rho_xx=O(t^(p-2)), all displayed tail integrals converge. Differentiation under the integrals on compact x intervals gives -Phi_yy=rho_x, V=(-Phi_y,Phi_x), and divergence V=0. The common weighted bounds yield V=O(r^p) by the estimate proved in result175. If two such velocities have the same source, their stream difference satisfies Phi_yy=0, hence Phi=yA(x)+B(x). Parity forces B=0 and A odd. Sublinear growth of the velocity along each line x=constant forces A'(x)=0; oddness then gives A=0. This fixes the hydrostatic gauge.

The implementation splits at a finite R but includes the entire tail with t=R/v, 0<v<1. For either f=rho_x or f=rho_xx,

 int_R^infinity f(x,t)dt=int_0^1 v^(-p) [R v^(p-2) f(x,R/v)]dv.

Use composite Gauss-Legendre integration on the finite intervals and Gauss-Jacobi integration with weight v^(-p) for the infinite interval. The residual tail integrand is bounded at v=0. It may have fractional-power corrections; finite-order Gauss-Jacobi integration is not declared exact. Change both orders and R, and record discrepancies. No exterior boundary condition or finite-box replacement is introduced.

## Exact center strain

The hydrostatic center strain is c_H=Phi_xy(0,0)=int_0^infinity rho_xx(0,y)dy. At theta=pi/2 the Cartesian formula reduces to rho_xx=(H_z+H_thetatheta)/r. Since dr/r=dt/T,

 c_H=int_-1^1 H_t dt + int_-1^1 H_thetatheta/T dt
     =-a-sum_{k=1}^{M-1} k^2(-1)^k int_-1^1 Q(t) sigma(t)^(k-1) beta_k(t)dt.

The first boundary term is H(1)-H(-1)=-a, because all beta_k are finite at1 and w(1)=0. The second equality uses H_thetatheta=-4 sum k^2(-1)^k w sigma^k beta_k and T=4sigma w/Q. Its apparent sigma denominator cancels for each k>=1. Each remaining integrand is a polynomial of degree at most N. Thus a Gauss-Legendre rule of degree at least N is exact in exact arithmetic. A separate rational implementation multiplies Chebyshev polynomials and uses int_-1^1 T_n(t)dt=0 for odd n and 2/(1-n^2) for even n. For binary parameters and coefficients this gives the exact rational c_H, including every angular mode. It is different from the isotropic inverse strain and must not be substituted for that strain in the original PDE.

## Spatial and anisotropic comparison

For a positive-slope source rho with slope a>0 and positive y-axis tail coefficient K, let l=(a/K)^P and h=sqrt(a). Its regauged anisotropic density is

 g(x,y)=(l/a)rho(hx/l,y/l).

It has g_y(0)=1 and y-axis tail coefficient1. Direct chain rules give g_x=rho_x/h, g_y=rho_y/a, g_xx=rho_xx/l at the transformed point. Changing the integration variable in the vertical inverse gives

 V1[g](x,y)=(l/h)V1[rho](hx/l,y/l),
 V2[g](x,y)=l V2[rho](hx/l,y/l),
 c_H[g]=c_H[rho].

This is a change of equation from an original IPM field to a hydrostatic input; it is not an extra symmetry allowing the original normalized slope to be set to1. Hydrostatic residuals must be reported as such. A nonzero ell+c_H-1 immediately prevents exact hydrostatic transport for a unit-slope input, independently of any fitted grid.

## Manufactured checks and scope

For rho=exp(-x^2)y exp(-tau y^2), tau>0, explicit integration gives

 Phi=-x exp(-x^2) sqrt(pi) erf(sqrt(tau)y)/(2 tau^(3/2)),
 V1=x exp(-x^2)exp(-tau y^2)/tau,
 V2=(4x^2-2)exp(-x^2)sqrt(pi)erf(sqrt(tau)y)/(4tau^(3/2)),
 c_H=-1/tau.

Differentiate these expressions to check the defining hydrostatic Poisson and divergence equations. For any radial input rho=yF(x^2+y^2) with F tending to0 and convergent inverse, rho_x=x partial_y F, hence V1=xF and c_H=-F(0). In particular every radial Q input has c_H=-a, regardless of P or its radial polynomial; angular manufactured inputs test the extra center terms.

The code must pass manufactured derivatives, full-tail velocity checks, exact center checks and parity checks before use on producer numeric data. Report finite sample residuals R_H=(ell X+V)·grad g-g with the prompt's Nf,Nv, absolute residuals and locations. Undefined ratios on the horizontal axis are left undefined. Numerical discrepancies are empirical comparisons, not interval enclosures, uniform bounds, or an existence theorem. Neither a hydrostatic numerical state nor an exclusion for this limiting problem by itself decides the original problem.
