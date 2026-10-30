# Candidate016 report display versus the frozen numerical record

## Statement and inputs

This is a transcription audit. It makes no assumption that the numerical
record is a valid certificate. The two frozen sources are
source/N3_NOTES_1222.md, SHA256
553d2e2b9aa367fcc670f86d8720de4a9e046e4c00b6fcf7475f9d0ee542c38b,
and source/N3_probe.json, SHA256
e71575779cd09d4c06bb438fdae06b9c1e6b43d63bb99e7263f1db8040a44f82.
Both concern exact candidate016 with coefficient SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
The notes'12:15 summary table does not faithfully transcribe eleven
scientific-notation values from this record. Its two frozen-vector
distance floors are overstated by factors about100000.

## Definitions and complete argument

An Arb display [x +/- r] denotes the real interval[x-r,x+r]. In the
following table, the second column is the literal report entry; the third
is the record's center rounded for readable comparison. These third-column
numbers are approximate descriptions, not new interval endpoints.

| Probe and field | Literal summary entry | Record center, approximately |
|---|---|---|
| frozen n7, absolute pairing I |1.164936965445|1.164936965446e-7|
| frozen n7, gradient bound H |3.840026800|3.8400268e-5|
| frozen n7, distance root m |3.14826565878395|3.148265658784e-5|
| frozen n1, absolute pairing I |1.616723147236|1.616723147236e-8|
| frozen n1, coefficient norm C |6.400387888829|6.400387888830e-5|
| frozen n1, gradient bound H |5.212818800|5.2128188e-5|
| frozen n1, distance root m |9.25537084376950|9.255370843770e-5|
| (21,522), absolute pairing I |3.802147645708|3.802147645708e-6|
| (23,2400), absolute pairing I |1.873293416406|1.873293416407e-6|
| (19,1800), absolute pairing I |3.407662337804|3.407662337804e-6|
| (1,2048), absolute pairing I |3.998274699380|3.998274699380e-7|

Read pairing_abs, C, H_upper and radius from the JSON's six probe rows.
Each third-column value follows by retaining its displayed exponent.
For example, the n7 radius lies in the displayed interval with center
3.14826565878395482553489687525e-5 and radius3.09e-36, hence strictly
between0.00003148 and0.00003149. The literal report value3.14826565878395
is greater than3 and so is outside that interval. The n1 radius similarly
lies between0.00009255 and0.00009256, whereas its printed table entry
exceeds9. Their ratios to the retained centers are approximately10^5.
For every other row the printed mantissa is the record's leading
mantissa with its nonzero negative decimal exponent removed. The
record's displayed uncertainty is many orders of magnitude smaller
than this difference. Thus all eleven discrepancies are transcription
errors. This argument requires no quadrature or numerical execution.

The notes'11:17 section already prints the correct scientific notation
for the first three probes. The later12:15 table needs repair. In prose,
the weak inequality bounds ||h||_2 for an exact density rho_bar+h with
the same c, subject to its specified canonical velocity and regularity
hypotheses. It does not bound a distance from the residual F to that
density. The JSON's repeated phrase 'distance from F to any exact
solution rho+h' should be corrected on that point as well.

## Scope and evidence

The discrepancy verdict is REFUTED for faithful transcription of the
12:15 table, CONFIRMED for the eleven corrections above. Validity of the
six actual weak calculations remains separate. Three held-out values
can be checked against the earlier independent N4 records; the frozen
vectors and first-mode2048 record are not certified by this inspection.
No source file outside this lane was changed. The frozen inputs and
this complete argument are the verification evidence.
