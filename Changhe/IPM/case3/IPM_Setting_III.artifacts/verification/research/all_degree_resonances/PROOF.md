# A lower bound for every real polynomial jet resonance

Status: independently proved below; exact cross-checks and model review pending. Date: 2026-10-20.

## Precise statement and scope

Let A>1 and a be real. For any odd degree d=2k+1>=3, consider polynomial pairs (h,chi) with h homogeneous of degree d, even in x and odd in y, and chi homogeneous of degree d+1, odd in both coordinates. Require

    (A*x*partial_x+y*partial_y-1)h+a*partial_x chi=0,
    -Delta chi=partial_x h.                                  (1)

In addition, require the coefficient of r^(d+1) sin((d+1)theta) in chi to be zero. This last condition fixes the highest harmonic stream term. It is the homogeneous linear problem for a density jet with that independent harmonic stream coefficient prescribed to be zero. It is not the unrestricted local homogeneous coupled problem: without this extra condition there is always a free harmonic datum.

A polynomial jet resonance means that (1) with this zero harmonic coefficient has a nonzero pair. Then:

* At degree 3, resonance holds exactly at a=4A.
* At every higher odd degree d>=5, no real resonance occurs for a<=4A. More precisely, every real resonance satisfies a>4A+d-5.

Thus among all odd polynomial degrees >=3 the smallest possible real resonance is a=4A at degree 3. This proves the all-degree lower bound that finite-degree numerical determinant samples do not establish. It does not bound the number of real roots above this threshold, nor assert all roots are real.

For a primary IPM profile, A=2c_l-1 and a=rho_y(0). These are the resonances of the linear jet solve after lower jets and the top stream harmonic datum are specified. Approaching a resonance need not force large coefficients: its inhomogeneous data can vanish in the obstructed direction. The result is not a nonexistence theorem for any range of a, and it does not classify the primary global profile problem.

## Monomial recurrence

Write

    h=sum_(j=0)^k h_j x^(2j)y^(2k+1-2j),
    chi=sum_(j=0)^k q_j x^(2j+1)y^(2k+1-2j),
    ell_j=2k+2j(A-1)>0.

The first equation in (1) gives

    ell_j*h_j+a*(2j+1)*q_j=0.                   (2)

For j=1,...,k, the coefficient of x^(2j-1)y^(2k+1-2j) in the second equation gives

    -2j(2j+1)q_j-(2k-2j+3)(2k-2j+2)q_(j-1)=2j h_j.

Substituting (2), without dividing by a or by a-ell_j, yields

    q_(j-1)= [2j(2j+1)/((2k-2j+3)(2k-2j+2))]
                         *(a/ell_j-1)*q_j.     (3)

All the q_j are therefore determined by q_k. If q_k=0 then all q_j and h_j vanish. Iteration gives

    q_j=C_(k,j) product_(i=j+1)^k(a/ell_i-1) q_k,
    C_(k,j)=(2k+1)!/[(2j+1)!(2k-2j+1)!].       (4)

The coefficient of sin((2k+2)theta) in
cos(theta)^(2j+1) sin(theta)^(2k+1-2j) equals
2^(-2k-1)(-1)^(k-j). To check this directly, take the coefficient of exp(i(2k+2)theta) in the product of the two exponential expansions, and convert it to a sine coefficient. There is no binomial factor at this highest frequency. Consequently the zero harmonic condition is

    sum_(j=0)^k (-1)^(k-j)q_j=0.

By (4), a resonance is equivalent to

    P_k(a)=sum_(j=0)^k C_(k,j)
                       product_(i=j+1)^k(1-a/ell_i)=0.         (5)

The recurrence and condition also prove sufficiency: take q_k=1, define the remaining coefficients by (3) and (2), and use (5). For a=0 this polynomial is strictly positive, so a nonzero pair at a root also has nonzero density. Equation (5) is an exact scalar determinant criterion, not a sampled calculation.

## Positivity below the threshold

For k=1, ell_1=2A and C_(1,0)=C_(1,1)=1, so P_1(a)=2-a/(2A). This proves the degree-3 statement.

Now let k>=2. If a<0, all factors in (5) are positive, so P_k(a)>0. Suppose instead

    0<=a<=ell_2=2k+4(A-1)=4A+2k-4.

For every i>=2, ell_i>=ell_2 and therefore 1-a/ell_i>=0. The only possibly negative factor is 1-a/ell_1, and it occurs only in the j=0 term. Combine the first two terms of (5):

    [1-a/ell_1+C_(k,1)] product_(i=2)^k(1-a/ell_i).

Here

    C_(k,1)=k(2k+1)/3>1,
    ell_2/ell_1=(2k+4(A-1))/(2k+2(A-1))<2.

The bracket is strictly positive. All remaining j>=2 terms are nonnegative, and the final j=k term equals C_(k,k)=1. It follows that P_k(a)>0 throughout this interval, including its endpoints. Thus every real root is greater than ell_2=4A+d-5, proving the claim.

## Dependencies and verification

The proof uses only finite polynomial algebra and the highest angular Fourier coefficient. Canonical inversion of a globally growing polynomial is not asserted. The role of the excluded harmonic term is exactly the one in ../indicial/PROOF.md and the cubic identity in ../origin/PROOF.md. Independent Fourier-basis tests in verification/ compare the criterion to the previously derived degree-3, degree-5 and degree-7 determinants. The argument above, not those finite checks, covers all degrees.
