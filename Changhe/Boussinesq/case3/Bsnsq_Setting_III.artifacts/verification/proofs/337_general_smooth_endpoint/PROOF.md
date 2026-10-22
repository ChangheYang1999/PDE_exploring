# Smooth temperature factorization at every simple hyperbolic endpoint

Prepared 2026-10-22T09:54:38.093732+00:00, before controls. This extends P334 as a conditional theorem for actual smooth fields. It supplies no actual profile or convergence theorem.

## Exact local statement and notation
Let W=(x a(x,u),P(x,u)) be a real C-infinity vector field near (0,0), with a and P even in x. Let A>0, kappa>0 and lambda>=0 satisfy 2A-lambda>0, and assume

    a(0,0)=A, P(0,0)=0, P_u(0,0)=-kappa, k=P_xx(0,0)/2.

Let Theta be real, smooth and even in x, satisfying W Theta=lambda Theta. If lambda=0 assume Theta(0,0)=0; for lambda>0 no extra zero-axis assumption is needed. Assume F_axis(u)=Theta_xx(0,u)/2 is not identically zero on (0,delta) or on (-delta,0), with delta chosen inside the interval where the smooth positive p and smooth rho used below are defined. Scalar ODE uniqueness makes this equivalent to being nonzero throughout that half-interval.

Then n=(2A-lambda)/kappa is a positive integer. There is a unique nonzero real C_u such that F_axis(u)=(C_u/2)u^n R(u), with R smooth, positive near0, R(0)=1. The uniqueness here is of C_u and of the unit R supplied by the scalar axis equation. As local germs:

1. The local unstable manifold is an even smooth graph u=H(x), H(0)=H'(0)=0, with H(x)=k x^2/(2A+kappa)+O(x^4).
2. There is exactly one smooth function Z normalized by Z_u(0,0)=1 such that Theta=(C_u/2)x^2 Z^n. It has the form Z=(u-H(x))L with L even in x, smooth, strictly positive, L(0,0)=1.
3. WZ=((lambda-2a)/n)Z. If n is even, I=xZ^(n/2) is smooth and odd, WI=(lambda/2)I, and Theta=(C_u/2)I^2. It is a first integral only when lambda=0.
4. In a sufficiently small neighbourhood, the zero set of Theta is exactly the union of the axis and u=H(x). At x!=0 on the graph its transverse vanishing order is exactly n. Off these curves its sign is sign(C_u) sign(u-H(x))^n. Thus even n gives the sign of C_u on both sides, while odd n gives a sign change across the unstable graph. No assertion of a global sign is made.
5. The zero of T=Theta_xx(0,u) at u=0 is isolated on the axis: T is nonzero on both punctured sides, and its signs differ by (-1)^n. In particular an actual smooth solution with a nonzero incoming axis coefficient cannot extend T by zero immediately beyond this simple endpoint.

The hypothesis requires an actual solution of the PDE on a neighbourhood. A formal transverse hierarchy is insufficient, as the explicit flat example in P334 shows. The integer n is derived, not an assumed freely chosen exponent.

## Axis vanishing and the forced integer
On x=0 the equation is P(0,u)Theta_u(0,u)=lambda Theta(0,u). Write P(0,u)=-kappa u p(u), p smooth, p(0)=1 and positive near0. If lambda>0, a nonzero solution on a half-interval is a nonzero constant times |u|^(-lambda/kappa) times a smooth positive unit. Indeed its logarithmic derivative is -lambda/(kappa u)+rho_0(u), where rho_0 is smooth by division of p(u)-1 by u. This diverges at0, contrary to smoothness. Thus Theta(0,u)=0 on both sides and at0; directly at the origin the equation also gives lambda Theta(0,0)=0. If lambda=0 it is constant on each side and continuity and Theta(0,0)=0 make both constants zero.

Evenness gives Theta_x(0,u)=0. Taylor's integral formula gives Theta=x^2 F, with smooth even F and F(0,u)=F_axis(u). Divide the equation for x!=0 and extend by continuity:

    x a F_x+P F_u+(2a-lambda)F=0.

On the axis this gives

    F_axis'/F_axis = (2a(0,u)-lambda)/(kappa u p(u)) = n/u + rho(u)

where rho is smooth, whenever F_axis is nonzero. The equation itself can be used without division: if R(u)=exp(integral_0^u rho(v)dv), then Q=F_axis/R satisfies u Q'=n Q. On each punctured side Q is c_+ u^n or c_- |u|^n, including the zero solution; ordinary ODE uniqueness shows that a nonzero value makes that side nonzero throughout. If n is not an integer, the derivative of order ceil(n) of a nonzero multiple of |u|^n diverges at0, contradicting smoothness. Thus n is a positive integer. The derivatives of order n from both sides agree, forcing c_-=(-1)^n c_+. At least one is nonzero, hence both are, and C_u=2c_+!=0. We obtain the exact two-sided formula F_axis=(C_u/2)u^n R(u), including0, with R(0)=1. This proves the integer and coefficient assertions without borrowing a formal jet.

## The unstable graph and its curvature
The linearization of W is diag(A,-kappa). Apply the smooth local stable-manifold theorem to -W, with stable x direction, unstable u direction, and gamma=-A/2. The exact dependency is Dutilleul Theorem1.1, PDF and extracted text pinned in P334 sources. A reflection-symmetric smooth cutoff extends the local field without changing its germ. The theorem identifies one smooth graph with the set of trajectories remaining small and decaying faster than exp(gamma t). Reflection preserves this set, so the graph is even. Its invariance equation is

    P(x,H(x))=x a(x,H(x))H'(x).

Every sufficiently small invariant C1 graph tangent to x has a>3A/4 along it. For -W, |x(t)|<=|x(0)|exp(-3At/4); its u coordinate is O(|x|), so it belongs to the same gamma-stable graph. This proves germ uniqueness with the theorem's exact stable-set definition. At degree two write H=h2 x^2+O(x^4). The equation gives k-kappa h2=2A h2, so h2=k/(2A+kappa).

## Actual transverse divisibility
Use coordinates q=u-H(x), and restrict to a symmetric box in (x,q), so that every segment used below lies in the domain. Invariance and smooth Taylor division put the field in the form

    W=x alpha(x,q) partial_x+q d(x,q) partial_q,
    alpha(0,0)=A, d(0,0)=-kappa.

Let f(x,q)=F(x,q+H(x)). Then

    x alpha f_x+q d f_q+(2alpha-lambda)f=0.

Set f_j(x)=partial_q^j f(x,0)/j!. If f_0,...,f_(j-1) vanish as functions, differentiation gives

    x alpha(x,0) f_j'(x)+(2alpha(x,0)-lambda+j d(x,0))f_j(x)=0.

Terms involving lower derivatives vanish identically, including their x derivatives. For j<n, division by alpha gives x f_j'=-b_j(x)f_j with b_j(0)=kappa(n-j)/A>0. Shrink once for the finitely many j<n so every b_j>=delta>0. A nonzero solution for x>0 obeys

    |f_j(x)|=|f_j(x0)| exp(integral_x^x0 b_j(t)/t dt)
              >=|f_j(x0)|(x0/x)^delta,

contrary to boundedness at0. The change x=-v proves the same on the other half-axis. Scalar ODE uniqueness and continuity finish the zero assertion. Induction proves f_0=...=f_(n-1)=0 as actual smooth functions, excluding nonzero flat-in-x exceptions at these orders.

Taylor's formula in q gives

    f=q^n K,
    K(x,q)=1/(n-1)! integral_0^1 (1-t)^(n-1) partial_q^n f(x,tq)dt.

K is smooth and even. At x=q=0 the axis calculation gives K=C_u/2. Hence 2K/C_u is positive near0 and has a unique positive smooth nth root with value1. Define Z=(u-H(x))(2K(x,u-H(x))/C_u)^(1/n). This proves factorization, parity, normalization, the exact local zero set and all sign/order conclusions.

## Transport and uniqueness of the factor
Differentiate Theta=(C_u/2)x^2 Z^n in WTheta=lambda Theta:

    (C_u/2)x^2 Z^(n-1)[n WZ+(2a-lambda)Z]=0.

On xZ!=0 cancel nonzero real factors; the complement is two smooth curves and has empty interior, so continuity proves the displayed transport formula everywhere. For even n, the product rule gives WI=[a+(lambda-2a)/2]I=(lambda/2)I. If another normalized smooth factor existed, equality of nth powers at x!=0 gives equality of absolute values, also on the axis by continuity. Both vanish on the same graph, and their u derivatives are positive after shrinking, so both have sign q. They are equal. No cancellation in the ring of smooth germs is used. Take one finite intersection of the graph, nonzero-axis, hierarchy, positive-unit and positive-Z_u neighbourhoods; all asserted identities then hold on that one fixed neighbourhood.

## Transfer to Boussinesq B2 and orientation
For an actual C-infinity B2 profile at beta>=2, put lambda=beta-2. At a simple endpoint y_* of the component J on which T(y)=Theta_xx(0,y) is nonzero, assume b(y_*)=0 and b'(y_*)=-kappa<0, where b(y)=W2(0,y). The prompt parity of Psi gives W1 odd and W2 even in x; div W=2beta. In SIGNED coordinates u=y_*-y, set P=-W2. Then a(0,0)=2beta+kappa=A, P_u=-kappa, k=-partial_x^2 W2(0,y_*)/2. The integer above is

    n=2+(3beta+2)/kappa,
    H(x)=k x^2/(4beta+3kappa)+O(x^4).

Here 2A-lambda=3beta+2+2kappa>0. The nonzero-axis condition follows from the definition of J; the prompt already imposes Theta(0,y)=0. This proof needs no global inverse or vorticity equation to derive its local necessary condition. Their other restrictions remain mandatory for a profile.

The coefficient C in Section4.53 of the lead report is defined with the UNSIGNED distance s=|y-y_*|, on J, and has sign A_report=2a0. It must not silently replace C_u. With epsilon=sgn(y_*) and u=y_*-y, points of J near the endpoint have u=epsilon s, so C_u=epsilon^n C. Thus C_u=C at a positive endpoint and C_u=(-1)^n C at a negative endpoint. There is no additional factor2: the report has T=C s^n(1+O(s)), while here F_axis=T/2=(C_u/2)u^n R(u). One may instead choose the interior-oriented coordinate u_in=epsilon(y_*-y), in which the leading coefficient is C, but then P_in=-epsilon W2 and k_in=-epsilon partial_x^2 W2/2. Every sign and graph statement must use its declared coordinate. If the endpoint belongs to another component rather than the central J, use its actual occupied side to determine epsilon; the abstract local theorem is unchanged.

At beta=2 and kappa=1, n=10 and the result recovers P334. For even n at beta>2 the smooth odd I has eigenvalue(beta-2)/2; it is not transported unchanged. For odd n the sign-change conclusion concerns the unstable graph, not crossing the axis. Formal data, local thermal manufactures and actual full-plane B2 profiles remain distinct. General B2 remains OPEN.

The nonzero-axis hypothesis cannot be dropped. For A=5,kappa=1,lambda=0 and W=(5x,-u), define E=exp(-1/(x^2 u^10)) away from the two axes and E=0 on them. The positive denominator x^2u^10 has W-derivative0, so WE=0 off the axes and then everywhere by continuity. Every fixed derivative is a finite sum of inverse powers of x,u times E; write t=x^2u^10 and restrict |x|,|u|<=1. For each inverse monomial |x|^(-a)|u|^(-b), choose an integer m>=max(a/2,b/10); then it is at most t^(-m), and t^(-m)exp(-1/t) tends to0 as t tends to0. Thus every derivative extends continuously by0 at both axes, including their intersection. For each coordinate direction, the fundamental theorem of calculus on segments, split at a crossed axis, identifies a continuous extension of a derivative with the derivative of the extended function. Inducting on derivative order proves smoothness and flatness on both axes, one of which is the unstable graph u=0. Thus E is an actual nonzero smooth transported function with F_axis identically zero and no normalized factor with a nonzero finite C_u. This differs from P334's exp(-1/x^2) perturbation, which deliberately fails the actual PDE. Neither is a full B2 profile.

No JavaScript/TypeScript, servers/listeners/tunnels, RLScience cluster, Lean/Lake builds, GitHub posting or human contact. Write only inside verification.
