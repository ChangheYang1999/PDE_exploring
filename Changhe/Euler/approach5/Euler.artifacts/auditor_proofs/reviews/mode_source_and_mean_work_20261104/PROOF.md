# Velocity-mode source identities and spherical-mean work signs

Status: independent reconstruction of the existing Theory Agent C  supplements.
The first result is kinematic. The work statements require the full
Euler equation. Exact designated verdicts appear in the auditor's ledger (AUDIT_LEDGER.md).

## 1. Statements and dependencies

For any C1 divergence-free U on R3, a center a and an axis through a,
let V_m be the complete real velocity projection onto the paired
azimuthal modes plus/minus m, m>=1, and let V_0 be its mean. Then ball
energies and the spherical integral of q=tr((DU)^2) split over these
modes. Each V_m separately satisfies the finite-radius positive-source
inequality of A3094, with its own energy and source. No individual mode
energy asymptotic follows merely from the asymptotic of their sum.

For C1 velocity/C1 pressure full rotating profiles, write

    (1-c)U+((Ay+U).grad)U+omega JU+grad P=0,
    div U=0, A=cI-omega J, J(x1,x2,x3)=(-x2,x1,0),
    e=|U|^2/2, D=U.grad(P+e).

Spherical means in Sections4-6 are about the origin, not an arbitrary
translated center. If 0<c<1 and the spherical mean Dbar is everywhere
nonnegative, U=0. This needs no boundedness or dilation assumption.
If in addition U is bounded, U(R .) tends to0 in distributions, and
0<c<1/2, either U=0 or Dbar takes both strict signs. The azimuthal mean
D_0 and D itself then take both strict signs as well, for every omega.
This uses the confirmed energy theorem A3053, including its precise
remainder above c=2/5 and its finite energy at c=2/5. It makes no claim
that both signs recur at arbitrarily large radii.

## 2. Exact mode convention and orthogonal decompositions

Translate a to0 and write R_phi for the chosen axial rotation. Its
unitary action on vector fields is

    T_phi U(x)=R_phi U(R_(-phi)x).

Define V_0=(1/(2pi))integral_0^(2pi) T_phi U dphi, and, for m>=1,

    V_m=(1/pi)integral_0^(2pi) cos(m phi) T_phi U dphi.

These are the real orthogonal isotypic projections. In particular V_m
contains both signs of the frequency; taking only one real part with
an extra factor1/2 would not be this convention. Rotation commutes with
divergence, so all V_m are C1 and divergence-free, including on the axis.
Completeness of the trigonometric system gives convergence and Parseval
in L2 on every rotation-invariant ball or sphere. Hence

    E(R)=sum_(m>=0) E_m(R).

The derivative transforms by matrix conjugation:
D(T_phi U)(x)=R_phi DU(R_(-phi)x)R_(-phi). Thus DV_m is the same real
projection of DU under this matrix action. Transposition commutes with
that action and its projections. On each sphere, apply Parseval to the
Frobenius pairing of DU with (DU)^T. This gives

    Q(r)=integral_(S2)tr(DU(r theta)^2)dtheta
        =sum_(m>=0) integral_(S2)tr(DV_m(r theta)^2)dtheta
        =sum_(m>=0) Q_m(r).

The last series is absolutely convergent: the absolute value of each
term is at most integral_(S2)|DV_m|_F^2, and their sum equals
integral_(S2)|DU|_F^2. No summability of derivatives at infinity is
used, only their continuity on each compact sphere.

For a compact radial scalar test psi, multiplication by D2 psi is a
bounded self-adjoint operator commuting with rotations. Orthogonality
therefore also gives

    integral U^T D2 psi U=sum_m integral V_m^T D2 psi V_m.

For a C1,1 radial test this follows identically with its bounded weak
Hessian. These identities do not assert any corresponding additivity
of the positive part of a source.

## 3. What the modewise inequality actually proves

For each V_m let q_m=tr((DV_m)^2), and set

    M_(m,+)(R)=integral_(B_R)r^2[q_m]_+,
    M^Q_(m,+)(R)=integral_0^R r^4[Q_m(r)]_+dr.

Take the same radial cutoff chi, values in[0,1], and
Cchi=4(sup|grad chi|+sup|D2 chi|_op) as in A3094. For T>rho>0,
compact testing with the convex C1,1 function equal to r^2 inside
B_rho and 2rho r-rho^2 outside gives

    2E_m(rho)<=M_(m,+)(2T)+Cchi(rho/T)E_m(2T),
    2E_m(rho)<=M^Q_(m,+)(2T)+Cchi(rho/T)E_m(2T).

Each follows directly from the independent proof of A3094-A3095 applied
to this C1 divergence-free field. Positivity is assigned only to the
uncut convex Hessian; the cutoff errors are retained. If a particular
mode separately has the required positive energy growth, the previous
absorption argument applies to it. A growth law for sum E_m alone does
not supply that extra premise. Moreover the projected field need not
satisfy the nonlinear profile equation: the other modes exert Reynolds
forcing. Neither q_+ nor Q_+ is a sum of its modewise positive parts.
Thus these identities supply no universal nonlinear mode coercivity.

## 4. Exact work identity and its rotational mean

Dot the full momentum equation with U. The term U.JU vanishes, and
U.((Ay+U).grad U)=(Ay).grad e+U.grad e. Consequently

    D=-2(1-c)e-(Ay).grad e
     =-2(1-c)e-c y.grad e+omega partial_phi e.       (1)

Equation(1) is not an identity for an arbitrary independent pair U,P;
it uses the momentum equation. Azimuthal averaging about the rotation
axis removes the last derivative and commutes with y.grad:

    D_0=-2(1-c)e_0-c y.grad e_0.

Circlewise Parseval in the real velocity convention above gives

e_0=sum_m average_phi(|V_m|^2/2). The displayed formula is explicitly
free of omega, but the profile and e_0 may themselves depend on omega.
No comparison between different rotating solutions follows.

## 5. Spherical mean, origin behavior and one-sided signs

Let ebar(r)=(1/(4pi))integral_(S2)e(r theta)dtheta, and similarly define
Dbar. The integral of partial_phi e on the sphere is zero. For r>0,

    Dbar=-2(1-c)ebar-c r ebar'
        =-c r^(1-k)(r^k ebar)', k=2(1-c)/c>0.       (2)

Continuity of U at0 gives r^k ebar(r) tending to0 as r decreases to0.
If Dbar>=0 for all r>0, the nonnegative function r^k ebar is
nonincreasing from this zero limit, hence identically zero. Then U=0,
by nonnegativity of |U|^2 and continuity. The same applies to Dbar=0.
This argument proves the first work statement without any behavior
assumption at infinity. Formula(2) needs only C1 regularity on r>0.

For the opposite sign suppose U is bounded with the stated dilation
limit and 0<c<1/2. If c<2/5, A3053 already gives U=0. For c>=2/5 put
beta=5-2/c and

    E(R)=integral_(B_R)|U|^2,
    g(r)=r^(1-beta)E'(r)=8pi r^k ebar(r)>=0.

Again g(0+)=0. The hypothesis Dbar<=0 implies g is nondecreasing.
If c=2/5, beta=0 and A3053 gives finite total energy. But
E(R)=integral_0^R g(r)dr/r; a nonnegative nondecreasing g with any
positive value makes this integral diverge at infinity. Thus g=0.

If 2/5<c<1/2 and U is nonzero, A3053 gives L>0 and
E(R)=LR^beta+O(R^(beta-1)), with0<beta<1. Monotonicity and the ratio
limit force g(r)<=beta L for every r: if g(r0)>beta L, integrate
E'=g r^(beta-1) over[r0,R] and let R tend to infinity to contradict
E(R)/R^beta tending to L. Therefore

    LR^beta-E(R)=integral_0^R [beta L-g(r)]r^(beta-1)dr.

The integrand is nonnegative and, because g(0+)=0, strictly positive
near0. The right side is nondecreasing and bounded below by a fixed
positive number at all sufficiently large R. The precise remainder
makes the left side O(R^(beta-1)), tending to0, a contradiction.
This step would fail if only E(R)/R^beta tending to L were known.

Neither global sign of Dbar is possible for a nonzero profile in the
stated class. Hence there exist r1,r2>0 with Dbar(r1)<0<Dbar(r2).
The spherical mean of D_0 equals Dbar. Each strict spherical sign
therefore gives a strict sign of D_0 somewhere on that sphere, and
circlewise averaging gives the corresponding sign of D somewhere.

## 6. Agreement with the integrated work identity

Integrating (1) over a centered ball, using div(Ay)=3c and
(Ay).n=cR on its boundary, gives

    integral_(B_R)D=(5c/2-1)E(R)-(cR/2)E'(R).       (3)

No pressure integration or normalization is used. The rotation is
tangent to the sphere. Formula(3) is the integrated identity already
used in A3079; (2) differentiates its radial distribution before
integration and yields the stronger spherical-sign conclusion. Both
proofs keep the additional boundedness/dilation hypotheses explicit.

## 7. Pure-swirl control and the remaining momentum equation

For U=F(r)Jy, direct differentiation gives div U=0 and the pressure-free
momentum residual

    M=(F+c r F')Jy-F^2(y1,y2,0)

for every omega. Let Gamma=(Jy).U=F(r)(y1^2+y2^2). Then

    (Jy).M=c y.grad Gamma+(1-2c)Gamma.

For the previously confirmed tail F=b r^s, b!=0,
s=(beta-5)/2 and0<beta<1, a circle integral forces1+cs=0 if the
residual is a gradient. This is exactly c=2/(5-beta). At that exponent
Gamma has the homogeneity permitted by the torque identity, but the
remaining required pressure gradient is F^2(y1,y2,0). Its first
component has z derivative2s b^2 r^(2s-2)y1 z, whereas its third
component is zero. It cannot be the gradient of a C1 pressure on a
shell containing points with y1 z!=0. A smooth prescribed gradient
would give local C2 regularity and commuting mixed partials. Thus the
full momentum obstruction remains valid at the torque-degenerate
exponent, and for every real c and omega. The control is purely m=0.

## 8. Verification and open boundaries

Both complete C notes of08:22:05 and08:29:36 were read. The mode
normalization, infinite Parseval passage, positive-part limitation,
origin limit and strong energy remainder were independently checked
above. These are existing configured model file exchanges; actual
provider execution is independently unattested. The notes' diagnostic
scripts, numerical cutoff constants and execution records are not
certified. No mathematical computation or formal build was used.

Automatic critical source integrability, assignment of total energy
growth to a particular mode, eventual work signs, and unrestricted
rotating nonexistence remain open. The all-center kinematic source
statement does not translate the origin-based full-profile work
identity to a different center without additional terms.
