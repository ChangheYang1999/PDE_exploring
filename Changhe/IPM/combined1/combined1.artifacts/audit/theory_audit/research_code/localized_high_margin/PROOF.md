# Radius ceiling when only the low-energy row is localized

## Statement and scope

Let s>0 and J^s=(1-Delta)^(s/2) on R^2. Use the unitary Fourier
transform and the ordered Hessian tensor. Suppose a proposed component
box for an S1 correction h has

    ||omega D^2 J^s h||2 <= r2,
    ||D J^s h||2 <= r1,
    ||w J^s h||2 <= r0,

where omega and w are measurable and at least1 almost everywhere.
Set n=(r2^2+2r1^2+r0^2)^(1/2). If the unchanged high-derivative
closure margin is required to be positive,

    1/2-4708s-(217/50+1049s/5)n/sqrt(s)>0,              (1)

then every correction in the box satisfies

    ||h||2 <= ||h||H^(2+s) <= n
         < 50/(651 sqrt(28248)) < 25/54684 < 1/2000.   (2)

The result applies to the specific recipe that changes the low-energy
row with a bounded transport weight w=exp(psi), normalized by
inf psi=0, and retains the original high row. No transport equation
for psi or property of the candidate can relax (2) under these
hypotheses. The result does not cover a new high-derivative estimate,
a decaying low weight w<1, or a norm for which n no longer dominates
the displayed Sobolev norm. Such changes require their own analysis.

## Proof

Since omega,w>=1, the Fourier identity

    (1+|xi|^2)^2 = 1+2|xi|^2+sum_(i,j) xi_i^2 xi_j^2

and Plancherel give

    ||h||H^(2+s)^2
      = ||J^s h||2^2+2||D J^s h||2^2+||D^2 J^s h||2^2
      <= r0^2+2r1^2+r2^2=n^2.

The multiplier of J^(2+s) is at least1, so ||h||2<=n. Equation(1)
requires s<1/9416. Dropping the additional positive term1049s/5
in its coefficient of n yields

    n < (50/217) sqrt(s)(1/2-4708s).

Put u=sqrt(s). The derivative of u/2-4708u^3 is
1/2-14124u^2. The unique positive maximum occurs at
u=1/sqrt(28248), with value1/(3sqrt(28248)). This proves the
irrational bound in(2). Finally28248>168^2 and
651*168=109368, so that bound is less than50/109368=25/54684.
Since50000<54684, the last quantity is less than1/2000.
The argument uses no low-row coercivity estimate and is complete.

## Consequences for the current candidates

The independently certified necessary unweighted L2 distances are
strictly greater than0.004769166867 for007 and0.00199234339 for013.
Both exceed1/2000. Therefore neither candidate can be closed by the
low-row-only recipe under(1), even if its low-row transport-weight
estimate is made arbitrarily strong. A hypothetical correction with
unweighted L2 mass at least2e-3 concentrated in the annulus20<=r<=32
also exceeds the ceiling: its full-plane L2 norm is at least that
annular norm. The same holds for2e-2. Angular localization changes
none of these inequalities.

This is a statement about this set of component inequalities, not a
nonexistence theorem for the stationary PDE. In particular the
necessary distances do not themselves place an upper bound on what
a substantially different localized norm can admit. No quantitative
closure radius for such a different norm has been certified here.

## Dependencies and verification

This is a direct consequence of the independently audited high-row
margin and the graded-budget calculation. A frozen copy of the
source proof and the T2 localized proposal is under source/. The
proposal's low-row-only comparison is heuristic; the present result
is conditional only on the explicitly displayed inequalities, and
does not promote that proposal to an existence theorem. Verification
requires only the displayed Fourier and polynomial identities and
integer comparisons, with no numerical computation or PDE solver.
