# Weak vorticity sign near interior equilibrium fibres

Date:2026-10-20. Status: main theorem CONFIRMED by the independent verifier,
after checking actual Opus53; Section5 conditional corollary also CONFIRMED
after checking actual Opus57.
This is a restricted structural result, not a full endpoint.

## 1. Statement and scope

Let a smooth full-plane B2 profile at beta=2 satisfy the prompt, including
x-reflection, Theta(0,y)=0, the nonzero quadratic center jet, the canonical
full-plane inverse, and sublinear velocity. Assume additionally that Omega
has one weak sign throughout the open right half-plane. Put W=2X+U-U(0).
Let gamma be the smooth compact equilibrium arc through the material center,
with its transverse eigenvalue4, as proved in packets45 and53. Let Phi be
the C1 scattering diffeomorphism on the escape set E, with angular coordinate
alpha and smooth angular temperature h, as in packets33,36,39,54. Thus

    Theta=h(alpha), W.grad alpha=0,
    grad alpha=(-W2,W1)/(2 e^{4t}) at Phi(X)=e^{2t}e(alpha).

Reflection commutes with the flow and with Phi. The invariant axis x=0
maps to the vertical scattering axis, and the right half-plane maps to
the right semicircle, as follows also from outward escape. Uniqueness of
the flow prevents an orbit from crossing x=0. Thus every orbit point below
lies in x>0, and every transversal may be chosen inside that open half-plane.

Consider an angle alpha_star in the open right semicircle whose complete
escaping orbit has backward limit p in the INTERIOR of gamma. Then hprime
cannot take both positive and negative values arbitrarily close to
alpha_star. In particular alpha_star cannot be any finite-order interior
extremum of h, even a degenerate extremum with first nonzero derivative
of order4,6 or higher.

This conclusion is stronger than packet56 on this particular family of
orbits. It does not apply to an orbit with a degenerate endpoint as backward
limit. A flat plateau is not excluded: opposite signs separated by an open
interval on which hprime=0 need not approach the same angle. No assumption
Z=gamma is made. Other equilibrium components do not affect this local proof.

## 2. A C1 asymptotic phase near an interior zero subarc

Choose smooth coordinates (u,v) on a neighborhood of a compact interior
subarc, with that subarc v=0. Since the field vanishes there, its components
factor as

    udot=v A(u,v), vdot=v B(u,v), B(u,0)=4.

The transverse derivative is coordinate invariant at zeros. Shrink the
chart so B>=b0>0. In backward time s>=0 the equations are

    u'=-v A(u,v), v'=-v B(u,v).

There is an inner rectangle such that all its negative orbits remain in
the larger chart: |v(s)|<=|v(0)|e^{-b0 s}, and total tangential displacement
is at most ||A|| |v(0)|/b0. In particular the limit

    S(u0,v0)=lim_{s->infinity} u(s)

exists, with |S-u0|<=C|v0|, and is invariant as long as coordinates apply.
We now prove the C1 regularity and bounded derivative used below; existence
of a smooth stable foliation is not an unproved input.

For an initial-point variation write (a(s),b(s))=(delta u,delta v).
Differentiation of the backward equations gives

    a'=-v A_u a-(A+v A_v)b,
    b'=-v B_u a-(B+v B_v)b.

Shrink the chart so B+v B_v>=b1>0. Variation of constants in the second
scalar equation, with bounded coefficients, gives

    |b(s)|<=e^{-b1 s}|b(0)|
              +C int_0^s e^{-b1(s-r)}|v(r)| |a(r)|dr.       (1)

Integrating(1) in s and using the first equation yields, for all T,

    |a(T)|<=|a(0)|+C|b(0)|
                  +C int_0^T |v(r)| |a(r)|dr.

Gronwall and int_0^infinity |v(r)|dr<=C|v0| give a uniform bound
|a(s)|<=C(|a(0)|+|b(0)|). Equation(1) then gives exponential decay of b,
possibly after choosing a smaller rate to absorb a resonant factor s.
The first equation now shows a' is absolutely integrable with a uniformly
exponentially small tail. Hence the finite-time maps u(s;u0,v0) and their
first derivatives converge uniformly on a smaller closed rectangle.
Their limit S is C1, with bounded derivative. On v0=0, S(u0,0)=u0, so
S_u=1 there and S_u remains nonzero after another restriction.

For each fixed value of S, the level set is a C1 graph u=U(S,v). On either
side v>0 or v<0 its connected small branch is one orbit: vdot=v B is
nonzero, and S is invariant. Conversely all points on this branch have
the same backward equilibrium (S,0). Choose the section height small enough that its O(|v_section|) total
tangential drift is less than the available margin at both ends of the
chart. Forward branches then reach that section before any side exit.
These are the two local fibres.
This construction uses only a compact interior subarc; all constants may
fail as the subarc approaches an endpoint.

## 3. Bounded scattering-angle gradients on these negative orbits

Choose the side containing the selected escape orbit. At a small fixed
nonzero v=v_section, the fibre point depends C1 on its base value S.
The selected point is in E. By openness, a whole section interval near
its base point belongs to E. Flow invariance then puts all corresponding
local fibre branches in E. Define A_angle(S) to be their scattering angle,
choosing a local real angular branch. Since Phi is C1, A_angle is C1.

Its derivative is nonzero. Indeed along the fixed-v section, if alpha_u
were zero, the identity W.grad alpha=0 and W_v=vB!=0 would also make
alpha_v zero. This contradicts the nonvanishing scattering-angle gradient.
Also S_u!=0 on the section, so A_angle'=alpha_u/S_u!=0.

The constancy of alpha along each fibre gives

    alpha(X)=A_angle(S(X))

throughout this open local family. The derivative bound from Section2
therefore gives a UNIFORM bound on |grad alpha| along all sufficiently
negative pieces of nearby orbits. Compact finite-time pieces give the
remaining uniform bound. For every fixed selected orbit point Y, there
is a neighborhood U_Y within E and a constant C_Y such that

    |alpha_x(phi_{-s}Z)|<=C_Y for all Z in U_Y and s>=0.    (2)

When using physical x rather than chart u, the coordinate derivative matrix
and its inverse are bounded on the compact chart, so(2) is unchanged.
This also shows the family of such escaping interior fibres is open in E.

## 4. A continuous scalar resolvent without dividing at a zero

Define, on that open family,

    I(Y)=int_0^infinity e^{-s} alpha_x(phi_{-s}Y)ds.         (3)

The bound(2) proves absolute convergence, and dominated convergence proves
continuity in Y. No assertion about differentiating(3) in arbitrary spatial
directions is needed. The exact vorticity resolvent, whose endpoint term
vanishes because negative orbits remain in compact balls, and Theta=h(alpha)
give

    Omega(Y)=hprime(alpha(Y)) I(Y).                        (4)

This is valid ALSO when hprime=0. It was derived from an absolutely
convergent integral, not by defining I as Omega/hprime. Along the flow,
change variables in(3), or split the integral at a finite time, to obtain

    d/dt I(phi_tY)+I(phi_tY)=alpha_x(phi_tY).               (5)

The source is continuous, so this time derivative is justified by the
fundamental theorem of calculus. Formula(5) is local in time and extends
along the selected complete orbit by repeating the construction.

Suppose hprime has positive and negative values accumulating at alpha_star.
On a smooth local transversal through any point Y_star of that orbit,
alpha parametrizes an interval. Choose sequences on this transversal with
angles approaching alpha_star from those two sign sets. Every point remains
in the open right half-plane. By the one weak sign of Omega and(4), I has
opposite weak signs along the two sequences. Its continuity forces
I(Y_star)=0. This argument applies at every point of the selected orbit,
so I vanishes identically there. Formula(5) gives alpha_x=0 along it.
The exact scattering gradient formula then gives W2=0 there. The complete
escaping orbit is horizontal. Packet56 excludes all such orbits for weakly
signed Omega using the strictly signed middle row of the full-plane angular
Green kernel. Its hypotheses allow arbitrary compact backward limit sets
and apply here at beta2. The case Omega identically zero on x>0 is already
excluded by the required center coefficient Omega_x(0)=2a0!=0. The
nonzero angular tail input of packet56 also follows from the target
hypotheses. This contradiction proves the theorem.

If h has a finite-order extremum, its first nonzero derivative has even
order2m and hprime changes sign across the extremum. Thus all these extrema
are excluded on the interior-fibre family, not only the Hessian case m=1.
The proof equally excludes a flat critical point if both signs of hprime
accumulate at that very point. It does not exclude a flat plateau boundary
with only one nonzero sign on its neighboring side.

## 5. A conditional monotonicity consequence on the zero arc

Assume in addition Z=gamma, a0>0, and that the restriction g of Theta to
the open right half of gamma is not constant on any open subarc. Parametrize
that half by arclength s from0 to its endpoint s_end. Packet53 gives K=gamma,
so every nonstationary interior fibre escapes. The preceding theorem is
therefore available at every interior base point. On either local fibre
family g(s)=h(A_angle(s)), by continuity of Theta at its backward limit.
Since A_angle' is continuous and nonzero, positive and negative values of
gprime accumulating at one point would give both signs of hprime at its
corresponding angle, which the theorem forbids.

The zero set of gprime has empty interior by the extra assumption. Thus
the relative closures of {gprime>0} and {gprime<0} cover (0,s_end).
If both were nonempty, their being closed and covering a connected interval
would force an intersection, producing exactly the forbidden common
accumulation point. The arc and Theta are smooth at0, so Taylor differentiation gives
gprime(s)=2a0 s+O(s^2)>0 initially. Therefore gprime>=0 everywhere, and g is strictly increasing:
on any interval its nonnegative continuous derivative is not identically0.
Continuity of Theta on the compact arc extends g continuously to the
endpoint. Its endpoint value L is strictly positive. The required evenness
Theta(-x,y)=Theta(x,y) supplies the same
range on the left arc, and packet53's range identity then gives

    0<=Theta<=L on the whole plane, Theta(gamma)=[0,L].

The endpoint angular arcs have the constant value L. This is only a
conditional shape constraint. The no-open-constant-subarc assumption is
additional and does not follow merely from smoothness or weak vorticity
sign. If such a constant subarc exists, its two open fibre strips have
Theta constant and Omega=0 by the scalar resolvent, which is not itself a
contradiction. No monotonicity claim is made in that case or when Z!=gamma.

## 6. Why the endpoint gap is real

Here is an exact local kinematic example showing why bounded negative
orbits alone do not imply the bounded-gradient estimate(2). In coordinates
(x,y) with y>0, take

    W=((4-3y^2)x,y^3),
    a(x,y)=x y^3 exp(2/y^2).

Direct differentiation gives divW=4 and W.grad a=0. On the slow orbit x=0,

    y(-s)=(y0^{-2}+2s)^{-1/2},
    a_x(0,y(-s))=(y0^{-2}+2s)^{-3/2} exp(2/y0^2+4s).

Hence int_0^infinity e^{-s}a_x(phi_{-s}(0,y0))ds diverges. The backward orbit
is bounded and approaches the degenerate zero0, but its invariant-coordinate
gradient grows too quickly. The function a is a smooth local first integral
on y>0 with nonzero gradient there; it is not asserted to be the scattering
angle of an admissible full-plane B2 field. This W also fails the coupled
B2 vorticity equation for Theta=0 and fails the global target. The example
only refutes the proposed inference from backward boundedness to(2).

The endpoint case with a flat reduced scalar field can be still slower.
No claim is made here that its actual B2 scattering-angle integral converges,
and an expression hprime times a divergent integral must not be used.

## 7. Verification and endpoint status

The proof was written before the manufactured calculation. The independent
symbolic check in verification/manufacture.json took0.189800455933 seconds
and verified divW, the first integral, the slow orbit and the nonzero
vorticity defect. Its reusable source is
../../code_independent/interior_phase_manufacture.py.

Actual reviewer53 returned model claude-opus-5-5, end_turn, after
89.241508519 seconds (18:32:52.802831 to18:34:22.044527 UTC).
The full written answer was read and checked. It confirms the main proof
and manufacture. Its axis-invariance, side-exit and packet56 hypothesis
clarifiers are incorporated above. Its aside allowing the material center
as this interior fibre's backward limit is unnecessary: the axis fibre
through the center is invariant and is not the selected open-right orbit.
Section5 was added after that request and is not covered by reviewer53.
Actual reviewer57 later returned claude-opus-5-5, end_turn, after
51.672291424 seconds and confirmed that corollary. Its full answer was
read. Smoothness at0, endpoint continuity and temperature-preserving
reflection are explicit above. The reviewer used a global fibre-angle
map, which is stronger than needed; our proof uses only its local C1
maps near each interior point. Weak sign enters through the preceding
main theorem, even though it is not reused in the connectedness step.
Requests54,55,56 supplied no written audit and are not endorsements.

No numerical profile is produced. The generic smooth B2 target and
weak-sign profiles with endpoint or plateau extrema remain OPEN. No Lean
formalization is claimed and no Lean/Lake execution is allowed.
