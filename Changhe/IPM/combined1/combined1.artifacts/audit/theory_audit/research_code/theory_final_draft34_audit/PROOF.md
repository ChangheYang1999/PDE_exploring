# Independent audit of THEORY_FINAL draft34

## Object, hypotheses and inherited results

The object is the frozen1655-line THEORY_FINAL draft34, saved by its
publisher at12:02Z and copied at2026-10-29T12:34:57.665394Z. Its SHA256 is
febf6c09e19a2e6b585c5263348250017d4af86fca9aa731db89fbc6d6106b40.
All989 lines of its difference from the accepted draft24 were read.
This audit confirms the changed mathematics under the hypotheses stated
below and identifies changes needed before the next consolidated report.
It neither certifies unseen later edits nor claims an existence closure.

The unchanged conditional closure theorems, contact term, fixed-c gauge,
maximal low and high operator domains, derivative bounds and coefficient
assumptions retain the accepted proofs of T4-358 and T4-373. Frozen copies
of those audit arguments and the sharp-L2 theorem are source dependencies.
T4-412 independently controls the intervening theory_v07 publication.
The full hypotheses cannot be replaced by a small sampled residual, a
single matrix margin, or the finite-dimensional rank of a candidate basis.

## 1. Conditional closure and exact arithmetic

Write X_(s,w)(f)=E_w(J^s f), J=(1-Delta)^(1/2), where
E_w(g)^2=||omega D^2g||_2^2+w1||Dg||_2^2+w2||g||_2^2,
omega=(1+4r^2)^(2/5). The correction ball has c[h]=0, a fixed
reference exponent c and a fixed leading far-field profile. The sharpw
parameters are mu=97/250, C=397, s=1/5184, cU=8/5, w2=2^20,
r=1351/10^6, eta=4207/(2*10^7), betaL=2. Under all reference and
commutator hypotheses of section2.1, the high rate is

 beta=mu-C*s-cU*r/sqrt(s)=63092119/405000000>1557/10000.

Thus eta/(1557/10000)<r and eta/beta<r. The exact beta also gives
1/beta<6.4226, even though1/(1557/10000) is slightly larger. With
c_s=1/(2 sqrt(pi*s*(1+s))), c_s*r/betaL<0.0137200. No background
hypothesis is inferred from these arithmetic inequalities.

The same family has a necessary L2 ceiling
b=(2mu/3)*sqrt(mu/(3C))/(cU sqrt(w2))<2.8496e-6. Keeping this formula,
cU and w2 fixed, raising b above the007 distance requires
C_new<397*(125/97)^3/1673^2=775390625/2554506927217<3.04e-4,
since positivity of the first Gram diagonal forces mu_new<1/2.
This necessity does not constrain an unrelated high estimate.

Every numerical row of section7 is checked by exact rational division
against the conservative ceilings3.7930e-6,2.8496e-6 and25/54684.
For D>d and beta<=b, d/b>q proves D/beta>q. Strict weak-distance
floors, not the six point tests, provide all-family exclusions. The
input floors remain independently established in their original topics.
The checker also gives conservative rows for the newly accepted023 and024.

## 2. New theorem passages

The third cutoff and endpoint result retain their finite angular,
nonresonance, differentiated-remainder and fixed-c assumptions. Their
acceptance is T4-365. The fourth cutoff and the positive endpoint
projection terms are T4-368. Small L2 cost of a tail surgery does not
make a fixed residual small, and the report correctly separates these
claims. The annular moment construction is accepted in370; its complete
residual is asymptotic to a nonzero multiple of R^(-2), as corrected in373.
The sharp amplitude moment bound is accepted in382 in the amplitude
class, with no sharpness asserted for the weighted-C1 class.

The screening argument preserves compatible canonical velocities and
operator domains. Equal nonintegrable sectors give L2 membership but
not every other compatibility condition. The extended-real triangle
inequalities avoid infinity minus infinity. The sufficient finite-basis
condition(P) is separately proved. A screen that fails its quantitative
inequality decides nothing about the existence question.

The universal compensated-velocity obstruction ranges over the stated
whole S1 class, including its fractional-ball and normalization
restrictions. It is not an impossibility result for an estimate that
uses the stationary equation. H_q controls both the amplitude and the
full gradient; a norm controlling H_q must include the corresponding
large endpoint radius. The K>0 and K=0 Newton majorants are correctly
separated. No scaling tangent in a nonintegrable far-field direction is
silently admitted to an L2 correction chart.

The017 cover is a complete rational partition with all leaves verified,
so its background rate is established. It gives no high inverse. The
profile limit of402 has no finite-radius remainder. The0.583 radial
cap of414 is the integral of the positive-part radial profile, not the
cutoff test alone. The report correctly calls the earlier cutoff rooms
necessary and not sufficient. The0.372 bound of415 and the optimistic
zero-error cap of422 remain subject to the pending independent review.

## 3. Exact scope needed for the remainder summary

The current two-weight construction uses q=1/c-4, delta=1-1/c,
kappa=1-q and the positive delta-term in the T4-335 tail list. It forces
0<epsilon<=delta. In the original A_in construction, the general bound
J(s)/H>=lambda*(5/s)^delta with lambda=1/2+5*2^(1-q) was proved
for s>=max(L0,5); on L0<=s<5 the supplied proof uses J(s)/H>=lambda.
Use this piecewise statement rather than silently extrapolating the
first intermediate inequality. Both give the same campaign obstruction.
This audit does not assert that the full J violates the extrapolated
bound; it identifies the hypothesis of the cited derivation.

Radial averaging must use
Eeff(r)=kappa*r^kappa*integral_r^infinity E(s)*s^(-kappa-1)ds.
The phrase effective constant above1.72 needs the specific fallback
Eu=1.747261 used in that numerical illustration. It is not the general
lower bound proved for every admissible universal fallback. The general
statement accepted in432 is stronger in scope: Emin=0.7930365064... and
Eeff>0.79303 up to every campaign target cutoff, above all required
Kcrit/Phi<0.785064. The outer-only extension has Eeff>0.79303648 at
each target and requires Ebase>=Emin in the fixed input tail list.
Neither estimate is a lower bound on the actual compensated velocity.

A full CI can start beyond r_grad. The general necessary condition is
max(R,r_grad)<=r_beta; comparisons that use R<=r_grad must name that
extra condition. Draft34 states that condition on its51*Kcrit line,
which is accepted. T4-421 and432 now remove that restriction from the
campaign failure by different arguments. The report should quote these
accepted arguments rather than leave the whole consequence CLAIMED.

## 4. Status and wording repairs before the next draft

1. Update023 and024 to the complete independent exclusions420 and431,
with the actual raw snapshot hashes and all-family scope. Remove their
untested, no certified distance and FLOAT-only descriptions. Historical
statements explicitly tied to matrixv120 may remain as history.
2. Use414 AUDITED via423,410 AUDITED via424, the campaign consequence
CONFIRMED in421, and425 AUDITED via432. The four outer-remainder errata
are accepted. Keep415/422 pending until the independent review arrives.
3. The sentence in section3.4 saying acceptance of R1-039 is pending is
stale:382 accepts it. Section9.1 already calls it AUDITED. Align them.
4. The smallest confirmed G0 is now016, in N4-341. The preferred complete
reference007 may be described by its broader hypothesis record, but no
longer as having the smallest confirmed G0. This was a later result, not
a retroactive error in the12:02 snapshot.
5. Replace every universal velocity constant can be taken below1.747261
by there exists a valid universal coefficient below1.747261. Admissible
coefficients are upward closed, so their set itself has no upper bound.
This is a quantifier clarification, not a change to the proved upper
bound on the optimal coefficient.
6. Where the9.28e-11 cap uses E_q*>133, call it the original T4-335
coefficient. The current sharper universal estimate is below1.747261,
with a separate obstruction using the improved endpoint H lower bound.
7. Extend the untested dyadic range through the latest snapshot number.
No full-family L2 result transfers to the decaying-weight dyadic ball.
8. Use the full radial-average result and its explicit input coefficient
hypothesis as in section3. Avoid treating the floating kernel thresholds
of426 as a complete sufficient CI criterion.

## Verdict and verification

CONFIRMED the changed theorem statements under their cited hypotheses,
the correction-chart and inverse distinctions, the source-specific
remainder comparisons, and the exact closure and ratio arithmetic.
The current-status assertions listed above must be updated; they do
not reverse an exclusion. The unrestricted1.72 fallback interpretation
is OPEN, not proved by the cited fixed-fallback computation. The existence
question, the stationary-only estimates, and the missing localized high
inverse remain OPEN. No publication beyond this frozen source is audited.

The finite checker verifies the frozen bytes and every numerical ratio,
the exact sharpw rate and self-map slack, the family ceiling and the
necessary C requirement. It uses local exact arithmetic and Arb only.
It imports no foreign code and repeats no large candidate integral.
