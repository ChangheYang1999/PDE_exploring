# A physical cancellation bound for critical Wiener moments

Status: proved analytic lemma. The companion 96-point numbers are FLOAT
screens; their whole-plane radial integrals have not yet been certified.

Use the Fourier convention hat f(xi)=integral exp(-ix·xi)f(x)dx. Let m be a
nonnegative integer, and let f be smooth with all-order symbol growth
\(f\in S^{m-\gamma}\), gamma>0. Define the scalar or vector derivative
\[
h=\begin{cases}\Delta^{(m+2)/2}f,&m\text{ even},\\
\nabla\Delta^{(m+1)/2}f,&m\text{ odd}.
\end{cases}
\]
Then h is L1, its components have zero integral, and its transform has
Euclidean norm |xi|^(m+2)|fhat(xi)| away from zero. Polynomial distribution
terms at zero play no role in the ordinary Fourier moments below.

Let E_j=||D^j f||2² for j=m+1,m+2; both are finite because gamma>0.
For every lambda,t>0, define
\[
L(s)=\begin{cases}s,&0\le s\le2,\\2+2\log(s/2),&s>2.\end{cases}
\]
Then the exact whole-plane estimate is
\[
\boxed{
\frac1{(2\pi)^2}\int|\xi|^m|\widehat f(\xi)|\,d\xi
\le\frac1{2\pi}\int L(\lambda|x|)|h(x)|\,dx
+\sqrt{\frac{E_{m+1}+tE_{m+2}}{4\pi}
\log\left(1+\frac1{t\lambda^2}\right)}.}
\tag{1}
\]
This avoids assigning a divergent global L2 norm to D^m f and avoids
introducing high derivatives of an artificial spatial partition.

## Proof

The derivative immediately preceding h has growth -1-gamma, so its flux
over a radius-R circle tends to zero. Integration by parts therefore proves
integral h=0 componentwise. The decay h=O(r^-2-gamma) also proves L1
integrability with the logarithmic weight in (1).

The mean-zero identity gives, for rho=|xi|,
\[
|\widehat h(\xi)|
=\left|\int(e^{-ix\cdot\xi}-1)h(x)\,dx\right|
\le\int\min(2,\rho|x|)|h(x)|\,dx.
\]
On rho<=lambda, use |fhat|=rho^(-m-2)|hhat| and polar coordinates.
Tonelli's theorem and
\[
\int_0^\lambda\frac{\min(2,\rho r)}\rho\,d\rho=L(\lambda r)
\]
give precisely the first term in (1).

For rho>=lambda, Fourier Cauchy-Schwarz and Plancherel give
\[
M_{high}^2\le(E_{m+1}+tE_{m+2})\frac1{(2\pi)^2}
\int_{|\xi|\ge\lambda}\frac{d\xi}{|\xi|^2(1+t|\xi|^2)}.
\]
The remaining radial integral equals
\(\log(1+(t\lambda^2)^{-1})/(4\pi)\), proving (1).

## Direct applicability to the actual stream

The verified Candidate 013 structure gives psi* in S^(2-gamma),
gamma=1-1/c. For each multiindex alpha of length zero, one, or two,
\[
f=x^\alpha\psi_*,\qquad m=2+|\alpha|
\]
satisfies the hypotheses. Thus (1) directly supplies the three critical
moment families in `CTR_WEIGHTED_KERNEL_REDUCTION_v01.md`:
M2(psi), M3(x_i psi), and M4(x_i x_j psi). The higher moments M4 and M5
where their physical L2 norms are finite use
\[
M_j(f)\le\sqrt{(\sqrt{E_jE_{j+2}}+E_{j+1})/(2\pi)}.
\tag{2}
\]
This follows from the same Fourier Cauchy-Schwarz argument with denominator
(lambda²+rho²)² and optimization in lambda. For M4.1 one may use the
log-convex interpolation M4.1<=M4^.9 M5^.1.

There is a convenient one-dimensional upper for the physical integral.
If e_h(r)=r integral_0^(2pi)|h(r,theta)|²dtheta, angular Cauchy-Schwarz gives
\[
\int L(\lambda|x|)|h(x)|dx
\le\int_0^\infty L(\lambda r)\sqrt{2\pi r e_h(r)}\,dr.
\tag{3}
\]
All radial densities in (3) come from finite harmonic sums and exact Arb
radial derivatives. Even h uses powers of the polar Laplacian; odd h uses
the radial and angular gradient of such a power. No angular truncation is
needed. A continuum radial quadrature with origin/exterior certificates
would make (1)--(3) a reproducible numerical obligation.

The script `Ctr_physical_cancellation_screen.py` evaluates these expressions
from the actual source's point evaluations, while labeling its finite
Gauss quadrature and radius cutoff as uncontrolled. No Ctr operator upper
or stationary existence statement follows from the screen alone.
