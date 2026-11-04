# Arbitrarily high analytic scalar nodal order on an angular band

Status: CONFIRMED at the exact conditional or countertest scopes in A599. Full independent proof postread completed. The unrestricted campaign conjecture is not proved.

## 1. Exact statement

Fix p>1, c=1/(p+1), omega real, t=omega/c, beta=(p-1)/(2p), a=1-2c, Jx=(-x2,x1,0), A=cI-omega J, any positive integer N and any epsilon>0. There is a periodic equatorial band D_delta={x!=0: |x3|/|x|<delta} with real analytic V,P2, twisted homogeneous of degrees-p and-2p, satisfying div V0, V.curl V0, k=(Ax).V0, local Poisson -Delta P2=partial_i partial_j(V_iV_j), W.grad S0 and rank grad k cross grad S0, where W=curl V and S=P2-|V|^2/2. At a point x0 in that band V and W are nonzero and

    S=g eta^(2N), g>0 analytic, eta analytic, grad eta!=0.

Thus if2N beta>=1, |S|^-beta is not locally integrable. The field is nonaxisymmetric and its radial component has zero azimuthal mean at every latitude.

## 2. Exact analytic construction

Use r=|x|, z=cos theta, w=1-z^2, chi=phi+t log r and

    V=r^-p[tF e_r+H/sqrt(w)e_theta+F/sqrt(w)e_phi],
    S=r^-2p h, P2=r^-2p(h+e),
    e=[(1/w+t^2)F^2+H^2/w]/2.

The complete independent derivation of every matrix entry, angular equation and highest-derivative coefficient is in the team records Sections3-4 (A590). Explicitly alpha=1/w+t^2, d=(2-p)t, D0=F_z+H_chi/w, and the remaining equations are

    A0=H_z-alpha F_chi-dF=0,
    B0=2p h D0-(p-1)(Fh_z+Hh_chi/w)=0,
    P0=L(h+e)+tr(M^2)=0,
    L=(w partial_z)_z+alpha partial_chichi
                      +t(1-4p)partial_chi+2p(2p-1).

Here M is the explicitly derived spherical-frame matrix r^(p+1)DV in that proof. Its trace gives divergence, its antisymmetric part gives actual curl, and Ax cross W=aV is an identity of the ansatz, proving helicity and k0. With A0=0 the pressure equation is exactly local Poisson.

Solve partial_z A0=partial_z B0=P0=0 for the pure second derivatives(H_zz,F_zz,h_zz). The coefficient matrix is

    [1,0,0; 0,2ph,-(p-1)F; H,w alpha F,w],

whose determinant is w[2ph+(p-1)alpha F^2]. Set the analytic Cauchy data at z0 to

    F=sin chi, H0, h=epsilon cos^(2N)chi,
    F_z0, H_z=(1+t^2)cos chi+d sin chi, h_z0.

Then A0=B0=0. The determinant factor is

    2p epsilon cos^(2N)chi+(p-1)(1+t^2)sin^2chi>0

on the whole initial circle. Both terms are nonnegative and cannot vanish together. Every other derivative on the right after matrix inversion has total order at most2 and normal order at most1. The primary Cauchy-Kovalevskaya theorem, Gantumur Theorem18/Corollary20 printed9-11, therefore applies with its exact normal-order hypotheses. The primary statements and proofs have been read. Local holomorphic extensions exist and the determinant remains nonzero near each real initial point. Analytic uniqueness patches the solutions on overlaps; compactness supplies a common band. Uniqueness under2pi shifts and complex conjugation gives periodicity and reality.

The differentiated constraints remain constant in z, so their zero initial values restore A0=B0=0. This is a convergent analytic solution of the undifferentiated equations, not a finite jet or numerical fit.

## 3. The nodal order holds in a neighborhood

At z0,chi=pi/2, F1, so F stays nonzero on a smaller rectangle. For the already constructed analytic solution the scalar equation is

    h_z+[H/(wF)]h_chi=[2p D0/((p-1)F)]h.

Solve the analytic characteristic equation dchi/dz=H/(wF), chi(0)=xi. Its map(z,xi) to(z,chi) is a local analytic diffeomorphism. Along it,

    h(z,chi(z,xi))=epsilon cos^(2N)xi
       exp(integral_0^z [2p D0/((p-1)F)](s,chi(s,xi)) ds).

The exponential is analytic and strictly positive on the real rectangle. Since cos xi has a simple zero at pi/2, the right side equals a positive analytic factor times(xi-pi/2)^(2N). The inverse characteristic coordinate eta=xi(z,chi)-pi/2 has nonzero differential. Passing to Cartesian coordinates on the band, with chi=phi+t log r and the positive factor r^-2p, gives the claimed three-dimensional factorization. This proves exact surface multiplicity, not merely a high order on the initial slice.

At r1,z0,chi=pi/2, the actual curl formula of A590 gives V=t e_r+e_phi and W=(p-1)e_theta, both nonzero. In coordinates(eta,two tangential variables), the volume Jacobian is bounded above and below by positive constants. Therefore b=|S|^beta is comparable to |eta|^(2N beta), and its reciprocal is not integrable when2N beta>=1. Any fixed p>1 allows such an integer N.

## 4. Symmetry and scope

The equations and data are preserved by(F,H,h)(z,chi) to(-F,-H,h)(z,chi+pi). The matrix M changes sign, e and tr(M^2) do not, and A0,B0 each change sign. Analytic uniqueness gives F,H antiperiodic under chi->chi+pi and h periodic under that shift. Thus F and tF have zero azimuthal mean at each latitude. At z0 the coefficient F=sin chi depends on azimuth, proving vector nonaxisymmetry even when omega0.

At a nodal point P2=|V|^2/2>0. This is compatible with the negative GLOBAL spherical mean of S in A591; a negative average imposes no pointwise prohibition there. The omitted poles, global canonical pressure and arrangement of nodes are substantive unresolved matching conditions. The example excludes an automatic nodal-order or A2 theorem derived from local analyticity and these local tail equations alone. It does not exclude a global theorem using additional information. No full nonlinear profile momentum equation is solved, and no computation is used.
