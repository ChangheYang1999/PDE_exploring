# Transport restrictions for outward similarity fields

Status: proved. Independently derived by the astra verifier on 2026-10-20. These are partial restrictions, not a full nonexistence theorem for B2.

## Statement and notation

Let beta>0, let U be locally Lipschitz on R^2, and suppose U(X)=o(|X|), uniformly as |X| tends to infinity. Put W(X)=beta X+U(X)-U(0). Let Theta be C^1 and satisfy

    W . grad Theta = (beta-2) Theta.

Then:

1. If 0<beta<2, Theta vanishes identically.
2. If beta=2, Theta is globally bounded, without any initial boundedness assumption.
3. If beta>2 and Theta is globally bounded, Theta vanishes identically. More generally Theta vanishes at every point with a bounded forward W-orbit.
4. Suppose beta>2 and, in addition, |U(X)-U(0)| <= C |X|^(1-delta) outside a ball, for some delta>0. Along every forward escaping orbit X(t) starting at Y, there is C_Y>0 such that |X(t)|=C_Y exp(beta t)(1+o(1)). If Theta(Y) is nonzero, then

    |Theta(X(t))| / |X(t)|^(1-2/beta) -> |Theta(Y)| C_Y^(-(1-2/beta)).

If Omega is C^1 and also solves W.grad Omega+Omega=Theta_x, conclusion 1 implies Omega=0. In general the unique Omega bounded on each backward orbit is

    Omega(Y) = integral_0^infinity exp(-t) Theta_x(phi_{-t}(Y)) dt.

Here phi_t is the flow of W. The stronger radial asymptotic in statement 4 must not be inferred from U=o(r) alone.

## Complete proof

Sublinearity implies |W(X)| <= C_0(1+|X|). Gronwall's inequality bounds a trajectory on every finite time interval in both time directions. Local Lipschitz regularity and this bound give a complete flow by the local ODE continuation theorem.

Choose R>0 so that |U(X)-U(0)| <= beta |X|/2 for |X|>=R. On this exterior region,

    W(X).X >= beta |X|^2/2.

For the backward trajectory Z(t)=phi_{-t}(Y), the radial function satisfies

    d/dt |Z(t)|^2 = -2 W(Z(t)).Z(t) <= -beta |Z(t)|^2

as long as |Z(t)|>=R. The closed ball of radius max(R,|Y|) is invariant under the backward flow: a first crossing outwards would contradict this strict inward radial derivative. A trajectory starting outside B_R enters B_R in finite backward time, since otherwise the displayed differential inequality would force its radius below R. Thus every backward orbit is contained in a compact ball, and every point outside B_R has a backward predecessor in the fixed ball B_R.

Along any orbit the temperature equation gives

    Theta(phi_t(Y))=exp((beta-2)t) Theta(Y).

If beta<2, apply this at negative times. The left side stays bounded on the compact set containing the backward orbit, while exp((2-beta)t) grows for t tending to positive infinity. Therefore Theta(Y)=0. Y was arbitrary.

If beta=2, Theta is constant on the same trajectories. For Y outside B_R, its value equals a value attained inside the fixed ball B_R. Consequently sup_R2 |Theta| <= max_B_R |Theta|, which is finite. This proves statement 2.

If beta>2 and Theta is bounded on a forward orbit, the positive-time formula forces Theta(Y)=0. This proves both forms of statement 3.

An unbounded forward trajectory eventually crosses the circle of radius R. It cannot return across this circle, and thereafter its radial derivative is positive. The inequality d|X|/dt >= beta |X|/2 shows that its radius tends to infinity at least exponentially. Under the extra power bound of statement 4,

    d/dt (log |X(t)| - beta t) = O(|X(t)|^(-delta)).

The right side is absolutely integrable over the forward tail. Therefore log |X(t)|-beta t converges to a finite real number. Exponentiation gives C_Y>0 and the claimed radial asymptotic. Substitute the exact exponential transport law for Theta to obtain the limit in statement 4.

Finally differentiate exp(-t) Omega(phi_{-t}(Y)). Its derivative is -exp(-t) Theta_x(phi_{-t}(Y)). Integration from zero to S gives

    Omega(Y)=exp(-S) Omega(phi_{-S}(Y))
             + integral_0^S exp(-t) Theta_x(phi_{-t}(Y)) dt.

Both Omega and Theta_x are bounded on the compact backward orbit. The first term tends to zero and the integral is absolutely convergent. This proves the representation and uniqueness. When Theta=0 it immediately gives Omega=0.

## Independent finite-ball verification of statement 1

Assume additionally U is C^1 and divergence-free, as in B2. Then div W=2 beta. For any p>max(1,2 beta/(2-beta)), f=|Theta|^p is C^1, and

    div(W f)=[2 beta+p(beta-2)]f.

For every sufficiently large R, the divergence theorem on B_R gives

    [2 beta+p(beta-2)] integral_B_R f = integral_boundary_B_R f W.n.

The coefficient on the left is strictly negative. The right side is nonnegative because W.n>0. Hence f=0 on B_R. Taking arbitrarily large balls proves Theta=0. This argument never integrates over the whole plane and assumes no L^p integrability. Once Theta=0, apply the same identity to |Omega|^q with q>max(1,2 beta), or use the already proved characteristic formula.

## Dependencies and scope

Only local ODE existence/uniqueness/continuation, elementary Gronwall estimates, and the divergence theorem on a finite ball are used. No literature theorem, canonical inverse, parity, sign assumption, or temperature tail assumption is used in the main proof. Thus the beta<2 exclusion covers the full prompt whenever the stated smoothness and sublinear velocity hold. It says nothing decisive about beta>=2.

The statement does not justify a pointwise asymptotic for Theta_x, a smooth angular limit for Theta, or a power-law vorticity tail. Those require separate hypotheses and proofs.
