# The velocity coefficient determined by an integrable angular tail

Status: new T4 result, OPEN independent Opus review. The argument below
is written before the exact specialization checker. It gives a uniform
asymptotic coefficient, not a finite-radius remainder certificate.

## 1. Exact statement and canonical normalization

Let -5<q<-3. Let h be a real C1 S1 function on the plane, where S1
means evenness in x and oddness in y, such that

 H=H_q(h)=max(sup (1+r)^(-q)|h|,
                sup (1+r)^(1-q)|grad h|)<infinity.

Assume a finite real odd sine polynomial b satisfies

 sup_theta |r^(-q)h(r,theta)-b(theta)| -> 0 as r -> infinity.   (1)

The moment M=integral X h(X)dX is absolutely convergent. Use exactly

 U[h](X)=(0,-h(X)/2)+PV integral K(X-Y)h(Y)dY,
 K(Z)=(-z1 z2,(z1^2-z2^2)/2)/(pi |Z|^4),                    (2)

which equals (psi_xy,-psi_xx) for the canonical solution Delta psi=h.
Put p=q+2 and write b=sum_(n positive odd) b_n sin(n theta). Since
-3<p<-1, p^2-n^2 is nonzero for every such integer n. Define

 B(theta)=sum_n b_n sin(n theta)/(p^2-n^2),
 V_q[b](theta)=(partial_xy,-partial_xx)[r^p B(theta)] at r=1.

Then

 sup_theta |r^(-q)(U[h](r e_theta)+DK(r e_theta)M)
                                  -V_q[b](theta)| -> 0.      (3)

Here e_theta=(cos theta,sin theta) is the unit position vector; it is
not the angular tangent. No convergence of grad h is assumed or claimed.

## 2. The compensated kernel passes to the tail limit

For R>=1 put g_R(Z)=R^(-q)h(RZ). On compact annuli g_R converges
uniformly to f(Z)=|Z|^q b(arg Z). Moreover, for Z!=0,

 |g_R(Z)|<=H|Z|^q,  |grad g_R(Z)|<=H|Z|^(q-1).               (4)

These follow directly from the weights and q<0. The bounds also hold
for f, by the elementary limiting Lipschitz argument: integrate the
gradient estimate along short line segments away from zero, pass to
the uniform limit and differentiate the smooth limiting function.

Both g_R and f are centrally odd. Since K is even, symmetrizing the
principal value integral in (2) and adding the full first moment give
at any unit vector e

 R^(-q)(U[h](Re)+DK(Re)M)
   =(0,-g_R(e)/2)+PV integral L_e(Z)g_R(Z)dZ,
 L_e(Z)=[K(e-Z)-K(e+Z)]/2+DK(e)Z.                           (5)

The scaling of the added term is exact: DK has degree -3 and
integral Z g_R(Z)dZ=R^(-q-3)M. Each original g_R moment exists.
Symmetrization uses equal small disks at the two reflected singular
points, which is exactly the reflected version of the original PV.

For |Z|<1/2 the constant and quadratic Taylor terms cancel in the
bracket, and its linear term is -DK(e)Z. Thus

 |L_e(Z)| <= C |Z|^3, |Z|<1/2,                             (6)

with a finite uniform C for |e|=1. Equation (4) makes this integrable
at zero: the radial exponent is q+4>-1. For |Z|>2, the kernel terms
are O(|Z|^-2), while DK(e)Z is O(|Z|). Thus

 |L_e(Z)g_R(Z)| <= C H |Z|^(q+1), |Z|>2,                   (7)

which is integrable at infinity because q+2<-1. The same estimates
hold for f, uniformly in e.

Only Z=e and Z=-e remain. In a disk of radius epsilon<1/4 about e,
subtract g_R(e) from the singular K(e-Z) term. Its constant part has
zero principal value since K has zero angular mean. Equation (4)
gives a uniform local Lipschitz constant, and
integral_(|W|<epsilon) |K(W)| |W| dW=epsilon. The subtracted part
therefore contributes at most C H epsilon. All other terms in that
disk are smooth and contribute O(H epsilon^2). The same argument
applies at -e and to f. Bounds are uniform in R>=1 and |e|=1.

Remove these two disks, an origin disk and an exterior region. On
the remaining set the kernel is uniformly bounded and g_R converges
uniformly to f. The integral difference tends uniformly to zero in e.
The bounds (6), (7) and the singular-disk estimate then let the removed
regions shrink or escape to infinity. The contact term converges by
(1). Consequently (5) has a uniform limit determined only by b:

 W[b](e)=(0,-f(e)/2)+PV integral L_e(Z)f(Z)dZ.               (8)

The integral in (8) is a compensated integral, not the uncompensated
convolution of the singular homogeneous density at the origin.

## 3. Identify the limit by an explicit regular comparison

Choose a smooth radial chi which is zero for r<=1 and one for r>=2.
Let h_b=chi(r) r^q b(theta). It is smooth, S1, has finite H_q and the
same tail. Section 2 gives the same W[b] for h_b and h. It therefore
suffices to compute U[h_b] mode by mode, with finitely many modes.

For f_n(r)=chi(r)r^q b_n, the regular canonical radial potential is

 A_n(r)=-[r^(-n) integral_0^r s^(n+1)f_n(s)ds
                +r^n integral_r^infinity s^(1-n)f_n(s)ds]/(2n).

It solves A_n''+A_n'/r-n^2 A_n/r^2=f_n, is regular at zero, and
has no growing harmonic term at infinity. Its two Hessian components
therefore give the canonical velocity. The integrals and their first
two derivatives exist; for r>=2 their tail portions are exact powers.

For n=1, I_infinity=integral_0^infinity s^2 f_1(s)ds is finite, and

 A_1(r)=-I_infinity/(2r)+b_1 r^p/(p^2-1), r>=2.

The first term has moment m=pi I_infinity and velocity -DK(X)(0,m).
For every odd n>=3, q+n+2>0 and direct integration gives

 A_n(r)=b_n r^p/(p^2-n^2)+C_n r^(-n), r>=2,

for a finite real C_n. Those higher harmonic Hessians are O(r^-5),
which is o(r^q) because q>-5. They have zero first moment. There are
only finitely many modes, so these bounds are uniform in angle. The
Hessian of the homogeneous r^p B term is exactly r^q V_q[b]. This
identifies W[b]=V_q[b] and proves (3), with no differentiated o-term.

## 4. Explicit coefficients and a two-dimensional family bound

For one coefficient b_n, set D_n=4(p^2-n^2). The contribution to V is

 V1=b_n[(p+n)(p+n-2)cos((n-2)theta)
                 -(p-n)(p-n-2)cos((n+2)theta)]/D_n,
 V2=-b_n sin(n theta)/2
       -b_n[(p+n)(p+n-2)sin((n-2)theta)
                 +(p-n)(p-n-2)sin((n+2)theta)]/D_n.           (9)

These follow by applying twice the polar Cartesian derivative rules.
Use cos(-k theta)=cos(k theta) and sin(-k theta)=-sin(k theta).
The central term -b_n sin(n theta)/2 is retained. It is exactly the
local density term, together with the principal-value contribution
in the canonical Hessian decomposition.

For the moment-resolved endpoint theorem, assume all its reference and
stationarity hypotheses, as well as finite odd sine A and P, so

 q=1/c-4, b=(A+tP)/(4c), t=m/pi, c>1.

In this application require -5<q<-3, as above. Define the exact matrix

 S_ij=(1/(2pi)) integral_0^(2pi) (q^2 f_i f_j+f_i' f_j'),
 (f_1,f_2)=(A,P),
 S_ij=(1/2)sum_n(q^2+n^2) f_(i,n)f_(j,n).

Assume A and P are linearly independent, so S is positive definite.
The limiting gradient argument already proved in Section 2 gives

 H_q(h)^2 >= z^T S z/(4c)^2, z=(1,t)^T.                     (10)

Let W(theta) be the two by two matrix with columns V_q[A](theta)
and V_q[P](theta). For any real z and each angle, Cauchy-Schwarz in
the S metric, applied separately to the two rows of W, gives

 |W z|^2 <= (z^T S z) trace(S^(-1) W^T W).

Thus, if a finite exact certificate proves

 T(theta)=[S22|V_q[A]|^2-2S12 V_q[A].V_q[P]
                  +S11|V_q[P]|^2]/det S <= Eprof^2          (11)

for every angle, then (3) and (10) imply

 limsup_(r->infinity) sup_theta
 |r^(-q)(U[h](r e_theta)+DK(r e_theta)M)| <= Eprof H_q(h).   (12)

The same bound holds for all homogeneous coefficients in span(A,P),
not only z=(1,t). This trace bound is sufficient, not necessarily sharp.
It uses the specific tail subspace, not only membership in an H_q ball.
It is therefore outside the domain of the universal lower-E obstruction.

For exact rational q and polynomial inputs, (9) has rational sine and
cosine coefficients. Products in (11) are finite even cosine series,
so T(theta) is a rational polynomial in u=cos(2theta), -1<=u<=1.
An immediate exact upper bound is sum_k |T_k| for the cosine
coefficients T_k, since |cos(k theta)|<=1. Alternatively, a rational
Bernstein upper enclosure on this whole interval proves
(11) if every Bernstein coefficient is at most Eprof^2. Subdivision
is permitted and its union must cover the complete interval. The
certificate checker must bind all input JSON hashes and derive (9),
S and T itself; a stored maximum or sampled angle is not a proof.

For the three fixed rational endpoint inputs 007, 013 and 014, the
specialization checker will test the single common rational target
Eprof=583/1000 using the cosine coefficient sum. Its successful output
would establish (12) with this Eprof, subject to the full hypotheses
above. The target was chosen after a FLOAT diagnostic, which itself
has no certificate status.

## 5. Limits of the conclusion and dependencies

Statement (3) gives no numerical convergence radius. Under just (1),
the convergence may be arbitrarily slow. Equation (12) consequently
cannot be inserted as a finite-radius error bound in CI351. To do so
one needs explicit decay and constants for h-r^q b, or a separate
quantitative compensated-kernel estimate on that remainder, together
with every original endpoint hypothesis. It also does not eliminate
the reference transport term U_R.grad h or supply a stationary H_q
budget. No inverse or existence theorem is asserted.

The proof uses the elementary zero-mean canonical kernel and Green
formula, both derived here. The application uses the accepted
moment-resolved endpoint theorem in ../moment_resolved_tail/PROOF.md
(T4-335, accepted T4-350) and its limiting gradient estimate in
../endpoint_gradient_budget/PROOF.md (T4-375, accepted T4-385).
Those references supply the stationary tail b; Sections 1 to 3 above
need only their own explicitly stated hypotheses.
