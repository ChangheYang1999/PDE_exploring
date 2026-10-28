# A uniform elementary linear error envelope

## Statement

Use the real and complex scalar-operator Holder spaces and the constants
C_a, D_a, C0, E, N0, L, B_C, B_D of
../linear_remainder/PROOF.md. Fix 0<rho<1/2 and 0<epsilon<1. Put

    ell_C = log(rho)+log(2)/2-1/2,
    ell_D = log(rho)+log(2)-1,
    P = (2^epsilon-1)/epsilon,
    Z = (N0(rho)+E(rho))P
        +2^(epsilon+1)/pi [1/(1-epsilon)+1/2-log(3/2)],
    K_C = (ell_C^2+1/4)/pi+Z+B_C(rho)+E(rho)L(rho),
    K_D = (ell_D^2+1-pi^2/12)/pi+Z+B_D(rho)+3E(rho)L(rho).

Then for every 0<a<=epsilon,

    C_a <= 2/(pi a)+C0+K_C a,
    D_a <= 2/(pi a)+2C0+K_D a.                              (1)

These constants use only elementary functions. The proof depends on the
linear-remainder transport theorem, whose independent lead cross-read
is pending at the time this note is written. Numerical simplifications
of K_C and K_D are to be recorded in verification and accepted only after
outward evaluation.

## Proof

Write the local C contribution as

    2a2(a)rho^a/a = [2/(pi a)] exp(h_C(a)),
    h_C(a)=a[log(rho)+log(2)/2]-log(1+a/2).

Then h_C(0)=0, h_C'(0)=ell_C<0, h_C' is negative and increasing,
and 0<h_C''(a)<=1/4. Consequently

    (exp(h_C))'' = exp(h_C)[(h_C')^2+h_C'']
                  <= ell_C^2+1/4,

and Taylor's formula with integral remainder gives

    2a2(a)rho^a/a <= 2/(pi a)+2ell_C/pi
                           +[(ell_C^2+1/4)/pi]a.            (2)

For D, write

    2A(a)rho^a/a = [2/(pi a)] exp(h_D(a)),
    h_D(a)=log(pi A(a))+a log(rho).

The gamma-ratio formula gives h_D(0)=0, h_D'(0)=ell_D<0 and

    h_D''(a) = (1/4) integral_0^infty
           t exp(-(1+a/2)t)(1-exp(-t/2))/(1-exp(-t)) dt.

Thus h_D'' is positive and decreasing, with value 1-pi^2/12 at zero.
Also h_D'(a)<0 because log(rho)<0 and the digamma difference
[psi(1+a/2)-psi(3/2+a/2)]/2 is negative. The same argument proves

    2A(a)rho^a/a <= 2/(pi a)+2ell_D/pi
                           +[(ell_D^2+1-pi^2/12)/pi]a.      (3)

Convexity of 2^a implies (2^a-1)/a<=P on 0<a<=epsilon. The factor
2^(a+1)[1/(1-a)+1/2-log(3/2)] is positive and increasing there.
Hence the nonlocal terms of the linear-remainder theorem are bounded
by N0(rho)+aZ, apart from its explicitly linear B and E L terms.
Substitute (2) or (3). The identities

    2ell_C/pi+N0(rho)=C0,
    2ell_D/pi+1/2+N0(rho)=2C0

complete the proof of (1). There is no parameter optimization, limiting
argument in the operator norm, or sampled-exponent assertion in (1).
