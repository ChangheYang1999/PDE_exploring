# Normalized solid harmonics and their Cartesian derivative recurrence

## Exact statement

Let L and d be nonnegative integers and let x=(x_1,x_2,x_3) belong to R^3. Write w=x_1+i x_2 and rho=x_1^2+x_2^2+x_3^2. For integers 0<=m<=ell<=L define

    Z_(ell,m)(x) = w^m sum_(j=0)^floor((ell-m)/2)
       (-1)^j (2ell-2j)! x_3^(ell-2j-m) rho^j
       / [2^ell j! (ell-j)! (ell-2j-m)!],
    N_(ell,m) = sqrt((2ell+1)(ell-m)! / [4 pi (ell+m)!]),
    H_(ell,m) = (-1)^m N_(ell,m) Z_(ell,m).

All square roots in this statement are the positive real roots. These are complex homogeneous polynomials, including at x=0. The following recurrence computes exactly H and all its Cartesian derivatives of total order at most d:

    H_(0,0) = 1/sqrt(4 pi),
    H_(m,m) = -sqrt((2m+1)/(2m)) w H_(m-1,m-1),             1<=m<=L,
    H_(m+1,m) = sqrt(2m+3) x_3 H_(m,m),                    0<=m<L,
    H_(ell,m) = A_(ell,m) x_3 H_(ell-1,m)
                  - B_(ell,m) rho H_(ell-2,m),            m+2<=ell<=L,
    A_(ell,m) = sqrt((4ell^2-1)/(ell^2-m^2)),
    B_(ell,m) = sqrt((2ell+1)((ell-1)^2-m^2)
                    / [(2ell-3)(ell^2-m^2)]).

For a multi-index a in N^3, with D^a denoting the ordinary Cartesian partial derivative, use the two product rules

    D^a(x_k h) = x_k D^a h + a_k D^(a-e_k) h,
    D^a(rho h) = rho D^a h + 2 sum_k a_k x_k D^(a-e_k) h
                               + sum_k a_k(a_k-1) D^(a-2e_k) h.

A term with zero integer prefactor is omitted, so negative derivative indices are never required. The real campaign convention is H_(ell,0) for m=0, and sqrt(2)(-1)^m times Re H_(ell,m) or Im H_(ell,m) for m>0. The same conversion applies to every derivative.

## Proof

The polynomial identity in angular_polynomials/PROOF.md identifies Z with the regular solid harmonic without the Condon-Shortley sign. Equivalently it follows directly by differentiating the explicit Legendre polynomial m times, multiplying by r^ell sin(theta)^m exp(i m phi), and expanding r^2=rho. Polynomial continuity includes the origin and the axis.

The associated Legendre recurrence, or direct comparison of the factorial coefficients in the displayed sum, gives

    Z_(m,m) = (2m-1) w Z_(m-1,m-1),
    Z_(m+1,m) = (2m+1) x_3 Z_(m,m),
    (ell-m) Z_(ell,m) = (2ell-1) x_3 Z_(ell-1,m)
                              - (ell+m-1) rho Z_(ell-2,m).

These are polynomial identities for every x. The first two follow from the single j=0 term. The third is the usual associated Legendre recurrence after homogenization; homogenization multiplies the last term by rho because its degree is two lower. Thus it remains valid where spherical coordinates degenerate.

Multiply each identity by (-1)^m N_(ell,m). The diagonal changes the sign because m decreases by one on its right side. Its normalization ratio is

    (2m-1) N_(m,m)/N_(m-1,m-1) = sqrt((2m+1)/(2m)).

The next diagonal has ratio (2m+1) N_(m+1,m)/N_(m,m)=sqrt(2m+3). In the last recurrence, the squared ratio multiplying x_3 is

    [(2ell-1)/(ell-m)]^2 [N_(ell,m)/N_(ell-1,m)]^2
       = (4ell^2-1)/(ell^2-m^2).

The squared ratio multiplying rho is

    [(ell+m-1)/(ell-m)]^2 [N_(ell,m)/N_(ell-2,m)]^2
       = (2ell+1)((ell-1)^2-m^2) / [(2ell-3)(ell^2-m^2)].

The ratios are positive in the stated ranges, proving A and B. Their denominators are nonzero. Starting with H_(0,0), the diagonal, next diagonal and ascending ell recurrence therefore give the stated polynomials by induction.

Apply the multi-index Leibniz rule. The only nonzero derivatives of x_k are its value and its first k derivative, yielding the first product rule. The only nonzero derivatives of rho are rho, 2x_k and the diagonal second derivatives 2. The binomial coefficient a_k choose 2 multiplied by 2 is a_k(a_k-1), yielding the second rule. Thus one can propagate D^a H in the same recurrence, using derivatives of total order at most |a|. Induction on ell proves every propagated derivative. Constant H_(0,0) has zero positive-order derivatives. Since polynomial mixed partial derivatives commute, one stored entry for each multi-index suffices; permuting its differentiation axes does not change the exact value.

Finally, H=(-1)^m N Z and (-1)^(2m)=1 give the stated conversion to the no-sign real convention. This proves the exact statement.

## Dependencies, implementation and scope

Dependencies are the explicit Legendre formula and associated recurrence, factorial arithmetic, polynomial continuation, and the multi-index Leibniz rule. The reference implementation is independent/src/mp_angular_recurrence.py. It uses local 70-digit Decimal arithmetic and constants evaluated with 90-digit mpmath arithmetic, and converts the exact binary64 input coordinates with Decimal.from_float. Its recurrence is normalized and complex; its derivatives use these product identities, not the production derivative ladders.

The qualification script compares selected modes and all requested derivative multi-indices with exact rational monomial differentiation evaluated at 90 digits. This cross-check is numerical evidence, not a certified error enclosure for all inputs or degrees. No claim about the rounding error of the 70-digit algorithm follows from the exact theorem alone. No formal proof is provided and no Lean or Lake process was run.
