# Implemented mathematical problem and approximation

Paths below are relative to `research/`. These formulas describe the current source and saved mode manifest, not a proposed enlarged space.

## Whole-plane equations and assumptions

The nondimensional target is

\[
(c_lX+U)\cdot\nabla\rho-\rho=0,\quad U=(-\psi_y,\psi_x),\quad-\Delta\psi=\rho_x,
\quad X=(x,y)\in\mathbb R^2.
\]

The represented potential is smooth and even in each coordinate. Set
\(\psi=\chi_{xy}\), \(\rho=-\partial_y\Delta\chi=yf\). Then density is even-x/odd-y; f is even in each coordinate; psi is odd in each coordinate. Commuting derivatives enforces the local Poisson equation. The canonical inverse additionally excludes arbitrary global harmonic additions and uses regularity/growth at infinity. For source sine modes n=2,4,...,

\[
\psi_n(r)=\frac1{2n}\left[r^{-n}\int_0^r t^{n+1}S_n(t)\,dt
+r^n\int_r^\infty t^{1-n}S_n(t)\,dt\right].
\]

This is independently checked by `base/stage12_assess.py:154–272`; it is not replaced by a finite outer-boundary condition. For current \(c_l>1\), represented leading growth is \(\chi=O(r^{3+\gamma})\), \(\psi=O(r^{1+\gamma})\), \(\rho,U=O(r^\gamma)\), \(f=O(r^{\gamma-1})\), \(\gamma=1/c_l<1\). Smoothness and finite computed integrals do not prove the existence of an exact solution.

## Exact generators and coefficient order

Define \(R=1+x^2+y^2\), \(t=(x^2+y^2)/R\), \(H_m=\operatorname{Re}(x+iy)^{2m}\), \(A=(3+\gamma)/2\), \(\delta=(1-\gamma)/2\).

The 24 core generators are

\[
\chi_{mk}=H_mR^{A-m-\sigma_k},\quad m=0,1,2,3,
\quad\sigma_k=(0,1,2,\delta,2\delta,3\delta),\quad k=0,\ldots,5.
\]

Order first `(m,k)` with m=0..3, k=0..4 (index 5m+k), then `(m,5)` with m=0..3 (indices 20+m). Source: `absolute_fields.py:26–39`.

The additional 162 Global generators are

\[
\chi^G_{mn}=H_mR^{A-m}t^{\max(5-m,0)}\sqrt{2n+1}\,P_n(2t-1).
\]

Use all m=0..8, n=0..17 in lexicographic order, remove `(3,0)`, then append `(9,0)` last. The exact saved list is `inputs/global.json`; `base/campaign_tools.py:14–22` constructs it. \(P_n=P_n^{(0,0)}\) is ordinary Legendre, not a nonzero-parameter Jacobi family; \(\int_0^1[\sqrt{2n+1}P_n(2t-1)]^2dt=1\). This normalizes the radial polynomial in dt, not its physical fields or angular factor (`base/spectral_basis.py:58–84`). Production evaluates the algebraically equivalent normalizer using gamma functions.

The omitted function is exactly dependent:
\(\chi^G_{3,0}=\chi_{3,0}-2\chi_{3,1}+\chi_{3,2}\).
No additional exact dependence is established at the present generic \(c_l\). Numerical near-dependence is retained in the solver. The homogeneous harmonic factor ensures Cartesian regularity; the added t power makes each added chi vanish to degree at least 10, so its f and \(\psi_x/y\) start at degree at least 6. Thus the additions leave the center and five lower Taylor equations unchanged. Their asymptotic envelopes do not enforce nonlinear far-field compatibility.

## Center and five Taylor equations

Raw parameters are \(p=(c_l,c_1,\ldots,c_{23})\in\mathbb R^{24}\), followed by the 162 extra coefficients. If \(s_j(c_l)\) denotes each core generator's center strain,

\[
c_0=\frac{1-c_l-\sum_{j=1}^{23}s_jc_j}{s_0},\quad
\partial_{c_l}c_0=\frac{-1-\sum_{j=0}^{23}s_j'c_j}{s_0},\quad
\partial_{c_j}c_0=-s_j/s_0.
\]

`absolute_fields.py:42–100` reconstructs this center relation at Decimal precision 90 from the exact represented binary inputs. Displayed saved c0 is not an independent optimization coordinate. Naively using its rounded value can leave a nonzero origin residual constant and invalidate the dr/r integral.

Using ordinary Taylor coefficients, with no factorial factors,

\[
f=a+bx^2+cy^2+dx^4+ex^2y^2+gy^4+\cdots,
\quad\psi=xy(h+ux^2+vy^2+wx^4+zx^2y^2+ky^4+\cdots),
\]

we have \(a=a_0=\rho_y(0)\), \(h=1-c_l\), and constrain

\[
\begin{aligned}
E_x&=2(2c_l-1)b+3au,&E_y&=2c+av,\\
D_1&=4(2c_l-1)d+bu+5aw,\\
D_2&=4c_le-5bv+9cu+3az,&D_3&=4g+3cv+ak.
\end{aligned}
\]

Source: `absolute_chart.py:29–73`; `base/engine/taylor_jet.py:9–57`. The local chart solves all five together, leaving 19 core tangent variables and 162 additive Global variables. Its coefficient-only normal correction has zero \(c_l\) row. Both \(c_l\) and physical \(a_0\) remain free. Inherited core bounds are \(1.02\le c_l\le10\), \(-100\le c_j\le100\) for j=1..23, with nonzero a0. Numerical feasibility uses defect tolerance 1e-10; “exact constraints” describes the mathematical equations, not exact floating-point zeros.

## Absolute residual, objective and quadrature

Write \(w_x=c_lx-\psi_y\), \(w_y=c_ly+\psi_x\), \(q=c_l-1+\psi_x/y\). The smooth quotient is evaluated analytically on axes, and

\[
R_f=w_xf_x+w_yf_y+qf,\qquad R_\rho=yR_f.
\]

The center-safe implementation forms q from a basis difference rather than subtracting large summed center values. Complete parameter derivatives include \(\gamma,\delta\), radial powers, c0, velocity, gradients, q and the explicit \(x f_x+y f_y\) contribution to \(\partial_{c_l}R_f\). Source: `absolute_fields.py:140–205`; `stage13_model.py:94–143`.

The primary functional is

\[
J_{\rm abs}=\frac1{\pi a_{\rm ref}^2}\int_0^{\pi/2}\int_0^\infty R_f^2\,\frac{dr}{r}\,d\theta,
\quad a_{\rm ref}=23.95065822465609.
\]

For fixed positive quadrature weights \(w_i\) in \(s=\log r\) and theta, the residual vector is
\(r_i=\sqrt{2w_i/(\pi a_{\rm ref}^2)}R_f(X_i)\), so \(J_{\rm mesh}=\frac12r^Tr\). The reference amplitude is a fixed input constant; it is never replaced by a0. The actual production mesh (`whole_axis_mesh.py:22–68`) has origin r=.02u, middle log-radius [log .02,16], and infinity r=exp(16)/u, with the correct du/u weights on transformed blocks. Training/refined rules have 90,624/241,664 nodes. Nodes remain fixed during an epoch. Finite quadrature approximates the continuous functional; it is not exactly dilation invariant or a rigorous integral enclosure.

Independent evaluation uses origin polynomial orders20/24, analytic integration, an 85-digit full-potential overlap test, adaptive radial/angular refinement, interval expansion and an all-angle tail envelope (`stage13_integration_v2.py:81–165`). Numerical error diagnostics combine those checks without claiming interval arithmetic.

Under exact spatial dilation L>0,
\(f_L(X)=f(X/L)\), \(\rho_L=L\rho(X/L)\), \(\psi_L=L^2\psi(X/L)\), \(U_L=LU(X/L)\), hence \(R_{f,L}(X)=R_f(X/L)\). Substitution r/L proves continuous J invariance whenever the integral exists. Both cl and a0 stay unchanged. Exact dilation is evaluated at shifted coordinates, never approximated by refitting this finite basis.

## Secondary diagnostics and unresolved asymptotics

Report sampled \(E_f=|R_f|/a_{\rm ref}\) and \(E_\rho=|R_\rho|/(ra_{\rm ref})=|\sin\theta R_f|/a_{\rm ref}\). The secondary normalized quotient and smooth y-factored density diagnostics are

\[
\frac{|R_f|}{|w_xf_x|+|w_yf_y|+|qf|},\qquad
\frac{|R_f|}{|w_xf_x|+|(q+1)(f+yf_y)|+|f|}.
\]

Zero denominators are undefined, not floored. The raw density ratio itself is0/0 on y=0; the second expression defines its smooth factored extension where meaningful. Identical predetermined independent grids are used for comparison. Sampled maxima are not continuous suprema.

For formal differentiated asymptotic expansions \(\rho\sim\sum_jr^{\alpha_j}F_j\), \(\psi\sim\sum_jr^{\alpha_j+1}\Phi_j\), \(\alpha_j=\gamma-j(1-\gamma)\), the necessary first transport relation is

\[
(c_l-1)F_1=-\gamma\Phi_0'F_0+(\gamma+1)\Phi_0F_0',
\qquad-\Phi_j''-(\alpha_j+1)^2\Phi_j=\alpha_j\cos\theta F_j-\sin\theta F_j'.
\]

Symmetry imposes F(0)=0, F'(pi/2)=0 and Phi(0)=Phi(pi/2)=0. The current independent coefficient audit finds this first nonlinear compatibility is not satisfied: original Rrho has a nonzero \(r^{2\gamma-1}=r^{0.105587864228\ldots}\) coefficient. Under the stated expansion/remainder assumptions, matching the entire first angular relation would leave a next power \(3\gamma-2<0\), but a projected angular match alone does not cancel unresolved modes. Neither the expansion itself nor existence/basis convergence is proved. These are future research issues, not constraints already installed in the solver.
