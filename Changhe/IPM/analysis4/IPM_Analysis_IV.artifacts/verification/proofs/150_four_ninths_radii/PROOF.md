# Explicit sufficient radii for the four-ninths profiles

Status: PROVED. Exact supersolutions V296 were independently reproduced by the theory part at11:52Z, and the remaining compact-formula dependency was reviewed in V306.

## Statement and hypotheses

Let b_i be one of the five real roots of the degree-nine obstruction polynomial certified in146, with delta=4/9, c=9/5 and f_1=sin(theta)+b_i sin(3theta). Suppose149 supplies an exact rational s_i>0 such that |sigma_k(b_i)|>=s_i for every k>=1. Let a_i be an exact rational upper bound for1+|b_i|.

Use the polynomial majorant Phi in145 with h=2, Q=9, B=4, L=9/2 and kappa=230/9. Order its ten unknowns as V_1,...,V_8,E,W. Write Phi(0,Y)=c0+JY, where J is strictly lower triangular and nonnegative. Put T=(I-J)^(-1), Y0=T c0 and

    G(z,Y)=Y0+T(Phi(z,Y)-c0-JY).

If an exact rational z0>0 satisfies G(z0,2Y0)<=2Y0 componentwise, then the nonnegative majorant converges at every |z|<z0. Hence, conditional on145, the tuned exterior solution and all weighted derivatives converge on every closed exterior r>=R with R>z0^(-9/4). For a leading amplitude epsilon, multiply this sufficient radius by |epsilon|^(9/4).

## Proof of the certificate implication

The affine inverse T is the finite sum I+J+...+J^9, so it has nonnegative rational entries. Every term of Phi-c0-JY has positive z degree and nonnegative coefficients. Thus G is monotone in nonnegative z,Y. Starting from Y0, iteration of G at z0 remains in the box [Y0,2Y0]. Its formal coefficients stabilize in increasing degree because the remainder has positive z degree. Monotone convergence gives a finite nonnegative coefficient sum at z0, bounded by2Y0. The resulting formal series is the unique triangular scalar majorant from145. Every coefficient is therefore bounded by a constant times z0^(-n). The physical variable is z=r^(-4/9), giving the stated strict exterior radius. A strict inequality leaves room for each polynomial derivative weight and for a positive angular strip width.

The root upper bound is checked directly on its exact isolating interval. The response lower bound is a separate all-index certificate, not a finite sample. The check of Phi is exact rational arithmetic. No assertion of an optimal radius is made.

## Dependencies and scope

Algebraic compatibility is146; response coverage is149; the analytic majorant and common potential are145. The present result only turns those hypotheses into numerical sufficient radii. A finite logarithmic potential correction at order9 is allowed, as in145; density and stream remain pure series.

## Exact sufficient radii

The calculation uses the following rational input and dyadic certificate table. Roots are listed in increasing order.

| Root | a | s | z0 | Sufficient strict radius |
|---|---:|---:|---:|---:|
| 1 | 133/125 | 2^-29 | 2^-215 | R>2^(1935/4) |
| 2 | 1153/1000 | 2^-24 | 2^-207 | R>2^(1863/4) |
| 3 | 127/100 | 2^-25 | 2^-212 | R>2^477 |
| 4 | 1423/1000 | 2^-14 | 2^-193 | R>2^(1737/4) |
| 5 | 2857/1000 | 1 | 2^-184 | R>2^414 |

Every inequality is strict componentwise for the box2Y0. The respective maximum component ratios are below0.825,0.874,0.793,0.818,0.842. The preceding dyadic choice2z0 fails for this same box. That failure makes no assertion about the optimal convergence radius. A common sufficient strict radius is2^484 for unit amplitude; multiply each radius by |epsilon|^(9/4) for amplitude epsilon.

The independent exact replay also verifies every response interval and every omitted integer-free interval from149. It completed at2026-10-31T11:31:50Z in0.664166150148958 actual seconds. verification/checks.json retains every rational affine matrix, constant vector, box, image and response certificate hash.
