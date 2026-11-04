# Low-pressure boundaries and a sharp local negative-pressure example

## 1. Exact hypotheses

Fix 2/5<c<1/2 and finite real omega. Set Jx=e3 cross x, A=cI-omega J, X=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), q=b/a>6 and eta=1/q. On an open G in R3 minus {0} let V,P be smooth. Write W=curl V, k=X.V, E=|V|^2 and S=P-E/2. Assume the reduced tail identities

    div V=0, V.W=0, DV X=-LV, -Delta P=tr((DV)^2),
    grad k=X cross W-aV, X.grad S=-bS, W.grad S=0,
    k grad S=qS grad k on supp W.                         (T)

Every support, closure, interior and boundary below is relative to G. For fixed 0<delta<1/2 put epsilon=1/2-delta,

    Z_delta={P<delta E}, Y={W!=0} intersect int{k=0},
    N_delta=Z_delta intersect Y, H=-S, R=E/H on {S<0}.

The separate profile premise used only when indicated is that V,P are the actual smooth tails V,P2 of a whole-space C2/C1 zero-helicity profile in the target range with the natural bounds |U|<=C(1+|x|)^(-p), |DU|<=C(1+|x|)^(-p-1), p=(1-c)/c, and the established natural tail normalization. The confirmed C49/A1321 consequence is P2>=0 at every supported common zero of V and W. In the statements below it suffices to assume this sign consequence itself. It is not included in (T).

We prove the ratio and local potential representation, all boundary alternatives, an analytic local example with V=W=0 and P=-1 in supp W, and the exact orbit statements of C57. The analytic example satisfies (T), not the separate global profile premise.

## 2. The ratio set and its local potential

On Y, k and grad k vanish, so aV=X cross W. The vector triple-product identity and the two scalar transport laws imply

    a grad S cross V=bS W.

Since W is nonzero on Y, V=0 there implies S=0. Thus V is nonzero on Y intersect {S<0}. Also P<delta E is equivalent to H>epsilon E and therefore to S<0 and R<1/epsilon. This proves

    N_delta=Y intersect {S<0} intersect {R<2/(1-2delta)}.

On this negative-scalar open set,

    grad H cross V=qH W,
    curl(H^(-eta)V)=H^(-eta)W-eta H^(-eta-1)grad H cross V=0.

On any ball B contained in it, the Poincare lemma gives a smooth scalar phi with V=H^eta grad phi. Then X.grad phi=0, div(H^eta grad phi)=0 and grad phi is nonzero throughout B. On N_delta intersect B the ratio inequality gives

    |grad phi|<epsilon^(-1/2)H^(1/2-eta),

with 1/2-eta>1/3. The primitive is asserted on each ball, not globally across arbitrary components or their zero boundaries.

## 3. Complete boundary classification

Let y be in boundary N_delta. Since N_delta is open, y is outside it and is a limit of its points. Thus y is in supp W and P(y)<=delta E(y). Every derivative of k vanishes on the open set N_delta and hence, by smoothness, at y.

If W(y)!=0 and P(y)<delta E(y), then S(y)<0. On a neighborhood where W and S are nonzero, (T) gives grad(k|S|^(-1/q))=0. Since k(y)=0 this forces k=0 nearby, putting y in N_delta, a contradiction. Hence P(y)=delta E(y). If V(y)=0, then S=P=0. One can see this directly from grad k=0: X cross W=0, so X is a multiple of the nonzero W and X.grad S=W.grad S=0 up to that multiple; homogeneity gives S=0. If V(y)!=0, then S=(delta-1/2)E<0, the same inverse-rank argument places y in Y, and R(y)=1/epsilon.

If W(y)=0, grad k(y)=0 and the contraction identity imply V(y)=0. Thus P(y)=S(y)<=0. The two alternatives are S(y)<0, the negative-pressure common-zero type (c2) of C56, or S(y)=P(y)=0. These alternatives and the two preceding W!=0 alternatives are exhaustive and disjoint.

Under the separate sign premise, S<0 at a supported common V/W zero is impossible. In every remaining case P(y)=delta E(y). No assertion of constant potential, zero normal flux or boundary smoothness follows from this equality.

## 4. Analytic ansatz and elimination of third derivatives

Near x*=e1 use the analytic quotient coordinates

    pi(x)=exp((omega/c)log|x| J)x/|x|,
    u=pi_2(x), v=pi_3(x).

These are constant along X and restrict to the usual coordinates (n2,n3) on the sphere near e1. For analytic functions f(u,v), h(u,v)>0 define

    phi(x)=f(u,v), H(x)=|x|^(-b/c)h(u,v),
    V=H^eta grad phi, S=-H, P=-H+|V|^2/2.

Then X.grad phi=0 and X.grad H=-bH. Direct differentiation gives DV X=-(aI+A^T)V=-LV and

    W=eta H^(eta-1)grad H cross grad phi.

Thus k=0, V.W=0, W.grad S=0 and scalar homogeneity hold. The contraction identity follows from differentiated homogeneity, and the rank equation is 0=0. Moreover W=0 if and only if grad phi=0: if grad phi were nonzero and parallel to grad H, contraction with X would contradict X.grad phi=0 and X.grad H=-bH!=0.

Only divergence and Poisson remain. Let

    d=div V, F=H^(-eta)d=Delta phi+eta grad(log H).grad phi,
    H2=H^(2eta), E2=Delta P+tr((DV)^2).

The product rule gives the exact identity

    E2=E2s+H2 grad phi.grad F,

where

    E2s=-Delta H+(|grad phi|^2/2)Delta H2
       +2 grad H2.(D2phi grad phi)+H2|D2phi|^2
       -eta H2 grad phi.grad(grad(log H).grad phi)
       +tr((DV)^2).

Here DV=H^eta D2phi+grad phi tensor grad(H^eta). This verifies the matrix order and shows that E2s contains no third derivative of phi, no derivative above second order, and is affine in D2H. The cancellation follows by substituting grad(Delta phi)=grad F-eta grad(grad(log H).grad phi) in the differentiated energy.

The ansatz gives d(F_t x)=exp(-t)d(x) and E2s(F_t x)=exp(-2t)E2s(x), where F_t=exp(tA). For the second equality, every term has scalar weight 2: b+2c=2 for Delta H and 2a+4c=2 for the terms with two factors of the potential derivatives. Rotations cancel in full contractions. Thus it suffices to solve d=E2s=0 on the transverse sphere. Their homogeneity then gives both identities on a flow neighborhood, where d=0 implies F=grad F=0 and hence E2=0.

## 5. Normal form and the negative-pressure common zero

Restrict the preceding two equations to the sphere. The divergence equation is affine in the second derivatives of f and contains only first derivatives of h. Its coefficient of f_vv is H^eta|grad v|^2, strictly positive near e1. Solve it analytically for f_vv and substitute into E2s. The coefficient of h_vv there is

    -|grad v|^2+O(|grad f|^2)

on the sphere. In detail the leading term comes from -Delta H. The only other second derivatives of H arise in (|grad phi|^2/2)Delta H2 and -eta H2 grad phi.grad(grad(log H).grad phi); both carry two factors of grad phi. Substituting f_vv introduces no h_vv because the divergence equation used no second h derivatives.

Prescribe analytic data along v=0:

    f(u,0)=u^2/2, f_v(u,0)=0,
    h(u,0)=1, h_v(u,0)=0.

At u=v=0 the potential gradient vanishes, and the two normal coefficients are 1 and -1, since grad v(e1)=e3 and H(e1)=1. The equations therefore solve analytically for f_vv,h_vv in terms of u,v, first jets and the remaining second derivatives f_uu,f_uv,h_uu,h_uv. This is a Cauchy-Kovalevskaya system in normal form. The analytic existence and uniqueness theorem, with real data and coefficients, supplies a real analytic local solution. Shrink the domain to keep h>0 and reconstruct the fields on a ball B about e1. Section 4 proves all of (T) there.

The external theorem used is Gantumur's Theorem18 and higher-order Corollary20, whose statements and proofs on printed pages9-11 of the retained 2011 primary notes were reread. Equivalently set the unknown first-jet vector to (f,f_u,f_v,h,h_u,h_v): its v derivatives use only that vector and its u derivatives, in analytic first-order normal form. This also checks the mixed-derivative compatibility assumed by the second-order notation.

At e1, grad phi=0, so V=W=0, while H=1 and P=S=-1. Along the sphere line v=0 with u!=0, f_u=u!=0. Independence of grad u and grad v gives grad phi!=0 and hence W!=0. These points approach e1, which therefore belongs to supp W. The analytic scalar phi is not constant on the connected ball, so its critical set has empty interior and supp W=B. Since E/H tends to zero at e1, shrink a neighborhood to have R<2 there. Every noncritical point in that neighborhood belongs to N_delta for every 0<delta<1/2; e1 itself is a boundary point of the negative-pressure type.

This exact analytic construction proves the sign law is not a consequence of (T), even with analyticity and dense vorticity. It has no common flat point, gives no whole-space tail or profile, and does not contradict the global C49 sign theorem.

## 6. Orbit and compactness statements

Along each linear-flow segment remaining in G, P and E scale by exp(-bt), k by exp(-at), and

    V(F_t x)=exp(-(1-c)t)O_t V(x),
    DV(F_t x)=exp(-t)O_t DV(x)O_t^T,
    W(F_t x)=exp(-t)O_t W(x), O_t=exp(-omega tJ).

The formulas hold on an open neighborhood of the initial point because the entire finite orbit segment is compactly contained in G. They preserve the strict sign P-delta E<0, nonvanishing W and a whole neighborhood where k=0. Hence the orbit segment stays in N_delta, in its original component.

If a component had compact closure K contained in G, every forward orbit starting in it could be continued inside G for all positive times: a finite first exit would have its endpoint in K, where openness allows continuation. Such an orbit stays in K but its radius exp(ct)|x| tends to infinity, a contradiction. Thus no component has compact closure contained in G. If G is forward invariant, the entire forward orbit lies in its component and makes that component unbounded. This applies to an exterior ball domain. No completeness inside a general G is assumed without the preceding argument.

## 7. Sharp elliptic threshold and unresolved continuation

The previously confirmed coupled principal symbol is invertible elliptic exactly when R<q. Section 2 therefore puts N_delta in that region if delta<=1/2-1/q. The threshold is sharp for (T): if delta is larger, choose theta with 1/2-delta<theta<1/q and use the confirmed C56 vortical local family, whose free harmonic pressure coefficient realizes S/E=-theta at e1. Then P/E=1/2-theta<delta while R=1/theta>q and W!=0,k=0. All conditions hold on a sufficiently small neighborhood. This sharpness does not involve an actual global profile or a flat point.

The bound for grad phi on N_delta does not prove continuation at a flat common zero. The coefficient H^eta may itself vanish to infinite order; the normalized drift eta grad(log H) is uncontrolled, the primitives are local, and the boundary classification gives no constant potential or zero flux. The example above settles the local sign distinction only. Common-flat exclusion, global matching and the arbitrary-helicity bare-decay conjecture remain open.

All four source sections and all remarks, the full eight-section C56 audit, the full seven-section CO62 audit and the stated primary analytic existence proofs were read. The submitting agent's numerical checks were not rerun and are not proof evidence. No computation or formal build was used. Source pins and dependencies are retained. Existing configured model Theory Agent C receives the audit through files; actual provider runtime remains independently unattested.
