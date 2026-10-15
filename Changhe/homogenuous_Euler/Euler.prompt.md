# Research Task: Global Nonexistence or Construction of Homogeneous Stationary Euler Flows for \(1<\alpha<2\)

You are GPT-6 Pro acting as an independent mathematical researcher specializing in incompressible Euler equations, geometric PDE, differential topology, and rigorous analysis.

**Your primary goal is to determine whether nontrivial globally \(C^2\) homogeneous stationary solutions of the three-dimensional incompressible Euler equations can exist for \(1<\alpha<2\), without imposing axisymmetry, a Beltrami condition, or any finite-dimensional ansatz.**

Pursue a rigorous nonexistence theorem if possible. Otherwise, seek a genuinely nonaxisymmetric counterexample, a meaningful conditional theorem, or the strongest rigorously established partial result.

Do not assume the desired conclusion. An unsuccessful investigation must still produce a substantive mathematical report. Work on this research problem for one complete research round.

## 1. Mathematical setup

Consider stationary incompressible Euler in \(\mathbb R^3\setminus\{0\}\):

\[
(u\cdot\nabla)u+\nabla p=0,\qquad
\nabla\cdot u=0.
\]

Seek homogeneous solutions

\[
u(r\omega)=r^{-\alpha}
\big(v(\omega)+f(\omega)\omega\big),
\]

\[
p(r\omega)=r^{-2\alpha}P(\omega),
\]

where

\[
1<\alpha<2,
\]

\(v\) is tangent to \(S^2\), and \(v,f,P\in C^2(S^2)\).

The spherical Euler system is

\[
(2-\alpha)f+\operatorname{div}_S v=0,
\]

\[
v\cdot\nabla_S f
=|v|^2+\alpha f^2+2\alpha P,
\]

\[
\nabla_v^S v+(1-\alpha)fv+\nabla_S P=0.
\]

Define the Bernoulli function

\[
H=|v|^2+f^2+2P.
\]

Then

\[
v\cdot\nabla_S H=2\alpha fH,
\]

and

\[
v\cdot\nabla_S f
=\alpha H+(1-\alpha)|v|^2.
\]

Independently verify all equations and sign conventions before relying on them.

The theorem under investigation is:

**Conjecture.** For every \(\alpha\in(1,2)\), every globally \(C^2\) homogeneous stationary incompressible Euler solution on \(S^2\) is trivial:

\[
v=f=P=0.
\]

This is the target to prove or refute, not an assumed fact.

## 2. Establish the precise literature baseline

Examine at least:

- Roman Shvydkoy, *Homogeneous solutions to the 3D Euler system*, arXiv:1510.03378, particularly Propositions 2.1, 3.1, 3.2, and 5.1, and Lemma 4.5.
- Ken Abe, *Existence of Homogeneous Euler Flows of Degree \(-\alpha\notin[-2,0]\)*, arXiv:2305.05987, particularly the Beltrami, axisymmetric, and existence results.
- Relevant subsequent literature, if accessible.

Separate unrestricted results from axisymmetric, irrotational, and Beltrami classifications.

In particular, Shvydkoy's Proposition 3.2 implies that for \(1<\alpha<2\), a globally \(C^2\) solution with \(H\equiv0\) is trivial. Verify its short proof independently.

Do not invoke the \(H\leq0\) result for \(0<\alpha<1\) outside its valid range.

A separate exploratory argument for \(0<\alpha<1\) used a Bernoulli-weighted divergence-free field and a regularized closed one-form. That argument has not been independently certified. Treat it as a possible source of ideas, not an established theorem.

## 3. Derive universal global identities

Starting with the complete spherical Euler equations, derive and verify

\[
\alpha\int_{S^2}H\,dS
=
(2-\alpha)\int_{S^2}f^2\,dS
+
(\alpha-1)\int_{S^2}|v|^2\,dS.
\]

For \(1<\alpha<2\), this shows that every nontrivial solution must satisfy

\[
\int_{S^2}H\,dS>0.
\]

Determine the strongest pointwise and geometric conclusions following from this positive-average identity.

Also analyze stagnation points. The radial momentum equation suggests

\[
v(\omega)=0\implies H(\omega)=0.
\]

Use the hairy-ball theorem to determine whether the zero set of \(H\) must be nonempty for every candidate solution.

Investigate whether \(H\) must be nonnegative, must change sign, or can have either sign. Prove any claimed sign restriction without an additional symmetry assumption.

## 4. Priority investigation: exclusion of negative-Bernoulli regions

This is a particularly promising preliminary lemma to verify independently.

For \(1<\alpha<2\), define

\[
\beta=\frac{2-\alpha}{2\alpha},
\qquad 0<\beta<\frac12.
\]

On a component of \(\{H<0\}\), set

\[
W_-=(-H)^\beta v.
\]

Bernoulli transport and incompressibility formally imply

\[
\operatorname{div}_S W_-=0.
\]

At the same time,

\[
W_-\cdot\nabla_S f
=(-H)^\beta
\left[\alpha H+(1-\alpha)|v|^2\right]<0.
\]

Investigate whether this yields an unconditional contradiction via integration, invariant measure, or Poincaré recurrence.

A concrete route is to extend \(W_-\) by zero across \(H=0\), and prove that the extension is divergence-free in the distributional sense.

Do not assume the extension is \(C^1\): since \(0<\beta<1/2\), that regularity can fail.

Instead, consider smooth cutoffs of the form

\[
W_\varepsilon
=
\chi\left(\frac{-H}{\varepsilon}\right)
(-H)^\beta v
\]

on \(\{H<0\}\), extended by zero elsewhere, with \(\chi\) vanishing near zero.

Derive the divergence exactly and determine whether it converges to zero distributionally as \(\varepsilon\to0\).

If successful, test whether integrating \(\operatorname{div}_S(fW_-)=W_-\cdot\nabla_S f\) establishes

\[
\boxed{H\geq0\quad\text{for }1<\alpha<2.}
\]

This is a proposed lemma, not an assumed theorem. Check every step carefully, including the behavior of arbitrary irregular zero sets.

If it is valid, treat it as a foundational reduction for the remainder of the investigation.

## 5. Bernoulli-weighted flow and global topology

Assuming \(H\geq0\) has been rigorously established, consider

\[
W=H^\beta v,
\qquad
\beta=\frac{2-\alpha}{2\alpha}.
\]

Investigate whether \(W\) is globally continuous and distributionally divergence-free on \(S^2\), even if it fails to be \(C^1\).

Since \(H^1_{\mathrm{dR}}(S^2)=0\), determine whether a global \(C^1\) streamfunction \(\Psi\) exists satisfying

\[
W=J\nabla_S\Psi,
\qquad JX=\omega\times X.
\]

Study the geometry of components of \(\{H>0\}\), their boundaries, possible annuli, critical points, and closed streamlines.

Check the exact regularity requirements of all topological arguments. In particular, classical Morse–Sard arguments cannot automatically be applied to an arbitrary \(C^1\) streamfunction.

Investigate whether connected-boundary components are impossible and what geometry remains for hypothetical solutions.

## 6. Singular weighted one-form: the main obstruction problem

Define

\[
\eta=(1-\alpha)v^\flat-df,
\]

where \(v^\flat\) is the metric-dual one-form.

Let \(\mu\) be the outward-oriented area form and \(\zeta=\operatorname{curl}_S v\), with \(d(v^\flat)=\zeta\mu\).

Verify directly from the complete Euler equations the identities

\[
\eta(v)=-\alpha H,
\]

\[
dH\wedge\eta=-2\alpha H\zeta\mu,
\]

and

\[
d\eta=(1-\alpha)\zeta\mu.
\]

Define

\[
\gamma=\frac{1-\alpha}{2\alpha}.
\]

For \(1<\alpha<2\),

\[
-\frac14<\gamma<0.
\]

On \(\{H>0\}\), these identities formally imply

\[
\boxed{d(H^\gamma\eta)=0.}
\]

This is the key analytical difficulty.

Unlike the case \(0<\alpha<1\), the exponent \(\gamma\) is negative. Therefore \(H^\gamma\eta\) may become singular as \(H\to0\).

Investigate rigorously:

- Whether the singular one-form admits a locally integrable or distributionally closed extension.
- Whether a regularization \(\Theta_\varepsilon=(H+\varepsilon)^\gamma\eta\) has a controllable exterior derivative.
- Whether a boundary-defect measure appears on the zero set of \(H\).
- Whether the complete Euler equations constrain the vanishing order of \(H\), the vorticity \(\zeta\), or \(\eta\) sufficiently to eliminate that defect.
- Whether pairing the regularized one-form with the global streamfunction of \(W\) gives a sign-definite integral contradiction.

Do not bound the regularization error by \(O(\varepsilon^\gamma)\) and then claim it vanishes: \(\gamma<0\), so that bound diverges.

Seek a sharper cancellation, a coarea estimate, a geometric argument, or an Euler-specific structural identity.

Distinguish conclusions valid under nondegenerate-zero, finite-order-vanishing, real-analytic, or other additional hypotheses from conclusions valid for arbitrary \(C^2\) profiles.

## 7. Alternative proof and construction strategies

Do not limit the investigation to the weighted-one-form approach.

Explore whether the interval \(1<\alpha<2\) admits a different mechanism based on:

- Global integrated energy, Bernoulli, or vorticity identities.
- The geometry of streamlines, invariant measures, or recurrence on the sphere.
- Hodge decomposition and the topology of stagnation sets.
- The full stationary Euler vorticity equation.
- Spectral obstructions from spherical harmonics.
- Exact finite-dimensional, nonaxisymmetric ansatzes, if these provide either counterexamples or instructive restricted rigidity results.
- Perturbative constructions near \(\alpha=1\) or \(\alpha=2\), with careful treatment of possible singular endpoint behavior.

For any candidate nonzero solution, verify the complete three-dimensional Euler equations, homogeneous scaling, and global \(C^2\) angular regularity.

Never regard a numerical solution or a truncated spectral residual as an exact Euler solution without a rigorous error or existence certificate.

## 8. Required deliverable

Produce a self-contained mathematical research report containing:

**Status:** SOLVED, PARTIAL, or STUCK.

**Main result:** The strongest theorem or counterexample actually established, stating the exact exponent interval, regularity, and symmetry assumptions.

**Detailed proof:** Complete derivations and estimates for every claimed mathematical result.

**Verified preliminary lemmas:** In particular, report whether the proposed \(H\geq0\) sign lemma for \(1<\alpha<2\) is correct.

**Remaining obstacle:** Identify exactly what prevents an unrestricted nonexistence proof, if no complete proof emerges.

**Counterexamples and tests:** Clearly distinguish actual Euler solutions from examples satisfying only reduced equations.

**Literature provenance:** Attribute known results accurately, and do not claim mathematical novelty solely because a derivation was produced.

**Recommended next research step:** Give one precise, self-contained problem that could resolve the remaining obstruction.

Aim for the strongest rigorous result obtainable in this research round. Do not manufacture a complete theorem if the decisive argument remains missing.

**Important:** The primary objective is an unrestricted theorem for globally smooth, genuinely three-dimensional Euler profiles. A result limited to axisymmetric, Beltrami, or finite-dimensional ansatz classes does not solve the main question.

Stop after producing the report. Do not initiate a new research round, delegate work to other agents, or move to Navier–Stokes.