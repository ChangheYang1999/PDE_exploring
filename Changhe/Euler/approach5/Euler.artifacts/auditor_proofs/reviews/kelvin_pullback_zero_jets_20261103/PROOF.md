# Kelvin pullback, Bernoulli coefficients and vorticity jets

Status: complete independent audit of C47, with a stronger classification of the nonzero first vorticity jet at an irrotational velocity zero. No general exclusion of T0 is asserted.

## 1. Exact setting and notation

Fix 2/5<c<1/2 and finite real omega. Put Jx=(-x2,x1,0), A=cI-omega J, a=1-2c, b=2(1-c)=1+a, kappa=1+c, p=(1-c)/c and B(y)=Ay+U(y). Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0, (1-c)U+DU B+omega JU+grad P=0,
    U.Omega=0, Omega=curl U,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1), C<infinity.

Use the canonical pressure constant Pinf and define

    H=P-Pinf+|U|^2/2+(Ay).U,
    Q=P-Pinf-|U|^2/2, g=U.B=H-Q.

The original carrier flow Phi_t is complete, all backward half-orbits are bounded, and E is its invariant escaping set. The actual C1 scattering diffeomorphism Xi:E -> D=R3 minus0 satisfies Xi(Phi_t y)=exp(tA)Xi(y). The tails V,W=curl V,P2 give X=Ax, k=X.V, S=P2-|V|^2/2, Z=int_D{k=0}, L=k o Xi, Sigma=S o Xi.

The confirmed inputs, at this exact class, are

    grad H=-aU+B cross Omega, BH=-ag, Omega.grad H=Omega.grad Q=0,
    D Phi_t Omega=exp(kappa t)Omega o Phi_t,
    d_t(D Phi_t^T U o Phi_t)=-D Phi_t^T(aU+grad Q) o Phi_t,
    exp(at)H o Phi_t -> L, exp(bt)Q o Phi_t -> Sigma in C1_loc(E),
    W o Xi=DXi Omega, grad k=X cross W-aV.

H and Q are C2, bounded and vanish at infinity. The scalar rank identity holds on the vortical subset of the open invariant domain containing E and extends to its closure. Tail V is C^(1,alpha) locally for every alpha<1. All supports and closures below are relative to D.

## 2. Kelvin pullback with justified differentiability

For y in E define

    M(y)=integral_0^infinity exp(ar)Q(Phi_r y)dr.

The C1 tail limit for Q bounds the integrand locally uniformly by C exp(-(b-a)r)=C exp(-r) for large r. Thus the integral converges absolutely and locally uniformly. For the truncated M_t, Kelvin gives

    grad M_t=U-exp(at)D Phi_t^T U(Phi_t y).

Write z_t=exp(-tA)Phi_t. With u_t(z)=exp((1-c)t)exp(omega tJ)U(exp(tA)z), the last term is exactly Dz_t^T u_t(z_t). Its local uniform limit is DXi^T V(Xi). Therefore both M_t and their gradients converge locally uniformly, proving M in C1(E) and

    DXi^T V(Xi)=U-grad M.                                  (2.1)

Changing the lower endpoint after flowing gives BM=-aM-Q. Contract(2.1) with Omega and use both helicity identities to get Omega.grad M=0. Contract with B, use DXi B=X o Xi, and obtain

    L=H+aM.                                               (2.2)

Only first derivatives of Xi are used.

## 3. Two-sided integral and two asymptotic coefficients

The identity d_t(exp(at)H(Phi_t y))=a exp(at)Q(Phi_t y), boundedness of H,Q and a>0 imply for every y in R3

    H(y)=a integral_(-infinity)^0 exp(ar)Q(Phi_r y)dr.

For y in E, adding aM and using(2.2) gives the absolutely convergent formula

    L(y)=a integral_(-infinity)^infinity exp(ar)Q(Phi_r y)dr.

Let q_s=exp(bs)Q o Phi_s. A change of variable gives

    exp(bt)M(Phi_t y)=integral_0^infinity exp(-u)q_(t+u)(y)du.

The q_s converge in C1 on compact subsets of E and their C1 norms there are uniformly bounded for large s. Dominated convergence of values and first derivatives gives

    exp(bt)M o Phi_t -> Sigma,
    exp(bt)(H o Phi_t-exp(-at)L) -> -a Sigma,
    exp(bt)(g o Phi_t-exp(-at)L) -> -b Sigma,                 (3.1)

all in C1_loc(E). Consequently k(x0)=S(x0)=0 is equivalent to H(Phi_t y0)=o(exp(-bt)); S(x0)=0 alone is equivalent to the analogous Q statement. A vanishing tail coefficient is not a pointwise statement about H(y0) or Q(y0).

## 4. Original and tail vorticity Jacobians

At any original zero Omega(y0)=0 set N=D Omega(y0). Differentiating the exact Cauchy formula removes the D2Phi term because it multiplies Omega(y0). Thus

    D Omega(Phi_t y0)=exp(-kappa t)D Phi_t(y0)N D Phi_t(y0)^(-1).  (4.1)

All backward orbit points stay in a fixed compact set, on which D Omega is bounded. Spectral radii in(4.1) scale by exp(-kappa t), so every eigenvalue of N is zero. In dimension3, N^3=0. The commutator and differentiated helicity/first-integral identities give

    NB(y0)=0, N^T U(y0)=0, N^T grad Q(y0)=0.                (4.2)

For x0=Xi(y0) with W(x0)=0, the exact pushforward and its first-order expansion at a zero give

    F:=DW(x0)=TNT^(-1), T=DXi(y0), F X0=0, X0=Ax0.

This pointwise derivative exists even though W need not be C1 on a neighborhood. Nilpotence follows without controlling the condition number of T along an infinite orbit. The original statement applies also in the core, although Xi and M do not.

## 5. Range containing the carrier direction

Suppose W(x0)=0 and X0 belongs to range F. This is equivalent to B(y0) belonging to range N. Formula(4.1) and D Phi_t B=B o Phi_t preserve that range inclusion along the whole carrier orbit. Equation(4.2) then makes g=U.B=0 there. Hence H is constant there; escape and H->0 make H=0. It follows that Q=0, L=0 and M=0 along the orbit. Also

    grad H=-aU, grad Q cross U=0                           (5.1)

there. For the second identity, N_t is nonzero, so the orbit point is approached by vortical points in the open escaping set. Extend the rank relation for H,Q by continuity.

The tail limits give k(x0)=S(x0)=0. Nonzero F makes x0 supported. If also V=DV=0, the point belongs to T0 and lies in closure Z by A1007: outside that closure a V zero has D Omega=0.

The source sufficient cases are valid. If rank F=2, its kernel is span X0; nilpotence gives nonzero range F^2 contained in that kernel, so X0 lies in range F. If F=X0 tensor ell with ell!=0, the inclusion is immediate and ell(X0)=0. At an interior Z point with V=DV=0, differentiating grad k=0 at that point gives X0 cross F=0, hence exactly this rank-one form when F!=0.

## 6. The submitted complementary-case implication

Assume V=DV=0, F!=0 and X0 not in range F. Nilpotence excludes rank2 as just explained; rank1 gives F=w tensor m with m(w)=m(X0)=0 and w not parallel to X0. A1007 puts x0 in closure Z, while the interior-Z calculation excludes x0 in Z. Differentiating grad k at x0 yields

    grad k(x0+h)=m(h)(X0 cross w)+o(|h|).

Since grad k=0 on Z, its points near x0 satisfy |m(h)|<=epsilon|h| after shrinking, for any epsilon>0. This proves the submitted conditional wedge implication. Section8 below shows that its antecedent is actually impossible in the stated actual class. Thus it is not a surviving configuration.

## 7. A two-sided classification before assuming a flat velocity zero

Here is the additional argument. Suppose V(x0)=W(x0)=0 and F!=0, but do not assume DV(x0)=0. At y0=Xi^(-1)(x0), N!=0. Choose one scalar component f of the original C1 Omega with df(y0)!=0. The submersion theorem gives a small coordinate box around y0, contained in E, whose two connected open halves f>0 and f<0 are vortical and whose union is dense. Their images Oplus,Ominus under Xi retain these properties.

On either image half, the set where k=0 is relatively closed. It is also relatively open by A963, since every vortical k zero has a full zero neighborhood. Connectedness therefore gives the dichotomy on each half: k is identically zero there, or k has no zero there.

If both halves have nonzero k, the scalar rank law supplies one finite constant on each, S=Dplus |k|^q and S=Dminus |k|^q, q=2(1-c)/a>2. Their finite maximum extends by density to a full neighborhood. Bounded X gives |S|<=C|V|^q. At V=W=0, the full-ball pressure lemma A1006 forces V=0 near x0, hence Omega=0 near y0. This contradicts df(y0)!=0.

At least one half, therefore, has k identically zero. In particular x0 belongs to closure Z. The exact gradient identity is differentiable at x0, because W has its pointwise derivative there. Put M0=DV(x0). Since grad k(x0)=0,

    D(grad k)(x0)=X0 cross F-aM0.                          (7.1)

On the open zero half, grad k=0. Its tangent set at x0 contains an open half-space, because it is the C1 image of a submersion half-box. Applying the derivative expansion to every direction in that half-space shows that the linear map in(7.1) vanishes on an open set of vectors, hence is identically zero:

    X0 cross F=aM0.                                      (7.2)

No Hessian continuity or C2 scattering map is assumed.

## 8. Nilpotence forces flat velocity and range parallel to X0

Since W(x0)=0 and div V=0, M0 is symmetric and trace free. Tail homogeneity and V(x0)=0 give M0 X0=0. In an oriented orthonormal basis with X0=ell e3, write

    M0 = [[u,v,0],[v,-u,0],[0,0,0]].

The identity F X0=0 makes the last column of F zero. Equation(7.2) determines its upper-left block as -(a/ell)J2 M2, where J2=[[0,-1],[1,0]] and M2 is the displayed two-by-two block. This product is symmetric, trace free and has eigenvalues plus/minus(a/ell)sqrt(u^2+v^2). Since F is block lower triangular and nilpotent, both eigenvalues vanish. Thus u=v=0 and

    DV(x0)=0, DW(x0)=X0 tensor ell0,
    ell0!=0, ell0(X0)=0, D(grad k)(x0)=0.                 (8.1)

Consequently X0 lies in range DW and Section5 applies: S=P2=0 and the original orbit has all the stated H,Q,g,M identities. The point is a supported T0 point in closure Z. This proves:

At every actual irrotational velocity zero with a nonzero first vorticity jet, the velocity derivative is zero and that vorticity jet has rank1 with range exactly span X0.

In particular C47(f) has an empty antecedent. Rank2 vorticity Jacobians are also excluded at irrotational velocity zeros, although Section5 still allows their range conclusion at W zeros with V!=0. This theorem uses both actual zero-region geometry and the pressure law, not merely nilpotent linear algebra.

## 9. Translation remarks, scope and evidence

Equation(2.1) gives V(x0)=0 if and only if U(y0)=grad M(y0). It also gives V=DV=0 if and only if U(y)-grad M(y)=o(|y-y0|). The forward implication uses V(Xi(y))=o(|y-y0|) and bounded DXi; the reverse uses its bounded inverse and differentiability of V. At a zero, differentiation of the product does not require differentiating DXi because its multiplying V value vanishes.

At the base regularity, the second pressure jet cannot be read merely from a C1 rescaled convergence assertion. Under the global all-order hypotheses of C48(a), the separate smooth-scattering argument does justify higher jet composition; an exterior-only smoothness assumption does not by itself make Xi smooth through a nonsmooth original core.

Inside Z at a flat zero with S!=0, the existing normal form bounds |W| by C|V|, so F=0. The new Sections7-8 also show that every flat zero with F!=0 has S=0, without an interior-Z premise. Points with F=0 remain unresolved. No ratio at a zero is defined and no negative pressure conclusion is made.

All seven C47 sections were read and independently reconstructed. The full pointwise nilpotence proof and A1006/A1008 pressure argument were rechecked. A focused existing configured model comparison of the new two-sided classification is requested. C47 is from a configured model agent; runtime identity is not independently attested. No numerical computation, formal build, extra agent or new model client is used.
