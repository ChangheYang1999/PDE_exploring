# Uniform later obstruction for one aligned off-axis family

Status: CONFIRMED at the exact scope below. The unrestricted rotating Euler profile problem remains OPEN. The complete submitted LIT296 proof is pinned in the team records with SHA256 3ab1181a67e1ebce2521a29cc2fcd58c12d74ffb85584af7ad5b65c21c999378. The earlier independently audited first compatibility calculation is in the team records; the separate full Cartesian tests at orders three and four are in the team records.

## 1. Exact statement

Fix 0<c<1/2, an arbitrary real r, v>0, and an integer n>=4. Set b=2(1-c), eta=(1-2c)/b and kappa=(b+1)/b. In local Cartesian coordinates let

    X=(cx+ry-vz,-rx+cy,1+vx+cz).

The carrier speed at the origin is one. Let H>0 and phi be smooth on a neighborhood of the origin, with

    XH=-bH, Xphi=0, V=H^eta grad phi, div V=0,
    W=curl V, E=|V|^2, P2=H+E/2,
    -Delta P2=tr((DV)^2), Z=DV V+grad P2.

Here (DV)_ij=partial_j V_i, so tr((DV)^2) is a matrix trace, not a squared Euclidean norm. Put w=x+iy, rho^2=x^2+y^2 and JT(x,y)=(-y,x). Prescribe on z=0

    phi=Re(w^n)/n+O(rho^(n+1)),
    Dn=8b eta(n-1)+12b(3n-1)+18c(n-1),
    g=6b(5n-1)v/Dn,
    h33=b(b+c)+vg, t=-h33/2+eta g^2/6,
    T=diag(t-eta g^2/3,t), gvec=(g,0), vvec=(v,0),
    u=-(b+c)gvec-r JT gvec+b vvec,
    d=-(b+2c)u-r JT u+T vvec-h33 vvec,
    A3=eta g^3(2eta+3)/36,
    H=1+gx+(1/2)(x,y).T(x,y)
        -rho^2(d1*x+d2*y)/8+(A3/6)Re(w^3)+O(rho^4).

All unspecified higher coefficients are free subject to the displayed field equations. There is no C1 scalar p1 on a neighborhood satisfying

    Xp1=-(b+1)p1,
    W.grad(p1-2V.grad P2)=0,
    Delta p1=-2tr(DV DZ).                                  (1)

The last equation may initially be distributional. This theorem applies to the stated normalized, aligned-gradient, fixed-phase family and every smooth completion of its prescribed jets. It does not assert that a general off-axis zero has these jets. Its rotation vector is (0,v,r), so it handles every r for every v>0 in this family, rather than every possible local configuration for a prescribed rotation. The zero order of V is n-1>=3.

## 2. Exhaustion of the scalar freedom

Interior elliptic regularity in (1) makes p1 smooth. The leading equations give X(V.grad P2)=-(b+1)V.grad P2: both V and grad P2 have the same skew rotation contribution, which cancels in their dot product, while their scalar weights add to b+1. Moreover W=eta H^(eta-1) grad H cross grad phi, so WH=0. Consequently

    theta=H^(-kappa)(p1-2V.grad P2)

satisfies Xtheta=0 and Wtheta=0. Since XH=-bH is nonzero, restriction to z=0 reduces the second equation to the two-dimensional Poisson bracket {f,theta}=0, with f=phi restricted to that section. The factor relating the two brackets is nonzero near the origin because the section is transverse to X and H>0.

For P=Re(w^n)/n, every homogeneous polynomial Q of degree j>0 with {P,Q}=0 is zero unless n divides j, and otherwise is a constant multiple of P^(j/n). To see this, write P=rho^n cos(n angle)/n and Q=rho^j q(angle). The bracket equation integrates on each sector to q=C cos(n angle)^(j/n). The sector boundaries are simple zeros of cos(n angle). Polynomial smoothness there requires an integer power, and the corresponding nonzero derivative across each boundary fixes the same constant on adjacent sectors. Thus no additional piecewise polynomial solution occurs.

Apply this observation to the successive homogeneous terms of theta-theta(0). Terms of degrees one through n-1 vanish. At the origin V has order n-1>=3, so the right side of the pressure equation and Delta(2V.grad P2) vanish there. The leading pressure equation gives Delta H(0)=0. Hence (1) at the origin is

    theta(0) kappa(kappa-1)|grad H(0)|^2=0.

Here kappa>1 and H_z(0)=-b, so theta(0)=0. The term of degree n is CP for a real C. Subtract C f and apply the same argument successively through degree 2n-1. It follows on the section that theta=Cf+O(rho^(2n)). The smooth noncharacteristic transport by X preserves this vanishing order in full local coordinates. Therefore

    theta=C phi+O(distance^(2n)).

The Laplacian of its contribution to p1 has order at least 2n-2>n. Thus the complete scalar freedom in (1), not merely a chosen scalar ansatz, reduces through residual degree n to the single real coefficient C.

The previous degree n-1 equation fixes C uniquely. Its high-band coefficient has a factor (2kappa-eta)g>0. Substitution of the stated g makes the remaining high coefficient real, and the stated A3 cancels the other band. These identities were derived for general n in the earlier first compatibility audit and are independently reproduced by the symbolic recurrence below. No further scalar parameter can alter the obstruction at degree n.

## 3. Reduced residual and the free field jets

After substituting p1=2V.grad P2+C H^kappa phi up to the irrelevant scalar remainder, the residual Delta p1+2tr(DV DZ) is, through degree n,

    R=Delta(C H^kappa phi)+Rlin,
    Rlin=2H^eta[Hess phi:B+grad phi.C_H],
    B=3Hess H+(eta/H)grad H tensor grad H,
    C_H=(2eta/H)Hess H grad H
       +[(eta/H)Delta H+(eta^2/H^2)|grad H|^2]grad H
       +grad Delta H.                                    (2)

This follows by expanding 2Delta(V.grad H)+2tr(DV Hess H), using V=H^eta grad phi and Delta phi=-eta H^(-1)grad H.grad phi. The two mixed Cartesian Hessian entries each contribute to the contraction. The remaining expression is

    Delta(V.grad E)+2tr(DV D(DV V))+tr(DV Hess E),

which has order at least 3n-6>n. The leading pressure equation also gives Delta H=O(distance^(2n-4)). In particular its section terms through degree two vanish and the terms involving Delta H or grad Delta H in (2) cannot affect the constant and linear terms of C_H needed at degree n.

The coefficient to be tested is K=[w^(n-1) conjugate(w)]R_n. The only potentially relevant free section jets are the harmonic part of phi of degree n+1 and the harmonic part of H of degree four. Their particular trace parts are forced by divergence and pressure. A free harmonic term of phi of degree n+2 has a trace-free transverse Hessian, whereas B(0) restricted to the transverse plane is 3t times the identity. Its contraction is zero; normal Hessian terms have higher order. Later potential terms do not contribute at this degree.

For a free harmonic potential of degree n+1, use the preceding general degree formula with that leading degree, keeping the fixed pressure jets. Its possible band of angular frequency n-2 has coefficient proportional to

    12A3-eta g^3(1+2eta/3)=0.

This calculation holds for both real harmonic phases, as shown by the complete complex contraction in Section 5 of the earlier first compatibility audit. The remaining change, including the scalar term, has only frequency n. A free harmonic quartic pressure contributes only 6 Hess(h4):Hess(P) at degree n. Its frequency has absolute value |n-4|, distinct from n-2 for n>=4. Normal derivatives and coefficient changes from h4 enter later. Thus no free field coefficient changes K. In particular n=4 is allowed: the quartic pressure changes the constant angular band while K has band two.

## 4. Finite exact recurrence for K

The following explicit recurrence makes (2) an algebraic identity check for arbitrary n. Treat w and wb as independent variables, x=(w+wb)/2. For a section scalar F of carrier weight d0, so XF=-d0 F, define

    T0=(c-ir)w partial_w+(c+ir)wb partial_wb,
    Nz(F)=-(d0+T0)F/(1+vx),
    Nzz(F)=[v partial_x F-(d0+c+T0)Nz(F)]/(1+vx),
    L(F)=4 partial_w partial_wb F+Nzz(F).        (3)

The first formula for normal derivatives is the transport equation on z=0. Differentiating it in z and using partial_z X=(-v,0,c) gives the second. Mixed Hessian entries are transverse derivatives of Nz; transverse entries use partial_x=partial_w+partial_wb and partial_y=i(partial_w-partial_wb). All Taylor truncations are made after the displayed derivatives to sufficient order.

Begin with the cubic section pressure in Section 1. Subtract the inverse transverse Laplacian applied to the degree-two part of L(H). The inverse on w^i wb^j is w^(i+1)wb^(j+1)/[4(i+1)(j+1)]. This fixes its quartic trace, and choose zero free harmonic quartic part. Start phi with the holomorphic half w^n/(2n), and successively subtract this inverse applied to degrees n-1 and n of

    L(phi)+eta H^(-1)grad H.grad phi.

This gives the required particular potential through degree n+2. Its conjugate leading half cannot contribute to K: doing so would require a change of angular frequency 2n-2, whereas the coefficient degrees and two derivatives here permit at most four; 2n-2>4 for n>=4. The calculations remain linear in phi at these orders.

Use (3) and the Cartesian contractions in (2). For the scalar term one may use

    Delta(H^kappa phi)
      =(2kappa-eta)H^(kappa-1)grad H.grad phi
       +kappa(kappa-1)H^(kappa-2)phi|grad H|^2

through degree n. The omitted kappa H^(kappa-1)phi Delta H is of higher order. Fix C by the preceding w^(n-1) coefficient and extract K. This recurrence uses finite rational operations with n symbolic. All divisions introduced by inverse Laplacians are nonzero for n>=4; the other displayed denominators are nonzero in the asserted parameter range.

The independently written sparse symbolic Taylor implementation in the team records reconstructs both normal jets, all Cartesian Hessian contractions and these trace equations. The source scripts were inspected but not executed. Its exact result agrees identically with the submitted coefficient, gives real C, and verifies both formulas below. This is a check of a symbolic rational identity, not extrapolation from selected integer orders. The finite recurrence and the sign argument together supply the stated all-n conclusion.

## 5. Nonzero axial rotation component

Put D=35cn-11c-40n+16. Exact simplification of (2)-(3) gives

    Im K=3r v^2(c-1)F(c,n)/D^2,
    F=(1600c^2-1450c-350)n^3
      +(-3500c^2+5630c-1895)n^2
      +(1554c^2-3120c+1500)n
      -198c^2+468c-279.                         (4)

For 0<=c<=1/2 the four coefficient functions are at most -350, 45, 1500 and -189/2 respectively. The first is convex, so its maximum is at an endpoint; the second and fourth are increasing on this interval; the third is decreasing. For n>=4, 45/n+1500/n^2<=105, hence

    F<=-245n^3-189/2<0.

Also D=(35n-11)c-40n+16<=21/2-45n/2<0. Formula (4) is therefore nonzero whenever r!=0, since v>0 and c<1.

## 6. Zero axial rotation component

For r=0 put a=1-2c>0 and m=n-4>=0. The same recurrence gives the exact identity

    K=-v^2(1-c)G(a,m,v)/(256 D^4),
    G=G0(a,m)+v^2 G2(a,m).                     (5)

The polynomials are the indexed sums of the integer data in the team records. G0 has exactly all 36 pairs 0<=i<=5, 0<=j<=5 for the monomial a^i m^j. G2 has exactly all 24 pairs 0<=i<=3, 0<=j<=5. All 60 coefficients are strictly positive integers. Their constant coefficients are 544063476807 and 265348870380 respectively.

The independent checker imports these exact integers, verifies the complete index rectangles and positivity, reconstructs G, and verifies (5) against its own symbolic recurrence for K after r=0, c=(1-a)/2, n=m+4. Importing the data alone is not the proof: the checked rational identity and complete positive coefficient set are essential dependencies. They imply G>0 for a,m>=0 and v>0. Since D!=0, (5) is strictly negative, including m=0. Thus K is nonzero also for r=0.

## 7. Contradiction, evidence and limits

If (1) held, every Taylor coefficient of its smooth Poisson residual would vanish. Sections 2-3 show that its degree-n middle coefficient is fixed for every allowed scalar and every smooth completion of the field jets. Sections 5-6 prove that this coefficient is nonzero for every parameter in Section 1. This contradiction proves the stated local obstruction.

The retained independent check started 2026-11-03T20:49:01.780552+00:00 and finished 2026-11-03T20:49:21.605344+00:00, using 19.824784669093788 actual seconds. It passed the symbolic source comparison, reality of C, formula (4), identity (5), all 60 positive coefficients and both complete index rectangles. It also recovered the earlier Cartesian n=4 invariant -5299294616/615616875. Its plan was recorded before execution. Code and complete output were read after execution. Source Cartesian samples corroborate the identity but are not the basis of the uniform proof. The job used CPU55, nice19, OMP1. No numerical sample is promoted to a proof, and no formal build was run.

The fixed speed, H(0)=1, phase, gradient alignment and prescribed cubic pressure are retained hypotheses. At n=3, the free quartic pressure has the same relevant angular band, and the earlier exact rational test admits cancellation; this proof does not cover that case. General off-axis zeros, arbitrary earlier jets, a full next-pressure solution at n=3, realization as an Euler profile, and the global decaying-profile conjecture remain OPEN. This result provides no far-field estimate, pressure normalization at infinity, or global characteristic completeness assertion.
