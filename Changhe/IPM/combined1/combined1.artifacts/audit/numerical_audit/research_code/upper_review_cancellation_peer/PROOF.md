# Cancellation in an ungrouped upper-bound trial

## Exact statement and hypotheses

Let t=r^2/(1+r^2), w=1-t, n=3, and psi=u(r)sin(3theta), where
u=r^3(1+r^2)^(-3/2)(1-t)=r^3(1+r^2)^(-5/2).
The two ungrouped coefficients are exactly1 and-1 at powers t^0,t^1,
both with beta=3/2. Then grad psi and r Delta psi belong to L2(R2),
and psi belongs to the gradient completion of compact smooth functions.
For F=-Delta psi, d=||grad psi||2^2, a=||A_(Delta psi)-grad psi||2^2,
and M2=||A_F||2^2, the exact values are

 d/pi=5/12, a/pi=25/432, M2/pi=205/432.

Consequently the claim that r Delta psi is in L2 exactly when the
minimum ungrouped beta exceeds3/2 is false. That strict inequality
remains a sufficient condition for the trial family already accepted
in N4-404 and T4-469. No candidate-domain hypothesis is weakened.

## Complete proof

The polynomial identity 1-t=w gives the stated combined expression.
Since r^3 sin(3theta)=3x^2y-y^3, psi is smooth on the entire plane.
At infinity u=O(r^-2), u'=O(r^-3), u''=O(r^-4), with the corresponding
higher differentiated bounds. Thus |grad psi|=O(r^-3) and
|r Delta psi|=O(r^-3), whose squares have finite polar integrals.
Smoothness gives local square integrability. A smooth radial cutoff
chi(r/R) equals1 on r<=R and0 on r>=2R. The gradient difference is
bounded by the gradient tail plus R^-1 times the L2 norm of psi on
that annulus. Both tend to zero. This proves the completion claim.

For exact integral verification write u=r w^b P(t) with b=3/2,P=t.
For y=log r, D_bP=(1-2bt)P+2twP' gives u_y=r w^bD_bP and
u_yy=r w^bD_b^2P. Angular integration gives

 d/pi=(1/2)int_0^1 w^(2b-2)((D_bP)^2+9P^2)dt,
 a/pi=(1/2)int_0^1 w^(2b-2)((D_bP)^2+(D_b^2P)^2/9)dt.

The source is F=r w^(b+1)S(t)sin(3theta),
S=(9P-D_b^2P)/t; its exact division is checked. Then
M2/pi=(1/18)int_0^1 w^(2b-2)(9P-D_b^2P)^2dt.
Substitute t=1-w and integrate each exact polynomial monomial as
1/(j+2). These operations give the three stated fractions, with
M2=d+a. Every denominator is positive. The ungrouped beta minimum
is exactly3/2, so the alleged necessity fails despite all admissibility
hypotheses being satisfied.

## Reciprocal review and scope

Read T4-475 proof and checker in full as text, freeze its result and
manifest, and verify their source bindings. Reproduce the cancellation
example with the own rational integrator of N4-404. Compare its other
manufactured, mixed, unmanufactured, same-mode Gram and positive-pole
fractions with N4-404's independently accepted exact results. An exact
match is reciprocal fixture confirmation, not a repeated candidate
integration. T4 froze the earlier T2 review49583d59; N4 froze its later
cfe759ad version after the source-run chronology correction. Keep both
identities and require their mathematical fixture result to be identical.

The general finite-mode divergence-free theorem and the candidate's
complete160-mode source premise remain accepted under N4-404. A
particular improved numerical H upper still has its own assembly and
reciprocal Opus review gate. No inverse, contraction, stationary solution,
trial completeness or correction-distance ordering is asserted. Existing
Opus5.5 theory lanes supply collaboration; configured identity is
us.anthropic.claude-opus-5-5, actual provider response unobservable.
No peer program, remote client, JavaScript/TypeScript, server or cluster
is executed. Exact JSON inputs and proof hashes are build dependencies.
