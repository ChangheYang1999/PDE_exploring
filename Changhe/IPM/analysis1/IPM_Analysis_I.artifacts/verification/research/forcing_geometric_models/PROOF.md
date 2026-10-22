# Independent geometric Taylor models of the forcing blocks

This argument precedes its checking programs. The application is OPEN
until both independent finite checks and their audit pass. It concerns
only the832 contemporary geometric models retained by topic120.

## Exact statement and dependencies

Use the exact canonical partition t_i of topic119, radial indices
4096<=i<=4108,16 angular parents, and the two by two blocks defined in
topic120. All saved floating numbers below mean their exact dyadic values.
Let H=32hk, W=2wk, a_s=bs H, a_p=-w+4bp wk+2wk and
 T=t_i+a_s, A=(theta_max/16)(q+1/2)+a_p.
On the rectangle0<=s<=H, |phi|<=W define
 Q_p(s,phi)=exp(2(T+s))-2p exp(T+s)cos(A+phi)+p^2.
Here p varies throughout the fixed exact positive source bracket of
topic119. This is the physical squared distance |X-(p,0)|^2 for
X=exp(T+s)(cos(A+phi),sin(A+phi)). It is defined on the entire rectangle,
including any overhang of the original spline parent. No residual or
spline extension is used in this statement.

For each saved qb or uq model let m_ij,r_ij denote its117 coefficient
midpoints and nonnegative radii, and e its nonnegative scalar remainder,
with0<=i<=12,0<=j<=8. The desired finite statement is: for every p there
exist real coefficients c_ij(p) in[m_ij-r_ij,m_ij+r_ij] such that
 |Q_p(s,phi)-sum c_ij(p)s^i phi^j|<=e,
or, for uq, with Q_p-c0 in place of Q_p, on the whole rectangle.
The statement is uniform in p. It permits correlated choices of the
coefficients, as a Taylor-model inclusion must. It does not assert that
arbitrary coefficients in the boxes represent the physical function.

The saved models come from topic120's contemporary replay, not an
attested historical residual run. The exact partition and source bracket,
all model arrays, source hashes and block coordinates must be pinned and
checked. There is no PDE existence, inverse or forcing-norm assertion.

## Tensor Taylor polynomial and analytic remainder

Put E=exp(T). The tensor Taylor polynomial of bidegree(12,8) has exact
coefficients
 a_ij=-2p E cos(A+j*pi/2)/(i!j!)                  if j>=1,
 a_i0=(2^i E^2-2p E cos(A))/i!                 if i>=1,
 a_00=(E cos(A)-p)^2+(E sin(A))^2.
The last formula is the same constant coefficient, expressed without
large cancellation. Equivalently
 a_00=(E-p)^2+4Ep sin^2(A/2).
For uq only the exact constant a_00 is decreased by c0.
These formulas follow by differentiating exp(T+s) and cos(A+phi), or
by multiplying their separate Taylor series. The scalar p^2 contributes
only to the constant coefficient.

Let P_12(s)=sum_(i=0)^12 s^i/i!, and let C_8(phi) be the degree8 Taylor
polynomial of cos(A+phi) about phi=0. For0<=s<=H,
 0<=P_12(s)<=exp(H),
 |exp(s)-P_12(s)|<=exp(H)H^13/13!.
The degree12 remainder for exp(2s) is at most
 exp(2H)(2H)^13/13!.
Taylor's integral theorem applies on either side of phi=0. The ninth
derivative of cosine is minus sine, so, with
 M=max(|A-W|,|A+W|),
 |cos(A+phi)-C_8(phi)|<=M W^9/9!,
since |sin(v)|<=|v| throughout the interval between A and A+phi.
The identity
 exp(s)cos(A+phi)-P_12(s)C_8(phi)
 =[exp(s)-P_12(s)]cos(A+phi)
   +P_12(s)[cos(A+phi)-C_8(phi)]
then bounds the tensor remainder, uniformly for0<p<=p_max, by
 R=E^2 exp(2H)(2H)^13/13!
   +2p_max E exp(H)[H^13/13!+M W^9/9!].          (1)
This is a complete analytic remainder, not a discarded-term heuristic.
No rounding guarantee for a floating exp, sin or integer power is used.
All quantities in(1) will be bounded with directed interval arithmetic.

## Coefficient boxes and the projection argument

Suppose independently directed calculations enclose every exact a_ij(p)
for every p in the bracket in[L_ij,U_ij]. Define the exact nonnegative
rational excess
 d_ij=max(0,(m_ij-r_ij)-L_ij,U_ij-(m_ij+r_ij)).
For each p, choose c_ij(p) to be the projection of a_ij(p) onto the saved
closed interval. It belongs to that interval, and
 |a_ij(p)-c_ij(p)|<=d_ij.
Therefore, by the triangle inequality,
 |sum(a_ij(p)-c_ij(p))s^i phi^j|
 <=sum d_ij H^i W^j=:D.                          (2)
If an independently calculated upper bound R_up of(1) satisfies
 D+R_up<=e,                                     (3)
then the desired model statement follows. Treating p occurrences
independently in interval arithmetic can only enlarge[L,U], and does
not affect the projection argument. The same argument applies after
subtracting c0 from a_00. In particular this directly checks uq; its
soundness is not inferred from a floating add_const operation.

A failed sufficient test(3) leaves this application OPEN. It does not
prove that the candidate is unsound. Candidate radii and remainders
must not be increased to obtain a PASS.

## Independent computations and audit

The first method uses Arb at512bits. It evaluates the derivative formulas
with exact factorials, the Cartesian-square constant, and the displayed
analytic remainder. All coefficient excesses and weighted sums are then
exact rational calculations using the directed ball endpoints.

The second method uses mpmath.iv at160decimal digits. It builds the
exponential coefficient sequences by a_(i+1)=a_i/(i+1) and the doubled
exponential sequence by b_(i+1)=2b_i/(i+1). Angular derivatives use the
independent recurrence c_(j+2)=-c_j/((j+2)(j+1)), starting at cos(A) and
-sin(A). The constant uses the half-angle formula. Coefficients are formed
by these sequences rather than importing the first method's values.
It evaluates(1) with independent directed exponentials and exact rational
powers, then performs its own rational projection tests. Both methods
must pass both models on all832blocks with117coefficients each.

An auditor must compare every required index, array hash and coordinate,
check all saved positive budgets without floating conversion, and verify
all inherited pins. The actual model review and any requested repairs
must be retained. Successful checking proves only the explicit geometric
component for the pinned contemporary arrays. Full composed cutoff models,
physical residual coefficients, Bernstein suprema, historic execution and
physical forcing norms remain separate obligations.
