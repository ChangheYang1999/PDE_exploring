# Realization of admissible jets by local analytic profiles

## Statement

Fix c, omega and an integer k>=1. At a point y_0 prescribe the k-jet of (U,P). Suppose it satisfies div U=0 and the profile momentum equation through derivative order k-1. If b_0=(cI-omega J)y_0+U(y_0) is nonzero, this jet is realized by a real-analytic solution of those equations on a neighborhood of y_0.

Hence the formal-jet monotonicity hypotheses in A044 and A081 are equivalent to monotonicity along all local analytic solutions. This equivalence does not extend the realization to global decaying profiles.

## Proof

Apply an orthogonal change of coordinates so that the first component b_1 is nonzero at y_0. Replace J by its conjugate under this change; all coefficients remain analytic. Write b=(cI-omega J)y+U. The system is equivalent, wherever b_1!=0, to

partial_1 U_1 = -partial_2 U_2-partial_3 U_3,

partial_1 P = -(1-c)U_1+b_1(partial_2 U_2+partial_3 U_3)
              -b_2 partial_2 U_1-b_3 partial_3 U_1-omega(JU)_1,

partial_1 U_i = -b_1^{-1}[(1-c)U_i+b_2 partial_2 U_i
                         +b_3 partial_3 U_i+omega(JU)_i+partial_i P], i=2,3.

This is a first-order Cauchy-Kovalevskaya system for the four unknowns (U_1,U_2,U_3,P), solved for all their first derivatives in y_1. The right side is analytic in y, the unknown values and the tangential first derivatives, in a neighborhood of the prescribed values.

On y_1=y_0,1 choose polynomial Cauchy data in (y_2,y_3) realizing every prescribed purely tangential derivative through order k. The analytic Cauchy-Kovalevskaya theorem gives a local analytic solution. Its value b_1 stays nonzero after shrinking the neighborhood.

It remains to check the whole jet, not just the data. In the differentiated normal-form equations, any derivative of order at most k containing a normal derivative is expressed in terms of derivatives with fewer normal derivatives, of no higher total order. Induction first on total order and then on the number of normal derivatives therefore determines every such derivative uniquely from the tangential jet. Admissibility of the prescribed jet gives exactly these same differentiated normal-form relations, since division by b_1 is valid. The prescribed and realized jets consequently agree.

For the monotonicity equivalence, every admissible nonzero-b jet is now realized by a local analytic solution. Conversely every solution jet is admissible. At b=0, the derivative of any function of the local solution jet along B is identically zero, so those points impose no missing inequalities. This proves the equivalence stated above.

## Scope

This confirms the newly added Proposition 5.3 in Theory Agent C in the team records. The Cauchy surface is noncharacteristic only in this local normal-form sense. No global extension, decay, finite energy or pressure condition is supplied by this theorem.
