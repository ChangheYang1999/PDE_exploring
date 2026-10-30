# Acceptance of the repaired normalized velocity review

## Claim and hypotheses

This result accepts the presentation repairs to T2's independent review
of T4-381 and T4-384. Their theorem statements and the acceptances in
T4-391 and T4-396 are unchanged. In particular let -5<q<-3, a=-q,
let H_q(h) be the maximum of the weighted amplitude and gradient norms
with weights (1+r)^a and (1+r)^(a+1), and let U be the canonical IPM
velocity, including its local density term. If a constant E bounds

 |U[h](X)+DK(X)M[h]| <= E H_q(h) |X|^q, |X|>=R0,

for all smooth real S1 functions with c[h]=0 and arbitrarily prescribed
positive L2 budget, then E >= (a-1)/(2a(a-3)). Here R0 is fixed,
M[h]=integral Xh(X)dX is absolutely convergent, and S1 means even in x
and odd in y. This is a universal estimate; the test functions are not
stationary solutions.

## Argument for the accepted repairs

The smooth normalized family is

 f_R=y(R^2+r^2)^(-(a+1)/2)/a,
 k_R=f_R-R^(-a-1)y eta(r^2)/a,
 eta(s)=exp(1-1/(1-s)) for 0<=s<1, and zero for s>=1.

A first sine mode has c[h]=-h_y(0)/4, so c[k_R]=0. Its first absolute
moment at infinity has radial majorant proportional to r^(2-a),
whose integral converges because a>3. The revised text now states this
condition. The original a>2 sentence was incorrect; a>3 was already
part of the actual theorem. The exact weighted gradient estimate gives
H_q(k_R) tending to one, while L2 scaling gives ||k_R||2 tending to
zero. The compact subtraction changes only the exterior dipole. The
Green formula therefore gives the same leading compensated velocity
as f_R. Taking the radius to infinity before taking R to infinity
proves the displayed lower bound. The complete calculation and origin
trace are in the accepted normalized proof alongside this topic.

The remaining repairs concern decimal inequalities. The revised checker
extracts each finite Arb endpoint as the exact dyadic rational m*2^e.
It finds a decimal scale 10^k using exact rational comparisons. A float
logarithm supplies only an initial guess; two exact loops correct that
guess. Multiplication by the decimal scale followed by floor or ceiling
then gives a rational lower or upper bound. The final decimal string is
converted back to an exact rational and its direction is asserted.
Thus rounding in the table does not depend on a rounded float endpoint.
The endpoint caps, critical E values and normalized sequence table now
all use the appropriate direction. The retained common caps and strict
critical bound are also asserted directly in Arb.

For example the 013 retained-delta cap is now at most 1.420801e-7;
the 014 positive-velocity onset is at least 21220.611; and the R=10000
weighted bound is at most 1.00000003. These safely enclose the already
accepted values. The fixed sharpw Ecrit values are at most 0.7850229,
0.7850635 and 0.7850374 for 007, 013 and 014, respectively. Each is
strictly below 0.785064. No theorem depends on a nearest-rounded table.

Only the exact theta-star entries are consumed from the separate 375
review result. Those entries are asserted to equal the exact angles
in the accepted 381 inputs. The full input hash is printed rather than
asserted, because a rerun changes its timestamp. The revised provenance
text now says this explicitly. The final three code, result and log
hashes in the review match the frozen files here. Earlier intermediate
files are retained separately. The mathematical checker diff adds only
the exact directed formatting, the stated Arb inequalities and this
provenance clarification; it does not alter the analytic formulas.

## Verdict and scope

CONFIRMED: all T4-396 repair requests are met in the frozen final review.
T4-384 remains AUDITED, as does T4-381. The final review was saved at
the recorded 10:58Z minute, after its final 10:57:44Z to 10:57:49Z run.
No foreign checker was executed in this acceptance. No new numerical
integral, stationary bound, inverse, candidate exclusion or existence
claim is inferred. The separate fractional-ball extension T4-397 still
requires its own independent review.
