# Finite diagnostics through order390 of the reset continuation

Status: finite arithmetic confirmed in V487 and V488, conditional on the order329 midpoint restart. No infinite tail conclusion is admitted.

## Exact scope and definitions

The input is the numerical experiments's512-bit interval continuation of the canonical delta=2/3 logarithmic recurrence. At order329 its inherited radii were discarded. Thus all interval conclusions here are conditional on that fixed midpoint seed, and do not propagate the original exact seed uncertainty. Define M_n and N_n to be the sums of absolute Fourier coefficients over every logarithmic column of density and stream respectively. A coefficient array consists of polynomial columns in t=log r and sine frequency indices, in the conventions of01.

The audit recomputes M_n,N_n, their nth roots and27-order least-squares log10 slopes from the stored coefficient balls. It checks the ten published rows381..390 and the Poisson identities at388..390. These are finite arithmetic statements, not asymptotic conclusions.

## Norm and Poisson checks

Each coefficient is enclosed by its stored midpoint and radius. Directed absolute values and addition therefore enclose the complete finite l1 norms. Positive lower bounds permit directed logarithms and roots. For each n and P=2-2n/3 the stream identity is checked coefficientwise:

    (4j^2-P^2)g_(q,j)-2P(q+1)g_(q+1,j)-(q+1)(q+2)g_(q+2,j)
    = ((P-2j)f_(q,j-1)+(q+1)f_(q+1,j-1)
       +(P+2j)f_(q,j)+(q+1)f_(q+1,j))/2.

Missing indices are zero. This identity follows from the already derived Poisson equation. Residual intervals must contain zero, and the canonical resonant t^0 stream coefficient must be exactly zero. A containing residual verifies consistency of finite enclosures and is not alone a uniqueness proof; the recurrence and seed convention supply that interpretation.

## Shifted multipliers and finite fits

Let x be the full coefficient vector at n-3 and y the vector at n, shifting x up one Fourier index while leaving logarithmic columns fixed. The least-squares multiplier is a_n=<x,y>/<x,x>; its relative residual satisfies e_n^2=1-<x,y>^2/(<x,x><y,y>). Directed sums enclose both. Nonzero denominators and nonnegative squared residuals are checked. The identity ||y||_2/||x||_2=|a_n|/sqrt(1-e_n^2) is checked separately.

The audit fits log10|a_n| to an affine function of log10 n,1/n,or n on each stated finite window. Ordinary least-squares formulas with interval arithmetic enclose the fitted coefficients and RMS residuals. The fitted functions may be numerically close over the window even when they predict different tails. No fitted model is asserted to persist beyond the checked orders. An observed positive finite drift does not prove eventual growth, divergence, or convergence of the IPM series.

Dependencies:01,154,207,215,221. Evidence files are created only by completed checks. The loaded checkpoint hash and its maximum order are recorded without copying the large checkpoint.
