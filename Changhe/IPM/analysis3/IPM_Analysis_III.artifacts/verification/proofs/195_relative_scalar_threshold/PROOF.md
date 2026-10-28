# A relative high-norm countertest with an exact threshold

## Statement and scope

Use the exact normalized joined trial rho_0, k=1615536043799051/9007199254740992 and ell_0=1/k. Let A_0 be its closed high linearization on the realization specified in proof 171, with high correction space H_full and target Y_H. Let F_0 be the residual in that target, eta_0=||F_0||_(Y_H)>0, n'_0 the derivative of the moving-tail normalization and c the continuous strain functional. For a direction d in the actual domain of A_0, put

 alpha_0=1/(ell_0 n'_0),
 R_d=A_0 d-alpha_0 c[d] F_0.

Both summands defining R_d belong to Y_H. Suppose c[d]!=0. Under hypotheses(I) and(S) of the conditional nonlinear theorem in proof 174, the necessary inequality is

 ||R_d||_(Y_H)/(eta_0 |c[d]|) >= 1/N_4-alpha_0,
 N_4=-n(4)>0.

For this exact trial and the fixed moving-tail cutoff of that theorem, the right side is strictly greater than 507/10000. Consequently a certified relative upper bound

 ||R_d||_(Y_H) <= (507/10000) eta_0 |c[d]|

for even one such direction refutes the conjunction(I),(S). Conditional on(I), it refutes(S). No absolute evaluation of eta_0 is required for that implication. This result does not supply the displayed upper bound or an admissible direction satisfying it. It does not determine the actual Newton step or rule out existence of a solution.

## Proof

Proof 181 proves eta_0 |c[d]| <= N_4 ||A_0 d||_(Y_H) under(I),(S). The triangle inequality, applied to finite target elements, gives

 ||A_0 d||_(Y_H) <= ||R_d||_(Y_H)+alpha_0 |c[d]| eta_0.

Divide by the positive number eta_0 |c[d]| and rearrange. This proves the first necessary inequality. Membership cannot be bypassed by separately estimating the unrenormalized terms M_0 or L_fix d; proof 188 proves that those terms generally lie outside the target. Proof 190 gives an equivalent finite renormalized expression for R_d.

The exact scalar certificate of proof 181 gives

 N_4 <= B,
 B=900092961156364332680674281201404954097584961
   /99512486174167779552048599149925000000000000.

The bound uses the original-data enclosure S<=3763077494715567/100000000000000, and

 B=3/k-12+S_upper(4/3-1/(1-k)).

Its coefficient of S_upper is positive. The original-data bounds and the cutoff inequalities used there are part of the hypotheses. The same cutoff is zero for r<=1, and the outer angular amplitude is nonnegative, so n'_0>=3. Therefore alpha_0<=k/3. Since 0<N_4<=B<181/20, exact rational comparison gives

 1/N_4-alpha_0 >= 1/B-k/3
                    >20/181-k/3
                    >507/10000.

The companion exact-arithmetic script verifies each rational comparison and binds the prior scalar certificate. The strict inequality proves the announced implication even when the proposed relative upper bound is non-strict.

For comparison, the coarser replacement N_4<9.06 gives only 50/453-k/3, which lies between 0.05058 and 0.0506. It cannot alone justify 0.0506 as a lower threshold. The stronger 0.0507 here uses the separate exact B bound. Both thresholds are sufficient criteria for a countertest, not values of a computed norm ratio.

## Dependencies and verification

Proof 181 supplies the scalar-radius necessary condition and exact B bound. Proof 190 supplies the finite residual-subtracted split. Proof 191 shows why failure of a uniform sufficient criterion does not determine the scalar component of the actual Newton step. The companion code uses exact rational arithmetic only. Its success is required before the decimal threshold is recorded as verified.
