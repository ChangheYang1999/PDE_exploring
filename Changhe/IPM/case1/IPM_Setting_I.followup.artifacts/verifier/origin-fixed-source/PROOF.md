# Origin discontinuity with the entire source germ fixed

Date: 2026-10-20. Status: complete informal proof, written before the associated checks. Independent review pending. This is a statement about compatible axis data only.

## Statement

Fix A>2, beta=2/A in (0,1), and L>0. Let w_0,g_0 be a smooth compatible pair on [0,L], with w_0 odd analytic near zero and

    w_0(0)=w_0(L)=0,   w_0'(0)=-A,   w_0'(L)=A,
    w_0<0 on (0,L),    g_0>0 on (0,L],
    w_0 g_0'=(w_0'-A)g_0,    g_0(x)/x^2 -> 1 at zero.

For each compatible w rebuild the density g from the same normalized first equation. Put

    Q=(g'-w'')/(2g^3),   m=-w/g,   W=m^(beta-2)/g,
    B[w]=(beta-1)A^(1-beta)/3
               * FP integral_0^L (Q-Q(L))W dx.                 (1)

The finite part in (1) removes divergent powers in the physical coordinate x at zero, with no added constant. Define the global weighted norm

    ||u||_crit=sum_(i=0)^2 sup_(0<x<=L)
                                  x^(i-7-beta)|u^(i)(x)|.      (2)

For every fixed real number a there are smooth compatible w_N=w_0+u_N, for all sufficiently large integers N, such that:

1. ||u_N||_crit tends to zero.
2. Each pair (w_N,g_N) agrees exactly with (w_0,g_0) on a neighborhood of zero, whose size may depend on N, and on one fixed neighborhood of L independent of N.
3. The obstruction has the limit

       B[w_N]-B[w_0] -> a kappa_A,
       kappa_A=(1-beta)(6+beta)(7+beta)/(6A)>0.                 (3)

In particular B is discontinuous even on the exact constraint g(L)=g_0(L), with all source derivatives and all center Taylor coefficients held fixed. This holds for every positive source value allowed by the base hypotheses, including g_0(L)=2A-2. It does not contradict the source-supported estimate in ../source-fixed-value/PROOF.md: the perturbations below have an origin component and an interior component.

## The normalized first equation and the finite part

For any sufficiently small perturbation u vanishing near both endpoints, direct integration of the first equation gives

    log(g_u(x)/g_0(x))
       =log(1+u(x)/w_0(x))
             -A integral_0^x [1/(w_0+u)-1/w_0] dt.            (4)

Near zero the analytic odd w_0 and the normalization imply g_0=x^2(1+O(x^2)) and m_0=(A/x)(1+O(x^2)). Consequently W_0=O(x^(-beta)), which is integrable. At L, g_0 has a positive smooth limit, m_0 is a positive constant times L-x, and Q_0-Q_0(L)=O(L-x). The upper endpoint of (1) is therefore integrable, with order (L-x)^(beta-1).

Formula (1) is the normalized third obstruction used in ../critical-norm/PROOF.md. To see the finite-part convention directly, define F=g^4 Q'/3 and H=A^beta g^3 m^(-beta). The first equation gives m'=-A/g and wH=-A^beta g^4 m^(1-beta), so -FP integral F/(wH)=(1/(3A^beta)) FP integral Q' m^(beta-1). Integration by parts with Q-Q(L) gives (1). The boundary product at L is O((L-x)^beta). At zero its powers are nonintegral: the Laurent powers of Q start at worst at x^(-5) in steps of two, and multiplication by m^(beta-1) introduces the noninteger shift 1-beta. The constant Q(L) also gives the noninteger power 1-beta. No finite-part boundary constant remains. Every constructed trace equals the base near zero, so these conventions continue to apply.

## The origin layer and its obstruction

Choose a fixed r_0 with 0<r_0<min(1,L)/4. Let chi be smooth on the real line, with 0<=chi<=1, chi=0 on (-infinity,0], and chi=1 on [1,infinity). Define

    t=log(r_0/x),
    p_N(x)=(a/N)x^(7+beta) chi(t)chi(N+2-t),    0<x<r_0,

and extend p_N by zero. It is flat at its support endpoints r_0 exp(-(N+2)) and r_0. Its derivatives satisfy, for i=0,1,2,

    |p_N^(i)(x)|<=C_a N^(-1)x^(7+beta-i).                    (5)

For fixed a and large N, the trace w_hat_N=w_0+p_N remains negative. Let g_hat_N be its normalized density. Formula (4), together with w_0=-A x+O(x^3), gives

    |d_x^i log(g_hat_N/g_0)|
                     <=C_a N^(-1)x^(6+beta-i),  i=0,1,2,     (6)

on (0,r_0]. On [r_0,L], w_hat_N=w_0 and g_hat_N=lambda_N g_0 with lambda_N=1+O_a(1/N). The density is positive and smooth up to L.

For completeness, the uniform calculation of the obstruction is as follows. With hats denoting the quantities of w_hat_N, equations (5) and (6) imply on (0,r_0]

    W_hat-W_0=O_a(N^(-1)x^6),
    Q_hat-Q_0=-p_N''/(2g_0^3)+O_a(N^(-1)x^(1+beta)),
    Q_hat(L)-Q_0(L)=O_a(1/N).

The difference of the integrands in (1) is consequently

    (Q_hat-Q_hat(L))W_hat-(Q_0-Q_0(L))W_0
       =-(A^(beta-2)/2)p_N'' x^(-6-beta)+E_N(x),
    |E_N(x)|<=C_a N^(-1)(x+x^(-beta)).                       (7)

Here the errors come from the lower term in Q_hat-Q_0, the product (Q_0-Q_0(L))(W_hat-W_0), the source constant subtraction, and the O(x^2) correction to g_0^(-3)W_0. Each is bounded by (7); products of perturbations are smaller for large N. On [r_0,L] the integrand difference is O_a(1/N) away from L and O_a(N^(-1)(L-x)^(beta-1)) near L. These bounds are integrable uniformly in N. Below the support of p_N only the source constant subtraction changes; its weight x^(-beta) is integrable. Thus the difference of finite parts is the ordinary integral of the difference. Equation (1) gives

    B[w_hat_N]-B[w_0]
       =(1-beta)/(6A) integral p_N'' x^(-6-beta) dx+O_a(1/N)
       =(1-beta)(6+beta)(7+beta)/(6A)
                            integral p_N x^(-8-beta) dx+O_a(1/N).

Both integrations by parts have zero boundary terms, since each p_N is flat and vanishes near zero. The last integral is exactly

    (a/N) integral_0^(N+2) chi(t)chi(N+2-t)dt
                   =a+(2a/N) integral_0^1 chi(t)dt.           (8)

This proves the limit (3) for the uncorrected origin layer, with an error uniform in N for each fixed a.

## An exact interior correction of the source germ

Choose one fixed nonnegative, nonzero smooth f supported in a compact subinterval (b,c) of (2r_0,L-r_0). Define

    I_N=integral_0^L [1/(w_0+p_N)-1/w_0]dx,
    J(t)=integral_0^L [1/(w_0+t f)-1/w_0]dx.

The supports avoid the endpoint singularities for every N. Estimate (5) gives |I_N|<=C_a/N, because the integrand on (0,r_0) is bounded by C_a N^(-1)x^(5+beta). On the fixed interior support, J is smooth near zero and

    J(0)=0,    J'(0)=-integral f/w_0^2 dx<0.                 (9)

By the scalar inverse function theorem there is a unique small t_N with

    J(t_N)=-I_N,    |t_N|<=C_a/N.                            (10)

Set u_N=p_N+t_N f. The supports are disjoint, so the reciprocal differences add exactly:

    integral_0^L [1/(w_0+u_N)-1/w_0]dx=I_N+J(t_N)=0.         (11)

For large N, w_N=w_0+u_N remains negative. Equation (4) and (11) imply g_N=g_0 on [c,L], since u_N=0 there and the accumulated integral has its final zero value. Also w_N=w_0 there. Near zero p_N and f vanish, so (4) gives g_N=g_0 and w_N=w_0. Thus the entire source germ and the entire center germ are fixed. The global norm (2) is O_a(1/N): (5) treats the origin layer, and the fixed support of f has a strictly positive distance from zero.

## Uniform effect of the interior correction on B

It remains to show that the correction does not remove the limit (8). This is not inferred from an unproved global continuity estimate for B. We compare its integrand directly between w_N and w_hat_N.

Before b, the normalized equation is causal: w_N=w_hat_N and g_N=g_hat_N exactly. Hence the only integrand difference in (1) there is

    [Q_hat_N(L)-Q_N(L)] W_hat_N.

The coefficient is O_a(1/N), since Q_N(L)=Q_0(L) and g_hat_N=lambda_N g_0 near L. Its weight is uniformly integrable on [0,b]: equation (6) gives W_hat_N<=C x^(-beta) near zero. This part contributes O_a(1/N) to B.

On the fixed interval [b,c], the functions w_0 and g_0 are bounded away from zero in modulus. The uncorrected quantities equal w_0 and lambda_N g_0 there. The correction t_N f has C^2 size O_a(1/N). Formula (4), or ordinary differentiation of it on this fixed interval, shows that the changes in g and g' are O_a(1/N). It follows directly from the definitions that the changes of Q,W and the source constant are O_a(1/N). This interval contributes O_a(1/N).

After c, the corrected pair equals the base pair. The uncorrected pair is (w_0,lambda_N g_0), with lambda_N=1+O_a(1/N). Writing G=g_0'/(2g_0^3) and V=-w_0''/(2g_0^3), one has exactly

    Q_hat_N=lambda_N^(-2)G+lambda_N^(-3)V,
    W_hat_N=lambda_N^(1-beta)W_0.

The same formulas hold at L. Subtracting the two endpoint values first shows that the difference of (Q-Q(L))W is O_a(N^(-1)(L-x)^(beta-1)) near L, and O_a(1/N) elsewhere on [c,L]. It is integrable uniformly in N.

Finally the corrected and uncorrected fields agree near zero, so their finite-part singular terms coincide. The above ordinary integral therefore gives

    |B[w_N]-B[w_hat_N]|<=C_a/N.                             (12)

Together with (8), this proves all the assertions.

## Dependencies and scope

The argument uses the normalized scalar axis ODE, the explicitly defined finite part, smooth cutoffs, ordinary integrations by parts and a scalar inverse function theorem on a fixed compact interval. Equations (7) and (8) repeat the origin estimate in ../critical-norm/PROOF.md so that the argument can be read without assuming an unproved stability property of B. The comparison (12) is specific to a fixed interior correction and has constants uniform over the stated origin family.

No assertion is made that any of these traces is induced by the canonical two-dimensional IPM inverse. The construction does not determine the number of free parameters of a PDE profile, provide a continuum kernel, place the numerical candidate in a certified neighborhood, or establish either strong-setting endpoint. Fixing endpoint germs does not by itself control this nonlocal axis functional in the critical norm.
