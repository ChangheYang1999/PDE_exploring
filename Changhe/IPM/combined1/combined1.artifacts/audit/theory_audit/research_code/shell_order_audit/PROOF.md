# Audit of the shell approximation rate

## Setting and claims

Let T>0, 0<epsilon<T/2, and eta be smooth, nonnegative, supported in(0,1), with integral1. Use the homogeneous negative Sobolev norm on the S1 class and the polar delta convention from the independently reviewed exterior-extension proof. Let mu(theta) be square integrable and S1. The shell approximation is

    g_epsilon(r,theta)=T mu(theta) eta((T-r)/epsilon)/(r epsilon)

on T-epsilon<r<T and zero elsewhere. Set m_p=int_0^1 s^p eta(s)ds. Then

    ||g_epsilon-mu delta(r-T)||H
       <=sqrt(T epsilon) sqrt(T/(T-epsilon)) m_(1/2)||mu||2.  (1)

For a single odd angular mode mu=mu_n sin(n theta), n>=1 odd,

    ||g_epsilon-mu delta(r-T)||H
       >= m_1 sqrt(T epsilon)||mu||2
          /sqrt(1+n epsilon/T+2n^2 epsilon^2/T^2).           (2)

These are the two new claims in the frozen T2 review. They imply sharpness of the epsilon^(1/2) order for each fixed nonzero mode and fixed eta. No assertion of an optimal leading constant is needed.

## Upper bound

For a smooth compact test psi, polar substitution gives the pairing

    T int mu(theta) int eta(s)[psi(T-epsilon s,theta)-psi(T,theta)]ds dtheta.

The fundamental theorem of calculus and weighted Cauchy-Schwarz bound the angular L2 norm of the bracket by

    sqrt(log(T/(T-epsilon s))) ||grad psi||2
       <=sqrt(epsilon s/(T-epsilon)) ||grad psi||2.

Integrating eta and using angular Cauchy-Schwarz proves(1). The S1 projection is contractive in homogeneous H1 and preserves the pairing, so the full dual norm and the S1 dual norm agree. The layer and shell have the same zero mean, and no constant-mode quotient is left unspecified.

## Lower bound

Choose psi=zeta(r)sin(n theta), where

    zeta(r)=epsilon(r/(T-epsilon))^n,  0<=r<=T-epsilon;
    zeta(r)=T-r,                      T-epsilon<=r<=T;
    zeta(r)=0,                        r>=T.

This continuous piecewise smooth function has square-integrable gradient and is in the closure of smooth compact S1 tests. Its pairing with the shell-minus-layer is pi T mu_n epsilon m_1. The layer contributes zero because zeta(T)=0.

The exact interior gradient energy is pi n epsilon^2: the radial and angular terms are equal, and their sum integrates to that value. On the shell the radial energy is pi(T epsilon-epsilon^2/2), while the angular energy is at most

    pi n^2 epsilon^3/[3(T-epsilon)] <=2pi n^2 epsilon^3/(3T).

Dropping the favorable negative term and replacing2/3 by2 gives the denominator squared in(2), after dividing by pi T epsilon. Since ||mu||2=sqrt(pi)|mu_n|, homogeneous duality proves(2). For fixed n and eta, m_1>0, so the order cannot be improved.

## Verdict and scope

Both new T2 estimates are CONFIRMED. The review independently confirms estimate(4) in the earlier T4 proof, so that shell approximation is now AUDITED. The original minimization and remainder arguments were T2-origin claims independently checked by T4; T2 correctly labels its own further check of those parts as a consistency check.

A quantitative increase in the minimum negative norm under a prescribed L2 upper bound is not proved by these shell estimates alone. The review labels that extension heuristic, correctly. Neither bound certifies an IPM residual, onset radius, or far-field remainder for a candidate. The proof depends only on the displayed shell construction, elementary polar integration and homogeneous Sobolev duality.
