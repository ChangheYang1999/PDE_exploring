# Finite parameter fits do not imply a smooth asymptotic growth constant

Status: PROVED in V592, admitted 2026-10-31T21:47:12+00:00, within the exact scope below.

## Statement

Fix a nonzero finite real odd sine polynomial f_1 whose sin(theta) coefficient is nonzero. For irrational delta in (0,1), let f_n(delta) be its canonical nonresonant recursion coefficients and define

    A(delta) = limsup_(n -> infinity) ||f_n(delta)||_1^(1/n),

with values in [0,infinity]. The norm is the angular Wiener norm. Every open parameter interval contains a dense set where A(delta)=infinity. At every Brjuno point delta_0 (meaning delta_0/2 is Brjuno), A(delta_0) is finite but A is discontinuous at delta_0 in the relative topology of the irrational parameters. In particular, A is not locally bounded at any parameter, and it is not a smooth function on the nonresonant parameter set. The same conclusions hold after the change of variable c=1/(1-delta).

## Proof

Theorem A gives a finite geometric coefficient bound at every Brjuno point, hence A(delta_0)<infinity. Theorems P', C* give a dense G_delta set of irrational parameters where the density power series has radius zero. The Banach-valued Cauchy-Hadamard formula identifies its inverse radius with A, so A=infinity there. For any Brjuno delta_0, choose one such divergent point within distance 1/j for each positive integer j, also remaining in (0,1). Along this sequence A=infinity while A(delta_0) is finite. This contradicts continuity at delta_0. Density also rules out any finite local upper bound. The parameter change to c is a homeomorphism, so preserves these conclusions.

The coefficient power series may be written with exponent n-1 rather than n; this does not change the Cauchy-Hadamard inverse radius. No zero-radius conclusion is drawn from finite-order data here; it is an input of the already admitted divergence theorem.

## What finite calculations establish

At any fixed finite order, each coefficient is rational in delta, with only finitely many possible poles in a compact parameter interval. Thus finite coefficients, and finite fitted statistics where their formulas are defined, can vary continuously across a sampled interval that avoids those poles. That observation does not control the limsup over all orders. A report should say that the finite fitted growth estimates vary modestly over the tested parameters; it should not say that the actual growth constant varies smoothly over all nonresonant parameters.

## Dependencies and scope

Use the admitted Brjuno theorem and the admitted prime-obstruction/divergence theorem for finite real profiles with a first harmonic (including topic42). This argument gives no discontinuity classification at the points where A=infinity, no sharp growth constant at a Brjuno point, and no uniform estimate on a restricted Brjuno sublevel set. It is compatible with the established continuity and uniform bounds on those restricted sets.

## Completed verification

A(delta)=limsup ||f_n(delta)||_1^(1/n) is finite at every Brjuno delta/2 and infinite on a dense G_delta set of irrational delta. Therefore it is discontinuous at every Brjuno point and nowhere locally bounded on the full irrational parameter set. The same holds in c=1/(1-delta). Fixed finite coefficients and finite fitted statistics can still vary continuously away from their finitely many poles.

The universal smoothness interpretation is REFUTED; the stated discontinuity consequence is PROVED. The report must attribute its observed mild parameter dependence to finite fitted estimates only. No discontinuity classification at infinite-valued points or on a restricted Brjuno sublevel set follows.
