# An axisymmetric harmonic repair along the whole carrier circle

Status: CONFIRMED at the finite-jet scope below, A448, 2026-11-03T03:38:59.042000+00:00. Independent reconstruction of the coordinator's nonflat review Section3.4. The calculation concerns finite Euler jets along a complete circle. The displayed modified field is helicity free but fails the full Euler equation. It is not a global decaying construction.

## 1. Exact statement and notation

Fix 0<c<1/2,omega in R,integer k>=1,R>0,C!=0. Put gamma=(1+c)/k,D=2c+gamma,A0=3c+gamma. On r>0 take the confirmed A440 exact family

    U_r=-(c+gamma/2)r+gamma R^2/(2r), U_theta=0,
    U_z=Dz-C(r^2-R^2)^(k+1)/(2(k+1)).

Let S=r^2-R^2,alpha0=-D^2/(2cR), and define

    phi=alpha0/(8R^3) [S^3-(18S^2+12R^2S)z^2
                         +(24S+16R^2)z^4-(16/5)z^6],
    V=grad phi, U_tilde=U+V,
    B_tilde=(cI-omega J)y+U_tilde, W=curl U=curl U_tilde.

Then phi is a harmonic polynomial in Cartesian coordinates. V and DV vanish on the whole circle Gamma={r=R,z=0}. Therefore Gamma and its complete derivative cocycle are unchanged by this modification. For omega!=0 it remains one carrier orbit of least period2pi/abs(omega), with backward spectrum(gamma,0,-3c-gamma); for omega0 it remains a circle of equilibria. The field U_tilde is divergence free and has zero helicity everywhere in r>0.

At every p in Gamma it passes the necessary A442 second-jet rank test:

    grad g_tilde=-gamma u,
    Hess g_tilde+gamma DU
       =[(gamma^2+3D^2)/(c^2R^2)] u tensor u,
    u=U_tilde(p), g_tilde=U_tilde.B_tilde.

A single axisymmetric analytic pressure correction near Gamma makes full momentum vanish through transverse degree k+1 at every circle point; its added degree is at most k+2. This is a simultaneous finite-jet statement. The next curl residual has a nonzero homogeneous term of degree k+1, so the displayed velocity cannot be made an exact Euler solution by any pressure on a neighborhood of Gamma. The actual W remains azimuthal and has nearby closed vortex circles.

## 2. Harmonicity and the whole-circle jet

For an axisymmetric function F(s,z),s=r^2, the Cartesian Laplacian is

    Delta F=4(s F_ss+F_s)+F_zz.

Write the bracket in phi as S^3+b(S)z^2+e(S)z^4+f z^6 with

    b=-18S^2-12R^2S, e=24S+16R^2, f=-16/5.

The radial Laplacian of S^3 is36S^2+24R^2S, canceled by2b. The radial Laplacian of b is-288S-192R^2, canceled by12e. The radial Laplacian of e is96, canceled by30f. There are no remaining terms. Thus phi is harmonic for every parameter, without a finite-sample inference.

In transverse coordinates delta=r-R,z at a circle point,

    phi=alpha0(delta^3-3delta z^2)+O((abs(delta)+abs(z))^4).

Hence V vanishes to order2 all along Gamma, so V=DV=0 there. In a fixed Cartesian frame at p=(R,0,0),delta=X+O(abs((X,Y,Z))^2); the cubic leading term is precisely alpha0(X^3-3XZ^2), the A443 point repair. Thus the velocity second jet at p is the same as that repaired jet. Rotation around the fixed z-axis takes this identity to every point of Gamma because both phi and the original field are equivariant and A commutes with those rotations.

In particular U,DU,B and DW on Gamma are unchanged. The derivative of a flow along a fixed orbit solves its variational equation using only DB on that orbit, so its full derivative cocycle is identical. This is stronger than preservation of instantaneous eigenvalues at one point. The cocycle statement makes no completeness assertion away from Gamma.

## 3. Rank test and helicity

At p=(R,0,0), write fixed orthonormal directions e_r,e_theta,e_z. The original circle data are

    u=-cR e_r, B=-omega R e_theta,
    DU=diag(-c-gamma,-c,D),
    grad g=-gamma u, Hess g+gamma DU=diag(gamma^2,0,3D^2).

The quadratic part of g_tilde-g=(B+U).V+abs(V)^2 is

    (B(p)+u).V_2=(3D^2/2)(X^2-Z^2).

Its Hessian is diag(3D^2,0,-3D^2), proving the asserted rank identity at p. Rotation then proves it at every circle point with the same scalar multiplier. W and D(B cross W) along Gamma are unchanged as well.

Because V is a gradient, W is unchanged on the whole local domain. More explicitly

    W=C r S^k e_theta.

Both U and V are meridional, so U_tilde.W=0 identically. This is an actual helicity-free field, unlike the one-point repair. It is still not an Euler solution.

## 4. Simultaneous finite-order momentum and its failure at the next curl order

Let R(U)=(1-c)U+((cI-omega J)y+U).grad U+omega JU. Axisymmetry cancels the actual Cartesian rotation contributions for both fields, and R(U_tilde)-R(U) is meridional. The curl difference is exactly

    curl(R(U_tilde)-R(U))=[V,W].

For an axisymmetric meridional V and W=w(r)e_theta, differentiation of the cylindrical basis gives

    [V,W]=(V_r w_r-V_r w/r)e_theta
           =2C k r^2 S^(k-1)V_r e_theta.                 (1)

In particular the term -V_r w/r is essential. With V_r=3alpha0(delta^2-z^2)+O((abs(delta)+abs(z))^3), the leading term of(1) is

    6C k R^2 (2R)^(k-1)alpha0
          delta^(k-1)(delta^2-z^2)e_theta.               (2)

It is a nonzero homogeneous polynomial of degree k+1, since all its scalar factors are nonzero. Thus no pressure can make the displayed U_tilde solve full Euler even on an arbitrarily small open tube about Gamma.

For completeness, the lower finite-jet assertion can be made with one pressure throughout the tube, rather than unrelated polynomials at its points. Use the transverse coordinates(delta,z). Let T_j be the degree-j homogeneous meridional Taylor part of R(U_tilde)-R(U) at(R,0), with its radial and vertical components in this coordinate pair. The constant and linear parts vanish: V has order2 and X=cy+U vanishes on Gamma, so every term of the rotation-canceled residual difference has order at least2. Equation(1) shows

    partial_delta (T_j)_z-partial_z (T_j)_r=0,
                  0<=j<=k+1.

For each j a potential is [delta(T_j)_r+z(T_j)_z]/(j+1), by the homogeneous Euler identity and the zero-curl relation. Set

    p_corr=-sum_(j=2)^(k+1)
                [delta(T_j)_r+z(T_j)_z]/(j+1).

This is a polynomial in(delta,z), hence an axisymmetric single-valued analytic function on a sufficiently small full tube where r>0. Adding it to the original exact pressure cancels residual components through degree k+1, uniformly around Gamma. Transverse order implies the same Cartesian Taylor vanishing at each circle point by the analytic coordinate change. Formula(2) shows why no degree-(k+2) residual cancellation can then succeed for this fixed U_tilde.

## 5. Exact scope and verification

The complete polynomial, bracket and pressure argument above is by hand and requires no new computation. The coordinator's original Section3.4 and its numerical/symbolic checks are pinned as the submitted review, with their exact stated parameter scopes. The all-parameter conclusions here follow from the displayed analytic formulas, not from those finite tests. Its offered C3 rank-test calculations are not used or certified by this reconstruction.

This construction proves only that A442's first differentiated rank test can be satisfied along a whole carrier circle with the original cocycle and with Euler-compatible finite jets. It does not refute A442, A445, the proposed periodic-negative exclusion, or A014. Its nearby closed W curves would forbid a global uniformly sublinear Euler extension if it were itself an exact germ; it already fails the local equation by(2). No global growth bound or target counterexample follows.
