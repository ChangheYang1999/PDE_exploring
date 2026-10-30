# The parent-transfer norm is a density norm

## Statement and exact hypotheses

Fix the campaign c and a real vector space C of real S1 functions in
L2(R2). For a reference density R, let S(R) consist of h in C for which
F(R+h;c)=0 in the stipulated distributional sense, with velocity
U_R+U[h], and define dist(R)=inf_{h in S(R)}||h||_2. The infimum of an
empty set is infinity. Suppose the two references R,R' obey condition(S):
g=R'-R belongs to C, U_(R')=U_R+U[g], and both equations use compatible
distributional senses. These are exactly theory_v07 section5.6's
hypotheses, not consequences of equality of residual sectors alone.

Then |dist(R')-dist(R)|<=||g||_2 when the distances are finite; in full
extended-real form,
 dist(R)-||g||_2 <= dist(R') <= dist(R)+||g||_2.
Consequently, if dist(R)>d and ||R'-R||_2<=tau<=d-b, then dist(R')>b.
The quantity tau must bound the density difference. A residual-difference
norm ||F(R';c)-F(R;c)||_2 is a different input and by itself does not
implement this criterion.

## Complete proof

If h' lies in S(R'), put h=h'+g. The vector-space hypothesis gives
h in C. The total densities coincide: R+h=R'+h'. The velocity identity
in(S) gives the same total velocity for both equations. Compatibility
of distributional senses therefore implies h in S(R). The converse
uses h'=h-g. Thus S(R')=S(R)-g. If one solution set is empty, both are,
and the extended-real inequalities follow. Otherwise apply both triangle
inequalities ||h-g||_2<=||h||_2+||g||_2 and
||h||_2<=||h-g||_2+||g||_2, then take the respective infima. The strict
transfer conclusion follows from dist(R')>=dist(R)-tau>d-tau>=b.

In the campaign notation R=rho_parent and R'=rho_child. Write
V=U[g], u=U_R. Direct expansion of the stationary residual gives
 F(R+g;c)-F(R;c)
   =(cX+u).grad g-g+V.grad R+V.grad g.
This is the residual difference, rather than g. The triangle argument
above has no occurrence of this expression. To replace ||g||_2 by a
norm of that residual difference would require another proved estimate
with its spaces, hypotheses and constant. No such estimate is supplied
by membership in the exact rational generator class or by the proposed
whole-plane integration. The rational integration engine can instead
integrate the density-difference field itself; that is the operation
already defined in ../reference_difference/PROOF.md.

## Source audit and verdict

The frozen theory_v07.md states g=R'-R and the exact tau requirement in
section5.6, and explicitly writes g=rho'-rho in its sufficient condition(P).
Its section6 request2 asks for this tau. N3's frozen12:25 ACK instead
proposes the field 'F_child - F_parent' and a legqs_norms/e2norms residual
calculation. Read with the campaign's F notation, this is the wrong
quantity for that request. Correct it to rho_child-rho_parent and check
(S), for example via(P), before using a certified upper bound. Whether
a particular transfer passes remains OPEN until that bound is compared
with the correct margin. A failed transfer test is not an exclusion.

Verdict: REFUTED the identification of the proposed residual-difference
norm with the requested density-transfer norm; CONFIRMED the correction
above under the exact stated hypotheses. No new numerical computation
or candidate verdict. The frozen source files, their hashes and the
source-inspection record provide the evidence. Nothing outside this
lane is modified.
