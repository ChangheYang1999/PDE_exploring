# Finite jets for the radial and twist tables

## Statement

Fix integers K>=0, N>=1, L>=0 and M>=0, real c>0 and omega, R0>0, R1>0, alpha and shift, and an integer d>=0. For each 0<=ell<=L choose either p_ell=alpha+ell-shift or an independently specified real exponent p_ell. Let a subset I of these degrees denote identically zero channels. All functions below are considered on the open real interval rho> -min(R0^2,R1^2), with d=0 interpreted as a unit damping factor. At a node rho0>=0 define

    u=rho+R0^2, s=sqrt(u), x=1-2R0/(s+R0),
    f_ell,k(rho)=(s/R0)^(-p_ell) [rho/(rho+R1^2)]^d T_k(2x-1),
    beta(rho)=omega/(2c) log(1+rho/R0^2).

For ell in I replace f_ell,k by zero. Here T_0(t)=1, T_1(t)=t and T_k(t)=2tT_{k-1}(t)-T_{k-2}(t). The radial and twist tables are

    B[ell,n,k]=f_ell,k^(n)(rho0),
    C[m,n]=(cos(m beta))^(n)(rho0),
    S[m,n]=(sin(m beta))^(n)(rho0),     0<=n<=K.

The truncated jet recurrences below, evaluated in exact real arithmetic, return these tables after multiplying their nth coefficients by n!. They introduce neither a derivative approximation nor new basis functions. The statement holds at rho0=0, including d>0, by smoothness on the stated open interval. It makes no floating-point error bound.

## Jet identities

Write J(f)_n=f^(n)(rho0)/n!. A jet is an element of the quotient ring R[h]/(h^(K+1)). Addition and scalar multiplication are componentwise. The product rule gives

    J(fg)_n=sum_{j=0}^n J(f)_j J(g)_{n-j}.

When a_0 != 0, the reciprocal coefficients b solve ab=1 in this ring. Thus b_0=1/a_0 and

    b_n=-(1/a_0) sum_{j=1}^n a_j b_{n-j}.

For a positive affine argument v=rho0+A with derivative1, the coefficients of (rho+A)^p are binom(p,n) v^(p-n). This follows by n differentiations of a positive real power. Those of log(rho+A) are log(v) at n=0 and (-1)^(n-1) v^(-n)/n for n>=1, by the same differentiation. The binomial coefficients satisfy binom(p,0)=1 and binom(p,n)=binom(p,n-1)(p-n+1)/n.

For a jet a of a smooth function, let b and e be the jets of cos(a) and sin(a). Since (cos(a))'=-a' sin(a) and (sin(a))'=a' cos(a), coefficient comparison gives

    b_0=cos(a_0), e_0=sin(a_0),
    b_n=-(1/n) sum_{j=1}^n j a_j e_{n-j},
    e_n= (1/n) sum_{j=1}^n j a_j b_{n-j}.

Every right-hand side uses only lower coefficients of b,e, so this defines the jets uniquely. The identities establish all listed recurrences without numerical differentiation.

## Assembly and proof of the statement

Use the positive-power recurrence with p=1/2 to obtain s. Add the constant R0, invert the resulting jet, multiply by -2R0 and add1 to obtain x. Its reciprocal exists because s(rho0)+R0>0. Apply the polynomial recurrence defining T_k to the jet 2x-1; the jet product identity proves by induction that the result is J(T_k(2x-1)) for every k<N.

The envelope is u^(-p_ell/2) R0^(p_ell), exactly (s/R0)^(-p_ell). Its jet follows from the affine-power identity and constant scaling. For d>0 the expression 1-R1^2/(rho+R1^2) equals rho/(rho+R1^2), and the reciprocal or affine-power recurrence gives its jet. Repeated jet products give the dth power, including all derivatives at zero. Multiplication by the envelope and polynomial jet then gives J(f_ell,k). Set the entire jet to zero for ell in I. Multiplying coefficient n by n! proves the radial table claim.

For beta, the zeroth coefficient is omega/(2c) log(1+rho0/R0^2). For n>=1 the derivatives of log(1+rho/R0^2) equal those of log(rho+R0^2), since their difference is the constant -log(R0^2). The affine-log recurrence therefore gives every positive-order coefficient. Scale by omega/(2c), then by m, and apply the sine/cosine recurrences. Multiplication by n! proves the twist table claim, including m=0.

All factors are smooth on the stated interval: positive real powers and logarithms have positive arguments, and both rational denominators are positive. The finite polynomial products and compositions therefore justify all derivatives used above. This completes the exact argument.

## Precision and scope

Exact equivalence of 1-R1^2/(rho+R1^2) with rho/(rho+R1^2) does not imply equal finite-precision accuracy near rho=0. Likewise log(1+t) and log1p(t) describe the same exact function but can have different computed errors when t is small. The recurrences prove the mathematical target of a table implementation. Its input convention, working precision, high/low split, cancellation and overflow or underflow still require separate verification. A high/low pair stores two rounded numbers; merely returning two entries is not an accuracy theorem.

Dependencies are finite Taylor coefficients, the product and chain rules, smooth positive powers, and the defining Chebyshev recurrence. No pressure, Euler residual, parameter finite difference or numerical solution is claimed. Numerical evidence belongs in verification; no formal proof or Lean build is performed.
