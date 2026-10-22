# Continuation past an axis saddle imposes another parity condition

Date:2026-10-20. Status: PROVED necessary condition. No full exclusion of smooth B2 profiles.

## Statement

Let beta>=2 and let b,a,q be smooth real functions on the whole real axis satisfying

    b a'=(2b'-Lambda)a, b q'+(M-b')q=2a,
    Lambda=3beta+2, M=2beta+1,
    b(0)=0, b'(0)=Lambda/2, a(0)=a0>0, q(0)=4a0/beta,
    b(y)=beta y+o(|y|) as |y| tends to infinity.

These are necessary axis conditions for the B2 profiles. Let y* be the nearest additional zero of b above or below0. If it is finite and simple, put kappa=-b'(y*)>0. Then

    d=1/kappa and r=beta/kappa are positive integers,
    r+d is odd.                                        (1)

Writing beta=P/Q in lowest positive terms, there must be an odd positive integer k such that

    d=Qk, r=Pk, P and Q have opposite parity.            (2)

Thus irrational beta and reduced odd/odd rationals, including all odd integers beta>=3, cannot have a simple nearest additional axis zero. Smooth degenerate endpoints are not excluded.

If either q>=0 on the whole axis or a>=0 on the whole axis, the stronger necessary conditions are

    P even, Q odd, k odd.                              (3)

For B2, global Omega>=0 in x>0 implies the first optional condition, and global Theta>=0 implies the second. Neither global sign condition is assumed in(1)-(2).

If a is real analytic on the axis and beta is irrational or is rational with odd numerator and odd denominator in lowest terms, then0 is the only axis zero, with b>0 above0 and b<0 below0. Under either optional sign condition, the same conclusion also holds for every reduced rational beta with odd numerator. No such conclusion is claimed for the remaining rational cases.

## Connection with the B2 fields

For a smooth B2 field set a(y)=Theta_xx(0,y)/2, q(y)=Omega_x(0,y), and b(y)=W2(0,y). Parity gives W1=xA near the axis, and div W=2beta gives A(0,y)=2beta-b'(y). The x^2 coefficient of the temperature equation is b a'+2A a=(beta-2)a, and the x coefficient of the vorticity equation is b q'+(A+1)q=2a. These are precisely the two displayed ODEs. The center temperature jet fixes b'(0)=Lambda/2 and then the second ODE gives q(0)=4a0/beta. Sublinear U gives b(y)=beta y+o(|y|). If Omega>=0 for x>0, then q(y)=lim_{x down to0}Omega(x,y)/x>=0. If Theta>=0, then a(y)=lim_{x to0}Theta(x,y)/x^2>=0. Thus both optional implications hold without an unmentioned sign assumption.

## Local information and its proof

The center data and the two scalar ODEs give a,q>0 until the nearest additional zero. For a this follows from its homogeneous equation away from zeros of b. For q, forward axis flow from near0 and its positive source2a preserve positivity. At the endpoint b'<=0 and direct evaluation of the equations gives a=q=0.

At a simple endpoint write z=y-y*, s=|z| on its central side. Dividing by b=-kappa z+O(z^2) and integrating gives

    a=A s^n times a smooth positive factor,
    H=s^m times a smooth positive factor,
    n=2+Lambda/kappa, m=1+M/kappa,

where H solves the homogeneous q equation. Along forward time d(q/H)/dt=2a/H>0. Its remaining increase is finite: the absolute time element is (1+O(s))ds/(kappa s), and n-m=1+(beta+1)/kappa>0. Thus q=Q_*s^m(1+o(1)) with Q_*>0. Nonzero one-sided Taylor asymptotics of smooth functions force n,m to be integers. Integer linear combinations then give

    d=2(n-2)-3(m-1), r=2(m-1)-(n-2),
    n=2+3r+2d, m=1+2r+d.                               (4)

These positive integers were established in detail in packet28 and are rederived here to fix exactly what is used.

## There is a next zero beyond the saddle

It suffices to consider an upper endpoint y*>0. Immediately to its right b<0. Axis sublinearity gives b>0 for all sufficiently large positive y. Therefore there is a first zero z*>y*, finite, with b<0 throughout I=(y*,z*). Existence of the first such zero follows from continuity and the fact that y* is simple, so it has a neighborhood with no other zero. Smooth continuation across y* gives a the nonzero sign(-1)^n near the left endpoint of I, and the homogeneous equation keeps this sign on all of I. Put k=b'(z*)>=0.

If k=0, follow an orbit in I backward. It tends to z*: an interior limit would be an interior zero of b, and a smooth scalar flow cannot reach an equilibrium in finite time. Along this orbit

    d log|a|/dt=2b'-Lambda.

For sufficiently negative t the right side is <=-Lambda/2. Integrating backward therefore makes |a| grow without bound, contrary to smoothness at the finite point z*. Hence k>0.

Near z*, the nonzero solution for a has exponent nu=2-Lambda/k<2. Bounded smoothness forces nu=0 or1. Thus exactly two cases remain:

    k=Lambda/2 and a(z*)!=0;
    k=Lambda and a(z*)=0, a'(z*)!=0.                    (5)

In the first case the q equation at z* gives q(z*)=4a(z*)/beta. In the second case it gives q(z*)=0. Differentiating the equation gives b q''+M q'-b''q=2a', and hence q'(z*)=2a'(z*)/M. In both cases q/a tends to a strictly positive value on the side I.

## Sign propagation and arithmetic

Let epsilon be the constant sign of a on I. Under the forward flow from z* toward y*, the function epsilon q satisfies

    d(epsilon q)/dt+(M-b')epsilon q=2|a|>0.

It is positive sufficiently close to z*, by(5), and remains positive by the integrating-factor formula. Thus q and a have the same sign on all of I. Their signs just across y*, fixed by their nonzero Taylor orders on the central side, are(-1)^m and(-1)^n. They must agree. Therefore n-m is even. By(4), n-m=1+r+d, proving(1).

For a lower endpoint apply this argument to btilde(y)=-b(-y), atilde(y)=a(-y), qtilde(y)=q(-y). They obey exactly the same equations and sublinearity. Thus the conclusion holds at either nearest endpoint.

If beta=P/Q is reduced, rQ=dP implies d=Qk,r=Pk for an integer k>=1. The condition r+d odd is k(P+Q) odd, equivalent to k odd and P,Q of opposite parity. This proves(2).

If q>=0 on both sides of y*, then m is even, hence d is odd by(4). Equation(1) then makes r even, proving(3). Alternatively if a>=0 on both sides, n is even, hence r is even by(4), and(1) makes d odd. This proves the same conclusion from temperature positivity alone. A one-sided positive sign does not imply an even Taylor order.

## Analytic-axis corollary and scope

At any degenerate zero of b, b=O(z^2). A finite leading Taylor term for a would have one lower order on the right side of b a'=(2b'-Lambda)a than on the left side, an impossibility. Hence a is flat there. A real analytic a with a(0)>0 cannot be flat anywhere on its connected axis. All zeros of b are then simple and cannot accumulate finitely, so if any additional one exists there is a nearest one. For irrational beta or reduced odd/odd beta, the exclusions already proved rule out that nearest zero. Under a sign hypothesis they rule it out whenever the reduced numerator is odd. This proves exactly the restricted analytic corollary stated above.

The proof independently verifies lead `astra/auditJ/PROOF.md` partsE-F. The extension from q>=0 to a>=0 is immediate from the same parity calculation and was checked here. The scalar equations and the global inverse can admit smooth data with degenerate endpoints, as the lead's separate examples show. Nothing here proves that the remaining arithmetic cases occur in the coupled PDE, or excludes its full smooth class. No formalization or numerical evidence is used.

External audit: actual claude-opus-5-5, review17, completed2026-10-20T15:36:18Z, confirmed the ODE proof and requested an explicit restriction of the analytic corollary. Its wording is now explicit. The map from the B2 fields to the axis ODEs and the optional sign implications are derived above, rather than delegated to that review.
