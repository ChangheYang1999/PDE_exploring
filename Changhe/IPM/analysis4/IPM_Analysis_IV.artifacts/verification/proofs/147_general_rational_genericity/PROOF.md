# Generic tuning on regular compatibility components at a general rational exponent

Status: PROVED conditional genericity theorem under the two exact algebraic hypotheses below. The theory part independently checked the equal-degree resultant argument at11:34Z; recorded in V299. The hypotheses hold for the four-ninths example146.

## Statement and hypotheses

Let h>=2 and Q>2h be coprime positive integers, delta=2h/Q and c=Q/(Q-2h). Fix an even bandwidth B>=6 and normalized real leading profiles

    f_1=sin(theta)+b sin(3theta)+sum_(j odd, 5<=j<B) t_j sin(j theta).

There are d=B/2-2 real coordinates t_j. Let O(b,t) be the first compatibility coefficient, namely the coefficient of sin((2h-3)theta) in f_Q. All earlier stream orders are nonresonant. Let sigma_k(b,t), k>=1, be the Q-step response to the free stream harmonic at order kQ, measured in the density obstruction at order (k+1)Q. Let sigma_infinity be its limiting response, as in 144.

Assume the following exact algebraic conditions on the two-mode specialization:

1. O(b,0) has degree exactly Q and is irreducible over the rationals, up to a nonzero rational factor.
2. For every integer k>=1 and also for k=infinity, sigma_k(b,0) is not a rational scalar multiple of O(b,0). The zero polynomial counts as a scalar multiple and is excluded.

Let M be the regular real hypersurface O=0, grad O!=0. Then the subset

    G={ (b,t) in M : inf_(k>=1)|sigma_k(b,t)|>0 }

is relatively open and dense in every connected component of M. Its complement has measure zero in every smooth chart. Every point of G has the unique convergent tuned exterior series of 145, including the common potential and every weighted derivative. Each compact subset of G has a common sufficient exterior radius. For B=6, the exceptional set is countable and relatively closed; its accumulation points within M lie among the finitely many zeros of sigma_infinity on O=0.

This statement concerns only regular normalized compatibility points. It makes no assertion at singular points or when the first sine coefficient is zero. A failure of the sufficient response condition does not by itself prove divergence or nonexistence.

## 1. Polynomial degrees and a uniform response estimate

Each order-n coefficient before the first stream resonance is a homogeneous polynomial of degree n in the leading amplitudes, with rational coefficients. This follows by induction from the quadratic stationary recurrence and its fixed nonzero rational divisors. Consequently O has total degree at most Q after normalization. Each response is homogeneous of degree Q in the leading amplitudes because its Q-step recurrence is linear in the inserted free harmonic and uses exactly Q total orders of the low fields. Thus every sigma_k has total degree at most Q in (b,t).

For completeness, a uniform bound follows from the same scalar norm inequalities as 145. Put a=||f_1||_1, L=Q/2 and kappa=B(Q-2h)(3-2h/Q)/h. The low scaled density norms are bounded by

    x_j=Cat_(j-1)(kappa L)^(j-1)a^j,  1<=j<=Q.

For a unit inserted stream harmonic at n=kQ, define alpha_r=(n+r)||phi_r||_1. The two orientations of the mixed response products give

    alpha_r/n <= kappa[x_r+2L sum_(s=1)^(r-1)(alpha_s/n)x_(r-s)].

If v_r is the scalar equality solution, its generating function is

    V(z)=kappa X(z)/(1-2kappa L X(z)),
    X(z)=a z+kappa L X(z)^2.

Expanding (1-4kappa L a z)^(-1/2) gives

    |sigma_k| <= v_Q
      = (1/2) binom(2Q,Q) kappa^Q L^(Q-1) a^Q,             (1)

uniformly in k. The same estimate holds over complex leading amplitudes, with their absolute-value norm.

Once the positive carrier q=2hk-2 satisfies q>=BQ, the response frequencies cannot meet zero or the opposite carrier branch. The largest density offset is BQ-1; intermediate stream offsets are at most B(Q-1). Every coefficient is then one fixed rational function of k, whose denominators are products of nonzero affine stationary and Poisson divisors. A sufficient starting index is

    k0=ceil((BQ+2)/(2h)).

There are finitely many amplitude monomials. Apply (1) on a bounded complex polydisk, or use a fixed finite interpolation set inside it, to bound each monomial coefficient uniformly in k. A bounded rational function of k has numerator degree at most denominator degree and has a finite limit. Taking these finitely many coefficient limits proves locally uniform convergence to the rational polynomial sigma_infinity of total degree at most Q. Formula 144 computes the same limit directly.

## 2. Irreducibility and the equal-degree issue

The coefficient of b^Q in O is a nonzero rational constant: it is nonzero by assumption 1, and total degree at most Q leaves it no dependence on t. Divide O by this coefficient and call the resulting monic polynomial P. If P factored in Q[t,b], both factors could be made monic in b since their leading coefficients multiply to 1. Specialization t=0 would preserve both b degrees and contradict the irreducibility of P(b,0), unless one factor had b degree zero. Such a monic factor is 1. Thus P is irreducible in Q[t,b], hence in Q(t)[b].

Fix any finite response or the limiting response S. Its b degree is at most Q. If P and S were not coprime in Q(t)[b], irreducibility would force P to divide S. If deg_b S<Q this would force S=0, contrary to assumption 2. Otherwise S=C(t)P. The leading b coefficient of S is a rational constant, again because its total degree is at most Q. Since P is monic, C(t) is that same rational constant. Specializing t=0 would make S(b,0) a rational scalar multiple of P(b,0), contrary to assumption 2.

This is the additional argument needed when obstruction and response have the same degree. A strict degree comparison, as in the h=1 cases, is not available here.

Therefore every resultant

    R_S(t)=Res_b(P(b,t),S(b,t))

is a nonzero polynomial. Every common zero of P and S projects to a zero of R_S, including a specialization where the degree of S drops, because P is monic and keeps its degree.

## 3. No response vanishes on a regular component

The points of M with partial_b P!=0 are open and dense in M. To prove density, suppose partial_b P vanished on a nonempty open piece of M. At a regular point some partial_(t_j)P is nonzero. Locally solve t_j=phi(b,t_hat). Implicit differentiation gives partial_b phi=0, so after shrinking to a connected coordinate box phi is independent of b. Fixing t_hat then gives one fixed t for which the monic polynomial P(b,t) vanishes on an interval, a contradiction.

If a response S vanished on a nonempty open piece of M, that piece would therefore contain a point with partial_b P!=0. Locally solve b=beta(t). The common-zero property would force the nonzero polynomial R_S(t) to vanish on an open set, a contradiction. Hence each finite or limiting response restricts to a nontrivial analytic function on every connected component of M.

## 4. Topology, measure and convergence

Local uniform convergence sigma_k->sigma_infinity implies

    inf_k |sigma_k|>0
      iff sigma_infinity!=0 and every finite sigma_k!=0.    (2)

Indeed a nonzero limit controls the tail and a finite minimum controls the remaining terms. The same locally uniform convergence shows that the condition is open: keep the limit uniformly away from zero in a neighborhood, control one common tail, then shrink the neighborhood for the finitely many preceding responses.

Each individual response zero set is closed with empty interior on each regular component, by Section 3 and analytic continuation. Baire's theorem gives a dense complement of their countable union in each chart. These analytic zero sets have measure zero: at any zero a derivative of some finite order is nonzero, and a derivative of one lower order has a regular zero hypersurface through the point. A countable derivative list and countable chart cover put the original zero set in a countable union of smooth hypersurfaces. The possibility that every derivative vanishes is excluded by the analytic identity theorem and Section 3. Equation (2) proves the assertions about G.

At each point of G, the exact compatibility condition and positive response lower bound are precisely the hypotheses of 145. Openness gives a locally uniform response lower bound; a finite cover of a compact subset and its bounded leading norms give one common majorant and exterior radius.

When B=6, there is one real t coordinate. Each nonzero resultant has finitely many roots, and the monic P has at most Q roots over each such t. Thus each individual response has only finitely many common zeros with P, and the entire exceptional set is countable. If exceptional points accumulated at a point with nonzero sigma_infinity, local uniform convergence would remove all sufficiently late responses in a neighborhood. Only finitely many earlier finite zero sets would remain, which cannot have infinitely many distinct points accumulating there. Therefore accumulation points in M lie among the finite common zeros of P and sigma_infinity. Relative closedness follows from openness of G.

## Dependencies and scope

The exact recurrence, resonance and limiting operator are in 144. The conditional convergence and potential reconstruction are in 145. The geometric and measure arguments are included in full here. For delta=4/9, irreducibility is certified in 146, and nonproportionality can be certified by its two-coefficient determinant D_k together with the limiting coprimality test. Those determinants and the infinite tail are now certified in V288. The application still requires independent review of this proof and145.
