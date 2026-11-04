# Exact equality locus for the central vorticity bound

Status: independent reconstruction of the Theory Agent C  equality observation. The result is conditional on the same central hypotheses as A2764 and describes growing affine realizations.

## 1. Statement and dependencies

Suppose U in C2 and P in C1 solve the incompressible rotating profile equation near zero, for real c and omega. Assume U(0)=0, H=D2P(0) is positive semidefinite, and W=curl U(0) is nonzero. The equation gives P in C2. Set

    e=W/|W|, u=omega^2|Je|^2, v=omega(e.e3), z=v^2,
    s=sqrt(6), beta=(s-2)/3,
    a_star=(12+6s+4sqrt(27+11s))/(8+3s),
    z_star=(a_star-s)/beta.

The sharp value |W|^2=59+24s is possible only if

    u=2+s+beta z,    0<=z<=z_star.                         (1)

Conversely, for every real omega and unit e satisfying (1), there is a full affine profile on R3 attaining that value with positive semidefinite pressure Hessian, for every real c. In particular the complete set of squared rotation rates admitting such affine equality examples is

    2+s <= omega^2 <= 2+s+(1+beta)z_star.                 (2)

Every equality Hessian is singular. The displayed examples grow linearly and do not imply anything about existence in the decay-only class. This proof uses the central reduction already independently confirmed in A2760 and A2764, restated below, and independently checks the Theory Agent C  note of 02:27Z. Its rounded decimal endpoints are not needed.

## 2. Central algebra and the two lower bounds

Use the oriented orthonormal frame (e,Je/|Je|,e cross Je/|Je|). The strict angle inequality already gives u>2. Let k=omega|Je|, a=u-2, w=|W|, K=(1+w^2)/4. The possible derivatives have the form

    M=[[1,k,0],[k,-1/2+eta,xi-w/2],[0,xi+w/2,-1/2-eta]].

Write y=(xi,-eta), and set

    C=[[3u+9u/a,3uv/a],[3uv/a,uv^2/a]],
    tau=tr C, h=((C11-C22)/2,C12), R=|h|.

The full pressure Hessian is

    H=[[a,-3k,-kv],
       [-3k,K-eta^2-xi^2-3u+2vxi,-2veta],
       [-kv,-2veta,K-eta^2-xi^2-2vxi]].

Its Schur complement is positive semidefinite exactly when

    K>=|y|^2+tau/2+|h-2vy|.

Minimizing the right side over y gives

    K_min=tau/2+R-z,                 if R>=2z,
    K_min=tau/2+R^2/(4z),            if R<2z.             (3)

The second branch necessarily has z>0. Its excess over tau/2+R-z is (R-2z)^2/(4z), strictly positive. Thus equality in the universal lower bound can occur only in the first branch, including its boundary.

## 3. Equality in Cauchy-Schwarz

Set q=z+15-3u. Direct expansion gives

    R=u sqrt(q^2+108a)/(2a),
    tau/2+R-z=15+[u sqrt(q^2+108a)-(u-4)q]/(2a).

The vectors (u-4,sqrt(8a)) and (q,sqrt(108a)) have norms u and sqrt(q^2+108a). Their scalar product is (u-4)q+12s a. Equality in Cauchy-Schwarz occurs exactly when the second vector is a nonnegative scalar multiple of the first. Their positive second coordinates force that multiple to be lambda=3s/2. Hence equality is exactly

    q=lambda(u-4),
    u=2+s+z/(3+lambda)=2+s+beta z.                      (4)

On this curve the common lower bound equals K0=15+6s and

    R=lambda u^2/(2a).

Since K=(1+|W|^2)/4, the target vorticity equality forces both (4) and the first-branch condition R>=2z.

## 4. Exact endpoint of the equality curve

On (4), a=s+beta z and z=(3+lambda)(a-s). The inequality R>=2z is equivalent, after multiplication by the positive 2a, to

    lambda(a+2)^2 >=4a(3+lambda)(a-s).

Substitute lambda=3s/2 and s^2=6, and divide by3/2. This becomes

    (8+3s)a^2-(24+12s)a-4s<=0.                          (5)

Its constant term is negative, so it has one positive and one negative root. The positive root is exactly a_star: the discriminant is64(27+11s). At a=s the left side is -24-10s<0, so a_star>s. As a>=s, condition (5) is exactly s<=a<=a_star, or 0<=z<=z_star. This proves necessity in (1).

Also omega^2=u+z=2+s+(1+beta)z. This is strictly increasing in z, so its image is precisely (2). No rounding is involved in either endpoint.

## 5. Explicit affine realization

Fix omega,e satisfying (1), put w=sqrt(59+24s), and compute the frame data above. Here R>0. Choose

    y=(v/R)h,    xi=y1, eta=-y2.

Then |y|^2=z and h-2vy=(1-2z/R)h. Since R>=2z, this gives |h-2vy|=R-2z. With K=K0=tau/2+R-z, the Schur complement has eigenvalues zero and2(R-2z), so H is positive semidefinite. Its first pivot is a>0.

Let E be the orthogonal frame matrix and define U(x)=E M E^T x, P(x)=(1/2)x^T E H E^T x. The central algebra yields H=-M-M^2-[E^T(omega J)E,M] and tr M=0. Consequently these fields solve the entire profile equation: for linear U the c-dependent terms cancel, leaving exactly the displayed matrix identity. Their vorticity is w e. They attain (1) for every real c.

The original derivative E M E^T sends e to e+omega Je and is nonzero, so the affine field grows on a ray. The Schur complement is singular throughout the equality curve; positive definite H is impossible at the sharp value, consistently with A2764.

## 6. Scope and comparison

The complete selected Theory Agent C  note was read. Its by-hand equality condition, first-branch restriction and nonuniqueness of the attaining rotation agree with Sections 3-4. The exact endpoint and explicit realizing parameters above supply the unrounded version. The Theory Agent C  numerical bisections and decimal endpoints are not used or newly certified.

Comparison is with the existing C agent configured as model, through the shared read-only note and the auditor's response files. Actual provider execution is independently unattested. No new client or agent, numerical computation, formal build, server or external publication is involved.

The current report's statement that the bound is attained "for example" at omega^2=2+sqrt(6) was already correct and needs no extension to state this whole equality locus. The central zero and pressure Hessian remain additional hypotheses; no global decaying-profile existence or nonexistence follows.
