# Axial positive-pressure zeros with arbitrary transverse pressure gradient

## 1. Exact local statements

Fix 2/5<c<1/2 and omega!=0. Let Jx=(-x2,x1,0), A=cI-omega J, X=Ax, a=1-2c, b=2(1-c), eta=a/b and kappa=(b+1)/b. Near a nonzero point p on the rotation axis let V,H be smooth, H>0, and put W=curl V, E=|V|^2, P2=H+E/2, Z=DV V+grad P2. Assume

    div V=0, X.V=0, X.grad H=-bH,
    X cross W=aV, W.grad H=0,
    -Delta P2=tr((DV)^2).

Suppose V vanishes to exact finite order N>=2 at p. If a C1 function p1 satisfies

    X.grad p1=-(b+1)p1,
    -Delta p1=2tr(DV DZ) in distributions,
    W.grad(p1-2V.grad P2)=0,

then grad_T H(p)=0, where T is the plane perpendicular to the rotation axis. This is the new local theorem of LIT291.

Combined with the independently confirmed pressure-critical theorem A2180-A2185, the stronger conclusion is that no such p1 exists, with no restriction on grad_T H(p). Both statements concern this local smooth finite-order axial class only. The source is pinned in the team records. No analyticity or smallness of rotation is assumed.

## 2. Normalization, potential and forced pressure jets

Write p=r0 e3, r0>0, H(p)=h0. Replace V,H,P2,p1 by V(r0 x)/sqrt(h0), H(r0 x)/h0, P2(r0 x)/h0 and r0 p1(r0 x)/h0^(3/2). Curl scales by r0/sqrt(h0), Z by r0/h0 and both sides of the next Poisson equation by r0^3/h0^(3/2). Thus all equations persist. Reflection in x3=0 commutes with J and preserves the cross-product equation because the two orientation factors cancel. It covers the negative half-axis. Hence p=e3,H(p)=1 is sufficient.

If grad_T H is nonzero, rotate about the axis to put grad_T H=(g,0), g>0. This rotation is used only once: the phase of the leading harmonic potential remains arbitrary. Set lambda=b/c in (2,3), sigma=omega/c, n=N+1>=3. Then eta=(lambda-2)/(2lambda) and kappa=(3lambda+2)/(2lambda).

The cross-product equations give a grad H cross V=bH W. Consequently curl(H^(-eta)V)=0; on a small ball V=H^eta grad phi with phi(p)=0 and X.grad phi=0. The distributional next Poisson equation makes p1 smooth by local elliptic regularity. The confirmed Hessian test A2107-A2111 implies that

    B=3D2H+(eta/H)grad H tensor grad H

is scalar on the transverse plane at p. Because V=DV=0, the leading Poisson equation gives Delta H(p)=0. Homogeneity and its derivatives give

    H_z=-lambda, H_zz=lambda(lambda+1),
    H_xz=-(lambda+1)g, H_yz=-sigma g.

The second mixed sign follows directly by differentiating X.grad H=-bH in y: the derivative of X in y is (omega,c,0), so c H_yz+omega g=0. Therefore, with t=-lambda(lambda+1)/2+eta g^2/6,

    D2_T H=diag(t-eta g^2/3,t), B_TT=beta I,
    beta=3t=-3lambda(lambda+1)/2+eta g^2/2.

These jets are consequences of the equations.

## 3. All needed transverse jets and the real scalar coefficient

For z=x3>0 use w=u+iv=z^(-1)exp(i sigma log z)(x1+i x2). Write H=z^(-lambda)h(u,v), phi=f(u,v). Put D=u partial_u+v partial_v, T=-v partial_u+u partial_v, Q=D-sigma T. Cartesian differentiation followed by restriction to z=1 gives

    Delta H=Delta_T h+(lambda+Q)(lambda+Q+1)h,
    Delta phi=Delta_T f+Q(Q+1)f.

The leading homogeneous term of f is harmonic:

    P=Re(K w^n)/n, K in C minus {0}.

The full required jets are

    h=1+gu+h2+h3+O(rho^4), rho^2=u^2+v^2,
    h2=((t-eta g^2/3)u^2+t v^2)/2,
    f=P+f_(n+1)+O(rho^(n+2)).

The pressure equation gives Delta H=O(rho^(2n-4)), so its constant and linear Taylor terms vanish. Hence

    h3=(g rho^2/8)Re(A3 w)+h3h,
    A3=-(lambda+1-i sigma)(lambda+2-i sigma),
    Delta_T f_(n+1)=-eta g Re(K w^(n-1)),

where h3h and the free part of f_(n+1) are arbitrary harmonic polynomials. In particular grad Delta H(p)=0.

Set tau=p1-2V.grad P2 and theta=tau/H^kappa. The confirmed scalar reduction gives X.grad theta=0 and Jac(f,theta)=0. Its constant is zero: the source vanishes at p, whereas Delta(H^kappa)(p)=kappa(kappa-1)(lambda^2+g^2)>0, and all possible nonconstant centralizer terms have order at least n. For completeness, a first homogeneous centralizer term R_j obeys Jac(P,R_j)=0. On each regular sector of P, homogeneity implies R_j=C_sector |P|^(j/n). For 0<j<n a nonzero coefficient violates C1 regularity across a regular nodal ray. Degree n is a global real multiple C P, by polynomial identity. After subtracting C f, the same argument excludes n<j<2n, because the transverse second derivative of |P|^(j/n) is unbounded. Thus

    theta=C f+O(rho^(2n)), C real.

Smooth Taylor remainders can be differentiated at the stated orders. The remainder in Delta tau has order at least 2n-2>n-1. Incompressibility gives the exact product identity

    Delta(H^kappa phi)=(2kappa-eta)H^(kappa-1)grad H.grad phi
       +kappa H^(kappa-1)phi Delta H
       +kappa(kappa-1)H^(kappa-2)phi|grad H|^2.

Its degree n-1 term yields

    [-Delta tau]_(n-1)=-C(2kappa-eta)g Re(K w^(n-1)).

This coefficient is real relative to the same unrestricted phase K.

## 4. Source extraction with all free jets

The next Poisson equation is

    -Delta tau=R_lin+R_cub,
    R_lin=2Delta(V.grad H)+2tr(DV D2H),
    R_cub=Delta(V.grad E)+2tr(DV D(DV V))+tr(DV D2E).

The cubic terms start at degree 3n-6, strictly larger than n-1 for n>=3. Let F=H^eta. Differentiated divergence gives

    Delta V=D2phi grad F+[Delta F I-F D2(log F)]grad phi.

Using this in R_lin gives

    R_lin=2F[D2phi:B+grad phi.C_H],
    C_H=(2eta/H)(D2H)grad H
       +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H
       +grad Delta H.

At p define

    u0=-3(lambda+1)-eta lambda, v0=-3sigma,
    c0=eta lambda(lambda+1)+(2/3)eta^2 g^2+eta^2 lambda^2,
    d0=2eta lambda sigma, q=n(1-i sigma).

The forced jets imply B_Tz=g(u0,v0) and (C_H)_T=g(c0,d0). Thus the degree n-1, mode n-1 part of the source is g Re(K R0 w^(n-1)), where

    R0=2[-beta eta+(3/2)(n-1)conjugate(A3)
         +eta(n-1)(-lambda(lambda+1)-g^2/2)
         -2(u0+i v0)q+c0+i d0].

Each term can be checked independently. Constant B_TT contracts the forced Laplacian of f_(n+1), giving -beta eta. For the particular cubic, use

    h3_part=g(A3 w^2 conjugate(w)
                    +conjugate(A3)w conjugate(w)^2)/16.

Its second conjugate-w derivative is g conjugate(A3)w/8. Contracting it with the holomorphic second derivative of P and its conjugate gives (3/2)(n-1)conjugate(A3). The conjugation is therefore essential.

Write D2_T H=diag(s,t), s+t=-lambda(lambda+1). The linear part of the gradient tensor in B is

    eta[g e1 tensor (D2_T H)x+(D2_T H)x tensor g e1
                                      -g^3 u e1 tensor e1].

Contract its holomorphic component with [[1,i],[i,-1]]. The coefficient of w is eta g(s+t-g^2/2), giving the third term after multiplication by n-1. Finally phi_z=-Qf; both mixed entries in the Hessian contraction are present, giving -2(u0+i v0)q. The transverse C_H term gives c0+i d0.

The free harmonic cubic pressure contributes only angular mode |n-3|, which is distinct from n-1 for every n>=3. The free harmonic f_(n+1) has zero trace against beta I. Vertical-vertical contractions, higher pressure and potential jets, and higher C_H terms begin above degree n-1. Multiplication by the linear term of F creates no contribution from degree n-2, since that earlier coefficient is beta Delta_T P=0 identically. These checks exhaust the source without prescribing free jets.

## 5. Strict phase contradiction and independent algebra check

Equality with the scalar coefficient forces

    -C(2kappa-eta)=R0, C real.

Its right imaginary part is

    Im R0=-sigma[3(n-1)(2lambda+3)
                          +4n lambda(3+eta)-4eta lambda]
          =-sigma[(20n-8)lambda+5n-5].

The bracket is strictly positive for lambda>2,n>=3. Since sigma!=0, the imaginary part cannot vanish. Multiplication by K does not remove this contradiction: the two real harmonic coefficients uniquely determine a complex coefficient, and K is nonzero. This proves grad_T H(p)=0 under the stated local hypotheses.

The independent symbolic checker subtracts the displayed imaginary identity and separately differentiates the cubic pressure and the anisotropic tensor coefficient. Every remainder is exactly zero, with actual elapsed time 0.49113901890814304 seconds. It ran on CPU55 with nice19 and OMP_NUM_THREADS=1. This supports the displayed symbolic proof; no sample inequality is used. The source's six Cartesian tests at one parameter pair and both phases were inspected, including the extra potential jet needed to differentiate incompressibility. They are supplemental checks only; their 134.03127860324457-second source runtime is not our runtime.

## 6. Combined local exclusion and actual-profile transfer

The preceding result forces zero transverse pressure gradient. A2180-A2185 excludes that remaining case under the identical local assumptions for every nonzero omega. Hence there is no finite-order N>=2 axial velocity zero with positive H and a next scalar, irrespective of transverse pressure gradient.

For an actual profile retain U in C2(R3), P in C1(R3), the full Euler profile system, U.curl U=0 everywhere and both natural bounds

    |U(y)|<=C(1+|y|)^(-p0),
    |DU(y)|<=C(1+|y|)^(-p0-1), p0=(1-c)/c.

Assume its leading pair V,S is smooth near a point p on the nonzero rotation axis, p in supp curl V, V(p)=0, with k=(Ax).V=0 and S>0 on a neighborhood. Supportedness rules out the identically zero local branch. A2134-A2140 gives a finite vanishing order; the actual-tail pointwise law gives DV(p)=0 and hence N>=2. The next scalar exists by A647-A648 when c!=3/7 and the confirmed averaged construction A653-A654 at c=3/7, omega!=0. The combined local theorem contradicts this supported zero. At omega=0 the separate ordinary-profile Liouville theorem already excludes the full decaying profile.

This transfer does not derive smoothness of the leading pair, helicity-freeness or either natural bound from velocity decay. It does not exclude off-axis zeros, S=0, boundary points of the open k=0 region, or identically zero local branches. The unrestricted conjecture remains OPEN.

## 7. Dependencies and scope of confirmation

A2107-A2111 supplies the necessary Hessian and scalar reduction. Its potential identity and low scalar facts are reproduced above to make the finite-jet argument explicit. A2180-A2185 is the separate complete pressure-critical local proof in the team records. A2134-A2140 and the stated actual next-scalar constructions are used only in the transfer, not in the new local theorem.

All seven source sections, both source checker programs and their outputs were read. All seven sections of this independent proof are to be postread before verdicts are registered. The source pin, independent question and pass criterion, script, exact output and final-read record are in verification. No formal build or new model client was used. Collaboration remains through the existing configured model agents, with actual provider execution independently unattested.
