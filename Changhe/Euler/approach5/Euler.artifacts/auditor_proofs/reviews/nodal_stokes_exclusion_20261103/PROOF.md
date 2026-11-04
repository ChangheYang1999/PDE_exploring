# Stokes excludes the proper regular nodal annuli

Status: CONFIRMED A883-A886 under the exact actual-profile hypotheses below. The bounded noncompact parallel equilibrium curve remains OPEN, A887.

## 1. Statement and checked inputs

Let 2/5<c<1/2, omega in R, Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, kappa=1+c and p=(1-c)/c. Suppose U in C2(R3;R3) and P in C1(R3) satisfy

    div U=0,
    ((1-c)I+omega J)U+DU(Ax+U)+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

for a finite C. Put B=Ax+U, Omega=curl U,

    H=P-Pinf+|U|^2/2+(Ax).U,
    Q=P-Pinf-|U|^2/2,

where Pinf is the actual pressure limit. Let Phi, Gamma, K, E, Xi, O and L have the precise definitions in the team records. In particular Xi is the actual C1 scattering diffeomorphism from the escaping set E onto R3 minus {0}; L extends k composed with Xi across original vortex excursions, where k(z)=(Az).V(z).

Let M be a nonempty connected component of

    {y in O:L(y)=0, dL(y)!=0, Omega(y)!=0}.

The confirmed A810-A818 and A878-A881 give a connected C2 invariant surface on which

    H=Q=0, N=grad H!=0, U=bN,
    B cross Omega=fN, f=1+ab,
    b!=0 constant, D2Q=0,
    2|sym DU|^2=U.curl Omega.

Then necessarily f=0 and the connected equilibrium curve P0={B=0} intersect M is noncompact. Thus the nonparallel branch is impossible for every omega. A parallel branch with compact P0 is also impossible.

This excludes these specified regular nodal sheets, not every carrier periodic orbit or every common zero of the actual tails. The global helicity and natural derivative hypotheses remain explicit.

## 2. A surface Stokes obstruction

Orient M by n=N/|N|. The last pointwise identity in Section 1 becomes

    curl Omega.n=2|sym DU|^2/(b|N|).                   (1)

Its sign is constant. Suppose there are increasing compact domains D_R in M, exhausting M, with C1 boundaries and boundary circulations tending to zero:

    integral_boundary(D_R) Omega.dx -> 0.             (2)

Stokes applies to the C1 field Omega on a C2 surface with C1 domain boundary. Equivalently one can approximate each C1 boundary inside a surface chart; the field and its exterior derivative are continuous. Multiplication by sign(b) gives

    integral_D_R 2|sym DU|^2/(|b||N|) dA
       =sign(b) integral_boundary(D_R) Omega.dx.

For any fixed compact surface patch D, the nonnegative integral over D is bounded by the right side for all large R. Equation (2) makes it zero. Continuity and positivity of |N| at every point force sym DU=0 throughout M. No total-area or a priori integrability condition is needed.

Along a complete B orbit in M the vorticity equation is

    d_t Omega=(DU-I-omega J)Omega.

Since sym DU=0 there, its squared norm obeys

    d_t |Omega|^2=-2|Omega|^2,
    |Omega(Phi_t y)|=exp(-t)|Omega(y)|.

Every backward B orbit is contained in a compact ball. Indeed outside a sufficiently large ball y.B>=c|y|^2-||U||infinity |y|>0, so the reversed field points inward. The displayed growth as t tends to negative infinity contradicts continuity of Omega on that ball when Omega(y)!=0. Thus no such exhaustion can exist for M.

## 3. The actual scattering map controls boundary length

For |y| sufficiently large, forward radial comparison gives

    |Phi_t y|>=exp(ct/2)|y|, t>=0.

With z_t(y)=exp(-tA)Phi_t y, the integral equation gives

    z_t(y)-y=integral_0^t exp(-sA)U(Phi_s y) ds
              =O(|y|^(-p))

uniformly in t. For F_t=D z_t the variational equation is

    F_t'=C_t F_t, F_0=I,
    C_t=exp(-tA)DU(Phi_t y)exp(tA).

The scalar exponential factors cancel in this conjugation, leaving orthogonal rotations. Hence

    |C_t|<=C |y|^(-p-1)exp(-(p+1)ct/2).

Its time integral is O(|y|^(-p-1)). Gronwall and the integral equation for F_t-I therefore give

    Xi(y)=y+O(|y|^(-p)),
    D Xi(y)=I+O(|y|^(-p-1)).                           (3)

The actual C1 existence of Xi is already a checked input; no derivative of a merely pointwise limit is taken. For all y in E, boundedness of U also gives the global estimate

    |Xi(y)-y|<=||U||infinity/c.                        (4)

Consequently |z| large forces |Xi^(-1)z| large and comparable to |z|. By (3), |D Xi^(-1)(z)|<=2 there after increasing the radius.

If gamma is a fixed C1 closed angular curve on S2, define its twisted radius-R copy by

    gamma_R=exp((log R/c)A)gamma.

It has length R length(gamma), since the linear map is R times an orthogonal rotation. The actual curve C_R=Xi^(-1)(gamma_R) has length at most 2R length(gamma). Its points have radius comparable to R, so the natural derivative bound gives |Omega|<=C R^(-p-1). Therefore

    |integral_C_R Omega.dx|<=C_gamma R^(-p) -> 0.       (5)

This uses no asymptotic estimate for D Omega and no second derivative of Xi.

## 4. The nonparallel annulus

Suppose f!=0. A815-A818 gives a properly embedded annulus with one carrier cycle C0 and K intersect M=C0. In global coordinates theta modulo a period T and zeta in R,

    B=partial_theta+kappa zeta partial_zeta,
    Omega=partial_zeta.

A863 gives two closed embedded C1 angular curves gamma_plus and gamma_minus. Each component zeta>0 or zeta<0 maps under Xi onto the entire twisted cone over its curve.

Cut each cone at radius R, keep its inner part, and include C0. This defines D_R with two boundary curves of exactly the form in Section 3. To verify that these are compact annular domains rather than only bounded subsets, set

    r_epsilon(theta)=|Xi(j(theta,epsilon))|, epsilon=+1,-1.

These continuous positive functions on a circle have a common positive lower bound and a finite upper bound. Carrier equivariance gives

    |Xi(j(theta,zeta))|
       =|zeta|^(c/kappa)
          r_epsilon(theta-log|zeta|/kappa).

Thus this radius tends uniformly to zero as zeta tends to zero and uniformly to infinity as |zeta| tends to infinity. The retained parts contain a neighborhood of C0 and lie in a compact parameter annulus. They are closed there, so they are compact. The boundary is regular C1 because the derivative of |Xi| along B is c|Xi|, nonzero at radius R. There is no boundary or seam at C0.

The domains increase and exhaust M. Equation (5) makes both boundary circulations tend to zero, regardless of their induced orientations. Section 2 is a contradiction. Hence f!=0 is impossible.

## 5. A compact parallel equilibrium curve

Suppose f=0 and P0 is compact. A865 gives the global product

    j:P0 times R -> M, j(q,zeta)=Gamma_zeta q,
    B=kappa zeta partial_zeta, Omega=partial_zeta.

P0 is a connected compact embedded one-dimensional manifold without boundary, hence a circle. A881, now confirmed independently of this argument, says both nonzero-sign halves lie in E. The two angular components are therefore closed C1 curves, each homeomorphic to P0.

For epsilon=sign(zeta), exact equivariance gives

    |Xi(j(q,zeta))|
       =|zeta|^(c/kappa)|Xi(j(q,epsilon))|.

The last factor is continuous and positive on compact P0, so it has uniform positive lower and finite upper bounds. Thus |zeta| tending to infinity forces |Xi(j(q,zeta))| to infinity uniformly in q. Estimate (4) then forces the actual position to infinity. For bounded zeta the image of P0 times a bounded closed interval is compact. This proves properness of the product embedding and the annular topology.

The same radius cuts as in Section 4 give compact annuli exhausting M, with C1 regular boundaries and no interface at the equilibrium circle. Each boundary satisfies (5). Section 2 again contradicts Omega!=0. Hence a compact P0 is impossible.

## 6. Verification and remaining scope

LIT187's complete six-section source was read. The pressure-flatness dependency is now CONFIRMED A878-A881, so this result no longer has an unconfirmed LIT186 premise. The variational estimate, inverse-map control, actual curve lengths, compact exhaustion, orientation sign and backward-flow contradiction were independently checked above. Exact source pins and hashes are retained beside this proof. No computation or formalization was required.

The conclusion supersedes the nonparallel and compact-parallel alternatives left OPEN in A882. The remaining regular nodal possibility is a parallel sheet over a bounded noncompact embedded equilibrium curve P0, with both vortex signs escaping. It does not supply an exhaustion with only two compact boundary circles. Its missing ambient equilibrium-curve endpoints may lie in the joint core and be irrotational with nonzero D Omega. This proof neither excludes such endpoints nor establishes their existence.

Critical vortical nodes, open nodal regions, nonzero helicity and removal of the derivative premise remain outside this result. The general decay-only conjecture remains OPEN. Comparison continues through existing configured model working files; provider runtime is not independently attested. No new client or agent is used.
