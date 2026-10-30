# Three remaining derivative norms and a weighted Hessian identity

## Statement and exact data

Let F be the complete residual of the exact candidate007 potential,
with its previously audited finite representation

    F=r sum_(ell,n) v^(ell delta/2) P_(ell,n)(t) sin(n theta),
    t=r^2/(1+r^2), v=1-t, delta=1-1/c,
    c=4076476460239181/2251799813685248.

Every P is rational and every n is a positive odd integer. The exact
candidate hash, residual-cache hash and assembly record are inputs to
this check. The targets are

    D2=||D^2 F||_2,
    rD2=||r D^2 F||_2,
    Pw1=||(1+r^2)^(-1/10) grad F||_2.

The Hessian is the ordered Cartesian tensor: its squared norm is
F_xx^2+2F_xy^2+F_yy^2. The Pw1 squared weight is
(1+r^2)^(-1/5)=v^(1/5). These are the exact N3 component definitions,
not the P2 norm with weight (1+4r^2)^(2/5).

## Polar formulas and radial integrals

For d=ell delta/2, set T_d P=(1-2dt)P+2t(1-t)P'. Direct differentiation
of f=r v^d P gives gradient components v^d T_d P sin(n theta)
and n v^d P cos(n theta). The orthonormal Hessian components have
radial factor r v^(d+1) and polynomial coefficients

    A=-2d T_d P+2(1-t)(T_d P)',
    B=n[-2d P+2(1-t)P'],
    C=(T_d P-n^2 P)/t.

Their angular factors are respectively sin(n theta), cos(n theta),
and sin(n theta). The middle component occurs twice in the ordered
tensor norm. These formulas follow by differentiating the orthonormal
polar frame; their full derivation is in ../polar_derivative_norms/PROOF.md.
The code checks exact divisibility in C and the trace identity

    t(A+C)=T_d(T_d P)-n^2 P.

For each polynomial E, factor E(1-v)=v^q Q(v) exactly. For a pair
(ell,q,Q),(ell',q',Q'), the integrand after angular integration and
r dr=dv/(2v^2) is pi/2 times v^b times the following polynomial:

| target | b | polynomial |
|---|---|---|
| D2 | (ell+ell')delta/2+q+q'-1 | (1-v)QQ' |
| rD2 | (ell+ell')delta/2+q+q'-2 | (1-v)^2 QQ' |
| Pw1 | (ell+ell')delta/2+q+q'-9/5 | QQ' |

All unordered distinct radial pairs have multiplicity two. Angular
orthogonality removes different positive frequencies. Every retained
diagonal exponent must be greater than -1; the same follows for cross
terms by averaging and is checked explicitly. Remaining products are
formed in outward Arb arithmetic at2048 bits, and

    integral_0^1 v^b sum_j a_j v^j dv=sum_j a_j/(b+j+1).

Every denominator is strictly positive. This integrates the full plane,
including infinity, without quadrature. Exact cancellations occur before
conversion to balls. A completed full norm requires all160 modes and
at least150 relative accuracy bits for every nonzero modal energy.
A partial positive sum is only a lower bound.

## Independent norm identities

For an additional check, integrate the square of the trace A+C by the
same full radial formula and compare it with each mode's D2 energy.
The equality is analytic, not an expectation based on close decimals:
for smooth compactly supported real f, twice integrating by parts gives

    integral |D^2 f|^2 = integral (Delta f)^2.

More generally, for smooth real w, integrations by parts give

    integral w[(Delta f)^2-|D^2 f|^2]
      =integral Hess(w)(grad f,grad f)-integral Delta(w)|grad f|^2.

Indeed the first integration leaves the two terms
w_j f_i f_ij-w_i f_i f_jj, summed over i,j. The first equals
-Delta(w)|grad f|^2/2 after integration, and integrating the second
once more yields Hess(w)(grad f,grad f)-Delta(w)|grad f|^2/2.
For w=r^2 in two dimensions, Hess(w)=2I and Delta(w)=4. Consequently

    ||r D^2 f||_2^2=||r Delta f||_2^2+2||grad f||_2^2.        (1)

The finite candidate expansion and exact canceled residual sectors give
F=O(r^(-beta)), with differentiated bounds through order3, for some
beta>0. The same holds for any of its finitely many angular projections.
Apply the integrations on disks and let the radius tend to infinity:
each boundary term for w=r^2 is O(R^(-2beta)) and tends to zero. Smoothness
removes the origin boundary. The displayed norm integrals converge by
the exact endpoint checks above. The unweighted identity and(1)
therefore apply to this candidate and its individual modes.

The already independently confirmed whole-plane quantity
N_1=||(1+r^2)^(1/2) Delta F||_2 satisfies

    rD2^2 = N_1^2-D2^2+2G1^2,  G1=||grad F||_2.             (2)

The final check compares the new direct weighted Hessian integral with
this separate combination of retained N_1 and G1 balls. The subtraction
is performed outward; no significance is inferred from cancellation of
rounded decimal values.

## Validation, dependencies and scope

The full N3 Cartesian differentiation result is frozen before this
calculation. Each of the three new full norm balls must overlap its N3
counterpart. Source identity is checked against the exact candidate raw
hash as well as the previously confirmed canonical representation. The
new implementation uses the independently derived polar norm formulas;
it does not import or execute N3 code. Each write-once mode binds to a
manifest containing source, cache, proof and helper hashes. All mode
files are checked before a complete upper norm is reported.

Dependencies: the candidate007 exact far-field and canonicalization
audit; the complete residual assembly and integration proof in
../whole_plane_norms/PROOF.md; the polar tensor formula cited above;
and the confirmed full N_1 and G1 records. These numerical quantities
are residual components. They imply neither an inverse estimate nor
existence of a profile. New results remain OPEN until the complete
independent comparison and proof checks have succeeded.
