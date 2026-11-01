# Six algebraic leading profiles at c=5/3

Status: PROVED. The independent theory-part implementation reproduced every all-k lower bound and component radius on2026-10-31T10:51Z. V277 records the review and source evidence.

## Statement and exact definition of the six profiles

Let delta=2/5, c=5/3, p_n=1-2n/5 and lambda_n=2(n-1)/3. Starting with f_1=sin(theta)+b sin(3theta), define the nonresonant pure coefficients through order9 by

    -[partial_theta^2+(p_n+1)^2]g_n
        =p_n cos(theta)f_n-sin(theta)f_n',
    lambda_n f_n=sum_(i+j=n)[-p_j g_i' f_j+(p_i+1)g_i f_j'].

There is no positive even sine resonance before order10. Define f_10 by the same second equation and let O10(b) be its sin(theta) coefficient. Define P10 to be the primitive integer polynomial with positive leading coefficient proportional to O10. This finite recurrence defines P10 exactly, without choosing an approximate root or any free harmonic.

P10 has degree10 and is irreducible over the rationals. It has six real roots, one in each of the following open rational intervals, listed in increasing order:

    (-490,-489)/1000, (48,49)/1000, (125,126)/1000,
    (212,213)/1000, (315,316)/1000, (559,560)/1000.

For each such exact root b_i and every real epsilon!=0, the leading profile

    f_1=epsilon[sin(theta)+b_i sin(3theta)]

admits a unique pure S1 density/stream series with all later compatibility conditions satisfied by its harmonic stream coefficients. Its coefficients have geometric bounds. The series and every weighted derivative converge absolutely and uniformly on some exterior r>=R, producing an exact stationary self-similar IPM solution. It has a common potential with logarithmic corrections only at orders5and10. The sufficient exterior radius scales as |epsilon|^(5/2). No quantitative numerical radius for these six profiles is asserted by this result alone.

## 1. Finite algebraic certificates

The exact signed Laurent implementation in topic130 differentiates Cartesian monomials and computes all45 ordered nonlinear products through order10. Nine independent Poisson residuals vanish exactly, and all ten density fields have the required sine symmetry and support. The resulting rational polynomial O10 and the complete prefix are stored as exact JSON. Their primitive numerator P10 is the polynomial just defined by the recurrence.

A modular certificate proves irreducibility. Modulo11, after multiplying by the inverse of its leading coefficient, P10 has ascending coefficients

    [7,5,3,7,0,0,7,5,9,2,1].

For this monic degree-ten polynomial F over F_11, exact modular polynomial arithmetic verifies

    X^(11^10)=X mod F,
    gcd(F,X^(11^5)-X)=1,
    gcd(F,X^(11^2)-X)=1.

These conditions exclude every proper irreducible factor degree dividing10 and prove F irreducible. A proper rational factor of the primitive P10 would reduce to a proper factor of F because its leading coefficient is nonzero modulo11. Thus P10 is irreducible over Q.

The rational Sturm sequence has variation8 at negative infinity and2 at positive infinity, proving exactly six distinct real roots. The narrow rational intervals in the certificate each have a variation drop of one and lie within the six displayed intervals. The polynomial and all source hashes are retained in topic130. No floating root approximation is used in these conclusions.

## 2. Every resonant response is nonzero

At stream order n=5k, k>=2, changing its free sin((2k-2)theta) coefficient changes the next forbidden density coefficient, at order5(k+1), by sigma_k times that change. Topic130 derives the exact five-step linear response. For each integer2<=k<=10 it gives a nonzero rational polynomial sigma_k(b) of degree at most5. None can vanish at a degree-ten algebraic root of P10.

For k>=11 every signed frequency in the five-step response has fixed sign, so the same calculation gives one rational function

    sigma_k(b)=N(k,b)/D(k).

The degree in b is5. The greatest common divisor in Q[k] of all coefficients of N as a polynomial in b is exactly (k-1)(2k-1)^2 up to a nonzero constant. Therefore N(k,b) is not the zero polynomial in b for any integer k>=11. The denominator is nonzero there: the response uses only the nonresonant orders5k+1through5k+4 and positive transport denominators. Again, irreducibility of P10 implies sigma_k(b_i)!=0 at each root. Direct exact responses at k11and12 agree with this rational formula.

The limiting response is

    sigma_infinity(b) = [105740262233375564340 b^5
      -75391590752721913500 b^4 +36221542308471166470 b^3
      -9366918632145457140 b^2 +859183320434242405 b
      -22057171011707398]/16814963483136000000.

It is a nonzero degree-five rational polynomial, so it also does not vanish at any b_i. Exact rational-function division gives sigma_k(b_i)->sigma_infinity(b_i). For each root, all sufficiently large k therefore satisfy |sigma_k(b_i)|>=|sigma_infinity(b_i)|/2. The finitely many earlier responses are nonzero, proving

    inf_(k>=2)|sigma_k(b_i)|>0.

This is an all-order algebraic argument. A long finite sample of nonzero responses would not suffice.

## 3. Convergence and the common potential

The compatibility O10(b_i)=0 follows from the exact root definition. The uniform response bound from Section2 is precisely the remaining hypothesis of the triangular majorant in131 with Q5 and B4. That argument gives unique compatible coefficients and geometric bounds, hence convergence with every weighted density and stream derivative. The reconstruction in132 supplies the common potential on the same strict geometric radius, with its two exceptional logarithmic terms at orders5and10. Termwise differentiation and multiplication recover the original potential equation.

For epsilon!=0, homogeneity of the response gives sigma_k(epsilon f_1)=epsilon^5 sigma_k(f_1). Inductively each density, stream and tuned harmonic coefficient of order n scales by epsilon^n: a provisional obstruction at order n+5 scales by epsilon^(n+5), and division by sigma_k scales its chosen H_n by epsilon^n. A geometric coefficient base therefore scales by |epsilon|, giving the radius scaling |epsilon|^(5/2). This is the same solution family viewed on a rescaled exterior, rather than a separate convergence mechanism.

## 4. Quantitative response certificate

For any exact root interval I and rational expression sigma=N/D, one can certify |sigma_k|>=s>0 by finitely many rational inequalities. Check k below a chosen K individually. For k=K+t, t>=0, verify that D(K+t) has positive coefficients and that every coefficient of sign(sigma_infinity)N(K+t,b)-sD(K+t) is nonnegative uniformly for b in I. A positive constant coefficient gives a strict lower bound for every real t>=0. Interval Horner evaluation with exact rational endpoints supplies rigorous coefficient bounds, including for the negative root. The completed exact certificate in verification/response_bounds.json uses K=11. In increasing root order it proves the uniform lower bounds 1/32, 1/8388608, 1/65536, 1/32768, 1/16384 and1/2048. Every required coefficient lower bound is strictly positive. These numbers are conservative lower bounds; no exact response minimum is asserted.

Dependencies:130for exact recurrence and response identities,131for the general triangular majorant,132for the potential, and elementary modular irreducibility and Sturm arguments. The independently reviewed existence theorem is PROVED. The separate quantitative bounds retain their stated review status.
