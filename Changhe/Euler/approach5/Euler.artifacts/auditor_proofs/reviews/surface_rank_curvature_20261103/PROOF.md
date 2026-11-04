# The rank identity on an actual invariant surface

Status: CONFIRMED as exact local rank identities and restricted surface exclusions, A751-A753. No general flat periodic Euler witness is excluded.

## 1. Exact setting and conclusion

Let c>0,c!=1/2 and omega be any finite real number. Put a=1-2c and A=cI-omega J. On an open subset of Euclidean R3 let U and P be C1 and solve

    (1-c)U+DU(Ax+U)+omega JU+grad P=0, div U=0.

Write B=Ax+U,W=curl U,H=P+|U|^2/2+(Ax).U,g=U.B. Let S be an oriented embedded C2 surface, with unit normal n, to which B and W are tangent. Assume U.W=0 on S and that T=U-q n is nonzero on the surface patch, where q=U.n. Let M=DU and define the shape operator K(v)=-D_v n on tangent vectors. The second fundamental form is II(v,w)=K(v).w. Define

    ell=n.Mn,
    mu=-(T.g)/(a|T|^2),
    F=mu g-g-|T|^2,
    Q=B.q+2T.q+2II(T,T)+q(ell+c+a mu).              (1)

The derivatives B.q and T.q are derivatives of the scalar trace q along S. The matrix entry ell uses only the value of n at the point and the ambient first derivative of U. All quantities in (1) are continuous under the given regularity.

At every point of S where dH wedge dg=0,

    F W=Q(n cross T).                               (2)

If Gamma is a compact subset of the patch with g=0, then F=-|T|^2 is uniformly separated from0 there and in a sufficiently small surface neighborhood. If Q vanishes throughout this neighborhood and rank holds at every vortical point of the neighborhood, W vanishes on that surface neighborhood. In particular this follows from q=0 and II(U,U)=0 throughout it. These are additional surface hypotheses, not consequences claimed for a general Euler profile.

## 2. Exact Lamb and curl identities

For our convention M_ij=partial_j U_i,

    B cross W=(M^T-M)B,
    grad H=grad P+M^T B+A^T U.

Since A^T+aI=(1-c)I+omega J, the momentum equation is exactly equivalent to

    grad H=-aU+B cross W.                            (3)

All terms are classical at C1 regularity. Also n cross W=(M^T-M)n. For a tangent vector v, differentiating q=U.n along S gives

    n.Mv=v.q+II(v,T).

Consequently the tangential part of Mn is

    (Mn)_tan=grad_S q+KT-n cross W.                 (4)

No extension of n off the surface is used. Formula (4) follows by pairing with all tangent v. Since B and W are tangent, n cross W is tangent as well.

## 3. The normal work derivative and cancellation of rotation

Let D=n.(B cross W) and E=n.(T cross W). Differentiate g=U.(Ax+U) in the ambient direction n at a point. Then

    n.g=(Mn).(B+U)+U.An.

Substitute U=T+qn and (4). The cross-product term has sign

    -(n cross W).(B+T)=D+E.

It follows that

    n.g=(B+T).q+II(T,B+T)+D+E+q ell+T.An+cq.        (5)

The normal component of Ax is -q because B is tangent, while its tangential component is B-T. Differentiating n.Ax=-q along T gives

    -II(T,B-T)+n.AT=-T.q.

The identity A+A^T=2cI and T.n=0 give T.An=-n.AT. Hence

    T.An=T.q-II(T,B-T).

Insert this in (5). Symmetry of II cancels the mixed terms, leaving

    n.g=B.q+2T.q+2II(T,T)+q(ell+c)+D+E.             (6)

This calculation keeps every contribution from normal velocity and curvature. The skew part of A cancels exactly; omega is unrestricted.

## 4. Rank determines the vorticity coefficient

Equation (3) gives grad_S H=-aT and n.H=-aq+D. Since a!=0 and T!=0, grad H is nonzero. At a rank point dg=mu dH, with exactly the scalar mu in (1), obtained by pairing with T. Therefore

    n.g=mu(-aq+D).                                  (7)

Since W is tangent and U.W=0, T.W=0. In the oriented two-dimensional tangent plane,

    W=(E/|T|^2)(n cross T),
    D=(g/|T|^2)E.                                  (8)

For the second identity use g=T.B and decompose B along T and n cross T. Equating (6) and (7), and then using (8), gives

    ((mu-1)g-|T|^2)E=|T|^2 Q,

which proves (2). This calculation is valid also if W=0 at a rank point. If rank is given only on the vortical set, it is used only at a hypothetical vortical point. The functions F and Q are defined and continuous on the whole patch, so the compact nonvanishing argument for F requires no extension of rank into an open irrotational region.

If g=0 on compact Gamma, the positive minimum of |T| on Gamma gives F<=-min_Gamma|T|^2 there. Continuity gives an open surface neighborhood with F!=0. If Q=0 there, any vortical point there would have W=0 by (2), a contradiction. This proves the restricted exclusion.

## 5. Incompressibility and the geometric obstruction that remains

At any point choose an orthonormal tangent pair v1,v2. Summing vi.Mvi gives div_S T-q tr K, whereas the normal entry is ell. Thus div U=0 gives

    ell=-div_S T+q tr K,
    Q=B.q+2T.q+2II(T,T)
                     +q(c-div_S T+q tr K+a mu).     (9)

This derivation is pointwise and does not require a C2 extension of n or an extra derivative of U. If q=0 throughout the patch, its surface derivatives vanish and Q=2II(U,U). A planar patch has II=0. For a curved invariant cylinder there is no reason supplied here for II(U,U), the derivatives of q, or q ell to vanish or have a fixed sign. The identity therefore records a compatibility condition, not an exclusion of a general cylinder.

At a flat zero-work carrier orbit lying in the rank closure, (2) implies Q=0 on the orbit when T!=0. Continuity alone does not make Q vanish on nearby loops. No conclusion about off-surface vortical accumulation follows even when W vanishes on S.

## 6. Direct radial trace theorem at C1 regularity

The special radial argument needs still fewer premises. In the Euclidean coordinates

    x=((R+h)cos(theta),-(R+h)sin(theta),z), r=R+h>0,
    volume=r dtheta dh dz,

suppose on z=0 that U=u(h) partial_h and W=w(theta,h) partial_theta, with u C1 and w continuous. Put b=cr+u and assume b(0)=0. Assume rank at the vortical points; helicity need not be separately assumed in a surrounding neighborhood. On the annulus B=omega partial_theta+b partial_h. The coordinate curl gives

    partial_z U^h=-r w, partial_z U^theta=0.

The first identity uses partial_h U^z=0 on the central trace, and the second uses W^h=0 and partial_theta U^z=0 there. Equations (3) and g=U.B now give

    H_h=-a u, H_z=-r b w,
    g_h=u'b+u b', g_z=-r w(b+u).

Thus the dh wedge dz coefficient of dH wedge dg is

    r w F0(h),
    F0=a u(b+u)+b^2 u'+bu b'.                       (10)

At h=0, u=-cR and F0=a c^2 R^2!=0. By continuity F0 is nonzero on a smaller interval, uniformly in theta. At any central point there with w!=0 the rank identity contradicts (10). Hence w vanishes on that entire central annulus. No derivative of w, higher transverse jet, division by w or global function g=G(H) is needed. If omega!=0 the central circle is a carrier orbit; if omega=0 it is a circle of equilibria. Both cases are covered.

This proves the lower-regularity LIT118 theorem and independently extends Section4 of in the team records. It excludes the particular nonzero radial traces considered in LIT116-LIT117 under rank. It does not exclude vorticity just off the annulus or a general nonradial or curved stable cylinder.

## 7. Sources and verification

The entire LIT118 and LIT119 source proofs were read and retained in verification. All identities have been independently reconstructed above, including the curl sign, normal derivative of work, affine skew cancellation, multiplier definition, curvature sign and exact C1 regularity. No computation or external theorem is used. A413 is relevant only to the separate global helicity-free uniformly sublinear C2 application, where it supplies rank; it does not supply the required surface geometry or radial traces.

Focused configured-model review is requested through the existing file exchange. The general W2 witness, pointwise derivative decay and arbitrary-sign nonexistence remain OPEN. No numerical evidence is used as proof.
