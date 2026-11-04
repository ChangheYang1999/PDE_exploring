# Quantitative Holder geometry at a strict-rate W2 direction

Status: A2445-A2448 CONFIRMED at the exact conditional scopes below; A2449-A2450 OPEN. The quantitative conclusions are necessary conditions. They neither construct nor exclude the configuration for exponents below one.

## 1. Exact local statement

Let 2/5<c<1/2, omega be any real number, a=1-2c, b=2-2c and q=b/a. Thus a>0, q>2 and (q-1)a=1. Put Jx=e3 cross x, A=cI-omega J, X(x)=Ax and L=(1-c)I+omega J. On an open neighbourhood N of w!=0 let V be C^(2,beta), 0<beta<1, and let P2 initially be C2. Write W=curl V, k=X.V and S=P2-|V|^2/2. Assume

    div V=0, DV X=-LV, -Delta P2=tr((DV)^2),
    X.grad k=-ak, X.grad S=-bS,
    grad k cross grad S=0 on the open set Q={W!=0}.

Assume w belongs to closure Q and

    V(w)=W(w)=DW(w)=k(w)=S(w)=grad k(w)=grad S(w)=0.

Suppose M=DV(w) is symmetric, trace free, annihilates X(w), and has eigenvalues sigma,-sigma on E=X(w)^perp, where sigma>0. Choose an orthonormal basis e,f of E such that

    Me=sigma' f, Mf=sigma' e, sigma'=sigma or -sigma,
    D2k(w)=D=-aM, D2S(w)=H=-4sigma^2 f tensor f.

The last Hessian hypothesis is an explicit premise of this local result. Its derivation in the W2 setting is A1732, not a consequence of regularity alone.

Take R>0 such that the closed transverse disc T_R={w+s e+u f:s^2+u^2<=R^2} lies in N. Let K_beta and H_beta bound the beta-Holder seminorms of the full ambient Hessians D2k and D2S on T_R. There are C<infinity and r0 in (0,R/2), with the quantitative smallness threshold depending only on a,sigma,beta,K_beta,H_beta and the restriction r0<R/2, such that every x=w+s e+u f in Q intersect T_r0 satisfies

    |u|<=C|s|^(1+beta),
    |k(x)|<=C|s|^(2+beta), |S(x)|<=C|s|^(2+2beta).

On each connected component C0 of Q intersect {k!=0}, write S=D_C0 |k|^q. At the indicated points,

    alpha=q D_C0 |k|^(q-2)=-4/(a s^2)(1+O(|s|^beta)),
    |D_C0|>=C^(-1)|s|^(-2-(q-2)(2+beta)).

The O constants are uniform over the components. For two distinct points x,x' in Q intersect T_r0, set d=|x'-x| and r=max(|x-w|,|x'-w|). Then

    |(x'-x).f|<=C d^beta r.                         (1)

All these statements also follow directly from C^(2,beta) scalars k,S satisfying the displayed point jets, rank identity and component power law. No global Euler assertion is needed for their proof.

## 2. Regularity, the power law and absence of vortical k-zeros

Since V is C^(2,beta), the function tr((DV)^2) is C^(1,beta). Interior Schauder regularity for the constant-coefficient Poisson equation makes P2 C^(3,beta) on smaller neighbourhoods. Consequently k and S are C^(2,beta). This is an interior statement and needs no boundary condition or normalization of P2. An additive pressure constant is already fixed by S(w)=0 and the assumed scalar transport.

Contracting the rank identity with X gives bS grad k=ak grad S. On each connected component of Q intersect {k!=0}, differentiation therefore gives grad(S |k|^(-q))=0. This proves the component law with a finite constant D_C0.

Let h=s e+u f and r=|h|. Taylor expansion at w, with constants controlled by the Hessian seminorms, gives

    k=-a sigma' s u+O(r^(2+beta)),
    p:=grad k=Dh+O(r^(1+beta)), K:=D2k=D+O(r^beta),
    g:=grad S=Hh+O(r^(1+beta)), H_x:=D2S=H+O(r^beta),
    Delta k=O(r^beta), Delta S=-4sigma^2+O(r^beta).

These are ambient gradients and traces restricted to the disc; the normal entries have not been discarded. Since |Dh|=a sigma r, grad k is nonzero on the punctured small disc and Delta S is strictly negative there. If a vortical point x on this disc had k(x)=0, use k as an ambient local coordinate inside Q. On each sufficiently small connected side of that coordinate surface the power law holds with a fixed finite constant. Because q>2, its Hessian tends to zero at the surface. Continuity would give D2S(x)=0, contrary to Delta S(x)<0. Thus k!=0 at all indicated vortical points.

Differentiating the power law inside Q gives

    S=alpha k^2/q, grad S=alpha k grad k,
    D2S=alpha[(q-1)grad k tensor grad k+k D2k].        (2)

Its trace has denominator

    (q-1)|grad k|^2+k Delta k
       =a sigma^2 r^2(1+O(r^beta)).

Here k=O(r^2), and (q-1)a=1. Hence alpha=-4/(a r^2)(1+O(r^beta))<0. In particular S<0 at each such point, and every component meeting this region has negative D_C0.

## 3. The first cusp estimate and its improvement

The rank identity and Taylor expansions imply

    0=(Dh) cross (Hh)+O(r^(2+beta))
      =4a sigma^2 sigma' u^2(e cross f)+O(r^(2+beta)).

It follows that u^2<=C r^(2+beta). After decreasing r0 this rules out |u|>=|s| at a nonzero vortical point: that inequality would imply 1<=C'|u|^beta. Therefore r<=sqrt(2)|s| and initially |u|<=C|s|^(1+beta/2).

To improve the exponent, take the e-f entry of (2). Its left side is O(r^beta). On the right,

    (e.grad k)(f.grad k)=a^2 sigma^2 s u+O(r^(2+beta)),
    k e.D2k f=a^2 sigma^2 s u+O(r^(2+beta)).

Consequently

    e.D2S f=-4a q sigma^2 (s u/r^2)(1+O(r^beta))
             +O(r^beta).                           (3)

The final additive error is essential; it is present in the source proof. For small r0 the multiplicative coefficient is bounded away from zero. Thus |s u|/r^2<=C r^beta, which gives |u|<=C|s|^(1+beta).

Substitution in the Taylor formula gives k=O(|s|^(2+beta)). Since r^2=s^2(1+O(|s|^(2beta))), the formula for alpha in Section 2 becomes its stated s-form. Equation (2) yields S=O(k^2/s^2)=O(|s|^(2+2beta)). Finally q>2 and k!=0 imply

    |D_C0|=|alpha| |k|^(2-q)/q
       >=C^(-1)|s|^(-2-(q-2)(2+beta)).

This is a uniform lower bound evaluated at points; it does not assert a single component contains all small levels.

## 4. Pairwise flatness across arbitrary components

Put F=grad k cross grad S. This field is C^(1,beta) and vanishes on the open set Q, so DF=0 there. At any y in Q,

    K_y f cross g_y+p_y cross H_y f=0.               (4)

Subtract (4) at x and x', divide by d, and put h'=(x'-x)/d. The exact result is

    ((K_x'-K_x)f/d) cross g_x'
      +K_x f cross ((g_x'-g_x)/d)
      +((p_x'-p_x)/d) cross H_x' f
      +p_x cross ((H_x'-H_x)f/d)=0.

The first and last terms have norm at most C d^(beta-1) r, because |p_x|+|g_x'|<=Cr. On the segment joining the two points the radius is at most r. Ambient integration of the Hessians along this segment gives

    (g_x'-g_x)/d=Hh'+O(r^beta),
    (p_x'-p_x)/d=Dh'+O(r^beta).

The segment need not be vortical. Only its endpoints were used in (4), and the scalars are defined on a neighbourhood of the full convex disc. The middle terms are therefore

    (Df) cross (Hh')+(Dh') cross (Hf)+O(r^beta)
      =8a sigma^2 sigma'(h'.f)(e cross f)+O(r^beta).

It follows that 8a sigma^3 |h'.f|<=C r^beta+C d^(beta-1)r. Multiply by d and use d<=2r and

    d r^beta=d^beta d^(1-beta)r^beta
       <=2^(1-beta)d^beta r.

This proves (1) without requiring common vortical components or a segment inside Q.

## 5. Consequences and the endpoint beta=1

On one line parallel to f, |(x'-x).f|=d, so d^(1-beta)<=Cr. At a fixed nonzero signed e-coordinate s, the cusp estimate makes r comparable with |s|. Thus the diameter of all vortical points on that line inside the small disc is at most (C|s|)^(1/(1-beta)). This bounds the union, even if it has several components.

For positive s and s' in [s,2s], Section 3 gives r<=C s and d<=C s, so (1) gives |u'-u|<=C s^(1+beta). The same statement holds for negative coordinates on replacing the interval by points of the same sign with comparable absolute values.

Homogeneity gives W(exp(tA)x)=exp(-t) exp(-omega t J)W(x) wherever the local flow is defined. Thus Q is locally X-invariant. The transverse flowbox projects vortical points approaching w to vortical points of T_r0 approaching w.

If the Hessians are Lipschitz, repeat Section 4 with beta=1. Every f-pair in Q near w would satisfy d<=C d r. Such a pair exists near every point of the open set Q. Taking a point sufficiently near the supported point w makes Cr<1, a contradiction. This is the prior A2037-A2038 exclusion, not an exclusion for beta<1. For beta<1, arbitrarily small positive d satisfies d^(1-beta)<=Cr; openness alone supplies no lower bound on d that could reverse the inequality.

## 6. Exact application to a W2 trace

For the actual-profile application retain the following additional assumptions. U is C2 on R3, P is C1, div U=0,

    (1-c)U+(Ay+U).grad U+omega JU+grad P=0,
    U.curl U=0, U(y)->0 uniformly,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1),
    p=(1-c)/c.

Assume the established C1 local tail convergence and scattering map hypotheses used in A1125,A1129,A1130,A1255. There is a lower-window W2 periodic carrier orbit, and a trace in its unstable set belonging to closure{curl U!=0} which escapes to infinity. Its covector rate rho is strictly less than -2(1-c). Let w be its supported scattering direction, and assume DV(w) has the nonzero saddle form in Section 1. Finally impose the additional C^(2,beta) regularity of the tail velocity near w. A1732 and A2035-A2036 then supply the local jets and identities of Sections 1-2. The present proof yields the stated necessary geometry.

No assertion here derives helicity freedom, the natural bounds, tail regularity or scattering convergence from bare velocity decay. The local calculation is valid for every omega; actual nonconstant W2 cycles already require omega!=0 by the preceding campaign results. Thus arbitrary omega is covered without constructing such a cycle at omega=0. No boundary integral, characteristic completeness assertion or exterior pressure normalization is used in this local audit.

## 7. Unsupported extension in Remark (lix)

The source correctly keeps the C^(2,beta) configuration OPEN, but its sentence "a C^(2,beta) exclusion would need a nonlocal input" is not proved. Checking the trace, selected Hessian entries, contact expansions and signs to their displayed order does not rule out another local argument, a higher compatibility condition or a sharper regularity mechanism. Nor does it construct jets satisfying every equation to all orders.

The approved reading is: the displayed estimates do not exclude the configuration, and whether another local or nonlocal argument excludes it remains open. The earlier mixed-type observation concerns only the displayed reduced system; it does not exclude every elliptic or other regularity mechanism. The radius in Section 1 is additionally restricted by the available neighbourhood. These scope clarifications do not change the estimates in Sections 2-5.

## 8. Evidence and limits

The source in the team records, the B65 claim and its symbolic tensor checker are hash-pinned in the team records. The full new proof and its standing local hypotheses, W2.17-W2.18 and Theorem FP(15) were read. The checker was read as corroboration; the three tensor identities needed above are derived directly in Sections 3-4 and no replay is required. This draft uses A1732 and A2035-A2038 only at their conditional scopes. The full C2 or C^(2,beta) configuration, the flat scattering direction and the unrestricted rotating decay-only problem remain open.
