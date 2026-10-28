# Joint transport across the two local disks

## Statement and conventions

Let 0<a<1. Use the real homogeneous Holder seminorm, circular principal
values and quotient operators of ../../01_setup/PROOF.md. Put
x=(1/2,0), y=-x, 0<delta<R=1/2, and

    T_phi=cos(phi)T_xx+sin(phi)T_xy,
    w_phi(r,theta)=[cos(2theta-phi)
      -r^2 Re(exp(i phi)/(1+r exp(i theta))^2)]/(2pi).

The local regular increment measure is supported on the two annuli
around x,y with delta<=r<=R. Its right-annulus density is
w_phi(r,theta) dtheta dr/r and its left-annulus measure is the negative
central reflection of the right measure. For the diagonal operator
include the atoms -delta_x/2+delta_y/2. For the traceless operator omit
them. This finite signed measure will be denoted mu_phi.

Let a finite partition of [delta,R] times the circle consist of cells
Q_j=[r_j,s_j] times I_j. Their endpoints overlap only on null sets.
Suppose numbers m_j>=0, signs epsilon_j in {-1,0,1}, and V_j>=0 obey

    epsilon_j w_phi>=0 on Q_j when m_j>0,
    m_j <= integral_(Q_j) |w_phi| dtheta dr/r,
    integral_(Q_j) |w_phi| dtheta dr/r <= V_j.

Set m_j=0 whenever no fixed sign has been proved. Extract a submeasure
of mass m_j and sign epsilon_j on the right cell, together with its
opposite reflected submeasure on the left cell. Include the two full
identity atoms in the diagonal case. Suppose a finite nonnegative
transport matrix has exactly these signed marginals. If its cost is
bounded by U_phi using the supremum of |z-z'|^a over each pair of
supports, then

    | integral f d mu_phi |
       <= [f]_a (U_phi+sum_j(V_j-m_j)(1+2s_j)^a).       (1)

This allows transport across different radial cells and includes the
identity atoms as two fixed supports. It does not impose a radial
allocation of their masses. No optimality assertion about the chosen
finite matrix is required.

## Proof of the local bound

If m_j>0, the sign condition and mass bound allow extraction of a
submeasure: multiply the restriction of |w_phi| by
m_j/integral_(Q_j)|w_phi|. A zero denominator occurs only when m_j=0,
in which case extract nothing. Reflect these submeasures to the left
annulus. The two signed extracted masses sum to zero, as do the
identity atoms. A transport matrix with the stated marginals can be
lifted to a transport between the actual measures by using the product
of the two normalized cell measures on each pair of cells. Atoms use
point masses. Its cost is bounded by the matrix flow times the largest
point-pair cost on that pair of supports. Therefore its action on f is
at most U_phi[f]_a.

The remaining measure on the right cell has variation at most V_j-m_j.
Pair each remaining point with its own negative, carrying its actual
sign. Its distance to that negative point is at most1+2s_j. The
seminorm inequality bounds this cost by the corresponding summand in
(1). All residual masses are nonnegative. The identity measure has
been included in full, so it has no unestimated residual. Summing gives
(1). The argument applies directly to finite signed measures and does
not use density of compact smooth functions in the Holder seminorm.

## Uniform radial enclosures

The already proved angular-cell rule in
../paired_local_circles/PROOF.md gives on each radial bin [r,s] a signed
angular lower mass l_j and upper variation v_j, uniform in the radius.
Consequently any exact rational

    0<=m_j<=l_j log(s/r)

is valid, with V_j=v_j log(s/r). The sum of all v_j in a bin can be
used instead of separate v_j, since all cells in that bin share the
residual distance bound1+2s. Rounding extracted masses down preserves
domination. Including their exact negatives on the opposite annulus
preserves zero total mass. The atom masses1/2 can be represented
exactly with any even integer mass unit.

For cells on the same pole, the largest distance is obtained by taking
both radii at endpoints and minimizing cos(theta-eta) over the two
angular intervals. The squared distance is

    r^2+s^2-2rs cos(theta-eta).

It is convex separately in r and s, so their four endpoint choices
suffice. For cells on opposite poles the distance is

    |1+r exp(i theta)+s exp(i eta)|.

Its square is again separately convex in r and s. Evaluate the four
radial endpoint choices with an interval enclosure over the angular
arcs. A center and its own annular cell have distance at most the
outer radius; the other center uses |1+r exp(i theta)| and both radial
endpoints. The two centers are distance one apart. Every resulting
nonnegative distance upper bound can be raised to a to give a valid
transport cost. A second independent bound, the center distance plus
the two enclosing-cell radii, may be minimized with the first one.

## Completing the operator estimate

The two omitted disks have the established bound

    S_a(delta)=2 a2(a) delta^a/a
                +(1+2delta)^a delta^2/[2(1-delta)^2],
    a2(a)=2^(1+a/2)/[pi(a+2)].

This includes their smooth cross kernels. Let L_j be the right side
constant in (1) at phi_j=j*pi/(2m), j=0,...,2m. Let M_j,E_j be any
proved upper costs for the middle and exterior regions, with the same
phase convention and disjoint spatial decomposition. Then

    D_a <= S_a(delta)+q max_j(L_j+M_j+E_j)+(q-1)/2,
    q=sec(pi/(4m)).                                    (2)

Indeed the regular functional, after removing the small disks, is
cos(phi)A+sin(phi)B-I/2 with I(f)=f(x)-f(y), ||I||=1.
Positive sine interpolation between adjacent phase nodes has coefficient
sum at most q. The identity coefficient then needs the correction
(c+d-1)I/2, of norm at most(q-1)/2. Reflection reduces the full phase
circle to[0,pi]. Add the phase-independent small-disk estimate.
The setup and the middle/exterior proofs justify the singular limits,
the integrability at infinity and passage to the homogeneous quotient.

For C_a, omit the atoms, use only j=0,...,m by sign and reflection
symmetry, and omit(q-1)/2 in(2). All formulas are valid for every
admissible partition and every exact feasible matrix. Numerical
improvement over existing bounds remains to be checked.
