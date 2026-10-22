# Restricted exclusions from the forward scattering map

Status: proved informal result, independently checked by the verifier. This audits the lead's `notes/thmE.md` as read on 2026-10-20 at 13:23 UTC. It is not a full exclusion in the prompt's class.

## Statement and hypotheses

Let beta >= 2. Let U be C^1 on the whole plane, divergence free, and put V=U-U(0), W=beta X+V. Suppose that for some delta in (0,1] and a constant C,

    |V(X)| <= C |X|^(1-delta),  |DV(X)| <= C |X|^(-delta),  |X| >= 1.

Let Theta and Omega be C^1 and solve

    W.grad Theta = (beta-2) Theta,
    W.grad Omega + Omega = partial_x Theta.

Assume W_1(0,y)=0 and Theta(0,y)=0 for every y. If any one of the following holds, then Theta=Omega=0:

1. Integral |Omega(X)|(1+|X|)^(-gamma) dX is finite for some gamma <= 2-2/beta.
2. Omega belongs to L^p for some 0 < p <= beta.
3. The integral over |X|>1 of |X_1 Omega(X)|/|X|^2 is finite.

The third condition is absolute integrability of the vertical center-velocity component. It is weaker than condition 1 with gamma=1. They are not equivalent for arbitrary vorticities. The third condition nevertheless gives the same exclusion by the argument below. No inverse relation between U and Omega is needed in this transport theorem; a Boussinesq profile satisfies more equations than are used here.

## 1. Escape and the bounded invariant set

Choose R0 so that W(X).X >= (beta/2)|X|^2 outside the closed ball of radius R0. The C^1 vector field W has at most linear growth, so its flow phi_t exists for every real t. Once a forward trajectory leaves this ball it escapes to infinity. Every backward trajectory remains in a compact ball depending on its starting point.

The set K of points with bounded forward trajectories equals the intersection, over t>=0, of phi_-t(closed B_R0). It is compact and invariant under the whole flow. The Jacobian of phi_t is exp(2 beta t), since div W=2 beta. Invariance and boundedness imply

    exp(2 beta t) |K| = |K| <= pi R0^2,

so |K|=0. Consequently the escape region E=R^2\K is open and dense.

## 2. Scattering coordinates

On an escaping trajectory, first use r'>=beta r/2 to make r^(-delta) integrable. Then integrate

    (log r)' = beta + O(r^(-delta))

to obtain r(t)=c(Y) exp(beta t)(1+o(1)), with c(Y)>0. The estimates are uniform when Y ranges over a compact subset of E: compactness supplies a uniform escape time and lower bound on the radius after that time.

The maps Phi_t(Y)=exp(-beta t)phi_t(Y) converge locally uniformly on E, because their time derivative is exp(-beta t)V(phi_t(Y)), an integrable quantity. For the derivatives write

    D phi_t(Y) = exp(beta t) N_t(Y),
    N'_t = DV(phi_t(Y)) N_t,  N_0=I.

The coefficient is integrable in t, locally uniformly in Y. Thus N_t converges locally uniformly to M_Y. Its determinant is exactly one for every t, because tr DV=0. The limit also has determinant one. It follows from convergence of functions and derivatives that Phi is C^1, D Phi=M, and

    det D Phi=1,
    Phi(phi_s Y)=exp(beta s)Phi(Y),
    Phi(Y) != 0.

In the exterior, estimates starting at t=0 give uniformly

    Phi(Y)=Y+O(|Y|^(1-delta)),
    D Phi(Y)=I+O(|Y|^(-delta)).

These estimates prove global injectivity. If two points have the same Phi image, evolve both by a large positive time s. Each lies within O(exp(beta(1-delta)s)) of the same point exp(beta s)Phi(Y), whose distance from zero is comparable to exp(beta s). The joining segment therefore lies in a ball on which the norm of D Phi-I is less than 1/2. Integrating D Phi along the segment shows that equal images imply equal endpoints. Flow uniqueness then identifies the original points.

The image Phi(E) is open and invariant under every positive dilation. On a sufficiently large circle the map Y -> Phi(Y)/|Phi(Y)| is homotopic to Y -> Y/|Y| through maps avoiding zero, hence has degree one and meets every direction. Dilation invariance then gives Phi(E)=R^2\{0}. Thus Phi is a C^1 diffeomorphism onto the punctured plane. This proof does not identify K with a point or assume that the source basin is the whole plane.

## 3. Temperature and vorticity along an orbit

Define Q=Theta composed with Phi inverse. Then Q is C^1 on the punctured plane and homogeneous of degree alpha=1-2/beta. Differentiating the exact temperature transport identity gives, locally uniformly for Y in E,

    grad Theta(phi_t Y)
      = exp(-2t) [M_Y^(-T) grad Theta(Y)+o(1)]
      = exp(-2t) [grad Q(Phi(Y))+o(1)].

Put g(Y)=partial_1 Q(Phi(Y)). This is continuous. The vorticity integrating factor is integrable at positive infinity, so

    A(Y) = Omega(Y) + integral_0^infinity exp(s) partial_x Theta(phi_s Y) ds

exists and is continuous locally on E. Integrating back from infinity gives

    Omega(phi_t Y) = exp(-t) A(Y) - exp(-2t)[g(Y)+o(1)].

The remainder is locally uniform. The exact scaling identities are

    A(phi_s Y)=exp(-s) A(Y),
    g(phi_s Y)=exp(-2s) g(Y).

This is a trajectory expansion. It does not by itself identify the second coefficient in an expansion at fixed Euclidean polar angle when A is nonzero. The difference Phi(X)-X can contribute at the same order or at an intervening order.

## 4. Escape coordinates and integrability

Take a circle S of radius R1>R0. Every exterior point lies on exactly one positive-time trajectory from S. With arc length d ell on S, its area element is

    dX = exp(2 beta t) (W.n)(sigma) dt d ell(sigma),

because D phi_t transports W and has determinant exp(2 beta t). Here W.n is positive. The radius is comparable to exp(beta t), uniformly on S.

For condition 1, Tonelli's theorem makes the time integral finite for almost every sigma. If A(sigma) is nonzero, its positive absolute integrand is asymptotic to a positive constant times exp((2 beta-gamma beta-1)t), whose exponent is at least 1. Thus A=0 almost everywhere on S. For such sigma, nonzero g instead gives exponent 2 beta-gamma beta-2 >= 0. This again diverges, including the equality case. Hence g=0 almost everywhere and, by continuity, everywhere on S.

For condition 2, the two exponents are 2 beta-p and 2 beta-2p. For any p in (0,beta], the first is positive and the second nonnegative. The same argument applies. This uses no triangle inequality or norm convexity, so p<1 is allowed.

For condition 3, along an orbit with Phi_1(sigma) != 0,

    |(phi_t sigma)_1|/|phi_t sigma|^2
      is comparable to exp(-beta t).

There are exactly two exceptional points of S. Indeed the direction map Phi(S)->unit circle is bijective: injectivity and the flow conjugacy identify two points with the same direction, and surjectivity was proved above. The two exceptional directions are the vertical rays. Away from them the exponents for the absolute integral are beta-1 for A and beta-2 for g. They are respectively positive and nonnegative for beta>=2. Tonelli and continuity again give g=0 on all of S.

Every orbit in E meets S, so the scaling identity propagates g=0 to E. Therefore partial_1 Q=0 on the punctured plane.

## 5. The symmetry axis removes the remaining temperature

On each half plane Z_2>0 and Z_2<0, the function Q depends only on Z_2. Homogeneity gives Q=C_+ Z_2^alpha and Q=C_- |Z_2|^alpha, respectively. This includes alpha=0, when the values are constants. The original y-axis is invariant because W_1 vanishes there. For large positive and negative y,

    Phi(0,y)=(0,y+O(|y|^(1-delta))).

Since Theta(0,y)=0, this sets both constants to zero. Continuity sets Q=0 on the remaining horizontal axis in the punctured plane. Thus Theta vanishes on E and, by density, everywhere.

Finally Omega(phi_-t Y)=exp(t)Omega(Y), because its forcing now vanishes. Backward orbits are compactly trapped, so continuity forces Omega(Y)=0 for every Y.

## Scope and audit verdict

CONFIRMED: the main theorem in the lead's draft under its explicit H1 and either H2(a) or H2(b). The proof above also permits p<1 and proves the actual component-integrability variant separately.

REFUTED as an equivalence for arbitrary fields: radial weighted L^1 integrability equals absolute convergence of one center-velocity component. A narrow angular concentration can make the latter finite and the former infinite. The equivalence is unnecessary for the repaired exclusion.

OPEN in the full prompt class: the derivative decay bound in H1 does not follow from sublinear velocity alone, and the weighted vorticity hypotheses are substantial restrictions. Nonintegrable tails remain allowed. This theorem cannot authorize the full NO endpoint.

Dependencies: elementary C^1 ODE flow theory, the change-of-variables formula, Tonelli's theorem, and degree one for a circle map homotopic to the identity. No numerical computation is used as proof.
