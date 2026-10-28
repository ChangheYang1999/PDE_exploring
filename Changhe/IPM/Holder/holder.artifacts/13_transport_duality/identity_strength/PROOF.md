# The identity term as an exact joint variational problem

## Statement, spaces and notation

Fix 0<alpha<1. Use real functions on R^2 with the Euclidean seminorm

    [f]_alpha = sup_(z != w) |f(z)-f(w)|/|z-w|^alpha,

modulo constants. The circular principal values and the homogeneous increment extension are those of ../../01_setup/PROOF.md. In particular,

    T_xx = R_1^2 + I/2,   T_xy = R_1 R_2,   S = T_xx + i T_xy.

Put x=(1/2,0), y=(-1/2,0), and let B be the normalized unit ball of real functions with f(0)=0 and [f]_alpha<=1. For f in B define

    A(f) = T_xx f(x)-T_xx f(y),
    B_1(f) = T_xy f(x)-T_xy f(y),
    r(f) = sqrt(A(f)^2+B_1(f)^2),
    j(f) = f(x)-f(y).

For real t define N_alpha(t)=||T_xx-tI|| on this real homogeneous space. Then

    N_alpha(t) = max_(f in B) [r(f)+|t| |j(f)|].                 (1)

In particular, with C_alpha=N_alpha(0) and D_alpha=N_alpha(1/2),

    C_alpha = max_B r(f),
    D_alpha = max_B [r(f)+|j(f)|/2].                            (2)

All maxima in (1) and (2) exist. They have the same supremum if B is replaced by real smooth compactly supported functions with seminorm at most one and arbitrary additive normalization; attainment in that smaller class is not asserted.

The function N_alpha is even, convex and 1-Lipschitz on R. It is nondecreasing on [0,infinity), and

    max(C_alpha, |t|+1/2) <= N_alpha(t) <= C_alpha+|t|.          (3)

Let M_t be the nonempty compact set of maximizers in (1), for t>=0. Write

    q_-(t)=min_(f in M_t)|j(f)|,
    q_+(t)=max_(f in M_t)|j(f)|.

For t>0, the one-sided derivatives satisfy

    N_alpha'(t-) = q_-(t),   N_alpha'(t+) = q_+(t).              (4)

At zero, N_alpha'(0+)=q_+(0) and N_alpha'(0-)=-q_+(0).

Consequently, if a C_alpha-maximizer has a nonzero input jump j, then

    D_alpha >= C_alpha+|j|/2 > C_alpha.                         (5)

If C_alpha=D_alpha, every C_alpha-maximizer has j=0 and N_alpha is constant on [0,1/2]. The converse assertion that j=0 for every C_alpha-maximizer implies C_alpha=D_alpha is NOT claimed. A zero initial derivative does not imply a constant convex function.

## Reduction to one pair and all phases

Translation and positive dilation of the input preserve the ratio defining the operator seminorm; dilation scales both input and output increments by the same factor. Rotate a general pair of distinct points onto the horizontal axis and use the verified identity

    U_beta^(-1) T_xx U_beta = cos(2beta)T_xx+sin(2beta)T_xy.

The identity operator is unchanged under every such conjugacy. Thus

    N_alpha(t)
      = sup_(f in B, phi in [0,2pi])
          |cos(phi)A(f)+sin(phi)B_1(f)-t j(f)|.                (6)

Every phase is obtained because phi=2beta covers the phase circle. The converse direction in this reduction follows by rotating a fixed-pair test back to the original operator, so (6) is an equality rather than an upper bound.

For fixed f, the quantity cos(phi)A(f)+sin(phi)B_1(f) ranges over the full interval [-r(f),r(f)]. For any r>=0 and c in R,

    max_(u in [-r,r]) |u-c| = r+|c|.

Substituting c=t j(f) proves (1) with a supremum.

## Compactness and attainment

The normalized ball B is compact in local uniform convergence by Arzela-Ascoli on successive disks and a diagonal argument. Its elements satisfy |f(z)|<=|z|^alpha. The proof in ../extremizer_existence/PROOF.md gives continuity of both singular increments on B by approximation with finite compactly supported measures and a common vanishing pole/exterior error. Point evaluation, and hence j, is continuous in this topology. Therefore r+|t||j| is continuous on B and attains its maximum. The same argument proves compactness of M_t and existence of q_- and q_+.

The approximation theorem in ../../02_upper_bounds/PROOF.md preserves the seminorm bound asymptotically and converges at every fixed operator increment, including the identity term. It transfers all suprema to compact smooth inputs. No density in the full Holder seminorm is used.

## Convexity, bounds and one-sided derivatives

Equation (1) is a supremum of the convex even functions t -> r(f)+|t||j(f)|, with 0<=|j(f)|<=1. It is therefore even, convex, 1-Lipschitz and nondecreasing for t>=0. Its value at zero is C_alpha, proving the first lower bound and the upper bound in (3). The input f(z)=cos(z_1) satisfies T_xx f=-f/2 modulo constants and has finite nonzero seminorm. It proves N_alpha(t)>=t+1/2 for t>=0. Evenness gives the other half of (3).

We give the derivative proof because compactness of the maximizing set matters. Put F(t)=N_alpha(t) for t>=0 and q(f)=|j(f)|. Fix t>=0. For a maximizer f in M_t,

    F(t+h) >= F(t)+h q(f),    h>0.

Taking q(f)=q_+(t) bounds the right difference quotient below by q_+(t). Conversely, choose a maximizer f_h at t+h. Since F(t)>=r(f_h)+t q(f_h),

    [F(t+h)-F(t)]/h <= q(f_h).

For any sequence h decreasing to zero, compactness gives a subsequence f_h converging locally uniformly. Continuity and the 1-Lipschitz bound for F imply that every such limit belongs to M_t. Hence every corresponding limiting slope is at most q_+(t). This proves F'(t+)=q_+(t), including at t=0.

For t>0 and 0<h<t, a maximizer in M_t with q=q_-(t) gives

    [F(t)-F(t-h)]/h <= q_-(t).

A maximizer f_h in M_(t-h) gives the opposite lower bound by q(f_h). Every convergent subsequence tends to a member of M_t, so the limiting lower bound is at least q_-(t). This proves the left derivative formula. At zero, evenness determines the left derivative.

Finally evaluate (1) at t=1/2 using a C_alpha-maximizer to obtain (5). If the endpoint values F(0) and F(1/2) agree, monotonicity makes F constant on that interval. Equation (5) then forces j=0 for every C_alpha-maximizer. This proves all stated implications.

## Scope and unresolved strictness

The result reorganizes the already defined operator norms; it introduces no numerical upper or lower endpoint. It does not establish C_alpha<D_alpha for every exponent. In particular, a maximizing trace-free witness can have equal values at the two increment points, and the argument does not produce a different maximizing witness with nonzero jump. The existing certified strict gaps and the existing small-alpha separation remain the only accepted global comparisons unless a further argument is supplied.

Dependencies: the setup and rotation proof, the compact smooth approximation theorem, and the compactness and continuity proof for homogeneous extremizers. No literature result or numerical computation is required beyond those accepted foundations.

Status at creation: OPEN pending independent cross-read by the lead.
