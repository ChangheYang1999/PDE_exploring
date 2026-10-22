# What transport alone proves at a linear source

Date: 2026-10-20. Status: independently derived local theorem. This concerns a linear source field, not the full IPM linearization or a global Fredholm theorem.

## Statement and spaces

Let A>1 and D=[-S,S]x[-Y,Y] with S,Y>0. Coordinates (s,y) are centered at a positive-axis source. Write T_t(s,y)=(exp(-At)s,exp(-t)y) for t>=0 and

L_A h=A s h_s+y h_y-h.

Functions are odd in y. Fix 0<alpha<1 and an integer m>=1. If f is odd in y and belongs to C^{m,alpha}(D), the equation L_A h=f has an odd C^{m,alpha} solution if and only if f_y(0,0)=0. All such solutions are

h(s,y)=c y+R f(s,y),
R f(s,y)=integral_0^infinity exp(t) f(T_t(s,y)) dt,

where c is arbitrary. The solution R f has (R f)_y(0,0)=0. The inverse on this complement preserves the isotropic derivative order; it is not a gain of one derivative.

For m=1 and R_D=sqrt(S^2+Y^2), component estimates include

|R f(s,y)| <= |y| R_D^alpha [f_y]_alpha/alpha,
||partial_y R f||_infinity <= R_D^alpha [f_y]_alpha/alpha,
||partial_s R f||_infinity <= ||f_s||_infinity/(A-1),
[partial_y R f]_alpha <= [f_y]_alpha/alpha,
[partial_s R f]_alpha <= [f_s]_alpha/(A-1+alpha).

These bounds use the Euclidean Holder seminorm. They do not involve the numerically fitted value of A. On the graph domain {h in C^{m,alpha}:L_A h in C^{m,alpha}}, this gives a local kernel of dimension one and a closed range of codimension one, after fixing parity. Equip the stated domain with the graph norm ||h||_{C^{m,alpha}}+||L_A h||_{C^{m,alpha}}. The operator is closed: convergence of h_n and L_A h_n in C^{m,alpha} implies convergence of L_A h_n to L_A h in C^{m-1,alpha}, so the two limits agree. Thus this is a Banach domain and the local operator is Fredholm of index zero. No boundary data are imposed on the outflow boundary of D.

## Necessity

Oddness gives h(0,0)=f(0,0)=0. On s=0 and y nonzero,

f(0,y)/y=h_y(0,y)-h(0,y)/y.

If h is C^1, the right side tends to h_y(0,0)-h_y(0,0)=0. Since f is differentiable at zero, f_y(0,0)=0. This argument does not differentiate the equation twice.

## Convergence and estimates

Oddness and the fundamental theorem of calculus give

f(s,y)=integral_0^y f_y(s,v)dv.

The compatibility condition and Holder continuity imply |f_y(s,v)| <= [f_y]_alpha (s^2+v^2)^{alpha/2}. Since ||T_t||<=exp(-t),

exp(t)|f(T_t(s,y))| <= |y| R_D^alpha [f_y]_alpha exp(-alpha t).

This integrable majorant proves uniform convergence and the first bound. Differentiating under the integral yields

partial_s R f=integral_0^infinity exp((1-A)t) f_s(T_t X)dt,
partial_y R f=integral_0^infinity f_y(T_t X)dt.

Uniform convergence follows respectively from A>1 and from f_y(0)=0 with Holder continuity. The bounds for supremum norms follow by integration. For two points X,Z in D, their images have distance at most exp(-t)|X-Z|. Applying the Holder difference estimate inside each derivative integral gives the two seminorm bounds. At the origin the y derivative of R f is zero.

For a multi-index beta=(a,b) with a+b>=2, differentiation gives

D^beta R f=integral_0^infinity exp((1-A a-b)t) D^beta f(T_t X)dt.

Here A a+b-1>0. The supremum norm is bounded by ||D^beta f||_infinity/(A a+b-1), and its Holder seminorm by [D^beta f]_alpha/(A a+b-1+alpha). Repeated differentiation is justified by these uniform integrable majorants. This proves the claimed C^{m,alpha} regularity and boundedness without isotropic derivative gain.

## Equation and uniqueness modulo y

For small tau such that the forward source trajectory remains in D, change variables in the integral to obtain

R f(exp(A tau)s,exp(tau)y)
=exp(tau)[R f(s,y)+integral_{-tau}^0 exp(v)f(T_v(s,y))dv].

Its derivative at tau=0 gives L_A R f=f. The formula at boundary points follows by continuity from the interior.

If L_A h=0, integration along backward characteristics gives h(X)=exp(t)h(T_t X). Differentiability at zero and oddness imply h(Z)=c Z_y+o(|Z|). Since exp(t)|T_t X| is bounded for fixed X and T_t X tends to zero, the remainder tends to zero as t tends to infinity. Thus h(X)=c y. Conversely L_A y=0. This proves uniqueness and the dimension of the local kernel. The functional f -> f_y(0) is continuous and nonzero in C^{m,alpha}; the constructive inverse proves its kernel is exactly the range.

## Why a bare C^1 cokernel assertion is insufficient

If both source and target are merely C^1, the single jet condition does not suffice for solvability. On a disc small enough that r=sqrt(s^2+y^2)<1/2, set

f(s,y)=y/log(e/r) for r>0, and f(0,0)=0.

This is odd in y and C^1. Indeed its first derivatives are sums of 1/log(e/r) and bounded angular factors times 1/log(e/r)^2, all tending to zero. In particular f_y(0,0)=0. A C^1 solution would, on the positive y-axis, satisfy

partial_y(h(0,y)/y)=1/[y log(e/y)].

Integration makes h(0,y)/y equal a constant minus log(log(e/y)), which is unbounded as y tends to zero. This contradicts differentiability of h. A Dini modulus for f_y is sufficient for convergence of the resonant integral; the Holder hypothesis in the theorem supplies one. Thus the bare assertion that a C^1 source operator has only one compatibility obstruction omits a necessary function-space issue.

## Exact resonance matters

For the nearby linear field A s partial_s+mu y partial_y, direct calculation gives

(A s partial_s+mu y partial_y-1)y=(mu-1)y.

The y direction is an exact kernel direction only at mu=1. For a normalized exact IPM solution with positive rho_y at a source, the PDE forces mu=1: parity makes DV diagonal on the axis, and comparing first jets at the fixed point in V dot grad(rho)=rho gives mu rho_y=rho_y. This comparison is valid under C^1 regularity of V and rho. A numerical trial with mu approximately one has no such exact transport identity. A claim that its density is an exact transport eigenfunction "up to the residual" is an approximation, not a kernel theorem. The nonlocal IPM coupling can alter this resonance and is absent from the present local model.

## Scope for the team specification

This theorem confirms the linear source's C^{m,alpha} kernel and resonant jet in a well-defined local graph domain. It supplies no global trajectory matching, no whole-plane range theorem, and no result for the full order-zero IPM coupling. It also shows why replacing a failed derivative-gaining inverse with a same-order inverse is a meaningful change of hypothesis. The global assertions F1 and F2 in SPEC v1 remain open or require revision; this local calculation does not validate them.
