# Radial polynomial differentiation and exact angular integration

## Hypotheses and representation

Let chi be a finite potential of the family in ../baseline/PROOF.md, with exact rational c>1 and coefficients. Set t=r^2/(1+r^2), u=1-t, and p_j=(3+1/c-j(1-1/c))/2. A Cartesian derivative of order d has the representation

sum_{j,n} (1+r^2)^p_j r^(-d) P[j,n](t) T_n(theta),

where T_n is a cosine or sine and P[j,n] is a rational polynomial. At d=0 this is exactly the defining canonical expansion. A term t^K has r-power 2K-d and (1+r^2)-power p_j-K. Using the polar derivative formulas from the baseline proof, define

A_minus = t P' + (n-d)P/2 + t(p_j P-tP'),
A_plus  = t P' - (n+d)P/2 + t(p_j P-tP').

An x derivative contributes A_minus at harmonic n-1 and A_plus at n+1, of the same trigonometric type. A y derivative changes cosine to sine with signs (-,+), and sine to cosine with signs (+,-). Negative harmonics are folded by sine oddness and cosine evenness. These are exact polynomial identities for r>0; smooth continuation at the origin follows from the original potential.

## Residual and angular quotient

The linear residual c r partial_r rho-rho is obtained in the order-three representation by replacing each density polynomial P by

c[(2t P'-3P)+2t(p_j P-tP')]-P.

The nonlinear residual is the exact product of the velocity polynomials of order three and density gradient polynomials of order four, combined by trigonometric product identities. Since each individual smooth basis density or velocity vanishes to first order at the origin and each density gradient is bounded there, the linear sine polynomial has a factor t^2 and the nonlinear sine polynomial a factor t^4. These divisibilities are also checked coefficient by coefficient.

Write F for the density residual and R_f=F/y, using its smooth quotient at y=0. Since

sin((2m+1)theta)/sin(theta)=1+2 sum_{k=1}^m cos(2k theta),

one obtains the finite exact representation

R_f(r,theta)=sum_{h,n even} u^b_h Q[h,n](t) cos(n theta),

b_h=(h+1)(1-1/c)/2 > 0.

Both the linear branch h and nonlinear pairs i+j+1=h have this same exponent. Therefore the normalized archived objective is

J_abs = 1/(pi a_ref^2) integral_{s=-infinity}^{infinity} integral_0^(pi/2) R_f^2 dtheta ds,

where s=log r. This is a different quantity from any of the unweighted residual Sobolev norms. Fourier orthogonality gives angular weights 1/2 for the squared cosine-zero coefficient and 1/4 for each positive cosine coefficient after division by pi. Since ds=dt/[2t(1-t)], polynomial integration reduces to Beta integrals.

## Finite-part Beta integration

After the angular products are grouped, each radial integrand is a sum of q_n t^n u^b/[2t(1-t)] with rational q_n and rational b>0. For n>=1,

integral_0^1 t^(n-1)(1-t)^(b-1)dt = B(n,b) = (n-1)!/[b(b+1)...(b+n-1)].

This is rational. For n=0 individual terms diverge, but the exact center identity makes the sum of their coefficients zero. Use the common analytic regularization t^(epsilon-1). The expansion B(epsilon,b)=1/epsilon-gamma_E-digamma(b)+O(epsilon) shows that the total is the finite sum -sum q_0 digamma(b), since the pole and Euler constant cancel. This regularization equals the ordinary convergent integral: subtract one common cutoff term for all n=0 components, leaving a numerator that vanishes at t=0 and hence an integrable expression. The n>=1 terms are already integrable. All endpoints at t=1 are integrable because b>0.

Thus rational polynomial algebra and validated digamma evaluations can enclose the full objective with no radial or angular quadrature. Ball evaluation of a field at a point provides only a point enclosure, separately from this integral argument.

## Angular resolution criterion

If the potential contains cosine harmonics through 2M, then rho contains sine harmonics through 2M+1 and the stream function through 2M+2. The polar Jacobian form of the nonlinear residual gives residual sine harmonics through 4M+3, so R_f has cosine harmonics through 4M+2 and its square through 8M+4. The composite trapezoid rule on [0,pi/2] with N equal subintervals is exact for these cosine integrals if N>2M+1. Indeed each nonconstant cos(2k theta) term has discrete trapezoid sum zero unless k is a multiple of 2N, and here k<=4M+2<2N. This condition is sufficient and concerns exact arithmetic only. Expanded bases require a new angular bandwidth check.

## Scope

This result concerns the archived J_abs and pointwise fields. Its exact integration does not make J_abs a closure norm. It provides an independent route to expose quadrature aliasing or coefficient conditioning. No assertion of existence or infinite-dimensional invertibility follows.
