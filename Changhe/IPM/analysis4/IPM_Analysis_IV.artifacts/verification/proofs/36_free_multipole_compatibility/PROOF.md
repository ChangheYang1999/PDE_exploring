# The first free multipole can affect later compatibility

Status: finite affine compatibility and pure-potential claims confirmed by exact arithmetic. No all-order continuation is claimed.

## Statement under investigation

At delta=4/9 and c=9/5, choose a leading high odd harmonic for which the first stream resonance, at n=9 and angular frequency 2, is compatible. Its density-free stream amplitude beta is then free. The later compatibility coefficient kappa_18 is an affine function of beta. If its slope is nonzero, there is exactly one beta that cancels the obstruction at the second resonance.

## Why the dependence is affine

Give each copy of the leading density formal weight 1 and give beta weight 9. Every nonlinear recursion term adds the two input radial indices, and every nonresonant inverse preserves its index. Consequently every density coefficient of order n is a polynomial in beta with each monomial containing at least one leading density factor and having total weight n. A term of degree two in beta therefore cannot appear in a density coefficient before order 19. All density coefficients through18 are affine in beta. The same holds for the nonresonant streams through17; the free stream at9 is affine by definition.

Thus exact evaluations at beta=0 and beta=1 determine kappa_18(beta) exactly. When the slope is nonzero, beta_*=-kappa_18(0)/(kappa_18(1)-kappa_18(0)) is rational and makes the second compatibility coefficient zero. A direct exact recomputation at beta_* can independently verify the resulting finite continuation.

## Method and scope

The executable checker uses the independent Cartesian Laurent representation and checks every finite Poisson and stationary identity. At n=9 it adds beta*sin(2 theta) only after proving zero forcing in that mode. At n=18 it reports the exact density compatibility coefficient before deciding whether to invert. When that coefficient is zero, it assigns the new free stream amplitude zero and verifies the Poisson equation there as well.

This addresses the role of free harmonic terms within the prescribed pure exponent lattice. It does not assert that the original potential has no logarithmic terms, and it does not prove compatibility at every later resonance or convergence. A failure with beta fixed to zero is a weaker assertion than failure for all allowed beta.

## Completed finite calculation, 2026-10-31T03:33:48Z

For leading modes 11, 13 and 15, the affine slope is nonzero. The unique cancelling amplitudes are approximately:

| Leading density | beta_* giving kappa_18=0 |
|---|---:|
| sin(11 theta) | -0.0012503215483813702 |
| sin(13 theta) | +0.0004856228739970855 |
| sin(15 theta) | -0.0011047455853532978 |

Each exact rational beta_* was substituted into a fresh Cartesian recurrence. All density stationary identities and stream Poisson identities through order18 pass exactly, including the zero second compatibility coefficient. The new free amplitude at18 was set to zero after compatibility was established. Exact values, nonzero slopes, hashes and actual times are retained in `verification/sin11.json`, `sin13.json` and `sin15.json`.

For leading modes 17 and 19, the slope is exactly zero and the constant compatibility coefficient is nonzero. Thus neither profile can pass the second stream resonance for ANY value of the first free amplitude, within this prescribed exponent lattice. The affine-degree proof is essential: testing only beta=0 and beta=1 would not by itself exclude a nonlinear dependence.

## The original pure-potential restriction

Passing the second stream resonance by choosing beta_* does not automatically preserve a pure potential at the first resonance. At n=9 the density exponent is -3 and the potential exponent is zero. A pure S1 potential representing a compatible density is unique up to an additive constant, so its frequency-two stream amplitude is fixed.

Write D_(2k) for the cosine coefficient of Delta chi at exponent -2 and a_(2k+1) for the sine coefficient of the density at exponent -3. The exact density map gives

\[
 a_{2k+1}=(k+1)D_{2k}+kD_{2k+2},\qquad k\ge1,
\]

with a_1=2D_0=0. Descending back substitution determines D_(2k). The pure potential has cosine coefficient -D_(2k)/(2k)^2. Direct Cartesian differentiation gives

\[
 \partial_{xy}\cos(4\theta)
   =r^{-2}[6\sin(6\theta)-2\sin(2\theta)],
\]

and hence its required stream amplitude is beta_pure=D_4/8. The independent implementation reconstructs the entire pure potential at this order and verifies both its density and stream by Cartesian differentiation, rather than relying only on this formula.

| Leading density | beta_pure | kappa_18 with beta_pure |
|---|---:|---:|
| sin(11 theta) | +0.00009064985202758888 | +0.00023654182002499653 |
| sin(13 theta) | -0.00001443767313632832 | +0.000027453377835622554 |
| sin(15 theta) | +0.000009861361941132426 | +0.000010214188176019598 |

All three final coefficients are exactly nonzero. Thus these three inputs are obstructed at18 when the ORIGINAL pure-potential ansatz is enforced. Their tuned pure-density/pure-stream prefixes instead require the density-free potential correction

\[
 -(\beta_* - \beta_{\rm pure})\log r,
\]

since Delta log r=0 and partial_xy log r=-r^(-2)sin(2 theta). This correction produces the chosen pure stream without adding logarithms to the density. The files ending `_pure_chi.json` retain the exact rational values and independent checks.

The uniqueness used here does not hide an extra analytic angular kernel. If a degree-zero S1 potential has zero density, its Laplacian is independent of y and homogeneous of degree -2. Smoothness across x=0 forces that Laplacian to be zero. A periodic harmonic degree-zero potential is constant. Thus no other smooth pure angular term changes beta_pure.
