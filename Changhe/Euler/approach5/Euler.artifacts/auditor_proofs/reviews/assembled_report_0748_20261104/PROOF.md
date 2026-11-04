# Audit of the corrected report and three source criteria

## 1. Exact assembly, comparison chain and scope

The checked report has SHA256
86286d4420b0704d08c1bca13b34fdab557ec74f498cc4c1fd25aef3785abb87,
7437 lines, and a stated verdict cutoff of A3077. Its predecessor
7fe98679351cf7a1c0be27adb731cae58c697f37679e7a8a214dc0b0ff91b294
was not approved because of A3066-A3068. Both are retained in verification,
with the complete 359-line direct difference. Every changed line was read,
including the long Appendix A rows in a separate untruncated pass.

The earlier independent review read the complete 424-line difference from
approved pin37391724 to pin7fe98679. That review remains a dependency.
Consequently the present comparison transfers the earlier approval
A3039, at cutoff A3032, to the corrected assembly at cutoff A3077. This
covers front matter, main Sections0-10 and Appendix A, with the previous
conditional and external-source qualifications. Historical Appendices B
and C are not collectively certified; their changed passages were checked
individually. This is a delta audit, not a fresh reading of all7437lines.

Throughout, U and P solve the full profile equation when a profile is
asserted, J(x1,x2,z)=(-x2,x1,0), q=tr((DU)^2), and
E(R)=integral_(B_R)|U|^2. Kinematic statements explicitly omit the equation.
The target remains2/5<c<1/2, every finite omega, and uniformly decaying
whole-space profiles. The general rotating conjecture remains open.

## 2. The corrections requested in A3066-A3068

The summary and historical source-symmetry passage now explicitly require
E(R)=o(R^3). The horizontal constant profile U=b with
P=-[(1-c)b+omega Jb].y remains a counterexample when that condition is
omitted. It has q=0, whereas its pressure is non-axisymmetric for nonzero
horizontal b in the target range. Thus the corrected text has the exact
scope of A3040-A3043.

The spherical-source table now assigns the positive definite Hessian to
f(y)=sqrt(1+|y|^2), whose radial and tangential eigenvalues are respectively
(1+|y|^2)^(-3/2) and (1+|y|^2)^(-1/2). For the compact test f chi_R it
separately retains an annular Hessian error bounded by C E(2R)/R. This
corrects the false positive-Hessian assertion without changing the proof.

The absorbing-ball theorem is described as localizing the pressure
symmetry. Local regularity and the local equation alone are correctly
separated from the global hypotheses needed for its proof. Assertions
that conditions do not follow from decay now say that they are not known
or not derived. The vorticity paragraph preserves bounded U and Hb and
removes only an additional vorticity condition at infinity. The period and
translation-return alternatives both inherit the common decay and c-range
premises. The specific objections in A3066-A3068 are therefore resolved.

## 3. Cumulative source criterion, Theorem8(f)

For C1 divergence-free U put
G(r)=integral_(B_r)q, N(r)=integral_(partial B_r)(U.e_r)^2,
K(r)=integral_0^r s G(s)ds and T(r)=E'(r).
Local mollification justifies the flux identity at this regularity:
G=N'-(T-N)/r. Since E and rN vanish at the origin, K=rN-E.
In particular K<=rE'-E and K>=-E. If E=o(r) and K>=-C for large r,
then ((E-C)/r)'>=0 and its limit is zero, giving E<=C. At finite energy,
integrability of N gives liminf rN=0, hence liminf K=-E(infinity).

For a bounded full C1/C1 profile with Hb,2/5<c<1/2, the confirmed energy
law gives E=Lr^beta+O(r^(beta-1)), beta=5-2/c in(0,1), with L>0 unless
U=0. Eventual lower boundedness of K therefore excludes a nonzero profile.
With the actual pressure mean Pbar, divergence of the equation gives
G=-4pi r^2 Pbar'. Thus eventual G>=0 or nonincreasing Pbar suffices.
The contrary necessary signs and liminf statements in Theorem3(j) follow.

Averaging K<=rE'-E over[R,2R] by integration by parts gives an upper bound
-k L R^beta+O(R^(beta-1)), where
k=(2^(beta+1)-1)(1-beta)/(1+beta)>0.
Together with K>=-E(2R), this puts K<=-(k/2)L R^beta on a set of measure
at least k 2^(-beta-2)R for all sufficiently large R. No derivative of the
energy error is used. The conditional angular-tail limit in the table
has coefficient integral|F.theta|^2-beta^(-1)integral|F|^2<0 for nonzero F,
since0<beta<1. The critical exponent is not included in this criterion.
The shear and decaying-swirl controls keep their non-profile limitations.
These statements match A3063-A3065 and their complete reconstruction.

## 4. Exterior spherical source criterion, Theorem8(g)

Write Q_a(r)=integral_(S2)q(a+r theta)dtheta. For every fixed center,
E=o(R) also gives shifted energy o(R). The convex-test argument implies
that a nonzero field has a negative spherical mean below a positive one.
If Q_a<=0 beyond b, take a radial convex h with h=0 on[0,rho], rho>b,
0<=h'<=1 and h',h''>0 beyond rho. The Hessian controls U outside B_rho(a),
while its compact-cutoff error is O(E(2R+|a|)/R), tending to zero. Letting
rho decrease to b proves compact velocity support.

For a full C1/C1 compactly supported U, the carrier has complete flow
Phi_t and determinant exp(3ct). The one-form alpha=U.dy satisfies
Phi_t^*d alpha=exp((2c-1)t)d alpha. Therefore the bounded open nonzero
vorticity set is invariant, but its volume is multiplied by exp(3ct).
When c is not zero this forces the set to be empty. Harmonicity and
compact support then give U=0. This is the prior A067 argument, not a new
claim of priority; it also treats c=2/5, where the energy coefficient
vanishes. The report's compact-support phrase is read as compact support
of U; the pressure is constant outside a ball containing that support by the equation.

Thus the bounded-Hb criterion covers0<c<1/2, including the critical case
conditionally. A nonzero profile has Q_a>0 arbitrarily far out for every
center, but arbitrarily distant negative means are not asserted. The
pressure conversion (r^2 Pbar_a')'=-r^2 Q_a/(4pi) is distinct from the
cumulative condition in(f). These statements match A3072-A3074.
The radius called beta in two report passages should preferably be renamed
rho to avoid collision with the energy exponent; this is a notation
precision, not a mathematical gap.

## 5. Positive quadratic source moment, Theorem8(h)

For a C1 divergence-free field with E=o(R), finite
M_+=integral |y|^2 max(q,0) implies finite energy. Use the C1,1 convex test
f_R=|y|^2 inside B_R and2R|y|-R^2 outside, multiplied by chi(y/L).
Its Hessian lies between0 and2I and equals2I on B_R. The error is bounded
by C(R/L)E(2L). First let L tend to infinity at fixed R, obtaining
2E(R)<=M_+, then let R increase. Only after finite energy is known,
monotone convergence for the positive and negative source parts and
dominated convergence for the Hessian give
2E(infinity)=M_+-M_-, with0<=M_-<=M_+<infinity.
The radial formula integral_0^infinity r^4 Q(r)dr is absolutely convergent.

For bounded full C1/C1 profiles, U_iU_j is in L2. The actual pressure
is its L2 Riesz pressure plus a constant, by the rescaled equation and
mean value property of the harmonic difference. The cutoff energy
identity then gives(2-5c)E(infinity)=0 for every finite omega. Consequently
finite energy implies U=0 for every real c not equal to2/5. At c=2/5 only
the moment identity is obtained. The report keeps2/5<c<1/2 in its target
corollary, and does not transfer that corollary to c=1/2. Its controls
correctly distinguish a kinematic obstruction from an Euler counterexample.
These statements match A3075-A3077, including the A121 range precision.

## 6. Construction screen and remaining transferred text

The added six-version screen has the scope of A3069-A3071. Differentiation
of u=tau^(gamma-1)U(x/tau^gamma) gives c=gamma>1 for the inspected family.
Rotation cancels for the axisymmetric no-swirl ansatz. The finite-energy
evolution is asymptotic, not an exact finite-energy profile. The inspected
current interior manuscript retains missing PDE and persistence steps;
the boundary manuscript has a periodic-cylinder domain. For
Gamma=g0+bz+O(z^2), the wall source is2g0b, as now stated, rather than2b
without g0=1. Neither complete construction proofs nor a classification of
all possible Euler singularities is certified.

The unchanged positive portions of the prior424-line review retain their
confirmed scopes: C1 absorbing-ball symmetry, source-pressure orthogonal
symmetries, local controls, energy recheck, stationary C1 theorem and source
sign theorem. Nothing in these changes proves the unrestricted rotating
conjecture or removes a conditional theorem's additional premise.

## 7. Existing-agent comparison and conclusion

The complete existing Theory Agent A notes A124 and A125 were read and retained.
A124 compares the intermediate6cb723cc against7fe98679 and re-derives(f),
including the quantitative constant and conditional angular-tail limit.
A125 compares86286d44 against6cb723cc, checking(g),(h), the main necessary
conditions, proof outlines and table rows against its prior complete
A120-A121 analyses. Both agree with the present reconstruction. The
optional radius notation correction above is accepted. Claimed regeneration
checks, scripts and execution are not independently certified here.

The exact report pin86286d44 is approved at cutoffA3077 with the scope in
Section1. Only results with their existing designated CONFIRMED verdicts
may be labeled PROVED, and a conditional result remains conditional.
Existing configured model file collaboration was used; actual provider
execution is independently unattested. No new model client or mathematical
computation was used.
