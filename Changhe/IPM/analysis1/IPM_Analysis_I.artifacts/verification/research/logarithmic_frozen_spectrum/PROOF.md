# Complete frozen-transport inverse classification in the logarithmic axis space

Date 2026-10-22T03:19:35.416063+00:00. Standalone informal proof written before new symbolic or exact scalar checks. Status OPEN pending independent checks, complete actual Claude Opus5.5 review and later own adjudication. This result concerns a precisely specified global frozen transport operator, not the full IPM linearization.

## Space, domain and exact statement

Let A>0, D=2A+1, s>=0 and a real. On x>0,y in R define the Hilbert space Y_(a,s) by the isometry

 (T_a h)(z,y)=exp((1/2-a)z)h(exp z,y)

onto the inhomogeneous Fourier Sobolev space H^s(R^2). The Fourier transform is unitary, with the convention partial_z corresponds to i xi and partial_y to i eta. Its squared norm is integral(1+xi^2+eta^2)^s |Fhat(xi,eta)|^2 dxi deta. This is exactly the space of anisotropic_frozen_transport_inverse; no physical boundary condition at x=0 or y=0 is added. Work first over complex scalars. The real and odd-in-y restrictions are addressed below.

Give T=-A x partial_x+D y partial_y-1 its maximal distributional domain D(T)={h in Y:Th in Y}. Define

 c=-A(a-1/2)-1,
 d_minus=c-D/2=-Aa-(A+3)/2,
 d_plus=d_minus+Ds.

Then T is closed and densely defined, and has the following complete classification.

1. If d_plus<0 or d_minus>0, T:D(T)->Y is bijective. Its inverse norm in the base Y norm is EXACTLY

 1/dist(0,[d_minus,d_plus]).                              (1)

The inverse is the forward-time integral in the first case and the negative-time integral in the second case.

2. If d_minus<0<d_plus, T is injective and its range has infinite-dimensional orthogonal complement. In particular it is not surjective and is not Fredholm.

3. If0 is an endpoint of[d_minus,d_plus], including the single-point interval when s=0, T is injective and has dense, nonclosed range. It has no bounded inverse and is not Fredholm.

These statements also hold on the closed odd-in-y subspace, and on the corresponding real spaces. Thus T has an inverse IF AND ONLY IF0 lies outside the closed interval[d_minus,d_plus]. The spectrum on the complex space is the closed vertical strip {lambda:d_minus<=Re(lambda)<=d_plus}, with empty point spectrum. The spectral statement follows from exactly the same proof with a scalar real shift and an elementary phase; it is not an extra hypothesis.

For the canonical exact dyadic k, A=2/k-1>3. For every a>=0 one has d_minus<0. Hence within nonnegative a weights, frozen invertibility is equivalent to d_plus=delta_Y<0. Combining the exact threshold identity from forward_axis_weight_threshold, every such inverse with s>=3/2 has a>5/2. The accepted compact test from axis_weighted_nonlocal_mapping therefore has full IPM image outside that Y, and the actual canonical residual is also outside that Y by canonical_axis_residual. This is a statement about these spaces and the applicability of this frozen-model route. It does NOT transfer model noninvertibility at other weights to the full variable or nonlocal operator.

## An explicit unitary reduction

The logarithmic conjugation gives

 P=T_a T T_a^(-1)=-A partial_z+D y partial_y+c.

Its group is S(t)F(z,y)=exp(c t)F(z-A t,exp(Dt)y), t in R. The accepted proof anisotropic_frozen_transport_inverse identifies its generator with the maximal distributional domain by test-function pairings. The same pairings apply for both signs of t. Strong continuity follows from the Fourier formula, first on Schwartz functions and then by density and bounds on compact time intervals.

On Fourier transforms,

 (S(t)F)hat(xi,eta)=exp((c-D)t)exp(-iA xi t)Fhat(xi,exp(-Dt)eta).

Split eta into its positive and negative half-lines. The excluded line eta=0 has measure zero. Put

 ell(xi)=(1/2)log(1+xi^2), tau=log|eta|-ell(xi),
 eta=sign*sqrt(1+xi^2)*exp(tau),
 W(xi,tau)=[|eta|(1+xi^2+eta^2)^s]^(1/2),
 V_sign(xi,tau)=exp(i A xi tau/D)W(xi,tau)Fhat(xi,eta).     (2)

For each sign this is a unitary change from the corresponding weighted Fourier half-plane onto L2(dxi dtau), since d eta=|eta|d tau. Both the positive factor and the phase in(2) are explicit. The inverse formula reconstructs Fhat almost everywhere; together the two copies exhaust H^s.

Using the group formula in(2), the phase exp(-iA xi t) is canceled by the change tau->tau-Dt. The ratio W(xi,tau)/W(xi,tau-Dt) is

 exp(Dt/2)[(1+exp(2tau))/(1+exp(2(tau-Dt)))]^(s/2).

Therefore the transformed group, on either copy, is

 (G(t)V)(xi,tau)=exp(integral_0^t d(tau-Du)du)V(xi,tau-Dt),
 d(tau)=d_minus+sD exp(2tau)/(1+exp(2tau)).                 (3)

The generator is

 Q=-D partial_tau+d(tau),                                (4)

independent of xi. This proves the reduction at the group level, not merely by formal differentiation away from eta=0. In particular no hidden matching condition across eta=0 is being assumed. The original group acts on the entire weighted L2 Fourier space and the transformation is onto its two-copy representation.

The real bounded smooth function d lies between d_minus and d_plus. The generator domain of(3) is exactly {V in L2:partial_tau V in L2 distributionally}. To see it directly, distributional differentiation gives Q; conversely the test-function-pairing identity G(t)V-V=integral_0^t G(u)QV du proves membership in the generator domain whenever QV in L2. Because d is bounded, QV in L2 is equivalent to partial_tau V in L2. Thus the maximal domain has been identified without imposing an endpoint condition in tau. Closedness and density also follow: -D partial_tau has its usual closed maximal L2 domain by the unitary Fourier transform in tau, and multiplication by d is bounded. Smooth compact functions of xi,tau are a dense subset of this domain's ambient Hilbert space.

The adjoint on either copy is

 Q*=D partial_tau+d(tau)

on the same derivative domain. This follows from the Fourier characterization of the adjoint of partial_tau and the bounded real multiplication operator, not from an unproved formal boundary cancellation.

## Kernel and obstruction in the interior strip

A distributional solution QV=0 is locally H1 in tau. By Fubini it solves the scalar ODE for almost every xi, and therefore has the form

 V(xi,tau)=C(xi) M(tau),
 M(tau)=exp(d_minus*tau/D)(1+exp(2tau))^(s/2).             (5)

The ODE follows by differentiation of M; the constant factor in M is immaterial. At minus infinity M is comparable to exp(d_minus*tau/D), and at plus infinity it is comparable to exp(d_plus*tau/D). Square integrability would require d_minus>0 AND d_plus<0. This is impossible because d_plus>=d_minus. Equality at an endpoint also fails square integrability, since the corresponding asymptotic is a nonzero constant. Thus ker(Q)=0 in every case, and the same is true of T.

The adjoint solution is

 Q* g=0,
 g(tau)=M(tau)^(-1)=exp(-d_minus*tau/D)(1+exp(2tau))^(-s/2). (6)

It belongs to L2(R_tau) exactly when d_minus<0<d_plus. In that case g'=-(d/D)g belongs to L2 as d is bounded, so it is genuinely in the adjoint domain. Every C(xi)g(tau), C in L2(R_xi), is then a member of ker(Q*). This is an infinite-dimensional closed subspace. Integration by the established adjoint identity proves it is orthogonal to Ran(Q). Consequently Ran(Q) is not dense and T is not surjective. The infinite-dimensional orthogonal complement rules out Fredholmness, regardless of whether the range is closed. No assertion about closed range in this interior case is needed here.

If0 is an endpoint, equation(6) is not in L2. The same ODE characterization gives ker(Q*)=0, including when d_minus=d_plus=0. It follows directly from Hilbert-space orthogonality that Ran(Q) is dense. The failure of closed range is proved below.

## Endpoint approximate kernels and sharp norms

Fix chi in C_c^infinity(-1,1) with L2 norm1 and any phi in C_c^infinity(R_xi) with L2 norm1. At a right endpoint where d_plus=0, take

 V_N(xi,tau)=phi(xi)N^(-1/2)chi((tau-N^2)/N).

Its norm is1 and its tau derivative has norm N^(-1)||chi'||. On its support tau>=N^2-N, so

 |d(tau)-d_plus|=sD/(1+exp(2tau))<=sD exp(-2(N^2-N)).

Thus ||QV_N||<=D||chi'||/N+sD exp(-2(N^2-N))->0. At a left endpoint d_minus=0, use center -N^2; the corresponding bound follows from d(tau)-d_minus=sD exp(2tau)/(1+exp(2tau)). If s=0 and the common endpoint is0, d is identically0, so either construction works. Every V_N is in the maximal domain. Since Q is closed and injective, a closed range would make its inverse from the range into L2 bounded by the closed graph theorem. These unit vectors contradict that bound. Hence the dense range is nonclosed.

For the inverse regimes, the already proved group satisfies for t>=0

 ||G(t)||<=exp(d_plus*t),
 ||G(-t)||<=exp(-d_minus*t).

These follow from(3) and the bounds on d; translation preserves the L2 norm. If d_plus<0, define R=-integral_0^infinity G(t)dt. If d_minus>0, define R=integral_0^infinity G(-t)dt. The integrals converge in operator norm and their respective bounds are1/(-d_plus) and1/d_minus. The difference-quotient group identity puts Rf in the generator domain and yields QRf=f. Integrating the group derivative for h in the maximal domain gives RQh=h, because the group tends to0 in the chosen time direction. Thus these are both-sided inverses.

Their bounds are sharp. In the first case use the same unit packets centered at+N^2. They satisfy

 ||(Q-d_plus)V_N||<=D||chi'||/N+sD exp(-2(N^2-N))->0.

Hence ||QV_N||->|d_plus|, and applying the inverse to QV_N yields ||R||>=1/|d_plus|. The reverse-time case uses the packets centered at-N^2 and obtains ||R||>=1/d_minus. This proves(1), including s=0. No derivative gain, trace regularity or additional norm estimate is implicit in(1).

For Q-lambda with lambda=u+iv, multiplication by exp(-iv*tau/D) removes the imaginary part: (Q-lambda)[exp(-iv*tau/D)H]=exp(-iv*tau/D)(Q-u)H. The preceding proof applies with d_minus,d_plus shifted by-u. It gives resolvent exactly outside the stated strip, no eigenvalues anywhere, adjoint obstructions in its interior and nonclosed dense range on its boundary. This proves the spectral statement.

## Odd parity, real scalars and the IPM consequence

Oddness in y is equivalent to Fhat(xi,-eta)=-Fhat(xi,eta). Transformation(2) uses the same phase and positive factor on both signs, so it identifies that subspace with pairs(V,-V), isometric to one L2 copy after a factor1/sqrt(2). All inverse, kernel and adjoint arguments persist. Real odd functions additionally obey V(-xi,tau)=-overline(V(xi,tau)). Because Q has real coefficients independent of xi, it preserves this relation. The adjoint vectors and approximate kernels above can be chosen with phi or C equal to i times a real even function of xi and with real tau factors. They then satisfy the relation and give infinitely many real independent obstructions. The inverse formulas preserve real functions, so the same classification and exact norms hold on the real odd space. The unrestricted real space follows either by the same construction or by complexification of a real operator.

For the canonical parameters and a>=0,

 d_minus=-Aa-(A+3)/2<0,
 d_plus=Ds-Aa-(A+3)/2.

Therefore the negative-time inverse regime is unavailable in this nonnegative-weight sector, and the complete classification makes d_plus<0 necessary as well as sufficient. Its exact algebraic solution is a>theta(s), where

 theta(s)-5/2=(D/A)(s-3/2).

At s>=3/2 this forces a>5/2. The previously accepted compact test and the actual residual each have a nonzero x^2 lower bound on a fixed positive-y rectangle, so they are outside the resulting Y. The respective parent proofs establish those facts for the actual canonical background. This closes only the missing necessity in the classification of this frozen Y model. It says neither that every weak-weight full IPM realization is noninvertible nor that strong weights with a smaller image-compatible domain are impossible. It establishes no a posteriori closure, no distance to X3, no exact-profile exclusion and no decisive endpoint.

## Computational and evidentiary plan

One symbolic path checks the chain rule in(2) before simplifying, the group-amplitude identity, d, M, g, the endpoint inequalities after substituting q=exp(2tau)>0, and the actual rational thresholds from the binary NPZ k. A separate exact polynomial path will verify the same rational differential identities after q substitution and decode k from the hexadecimal JSON. Endpoint and spectral arguments above are analytic for all parameters; no numerical packet experiment is proposed as evidence. Complete actual-model review and later own adjudication are required before this proof is accepted. Inherited evidence identifies earlier proved hypotheses by hashes, which prove byte identity only.
