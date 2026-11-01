# Necessary radii for the three two-mode profiles at delta4/7

Status: PROVED. The exact specialization, all seven low-order top coefficients, root enclosures and directed constants pass independent checks (V516).

## Statement and notation

Let b_1<b_2<b_3 be the three positive real roots of the exact compatibility polynomial in239. Fix i in{1,2,3}, a nonzero real epsilon, and the uniquely tuned stationary series with leading density epsilon(sin(theta)+b_i sin(3theta)) at delta=4/7, c=7/3. If its second angular derivative series converges uniformly term by term on the closed exterior r>=R with the natural density weight, then

    R > (b_i/R_H)^(7/4) |epsilon|^(7/4),
    R_H = (16/3) [(7/12) Gamma(7/12) Gamma(7/4) / Gamma(7/3)]^(12/7).

The statement is necessary, not sufficient. The separately admitted sufficient exponents are27,117/4,109/4. No equality between the necessary and sufficient radii is asserted.

## Proof

Write A_n for the coefficient of sin((4n-1)theta) in f_n. The sharp bandwidth is4n-1. Only the two highest participating frequencies produce this frequency in the quadratic recurrence. Every free stream harmonic has frequency delta n-2<4n, so tuning does not change this sector. The top stream coefficient associated with A_i is -A_i/[2((4-delta)i+2)]. Substituting the two top modes into the stationary bracket gives

    A_n = (-1)^(n-1)(epsilon b_i)^n h_n,
    4d(n-1)h_n = sum_{j=1}^{n-1} [8(n-j)/((4-delta)j+2)-1] h_j h_(n-j),
    h_1=1, d=4/3.

The general highest-sector theorem gives h_n R_H^n asymptotic to K n^(-1-1/beta), with K>0, a=2/(4-delta)=7/12 and beta=6/(4-delta)=7/4. Its radius is4d[a Gamma(a)Gamma(beta)/Gamma(a+beta)]^(1/a), exactly the R_H displayed above.

At r=(b_i/R_H)^(7/4)|epsilon|^(7/4), the highest Fourier coefficient of the weighted second angular derivative of the n-th term has positive modulus asymptotic to a fixed nonzero constant times n^(1-1/beta)=n^(3/7). Hence the terms do not tend to zero in uniform norm: a Fourier coefficient is bounded in modulus by a fixed constant times that norm. At smaller r the same coefficient additionally grows exponentially. Uniform termwise convergence therefore requires the strict stated inequality. The sign of epsilon is irrelevant because the obstruction uses moduli.

## Verification and scope

The arithmetic check independently evaluates R_H and all three root-dependent thresholds at512 and1024 bits with fresh input conversion, verify the exact rational constants, and compare the first seven highest coefficients with the separately computed exact prefix polynomials. Decimal lower bounds must be rounded downward before they can be inserted into a necessary inequality.

Dependencies: the highest-sector asymptotic theorem228 and the original general top-mode theorem; exact root isolation239; sufficient bounds247. This proof uses no finite fitted asymptotic data.

The unit-amplitude necessary thresholds are0.0127184082743191090002969589556,0.0430461204612887181771044679424 and0.880537369551225375578391902888. Thus the downward-rounded lower bounds0.0127184,0.0430461,0.880537 are valid. The slightly different longer decimals in the theory part request result from inserting roots rounded to ten decimal places; they are not the exact-root constants.
