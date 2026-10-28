# A linear remainder for the trace-free sharp norm at small exponent

## Statement and exact coefficient

Use the normalized real operators, homogeneous Holder seminorm and
extension modulo constants in ../../01_setup/PROOF.md. Put x=1/2,
y=-1/2 and

    nu(w)=K_xy(w-x)-K_xy(w-y),
    Z=closure{w outside the poles: nu(w)=0},
    d(w)=dist(w,Z),
    f_a(w)=2^(a-1) sign(nu(w)) d(w)^a,   f_a=0 on Z.

The poles belong to Z. The signed-distance argument gives [f_a]_a<=1.
Define I(a)=integral nu f_a, which is an absolutely convergent positive
integral for every 0<a<1. Then, with
C0=1/2+(log(2)-1)/pi,

    I(a)=2/(pi a)+C0+kappa_C a+o(a) as a -> 0+.              (1)

Here kappa_C is an explicit convergent integral, defined as follows.
Choose a sufficiently small fixed delta>0 so the local descriptions of
Z below apply in the two radius-delta pole disks. Let D_delta be their
complement, and let d0(w) be distance to the two perpendicular own-kernel
zero lines in the pole disk containing w. Set

    J0 = 1-(4/pi)log(delta),
    J1 = integral_(D_delta) |nu| log(d)
         + integral_(two disks) [|nu| log(d)-|own kernel| log(d0)],
    ell = log(delta)+log(2)/2-1/2,
    kappa_C = (ell^2+1/4)/pi+(log(2)/2)J0+J1/2.             (2)

The bracketed local integrand is absolutely integrable. Changing delta
within the admissible range does not change kappa_C. In particular,
C_a>=I(a). Combining (1) with the linear upper theorem in
../../08_improved_upper_bounds/explicit_second_term/linear_remainder/PROOF.md
gives

    C_a=2/(pi a)+C0+O(a).                                  (3)

Equation (3) is conditional only on that separately stated upper theorem,
whose independent lead cross-read is pending. Formula (1) and the lower
consequence are proved here independently of its transport argument.
No numerical value of kappa_C and no existence of a third-term limit for
the sharp norm are asserted.

## Zero-set geometry

The explicit diagonal calculation in ../diagonal/PROOF.md gives

    Z = {Y=0} union {X=b(Y)} union {X=-b(Y)},
    b(Y)^2 = [1/4-Y^2+2sqrt(Y^4+Y^2/4+1/16)]/3.

The function b is smooth and positive, b(0)=1/2, and
b(Y)=1/2+O(Y^4), b'(Y)=O(Y^3) near zero. Thus near either pole, Z
consists of the horizontal line and a smooth curve with fourth-order
contact with the vertical line through that pole. The other graph is
separated by a positive distance. Near a pole, at radius r,

    d/r and d0/r have their zeros at four angles separated uniformly,
    with corresponding angular roots displaced by O(r^3).             (4)

In fixed neighborhoods of the four roots, each distance divided by r is
comparable to distance in angle from that root, with uniform constants.
Away from those neighborhoods it is bounded below. These statements
follow directly for the horizontal line. For the curved vertical line,
distance to its graph lies between |X-b(Y)|/sqrt(1+L_r^2) and |X-b(Y)|,
where L_r=O(r^3) bounds the slope in a radius-2r neighborhood. Nearest
points lie in that neighborhood because the pole is in Z. On the
circle, the derivative of [X-b(Y)]/r at each vertical crossing is
bounded away from zero. The implicit function theorem gives (4).

At infinity, b(Y)/|Y| -> 1/sqrt(3), and the differentiated explicit
formula gives b'(Y) -> sign(Y)/sqrt(3). Hence the same angular
transversality holds uniformly for all sufficiently large circles:
there are six separated angular crossings, approaching the three
straight zero lines of the leading cubic harmonic. In particular,

    sup_(r>=R0) integral_0^(2pi) |log(d(r e^(i theta))/r)| dtheta < infinity.
                                                                    (5)

To justify (5), partition each circle into uniformly sized neighborhoods
of those crossings and their complement. In each neighborhood the
normalized distance is comparable, above and below, to angular distance
from its crossing, by the graph slope bounds. The integral of
|log|theta-theta0|| on a fixed interval is finite and independent of
theta0. On the complement the normalized distance has uniform positive
lower and finite upper bounds.

## A weighted logarithmic comparison at each pole

Let q(theta) be the absolute angular own-kernel factor, |sin(2theta)|
after rotating coordinates. For sufficiently small r,

    integral_0^(2pi) q(theta) |log(d/d0)| dtheta <= C r^3.   (6)

Here and below C denotes a finite constant in the domination proof,
not an unspecified constant in a claimed numerical operator bound.
We give the local justification of (6). The horizontal distance is
unchanged. Near a vertical zero, put u=cos(theta) (with the appropriate
sign), so q is bounded by C|u| and angular measure is comparable to du.
The normalized graph equation is u-eta_r(u), where
|eta_r|<=C r^3 and |eta_r'|<=C r^3. It has a unique root u_r=O(r^3), and

    |u-eta_r(u)|=|u-u_r|[1+O(r^3)].

The graph-distance slope factor contributes O(r^6) to its logarithm.
On |u|>=2C r^3, the logarithm of the ratio to |u| is at most
C r^3/|u|+C r^3. Its integral against |u| is O(r^3). On
|u|<=2C r^3, rescale u=r^3 v and u_r=r^3 v_r. The integral against
|u| of |log(|u-u_r|/|u|)| is O(r^6), uniformly for v_r in a bounded
interval, because the two logarithmic singularities have uniformly
bounded integrals there. Taking the minimum with distance to the
horizontal line cannot increase the logarithmic change: the map
s -> min(log(s),log(h)) is 1-Lipschitz. The other root neighborhoods
are treated identically. This proves (6).

Also | |nu|-|own kernel| | is bounded on each pole disk by the smooth
cross kernel. The local distance has an integrable logarithm by the
same graph-coordinate argument, including the intersection at the
pole. Decompose the bracket in J1 as

    (|nu|-|own kernel|)log(d)+|own kernel|log(d/d0).

The first term is integrable; (6) proves absolute integrability of the
second, since its radial majorant is C r^2 dr.

## Differentiating the regularized positive integral

For a fixed small delta define

    J(a)=integral_(D_delta) |nu| d^a
          +integral_(two disks) [|nu|d^a-|own kernel|d0^a].

The exact own-kernel angular integral gives

    I(a)=2a2(a)delta^a/a+2^(a-1)J(a).                       (7)

The finite-part identity N(pi/4)=1/2 from the diagonal proof gives
J(0)=J0. We now prove J'(0+)=J1 by dominated convergence.

On a pole disk take delta so small that d,d0<1. For positive numbers
u,v<1 and 0<a<=1/2,

    |(u^a-v^a)/a| = |integral_v^u t^(a-1)dt|
                    <= |log(u/v)|.                       (8)

Split the local difference as
(|nu|-|own kernel|)d^a+|own kernel|(d^a-d0^a).
For the first part, |(d^a-1)/a|<=|log(d)|. For the second, use (8) and
(6). These are exactly the integrable majorants established above, so
the local derivative is the local term in J1.

On any compact set outside the pole disks, the zero curves are smooth
and their logarithmic distance is locally integrable. At infinity,
|nu|<=C r^-3 and d<=2r. For d<1 use |(d^a-1)/a|<=|log(d)|. For d>=1
use |(d^a-1)/a|<=d^(1/2)log(d). Equation (5) bounds the angular averages
of the negative logarithm; the positive logarithm is O(log(r)). Thus a
radial majorant is C r^(-3/2)(1+log(r))dr, which is integrable. This proves
the exterior derivative and hence J'(0+)=J1.

Finally,

    2a2(a)delta^a/a
       =2/(pi a)+2ell/pi+[(ell^2+1/4)/pi]a+O(a^2).

Insert J(a)=J0+aJ1+o(a) and 2^(a-1)=(1+a log(2)+O(a^2))/2 into (7).
The constant term is C0, and the linear coefficient is exactly (2).
This proves (1). Since the left side of (7) is independent of delta,
so is its derivative coefficient kappa_C. Compact smooth approximation
from the setup preserves the lower operator bound.
