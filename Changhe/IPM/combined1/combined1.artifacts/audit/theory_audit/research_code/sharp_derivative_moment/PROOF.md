# Sharp angular reduction of the first-moment derivative bound

Status: independent analytic verification of the T1/T3 theory worker R1-026 remark R2. The variational formula is CONFIRMED; numerical eigenvalues in the review remain FLOAT. The small missing lower-bound step for the value 1 is supplied below.

## Exact statement

For integer k>=0 and fixed R>0, let w_R(X)=sqrt(1+|X|^2/R^2), and let U[h]=(-R1R2h,R1^2h). All derivative norms use the full ordered k-tensor and sum both velocity components. Let B consist of real H1 functions b on the circle with b(theta+pi)=-b(theta). Define

    Lambda_k=sup_(b in B, b nonzero)
      int cos^2(theta)(|b'|^2+(k+2)|b|^2) dtheta
        / int (|b'|^2+k|b|^2) dtheta.

The best squared constant in both

    || |X| D^k U[h] ||2^2 <= C || |X| D^k h ||2^2,
    || w_R D^k U[h] ||2^2 <= C || w_R D^k h ||2^2

on real smooth compactly supported centrally odd h is C=Lambda_k. In particular 1<=Lambda_k<=1+2/(k+1). If the class is restricted to S1 (even in x and odd in y), the same statement holds with B restricted to the span closure of sin(n theta), n positive odd. The full centrally odd constant is the maximum of the sine and cosine constants. A numerical value for the full class is not automatically the sharp S1 value.

## Fourier reduction and upper bound

The audited T4-206 moment identity, with a=kappa^k hhat and kappa=|xi|, gives

    numerator=int [cos^2(theta)|partial_kappa a|^2
       +cos^2(theta)(|partial_theta a|^2+(k+2)|a|^2)/kappa^2] dxi,
    denominator=int [|partial_kappa a|^2
       +(|partial_theta a|^2+k|a|^2)/kappa^2] dxi.

Real and imaginary parts separate, so the real angular supremum bounds the angular term for complex a as well. The radial part is bounded with constant1. Thus C<=max(1,Lambda_k). Odd Poincare gives Lambda_k<=1+2/(k+1). The unweighted tensor norm satisfies ||D^k U[h]||2<=||D^k h||2, so the same max bound applies to w_R.

To see Lambda_k>=1, take a nonzero real smooth bump supported within distance epsilon of0 on the circle and subtract its pi translate. The result is anti-periodic, has support where cos^2(theta)>=1-epsilon^2, and therefore has Rayleigh quotient at least1-epsilon^2. Let epsilon decrease to0. An odd local bump gives the same construction in the S1 sine class. Hence max(1,Lambda_k)=Lambda_k. This establishes the upper bounds and the missing lower bound for1 in the original review.

## Sharpness through Fourier annuli

Smooth anti-periodic functions are dense in B in H1, and the denominator is positive on nonzero B by odd Poincare. Fix a smooth real nonzero b with Rayleigh quotient arbitrarily close to Lambda_k. Choose nonzero real g in C_c^infinity((-2,-1)) and set g_T(t)=g(t/T), T>0. Define

    hhat_T(kappa,theta)=i kappa^(-k) g_T(log kappa)b(theta).

It is smooth, supported in the annulus exp(-2T)<kappa<exp(-T), and satisfies hhat_T(-xi)=conjugate(hhat_T(xi)), so h_T is real, centrally odd and Schwartz. Put a_T=i g_T(log kappa)b. The radial moment energy equals

    int |g_T'|^2 dt int |b|^2 dtheta
       =T^(-1) int |g'|^2 int |b|^2,

while the angular moment energy is T int |g|^2 times its angular denominator. Thus their ratio tends to0 as T tends to infinity, and the pure-moment quotient tends to the angular Rayleigh quotient of b.

The unweighted D^k norm is int exp(2t)|g_T(t)|^2 dt int |b|^2, bounded by exp(-2T) T int |g|^2 int |b|^2. For fixed R the unweighted contribution is negligible compared with R^(-2) times the moment energy. Therefore the w_R quotient has the same limit. This proves sharpness on Schwartz functions.

For fixed T multiply h_T by an even radial cutoff eta(X/N). The result is smooth, compactly supported, centrally odd, and converges to h_T in both displayed input seminorms: the term with no cutoff derivative converges by dominated convergence, and every other Leibniz term tends to0 by Schwartz decay, even with the single |X| factor. The audited T4-206 bounds give convergence of the output tensors. Their quotients therefore converge too. This proves sharpness on the stated compact test class.

For S1 choose b in the odd sine class; the same Fourier construction has exactly the required reflection symmetries and the radial cutoff preserves them. Orthogonality of even and odd functions under the even weight cos^2(theta), and of their derivatives under the same weight, makes the full variational quotient split into cosine and sine blocks. Its supremum is their maximum.

## Scope

Dependencies: the audited T4-206 Fourier identity, elementary circle Fourier series and Plancherel. No numerical eigenvalue enclosure is needed for the statement. The review's finite-dimensional eigenvalues give diagnostics and lower-bound candidates only; they do not prove an upper bound for the infinite space. This result supplies no transport estimate, origin trace, commutator or inverse, and changes no closure-matrix row.
