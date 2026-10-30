# Candidate015 independent two-mode Laplacian reproduction

The exact target is C1-N1-015-pairQ-quot013 at
c=4076476460239181/2251799813685248. Its canonical JSON is bound to
its immutable raw snapshot by the accepted candidate audit. The own
computation uses only this canonical source and existing exact own
Cartesian/polar field routines. It recomputes both modes1 and3 at every
a in{0,1/4,1/2,3/4,1,5/4,3/2,7/4} from all contributing input modes.
The complete proof below fixes the measure, norms, endpoint conditions,
cell argument and every analytic hypothesis. This target's numerical
conclusion is OPEN until that production and this comparison pass.

The peer record supplies seven complete energies as exact rational
multiples of pi, one for each positive a, and two mode energies at each.
For every row check positivity and exact addition of the two rational
mode energies, then compare each with the independently produced own
containing energy ball. Check the norm lower and upper endpoint displays
against the same exact peer energy. These displays are containing balls,
not rational endpoint centers. Finally recompute all seven complete-cell
ratios with own energies and the exact maximum formula below, compare
the own production's saved cells, and verify every strict rational floor.

This is a projection lower witness, not a full upper norm. The conditional
seven-cell scheme exclusion cannot be inferred from L2 distances.
It needs the independent origin identities, all framework realization,
canonical velocity, hyperplane, partition and absorption hypotheses.
No inverse is constructed and no profile nonexistence follows.

The peer result binds wlap_modes.py and its canonical hash only. Its
historical F cache has been deleted. Current e2norms.py and hminus1.py
are frozen and read as explanatory source, not claimed to be the exact
historical loaded versions. No peer source is executed. The own complete
reproduction supplies the physical-source certificate independently of
that missing historical cache. This provenance limit is retained.

## Underlying complete argument

# Projected whole-plane Laplacian tests for successor candidates

## Exact reference, quantities and conditional conclusion

Each input is a previously audited exact single-scale candidate
with c=4076476460239181/2251799813685248, gamma=1/c and
delta=1-gamma. Its candidate record must confirm immutable
snapshot hashes and all forbidden residual sectors exactly zero.
Let rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy) and
F=(cX+u).grad rho-rho. Fix a finite set S of positive odd modes.
For a>=0 define

    J_S(a)^2=sum_(n in S) int_R2 (1+r^2)^(2-a)
                                     |Delta Pi_n F|^2 dX,

where Pi_n is the full-circle sine projection. Orthogonality
and radial weighting give J_S(a)<=N_a(F), the same norm of
the full Laplacian. In particular no omitted angular term
is treated as zero and no full upper norm is claimed.

Assume the exact realization, domain, input hyperplane, dyadic
partition, velocity and absorption hypotheses of the audited
FW-T-DYADIC-Y-v1 framework and T4-146 origin inverse theorem,
as frozen with their Opus reviews in origin_dyadic_ceiling/.
Their additional numerical origin hypotheses are

    1<c<2, chi_xxyy(0)=1-c, a0=rho_y(0)>=5c-4.

The checker verifies these directly from the canonical origin
polynomial. Under those analytic assumptions, a necessary
condition for the registered scheme is

    5^((a-2)/2) J_S(a)
        <H(c-1)(1+c-ca)/(1+a),  0<a<1+1/c,           (1)

where H(d)=max_(0<s<d)(d-s)sqrt(4 pi s(1+s)). If every
recorded scalar cell violates(1) strictly, that candidate
is excluded from this specified sufficient scheme for
0<a<2, 0<s<1 and each fixed finite Rw>0. This is conditional
on the full framework hypotheses. It is not nonexistence
of an exact profile or failure of every possible proof scheme.
The numerical tests remain OPEN until independently reviewed.

## Exact residual projection and Cartesian verification

The independent canonical derivative algebra represents
rho and the Cartesian velocity derivatives by finite rational
polynomials in t=r^2/(1+r^2), with branch factors determined
by c. The product identity

    cos(l theta)sin(m theta)
        =[sin((m+l)theta)+sin((m-l)theta)]/2

selects every pair contributing to the requested sine mode.
Keep the sign of m-l. Combine the linear drift and every
selected nonlinear product exactly, then divide out the
verified zero powers at the origin. This gives

    Pi_n F=r sum_ell v^(ell delta/2) P_(ell,n)(t) sin(n theta),
    v=1-t.

This is the direct projection proved in successor_weak_probes.
All background frequencies contributing to a selected residual
mode are retained. Selection of few output modes does not mean
selection of few input background frequencies.

For d=ell delta/2 set T_d P=(1-2dt)P+2t(1-t)P'. Applying
r partial_r twice and the angular second derivative gives

    Delta[r v^d P(t) sin(n theta)]
        =r v^(d+1)L(t) sin(n theta),
    t L=T_d(T_d P)-n^2 P.

The code constructs L by exact polynomial division and checks
zero remainder. Independently apply the exact Cartesian
derivative recurrence twice in each coordinate to the projected
field, add the two diagonal derivatives and compare every
coefficient with L. Also verify equality of the two mixed
Cartesian derivatives. These identities precede integration.

## Finite exact moments and outward products

Compose each L with t=1-v exactly and extract the exact lowest
power v^q with nonzero coefficient. Write L(1-v)=v^q Q(v).
Require ell delta+2q-2>0 for each branch, which guarantees
diagonal integrability at a=0. The integral for one mode is

    (pi/2) sum_(ell,k) int_0^1
      v^(a+(ell+k)delta/2+q_ell+q_k-3)
      (1-v)Q_ell(v)Q_k(v)dv.

Use each unordered pair with multiplicity2 off the diagonal.
Every radial cross term is included. Convert exact rational
coefficients to containing Arb balls only after differentiation
and endpoint cancellation. Form polynomial products outward.
Each monomial integral is1/(a+b+j+1); all denominators must
be strictly positive rational numbers. Thus the resulting
energy and square-root balls enclose the whole-plane projected
norm. This includes spatial infinity v=0 without truncation,
quadrature or a leading-term replacement.

## Seven-cell implication

Write d=c-1 and A=1+1/c. Exact differentiation gives

    d/ds[(d-s)^2 s(1+s)]
       =(d-s)[d+(2d-3)s-4s^2].

The bracket has one positive root in(0,d),

    s_star=(2d-3+sqrt((2d-3)^2+16d))/8.

It is the unique maximum point. Evaluating H(d) there gives
a containing ball for the exact maximum, without a numerical
maximization assumption. J_S(a) decreases because its integrand
decreases pointwise. The function(1+c-ca)/(1+a) decreases
on[0,A]. Therefore on a cell[l,h], and for an evaluated weight
e>=h, the strict inequality

    5^((l-2)/2)J_S(e) > H(d)(1+c-cl)/(1+l)           (2)

violates(1) throughout that cell. Use quarter points from0
to3/2 and the final cell[3/2,A], evaluated at7/4. These seven
cells cover[0,A]. For A<=a<2 the required positive low rate
1+c-ca already fails. Any positive-s case not allowed by
the origin inverse theorem also fails its hypotheses.
The strict test is performed with full containing balls;
an upper norm endpoint alone is never used to exclude.

## Calibration and dependencies

First evaluate modes1 and3 for007 at weights0,1/4,...,7/4 and
compare every projected norm with the independent Cartesian
records of N4-113. Reproduce all seven confirmed scalar
ratios in N4-128/129. This checks the complete pipeline
before applying it to008 and009. Additional selected modes
may strengthen a lower bound; they cannot produce a full
upper norm unless all modes are accounted for separately.
The candidate, audit, helper, norm and theorem hashes are
registered in each write-once output. The Opus reviews of
T4-146 are retained as dependencies; they are not repeated
or replaced by a numerical comparison.
