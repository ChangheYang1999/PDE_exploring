# Exclusion of radial zero-vorticity latitude interfaces

Status: CONFIRMED under the exact local hypotheses below, A929-A931. The unrestricted extension remains OPEN, A932.

## 1. Exact theorem and dependencies

Let 0<d<1/2, c=1/(d+2), p=1+d, sigma=1-d, q=2p/d, m=3p+1, gamma=m/d and omega be any real number. Set A=cI-omega J, Jx=(-x2,x1,0), r=|x|, z=x3/r and w=1-z^2. Fix -1<h<1 and a full azimuthal one-sided band r>0,h<z<h+delta<1. Let V be locally C1 and P2 locally C2 up to the boundary away from r=0. Assume V is axisymmetric without swirl, div V=0, and

    V(exp(tA)x)=exp(-(1-c)t)exp(-omega tJ)V(x),
    P2(exp(tA)x)=exp(-2(1-c)t)P2(x),
    -Delta P2=tr((DV)^2),
    dk wedge dS=0, k=(Ax).V, S=P2-|V|^2/2.

Suppose at r=1,z=h that V=lambda e_r, lambda!=0, and curl V=0. There is no C1 scalar p1 on the open band satisfying

    p1(exp(tA)x)=exp(-(3-2c)t)p1(x),
    -Delta p1=2div((DV)Z), Z=DV V+grad P2,
    dk wedge d(p1-2V.grad P2)=0.

The second pressure equation may initially be distributional. Reflection in the equator gives the same result for the other side. Poles are excluded. The theorem requires radial interface velocity, not just its nonzero radial component.

The leading finite-regularity argument is A926, proved independently in the team records. The equatorial exclusion uses A670-A672 and its complete exact coefficient evidence. Actual-profile applications additionally require all the hypotheses of the leading and next tail constructions, including global zero helicity, natural decay rates and an adjacent vortical band. They are not consequences of bare velocity decay. A647-A648 and A653-A655 supply the next scalar for the entire target interval, including c=3/7.

## 2. Finite regularity and analytic equations

Normalize V,P2,p1 by lambda,lambda^2,lambda^3. Every equation is preserved for either sign of lambda. Then on a smaller band

    V=r^-p[R e_r+f e_theta/sqrt(w)], f'=sigma R,
    R(h)=1, R'(h)=0, f(h)=0,
    Q=-D R^q+(R^2+f^2/w)/2, P2=r^-2p Q.

The constant D is real. These equations follow from divergence, curl and the rank equation, since k=c r^-d R has nonzero radial derivative when R>0. Write H=1-Dq, Q0=1/2-D, ell=2p(2p-1). The leading pressure equation is

    (wQ')'+ell Q+T=0,
    T=2(d^2+d+1)R^2+2zff'/w+2z^2f^2/w^2+2pfR'+2pf^2/w.

At H=0 only R in C1 and Q in C2 are needed: R=1+o(z-h), f=sigma(z-h)+o((z-h)^2) imply w0 Q''=sigma^2 and Q0=1/(2p), where w0=1-h^2. The pressure residual is 3d^2+2d+4>0. Hence H!=0. The analytic implicit function theorem first makes R C2 and f C3. The coefficient of f''' in the pressure equation is w[R-DqR^(q-1)]/sigma, nonzero at h. Analytic ODE existence and uniqueness identify the original one-sided germ with an analytic germ. At h=0 uniqueness also gives the parity required in the equatorial theorem. No parity or analyticity was assumed.

The next rank equation now integrates to

    p1=r^-m G, G=C R^gamma-4pRQ-2fQ'

for a real C. Thus p1 is analytic too, and the initially distributional pressure equation becomes pointwise and analytic across h.

## 3. Complete gradient source and finite coefficient recipe

Put j=2p+1. The field Z=r^-j[B e_r+N e_theta/sqrt(w)] has

    B=-pR^2-fR'-f^2/w-2pQ,
    N=-Rf-zf^2/w-wQ'.

In the orthonormal spherical frame, including connection terms,

    M_V=r^(p+1)DV=
      [[-pR,-(wR'+f)/sqrt(w),0],
       [-pf/sqrt(w),R-f'-zf/w,0],
       [0,0,R+zf/w]],
    M_Z=r^(j+1)DZ=
      [[-jB,-(wB'+N)/sqrt(w),0],
       [-jN/sqrt(w),B-N'-zN/w,0],
       [0,0,B+zN/w]].

Differentiating div V=0 shows div((DV)Z)=tr(DV DZ); the leading pressure equation also gives div Z=0. Therefore the full next equation is

    E=(wG')'+m(m-1)G+T1=0,
    T1=2[pjRB+j(wR'+f)N/w+pf(wB'+N)/w
          +(R-f'-zf/w)(B-N'-zN/w)+(R+zf/w)(B+zN/w)].

Set u=z-h and expand R=1+sum_(n>=2) r_n u^n,

    f=sigma[u+sum_(n>=2) r_n u^(n+1)/(n+1)],
    Q=Q0+sum_(n>=2) Q_n u^n.

For n=0,1,2,3 the leading coefficient equation is

    (n+2)(n+1)w0 Q_(n+2)-2h(n+1)^2 Q_(n+1)
       +[ell-n(n+1)]Q_n+T_n=0.

The new r_(n+2) in Q_(n+2) has coefficient H!=0. These four finite rational recurrences determine all jets needed for E0,E1,E2,E3. The same recurrence with G,T1,m(m-1) computes those four next coefficients. This recipe, the two explicit gradient matrices and the binomial rule define the coefficients independently of any imported numerical table.

To check the delicate first derivative, set K0=-ell Q0-2(d^2+d+1). Direct differentiation gives

    Q''=K0/w0,
    Q'''=h[4Q''/w0-2sigma^2/w0^2],
    R''=(Q''-sigma^2/w0)/H,
    R'''=h[4Q''/w0-8sigma^2/w0^2]/H.

At h, B=2p(D-1), B'=N=N''=0, N'=-sigma-w0 Q'' and T1'=4sigma h N'/w0. With K=Cgamma-4pQ0, one obtains G''=KR''-8Q'' and G'''=KR'''-(4p+6sigma)Q'''. Thus

    E'(h)=(4sigma h/w0)[-sigma K/H-3w0Q''+(4-d)sigma].

These expressions and all orders retained in the finite scripts were checked against the full source. For example the fifth-order terms in Q outside H r5 are

    (1-Dq(q-1))r2r3
      +(sigma^2/2)[4h/w0^3+8h^3/w0^4+4h r2/(3w0^2)+r3/(2w0)].

The corresponding coefficient of G is

    C[gamma r5+gamma(gamma-1)r2r3]
      -4p[Q5+r2Q3+r3Q2+r5Q0]
      -10sigma Q5-2sigma r2Q3-sigma r3Q2.

Terms omitted in the cubic source contain vanishing factors at h and cannot contribute through that order. This was checked before executing the exact replay.

## 4. Necessary polynomial equations and exceptional cases

The h=0 case is the confirmed equatorial theorem, so assume 0<|h|<1. Put

    L=2D(d+1)-d=-dH,
    M=D(d+1)(d+2)+d^2+2.

The coefficient of C in E0 is 2(3d+4)M/L. If M=0, direct substitution into E0 before division gives

    -4(17d^4+46d^3+78d^2+70d+32)/(d+2),

strictly negative. Thus L and M are both nonzero. Solving E0=0 gives

    C=-2[22D^2d^4+82D^2d^3+122D^2d^2+86D^2d+24D^2
          -23Dd^4-73Dd^3-92Dd^2-50Dd-8D
          +6d^4+14d^3+14d^2+2d]/[(3d+4)M].

After substitution the remaining necessary equations are

    E1=(4sigma h/w0)(-B1/M),
    B1=(12d^4+54d^3+84d^2+54d+12)D^2
       +(-21d^4-65d^3-43d^2+11d+10)D
       +d^4+6d^3-37d^2-44d-34,
    E2=N2/(w0^2 L^2 M),
    E3=h N3/(-3w0^3 L^2 M).

Here t=h^2 and N2,N3 are the integer polynomials obtained by Section 3 and the displayed substitution for C. Each is linear in t and of degree four in D. Their full exact expressions and integer arrays are retained in the team records and in the team records. No parameter-dependent numerator content is discarded. Every divided factor has been proved nonzero. Hence E=0 implies B1=N2=N3=0.

## 5. Exact elimination and strict sign

Write N_i=a_i t+b_i. A common root implies R_t=a2 b3-a3 b2=0, including when either leading coefficient vanishes. The exact Sylvester determinant in D is

    Res_D(B1,R_t)=-1769472(d-1)^8(d+1)^16(d+2)^4(2d+1)^2
      *(13d^4+17d^3+67d^2+78d+68)^2
      *(17d^4+46d^3+78d^2+70d+32)^2 P18(d).

The integer coefficients of P18 are in the exact certificate. Coefficients 0,1,2,3,4,18 are positive; coefficients 5 through 17 are negative. For each negative coefficient c_k and 0<d<1/2,

    c_k d^k >= c_k d^3/2^(k-3).

The exact remaining cubic coefficient is

    c3-sum_(k=5)^17 (-c_k)/2^(k-3)=719364405827761/16384>0.

All remaining retained terms are positive, so P18(d)>0. The other displayed factors are nonzero in the same interval. Thus the determinant is nonzero, contradicting a common D root of B1 and R_t.

The determinant identity is verified with standard-library integer arithmetic separately from symbolic resultants. The D degrees are fixed at 2 and 8. From the coefficient degrees in d, the Sylvester determinant has degree at most 64. Exact fraction-free determinants at the 65 distinct integers 0,...,64, retaining these fixed D degrees even when leading coefficients vanish, prove identity with the degree-at-most-64 target. The checker also independently multiplies the factors and checks the rational sign bound. This is a finite exact polynomial proof, not sampled-parameter evidence. Its scope is the supplied polynomials; Sections 2-4 supply the separate analytic derivation.

## 6. Scope and verification

No boundary term at spatial infinity, pressure normalization at the origin or characteristic completeness is used in this local theorem. The omega dependence disappears because the stated local field is axisymmetric and swirl-free; omega has not been set to zero. All actual-profile applications still need their separate global pressure construction, decay and helicity hypotheses.

General polar velocity at the interface, zero radial amplitude, swirl, nonaxisymmetric interfaces and poles remain outside this theorem. In particular it does not prove the full decaying rotating-profile conjecture.

The full eight-section submitted proof and all six reconstruction and checking scripts were read. A recorded question and exact pass criterion preceded this agent's sequential replay on one CPU. Sources are hashed in the team records; actual times and exit codes are in the team records. No numerical optimization or formal build is used. The final audit record reports the reconstruction, symbolic expressions comparison, exceptional-case checks and independent integer certificate result.
