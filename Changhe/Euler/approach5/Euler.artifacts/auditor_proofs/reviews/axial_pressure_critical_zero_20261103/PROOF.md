# Axial pressure-critical zeros and the full next scalar

## 1. Statement, normalization and scope

Let 2/5<c<1/2, omega!=0, Jx=(-x2,x1,0), A=cI-omega J, X=Ax, a=1-2c, b=2(1-c), eta=a/b and kappa=(b+1)/b. On a neighborhood of a nonzero point p of the rotation axis suppose V,H are smooth, H>0, and write W=curl V, E=|V|^2, P2=H+E/2 and Z=DV V+grad P2. Assume

    div V=0, X.V=0, X.grad H=-bH,
    X cross W=aV, W.grad H=0,
    -Delta P2=tr((DV)^2).

Assume V has exact finite order N>=2 at p and grad H(p) has no transverse component. Then no C1 scalar p1 exists locally with

    X.grad p1=-(b+1)p1,
    -Delta p1=2tr(DV DZ) in distributions,
    W.grad(p1-2V.grad P2)=0.

This is a local obstruction, not a nonexistence theorem for all tails. Finite order excludes the identically zero branch. No prescribed higher Taylor data, analyticity or restriction on the magnitude of nonzero omega is needed.

To normalize p=r0 e3, r0>0, H(p)=h0, replace V,H,P2,p1 by V(r0 x)/sqrt(h0), H(r0 x)/h0, P2(r0 x)/h0 and r0 p1(r0 x)/h0^(3/2). Then W scales by r0/sqrt(h0), Z by r0/h0 and both sides of its scalar Poisson equation by r0^3/h0^(3/2). All equations are preserved. Reflection in x3 commutes with A and transforms curl with the determinant factor, which cancels in the cross-product equation. Thus p=e3, H(p)=1 covers both halves of the axis.

## 2. Potential, scalar reduction and the forced second jet

The cross-product equations imply a grad H cross V=bH W. Hence curl(H^(-eta)V)=0. On a small simply connected ball write V=H^eta grad phi, with phi(p)=0. Since X.V=0, X.grad phi=0. A hypothetical p1 is smooth by local elliptic regularity, because its distributional Laplacian has a smooth right side.

The independently confirmed next-scalar Hessian test A2107-A2111 gives that 3D2H+(eta/H)dH tensor dH is scalar on X(p)-perp. The pressure-critical assumption makes the added gradient tensor vanish on that plane. The Poisson equation gives Delta H(p)=0 since V=DV=0. Differentiating the homogeneity equation along the axis gives H_z=-lambda, H_zz=lambda(lambda+1), H_xz=H_yz=0, where

    lambda=b/c in (2,3), sigma=omega/c,
    eta=(lambda-2)/(2lambda), kappa=(3lambda+2)/(2lambda).

Therefore the transverse quadratic term is A2 rho^2, A2=-lambda(lambda+1)/4.

Set tau=p1-2V.grad P2 and theta=tau/H^kappa. The transport and centralizer reduction of the same Hessian audit gives X.grad theta=0 and vanishing transverse Jacobian of theta and phi. Its constant term is zero: the first nonconstant centralizer term has order at least n=N+1>=3, while Delta(H^kappa)(p)=kappa(kappa-1)lambda^2!=0 and the scalar source vanishes at p. Thus the constant term would violate the Poisson equation.

## 3. Full transverse Taylor data

For z=x3>0 use w=u+iv=z^(-1)exp(i sigma log z)(x1+i x2). Write H=z^(-lambda)h(u,v), phi=f(u,v). Let D=u partial_u+v partial_v, T=-v partial_u+u partial_v and Q=D-sigma T. Cartesian differentiation, before restricting to z=1, gives

    Delta H=Delta_T h+(lambda+Q)(lambda+Q+1)h,
    Delta phi=Delta_T f+Q(Q+1)f.

The leading term of f is harmonic of degree n=N+1. An orientation-preserving transverse rotation puts it in the form P=K Re(w^n)/n with K>0. Define delta=K^2 for n=3 and delta=0 for n>=4. The full low-order expansions are

    h=1+A2 rho^2+h3+B4 rho^4+h4h+O(rho^5),
    B4=lambda(lambda+1)(lambda+2)(lambda+3)/64-delta,
    f=P+f_(n+1)+f_(n+2)+O(rho^(n+3)).

Here h3,h4h and f_(n+1) are arbitrary real homogeneous harmonic polynomials of the indicated degrees. Nothing sets them to zero. The pressure equation gives Delta_T h3=0. Its transverse quadratic equation has radial source (lambda+2)(lambda+3)A2 rho^2 plus 16delta rho^2, fixing B4 and leaving h4h free. In particular its full Cartesian consequence is Delta H=-16delta rho^2+O(rho^3) on z=1.

The scalar divergence equation reads

    Delta_T f+Q(Q+1)f
      +eta h^(-1)[grad_T h.grad_T f+((lambda+Q)h)(Qf)]=0.

Put q=n(1-i sigma) and G=-q(q+1)-eta(2A2 n+lambda q). Its degree-n part is Delta_T f_(n+2)=K Re(G w^n)/n. The harmonic part of f_(n+2) remains free. The terms h3 and f_(n+1) enter this scalar equation only at higher degrees or as the vanishing Laplacian of a harmonic polynomial.

## 4. The real transported coefficient

The centralizer relation implies

    theta=C f+O(rho^(2n)), C real.

Here is the finite-jet justification without analyticity. For a first nonzero homogeneous term R_j of theta after subtracting a constant, zero Jacobian with P implies R_j=C_sector |P|^(j/n) on each sector of P. At a regular nodal ray, noninteger exponents in (0,1) contradict C1 polynomial regularity, and exponents in (1,2) contradict C2 polynomial regularity. Degree n gives a single global real multiple of P by polynomial identity. Subtracting C f preserves the centralizer relation, so repeating this argument excludes every remaining degree n<j<2n. Smooth Taylor remainders and their derivatives have the asserted orders.

The remainder contributes to Delta tau only at order 2n-2>n. The product rule and div(H^eta grad phi)=0 give

    Delta(H^kappa phi)=(2kappa-eta)H^(kappa-1)grad H.grad phi
       +kappa H^(kappa-1)phi Delta H
       +kappa(kappa-1)H^(kappa-2)phi|grad H|^2.

Consequently its degree-n, angular-mode-n coefficient, in the convention K Re(D0 w^n)/n, is

    D0=(2kappa-eta)(2A2 n+lambda q)+kappa(kappa-1)lambda^2.

The tested coefficient of -Delta tau is therefore -C D0.

## 5. Complete source coefficient and free-mode check

Substituting p1=tau+2V.grad P2 into its Poisson equation yields

    -Delta tau=R_lin+R_cub,
    R_lin=2Delta(V.grad H)+2tr(DV D2H),
    R_cub=Delta(V.grad E)+2tr(DV D(DV V))+tr(DV D2E).

With F=H^eta, differentiated incompressibility gives

    Delta V=D2phi grad F+[(Delta F)I-F D2(log F)]grad phi.

Thus the exact linear source equals 2F[D2phi:B+grad phi.C_H], where

    B=3D2H+(eta/H)grad H tensor grad H,
    C_H=(2eta/H)(D2H)grad H
      +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H+grad Delta H.

Only the constant and quadratic transverse entries of B, linear mixed entries, constant vertical entry, linear transverse C_H and constant vertical C_H can contribute to the tested angular mode. Their relevant coefficients are

    d0=-2A2[3(lambda+2)+eta lambda],
    e0=3lambda(lambda+1)+eta lambda^2,
    C_T=2eta[4A2^2+2A2 lambda(lambda+2)]+2eta^2 lambda^2 A2-32delta,
    C_Z=-2eta lambda^2(lambda+1)-eta^2 lambda^3,
    B_TT=6A2 I+12B4 rho^2 I+(24B4+4eta A2^2)xx^T,
    B_Tz=d0 x, B_zz=e0, (C_H)_T=C_T x, (C_H)_z=C_Z.

These are projections to the relevant degrees and modes, not full Taylor identities omitting the free jets. Contraction with the known Laplacian of f_(n+2), Euler's identity x^T D2P x=n(n-1)P, phi_az=partial_a(-Qf) and phi_zz=Q(Q+1)f gives the tested total coefficient

    R0=2[6A2 G+(24B4+4eta A2^2)n(n-1)-2d0 n q
          +e0 q(q+1)+C_T n-C_Z q]+288delta.

The cubic source has minimum degree 3n-6. For n>=4 it is too high. For n=3, only the leading velocity K(u^2-v^2,-2uv) contributes. Its three displayed cubic terms have coefficients 192K^3,48K^3,48K^3 multiplying Re(w^3)/3, respectively. Dividing by K gives 288delta.

All free terms have been checked. A Hessian contraction of real planar harmonics of degrees r,s has angular mode |r-s|, since the trace cancels the sum frequency. Thus h4h paired with P has mode |n-4|, and h3 paired with f_(n+1) has mode n-2. Neither is n. The h3 pairing with P is degree n-1, and multiplying it by F-1 raises it above n because H has no linear transverse term. Its mixed/vertical entries also enter too high. The free harmonic f_(n+2) contracts the constant transverse B by its zero Laplacian. Every other occurrence of f_(n+1) has higher degree. Finally grad Delta H at the required degree is fixed by the full pressure equation, so higher pressure terms cannot create an omitted contribution there. This checks the arbitrary cubic/fourth pressure jets and arbitrary higher potential jets, including n=3.

The two real mode coefficients must therefore satisfy the complex equation -C D0=R0 with C real.

## 6. Exact phase identity and strict sign

Eliminating the real C gives the necessary condition Im(R0 conjugate(D0))=0. Exact expansion gives

    Im(R0 conjugate(D0))=-(n sigma/8)K0,
    K0=lambda F0(lambda,n)
       +lambda n^2 sigma^2(200lambda^2+380lambda+168)
       +64delta(5lambda+6)(3n^2+n-18),
    F0=(50n^2-32n+24)lambda^4+(10n^2-72n+91)lambda^3
       +(-80n^2+18n+116)lambda^2+(-4n^2+66n+68)lambda
       +24n^2+20n+16.

For x=lambda-2>0,y=n-3>=0, its exact expansion is

    F0=x^4(50y^2+268y+378)+x^3(410y^2+2132y+2989)
       +x^2(1180y^2+5898y+8312)+x(1396y^2+6626y+9706)
       +576y^2+2592y+4320.

All coefficients are positive, with constant 4320. The remaining terms of K0 are nonnegative, since delta>=0 and 3n^2+n-18=3y^2+19y+12>0. Hence K0>0. Since sigma!=0 and n>=3, the phase is nonzero. No division by D0, sigma or an unknown Taylor coefficient is used, so no singular exceptional parameter was discarded. This contradicts the necessary complex equation and proves Section 1.

The independent exact checker in the team records subtracts these symbolic polynomials over the rationals, rather than sampling parameters. It returned PASS in 0.39557872992008924 actual seconds on CPU55 at nice19. It verified the zero identity, all 15 positive shifted coefficients, the positive constant and the amplitude polynomial. An initial syntax error stopped before computation and is recorded in the team records. The source's six Cartesian sample checks were read as supporting evidence only; the general argument is the calculation above.

## 7. Application to actual profiles and its limitations

For the actual-profile consequence retain U in C2 on R3, original pressure in C1, the full rotating Euler profile and divergence equations, U.curl U=0 globally, and both natural bounds

    |U(y)|<=C(1+|y|)^(-p0), |DU(y)|<=C(1+|y|)^(-p0-1),
    p0=(1-c)/c.

Assume the leading tail pair is smooth on an open region with k=0,S=H>0. At a velocity zero p in supp curl V on the nonzero rotation axis, the nontrivial branch of A2134-A2139 gives finite order, and the actual-tail law V=DV=0 gives N>=2. The next scalar follows from A647-A648 away from c=3/7 and the averaged A653-A654 at c=3/7, omega!=0. Thus every such supported axial zero must have nonzero transverse pressure gradient. This transfer needs the supported-zero hypothesis; the identically zero local branch does not contradict the local equations.

At omega=0 the phase vanishes and this proof gives no local contradiction. The separate global ordinary-profile theorem A2045-A2047 excludes the stated decaying actual profiles. Axial zeros with nonzero transverse pressure gradient, off-axis zeros, S=0, boundaries of the open k=0 region and unrestricted decaying rotating profiles remain OPEN. Neither natural bounds nor zero helicity is derived from decay.

## 8. Verification record and dependencies

All eight source sections, all three source checker programs, the previously confirmed scalar/Hessian and local-zero reductions used above, and this full eight-section proof were read. The immutable source and experiment outputs are in the team records with hashes. A small exact algebra computation answers only the stated identity question; the finite-jet and free-mode arguments supply its analytic relevance. No formal build, new model client, server, cluster or outside-agent write was used. Existing configured model team collaboration continues through the audit files; actual provider execution is independently unattested.
