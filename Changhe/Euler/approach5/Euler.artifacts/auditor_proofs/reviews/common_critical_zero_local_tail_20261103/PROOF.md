# Analytic local tails with an open set of common critical scalar zeros

Status: CONFIRMED A899-A900 as a local necessary-tail countertest. Global actual-tail realization and full-profile nonexistence remain OPEN, A901.

## 1. Statement and scope

Fix 2/5<c<1/2, any finite real omega, p=(1-c)/c>1, sigma=omega/c, Jx=e3 cross x, A=cI-omega J and E=(1-c)I+omega J. There is delta>0 and an analytic axisymmetric pair (V,P2) on the full azimuthal cone r>0, |theta-pi/2|<delta satisfying

    V(exp(tA)x)=exp(-tE)V(x),
    P2(exp(tA)x)=exp(-2(1-c)t)P2(x),
    div V=0, V.curl V=0,
    -Delta P2=partial_i partial_j(V_i V_j),
    k=(Ax).V=0, S=P2-|V|^2/2=0,
    V!=0, W=curl V!=0.

Thus W.grad S=0 and grad k cross grad S=0, and every point is a common critical zero of k and S. This is an exact local solution of the stated necessary tail equations. It is not a full local profile: at the unit equator the radial momentum residual is -(p+1)-2p sigma^2<0. No polar-cap extension, global canonical pressure, actual scattering realization or smooth extension at the origin is asserted.

The calculation specializes the checked positive-S construction A875-A876 in the team records. For clarity, the complete local construction with S=0 is included below; no unproved global existence statement is imported.

## 2. Divergence, vorticity and the zero scalars

In the orthonormal spherical frame set

    V=r^(-p)(f e_r+g e_theta+h e_phi),
    f=sigma sin(theta)h,
    g'=G=-cot(theta)g-(2-p)sigma sin(theta)h.

Divergence is r^(-p-1)((2-p)f+g'+cot(theta)g), so it vanishes. Since Ax=cr e_r-omega r sin(theta)e_phi, k=0. Direct differentiation gives

    W=r^(-p-1)((h'+cot(theta)h)e_r+(p-1)h e_theta
                       +((1-p)g-f')e_phi).

The g terms in V.W cancel. The remaining coefficient is f(h'+cot(theta)h)-hf'=0 for the displayed f. Set

    P2=|V|^2/2=r^(-2p)Pbar,
    Pbar=((1+sigma^2 sin(theta)^2)h^2+g^2)/2.

Then S=0 identically. The radial degrees and rotational equivariance of this axisymmetric field give the two twisted homogeneity laws. Poisson is the only equation still to solve.

## 3. An analytic ordinary differential construction

Put v=h' and f'=sigma(cos(theta)h+sin(theta)v). The matrix r^(p+1)DV in the spherical frame, with derivative columns, is

    M=[-p f, f'-g, -h;
       -p g, G+f, -cot(theta)h;
       -p h, v, f+cot(theta)g].

Consequently

    T=tr(M^2)=p^2 f^2+(G+f)^2+(f+cot(theta)g)^2
                     -2p g(f'-g)+2p h^2-2cot(theta)h v.

Because div V=0, the stress double divergence is r^(-2p-2)T. For the scalar pressure,

    Delta P2=r^(-2p-2)(Pbar''+cot(theta)Pbar'
                                      +2p(2p-1)Pbar).

Let D0=partial_theta+G partial_g+v partial_h, holding v fixed in this operator. Along g'=G,h'=v one has

    Pbar'=D0 Pbar,
    Pbar''=D0^2 Pbar+Pbar_h v',
    Pbar_h=(1+sigma^2 sin(theta)^2)h.

Thus Poisson is exactly the system

    g'=G, h'=v,
    v'=(-T-D0^2 Pbar-cot(theta)D0 Pbar
             -2p(2p-1)Pbar)/((1+sigma^2 sin(theta)^2)h).

At theta=pi/2 prescribe g=0,h=1,v=0. The right side is analytic near these data and its denominator is positive. Analytic ODE existence supplies a solution on a small interval about pi/2. Shrink this interval to keep h>0 and avoid the poles. Use the same coefficients for all azimuths. The field is analytic in Cartesian coordinates on the cone, since its spherical frame and coordinates have no singularity there. Its e_phi component and W's e_theta component prove V,W nowhere zero. The interval width may depend on c and omega; no uniform width is claimed.

## 4. Failure of the full momentum equation

Homogeneity implies DVAx=-EV. At the unit equator the initial data give V=sigma e_r+e_phi, W=(p-1)e_theta and Pbar=(1+sigma^2)/2. The first row of M gives

    e_r.DVV=-p sigma^2-1,
    e_r.grad P2=-2p Pbar=-p-p sigma^2.

Their sum is -(p+1)-2p sigma^2<0, which is the radial component of EV+DV(Ax+V)+grad P2. This exact nonzero residual does not depend on the second derivative chosen by the pressure ODE. The field also grows like r^(-p) toward the removed origin. The example is therefore not an actual local or whole-space profile.

## 5. Audit and limits

The complete six-section submitted LIT189 proof and the earlier five-section independent construction were read. The zero-scalar specialization preserves the nonzero highest-derivative coefficient, and the changed residual was recomputed. This entire proof was read after writing. The theoretical question is whether the local necessary tail equations alone exclude nonzero V,W on an open common critical zero set. The pass criterion is exact analytic local existence and a separate full-momentum failure, both established above. No computation or formalization was needed.

This disproves a local-only implication that k=S=0 forces irrotationality or zero velocity. It does not contradict A707, which concerns an actual global scattering tail with S identically zero throughout punctured space and uses the global core-return argument. It leaves global actual critical-node exclusion open. Existing configured model agent comparison continues; provider runtime is not independently attested.
