# Independent audit of the potential basis rank

Status: independent audit of N4-158; arithmetic result recorded separately.

## Exact statement and hypotheses

Use the frozen exact candidate C1-N1-007-d2w-j7-e2bal, with c =
4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
Its 2982 variable potential generators have labels (j,m,spec). Put
s=x^2+y^2, t=s/(1+s), H_m=Re(x+iy)^(2m), p_j=(3+gamma-j delta)/2.
The common factor in a block (j,m) is H_m(1+s)^(p_j-m); its columns
are t^w for spec=(mono,w), and t^w P_n(2t-1) for spec=(leg,w,n).
The rank is the dimension over the real numbers of their function span.
The claimed rank is 1922, with exactly 1060 zero-potential directions.

## Proof and independent arithmetic method

Generate the shifted Legendre polynomials by their three-term recurrence,
starting at P_0=1 and P_1=2t-1. This uses rational arithmetic throughout.
Each resulting column has integer coefficients. In a block let S be the
union of the degrees with nonzero coefficient. The dimension is at most
min(number of columns, |S|). Reduce the integer column matrix modulo the
prime 2147483647 and compute its rank by row elimination. If this modular
rank equals the upper bound, the rational and real ranks equal that bound:
a nonzero modular minor comes from a nonzero integer minor. The primality
is checked by exact trial division up to its integer square root, so the
modular argument has no primality assumption hidden in software.

The verifier also checks every N4 kernel relation directly, using the
independently generated recurrence columns. Each relation has coefficient
one in its stated nonpivot position and zero in all other nonpivot
positions. Hence those relations are linearly independent. Their count
is the difference between column count and the independently certified
rank, so they form the complete kernel within their block.

Distinct angular labels cannot cancel by Fourier orthogonality. For fixed
m, use u=1/(1+s). A nonzero polynomial in t=1-u has a first nonzero integer
power u^k. The leading radial power in branch j is u^(m-p_j+k).
For different j these exponents cannot agree, since (j-j')delta/2 is not
an integer. The verifier checks every pair of the finitely occurring
branch labels over the rationals. In any proposed nontrivial relation
there is therefore a unique least leading exponent; divide by its power
and let u tend to zero to contradict the relation. The full rank is the
sum of the block ranks, proving the assertion after the finite checks.

## Meaning for optimization and scope

A zero-potential relation leaves every derivative of the potential
unchanged. Therefore it leaves rho, U, F, physical background constraints,
tail coefficients and origin jets unchanged for every perturbation size.
It belongs to the nullspace of the exact residual Jacobian and of every
physical linearized constraint. If all columns remain variable, restriction
to that constraint kernel retains all 1060 directions. They do not define
nonzero density perturbations or a PDE kernel. Coefficient constraints that
are not functions of the physical fields need separate checking.

This result concerns the potential representation. It does not assert
that differentiation from potentials to densities is injective. It does
not establish an inverse, an optimization improvement, or any smallness
claim. Floating normal matrices also need assembly and spectral error
bounds before a small positive singular value can be resolved. The
frozen implementation is read only; no optimizer is executed.

Dependencies: shifted Legendre recurrence, elementary linear algebra over
Q and a finite field, Fourier orthogonality, and the displayed asymptotic
argument. Exact inputs and independently checked counts are retained with
hashes in source/ and verification/.
