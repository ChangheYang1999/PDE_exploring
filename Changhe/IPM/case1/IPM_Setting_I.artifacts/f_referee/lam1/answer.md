The exponent \(\lambda=g_*/A\) is correct for the proposed axis-visible conormal branch. Its extension into the plane is consistent at leading order, including with nonzero \(a_2\), but this does **not** establish a nonlinear planar solution with that layer, or a global family varying \(c_l\).

Two corrections materially affect the numerical interpretation:

- A \(2.9306\)-power predicts an unbounded third derivative, not a finite third-derivative jump.
- The supplied shape files use **degree-seven splines**, not cubic splines. Their fitted “jump” is a feature of extrapolation across a smooth approximation.

I distinguish exact identities, conditional expansion calculations, and numerical evidence below.

For **(a)**, the axis equations are correct. Define
\[
q(x)=\rho_y(x,0),\quad w(x)=W_1(x,0),\quad
h(x)=W_{2y}(x,0),\quad a_2(x)=\tfrac12W_{1yy}(x,0).
\]
Differentiating transport once in \(y\), restricting divergence to the axis, and differentiating curl once in \(y\) give
\[
\boxed{wq'=(1-h)q,\qquad w'+h=2c_l,\qquad h'+q'=2a_2.}
\]
These identities require only the stated \(C^{2,\alpha}\) regularity, assuming the corresponding elliptic velocity exists.

The Taylor notation needs qualification: \(C^{2,\alpha}\) and oddness give
\[
\rho(x,y)=yq(x)+O(|y|^{2+\alpha}),
\]
not generally \(O(y^3)\). Initially \(q,h\) have only \(C^{1,\alpha}\) trace regularity.

Write \(g=q(x_*)>0\). Transport at \(P\) forces \(h(P)=1\), and divergence gives \(w'(P)=A=2c_l-1\). With
\[
\xi=x-x_*,\quad v=q-g,\quad u=1-h,\quad
F(\xi)=2\int_0^\xi a_2(x_*+t)\,dt,
\]
the exact equations become
\[
\boxed{u=v-F,\qquad w'=A+u,\qquad wv'=u(g+v).}
\]
For a singular perturbation whose contribution to \(F\) is higher order, the indicial equation is
\[
A\xi v'_{\rm sing}=gv_{\rm sing},
\]
hence
\[
v_{\rm sing}=C_+\xi_+^\lambda+C_-(-\xi)_+^\lambda,
\qquad
\boxed{\lambda=g/A}.
\]
The changes in \(w\) begin at order \(|\xi|^{\lambda+1}\), so they do not alter this exponent.

**The qualification about \(F\) is essential.** The axis equations alone do not prohibit a contribution to \(F\) of the same order as \(v\). Consequently they alone neither prove the polarization \(h_{\rm sing}=-q_{\rm sing}\) nor classify the possible singularities.

The \(a_2=0\) strip construction is an exact nonlinear local example:
\[
w'=A+v,\qquad wv'=v(g+v),\qquad
\rho=y(g+v),\quad W=(w,y(1-v)).
\]
Direct substitution verifies all three local PDEs. Nonzero fractional branches exist: on the positive branch, for example,
\[
w=K v^{A/g}(g+v)^{1-A/g},\qquad
\xi=K\int_0^v t^{A/g-1}(g+t)^{-A/g}\,dt,
\]
so \(v\sim C\xi^{g/A}\). Negative amplitudes and the other half-axis are treated similarly. This proves local compatibility with the differential equations; it does not enforce the globally selected Biot–Savart inverse, centre normalization, or far field.

Here is the planar calculation with nonzero \(a_2\). Its hypothesis is a smooth invariant curve and a conormal expansion with remainders that can be differentiated to the required orders. **I do not prove that every \(P_2\) solution has such an expansion.**

Choose
\[
\Gamma=\{x=\gamma(s),\ y=s\},\qquad
n=x-\gamma(y),\qquad D=1+\gamma'^2,
\]
and put
\[
V(s)=W_2(\gamma(s),s),\qquad R(s)=\rho(\gamma(s),s).
\]
Suppose the leading nonsmooth density is
\[
\rho_{\rm sing}=b_+(s)n_+^\lambda+b_-(s)(-n)_+^\lambda.
\]
For either side, write its amplitude as \(b\). The elliptic equation forces
\[
\boxed{
W_{\rm sing}=-\frac{b(s)}{D(s)}(\gamma'(s),1)n_\pm^\lambda
+\text{higher normal orders}.
}
\]
One can check this directly: if \(F_\pm'(n)=n_\pm^\lambda\), take
\[
\psi_{\rm sing}=-\frac{b(s)}{D(s)}F_\pm(n).
\]
Its leading normal Laplacian gives \(\rho_x\), and its perpendicular gradient gives the displayed velocity. The leading singular velocity is tangent to \(\Gamma\). Remote Biot–Savart contributions change the smooth local part, not this leading singular coefficient.

Define the normal expansion rate by
\[
W\cdot\nabla n=\kappa(s)n+O(n^2).
\]
Invariance and divergence imply
\[
\kappa=2c_l-V',\qquad VR'=R.
\]
Collecting the \(n_\pm^\lambda\) coefficient in transport gives
\[
\boxed{
Vb'+\left(\lambda\kappa-1-\frac{R'}D\right)b=0.
}
\]
Indeed, background transport contributes \(Vb'+\lambda\kappa b\), while singular velocity acting on the regular density contributes \(-bR'/D\).

Near \(P\),
\[
V(s)\sim s,\qquad R(s)\sim gs,\qquad \kappa(s)\to A.
\]
For the axis-visible odd branch \(b(s)\sim Cs\), the amplitude equation reduces to
\[
\lambda A=g.
\]
Along a regular portion of \(\Gamma\),
\[
b(s)=b(s_0)\exp\!\left[
\int_{s_0}^{s}
\frac{1+R'(t)/D(t)-\lambda\kappa(t)}{V(t)}\,dt
\right].
\]
Thus the amplitudes evolve, but **the exponent stays fixed**. Replacing it by a pointwise quotient along the curve is incorrect. A varying exponent would produce an additional \(Vb\lambda'(s)n^\lambda\log|n|\) term.

At \(s=0\), differentiating the displayed singular velocity in \(y\) gives
\[
h_{\rm sing}=-q_{\rm sing}.
\]
This proves the claimed polarization within the conormal expansion.

Nonzero \(a_2\) bends the curve. Writing
\[
\gamma(s)=x_*+\beta s^2+\cdots
\]
and imposing invariance gives
\[
\boxed{\beta=\frac{a_2(P)}{2-A}.}
\]
As a further consistency check, expansion of the stream function gives
\[
a_{2,\rm sing}=-3\beta q_{\rm sing}
+\text{higher orders}.
\]
Thus \(F_{\rm sing}\) starts at order \(|\xi|^{\lambda+1}\), exactly as required by the axis indicial calculation.

These are necessary, consistent coefficient equations. They are not a convergence or existence proof for the full nonlinear conormal expansion.

There are two qualifications about regularity and the curve:

- For a nonzero layer on an open segment, \(2<\lambda<3\) gives \(C^{2,\lambda-2}\), but neither \(C^3\) nor \(C^{2,\alpha}\) with \(\alpha>\lambda-2\). The endpoint is allowed for a pure power; logarithmic factors can spoil it. The factor \(y\) does not save regularity on a neighbourhood of \(P\), because the layer contains points with \(y\ne0\).
- The axis trace alone does not prove this obstruction. For example,
  \[
  \rho(\xi,y)=y(\xi^2+y^2)^{\lambda/2}
  \]
  is \(C^3\) for \(\lambda>2\), yet \(\rho_y(\xi,0)=|\xi|^\lambda\). This is a trace counterexample, not an IPM solution.

Also, “the weak manifold” requires a specification at this regularity. Even \((A\xi,y)\) has the invariant curves \(\xi=c|y|^A\), all tangent to the weak direction. A chosen sufficiently smooth germ or continued characteristic resolves this ambiguity; the tangent condition alone does not.

For **(b)**, no global dimension count follows from the two local amplitudes.

The global elliptic inverse, centre conditions, far field, and continuation along \(\Gamma\) can determine \(C_\pm\), force them to vanish, or leave freedom. The amplitude ODE tells you how an existing amplitude propagates; it does not tell you which global amplitudes are admissible.

Even the local two-amplitude count is not exhaustive without a stronger expansion hypothesis. Formally, if the first odd tangential coefficient is \(b(s)\sim Cs^p\), the same calculation gives
\[
\lambda_p=\frac{1+g-p}{A}.
\]
Branches with \(p=3,5,\ldots\) are invisible to the leading axis trace. This is a warning against counting all \(P_2\) freedom through \(q\), not a proof that these additional branches exist globally.

A Fredholm or kernel statement also needs a fixed Hölder exponent, far-field weights, boundary conditions, and normalization. There is a further difficulty for a family whose layer moves:
\[
\partial_\varepsilon
\bigl(x-\gamma_\varepsilon(y)\bigr)_+^\lambda
=
-\lambda\,\partial_\varepsilon\gamma_\varepsilon(y)
\bigl(x-\gamma_\varepsilon(y)\bigr)_+^{\lambda-1}.
\]
This derivative generally leaves \(C^{2,\alpha}\). Such a family need not produce a kernel vector in the naive fixed-coordinate function space. Interface-adapted coordinates or a weaker linearization space may be necessary. Varying \(\lambda\) likewise introduces \(n^\lambda\log|n|\), which requires care at the endpoint Hölder exponent.

Therefore:

- Extra global kernel or a \(c_l\)-family is possible, but unproved.
- Local free amplitudes do not establish either.
- Even a verified kernel would require nonlinear solvability analysis before concluding that a family exists.

The reported softness establishes poor conditioning of the finite fitting problem. It does not establish nonuniqueness. Agreement inherited through successive bases is not independent evidence of six-digit accuracy. The relevant numerical object is a fully reoptimized objective-versus-\(c_l\) curve, repeated under refinement and independent initialization.

For **(c)**, a least-squares artefact is a serious possibility—and velocity feedback makes your proposed mechanism stronger.

At fixed \(P,c_l\), consider a paired cubic defect
\[
\delta q=\frac{J}{6}\xi_+^3,\qquad
\delta h=-\delta q+O(\xi_+^4),\qquad
\delta w=\frac{J}{24}\xi_+^4+O(\xi_+^5).
\]
For the divided axis residual
\[
T=wq'+(h-1)q,
\]
linearization gives
\[
\boxed{
\delta T=\frac{(3A-g)J}{6}\xi_+^3+O(\xi_+^4).
}
\]
The term \(AJ\xi^3/2\) accounts only for \(w\,\delta q'\). The term \(q\,\delta h\) supplies the near cancellation.

From the exported candidate,
\[
3A-g\simeq0.7044088,\qquad
\frac{3A-g}{3A}\simeq0.023127.
\]
The coupled cubic defect is therefore about **43 times less visible** at leading order than the transport-only estimate suggests. This calculation demonstrates a mechanism; it does not identify the measured feature with that particular defect.

The ratio near \(-1\) does not decide between a genuine mode and an artefact. The elliptic response produces this polarization for thin normal density features even when transport is not satisfied. Under sufficient one-sided regularity the exact identity gives
\[
[h''']+[q''']=2[a_2''],
\]
but independently fitted extrapolations need not obey that identity.

My read-only checks reproduce the reported feature:

| Quantity | c6d | c6f |
|---|---:|---:|
| \(g/A\) | 2.93061874 | 2.93061836 |
| Fitted \([H''']\), window \(0.05\)–\(0.5\) | 0.124091 | 0.120068 |
| Window \(0.1\)–\(0.8\) | 0.116038 | 0.114896 |
| Window \(0.2\)–\(1.2\) | 0.126651 | 0.126346 |
| Actual analytic \(H'''(P)\) | −0.0729153 | −0.0927353 |

All seven supplied shapes store `spline_order=7`, passed as the degree argument to SciPy’s `BSpline`. Their interior knots are simple, so these trials are \(C^6\) across knots and analytic between them. In particular, their literal \([H''']\) at \(P\) is zero. SciPy explicitly defines this argument as the spline degree. 

The nearest knots in c6d and c6f are about \(0.0065055\) to the right of \(P\). My axis evaluation agrees with the supplied `axis_H` to \(2.3\times10^{-16}\) on 201 points; a separate fit confined to the knot span containing \(P\) confirms the analytic third derivatives above.

For c6d, the three fitted \(([q'''],[h'''])\) pairs are approximately
\[
(3.7023,-3.3629),\quad
(3.4742,-3.3162),\quad
(3.7953,-2.9895).
\]
Their ratios reproduce your range.

The small control values are confirmed for the smallest window. They are not uniform across all three windows: at \(x_*+0.8\), for example, c6d gives about \(0.0549\) and \(-1.5704\) in the two larger windows. The largest crosses the feature at \(P\). Thus the control bound needs its window qualification.

For a genuine fractional term,
\[
q_{\rm sing}'''=
\begin{cases}
K_\lambda C_+\xi^{\lambda-3},&\xi>0,\\
-K_\lambda C_-(-\xi)^{\lambda-3},&\xi<0,
\end{cases}
\qquad K_\lambda=\lambda(\lambda-1)(\lambda-2).
\]
There is no finite limiting jump. Scaling both fitting windows by \(\epsilon\) scales their fractional contribution as \(\epsilon^{\lambda-3}\). Here that grows only about \(17\%\) per decade of shrinking scale, so apparent window stability is weak evidence. Cancellation between sides can also conceal this growth.

Shrinking windows in the existing trials reaches knot-scale oscillations rather than a stable fractional scaling regime.

The strongest practical numerical test is a combined restart and convergence experiment:

1. **Remove the resolved feature from the initial guess.** Smoothly patch \(H\) across a small tube around the proposed curve, preserve parity and centre normalization, and project back into the trial space. Also use starts with opposite fitted amplitudes. Refit at fixed \(c_l\) first, then allow \(c_l\) to vary, with fresh optimization state.

2. **Compare representations and radial resolutions.** Use the original basis, shifted/refined radial knots, and an explicit fractional enrichment. A simple new knot at \(P\) in the actual degree-seven basis still preserves \(C^6\). To allow a cubic third-derivative jump requires total knot multiplicity five, leaving \(C^2\). A radial knot is only an axis pilot, since the predicted interface is curved.

3. **Validate away from fitting nodes.** Compare the original objective, independently sampled residuals, the divided axis residual \(T\), and the curl identity. The original density residual vanishes exactly on the axis by parity, so an axis row alone tests little.

4. **Measure scaling on each side.** Use fourth differences at normal distances \(h,2h,\ldots,5h\), and repeat for dyadic \(h\), on the axis and several transverse slices. These annihilate a cubic and give \(h^\lambda\) for the proposed fractional term, versus \(h^4\) for a smooth background. Require a scale range above the representation scale and convergence under refinement. Test \(\lambda=g/A\), rather than estimating it freely from one polynomial-plus-power fit.

Regeneration from independent starts would address inheritance, but could still reproduce an optimizer artefact. Stable amplitudes, exponent, physical location, amplitude transport, and independently checked residuals under refinement would be substantially stronger evidence. No finite numerical experiment proves continuum existence.

For **(d)**, the appropriate enrichment is curved and coupled to the elliptic solve. Locally, where \(a>0\), use
\[
\boxed{
H=H_{\rm reg}
+\chi(n,s)\bigl[d_+(s)n_+^\lambda+d_-(s)(-n)_+^\lambda\bigr],
\qquad
\lambda=\frac{\rho_y(P)}{2c_l-1}.
}
\]
Here \(n=x-\gamma(y)\), and \(\chi\) is smooth, equals one on a smaller tube containing \(P\), and tapers away before the centre and imposed far field. Reflect the construction near \(-P\) to preserve evenness in \(x\). Test several cutoff widths.

Since \(d=b/R\), its leading amplitude equation is
\[
\boxed{
Vd'+\left(\lambda\kappa-\frac{R'}D\right)d=0,
\qquad d_\pm(0)=C_\pm/g.
}
\]
The amplitudes in \(H\) are even in \(y\). Recompute the full velocity from the enriched density; do not impose an independent correction to \(h\). Cutoff transitions produce real transport forcing, which the global fit must accommodate.

For the exported c6d field I obtain
\[
a_2(P)\simeq0.08954942,\qquad
\gamma(y)=x_*-0.01098399\,y^2+\cdots.
\]
In polar coordinates this becomes
\[
r(\theta)=x_*+3.488\,\theta^2+\cdots.
\]
Thus the proposed layer initially bends toward increasing polar radius. It is not a circular radial feature.

A correctly coupled layer cancels the leading \(|n|^\lambda\) transport residual. Under the assumed expansion, a leading-order enrichment leaves subsequent terms of orders \(|n|^{\lambda+1}\) and \(|n|^{2\lambda}\), plus cutoff effects. **A genuine mode does not require a residual spike at \(P\).** Rounding it on normal scale \(\epsilon\) can produce an error of order amplitude times \(\epsilon^\lambda\), with an additional local \(y\) factor in the density residual.

The observed strip is therefore plausible as an approximation response to a conormal layer, but it is not diagnostic. Band-edge angular oscillations can also arise from projection, quadrature, radial under-resolution, or optimization. Increasing only the angular cap need not resolve any of those. The predominantly left-of-\(P\) location is not the predicted curve itself, although approximation errors may lie to either side.

I reproduce a maximum of approximately \(2.447\times10^{-6}\) in the inspected c6d strip using
\[
|W_1\rho_x|+|W_2\rho_y|+|\rho|
\]
as denominator. The export’s stored `denominator` is different and gives \(6.844\times10^{-7}\) at the same point. Future comparisons should identify the normalization explicitly. Only c6d fields were supplied, so I did not independently verify the residual comparison between angular caps.

The detailed local proofs and numerical record are in [PROOF.md](PROOF.md), with reproducible checks listed in [INDEX.md](INDEX.md). No full solver refit or global existence/kernel proof was performed.

Opus 5.5 collaboration was unavailable: the permitted Python Bedrock client failed credential retrieval before inference. No model ran, and no substitute was used.