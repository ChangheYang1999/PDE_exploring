# Infinitely many polynomial moment constraints on a local repair

Written 2026-10-21T08:15Z. This is a linearized result on the exact polynomial patch. It does not assert a global nonlinear obstruction for a B2 profile or determine the complete adjoint nullspace.

## 1. Setting and statement

Fix beta>=2 and a!=0. Put q=4a/beta, lambda1=(beta-2)/2 and lambda2=1+3beta/2. On R^2 use

    W=(lambda1 x, lambda2 y-q x^2/2), Theta=a x^2, Omega=q x.

These solve the two stationary transport equations, have div W=2beta, and satisfy Omega=-curl(W-beta X). The background is used only on a polynomial patch. Its velocity is not sublinear at infinity, and it is not an admissible whole-plane B2 profile.

Write grad^perp eta=(-eta_y,eta_x), D=W.grad-2beta, and define

    L eta=-(W.grad+1)Delta D eta-q partial_y D eta-2a partial_x(x eta_y),
    L^*p=(W.grad+4beta)Delta[-W.grad p+(1-2beta)p]
         -q(W.grad+4beta)p_y-2a x p_xy.

If a smooth stream variation chi and temperature variation tau are compactly supported away from x=0 and satisfy the linearized thermal equation, packet143 proves that chi=D eta and tau=2ax eta_y for a compact eta. Consequently their linearized vorticity residual is L eta. A proof of the needed parametrization is repeated below.

**Theorem.** Let V_k be the space spanned by x^(2i+1)y^j for integers i,j>=0 with i+j<=k. Then L^*(V_k) is contained in V_(k-1), where V_(-1)={0}. Therefore

    dim {p in V_k : L^*p=0} >= k+1.

There are infinitely many linearly independent odd polynomial weights p satisfying L^*p=0. Every compact thermal-preserving infinitesimal change on the polynomial patch obeys integral p f_dot=0 for all these weights.

Besides p=x, an explicit independent weight is

    p3=x^3+c xy,
    c=3(7beta-8)(9beta-2)/(q(17beta-4)),

and L^*p3=0. The denominator is nonzero and c!=0 for beta>=2 and a!=0.

On any nonempty pair of reflected open disks separated from the axis, these weights give infinitely many independent linear functionals on the space of smooth compactly supported odd right-hand sides. Thus the intersection of the residual range with that target space has infinite algebraic codimension in the target space. No topological Fredholm statement, closed-range assertion, or full cokernel description is intended.

## 2. Derivation of the operator from the equations

The residual convention is

    f=(W.grad+1)Omega-Theta_x,
    t=W.grad Theta-(beta-2)Theta.

For delta W=grad^perp chi and delta Omega=-Delta chi, differentiation gives

    t_dot=W.grad tau-(beta-2)tau-2ax chi_y,
    f_dot=-(W.grad+1)Delta chi-q chi_y-tau_x.

Suppose chi,tau are compactly supported away from the axis and t_dot=0. Let T(x)=integral tau(x,y)dy. Integrating in y gives

    lambda1 x T'-(lambda2+beta-2)T=0.

For beta>2, uniqueness for the regular linear ODE on each open half-axis and compact support imply T=0. For beta=2 it is -4T=0. Hence

    eta(x,y)=(1/(2ax)) integral_{-infinity}^y tau(x,z)dz

is smooth and compactly supported away from the axis. It is odd if tau is even. Since lambda1-lambda2-(beta-2)=-2beta, the thermal equation becomes partial_y(chi-D eta)=0. Compact support in y gives chi=D eta. Substituting into f_dot gives L.

The support of eta may fill vertical gaps. For perturbations inside a disk contained in the polynomial patch, its vertical hull stays in that disk. More generally this proof is applied on the global polynomial extension of the patch, with chi,tau extended by zero; the necessary moment identities follow without a claim that eta has exactly the original support.

Since div W=2beta, the adjoint of D is -W.grad-4beta. Reversing the derivative compositions and integrating compactly supported functions by parts gives the displayed L^*. In particular integral p L eta=integral eta L^*p. Polynomial weights cause no convergence problem because eta and L eta are compactly supported.

## 3. Weighted polynomial degree and dimension

Assign weight1 to x and weight2 to y. The operator W.grad preserves weighted degree: its terms x partial_x, y partial_y and x^2 partial_y each have weight0. The Laplacian has two terms, lowering weighted degree by2 and4. The terms W.grad partial_y and x partial_xy lower it by2. It follows that L^* lowers the maximal weighted degree by at least2.

All its terms preserve oddness in x. For example, x^2 partial_y preserves parity, the Laplacian preserves parity, and x partial_xy also preserves parity. The odd polynomials of weighted degree at most2k+1 are exactly V_k, since a monomial x^(2i+1)y^j has weight2(i+j)+1. Therefore L^*(V_k) is contained in V_(k-1).

There are (k+1)(k+2)/2 such monomials in V_k and k(k+1)/2 in V_(k-1). Rank-nullity gives the claimed lower bound k+1. This argument proves a lower bound only; equality and a basis of the complete polynomial nullspace are not asserted. Since the bounds grow with k, the polynomial nullspace is infinite dimensional.

If independent polynomials p_1,...,p_N gave dependent moment functionals on odd tests supported in a reflected disk pair, a nonzero linear combination p would integrate to zero against all such tests. Because p is odd, arbitrary tests on the right-hand disk, with their odd reflection, would give twice the integral of p against arbitrary tests there. Thus p would vanish on that disk. A polynomial vanishing on a nonempty open set vanishes identically, contradicting independence. The moment functionals are therefore independent. Each annihilates the residual range by the integration-by-parts identity, proving the algebraic codimension assertion.

## 4. The first additional weight and a counterexample to sufficiency of affine moments

Direct calculation gives

    L^*(x^3)=(3/2)(8-7beta)(9beta-2)x,
    L^*(xy)=(q/2)(17beta-4)x.

Their displayed linear combination p3 is therefore annihilated. It is independent of x because its x^3 coefficient is1. Both coefficient factors defining c are strictly positive apart from the sign of q, so c!=0.

Choose a nonnegative, nonzero, smooth even function rho compactly supported in a reflected pair of disks away from the axis. Set

    f_target=partial_y(x rho).

Then f_target is odd in x and compactly supported. All three affine moments vanish:

    integral f_target=integral x f_target=integral y f_target=0.

The first two vanish by y integration, and the third equals -integral x rho=0 by parity. However,

    integral p3 f_target=-c integral x^2 rho != 0.

Thus this right-hand side cannot be the linearized vorticity residual of any compact thermal-preserving perturbation of the polynomial configuration with the stated support conditions. Vanishing affine moments alone does not suffice for that linearized repair problem.

This example does not exclude a nonlinear finite perturbation, a perturbation that changes the exterior, a non-polynomial background, or a profile whose residual has a different structure. In particular it does not evaluate the residual of the exterior-gluing construction in packet135.

## 5. Dependencies and verification

The proof uses differentiation, compact integration by parts, scalar ODE uniqueness, rank-nullity, and the polynomial identity theorem. The required portion of packet143 is repeated here. Packet142 supplies context for the three affine moments, but is not needed as a premise.

Verification completed 2026-10-21T08:19:30.668547+00:00: 33 algebraic controls, 54 exact sparse-rational matrix controls and nine compact counterexample quadratures passed. Actual Claude Opus5.5 review207 returned a complete written confirmation; its range-intersection and regular-ODE wording changes were independently checked and incorporated. Computation verifies finite instances only; the dimension argument above proves the claim for every k. The observed matrix ranks are not used to assert equality in the general nullity bound. Evidence is in verification/SUMMARY.md and build_inputs.json. No Lean build or other prohibited computation is used.
