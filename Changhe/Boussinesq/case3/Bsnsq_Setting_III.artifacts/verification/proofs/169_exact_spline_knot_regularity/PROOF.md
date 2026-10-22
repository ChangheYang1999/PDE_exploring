# Exact smoothness tests at radial spline knots

Written 2026-10-21, shift 6, before the certificate implementation. Status: CONFIRMED. The proposition below is proved and three frozen archive applications passed the exact independent checks recorded in verification/. This is a representation audit, not a B2 nonexistence theorem.

## 1. Statement and notation

Let p be a positive integer. Let 0=t_0<t_1<...<t_N=1 be simple interior breakpoints, with clamped endpoint multiplicities p+1, and let B_j be the degree-p B-spline basis. The knots and coefficients are exact real numbers. For the numerical certificates they are the exact binary values recorded in JSON, not rounded decimal approximations. Fix b,L>0 and set

    t(r)=1-(1+r^2/L^2)^(-1/(2b)),
    d(r)=r/sqrt(r^2+L^2),
    S_n(t)=sum_j c_nj B_j(t),
    Q(r,phi)=(1-t(r))^a sum_(n=0)^(K-1) d(r)^(n mod 2) S_n(t(r)) cos(n phi).

Here x=r sin(phi), y=-r cos(phi); K is finite; a is any real exponent. The masking of inactive coefficients, when present, is part of c_nj. Define Theta=x^2 Q with a=b+2, or Omega=x Q with a=b+1. These are the explicit r2 trial formulas, with separate arrays for the two fields.

At each interior knot t_i define

    J_ni = S_n^(p)(t_i+) - S_n^(p)(t_i-).

All derivatives below are one-sided where required.

(i) Away from the origin, Q is C^(p-1) and piecewise real analytic. It is C^p across the circle r=r_i=t^(-1)(t_i) if and only if J_ni=0 for every n. It is smooth across all the knot circles if and only if every S_n is the restriction of one polynomial of degree at most p. The same conclusions about failure of C^p hold for Theta and Omega: a nonzero jump occurs at some point with x nonzero.

(ii) A particularly simple sufficient test uses y=0 and x=r>0. Set

    J_i^axis = sum_(even n) (-1)^(n/2) J_ni.

If J_i^axis is nonzero, then the p-th Cartesian x derivative of Theta, respectively Omega, has a nonzero jump at (r_i,0), equal to

    r_i^2 (1-t_i)^a [t'(r_i)]^p J_i^axis,
    r_i   (1-t_i)^a [t'(r_i)]^p J_i^axis.

All prefactors are strictly positive. This test therefore reduces smoothness failure to exact rational arithmetic whenever knots and coefficients are rational, even though r_i itself generally is not rational. A zero value of this one test is not sufficient for smoothness.

(iii) Interior derivative coefficients, and hence the J_ni, can be computed exactly by repeated divided differences. Starting with degree p, knots k, and coefficients c_j, replace

    c_j by p (c_(j+1)-c_j)/(k_(j+p+1)-k_(j+1))

and remove the first and last knot, then decrement p. Repeat until degree zero. Denominators are positive for the clamped simple-knot representation used here. The resulting degree-zero coefficients are the constant p-th derivatives on successive nonempty knot intervals. Their adjacent differences are the jumps. This prescription is equivalent to the exact derivative of the represented function, not an estimate by finite differences.

## 2. Proof of the radial and angular assertions

At a simple knot, a degree-p spline has matching derivatives through p-1. On either adjacent interval it is a polynomial. Therefore the only possible order-p jump is J_ni. The radial map is real analytic with

    t'(r)=r/(b L^2) (1+r^2/L^2)^(-1/(2b)-1)>0

for r>0. Its inverse is real analytic locally. The envelopes and d are positive and real analytic there. Repeated product and chain rules show that all lower-derivative terms match; the remaining jump in the p-th radial derivative is

    (1-t_i)^a [t'(r_i)]^p sum_n d(r_i)^(n mod 2) J_ni cos(n phi).

The finite cosine functions are linearly independent on every open angular interval. Consequently the jump vanishes for all phi precisely when all J_ni vanish. If at least one coefficient is nonzero, the nonzero trigonometric polynomial cannot be supported only on the two axis angles x=0. It is nonzero at some angle with x nonzero. Multiplication by x or x^2 cannot remove that jump there: their lower-order product-rule terms match. This proves the corresponding failure for the original fields.

At phi=pi/2, odd modes vanish and cos(n pi/2)=(-1)^(n/2) for even n. Varying r along this ray is exactly varying the positive Cartesian coordinate x with y=0, which gives the displayed witnesses in (ii).

If every J_ni vanishes, the p-th derivative of S_n agrees on adjacent intervals. It is therefore one constant on (0,1). Integrating p times and using the already matching lower derivatives shows that S_n is one polynomial of degree at most p. Conversely a polynomial has no jumps. This proves the all-knots equivalence. The assertion is about finite p and a finite number of knots and angular modes. It makes no assertion about regularity at the origin unless the center masking is also checked.

## 3. Proof of the exact arithmetic recurrence

The degree-p B-spline identity is

    d B_(j,p)/dt = p B_(j,p-1)/(k_(j+p)-k_j)
                  -p B_(j+1,p-1)/(k_(j+p+1)-k_(j+1)),

with zero terms for repeated-knot zero denominators. It follows directly by differentiating the polynomial recursion defining B-splines; the degree-one case follows by differentiating the two affine pieces, and induction gives the identity. Summing against c_j, shifting the second sum, and dropping the two endpoint zero-support terms gives the coefficient recurrence in (iii) on the knot vector with its ends removed. Repetition reaches degree zero. For a clamped vector with only simple interior knots, each remaining denominator spans a positive interval. Each output coefficient belongs to the corresponding nonempty breakpoint interval, so subtraction of adjacent output constants gives the stated one-sided jump. This also specifies an independent checker using exact piecewise polynomial recursion instead of the derivative-coefficient recurrence.

## 4. Scope and possible smoothing

A nonzero exact jump rules out the literal finite field as a C-infinity profile. It does not rule out a nearby smooth field or an approximation sequence. The degree-five case is generally C4, which suffices for many first-derivative residual measurements. A small residual on either side of a knot cannot prove that the fifth derivative matches there.

Indeed, if the finite fields are already smooth at the center, their interior splines can be smoothed in small disjoint intervals around the knots, retaining the fields exactly near the center and in the final exterior interval. Convolution with a smooth compactly supported one-dimensional mollifier, joined with cutoffs inside those intervals, approximates each S_n in C^(p-1); for p>=3 it can be made arbitrarily close in C2. The same angular factors preserve parity. Fix these disjoint smoothing intervals before taking the mollifier scale to zero. The modifications then have support in one fixed finite annulus in physical space. Thus no finite-knot obstruction excludes such smooth replacements.

For completeness, the canonical relative inverse of a compact odd vorticity change tends to zero in C1 on each fixed compact set when that change tends to zero in C2. For the velocity itself use the locally integrable kernel K and subtract K(-Y). For its derivative, integrate by parts to move one derivative to the compact C1 source; boundary terms vanish. The resulting K convolution is bounded on each compact by a constant times the C1 norm of the source on its fixed support. The subtracted center value has the same estimate. This estimate concerns delta V, the relative inverse of the compact vorticity change delta Omega. That velocity change is a constant plus a decaying function at infinity. For a statement about the full modified velocity, additionally assume that the original canonical relative inverse exists and is sublinear. Linearity then shows that the modified full inverse is still sublinear. If the modified vorticity is smooth also at the center, its full inverse is smooth. For the intended exponent a=b+1, the physical vorticity is O(r^(-1/b)) because the final-interval splines are bounded. The kernel difference is O(|X|/|Y|^2) for |Y|>2|X|, so the relative integral converges absolutely at infinity. Splitting at radii comparable to |X| bounds its growth by O(1+r^(1-1/b)) for b>1, O(1+log(2+r)) for b=1, and O(1) for 0<b<1, assuming local boundedness at the center. All three bounds are sublinear. This justifies the intended application; such conclusions do not follow from an arbitrary exponent a. The physical temperature instead has order O(r^(1-2/b)), which grows when b>2. First-order transport residuals therefore change continuously on each compact set whenever the original inverse exists. The center strain may change slightly; no exact center condition or exact PDE is asserted for the smoothed replacement.

## 5. Dependencies and evidentiary status

This proof uses finite-dimensional polynomial algebra, the B-spline recursion, analytic changes of one real coordinate, and the integrable two-dimensional velocity kernel. It imports no fitting-lane implementation. Packet12 gives the separate center Taylor restrictions; packet163 gives an independent, stronger low-order PDE rejection for the particular continuation states. No Lean or Lake build is authorized. Exact JSON jump certificates and separately implemented checks will be stored in verification/ and registered as build inputs.
