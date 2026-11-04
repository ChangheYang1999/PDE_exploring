# Pointwise vorticity jets at tail zeros outside open scalar-zero regions

Status: independent complete audit of LIT197. The pointwise differentiability and first-jet exclusions below are proved with their exact local scope. No exclusion of an arbitrary supported flat zero follows.

## 1. Exact statement and dependencies

Let 2/5<c<1/2, omega in R, a=1-2c, p=(1-c)/c and q=2(1-c)/a>6. Set Jx=(-x2,x1,0), A=cI-omega J and B=Ax+U. Suppose U in C2(R3;R3), P in C1(R3) solve

    div U=0,
    (1-c)U+DU B+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

with one finite C. Write Omega=curl U, E for the escaping set of the complete carrier flow, and Xi:E->D=R3 minus {0} for its actual C1 scattering diffeomorphism. The confirmed construction supplies V in C^(1,alpha)_loc(D) for every alpha<1, W=curl V, P2 in C1, and

    DXi(y)Omega(y)=W(Xi(y)),
    div V=0, -Delta P2=partial_i partial_j(V_i V_j),
    k=X.V, X(x)=Ax, S=P2-|V|^2/2,
    X.grad k=-ak, X.grad S=-2(1-c)S,
    grad k cross grad S=0 on {W!=0}.

Let Z=int_D{k=0}. By A963/A970, at any vortical point with k=0 the scalar is zero on an open neighborhood. Therefore, throughout D minus closure Z,

    k=0 implies W=0.                                  (1)

The claims are:

(a) At every x0 in D with W(x0)=0, W is differentiable at that point. If y0=Xi^(-1)(x0) and T=DXi(y0), then

    DW(x0)=T D Omega(y0) T^(-1).                       (2)

(b) If V(x0)=0 and x0 is outside closure Z, then Omega(y0), D Omega(y0), W(x0) and DW(x0) are all zero.

(c) More generally suppose V(x0)=0 outside closure Z and a connected open neighborhood N of y0, contained in E, has Xi(N) outside closure Z. If its vortical set is dense and has finitely many connected components, then V is zero on a neighborhood of x0. This is impossible when x0 belongs to supp W. Thus every such neighborhood at a supported zero has either an open irrotational subset or infinitely many vortical components.

All closures are relative to D or the specified neighborhood. Part(a) needs no scalar-region restriction. Parts(b)-(c) do not apply on the boundary of Z or inside it. A neighborhood on which W is C1, Xi is C2 or V is C2 is never assumed.

## 2. Differentiating the pushforward only at a zero

If W(x0)=0, invertibility of T gives Omega(y0)=0. For h tending to zero,

    Omega(y0+h)=D Omega(y0)h+o(|h|),
    DXi(y0+h)=T+o(1).

Thus the exact pushforward becomes

    W(Xi(y0+h))=T D Omega(y0)h+o(|h|).

The inverse C1 map satisfies h=T^(-1)(x-x0)+o(|x-x0|), with comparable distances. Substitution proves(2). No second derivative of Xi occurs, because the potentially problematic factor multiplies a vector field vanishing at y0. At a nonzero W point the same argument cannot remove that factor's derivative.

## 3. Local pressure rigidity with a quantitative Holder threshold

We prove a slightly more general local lemma to check all constants in the submitted epsilon=1/8 argument. Let 0<alpha<=1 and

    0<=epsilon<alpha/(2(1+alpha)).

On a ball about 0 let v be C^(1,alpha), div v=0, and pi in C1 solve -Delta pi=partial_i partial_j(v_i v_j) in distributions. Put s=pi-|v|^2/2. Assume

    v(0)=curl v(0)=0,
    s(x)-s(0)>=-epsilon |v(x)|^2                        (3)

on a full smaller ball. Then v is identically zero on a neighborhood of 0.

Indeed, div v=0 gives Delta pi=-tr((Dv)^2) distributionally. The right side is locally Holder, so pi is C2; for alpha=1 use any smaller positive Holder exponent. Put M=Dv(0). It is symmetric and trace free. Let overbar denote normalized sphere average at radius r and set

    E(r)=overbar |v|^2, F(r)=overbar (v.n)^2.

Taylor expansion and the pressure trace give

    E(r)=|M|^2 r^2/3+o(r^2),
    overbar(s-s(0))=-|M|^2 r^2/3+o(r^2).

Averaging(3) yields (1-epsilon)|M|^2<=0. Since epsilon<1, M=0. Holder continuity of Dv now gives E,F=O(r^(2+2alpha)).

The exact radial pressure-flux identity is

    overbar(pi)'=-F'-(3F-E)/r.                         (4)

For clarity, integrate the pressure equation over the ball: overbar(pi)'=-overbar(((v.grad)v).n). Writing v=v_r n+v_tan and using

    partial_r v_r+2v_r/r+div_S(v_tan)/r=0

in the sphere integration by parts gives overbar(((v.grad)v).n)=F'+(3F-E)/r. The identity requires only v and Dv. One may obtain it by local mollification of a divergence-free field, followed by uniform convergence of those quantities on smaller balls. No boundary at infinity is present.

Define

    Y(r)=overbar(pi-pi(0))+F(r).

Equations(3)-(4) give

    Y'=(E-3F)/r,
    Y>=(1/2-epsilon)E+F>=0.                            (5)

Since Y(0)=0 and Y'=O(r^(1+2alpha)), Y=O(r^(2+2alpha)). Also Y'<=gamma Y/r for gamma=1/(1/2-epsilon). Hence r^(-gamma)Y is nonincreasing and nonnegative. The stated bound on epsilon is exactly gamma<2+2alpha, so its limit at zero is zero. Therefore Y=0, and(5) gives E=0 on all sufficiently small spheres. Continuity proves v=0 on a ball.

For the submission take alpha=1/2 and epsilon=1/8; gamma=8/3<3. The initial quadratic coefficient is 7/8 and all submitted constants agree. In particular, if V(x0)=W(x0)=0 and

    |S(x)|<=C0 |V(x)|^q, q>2                          (6)

on a full neighborhood, then S(x0)=0 and shrinking makes C0|V|^(q-2)<=1/8. The lemma applies. Neither a bound only on one side nor a bound on a nondense subset suffices.

## 4. Two vortical sides exclude a nonzero original first jet

Suppose V(x0)=0 outside closure Z. Since k(x0)=0, (1) gives W(x0)=0, and the pushforward gives Omega(y0)=0.

On any connected open vortical subset in D minus closure Z, k has no zero and X.grad k=-ak!=0. The scalar rank equation gives grad S=lambda grad k. Evaluating on X yields lambda=qS/k, and therefore

    grad(S |k|^(-q))=0.

Connected open subsets of Euclidean space are path connected, so

    S=D_j |k|^q                                       (7)

there for one finite real constant D_j. No uniform bound is inferred across infinitely many subsets.

If D Omega(y0)!=0, choose one component f of the original C1 vorticity with df(y0)!=0. The submersion theorem gives a coordinate box N about y0, with first coordinate f, contained in E and mapped outside closure Z. The two sets f>0 and f<0 within this box are connected, open and vortical. Their union is dense; their omitted coordinate plane has no interior. Their images under Xi have the same properties in Xi(N).

Apply(7) to each image, using constants D+ and D-. Their maximum absolute value gives

    |S|<=max(|D+|,|D-|)|k|^q

on the dense union and, by continuity, on all Xi(N). On a smaller ball about x0, boundedness of X and k=X.V give(6). Section3 now forces V=0 on a ball. Its curl vanishes there, so the exact invertible pushforward forces Omega=0 on the inverse-image neighborhood of y0, contradicting D Omega(y0)!=0.

Hence D Omega(y0)=0; equation(2) gives DW(x0)=0. The submersion was applied to the original C1 vorticity, not to a hypothetically C1 tail vorticity. The two coordinate halves need not be whole components of the full vortical set; their own connectedness is enough for(7).

## 5. Finite components and exact limits

Under the premises of(c), each of the finitely many connected components of the original vortical part of N is open and maps to a connected open vortical subset. Equation(7) supplies one finite constant on each. Take their finite maximum and use density and continuity to extend the bound to the whole image neighborhood. Section3 again forces V=0 near x0.

At a supported zero this is impossible. Failure of density of the open vortical set means that its complement contains a nonempty open set, precisely the irrotational alternative stated. The finite-component premise is not automatic for C1 vorticity.

The conclusions do not exclude a first-order flat original vorticity zero: a C1 field may have both value and derivative zero at a point while remaining nonzero arbitrarily close. Pointwise existence and vanishing of DW do not give a C1 neighborhood of W or a C2 tail. At points in closure Z, the scalar may vanish on one or both vortical coordinate sides, so division by k and the finite constants in(7) are unavailable. The proof has no conclusion there, including at the Tflat boundary identified in A973/A984.

Dependencies: the confirmed actual scattering and pressure identities in Section1, A963/A970, the C1 inverse/submersion theorems, and local elliptic regularity. The pressure lemma reproduces and strengthens the particular constant check in A696-A697. All seven source sections and this independent five-section argument were read completely; no numerical computation or formal build was needed. LIT197 is a the second model agent source. Focused existing configured model comparison remains requested through team files and is not counted as received; provider runtime is unattested. No new client or agent was used.
