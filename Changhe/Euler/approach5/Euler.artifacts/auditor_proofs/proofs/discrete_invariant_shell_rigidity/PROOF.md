# Discrete carrier invariance and regular basin rigidity

## Exact statements

Let c>0, omega real, J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, and B=Ay+U, where U is C1, bounded and divergence free on R3. Write Phi_t for its complete flow. Let T>0, E be open with Phi_T E contained in E, and f:E->R continuous with f(Phi_T y)=f(y). If for every rho>1,

    R^-3 integral_(E intersect {R<|y|<rho R}) |f(y)| dy ->0,

then f=0 on E. No profile equation is needed for this statement. In fact one sufficiently large shell ratio depending on cT suffices.

Now let 0<c<1/2, omega arbitrary, U C2 and P C1 solve the Euler profile equation, with U bounded and U(R.) tending to zero in distributions. Put Omega=curl U and H=P+|U|^2/2+Ay.U. Let Lambda be a compact transitive locally maximal uniformly hyperbolic attractor for the backward flow Psi_t=Phi_-t, with no zeros of B, Omega or B cross Omega. Assume the regular-attractor structure of A115: its open invariant basin V is the union of the complete strong stable leaves through Lambda, and those leaves are the complete Omega curves. If U.Omega=0 on V, then H is constant on V. No mixing assumption is needed.

For a uniformly decaying profile, if such basins cover almost every vortical point and each has U.Omega=0, then U=0. By A283 one may instead assume helicity has one sign on each basin, with different signs allowed for different basins.

## Discrete invariant shell lemma

Let M=||U||_infinity. Linear growth and local regularity give a complete flow with determinant exp(3ct). For r=|Phi_t y| away from zero,

    cr-M <= r' <= cr+M.

Any point with radius greater than M/c escapes to infinity. Hence the set K of points with bounded forward orbit lies in the closed radius-M/c ball. It is measurable (express boundedness by countably many time and radius tests) and invariant. Its finite volume satisfies |Phi_t K|=exp(3ct)|K| while Phi_t K remains in that ball. Thus |K|=0.

If f is nonzero, choose eps>0 such that E'={y in E:|f(y)|>eps} is nonempty. It is open and forward Phi_T invariant. It contains an escaping point. After an integer multiple of T, choose a small ball D contained in E', with all its radii between R1 and 2R1 and R1>=2M/c. Such a choice is possible by moving sufficiently far out. The radial inequalities integrate to

    exp(ct)(r(0)-M/c)+M/c <= r(t)
       <= exp(ct)(r(0)+M/c)-M/c.

Consequently, for rho_n=exp(cnT)R1/2,

    Phi_(nT) D contained in {rho_n<|y|<5rho_n},
    |Phi_(nT) D|=8 R1^-3 |D| rho_n^3.

Every image remains in E'. Therefore along the radii rho_n the normalized shell integral with ratio5 is at least 8 eps R1^-3 |D|>0. This contradicts the assumed limit. This subsequence proof is enough and avoids any need to fill the gaps between successive shells. It also handles M=0. The original all-large-R version in CO22 is valid, but unnecessary.

## Euler shell mean

A052, with its proof in the team records, is explicitly under bounded distributionally vanishing dilates. It gives U=0 for c<2/5, bounded E(R)=integral_B_R|U|^2 at c=2/5, and E(R)<=C R^beta for c>2/5, beta=5-2/c<1. Thus in every nontrivial case E(R)<=C R^beta for some 0<=beta<1.

Cauchy-Schwarz gives, for fixed rho>1,

    integral_(R<|y|<rho R) |U.B|
       <= ||A|| rho R |B_(rho R)|^(1/2) E(rho R)^(1/2)+E(rho R)
       <= C_rho [R^((5+beta)/2)+R^beta].

After division by R^3 both terms tend to zero. This uses no pointwise pressure decay and no new boundary term.

## Weak stable density and the basin theorem

Use the local-product consequence already checked in A267: the weak stable set of any periodic orbit is dense in a transitive basic hyperbolic set. Here is the argument needed. Choose a dense forward orbit z, first close to a prescribed target and later arbitrarily close to a periodic point p. The local product of the later point's strong unstable plaque with p's center-stable plaque lies in Lambda. Pull it back to the earlier time. Strong unstable contraction makes it arbitrarily close to the target, while it remains in the weak stable set of p's orbit. The basic-set hypotheses supply the returns and a periodic orbit. This is a statement about a regular transitive basic set; no assertion is made for an arbitrary nontransitive hyperbolic ambient set.

The Lamb identities are

    Omega.grad H=-(1-2c) U.Omega,
    B.grad H=-(1-2c) U.B.

The helicity hypothesis makes H constant along each complete Omega curve, hence each strong stable leaf in V. Let p be a periodic point of Psi with period L>0. On every strong stable leaf through Psi_s p, flow invariance of the leaves gives

    H(Psi_(t+L) y)=H(Psi_(t+L+s) p)=H(Psi_(t+s) p)=H(Psi_t y).

Density of their union in Lambda and continuity give H composed Psi_L=H on Lambda. Every point of V belongs to a strong stable leaf through Lambda; constancy on these leaves extends the equality to V. Equivalently H composed Phi_L=H on V.

Differentiate this equality along B. The function f=U.B is continuous and Phi_L invariant on V. The Euler shell estimate and the discrete shell lemma imply f=0 on V. Therefore B.grad H=0 there as well. On the weak stable set of p's orbit, H then equals H(p): it is constant on the periodic orbit by B.grad H=0 and on its strong stable leaves by the helicity identity. Density gives the same value on Lambda and then on V. This proves the theorem.

Under decay, the covering conclusion follows from A265-A266, the independently proved arbitrary-boundary Bernoulli localization theorem. Its hypotheses are precisely open constant-H regions covering almost every point with Omega!=0; the constants need not initially agree. A283 supplies the optional one-sign replacement because each V is invariant under the complete vortex flow.

## Scope and verification

CO22 is confirmed with the stated regular-attractor structure, the helicity premise and separate coverage retained. The discrete lemma works for all c>0. The Euler application uses 0<c<1/2. This independently checks the configured-model coordinator's argument; no new model call or claimed provider attestation is involved. It does not certify existence or coverage of regular basins or the helicity condition. No numerical computation or formal build is used.
