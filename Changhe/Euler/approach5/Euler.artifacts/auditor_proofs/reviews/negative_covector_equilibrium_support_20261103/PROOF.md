# An exceptional negative-covector support contains a carrier equilibrium

Status: independently reconstructed LIT100, checked against the focused configured-model review. The final verdict is recorded in the auditor's ledger (AUDIT_LEDGER.md). This removes first-vorticity-flat regular support points from the obstruction in the earlier LIT99 argument. It does not itself exclude supports containing equilibria.

## 1. Exact statement and dependencies

Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, (1-c)U+B.grad U+omega JU+grad P=0,
    A=cI-omega J, B=Ay+U, W=curl U,
    0<c<1/2, omega in R, U=o(|y|) uniformly,
    U.W=0 everywhere.

Here J(x,y,z)=(-y,x,0). Put a=1-2c, kappa=1+c, d=3c, D=d+kappa,

    H=P+|U|^2/2+(Ay).U, g=U.B, alpha=B cross W.

Let mu be a compactly supported probability, invariant and ergodic under the whole carrier flow, with support S, and assume almost everywhere

    B!=0, W=0, DW!=0, D alpha=0.                         (1)

Then S contains a zero of B, although mu({B=0})=0. The statement concerns accumulation in the support, not an equilibrium atom.

We use the confirmed A444-A445 conclusions: H=h and W=g=0 on S; grad H=-aU there; at every point of S with U!=0, grad g=-kappa U. Any zero of U on S is the spatial origin and is also a zero of B. These conclusions extend to all such support points by continuity, including points with DW=0. The final contradiction uses the independently confirmed A449 exclusion of the periodic negative-covector branch, and therefore the global sublinearity and helicity assumptions remain essential.

The Lamb identity grad H=-aU+alpha upgrades H to C2; g is C2 and BH=-ag. Uniform sublinearity makes |B(y)|<=C(1+|y|), so the C1 flow is complete by Gronwall in both time directions. No boundedness of DU at infinity is required.

## 2. Projection onto the regular H surface

Suppose B has no zero on S. Compactness and the A444 zero restriction give positive lower bounds for |B|, |U| and |grad H| there. Choose a relatively compact open neighborhood V of S on which grad H!=0, and form the oriented C2 surface M={H=h} intersect V. It may be disconnected and need not be compact or complete. Define on V

    n=grad H/|grad H|^2, Btilde=B-(BH)n.                  (2)

The field Btilde is C1 and Btilde H=0, so it induces a C1 surface flow on M. On S, BH=0 and Btilde=B. Every original orbit in S is therefore a solution for Btilde and remains compact. Uniqueness identifies the two full orbits on S. This establishes invariance of S without asserting completeness elsewhere on M.

At every x in S the scalar differential satisfies

    d(BH)=-a dg=a kappa U.flat=-kappa dH.                (3)

If v is tangent to M at x, differentiation of(2) gives

    D Btilde(x)v=DB(x)v-d(BH)(x)v n(x)-(BH)(x)Dn(x)v
                =DB(x)v.                               (4)

This uses only n in C1, available because H is C2. No second derivative of n or of W appears. More explicitly, the projected derivative of a tangent initial vector remains tangent because H is a first integral. Formula(4) makes this derivative vector solve the original variational equation along the common orbit, with the same initial data. Uniqueness of that linear equation identifies the full tangent cocycles. Formula(3) also directly shows that the original derivative transports ker dH along S. The original B need not be tangent to M away from S.

## 3. The uniform surface Poincare estimate

Let Psi_t be the backward B flow. Differentiating the covector pullback along orbits in S, using(3), yields

    D Psi_t(x)^T grad H(Psi_t x)=e^(kappa t)grad H(x).   (5)

The ambient determinant is det D Psi_t=e^(-dt). For F=D Psi_t(x), (5) gives

    F^(-T)grad H(x)=e^(-kappa t)grad H(Psi_t x).

The codimension-one area formula |det F| |F^(-T)nu|, for a unit normal nu at x, therefore gives

    J_2(F|T_xM)=e^(-Dt)|grad H(Psi_t x)|/|grad H(x)|.    (6)

Inside T_xM choose the one-dimensional line perpendicular to B(x). The normal Poincare derivative P_x^t means projection of F from this line to the corresponding perpendicular line at Psi_t x, along the flow direction. Since F B(x)=B(Psi_t x), taking the two-dimensional determinant in unit-flow and unit-normal bases gives exactly

    |P_x^t|=e^(-Dt) |grad H(Psi_t x)|/|grad H(x)|
                       * |B(x)|/|B(Psi_t x)|.           (7)

All ratios are uniformly bounded on S. There exists C>=1 with |P_x^t|<=C e^(-Dt) for every x in S and t>=0. This estimate is valid even where DW=0. It involves neither a Lyapunov limiting argument nor a uniform lower bound on |DW|.

## 4. Uniform normal contraction forces recurrent regular points to be periodic

We prove the needed local dynamical lemma. Let X be a C1 field on an oriented C2 surface near a compact full-flow invariant K, nonzero on K. Assume its normal Poincare derivatives satisfy |P_x^t|<=C e^(-eta t) for all x in K,t>=0, with eta>0. Every recurrent x in K is periodic. Consequently each whole-flow ergodic probability supported on K is normalized time measure on a periodic orbit.

Choose L so that C e^(-eta L)<1/4. Near K, take transverse unit vectors obtained by rotating X/|X| by a right angle in the surface. This is a C1 field. Its short integral curves give transverse sections I_x with unit normal derivative at their centers. Let Theta_x(s,t)=Phi_t(I_x(s)). The parametrized inverse function theorem applies uniformly on K, since its center derivative has the two perpendicular columns n(x),X(x), with |X| bounded below. It gives common coordinate rectangles and jointly continuous inverse first derivatives. In finitely many surface charts this is one coherent construction, rather than unrelated choices on overlaps. Holonomy near time L from I_x to I_(Phi_L x) is the first coordinate of Theta_(Phi_L x)^(-1) composed with Phi_L and I_x. It fixes the centers and has center derivative of norm less than1/4. Uniform continuity of the first derivatives gives a common delta>0 on which every such map F_x is defined and

    |F_x'(s)|<=1/2, |F_x(s)|<=|s|/2, |s|<=delta.         (8)

The transit times are positive and close to L. Only a C1 field is used. The common neighborhoods exist although the surface is incomplete, since each central segment remains in compact K and L is fixed.

Composing n such block holonomies along the orbit of x gives a map defined on the entire initial interval [-delta,delta], with image radius at most2^(-n)delta and derivative norm at most2^(-n). If x is recurrent, take t_j->infinity with Phi_(t_j)x->x and write t_j=n_j L+r_j, 0<=r_j<L. Append the bounded-time r_j map and a short projection to I_x in its flow box. For all large j the shrinking block image lies in the common domain of this last map. The resulting return holonomy R_j has center tending to0 and derivative norm at most C0 2^(-n_j), where C0 is uniform by finite-time derivative bounds and transversality near K.

For large fixed j, R_j maps the closed initial interval strictly inside itself and is a contraction. Its fixed point q_j belongs to a periodic orbit Gamma_j, since the transit time is positive. Iterates of R_j take x to q_j. For this fixed map the return times are continuous, bounded and positive on the compact interval. Continuous dependence over the intervening bounded time segments proves that the full forward orbit of x approaches Gamma_j. Recurrence of x then implies x belongs to the closed orbit Gamma_j. Its entire orbit lies in K by invariance.

Finally choose a point both recurrent and generic for a given whole-flow ergodic probability on K. Continuous-time ergodicity supplies its empirical limit, without ergodicity of a prescribed time-L map. Since it is periodic, this limit is normalized time measure on that orbit. This proves the lemma.

## 5. Application and scope

Apply the lemma to X=-Btilde, K=S and eta=D. On S this is the original backward flow, so its invariant probability and ergodicity are exactly those of mu. Thus mu is supported on a nonstationary periodic B orbit. The almost-everywhere conditions(1) hold somewhere on that orbit and propagate everywhere by the differentiated Cauchy law. In particular rank DW=1 and image DW=R B all around it; the A444 covector identity already holds at every point. The exact A449 hypotheses therefore hold, contradicting that theorem.

Hence S intersects {B=0}. There is no contradiction with(1): this equilibrium subset has measure zero. Near it the speed ratio in(7) can diverge, transverse sections lose uniform size, and Section4 no longer applies. No hyperbolicity, finiteness or isolation of the equilibrium set follows.

The projected field is an auxiliary C1 surface field. It is not asserted to satisfy Euler away from S. The proof does not use the LIT95 or LIT99 arguments, a dense vortical neighborhood, a global compact surface theorem, or a numerical calculation. At omega=0 the independent A010 theorem already settles the global profile; the unresolved global branch concerns nonzero omega.
