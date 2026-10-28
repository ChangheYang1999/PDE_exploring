# Quadratic localization of the lower-clamp correction

## Statement

Use the real homogeneous Holder space, kernel, projection witness, parameters
and notation of ../PROOF.md. In particular 0<a<1, b>0, lambda>0,
lambda[P]_a<=1, and the pole disk has radius 0<epsilon<1/2. Retain the two
active-profile hypotheses

    (lambda+2^(a-1)) epsilon^a <= c+1/2,
    lambda epsilon^a <= 1/2.                              (1)

Define

    C_e=(1-2epsilon)^(a-1),
    A(a)=Gamma(1+a/2)/(2sqrt(pi) Gamma(3/2+a/2)),
    M=lambda A(a) epsilon^a/a+epsilon^2/4,
    E_c=a C_e^3 epsilon^(3-2a)/(6pi lambda^2(3-2a)),
    E_s=epsilon^(a+2)/[(a+2)(1-epsilon)^2].              (2)

Assume additionally

    a C_e epsilon^(1-a) <= lambda/2.                    (3)

Then the own-pole lower-clamp correction is nonpositive and has magnitude
at most E_c. The complete integral J_e defined in the parent proof satisfies

    M-E_c-E_s <= J_e <= M+E_s.                           (4)

Both pole disks contribute 2J_e to the increment integral I0. The diagonal
identity contribution of R_1^2 remains -I/2, with the sign selection already
proved in the parent witness theorem. No numerical lower bound is claimed
here before checking the parameters and the finite annular integrals.

## Complete proof

The parent proof derives on the disk, for r=|u|,

    f(e+u)=-1/2+lambda P(u)+d(u),
    d(u)=(1/2-h(e+u)-lambda P(u))_+,
    h(e+u)=(1+2u_1)^a/2.

Since P>=0 and h>=1/2 when u_1>=0, d vanishes on that half disk. For u_1<0,
put t=-u_1/r. The mean value theorem gives

    1/2-h(e+u) <= a C_e r t.                            (5)

If |u_1|>=|u_2|, then the projection profile obeys P(u)>=r^a/2. Therefore

    1/2-h(e+u)-lambda P(u)
      <=a C_e r-lambda r^a/2 <=0

by (3), since r^(1-a)<=epsilon^(1-a). Thus the correction can occur only
where |u_1|<|u_2| and u_1<0. On this set 0<t<1/sqrt(2), the kernel K(u)
is negative, and

    P(u)=r^a[1-(1-2t^2)^a]/2 >= a r^a t^2.             (6)

The inequality follows from concavity: s^a<=1+a(s-1), applied at
s=1-2t^2 in [0,1]. Combining (5) and (6) gives

    0<=d(u)<=a(C_e r t-lambda r^a t^2)_+.               (7)

For each fixed radius the possible clamp support has two symmetric arcs.
Their angular change of variable is dtheta=dt/sqrt(1-t^2), while
|cos(2theta)|=1-2t^2. Hence, with the radial area element included,

    -integral_(|u|<epsilon) K(u)d(u) du
      <= (a/pi) integral_0^epsilon (dr/r)
          integral_0^(1/sqrt(2))
            [(1-2t^2)/sqrt(1-t^2)]
            (C_e r t-lambda r^a t^2)_+ dt.

For 0<=t<=1/sqrt(2), the bracketed factor is nonnegative and at most one:
1-2t^2<=1-t^2<=sqrt(1-t^2). The positive part of the quadratic vanishes
for t>=s_r=C_e r^(1-a)/lambda. Extending its nonnegative integration
range to [0,s_r] therefore gives the upper bound

    (a/pi) integral_0^epsilon (dr/r)
          [C_e r s_r^2/2-lambda r^a s_r^3/3]
       = (a C_e^3/(6pi lambda^2))
          integral_0^epsilon r^(2-2a) dr
       = E_c.

The integral is finite because 3-2a>1. The sign of K on the support gives
simultaneously

    -E_c <= integral_(|u|<epsilon) K(u)d(u) du <=0.       (8)

No differentiation of the profile at its zero directions is used.
The active-profile identities are pointwise and include those directions.

The parent proof computes the pure profile own-pole integral exactly as
lambda A(a)epsilon^a/a. The smooth other-pole constant contributes exactly
epsilon^2/4 by the mean value property of the harmonic kernel K. The
remaining smooth contribution has absolute value at most E_s, by [f]_a<=1
and |e+u|>=1-epsilon. Combining these facts with (8) proves (4).

Reflection in the pole midline identifies the two omitted disks exactly,
as in the parent proof. All singular constants are removed by circular
principal values, and every remaining displayed local integral is
absolutely convergent. This proves the statement.

## Scope, dependencies and verification

The global witness theorem and the parent pole-disk proof are the only
analytic dependencies. Conditions (1) and (3) must be checked with outward
arithmetic for every numerical use. A finite annular certificate must
start at this same epsilon, or its earlier completed annular tasks must
be removed with an exact coverage check before this formula is inserted.
The full spatial partition, tail and midpoint remainder must still be
accounted for. The claim is awaiting independent lead cross-read.
