# Exact scattering Lamb identity and the leading displacement

## Statement and hypotheses

Let 1/3<c<1 and omega be any finite real number. Put A=cI-omega J, B=Ay+U, and Omega=curl U. Assume U,P are C2 global solutions of the rotating profile equation, U is bounded, U(R times .) tends to zero in distributions as R tends to infinity, and

    integral_1^infinity sup_(|y|>=r)|DU(y)| dr/r < infinity.

Let K be the forward-bounded set of B, let S be the scattering diffeomorphism from R3\K to R3\{0}, and let Omega_tilde=S_*Omega and U_tilde be its Biot-Savart velocity, as in A209-A210. Put H=P+|U|^2/2+(Ay).U and k=(1-c)/c. Then:

1. For c!=1/2,
   (1-2c)U_tilde=Az cross Omega_tilde-grad(Az.U_tilde).
   The gradient is classical because the continuous scalar on its right has a continuous distributional gradient.
2. There is a C1 function psi on R3\{0} such that
   (S^(-1))* (U.dy)-U_tilde.dz=d psi.
   In particular circulation is preserved for every closed piecewise C1 curve C in R3\K:
   integral_C U.dy=integral_(S(C)) U_tilde.dz.
3. For c!=1/2, on R3\K,
   U.dy-S*(U_tilde.dz)=-(1-2c)^(-1)d[H-(AS).U_tilde(S)].
4. Uniformly as |y| tends to infinity,
   S(y)-y=U_tilde(y)+o(|y|^(-k)).

These are conditional on the stated Dini bound. They do not supply a signed obstruction or a classification of all possible asymptotic constraints.

## Proof

A209-A210 give det DS=1, S_*B=Az, Omega_tilde continuous and distributionally divergence free on R3, and curl U_tilde=Omega_tilde. They also give the twisted homogeneity

    Omega_tilde(exp(sA)z)=exp(-s) exp(-omega sJ)Omega_tilde(z),
    U_tilde(exp(sA)z)=exp(-(1-c)s) exp(-omega sJ)U_tilde(z),

and U=U_tilde+o(|y|^(-k)) uniformly. The scattering displacement obeys |S(y)-y|<=d=sup|U|/c, and h_t(y)=exp(-tA)Phi_t(y) obeys |h_t(y)-y|<=d.

Write a0=1-2c and V_tilde=(Az cross Omega_tilde)/a0. Contraction of the volume form and the homogeneity of Omega_tilde show

    d(V_tilde.dz)=i_(Omega_tilde)vol

in distributions away from zero. Hence the continuous one-form l=U_tilde.dz-V_tilde.dz is closed. Its pullback by exp(sA) is exp((2c-1)s)l. Cartan's formula gives

    d(i_(Az)l)=(2c-1)l.

Since Az.V_tilde=0, the contraction is Az.U_tilde. Rearranging proves item 1. The right side identifies all distributional first derivatives of this scalar as continuous functions, which supplies its C1 representative (equal to the already continuous scalar).

For item 2, exterior differentiation commutes distributionally with pullback of the smooth form U.dy by the C1 map S^(-1). This follows locally by approximating that map in C1 by smooth maps; both the one-form pullbacks and their known two-form derivatives converge uniformly. Volume preservation and the pushforward definition give

    d[(S^(-1))*(U.dy)]=i_(Omega_tilde)vol=d(U_tilde.dz).

A continuous distributionally closed one-form has a local C1 potential, by mollification and the local Poincare lemma. Simple connectivity of R3\{0} makes the local potentials globally compatible up to constants. Integration gives the circulation assertion.

The exact profile Lamb relation is a0 U=B cross Omega-grad H. Volume preservation and both vector-field pushforwards imply

    U.dy=S*(V_tilde.dz)-a0^(-1)dH.

Item 1 gives S*(U_tilde.dz)=S*(V_tilde.dz)-a0^(-1)d[(AS).U_tilde(S)]. Subtracting proves item 3, including its sign.

For item 4 use

    S(y)-y=integral_0^infinity exp(-tA)U(Phi_t y)dt.

Write U=U_tilde+f, with |f(x)|<=epsilon(|x|)|x|^(-k), where epsilon decreases to zero. Homogeneity gives the exact identity

    exp(-tA)U_tilde(Phi_t y)=exp(-t)U_tilde(h_t(y)).

Normalize y=exp(sA)w, |w|=1. The bound |h_t(y)-y|<=d implies |exp(-sA)h_t(y)-w|<=d/|y|. Uniform continuity of U_tilde on a fixed compact annulus therefore gives

    U_tilde(h_t(y))-U_tilde(y)=o(|y|^(-k))

uniformly for all t>=0. Integrating against exp(-t), whose integral is one, gives the main term and a uniform little-o remainder.

Finally |Phi_t y|>=(|y|-d)exp(ct) for large |y|. Since c(1+k)=1,

    |exp(-tA)f(Phi_t y)|
       <=exp(-t)epsilon(|y|-d)(|y|-d)^(-k).

Its integral is o(|y|^(-k)). This proves item 4 for the full range 1/3<c<1, including c=1/2.

## Dependencies and audit scope

The input scattering and tail theorems are proved in the team records and in the team records. The inspected new source is in the team records, equations (4.4'), (4.6)-(4.8). No numerical work, stronger derivative decay, or convergence of second derivatives is needed. In particular continuous Omega_tilde is sufficient; smoothness of the scattering map beyond C1 is not assumed.
