# Anisotropic slope coordinates and the singular hydrostatic inverse

Written 2026-10-21T07:15:42.566079+00:00 before computational verification. Result 174. These are exact coordinate statements and inverse-operator facts. The counterexamples below are not stationary profiles. The primary existence question remains open.

## 1. Exact transformation

Fix ell>1 and let a=rho_y(0) be nonzero. Write h=sqrt(|a|), x=h*xi, rho(x,y)=a*g(xi,y), psi(x,y)=h*Phi(xi,y). Put eps=1/|a| and s=sign(a). Direct differentiation gives rho_x=(a/h)g_xi, rho_y=a*g_y, U1=-h*Phi_y, U2=Phi_xi, and

(ell*xi-Phi_y)g_xi+(ell*y+Phi_xi)g_y=g,
-Phi_yy-eps*Phi_xixi=s*g_xi,
g_y(0)=1.

Conversely these equations reconstruct the original profile equations with slope a. This is a bijective coordinate change for each fixed a, not a symmetry of the original isotropic PDE: the invariant slope is now an ellipticity parameter, with a separate sign. Setting g_y(0)=1 in this transformed equation does not set the original slope to one.

The new velocity is V=(-Phi_y,Phi_xi)=(U1/h,U2). Thus div_(xi,y) V=0. The old and new radii are comparable for fixed h>0, so U=o(|(x,y)|) is equivalent to V=o(|(xi,y)|). The density and gradient growth assumptions are likewise equivalent with constants depending on a. Reflection parities are preserved. Differences of two canonical velocities arise from a solution of Phi_yy+eps*Phi_xixi=0. Rescaling xi reduces each velocity component to an entire harmonic function of sublinear growth, hence a constant. Velocity parities exclude the constants. Therefore the transformed inverse is canonical and unique for eps>0. This argument gives no estimate uniform as eps tends to zero.

The center strain is unchanged: psi_xy(0)=Phi_xiy(0). Hence a profile still requires ell+Phi_xiy(0)=1. If rho=a*y+b*x^2*y+e*y^3+O(r^5), then g=y+s*b*xi^2*y+(e/a)*y^3+O(|(xi,y)|^5). For a>0 the xi^2*y coefficient is b as stated by the lead; for a<0 it is -b. These b,e are in the chosen spatial representative.

If rho(0,y)~K*y^(1/ell) as y tends to positive infinity, then g(0,y)~(K/a)*y^(1/ell). The established axis theorem gives K/a>0 for any primary profile. The genuine spatial scaling sends K/a to lambda^(1-1/ell)K/a, so every such profile has the unique representative K/a=1. This gauge does not bound a, impose angular shape, or assert compactness of a sequence as a grows.

## 2. The stratified singular solution

For p=1/ell in (0,1), rho(y)=K*sign(y)*|y|^p and U=0 satisfy ell*y*rho_y=rho away from y=0. Also rho_y=K*p*|y|^(p-1) is locally integrable, so the identity holds as distributions on the whole plane, without a delta measure at the axis. Since rho_x=0, the canonical zero velocity has the required divergence, curl and parities. The density is C^{0,p}, but not C^1 at y=0 when K is nonzero. It also violates the full-plane gradient growth bound along x tending to infinity with y fixed and nonzero, since its nonzero y derivative is independent of x. It is outside the primary and any smooth secondary class. Its angular trace has the same non-C^1 defect at horizontal directions. No claim that a smooth profile approaches it follows.

## 3. A conditional hydrostatic limit for rapidly decaying inputs

Here a>0 and the input g is fixed as eps tends to zero. Assume g is a real Schwartz function on R^2, even in xi and odd in y. Partial Fourier transform in xi uses ghat(k,y)=int exp(-ik*xi)g(xi,y) dxi, with inverse factor 1/(2*pi). For k!=0 put q=sqrt(eps)*|k|. The odd-in-y full-plane solution is

Phihat_eps(k,y)=ik*int_0^infinity D_q(y,s)*ghat(k,s) ds,  y>=0,
D_q(y,s)=[exp(-q*|y-s|)-exp(-q*(y+s))]/(2q).

This is the one-dimensional Green function with odd reflection, obtained by solving (-d_y^2+q^2)D_q=delta on the line and subtracting the reflected source. It is the transformed canonical inverse: its derivatives have the stated parities and sublinear growth, and uniqueness was proved in Section 1. The zero Fourier mode has no source and contributes no velocity.

For y,s>=0, 0<=D_q(y,s)<=min(y,s). This follows from D_q=exp(-q*max(y,s))*sinh(q*min(y,s))/q and sinh(z)<=z*exp(z). Its y derivative has magnitude at most one, with limit 1 for s>y and 0 for s<y as q tends to zero. Dominated convergence therefore gives, uniformly on bounded sets for the indicated integrals,

Phi_0(xi,y)=int_0^y s*g_xi(xi,s) ds+y*int_y^infinity g_xi(xi,s) ds,
V1_0(xi,y)=-int_y^infinity g_xi(xi,s) ds,
V2_0(xi,y)=int_0^y s*g_xixi(xi,s) ds+y*int_y^infinity g_xixi(xi,s) ds.

The domination is justified after Fourier inversion because int |k|^j int (1+s)|ghat(k,s)| ds dk is finite for every fixed j for a Schwartz input. More xi derivatives follow the same way. The first y derivative of V1 follows either the PDE or direct integration; higher local convergence can be read from the same ODE and differentiated inputs. No claim of convergence for varying g_eps is made without uniform bounds and convergence assumptions on that sequence.

The limit solves -Phi_0,yy=g_xi, Phi_0 odd in both variables. It has bounded velocity, hence the sublinear gauge. Any other hydrostatic potential with these parities differs by y*H(xi). Its velocity difference is (-H(xi),y*H'(xi)). Sublinear growth along each vertical line forces H'=0; oddness in xi then gives H=0. Thus the limit has the unique hydrostatic canonical velocity in this class. In particular,

c_0=Phi_0,xiy(0)=int_0^infinity g_xixi(0,s) ds.

For a sequence of profiles, identifying c_0 with 1-ell requires a justified passage of that sequence through this inverse limit. The original admissible class supplies none of the required uniform Fourier moments. The formula is conditional, not an additional necessary condition already proved for arbitrary large-slope profiles.

## 4. The given growth bounds permit a divergent canonical strain

Fix 0<gamma<1 and set

h(xi)=exp(-xi^2),  f(y)=y*(1+y^2)^((gamma-2)/2),  g(xi,y)=h(xi)*f(y).

This is smooth, even in xi, odd in y, and g_y(0)=1. It satisfies the primary density and gradient growth bounds as a function, without satisfying the transport equation. Indeed h and every derivative decrease faster than powers, while |f(y)|<=C(1+|y|)^(gamma-1) and |f'(y)|<=C(1+|y|)^(gamma-2). Using 1+sqrt(xi^2+y^2)<=C(1+|xi|)(1+|y|) proves |grad g|<=C(1+r)^(gamma-1); g is bounded and hence obeys the density bound. This direct estimate does not assume a global Hessian estimate.

For xi!=0, the proposed integral of g_xi=h'(xi)f diverges, since

int_y^S f(s) ds=[(1+S^2)^(gamma/2)-(1+y^2)^(gamma/2)]/gamma.

There is no hydrostatic velocity for this g with V=o(r). To see this, any odd-in-y potential solving -Phi_yy=h'(xi)f(y) must have

Phi(xi,y)=y*H(xi)-h'(xi)*int_0^y (y-s)f(s) ds.

At xi=0, h''(0)=-2. Thus V2(0,y)=y*H'(0)+2*int_0^y (y-s)f(s) ds. The integral is asymptotic to y^(gamma+1)/[gamma*(gamma+1)], as follows by scaling s=y*z and dominated convergence, because f(y*z)/(y*z)^(gamma-1) tends to one and is bounded by one. This superlinear term cannot be cancelled by y*H'(0).

More strongly, the canonical positive-eps center strain actually diverges. The Fourier formula above is valid for this input for every eps>0, first with a vertical cutoff and then by dominated convergence using the exponential factor. With hhat(k)=sqrt(pi)*exp(-k^2/4), define L(q)=int_0^infinity exp(-q*s)f(s) ds. Then

c_eps=-(1/(2*pi))*int_R k^2*hhat(k)*L(sqrt(eps)*|k|) dk.

All integrands here are nonnegative before the minus sign. Since 0<f(s)<=s^(gamma-1), q^gamma L(q)<=Gamma(gamma). Scaling s=z/q and dominated convergence shows q^gamma L(q)->Gamma(gamma) as q decreases to zero. A second dominated convergence, now in k, is justified by the integrable function |k|^(2-gamma)*hhat(k). Therefore

eps^(gamma/2)*c_eps -> -D_gamma,
D_gamma=2^(2-gamma)*Gamma(gamma)*Gamma((3-gamma)/2)/sqrt(pi)>0.

The last constant follows by the substitution z=k^2/4 in the Gaussian integral. In particular c_eps tends to negative infinity. This is an explicit failure of a finite canonical inverse limit under exactly the allowed function and gradient bounds. It does not exclude a profile sequence: the example does not solve transport, and a true sequence has nonlocal constraints that might enforce additional cancellation.

## 5. An independent Gaussian-mixture formula

The strain limit can also be checked without the Laplace asymptotic. For g_t(xi,y)=exp(-xi^2)*y*exp(-t*y^2), t>0, direct two-dimensional Fourier inversion gives

c_eps[g_t]=-1/(sqrt(t)+sqrt(eps))^2.

For t=1 the polar radial integral is 8 and the angular reduction is

c_eps=-(4/pi)*int_0^infinity z^2/[(1+z^2)^2(eps+z^2)] dz.

Writing a=sqrt(eps)>0, the integral is pi/[4(1+a)^2]. One derivation starts with J(a)=int_0^infinity dz/[(z^2+a^2)(z^2+b^2)]=pi/[2ab(a+b)] for a,b>0, obtained by partial fractions, including the coincident case by continuity. Since z^2/(z^2+b^2)^2=1/(z^2+b^2)-b^2/(z^2+b^2)^2, the needed integral at b=1 is J+(b/2)d_b J=pi/[4b(a+b)^2]. The anisotropic y change of variables yields the displayed t formula. All Gaussian Fourier integrals are absolutely convergent.

Put nu=1-gamma/2 in (1/2,1). The positive Gamma integral represents f(y)=y*(1+y^2)^(-nu) as

f(y)=(y/Gamma(nu))*int_0^infinity t^(nu-1)*exp(-t)*exp(-t*y^2) dt.

For the center strain, Tonelli applies to the nonnegative integrands in the negative-strain Fourier formula, and the final one-dimensional integral is finite for eps>0. Consequently

c_eps=-(1/Gamma(nu))*int_0^infinity t^(nu-1)*exp(-t)/(sqrt(t)+sqrt(eps))^2 dt.

After t=eps*v^2 this becomes

eps^(gamma/2)c_eps=-(2/Gamma(nu))*int_0^infinity v^(1-gamma)*exp(-eps*v^2)/(1+v)^2 dv.

The limiting integral is the beta integral B(2-gamma,gamma), giving D_gamma=2*Gamma(2-gamma)*Gamma(gamma)/Gamma(1-gamma/2). The Gamma duplication identity shows this equals the constant in Section 4. This provides a second exact derivation and a stable numerical quadrature. For the Schwartz manufactured input g_1=exp(-xi^2-y^2)*y the limit strain is -1 and the limiting potential is -sqrt(pi)*xi*exp(-xi^2)*erf(y)/2, which differentiates to the three formulas in Section 3.

## 6. Scope and dependencies

CONFIRMED analytically: the exact anisotropic equations, both slope signs, the fixed-eps canonical gauge, the stratified distributional example, the Schwartz-input hydrostatic limit, and the class-admissible non-profile counterexample with divergent strain. OPEN: compactness and the inverse limit along actual profiles, the existence of profiles at any slope, and all proposed numerical concentration mechanisms. Verification evidence will be placed in verification/. Dependencies are elementary chain rule and polynomial jets, the canonical uniqueness argument in ../inverse/PROOF.md, one-dimensional Green functions, dominated convergence, and the elementary Gaussian integral. These are standalone informal proofs; no formal compilation is authorized.
