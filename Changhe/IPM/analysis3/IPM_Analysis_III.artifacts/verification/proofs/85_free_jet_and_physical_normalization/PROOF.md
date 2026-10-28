# Free-jet Fredholm realizations and physical normalization

## Statements and scope

Let Z and Y be the strong spaces of proof 76, let J:Z->R be their
continuous cubic coordinate, and let L=Lred:Z->Y be the actual Fredholm
operator of index zero. The domain Z includes a free J coordinate.
Then

 Z0=ker J is closed of codimension one,
 L0=L restricted to Z0 is Fredholm of index -1.                (1)

In particular an injective L0 cannot be onto Y. If L itself is an
isomorphism, then

 ran L0={f in Y:J[L^(-1)f]=0},                               (2)

a closed hyperplane. The normalization condition J=0 cannot be imposed
on the index-zero theorem without accounting for this change.

There is a separate exact way to obtain the physically normalized
profile from a free-J existence theorem. Suppose an eventual nonlinear
construction produces a classical full-plane solution rho_* with the
canonical velocity, the stated parities, sublinear far growth, and

 rho_*(x,y)=a x^2 y+o(r^3), a=1+j>0,
 rho_*(r,theta)=r^q Theta(theta)+o(r^q), 0<q<1,

where the first expansion has the regularity required to identify its
cubic coefficient. Set lambda=sqrt(a) and

 rho_norm(X)=lambda rho_*(X/lambda).                         (3)

Then rho_norm is an exact solution of the same normalized-speed
stationary equation, has leading cubic coefficient1, the same speed
ell and exponent q, and has far angular profile

 Theta_norm=lambda^(1-q) Theta.                             (4)

Thus a free-J construction followed by (3) satisfies the physical
normalization, provided changing the far amplitude is allowed. It does
not preserve a chart in which Theta itself is fixed. Theorems (1)-(4)
are structural facts. They do not supply the missing nonlinear solution.

## Proof of the Fredholm restriction

The nonzero functional J is continuous by the definition of Z. For
example its scalar component includes functions equal to a nonzero
constant at the negative end and zero at the positive end, so J is
surjective. Hence Z=Z0 direct-sum R e for some e with J(e)=1.

First, L0 has finite kernel as a subspace of ker L. Its range is closed:
let N=ker L. On a fixed closed complement of N, L has a bounded inverse
to its closed range. If J is zero on N, the restriction J along that
inverse is a continuous functional on ran L, and ran L0 is its kernel.
If J is not zero on N, every preimage of any element of ran L can be
adjusted by an element of N to have J=0, so ran L0=ran L. In both cases
the range is closed and has finite codimension.

If J is nonzero on N, dim ker L0=dim N-1 and the range codimension is
unchanged. If J is zero on N, the kernel dimension is unchanged and
the range codimension increases by one: the induced functional on
ran L is nonzero because J is nonzero on Z. Since ind L=0, both cases
give ind L0=-1. Formula (2) is immediate when N=0 and ran L=Y.
This proof applies to the maximal graph norms actually used; it does
not require a classical pointwise trace on all of Z.

## Exact scaling covariance

For a density f and positive lambda, define S_lambda f(X)=lambda
f(X/lambda). Its canonical stream function is

 psi_lambda(X)=lambda^2 psi_f(X/lambda).

Indeed -Delta psi_lambda=partial_x S_lambda f, and its velocity is

 U[S_lambda f](X)=lambda U[f](X/lambda).                     (5)

The canonical full-plane growth and symmetry convention is preserved
under positive dilation; no harmonic velocity is added. Equivalently,
(5) follows by changing variables in the symmetrically truncated
full-plane integral and taking its canonical limit. Differentiating
(5) at0 shows

 c[S_lambda f]=c[f].                                       (6)

For ell[f]=(1+c[f])/3, equations (5)-(6) imply the exact residual
covariance

 F_N(S_lambda f)(X)=lambda F_N(f)(X/lambda).                 (7)

The same formula holds with ell treated as a fixed independent scalar.
Thus (3) preserves stationarity and its speed. Its cubic coefficient is
a lambda^(-2)=1, while its leading far coefficient is multiplied by
lambda^(1-q), proving (4). The origin relation 3ell-c=1 is unchanged.
Parity is preserved by positive dilation.

## Quantitative elementary consequences

If |j|<=epsilon<1, then

 sqrt(1-epsilon)<=lambda<=sqrt(1+epsilon),
 |lambda-1|=|j|/(sqrt(1+j)+1)
            <=|j|/(sqrt(1-epsilon)+1),                    (8)

and

 |log lambda|<=|j|/[2(1-epsilon)].                         (9)

Consequently the relative far-amplitude change obeys

 |lambda^(1-q)-1|
 <= exp((1-q)|j|/[2(1-epsilon)])-1.                        (10)

These are exact bounds. A bound in a chosen global correction norm
requires its dilation continuity and the far-amplitude coordinate;
one cannot measure (3)-rho_bar in a space that excludes any change in
the leading r^q tail. On every fixed compact annulus, ordinary Sobolev
or C^m dilation continuity holds at the regularity of the solution.
No unproved global norm comparison is asserted here.

## Relation to the scaling tangent

For a sufficiently regular f, the tangent at lambda=1 is
K_f=f-X.grad f. Its cubic coefficient is -2a, and its far leading
coefficient is (1-q)r^q Theta. Differentiating (7) at an exact stationary
solution gives L_f K_f=0 in a domain that admits this tail-amplitude
direction. At the approximate background instead,

 L_bar K_bar=F_N(rho_bar)-X.grad F_N(rho_bar),

which need not vanish. This explains why the index-zero fixed-tail
realization with free J does not contradict the formal scaling kernel:
K_bar is not in that realization, because its leading tail is excluded.

After a solution has been constructed, normalization (3) changes the
far amplitude precisely along this excluded direction. Alternatively a
scheme that imposes J=0 from the start must introduce an appropriate
scalar far-amplitude variable or explicitly retain the compatibility
condition in (2). This proof does not assert that any such augmented
linearization is invertible.

Dependencies: proof 76 for the actual index-zero realization and
continuity of J; the exact scaling covariance of the full-plane IPM
system, rederived above. No inverse, residual-smallness or high-order
regularity theorem is assumed except where explicitly stated.
