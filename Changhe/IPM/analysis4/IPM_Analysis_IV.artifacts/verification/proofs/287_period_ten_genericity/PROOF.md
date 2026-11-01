# Generic period-ten tuning on every regular compatibility component

Status: PROVED in V586, admitted 2026-10-31T21:14:52+00:00, within the exact scope below.

## Statement and notation

Fix an even integer B>=6, put d=B/2-2, and set delta=1/5 and c=5/4. Consider the real leading profiles

    f_1(b,t)=sin(theta)+b sin(3theta)
             +sum_(j odd,5<=j<B) t_j sin(j theta), t in R^d.

Use the pure stationary recurrence01 with p_n=1-n/5 and P_n=2-n/5. Before the first nontrivial stream resonance20 there is no free stream harmonic. Let O(b,t) be the sin(theta) coefficient of f_20, and let M be the regular real hypersurface O=0, grad O!=0. For integer k>=2, let sigma_k(b,t) be the coefficient of sin((2k-1)theta) in the change of f_(10k+10) caused by a unit addition of sin((2k-2)theta) to g_(10k). The affine ten-step response is defined on all parameters, whether or not O=0. Put

    G={x in M: inf_(k>=2)|sigma_k(x)|>0}.

Then G is relatively open and dense in every connected component of M. Its complement has measure zero in every smooth chart. Each x in G determines a unique tuned pure formal density and stream pair which converges, with all appropriately weighted derivatives, on a sufficiently large closed exterior. The common potential has a convergent expansion with possible logarithms at orders10 and20. Each compact subset of G has one common sufficient exterior radius.

When B=6 the set M minus G is countable and relatively closed. Its accumulation points within M belong to the finite zero set of sigma_infinity=lim_(k->infinity)sigma_k. For a nonzero real first coefficient epsilon, normalize the profile by epsilon: responses scale by epsilon^10 and sufficient physical radii by |epsilon|^5. No claim is made about singular compatibility points, zero first coefficient, excluded profiles, a common explicit radius on all of G, or whole-plane stationary extension.

## Exact specialization inputs

Topic281 supplies the irreducible degree20 polynomial P_20 proportional to O(b,0), with fourteen simple real roots. Topic282 proves that, at each such root, every sigma_k and sigma_infinity is nonzero: the response polynomials have degree at most10, their tail coefficient gcd has no integer zero for k>=21, and the small and limiting polynomials are nonzero. This provides a point where every one of these polynomials is nonzero. No radius calculation or finite growth fit is needed for this input.

## Polynomial and component argument

Every coefficient before the first resonance is a polynomial in the leading amplitudes: the recurrence multiplies complementary orders and divides only by fixed nonzero rational numbers. Thus O has total degree at most20. Its b^20 coefficient is a nonzero rational constant because the specialization at t=0 has degree20. Dividing by this coefficient gives a monic polynomial P(b,t).

P is irreducible over Q[t,b]. Any factorization of a monic polynomial over the integral polynomial ring can be chosen monic in b. Specializing t=0 preserves both b degrees, contradicting the irreducibility of P(b,0) unless one factor has b degree zero. Such a monic factor is1. Gauss's lemma gives irreducibility over Q(t)[b].

Each finite response is a polynomial in the profile parameters of total degree at most10. The compact response construction149 gives a locally uniform limit sigma_infinity, also a rational polynomial of degree at most10: its fixed rational denominators are nonzero at inverse carrier zero and in a neighborhood of zero. The specialization inputs make every finite and limiting polynomial nonzero. None can be divisible by P, whose b degree is20. Hence each resultant

    R_h(t)=Res_b(P(b,t),sigma_h(b,t)), h=2,3,... or infinity,

is a nonzero rational polynomial. Every common zero of P and sigma_h projects to R_h=0. Monicity of P makes this statement valid even where the b degree of sigma_h drops.

Points with partial_b P!=0 are dense in M. Otherwise some regular open piece admits coordinates t_j=phi(b,t_hat), and the relation partial_b P=0 gives partial_b phi=0. On a smaller coordinate box, phi is independent of b. Fixing t_hat would then make a monic polynomial P(b,t) vanish on a b interval, which is impossible.

If sigma_h vanished on an open piece of M, that piece would contain a point with partial_b P!=0. The implicit representation b=beta(t) there would make the nonzero polynomial R_h vanish on an open t set. Therefore the zero set of each response is closed and nowhere dense on every regular component. It has chart measure zero as well: a nonzero real analytic function has its zero set covered by the regular zero sets of its derivatives of minimal nonzero order, using a countable family of derivatives and charts. Analytic continuation excludes points of infinite-order vanishing on a component where the function is not identically zero.

## Uniform nonvanishing, convergence and exceptional sets

Local uniform convergence to sigma_infinity implies that G is exactly the set where every finite response and the limiting response are nonzero. At such a point, a neighborhood separates the tail from zero; finitely many earlier responses remain separated on a smaller neighborhood. Thus G is relatively open. Its complement is the countable union of the finite and limiting zero sets. The Baire theorem on each manifold component gives density, and countable subadditivity gives chart measure zero.

For each point of G, O=0 and the positive response infimum are precisely the hypotheses of131, valid for every integer Q>=3. The choice H_(10k)=-R_k/sigma_k uniquely enforces the next compatibility condition. The triangular majorant gives a geometric coefficient bound. The finite angular bandwidth absorbs every fixed derivative on a strict exterior;132 reconstructs the common potential, with only the possible logarithmic orders10 and20. A compact subset of G has a uniform positive response lower bound and bounded leading norm by a finite neighborhood cover. The same majorant then gives a common radius.

For B=6, each nonzero resultant has finitely many roots in the single variable t. Each fiber P(b,t)=0 has at most20 points. Each individual response zero set is therefore finite. Their countable union is relatively closed because G is open. Near any point where sigma_infinity is nonzero, local uniform separation leaves only finitely many finite-response zero sets. Thus distinct excluded points can accumulate only at the finite limiting zero set.

Finally, homogeneity of the ten-step response gives epsilon^10. Since the series variable is r^(-1/5), multiplying the coefficient growth base by |epsilon| gives the physical factor |epsilon|^5.

## Dependencies and scope

This is the Q=10 specialization of257. Its analytic dependencies are01,131,132,149 and257; its exact inputs are281 and282. The dependency receipt must verify their immutable admission and source hashes. It does not constitute a new execution of the symbolic recurrence and supplies no new quantitative exterior bound.

## Completed verification

For every fixed even bandwidth B>=6 at delta1/5, the normalized regular compatibility hypersurface has an open dense, full-chart-measure subset on every connected component where every response is uniformly separated from zero. Each such profile has a unique convergent tuned exterior series; compact subsets admit one common sufficient exterior. For B6 the excluded set is countable and relatively closed, with accumulation only in the finite limiting-response zero set. Nonzero leading amplitude scales the responses by epsilon^10 and the physical radii by |epsilon|^5.

The genericity and local stability statements are PROVED within the fixed exponent and finite profile spaces stated in287. No singular-point, exponent-open, global-radius or whole-plane assertion is made.
