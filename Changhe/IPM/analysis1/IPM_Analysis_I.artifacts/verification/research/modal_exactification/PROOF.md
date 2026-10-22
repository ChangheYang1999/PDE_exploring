# Audit of modal trial exactification and outward conversion

Date: 2026-10-20. Scope: the immutable snapshots and hashes in evidence/snapshot_manifest.json, read at their recorded UTC time. The actual calls and exact rational counterexamples are reproducible with code/audit_definition.py. The trial snapshot has SHA256 a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874. This note distinguishes the stored dyadic trial from a future exactly defined repair.

## 1. Stored coefficients do not have exact joins

For clamped degree-seven splines with coefficients S_mi, the endpoint values are S_m0 and S_m,last. The inner and outer formulas in the numerical source have coordinate tau=0 at their intended joins. Hence the value jumps, outer formula minus spline, are exactly

J_in,m=delta_m0+sum_j D_mj+Ei_m0-S_m0,
J_out,m=sum_q A_mq+Eo_m0-S_m,last.

Every input in these identities is a stored binary64 number and therefore an exact rational. Independent Fraction arithmetic finds nonzero jumps in all 260 modes at both endpoints. The largest absolute inner jump is about 5.77401e-15; the largest absolute outer jump is about 6.63968e-23. These are exact nonzero rational results, not roundoff estimates. Thus interpreting all stored coefficients literally does not define a continuous modal trial. Trigonometric linear independence prevents nonzero modal jumps from cancelling at all angles.

The numerics report separately proposes defining Ei, Eo, and one far coefficient by exact equations. Such an exactified trial is a different, potentially valid object. This first objection does not refute that convention. It requires that certificate and residual calculations consistently use that object and quantify its distance from X3.

## 2. The exactification code uses two different radial endpoints

The snapshotted cert_green.py defines tmin=log(rmin) and t0=log(R0), where the radii are the exact stored dyadics. Its SplineCells instead uses the exact stored dyadic knots. Those endpoint knots are the previously rounded logarithms. It solves the correction equations using spline jets at the knot endpoints, but its inner/outer scalar integrals use tmin and t0. Its Green code uses the knot endpoints in the exponential prefactors instead. These conventions are different in exact arithmetic.

Independent Arb calculations at 256 bits, using the exact dyadics, enclose

log(rmin)-knot_first = -2.00049303258570034...e-17,
log(R0)-knot_last = 2.35615599600723169...e-16.

Both balls exclude zero. Equivalently, exp(knot_first)-rmin is about 1.53066e-19 and exp(knot_last)-R0 is about -8.04148e-13. The first and last integration boundaries therefore have a gap relative to the physical intervals specified by those radii. Smallness does not give exact joins or exact agreement of two strain formulas.

A consistent repair is to define the physical region boundaries by exp of the exact endpoint knots, use the knots themselves as all logarithmic boundaries, and evaluate their exponential prefactors in outward arithmetic. Another is to replace the endpoint knots by exact logarithms and rebuild every affected spline formula. Either is an exact mathematical convention, not a floating equality assertion.

## 3. Direct Arb-to-double midpoint/radius export loses enclosure

For an Arb ball z with exact midpoint m_A and radius r_A, conversion to a double midpoint m introduces an error |m-m_A|. A valid exported double radius must satisfy

r >= r_A+|m-m_A|.

The snapshot exports float(z.mid()), float(z.rad()) without this correction. At 256 bits, applying that rule to z=1/3 gives double midpoint 0x1.5555555555555p-2 and radius 0x1p-257. Exact rational arithmetic shows that the interval misses 1/3 by more than 1.85037e-17. Thus this export rule is refuted. The separate MR.from_arb routine includes a conversion allowance, but main() in this cert_green snapshot does not use it.

Writing dependent coefficient midpoints as 60-digit strings without radii also does not create exact satisfying coefficients. Such strings can be informational approximations if downstream certification re-evaluates the exact defining equations. They cannot silently replace those equations.

## 4. An unsafe absolute-value lower bound

The snapshotted MR.mig returns max(abs(m)-r,0) in round-to-nearest arithmetic. Take m=1 and r=2^-55. The exact infimum of absolute value on the interval is 1-2^-55, but the actual function returns 1. This is a false lower bound, confirmed by an actual source call and exact Fraction comparison. An outward downward subtraction followed by maximum with zero repairs it.

The module's exponential remainder routine explicitly assumes a libm error bound; its random tests do not prove that assumption. No certificate depending on this routine has been accepted. The other midpoint-radius operations require their own audit; these counterexamples do not claim they all fail.

## Dependencies and verdicts

The value jumps use clamped B-spline endpoint identities and exact dyadic arithmetic. The boundary mismatch uses outward logarithms and exponentials with exact inputs. The conversion and lower-bound failures are elementary rational inequalities. All four findings are CONFIRMED counterexamples to the indicated snapshot claims. A corrected exactification, consistent Green operator, and residual certificate remain OPEN. None of these findings excludes an exact nearby IPM solution.

## 5. Gradual-underflow matrix counterexample

The refreshed midrad source SHA256 269e543b4c0a0c074d02fdb574c8e9bcffcfc115ebe4d3f60f6ffe81cde26833 still fails its claimed general gradual-underflow enclosure. Let eta=2^-1074, K=100, and let every entry of a 1 by K midpoint-radius matrix A have midpoint and radius 2^-537. Let every entry of a K by 1 matrix B have midpoint and radius 2^-538. The midpoint products and each of the three propagated-radius products have individual terms eta/2. In the actual tested BLAS path these tie to zero. The routine's final allowance and successor operations return midpoint zero and radius 105 eta. Choosing all upper endpoints in the input intervals gives the exact admissible product K times (2 times 2^-537)(2 times 2^-538)=200 eta. It lies outside the returned interval.

The executable audit uses exact Fractions for this comparison; the complete result and source hash are in evidence/underflow_audit.json. This refutes the routine's general enclosure claim in its stated arithmetic model. It does not prove that a particular residual run reaches these exponents. A valid application could instead prove appropriate lower exponent bounds for every operation or replace the insufficient underflow allowance with a proved one. A separate initial objection to the normal-range gamma factor was withdrawn after analysis; it is not counted as a counterexample.

## 6. Actual dependent-coefficient JSON import fails containment

The completed numerics Green run produced data/cert_coeffs.json. A snapshot of that actual file and its writing and reading sources is retained in evidence/coeff_export_1453/; the directory label is descriptive, while evidence/dependent_export_audit.json records the real audit time and hashes. The writer prints Ei, Eo and A00 with str(60, radius=False). The outer/inner Green reader actually imports those strings with arb(x) at 256 bits. This replaces each exact dependent coefficient by a much narrower enclosure of a rounded decimal. It does not retain the defining equations.

The independent audit reconstructs endpoint jets by exact rational derivative B-spline recurrences. All 1820 inner coefficients and all 1813 outer coefficients in modes m>=1 lie outside their actual imported balls. These outer modes have no scalar-dependent coefficient, so their comparisons are exact rational inequalities. For A00, the imported ball is disjoint from the independent mpmath.iv enclosure of the exact normalization-defined value. This last comparison uses a real interval rather than pretending A00 is rational.

There is also a direct join contradiction after the import. The first four inner value-jump balls all exclude zero. In mode zero the jump is approximately 2.0191193e-69, with radius below 5.33e-77. It equals imported Ei_00 plus the exact non-correction inner value minus the exact spline endpoint value. Hence even the value join cannot be certified exactly for the imported coefficients. The size is negligible for ordinary floating evaluation, but an enclosure proof must cover it.

Verdict: CONFIRMED failure of actual dependent-input containment. This does not establish that a published final residual upper bound is numerically too small. It blocks accepting its current proof of enclosure. Export enclosing balls, exact dyadic endpoint intervals, or recompute the defining equations in the consumer; then include the resulting uncertainty uniformly in downstream arithmetic.

Follow-up audit: code/audit_dependent_export.py now extracts and executes all three assignment statements of the actual frozen outer/inner reader by Python AST, with the same 256-bit precision and the actual coefficient JSON. It also asserts the clamped-knot and degree conventions. The containment failures are unchanged. Across all checked coefficients the largest relative discrepancy between the exported decimal and the exact coefficient is below 5.002e-59; the worst entry is Eo mode82, power6. This quantifies the small error and rules out a large hidden convention mismatch as its explanation. The source snapshots and input hashes remain recorded. The scope is still false input containment, not a numerically false final residual bound.

## 2026-10-20T15:31:52.371224+00:00 Radius export repair is still insufficient

The new nested ball exporter in cert_green.py (SHA c608e80add8bce6d637aadb69874ce59f3a72c750c3e2a27473d0be65fc90719) prints the Arb radius with five significant digits and radius=False, converts that nearest decimal to binary64, then multiplies by 1+1e-9. This is not an upper bound of the radius. A five-digit decimal can round down by about 1e-5 relatively. The added 1e-95 times the midpoint is irrelevant in the exhibited regime.

Executing the exact AST-extracted exporter and loader at Arb precision256 on x=arb(1,"1.23451") loses an upper endpoint amount 5369/536870912. The same test with radius1.23451e-70 loses an upper endpoint amount 7411/7410693711188236507108543040556026102609279018600996098525285376506440296955904. Thus outward rounding when Arb receives the new radius does not repair the missing interval. These are exact rational stored-midpoint-plus/minus-stored-radius comparisons, not float comparisons or rounded endpoint extraction comparisons.

Verdict: REFUTED as a general enclosing-ball export rule. This alone does not prove that a particular dependent coefficient or final residual bound fails. Full source snapshot and executable reproduction: evidence/radius_export_source_snapshot.py, code/audit_radius_export.py, evidence/radius_export_audit.json. A safe replacement should export exact dyadic midpoint and radius integers/exponents, or a rigorously outward decimal bound without nearest five-digit truncation.
