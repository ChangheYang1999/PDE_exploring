# Finite angular degree of the represented pressure source

Status: proved conditional statement about the exact finite representation. This is not a floating-point error estimate.

## Statement and notation

Let I be an open interval of real parameters. Fix nonnegative integers L_T and L_S. On each compact subset of I times (0,infinity), suppose the scalar potentials have the finite representations

T(p,y) = sum over l<=L_T and m of a_lm(p,|y|^2) H_lm(y),
S(p,y) = sum over l<=L_S and m of b_lm(p,|y|^2) H_lm(y),

where H_lm is a homogeneous harmonic polynomial of degree l on R^3. The coefficients may be real or complex, with the real combinations chosen when a real field is needed. Assume all derivatives in p and in rho=|y|^2 used below exist and are continuous, through three rho derivatives and one p derivative. Define

U = curl(T y) + curl curl(S y),
d = max(L_T+1, L_S+2),
f = tr((DU)^2),
f_p = 2 tr(DU DU_p),

with (DU)_ij = partial_j U_i. At every fixed p and radius r>0, each component of DU and DU_p restricted to y=r n, n in S^2, is the restriction of a polynomial in n of degree at most d. Both f and f_p are restrictions of polynomials of degree at most K=2d. Their spherical-harmonic expansions therefore have no degrees greater than K.

Let L_P>=K. Use an N-point Gauss-Legendre rule for mu=cos(theta) on [-1,1] and M equally spaced azimuths on [0,2pi), with an arbitrary common azimuthal offset. If

2N-1 >= K+L_P,   M > K+L_P,

then exact arithmetic evaluates every spherical-harmonic coefficient of f and f_p through degree L_P exactly by this product quadrature. Its coefficients at degrees greater than K are zero. This includes unnormalized and normalized real or complex spherical harmonics, provided they are the restrictions of the corresponding harmonic polynomials.

## Field degree calculation

It suffices to consider one term a(rho)H_l(y). The identities grad rho=2y, y dot grad H_l=l H_l and Delta H_l=0 imply

curl(a H_l y) = a grad H_l cross y.

For fixed r this is a polynomial in n of degree l. One Cartesian derivative differentiates the polynomial factor, giving degree l-1, or the radial factor, giving an additional y and degree l+1. The toroidal contribution to DU thus has degree at most l+1.

For the poloidal term use curl curl V = grad div V - Delta V. Direct differentiation gives

div(a H_l y) = ((l+3)a + 2rho a') H_l,
Delta(a H_l) = (4rho a'' + (4l+6)a') H_l,
Delta(a H_l y) = y Delta(a H_l) + 2 grad(a H_l).

Combining these equations cancels the a'' terms and yields

curl curl(a H_l y)
= ((l+1)a + 2rho a') grad H_l - 2l a' y H_l.

For fixed r the two angular polynomial degrees are l-1 and l+1. A Cartesian derivative of the first term has degrees at most l-2 and l, and a derivative of the second has degrees at most l and l+2. Terms with negative degree are absent. Thus the poloidal contribution to DU has degree at most l+2.

Differentiation with respect to p replaces a and its rho derivatives by their p derivatives. It leaves the angular polynomials and their degree bounds unchanged. Finite sums preserve the maximum degree bound d. The trace in f and the mixed trace in f_p are sums of products of two such components, so their degree is at most 2d.

A polynomial restricted to S^2 is a finite sum of restrictions of homogeneous polynomials. Each homogeneous polynomial has a harmonic decomposition into homogeneous harmonic polynomials multiplied by powers of |n|^2. On S^2 these powers are one, and every resulting harmonic degree is no larger than the original polynomial degree. This proves the claimed spherical-harmonic support.

## Exactness of the product quadrature

For a coefficient of degree l<=L_P, the integrand is f(n) times the conjugate harmonic polynomial of degree l restricted to the sphere. It is a polynomial in n of degree at most D=K+L_P. The same argument applies to f_p.

Write n=(sqrt(1-mu^2) cos(phi), sqrt(1-mu^2) sin(phi), mu). Each Cartesian monomial of degree at most D is a trigonometric polynomial in phi with frequencies of magnitude at most D. An M-point equally spaced rule with M>D integrates all these frequencies exactly: the average of exp(i k phi) is zero for 0<|k|<=D and one for k=0. The offset only multiplies a nonzero frequency average by a phase and has no effect on this conclusion.

After the azimuthal average, a monomial with an odd total power in either the first or second Cartesian coordinate has zero mean. Every surviving term is a constant times (1-mu^2)^j mu^k, with 2j+k<=D. It is a polynomial in mu of degree at most D. The N-point Gauss-Legendre rule integrates that polynomial exactly when 2N-1>=D. Linearity proves exactness of every requested coefficient.

## Application and scope

A radial smooth twist mixes the real sine and cosine harmonics within one degree; at fixed r it only changes their radial coefficients. Radial envelopes, radial Chebyshev sums, radial core damping and the existing B, D and E channels likewise have the assumed form. Parameter-dependent tail elimination changes radial coefficients and preserves the angular degree bounds wherever the elimination is differentiable.

For a representation with toroidal degrees through 15 and poloidal degrees through 14, d=16 and K=32. A pressure cutoff L_P=36 needs 2N-1>=68 and M>68. In particular, (N,M)=(38,74) and (40,80) meet these exact-arithmetic bounds. For toroidal and poloidal degrees through 6, d=8 and K=16; L_P=18 with (N,M)=(22,44) meets the bounds as well. These substitutions apply only after the stated channel maxima have been checked against the input metadata.

This result excludes angular truncation and angular quadrature error for the stated exact formulas and sufficient grids. It does not bound errors in stored angular tables, represented coefficients, field evaluation, matrix multiplication or radial quadrature. It does not validate a pressure algorithm that uses an inconsistent velocity gradient. Refinement remains useful for measuring those numerical effects. No Euler solution or stationarity statement follows.

## Dependencies

The only external mathematical identities used are Cartesian vector differentiation, the harmonic decomposition of a polynomial, the finite Fourier sum and polynomial exactness of Gauss-Legendre quadrature. The displayed calculation proves the representation-specific degree bound. The represented radial-channel hypotheses are discussed in ../represented_tail_decay/PROOF.md; the full-space pressure convention is specified in ../pressure_consistency/PROOF.md. No formal proof has been run.
