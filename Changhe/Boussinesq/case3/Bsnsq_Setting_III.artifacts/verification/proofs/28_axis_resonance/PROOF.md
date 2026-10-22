# Axis zeros and smoothness resonances

Date: 2026-10-20. Status: PROVED restrictions; no full B2 exclusion.

## Statement and hypotheses

Let beta >= 2 and let smooth fields on the whole plane satisfy

    W = beta X + U - U(0),  div U = 0,  curl U = -Omega,
    W.grad Theta = (beta-2)Theta,
    W.grad Omega + Omega = Theta_x.

Assume the B2 reflection parity, Theta(0,y)=0, and the center normalization
Theta=a0 x^2+O(|X|^3), a0>0. Put

    b(y)=W2(0,y), a(y)=Theta_xx(0,y)/2, q(y)=Omega_x(0,y),
    Lambda=3 beta+2, M=2 beta+1, mu=Lambda/2.

Then the following conclusions hold.

1. On the interval from the origin to the nearest additional axis zero in either direction, a and q are strictly positive. At any finite such endpoint y*, a=q=0 and b'(y*)<=0.
2. If kappa=-b'(y*)>0, then from the central side, with s=|y-y*|,

       a=A s^n(1+O(s)), q=Q s^m(1+o(1)), A,Q>0,
       n=2+Lambda/kappa, m=1+M/kappa.

   Both n,m are integers. Therefore d=1/kappa and r=beta/kappa=beta d are positive integers. An irrational beta has no nondegenerate nearest additional axis zero.
3. If Omega>=0 on x>0, then m is even and d is odd; integrality of beta d already follows without this sign assumption. If Theta>=0 throughout the plane, n is also even. These are necessary arithmetic conditions, not existence conditions.
4. At a degenerate nearest endpoint, a and q are flat: all their derivatives vanish.
5. More generally, at any simple axis zero bordering an interval on which a is not identically zero, a repelling axis derivative belongs to {Lambda/2,Lambda}, while an attracting derivative -kappa obeys Lambda/kappa in the positive integers. A transition from an identically zero interval for a to a nonzero interval can occur only through a degenerate axis zero.
6. If a is real analytic on the entire axis, all axis zeros are simple. For irrational beta the origin is its only axis zero.

Only the local ODE hypotheses are needed for these conclusions. A condition such as U=o(|X|) ensures completeness of the whole-plane flow when that is also desired. Analyticity in item6 is an additional hypothesis; it is not a consequence of smoothness.

## Derivation of the axis system

Parity gives W1=Omega=0 on the axis and d_y W1=0 there. Since curl W=-Omega, d_x W2=0 there. Divergence then gives d_x W1=2 beta-b'. Taylor expansion in x yields

    Theta=a(y)x^2+O(x^4), Omega=q(y)x+O(x^3),
    W1=(2 beta-b')x+O(x^3), W2=b(y)+O(x^2).

The respective x^2 and x coefficients of the two transport equations give

    b a'=(2b'-Lambda)a,                    (1)
    b q'+(M-b')q=2a.                       (2)

The center equations give

    b(0)=0, b'(0)=mu, a(0)=a0, q(0)=4a0/beta.   (3)

On the upper central interval b>0. Equation(1), away from its zero at0, preserves the sign of a. It is positive near0 by continuity, hence positive throughout this interval. Along its forward axis flow, equation(2) has a positive source2a. Every point can be reached from a point sufficiently close to0, where q>0, so the integrating-factor formula gives q>0. The lower central interval has b<0 and forward flow directed toward decreasing y; exactly the same argument applies. No global sign of Omega is used.

At a finite central endpoint the one-sided sign of b implies b'<=0. Evaluating(1) there gives a=0 because 2b'-Lambda<0. Equation(2) then gives q=0 because M-b'>0.

## Simple attracting endpoint

Let z=y-y*, b=-kappa z+O(z^2), kappa>0. Smoothness of b permits division by z and implies

    a'/a = n/z + rho(z), n=2+Lambda/kappa,

with rho smooth across0. On the central side this integrates to

    a=A |z|^n exp(integral_0^z rho), A>0.

Let H>0 solve the homogeneous equation b H'+(M-b')H=0 on that side. Similarly H=C |z|^m times a smooth positive factor, with m=1+M/kappa. Along forward flow,

    d(q/H)/dt=2a/H>0.

The endpoint corresponds to t tending to infinity. In the variable s=|z|, the absolute time element is (1+O(s)) ds/(kappa s). Thus the remaining increase in q/H is bounded by a constant times

    integral_0^epsilon s^(n-m-1) ds,

which is finite since n-m=1+(beta+1)/kappa>0. Its limiting value is finite and positive, since q/H was positive at any fixed interior point. This proves the asserted asymptotic for q, without any global sign assumption. The formula dt=-ds/(kappa s)(1+O(s)) has a minus sign when oriented toward the endpoint; the positivity argument uses forward time, and the convergence estimate uses its absolute value.

A smooth function with one-sided asymptotic C s^alpha, C!=0, cannot be flat. Its first nonzero Taylor order therefore equals alpha, so alpha is a nonnegative integer. Applying this to a and q gives n,m integral. The identity

    2Lambda-3M=1

then implies

    d=1/kappa=2(n-2)-3(m-1)=2n-3m-1,
    r=beta d=2(m-1)-(n-2).

Thus n=2+3r+2d and m=1+2r+d. The second integer identity, using 2M-Lambda=beta, is stronger than the initially stated 2 beta d integrality.

This proves item2. If Omega>=0 on x>0, taking Omega(x,y)/x as x decreases to0 gives q(y)>=0 on both sides of y*. Its nonzero Taylor order m is even. Hence d=2n-3m-1 is odd and m-1-d is even, as also follows already from the sign-free identity. Global Theta>=0 similarly makes a>=0 on both sides, forcing n even. No one-sided sign alone forces an even order.

## Degenerate endpoint and arbitrary axis zeros

If b'=0 at a zero, then b=O(z^2). If a has finite Taylor order j, the left side of(1) has order at least j+1, while its right side has leading coefficient -Lambda times the nonzero order-j term of a. This is impossible. Thus a is flat. The same argument in(2), whose forcing2a is now flat, makes q flat. This argument applies at any degenerate axis zero, even without adjacency to the center.

At a simple zero with b'=k>0 and a nonzero on an adjacent interval, equation(1) instead gives a=C |z|^nu times a smooth nonvanishing factor, nu=2-Lambda/k<2. Boundedness and smoothness force nu=0 or1, hence k=Lambda/2 orLambda. If k<0 its exponent is2+Lambda/|k|, which forces Lambda/|k| to be an integer. If a were zero on the other side, all its derivatives at0 would vanish, contradicting this finite nonzero Taylor order. Therefore a transition from an identically zero interval requires a degenerate zero.

For completeness, at the two repelling derivatives the homogeneous q exponent is

    1-M/k = -beta/(3beta+2), or (beta+1)/(3beta+2).

It is nonintegral. Thus a smooth solution cannot contain a nonzero coefficient of this singular homogeneous mode relative to a smooth particular solution. This is a local regularity condition, not an independent global obstruction.

Finally, if a is real analytic on the connected axis and a(0)!=0, it cannot be flat at a point or vanish on an interval. The preceding argument excludes every degenerate zero of b. Simple zeros have no finite accumulation. If any additional axis zero exists, there is consequently a nearest one, and item2 applies. Irrational beta excludes that simple zero. This proves item6.

## A necessary third-order center check

Differentiate(1) at0, using2mu=Lambda:

    a'(0)=2b''(0)a0/mu.

Differentiate(2); the two b'q' terms cancel, leaving

    M q'(0)=b''(0)q(0)+2a'(0)
            =b''(0)[q(0)+4a0/mu].          (4)

Equation(4) is necessary for a full profile and is a useful inexpensive candidate check. It is stronger than the already imposed zeroth-order axis equations. It depends on the actual velocity, not an externally prescribed strain alone.

## Dependencies, audit, and scope

The proof uses only smooth Taylor expansion, scalar ODEs, and the elementary identity theorem for real analytic functions. It independently checks the lead's `notes/axis_structure.md` propositions1-3 and the new sign-free resonance extension. Propositions4-5 of that note were also checked, with the homogeneous-mode statement interpreted relative to a smooth particular solution. Lead `astra/posvort/PROOF.md` supplies the prior positive-vorticity version; its oriented ds sign is immaterial after taking the absolute time element as above.

There is no exclusion of degenerate smooth endpoints, no full-system example at an allowed resonance, and no full NO. The smooth B2 problem remains open. No numerical experiment or formal proof is used in this argument.

Update 2026-10-20T15:30:51.516233+00:00: lead auditJ pointed out the stronger sign-free identity beta d=2(m-1)-(n-2). I independently checked and incorporated it. The original weaker assertion was true, but the stronger one removes an unnecessary sign hypothesis. Global continuation adds another parity restriction, separately proved in packet30.
