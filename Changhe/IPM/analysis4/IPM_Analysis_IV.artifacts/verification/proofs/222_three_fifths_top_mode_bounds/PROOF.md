# Necessary exterior radii at delta=3/5

Status: PROVED, using the analytic implication already admitted in170 and the directed checks admitted inV460.

## Statement and hypotheses

Let delta=3/5 and let b be one of the four real algebraic roots isolated in200. Consider the tuned pure series with leading density epsilon(sin(theta)+b sin(3theta)), epsilon nonzero. Define

    a=10/17, beta=30/17,
    R_H=6 [a Gamma(a) Gamma(beta)/Gamma(a+beta)]^(1/a),
    R_*(b,epsilon)=(|epsilon b|/R_H)^(5/3).

Uniform termwise convergence with two angular derivatives on a closed exterior r>=R requires R>R_*(b,epsilon). This is a necessary condition only. The exact expression, not an arbitrary rounded decimal, is the lower bound.

## Proof

The density frequency at order n is at most4n-1. A free resonant harmonic at order10k has frequency6k-2<40k. Under later products with the other density or stream factors it remains strictly below the highest possible output frequency. Induction therefore shows that tuning never changes the coefficient A_n of sin((4n-1)theta).

With d=c-1=3/2 and eta=4-delta=17/5, the independent top-mode recurrence in38 gives A_n=(-1)^(n-1)(epsilon b)^n h_n, where

    h_1=1,
    4d(n-1)h_n=sum_(i+j=n) [8j/(eta i+2)-1]h_i h_j.

Its generating function has radius R_H, by the incomplete beta inverse proved in38. Topic115 gives h_n R_H^n asymptotic to K n^(-1-nu), with K>0 and nu=1/beta=17/30. At r=R_* the highest Fourier coefficient of the second angular derivative of an individual density term is consequently asymptotic in magnitude to a positive constant times n^(1-nu). It does not tend to zero. A Fourier coefficient is a continuous linear functional on continuous angular functions, so the uniform term test fails. At smaller r even the undifferentiated top coefficient grows exponentially. This proves the strict necessary inequality.

## Arithmetic verification

Refine the exact root intervals from200 by rational bisection, evaluate Gamma and the positive fractional powers with directed balls, and retain dyadic enclosures. Every decimal called a rigorous lower bound must be checked below the exact R_*. Separately compare the scalar recurrence with independent Cartesian coefficients through order8 at delta3/5 and an arbitrary exact two-mode coefficient7/10; this is before the first resonance. A scalar ratio at order1500 is a finite consistency check only and does not enter the proof.

## Dependencies and scope

Topics38,115,118 and170 provide the top-mode formula, asymptotics and endpoint term test. Topic200 provides the four algebraic roots. No sharp exterior radius, whole-plane solution or asymptotic estimate of the full coefficient norm is claimed.

## Completed constants

The directed value is R_H=3.1373310960254773096.... The four exact lower-radius expressions have values0.0016010081459...,0.0037185174863...,0.0259225531482...,0.0624634373744.... Certified downward decimal bounds are respectively0.001601008,0.003718517,0.025922553,0.062463437. The scalar recurrence through1500 and seven Cartesian top-coefficient checks pass. The decimal0.026 exceeds the third expression and is only a rounded approximation, not a certified lower bound.
