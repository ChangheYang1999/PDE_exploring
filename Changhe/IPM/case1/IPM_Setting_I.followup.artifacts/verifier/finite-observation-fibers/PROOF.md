# Exact axis-obstruction values with fixed finite observations

Date: 2026-10-20. Status: complete informal argument, independent review pending. This is a result about scalar compatible axis data, not about coupled IPM profiles.

## Statement

Fix A>2, beta=2/A, L>0, and a smooth compatible pair(w_0,g_0) on[0,L] satisfying

    w_0(0)=w_0(L)=0, w_0'(0)=-A, w_0'(L)=A,
    w_0<0 on(0,L), g_0>0 on(0,L],
    w_0 g_0'=(w_0'-A)g_0, g_0(x)/x^2 ->1 as x->0.

Assume w_0 is odd analytic near0. Rebuild g_w from w by the same normalization. Set

    Q_w=(g_w'-w'')/(2g_w^3), m_w=-w/g_w,
    B[w]=(beta-1)A^(1-beta)/3
              * FP integral_0^L (Q_w-Q_w(L)) m_w^(beta-2)/g_w dx.

The finite part is in the physical coordinate x, subtracting only the divergent noninteger powers at0. Define

    ||u||_crit=sum_(i=0)^2 sup_(0<x<=L) x^(i-7-beta)|u^(i)(x)|.

For every0<delta<L, every epsilon>0 and every real target b, there exists a smooth compatible w such that

1. ||w-w_0||_crit<epsilon and B[w]=b exactly;
2. (w,g_w) agrees with(w_0,g_0) on[delta,L];
3. (w,g_w) agrees with(w_0,g_0) on some neighborhood of0.

Consequently, fixing all local jets at an arbitrary finite set of axis points does not impose any bound on B in any positive-radius critical-norm neighborhood of this base. The center and source germs can be fixed as well. This conclusion makes no assertion about which such traces arise from the two-dimensional canonical inverse.

## Construction with a compact amplitude interval

Let chi be a fixed smooth cutoff with0<=chi<=1, chi=0 on(-infinity,0], and chi=1 on[1,infinity). Choose0<r_0<min(1,delta)/8, and choose a fixed nonnegative nonzero smooth f with compact support in(b_0,c_0), where

    2r_0<b_0<c_0<delta.

For a real amplitude a and integer N>=3 define

    p_(N,a)(x)=(a/N)x^(7+beta)
           chi(log(r_0/x))chi(N+2-log(r_0/x)),   0<x<r_0,

and extend it by zero. Put

    I_N(a)=integral_0^L[1/(w_0+p_(N,a))-1/w_0]dx,
    J(t)=integral_0^L[1/(w_0+t f)-1/w_0]dx.

Fix any finite M>0 and restrict a to[-M,M]. The complete origin-layer argument in ../origin-fixed-source/PROOF.md yields the following estimates uniformly on this compact amplitude interval for all sufficiently large N:

    ||p_(N,a)||_crit<=C_M/N, |I_N(a)|<=C_M/N.                  (1)

Uniformity does not require a new limiting theorem. Each derivative estimate for p has the explicit factor|a|/N. The normalized equation has denominators w_0+p comparable to w_0 once C M/N is small. All errors in that proof contain bounded powers of|a|/N and constants determined only by the fixed base and cutoffs. Replacing|a| by M in those estimates gives a common constant and a common lower threshold for N.

On the fixed support of f, the scalar map J is smooth, J(0)=0 and

    J'(0)=-integral f/w_0^2 dx<0.

There is therefore one fixed inverse neighborhood of0 for J. By(1), -I_N(a) lies in this neighborhood for every|a|<=M once N is large. Define

    t_N(a)=J^(-1)(-I_N(a)),
    w_(N,a)=w_0+p_(N,a)+t_N(a)f.                             (2)

The map a->t_N(a) is smooth for this fixed N, with |t_N(a)|<=C_M/N uniformly. The two supports are disjoint, so their reciprocal differences add exactly and

    integral_0^L [1/w_(N,a)-1/w_0]dx=0.                       (3)

For large N the perturbed w remains negative in(0,L), uniformly for|a|<=M. The normalized first equation gives

    log(g_(N,a)(x)/g_0(x))
      =log(w_(N,a)(x)/w_0(x))
          -A integral_0^x[1/w_(N,a)-1/w_0]dt.                (4)

For x>=c_0 the perturbation is zero and the accumulated integral has reached its final value0, so(w_(N,a),g_(N,a)) equals the base pair there. For x<r_0 exp(-(N+2)) both perturbations and the accumulated integral are zero, so the pair equals the base near0 too. Positivity of the rebuilt density follows from(4). Smoothness and all endpoint compatibility conditions follow from exact agreement with the base near both endpoints. Also

    sup_(|a|<=M)||w_(N,a)-w_0||_crit<=C_M/N.                  (5)

## Uniform obstruction expansion

The origin estimate and the interior-correction estimate in ../origin-fixed-source/PROOF.md, now with the uniform constants just justified, give

    sup_(|a|<=M)|B[w_(N,a)]-B[w_0]-a kappa_A|<=C_M/N,
    kappa_A=(1-beta)(6+beta)(7+beta)/(6A)>0.                  (6)

Here is the mechanism, to specify the dependency fully. If the interior correction is temporarily omitted, subtraction of the two finite-part integrands leaves the leading term

    -(A^(beta-2)/2)p_(N,a)'' x^(-6-beta).

The remaining terms are bounded on(0,r_0] by C_M N^(-1)(x+x^(-beta)), and away from0 by an integrable envelope of size C_M/N, including the source endpoint after subtracting Q(L). Two integrations by parts, with zero boundary terms, turn the leading contribution to B into

    kappa_A integral_0^L p_(N,a)x^(-8-beta)dx
       =a kappa_A[1+(2/N)integral_0^1 chi(t)dt].

The interior correction has C^2 size C_M/N on its fixed support. Before that support only the endpoint constant Q(L) changes in the subtracted integrand, against the integrable weight O(x^(-beta)). On its support all denominators stay away from zero. After it, write the uncorrected density as lambda g_0 with lambda=1+O_M(1/N); the exact factors in Q are lambda^(-2) and lambda^(-3), and the weight factor is lambda^(1-beta). Subtracting their endpoint values first leaves the integrable envelope C_M N^(-1)(L-x)^(beta-1). Thus the correction changes B by at most C_M/N uniformly. These are exactly the estimates establishing(6).

For each fixed large N, the map a->B[w_(N,a)] is continuous on[-M,M]. Indeed all these fields agree with the base on the same neighborhood of0 and on[c_0,L]. Differences of their finite parts are ordinary integrals over a fixed compact subinterval of(0,L), since their Q(L) and endpoint germs agree. There the integrand is a smooth function of a with nonvanishing denominators. Ordinary continuity under a compact integral proves the assertion. No uniform global continuity of B in the critical norm is being assumed.

## Exact target by the intermediate value theorem

Write D=b-B[w_0], and choose

    a_-=(D-1)/kappa_A, a_+=(D+1)/kappa_A,
    M>max(|a_-|,|a_+|).

Choose one N large enough for(1)-(6), for C_M/N<epsilon in(5), and for the error in(6) to be less than1/2. Then

    B[w_(N,a_-)]<b-1/2,
    B[w_(N,a_+)]>b+1/2.

Continuity and the intermediate value theorem provide a_N in(a_-,a_+) with B[w_(N,a_N)]=b exactly. Set w=w_(N,a_N). Equations(4)-(5) prove all remaining requirements. This argument uses a finite N chosen after the target and accuracy, not an assertion that the limiting critical-norm profile has a different B.

## Consequence for finite observations and its precise scope

Let S be any finite subset of[0,L]. If S contains a positive point, choose delta smaller than its smallest positive point. If not, choose any delta in(0,L). The construction agrees with the base on a neighborhood of every point of S, including0 when present. Thus all derivatives of both w and g at those points agree exactly, whatever finite orders an observation rule uses. Nevertheless B can be prescribed arbitrarily in every critical-norm ball of positive radius.

More formally, let D_obs(w,g) be any finite list of these local jet values and let Phi be any real-valued deterministic estimator based only on that list. On this class with D_obs fixed at its base value and ||w-w_0||_crit<epsilon, Phi is constant while B ranges over the whole real line. Therefore the absolute error |Phi-B| is unbounded on that set. This is an impossibility result for that specified information and admissible axis class. It does not cover methods that supply additional global analytic bounds, integrals, a stronger norm, or the two-dimensional canonical-coupling equation. It also does not show that any coupled solution family exists or that either strong-setting endpoint is attained.
