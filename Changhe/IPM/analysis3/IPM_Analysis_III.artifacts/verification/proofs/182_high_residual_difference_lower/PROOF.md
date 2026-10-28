# Difference lower bounds for the high residual norm

## Statement

Use the exact residual, scalar axis trace g_axis, unitary Fourier transform and fixed high target norm eta_* of topics177 and179. In particular eta_*>=||g_axis||H^(25/4)(R), and g_axis has five continuous derivatives. For distinct real numbers t and u,

 eta_* >= |g_axis^(5)(t)-g_axis^(5)(u)| /
       [sqrt(8sqrt(2)/(3pi)) |t-u|^(3/4)].              (1)

A directed lower bound for this expression is a certified lower bound for eta_*. Different such bounds may be maximized but are not added here. The original-data evaluation and its independent reconstruction will be recorded below before any numerical claim is accepted.

## Proof

For f in H^(25/4)(R), the inverse Fourier transform, Cauchy-Schwarz and |exp(iu)-1|^2<=min(u^2,4) give

 |f^(5)(t)-f^(5)(u)|^2
 <= ||f||H^(25/4)^2 /(2pi)
       integral_R |xi|^10 |exp(i(t-u)xi)-1|^2 (1+xi^2)^(-25/4) dxi.

For xi!=0, replace (1+xi^2)^(-25/4) by the larger |xi|^(-25/2). Put h=|t-u|>0, use symmetry and split the positive integral at2/h. Its upper bound, including1/(2pi), is

 (1/pi)[h^2 integral_0^(2/h) xi^(-1/2)dxi
                   +4 integral_(2/h)^infinity xi^(-5/2)dxi]
 =8sqrt(2) h^(3/2)/(3pi).

Both integrals converge. This also justifies passing from smooth functions to the continuous fifth derivative representative of every f in H^(25/4). Taking square roots and using the scalar axis summand of eta_* proves(1). Proof 177 proves membership of the actual residual, including the finitely many C5 spline joins. Thus a pair straddling a join is permitted; no sixth derivative trace is used.

## Numerical procedure and scope

The point evaluator in proof 179 is used first at exact rational points near t=8, with all original angular modes and canonical Green data. For the strongest pair, each fifth derivative must subsequently be recomputed from exact original Phi control derivatives, independently differentiated exponential-polynomial velocity and the binomial series for the weight, as in proof 179's alternative reconstruction. The constant in(1) and every power of the exact rational separation are enclosed by directed ball arithmetic. Source and code hashes, exact rational enclosure endpoints and precision are retained.

As in proof 179, a large lower bound for eta_* does not by itself refute(S). Both inverse estimates and the operator-difference constant belong to those inequalities, and high target norm scaling changes the inverse constant.

Dependencies: proof 177 for the exact norm and residual membership; proof 179 for the exact scalar axis identity and independent point-derivative algorithms.

## Certified result

At t=8 and u=1001/125=8.008, the384-bit all-mode Green-ODE calculation gives the expression in(1) approximately36400585492.45674348985659. Both points were independently reconstructed at1024 bits from the original exact rational Phi controls, explicitly differentiated Green exponential polynomials and the alternative binomial weight series. The derivative enclosures overlap the384-bit computation through every order0 to5. The exact directed lower endpoint of(1) exceeds36400585492. Therefore

 eta_* > 36400585492 > 3.64005 times10^10.

This strengthens proof 179's one-point lower bound in precisely the same high target norm. The pair crosses an original spline join, which is legitimate by the C5 and H^(25/4) membership theorem. All comparisons and source hashes are stored in evidence/final_certificate.json. No hypothesis of(S) other than the residual membership is inferred from this number.
