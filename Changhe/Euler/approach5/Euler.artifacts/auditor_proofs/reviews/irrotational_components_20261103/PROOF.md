# Irrotational components and the tail regularity ledger

## 1. Statement and hypotheses

Let 1/3<c<1/2 and omega be any finite real number. Write Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2-2c and m=a/c. Let V be a C1 vector field on R3 minus {0}, satisfying

    div V=0, DV X=-LV.

Set W=curl V and k=X.V. Then the following holds. If O is an open set invariant under exp(tA), W=0 in O, and V=0 on its boundary relative to R3 minus {0}, then V=0 in O. No pressure, helicity, rank identity or boundary regularity is needed for this assertion.

A connected component of int{W=0} on which V is nonzero has a boundary point with V nonzero, lying in the support of W. At C1 velocity regularity W=0 at that contact. If V is C2 on a neighborhood of the contact, then DW=0 there as well. The additional contact identities involving S=P2-|V|^2/2 require the C2 Poisson and rank hypotheses of A1729.

The subsequent local no-bubble result retains the actual-profile hypotheses of A1733: a helicity-free profile with the natural U and DU bounds, its established tail and scattering limits, an escaping lower-window W2 direction w, a C2 tail near w, grad S(w) nonzero, w in supp W and w outside closure Z, where Z=int{k=0}. In particular this is the equality-rate branch rho=-b. It is not asserted for every T0 point.

## 2. The global harmonic potential and quotient equation

The product rule gives grad k=A^T V+DV^T X. Since (DV^T-DV)X=X cross W and A^T-L=-aI,

    grad k=-aV+X cross W,       X.grad k=-ak.

On O, grad k=-aV. Thus k is C2 there and Delta k=-a div V=0. Consequently -k/a is a globally defined harmonic potential for V on O, even if O is not simply connected. This does not involve an unproved zero-period hypothesis: the explicit scalar k supplies the potential. On boundary O, k=X.V=0 directly.

Every orbit of exp(tA) meets S2 exactly once, because |exp(tA)x|=exp(ct)|x|. The smooth quotient map is

    q(x)=exp((omega/c) log|x| J) x/|x|.

The invariant scalar |x|^m k(x) is therefore a function Psi on the open quotient domain D=q(O) in S2. It is continuous on closure D, and is zero on boundary D. Saturation identifies the relative boundary of O with the inverse image of boundary D. In spherical coordinates, with eta=phi+(omega/c)log r and k=r^(-m)Psi(theta,eta), the radial operator r partial_r acts as -m+(omega/c)partial_eta. Therefore Delta k=0 is equivalent to

    L_m Psi=0,
    L_m=Delta_S+(omega/c)^2 Y^2+(omega/c)(1-2m)Y+m(m-1),

where Y is the smooth rotation field on S2. In a spherical chart Y=partial_eta. Its principal quadratic form is |xi|^2+(omega/c)^2(Y.xi)^2, so it is uniformly elliptic on S2 for each finite omega, including at the coordinate poles. No estimate uniform in the size of omega is required by the maximum argument.

## 3. Maximum principle with an arbitrary boundary

Since 0<m<1, the zeroth-order coefficient m(m-1) is strictly negative. If Psi has a positive value, it attains a positive maximum on compact closure D. The boundary value is zero, so a maximum occurs in D. There the gradient vanishes and the Hessian is negative semidefinite. The elliptic principal term is nonpositive and m(m-1)Psi is strictly negative, contradicting L_m Psi=0. Applying the same argument to -Psi rules out a negative value. This proof also works when D=S2, and needs no smoothness of boundary D.

Hence Psi=k=0 on O and V=-grad k/a=0. The lower endpoint c=1/3 cannot simply be inserted: for every omega the field V(x)=Kx/|x|^3, K nonzero, is C-infinity off zero, divergence free, irrotational and twisted homogeneous with the required degree at c=1/3. Taking O=R3 minus {0} makes its boundary empty while V is nonzero. This is a singular tail example, not a smooth global profile counterexample. Neither S nor P2 has the favorable scalar coefficient: their positive exponent b/c gives (b/c)(b/c-1)>0 in the target range, so this maximum argument does not apply to them.

## 4. Global components and contact regularity

Let O be a connected component of int{W=0}. The path t mapped to exp(tA)x stays in int{W=0} by the homogeneous curl law and is connected, so the whole orbit of each x in O remains in O. Thus O is saturated.

Every boundary point z of O belongs to supp W. Otherwise some ball centered at z is contained in int{W=0}. That connected ball intersects O and would belong to the same component, contrary to z being a boundary point. Continuity also gives W(z)=0. If V vanished on every boundary point, Sections 2-3 would force V=0 on O. Therefore any nonzero component has a contact with V(z) nonzero.

A component O has V=0 identically if and only if O is contained in Z. One direction uses k=X.V; the other uses grad k=-aV on O. This equivalence is about irrotational components, not about all components of Z.

If V is C2 near z, W is C1 there and DW=0 on O. Continuity then gives DW(z)=0. The literal claim in B62 that W is C1 under only C1 tail regularity is incorrect: C1 V gives continuous W, not C1 W. Move DW(z)=0 inside the C2 qualification. This regularity correction leaves the maximum principle and the nonzero boundary contact intact.

With C2 V,P2, the Poisson equation and rank identity of A1729, the nonzero-velocity contact satisfies, with v=V(z), N=DV(z) and G=|N|_F^2>0,

    grad S(z)=2Gk(z)v/|v|^2,
    S(z)=-2Gk(z)^2/(b|v|^2),
    D2S(z)=-2G(v tensor v)/|v|^2+2Gk(z)N/|v|^2.

Thus k(z) and grad S(z) vanish together. At C3 the A1736 differentiated component identity excludes k(z)=0, including contacts of varying components. These are local conclusions at the contact obtained above; the contact need not be arbitrarily close to a chosen flat point.

## 5. The precise local no-bubble consequence

Use a small transverse disk T centered at w and its full flow saturation, not merely a box with finite time endpoints. Equivalently choose a relatively compact disk D0 about q(w) on the quotient sphere. Shrink it so its full inverse image avoids Z, and so every interior interface between int{W=0} and supp W has V=0, as supplied by A1733. The orbit through w also has V=0. These facts are preserved by the twisted scaling.

Suppose a connected component C of the irrotational open set in this saturated neighborhood has quotient closure disjoint from boundary D0. Every boundary point of C then lies on an interior vortical contact or on the central orbit. There are no artificial time-end boundaries because the neighborhood is fully saturated. V vanishes at all those points. Sections 2-3 apply to C, giving V=0 and hence C contained in Z, contrary to the choice of D0.

Consequently the closure of each such irrotational component meets the transverse boundary. This is the exact meaning of reaches the boundary. It does not assert that the boundary point lies inside the open component. It does not exclude components which leave the small neighborhood and encounter nonzero velocity farther away.

## 6. Source integration repairs

The revised Theorem FP(12), copied to REPORT_SECTION_B, correctly separates the nonflat cases (a)-(b) from the flat case (c). However its opening contact formula now lost the explicit premise V(z) nonzero. Being off the orbit does not imply it in the flat case, and the displayed quotients are undefined at V=0. Indeed case (c) itself places the accumulating contacts in {V=0}. Add V(z) nonzero to the opening contact premise, also in THEOREM_B_SUMMARY S11(g). EXACT_IDENTITIES I17 already retains that premise for its contact formula.

I17 has a separate overstatement in its last scattering-direction parenthesis. In general the exact homogeneity derivative is

    D2S(w)X(w)=-(bI+A^T)grad S(w).

It is zero in the strict-rate branch, or after the supported nonflat equality case has been excluded. It is not zero at an equality-rate direction with grad S(w) nonzero, since bI+A^T=(2-c)I+omega J is invertible. Likewise D2k=-aDV uses DW=0, or the independently established nonflat W2 jet input; V=W=0 alone does not supply it. Restrict this last I17 parenthesis to the supported nonflat contradiction branch, and state grad S=0 before using D2S X=0. The general Hessian formula with the (Ah) cross W term is now correctly repaired.

The finite-jet T0 scope, the existence qualification on third derivatives and the limiting-constant interpretation for varying components are correctly integrated in the reviewed B59-B61 changes. The global common-flat residual must still be distinguished from pointwise infinite flatness at every T0 point.

## 7. Scattering and a pressure-regularity simplification

The provenance claim that C1 scattering is automatic under the natural U and DU bounds is correct. For p=(1-c)/c, an escaping orbit has radius comparable to exp(ct), locally uniformly in its initial point. The variation-of-constants integrand exp(-tA)U(Phi_t y) is O(exp(-t)). The derivative Q_t=exp(-tA)DPhi_t solves

    Q_t'=exp(-tA)DU(Phi_t y)exp(tA)Q_t.

The matrix coefficient is O(exp(-t)); scalar dilation cancels in this conjugation and rotation is orthogonal. Gronwall and integration give locally uniform convergence of Q_t and hence C1 convergence to Xi. Since div B=3c, det Q_t=1 for all t and det DXi=1. The exact curl Cauchy law and local C1 tail convergence then yield W(Xi y)=DXi(y)Omega(y). This reconstructs the part of A209-A210, A538-A539, A1005 and A1325 used by B60 without a vorticity-density premise.

A539 already supplies P2 in C^(2,alpha)_loc for every alpha<1 under the natural bounds. Thus the added C2 tail premise is only V in C2 near w. The C3 premise can also be written using V alone: if V is C3 near w, f=-tr((DV)^2) is C2, so its first derivatives are locally Lipschitz. The distributional equation Delta P2=f and interior Poisson Schauder regularity, applied on successively smaller balls, imply P2 in C^(3,alpha)_loc for every alpha<1. The harmonic ambiguity is smooth and causes no loss. Hence V in C3 near w suffices for both C3 fields required by A1735-A1736. This uses the same standard local elliptic regularity input as A539, not an additional pressure normalization or decay assumption.

## 8. Scope and verification

B62's main maximum principle and its two properly qualified consequences are confirmed. The missing derivative regularity, missing nonzero contact premise and I17 scattering-jet shorthand require the repairs in Sections 4 and 6. The C3 pressure simplification in Section 7 is an independent strengthening.

The full B source subsection and changes to its claim ledger were read, together with the relevant report, summary and exact-identity passages. Source copies and hashes are in verification. Earlier A1729-A1740 and A209-A210/A538-A539 supply the explicitly identified dependencies. No numerical computation or formal build was run. Existing configured model agents remain the file-based collaborators; the actual provider runtime is not independently attested. This argument does not exclude all irrotational patches, prove the missing C2 strict-rate exclusion or settle the bare-decay, arbitrary-helicity problem.
