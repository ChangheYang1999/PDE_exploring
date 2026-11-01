# Stability on the rational compatibility hypersurface

Status: PROVED. The complete argument and finite certificates were independently reviewed and confirmed by the theory part at2026-10-31T10:07Z. Exact hypotheses and scope remain as stated below.

## Statement

Fix an even bandwidth B>=4 and equip the complex vector space of sine polynomials supported on1,3,...,B-1 with the sum of the absolute coefficient values. Let f* be a real polynomial in this space satisfying O6(f*)=0 and

    inf_(k>=2) |sigma_k(f*)| >= s*>0.

The obstruction O6 and cubic responses sigma_k are those in topic119. There is an open complex neighborhood U of f* on which every response remains nonzero and uniformly bounded away from zero. Every real f in U with O6(f)=0 therefore generates a convergent pure S1 density/stream series by the unique tuning in TheoremT. The convergence is uniform in f on a smaller neighborhood, including all appropriately weighted spatial derivatives. Each coefficient, and the convergent weighted sums on their common exterior domain, depend holomorphically on f restricted to O6(f)=0.

For either explicit profile f*=sin(theta)+b* sin(3theta), b* a real root of the sextic P6 in topic119, this gives a nonconstant analytic family

    f_tau=sin(theta)+b(tau) sin(3theta)+tau sin(5theta),
    b(0)=b*, O6(f_tau)=0,

for all sufficiently small real tau. The coefficient of sin(5theta) is an independent shape parameter, so this family is not merely amplitude scaling. A common exterior radius can be bounded constructively as described below. The canonical zero-multipole convention is not imposed.

## A uniform cubic response bound

Set kappa=7B/3 and L=3/2. The nonlinear norm estimate and Poisson bound in topic119 hold for complex sine coefficients, because their proofs use only the triangle inequality. Write a=||f||_1 and x_i=i||f_i||_1 for i1,2,3. The first three pure orders are independent of every resonant constant and satisfy

    x1=a, x2<=kappa L a^2, x3<=2 kappa^2 L^2 a^3.

Fix n=3k>=6. Perturb the entire harmonic stream coefficient H_n by1, leaving f_n and all previous coefficients fixed. Let phi_r be the resulting density change at order n+r, r1,2,3. These changes depend only on f1,f2,f3 and on the unit harmonic stream. They do not depend on earlier tuned multipoles: a nonlinear pair containing an H_n-dependent high order has its other index at most3. Two such high orders cannot occur in any of these sums because n+3<2n.

Put y_r=(n+r)||phi_r||_1/n. Applying the same norm estimate to these response equations gives

    y1 <= kappa x1,
    y2 <= kappa[x2+2L x1 y1],
    y3 <= kappa[x3+2L(x2 y1+x1 y2)].

The factor2 counts the two orientations of a high and a low index, and L bounds the Poisson inverse in each. The direct harmonic contribution is x_r. Thus

    y1<=kappa a,
    y2<=3 kappa^2 L a^2,
    y3<=10 kappa^3 L^2 a^3.

The response sigma_k is one sine coefficient of phi3. Consequently, for every k>=2 and every complex f in the stated finite-dimensional space,

    |sigma_k(f)| <= M_B ||f||_1^3,
    M_B=10 kappa^3 L^2.                                      (1)

Each sigma_k is a homogeneous cubic polynomial in f. This follows directly from the three response equations and the homogeneous degrees1,2,3 of f1,f2,f3. The bound is uniform over all k, including arbitrarily late resonances.

## Uniform openness of the response condition

Let A0>=||f*||_1. For any f with ||f-f*||_1<=1 and any unit direction h, the polynomial z -> sigma_k(f+zh) is bounded on |z|=1 by M_B(A0+2)^3. Cauchy's coefficient formula therefore gives

    |D sigma_k(f)[h]| <= M_B(A0+2)^3.

Integrate along the segment from f* to f. For

    ||f-f*||_1 < min(1, s*/[2 M_B(A0+2)^3]),                 (2)

we obtain |sigma_k(f)-sigma_k(f*)|<s*/2 simultaneously for every k. Hence all moduli are at least s*/2. This argument supplies uniform openness without interchanging pointwise limits or assuming a uniform rational-function expansion in k.

The O6=0 condition remains necessary. On its zero set inside (2), TheoremT applies with the same upper bound A0+1 on the leading norm, the same bandwidth, and the same lower response bound s*/2. Its nonnegative majorant system is therefore common to every profile in this neighborhood, yielding a common positive convergence radius and all weighted derivative bounds.

Every finite coefficient and tuning constant is holomorphic in f on this neighborhood: they are obtained by finitely many polynomial operations, fixed nonresonant Poisson inverses, and division by nonvanishing sigma_k. These formulas may be defined as algebraic formulas even off the compatibility zero set; their interpretation as a pure solution is restricted to that set. The uniform majorant proves normal convergence on smaller disks. Cauchy's integral formula then gives holomorphic dependence of the summed weighted fields. No assertion is made about pure solutions off O6=0.

## Nontrivial shape families through both sextic roots

Take B=6 and consider the polynomial

    O(b,tau)=O6(sin(theta)+b sin(3theta)+tau sin(5theta)).

At tau0 it equals P6(b)/35818438656000000. The sextic P6 is irreducible over the rationals and has characteristic zero, so it has no repeated roots. Thus partial_b O(b*,0) is nonzero. The complex analytic implicit function theorem gives a unique local holomorphic b(tau) with b(0)=b* and O(b(tau),tau)=0. Uniqueness and real coefficients imply that b(tau) is real for real tau. Shrink the parameter disk until (2) holds. TheoremT then proves the claimed nontrivial real analytic family. The same argument allows any finite list of higher odd sine modes as free shape parameters, after increasing B.

For these B6 families, take A0=2, kappa14, L3/2 and s*=1/100000, the latter certified for both central profiles in topic120. Then M_B=61740, and the sufficient profile-distance bound is

    ||f-f*||_1 < 1/790272000000.                            (3)

Indeed the denominator is 128 M_B times100000. The shape parameter disk is chosen so that |b(tau)-b*|+|tau| satisfies (3). This is a conservative neighborhood bound in profile space, not a numerical estimate for the maximal tau interval.

## A common constructive radius for the three-mode families

Inside (3), ||f||_1<=3 and every response modulus is at least1/200000. Use the majorant system in topic119 with

    a=3, kappa=14, sigma_*=1/200000,
    d=(3/2)kappa a^2=189, e=3 kappa a d=23814.

Write Phi=c+JY+z Psi, Q=(I-J)^(-1), Y0=Qc as in topic120. The same nonnegative formal iteration proves convergence at z0 if

    max Y0<=M,
    z0 max Q Psi(1,2M,2M,2M,2M)<=M.

The exact certificate verifies both inequalities with M=2^70 and z0=2^(-160). Therefore every member of the family converges with all weighted derivatives on the common exterior r>2^240. The potential-series reconstruction of topic121 would give the same radius for the potential, with its finite logarithmic corrections. The abstract common radius and the density/stream conclusion do not depend on that potential refinement or on this optional explicit certificate.

Dependencies: topic119 for the nonlinear estimate, response construction, and majorant theorem; topic120 for the uniform response bound of the two central profiles; the elementary Cauchy formula and analytic implicit function theorem. All arithmetic constants and exact inequalities are retained in verification. No claim about varying c or about a whole-plane stationary extension is included.
