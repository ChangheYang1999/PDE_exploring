# Positive density lower sums for the axis projection witness

## Statement

Use exactly the spaces, operator, witness f, and parameters of
../axis_projection_stieltjes/PROOF.md, including a separately certified
profile factor K. Put X=a+s d, Y=d v with a=1/2, s in{-1,1}, d,v>0,
and restrict X>0. For any disjoint finite logarithmic cells in d,v, a
rigorous nonnegative lower bound on the density below, times the exact
logarithmic cell area, contributes to a lower bound for
(R_1^2 f)(a,0)-(R_1^2 f)(-a,0), after summing, multiplying by four, and
adding one:

    W(d,v)=2a X d v^2/[pi(1+v^2)((X+a)^2+d^2 v^2)] (-partial_Y f).

Only cells on which a positive density lower bound is established are
retained. In particular cells with unresolved minimum or clamp branches
may be discarded. The result is a lower bound, not a quadrature enclosure
of the full witness value.

## Proof

The positive-variation identity in ../monotone_axis/PROOF.md applies.
For a monotone function, its almost-everywhere derivative is the density
of the absolutely continuous part of its positive variation measure.
The remaining singular part is nonnegative. Thus retaining any lower
bound on -partial_Y f can only decrease the positive integral. On a
cell with fixed smooth branch, the derivatives below are ordinary
calculus. The coordinate Jacobian is d^2 v for variables log d,log v.
Multiplying by V gives exactly the prefactor in W.

Let H(v)=P(1,v). Away from v=1,

    -H'(v)=alpha v (1+v^2)^((-alpha-2)/2)
             [(v^2+3)|1-v^2|^(alpha-1)-(1+v^2)^alpha]/2.

It is positive by the monotonicity proof. On a v interval, a lower bound
is obtained by taking the lower endpoints of positive factors and, in
the bracket, using the upper endpoint of |1-v^2| in its negative power
and the upper endpoint of (1+v^2)^alpha in the subtracted term. Clamp
the resulting lower bound to zero. This remains valid if the interval
contains v=1, since the displayed inequality is needed only almost
everywhere. The cusp branch -1/2+P(X-a,Y)/K has density

    d^(alpha-1)(-H'(v))/K.

For a signed-distance branch g=sign*c D^alpha, c=2^(alpha-1), suppose
one particular line segment, ray or axis is uniformly nearest on the
cell. Let R_Y be the vertical residual from its orthogonal projection,
with the projection clipped to the piece's parameter interval. Then

    -partial_Y g=-sign*c*alpha*R_Y*D^(alpha-2).

This formula also holds through a change between an interior and endpoint
projection wherever differentiable; the distance is continuously
differentiable away from the piece. Strictly positive distance and a
uniform component sign suffice. If the axis is nearest, the derivative
is zero. A branch is used only when interval comparisons prove that it
is the minimum defining F, and that F lies strictly between -h and h.
Otherwise assign density zero. This accounts for all branch uncertainty
without assuming it has small measure.

Outward interval evaluation of W, followed by taking its lower endpoint,
proves the cell bound. A complete merge must check exact integer cell
coverage, common parameters, certified K, and source hashes. Omitted
infinite tails and unresolved cells have a favorable sign.
