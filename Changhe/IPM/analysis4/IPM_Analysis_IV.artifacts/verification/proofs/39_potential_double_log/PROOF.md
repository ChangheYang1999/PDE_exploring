# A squared logarithm is necessary at potential degree zero

Status: exact local reconstruction and minimal-degree argument. This corrects the statement that only one extra logarithmic power is needed at every exceptional potential order.

## Statement

For a pure density coefficient r^(-3) f(theta), where f is a finite S1 sine polynomial, let alpha be its sin(theta) coefficient. If alpha is nonzero, every polynomial-log potential of radial degree zero generating that density has logarithmic degree at least two. A degree-two potential always suffices, with constant-angular t^2 coefficient alpha/4, where t=log r. The stream can be matched to any chosen free resonant amplitude by adding a multiple of log r.

In particular,

\[
 \chi=\frac{t^2+t}{4},\qquad
 \rho=r^{-3}\sin\theta,\qquad
 \psi=-\frac12r^{-2}t\sin(2\theta)
 \tag{1}
\]

satisfy rho=-partial_y Delta chi and psi=chi_xy. The resonant stream coefficient has value zero at t=0. These are reconstruction identities, not by themselves a stationary solution.

## Direct calculation

For a radial potential C(t),

\[
 \Delta C(t)=r^{-2}C''(t),\qquad
 \partial_x\partial_y C(t)
   =\frac12r^{-2}[C''(t)-2C'(t)]\sin(2\theta).
\]

Thus chi=t^2/4 has Delta chi=r^(-2)/2, density r^(-3) sin(theta), and stream r^(-2)(1/4-t/2) sin(2theta). Adding t/4 leaves the density unchanged and subtracts r^(-2)sin(2theta)/4 from the stream. This proves (1). The independent Cartesian Laurent calculation is retained in verification/identities.json.

## Why degree one cannot suffice

Suppose chi=t C_1(theta)+C_0(theta) generated the pure target density. In its highest logarithmic degree, the density map is the pure degree-zero potential map applied to C_1. Since the target has no logarithm, C_1 lies in that map's kernel.

The kernel on smooth periodic even angular coefficients consists only of constants. Indeed, zero density gives partial_y Delta chi=0. A pure degree-zero potential has a Laplacian homogeneous of degree -2, so the latter is a function of x alone of that degree. Smoothness across x=0 forces it to vanish. The angular harmonic equation at degree zero is C_1''=0, hence C_1 is constant. The same conclusion follows by descending finite Fourier coefficients.

But constant C_1 times log r is harmonic and has zero density. The entire target would therefore have to come from the pure C_0. At degree zero a pure potential has zero sin(theta) density coefficient, as the exact triangular map gives a_0=2 d_0 and d_0=0. This contradicts alpha!=0.

For existence at degree two, subtract alpha sin(theta) from f. The remaining pure density lies in the range of the pure degree-zero potential map, by the finite Fourier compatibility theorem in topic10. Add alpha t^2/4 to its pure preimage. Finally add a suitable multiple of t to set the free sin(2theta) stream amplitude. This does not change density.

## Relation to the all-order logarithmic construction

The meromorphic potential inverse of topic10 has a double pole at q=0 in its constant angular component. Substitution of polynomial differentiation converts this into two integrations, so its general bound is deg_t C_n <= deg_t F_n+2 at q_n=0. At the other exceptional potential degrees below four, at most one additional logarithmic power is needed. The formal existence theorem is unchanged; the one-power wording in the theory part's Section14.1 needs this exception.

This phenomenon is active for the canonical delta=4/9, f_1=sin(theta) expansion: its first stream resonance is n=9, q_9=0, and its exactly verified a_(9,0) is nonzero. The potential coefficient at that order therefore needs a squared logarithm even though the density coefficient is pure and the stream has degree one.
