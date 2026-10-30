# Whole-plane signed gradient bounds by rational Bernstein weights

## Statement and exact hypotheses

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma.
Let chi be the exact finite potential of a named immutable primary
candidate, and rho=-partial_y Delta chi. Let tau>0 be rational. Assume
the exact reconstruction and all source identities in
../scaled_background_cover/PROOF.md and its hash-bound candidate result.
They provide t=r^2/(1+r^2), z=cos(2theta), w=(1-t)^(delta/2) and exact
polynomials D(t), P_j(t,z), Q_j(t,z), 1<=j<=J, satisfying

 D rho_y = sum_j w^j P_j,
 D rho_x = sin(2theta) sum_j w^j Q_j,
 D(t)=product_R (1+(R^2-1)(1-t))^e_R >=1, 0<=t<=1.

Here every e_R is a nonnegative integer and R in{1,10,25,50,100}; the
full raw coefficient list, positive denominator and exact origin are
retained, with no discarded angular modes or radial cutoff. These
reconstruction hypotheses must be independently reviewed before a new
whole-plane certificate is called certified.

A completed, independently reviewed finite certificate described below
proves

 (sqrt(rho_x^2+rho_y^2)-rho_y)/2 <= tau on all of R2.

This is equivalent to positive semidefiniteness of
 A=[[tau+rho_y,-rho_x/2],[-rho_x/2,tau]].
Its smaller eigenvalue is tau minus the displayed quantity. An incomplete
cover, an unreviewed reconstruction, or a failed cell is OPEN, and proves
no negative assertion about the actual bound. No inverse or existence
result is included.

## Rational Bernstein range theorem

On a rectangle a<=t<=b, c0<=z<=d0, use local coordinates s,q in[0,1].
Let a polynomial P of degree at most(n,m) and positive polynomial D of
degree at most n have Bernstein expansions

 P=sum_(i,k) p_ik B_i,n(s) B_k,m(q),
 D=sum_i d_i B_i,n(s), with every d_i>0.

Then P/D is between min_(i,k) p_ik/d_i and max_(i,k) p_ik/d_i.
Indeed its value is the weighted sum of those ratios with weights
 d_i B_i,n(s) B_k,m(q)/D. These are nonnegative and sum to one. The same
argument holds with an additional independent variable and any tensor
Bernstein polynomial in that variable: retain d_i as the denominator
coefficient for each full tensor index.

For the D above every local Bernstein coefficient is strictly positive
at every degree n>=degree D. Each linear factor has positive endpoint
values and thus positive degree-one Bernstein coefficients. Multiplying
such expansions uses

 B_i,n B_k,m = binom(n,i)binom(m,k)/binom(n+m,i+k) B_(i+k,n+m),

whose factors are positive. Products therefore have positive coefficients.
Elevation to a larger degree also uses convex combinations of adjacent
coefficients, preserving positivity. An outward numerical implementation
must verify the strict positivity of every denominator coefficient; a
failed verification cannot accept a cell.

This theorem avoids replacing D by unrelated minimum and maximum values.
Every polynomial coefficient and rational division is enclosed outward.
The extrema use directed lower and upper endpoints, so coefficient
rounding enlarges the proven range.

## Independent-w enclosure

Build the Bernstein matrices for each numerator of A, including the
constant numerator tau D for both diagonal entries. At each radial
Bernstein index i divide every coefficient by the positive d_i. Since
w lies in[(1-b)^(delta/2),(1-a)^(delta/2)], convert the w polynomial to
the Bernstein basis on that interval and take all tensor coefficient
extrema. The rational range theorem with three independent variables
proves entry enclosures on the rectangle, including the correlated curve
w=(1-t)^(delta/2). This remains valid when b=1.

## Correlated Taylor enclosure

For b<1 put mu=(a+b)/2,H=(b-a)/2. For each j, q_j=j delta/2 and
f_j(t)=(1-t)^q_j, let T_j be its degree-six Taylor polynomial at mu.
Taylor's theorem gives a uniform error

 E_j=|(q_j)_7| H^7/7! *
     max((1-a)^(q_j-7),(1-b)^(q_j-7)).

The falling factorial and sign come from seven differentiations. E_0=0.
The maximum follows from monotonicity of this one real power on the
positive interval. Multiply the numerator P_j Bernstein expansion by
T_j using the displayed exact product identity, and add over j. These
numerators have radial degree at most n+6. Elevate D to that same degree
and apply the rational range theorem to the summed coefficients. The
remainder has absolute value at most sum_j E_j sup|P_j/D|, with each
sup bounded by the original degree-n rational coefficients. This proves
a second enclosure for every matrix entry. The larger of independently
valid lower eigenvalue bounds from the two enclosures is still valid.

## Eigenvalue bound and full-plane coverage

Suppose the diagonal entries have lower bounds A0,B0, and the coefficient
of sin(2theta) in the off-diagonal entry has absolute bound Q0. Let zmin
be zero if[c0,d0] contains zero, and otherwise its least absolute endpoint.
Then the off-diagonal magnitude is at most C0=Q0 sqrt(1-zmin^2).
Subtracting a nonnegative diagonal matrix and increasing the off-diagonal
magnitude can only lower the explicit smaller eigenvalue. Valid lower
bounds are therefore

 (A0+B0-sqrt((A0-B0)^2+4C0^2))/2,
 min(A0,B0)-C0.

Take their maximum with outward arithmetic. Accept a cell only when the
directed lower enclosure is nonnegative. Every split bisects one radial
or angular interval. Store all accepted and pending leaf paths, and
verify their unique, complete, prefix-free binary tree after every step.
Only empty pending leaves and nonnegative bounds on every accepted leaf
prove coverage of[0,1]x[-1,1]. That rectangle covers the whole plane in
(t,z); the exact origin and continuity remove the polar coordinate
singularity, and the endpoint t=1 is compactification, not a finite
radial cutoff. Zero-width physical-coordinate endpoints cause no omitted
finite point. A seeded partition is used only as a partition: none of
its previous candidate bounds is reused.

## Verification and scope

Bind every raw, reconstruction, proof, own-code and seed hash. Do not
alter the prior reconstruction code or proof. Reuse its exact polynomial
file as input. The new checker independently evaluates D coefficients
at local Bernstein indices and checks positivity; the finite cover
contains all candidate data and every cell bound. Manufactured rational
fixtures exercise numerator=denominator, a constant multiple, a degree-one
factor and a signed angular polynomial, at cells near zero and infinity.
These are arithmetic regression checks, not substitutes for the proof.

The original common-denominator cover remains unchanged and incomplete.
Its loose interval bounds do not refute the true signed-gradient margin.
This argument concerns exact rational functions and positive real powers;
it uses no spatial quadrature, numerical optimization or formal build.
