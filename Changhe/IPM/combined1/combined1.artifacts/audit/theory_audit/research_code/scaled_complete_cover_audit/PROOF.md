# Independent complete signed-gradient cover for candidate 017

Status: the theorem below is conditional on every recorded leaf passing.
The independent arithmetic is written after this proof. The exact density
and gradient representation was accepted in T4-378; no representation is
inferred from point samples here.

## 1. Exact object and target

Use the immutable raw candidate C1-N1-017-legqs50-quot013, SHA256
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114.
Its canonical density rho has the exact T4-378 representation

    t=r^2/(1+r^2), z=cos(2theta), w=(1-t)^(delta/2),
    D(t)=(1+2499(1-t))^19,
    rho_y=sum_{j=1}^8 w^j P_yj(t,z)/D(t),
    rho_x=sin(2theta) sum_{j=1}^8 w^j P_xj(t,z)/D(t).

Here delta=1-1/c with c=4076476460239181/2251799813685248. Each
polynomial has radial degree at most103 and angular degree at most80.
All40082 nonzero rational coefficients were independently reconstructed
in T4-378. The large exact JSON is reused by hash from that topic.

The target is the whole-plane inequality

    Theta(rho)=sup_X (|grad rho(X)|-rho_y(X))/2 <=2/25.       (1)

If (1) is established, the accepted structured commutator bound of366
implies

    c+1-Theta(rho)-kappa > 2.00123867.                       (2)

These statements are background bounds, not an inverse or existence
proof. Candidate017 already fails the registered small-distance budgets.

## 2. Independent Bernstein subdivision

For n fixed let B_i^n(s)=binom(n,i)s^i(1-s)^(n-i). Convert the full
polynomials once to the tensor Bernstein basis on [0,1] times[-1,1].
The t^k coefficient is binom(i,k)/binom(n,k). For z^k the coefficient
is the exact rational sum

    sum_{l=0}^{min(i,k)} binom(k,l)(-1)^(k-l)2^l
                              binom(i,l)/binom(n,l).

Unlike a fresh power-basis transformation on each leaf, this audit
restricts the resulting coefficients through the prescribed binary tree.
For a half interval, de Casteljau subdivision gives

    left_i=sum_{j=0}^i binom(i,j)2^(-i) parent_j,
    right_i=sum_{j=i}^n binom(n-i,j-i)2^(-(n-i)) parent_j.   (3)

For angular splits use (3) in the angular index. These identities follow
by substituting s=u/2 or s=(1+u)/2 in the Bernstein polynomial and
collecting powers of u and 1-u. Every coefficient matrix operation is
performed with outward Arb balls; the exact rational matrices enter
without floating-point endpoints.

The frozen247 leaves are checked independently to form a full binary
partition: every internal prefix has precisely the children t,T or z,Z,
no leaf is a prefix of another, all leaves are unique, and their exact
rectangles have disjoint interiors and total area2. Thus every finite
point of the physical plane lies in a checked rectangle; the included
t=1 edge also controls the limiting far field.

## 3. Positive denominator and two range enclosures

On a cell [a,b] times[c0,d0], write L=1+2499(1-a)>0 and
R=1+2499(1-b)>0. The Bernstein coefficients of D at degree n>=19 are

    d_i=sum_k binom(19,k)binom(n-19,i-k)/binom(n,i)
                                      L^(19-k)R^k,         (4)

where invalid binomial indices contribute zero. Each coefficient is
strictly positive. The ratios of numerator coefficients to d_i bound
the rational function, because its value is a convex combination with
weights d_i B_i^n B_j^m/D. This is the rational range theorem377.

For an enclosure treating w independently, let wl=(1-b)^(delta/2),
wh=(1-a)^(delta/2). Convert sum_j w^j p_j into degree8 Bernstein
coefficients on [wl,wh], while keeping the already normalized radial
and angular coefficients. The extrema of the resulting tensor enclose
the function even though the allowed w and t are correlated.

For b<1, also retain that correlation with a degree6 Taylor polynomial
T_j(t) of (1-t)^(j delta/2), expanded at mu=(a+b)/2. Its uniform
remainder is bounded by

    E_j=|(j delta/2)_7| ((b-a)/2)^7/7!
                     *max_{v in {1-a,1-b}} v^(j delta/2-7).

The falling factorial is exact. Multiply T_j by P_j using the Bernstein
product identity

    B_i^n B_k^6 = binom(n,i)binom(6,k)/binom(n+6,i+k)
                                                   B_(i+k)^(n+6).

Normalize the summed product by (4) at degree n+6. Add the uniform
error sum_j E_j max|P_j/D|, whose separate rational ranges use degree n.
This proves the correlated enclosure without assuming that independent
interval choices can occur simultaneously. The finite endpoint b=1
uses only the independent-w enclosure.

## 4. Signed bound and acceptance criterion

Suppose one enclosure gives rho_y>=y0 and |sum_j w^j P_xj/D|<=x0.
Let s0=max_{z in[c0,d0]} sqrt(1-z^2), found at zero if the interval
contains zero and at its endpoint nearest zero otherwise. Then
|rho_x|<=s0 x0. The function

    (sqrt(y^2+x^2)-y)/2

is nonincreasing in y and nondecreasing in |x|. Therefore the cell
upper bound is

    theta_cell <=(sqrt(y0^2+(s0 x0)^2)-y0)/2.               (5)

The minimum of the bounds obtained from the two valid enclosures is
also valid. The checker accepts a leaf only when its outward upper
bound from (5) is at most2/25. All247 leaves must pass before (1) is
recorded as confirmed. In particular a nonnegative bound reported by
the other lane is not sufficient for acceptance.

The origin is covered by continuity of the exact representation
(T4-378 checks its angular cancellation). The far field is covered by
t=1 and positive D, with every w^j tending to zero. The sign of
sin(2theta) is immaterial in (5), so the full plane is covered despite
the folded angular coordinate.

## 5. Verification evidence and limits

Freeze the complete source cover and the accepted reconstruction and
Hessian evidence before execution. Record every leaf's exact rectangle,
both independently recomputed signed bounds, positive denominator
coefficient lower bound, input hashes, precision and real elapsed time.
A stopped computation is incomplete; its checked leaves imply no
whole-plane bound until the full partition is accepted.

No spatial quadrature or sampled maximum enters (1). The only numerical
constants in (2) are outward bounds for exact inputs. All domain and
range hypotheses of any later inverse theorem remain separate.
