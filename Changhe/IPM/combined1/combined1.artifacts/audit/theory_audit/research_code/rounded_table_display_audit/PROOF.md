# Rounded values in a column headed “residual LB”

## Statement and exact premises

This is a finite audit of the coordinator report frozen at SHA256
7fd963af5ac20ddc4cf2a2c253f1e1f76e7d719af431642108714311307b4743.
The column at line 1050 is headed “residual LB”. Its rows 20 and 37,
at lines 1069 and 1086, display the d2 full-plane residual norm G0 as
4.99. Row 80, at line 1129, displays the candidate 016 full-plane norm
R = ||r F||_2 as 7.1457012. The norms are real nonnegative Lebesgue
norms on R2 of their source-bound residuals; neither is a grid maximum.

Assume the accepted complete d2 G0 certificate of N4-024 and the complete
016 component certificate of N4-392, independently composed in T4-467.
Their exact enclosing intervals are the source JSON records bound in the
manifest. T4-467's earlier local copy is also bound, so the 016 premise
does not rely solely on N4-439's new description. Let their positive
containing endpoints be a_d, b_d and a_16, b_16 respectively. The exact
comparisons established here are

  4.985 < a_d <= b_d < 4.99 < 4.995,
  7.14570115 < a_16 <= b_16 < 7.1457012 < 7.14570125.

It follows that the three printed values are valid nearest decimal
summaries, but are not lower bounds on their respective quantities.
Thus the blanket literal interpretation of “residual LB” is REFUTED.
N4-439's correction of this heading and these three entries is CONFIRMED.
This acceptance does not cover every supplemental check in N4-439, nor
assert that any exclusion ratio was computed from a rounded value.

## Complete argument

For a real x in [a,b], a positive decimal unit u and a displayed decimal d,
the strict inclusions d-u/2 < a <= b < d+u/2 put every possible x inside
the nearest-rounding cell of d. Strictness removes any tie convention.
If also b<d, then x<=b<d. Therefore d cannot be a lower bound on x,
although it is a valid rounded display. All comparisons are exact
rational comparisons and need no floating-point square root or integral.

For d2 take d=499/100 and u=1/100; for 016 take d=17864253/2500000
and u=1/10000000. Parse a ball [c +/- e] as [c-e,c+e], with e>=0.
The lower endpoint of the certified lower ball and upper endpoint of the
certified upper ball contain d2 G0. For 016 use the accepted exact rational
endpoints, and compare them with the previously accepted T4-467 record.
The checker verifies the displayed strings at each frozen row, both
rounding inequalities, b<d, and every exact defect endpoint in N4-439.
The 016 example alone refutes the universal heading under the independently
accepted T4-467 premises. The d2 examples agree with the accepted N4-024
certificate. No stronger analytic premise is inferred from file hashes.

## Repair and scope

Use “residual value or bound” as the column heading. Add:
“Finite decimal entries without an inequality sign or an explicit enclosing
interval are rounded summaries of their cited certificates. They are not
directed bounds. Ratios use the exact underlying bounds and thresholds.”

Explicit inequalities must continue to be interpreted as directed claims.
A display convention cannot license an incorrect explicit inequality.
The repair changes no numerical certificate, ratio, candidate verdict or
existence conclusion. The residuals and all underlying calculations were
fixed before the freeze. Only exact comparisons of those records occur
here. The proof is written before the independent checker. Peer code is
read as inactive evidence and is never executed. The complete 017 upper
norm and all unsupplied inverse conditions remain OPEN.
