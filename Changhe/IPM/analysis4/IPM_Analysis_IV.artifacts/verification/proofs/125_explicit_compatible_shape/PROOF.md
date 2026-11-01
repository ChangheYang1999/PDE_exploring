# An explicit disk of compatible three-mode profiles

Status: PROVED. The complete argument and finite certificates were independently reviewed and confirmed by the theory part at2026-10-31T10:07Z. Exact hypotheses and scope remain as stated below.

## Statement

Let O(b,tau) be the coefficient of sin(theta) in the sixth density term obtained by the exact c=3 recurrence from

    f1=sin(theta)+b sin(3theta)+tau sin(5theta).

This is a rational polynomial of total degree at most six in b and tau. At tau=0 it is P6(b)/35818438656000000, with P6 as in topic119. Let I=[l,u] isolate either real root b* of P6 and put m=(l+u)/2. Expand

    O(m+x,tau)=sum c_ij x^i tau^j,
    A=c_10.

Choose positive rational h and t0 such that

    (u-l)/2 < h,
    sum_((i,j)!=(1,0)) |c_ij| h^i t0^j < |A|h,             (1)
    h+(u-l)/2+t0 < 1/790272000000.                         (2)

Then there is a unique holomorphic b(tau) on a neighborhood of the closed complex disk |tau|<=t0 with |b(tau)-m|<h and O(b(tau),tau)=0. It satisfies b(0)=b*, and is real for real tau. Every corresponding real profile generates the tuned convergent exterior series of topic122. The uniform radius supplied by topic124 is R>2^72 if that refinement is established; the earlier radius is R>2^240.

## Complete argument

On |x|=h and |tau|<=t0, inequality (1) gives

    |O(m+x,tau)-Ax| < |Ax|.

The homotopy Ax+s[O(m+x,tau)-Ax], 0<=s<=1, has no zero on the circle. Its winding number about zero is therefore the winding number of Ax, namely one. The argument principle implies that O(m+x,tau) has exactly one zero inside, counted with multiplicity. That zero is simple. The strict finite inequality continues to hold for a slightly larger tau disk. The analytic implicit function theorem provides local holomorphic root branches there; uniqueness makes these branches agree on overlaps, yielding the asserted single branch. At tau0, the known algebraic root lies inside the circle and must be this root. For real tau, conjugation gives another root in the same disk, so uniqueness makes the root real.

The profile distance from the central profile is

    ||f_tau-f_*||_1=|b(tau)-b*|+|tau|
                 < h+(u-l)/2+t0.

By (2), every profile lies inside the uniform response neighborhood proved in topic122. Its exact compatibility is O6=0 by construction. TheoremT gives the unique tuned solution; the common majorant bound supplies uniform convergence and all weighted derivative bounds. The shape variation is nontrivial because the coefficient of sin(5theta) is exactly tau, while the coefficient of sin(theta) remains one. This is a fixed-c family, not an assertion about an open interval of similarity exponents.

## Finite certificate specification

Compute O from signed Laurent Cartesian derivatives, independently of the theory part's Fourier code. Verify its restriction at tau0 against topic119. Use the exact 20-decimal isolating intervals already certified in topic120, set h=10^(-13), and test t0=10^(-j) for positive integers j until (1) and (2) both hold. Retain all coefficients, exact disk bounds, failed earlier trials and the selected positive t0. The derivative b'(0)=-O_tau(b*,0)/O_b(b*,0) can be enclosed independently by rational interval or ball arithmetic, but is not needed for existence.

Dependencies: the exact recurrence in topic119, the response-neighborhood proof of topic122, and the elementary argument principle. Topic124 is needed only for the improved displayed exterior radius. The exact certificate passes with h=10^(-13), t0=10^(-13) for the first root and t0=10^(-14) for the second root. The exact polynomial has total degree six and its restriction at tau0 agrees with topic119. The computed tangents are b1'(0)=0.82696011749974457737644095888662259912395820738331337754478748075 +/- 2.51e-67 and b2'(0)=1.3883180477148787664209474278385528681369017331949709849138171515 +/- 1.58e-65. The tangents are finite checks; existence uses the exact circle inequalities, not a linear approximation. The original all-order conclusions are PROVED after the independent review recorded above, including topics122 and124.

## Proposed exact recentering refinement

This paragraph is an additional refinement awaiting independent review; the original theorem centered at the rational m is already PROVED. The same disk may be stated with the algebraic root b_i as its center, with exactly |b-b_i|<h=10^-13 and no interval-width qualifier.

Indeed both certified circle ratios are less than9/10. At the unique zero in |b-m|<h, the equation gives |b-m|<(9/10)h. The retained intervals have width at most2*10^-20, so |m-b_i|<=10^-20=10^-7 h. Thus this zero lies strictly inside |b-b_i|<h. For uniqueness there, apply the same circle estimate at h'=(101/100)h. The total polynomial degree is6, so its remainder bound grows by at most(101/100)^6, while the linear term grows by101/100. The enlarged circle ratio is therefore less than(9/10)(101/100)^5<1. It contains exactly one zero. Since the disk centered at b_i of radius h lies inside the disk centered at m of radius h', uniqueness follows. The parameter radii, response neighborhood and exterior bound remain unchanged.
