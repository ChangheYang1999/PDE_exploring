# Conditional quadratic logarithmic growth from shifted multipliers

Status: PROVED as a conditional theorem in V500 after independent review. Its all-order hypotheses remain OPEN for the computed IPM sequence.

## Statement and notation

Let H be a real Hilbert space, S a linear isometry and Q a positive integer. For nonzero vectors x_n in H, define for n>Q

    a_n=<S x_(n-Q),x_n>/||x_(n-Q)||^2,
    e_n=||x_n-a_n S x_(n-Q)||/||x_n||.

Fix one residue class modulo Q. Suppose eventually a_n!=0, e_n<=E<1 and

    log10|a_n|/n -> beta

along this class, where beta is real. Then, along this class,

    log10||x_n||/n^2 -> beta/(2Q).                    (1)

For the lower implication only, if liminf log10|a_n|/n>=beta>0, then liminf log10||x_n||/n^2>=beta/(2Q), with no uniform residual bound required. Consequently the H-valued series sum x_n z^n has radius zero if this lower hypothesis holds on even one residue class.

## Proof

Orthogonality of the projection residual and the isometry give

    ||x_n||/||x_(n-Q)||=|a_n|/sqrt(1-e_n^2).

Under e_n<=E<1, the logarithm of the last factor belongs to the fixed interval [0,-log10(1-E^2)/2]. Thus

    log10||x_n||-log10||x_(n-Q)||=beta n+o(n)+O(1).

Write n=n0+kQ and telescope from a fixed sufficiently large n0. The exact sum of the visited indices is

    sum_(j=1)^k (n0+jQ)=(n^2-n0^2)/(2Q)+(n-n0)/2.

The sum of the o(n0+jQ) terms is o(n^2): for each positive eta, all but finitely many terms have absolute value at most eta(n0+jQ), and the finite remainder divided by n^2 vanishes. The bounded residual corrections have total O(n). Dividing by n^2 proves (1).

Without the residual bound, Cauchy-Schwarz or the same projection identity gives ||x_n||>=|a_n| ||x_(n-Q)||. For every eta in (0,beta), the stated liminf hypothesis implies log10|a_n|>=(beta-eta)n eventually on the chosen class. Telescope this lower inequality, divide by n^2, then let eta decrease to zero. The resulting positive lower quadratic rate forces limsup ||x_n||^(1/n)=infinity and therefore zero power-series radius.

## Exact finite linear model

If, as a separate model identity on a residue class, log10|a_n|=alpha+beta n and e_n=E is constant, put d=-log10(1-E^2)/2. Exact telescoping gives

    log10||x_n|| = beta n^2/(2Q) + ((alpha+d)/Q+beta/2)n + C.

For beta>0 its continuous interpolation has its minimum at n=-(alpha+d)/beta-Q/2. This location is a property of the assumed exact model. A least-squares fit over finitely many indices does not establish that identity, the asymptotic hypothesis of (1), or the predicted minimum for the actual sequence.

## Application and scope

For the canonical logarithmic IPM coefficients, use the zero-padded l2 array of logarithmic and angular coefficients, with S the one-mode shift and Q=3. This is the isometry from215. There are only polynomially many coefficient positions, so l1 and l2 logarithmic norms differ by O(log n), which does not change (1).

If the positive lower tail hypothesis is established for the canonical recursion with a nonzero finite real odd-sine leading profile and rational delta in (0,1), the density norms have no exponential bound. The previously proved coefficient-to-physical dichotomies98,99,94 then give unbounded individual terms almost everywhere and on a dense residual set in the punctured plane. This physical conclusion needs those canonical-recursion hypotheses. The present finite order390 fit establishes none of these all-order assertions.

Dependencies:215 for the projection interpretation;98,99,94 only for the final physical-series implication.
