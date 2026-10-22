# Angular identities, interval conversion and adaptive-cell audit

Written before the checking code, 2026-10-20. Status OPEN pending numerical checks and review. This result addresses the angular part of the frozen finite-flow source only.

## 1. Exact statement and notation

Let n be a positive integer, theta in[0,pi/2], and

 C_n(theta)=cot(theta)sin(2n theta),
 S_n(theta)=tan(theta)sin(2n theta).

At the apparent singular endpoints these denote their continuous polynomial extensions. Put C0(theta)=cos(2n theta). For any angular center theta0 and |z|<=d, each of these functions has Taylor coefficients f(theta0),f'(theta0),f''(theta0)/2 and remainder at most M_n d^3/6, with

 M_n=(2n)^3 for C0,
 M_n=4n^4+8n^3+4n² for C_n and S_n.                         (1)

The source uses the larger integer4n^4+8n^3+6n²+2n. Hence its analytic third-derivative majorant is valid. The theorem includes the axes, without division by sin or cos there.

For finite radial quantities P_n=2n psi_n/r² and R_n=psi'_n/r, the angular formulas are

 s=c_l-sum P_n cos(2n theta),
 V2/y=s+sum R_n C_n(theta),
 V1/x=s-sum R_n S_n(theta).                                (2)

The proof of these identities is independent of their numerical enclosures. The finite checks below cover all51000 possible angular cells from200 base intervals and at most7 binary refinements, and all261 modes at200 base centers plus21 specified refined centers. Only those221 center coefficient enclosures are independently recomputed; this is not a claim to have recomputed the coefficients at every possible refined center or any full radial field.

## 2. Polynomial formulas and derivatives

The geometric sine sum gives sin(2n theta)/sin(theta)=2 sum_(j=0)^(n-1)cos((2j+1)theta). Multiplying by cos(theta) gives

 C_n=1+cos(2n theta)+2 sum_(j=1)^(n-1)cos(2j theta).          (3)

A second telescoping geometric sum gives

 S_n=(-1)^(n-1)[1+(-1)^n cos(2n theta)
                    +2 sum_(j=1)^(n-1)(-1)^j cos(2j theta)]. (4)

These identities hold on the open quadrant and, being trigonometric polynomials, extend to both endpoints. Independently, the source represents C_n as cos(theta) times D_n=2 sum cos((2j+1)theta), and S_n as sin(theta) times E_n=2 sum (-1)^(n-1-j)sin((2j+1)theta). Direct differentiation gives exactly the source's three coefficient formulas; its variable E2 has the opposite sign of the second derivative before applying the final minus sign. There is no missing sign in that implementation.

For either product, Leibniz' rule and |D_n^(k)|,|E_n^(k)|<=2 sum_(j=0)^(n-1)(2j+1)^k imply

 |f'''|<=2 sum_(j=0)^(n-1)[1+3(2j+1)+3(2j+1)²+(2j+1)^3]
        =16 sum_(l=1)^n l³=4n²(n+1)².

This proves(1). Taylor's theorem on a closed interval proves its uniform remainder. The inequality holds at endpoints by continuity.

For(2), the convention U=(-psi_y,psi_x) gives U_r=-psi_theta/r and U_theta=psi_r. The Cartesian rotation gives U1/x=-psi_theta/r²-(tan theta)psi_r/r and U2/y=-psi_theta/r²+(cot theta)psi_r/r. Expanding the finite sine series proves(2), including the continuous axis extensions.

## 3. Conversion of Arb balls to binary64 boxes

Assume the Arb midpoint is converted to nearest binary64, all converted values are finite, and positive scalar operations obey the arithmetic model of topic72. For any real x and its nearest finite binary64 m,

 |x-m|<=u|m|+eta/2.                                        (5)

Indeed, the half-spacing on either side of a normal m is at most u|m|; for a subnormal the spacing is eta. At a binade boundary use the larger adjacent spacing. If b is an Arb ball with midpoint x and radius r, nearest conversion r0 of the radius satisfies succ(r0)>=r. Therefore the source formula

 succ(succ(succ(r0)+succ(u|m|))+eta)

is at least r+u|m|+eta and encloses b centered at m. Likewise `up` and `lo`, which take the successor or predecessor after converting an outward endpoint, are safe.

The public python-flint0.9.0 source `arb.__float__` uses arf_get_d(mid,ARF_RND_NEAR), as recorded in evidence/python_flint_arb_0_9_0.pyx.txt lines497-498. That reference supports the declared conversion model; downloading a source tag does not establish provenance of the installed binary. The finite coefficient comparisons below do not depend on claiming binary provenance from that download.

## 4. Angular partitions and cache keys

The exact base edges are q*pi with q=i/400, i=0,...,200. Refinement replaces[q_a*pi,q_b*pi] by the two intervals with midpoint(q_a+q_b)pi/2. Induction proves exact partition coverage and shows that depth at most7 produces200 sum_(j=0)^7 2^j=51000 potential nodes. Every potential true edge lies in(pi/51200)Z. The actual floating cache key is the four-tuple of converted Arb midpoints and radii of its two endpoints. Mathematical grid separation alone is not enough to validate this implementation; the checker constructs all actual Arb128 nodes in source order, compares each endpoint and half-width with independent Arb512 and iv180 values, and rejects any key shared by different exact rational edge pairs. This finite enumeration proves absence of collisions on this particular adaptive tree.

The exported half-width d is recomputed for every potential cell. For every distinct actual d and every n=1,...,261 the source's full binary64 remainder expression is compared to the exact rational value M_source(n)d³/6. This checks the actual powers and all composed rounding in that expression without assuming a general libm power error bound. It does not validate unrelated powers in the radial source.

## 5. Center coefficients and independent methods

For each of the200 base cells and three prescribed refined cells at every depth1,...,7 (the left edge, right edge and leftmost descendant of base100), evaluate the actual source at Arb128. Save all3 families times3 coefficients times261 modes as exact binary64 midpoint/radius arrays. Independently use Arb512 and mpmath.iv180 with the even-frequency formulas(3)-(4) and their derivatives. For each saved box, the independent interval minus its exact binary64 midpoint must have magnitude at most its exact radius. Comparisons are directed interval comparisons; no rounded decimal endpoint is used to accept containment.

A fresh auditor will use Arb1536 with an independent trigonometric recurrence and compare every saved box again, verify exact node identities and input hashes, and reconstruct the coefficient count. The logical claims still depend on trusted interval libraries. The actual source evaluator and both independent methods are run locally, single-threaded, with the ongoing heavy middle process paused and resumed.

## 6. Remaining scope

This proves the displayed exact identities and the stated finite angular checks if the recorded computations pass. It does not certify radial Taylor models, all possible refined-center numerical values, full finite-flow aggregates, a BLAS implementation, historical source provenance, the full inverse, or any existence/exclusion endpoint. In particular, a correct angular majorant is only one part of the full-field certificate.
