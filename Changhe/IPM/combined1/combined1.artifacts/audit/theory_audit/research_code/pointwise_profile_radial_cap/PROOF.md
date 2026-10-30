# Complete radial-integral ceiling with coefficient93/250

## Exact conditional statement

Use precisely the canonical stationary endpoint setting and the
three exact references of T4-414, whose standalone proof is copied
in source/T4_414_PROOF.md. Thus c>1, q=1/c-4, delta=1-1/c,
D=5c-1, H=H_q(h)>=H0, G>=g0=Theta0'(0)>0, and the full-circle
endpoint projection norm is B>0. Set E=93/250. Suppose the CI error
majorant contains H E G r^-delta/D on its whole integration region.
Ignore every other nonnegative error term and take V=0. This assumes
a zero finite-radius remainder and is deliberately favorable.

Define alpha=-2q-2 and

 S=2delta^2/[alpha(alpha+delta)(alpha+2delta)],
 r0=[sqrt(2pi) H0 E g0/(D B)]^(1/delta).

For every starting radius R>=0, the square root of the CI integral
is at most

 cap=B r0^(q+1) sqrt(S).                                (1)

The result is an upper ceiling on what this necessary-distance test
could certify with that sufficient majorant. Passing a target is
not existence, an inverse, or a achieved exclusion. In particular
the unknown H upper budget, finite-radius remainder, and the other
reference errors remain unresolved. The profile coefficient93/250
is proved by T4-415's finite rectangle certificate, whose independent
review is tracked separately. Formula(1) is a conditional arithmetic
specialization and does not need to assume that review is complete.

## Complete argument

The nonnegative error term and H>=H0,G>=g0 give
sqrt(2pi)ehat(r)>=B(r0/r)^delta. The CI integral is therefore at
most B^2 times the integral from r0 to infinity of
[1-(r0/r)^delta]^2 r^(2q+1). Substitute r=r0u and integrate
its three powers. The bracket is
1/alpha-2/(alpha+delta)+1/(alpha+2delta)=S. This proves(1).
The choice of R=0 only enlarges the domain; a positive R and further
error terms can only reduce it.

## Exact specialization and verification

The stored c, exact endpoint maps, g0 and pointwise angles are those
already checked in380/414. Use H0=999775,999745,999748 for007,013,014,
respectively, after recomputing the pointwise lower bound Phi and
checking H0<Phi by Arb. Reconstruct B by exact sine orthogonality.
For each of the four exact targets beta, compare cap/beta with1
and give a rational enclosing interval for cap and cap/beta.
Also recompute the threshold

 Ecrit=D B/[sqrt(2pi)H0 g0] [B sqrt(S)/beta]^(delta/(-q-1)).

Its comparison with93/250 must agree with cap/beta's comparison.
Only outward interval comparisons are accepted; display decimals
are not substituted for exact JSON data. All inputs and proof text
are bound before the checker runs, with real execution times recorded.
