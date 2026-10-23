# Finite polynomial axis traces cannot solve the auxiliary transport equation for 1<P<=2

Result245, written before supporting code. This proof extends the P=2 argument in result243 by differentiating the forced rational expression for velocity. It uses no formula for a noninteger-power primitive.

## Exact statement

Let C>0 and 1<P<=2 be real. Let H,k be real polynomials with H(0)=0 and H'(0)!=0. For 0<t<1 set

    w=1-t^2,  y=Ct w^(-P),  G(y)=yH(w),
    V(y)=integral_0^y k(w(s))ds.

For any real c, the identity (cy+V)G_y=G cannot hold on any nonempty open interval of positive y. In particular it cannot hold globally with c=P/(P-1), the value compatible with the nonzero far-field amplitude and a sublinear velocity. Requiring k(0)=0, as in the finite hydrostatic trials, only restricts this class further.

The inverse t(y) exists: y_t=C[1+(2P-1)t^2]w^(-P-1)>0, y tends to zero at t=0 and to infinity at t=1. Integrals on finite intervals are ordinary integrals of continuous functions. The theorem does not suppose that these axis traces come from a full density or that V is the full elliptic IPM velocity.

## Proof

Write H(w)=w h(w), with h(0)!=0. Define

    F(t)=C t h(1-t^2),
    D(t)=wF'(t)+2(P-1)tF(t),
    Q(t)=1+(2P-1)t^2.

The polynomial F is nonzero and odd, of positive odd degree m. It obeys F(0)=0 and F(1)=-F(-1)=C h(0)!=0. Thus gcd(F,w)=1, and

    G=F w^(1-P),  G_t=D w^(-P),  G_y=D w/(C Q).

Also D(1)=2(P-1)F(1)!=0 and D(-1)=-2(P-1)F(-1)!=0. In particular D is nonzero and gcd(D,w)=1.

Suppose the transport identity holds on an open interval, and shrink that interval so D is nonzero. It gives

    V=C w^(-P) A(t),  A(t)=F(t)Q(t)/D(t)-c t.          (1)

Here A is a rational function of t, although P need not be rational. Differentiate (1) on the real interval and use V_y=k(w). Dividing by y_t yields the rational identity

    w A'(t)+2P t A(t)=k(w) Q(t).                      (2)

It holds as an identity of rational functions because it holds on a nonempty real open interval.

The rational function A has no finite pole. Indeed a pole t=alpha not equal to ±1 of order l>=1, with leading Laurent coefficient a!=0, gives a pole of order l+1 with leading coefficient -l w(alpha)a on the left of (2). The term 2PtA has order at most l and cannot cancel it. The right side is a polynomial, a contradiction. At ±1 there is no pole of A since its denominator D does not vanish there. A rational function with no finite pole is polynomial. Therefore

    D divides FQ.                                    (3)

First assume m != 2(P-1). The leading coefficient of D is [2(P-1)-m] times that of F, so deg D=m+1. Let s be the number of distinct complex roots of F and let J be the monic gcd of D and F. Since gcd(F,w)=1,

    J=gcd(F',F),  deg J=m-s.

After dividing (3) by J, the coprime polynomials D/J and F/J show that D/J divides Q. Hence

    s+1=deg(D/J)<=2.

Since F(0)=0, s>=1. Thus s=1 and F(t)=a t^m for a!=0. In this case the factor of D after removing its gcd with F is proportional to

    m+[2(P-1)-m]t^2.

It is quadratic in the present case and must be proportional to Q. Comparing its two coefficients gives

    2(P-1)-m=m(2P-1),  or  m=(P-1)/P.

The right side lies strictly between zero and one, contradicting the positive integer m.

It remains to handle m=2(P-1). Since 1<P<=2 and m is a positive odd integer, the only possibility is P=3/2 and m=1. Then F=a t, D=a, Q=1+2t^2 and A=t(1+2t^2-c). Equation (2) becomes

    k(1-t^2)=[(1-c)+(8-2c)t^2]/(1+2t^2).             (4)

A polynomial in t^2 can equal this rational function only if its numerator is a multiple of 1+2t^2. Comparison of coefficients would require

    8-2c=2(1-c),  or 8=2,

which is impossible. Equivalently the numerator is -3 at t^2=-1/2, independently of c, so the pole cannot cancel. This disposes of the exceptional case and completes the proof.

## Hypotheses, dependencies and scope

The proof is standalone polynomial algebra and differentiation; it does not use numerical fitting, a finite grid, a sign condition, a monotonicity assumption, or analyticity of a hypothetical IPM profile. Only the stated finite polynomial ansatz is assumed. Complex roots are used to prove polynomial divisibility, not to postulate complex continuation of an unknown PDE solution. Identity (2) is rational even when P is irrational.

For the standard map r=L sqrt(1-w)/(2w)^P, C=L/2^P. Along the positive y-axis, the finite hydrostatic representation rho=y w sum_j(1-w)^j beta_j(1-2w)cos(2j theta) gives such an H. The complete auxiliary inverse has V_y(0,y)=integral_y^infinity g_xx(0,s) ds=k(w(y)); it is this integrated derivative, not g_xx itself, that is a finite polynomial k(w), as documented by the exact certificates. The hypotheses must still be checked on each certificate, including exact P in (1,2] and nonzero H'(0). Stored exponents must not be silently replaced by their intended values.

This excludes exact members of the finite polynomial axis class, including the c=2 and c=3 finite auxiliary trials when their certificate hypotheses hold. It does not exclude an infinite-degree limit, another representation, or full-plane IPM profiles. No uniform lower residual bound over polynomial degrees follows. In particular it does not turn an optimizer stall into a principal NO verdict, and it does not refute convergence solely because each finite iterate is non-exact. The principal endpoint remains UNRESOLVED.
