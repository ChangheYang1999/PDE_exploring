# Audit of the H12 numerical report's conclusions

This audits the inference and status claims in the frozen 08:02 UTC
NUMERICS_FINAL, SHA256
cc80028931ebc98b8e8d313eca840d88b17b3886ecdf3683bde20789b8d8402b.
The complete source is adjacent. This is not a rerun of every FLOAT
entry. The main conclusions below already follow from T4-214 to219,
T4-273, T4-312, T4-321/332 and T4-330. This proof restates the logical
arguments so that the report corrections stand alone.

## 1. Finite probes do not identify a span floor or residual mass

Let H be an infinite-dimensional real Hilbert space and let ell_1,...,
ell_N be bounded linear functionals. Their common kernel contains a
nonzero vector: restrict the map h -> (ell_i(h)) to the span of N+1
linearly independent vectors and apply rank-nullity. Thus there is
w != 0 with ell_i(w)=0 for all i. For every F and real t, F+t w has
the same measured pairings, but its norm tends to infinity as |t| grows.
For smooth S1 fields one may choose the N+1 vectors to be smooth
compact radial bumps times one fixed odd sine harmonic, with disjoint
radial supports. The same conclusion then holds within smooth S1
fields in that chosen angular band. It holds even when all pairings
are computed exactly.

Small finitely many pairings consequently do not upper-bound the norm
of that angular band. Nor do larger values prove that the band's norm
has increased: adding a sufficiently large common-kernel vector to
the earlier field gives the same earlier measurements and arbitrarily
larger earlier norm. The campaign's necessary radii additionally have
reference-dependent denominators, so comparing those radii does not
isolate even the raw pairing amplitudes.

Likewise, a better trial in an expanded basis does not prove that the
old basis had a positive best residual. Minimize |x-1| in the old space
R. Its infimum is zero. A damped least-squares step from x=0 has
x=1/(1+lambda), lambda>0, and residual lambda/(1+lambda), as close to
one as desired. A later trial at (x,y)=(1,0) in the enlarged space R2
has residual zero even though the original space already contains that
minimizer. Therefore finite optimization records, including exact
ones, do not certify an old-space lower bound.

The inferences in source lines23-25 and183-186 are REFUTED: neither a
SPAN limit nor movement of mass into modes33 to47 follows from the
reported trials. The observed FLOAT changes may be reported exactly
as trial comparisons. The truth of a positive minimum over the old
admissible family remains OPEN.

## 2. A certified design probe remains evidence

In the campaign's fixed-c chart, with the full hypotheses of the weak
proof, every distributional stationary L2 correction h satisfies

    |I| <= D ||h||2 + H ||h||2^2,
    I=<F,phi>, D>=0, H>=0.

This follows by testing the equation and applying Cauchy-Schwarz and
the canonical velocity contraction. Its proof makes no assumption
about whether phi was used during optimization. If the right-hand
side at an allowed radius b is strictly smaller than a certified
lower bound for |I|, the entire closed ball is excluded. Optimizing
that pairing cannot invalidate the inequality. Conversely, making it
small does not produce an upper bound on true solution distance.

Thus the phrase 'design rows, not evidence' in section4b is REFUTED
as a statement about rigorous necessary tests. The claim in lines226-
227 that NC-T-DIST fails only because nobody optimized it is likewise
REFUTED:014 and015 use angular pairing objectives and still have
certified violations. A statement that the point test is 'not removable'
by any redesign is OPEN; the current point certificates exclude the
specified references and balls, not every reference in a family.

The Newton bound in line115 is retained. For the linear equation
Lh=-F, testing gives |I|<=D||h||2 without the quadratic term. T4-214
checks the strict numerical inequality I>D*0.0047694 for007, so every
admissible exact L2 Newton solution has norm greater than0.0047694.
A damped approximate step with a nonzero linear residual is not an
exact Newton solution. Cite T4-214 for this distinction.

## 3. Two dampings and a spectrum do not certify an optimum

For the scalar residual x-1, the damped solutions at any two positive
lambdas are both strictly below the undamped solution1. Their two
norms do not bracket its norm; their residuals are both strictly above
the optimal residual0. This exact counterexample refutes the generic
'bracket the FLOAT answer' implication in line119. One can instead
report a range observed at the two tested damping values. Coordinate
redundancy may make coefficient minimizers nonunique without making
the physical least-squares problem mathematically meaningless.

The Jacobian spectrum contains no gradient information by itself.
For f_b(x)=x-b in R, at x=0 the Jacobian is1 for every b. The gradient
of |f_b|^2 is-2b, so the same spectrum occurs both at a stationary
point (b=0) and at arbitrarily nonstationary points. A measured small
coordinate gradient is also not an invariant stationarity certificate
without its norm, scaling and error control. Therefore lines236-237
cannot infer that the plateaus are stationary rather than conditioning
stalls from gn_spectrum. Section7 already states the correct OPEN
status of their cause; the conclusion must agree with it.

## 4. Calibration is not a general quadrature error theorem

A quadrature rule with finitely many nodes cannot have a uniform
relative-error guarantee over all smooth integrands. Choose a nonzero
nonnegative smooth bump supported in a small open ball disjoint from
the nodes. Its quadrature value is zero and its integral is positive.
Rescaling changes the integral arbitrarily. Thus the blanket relative
error assertion in line7 is REFUTED unless restricted to the tested
calibration integrands. Derivative bounds and a proved remainder would
be needed for a larger stated function class. The heading's single
MID32 rule also conflicts with its explicitly labeled MID24 and MID16
experiments. Each diagnostic should retain its actual rule.

## 5. Scope, exact indices and current certificates

The valid H12 coverage is every registered scalar and original graded
candidate/framework pair through017, except the controlled FLOAT
comparison011. The registered dyadic family is separately excluded
only at state131,d2,007,008,009,010. The localized route lacks a complete
high estimate. Candidate018 is newly registered and OPEN. The blanket
all-snapshot/all-ball claims in lines18-19 and103-104 are REFUTED.

The strongest confirmed necessary L2 floors are >0.004769166867 for007,
>0.001232449584356253 for015, >0.001470360924123708 for016, and
>0.00167183069831928 for017. They exceed the scalar and original graded
ceilings;016 and017 no longer await such a test.007 has confirmed
0.6355243760<||F||_Hdot^-1<0.6355322686 and X(F)>756.531263, so its
forcing gap against0.00021035 exceeds3596535.57. These statements
reference the already audited computations; none is a new computation
here. Rounded norm displays should be described as rounded enclosures,
not literal exact equalities.

Define the report's old sector index h explicitly by global K=h+1.
The nonautomatic L2 sectors are global(2,0),(3,0),(4,0), equivalently
old(1,0),(2,0),(3,0). The seven negative-norm sectors are global(2..6,0),
(1,1),(2,1). The printed eleven-sector list in line12 contains only
ten entries: add the automatically zero leading global(1,0), or say
ten nonautomatic cancellations. The assertion that every candidate
from002 cancels all seven is contradicted by the report's own004 row,
which describes its four-branch L2-only construction.

Finally, potential modes m=9..15 generate density modes2m-1 and2m+1,
so the possible density range is17..31, not19..31. Differentiating a
cos(2m theta) angular term yields the two adjacent odd sine harmonics.
The exact mode17 coefficient is nonzero in the specific added family
by T4-321, with density injectivity accepted in T4-332. That mode must
be included when explaining whether a design probe is held out.

## 6. Outcome and dependencies

No certified exclusion is reversed. The report should retain the
measured FLOAT improvements, their actual objectives and quadratures,
and the rigorous current certificates, while leaving the cause of the
plateau and a lower bound over the old family OPEN. This audit does
not certify the many other FLOAT values or any future optimization.
Dependencies: frozen source; elementary Hilbert-space linear algebra
and bump functions; weak-test proof T4-185/196/214; scope T4-330;
current certificates T4-304/310/311/319/320/331; exact support T4-321/332;
007 full negative norm N4-249 and forcing bound recorded in T4's summary.
