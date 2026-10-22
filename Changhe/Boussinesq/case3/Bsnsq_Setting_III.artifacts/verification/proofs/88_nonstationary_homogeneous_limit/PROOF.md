# The homogeneous far field cannot be stationary

Date: 2026-10-20. Status: independently derived complete informal proof; exact checks and actual Claude Opus 5.5 follow-up audit agree with the stated scope. This is a necessary far-field condition, not an existence or nonexistence endpoint.

## 1. Statement and dependencies

Let beta>=2 and let (Omega,Theta,V) be a nontrivial smooth full-plane B2 profile in class A, with the prompt's reflection, center and canonical relative-inverse conditions. The convention is Omega=-curl V=-Delta Psi, V=(-Psi_y,Psi_x), and the defining vorticity equation has the source +Theta_x, exactly as stipulated in PROMPT.md. It is consistent with physical buoyancy -theta e_2; no standard-curl sign is substituted. Put s=1/beta, m=1-2s and k=2-s. The previously proved smooth far-field expansions (packets33,35,36,38) give smooth periodic real functions a,h,f,b,d with

    Omega(r,theta)=r^(-s)a(theta)+r^(-2s)b(theta)+o(r^(-2s)),
    Theta(r,theta)=r^m h(theta)+r^(m-s)d(theta)+o(r^(m-s)),
    Psi_0(r,theta)=r^k f(theta),
    a=-(f''+k^2 f),
    u_0r=-f', u_0theta=k f.

Both scalar remainders are uniform in theta. The leading a is not identically zero. Reflection gives f(pi-theta)=-f(theta), in particular f(pi/2)=f(-pi/2)=0. The second scalar coefficients are

    d=k f h'-m f' h,
    b=k f a'+s f' a-m cos(theta)h+sin(theta)h'.          (1)

Then b and d cannot both vanish identically. Consequently the limiting homogeneous physical fields do not solve both steady transport equations on the punctured plane. Neither exact homogeneity of both scalar profiles outside a ball, nor simultaneous uniform improvements of both displayed remainders to o(r^(-2s)) and o(r^(m-s)), respectively, are possible.

There is also a stronger conditional statement. If either half-axis has no zero of W=beta X+V other than the center, then d is not identically zero. In particular d is nonzero for every profile in the global-source subclass G at beta>2. This also rules out the temperature remainder alone being o(r^(m-s)). This extra conclusion uses the nonzero axis-tail coefficients of packet65, whose hypotheses and proof explicitly include beta=2; it is not asserted when both half-axes contain additional zeros.

The main proof below is an independent check of the lead's notes/draft_4_25.md. Section4 is an additional verifier derivation.

## 2. Angular first integrals under the stationary assumption

Suppose b=d=0. Let J be any connected component of {f!=0} on the angular circle. Since the two vertical directions are zeros, J is a proper open arc with endpoints where f tends to zero; its sign sigma is constant. If m>0, the first identity in(1) integrates on J to

    h=C |f|^(m/k),                                      (2)

where C is real and may be zero. The case m=0 instead gives h'=0 on J. No division is performed at an endpoint or zero of f.

For m>0 multiply the second identity in(1) by |f|^(s/k)/(k f). Since m+s-k=-1, direct differentiation gives

    (|f|^(s/k)a)'=(C m/k)(sin(theta) sigma |f|^(-1/k))'. (3)

It follows that, for another constant D,

    a=(C m/k) sin(theta) sigma |f|^(-(1+s)/k)
          +D |f|^(-s/k).                               (4)

At least one endpoint theta_e of J has sin(theta_e)!=0. Indeed, if both endpoints belonged to {0,pi}, the intervening connected arc would contain one of the vertical directions where f=0, contrary to J being a component of {f!=0}. Multiply(4) by |f|^((1+s)/k) and approach that endpoint. The boundedness of a, positivity of (1+s)/k and 1/k, and f->0 give C m sin(theta_e) sigma/k=0. Thus C=0. Equation(4), the boundedness of a, and s/k>0 then imply D=0. Hence a=0 on J.

When m=0, the equation h'=0 on J removes both temperature terms from b=0. The remaining equation is k f a'+s f'a=0, so a=D |f|^(-s/k). Its boundedness at either endpoint forces D=0, again giving a=0 on J.

On the interior of {f=0}, the relation a=-(f''+k^2f) gives a=0 directly. The union of this interior and {f!=0} is dense: the omitted boundary of the closed zero set has empty interior. Continuity therefore gives a=0 on the entire circle. This contradicts the nonzero-tail theorem and proves the main assertion. This argument requires neither a finite number of zeros nor finite vanishing order at an endpoint.

## 3. Relation to the physical limit and asymptotic uniqueness

For the homogeneous fields omega_0=r^(-s)a, theta_0=r^m h and u_0=J_+ grad(r^k f), polar differentiation gives

    u_0.grad theta_0=r^(m-s)d,
    u_0.grad omega_0-partial_x theta_0=r^(-2s)b.

Here m-1=-2s. Thus their two steady equations are exactly d=0 and b=0; one cannot replace this pair by a claim about a single equation. If the exact scalar profiles are homogeneous beyond a fixed radius, uniqueness of the expansions forces b=d=0. The same conclusion follows by multiplying the two stipulated improved remainders by r^(2s) and r^(-m+s), respectively, and taking uniform angular limits.

This gives nonvanishing of at least one coefficient, with no universal lower bound on its norm. It supplies no quantitative residual bound for an approximate profile.

## 4. A nonzero second temperature coefficient on a free half-axis

Suppose the half-axis with sign sigma in {+1,-1} has no additional zero. Packet65 gives positive constants P,Q (after the allowed signed normalization a0>0) such that at theta_0=sigma pi/2,

    h(theta_0)=h'(theta_0)=0, h''(theta_0)=P>0,
    a(theta_0)=0, a'(theta_0)=-sigma Q, Q>0.             (5)

The Taylor argument only needs P and Q to be nonzero; their signs need not agree. Set t=theta-theta_0. Reflection makes f odd in t and h even in t. Write their smooth Taylor expansions as

    f=A t+(B/6)t^3+O(t^5),
    h=(P/2)t^2+(H/24)t^4+O(t^6).

Substitution into d=k f h'-m f'h shows that its quadratic coefficient is

    A P (k-m/2)=(3/2) A P.                             (6)

Thus d identically zero would force A=0. Differentiating a=-(f''+k^2f) at theta_0 then gives B=sigma Q!=0. With A=0, the fourth-order coefficient of d is

    B P (2k-3m)/12=B P(1+4s)/12,                       (7)

which is nonzero because s>0 and B,P are nonzero. This contradiction proves d!=0. The Taylor argument applies without modification to beta=2 (m=0), whenever the stated free-half-axis hypothesis holds. It uses only derivatives through order4 of d and order3 of f, not analyticity or a convergent Taylor series.

For comparison, the smooth angular data beta=8, f=cos(theta)^5 and h=cos(theta)^2 have d=0: m/k=2/5 and h=|f|^(2/5). They have a=-(f''+k^2f), with a' zero on the verticals, so they do not meet the free-axis input(5). Moreover b(0)=-m=-3/4, so they do not refute the main assertion. This is only angular data, not a profile.

## 5. Verification and scope

The argument was written before the separate exact symbolic checks. Verification evidence and actual model responses belong in verification/. No formal proof assistant was run. The unrestricted profile problem remains open: nonzero second terms are permitted, and both half-axes may have additional zeros outside G.
