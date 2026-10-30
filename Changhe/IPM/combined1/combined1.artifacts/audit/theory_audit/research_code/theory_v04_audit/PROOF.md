# Independent audit of theory_v04

## Scope and evidence

This audit reads all 852 lines of source/theory_v04.md, the immutable
publication of 2026-10-29T06:06:04Z, SHA256
7638b0dae2e1cd03bd307fec28143ce84ae37b5a42a0d882d64e879094fcca93.
The companion source/THEORY_FINAL.md is draft 6. Source hashes are in
source/SHA256.json. Previously audited theorems retain their exact
hypotheses; this document does not independently rerun every older
candidate certificate or convert an OPEN computation into a proof.

The weak-test, adjoint-domain, full-span Gram, strict closed-ball,
defect-feasibility, fixed-c scaling and forced-tail repairs in sections
1 and 2 agree with the earlier audits they cite. The new positive-ray
claim of section 5.2 is proved below with its necessary qualifications.
The arithmetic check verifies every printed distance ratio in section
3 against the exact larger budgets, and checks the rounding issues.
There is no existence closure in this publication.

## 1. Directed rounding of displayed bounds

Let

    mu=97/250, C=397, b=8/5, d=48/25,
    sf=1/5184, smax=1/1024, q=361/1024,
    A=sqrt(1601^(4/5)q^2+2^15 q+2^20),
    Rstar=(2mu/(3b))sqrt(mu/(3C)).

The already audited annular argument, for a globally H2 correction
supported in 20<=r<=32 and having only sine modes n>=19, gives

    ||h||2 <= (1351/10^6)/[(1-d sf)A]       (fixed ball),
    ||h||2 < Rstar/[(1-d smax)A]           (parameter family).      (1)

These right sides are respectively

    1.312585971071236...e-6,
    2.839272408273124...e-6.

Consequently the displayed fixed-ball value1.312585971e-6 and the
family value2.839272408e-6 are not upward roundings of (1). The cited
calculation establishes instead the safe bounds1.312585972e-6 and
2.839272409e-6, or the simpler family bound2.84e-6.
This refutes the rounding/equality inference, not the smaller bounds
as independently provable mathematical assertions: (1) is an upper
estimate, and no claim of its sharpness has been made. No candidate
exclusion changes.

Similarly let s=1/262144,t=1/5184. For the exact forcing norms and
hypotheses of ../forcing_conversion/PROOF.md, including f in E3 and
Q3(f)<=10^6 E2(f), the proved estimate is

    X_t(f)<=kappa N_s(f),
    kappa=2[(2*10^12+16410)^(t/2)+34t]/(1-34s)
          =2.01885036527399881954... .                         (2)

Printing this last equality as kappa=2.01885 is an approximation;
substituting it in an upper inequality does not follow from (2).
The safe upward rounding2.018851 is sufficient for the already stated
threshold comparison: if N_s(f)<=163.88/1572864, then
2.018851 N_s(f)<4207/20000000. Thus that comparison remains valid.
Again this is a correction of the deduction, not a proof that no
sharper norm inequality is possible.

## 2. Positive leading-amplitude ray and dilation

Let c>1, gamma=1/c, delta=1-gamma, N=floor(2/delta),
e_j=1-(j+1)delta, and let chi be a smooth radial cutoff vanishing
near zero and equal to one outside a compact set. Let Theta_0 be a
nonzero smooth real S1 angular density profile. Let Theta_j for
1<=j<N be its forced profiles from the audited recurrence

    j(c-1)Theta_j = sum_(l+m=j-1)
      [-e_m Psi_l' Theta_m + (e_l+1)Psi_l Theta_m'],             (3)

where Psi_l depends linearly on Theta_l through the nonresonant
angular stream equation. Let R=sum chi r^e_j Theta_j+g with S1
g in L2, and define D_lambda f(X)=lambda f(X/lambda), lambda>0.
All velocities are the canonical ones of the audited tail chart.
Let S(R) be the set of S1 stationary densities at this c in R+L2.
Distributional products and the canonical velocity have the same
meaning as in the previously audited weak and tail statements.

Then for mu>0 and lambda=mu^(1/delta):

1. The forced profiles of mu Theta_0 are mu^(j+1)Theta_j.
2. Every reference R_mu with those profiles and an L2 remainder lies
   in the same affine L2 class as D_lambda R.
3. D_lambda gives a bijection S(R)->S(D_lambda R).
4. For the specifically dilated reference,

       dist_L2(D_lambda R,S(D_lambda R))
         =lambda^2 dist_L2(R,S(R)),                           (4)

   with infimum over an empty set interpreted as infinity.

Proof. The assertion for Theta_0 is immediate. If profiles through
j-1 have their stated degrees, every term with l+m=j-1 in (3) has
degree(l+1)+(m+1)=j+1 in the leading amplitude. Division by the
nonzero scalar j(c-1) proves the first assertion by induction.
Now 1-e_j=(j+1)delta, hence

    D_lambda[chi(r)r^e_j Theta_j]
       =chi(r/lambda)r^e_j mu^(j+1)Theta_j.

The difference between the two cutoff choices is smooth and compactly
supported away from zero, hence belongs to L2. Dilation maps L2 to
L2, proving the second assertion. Canonical velocity covariance gives
U[D_lambda rho]=D_lambda U[rho]. Direct differentiation then gives
F(D_lambda rho;c)=D_lambda F(rho;c). D_(1/lambda) is its inverse and
maps the affine classes back, proving the third assertion. Finally

    ||D_lambda h||2^2=lambda^4 ||h||2^2

by X=lambda Y in the two-dimensional integral. Take the infimum over
the bijective solution sets to obtain (4). No inverse estimate is
used, and no existence of a member of either solution set is implied.

The positive amplitude ray is therefore a symmetry orbit of affine
classes. Negative amplitudes are not obtained from lambda>0. Arbitrary
refits R_mu in the same class need not satisfy (4), because the
reference point has also moved within that class. If R_mu=D_lambda R+a
with a in L2, the two distances differ by at most ||a||2 when the
solution set is nonempty, by the triangle inequality. One must name
the reference when reporting a distance, not only its affine class.

### A homogeneous norm alone does not make a ratio invariant

For a norm with ||D_lambda h||E=lambda^alpha||h||E, the corresponding
distance scales by lambda^alpha for the dilated reference. Its ratio
to an admissible radius b_lambda is invariant only if that radius
also satisfies b_lambda=lambda^alpha b_1. Homogeneity of the norm
places no such condition on a chosen radius or a theorem's background
constants. As an elementary counterexample take the homogeneous L2
norm, the dilation-invariant solution set{0}, a nonzero S1 reference
R in L2, and balls of radius1 at every reference. The distance/radius
ratio is lambda^2||R||2, which is not invariant.

Thus the unconditional sentence in section5.2 about a framework with
a homogeneous norm is not justified. The valid statement is conditional
on covariance of its admissible balls and every theorem hypothesis.
No such covariance has been computed for the registered inhomogeneous
or weighted frameworks. The exact positive-ray assertions1-4 above
are independent of that unproved budget comparison.

## 3. Design rows and unsupported span inferences

For a canonical S1 reference R, write I=<F(R),phi>,
M=(2c+1)phi+(cX+U[R]).grad phi,
D=||M||2+||phi grad R||2 and H>=||grad phi||infinity.
For every admissible stationary correction h in L2 the audited weak
identity yields

    |I|<=D||h||2+H||h||2^2.                                  (5)

Neither derivation nor applicability of (5) depends on whether the
optimizer used phi. A violated design row therefore remains a valid
necessary-distance certificate. A small certified value only weakens
this one lower bound; it gives no upper bound on the actual distance.
A held-out row has the same mathematical status, while serving an
additional role in detecting an objective that missed an obstruction.
Neither type of row measures the exact distance in general.

Sections0 item5 and6 item3 infer absent basis leverage from a few
optimization records. No such inference is justified without further
bounds. For example a scalar residual f=-1 and Jacobian J=1 have zero
undamped minimum, but positive damping lambda gives step1/(1+lambda)
and residual-lambda/(1+lambda), which stays near-1 at large lambda.
Small change in the residual can coexist with full representational
ability. The detailed multirow version and the correctly conditioned
dual lower bound are in ../damped_diagnostic_scope/PROOF.md.

Valid replacement: the reported optimization reduced some pairings,
while the tested high-mode pairings remained large. This motivates
new basis functions or changes to the optimization. It does not prove
a positive minimum residual over the current span or zero leverage.
SectionR2 item1 already states this limitation for the damped trials;
the summary and basis recommendation must preserve it too.

## 4. Remaining report scope

The first sentence of section5 says no chart satisfying R-TE exists.
The documented conclusion is that no such chart has been constructed
or verified in this program. The latter is a status statement; the
former would assert a new nonexistence theorem and is unsupported.
The final sentence of R2(c), concerning a new high-row estimate,
requires the same qualification. R-TE is a list of design requirements,
not an established inverse theorem. The exclusion at the critical
weight does not exclude other weights or infinite-dimensional charts.

Section3 uses already audited candidate certificates. Its exact ratio
checks use the true bound25/54684 for the graded comparison, rather
than relying on a downward printed decimal. Every claimed factor must
be below the ratio to this larger budget. The numerical check retains
all factors and every comparison in verification/result.json.

The weighted-force finite-tail examples in section2.2 remain labeled
CLAIMED, as stated there. The complete derivative and Hdot^-1 values
of newer numerical reports are not certified by this text audit.
Every all-c interpretation retains the common nonzero leading-tail
hypothesis; every fixed-ball exclusion retains its specified spaces,
normalizations, canonical velocity and positive-margin assumptions.
