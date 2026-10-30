# Independent acceptance of the rational Bernstein range theorem

## Statement and dependencies

Let P(t,z) be a real polynomial of separate degrees at most n,m on
[a,b] times [c,d], a<b, c<d. Let D(t) have degree at most n and strictly
positive Bernstein coefficients d_i at degree n on [a,b]. Write p_ik
for P's tensor Bernstein coefficients. Then P/D lies in the convex
hull of the numbers p_ik/d_i. This remains true entrywise for vector
or symmetric-matrix coefficients, with common convex weights, and
with additional independent polynomial variables.

For D(t)=product_l (1+A_l(1-t))^k_l, A_l>=0 and nonnegative integer
k_l, every Bernstein coefficient at every degree n>=sum k_l is
strictly positive on every nondegenerate interval in [0,1]. For
q_j=j delta/2, delta>0, consider sum_(j=0)^J (1-t)^q_j P_j(t,z)/D(t).
Both the independent-power enclosure and the correlated degree-six
Taylor enclosure described below contain it, including the Taylor
remainder. The independent-power enclosure also permits b=1.

If rho_y and rho_x have the exact forms in section3 below, any
complete finite rectangle partition with nonnegative outward lower
bounds for its stated two-by-two matrix proves theta<=tau globally.
An incomplete partition, fixtures or an implementation review alone
establishes no particular candidate's theta.

N4-285 contains the original proof and inspected implementation.
T4-377 supplies an independent complete proof, direct polynomial
transforms, actual-denominator and Taylor checks, and a frozen partial
partition check. This topic checks those bindings and calculations.
Candidate reconstruction N4-284 and the complete017 cover N4-309 are
separate dependencies and are not accepted by this theorem review.

## 1. Rational convex weights and denominator positivity

Put s=(t-a)/(b-a), v=(z-c)/(d-c), and use Bernstein basis B_i,n.
Since the bases are nonnegative and sum to one,

    P/D=sum_(i,k) [d_i B_i,n(s)B_k,m(v)/D] (p_ik/d_i).

The bracketed quantities are nonnegative and sum to one, proving the
claim. Each extra independent variable contributes another
nonnegative partition of unity. This argument also gives a uniform
absolute bound for each P_j/D by the maximum absolute coefficient
ratio, which will control the Taylor error.

A linear factor 1+A(1-t) has positive endpoint Bernstein coefficients
on [a,b] subset [0,1]. Products satisfy

    B_i,n B_j,m=binom(n,i)binom(m,j)/binom(n+m,i+j) B_(i+j,n+m).

For every output index at least one contributing index pair exists;
all contributions to a product of positive factors are positive.
Degree elevation is a convex average of those positive coefficients.
This proves denominator positivity, including at the t=1 endpoint.
Outward computation must still check each denominator lower endpoint
strictly positive before division. Independent interval enclosures of
numerator and denominator coefficients are valid here because the
exact coefficient ratio lies in each interval quotient.

## 2. Fractional powers with a uniform Taylor remainder

On [a,b], w=(1-t)^(delta/2) belongs to
[(1-b)^(delta/2),(1-a)^(delta/2)]. Treating w as an independent
polynomial variable enlarges the set, so section1 bounds the correlated
curve as well. The constant zero power is one, also when b=1.

For b<1 put mu=(a+b)/2 and h=(b-a)/2. Taylor's theorem for
f_j(t)=(1-t)^q_j through degree6 gives

    |f_j(t)-T_j(t)|<=E_j,
    E_j=|(q_j)_7| h^7/7!
        *max((1-a)^(q_j-7),(1-b)^(q_j-7)).

This follows from f_j^(7)(t)=-(q_j)_7(1-t)^(q_j-7) and monotonicity
of the endpoint power; E_0=0. Form the polynomial sum_j T_j P_j,
elevate D to the common degree n+6, and apply section1. The omitted
part has absolute value at most

    sum_j E_j max_(i,k) |p_(j,i,k)/d_i|.

This proves the correlated enclosure with its stated error. Either
valid enclosure may be chosen on a cell. A comparison between their
widths is a numerical efficiency choice, not an extra hypothesis.

## 3. Signed-gradient matrix and a complete partition

Assume an exact continuous reconstruction on the compact rectangle
satisfies rho_y=sum_j w^j P_j/D and
rho_x=sin(2theta_angle)sum_j w^j Q_j/D, z=cos(2theta_angle).
For tau>0 the smaller eigenvalue of

    A=[[tau+rho_y,-rho_x/2],[-rho_x/2,tau]]

is tau-(sqrt(rho_x^2+rho_y^2)-rho_y)/2. Suppose both diagonal entries
have lower bounds a0,b0, and the magnitude of the off-diagonal entry
has upper bound C. Then both

    (a0+b0-sqrt((a0-b0)^2+4C^2))/2,
    min(a0,b0)-C

are lower bounds for lambda_min(A). Subtracting the excess diagonal
entries subtracts a positive semidefinite matrix; the explicit
smaller eigenvalue decreases with the off-diagonal magnitude. The
second bound follows because the off-diagonal matrix has norm C.
On the angular cell use |sin(2theta_angle)|<=sqrt(1-z0^2), where
z0 is the minimum of |z| there. This retains the angular correlation.
All comparisons in outward arithmetic use lower endpoints.

A leaf-free internal node must have its two exact halves along one
axis. By induction on the number of splits, a finite tree with no
missing child, duplicate leaf or leaf ancestor partitions its root.
Therefore a full [0,1] times [-1,1] partition with every leaf bound
nonnegative proves theta<=tau. The substitution t=r^2/(1+r^2) includes
every finite r>0; exact origin continuity gives r=0. Compactification
at t=1 leaves no unexamined finite radial tail. Sampling points cannot
replace the polynomial identities or interval bounds for whole cells.

## 4. Finite acceptance and scope

The checker freezes T4-377's proof, checker, manifest, fixtures and
partial cover as bytes without executing peer code. It binds the
unchanged current N4 sources except the intentionally frozen partial
cover, whose timestamp differs from the later completed cover.
Exact polynomial substitution, degree elevation and reconstruction
independently check the twelve actual positive-denominator transforms.
The finite fixture records and Taylor calculations are checked within
the analytic proof above. Every input is hashed before and after use.
The final result accepts N4-285 through T4-377 only. The complete017
reconstruction, each actual cover leaf, background inequality, inverse
and existence claims require their own evidence.
