# Independent 48-hour research assignment: Rigorous error analysis for the existing full-plane IPM self-similar numerical profile

## 0. Nonnegotiable mission, runtime, and outcomes

You are beginning a **standalone mathematical/computer-assisted research project**. All context needed to understand the target PDE, the numerical evidence, and a previous *conditional* analytical approach is included below. **Do not assume that you can access earlier conversations, reports, or code unless you actually discover those files in your workspace.** Do not invent missing coefficient files, computations, verifiers, proofs, or figures.

**Principal task:** Determine whether the currently reported high-accuracy, even-in-`x`, odd-in-`y`, full-plane IPM self-similar profile can be justified by a *rigorous, quantitative a posteriori error analysis*. We want an actual exact solution of the fully coupled, canonical, full-plane profile equation near a reconstructible numerical approximation, with an explicit error bound in a function space that makes every equation meaningful. This is not a request merely to improve a numerical fit or re-state its residual.

**Research-duration rule (STRICT):** Unless one of the decisive endpoints defined below has actually been achieved and independently verified, perform **at least 48 hours of genuine wall-clock research**, recorded with real UTC timestamps. Reading, mathematical derivations, implementations, tests, counterexamples, theorem/proof audits, and constructive computational work count; artificial idle time, a promise to continue later, fabricated parallel agents, or stale work from before the start do not. If the environment interrupts a long run, checkpoint work, restart, and accurately distinguish active work, elapsed wall time, and interruptions. Report early termination **only** for a fully decisive endpoint. If no decisive endpoint has been attained at 48 hours, report **UNRESOLVED**, accurately distinguishing successes from gaps. If a platform cannot support genuinely elapsed 48-hour work, state the limitation rather than falsely attesting to its completion.

Acceptable **decisive** endpoints, either of which permits finishing before 48 hours:

- **YES — rigorous a posteriori existence:** A self-contained theorem and a completely reproducible proof (analytical with quantitatively validated computation if necessary) establishing an exact solution `(rho, psi, c_l)` of the specified **full-plane canonical equation** within an explicitly bounded neighborhood of an explicitly reconstructible numerical profile (X3 or an improved/refined profile in its same branch). Specify precisely whether the theorem concerns the finite-regularity class `P_2`, a stronger `P_m`, or the smooth class `P_infty`. Include every hypothesis, an actual validated residual bound in the target norm, inverse/linear stability estimate, nonlinear remainder estimate, normalization/gauge treatment, and a strictly verified closing inequality. A partial inverse estimate, a small residual, or a computer floating-point certificate with unbounded error does **not** qualify as YES.
- **NO — rigorous and properly scoped exclusion:** A theorem with independently audited proof that **no exact solution exists in a precisely stated, nontrivial neighborhood of the explicit candidate**, under the full PDE, canonical gauge, symmetries, center factorization and specified target topology (or a stronger theorem excluding the entire requested branch). Quantify the neighborhood and clearly distinguish `P_2` from `P_infty`. A demonstration that one chosen energy estimate is indefinite, that one Banach norm fails, that one Newton method diverges, or that the *specific numerical trial* has a nonzero residual does **not** qualify as NO. If the neighborhood is too narrow to contain a meaningful numerical-uncertainty ball, disclose that and do not present an empty/formal exclusion as a decisive result.

If neither endpoint is proved, the verdict is **UNRESOLVED** after at least 48 hours, including sharp, verifiable conditional estimates and precise remaining obstructions. **A YES based only on numerical evidence is NOT a decisive endpoint for this project.** (Numerical evidence was an allowable YES in an earlier *numerical discovery* study, but not in this *a posteriori existence* study.)

Use a **researcher** and a genuinely **independent, adversarial verifier** whenever parallel or separate implementations are available. The verifier must reconstruct critical identities, test the correct PDE and domain, challenge every inequality and numerical rounding, and reject unproved functional-analytic assertions. Do not simulate an independent reviewer merely by labelling your own unchecked notes “verified.”

**Methodological freedom:** A previous `Phi`-energy and `q = partial_x h` Hölder path is reproduced below as a **reference to explore only if useful**. You are expressly authorized, and encouraged when justified, to abandon, localize, replace, or combine it with other methods. **Do not waste the 48 hours trying to force conditions already known to fail.** The goal is the actual a posteriori error theorem, not the survival of a particular proof strategy. Do not use a numerical search for a different origin-degeneracy branch in place of this task.

---

## 1. Exact mathematical problem: full-plane stationary IPM

Unknowns are a real density `rho(X)`, real stream function `psi(X)`, real scaling parameter `c_l`, with `X=(x,y) in R^2`, and

\[
\boxed{\begin{aligned}
&(c_lX+U)\cdot\nabla\rho=\rho,\\
&U=(-\psi_y,\psi_x)=\nabla^\perp\psi,\\
&-\Delta\psi=\partial_x\rho \quad\text{on }\mathbb R^2.
\end{aligned}}
\tag{IPM-SS}
\]

Require the *old/known numerical branch*, not the nondegenerate `rho_y(0) != 0` branch:

\[
\boxed{\rho(-x,y)=\rho(x,y),\qquad \rho(x,-y)=-\rho(x,y).}
\]

Thus `psi` is odd in both coordinates; `U_1` is odd in `x`, even in `y`; `U_2` is even in `x`, odd in `y`. Locally around the origin, require the **strong factorization**

\[
\boxed{\rho(x,y)=x^2y\,a(x,y),\quad a(-x,y)=a(x,y),\quad a(x,-y)=a(x,y),\quad a(0,0)=1.}
\tag{center}
\]

A first admissible target class is the previously distinguished **`P_2`**:

- `rho in C^{2,alpha}_loc(R^2)` for some `0 < alpha < 1`, with the center factor `a` merely continuous near `(0,0)`; *the factorization is required, not just the cubic Taylor jet*;
- the parity above and the exact, canonical, full-plane Poisson/velocity law below;
- for some `gamma < 1`, a global sublinear-growth bound
  \[
  |\rho(X)|+(1+|X|)|\nabla\rho(X)|\le C(1+|X|)^\gamma;
  \]
- the stationary equation pointwise and nontrivial normalization `a(0)=1`.

A separately distinguished **`P_infty`** class strengthens the center condition to `a in C^infty` near zero (while retaining a clearly stated global differentiability class). The problem originally requested in the numerical study was `P_infty`; the numerical report's evidence, however, supports only the **weaker `P_2`** target. Be **completely explicit** about which class you prove existence for. A `P_2` theorem would be major progress, but **does not settle `P_infty`**.

Canonical whole-plane inverse / gauge is essential. Do **not** permit an arbitrary harmonic `lambda*x*y` in `psi`; that would add a linear strain and change `c_l`. Equivalent canonical characterizations under the decay/growth assumptions are: `div U=0`, `curl U=-partial_x rho`, the parity, and `U(X)=o(|X|)` at infinity. One explicit angular-mode formulation is: if

\[
\partial_x\rho=\sum_{n\ge1} f_n(r)\sin(2n\theta),\qquad
\psi=\sum_{n\ge1}\psi_n(r)\sin(2n\theta),
\]

then

\[
\boxed{\psi_n(r)=\frac1{4n}\left[r^{-2n}\int_0^r s^{2n+1}f_n(s)\,ds
+r^{2n}\int_r^\infty s^{1-2n}f_n(s)\,ds\right].}
\tag{Green}
\]

Check the formula from `-Delta psi=partial_x rho`, including signs, normalization of angular modes, differentiability, convergence at 0/infinity, and how far-field tails affect local strain. Another characterization uses the velocity singular integral with local term `-rho*e_2/2` and kernel

\[
K_1(Z)=-\frac{z_1z_2}{\pi|Z|^4},\qquad
K_2(Z)=\frac{z_1^2-z_2^2}{2\pi|Z|^4}
\]

under symmetric truncation. Validate implementation independently where possible.

Set `c = psi_xy(0,0)`. Comparing the lowest-order `x^2 y` term in `(IPM-SS)` gives the **exact scaling constraint**

\[
\boxed{3c_l-c=1,\qquad c_l=\frac{1+\psi_{xy}(0,0)}3.}
\tag{norm}
\]

For a correction `h` preserving `a(0)=1`, the linear scaling functional is

\[
\boxed{c[h]=\frac13\,\psi[h]_{xy}(0,0),\quad -\Delta\psi[h]=\partial_x h.}
\tag{rank-one}
\]

Do **not** mistakenly use `c_l=1/2+psi_xy(0)`: that was the **old half-plane** setup with boundary density behaving as `x^2`, not the current **full-plane `x^2 y`** branch. Do **not** import the `c_l+psi_xy(0)=1` identity: that belongs to the *different* `y`-leading branch and is also not the current problem.

Under the center/growth restrictions, nonzero profiles in the reported admissible class have `c_l>1`. In the numerical reconstruction, the far-field scaling is `k=1/c_l` with `0<k<1`. Treat any theorem used to deduce `c_l>1` as a theorem requiring its own hypotheses, rather than silently assuming it for all conceivable variants.

### Local geometry and characteristic issues

Let `V=c_lX+U`. By symmetry and (norm),

\[
DU(0)=\mathrm{diag}(-(3c_l-1),3c_l-1),
\]
\[
\boxed{DV(0)=\mathrm{diag}(1-2c_l,\,4c_l-1).}
\]

At `c_l ~= 5.57536`, the origin is a saddle for the *rescaled* characteristic field: eigenvalues roughly `-10.1507` and `+21.3015`. The physical `U` also carries strong nonlocal linear strain at zero; `rho=O(|X|^3)` does **not** imply `DU(0)=0`.

The old numerical branch also has a first positive root `x_*` of `V_1(x,0)` near `x_*=8.600064`; set `P=(x_*,0)`. For an exact admissible profile with positive axis derivative on `(0,x_*]`, previously derived source-point identities are

\[
\partial_xV_1(P)=2c_l-1,\quad \partial_yV_2(P)=1,\quad
\rho_y(P)>0.
\]

Thus `P` is a **source** of `V` in the plane, with eigenvalues about `10.1507` and `1`. Other fixed points and absence of zeros require *validation*; sampled grid tests do not prove global nonexistence of extra equilibria. Source/saddle dynamics, separatrices, and the possibility of fractional regularity can dominate the Fredholm/inverse problem.

### Connection to physical finite-time gradient blowup, and its limitation

If an exact nontrivial profile with `c_l>1` exists, define

\[
\alpha=\frac1{c_l-1},\quad \beta=\frac{c_l}{c_l-1}=\alpha+1,\quad
X=\frac Z{(T-t)^\beta},
\]
\[
\varrho(t,Z)=\alpha(T-t)^\alpha\rho(X),\quad
u(t,Z)=\alpha(T-t)^\alpha U(X),\quad
\Psi(t,Z)=\alpha(T-t)^{\alpha+\beta}\psi(X).
\]

These solve physical unforced IPM with `|grad_Z varrho| ~ (T-t)^{-1}` in supremum norm when the profile has nonzero bounded gradient. However the existing profile grows as `r^{1/c_l}` at infinity and is unbounded there: existence would **not by itself** prove gradient blowup from bounded or compactly supported global density. The central research goal remains the **profile error theorem**; do not divert to proving localization of physical blowup unless it directly enables the error analysis.

---

## 2. Reproducible facts about the existing numerical candidate (report's `X3`)

These are reported computations, **not certified global bounds**. Independently reproduce any such values on which your argument relies. The previous final numerical report was a 42.46-hour study; its **YES** meant *strong numerical evidence for `P_2`, not an existence proof*. It expressly left the smooth `P_infty` existence question unanswered.

- Candidate label: **`X3`** (sometimes coefficient filename **`c6g_shape.npz`**; reported MD5 `15f8095f7e79dbfa0c50d75e5fe8997a`). Same-budget free-`c_l` control `F3`: **`c6gF_shape.npz`**, reported MD5 `0398af3f08a2a4f75e42c846edbaa375`.
- Held numerical exponent: `c_l = 5.575362610641546` (rounded `5.5753626`). Canonical inverse of the stored density gives `(1+psi_xy(0))/3 ~= 5.5753626074`; **discrepancy about `3.2e-9`**. The held number was **not uniquely determined by the equation**; different nearby `c_l` values yielded competitive fits. Even `[5.5524653, 5.5793640]` is only a span of *tested, not-yet-excluded fitting exponents*, NOT a certified enclosure of any exact exponent. An independently fitted fixed-`c_l` profile at `5.5683739` improved some residual diagnostics relative to X3.
- Spatial scale `L = 7.6514246`; `k=1/c_l ~= 0.17936053`.
- First positive source point `x_* ~= 8.600064`; measured `|partial_y V_2(P)-1|` decreased from around `2.8e-7` to `3.1e-8` to `1.8e-8` as radial evaluator resolution increased. This is a **consistency check**, not a rigorous root enclosure.
- The candidate uses **375 radial spline coefficients per angular mode** and angular modes `m <= 200`, degree-7 clamped splines; a refinement row `m <= 250` and a variety of further-budget/domain fits exist in the reported study. The current X3 is not the unique best fit at all budgets or norms; improvement under refinement does not yet give a posteriori invertibility.

### Explicit trial-function family

In polar coordinates `(r,theta)` with `u=r/L`, let

\[
q_r=1-(1+u^2)^{-(1-k)/2},\qquad
\chi=\frac{u^2}{u^2+r_0^2},\quad r_0=0.02,
\]
\[
\boxed{\bar\rho=x^2y\exp(H),}
\]
\[
\boxed{\begin{aligned}
H={}&\frac{k-3}{2}\log(1+u^2)
+\sum_{m=0}^{M}\chi^{\max(m-1,0)}b_m(q_r)\cos(2m\theta)\\
&+\left(\frac{u^2}{1+u^2}\right)^{p_3/2}
|\cos\theta|^{p_3-2}\sin^2\theta\,T(2q_r-1),
\end{aligned}}
\tag{ansatz}
\]

with `M=200`, `p_3=6+2/(2c_l-1)`, radial degree-7 clamped splines `b_m` with `b_m(0)=0`, 375 coefficients per mode, and `T` a degree-5 Chebyshev polynomial. The radial-knot scheme and spline coefficients are **not supplied by these formulas or by the text report**; **actual coefficient files are necessary to reproduce the precise X3 field**. If the repository has those coefficient files, verify and use them. If absent, do not pretend that the X3 residuals or a theorem near X3 have been reproduced; seek the artifacts, or explicitly build a *new* candidate and prove a theorem about that new candidate.

Candidate has `p_3 ~= 6.19703`, `beta_reg=p_3-6 ~= 0.19703`. The explicit fractional-power part and the spline regularity make the **trial itself** `bar rho in C^{6,beta_reg}_loc`, `a in C^{4,beta_reg}_loc`; it is not `C^infty`. This does **not** prove an exact nearby profile has only this regularity, nor that an exact `P_infty` profile is impossible.

At infinity, the reported ansatz has a two-term expansion

\[
\bar\rho(r,\theta)=r^k\Theta_0(\theta)
\bigl(1+r^{k-1}\Theta_1(\theta)+O(r^{2k-2})\bigr).
\tag{far}
\]

The leading homogeneous growth `r^k` is essential; polynomial growth of the background invalidates naive unweighted `L^2` or `dot H^{-1}` assumptions. Its velocity is obtained from the full-plane inverse, not by imposing a wall boundary condition or an arbitrary exterior affine strain. **Far-field asymptotic coefficients must satisfy the PDE's own compatibility equations**; splines continued past their fit region do not guarantee that.

### Numerical residual definition and reported maximum values

Define **unnormalized, true profile residual**

\[
\boxed{\varepsilon(X)=(\bar c_l X+\bar U)\cdot\nabla\bar\rho-\bar\rho.}
\]

Define the two **pointwise denominator functions**

\[
\boxed{N_f=|\bar V_1\bar\rho_x|+|\bar V_2\bar\rho_y|+|\bar\rho|,}
\]
\[
\boxed{N_v=|\bar\rho|+|X\cdot\nabla\bar\rho|+|\bar U\cdot\nabla\bar\rho|.}
\]

The report's headline on independent **between-node** evaluator grids, for X3, was

\[
\max\frac{|\varepsilon|}{N_f}=6.83\times10^{-7}\ \text{to}\ 7.16\times10^{-7}
\quad\text{(over three fine grid configurations)},
\]
\[
\max\frac{|\varepsilon|}{N_v}\le 1.112\times10^{-6}
\quad\text{(full evaluated radial range; far-field maximum)},
\]

and about `1.91e-7` to `2.01e-7` for `max |epsilon|/N_v` restricted to `r <= 1000` **with the evaluator's near-`y`-axis cancellation-floor columns excluded**. The report also supplied **absolute** (`not normalized`) sampled maxima:

| Region | Max `|epsilon|` on evaluator grid (approximately) |
|---|---:|
| `r <= 0.1` | `1.71e-13` |
| `0.1 <= r <= 2` | `8.92e-8` |
| `2 <= r <= 10` | `6.03e-5` |
| `|X-P| < 0.5` | `1.05e-5` |
| `10 <= r <= 100` | `1.99e-5` |
| `100 <= r <= 1000` | `6.03e-6` |
| `1000 <= r <= 7.652e6` | `1.897e-4` |

Thus `max_{r<=1000}|epsilon| ~= 6.03e-5` and the full evaluated-region absolute maximum is about `1.897e-4` (outer, unfitted region). **These are sampled maxima, not rigorous `L^infty` bounds on R^2, nor certified forcing norms in your function space.** The elliptic equation is solved by a numerical inverse, not separately fitted; the elliptic inversion error must be enclosed separately if used in a theorem.

The report's numerical optimizer minimized a *weighted Euclidean fit residual*, essentially `(V.grad bar rho - bar rho)/(|bar rho|+|X.grad bar rho|)` at fitting nodes, plus center/source constraints. Its reported objective for X3 was `1.619e-6` (depends on number of fit points, weights, and sample grid). **Do not equate this to either normalized maximum or an unweighted absolute residual.**

The smallest-normalization denominators vanish on axes/at equilibria. Never silently treat `0/0` as zero; control limits from Taylor expansions, derivative residuals, or certified enclosures, and independently diagnose cancellation floors in pointwise evaluation.

### Far-field and characteristic diagnostics

- Near `P`, the flux-normalized maximum is roughly `6.5e-7` to `7.2e-7`. A dense 857-label characteristic defect was about `1.388e-6` at cutoff `eps_P=0.03`, and about `1.602e-6` at `eps_P=0.01`. This diagnostic is a **spread**, not an absolute transport error or a global bound; its logarithmic common mode may be invisible to the spread.
- Outside the main fitted band (`r > 1000*L`), `N_v` normalized maximum is about `1.09e-6` to `1.112e-6`, around `r=3.6e4`–`3.7e4` close to the `y` axis. A numerical fit with actual rows out to `9000*L`, together with enlarged inverse radius and extra iterations, reduced one tested far band to approximately `3e-8`; this indicates that the original far residual is substantially a defect of its unfitted exterior continuation, **not** an inherent numerical floor. Differences in fit rows, inverse domain, and iteration budgets must be separately attributed.
- The first asymptotic correction `Theta_1` is constrained by `Theta_0` through the profile equation. For `psi_0=r^{k+1}F(theta)` the report derived the formal relation
  \[
  \boxed{(c_l-1)\Theta_0\Theta_1
  =(k+1)F\Theta_0'-kF'\Theta_0.}
  \]
  The original X3's stored vs forced `Theta_1` mismatch at the `y` axis was about `4.08e-3`. The outer residual is a mixture of several orders, not just the leading mismatch; check any perturbative far-field analysis carefully.
- There is an intrinsic **soft numerical direction in `c_l`**. Fixed-`c_l` fits at different exponents have comparable, sometimes better residuals; neither the exact exponent nor isolation of the solution was established. A proof must control/quotient this direction or show it corresponds to a legitimate family. Do not assume a unique solution from the displayed digits.

### Critical regularity warning (`B_3`)

Write `g(x)=rho_y(x,0)`, `G_3(x)=partial_y^3 rho(x,0)/6` and `w(x)=V_1(x,0)`. Under sufficient axis differentiability, the `G_3` equation contains a homogeneous solution

\[
\boxed{G_3^{hom}(x)=B_3 |x|^{p_3} e^{E(x)},\qquad
p_3=6+\frac2{2c_l-1}.}
\]

Smooth `a` near zero forces `B_3=0`; analogous compatibilities occur in higher odd-in-`y` coefficients. The *axis-data estimator* of `B_3` on X3 was roughly `0.299` to `0.303` (natural units `x_*^{2-p_3}`), but the trial's actual inserted coefficient of the fractional `y^3 |x|^{p_3}` term was only about `+0.046` in the same units. Their difference, roughly `0.25`, is accounted for by **defects of the trial in the `y` and `y^3` coefficient equations** along the `x` axis; it is not an exact-profile contradiction and not evidence of an error bound on `B_3` of a nearby exact solution. A rigorous `P_infty` claim requires genuine control of those regularity compatibility coefficients. A `P_2` existence theorem does not need to force `B_3=0`.

---

## 3. Exact perturbation equation and the *previous* conditional analysis

**The following is reproduced as context, NOT as a mandatory or already-closed proof.** The original derivation concerned the upper half-plane with a *different origin normalization* `c_l=1/2+psi_xy(0)`. The local algebra can be carried to the whole plane with the current `1/3` normalization, but the estimates relied on numerical/background positivity conditions that **provably fail here**. Re-derive identities, signs, regularity and decay independently before using them.

Let `(bar rho, bar psi, bar c_l)` be a numerical background, compute `bar U` from the canonical inverse, and define

\[
\bar V=\bar c_lX+\bar U,\quad
G=X\cdot\nabla\bar\rho,\quad
\varepsilon=\bar V\cdot\nabla\bar\rho-\bar\rho.
\]

Let the unknown correction be `h` and

\[
-\Delta\psi[h]=\partial_xh,\quad U[h]=\nabla^\perp\psi[h],\quad
c[h]=\frac13\psi[h]_{xy}(0),\quad V[h]=U[h]+c[h]X.
\]

Set `rho=bar rho+h`, `c_l=bar c_l+c[h]` if `bar c_l=(1+bar psi_xy(0))/3` **exactly** (otherwise add and track the explicit scalar normalization defect). The exact perturbation equation is

\[
\boxed{\bar V\cdot\nabla h-h+U[h]\cdot\nabla\bar\rho
+c[h]G+V[h]\cdot\nabla h=-\varepsilon.}
\tag{pert}
\]

The complete linearization is

\[
\boxed{Lh=L_0h+c[h]G,\qquad
L_0h=\bar V\cdot\nabla h-h+U[h]\cdot\nabla\bar\rho.}
\tag{lin}
\]

If the numerical background has `a_bar(0)=1` exactly, corrections must preserve it, for instance `h=x^2 y b` near zero with `b(0)=0` (in whatever topology can truly evaluate these quantities). Do not let a spurious scalar normalization direction slip through, and distinguish genuine scale freedom from fixed normalization.

### 3A. The former `Phi` energy

For perturbation `h` let `-Delta Phi=h` on `R^2`, with the same odd-in-`y` parity and canonical decay/gauge; then `psi[h]=Phi_x` and `U[h]=(-Phi_xy,Phi_xx)`, provided the underlying inverse exists in the function space. Set

\[
S(\bar U)=\frac{D\bar U+(D\bar U)^T}{2},\qquad
E_\Phi=\|\nabla\Phi\|_{L^2(R^2)}.
\]

For sufficiently decaying/regular perturbations, integration by parts yields the identity

\[
\boxed{-\langle L_0h,\Phi\rangle
=\int_{R^2}\nabla\Phi^T M_\Phi(X)\nabla\Phi\,dX,}
\]
\[
\boxed{M_\Phi=(1+2\bar c_l)I+S(\bar U)
+\begin{pmatrix}\bar\rho_y&-\bar\rho_x/2\\-\bar\rho_x/2&0\end{pmatrix}.}
\tag{Phi-matrix}
\]

In the earlier half-plane argument one hoped for `delta_Phi=inf_X lambda_min(M_Phi(X))>0` and then

\[
\delta_\Phi E_\Phi^2
\le |\langle\varepsilon+c[h]G+V[h]\cdot\nabla h,\Phi\rangle|.
\]

**However this positivity condition is FALSE for the actual full-plane X3 branch.** From `bar rho=x^2 y a`, `bar rho_x(0)=bar rho_y(0)=0`, `bar psi_xy(0)=3bar c_l-1`, and the parity of `bar psi`,

\[
\boxed{M_\Phi(0)=\operatorname{diag}(2-\bar c_l,\ 5\bar c_l)
\approx\operatorname{diag}(-3.57536,27.87681).}
\tag{indefinite}
\]

The negative first direction is a genuine negative direction for the quadratic form on localized parity-compatible perturbations (take an `x`-oscillatory test potential supported near but away from the coordinate axes), even when `c[h]=0`. Thus the original *uniform pointwise positive-matrix proof* cannot work unchanged. This **does not prove spectral instability** or noninvertibility of `L`, nor does it imply `Phi` itself is dynamically unstable: an indefinite stationary energy pairing is not a spectrum theorem. Try other energies (anisotropic/symmetrized, microlocal, weighted, spatially localized, including lower-order corrections), or bypass this energy entirely if more effective. For any new weight, recheck boundary terms and how the nonlocal `U[h]` commutator enters; do not assume (Phi-matrix) stays identical after weighting.

### 3B. Previous `q=partial_x h` equation (exact algebra; global damping fails)

Let `q=partial_x h`, `W=bar V+V[h]`, and `g=grad(bar rho+h)`. Write the **transport coefficient** as `a_tr` to avoid confusion with center factor `a`:

\[
a_{tr}=\frac{\partial_x\bar V_2}{\bar V_2},\qquad
 d=1-\partial_x\bar V_1+a_{tr}\bar V_1,
\]
\[
B=\nabla\bar\rho_x-a_{tr}\nabla\bar\rho,\qquad
C=G_x-a_{tr}G,\qquad
R=-\varepsilon_x+a_{tr}\varepsilon.
\]

On regions where `bar V_2 != 0`, differentiation of (pert), and elimination of the **linear** `partial_y h` via the original transport equation, yields

\[
\boxed{W\cdot\nabla q-(d-c[h])q+U[q]\cdot g
=R-a_{tr}h-U[h]\cdot B-c[h]C
+a_{tr}V[h]\cdot\nabla h.}
\tag{q-equation}
\]

Here `U[q]=partial_x U[h]` is an **order-zero** nonlocal operator acting on `q` (for instance `-Delta psi[h]=q`), whereas `U[h]` is one derivative smoother relative to `q`. Keeping `V[h].grad q` in the full transport field avoids treating a derivative-losing nonlinear term as source, but `g` and the last forcing remain nonlinear. Check this equation and all its sign/quotient domains independently.

For the **strict linearization** retain `c[h]` as a rank-one source:

\[
\boxed{\bar V\cdot\nabla q-dq+U[q]\cdot\nabla\bar\rho
=R-a_{tr}h-U[h]\cdot B-c[h]C.}
\]

On `y=0`, by parity `bar V_2=y b(x,y)`; where `b!=0`, `a_tr=b_x/b` has a continuous axis limit. That does **not** guarantee a global extension through other zeros of `bar V_2`. Verify any divisions before using them.

The old proof required `gamma_0=inf_X d>0` and a forward-flow Hölder gap. This too **fails near the new source point `P`**. For an exact profile at `P`, `bar V_1(P)=0`, `partial_x bar V_1(P)=2c_l-1`, so

\[
\boxed{d(P)=1-(2c_l-1)=2-2c_l\approx-9.15073<0.}
\tag{negative-d}
\]

Thus the former global `gamma_0>0` estimate cannot be transferred. **Do not claim that lowering the Hölder exponent or improving a Schauder constant repairs negative `inf d`.** Geometry-adapted forward/backward resolvents, stable/unstable manifold matching, spatial weights, axis-boundary equations, Fredholm arguments or completely different function spaces may be necessary.

### 3C. The conditional forward-flow Hölder route (for reference only)

For a scalar stationary equation

\[
W\cdot\nabla f-\widetilde d f=H
\]

with forward flow globally defined and functions bounded, the previous route used

\[
\gamma=\inf\widetilde d,\qquad
L_{flow}=\sup_X\lambda_{max}\left(\frac{DW+(DW)^T}{2}\right),
\]
\[
\Delta=\gamma-\alpha L_{flow},\qquad \theta=1-\alpha L_{flow}.
\]

Under `gamma>0` and `Delta>0`, integrating along forward characteristics yields

\[
\gamma\|f\|_\infty\le\|H\|_\infty,\qquad
\Delta[f]_{C^\alpha}
\le [H]_{C^\alpha}+\frac{[\widetilde d]_{C^\alpha}}\gamma\|H\|_\infty.
\]

For the `h` transport equation, the analogous sufficient condition is `theta>0`. For the `q` equation, the top-order nonlocal contribution must be estimated in a Hölder space by a *valid quantitative coefficient* `K_alpha(g)`:

\[
[U[q]\cdot g]_{C^\alpha}
\le (K_\alpha(g)+\eta)[q]_{C^\alpha}
+C_{\eta,g} E_\Phi.
\]

The Fourier principal symbol (up to the chosen sign convention for `psi`) is

\[
\boxed{m_g(\xi)=\frac{g_1\xi_1\xi_2-g_2\xi_1^2}{|\xi|^2}.}
\]

Its `L^2` multiplier supremum does **not** automatically give a valid or sharp `C^alpha` operator norm. Previously proposed closure required

\[
\gamma_0=\inf d>0,\qquad \theta_0=1-\alpha L_{flow}>0,
\qquad\gamma_0-\alpha L_{flow}>K_\alpha(\nabla\bar\rho),
\]

and *separate treatment of the scaling functional* `c[h]`. This chain is conditional, and its first positive-damping condition fails for X3. For any modified estimate, exhibit the exact new operator, weights, norm, principal coefficient and strict inequality; reject abstract big-`O` absorption and unjustified `K_alpha=1`.

For scaling feedback, the local Schauder estimate has the form

\[
|c[h]|\lesssim_\alpha \frac13\left(\|q\|_{C^\alpha(B_2)}+E_\Phi\right)
\]

under compatible space and potential bounds, but the `q` coefficient is **not arbitrarily small** and cannot simply be absorbed. If `L_0^{-1}` is actually bounded, one can formally use a Sherman–Morrison-style rank-one reduction. Let `w=L_0^{-1}G`; then (with the chosen sign conventions) invertibility of `L=L_0+c[\cdot]G` would require

\[
\boxed{1+c[w]\ne0.}
\]

This is merely an optional route and **depends on establishing `L_0^{-1}` in a compatible space**, including the fact that `G` belongs to the correct codomain. Alternative formulations may treat `c_l` as a scalar unknown and add the normalization equation to the joint system instead of forming rank-one `L`.

### 3C-extra. Complete form of the old *conditional* combined Hölder estimate

The original analysis defined, on a domain and in a function space where **all** these quantities are finite,

\[
Q=[q]_{C^\alpha},\quad E_\Phi=\|\nabla\Phi\|_2,\quad
D=[d]_{C^\alpha},\quad
 a_0=\|a_{tr}\|_\infty,\quad a_\alpha=[a_{tr}]_{C^\alpha},
\]

and a forcing gauge for the scalar transport estimate

\[
\mathfrak T(H)=[H]_{C^\alpha}+\frac D\gamma\|H\|_\infty.
\]

The background-only residual and scaling quantities were

\[
\boxed{\begin{aligned}
\mathfrak R={}&\mathfrak T(R)
+\frac{a_0}{\theta}[\varepsilon]_{C^\alpha}
+\left(a_\alpha+\frac{Da_0}{\gamma}\right)\|\varepsilon\|_\infty,\\
\mathfrak C={}&\mathfrak T(C)
+\frac{a_0}{\theta}[G]_{C^\alpha}
+\left(a_\alpha+\frac{Da_0}{\gamma}\right)\|G\|_\infty,\\
\mathfrak N={}&\mathfrak T\bigl(a_{tr}V[h]\cdot\nabla h\bigr).
\end{aligned}}
\tag{former-source-constants}
\]

The tame interpolation sought was, for every fixed `eta>0`,

\[
\|U[h]\|_{C^\alpha}\le\eta Q+C_{\eta,\alpha}E_\Phi,
\]
\[
[U[q]\cdot g]_{C^\alpha}
\le(K_\alpha(g)+\eta)Q+C_{\eta,g}E_\Phi.
\]

Combining these with the flow estimates led **conditionally** to

\[
\boxed{(\Delta-K_\alpha(g)-\tau)Q
\le \mathfrak R+|c[h]|\mathfrak C+\mathfrak N+C_\tau E_\Phi,}
\tag{former-Q-inequality}
\]

for arbitrary fixed `tau>0` after choosing the interpolation parameters, provided `gamma>0`, `theta>0`, `Delta>K_alpha(g)+tau`, and the background and nonlinear coefficients satisfy the required bounds. The corresponding supremum estimate was

\[
\gamma\|q\|_\infty\le
\underbrace{\|R\|_\infty+a_0\|\varepsilon\|_\infty}_{\mathfrak R_\infty}
+|c[h]|\underbrace{(\|C\|_\infty+a_0\|G\|_\infty)}_{\mathfrak C_\infty}
+\|a_{tr}V[h]\cdot\nabla h\|_\infty
+\eta_\infty Q+C_{\eta_\infty}E_\Phi.
\]

In the strict linearized equation set the last nonlinear forcing to zero and `g=grad bar rho`. This provides the old target estimate

\[
\|h_x\|_{C^\alpha}
\le C_R\|\varepsilon\|_{C^{1,\alpha}}
+C_c|c[h]|+C_EE_\Phi,
\]

**only if** the stated forward-flow gaps, the top-order Schauder coefficient, and the source norms truly exist. The old argument intentionally left `C_E` potentially large and did not absorb the scalar `c[h]` feedback. **All four original obstacles remain relevant here**: negative `inf d`, possible zeros of `bar V_2`, no positive `Phi` energy, and unbounded `G`/far source in the unweighted source norm. This material is provided so you can reuse individual valid identities or estimates, **not** to demand their closure or pretend the conditions hold.

### 3D. Far-field incompatibility of the former unweighted energy

The background grows as `bar rho ~ r^k Theta_0`, `k=1/bar c_l>0`, so

\[
G=X\cdot\nabla\bar\rho\sim k r^k\Theta_0.
\]

Generally `G notin L^infty`, and in this unweighted two-dimensional setting `G` does not define a bounded functional on homogeneous `dot H^1` tests, hence `G notin dot H^{-1}`. A ring test `varphi_R(X)=varphi(X/R)` has `||grad varphi_R||_2` independent of `R` but `\langle G,varphi_R\rangle ~ R^{k+2}` if angular projections are nonzero. Likewise, a nonzero far residual `epsilon ~ r^{2k-1} F(theta)` pairs with the ring as `R^{2k+1}`, so `epsilon notin dot H^{-1}` in general despite pointwise decay. Do not turn small pointwise normalized residuals into a false `dot H^{-1}` bound.

You may subtract a rigorously constructed asymptotic background/counterterm; use properly weighted Hölder or Sobolev norms; divide core from far field and prove matching; or use a domain compactification with validated exterior. Whatever you choose, define how the nonlocal canonical velocity reacts to asymptotic changes. Unweighted `E_Phi=||grad Phi||_2` may still make sense for a specially constrained **decaying correction**, but `c[h]G` and the numerical residual can lie outside the corresponding forcing space. Such a constraint must be proved, not presumed.

---

## 4. Possible alternative research paths — choose by actual mathematical merit

**Do not interpret this list as required subproblems.** You must actively test and reprioritize routes; the reported obstructions justify switching strategy. Several strong alternatives are:

1. **Weighted/anisotropic or conormal Banach spaces.** Separate source/saddle sectors and stable/unstable directions of `V`. Solve the transport component on appropriate forward/backward characteristics, impose matching/compatibility across separatrices, and bound the order-zero IPM coupling without an illicitly small Hölder constant. Explicitly test regularity loss near `P` and the fractional-power mode at the origin.
2. **Fredholm and microlocal analysis.** Study `V.grad -1+U[.]grad bar rho` as a nonlocal, order-zero perturbed transport operator in spaces adapted to the dynamical structure, without assuming the nonlocal part is compact or lower order. Characterize kernel/cokernel, index, weight resonances and any exponent soft direction. Validate a resolvent or parametrix if available.
3. **Axis/characteristic reconstruction + Poisson fixed point.** Let `w(x)=V_1(x,0)`, `g(x)=rho_y(x,0)`, `h_axis(x)=partial_y V_2(x,0)`. Necessary axis identities for an exact profile include
   \[
   w'+h_{axis}=2c_l,\qquad w g'=(1-h_{axis})g,
   \]
   and, when `w(x_*)=0`, `g>0` on `(0,x_*]`, `g~x^2` at 0,
   \[
   \left(\frac wg\right)'=\frac{2c_l-1}{g},\qquad
   w(x)=-(2c_l-1)g(x)\int_x^{x_*}\frac{dt}{g(t)},
   \]
   \[
   \int_0^{x_*}\left(\frac1{g(x)}-\frac1{x^2}\right)dx=\frac1{x_*}.
   \]
   These are **necessary but not sufficient**: the axis data must come from the full-plane nonlocal inverse. Explore a fixed-field characteristic formula on the basin of `P` where justified, and solve a coupled axis-to-plane problem if that gives sharper stability.
4. **Validated numerical Newton–Kantorovich / radii polynomial.** Construct an actual approximate inverse/parametrix including finitely many modes plus controlled infinite-dimensional tail, interval-arithmetic bounds on all operators, nonlocal Green tails, nonlinear products, free `c_l`, symmetry normalization, and transport degeneracy. In spaces permitting derivative loss, a naive inverse theorem may be invalid; investigate tame scales, an a posteriori Nash–Moser argument, or a different formulation if necessary.
5. **Finite-domain core + validated exterior matching.** Correct the far-field coefficients analytically, treat `Theta_0,Theta_1,...` as unknowns satisfying asymptotic compatibility, solve the core with quantitative boundary influence, and prove that the canonical inverse and transport match throughout the infinite plane. No artificial Dirichlet/Neumann wall at a numerical cutoff.
6. **Rigorous geometric exclusions/local nonexistence.** If actual spectral/compatibility data imply a quantitative incompatibility that no correction in a given ball can remove, establish and state a genuine NO theorem for that ball. In particular, study whether any exact smooth `P_infty` profile can have `B_3=0`; but remember this is separate from existence of finite-regularity `P_2` solutions.
7. **Change of dependent variables.** The even/odd symmetry permits locally `rho=y f(x^2,y^2)` and `psi=xy phi(x^2,y^2)` for sufficiently smooth functions; under the additional center factorization `rho=x^2 y a(x^2,y^2)` near zero. The resulting PDE is a first-order scalar transport coupled to an elliptic operator equivalent, in radial-square coordinates, to a six-dimensional radial Laplacian. Re-derive transformations and their boundary/regularity hypotheses. Determine whether this gives useful weighted elliptic estimates or simply transfers the degeneracy.

Potential local center compatibility (for smooth center data) may be useful as a diagnostic. Write

\[
a=1+\delta x^2+\gamma y^2+\cdots,\qquad
\psi=cxy+\alpha_{psi}xy^3+\beta_{psi}x^3y+\cdots.
\]

Then the exact equations require

\[
\boxed{c=3c_l-1,\quad \alpha_{psi}+\beta_{psi}=-\tfrac13,\quad
\beta_{psi}=2(2c_l-1)\delta,\quad
(8c_l-2)\gamma=5\alpha_{psi}.}
\]

These are only necessary Taylor identities. Check differentiability assumptions before using them in a finite-regularity theorem.

---

## 5. What a *real* a posteriori proof must contain

Produce a candidate + a precise Banach formulation, **not** only a sequence of formal inequalities. Specify:

**(i) Exact nonlinear mapping and its domain.** Either eliminate `psi` with the canonical whole-plane inverse and define

\[
\mathcal F(\rho,c_l)
=(c_lX+U[\rho])\cdot\nabla\rho-\rho
\]

plus the scalar constraint `3c_l-1-psi[\rho]_{xy}(0)=0`, symmetry and center normalization; or eliminate `c_l` by its density functional and work on the normalized density submanifold. State all far-field coefficients and function-space conditions ensuring `\mathcal F` is well-defined and differentiable. Separate the numerical residual from the elliptic inverse error.

**(ii) A specific tail/asymptotic representation.** Explain what data are fixed or solved for at `r=infty` and what decays. Establish the effect of a perturbation in `rho` on the nonlocal strain at `0` and on the source point. If holding the leading `Theta_0` fixed excludes genuine neighboring solutions, say so; if varying it, include those unknowns and equations. Analyze whether near-resonance/soft `c_l` is a kernel, true family, or numerical ill-conditioning.

**(iii) Linear invertibility/solvability in this exact space.** Identify any characteristic boundary/selection conditions at origin `0`, source `P`, invariant axes, infinity, and separatrix; prove existence of a bounded right/left inverse or an appropriate alternative (Fredholm with solvability constraints, Lyapunov–Schmidt, Nash–Moser). Distinguish the estimate for `L_0` from that of full `L`, and treat the free `c_l` equation and neutral scales correctly.

**(iv) Validated forcing/error norm.** Certify `\|\mathcal F(\bar\rho,\bar c_l)\|_Y` and every derivative/far-field piece required by `Y`, not only pointwise residual at finitely many grid points. Use interval arithmetic or analytic sampling/derivative remainders if computation is involved. Near zeros of `N_f`, specify regularized limits. Include `P`, origin, axes, and `r->infty`. The displayed `6.03e-5` absolute interior residual and `1.897e-4` global sampled maximum are **not** automatically admissible `Y` norms.

**(v) Nonlinear remainder and a quantitative closing inequality.** For instance, if a legitimate bounded approximate inverse `A` for `D\mathcal F(\bar z)` has been built (with `z=(rho,c_l)` or the eliminated formulation), supply certified constants `Y,Z_0,Z_2` obeying an actual theorem of the form

\[
\|A\mathcal F(\bar z)\|\le Y,\qquad
\|I-A D\mathcal F(\bar z)\|\le Z_0,
\]

and a rigorously quantified quadratic or Lipschitz bound on the preconditioned derivative/remainder over a radius `r`. Show **numerically certified strict** inequalities for existence/uniqueness in the properly defined ball (e.g. `Y+Z_0 r+Z_2 r^2<r`, `Z_0+2Z_2r<1` if the precise hypotheses justify these expressions). **Do not manufacture these constants or apply this criterion where the operator loses derivatives.** A different honest theorem is equally acceptable.

**(vi) Actual scope of the conclusion.** State whether the solution is merely `P_2`, more regular, `P_infty`, unique in a ball or one element of a family, and whether it has the required far-field behavior. Do not infer smoothness from a norm that controls only two derivatives; conversely, if the trial has a fractional mode, consider whether an exact correction can remove it, rather than asserting the exact solution must inherit it. If quantitative error control enables a sign/nonzero conclusion about `B_3`, prove that the functional is continuous with an explicit bound in your chosen topology.

**(vii) Reproducible verification.** Separate analytic claims, floating-point exploratory evidence, and interval/certified results. An adversarial auditor should independently derive the linearization, normalizations, characteristic signs, Green representation, interpolation constants, and numerical enclosures, and search for counterexamples or unbounded sequences to each proposed norm inequality.

### Targeted priority tests (suggested, not rigid)

- **Test 1: data and residual provenance.** Locate numerical coefficient files/generator, confirm hashes where possible, and reproduce the ordinary sampled residual/center/source values with an independent evaluator. If artifacts are missing, track the blocker explicitly and continue analytical work and/or build an explicitly new candidate; do not claim the old X3 was verified.
- **Test 2: identify an honest Banach space.** Check far-field growth, corrections of `Theta_0,Theta_1`, center factorization, finite regularity and characteristic direction. Try to falsify proposed embeddings/inverse estimates with explicit high-frequency or large-radius test fields before using them.
- **Test 3: solve or sharply isolate the inverse problem.** Analyze near `0` and `P` and any transport resonance, the order-zero nonlocal coupling and scalar `c_l` feedback. Produce an explicit operator bound, valid parametrix, or a counterexample to the proposed bound. If one path fails, switch.
- **Test 4: certify residual *in the chosen norm*.** Address the far field and domains; if necessary improve/correct the exterior numerically rather than polishing only the interior normalized maximum.
- **Test 5: close a validated fixed point if possible.** If not, obtain the sharpest correct conditional criterion with every unknown constant named, an explicit unbounded/negative direction when a criterion fails, and a prioritized next experiment capable of deciding it.

---

## 6. Reporting and quality standards

Deliver a substantive final report with these sections:

1. **Verdict** `YES`, `NO`, or `UNRESOLVED`; a one-sentence *mathematical scope* of that verdict and a candid proof/evidence distinction.
2. Exact PDE, admissible class, canonical inverse, normalization, and how the original X3 candidate or any new approximation was acquired/reconstructed.
3. Accurate UTC start/end times, true elapsed wall-clock research interval, interruptions, meaningful session breakdown, and pointers to raw run/proof logs. **Never claim a runtime you cannot substantiate.**
4. Technical dependency chart: exact algebraic identities, conditional lemmas, certified inequalities, exploratory calculations, and false statements/counterexamples.
5. Strongest **linearized inverse theorem or obstruction**, with full hypotheses, actual norms, and quantitative constants or a clear explanation of why not established.
6. Residual tables **both absolute and normalized**, where measurable; and rigorous enclosures in the *new chosen error norm* if claimed. Include three or more distinct resolutions/physical domain extents as appropriate to any claim of numerical convergence; display locations of maxima including near P and infinity. Disclose axis evaluation floors and effects of far-field closure.
7. Fully explicit a posteriori theorem and verified closing inequality if YES; or full proof of exclusion and its precise neighborhood if NO.
8. Independent-verifier notes: what was actually rederived/recomputed, what objections were raised, which were resolved, and which remained open. Do not pass off a single implementation/run as independent confirmation.
9. Genuine reproducibility appendix: coefficient hashes, scripts, versioned code, commands, environment, interval arithmetic settings, sampled vs certified outputs, and paths to source files. If data unavailable, record the exact missing artifacts.
10. If UNRESOLVED, a **ranked, concrete** list of obstructions and the minimum next calculations or lemmas needed; explicitly separate *method-specific* failure from *nonexistence of the underlying exact profile*.

**Critical audit checklist:**

- Full plane, canonical law, even `x` and odd `y`; no hidden half-plane boundary condition or harmonic `lambda xy`.
- Old branch: `rho=x^2 y a`, `a(0)=1`, `c_l=(1+psi_xy(0))/3`. No substitution of the `y`-leading first-direction branch.
- `P_2` and `P_infty` are different claims; candidate X3 is explicitly finite-regularity and need not be a smooth exact solution.
- The report's `c_l` is not certified/uniquely determined; include its soft direction.
- Existing `Phi` matrix positivity fails, and existing global positive-`d` condition fails. Neither failure implies instability or nonexistence.
- Unweighted `dot H^{-1}` forcing with `G ~ r^k` or far residual `r^{2k-1}` is generically invalid; do not confuse normalized numerical error with forcing norm.
- The IPM nonlocal order-zero coupling is not automatically compact or arbitrarily small in top Hölder norm.
- Prove or rigorously enclose **global** far-field conditions, origin and source geometry, axis/characteristic compatibility, and exact scalar normalization.
- Only certify claims that actually follow from proven inequalities or verified enclosures; no hidden `O(1)` constants in a quantitative closure.
- **No early completion** without a fully decisive rigorous YES or rigorous NO. If still unresolved, continue honest research for 48 real hours and report `UNRESOLVED` without exaggeration.

**Begin now:** first rederive the exact nonlinear and linearized equations, recheck the two known local obstructions (`M_Phi(0)` and `d(P)`), identify/reconstruct the numerical candidate if files exist, and then choose whichever quantitative error-analysis route offers the best genuine chance of certifying an exact full-plane profile. Treat the old `Phi`-energy/`q`-Hölder analysis as an optional tool, not an imposed methodology.
