# Exact affine saturation of the closed vorticity threshold

## 1. Statement and audited endpoint input

Fix 0<c<2/3 and any real omega. Let t_c and h_c be the regular nonlinear-weight branch of A1782-A1789, whose complete independent proof was reread. Its required endpoint properties are

    0<t_c<3, T(c)=sqrt(t_c), h_c'(t_c)=3/(2t_c),
    H[h_c,1](t_c)=0,
    H[h,1](t)=2th'-3ch-t/2-(2/3)t^2(h')^2.

Put w=T(c), Jx=e_3 cross x and

    G=[[-1/2,-w/2,0],[w/2,-1/2,0],[0,0,1]],
    U(x)=Gx, P(x)=(1+w^2)(x_1^2+x_2^2)/8-x_3^2.

This is a smooth, nonzero full rotating profile with sup|curl U|=T(c), vanishing C59 equality density, and strictly positive cubic Betchov density. It violates both Hb assumptions and spatial decay. It is therefore an exact test of the boundary step, not a counterexample to C59 or the campaign conjecture.

## 2. Full momentum and equality density

The matrices G and J commute and tr G=0. Consequently the full rotating momentum residual is

    (1-c)U+DU[(cI-omega J)x+U]+omega JU+grad P
      =[G+G^2+omega(JG-GJ)]x+grad P.

The horizontal block of G+G^2 is -(1+w^2)I_2/4 and its vertical entry is2, exactly minus the Hessian of P. The residual and divergence vanish. This checks full momentum, not only its curl or pressure equation.

Direct differentiation gives W=curl U=w e_3 and S=(G+G^T)/2=diag(-1/2,-1/2,1). At t=w^2=t_c,

    h_c'(t_c)(W tensor W-t_c I/3)
      =diag(-1/2,-1/2,1)=S.

Thus |S-h_c'(t_c)(W tensor W-t_c I/3)|^2=0. Together with H[h_c,1](t_c)=0, this makes the entire nonnegative equality density in C59 zero, even though W!=0.

## 3. Cubic identity, boundary flux and exact energy

The horizontal eigenvalues of G are -1/2+iw/2 and -1/2-iw/2, and the vertical eigenvalue is1. Therefore

    tr G^3=1+2[-1/8+3w^2/8]=3(1+w^2)/4>0.

Equivalently, the C59 equality formula gives

    (2/9)(3/(2t_c))^3 t_c^3
       +(1/2)(3/(2t_c))t_c^2=3(1+t_c)/4.

For this constant G, define F=G^2 U-(tr G^2)U/2. Its divergence is tr G^3 because DU=G and tr G=0. The ordinary divergence theorem on the full ball gives

    integral_(partial B_R) F.n dS
       =(4pi R^3/3)tr G^3=pi(1+w^2)R^3.

No limit of an unbounded integral is taken. Also

    |U|^2=((1+w^2)/4)(x_1^2+x_2^2)+x_3^2,
    integral_(B_R)|U|^2 dx=2pi(3+w^2)R^5/15,

since each coordinate square integrates to4pi R^5/15. Thus the cubic boundary flux grows like R^3, and the energy grows like R^5. These exact positive constants agree with the submitted proof.

## 4. The class actually tested

U is unbounded. It also fails the second Hb clause: U(Rx)=R U(x), and choosing a nonnegative nonzero smooth compactly supported chi gives the vector test chi U with pairing

    integral U(Rx).chi(x)U(x)dx=R integral chi|U|^2 dx ->infinity

when chi is supported where U!=0. Hence dilation does not tend to zero even in distributions. Both missing hypotheses are explicit.

The exact endpoint input and full equation do not make the inference D=0 implies W=0 valid without a boundary argument. This test proves that logical limitation. It does not show optimality within the bounded or decaying class, does not refute the audited endpoint theorem, and supplies no target counterexample. All calculations are analytic. No numerical or formal computation was needed.
