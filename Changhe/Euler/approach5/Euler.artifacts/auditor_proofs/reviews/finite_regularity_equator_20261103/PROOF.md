# Finite regularity at an equatorial irrotational interface

Status: CONFIRMED A676 after complete source and independent proof postreads. Prepared 2026-11-03T10:03:00.372246+00:00.

## 1. Statement and hypotheses

Let 2/5<c<1/2 and omega be any finite real number. Set

    p=(1-c)/c, d=p-1 in(0,1/2), sigma=1-d,
    a=1-2c=cd, q=2p/d, m=3p+1,
    A=cI-omega J, Jx=e3 cross x.

Use r=|x|, z=x3/r, w=1-z2 and the spherical frame with e_theta pointing in increasing colatitude. On the full azimuthal band r>0,0<z<delta<1, let V be C1 and P2 C2 locally up to z=0 away from0. Assume V is axisymmetric with zero azimuthal component, including its boundary values, and

    div V=0,
    V(exp(sA)x)=exp(-(1-c)s) exp(-omega sJ)V(x),
    P2(exp(sA)x)=exp(-2(1-c)s)P2(x),
    -Delta P2=tr((DV)2),
    dk wedge dS=0, k=(Ax).V, S=P2-|V|2/2.          (1)

The dilation identities are imposed for every real s. At r=1,z=0 suppose

    V=lambda e_r, lambda!=0, curl V=0.             (2)

Then, after shrinking delta and scaling by lambda, V and P2 equal the analytic normalized family of A670. Therefore no C1 scalar p1 can satisfy

    p1(exp(sA)x)=exp(-(3-2c)s)p1(x),
    -Delta p1=2div((DV)Z), Z=DV V+grad P2,
    dk wedge d(p1-2V.grad P2)=0.                   (3)

The Poisson equation here is distributional. No analytic or parity assumption is made initially. The theorem is a local interface exclusion in this exact geometry; it is not a general nonexistence theorem.

## 2. Normalization and scalar integration

Replace V by V/lambda, P2 by P2/lambda2, and p1 by p1/lambda3. Then k scales by1/lambda, S by1/lambda2, and Z by1/lambda2. Both sides of the next Poisson equation scale by1/lambda3 and its rank by1/lambda4. All other equations are similarly homogeneous. This normalization is valid also for negative lambda. Hence assume lambda=1.

Axisymmetry and twisted homogeneity reduce the field to

    V=r^-p[R(z)e_r+f(z)e_theta/sqrt(w)].            (4)

Here R is C1. The divergence formula gives f'=sigma R, hence f is C2. The data give R(0)=1,f(0)=0. The azimuthal curl is

    curl V=r^(-p-1)[wR'-df]e_phi/sqrt(w).          (5)

Indeed its spherical formula is r^-1[partial_r(r V_theta)-partial_theta V_r], with partial_theta z=-sqrt(w). At z=0, (5) gives R'(0)=0 and f''(0)=0. Restrict to a smaller band on which R>0. Since the swirl is zero, k=c r^-d R>0 and partial_r k=-dk/r is never zero.

The first rank identity gives dS=b dk, with b continuous. Contract with Ax and use the homogeneities to obtain -2(1-c)S=-a k b, so b=qS/k. Therefore d(S/k^q)=0 on the connected band. One real constant D gives

    S=-D r^-2p R^q,
    P2=r^-2p Q(z),
    Q=-D R^q+(R2+f2/w)/2.                         (6)

This also proves axisymmetry of P2, although it was not assumed. Its C2 regularity makes Q C2 up to0.

## 3. The singular leading coefficient is already inconsistent

Put F(R)=-D R^q+R2/2. If D=1/q, then F'(1)=0. The known C1 regularity and R'(0)=0 give R=1+o(z); f'=sigma R gives f=sigma z+o(z2). Taylor expansion of the analytic function F of its scalar argument, rather than an unjustified second derivative of R, yields

    Q(z)=Q(0)+sigma2 z2/2+o(z2).

Because Q is one-sided C2, Q'(0)=0 and Q''(0)=sigma2. Also Q(0)=1/2-1/q=1/(2p).

The pressure equation in (1), evaluated using (4), is

    (wQ')'+ell Q+T=0, ell=2p(2p-1),
    T=2(d2+d+1)R2+2zff'/w+2z2 f2/w2
      +2pfR'+2pf2/w.                              (7)

The contraction is the same exact full matrix trace independently reconstructed in A670. Only first derivatives of R and f occur, so T is continuous at0. Equation (7) can be passed to the boundary without assuming R''. There it would read

    0=sigma2+(2p-1)+2(d2+d+1)=3d2+2d+4,

which is impossible. This excludes the denominator singularity before any regularity improvement or division.

## 4. Implicit regularity gain and analytic uniqueness

For D!=1/q, the derivative with respect to R in (6) at z=0,f=0,R=1 is1-Dq, which is nonzero. The analytic implicit function theorem solves (6) for R as a real-analytic function of (z,f,Q) near these data. Since f and Q are C2 up to the one-sided boundary, their composition is C2, so R is C2 and f is C3.

Substitute R=f'/sigma in (7). Its coefficient of f''' is

    w[R-Dq R^(q-1)]/sigma,

nonzero near the initial data. All remaining terms are analytic in z,f,f',f'' for w>0 and R>0. Thus the one-sided C3 function satisfies an analytic normal-form ODE

    f'''=G(z,f,f',f''),
    f(0)=0, f'(0)=sigma, f''(0)=0.                 (8)

Local existence for an analytic ordinary differential equation supplies an analytic two-sided solution, and ordinary uniqueness for its locally Lipschitz first-order system identifies the given one-sided solution with its restriction. This is not an inference of convergence from formal coefficients. Reflection f(z) to -f(-z) preserves (7) and these initial data. Uniqueness makes the extension odd, with R and Q even. The positivity of R makes its noninteger powers analytic, with no branch ambiguity.

Consequently the positive-band solution is exactly the normalized analytic equatorial family in A670 for the same real D. No analytic continuation through the field actually prescribed on the negative side is asserted.

## 5. Next scalar and exact incompatibility

The rank in (3) and nonzero radial derivative of k similarly force, by homogeneity,

    p1-2V.grad P2=C r^-m R^(m/d),
    p1=r^-m[C R^(m/d)-4pRQ-2fQ'].                 (9)

This step requires only C1 p1. The right side becomes analytic up to0 by Section4, regardless of whether boundary regularity of p1 was initially imposed. It is independent of azimuth, because the scalar rank removes the azimuthal derivative as well. After the regularity gain, div Z=tr((DV)2)+Delta P2=0 and div((DV)Z)=tr(DV DZ), so the distributional and classical next equations coincide.

A670-A671 independently prove that four successive even Taylor coefficients of this next Poisson equation are incompatible for every real D and every0<d<1/2. Their proof includes both exceptional denominators, independent reconstruction from the full gradient matrices, exact resultant identities and an integer/modular coprimality certificate. The first exceptional denominator has independently been excluded already in Section3. Applying that theorem to (9) proves that (3) is impossible.

## 6. Actual-profile implication, dependencies and limits

Here a global Euler profile means div U=0 and (1-c)U+[(Ay+U).grad]U+omega JU+grad P=0 on R3. For such a global C2/C1 profile with global zero helicity and the explicit natural bounds |U|<=C(1+r)^-p, |DU|<=C(1+r)^(-p-1), the confirmed tail limits give V C1 and P2 C2 on compact annuli. A647-A648 and A653-A655 give (3) for every target exponent, including3/7, and every finite omega. Leading and next rank hold on the vortical set. If the whole positive band is vortical and has the local symmetry and boundary data (2), all hypotheses above hold and the interface is excluded. An alternative sufficient premise is uniform velocity decay and the precise square-root derivative bound of A498/A601.

The proof needs local axisymmetry, zero swirl, the equator, nonzero radial boundary velocity and zero interface vorticity. It imposes no symmetry elsewhere in the profile, no A2 condition, no sign of S and no initial parity or analyticity. General latitude, nonzero polar boundary velocity, swirl and nonaxisymmetric local geometry remain outside its scope. A leading local germ remains possible when the next scalar equation is omitted, as A672 illustrates. Bare-decay nonexistence and the full transmission problem remain OPEN.

Dependencies are A670-A671 for the exact algebra, the indicated confirmed actual-tail and scalar theorems for that corollary, elementary implicit-function and ODE uniqueness theorems, and the displayed direct spherical identities. No numerical computation or formal build was needed for this reduction. The complete LIT170 source was read, and all six sections were independently reconstructed.
