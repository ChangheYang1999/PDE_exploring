# A compact thermal conjugacy changes the strain-weighted residual moment

Status: CONFIRMED by independent informal proof and8 exact controls, 2026-10-21. Nine finite quadrature checks support the implementation. Three actual claude-opus-5-5 requests returned no written audit; that availability limitation is recorded below. This is a conditional construction from the already verified configuration of packet135, not a B2 profile or a general residual-removal theorem.

## Statement and hypotheses

Fix beta>2 and a0>0. Put k=beta-2, lambda=(beta-2)/2, mu=1+3beta/2, c=1+beta/2 and q=4a0/beta. Let a smooth full-plane configuration have W=beta X+v, div v=0, v(0)=0, Omega=-curl v and canonical relative velocity v=K0 Omega. Suppose it has the B2 parity, center data and sublinear velocity, solves W.grad Theta=k Theta, has a whole-plane backward basin of the origin, and has positive Omega on x>0. Suppose its vorticity residual R=W.grad Omega+Omega-Theta_x is compactly supported away from the origin. In a neighborhood of a closed disk centered at (x*,0), x*>0, assume its fields are exactly

    W0=(lambda x,mu y-q x^2/2), Omega0=q x, Theta0=a0 x^2.       (1)

Assume the reflected disk is in the same polynomial patch and both disks are separated from the origin and x=0. Packet135 supplies configurations with a polynomial source disk large enough to contain such disks, after protecting a smaller source disk.

There exists a smooth compactly supported, odd-in-x function eta in this patch such that, for all sufficiently small real epsilon, its Hamiltonian flow creates configurations preserving thermal transport, all center data, all exterior fields, parity, positivity, the canonical inverse and the backward basin, but

    d/depsilon at0 integral p0(X) R_epsilon(X) dX !=0,
    p0(x,y)=x y/(x^2+y^2)^2.                                  (2)

The residual remains compactly supported and zero in the protected source disk. Hence the moment in(2) is not determined by center data and the complete exterior fields in this configuration class. This does not show that any configuration can be corrected into a profile. The deformed configurations need not retain vorticity transport in the two perturbed disks.

## Exact preservation properties

Set h=grad-perp eta=(-eta_y,eta_x) and let Phi_epsilon be its flow. A smooth compact vector field generates a global smooth diffeomorphism for every finite parameter. Since div h=0, det D Phi_epsilon=1. Since eta is odd in x, h commutes with the reflection (x,y)->(-x,y), and so does Phi_epsilon. It is the identity outside a compact subset of the patch and on a neighborhood of the protected source disk.

Define W_epsilon=(Phi_epsilon)_*W and Theta_epsilon=Theta composed with Phi_epsilon inverse. Conjugacy gives W_epsilon.grad Theta_epsilon=k Theta_epsilon exactly. The volume-preserving change of variables gives div W_epsilon=(div W) composed with Phi_epsilon inverse=2beta. Thus v_epsilon=W_epsilon-beta X is divergence free. It equals v near0 and outside the perturbation support. In particular v_epsilon(0)=0, the center derivatives agree to all orders, the exterior fields and their tails agree exactly, and sublinearity persists. Define Omega_epsilon=-curl v_epsilon. The flow and its reflected parity give the required parity of these fields. The complete flow of W_epsilon is Phi_epsilon composed with the W flow composed with Phi_epsilon inverse; because Phi_epsilon fixes0, its whole-plane backward basin is unchanged.

To check the inverse, let d=v_epsilon-v. This is a smooth compactly supported divergence-free vector field with d(0)=0. Set rho=-curl d. Its ordinary full-plane Biot-Savart velocity K*rho is smooth, has the same divergence and curl as d, and tends to0 at infinity because rho is compact with zero total integral. The difference is an entire harmonic vector field tending to0 at infinity; each component is zero by the mean-value property. Thus K*rho=d, and its value at0 is0. The relative inverse therefore also equals d. By linearity v_epsilon=K0 Omega_epsilon, with no harmonic correction or changed gauge. This argument does not assume that the unsubtracted velocity for the original slow tail converges.

On the positive-x perturbation support Omega=qx is bounded below by a positive constant. The deformed vorticity converges to it uniformly as epsilon tends to0, so it stays positive there for sufficiently small epsilon. Outside that support it is unchanged. This proves positivity on the whole right half-plane. The residual changes only in the compact perturbation support, so its moment against p0 is an ordinary absolutely convergent integral, despite p0's singularity at the protected origin.

## Independent first variation and adjoint

Here curl d means partial_x d2-partial_y d1. Direct differentiation of the pushforward, at fixed spatial position, gives

    dot W=(W.grad)h-(h.grad)W,
    dot Theta=-h.grad Theta,
    dot Omega=-curl dot W.                                    (3)

These variations are supported inside the polynomial patch, so every integration by parts below has zero boundary term. For an arbitrary smooth test weight p on that support, define

    f=-W.grad p+(1-2beta)p,
    B=p grad Omega+grad-perp f,
    D=(W.grad)B+2beta B+(DW)^T B+p_x grad Theta.                (4)

Differentiating R and integrating once in the advective term gives

    integral p dot R
      =integral dot W.dot(p grad Omega)+dot Omega f
         -integral p_x h.grad Theta
      =integral dot W.dot B-integral h.dot(p_x grad Theta).

Substitution of(3) and a second integration by parts gives -integral h.dot D. Since h=(-eta_y,eta_x), this equals

    integral eta (partial_x D2-partial_y D1)
      = integral eta A p,  A p=curl D.                         (5)

Thus(4)-(5) derive the adjoint directly as a vector identity; no coefficient extraction or teammate code is required.

For the polynomial patch(1), div W=2beta and grad Omega=(q,0). Put H=Delta(W.grad p0)+q(p0)_y. Since Delta p0=0 off0 and W=(lambda x,mu y-qx^2/2), elementary differentiation gives

    H=2(lambda-mu)(p0)_xx-2q x(p0)_xy,
    curl B=-H.

Expanding curl D in(4), the off-diagonal terms -q x B2_y cancel, and the diagonal terms sum to4beta curl B. The result is

    A p0=-(W.grad+4beta)H-2a0 x(p0)_xy.                        (6)

This also proves the sign of the adjoint in(5). At y=0,

    (p0)_xy=-3/x^4,
    H=6q/x^3, H_x=-18q/x^4,
    H_y=24(lambda-mu)/x^5.

Inserting these expressions in(6) yields

    A p0(x,0)=[30lambda-12mu-24beta]q/x^3+6a0/x^3
              =-3q(17beta+28)/(2x^3), x!=0.                  (7)

The final equality uses q=4a0/beta. This is strictly negative at x*>0. By continuity it stays negative on a sufficiently small positive-x disk inside the patch. Choose a nonnegative, nonzero smooth bump eta there and extend it oddly to the reflected disk. The coefficient A p0 is odd in x, so eta A p0 is even, negative on each nonzero bump, and its integral is strictly negative. Equations(5)-(7) prove(2). Differentiability in epsilon then gives different moment values for sufficiently small nonzero epsilon of one sign, while all preservation properties remain exact.

## Dependencies and scope

Packet135 supplies the global reference configuration and exact polynomial patch; the deformation and all first-variation arguments are proved here. The full-plane compact-source inverse uses the standard Newtonian inverse, already independently implemented and tested elsewhere in this lane. No assumption of a wall, y reflection, finite-energy slow tail or an unanchored convergent inverse is introduced.

This refutes only the proposed determination of the p0-weighted residual by center and exterior data, and the corresponding claim that p0 annihilates all normalized thermal-preserving variations. It neither identifies the full coupled adjoint kernel nor proves its absence. Surjectivity, closed range, nonlinear correction, and any class-wide nonexistence conclusion remain open.
