# Compact invariant measures and forced exponents

## Exact statements

Let `c>0`, let `omega` be finite, and let `U in C^2(R^3;R^3)`, `P in C^1(R^3)` solve the rotating Euler profile equation with `div U=0`. Write

\[
 B=(cI-\omega J)y+U,\quad \Omega=\nabla\times U,\quad F=B\times\Omega,
 \quad b=1+c,\quad a=1-2c.
\]

Assume uniform sublinearity `U=o(|y|)` when invoking the global flow and compact backward orbits below. Denote the B-flow by `Phi_t` and its reverse by `Psi_t=Phi_-t`.

1. Suppose `0<c<1/2` and `F(x)!=0`. There exists a compactly supported ergodic invariant probability measure for `Psi`, supported on the alpha-limit set of `x` for `Phi`, whose largest Lyapunov exponent is at least `a`. No global bound on `DU` is needed.
2. Let `mu` be any compactly supported ergodic B-invariant probability measure with `mu({B!=0})=mu({Omega!=0})=1`. The forward Lyapunov exponents, with multiplicities, are exactly

\[
                 1+c,\qquad 0,\qquad 2c-1.
\]

For the backward flow they are `-(1+c),0,1-2c`. In particular `F!=0` almost everywhere for such a measure. This second assertion is local to a compact invariant set and does not need global sublinearity.

These assertions do not imply positive metric entropy, existence of an invariant measure seeing nonzero vorticity, or nonexistence of a profile. A limiting measure produced in statement 1 may be supported on vorticity zeros or equilibria.

## Dependencies and regularity

The exact identities used are

\[
 D\Phi_t(x)B(x)=B(\Phi_t x),\qquad
 D\Phi_t(x)\Omega(x)=e^{bt}\Omega(\Phi_t x),\qquad
 \det D\Phi_t=e^{3ct}.
\]

They were derived in the foundation audit. Uniform sublinearity gives a complete flow and compact backward orbit closure. Thus `DB` is bounded on every compact orbit set used here even when it is unbounded on all of space.

We use the multiplicative ergodic theorem in this precise standard form: an invertible differentiable flow preserving a probability measure has almost-everywhere Lyapunov exponents and a vector filtration if the logarithms of the norms of the time-one derivative and its inverse are integrable; the sum of the exponents is the asymptotic logarithmic determinant. Compact support and a `C^1` vector field give these integrability assumptions. We also use weak compactness of probabilities on a compact metric space, invariance of limits of time averages, and ergodic decomposition/Birkhoff's theorem for a continuous bounded observable. No smooth invariant density or entropy formula is assumed.

## 1. A measure recording backward stretching

The cross-product identity for a linear isomorphism, combined with the three exact identities above, gives

\[
 F(\Phi_t x)=e^{-at}D\Phi_t(x)^{-T}F(x).
\]

For the reverse flow this is

\[
 D\Psi_t(x)^T F(\Psi_t x)=e^{at}F(x).
\]

Let `K_x` be the compact closure of the backward orbit and put `M=max_(K_x)|F|`. For `F(x)!=0`, this positive finite number gives

\[
 \|D\Psi_t(x)\|\ge e^{at}|F(x)|/M\qquad(t\ge0).       \tag{1}
\]

For each `T>0`, choose a unit vector `v_T` attaining the operator norm of `D Psi_T(x)`. Let the normalized tangent flow be

\[
 \widehat\Psi_t(z,v)=
 \left(\Psi_t z,\frac{D\Psi_t(z)v}{|D\Psi_t(z)v|}\right),\qquad |v|=1.
\]

It is well-defined and continuous. Its infinitesimal logarithmic length change is the continuous observable

\[
 g(z,v)=-v\cdot DB(z)v.
\]

Indeed the variational equation is `w'=-DB(Psi_t z)w`, so

\[
 \int_0^T g(\widehat\Psi_t(x,v_T))\,dt
       =\log|D\Psi_T(x)v_T|\ge aT+\log(|F(x)|/M).       \tag{2}
\]

Form the empirical probabilities of these tangent-flow segments, of length `T`. They are supported on the compact set `K_x times S^2`. Any weak limit along `T->infinity` is invariant: for each fixed time shift the difference of the two time averages is bounded by the two endpoint intervals divided by `T`. The changing initial vector does not affect this endpoint estimate. Its base projection is supported on the alpha-limit set, because the base orbit eventually lies in every neighborhood of that set.

By (2), the limit `nu` satisfies `integral g dnu>=a`. Ergodic decomposition gives an ergodic component `nu_*` with `integral g dnu_*>=a`. Its base projection `mu_*` is ergodic and invariant. Birkhoff's theorem and the logarithmic-length identity show that the derivative grows along the selected unit vector with exponent `integral g dnu_*` at almost every point of this tangent measure. The largest derivative exponent over the base measure is therefore at least `a`. All measures remain supported over the stated compact alpha-limit set.

## 2. Exact spectrum of a nonstationary vortical invariant measure

The sets `{B=0}` and `{Omega=0}` are invariant, by the exact transport identities. Under the hypotheses of statement 2, both transported vectors are nonzero almost everywhere.

Choose a point regular for the multiplicative ergodic theorem and recurrent for the time-one map. It can be chosen so that the orbit returns infinitely often to a compact positive-measure set on which `|B|` and `|Omega|` are bounded below. Such a set exists by the assumed almost-everywhere nonvanishing and compact support. Poincare recurrence and a countable covering supply this property for almost every point.

Compactness bounds both vector fields above along the orbit. The exact identities then imply, at recurrent times `n_j`,

\[
 \frac1{n_j}\log|D\Phi_{n_j}B(x)|\longrightarrow0,\qquad
 \frac1{n_j}\log|D\Phi_{n_j}\Omega(x)|\longrightarrow b.
\]

The full Lyapunov limits of these vectors exist at a regular point; hence their exponents are exactly `0` and `b`. They cannot be parallel because `b>0` and a nonzero vector has only one exponent. Thus `F!=0` almost everywhere.

The sum of the three exponents is `3c`, since the determinant is exactly `exp(3ct)`. Two of them have already been identified with independent vectors as `0` and `b`. The third is `3c-b=2c-1`. For `0<c<1/2` all three are distinct; for the broader `c>0` statement the same computation holds with multiplicities even if two numerical values coincide. Reversing an invertible flow negates the exponents.

## Scope and the unresolved step

A nonzero Lebesgue-measure vortical region gives points with `F!=0`, by A027, and therefore at least one compact invariant measure with the backward growth in statement 1. This does not ensure that the measure itself gives positive mass to `{Omega!=0}`. Even statement 2's positive backward exponent does not imply positive entropy without further hypotheses. No Pesin entropy equality, invariant density, hyperbolicity of the entire limit set, or classification of alpha-limits has been inserted.
