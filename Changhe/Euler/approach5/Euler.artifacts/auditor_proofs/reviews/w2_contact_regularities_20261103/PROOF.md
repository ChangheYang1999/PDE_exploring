# Contact identities and regularity at an escaping W2 direction

## 1. Exact setting and local inputs

Fix 2/5 < c < 1/2 and any finite real omega. Let Jx = e_3 cross x, A = cI-omega J, X(x) = Ax, L = (1-c)I+omega J, a = 1-2c, b = 2-2c and q = b/a > 6. On a neighborhood in R^3 minus {0}, suppose V,P2 are C^2, and set W = curl V, k = X.V and S = P2-|V|^2/2. The local identities used below are

    div V = 0, DV X = -LV, -Delta P2 = tr((DV)^2),
    X.grad k = -ak, X.grad S = -bS,
    grad k cross grad S = 0 on VV = {W != 0}.

All statements up to the explicitly identified actual-profile conclusions follow from these identities and the additional point conditions stated below. Put F0 = {W=0}. Closures and interiors are relative to the local neighborhood. C^3 statements assume V,P2 are C^3 on a neighborhood, not merely that a pointwise second derivative exists.

For the W2 application, w != 0 is the scattering direction of an escaping lower-window W2 trace. The prior actual-profile results A1125, A1129, A1130 and A1255 supply

    V(w)=W(w)=P2(w)=S(w)=k(w)=grad k(w)=0,
    M=DV(w) symmetric, trace free, M X(w)=0.

In the supported nonflat case, A1255 further supplies DW(w)=0 and D2k(w)=-aM. These additional two identities are used only in that case below; they are not asserted at an arbitrary flat direction.

They also supply the dichotomy grad S(w) != 0 exactly at rho = -b, and grad S(w) = 0 when rho < -b. These conclusions retain the helicity-free profile class, the natural bounds

    |U(y)| <= C(1+|y|)^(-p), |DU(y)| <= C(1+|y|)^(-p-1), p=(1-c)/c,

and the established C1 local tail convergence and scattering hypotheses. The standing condition (D) is integral_1^infinity sup_{|y|>=r}|DU(y)| dr/r < infinity; the displayed natural bound implies it. These are additional to bare decay. Support of w is either an explicit premise or obtained from the C1 scattering law in Section 7. No assumption of vorticity density in a whole neighborhood is silently inserted.

If M != 0, set E = X(w)^perp. Then M|E has eigenvalues sigma,-sigma for sigma > 0, M^2|E = sigma^2 I and |M|_F^2 = 2sigma^2. A smooth twisted-flow chart is (t,h) mapped to exp(tA)(w+h), for h in a small disc of E. Since |V(w+h)| >= sigma|h|/2 for h != 0 small, its local zero set in the nonflat case is precisely the twisted orbit Gamma through w. The punctured chart, with Gamma deleted, is connected.

## 2. Elementary identities and component power law

The product rule, curl identity and homogeneity give

    grad k = -aV + X cross W,
    Delta k = -2omega W_3 - X.curl W,
    Delta S = -tr((DV)^2)-|DV|_F^2+V.curl W.

For example Delta k = 2 sum_ij A_ij partial_j V_i + X.Delta V; the first term is -2omega W_3, while Delta V = -curl W. Contracting the rank identity with X gives

    bS grad k = ak grad S on VV.

Thus each connected component C of VV intersect {k != 0} has a single finite constant D_C with S = D_C |k|^q. The algebraic constants satisfy (q-1)a = 1 and q(q-1)a^2 = b.

## 3. Contact identity with varying components

Let z lie in closure VV, with W(z)=DW(z)=0 and v=V(z) != 0. This is the full local premise; being off Gamma is only one way to guarantee v != 0 in the nonflat case. Write N=DV(z), G=|N|_F^2. Then N is symmetric and trace free. Since NX(z)=-Lv and L is invertible, G > 0. Section 2 gives

    grad k(z)=-av, D2k(z)=-aN, Delta k(z)=0, Delta S(z)=-2G.

Since grad k(z) != 0, its zero set is a regular surface near z. Every nonempty open subset of VV there contains points with k != 0. Choose any such sequence x_n tending to z, and allow its components and constants D_n to vary. Set alpha_n = qD_n |k(x_n)|^(q-2). Differentiating the power law inside each component gives

    S = alpha_n k^2/q, grad S = alpha_n k grad k,
    D2S = alpha_n[(q-1)grad k tensor grad k + k D2k].

Taking traces shows that alpha_n tends to

    alpha = -2G/((q-1)a^2|v|^2) < 0,

because the bracket tends to the strictly positive denominator. Passing to the limit in all three identities yields

    grad S(z) = (2G k(z)/|v|^2)v,
    S(z) = -2G k(z)^2/(b|v|^2),
    D2S(z) = -2G(v tensor v)/|v|^2 + (2G k(z)/|v|^2)N.       (1)

In particular

    |k(z)| = |grad S(z)||v|/(2G),
    G >= |grad S(z)|/(2|X(z)|),                              (2)

and k(z) != 0 if and only if grad S(z) != 0. The last inequality uses |k| <= |X||v| and also holds when both sides before cancellation are zero. The constants D_n are eventually negative.

If z is in the closure of one fixed component, k(z) cannot be zero: otherwise its fixed D would give alpha_n tending to zero, contrary to alpha < 0. At such a contact,

    D_C = -2^(q-1)G^(q-1)/(b |v|^q |grad S(z)|^(q-2)),
    |D_C||v|^(q-2) >= 3(1-c)/(2|X(z)|^q).                  (3)

For the inequality, the trace-free symmetric estimate |NX|^2 <= (2/3)G|X|^2 and |Lv| >= (1-c)|v| imply G >= 3(1-c)^2 |v|^2/(2|X|^2). Combine this with b|D_C||k|^(q-2)|v|^2 = 2G and |k| <= |X||v|. Since b=2(1-c), the constant in (3) follows. When k(z) != 0, the formula determines a fixed component constant or the limiting constant at a varying-component contact; it does not set every member of a varying sequence equal to the same number. At a C2 varying-component contact with k(z)=0, the constants instead diverge and this finite formula is not asserted.

## 4. The C2 equality-rate exclusion

Assume w is supported, M != 0 and ell=grad S(w) != 0. The vector field F=grad k cross grad S is C^1 and is zero on the open set VV. Therefore DF is zero there, and DF(w)=0 by continuity and support. Since grad k(w)=0,

    DF(w)[h] = -a(Mh) cross ell.

Consequently the range of M lies in the line spanned by ell, contradicting its rank two. This excludes a supported nonflat W2 direction at the equality rate rho=-b under C2 tail regularity, without an interface or density argument. It does not exclude a flat supported direction or a nonflat strict-rate direction at this regularity.

## 5. The C2 strict-rate necessary structure

Assume w is supported, M != 0 and grad S(w)=0. Write H=D2S(w). Differentiating X.grad S=-bS gives HX(w)=0, so H maps E into E. The Poisson identity gives tr H = -2|M|_F^2 = -4sigma^2.

Let Z0 = closure VV intersect closure(int F0), with Gamma deleted. This set meets every sufficiently small punctured flow chart. Otherwise int F0 would be both open and closed in that connected punctured chart. It cannot be the whole chart because w is supported, so it would be empty. VV would then be dense, extending the rank identity to the entire chart. Taylor expansion would give (Mh) cross (Hh)=0 for every h in E. Since M|E is invertible, H|E would be a scalar multiple of M|E, forcing trace zero, a contradiction.

At every point of Z0, W=DW=0 because W is C1 and vanishes on int F0. In the nonflat case V != 0 off Gamma, so Section 3 applies. Project contacts by the twisted flow to w+s_n e_n, with s_n tending to zero and unit e_n tending to e in E. Put m=e.Me. Taylor expansion in the signed identities (1) gives

    He = -2a m Me,
    H = -4(Me tensor Me)-2a m M.

Indeed k/s_n^2 tends to -am/2, V/s_n tends to Me, |V|^2/s_n^2 tends to sigma^2 and G tends to 2sigma^2. Applying the second limit to e gives He=-(4+2a)mMe; comparison with the first forces m=0 and He=0. For a unit f in E perpendicular to e this proves

    D2S(w)=-4sigma^2 f tensor f,
    D2P2(w)=sigma^2 e tensor e-3sigma^2 f tensor f,
    D2S(w)X(w)=D2P2(w)X(w)=0.                             (4)

The prior exact transverse expansion A1256 also follows here by expanding bS grad k=ak grad S to degree three along any vortical sequence. With D=-aM it gives

    b(e.He)De = a(e.De)He.

For H in (4), this forces every transverse limiting vortical direction into ker H, namely the line R e. This line is a null line of M. This statement is about a transverse section or projection along the twisted flow, not every direction in three dimensions.

Finally if the D_n were bounded along any vortical k != 0 sequence tending to w, alpha_n=qD_n|k|^(q-2) would tend to zero. The bracket in the trace identity of Section 3 stays bounded, so Delta S would tend to zero, contradicting Delta S(w)<0. Thus |D_n| tends to infinity along every such sequence, and no fixed component has w in its closure. These are necessary conditions, not a construction or an exclusion at C2.

## 6. Flat equality-rate interfaces

Retain the actual-tail inputs and assume C2 tails, w supported, grad S(w) != 0 and w outside closure Z, where Z=int{k=0}. Section 4 forces M=0. Since grad S stays nonzero and {k=0} has empty interior locally, the scalar relation on VV implies VV is contained in {k != 0, S != 0} locally. To check a possible regular S-zero inside VV, choose a small ball contained in VV. Its two local sign sides have k=C|S|^(1/q); C1 regularity and 1/q < 1 force both constants to be zero. This would put an open set inside {k=0}, a contradiction. A k-zero with S != 0 gives the same contradiction directly.

At a contact in Z0 with V != 0, (2) bounds |DV|_F^2 below by |grad S|/(2|X|), which stays bounded away from zero near w. But DV tends to DV(w)=0. Thus all sufficiently near contacts are velocity zeros. Contacts must occur off Gamma in every punctured flow chart: otherwise the connectedness argument makes VV dense near w. The actual-profile dense-zero theorem A1096 would then give grad P2(w)=0, contradicting grad S(w) != 0 and V(w)=0. The use of A1096 here is explicit and uses its actual-profile and natural-bound scope; this last conclusion is not asserted for every abstract local tail system.

## 7. Support from scattering

Assume the C1 scattering map Xi exists on an open escaping neighborhood of the original trace point y0, with

    W(Xi(y))=DXi(y)Omega(y), det DXi(y)=1.

If y0 is in closure{Omega != 0}, take vortical y_n tending to y0. The escaping set is open because the orbit enters the outward region in finite time; continuous dependence supplies a neighborhood doing the same. Invertibility of DXi gives W(Xi(y_n)) != 0. Since Xi is continuous, Xi(y_n) tends to w=Xi(y0), proving w belongs to supp W. The determinant law follows from det DPhi_t=e^(3ct) and det exp(-tA)=e^(-3ct), followed by the C1 derivative limit. It needs that derivative convergence, not just convergence of Xi as a map.

This removes the separate support premise for the escaping W2 application under exactly that scattering hypothesis.

## 8. The C3 exclusion at every rate

Assume V,P2 are C3 near a supported W2 direction. If M != 0, Section 4 gives grad S(w)=0. Now F=grad k cross grad S is C2, and D2F=0 on VV extends to w. The two vanishing gradients eliminate the third-derivative terms at w, leaving

    D2F(w)[h,h]=2(Dh) cross (Hh)=0, D=-aM.

Both D and H annihilate X(w) and preserve E, and D|E is invertible. Hence the linear map H|E (D|E)^(-1) sends every vector to a parallel vector and is a scalar multiple of the identity. Thus H|E=lambda D|E has trace zero. This contradicts tr H=-4sigma^2. Therefore M=0.

Combining with Section 7, every escaping lower-window W2 direction in this C3-tail class is a T0 point in the precise finite-jet sense

    V=DV=W=0, S=P2=0 at w.

This does not by itself assert infinite flatness of V or S, nor that w is an interior point of T0. Any use of the common infinitely flat frontier requires the additional hypotheses of the corresponding earlier theorem. C3 regularity of the original profile alone is not substituted for C3 regularity of its tail.

## 9. C3 excludes a zero k at every nonzero-velocity contact

At a Section 3 contact with C3 tails, suppose k(z)=0. Then (1) gives S=grad S=0 and D2S=lambda p tensor p, with p=grad k=-av != 0 and lambda=-2G/(a^2|v|^2) != 0. The C2 field B=k grad S-qS grad k vanishes on VV, so D2B(z)=0 by support. The product rule gives

    D2B(z)[h,h]=(2-q)lambda(p.h)^2 p.

Taking h=p contradicts q>2. Thus k(z) != 0 and grad S(z) != 0, even when the approximating components vary. Formula (3) applies exactly to any fixed component whose closure contains z. For varying components its right side is the limit of their constants, not an asserted equality for each constant.

## 10. General jet constraint and two qualifications

For arbitrary C2 k,S with the rank relation on an open set accumulating at w, grad k(w)=0 and rank D2k(w)>=2 imply grad S(w)=0 by Section 4's derivative argument. If k,S are C3, the second derivative gives (Dh) cross (Hh)=0 for all h. In fact H=lambda D on the whole space: on the range one uses two independent images of D; if z is in ker D, compare h and h+z for those two images to get Hz=0. This is stronger than the source's restriction to the kernel complement.

The submitted general formula for D2k omits a product-rule term. The correct expression is

    D2k(w)[h] = -aDV(w)h + (Ah) cross W(w) + X(w) cross DW(w)h.       (5)

The middle term vanishes at the W2 points, so every W2 proof above remains valid. It cannot be dropped merely because grad k(w)=0 or k(w)=0. For example when omega=0, the smooth local homogeneous divergence-free field V(x)=|x|^(-p-1)(e_3 cross x), away from zero, has k identically zero and W nonzero on the equatorial plane when p>1. Its omitted term is nonzero. This tests the claimed general differentiation formula; it is not an actual global profile counterexample.

In the surviving C2 nonflat configuration, if third derivatives exist at vortical points, differentiating the rank relation there gives

    2|D2k h cross D2S h| <= |grad S||D3k[h,h,.]| + |grad k||D3S[h,h,.]|.

With h=f in (4), the left side tends to 8a sigma^3 > 0, while both gradients tend to zero. Thus those third derivatives cannot remain bounded along such a sequence. C2 regularity alone does not supply third derivatives at those points, so the statement needs this existence qualification.

## 11. Source comparison, scope and verdict

The complete submitted subsection 3f-ter, its Theorem FP items 12-13, and the prior transverse and dense-zero proofs were read. The contact identities, C2 equality exclusion, C2 strict-rate necessary structure, conditional flat interfaces, support transfer, C3 exclusion and C3 contact lemma are CONFIRMED at the scopes above. Equation (5) repairs the source's general parenthetical formula. The third-derivative and varying-component qualifications in Sections 9-10 are retained. Theorem FP item 12 should introduce the nonflat assumption for parts (a)-(b), not for its separate flat part (c).

No characteristic completeness claim is added: the actual W2 and scattering inputs already supply the escaping flow, and the new arguments are local. No pressure constant is reset: P2 and S use the canonical tail normalization of those inputs. Every finite omega is allowed; constants need not be uniform as |omega| tends to infinity. The full bare-decay arbitrary-helicity problem remains OPEN. No computation or formal build was used.

The submitting agent is configured model; its quoted referee is the external referee (a second model). Existing model configured agents receive this comparison through the shared notes. The configuration is not independent provider runtime attestation, and no new model client was invoked.
