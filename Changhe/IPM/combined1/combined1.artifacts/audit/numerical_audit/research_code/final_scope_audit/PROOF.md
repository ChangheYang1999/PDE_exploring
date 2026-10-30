# Selected final-report claims: certified norms and comparison scope

## Statement and exact objects

This is a review of selected numerical statements in the frozen coordinator
report source/the joint closure report_1357_v01.md. It is not a review of every theorem
or every claim in that report. The source hash and each supporting result
are recorded in verification/PREPARE_v01.json before the finite checker.
The source header says 13:49Z, while its answer sections say 13:57Z. These
are document labels; the independent copy time is recorded separately.

For candidate C1-N1-007-d2w-j7-e2bal, raw SHA256
ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21,
use c=4076476460239181/2251799813685248 and the canonical residual
F=(cX+U[rho]).grad rho-rho on R^2. Norms use Lebesgue measure and the
unitary Fourier transform. Put J=(1-Delta)^(1/2), Lambda=(-Delta)^(1/2),
omega=(1+4|X|^2)^(2/5), and

 G0=||F||2, G1=||DF||2, P2=||omega D^2 F||2,
 Q3=||omega D^3 F||2, H=||Lambda^(-1) F||2,
 E^2=P2^2+2^14 G1^2+2^18 G0^2+2^18(20/21)H^2,
 N_s(F)=E(J^s F),
 X_(s,w)(F)^2=||omega D^2 J^s F||2^2
                 +w1||D J^s F||2^2+w2||J^s F||2^2.

Derivatives have the complete ordered Cartesian tensor norm. Assume the
already accepted numerical certificates N4-249, N4-252 and N4-180 with
exactly the candidate, source bindings and scope of their standalone
proofs. Then H is certified in the coarse strict interval

 0.6355243760000922 < H < 0.6355322685705510.

There are two-sided certified N_s enclosures at s=1/262144,
1/268435456,1/65536 and1/8192, with the exact thresholds respectively
1/1572864,1/2684354560,3/327680 and5289/50000000. Their accepted
rational outward endpoints are read from N4-252. Therefore a current
statement that this H enclosure is still running, or that only lower
N_s bounds are certified, conflicts with the accepted evidence. This
statement does not promote every finer digit of the own Green formula.

For candidate C1-N1-016-legqs25-quot013, raw SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42,
N4-374 and the reciprocal T4-451/N4-380 give the sharpw sufficient-test
ratio a strict lower bound of3542234. N4-180 gives007 the strict lower
factor3596535.57. Comparing those lower bounds cannot order the actual
ratios or the distances to solutions. In particular the wording
"smallest certified forcing-norm ratio" must specify a comparison set
and distinguish an actual enclosing interval from a quoted lower factor.
This review does not certify candidate016 P2 or H.

## Argument and numerical dependencies

N4-249 compares an independent complete160-mode Green formula with the
peer's31 Galerkin modes and129-mode Hardy tail, proving the stated coarse
H enclosure under its exact-source and historical-code qualifications.
That already accepted result, not new integration here, supplies H.

For completeness the comparison used by N4-252 is, for0<s<1/34,

 (1-34s)E <= N_s(F)
           <= E^(1-s)(2Q3^2+16410E^2)^(s/2)+34sE.

Its source proof bounds the Bessel commutator with the globally Lipschitz
weight and uses Hilbert-space Fourier interpolation. All five component
intervals are independently accepted. Both comparison sides increase in
positive E and the upper side increases in Q3. Substitution of lower and
upper component endpoints thus gives a two-sided enclosure. The current
check verifies every stored rational outward endpoint against the saved
comparison balls, rather than repeating the component integrations or
claiming a new proof of the source commutator. All four exact source
thresholds are retained; a binary64 display is not substituted.

The ordering issue is elementary. For positive a,b, lower information
b>L_b and a>L_a with L_b<L_a admits either order. In the present sharpw
scale, the saved007 enclosure contains757 and the known016 lower
comparison is below750. The pairs(a,b)=(757,750) and(757,800) satisfy
these scalar enclosures and lower comparisons, but have opposite orders.
These are counterexamples to a logical inference from the quoted scalar
bounds, not asserted realizations of two IPM residuals. A separate lower
bound for b above a certified upper bound for a could prove an ordering;
that stronger test must use accepted inputs and is not supplied here.

Finally, a sufficient condition S implies existence E. Failure of S
alone does not imply failure of E. N4-374/N4-380 and N4-252 concern these
sufficient tests. The accepted weak and point certificates prove their
own correction-ball exclusions under their stated hypotheses. The
present review preserves that distinction and the separate dyadic scope.

## Finite check and scope

Bind the frozen report, the own accepted results and their explicitly
recorded direct local input hashes before arithmetic. Check the exact
source passages and record their line numbers. Check the H enclosure
flags and strict coarse endpoints, all four N_s outer endpoints and
thresholds, the two distinct sharpw lower factors, and the logical scalar
counterassignments. Compare the accepted380 result with its own original
374 and accepted373 inputs. Rehash all bindings afterwards.

Verdicts apply to the specified passages of this frozen draft. The check
is not a complete report review, an integral reproduction, an inverse
certificate, a candidate ranking or an existence proof. A later repaired
report must be assessed by its new hash. Current proof and input equality
do not retrospectively observe historical process loading.
