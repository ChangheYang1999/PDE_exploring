# 16-Hour Research Task: Near-Sharp Hölder Constants for Second-Order Riesz Transforms

## 1. Research objective and strict scope

Conduct a sustained **16-hour mathematical research investigation** of optimal Hölder seminorm estimates for two-dimensional second-order Riesz transforms.

The objective is to establish **rigorous, explicit, and as nearly sharp as possible \(C^\alpha\) operator bounds**, especially for small positive \(\alpha\).

You may use all appropriate research methods:

- Extensive mathematical literature searches.
- Analytical derivations and rigorous proofs.
- Symbolic calculations.
- Numerical integration and numerical optimization.
- High-precision computation.
- Computer-assisted rigorous inequalities and interval arithmetic.
- Numerical exploration of extremizers and near-extremizers.

There is no prohibition on substantial computation.

However, there is one nonnegotiable requirement:

**The final mathematical result must be a rigorously proved theoretical inequality. Purely numerical results are not acceptable as the main deliverable.**

If sharpness cannot be proved, establish the smallest theoretical upper bound you can rigorously justify.

Numerical computations should primarily help identify optimal constants, guide proofs, improve analytical inequalities, and assess whether the proven upper bound is close to sharp.

Do not investigate the underlying PDE, transport equations, \(L^2\), \(H^{-1}\), nonlinear stability, energy estimates, or stability closure.

Study only Hölder estimates for the specified operators.

## 2. Mathematical definitions

Work in \(\mathbb R^2\).

Define the first-order Riesz transforms by

\[
R_j=\partial_j(-\Delta)^{-1/2}.
\]

The two main second-order operators are

\[
A_{xx}=R_1^2=\partial_{xx}(-\Delta)^{-1},
\]

\[
A_{xy}=R_1R_2=\partial_{xy}(-\Delta)^{-1}.
\]

Because the diagonal second-order Riesz transform contains a local distributional contribution, also define

\[
T_{xx}=R_1^2+\frac12I
=\frac12(R_1^2-R_2^2),
\]

and

\[
T_{xy}=R_1R_2.
\]

Their principal-value kernels are

\[
K_{xx}(z)
=\frac{z_1^2-z_2^2}{2\pi|z|^4}
=\frac{\cos2\theta}{2\pi|z|^2},
\]

\[
K_{xy}(z)
=\frac{z_1z_2}{\pi|z|^4}
=\frac{\sin2\theta}{2\pi|z|^2}.
\]

Consequently,

\[
R_1^2=T_{xx}-\frac12I.
\]

Verify all of these formulas carefully, including their Fourier multipliers, signs, normalization, and distributional local terms.

The main Hölder seminorm is

\[
[f]_\alpha
=\sup_{x\ne y}
\frac{|f(x)-f(y)|}{|x-y|^\alpha},
\qquad 0<\alpha<1.
\]

Start from real-valued test functions in \(C_c^\infty(\mathbb R^2)\), and specify a mathematically appropriate extension to homogeneous Hölder spaces if needed.

In particular, carefully address the definition of singular integrals on functions that need not decay at infinity, and distinguish operators defined modulo constants from pointwise-normalized operators.

## 3. Constants to investigate

The primary sharp constant is

\[
C_\alpha
=\sup_{[f]_\alpha\ne0}
\frac{[T_{xx}f]_\alpha}{[f]_\alpha}.
\]

By rotational invariance, we expect

\[
\boxed{
\|T_{xx}\|_{\dot C^\alpha\to\dot C^\alpha}
=
\|T_{xy}\|_{\dot C^\alpha\to\dot C^\alpha}
=C_\alpha.
}
\]

Prove this equality rigorously.

Also investigate the sharp constant of the original diagonal second-order Riesz transform,

\[
D_\alpha
=\|R_1^2\|_{\dot C^\alpha\to\dot C^\alpha}.
\]

Since

\[
R_1^2=T_{xx}-\frac12I,
\]

we have

\[
|D_\alpha-C_\alpha|\le\frac12.
\]

This means the leading small-\(\alpha\) asymptotic coefficients agree, whenever they exist.

However, the exact finite-\(\alpha\) constants may differ substantially.

**We need rigorous estimates for both \(C_\alpha\) and \(D_\alpha\).**

Do not assume that removing or adding \(\frac12I\) necessarily improves the full operator norm.

The main priority is obtaining the smallest rigorous bounds for these constants.

## 4. Exploit the composition and complex structure

A second-order Riesz transform is the composition of two first-order Riesz transforms.

However, do not simply multiply their independent Hölder operator norms.

That generally produces an \(O(\alpha^{-2})\) bound and loses cancellation.

Instead, combine the operators exactly at the Fourier multiplier level and estimate their composition as a single singular integral.

Investigate all useful structures:

1. Fourier multiplier identities.
2. Distributional singular-integral representations.
3. Angular cancellation.
4. Rotation invariance.
5. Harmonic decomposition.
6. Mellin transforms and homogeneous functions.
7. Relations to the Beurling–Ahlfors transform.

In particular,

\[
T_{xx}+iT_{xy}
=\frac12(R_1+iR_2)^2.
\]

Investigate whether the theory of the Beurling transform provides sharper Hölder bounds, explicit constants, or exact formulas.

Carefully distinguish real-valued Hölder operator norms from complex-valued ones.

Use any exact algebraic identities that may improve the theoretical estimate.

## 5. Extensive literature investigation

Search for results concerning:

- Sharp Hölder norms of the Hilbert transform.
- Hölder estimates for first- and second-order Riesz transforms.
- Hölder norms of the Beurling–Ahlfors transform.
- Sharp Schauder constants.
- Calderón–Zygmund operators with special angular kernels.
- Sharp modulus-of-continuity inequalities.
- Optimal singular-integral estimates in Besov and Hölder–Zygmund spaces.

Determine whether the precise constants we need are known.

Separate carefully:

1. Proven exact sharp constants.
2. Sharp small-\(\alpha\) asymptotic coefficients.
3. Explicit but nonsharp upper bounds.
4. Qualitative boundedness results.
5. Numerically conjectured constants.

Use verifiable references, with exact theorem statements and their hypotheses wherever possible.

Do not rely on unverified bibliographical claims.

If existing literature provides a useful estimate, reproduce the relevant argument and attempt to optimize its constants.

Do not stop at a published nonsharp bound if there is a plausible way to improve it.

## 6. Primary mathematical goal: small-\(\alpha\) sharp asymptotics

The first major objective is the small-\(\alpha\) behavior

\[
C_\alpha\sim \frac{C_*}{\alpha},
\qquad \alpha\to0^+,
\]

if such an asymptotic formula holds.

Determine whether

\[
\boxed{
C_*=\lim_{\alpha\to0^+}\alpha C_\alpha
}
\]

exists.

Try to calculate \(C_*\) exactly.

Ideally establish

\[
C_\alpha=\frac{C_*}{\alpha}+O(1)
\]

with a rigorous remainder.

If a complete proof is not possible, prove the sharpest possible two-sided inequalities

\[
C_*^-
\le\liminf_{\alpha\to0^+}\alpha C_\alpha
\le\limsup_{\alpha\to0^+}\alpha C_\alpha
\le C_*^+.
\]

The numerical gap \(C_*^+-C_*^-\) should be made as small as possible.

Do not treat matching numerical approximations as proof of equality.

Also consider whether a better expansion can be proved, for example,

\[
C_\alpha=\frac{C_*}{\alpha}+C_0+o(1).
\]

This is optional and should not delay the main objective of a rigorous near-sharp bound.

## 7. Second mathematical goal: optimized finite-\(\alpha\) bounds

For general \(0<\alpha<1\), find an explicit formula \(F(\alpha)\) such that

\[
\boxed{
C_\alpha\le F(\alpha).
}
\]

Also derive an explicit formula \(G(\alpha)\) satisfying

\[
\boxed{
D_\alpha\le G(\alpha).
}
\]

Every constant must be explicitly defined and rigorously justified.

Bounds of the form

\[
F(\alpha)=\frac{A}{\alpha}+\frac{B}{1-\alpha}+D
\]

are acceptable intermediate results, but do not assume this is the optimal functional form.

Try to improve the constants and the dependence on \(\alpha\).

In particular:

- Optimize any near-field/far-field splitting parameters.
- Do not introduce unnecessarily large triangle-inequality constants.
- Preserve cancellation between singular-integral contributions.
- Exploit the angular structure of the kernels.
- Avoid independent estimates of terms when their combination has better cancellation.
- Investigate sharper estimates for increments \(Tf(x)-Tf(y)\).
- Where appropriate, optimize over the entire class of admissible Hölder increments.

An inequality is not the final result merely because it is correct.

**Continue improving the proven constant until there is no reasonable remaining improvement within the research time.**

If the theory leads to an optimization problem over finitely many parameters, optimize it rigorously, using certified numerical methods if necessary.

For instance, a bound of the form

\[
F(\alpha)=\inf_{\lambda>0}\Phi(\alpha,\lambda)
\]

is acceptable if the inequality has a complete proof and the optimization is well-defined. Prefer a usable explicit or rigorously computable expression.

## 8. Lower bounds and possible extremizers

A key part of the investigation is determining how close the theoretical bound is to sharp.

Search for extremizing or near-extremizing functions.

Possible test families include

\[
f(r,\theta)=\chi(r)r^\alpha g(\theta),
\]

with optimized angular profile \(g\).

Other possibilities include:

- Piecewise-defined homogeneous functions.
- Functions with angular sign changes.
- Functions supported on annuli.
- Multiscale constructions.
- Oscillatory or highly anisotropic functions.
- Functions suggested by the complex structure of the Beurling transform.

Do not assume that a single angular Fourier mode is extremal.

Explore numerical optimization over these families.

However, numerical results must serve the analytical goal.

Whenever a promising candidate is found, attempt to convert it into a rigorous lower bound.

For example, construct an explicit test function and prove

\[
C_\alpha\ge L(\alpha)
\]

using exact integration, explicit inequalities, or certified numerical integration with mathematically justified error bounds.

Then compare

\[
L(\alpha)\le C_\alpha\le F(\alpha).
\]

A small rigorous gap would strongly support near-sharpness.

If only a numerical lower-bound candidate is available, label it as heuristic and never present it as a theorem.

## 9. Numerical experimentation: permitted and encouraged

Use numerical computation actively wherever it may improve the mathematical result.

Examples include:

1. Searching for optimal angular functions.
2. Optimizing analytic cutoff parameters.
3. Numerically approximating extremizers.
4. Testing competing theoretical inequalities.
5. Investigating small-\(\alpha\) asymptotic coefficients.
6. High-precision evaluation of exact formulas.
7. Testing whether proposed inequalities are nearly saturated.
8. Certified verification of finite-dimensional optimization steps.

You may use Python, Julia, Mathematica, or other suitable tools.

Do not artificially restrict computation to tiny experiments.

Nevertheless, numerical work must be purposeful.

**The final deliverable cannot consist only of a numerical estimate of an operator norm.**

The main result must be a proven upper bound.

Numerical evidence is secondary and should help assess how near-sharp the theorem may be.

In particular, a numerical estimate smaller than a theoretical upper bound does not automatically prove that the upper bound can be improved.

When possible, convert numerical observations into explicit mathematical lemmas.

## 10. Secondary issue: restricted symmetry classes

Only after substantial progress on the unrestricted estimates, investigate whether symmetry restrictions improve the constants.

For example, consider functions that are odd in both variables, or even in both variables.

Determine whether

\[
\|T_{xx}\|_{\dot C^\alpha_{\mathrm{odd,odd}}\to\dot C^\alpha}
\]

or

\[
\|T_{xy}\|_{\dot C^\alpha_{\mathrm{odd,odd}}\to\dot C^\alpha}
\]

is smaller than the unrestricted constant.

Do not assume rotation invariance identifies these restricted constants.

This investigation is strictly secondary.

If time is limited, prioritize the unrestricted \(C^\alpha\) estimates and omit this section entirely.

Do not study the PDE producing these symmetry constraints.

## 11. Mandatory standards for theoretical results

Every claimed theorem must specify:

1. The precise function space.
2. The exact Hölder seminorm.
3. The definition of the singular integral.
4. The operator normalization.
5. The complete upper-bound constant.
6. The admissible range of \(\alpha\).
7. A mathematically valid proof.

No generic unspecified constants are allowed in the final main inequalities.

Distinguish explicitly between:

- Proven exact sharp constants.
- Proven asymptotically sharp estimates.
- Rigorous near-sharp bounds.
- Rigorous but nonsharp intermediate estimates.
- Numerical conjectures.

Numerical optimization cannot replace a missing analytical proof.

If you use interval arithmetic to certify a constant, provide sufficient information to reproduce the enclosure rigorously.

If a proof fails, document the failure, correct it, and seek an alternative method.

Be especially careful with:

- Principal-value cancellations.
- Singularities at the origin.
- Large-radius convergence.
- Local identity terms.
- The difference between full Hölder norms and homogeneous seminorms.
- The dependence on \(\alpha\).
- Possible losses from applications of the triangle inequality.

Independently recheck any final theorem before reporting it.

## 12. Time allocation: 16 hours

**Use a 16-hour wall-clock research budget, subject to actual execution limits.**

Do not interpret the time budget as a request to simply wait or repeatedly perform unproductive calculations.

The entire period should be directed toward advancing the rigorous mathematical result.

### Hours 0–2: Literature and mathematical setup

- Verify all kernels and Fourier multipliers.
- Establish rotation identities.
- Survey the relevant sharp-constant literature.
- Identify promising proof methods.
- Establish at least one initial explicit rigorous upper bound if feasible.

### Hours 2–8: Main analytical work

- Derive rigorous \(C^\alpha\) bounds.
- Track all coefficients.
- Exploit kernel cancellations.
- Optimize the main estimates.
- Investigate Beurling-transform methods and other promising representations.
- Study the small-\(\alpha\) asymptotics.

### Hours 8–13: Improve sharpness using theory and computation

- Search for near-extremizers.
- Compare numerical candidates with rigorous bounds.
- Refine the analytical inequalities.
- Optimize any auxiliary parameters.
- Attempt rigorous lower bounds and sharp asymptotics.
- Iterate between theoretical analysis and numerical exploration.

### Hours 13–16: Proof optimization and independent audit

- Recheck every theorem.
- Independently verify all constants and signs.
- Eliminate unjustified steps.
- Test whether the final constants can be improved.
- Produce the complete mathematical report.

These phases are guidelines, not rigid restrictions. If a more promising method appears, reorganize the schedule.

Do not terminate the investigation merely because a correct but loose estimate has been obtained.

If the main theorem is proved early, use the remaining productive research time to improve its constant, strengthen the lower bound, or verify sharpness.

Save intermediate results and checkpoints periodically so that work can be resumed if the environment interrupts the session.

If the execution environment imposes a shorter runtime, preserve the proof, code, bibliography, and remaining research plan rather than falsely claiming that all 16 hours were completed.

Report actual time spent.

## 13. Required final mathematical results

The final report must prominently state the strongest proven bounds in the form

\[
\boxed{
[T_{xx}f]_\alpha\le F(\alpha)[f]_\alpha,
}
\]

\[
\boxed{
[T_{xy}f]_\alpha\le F(\alpha)[f]_\alpha,
}
\]

and

\[
\boxed{
[R_1^2f]_\alpha\le G(\alpha)[f]_\alpha.
}
\]

Here \(F(\alpha)\) and \(G(\alpha)\) must be explicit, rigorously established, and optimized as far as possible.

Also report the best rigorous lower bounds

\[
L(\alpha)\le C_\alpha,
\]

if available.

For small \(\alpha\), clearly state the best established coefficient of \(1/\alpha\).

If exact sharpness remains unproved, quantify the gap between the best theoretical upper and lower bounds.

## 14. Final deliverables

Produce a self-contained research report containing:

1. Mathematical definitions and identities.
2. Literature findings with verified references.
3. A complete theorem for the explicit Hölder upper bounds.
4. Detailed mathematical proofs.
5. Every optimization used in the theoretical constants.
6. Rigorous lower bounds, if obtained.
7. Numerical experiments and their relevance to sharpness.
8. Small-\(\alpha\) asymptotic analysis.
9. A precise comparison of the bounds for \(T_{xx}\), \(T_{xy}\), and \(R_1^2\).
10. A list of unresolved steps and the remaining theoretical gap.

Preserve any supporting reproducible numerical or symbolic code, but keep the primary output mathematical.

## 15. Final priority and success criterion

The principal goal is not to produce a large number of calculations or conjectures.

It is to produce **the strongest rigorous \(C^\alpha\) estimate possible**.

The ideal result is the exact sharp constant.

The next best result is a provably sharp small-\(\alpha\) asymptotic coefficient.

If neither is attainable, the required result is a rigorously proved explicit upper bound, optimized to be as small as possible, with theoretical or numerical evidence indicating its closeness to sharpness.

**Purely numerical conclusions, unsupported sharpness claims, and bounds containing unspecified constants are unacceptable as final results.**

Remain focused exclusively on the Hölder estimates for these second-order Riesz transforms throughout the 16-hour investigation.
