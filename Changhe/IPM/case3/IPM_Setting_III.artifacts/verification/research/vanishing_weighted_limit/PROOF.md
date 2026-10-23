# Exact strain and weighted residual of a vanishing non-profile family

Date: 2026-10-20. Independent implementation checks passed 2026-10-20T19:58:40.965559+00:00. Status: complete independent analytic argument; implementation
checks are recorded separately. This extends results47 and53. It concerns
explicit non-solutions and does not classify a numerical continuation branch.

## Statement and hypotheses

For 0<D<=1 put ell=1+D, eta=D/(1+D), a=4D and r=|X|. Define

    f(r)=(1+r^2)^(-eta/2), H(r)=integral_0^1 u^3 f(ur)du,
    rho_D=a y f(r), psi_D=-a x y H(r), U_D=(-psi_y,psi_x),
    h_D=rho_D-a y, F_D=(ell X+U_D).grad rho_D-rho_D.

Result47 proves smoothness, the prescribed parities and growth, the canonical
full-plane inverse, and the exact nondegenerate center relations a=4D and
psi_xy(0)=-D. The same result proves F_D is not identically zero for any D>0.
The following identities and limit strengthen that manufactured example:

    sup |sym DU_D|_op = D,
    sup_{X!=0} (-X.U_D/r^2) = D,
    X.(ell X+U_D) >= r^2,                                (1)

and, for the full-plane norm ||g||_m^2=integral g^2 r^(-2m)dX,

    h_D/D^2 -> G=-2y log(1+r^2),
    F_D/D^2 -> J=-4y r^2/(1+r^2)                          (2)

strongly in this weighted L2 space for every fixed 2<m<4. In particular,

    ||F_D||_3/||h_D||_3 -> 2sqrt(3)/pi.                   (3)

The limit in (3) is positive. It is unchanged by any positive D-dependent
spatial dilation. These statements do not assert weighted norm convergence
of the dilated functions themselves. They distinguish the strain cap and
small pointwise relative residuals from the full transport equation.

## Exact global strain, without a sampled maximum

Write f'=df/dr and set

    L(r)=r f'-6f+24H, K(r)=2f+r f'.

The identity rH'=f-4H from result47 also gives
r^2H''-rH'=L. Directly differentiating U gives, with theta=arg(X),

    S_11=(a/8)(K-L cos(4theta)),
    S_12=-(a/8)L sin(4theta), S_22=-S_11,
    S=sym DU.                                           (4)

For example S_11=a(H+rH'+x^2y^2 L/r^4), and
S_12=a xy(y^2-x^2)L/(2r^4), which verify the factors in (4).
The apparent polar expressions extend to r=0 by smoothness.

Let t=r^2, nu=eta/2, and P(t)=(1+t)^(-nu). Then

    f=P(t), r f'=2tP'(t), H=(1/2)integral_0^1 uP(tu)du.

The function P is positive, decreasing and convex, and 0<nu<=1/4.
Convexity gives both a tangent bound and a chord bound on 0<=u<=1:

    P(tu)>=P(t)+t(u-1)P'(t),
    P(tu)<=(1-u)P(0)+uP(t).

After multiplication by u and integration, these imply

    H>=P(t)/4-tP'(t)/12,
    H<=1/12+P(t)/6.                                     (5)

The first bound makes L=2tP'-6P+24H nonnegative. Also
K=2P[1-nu t/(1+t)]>0. Since a>0, (4) therefore yields

    max_theta |S|_op=(a/8)(K+L)
        =a(3H-f/2+r f'/4)<=a/4.                         (6)

The last step uses the second bound in (5) and r f'<=0.
At the origin f=1,H=1/4 and r f'=0, so S=diag(a/4,-a/4).
Thus the first equality in (1) follows exactly, including attainment.
This proof in fact works for 0<eta<1 with a=4D; the narrower range above
is the range already used by the manufactured family.

The velocity formula also gives

    X.U_D/r^2=aH(r)cos(2theta).

Here 0<H<=1/4 with limit 1/4 at the origin. Consequently the supremum of
its negative is a/4=D. Adding ell=1+D proves the remaining statements
of (1). The supremum for X!=0 is obtained as a limit along the vertical
axis. It need not be attained away from the origin.

## Whole-plane weighted convergence

On compact sets, smooth dependence on eta and eta/D->1 gives

    (f-1)/D -> -log(1+r^2)/2.

Moreover 0<=1-exp(-u)<=u for u>=0, hence

    |h_D/D^2|=4|y||f-1|/D<=2|y|log(1+r^2).              (7)

The square of the right side times r^(-2m) is integrable over the plane:
near zero its polar integrand is O(r^(7-2m)), and at infinity it is
O(r^(3-2m)log^2 r). These are integrable for 2<m<4.
Equation (7), the pointwise limit, and dominated convergence prove the
first limit in (2).

For completeness an exact residual expression with a removable origin
singularity is

    F_D/D^2=4y f[(1-q)-4H-4(x^2/r^2)(f-4H)
                       -4eta(x^2-y^2)H/(1+r^2)],
    q=r^2/(1+r^2).                                      (8)

It follows by multiplying the explicit velocity and density gradient;
no equation of motion is imposed. To see its uniform regularity at zero,
write H(r)=b(t), t=r^2. Then f-4H=2t b'(t), and the bracket equals

    B_0(t)+x^2 B_2(t),
    B_0=1/(1+t)+(-4+4eta)b-4eta b/(1+t),
    B_2=-8b'-8eta b/(1+t).                              (9)

On 0<=t<=1 and 0<=eta<=1/2, b and its first two derivatives are bounded
uniformly, directly by differentiating its integral. Since B_0(0)=0,
(9) gives |B_0+x^2B_2|<=Ct there. On r>=1, formula (8) gives a uniform
constant bound: f<=1, H<=1/4, |f-4H|<=2, eta<=1/2 and
|x^2-y^2|/(1+r^2)<=1. Combining the two regions,

    |F_D/D^2|<=C|y|min(r^2,1).                          (10)

At eta=0, f=1 and H=1/4, so (8) tends to -4yq=J.
The squared majorant in (10), times r^(-2m), has polar behavior
r^(7-2m) at zero and r^(3-2m) at infinity. It is integrable for precisely
the required open range 2<m<4. A second application of dominated
convergence proves the second limit in (2). This treats the infinite
domain and both axes; compact convergence alone would not suffice.

## Exact limiting norms and dilation

At m=3, direct polar integration and t=r^2 give

    ||G||_3^2=2pi integral_0^infty log^2(1+t)/t^2 dt,
    ||J||_3^2=8pi integral_0^infty (1+t)^(-2)dt=8pi.

Integrating the first radial integral by parts has zero boundary terms
at both endpoints and gives

    integral_0^infty log^2(1+t)/t^2 dt
       =2 integral_0^infty log(1+t)/(t(1+t))dt
       =2 integral_0^1 -log(1-u)/u du
       =2 sum_{n>=1}1/n^2=pi^2/3.

The series interchange is justified by nonnegative terms. The last
identity is the classical Basel sum. Thus ||G||_3^2=2pi^3/3>0.
Taking ratios in the strong limits (2) proves (3).

Under the genuine spatial dilation rho_lambda(X)=lambda rho(X/lambda),
the slope a remains fixed, h_lambda=lambda h(X/lambda), and
F_lambda=lambda F(X/lambda). Both weighted norms scale by lambda^(2-m),
so their ratio is unchanged even for a D-dependent choice of lambda.
The strain and radial compression in (1) are also unchanged.

## Dependencies, verification and scope

The canonical inverse and nonexactness are the explicit calculations of
result47. Equation (8) is also used in result53, but the weighted
convergence proof here requires no derivative-energy theorem. The exact
strain calculation independently verifies the cap stated in the weighted
review's non-profile example. The new weighted residual limit is not
inferred from that review.

Independent implementation checks reconstruct the Cartesian strain,
the residual, angular integration and limiting radial integrals. Those
checks support the displayed calculations; the global estimates (5),
(7) and (10) supply the proof. Numerical quadrature values, if reported,
are not interval bounds. No exact primary profile is constructed or
excluded by this result. In particular a family of non-profiles with
sigma=D does not prove sigma<=D for solutions.
