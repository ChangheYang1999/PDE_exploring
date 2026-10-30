# Independent audit of the optimizer's exact quotient starting states

## Exact statement and scope

Fix c=4076476460239181/2251799813685248, gamma=1/c and delta=1-gamma.
For nonnegative integer j,m,w,n let p_j=(3+gamma-j delta)/2,
t=r^2/(1+r^2), H_m=Re(x+iy)^(2m), and

    G_(j,m,P)=H_m(1+r^2)^(p_j-m) P(t),

where P is t^w or t^w P_n(2t-1), with Legendre P_n(1)=1.
The two frozen exact N1 files re-express candidates007 and013 using
1922 selected generators from each original2982-generator list.
Every coefficient is an exact rational from JSON. The verification
states the raw and canonical hashes for each actual input.

The claims are that each new exact coefficient list represents exactly
the same potential as its corresponding independently accepted original
candidate, and that the selected1922 generators are linearly independent
over R and span the original space. Consequently there are1060 removed
zero-potential directions,1660 selected Legendre generators and262
selected monomials. Density, canonical velocity, residual, origin jets
and tail constraints therefore remain identical as mathematical fields.
This is a coordinate re-expression, not a new numerical reference.
Binary64 coef_float entries, optimizer convergence, condition numbers,
least-squares minima and inverses are outside the statement.

## Independent coefficient check

The three-term Legendre recurrence gives the exact polynomial P_n(2t-1).
Independently compare it with

    sum_(k=0)^n (-1)^(n-k) binom(n,k) binom(n+k,k) t^k.

This identity follows from Rodrigues' formula by differentiating
(t^2-t)^n exactly n times and dividing by n factorial. Multiplying by
t^w gives each generator polynomial. Expand every original and new
coefficient list and sum the coefficient of each(j,m,m+k). Equality
of these finite maps proves equality of the potentials pointwise for
all finite real x,y, because 1+r^2 is positive. The independent canonical
JSON is compared coefficientwise with the new map, and its own source
binding and exact c are checked. No coefficient is dropped by tolerance.

## Independence and preservation of the span

In each fixed(j,m) block, eliminate the largest remaining polynomial
power over Q. Every nonzero pivot polynomial has a different leading
degree, so the pivots are independent over R. Reduction of the new list
must produce no relation and retain all1922 entries. The original list
was already independently proved to have rank1922. The newly retained
generator shapes are compared with their exact original indices in
N1's metadata. They therefore form an independent1922-element subset
of that original span, hence span it.

Angular orthogonality separates m. Different j blocks are independent:
after v=1-t their finite power expansions have exponents whose classes
modulo integers differ by (j-j')delta/2. This is checked to be a
noninteger for all distinct branches in the actual files. If a finite
nonzero combination vanished, divide by its smallest exponent and
let v approach zero. Its nonzero leading coefficient could not vanish,
a contradiction. This also proves that the block rank computation is
the full function-space rank. The rank-nullity theorem gives the removed
dimension2982-1922=1060. No finite numerical singular value enters.

The derivatives defining rho=-partial_y Delta chi and
u=(-chi_xyy,chi_xxy) are linear operations on these smooth functions,
so exact potential equality preserves them. Their nonlinear residual
also agrees, since it is formed by the same products at the same c.
All normalized origin and tail identities already accepted for007 and013
therefore transfer to these re-expressions without another optimization.

## Verification evidence

Freeze both new coefficient files in source before running any code.
Use this lane's independently audited quotient arithmetic from
../quotient_coordinates/code/reduce.py and compare all1922 canonical
coefficients with the previously accepted exact sources. Its rational
elimination and two Legendre identities are independent of N1's rref
implementation. Freeze the N1 implementation for inspection only; never
execute it. Verify each new file's stated original hash and selected
indices. Record every input, code and proof hash, all exact comparisons,
block counts and real times in verification/result.json. The result is
CONFIRMED only when these actual computations finish and all checks pass.
The exact rational coefficient files remain the authority; rounded
convenience fields are not certified by this argument.
