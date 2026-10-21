# Critical source discontinuity at the exceptional value

Date: 2026-10-20. Status: complete informal proof, independent review pending. This strengthens the axis-data topology statement, without constructing a coupled profile.

## Statement and notation

Fix A>2, beta=2/A, L>0. Suppose w_0 is smooth on [0,L], odd and analytic near zero, with simple endpoint zeros, w_0'(0)=-A, w_0'(L)=A and w_0<0 on (0,L). Let g_0 solve

    w_0 g_0'=(w_0'-A)g_0,       g_0/x^2 -> 1 at zero,

and assume it extends smoothly and positively to L. For every compatible w define g with the same normalization, and put

    Q=(g'-w'')/(2g^3),  m=-w/g,  W=m^(beta-2)/g,
    B[w]=(beta-1)A^(1-beta)/3
          * FP integral_0^L (Q-Q(L))W dx.                    (1)

The finite part is in x at zero, with divergent powers removed and no added constant. Then B is discontinuous at w_0 in C^(2,1-beta)[0,L], with no exception for g_0(L)=2A-2. The approximating traces can be smooth and equal to w_0 on neighborhoods of both endpoints. In fact any prescribed finite nonzero jump can be obtained along a sequence tending to w_0 in this norm.

When g_0(L) differs from 2A-2 this follows from the single source construction in ../source-critical/PROOF.md, with its amplitude multiplied by a fixed constant. The issue here is the exceptional value. Its zero leading coefficient does not persist under arbitrarily small interior changes of the normalized axis data.

## Moving the source density by an interior perturbation

Assume henceforth g_*=g_0(L)=2A-2. Choose h nonnegative, smooth, not identically zero, with compact support in (L/4,L/2), and set

    w_t=w_0+t h,     I=integral_0^L h/w_0^2 dx > 0.

For small t of either sign, w_t stays negative and has all the same endpoint germs as w_0. Write g_t for its normalized density. Integration of the logarithmic first equation gives exactly

    log(g_t/g_0)=log(1+t h/w_0)
                -A integral_0^x (1/w_t-1/w_0) du.              (2)

Past the support of h, g_t=lambda_t g_0, where

    log lambda_t=A I t+O(t^2),
    g_t(L)=g_*+A g_* I t+O(t^2).                              (3)

The error estimates are uniform for |t| small because w_0 is bounded away from zero on the fixed support. The densities are positive, smooth, and identical to g_0 near zero. Near L they are constant multiples of g_0, so compatibility is preserved.

We also have B[w_t]-B[w_0]=O(t). On a fixed interior interval this follows from (2) and differentiation. Near L, Q_t-Q_t(L)=O(L-x) with constants and differences bounded by C and C|t| respectively, and W_t is comparable to (L-x)^(beta-2). Thus the difference of the integrands in (1) is O(|t|(L-x)^(beta-1)), which is integrable. Near zero, the only difference is the subtraction of Q_t(L); it is O(|t|) times W_0=O(x^(-beta)), also integrable. The divergent center terms cancel exactly. These bounds prove the assertion using an ordinary integral of the difference.

## A source layer with separate amplitude and length

Fix 0<d_0<min(1,L/4), and a smooth cutoff chi with values in [0,1], equal to zero for arguments at most zero and one for arguments at least one. For delta=L-x, T>=3 and real epsilon sufficiently small, define

    a_T(delta)=chi(log(d_0/delta))
                *chi(T+2-log(d_0/delta)),
    v_(epsilon,T)(x)=epsilon delta^(3-beta) a_T(delta).        (4)

Extend this by zero outside 0<delta<d_0. It is smooth, flat at both support endpoints, and zero near both 0 and L. Its support has logarithmic length T+2. The estimates

    |d_delta^i v_(epsilon,T)|
        <= C_i |epsilon| delta^(3-beta-i),  i=0,1,2,3,
    ||v_(epsilon,T)||_(C^(2,1-beta)) <= C |epsilon|           (5)

hold uniformly in T. To check the Holder bound, let alpha=1-beta. The second derivative has modulus at most C|epsilon|delta^alpha and derivative at most C|epsilon|delta^(alpha-1). For two arguments d<e, use the amplitude bounds if e-d>=d/2; otherwise integrate the derivative bound. Both cases give C|epsilon|(e-d)^alpha. The estimates hold through the smooth zero extensions.

For all small |t| and |epsilon|, uniformly in T,

    B[w_t+v_(epsilon,T)]-B[w_t]
      =epsilon (T+c_chi) K(g_t(L))
                    +O(|epsilon|+epsilon^2(T+2)),             (6)
    K(g)=(1-beta)(3-beta)(2-beta-g/A)/(6A g^(beta+2)),
    c_chi=2 integral_0^1 chi(u)du.

Here is the full error estimate underlying (6). On the source segment w_t=w_0, and g_t=lambda_t g_0. Their fixed-order derivatives, positive lower bounds for g_t, and bounds for -w_t/delta are uniform for |t| small. Let g_new be rebuilt from w_t+v, eta=log(g_new/g_t), eta_*=eta(L), zeta=eta-eta_*. Equation (2) applied to v gives

    |eta_*|<=C|epsilon|,
    |zeta|<=C|epsilon|delta^(2-beta),
    eta'=-v'/(A delta)+O(|epsilon|delta^(2-beta))
                            +O(epsilon^2 delta^(3-2beta)).    (7)

The exact derivative is eta'=v'/(w_t+v)+(A-w_t')v/[w_t(w_t+v)]. The source expansions and (5) prove (7), with constants uniform in t,T. Below the support zeta=0.

Put lambda=exp(eta_*), G=g_t'/(2g_t^3), V=-w_t''/(2g_t^3), Qbar=lambda^(-2)G+lambda^(-3)V and Wbar=lambda^(1-beta)W_t. Then Qbar(L)=Q_new(L), and exactly

    Q_new=lambda^(-2)e^(-2zeta)G
          +lambda^(-3)e^(-3zeta)V
          +lambda^(-2)e^(-2zeta)eta'/(2g_t^2)
          -lambda^(-3)e^(-3zeta)v''/(2g_t^3),
    W_new/Wbar=(1+v/w_t)^(beta-2)e^(-(beta-1)zeta).

The smooth comparison term

    (Qbar-Qbar(L))Wbar-(Q_t-Q_t(L))W_t

is O(|epsilon|delta^(beta-1)). Further,

    W_t=A^(beta-2)g_t(L)^(1-beta)delta^(beta-2)(1+O(delta)).

Substitution of these identities yields

    (Q_new-Q_new(L))W_new-(Q_t-Q_t(L))W_t
      =-A^(beta-2)/(2g_t(L)^(beta+2))
          *[v''+(g_t(L)/A)v'/delta]delta^(beta-2)+E,
    |E|<=C|epsilon|[1+delta^(beta-1)]
                     +C epsilon^2 delta^(-1)1_support(v).    (8)

To account for all errors, changes of the smooth terms due to zeta cost O(|epsilon|) after multiplication by W_t. The remainder in eta' in (7) costs O(|epsilon|)+O(epsilon^2 delta^(1-beta)). Replacing g_t(x) and W_t by their leading source values in the v terms costs O(|epsilon|). The relative weight change is O(|epsilon|delta^(2-beta)); its product with the singular v terms is O(epsilon^2 delta^(1-beta)) and with Qbar-Qbar(L)=O(delta) is O(|epsilon|delta). Replacing lambda by one in the leading v terms costs O(epsilon^2 delta^(-1)) on their support. These are precisely bounded by the right side of (8), after a fixed enlargement of C.

Integration of (8) gives error O(|epsilon|+epsilon^2(T+2)). Outside the source segment the rebuilt density is unchanged from g_t, and only the changed Q(L) contributes to (1); its integral is O(|epsilon|), including the integrable x^(-beta) center weight. Thus the difference of finite parts is an ordinary convergent integral. Multiplication by the prefactor in (1), followed by two and one integrations by parts in delta, gives the leading term

    K(g_t(L)) integral_0^d_0 v delta^(beta-4)d_delta
      =K(g_t(L)) epsilon (T+c_chi).

All boundary terms vanish because v and its first derivative are flat at d_0 and zero near zero. This proves (6), including the required uniformity and the sign of its coefficient.

## The exceptional sequence and its nonzero jump

At g_*=2A-2 we have 2-beta-g_*/A=0 and

    K(g_*)=0,
    K'(g_*)=-(1-beta)(3-beta)/(6A^2 g_*^(beta+2)).             (9)

Take t_n=1/n, epsilon_n=1/n^2 and T_n=n^3, for integers n large enough to preserve negativity. Define

    w_n=w_(t_n)+v_(epsilon_n,T_n).

Equations (5) and the fixed smooth h imply ||w_n-w_0||_(C^(2,1-beta))=O(1/n). Each w_n has the same w germs as w_0 at both endpoints. Its density remains smooth and positive by (2) and (7). Equations (3), (6), and (9) give

    B[w_n]-B[w_(t_n)]
      =(n+O(n^(-2)))
          *[K'(g_*) A g_* I/n+O(n^(-2))]+O(1/n)
      -> -(1-beta)(3-beta) I/(6A g_*^(beta+1)) < 0.          (10)

Since B[w_(t_n)]-B[w_0]=O(1/n), the same nonzero limit holds relative to w_0. This proves discontinuity at the exceptional value. Multiplying epsilon_n by any fixed nonzero real constant multiplies this limit by that constant while leaving the error O(1/n) and the norm convergence unchanged. Hence every finite nonzero jump can be prescribed.

## Scope and dependencies

Formula (1) and its endpoint conventions follow from the exact compatible axis ODE as proved in ../critical-norm/PROOF.md. The source-layer estimate extends the already reviewed calculation in ../source-critical/PROOF.md by separating amplitude and logarithmic length; the uniform remainder is given explicitly here. No numerical limit is used as proof. The only additional ingredient is a compact interior perturbation that changes the globally normalized source density.

This removes an exception from an axis-data continuity statement. It does not realize these traces by a canonical two-dimensional profile, remove any source regularity hypothesis, determine the dimension of a coupled family, or establish either strong-setting endpoint. If one additionally fixes g(L) exactly, the present exceptional construction is unavailable and no conclusion for that smaller class is asserted.
