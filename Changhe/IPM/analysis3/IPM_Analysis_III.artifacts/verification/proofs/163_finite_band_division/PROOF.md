# Division of the actual angular velocity at an invariant axis

## Statement

Let

 v(t,theta)=sum_(n=1)^N q_n(t) sin(2n theta),
 q_n in W^(m,infinity)(R), N finite.

Then v/cos(theta) and v/sin(theta), initially defined away from their respective axes, extend to W^(m,infinity) functions on the cylinder. Their norms are bounded by a constant depending only on N,m times sum_n ||q_n||W^(m,infinity). In particular the actual modal background angular velocity, whose radial coefficients are W^(7,infinity), has divided coefficients of that same regularity. The assertion in proof 159 about the background cofactor scalar and transported smooth core therefore needs no loss of one radial derivative.

The statement is special to finite angular bandwidth. The proposed justification that an angular Hardy average maps a general bounded function of two variables into positive isotropic Sobolev regularity is false.

## Proof of the division statement

For each n, sin(2n theta) vanishes wherever sin(theta) or cos(theta) vanishes. More explicitly, the multiple-angle formula gives

 sin(2n theta)/sin(theta)=U_(2n-1)(cos(theta)),
 sin(2n theta)/cos(theta)=2 sin(theta) U_(n-1)(cos(2theta)),

where U_j is the polynomial determined by U_0=1, U_1(z)=2z and U_(j+1)=2zU_j-U_(j-1). The second displayed identity must include its parity shift correctly: sin(2n theta)=sin(2theta)U_(n-1)(cos(2theta)), so the quotient is exactly as written. Both right sides are fixed smooth trigonometric polynomials. Every mixed derivative of total order at most m is a finite sum of a radial derivative q_n^(j), j<=m, times a bounded derivative of one of those polynomials. The weak radial derivatives and the classical angular derivatives commute. This proves the norm bound and the claimed extension.

The background field has exactly this finite sine expansion, by the canonical modal Green formulas of topics15 and68. The accepted regularity of its radial velocity coefficients is W^(7,infinity), as used in topics114 and126. Multiplication by cot(theta)-2tan(theta) uses the two quotients just proved and smooth sine or cosine factors; it therefore preserves W^(7,infinity). Smooth coefficient perturbations used in the approximation in proof 159 can also be divided without loss of any prescribed finite order, since they have all derivatives. Their higher norms need not be uniform in the approximation index; the uniform energy estimate only uses the lower norms stated there.

## Counterexample to the general Hardy-average shortcut

Fix 0<eta<1 and define on the one-dimensional torus

 a(t)=sum_(j>=1) 2^(-eta j/2) cos(2^j t).

The series converges uniformly, so a is bounded and continuous. Its H^eta norm is infinite: at its distinct frequencies 2^j, the squared weighted Fourier coefficients have sum comparable to sum_j 2^(eta j). Define f(t,phi)=a(t), independently of the angular variable phi, on a product of this torus with a bounded interval. Then

 integral_0^1 f(t,tau phi) d tau=a(t).

The average retains the tangential Fourier coefficients and is not in the isotropic H^eta space of that product. The same counterexample can be localized to a coordinate chart: if every localized piece of a finite smooth partition were H^eta, their sum would be H^eta, a contradiction. Thus boundedness alone cannot supply positive isotropic regularity through this angular average. A proof using such an average would have to retain separate tangential regularity hypotheses.

## Scope

This confirms the finite-band regularity input in proof 159 and refutes only the unsupported general Hardy-average explanation in the theory author's note35. It does not enlarge the regularity of an arbitrary rough perturbation. Those perturbations are controlled by the coefficient norms of topics155 and158, not by a W7 assertion.
