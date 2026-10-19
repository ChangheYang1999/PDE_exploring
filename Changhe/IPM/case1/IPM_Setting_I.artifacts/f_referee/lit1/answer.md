**I did not verify an existence or nonexistence theorem for your particular smooth, whole-plane, even-in-\(x\), odd-in-\(y\) profiles with \(R=x^{2}y\,a\), \(a(0)=1\).** The wall computations, infinite-energy examples, forced blowup constructions, and stability theorems concern substantially different classes.

Below, **[Text]** means I inspected the relevant statement or equations in a primary paper; **[Abstract]** means only the abstract supports the description; **[Calculation]** means an argument supplied here. Inspecting a theorem statement is not an independent verification of its entire proof. The literature cutoff is **17 October 2026**.

1. **Normalization and the numerical wall profiles.**

   **Wang et al., *Discovery of Unstable Singularities*, arXiv:2509.14185 (2025). [Text]** The title is “Discovery,” not “Discovering.” This is numerical work: it reports a stable IPM candidate and three unstable candidates, together with residual and spectral computations. It does **not** contain a computer-assisted existence theorem for those IPM profiles. The paper explicitly identifies boundary-free self-similar IPM as a remaining challenge. ([arxiv.org](https://arxiv.org/pdf/2509.14185), [arxiv.org](https://arxiv.org/html/2509.14185v1))

   **Wang–Léger–Lai–Buckmaster, *Resolving Sharp Gradients of Unstable Singularities to Machine Precision via Neural Networks*, arXiv:2511.22819 (2025). [Text]** This follow-up improves numerical accuracy and adds a fourth unstable IPM candidate. Its domain is
   \[
   \mathbb H=\{x_2>0\},\qquad u_2(x_1,0)=0,
   \]
   and its ansatz is explicitly
   \[
   \rho(t,x)=(1-t)^\lambda H(Y),\quad
   u(t,x)=(1-t)^\lambda V(Y),\quad
   Y=\frac{x}{(1-t)^{1+\lambda}}.
   \]
   Consequently,
   \[
   ((1+\lambda)Y+V)\cdot\nabla H=\lambda H.
   \]
   The reported exponents are approximately
   \[
   1.0285722760323,\quad 0.472129736156,\quad
   0.3149617817,\quad0.24156641,\quad0.1987237.
   \]
   These are numerical estimates, not certified intervals. ([arxiv.org](https://www.arxiv.org/pdf/2511.22819v1))

   The intended reflection class has density even in the horizontal coordinate, horizontal velocity odd in that coordinate, and vertical velocity even. The density has a nonconstant, nonzero wall trace; there is no odd-in-\(x_2\) smoothness condition. The represented candidates are smooth at finite points of the closed half-plane. Smoothness of an exact nearby solution has not thereby been proved. I could verify the local div–curl formulation, wall condition, and use of asymptotic envelopes, but **not a complete explicit renormalized integral prescription** from the supplementary material. ([arxiv.org](https://arxiv.org/html/2509.14185v1), [arxiv.org](https://www.arxiv.org/pdf/2511.22819v1))

   **Conversion to your normalization. [Calculation]** Put
   \[
   R=\frac H\lambda,\qquad U=\frac V\lambda.
   \]
   Then
   \[
   c_l=1+\frac1\lambda.
   \]
   Thus their \(\lambda\) is neither your \(c_l\) nor the physical spatial exponent, which is \(1+\lambda\). In particular, all the listed candidates correspond to \(c_l>1\).

   If the leading far-field balance is dilation-dominated and matches a time-independent outer density, the expected growth is
   \[
   H(r,\theta)\sim r^{\lambda/(1+\lambda)}h(\theta)
   =r^{1/c_l}h(\theta).
   \]
   This is **sublinear growth of density**, while its gradient decays like
   \(r^{-1/(1+\lambda)}\). This calculation is conditional on that far-field regime; it is not a proved asymptotic theorem about the numerical candidates. Also,
   \[
   \nabla_x\rho=(1-t)^{-1}\nabla_YH:
   \]
   the first-gradient similarity rate is \(1/(1-t)\), independently of \(\lambda\).

   There is a sign error worth guarding against: equation (8) in the November paper prints
   \(\partial_1V_2-\partial_2V_1=+\partial_1H\), whereas its displayed Darcy law gives **minus** \(\partial_1H\). Your stream-function convention is consistent with Darcy’s law. ([arxiv.org](https://www.arxiv.org/pdf/2511.22819v1))

2. **Other blowup constructions: which ones actually concern IPM.**

   **(a) Castro–Córdoba–Gancedo–Orive and Collot–Prange–Tan: infinite energy. [Text]**

   *Incompressible flow in porous media with fractional diffusion*, **arXiv:0806.1180 (2008), Nonlinearity 22 (2009)**, includes infinite-energy singular solutions. Its dissipative global results must not be transferred to inviscid IPM. ([arxiv.org](https://arxiv.org/abs/0806.1180))

   Collot–Prange–Tan, *Stable self-similar singularity formation for infinite energy solutions of the incompressible porous medium equations*, **arXiv:2507.17381 (2025)**, study the associated reduction on
   \[
   [-\pi,\pi]\times\mathbb R
   \quad\text{with walls at }x=\pm\pi,
   \qquad\text{or }\mathbb T\times\mathbb R.
   \]
   These are **vertical walls**, unlike the numerical horizontal-wall problem. Their stream function is linear in the unbounded coordinate. The reduced unknown \(b\), of zero horizontal mean, has the explicit solution
   \[
   b(t,x)=\mu\sec(\mu t)\cos x.
   \]
   Theorem 1.1 states stability for mean-zero \(C^3\) data satisfying
   \[
   \|b_0-\mu\cos x\|_{C^3}\le\delta\mu,\qquad \mu>0,
   \]
   with
   \[
   b(t,x)=\frac{\cos x}{T-t}+\widetilde b(t,x),
   \qquad
   \|\widetilde b(t)\|_{C^1}\lesssim(T-t)^{-3/4}.
   \]
   Theorem 1.2 gives instability of this asymptotic form under arbitrarily small \(C^{2-\varepsilon}\) perturbations, \(0<\varepsilon\le2\). The references to equation (1.7) in these two statements appear erroneous: the blowup equation is (1.2); (1.7) is the transformed equation. ([arxiv.org](https://arxiv.org/pdf/2507.17381))

   To make the distinction concrete, **direct substitution in your sign convention** verifies
   \[
   \begin{aligned}
   A(t)&=\mu\sec(\mu t),& B(t)&=\mu\tan(\mu t),\\
   \rho(t,x,y)&=y(A(t)\cos x+B(t)),\\
   u(t,x,y)&=(A(t)\sin x,-A(t)y\cos x),\\
   p(t,x,y)&=A(t)\cos x-\tfrac12B(t)y^2.
   \end{aligned}
   \]
   The transport equation reduces to \(A'=AB,\ B'=A^2\). These fields are smooth, density is even in \(x\) and odd in \(y\), and the periodic solution lifts to \(\mathbb R^2\). But density and velocity grow linearly in \(y\), energy is infinite, and the leading blowup has no shrinking horizontal scale. Velocity is specified explicitly through Darcy’s law, rather than by applying an unqualified \(L^p\) Riesz-transform formula to growing data.

   **(b) Córdoba–Martínez-Zoroa: smooth forced whole-plane blowup. [Text]**

   *Finite time singularities of smooth solutions for the 2D incompressible porous media (IPM) equation with a smooth source*, **arXiv:2410.22920 (2024; inspected v3, February 2025)**.

   The stated theorem gives \(\rho_0\in C_c^\infty(\mathbb R^2)\) and a spatially compactly supported source
   \[
   F\in L^\infty_tC^\infty_x
   \]
   such that the classical solution is spatially \(C_c^\infty\) for \(0\le t<1\), but
   \[
   \|\rho(t)\|_{C^1}\longrightarrow\infty.
   \]
   They also state \(\|\nabla u(t)\|_\infty\to\infty\) and terminal regularity
   \[
   \rho(1)\in C^\infty(\mathbb R^2\setminus\{0\})
   \cap C^\alpha,\qquad 0\le\alpha<1.
   \]
   **Uniform space-time \(C^\infty\) forcing is not the theorem in that version**: improving time regularity is discussed separately. The construction uses successively separated scales, not a stationary self-similar profile. Thus there are no selected similarity exponents or growing-profile Biot–Savart prescriptions to extract from this theorem. ([arxiv.org](https://arxiv.org/pdf/2410.22920))

   **(c) Bianchini–Córdoba–Martínez-Zoroa: critical ill-posedness, not smooth-data finite-time blowup. [Text]**

   *Non Existence and Strong Ill-Posedness in \(H^2\) for the Stable IPM Equation*, **arXiv:2410.01297 (2024)**.

   Theorem 1.2: for every \(\varepsilon>0\), there are \(T_\varepsilon>0\) and an initial perturbation \(\eta_0\) with \(\|\eta_0\|_{H^2(\mathbb R^2)}\le\varepsilon\), such that a classical solution with
   \(\rho_0=-y+\eta_0\) satisfies
   \[
   \rho(t)+y\notin H^2\quad(0<t\le T_\varepsilon),
   \]
   while remaining in every \(H^{2-\delta}\), \(\delta>0\), and in \(C^1\). The paper states uniqueness in the corresponding \(H^1\) perturbation class. The construction uses **your even-\(x\), odd-\(y\) symmetry**. It does not construct your self-similar profiles, and its “nonexistence” is nonexistence of an \(H^2\)-regular evolution for particular data, not a profile Liouville theorem. ([arxiv.org](https://arxiv.org/pdf/2410.01297))

   **(d) Dembski: unforced blowup without boundary density, but on a wedge. [Text]**

   *Singularity Formation in the Incompressible Porous Medium Equation without Boundary Mass*, **arXiv:2511.01827 (2025)**.

   Gravity points in the negative first-coordinate direction. The domain is a symmetric wedge
   \[
   \Omega_L=\{r>0,\ |\theta|<L\},\qquad L<\pi/2,
   \]
   with \(L\) obtainable arbitrarily close to \(\pi/2\). Density is even in \(\theta\). The paper uses scale-invariant Hölder spaces, with
   \[
   \|f\|_{\mathring C^{k,\alpha}}
   =\|f\|_\infty+
   \sum_{j=0}^{k}
   [\,|X|^{j+\alpha}\nabla^jf\,]_{C^\alpha}.
   \]
   Theorem 1.2 asserts, for every integer \(k\ge0\) and \(0<\alpha<1\), compactly supported initial density with gradients in these classes, vanishing near the angular boundary, whose solution satisfies
   \[
   \limsup_{t\uparrow1}\int_0^t\|\nabla\rho(s)\|_\infty\,ds=\infty.
   \]
   The underlying homogeneous construction is
   \[
   \rho=\frac r{1-t}P_*(\theta),\qquad
   \psi=\frac{r^2}{1-t}G_*(\theta),
   \]
   with
   \[
   P_*+2G_*P_*'=G_*'P_*,
   \qquad
   G_*''+4G_*=P_*\sin\theta+P_*'\cos\theta,
   \quad G_*(\pm L)=0.
   \]
   Density grows linearly before truncation and is generally only Lipschitz at the vertex. Angular and spatial truncations yield the localized construction. **The half-plane endpoint is excluded**, and smoothness at the vertex is not asserted. ([arxiv.org](https://arxiv.org/pdf/2511.01827.pdf), [arxiv.org](https://arxiv.org/html/2511.01827v1))

   **(e) Developments in September–October 2026. [Abstract only]**

   These must be mentioned given the present date, but I have **not audited their proofs**:

   - Alpöge–Buckmaster–Coiculescu, **arXiv:2609.16470 (2026)**, *Extending the Córdoba-Martínez-Zoroa IPM Blow-Up to Uniformly Space-Time Smooth Forcing*: on \(\mathbb T^2\), smooth odd data and
     \(F\in C^\infty([0,1]\times\mathbb T^2)\), with density and velocity gradients diverging and density converging in every \(C^\eta,\ \eta<1\). The metadata describes a Lean-formalized proof; I did not check that formalization. ([arxiv.org](https://arxiv.org/abs/2609.16470))
   - Fan Zheng, **arXiv:2610.06544 (2026)**, *Finite-time blowup of the IPM equation from smooth initial data without forcing*: claims unforced smooth-data gradient blowup on \(\mathbb T^2\), via a multiscale construction, with terminal \(C^\eta\) convergence for \(\eta<1\). ([arxiv.org](https://arxiv.org/abs/2610.06544))
   - Mimi Dai, **arXiv:2610.06712 (2026)**, *Finite-time blowup for 2D unforced IPM*: claims smooth odd periodic data for which
     \(\partial_2\rho(t,0)\) and \(\partial_1u_1(t,0)\) tend to \(+\infty\), while density and velocity stay bounded in \(L^2\). ([arxiv.org](https://arxiv.org/abs/2610.06712))

   None of these abstracts establishes an isotropically self-similar profile, specifies your separate reflection symmetries, or selects \(c_l\).

   **(f) What I could verify about computer assistance.**

   Chen–Hou’s relevant pair is **arXiv:2210.07191 (2022)** and **arXiv:2305.05660 (2023)**, *Stable nearly self-similar blowup … I: Analysis; II: Rigorous Numerics*. They concern **2D Boussinesq and axisymmetric 3D Euler with boundary**, not IPM. I did not locate a verified Chen–Hou computer-assisted theorem validating the Wang et al. IPM wall candidates. ([arxiv.org](https://arxiv.org/abs/2210.07191), [arxiv.org](https://arxiv.org/abs/2305.05660))

   Also distinguish Kiselev–Sarsam, **arXiv:2412.16376 (2024), Nonlinearity 38 (2025)**: their finite-time blowup theorem is for a **one-dimensional boundary-layer model**, not the full two-dimensional IPM equation. ([arxiv.org](https://arxiv.org/abs/2412.16376))

3. **Nonexistence and stationary rigidity.**

   **(a) A directly applicable general transport theorem. [Text]**

   Dongho Chae, *Nonexistence of self-similar singularities for the 3D incompressible Euler equations*, **arXiv:math/0601060 (2006; published 2007)**, contains a separate divergence-free transport result.

   Theorem 2.1 considers
   \[
   \beta\Theta+\frac1{\alpha+1}X\cdot\nabla\Theta
       +V\cdot\nabla\Theta=0,\qquad \operatorname{div}V=0,
   \quad\alpha\ne-1.
   \]
   Its conclusion is \(\Theta=0\) if
   \[
   \Theta\in L^{p_1}(\mathbb R^n)\cap L^{p_2}(\mathbb R^n),
   \qquad0<p_1<p_2\le\infty.
   \]
   The underlying Theorem 2.2 treats
   \(\theta(t,x)=\Psi(t)\Theta(\Phi(t)x)\): either \(\Theta=0\), or both \(\Psi\) and \(\det\Phi\) are constant. The proof uses a classical, globally defined, measure-preserving flow. That hypothesis should be made explicit when applying the result to profiles with unbounded velocity. ([arxiv.org](https://arxiv.org/pdf/math/0601060))

   **(b) Precise elementary versions for your equation. [Calculation]**

   Suppose \(R,U\in C^1\), \(\operatorname{div}U=0\), and
   \[
   W=c_lX+U,\qquad W\cdot\nabla R=R.
   \]

   If \(|U(X)|\le C(1+|X|)\), the flow \(\Phi_s\) of \(W\) is complete and
   \[
   R(\Phi_sX)=e^sR(X),\qquad
   \det D\Phi_s(X)=e^{2c_ls}.
   \]
   Therefore, for \(0<p<\infty\) and \(R\in L^p\),
   \[
   \int|R|^p=e^{(p+2c_l)s}\int|R|^p.
   \]
   Hence
   \[
   (p+2c_l)\int|R|^p=0.
   \]
   In particular, **one finite \(L^p\) condition suffices when \(c_l>0\)**. For arbitrary \(c_l\), the exceptional identity is \(c_l=-p/2\); two distinct \(p\)'s exclude it.

   If \(R\) is bounded and the forward flow is complete, then
   \(e^s|R(X)|\le\|R\|_\infty\), so \(R=0\).

   If \(R(X)\to0\) as \(|X|\to\infty\), no velocity-growth assumption is needed: a nonzero \(R\) attains a positive maximum or negative minimum, where \(\nabla R=0\), contradicting \(W\cdot\nabla R=R\).

   **These arguments do not exclude sublinearly growing profiles.** Nor may one integrate by parts against a growing profile and silently discard its far-field flux.

   **(c) Actual stationary IPM is a different equation. [Text and calculation]**

   Elgindi’s Lemma 1.1 concerns \(u\cdot\nabla\rho=0\) on a bounded impermeable domain. Its energy argument gives
   \[
   \int\rho u_2=0,\qquad
   \int|u|^2=-\int\rho u_2=0,
   \]
   and therefore \(u=0,\ \partial_x\rho=0\). On a strip, this means \(\rho=f(y)\). For a completely general domain with disconnected horizontal sections, \(\partial_x\rho=0\) is the precise conclusion without additional geometric qualifications. ([arxiv.org](https://arxiv.org/pdf/1411.6958))

   A nonzero bounded stationary density certainly exists: \(\rho=\tanh y,\ u=0\). Thus “bounded stationary IPM profiles are zero” is false. On the whole plane there are even stationary solutions with nonzero velocity, for example
   \[
   \rho=f(x),\qquad u=(0,-f(x)),\qquad p=0.
   \]
   Conversely, a \(C^1\), compactly supported whole-plane stationary density with the usual decaying Darcy velocity must vanish, by the same energy argument and horizontal independence.

   **(d) Córdoba–Gancedo–Orive (2007): verification limitation.**

   The bibliographic reference is *Analytical behavior of two-dimensional incompressible flow in porous media*, **Journal of Mathematical Physics 48, 065206 (2007)**. I did not obtain readable full theorem text or verify an arXiv number. Kiselev–Yao §2.1 attribute to its Theorem 3.2 local well-posedness in \(H^s(\mathbb R^2)\), \(s>2\), and continuation under
   \[
   \int_0^T\|\nabla\rho(t)\|_{\mathrm{BMO}}\,dt<\infty.
   \]
   **I did not verify a self-similar Liouville theorem in that paper and would not cite it as excluding your profiles.** ([pubs.aip.org](https://pubs.aip.org/aip/jmp/article/48/6/065206/914762/Analytical-behavior-of-two-dimensional), [arxiv.org](https://arxiv.org/pdf/2102.05213))

4. **The stability and small-scale-formation literature does not supply a general profile exclusion.**

   Throughout this item, the stable background in **your** gravity convention is \(-y\). Some papers reverse gravity and consequently write \(+y\).

   **(a) Elgindi, arXiv:1411.6958 (2014; ARMA 225, 2017). [Text]**

   Theorem 1.3: for \(s\ge20\), sufficiently small
   \[
   \eta_0\in H^s(\mathbb R^2)\cap W^{4,1}(\mathbb R^2),
   \qquad \rho_0=-y+\eta_0,
   \]
   yields a global solution with
   \[
   \|\eta(t)\|_{H^3}\lesssim\varepsilon t^{-1/4},\quad
   \|u_1(t)\|_{H^3}\lesssim\varepsilon t^{-3/4},\quad
   \|u_2(t)\|_{H^3}\lesssim\varepsilon t^{-5/4}.
   \]
   Theorem 1.4 treats small periodic perturbations: uniform \(H^{20}\) control and
   \(\|u(t)\|_{H^3}\lesssim\varepsilon t^{-5/2}\).
   Here the **perturbation** is periodic; the total density \(-y+\eta\) is not a periodic scalar on \(\mathbb T^2\). ([arxiv.org](https://arxiv.org/pdf/1411.6958))

   **(b) Castro–Córdoba–Lear, arXiv:1804.08490 (2018; ARMA 232, 2019). [Text]**

   On \(\Omega=\mathbb T\times[-1,1]\), define
   \[
   X^k=\{f\in H^k(\Omega):
          \partial_y^{2j}f|_{\partial\Omega}=0
          \text{ for every }2j<k\}.
   \]
   The stated stability result assumes \(\eta_0\in X^k\), \(k\ge10\), sufficiently small. It gives global existence, uniform smallness in \(H^k\), and
   \[
   \|u(t)\|_{H^3}
   +\|\eta(t)-\langle\eta(t)\rangle_x\|_{H^3}
   \lesssim\varepsilon(1+t)^{-5/4}.
   \]
   The limit can be another nearby stratified density. The higher boundary compatibility conditions are essential hypotheses; merely imposing \(u_2=0\) is not this theorem. ([arxiv.org](https://arxiv.org/pdf/1804.08490.pdf))

   **(c) Jo–Kim, arXiv:2210.11437 (2022; revised/published 2024). [Text; detailed formulas checked in v1]**

   Their Theorem A allows
   \[
   \rho_s(y)=-\int_0^y(N+\sigma(z))\,dz,\qquad
   \sigma\in\mathcal S(\mathbb R),\quad m\in\mathbb N,\ m>3,
   \]
   provided
   \[
   N\ge C_m\!\left(
       \|\eta_0\|_{H^m}
       +\|\langle\xi\rangle^{m+1}\widehat\sigma(\xi)\|_{L^1}
       \right).
   \]
   It gives a unique global \(C_tH^m\cap C_t^1H^{m-1}\) perturbation,
   \[
   \|u(t)\|_{H^m}\lesssim(1+Nt)^{-1/2}\|\eta_0\|_{H^m},
   \quad
   \|\nabla u_2(t)\|_{H^{m-1}}
       \lesssim(1+Nt)^{-1}\|\eta_0\|_{H^m},
   \]
   and \(\|\eta(t)\|_\infty\to0\).
   For \(\sigma=0\), real \(m>3\) is allowed on \(\mathbb R^2,\mathbb T^2\).
   Theorems B–C give convergence to a stratified limit \(\eta_\infty\) on the periodic perturbation domain and confined strip, respectively; the strip requires \(\eta_0\in X^m\), integer \(m>3\). For \(0\le s\le m\),
   \[
   \begin{aligned}
   &(1+Nt)^{(m-s)/2}\|\eta-\eta_\infty\|_{H^s}\\
   &+(1+Nt)^{(m-s+1)/2}\|u\|_{H^s}
   +(1+Nt)^{(m-s+2)/2}\|u_2\|_{H^s}
   \lesssim\|\eta_0\|_{H^m}.
   \end{aligned}
   \]
   These are perturbative stability results. ([arxiv.org](https://arxiv.org/pdf/2210.11437.pdf), [arxiv.org](https://arxiv.org/abs/2210.11437))

   **(d) Bianchini–Crin-Barat–Paicu, arXiv:2210.02118 (2022; ARMA 248, 2024). [Text]**

   Theorem 2.3 assumes
   \[
   0<\tau<1,\qquad s\ge3+\tau,\qquad
   \|\eta_0\|_{\dot H^{1-\tau}\cap\dot H^s}\le\delta_0
   \]
   on \(\mathbb R^2\), around \(-y\). It gives a unique global strong solution and
   \[
   \begin{aligned}
   &\|\eta\|_{L^\infty_t(\dot H^{1-\tau}\cap\dot H^s)}
   +\|R_1\eta\|_{L^2_t(\dot H^{1-\tau}\cap\dot H^s)}\\
   &\quad+\|(\nabla R_1^2\eta,\Lambda R_1^2\eta)\|_{L^1_tL^\infty_x}
   \lesssim\|\eta_0\|_{\dot H^{1-\tau}\cap\dot H^s}.
   \end{aligned}
   \]
   The explicit relation \(s\ge3+\tau\) is more precise than quoting only the abstract’s shorthand \(s>3\). ([timotheecrinbarat.com](https://www.timotheecrinbarat.com/_files/ugd/d28565_a7920e01b29f4dfe98bf2b8933a126df.pdf))

   **(e) Park, arXiv:2403.14187 (2024). [Text]**

   *Stability analysis … via energy structure*, Theorem 1.1: on
   \(\mathbb T\times(0,1)\), around \(\rho_s=1-y\), integer \(k\ge3\), assume
   \[
   \rho_0-\rho_s\in H_0^k,\qquad
   \|\rho_0-\rho_s\|_{H^k}\le\varepsilon_k.
   \]
   Then the solution is global, uniformly small in \(H^k\), and
   \[
   \|\rho(t)-\rho_0^*\|_{L^2}\lesssim\varepsilon t^{-k/2},
   \]
   where \(\rho_0^*\) is the decreasing vertical rearrangement. Here \(H_0^k\) is the closure of smooth functions supported away from the walls, not simply the zero-trace \(H^k\) space. ([arxiv.org](https://arxiv.org/pdf/2403.14187))

   **(f) A relevant 2025 improvement. [Text]**

   Bianchini–Jo–Park–Wang, *Sharp asymptotic stability of the incompressible porous media equation*, **arXiv:2505.05165 (2025)**, works on **\(\mathbb T\times\mathbb R\)**. Theorem 1.1 assumes real \(k>2\),
   \[
   \inf_y(-\rho_s'(y))>0,\qquad
   \|\rho_s'\|_{C^{k+1}}<\infty,
   \]
   and sufficiently small \(H^k\) perturbation. It gives global uniform \(H^k\) control and
   \[
   \|\rho(t)-\rho_0^*\|_2\lesssim\varepsilon t^{-k/2}.
   \]
   **This is not, as stated, a theorem on \(\mathbb R^2\).** ([arxiv.org](https://arxiv.org/pdf/2505.05165v2))

   **(g) Kiselev–Yao, arXiv:2102.05213 (2021; ARMA 247, 2023). [Text]**

   These conclusions are conditional on global smoothness:

   - Theorem 1.1: nonzero \(\rho_0\in C_c^\infty(\mathbb R^2)\), odd in \(y\), nonnegative for \(y>0\), implies, for every \(s>0\),
     \[
     \int_0^\infty\|\rho(t)\|_{\dot H^s}^{-4/s}\,dt<\infty,
     \qquad
     \limsup_{t\to\infty}t^{-s/4}\|\rho(t)\|_{\dot H^s}=\infty.
     \]
   - Theorem 1.2: on \(\mathbb T^2\), additionally require evenness in \(x\), \(\rho_0(0,y)=0\), and nonnegativity on \([0,\pi]^2\). Then, for \(s>-1/2\),
     \[
     \limsup_{t\to\infty}
     t^{-(s+1/2)}\|\partial_x\rho(t)\|_{\dot H^s}=\infty.
     \]
     Odd periodic reflection also gives the corresponding strip result.
   - Theorem 1.5: any smooth stationary density on the confined strip admits arbitrarily small smooth \(H^{2-\gamma}\) perturbations, \(\gamma>0\), with unbounded higher Sobolev growth, again conditional on global smoothness.

   This is particularly relevant to your symmetries, but it neither proves finite-time blowup nor excludes self-similarity. ([arxiv.org](https://arxiv.org/pdf/2102.05213))

5. **Odd reflection, the wall, and growing-profile velocity.**

   **(a) The equivalence is valid with regularity and normalization qualifications. [Calculation]**

   Write \(Z^*=(z_1,-z_2)\). The Dirichlet Green function for \(-\Delta\) on \(\mathbb H\) is
   \[
   G_D(X,Z)=\frac1{2\pi}
       \log\frac{|X-Z^*|}{|X-Z|}.
   \]
   For sufficiently decaying data,
   \[
   \psi_+(X)=\int_{\mathbb H}G_D(X,Z)\,\partial_{z_1}\rho_+(Z)\,dZ
   \]
   is exactly the restriction of the whole-plane potential generated by
   \[
   \rho_o(x,y)=
   \begin{cases}
   \rho_+(x,y),&y>0,\\
   -\rho_+(x,-y),&y<0.
   \end{cases}
   \]
   Its stream function is odd in \(y\), so \(u_1\) is even and \(u_2\) odd; hence \(u_2=0\) on the wall. The same reflection preserves the transport equation.

   Conversely, a half-plane solution with zero density trace admits this odd extension in the corresponding classical class, provided the velocity is recovered using the matching Green-function normalization.

   **Zero trace alone does not give a smooth extension.** For a \(C^\infty\) odd extension one needs
   \[
   \partial_y^{2j}\rho_+(x,0)=0,\qquad j=0,1,2,\ldots.
   \]
   Zero trace is sufficient for a \(C^1\) odd extension of a \(C^1\) function, but not generally for \(C^2\). The \(X^k\) conditions above are the Sobolev counterpart of this issue. ([arxiv.org](https://arxiv.org/pdf/1804.08490.pdf))

   **(b) Nonzero wall density cannot be reflected into your smooth class.**

   If the upper trace is \(h(x)\ne0\), odd reflection has jump \(2h(x)\). It may provide a discontinuous weak whole-plane configuration, but not your smooth profile. Even reflection does not implement the same Darcy/Dirichlet problem. Subtracting a nonconstant wall trace changes both the transport equation and the induced velocity; it is not a symmetry.

   Thus the numerical wall profiles cannot simply be reinterpreted as your odd-in-\(y\) profiles.

   **(c) A sufficient renormalization for your growing class. [Calculation]**

   The order-zero Darcy kernel away from the origin is
   \[
   K(Z)=\frac1{2\pi}
   \left(-\frac{2z_1z_2}{|Z|^4},
          \frac{z_1^2-z_2^2}{|Z|^4}\right),
   \]
   with the additional local term \(-\tfrac12(0,R)\). This kernel representation is also displayed in the critical IPM paper. ([arxiv.org](https://arxiv.org/pdf/2410.01297))

   For locally smooth \(R\) with \(R(X)=O(|X|^\alpha)\), \(0\le\alpha<1\), one can define velocity differences by
   \[
   \begin{aligned}
   U(X)-U(0)
   ={}&\operatorname{pv}\int_{\mathbb R^2}
       [K(X-Z)-K(-Z)]R(Z)\,dZ\\
      &-\tfrac12(0,R(X)-R(0)).
   \end{aligned}
   \]
   The tail converges because the kernel difference is \(O_X(|Z|^{-3})\), giving the radial bound
   \(\int^\infty r^{\alpha-2}\,dr<\infty\). Your symmetry fixes \(U(0)=0\).

   **The closure at infinity matters:** the Poisson equation and your parity alone permit
   \[
   \psi\mapsto\psi+bxy,\qquad
   U\mapsto U+(-bx,by).
   \]
   This changes \(\psi_{xy}(0)\). A prescribed renormalized operator, or suitable sublinear velocity growth excluding this harmonic strain, is therefore part of the problem—not an optional convention.

6. **Smoothness selection and what it actually says about \(c_l\).**

   **(a) A necessary local resonance condition. [Calculation]**

   Let \(W(X_*)=0\), \(W\cdot\nabla R=R\), and suppose the first nonzero Taylor term of \(R\) at \(X_*\) is a homogeneous polynomial \(P_m\). Then
   \[
   R(X_*)=0,\qquad
   (A Z)\cdot\nabla P_m=P_m,\qquad A=DW(X_*).
   \]
   If \(A\) is diagonalizable with eigenvalues \(\mu_1,\mu_2\), some monomial appearing in \(P_m\) must satisfy
   \[
   j\mu_1+k\mu_2=1,\qquad j,k\in\mathbb N_0,\quad j+k=m.
   \]
   In particular, if \(\nabla R(X_*)\ne0\),
   \[
   A^{T}\nabla R(X_*)=\nabla R(X_*).
   \]

   At a hyperbolic source, a smooth solution flat to every order must vanish locally: backward trajectories approach the source exponentially, whereas \(R\) decreases along them exactly like \(e^{-s}\). An arbitrarily high Taylor remainder estimate then forces \(R=0\). Thus a **nontrivial smooth germ at a source must have a finite-order resonance**.

   This is necessary, not sufficient. Higher Taylor equations have compatibility conditions, and global matching must still determine the velocity and its derivatives.

   **(b) Your origin is a saddle in the numerical blowup range. [Calculation]**

   Put \(q=\psi_{xy}(0)\). Symmetry gives
   \[
   DU(0)=\operatorname{diag}(-q,q).
   \]
   Comparing the \(x^2y\) coefficient yields exactly
   \[
   2(c_l-q)+(c_l+q)=1,
   \qquad 3c_l-q=1.
   \]
   Consequently,
   \[
   DW(0)=
   \operatorname{diag}(1-2c_l,\ 4c_l-1).
   \]
   The origin is a source precisely when
   \[
   \frac14<c_l<\frac12.
   \]
   For \(c_l>1\), it is a saddle. Therefore a selection argument predicated on a source **at the origin** does not apply in that range. Other stagnation points may impose additional resonances, but they must be located and analyzed.

   The cubic compatibility alone does **not** quantize \(c_l\): it relates \(c_l\) to the globally determined strain \(q\).

   **(c) Relevant literature, with limits on its applicability.**

   Eggers–Fontelos, *The role of self-similarity in singularities of PDE’s*, **arXiv:0812.1339 (2008), Nonlinearity 22 (2009)**, surveys rigorous, formal, and numerical selection mechanisms; it is not an IPM selection theorem. ([arxiv.org](https://arxiv.org/abs/0812.1339))

   Their more directly relevant primary paper is *Selection of singular solutions in non-local transport equations*, **Nonlinearity 33 (2020), 325–340**, published online in December 2019. **I did not verify an arXiv number.** It studies fractional nonlocal transport/CCF-type models, derives an origin regularity constraint involving a global integral of the profile, and numerically follows stable and unstable branches. This illustrates why nonlocal strain enters exponent selection; its numerical branch construction is not a general existence or quantization theorem for IPM. ([people.maths.bris.ac.uk](https://people.maths.bris.ac.uk/~majge/Eggers_2020_Nonlinearity_33_325.pdf))

   Elgindi–Ghoul–Masmoudi’s **arXiv:1906.05811 (2019)** concerns stable blowup in a family of one-dimensional nonlocal transport/stretching equations. Their **arXiv:1910.14071 (2019)** concerns finite-energy \(C^{1,\alpha}\) Euler blowup and localization of self-similar dynamics. Neither supplies an IPM theorem determining your \(c_l\). ([arxiv.org](https://arxiv.org/abs/1906.05811), [arxiv.org](https://arxiv.org/abs/1910.14071))

   What remains unverified is therefore specific: **a smooth growing whole-plane IPM profile in your cubic symmetry class, a theorem selecting its exponent, and a rigorous validation of the numerical IPM wall candidates.** The results above provide useful obstructions and comparisons, but do not settle those questions.

The requested Opus 5.5 consultation was unavailable: the configured Bedrock client could not retrieve AWS credentials. No other model was substituted.