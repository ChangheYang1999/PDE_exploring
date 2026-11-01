# Necessary exterior radii for tuned rational profiles

Status: PROVED and independently confirmed in V322. The analytic implication follows from the proved highest-mode theorems38,115 and118; the numerical constants are enclosed independently.

## Statement

Let delta=2h/Q lie in(0,1), with h,Q positive integers, and let a compatible tuned pure density/stream series exist as in131 or145. Suppose its leading density has highest odd frequency B-1 with nonzero coefficient alpha, where B>=2 is even. Set

    d=delta/(1-delta), eta=B-delta,
    a=2/eta, beta=2(B-1)/eta,
    R_H=4d [a Gamma(a)Gamma(beta)/Gamma(a+beta)]^(1/a).

Then uniform termwise convergence of the density with two angular derivatives on a closed exterior r>=R requires

    R > (|alpha|/R_H)^(1/delta).

For f_1=epsilon(sin(theta)+b sin(3theta)), B=4 and alpha=epsilon b. This is only a necessary condition. It neither identifies the actual radius nor improves a sufficient convergence radius.

## Proof

The induction on angular support gives degree at most Bn-1 for f_n and Bn for g_n. At a stream resonance n=kQ the free harmonic has frequency delta n-2=2hk-2, strictly less than Bn since delta<1 and B>=2. It cannot contribute to the top stream frequency.

Assume the top density coefficients at orders below n agree with those of the ordinary top-mode recurrence. In an ordered advection product of orders i and j with i+j=n, an output at frequency Bn-1 can arise only from stream frequency Bi and density frequency Bj-1. Any smaller input frequency yields a strictly smaller output, since angular differentiation preserves frequency. The top stream coefficient is the ordinary nonresonant inverse of the top density coefficient; its denominator is strictly positive. Thus the free harmonics and every lower-frequency change they later generate never alter any top coefficient. This induction treats their propagated effects as well as their direct contribution.

Theorem38 therefore gives A_n=(-1)^(n-1)alpha^n h_n for the top density coefficient. Theorem115 gives h_n R_H^n asymptotic to K n^(-1-nu), where K>0 and nu=1/beta lies strictly between1/2 and1. At the critical radius r_*=(|alpha|/R_H)^(1/delta), the top coefficient of the second angular derivative of the nth density term has magnitude asymptotic to a positive constant times n^(1-nu). It does not tend to zero. A Fourier coefficient is a bounded linear functional on continuous angular functions, so the derivative terms fail the necessary uniform term test there. At smaller radii their undifferentiated top coefficients grow exponentially. Hence any closed exterior with the stated convergence must start strictly above r_*. This is exactly the argument of118, with the top-mode independence just proved for tuned series.

## Numerical verification and scope

Evaluate the positive gamma functions and rational powers with outward-rounded intervals. Use the exact algebraic root intervals from the earlier profile certificates, not rounded root inputs. Check all quoted six-place values of R_H against their rounding bins, and check the radius comparisons for every real root. Separately compare a finite scalar top recurrence and the independently constructed Cartesian low-order coefficients. The finite scalar ratio is only an approximation to R_H and is never used to prove its exact formula.

The assumptions do not allow arbitrary extra off-lattice harmonic multipoles. Only the prescribed resonant harmonics are covered. A two-mode statement with B=4 is not asserted for arbitrary higher-bandwidth leading data; for those data the general B formula applies.

## Completed numerical audit

All23 algebraic-root bounds pass at512 bits. The quoted six-place R_H values round correctly. The largest4/9 root has necessary radius1.14443779720792726371668217..., and every other tested root has necessary radius below0.16. At scalar order1500 the relative error of the corrected ratio lies between7.26e-7 and8.88e-7. This is agreement to six significant digits, not six decimal places. Four independent Cartesian top coefficients through order5 agree. Actual total elapsed time8.946491541340947 seconds.
