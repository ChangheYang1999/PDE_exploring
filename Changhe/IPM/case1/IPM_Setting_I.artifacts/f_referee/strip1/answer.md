The oscillation is demonstrably tied to angular truncation. It does **not** yet identify a singularity of the exact profile or a particular value of \(c_l\). My computations favor adding resolution at **fixed physical height \(y\)** near the axis, rather than using the proposed \(y/|\xi|^{1/A}\) stretch.

There is also a regularity qualification: smoothness of \(H\) follows from a smooth velocity field and the \(C^1\) source condition. It does not follow from the stated \(C^1\) condition alone without an additional regularity argument for the coupled system.

Here are the proved statements, followed by the computations and the proposed remedy.

**For (a), the fixed-field transport argument is particularly simple after dividing by \(y\).** Put
\[
W_2=yb,\qquad q=\rho/y,\qquad f=\log q,
\]
so that \(H=f-2\log x\). Assume \(g_*=\rho_y(P)>0\). Oddness and \(C^1\) regularity in a neighborhood give
\[
q(x,y)=\int_0^1\rho_y(x,ty)\,dt,
\]
hence \(q\) extends continuously to \(P\), with value \(g_*\). Off the axis,
\[
W\cdot\nabla f=1-b.
\]
Writing \(\phi_t\) for the flow of \(W\), backward integration gives
\[
\boxed{\;
f(X)=\log g_*+\int_{-\infty}^{0}[1-b(\phi_tX)]\,dt .
\;} \tag{1}
\]

If \(W\) is \(C^\infty\) near \(P\), this integral is \(C^\infty\). Indeed, the backward flow contracts exponentially. Its spatial derivatives of every fixed order also decay exponentially, by the variational equations and induction. Since \(b(P)=1\), the integrand and all its spatial derivatives have integrable bounds. Thus differentiation under the integral is justified.

Consequently, for a smooth fixed field, \(H\) is smooth and even in \(y\) near \(P\). This regularity propagates along the left axis segment by finite-time flow maps wherever \(W\) remains smooth.

Here is its expansion. Write
\[
\begin{aligned}
W_1&=A\xi+a_{20}\xi^2+a_{02}y^2+O(|(\xi,y)|^3),\\
b&=1+b_{10}\xi+b_{20}\xi^2+b_{02}y^2+O(|(\xi,y)|^3).
\end{aligned}
\]
If
\[
f=\log g_*+u\xi+v\xi^2+t y^2+O(|(\xi,y)|^3),
\]
then direct substitution gives
\[
u=-\frac{b_{10}}A,\qquad
v=-\frac{b_{20}+a_{20}u}{2A},\qquad
t=-\frac{b_{02}+a_{02}u}{2}.
\]
Therefore
\[
\boxed{
H=\log\frac{g_*}{x_*^2}
+\left(u-\frac2{x_*}\right)\xi
+\left(v+\frac1{x_*^2}\right)\xi^2
+t y^2+O(|(\xi,y)|^3).
} \tag{2}
\]
At higher orders, the transport denominators are
\[
iA+2j>0,\qquad (i,j)\ne(0,0).
\]
There is no scalar resonance forcing logarithms or fractional powers in this smooth expansion.

The full-vector-field linearization argument in 13.1 nevertheless needs correction. It checks resonances at eigenvalue \(1\), but the fast component permits
\[
A=2j,\qquad y^{2j}\partial_\xi .
\]
For example, the fixed field
\[
W=(A\xi+d y^A,y)
\]
at even integral \(A\) has invariant
\[
\xi/y^A-d\log y,
\]
while \(\rho=g_*y\) remains perfectly smooth. Logs in characteristic coordinates need not be logs in \(H\). In particular, \(A=10\), or \(c_l=5.5\), is **not** a value selected by removing a scalar resonance in \(H\).

Along the axis, write
\[
W_1=w+a_2y^2+\cdots,\quad
W_2=y(h+b_3y^2+\cdots),\quad
f=f_0+f_1y^2+\cdots.
\]
Then
\[
wf_0'=1-h,\qquad
wf_1'+2hf_1=-b_3-a_2f_0'. \tag{3}
\]
In particular,
\[
f_0(x)=\log g_*+\int_{x_*}^{x}\frac{1-h(s)}{w(s)}\,ds.
\]
The apparent singularity is removable because \(h(P)=1\) and \(w=A\xi+O(\xi^2)\).

More generally,
\[
wf_n'+2nhf_n=S_n
\]
has homogeneous solution
\[
C_\pm|\xi|^{-2n/A}\times\text{a smooth nonzero factor}.
\]
These are **negative**, not positive, fractional powers. Source regularity excludes them and selects the regular particular solution. A nonzero \(h(P)-1\), by contrast, produces a logarithm in \(f_0\).

Let \(H_0=f_0-2\log x\). At every fixed \(r<x_*\) in the smooth region,
\[
\boxed{
H(r,\theta)
=H_0(r)+
\left[r^2f_1(r)-\frac r2H_0'(r)\right]\theta^2+O(\theta^4).
} \tag{4}
\]
There are expansions to every even order. Thus a smooth angular localization near \(\theta=0\) has superalgebraically decaying cosine coefficients. This does **not** imply exponential decay without analyticity, nor superalgebraic decay of the whole-circle coefficients if another angular location is less regular.

That distinction matters here: the supplied centre terms themselves contain an angular power
\[
\cos^{\,4+2/A}\theta,
\]
which is not smooth at the other axis.

The limitation concerning the original \(C^1\) hypothesis is substantive. Even the **local coupled equations** allow finitely smooth source fields with fractional \(H\). To see this, choose nonintegral \(\lambda>2\), set \(g_*=\lambda A\), and construct functions satisfying
\[
w'=A+v,\qquad wv'=v(g_*+v),\qquad
v(\xi)\sim C|\xi|^\lambda,\quad w(\xi)\sim A\xi.
\]
Such functions exist: for \(\xi\ge0\), one explicit parametrization is
\[
\xi=K\int_0^v u^{1/\lambda-1}(g_*+u)^{-1/\lambda}\,du,\qquad
w=K(g_*+v)^{1-1/\lambda}v^{1/\lambda},
\]
extended with \(v\) even and \(w\) odd. Set
\[
W=(w(\xi),\,y(1-v(\xi))),\qquad
\rho=y(g_*+v(\xi)).
\]
Direct calculation gives
\[
\operatorname{div}W=2c_l,\quad
\operatorname{curl}W=-\rho_x,\quad
W\cdot\nabla\rho=\rho.
\]
These fields are at least \(C^2\), have the required source eigenvalues, but
\[
H=\log(g_*+v(\xi))-2\log(x_*+\xi)
\]
contains \(|\xi|^\lambda\).

This is a local example, **not** a global normalized profile with sublinear velocity. It establishes that the requested smoothness cannot be derived merely from local transport, local Darcy coupling, and constant source data. A global bootstrap excluding this behavior remains an additional, unproved step here. Under \(W\in C^{m,\alpha}\), the direct argument guarantees at least \(H\in C^{m-1,\alpha}\); bare \(C^1\) regularity of \(\rho\) only guarantees continuity of \(\rho/y\).

The origin introduces a different fractional-power mechanism. Its linear field is
\[
(-Ax,By),\qquad B=2A+1.
\]
The invariant is \(I=yx^{B/A}\), and
\[
\rho=x^2yF(I).
\]
The first even correction \(F(I)=1+CI^2+\cdots\) gives
\[
C x^{6+2/A}y^3.
\]
This explains the origin exponent \(6+2/A\approx6.19699\). It does not produce a cusp as \(y\to0\) at fixed \(x>0\). The saddle passage map has exponent
\[
A/B\approx0.47653
\]
and logarithmically increasing residence time near the separatrix, which can make this family of characteristics numerically sensitive.

**For (b), I computed the saved shapes directly from their coefficients**, including the centre terms and each file’s physical scale \(L\). The direct reconstruction agrees with the supplied evaluator in \(H\) to \(3.3\times10^{-16}\) on the cross-check. These are shape diagnostics, not a new high-resolution residual audit.

For \(\Delta H=H_{\mathrm{c6f}}-H_{\mathrm{c6d}}\), the signed values are:

| Physical \(r\) | \(\Delta H(0)\) | \(\Delta H(0.015)\) | \(\Delta H(0.03)\) |
|---:|---:|---:|---:|
| 7.60 | −0.380 | +0.584 | −0.320 |
| 8.00 | −0.544 | +0.795 | −0.504 |
| 8.30 | −0.722 | +0.995 | −0.620 |
| 8.47 | −0.889 | +1.014 | −0.681 |
| 8.56 | −0.665 | +0.708 | −0.520 |
| 8.62 | +0.246 | +0.081 | +0.040 |
| 8.70 | +0.162 | −0.004 | +0.107 |

All entries are in \(10^{-6}\). The small differences from the quoted regular-part table arise from retaining all terms and the physical-scale differences.

The sign reversal is near \(P\), but is not exactly pinned to it: the full axis difference vanishes at \(r=8.60524\); its \(m\ge60\) part vanishes at \(8.61488\). This dependence on filtering argues against assigning the sign reversal an exact geometric meaning.

I fitted the packet at seven radii from \(7.6\) to \(8.56\) to one reference profile at \(8.47\), using
\[
z_p=\frac{y}{|x-x_*|^p},
\]
with an independent amplitude and a smooth quadratic background at each radius. On \(0\le\theta\le0.08\):

| Coordinate model | Relative RMS discrepancy, \(m\ge60\) packet |
|---|---:|
| Fixed physical \(y\), \(p=0\) | 0.114 |
| Characteristic stretch, \(p=1/A=0.09850\) | 0.421 |
| Best fitted \(p\) | approximately \(0\) |

Repeating with the **full** difference gives discrepancies \(0.120\) and \(0.418\), respectively. Thus this conclusion is not caused by the \(m=60\) cutoff.

A smooth even fit to the packet at \(r=8.47\) is
\[
\begin{aligned}
10^6\Delta H_{\ge60}(\theta)\approx {}&
e^{-\theta^2/(2\sigma^2)}
\left[
-0.9455\cos(\omega\theta)
+0.9430\frac{\theta}{0.04}\sin(\omega\theta)
\right]\\
&-0.0114+0.0495(\theta/0.08)^2,
\end{aligned}
\]
with
\[
\omega=192.85,\qquad \sigma=0.03282.
\]
Its relative RMS discrepancy is \(0.120\). The corresponding physical scales are approximately
\[
k_y=22.77,\qquad \sigma_y=0.278.
\]
Both angular functions in this fit are even and smooth.

On the common positive-angle interval \(0.003\le\theta\le0.08\), Gaussian-windowed oscillations in \(\theta\) fit substantially better than oscillations in \(\log\theta\): relative discrepancies \(0.134\) versus \(0.644\). This rejects a simple log-periodic description **of the added packet**. It does not exclude a logarithmic or fractional underlying function whose spectral truncation generates that packet.

The claimed power law also needs qualification. Using five-mode RMS blocks at \(r=8.47\), I obtain:

| Fitted modes | Power-law exponent |
|---|---:|
| 60–120 | 2.95 |
| 80–120 | 3.81 |
| 100–130 | 5.76 |

An exponential fit is slightly better than a power law in the first two windows. These short, taper-contaminated spectra do not establish an asymptotic \(m^{-3.4}\) law.

Finally, the origin multiplier is innocuous here:
\[
\chi(8.47)=0.99967363,\qquad \chi^{149}=0.95253.
\]
It attenuates the top mode by only about \(5\%\). The physical radial knots near \(P\) are roughly \(0.0164\) apart. Polar coordinates are regular at \(r\approx8.6\). Neither the coordinate system nor this multiplier creates a singularity at \(\theta=0\).

These computations support the following interpretation of facts (1)–(5), with the causal parts still heuristic.

1. **The band-edge character is established.** Its period follows the cap. Differentiating incompletely represented angular content makes the residual particularly sensitive to the highest modes. The numerical factor \(0.9\) is measured, not a universal transport constant.

2. **The unchanged normalized maximum does not establish a singular limiting solution.** The cap step changes the profile and fit history, rather than truncating one fixed function. Moreover, the physical denominator vanishes proportionally to \(|y|\), and horizontal transport becomes small near \(P\); improvement of the absolute residual need not yield comparable improvement of this ratio. The ratio has a finite axis limit after division by \(\rho\), so normalization alone does not explain the oscillation.

3. **A literal singularity of the finite trial at \(P\) is absent.** At fixed radius its regular angular part is a finite trigonometric polynomial, and its centre terms are analytic near \(\theta=0\). A singularity could belong to a hypothetical limit of the trials, but that has not been demonstrated.

   A simple isotropic point singularity at \(P\) would be seen from a circle through complex angular locations
   \[
   \theta=\pm i\log(x_*/r).
   \]
   The distances are \(0.07241\) at \(r=8.0\) and \(0.01532\) at \(8.47\): a factor \(4.7\) change. The observed packet does not narrow comparably. This particular point-singularity explanation is poorly supported.

4. **A regularized, inadmissible source-data component remains possible.** In the linear model,
   \[
   \rho=y\Phi(\xi/|y|^A).
   \]
   Nonconstant \(\Phi\) violates continuity of \(\rho/y\) at \(P\). A finite smooth fit can nevertheless approximate such behavior outside an unresolved region at low least-squares cost.

   If this mechanism produced
   \[
   H_{\rm bad}\sim C|y|^p|\xi|^{-p/A},
   \]
   then localized cosine coefficients would behave like \(m^{-p-1}\). A genuine exponent \(3.4\) would suggest \(p=2.4\), with radial amplitude \(|\xi|^{-0.2364}\) and characteristic height scale \(|\xi|^{0.0985}\). Neither scaling has been established by the present packet. The direct collapse test favors fixed \(y\).

5. **The exceptional characteristic label is consistent with separatrix sensitivity, not diagnostic of a \(\Phi\)-mode.** It samples a different part of the error and experiences long saddle passage. Also, a non-axis characteristic eventually approaches this source backward in the weak vertical direction. “Reaches \(P\) horizontally” for such a label describes a finite stopping radius; it cannot be its ultimate asymptotic direction. Testing smaller stopping radii is therefore essential before using its \(J\) value as a source singularity diagnostic.

**For (c), I recommend a smooth Cartesian patch with fixed physical \(y\)-resolution.** This is a proposal supported by the measurements, not a demonstrated sub-\(10^{-6}\) refit.

Use a patch covering approximately
\[
7.5<x<8.9,\qquad |y|<0.8,
\]
with additional refinement on \(8.3<x<8.7\). Retain the existing global representation and add smooth, even functions such as
\[
a_j(x)e^{-y^2/(2s_j^2)}\cos(k_jy),\qquad
b_j(x)y\,e^{-y^2/(2s_j^2)}\sin(k_jy).
\]
The measured packet suggests widths \(s_j\) around \(0.2\)–\(0.4\), and frequencies spanning roughly \(k_j=20\)–\(50\). An even spline basis in \(\operatorname{asinh}(y/y_0)\), with \(y_0\approx0.03\)–\(0.05\), is another concrete option.

Include separate axis coefficients and enforce (3), with the regular source boundary values. The remaining patch functions can have their constant and quadratic jets removed if necessary. Do not introduce \(|\xi|\)-dependent singular widths merely to accommodate the proposed characteristic scaling.

For an initial resolution estimate:

- use \(\Delta x\approx0.008\) near \(P\);
- sample or collocate at \(\Delta y\approx0.005\)–\(0.01\) in the active strip;
- continue more coarsely outside it.

The residual’s observed zero spacing is about \(0.10\) in physical \(y\), so this supplies roughly 10–20 samples per lobe. The elliptic evaluation and between-node residual check must also resolve those scales.

A stronger alternative is to use (1) as the local representation itself, with a source Taylor expansion to terminate backward integration. This eliminates the local transport residual for a **fixed** \(W\); the coupled elliptic consistency still has to be solved. It directly prevents arbitrary source-data functions from entering the trial.

If one merely increases the global cap to \(M=200\), the observed band-edge mechanism predicts a zero spacing near
\[
\frac{\pi}{2(0.9)200}=0.00873.
\]
It does not predict that the maximum will fall below \(10^{-6}\). Assuming an actual \(m^{-3.4}\) coefficient tail and one differentiated tail would give the optimistic estimate \(M\approx284\) for a factor \(2.44\) reduction, but the existing cap experiment does not validate that extrapolation.

**For (d), an identity-free selection criterion is conceivable, but none is established by these data.** One could continue fully refitted profiles in \(c_l\), extract a signed coefficient of a verified nonsmooth asymptotic component, and require that coefficient to vanish. Such a coefficient must have a stable definition under changes of radius, cutoff, representation, and characteristic stopping radius.

Raw high-mode amplitudes fail this test. For example, on the supplied \(c6d\) soft direction, linearly extrapolating the axis sum of modes \(m\ge60\) to zero gives:

| Radius | Formal \(c_l\) offset |
|---:|---:|
| 8.30 | \(-0.00657\) |
| 8.47 | \(-0.00333\) |
| 8.52 | \(-0.000758\) |

At \(r=8.47\), changing the cutoff from \(60\) to \(80\) changes the offset to \(-0.00660\). These are not proposed exponents; they demonstrate that “make the high modes vanish” is not yet a well-defined criterion.

Using the observed residual sensitivity \(5\times10^{-4}\) per unit \(c_l\) as an optimistic scale, determining \(c_l\) within \(10^{-4}\) would require the relevant signed defect and its systematic errors to be controlled below about \(5\times10^{-8}\). For \(10^{-5}\), the requirement is \(5\times10^{-9}\). Current representation effects are larger.

The fixed value \(c_l=5.5753626\) is therefore a useful, better-performing trial value; it has **not** removed the strip. Neither that experiment nor extrapolation of unsigned lobe maxima selects the exact exponent. A matched continuation with the local Cartesian representation is the next discriminating test.

The complete local proofs and reproducible calculations are retained in [PROOF.md](PROOF.md) and the [reading-order index](INDEX.md).

Opus 5.5 collaboration was attempted through both existing Bedrock profiles; both failed for unavailable credentials. No other model was substituted.