# Primary Opus review of the negative-norm upper argument

## Statement, spaces and exact scope

Let F be real and locally integrable on R2, with finitely many positive
angular sine modes f_n(r) and integral r^3 f_n(r)^2 dr finite for each n.
All norms use Lebesgue measure. Define H(F) as the supremum of |int F phi|
over compact smooth real phi with ||grad phi||2<=1. Let psi be smooth,
in the gradient completion of compact smooth functions, with finitely
many positive sine modes and r Delta psi in L2. Set
A_F=-e_theta r sum f_n cos(n theta)/n, M2=||A_F||2^2, and
Z=A_(Delta psi)-grad psi. Then div A_F=F, div Z=0, and

 H(F)^2 <= M2+2t<A_F,Z>+t^2||Z||2^2

for every real t. If a=||Z||2^2>0 and b=<A_F,Z>, minimizing gives
H(F)^2<=M2-b^2/a. Orthogonal fields of different angular frequencies
permit the sum of their improvements. Tests at the same frequency
require a Gram matrix or selection of one test.

For a single mode psi=u(r)sin(n theta), write y=log r, v(y)=u(exp y).
Its components are Z_r=-v'/r sin(n theta) and
Z_theta=-v''/(nr)cos(n theta). Hence

 a=pi int (v'^2+v''^2/n^2)dy,
 b=(pi/n^2) int r f_n(r)(r^2u''+ru')dr.

These identities use angular integration. The first distributional
identity follows by angular integration by parts at each r>0, with no
radial flux at the origin. A_F and Z are in L2 by the hypotheses.
Cauchy-Schwarz and expansion of their squared norm prove the inequality.
The full argument, cutoff justification and rational trial formulas are
in ../candidate016_solenoidal_upper/PROOF.md. The T2 review is read in
full, including its distinction between the general statement and an
actual candidate application.

## Review and independent finite checks

Freeze the T2 primary review of T4-469, its exact fixture output, its
checker as text, and its log. Bind every target proof, supplement,
fixture and source hash. T2 is the existing theory lane configured for
us.anthropic.claude-opus-5-5. Its provider response identity cannot be
observed here. No replacement model, remote client or peer program is
executed. A hash binding is provenance, not a new numerical integration.

Independently reproduce the exact polynomial fixtures with rational
arithmetic. Put t=r^2/(1+r^2), w=1-t and u=r w^b P(t). Then
D_b P=(1-2bt)P+2twP', u_y=r w^b D_bP and u_yy=r w^b D_b^2P.
For source f=r w^e A(t), angular integration and dy=dt/(2tw) give

 d/pi=(1/2)int w^(2b-2)((D_bP)^2+n^2P^2)dt,
 a/pi=(1/2)int w^(2b-2)((D_bP)^2+(D_b^2P)^2/n^2)dt,
 M2/pi=(1/(2n^2))int w^(2e-4)t^2 A^2 dt,
 b_pair/pi=(1/(2n^2))int w^(e+b-3)t A D_b^2P dt,
 p/pi=(1/2)int w^(e+b-3)t A P dt.

The formulas for mixed powers follow by including every ordered pair.
Replace t by 1-w, and integrate each polynomial coefficient times w^q
as 1/(q+j+1), checking q>-1 or exact endpoint vanishing first.
For manufactured F=-Delta psi, A=(n^2P-D_b^2P)/t and e=b+1;
verify exact division before integration. Compare all fixture fractions,
the combined and mixed tests, the unmanufactured-source inequalities,
the two-exponent energy, and the same-mode Gram result against T2.

The positive-pole example is also exactly reproducible: substitute w=s^2
in its integral to obtain an even rational function of s with denominator
(1+3s^2)^2 on [0,1]. Divide the numerator by that denominator, then
resolve the remainder as C/(1+3s^2)+D/(1+3s^2)^2. Verify reconstruction
as a polynomial identity. The polynomial integral is rational, while

 int_0^1 ds/(1+3s^2)=pi/(3 sqrt(3)),
 int_0^1 ds/(1+3s^2)^2=1/8+pi/(6 sqrt(3)).

Thus the result is an exact rational plus a rational multiple of
sqrt(3)pi. Check those two exact coefficients against T2's closed form.
The separate decimal quadrature agreement remains a numerical observation.

## Candidate and tail hypotheses

The accepted N4-392 certificate identifies the complete candidate016
residual, raw SHA256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42,
as 1360 exact rational branches in the 160 sine modes 1,3,...,319, with
finite complete ||rF||2. Its accepted group certificates and the exact
trial labels in N4-399 supply the domain and integrability hypotheses.
This discharges T2 remark R4's finite-source condition for this candidate.
The full M2 need not be individually integrated in every mode: the proved
bound in ../candidate016_angular_tail_bound/PROOF.md includes every
omitted mode through accepted total ||rF||2 and positive modal squares.
It never identifies a partial sum with the full M2.

This audit confirms the general primary review and the finite-source
hypothesis. It does not accept a particular numerical improved H upper:
that remains subject to the separately assembled all-mode bound and the
announced reciprocal Opus review, including the tail application.
It establishes no linear inverse, contraction, exact solution, complete
trial basis or ordering of stationary correction distances.
