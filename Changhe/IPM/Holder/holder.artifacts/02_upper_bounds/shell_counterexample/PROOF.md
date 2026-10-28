# The diagonal does not maximize the sphere-term norm

## Statement

For $0<\alpha<1$, define

$$S_\beta(f)=\frac1{2\pi}\int_0^{2\pi}\cos2\theta\cos(\theta-\beta)
f(\cos\theta,\sin\theta)\,d\theta.$$

Inputs are real functions on $\mathbb R^2$ with Euclidean alpha-Hölder seminorm at most 1. The proposed identity $\sup_\beta\|S_\beta\|=\|S_{\pi/4}\|$ is false: it fails at the exact rational value $\alpha=99/100$.

## Exact diagonal norm

Put $\phi=\theta-\pi/4$. Then the density becomes $-2\sin\phi\cos^2\phi$. Reflection $\phi\mapsto-\phi$ pairs equal positive and negative densities at chord distance $2|\sin\phi|$. The signed alpha-power of the coordinate normal to the reflecting line attains equality. Thus

$$\|S_{\pi/4}\|=\frac{2^\alpha}{\pi}
\mathrm B\left(\frac{\alpha+2}{2},\frac32\right).$$

Here $\mathrm B$ is Euler's beta integral. This proof establishes the diagonal formula, but supplies no comparison with other directions.

## Explicit axis witness

Let $e=(1,0)$ and define

$$u(z)=(2-|z-2e|)_+-(2-|z+2e|)_+.$$

The interiors of the two radius-2 balls are disjoint. The function is the signed distance to its zero set within each ball and zero outside, so the signed-distance argument from the main lower-bound proof shows that $u$ is 1-Lipschitz. Therefore

$$f(z)=2^{\alpha-1}\operatorname{sign}(u(z))|u(z)|^\alpha$$

has alpha-Hölder seminorm at most 1.

On the first-quadrant unit circle, $u(\cos\theta,\sin\theta)=(2-\sqrt{5-4\cos\theta})_+$. Symmetry gives

$$S_0(f)=\frac2\pi\int_0^{\pi/2}\cos2\theta\cos\theta\,
2^{\alpha-1}(2-\sqrt{5-4\cos\theta})_+^\alpha\,d\theta.$$

The integral includes its negative contributions; no sign has been discarded.

## Reproducible certificate

`../../code/certify_shell_counterexample.py`, relative to the artifacts root, evaluates this integral by interval Riemann sums at $\alpha=99/100$. It uses 32768 equal subintervals of $[0,\pi/2]$ and 128-bit python-flint ball arithmetic. On each interval, cosine, square root, positive part, and alpha-power are enclosed before multiplication by the signed trigonometric density. Summing these interval ranges times the exact interval widths encloses the entire integral. The positive-part power is evaluated through its endpoint values, avoiding an invalid fractional power of a ball that extends below zero.

The resulting axis-witness interval lies strictly above $0.25453$, while the exact diagonal formula is less than $0.24938$. In particular, the gap is greater than $0.00515$. Full enclosures are retained in `../../data/shell_counterexample_certificate.json`, relative to the artifacts root. The script asserts positivity of the interval gap.

This refutes diagonal maximality. It does not refute either of the two uniform sphere upper bounds in the parent proof, which remain valid.

## Dependencies and scope

Only the signed-distance Hölder estimate and the retained interval computation are used. The preliminary discrete transport calculation in `data/shell_transport_exploration.json` suggested the witness search; it is not part of the proof.
