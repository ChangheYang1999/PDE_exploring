# Remaining global-source estimates and resolvent qualifications

Date:2026-10-20. Status: CONFIRMED by independent verification of lead gsrc1 Sections3,7-9.
Actual Opus39 returned no audit text; no external endorsement is claimed. No full nonexistence or existence conclusion.

## Setting and assertions

Use the smooth class-A B2 setting with beta>2, a0=1 and W=beta X+V,
V(0)=0, div W=2beta, Omega=-curl V. Assume0 is the only zero of W.
Put nu=1/beta, lambda=(beta-2)/2, mu=1+3beta/2 and gamma=lambda/beta.
Packets33 and48 give DV=O(r^{-nu}), V=O(r^{1-nu}), complete backward
convergence to0, and a smooth global weak coordinate xi with

    Theta=xi^2, W.grad xi=lambda xi, sign xi=sign x,
    grad xi nowhere zero.

Let phi_t be the flow of W. Write the axis functions A=Theta_xx/2,
q=Omega_x and b=W2, all evaluated at x=0. Then:

1. |grad xi|<=C(1+r)^{gamma-1} and
   |xi|<=C|x|(1+r)^{gamma-1}. The absolute scalar resolvent

       R(X)=int_0^infinity e^{-t}|Theta_x(phi_{-t}X)|dt

   obeys R<=C|x| on compact sets and R<=C|x|r^{-1-nu} for large r.

2. Positive constants A_+,A_-,q_+,q_- exist with, as s->infinity,

       A(+-s)=A_+- s^{-1-2nu}(1+O(s^{-nu})),
       q(+-s)=q_+- s^{-1-nu}(1+O(s^{-nu})).              (1)

   The axis integrals satisfy

       int_R (b'-beta)A=(2/3)int_R A,
       int_R [1-2(b'-beta)]q=2int_R A.                 (2)

3. For L>0 define Fomega(L)=int_R Omega(L,y)dy,
   Ftheta(L)=int_R Theta(L,y)dy,
   J(L)=int_R V1(L,y)Omega(L,y)dy. These are absolutely convergent and

       beta L Fomega(L)+J(L)
         =Ftheta(L)+(2beta-1)int_0^L Fomega(s)ds.       (3)

4. Set K=xy/r^4 and c=Psi_xy(0). Then

       c=(1/pi)int_0^infinity e^{(2beta-1)t}
                     int_R2 K(phi_tZ)Theta_x(Z)dZdt.  (4)

   This double integral is absolutely convergent. Its integration by
   parts version is valid only as the limit of finite time integrals:

       c=-(1/pi)lim_{T->infinity}int_0^T e^{(2beta-1)t}
                   int_R2 Theta(Z)partial_x[K(phi_tZ)]dZdt. (5)

   No absolute convergence in infinite time is asserted for(5).

5. The vector integrals

       E_T=int_0^T e^{-(beta-1)t}(phi_t)_* e1 dt

   satisfy E_T.grad Theta->Omega, absolutely for the scalar contraction,
   but this fact does not imply convergence of E_T. Even C1 convergence
   near0 would require the additional center condition

       W2_xx(0)=0, equivalently b''(0)=-4/beta.          (6)

   That condition is not inferred for B2 profiles. It is necessary for
   the proposed vector limit, not for the scalar resolvent or the PDE.

6. Every level xi=s!=0 is a connected proper line with infinite
   unweighted forward flux int_{xi=s} W.n d sigma, where
   n=grad xi/|grad xi| if s>0. For s<0 reverse the normal to give positive
   flux. Compactness of a cross-section cannot be assumed.

## 1. Backward exterior estimates

Choose a large circle beyond which W.X>=beta r^2/2 and DV=O(r^{-nu}).
For an exterior target X, write X_t=phi_{-t}X until its first backward
hit of that circle, at t=tau. Radial integration gives

    |X_t| comparable to r e^{-beta t}, e^tau comparable to r^nu.

Here the errors are uniform: int_0^tau |X_t|^{-nu}dt is bounded by
a constant determined by the fixed exit radius. The same integral
controls the variational equation, so

    ||D phi_{-t}(X)||<=C e^{-beta t}.

Since V1/x=O(r^{-nu}) (by parity and DV, or packet50), the horizontal
scalar equation gives also |(X_t)_1| comparable to |x|e^{-beta t}.

For a fixed t the eigenfunction identity gives
xi(X)=e^{lambda t}xi(X_t). Differentiate at fixed t first; only then
set t=tau. Bounded grad xi on the fixed circle yields
|grad xi(X)|<=C e^{(lambda-beta)tau}<=C r^{gamma-1}.
Similarly, xi vanishes on the axis and is smooth on the circle's compact
neighborhood, so |xi(X_t)|<=C|(X_t)_1|. This gives the stated bound
for xi. Thus |Theta_x|=|2xi xi_x|<=C|x|r^{-1-2nu}.

## 2. The absolute scalar resolvent

On any fixed compact set, backward convergence to the hyperbolic
source0 is uniform. To justify uniformity, take a small backward-invariant
source disk. Each point of the compact set enters it after finite
backward time. By continuous dependence an open neighborhood enters
by the same time. A finite cover provides a common upper entry time;
backward invariance keeps every trajectory inside thereafter.

In the disk, the horizontal coefficient W1/x is at least lambda/2>0,
so backward horizontal coordinates decay at least as e^{-lambda t/2}.
On the finite initial time interval, |(phi_{-t}X)_1|<=C|x| by its scalar
linear equation. Smooth oddness gives |Theta_x|<=C|x| in the compact
region of these trajectories. Therefore R(X)<=C|x| uniformly on the
initial compact set.

For exterior X, split R at the hit time tau from Section1. Before the
hit, its integrand is bounded by

    C e^{-t}|x|e^{-beta t}(r e^{-beta t})^{-1-2nu}
           =C |x|r^{-1-2nu}e^t.

Its integral is O(|x|r^{-1-nu}). The part after the hit is
 e^{-tau}R(X_tau)<=C e^{-tau}|(X_tau)_1|
                   <=C |x|r^{-1-nu}.
This proves the first assertion and the absolute convergence. The
vorticity resolvent follows by integrating its exact scalar equation
backward: the endpoint e^{-t}Omega(X_t) tends to0 in the bounded
backward region, hence
Omega(X)=int_0^infinity e^{-t}Theta_x(phi_{-t}X)dt.

## 3. Axis tails and their integrated identities

Packet49 proves A,q>0 on the axis and gives

    b A'=(2b'-Lambda)A,
    b q'+(M-b')q=2A,
    Lambda=3beta+2, M=2beta+1.                         (7)

For positive y, b=beta y+O(y^{1-nu}) and b'=beta+O(y^{-nu}). Thus

    A'/A=-(1+2nu)/y+O(y^{-1-nu}).

The error is integrable at infinity; exponentiating its integral gives
the first positive tail constant in(1), with the stated relative
error. For the q equation, let I be a positive integrating factor
with I'/I=(M-b')/b. Then

    I(y)=C y^{1+nu}(1+O(y^{-nu})),
    (Iq)'=2IA/b=O(y^{-1-nu})>0.

The derivative is integrable. Since Iq is already positive, its limit
is finite and strictly positive. Its error from that limit is
O(y^{-nu}), proving the q asymptotic in(1). For y=-s replace b by
-b(-s), obtaining exactly the same ODEs and estimates.

All terms of(7) are integrable on the axis, and bA,bq tend to0 at
both ends by(1). Integrating the first equation by parts gives
3int b'A=Lambda int A; integrating the second gives
int(M-2b')q=2int A. These are exactly(2).

## 4. Vertical strip identity

The undivided vorticity equation is

    div(W Omega)=Theta_x+(2beta-1)Omega.               (8)

Integrate over (0,L) times(-R,R). The left side at x=0 has no flux.
At fixed0<=x<=L the bounds of packet50 give
|Omega(x,+-R)|<=C_L x R^{-1-nu} and |W2|<=C R.
Therefore both horizontal boundary fluxes tend to0 as O(R^{-nu}).
Vertical integrability of Omega,Theta and V1 Omega follows from
Theta=x^2P, Omega=xQ, V1=xv and the bounds in50. Fubini is valid over
this fixed-width strip. Let R grow and use Theta(0,y)=0; equation(3)
follows. Neither an infinite unweighted full-plane mass nor an
unsubtracted center drift is used.

## 5. Strain resolvent and finite-time integration by parts

The center strain identity is c=(1/pi)int K Omega. Its integral is
absolutely convergent by the smooth odd center source and the tail.
By Section2,

    int_R2 |K(X)| R(X)dX<infinity:

near0 the radial bound is Cdr; at infinity it is C r^{-1-nu}dr.
Tonelli therefore permits insertion of the absolute scalar resolvent.
For each t set X=phi_tZ, whose Jacobian is e^{2beta t}. This gives(4)
and proves absolute convergence of its double integral.

For a fixed finite T, integrate the inner expression by parts in Z
on punctured disks. At the inner boundary Theta=O(r^2),
K(phi_tZ)=O_T(r^{-2}) and the line measure is O(r), so the boundary
term is O_T(r). At infinity, |phi_tZ| is comparable to |Z| uniformly
for0<=t<=T; hence the boundary term is O_T(R^{-2nu}). It also tends
to0. The differentiated spatial integrand is integrable: near0 it
is O_T(r^{-1}) with plane measure; at infinity it has radial majorant
C_T r^{-1-2nu}dr. Global boundedness of DW controls Dphi_t on finite
time intervals. This proves the finite-T identity. Taking T->infinity
in the original absolutely convergent form gives(5). The bounds C_T
are not uniform in T, so this argument supplies no infinite-time
absolute bound for the differentiated form.

## 6. Why the vector resolvent can fail

Write Y_t=(phi_t)_* e1=Dphi_t(phi_{-t}X)e1. The temperature transport
identity differentiated in initial data gives

    Y_t(X).grad Theta(X)=e^{(beta-2)t}Theta_x(phi_{-t}X).

Thus E_T.grad Theta is exactly the truncated scalar resolvent.
With the Lie bracket [W,Y]=W.grad Y-Y.grad W, the pushed field obeys
partial_tY_t=-[W,Y_t]. Integration by parts in time gives

    [W,E_T]=e1-(beta-1)E_T-e^{-(beta-1)T}Y_T.           (9)

Deleting the terminal term requires additional control.

For a concrete check, the polynomial field

    W1=lambda x, W2=mu y-2x^2/beta,
    Theta=x^2, Omega=4x/beta

solves both transport PDEs, the center data and Omega=-curl W.
It is not admissible: V has linear and quadratic growth. Its exact
pushed field is

    (Y_t)_1=e^{lambda t},
    (Y_t)_2=8x/[beta(beta+6)]
                         [e^{lambda t}-e^{(beta+2)t}]. (10)

The second integrand defining E_T contains a multiple of-e^{3t}x,
so E_T diverges for every x!=0. The scalar contraction nevertheless
converges to2x int_0^infinity e^{-beta t/2}dt=4x/beta=Omega.
This example refutes only an inference from the scalar contraction,
not any theorem that additionally uses the true sublinear tail.

For an actual profile let ell=W2_xx(0). The second variational equation
along the equilibrium0 gives

    partial_x(Y_t)_2(0)=ell/(2lambda-mu)
                  [e^{lambda t}-e^{(mu-lambda)t}].     (11)

Indeed (D^2phi_t(0)[e1,e1])_2 solves H'=mu H+ell e^{2lambda t}
with H(0)=0, then the initial-point derivative contributes e^{-lambda t}.
Since mu-lambda=beta+2, the second term of the weighted integral of
(11) grows as e^{3t}. Thus C1 convergence of E_T forces ell=0.
Finally divergence gives partial_y W1_x(0)=-b''(0), and
Omega_x(0)=partial_y W1_x(0)-W2_xx(0)=4/beta. This proves(6).
Nothing in this calculation proves ell=0 for the original PDE.

## 7. Infinite unweighted flux on the global sections

Packet48 gives a global diffeomorphism with first coordinate xi.
Therefore {xi=s} is the image of the connected proper line
{(s,eta):eta in R}. Both ends are unbounded and its total arclength
is infinite. Section1 bounds grad xi globally, and for s>0

    W.n=lambda s/|grad xi|>=lambda s/sup|grad xi|>0.

Its integral over the level line is infinite. For negative s use the
opposite normal. A weighted flux may converge, but its end terms
must be computed separately; the unweighted section is not finite.

## Dependencies and scope

Packets33,48 supply the source geometry and asymptotic derivative
control;49 supplies axis positivity and equations;50 supplies quotient
bounds for the vertical strip. Every new integration and terminal term
has been justified above. These arguments verify the corresponding
gsrc1 claims with their stated G scope. They do not prove G empty.

## Audit record

The independent verifier checked the fixed-time differentiation, both exterior
resolvent pieces, the axis integrating factors, the strip top/bottom flux,
the finite-time spatial integration by parts and the exact second variational
equation. Actual Opus39 was requested but returned no written audit on
2026-10-20T17:39:03Z, after25.347409639seconds, model claude-opus-5-5.
This unavailable review supplies no agreement. Lead auditO separately
checks the global gradient and scalar-resolvent estimates; its conclusions
were compared against the explicit derivations above, not taken on trust.
