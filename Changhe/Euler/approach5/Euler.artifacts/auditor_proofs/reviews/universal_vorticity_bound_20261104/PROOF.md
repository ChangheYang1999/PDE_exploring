# Independent audit of the sharp rotation-uniform central vorticity bound

Status: independent reconstruction and existing coordinator comparison complete. The bound is local and conditional on a central velocity zero and a semidefinite pressure Hessian. It is not nonexistence in the unrestricted decaying class.

## 1. Exact statement and notation

Let Jx=e3 cross x, and let c and omega be any real numbers. On a neighborhood of zero suppose U is C2, P is C1, and

    div U=0,
    (1-c)U+DU[(cI-omega J)x+U]+omega JU+grad P=0.      (1)

Assume U(0)=0. The equation upgrades P to C2. Put M=DU(0), H=D2P(0), W=curl U(0). If H is positive semidefinite and W is nonzero, then

    |W|>=sqrt(59+24sqrt(6)).                            (2)

If H is positive definite, then W is nonzero and (2) is strict. A local pressure minimum supplies semidefinite H; a strict minimum alone does not supply positive definite H. The constant is attained by a complete affine profile with a nonisolated quadratic pressure minimum, for every c and one allowed rotation. Positive definite affine examples approach the same constant from above. All these examples grow at infinity.

## 2. Exhausting the possible central matrices

Write B=(cI-omega J)x+U. All terms on the right of the formula for grad P from (1) are C1, hence P is C2. Differentiating at zero, where B=0, cancels the c terms and gives

    H=-M-M^2-omega[J,M],   tr M=0.                      (3)

Curling (1) gives Omega+B.grad Omega+omega JOmega-DU Omega=0, with Omega=curl U. At zero this is MW=W+omega JW. Substituting in (3), including the identity M(MW)=MW+omega M(JW), yields

    HW=-2W-3omega JW-omega^2 J^2W.                     (4)

Skew symmetry of J gives

    W.HW=-2|W|^2+omega^2|JW|^2,
    (JW).HW=-3omega|JW|^2.                             (5)

If H is semidefinite and W is nonzero, the first expression is nonnegative. If it were zero, diagonalization of H would give HW=0. Equality in the first expression also implies omega and JW are nonzero, contradicting the second expression. Thus omega^2|JW|^2>2|W|^2.

Let w=|W|, e=W/w, s=|Je|, z=e.e3, k=omega s, v=omega z, u=k^2 and a=u-2. Then s>0 and a>0. Use the positively oriented orthonormal frame (e,f,g), where f=Je/s and g=e cross f. The identity e3=ze+sg gives

    omega J=[[0,-k,0],[k,0,-v],[0,v,0]].

The equation Me=e+omega Je fixes M's first column as (1,k,0). Since curl U=we, its skew part is half the matrix of cross product with we. Together with trace zero, these facts leave exactly the two real parameters eta and xi:

    M=[[1,k,0],[k,-1/2+eta,xi-w/2],[0,xi+w/2,-1/2-eta]].

For K=(1+w^2)/4, multiplication in (3) gives

    H=[[a,-3k,-kv],
       [-3k,K-eta^2-xi^2-3u+2vxi,-2veta],
       [-kv,-2veta,K-eta^2-xi^2-2vxi]].                (6)

For example, the 12 entry of M+M^2 is k(3/2+eta), and that of omega[J,M] is k(3/2-eta), giving -3k in H. The terms in xi-w/2 cancel in entry 13, leaving -kv. In entry 22 the first two matrices give eta^2+xi^2+u-K and the commutator gives 2u-2vxi. In entry 23 they give zero and 2veta, respectively. Thus the signs and all variable entries in (6) are fixed without a symmetry assumption on the original profile.

## 3. A uniform lower bound for the Schur complement

Set y=(xi,-eta) and

    C=[[3u+9u/a,3uv/a],[3uv/a,uv^2/a]],
    tau=tr C, h=((C11-C22)/2,C12), R=|h|.

Completing the square in the first coordinate, using a>0, shows that H is semidefinite precisely when

    (K-|y|^2)I-C+2v[[y1,y2],[y2,-y1]]

is semidefinite. The eigenvalues of a two-by-two symmetric matrix with trace tau and traceless coordinates h are tau/2 plus or minus |h|. Therefore

    K>=|y|^2+tau/2+|h-2vy|.

The reverse triangle inequality and a square give

    |y|^2+|h-2vy|
       >=|y|^2+R-2|v||y|
       =R-v^2+(|y|-|v|)^2
       >=R-v^2.

Consequently

    K>=tau/2+R-v^2.                                    (7)

Positive definite H makes the first eigenvalue inequality strict, hence also makes (7) strict. Neither the sign of R-v^2 nor the minimizing branch from the separate magnitude classification is needed.

## 4. Exact lower bound independent of rotation and angle

Introduce q=v^2+15-3u. Directly from the entries of C,

    tau=u(3u+3+v^2)/a,
    R=u sqrt((3u+3-v^2)^2+36v^2)/(2a).

Expansion gives (3u+3-v^2)^2+36v^2=q^2+108a, and hence

    tau/2+R-v^2
      =15+[u sqrt(q^2+108a)-(u-4)q]/(2a).             (8)

The vectors (u-4,sqrt(8a)) and (q,sqrt(108a)) have norms u and sqrt(q^2+108a), since (u-4)^2+8a=u^2 and u>2. Their scalar product is (u-4)q+12sqrt(6)a. Cauchy-Schwarz therefore implies

    u sqrt(q^2+108a)-(u-4)q>=12sqrt(6)a.

Equations (7)-(8) give K>=15+6sqrt(6). Because w^2=4K-1, this is (2). If H is positive definite, the bound is strict. If W=0 instead, M is symmetric; tracing (3) gives tr H=-tr M^2=-|M|_F^2. Semidefinite H then implies M=0 and, from (3), H=0. In particular positive definite H rules out W=0.

## 5. Exact endpoint and positive definite examples

Let r=sqrt(6), omega0=sqrt(2+r), K0=15+6r and w0=sqrt(59+24r). In the usual coordinates, take

    M0=[[1,omega0,0],[omega0,-1/2,-w0/2],[0,w0/2,-1/2]],
    H0=[[r,-3omega0,0],[-3omega0,9+3r,0],[0,0,15+6r]].

The matrix formula (6), with eta=xi=v=0, verifies

    M0+M0^2+omega0[J,M0]+H0=0.

Thus U(x)=M0x and P(x)=x.H0x/2 solve the full equation (1) for every real c. Their divergence is zero and their vorticity is (w0,0,0). The upper two-by-two block of H0 has positive diagonal entries and determinant r(9+3r)-9(2+r)=0. Its remaining diagonal entry is positive. Hence H0 is semidefinite and the pressure has a global, nonisolated minimum. This profile attains (2).

For w>w0 replace w0 by w in M0 and set

    H=H0+[(w^2-w0^2)/4]diag(0,1,1).

Equation (6) still verifies the full equation. A vector in the null space of this nonnegative quadratic form would have its last two coordinates zero and then, by H0's first entry r>0, its first coordinate zero. Thus H is positive definite. Letting w decrease to w0 proves sharpness of the strict bound as an infimum. Since M0 has first diagonal entry 1, these velocities grow on a ray. No decaying profile is constructed.

## 6. Scope and verification

The proof uses exactly the central zero, the full local profile equation and the semidefinite Hessian condition. It neither proves that decay supplies a central zero or pressure minimum nor permits moving an arbitrary velocity zero to the similarity center without transforming the equation. Semidefinite H does not by itself supply a neighborhood pressure minimum. The distinction between strict minimum and positive definite Hessian is retained.

All six source sections and all six independent sections were read in full. The proof is algebraic apart from differentiation of C2/C1 functions. It uses no numerical optimization, external theorem beyond elementary linear algebra, global characteristic completeness, formal build or new model client. Supplementary source checks are not dependencies. The existing coordinator comparison is recorded below.

## 7. Existing comparison and endpoint scope

All four items and W1-W3 of the coordinator comparison, written at 2026-11-04T02:13Z, were read. All thirteen supplementary check lines were read, not rerun. The comparison agrees with the derivation above. In particular the Cauchy-Schwarz estimate is an exact proof of the global lower bound; the 200000 sampled pairs in the log supply no additional proof coverage.

The comparison also checks compatibility with the exact two-branch threshold of LIT327. In its second branch the difference between the exact minimized value and R-v^2 is (R-2v^2)^2/(4v^2), so the simpler lower bound used here is valid in that branch as well. Equality is attained at v=0 and u=2+sqrt(6), as Section 5 proves. Neither this proof nor the comparison asserts uniqueness of the attaining rotation and direction.

The statements for a positive definite Hessian and for a strict pressure minimum must remain separate. A positive definite Hessian excludes W=0 and forces a strict magnitude inequality. A strict minimum can have a singular Hessian and does not justify that strict inequality by itself. No center premise is inferred from decay. The existing comparison uses the configured coordinator agent; no additional client or agent was invoked.

## 8. Source and comparison revision check

At 2026-11-04T02:26:04.777051+00:00, the complete revision from the archived submission was read. The source revision records A2764-A2766 and adds a precise completed-comparison paragraph. It distinguishes a strict pressure minimum from positive definite Hessian, retains the growing affine examples, and asserts no uniqueness of the minimizing angle. No statement or equation changes. Its sampling disclosure is limited to that agent; this audit previously read the coordinator log but did not rerun it. The exact source hash is 682bf2350c41d8c2749b55a893e5dbe9ddf4979c62f3ae9957e5217bcc66f3c2; both versions and their diff are retained under verification. A2784 confirms only these revision transfers.
