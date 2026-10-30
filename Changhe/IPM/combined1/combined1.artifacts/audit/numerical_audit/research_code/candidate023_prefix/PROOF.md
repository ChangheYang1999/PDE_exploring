# Candidate 023: the complete residual prefix through exponent -7/2

## Statement and hypotheses

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma
and the exact rational potential in C1-N1-023-legqs25p100-quot013,
raw SHA256 d67bdd9ff05917736e686af5f834a2e12afede891098ccf8f9de8a6e2d7a71df.
Set rho=-partial_y Delta chi, psi=partial_x partial_y chi,
u=(-partial_y psi,partial_x psi), F=c X.grad rho-rho+u.grad rho.
The field is assumed to have its existing canonical-potential
identification. This calculation concerns exact asymptotic coefficients.

For positive K and nonnegative L write e(K,L)=1-K delta-2L.
There are precisely sixteen labels with e>=-7/2. The proposed statement
is that exactly eleven residual sectors vanish, and the five nonzero
labels, in decreasing exponent order, are
(4,1),(9,0),(5,1),(1,2),(10,0). The first four L=0 density and stream
profiles equal those of accepted candidate 007. Numerical checks of these
candidate-specific assertions are required. No norm, background margin,
inverse, stationary solution or existence conclusion follows.

## Exact expansion and differentiation

Write z=r^(-2), H_m=Re(x+iy)^(2m), p_j=(3+gamma-j delta)/2.
For a generator H_m S^(p_j-m) t_R^w u_R^Q P_N(2t_R-1), where
S=1+r^2, t_R=r^2/(R^2+r^2), u_R=R^2/(R^2+r^2), the radial factor
remaining after r^(2p_j) cos(2m theta) is

 R^(2Q) z^Q (1+z)^(p_j-m) A_N(R^2 z)
                         (1+R^2 z)^(-w-Q-N),
 A_N(z)=(1+z)^N P_N((1-z)/(1+z)).

The Legendre recurrence constructs A_N as an exact polynomial. Its
finite coefficients and the two binomial series give every Taylor
coefficient rationally. This identity follows by t_R=1/(1+R^2 z).
All factors are analytic near z=0; differentiating any fixed finite
number of times preserves the Taylor remainder order. All 504 scaled
terms have Q=4 and hence contribute zero directly at L<=2. Optimized
old coefficients can still change the retained sectors.

A potential term r^d C(theta) yields its exact differentiated angular
polynomials by
partial_x=cos(theta) partial_r-sin(theta) r^(-1) partial_theta and
partial_y=sin(theta) partial_r+cos(theta) r^(-1) partial_theta.
The Laplacian acts on cos(n theta) by d^2-n^2 and lowers radial degree
by two. Finite trigonometric identities compute rho, psi, u and grad rho.
At density exponent alpha_(j,q)=gamma-j delta-2q, the linear residual
is (c alpha_(j,q)-1)rho_(j,q). Products of u_(i,a) with grad rho_(j,b)
have exponent alpha_(i+j+1,a+b). Summing every such ordered pair and
all angular coefficients forms the complete exact residual at that label.
The identity Delta psi=-partial_x rho follows directly from the definitions
and is checked separately in every retained sector.

## Completeness

The program uses j=K-1 and q=L, and retains q<=2 and residual j<=9,
including all field branches needed by products. The first omitted
radial exponent is gamma-6 and the first omitted branch exponent is
gamma-10 delta. Both are strictly below -7/2. Because delta>0 and all
indices are nonnegative, no omitted product can contribute a retained
exponent. Exact rational filtering yields all sixteen distinct labels.
The computed subset is therefore complete at this threshold.

For each retained sector the checker saves full exact density, stream
and residual Fourier maps, the stream identity, its zero/nonzero flag,
and the full-circle residual norm from sqrt(pi sum_n E_n^2).
A nonzero rational coefficient proves nonvanishing. Full-circle
orthogonality proves the displayed norm formula. Arb encloses only its
square root; containing zero is never treated as an exact cancellation.
The first surviving exponent exceeds the omitted bound and is therefore
the actual leading exponent. Earlier rectangular coefficients are
compared wherever retained, and the four leading density and stream
maps are recomputed from raw 007. Independent peer expansion remains
OPEN until it is supplied and compared.

## Dependencies and evidence

The analytic identities, local generator representation and remainder
justification are proved in ../generator_sector_audit/PROOF.md and
../multiscale_generators/PROOF.md. Code uses our homogenized Legendre
recurrence and exact Cartesian homogeneous differentiation. Those
components are already audited, but this candidate application needs
its own peer review. All executed files, exact JSON inputs and earlier
point and shape results are rehashed. No publisher code is executed.
