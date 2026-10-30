# Exact redundant directions survive the physical constraints

## Statement

Let B:R^2982->V map the frozen candidate007 generator coordinates
to its potential. The independently confirmed rank is1922 and
dim ker B=1060. Let C:V->R^426 collect its420 independent tail
constraints, center strain and five residual Taylor coefficients.
The confirmed derivative DC at007 has rank426 on V. Let J
be any derivative of finitely many residual, field, weak-pairing
or background-penalty rows which depend only on that potential.

Every vector in ker B lies in ker(DC B) and in ker(J B).
In particular the homogeneous constrained coefficient space
has dimension2556=1496+1060 and contains all1060 exact zero
potentials. The426 physical constraints absorb none of these
1060 directions. For an exact basis Z of ker(DC B), the finite
normal matrix (J B Z)^T(J B Z) has nullity at least1060.
A rectangular Jacobian need not list that many zero singular
values under the convention of listing only min(rows,columns)
values; the normal-matrix statement has no such ambiguity.

## Proof

For v in ker B, B(alpha+t v)=B alpha for every real t. Every
physical constraint and residual row is constant along that
line, so its derivative annihilates v. This uses complete exact
polynomial identities, not numerical residual tolerances. The
map B restricted to ker(DC B) surjects onto ker DC, with kernel
ker B: if DC w=0, choose alpha with B alpha=w and then
DC B alpha=0. Rank-nullity gives

    dim ker(DC B)=dim ker DC+dim ker B
                =(1922-426)+1060=2556.

Thus the426 constraints cannot reduce1060 to1022. Because Z
is injective with image the whole constraint kernel, every
zero potential has a unique coordinate in that image, producing
1060 independent zero vectors of J B Z and its square Gram.
Multiplication by an invertible diagonal rescaling preserves
this nullity. Numerical constraint rows may violate exact
identities by rounding; that is an error to assess, not an
exact absorption of38 directions.

The frozen spectrum code forms binary64 normal matrices and
clips negative eigenvalues to zero. Its count of1022 values
below a relative tolerance1e-8 is a property of those rounded
matrices and thresholds. It cannot replace the exact count
or supply an error bound for the physical residual inverse.

## Damping does not prove that redundancy has no numerical effect

The optimizer adds lambda I after scaling the columns of the
projected Gram to unit diagonal. For every lambda>0 this
regularizes an exact positive semidefinite matrix, including
its kernel. It does not make the physical step independent
of the redundant representation.

For the scalar objective f(x)=(x-1)^2/2 at x=0, a one-coordinate
Jacobian[1] gives the damped step x_new=1/(1+lambda). Represent
the identical physical variable as x=a+b, with Jacobian[1,1].
Both column norms are1, so the same scaling leaves the Gram
[[1,1],[1,1]]. The damped normal equation gives

    a_new=b_new=1/(2+lambda),
    x_new=2/(2+lambda).

The difference is lambda/((1+lambda)(2+lambda))>0. Both systems
are strictly positive definite after damping; their physical
steps differ. The exact check at lambda=1 yields1/2 versus2/3.
This counterexample refutes a universal implication from
regularization to representation independence. It does not
identify the cause of any particular007 failed optimizer step.
That causal claim needs a matched experiment on an equivalent
reduced representation with its constraints and damping metric
specified. The quotient artifact in quotient_coordinates
supplies exact coordinates for such an experiment.

## Independent checks and scope

The verifier checks the retained1060 unit-nonpivot relations
and reconstructs each exact zero radial polynomial from the
raw generator shapes by the Legendre recurrence. Their
endpoint values, endpoint derivatives and every low Taylor
coefficient are therefore exactly zero. The previously
confirmed constraint rank and homogeneous dimensions are
rechecked against both N4 and T4 records. The two small
damped systems are solved over rational numbers. No
optimizer or dense floating matrix is executed.

This is a parameterization audit. It neither constructs a
nonzero PDE near-kernel nor proves that deleting redundancy
improves residual smallness, physical conditioning or closure.
