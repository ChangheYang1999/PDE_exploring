# Candidate001 affine L2 exclusion, accepted reviews and the changed-c test

Written at 2026-10-29T15:09:56.978235+00:00, before this topic's checker was implemented.

## Statement and notation

Let chi be the sum of the 860 exact rational generators in source/raw.json,
SHA256 8077f1305e5403264831de280689bb9334628bd1aa1233ce4dec58017dc355c7.
This is the immutable candidate C1-N1-001-refit860-jabs. Write
c0=4076476460239181/2251799813685248, gamma=1/c0, delta=1-gamma,
rho=-partial_y Delta chi, and u=(-chi_xyy,chi_xxy). Let L2 be the real
Lebesgue space on R2. For h in L2 define U[h]=(-R1R2 h,R1^2 h), with
Rj of Fourier symbol i xi_j/|xi|. For every fixed real c and every fixed
constant vector v in R2 there is no real h in L2 satisfying

 F_(c,v)+div((cX+u+v)h)-(2c+1)h
        +U[h].grad rho+div(h U[h])=0                         (1)

in distributions, where F_(c,v)=(cX+u+v).grad rho-rho. The canonical
case is v=0. Neither a trace nor a symmetry, normalization, smallness,
correction-gradient or moment assumption is imposed on h.

This is a nonexistence result within the one affine class rho+L2,
for the specified reference velocity and its constant translates.
It covers every correction space continuously embedded in L2 at every
radius. It does not decide classes admitting non-L2 corrections, a
changed far-field density, an unrelated profile, or existence of a
self-similar profile. A linear velocity background is outside scope.

## Exact input and its independent verification

The original standalone application is preserved as
source/application_PROOF.md, SHA256
771ad6b4af564e1b3a0acf1284184fd8f36c15d2dd090212370122d433789a3e.
Its 896 exact checks reconstruct the leading coefficients from raw
rows. T1 R1-046 independently derives the density and velocity by
Cartesian differentiation of homogeneous Laurent polynomials, with
912 passing checks. T2 independently uses Wirtinger differentiation
with exact Gaussian rational coefficients, with 30 passing checks
including four finite-point diagnostic checks. Both independent
calculi agree exactly with the source/leading_coefficients.json table.
The latter four FLOAT checks are supportive observations and are not
premises of this proof. This audit reads each complete proof and
checker and verifies the source identities; it executes no peer code.

Every raw generator has form

 A H_m(X)(1+r^2)^(p_j-m) T(r^2/(1+r^2)),
 H_m=r^(2m)cos(2m theta), p_j=(3+gamma-j delta)/2,

where j is 0,1,2,3, m<=9, and T=t^k or t^w P_n(2t-1) with
nonnegative integer indices. Since T(1)=1, extracting r^(2p_j)
leaves (1+z)^(p_j-m)T(1/(1+z)), analytic near z=r^-2=0 with
constant term one. This finite generator sum has angularly uniform
exterior asymptotic expansions, with the corresponding remainders
under each fixed finite derivative. It is smooth at the origin.
In particular u=O(r^gamma), grad rho=O(r^(gamma-1)), and

 rho=r^gamma G0(theta)+r^q G1(theta)+o(r^q),
 F_(c0,0)=r^q E(theta)+o(r^q),
 X.grad rho=gamma r^gamma G0(theta)+o(r^gamma),      (2)

where q=2gamma-1=427123167131315/4076476460239181 and 0<q<gamma<1.
The angular profiles are the exact sine polynomials in the stored
table. G0 has the ten nonzero modes 1,3,...,19; E has the ten
nonzero modes 21,23,...,39. Thus

 int E G0=0, int E^2>0, int G0^2>0                 (3)

on [0,2pi]. Each square integral is pi times the exact positive sum
of squared rational coefficients. The q coefficient is exactly
(c0 q-1)G1+[u0.grad(r^gamma G0)]_angular. No angular mode is dropped.
All residual labels are gamma-H delta-2K. The (0,0) term vanishes
because c0 gamma=1, (1,0) is q, and all remaining labels have H>=2
or K>=1, hence are strictly below q. No distinctness claim for an
unbounded label set is needed to justify the leading sector.

The accepted annular theorem source/annular_PROOF.md supplies a
previous independent audit, but the full argument follows here.

## The distributional annular argument

The multiplier has vector symbol
(xi1 xi2/|xi|^2,-xi1^2/|xi|^2), which is divergence free and has
squared norm xi1^2/|xi|^2<=1. Plancherel gives ||U[h]||2<=||h||2.
Consequently h U[h] is in L1 and (1) is a well-defined distribution.
The smooth coefficients have no local singularity or contact term.

Choose eta in C_c^infinity((1,2)), nonnegative and nonzero. For a
smooth angular factor A, put phi_R=R^-1 eta(r/R)A(theta), supported
on A_R={R<r<2R}. Its L2 norm and that of X.grad phi_R are bounded
independently of R, while ||grad phi_R||2=O(R^-1) and
||grad phi_R||infinity=O(R^-2). Testing (1) gives, for R large,

 |<F_(c,v),phi_R>| <= C ||h||L2(A_R)
   +C R^(gamma-1)(||h||L2(A_R)+||U[h]||L2(A_R))
   +C |v| R^-1 ||h||L2(A_R)
   +C R^-2 ||h||L2(A_R)||U[h]||L2(A_R).            (4)

The constant depends on this fixed c, v, eta and angular factor,
and the smooth reference bounds, but not R. The cX transport and
(2c+1)h term give the first term. The u transport and U[h].grad rho
term give the second. The constant transport gives the third, and
the nonlinear divergence term gives the fourth by Holder's inequality.
Each annular L2 tail tends to zero. Since gamma<1, the whole right
side tends to zero, without differentiation of h.

If c=c0, use A=E. The added background forcing v.grad rho is
O(r^(gamma-1))=o(r^q), since gamma-1<q. By (2),

 <F_(c0,v),phi_R>=R^(q+1)(C_E+o(1)),
 C_E=(int_1^2 t^(q+1)eta(t)dt)(int_0^(2pi)E^2)>0.

This diverges because q>0 and contradicts (4).

If c!=c0, use A=G0. Then

 F_(c,v)=(c-c0)gamma r^gamma G0+o(r^gamma),
 <F_(c,v),phi_R>=R^(gamma+1)((c-c0)gamma C_G+o(1)),
 C_G=(int_1^2 t^(gamma+1)eta(t)dt)(int_0^(2pi)G0^2)>0.

The absolute value diverges and contradicts (4). Both the radial
exponent and angular factor have changed. Using E in this case would
give zero leading pairing by (3), so that interpretation of the old
abbreviated sentence is invalid. This explicit test is the required
clarification of section 4 of T4-458. T1 already stated it explicitly;
T2 correctly requested that it be written into the accepted record.

## Normalization, scope and acceptance

The normalized high-regularity condition c[h]=partial_y U2[h](0)=0
and its contact contribution -h_y(0)/4 are not used. General L2 h
need not have such traces. Exclusion of the entire affine L2 class
therefore includes any normalized subset with defined traces. A
scaling perturbation changing the growing angular far field is not
an L2 correction, so the theorem makes no assertion about it.

Both Opus theory reviews are accepted for the canonical application.
The constant-background extension in T1 R1 is also confirmed by (4)
and the strict ordering gamma-1<q. The word correction is recorded
without changing the reviewed source hash. The exact candidate
application has CONFIRMED status after T4-458 and this peer acceptance.
No contraction, inverse construction, small residual or existence
closure is inferred. The stored source hashes identify what was
reviewed; they are not substitutes for the arguments or arithmetic.

The finite checker checks the raw branch sums, exact exponents,
nonzero norms, orthogonality, ten observed external identities,
the two review targets and logs, and preservation of all local inputs.
It does not recompute the independent derivative calculi or the
finite-point Taylor experiment. The exact rational coefficient data
remain in JSON. Actual run times and evidence hashes are saved in
verification/result.json.
