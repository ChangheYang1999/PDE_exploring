# Completed finite checks and remaining physical hypotheses

The finite audit at2026-10-21T09:54:04.182343Z passed291 file pins,
all33 snapshots,208 prior pins,26 parts,208 parent-angle pairs and43949
retained rows. All219745 geometric field equalities and explicit Green,
trial, source-bracket and canonical partition checks pass. The inherited
two independent geometry computations cover106496 cases, including62547
omitted cases. New source_geometry.json resolves F1 and explicitly reports
the absent cart_derivative_table while checking the actual table, F2.

The direct Arb512 aggregate and exact nine-moment expansion plus iv160
powers pass14 independent cross-comparisons. Exact powers prove the six
strict ceilings in ADDENDUM.md. The inside/straddle products pass137235
checks per method;331 saved series tails pass exact, Arb and iv methods.
No physical q/c0 assertion is inferred from these scalar tail checks.

All six cutoff fields now pass263694 checks in each of two complete
methods: Arb256 with all explicitly proved critical points, and exact
rational full-polynomial Bernstein ranges on9 disjoint chunks covering
[0,43949). The latter uses no critical roots and no floating arithmetic.
The failed iv run and the coarse separate-factor method are preserved;
they are not counted as completed verification. The exact method's
unnecessary assertion that dmin>=0 failed on one valid negative outward
endpoint and was repaired, as proved in DISTANCE_ADDENDUM.md. Its earlier
four chunks used the stronger assertion; source equality except for this
assertion is verified. All source branches reject nonfinite saved fields.

The count17870 in the Arb output is the number of nonconstant cutoff
rows, comprising16502 transition plus1368 straddling rows. The final
packet uses that unambiguous name, resolving F3. Every inside row has
tau=1 and zero derivatives; all six saved fields are finite/nonnegative,
and T0>=1, which resolves the partial F4 objection from the truncated
first review. The new exact symbolic audit checks30 table entries,
four radial derivatives, five scalar composition orders and seven
Leibniz expressions against the frozen v2.2 source.

The auditor additionally found an error in the verifier's auxiliary
Hessian float export, unrelated to any forcing input: nextafter(0,+inf)
was greater than a saved zero on26079 constant rows. Its comment claiming
all exported values were below saved endpoints was false. The original
program/output and failure are retained. HESSIAN_EXPORT_ADDENDUM.md and
check_hessian_export.py replace precisely those auxiliary entries by the
proved exact zero and verify all43949 comparisons. Core cutoff and norm
checks did not use this auxiliary file.

Acceptance requested here is only the conditional finite theorem under
H0/H1/H2 in ADDENDUM.md. UPSTREAM_SCOPE.md makes a further dependency
explicit: even completion of the queued98/99/101 would not certify the
five nonlinear residual jets used here. The source constructs those jets
through differentiated density/ODE models and30 angular convolutions per
parent. Topic118's contemporary replay and reductions do not prove that
these jets enclose the physical residual derivatives. Neither a C0
remainder nor a source hash supplies that missing theorem. Full angular,
Cartesian, recentering, cutoff composition and Bernstein ancestry remain
required. B3 derivative suprema need further cells absent from the
retained forcing rows. These obligations remain OPEN.

The previous actual Opus5.5 requestf4b7c98b-0755-4a00-b5a7-12f6f5d49848
stopped at max_tokens, so its partial response is not acceptance. This
complete followup is requested to resolve its finite objections and any
new issues. No physical forcing norm, global inverse, nonlinear closing
inequality, neighborhood exclusion or decisive endpoint is asserted.
