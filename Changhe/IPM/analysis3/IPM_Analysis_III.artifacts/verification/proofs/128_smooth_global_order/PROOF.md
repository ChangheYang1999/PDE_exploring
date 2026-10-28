# A smooth monotone order for the actual modal transport

## Exact statement

Use the exact normalized modal field V of proof 79 and its accepted original-data certificates. Put ell=1/k, A=2ell-1, D=4ell-1 and Sigma=A+D. Let M be the radial blow-up of the origin and radial compactification of the plane, with coordinates

 u=r/(1+r) in[0,1], theta in R/(2 pi Z).

Thus M is a compact cylinder. The two source points are P_+=(p,0), P_-=(-p,0). Write S_x for the two points of its origin circle in the horizontal directions, S_y for the two points in the vertical directions, and I for its entire circle at infinity. The lifted vector field is denoted W. On the ordinary logarithmic cylinder it is q partial_t+vartheta partial_theta, t=log r.

**Theorem.** There is a real function Lambda in C^infinity(M), invariant under the two coordinate reflections, with

 0<=Lambda<=3,
 Lambda(P_+)=Lambda(P_-)=0, Lambda(S_x)=1,
 Lambda(S_y)=2, Lambda|I=3,
 W Lambda>0 on M\(P_+ union P_- union S_x union S_y union I).

Its derivatives of positive order vanish at each of these critical sets, in the smooth coordinates of M. In particular W Lambda>=0 everywhere. For any compact K avoiding these sets, min_K W Lambda>0.

Consequently there exists a reflection-invariant, uniformly smooth order s(t,theta) on the logarithmic cylinder such that

 41/20<=s<=25/4, W s>=0,
 s=41/20 near both P points and near S_x in the radial blow-up,
 s=25/4 on the prescribed sector |cos theta|<=1/2 and for every sufficiently large r.

Every derivative of s in t and theta is bounded. Thus the order hypothesis of topics123 and126 is satisfied for the actual field. The construction is qualitative: no derivative bound, escape minimum or operator norm is certified here. The angular sector1/2 is a prescribed geometric set, not a numerical estimate.

## The flow on the compact cylinder

The accepted endpoint formulas give

 rdot=r[-A cos^2 theta+D sin^2 theta+O(r^2)],
 thetadot=Sigma sin theta cos theta+O(r^2)                 (1)

at the origin, with a C1 extension to r=0. The remainders and their needed first derivatives are uniform in theta. Reflection symmetry makes both axis directions invariant. The exact finite modal formulas allow extension across r=0 by taking the radial coefficient odd in r and the angular coefficient even in r; this extension is C1. It will only be used for smoothing near that boundary.

At infinity rdot/r=ell+O(r^(k-1)) and thetadot=O(r^(k-1)), with0<k<1. The induced u velocity and angular velocity tend uniformly to zero at u=1. Declare each point of I fixed. This gives a continuous complete flow on M: points near I remain near I over every bounded time interval by the radial differential inequality, and their angular displacement tends uniformly to zero. Uniqueness at I follows from the same radial inequality. No C1 regularity at I is asserted or used.

Proof 79 proves every physical interior quadrant orbit runs from its adjacent P to infinity. The horizontal segment from P to the origin runs from P to S_x after blow-up. The outer horizontal ray runs from P to I. The vertical rays run from S_y to I. Equation(1) gives the remaining origin-circle arcs from S_x to S_y. These are all orbits on M. There are no other limiting or recurrent sets.

## Three attractor-repeller pairs

An attractor here means a compact invariant set with a stable attracting neighborhood. Its dual repeller is the complement of its forward basin. Write H for the two closed horizontal segments from the blown-up S_x points to P_+,P_-. Write O for the whole origin circle and Y for both closed vertical rays, including their S_y endpoints and endpoints in I. The following pairs have the displayed attracting set A_i and dual repelling set R_i:

 i=1: A_1=O union Y union I,       R_1={P_+,P_-};
 i=2: A_2=Y union I,              R_2=H;
 i=3: A_3=I,                     R_3=O union H.             (2)

Here a union already containing an endpoint does not add another copy. The sets in each pair are disjoint compact invariant sets.

For pair3, choose a large radius R with rdot>=ell r/2 for r>=R. The closed collar r>=R is a forward trapping neighborhood of I. Its maximal invariant set is I: every nonconstant physical orbit in it eventually leaves it in backward time, by the orbit classification. The basin of I consists of every physical point except H, while the origin circle stays on that circle. Thus its dual repeller is O union H.

For pair1, choose disjoint small closed ellipsoids around P_+,P_- that trap the backward flow strictly. Their existence follows from the positive definite symmetric part of DV at each source, already certified. The complement of their interiors traps the forward flow strictly at its boundary. Its maximal invariant set consists of points whose backward orbit does not converge to either P, which the classification identifies with O union Y union I. This is an attractor: a compact strictly trapping neighborhood has uniform attraction to the intersection of its forward images. To see the last fact directly, failure of uniform approach would give points in nested compact forward images with a limit outside the intersection, a contradiction. Its dual repeller is precisely the two sources.

For pair2 one must also check stability, rather than deduce it only from the list of limits. Near S_y put z=|pi/2-theta| or its reflected counterpart. From(1), for some r_0,z_0>0,

 rdot>=D r/2, zdot<=-Sigma z/2 when r<=r_0,z<=z_0.        (3)

The estimate for zdot uses axis parity, so the error divided by z is O(r^2). On a fixed compact vertical segment r_0/2<=r<=2R, the accepted d=V_2(0,r)/r>0 and continuity give q>=d_*/2>0 in a sufficiently thin vertical sector. Axis tangency also gives |zdot|<=C z there. Its passage time from r_0/2 to2R is at most

 T_*=(2/d_*) log(4R/r_0).

An initial sector narrower by the factor exp(-C T_*) stays in the chosen sector until it reaches the forward trapping far collar. For smaller radii(3) first brings every r>0 to r_0 while its angle contracts. Points on r=0 contract to S_y. Given any neighborhood of A_2, choose the far collar and the thin sectors inside it. These estimates produce a smaller neighborhood whose entire forward image stays in the first neighborhood and approaches A_2. This proves Lyapunov stability and local attraction. The orbit classification identifies the full basin as M\H, so its dual repeller is H.

For any of these pairs, attraction is uniform on a compact subset of its basin. Indeed, stability supplies a forward-stable smaller neighborhood for any prescribed error. Each point of the compact set eventually enters it; continuity over that finite time gives an open neighborhood with the same property. A finite subcover bounds all entrance times. This is the only uniform attraction fact needed below.

## A continuous strictly monotone function for one pair

Fix one pair(A,R) in(2) and a reflection-invariant metric on M. Define

 D_0(x)=dist(x,R)/(dist(x,A)+dist(x,R)),
 v(x)=inf_(t>=0) D_0(Phi_t x).

The denominator is positive because A,R are disjoint compact sets. Then0<=v<=1, v=0 on R, v=1 on A, and v(Phi_s x)>=v(x) for s>=0. For x outside A union R,0<v(x)<1. Positivity follows by using uniform attraction for the tail of its orbit and a positive minimum on an initial compact orbit segment. The strict upper bound follows by choosing t=0.

The function v is continuous. At R,0<=v<=D_0 proves continuity. At A, stability forces D_0 to remain uniformly close to1 on forward trajectories started close to A. Elsewhere, uniform attraction on a small closed neighborhood disjoint from R reduces the infimum, up to an arbitrarily small error, to a finite time interval. The finite-time infimum of a jointly continuous function is continuous.

Now put

 L(x)=integral_0^infinity exp(-t) v(Phi_t x)dt.

Dominated convergence proves continuity. It is nondecreasing along the flow and has values0 on R and1 on A. It is strictly increasing along every nonconstant time step outside A union R. If L(Phi_s x)=L(x) for some s>0, the nonnegative continuous integrand v(Phi_(t+s)x)-v(Phi_t x) vanishes for every t>=0. Its monotonicity then makes v constant on the forward orbit. That constant must be1 by attraction, contradicting v(x)<1. Finally set

 w(x)=integral_0^1 L(Phi_t x)dt.

Then w is continuous,0 on R,1 on A, and its directional derivative exists and is the continuous function

 Ww=L(Phi_1 x)-L(x)>0 on M\(A union R).                  (4)

All functions are reflection invariant. This construction proves the particular Lyapunov fact needed here without assuming a differentiable version of Conley's theorem.

## Smoothing while preserving the directional inequality

We give the needed elementary approximation argument. On a compact set K disjoint from A union R and from I, w and Ww are continuous and W is C1. Extend the origin chart by the even-r convention for w and the odd/even convention for W described after(1). The distributional directional derivative of w equals(4). This follows by integrating in a C1 flow box and its continuous Jacobian, or directly from the flow identity by a difference quotient. The same identity survives the reflection extension because the normal component of W vanishes on r=0.

Let rho_epsilon be a smooth compactly supported mollifier in a coordinate chart. The commutator between W.grad and convolution tends uniformly to zero. An explicit formula is

 W.grad(rho_epsilon*w)-rho_epsilon*(W.grad w)
 = integral [grad rho_epsilon(x-y).(W(x)-W(y))
             +rho_epsilon(x-y) div W(y)] [w(y)-w(x)]dy.    (5)

The terms with w(x) cancel by integration by parts. Bounded first derivatives of W and uniform continuity of w bound(5) by a constant times the modulus of continuity of w at scale epsilon. Also rho_epsilon*(Ww) converges uniformly to Ww. Thus mollification approximates both w and its directional derivative uniformly on K. A finite smooth partition of unity preserves this assertion: its extra terms contain only the uniformly small approximation errors times W applied to the partition functions. Reflection averaging preserves both the approximation and positivity.

For any sufficiently small a>0, apply this approximation on the compact band {a<=w<=1-a}. This band avoids A,R and I. Elsewhere use a smooth global approximation to w, taking it identically0 sufficiently near R and identically1 sufficiently near A, including I. These alterations can be made outside the narrower band. Their directional derivative is immaterial there. Choose the approximation error small enough, and compose with a smooth nondecreasing scalar function F_a that is0 near0,1 near1 and has positive derivative on a prescribed smaller middle interval. Wherever F_a' is nonzero, the smoothed function has positive directional derivative by(4)-(5). The result l_a is C^infinity on M,

 0<=l_a<=1, W l_a>=0,
 l_a=0 near R, l_a=1 near A,
 W l_a>0 on any prescribed compact subband0<w<1.          (6)

The statement about all of M is legitimate despite the finite regularity of W: only w is being smoothed, and every nonconstant part of l_a is supported away from I, where W is C1. The final l_a is exactly constant near I. Its reflection symmetry gives a smooth even extension at the axis directions; there is no one-sided angular gluing.

## A complete smooth function and the Sobolev order

Let C={P_+,P_-} union S_x union S_y union I. Exhaust M\C by reflection-invariant compact sets K_n. Apply the preceding construction separately to all three pairs. At every point outside C, at least one of the three pair functions w_i lies strictly between0 and1. This follows either from(2) or from the complete orbit list. Compactness of K_n gives a positive lower bound for

 max_i min(w_i(x),1-w_i(x)), x in K_n.

Choose the three smooth cuts in(6) sufficiently close to their endpoint values that their sum Lambda_n satisfies W Lambda_n>0 on K_n. It is nondecreasing everywhere. Its critical values are exactly0,1,2,3 in the required order, by the membership table in(2), and it is constant in a neighborhood of each critical set. In particular every Lambda_n is smooth in the compactified coordinate u, even though the compactified vector field need not be C1 at I.

Choose positive weights b_n with sum b_n=1 and

 sum_n b_n ||Lambda_n||_(C^j(M))<infinity for every j.

For example normalize b_n proportional to2^(-n)/(1+max_(j<=n)||Lambda_n||_(C^j)). Then Lambda=sum_n b_n Lambda_n converges in C^infinity(M), has the specified values and range, and W Lambda>=0. For every x outside C, some K_n contains x, so one strictly positive summand gives W Lambda(x)>0. Derivatives of positive order vanish on C, since they vanish there for each summand and converge uniformly. This proves the first statement.

On R_2=H the value of Lambda lies in[0,1], since the pair2 and pair3 cuts vanish there. On A_2=Y union I it lies in[2,3], since the pair1 and pair2 cuts equal1 there. Composing Lambda with a smooth nondecreasing function constant below1+a and above2-a,0<a<1/2, already gives the required low and high values on some uniform neighborhoods.

To obtain the prescribed angular sector1/2, use pair2 directly. The compact set K_high={|cos theta|<=1/2} union I is disjoint from R_2. Its continuous function w_2 has a strictly positive minimum mu on K_high. Apply the smoothing construction with transition band strictly inside(0,mu), with approximation error smaller than its distance from both endpoints. Choose the scalar cut equal to1 before mu and equal to0 sufficiently near0. The resulting smooth l satisfies Wl>=0, l=0 on a neighborhood of R_2, and l=1 on a neighborhood of K_high. Set

 s=41/20+(25/4-41/20)l.

This gives every asserted constant region. It is not necessary to use the same scalar function Lambda for both the escape multiplier and this stronger prescribed-sector order. Both are smooth and nondecreasing along exactly the same flow.
Every cylinder derivative of s is bounded: near the origin partial_t=r partial_r, which preserves bounded smooth derivatives on the compact blow-up; away from the ends this is ordinary compactness; near infinity s is constant. Reflection symmetry is inherited. This proves the second statement.

## Dependencies and scope

The actual field, its exact normalization, C1 lifted origin coefficients, axis positivity and global orbit classification are supplied by the accepted topics52,60,68 and79. The proof above supplies the topological and smoothing steps, rather than treating the words 'Conley function' as a smoothness theorem. A primary comparison reference is M. R. Razvan, On Conley's Fundamental Theorem of Dynamical Systems, arXiv:math/0009184 (2000), Theorems3.2-3.3, which constructs continuous Lyapunov functions for attractor-repeller pairs and Morse decompositions. No smoothness conclusion from that reference is assumed here.

This proves existence of the order needed by the previously checked H1 and H2 statements. It gives a qualitative globally nonnegative escape function with positive derivative off the critical sets. It proves neither H3 nor the uniform-in-frequency normal inverse, low injectivity, a complement certificate, a numerical high inverse bound, or nonlinear existence.
