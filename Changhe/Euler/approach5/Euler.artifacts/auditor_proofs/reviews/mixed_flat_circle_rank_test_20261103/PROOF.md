# Mixed flat circles: the ambient rank obstruction and a limited repair

Status: independent reconstruction of LIT107. Full mathematical checks are written below. The complete focused configured-model review and the full corrected reconstruction have been read. CONFIRMED as A491 at the exact scope below. This is a local jet calculation and a necessary global test, not an exact repaired Euler germ.

## 1. Exact statement and dependencies

Fix 0<c<1/2, omega in R, an integer k>=3, R>0 and Q!=0. Let

    a=1-2c, d=3c, kappa=1+c,
    lambda=(1+4c)/(k-2), D0=2c+lambda,
    A=cI-omega J, B=Ay+U, W=curl U, g=U.B.

On a full small tube about Gamma={r=R,z=0}, define the analytic coordinate x by

    r^2=R^2+2R integral_0^x [1+Q s^k]^(-1) ds,
    q=Qx^k,
    b_r=-lambda R x/[r(1+q)],
    D=D0-lambda kq/(1+q),
    U=(b_r-cr)e_r+D z e_z.                           (1)

Here b_r is a scalar carrier component. The inverse analytic coordinate exists because dr/dx=1 at x=0. A459 proves that(1), with the single-valued analytic pressure

    P=-integral_R^r [(1-c)(b_s-cs)+b_s(b_s-cs)'] ds
          -D0(1+D0)z^2/2,                            (2)

is an exact local rotating Euler profile, with no swirl and zero helicity. In(2), b_s is the radial component as a function of its scalar argument s.

The claims checked here are:

1. At any p in Gamma, its second velocity jet violates the necessary ambient rank identity for a global C2 uniformly sublinear helicity-free Euler profile at a point in closure{curl U!=0}. The same c,omega and spatial point are required in this comparison.
2. The explicit harmonic potential in Section3 changes that second jet to satisfy this rank test on the whole circle. It preserves U,DU and every actual vorticity derivative there, and preserves the full carrier derivative cocycle along the circle.
3. One single-valued analytic pressure correction cancels momentum through transverse degree k+1. The displayed corrected velocity nevertheless has a nonzero curl residual of degree k+1 and is not an exact Euler germ.
4. Its actual vorticity is zero on the stable cylinder. A tangency conclusion alone therefore cannot supply the nonzero stable derivative used in A462.

The global test is A413/A442. A014 is used only for the separate nonextension of the original exact germ, which has closed vortex circles. No global extension or exact Euler solution is asserted for the repaired field.

## 2. The original second jet

Set delta=r-R. Since k>=3, inversion of(1) yields

    x=(r^2-R^2)/(2R)+O(delta^(k+1)),
    b_r=-lambda(r^2-R^2)/(2r)+O(delta^(k+1)).

Consequently, at r=R,

    b_r=0, b_r'=-lambda, b_r''=lambda/R,
    D=D0, D'=D''=0.

At p, in the Cartesian orthonormal basis(e_r,e_theta,e_z),

    u=U(p)=-cR e_r,
    M=DU(p)=diag(-c-lambda,-c,D0).                   (3)

The middle entry is U_r/r=-c; omitting this curvilinear contribution would give the wrong Cartesian matrix. The scalar g is independent of theta and omega:

    g=(b_r-cr)b_r+D(c+D)z^2.

Direct differentiation gives

    g_r=cR lambda,
    g_rr=2lambda^2+c lambda,
    g_zz=2D0(c+D0), g_rz=0.

The Cartesian tangential Hessian entry is g_r/R=c lambda. Therefore

    grad g=-lambda u,
    Hess g+lambda M=diag(lambda^2,0,3D0^2).           (4)

The exact vorticity is

    W=lambda k^2 Q r x^(k-1)z/[R(1+q)] e_theta
      =C delta^(k-1)z e_theta+O((|delta|+|z|)^(k+1)),
    C=lambda k^2 Q.                                 (5)

Indeed x'=r(1+q)/R, D'=-lambda k^2 Q r x^(k-1)/[R(1+q)] and W_theta=-D'z. In particular W=DW=0 on Gamma, so D(B cross W)=0 there.

For a global profile satisfying the stated C2, sublinearity and helicity hypotheses, A413's rank tensor and its C1 ambient closure extension give at a vortical-closure point with U!=0 and W=D(B cross W)=0

    grad g=rho U,
    Hess g-rho DU=tau U tensor U.                   (6)

The second velocity jet fixes every term in(6), since g=U.(Ay+U). In a matching jet(4) forces rho=-lambda. Its vertical Hessian remainder is3D0^2>0, whereas u tensor u has zero vertical component. This proves the claimed impossibility at a closure point. No conclusion is taken at points outside the closure of the vortical set.

## 3. A harmonic correction and its exact rank effect

Put S=r^2-R^2 and b0=-D0^2/(2cR), and let

    phi=b0/(8R^3)[S^3-(18S^2+12R^2 S)z^2
                       +(24S+16R^2)z^4-(16/5)z^6],
    V=grad phi, U_tilde=U+V.                        (7)

For an axisymmetric F(S,z),

    Delta F=4[(S+R^2)F_SS+F_S]+F_zz.

The radial Laplacians of the three successive coefficients in(7) are36S^2+24R^2S, -288S-192R^2 and96. They cancel, respectively, twice the z^2 coefficient, twelve times the z^4 coefficient and thirty times the z^6 coefficient. Thus Delta phi=0 exactly.

The first transverse term of phi is b0(delta^3-3delta z^2). It follows that V=DV=0 at every point of Gamma. At p=(R,0,0), in fixed Cartesian displacement(X,Y,Z),

    V_2=(3b0(X^2-Z^2),0,-6b0 XZ).

The quadratic term of g_tilde-g=(B+U).V+|V|^2 is(B(p)+u).V_2. Since B(p)=-omega R e_theta and(V_2)_theta=0, this equals

    -3cR b0(X^2-Z^2)=(3D0^2/2)(X^2-Z^2).

The Hessian change is diag(3D0^2,0,-3D0^2). Hence

    grad g_tilde=-lambda u,
    Hess g_tilde+lambda M
       =[(lambda^2+3D0^2)/(c^2R^2)]u tensor u.        (8)

Rotation equivariance makes this one calculation valid around all of Gamma. Harmonicity preserves div U=0. Since curl V=0, the actual vorticity is unchanged everywhere, not only through finitely many jets. Both velocities are meridional, so both have identically zero helicity. V=DV=0 on Gamma preserves the carrier and its full variational equation there. For omega!=0 the same nonstationary orbit has backward exponents(lambda,0,-d-lambda), by A459. For omega=0 it consists of equilibria; no nonstationary measure is inferred in that case.

## 4. First curl residual and the finite pressure correction

For any divergence-free velocity define

    N(U)=(1-c)U+((Ay+U).grad)U+omega JU.

The exact curl identity is curl N(U)=kappa W+[B,W]. Adding V leaves W unchanged, so

    curl[N(U+V)-N(U)]=[V,W].                        (9)

For V axisymmetric meridional and W=w e_theta, differentiating the cylindrical basis gives

    [V,W]=[V_r(partial_r w-w/r)+V_z partial_z w]e_theta.

Here V_r=3b0(delta^2-z^2)+O((|delta|+|z|)^3), V_z=-6b0 delta z+O((|delta|+|z|)^3), and(5) gives the leading degree k part of w. The term V_r w/r has degree at least k+2. The degree k+1 part of(9) is therefore

    3b0 C delta^(k-2)z[(k-3)delta^2-(k-1)z^2]e_theta. (10)

Its coefficient of delta^(k-2)z^3 is -3b0 C(k-1), which is nonzero for every allowed parameter. The special cancellation of the delta^k z coefficient at k=3 does not cancel this term. No scalar pressure can remove a nonzero curl, proving that this fixed repaired field is not an exact Euler germ.

The finite momentum statement has one degree of separation from the curl statement. Rotation cancels identically for each axisymmetric vector field, so E=N(U+V)-N(U) is a meridional analytic vector field in(delta,z). Its degree0 and degree1 parts vanish: V starts in degree2 and the meridional part of cy+U vanishes on Gamma. Let T_j denote the homogeneous degree j pair(E_r,E_z). Since curl E has no degree below k+1,

    partial_delta(T_j)_z=partial_z(T_j)_r
                   for every 0<=j<=k+1.

A curl-free homogeneous pair of degree j has potential

    [delta(T_j)_r+z(T_j)_z]/(j+1),

as follows by differentiating and using Euler's homogeneous identity. Consequently

    p_corr=-sum_(j=2)^(k+1)
                  [delta(T_j)_r+z(T_j)_z]/(j+1)      (11)

cancels every momentum coefficient through degree k+1. This is one finite polynomial in(delta,z), and thus a single-valued analytic axisymmetric pressure on a full tube, where r>0. Its degree is at most k+2. The residual curl(10) comes from the subsequent degree k+2 momentum and cannot be changed by(11). There is no conflict between the two degree statements.

## 5. Stable-cylinder scope and limits

For the exact starting carrier, B_r=b_r and B_z=(c+D)z. When omega!=0, Gamma is hyperbolic, z=0 is its forward stable cylinder and r=R is its unstable cylinder. Formula(5) vanishes on both cylinders. Since phi is even in z, the correction preserves z=0. The linear normal rates on Gamma are unchanged, so a sufficiently small part of z=0 remains its stable cylinder, and W is still identically zero there. The corrected unstable cylinder is not r=R. Its graph and the nonzero vorticity on it are computed in Section6; r=R remains only a zero set of the unchanged vorticity.

Thus tangency of W to the stable cylinder supplies no nonzero stable derivative in this example. Nearby points with xz!=0 have nonzero azimuthal vorticity, and its nonconstant integral curves are closed circles. A014 already prohibits global uniformly sublinear extension of the whole original exact germ. The displayed repaired field is not exact Euler. Its nonzero residual is not an obstruction to extending the finite jet, because the leading residual is nonresonant and removable by higher velocity terms, as detailed below.

At k=3, lambda=1+4c exceeds2(1-2c) for c>1/8. In particular, throughout the target interval, this large preserved backward rate coexists with the displayed rank test on Gamma, unchanged actual curl and vanishing momentum jets through degree4. It does not give an exact local realization of all global rank identities, arbitrary finite-order Euler realization at this fixed spectrum, or a target counterexample.

No computation is needed. All degree counts, Cartesian Hessians, signs and pressure primitives above were checked directly. The submitted source is pinned alongside this reconstruction. The complete focused review checked the precise closure hypothesis, the difference between a second-jet global obstruction and whole-germ nonextension, and the one-degree curl/momentum distinction. Its findings are independently incorporated in Section6.

## 6. Focused review, exact residual and the corrected unstable cylinder

The full coordinator review is pinned in the team records. Its core formulas were independently checked against Sections2-4. The A442 pass is only at points of Gamma; no rank identity on an entire neighborhood is claimed. A second jet without the vortical-closure premise is realized by an irrotational harmonic-gradient profile, so that premise remains essential.

For the harmonic correction V=grad phi one has the exact identity

    N(U+V)-N(U)=grad[a phi+(Ay).V+U.V+|V|^2/2]-V cross W.

To prove it, use (V.grad)V=grad|V|^2/2, (U.grad)V+(V.grad)U=grad(U.V)-V cross W, and symmetry of DV. Since A^T=cI+omega J, the remaining linear terms are grad[a phi+(Ay).V]. Thus the analytic pressure P_tilde=P-a phi-(Ay).V-U.V-|V|^2/2 leaves exact residual W cross V, and H_tilde=H-a phi. It starts at degree k+2 and its curl has the nonzero degree-(k+1) term already computed. This proves only that this displayed velocity cannot be made exact by changing pressure.

The leading vorticity operator on delta^i z^j e_theta has coefficient kappa-lambda i+(d+lambda)j. The two residual monomials delta^k z and delta^(k-2)z^3 have coefficients-lambda and2d+3lambda=3D0, both nonzero. A correction to vorticity at degree k+1 therefore cancels that residual, with a divergence-free meridional velocity correction at degree k+2, without changing the velocity(k+1)-jet. At this formal degree such a velocity is obtained from a planar stream potential whose degree-(k+3) Laplacian is the prescribed polynomial; the planar polynomial Laplacian is onto. Curvature changes only higher terms. No all-order continuation or convergence conclusion is taken. The review's additional two-order computations and its proposed higher rank obstruction are not needed for the present theorem and are not independently certified here.

The zero set r=R is preserved as a zero set of W but is not invariant for the corrected carrier: B_tilde,r(R,z)=-3b0 z^2+O(z^4), with b0 nonzero. In the meridional plane the corrected saddle has unstable graph delta=h2 z^2+O(z^4). Substitution in h'(z) B_tilde,z=B_tilde,r gives (2d+3lambda)h2=-3b0 and hence h2=D0/(2cR)>0. The exact factorization W=C delta^(k-1)z(1+O(delta)) e_theta then gives W=C h2^(k-1)z^(2k-1)+O(z^(2k+1)), which is nonzero on that unstable graph away from Gamma. In contrast z=0 is the stable invariant cylinder and W vanishes there. Rotation equivariance extends these planar statements to the whole circle, also when omega=0.

Finally lambda^2+3D0^2=2|M|_F^2, by D0=2c+lambda. The corrected second jet therefore satisfies the full flat Hessian law, not just its rank-one remainder. This is still only circle-level second-order data and finite momentum compatibility. It neither constructs an exact corrected germ nor proves an obstruction at general flat periodic orbits.
