# Rational Bernstein range and signed-gradient certificate audit

This independently reviews the mathematical range theorem and its
implementation in N4-285. Reconstruction of a particular candidate is
a separate hypothesis. An incomplete cell cover supplies no whole-plane
bound. All coefficients and rectangle endpoints below are exact reals;
outward interval replacements must contain them.

## 1. Positive rational Bernstein weights

Let a<b and c<d. Use local variables s=(t-a)/(b-a), zeta=(z-c)/(d-c)
in [0,1]. Let P(t,z) have degree at most(n,m) and let D(t) have
degree at most n. Suppose their tensor Bernstein coefficients are
p_ik and d_i, with every d_i>0. Since the Bernstein basis is
nonnegative and sums to one,

    P/D=sum_(i,k) [d_i B_i,n(s) B_k,m(zeta)/D] (p_ik/d_i).

The bracketed weights are nonnegative and sum to one. Thus P/D lies
between the minimum and maximum of the coefficient ratios p_ik/d_i.
An extra independent variable is handled by including its Bernstein
basis in the same weights. No independent lower estimate of D in a
separate division is needed. For vector or matrix values the identity
also holds entrywise with the same nonnegative weights.

In the campaign D is a product of powers of 1+A(1-t), A>=0. Its
linear factors have positive values at both endpoints of every
subinterval of [0,1]. Their degree-one Bernstein coefficients are
those endpoint values. Products use

    B_i,n B_k,m = binom(n,i)binom(m,k)/binom(n+m,i+k) B_(i+k,n+m).

At each resulting index at least one contributing term exists and
all contributing factors are positive. Hence every coefficient is
strictly positive. Degree elevation preserves positivity because it
uses convex combinations. This proves positivity at every common
degree at least deg D. In outward arithmetic every computed d_i must
still have a positive lower endpoint before division is allowed.

## 2. Fractional powers and a correlated Taylor alternative

Let delta>0, w=(1-t)^(delta/2), J>=0, and let the numerator be
sum_(j=0)^J w^j P_j(t,z). On a cell [a,b]x[c,d] contained in
[0,1]x[-1,1], w lies between (1-b)^(delta/2) and
(1-a)^(delta/2). Convert this w polynomial to a Bernstein basis on
that interval, keeping the previously normalized coefficients
p_(j,i,k)/d_i. Section1 with an independent third variable encloses
the full range, and therefore its correlated subcurve. The endpoint
b=1 is allowed. Zero powers use the constant polynomial one.

If b<1 there is another enclosure. Put mu=(a+b)/2, h=(b-a)/2,
q_j=j delta/2. Taylor-expand f_j(t)=(1-t)^q_j through degree six
at mu. Since all 1-t are positive, the derivative remainder gives

    |f_j-T_j|<=E_j,
    E_j=|(q_j)_7|h^7/7!
          *max((1-a)^(q_j-7),(1-b)^(q_j-7)),

where (q)_7 is the falling factorial and E_0=0. The maximum is valid
because that power of 1-t is monotone. Multiply the degree-n Bernstein
coefficients of P_j by the degree-six coefficients of T_j using the
product identity. Sum the resulting numerators, elevate D to degree
n+6, and apply Section1. Add the uniform remainder

    sum_j E_j max_(i,k) |p_(j,i,k)/d_i|.

This is valid because the original rational coefficients bound
sup|P_j/D|. Importantly, D is not replaced by a global unrelated
extremum after the Taylor multiplication. The two constructions give
independent valid enclosures; neither assumes the other is sharper.

## 3. Matrix lower bound and coverage

Assume a valid exact reconstruction gives

    rho_y=sum_j w^j P_j/D,
    rho_x=sin(2theta) sum_j w^j Q_j/D,
    z=cos(2theta), D>0.

For tau>0, the signed-gradient inequality
(sqrt(rho_x^2+rho_y^2)-rho_y)/2<=tau is equivalent to positive
semidefiniteness of

    A=[[tau+rho_y,-rho_x/2],[-rho_x/2,tau]].

Indeed its smaller eigenvalue is tau plus rho_y/2 minus half the
Euclidean gradient magnitude. If the diagonal entries have lower
bounds a0,b0 and the coefficient of sin(2theta) in the off-diagonal
entry has absolute bound q0, then let z0 be the minimum of |z| over
the angular cell and C=q0 sqrt(1-z0^2). Both

    (a0+b0-sqrt((a0-b0)^2+4C^2))/2,
    min(a0,b0)-C

are lower bounds for lambda_min(A). Reducing diagonal entries
subtracts a positive semidefinite diagonal matrix. The explicit
smaller eigenvalue decreases with the off-diagonal magnitude; this
proves the first bound. The operator norm of the off-diagonal matrix
is C, proving the second. Taking their maximum, or the maximum from
the two range constructions above, remains a lower bound. Interval
computation must compare the resulting lower endpoint with zero.

A cell split replaces one rectangle by its two exact halves. A finite
prefix-free tree whose every interior vertex has both children covers
the initial rectangle. A complete cover with nonnegative bounds on
all leaves proves the inequality everywhere in [0,1]x[-1,1]. With
t=r^2/(1+r^2), this includes every finite r>0. Smoothness and the
checked exact origin value supply r=0; t=1 is a compactification
endpoint, not a radial truncation. Pending leaves prevent any such
global conclusion. Sampling points or fixtures cannot replace the
reconstruction and all leaf checks.

## 4. Implementation review and verification scope

The frozen95-line N4 driver uses normalized coefficient matrices in
both constructions, increases the denominator degree by six for the
Taylor numerator, includes its exact tau D term, retains the
sin(2theta) factor for the eigenvalue bound, and calls the tree check
after each split. Its shared helper forms all falling-factorial and
Bernstein product coefficients as in the proof. Its comparisons use
outward Arb endpoints. I read all of these routines as text; no
foreign code is executed.

The independent checker below uses direct rational polynomial
substitution to verify denominator positivity and exact fixture
identities, rather than the peer's matrix transformation. It verifies
all stored fixture point enclosures, reconstructs the finite tree of
the frozen partial cover independently, and checks all saved accepted
lower bounds are nonnegative. This does not recompute the actual
candidate leaf bounds. Those and its exact field reconstruction have
separate review status. The final record must distinguish the proved
range theorem from the still incomplete candidate cover.
