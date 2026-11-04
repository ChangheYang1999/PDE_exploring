# Critical transported zeros near a vortical carrier cycle

Status: CONFIRMED as a local vanishing theorem and its stated actual-profile corollary. Open-zero periodic cycles are not excluded.

## 1. Exact local theorem

Let O be open in R3, B in C2(O;R3), Omega in C1(O;R3) and L in C1(O). Let kappa>d>0 and a=kappa-d. Assume pointwise

    div B=d, [B,Omega]=-kappa Omega,
    B.grad L=-aL, Omega.grad L=0,
    [B,Omega]=D Omega B-DB Omega.

Suppose C is a nonconstant periodic B orbit of period T>0 in O, Omega is nonzero at one point of C, and dL=0 on C. Then L vanishes in an open neighborhood of C. Only local flows are required. In particular the theorem assumes no global completeness or surface recurrence.

## 2. Multipliers and precise stable decay

Let Phi be the local B flow and x0 in C. The bracket identity integrates to

    D Phi_t(x0) Omega(x0)=exp(kappa t)Omega(Phi_t x0).

Thus Omega stays nonzero on C, and the monodromy has eigenvectors B(x0),Omega(x0) with respective eigenvalues 1,exp(kappa T). They are independent. The determinant is exp(dT) by the variational determinant equation, so the third eigenvalue is mu=exp(-aT) in (0,1). A C2 transverse Poincare map therefore has the two distinct hyperbolic eigenvalues mu and exp(kappa T).

Apply the local C2 stable-manifold theorem for a hyperbolic fixed point to this return map. This standard finite-dimensional theorem, already a dependency of A462, gives a C2 invariant stable curve. In a coordinate s vanishing at x0, the restricted return map f and the return time tau satisfy

    f(s)=mu s+O(s^2), tau(s)=T+O(|s|).

Choose mu<lambda<1 and shrink until |f(s)|<=lambda|s| and the iterates remain in the stable arc. For s_n=f^n(s), summability of |s_n| follows from this rough contraction. The sharper estimate

    |s_(n+1)|<=mu |s_n|(1+C|s_n|)

then gives |s_n|<=C_s mu^n by the convergent product. A zero iterate causes no difficulty. Also t_n=sum_(j<n)tau(s_j)=nT+O_s(1), because the return-time errors are summable. Consequently

    exp(a t_n)|s_n|<=C'_s.

Both the exact stable multiplier and the actual accumulated flow time are needed; a slightly slower exponential contraction would not give this bounded product.

## 3. Vanishing and local saturation

Periodicity and B.grad L=-aL imply L=0 on C. Restrict L to the stable curve and call the resulting function ell. Criticality gives ell(0)=ell'(0)=0 and hence ell(s)=o(|s|). Transport gives

    ell(s_n)=exp(-a t_n)ell(s).

If an iterate is zero, ell(s)=0. Otherwise the bounded product in Section 2 yields

    |ell(s)|=exp(a t_n)o(|s_n|)->0.

Therefore L vanishes on the stable arc and on its short B-flow images, a local two-dimensional stable cylinder. At x0 the cylinder tangent plane is the span of the flow direction and the stable direction. Omega is transverse to that plane, since its monodromy eigenvalue exp(kappa T) is different from both other eigenvalues.

Apply the local C1 Omega flow to a cylinder chart. The resulting three-variable map has invertible derivative at x0, so the C1 inverse-function theorem gives an open image containing x0. Since Omega.grad L=0, L vanishes on this image. Transport by finitely many short B-flow maps gives an open zero neighborhood of the whole compact orbit. No global leaf topology or completeness is used.

## 4. Actual Euler-profile corollary

Let 2/5<c<1/2, omega in R, Jx=(-x2,x1,0), A=cI-omega J, p=(1-c)/c, a=1-2c and kappa=1+c. Suppose U in C2(R3;R3), P in C1(R3) solve pointwise

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

with one finite constant C. Put B=Ax+U, Omega=curl U. Let E be the open forward escaping B set and O its saturation by the complete original Omega flow. Use the confirmed C1 transported scalar L on O, extending k composed with the scattering diffeomorphism Xi on E, with k(z)=(Az).V(z). Every vortical periodic B orbit lying in O is contained in the interior of {L=0}.

Indeed, periodicity gives L=0 on the orbit. A897 excludes regular vortical L-zeros in E, using the C1 scattering diffeomorphism and its nonvanishing vorticity transport. The same exclusion holds throughout O: a finite Omega-flow segment takes any point of O into E; invariance of L and invertibility of the flow derivative preserve nonvanishing of dL, while a flow preserves nonvanishing of its own generator. Therefore dL=0 all along the vortical cycle. Apply Sections 1-3 with d=3c; kappa-d=a>0.

This finite translation is the needed domain check. L is never evaluated on the joint core where it has not been defined. The abstract proof does not depend on LIT190 or on second-order scalar flatness.

## 5. Dependencies, checks and open scope

The finite-dimensional C2 stable-manifold theorem is an explicit analytic dependency, already audited for A462. All other local ingredients are proved above: bracket transport, the determinant identity, exact contraction product, return-time summability, scalar transport and local saturation. The actual corollary separately uses A897 and the established global scattering and transported-scalar construction under zero helicity and natural rates.

The full six-section LIT191 source and this full proof were read. All steps were checked analytically, with no computation or formal build. A periodic orbit entirely inside an open zero region is not excluded. Cycles in the joint core are outside the domain. No properness, surface measure, second-order flatness, elimination of critical nodes or unconditional rotating nonexistence follows.
