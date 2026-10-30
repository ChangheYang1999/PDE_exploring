# Exact scope of homogeneous stream resonances

Date: 2026-10-29T05:38:35.874053+00:00. Status: independently checked correction to the wording of T2 review R3 for T4-256. No numerical input is required.

## Statement

Let e be real and Theta be a smooth real S1 angular profile, meaning a smooth2pi-periodic sum of sin(n theta) with positive odd n. Seek a stream psi=r^(e+1)Psi(theta) on r>0, with Psi a smooth sum of positive even sine harmonics, satisfying Delta psi=-partial_x(r^e Theta). For every such Theta there is a unique such Psi if and only if

    e not in {2k-1,-2k-1 : k=1,2,...}.

Thus (-3,1) is the maximal connected interval containing gamma in(0,1) with this property. It is not the complete set of nonresonant exponents. At a resonant exponent some profiles still admit homogeneous streams; arbitrary profiles do not. These are local homogeneous identities on r>0 and make no global canonical-velocity claim outside the weighted class used in T4-256.

## Proof

Polar differentiation gives

    [partial_theta^2+(e+1)^2]Psi
       = -e cos(theta)Theta+sin(theta)Theta'.

The source for Theta=sin(n theta) is

    (n-e)/2 sin((n+1)theta) -(n+e)/2 sin((n-1)theta).

The zero sine mode vanishes. On positive even m the angular eigenvalue is(e+1)^2-m^2. All are nonzero precisely outside the listed set. In that case the source coefficients decay faster than any inverse power of m, and division by the eigenvalues preserves rapid decay and gains two derivatives. This constructs a smooth solution and proves uniqueness coefficient by coefficient.

If e=m-1 for positive even m, choose Theta=sin((m+1)theta). Its source at frequency m has coefficient-m, which cannot belong to the range of the singular angular operator. If e=-m-1 choose Theta=sin((m-1)theta); the source at frequency m is m, likewise not in the range. Thus the assertion for every profile fails at each excluded exponent. Homogeneous kernel elements also preclude uniqueness whenever a solution exists.

The nearest resonant exponents on either side of gamma in(0,1) are-3 and1, proving the connected-interval statement. As an explicit counterexample to the unqualified wording, for e=-4 one has

    -partial_x(r^-4 sin(theta))=(5/2)r^-5 sin(2theta),
    Delta[(1/2)r^-3 sin(2theta)]=(5/2)r^-5 sin(2theta).

More generally9-m^2 is nonzero at every positive even m, so all smooth S1 profiles admit homogeneous streams at e=-4.

At e=-3, the source for sin(theta) is2r^-4 sin(2theta); it is solved by-(1/2)r^-2 log(r)sin(2theta). At e=1, the source for sin(3theta) has resonant coefficient-2sin(2theta), solved in that component by-(1/2)r^2 log(r)sin(2theta). These two endpoint examples from the Opus review are confirmed. They explain why a retained-exponent interval[a-1,1) first encounters a stream resonance when a reaches-2. They do not prove an impossibility theorem for every construction at a<=-2.

## Dependencies and scope

Only polar differentiation, product-to-sum identities and smooth Fourier series are used. T4-256 remains valid in its stated range. The associated weighted multiplier constant also degenerates at|a|=2, but that separate fact is not a proof that all possible weighted formulations fail there.
