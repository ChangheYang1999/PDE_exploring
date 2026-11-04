# Finite compatibility at every prescribed nonzero rotation magnitude

## 1. Exact theorem and local scope

Let 0<c<1/2, n be an integer at least4 and v>0 be arbitrary. Put a=1-2c, b=2(1-c)=a+1, eta=a/b, kappa=(b+1)/b, m=n-4 and X=(cx-vz,cy,1+vx+cz). There are real analytic H>0, phi,p1 near zero, with H(0)=1 and grad_xy H(0)=(g,0) for some nonzero real g, such that

    V=H^eta grad phi, W=curl V, P2=H+|V|^2/2, Z=DV V+grad P2,
    XH=-bH, Xphi=0, div V=0, -Delta P2=tr((DV)^2),
    Xp1=-(b+1)p1, W.grad(p1-2V.grad P2)=0,
    Delta p1+2tr(DV DZ)=O(distance^(n+1)).

The distance is from the unique local common zero arc of V,W. The fields have exact transverse order n-1 and W has full relative support. The section potential starts with Re((x+iy)^n)/n. A rigid rotation gives the same result at an equatorial off-axis point for any rotation axis with magnitude v. No sign for g is prescribed. This is an exact leading-system germ and finite next-residual construction, not a full next scalar or Euler profile. Rotation zero is not included.

The source is LIT300, pinned as in the team records, SHA256 eb704bcdbdb9f44bf0d02ebb65ccd40e63418f5913f5954c3bf697152c7fdae3. All six source sections and the whole source checker and data were read. The new coefficient-map determinant and boundary checks were independently assembled from the printed formulas and imported exact JSON. They passed in20.617871346883476 actual seconds on CPU55, nice19, OMP1. The unrestricted-g finite recurrence was already checked in A2386 and was not rerun. No exploratory numerical root or simple-root assumption is used.

## 2. Quartic, response and elimination

Write g=-tv and zeta=v^2. Let F=A+zeta B, where

    A=-(A2 t^2+A1 t+A0)/[96(a+1)],
    A2=(108a^3+48a^2-252a)m+348a^3+52a^2-888a+216,
    A1=(576a^3+1386a^2+1080a+270)m+2102a^3+4790a^2+3210a+522,
    A0=(495a^3+1683a^2+1881a+693)m+2115a^3+7047a^2+7749a+2817,
    B=t(B3 t^3+B2 t^2+B1 t+B0)/[144(a+1)^3],
    B3=(48a^3+156a^2+108a)m+128a^3+432a^2+324a,
    B2=-(42a^3+186a^2+144a)m-108a^3-540a^2-432a,
    B1=(279a^3+396a^2-45a-162)m+1233a^3+1656a^2-387a-810,
    B0=405(a+1)^3(m+5).


Define

    C0(t)=2a(3a+5)t+(3/4)(a+1)(11a+9),
    D(t)=t[2at^2-3at-9(a+1)]/[2(a+1)], G=C0+zeta D,
    N=N3 t^3+N2 t^2+N1 t+N0,
    N3=2a[45a^3 m+129a^3+84a^2 m+215a^2+39am+114a+18],
    N2=3a(a+1)[(15a^2+59a+42)m+82a^2+202a+84],
    N1=-9(a+1)^2[(5a^2+15a)m-25a^2+33a+18],
    N0=81(a+1)^3(5a-4m-11).

For fixed a in(0,1), m>=0 and zeta>0, A0,B3>0, so F(0)<0 and the quartic leading coefficient is positive. Thus F has at least one positive and one negative real root, necessarily distinct and nonzero. We require a root with G nonzero. The exact polynomial identity

    BC0-DA=t[(5a+9)t+6(a+1)]N/[144(a+1)^3]

was checked in A2386 and independently checked again here. If F(t)=G(t)=0, its left side vanishes. The root t=0 is impossible. The possible additional linear root tL=-6(a+1)/(5a+9) satisfies

    G(tL)=27(a+1)(7a^2+64a+81)/(5a+9)^3
             *[zeta+(5a+9)^2/36]>0.

Consequently every common root of F,G is a root of N. This argument multiplies identities and divides by no root-dependent value of D, so a possible zero of D causes no loss.

## 3. Distinct-root obstruction away from a=1/5

Write C0=c1 t+c0 and D=d3 t^3+d2 t^2+d1 t. For distinct complex numbers r,s, direct expansion gives

    [C0(r)D(s)-C0(s)D(r)]/(s-r)
      =c0[d3(r^2+rs+s^2)+d2(r+s)+d1]
         +c1 rs[d3(r+s)+d2].

Suppose r,s are distinct roots of N. N3>0, so N has degree3. Let q be the third root with its algebraic multiplicity; q may equal r or s. Set sigma=-N2/N3, e2=N1/N3, u=sigma-q and w=e2-qu. Vieta gives r+s=u, rs=w. The divided expression is therefore

    Xi(q)=c0[d3(u^2-w)+d2 u+d1]+c1 w[d3 u+d2].

Let H0=N3/(2a)>0 and Xin(q)=16(a+1)H0^2 Xi(q). Expansion makes Xin a cubic polynomial in q with polynomial coefficients in a,m. The common denominator is nonzero in the parameter range. The exact determinant identity is

    Res_q(N,Xin)
      =-314928 a^5(a+1)^6(5a-1)^2 H0^5 Q(a,m).

Here Q is defined by the complete exact input in the team records: Q=sum h_ij a^i m^j, one coefficient for every0<=i<=11,0<=j<=4. The checker verifies the complete index rectangle, uniqueness of indices, integrality and strict positivity of all60 entries, and equality with the full determinant. It does not infer the determinant identity from positivity or from importing the table. The determinant is that of the coefficient map (U,V) to UN+VXin, with U,V of degree at most2, in descending monomial bases. Its columns were formed explicitly and its determinant evaluated in an exact polynomial domain. This is the transpose of the usual six-by-six Sylvester matrix, with the same determinant.

In particular Q(a,m)>0 for a>0,m>=0, including m=0 because the coefficients with m-exponent0 are positive. If a!=1/5, every other displayed factor is nonzero. N and Xin have no common complex root. Now if the two distinct roots r,s also satisfied G(r)=G(s)=0, then C0(r)=-zeta D(r) and C0(s)=-zeta D(s), making the divided expression zero. Hence Xi(q)=0 and Xin(q)=0 while N(q)=0, a contradiction. This works even if either D value vanishes, or N has a repeated root. There is at most one distinct common root of F,G. F has roots on both sides of zero, so at least one of them is nondegenerate. Choose it and set g=-tv, which is nonzero.

## 4. The parameter a=1/5

This is c=2/5. Although it is the endpoint of the campaign interval, it belongs to the stronger local theorem and cannot be silently omitted. Direct substitution gives

    G(t)=(2t+9)(25t^2 zeta-150t zeta+336)/300.

For t<0 and zeta>0 the quadratic factor is strictly positive. Hence the only possible negative root of G is -9/2. But

    F(-9/2)=3[148500m zeta+84480m+202725 zeta+23488]/12800>0.

Every negative root of F is therefore nondegenerate. Such a root exists by Section2. Both identities were checked exactly from the original A,B,C0,D definitions. This completes the selection for all parameters. No selection needs to vary continuously with the parameters.

## 5. Finite jets and the complete residual through degree n

Set w=x+iy and rho^2=x^2+y^2. With the selected nonzero g put

    h33=b(b+c)+vg, h0=-h33/2+eta g^2/6,
    T2=diag(h0-eta g^2/3,h0),
    u=-(b+c)(g,0)+b(v,0),
    d=-(b+2c)u+T2(v,0)-h33(v,0),
    A3=eta g^3(2eta+3)/36,
    h3=1+gx+(x,y).T2(x,y)/2-rho^2(d.(x,y))/8+(A3/6)Re(w^3).

The first and second normal derivatives of a transported section F, XF=-d0 F, are

    Nz F=-(d0+T0)F/(1+vx),
    Nzz F=[v partial_x F-(d0+c+T0)Nz F]/(1+vx),
    T0=c(w partial_w+wb partial_wb).

These follow by differentiating XF=-d0 F once in z before setting z=0. In particular the v partial_x term has the positive sign. The section Laplacian is L=4 partial_w partial_wb+Nzz. Let I(w^i wb^j)=w^(i+1)wb^(j+1)/[4(i+1)(j+1)]. Fix the pressure trace through degree4 as h3-I([Lh3]_2), initially with zero free quartic harmonic. Start the holomorphic potential half at w^n/(2n) and subtract I of its divergence residual at degrees n-1 and n successively. This determines the nonharmonic traces through degree n+2. All factors n+i+1 used here are nonzero for n>=4 at the indices encountered. The conjugate half supplies a real section.

At the center B_H=3 Hess H+(eta/H)grad H tensor grad H restricts to a scalar on X(0)^perp. This kills the degree n-2 term of the next scalar residual. The low band at degree n-1 vanishes by 12A3=eta g^3(1+2eta/3). Its high band is real by reflection y to -y. Let R0 be twice

    -3h0(eta g+v)-(3/2)(n-1)d1
    +eta g(n-1)(-h33-g^2/2)-2nc(3u1-eta b g)
    +(3h33+eta b^2)v
    +[2eta(T2(g,0)-bu)+eta^2(g^2+b^2)(g,0)]_1.

Its scalar response is (2kappa-eta)g, nonzero because 2kappa-eta>0 and g!=0. Define C_n=-R0/[(2kappa-eta)g] and p1=2V.grad P2+C_n H^kappa phi. The direct R0 formula was separately checked against the engine's extracted C_n.

Through degree n the full residual is

    R=Delta(C_n H^kappa phi)
       +2H^eta[Hess phi:B_H+grad phi.C_H],
    C_H=(2eta/H)Hess H grad H
       +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H+grad Delta H.

The omitted velocity terms are cubic and start at degree3n-6>n. The exact leading pressure equation gives Delta H of order at least2n-4>=4. Its contributions to the low jets of C_H and to the scalar term above are therefore beyond degree n. In particular the engine's omission of these low jets is justified by the equation, not an assumption that H is globally harmonic.

The holomorphic contribution at degree n has exactly three bands J w^n+K w^(n-1)wb+L0 w^(n-2)wb^2. All coefficients are real. Two derivatives of the leading harmonic and coefficient jets of degree at most2 permit only these frequency changes; the explicit engine enumerates all retained monomials and the independent checker finds no others. Its rational output agrees exactly with K=v^2 F and T=(C_n-C_(n+1))(2kappa-eta)g=vG, holding c,v,g fixed when replacing n by n+1. The symbolic n computation is an identity, not a sample of integer n.

## 6. Free harmonics and retention of the jets

Add beta Re(w^4)/24 to h and alpha Re(w^(n+1))/(n+1) to the potential. The quartic pressure changes only the low coefficient, by3(n-1)beta, through6 Hess(phi_leading):Hess(delta h). Choose beta=-L0/[3(n-1)]. The potential changes the high coefficient by alpha T/2; its possible low coefficient vanishes by the same previous-degree identity with n replaced by n+1. Choose alpha=-2J/T. The middle coefficient already vanishes by root selection. T is nonzero by Sections3-4 and n-1 is nonzero. For n=4 the low band is its own conjugate, so the coefficient and response both double and the same beta cancels it.

The alpha-beta product begins at degree n+1. A free harmonic of potential degree n+2 contracts to zero with the scalar restriction of B_H at the center. No unchosen higher jet changes this degree-n cancellation. All lower residual bands were already canceled. This proves compatibility of the specified finite jets for the two exact leading equations and finite order for the next scalar residual; it does not solve the latter at later orders.

## 7. Analytic realization without a third-derivative equation

Use the local analytic flow chart of X from z=0. It exists because X(0)=(0,0,1). In its coordinates set H=e^(-bs)h, phi=f. Thus both transport equations hold identically. Define

    F0=Delta phi+eta grad(log H).grad phi,
    E2s=Delta H+(1/2)|grad phi|^2 Delta(H^(2eta))
       +2grad(H^(2eta)).(Hess phi grad phi)+H^(2eta)|Hess phi|^2
       -eta H^(2eta)grad phi.grad(grad(log H).grad phi)
       +tr((DV)^2).

Expansion of Delta(|V|^2/2) gives

    Delta P2+tr((DV)^2)=E2s+H^(2eta)grad phi.grad F0.

This identity removes the apparent third derivatives of phi. F0=0,E2s=0 is an analytic second-order system in the section functions f,h. In E2s the second derivatives of h occur affinely. At zero H=1 and grad phi=Hess phi=0 since n>=4. Solve the first equation for f_yy and then the second for h_yy. Their diagonal coefficients at the prescribed jet are1; the implicit function theorem solves the system for these two highest derivatives in a neighborhood. It is noncharacteristic for the analytic Cauchy theorem.

Prescribe analytic f,f_y,h,h_y on y=0 whose finite jets equal those constructed above, for example the corresponding polynomials with arbitrary higher coefficients zero. The Cauchy theorem gives an analytic solution. Uniqueness of the recursive Taylor coefficients for f_yy,h_yy makes its finite jets agree with the compatible finite jets in Sections5-6. The pressure trace through degree4 and potential trace through degree n+2 are the only traces needed for the tested scalar residual. Shrink the chart to keep H>0. The divergence and pressure equations are now exact, whereas the next scalar residual is still asserted only through degree n. This is the same noncharacteristic local mechanism checked in A2355; it does not require any global flow or boundary assumption.

## 8. Zero arc, exact scalar transports and limits

On the transverse section the leading gradient of Re(w^n)/n has norm rho^(n-1). Higher analytic terms are O(rho^n), so the section potential has exactly one critical point sufficiently near zero. The invertible flow chart and transport Xphi=0 carry this to precisely one zero arc of grad phi, hence of V. Because XH=-bH is nonzero and Xphi=0, grad H and a nonzero grad phi cannot be parallel. Consequently

    W=eta H^(eta-1)grad H cross grad phi

has exactly the same zero set and exact order n-1. The transverse cross product is uniformly bounded below relative to |grad phi| after shrinking the chart, using bH>0 and X bounded. Thus the zero arc has empty interior and the closure of the nonzero set of W is the whole local domain.

The cross product also annihilates H and phi, so W.grad(p1-2V.grad P2)=0 exactly. The homogeneity of V and grad P2 makes their scalar product have weight b+1; H^kappa phi has the same weight. Thus Xp1=-(b+1)p1 exactly. Applying the scalar Laplacian adds weight2c. The other residual term has the same weight, so its total carrier weight is b+1+2c=3. An O(rho^(n+1)) section residual therefore retains that transverse order all along the local arc. Local equivalence of chart distance and Euclidean distance proves the estimate of Section1.

No pressure normalization, far-field bound, extension across the rotation axis or completeness at infinite time is claimed or used. Every nonzero rotation magnitude is now covered at this finite level. The rate exception of LIT299 is removed by allowing either sign of g. A full next scalar, an all-order or convergent Euler tail, and the global smooth decaying nonexistence conjecture remain unproved by this argument. An obstruction for different fixed positive-gradient jets is compatible with the construction here.
