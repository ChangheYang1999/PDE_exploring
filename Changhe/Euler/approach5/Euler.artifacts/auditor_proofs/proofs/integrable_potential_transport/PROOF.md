# Integrability does not fix the transported potential

## 1. Exact local statement

Let u be a smooth divergence-free velocity on an oriented Euclidean three-manifold, w=curl u, and theta a smooth time-dependent one-form with d theta=i_w vol. Write D=partial_t+L_u. If D(d theta)=0 and theta wedge d theta=0 identically in spacetime, then locally

    D theta=d chi,       d chi wedge d theta=0,
    equivalently w.grad chi=0.                       (1)

These hypotheses do not force d chi=0. This remains false when theta is the nowhere-zero physical velocity form of an exact steady Euler solution on a compact manifold without boundary and with complete flow.

Since D commutes with d, d(D theta)=0, so the local Poincare lemma gives chi. Applying D to theta wedge d theta gives only (D theta) wedge d theta=d chi wedge d theta. Finally d chi wedge i_w vol=(w.grad chi)vol. This proves (1), and identifies the missing wedge factor in the invalid stronger inference.

## 2. Complete exact torus counterexample and its corrected gauge

On the flat torus (R/(2pi Z))^3 set

    f(y)=2+sin y, u=(f(y),0,0), p=0,
    theta=f(y)dx, w=(0,0,-cos y).

The coordinate function x is not globally real-valued, but dx and all displayed forms are globally defined. Since u is independent of x, div u=0 and (u.grad)u+grad p=0. The vector potential satisfies

    d theta=f'(y)dy wedge dx=i_w vol,
    theta wedge d theta=0, theta!=0 everywhere.

The complete flow is Xi_t(x,y,z)=(x+t f(y),y,z). Its exact pullback is

    Xi_t^*theta=f(y)(dx+t f'(y)dy),
    L_u theta=f f' dy=d(f^2/2)!=0,
    L_u(d theta)=0.

Thus all premises of Section1 hold, and D theta is nonzero on open sets. The source of failure is algebraic, not a boundary term, regularity issue or incomplete flow.

A transported gauge nevertheless exists:

    theta_t=f dx-t f f' dy=theta-t d(f^2/2).

Its exterior derivative is d theta, it is integrable and nowhere zero, and Xi_t^*theta_t=theta. Therefore (partial_t+L_u)theta_t=0. This is a different potential for the same vorticity, and at nonzero times it is not the physical velocity form. The example refutes automatic transport of an arbitrary integrable potential, not existence of a transported gauge or a theorem retaining uniqueness of the integrable potential.

The same formulas on R3 define a bounded nondecaying steady Euler field. They are not a whole-space decaying profile of the campaign similarity equation.

## 3. Correct identity for the actual rotating profile

Let U in C2 and P in C1 solve the full rotating profile equation on an open domain, with 0<c<1/2 and arbitrary real omega. Set A=cI-omega J, B=Ay+U, theta=U.flat, W=curl U, q=|U|^2/2, a=1-2c and R=q-P. Momentum makes grad P C1, so P is C2. The Lie derivative of a one-form, identified with a vector, is

    L_B theta=(B.grad)U+(DB)^T U
             =-(1-c)U-omega JU-grad P
                         +(cI+omega J)U+grad q
             =-a theta+dR.                           (2)

Differentiation yields L_B(d theta)=-a d theta. If U.W=0, then theta wedge d theta=0, and applying L_B gives

    0=(-a theta+dR) wedge d theta-a theta wedge d theta
      =dR wedge d theta.

Consequently W.grad R=0. It does not imply grad R=0. No decay, symmetry, global Clebsch representation or pressure normalization enters this identity.

For the reduced Bernoulli function H=P+q+Ay.U=P-q+U.B, one has R=U.B-H. In the helicity-free case the known identities WH=0 and W(U.B)=0 give exactly WR=0. Thus this calculation supplies no additional transverse constraint or sign.

## 4. The gradient term is nonzero for an exact local similarity profile

On y2>0, let omega=0, alpha=(1-c)/c and

    U=(y2^(-alpha),0,0), P=0.

It is smooth, solenoidal and solves the full local momentum equation because the only nonzero component is (1-c)y2^(-alpha)+cy2[-alpha y2^(-alpha-1)]=0. Its vorticity is W=(0,0,alpha y2^(-alpha-1)), so U.W=0 and W!=0. But

    dR=dq=-alpha y2^(-2alpha-1)dy2!=0.

Thus local similarity momentum does not eliminate the gradient in (2). This profile is singular on y2=0 and has no target-class conclusion. Its lack of rotation is sufficient to refute a statement asserted for every omega; (2) itself is valid at every omega.

## 5. Source and verification scope

Machon arXiv2002.09992v2, printed page8, Section5.1 after equation31, presents the stronger implication as an alternative justification of transport. Its first argument instead chooses advected Clebsch functions; that choice is compatible with the transported gauge in Section2. Earlier uniqueness assumptions can also distinguish a canonical potential after pullback. The present counterexample has multiple admissible potentials, so no uniqueness theorem is refuted.

Both actual Machon manuscripts were read, and the printed page8 image was inspected. The separate [source review](auditor_proofs/reviews/godbillon_vey_20261103/PROOF.md) records what was checked and what remains outside this audit. No global Godbillon-Vey invariant, singular extension, finite-energy estimate or Liouville theorem is invalidated or established by this local correction. All equations above were independently reconstructed without a numerical computation.
