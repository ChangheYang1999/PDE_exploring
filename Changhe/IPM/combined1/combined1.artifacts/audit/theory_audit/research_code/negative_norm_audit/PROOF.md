# Independent audit of the exact radial negative-norm formula

## 1. Statement, notation and scope

This note independently proves the formula in the frozen source/n4_proof.md. It concerns the actual homogeneous Hdot^-1 norm on R2, with Fourier transform fhat(xi)=integral f(X) exp(-i X.xi) dX and spatial Lebesgue measure. It does not certify a numerical candidate norm.

Let F be a finite real S1 sum

    F(r,theta)=sum_(n positive odd) f_n(r) sin(n theta),
    f_n(r)=r sum_i t^m u^(b_i) Q_i(u),
    m=(n-1)/2, t=r²/(1+r²), u=1/(1+r²),

where Q_i are real polynomials and every b_i>3/2. The coefficients and b_i may be rational for an exact rational answer, but rationality is not needed for the analytic identity. Define

    A_i(u)=(1-u)^n Q_i(u),
    D_i(u)=sum_l [u^l]Q_i(u) u^l/(b_i+m-1+l).

Then F belongs to Hdot^-1 and

    ||F||_Hdot^-1²/pi
       =sum_n (1/(4n)) sum_(i,j) sum_k
                    [u^k](A_i D_j)/(b_i+b_j-3+k).          (1)

Every displayed denominator is positive. Signed polynomial coefficients and cross terms are retained. In particular the right side is rational for rational input. The hypotheses are sufficient; this note does not classify data that fail them.

## 2. Membership and the Green solution

At the origin each f_n=O(r^n), because r t^m=r^n(1+r²)^(-m). At infinity every summand is O(r^(1-2b_i)), with exponent strictly below-2. Thus ||rF||_2 is finite. Angular Poincare on the centrally odd test space gives

    ||F||_Hdot^-1 <= ||rF||_2.

Indeed |integral F phi|<=||rF||_2 ||phi/r||_2, while integral |phi/r|²<=integral |grad phi|² because all contributing angular frequencies have absolute value at least1. Projecting arbitrary tests onto the S1 subspace does not increase their gradient norm.

For each n, the regular decaying radial Green solution is

    phi_n(r)=[r^(-n) I_n(r)+r^n J_n(r)]/(2n),
    I_n(r)=integral_0^r s^(n+1) f_n(s) ds,
    J_n(r)=integral_r^infinity s^(1-n) f_n(s) ds.             (2)

Differentiation verifies -(phi_n''+phi_n'/r-n² phi_n/r²)=f_n. At zero the solution and its derivative have the regular r^n behavior; possible higher-order terms do not affect finite energy. At infinity it is a sum of decaying powers and possible r^(-n) log r terms, all with square-integrable gradient. Integration by parts on annuli has vanishing boundary terms, so

    integral f_n phi_n r dr
        =integral (|phi_n'|²+n²|phi_n/r|²) r dr.

The full Green function therefore represents the unique Hdot^1 solution modulo constants, and Fourier or duality characterization identifies its gradient energy with ||F||_Hdot^-1². Full-circle sine orthogonality supplies the factor pi.

## 3. A direct outer-integral derivation

The two terms in (2) contribute equally after interchanging the two radial variables. The changes of order are valid term by term in absolute value: near zero f_i=O(r^n); near infinity f_i=O(r^(1-2b_i)); and every b_i+b_j>3. Consequently

    ||F||_Hdot^-1²/pi
        =sum_n (1/n) sum_(i,j) integral_0^infinity
                    r^(n+1) f_i(r) J_j(r) dr.             (3)

Unlike an inner antiderivative, the outer antiderivative never passes through a zero exponent. Direct substitution u=1/(1+r²) gives

    s^(1-n) f_j(s) ds=-(1/2)u^(b_j+m-2) Q_j(u) du,
    J_j(r)=(1/2)u^(b_j+m-1) D_j(u).                       (4)

The other radial factor is

    r^(n+1) f_i(r) dr
       =-(1/2)(1-u)^n u^(b_i-m-3) Q_i(u) du.              (5)

Insert (4)-(5) into (3). The nth radial contribution becomes

    (1/(4n)) sum_(i,j) integral_0^1
                u^(b_i+b_j-4) A_i(u) D_j(u) du.

Integrating each polynomial coefficient yields (1). Positivity of b_j+m-1+l and b_i+b_j-3+k justifies every individual elementary integral. This derivation avoids the intermediate logarithmic case entirely, while giving the same expression as N4.

## 4. Audit of the frozen implementation

The copied n4_negative.py first divides P(t) by t^m exactly, substitutes t=1-u, extracts its exact leading u power and adds that order to the radial exponent b. It forms A_i as (1-u)^n Q_i, D_j with the denominators in (4), groups all products by b_i+b_j, integrates by the denominators in (1), and multiplies by pi only at the final Arb square root. Its summation includes all ordered pairs i,j, so no additional cross-term factor2 belongs in (1). The final factor1/(4n) is correct.

This is an independent analytic and code-inspection audit, not an independent execution of the candidate calculations. The manufactured checks and signed cross-checks in N4's verification directory support its implementation, but no numeric verdict is inferred from them here.

One interface limitation should remain explicit. The routine returns status INFINITE when a term fails b>3/2. Such a conclusion requires the separate nonresonance/grouping hypothesis: terms with the same effective radial exponent could cancel across the supplied representation. For the case4 branch lists, N4's sector audit supplies this check. The generic mathematical theorem above makes no infinity claim for arbitrary ungrouped input. A generic caller must either group all resonant branches exactly or label failure of the sufficient representation as undecided.

## Dependencies

The norm duality, angular Poincare inequality, elementary radial ODE, exact variable substitution and polynomial integration are all used with their hypotheses stated above. No matrix positivity, approximate-solution smallness, linear inverse or existence theorem is supplied by this result.
