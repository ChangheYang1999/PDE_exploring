# A zero-velocity carrier equilibrium has an irrotational neighborhood

Status: CONFIRMED as A478 at 2026-11-03T04:59:54.883072+00:00. The complete source proof, configured-model coordinator review and this independent reconstruction have been read and checked in full. The main decay-only conjecture remains open.

## 1. Exact local theorem and global application

Let U be C2 on a neighborhood of0 in R3, with div U=0 and U(0)=0. Fix0<c<1/2 and any finite real omega, and put

    A=cI-omega J, B(x)=Ax+U(x), W=curl U,
    a=1-2c, kappa=1+c, g=U.B,
    J(x1,x2,x3)=(-x2,x1,0).

Assume U.W=0 on that neighborhood and that a scalar H satisfies

    grad H=-aU+B cross W,
    (B.grad)W=(DB-kappa I)W.                          (1)

The gradient in (1) is C1, so H is C2 locally. Finally assume the rank identity

    grad H cross grad g=0 on O={W!=0}                 (2)

near0. Then W is identically zero on some neighborhood of0. The theorem requires neither uniform sublinearity nor a globally complete flow. It uses only local identities and local rank (2).

For a global C2 rotating incompressible Euler profile with C1 pressure, U=o(|y|) uniformly,0<c<1/2,any omega, and U.curl U=0 everywhere, A413 supplies (2). Its Lamb and vorticity identities supply (1). Thus if U(0)=0, the origin is separated from the vortical set. Since A is invertible, a carrier equilibrium with U=0 must be the origin. Consequently every carrier-equilibrium witness in the global helicity-free A471 alternative is at a nonzero spatial point and has U!=0. This does not exclude those remaining equilibria or flat periodic witnesses.

## 2. The vorticity and two symmetric matrices at0

Write M=DU(0), w=W(0). Differentiating U.W=0 at0 gives M^T w=0, since U(0)=0. For the Jacobian convention DU acting on vectors,

    M-M^T=[w]_cross,

so Mw=M^Tw=0. The equilibrium instance of (1) gives

    (A+M)w=kappa w, Mw=w+omega Jw.

Taking the scalar product with w yields |w|^2=0 because J is skew. Hence w=0, M is symmetric, and tr M=0.

Set F0=A+M and

    N=M F0+F0^T M
      =2M^2+2cM+omega(JM-MJ).                         (3)

The matrix N is symmetric and tr N=2|M|_F^2. Uniformly near0, Taylor estimates at the stated C2 regularity give

    grad H=-aMx+O(|x|^2), Hess H=-aM+O(|x|),
    grad g=Nx+O(|x|^2), Hess g=N+O(|x|).              (4)

Here U,B,W vanish at0, U and B are C2, and W is C1. In Hess H, the derivative of B cross W is DB cross W+B cross DW=O(|x|). In Hess g, all terms containing D2U have a factor U or B and are O(|x|); all remaining first derivatives differ from their origin values by O(|x|). No third derivative of U is needed.

Define the homogeneous quadratic map Q(x)=(Mx) cross (Nx). Differentiating the cross product of the two gradients in (4) gives

    D(grad H cross grad g)(x)=-a DQ(x)+O(|x|^2).

The set O is open and (2) holds identically there. Its derivative is therefore zero at each point of O. Since a!=0,

    ||DQ(x)||<=C|x|^2 for x in O near0.               (5)

The linear map x -> DQ(x) is the extra information obtained by differentiating rank on the open vortical set. A rank identity only at a limiting point would not give (5).

## 3. The kernel of this linear map is proper and isotropic for M

Suppose M!=0 and put

    T={v:DQ(v)=0}.

It is a linear subspace because DQ is linear in its base point. It is proper. Otherwise DQ would vanish everywhere, so Q would vanish by homogeneity. Since M is nonzero symmetric and trace-free, rank M>=2. If Mx and Nx are dependent for every x, this rank implies N=lambda M: compare two vectors with independent M images and their sum, then compare any other nonzero image with one of those two. A vector in ker M has its N image in both independent image lines, by adding it to the two reference vectors, so that image is zero. Taking traces contradicts tr N=2|M|_F^2>0. This proves properness.

For any v in T,

    v^T Mv=0.                                        (6)

If Mv=0 this is immediate. Otherwise Euler's homogeneous identity DQ(v)v=2Q(v) gives Nv=lambda Mv for some real lambda. For every h,

    0=DQ(v)h=Mh cross Nv+Mv cross Nh
                =Mv cross (N-lambda M)h.

Thus the symmetric matrix N-lambda M has range contained in the line spanned by z=Mv. It equals t z z^T for a real scalar t. Its trace gives t|z|^2=2|M|_F^2>0. Applying it to v gives0=t z(v^T Mv), proving (6).

In finite dimensions the linear map x -> DQ(x) has a positive least singular value on T-perp, unless that space is zero, which properness excludes. Hence (5) gives

    dist(x,T)<=C1|x|^2 on O near0.                    (7)

Decompose x=v+z with v in T and z perpendicular to T. Then |v|<=|x| and |z|<=C1|x|^2. Expanding the quadratic form and using (6) yields

    |x^T Mx|<=C2|x|^3 on O near0.                    (8)

## 4. Exact radial rate and the thin-volume contradiction

Since J is skew, U=Mx+O(|x|^2) and (8) imply

    x.B(x)=c|x|^2+O(|x|^3) on O near0.               (9)

Choose a small closed ball where this is at least c|x|^2/2 for all its vortical points. A solution of the backward field -B starting at such a point stays vortical at every finite time: along it (1) is an invertible linear ODE for W. While it remains in the ball, (9) makes its radius strictly decrease. It cannot exit. Local existence extends it for all nonnegative time because it remains in a compact subset of the domain of the C1 field. Thus no global completeness assertion is being used.

Write Psi_t for this local backward flow continued along the trapped trajectories, and r(t)=|Psi_t x|. Equation (9) gives

    |(d/dt)log r(t)+c|<=C r(t),
    r(t)<=r(0)exp(-ct/2).

Integration of the first inequality using the second gives a uniform constant C3, independent of the starting point in the small ball, such that

    r(t)<=C3 exp(-ct)r(0).                            (10)

This exact exponent c matters. The weaker exponent c/2 alone would not yield the volume contradiction below.

Let k=codim T>=1. The tube bound (7) implies, for sufficiently small R,

    |O intersect B_R|<=C4 R^(3+k).                    (11)

Indeed the3-k tangential coordinates have size at most R, and the k normal coordinates have size at most C1 R^2. Orthogonal product boxes give the claimed volume bound, including the case T={0}.

If vortical points existed arbitrarily near0, choose a nonempty ordinary ball D with closure in O and in the trapping ball. Its backward image lies in O intersect B_(C5 exp(-ct)) by (10). On the other hand, div B=3c exactly, so the variational determinant for the local flow is

    det D Psi_t=exp(-3ct).

Uniqueness makes each finite-time map one-to-one, and the change-of-variables formula applies on D. Therefore

    exp(-3ct)|D|=|Psi_t D|
                       <=C6 exp(-(3+k)ct).

Multiplying by exp(3ct) and letting t tend to infinity contradicts |D|>0. This excludes vortical accumulation at0 when M!=0. The flow may fail to be trapped at nonvortical nearby points; that is irrelevant to the chosen open ball and its images.

## 5. The case M=0

If M=0, choose a small ball with |U(x)|<=c|x|/2 and ||sym DU(x)||<=1/2. Then x.B(x)>=c|x|^2/2 at every point, so all backward trajectories in the ball are trapped, complete for nonnegative time locally, and tend to0. Along any such orbit, (1) gives

    dW(Psi_t x)/dt=(I+omega J-DU(Psi_t x))W(Psi_t x),
    d|W(Psi_t x)|^2/dt
       =2|W|^2-2W.sym(DU)W>=|W|^2.

A nonzero initial value would grow exponentially, contradicting the boundedness of W on the compact ball, or its convergence to W(0)=0. Thus W vanishes on that entire smaller ball. This also follows from A473 but is proved directly here.

## 6. Dependencies, review and limitations

The local proof uses a!=0,c>0, exact div B=3c, local C2 velocity, zero helicity, the two identities (1), and rank (2) on the open vortical set. It has no boundary integration, pressure normalization, decay assumption, probability measure or global orbit classification. All constants may depend on the local field and omega; the theorem is valid for every finite omega.

The full coordinator CO26 source and its configured-model check are pinned in verification. The originating the external referee (a second model)-up reported that its own attempted model consultation failed to obtain credentials. That unavailable inner consultation is not treated as a successful review. The separate existing coordinator, configured as model, supplied the substantive review; this identifies configuration evidence rather than independently attested provider metadata. Its advice has been independently checked here, including the C2 remainder orders, the linear-algebra kernel, exact radial rate and Jacobian.

This strengthens A472 from first-order flatness and a proper approach cone to an actual irrotational neighborhood at a zero-velocity origin, using the differentiated rank identity. It does not remove nonzero-velocity carrier equilibria from A471 and does not bound their backward exponents. Global arbitrary-omega nonexistence from U tending0 remains open.
