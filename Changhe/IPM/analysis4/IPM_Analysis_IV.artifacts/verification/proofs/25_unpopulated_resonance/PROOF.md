# A first resonance whose forcing mode is not populated

Status: proved support selection rule; a finite exact example is checked separately. First-resonance compatibility is not an all-order existence or convergence theorem.

## Statement

Let `delta` be rational and let its first stream resonance occur at an odd order `n_0`. Put `m_0=n_0 delta-3`, the positive odd density frequency tested by compatibility. For any odd integer

\[
 M>m_0+n_0-1=n_0(1+\delta)-4,
\]

start from `f_1=sin(M theta)`. Then the uniquely defined density recursion through order `n_0` has zero coefficient at frequency `m_0`. Thus the first stream resonance is compatible, despite its zero Poisson denominator.

For example, at `delta=4/9`, `c=9/5`, the first stream resonance is `n_0=9`, `m_0=1`. The nontrivial datum `f_1=sin(11 theta)` has zero compatibility coefficient at that resonance. This contrasts with the nonzero coefficient for `sin(theta)` at exactly the same parameter.

## Support induction

Use complex signed angular frequencies. Define

\[
 S_n=\{M(s_1+\cdots+s_n)+(t_1+\cdots+t_{n-1}):
              s_a,t_b\in\{-1,1\}\}.
\]

For `n=1`, the Fourier support of `sin(M theta)` is contained in `S_1={-M,M}`. Cartesian differentiation in the Poisson forcing shifts angular frequencies by one in either direction. The nonresonant Poisson inverse itself preserves frequencies. Therefore if `f_i` has support in `S_i`, its stream has support in `S_i+{-1,1}`.

Angular derivatives do not change support, and multiplication adds frequencies. The nonlinear density product of orders `i` and `j`, where `i+j=n`, consequently has support in

\[
 S_i+S_j+\{-1,1\}\subseteq S_n.
\]

The recursion divides by a scalar and sums such products, so `f_n` has support in `S_n`. This induction applies through `n_0`: computing `f_(n_0)` only uses preceding, nonresonant streams.

When `n_0` is odd, the sum of the `n_0` signs `s_a` is an odd integer with absolute value at least one. The remaining sum has absolute value at most `n_0-1`. Every frequency in `S_(n_0)` therefore has absolute value at least `M-(n_0-1)>m_0`. The tested coefficient vanishes identically. Topic 03 then gives compatibility of the stream equation.

## Scope and potential qualification

The first stream harmonic is free at a compatible resonance. Different choices can affect subsequent orders. Moreover, a pure potential representation can impose an additional normalization of that harmonic; polynomial logarithmic potentials can realize a general choice as in topic 10. No such choice or continuation is asserted by this support argument.

The result proves that zero denominators alone are insufficient to infer obstruction, even for nonzero real finite sine-polynomial data. It does not contradict the finite `sin(theta)` scan and does not settle the density hypothesis in the conditional divergence theorem.

## Finite evidence

The exact Cartesian/Laurent engine of topic 24 recomputes orders one through nine for the stated `sin(11 theta)` example. It extracts the compatibility coefficient and Poisson forcing without dividing at order nine. The full final density polynomial and exact zeros are retained in `verification/sin11_delta4_9.json`. The proof itself is the support induction above, independent of the finite computation.
