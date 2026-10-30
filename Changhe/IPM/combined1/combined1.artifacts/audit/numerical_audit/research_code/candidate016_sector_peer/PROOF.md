# Complete exact residual-sector comparison for candidate 016

## Statement, hypotheses, and scope

The reference is the function defined by the immutable rational generator file
for C1-N1-016-legqs25-quot013, SHA256
a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Let c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma.
The potential chi defines rho=-partial_y Delta chi, psi=partial_x partial_y chi,
and U=(-partial_y psi,partial_x psi). The residual is
F=c X.grad rho-rho+U.grad rho. The coefficient functions in this proof
are finite Fourier sine or cosine polynomials on the full circle.

We independently compare all density, stream, and residual coefficients for
the sixteen labels (K,L), K>=1,L>=0, whose exponent
 e(K,L)=1-K delta-2L
is at least -7/2. The proposed conclusion is exactly eleven zero residual
sectors and five nonzero sectors in decreasing exponent order:
 (4,1), (9,0), (5,1), (1,2), (10,0).
The first four L=0 density and stream profiles must equal those of the
separately audited candidate 007. This statement concerns asymptotic
coefficients only. It implies no residual upper norm, existence theorem,
background bound, inverse estimate, or optimality of a finite basis.

## Independent expansion and differentiated remainder

Write z=r^-2. A generator with branch j, angular degree 2m, and rational
positive scale R has potential
 r^(2m) cos(2m theta) (1+r^2)^(p_j-m)
 t_R^w u_R^Q P_n(2t_R-1),
where p_j=(3+gamma-j delta)/2, t_R=r^2/(R^2+r^2), and
u_R=R^2/(R^2+r^2). Mono and unscaled Legendre terms are the stated special
cases. The independent expansion uses the homogeneous polynomial
 A_n(z)=(1+z)^n P_n((1-z)/(1+z)).
Its radial factor after extracting r^(2p_j) is
 R^(2Q) z^Q (1+z)^(p_j-m) A_n(R^2 z)
 (1+R^2 z)^(-w-Q-n).
This follows by substituting t_R=1/(1+R^2 z). The finite polynomial A_n
is obtained from the Legendre recurrence. Convolution of its coefficients
with the two generalized binomial series gives each exact rational Taylor
coefficient. This differs from the peer's expansion of P_n(2t-1) into
powers of t before convolution. Both series are analytic near z=0;
finite differentiation preserves the required asymptotic remainder order.
All new scaled terms have Q=4 and therefore make zero direct contribution
to the field coefficients with L<=2. Optimized unscaled coefficients can
nevertheless change those coefficients.

For every computed homogeneous potential r^d C(theta), differentiate in
Cartesian directions using the polar formulas
 partial_x=cos(theta) partial_r-sin(theta) r^-1 partial_theta,
 partial_y=sin(theta) partial_r+cos(theta) r^-1 partial_theta.
Trigonometric product identities give finite exact coefficient maps for
rho, psi, their derivatives, and U. For density exponent a=d-3, form the
linear residual (c a-1)rho. Add every product U_i.grad rho_j at its exact
rational exponent, using complete Fourier products. Verify separately
 Delta psi=-partial_x rho
for every sector. This checks the stream sign and the homogeneous-degree
shift independently of the nonlinear residual assembly.

## Completeness and equality checks

The local code uses j=K-1 and q=L. It computes q<=2 and j<=9 for the
residual, while retaining every generator branch required in products.
The first omitted radial exponent is gamma-6 and the first omitted
branch exponent is gamma-10 delta. Both are strictly less than -7/2.
Nonlinear sector labels add positive K and nonnegative L, so a factor
outside this range cannot contribute to a retained exponent. Filtering
by exact rational comparison gives all sixteen labels, with distinct
exponents. The thirteen labels common to the earlier rectangular audit
are compared again. The three additional labels (9,0),(1,2),(10,0) are
recomputed in exact arithmetic, not inferred from the publisher's FLOAT
norm table.

At each retained label compare all three complete angular coefficient
maps with the independently derived peer maps. Equality of finite maps
proves equality of the corresponding Fourier polynomials. A nonzero
coefficient proves a nonzero sector. Orthogonality gives the exact
full-circle squared norm pi times the sum of squared sine coefficients;
Arb arithmetic encloses its square root and compares it with the peer's
outward interval. The leading nonzero sector is established because its
exponent is above the complete omitted bound. Recompute the first four
leading density and stream maps from the independently frozen raw 007
input and compare them exactly. This completes the stated argument when
all exact checks succeed.

## Dependencies and evidence

The raw-generator algebra and its analytic remainder argument are in
../generator_sector_audit/PROOF.md and PROOF_CANDIDATES.md; its local
implementation is generator_sector_audit/code/direct.py, using the
Legendre recurrence in multiscale_generators/code/moments.py and Cartesian
homogeneous differentiation in sector_audit/code/sectors_flint.py.
The peer proof and code are frozen under source/ and are read as text only.
The result binds the raw snapshot, all local dependencies, and every
frozen peer file by SHA256. Hashes identify data; the mathematical proof
and exact checks justify claims. No foreign code is executed.
