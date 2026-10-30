# Audit of the annular correction-radius calculation

## Claims and hypotheses

The source is the frozen T1 draft theory_v04.p3.md, section R2 item6,
and its annulus_admissible.py. This audit distinguishes its supported-
correction lemma from its proposed parameter-family ceiling and its
heuristic change of weights.

Let h belong to H^2(R^2), vanish outside20<=r<=32, and have only sine
angular frequencies n>=19. All norms below are on the whole plane.
Set q=(19/32)^2=361/1024 and omega(r)=(1+4r^2)^(2/5). Define

    E(h)^2=||omega D^2 h||2^2+2^15||D h||2^2+2^20||h||2^2.

Then

    E(h)>=A ||h||2,
    A=[1601^(4/5)q^2+2^15q+2^20]^(1/2).               (1)

For the sharpw norm X_s, assume the already audited comparison

    X_s(h)>=(1-ds)E(h), d=48/25, 0<s<=1/1024.          (2)

Let mu=97/250, C=397, b=8/5. The positive scalar margin is
mu-Cs-b R/sqrt(s)>0, where R bounds X_s(h). The single fixed ball is
s_f=1/5184, R_f=1351/10^6. The family allows varying s under its own
margin and the range in(2).

## Proof of the supported-correction estimate

For almost every radius, Parseval's identity for the angular sine
series gives integral|partial_theta h|^2>=19^2 integral|h|^2.
Polar integration and r<=32 on the support yield

    ||D h||2^2 >= ||r^-1 partial_theta h||2^2
              >= q ||h||2^2.

Integration by parts for H^2 functions, justified by smooth
approximation in H^2 or the Fourier transform, gives
||D h||2^2=<h,-Delta h><=||h||2||Delta h||2. Plancherel gives
||D^2 h||2=||Delta h||2 for the ordered Hessian tensor. Thus
||D^2 h||2>=q||h||2, including the case h=0. Weak derivatives vanish
off the support of h, and omega is increasing, so
||omega D^2 h||2>=omega(20)||D^2 h||2. These inequalities prove(1).
There is no boundary trace term introduced at20or32: the assumption
is that h is globally H^2 and supported there.

## Fixed radius versus parameter-family ceiling

At the fixed pair(s_f,R_f), equations(1)-(2) rigorously give

    ||h||2<=R_f/[(1-d s_f) A].                          (3)

The source's scalar maximum

    R_*=(2mu/(3b))sqrt(mu/(3C))                        (4)

is indeed the maximum of (mu-Cs)sqrt(s)/b. It is attained at
s_*=mu/(3C), which lies in(0,1/1024). But dividing R_* by
(1-d s_f)A does not give the parameter-family ceiling by this
argument: the parameter in(2) is still s, and s_* is greater than
s_f. At s_* the allowed radii approach R_*, while (1-ds_*)A is
strictly smaller than(1-ds_f)A. Hence the supremum of the radius
bounds supplied by(1)-(2) is already strictly larger than the
source's proposed family number. This is a defect in that derivation,
not a claim that its upper number has an explicit PDE counterexample.

One immediate conservative uniform repair is

    ||h||2 < R_*/[(1-d/1024) A].                       (5)

Every admissible s in(2) has1-ds>=1-d/1024>0, so(4)proves(5).
The exact optimal scalar envelope could instead maximize
(mu-Cs)sqrt(s)/[b(1-ds)A]. Its critical point solves

    d C s^2+(d mu-3C)s+mu=0.

That optimization is not needed for the conservative repair.

## Scope of localization and changed weights

Assumption(1) concerns a correction h supported in the annulus and
with the specified angular spectrum. Concentration of the reference
residual there does not prove either property of an exact correction.
Thus the annular improvement cannot be applied to every correction
merely from the residual measurements. The global bound obtained by
A=2^10 remains valid without these support or angular assumptions.

The later decaying-weight estimates in the source deliberately retain
R_* after changing the norm. They are heuristic, as the source itself
states; they are not a closure-radius theorem for the changed norm.
Nor does the necessary unweighted L2 distance transfer unchanged to a
decaying weighted norm. These points prevent the concluding sentence
'A weaker norm does not help' from following as a general theorem.
The distinct low-row-only implication in ../localized_high_margin/
PROOF.md does hold under its explicitly unchanged high-row hypotheses.

## Verification and dependencies

The positive-gap scalar envelope and norm comparison are inherited
from the audited sharpw framework. The displayed annular and
optimization arguments are complete. The checker encloses(3)-(5),
checks s_*<1/1024 and s_*>s_f, and compares conservative decimal
ceilings. All source files and exact parameters are bound in JSON.
No new PDE theorem, candidate evaluation, or residual upper bound
is asserted.
