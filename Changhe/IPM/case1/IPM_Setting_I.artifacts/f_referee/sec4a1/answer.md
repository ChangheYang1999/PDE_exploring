I take R2 as given. One preliminary correction: for the **trial’s** source, writing \(h_0=\partial_yW_2(P)\), incompressibility gives
\[
DW(P)=\operatorname{diag}(a_f,h_0),\qquad a_f=2c_l-h_0.
\]
Thus \(a_f=A=2c_l-1\) only when \(h_0=1\).

**S1 — CORRECT WITH QUALIFICATION. The stated regularity is a lower bound, not the sharp regularity of the density.**

The Cartesian expression is correct:
\[
f(x,y)=|x|^{p_3-2}y^2(L^2+x^2+y^2)^{-p_3/2}T(2q-1).
\]
Writing \(p_3=6+\beta\), this is \(C^{4,\beta}_{\mathrm{loc}}\). At points \((0,y_0)\), \(y_0\ne0\), where its smooth coefficient is nonzero, this regularity is sharp.

The integer angular modes are regular at the origin. To see the cancellation explicitly, set
\[
t=u^2,\qquad b_m(q(t))=tB_m(t).
\]
On the first knot interval, \(B_m\) is analytic: \(b_m\) is polynomial there, \(q\) is analytic, and \(b_m(0)=0\). For \(m\ge1\),
\[
\chi^{m-1}b_m(q(t))\cos(2m\theta)
=
\frac{\operatorname{Re}(x+iy)^{2m}}{L^{2m}}
\frac{B_m(t)}{(t+r_0^2)^{m-1}}.
\]
Since \(r_0>0\), this is analytic near the origin. The \(m=0\) term is simply \(tB_0(t)\).

Away from the origin, the angular factors are smooth. Degree-seven splines with simple interior knots have continuous derivatives through order six and Lipschitz sixth derivatives. Consequently, **each complete integer angular spline term is \(C^{6,1}_{\mathrm{loc}}(\mathbb R^2)\)**, including at the origin. “Analytic at the origin” should refer specifically to these integer angular terms, within the first knot interval; it does not describe the fractional term.

There is an important improvement when passing from \(H\) to \(\rho_h\). Write
\[
H=G+|x|^{p_3-2}B,\qquad G\in C^{6,1}_{\mathrm{loc}},\quad B\ \text{smooth}.
\]
Then
\[
\rho_h=x^2ye^G
+ye^G\sum_{j\ge1}\frac{B^j}{j!}|x|^{2+j(p_3-2)}.
\]
The first nonsmooth power in the density is \(|x|^{p_3}\), not \(|x|^{p_3-2}\). Therefore
\[
\boxed{H,a\in C^{4,\beta}_{\mathrm{loc}},\qquad
\rho_h\in C^{6,\beta}_{\mathrm{loc}}.}
\]
For the supplied candidate, \(T\not\equiv0\), so these are sharp: \(\rho_h\) is not \(C^{6,\gamma}_{\mathrm{loc}}\) for \(\gamma>\beta\), and is not \(C^7_{\mathrm{loc}}\). These sharpness claims would need qualification for a family member with \(T\equiv0\).

The stored parameters give
\[
k=0.17936053129375418,\qquad
\boxed{\beta=\frac{2k}{2-k}=0.19703025709006358},
\]
and
\[
p_3=6.197030257090064.
\]
Even using \(k=0.17936\) gives \(p_3=6.197029615959223\). Thus the quoted \(6.19698\) is inconsistent with the exponent formula, rather than a correct rounding of it.

All terms in \(H\) vanish at the origin, so \(a(0)=1\) structurally, independently of coefficient accuracy. The parity is correct. The trial satisfies the regularity and normalization requirements of \(\mathcal P_2\).

*Replacement wording:*

> The integer angular spline terms are \(C^{6,1}_{\rm loc}\) on the full plane and analytic near the origin within the first knot interval. The fractional term makes \(H\) and \(a\) sharply \(C^{4,\beta}_{\rm loc}\), while the factor \(x^2y\) makes \(\rho_h\) sharply \(C^{6,\beta}_{\rm loc}\), where \(\beta=2k/(2-k)\approx0.1970302571\) for this candidate. The normalization and parity hold exactly, and the trial meets the regularity requirements of \(\mathcal P_2\).

**S2 — CORRECT WITH QUALIFICATION. The expansion is uniform in angle when its bracket is defined without dividing on the axes.**

On the full plane, define
\[
F(\theta)=|\cos\theta|^{p_3-2}\sin^2\theta,
\]
and
\[
B_0(\theta)=\sum_m b_m(1)\cos(2m\theta),\qquad
B_1(\theta)=\sum_m b_m'(1)\cos(2m\theta).
\]
The absolute value is unnecessary on the stated right-half-plane angular interval, but necessary in a full-plane formula.

Put \(\delta=1-q\). On the last knot interval,
\[
b_m(q)=b_m(1)-\delta b_m'(1)+O(\delta^2),
\]
\[
T(2q-1)=T(1)-2\delta T'(1)+O(\delta^2),
\]
and
\[
\delta=L^{1-k}r^{k-1}(1+O(r^{-2})).
\]
The factors involving \(\chi\), the base radial power, and \(s^{p_3/2}\) each contribute \(O(r^{-2})\) corrections. Hence
\[
\rho_h=r^k\Theta_0(\theta)
\left[1+r^{k-1}\Theta_1(\theta)+E(r,\theta)\right],
\]
where
\[
\boxed{\Theta_0
=L^{3-k}\cos^2\theta\sin\theta\,
e^{B_0(\theta)+T(1)F(\theta)}}
\]
and
\[
\boxed{\Theta_1
=-L^{1-k}\left[B_1(\theta)+2T'(1)F(\theta)\right].}
\]
Here \(b_m'\) differentiates with respect to \(q\), while \(T'\) differentiates its own argument. This explains the factor \(2\).

Uniformly in \(\theta\),
\[
E=O(r^{2k-2}+r^{-2})=O(r^{2k-2}),
\]
because \(k>0\); numerically \(2k-2\approx-1.6413>-2\).

The angular fractional power causes no difficulty for this **uniform \(C^0\) estimate**: it is bounded and continuous. Unlimited angular differentiability is not being claimed.

At an axis, both \(\rho_h\) and \(\Theta_0\) vanish. Their quotient is undefined there, but the bracket can be constructed directly from the exponential factors and extended continuously across the axes. This gives the asserted uniform expansion without dividing by zero.

*Replacement wording:*

> The displayed expansion holds with \(\Theta_1=-L^{1-k}[\sum_m b_m'(1)\cos(2m\theta)+2T'(1)|\cos\theta|^{p_3-2}\sin^2\theta]\). Its bracket has a continuous extension across the axes and a remainder uniformly \(O(r^{2k-2})\) in angle. The leading term is homogeneous of degree \(k=1/c_l\).

**S3 — CORRECT WITH QUALIFICATION. There is a full continuous extension, not merely a directional limit.**

Sufficient local hypotheses are
\[
\rho\in C^2,\quad W\in C^1,\quad
\rho(x,0)=W_2(x,0)=0,\quad W(P)=0,\quad \rho_y(P)>0.
\]
The stated symmetries provide the two vanishing conditions.

Factor
\[
\rho=yg,\qquad W_2=yh.
\]
One may define
\[
g(x,y)=\int_0^1\rho_y(x,\tau y)\,d\tau,
\]
and similarly define \(h\) using \(\partial_yW_2\). Then \(g\in C^1\), \(h\) is continuous, and \(g>0\) near \(P\). Off the axis,
\[
\boxed{\frac{R}{\rho}=h-1+W\cdot\nabla\log g.}
\]
The right side is continuous on a whole neighborhood of \(P\), including the axis, and at \(P\) equals \(h(P)-1\).

Thus “undefined on the x-axis” describes the original quotient only; its singularity is removable locally. The limit holds along every off-axis approach to \(P\).

At fixed density, imposing \(h(P)=1\), with \(P\) located using the corresponding trial field, imposes exactly the vanishing of this limiting normalized residual. It can avoid using the **origin identity**, but it is not an independent test of the transport equation near the source.

That conclusion requires normalized residual control approaching \(P\). Small unnormalized \(R\), or small residuals at finitely many points away from \(P\), do not establish it.

*Replacement wording:*

> Near \(P\), \(R/\rho\) has the continuous extension \(h-1+W\cdot\nabla\log(\rho/y)\), whose value at \(P\) is \(h(P)-1\). Consequently, imposing \(h(P)=1\) enforces the source limit of the normalized transport equation.

**S4 — CORRECT WITH QUALIFICATION. The identity is exact for frozen trial velocity; the asymptotic and label-spread statements need restrictions.**

Prescribe the trial’s own density on the cutoff section and transport it using the **fixed trial field \(W\)**:
\[
\boxed{\rho_{\mathrm{tr},\epsilon}(X_0)
=e^{-t_\epsilon}\rho(\Phi_{t_\epsilon}X_0).}
\]
This transports a scalar with \(W\cdot\nabla\rho_{\mathrm{tr}}=\rho_{\mathrm{tr}}\). It does not recompute velocity from the transported density.

Along a characteristic on which \(\rho\ne0\),
\[
\frac{d}{dt}\log|\rho(\Phi_tX_0)|=1+\frac R\rho(\Phi_tX_0).
\]
Therefore
\[
\boxed{J_\epsilon
=\log|\rho(X_0)|-\log|\rho_{\mathrm{tr},\epsilon}(X_0)|.}
\]
In the positive-density quadrant these are ordinary logarithms. Moreover,
\[
e^{J_\epsilon}-1
=\frac{\rho(X_0)-\rho_{\mathrm{tr},\epsilon}(X_0)}
{\rho_{\mathrm{tr},\epsilon}(X_0)}.
\]
The denominator matters: relative to the trial density, the difference is \(1-e^{-J_\epsilon}\).

For the asymptotics, assume the backward orbit converges to \(P\), \(a_f>h_0>0\), and enough Hölder regularity that
\[
f(X):=(R/\rho)_{\mathrm{extended}}(X)
=h_0-1+O(|X-P|^\alpha).
\]
For example, \(W\in C^{1,\alpha}\), \(\rho\in C^{2,\alpha}\) suffice locally. Mere continuity would not generally justify an \(O(1)\) remainder after integration.

Because \(y'=yh(X)\), every fixed off-axis orbit satisfies
\[
y(t)=Y(X_0)e^{h_0t}(1+o(1)),\qquad Y(X_0)\ne0.
\]
The horizontal displacement is \(o(e^{h_0t})\), by variation of constants and \(a_f>h_0\). Thus the backward approach is along the **slow vertical eigendirection**, despite the much larger horizontal eigenvalue.

Consequently,
\[
-t_\epsilon
=\frac{\log(1/\epsilon)+\log|Y(X_0)|}{h_0}+o(1),
\]
and
\[
\boxed{J_\epsilon(X_0)
=\frac{h_0-1}{h_0}\log(1/\epsilon)+C(X_0)+o(1).}
\]
The integral of \(f-(h_0-1)\) converges because the orbit approaches exponentially and the error is Hölder.

In this symmetric setting, fast backward approaches lie on the invariant x-axis. Off-axis labels cannot have \(Y=0\). On the axis, \(\rho=0\), so neither the original \(J_\epsilon\) nor the density-logarithm comparison is defined. If one instead integrates the continuous extension \(f\), an axial orbit has coefficient
\[
\frac{h_0-1}{a_f},
\]
not \((h_0-1)/h_0\).

The \(O(1)\) is generally **not uniform as off-axis labels approach the x-axis**. Uniformity is available on suitably controlled compact families separated from it.

For any fixed finite set of off-axis labels, differences of \(J_\epsilon\) cancel the common divergent term. A spread over an unrestricted family approaching the axis need not remain bounded. Nor does a spread of \(e^{J_\epsilon}-1\) cancel the common multiplicative error. Even a bounded logarithmic spread can conceal a large common transport defect.

*Replacement wording:*

> For fixed off-axis labels whose backward characteristics converge to \(P\), \(J_\epsilon\) is the logarithmic ratio to transport with frozen trial velocity and trial cutoff data. Under Hölder regularity, \(J_\epsilon=(h(P)-1)\log(1/\epsilon)/h(P)+C(X_0)+o(1)\). Differences over a fixed finite set of such labels remove the common logarithmic divergence, but do not measure the common transport error; uniformity near the invariant x-axis is not asserted.

**S5 — WRONG literally. The correct exclusion uses polynomial degree or a spherical supremum.**

“Every polynomial density” is too broad, and even \(x^2y\) vanishes along entire rays.

For a polynomial density in the specified normalized class, its total degree \(d\) satisfies \(d\ge3\). Its nonzero leading homogeneous part gives
\[
\boxed{\sup_{|X|=r}|\rho(X)|\asymp r^d.}
\]
Thus it is not \(O(r^k)\) for \(k<3\), and cannot have the far field required by the stated R2 with \(c_l>1\). This is the correct growth exclusion.

There is also an independent algebraic obstruction if these are interpreted as **polynomial Poisson states**. Suppose \(\psi\) is polynomial of degree at most \(d+1\), satisfying \(-\Delta\psi=\rho_x\). Let
\[
P=\rho_d,\qquad Q=\psi_{d+1}.
\]
Here \(Q\ne0\), because \(P_x\ne0\). The degree-\((2d-1)\) part of transport must vanish:
\[
Q_xP_y-Q_yP_x=0.
\]
Euler’s identities then give
\[
dP Q_x=(d+1)Q P_x.
\]
Let \(m\) be the multiplicity of \(x\) in \(P\), and \(n\) its multiplicity in \(Q\). Since \(x^2y\) divides \(P\),
\[
2\le m\le d-1.
\]
Comparison of the lowest powers of \(x\) gives
\[
dn=(d+1)m.
\]
Since \(d\) and \(d+1\) are coprime, this forces \(d\mid m\), a contradiction. Thus no such polynomial pair solves transport, for any \(c_l\).

This argument is independent of R2, but its polynomial-\(\psi\) hypothesis must be stated. The full-plane inverse used for a sublinear density need not even be defined on polynomial growth; one should not silently apply that inverse outside its domain.

*Replacement wording:*

> Every polynomial density in the normalized class has total degree at least three and spherical supremum comparable to \(r^d\). It therefore cannot satisfy the sublinear far field required by R2. The trial instead has the prescribed homogeneous leading degree \(k=1/c_l\).

**S6 — WRONG as an unconditional inference from the measured steps. Several constituent claims have valid conditional versions.**

First, the exponent needs its indicial hypothesis. At an exact source, invariance of a regular graph gives
\[
\gamma'(0)=0,\quad V'(0)=1,\quad D(0)=1,\quad
R_\Gamma'(0)=\rho_y(P),
\]
where I write \(R_\Gamma(s)=\rho(\gamma(s),s)\) to distinguish it from the transport residual.

Using the stipulated amplitude equation, if an active amplitude has a nonzero linear onset
\[
b(s)=\beta_0s+o(s),\qquad b'(s)=\beta_0+o(1),
\]
then its order-\(s\) balance gives
\[
\lambda(2c_l-1)=\rho_y(P).
\]
Thus the quoted exponent is correct under that expansion hypothesis. Oddness alone does not establish a nonzero linear coefficient. More generally, an onset \(b\sim Cs^\nu\) would give
\[
\lambda(2c_l-1)=1+\rho_y(P)-\nu.
\]
This does not establish existence of another layer; it identifies the hypothesis needed for the claimed exponent.

At points with nonzero amplitude, \(2<\lambda<3\) gives transverse \(C^{2,\lambda-2}\) regularity and failure of \(C^3\). But its third derivative behaves as \(|n|^{\lambda-3}\): **there is no finite third-derivative jump**.

On a connected interval with \(V\ne0\) and continuous ODE coefficients,
\[
b_\pm(s)=b_\pm(s_0)M(s),\qquad
M(s)=\exp\left[
-\int_{s_0}^s
\frac{\lambda\kappa-1-R_\Gamma'/D}{V}\,d\sigma
\right]>0.
\]
Therefore:

- Each amplitude preserves sign, or vanishes identically.
- Every **fixed real linear combination** of \(b_+\) and \(b_-\) also preserves sign, or vanishes identically.
- This applies on a branch separated from \(s=0\), not across the source, where odd density amplitudes change sign.

For example, symmetric third-derivative sampling gives
\[
\partial_x^3\rho_{\rm sing}(\gamma+w,s)
-\partial_x^3\rho_{\rm sing}(\gamma-w,s)
=
\lambda(\lambda-1)(\lambda-2)(b_++b_-)w^{\lambda-3}.
\]
A fixed reflected polynomial-extrapolation design replaces the prefactor by an estimator-dependent constant, but retains the sum and scaling. Fixed unequal designs give a fixed weighted sum. Changing windows or fitting designs can change the weights.

In particular, \(b_+=-b_-\) cancels from a symmetric leading step although a layer is present.

Passing to \(H\) does not automatically destroy sign preservation. Where \(s>0\) and \(R_\Gamma(s)>0\), its leading conormal coefficients are
\[
\boxed{d_\pm(s)=\frac{b_\pm(s)}{R_\Gamma(s)}.}
\]
Indeed, expand \(\log(\rho_{\rm reg}+\rho_{\rm sing})\); subtracting \(2\log x+\log s\) changes only the smooth background. Both \(d_\pm\) share a positive multiplier.

Near the axis, if \(b_\pm(s)\sim\beta_\pm s\), then
\[
d_\pm(s)\longrightarrow \frac{\beta_\pm}{\rho_y(P)}.
\]
The apparent \(1/y\) from forming \(a=\rho/(x^2y)\) is canceled by the amplitude’s odd, linear onset. At \(y=0\), one must use this extension of \(H=\log a\), not \(\log\rho\).

Regarding zeros of \(V\), the information \(W_2=yh\), \(h(P)=1\), alone proves positivity only locally. For an **exact solution on a regular invariant graph extending to \(s=1\)**, however, there is a stronger argument:
\[
V(s)R_\Gamma'(s)=R_\Gamma(s).
\]
Initially \(V>0\) and \(R_\Gamma>0\), because \(\rho_y(P)>0\). Until a proposed first zero of \(V\), this equation makes \(R_\Gamma\) strictly increasing. At that zero, invariance gives \(W=0\), so transport requires \(R_\Gamma=0\), a contradiction. Hence
\[
V(s)>0\qquad(0<s\le1)
\]
provided that regular exact graph exists throughout the interval.

This argument neither proves graph extension to \(1\) nor applies to a trial with nonzero residual.

Finally, a fixed-window estimator includes smooth-background errors and subleading layer terms. A controlled conormal expansion with a consistent shrinking-window design would give
\[
w^{3-\lambda}\operatorname{step}_w(H;s)
\longrightarrow
\text{a fixed linear combination of }d_\pm(s).
\]
That limiting coefficient preserves sign or vanishes. The reported unscaled, finite-window measurements do not establish this limit or dominance of its leading term.

Every individual fit is \(C^6\) near \(\Gamma\), so its literal third-derivative jump is already zero. The sign reversal therefore does **not** exclude a layer in an exact solution or in a singular limit of fits. It contradicts a dominant-single-layer interpretation only if the estimator design, nonzero leading combination, and smaller remainders have independently been controlled.

*Replacement wording:*

> Under the stated conormal expansion and nonzero linear amplitude onset at the axis, a nonzero layer has exponent \(\lambda=\rho_y(P)/(2c_l-1)\) and transverse regularity \(C^{2,\lambda-2}\), but no finite third-derivative jump. On a regular positive branch, its two amplitudes share a positive transport multiplier, so a fixed estimator’s nonzero leading layer coefficient preserves sign. The observed finite-window sign reversal does not establish such a leading coefficient and does not exclude a layer in an exact solution; that question remains open.

I reconstructed the coefficient ordering and spline representation directly from the archive. The checks confirmed simple interior knots, endpoint multiplicity eight, and \(b_m(0)=0\). They gave
\[
T(1)\approx8.6885021381,\qquad T'(1)\approx45.2975625570.
\]
At the **stored, not independently reverified** source coordinate, direct density evaluation gave
\[
\rho_y(P)\approx29.7494476791,\qquad
\frac{\rho_y(P)}{2c_l-1}\approx2.93077066225.
\]
Far-field checks on 513 angles at \(r=10^4,10^5,10^6\) were consistent with the derived remainder order. These were floating-point spot checks; I did not recompute the velocity or \(\Gamma\).

The standalone argument and reproducible checks are saved in [PROOF.md](PROOF.md) and [spot_checks.json](spot_checks.json).

The configured collaboration target was `us.anthropic.claude-opus-5-5`, but Bedrock connectivity was unavailable. No Opus review was obtained, and no substitute model was used.