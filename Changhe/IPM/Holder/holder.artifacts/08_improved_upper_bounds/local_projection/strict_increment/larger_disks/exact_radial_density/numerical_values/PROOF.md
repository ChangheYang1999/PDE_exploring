# Directed scalar endpoints with the exact radial minorant

## Statement and hypotheses

Use the operator convention, homogeneous real or complex scalar Holder seminorm, and exponents0<alpha<1 of ../PROOF.md. The operator is R_1^2=T_xx-I/2 and D_alpha is its sharp seminorm. Numerical acceptance is conditional on independent confirmation of that exact-radial-density theorem and the earlier V195 reflection lemmas.

Foralpha=1/1000,1/100 use the exact rational J_D upper endpoints and rational cutoffs s=rho in the accepted V118 certificate. Foralpha=1/20,1/10 use the accepted exterior-circle D upper endpoints and s=1/2. For the other six table exponents use an explicitly named accepted cross-disk recombination certificate and s=1/2. Denote these unchanged original upper endpoints by U_alpha. They contain the full original translation cost1/2. A bound from which a strict gain has already been subtracted is never used as an original base.

Define p=alpha(1-alpha),q=p(2-alpha)(3-alpha) and

    J_*=-31/32+(27/8)log(4/3),
    K_*=-233/1024+(405/512)log(4/3).

In the two cutoff rows put c2=s^4/[512(1-s)^2],c4=s^6/[49152(1-s)^2]; in all other rows put c2=c4=0. The exact radial theorem proves

    D_alpha <= U_alpha-p(J_*s^2-c2)-q(K_*s^4-c4).

All gains are positive. The cutoff density is the retained w_*-H and the other rows use the full radial submeasure. Both are coupled by reflection with identical marginals. The scalar calculation subtracts the gain exactly once, after the remaining terms and phase interpolation have been bounded.

## Verification procedure

The program code/certify_exact_radial_gain.py checks the exact-radial analytic acceptance, V195, V118, the named cross recombination, the circle certificate and every registered transitive source hash. It computes the B3 and B5 coefficients by exact rational binomial sums and verifies the displayed J_* and K_* coefficients.

A256-term exact rational atanh series at1/7, with positive remainder2(1/7)^513/[513(1-1/49)], encloses log(4/3). Its propagated J_*,K_* and gain intervals must lie inside independently computed384-bit balls. A768-bit calculation uses log4-log3 and the direct B3,B5 sums, and must lie inside the first balls. The new moments are also checked to exceed the earlier J,K using disjoint ball endpoints.

Subtract the certified lower endpoint of each total positive gain from the exact original base. Round upward at ten decimal places and verify the rounding by exact rational inequalities. Save both the quadratic-only and the stronger quadratic-plus-quartic endpoints, together with source hashes, all gain intervals and real execution time. No quadrature or optimization is hidden in this scalar computation.

## Scope

Only the ten displayed endpoints are certified by this file after every stated check passes. The analytic theorem covers all exponents and admissible radii. Earlier accepted endpoints remain valid. No new value is accepted while the analytic cross-read is pending.
