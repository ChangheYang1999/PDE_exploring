# A uniform anisotropic inverse limit under a weighted Hessian bound

Result 175. Written 2026-10-21T07:23:25.323023+00:00 before computational checks. This is a conditional inverse theorem, not an existence theorem. It strengthens the fixed Schwartz-input statement of result174 to a class that allows a nonzero sublinear angular far field.

## Statement

Fix 0<gamma<1. Let g be smooth, even in xi and odd in y, and suppose on the whole plane that

|g| <= C(1+r)^gamma, |grad g| <= C(1+r)^(gamma-1), |g_xixi| <= C(1+r)^(gamma-2),
r=sqrt(xi^2+y^2).

Only the displayed second derivative is needed, not every Hessian entry. For eps>0 let Phi_eps be the odd-in-both-variables canonical potential solving

-Phi_eps,yy-eps*Phi_eps,xixi=g_xi,
V_eps=(-Phi_eps,y,Phi_eps,xi)=o(r).

Then V_eps converges locally uniformly as eps tends to zero to the uniquely gauged hydrostatic velocity

V1_0(xi,y)=-int_y^infinity g_xi(xi,s) ds,
V2_0(xi,y)=int_0^y s*g_xixi(xi,s) ds+y*int_y^infinity g_xixi(xi,s) ds,

for y>=0, extended with the required parities. The canonical strain converges to

Phi_eps,xiy(0,0) -> int_0^infinity g_xixi(0,s) ds.

Moreover |V_eps(xi,y)| <= C_gamma C (1+r)^gamma for every eps>0 with a constant independent of eps. The same conclusions hold for varying inputs g_eps converging in C^2 on every compact set to g_0, provided the three displayed bounds hold with one common C. No such common bound has been established for the team's candidate or hypothetical profile sequences.

## Poisson-kernel representation

For a>0 put P_a(z)=a/[pi(a^2+z^2)], and let P_0*f=f. This nonnegative kernel has integral one, is even, and is an approximate identity as a tends to zero: split the integral into |z|<delta and its complement, whose mass tends to zero. Its Fourier transform is exp(-a|k|). For completeness this identity follows by closing the integral of exp(-ikz)/(z^2+a^2) in the half plane where the exponential decreases and taking the single simple pole; at k=0 it is the elementary arctangent integral. Consequently P_a*P_b=P_(a+b), also verified by partial fractions. Convolutions below are in xi alone and are absolutely convergent because the differentiated inputs are bounded.

For y,s>=0 the one-dimensional odd Green function from result174 can be written

D_q(y,s)=(1/2)int_(|y-s|)^(y+s) exp(-q*t) dt.

Its y derivative away from s=y is

(1/2)[sign(s-y)exp(-q|y-s|)+exp(-q(y+s))].

Replacing the exponential by the Poisson convolution gives the candidate potential and velocity

Phi_eps(xi,y)=(1/2)int_0^infinity int_(|y-s|)^(y+s) (P_(sqrt(eps)*t)*g_xi(.,s))(xi) dt ds,

V1_eps(xi,y)=-(1/2)int_0^infinity [sign(s-y)(P_(sqrt(eps)*|y-s|)*g_xi)(xi,s)
                                          +(P_(sqrt(eps)*(y+s))*g_xi)(xi,s)] ds,
V2_eps(xi,y)=(1/2)int_0^infinity int_(|y-s|)^(y+s) (P_(sqrt(eps)*t)*g_xixi)(xi,s) dt ds.

The value on the measure-zero line s=y has no effect. All these integrals converge by the bounds below. For compactly supported smooth inputs of the stated parities these formulas follow by the partial Fourier transform and the Green function. For general g, multiply by smooth even cutoffs in xi and y at radius R. The cutoff densities retain the same three weighted bounds with constants independent of R: the extra xi derivatives have factors R^-1 and R^-2 on r comparable to or above R, bounded by the stated orders. They converge locally with their derivatives to g. Applying the estimates below proves local convergence of these potentials and velocities and convergence of the formulas. The elliptic equation passes in distributions, giving the desired smooth canonical solution by local elliptic regularity. The uniform growth estimate and uniqueness from result174 identify it with the canonical inverse.

## Estimates and passage to the limit

Write f_s(xi)=g_xi(xi,s). Since g is even in xi, f_s is odd, f_s(0)=0, and f_s'=g_xixi. The original bounds imply

||f_s||_infinity <= C(1+s)^(gamma-1),
||f_s'||_infinity <= C(1+s)^(gamma-2).

Poisson convolution preserves these two sup norm bounds and oddness. Thus, for every a>=0,

|(P_a*f_s)(xi)| <= C min((1+s)^(gamma-1), |xi|(1+s)^(gamma-2)),
|(P_a*g_xixi(.,s))(xi)| <= C(1+s)^(gamma-2).

The first is integrable in s for each fixed xi; for xi in a compact set its second bound gives a common integrable majorant. The second bound times min(y,s) is integrable for every bounded y. Therefore the potential and velocity integrals above converge absolutely and locally uniformly. For a fixed (s,t), the approximate identity gives convergence of the convolutions as eps tends to zero. Dominated convergence gives the displayed hydrostatic formulas, first pointwise. Uniformity on compact sets follows from the uniform approximate-identity property for a continuous input on a compact set, the same tail bounds, and a compact s,t truncation. In V1 the sign(s-y) is bounded and causes no difficulty in this argument.

The global estimate is uniform in eps. The absolute value of V1 is at most the integral of the first majorant over all s>=0. For |xi|>=1, split at s=|xi|: the first part is at most C_gamma(1+|xi|)^gamma and the second at most C_gamma |xi|(1+|xi|)^(gamma-1). For |xi|<1 use the second majorant throughout. The V2 bound is

C int_0^infinity min(y,s)(1+s)^(gamma-2) ds <= C_gamma(1+y)^gamma,

by splitting at s=y. Hence V_eps=O((1+r)^gamma) uniformly in eps, including the limit. Parities are immediate. The hydrostatic gauge uniqueness is elementary: any other odd potential differs by y H(xi); its velocity difference is (-H,y H'), and sublinear growth on each vertical line forces H'=0, then oddness forces H=0.

At y=0 the V1 formula can be differentiated once in xi, because its derivative has integrable majorant C(1+s)^(gamma-2). Thus

c_eps=Phi_eps,xiy(0,0)=int_0^infinity (P_(sqrt(eps)*s)*g_xixi(.,s))(0) ds.

The approximate identity and dominated convergence give the strain limit. No nonintegrable boundary term has been discarded.

For varying g_eps the same majorants hold. On a compact xi,s set, C^2 convergence and the approximate-identity split show P_(sqrt(eps)*t)*g_eps,xi and P_(sqrt(eps)*t)*g_eps,xixi converge uniformly to the corresponding g_0 derivatives: the outer xi tail is bounded by the uniform sup norms times the Poisson tail mass. Truncating s,t and then using the common integrable majorants proves every preceding convergence statement unchanged.

## Growing-tail manufactured family

For 0<gamma<1 let p=(gamma-1)/2 and take g=y*(1+xi^2+y^2)^p. It has g_y(0)=1 and all three weighted bounds, with genuine r^gamma growth. Its hydrostatic velocity is

V1_0=xi*(1+xi^2+y^2)^p,
V2_0=-int_0^y [(1+xi^2+s^2)^p+2p*xi^2*(1+xi^2+s^2)^(p-1)] ds,
c_0=-1.

The first formula follows by integrating g_xi=2p*xi*s*(1+xi^2+s^2)^(p-1) from y to infinity. The second follows by divergence and V2(xi,0)=0, and agrees with the Green formula by integration by parts.

In fact c_eps=-1/(1+sqrt(eps))^2 for this entire family, independently of gamma. To verify this directly from the Poisson strain formula, use polar coordinates xi=r*cos(theta), s=r*sin(theta), 0<=theta<=pi. The two radial integrals are int_0^infinity r*(1+r^2)^(p-1)dr=-1/(2p) and int_0^infinity r^3*(1+r^2)^(p-2)dr=1/[2p(p-1)]. Thus, writing a=sqrt(eps),

c_eps=(a/pi)*int_0^pi sin(theta)^2*(2*cos(theta)^2-1)/(cos(theta)^2+a^2*sin(theta)^2) dtheta
     =(2a/pi)*int_0^infinity (z^2-1)/[(1+z^2)^2*(z^2+a^2)] dz.

The latter integral follows by z=cot(theta) and reflection. Let J(a,b)=pi/[2ab(a+b)] as in result174. The integral at b=1 is J+(b^2+1)/(2b)*d_b J, evaluated at b=1; multiplying by 2a/pi simplifies to -1/(1+a)^2. Alternatively express g as a positive Gamma mixture of y*exp(-t*(xi^2+y^2)); each Gaussian has the same strain because its isotropic spatial scaling preserves the slope and strain. This supplies an independent check. No member of this manufactured family is being claimed to solve transport.

For the positive-slope anisotropic profile equation, cubic jets also give a useful conditional diagnostic. Write g=y+B*xi^2*y+E*y^3+O(r^5), Phi=c*xi*y+D*xi^3*y+F*xi*y^3+O(r^6). Center normalization is c=1-ell. The cubic equations are F=-2E, 3D=-(4ell-2)B, and 3(eps*D+F)=-B. Eliminating D,F gives [1-eps*(4ell-2)]B=6E. Thus if such jets converge and eps tends to zero with bounded ell, B_0=6E_0. Passing jets to the limit requires the corresponding local derivative convergence. This identity is exact for a smooth profile, and is only a residual diagnostic for saved non-profile states.

## Scope

The original prompt imposes only the first two weighted bounds, not the third, and does not impose a common bound after anisotropic slope rescaling. The divergent example in result174 has g_xixi(0,s) asymptotic to -2 s^(gamma-1), so it fails exactly this sufficient extra condition. This theorem neither contradicts that example nor establishes the condition for profiles. If a sequence of positive-slope profiles with slope tending to infinity obeyed these uniform rescaled bounds and local C^2 convergence, its transformed center equation would pass to int_0^infinity g_0,xixi(0,s)ds=1-ell_0 whenever ell also converges. That is conditional only.

Dependencies: elementary Poisson kernel facts proved above, the one-dimensional Green formula and canonical uniqueness in result174, local elliptic regularity, dominated convergence, and cutoff approximation. Computational manufactures and any independent review are recorded under verification/.
