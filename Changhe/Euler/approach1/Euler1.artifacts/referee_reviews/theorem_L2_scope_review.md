**Conditional verdict: L2 covers the entire primary exact-profile target, but it does not exclude every secondary result that the task explicitly asks to preserve.** In particular, it does not decide the \(c_l=1/2\) calibration or candidates with \(c_l>1/2\). The distinction matters when interpreting the phrase “the whole explicitly specified search class” in the stopping clause.

I read [PROMPT.md](../Euler1.prompt.md) in full, including all the sections specified in the question, and [THEORY_NOTES.md, sections 7–8](THEORY_NOTES.md:208). References below to “Task” and “Theory” mean these files. I take L2 as given, as instructed; this report checks its scope and the stated consequence for approximate solutions, and does not certify the separately audited proof of L2.

A final reread found intervening edits within Theory §7's proof. The theorem statement, §7.8, and §8 relevant to this scope audit were unchanged; the corrections below address their quoted wording. I have edited neither input file.

The requested Claude Opus 5.5 collaboration was unavailable. I attempted the permitted Python/Bedrock route through both configured AWS profiles; both failed to obtain credentials before a model request could be made. No Opus model was invoked or confirmed, and no other model was substituted as an Opus review. The mathematical checks below are my own.

For question 1, the essential implication is short. Write \(c=c_l\). Every exact primary target is a smooth, divergence-free solution of \((E_C)\) on all of \(\mathbb R^3\), with
\[
  2/5<c<1/2,\qquad \lim_{|y|\to\infty}U(y)=0.
\]
After the permitted constant axial translation, it satisfies \((E)\), belongs to \(C^2(\mathbb R^3)\), and has \(U=o(|y|)\). L2 therefore gives a constant velocity; the decay condition makes that constant zero. The equation then gives constant pressure. Task §6 rejects this result as a target. This argument does not require any additional symmetry, power-law tail, energy, or stagnation-set assumption.

The full comparison follows. The conditions are cumulative: a symmetry or gauge condition alone does not imply L2. “Additional restriction” in the last column means that L2 does not need that condition, so imposing it cannot create a gap in the exclusion.

| Task condition and location | Comparison with L2 |
|---|---|
| **Exact equation and domain:** unforced, incompressible three-dimensional Euler on all of \(\mathbb R^3\); \((1-c)U+(cy+U)\cdot\nabla U+\nabla P=0\), \(\nabla\cdot U=0\). Derivatives are in physical similarity coordinates. Task §§1, 3. | Exactly L2's equation and domain. An exact profile satisfies these pointwise. Small sampled residuals alone do not establish this hypothesis. |
| **Similarity ansatz:** \(\tau=T-t>0\), \(y=(x-x_*)/\tau^c\), \(u=\tau^{c-1}U(y)\), \(p=\tau^{2c-2}P(y)\), \(\omega=\tau^{-1}\nabla\times U\). The exponent is the positive physical collapse exponent. The initial target is isotropic, has one spatial similarity scale, and is time independent in these coordinates. Task §§1, 3. | This gives the stationary system used by L2, with the same \(c\), not a differently normalized exponent. L2 does not address general time-dependent rescaled profiles or different scaling laws. |
| **Primary exponent:** \(0.4<c_l<0.5\). The separation from \(0.5\) must be numerically resolved; \(c_l\) is not to be minimized independently of solving the equations. Task §1. | The exact interval is contained in \(0<c<1/2\). L2 requires no fixed positive margin below \(1/2\). Numerical resolution of that margin is an evidence requirement, not a theorem hypothesis. |
| **Endpoint \(c_l=2/5\):** outside the initial open primary interval and requiring separate finite-energy treatment. Task §7. | It is inside L2's interval, so L2 excludes nonzero smooth decaying exact profiles there as well. The endpoint is not a gap in L2. |
| **Secondary exponents:** \(c_l=1/2\) is a calibration or secondary result; credible candidates outside the primary interval must be preserved and labeled. Task §1; the \(1/2\) baseline is also requested in §13. | The task's entire set of secondary possibilities does **not** imply \(c<1/2\). L2 does not exclude candidates at or above \(1/2\). Positive exponents below \(1/2\), including \(2/5\), remain covered if the other hypotheses hold. |
| **Center:** a point on the fixed \(z\)-axis. No horizontal drift or rotating frame is introduced. Task §§1, 3. | Compatible with L2. Center placement is not an additional restriction in the theorem's equation. It does not require \(U(0)=0\), an axis vorticity maximum, or a unique stagnation point. |
| **Optional axial drift:** constant \(C\), with transport \(cy+Ce_z+U\), \(z_c'(t)=-C\tau^{c-1}\), and \(z_c(t)=z_*+(C/c)\tau^c\). An appropriate centering condition and the equivalent canonical profile must be reported. Do not impose both \(U(0)=0\) and an unrelated center condition without checking compatibility. Task §3. | Removable for every fixed \(C\) because \(c>0\). The translation preserves all of L2's analytic hypotheses and the task's axial symmetry. The calculation is given below. |
| **Required two-fold symmetry:** \(Q=\operatorname{diag}(-1,-1,1)\), \(U(Qy)=QU(y)\), \(P(Qy)=P(y)\). Task §4. | An additional restriction. L2 is independent of symmetry. The symmetry is simultaneous horizontal sign reversal, not separate scalar parity for each horizontal component. |
| **Genuine fundamental \(m=2\) content:** non-axisymmetry, with resolvable nonzero \(n=2\) content in cylindrical velocity; purely four-fold and axisymmetric substitutes do not suffice. The vector rotational average is the specified measure of axisymmetry. Task §§4, 6. | An additional restriction, incompatible with L2's constant conclusion. L2 does not infer genuine \(m=2\) structure merely from equivariance, and the task does not permit that shortcut either. |
| **Angular freedom:** cylindrical fields are \(\pi\)-periodic; even harmonics, both sine and cosine components, the axisymmetric mean, and nonlinear higher harmonics must remain available. A wedge has rotational periodic identification. A truncation to \(n=0,\pm2\) is not an exact invariant reduction. Task §4. | No restriction on these features is imposed by L2. Its exclusion concerns the full equation, so it does not depend on a finite angular truncation. |
| **No additional imposed symmetry or altered problem:** no imposed separate horizontal reflections, \(z\)-parity, angular reflection, no-swirl condition, or full inversion parity; no physical boundary, external force, compressibility, imposed \(z\)-periodicity, or modified convection law. Initialization homotopies must return to the exact problem. Task §§1, 4. | L2 does not require any of the extra symmetries. Its equation matches the final problem. A residual for a modified equation would not establish its equation hypothesis. Accidental extra symmetry is distinct from imposing it as a search restriction; axisymmetric artifacts remain explicitly excluded. |
| **Smoothness and axis regularity:** a smooth Cartesian field, including the axis and center, with derivative convergence checked under refinement. The displayed transverse Taylor expansions and coupled cylindrical Fourier conditions must be respected; the transverse \(2\times2\) linear block is general. Task §§4, 11. | Smoothness implies \(C^2\) at every finite point, exactly the regularity L2 needs. L2 does not require uniform bounds on all derivatives over \(\mathbb R^3\). A genuinely only-\(C^{1,\alpha}\) field fails this implication and also fails the stated smooth target. The displayed axis conditions alone are not a substitute for smoothness of the limiting field. |
| **Representation and differential consistency:** velocity and pressure are the physical unknowns; any vorticity or potential parameterization must satisfy its defining relation to \(U\). Exact incompressibility is preferred; a divergence penalty is permitted for exploration but must be independently controlled. Smooth representations, correct coordinate derivatives, and full cylindrical geometric terms are required. Task §§3–5. | These are ways to approximate or verify the hypotheses, not replacements for them. L2 applies to an exact divergence-free limit. Neither a small aggregate loss nor a smooth network architecture proves those properties of a limit. |
| **Mandatory far field:** “The velocity must decay”; growing affine backgrounds and imposed external strain are excluded. Task §7. | On the usual whole-space meaning \(U(y)\to0\) as \(\lvert y\rvert\to\infty\), this implies \(U=o(\lvert y\rvert)\), and indeed is stronger. No algebraic decay rate is needed. |
| **Suggested tail, not mandatory tail:** \(d=1-1/c\), \(U\sim R^dA_\infty\), \(\nabla U,\Omega=O(R^{-1/c})\), \(P-P_\infty\sim R^{2d}B_\infty\), with unknown angular functions. In the primary interval, \(-3/2<d<-1\). These are assumptions to test, not a universal asymptotic theorem. Task §7. | Such a tail satisfies L2's velocity condition when understood globally with bounded angular coefficients. More importantly, L2 needs neither these powers nor these derivative or pressure asymptotics. Rejecting the suggested tail does not evade L2 while retaining global velocity decay. |
| **Tail flexibility:** no imposed compact support or exponential decay; no silently imposed fast-vorticity class. Explicit leading tails must obey \(\operatorname{div}_{S^2}A_T+(d+2)A_r=0\). Allow subleading powers, including degree \(2d-1\), and do not require exact exterior homogeneity. Task §7. | L2 adds none of these restrictive tail assumptions. The angular divergence identity implements the task's incompressibility when that tail ansatz is used. All globally decaying tails satisfying the equation are covered. |
| **“Smooth at every finite point”:** no assumption of analyticity at compactified infinity, which could exclude noninteger subleading powers. Task §7. | Fully compatible with \(C^2(\mathbb R^3)\). Infinity is not a point of \(\mathbb R^3\). Lack of analyticity, or lack of smoothness after compactification, does not violate L2's finite-point regularity requirement. |
| **Finite-energy interpretation:** a global similarity profile potentially usable as an inner limit of a solution from smooth finite-energy data. Do not require \(U\in L^2(\mathbb R^3)\). The profile need not describe the physical solution globally. Task §7. | L2 assumes no global energy bound. Every smooth profile already has finite energy on bounded sets. Physical matching and strong convergence are separate questions; neither creates an exception to L2 for an exact limit satisfying its hypotheses. |
| **Nontriviality and artifact rejection:** reject zero, constant, globally affine, irrotational, axisymmetric, boundary-supported, and effectively two-dimensional substitutes; verify genuine three-dimensional structure and stretching. Task §6. | These strengthen acceptance conditions. L2 forces precisely a rejected constant, and decay forces zero. Nonconstant affine fields usually fail sublinearity and are already inadmissible because of the task's far field. |
| **Scale and phase gauges:** use one justified spatial normalization, one pressure constant, and centering/angular phase conditions when needed. The true scaling is \(U_a(y)=aU(y/a)\), \(P_a(y)=a^2P(y/a)\), \(C_a=aC\). Do not fix several amplitudes or arbitrary derivative values without counting the available freedoms. Task §6. | L2 is invariant under this scaling and needs no gauge. The task's scale symmetry preserves \(\nabla U\) in supremum norm, so it does not justify prescribing \(\|\Omega\|_\infty=1\). These gauges cannot provide an escape from L2. |
| **Pressure gauge and consistency:** one additive constant, e.g. \(P(0)=0\), not also an independent \(P(\infty)=0\); test gradients or pressure relative to a limiting constant. Whole-space pressure/Biot–Savart consistency must be checked or explicitly left unfinished; an arbitrary exterior harmonic field must not be hidden forcing. Task §§6, 7. | L2 needs a global pressure satisfying the equation, not a pressure normalization, pressure decay rate, or prescribed pressure integral formula. For \(U\in C^2\), the equation gives \(\nabla P\in C^1\), hence \(P\in C^2\). Additional pressure consistency requirements narrow the admissible set. |
| **Stagnation geometry and paired peaks:** locate zeros of \(V=cy+Ce_z+U\), including off-axis pairs. Do not impose local outgoing behavior at every zero, nonzero axis vorticity, or an axis peak. Paired off-axis peaks inside the one shrinking core are allowed. Task §§1, 4, 8. | L2 imposes no stagnation-set cardinality, geometry, outgoing condition, or peak-location hypothesis. Multiple peaks inside one profile are covered. The task's conditional axis and peak-stretching checks are diagnostics, not extra assumptions on all branches. |
| **Numerical credibility:** full independent residual tests, axis and tail checks, angular resolution, non-affinity, removal of artificial penalties, and refinement of capacity, sampling, domain, and exponent. No unresolved outward core escape, shrinking unresolved core, or boundary transition is acceptable. Task §§6–7, 10–11. | L2 is an exact-profile obstruction, not a numerical acceptance threshold. These tests do not become unnecessary evidence for claims about saved numerical states. Section 8's restricted residual floor is discussed separately below. |
| **Other mechanisms and later physical claims:** anisotropic, discretely self-similar, rotating-profile, and multiple macroscopic-center mechanisms are outside the initial project. Stability, construction from one fixed initial condition, outer matching, and Navier–Stokes blowup are distinct achievements. Task §§1, 7, 12. | L2 does not generally decide those mechanisms or achievements. It excludes any proposed stationary inner limit that actually satisfies its hypotheses, regardless of the physical narrative attached to it. |

Task §9 also permits an exact nonconstant affine field as a residual unit test. Such tests remain legitimate diagnostics for every \(c\); they are explicitly inadmissible final candidates because of their far field. L2's failure to exclude a non-sublinear unit test is not a failure to cover the primary search target.

To make the axis conditions explicit, set \(r=(y_1^2+y_2^2)^{1/2}\). At each fixed \(z\), Task §4 requires the smooth Cartesian structure
\[
 U_1=a(z)y_1+b(z)y_2+O(r^3),\quad
 U_2=k(z)y_1+h(z)y_2+O(r^3),\quad
 U_3=w(z)+O(r^2),\quad a+h+w'=0.
\]
The four transverse coefficients are not restricted to an axisymmetric dilation-plus-rotation form. With the convention \(f=\sum_n f_n e^{in\theta}\), the listed necessary cylindrical smoothness conditions are
\[
 (U^r+iU^\theta)_n=O(r^{|n+1|}),\qquad
 (U^r-iU^\theta)_n=O(r^{|n-1|}),\qquad
 U^z_n,P_n=O(r^{|n|}).
\]
These are consequences or implementation checks for the smooth equivariant class; checking just these orders is not a proof of full smoothness. In particular, genuine \(n=2\) horizontal velocity can start at order \(r\). Nothing in L2 requires the more restrictive order \(r^3\).

The local checks in Task §8 are also conditional, not restrictions on every branch. At an axis stagnation point shifted to the origin, symmetry gives
\[
 \nabla U(0)=
 \begin{pmatrix}a&b&0\\k&h&0\\0&0&e\end{pmatrix},
 \qquad \Omega(0)=(0,0,k-b).
\]
If this vorticity is nonzero, the exact vorticity equation at \(V(0)=0\) gives \(\nabla U(0)\Omega(0)=\Omega(0)\), so \(e=1\). Divergence then gives \(a+h=-1\), and the transverse trace of \(\nabla V\) is \(2c-1<0\). At an interior maximum of \(|\Omega|\), when such a differentiable maximum exists, dotting the vorticity equation with \(\Omega\) gives
\[
 \Omega\cdot(\nabla U\,\Omega)=|\Omega|^2.
\]
Velocity decay alone need not ensure that a global vorticity maximum is attained. Neither this maximum nor nonzero vorticity at an axis stagnation point is a hypothesis of L2.

For question 2, the potentially delicate cases can be settled directly.

**The axial drift produces no scope gap.** Let \(a=(C/c)e_z\), \(Y=y+a\), and define
\[
 \widehat U(Y)=U(Y-a),\qquad \widehat P(Y)=P(Y-a).
\]
Then
\[
 cy+Ce_z+U(y)=cY+\widehat U(Y),
 \qquad \nabla_Y\widehat U(Y)=\nabla_yU(Y-a).
\]
Thus \((U,P)\) solves \((E_C)\) if and only if \((\widehat U,\widehat P)\) solves \((E)\); divergence is unchanged. Also
\[
 \frac{|\widehat U(Y)|}{|Y|}
 =\frac{|U(Y-a)|}{|Y-a|}\,\frac{|Y-a|}{|Y|}\longrightarrow0
\]
whenever \(U=o(|y|)\). Translation preserves \(C^2\) and global decay.

Since \(Qa=a\),
\[
 \widehat U(QY)=U(Q(Y-a))=Q\widehat U(Y),
 \qquad \widehat P(QY)=\widehat P(Y).
\]
A pressure constant can be reset after translation if desired. The physical coordinate identity is also exact:
\[
 Y=\frac{x-z_c(t)e_z}{\tau^c}+\frac Cc e_z
  =\frac{x-z_*e_z}{\tau^c}.
\]
This is recentering, not a new dynamical mechanism. Arbitrarily large but fixed \(C\) does not affect the exact theorem. For a sequence with varying \(C\), however, uniform numerical tail bounds must be checked after recentering; they are not automatically preserved with the same constants.

**Arbitrarily slow global decay is covered; decay on selected rays is not the same assumption.** The ordinary meaning of global decay is
\[
 \forall\varepsilon>0\ \exists R_0\ 
 \forall y,\quad |y|>R_0\Longrightarrow |U(y)|<\varepsilon.
\]
This implies sublinearity regardless of rate. In fact, smooth global decay makes \(U\) bounded, and \(|U(y)|/|y|\le M/|y|\to0\). A tail decreasing like an inverse logarithm, slower than every negative power, presents no problem. Neither a homogeneous leading term nor derivative decay is required by L2.

Decay in only some directions does not meet the task's global decay condition. Even convergence along every fixed ray, with no uniform control as the direction varies, does not by itself imply global decay or sublinearity. This distinction is real: one can put smooth bumps of height \(R_k\) in unit balls centered at
\[
 p_k=R_k(\cos(2^{-k}),\sin(2^{-k}),0),\qquad R_k=2^{3k}.
\]
Every fixed ray misses all sufficiently late balls. For the limiting ray with angle zero, its distance from \(p_k\) grows like \(R_k2^{-k}\); for any other fixed direction, the eventual angular separation is bounded away from zero. Yet a bump sum \(f\) with \(f(p_k)=R_k\) is not \(o(|y|)\). The sum is smooth because its supports are locally finite.

This construction is only a counterexample to a logical implication about decay, not an Euler profile or an existence claim. If desired, divergence-free, \(Q\)-equivariant velocity versions follow by using a compactly supported divergence-free vector bump \(W\) with \(W(0)\ne0\), and summing
\[
 R_k\bigl[W(y-p_k)+QW(Qy-p_k)\bigr].
\]
The paired supports have the same ray property. Translation, proper rotation, and locally finite summation preserve smoothness and divergence. At \(p_k\), only the first bump contributes for all sufficiently large \(k\). Such a \(W\) exists explicitly: take \(W=\nabla\times[\chi(y)(e_1\times y)/2]\), with a smooth cutoff \(\chi\) supported in the unit ball and equal to one near zero. Then \(W(0)=e_1\).

Nothing in Task §7 says to replace global decay by raywise decay. Under its standard meaning, there is no gap here. If the intended specification were changed to merely directional decay, a separate global sublinearity assumption or proof would be needed. Some fields that fail global decay are nevertheless globally sublinear—for example bounded fields or fields with sublinear growth—and L2 still covers those. Failure of decay alone is not an escape from the theorem.

**A genuinely only-\(C^{1,\alpha}\) axis or center is outside both L2 and the stated smooth target.** Such a solution is not excluded by L2 as stated. But Task §§1, 4, 7, and 11 do not admit a finite-point regularity defect as an acceptable smooth profile. The warning about compactified infinity does not relax regularity at the origin or axis. Nor does the task's instruction to preserve candidates at other exponents authorize changing the regularity class.

One must distinguish “known to be \(C^{1,\alpha}\), with higher regularity unresolved” from “actually not \(C^2\).” In the first case L2's applicability is unverified. In the second it fails, and the field is not an answer to the smooth target. Smooth numerical approximants can converge to a rough limit; smooth activations therefore do not close this issue. No regularity upgrade from \(C^{1,\alpha}\) to \(C^2\) is supplied by L2.

**The endpoint \(1/2\) and larger exponents are genuine uncovered secondary possibilities.** Task §1 says, verbatim:

> A candidate at c_l=0.5 is a secondary result or calibration, not achievement of the subcritical target. Preserve a credible candidate outside the primary interval, but clearly label its different significance. Failure of a search or of a restricted ansatz is not a nonexistence theorem.

Neither \(c=1/2\) nor \(c>1/2\) satisfies L2's exponent hypothesis. The theorem consequently says nothing about the existence or nonexistence of acceptable profiles there. “Not excluded by L2” is not evidence that one exists. Credible numerical states in those regimes must not be discarded on L2's authority. Conversely, an outside-primary candidate with \(0<c\le2/5\) is still excluded as a nonzero exact smooth decaying profile by L2.

An estimated exponent whose uncertainty crosses \(1/2\) cannot be declared excluded merely because its fitted central value is below \(1/2\). The task already requires this uncertainty to be reported. For a mathematically specified exact exponent strictly below \(1/2\), however close, L2 applies.

**The inner-limit language does not enlarge the stated exact-profile class.** Task §7 says:

> The goal is a global similarity profile potentially usable as the inner limit of a solution with smooth finite-energy initial data. Do NOT require U itself to belong to L^2(R^3).

“Global” here concerns the profile's domain in \(y\). It does not require the self-similar formula to describe the physical solution at every \(x\) before blowup. A limit defined on every fixed bounded similarity region can still be a profile on all of \(\mathbb R^3\), and L2 applies if that limit is \(C^2\), stationary, solves the specified equation, and is sublinear.

For completeness, the finite-energy motivation can be checked without adding a hidden global \(L^2\) hypothesis. Suppose the physical solutions have a uniform energy bound \(E\), and their rescaled velocities \(v_\tau\) converge strongly in \(L^2(B_R)\) to \(U\) for every fixed \(R\). Then
\[
 \tau^{5c-2}\int_{B_R}|v_\tau|^2\,dy\le E.
\]
If \(c<2/5\), this forces \(\int_{B_R}|U|^2=0\). At \(c=2/5\), it gives \(\int_{B_R}|U|^2\le E\) for every \(R\), hence \(U\in L^2(\mathbb R^3)\) by increasing \(R\). If \(c>2/5\), it gives no uniform global \(L^2\) bound for \(U\). These are conditional consequences of the stated uniform energy and convergence assumptions, not additional assumptions of L2.

This also explains why endpoint matching deserves separate discussion. A nonzero uniform angular tail of degree \(d=-3/2\) has logarithmically divergent energy, since its radial energy integral is proportional to \(\int^\infty r^{2d+2}\,dr=\int^\infty dr/r\). In the open primary interval the suggested nonzero leading tail also need not be square integrable. L2 uses neither this tail nor any energy integration.

Smooth finite-energy initial data alone do not ensure smoothness of a rescaled limit; derivative convergence still has to be established. They also do not, by themselves, establish the task's decay condition or stationarity. Those are explicit requirements of the desired profile. L2 excludes such a smooth decaying stationary inner limit in its exponent range. It does not rule out physical Euler blowup with a limit failing \(C^2\) regularity or global sublinearity, no stationary limit, or another scaling mechanism.

Paired off-axis peaks require no additional exception: fixed distinct points in similarity coordinates have physical separation proportional to \(\tau^c\), and thus lie in the same shrinking core. They are not multiple macroscopic centers.

For question 3, the permitted theorem-based status is exactly **RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS**. Task §14 states:

> Use an honest status such as STRONG NUMERICAL CANDIDATE, PRELIMINARY CANDIDATE, NO ACCEPTABLE CANDIDATE FOUND IN THIS SEARCH, or RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS. The last status requires an actual proof, not failed optimization.

Conditional on the separate proof audit being complete and successful, an accurate status sentence would be:

> RIGOROUS OBSTRUCTION UNDER EXPLICIT ASSUMPTIONS: Theorem L2 rules out every nonzero exact \(C^2\), globally decaying stationary Euler similarity profile on \(\mathbb R^3\) with \(0<c_l<1/2\), including the task's entire smooth primary \(m=2\) target \(2/5<c_l<1/2\), its permitted constant axial recenterings, and \(c_l=2/5\). It does not exclude the \(c_l=1/2\) calibration or candidates with \(c_l>1/2\), and it does not establish a numerical residual threshold or a general obstruction to Euler or Navier–Stokes blowup.

There are two different questions about stopping, and they must not be conflated. Task §13 says:

> A rigorous mathematical obstruction covering the whole explicitly specified search class, if truly proved and independently checked, supersedes further blind numerical work. Otherwise do not treat lack of convergence as a proof of nonexistence. Safety/permission/resource constraints may force an earlier stop; state the blocker and actual active hours exactly.

For the **primary exact-profile class**, L2 gives the requisite complete mathematical exclusion, conditional on its proof. Further blind numerical work aimed at finding a member of that empty class has been superseded mathematically.

For the **union of primary and explicitly preserved secondary possibilities**, L2 is not a whole-class obstruction: the task expressly includes a \(1/2\) calibration and preservation of credible candidates outside the primary interval. It therefore cannot, by itself, satisfy a literal claim that every remaining task-sanctioned exponent or secondary outcome has been ruled out. In particular, the scope audit does not certify an automatic blanket exemption from every remaining campaign obligation by treating those secondary possibilities as excluded.

The text also does not require a new exhaustive 96-hour campaign over all \(c\ge1/2\); preserving a credible outside-primary candidate is not an instruction to search every such exponent indefinitely. The defensible report separates the mathematical resolution of the primary objective from the state of the calibration and secondary work. If the entire campaign ends early, the report must identify the scope of the obstruction, the unfinished secondary work, and the actual reason for leaving that work unfinished. It must not describe L2 as a theorem about all of it.

The proof does not retroactively create numerical time or numerical results. Task §13 specifies:

> Count actual non-overlapping wall-clock time spent running substantive optimization, simulation, or independent numerical validation. Exclude idle time, waiting for a human, suspended jobs, literature reading, environment setup, drafting reports, and offline periods.

It also says:

> The 96-hour milestone is reached only after the measured active time is genuinely >=96h.

Task §14 adds:

> If execution limits, hardware protections, or permissions prevent completion in the current session, checkpoint and state actual active hours and a precise continuation command, never pretend that 96 hours were completed. The success criterion is credible mathematical/numerical evidence, not simply spending compute or lowering a training loss.

Accordingly, the final campaign report must retain all of the following:

- The actual independently auditable, non-overlapping active time. If it is below 96 hours, say explicitly that the 96-hour numerical milestone was not completed. Mathematical reading, proof writing, and this scope audit do not count as active numerical experiments.
- The numerical states actually obtained, including negative results and artifacts; the tested exponents and whether they were fixed or fitted; the available independent validation evidence; and any unresolved exponent sensitivity, axis, tail, pressure, or nondegeneracy issue.
- An explicit distinction between an approximate numerical state and a nonzero exact profile now excluded by L2. A small residual can remain a real numerical observation even when it cannot certify such an exact profile.
- The status of the \(c_l=1/2\) calibration and every credible outside-primary candidate: preserved and labeled if obtained, or not obtained/not searched/not fully validated as appropriate.
- The portions of the experiment queue, refinement, alternative representations, and independent checks that were not performed. An obstruction to exact primary profiles is not evidence that those experiments were executed.
- The proof's precise hypotheses, the separate proof-review evidence, and any uncompleted review. This scope audit alone does not meet the requirement that L2's proof be independently checked.
- The existing reproducibility deliverables required by §14: equations and source notes; runnable training, validation, tests, and resumption commands; configurations, saved candidates, and experiment tables; REPORT.md; STATE.json and NEXT_STEPS.md; the campaign ledger; and run/status/stop/resume scripts. Report missing or inapplicable items explicitly. Do not fabricate snapshots at active-hour milestones never reached. If work remains suspended for execution reasons, provide the real saved state and literal continuation command.

In particular, Task §14 requires these questions to be answered:

> Did we obtain a genuinely non-axisymmetric m=2 candidate? Is c_l numerically resolved below 1/2? Does the candidate survive removal of artificial nondegeneracy constraints and refinement? What is the worst validated region? Is the tail credible? What prevents a stronger conclusion?

When no acceptable candidate exists, “not applicable” or “not established” is an honest answer to the candidate-specific questions, with the reason stated. A theorem cannot supply missing validation metrics. I did not audit the campaign ledger or saved numerical candidates for this scope report, so I give no campaign-hour total or numerical-result claim. This audit performed no numerical profile experiments and adds zero active numerical experiment hours.

For question 4, Theory §7.8 is substantially correct about the **primary target**, but several expressions need correction or qualification:

- “This includes the target class of the task” is correct if “target” means the primary interval and its stated smooth decaying profiles. It overclaims if it is used to mean every explicitly requested secondary outcome. The primary/secondary distinction should be written into the scope statement.
- “With or without finite local energy” is misleading in its ordinary profile-space meaning. A \(C^2\) field has finite energy on every bounded region. The optional condition relevant to Task §7 is **finite total profile energy**, \(U\in L^2(\mathbb R^3)\). If the phrase instead means a uniform-in-time physical core-energy bound, that different condition should be named explicitly.
- “NOT COVERED: … growing velocity” is false as a blanket statement. L2 covers all \(o(|y|)\) growth, including unbounded sublinear growth. Replace it by “velocity not satisfying \(U=o(|y|)\), including nonconstant affine backgrounds.”
- “Any tail” must remain explicitly subordinate to global sublinearity. It does not include arbitrary linear growth hidden in narrowing angular regions. The listed homogeneous and nonhomogeneous decaying tails are correctly covered.
- “Profiles below \(C^2\)” correctly lists a theorem limitation, but the text should not imply that genuinely rough finite-point profiles are part of the stated smooth primary target.
- “Approximate solutions (no quantitative residual floor; section 8)” should distinguish no **computed numerical bound** from no positive floor at all. Section 8 asserts a nonconstructive positive floor on a restricted uniformly controlled class; it is not a theorem for the whole numerical search class.

I propose the following exact replacement for §7.8:

> **7.8 Scope.** L2 applies to exact time-independent solutions of \((E)\), or of \((E_C)\) after removal of the constant axial drift, on all of \(\mathbb R^3\), with \(0<c<1/2\), \(U\in C^2(\mathbb R^3)\), and \(U(y)=o(|y|)\) as \(|y|\to\infty\). It concludes that \(U\) is constant; if \(U\to0\), it concludes that \(U=0\) and \(P\) is constant.
>
> These hypotheses include the entire primary exact-profile class in Task §§1, 3, 4, and 7: smooth, globally decaying, genuinely two-fold profiles with \(2/5<c_l<1/2\), the prescribed isotropic stationary similarity ansatz, and the permitted constant axial recentering. The same exclusion applies at \(c_l=2/5\). No extra assumption on stagnation-set geometry, axis vorticity, off-axis paired peaks, angular tail structure, algebraic decay rate, analyticity at infinity, or total profile energy is needed. Every \(C^2\) profile already has finite energy on bounded sets; \(U\in L^2(\mathbb R^3)\) is not required.
>
> L2 does not decide the \(c_l=1/2\) calibration or candidates with \(c_l>1/2\), which the task explicitly treats as possible secondary results. Thus it is a complete obstruction to the primary exact-profile target, not an obstruction to every secondary possibility mentioned in the task.
>
> Outside L2's hypotheses are profiles failing \(C^2\) regularity at a finite point, or failing global sublinearity, including nonconstant affine backgrounds. Unbounded sublinear growth is covered by L2, although the task itself requires decay. Other time-dependent, discretely self-similar, rotating, anisotropic, or multiple macroscopic-center mechanisms are not generally decided by this stationary-profile theorem. Multiple peaks within one similarity core do not constitute such an exception.
>
> L2 alone gives no numerical acceptance threshold for approximate profiles. Section 8 gives a nonconstructive positive residual floor only under its additional uniform bounds and normalization. Neither statement establishes stability, a construction from finite-energy initial data, or a general obstruction to Euler or Navier–Stokes blowup by other mechanisms.

The sentences just before §7.8 saying “no obstruction” at \(c=1/2\) and \(c>1/2\) should likewise say **“this argument gives no obstruction.”** Failure of this argument is not a proof of existence or a statement that no other obstruction is possible.

Theory §8's compactness result is valid conditional on L2, with its stated fixed-\(c\), fixed-\(K\) hypotheses. Those hypotheses are substantially stronger than the task's exact-profile conditions. The task does not require the prescribed power envelope for every velocity, a global \(D^3U\) bound, a common bound across approximants, or the curvature normalization. A smooth decaying field can even have unbounded derivatives at infinity. None of these facts weakens L2's exact primary-class exclusion; they limit what §8 says about numerical approximations.

The statement that “the bound on \(D^3U\) (or a fixed Hoelder modulus of \(D^2U\)) is necessary” is too categorical. A \(D^3U\) bound or a fixed Hölder modulus is a **sufficient** way to get equicontinuity of \(D^2U\). A common modulus of continuity tending to zero also suffices and need not be Hölder. The supplied example proves that simply deleting this compactness control while retaining the other displayed bounds invalidates the asserted floor. It does not prove that those two particular regularity assumptions are the only possible ones.

The numerical interpretation also needs to retain its quantifiers: a fixed exponent, a common bound, a specified normalization, exact divergence or a controlled divergence defect, and a true whole-space residual norm. A finite set of sampled residual values or an RMS on a truncated domain does not establish the \(L^\infty(\mathbb R^3)\) premise. No uniform floor as \(c\to1/2\) follows from a theorem stated separately for each fixed \(c\).

Here is an exact replacement for §8 that includes the proof and the corrected interpretation:

> **8. Approximate solutions: a nonconstructive residual floor for a restricted class.** Work in canonical coordinates, after removing any constant axial drift. Fix \(0<c<1/2\), put \(d=1-1/c\), and fix \(K\ge1\). With \(\langle y\rangle=(1+|y|^2)^{1/2}\), let \(\mathcal F(c,K)\) consist of \(U\in C^3(\mathbb R^3;\mathbb R^3)\) satisfying
> \[
> \nabla\cdot U=0,\qquad
> |D^jU(y)|\le K\langle y\rangle^{d-j}\quad(j=0,1,2),
> \qquad \|D^3U\|_\infty\le K,\qquad \|D^2U\|_\infty=1.
> \]
> Assuming L2, there exists \(\varepsilon_0(c,K)>0\) such that, for every \(U\in\mathcal F(c,K)\) and every \(P\in C^1(\mathbb R^3)\),
> \[
> \|(1-c)U+(cy+U)\cdot\nabla U+\nabla P\|_{L^\infty(\mathbb R^3)}
> \ge\varepsilon_0(c,K).
> \]
>
> **Proof.** Suppose instead that such pairs \((U_n,P_n)\) have residuals tending to zero in the displayed whole-space norm. The derivative bounds and the uniform bound on \(D^3U_n\) give a subsequence converging in \(C^2_{\mathrm{loc}}\) to \(U\), by Arzelà–Ascoli and a diagonal extraction. The limit is divergence free and satisfies the same bounds for derivatives of orders zero through two.
>
> Set \(F_n=(1-c)U_n+(cy+U_n)\cdot\nabla U_n\). These fields converge locally uniformly to \(F=(1-c)U+(cy+U)\cdot\nabla U\). For any closed piecewise smooth curve \(\gamma\), the circulation of \(F_n\) is that of the residual, because the circulation of \(\nabla P_n\) is zero. It therefore tends to zero. The \(C^1\) field \(F\) has zero circulation around every such curve, so there is a global \(P\in C^2(\mathbb R^3)\) with \(\nabla P=-F\). Thus the limit solves the exact equation.
>
> Since \(d-2<0\), the second-derivative envelope gives \(|D^2U_n|\le1/2\) outside the fixed radius \((2K)^{1/(2-d)}\). The normalization \(\|D^2U_n\|_\infty=1\) must consequently be attained inside a fixed compact ball. Local uniform convergence of \(D^2U_n\) preserves \(\|D^2U\|_\infty=1\). The velocity envelope gives \(U\to0\), because \(d<0\). L2 forces \(U=0\), contradicting the surviving normalization. This proves the asserted positive floor.
>
> The curvature normalization is a legitimate single spatial-scale gauge for fields with \(0<\|D^2U\|_\infty<\infty\), since \(U_a(y)=aU(y/a)\) gives \(\|D^2U_a\|_\infty=\|D^2U\|_\infty/a\). Rescaling can change the constant in the other bounds. This gauge does not justify fixing an additional independent amplitude or the vorticity supremum.
>
> Some uniform compactness control on \(D^2U\) cannot simply be omitted from this argument. A bound on \(D^3U\), a common Hölder modulus of \(D^2U\), or another common modulus of continuity tending to zero is sufficient. To see why the other displayed bounds alone do not imply the floor, take a nonzero smooth compactly supported divergence-free field \(W\), normalized so that \(\|D^2W\|_\infty=1\), and set \(U_\ell(y)=\ell^2W(y/\ell)\), \(P_\ell=0\), \(0<\ell\le1\). Then the order-zero, order-one, and order-two envelopes hold with a common sufficiently large \(K\), and \(\|D^2U_\ell\|_\infty=1\), but \(\|D^3U_\ell\|_\infty=\ell^{-1}\|D^3W\|_\infty\). With \(x=y/\ell\), the momentum residual is
> \[
> \ell^2\bigl[(1-c)W(x)+cx\cdot\nabla W(x)\bigr]
> +\ell^3 W(x)\cdot\nabla W(x),
> \]
> whose supremum tends to zero. This is a family of approximate fields, not a family of nonzero exact profiles.
>
> If exact incompressibility is omitted, the same compactness proof gives a positive floor for the sum of the momentum and divergence \(L^\infty(\mathbb R^3)\) residuals, under the remaining common bounds and normalization.
>
> **Numerical interpretation.** For a sequence of normalized divergence-free fields at one fixed \(c\in(0,1/2)\), convergence of the true whole-space momentum residual to zero implies that, for every fixed finite \(K\), the sequence is eventually outside \(\mathcal F(c,K)\). It cannot simultaneously retain all the displayed common derivative and tail bounds and the normalization. This statement neither identifies which bound fails nor provides a computed value of \(\varepsilon_0\). It does not apply directly to sampled residuals, truncated-domain losses, general flexible tails, or exponent sequences approaching \(1/2\). A merely decreasing residual need not converge to zero and can remain above an unknown positive floor. The task does not assume membership in \(\mathcal F(c,K)\); this floor is therefore a separate conditional result for a restricted class of approximations.

These changes preserve the actual mathematical strength of L2: the primary smooth decaying exact-profile target is excluded without extra tail or energy hypotheses. They also preserve the task's explicit limits: secondary exponents remain undecided, approximate numerical states require honest reporting, and a successful theorem audit does not establish numerical work or physical blowup conclusions that were not obtained.
