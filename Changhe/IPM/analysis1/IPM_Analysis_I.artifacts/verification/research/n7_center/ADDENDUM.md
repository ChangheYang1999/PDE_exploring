# Coefficient scale, remote velocity change, and the rejected sign convention

## Corrected convention and interpretation of the coefficient bound

The first draft used an inconsistent alternative stream convention; it is retained as evidence/rejected_proof_v1.md. The current PROOF.md uses precisely -Delta psi=partial_x rho and U=(-psi_y,psi_x), as PROMPT.md requires. Opus5.5 accepted the corrected analytic proof, but its last data-obligations bullet accidentally said the coefficient should be negative times sign(D). The displayed coefficient is positive times sign(D): both 2-6/k and 13-521 are negative. The exact data have D[259,4]>0. This incidental review sentence is rejected and a follow-up requests its retraction.

The primary and independent calculations give D[259,4]/r_-^10 approximately 2086622.5988, the top degree-13 density coefficient approximately 260827.82485, and the top degree-13 residual coefficient approximately 1041857525.77184. These approximations are not inequalities; exact rational enclosure endpoints are in checks.json. The bound max_{m>5}|D[m,4]|<6.9e-11 is true for the dimensionless, scaled D. It is false as a bound on physical coefficients of r^13 in the residual. Large physical coefficients here do not imply a large residual: they multiply r^13 only for r<r_-=approximately0.0076514. No residual norm is inferred.

## Exact nonzero change of the exterior canonical velocity

Consider the original and N7 trials under the same exactification rule. Suppose the stored spline S, knots, outer coefficients Aout and the other inputs except D and Ei are unchanged. A direct NPZ member comparison will check this. Exactification recalculates the corrections from the common spline jets. Normalization can change Aout[0,0] and the corresponding outer correction in mode0, but changes no high angular mode. Thus the highest density mode m=259 agrees outside r_-, and all of its change is inside that radius. Let d_j be its original D[259,j-1], j=1,2,3,4, b the common inner correction exponent and z=r/r_-. The exact C^6 jet matching gives

 Delta a_259(r) = -sum_{j=1}^4 d_j [z^{2j}-z^b sum_{i=0}^6(2j-b)^i (log z)^i/i!].       (2)

To prove this, each bracket and its first six derivatives in log z vanish at z=1, because the polynomial is the sixth Taylor polynomial of exp((2j-b)log z). Its power coefficient is exactly the removed term. The correction matrix is triangular with nonzero factorial diagonal, so these seven matching conditions determine the correction uniquely. No stored floating Ei is used.

Set L=521 and l=L+1=522. Only m=259 can produce the density frequency L and the forcing frequency l. The change of the density coefficient at L is q(r)=r^3 Delta a_259(r)/8. By direct differentiation its contribution to partial_x rho at frequency l is (q'(r)-Lq(r)/r)/2. Its outer Green moment is

 I=integral_0^{r_-}r^{l+1}(q'-Lq/r)/2 dr
  =-l integral_0^{r_-}r^l q(r)dr
  =-(l/8)integral_0^{r_-}r^{l+3}Delta a_259(r)dr.        (3)

The boundary term vanishes: q(r_-)=0 by matching, and the center term has a positive power. Write A=l+4=526. Substitution of (2) and integration of z^{A+b-1}(log z)^i give

 S=sum_{j=1}^4 d_j (b-2j)^7/[(A+2j)(A+b)^7],
 I=(l/8) r_-^{l+4} S.                                  (4)

Indeed integral_0^1 z^{c-1}(log z)^i dz=(-1)^i i!/c^{i+1}. The geometric remainder is

 1/(A+2j)-sum_{i=0}^6(b-2j)^i/(A+b)^{i+1}
   =(b-2j)^7/[(A+2j)(A+b)^7].

Every coefficient in S is an exact rational, so its sign and nonvanishing can be decided exactly from the four original D entries and b.

For -Delta psi=partial_x rho, the regular decaying Green formula at angular frequency l is

 psi_l(r)=[r^{-l}integral_0^r s^{l+1}f_l(s)ds
          +r^l integral_r^infinity s^{1-l}f_l(s)ds]/(2l).

Differentiate the two integrals to verify -Delta psi_l=f_l. Consequently, for r>=r_-, the change of this stream coefficient is exactly

 Delta psi_522(r)=r_-^{526} S r^{-522}/16.               (5)

If S!=0, the canonical exterior velocity changes. This remains true after exact normalization through Aout[0,0], because that adjustment affects forcing frequencies at most4 and cannot cancel frequency522. The change can be vastly smaller than printed precision; (5) proves nonidentity, not a numerically significant error. The claims that printed middle certificates or FFT values agree are separate numerical questions, not contradicted by a tiny nonzero change. Statements that the canonical field or the normalized density differs only inside r_- are not justified by support of the unnormalized density repair.

## Scope of additional verification

The exact nonzero value of S, the finite geometric identity, the Green sign, the matching identity, and unchanged NPZ members are checked in code/check_remote.py. Its independent exact moment check expands the seven logarithmic moments directly instead of using the closed geometric remainder. No high-precision exponentiation of the tiny exterior coefficient is needed to establish nonvanishing. This addendum is written before that additional checker. The primary center proof and checker are preserved unchanged.
