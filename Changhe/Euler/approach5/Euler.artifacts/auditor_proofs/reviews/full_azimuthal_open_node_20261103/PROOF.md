# An analytic open nodal tail on a complete azimuthal band

## 1. Exact local result

For every 2/5<c<1/2 and finite real omega, put p=(1-c)/c, sigma=omega/c, q=2p/(p-1), Jx=e3 cross x, A=cI-omega J and L=(1-c)I+omega J. There is a delta>0 and a real-analytic axisymmetric pair (V,P2) on the entire cone |theta-pi/2|<delta, r>0, with all azimuthal angles included, such that

    V(exp(tA)x)=exp(-tL)V(x), P2(exp(tA)x)=exp(-2(1-c)t)P2(x),
    div V=0, V.curl V=0, -Delta P2=partial_i partial_j(V_i V_j),
    W.grad S=0, grad k cross grad S=0,
    W=curl V, k=(Ax).V=0, S=P2-|V|^2/2>0, V!=0, W!=0.

The pair does not solve the full local momentum equation. At the unit equator its radial residual is -(3p+1)-2p sigma^2. This is a local necessary-tail countertest only. There is no extension to the origin, the polar caps or an actual global profile in the claim.

## 2. Divergence, curl and the transported scalar

Seek, in the orthonormal spherical frame,

    V=r^(-p)(f e_r+g e_theta+h e_phi), f=sigma sin(theta)h,
    g'=G=-cot(theta)g-(2-p)sigma sin(theta)h.

The divergence is r^(-p-1)((2-p)f+g'+cot(theta)g), hence vanishes. Since Ax=cr e_r-omega r sin(theta)e_phi, k=0 identically. Direct differentiation gives

    W=r^(-p-1)((h'+cot(theta)h)e_r+(p-1)h e_theta+((1-p)g-f')e_phi).

The g terms in V.W cancel, leaving f(h'+cot(theta)h)-hf', which vanishes for this f. For h>0, V is nonzero and the e_theta component of W is nonzero.

Set s(theta)=(sin(theta)h)^q and S=r^(-2p)s. Its logarithmic derivative is q(cot(theta)+h'/h), and (p-1)q=2p gives W.grad S=0 exactly. Rank is automatic from k=0. Define

    P2=r^(-2p)Pbar,
    Pbar=(sin(theta)h)^q+((1+sigma^2 sin(theta)^2)h^2+g^2)/2.

Then P2-|V|^2/2=S. All expressions are real analytic for 0<theta<pi and h>0, even for nonintegral q. Axisymmetry and degrees -p,-2p give the two twisted homogeneity laws, since pc=1-c and rotation transports the spherical frame equivariantly.

## 3. The pressure equation determines a nonsingular analytic ODE

Write v=h'. The matrix r^(p+1)DV, with derivative columns in the spherical frame, is

    M=[-p f, f'-g, -h;
       -p g, G+f, -cot(theta)h;
       -p h, v, f+cot(theta)g].

The last column follows from differentiating e_r,e_theta,e_phi with respect to azimuth and dividing by r sin(theta). Its signs give

    T=tr(M^2)=p^2 f^2+(G+f)^2+(f+cot(theta)g)^2
             -2p g(f'-g)+2p h^2-2cot(theta)h v.

This depends only on theta,g,h,v. Since div V=0, the stress double divergence is r^(-2p-2)T. The scalar Laplacian is

    Delta P2=r^(-2p-2)(Pbar''+cot(theta)Pbar'+2p(2p-1)Pbar).

Define D0=partial_theta+G partial_g+v partial_h, without differentiating v. Along g'=G,h'=v,

    Pbar'=D0 Pbar, Pbar''=D0^2 Pbar+Pbar_h v'.

Its highest-derivative coefficient is

    A0=Pbar_h=q sin(theta)^q h^(q-1)+(1+sigma^2 sin(theta)^2)h>0.

Thus the exact pressure equation is the explicit system

    g'=G, h'=v,
    v'=(-T-D0^2 Pbar-cot(theta)D0 Pbar-2p(2p-1)Pbar)/A0.

Prescribe g(pi/2)=0,h(pi/2)=1,v(pi/2)=0. The right side is analytic near these data with nonzero denominator, so the analytic ODE existence theorem supplies a solution on |theta-pi/2|<delta. Shrink delta to keep h>0 and avoid both poles. The Cartesian field is analytic on this cone because r and the spherical frame are analytic there. Using the same coefficients for every azimuth ensures genuine full azimuthal periodicity. No numerical solution, global pressure normalization or uniform lower bound on delta over all omega is used.

## 4. Direct failure of the full momentum equation

At the unit equator, f=sigma,g=0,h=1,f'=0, so

    V=sigma e_r+e_phi, W=(p-1)e_theta, S=1,
    Pbar=3/2+sigma^2/2.

Twisted homogeneity gives DVAx=-LV. Therefore the full momentum residual reduces to DVV+grad P2. The first row of M gives its convective radial part -p sigma^2-1, and the pressure radial derivative is -2p Pbar=-3p-p sigma^2. Their sum is

    -(3p+1)-2p sigma^2<0.

This proves, independently of the solved highest derivative, that the constructed pair is not a full local profile. Its nonzero homogeneous velocity also diverges at the removed origin.

## 5. Verification and limits

The complete seven-section LIT185 source was read and every spherical derivative, highest-derivative coefficient and residual term above was checked analytically. The local existence theorem is applied only after explicitly isolating v'. No computation or formalization was needed.

The basic all-omega open-node existence was already A840; this result adds a complete azimuthal band and an ordinary differential construction. It retains swirl. The actual swirl-free band theorem therefore does not apply, and the whole-sphere axisymmetric tail theorem has missing global domain and pressure premises here. Neither arbitrary-omega global nonexistence nor an actual counterexample follows. Existing configured model agent comparison continues, with runtime unattested.
