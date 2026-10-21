# The source multiplier in the critical axis functional

Date: 2026-10-20. Status: complete informal argument, written before the associated checks. Independent review pending. The result concerns compatible axis data only.

## Statement

Fix A>2, beta=2/A, and L>0. Let w,g be a smooth compatible pair on [0,L] with

    w g'=(w'-A)g,       g/x^2 -> 1 at zero,
    w(0)=w(L)=0,       w'(0)=-A,       w'(L)=A,
    w<0 on (0,L),      g>0 on (0,L].

Assume w is odd analytic near zero, and write g_*=g(L). For each perturbed w_v=w+v, rebuild g_v from the same normalized first equation. Define

    Q=(g'-w'')/(2g^3),       m=-w/g,       W=m^(beta-2)/g,
    B[w]=(beta-1)A^(1-beta)/3
          * FP integral_0^L (Q-Q(L))W dx.                     (1)

The finite part removes the divergent powers in the physical coordinate x at zero, with no added constant. Its definition and compatibility with the third axis equation are those proved in ../critical-norm/PROOF.md.

There is a sufficiently small fixed d_0 in (0,min(1,L/2)) with the following property. Let v be smooth on [0,L], identically zero for x<=L-d_0 and on a neighborhood of L. At x=L-d_0 it is flat; its closed support may contain this boundary point. Put

    e(v)=max_(i=0,1,2) sup_(0<delta<d_0)
                     delta^(i-3+beta)|v^(i)(L-delta)|,
    J(v)=integral_0^d_0 v(L-delta) delta^(beta-4) d_delta,
    K(s)=(1-beta)(3-beta)(2-beta-s/A)/(6A s^(beta+2)).

There are e_0,C>0 depending only on the fixed base and d_0 such that, for every such v with e(v)<=e_0,

    |B[w+v]-B[w]-K(g_v(L))J(v)| <= C e(v).                  (2)

The source value in (2) is the actual rebuilt g_v(L), rather than the original g_*. No bound for J(v) in terms of e(v) alone is asserted. Every integral J(v) is nevertheless finite for each individual v, because v vanishes on a neighborhood of L.

As a consequence, at the exceptional base g_*=2A-2 there is a sequence consisting only of source-supported perturbations for which

    ||v_n||_(C^(2,1-beta)[0,L]) -> 0,
    B[w+v_n]-B[w] -> -kappa < 0,                            (3)

where kappa is given explicitly below. The perturbations and rebuilt densities are smooth and keep the w germs at both endpoints. They change g(L). Thus (3) does not contradict the fixed-source-value estimate in ../source-fixed-value/PROOF.md.

## Normalization with the source multiplier kept exact

Write e=e(v). Since w(L-delta)=-A delta+O(delta^2), we can choose d_0 so that -w/delta and g are bounded above and below by positive constants on the source segment. For small e,

    |v/w| <= C e delta^(2-beta) <= 1/2.

Thus w+v is negative there. The normalized first equation gives the exact formula

    eta(x)=log(g_v(x)/g(x))
           =log(1+v(x)/w(x))
                -A integral_0^x [1/(w+v)-1/w] du.           (4)

The original endpoint germs are preserved because v is zero near both endpoints. In particular g_v is positive and smooth, agrees with g before the source segment, and is a positive constant multiple of g near L. Set

    eta_s=eta(L),       lambda=exp(eta_s),
    s=g_v(L)=lambda g_*,       zeta=eta-eta_s.

The integrand in (4) has absolute value at most C e delta^(1-beta). Hence

    |eta_s| <= C e,       |lambda-1| <= C e.

Subtracting (4) at L gives

    zeta(x)=log(1+v/w)
                +A integral_x^L [1/(w+v)-1/w] du,
    |zeta(x)| <= C e delta^(2-beta).                         (5)

Differentiating (4) gives, exactly,

    eta'=v'/(w+v)+(A-w')v/[w(w+v)].

The source expansion w=-A delta+O(delta^2), w'=A+O(delta), together with the bounds defining e, therefore gives

    eta'=-v'/(A delta)+O(e delta^(2-beta))
                              +O(e^2 delta^(3-2beta)).       (6)

Here and below derivatives marked by a prime are with respect to x. Constants in (5) and (6) are independent of the number, lengths and distances to L of the components of the support. No third derivative of v is used.

## Uniform remainder in the finite-part functional

Introduce the smooth base functions

    G=g'/(2g^3),       V=-w''/(2g^3),
    Qbar=lambda^(-2)G+lambda^(-3)V,
    Wbar=lambda^(1-beta)W.

Since v is zero near L, Qbar(L)=Q_v(L). Exact substitution of g_v=lambda exp(zeta)g gives

    Q_v=lambda^(-2)e^(-2zeta)G
         +lambda^(-3)e^(-3zeta)V
         +lambda^(-2)e^(-2zeta)eta'/(2g^2)
         -lambda^(-3)e^(-3zeta)v''/(2g^3),
    W_v/Wbar=(1+v/w)^(beta-2)e^(-(beta-1)zeta).             (7)

Moreover,

    W=A^(beta-2)g_*^(1-beta)delta^(beta-2)(1+O(delta)),
    Qbar-Qbar(L)=O(delta).

The constants here and their fixed-order base derivatives are uniformly bounded for small e, because lambda remains in a fixed compact positive interval. Comparing the smooth terms at multiplier lambda and multiplier one costs

    (Qbar-Qbar(L))Wbar-(Q-Q(L))W
                 =O(e delta^(beta-1)).                     (8)

Apply (5), (6) and (7) to the remaining terms, keeping lambda in every leading coefficient. The result is

    (Q_v-Q_v(L))W_v-(Q-Q(L))W
       =-A^(beta-2)/(2s^(beta+2))
          [v''+(s/A)v'/delta]delta^(beta-2)+E(delta),
    |E(delta)| <= C e[1+delta^(beta-1)]
                            +C e^2 delta^(1-beta).          (9)

For completeness, the individual error estimates are as follows. Changes in G and V through zeta are O(e delta^(2-beta)), and multiplication by Wbar makes them O(e). The two errors in eta' in (6) become O(e) and O(e^2 delta^(1-beta)). Replacing smooth g(x) and the factor Wbar/delta^(beta-2) by their source values in terms containing v' or v'' introduces a relative O(delta), and hence an O(e) error. The relative change W_v/Wbar-1 is O(e delta^(2-beta)); its product with the leading v terms is O(e^2 delta^(1-beta)), and its product with Qbar-Qbar(L) is O(e delta). Equation (8) supplies the remaining integrable term. The leading v'' coefficient is lambda^(-beta-2) times its base coefficient, and the leading v' coefficient is lambda^(-beta-1) times its base coefficient. These are exactly the coefficients expressed by s in (9). No replacement lambda=1 is made. In particular no e^2/delta error is introduced.

All three powers in the remainder in (9) are integrable at delta=0 since 0<beta<1. On [0,L-d_0], w_v=w and g_v=g, so the only change in the integrand in (1) is the subtraction of Q_v(L)-Q(L)=O(e). The weight W is integrable there: near zero it is O(x^(-beta)), since w=-A x+O(x^3) and g=x^2+O(x^4). Thus the difference of the two finite parts is an ordinary convergent integral, with an O(e) contribution from this part of the interval. This also proves that no origin constant or boundary term has been discarded.

Multiplication of (9) by the prefactor in (1), and the change of variable x=L-delta, give

    B[w+v]-B[w]
       =(1-beta)/(6A s^(beta+2))
          integral_0^d_0 [d_delta^2 v-(s/A)d_delta v/delta]
                               delta^(beta-2)d_delta
          +O(e+e^2).                                      (10)

Here v in the integral denotes v(L-delta). Two integrations by parts for the second derivative and one for the first derivative yield

    integral [d_delta^2 v-(s/A)d_delta v/delta]delta^(beta-2)
          =(3-beta)(2-beta-s/A) J(v).                       (11)

All endpoint terms vanish. At delta=0 the function is zero on a neighborhood; at delta=d_0 it and its first derivative are flat. The integrals are ordinary finite integrals for each v, even when J(v) is large. Equations (10) and (11), followed by e<=e_0, prove (2).

## A single source plateau at the exceptional base

Choose a smooth chi with values in [0,1], zero on (-infinity,0] and one on [1,infinity). For T>=3 set

    a_T(delta)=chi(log(d_0/delta))
                    chi(T+2-log(d_0/delta)),
    v_(epsilon,T)(L-delta)=epsilon delta^(3-beta)a_T(delta)
                                  for 0<delta<d_0,           (12)

and extend by zero. Each v is smooth, flat at delta=d_0, and zero near delta=0. Its derivatives satisfy

    |d_delta^i v| <= C_i |epsilon|delta^(3-beta-i),
                                      0<=i<=3.

The C^(2,1-beta) norm is at most C|epsilon| independently of T. To see the seminorm estimate, set alpha=1-beta. The second derivative is bounded by C|epsilon|delta^alpha and its derivative by C|epsilon|delta^(alpha-1). For d<e, use the amplitude bounds when e-d>=d/2 and integrate the derivative bound otherwise. Both cases give C|epsilon|(e-d)^alpha. The same bounds apply across the smooth zero extensions.

Changing to t=log(d_0/delta) gives exactly

    J(v_(epsilon,T))=epsilon(T+c_chi),
    c_chi=2 integral_0^1 chi(t)dt.                           (13)

Define a strictly positive finite number

    I_infinity=integral_0^d_0
            delta^(3-beta)chi(log(d_0/delta))/w(L-delta)^2
                                                    d_delta.

Its finiteness follows from the upper bound C delta^(1-beta) near zero. Applying (4) at L yields

    log lambda=A integral_0^L v/[w(w+v)] dx
        =A epsilon I_T+O(epsilon^2),
    I_T=integral_0^d_0 delta^(3-beta)a_T(delta)/w(L-delta)^2
                                                    d_delta,
    |I_T-I_infinity|<=C exp(-(2-beta)T).                     (14)

The quadratic error is uniform in T, because v^2/|w|^3 is bounded by C epsilon^2 delta^(3-2beta), which is integrable. The final estimate in (14) holds because a_T differs from the first cutoff only for log(d_0/delta)>=T+1. Consequently,

    s=g_*+A g_* I_infinity epsilon
               +O(epsilon^2+|epsilon|exp(-(2-beta)T)).        (15)

Assume now g_*=2A-2. Direct differentiation gives

    K(g_*)=0,
    K'(g_*)=-(1-beta)(3-beta)/(6A^2 g_*^(beta+2)).            (16)

Take epsilon_n=1/n and T_n=n^2 for sufficiently large integers n. Equations (2), (13), (15) and (16) imply

    B[w+v_n]-B[w]
       =K(s_n)(n+c_chi/n)+O(1/n)
       -> K'(g_*) A g_* I_infinity
        =-(1-beta)(3-beta) I_infinity/(6A g_*^(beta+1)).     (17)

This proves (3) with the positive kappa given by (17). Every error tends to zero: the quadratic Taylor error in K times n is O(1/n), the uniform error in (2) is O(1/n), and the exponential term times n is O(exp(-(2-beta)n^2)). If epsilon_n=a/n with fixed real a, the same argument gives the limit -a^2 kappa. This particular one-plateau construction gives a negative jump for either sign of a; it does not claim an arbitrary signed jump from this restricted form.

## Dependencies and scope

The proof uses the normalized first axis equation, the finite-part formula (1), smooth source expansions, ordinary integrations by parts and a uniform Taylor estimate on positive scalar powers. It sharpens the remainder accounting in ../source-exception/PROOF.md. Unlike that construction it needs no separate interior perturbation. At the exceptional base and the exact constraint g_v(L)=g_*, (2) immediately gives the fixed-source estimate of ../source-fixed-value/PROOF.md because K(g_*)=0.

This result does not prescribe a canonical two-dimensional velocity, construct a coupled profile, prove a PDE stability estimate, or settle either endpoint. It shows that controlling the critical size of an axis perturbation and approximately preserving its source value is insufficient when its weighted source integral can grow. Numerical checks of the algebra are supplementary to the complete argument above.
