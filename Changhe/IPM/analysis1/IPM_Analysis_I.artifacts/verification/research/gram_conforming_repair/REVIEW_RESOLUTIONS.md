# Final review resolutions and precise norm binding

The first actual Claude Opus 5.5 review accepted the repair, interval
directions, independence and limited conclusion. Its remaining dependency
was the precise definition of X. The frozen definition is in
research/gram_internal_jumps/SOURCE_BINDING.md and is pinned by that topic's
verdict. Here it is explicit:

    ||h||_X^2 = integral (h^2+r^2|grad h|^2) w(r) dX,
    w(r) = m(r)^(-2)(1+r^2/L^2)^(-3/2),
    m(r) = (r/L)^3(1+r^2/L^2)^((k-3)/2).

The gradient is the distributional weak gradient. Broken energy uses the
same integral with the piecewise classical derivatives instead. The
original discontinuous functions generally have only the latter.

For h=r^3 B(log r) Phi(theta), its radial derivative is
r^2(3B+B')Phi and its angular component is r^2 B Phi'. Thus h^2 and
r^2|grad h|^2 each have the factor r^6. The polar area measure becomes
r^2 dt dtheta, so the common radial factor is

    r^8 w(r) = L^6 r^2(1+r^2/L^2)^(3/2-k) = L^6 W(log r).

Indeed the r exponent is 8-6=2 and the other exponent is
(3-k)-3/2=3/2-k. These exact identities and the definition's frozen pin
are checked in evidence/norm_linkage.json. For every fixed integer m,
Phi_m=cos^2(theta)sin(theta)cos(2m theta) is nonzero on a sufficiently small
positive arc, so A0 is strictly positive. The common denominator factor
A0+A1 is therefore positive before cancellation. No bound on m is needed.

The ADDENDUM table contains literal vertical bars in two cell labels,
which can disrupt Markdown rendering. Its numerical text is unchanged.
This correctly formatted table is authoritative for those labels:

| Quantity | M16 | M24 |
| --- | ---: | ---: |
| Single-column relative broken energy error | 8.447e-15 | 2.5676e-14 |
| Coefficient sup error | 1.98e-16 | 1.8e-16 |
| Piecewise t-derivative sup error | 3.752e-15 | 1.2642e-14 |

Every ceiling is a strict exact rational upper bound. The two engines
independently check all 4432 repaired traces and all 277 column bounds.
The first review, raw response and original reviewed files remain intact.
The formula defines 1440 and 4488 independent continuous functions in X
in the two NEW repaired spaces. It does not supply a relative operator
bound on arbitrary linear combinations. In particular it does not move
the old floating Gram spectrum to a rigorous spectrum in X. Derivative
jumps can remain, and no C1 or smoothness assertion is made. The full
operator, normalization, inverse and nonlinear closure remain OPEN.
