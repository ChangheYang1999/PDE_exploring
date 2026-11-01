# Conditional coefficient diagnostics through order380

Status: finite tables and full-array fits CONFIRMED inV456/V458. The density root label is corrected inV457. All conclusions concern the continuation initialized from the order329 midpoints.

## Statement and definitions

For the canonical logarithmic recursion at delta=2/3 and f_1=sin(theta), let f_(n,q,j) and g_(n,q,j) be the stored density and stream sine coefficients of(log r)^q. Define M_n=sum_(q,j)|f_(n,q,j)| and N_n=sum_(q,j)|g_(n,q,j)|. The requested finite quantities are these sums, their logarithms and roots, the ratio N_n/M_n, adjacent and three-order logarithmic decrements, and the least-squares slopes on27 successive orders. All are evaluated by directed arithmetic from the retained checkpoint.

For the last three orders, check the logarithmic Poisson equation in every coefficient. With P_n=2-2n/3 and stream frequency2j, it is

    (4j^2-P_n^2)g_(n,q,j)-2P_n(q+1)g_(n,q+1,j)
       -(q+1)(q+2)g_(n,q+2,j)
    =[(P_n-2j)f_(n,q,j-1)+(q+1)f_(n,q+1,j-1)
       +(P_n+2j)f_(n,q,j)+(q+1)f_(n,q+1,j)]/2.

Missing indices have value zero. This follows by applying the radial operator P_n+partial_t twice in the angular Poisson equation, where t=log r. The canonical convention sets the resonant constant stream coefficient to zero. Residual containment checks consistency of the saved intervals with these equations; it is not an independent proof that they enclose the original exact canonical sequence.

## Shifted-vector fits

Treat each full coefficient array as a finite vector extended by zero, and let S shift its angular coefficient index upward by one. For x=x_n and y=Sx_(n-3), define a_n=<x,y>/||y||_2^2 and e_n=||x-a_n y||_2/||x||_2. Then S is an isometry and

    ||x_n||_2/||x_(n-3)||_2=|a_n|/sqrt(1-e_n^2).

This is the Pythagorean projection identity proved in215. Directed fits of log10|a_n| against log10 n,1/n and n record finite trends on each specified window. The formulas are the usual centered least-squares slope sum(x-xbar)(y-ybar)/sum(x-xbar)^2 and intercept ybar-slope*xbar. No inference of an infinite-order law is made.

## Source uncertainty and reporting scope

The source run discarded the inherited interval radii at329. Its later intervals bound arithmetic for that selected input only. Every finite interval in this topic has that same condition. Even agreement with a perturbed input sample supplies no bound for the discarded full input box. All-order geometric or factorial growth, convergence of the canonical logarithmic series, and a physical convergence radius remain open. Numerical results will be compared against the earlier independently retained intervals and the printed tables before admission.
