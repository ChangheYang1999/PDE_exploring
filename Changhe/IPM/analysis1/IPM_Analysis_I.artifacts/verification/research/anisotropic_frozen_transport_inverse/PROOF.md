# An explicit inverse for the frozen transport operator in a logarithmic axis-weighted space

Date 2026-10-22T02:40:23.998244+00:00. This proof is written before the exact scalar application. The theorem and modal-parameter application remain OPEN pending independent checks, actual Claude Opus5.5 review and later own adjudication. This is a frozen local operator result, not an inverse for the full IPM linearization.

## Space, operator and theorem

Let alpha be real, beta>0, a real, and s>=0. On the half-plane x>0, y in R, define T_a h(z,y)=exp((1/2-a)z)h(exp(z),y), z=log x. Define Y_(a,s) as the distributions for which T_a h belongs to the inhomogeneous Fourier Sobolev space H^s(R^2_(z,y)), with norm ||h||_Y=||T_a h||_(H^s). The Fourier convention is unitary and the norm squared is integral(1+xi_z^2+xi_y^2)^s |g_hat(xi)|^2 dxi. Equivalently, Y is the isometric pullback of H^s under T_a; this defines a complete Hilbert space. Its zeroth-order contribution is exactly integral_(x>0) x^(-2a)|h(x,y)|^2 dxdy.

Consider A h=alpha x partial_x h+beta y partial_y h-h. Give it the maximal distributional domain

 D(A)={h in Y: A h in Y as a distribution on x>0}.

Put delta=alpha(a-1/2)+beta(s-1/2)-1. Then A is a closed, densely defined generator on Y. Its semigroup for t>=0 is

 S_h(t)h(x,y)=exp(-t)h(exp(alpha t)x,exp(beta t)y),

and ||S_h(t)||_(Y->Y)<=exp(delta t). If delta<0, then A:D(A)->Y is bijective and

 A^(-1)f=-integral_0^infinity S_h(t)f dt,
 ||A^(-1)f||_Y <= (-delta)^(-1)||f||_Y.                       (1)

The integral converges in Y. The same statements hold on the closed odd-in-y subspace, with the corresponding domain. No regular extension across x=0 is asserted, and no nonlocal IPM term is part of A.

For the exactly normalized modal central coefficients, let ell=1/k with the exact stored positive dyadic k from the canonical construction, alpha=1-2ell and beta=4ell-1. Take a=6, s=153/50 and mu=a+s-1=403/50. Define d=beta-alpha and

 p=(beta mu-1)/d, q=(1-alpha mu)/d.

The arithmetic application must independently prove beta>0, d>0, delta<0 and enclose the inverse ceiling(-delta)^(-1). It must also check the exact identities

 p+q=mu, alpha p+beta q=1,
 p-(a-1/2)=delta/d, q-(s-1/2)=-delta/d.                      (2)

Thus the proposed homogeneous solution x^p sign(y)|y|^q of A h=0 fails even the zeroth-order Y integrability near x=0 wherever y stays in a nonzero compact interval. This reconciles that candidate with the inverse (1); it is not an element of the inverse's domain. No scalar decimal is asserted before the new exact checks.

## Conjugation and the semigroup estimate

Set nu=1/2-a and g=T_a h. Direct differentiation gives

 T_a A T_a^(-1)g=P g=alpha partial_z g+beta y partial_y g+c g,
 c=alpha(a-1/2)-1.

The explicit pullback semigroup on H^s is S(t)g(z,y)=exp(c t)g(z+alpha t,exp(beta t)y). It satisfies S(t+u)=S(t)S(u) and S(0)=Id. Its Fourier transform is

 S(t)g_hat(xi_z,xi_y)=exp((c-beta)t)exp(i alpha t xi_z)
                      g_hat(xi_z,exp(-beta t)xi_y).

Changing variable eta_y=exp(-beta t)xi_y gives

 ||S(t)g||_(H^s)^2=exp((2c-beta)t)integral
   (1+xi_z^2+exp(2beta t)eta_y^2)^s |g_hat(xi_z,eta_y)|^2 dxi_z deta_y.

Since beta>0,t>=0,s>=0,

 (1+xi_z^2+exp(2beta t)eta_y^2)^s
 <=exp(2s beta t)(1+xi_z^2+eta_y^2)^s.

This proves ||S(t)||<=exp((c+beta(s-1/2))t)=exp(delta t). Translation in z contributes no growth. For Schwartz g, continuity at t=0 in H^s follows by dominated convergence in this explicit Fourier formula, with t restricted to a compact interval. Schwartz functions are dense in H^s, and the bound is uniform on compact t intervals, so S is strongly continuous on H^s. Conjugation proves the asserted physical-space formula and bound on Y. Reflection y->-y commutes with S, so the odd subspace is closed and invariant.

## The generator and its maximal domain

On Schwartz functions the strong derivative at0 is P=alpha partial_z+beta y partial_y+c. Thus the generator domain is dense. Its distributional action agrees with P on every generator-domain element, by differentiating pairings with Schwartz test functions in the explicit pullback formula.

Conversely, let g in H^s and Pg=f in H^s distributionally. Pair S(t)g with a Schwartz test function, change variables in z,y, and differentiate the resulting smooth test function. The formal distributional adjoint is P^*=-alpha partial_z-beta y partial_y+(c-beta). This gives d/dt S(t)g=S(t)f in distributions, and hence

 S(t)g-g=integral_0^t S(u)f du.                              (3)

The right side is a Bochner integral in H^s. Both sides represent the same distribution and belong to H^s, so (3) holds in H^s. Divide by t and use strong continuity to obtain the generator derivative f. The generator domain is therefore exactly the maximal distributional domain. This argument does not require an unproved core theorem or an assumption about the range.

Closedness can also be seen directly from(3): if g_n->g and Pg_n->f in H^s, pass to the limit in(3) by the semigroup bound. Divide by t at0 to conclude g is in the maximal domain with Pg=f. Conjugation transfers this closedness and domain description to A on Y.

## Proof of the inverse

If delta<0, Gf=integral_0^infinity S(t)f dt converges in H^s and has norm at most(-delta)^(-1)||f||. The semigroup law gives

 (S(h)Gf-Gf)/h=-(1/h)integral_0^h S(t)f dt -> -f

as h decreases to0. Thus Gf is in D(P) and PGf=-f. For g in D(P), equation(3) and its derivative give integral_0^T S(t)Pg dt=S(T)g-g. The semigroup bound makes S(T)g tend to0, so GPg=-g. Therefore -G is both a left and right inverse. This proves bijectivity and(1), with no independent invertibility theorem needed. The same proof on the invariant odd subspace uses the same bound.

## Why the candidate is outside the space

The homogeneous candidate H=x^p sign(y)|y|^q satisfies A H=(alpha p+beta q-1)H=0 wherever xy is nonzero. From mu=(a-1/2)+(s-1/2), direct algebra gives

 d[p-(a-1/2)]=beta mu-1-(beta-alpha)(a-1/2)=delta.

The remaining identities in(2) follow. With delta<0 and d>0, p<a-1/2. Take a smooth cutoff that is identically1 when0<x<epsilon and y lies in a fixed positive compact interval[y0,y1]. There |H| is bounded below by a positive constant times x^p. Its zeroth-order weighted square integral dominates

 const integral_0^epsilon x^(2p-2a)dx.

Since2p-2a<-1, this diverges. Thus even the cutoff candidate is outside Y. This is an actual lower-bound nonmembership argument, not a regularity conclusion drawn from an upper bound. It covers the stated anisotropic model only, not every conceivable axis-weighted space.

## Scalar application, dependencies and limits

The exact normalized trial has ell=1/k and central matrix diag(alpha,beta) for V=ell X+U[rho], by the accepted canonical center construction and its normalization. Recheck the complete parent higher_center_weight_quasimodes verdict and its pins before accepting this application. The k input is an exact dyadic parameter; the rounded outer-density exponent of a separate literal stored trial is irrelevant here.

One scalar path will decode the NPZ k with Fraction and evaluate the exact rational formulas with Arb512. The other will decode the canonical JSON hexadecimal string using integer arithmetic, independently derive the symbolic identities, and evaluate with iv220. All intervals and any displayed directed ceilings must be checked by exact rational comparisons. The infinite-time semigroup estimate, domain equality, Bochner inverse and nonmembership arguments are analytic, not inferred from these scalar checks.

This theorem supplies only the frozen constant-coefficient central transport inverse in the explicitly defined global logarithmic model. It does not bound variable-coefficient errors, the canonical nonlocal perturbation, the strain term, the full operator's domain, the nonlinear map, far-field constraints, distance to X3 or any a posteriori closing inequality. In particular, preservation of this strong axis-weighted space by the full IPM linearization is a separate open requirement. No contradiction with the proved same-X_m quasimodes in radial center weights is asserted, and no decisive PDE endpoint follows.
