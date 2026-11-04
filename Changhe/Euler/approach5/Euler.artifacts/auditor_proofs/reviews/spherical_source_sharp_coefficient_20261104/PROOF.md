# Sharp coefficient for the positive spherical source

Independent audit with a complete existing-agent comparison. Designated
verdicts are recorded separately in the auditor's ledger (AUDIT_LEDGER.md). Optimality here concerns
a kinematic class and positive part after spherical integration. No
full-profile optimality or general nonattainment is asserted.

## 1. Statement, notation and scope

Let U be C1 on R3, div U=0, q=tr((DU)^2), and
E(R)=integral_(B_R)|U|^2. Fix L>0 and0<beta<1. Write

    Q(r)=integral_(S2)q(r theta)dtheta,
    H_Q(R)=integral_1^R r^(4-beta)[Q(r)]_+dr,
    F_tan(R)=integral_(2<|y|<R)|y|^(-beta)|U_tan|^2dy,
    U_tan=U-(U.e_r)e_r,
    k_beta=beta(2-beta)(1-beta).

The sphere measure has total4pi. If E(R)=LR^beta+O(R^(beta-1)), then

    H_Q(R)>=k_beta L log R+beta(2-beta)F_tan(R)-C       (1)

for every sufficiently large R, with a finite field-dependent C. With
only E(R)/(LR^beta) tending to1, the corresponding conclusion is

    liminf H_Q(R)/log R >= k_beta L
                  +beta(2-beta)liminf F_tan(R)/log R. (2)

The same statements hold about any fixed center a, with the same L and
k_beta, using radial/tangential components relative to a. Other constants
may depend on a.

The coefficient k_beta, when the tangential term is omitted, is the
optimal universal lower coefficient in this kinematic class, even among
smooth uniformly decaying divergence-free fields. For every epsilon>0
there is such a field with exact E(R)=LR^beta for R>=2 and
lim H_Q(R)/(L log R)<k_beta+epsilon. Its shifted energy is
LR^beta+O_a(R^(beta-2)); it has smooth Poisson pressure but solves no
full rotating Euler profile equation, for any real c and omega. No
minimizer, pointwise-q_+ optimality or full-profile optimality is claimed.

## 2. Compact test and the retained tangential term

For a compact smooth test phi, local mollification and div U=0 give

    integral q phi=integral U^T D^2 phi U.             (3)

Choose smooth radial nonnegative f, zero on B1 and equal to r^(2-beta)
outside B2, and a radial smooth cutoff chi with values in[0,1], equal
to1 on B1 and0 outside B2. Test with f(y)chi(y/R). Outside B2,

    U^T D^2 f U=(2-beta)r^(-beta)
                      [(1-beta)|U|^2+beta|U_tan|^2]. (4)

The inner Hessian can have either sign; its compact integral is bounded
by a field-dependent constant. Terms involving derivatives of chi are
supported in R<r<2R and bounded in operator norm by C_beta R^(-beta),
so their total contribution is at most C_beta R^(-beta)E(2R)=O(1).
The remaining main Hessian is nonnegative outside B2.

On the source side, radiality permits the positive part after integration
over the sphere. Outside B2 the signed source pairing is at most H_Q(2R),
up to the fixed integral over1<r<2. The inner source pairing is another
finite constant. Thus (3)-(4) imply

    H_Q(2R)>=(2-beta)(1-beta)F(R)
                         +beta(2-beta)F_tan(R)-C,
    F(R)=integral_(2<r<R)r^(-beta)|U|^2.

Both F and F_tan change by O(1) across a factor-two annulus, since their
nonnegative increments are bounded by R^(-beta)E(2R). Therefore one may
replace2R by R on the left and R by R/2 on the right, and then restore
F(R),F_tan(R), losing only another constant.

Exact finite integration by parts gives

    F(R)=R^(-beta)E(R)-2^(-beta)E(2)
                          +beta integral_2^R r^(-beta-1)E(r)dr.

Under the precise remainder, the error integrand is O(r^-2), giving
F(R)=beta L log R+O(1). Under the ratio limit it gives
F(R)/log R tending to beta L by a logarithmic Cesaro argument. These
prove (1)-(2); no derivative of the remainder is used. Since
E(R-|a|)<=E_a(R)<=E(R+|a|), either energy hypothesis passes to each fixed
center, with the required remainder order in the precise case. Apply
(3) to U(a+.). Translation of the full Euler equation is not invoked.

## 3. Exact smooth energy construction

Put t=(beta-3)/2, k=t+2=(beta+1)/2. Then -3/2<t<-1 and1/2<k<1.
Let Y=Y_ell be an L2-normalized real zonal spherical harmonic of positive
integer degree ell, Lambda=ell(ell+1). We use only

    integral Y^2=1, integral|grad_S Y|^2=Lambda,
    (1-mu^2)Y''-2mu Y'+Lambda Y=0,
    Y(1)!=0, Y'(1)=Lambda Y(1)/2.

The second integral follows from integration by parts on the sphere;
the last identity is the Legendre equation evaluated at1. All angular
fields below are smooth on the whole sphere, including its poles.
For smooth radial g which vanishes near0 set

    V_g=gY e_r+(rg'+2g)grad_S Y/Lambda.

The radial divergence (rg'+2g)Y/r cancels the spherical divergence,
since Delta_S Y=-Lambda Y. Thus V_g is divergence-free. Its energy
on a radial interval is the integral of
r^2[g^2+(rg'+2g)^2/Lambda].

Choose a fixed smooth chi0 in[0,1], zero for r<=1 and1 for r>=2.
Let g0=chi0 r^t, K_ell=1+k^2/Lambda and b^2=beta L/K_ell.
Define the finite constant

    C_chi=integral_1^2 r^(beta-1)(r chi0'+k chi0)^2dr.

The energy of bV_g0 in B2 is at most
b^2[(2^beta-1)/beta+C_chi/Lambda]. Its desired energy there is
L2^beta=b^2 K_ell 2^beta/beta. If Lambda>2beta C_chi, the deficit D
between desired and actual energy is greater than b^2/(2beta)>0.
Choose nonzero smooth zeta supported in(1/4,1/2) and set
I_ell=integral|V_zeta|^2>0. The field

    U=bV_g0+sqrt(D/I_ell)V_zeta                        (5)

is smooth and divergence-free, zero near0. The summands have disjoint
radial support, so the added energy is exactly D, without cross terms.
For r>=2,

    U=b r^t[Y e_r+a grad_S Y], a=k/Lambda.             (6)

Its sphere energy is b^2 K_ell r^(beta-1)=beta Lr^(beta-1), so the exact
inner fill gives E(R)=LR^beta for every R>=2. Since t<0 and the sphere
field is bounded for each fixed ell, U tends uniformly to0. No estimate
uniform in ell on angular derivatives is asserted.

## 4. Shifted energy and the exact spherical coefficient

The scalar density |U|^2 is even. Indeed both vector terms in V_g
transform by the same sign(-1)^(ell+1) under y mapped to-y. For
E_a(R)=integral_(B_R)|U(a+x)|^2dx the first center derivative at a=0
is zero, by this parity. A second center derivative is

    partial_(a_k)partial_(a_j)E_a(R)
       =integral_(partial B_R) partial_k(|U|^2)(a+x)n_j dS.

For fixed a and large R, the homogeneous tail density has gradient
O_a(R^(beta-4)); hence this derivative is O_a(R^(beta-2)). Taylor's
formula on the segment from0 to a proves
E_a(R)=LR^beta+O_a(R^(beta-2)). No unspecified constant energy offset
is hidden in this estimate.

Write N(r)=integral_(partial B_r)(U.e_r)^2 and T(r)=E'(r).
Equation(3) for radial tests says

    r^2 Q=N''-[(T-N)/r]'.

With A(r)=rN(r)-E(r), this becomes r^3 Q=A''-A'/r. These identities
follow by finite integrations by parts in r; they also hold as
distributions for general C1 fields. For (6), N=b^2r^(beta-1).
Let theta_ell=1/K_ell. Then

    A=(beta theta_ell-1)Lr^beta,
    Q=beta(2-beta)(1-beta theta_ell)Lr^(beta-5)>0,
    H_Q(R)=beta(2-beta)(1-beta theta_ell)L log R+O(1),
    F_tan(R)=beta L(1-theta_ell)log R+O(1).

Thus the leading coefficients attain equality in (1). As ell increases,
theta_ell increases to1 and the H_Q coefficient divided by L tends
to k_beta from above. Arbitrarily large ell satisfies the deficit
condition. Together with the universal lower bound this proves the
stated infimum. Since Q_+ can be strictly smaller than integral q_+
over a sphere, this construction proves no optimality for pointwise
positive part of q.

## 5. Smooth Poisson pressure

A pressure is defined by the Newtonian second-derivative distribution
applied to U_iU_j. In explicit form it is

    P0(y)=-|U(y)|^2/3+(1/(4pi))PV integral
       (3z_i z_j-|z|^2 delta_ij)|z|^(-5)
                                  U_i(y-z)U_j(y-z)dz.

Near z=0 subtract the value of the smooth tensor density at y. The
kernel has zero spherical mean, and the remaining first-order difference
is locally integrable. A distant dyadic annulus contributes at most
C R^(-3)E_y(2R)=O(R^(beta-3)), a summable bound.
On each compact observation set split the tensor into a smooth compact
part and its complement. The first part has a smooth Newtonian pressure;
derivatives of the complementary pressure act on the separated kernel
and the differentiated far tails converge. Hence P0 is smooth.
Truncating the tensor at increasing radii gives local convergence of
pressures and distributional convergence of their Laplacians, so
-Delta P0=partial_i partial_j(U_iU_j)=q. This does not establish momentum.

## 6. Failure of full momentum for every c and omega

The field (5) is axisymmetric in the vector sense. Consequently
(Jy.grad)U=JU and the two rotation terms cancel for every omega.
In its homogeneous exterior, curl of any supposed full momentum
identity with C1 pressure would give

    (1-c+ct)Omega+curl[(U.grad)U]=0.                  (7)

The first term has radial degree t-1 and the second2t-2, which are
different. The smooth momentum residual would have zero distributional
curl if it were a C1 gradient, so (7) is a necessary ordinary identity.
The exterior vorticity is

    Omega_phi=b d r^(t-1)partial_theta Y,
    d=a(t+1)-1<0.

It is nonzero for positive ell. At any direction where it is nonzero,
varying r in (7) forces1-c+ct=0. Equation(7) would then require the
nonlinear curl to vanish everywhere in the exterior. The forced value
of c is2/(5-beta), but the following contradiction also excludes it.

Put rho=r sin theta, mu=cos theta, and
zeta_v=Omega_phi/rho=-b d r^(t-2)Y'(mu). Direct differentiation gives

    U.grad zeta_v=-b^2 d r^(2t-3)Y'
                            [(t-2)Y+a(1-mu^2)Y'']
                 =-b^2 d r^(2t-3)Y'[-4Y+2a mu Y'].

The second equality uses aLambda=k=t+2 and the Legendre equation.
At mu=1 the factors Y' and the bracket have nonzero limits, namely
Lambda Y(1)/2 and(k-4)Y(1). Therefore the expression is nonzero at
some points off but near the axis. For an axisymmetric no-swirl field,
the azimuthal component of curl[(U.grad)U] equals
rho U.grad(Omega_phi/rho): the term (Omega.grad)U subtracts exactly
Omega_phi U_rho/rho from U.grad Omega_phi. Thus that nonlinear curl
is nonzero, a contradiction. This excludes every real c, every omega
and every C1 pressure, including harmonic additions to P0.

## 7. Euler interpretation and evidence boundary

Here the full profile system means

    (1-c)U+(((cI-omega J)y+U).grad)U+omega JU+grad P=0,
    div U=0, J(y1,y2,y3)=(-y2,y1,0).

For a bounded C1 velocity and C1 pressure solving this system, assume Hb: U(R.) tends to0 in distributions. If2/5<c<1/2
and U is nonzero, A3053 supplies the precise energy law with
beta=5-2/c and L>0. Therefore (1) is a necessary condition for every
finite omega, with spherical-source weight4-beta=2/c-1. Finite total
critical spherical-source moment at any center forces U=0 and constant
pressure. The tangential term is a nonnegative refinement. No symmetry
of an actual profile is assumed in this necessary condition.

All six source sections,32manual checks, formal-source note and reading
record were read and retained. The proof above uses no mathematical
computation or formal build. It is independent of pending versions of
other source results: (3), radial integration, the Legendre equation and
energy filling suffice. The complete A135 comparison is retained and checked
in Sections 8-9. Its symbolic diagnostics are not used as proof evidence.
Kinematic sharpness is not a rotating Euler counterexample, a full-profile
optimality statement or a proof of the unrestricted conjecture.


## 8. Signed-pairing slack and the full comparison

The complete A135 comparison, retained as in the team records,
agrees with Sections 1-7. In particular, the cutoff derivatives are supported
on one annulus, the positive-part operation is taken after spherical
integration, and the exact compact energy fill uses disjoint supports.
The comparison's Z1 has the following precise content. Write m=2-beta and

    S(R)=integral q(y) f(y)chi(y/R)dy,
    H_chi^plus(R)=integral_2^infinity chi(r/R)r^(4-beta)[Q(r)]_+dr,
    H_chi^minus(R)=integral_2^infinity chi(r/R)r^(4-beta)[-Q(r)]_+dr.

The part of the main Hessian on R<r<2R is bounded by
m R^(-beta)E(2R)=O(1), as are the cutoff derivatives and the fixed inner
terms. Equation (4), without discarding the tangential energy, therefore gives

    S(R)=m[(1-beta)F(R)+beta F_tan(R)]+O(1).

Under the precise energy remainder this is

    S(R)=k_beta L log R+beta m F_tan(R)+O(1),
    H_chi^plus(R)=k_beta L log R+beta m F_tan(R)
                                      +H_chi^minus(R)+O(1).             (8)

Under the ratio limit the displayed O(1) after replacing F by beta L log R
must instead be o(log R). No derivative of the energy remainder is taken.
If integral_2^infinity r^(4-beta)[-Q(r)]_+dr is finite, (8) and

    H_Q(R)-C<=H_chi^plus(R)<=H_Q(2R)

imply H_Q(R)=k_beta L log R+beta m F_tan(R)+O(1). For the lower bound use
(8) at R/2 and F_tan(R)-F_tan(R/2)=O(1); for the upper bound use (8) at R.
The ratio-only version has error o(log R). This proves the stated slack
interpretation and its exact boundary between additive and asymptotic errors.

Z3 is also valid. The two radial degrees in (7) are distinct since t!=1,
so both curl terms vanish separately if (7) holds for all exterior radii.
In fact d=a(t+1)-1<-1 because a>0 and t+1<0. When beta=5-2/c, the forced
value c=2/(5-beta) is already the prescribed c, and the linear tail term
vanishes. The remaining steady Euler vorticity equation still fails by the
nonzero expression in Section 6. No case of real c or finite omega is omitted.

## 9. Attainment at each positive tangential fraction

Here is the justified portion of A135's Z2. Fix tau in (0,1], let
vartheta=1-tau in [0,1), and choose ell large enough that
vartheta<=1/K_ell and Lambda>2beta C_chi. In addition to V_g of Section 3,
set W_h=h(r)e_r cross grad_S Y. It is divergence-free, because it is
tangential and div_S(e_r cross grad_S Y)=0. It is pointwise orthogonal
to V_g. With the same chi0 and g0, put

    h0=chi0 r^t/sqrt(Lambda),
    b_p^2=beta vartheta L,
    b_t^2=beta L(1-vartheta K_ell).

These numbers are nonnegative and not both zero. The tail of
b_p V_g0+b_t W_h0 has sphere energy
(b_p^2 K_ell+b_t^2)r^(beta-1)=beta Lr^(beta-1), and radial sphere energy
N(r)=b_p^2 r^(beta-1)=beta vartheta Lr^(beta-1).
Its energy in B2 is at most

    b_p^2[(2^beta-1)/beta+C_chi/Lambda]
                             +b_t^2(2^beta-1)/beta.

The target energy L2^beta equals
(b_p^2 K_ell+b_t^2)2^beta/beta. Thus the deficit D' is at least

    b_p^2[1/beta-C_chi/Lambda]+b_t^2/beta>0.

Fill it by adding sqrt(D'/I_ell)V_zeta, using the same disjoint compact
support as Section 3. The resulting U is smooth, divergence-free,
uniformly decaying and satisfies E(R)=LR^beta for all R>=2. The radial
identity in Section 4 now gives

    Q(r)=beta m(1-beta vartheta)Lr^(beta-5)>0,
    F_tan(R)=beta L tau log R+O(1),
    H_Q(R)=beta m(1-beta+beta tau)Llog R+O(1).            (9)

Conversely, (1) implies that any field in the precise energy class with
F_tan(R)/(beta Llog R) tending to tau has

    liminf H_Q(R)/(Llog R)>=beta m(1-beta+beta tau).

The constructed field attains this bound as a limit. This proves the
minimum at every fixed positive tangential fraction; it uses no Euler
momentum identity. The same conclusion holds about every fixed center
for this construction. To check this, note that poloidal and toroidal
summands have opposite parities, but are pointwise orthogonal. The
compact fill has disjoint support from both exterior summands. Therefore
|U|^2 is even, and the second-center-derivative estimate of Section 4 gives
E_a(R)=LR^beta+O_a(R^(beta-2)). In the homogeneous tail,
|grad q|<=C r^(beta-6), so the change of Q at a shifted center, including
the positive part, contributes at most C_a integral^R r^(-2)dr=O_a(1)
to H_Q. The radial projection changes by O_a(r^(-1)), and translating U
changes it by O_a(r^(t-1)). Hence the change in the weighted tangential
energy density after radial integration is O_a(r^(-2)), also integrable.
The pressure construction of Section 5 applies unchanged.

Two qualifications in the first A135 version are essential. As tau tends
to zero, this family approaches k_beta. It does not decide whether some
other single field attains k_beta at tau=0. For ell=1 and vartheta=0 its
exterior is the pure-swirl tail used in LIT373, but its compact poloidal
fill need not be that earlier entire field. No full momentum claim for
these mixed controls is needed or certified here.

Finally, A135's closing statement that k_beta is not optimal for pointwise
q_+ is not justified by LIT376 and conflicts with the independent LIT377
audit A3118. The correct scope is that this spherical construction does
not establish pointwise optimality; A3118 establishes it by a different
construction. Optimality within the full Euler class remains open.
