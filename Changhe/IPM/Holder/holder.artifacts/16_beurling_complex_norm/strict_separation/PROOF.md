# Strict complex-versus-real separation at every Holder exponent

## Statement and dependencies

For each0<a<1, let C_a be the real-input norm of T_xx and let M_a be
the complex-input norm of S=T_xx+i T_xy, on homogeneous Holder space
modulo constants with Euclidean seminorm. Then

    M_a>C_a.                                           (1)

Consequently the conventional Beurling transform has strictly larger
norm on complex inputs than on real inputs, at every such exponent.
The two Beurling norms are2M_a and2C_a. No exact finite-exponent norm
is claimed.

The finite central-cover condition stated below is certified in
verification/central_cover.json and independently replayed in
verification/independent_audit.json. The endpoint arguments are analytic. Dependencies
are the explicit real upper bound in ../../02_upper_bounds/PROOF.md,
and the complex lower bounds in ../glued_witness/PROOF.md and
../exact_angular_modes/PROOF.md.

## A convenient real upper bound

Use the exact angular constants a2(a),a3(a) from the real upper proof.
Set

    b(a)=2^(a+1)/(3pi),
    s(a)=[2a3(a)+(1-a)b(a)]/[2a2(a)],
    U(a)=2a2(a)s(a)^a/[a(1-a)].

The real proof allows the antipodal boundary estimate b(a) alone, so
C_a<=U(a). Before optimizing its radius, that same proof gives

    C_a<=2a2(a)/a+2a3(a)/(1-a)+b(a).                    (2)

Positive-integral Holder interpolation implies

    a2(a)<=1/pi,
    a3(a)<=1/pi,
    a3(a)<=1/4 when a>=3/4.                            (3)

For the first claim use a2(0)=1/pi and a2(1)=2sqrt2/(3pi)<1/pi.
For the second use2sin(t)<=1 on0<=t<=pi/6. For the third, a3 is
decreasing, and log-convexity gives

    a3(3/4)^4<=a3(0)a3(1)^3=81sqrt3/(512pi^4)<1/256.

The last strict inequality follows from sqrt3<2 and pi>3.

For n=2,3 one has Qn(a)<=n^a. Indeed sin(nt)<=min(1,n sin t)
for0<=t<=pi/(2n), and min(1,v)<=v^a for allv>=0.

## The small-exponent interval

Suppose0<a<=1/10. The flower lower bound, keeping only its first
positive term, gives

    a M_a>=2^(-a)/Q2(a)>=4^(-a)>4/5.

Here4^(-a)>=4^(-1/8)=2^(-1/4)>4/5, the last inequality following by
raising to the fourth power. From(2),(3), a/(1-a)<=1/9,
a<=1/10,2^(a+1)<=4 and pi>3,

    a C_a <=2/pi+2/(9pi)+2/(15pi)<106/135<4/5.

Thus the scaled separation margin exceeds2/135 throughout this interval.

## The large-exponent interval

Suppose9/10<=a<1. The cubic lower bound and Q3<=3^a<=3 imply

    (1-a)M_a >=(a+3)/(2Q3)>=(39/10)/6=13/20.

Since a3<=1/4, (1-a)/a<=1/9,1-a<=1/10 and2^(a+1)<=4,
(2) gives

    (1-a)C_a<=1/2+2/(9pi)+2/(15pi)<1/2+16/135<13/20.

This proves strict separation on the second endpoint interval.

## The finite central cover

For1/10<=a<=9/10 use the lower functions

    L_flower(a)=[2^(-a)/a+J_a]/Q2(a),
    L_glued(a)=L_flower(a)+2^a a pi/[Q3(a)sin(pi a)],
    L_cubic(a)=(a+3)/[2(1-a)Q3(a)].

A finite list of rational closed intervals covers[1/10,9/10] without
gaps or interior overlap. On each interval, outward ball arithmetic
must prove at least one of

    a(1-a)(L_glued(a)-U(a))>0,
    a(1-a)(L_cubic(a)-U(a))>0.                          (4)

The certificate stores the exact rational endpoints and lower and
upper bounds for these two quantities, and identifies a positive one.
Since a(1-a)>0, this proves(1) on the central interval.

J_a may be replaced in(4) by any finite positive partial sum of
sum_(k>=0)2^(-a-k-1)/(a+k+1); this only weakens the lower bound.
For a3(a), use the certified positive binomial series for

    I_p(a)=integral_0^(1/2) t^(a+1+2p)/sqrt(1-t^2) dt,
    a3(a)=3*2^a/pi [3 I_0(a)-4 I_1(a)].

AfterNterms, the I_p tail is nonnegative and at most

    (4/3)2^(-a-2-2p-2N)/(a+2+2p+2N).

This follows from binomial coefficients at most one and the geometric
ratio at most1/4. Subtracting the interval for I_1 is outward, not a
sign assumption about truncated expressions. All other expressions
are elementary functions of positive arguments on the central interval.
Thus a successful certificate uses no unbounded numerical quadrature
or floating sample as a continuum assertion.

## Verification status

The42-interval central cover and its independent256-bit replay both
pass. The replay uses a separately derived positive series for a3,
recorded in verification/AUDIT.md. Exact rational endpoints cover
[1/10,9/10] once, and every selected gap is strictly positive. The
finite condition is therefore fulfilled. Failure of a different mesh
would not by itself refute strict separation.
