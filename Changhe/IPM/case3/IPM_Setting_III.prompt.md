# Independent 48-Hour Research Task — Full-Plane IPM, Nondegenerate Axis Branch, and Unresolved Scaling Freedom

## Mandatory research duration and outcome

Work independently on the mathematical and computational problem specified below. **Do not stop before 48 hours of genuine elapsed research time unless you have already reached one of the two decisive endpoints defined below.** In particular, resolving a gauge ambiguity, finding a plausible normalization, proving a conditional lemma, or obtaining a promising intermediate fit is NOT an early-stop endpoint. An early termination must be justified by the full endpoint evidence, not by promising intermediate calculations or a tentative obstruction. Record real UTC start/end times, substantive activities, code/test artifacts, and any interruptions. Do not fabricate elapsed time, runs, referees, or verification.

The two acceptable decisive endpoints are:

- **NO — Rigorous nonexistence:** a complete, independently checked mathematical proof excluding **all** nondegenerate first-order profiles in the precisely stated admissible class, without extra unadvertised sign, monotonicity, topology, or analyticity assumptions. A result for only a narrower class is not NO for the principal problem.
- **YES — Strong reproducible numerical existence evidence:** an explicit, genuinely nondegenerate candidate together with the stringent independent validation in the section *Numerical evidence standard*. YES is **numerical evidence, not a theorem of existence**. Explicitly distinguish it from a computer-assisted existence proof. Do not report YES merely because an optimizer produces a small training-grid loss.

If neither endpoint is reached within 48 hours, do not fabricate YES or NO. Report **UNRESOLVED** with the strongest verified theorems, best numerical evidence, precise obstructions, failed approaches, code and reproducibility artifacts. Continue while productive if practical. Do not treat the 48-hour requirement as permission to stop early with a partial result.

Use separate **researcher** and **independent verifier/adversarial auditor** roles or independent implementations whenever possible. The verifier must check the defining PDE, inverse operator, gauge, symmetry, origin relations, far-field behavior, residuals and claims, rather than trusting the researcher's summaries.

## 1. Objective and what has changed

Explore the **full-plane**, unforced two-dimensional incompressible porous media (IPM) self-similar profile problem under even-in-\(x\), odd-in-\(y\) symmetry, but **remove the previously imposed condition \(\rho=x^2 y\,a\)** and especially do not impose \(\rho(0,y)\equiv0\).

The primary new branch is **genuinely nondegenerate at the origin**:
\[
\partial_y\rho(0,0)\neq0.
\]
Locally, smoothness and symmetry then allow
\[
\rho(x,y)=y\,a(x^2,y^2),\qquad a(0,0)\neq0.
\]
Here \(a\) must be an unknown, not a prescribed function, and \(a(0,0)\) must **not** simply be set equal to 1 unless an actual symmetry of the normalized coupled PDE allowing that normalization is proved. It is sufficient to report its computed nonzero value and numerical stability.

Also explore, as a clearly labeled *secondary* branch, profiles without an \(x^2\) factor for which \(\rho_y(0,0)=0\) but \(\rho(0,y)\not\equiv0\) (for example, a possible \(y^3\)-leading branch). Do not substitute success or failure on this secondary branch for a conclusion about the primary \(y\)-leading branch.

**Do not rediscover the previously studied \(x^2 y\) branch and count that as success.** The distinction is substantive: the original \(x^2y\) ansatz imposes an invariant zero-density line and a saddle at the origin for the rescaled field; the \(y\)-leading branch has different normalization and characteristic geometry.

## 2. Complete PDE and symmetry setting

Find a real parameter \(c_l>1\), a density \(\rho\not\equiv0\) on \(\mathbb R^2\), stream function \(\psi\), and velocity \(U\) such that
\[
\boxed{\begin{aligned}
&(c_l X+U)\cdot\nabla\rho=\rho,\qquad X=(x,y)\in\mathbb R^2,\\
&U=(-\partial_y\psi,\partial_x\psi),\\
&-\Delta\psi=\partial_x\rho.
\end{aligned}}
\]
Impose
\[
\rho(-x,y)=\rho(x,y),\qquad \rho(x,-y)=-\rho(x,y),
\]
with \(\psi\) odd in both \(x\) and \(y\), and impose the **canonical full-plane velocity law**: divergence-free \(U\), curl \(U=-\partial_x\rho\), these parities, and \(U(X)=o(|X|)\) at spatial infinity. This rules out an arbitrary harmonic \(\lambda xy\) contribution to \(\psi\), which would change the strain and the scaling parameter. State explicitly how the canonical inverse is evaluated and prove or numerically validate that it has the required convergence and gauge.

Primary admissible class: \(\rho\in C^\infty_{\mathrm{loc}}(\mathbb R^2)\) with the above symmetries, \(\rho_y(0)\neq0\), and for some \(0<\gamma<1\),
\[
|\rho(X)|+(1+|X|)|\nabla\rho(X)|\le C(1+|X|)^\gamma.
\]
Any explicit weaker \(C^{m,\alpha}_{\mathrm{loc}}\) or finite-regularity variant must be defined and assessed **separately**. Evidence for such a weaker variant cannot silently be labeled as existence evidence for the smooth class. Check higher derivative regularity at the origin, on the symmetry axes, and across any characteristic separatrix.

No physical boundary is present; the domain is all of \(\mathbb R^2\). The axis \(y=0\) is a symmetry line, **not** a wall with an independently imposed boundary condition. There is no imposed \(x^2\) vanishing. The trivial/affine profile \(\rho=A y,\ U=0,\ c_l=1\) is excluded by \(c_l>1\) and sublinear density growth; do not present it as a blowup profile.

## 3. Exact origin identities — essential safeguards

Set \(c=\psi_{xy}(0,0)\). Symmetry implies
\[
DU(0)=\operatorname{diag}(-c,c),\qquad
D(c_lX+U)(0)=\operatorname{diag}(c_l-c,c_l+c).
\]
If \(\rho_y(0,0)\neq0\), differentiating the profile equation at the origin gives the **new normalization**
\[
\boxed{c_l+c=1},\qquad
\boxed{c=1-c_l}.
\]
Consequently
\[
\boxed{D(c_lX+U)(0)=\operatorname{diag}(2c_l-1,1).}
\]
For \(c_l>1\), the origin is a **source** of the rescaled characteristic flow, not a saddle. This is fundamentally different from the old \(x^2y\) normalization \(3c_l-c=1\), whose numerical branch gave \(c_l\simeq5.575\) and a saddle. **Never use \(3c_l-c=1\) for the present primary branch.** Compute \(c\) independently from the canonical velocity generated by the candidate and verify \(c_l+\psi_{xy}(0)=1\), without enforcing it as a tautology in both the generator and the evaluator.

The coefficient \(a_0:=\rho_y(0,0)\) is a genuine datum of the \(c_\rho=1\) normalized equation, not something that can be set to 1 by its remaining spatial scaling. This point is essential to the new research task and is expanded immediately below.

A technical trap: the old absolutely convergent integral formula for \(\psi_{xy}(0)\), developed with \(\rho=O(|X|^3)\), need not be absolutely convergent when \(\rho\sim a_0 y\). Use the correct angular-mode or cancellation-renormalized evaluation of the strain, and cross-check against differentiated stream functions and direct velocity quadrature. Do not treat a conditionally convergent integrand as absolutely integrable.

Derive and independently verify any additional center Taylor compatibility relations in the new branch; do not transplant the earlier \(x^2y\) center conditions or the old \(B_3\) / \(C^6\) regularity obstruction without rederivation.

## 3A. Essential open issue: remaining normalization freedom (investigate independently; do not assume a gauge)

There is an important, **still-unresolved research-design issue**: after normalizing the coefficient of \(\rho\) on the right-hand side to 1, the stationary equation still possesses one continuous, genuine **spatial scaling symmetry**. You must investigate and account for it before interpreting numerical uniqueness, parameter accuracy, solver conditioning, and convergence.

For the *general* profile equation
\[
(c_lX+U[\rho])\cdot\nabla\rho=c_\rho\rho,
\qquad -\Delta\psi=\partial_x\rho,
\]
the two-parameter transformation
\[
\begin{aligned}
\rho_{A,B}(X)&=A\rho(BX),\\
\psi_{A,B}(X)&=\frac{A}{B}\psi(BX),\\
U_{A,B}(X)&=A U(BX),\\
c_{l,A,B}&=AB\,c_l,\\
c_{\rho,A,B}&=AB\,c_\rho,
\end{aligned}
\qquad A,B>0,
\]
leaves the *form* of the system unchanged. Hence \(c_l/c_\rho\) and \(\rho_y(0)/c_\rho\) are invariant. In our required convention \(c_\rho=1\), only \(AB=1\) remains, equivalently
\[
\boxed{
\rho_\lambda(X)=\lambda\rho(X/\lambda),\quad
\psi_\lambda(X)=\lambda^2\psi(X/\lambda),\quad
U_\lambda(X)=\lambda U(X/\lambda),\quad
c_{l,\lambda}=c_l,
}\qquad\lambda>0.
\]
Crucially,
\[
\boxed{\partial_y\rho_\lambda(0)=\partial_y\rho(0)=a_0.}
\]
So **neither \(c_l\) nor \(a_0\) can be arbitrarily fixed by this residual symmetry**. Also, the additive constant in \(\psi\) is physically irrelevant, while a free harmonic strain \(\kappa xy\) is **not** an allowed gauge because it changes \(U\) and is excluded by the canonical full-plane velocity law. The symmetry center is fixed at the origin.

**Your independent task concerning this freedom:** determine rigorously whether there are any additional genuine transformations, which parameters are invariant, what (if anything) should be normalized, and whether the remaining scale can be handled without incorrectly removing solutions. Investigate the implications for analysis, numerical continuation, conditioning, reproducibility and comparison of different solutions. **No particular scale-fixing condition or algorithm is being prescribed. Develop and justify your own treatment**, or explicitly leave this issue open if none can be justified. In particular:

- Do **not** set \(a_0=1\), choose a numerical value of \(c_l\), or impose any additional shape/derivative/point-value condition and declare it *without loss of generality* without a proof that the relevant condition is attainable for **every** solution in the stated class (or an explicit restriction to a separately named subclass).
- Do **not** confuse a genuine gauge orbit with a family of distinct solutions having different invariant parameters; do **not** interpret the drift of a numerical optimizer along a gauge direction as evidence that \(c_l\) or \(a_0\) is undetermined by the equation.
- If you adopt any normalization or quotient construction, derive how all unknown fields, derivatives, far-field coefficients and norms transform, and check that the full PDE, canonical inverse and admissible class are preserved.
- If there are exceptional profiles for which a proposed normalization cannot be applied, state that explicitly and **do not discard them silently**.
- Report whether your endpoint evidence (YES/NO/UNRESOLVED) is robust under the genuine scaling symmetry. The research endpoint is existence or nonexistence of a **profile**, not an arbitrary choice of its representative.

**Important:** The mathematical statements above explain the known symmetry and the obstacle; they are **not** a recommendation for how to remove it. Decide the correct course independently. Do not request a suggested gauge or reuse a gauge from the older \(x^2y\) numerical study without deriving it here.

## 4. Why an exact profile would imply physical IPM gradient blowup

For an exact profile with \(c_l>1\), put
\[
\alpha=\frac1{c_l-1},\qquad \beta=\frac{c_l}{c_l-1},\qquad X=Z/(T-t)^\beta.
\]
Then
\[
\varrho(t,Z)=\alpha(T-t)^\alpha\rho(X),\quad
u(t,Z)=\alpha(T-t)^\alpha U(X),\quad
\Psi(t,Z)=\alpha(T-t)^{\alpha+\beta}\psi(X)
\]
solve physical IPM \(\partial_t\varrho+u\cdot\nabla\varrho=0\), \(-\Delta\Psi=\partial_{z_1}\varrho\). In particular,
\[
\partial_{z_2}\varrho(t,0)=\frac{\alpha\rho_y(0)}{T-t}\neq0,
\]
which blows up as \(t\uparrow T\). Correct the notational typo \(\nu\to u\) in any report. Explain that the imposed sublinear-growth class generally allows density unbounded at spatial infinity: even a proved exact profile need **not** provide blowup from globally bounded or compactly supported initial density. Do not claim that stronger result without an additional localization/stability argument.

## 5. Analytical research program (not limited to these approaches)

**A. Establish necessary conditions, and attempt a rigorous NO theorem.**
Analyze the canonical strain identity and its sign; investigate whether positivity/sign of \(\rho_y(0)\), symmetries, far-field growth, and \(c_l>1\) can coexist with \(c=1-c_l<0\). Never assume global positivity, monotonicity, a finite critical-point set, or the absence of internal equilibria without proof. Study the origin source flow, invariant axes, global characteristics, and whether characteristic reconstruction plus sublinear growth imposes a contradiction. Check the integral identities and potential far-field asymptotics. A genuine NO must exclude the full primary class; conditional exclusions must be separately labeled.

**B. Construct a credible smooth profile numerically.**
Use representations that explicitly allow \(\rho_y(0)\neq0\) and \(\rho(0,y)\neq0\): for example, \(\rho=y\,a(x^2,y^2)\) near zero, coupled to a smooth global radial-angular or compactified representation. Do not multiply by \(x^2\), force \(a(0)=0\), or impose old saddle/source-point conditions. Do not bake in fractional-power singularities and infer the resulting regularity from the ansatz. Treat \(c_l\), \(\rho_y(0)\), spatial scales, far-field angular profile and its corrections as coupled unknowns. Independently investigate the residual scaling ambiguity as specified in Section 3A; do not assume a particular resolution. Derive the leading far-field compatibility from the PDE rather than assuming fitted continuation is valid. One plausible asymptotic is \(\rho(r,\theta)\sim r^{1/c_l}\Theta_0(\theta)\); derive and check this, and solve for higher-order corrections when needed.

**C. Independent numerical methodology.**
Implement a first solver and a genuinely separately written generator/Poisson inverse/residual evaluator. Seek a second discretization (e.g., Cartesian/spectral versus polar/compactified) not sharing the first solver's differentiation and closure. Compare exact manufactured fields. Test possible near-axis cancellation and the full-plane harmonic gauge. Quantify how residuals change when the far-field domain or asymptotic closure changes. Evaluate between fitting nodes at substantially higher resolution. Check all axes and all neighborhoods of equilibria, and include characteristic-integrated residual tests when useful.

**D. Why previous partial analyses might fail or help.**
Previous work on the \(x^2y\) branch found an indefinite \(\Phi\)-energy matrix and a negative transport coefficient at a *different* source point \(P=(x_*,0)\). These values are tied to the old origin normalization and geometry. Recompute them from scratch for the \(y\)-leading source geometry; do not assume they apply unchanged. Explore weighted/anisotropic characteristic estimates, nonlocal coupling, and linearized invertibility. You do not need to prove a complete a posteriori theorem to reach the defined numerical YES endpoint, but distinguish evidence from proof.

## 6. Numerical evidence standard for YES

Declare **YES (strong numerical evidence)** only if all of the following are addressed convincingly:

1. Give an **explicit reconstructible candidate** (source/coefficients and all parameters) on the whole plane, with \(c_l>1\), proven-by-formula even-\(x\)/odd-\(y\) parities, no forced \(x^2\), and a measured nonzero \(\rho_y(0)\) that is well resolved and robust across independent evaluations. State the smoothness the candidate itself actually has; spline basis regularity is not proof of \(C^\infty\).
2. Use the canonical law to compute \(U\) from \(\rho\); do **not** independently optimize arbitrary velocity or harmonic strain. Check \(c_l+\psi_{xy}(0)=1\) to substantially better accuracy than the residual target, including at least one independent check that does not merely reuse the origin constraint.
3. Define the **un-normalized transport residual** \(R=(c_lX+U)\cdot\nabla\rho-\rho\), and report its sampled absolute maxima by regions and locations, together with at least two pointwise normalized maxima:
   \[
   N_f=|(c_lx+U_1)\rho_x|+|(c_ly+U_2)\rho_y|+|\rho|,
   \qquad N_v=|\rho|+|X\cdot\nabla\rho|+|U\cdot\nabla\rho|.
   \]
   Give \(\max |R|/N_f\) and \(\max |R|/N_v\) **on independent between-node grids**, with principled treatment near zeros of denominators, axes, and equilibria. Aim for worst-case normalized residuals around \(10^{-6}\) or below over the verified range, or convincingly justify an alternative quantitatively credible standard. A small training loss alone is insufficient.
4. Evaluate at **at least three independent resolutions and three substantially different physical domain extents**, and show systematic refinement of the true full-plane residual, rather than merely of a closed finite-box problem. Disentangle finite-basis error, optimizer budget, inverse error and far-field truncation; provide fair equal-budget tests for changed discretizations.
5. Compute the far-field residual and asymptotic matching errors under the true canonical inverse well beyond the fitting region. Test changes to exterior closure and avoid an invented boundary condition or hidden homogeneous velocity component.
6. Check \(\rho_y(0)\), \(c_l\), origin Taylor identities, flow Jacobian, all apparent critical points, parity and regularity for numerical convergence. **Explicitly separate known symmetry-generated soft directions from other weakly constrained directions**, rather than treating them as identical. Report parameter uncertainty **as observed numerical sensitivity, not a rigorously enclosed value**; do not quote unjustified digits.
7. Have an independent verifier recompute headline residuals and essential constraints with independent code; conduct adversarial checks for spurious polynomial states, trivial \(c_l=1\) solutions, solution-lineage bias, an old \(x^2y\) branch accidentally reintroduced by parameterization, spurious cancellations on axes, and a far-field/gauge artifact.
8. Provide the reproducible coefficient files, generator, evaluation code, run commands, parameter files and logs with a concise roadmap. If some artifacts cannot be supplied, state exactly which are missing and why the evidence standard remains justified (or does not).

No finite sampled-grid error automatically certifies a uniform global residual bound or an exact nearby solution. Be precise in all conclusions.

## 7. Rigorous NO standard

For NO, provide an explicit theorem with all assumptions and a self-contained proof. Identify the exact step which contradicts \(\rho_y(0)\neq0\), \(c_l>1\), canonical inverse, smoothness, symmetries or sublinear growth. Independently audit signs, convergence, characteristic limits, integration by parts, harmonic ambiguity and any use of maximum principles. Do **not** claim full nonexistence if the argument requires a sign-definite density or extra geometric hypothesis not included in the principal class. A theorem for such a narrower class is valuable partial progress but not the primary NO endpoint.

## 8. Deliverable and work discipline

Write the final research report in English with:

1. Verdict **YES / NO / UNRESOLVED** and exact scope (smooth primary class versus any weaker/secondary branch).
2. Complete PDE, canonical gauge, symmetry, growth, origin condition and scaling; no dependence on earlier prompts or repositories.
3. Main analytical findings, proof details and independent objections/rebuttals.
4. Reproducible numerical candidate and all residual tables if a candidate was attempted, including **absolute residuals** and pointwise normalization denominators.
5. Explicit checks of whether \(\rho_y(0)\neq0\) truly holds, whether the observed \(c_l\) is determined, and a stand-alone audit of the extra scaling freedom, including any independently justified gauge treatment and exceptions.
6. Precise account of what prevents a rigorous existence or nonexistence proof if unresolved.
7. The most important next mathematical/computational steps, prioritized by probability of deciding the question.
8. Genuine UTC timeline, elapsed research hours and substantiated verification record. If stopping before 48 hours, state the exact decisive endpoint that justified it.

Avoid status inflation: a solver failure is not a nonexistence theorem; a small normalized residual is not a rigorous existence proof; a finite-regularity candidate is not a smooth solution; and a profile from the previous \(x^2y\) class is not a solution of the new nondegenerate branch.

**Start by independently rederiving the origin relation, the symmetry/scaling structure, and the canonical inverse for a \(y\)-leading profile. Choose your own mathematically defensible response to the extra freedom; none is prescribed here. Then pursue rigorous exclusion and numerical construction in parallel, assigning a separate skeptical verifier to challenge both. Do not terminate early absent a genuinely decisive result.**
