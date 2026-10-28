# A complete geometric bound for the projection profile, all exponents

## Statement

For 0<alpha<1 and z in R^2 define

    g(z)=1/2[|z|^alpha+sgn(z1 z2)(2|z1 z2|/|z|)^alpha], g(0)=0.

The seminorm is the Euclidean homogeneous Holder seminorm. For 0<u<=1,
0<=a,b<=pi/2, put D_minus=(1+u^2-2u cos(a-b))^(1/2), and
D_plus=(1+u^2-2u cos(a+b))^(1/2). Set

    S=(1-u^alpha+|sin(2a)^alpha-u^alpha sin(2b)^alpha|)/(2D_minus^alpha),
    Q=(1-u^alpha+sin(2a)^alpha+u^alpha sin(2b)^alpha)/(2D_plus^alpha).

Zero denominators are treated by the local bounds below. Let S_alpha and
Q_alpha be their suprema over nondegenerate parameters, with u<1 for Q.
Then

    [g]_alpha <= max(1,S_alpha,Q_alpha).

This theorem extends the earlier geometric reduction by retaining the
same-quadrant cases explicitly. A certificate for Q alone at alpha>1/2
is not sufficient. All suprema can be bounded by finite outward interval
coverings with the endpoint rules below.

## Reduction of all pairs

The function g is nonnegative, homogeneous of degree alpha, centrally
symmetric and invariant under coordinate interchange. Its value lies in
[0,|z|^alpha]. Pairs involving zero therefore have quotient at most one.
Pairs in opposite quadrants with the same sign of z1 z2 have distance at
least the larger radius, so their quotient is at most one.

For two points in a single quadrant, normalize the larger radius to one
and write the other radius as u<=1. Reflection gives angles a,b in[0,pi/2].
In a positive quadrant twice the value difference is A+B; in a negative
quadrant it is A-B, where A=1-u^alpha>=0 and
B=sin(2a)^alpha-u^alpha sin(2b)^alpha. Since max(|A+B|,|A-B|)=A+|B|,
the larger of the two quotients is precisely S.

For adjacent quadrants of opposite signs, call the positive point p and
the negative point q. The ordering g(q)-g(p) is at most
(|q|^alpha-|p|^alpha)/2, so its positive part has quotient at most1/2.
Normalize |p|=1. If |q|=u<1, the other ordering gives Q by central
symmetry and coordinate interchange. If |q|=U>=1, the calculation in
../local_projection_profile/PROOF.md gives quotient at most one: write
s=sin(2a),v=sin(2b),R=U^alpha and use

    1-R+s^alpha+Rv^alpha<=s^alpha+v^alpha<=2((s+v)/2)^alpha,
    s+v<=2|p-q|.

These inequalities hold for every alpha<1. Continuity includes the axes.
This proves the reduction without an omitted angular or radial ordering.

## Bounds for the same-quadrant diagonal

On each quadrant d(z)=2|z1 z2|/|z| is2-Lipschitz, as shown by its explicit
gradient in the earlier profile proof. For a same-quadrant pair of radii
1,u and distance D_minus,

    S <= 2^(alpha-1)+(alpha/2)(D_minus/u)^(1-alpha).

Indeed the radial term is at most alpha u^(alpha-1)D_minus by the mean
value theorem; the d^alpha difference is at most(2D_minus)^alpha.
This bound remains valid for all u>0, not only D_minus<=u. In particular
it is less than any fixed K>1 on a sufficiently small neighborhood of
the degenerate diagonal. Away from that diagonal direct interval division
is valid. On 0<u<=epsilon, the range bound gives both S,Q at most
(1-epsilon)^(-alpha).

## Opposite-quadrant upper radial endpoint

Let k=1/(1-alpha), R=u^alpha and M=((1+R^k)/2)^(1/k). The geometric
weighted power-mean argument, valid for every alpha<1, gives

    Q<=min((1-u)^(-alpha), M+(1-R)/(2(1-u)^alpha)).

For 1-epsilon<=u<1 set R0=(1-epsilon)^alpha and
c=alpha(1-epsilon)^(alpha-1). Taylor's theorem on[R0,1] yields

    M-(1+R)/2 <= (k-1)(1-R)^2/(8 R0^max(1,k-1)).

To see this, the maximum second derivative of x^k on that interval is
k(k-1)max(1,R0^(k-2)); the derivative used to invert the power is at
least kR0^(k-1). Combining this with1-R<=c(1-u) gives the endpoint bound

    Q <= 1+(k-1)c^2 epsilon^2/(8R0^max(1,k-1))
           +(c/2)epsilon^(1-alpha).

This is the general-k endpoint rule. The earlier rule with denominator
R0 alone was justified only for k<=2.

## Finite certification

Cover Q on[epsilon,1-epsilon]x[0,pi/2]^2 and S on[epsilon,1]x[0,pi/2]^2.
Every split uses exact rational coordinates in u,a/pi,b/pi. For Q, a+b
at least pi/2 gives the simple bound one. Else direct numerator and
geometric distance bounds, reduced by the two power-mean bounds, are
valid. For S, use the smaller of direct interval division and the local
same-quadrant bound just proved. The distance minimum in a radial interval
is obtained by minimizing1+u^2-2u cos(delta), a convex quadratic; delta
is the smallest absolute angular difference for S and the smallest
angular sum for Q. Any unresolved comparison may use sin(delta)^2 as
a weaker valid lower bound. Exact coverage and both endpoint tests are
required before a numerical K is asserted.

## Monotonicity of the rotated profile

Rotate g so that

    P(X,Y)=1/2[r^alpha+sgn(X^2-Y^2)(|X^2-Y^2|/r)^alpha].

For fixed X, P is nonincreasing in |Y|. For X!=0, write w=Y^2/X^2 and
q=(1-w)/(1+w). Apart from a positive factor, the derivative with respect
to w has sign

    1+sgn(q)|q|^alpha-2(1+q)|q|^(alpha-1).

For q>=0 this is1-q^alpha-2q^(alpha-1)<0. For q<0, putting v=-q gives
1-v^alpha-2(1-v)v^(alpha-1)<0, since concavity implies
1-v^alpha<=alpha(1-v)v^(alpha-1). Continuity covers w=1; at X=0 the
profile is identically zero. Thus the normalized profile can be used in
the positive vertical-variation theorem whenever its seminorm factor has
been certified. This monotonicity itself does not certify that factor.
