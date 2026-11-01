# Convergence of the one-edge and three-edge series

Status: PROVED. The theory part independently reviewed and adopted this proof; the final transcription was checked in V207 and V208. This concerns the modified edge recurrences of topic102. It does not prove convergence of the full nonlinear stationary IPM series.

## Exact statement

Fix delta=2/3, c=3, and F_1(theta)=sin(theta). For K=1 or K=3, retain exactly the ordered pairs (i,j) with i+j=n and min(i,j)<=K in the stationary recurrence. Count every ordered pair once, including a central pair. Use the canonical polynomial Poisson inverse, with the entire constant coefficient of every resonant stream mode set to zero. Write the resulting density and stream coefficients as F_n(t,theta), G_n(t,theta), where t=log r, and put

    ||H||_3 = sum_(k>=0) k! 3^k ||[t^k]H||_(angular l1).

Then, for every n>=1,

    ||F_n||_3 <= A_K^(n-1),
    ||G_n||_3 <= 3 A_K^(n-1),

where A_1=23/10 and A_3=5/2. The density, stream, velocity and compatible potential series converge absolutely with all fixed natural weighted derivatives on r>=R for every R>A_K^(3/2). They define real analytic exterior fields satisfying the modified edge equation. In particular R=4 is sufficient for both variants.

The conclusion gives a finite sufficient radius, not an exact radius or an asymptotic coefficient rate. It does not identify the rates observed in the finite numerical experiment.

## Linear inverse estimates

The exact polynomial identities give

    ||D H||_3 <= (1/3)||H||_3,
    ||integral_0^t H(v)dv||_3 = 3||H||_3,

where D=partial_t. Every nonzero Poisson shift at delta=2/3 has magnitude at least 2/3. The finite Neumann expansion consequently gives

    ||(D+s)^(-1)|| <= 1/(|s|-1/3) <= 3.

A resonant shift uses the integral from zero, also of norm3. Each density sine coefficient enters at most two stream incidences, each with factor1/2. Deleting the entire resonant output constant contracts the norm. Thus the canonical stream map satisfies

    N_n <= 3 M_n,
    M_n=||F_n||_3, N_n=||G_n||_3.                 (1)

This is the sharp-scale Poisson estimate of topic89 at scale3. Similarly,

    ||(2(n-1)-3D)^(-1)|| <= 1/(2n-3), n>=2.       (2)

Both estimates hold on every finite polynomial space, uniformly in its degree.

Multiplication by a log-independent trigonometric polynomial H obeys

    ||H B||_3 <= ||H||_(angular l1) ||B||_3.       (3)

Indeed each log column is multiplied separately, and the angular sine/cosine coefficient norm is submultiplicative by the product-to-sum identities. This step uses that H is log-independent. It does not assert that the factorial-weighted norm is a Banach algebra for general log polynomials.

## The low profiles and their constants

For either edge recurrence the coefficients through order3 agree with the full recurrence. They are log-independent in both density and stream. Their plain coefficient norms are

    i       H_i=||F_i||             Q_i=||G_i||
    1       1                      3/20
    2       1/10                   33/4480
    3       251/44800              637/537600.

Only the first row is needed when K=1. All four higher fractions are exact consequences of the independently generated Cartesian reference in topic102. Set p_i=1-2i/3, P_i=2-2i/3, and

    B_i=(|P_i|+2i/3)Q_i + (2i-1+3|p_i|)H_i,
    C_i=(|P_i|+4i/3)Q_i + 5(2i-1)H_i.

Then

    B_1=23/10,
    B_2=929/2240,
    B_3=2537/53760.                              (4)

Moreover C_i+B_i(2i-3)>=0 for i=1,2,3. For i>=2 this follows because both summands are positive. For i=1 the difference C_1-B_1 is31/10.

## The finite-memory majorant

Take n>=4 for K=1, or n>=7 for K=3. Each retained pair has exactly one index i<=K and the other index j=n-i>K, with j>=3. The two orientations are distinct. Angular support satisfies

    maxfreq(F_j)<=2j-1, maxfreq(G_j)<=2j,

by the usual support induction, which remains valid after removing convolution pairs.

The two contributions with low index i are

    P_i G_i F_j' - G_i'(p_j+D)F_j,
    (P_j+D)G_j F_i' - G_j' p_i F_i,

where primes are angular derivatives. There are no D F_i or D G_i terms because the low profiles are log-independent. For j>=3,

    |p_j|+1/3=2j/3-2/3,
    |P_j|+1/3=2j/3-5/3.

Using (1)-(3) and the angular support bounds, the norm of their sum is at most

    { Q_i[|P_i|(2j-1)+2i(2j/3-2/3)]
      +3H_i[(2i-1)(2j/3-5/3)+2j|p_i|] } M_j
    = (2B_i j-C_i)M_j.

Apply (2), and use n=i+j and C_i+B_i(2i-3)>=0. This yields

    M_n <= sum_(i=1)^K B_i M_(n-i).              (5)

Every constant in this bound is independent of n. The argument explicitly covers all retained ordered pairs, without inserting a factor for a duplicated central pair.

## Geometric induction and finite base cases

For K=1, (5) gives M_n<=(23/10)M_(n-1) for n>=4. The exact first three coefficients satisfy M_n<=(23/10)^(n-1): M_1=1, M_2=1/10, M_3=251/44800. This proves the density bound for all n.

For K=3, (5) applies at n>=7. The exact first six density profiles are log-independent and satisfy M_n<=(5/2)^(n-1). The finite checks, including every rational norm, are retained in verification/checks.json. Finally,

    B_1/(5/2) + B_2/(5/2)^2 + B_3/(5/2)^3
       = 831077/840000 < 1.  (6)

Substituting the induction hypotheses into (5) therefore proves M_n<=(5/2)^(n-1). The stream bound in both cases follows from (1).

## Convergence, potential and the modified equation

The factorial norm controls evaluation at every finite real or complex t:

    ||H(t)||_(angular l1) <= exp(|t|/3)||H||_3.

The geometric bound, the linear angular support bound, and the strict margin A_K R^(-2/3)<1 give absolute convergence of every fixed naturally weighted density and stream derivative on r>=R. The harmless factor exp(|log r|/3) is absorbed by the strictly decreasing higher radial powers; finitely many early terms are handled directly. More explicitly, for r>=R>1 and n>=2,

    r^(-(2/3)(n-1)) exp(log(r)/3)
       <= R^(-(2n-3)/3).

Any fixed derivative costs only a polynomial in n and constants depending on its order. A small complex angular strip contributes an additional geometric factor exp(2n eta), which can be absorbed into the same strict margin. This also proves local complex convergence and real analyticity.

The joint potential reconstruction estimate of topic41 applies to this norm because ||D||_3<=1. It bounds the compatible potential coefficients by a polynomial in n times M_n+N_n, apart from finitely many early orders. Those early coefficients have been constructed explicitly. Thus the potential series and its naturally weighted derivatives converge as well. This reasoning uses the linear potential identities, not the omitted nonlinear pairs.

Let rho_<=K and u_<=K denote the finite first K density and velocity sums. Absolute convergence permits multiplication and regrouping, so the summed fields satisfy

    (c x dot grad -1)rho
       + u_<=K dot grad rho + u dot grad rho_<=K
       - u_<=K dot grad rho_<=K = 0, c=3.         (7)

At an order where both indices are at most K, the subtraction ensures that the corresponding ordered product is counted once. All other retained products are also counted once. This is the modified edge equation. The missing term involving two high-order tails generally prevents (7) from being the full stationary IPM equation.

## Dependencies and scope

Topic102 defines the exact modified recurrence and supplies independently checked low coefficients. Topic89 supplies the uniform Poisson bound, whose short proof is repeated here. Topics41 and82 supply the linear reconstruction and standard weighted convergence implications. The present new step is the finite-memory estimate (5), which works because the retained low factors have log degree zero. The proof does not apply directly to K=10 or K=30, where some retained low factors have positive log degree, or to the full nonlinear sum.
