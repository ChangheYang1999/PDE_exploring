# Corrections, completed checks, and exact scope

This addendum supersedes the following wording in PROOF.md. The proof's local
estimate (26), including every K_i formula and scaling exponent, is unchanged.
The auxiliary semigroup construction remains OPEN in this topic.

## Canonical stream function and the local distribution

The convention is Delta psi = partial_x h and U=(partial_y psi,-partial_x psi).
Let G=(2pi)^(-1)log r. With circular principal values,

 partial_xx G=delta_0/2+PV K,
 K=(y^2-x^2)/(2pi r^4),
 U2=-h/2+PV[(x^2-y^2)/(2pi r^4)]*h.

Thus the sign of K2 in PROOF.md is correct. The phrase local term-rho e2/2
in section5 is a typo: the local term is -h e2/2.

Differentiating a principal value distribution requires retaining its boundary
term. For a smooth test function phi, integration by parts outside r=epsilon
and Taylor expansion on its circular boundary give

 <partial_y PV K,phi>=<PV partial_y K,phi>
           +lim integral_(r=epsilon) K phi omega_y dS.

The constant Taylor term integrates to zero. The x derivative term also
integrates to zero. For the y derivative the angular coefficient is

 (2pi)^(-1) integral_0^(2pi) (sin^2(theta)-cos^2(theta))sin^2(theta) dtheta
 = (2pi)^(-1)(3pi/4-pi/4)=1/4.

All higher Taylor terms vanish in the boundary limit. Since
partial_y K=Ksigma=y(3x^2-y^2)/(pi r^6), it follows that

 partial_xxy G=partial_y delta_0/4+PV Ksigma,
 sigma[h]=h_y(0)/4+PV(Ksigma*h)(0).                         (A1)

Here PV is circular. The angular integrals of Ksigma against 1,x/r,y/r vanish,
so its principal value exists on smooth tests. In the convolution at0 the
kernel is evaluated at -Y. All bounds in section5 use its absolute value.
For the initially stipulated h(0)=grad h(0)=0, the local term in (A1) vanishes
and the integral is absolutely convergent. Consequently (18) is unchanged.
The proposed +h_y(0)/2 in the first follow-up was wrong; it omitted the
principal-value boundary correction. The Opus follow-up identified this and
the calculation above independently verifies the coefficient1/4.

## Scaling objection resolved

The multiplier B_s in (7) is not the cruder M_s=2^(s/2)W_s. If
f_delta=delta^a F_delta((X-P)/delta) with the uniform smoothness required in
section8, then

 W1(f_delta)=O(delta^(a-1)),
 ||f_delta||Hs=O(delta^(a+1-s)),
 B_s(f_delta)=O(delta^a+delta^(a-1)+delta^(a+1-s))
             =O(delta^(a+1-s)), s=3.1, delta<=1.

Thus B_s(q)=O(delta^(2-s)), B_s(T)=O(delta^(1-s)), and the bounded positive g
in Q is also O(delta^(2-s)), because 2-s<0. The original d_H and K3 rates
follow. The first localization review's contrary objection used M_s and was
explicitly retracted in the follow-up. W_s(chi) does occur in d_H; the
follow-up's residual comment claiming it occurs only in tail terms is false.
The actual d_H term has exponent (2-s)-s+(1-s)=3-3s, as stated in the proof.
No numerical test replaces this scaling argument.

## Completion and outer constants

The extension assertion means the graph completion of the initial smooth
admissible functions in

 ||tau Lh||Hs + ||h||Hs(B_(2delta)\B_delta)
              + ||h||Ht(B_(3delta)) + N(h).

The N term is applied to differences when defining Cauchy sequences. Estimate
(26) makes chi h Cauchy in Hs, and (18) makes sigma Cauchy. The restriction
and separated-kernel arguments similarly identify the local velocity limits.
No density assertion in a separately prescribed IPM space is made. In
particular, local Ht convergence alone does not control the remote moments
or imply the origin normalization for arbitrary limiting functions.
In section9 the constant b must include K2*C_A if A_h<=C_A O is substituted.

## Evidence and qualifications

The original proof was written before code; evidence/proof_first.json records
its hash and chronology. The unchanged proof, frozen source, current producer,
and fresh audit are hash-bound in evidence/checks.json and output_audit.json.
There are29 symbolic identities,54 scalar enclosures and62 exact rational
frequency pairs. Arb512 and mpmath.iv180 each check186 sampled inequalities.
The independent Arb1536 audit uses Gamma reflection, exact rational angular
symbol differences and exp/log powers. It verifies240 full-ball inclusions,
15 exact constants and16 affine box endpoint inequalities. The finite samples
are only supplementary checks of the universal proofs.

Three failed primary runs are retained. Direct diagnostics identified the
installed Arb generic power on a zero-containing ball as a source of NaN;
interval squares now use multiplication. Exact collinearity is handled by the
symbol's degree-zero evenness. Intersecting the ratios with nonnegative reals
uses their proved mathematical nonnegativity, not a numerical assumption.
No failed run was used as evidence of a successful enclosure.

The attempted bibliographic lookup did not produce a successful web result.
The earlier metadata claim of verification was retracted and preserved in
literature_context_retracted_before_review.json. The current status is
UNVERIFIED_AND_UNUSED. Remove the paper mention in the final paragraph of
PROOF.md from the dependencies: no external paper or theorem is used here.

The source coefficient box, C4/C5 regularity and E<kappa are hypotheses.
Actual certified disc derivative bounds, a high-Sobolev residual certificate,
outer estimates and the full IPM inverse are OPEN. This is no decisive endpoint.
