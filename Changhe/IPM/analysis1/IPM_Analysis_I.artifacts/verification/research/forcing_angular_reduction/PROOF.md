# Finite angular-remainder reduction on regenerated inputs

Written before the checking code. The purpose is to verify the actual
finite arithmetic of a regenerated angular r2 reduction, under explicit
radial-model hypotheses. Historical r2 arrays were not preserved by the
producer. A regenerated computation cannot attest those absent arrays.

## Statement and scope

Use the frozen topic115 code and input NPZ files, identified by hashes.
There are13 radial cells ci=4096,...,4108; five radial derivative indices
i=0,...,4;523 sine modes N=0,...,522; angular polynomial degree8; and
angular derivative indices j=0,...,4-i. Let nu_N=2N+1. All observed
binary64 values below are treated as exact rationals.

For each ci,i,N, suppose the true radial modal function f_iN(s), on
0<=s<=h_ci, lies in a Taylor model
 P_iN(s)=sum_{q=0}^{12} c_iNq s^q,  |f_iN-P_iN|<=e_iN,
where |c_iNq-m_iNq|<=r_iNq. The radius entries and e_iN are nonnegative.
These are hypotheses on the inherited radial models, not results here.
Let H_ci,q>=h_ci^q be the regenerated nonnegative power bounds. Define
 B_iN=sum_q (|m_iNq|+r_iNq) H_ci,q + e_iN.                 (1)
Suppose the regenerated saved scalar E_iN satisfies E_iN>=B_iN.
Then E_iN bounds both |f_iN| and |P_iN| on the radial cell.

Let w be the common angular half-width from topic115. Suppose the
regenerated nonnegative factor b_jN satisfies
               b_jN >= nu_N^(j+9) w^9 / 9!.              (2)
For any angular center theta_c, put
 T_jN(phi)=sum_{p=0}^8 nu_N^(j+p)
                  sin(nu_N theta_c+(j+p)pi/2) phi^p/p!.
For |phi|<=w, the exact angular derivative has remainder
 |partial_theta^j sin(nu_N(theta_c+phi))-T_jN(phi)|
                         <= nu_N^(j+9) w^9/9! <= b_jN.  (3)
Consequently the sum of the angular polynomial errors multiplied by the
radial polynomials is bounded by
                         S_ciij=sum_N E_iN b_jN.        (4)
If a regenerated native r2_ciij is at least this exact positive sum,
it is a valid upper bound for this angular-error contribution.

## Complete argument

For0<=s<=h_ci, each coefficient interval gives
|c_iNq s^q|<=(|m_iNq|+r_iNq) H_ci,q. Summing proves
|P_iN|<=B_iN-e_iN<=B_iN, and the model error gives |f_iN|<=B_iN.
Taylor's formula with its integral remainder, or the repeated real
mean-value theorem, applied to partial_theta^j sin(nu_N theta) gives(3):
the ninth remaining derivative has absolute value at most nu_N^(j+9).
The remainder theorem is valid for both signs of phi by reversing the
integration limits; its absolute integral is |phi|^9/9!.
Multiplying(3) by |P_iN|<=E_iN and summing proves(4).

For clarity, the full polar interpolation error can be decomposed as
 f_iN sin_j - P_iN T_jN
       =(f_iN-P_iN) sin_j + P_iN(sin_j-T_jN).
The first term is bounded separately by e_iN nu_N^j. This note verifies
only the second contribution; it does not silently drop the first term
or certify the composed matrix coefficients.

## Finite verification, without a generic reduction-kernel hypothesis

Regenerate and save all65 radial model arrays, their E bounds, the five
factor arrays, the195 native positive sums and the195 native r2 outputs.
The frozen source formulas are checked explicitly. All sixteen angular
cells use the same factors because their formulas depend on j,nu,w only,
not theta_c; there are exactly13 times15 distinct reductions.

One checker will use Arb384 direct evaluation of(1),(2),(4). Another
will use exact rational arithmetic, expanding(1) into separate midpoint
and radius sums. They must check every coefficient, every mode and every
reduction, not samples. The factor inequalities also receive an iv120
check. Every output inequality is an exact comparison to a saved dyadic
endpoint. Thus a successful finite comparison of r2 with(4) requires no
unproved assumption about the actual reduction tree, FMA, or libm: its
input and output bit patterns are directly checked.

For additional context, topic115's sufficient condition is checked too:
the recorded native sum should exceed the exact normal threshold
523*2^-1021. This is not used instead of the direct finite comparison.
The generic subnormal counterexample in topic115 remains valid.

This result concerns regenerated inputs and outputs only. The absent
historical r2 arrays cannot be authenticated, even if the same code and
input hashes are used. The inherited radial models, their exact Green
interpretation, full polar polynomial coefficients and Cartesian/Bernstein
composition remain OPEN. No physical forcing norm or PDE endpoint follows.
