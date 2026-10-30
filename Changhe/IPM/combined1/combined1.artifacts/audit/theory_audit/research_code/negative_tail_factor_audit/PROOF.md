# Independent check of the exterior Green-kernel factor

## Exact statement

Fix an integer n>=1, radius R>0, real coefficients e_j and finitely many exponents a_j<-2. Let F(r,theta)=1_(r>=R) sum_j e_j r^a_j sin(n theta). With the full-plane homogeneous norm ||F||H^2=<F,(-Delta)^-1 F>,

    ||F||H^2 = (pi/n) sum_(i,j) e_i e_j
               R^(a_i+a_j+4)/[(n-a_i-2)(-a_i-a_j-4)].         (1)

The sum is ordered. Its coefficient is pi/n. A formula pi/(2n) with the same ordered sum is false. No statement is made about truncation errors when F is only an asymptotic approximation.

## Proof by the radial Green function

The two homogeneous radial solutions of -p''-p'/r+n^2 p/r^2=0 are r^n and r^-n. Requiring regularity at zero, decay at infinity and the jump -[r partial_r G]_(r=s- to s+)=1 gives

    G_n(r,s)=(1/(2n))(min(r,s)/max(r,s))^n.

Thus the radial potential is integral G_n(r,s) f(s)s ds. Angular integration of sin^2(n theta) gives pi. On R<=s<=r the i,j monomial integral is

    integral_R^infinity integral_R^r
      r^(a_i+1-n) s^(a_j+1+n) ds dr
      = integral_R^infinity s^(a_j+1+n)
           [s^(a_i+2-n)/(n-a_i-2)] ds
      = R^(a_i+a_j+4)/[(n-a_i-2)(-a_i-a_j-4)].

The displayed exponents make both denominators positive and justify the exchanged integrals, first for positive monomials and then for their finite linear combination. The integrand of the full f(r)f(s) integral is symmetric in r,s. Its two triangles have equal integrals, and the diagonal has measure zero. Hence multiplication by pi/(2n) for the full square gives pi/n for one triangle's ordered expansion. This proves(1). It also covers a_j+n+2=0 without dividing by that quantity.

## Independent source with an explicit potential

Take n=1, R=1 and f(r)=r^-4 for r>=1, zero inside. The potential's radial factor is

    p(r)=r/6 for r<=1,
    p(r)=1/(2r)-1/(3r^2) for r>=1.

It solves the radial equation in each region. At r=1 its values both equal1/6 and its derivatives both equal1/6, so no interface measure is added. It is regular at zero and tends to zero at infinity. Consequently

    ||F||H^2/pi = integral_1^infinity r^-4 p(r) r dr
                = 1/6-1/12=1/12.

Formula(1) gives the same value. Replacing pi/n by pi/(2n) gives pi/24 instead. This counterexample is exact, positive and independent of any IPM candidate.

## Implementation scope

The frozen N1 source is copied in source/N1_ipm_hminus1.py and is read only as text; it is not executed. Its tot_oo loop sums all ordered exponent pairs for one triangular integral, then multiplies by pi/(2n). This precisely matches the refuted formula. The corrected exterior coefficient must be pi/n, or the loop must explicitly include both triangles. This audit does not certify the source's other quadratures or claim that its owner has already repaired the file.

The local script checks the radial differential equation, continuity, and both norm formulas with exact symbolic arithmetic. Evidence belongs in verification/. N4's mathematical diagnosis is independently CONFIRMED upon successful execution, and the frozen N1 exterior factor is REFUTED.
