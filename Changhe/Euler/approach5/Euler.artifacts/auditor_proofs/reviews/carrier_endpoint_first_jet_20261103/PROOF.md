# Exact endpoint first jets for the carrier directional estimate

## 1. Statement and scope

Let 0<c<1/2 and omega be any real number. Define a=1-2c,b=2(1-c)=1+a,eta=a/b,Jz=e3 cross z,A=cI-omega J and L=(1-c)I+omega J. The local carrier is X(y)=Ay. At a nonzero point p there exist a positive scalar value H and a nonzero vector value V, with assigned first derivatives, satisfying

    X dot V=0, div V=0, W=curl V,
    (DV)X=-LV, grad(X dot V)=0, X cross W=aV,
    X dot grad H=-bH, W dot grad H=0, W dot V=0,
    W=eta grad(log H) cross V,
    |sym DV|^2=|W|^2/(2a^2),
    grad log(|V|^2/H)=0.

All identities in this statement are imposed only at p. These first jets refute a strict directional conclusion from these identities alone at the exact ratio mu=1/(2a^2). For every gamma>0 no direction Z can satisfy both d(log H)(Z)>0 and d(log(|V|^2/H)+gamma log H)(Z)<=0. This is not a construction satisfying these equations on a neighborhood, and imposes no Poisson equation. It neither proves nor refutes the endpoint extension of the full common-flat-orbit theorem A2284.

The complete five-section LIT297 source was read and pinned in the team records. Its equations are independently verified below. The contextual theorem and above-threshold limitation have the independent proof in the team records, A2278-A2284. No computation is needed.

## 2. Construction and derivative convention

Choose R>0,p=(R,0,0),V=e3,H=1. Then X=(cR,-omega R,0) is horizontal and nonzero. Choose any horizontal vector u with X dot u=-b. Such a vector exists; all choices are

    u=-bX/|X|^2+s f,

where f is a horizontal unit vector perpendicular to X and s is real. In particular u dot V=0 and u!=0. Assign grad H=u and define

    W=eta u cross V,
    M=(u tensor V+V tensor u)/(2b),
    D=M+[W cross]/2,

where D_ij=partial_j V_i and [W cross]z=W cross z. The affine field V(y)=e3+D(y-p) and scalar H(y)=1+u dot(y-p) realize exactly these first jets, with H positive on a sufficiently small ball. Their existence is only a first-jet realization; they are not asserted to obey the identities away from p.

M is symmetric and trace free. The linear vector field [W cross](y-p)/2 has curl W, meaning its curl is the vector W itself. This follows directly from the three Cartesian curl components, each equal to the corresponding component of W. Thus sym D=M,tr D=0 and the assigned curl of V is W.

## 3. Verification of the carrier and scalar relations

Since X dot V=0 and X dot u=-b,

    MX=-V/2,
    [W cross]X=eta[(u cross V) cross X]=-aV.

It follows that DX=-(1+a)V/2=-(1-c)V=-LV, because JV=0. Also D^T X=-(1-a)V/2=-cV=-A^T V. The derivative of X dot V is A^T V+D^T X=0. The other vector identity follows independently from the triple product:

    X cross W=eta[u(X dot V)-V(X dot u)]=aV.

The scalar relations hold because H=1 and grad H=u. The dot product X dot grad H is -b. W is orthogonal to both u and V, and grad(log H)=u, so all three remaining scalar/curl identities hold.

At the point E=|V|^2=1. Directly,

    MV=u/(2b), [W cross]V=-eta u,
    grad E=2D^T V=(1/b+eta)u=u.

Here1/b+eta=(1+a)/b=1. Consequently grad log E=grad log H=u, which proves the required vanishing of grad log(E/H). No coordinate restriction on omega was used other than its prescribed vertical axis; every real omega is allowed.

## 4. Endpoint norm and directional obstruction

The tensors u tensor V and V tensor u are orthogonal in the Frobenius inner product because u dot V=0. Their squared norms both equal |u|^2, as |V|=1. Therefore

    |M|^2=|u|^2/(2b^2),
    |W|^2=eta^2|u|^2=a^2|u|^2/b^2.

Since a>0 and u!=0, W!=0 and the ratio is exactly1/(2a^2). At these same data,

    d(log(E/H)+gamma log H)(Z)=gamma u dot Z.

For gamma>0 this is positive whenever d(log H)(Z)=u dot Z>0. Thus the proposed two signs are incompatible for every direction Z, even without restricting Z to a transverse plane. If s!=0, taking the transverse direction f shows that directions increasing H do exist after orienting f suitably; the failure concerns the second sign, not their absence.

This strengthens the algebraic limitation A2283 from ratios strictly above the threshold to equality. It does not settle the full theorem at equality: the common flat point, its entire smooth flowbox, the sign and flatness of the pressure, and the Poisson coupling were not imposed. Additional differential information could still prove a full endpoint theorem.

## 5. Verdicts and verification evidence

A2304 CONFIRMS the exact first-jet construction and every identity, for all0<c<1/2 and all real omega. A2305 CONFIRMS the directional-method obstruction at the exact endpoint. A2306 leaves the full endpoint theorem, field sharpness, common-flat-orbit existence and unrestricted decaying-profile conjecture OPEN. No numerical observation is used as proof and no computational runtime is claimed.

The complete source and all five independent proof sections were read. No formal build was run. The actual configured model collaboration continues through existing working files; provider execution is independently unattested.
