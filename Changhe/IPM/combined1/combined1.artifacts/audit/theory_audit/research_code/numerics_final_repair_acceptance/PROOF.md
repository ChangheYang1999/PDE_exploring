# Acceptance of the numerical report repairs and a penalty-scaling caution

## Scope and dependencies

This audits the eight requests in T4 handoff174 against the frozen numerical
report in source/NUMERICS_FINAL.md. It accepts the repaired mathematical
scope, not every new FLOAT number or the behavior of a future optimizer.
The exact radius proof and interval evidence remain in T4-374. The source
hash, capture time and dependency hashes are in verification/manifest.json.

## The eight repairs

1. The summary and Sections9.4,9.5 now distinguish the unrestricted sharpw
L2 ceiling2.84957773827575...e-6 from2.839272409e-6, which requires globally
H2 corrections supported in20<=r<=32 with sine modes at least19. The
conservative unrestricted number2.8496e-6 and factor above515.9 for016
are valid. These follow by maximizing(mu t-Ct^3)/b and dividing by1024;
T4-374 gives the exact constants and the additional annular estimate.

2. The017 n23 floor is now0.001068502321536437, below the certified root.
Its strict lower-bound direction is correct. The stronger n19 certificate
is separately retained.

3. The point paragraphs now use the per-pair007/009 sharpw ratios4.558
and3.048 and distinguish the differing radii. The original graded ratios
are placed between4 and5 and between2 and3. The removed universal orders
of magnitude and common-radius claim are no longer used.

4. The015 result is now a twelve-step trial observation. Its cause is
OPEN. Section9.3 no longer infers a causal cost for(B-L2) from trials
with different starting points, objectives and weights.

5. The020 history now agrees with its displayed comparisons:38.16-fold
for the small-radius pair,26.10 percent at(23,1200) against017, and the
58 percent exception at(31,2400) against016. These are arithmetic on
reported FLOAT values, not certified continuum changes.

6. The report now calls1024G0 a binding necessary contribution rather
than the dominant sharpw energy. The ratio to the certified X lower
bound is below0.51, as in T4-374.

7. Section7b explicitly says the08:33 and08:47 declarations postdate
the08:32 launch. The older public25-probe register and the separate
analytic span theorem are the evidence that remains available.

8. N4-268 and N4-273 are correctly CONFIRMED through366 and367, and the
017 cover remains OPEN pending complete independent replay. The inverse
remains OPEN. However the report header still says this version was
written at09:08Z, even though it includes the10:05:34Z snapshot and later
repairs. The requested current revision time was not applied in these
frozen bytes. No historical writing time is inferred from the file's
modification time. Use an actual current timestamp on the next revision.

Thus requests1-7 and the mathematical portion of8 are CONFIRMED. The
claim that all eight requests are fully applied is REFUTED by the stale
header. No candidate verdict changes on account of this textual repair.

## New021 explanation: energy size is not sensitivity

The new021 text calls its14 penalty rows inert because a term of size25
is small relative to an objective of size1.3e7, and therefore calls the
run a continuation of020. That inference is unsupported without a matched
run or a sensitivity calculation. The observation that the displayed
row values did not decrease is valid as a trial report; the claimed cause
and the equivalence to dropping those rows remain OPEN.

Here is a complete scalar counterexample to the general inference.
Let B(x)=10^7+(x-1)^2 and P_M(x)=25(1+Mx)^2, M>0. At x=0 the penalty
value is25 while B is10000001. Yet B'(0)=-2 and P_M'(0)=50M. The
unpenalized unique minimizer is1, while the positive quadratic B+P_M
has unique minimizer

    x_M=(1-25M)/(1+25M^2).

This follows by solving(B+P_M)'=2(x-1)+50M(1+Mx)=0; its second
derivative is2+50M^2>0. As M tends to infinity, x_M tends to0 from below,
so the minimizer change tends to1 despite the arbitrarily small
relative initial energy contribution obtained by enlarging the constant
in B. Value fractions do not bound gradients, Hessians or parameter
steps. The campaign's reported scalar penalty value therefore cannot
establish inertness. This counterexample says nothing about the actual
unmeasured Jacobian of021 and does not prove that its rows mattered.

## Status

CONFIRMED repaired bounds and scopes described above. OPEN actual causal
impact of021's14 rows. REFUTED the inference from energy size alone and
the claim that the current revision timestamp was already corrected.
No additional computation or foreign code execution is needed.
