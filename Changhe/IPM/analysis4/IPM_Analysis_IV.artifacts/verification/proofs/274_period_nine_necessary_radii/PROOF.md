# Necessary exterior radii for the ten period-nine branches

Status: protocol and proof written before the directed calculation. Numerical admission is recorded separately.

## Statement and notation

Let delta=2/9, c=9/7, and let b_i be one of the ten real roots of the exact compatibility polynomial P_18 in267. For real epsilon nonzero, let the uniquely tuned stationary density series have leading term f_1(theta)=epsilon[sin(theta)+b_i sin(3theta)]. Set

    a=9/17, beta=27/17, d=2/7,
    R_H=(8/7)[a Gamma(a) Gamma(beta)/Gamma(a+beta)]^(1/a).

If this density series and its second angular derivative converge uniformly term by term with their natural radial weight on the closed exterior r>=R, then

    R > (|b_i|/R_H)^(9/2) |epsilon|^(9/2).

This is a necessary condition only. The sufficient radii and existence assertions are proved separately in267. No equality with the true convergence threshold is asserted.

## Highest Fourier sector

Write A_n for the density coefficient at sin((4n-1)theta). The bandwidth is4n-1. Only the two highest contributing frequencies reach this sector in the quadratic recursion. The free stream harmonic at a resonant order n has frequency(2/9)n-2, below4n; its propagated lower frequencies cannot change A_n. The top stream coefficient is -A_n/[2((4-delta)n+2)]. Substitution in the exact stationary bracket, as in38 and259, gives

    A_n=(-1)^(n-1)(epsilon b_i)^n h_n, h_1=1,
    4d(n-1)h_n = sum_(j=1)^(n-1)
       [8(n-j)/((4-delta)j+2)-1] h_j h_(n-j).

The positive scalar solution and its singularity asymptotic are proved in115 and117:

    h_n>0,  h_n R_H^n ~ K n^(-1-1/beta),  K>0.

Here 4-delta=34/9, so the scalar parameters 2/(4-delta) and6/(4-delta) are exactly9/17 and27/17. This establishes the displayed beta-function formula without using finite fits.

## Boundary exclusion

Every b_i is nonzero because P_18 is irreducible of degree18 and P_18(0) is nonzero. At r=(|epsilon b_i|/R_H)^(9/2), the highest Fourier coefficient of the second angular derivative of the nth weighted density term has magnitude proportional to

    (4n-1)^2 h_n R_H^n ~ 16K n^(10/27).

It does not tend to zero. Fourier coefficient extraction is bounded in the uniform angular norm, so the individual terms cannot tend uniformly to zero there. At a smaller radius the same expression also has an exponentially increasing factor. Uniform convergence of the derivative series is therefore impossible at or below the threshold, proving the strict necessary inequality for both signs of epsilon and b_i.

## Verification and dependencies

Compare all18 exact scalar coefficients with the top monomials of the separately computed Cartesian polynomial prefix in267. Evaluate R_H and all ten root-dependent thresholds independently at512 and1024 bits, refining the exact root intervals on each pass. Check each published rounded-down constant against a directed enclosure. Recompute the four finite scaled coefficients at orders100,400,800,1500 in interval arithmetic to audit the theory part's scalar-recursion diagnostic; these numbers do not enter the proof of the asymptotic.

Dependencies:01 and38 for the exact recurrence and bandwidth;115 and117 for the scalar solution and asymptotic;259 for the general necessary-radius argument;267 for the exact roots and convergent tuned branches. Source snapshots, hashes and actual run times are retained alongside the verification output.
