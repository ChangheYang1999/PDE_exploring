# Boundaries of open scalar-zero regions are supported flat velocity zeros

Status: CONFIRMED A973-A974 after complete independent derivation and postread. This is a consequence of the confirmed noninterior-node exclusion, not a proof excluding open zero regions.

## 1. Statement and hypotheses

Fix 2/5<c<1/2 and any finite real omega. Write Jx=(-x2,x1,0), A=cI-omega J, X(x)=Ax, E=(1-c)I+omega J, a=1-2c and p=(1-c)/c. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    (1-c)U+DU(Ax+U)+omega JU+grad P=0,
    U.curl U=0,
    |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1)

for a finite constant C. Let V in C1(D;R3), D=R3 minus{0}, be its actual velocity tail, W=curl V, k=X.V, and K=k restricted to S2, G=W restricted to S2. The actual tail has the identities

    V(exp(tA)x)=exp(-tE)V(x), div V=0,
    DV(x)X(x)=-EV(x), grad k=X cross W-aV.             (1)

By A963/A970, every zero of k with W!=0 is an interior zero in D. The sphere is a global transverse section of the twisted rays exp(tA)x, since |exp(tA)x|=exp(ct)|x|. Thus interior and boundary statements for zero sets of K correspond exactly to those on their twisted cones.

Set

    Z={w in S2:K(w)=0}, A0=int_S2 Z,
    Tflat={w in S2:V(w)=0,DV(w)=0} intersect supp_S2 G.

Here DV is the full ambient derivative, and supp_S2 G is the closure of the angular set {G!=0}. Then

    boundary_S2 A0 subset Tflat.                       (2)

Consequently, if Tflat is empty, either K is identically zero on S2, or U is identically zero on R3. In particular, if K is not identically zero and Tflat is empty, U=0. The hypotheses of zero helicity and natural gradient decay are not removed. The case K identically zero remains open in this argument.

## 2. First-order data at an open-zero boundary

Let w belong to boundary A0. Because Z is closed, K(w)=0. Since A0 is open, w does not belong to A0. Thus w is a noninterior zero of K. The sphere-to-cone correspondence and A963 give W(w)=0.

Moreover grad k(w)=0. Indeed k vanishes on the open twisted cone over A0, so its full ambient gradient vanishes there. There are points of A0 tending to w; continuity of grad k gives this assertion at w. Equation(1) now gives V(w)=0, since a>0.

The same argument holds at every boundary point, so

    boundary A0 subset {V=0,W=0,grad k=0}.              (3)

This assertion concerns boundary A0. It does not concern every point of boundary Z: isolated zero curves outside the closure of A0 may be regular irrotational zeros with nonzero velocity.

## 3. A nonflat angular zero would be isolated

Suppose M=DV(w) is nonzero. Since W(w)=0, M is symmetric. Since div V=0, its trace is zero. Equation(1), with V(w)=0, gives M X(w)=0. The vector X(w) is nonzero because w.X(w)=c>0.

A nonzero real symmetric trace-free 3-by-3 matrix with a nontrivial kernel has eigenvalues nu,-nu,0 for some nu!=0. In particular it has rank2 and kernel exactly R X(w).

The tangent plane T_w S2 is transverse to X(w), again because w.X(w)=c>0. Therefore M restricted to T_w S2 is injective and maps that two-dimensional plane isomorphically onto image M. Let P_M be orthogonal projection to image M. In a smooth angular chart centered at w, the derivative of the map P_M V into this fixed two-dimensional space is this isomorphism. The C1 inverse-function theorem implies that P_M V, hence V itself, has no zero other than w in a sufficiently small angular disk D0 about w.

By(3), this disk has no boundary point of A0 other than w. The punctured disk D0 minus{w} is connected. Its intersection with A0 is relatively open, and is also relatively closed because every relative boundary point would lie in boundary A0. It is nonempty since w is in the closure of A0 and w itself is not in A0. It must therefore be the entire punctured disk.

K vanishes on that punctured disk, and also at w by continuity. Thus it vanishes throughout D0, making w an interior zero. This contradicts w in boundary A0. We conclude M=0, which proves

    boundary A0 subset {V=0,DV=0}.                     (4)

No second derivative of k, smooth boundary of A0, finite number of components, or transverse differentiability of W is assumed.

## 4. Every such boundary point lies in the support of vorticity

Suppose instead that w is outside supp_S2 G. Then W vanishes on an angular neighborhood of w and, by twisted homogeneity, on its open cone in D. Choose a connected Euclidean ball B0 about w in that cone. There div V=curl V=0, so every component of V is harmonic in distributions and hence smooth and real analytic.

The scalar k=X.V is also harmonic there. In coordinates,

    Delta k=X.Delta V+2 sum_(i,j) A_ij partial_j V_i.

The first term is zero. Since DV is symmetric and trace free, the contraction with A=cI-omega J vanishes: its scalar part is c div V=0 and its skew part contracts to zero with the symmetric DV. Thus Delta k=0.

The ball meets the open cone over A0 in a nonempty open set, because w belongs to its boundary. On that open subset k=0. Analytic uniqueness for harmonic functions gives k=0 throughout the connected ball B0. This makes w an interior angular zero, the same contradiction as before. Therefore w lies in supp_S2 G. Combining this with(4) proves(2).

Only local harmonic uniqueness is used. There is no assumed unique continuation for the full Euler system or across a vortical boundary.

## 5. Consequence when supported flat zeros are absent

If Tflat is empty, (2) makes boundary A0 empty. The set A0 is open and then also closed in the connected sphere, so A0 is either empty or all of S2.

If A0 is all of S2, then K is identically zero. This is one of the two alternatives in the statement.

If A0 is empty, A963 implies that no zero of K is vortical. Therefore the nodal premise N, namely {k=0} subset {W=0} on D, holds. The already confirmed conditional concentration theorem A914, equivalently A834 with N, says that N and absence of Tflat force U=0. Its exact hypotheses are the actual global hypotheses in Section1. Briefly, a nonzero profile has a lower angular sublevel mass C tau; regular zero charts and nonflat saddle charts have o(tau) mass, while the only remaining possible concentration points under N belong to Tflat. A finite sphere cover then contradicts the lower bound.

Thus under the stated hypotheses U!=0 and Tflat empty together force K identically zero. Equivalently, U!=0 and K not identically zero force Tflat nonempty. These are necessary alternatives, not exclusions of the K identically zero case.

## 6. Verification and dependencies

This proof uses A963/A970 for the exclusion of noninterior vortical zeros and A914/A834 only for the final nonexistence corollary. The boundary inclusion itself uses only(1), C1 regularity, that nodal exclusion, elementary linear algebra, the C1 inverse-function theorem, connectedness of a punctured two-dimensional disk, and harmonic uniqueness. Pressure normalization is needed in the upstream actual-tail results but no new pressure assumption or boundary integral is introduced here.

The theoretical question is whether the boundary of an open scalar-zero region can remain separate from the previously identified flat-velocity concentration obstruction. The pass criterion is full ambient DV=0 and membership in supp G at every such boundary point. Sections2-4 establish both without a regularity assumption on that boundary. No numerical computation or formal build was used.

A focused comparison has been requested through the files of the existing configured model agents. No focused response or provider runtime attestation is claimed here. All writes remain in this agent; no new model client or agent was used.


## 7. Full LIT196 comparison and zero extension

The complete six-section LIT196 source was read after the independent boundary proof above. Its boundary conclusion and global-k-zero alternative agree with Sections2-5. Its direct support proof is even shorter: on an irrotational ball (1) gives grad k=-aV, so div V=0 gives Delta k=0 distributionally. Harmonic regularity and local uniqueness give the same conclusion. Both proofs require only the local ball, not analytic unique continuation for Euler.

There is also a valid separation of the leading velocity field. Write Z for the open twisted cone over A0 and define V0=V on Z, V0=0 on D minus Z; put V1=V-V0. The actual tail is locally C^(1,alpha) for each fixed 0<alpha<1 by the previously confirmed tail theorem. At each boundary point x0, V(x0)=DV(x0)=0. Differentiability gives |V0(x0+h)|<=|V(x0+h)|=o(|h|), so DV0(x0)=0. Inside and outside Z the derivative is respectively DV and zero. Its continuity across the boundary follows from DV=0 there. Hence

    DV0=1_Z DV, curl V0=1_Z W, div V0=0

pointwise, including the boundary. These C1 formulas also hold distributionally with no interface measure.

To check the full local Holder claim, work in a convex ball compactly contained in D on which DV has Holder constant C_alpha. If x and y lie on opposite sides of Z, their segment has a boundary point b between them. For the point x inside Z,

    |DV0(x)-DV0(y)|=|DV(x)-DV(b)|
                      <=C_alpha |x-b|^alpha<=C_alpha |x-y|^alpha.

If both points lie inside use the original Holder bound; if both lie outside the derivative difference is zero. This proves V0 is locally C^(1,alpha), and the same holds for V1. Twisted homogeneity follows from invariance of Z. Each field is divergence free and helicity free, since V0.curl V0=1_Z V.W and the analogous equality holds for V1. The first field has X.V0=0 globally. Pointwise at most one separated field is nonzero, so

    V tensor V=V0 tensor V0+V1 tensor V1.

Consequently the corresponding distributional quadratic Poisson sources split. This algebra gives no individual pressure-transport identity: the pressure induced by either term remains nonlocal and can contribute harmonically on the other region. It does not prove V0 or V1 is an actual profile tail or an independent Euler profile. This qualification is explicit in LIT196 and is correct.

The LIT196 source is from the literature agent the second model, not a focused model response. The complete boundary and zero-extension arguments are confirmed without computation.
