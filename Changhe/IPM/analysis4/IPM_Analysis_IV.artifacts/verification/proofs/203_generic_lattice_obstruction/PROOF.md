# Generic order-eighteen obstruction on high harmonic lattices

Status: PROVED. Exact witnesses were confirmed in V413; the independent theory-part review is admitted in V415 on 2026-10-31T15:09:34+00:00.

## Statement

Fix delta=4/9 and c=9/5. Let M be either17 or19. Let J be any finite nonempty set of positive odd integers containing1, and write

    f_1(theta) = sum_(j in J) a_j sin(j M theta),   a in R^J.

There is a nonzero homogeneous polynomial R_J in Q[a_j:j in J], of degree18, such that every pure density/stream far-field series with this leading profile must satisfy R_J(a)=0. This necessary condition holds even when every resonant stream harmonic in the prescribed exponent lattice is allowed.

Consequently, an open dense subset of full Lebesgue measure in R^J is obstructed at order18. Every profile in this subset is nonzero. In particular, the first compatibility condition at order9 vanishes for every member of these finite-dimensional families, but it is generically insufficient to continue through the second resonance.

The assertion concerns pure density and stream exponents p_n=1-4n/9 and p_n+1. It permits the density-free potential logarithm that realizes an arbitrary first stream harmonic. It does not concern logarithmic density/stream expansions or additional exponent channels, and it makes no genericity assertion in the similarity parameter.

## Support argument

Every signed leading frequency is an odd multiple of M. The sum of an odd number r of such frequencies is again an odd multiple of M. The low-order support induction gives

    supp(f_r) contained in r Lambda + E_(r-1),
    E_s = {-s,-s+2,...,s},

where Lambda is the signed leading support. This is proved directly by the Poisson shift by one frequency and the additive supports in the polar quadratic recurrence. In particular, each frequency at order9 is an odd multiple of M plus an even integer of absolute value at most8. Its absolute value is at least M-8>=9. The first compatibility coordinate, frequency1, therefore vanishes identically in all coefficients a_j.

At the first resonance, the free stream harmonic is H9 sin(2 theta). A density term involving two copies of H9 first has order19, because each density monomial contains at least one leading density factor. Thus the density through18 is affine in H9. Equivalently, the direct affected-factor count gives first possible quadratic order9+10=19.

The response of the frequency5 compatibility coordinate at18 has support in

    {-2,2} + 9 Lambda + E_8.

To reach frequency5 from carrier2 requires3 in 9 Lambda+E_8; from carrier-2 it requires7 there. Both are impossible since every element has absolute value at least M-8>=9. Therefore the response is identically zero, for all a_j and every H9. These facts use only support and affineness, not cancellation inferred from finite samples.

## Polynomial obstruction and exact witness

Set H9=0 and form f18. All density recursions are polynomial operations on the leading coefficients, and every nonresonant Poisson inverse multiplies by fixed rational numbers. At9 the identically zero forcing coordinate is omitted and its free harmonic is set to zero. There are no other intermediate resonances. Thus the coefficient R_J(a) of sin(5 theta) in f18 is a rational polynomial. Scaling a by a scalar multiplies f_n by that scalar to the power n, so R_J is homogeneous of degree18.

The preceding response argument shows that this same R_J(a) is the compatibility coefficient for every possible H9. Hence R_J(a) must vanish for any pure continuation to order18.

To prove that R_J is nonzero, take a_1=1 and every other coefficient zero. The calculation reduces exactly to f1=sin(M theta), independent of J. The retained exact witnesses from topic36 give a nonzero rational frequency5 coefficient for each M=17 and M=19, with zero response to H9. Copies, hashes and exact rational comparisons are stored in verification. No sign or decimal approximation is needed for the nonvanishing conclusion.

## Genericity and its limits

A nonzero real polynomial is continuous, so its nonzero set is open. Its zero set has empty interior: if it vanished on a box, successive one-variable polynomial identities would force every coefficient to vanish. Its zero set also has Lebesgue measure zero. This follows by induction on the dimension: expand in the last variable, discard the measure-zero set where every coefficient polynomial vanishes, and use that a nonzero one-variable polynomial has finitely many roots; apply Fubini on bounded boxes. Thus R_J is nonzero on an open dense set of full measure.

At a=0 the homogeneous polynomial vanishes, so the asserted obstructed profiles are all nonzero. The exceptional algebraic set R_J=0 may contain additional compatible or incompatible profiles; this proof does not classify it. No convergence or divergence statement about generalized logarithmic series follows.

## General form of the support calculation

For delta=2h/Q with Q odd, h>=2, gcd(h,Q)=1 and2h<Q, leading frequencies on the odd-M lattice give every element of Q Lambda+E_(Q-1) absolute value at least M-Q+1. If M>Q+6h-6, this excludes both response offsets2h-1 and6h-5 at the first resonant harmonic. It also excludes the initial compatibility frequency2h-3. The response at the second resonance therefore vanishes for the entire lattice family. Whenever a nonzero single-profile obstruction at order2Q is separately certified, the same polynomial argument supplies a generic order2Q obstruction. Here Q=9,h=2 and the independently recorded witnesses are M=17 and19.

## Dependencies

The exact density and stream recurrence is topic01. The original unit-profile witnesses and free-harmonic calculation are topic36, V043. The general support calculation is proved above and agrees with topic201. Independent review must check the polynomial and genericity argument as well as the witness provenance before this result is labeled PROVED.

## Independent review, 2026-10-31T15:09:34+00:00

The theory part independently checked the support gap, affine dependence on the first free harmonic, homogeneity, exact-witness specialization and polynomial genericity argument. The review reports no gap. These families have zero sin(theta) coefficient, so they lie outside the normalized profile space of the separate regular-component genericity theorem.

The set of profiles that continue through every order is contained in the closed nowhere dense null set R_J=0. This proof does not establish that the full set of continuing profiles is itself closed. The obstruction statement above needs only the proved containment.
