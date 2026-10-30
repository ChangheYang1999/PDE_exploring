# Exact mode-wise negative norm, strictness and sharpness

This independently checks R2 in the Opus review of the mode-n Hardy lemma.
It does not recheck the separate numerical Galerkin enclosure for007.

## 1. Precise domain and statement

Let n>=1 be an integer, let f be real and measurable on (0,infinity), and
assume both g(X)=f(r)sin(n theta) and r g(X) belong to L2(R2). Define

    ||g||_H = sup_(phi in C_c^infinity, ||grad phi||_2>0)
                   |integral g phi|/||grad phi||_2,
    G(t)=e^(2t) f(e^t).

Use the unitary Fourier transform in t. Then

    ||r g||_2^2=pi ||G||_2^2,
    ||g||_H^2=pi integral |Ghat(tau)|^2/(tau^2+n^2) dtau,     (1)
    ||r g||_2^2/n^2-||g||_H^2
      =(pi/n^2) integral tau^2 |Ghat(tau)|^2/(tau^2+n^2) dtau. (2)

Consequently ||g||_H<||r g||_2/n for every nonzero g. The factor1/n
cannot be reduced and is not attained by a nonzero function. The same
statements hold for cosine modes.

## 2. Proof, including the origin

For a compact smooth test phi, its sine projection is psi(r)sin(n theta),
where psi=pi^-1 integral phi(r,theta)sin(n theta)dtheta. Subtract phi(0)
in this integral to obtain psi=O(r), psi'=O(1) near0. Orthogonality gives

    ||grad(phi_n)||_2^2
      =pi integral_0^infinity (psi'^2+n^2 psi^2/r^2) r dr
      <=||grad phi||_2^2.

The pairing is pi integral f psi r dr and is bounded by
||r g||_2 ||phi_n/r||_2 <= ||r g||_2 ||grad phi||_2/n.
This also proves continuity in the Dirichlet completion.

Let Vhat=Ghat/(tau^2+n^2). Then V is in H2(R) and
-V''+n^2 V=G. For U=V(log r)sin(n theta), polar differentiation gives
-Delta U=g away from0, while

    ||grad U||_2^2=pi integral (|V'|^2+n^2|V|^2)dt
                  =pi integral |Ghat|^2/(tau^2+n^2)dtau.

The origin cannot be discarded without a check. Cutting phi_n off at
r=epsilon changes its Dirichlet norm by O(epsilon), since psi=O(r)
and psi'=O(1). The pairing changes by a quantity tending to0 by the
preceding Hardy bound. Thus the punctured-plane weak identity extends
to every smooth test on the whole plane. There is no delta source at0.
Approximate V in H1 by compact smooth V_j on R. The functions
V_j(log r)sin(n theta) are smooth compact tests supported in annuli,
and their gradients converge to grad U. Testing along this sequence
shows ||g||_H=||grad U||_2, proving(1). Plancherel gives(2). Its integrand
is strictly positive away from tau=0 for nonzero Ghat, up to sets of
measure0, proving strictness.

For optimality choose any nonzero real a in C_c^infinity(R), and set
G_L(t)=a(t/L). The corresponding g_L is a smooth function on an annulus
and satisfies both L2 assumptions. After tau=s/L the squared ratio is

    n^2 ||g_L||_H^2/||r g_L||_2^2
       = integral |ahat(s)|^2 n^2/(n^2+s^2/L^2) ds
                     / integral |ahat(s)|^2 ds ->1.

Dominated convergence proves sharpness, with no distributional extremizer
claimed inside the function space.

## 3. Two exact examples

For f(r)=r^n exp(-r^2), polar integration gives

    ||r g||_2^2=pi (n+1)!/2^(n+3).

With the unitary two-dimensional Fourier transform, the Gaussian has
transform (1/2)exp(-|xi|^2/4). Applying the harmonic polynomial
Im(x+i y)^n gives transform (-i)^n 2^(-n-1)
Im(xi_1+i xi_2)^n exp(-|xi|^2/4). This follows by repeated
multiplication/derivative identities; the derivative of xi_1+i xi_2
under partial_(xi_1)+i partial_(xi_2) is0. Hence

    ||g||_H^2=pi (n-1)!/2^(n+3),
    n^2 ||g||_H^2/||r g||_2^2=n/(n+1).                         (3)

For the separate logarithmic Gaussian a(t)=exp(-t^2/2), G_L=a(t/L),
put x=n L. Both g_L and r g_L remain in L2. Formula(1) gives

    n^2 ||g_L||_H^2/||r g_L||_2^2
      =sqrt(pi) x exp(x^2) erfc(x).                          (4)

To evaluate the integral, write1/(u^2+x^2) as the Laplace integral
of exp(-s(u^2+x^2)), integrate the Gaussian in u, then substitute
v=sqrt(1+s). This gives(4). In particular its deficit from1 lies
strictly between0 and1/(2x^2). This quantitative bound follows by
replacing u^2/(x^2+u^2) by u^2/x^2 inside the Gaussian integral.

## 4. Domain clarification for the proposed extension

The reviewed lemma assumes g and r g in L2; under those assumptions all
claims above are CONFIRMED. If the assumption g in L2 is removed, r g in
L2 alone need not make g a locally integrable function. For example,

    f(r)=1/(r^2 log(1/r)) for0<r<exp(-1), and0otherwise,

has integral f^2 r^3 dr finite, but integral |f|r dr infinite. Its sine
mode is not a regular distribution defined by Lebesgue integration.
An extension is possible by explicitly defining angular cancellation:

    <g,phi> = pi integral f(r) psi(r) r dr,

or equivalently the limit after removing centered disks. The preceding
Hardy estimate makes this a continuous distribution, and the same proof
then gives(1)-(4) on that specified domain. Treating the extended g as an
ordinary locally integrable function without this convention is invalid.
The007 numerical application uses regular smooth functions and is unaffected.
