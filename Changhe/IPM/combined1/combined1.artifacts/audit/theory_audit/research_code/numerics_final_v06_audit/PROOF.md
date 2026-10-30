# Audit of the numerical report after theory_v06

## Scope and frozen claims

The source is the complete 197-line NUMERICS_FINAL revision with SHA256
2aba92677db6a2360b76562c29ab485d1edc1d2834f9fa6c93baedeb2d1945fb,
frozen in the preceding audit at 2026-10-29T09:27:02.390996Z. Its header
says 09:08, but its content includes later results and the 09:19 theory
ACK. This is a review of conclusions and certificate use. It does not
certify every FLOAT entry or an unregistered candidate.

Dependencies are the accepted point certificates for007 and009,
T4-320's017 n23 certificate, T4-278's annular estimate, T4-373's
unrestricted scalar envelope, and the elementary counterexamples of
T4-340. Each dependency used by the checker is copied and hash-bound.
The proof below states the inference limitations independently.

## 1. Accepted repairs and current exclusion scope

The report now correctly distinguishes ten nonautomatic canceled
sectors from the automatic leading sector, and old h from global l=h+1.
The004 exception is retained. The principal statement that every
registered scalar ball and original graded box through020 is excluded,
except the FLOAT comparison011, agrees with the accepted certificates.
The dyadic exclusions have the narrower state131,d2,007 to010 scope.
The localized route has no complete high inverse. These conclusions
are CONFIRMED; none of the corrections below reverses an exclusion.

The distinctions between exact candidate coefficients and their
binary64 evaluation, calibration and a quadrature theorem, design
pairings and certified necessary tests, feasible least-squares values
and a positive span floor, and coefficient conditioning and physical
conditioning are now correct in the corresponding revised paragraphs.
A certified pairing with a probe phi in an angular band B gives
||Pi_B F||2 >= |<F,phi>|/||phi||2 by orthogonality and Cauchy-Schwarz.
The corrected report properly retains this lower bound while denying
an upper bound or an inference that mass increased between trials.

## 2. Annular and unrestricted correction budgets

Let X_s be the sharpw norm, with X_s(h)>=1024||h||2. Its positive
scalar margin is

    mu-C s-b R/sqrt(s)>0,
    mu=97/250, C=397, b=8/5, X_s(h)<=R.

Writing t=sqrt(s), every admissible radius is smaller than
(mu t-C t^3)/b. Its maximum is

    R_*=(2mu/(3b))sqrt(mu/(3C)).

Therefore every correction in this parameter family has

    ||h||2 < R_*/1024 = 2.84957773827575...e-6.         (1)

T4-278 improves the denominator only under additional hypotheses:
h is globally H2, supported in20<=r<=32 and has only sine frequencies
n>=19. Put q=361/1024 and

    A^2=1601^(4/5)q^2+2^15 q+2^20.

Angular Poincare, ||Dh||2^2 <= ||h||2||D2h||2 and the radial weight
minimum on the support give E(h)>=A||h||2. The audited comparison
X_s(h)>=(1-48s/25)E(h), for0<s<=1/1024, then gives the specialized
bound

    ||h||2 < R_*/[(1-48/(25*1024))A]
            < 2.839272409e-6.                        (2)

The source's summary and sections9.4,9.5 apply(2) to the unrestricted
family. This deduction is REFUTED: residual concentration does not
supply support or angular restrictions on an unknown correction. Use
(1), conservatively2.8496e-6, for that family. The016 accepted distance
floor gives a ratio greater than515.9, about516, using this ceiling;
518 is the specialized comparison and needs its extra hypotheses.

## 3. Directed rounding and point-gap comparisons

The accepted017 n23,K2400 result encloses the positive root of the
necessary inequality |I|<=D beta+H beta^2 at

    beta = 0.001068502321536438039569901431... .

Its stored strict lower bound is1068502321536437/10^18. The table's
claim of a certified floor greater than0.001068502322 AT THIS PROBE
rounds upward past the enclosed root and is not supplied by this
certificate. Replace it by0.001068502321536437 or a downward rounding.
The stronger n19 bound exceeds both numbers, so this is a certificate
attribution and rounding defect, not a reversal of the017 distance
exclusion or a claim that the full distance is below the printed value.

The universal phrase '2 to4 orders of magnitude in the point test'
with radii2^-14 to2^-16 does not describe the six scalar balls and the
original graded family. For example, the sharpw ball has radius
1351/10^6, and sharp has735/10^6, both larger than2^-14. At the accepted
point X=(1/10,73/100), the ratios of |F(X)| to the sharpw necessary
point upper bound are between4 and5 for007 and between3 and4 for009.
The corresponding original graded uniform ratios are between4 and5,
and between2 and3. These are rigorous positive gaps, not factors100
to10000. In a point estimate A n+B n^2 with A,B>=0, if t=n_nec/n>1,
then (A t n+B t^2 n^2)/(A n+B n^2)>=t. Thus the necessary-radius factor
at this point is no larger than that displayed residual ratio. Other
points require their own certificates. Replace the blanket statement
by the actual tested radii and per-pair gaps; retain all valid exclusions.

## 4. Trial comparisons do not identify causes or an optimum

The statement that quotient015 changed little in twelve steps is a
trial observation. The further sentence 'redundancy is not the cause
of the immobility' does not follow: removing a coordinate kernel does
not remove small positive singular values or damping dependence.
For example, minimize |epsilon x-1|^2 with epsilon>0. The density map
x -> epsilon x is injective. A damped step from0 has physical output
epsilon^2/(epsilon^2+lambda), arbitrarily small when epsilon^2 is much
smaller than lambda, although the exact minimum is0. Adding and then
removing a redundant y coordinate changes none of this. This refutes
the causal deduction, while leaving the cause in these trials OPEN.

Similarly a finite comparison of objectives with different weights
and starts cannot determine the cost of imposing(B-L2). Even two
feasible values give only upper bounds on their own infima. A smooth
objective can agree with all finitely many measured values and be
changed on a disjoint open set by a smooth bump, changing its infimum.
Section6 correctly says the trials do not isolate the cost. Section9.3's
'costs a factor1 to3 in G0' should be removed or restricted to explicitly
named trial ratios. Failure of a Hilbert-Schmidt sufficient background
criterion does not prove failure of the actual low-operator coercivity.

The candidate020 discussion is internally inconsistent. Section4 now
records the(31,2400)exception up to58percent above016 and a small-radius
increase from3.8e-6 to1.45e-4, a factor about38.16. Section7 still says
10to20percent for K>=1200 and at most8fold at small radii. Even the
printed(23,1200) values3.43e-4 versus2.72e-4 give26.10percent, outside
10to20percent. These are arithmetic comparisons of reported FLOAT
values, not certified continuum ratios. The two prose summaries must
agree with the complete labeled table.

The term1024G0 is a binding necessary contribution to X(F), but it is
not most of the evaluated norm: for007 it is about385.73, while the
accepted lower bound X(F)>756.531263 gives its fraction below0.510.
The squared fraction is below0.261. Thus section9.2 should say the G0
necessary test alone already fails, rather than asserting dominance
of the registered forcing norms. We do not infer component locations
or full norm decompositions from this one comparison.

## 5. Exact angular quadrature: full tensors and components

Let chi=sum_(m=0)^M a_m(r)cos(2m theta), with smooth radial functions,
r>0, and define rho=-partial_y Delta chi, psi=partial_xy chi,
u=(-psi_y,psi_x), F=(cX+u).grad rho-rho. The polar Jacobian formula
shows that F has only odd sine frequencies up to d=4M+3: rho has
frequencies up to2M+1 and psi up to2M+2. No radial profile assumption
is needed for this frequency bound.

For ideal quadrant nodes theta_i=(i+1/2)pi/(2N), every cosine mode
cos(2q theta) with integer0<q<2N has zero quadrature sum. Indeed

    2sin(x/2)sum_i cos((i+1/2)x)=sin(Nx), x=q pi/N,

and the denominator is nonzero. Its exact integral is also zero.
Consequently N>=2M+2 integrates F^2 and (Delta F)^2 exactly in theta.
It also integrates the full gradient and Hessian Frobenius squares:

    |grad F|^2=F_r^2+r^-2 F_theta^2,
    |D2F|^2=F_rr^2+2(r^-1 F_rtheta-r^-2 F_theta)^2
                      +(r^-1 F_r+r^-2 F_thetatheta)^2.

The polar orthonormal components on the right have angular frequencies
at most d, so their squares have cosine indices q<=d<2N. The Hessian
formula follows by differentiating grad F in the polar orthonormal
frame; orthogonal conjugation preserves the Frobenius norm. Radial
weights do not change exactness. Thus the source's N>=2M+2 rule is
CONFIRMED for these rotation-invariant norms, including the ordered
Cartesian tensor convention in the theory.

An individual Cartesian derivative of order j can have frequency d+j.
The separately weighted component squares are covered instead by the
sufficient condition d+2<2N, or N>=2M+3. These distinct claims should
not be conflated. For the actual/proposed families with M=79, the
adopted N=180 satisfies both conditions, as N4-295 correctly proves.
Ideal angular exactness supplies no floating-evaluation, radial or
whole-plane remainder bound.

## 6. Provenance and status

The source's pre-registration heading says the declaration at08:33
preceded runs launched08:32. It did not. For021 to023 the coordinator
allows the older25-pair register, and analytic nonmembership in the
recorded objective span, as distinct held-out evidence. State those
actual facts. Do not turn the later declaration into an earlier one.
The prelaunch records for024 and025 have their own hashes and are
not challenged by this observation.

N4-268's complete-plane kappa upper bounds for016 and017 are now
CONFIRMED by T4-366, and N4-273's partition by T4-367. Their OPEN labels
are stale, but neither result supplies a global theta bound or a full
inverse. Exact far-field cancellation proves membership only in the
specified registered norms with the audited decay and remainder
conditions; it should not be read as membership in arbitrary new,
faster weighted-tail spaces. The new bases and trial runs likewise
need actual snapshot binding before a certificate applies.

## Verdict and verification

CONFIRMED the repaired exclusion scope and logical distinctions in
section1, the specialized annular theorem under its hypotheses, and
the exact angular rules in section5. REFUTED the unrestricted use of
the annular ceiling, the upward rounding at the specified017 probe,
the blanket point-gap and radius description, the stated causal
inferences from finite trials, and the inconsistent020 summaries.
The actual cause of the plateaus, optimum under(B-L2), later candidate
quality and every missing inverse or closure condition remain OPEN.

The checker imports exact parameter JSON and frozen accepted interval
outputs, verifies the source hashes and the numerical comparisons,
and checks the Hessian's orthogonal invariance symbolically. This is
not a rerun of the lengthy accepted candidate integrals. New angular
full-tensor sharpening is offered to N4 for independent review.
