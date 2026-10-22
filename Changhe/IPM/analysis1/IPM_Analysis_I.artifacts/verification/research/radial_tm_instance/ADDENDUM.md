# Implementation clarifications after the initial review

The initial actual Claude Opus 5.5 review at 2026-10-21T02:23:24Z accepted
this as a sufficient finite criterion. The following details govern its
implementation and narrow several statements in that review.

1. Every integer power is evaluated with Python's exact integer convention,
including 0^0=1. In particular the homogeneous j=0 term is one. For
lambda=0 and j>=k+1 the independent exact identity is
T_(j,k)(0)=2^(j-k-1)/(j (j-k-1)!). This follows by integrating
exp(2v)v^k directly. The review's proposed expanded expression was not
unambiguous; this exact identity is used for the assertions.

2. The F box is precisely the reconstructed frozen producer's F box for
this cell. The topic69 rational audit proves that this box contains the
exact sparse modal image of its input T box. Our new propagation test
quantifies over every F in this larger box. It therefore does not require
that a new F box contain the producer box, as the review suggested: the
boxes are identical. Neither propagation engine imports the producer's
radial arithmetic. Their independence is in solving the ODE and bounding
its error, not in obtaining an untrusted source box. The original T and
A/B membership obligations remain separate.

3. All three producer modules are pinned: cert_flow.py, cert_resid.py,
and midrad.py. The scalar archive, its checker, its checks, and the
producer input NPZ are pinned. Candidate reconstruction records the actual
Python, NumPy, python-flint and mpmath versions. It is a finite assertion
about this runtime, not a universal proof of NumPy arithmetic.

4. The exact adjacent partition endpoints come from the partition JSON.
For every selected cell the code checks 0<t_(i+1)-t_i<=h, common point
inclusion in tb, and E inclusion at the same t_i. Topic75 already checks
all adjacent partition points; this local check repeats what is needed.
Whole partition coverage still requires that all cells be accepted.

5. The review says the producer's coefficients are exact Taylor
coefficient enclosures. This is a conclusion sought by the new test,
not an assumption we accept from inspection. Any failed coefficient or
remainder comparison remains OPEN. A floating display of a failed ratio
is only diagnostic; each verdict uses directed or exact comparisons.
