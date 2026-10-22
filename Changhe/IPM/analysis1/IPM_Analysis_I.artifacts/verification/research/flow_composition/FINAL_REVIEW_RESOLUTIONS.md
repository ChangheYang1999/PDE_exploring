# Final review resolutions and direct width check

Written before the supplemental computation. This note is mandatory with
PROOF.md and ADDENDUM.md. It does not enlarge the nine-rectangle scope.
The completed actual Opus5.5 review accepts the restricted conditional
verdict and withdraws its centre-sliver objection.

The proposed check d >= (r-l)(355/113)/102400 is sufficient but unnecessary.
A failure of that stronger check cannot refute d >= (r-l)pi/102400.
Its rational upper bound is too coarse to decide widths rounded only a
few binary ulps above the true half-width. We instead prove a rational
upper bound from Machin's formula, and compare the stored dyadic d exactly.

For 0<x<1 the identity 1/(1+t^2)=sum_(j=0)^(N-1)(-t^2)^j
+(-t^2)^N/(1+t^2), integrated from0 to x, shows that arctan(x) lies
between the N-term sum and the sum including termN. Both endpoints are
rational for rational x. Use N=40 for x=1/5 and x=1/239. Four times the
first angle minus the second has tangent1: tan(2 arctan(1/5))=5/12,
tan(4 arctan(1/5))=120/119, and the subtraction formula gives1.
This angle lies in(0,pi/2): the elementary bounds x-x^3/3<arctan(x)<x
give a positive lower bound and an upper bound4/5<1<pi/2. Therefore
4 arctan(1/5)-arctan(1/239)=pi/4. Scaling the rational alternating bounds
by16 and-4 gives an exact rational interval for pi. This establishes the
width claim if its rational upper endpoint times(r-l)/102400 is <=d.
A fresh Arb512 enclosure provides a separate interval comparison.

The original ADDENDUM.md was already hashed in addendum_record.json at
11:23:52Z. This was after the first exact cell0 run but before the iv cell0
and both later-cell runs. Its corrections concern mathematical fixed
centres and notation, not changed arithmetic. We retain the real chronology
rather than claiming it was recorded before all runs. PROOF.md preceded
all new computations. Every final file, including this addendum and its
record, will be pinned in the final verdict.

The source semantics to be checked are exact expressions from the frozen
cert_flow.py: line164 defines SP=sum cos*P,SC=sum C*R,SS=sum S*R;
lines174-177 define s=c_l-SP,v2=s+SC,v1=s-SS; lines178-182 define
T=-(1+c_l)-a SS+b SC+mu s. The returned s,v2y,v1x,T0 endpoints in
line183 are respectively these four expressions. AST and exact source
excerpts will bind the names without trusting source arithmetic. The
parameter tuple a=129/20,b=307/100 is in line30. Each current candidate
range was separately contained by both independent reference methods.

Finally inspect all saved exact margins again and record the minimum with
its method, radial cell, angular index/node, function and endpoint. This
is a record audit, not a third arithmetic engine. Physical canonical
radial membership, full rectangle coverage and both endpoints remain OPEN.
