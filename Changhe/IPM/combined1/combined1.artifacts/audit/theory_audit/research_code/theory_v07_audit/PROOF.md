# Independent audit of theory_v07 preview 1

## Object, dependencies and exact scope

This audit concerns the complete frozen 542-line theory_v07 preview,
SHA256 393b6640fff20907d2a96184072b0f355e862c0f797c876acfbf45ffff277f5f.
The file was read in full. It is a preview, not the published exchange
version. The accepted source proofs and exact parameters are frozen in
source/ and data/. The numerical checks below concern new constants;
unchanged theory_v06 statements retain the T4-373 audit and its repairs.

## 1. Screening and domains

Let C be a real vector subspace of real S1 L2 functions. For references
R and R' at the same c assume g=R'-R belongs to C, their velocities
satisfy U_R'=U_R+U[g], and both stationary equations are interpreted in
compatible distributional senses. Then k solves the R' equation if and
only if k+g solves the R equation. Thus S(R')=S(R)-g. The triangle
inequality gives both extended-real distance inequalities in 5.6(a).
Empty solution sets cause no subtraction of infinities because the
finite quantity ||g||2 is subtracted from a single extended distance.
If dist(R)>d and ||g||2<=d-b, then dist(R')>b. This proves 5.6(b),
including the direction and the boundary case of its sufficient test.
Its contrapositive excludes the closed L2 ball of radius d-b.

The sufficient generator hypothesis (P) is exactly T4-393: equal
leading potential coefficients for l=1,...,4 cancel all non-L2 density
and velocity tails. The remainder and all its differentiated tails are
O(r^(1-5delta-k)). At the actual delta this is square integrable.
The velocity difference and the canonical L2 velocity of g have the
same divergence and curl; their difference is L2 and harmonic and
therefore zero by Fourier transformation. Both stationary products are
locally integrable, so adding g preserves the equation in distributions.
The smooth-origin and first four sector identities used here are exact
properties of the generator family. Mere density sector matching is
not substituted for these hypotheses. No H_q assertion is inferred.
Sections 5.6(a)-(e) and the actual failed 021-to-020 transfer agree with
the accepted T4-393 and T4-394 statements.

## 2. Endpoint certificate and weighted norms

All the hypotheses of T4-335, T4-338, T4-339 and T4-351 remain explicit
in 5.7(a). In particular a finite H_q correction and the reference
remainder bounds are required. The gradient limit gives the rational-
angle lower bounds H>H0. Using the integer H0, rather than silently
using the larger computed value, gives the following safe upper bound
for the square root of the CI right side:

 cap=B r0^(q+1)/sqrt(-2q-2),
 r0=[sqrt(2pi) H0 (v0+E g0)/(D_delta B)]^(1/delta).

Dropping other nonnegative error terms increases the right-side bound.
Because q+1<0, the cap decreases with H0, E, v0 and g0. Solving cap>=beta
therefore gives the necessary upper threshold for E printed in 5.7(b).
The first-sine test gives E>=(-q-1)/(2(-q)(-q-3)). The moment formula in
5.7(c) is pi B(4,a-3)/a=6pi/[a^2(a-1)(a-2)(a-3)]. These identities have
exactly the signs and normalization of the canonical velocity theorem.

Retaining the single radial error term gives the sharper factor
sqrt(1/A-2/(A+delta)+1/(A+2delta)), A=-2q-2, in place of 1/sqrt(A).
The checker recomputes both caps and all four E thresholds for each
candidate using the printed integer H0. It checks the gap at the fixed
sharpw radius, rather than only the rounded family ceilings. The
combined conclusion NC-T-UNIV-E is CONFIRMED for this universal-constant
form of CI. It bounds one certificate, not the solution distance or
all possible endpoint arguments. Moment interpolation cannot improve
these cap bounds since their derivation already drops the moment terms.

If ||k||Y>=H_q(k), every stationary k in the stated class has ||k||Y>H0.
Under a valid Newton-Kantorovich theorem with K>0 and K eta<=1/2, its
majorant radius t* obeys t*<=2eta and t*<=1/K. Existence of the produced
solution then forces eta>H0/2 and K<1/H0. The weakest H0=999745 yields
eta>499872.5 and K<1.00026e-6. If K=0, the majorant is linear, t*=eta;
eta>H0 and K<1/H0 hold directly. A reference to 1/K must either specify
K>0 or use the extended value infinity at K=0. The preview's intended
conclusion NC-T-ENDPT-Y is correct with this elementary endpoint case.

## 3. Candidate 021 and status repairs

The stated lower distance is the exact downward rational bound of
T4-392. Dividing it by the upward rounded scalar ceilings and the exact
graded ceiling gives the three downward ratios in section 3. The
point, origin and complete prefix use T4-387 to T4-389. Their scopes
remain separate, and the direct weak test supplies the all-ball
exclusion. The table is therefore CONFIRMED. No comparison of lower
bounds is interpreted as an ordering of true distances.

The preview correctly incorporates the q>=4 scaled-block repair,
the precise annular support/frequency conditions, the held-out timing
qualification and the R1-037 residual-rate correction from T4-373.
It also correctly distinguishes the 81 current analytic rows from
statistical or historical independence. The 022 actual-shape claim was
OPEN at the preview's cutoff; later N4-321 requires a new acceptance.
T4-384 is now AUDITED through T4-396, and the T2 review repairs are
accepted by T4-398. Those are status updates after the frozen cutoff.
T4-397 remains OPEN and must not yet be used as an input.

## 4. Required wording qualifications

The literal sentence 5.7(d)(i), "It has to fail for the test function
of (c)", is too broad when applied to an arbitrary stationary-only
velocity estimate. Restricting the already proved universal estimate
E=133.004254... to stationary corrections gives a stationary estimate
and does not fail on the test. Replace it by: "An estimate sharp enough
to evade NC-T-UNIV-E must use additional restrictions that exclude the
universal test sequence." The open question is a sufficiently sharp
stationary estimate. The intended necessary condition is unaffected.
Section 6 item 4 may likewise refer to a correction-specific tail
expansion or further hypotheses, as well as direct use of stationarity.

In 5.7(e)(ii), state K>0 for the 1/K formula and handle K=0 as above.
The phrase "no numerical report since numerics_v10" should say "no
published versioned numerics report" because NUMERICS_FINAL has had
several revisions that this preview itself cites.

## Verdict

CONFIRMED: NC-T-SCREEN with full (S), NC-T-UNIV-E on its explicit domain,
NC-T-ENDPT-Y with the K=0 qualification, the 021 table and all four
T4-373 repairs. REFUTED as a literal unrestricted assertion: every
stationary-only velocity estimate must fail on the universal test.
The intended sharp-estimate question remains OPEN. Published v07 and
future status changes require their own exact-file check.
