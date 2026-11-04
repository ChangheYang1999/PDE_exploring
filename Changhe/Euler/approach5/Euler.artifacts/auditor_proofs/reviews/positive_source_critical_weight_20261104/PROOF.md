# Critical positive-source weight from sublinear energy growth

Status: independently reconstructed and compared with the existing theory agent, including its corrected response. The theorem is kinematic; its Euler application is conditional on an additional finite weighted moment. Exact designated verdicts are recorded in the auditor's ledger (AUDIT_LEDGER.md).

## 1. Statement and dependencies

Let U be C1 on R3 with div U=0. Define

    E(R)=integral_(B_R)|U|^2,
    q=tr((DU)^2), q_+=max(q,0),
    M_+(R)=integral_(B_R)|y|^2 q_+(y)dy.

Assume E(R)/(L R^beta) tends to1, with L>0 and 0<beta<1. Then there
is c_beta>0, depending only on beta and a fixed smooth cutoff, such that

    M_+(R)>=c_beta L R^beta

for all sufficiently large R. Consequently

    integral_(1<|y|<R)|y|^(2-beta)q_+(y)dy
        >= beta c_beta L log R-C,

for some finite C. In particular the integral over R3 with weight
(1+|y|)^(2-beta) is infinite. For every fixed center a the same conclusions
hold with |y-a|, the same L and c_beta, but potentially different starting
radius and additive constant. No uniformity over a is asserted.

A smooth decaying divergence-free control below has exactly E(R)=L R^beta
for R>=2, quadratic positive-source moment L h_beta R^beta+O(1), and
critical moment beta L h_beta log R+O(1), where
h_beta=(3-beta)^(3/2)/sqrt(5-beta). Every smaller real power gives a finite
positive-source moment. Thus the exponent is sharp in this kinematic
class. The control fails full Euler for every finite c and omega.

For bounded C1/C1 full profiles with Hb, 2/5<c<1/2, the confirmed energy
law A3053 supplies this hypothesis with beta=5-2/c and L>0 unless U=0.
Therefore finiteness of integral(1+|y-a|)^(2/c-3)q_+ for even one fixed a
implies U=0 and P constant. The result does not derive that finiteness
from the full equation, and neither endpoint is included.

## 2. Finite-radius identity and error bound

Local convolution gives the distributional identity
q=partial_i partial_j(U_iU_j). Hence for every compact smooth scalar test
psi, integral q psi=integral U^T D^2 psi U. The same identity holds for
a compact C1,1 test that is smooth except across one sphere: mollification
has locally bounded Hessians converging almost everywhere, while its
values converge uniformly. A continuous gradient excludes a surface
measure in the Hessian.

Choose a radial smooth cutoff chi with0<=chi<=1, equal to1 on B_1 and zero
outside B_2, and write K1=sup|grad chi|, K2=sup|D^2 chi|_op and
Cchi=4(K1+K2).
For rho>0 put

    phi_rho(y)=|y|^2                 if |y|<=rho,
               2rho|y|-rho^2        otherwise.

This is C1,1 and convex, bounded between0 and |y|^2. Its Hessian equals2I
inside B_rho and (2rho/|y|)(I-e_r tensor e_r) outside; it is nonnegative.
Moreover phi_rho<=2rho|y| and |grad phi_rho|<=2rho.

For T>rho, test against phi_rho chi(y/T). On the outer annulus the
additional Hessian terms have norm at most

    (4rho T)K2/T^2+2(2rho)K1/T=Cchi rho/T.

The nonnegative main term dominates2E(rho). The nonnegative test is at
most |y|^2 and supported in B_(2T), so its source integral is at most
M_+(2T). All integrals here are finite. Therefore

    2E(rho)<=M_+(2T)+Cchi(rho/T)E(2T).                 (1)

Only the uncut phi_rho is convex. No sign is assigned to the full cutoff
Hessian, no derivative of U is estimated at infinity, and no negative
source moment is assumed finite.

## 3. Scale absorption and the logarithmic divergence

Set

    K=max(2,(2^(beta+2)Cchi)^(1/(1-beta))),
    c_beta=1/[2(2K)^beta].

For every sufficiently large rho, E(rho)>=(L/2)rho^beta and
E(2Krho)<=2L(2Krho)^beta. Taking T=Krho in (1) gives

    M_+(2Krho)>=Lrho^beta[1-2^(beta+1)Cchi K^(beta-1)]
               >=(L/2)rho^beta.

The choice of K makes the bracket at least1/2 because beta-1<0.
Every sufficiently large R is2Krho, proving the claimed bound at all
such R, not only a sequence. The ratio limit alone was used.

M_+ is locally absolutely continuous, since q_+ is continuous. Fix a
large r0>=1. Integration by parts on the finite interval[r0,R] gives

    integral_(r0<|y|<R)|y|^(2-beta)q_+
      =R^(-beta)M_+(R)-r0^(-beta)M_+(r0)
       +beta integral_(r0)^R t^(-beta-1)M_+(t)dt.

Discard the nonnegative first term and use the lower bound on M_+ in
the remaining integral. This gives beta c_beta L log R minus a fixed
constant. Local integrals are finite, and (1+r)^(2-beta)>=r^(2-beta),
so the full weighted integral diverges. This argument neither
differentiates an asymptotic error nor subtracts divergent integrals.

For fixed a and R>|a|, the energy on B_R(a) lies between E(R-|a|) and
E(R+|a|). Both divided by L R^beta tend to1. Translating the kinematic
identity proves the same theorem at a. No translation invariance of the
full profile equation is assumed.

## 4. Exact-energy control and sharpness of the power

Let J(x1,x2,z)=(-x2,x1,0), K0=8pi/3, s=(beta-5)/2 and
b=sqrt(beta L/K0). Choose smooth chi0 between0 and1, zero for r<=1 and
one for r>=2. The field b chi0(r)r^s Jy is smooth, divergence-free, and
has energy strictly smaller than L2^beta inside B_2. Its energy equals
K0 integral r^4 f(r)^2dr. Fill the positive deficit with a scalar
multiple t0 eta0 of a nonzero smooth bump supported in(1/4,1/2), where

    t0^2=(L2^beta-K0 integral_0^2 b^2 chi0(r)^2 r^(2s+4)dr)
          /[K0 integral_0^2 r^4 eta0(r)^2dr].

The supports are disjoint, so no cross term occurs. With
f0=b chi0 r^s+t0 eta0 and U0=f0(r)Jy, the inner energy is exactlyL2^beta.
Outside2, the sphere energy is beta L r^(beta-1), hence E0(R)=L R^beta.
The field is smooth at0 because it vanishes near0, and its magnitude is
O(r^((beta-3)/2)), tending uniformly to zero.

For r>=2, direct multiplication of
DU0=f0J+(f0'/r)(Jy) tensor y gives, with t=z/r,

    q0=b^2 r^(beta-5)[(3-beta)-(5-beta)t^2].           (2)

Set A=3-beta and B=5-beta. The positive angular band is |t|<sqrt(A/B),
and its bracket integral over S2 is

    2pi integral_(-sqrt(A/B))^(sqrt(A/B))(A-Bt^2)dt
        =(8pi/3) A^(3/2)/sqrt(B).

Multiplication by b^2 therefore gives beta L h_beta. Radial integration
with the quadratic weight gives L h_beta R^beta+O(1); with the critical
weight it gives beta L h_beta log R+O(1). With any real power gamma, the
tail for (1+r)^gamma is comparable to integral r^(gamma+beta-3)dr,
finite exactly when gamma<2-beta. The compact interior contributes finite
constants. The order and exponent are sharp; c_beta is not asserted optimal.

## 5. Full momentum fails for the control

On r>2 the control is b r^s Jy. Its rotation terms cancel because
(Jy).grad U0=JU0. Also y.grad U0=(s+1)U0 and
(U0.grad)U0=-b^2 r^(2s)(x1,x2,0). Full momentum would therefore require

    (1+cs)U0-b^2r^(2s)(x1,x2,0)+grad P=0.             (3)

The angular derivative of a single-valued C1 pressure integrates to zero
around a horizontal circle in this exterior. The other angular term is
constant on that circle and nonzero unless1+cs=0. If that coefficient
vanishes, (3) instead requires grad P=b^2r^(2s)(x1,x2,0). Its first
component has z derivative2s b^2r^(2s-2)x1z, nonzero where x1z is nonzero,
while the z component has x1 derivative zero. This smooth vector field
cannot be a gradient. A C1 pressure with that gradient would be C2
locally, so the mixed-derivative contradiction is legitimate. This treats
all finite c and omega, including the torque-degenerate coefficient.

## 6. Euler implication and evidence boundary

The full rotating equation is

    (1-c)U+[((cI-omega J)y+U).grad]U+omega JU+grad P=0,
    div U=0.

For U in C1 intersect L-infinity, P in C1, and Hb meaning U(R.) tends to
zero in distributions, A3053 gives the positive-coefficient energy law
in2/5<c<1/2 when U is nonzero. The exponent in this theorem is then
2-beta=2/c-3 in(1,2). This proves the additional finite-moment criterion
for all finite omega. The inequality

    q_+<=|q|<=sum_(i,j)|partial_i U_j partial_j U_i|
             <=sum_(i,j)|partial_i U_j|^2=|DU|_F^2

also gives the sufficient weighted derivative condition, without any
integration by parts at infinity. No bound or integrability for DU is
inferred from decay.

All six source sections at19fca718 and all29manual checks were read,
including the formal-source scope. The proof here does not depend on the
separate LIT372 construction; only the already confirmed energy theorem
is imported for the Euler corollary. No computation or formal build was
used. The complete existing-agent comparison at6b99e824 was read, including
all six section checks and W1-W4. Sections7-9 reconstruct its useful
refinements and correct two statements in that original comparison. The
complete corrected comparison and A129 acknowledgment were also read;
they adopt both corrections and the scope precisions. Existing
configured model file collaboration is recorded; actual provider
execution is independently unattested. No novelty, automatic integrability
or optimal full-Euler threshold is asserted.

## 7. Positive part after spherical averaging

For a fixed center a define the unnormalized spherical integral

    Q_a(r)=integral_(S2) q(a+r theta)dtheta,
    Q_(a,+)(r)=max(Q_a(r),0),
    M^Q_(a,+)(R)=integral_0^R r^4 Q_(a,+)(r)dr.

These are continuous or continuously differentiable, respectively. Because
the test in Section2 is radial about its chosen center, its source pairing
equals integral phi_rho(r)chi(r/T)Q_a(r)r^2dr. Its nonnegative weight is
at most r^2 and supported in[0,2T]. It is therefore at most
M^Q_(a,+)(2T). The identical Hessian calculation proves

    2E_a(rho)<=M^Q_(a,+)(2T)+Cchi(rho/T)E_a(2T).

The absorption and finite-interval integration by parts of Section3 now
give, with the same K and c_beta,

    M^Q_(a,+)(R)>=c_beta L R^beta,
    integral_1^R r^(4-beta)Q_(a,+)(r)dr
        >=beta c_beta L log R-C_a

for all sufficiently large R. Since Q_(a,+) is at most the spherical
integral of q_+, this is a stronger lower-bound statement. No assertion
that the two criteria admit strictly different full profiles is needed.

Consequently a bounded C1/C1 full profile with Hb and2/5<c<1/2 is zero if,
for one center a,

    integral_1^infinity r^(2/c-1)Q_(a,+)(r)dr<infinity.

This includes a finite positive quadratic source moment and an eventually
nonpositive spherical source mean, in this open range of c. It does not
extend this argument to the critical endpoint c=2/5.

For the actual pressure let Pbar_a denote its normalized spherical mean.
The distributional Poisson equation gives

    (r^2 Pbar_a'(r))'=-r^2 Q_a(r)/(4pi).

The right side is continuous away from0, so this identity also supplies the
needed classical derivative of r^2 Pbar_a'. The radial critical integral
is exactly

    4pi integral_1^infinity r^(2/c-3)
        [-(r^2 Pbar_a'(r))']_+ dr.

Thus this weighted amount of decrease is infinite for a nonzero profile,
about every fixed center. This is not a pointwise sign for Pbar_a'.

For the Section4 control,

    Q_0(r)=beta L(2-beta)r^(beta-5)>0,  r>2.

Indeed the full angular integral of the bracket in(2) is
(8pi/3)(2-beta). Hence its radial positive quadratic moment is
(2-beta)L R^beta+O(1), and its radial critical moment is
beta(2-beta)L log R+O(1). For weight exponent gamma the tail is again
integral r^(gamma+beta-3)dr. The critical power is therefore also sharp
for this spherical version in the stated kinematic class.

## 8. Two-sided energy bounds and the signed control moment

The all-radius lower bound needs only two-sided growth. Suppose that
0<a0<=A0 and, for all sufficiently large R,

    a0 R^beta<=E(R)<=A0 R^beta,  0<beta<1.

Choose K>=2 with K^(1-beta)>=2^beta Cchi A0/a0. At T=K rho the finite
inequality gives

    M_+(2K rho)>=
      [2a0-2^beta Cchi A0 K^(beta-1)]rho^beta
      >=a0 rho^beta.

The same is true of M^Q_+. Thus the coefficient at radius R is
a0/(2K)^beta, and integration by parts gives a positive logarithmic
critical-moment lower bound. An exact limiting energy coefficient is
unnecessary for these qualitative conclusions.

For the control put F=(U0.grad)U0=-f0(r)^2(x1,x2,0). Then q0=div F,
y.F=-|U0|^2, and on the sphere of radius R,
F.n=-f0(R)^2(x1^2+x2^2)/R. The finite-radius divergence theorem gives

    integral_(B_R) |y|^2 q0
      =R^2 integral_(partial B_R) F.n-2integral_(B_R)y.F
      =2E0(R)-K0 f0(R)^2R^5
      =(2-beta)L R^beta,  R>2.

Subtracting this finite signed moment from M_+(R) yields

    M_-(R)=[h_beta-(2-beta)]L R^beta+O(1),

where M_- uses max(-q0,0). Its coefficient is positive: both h_beta and
2-beta are positive, and

    h_beta^2-(2-beta)^2=(7-3beta)/(5-beta)>0.

Both one-sided quadratic moments therefore diverge. This computation
does not subtract infinite integrals.

At beta=5-2/c, s=(beta-5)/2=-1/c. Thus the control's exponent is exactly
the case in which the angular coefficient1+cs in(3) vanishes. The pressure
curl test in Section5 is essential for this case.

## 9. Derivative rates, corrected comparison and evidence limits

The comparison's matrix identity has paired signs reversed. For the
Jacobian A the correct identities are

    |A|_F^2+tr(A^2)=(1/2)sum_(i,j)(A_ij+A_ji)^2,
    |A|_F^2-tr(A^2)=(1/2)sum_(i,j)(A_ij-A_ji)^2.

Both are obtained by expansion and imply |q|<=|DU|_F^2, as used above.
The inequality in the original proof is unaffected.

The comparison's statement that A492/A498 give no rate for DU is also
incorrect. The complete A476/A477/A492/A498 ledger statements were
reread. Under their full-profile hypotheses, uniform velocity decay,
bounded DU and1/3<c<1 give the natural bound DU=O(r^(-1/c)).
Those earlier proofs are dependencies, not newly proved here. Their
conclusion does not give a finite critical weighted derivative moment:
substituting that upper bound gives a radial majorant proportional to
r^(-1), whose integral diverges. A divergent upper bound alone proves
neither convergence nor divergence of the actual integral.

For the control itself,

    |DU0|_F^2=b^2r^(2s)[2+s(s+2)(1-t^2)],  t=z/r.

Here -5/2<s<-2, so the bracket is bounded above and below by positive
constants. At the Euler-relevant exponent s=-1/c its critical derivative
moment does diverge logarithmically. The velocity has exact natural
order in its sphere supremum and along any fixed nonaxial direction;
it vanishes on the axis. A uniform positive radial lower bound on |U0|
would therefore be false.

A sufficient additional pointwise assumption is, for some epsilon>0,

    |DU(y)|<=C |y|^(-1/c)(log|y|)^(-1/2-epsilon)

for all sufficiently large |y|. Its squared critical weighted integral
is bounded by a constant times
integral dr/[r(log r)^(1+2epsilon)], which is finite. The profile is
then zero by Section6. This improvement is not inferred from decay.

The comparison's diagnostic script, numerical checks, claimed execution
times and nonoptimal numerical comparison of constants are not certified.
The analytical refinements above are independently proved, with exact
algebra in place of those diagnostics. The unrestricted rotating problem
and automatic satisfaction of any finite critical moment remain open.

The corrected comparison of08:15, retained in verification, accepts these
rate, sign, cutoff, normalization and axial-zero precisions. No unresolved
disagreement remains on the stated analytical results.
