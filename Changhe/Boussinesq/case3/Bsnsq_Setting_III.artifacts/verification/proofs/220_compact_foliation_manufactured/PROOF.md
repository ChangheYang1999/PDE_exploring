# A smooth full-plane transport field with the required leading center jets

## Exact statement and scope

There exist smooth real fields Theta,Omega,Psi on R2, with Theta even in x, Omega and Psi odd in x, Theta(0,y)=0, and bounded nonzero Theta, for which beta=2 and the canonical full-plane inverse U=(-Psi_y,Psi_x) satisfy
W=2X+U(X)-U(0), W.grad Theta=0, -Delta Psi=Omega, U(X)=o(|X|).
They also satisfy Theta=x^2+O(|X|^4), Psi_xy(0)=2, and Omega=2x+O(|X|^2), the two required leading center identities at a0=1,beta=2. They do not satisfy the vorticity equation: the coefficient of xy in W.grad Omega+Omega-Theta_x is40. Thus this is a manufactured diagnostic, not a B2 profile or an existence endpoint.

The construction lies in the separable form Theta=H(x/a(y)), but H is constant at sufficiently large argument. It shows that the large-argument Hprime hypothesis in P218 cannot be dropped even when nonzero temperature jet, full-plane canonical inversion, sublinear velocity and both leading center identities are retained. The full vorticity equation remains essential. No conclusion about general smooth beta2 profiles follows.

## Smooth cutoffs and fields

Let rho(t)=exp(-1/t) for t>0 and0 for t<=0. For A<B define chi_(A,B)(s)=rho(B-s)/(rho(B-s)+rho(s-A)). The denominator is strictly positive, since both arguments cannot be nonpositive when A<B. This is smooth, equals1 on s<=A and0 on s>=B. Set
eta(s)=chi_(1,9/4)(s), chi(s)=chi_(4,9)(s),
H(k)=integral_0^(k^2) eta(s) ds.
Then H is smooth, even and bounded, H(k)=k^2 for |k|<=1, and Hprime(k)=2k eta(k^2) vanishes for |k|>=3/2. No evaluation of a divergent cutoff ratio is used.

Let a(y)=sqrt(1+y^2), k=x/a(y),
A(y)=integral_0^y a(s) ds=(y a(y)+asinh(y))/2,
q(y)=4A(y)/a(y)-2y=2asinh(y)/a(y),
Psi(x,y)=chi(k^2)[x q(y)-k^3/3],
Theta(x,y)=H(k), Omega=-Delta Psi, U=(-Psi_y,Psi_x), W=2X+U.
All functions are smooth since a>0. The two terms of Psi are odd in x and chi(k^2) is even. Theta is even and vanishes on x=0. The construction imposes no y-reflection: its Psi contains both an xy term and an x^3 term near the origin. U(0)=0, so the stated W is exactly the B2 relative field for this particular manufactured example. Zero center velocity is a property of this example, not an assumption on the B2 research class.

## Exact temperature transport and divergence

Where Hprime(k) is nonzero, |k|<3/2 and the cutoff chi(k^2) is identically1 in a neighborhood. There Psi=xq(y)-k^3/3. Since k_y=-k a'/a,
U2=q-k^2/a, U1=-xq'-k^3 a'/a.
Differentiating q=4A/a-2y gives q'=2-4Aa'/a^2. Therefore
W2=(4A-k^2)/a,
W1=k a'(4A-k^2)/a=k a' W2.
The derivative of k along W is (W1-k a'W2)/a=0. Hence W.grad Theta=Hprime(k) W.grad k=0 there. Where Hprime(k)=0, grad Theta=0, so transport holds without any condition on the cutoff derivatives. Thus temperature transport holds everywhere. Since U is a rotated gradient, div U=0 and div W=4 identically. The elliptic equation holds by the definition of Omega; canonical inversion is checked separately below.

## Leading jets and explicit vorticity failure

Near0 both cutoffs are constant1 and H(k)=k^2. Taylor expansion gives
Theta=x^2/(1+y^2)=x^2-x^2y^2+O(|X|^6),
q(y)=2y-(4/3)y^3+O(y^5),
Psi=2xy-x^3/3-(4/3)xy^3+(1/2)x^3y^2+O(|X|^6).
Consequently Psi_xy(0)=2, U(0)=0 and Omega_x(0)=2. To determine the residual at degree2 it suffices to use
Omega=2x+8xy+O(|X|^3), W1=O(|X|^3), W2=4y-x^2+O(|X|^3), Theta_x=2x+O(|X|^3).
It follows that W.grad Omega+Omega-Theta_x=32xy+8xy+O(|X|^3)=40xy+O(|X|^3). In particular the exact mixed derivative of this residual at0 is40, so the vorticity equation fails. These center expansions are analytic in a neighborhood of0, irrespective of the finite-cutoff transition away from0. No numerical residual floor is involved.

## Far field and canonical full-plane inverse

The support of Psi is contained in |x|<=3a(y). For large |X| in that set, |y| is comparable to |X| and |k|<=3. The elementary bounds q=O(log(2+|y|)/|y|), q'=O(log(2+|y|)/|y|^2) and q''=O(log(2+|y|)/|y|^3) follow by differentiating asinh(y)/sqrt(1+y^2). Derivatives of k of orders1 and2 are O(|y|^-1) and O(|y|^-2), respectively, uniformly for bounded k. The cutoffs and all derivatives on the bounded k interval are bounded. Product differentiation yields
Psi=O(log(2+r)), U=O(log(2+r)/(1+r)), Omega=O(log(2+r)/(1+r)^2), r=|X|.
Outside the support the same bounds hold trivially. Thus U tends to0 and is sublinear, and Omega is smooth and bounded everywhere.

For the stated sign convention the velocity kernel is K(Z)=(Z2,-Z1)/(2pi|Z|^2). Define V(X)=integral_R2 K(X-Y) Omega(Y) dY. The integral is locally absolutely integrable because K has an integrable inverse-distance singularity and Omega is bounded. It converges absolutely at infinity, where its radial majorant is a constant times log(r)/r^2. A stream-function integral need not converge; only this velocity integral is used.

For R=|X| large, split the integral into |Y|<=R/2, R/2<|Y|<2R, and |Y|>=2R. The first part is O(log(2+R)^2/R), since the integral of |Omega| over that disk is O(log(2+R)^2). On the middle annulus |Omega|=O(log R/R^2), and the integral of |X-Y|^-1 over a disk of radius3R is O(R), giving O(log R/R). The far part is O(log R/R). Thus V(X) tends uniformly to0.

The fundamental solution -log|Z|/(2pi) gives div V=0 and curl V=-Omega in distributions, with curl V=partial_x V2-partial_y V1. Local convolution with the smooth source and its compactly supported local cutoff gives smoothness, while the tail and its differentiated kernels converge locally uniformly. Equivalently the local potential equation gives the same smooth representative. U has those same divergence and curl identities. Hence each component of D=V-U is harmonic on R2. It tends to0 and is bounded. The mean-value derivative estimate on a disk of radiusR, |grad D(X)|<=C sup|D|/R, obtained by differentiating the Poisson formula, gives grad D=0 after R tends to infinity. Thus D is constant and its limit makes it zero. Therefore the constructed U is exactly the absolutely convergent full-plane canonical inverse, with no added harmonic strain or uniform velocity.

## Dependencies and verification

The proof uses calculus, the displayed smooth cutoff, the fundamental solution of the planar Laplacian and the bounded harmonic mean-value argument supplied above. P218 is needed only to explain which hypothesis this example tests, not to prove the construction. The B2 formulas are fixed by PROMPT. This complete informal proof is written before the checker. Planned verification is independent symbolic differentiation of the uncut core, exact center coefficients and cutoff-support logic, plus actual Opus5.5 adversarial review. No Lean/Lake, server, GPU or external solver is used. This example is a manufactured test and its vorticity residual is exactly nonzero.
