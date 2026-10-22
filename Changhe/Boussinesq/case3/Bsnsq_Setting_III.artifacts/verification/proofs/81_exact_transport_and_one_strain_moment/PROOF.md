# Exact temperature transport and one strain identity do not certify a profile

Date:2026-10-20. Status: complete independent construction. No profile existence or nonexistence claim.

## Statement

For every beta>2 there are smooth fields Psi,Omega,Theta on the full plane with the following properties:

1. Omega=-Delta Psi and V=(-Psi_y,Psi_x) is the canonical centered full-plane velocity of Omega. Psi and Omega are odd in x, Theta is even in x and vanishes exactly on the vertical axis.
2. V(0)=0, c=Psi_xy(0)=1+beta/2, Theta=a0*x^2 near0 with a0>0, and Omega_x(0)=4a0/beta. Both B2 transport equations hold exactly on a neighborhood of0.
3. W=beta X+V has no zero except0. Every nonzero forward orbit escapes, and every backward orbit converges to0. The temperature equation W.grad Theta=(beta-2)Theta holds exactly on the whole plane.
4. With nu=1/beta, V=O(r^(1-nu)), Omega=mu r^-nu cos(theta) for every sufficiently large r, with mu>0, and Theta=O(r^(1-2nu)), grad Theta=O(r^-2nu). Here theta is the usual polar angle X=(r cos(theta),r sin(theta)).
5. The full-plane strain identity holds exactly:

       pi c=integral Omega V.grad K-(1/2)integral Theta V.grad(partial_x K),
       K=xy/r^4.

6. The vorticity transport equation fails on a whole horizontal interval. Thus these are not B2 profiles.

Positive scaling can set a0=1 without changing any of these conclusions. In particular, the exact temperature equation, canonical inverse, center relations, nonzero slow vorticity tail, global source geometry and this single strain identity together are insufficient to certify the remaining PDE.

## 1. A radial cutoff and a computable vorticity moment

Choose any smooth nonincreasing chi on[0,infinity) with chi=1 on[0,1], chi=0 on[2,infinity), and0<=chi<=1. Set eta=1-chi and

    C_chi=12 integral_1^2 chi(s)(1-chi(s))/s ds
              +9/2+(3/2) integral_1^2 s chi'(s)^2 ds.

This is a finite positive number. Write c=1+beta/2, lambda=beta-c=(beta-2)/2>0 and b0=lambda/16. Choose R>4 so large that

    A_R=12 log R-C_chi>2/b0.                              (1)

For0<=b<=b0 define the compact stream

    Psi_(b,0,0)=c x y chi(r/R)+b r^2 sin(4theta) eta(r)chi(r/R).   (2)

The second term is smooth at0 because eta vanishes on an entire neighborhood there. Every term is odd in x. Put Omega=-Delta Psi and V=(-Psi_y,Psi_x). Then

    N(b,0,0):=integral Omega V.grad K=pi c b A_R.          (3)

Here is a full calculation of(3). More generally write Psi=r^2 a(r) sin(2theta)+r^2 e(r) sin(4theta). Its vorticity coefficients are

    H2=-5r a'-r^2 a'',   H4=12e-5r e'-r^2 e''.

Using V_r=-Psi_theta/r and V_theta=Psi_r, angular integration with K=(1/2)r^-2 sin(2theta) gives

    N/pi=integral_0^infinity [H4(2a/r+a'/2)+H2(-e/r+e'/2)] dr.   (4)

Only the H4-sin4 and H2-sin2 products survive; their angular squared integrals are pi. Integration by parts gives

    N/pi=integral [24ae/r+9(e a'-a e')-3r a'e'] dr.        (5)

For completeness, the difference between the integrands of(4) and(5) is the derivative of

    -2r a e'+r e a'-(r^2/2)a'e'+a e.

It vanishes at both endpoints for the functions in(2). Substitute a=(c/2)chi(r/R), e=b eta(r)chi(r/R). The derivatives of eta and chi(r/R) have disjoint supports. Hence

    N/pi=(cb/2)[24 integral eta(r)chi(r/R)^2 dr/r
                            -9-3 integral r (d_r chi(r/R))^2 dr].

Splitting at1,2,R,2R, using eta=1-chi, and changing r/R to s in the outer part gives(3). All these integrals are over compactly supported integrands, with no singular source at0. In particular N(0,0,0)=0 and N(b0,0,0)>2pi c by(1).

## 2. Exact center data, a slow tail and uniform radial expansion

Add two smooth terms to(2):

    Psi_(b,d,mu)=Psi_(b,0,0)+d x^3 chi(r)+mu Q(r,theta),
    Q=-(r^(2-nu) cos(theta))/((2-nu)^2-1) * eta(r/(4R)).        (6)

Take d<0 and mu>0, both sufficiently small. Q vanishes on r<=4R and is smooth everywhere. For r>=8R,

    -Delta(mu Q)=mu r^-nu cos(theta).                     (7)

For r<1 the stream is exactly cxy+d x^3. Consequently

    W=(lambda x, (beta+c)y+3d x^2), Omega=-6d x,
    a0=-3beta d/2>0, Theta_local=a0 x^2,                  (8)

and both transport equations hold for these local fields: 2lambda=beta-2 and (lambda+1)(-6d)=2a0. Neither b nor mu changes the center jets.

There is a uniform positive radial lower bound. The radial velocity of a stream is -Psi_theta/r, so radial cutoff derivatives do not enter W.radial. The first two terms of(2) contribute at most c r and4b r in absolute radial magnitude. On the support r<=2 of the cubic term its radial contribution is at most6|d|r. The last term contributes at most

    mu r^(1-nu)/((2-nu)^2-1) for r>=4R,

and0 inside. Choose |d|<lambda/48 and mu so small that this last quantity is at most(lambda/8)r. Since4b<=lambda/4, one obtains

    W(X).X >= (lambda/2)|X|^2.                           (9)

The fields are smooth and have at most linear growth, so their flow is complete in both time directions. Inequality(9) makes every nonzero radius increase at least exponentially forward and decrease at least exponentially backward. Thus0 is the only zero, every nonzero forward orbit escapes and every backward orbit tends to0.

The velocity from(6) is sublinear at infinity and zero at0. Its divergence is0 and negative curl is Omega. Since Omega is smooth with the stated decaying tail, its relative full-plane inverse exists. The difference between that inverse and V is harmonic with sublinear growth, hence constant, and is0 at0. Thus V is the canonical relative inverse. There is no extra harmonic strain.

## 3. Global exact temperature transport

The reflection x->-x commutes with W. Its vertical axis is invariant, and a trajectory starting with x>0 never crosses it. For a point Y, choose T>0 large enough that phi_(-T)Y lies in r<1, and define

    xi(Y)=e^(lambda T) [phi_(-T)Y]_1,
    Theta(Y)=a0 xi(Y)^2.                                 (10)

The definition does not depend on any further increase of T: in r<1 the first component satisfies x'=lambda x, and the backward flow remains in that ball by(9). On a compact set of Y and a compact parameter rectangle satisfying(9), one common T works. Smooth dependence of the finite-time flow therefore makes xi smooth in Y and continuous in all parameters. Near0, xi=x exactly. Reflection makes xi odd in x; invariance and uniqueness make xi nonzero with the sign of x off the axis. Thus Theta is positive there and has exactly the required zero set and center polynomial.

The definition also gives xi(phi_tY)=e^(lambda t)xi(Y), proving the temperature equation everywhere. The local vorticity equation was already checked in(8).

The claimed temperature bounds follow from its flow. Outside8R, V=O(r^(1-nu)) and DV=O(r^-nu), uniformly for sufficiently small parameters. Radial expansion gives

    t=(1/beta)log(r/r0)+O(1)

along the orbit from a fixed large circle r0 to radius r, with constants uniform in angle and the chosen compact parameter set: integrate d(log r)/dt=beta+O(r^-nu), whose error has finite time integral by(9). Transport then gives Theta=O(r^(1-2nu)). The gradient solves

    d_t grad Theta(phi_tY)=-(2I+DV(phi_tY)^T)grad Theta(phi_tY).

The integral of |DV| is uniformly finite, so the gradient is O(e^-2t)=O(r^-2nu). On the initial compact circle Theta and its gradient are O(|d|), uniformly in b and small mu, by(10). These same bounds therefore carry the factor |d|.

## 4. Matching the scalar strain identity

For(6),(10) define

    D(b,d,mu)=N(b,d,mu)-(1/2)B(b,d,mu)-pi c,
    B=integral Theta V.grad(partial_x K).

Every integral is absolutely convergent. Near0, N's and B's integrands are O(r^-1). At infinity they are respectively O(r^-2-2nu) and O(r^-2-3nu). These bounds can be chosen uniformly in a small parameter rectangle, using section3. On compact sets the fields and flow depend continuously on the parameters; dominated convergence therefore makes D continuous. At d=0 define Theta=0 by the same formula(10). In particular B=0 there, and B tends to0 uniformly as d tends to0.

The center strain is c for every b,d,mu, since all extra stream terms have zero mixed second derivative at0. At d=mu=0, equation(3) gives

    D(0,0,0)=-pi c<0,
    D(b0,0,0)=pi c(b0 A_R-1)>pi c>0.

Continuity preserves these two strict inequalities for some fixed sufficiently small d<0 and mu>0, while also preserving(9). The intermediate value theorem in b then gives a b_* in(0,b0) with D(b_*,d,mu)=0. This is exactly the strain identity in the statement. The argument needs no assertion that an approximate root solves the full PDE.

## 5. Explicit failure of the remaining equation and normalization

On the annulus2R<r<4R every term of the stream vanishes: the compact parts have ended and the tail has not begun. Hence V=Omega=0 and W=beta X there. The positive temperature satisfies

    Theta(x,0)=C x^(1-2/beta), C>0,  2R<x<4R,

by its exact transport equation along this radial interval. Therefore

    W.grad Omega+Omega-Theta_x
       =-(1-2/beta)C x^(-2/beta)<0                       (11)

on the whole interval. This proves that the constructed fields are not profiles, even though the scalar moment of this residual vanishes by packet79 and the exact temperature equation.

Finally use the exact positive scaling with l=a0:

    Psi_l(X)=l^2 Psi(X/l), Omega_l(X)=Omega(X/l),
    V_l(X)=l V(X/l), Theta_l(X)=l Theta(X/l).

It sets the quadratic temperature coefficient to1 and preserves c, all transport statements, radial expansion and the strain identity. The tail coefficient becomes mu*l^nu>0 and the interval of failure scales by l.

## 6. Normalized pointwise collapse is still possible

Fix beta,R and a sufficiently small mu>0 as above. The strict endpoint signs of D persist for every sufficiently small d<0. For each such d choose any root b_d in[0,b0] supplied by section4, and set l=a0=-3beta d/2. No continuous choice of b_d is needed.

After the positive normalization, all these fields have a0=1, c=1+beta/2 and Omega_x(0)=4/beta. Nevertheless, as d tends to0, their fields tend to0 pointwise throughout the plane and in C1 on every compact annulus avoiding0. Indeed for |X|>8Rl, the compact parts have vanished and the tail is exactly homogeneous, so

    Omega_l(X)=mu l^nu |X|^-nu cos(theta),
    V_l(X)=O(l^nu |X|^(1-nu)), DV_l=O(l^nu |X|^-nu).

The same exact homogeneity bounds the first derivatives of Omega_l. Section3's uniform temperature and gradient estimates include the factor a0, and yield

    |Theta_l(X)| <= C l^(1+2nu)|X|^(1-2nu),
    |grad Theta_l(X)| <= C l^(1+2nu)|X|^-2nu.

These estimates are uniform in b_d. At0 all three fields themselves are0, so pointwise convergence includes0. Their center derivatives do not converge to those of the zero field: DV_l(0)=diag(-c,c), Omega_l,x(0)=4/beta and Theta_l,xx(0)=2 remain fixed. Thus there is no C1 convergence of velocity or vorticity, or C2 convergence of temperature, on a neighborhood of0. The nonzero far-tail coefficient mu l^nu also tends to0.

This is a sequence of nonprofiles, each failing the vorticity equation on its scaled annular interval. It establishes that the particular exact checks listed here, even with normalized center derivatives, do not by themselves prevent pointwise collapse with concentration near0. It does not assert such collapse for an exact B2 solution sequence.

Dependencies: elementary polar calculus and integration by parts, complete smooth flows with linear growth, the relative inverse uniqueness, dominated convergence and the intermediate value theorem. The scalar balance interpretation also follows from packet79. No numerical calculation is used to prove the construction. It addresses the sufficiency of a list of checks, not the existence problem for the full B2 system.
