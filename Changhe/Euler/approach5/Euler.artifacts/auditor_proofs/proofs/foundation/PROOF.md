# Exact identities and the limits of the elementary flow argument

Status: independently checked. Each numbered result below has the scope stated here. None alone proves the main rotating Liouville conjecture.

## Statement and hypotheses

Let `c > 0` and `omega` be finite real constants. Let `U` be a `C^2` vector field on `R^3`, let `P` be `C^2`, and suppose

\[
 (1-c)U+(B\cdot\nabla)U+\omega JU+\nabla P=0,
 \qquad \nabla\cdot U=0,
\]

where

\[
 J=\begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix},\quad
 A=cI-\omega J,\quad B=Ay+U,\quad X=cy+U,\quad
 \Omega=\nabla\times U,\quad q=\tfrac12|U|^2.
\]

Write `G = DU`, with entries `G_ij = partial_j U_i`, and `S = (G+G^T)/2`.

Results 1 to 5 are local identities and need no decay or pressure normalization. Results 6 to 8 assume in addition that `U(y)=o(|y|)` uniformly at infinity. The target assumption `U(y) -> 0` implies this. Result 9 explicitly assumes an additional global flux condition. All results allow arbitrary finite `omega` and impose no symmetry.

## 1. Pressure equation

Taking divergence gives

\[
 -\Delta P=\partial_iU_j\,\partial_jU_i
           =\partial_i\partial_j(U_iU_j).
\]

Indeed, the divergence of the transport term is

\[
 \partial_iB_j\,\partial_jU_i
 =c\partial_iU_i-\omega J_{ji}\partial_jU_i
  +\partial_iU_j\partial_jU_i.
\]

The first summand vanishes. Relabeling indices in the second shows that it cancels `div(omega J U)`. No integration by parts at infinity has been used. The Poisson equation alone determines pressure only up to a harmonic function. For a fixed exact `U`, the full momentum equation also fixes `grad P`; one may not add a nonconstant harmonic pressure and keep the same solution.

## 2. Vorticity equation and Cauchy formula

Taking curl, including both rotation terms, gives

\[
 \Omega+(B\cdot\nabla)\Omega-(\Omega\cdot\nabla)U
       +\omega J\Omega=0.                                      \tag{2.1}
\]

The linear rotational operator `JU-(Jy dot grad)U` is the infinitesimal rotation action on vector fields; curl commutes with that action. The scaling term contributes `c Omega`, which combines with `(1-c)Omega` to give the first term in (2.1). The usual divergence-free nonlinear curl identity gives the two nonlinear terms.

If `Phi_s` denotes a defined interval of the `B` flow, then

\[
 D\Phi_s(a)\,\Omega(a)=e^{(1+c)s}\Omega(\Phi_s(a)).               \tag{2.2}
\]

To check this, differentiate the right side using (2.1). Its derivative is
`(cI-omega J+G) e^{(1+c)s}Omega(Phi_s(a))`, which is exactly the variational equation for `DPhi_s(a)Omega(a)`, with the same initial value. Equivalently,

\[
 [B,\Omega]=-(1+c)\Omega.                                      \tag{2.3}
\]

The antisymmetric part of `G` is the map `v -> Omega cross v/2`, so it annihilates `Omega`. Dotting (2.1) with `Omega` therefore yields

\[
 \tfrac12 B\cdot\nabla|\Omega|^2
   =\Omega\cdot S\Omega-|\Omega|^2.                            \tag{2.4}
\]

At any critical point of `|Omega|^2` with nonzero vorticity, the directional stretching quotient is exactly one. Existence of a global maximum of vorticity does not follow from velocity decay alone.

## 3. Rotating Bernoulli identity

Define

\[
 H=P+\tfrac12|X|^2+\tfrac{c(c-1)}2|y|^2-\omega(Jy)\cdot X.
\]

Then

\[
 (1-2c)X+\Omega\times B+\nabla H=0,                            \tag{3.1}
\]

and

\[
 B\cdot\nabla H=(2c-1)X\cdot B.                               \tag{3.2}
\]

For a direct coefficient check, expand

\[
 H=P+q+c\,y\cdot U+\tfrac{c(2c-1)}2|y|^2-\omega(Jy)\cdot U.
\]

Differentiation gives

\[
 \nabla H=\nabla P+G^TB+cU+\omega JU+c(2c-1)y.
\]

Since `Omega cross B = (G-G^T)B`, adding the other terms in (3.1) reproduces the momentum equation exactly. Dotting with `B` proves (3.2). In particular,

\[
 X\cdot B=|X|^2-\omega(Jy)\cdot U.
\]

The final term has no fixed sign. In contrast, for `omega=0` and `c<1/2`, (3.2) is the strict Lyapunov identity `B dot grad H = -(1-2c)|B|^2`.

## 4. Circulation and vorticity flux

Let `C_0` be a closed piecewise `C^1` loop, and let `C_s=Phi_s(C_0)`. Then

\[
 \frac{d}{ds}\oint_{C_s}U\cdot d\ell
       =(2c-1)\oint_{C_s}U\cdot d\ell.                        \tag{4.1}
\]

The derivative of a line integral transported by `B` has integrand
`GU+(...)` only if the transport field equals `U`; here the correct integrand is

\[
 GB+(DB)^TU
 =[-(1-c)U-\omega JU-\nabla P]
   +[cU+\omega JU+G^TU]
 =(2c-1)U+\nabla(q-P).
\]

The gradient integrates to zero on the closed loop. Thus circulation scales by `exp((2c-1)s)`. Stokes' theorem gives the same scaling for vorticity flux through transported compact orientable surfaces. No outer boundary or pressure normalization is involved.

If a periodic `B` orbit has period `T>0`, transporting its oriented geometric loop for time `T` returns the loop to itself. For `c != 1/2`, (4.1) forces its `U` circulation to be zero. This does not force the loop to have zero length or force `B` to vanish there.

## 5. Local energy balance and radial cutoff

The scalar product of momentum with `U` gives

\[
 \nabla\cdot(qB+PU)+(2-5c)q=0.                                \tag{5.1}
\]

Here `div B=3c`, `div U=0`, and `U dot JU=0`. For every compactly supported `C^1` scalar cutoff `phi`,

\[
 (2-5c)\int q\phi=\int(qB+PU)\cdot\nabla\phi.                 \tag{5.2}
\]

For radial `phi`, `(Jy) dot grad phi=0`. This removes rotation from the explicit cutoff flux, but it does not remove the nonlinear or pressure fluxes. For every positive radius, the divergence theorem yields

\[
 (2-5c)\int_{B_R}q
  =-\int_{\partial B_R}(qB+PU)\cdot n.
\]

No sign can be assigned to the pressure flux from the Poisson equation alone.

## 6. Completeness, backward trapping and limit sets

Assume `U=o(|y|)` uniformly. Then `|B(y)| <= C(1+|y|)` for a finite constant depending on `c`, `omega` and `U`. Local existence and uniqueness follow from `B in C^1`. Gronwall's inequality prevents finite-time escape in both time directions, so `Phi_s` is defined for all real `s` and is a `C^1` diffeomorphism with inverse `Phi_-s`. A global bound on `DU` is not needed.

Choose `R_0` sufficiently large that `|U(y)| <= c|y|/2` for `|y| >= R_0`. Since `(Jy) dot y=0`,

\[
 B(y)\cdot y\ge (c/2)|y|^2\quad (|y|\ge R_0).                 \tag{6.1}
\]

Every backward trajectory enters `closed B_R0` in finite backward time and stays there. Indeed, while outside, its radius in backward time satisfies `r' <= -cr/2`; (6.1) also makes the ball invariant for backward time. Consequently every alpha-limit set is nonempty, compact, connected and fully invariant. Connectedness follows by expressing the limit set as the decreasing intersection of the compact connected closures of backward orbit tails.

The field has at least one zero. On a sufficiently large sphere the homotopy `Ay+tU`, `0<=t<=1`, has positive scalar product with the outward radius and hence no zero there. Its degree is that of `A`, namely `sign det A=+1`, so it has a zero inside. This last conclusion could equivalently be obtained from the usual outward-vector-field version of Brouwer's theorem.

## 7. Compact invariant core and its zero volume

For any radius `R` satisfying (6.1), set

\[
 K=\bigcap_{t\ge0}\Phi_{-t}(\overline B_R).
\]

The sets in the intersection are nonempty nested compact sets. A point belongs to `K` exactly when its entire forward orbit stays in `closed B_R`. Any forward orbit that leaves this ball escapes to infinity by (6.1). Thus `K` is precisely the set of points having bounded forward orbit; it is compact and fully invariant, and it does not depend on the chosen sufficiently large radius. Every alpha-limit set is contained in `K`.

Jacobi's formula for the variational equation gives

\[
 \det D\Phi_s(a)=e^{3cs}.
\]

Therefore

\[
 |K|\le |\Phi_{-t}(\overline B_R)|=e^{-3ct}|B_R|,
\]

for every `t>=0`, and `K` has three-dimensional Lebesgue measure zero.

This is a statement about the invariant core, not its backward basin. All points have bounded backward trajectories, so the basin of the core under backward time is the whole space. Confusing these two sets invalidates a nonexistence argument.

## 8. Positive divergence and decay do not exclude periodic orbits

This is a counterexample to an auxiliary dynamical inference, not an Euler profile.

Fix `c>0`, `omega != 0`. Choose a smooth compactly supported cutoff `chi` equal to one on a ball of radius two. Define a vector potential

\[
 a(y)=\chi(y)(-c y_2y_3,\ c y_1y_3,\ 0),\qquad U=\nabla\times a.
\]

Then `U` is smooth, compactly supported and divergence-free. On the ball of radius two it is

\[
 U=(-cy_1,-cy_2,2cy_3).
\]

Hence on the unit circle in `y_3=0`,

\[
 B=cy-\omega Jy+U=-\omega Jy,
\]

which has that circle as a nonconstant periodic orbit of period `2pi/|omega|`. Globally `div B=3c`, `U -> 0`, and all the flow conclusions of results 6 and 7 apply. The construction is not claimed to solve the momentum equation; it shows exactly why the flow conclusions alone cannot supply the missing Euler rigidity.

## 9. What the finite-energy identity actually requires

Suppose additionally `U in L^2(R^3)` and the cutoff flux in (5.2) tends to zero for a fixed standard family `phi_R(y)=phi(y/R)` with `phi=1` near the origin. Then dominated convergence gives

\[
 (1-\tfrac52c)\int_{\mathbb R^3}|U|^2=0.
\]

Thus `U=0` for `c != 2/5`. The flux condition is part of this statement. A sufficient familiar package is bounded `U`, `U in L^2`, and `P-P_0 in L^2` for some constant: the linear radial flux is bounded by a constant times the annular `L^2` tail, the cubic flux by `C R^-1 ||U||_infinity` times that tail, and the pressure flux by `C R^-1 ||P-P_0||_2 ||U||_2`. The constant pressure has zero cutoff work because `div U=0`.

Neither `U in L^2` nor this pressure package follows just from `U -> 0` by the arguments above. Any later proof of either implication must be recorded separately.

## Dependencies and verification

Only differentiation, the divergence and Stokes theorems on compact sets, local ODE existence/uniqueness, Gronwall, the variational equation, elementary degree theory and measure change of variables are used. No external Liouville theorem or pressure representation is assumed. These are analytic proofs, not formal Lean verification. The audit ledger lists the exact approved scopes.

## 10. Helicity and axial angular momentum

The following identities need only the original local smoothness and exact equation. Write `h=U dot Omega` and `M=(Jy) dot U`, and use `partial_theta P=(Jy) dot grad P`. Then

\[
 B\cdot\nabla h=(c-2)h+\Omega\cdot\nabla(q-P),
\]

\[
 \operatorname{div}\big(Bh-(q-P)\Omega\big)=(4c-2)h.          \tag{10.1}
\]

To verify the first line, differentiate `U dot Omega` along `B` and substitute both the velocity and vorticity equations. The two skew-rotation terms cancel, the two damping terms sum to `(c-2)h`, and `U dot (Omega dot grad)U=Omega dot grad q`. The second line follows from `div B=3c` and `div Omega=0`.

Likewise,

\[
 B\cdot\nabla M=(2c-1)M-\partial_\theta P,
\]

\[
 \operatorname{div}(BM+PJy)=(5c-1)M.                         \tag{10.2}
\]

Indeed, differentiating the factor `Jy` gives `(JB) dot U`. Its rotational contribution cancels the term `-omega (Jy) dot JU` from momentum, and its scaling contribution is `cM`. Since `div(Jy)=0`, the pressure term has the divergence form shown. On every sphere `Jy` is tangent, so

\[
 \int_{\partial B_R}(cR+U\cdot n)M
     =(5c-1)\int_{B_R}M.
\]

The corresponding finite-ball helicity identity retains the full boundary flux from (10.1). Neither identity is a global integral theorem without an additional justified boundary limit.

## 11. Similarity-flow invariant measures

If `c!=1/2` and `mu` is a probability measure with compact invariant support for the `B` flow, invariance and the Bernoulli identity give

\[
 \int X\cdot B\,d\mu=0,
 \qquad
 \int|X|^2\,d\mu=\omega\int (Jy)\cdot U\,d\mu.               \tag{11.1}
\]

Differentiate invariance of `integral H(Phi_s y) dmu` at `s=0`; all derivatives are bounded on a compact neighborhood of the support. Divide by `2c-1`. The algebraic formula for `X dot B` proves the second equality. At `c=1/2`, the Bernoulli identity alone does not give (11.1).

These are identities for `B`-invariant measures. They are distinct from the `Omega`-invariant mean-action identity proved in the team records.
