# The exact integrated residual balance

Date:2026-10-20. Status: complete proof, preceding computation. This is an identity for approximate fields, not an existence or nonexistence theorem.

## Statement, hypotheses and notation

Let beta>0 and0<nu<1. Let Omega,Theta be C1 on the plane, and let V be C1, divergence free, with V(0)=0. Assume near0

    Omega=O(r), grad Omega=O(1),
    Theta=O(r^2), grad Theta=O(r), V=O(r),

and as r tends to infinity, uniformly in angle,

    Omega=O(r^-nu), grad Omega=O(r^-nu-1),
    Theta=O(r^(1-2nu)), grad Theta=O(r^-2nu),
    V=O(r^(1-nu)).

Write W=beta X+V and define the actual equation defects, with the B2 signs,

    R_Omega=W.grad Omega+Omega-Theta_x,
    R_Theta=W.grad Theta-(beta-2)Theta.

Define K=xy/r^4 and g=partial_x K=y(y^2-3x^2)/r^6 off0. All integrals below are over the full plane. Put

    pi c_Omega=integral K Omega,
    N[V]=integral Omega V.grad K,
    B[V]=integral Theta V.grad g,
    D[V]=N[V]-(1/2)B[V]-pi c_Omega.

Then every displayed integral is absolutely convergent, and

    integral K R_Omega=pi c_Omega-N[V]+integral g Theta,        (1)
    integral g R_Theta=2 integral g Theta-B[V],               (2)
    D[V]=(1/2)integral g R_Theta-integral K R_Omega.           (3)

If V is the canonical centered velocity of Omega, c_Omega is its center strain Psi_xy(0). For a prescribed or mixed transport velocity this equality need not hold: c_Omega always denotes the strain of the represented Omega, not that of the chosen V. No center normalization or equality c_Omega=1+beta/2 is assumed for these identities.

## Proof of absolute convergence and the boundary limits

K,g,grad K,grad g are homogeneous of degrees -2,-3,-3,-4. Near0, K Omega, Omega V.grad K, g Theta and Theta V.grad g are all O(r^-1); their absolute integrals have radial bound C dr. Also R_Omega=O(r), R_Theta=O(r^2), so the two weighted residuals have the same integrable bound.

At infinity, K Omega=O(r^-2-nu), Omega V.grad K=O(r^-2-2nu), g Theta=O(r^-2-2nu), and Theta V.grad g=O(r^-2-3nu), all integrable. The possibly slower linear transport parts give K R_Omega=O(r^-2-nu)+O(r^-2-2nu) and g R_Theta=O(r^-2-2nu)+O(r^-2-3nu), again integrable. These estimates do not require cancellation of the leading profile transport terms.

Work first on epsilon<r<R. Since div V=0, div W=2beta. Euler homogeneity gives X.grad K=-2K and X.grad g=-3g. The boundary term from integration by parts in integral K W.grad Omega is integral_(boundary) K Omega W.n. It is O(epsilon) at the inner circle and O(R^-nu) at the outer circle. The boundary term for integral g W.grad Theta is likewise O(epsilon) and O(R^-2nu). Finally the term from integrating K Theta_x is integral_(boundary) K Theta n_x, with bounds O(epsilon) and O(R^-2nu). Every boundary term tends to0.

It follows that

    integral K W.grad Omega
      =-integral Omega [W.grad K+2beta K]
      =-integral Omega V.grad K=-N[V].

Also integral K Theta_x=-integral g Theta. Substitution into the definition of R_Omega proves(1).

Similarly,

    integral g W.grad Theta
      =-integral Theta [W.grad g+2beta g]
      =beta integral g Theta-B[V].

Subtracting (beta-2) integral g Theta proves(2). Elimination of integral g Theta proves(3), with the signs shown. If V=B[Omega], the standard center derivative of the absolutely convergent relative inverse gives c_Omega=(1/pi)integral K Omega. Under the stated local odd-type bound this integral is ordinary absolute integration, not a principal value. This last identification is not needed for(1)-(3).

## Two transport fields and the role of forcing

For two such divergence-free centered velocities V_a,V_b, with identical represented Omega and Theta, let delta V=V_a-V_b. Linearity gives

    D[V_a]-D[V_b]
      =integral Omega delta V.grad K
         -(1/2)integral Theta delta V.grad g
      =(1/2)integral g delta V.grad Theta
         -integral K delta V.grad Omega.                  (4)

The last equality follows either from(3) or the same absolutely convergent integrations by parts. In the multiplicative homotopy V_m=eps V_self+(1-eps)V_external,

    D[V_m]=eps D[V_self]+(1-eps)D[V_external].             (5)

For the additive homotopy V_m=V_self+lambda V_source, the difference D[V_m]-D[V_self] is lambda times the linear expression in(4). A small mixed residual moment therefore does not imply a small self-induced residual moment. Nor does either small moment imply a small pointwise residual, since the weights change sign.

## Scope of a numerical check

Equation(3) permits two substantially different evaluations: the left side uses values of Omega,Theta,V and exact derivatives of the kernel; the right side uses spatial derivatives of the represented fields. Agreement checks inverse, quadrature, differentiation, gauge, integration limits and signs together. It is still only a consistency check on the approximation. An interval bound on a moment would remain weaker than control of the defining PDE throughout the plane. No denominator floor or subjective normalization appears in this identity.

Dependencies: Euler homogeneity, the divergence theorem on punctured annuli, the stated decay estimates and, only for interpreting c_Omega, the centered full-plane inverse. No numerics are used in the proof.
