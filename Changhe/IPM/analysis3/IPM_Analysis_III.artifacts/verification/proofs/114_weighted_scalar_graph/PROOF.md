# Endpoint weights and the fractional scalar graph domain

## Exact scalar space

Use the actual axis operator

 A beta=d beta'+b beta, b=D-d-2d', D=4ell-1, ell=1/k,
 k=1615536043799051/9007199254740992.

The low domain B and its free coefficient J are those of proof 38. The actual d is bounded above and below by positive constants. Set sigma=25/4, delta=9/5 and gamma=-1/2. Choose smooth positive a(t), equal exp(delta t) for t<=0 and exp((gamma-3)t) for t>=1. Choose a smooth cutoff chi(t), equal1 for t<=0 and0 for t>=1. Define

 Gamma_H={f:a^(-1)f in H^sigma(R)},
 B_H={beta in B:A beta in Gamma_H},
 ||beta||_(B_H)^2=||beta||_B^2+||a^(-1)A beta||_(H^sigma)^2. (1)

Then Gamma_H is continuously included in the low target Gamma, A:B_H->Gamma_H is an isomorphism, and

 ||beta||_(B_H) is equivalent to
       |J|+||a^(-1)(beta-J chi)||_(H^(sigma+1)).           (2)

All constants are finite and depend only on the fixed cutoffs and actual coefficient bounds. No numerical inverse constant is asserted.

The same statement holds for1/4<delta<2 and gamma<-3/8, provided gamma<k. The latter follows for the present negative gamma and positive k.

## Why the old scalar weight is insufficient

Let G^sigma be the old exponential-weight Sobolev target of proof 113. Choose lambda=1/2 and a smooth cutoff chi_- supported in t<0, equal1 for t<=-1. Put beta(t)=exp(lambda t)chi_-(t). Then beta belongs to B, has J=0, and A beta belongs to G^sigma for every finite sigma. Indeed its inner weighted squared exponent is2lambda-1/2>0 and it vanishes at the outer end.

For the actual field, the remainder of its transport lift has the leading form

 Err beta / (x^2 y)=-Sigma lambda cos(theta)^2 r^lambda+o(r^lambda),
 Sigma=(2ell-1)+(4ell-1)>0.

On an angular patch where cos(theta) is nonzero, division by a gives r^(lambda-delta), which is not square-integrable in dt. Thus matching the fractional order without matching the origin weight does not give the required high remainder mapping. The renormalized coupling has cofactor O(r^2) for this beta, by its exact finite-mode moments and the cancellation of the leading cubic term; it cannot cancel the displayed r^lambda contribution. Therefore the full lower block also fails this stronger endpoint membership for the old scalar space.

## Actual coefficient regularity

The original exact-join density has finitely many angular modes with C6 radial coefficients and bounded piecewise-analytic derivatives on the finite knot interval. Its x derivative has C5 coefficients. The radial Green equation makes each stream-function coefficient C7, so the radial velocity and its divided axis coefficients are at least C6, with bounded one-sided derivatives of every fixed order. In particular d is in W^(7,infinity) locally, while p=b/d is in W^(6,infinity) locally. The positive lower bound on d permits division.

At both endpoints the differentiated modal formulas of proof 52 give

 d-D=O(exp(2t)), p=O(exp(2t)) at negative infinity,
 d-ell=O(exp(-(1-k)t)), p-(3-k)=O(exp(-(1-k)t)) at positive infinity,

with every fixed number of t derivatives needed here. Consequently d, 1/d and p have bounded derivatives through the integer orders just stated. Subtract fixed smooth functions with their respective endpoint constants. The remaining coefficients belong to H^sigma: their sixth weak derivatives are piecewise Lipschitz with finitely many jumps and decay exponentially at both ends. The fractional difference estimate in proof 113 applies because sigma-6=1/4<1/2.

## The weighted L2 step

Since delta>1/4 and gamma<-3/8, multiplication by a maps H^sigma continuously into the old weighted L2 target. The low inverse A^(-1) therefore defines beta in B for every f in Gamma_H and bounds its J. Write H for the low integrating factor and z=beta/H. At the inner end,

 beta-J=J(H-1)+H integral_(-infinity)^t f(s)/(d(s)H(s)) ds. (3)

Here H-1=O(exp(2t)), so its quotient by a is square-integrable because delta<2. After division by a, the integral in (3) is bounded by a convolution kernel C exp(-delta u), u>=0, acting on f/a. Its L1 norm is finite. This proves the weighted L2 bound at that end.

At the outer end the low future formula gives

 beta(t)=-H(t) integral_t^infinity f(s)/(d(s)H(s)) ds.      (4)

Since H is comparable to exp((k-3)t), division by a bounds this by the future convolution kernel C exp(-(k-gamma)u), u>=0. It is integrable because gamma<k. Compact intervals are controlled by the low inverse and the equation. Thus v=(beta-J chi)/a belongs to L2, with its norm bounded by ||f/a||_(H^sigma).

## Fractional bootstrapping and the converse

The equation for v is

 v'=d^(-1)(f/a)-[p+a'/a]v-J(p chi+chi')/a.                (5)

The last fixed coefficient belongs to H^sigma. Its inner decay is exp((2-delta)t); at the outer end it vanishes. The multiplier a'/a is smooth with bounded derivatives, and p has the regularity just checked.

Starting with v in L2, the integer product estimates in (5) give successively v in H1,...,H7, because f/a is in H6 and p has six bounded weak derivatives. For the final quarter derivative, p and d^(-1) are smooth endpoint steps plus H^sigma functions. The H^sigma multiplication inequality in one dimension applies since sigma>1/2; it follows directly from weighted Fourier convolution and the L1 bound on the Fourier transform. As v is already in H7, every term on the right of (5) belongs to H^sigma. Hence v belongs to H^(sigma+1), with a bounded norm. This proves the forward estimate in (2).

Conversely, for any J real and v in H^(sigma+1), define beta=J chi+a v. Its endpoint powers put beta in the low B domain, with the prescribed coefficient J. Substitution in (5) proves A beta/a in H^sigma and bounds its norm. This proves the reverse estimate. Completeness follows from either the graph definition or this norm equivalence. The low inverse gives both injectivity and surjectivity of A on the specified high spaces.

## Scope

The endpoint and fractional-order issues of the scalar domain are resolved for the explicit space (1). The space has a free classical cubic coefficient; it does not impose J=0. A separate finite-codimension normalization restriction would change the low index and is not used here. The mapping of the lower block and the high remainder inverse are separate questions.
