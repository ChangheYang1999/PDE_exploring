# Generic period-nine tuning on every regular component

Status: PROVED, admitted V562 after the dependency check and independent theory-part review.

## Statement and notation

Fix an even integer B>=6, put d=B/2-2, and set delta=2/9 and c=9/7. Consider normalized real leading profiles

    f_1(b,t)=sin(theta)+b sin(3theta)
             +sum_(j odd,5<=j<B) t_j sin(j theta),  t in R^d.

Use the pure stationary recurrence of01, with density exponent p_n=1-2n/9, stream exponent P_n=2-2n/9, and zero free stream harmonics before the first nontrivial resonance18. Let O(b,t) be the sin(theta) coefficient of f_18. Let M be the regular real hypersurface O=0, grad O!=0.

For k>=2, sigma_k(b,t) is the coefficient of sin((2k-1)theta) in the change of f_(9(k+1)) caused by a unit addition of sin((2k-2)theta) to g_(9k). This response is defined by the affine nine-step recurrence on all profile parameters, even when O!=0. Set

    G={x in M: inf_(k>=2)|sigma_k(x)|>0}.

Then G is relatively open and dense in every connected component of M, and its complement has measure zero in each smooth chart. Every x in G determines a unique recursively tuned pure density and stream series. These series and all their weighted derivatives converge uniformly on some closed exterior. They admit a common convergent potential expansion, possibly with the two permitted logarithmic orders9 and18. Each compact subset of G has one common sufficient exterior radius.

For B=6, M minus G is countable and relatively closed. Its accumulation points in M belong to the finite set where sigma_infinity=0, with sigma_infinity=lim_(k->infinity)sigma_k. No conclusion about excluded or singular profiles, or profiles with zero first sine coefficient, is asserted.

For a nonzero real first coefficient epsilon, normalize by epsilon. Every response scales by epsilon^9 and every sufficient exterior radius by |epsilon|^(9/2). The theorem gives no common explicit radius for all of G and does not imply a whole-plane stationary extension.

## Exact inputs already proved

Topic267, V549, proves that O(b,0) is a nonzero rational multiple of an irreducible polynomial P_18 of degree18. Its primitive descending coefficient hash is recorded in the verification receipt. It has ten simple real roots. Topic267, V551, proves, at the smallest root b_*, the bound

    |sigma_k(b_*,0)|>2^20  for every integer k>=2.

The same admitted compact-response cover includes inverse carrier tau=0 and therefore also proves |sigma_infinity(b_*,0)|>2^20. Only this one center is needed here. The other nine convergence certificates and any symbolic formula of degree595 are unnecessary for this argument.

## Polynomial and component argument

The recurrence below18 adds products of coefficients of complementary orders and divides only by fixed nonzero rational denominators. Every coefficient of order n is therefore homogeneous of degree n in the leading amplitudes before normalization. In particular O has total degree at most18. Its coefficient of b^18 is a nonzero rational constant, because the specialization O(b,0) has full degree18. Divide by that coefficient and call the resulting monic polynomial P(b,t).

P is irreducible over Q[t,b]. Indeed, in a factorization its factors can be chosen monic in b: their leading coefficients multiply to1 and are units in Q[t]. Specializing t=0 preserves their b degrees, contradicting irreducibility of P(b,0) unless one factor has b degree0. A monic factor of b degree0 is1. Gauss's lemma then gives irreducibility over Q(t)[b].

Each sigma_k has total profile degree at most9. The compact response construction149 shows local uniform convergence in finite complex parameter neighborhoods to a rational polynomial sigma_infinity of degree at most9: the compact formula has fixed rational denominators and can be evaluated at inverse carrier0. The bound at b_* makes every finite response polynomial and the limiting polynomial nonzero. None can be divisible by P, whose b degree is18. Hence, for h=k or infinity,

    R_h(t)=Res_b(P(b,t),sigma_h(b,t))

is a nonzero rational polynomial. Every common zero of P and sigma_h projects to R_h=0; monicity ensures this statement survives specialization.

Points with partial_b P!=0 are dense in M. Otherwise a regular open piece has some partial_(t_j)P!=0 and can be written t_j=phi(b,t_hat). There partial_b P=0 forces partial_b phi=0. On a smaller coordinate box, phi is independent of b. Fixing t_hat gives a fixed t at which the monic polynomial P(b,t) vanishes on an interval, a contradiction.

If sigma_h vanished on an open piece of M, that piece would contain a point with partial_b P!=0. Writing b=beta(t) there would make the nonzero resultant R_h vanish on an open subset of R^d. Thus no response vanishes identically on a regular component. Its zero set is closed, nowhere dense, and has chart measure zero. For the last assertion one may cover analytic zeros by the regular zero sets of derivatives of minimal nonzero order; the countable derivative and chart families give a null cover. Analytic continuation rules out a point where all derivatives vanish on a component on which the function is nontrivial.

## Uniform positivity and convergence

Local uniform convergence to sigma_infinity implies that G is precisely the set where the limit and every finite response are nonzero. At such a point the tail is uniformly separated from zero on a small neighborhood; finitely many earlier responses are also separated there. Thus G is open. Its complement is the countable union of the finite and limiting zero sets. The Baire property of a smooth manifold gives density in each component, and countable subadditivity gives the measure assertion.

For x in G, the exact compatibility O=0 and the positive response infimum are the hypotheses of the tuned convergence theorem131. Successively setting each free harmonic to minus its obstruction divided by its response gives the unique tuned series. The theorem's analytic majorant gives exterior convergence. The finite Fourier bandwidth absorbs fixed derivatives on a strict exterior, and132 reconstructs the common potential, with logarithms allowed only at9 and18. On a compact subset of G, a finite neighborhood cover supplies a common positive response lower bound and bounded leading norms; the same majorant then supplies a common radius.

When B=6, t is one-dimensional. Each nonzero resultant has finitely many zeros and each fiber P(b,t)=0 has at most18 points. Each individual response zero set is therefore finite. Their countable union is relatively closed because G is open. Near a point where sigma_infinity!=0 only finitely many response zero sets can occur, by local uniform tail separation. Distinct exceptional points can accumulate only at a zero of sigma_infinity, and the latter set is finite by its own resultant.

Homogeneity yields the stated epsilon^9 response factor. Since the series variable is r^(-2/9), scaling its coefficient base by |epsilon| scales the radius by |epsilon|^(9/2).

## Dependencies and verification scope

This is a standalone specialization of the general proof257, independently reviewed and admitted inV532. Its analytic dependencies are01,131,132,149 and257. Its exact inputs are267/V549 and267/V551. The new receipt checks these immutable dependencies, the selected center and the nonzero limiting enclosure. It is a dependency and specialization check, not a fresh computation of P_18 or the all-index cover. It does not certify the theory part's separate large symbolic response numerator or its factorization.
