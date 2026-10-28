# What a knot-scale norm diagnostic can and cannot imply

## Claim under audit

The theory author's note42, dated2026-10-28 13:01Z, correctly labels a proposed violation of the scalar-radius test as heuristic. It also interprets alignment of a smooth scalar direction's image with the high-frequency residual as saying that the actual Newton step wants a change of the dilation rate comparable to minus ell_0. The following audit separates those two ideas.

The point and two-point estimates of topics179,182,187 are rigorous lower bounds for one scalar summand of the full high norm. They do not prove that this summand dominates the other summands, or that the sampled radial intervals dominate even the scalar H^(25/4) norm. To infer the necessary-test violation from the proposed multiplier W, one would need an upper bound for the complete image A_0d in the fixed norm, or equivalent controlled multiplier and remainder estimates. Those are still absent.

Even if a scalar-direction image is nearly parallel to a large residual, and the uniform scalar-radius test fails, the actual Newton step need not change the scalar parameter at all. This implication fails already for an invertible operator on a two-dimensional Euclidean space.

## Exact counterexample

Take X=Y=R^2 with Euclidean norms, F=e_1=(1,0), c(x_1,x_2)=x_2 and

 A = [[1, 1/20], [0, 1/1000]],
 d=e_2=(0,1), N=9.

Then A is invertible, c[d]=1 and

 A d=(1/20)F+(1/1000)e_2.

The image is close to a scalar multiple of F, with relative perpendicular error1/50. Nevertheless

 N^2 ||A d||^2=81(1/400+1/1000000)=202581/1000000<1
             =||F||^2 |c[d]|^2.

Thus the analogue of the necessary scalar-radius condition fails. But

 -A^{-1}F=-e_1,
 c[-A^{-1}F]=0.

The exact Newton step has no scalar component. Scaling the residual to L F for any L>0 does not change this conclusion: its Newton step is-L e_1 and still has zero scalar functional. Scaling A to L A at the same time also preserves the displayed relative alignment and the failure of the norm test for residual L F.

Every statement follows by multiplying the displayed2-by-2 matrix. Its determinant is1/1000 and its inverse is [[1,-50],[0,1000]], so there is no issue of singularity or approximate inversion. The companion script checks all comparisons as rational identities.

## Implication for the IPM heuristic

The counterexample refutes the logical implication from image alignment or the uniform norm-test failure to a specified scalar component of the exact Newton step. It does not refute the theory author's explicitly labelled heuristic about the actual IPM operator, whose inverse has additional structure. That heuristic would need further evidence concerning the inverse acting on this particular residual.

The distinction is relevant because the uniform inverse constant controls every forcing direction. A lower bound on that constant can come from a nearly cancelling combination of directions, while a particular forcing has an inverse with zero scalar component. The scalar-radius theorem is a necessary condition for the sufficient contraction criterion. Its failure would rule out that criterion on the stated ball and norm, but would not by itself rule out a small actual correction or existence of an exact profile.

For the actual IPM expressions, the leading radial derivative coefficient can be checked algebraically. Let u_f=U[f].e_r/r. The fixed-background high radial derivative of the density in A_0d has coefficient

 u_d+c[d](1-k^2 u_KP)/n'_0,

while the corresponding coefficient in F_0 is ell_0+u_rho0. Their formal ratio is the W in the theory author's note, wherever the latter denominator is nonzero. This coefficient comparison is not a high-norm estimate: angular derivatives, commutators, lower radial derivatives, both tails and the full sector must also be controlled. Values of the axis coefficient alone do not establish nonvanishing or a multiplier bound away from the axis.

## Verdict and scope

CONFIRMED: the stated radial principal-coefficient ratio, as an algebraic comparison where its denominator is nonzero.

OPEN: domination by the sampled knot zones, the needed complete-image upper bound, failure of the actual IPM condition(S), and the scalar component of its exact Newton step.

REFUTED as a general inference: nearly parallel scalar-direction image plus failure of the norm test forces a large scalar Newton step. The exact finite-dimensional counterexample proves the limitation.

Dependencies: topics181 and190 for the actual necessary tests, proof 187 for the rigorous scalar lower bound, and the immutable theory author note42 for the precise heuristic under audit. This is an audit of implications, not a nonexistence claim.
