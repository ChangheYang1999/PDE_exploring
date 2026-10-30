# A first-moment expansion and the noncompact endpoint condition

Status: new T4 analytic result, OPEN independent Opus review. The proof
below is written before the exact specialization checker. The canonical
kernel is the same one audited in the neighboring forced-tail results.
The new step keeps its dipole coefficient instead of bounding it as an
error. This distinguishes a necessary endpoint condition from a claim of
existence or a statement about arbitrary L2 corrections.

## 1. Exact spaces and moment-resolved velocity estimate

Let -5<q<-3. Let h be a real centrally odd C1 function on R2 with

    H=H_q(h)=max(sup_X (1+|X|)^(-q)|h(X)|,
                 sup_X (1+|X|)^(1-q)|grad h(X)|)<infinity.

The first moment vector M=integral_R2 Y h(Y)dY is absolutely convergent.
Define the complete canonical IPM velocity by its L2 multiplier
(xi_1 xi_2,-xi_1^2)/|xi|^2, equivalently by

    U[h](X)=(0,-h(X)/2)+PV integral K(X-Y)h(Y)dY,
    K(Z)=(-z_1 z_2,(z_1^2-z_2^2)/2)/(pi |Z|^4).

For r=|X|>=2 one has the uniform estimate

    |U[h](X)+DK(X)M| <= E_q H r^q,                              (1)
    E_q=1/2+2^(-q)+2^(3-q)+2^(q+2)/(-q)
              +2^(-q-2)/(-q-3)+2^(2-q)/(q+5).                 (2)

In particular U[h]=O(r^q) at infinity if and only if M=0.

Proof. The bound on h gives h in L2 and absolute convergence of M,
since integral_1^infinity rho^(q+2)drho converges. The principal value
is legitimate because h is C1 and K has zero angular mean. The far
integral is absolutely convergent. The explicit local term is retained.

Split the integral into the disjoint regions B(X,r/2), B(0,r/2), the
remainder in |Y|<=2r, and |Y|>2r. Boundaries have measure zero. The two
open balls are disjoint. The kernel has magnitude 1/(2pi|Z|^2), and
its derivative has operator norm 1/(pi|Z|^3). On B(X,r/2), subtract
h(X) and use |grad h|<=H(r/2)^(q-1). Integrating |K(Z)||Z| gives
(r/2), so the bound is 2^(-q)H r^q. On the remainder region,
|X-Y|>=r/2 and |Y|>=r/2; bounding its area by4pi r^2 gives
2^(3-q)H r^q. In |Y|>2r, |X-Y|>=|Y|/2, giving
2^(q+2)H r^q/(-q). The contact term is at most H r^q/2.

On B(0,r/2), expand K(X-Y) to degree two in Y. Central oddness of h
cancels both the constant and quadratic integrals. The linear integral
is -DK(X) times the moment on this ball. Replace that moment by M;
the error has bound

    (1/(pi r^3)) integral_(|Y|>=r/2)|Y| |h(Y)|dY
       <=2^(-q-2)H r^q/(-q-3).                                (3)

For completeness, identify a vector (v_1,v_2) with v_2+i v_1. In this
identification K(z)=1/(2pi z^2). Its third directional derivative has
magnitude 12|Y|^3/(pi|z|^5). The Taylor segment X-tY remains at radius
at least r/2; division by3! bounds the remainder by
64|Y|^3/(pi r^5). Therefore its integral is at most

    (128H/r^5) integral_0^(r/2) rho^4(1+rho)^q drho
       <=2^(2-q)H r^q/(q+5).                                  (4)

The second inequality uses q<0 and q>-5. Summing these six bounds
proves (1)-(2). No derivative of U[h] is estimated. The complex first
derivative also proves |DK(X)M|=|M|/(pi r^3). Thus M=0 suffices for
the O(r^q) bound. Conversely such a bound and (1), divided by r^-3,
force M=0 since q+3<0. This proves the equivalence.

## 2. S1 dipole and the endpoint forced-tail theorem

Fix c>1, gamma=1/c, delta=1-gamma, and qstar=gamma-4. Let R be a real
C1 S1 reference on R2 with its specified canonical velocity U_R. Put

    F(R)=c X.grad R-R+U_R.grad R.

Assume continuous angular functions A, a C1 angular function Theta,
positive epsilon and eta, finite nonnegative constants V,G,E_F,E_R,
and R0>=2, such that for every r>=R0,

    |U_R|<=V r^gamma, |grad R|<=G r^(gamma-1),
    |F(R)-r^qstar A(theta)|<=E_F r^(qstar-epsilon),
    |grad R-r^(gamma-1)(gamma Theta e_r+Theta' e_theta)|
                         <=E_R r^(gamma-1-eta).                (5)

Let h be real C1 and S1, with H=H_qstar(h)<infinity. Suppose R+h
is stationary at this same c and its velocity is U_R+U[h]. The
stationary equation may be pointwise or distributional with continuous
terms. Define

    m=integral y h(x,y)dxdy,
    P(theta)=gamma cos(2theta)Theta(theta)+sin(2theta)Theta'(theta).

Then uniformly in theta,

    h(r,theta)=r^qstar [A(theta)+(m/pi)P(theta)]/(4c)+e(r,theta), (6)

where, writing q=qstar and E=E_q from (2),

    |e| <= E_F r^(q-epsilon)/(1-c(q-epsilon))
      + |m| E_R r^(q-eta)/(pi(1-c(q-eta)))
      + H(V+E G) r^(q-delta)/(1-c(q-delta))
      + |m| H r^(q-4)/(pi(1-c(q-4)))
      + E H^2 r^(2q-1)/(1-c(2q-1)).                            (7)

All denominators are positive. In particular e=O(r^(q-epsilon_star))
with epsilon_star=min(epsilon,eta,delta,4,1-q)>0.

Proof. S1 means evenness in x and oddness in y, so the first moment
vector is (0,m). Differentiation of the exact kernel gives

    -partial_yK(X)=(cos(3theta),sin(3theta))/(pi r^3).

Thus (1) yields U[h]=m(cos3theta,sin3theta)/(pi r^3)+w,
|w|<=E H r^q. The radial and angular components of the displayed
dipole are m cos2theta/(pi r^3) and m sin2theta/(pi r^3).
Its pairing with the leading gradient in (5) is exactly
(m/pi) r^q P(theta). The error in that pairing is at most
|m|E_R r^(q-eta)/pi. The pairing of w with the full grad R is
at most EHG r^(q-delta). The other transport terms have bounds

    |U_R.grad h|<=VH r^(q-delta),
    |U[h].grad h|<=|m|H r^(q-4)/pi+E H^2 r^(2q-1).

Subtracting the stationary equation gives

    c r partial_r h-h=-F(R)-U_R.grad h-U[h].grad R-U[h].grad h.

Because r^-gamma h tends uniformly to zero, integrate the equation
for partial_r(r^-gamma h) from r to infinity. Each error power p is
less than gamma, and the integral of a bound B r^p is
B r^p/(1-cp). The leading denominator is
1-c qstar=4c. This proves both the sign in (6) and the complete
bound (7). The local part of the velocity was included in (1), so
there is no omitted contact contribution to this argument.

No additional origin normalization is required for this necessary
condition. If a chart imposes one, it can be imposed in addition to
these hypotheses. The proof does not change c or remove a scaling mode.

## 3. Moment compatibility and faster-decay obstructions

Under (5), if the stationary correction in section2 additionally has
H_qprime(h)<infinity for any qprime<qstar, then

    A=-(m/pi)P.                                                (8)

Indeed H_qstar(h)<=H_qprime(h) and r^-qstar h tends uniformly to zero;
apply (6). Thus A not in the real linear span of P excludes every
such faster weighted C1 correction, regardless of its first moment.
This does not exclude general L2 corrections.

More quantitatively define d=dist_(L2(S1))(A,span_R{P}), using ordinary
arc length dtheta on the full circle. When P is zero interpret the
span as {0}. Equation (6) gives

    lim_(r->infinity)||r^-qstar h(r,.)||_(L2(S1))>=d/(4c).        (9)

If the moment m vanishes, the exact limiting angular coefficient is
A/(4c). Equation (1) shows why moment cancellation is the missing
condition for extending the faster velocity estimate below exponent-3.
The limit (9) is an angular tail coefficient bound, not an L2(R2)
distance bound: a fixed integrable tail can start arbitrarily far out.

## 4. Exact angular data and scope of the campaign check

The files data/{007,013,014}_endpoint.json are immutable copies of
T4-305's independently verified exact rational angular maps. They
contain Theta0, F12=A, and P for the campaign c, with A=-4c Theta12.
The checker verifies that definition coefficientwise, recomputes P
from Theta0 using the signed sine product formulas, and recomputes the
exact projection of A onto span{P}. A nonzero two-coordinate determinant
certifies d>0, independently of all rounded norms. Directed Arb arithmetic
then encloses d/(4c) and E_qstar.

These angular pairs have d>0. To apply section2 to a new reference,
one must first prove all of (5), including removal of every residual
sector above qstar while preserving the relevant A and Theta. The
original references and the single- or double-tail repaired references
still have larger residual terms, so they do not yet meet that hypothesis.
The computed angular obstruction is conditional on this missing step;
it is not a new unconditional endpoint exclusion for those references.
T4-305 already gives a separate compact-correction exclusion for the
original references. No compactness assumption is used in sections1-3.

## Dependencies and verification

The canonical L2 kernel and its local term are the campaign's audited
operator. All new estimates and the endpoint implication are proved
above. The numerical specialization depends on the exact angular data
of T4-305, not on an asymptotic truncation being treated as a full-plane
norm. The checker verifies the rational kernel derivative identities,
exact campaign exponents, angular maps, projection orthogonality and
strict rational lower bounds. Source hashes, real completion time and
measured elapsed seconds are recorded in verification/. Independent
Opus review remains necessary before this new analytic result is AUDITED.
