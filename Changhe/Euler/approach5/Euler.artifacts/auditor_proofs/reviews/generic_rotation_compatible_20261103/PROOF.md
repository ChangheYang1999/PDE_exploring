# Prescribed rotation outside at most one exceptional magnitude

## 1. Exact local assertion and evidence

Fix 0<c<1/2, n an integer at least4, a=1-2c, b=2(1-c)=a+1, eta=a/b, kappa=(b+1)/b and m=n-4. Thus 0<a<1, b>0 and eta>0. This audit concerns LIT299, source SHA256 a65636f29181aeeecf547ab97e7d414e6fc9ee2e59fd19b2fe9274f09cb338f3, retained as in the team records. Its assertion is local and analytic. It supplies neither a full next scalar nor a global Euler profile.

Define the cubic N and two auxiliary polynomials by

    N=N3 t^3+N2 t^2+N1 t+N0,
    N3=2a[45a^3 m+129a^3+84a^2 m+215a^2+39am+114a+18],
    N2=3a(a+1)[(15a^2+59a+42)m+82a^2+202a+84],
    N1=-9(a+1)^2[(5a^2+15a)m-25a^2+33a+18],
    N0=81(a+1)^3(5a-4m-11),
    C0(t)=2a(3a+5)t+(3/4)(a+1)(11a+9),
    D(t)=t[2at^2-3at-9(a+1)]/[2(a+1)].

Let tau denote the unique positive root of N, proved below. Define E(c,n) to be empty if D(tau)>=0, and otherwise the singleton containing sqrt(-C0(tau)/D(tau)). For every prescribed v>0 outside E(c,n), put X=(cx-vz,cy,1+vx+cz). There are real analytic H>0, phi,p1 near zero, with H(0)=1, section gradient grad_xy H(0)=(g,0) for some g<0, and section potential leading term Re((x+iy)^n)/n, such that

    V=H^eta grad phi, W=curl V, P2=H+|V|^2/2, Z=DV V+grad P2,
    XH=-bH, Xphi=0, div V=0, -Delta P2=tr((DV)^2),
    Xp1=-(b+1)p1, W.grad(p1-2V.grad P2)=0,
    Delta p1+2tr(DV DZ)=O(distance^(n+1)).

Here distance is distance from the one common local zero arc of V and W. Both have exact transverse order n-1 and W has full relative support. The estimate is local after shrinking the neighborhood. The expression using distance at the arc is stronger than the displayed source estimate from the origin, and follows from transport below. The rotation vector is (0,v,0), with the sign convention of the source, after translation from p=(v,0,c)/(c^2+v^2); p is off-axis and equatorial. Coordinate rotation allows any axis. The exceptional rate is unclaimed, not excluded.

All six source sections and the full sparse engine and coefficient extractor were read. The reviewed engine was replayed, with independently written checks of the printed identities and exact JSON certificates. It passed in189.9718481344171 actual seconds on CPU55, nice19, OMP_NUM_THREADS=1. This is not a second independently implemented recurrence. The source's separate original Cartesian sample is supplementary. Exploratory resultants and numerical root illustrations are not used in this proof.

## 2. Middle equation, root selection and exceptional set

Use g=-tv. The exact recurrence of Section3 gives middle coefficient v^2 F(t), where F=A+v^2 B and

    A=-(A2 t^2+A1 t+A0)/[96(a+1)],
    A2=(108a^3+48a^2-252a)m+348a^3+52a^2-888a+216,
    A1=(576a^3+1386a^2+1080a+270)m+2102a^3+4790a^2+3210a+522,
    A0=(495a^3+1683a^2+1881a+693)m+2115a^3+7047a^2+7749a+2817,
    B=t(B3 t^3+B2 t^2+B1 t+B0)/[144(a+1)^3],
    B3=(48a^3+156a^2+108a)m+128a^3+432a^2+324a,
    B2=-(42a^3+186a^2+144a)m-108a^3-540a^2-432a,
    B1=(279a^3+396a^2-45a-162)m+1233a^3+1656a^2-387a-810,
    B0=405(a+1)^3(m+5).

For any v>0, F(0)<0 because A0>0, while the degree-four coefficient v^2 B3/[144(a+1)^3] is positive. Thus F has a positive real root. No unsupported sign assertion about A2 or B1 is needed.

The high harmonic response T obeys T/v=C0+v^2 D. Direct rational polynomial expansion gives

    BC0-DA=t[(5a+9)t+6(a+1)]N/[144(a+1)^3].

The independent checker reconstructs both sides from the recurrence and verifies this identity exactly. If F=T=0 at t>0, multiply F by D and use the response to obtain DA-BC0=0. The prefactor of N is nonzero, so N(t)=0. The coefficients of N have descending signs +,+,-,-: N3,N2>0, N0<0, and the bracket in -N1 is positive since -25a^2+33a+18>=8a+18>0. Descartes' rule counts at most one positive root with multiplicity; N(0)<0 and its positive leading coefficient give one. Hence tau exists, is unique and is simple.

C0(t)>0 for t>0. Therefore a simultaneous positive root requires D(tau)<0 and v^2=-C0(tau)/D(tau). Outside E, every positive root of F is nondegenerate for the high response. Choose any one of them. Neither continuity nor analyticity of this selection in c,n,v is required, since the claimed germs are constructed separately for each parameter value. Seven indexed exact certificates independently reconstruct the sign polynomials after a=u/(1+u), u>0. They are supplementary to the direct inequalities just given; importing JSON alone establishes no sign.

## 3. Finite jets and the complete residual through degree n

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

Its scalar response is (2kappa-eta)g, nonzero because 2kappa-eta>0 and g<0. Define C_n=-R0/[(2kappa-eta)g] and p1=2V.grad P2+C_n H^kappa phi. The direct R0 formula was separately checked against the engine's extracted C_n.

Through degree n the full residual is

    R=Delta(C_n H^kappa phi)
       +2H^eta[Hess phi:B_H+grad phi.C_H],
    C_H=(2eta/H)Hess H grad H
       +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H+grad Delta H.

The omitted velocity terms are cubic and start at degree3n-6>n. The exact leading pressure equation gives Delta H of order at least2n-4>=4. Its contributions to the low jets of C_H and to the scalar term above are therefore beyond degree n. In particular the engine's omission of these low jets is justified by the equation, not an assumption that H is globally harmonic.

The holomorphic contribution at degree n has exactly three bands J w^n+K w^(n-1)wb+L0 w^(n-2)wb^2. All coefficients are real. Two derivatives of the leading harmonic and coefficient jets of degree at most2 permit only these frequency changes; the explicit engine enumerates all retained monomials and the independent checker finds no others. Its rational output agrees exactly with K=v^2 F and T=(C_n-C_(n+1))(2kappa-eta)g=v(C0+v^2 D), holding c,v,g fixed when replacing n by n+1. The symbolic n computation is an identity, not a sample of integer n.

## 4. Free harmonics and retention of the jets

Add beta Re(w^4)/24 to h and alpha Re(w^(n+1))/(n+1) to the potential. The quartic pressure changes only the low coefficient, by3(n-1)beta, through6 Hess(phi_leading):Hess(delta h). Choose beta=-L0/[3(n-1)]. The potential changes the high coefficient by alpha T/2; its possible low coefficient vanishes by the same previous-degree identity with n replaced by n+1. Choose alpha=-2J/T. The middle coefficient already vanishes by root selection. T is nonzero by Section2 and n-1 is nonzero. For n=4 the low band is its own conjugate, so the coefficient and response both double and the same beta cancels it.

The alpha-beta product begins at degree n+1. A free harmonic of potential degree n+2 contracts to zero with the scalar restriction of B_H at the center. No unchosen higher jet changes this degree-n cancellation. All lower residual bands were already canceled. This proves compatibility of the specified finite jets for the two exact leading equations and finite order for the next scalar residual; it does not solve the latter at later orders.

## 5. Analytic realization without a third-derivative equation

Use the local analytic flow chart of X from z=0. It exists because X(0)=(0,0,1). In its coordinates set H=e^(-bs)h, phi=f. Thus both transport equations hold identically. Define

    F0=Delta phi+eta grad(log H).grad phi,
    E2s=Delta H+(1/2)|grad phi|^2 Delta(H^(2eta))
       +2grad(H^(2eta)).(Hess phi grad phi)+H^(2eta)|Hess phi|^2
       -eta H^(2eta)grad phi.grad(grad(log H).grad phi)
       +tr((DV)^2).

Expansion of Delta(|V|^2/2) gives

    Delta P2+tr((DV)^2)=E2s+H^(2eta)grad phi.grad F0.

This identity removes the apparent third derivatives of phi. F0=0,E2s=0 is an analytic second-order system in the section functions f,h. In E2s the second derivatives of h occur affinely. At zero H=1 and grad phi=Hess phi=0 since n>=4. Solve the first equation for f_yy and then the second for h_yy. Their diagonal coefficients at the prescribed jet are1; the implicit function theorem solves the system for these two highest derivatives in a neighborhood. It is noncharacteristic for the analytic Cauchy theorem.

Prescribe analytic f,f_y,h,h_y on y=0 whose finite jets equal those constructed above, for example the corresponding polynomials with arbitrary higher coefficients zero. The Cauchy theorem gives an analytic solution. Uniqueness of the recursive Taylor coefficients for f_yy,h_yy makes its finite jets agree with the compatible finite jets in Sections3-4. The pressure trace through degree4 and potential trace through degree n+2 are the only traces needed for the tested scalar residual. Shrink the chart to keep H>0. The divergence and pressure equations are now exact, whereas the next scalar residual is still asserted only through degree n. This is the same noncharacteristic local mechanism checked in A2355; it does not require any global flow or boundary assumption.

## 6. Zero arc, exact scalar transports and limits

On the transverse section the leading gradient of Re(w^n)/n has norm rho^(n-1). Higher analytic terms are O(rho^n), so the section potential has exactly one critical point sufficiently near zero. The invertible flow chart and transport Xphi=0 carry this to precisely one zero arc of grad phi, hence of V. Because XH=-bH is nonzero and Xphi=0, grad H and a nonzero grad phi cannot be parallel. Consequently

    W=eta H^(eta-1)grad H cross grad phi

has exactly the same zero set and exact order n-1. The transverse cross product is uniformly bounded below relative to |grad phi| after shrinking the chart, using bH>0 and X bounded. Thus the zero arc has empty interior and the closure of the nonzero set of W is the whole local domain.

The cross product also annihilates H and phi, so W.grad(p1-2V.grad P2)=0 exactly. The homogeneity of V and grad P2 makes their scalar product have weight b+1; H^kappa phi has the same weight. Thus Xp1=-(b+1)p1 exactly. Applying the scalar Laplacian adds weight2c. The other residual term has the same weight, so its total carrier weight is b+1+2c=3. An O(rho^(n+1)) section residual therefore retains that transverse order all along the local arc. Local equivalence of chart distance and Euclidean distance proves the estimate of Section1.

No pressure normalization, far-field bound, extension across the rotation axis or completeness at infinite time is claimed or used. The all-but-at-most-one-rate finite result is confirmed. The exceptional rate, a full next scalar, an all-order or convergent Euler tail, and the global smooth decaying nonexistence conjecture remain unproved by this argument. An obstruction for different fixed positive-gradient jets is compatible with the construction here.
