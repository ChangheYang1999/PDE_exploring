# Independent audit of a parity-based Hilbert-Schmidt budget

## Statement and scope

Let rho be the exact smooth S1 density of C1-N1-008-d2w-j7-x3bal,
with canonical SHA-256
13fe3fb1d9204b61e08599da7c4f5d6584034666040305bd01e4dde1783677f1.
It is even in x, odd in y, and has the differentiated sublinear tails
required by the audited gradient-commutator identity. Put a=rho_x,
b=rho_y, R_j=partial_j(-Delta)^(-1/2), and

    K=[R1,[R1,b]]/2-[R1,[R2,a]]/2.

The exact Hilbert-Schmidt identity is

    kappa²=((log2-1/2)||D a||2²+(3log2-2)||D b||2²)/(16pi).

For n>=0 define f_n=partial_z^n(z²+r²)^(-1/2)|_(z=1) and
h_n=-Delta f_n. For a positive integer d let G and B be the d by d
matrices with entries <h_j,h_i> and <K h_j,h_i>. Then G is positive
definite, T=tr(G^-1 B G^-1 B)>=0, and

    ||K restricted to S1||op <= sqrt(kappa²-T).

The computation audits G, B, T and the remaining bound at d<=12
against an independently produced T4 record. It does not certify a
new nonlinear inverse, a full-plane theta bound or existence. The
low-generator extension remains the separately reviewed theory input.

## Why a different symmetry block can improve the bound

Each x or y reflection changes the sign of the appropriate Riesz
transform and of a, while b is even in both variables. Expanding the
double commutators shows that K commutes with both reflections. K is
self-adjoint and Hilbert-Schmidt by the gradient-commutator identity.
The four parity subspaces are therefore orthogonal reducing spaces.
Every h_n is even-even, orthogonal to S1. If P is the projection onto
their span, the Hilbert-Schmidt sum over an adapted orthonormal basis
gives ||K|S1||HS²+||PKP||HS²<=kappa². The coefficient map S satisfies
S*S=G and S*KS=B, so SG^-1/2 is an isometry and
||PKP||HS²=tr(G^-1 B G^-1 B). This proves the bound.

## Independent construction of the test family and Gram matrix

Use the nonunitary Fourier transform integral exp(-i X.xi)f(X)dX.
The harmonic Poisson extension identity gives
hat f_n(xi)=2pi(-|xi|)^n exp(-|xi|)/|xi|, interpreted as a tempered
distribution for n=0. Multiplication by |xi|² makes each h_n an L2
function. A finite dependence of h_n would give a zero polynomial
in |xi| on (0,infinity), so the family is independent. Plancherel and
polar integration directly give the exact formula

    G_ij/pi=(-1)^(i+j)(i+j+3)!/2^(i+j+3).

This checks the entire Gram matrix without reusing a radial integral.
The real-space functions are constructed independently by

    f_n(t)=(-1)^n n! (1+t)^(-(n+1)/2)
                         P_n((1+t)^(-1/2)), t=r²,

where P_n is the Legendre polynomial. Its coefficients follow from
Rodrigues' formula:

    P_n(z)=2^-n sum_(k=0)^floor(n/2)
        (-1)^k (2n-2k)!/[k!(n-k)!(n-2k)!] z^(n-2k).

Substitution yields finite rational sums of (1+t)^(-p), with
half-integer p. Differentiate these sums directly with respect to t.

## Direct gradient formula for the compression

The Poisson relation (-Delta)^(1/2) f_n=-f_(n+1) gives
R_j h_n=-partial_j f_(n+1). Set H_n=-4(f_n'+t f_n''), and

    A_ij=-2(H_i f_j''+H_j f_i'')-4 f_(i+1)' f_(j+1)',
    D_ij=H_i f_j'+H_j f_i'.

Expanding Sym(U[.].D rho)-P0, with
P0=R1 b R1-(R1 a R2+R2 a R1)/2, yields

    B_ij=integral [a xy A_ij+b(D_ij-x² A_ij)] dX.

Here U1[h_n]=-partial_xy f_n and U2[h_n]=partial_xx f_n.
Only the sine2 coefficient a2 of a and the cosine0,cosine2
coefficients b0,b2 of b survive angular integration. With radial
coefficient functions expressed in t,

    B_ij/pi=integral_0^infinity
       [t A_ij(a2-b2-2b0)/4+D_ij b0] dt.                 (1)

This formula is evaluated directly from the independently
Cartesian-differentiated background. It does not integrate by parts
onto the density, unlike the peer computation.

Write u=t/(1+t), v=1-u. For each branch of the original potential,
its fourth Cartesian derivatives have the form
v^alpha Q(u), alpha=(j+1)(1-1/c)/2, with Q obtained by exact division
of the stored numerator by u². All such divisions are checked.
A term (1+t)^(-k) times the gradient and t has integral

    sum_l Q_l Beta(l+2,k+alpha-2),

and the term without t has integral

    sum_l Q_l Beta(l+1,k+alpha-1).

The relevant beta parameters are strictly positive. For positive
integer m and rational q, Beta(m,q)=(m-1)!/product_(j=0)^(m-1)(q+j),
so both integrals are exact rationals. All polynomial cancellation
occurs before outward evaluation. Equation (1) therefore constructs
an exact B/pi from the full-plane gradient without quadrature.

## Verification obligations

Compare every entry of G/pi and B/pi against the frozen peer matrix,
then compare exact T at d=1,2,4,8,12. Check all LDL pivots of G are
positive, all captured energies are nonnegative and no greater than
the full kappa² enclosure, and all final outward square roots overlap
the peer results. The full kappa is computed using the independently
confirmed background energies of N4-107. All input hashes are retained.
These arithmetic checks are distinct from a later candidate-specific
full-plane signed bound or a nonlinear closure claim.
