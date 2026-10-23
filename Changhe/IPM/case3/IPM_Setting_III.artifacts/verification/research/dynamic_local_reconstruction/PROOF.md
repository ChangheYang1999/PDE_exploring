# Independent reconstruction of the shifted dynamic basis

Written 2026-10-21T07:10:02.004730+00:00, before implementation and finite checks. Status: mathematical derivation, numerical validation pending. This result does not establish a profile or trajectory convergence.

## Statement and conventions

Let N be a positive integer, 1 <= M <= N+1, L>0 and P>1. Put sigma=(1+t)/2, w=(1-t)/2 and r=L sqrt(sigma) (1-t)^(-P). For each k<M fix t_k<1, set A_k=2/(1-t_k), B_k=-(1+t_k)/(1-t_k), and specify

beta_k(t)=sum_(j=0)^(N-k) u_kj T_j(A_k t+B_k),
rho(r,theta)=r sin(theta) w sum_(k=0)^(M-1) sigma^k beta_k(t) cos(2k theta).

The stored coefficients and map parameters are exact binary rationals. The checkpoint does not store the nodes t_k used to define its shifted basis. The audit therefore records its reconstructed binary nodes explicitly and compares with an independently rounded high-precision cosine grid. Any claim of equality to the producer field has this reproducibility qualification. No nodal density interpolation is used to replace the specified polynomial.

## Exact change of coordinates

Let C_j be the vector of ordinary Chebyshev coefficients of T_j(A t+B). C_0=(1), C_1=(B,A), and C_(j+1)=2A t C_j+2B C_j-C_(j-1). Multiplication by t is exact in Chebyshev coefficients because t T_0=T_1 and t T_n=(T_(n+1)+T_(n-1))/2 for n>=1. This recurrence follows directly from the defining recurrence for T_j. Induction proves that sum u_j C_j is exactly the same polynomial at every real t, including t values whose shifted coordinate is outside [-1,1]. Rational arithmetic makes this an exact coordinate conversion for the specified binary shifts. It does not justify rounding the converted coefficients when their cancellation is large.

For direct reconstruction evaluate Clenshaw at A_k t+B_k, multiplying its derivative by A_k. The full Cartesian field is evaluated as y w sum beta_k(t) Re[(sigma (x+iy)^2/r^2)^k], with the origin interpreted by continuity. This proves even-x and odd-y symmetry. Since sigma is a smooth analytic function of r^2 near zero and sigma^k cos(2k theta) is a homogeneous harmonic polynomial times a smooth radial factor, every finite representation is locally smooth, including at the axes and origin. At infinity rho=O(r^(1-1/P)) and grad rho=O(r^(-1/P)). Thus the canonical inverse developed in result q_full_inverse_primitives applies. The actual exponent is determined by P; a saved gamma is not silently substituted for 1-1/P.

## Canonical inverse and center data

The exact converted coefficients are passed to the verifier's independently derived compact-coordinate primitive inverse. That inverse sums the full interior and exterior Green moments, without a finite outer boundary. It removes any free xy harmonic term by sublinear velocity growth. Its scalar density and derivatives use the exact converted coefficients at sufficient working precision; cancellation is monitored by repeating the computation at higher precision and by direct evaluation in the shifted coordinates. This reuses verifier code, never producer code.

If a=beta_0(-1), the independent center strain is c=-a/4+int_(-1)^1 [((1-t)/16+P(1+t)/8)(beta_1(t)-(1+t)beta_2(t)/2)] dt. The integrand is a polynomial and the integral is rational for the binary parameters. The expression includes the local cancellation term -a/4; the uncancelled cubic-kernel integral is not absolutely convergent for a*y. The same formula also supplies exterior moments by replacing the lower limit with t(R), omitting the local term when R>0.

Put ell_c^2=L^2 2^(-2P). The cubic density coefficients are b=[2 beta_0'(-1)-a+beta_1(-1)]/ell_c^2 and e=[2 beta_0'(-1)-a-beta_1(-1)]/ell_c^2. At a saved DR state the normalized density is rho_star=rho/cw for cw>0. With cx=C*cw, its residual obeys R_star=-G/cw^2, where G=cw*rho-(cx X+U[rho]).grad rho is the full continuum right-hand side. A numerical projection of G is a separate field and is not substituted into this identity.

## Verification plan and scope

Before evaluating new saved states, check the affine conversion exactly on low-degree rational manufactures, compare direct shifted and converted evaluations at high precision, reconstruct saved beta nodal values, check both parities and Cartesian derivatives, and verify that legacy Chebyshev inputs are unchanged. Then audit matched-time state files using the full inverse. Compare the independent strain to the saved c without imposing its identity. Publish absolute residuals, both pointwise normalization denominators, the actual saved times, source hashes, and empirical precision checks. Numerical agreement at sampled points is not a uniform bound, a continuum convergence theorem, or evidence that a nonstationary state solves the profile PDE.

Dependencies: polynomial algebra, the inverse proof in ../q_full_inverse_primitives/PROOF.md, and the DR correspondence in ../dynamic_rescaling_implementation/PROOF.md. All computational evidence is in verification/. No formal sources are needed for this informal audit.

## Stored basis-node provenance (2026-10-21)

A shifted-basis checkpoint is a function of both its coefficients and the affine maps t -> (2t-1-t_k)/(1-t_k). If the checkpoint supplies the array t_k, that array is part of the field definition. Recomputing it may select another floating-point polynomial. The reader must use stored t_k when present, validate its shape and ordering, and reconstruct the Radau array only as a declared fallback for older states without nodes. Exact conversion uses those same saved binary numbers. A manufacture with deliberately perturbed stored interior nodes distinguishes these two fields and checks snapshot preservation. This strengthens provenance; it does not retrospectively alter any old checkpoint lacking the array.
