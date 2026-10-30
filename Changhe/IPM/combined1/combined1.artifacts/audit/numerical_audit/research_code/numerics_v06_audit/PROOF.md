# Exact redundancy and finite asymptotic tables in numerics_v06

## Statements and source scope

The source is immutable numerics_v06, published2026-10-29T04:42:22Z,
and the corresponding N1 far_weak.py. The exact candidate is007 at
c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma.
All results concern that finite campaign generator representation.

First, its potential map has rank1922 and kernel dimension1060. All
physical normalization and residual rows factor through the potential
map, so every one of these1060 directions remains in the kernel after
linearizing those constraints. The426 independent constraint rows give
a2556-dimensional coefficient tangent with1496 physical directions.
The identity is2556=1496+1060. Thus1022 floating spectral zeros cannot
be equated with the exact redundant directions, nor can a remaining
floating spectrum be called the quotient spectrum without constructing
the quotient. The complete exact argument, relations and independent
checks are in ../basis_redundancy/PROOF.md,
../quotient_coordinates/PROOF.md and the N4-178 constraint audit.

A damped coefficient step need not give a coordinate-independent
physical step. For the scalar model J(w)=w and target f=1, minimizing
(w-1)^2+w^2 gives w=1/2. Represent the same physical variable as
w=a+b with identical two columns. Minimizing(a+b-1)^2+a^2+b^2
gives a=b=1/3 and w=2/3. Both Hessians are positive definite.
Thus coefficient damping alone cannot justify dismissing redundancy
as a cause of different physical optimizer behavior. This does not
prove that a particular optimization plateau was caused by conditioning.
Such a causal conclusion remains open without a controlled quotient
comparison or a coordinate-invariant physical metric.

Second, the finite far-field table used by far_weak.py does not equal
the entire far-field residual of007. An exact coefficient omitted by
the table can be computed without the residual assembly as follows.
The canonical potential is

    chi=sum a_(j,m,k) r^(2k) (1+r^2)^(p_j-k) cos(2m theta),
    p_j=(3+gamma-j delta)/2.

For r>1, set z=r^-2. The convergent binomial expansion of each term is

    a r^(2p_j) cos(2m theta) sum_(q>=0) binom(p_j-k,q) z^q.

The generalized binomial coefficients obey b0=1,
b_(q+1)=b_q(p_j-k-q)/(q+1), an exact rational recurrence. This also
follows by the Taylor expansion of(1+z)^(p_j-k) at0; its differential
equation gives the recurrence and analyticity gives convergence for
|z|<1. Termwise Cartesian derivatives are justified on every closed
subannulus r>1. There are only finitely many source generators.

For each q, let d=3+gamma-2q and sum only branchj0. A homogeneous
potential A r^d cos(n theta), n=2m, contributes to density
rho=-partial_y Delta chi the sine coefficients

    sin(n+1): -A(d^2-n^2)(d-2-n)/2,
    sin(n-1): +A(d^2-n^2)(d-2+n)/2.

Negative sine frequencies change sign, and the zero frequency vanishes.
Consequently only m0 andm1 contribute to the first sine harmonic.
Its coefficient at r^(gamma-2q) is the exact rational obtained by
multiplying the displayed factors by
sum_k a_(0,m,k) binom(p0-k,q). The linear residual multiplies it by
c(gamma-2q)-1=-2cq.

The checker computes q0..6, records all exact values and requires the
q4 residual coefficient to be nonzero. Its exponent is gamma-8,
which is below the N1 table cutoff. No other branch or quadratic product
can cancel this coefficient: a residual power is1-ell delta-2q' with
ell>=1, and the q4 coefficient above hasell1. A coincidence would
require(ell-1)delta to be an even integer. For the finite007 residual
branch rangeell2..16, the checker verifies that this is impossible.
The regularized factors therefore leave an actual nonzero omitted
power, not merely a possible error term of unknown sign.

For a finite homogeneous model F_tr=sum r^e S_e, its full-radius probe
pairing against phi_k=r sin(theta)t^k(1+r^2)^-2 is exactly

    sum_e pi s1(e) T_e(k),
    T_e(k)=1/2 B(k+(e+3)/2,(1-e)/2),

provided both beta parameters are positive. The formula follows from
r^2 substitution and sine orthogonality. It is not equality with the
actual smooth residual when F_tr is a truncated asymptotic expansion.
A certified error bound must include both the exterior truncation
remainder and the artificial power model on the interior disk. The
actual residual's interior estimate alone does not control either.
An estimate of the last retained term does not bound the omitted sum.

The separately proved asymptotic law m_k~K k^((e+1)/2), conditional
on a nonzero leading sine coefficient and uniform remainder/growth
bounds, remains compatible with this finding. Sincee<-1 it implies
m_k tends to zero. It supplies neither a finite certified maximizing
index nor a numerical onset radius without quantitative error bounds.
The published finite-list cancellation percentages and convergence
onset300..600 remain floating diagnostics. Coefficient size and initial
term ratios by themselves do not locate the analytic convergence radius.

## Evidence and limits

The checker freezes and hashes the publication, code and prior exact
rank certificate, then recomputes the omitted coefficient directly from
the independently confirmed canonical007 source. No optimizer or
foreign code is executed. All coefficients stay in exact JSON. This
review certifies algebraic distinctions, not a new norm, inverse,
optimizer convergence result or existence/nonexistence claim.
