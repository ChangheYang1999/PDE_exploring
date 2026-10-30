# Acceptance of the profile-specific limiting velocity theorem

## Statement and notation

Let -5<q<-3. Let h be a real C1 function on R2, even in x and odd in y,
and suppose

 H=max(sup (1+r)^(-q)|h|, sup (1+r)^(1-q)|grad h|)<infinity.

Use the canonical velocity U[h]=(partial_xy,-partial_xx)Delta^(-1)h,
including the local term (0,-h/2). Its nonlocal kernel is
K(X)=(-xy,(x^2-y^2)/2)/(pi r^4), and M=integral Xh(X)dX is absolutely
convergent. Suppose r^(-q)h(r e_theta) tends uniformly to a finite odd
sine polynomial b(theta). Put p=q+2 and

 B(theta)=sum_n b_n sin(n theta)/(p^2-n^2),
 V_q[b](theta)=(partial_xy,-partial_xx)[r^p B(theta)] at r=1.

Then r^(-q)(U[h](r e_theta)+DK(r e_theta)M) tends uniformly to V_q[b].
For each of the exact reference data sets 007, 013 and 014 frozen by
T4-402, if b=(A+tP)/(4c) for some real t and
c=4076476460239181/2251799813685248, q=1/c-4, then

 limsup_(r->infinity) sup_theta r^(-q)|U[h]+DK M|
 <= (583/1000) H.                                           (1)

The original full statement, formula (9), exact data manifest and
certificate are frozen in source/original_PROOF.md,
source/original_manifest.json and source/original_result.json. This
acceptance concerns their exact references, not arbitrary angular data.

## Argument and independent checks

Central oddness folds the compensated integral into the kernel
[K(e-Z)-K(e+Z)]/2+DK(e)Z. This is O(|Z|^3) at the origin and O(|Z|)
at infinity. Against the bound |R^(-q)h(RZ)|<=H|Z|^q, both regions
are uniformly integrable exactly when q>-5 and q<-3, respectively.
Near either singular point e or -e, subtract the local value. The
uniform gradient bound H|Z|^(q-1) makes the principal-value contribution
from a disk of radius eta at most a fixed constant times eta. On the
remaining compact set use uniform convergence. The contact term
converges as well. This proves existence of a uniform limit depending
only on b, without differentiating an uncontrolled asymptotic error.

Identify that limit by using a smooth radial cutoff of r^q b. The
canonical radial Green formula gives the homogeneous potential
r^p B and a harmonic remainder in each sine mode. In mode one, the
remainder is exactly the dipole potential -m sin(theta)/(2pi r),
whose velocity cancels DK M. In modes n>=3, its differentiated
remainder is O(r^(-n-2))=o(r^q). Thus the limit is V_q[b] above.

The rescaled gradient bound passes to the limit in distributions
and gives q^2 b^2+(b')^2<=H^2 pointwise. Let f1=A, f2=P,
z=(1,t), and S_ij=(1/2)sum_n(q^2+n^2)f_i,n f_j,n. Then
z^T S z<=(4cH)^2. If W(theta) is the two-column matrix with columns
V_q[A], V_q[P], positive definiteness of S implies

 |Wz|^2 <= (z^T S z) trace(S^(-1)W^T W).

The exact cosine coefficients T_k of the trace satisfy
sum_k|T_k|<(583/1000)^2 for all three references. This proves (1).

The independent review source/review.md recomputes the differentiated
Cartesian identity on enough rational unit-circle points to determine
each trigonometric polynomial of degree n+2. It checks the Green tail
and first-mode test, and independently obtains all three Gram matrices
and trace cosine polynomials using complex exponential coefficients.
The review's 15 analytic algebra checks and 21 exact data checks pass.
The acceptance checker binds its source and output hashes, checks
those booleans, rechecks each exact l1 value against the original
certificate and the rational square, and binds its dependent 375 result.
No reviewer code is executed in this acceptance.

## Verdict and scope

CONFIRMED: all analytic statements and the finite rational certificate
of T4-402 are now independently AUDITED. The independent review's
additional angular upper enclosures and its FLOAT pointwise-profile
optimizations are separate results and are not needed for this verdict.
There is still no finite radius or remainder in (1).

Section 4 of the review analyzes a necessary cutoff-radius test, not
the full radial integral. Its positive room below the cutoff threshold
does not prove that coefficient 0.583 can pass the full CI351 test.
The stronger retained radial shape must be checked separately. Neither
this acceptance nor that necessary test proves existence, an inverse,
a bound on H, or any new candidate exclusion. Additional stationary
hypotheses are needed to identify b with (A+tP)/(4c).

Collaboration uses the existing independent theory lane configured for
Claude Opus5.5; the actual provider identity is not observable here.
