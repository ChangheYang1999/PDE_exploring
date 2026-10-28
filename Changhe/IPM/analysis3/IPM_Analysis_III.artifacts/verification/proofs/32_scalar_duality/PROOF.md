# A scalar estimate does not require a full inverse

## Exact statement

Let X and Y be real Banach spaces, L:X->Y bounded and linear, and c in X*.
Then the following are equivalent for any C>=0:

1. |c[h]|<=C||Lh||_Y for every h in X.
2. There is phi in Y* with ||phi||<=C and L*phi=c.

The optimal constant in1 is the minimum norm of a solution in2. In
particular, neither injectivity nor closed range of L is required.
For a closed unbounded operator on a base space, take X to be its domain
with its graph norm. The adjoint in2 is then the Banach-space transpose
of that bounded domain-to-target map, not an unqualified formal PDE adjoint.

## Proof

Condition2 implies1 by the definition of the dual norm. Conversely1 implies
c=0 on ker L. Thus the formula phi0(Lh)=c[h] defines a well-defined linear
functional on range L, with |phi0(f)|<=C||f||_Y. It extends continuously to
the closure of the range, and the Hahn-Banach theorem extends it to Y with
the same norm. The extension phi satisfies L*phi=c. Applying this construction
with the exact supremum of |c[h]|/||Lh|| proves attainment of the optimal
constant, when finite. If c=0, the zero functional gives the assertion.

## Two explicit counterexamples to necessity of an inverse

On X=R2 and Y=R, let L(x1,x2)=x1 and c(x1,x2)=x1. Then1 holds with C=1,
although L has a nontrivial kernel and no inverse.

Even injectivity does not repair the claimed implication. On X=Y=ell2,
let (Lh)_n=h_n/n and c[h]=h_1. Then |c[h]|<=||Lh|| and phi(f)=f_1 is an
exact dual solution. L is injective and has dense range, since its range
contains every finite sequence. Its range is not closed: the vector
f_n=1/n lies in ell2 and in the closure of the range, but its putative
preimage is the constant sequence1, outside ell2. Also ||L e_n||=1/n
while ||e_n||=1, excluding any bounded inverse estimate. Thus a scalar
estimate can survive even when no whole-space coercive estimate exists.

These examples refute the general logical assertion in the submitted
S2_C_FUNCTIONAL.md section8.1 that no route to a c-estimate avoids a full
inverse bound. They do not prove a c-estimate for the IPM operator.

## A possible rigorous approximate-dual certificate

Suppose phi in Y*, ||c-L*phi||_X*<=delta, and one has the independent
conditional estimate

    ||h||_X<=A||Lh||_Y+B|c[h]|                         (3)

for all h in X, with A,B>=0. If delta B<1, then

    |c[h]|<=(||phi||+delta A)/(1-delta B) ||Lh||_Y.    (4)

Indeed |c[h]|<=||phi||||Lh||+delta||h||, and substitution of3 followed
by absorption proves4. This is a useful weaker target when a single
scalar obstruction remains. It does not claim3 for IPM. An approximate
adjoint residual measured only in X* is insufficient without a relation
such as3, because high-frequency near-kernel vectors can have large X
norm relative to their image norm.

For a finite-dimensional obstruction E rather than one scalar, the same
argument applies with a vector of functionals and a matrix absorption
bound. All domain and dual norms must be specified before numerical
adjoint residuals have this meaning.

## Consequences for the current IPM spaces

For the radial fixed-operator graph, the unit-strain packets of proof 29
satisfy c[h_n]=1 and Lfix h_n->0. Therefore no estimate1 holds there,
regardless of a Fredholm theorem for Lfix. In that weak graph c is not even
a bounded graph functional, which is a separate obstruction before any
dual calculation.

For the strengthened space Z_cap of proof 31, c is bounded. For any actual
operator realization X continuously embedded in Z_cap and mapping to the
chosen Y, the criterion above applies. A scalar c-bound is an adjoint
solvability problem on that realization. A bounded full inverse is one
sufficient way to solve it, not a necessary condition. Whether the exact
IPM adjoint equation has a bounded solution in these spaces remains OPEN.

This note uses only linear functional analysis. It asserts no omitted
edge estimate, derivative-loss bound, or computational certificate.
