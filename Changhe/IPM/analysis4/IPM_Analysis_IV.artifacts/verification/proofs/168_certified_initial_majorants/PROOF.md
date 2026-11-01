# Initial coefficient bounds in the rational majorant

Status: PROVED. Independent theory-part review dated2026-10-31T12:56Z closes the analytic audit; exact finite certificates are retained. See V327.

## Theorem

Assume the hypotheses of topic145: coprime integers h>=2 and Q>2h, delta=2h/Q, even bandwidth B, a nonzero finite sine leading profile with frequencies below B, vanishing first obstruction, and a lower bound s>0 for every tuning response. Let f_1,...,f_Q be its uniquely determined initial density coefficients. Choose any strictly positive rational numbers d_1,...,d_Q satisfying

    j ||f_j||_1 <= d_j,   1<=j<=Q.

Use the majorant map (5) of topic145 with

    P(z)=sum_(j=1)^Q d_j z^j,
    P_r(z)=sum_(j=r)^Q d_j z^j,

and unchanged constants L=Q/2 and kappa=B(Q-2h)(3-2h/Q)/h. Denote this polynomial map by Phi(z,Y), in the order Y=(V_1,...,V_(Q-1),E,W). Its constant-level part has the form c0+JY with J strictly lower triangular. Set T=(I-J)^(-1), Y0=T c0 and

    G(z,Y)=Y0+T(Phi(z,Y)-Phi(0,Y)).

If z0>0 and a nonnegative vector b>=Y0 satisfy G(z0,b)<=b componentwise, the unique tuned IPM series and all its appropriately weighted derivatives converge on every closed exterior

    r>=R>z0^(-Q/(2h)).

The common potential has the same sufficient radius and the finite logarithmic terms specified in145. For a leading amplitude epsilon, multiply the radius by |epsilon|^(Q/(2h)). This is a sufficient radius, not a claim of optimality.

## Proof

The free stream harmonic first occurs in g_Q. It therefore first contributes to the density at order Q+1. All density coefficients through Q are known before any harmonic is tuned. Their verified norm upper bounds can be used as the initial values of the scalar majorant directly.

For base index n>=Q, define the scalar lookahead variables and harmonic majorants by equality in (3) and (4) of145, using the chosen d_j for j<=Q. After computing these quantities, define the next scalar density bound by equality in (2), starting at order Q+1. The ordering is triangular: a lookahead density-density sum has indices at most n; the harmonic sum has harmonic index at most n-1; the remaining provisional terms have smaller lookahead index. Every coefficient on the right is nonnegative.

Induct in this triangular ordering. The initial inequalities hold by hypothesis. At a later density step, inequality (2) and previously established bounds prove domination. At a true resonance, inequalities (3) and (4), together with the response lower bound s, prove domination of the provisional coefficients and the selected free harmonic. At nonresonant base indices the artificial lookahead and harmonic variables are harmless nonnegative enlargements. This proof never requires the initial d_j to satisfy the Catalan recurrence or even its scalar inequalities. Those Catalan numbers in145 supplied convenient initial upper bounds only.

Summing the scalar equations for n>=Q and the density equation for orders at least Q+1 gives exactly the same generating map (5). The polynomial P records the independently bounded initial coefficients. No low-order density equation is imposed again. The shift identities depend on the starting indices and are unchanged when the coefficients of P change.

At z=0 each A_r=[P_r^2]_(>=Q+r)/z^(Q+r)+2z(P_r/z^r)W+z^(Q+2-r)W^2 has a constant scalar value and no W dependence. The successive V rows depend linearly only on earlier V rows; E depends linearly on the V rows; W depends linearly only on E. Thus J is strictly lower triangular and T=I+J+...+J^Q is nonnegative. All coefficients of Phi(z,Y)-Phi(0,Y) are nonnegative and have positive z degree.

Iterating the transformed map from zero produces nonnegative polynomial coefficients and remains bounded by b on the real point z0, by the supersolution inequality and monotonicity. At every fixed coefficient degree, the iteration stabilizes to the unique formal scalar solution: each nonconstant term of G carries positive z degree, so its coefficient depends only on lower degrees. The bounded monotone evaluations imply that every component's nonnegative coefficient sum at z0 is finite and at most b. Therefore each scalar coefficient is bounded by a constant times z0^(-n). The true density and stream coefficients satisfy the same geometric estimate by domination.

The angular support is at most Bn, and each fixed weighted spatial derivative introduces only a polynomial factor in n. A strict exterior radius allows a smaller positive angular strip and sums every such derivative absolutely and uniformly. The potential reconstruction of145 preserves the geometric base. This proves the statement.

## Certificate construction

Recompute f_1,...,f_Q with the signed Cartesian recurrence at the exact algebraic leading root. Evaluate each j||f_j||_1 by interval arithmetic and round its upper endpoint upward to a rational d_j. Record those endpoints and the selected rational bounds. The interval root and the full finite calculations are inputs to the certificate, not substituted decimal approximations.

Construct Phi with these initial values and check its constant affine part, strict triangularity, and coefficient identity against the independently indexed scalar recurrence. Finally retain exact rational values for Y0, the box, its image, and the failed adjacent dyadic box when searching within the family b=2Y0. Failure of that neighboring box does not imply a sharp convergence boundary.

The response lower bounds remain those already proved in the corresponding profile certificates. Smaller initial bounds cannot replace a missing response certificate. Finite coefficient decay alone does not enter the convergence argument.

## Initial certificates completed

The five two-mode roots pass with the already proved response bounds from150. Their smallest passing dyadic exponents in the box family 2Y0 are 125,120,134,122,127, giving sufficient radius exponents 1125/4,270,603/2,549/2,1143/4. The exact boxes also fail at the preceding dyadic exponent. The full five-root calculation took 1.2171497070230544 seconds.

For the nearest Candidate-shaped root3, the established response bound s=2^-28 gives q=150, radius 2^(675/2) for the normalized profile, and radius 2^348 after restoring Candidate007's original first amplitude. Its maximum component ratio is below0.893. The calculation took0.5951963230036199 seconds. These improved radii await review of the initial-bound extension above; all exact box computations and low-order norm enclosures pass.

An initial output attempt failed because a tuple of exact rational endpoints was not converted by the JSON helper. The arithmetic had completed; the serializer was repaired and the calculations rerun. The failed output and scheduling record are retained.

## A smaller bilinear constant after the initial block

The same certificate is valid with the smaller common constant

    kappa_* = B [2-delta+max(delta,1-delta)]
                * (1-delta)/delta * (Q+1)/Q.

Indeed |p_j|/j=|1/j-delta|<=max(delta,1-delta), while |P_i|/i=|2/i-delta|<=2-delta for i,j>=1. The Fourier support bounds therefore give

    ||T(g_i,f_j)||_1
      <= B [2-delta+max(delta,1-delta)] i j ||g_i||_1 ||f_j||_1.

Every density or provisional-density equation actually estimated after the initial block has total order m>=Q+1. For such m,

    m/lambda_m = (1-delta)/delta * m/(m-1)
                 <= (1-delta)/delta * (Q+1)/Q.

This proves the claimed common factor. In the harmonic estimate, eta_n=n|H_n| is bounded by n/(n+Q) times the corresponding next-obstruction norm estimate, so dropping that factor only enlarges the bound. No equation at orders2 through Q uses kappa_*, because those coefficients are enclosed independently. All coefficients of the new generating map remain nonnegative and the preceding domination and box proof applies unchanged.

For delta=4/9 and B=4 this gives kappa_*=950/81, in place of230/9. For B=20 it gives4750/81, in place of1150/9. This refinement also awaits independent review.

## Reduced-constant certificates

With the same old proved response lower bounds and the reduced constant, the five two-mode profiles give q=113,108,122,110,115. Candidate-shaped roots2 and3 give q=132,138, hence normalized sufficient radius exponents297 and621/2 and conservative restored-amplitude exponents307 and321. Every selected box passes strictly and the preceding dyadic box fails. The five-root batch took1.3260554750449955 seconds; the two Candidate-shaped roots took1.2883725478313863 seconds. These exact finite checks are confirmed; the improved all-order radii await review of the two extensions proved above.

The script defaults to the old, already proved response bounds. Its --response sharp option explicitly selects the separately computed164 inputs; it never switches those inputs merely because another run has created a file. The --improved-kappa option selects the reduced constant and writes distinct output names.

## Certificates with the sharper Poisson norm

With both the reduced nonlinear constant and L9=243/104 from169, the five two-mode profiles give q104,100,113,101,107. Candidate-shaped roots2,3,4 give q124,129,126. The two earliest restored sufficient exponents are289 and300; root4 gives293. Every exact box and coefficient identity passes. These improvements await independent review of168 and169. The resonance-period projection171 subsequently produces smaller boxes under an additional reviewed construction once that review is complete.

## Review closure

The theory part independently checked the complete argument at12:56Z and reproduced the dyadic certificates using a separate Fourier implementation. Earlier pending-review statements above record their original status; V327 closes that review for this topic. The separate resonance-period and longer-prefix extensions require their own reviews.
