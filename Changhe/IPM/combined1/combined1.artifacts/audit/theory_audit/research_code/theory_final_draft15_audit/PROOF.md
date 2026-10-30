# Audit of THEORY_FINAL draft15

## Scope and dependencies

This audits every change from the frozen draft12 through draft15, not
only the latest edit. The full diff is in source/changes.diff. Unchanged
claims keep their earlier audits; no fresh global proof is asserted.
The exact source hash and arithmetic results are recorded in verification/.
The prior audit is ../theory_final_h12_audit/PROOF.md, T4-328 to330.

## 1. Accepted repairs

The global exponent convention is e=1-l delta-2q. The nonautomatic L2
conditions are now (2,0),(3,0),(4,0), correctly excluding the automatic
leading term. The seven negative Sobolev conditions are enumerated
correctly. The forced-tail summary states the needed reference growth
bounds and the new correction k to R+eta, including H_q2(k)<infinity.
The total correction is h=eta+k. These repairs resolve the substantive
defects recorded in328and329.

The cutoff radius criterion is now symbolic and exact, and its numerical
value is labeled FLOAT. The residual tradeoff is stated only for this
cutoff family. The stale request to test010 is removed, and its completed
dyadic exclusion is cited. The text distinguishes a smaller finite set of
necessary probe bounds from a bound on the actual solution distance or
an optimization infimum. The changed table uses the already confirmed017
n23 floor, and all42 ratios remain conservative by exact arithmetic.
The valid newer017 n19 floor of331 is an update still to be incorporated.

## 2. Remaining error in the second cutoff description

The sentence saying that both cutoffs change the (5,1) residual coefficient
is false. Put q1=-1-4delta, q2=1-9delta and q3=-1-5delta. The first cutoff
has density and velocity of degree q1. Its cross terms with the leading
reference have degree q1-delta=q3 and can change that coefficient.
The second cutoff has degree q2. Its only linear contribution is atq2;
its mixed terms have degree at most q2-delta<q3, and its self term has
degree2q2-1<q3. Thus it cannot change theq3 coefficient. It preserves
the (5,1) coefficient after the first cutoff. The source theorem324
states these inequalities correctly. Its general construction is still
OPEN independent review; correcting this report sentence does not accept
that new theorem prematurely.

## 3. Status updates and limits

The second314 review has been accepted in333, with its new norm and
endpoint-sector conclusions confirmed in334.322 is accepted through332.
The stronger017 witness is accepted through331.335 is a new OPEN
endpoint theorem, not a proved result to add to the draft. The no-closure
statement and all registered scalar/graded exclusions are unchanged.
Dyadic and incomplete localized routes retain their separately stated
scope. The new correction above changes neither any certified candidate
coefficient nor an exclusion verdict.
