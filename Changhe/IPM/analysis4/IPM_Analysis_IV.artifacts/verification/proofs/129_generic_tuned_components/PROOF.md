# Generic compatible profiles on a regular component at c=3

Status: PROVED. The theory part independently derived TheoremT.8 at2026-10-31T10:10Z; its broader analytic-submanifold version was checked against this argument at2026-10-31T10:13:32Z. This result is componentwise. It makes no assertion about a compatibility component that contains no known profile with all nonzero responses and nonzero limiting response.

## Statement

Fix an even B>=4. Let S_B be the real vector space of sine polynomials

    f=sum_(j odd, 1<=j<B) a_j sin(j theta),

with norm sum |a_j|. Let O6(f) and sigma_k(f), k>=2, be the sixth-order compatibility obstruction and the cubic responses of the c=3 recurrence in119. The responses are defined by their three response equations for every f, whether or not O6(f)=0. Define the regular compatibility hypersurface

    R_B={f in S_B: O6(f)=0 and dO6(f) is nonzero}.

There is a homogeneous cubic polynomial sigma_infinity on S_B such that sigma_k converges to sigma_infinity uniformly on each bounded complex coefficient set, at rate O_B,A(1/k) when ||f||<=A.

Let M be a connected component of R_B. Assume M contains f_* such that

    sigma_infinity(f_*) != 0,
    sigma_k(f_*) != 0 for every k>=2.                         (H)

Then

    G_M={f in M: inf_(k>=2)|sigma_k(f)|>0}

is relatively open and dense in M. Its complement has measure zero in every smooth coordinate chart of M and is contained in a countable union of smooth hypersurfaces in such charts. Every f in G_M has the uniquely tuned convergent pure density and stream series of TheoremT and the convergent potential of121. Every compact subset of G_M has a common sufficient exterior radius and all weighted derivative bounds.

Hypothesis(H) holds for each component containing either verified profile sin(theta)+b_i sin(3theta), where b_i is one of the two real sextic roots in119. This applies for every fixed even B>=4, by embedding the profile with zero higher coefficients. Therefore the theorem is unconditional on those components. Other components and singular points of O6=0 remain outside its conclusion.

## 1. Eventual rational dependence on the resonance index

Write n=3k and m=2k-2. The unit free stream perturbation has frequency m. The first three unperturbed density terms f1,f2,f3 and streams g1,g2 are fixed polynomials in the leading coefficients, of their respective homogeneous orders. They have angular supports at most B-1,2B-1,3B-1 and B,2B.

The response equations of119 construct phi1 at n+1 from the unit perturbation and f1; phi2 at n+2 from the unit perturbation and f2, and the two orientations of phi1 with the order1 fields; phi3 at n+3 from the unit perturbation and f3, and the four orientations of the order1 and order2 fields with phi2 and phi1. There are only finitely many shifted frequencies, independently of k. Their supports are contained in

    phi1: m+[-B+1,B-1],       P_(n+1)phi1: m+[-B,B],
    phi2: m+[-2B+1,2B-1],    P_(n+2)phi2: m+[-2B,2B],
    phi3: m+[-3B+1,3B-1].

The statements follow by adding frequencies in each product and allowing the shift by1 in the Poisson forcing. For k>=2B+2, all these signed-frequency representatives are positive. Thus reflection of a negative sine frequency introduces no k-dependent case split. The target sigma_k is the coefficient of phi3 at frequency m+1.

Every radial exponent and angular frequency in this finite calculation is affine in k. Every stationary divisor is linear in k. Each nonresonant Poisson divisor is quadratic in k; it cannot vanish at n+1 or n+2, because these orders are not multiples of3 and positive even sine frequencies are the only allowed stream frequencies. The signs and supports have stabilized. Consequently each coefficient of a degree3 monomial in the leading amplitudes in sigma_k is, for all k>=2B+2, one fixed rational function of k with rational coefficients.

This argument concerns the response equations only. It does not require the full nonlinear recurrence at orders tending to infinity, and it does not assume compatibility away from O6=0.

## 2. A uniform cubic limit

Topic122 proves for complex coefficient vectors that

    |sigma_k(f)| <= M_B ||f||^3,
    M_B=(45/2)(7B/3)^3,                                    (1)

uniformly in k. Let d=B/2 and expand sigma_k as a homogeneous cubic in its d coordinates. On the complex coordinate polydisc |a_j|<=1, the right side of(1) is at most M_B d^3. The multivariable Cauchy coefficient formula therefore bounds every cubic coefficient uniformly by M_B d^3.

By the previous section each such coefficient is eventually rational in k. A rational function bounded on all sufficiently large integers has numerator degree at most denominator degree after cancellation. It therefore has a finite limit and differs from its limit by O(1/k). This also covers the identically zero function. There are finitely many cubic monomials, so their limits define a homogeneous cubic polynomial sigma_infinity. Summing the coefficient estimates gives

    sup_(||f||<=A) |sigma_k(f)-sigma_infinity(f)| <= C_(B,A)/k

for sufficiently large k. This holds over complex coefficient vectors. Both the finite formula and an admissible constant are computable from the fixed response calculation; no numerical sampling of k is needed for the existence statement.

## 3. Characterizing the uniform response condition

For every fixed f, convergence sigma_k(f)->sigma_infinity(f) gives the exact equivalence

    inf_k |sigma_k(f)|>0
      iff sigma_infinity(f)!=0 and sigma_k(f)!=0 for all k.  (2)

The forward direction follows by taking the limit. For the reverse, the tail has modulus at least half the positive limit modulus, and the finitely many preceding nonzero moduli have a positive minimum.

The set in(2) is open. At one of its points choose a bounded neighborhood on which sigma_infinity stays away from zero. Uniform convergence makes every sufficiently late sigma_k stay away from zero there; continuity handles the remaining finite set after shrinking the neighborhood. Alternatively the uniform Lipschitz estimate of122 gives the same openness directly.

On a compact subset K of G_M, finitely many such neighborhoods give a common lower response bound. The leading norms are also bounded on K. TheoremT uses only this lower bound, B and the leading norm bound, so its majorant gives one common exterior radius. The weighted spatial derivative bounds and the potential conclusion follow from119and121. This does not provide a useful numerical value for the common radius without bounds for the particular compact set.

## 4. Density and the exceptional set

M is a connected real analytic manifold, since dO6 is nonzero there. By(H), none of the analytic functions sigma_infinity or sigma_k restricts to the identically zero function on M. The identity theorem shows that each zero set has empty interior. Each is closed in M. The complement of G_M is exactly their countable union, by(2). Baire's theorem in locally compact coordinate neighborhoods therefore makes G_M dense in M.

For completeness, the stronger measure statement uses the following elementary analytic-zero argument. Let h be a nontrivial real analytic function on a connected coordinate domain. At any zero of h, some derivative of finite order is nonzero; otherwise its Taylor series would vanish and the identity theorem would force h to vanish identically. Choose the smallest such order. A derivative D^beta h of one lower order vanishes at that point and has nonzero gradient there. Thus the zero set of h is contained in the countable union, over beta, of the regular zero sets

    {D^beta h=0, grad D^beta h!=0}.

The implicit function theorem makes each one locally a smooth hypersurface, which has Lebesgue measure zero. A countable chart cover and a countable union over h=sigma_infinity,sigma2,sigma3,... prove the assertion on M. Smooth changes of coordinates preserve null sets locally. This is also the argument of Mityagin, cited below.

## 5. Verified components

On f=sin(theta)+b sin(3theta), the exact response limit from119 is

    sigma_infinity=-(75b^3+6735b^2-2925b+314)/129600.

Its value is nonzero at both verified sextic roots, and123 gives inf_k|sigma_k|=|sigma4|>0 there. The sextic roots are simple, so the partial derivative of O6 with respect to b is nonzero. Consequently both profiles belong to R_B for every B>=4. They satisfy(H), proving the asserted unconditional applications.

Dependencies:119for the exact response construction and base profiles;122for the uniform complex cubic estimate;123for the certified base response gaps;121for the potential. The additional analytic-zero reference is Boris S. Mityagin, “The Zero Set of a Real Analytic Function,” arXiv:1512.07276v1, Proposition0 and Claims1-2. Its primary-source text was checked on2026-10-31. The argument needed here is included above. This result does not prove that all regular components satisfy(H), that the sextic compatibility variety is irreducible, or that singular compatible profiles have convergent series.

## Independent comparison with TheoremT.8

The theory part independently gives the sharper stable-frequency threshold k>=3B/2+1. Then m=2k-2>=3B, so every response frequency is positive and the density inputs to the two Poisson inverses have frequency at least3. This confirms all divisor and support cases. Its proof also applies to an arbitrary connected real analytic submanifold Z of O6=0 containing one profile satisfying(H), including a nonsingular part of a compatible analytic curve. On such a curve the exceptional set is relatively closed and countable; its accumulation points within the curve lie among the isolated zeros of sigma_infinity. Endpoints outside the analytic parameter domain are not covered by that accumulation statement. The sufficient uniform response condition, not actual divergence at exceptional points, is what is characterized. The complete independent source theorem is retained in sources/lead_theorem_T8.md.
