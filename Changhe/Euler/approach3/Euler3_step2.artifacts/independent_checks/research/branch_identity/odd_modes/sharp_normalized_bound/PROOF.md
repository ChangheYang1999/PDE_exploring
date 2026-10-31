# Sharp separation from an even field in the normalized distance

Status: proved Hilbert-space statement. The application to the P3 coefficients below remains empirical because their odd fraction has no certified evaluation enclosure.

## Statement and notation

Let H be a real Hilbert space, E an orthogonal projection with nonzero range, and O=I-E. Fix u in H with ||u||>0 and put

    delta = ||Ou||/||u||,   s = ||Eu||/||u|| = sqrt(1-delta^2).

For every nonzero v in range(E), define

    d(u,v) = ||u-v||/min(||u||,||v||).

Then

    d(u,v) >= h(delta),
    h(delta) = sqrt(2-2 sqrt(1-delta^2)).                         (1)

The same bound holds for the unit-shape distance ||u/||u|| - v/||v||||. Both bounds are sharp over nonzero even vectors v. If Eu is nonzero, equality is attained by v=||u|| Eu/||Eu||. If Eu=0, equality is attained by every v in range(E) with ||v||=||u||. The latter vectors exist because range(E) is nonzero.

If T is any Hilbert-space isometry commuting with E, then the same lower bound holds with u replaced by Tu. In particular it holds for every axial rotation in the shell space from ../PROOF.md and for the infimum over all such rotations. The maximum of these lower bounds over a specified finite family of shells bounds the maximum-over-shells normalized distance.

## Proof

Since v is even, <u,v>=<Eu,v>. Cauchy-Schwarz gives <u,v> <= s ||u|| ||v||. Write a=||u||, b=||v|| and t=max(a,b)/min(a,b), so t>=1. Consequently

    d(u,v)^2 >= t^2+1-2st
              = 2-2s + (t-1)(t+1-2s)
              >= 2-2s.

The last product is nonnegative because 0<=s<=1 and t>=1. Taking the nonnegative square root proves (1). Equality requires t=1 and maximal inner product, except that when s=0 every even vector is orthogonal to u. The vectors stated above satisfy these conditions.

For the unit-shape distance, direct expansion gives

    ||u/a-v/b||^2 = 2-2<u,v>/(ab) >= 2-2s.

The same equality vectors work. Commutation with E and isometry imply ||OTu||=||TOu||=||Ou|| and ||Tu||=||u||, so delta is unchanged. Apply (1) to Tu. Taking the maximum over shells preserves each lower bound, and a bound valid for every rotation also bounds the infimum over rotations.

The function h is nondecreasing on [0,1], and h(delta)>=delta because

    h(delta)^2-delta^2 = (1-s)^2 >= 0.

For a proposed distance threshold q in [0,sqrt(2)], (1) implies d>=q whenever

    delta^2 >= q^2-q^4/4.                                      (2)

Indeed h(delta)>=q is equivalent to s<=1-q^2/2, whose right side is nonnegative on that interval. Squaring and substituting s^2=1-delta^2 proves (2).

## Application and correction of V538

V538 measured the largest P3 odd fraction as delta=0.4266113410592721 on shell j=0. This number itself is below0.43. It therefore cannot be rounded upward to claim an odd-fraction lower bound of0.43.

However, the registered distance divides by the smaller of the two field norms. It has the stronger bound (1), not only the simpler bound delta. For the exact real represented by the saved binary64 fraction, h(delta) exceeds0.43. The accompanying rational computation encloses h of that saved scalar. It does not enclose the true continuum odd fraction or replace an arithmetic error bound for the field evaluation.

Thus V538's broad wording that a distance lower bound of0.43 was refuted was incorrect. The evidence supplied there did not refute such a distance bound. The exact theorem supports it conditionally on a sufficient odd-fraction bound, while the present calculation provides empirical support only. For this measured state, about0.437 is the empirical sharp minimum distance to the even subspace under either normalized metric. Actual distances to particular even fields may be larger.

No Euler equation, pressure, branch uniqueness or nearby-solution exclusion is established. No formal proof has been built. Dependencies are orthogonal projection, Cauchy-Schwarz, elementary real algebra and the shell rotation/projection construction in ../PROOF.md.
