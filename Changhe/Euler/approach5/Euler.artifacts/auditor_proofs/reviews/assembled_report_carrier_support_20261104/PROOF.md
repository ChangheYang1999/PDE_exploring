# Audit of the carrier-equilibrium pressure-support report addition

Status: complete mathematical transfer and structural audit of the exact snapshot below. Later revisions need a separate check.

## 1. Snapshot and transfer scope

The candidate report has SHA256 2007222fbbbfd5db928a31337f0fa8b2e90997f19573721b742524642ab37865, 1052237 bytes, and verdict cutoff A2775. Both coordinator copies agreed at capture. Its predecessor, 7888891b, was approved by A2775 through A2769.

The independently generated delta agrees with the coordinator's submitted delta apart from the two file labels. It contains four hunks. Every changed line was read. In the third hunk the sole change is a new Appendix A table row; the large unchanged context transfers from A2775. The other hunks update the timestamp, the approval summary and the history entry. The historical change was checked individually; no collective approval of historical appendices is asserted.

## 2. Mathematical content

The new row's part (a) is exactly the carrier-equilibrium translation of A2770. With A=cI-omega J, L=(1-c)I+omega J, B(a)=0 and q=U(a), set V(x)=U(a+x)-q and Q(x)=P(a+x)-P(a)-grad P(a).x. The original equation at a gives grad P(a)=-Lq, so the translated pair solves the same equation and has V(0)=grad Q(0)=0. This algebra is valid for every real c and omega. Under the stated positive semidefinite Hessian hypothesis, nonzero W implies omega^2|JW|^2>2|W|^2, while W=0 forces DU(a)=0.

Part (b) has the exact global hypotheses of A2771: U is C2, P is C1, c>0, the full equation holds on R3, and the actual pressure tangent plane supports P in a neighborhood of a carrier equilibrium. The translated pair satisfies the hypotheses of A2748. Therefore |omega|<=sqrt(2), or DU(a)=0 for arbitrary omega, gives a constant U=-Aa with grad P=-LU. If U decays, this constant vanishes; invertibility of A for c>0 then gives a=0 and P constant. Conversely a nonconstant profile under these hypotheses must have W nonzero and satisfy the strict angular inequality, since zero W would imply the already excluded zero derivative alternative.

Part (c) accurately records A2772. For phi=x^3-3xy^2, the harmonic-gradient velocity and the stated pressure solve the entire equation for every real c and omega. The line value is -(1+c)t^3-(9/2)t^4. If c differs from -1, choosing the sign of t to match 1+c makes it negative; when c=-1 it is negative at every nonzero t. The vanishing Hessian therefore cannot replace neighborhood support. This field grows quadratically, so it is not a decaying counterexample.

The row and its hypothesis cells keep local algebra, global rigidity, parameter ranges and decay consequences separate. The supporting-plane premise and derivative alternative are not established for an arbitrary decaying profile; A2773 remains OPEN. The summary cites A2775 at the correct predecessor cutoff and cites A2774 for its transfer. The new history entry accurately describes A2770-A2775.

## 3. Verification evidence and conclusion

The file checks parse all2775 verdicts through the cutoff without unknown or conflicting statuses. All221 explicit confirmation lists contain only CONFIRMED entries. All2364 distinct positive verdict references exist. The previously reviewed uses of A0 denote mathematical objects, not verdict numbers.

All nine Markdown tables pass, with581 data rows and599 total rows. No absolute local paths or em dashes occur. Four unchanged mathematical norm blocks have no table separator and are correctly omitted from table counting. The scripts perform standard-library file bookkeeping, not a mathematical experiment.

The delta preserves the independently proved results and their exact scope. Together with A2775, it supports cumulative approval of the candidate front matter, sections0-10 and AppendixA through A2775. The main arbitrary-helicity decaying-profile conjecture remains OPEN.
