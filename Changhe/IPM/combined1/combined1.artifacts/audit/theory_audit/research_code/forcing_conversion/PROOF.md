# Quantitative forcing conversion under an E3 derivative-ratio bound

## Exact spaces and statement

All functions are real S1 on R2, even in x and odd in y. All norms are
whole-plane Lebesgue norms, and D^j contains all ordered Cartesian
partials with the Frobenius norm. Put J=(1-Delta)^(1/2) and
omega=(1+4|X|^2)^(2/5). Complete smooth compact S1 functions in

    E(f)^2=||omega D2 f||2^2+2^14||Df||2^2+2^18||f||2^2
             +2^18(20/21)||f||Hdot^-1^2,
    E3(f)^2=||omega D3 f||2^2+2^173 E(f)^2.

Set Q(f)=||omega D3 f||2, N_u(f)=E(J^u f), and

    X_u(f)^2=||omega D2 J^u f||2^2+2^15||D J^u f||2^2
                +2^20||J^u f||2^2.

Fix s=1/262144, t=1/5184, eta_A=1/1572864 and eta_w=4207/20000000.
For any f in E3 and any K>=0 with Q(f)<=K E(f),

    X_t(f)<=kappa(K)N_s(f),
    kappa(K)=2[(2K^2+16410)^(t/2)+34t]/(1-34s).       (1)

The finite outward checks below imply

    Q(f)<=10^6 E(f), N_s(f)<=163.88 eta_A
                   => X_t(f)<eta_w,                  (2)

unless f=0, for which the non-strict conclusion is immediate. They also
imply that N_s(f)<=eta_A suffices for X_t(f)<eta_w whenever
Q(f)<=10^11500 E(f). These are comparisons of forcing tests under the
stated derivative-ratio assumption. Background hypotheses and nonlinear
ball conditions of the two existence theorems are separate.

There is no reverse norm comparison N_s<=C X_t even on band-limited
Schwartz S1 functions satisfying Q<=10^6 E. The selected completed
spaces remain incomparable without the derivative-ratio restriction.

## Proof of the conversion

At a common u, inspection of the exact component weights gives
X_u<=2N_u, first on the smooth core and then on its compatible
completions. The two imported A2 theorems, with their precise ranges,
are

    N_u(f)<=E(f)^(1-u)(2Q(f)^2+16410E(f)^2)^(u/2)
                                  +34uE(f), 0<u<=1/2,
    N_s(f)>=(1-34s)E(f), 0<s<1/34.

They are stated in the frozen A2_S1_CLOSURE.md section2; membership in
E3 implies the required N_u membership. If E(f)=0 then f=0. Otherwise
insert Q<=KE in the first bound with u=t, apply X_t<=2N_t, and use the
second bound to obtain(1). The function kappa is increasing for K>=0.

With K=10^6, outward arithmetic checks

    eta_w/(kappa(10^6) eta_A)>4097/25=163.88.

This proves(2). The other claimed comparison is the strict test
kappa(10^11500)eta_A<eta_w. The exact rational constants and all
containing intervals are stored in verification/result.json. No
inference is based on decimal approximations printed in prose.

## Why the reverse comparison still fails

Choose nonzero real radial eta in C_c^infinity({1<|xi|<2}) and put
psi(xi)=i xi2 eta(xi). For 0<r<1/4 set

    ghat_r(xi)=r^-1 psi(xi/r).

This is purely imaginary, even in xi1 and odd in xi2, with Hermitian
symmetry, so g_r is real and S1. It is Schwartz and band-limited. Direct
change of variables gives ||g_r||2 constant and positive, while
||g_r||Hdot^-1 is a positive constant times r^-1. Hence E(g_r) grows
at least as a positive multiple of r^-1.

Use omega(X)<=C(1+|X|^2)^(1/2) and Plancherel. A derivative of order j
has unweighted norm O(r^j); one xi derivative of its Fourier transform
has norm O(r^(j-1)). Consequently Q(g_r)=O(r^2) and the weighted
Hessian is O(r). Multipliers J^u and their first xi derivatives are
uniformly bounded on the shrinking Fourier supports, so the same
estimates hold after applying J^s or J^t. In particular X_t(g_r) is
bounded above and below by positive constants, and N_s(g_r) tends to
infinity. Every g_r belongs to E3. For small r, Q(g_r)/E(g_r)=O(r^3)
is below10^6. Thus no reverse constant exists even in this class.
The Schwartz functions represent members of the compact-core
completions by symmetric physical cutoffs; their oddness removes the
zero Fourier value needed in the negative norm near xi=0.

## Dependencies and scope

The only substantive imported estimates are the two displayed A2
residual-conversion theorems. The component comparison and scaled
Fourier argument are proved above. This independently checks T2's
the review of T4-259 remarkR2. It supplies a conditional norm comparison, not
a new inverse, candidate certificate or existence proof. In particular
it does not justify calling the two selected forcing spaces nested,
and the threshold quotient330.85 alone is not a same-norm improvement.
