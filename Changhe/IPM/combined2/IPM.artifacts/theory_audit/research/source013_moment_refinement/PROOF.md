# Sharper source013 Sobolev bounds from the same certified moments

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248 and the unchanged source013 residual F and weight W=sqrt(1+4|X|^2) defined in ../source013_norms_actual_audit/PROOF.md. That theorem's exact source identities, accepted regional containment hypotheses, Fourier convention and H3 membership are retained here. Put g=WF and

    T_j=integral |D^j g|_F^2, 0<=j<=3.

The full ordered tensor convention gives T_j=integral |xi|^(2j)|g_hat(xi)|^2. Suppose the audited exact data give L_j<=T_j<=U_j. Define a rational Q1>=sqrt(U0 U2) and set

    U1_new=min(U1,Q1),
    E_m^+=sum_(j=0)^m binom(m,j) Uj_new,
    E_m^-=sum_(j=0)^m binom(m,j) Lj,

where the other Uj_new are unchanged. Then the integer Sobolev bounds sqrt(E_m^-)<=||g||_(H^m)<=sqrt(E_m^+) hold, as does

    max(sqrt(E_2^-), ((E_2^-)^11/E_1^+)^(1/20))
       <= ||g||_(H^(21/10)) <= ((E_2^+)^9 E_3^+)^(1/20),

provided E_1^+>0. The zero case gives g=0 and all norms zero. Every root used in a numerical display is rounded outward and checked by an exact rational power inequality.

## Complete proof

Apply Cauchy-Schwarz on Fourier space to the functions |g_hat| and |xi|^2 |g_hat|. Their squared integrals are T0 and T2, so T1^2<=T0 T2. Consequently T1<=sqrt(U0 U2)<=Q1, and intersecting this upper with the original U1 preserves containment. This argument is on the whole plane. It introduces no boundary term and does not use a regional integration-by-parts identity.

The binomial expansion of (1+|xi|^2)^m proves the displayed integer energies. Holder interpolation between orders2 and3 gives ||g||_(H^(21/10))^20 <= (E_2^+)^9 E_3^+. Interpolating order2 between orders1 and21/10 gives the lower twentieth-power inequality. Monotonicity supplies the other lower bound. These arguments use only the same g and the newly containing moment intervals, so the previous proof and all source constraints are unchanged.

For exact arithmetic, a nonnegative rational p and decimal scale S admit integers n with n^k<=p S^k<(n+1)^k. The rational n/S is a containing lower kth root; (n+1)/S is a containing upper, unless equality permits n/S for both. The checker constructs these integers and independently verifies the resulting inequalities after rational reduction. It checks Q1^2>=U0 U2, all revised binomial energies, and every square and twentieth-power endpoint.

## Dependencies and verification

The input is the actual independently replayed whole-plane moment record of AT1411-1413, not FLOAT samples or a new regional estimate. The checker binds its input moments, successful audit and actual reviews, and writes the revised intervals as exact JSON. The original published norm intervals remain true; this corollary tightens them using a relation between their moments. Its numerical result is asserted only after the verification/check_v01.json record passes.

## Scope

This supplies a tighter P-S1 residual norm upper and associated integer bounds for correction013. It does not change the residual, Candidate007, c, the weight or the plain L2 interval. It gives no P-S2 or strong Holder S_F norm, no global background or near/far operator bound, and no full inverse, invariant ball or stationary existence theorem. No closure ratio follows. No Lean build is used.

## Verified numerical instance

The exact check passed at2026-11-03T17:56:34.600797Z, after0.206326557 seconds and50 checks. The new containing T1 upper is1753172184615505697567/400000000000000000000000000.

| Order | Norm lower | Norm upper |
|---|---:|---:|
| 0 | 0.0013532483424295800722 | 0.0013532915780295398223 |
| 1 | 0.0013570907686964908636 | 0.0024928555025721900662 |
| 2 | 0.0034386898906426931721 | 0.0045920100720295764317 |
| 3 | 0.3653713152531953519335 | 0.3653913884879045330514 |

The resulting P-S1 H^(21/10) norm interval is [0.0035510975483434412497, 0.0071134188189452482335]. Exact rational endpoints and their power comparisons are in verification/result_v01.json and verification/check_v01.json. No additional numerical quadrature or source evaluation was used.
