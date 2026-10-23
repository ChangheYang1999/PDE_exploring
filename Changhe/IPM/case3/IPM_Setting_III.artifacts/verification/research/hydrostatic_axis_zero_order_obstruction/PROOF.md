# Polynomial axis obstruction with arbitrary positive far-field zero order

Result253. Written2026-10-21 before supporting code. This extends result245 by removing the simple-zero hypothesis. It is an auxiliary-axis theorem, not an IPM nonexistence theorem.

## Statement

Let C>0 and P>1. Let H and k be real polynomials with H nonzero and H(0)=0. For 0<t<1 define

    w=1-t^2,  y=Ct w^(-P),  G(y)=yH(w(t(y))).

Let V be differentiable on a nonempty open interval I contained in (0,infinity), with V_y(y)=k(w(t(y))) there. No normalization of the additive constant of V is imposed. If there is a real c for which

    (cy+V(y))G_y(y)=G(y)                               (1)

holds on I, then, writing H(w)=w^n h(w) with n>=1 and h(0)!=0, the positive odd integer d=deg[t h(1-t^2)] satisfies

    P=n+d/2,   d>=5.                                  (2)

Consequently (1) is impossible for every 1<P<7/2, with no restriction on the finite order n of the zero of H. More generally it is impossible for every P>1 except possibly P=7/2,9/2,11/2,... . The exceptional values are left OPEN; (2) asserts necessity, not existence at those values.

The coordinate is valid because y_t=C[1+(2P-1)t^2]w^(-P-1)>0, with endpoint limits0 and infinity. The inverse t(y) is defined on the whole positive axis. The functions in (1) need only be specified on I except for the explicit global formula for G.

## Rational reduction

Set

    F(t)=C t h(1-t^2),
    D(t)=wF'(t)+2(P-n)tF(t),
    Q(t)=1+(2P-1)t^2.

F is a nonzero odd polynomial of positive odd degree d. Also F(1)=C h(0)!=0 and F(-1)=-C h(0), so F and w are coprime. Direct differentiation gives

    G=F w^(n-P),
    G_t=D w^(n-P-1),
    G_y=D w^n/(C Q).

D is not the zero polynomial. If P!=n this follows from D(1)=2(P-n)F(1)!=0. If P=n it follows from D=wF' and the nonconstancy of F. Shrink I to a nonempty open subinterval on which D is nonzero; this is possible because a nonzero polynomial has only finitely many roots. Equation(1) then implies

    V=Cw^(-P) A(t),  A=FQ/D-ct.

Differentiating and dividing by y_t yields

    L_P A := w A'+2Pt A = k(w)Q.                      (3)

Both sides are rational functions of t; equality on the subinterval makes (3) an identity of rational functions. No analytic continuation assumption on an unknown PDE solution is used.

Every rational solution A of (3) is a polynomial. At a finite pole alpha not equal to ±1, with order ell>=1 and leading coefficient a!=0, wA' has a pole of order ell+1 with coefficient -ell w(alpha)a, while 2PtA has order at most ell. This contradicts the polynomial right side. At alpha=1 the coefficient of (t-1)^(-ell) in L_P A is 2(ell+P)a, which is nonzero. At alpha=-1 it is -2(ell+P)a, also nonzero. Thus there are no finite poles. A rational function without finite poles is a polynomial.

It follows that B=FQ/D=A+ct is a polynomial, hence

    D divides FQ,  and L_P B is divisible by Q,         (4)

because L_P(ct)=cQ. If P=n, D(1)=0 while F(1)Q(1)=2PF(1)!=0, contradicting (4). Hence P!=n. In this case D and w are coprime.

## The generic degree case

Suppose d!=2(P-n). The leading coefficient of D is [2(P-n)-d] times that of F, so deg D=d+1. Let s be the number of distinct complex roots of F and let J be the monic greatest common divisor of F and D. Since F and w are coprime, a root of F of multiplicity m has multiplicity exactly m-1 in D. Indeed, at such a root alpha, w(alpha)!=0 and the derivative term in D has order m-1, while tF has order at least m. Therefore deg J=d-s and J is the monic gcd of F and F'.

After dividing D|FQ by J, the coprimality of D/J and F/J implies D/J divides Q. Hence

    s+1 = deg(D/J) <=2.

F has the root0, so s>=1, forcing s=1 and F=a t^d. Removing its common factor t^(d-1) from F and D, the quadratic factor of D is

    d+[2(P-n)-d]t^2.

It must be proportional to Q, which gives 2(P-n)-d=d(2P-1), or

    d=(P-n)/P=1-n/P<1.

This contradicts the positive integer d. Thus necessarily d=2(P-n).

## Excluding the first two resonant degrees

At a resonant degree d, P=n+d/2. Set q=2P-1=2n+d-1>0 and Q=1+q t^2. Since n>=1 and d is positive odd, the first two possible values are d=1 and d=3. We exclude both using the necessary polynomial condition L_P B divisible by Q from (4). Write alpha for either complex root of Q. Then alpha^2=-1/q and w(alpha)=(q+1)/q.

If d=1, F=a t and D=a. Thus B=tQ and

    (L_P B)(alpha)=w(alpha) alpha Q'(alpha)
                       =-2(q+1)/q !=0.

This contradicts divisibility by Q.

Now let d=3. Write F=a t^3+b t, with a!=0 and a+b!=0 because F(1)!=0. A direct computation gives

    D=b+(3a+2b)t^2,   q=2n+2>=4.

If b=0, then D=3a t^2 and B=tQ/3. As in the degree1 case,

    (L_P B)(alpha)=-2(q+1)/(3q) !=0.

If b!=0, F is squarefree:0 is simple, its two nonzero roots are distinct and simple. Since F and w are coprime, gcd(F,D)=1. Thus (4) requires D to divide Q. D is an even polynomial of degree0 or2, so there are only two cases.

If D is constant, 3a+2b=0 and a/b=-2/3. Then B=t(1-2t^2/3)Q. At alpha,

    (L_P B)(alpha)
      =-2(q+1)/q * (1+2/(3q)) !=0.

If D is quadratic, it equals bQ. Hence a/b=(q-2)/3 and B=t[1+(q-2)t^2/3]. Using 2P=q+1 gives

    (L_P B)(alpha)=-2(q-2)(q+1)/(3q^2) !=0,

since q>=4. These exhaust degree3 and contradict (4) in every case.

Therefore any identity requires a resonant odd degree d>=5, proving (2). Since n>=1, P=n+d/2 is then a half-integer at least7/2. The asserted exclusions follow.

## Hypotheses and limits

H nonzero is essential: H=0 gives G=0 and (1) trivially. H(0)=0 is also essential: for a nonzero constant H, taking V=(1-c)y and k=1-c solves (1), for every admissible P. These counterexamples are axis data, not claimed IPM profiles.

The proof allows arbitrary polynomial k, arbitrary real c, arbitrary additive constant in V, arbitrary finite zero order n, and arbitrary finite degree. It does not give a lower bound for residuals as the degree grows, exclude a nonpolynomial axis trace, or prove that any such axis data arise from a plane density. In particular it cannot exclude an infinite-degree limit and cannot justify an early NO endpoint for Setting III.

## Dependencies and evidence

The proof is standalone polynomial algebra and ordinary differentiation. Result245 motivated it but is not needed as an unproved lemma. The supporting checker independently verifies the reductions, pole coefficients, gcd/divisibility examples, generic-degree relation, and all resonant degree1/3 formulas with symbolic and exact rational arithmetic. Manufactured examples check the necessity of H nonzero and H(0)=0. Verification files are under verification/. An actual Opus5.5 review is requested through the lead lane; external agreement must be checked before any team adoption.
