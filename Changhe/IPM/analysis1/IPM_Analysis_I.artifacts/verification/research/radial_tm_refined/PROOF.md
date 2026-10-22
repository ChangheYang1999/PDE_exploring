# Complete middle-region radial Taylor-model criterion with endpoint refinement

Status at proof writing: an exhaustive verifier is being constructed.
No full computation or canonical-data conclusion is asserted. This proof
precedes its implementation. The independently checked three-cell result
in topic93 supplies useful tests, not coverage of the other cells.

## 1. Exact finite statement and dependencies

There are 7809 adjacent middle cells with exact rational log-radius
endpoints t_i<t_(i+1), as specified in the frozen partition JSON. On cell i
put u=t-t_i. Let h_i be the positive binary64 number in the scalar archive,
interpreted exactly, with t_(i+1)-t_i<=h_i and 522h_i<1. Let E_i lie in its
positive scalar interval. For n=1,...,261, take constant real input values
A_n, B_n and F_(n,k), k=0,...,7, in the exact midpoint-radius boxes produced
from the frozen input arrays. Write Z=E_i^2 and

 f_n(u)=Z exp(2u) sum_(k=0)^7 F_(n,k)u^k,
 lambda_+=2n-2, lambda_-=-2n-2,
 q_+'=lambda_+q_+-f_n, q_+(0)=B_n/Z,
 q_-'=lambda_-q_-+f_n, q_-(0)=A_n/Z,
 P_n=(q_++q_-)/2, R_n=(q_+-q_-)/2.                    (1)

All these solutions are entire functions of u for each admitted input.
Every input interval in this statement is an independent box constraint;
allowing independent choices can enlarge the true correlated family.

The producer exports degree12 polynomials with coefficient intervals and
nonnegative constant remainder budgets for P_n and R_n. The finite claim
is that each such Taylor model encloses (1) on [0,h_i], for every input
choice, on every cell and every mode. It requires precisely

 7809*261*13*2 = 52,991,874 coefficient containments per method,
 7809*261*2 = 4,076,298 remainder containments per method.       (2)

Two independently coded interval methods must each prove all of these
containments. A failed sufficient bound leaves the claim OPEN. In
particular a large upper bound alone does not refute the candidate.
No candidate radius or remainder may be increased to obtain acceptance.

The dependencies are topic69's exact polar identities and modal maps,
topic75's common exact-point scalar data, topic81's ODE identification,
and topic93's independently reconstructed finite-family criterion and its
mandatory refinements. They do not supply the missing exhaustive run.
Topics98 and99 separately address canonical A/B and T membership. A
canonical-trial conclusion is conditional on those complete checks and
all the same-point and same-array linkage checks below. This theorem
alone contains no angular assembly or full flow-field inequalities.

## 2. Exact modal forcing linkage

Write the exact input polynomial factor as

 a(u,theta)=sum_(m=0)^259 sum_(k=0)^7 a_(m,k)u^k cos(2m theta).

Then rho=r^3 cos(theta)^2 sin(theta) a. The elementary identity

 cos(theta)^2 sin(theta)cos(2m theta)
 =[sin((1+2m)theta)+sin((1-2m)theta)
   +sin((3+2m)theta)+sin((3-2m)theta)]/8

is valid also when frequencies repeat or are negative. A negative
frequency contributes with negative sign; all repetitions are collected.
Let H_j be the resulting coefficient of sin((2j+1)theta). Directly using
partial_x=cos(theta)partial_r-sin(theta)partial_theta/r gives

 F_n=[(4-2n)H_(n-1)+(4+2n)H_n+H'_(n-1)+H'_n]/2.       (3)

Here the prime differentiates u. Thus every F_(n,k) is a rational linear
functional of the input a_(m,k) and a_(m,k+1), with denominator dividing16.
Its whole-box image is found by collecting each repeated input coefficient
before taking absolute values: if the weights are w_l, midpoint entries
m_l and radii r_l>=0, its image is

 [sum w_l m_l-sum |w_l|r_l, sum w_l m_l+sum |w_l|r_l].   (4)

Each floating input is an exact dyadic rational. Every finite binary64
number is an integer multiple of eta=2^(-1074). Hence (4), including
comparison with the actual freshly generated F box, can be checked using
signed integers after multiplying by16/eta. The new checker must verify
all 16,305,192 forcing coefficients on its actual runtime arrays. Identical
source files alone are not used as a substitute for this linkage.

## 3. First coefficient method: exact integral weights

For j>=k+1 define the integer

 Q_(j,k)(lambda)=sum_(v=0)^(j-k-1)
        [(k+v)!/v!] lambda^(j-k-1-v)2^v,                (5)

and put Q_(j,k)=0 otherwise. Expand the exponential factors in
integral_0^u exp(lambda(u-v))exp(2v)v^k dv. Uniform absolute convergence
on every compact interval permits termwise integration. The beta integral

 integral_0^u (u-v)^a v^(k+b) dv
 =a!(k+b)! u^(a+k+b+1)/(a+k+b+1)!

shows that its degree-j Taylor coefficient is Q_(j,k)/j!.
Consequently the exact coefficients of (1) are

 P_j=[B lambda_+^j+A lambda_-^j]/(2j! Z)
      +Z sum_k F_k[Q_(j,k)(lambda_-)-Q_(j,k)(lambda_+)]/(2j!),
 R_j=[B lambda_+^j-A lambda_-^j]/(2j! Z)
      -Z sum_k F_k[Q_(j,k)(lambda_-)+Q_(j,k)(lambda_+)]/(2j!). (6)

Here and below 0^0=1, in particular at j=0. At lambda=0, the single
nonzero summand in (5) yields Q_(j,k)(0)=(j-1)!2^(j-k-1)/(j-k-1)!,
which also follows by integrating exp(2v)v^k directly.

The first method constructs (5) with exact integer arithmetic. For every
j,n it computes exact dyadic midpoint-radius hulls of the A/B linear
form and the F linear form in (6), combining repeated F_k first. Divide
by the exact positive integer2j!, and evaluate U/Z+ZV with Arb directed
balls. The full positive E interval is squared to bound Z. The two
occurrences of Z may be treated independently; this only enlarges the
result. The original resulting ball is tested first. If its containment fails,
the endpoint refinement in section 8 is permitted. Either accepted entire
enclosure must lie inside the exact candidate interval. Only checking
the midpoint is insufficient.

Exact endpoint comparisons are possible without rounding the target:
if an independent endpoint is m2^e and the target is c eta, compare
m2^(e+1074) with c by shifting one integer side. This covers arbitrarily
small values and subnormals. Nonfinite arithmetic is a failure, not an
accepted infinity. No assumption about BLAS summation is used here.

## 4. Second coefficient method: differentiated ODE on a formal basis

The second method does not use the sum (5). Represent the homogeneous
A/B and each individual F_k as formal independent symbols. If the
Taylor coefficient is q_j, let C_j=j!q_j. The ODE implies

 C_(+,j+1)=lambda_+ C_(+,j)-Z sum_(k<=j) F_k j!2^(j-k)/(j-k)!,
 C_(-,j+1)=lambda_- C_(-,j)+Z sum_(k<=j) F_k j!2^(j-k)/(j-k)!, (7)

starting at C_(+,0)=B/Z and C_(-,0)=A/Z. Store the A/B weights apart
from the Z F weights. All recurrence weights are integers. Average the
formal coefficient vectors to obtain P and R before substituting their
interval inputs; this retains the F cancellation shared by the two ODEs.
Use independently coded interval substitution in mpmath.iv for each
coefficient, with its own directed positive Z interval and division by
2j!. Do not import the first method's interval hulls or weight table.

For the finite integer lambdas and orders0,...,20 used here, an exact
preflight comparison may check equality of the two independently built
weight tables. That is an implementation diagnostic. Equations (5)-(7)
are independently proved formulas; neither is justified by agreement of
a finite sample. The second method must independently pass every
candidate coefficient containment.

## 5. Whole-cell remainder through order20

For efficiency it is permissible to replace h_i by an explicit rational
H_i>=h_i, for example a dyadic upper rounding, if 522H_i<1 remains true.
All estimates below then apply to the entire polynomial-forcing family
on [0,H_i]. The actual spline is not extended across its next knot. The
canonical conclusion still uses only [0,t_(i+1)-t_i]. If the enlarged
interval prevents a sufficient bound, use h_i itself and record the
failed enlarged test. Neither branch changes the candidate budget.

Let C_k=|mid(F_k)|+rad(F_k), E_lo>0 and E_hi be the exact E endpoints.
For 0<=i<=20 put

 G_i=E_hi^2 exp(2H_i) sum_(k=0)^7 C_k
       sum_(v=0)^min(i,k) binom(i,v)2^(i-v) k!/(k-v)! H_i^(k-v). (8)

Leibniz's rule proves G_i>=sup|f^(i)|. Variation of constants gives

 Y_+=exp(max(lambda_+,0)H_i)(sup|B|/E_lo^2+H_i G_0),
 Y_-=exp(max(lambda_-,0)H_i)(sup|A|/E_lo^2+H_i G_0).

Iterating q'=lambda q+sign f gives the exact derivative identity

 q^(21)=lambda^21 q+sign sum_(i=0)^20 lambda^(20-i) f^(i).

Thus define D_+=|lambda_+|^21Y_++sum_i|lambda_+|^(20-i)G_i,
and D_- analogously. Taylor's integral theorem bounds the order20
remainder of either P or R by

 J=(D_++D_-) H_i^21/(2*21!).                            (9)

Again 0^0=1 is necessary for n=1 in the last sum. For each family use
its own interval coefficients c_j obtained through degree20, and let
M_j bound their absolute values. Then its degree12 remainder is at most

 sum_(j=13)^20 M_j H_i^j+J.                             (10)

Every value in (8)-(10) is evaluated with directed arithmetic. The first
method evaluates (8) using its displayed finite derivative weights. The
second constructs the derivative polynomials by repeated application of
p -> p'+2p starting from sum C_k u^k, and evaluates them by Horner on the
nonnegative endpoint H_i. This is a separate construction of each G_i.
The exponentials are bounded directly by the respective interval engines,
not by an unchecked floating call. Both (10) bounds must be at most the
same unchanged producer remainder. This is a sufficient test, not a
necessary condition for the producer's model to be valid.

## 6. Output audit, restart, and independent selected replay

Each cell is an atomic unit of the exhaustive calculation. Its record
must identify its exact endpoints, h_i and H_i, candidate array hashes,
actual input links, all counts, any failed enlarged-domain attempts,
and representative exact containment witnesses. Coefficient and remainder
comparisons use every required index even if only selected witnesses are
saved. The code's complete coverage, two-method execution and final
footer are essential; counts or digests alone are not mathematical proof.

The header pins the complete proof, source modules, exact data, scalar
archive and program files. An interrupted final JSON line may be removed
only after every earlier complete line and its header are validated.
Complete rows are never silently replaced. Reject a mismatching header,
duplicate or out-of-order cell, nonfinite value, negative radius, changed
source, missing footer at final audit or incomplete coverage. Log restart
boundaries, and replay the complete cells immediately on each side of
every actual interruption. The initial empty --resume event is recorded
separately and does not pretend that an interruption occurred.

An output auditor regenerates the frozen candidate arrays, validates all
saved rational endpoint inequalities and all coverage/pins, and computes
fresh selected enclosures at higher Arb precision by a third method.
This method solves for a degree7 particular polynomial Q from

 Q'+(2-lambda)Q=sign sum F_k u^k,
 q(u)=exp(lambda u)(q(0)-ZQ(0))+Z exp(2u)Q(u),           (11)

when lambda!=2. Solve the polynomial equation backwards from its highest
degree. When lambda=2, use

 q(u)=exp(2u)[q(0)+sign Z sum F_k u^(k+1)/(k+1)].

Direct differentiation verifies both expressions including the initial
condition. Taylor coefficients and a higher-order derivative remainder
follow by the product rule, preserving each input coefficient symbol
before bounding. These selected checks supplement the complete two-method
run; they are not themselves exhaustive coverage. Complete-cell replay
also includes the first and last cells, reproducibly selected cells and
every interrupted boundary. All promised sets must be explicitly matched
against the auditor's required sets before publication.

## 7. Conditional canonical conclusion and limits

On each accepted cell, the scalar archive places exp(t_i) in E_i at the
same exact point. The exhaustive forcing check (3)-(4) uses the actual
T and F arrays of this run. If topic99 has independently established that
those T boxes contain the exact normalized trial's local factor Taylor
coefficients, and topic98 has independently established the canonical
Green A/B at t_i, then the true canonical P_n,R_n solve (1). Uniqueness
of the scalar ODE, proved directly by variation of constants, puts them
inside the accepted Taylor models throughout the exact cell. Adjacent
exact cells cover the full finite annulus with no rounding gaps.

Until both canonical membership obligations and this full run are closed,
the conclusion remains a conditional finite-family statement. It does
not prove angular products, tensor Bernstein assembly, the spatial box
classification or every stated flow inequality. Neither a transport
inverse nor the physical nonlocal inverse follows solely from radial
Taylor models. There is no decisive IPM Analysis I endpoint here.

## 8. Endpoint refinement, exact statement and proof

This new topic162 repeats the full finite check from cell0. It neither
edits nor resumes topic101's failed stream. Topic161 proves containment
for its first failed coefficient only, not the remaining coefficients.
All target boxes, runtime candidate generation, ordinary degree12
convention, modes, cells and remainder budgets remain unchanged.

For an integer linear form U with input intervals and collected integer
weights, let [u0,u1] be its exact whole-box image. Let [v0,v1] be the
corresponding exact image of V. Let 0<e0<=E<=e1 and z0=e0^2,z1=e1^2.
Every coefficient in (6) is (U/Z+ZV)/d, d=2j!>0. Put

 lq=u0/z1 if u0>=0, otherwise u0/z0;
 uq=u1/z0 if u1>=0, otherwise u1/z1;
 lp=z0*v0 if v0>=0, otherwise z1*v0;
 up=z1*v1 if v1>=0, otherwise z0*v1.

Then [(lq+lp)/d,(uq+up)/d] contains the coefficient for every admitted
input. Indeed U/Z increases with U for every positive Z. Its minimum
therefore occurs at U=u0, after which its derivative in Z is -u0/Z^2;
its maximum uses U=u1 in the same way. The product ZV increases with V,
and its derivative in Z after fixing an endpoint is that endpoint.
These observations give the four displayed extrema, including zero and
sign-crossing intervals. Adding the two ranges is valid even when their
Z values are correlated. It may enlarge the exact joint range but never
underestimates it. Division by positive d preserves order. All these
quantities are exact rationals; no real extremum is inferred from a
floating sample. Signed dyadic inputs, including subnormals, are decoded
exactly before forming the linear images.

The first method performs this rational computation with Python Fraction
only after its original Arb512 coefficient enclosure fails the sufficient
test. Each rational endpoint is separately converted to an Arb512 point
ball. The lower endpoint of the lower ball and upper endpoint of the
upper ball form the outward dyadic test interval. They are never united
into a wide ball before the comparison. A nonfinite result, nonpositive
E lower endpoint, or failed refined containment stops the full run OPEN.
The original unrefined coefficient balls remain in the order20 remainder
bound (10); their validity does not depend on passing a coefficient test.
Thus endpoint refinement does not secretly change a remainder estimate
or candidate budget. The independent iv180 ODE recurrence is unchanged
and must pass every coefficient and every remainder on its own.

The independent output audit recomputes every refinement from the actual
input arrays. Its third method uses (11) and exact backwards solution of
the polynomial equation, collecting each forcing symbol before bounding.
Its homogeneous weights already contain 1/(2j!), and its forcing weights
contain their Taylor factorials. It therefore represents the coefficient
as U/Z+ZV, without an additional division by 2j!. It constructs U and V
with fmpq arithmetic, taking minima and maxima of all four rational corner
values for U/Z and ZV. This gives the same valid independent-interval
bound by bilinearity of ZV and monotonicity of division on positive Z.
It does not import the first engine's integral weights or rational hull
function. Each resulting rational endpoint is separately outward rounded
with Arb1536. When this third method's original ball test fails, this
independently derived refinement is allowed, recorded and checked. Its
original degree22 coefficients still provide its order22 remainder.
Every first-engine refinement's index is included in the third selection,
including all its 26 degree0..12 P/R coefficient tests for that mode.

Every saved refinement records cell (through its parent row), family,
mode, degree, the failed original exact dyadic bounds, the new outward
bounds, and the unchanged candidate endpoints. Original failure and new
success must both be checked, with no duplicate indices. The output
auditor regenerates original Arb512 bounds and the Fraction refinement
for identity with the saved record, then reconstructs the new enclosure
independently with the finite-particular fmpq method. Both independent
enclosures must pass the same original target; they need not have
identical rounded endpoints. Complete-cell replay compares refinement
records exactly. A bounded set of saved worst-case witnesses never
replaces the exhaustive coefficient loops.

The replay seed for this topic is
'ipmA-ver/topic162/radial-refined/replay/v1'. The fixed required set is
{0,2955,7808} plus the first two distinct indices from successive four-byte
big-endian SHA256(seed) words modulo7809. It also includes actual restart
neighbors as specified in section6. On replay cells and every257th cell,
third-method selected modes include1,2,3,64,135,261, intersected with the
run's modes. All recorded worst-case and refined modes are also included.
The output header pins this policy and the new schema radial-refined-v2.

The computational acceptance criterion is conditional until full fresh
coverage, candidate regeneration, the independent output audit and the
required replay finish and their actual results undergo a later review.
Proof or preflight acceptance alone is not the full mathematical verdict.
Section7's canonical linkage and limitations continue to apply.
