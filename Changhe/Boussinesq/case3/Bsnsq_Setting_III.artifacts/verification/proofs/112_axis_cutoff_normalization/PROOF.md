# Axis transport with an inexact center slope and finite cutoffs

Written 2026-10-21T02:38:54.050870+00:00. Status: conditional proof completed before numerical checks;27 manufactured finite-cutoff controls passed, and actual Opus146 returned a full written confirmation. Native inverse/axis checks completed; see verification/SUMMARY.md. No B2 profile is asserted.

## Statement and notation

Fix beta>2, a0>0, mu=3beta/2+1, P=(2beta+1)/mu, rho=(beta+1)/mu, ell=mu/beta and s=1/beta. Let v>0 on(0,infinity) be C1, with v(r)=k r+O(r^(1+delta)) and v'(r)=k+O(r^delta) at0 for k,delta>0, and v(r)=beta r+O(r^(1-s)) at infinity. Put A=2beta-v'. The exact axis temperature equation for H=Theta_xx(0,r) is

    v H'=(beta-2-2A)H=(2v'-2mu)H.                     (1)

A finite nonzero center limit H(0)=2a0 is possible only if k=mu. If k differs from mu, every nonzero solution of(1) behaves as H(r)=C r^h(1+O(r^delta)), where h=2-2mu/k. In particular a small center error cannot define an exact globally center-normalized solution, even if its cutoff effect is numerically small.

## Proof and cutoff dependence

Divide(1) by vH and subtract h/r. The remainder is O(r^(delta-1)), integrable at0. Integration proves the stated asymptotic, including a finite nonzero multiplicative constant. If h>0 the center limit is0; if h<0 it is infinite. Thus a nonzero finite center limit requires h=0.

The numerical closed formula in packet107 uses a center-normalized auxiliary coordinate zeta. With a finite inner cutoff epsilon, define instead

    zeta_epsilon(r)=r exp integral_epsilon^r(mu/v(t)-1/t)dt, r>=epsilon.

Let e=1-mu/k, so h=2e. Since mu/v-1/r=-e/r+O(r^(delta-1)), at any fixed positive r,

    zeta_epsilon(r)=epsilon^e Z(r)(1+O(epsilon^delta)),
    Z(r)=r^(mu/k)(1+O(r^delta)) at0.                   (2)

The positive limiting function Z is obtained by integrating the integrable remainder; the same multiplicative error is independent of r>=epsilon. At infinity Z=C_* r^ell(1+O(r^-s)), with C_*>0, because mu/v-ell/r=O(r^(-1-s)). Hence the inferred constant C_epsilon=lim zeta_epsilon/r^ell satisfies C_epsilon~epsilon^e C_*.

Assume also k>beta+1, as for a sufficiently small center error. Then (mu/k)rho=(beta+1)/k<1, so I_*=integral_0^infinity Z^-rho is finite. The code's analytic fill below epsilon corresponds to

    I_epsilon=epsilon^(1-rho)/(1-rho)
                         +integral_epsilon^infinity zeta_epsilon^-rho.

Using(2), the second term is asymptotic to epsilon^(-e rho) I_*. The fill is lower order since 1-rho+e rho=1-(beta+1)/k>0. Consequently the cutoff-based expression obeys

    Q_epsilon=(2a0 beta/mu²) C_epsilon^-P I_epsilon
       ~ (2a0 beta/mu²) C_*^-P I_* epsilon^-h,          (3)

where P+rho=2. This proves the cutoff scaling. It is not the far-axis slope of a true center-normalized profile when k!=mu. In particular k<mu gives Q_epsilon->0 and k>mu gives Q_epsilon->infinity as epsilon->0. For small fixed errors the dependence over a finite number of decades can be tiny; the theorem does not establish that any reported finite-cutoff number is grossly inaccurate.

## Far cutoff

For k=mu, or for a fixed inner normalization, write zeta=C r^ell(1+O(r^-s)). Since ell rho=1+s,

    integral_R^infinity zeta^-rho dr
           =beta C^-rho R^-s+O(R^-2s).                (4)

This follows by integrating the asymptotic bound termwise with an error majorant, not by assuming a complete series. Thus omitting this integral gives a slow algebraic error. Replacing C by C_R=zeta(R)/R^ell also incurs O(R^-s), and can change the sign of the total error. Adding the leading term of(4) does not remove the separate C_R bias. Exact axis ODEs do not make finite quadrature, interpolation, initial cutoff or exterior truncation exact.

## Scope and verification

The identities A+v'=2beta and(1) are independently derived from divergence and the x² coefficient of temperature transport. Packet107 supplies the correct formula when k=mu. Current saved fields are already rejected nonsolutions; the purpose here is to interpret their Q diagnostics, not to assert an additional full-class obstruction. Numerical checks will use the verifier's full-plane inverse, not the numerics lane's inverse or characteristic code. Compare both pure B2 velocity and the explicitly forced velocity. Read the actual center defect before making any applicability claim.

No JavaScript/TypeScript, servers, RLScience cluster, Lean/Lake or GPU execution.

## Manufactured family for numerical calibration

For v(r)=k r(1+r²)/(1+(k/beta)r²), direct partial fractions give

    zeta_epsilon=Ce r^(mu/k)(1+r²)^tau,
    Ce=epsilon^(1-mu/k)(1+epsilon²)^(-tau),
    tau=(mu/beta-mu/k)/2.

Thus C_epsilon=Ce and C_R=Ce(1+R^-2)^tau. With a=(1-(beta+1)/k)/2>0 and b=1/(2beta), substitution u=r²/(1+r²) gives

    integral_epsilon^R zeta_epsilon^-rho dr
       =Ce^-rho/2 integral_(epsilon²/(1+epsilon²))^(R²/(1+R²))
                                u^(a-1)(1-u)^(b-1)du.

This proves the incomplete-beta reference used in27 controls, independently of adaptive log-radius integration. The inner analytic fill is the artificial k=mu fill even when k!=mu; this is deliberately the cutoff diagnostic under test and is not a valid exact center normalization. The result remains subject to k>beta+1 as stated above.
