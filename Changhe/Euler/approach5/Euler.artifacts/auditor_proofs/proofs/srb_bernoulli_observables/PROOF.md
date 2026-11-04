# Bernoulli flux coordinates and physical time averages

Audits A212-A213. Written: 2026-11-02T22:00:53Z. A212 is CONFIRMED with the qualifications stated here. The two broader inferences listed last remain OPEN.

## Statement

Let U,P be a real C^2 Euler profile on R3, with 0<c<1/2 and finite omega, and assume U=o(|y|) uniformly. Set X=cy+U, B=X-omega Jy, W=curl U, a0=1-2c, S=(DU+DU^T)/2, and let Psi_t be the backward B flow. Put H=Htilde-c a0 |y|^2/2, where Htilde=P+|U|^2/2+(cy-omega Jy).U. Then the one-form

    alpha=(B cross W).dy=dH+a0 X.dy

satisfies Psi_t^*alpha=exp(a0 t)alpha.

Assume nu is a compactly supported full-flow-ergodic probability with nu(W!=0,B!=0)=1 and the vortical SRB properties already specified in A207. On every oriented C^1 arc gamma transverse to ker alpha and oriented so alpha(gamma')>0,

    length_alpha(gamma)=H(gamma(end))-H(gamma(start))+a0 integral_gamma X.dy.

If the images Psi_t(gamma) stay in a common compact set, then

    integral_(Psi_t gamma) X.dy
      =exp(a0 t)length_alpha(gamma)/a0+O(1).

The conditional SRB mass is a plaque-dependent positive constant times this alpha-length, not the unnormalized length itself. On a one-dimensional return branch the coordinate r(p)=H(p)-H(p0)+a0 integral_(p0 to p) X.dy has dr=alpha, and the return derivative is exp(a0 T(r)).

On O={W!=0} define n=W/|W|, a=n.Sn, b=Sn-a n and p_nn=n.D^2P n. Every point in the continuous-time basin of nu has

    lim_(T->infinity) (1/T) integral_0^T [|b|^2-p_nn-(a-1)^2](Psi_t z)dt=2.

The analogous bounded first-order and fixed-frame moment observables have their nu averages. No boundedness of 1/|W| on supp nu is assumed.

## Proof

The first identity is the checked Lamb form, with a quadratic exact differential moved from U to X. Pullback under Psi follows either from Cartan's formula or the exact bracket/divergence identities in A199. Integrating the one-form gives the signed arc formula. The chosen orientation identifies its signed integral with positive alpha-length. Pullback gives the exponential factor exactly; the two endpoint values of H remain bounded on the common compact set. A207 supplies only proportionality of each conditional measure to alpha-length, with its own normalizing constant. The return derivative follows by differentiating the pullback identity on the return section: the variable return-time term vanishes because alpha(B)=0.

For the moment statement, the checked Riccati identity is

    B.grad a=|b|^2-a^2-a-p_nn,
    B.grad n=b-omega Jn.

All a,b,p_nn and B.grad a are bounded on O intersect any fixed compact set, even if W approaches zero. Bounded flow difference quotients, or integration over a finite time interval followed by invariance, give integral B.grad a dnu=0. The exact magnitude equation is d_t log|W(Psi_t z)|=1-a(Psi_t z). Ergodicity gives a limiting average of bounded a. Recurrence to a set with |W| bounded below, and boundedness above on the compact support, force that average to be one. Hence integral[|b|^2-p_nn-(a-1)^2]dnu=3 integral a-1=2.

A basin point lies in O: otherwise W vanishes along its orbit, so the time average of the bounded continuous function min(1,|W|) is zero, contrary to its positive nu integral. Its forward Psi orbit is eventually in a common trapping ball. Each displayed observable is bounded and continuous on O in that ball. Extend it by zero on {W=0}. Its possible discontinuities lie in this closed nu-null set. Weak convergence of the empirical probabilities therefore gives convergence of its integrals. Explicitly, first multiply the observable by a continuous cutoff that vanishes when |W|<=delta and equals one when |W|>=2delta. This is continuous, so basin convergence applies. The error is bounded by a constant times empirical mass in {|W|<=2delta}; use a continuous majorant supported in {|W|<=3delta}, then let delta decrease to zero. Since nu(W=0)=0, the error vanishes. Thus the time-average assertion holds for every point in this basin, not only almost every one.

The same cutoff argument handles every bounded directional expression continuous on O. It does not automatically handle an unbounded observable or a merely measurable Oseledets direction with further discontinuities.

## Necessary qualifications to the draft's Section 14

1. The arc formula uses oriented alpha-length. With the opposite orientation its right side is negative. Conditional SRB mass also has a plaque-dependent normalization (A207).
2. In this Euler setting n is C^1 on O simply because W is C^1 and nonzero there. A131 gives continuity of hyperbolic plaques, not a general theorem that the stable direction of every C^2 flow is C^1 along unstable leaves. No C^1 extension to supp nu intersect {W=0} is established.
3. If b=0, the actual equation is B.grad n=-omega Jn. Along a B orbit n therefore rotates as exp(-omega tJ)n(0); this does not make n spatially constant. The assertion that b=0 is impossible for nonaxial directions when omega!=0 requires the ADDITIONAL hypothesis that n is constant on the support. With that hypothesis, 0=B.grad n forces b=omega Jn and the axial conclusion follows. Without it the draft's inference is OPEN, not a consequence of A120.
4. The pressure identities constrain selected moments. They do not classify all possible pressure moments or prove that every further contradiction must use a particular nonlocal input.

## Dependencies and scope

This is the precise valid part of Theory Agent B B23, THEORY_B Section 14. It uses A119-A120 and A207, with the existing compact vortical SRB probability as a hypothesis. It does not assert that such a measure exists for every C^2 profile, and it gives no sign contradiction.
