# Source interval propagation and response to the first review

This addendum supplements PROOF.md and is written before the corrected calculation. The first run retained in evidence/run.log passed both engines' endpoint signs and the Arb whole-bracket inequalities, but failed an mpmath.iv whole-bracket inequality. It is a failed enclosure attempt, not evidence that the underlying inequality is false. Direct primitive subtraction loses shared-variable cancellation over a varying endpoint. The original code remains frozen as check_source.py. The corrected calculation is check_source_v2.py.

## A stable whole-bracket second method

Use the finite-primitive formula only at x=a and x=b, retaining every endpoint ball. For the whole bracket, take t0=log a and 0<=u=t-t0<=d_t, where d_t is a directed upper bound for log b-log a. If y'=lambda y+F(t) and |F|<=H on this interval, variation of constants gives

 |y(t)-y(t0)|<=d_t exp(|lambda|d_t)(|lambda||y(t0)|+H).

Indeed |exp(lambda u)-1|<=|lambda|u exp(|lambda|u), and the forcing integral is at most u exp(|lambda|u)H. The absolute value of the forcing sign is immaterial. For I use lambda=-m-4 and F=H_(n-1); for J use lambda=m-4 and F=-H_n. Each polynomial forcing bound is evaluated over the whole t interval, using its complete original polynomial. This encloses both canonical moments throughout the interval from the separately certified left endpoint. The primary engine continues using its signed exponential series over the whole interval. The two engines share exact inputs and accepted canonical anchors; their propagation and final arithmetic are separate. No claim of independent generation of the original density or anchor archive is made.

## Normalization, derivative identities and the auxiliary domain

The input k is an exact dyadic by definition in topic15 section1. It is distinct from the exact-real correction z in that topic's central-strain normalization section:

 z=(3/k-1-c0)/slope,
 sigma=c0+slope*z=3/k-1,
 c_l=(1+sigma)/3=1/k.

Thus setting c_l to the reciprocal of the exact dyadic k is correct and is not midpoint substitution for z. The canonical moment archive encloses the exact-real correction. Its accepted provenance, including normalization, remains an explicit shared dependency. The first model review conflated k with z; the full topic15 proof is supplied for follow-up.

The initial mode check merely compared hard-coded opposite vectors. It was a regression of listed coefficients, not an independent differentiation. The corrected exact check starts with independent formal symbols I,J,Hlo,Hhi, forms their ODE derivative, differentiates the radial velocity, and forms the angular derivative of psi_x at theta0 from

 psi_x=r^3/2[cos(theta)(4Y+Y')sin(mtheta)-m sin(theta)Y cos(mtheta)], Y=J-I.

Thus partial_y psi_x=r^2/2[m(4Y+Y')-mY]. Independently, d_x(-psi_y)=-m r^2/2[3Y+Y']. Both are compared to the coefficients actually used by the two engines. The exact arithmetic derives the ODE contributions before comparison; the universal identities follow by the displayed product and chain rules.

Here kappa=1687/500, s=31/10. The lower bound for the auxiliary gap requires only ||Dwvec||>=0:

 d=1+(A+mu)/2-kappa+s||Dwvec|| >=1+(10+99/100)/2-1687/500=3121/1000.

No upper enclosure of ||Dwvec|| is needed for this lower bound. The corresponding upper norms needed for E were already bounded in topics84-86.

Topic78 states explicitly that wvec,qvec are real C_c^4 vector fields and that the realization is the maximal distributional transport domain in H^(31/10). The fields constructed here are respectively C_c^6 and C_c^5 on their support and extend with those regularities by zero, so the stated C_c^4 hypotheses hold. Its R is a specified finite analytic expression and remains unevaluated numerically.

Both methods' moment overlaps are consistency diagnostics enforced as fail-fast assertions; they contribute no containment argument. Each endpoint sign and whole-bracket target must pass separately in each engine. All scope restrictions in PROOF.md remain, including the distinction between the trial and an exact stationary solution.
