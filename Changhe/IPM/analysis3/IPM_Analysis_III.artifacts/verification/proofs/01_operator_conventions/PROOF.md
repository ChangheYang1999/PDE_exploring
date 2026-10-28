# Canonical signs and the normalized equation

Status: independently derived analytical statements. Numerical application requires the separately recorded input checks. No inverse or existence theorem is asserted.

## 1. Canonical inverse and strain

Let h be real, even in x and odd in y, locally C^{2,alpha}, with all Taylor coefficients of degrees at most two zero at the origin, for some 0<alpha<1. Assume |h(X)|+r|grad h(X)| <= C r^k for r>=1, with k<1. Assume the canonical solution of -Delta psi=partial_x h is selected by its odd-in-both-coordinates parity, local regularity and sublinear velocity, with no harmonic strain added. These assumptions include the explicit X3 formula once its regularity and tail have been checked.

With Fourier transform hat h(xi)=integral exp(-i X.xi)h(X)dX and inverse prefactor (2pi)^{-2}, differentiation gives, away from xi=0,

    hat U_1 = xi_1 xi_2 |xi|^{-2} hat h,
    hat U_2 = -xi_1^2 |xi|^{-2} hat h.

Indeed hat psi=i xi_1 |xi|^{-2}hat h, U=(-psi_y,psi_x). Writing R_j with multiplier i xi_j/|xi| gives U=(-R_1 R_2 h,R_1^2 h). If G=-(2pi)^{-1}log r, then

    partial_xx G = p.v. [(x^2-y^2)/(2pi r^4)] - delta_0/2,
    partial_xy G = p.v. [xy/(pi r^4)].

The delta term in the first identity follows because the trace is Delta G=-delta_0, reflection symmetry makes the two diagonal contact terms equal, and the off-diagonal term is odd in each coordinate. Thus R_1^2=T_xx-I/2 and R_1R_2=T_xy in these conventions.

The raw central strain c[h]=psi_xy(0) is

    c[h]=(1/pi) integral_{R^2} h(X) y(3x^2-y^2)/r^6 dX
        =(1/pi) integral_{R^2} h(X) sin(3theta)/r^3 dX.       (1)

Here the integral is absolute. Near zero, Taylor's theorem gives h=O(r^{2+alpha}), so the absolute radial integrand is O(r^alpha)dr. At infinity it is O(r^{k-2})dr, which is integrable for k<1. To verify the sign without differentiating a singular distribution at zero, expand partial_x h in sin(2n theta). If f_1 is its sin(2theta) coefficient under the convention (1/pi)integral_0^{2pi}, the regular sublinear Poisson Green formula gives

    c[h]=(1/2)integral_0^infinity f_1(r)/r dr
         =(1/pi)integral partial_x h(X) xy/r^4 dX.

This Green formula follows by solving -(psi_n''+psi_n'/r-4n^2 psi_n/r^2)=f_n with one solution regular at zero and the other sublinear in velocity at infinity. The n=1 coefficient of r^2 sin(2theta)=2xy is (1/4)integral f_1/r. Integration by parts on epsilon<r<R gives (1), because -partial_x(xy/r^4)=y(3x^2-y^2)/r^6. The inner boundary is O(epsilon^{1+alpha}) and the outer is O(R^{k-1}); both vanish. If a_3(r)=(1/pi)integral h(r,theta)sin(3theta)dtheta, then c[h]=integral_0^infinity a_3(r)/r^2 dr.

## 2. Normalization at continuous factor regularity

Let rho be C^1 near zero, rho=x^2y a with a continuous at zero and a(0)=1. Let U be C^1, divergence free, with the canonical reflection parities, and c=psi_xy(0). Parity gives U(0)=0 and DU(0)=diag(-c,c). If (ell X+U).grad rho-rho=0 distributionally near zero, then

    3ell-c=1.                                               (2)

Proof: set rho_e(X)=e^{-3}rho(eX) and V_e(X)=e^{-1}(ell eX+U(eX)). On compact sets rho_e tends uniformly to x^2y and V_e tends in C^1 to B X, where B=diag(ell-c,ell+c). Since div V_e=2ell, stationarity is div(V_e rho_e)=(1+2ell)rho_e. Passing to distributions gives BX.grad(x^2y)=x^2y. The coefficient is 2(ell-c)+(ell+c)=3ell-c. This proof does not differentiate the continuous factor a.

For ell>1/2, an exactly normalized background has

    DV(0)=diag(-A,D), A=2ell-1, D=4ell-1=2A+1.

For a nonstationary background whose scalar is chosen as ell=(1+c[rho])/3, the same central matrix follows from that scalar definition alone. With an independently held scalar ell_held it instead equals diag(ell_held-c[rho],ell_held+c[rho]); numerical proximity is not equality.

## 3. Full perturbation identity

Let U and c be linear on a vector space containing rho_bar and h, and assume every displayed product is defined in the desired distribution or function space. Define ell(rho)=(1+c[rho])/3 and

    F(rho)=(ell(rho)X+U[rho]).grad rho-rho.

Then, identically,

    F(rho_bar+h)=F(rho_bar)+Lh+N(h),
    Lh=V.grad h-h+(U[h]+c[h]X/3).grad rho_bar,
    N(h)=(U[h]+c[h]X/3).grad h,
    V=ell(rho_bar)X+U[rho_bar].                              (3)

Expand the two linear maps and the bilinear product. The scalar variation is exactly c[h]/3. Equation (3) is a Frechet derivative only in spaces where the relevant linear and bilinear maps are continuous. Algebra alone does not establish that continuity.

If a file holds ell_held instead of ell(rho_bar), put delta=(1+c[rho_bar])/3-ell_held. The normalized residual is F_held(rho_bar)+delta X.grad rho_bar, and the normalized transport in L contains the additional delta X.grad h. Both terms must be retained.

Near zero, if U[h]=c[h](-x,y)+o(r), the cubic leading part cancels exactly:

    [c[h](-x,y)+c[h](x,y)/3].grad(x^2y)
      =(-2c[h]x/3,4c[h]y/3).(2xy,x^2)=0.                 (4)

Consequently an exact decomposition of the coupling, with p=x^2y, is

    (U[h]+c[h]X/3).grad rho_bar
      =(U[h]-c[h](-x,y)).grad rho_bar
        +(-2c[h]x/3,4c[h]y/3).grad(rho_bar-p).

Quantitative smallness requires bounds on both remainders; the cancellation itself supplies none.

## 4. Scaling and tail variation

Assume the canonical inverse commutes with the dilation rho_lambda(X)=lambda rho(X/lambda). This follows either by changing variables in its Green formula or by uniqueness in the canonical class. Then U[rho_lambda](X)=lambda U[rho](X/lambda), c[rho_lambda]=c[rho], and F(rho_lambda)(X)=lambda F(rho)(X/lambda). For a differentiable dilation path, K=rho-X.grad rho therefore satisfies

    L_rho K=F(rho)-X.grad F(rho),   c[K]=0.

The coefficient of x^2y in rho_lambda is lambda^{-2}, so J(K)=-2. At an exact solution LK=0, but no kernel statement at a numerical approximation follows without its residual derivative. Restricting J(h)=0 removes this tangent algebraically only when J is meaningful and its kernel is closed in the chosen domain topology.

If the leading tail is r^{k(ell)}Theta(theta), with k=1/ell, then differentiating ell by delta ell gives

    delta k=-delta ell/ell^2=-c[h]/(3ell^2),
    delta(r^k Theta)=r^k delta Theta
                    -c[h] r^k log(r)Theta/(3ell^2).       (5)

This statement presupposes differentiability of the tail parametrization. The logarithmic direction is part of the linear variation and must have its own coefficient or lie in the chosen space. A decaying correction space that excludes it forces an additional compatibility condition.

## 5. The source point

Let an exact stationary rho be C^2 and V C^1 near an axis point P=(x_*,0), with V(P)=0. Let g(x)=rho_y(x,0), w(x)=V_1(x,0), and mu(x)=partial_y V_2(x,0). Suppose g(x_*) is nonzero. Parity and incompressibility imply

    w'+mu=2ell,  w g'+mu g=g.

The second identity is obtained by differentiating stationarity in y at y=0; rho_x and V_2 vanish there. At P, mu=1, w'=2ell-1. The off-diagonal entries vanish by parity. Thus the source transport eigenvalues are 2ell-1 and 1. A sampled approximate source has no right to these exact values without its own residual identity.

Freeze the local transport at diag(A,mu), use s=x-x_*, and freeze grad rho at (0,g). The translation-invariant singular-integral multiplier contributes U[h].(0,g)=-g M h, where M has multiplier xi_1^2/|xi|^2. The corresponding principal frozen expression is

    L_P h=A s h_s+mu y h_y-h-g M h.                       (6)

Equation (6) deliberately omits the global rank-one term. Before freezing its spatial coefficient, that term is c[h] X.grad rho/3; with the gradient frozen but X retained it is c[h]g y/3, because P.(0,g)=0. It vanishes at P, but not on a neighborhood. Any localized full operator must retain it or justify its treatment as a separate finite-rank perturbation.

## Dependencies and scope

Only the explicit Green ODE, elementary distributional integration by parts, Taylor's theorem and differentiation of the stated paths are used. Hypotheses concerning existence and regularity of the canonical velocity are explicit. Neither numerical coefficients nor a global inverse enter these proofs. The reference Analysis I often writes Sigma for the raw strain and c=Sigma/3; throughout this run c is raw strain, as in PROMPT.md.
