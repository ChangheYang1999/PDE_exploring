# C2 transverse geometry and the remaining coverage gap

## Setting

Let \(0<c<1/2\), \(\omega\in\mathbb R\), \(U\in C^2(\mathbb R^3)\)
and \(P\in C^1(\mathbb R^3)\) solve the rotating Euler profile equation,
with \(\operatorname{div}U=0\) and \(U(y)\to0\) as \(|y|\to\infty\).
The equation makes \(\nabla P\) C1. Set
\[
 B=(cI-\omega J)y+U,\quad \Omega=\operatorname{curl}U,\quad
 a=1-2c,\quad\kappa=1+c,\quad
 \alpha=(B\times\Omega)\cdot dy,\quad
 R=\{\alpha\ne0\},\quad Z=\{\alpha=0\}.
\]
Write \(\Psi_t\) for the flow of \(-B\). Its completeness follows from
the linear growth of \(B\). Its forward orbits from a fixed compact set
stay in a common compact set: outside a sufficiently large ball,
\((-B)\cdot y\le-c|y|^2/2\).

Taking curl and applying Cartan's formula gives
\[
 \operatorname{div}B=3c,\quad [B,\Omega]=-\kappa\Omega,\quad
 d\alpha=a\,\iota_\Omega\mathrm{vol},\quad
 \alpha\wedge d\alpha=0,\quad
 \mathcal L_B\alpha=-a\alpha.
\]
Here the standard orientation is used. In particular
\[
 D\Psi_tB=B\circ\Psi_t,\quad
 D\Psi_t\Omega=e^{-\kappa t}\Omega\circ\Psi_t,\quad
 \Psi_t^*\alpha=e^{at}\alpha.                                      \tag{1}
\]
These identities also show that \(R,Z,\{\Omega\ne0\}\) are invariant.
The compact core means the set of points whose full carrier orbit is
bounded. No invariant measure or attractor is assumed to exist.

## Initial degeneracy and transported curve measures

**Statements.** The set \(Z\cap\{\Omega\ne0\}\) is Lebesgue null.
If a compact embedded C1 arc \(\gamma\subset R\) is transverse to
\(\ker\alpha\), orient it positively and set
\[
 L_0=\int_\gamma\alpha>0,\qquad
 \nu_0=L_0^{-1}d\ell_\alpha|_\gamma,\quad \nu_t=(\Psi_t)_*\nu_0.
\]
Then, with \(\gamma_t=\Psi_t\gamma\),
\[
 \ell_\alpha(\gamma_t)=e^{at}L_0,\qquad
 \nu_t={d\ell_\alpha|_{\gamma_t}\over e^{at}L_0}.                    \tag{2}
\]
The Cesaro averages \(T^{-1}\int_0^T\nu_t\,dt\) have invariant weak
subsequential limits supported on the compact core.

**Proof.** At a point of \(Z\cap\{\Omega\ne0\}\), \(d\alpha\ne0\).
Some derivative of some C1 component \(\alpha_i\) is nonzero. The
implicit function theorem puts its zero set locally in a C1
hypersurface containing \(Z\). A countable cover proves nullity.

Equation (1) proves (2) on every subarc and preserves transversality.
Trapping supplies a common compact support. For fixed \(s\ge0\), the
change of a continuous observable's average under \(\Psi_s\) is bounded
by \(2s\|h\|_\infty/T\), with the supremum taken on the relevant compact
set. Every limit is invariant under positive times, hence under the
complete group of times. Its compact support is invariant and lies in
the core.

For the Euclidean unit tangent \(\tau_t\), its density with respect to
arc length is
\[
 {|\alpha(\tau_t)|\over e^{at}L_0}.
\]
A small numerator does not make this density large. The problem is a
loss of comparison of the two lengths and of control of local pieces.
If \(M=\sup\|\alpha\|\) on the trapping compact set, (1) also gives
\(\|D\Psi_tv\|\ge e^{at}|\alpha(v)|/M\). This is a stretching bound,
not a conclusion about the conditional measures of a weak limit.

For an elementary test of closedness, take
\(\alpha_0=x\,dy-y\,dx\), positive integers \(N_n/e^{an}\to\infty\),
and \(\epsilon_n^2=e^{an}/(2\pi N_n)\). The embedded arcs
\[
 \eta_n(\theta)=(\epsilon_n\cos\theta,\epsilon_n\sin\theta,
                  \epsilon_n\theta/(2\pi N_n)),\quad
 0\le\theta\le2\pi N_n,
\]
satisfy \(\alpha_0(\eta_n')=\epsilon_n^2\), have alpha-length \(e^{an}\),
and lie in the ball of radius \(\sqrt2\epsilon_n\). Their normalized
alpha-length measures converge to the atom at zero. They are not
iterates of one flow and are not an Euler or trapping counterexample.
They only disprove the proposed closedness inference from these
geometric properties alone.

## Regular leaves and invariant probabilities

**Statements.** The connected leaves of \(\ker\alpha\) on \(R\) are
fixed by the global \(\Psi\) action. All points of one such leaf have
the same limiting Cesaro averages of continuous observables.
Every compactly supported ergodic flow-invariant probability \(\mu\)
with \(\mu(R)=1\) has Lyapunov spectrum \((a,0,-\kappa)\).
Every invariant probability carried by \(Z\cap\{\Omega\ne0\}\) is
carried by \(\{B=0\}\).

**Proof.** The C1 Frobenius theorem applies to \(\alpha\) on \(R\).
Since \(B\in\ker\alpha\), a \(\Psi\) orbit stays in its connected leaf.
The global leaf-space action is therefore the identity.
Also \(\alpha(B)=0\) but \(\mathcal L_B\alpha=-a\alpha\ne0\), so
\(\alpha\) is not a basic form descending to a fixed form on that quotient.

Let \(\Gamma_s\) be the local C1 vorticity flow. On any fixed compact
initial vorticity arc, (1) and integration in \(s\) give
\[
 \Psi_t\Gamma_sx-\Psi_tx
   =e^{-\kappa t}\int_0^s\Omega(\Psi_t\Gamma_ux)\,du .
\]
Trapping bounds the integrand uniformly for \(t\ge0\). Endpoints have
exponentially approaching orbits, hence equal limiting averages.
A fixed carrier time shift also leaves these averages unchanged.
The two vector fields span each regular leaf; their local flow
compositions give open orbits in that leaf by the inverse function
theorem. Connectedness makes a single such orbit the whole leaf.
Finite concatenation proves the assertion. Local C1 holonomy can
transfer an already established transverse almost-everywhere statement
to volume. It does not establish that transverse statement.

For the spectrum, use Oseledets regularity and recurrence on the compact
support. The vector \(B(x)\ne0\) has a well-defined exponent.
Its image \(B(\Psi_tx)\) is bounded and, along recurrent times to a
neighborhood of \(x\), bounded below. Its exponent is therefore zero.
The same argument for \(\Omega(x)\), using its factor \(e^{-\kappa t}\)
in (1), gives exponent \(-\kappa\). The vectors are independent on \(R\).
Finally \(\det D\Psi_t=e^{-3ct}\) gives the remaining exponent
\(\kappa-3c=a\). No integrability of \(\log|B|\) or \(\log|\Omega|\)
is used. Flow ergodicity does not require time-one ergodicity for this
argument.

On \(Z\cap\{\Omega\ne0\}\), write
\(B=h\Omega\), \(h=(B\cdot\Omega)/|\Omega|^2\). Equation (1) gives
\(h(\Psi_tx)=e^{-\kappa t}h(x)\). Invariance of a probability carried
there gives
\[
 \mu\{|h|>\varepsilon\}
   =\mu\{|h|>e^{\kappa t}\varepsilon\}\longrightarrow0 .
\]
Thus \(B=0\) almost everywhere for that probability. This does not
exclude empirical concentration on equilibria or on \(\{\Omega=0\}\).

## Compact regular invariant sets

**Statement.** A compact full-flow-invariant set \(\Lambda\subset R\)
is uniformly hyperbolic for the flow, with stable line
\(\mathbb R\Omega\), flow line \(\mathbb RB\), and unstable rate \(a\).
If it is additionally a basic hyperbolic attractor, the established
Bowen-Ruelle theorem gives its physical SRB measure and almost-everywhere
coverage of its attracting basin. That conditional consequence does not
assert that the core or a typical regular orbit has this structure.

**Proof of hyperbolicity.** On \(\Lambda\) put
\(N=\alpha^\sharp/\|\alpha\|^2\) and \(f=\Psi_1\).
The frame \((B,\Omega,N)\) is continuous with determinant one, so it
and its inverse are uniformly bounded. Write
\[
 DfN=\beta B\circ f+\delta\Omega\circ f+e^aN\circ f.
\]
The bounded continuous coefficients admit unique continuous solutions
\[
 p(fx)=e^{-a}(p(x)+\beta(x)),\qquad
 q(fx)=e^{-a}(e^{-\kappa}q(x)+\delta(x)),
\]
by the contraction principle after composition with \(f^{-1}\).
Thus \(W=N+pB+q\Omega\) has \(\alpha(W)=1\) and
\(DfW=e^aW\circ f\). For every real \(t\), the section
\(e^{-at}D\Psi_tW\circ\Psi_{-t}\) has the same two defining properties.
Uniqueness gives \(D\Psi_tW=e^{at}W\circ\Psi_t\).
Uniform nondegeneracy of \((B,\Omega,W)\) now proves the three claimed
uniform rates.

For the conditional SRB consequence, the attracting and transitivity
hypotheses are precisely the additional hypotheses of the source theorem,
already checked in A085. Its unstable conditional density is proportional
to alpha-length: if \(q(x)=|\alpha(e_x^u)|\) for a unit unstable vector,
then
\[
 J_t^u(x)q(\Psi_tx)=e^{at}q(x).
\]
The invariant unstable-density ratio telescopes to \(q(y)/q(x)\) on one
plaque, since backward iterates converge and \(q\) is continuous and
bounded away from zero. The source formula and its partition scope were
checked in A207 and A375. This identifies conditionals after existence.

## Open conclusion and dependencies

The compact-support spectrum does not give the entropy equality
\(h_\mu(\Psi_1)=a\). At C2 the Ledrappier-Young criterion would give
unstable absolute continuity from that equality, including the neutral
flow exponent, but no general entropy lower bound is proved here.
The initial nullity of \(Z\cap\{\Omega\ne0\}\) does not control mass of
empirical limits there. Even excluding such mass would not alone prove
the SRB property. Coverage additionally needs construction localized to
every positive-volume residual set, not just existence of one measure.

At C1 plus Hölder regularity of \(U\), \(\Omega,\alpha\) need only be
Hölder. The C1 Frobenius theorem and unique vorticity flow used here then
need new justification. Neither lower regularity nor C2 coverage is
settled by this proof.

Dependencies: the explicitly derived transport identities, compact weak
convergence, the implicit function and Frobenius theorems, recurrence,
Oseledets' theorem, and the contraction principle. Only the explicitly
conditional SRB paragraph uses Bowen-Ruelle and the invariant density
formula. Verdicts A378-A380 record the separate scopes.
