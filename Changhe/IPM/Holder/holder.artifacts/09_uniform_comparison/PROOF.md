# A certificate principle for comparison over an exponent interval

## Scope and statement

This result supplies a rigorous interpolation method for comparing the explicit upper plan and the polygonal lower witness on a continuum of Hölder exponents. It does not itself assert a numerical ratio. The operator definitions and spaces are those in `../01_setup/PROOF.md`.

Fix the phase-grid parameter $m$ in the reflection-orbit upper theorem, and denote that theorem's right side by $U(\alpha)$. Fix a polygonal shape $a>0$, and denote its exact lower witness by $I(\alpha,a)>0$. Then

$$\alpha\longmapsto \log U(\alpha),\qquad
\alpha\longmapsto \log\frac{I(\alpha,a)}\alpha$$

are convex on $(0,1)$.

Consequently certified upper values of $U$ at two endpoints give a geometric-interpolation upper bound throughout the interval. Certified lower and upper values of the same witness $I/\alpha$ at neighboring exponents give explicit supporting-line lower bounds, as detailed below. Combining them certifies a uniform ratio on an exponent interval from finitely many nodal certificates.

## Logarithmic convexity of the upper plan

The local term has an integral representation against a positive measure, with integrand equal to a fixed positive distance raised to the exponent $\alpha$. This follows directly from the reflection-pairing integral before the radial variable is integrated.

The exact third-harmonic tail has the same property. Each higher-harmonic majorant in the displayed $H_\alpha$ is also a positive integral of a fixed distance to the power $\alpha$: restore the radial integral over $r\ge1$ and use the fixed Jensen distance in the angular factor. The convergent positive series preserves logarithmic convexity.

For each fixed phase, the four-point transport plan is independent of $\alpha$. Indeed, whether the horizontal or vertical plan is used is determined solely by the comparison of its two mass magnitudes. Its cost is a positive linear combination of horizontal, vertical and diagonal distances to the power $\alpha$. Integrating the plan gives another positive moment integral. The sum of these local, regular and exterior costs is logarithmically convex by Hölder's integral inequality.

The finite maximum over phases preserves logarithmic convexity. To see this while retaining the phase-independent terms, write $U$ as the maximum of the full positive costs for the individual phases. The grid-inflation factor is constant in $\alpha$ and merely rescales the positive regular measure. This proves the first assertion. Taking the minimum with a different upper-bound family is not part of this assertion: a minimum need not preserve logarithmic convexity.

## Logarithmic convexity of the lower moment

The positive layer-cake identity in `../05_team_audit/structured_layercake/PROOF.md` gives

$$\frac{I(\alpha,a)}\alpha
=\frac12\int_0^\infty(2t)^\alpha J_a(t)\,\frac{dt}{t},\qquad J_a(t)>0.$$

The integral is finite for every $0<\alpha<1$, by the proved endpoint expansions. Hölder's integral inequality proves logarithmic convexity. The fixed shape is essential here; the maximum over separately optimized shapes cannot be used to justify secant slopes from different witnesses.

## Safe supporting lines from nodal enclosures

Let $p<a<b<q$ be exponents. Suppose $h(t)=I(t,a_0)/t$ for one fixed shape $a_0$, with certified enclosures $0<\ell_t\le h(t)\le u_t$ at the four nodes. Convexity of $g=\log h$ gives, for $t\in[a,b]$,

$$g(t)\ge L_a(t):=
\log\ell_a+\frac{t-a}{a-p}(\log\ell_a-\log u_p),$$

$$g(t)\ge L_b(t):=
\log\ell_b+\frac{b-t}{q-b}(\log\ell_b-\log u_q).$$

For the first inequality, the actual secant from $p$ to $a$ is no larger than any supporting slope to its right; replacing $g(a)$ downward and $g(p)$ upward only lowers the resulting affine function. The second is the reflected argument. These lines remain valid even if a numerical derivative has not been computed.

If $U(a)\le A$ and $U(b)\le B$, define the affine upper line

$$E(t)=\frac{b-t}{b-a}\log A+\frac{t-a}{b-a}\log B.$$

Then the pointwise comparison satisfies

$$\log\frac{U(t)}{I(t,a_0)}
\le E(t)-\log t-\max\{L_a(t),L_b(t)\}.$$

On each region where one lower line is the maximum, the right side is affine minus $\log t$, hence convex. Its maximum over $[a,b]$ is therefore achieved among the two endpoints and, if present, the intersection of the two lower lines. An interval-arithmetic implementation can enclose these three evaluations. Alternatively, choose any fixed subdivision point and use either valid lower line on each subinterval; convexity then reduces each subinterval to its endpoints, without solving for a possibly uncertain intersection.

This is a proof of a finite verification procedure. No numerical uniform comparison is claimed until those nodal bounds and endpoint evaluations have been certified.
