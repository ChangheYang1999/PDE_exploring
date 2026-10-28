# Uniform exclusion for the adjustable logarithmic theorem

The adjustable derivative hierarchy and logarithmic parameter do not remove the certified local obstruction around the three references. This result requires no reference matrix or derivative inequalities.

## 1. Exact statement

Fix R=2^31, 0<tau<=2^-20, 1/2<beta<=1 and Astar>=2048. Use the canonical full-plane velocity, S1 parity, distributional realization and compact smooth core completions of topics83 and89. Set

    Q=(1+tau log(1-Delta))^beta,
    omega1=(1+r^2)^(-1/10), omega2=(1+4r^2)^(2/5),
    w=(1+r^2/R^2)^(-11/10), L(h)=||wh||_(Hdot^-1),
    Mstar(h)^2=||omega2 D^2Qh||_2^2
                +Astar^2||omega1 DQh||_2^2+Astar^2 2^31 L(h)^2.

Let rho be one of the exact references state131, nb_Mpen2_exact or nb_d2_exact identified and reconstructed in topics51,52 and73. Set F=(cX+U[rho]).D rho-rho with their common exact exponent c=4076476460239181/2251799813685248.

**Theorem.** For any prospective real exponent c', there is no h in the following closed Mstar balls for which rho+h is an exact canonical stationary profile in distributions:

| Reference | Excluded radius |
|---|---:|
| state131 | 2^21 tau^beta |
| nb_Mpen2_exact | 2^-15 tau^beta |
| nb_d2_exact | 2^-15 tau^beta |

These are exclusions in the infinite dimensional completed space. They apply to corrections outside the finite generator families. They do not rule out larger corrections or other far-field classes.

The extended residual norms obey

    Mstar(F_131) > (Astar/2048) 35350195123413029343106947,
    Mstar(F_Mpen2) > (Astar/2048) 1935892108,
    Mstar(F_d2) > (Astar/2048) 1936535207.                       (1)

For epsilon=2beta-1, the radius r0=2^-20 tau^beta sqrt(epsilon) and residual threshold eta=r0/32 in89 therefore satisfy:

* The original's excluded radius is at least 2^41 r0. Each refit's is at least 32 r0.
* The residual-to-threshold ratio exceeds (Astar/2048)2^119 for the original and (Astar/2048)2^65 for either refit.

These claims hold for every admissible parameter choice in89, even if Astar is enlarged or tau is reduced to absorb very large higher derivative bounds.

## 2. Uniform norm conversion and local exclusion

Let M denote the same native norm with Astar=2048, N_tau=E(Qh), and N_beta=E((1+log(1-Delta))^beta h). Topics77 and83 prove, on the common completed distributions,

    M(h)<=Mstar(h),
    N_tau(h)<=D_tau M(h),
    D_tau=1+77*2^(17/2) R^(6/5) tau,
    N_beta(h)<(2 tau^(-beta)+16)N_tau(h)                       (2)

for nonzero h. No factor 29/7 belongs on the last inequality. For zero h use the non-strict form. Since R^(6/5)=2^(186/5)<2^38 and 2^(17/2)<2^9,

    D_tau<1+77*2^27<2^34.

Since tau^beta<=tau^(1/2)<=2^-10, one has 2+16tau^beta<3. Consequently

    N_beta(h)<2^36 tau^(-beta)Mstar(h).                         (3)

The equivalence preserves the canonical velocity and distributional meaning. Topic73 excludes closed N_beta balls of radii 2^57 for the original and 2^21 for the refits, uniformly in 0<=beta<=1. Equation(3) maps the balls in the statement into those excluded balls. The argument of73 also forces c'=c by the unchanged nonzero leading homogeneous density; no normalization or reference-energy hypothesis is needed. This proves the first assertion.

Dividing the stated radii by r0 gives 2^41/sqrt(epsilon) and 2^5/sqrt(epsilon). Both comparisons follow from 0<epsilon<=1.

## 3. Native residual witnesses and comparison with eta

Directly from the definition,

    Mstar(F)>=Astar*2^(31/2)L(F)
             =(Astar/2048)2^(53/2)L(F).                       (4)

The constants of(1) are the actual low-norm witness bounds proved in86, section3, from the independent original and refit annular certificates51 and52. In particular they are not inferred by taking a component of a full norm lower bound. Their derivation does not involve tau or beta. Equation(4) proves(1).

For all parameters here,

    eta=2^-25 tau^beta sqrt(epsilon)<2^-35.

Strictness holds because beta>1/2 and tau<1. The first integer in(1) exceeds 2^84; each of the other two exceeds 2^30. Division by eta gives the asserted strict gaps 2^119 and 2^65, retaining the additional Astar/2048 factor.

These are extended-norm lower bounds: if F is not in the high space its norm is infinite. No membership assertion is needed for this obstruction.

## 4. Dependencies and verification scope

The proof uses the exact reference bindings and completed-space exclusion73, the norm equivalences77 and83, and the native annular quotients51,52,86. It does not use the existence theorem89 except to compare its radius and threshold. The verification recomputes every new scalar comparison with rational arithmetic and checks the proof and prior audit hashes. It does not rerun the already audited coefficient reconstruction or annular integration. No new numerical optimization, quadrature or formal build is needed.
