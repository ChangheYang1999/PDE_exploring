# Independent exact far-field audit of candidate024

## Statement and scope

The reference is C1-N1-024-rulem32-legqs25, with exact generator JSON
SHA256 3472badc9c6b49b8d1d244b0eb3c7569706d541a0ab3df56e0284ca70a35307d.
Let c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
and F=c X.grad rho-rho+U[rho].grad rho. This audit concerns the complete
asymptotic sectors with exponent at least -7/2, the first four leading
density/stream profiles, and their exact zeros. The local point and
normalization checks are separate in ../candidate024_point/PROOF.md.

The claim is that the first residual sector is (4,1), exponent4gamma-5,
that all eleven other required zero sectors in this prefix vanish, and
that the five nonzero sectors are (4,1),(9,0),(5,1),(1,2),(10,0).
Every retained sector is stored with exact rational angular coefficients.
The thirteen sectors common to the cutoff-selected list and N4's
rectangular K<=8,L<=1 list are compared in exact coefficients and norms.
All sixteen rows are compared with the published N1 table. Published
FLOAT values serve only as comparison targets; exact coefficients supply
the zeros. The three additional rows (9,0),(1,2),(10,0) have independently
derived exact nonzero coefficients here, with N1 FLOAT comparisons only.

## Direct generator expansion

Write z=r^-2. The potential generator with angular mode2m, branchj and
specification (w,n,Q,R) is

    r^(2m) cos(2m theta) (1+r^2)^(p_j-m)
      t_R^w u_R^Q P_n(2t_R-1),
    p_j=(3+gamma-j delta)/2,
    t_R=r^2/(R^2+r^2), u_R=R^2/(R^2+r^2).

Use P_n(2t-1)=sum_k b_k t^k with
b_k=(-1)^(n+k) binom(n,k) binom(n+k,k). Factoring r^(2p_j),
the exact radial factor is

    R^(2Q) z^Q (1+z)^(p_j-m)
       sum_k b_k (1+R^2 z)^(-w-Q-k).                 (1)

Thus its coefficient at z^L is the finite convolution of two generalized
binomial series. Formula(1) includes mono with n=Q=0 and R=1, leg with
Q=0,R=1, and legqs. All factors are analytic for |z|<1/R^2. After any
fixed finite number of radial derivatives their Taylor remainders have
the corresponding differentiated asymptotic orders. No convergence at
an intermediate radius is asserted.

All252 scaled generators at radius25, have Q=4. Hence they make exactly zero
contribution to potential, density and velocity sectors with L<=2.
Differentiation changes radial homogeneity but does not lower L. This
is the precise far-field reason these new functions cannot themselves
change any sector in the prefix under examination. Their coefficients
may still change the optimized coefficients of the old generators.

## Homogeneous differential algebra

For one potential coefficient A r^d cos(n theta), put e=d-3. The density
rho=-partial_y Delta chi has sine coefficients

    n+1: -A(d^2-n^2)(d-2-n)/2,
    n-1: +A(d^2-n^2)(d-2+n)/2.

The stream psi=partial_x partial_y chi has sine coefficients

    n+2: +A(d-n)(d-n-2)/4,
    n-2: -A(d+n)(d+n-2)/4.

Negative sine frequencies reverse sign and frequency0 vanishes. These
identities follow by polar differentiation. They agree with the formulas
proved in ../weighted_tail_candidate_audit/PROOF.md. For each resulting
sector, check Delta psi=-partial_x rho as an independent exact identity.

The density exponent of (K,L) is e(K,L)=1-K delta-2L, and the stream
exponent is e(K,L)+1. A stream mode A sin(m theta) at exponent ep+1 and
a density mode B sin(n theta) at exponent et contribute to F at the sum
of their sector labels with coefficients

    n+m: AB[-et m+(ep+1)n]/2,
    n-m: AB[-et m-(ep+1)n]/2.

Together with (c e-1) times the density coefficient this gives every
residual coefficient exactly, without integrating or sampling angles.

## Completeness and comparison

Since K>=1,L>=0 and delta>0, e>=-7/2 allows only L=0,1,2 and finitely
many K. The code enumerates this exact rational condition rather than
relying on floating cutoffs. Products contributing to such a sector have
positive K and nonnegative L, so every factor required is retained.
Distinct labels in this prefix have distinct rational exponents. The
first omitted K and L give exponents below the cutoff.

The first four L=0 density and stream profiles are compared exactly with
the separately accepted007 coefficient table. The first nonzero residual
coefficient gives the full-circle angular norm sqrt(pi sum a_n^2), with
outward Arb arithmetic. This establishes asymptotic structure and
weighted membership obstructions only. No residual upper norm, inverse,
stationary profile or optimality of this candidate follows.
