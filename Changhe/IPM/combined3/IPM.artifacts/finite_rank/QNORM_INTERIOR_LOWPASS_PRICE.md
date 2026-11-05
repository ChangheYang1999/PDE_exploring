# An explicit interior Gaussian low-frequency price in the Q norm

Status: proved operator estimate. It does not prove the surrounding near/far or low/high decomposition for a background commutator.

Let q=21/10, W²=1+4r² and \(P_\mu=\exp(\Delta/(2\mu²))\), whose Fourier symbol is exp(-|xi|²/(2mu²)). Let chi be any real multiplication cutoff with |chi|<=1 supported in r<=R. Then
\[
\boxed{\|\chi P_\mu WJ^q g\|₂\le C_{\rm low}(R,\mu)\|g\|₂.}
\]
The proof explicitly respects the placement WJq; it does not commute W past Jq or replace inhomogeneous Jq by |D|q.

By adjointness it suffices to bound Jq W Pmu chi on L2. Put h=Pmu chi v and, for m2,3,
\[
A_m=\sup_\xi\langle\xi\rangle^mP_\mu(\xi),\quad
D_m=\sup_\xi|\nabla_\xi(\langle\xi\rangle^mP_\mu(\xi))|,
\]
\[
L_m=(1+2R)A_m+2D_m,\qquad B_j=\sup_\xi|\xi|^jP_\mu(\xi).
\]
The exact commutator [xj,m(D)] gives
\[
\|WJ^m h\|₂\le L_m\|v\|₂.
\]
No derivatives of chi enter: ||x chi v||₂<=R||v||₂.

The explicit weight derivatives obey |grad W|<=2, |D²W|F<=6, |DeltaW|<=8 and |grad DeltaW|<=32. For the last bound,
\(\partial_r\Delta W=-64r(1+r²)/(1+4r²)^{5/2}\), whose absolute value is below32 using r/W<=1/2 and (1+r²)/W4<=1.

Write J²(Wh)=WJ²h+E2, E2=−2gradW·gradh−(DeltaW)h. Then
\[
\|J²(Wh)\|₂\le A_2^*\|v\|₂,\qquad A_2^*=L_2+4B_1+8B_0.
\]
Differentiating E2 and applying the preceding weight bounds gives
\[
\|E_2\|_{H¹}\le(24B_1+4B_2+40B_0)\|v\|₂.
\]
For any Schwartz w, integration by parts and the q1 version of the exact quadratic-weight Fourier identity give
\[
\|Ww\|_{H¹}²\le\|WJw\|₂²+8\|w\|₂².
\]
Indeed the left side equals int W²(w²+|gradw|²)−int WDeltaW w², and WDeltaW>=0. The remaining first integral is the vector integer norm Ttilde1, which is at most ||WJw||²+8||w||² by Fourier differentiation. Applying this with w=J²h yields
\[
\|J³(Wh)\|₂\le A_3^*\|v\|₂,
\quad A_3^*=L_3+\sqrt8 A_2+24B_1+4B_2+40B_0.
\]
Spectral interpolation and adjointness prove
\[
\boxed{C_{\rm low}=(A_2^*)^{9/10}(A_3^*)^{1/10}.}
\]

## Concrete bounds at mu=.1

Since log(1+t)<=t, A_m<=1 whenever mu^-2>=m. For m2,3,
\[
D_m\le\frac{\mu^{-2}}{\sqrt{e(\mu^{-2}-m)}},\quad
B_0=1,\quad B_j=(j\mu²/e)^{j/2}.
\]
All quantities are enclosed by Arb in `Qnorm_interior_lowpass_price.py` and its JSON output. At R10000, C_low² is below4.02e8; at R30000 it is below3.61e9. These are low-order quadratic prices multiplying ||g||₂². They fit inside the scale of the inherited weak budgets, provided the rest of the proof allocates them correctly.

The same Gaussian satisfies ||Pmu G||₂<=||J^-1G||₂ for mu<=1, since sup<xi>Pmu<=1. Thus a low-frequency norm charge can be paid directly from a Bessel low-order damping term. The low/high cross terms of an actual commutator still require their own proof.
