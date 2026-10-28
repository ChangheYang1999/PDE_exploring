# Pointwise lower bounds for the high residual norm

Status: original-data evaluations and independent derivative and scalar audit complete.

## Statement and exact norm

Use the exact normalized original trial, parameter, canonical full-plane velocity, and explicit high target norm eta_* of proof 177. In particular sigma=25/4, a_*(t)=exp(9t/5)(1+exp t)^(-53/10), and g_axis(t) is the vertical-axis value of F/(r^3 p a_*), where p=cos(theta)^2 sin(theta). The norm includes ||g_axis||H^sigma(R) as an orthogonal summand. For every real t and integer 0<=j<=5,

 eta_* >= |g_axis^(j)(t)|/C_j,
 C_j^2=Gamma(j+1/2)Gamma(sigma-j-1/2)/(2pi Gamma(sigma)). (1)

A strictly positive directed lower bound for the numerator and an upper bound for C_j therefore certify a high-norm lower bound. Finitely many pointwise bounds may be maximized, but may not be added without further justification. No nonlinear smallness conclusion follows from such a bound alone.

## Proof of the functional inequality

The scalar Fourier transform is unitary, as in proof 177. For f in H^sigma(R), Cauchy-Schwarz in the inverse transform gives

 |f^(j)(t)| <= (2pi)^(-1/2)[integral_R xi^(2j)(1+xi^2)^(-sigma) dxi]^(1/2) ||f||H^sigma.

The integral is the beta function B(j+1/2,sigma-j-1/2), by u=xi^2. It is finite precisely when sigma>j+1/2. This also gives the continuous representative of each derivative through order5. Proof 177 proves membership of the actual axis residual in H^sigma, including the C5 joins, so the inequality applies to the exact trial at every point. Taking the axis summand in eta_* proves (1).

## Original-data derivative reconstruction

Write H=r^(-3)rho=sum_m H_m(t)sin((2m+1)theta). Let

 A(t)=-1/2 sum_m (-1)^m(2m+1)^2 H_m(t),
 d(t)=ell-sum_(n>=1)(-1)^n P_n(t), D=4ell-1.

The exact cofactor trace of the residual is

 gamma=d A'+(D-d-2d')A, g_axis=gamma/a_*.

This is the same independently verified axis identity as topics105 and175. All sums retain every original angular mode. Derivatives through order5 use A through order6 and d through order6. On open spline cells the H derivatives follow directly from the exact polynomial representation. On either end they follow by differentiating its exact exponential-polynomial representation.

For an independent reconstruction of the velocity derivatives, put R_m=exp(2t)H_m and let I_n,J_n be the scaled canonical Green quantities. Their point values are recovered from P_n,Q_n by

 I_n=[Q_n+(R_(n-1)+R_n)/2-P_n]/(2n),
 J_n=[Q_n+(R_(n-1)+R_n)/2+P_n]/(2n).

Then I_n'=-(2n+2)I_n+R_(n-1), J_n'=(2n-2)J_n-R_n and P_n=n(J_n-I_n). These exact ODEs give every required derivative. The first derivative is checked against the independently evaluated canonical point formula. Differentiating the displayed axis identity by Leibniz's rule gives gamma^(j).

Finally set m=1/a_* and z=exp(t)/(1+exp(t)). If P_0=1 and

 P_(j+1)=(-9/5+53z/10)P_j+z(1-z)P_j',

then m^(j)=m P_j(z). This is the rational polynomial recurrence already independently audited in proof 177. Leibniz's rule gives the weighted axis derivatives. Exact rational points, original input hashes and every directed enclosure are retained in JSON. No numerical result is accepted until the independent audit is complete.

## Independent reconstruction required for the final certificate

At the strongest sampled interior point, the second calculation forms the exact rational axis control values directly as the alternating sum of the original Phi_m B-spline controls. It evaluates their derivatives by the B-spline derivative identity, without modal angular division or the local polynomial conversion used above. The canonical velocity is reconstructed as exponential polynomials on the containing cell and differentiated explicitly, instead of using the Green ODE jet recurrence. Finally, the multiplier derivatives are obtained by expanding

 m(t+s)=m(t)exp(-9s/5)[1+z(t)(exp(s)-1)]^(53/10)

through degree5 with the rational binomial theorem. The axis product is then computed as a product of ordinary Taylor series. Agreement with the earlier full-angular and Green-ODE derivative enclosures is required. The exact rational lower endpoint must exceed the reported rational bound; an approximate decimal midpoint is not sufficient.


## Certified numerical result

The 640-bit all-angular replay gives a lower-bound expression at t=8 and j=5 of approximately1906360017.4332740800846. The independent1024-bit calculation from the exact rational Phi B-spline controls, explicitly differentiated Green exponential polynomials and a binomial weight series overlaps every residual derivative through order5. Its exact lower endpoint exceeds1906360017. Therefore, in the precise equivalent high norm of proof 177,

 eta_* > 1906360017 > 1.90636 times10^9.

Together with V182, this encloses the norm between1906360017 and6.321 times10^129. Neither endpoint is an estimate of the true norm. The lower bound is a single-point Sobolev consequence and the upper bound uses deliberately crude derivative and cutoff majorants. Both concern the same exact normalized modal object and the same fixed high target norm. They prove no inverse estimate or failure of nonlinear existence. In particular a large value of eta_* alone does not refute (S), whose inverse constants change when the norm changes.

The384-bit pilot at t=2 and4 overlaps the640-bit replay there. The latter additionally checks t=0,6,8,10 and all six scalar-axis derivatives against full angular convolution and exact cofactor division. The strongest point t=8 was then reconstructed by the independent algorithm above at1024 bits. Input, scalar correction, canonical Green boundary data, source code and proof hashes are bound in evidence/final_certificate.json. The full upper-bound membership theorem supplies the pointwise derivative representatives; no unsupported trace of an arbitrary weak residual is taken.
