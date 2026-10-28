# Directed evaluation of the sharper finite-part bounds

## Statement and prerequisites

Use the homogeneous scalar Holder spaces, circular principal-value kernels, quotient extension and exact bounds in ../PROOF.md. This evaluation is conditional on that analytic proof receiving its independent acceptance. Every accepted number is an upper bound, not an assertion of optimality of the radius or of the operator norm.

Fix epsilon=1/100. For the uniform C envelope choose rho_C=34891/100000; for the uniform D envelope choose rho_D=15993/50000. Insert these exact rational radii into the K_C,K_D formulas of ../../linear_envelope/PROOF.md, replacing B_C,B_D by B_C^*,B_D^* as proved in ../PROOF.md. Then the resulting constants bound the coefficients of alpha throughout 0<alpha<=1/100. In particular the intended simplified inequalities are

    C_alpha <= 2/(pi alpha)+C0+2.4945 alpha,
    D_alpha <= 2/(pi alpha)+2C0+2.7442 alpha,
    C0=1/2+(log(2)-1)/pi.

These decimal simplifications are not accepted until the code verifies the adverse endpoints. The rational choices came from a floating-point scan; the proof uses only their admissibility and exact substitution, and makes no claim of global minimization.

For finite exponents evaluate the same sharper J_C,J_D formulas at the following fixed rational radii, with rho written in units of 1/100000:

    alpha       C radius numerator      D radius numerator
    1/1000          34880                   31975
    1/200           34868                   31961
    1/100           34853                   31944

Each resulting adverse upper endpoint is valid independently, whether or not it improves the current best table value.

## Exact Catalan enclosure and numerical method

The complete proof in ../catalan_evaluation/PROOF.md supplies S_512<G<S_512+2^(-512), using exact rational recurrences. Evaluate this rational interval directly in 384-bit ball arithmetic. Independently compute G with the special-function constant at 768 bits and check that its ball lies inside the exact rational interval. The latter check corroborates the implementation; the proof of the Catalan enclosure is elementary and does not depend on a special-function approximation.

Evaluate each displayed algebraic, exponential, logarithmic and gamma-ratio expression with outward ball arithmetic. Extract binary endpoints as exact rationals, never by decimal conversion of a printed approximate ball. Round the upper rational endpoint upward to ten decimal places. At 768 bits recompute with a different grouping of the positive terms and verify that the new ball lies inside the saved 384-bit interval and below its printed upper endpoint. Exact rational arithmetic verifies each final upward rounding.

Use the accepted parent formula

    A(alpha)=Gamma(1+alpha/2)/(2 sqrt(pi) Gamma(3/2+alpha/2)),
    a2(alpha)=2^(1+alpha/2)/(pi(2+alpha)).

All these functions are positive at the chosen arguments, and all radii satisfy 0<rho<1/2. The cost L is the maximum of two explicit real quantities; enclose it by the ball maximum, or establish the winning branch by disjoint endpoint comparison. No floating-point optimization certificate is required.

## Optional combination with retained reflection

After independent acceptance of the exact radial-minorant theorem in ../../../local_projection/strict_increment/larger_disks/exact_radial_density/PROOF.md, define at a chosen radius rho

    M2=J_*rho^2-rho^4/[512(1-rho)^2],
    M4=K_*rho^4-rho^6/[49152(1-rho)^2].

Both are positive. The same retained edges are present in the sharper-deficiency proof. Thus one may subtract alpha(1-alpha)M2+alpha(1-alpha)(2-alpha)(3-alpha)M4 from the finite D bounds. For 0<alpha<=epsilon the saving divided by alpha is at least

    (1-epsilon)M2+(1-epsilon)(2-epsilon)(3-epsilon)M4.

Subtracting a directed lower bound for this expression from the directed upper bound for K_D therefore yields another uniform linear envelope. This optional calculation must have its own accepted analytic manifest. The previous uncombined bounds remain independently valid. No saving is subtracted twice.

## Evidence

The executable is code/certify_sharp_deficiency.py at the artifacts root. The final JSON records exact chosen radii, both precisions, rational Catalan endpoints, input/proof/program hashes, the analytic acceptance identifiers and every safe decimal. No new singular-integral quadrature occurs in this evaluation.
