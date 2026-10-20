# Independent 48-hour research challenge: full-plane 2D inviscid Boussinesq self-similar profiles

**Standalone instruction.** This file supplies all essential mathematical context. Do not assume any earlier conversations, other prompts, private repositories, or precomputed profile files exist. The mathematical target is specified below. Verify all formulas and sign conventions independently before implementing a solver. The objective is a **definitive endpoint**: either a mathematically rigorous nonexistence result for the stated class, or exceptionally credible, independently reproduced numerical evidence for a nontrivial solution. Numerical evidence must NEVER be called an existence proof.

**Minimum duration and early-stop rule.** Conduct at least **48 hours of real elapsed active research** unless one of those two endpoints is attained *and independently audited earlier*. A preliminary numerical state, promising idea, local incompatibility, conditional theorem, failed method, or a negative result for a narrower subclass is NOT sufficient to end before 48 hours. Keep UTC start/end times, a contemporaneous work log, scripts, solver histories, and verifier findings. Do not count idle time outside active work as research and do not invent log entries or a 48-hour duration. If a real runtime or authorization constraint makes 48 hours impossible, disclose it rather than fabricating work. At the end of a genuinely completed 48-hour investigation, an honest `UNRESOLVED` is mandatory if neither endpoint has been achieved; it is not an acceptable *early* success.

## 1. Original PDE and self-similar reduction

Fix the following sign convention, irrespective of other conventions used in the literature:

\[
\partial_t\omega+u\cdot\nabla\omega=\partial_{z_1}\theta,\qquad
\partial_t\theta+u\cdot\nabla\theta=0,\qquad
u=(-\partial_{z_2}\psi,\partial_{z_1}\psi),\qquad
-\Delta_z\psi=\omega,\quad z\in\mathbb R^2.
\]

The sign of vorticity/stream function and, if necessary, the buoyancy force may differ in other references. Do not silently mix conventions: check physical consistency and translate papers carefully, including possible sign changes of temperature or vorticity.

For a candidate blow-up time \(T\), put \(\tau=T-t\), and take the exactly stationary, first-kind/power-law ansatz with unknown \(\beta>0\):

\[
X=\frac{z}{\tau^{\beta}},\qquad
\omega(t,z)=\tau^{-1}\Omega(X),\quad
\theta(t,z)=\tau^{\beta-2}\Theta(X),\quad
u(t,z)=\tau^{\beta-1}U(X),\quad
\psi(t,z)=\tau^{2\beta-1}\Psi(X).
\]

The stationary profile equations are

\[
\boxed{
\begin{aligned}
 &(\beta X+U)\cdot\nabla\Omega+\Omega=\partial_x\Theta,\\
 &(\beta X+U)\cdot\nabla\Theta=(\beta-2)\Theta,\\
 &-\Delta\Psi=\Omega,\qquad U=(-\Psi_y,\Psi_x).
\end{aligned}}
\tag{P}
\]

Throughout, \(X=(x,y)\in\mathbb R^2\). In the moving-center branch below the correct relative-field modification is explicitly specified; do NOT silently use (P) instead of its moving variant.

The unknown \(\beta\) is genuine, not a quantity that can be assigned an arbitrary value after the time exponents have been fixed. You may choose a mathematically equivalent normalization only if you display the transformation and retain any invariant exponent ratio as an unknown. Treat remaining spatial scaling and any background-velocity gauge explicitly; do not mistake a soft numerical direction for a symmetry.

### Full-plane elliptic inverse and admissibility

The Poisson inversion is on **all of \(\mathbb R^2\)**. There is no solid physical boundary. A calculation in a quadrant or half-plane is allowed only as a symmetry-reduced representation of the exact full-plane integral operator. Do not set an artificial Dirichlet condition at the edge of a numerical box and call it the physical problem.

Define a canonical Biot–Savart law, including its admissible tail class and treatment of the far field. For example, when integrals converge,

\[
\Psi(X)=-\frac1{2\pi}\int_{\mathbb R^2}\log|X-Y|\,\Omega(Y)\,dY,\qquad
U=(-\Psi_y,\Psi_x),
\]

with appropriate regularization, moment cancellation, subtractions, or a modal Green formula when this integral itself is not absolutely defined. The velocity, not the potentially divergent additive constant of \(\Psi\), is the physical quantity. No unadvertised affine straining field, harmonic correction, imposed exterior multipole, wall image, or free uniform velocity may be appended. A constant vertical velocity is a genuine gauge/observer-frame issue in the one-axis moving-center setting: state exactly what the chosen canonical inverse fixes.

**Choose and justify the far-field function class rather than borrowing one from IPM.** The broad research target is nontrivial full-plane smooth profiles with the stated local jet and parity, a canonical whole-plane velocity with sublinear growth \(U(X)=o(|X|)\), and polynomially controlled temperature/vorticity tails compatible with that velocity law. Do not define an artificially tiny admissible class just to obtain an easy NO: a theorem requiring extra assumptions must be honestly presented as a restricted-class theorem. Establish that the whole-plane inverse, the stationary equations, the numerical residuals, and any integrations by parts are well-defined in the chosen analytical subclasses. An admissible family can include unbounded far-field profiles, but identify its growth/decay assumptions and distinguish it from a profile producing bounded smooth physical initial data. Seek smooth classical profiles first; if you discover only finite-regularity or singular profiles, report them as separate endpoints with their precise regularity.

### Important invariant and blow-up checks

The exact transported temperature satisfies \(\|\theta(t)\|_\infty=\|\theta(0)\|_\infty\) whenever the classical full-plane flow is globally defined and the norm is finite. For the above ansatz, if \(0<\|\Theta\|_\infty<\infty\), this forces \(\beta=2\). If \(\beta\ne2\), a candidate exact global stationary profile with nonzero temperature cannot simultaneously produce a classical full-plane evolution with finite nonzero temperature \(L^\infty\) norm at each time. Make this distinction an explicit diagnostic, not an automatic exclusion of all unbounded-profile or local-asymptotic classes. Other conserved norms may impose further restrictions; derive their actual hypotheses.

For a sufficiently regular nonzero \(\Omega\) and \(\nabla\Theta\), the self-similar formulas formally give \(\omega\sim\tau^{-1}\) and \(\nabla_z\theta\sim\tau^{-2}\) at shrinking physical scales. These do not establish blow-up from bounded data if the profile already has infinite norm at infinity. Exact global stationary profiles, approximate profiles, nearly self-similar evolution, and physical finite-energy bounded-data blow-up are four distinct claims. Keep them separate.

## 2. Related background to examine independently

The impetus is the boundary-based work of Jiajie Chen and Thomas Y. Hou on 2D Boussinesq/3D Euler singularity formation:
- https://arxiv.org/abs/1910.00173 (\(C^{1,\alpha}\) velocity and boundary).
- https://arxiv.org/abs/2210.07191 (smooth-data analysis, weighted estimates).
- https://arxiv.org/abs/2305.05660 (rigorous numerics).

Those are **boundary** studies and do not establish a whole-plane exact stationary profile. Transfer their ideas only after rederiving the whole-plane kernel, transport geometry, and scaling. Also check modern exact self-similar/profile nonexistence literature, especially:
- Ken Abe, Daniel Ginsberg, In-Jee Jeong, *Stationary self-similar profiles for the two-dimensional inviscid Boussinesq equations*, https://arxiv.org/abs/2410.21765 (half-plane radially homogeneous classes; do not misapply its theorems to a different full-plane profile class).
- Luman Ju, *On the profiles of locally self-similar solutions for the 2D inviscid Boussinesq equations* (2020).
- Chae's papers on nonexistence of self-similar Boussinesq/Euler profiles under decay/integrability assumptions.

This is a starting bibliography, not an assertion that any listed theorem solves this setting. Retrieve the exact theorems and check all hypotheses. If an existing result rigorously decides the precise class of this prompt, an independently audited application can count as the NO endpoint.

## 3. Setting B2 — only \(x\)-reflection symmetry, moving material center

**Only this setting is your target. B1 (forcing the fixed origin to satisfy \(U(0)=0\)) is deliberately excluded from the main research program. Do NOT silently add \(y\)-reflection symmetry, an impermeable wall at \(y=0\), or a condition \(U_2(0)=0\).**

Require
\[
\Theta(-x,y)=\Theta(x,y),\qquad
\Omega(-x,y)=-\Omega(x,y),\qquad
\Psi(-x,y)=-\Psi(x,y),
\]
with no parity condition in \(y\). Thus \(U_1(0,y)=0\), but \(U_2(0,y)\) need not vanish. The \(x=0\) axis is invariant and contains a moving material center; the horizontal line \(y=0\) is **not** a physical or reflective boundary and may be crossed by the flow.

Assume an \(x^2\)-leading, nontrivial, smooth temperature in coordinates centered on the moving material point:
\[
\boxed{\Theta(x,y)=a_0x^2+\text{terms of order at least three},\qquad a_0\ne0.}
\]
To preserve the \(x^2\) structure along the invariant axis, impose \(\Theta(0,y)=0\), or prove an equivalent global structure; smooth evenness then permits \(\Theta=x^2F(x^2,y)\). The vorticity is odd in \(x\) and can be written locally \(\Omega=xG(x^2,y)\). In contrast to the fourfold settings, odd powers of \(y\) in \(F,G\) are allowed.

### Derive the moving center correctly, including the nonzero velocity at its center

Let the physical material center be \(z_c(t)=(0,z_{c,2}(t))\), evolving by \(z_c'(t)=u(t,z_c(t))\). Write
\[
\tau=T-t,\qquad X=\frac{z-z_c(t)}{\tau^\beta},
\]
\[
\omega=\tau^{-1}\Omega(X),\quad
\theta=\tau^{\beta-2}\Theta(X),\quad
u=\tau^{\beta-1}U(X),\quad
\psi=\tau^{2\beta-1}\Psi(X).
\]
With \(v_0=U(0)=(0,U_2(0))\) defined by the **canonical full-plane inverse** of \(\Omega\), one has
\[
 z_c'(t)=\tau^{\beta-1}v_0,\qquad
 z_c(t)=z_*-\frac{v_0}{\beta}\tau^\beta\quad(\beta>0).
\]
The correct stationary moving-center system is
\[
\boxed{
\begin{aligned}
 &W\cdot\nabla\Omega+\Omega=\Theta_x,\\
 &W\cdot\nabla\Theta=(\beta-2)\Theta,\\
 &W=\beta X+U(X)-U(0),\\
 &-\Delta\Psi=\Omega,\quad U=(-\Psi_y,\Psi_x).
\end{aligned}}
\tag{B2-P}
\]
Crucial: the term \(-U(0)\) is not optional and cannot be replaced by an arbitrary fitted drift independent of the physical velocity. Re-derive this exact relation and check the reconstruction in physical variables. The blow-up limiting point \(z_*\) is fixed in physical space, but the marked material center need not remain stationary before \(T\). Also investigate the coordinate/translation equivalence between a moving similarity center and a shifted fixed limiting center, carefully distinguishing coordinate freedom from the physical condition \(U(0)=0\).

### Local necessary conditions

Let \(c=\Psi_{xy}(0)\). Since \(U(0)\) has been subtracted, \(W(0)=0\); parity gives
\[
DW(0)=\begin{pmatrix}\beta-c&0\\0&\beta+c\end{pmatrix}.
\]
The temperature jet \(\Theta\sim a_0x^2\) forces
\[
2(\beta-c)=\beta-2,\qquad
\boxed{c=1+\frac\beta2}.
\]
If \(\Omega(x,y)=b_0x+\cdots\), the vorticity equation gives
\[
(\beta-c+1)b_0=2a_0,\qquad
\boxed{b_0=\frac{4a_0}{\beta}}.
\]
The full-plane Biot–Savart integral must reproduce **both** \(c\) and \(v_0\); local coefficient matching is insufficient. In particular, for a sufficiently integrable, nonzero \(\Omega\ge0\) in \(x>0\),
\[
U_2(0)=\frac1\pi\int_{x>0}\frac{x\,\Omega(x,y)}{x^2+y^2}\,dxdy>0.
\]
This sign observation rules out a stationary material center with \(U(0)=0\) for that sign subclass (B1), but **does not rule out B2**. If \(\Omega\) changes sign, the sign restriction need not hold. Check all integral hypotheses rather than relying on this as a universal theorem.

### Exact reduced equations (optional numerical representation)

Let \(s=x^2\) and write
\[
\Theta=x^2F(s,y),\quad \Omega=xG(s,y),\quad\Psi=xH(s,y).
\]
Then
\[
U_1=-xH_y,\qquad U_2=H+2sH_s,\qquad v_0=(0,H(0,0)),
\]
\[
 A=\beta-H_y,\qquad B=\beta y+H+2sH_s-H(0,0),
\qquad W=(xA,B).
\]
The stationary equations are
\[
\boxed{
\begin{aligned}
 2A(F+sF_s)+BF_y&=(\beta-2)F,\\
 A(G+2sG_s)+BG_y+G&=2(F+sF_s),\\
 4sH_{ss}+6H_s+H_{yy}&=-G.
\end{aligned}}
\tag{B2-red}
\]
At the center \((s,y)=(0,0)\):
\[
F(0,0)=a_0\ne0,\qquad H_y(0,0)=1+\beta/2,\qquad G(0,0)=4a_0/\beta.
\]
There is no condition \(H(0,0)=0\); indeed \(H(0,0)=U_2(0)\) generally is nonzero, and it is subtracted from the moving transport field. Verify these identities independently and carefully distinguish \(H\), a coefficient of \(\Psi\), from an arbitrary harmonic part of \(\Psi\).

### Specific analytic and computational questions

- Does there exist a smooth whole-plane moving-center stationary B2 profile with \(a_0\ne0\) and \(\beta>0\)? If not, seek a rigorous global exclusion. A proof excluding only \(U_2(0)=0\) or positive-vorticity fixed-center B1 is **irrelevant as a full NO for B2**.
- Can one preserve Chen–Hou's x-symmetric positive-vorticity temperature-production mechanism *without* the original impermeable boundary? Investigate axis transport, center drift, and the resulting nonlocal kernel, rather than importing half-plane estimates verbatim.
- Do not impose any boundary conditions at \(y=0\), and never compute \(\Psi\) by an upper-half-plane Dirichlet inverse. Independently check the nonzero center drift and its convergence under box/refinement changes.
- Examine the \(\beta=2\) bounded-temperature compatibility, other far-field tail classes, and whether a claimed profile could correspond to finite smooth data rather than an already unbounded field.
- Under the remaining exact spatial scaling \(\Theta_\lambda=\lambda\Theta(X/\lambda)\), \(\Omega_\lambda=\Omega(X/\lambda)\), \(U_\lambda=\lambda U(X/\lambda)\), one has \(a_0\mapsto a_0/\lambda\), \(v_0\mapsto\lambda v_0\), and unchanged \(\beta\). Study and, if useful, fix its gauge without incorrectly forcing \(U(0)=0\) or excluding other branches.


## 4. Research protocol: prove NO or find a verified numerical YES

**Do analysis and numerical investigation in parallel, with a genuinely independent verifier.** Start by checking all local Taylor identities, exact transport constraints on invariant axes, center conditions, full-plane Biot–Savart signs and normalization freedoms. Search systematically for a *global* nonexistence theorem in the exact class; a theorem requiring stronger positivity, analyticity, finite energy, finite temperature sup norm, or a restricted \(\beta\)-range only excludes that subclass and cannot be advertised as NO for the unrestricted class.

If NO is not established, implement a high-resolution self-similar profile search for \(\Theta,\Omega\) and unknown \(\beta\), using a smooth, parity-compatible representation. Do not hard-code non-integer-power singular terms or a preferred exponent based on an earlier unsuccessful fit. Do not force the solution to have a fixed sign unless studying and labeling a separate sign-restricted subproblem; allowing sign changes may be indispensable. Exclude the trivial \(\Theta=\Omega=0\) and pure harmonic/affine-gauge artifacts. Check the genuine spatial scaling freedom; fix it by a justified method **only if necessary**, while ensuring that no admissible branch is silently excluded.

A competent program should try substantially different initial guesses, at least two mathematically different representations/solvers where possible, and separate runs with free \(\beta\) and several fixed values. A single optimization lineage is not independent evidence for uniqueness or for a determined exponent. Check whether the Jacobian has neutral scaling directions, weak exponent directions, near-zero singular values, or hidden compatibility conditions; perform continuation and refined reoptimization rather than interpreting a small residual as convergence to an exact solution.

### Residuals and independent verification

Set \(W=\beta X+U\) (or the explicitly modified moving-center field). The **unscaled Cartesian residuals** are

\[
R_\Omega=W\cdot\nabla\Omega+\Omega-\Theta_x,\qquad
R_\Theta=W\cdot\nabla\Theta-(\beta-2)\Theta,\qquad
E=-\Delta\Psi-\Omega.
\]

Define and report both absolute maxima and *pointwise* normalized maxima, e.g.

\[
\begin{aligned}
N_\Omega&=|W_1\Omega_x|+|W_2\Omega_y|+|\Omega|+|\Theta_x|,\\
N_\Theta&=|W_1\Theta_x|+|W_2\Theta_y|+|\beta-2|\,|\Theta|.
\end{aligned}
\]

For each ratio \(|R|/N\), disclose how zeros and floating-point underflow of \(N\) are handled; never use a large artificial floor to hide a defect near a symmetry axis or a stagnation point. If the PDE is divided by \(x\), \(y\), \(xy\), or \(x^2\) to remove parity factors, independently evaluate the **desingularized residual** and its axis limit, not only the original residual that vanishes automatically with the prefactor. Include elliptic inversion error separately; a Poisson solve by construction is not an exact numerical certification of \(E=0\).

As a concrete target for **strong numerical existence evidence**, seek maxima on independently generated between-node evaluation points in both normalizations near \(10^{-6}\) or smaller, with matching convergence in desingularized residuals, and quantify the absolute residual in each region. A different threshold is acceptable only with a compelling, independently audited conditioning/error-budget argument. No single absolute or normalized threshold, by itself, proves an exact solution or even the existence of a nearby solution.

Minimum verification programme (unless an equally strong independent replacement is justified):
1. At least **three angular/spatial resolutions** and **three independent fit/inverse domains**, including the physical origin, each symmetry axis, any other stagnation points/separatrices, and the far field. Distinguish improvement due to longer optimization from improvement due to resolution using equal-budget comparisons.
2. A **separately implemented** residual generator and Poisson/Biot–Savart evaluator, not just a second call to the fitting code. Where feasible, verify the velocity at sampled points using a different physical-space quadrature or Fourier/Green representation. Include rigorous interval bounds if attainable, but otherwise describe sampling errors honestly.
3. Measure \(\beta\), local Taylor compatibility coefficients, stagnation-point locations/derivatives, nontrivial amplitudes, residual maxima by region, objective values, numerical gradients and any near-kernel directions, and show that the claimed facts are stable under refinement. Give the coefficients/files needed to regenerate the candidate; not just plots or screenshots.
4. Derive or fit the **far-field leading and next-order asymptotics** from the PDE, compare them with the numerical profile, and measure the error caused by closing an inverse on a finite box. A boundary-imposed or artificially continued profile is not a full-plane solution until the true canonical inverse and far-field residual are checked.
5. Audit the exact physical time-dependent reconstruction, parity, local smoothness on both axes and at the center, conservation laws and genuine distinction between an unbounded-data exact self-similar solution and a finite-energy smooth-data blow-up construction.

### YES and NO success criteria

- **YES (reliable numerical existence evidence):** supply an explicit nontrivial candidate in the **stated setting**, with independently reproduced and resolution/domain-stable small Cartesian and desingularized residuals; a properly determined or explicitly weakly determined \(\beta\); correctly normalized gauge/scaling; an independently audited full-plane velocity; far-field and stagnation-point checks; complete reproducible coefficient/source files and error tables. Call it **numerical evidence only** unless you also prove a rigorous a posteriori existence theorem.
- **NO (mathematical exclusion):** give a complete, independently audited theorem excluding **every profile in the stated admissible setting**, with all regularity, nontriviality, far-field and parameter assumptions clearly stated. If only the positive-vorticity, bounded-temperature, fixed-exponent, finite-energy, or analytic subclass is excluded, label this a **partial** theorem and continue; it is not a NO endpoint for a broader class. A failed least-squares fit, apparent residual floor, singular Jacobian or coarse-grid instability is NEVER proof of nonexistence.
- **UNRESOLVED after at least 48 genuine hours:** report the best defensible numerical states, all actual proofs (with their precise restricted scopes), the most serious remaining obstacles, what strategies were decisively ruled out, and the reproducible artifacts. State explicitly that neither accepted endpoint has been reached.

### Independence and time accounting

Use at least a researcher/solver and an adversarial verifier. The verifier independently derives the equations and local constraints, writes residual/inverse tests, challenges normalization/gauges and far-field closure, and rejects inflated claims. If available, a separate analytic referee should critique every nonexistence proof and every inference from numerics to existence. The independent reviewer must not simply inspect the solver's own reported loss.

Maintain a durable UTC timeline and source-control/log record of every significant attempt; document machine/software versions, compute budgets, failures, and restart inputs. Allocate the requested 48-hour horizon to actual mathematical work; if the numerical approach stalls, try analytically distinct methods instead of looping identical solver settings. Do not switch to a different setting or weaken the target silently. Stop before 48 hours **only** on an audited full YES or NO under the preceding standards. No fabricated duration, invented verification, unreported assumption, or fake coefficient file.

## 5. Final deliverable format

Begin with exactly one headline: `YES — independently validated numerical evidence`, `NO — rigorous nonexistence theorem`, or `UNRESOLVED — 48h investigation completed`. Immediately state the exact solution class to which that headline applies. Supply a complete mathematical problem statement; identities and proofs with assumptions; independent residual tables (including **absolute** errors), domain and basis studies, far-field/inverse uncertainties, and files/scripts for reproduction; a clear list of all restrictions and limitations; and real UTC start/end times. If the work supports a stronger exact existence theorem, state it separately with its complete proof, not by relabeling numerical evidence.
