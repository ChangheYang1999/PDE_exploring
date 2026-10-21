# Source-side discontinuity at the critical Holder exponent

Date: 2026-10-20. Status: complete informal argument awaiting independent review. This concerns compatible axis functions, not coupled profiles.

## Statement

Fix A>2, beta=2/A in(0,1), and L>0. Let w_0 be smooth on[0,L], odd and analytic near0, negative on(0,L), with w_0'(0)=-A, w_0'(L)=A and simple zeros at0andL. Let the normalized positive solution g_0 of

    w_0 g_0'=(w_0'-A)g_0,        g_0/x^2 ->1 at0

extend smoothly and positively toL. Write g_*=g_0(L), and suppose g_* != 2A-2. Define B[w] by the normalized third finite part, equivalently

    B[w]=(beta-1)A^(1-beta)/3 FP int_0^L (Q-Q(L))W dx,
    Q=(g'-w'')/(2g^3), m=-w/g, W=m^(beta-2)/g.           (1)

The finite part removes divergent powers with no added constant. Then B is discontinuous at w_0 in C^(2,1-beta)[0,L], even among smooth compatible functions equal to w_0 on neighborhoods of both endpoints. Specifically, there are v_N with

    ||v_N||_(C^(2,1-beta)) <= C/N,
    B[w_0+v_N]-B[w_0] -> K_* != 0,
    K_*=(1-beta)(3-beta)(2-beta-g_*/A)/(6A g_*^(beta+2)). (2)

The nonvanishing hypothesis is necessary for this leading mechanism. No statement at its exceptional value is proved here. The theorem addresses a critical topology on w, not a regularity obstruction for the density of a PDE solution.

## Construction and the Holder norm

Choose a fixed smooth cutoff chi on the real line with values in[0,1], zero on(-infinity,0] and one on[1,infinity). Fix 0<d_0<min(1,L)/2, put delta=L-x and t=log(d_0/delta), and define

    a_N(delta)=chi(t)chi(N+2-t),
    v_N(x)=delta^(3-beta) a_N(delta)/N.

Extend v_N by zero off this support. It is smooth, supported away from both endpoints, and all endpoint germs are unchanged. Put eps=1/N. Uniform bounds on cutoff derivatives give

    |d_delta^i v_N|<=C_i eps delta^(3-beta-i), i=0,1,2,3. (3)

The support is delta in[d_0 exp(-(N+2)),d_0]. The estimates imply w_N=w_0+v_N<0 for largeN.

Write alpha=1-beta. The amplitude bound on v_N'' is C eps delta^alpha and its derivative is bounded by C eps delta^(alpha-1). These imply a Holder seminorm at most C eps, uniformly inN. Indeed, for 0<=d<e, if e-d>=d/2, both amplitudes are bounded by a fixed multiple of eps(e-d)^alpha. Otherwise use the derivative estimate and the mean value theorem to get C eps d^(alpha-1)(e-d)<=C eps(e-d)^alpha. This covers the zero extensions too, since the functions are smooth and the bounds hold on the whole positive delta interval. Lower derivative and supremum bounds follow directly from(3). Thus the norm in(2) tends to zero.

## Normalized density and source scaling

The exact first axis equation gives, for sigma=v_N/w_0,

    eta=log(g_N/g_0)=log(1+sigma)-A int_0^x(1/w_N-1/w_0)du. (4)

Before the support this is zero. NearL, w_0=-A delta+O(delta^2), so |sigma|<=C eps delta^(2-beta), and the integral in(4) has a finite endpoint limit of size O(eps). Let eta_*=eta(L), lambda=exp(eta_*), and zeta=eta-eta_*. On the source segment,

    |eta_*|<=C eps,
    |zeta|<=C eps delta^(2-beta),
    eta'= -v_N'/(A delta)+O(eps delta^(2-beta))
                               +O(eps^2 delta^(3-2beta)). (5)

Primes here and below are x derivatives. The zeta estimate follows by subtracting(4) atL and integrating the bound C eps delta^(1-beta) on the reciprocal difference. For the derivative, the exact identity is

    eta'=v_N'/w_N+(A-w_0')v_N/(w_0 w_N).

Use A-w_0'=O(delta), w_N=-A delta[1+O(delta)+O(eps delta^(2-beta))], and(3) to prove(5). NearL below the support, zeta=0 exactly. Consequently g_N=lambda g_0 there and is smooth and positive atL. All perturbed traces are compatible with the stated domain ofB.

## Convergent difference of the finite parts

Formula(1), including its endpoint conventions, is proved in ../critical-norm/PROOF.md. Its use here requires no differentiation of a limiting rough trace. Each w_N is smooth and has the same analytic germ at0. The lower finite-part terms therefore agree before subtracting Q(L).

Define source-scaled comparison quantities on the fixed source segment:

    G=g_0'/(2g_0^3), V=-w_0''/(2g_0^3),
    Qbar=lambda^(-2)G+lambda^(-3)V,
    Wbar=lambda^(1-beta)W_0.

These are algebraic comparison quantities, not globally normalized axis data. They obey Q_N(L)=Qbar(L). Since Qbar and Q_0 are smooth and lambda=1+O(eps),

    (Qbar-Qbar(L))Wbar-(Q_0-Q_0(L))W_0
                                  =O(eps delta^(beta-1)).        (6)

To expand the remaining difference use the exact identity

    Q_N=lambda^(-2)e^(-2zeta)G+lambda^(-3)e^(-3zeta)V
          +lambda^(-2)e^(-2zeta)eta'/(2g_0^2)
          -lambda^(-3)e^(-3zeta)v_N''/(2g_0^3).

Furthermore

    W_N/Wbar=(1+sigma)^(beta-2)e^(-(beta-1)zeta),
    W_0=A^(beta-2)g_*^(1-beta)delta^(beta-2)(1+O(delta)).

Combining these identities with(3)-(5), and replacing lambda by1 in the leading terms, gives

    (Q_N-Q_N(L))W_N-(Q_0-Q_0(L))W_0
       =-[A^(beta-2)/(2g_*^(beta+2))]
            [v_N''+(g_*/A)v_N'/delta]delta^(beta-2)+E_N,
    |E_N| <= C eps[1+delta^(beta-1)]
                  +C eps^2 delta^(-1) 1_(support of v_N).        (7)

Here are the error terms explicitly. The difference e^(-izeta)-1 in the smooth G,V terms costs O(eps delta^(2-beta)), which becomes O(eps) after multiplication by W_0. The remainder in eta' in(5) has the same integrable bound. Replacing g_0 by g_* or the leading expression for W_0 costs a relative O(delta), also yielding O(eps). The relative weight change is O(eps delta^(2-beta)); its product with the leading Q correction is O(eps^2 delta^(1-beta)), which is integrable. Its product with Qbar-Qbar(L)=O(delta) is O(eps delta). Replacing lambda by1 costs O(eps^2 delta^(-1)) after weighting and is supported where the leading v_N' and v_N'' occur. Equation(6) supplies the remaining O(eps delta^(beta-1)) term. Constants depend only on the fixed base, cutoff and d_0.

The integral of the last term of(7) is at most C eps^2(N+2)=O(eps), and all other terms have integral O(eps). Outside the source segment, w_N=w_0 and g_N=g_0. There the only difference in(1) is the changed Q(L), of size O(eps), times W_0. Near0, W_0=O(x^(-beta)), which is integrable because beta<1. Thus this part also contributes O(eps). In particular the difference of the normalized finite parts is the ordinary integral of the displayed difference.

Multiplying(7) by the constant in(1), and using v_N'=-d_delta v_N, proves

    B[w_N]-B[w_0]
      =(1-beta)/(6A g_*^(beta+2))
         int_0^d_0 [d_delta^2 v_N-(g_*/A)d_delta v_N/delta]
                          delta^(beta-2)d_delta +O(1/N).        (8)

All boundary terms vanish: v_N and d_delta v_N vanish near delta=0 and are flat at delta=d_0. Two integrations in the first term and one in the second yield

    integral in(8)
       =(3-beta)(2-beta-g_*/A)
                          int_0^d_0 v_N delta^(beta-4)d_delta.

Finally the last integral is

    N^(-1)int_0^(N+2) chi(t)chi(N+2-t)dt
       =1+(2/N)int_0^1 chi(t)dt ->1.

This proves(2). The sign may be either sign, depending on the fixed source slope of the density through g_*; it is not universal.

## Dependencies and scope

Dependencies are the exact axis ODE, the finite-part integration identity with justified endpoints, elementary smooth cutoffs, the displayed uniform estimates and ordinary integration by parts. The proof is written before numerical tests; symbolic checks only verify algebraic constants and do not replace the uniform estimates.

Each trace is smooth and shares the same w germs at both endpoints, while its normalized g may be multiplied by a constant on the final source segment. No coupled two-dimensional realization is claimed. The theorem neither removes the source hypotheses of the smooth-profile necessary conditions nor decides whether a family of profiles exists. It does not duplicate a global a posteriori inverse or residual certificate.
