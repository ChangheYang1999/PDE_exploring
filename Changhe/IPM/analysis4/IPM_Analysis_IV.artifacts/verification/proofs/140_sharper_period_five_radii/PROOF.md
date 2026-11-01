# Sharper rational certificates for the six period-five exterior radii

Status: PROVED. The independent Cartesian certificates and the theory part's separate Fourier and rational computations agree. The independent review dated 2026-10-31T11:06Z is recorded in V284. All conclusions retain the exact hypotheses and scope stated below.

## Statement and hypotheses

Let b_i, i=1,...,6, be the six real roots of the order10 obstruction polynomial in133. At delta=2/5 and c=5/3 use the unique compatible pure density and stream series with leading term epsilon(sin(theta)+b_i sin(3theta)), epsilon real and nonzero. Suppose a_i and s_i are the exact positive rational norm and response bounds in the certificate: 1+|b_i|<=a_i and |sigma_k(b_i)|>=s_i for every k>=2. Let Phi_i(z,Y) be the six polynomial right sides in131 at Q=5, B=4, L=5/2, kappa=156/5, a=a_i and s=s_i. The variables are Y=(W,V1,V2,V3,V4,E).

If positive rational z_i and a componentwise positive rational vector Y_i satisfy

    Phi_i(z_i,Y_i)<=Y_i,

then the density, stream and common potential series, together with every appropriately weighted Cartesian derivative, converge absolutely and uniformly on every r>=R with

    R>z_i^(-5/2)|epsilon|^(5/2).

The potential has logarithmic corrections only at orders5and10. This is an exterior stationary solution theorem, with no global stationary extension claim. Convenient integer radii R_i may replace z_i^(-5/2) whenever the exact inequality R_i^2 z_i^5>1 holds.

## Complete proof of the certificate

The map Phi has the form c+JY+Psi(z,Y), where c and J are nonnegative, J is strictly lower triangular, and every coefficient of Psi is nonnegative and has a positive power of z. Thus T=(I-J)^(-1)=I+J+...+J^5 is nonnegative. Multiplying the supersolution inequality by T gives

    Y_i>=Tc+T Psi(z_i,Y_i)=G(z_i,Y_i).

Iteration of G from zero is coefficientwise nondecreasing as a formal series. Its coefficients stabilize degree by degree because every nonconstant iteration term contains z. At z=z_i the iterates remain bounded by Y_i. Monotone convergence therefore bounds the unique formal majorant at z_i and gives geometric coefficient bounds with base z_i^(-1). This is the majorant sequence which dominates the actual tuned coefficients by131. The uniform response hypotheses come from139, not from finite sampling.

On every strict subdisk in z, each fixed derivative only multiplies coefficients by a polynomial in the order, which is summable against the strict geometric margin. A small complex angular strip costs exp(Bn tau) and is absorbed by the same margin. Since z=r^(-2/5), the strict exterior radius follows. The potential reconstruction132 preserves this geometric base; its two finite logarithmic terms are smooth on the exterior. Absolute convergence justifies all products and derivatives in the original potential equation. Homogeneity scales each order-n coefficient by epsilon^n and gives the displayed amplitude factor.

Numerical iteration may propose z_i and Y_i. It does not prove a singularity location or an optimal radius. The final exact rational vector, all components of Phi_i, all positive margins, and the integer radius inequality are the complete quantitative evidence. A failed proposal has no implication for convergence of the actual IPM series.


## Completed rational certificates

The radii below multiply |epsilon|^(5/2). Each printed scientific-notation number denotes the exact terminating decimal integer, rounded upward. Every row has six strictly positive rational margins Y_i-Phi_i(z_i,Y_i) and an exact check R_i^2 z_i^5>1. All rational inputs and outputs appear in verification/checks.json.

| Root | Uniform response lower bound | Sufficient exterior radius |
| --- | --- | --- |
| 1 | 401/1000 | 7.01e37 |
| 2 | 217/100000000 | 5.33e48 |
| 3 | 79/500000 | 3.41e44 |
| 4 | 417/1000000 | 9.19e43 |
| 5 | 23/20000 | 2.48e43 |
| 6 | 171/25000 | 3.68e42 |

The computation took 274.6520210863091 seconds. The certificate does not establish an optimal radius or a singularity location.
