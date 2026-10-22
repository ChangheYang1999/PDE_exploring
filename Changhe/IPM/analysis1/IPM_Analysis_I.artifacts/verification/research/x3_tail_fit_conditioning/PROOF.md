# Topic151. Analytic far coefficients and source-fit diagnostics

2026-10-21. Written before new evaluation. This result supplies exact coefficient identities and a reproducible floating diagnostic. No finite-R tail remainder or interval residual enclosure is asserted.

## Hypotheses and statement

Use the exact X3 formula, k,L,p,a,z,w, and Cjl of topic150 PROOF. Each b_m is evaluated on its final polynomial span. Write j_m=max(m-1,0), P(theta)=cos(theta)^2 sin(theta), g(theta)=|cos(theta)|^(p-2)sin(theta)^2, and primes on b_m and T for derivatives of their scalar arguments. Define

H00=sum_m b_m(1)cos(2m theta)+T(1)g,
H10=-sum_m b_m'(1)cos(2m theta)-2T'(1)g,
H20=(1/2)sum_m b_m''(1)cos(2m theta)+2T''(1)g,
H01=(k-3)/2-r0^2 sum_m j_m b_m(1)cos(2m theta)-(p/2)T(1)g.

Then
C00=P exp(H00), C10=C00 H10, C20=C00(H20+H10^2/2), C01=C00 H01.

For the pair (j,l) and d=ja+2l, define q=k-1-d and
E_jl(theta)=(k-d)cos(theta)Cjl(theta)-sin(theta)Cjl'(theta).
The corresponding contribution to the source rho_x is L^2 u^q E_jl. Its n-th sine coefficient is L^2 u^q e_jl,n, where

e_jl,n=(4/pi)int_0^(pi/2) Cjl(theta)[(k-d+1)cos(theta)sin(2n theta)+2n sin(theta)cos(2n theta)]dtheta. (1)

For any fixed outer radius R, the asymptotic coefficients expressed in the fitting basis (r/R)^q are A_jl,n=L^2(R/L)^q e_jl,n. Finite-window least-squares coefficients in that basis need not equal these asymptotic coefficients.

## Proof

Substitute qcompact=1-z(1+w)^(-a/2) in the final polynomial spline, and use the bidisc expression in topic150. At w=0 the compact displacement is exactly -z. Taylor's formula for b_m gives the coefficient -b_m' for z and b_m''/2 for z^2. The Chebyshev polynomial has argument1-2z at w=0 and contributes -2T' and2T''. For the pure w term set z=0: log(1+w) contributes(k-3)/2, the chi factor contributes-j_m r0^2, and the singular radial factor contributes-p/2. Thus the four H coefficients above are exact. Exponentiating adds H10^2/2 only to the z^2 term. Multiplying by P proves the stated C formulas.

The Cartesian derivative identity proved in topic150 gives E_jl. Integrate it against sin(2n theta). Integration by parts of the term -sin(theta)Cjl'(theta)sin(2n theta) has zero boundary term because sin(2n theta) vanishes at both endpoints and Cjl is bounded C1. Its derivative on the other factor is cos(theta)sin(2n theta)+2n sin(theta)cos(2n theta). This proves (1) without angular differentiation in the quadrature. Finally u=(r/R)(R/L), giving the scaling of A.

For an exterior change represented by coefficients delta A at fixed R, the exact mode1 strain change is delta c=(1/2)sum delta A/(-q), by direct integration from topic150. This identifies the quantity worth comparing; a small floating least-squares residual does not bound delta c relative to the true source.

## Planned numerical evidence and its limits

Read the exact JSON inputs, evaluate the scalar splines by an independent de Boor implementation, and differentiate their control coefficients to obtain endpoint derivatives. Compute the displayed angular integrals with two Gauss rules. Evaluate source mode1 on the actual saved fit radii with direct angular quadrature, independently of the producer's DST and modal recurrence. Fit with a QR-based least-squares solve and report the singular values and condition numbers of the design matrix. Compare coefficients with the analytic asymptotic expressions and compare the fitted exterior strain moments. These computations use binary64 and are diagnostics. They provide neither rigorous quadrature error, rigorous conditioning bounds, finite-window extrapolation error, historical execution attestation, nor an explanation of every bitwise coincidence in the saved fields. The exact identities survive independently of those diagnostic outcomes.

Dependencies: topic150 analytic formulas (reconstructed above where used); exact data_exact/x3.json for the X3 coefficients. No assumption of stationarity or profile existence is used. The IPM endpoint remains OPEN.
