# Resonant root obstruction for finite polynomial axis data

Result254. Written 2026-10-21 before supporting code. This is a finite auxiliary-axis theorem. Its use in the team report is pending independent review.

## Statement

Assume the hypotheses of result253: C>0, P>1, nonzero real polynomial H with H(0)=0, real polynomial k, y=Ct(1-t^2)^(-P), G=yH(1-t^2), and a differentiable V with V_y=k(1-t^2) and (cy+V)G_y=G on a nonempty open positive-axis interval. The constant c and additive constant of V are arbitrary.

Write H(w)=w^n h(w), n>=1, h(0)!=0, F(t)=Ct h(1-t^2), d=deg F, and let s be the number of distinct complex roots of F. Then necessarily

    P=n+d/2,  F is not squarefree,  s>=5,  d>=7.

Consequently no identity is possible for 1<P<9/2, or for any non-half-integer P>1. At every P>1 the identity is impossible if F is squarefree or has at most three distinct roots. The remaining repeated-root cases at half-integers P>=9/2 are OPEN.

## Dependencies and notation

Result253 supplies the fully proved rational reduction and necessary resonance P=n+d/2. Set

    w=1-t^2, q=2P-1>0, Q=1+qt^2,
    D=wF'+dtF, L_P A=wA'+2PtA.

F is odd, F(+/-1)!=0, and D is a nonzero even polynomial. The reduction proves that B=FQ/D is polynomial and Q divides L_P B. Let J be the monic gcd(F,F'), and S=F/J. Because F has no roots at +/-1, a root of multiplicity m in F has multiplicity exactly m-1 in D. Thus J is also the monic gcd(F,D), and D/J divides Q.

The root at zero of an odd polynomial has odd multiplicity. Nonzero roots occur in opposite pairs with equal multiplicities. It follows that J is even, S is odd, s=deg S is odd, and deg J=d-s is even. Since D/J is even and Q has degree two, there are only two possibilities:

    D=lambda J, or D=lambda JQ,     lambda!=0.          (1)

## No root of F at the imaginary roots of Q

Put a=q^(-1/2)>0. For real z define

    v(z)=F(i z)/(i(1+z^2)^(d/2)).

This is real valued, continuously differentiable on the real axis, and v(0)=0. Direct differentiation gives

    v'(z)=D(i z)/(1+z^2)^(d/2+1).                     (2)

Suppose F(i a)=0, and choose the smallest positive zero z0<=a of F(i z). Such a smallest zero exists because F is a nonzero polynomial. The function v vanishes at both endpoints of [0,z0] and is nonzero in its interior. Rolle's theorem gives z* in (0,z0) with v'(z*)=0 and F(i z*)!=0. By (2), D(i z*)=0. But J divides F, and Q(i z*)=1-q z*^2>0 since z*<a. Either alternative in (1) therefore forces F(i z*)=0, a contradiction.

Thus F(i a)!=0. By real coefficients F(-i a)!=0 as well. J and S also do not vanish at either root alpha of Q.

## Eliminating the constant quotient

If D=lambda J, then B=S Q/lambda. At either root alpha of Q,

    (L_P B)(alpha)=w(alpha) S(alpha) Q'(alpha)/lambda.

Every factor on the right is nonzero: w(alpha)=(q+1)/q, S(alpha)!=0, Q'(alpha)=2q alpha!=0. This contradicts Q dividing L_P B. Hence necessarily D=lambda JQ, and B=S/lambda.

## Eliminating squarefree and low-distinct-root cases

If F is squarefree, J=1 and D=lambda Q. At a root alpha of Q the relation D(alpha)=0 yields w(alpha)F'(alpha)=-d alpha F(alpha). Therefore

    (L_P B)(alpha)=(2P-d) alpha F(alpha)/lambda
                       =2n alpha F(alpha)/lambda !=0.

This is another contradiction. Thus J is nonconstant.

If s=1, the odd polynomial F has just the root zero and is F=A t^d. At resonance D=dA t^(d-1), so D/J is constant. This was already excluded.

If s=3, write S=A t^3+B0 t with A!=0. Since L_P(t)=Q and alpha^2=-1/q,

    (L_P S)(alpha)=-2A(q+1)/q^2 !=0.

Then Q does not divide L_P(S/lambda), a contradiction. These are all positive odd s below five. Therefore s>=5. As J is nonconstant even, deg J>=2, so d=s+deg J>=7. The claimed restrictions follow.

## Scope and open step

This argument uses no sign condition on H and no assumption that all complex roots are real or imaginary. The imaginary-axis Rolle argument is applied only to an explicitly defined real function of z. It does not assume the density itself has an analytic continuation. The theorem concerns the polynomial formulas for an auxiliary axis trace.

The remaining algebraic case is D=lambda JQ with J nonconstant, odd squarefree S=F/J of degree at least five, F(+/-1)!=0, and Q dividing L_P S. No contradiction or example for this remaining case is claimed. In particular there is no full-plane IPM exclusion, no degree-uniform residual bound, and no exclusion of nonpolynomial or infinite-degree limits.

The dependency is research/hydrostatic_axis_zero_order_obstruction/PROOF.md, whose exact proof and 2036+33 supporting checks are recorded in its verification folder. The new checker will verify the derivative identity, parity/gcd reductions on manufactured polynomials, remainders, and representative repeated-root cases. Actual Opus5.5 review is requested separately.
