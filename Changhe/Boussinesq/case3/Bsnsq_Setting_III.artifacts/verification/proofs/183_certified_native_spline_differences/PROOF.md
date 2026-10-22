# Exact comparisons of native radial splines and their inverse constants

Status: CONFIRMED general theorem and exact finite-state applications. The complete argument was drafted before implementation and reviewed by actual Claude Opus5.5; all certificates passed the separate rational checker. Review scope and follow-up are in verification/review_adjudication.md.

## Statement, notation and scope

Let S_A and S_B be two real quintic splines on[0,1], specified by rational clamped knot vectors and rational B-spline coefficients. Each interior knot has multiplicity at most3, so both functions are globally C2. Endpoint derivatives are one-sided. No approximate floating-point value is used as an exact real input: an input obtained from an archive denotes precisely its stored binary rational value, including the generated knots, under the separately stated decode rule.

Set D(t)=S_A(t)-S_B(t) and P(z)=D(1-z). Fix a common noninteger b in(3,4) and a common scale L>0. These equal-parameter assumptions are essential: the following comparison of inverse constants uses linearity in P at fixed b,L. Let gamma=b-3, and let delta be one minus the largest interior knot in the union of the two knot vectors. If there are no interior knots put delta=1. Then P is one polynomial on[0,delta].

For k=0,1,2, the certificate described below gives exact rational numbers l_k,u_k with

    l_k <= sup_[0,1] |D^(k)| = sup_[0,1] |P^(k)| <= u_k.             (1)

These are global suprema of the represented functions, not sampled estimates. Their C2 norm, with the maximum convention, lies between max_k l_k and max_k u_k. We report derivatives separately because their units and numerical scale differ.

The inverse constant for a native first-cosine vorticity

    Omega(r,theta)=r z^(b+1) S(1-z) cos(theta),
    z=(L²/(L²+r²))^(1/(2b)),

is C2(S)=-(bL²/2)J_b(S(1-z)), with the finite-part functional of181. Thus

    |C2(S_A)-C2(S_B)| <= (bL²/2) [
      |P(0)|/(b-1) + |P'(0)|/(b-2) + |P''(0)|/(2(b-3))
      + u_2 {17 delta^(-gamma)/(3(1-gamma))
                        +(delta^(-gamma)-1)/gamma} ].              (2)

The right side is finite for every fixed pair. It need not be a useful small bound. A large certified upper bound is not a large error lower bound. Independently certified inverse constants may give a much tighter interval for their actual difference. Neither kind of finite-state comparison estimates error relative to an unknown PDE solution, proves a refinement limit, or establishes a branch theorem. The scalar S is only the first angular cosine coefficient after the exact mask and projection; these norms are not asserted to be norms of the full fields.

## Exact restriction and Bernstein bounds

Merge the distinct knots into an increasing partition0=t_0<...<t_N=1. On each closed cell, both splines restrict to polynomials of degree at most5, with the appropriate one-sided value at a knot. Since the functions are C2, derivatives up to order2 agree from either neighboring cell. They may therefore be bounded separately on all closed cells without missing any value.

An affine substitution t=a+h v, h>0, sends a cell to[0,1]. Write its k-th physical derivative as

    q_k(v)=sum_(j=0)^(5-k) a_j v^j
          =sum_(i=0)^(5-k) B_i binom(5-k,i) v^i(1-v)^(5-k-i).

Here padding by zero power coefficients is allowed, and the derivative includes the factor h^(-k). For n=5-k the exact conversion is

    B_i=sum_(j=0)^i a_j binom(i,j)/binom(n,j).                        (3)

To verify(3), expand v^j as sum_(i=j)^n[binom(i,j)/binom(n,j)]binom(n,i)v^i(1-v)^(n-i). The coefficient product equals binom(n-j,i-j)v^j, and summing the remaining binomial terms gives v^j. This proves the basis identity.

All Bernstein basis functions are nonnegative on[0,1] and their sum is1. Consequently min_i B_i<=q_k(v)<=max_i B_i and

    |q_k(v)|<=max_i|B_i|.                                          (4)

Subdividing a cell into any finite rational partition and applying(4) on each piece remains a rigorous bound. We use a fixed dyadic depth, with de Casteljau's exact rational recurrence to obtain the smaller Bernstein nets. The recurrence follows directly by substituting an affine restriction into the polynomial identity. No root finder is needed, and convergence of the subdivision algorithm is not assumed for validity of a finite certificate.

The upper bound u_k is the maximum absolute Bernstein coefficient over all pieces. The lower bound l_k is the maximum of absolute values at their endpoints and midpoints, evaluated exactly from the same polynomials. Each such value belongs to the global range, so it is a valid lower bound. A small gap u_k-l_k demonstrates sharpness of the finite enclosure; it is not needed for correctness.

## An independent checker

The generator may use exact Cox recursion to construct each polynomial and the explicit conversion(3). The checker instead verifies the archive decode, then uses exact pointwise de Boor evaluation on the original knot vectors. It verifies nondecreasing knots, endpoint multiplicity6, interior multiplicity at most3, coefficient count, and identical exact b,L. Each archive must use the same r2 compactification, mask rule and first-cosine projection. At t=1 the evaluator uses the last nondegenerate span, hence the left endpoint limit. Derivative splines are generated algebraically by

    d_i = d (c_(i+1)-c_i)/(knot_(i+d+1)-knot_(i+1)),

with the first and last knots removed and degree reduced from d to d-1; terms with zero denominator have coefficient0. This is the derivative identity obtained by differentiating the two terms in the B-spline recursion and collecting neighboring coefficients. For k<=2 it yields the physical t derivative. Under the C2 multiplicity assumption its endpoint values agree with the continuous derivative.

On a proposed leaf interval, a derivative has degree at most n=5-k. The checker evaluates its stored Bernstein polynomial and the difference of the two independently evaluated derivative splines at the checker-chosen n+1 distinct rational points v=i/n, i=0,...,n, of that leaf. It first verifies that the stored net has exactly n+1 entries, so its degree is at most n. Their difference is a polynomial of degree at most n, with n+1 zeros; polynomial division by each distinct linear factor shows it is identically zero. Thus these evaluations are an exact polynomial identity test, not a sampling test for positivity. The checker also verifies that the leaf intervals are ordered, cover[0,1] without gaps or overlaps, and do not cross any knot of either spline. These checks establish the prerequisite that each comparison involves a single polynomial piece. It recomputes both maxima in(1) from the verified Bernstein nets and exact endpoint/midpoint values. A certificate with an altered coefficient, omitted cell or wrong derivative scaling is rejected.

The JSON inputs, archive checksums, decode script and both evaluator scripts are part of the build inputs. Importing the numerical data does not prove(1); the exact identities and rational inequalities are the proof of the certificate's assertion. No Lean or Lake build is used or claimed.

## Control of the inverse functional

With p_j=P^(j)(0)/j!, the definition is

    J_b(P)=sum_(j=0)^2 p_j/(j+1-b)
            + integral_0^1 z^(-b)[P(z)-p_0-p_1 z-p_2 z²] dz.

The two fields have identical b,L, so their J_b difference is J_b of their difference. Global C2 quintics are smooth on the initial cell[0,delta], and the remaining compact interval is away from the singular endpoint, so the displayed integral converges.

Packet181 proves for M=||P''||_infinity the bounds |R(z)|<=17 M z³/(3delta) on[0,delta] and |R(z)|<=M z² on[delta,1]. The first follows by interpolating the cubic P'' on the first cell, bounding its derivative by34M/delta, and Taylor's integral remainder. The second follows by twice integrating P''(s)-P''(0). Integrating these two estimates against z^(-b) gives exactly the brace in(2), multiplied by M. The absolute Taylor terms give the first three summands. Substituting the certificate upper bound u_2 proves(2).

If the numerical value delta^(-gamma) is needed rigorously, use a rational enclosure for delta^(1-gamma) and divide by delta. The power-enclosure routine is the previously checked rational log/exponential certificate of111. The brace is increasing in that power; replacing it by its upper endpoint preserves the bound. All remaining factors in(2) are positive rational numbers. The finite-part constants themselves are certified independently by the N-fold rational integration formula of111, whose archive decode is the same exact mask and projection used here. Packet181 derives the functional norm estimate;111 supplies the distinct exact-value certificates, including the current stored states, so subtraction of their two rational intervals encloses the actual difference without relying on(2).

## Verified applications and controls

Completed UTC 2026-10-21T16:28:30.268480+00:00. The common exponent is exactly b=6963690923821629/2251799813685248, the stored binary floating-point value of3.0925. It is not the exact rational1237/400. The common scale is exactly L=3/2. All five original scalar inputs passed archive decoding and knot validation, with every interior knot simple (thus in particular of multiplicity at most3). Endpoint derivatives through order2 are continuous across all interior knots. The half-open de Boor convention therefore evaluates the same endpoint value as the adjacent polynomial piece.

The following tables display rounded rational enclosure endpoints. The authoritative exact rational intervals and upper bounds are in verification/summary.json and the individual certificate JSON files. A displayed zero-width interval can represent distinct exact endpoints that round to the same number. No displayed rounded decimal is used as a certificate input.

| Difference from Nt56/K24 | sup abs D | sup abs D prime | sup abs D double prime | C2 difference | Bound (2) |
|---|---:|---:|---:|---:|---:|
| Nt56/K32 | [1.828789522e-07, 1.828800039e-07] | [1.61660845e-06, 1.616664054e-06] | [0.000204330723, 0.000204330723] | [-0.002789897189, -0.002789897189] | 0.01107068765 |
| Nt84 initial refit | [2.926964015e-06, 2.926964015e-06] | [0.004332124468, 0.004332124468] | [2.36649686, 2.36649686] | [-71.66913511, -71.66913511] | 159.3311396 |
| Nt84 accepted | [0.000100028286, 0.000100028286] | [0.01722287978, 0.01755987889] | [7.603476304, 7.603476304] | [-240.5751741, -240.5751741] | 511.8962895 |
| Nt56/K24 tightened | [3.353276634e-07, 3.353276634e-07] | [1.340179961e-06, 1.34300945e-06] | [0.0001312683429, 0.0001312683429] | [-0.003768823641, -0.003768823641] | 0.008425568814 |


The baseline scalar norms are [2.673922447, 2.673922447], [3.949083085, 3.949094735], [33.4162858, 33.41828174], respectively for derivative orders0,1,2. These were independently certified against an explicitly zero spline on the same mesh. The synthetic input has no associated candidate archive: its zero coefficients are checked exactly, while the original baseline archive is decoded independently. Ratios to the corresponding baseline norms, and to the absolute baseline inverse constant, are enclosed by division of positive rational intervals:

| Difference | Relative order0 norm | Relative order1 norm | Relative order2 norm | Relative absolute C2 difference |
|---|---:|---:|---:|---:|
| Nt56/K32 | [6.839351395e-08, 6.839390729e-08] | [4.0936178e-07, 4.093770679e-07] | [6.114339588e-06, 6.114704795e-06] | [6.153221187e-06, 6.153221187e-06] |
| Nt84 initial refit | [1.094633099e-06, 1.094633099e-06] | [0.001096991781, 0.001096995017] | [0.07081443859, 0.0708186683] | [0.1580689218, 0.1580689218] |
| Nt84 accepted | [3.740882094e-05, 3.740882094e-05] | [0.004361222239, 0.004446571143] | [0.2275244539, 0.2275380438] | [0.5305974226, 0.5305974226] |
| Nt56/K24 tightened | [1.254066526e-07, 1.254066526e-07] | [3.393638418e-07, 3.400813357e-07] | [3.928039864e-06, 3.928274484e-06] | [8.312279595e-06, 8.312279595e-06] |


The initial Nt84 refit differs by about1.09e-6 relative in order0, by0.110percent in order1 and by7.08percent in order2; its inverse constant differs by15.81percent. After the Nt84 solve, these relative differences are about3.74e-5,0.436-0.445percent and22.75percent, while the inverse constant differs by53.06percent. The two rows must not be conflated. Angular refinement and tightening the tolerances have much smaller differences for this particular scalar. These observations isolate no numerical error source. They demonstrate finite-state sensitivity, while the theorem181, not these four comparisons alone, proves the failure of uniform control from weaker norms. The norm bound uses only the order2 upper bound and the three endpoint derivatives. The wider order1 enclosure for the accepted Nt84 difference does not enter that bound.

The exact functional differences are enclosed by the separate111 value certificates. Bound(2) is conservative for these four comparisons, as checked by exact rational inequality against both endpoints of each difference interval. No claim of a generally small or sharp bound for arbitrary data is made.

The four real pair certificates contain40320 exact polynomial node identities, with counts6720,13440,13440,6720. These are the degree-bounded identity tests in the proof, not point samples offered as a supremum argument. They completed in31.048158609s, from2026-10-21T16:22:29.576173+00:00 to2026-10-21T16:23:00.624335+00:00, using one CPU thread at nice19. The baseline norm adds6720 such identities and3.966638244s. Its role and synthetic zero input are recorded separately.

Five manufactured function pairs passed: an identical quadratic on unequal meshes; a quadratic with exact interior maximum1/4 and derivative norms1 and2; a constant shift; a quintic; and its reversed difference. They contain900 exact identities in total. Six corruptions were rejected: wrong net degree, a changed derivative net, a missing leaf, overlapping leaves, an incorrect global upper bound and an incorrect endpoint derivative. The controls completed in0.384250198s. The quadratic test first demanded an exact point enclosure, which is not guaranteed by finite Bernstein subdivision. It was corrected to require containment of the known norm and a small gap; the final rational enclosure[1763/7056,1765/7056] correctly contains1/4. This was a faulty test expectation, not evidence that an invalid certificate passed.

Reproduce with the four scripts native_spline_difference.py, check_native_spline_difference.py, run_native_spline_difference.py and certify_native_spline_reference_norm.py under code_independent. The controls are test_native_spline_difference.py. Generator and checker have different polynomial evaluation algorithms. Neither imports the numerical lane's code. The certificates prove statements about the exact stored scalar representations only. They do not certify the complete smooth B2 profile class, PDE residuals, a branch fold, a continuum refinement limit or error relative to an unknown solution.
