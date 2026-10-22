# Absolute and signed center drift: exact scope

Prepared 2026-10-22T11:39:32.971503+00:00 before the checks. This is an audit of SPEC A5, using the already independently checked asymptotic theorem as an explicit dependency. It is not a new full B2 endpoint.

## Statement and hypotheses

Let beta>=2, s=1/beta, and let a smooth nontrivial B2 solution have the prompt's sublinear velocity and polynomial vorticity. P01 and P40 reduce the possible nontrivial class to beta>=2 with a power-decaying vorticity. P18 proves divergence of the absolute component integral integral |x Omega|/|X|^2. This does not on its own determine a signed circular truncation. Thus the phrase 'this NEVER happens' in SPEC A5, immediately after saying 'this integral converges', must explicitly name absolute convergence; the subsequent sentence already leaves signed circular truncations uncontrolled in general.

Under the additional hypotheses Omega>=0 for x>0 and a0>0, P18 alone gives v0(R)>=c R^(1-s) for large R. Separately, the uniform asymptotic theorem stated in SPEC Theorem D, verified in P33, gives Omega(r,theta)=r^(-s)(a(theta)+e(r,theta)), where sup_theta|e| tends to zero, a is continuous, nonzero and odd under x reflection. More generally the uniform asymptotic alone gives

    v0(R) = B R^(1-s) + o(R^(1-s)),
    B = [2 pi (1-s)]^(-1) integral_0^(2pi) cos(theta) a(theta) dtheta.

Under the additional sign hypothesis, B>0. Without that hypothesis B can have either sign or vanish.

This supplies the stronger 'like' statement if Theorem D is cited. Without that dependency, the P18 citation alone supplies only 'at least'. The sign assumption is conditional and not imposed on the broad class.

## Proof

Write x=r cos(theta). The ordinary center component in the radius R disk is (2pi)^(-1) integral_0^R integral cos(theta) Omega(r,theta) dtheta dr; the polar Jacobian cancels the 1/r kernel. Its bounded inner disk contribution is O(1), since smooth vorticity makes the kernel locally integrable. Integrating the leading term from any fixed r0 gives B R^(1-s)+O(1). For each epsilon>0 choose r0 large enough that sup_theta |e(r,theta)|<=epsilon for r>=r0. The outer error is then at most [epsilon/(2pi)] integral |cos(theta)| dtheta integral_r0^R r^(-s) dr, which is O(epsilon R^(1-s)); the fixed inner error divided by R^(1-s) vanishes. First let R tend to infinity, then epsilon tend to zero. This proves the little-o remainder.

The sign assumption gives a>=0 on the right half-circle, while odd reflection makes cos(theta)a(theta)>=0 on both halves. Since a is continuous and nonzero, it is nonzero at some point with cos(theta) != 0, and is strictly positive on a nonempty open subarc of the right half-circle after reflection if necessary. The angular integral is positive. No pointwise positivity of a everywhere is needed.

For a counterexample to the logical inference from absolute divergence to divergence of signed disk integrals alone, take a smooth cutoff 0<=chi(r)<=1, zero for r<=1 and one for r>=2, and Omega=chi(r) r^(-s) cos(3theta). It is smooth on the plane and odd under x reflection. Its signed center disk integral vanishes identically by angular orthogonality, but its absolute component integral grows as a positive constant times R^(1-s). Its once-subtracted inverse is sublinear by P03. It is not asserted to solve the coupled B2 equations or satisfy the center jet. It refutes the integral implication for fields, without constructing a counterexample B2 solution.

For the angular control, cos(theta)cos(3theta) has primitive sin(2theta)/4+sin(4theta)/8, changes sign at pi/6 inside [0,pi/2], and has even, pi-periodic absolute value. Thus its absolute integral on the circle is 4 times twice the primitive at pi/6, namely 3 sqrt(3)/2. The signed integral is zero by orthogonality. The separately checked smooth cubic field r^3 cos(3theta)(1+r^2)^(-(3+s)/2) has the same leading angular coefficient and avoids a cutoff. It is also only a field control.

## Verification and scope

Read the actual SPEC as data and compare the exact wording. Independently check angular orthogonality, sign and exponent factors with exact arithmetic and a separately implemented quadrature control; do not execute other lanes' code. The analytic argument above proves the integration lemma. Numerical controls only check implementation. The suggested minimal repair explicitly names absolute convergence. Citing P18 alone gives no signed-convergence conclusion and only 'at least' under the sign hypothesis. Citing P33 additionally gives the leading-order formula above for every solution, with divergence for B!=0 and convergence undecided by that leading theorem when B=0; under the sign hypothesis it gives asymptotic equivalence to a positive constant times R^(1-s). Actual SPEC adoption is a separate readback.

Dependencies: P01, P03, P18, and P33 for the uniform angular asymptotic, all under their exact hypotheses. General B2 remains OPEN. No JavaScript/TypeScript, servers/listeners/tunnels, RLScience cluster, Lean/Lake, commits/pushes/posts or human contact. Writes only inside verification.
