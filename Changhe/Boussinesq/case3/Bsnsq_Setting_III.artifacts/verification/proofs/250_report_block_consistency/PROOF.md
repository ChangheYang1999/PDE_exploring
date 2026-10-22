# Independent audit of the 4.39 to 4.43 consistency edits

## Exact statement and scope

This packet checks the seventeen declared replacements F1 to F17 in the lead's work/ref443/fix/text_v1.md against the report actually entered at02:09UTC. The base report, replacement text, proposed entire report, referee text and timeline are immutable inputs recorded in verification/freeze.json. The result concerns whether those finite replacements are mathematically justified and whether the proposed report changes anything else. It is not a new existence or nonexistence theorem.

The common mathematical setting is a smooth B2 field on R2 with beta>0, W=beta X+U(X)-U(0), div W=2beta, Omega=partial_y W1-partial_x W2, W.grad Omega+Omega=Theta_x, and W.grad Theta=(beta-2)Theta. Temperature is even in x, zero on x=0, and has nonzero leading jet a0 x2; vorticity is odd in x. The velocity is uniformly sublinear at infinity. No y parity or bound on every derivative at infinity is added. On the axis let T(y)=Theta_xx(0,y), b(y)=W2(0,y), and J be the component of {T!=0} containing0. Write I_j(y)=partial_x^(2j)Theta(0,y)/T(y)^j on J. The prior independently proved results P231, P237 and P242 state that I2 and I3 cannot both be constant on J for beta>=2. Their whole proofs and certificates are explicit dependencies. Nothing here assumes those ratios are constant for a general profile.

## Inheritance, sublinearity and the shortened statements

Uniform sublinearity means sup on|X|=r of|W-beta X|/r tends to0. It cannot mean sublinearity of W, because the reverse triangle inequality gives |W|/r>=beta-|W-beta X|/r, with limit beta>0. Thus F2 corrects a named field without changing the intended hypothesis. Referring to the first paragraph of each antecedent theorem in F3 and F4 unambiguously retains exactly the common hypotheses, not extra derivative or component-end conditions of particular parts. These openings will be checked in the actual frozen report.

Suppose Theta(x,y)=H(x/rho(y)) on some open neighbourhood of the whole axis, where rho is positive. No regularity of rho or H need be assumed: the slice y=0 gives H(k)=Theta(k rho(0),0) for k near0, so H is smooth there. For each fixed y, differentiation in x then gives T(y)=H''(0)/rho(y)^2 with H''(0)=2a0 rho(0)^2 nonzero. It follows that rho(y) is the positive square root of H''(0)/T(y), hence smooth on R. For every y there is an x interval on which the representation holds, enough to differentiate atx=0. Thus T(y)=H''(0)/rho(y)^2. At0, H''(0)=2a0 rho(0)^2!=0; consequently T never vanishes, J=R, and I_j=H^(2j)(0)/H''(0)^j is constant. The cited two-ratio theorem contradicts this for beta>=2. It uses no uniform width for the neighbourhood. This proves the containment asserted by the concise Summary and Q1 bullet; it does not exclude general temperatures. The finite endpoints of J are the nearest noncentral zeros of b by P237, already separately proved. Retaining that statement creates no new endpoint restriction. The old finite-degree polynomial exclusion is unchanged. These logical implications, rather than the referee's approval, justify F15 and F16.

## Integrality and parity are separate conditions

At a simple nearest axis zero y*, write kappa=-b'(y*)>0. The scalar axis equations for a=T/2 and q=Omega_x(0,y) are b a'=(2b'-3beta-2)a and b q'+(2beta+1-b')q=2a. Their nonzero leading orders at the endpoint are n=2+(3beta+2)/kappa and m=1+(2beta+1)/kappa. Smoothness makes n,m integers and their integer combinations d=2(n-2)-3(m-1)=1/kappa and r=2(m-1)-(n-2)=beta/kappa integers. This alone permits beta3,kappa1,n13,m8,r3,d1. The global continuation and sign argument in the appended P30 proof additionally requires n-m even, equivalently r+d odd. The example has r+d4, so it fails that condition. For reduced beta=P/Q, rQ=dP implies r=Pk,d=Qk with integer k>=1; r+d odd forces k odd and P,Q of opposite parity. Therefore the exclusion of reduced odd/odd beta needs parity as well as integrality. This proves the F1 distinction; it is read under the global hypotheses expressly retained by the Summary. No claim that local smoothness alone forces the global parity condition is made here.

## Smooth Taylor coefficients and the t=0 polynomial step

For smooth rho define r_n=rho^(n)(0)/n!. Every finite coefficient extraction follows from finite Taylor's theorem and differentiation of identities; it does not assert convergence of an infinite Taylor series. F5 makes this explicit. The coefficients -24(3beta-4)A2 and -80(beta-2)(3beta-1)A are nonzero for beta>2 and A!=0, which is part of the center normalization. F6 therefore states all required factors.

The chart1 polynomials arise by clearing denominators from the finite coefficients in the same chart, not by reusing the chart0 polynomials after an unmentioned division by B. All removed denominator and coefficient factors are nonzero for beta>2 and A=beta(3beta+2-4t)/4!=0, as certified independently in P242. F7 defines those polynomials before using them.

At t=0 write F_j(B,0,beta)=kappa_j(beta)B h_j(B,beta) for j2,3,4, with kappa_j nonzero for beta>2. The finite algebra to be replayed below states that h2 has degree one in B with coprime coefficients in Q[beta] and that the gcd of Resultant_B(h2,h3) and Resultant_B(h2,h4) is, up to a nonzero rational unit,

    beta2 (beta-2)2 (2beta+1)2 (3beta-1) (3beta+2)4 (7beta+4).

Assume a common solution with beta>2 and B!=0. Division by B and the nonzero kappa_j makes h2=h3=h4=0. The specialization of each polynomial resultant vanishes at that beta even if a leading coefficient drops; this follows from its Sylvester determinant identity. Thus the displayed gcd must vanish there. Every factor is strictly positive at beta>2, contradiction. Hence B=0. The coprime coefficients ensure h2 is not the zero polynomial at any beta, but no converse of the resultant condition is used. The report's factor256 is just its chosen resultant normalization; our check compares exact factors and, where normalization differs, the nonzero rational unit. F8 is justified once these finite equalities are confirmed. The B=0 branch is retained, not divided away from the proof.

## Reflection and notation

Set S_y=diag(1,-1), transformed U(X)=S_y U(S_y X), transformed Theta(X)=-Theta(S_y X), transformed Omega(X)=-Omega(S_y X), and transformed Psi(X)=-Psi(S_y X). Direct differentiation gives transformed U=(-Psi_y,Psi_x), -Delta Psi=Omega, transformed W=S_y W(S_y X), transformed div W=2beta, and both transformed transport equations equal minus the original equation evaluated at S_y X. The canonical relative inverse is preserved by a change of variables in its kernel, or uniqueness with the same relative gauge. The center subtraction transforms with U(0). Thus this maps the class to itself, flips a0 and changes rho(y) to rho(-y). Relabeling this reflection S_y avoids collision with the established x reflection S; it imposes no y parity. F9 and F10 are exactly a relabeling. F11 to F14 list symbols already present or introduced by F7/F8. F17 clarifies a reference to step7 of4.40; it changes no mathematical sentence otherwise.

## Complete prior proof and verification method

The full P30 global parity proof is reproduced below because its global argument is essential to interpreting F1. P242 already contains the full finite-jet derivation, smooth uniqueness and component continuation closing the two-ratio theorem; its proof and certificate manifests are registered as dependencies. We will parse each old/new pair independently, require each old text to occur exactly once after whitespace normalization, apply all seventeen replacements, and independently append exactly one declared timeline entry. Whole-text equality to the preview, preservation of all140 earlier timeline entries, and unchanged table rows test for unintended edits. This procedure does not run the lead's editing script. The chart1 t=0 polynomials are reconstructed from our earlier exact JSON, with independent resultants and gcds for this smaller step. No large resultants need to be rerun because no underlying algebra changed. No formalization or Lean/Lake build is claimed.

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
