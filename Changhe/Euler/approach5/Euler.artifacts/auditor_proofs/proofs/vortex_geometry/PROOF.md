# Restrictions on the frozen vorticity flow

## Exact statement

Let `c>0`, `omega in R`, and let `U in C^2(R^3;R^3)`, `P in C^2(R^3)` solve the rotating profile equation, with `div U=0` and uniform `U=o(|y|)`. Write

\[
 B=(cI-\omega J)y+U,\qquad \Omega=\nabla\times U.
\]

Consider the autonomous frozen vorticity field `Omega`, not the field `B`.

1. `Omega` has no nonconstant periodic integral curve.
2. On every compact set invariant under the full frozen vorticity flow, that flow has zero topological entropy.
3. For every invariant probability measure of the frozen vorticity flow having compact invariant support,

\[
 \int U\cdot\Omega\,d\mu=0.
\]

All three statements hold for every finite `omega`, with no symmetry or pressure normalization. They verify and apply the mechanisms of Section 8 of the Liu manuscript to the target rotating equation. They do not imply that `Omega=0`, nor do they exclude chaos or recurrence for the similarity flow `B`.

## Flow distinction and dependencies

Let `Phi_s` be the complete `B` flow, whose existence and uniform backward confinement on compact sets were proved in the team records. Let `psi_t` be the local flow of `Omega`. At this stage of the argument only its local existence is used; on a compact invariant set its restricted flow is complete. Subsequent result A048 proves global completeness from the full bracket equation and sublinear velocity. Thus this early proof does not leave global completeness as a standing open issue; derivative boundedness is not needed for that later result.

The exact Cauchy formula is

\[
 D\Phi_s(x)\Omega(x)=e^{(1+c)s}\Omega(\Phi_s x).                \tag{1}
\]

By uniqueness of integral curves, wherever both sides are defined,

\[
 \Phi_s\circ\psi_t=\psi_{e^{(1+c)s}t}\circ\Phi_s.             \tag{2}
\]

Thus a compact complete vorticity orbit or invariant set is carried to another such set by every `Phi_s`.

## 1. No regular closed vortex line

Suppose `x(t)` is a nonconstant periodic solution of `x'=Omega(x)` with period `T>0`. Fix `L>0`. Formula (2) sends its image under `Phi_-nL` to a nonconstant periodic vorticity orbit with period

\[
 T_n=e^{-(1+c)nL}T.
\]

Uniform backward confinement puts all these curves in one closed ball `D`. Since `Omega in C^1`,

\[
 M=\sup_D\|D\Omega\|<\infty.
\]

Every nonconstant periodic vorticity orbit in `D` has period at least `2pi/M` when `M>0`. Indeed, its velocity `v=x'` has mean zero, is periodic, and satisfies `v'=D Omega(x)v`. The periodic Wirtinger inequality gives

\[
 \int_0^T|v|^2
 \le\left(\frac{T}{2\pi}\right)^2\int_0^T|v'|^2
 \le\left(\frac{TM}{2\pi}\right)^2\int_0^T|v|^2.
\]

The last integral is positive. If `M=0`, the same inequality immediately forbids a nonconstant periodic orbit. Since `T_n->0`, either case is a contradiction.

No circulation sign or pressure condition was used.

## 2. Zero entropy on compact frozen-vorticity invariant sets

Let `K` be compact and invariant under every `psi_t`, and put `K_n=Phi_-nL(K)`. These sets are compact, invariant, and contained in one fixed ball `D`. Rearranging (2), the flow on `K_n` is conjugate to the flow on `K` accelerated by

\[
 c_n=e^{(1+c)nL}.
\]

Consequently

\[
 h_{\rm top}(\psi_1|K_n)=c_n h_{\rm top}(\psi_1|K).           \tag{3}
\]

Here entropy is that of the time-one map, equivalently the continuous-time separated-orbit definition. Time acceleration multiplies entropy because the orbit-metric time interval `[0,T]` becomes `[0,c_n T]`; conjugacy preserves entropy by uniform continuity of the two maps on their compact domains.

On the convex ball `D`, the derivative bound `M=sup_D||D Omega||` yields

\[
 |\psi_t x-\psi_t y|\le e^{Mt}|x-y|
\]

for `x,y` in any `K_n` and `t>=0`. Cover `K_n` by occupied cubes of side `epsilon e^-MT/sqrt(3)`, taking one point in each. This is an `epsilon` spanning set for the orbit metric up to time `T`, of size at most

\[
 C_D(1+\epsilon^{-1}e^{MT})^3.
\]

Thus all the left sides in (3) are bounded by `3M`, uniformly in `n`. Since `c_n->infinity`, the entropy on `K` must be zero.

This argument permits nonempty aperiodic invariant sets of zero entropy. It does not classify them.

## 3. Vanishing invariant mean action

Write `alpha=U dot dy`, `a=1-2c`, and `b=U dot Omega`. The one-form version of the verified circulation identity is

\[
 \mathcal L_B\alpha+a\alpha=d(q-P),\qquad q=|U|^2/2.
\]

For `F=Phi_L`, integration gives a globally defined `C^1` function `G` such that

\[
 F^*\alpha=r\alpha+dG,\qquad r=e^{-aL}.
\]

Set `C=e^{(1+c)L}`. Evaluation on `Omega`, using (1), gives

\[
 C b(Fx)=r b(x)+\Omega(x)\cdot\nabla G(x).                    \tag{4}
\]

Let `mu` have compact invariant support `K` and be invariant under `psi_t`. Put `mu_n=(Phi_-nL)_*mu`. By (2), each `mu_n` is also vorticity-flow invariant. Its support `K_n` lies in the same fixed compact ball. Differentiating invariance of the integral of `G` is legitimate on this compact support and gives

\[
 \int \Omega\cdot\nabla G\,d\mu_n=0.
\]

Integrating (4) therefore yields

\[
 \int b\,d\mu_n=(C/r)^n\int b\,d\mu
               =e^{(2-c)nL}\int b\,d\mu.                    \tag{5}
\]

For `0<c<2`, the boundedness of `b` on the common ball forces the initial integral to vanish.

To obtain every other positive `c`, use the rotating Bernoulli identity from the foundation proof. With `X=cy+U`, it gives

\[
 \Omega\cdot\nabla H=-(1-2c)X\cdot\Omega.
\]

Both `H` and `|y|^2/2` can be differentiated under the invariant integral on the compact support. Hence

\[
 0=-(1-2c)\int X\cdot\Omega\,d\mu,
 \qquad \int y\cdot\Omega\,d\mu=0.
\]

For `c!=1/2` this directly gives `integral U dot Omega=0`. The remaining value `c=1/2` is already covered by (5). This proves the claim for all `c>0` and all finite rotations.

For `c!=1/2`, this last direct argument actually needs no far-field growth condition: compact support of the invariant measure suffices. Sublinear growth remains part of the common theorem statement because it is used in the other assertions and in the critical case.

## Scope checks

The compact support condition is essential to each boundedness and differentiation argument presented here. The measure is invariant under `Omega`, not merely under `B`. A vortex-line invariant measure is different from whole-space volume measure and from a particle invariant measure. The conclusion is a mean-action identity, not pointwise vanishing of helicity density.

If `U dot Omega` has one strict sign on a nonempty compact vorticity-flow invariant set, an invariant probability obtained by time averaging contradicts statement 3. This is a conditional obstruction. It does not prove that every nonzero profile has such a set.
