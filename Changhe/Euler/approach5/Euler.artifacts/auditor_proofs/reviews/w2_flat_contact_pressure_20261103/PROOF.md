# Local pressure jets and zero-potential regions at flat W2 directions

Status: local theorem and conditional actual-tail application CONFIRMED A2515-A2519. The unused A1255 inference is REFUTED A2520; broader conclusions remain OPEN A2521. All flatness statements below are finite-jet statements unless explicitly qualified otherwise.

## 1. Exact local theorem

Let 0<c<1/2, omega in R, Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c and b=2(1-c). Let D be open in R3 minus {0}. Suppose V:D->R3 and P2:D->R are C2 and satisfy

    div V=0, DV X=-LV, -Delta P2=tr((DV)^2),
    W=curl V, k=X.V, S=P2-|V|^2/2,
    X.grad S=-bS,
    grad k cross grad S=0 on VV={W!=0}.                     (1)

All neighbourhoods and boundaries are relative to D. Put K=closure_D VV, O=int_D{W=0}=D minus K and Z=int_D{k=0}. Suppose w belongs to K and

    V(w)=DV(w)=W(w)=0, S(w)=0.                        (2)

No value of DW(w) is assumed. In particular DV(w)=0 alone would not imply DW(w)=0. Then:

(a) If grad S(w)!=0, k vanishes on a neighbourhood of w. Thus w belongs to Z and V=X cross W/a there.

(b) If grad S(w)=0 and there exist points z_n->w in K with W(z_n)=DW(z_n)=0 and V(z_n)!=0, then D2S(w)=D2P2(w)=0.

(c) If grad S(w)=0 and w is not in closure_D Z, then D2S(w)=D2P2(w)=0. Equivalently, if this second pressure jet is nonzero at a strict-gradient point satisfying (2), then w belongs to closure_D Z.

A point z in K with W(z)=DW(z)=0 is called a flat-vorticity contact here. This term records precisely these two finite jets. Every boundary point of O is such a contact because W is C1 and W=DW=0 on O. No boundary regularity is assumed.

The proof is local, needs only C2 and the exact equations (1), and has constants depending on a chosen compact neighbourhood. The application in Section7 retains the additional actual-tail, helicity and escaping-trace hypotheses. No existence of these configurations, infinite-order flatness, or global exclusion is claimed.

## 2. Elementary identities and the contact estimate

Differentiating k=X.V and using DV X=-LV gives

    grad k=-aV+X cross W, X.grad k=-ak,
    Delta k=-2 omega W_3-X.curl W,
    Delta S=-tr((DV)^2)-|DV|_F^2+V.curl W.                  (3)

The curl law is W(exp(tA)x)=exp(-t)exp(-omega tJ)W(x) whenever the finite local orbit lies in D. The velocity law is V(exp(tA)x)=exp(-tL)V(x). They follow from the transport identity, or by pulling back the homogeneous field and differentiating. They preserve K, O, nonzero V, the contact condition W=DW=0 and the central zero jets V=DV=W=0 on each local flowbox. This requires only finite local times.

Contract the rank relation in (1) with X and use both scalar transport laws. It gives

    bS grad k=ak grad S                                    (4)

on VV, hence on K by continuity. Where k!=0 in VV, it says grad(S/|k|^q)=0 with q=b/a>2. Thus S=D_C|k|^q on each connected component, with a possibly different constant D_C.

The exact contact estimate established in A1729 has no uniform-component premise. For completeness, at a contact z with v=V(z)!=0 put N=DV(z) and G=|N|_F^2. W=DW=0 gives N symmetric and trace free, grad k=-av, D2k=-aN, Delta k=0 and Delta S=-2G. Also NX=-Lv and L is invertible, so G>0. Since grad k(z)!=0, choose points x_j in VV with k(x_j)!=0 tending to z. At those points write alpha_j=qD_j|k(x_j)|^(q-2). Differentiating the component law yields

    grad S=alpha_j k grad k,
    Delta S=alpha_j[(q-1)|grad k|^2+k Delta k].               (5)

The bracket tends to (q-1)a^2|v|^2>0. Therefore alpha_j has the fixed limit -2G/[(q-1)a^2|v|^2], independent of the components. As (q-1)a=1, passing to the gradient identity gives

    grad S(z)=2G k(z)v/|v|^2,
    |grad S(z)|<=2|X(z)||DV(z)|_F^2.                        (6)

The inequality uses |k|<=|X||V|. This proof uses no derivative of S beyond order2 and remains valid when component constants are unbounded.

## 3. Zero-velocity contacts and harmonic extension across an arbitrary boundary

First let z be a contact with V(z)=0 and grad S(z)!=0. Then N=DV(z) is symmetric and trace free, grad k(z)=0, and D2k(z)=-aN. The vector field F=grad k cross grad S is C1, identically zero on the open set VV, so its derivative is zero there and, by continuity, on K. At z,

    0=DF(z)[h]=-a(Nh) cross grad S(z)

for every vector h. Thus the range of N lies in one line. A symmetric trace-free matrix of rank at most one is zero. Hence

    V(z)=DV(z)=k(z)=grad k(z)=D2k(z)=0.                      (7)

Now let U be a connected neighbourhood which contains a nonempty vortical open subset, and suppose k, grad k and D2k all vanish on boundary O intersect U. Define f=k on O intersect U and f=0 on U minus O. It is C2 across this arbitrary boundary. To justify the gluing explicitly, at a boundary point z Taylor's theorem gives k(z+h)=o(|h|^2), grad k(z+h)=o(|h|), and D2k(z+h)->0. The same bounds hold for f and its proposed derivatives, since they are either those of k or zero. Difference quotients first identify Df and then D2f at z; their continuity follows from the bounds. Away from the boundary the assertion is immediate.

On O, (3) gives grad k=-aV and Delta k=0. Off closure O, f is identically zero; at the boundary its second derivative is zero. Thus Delta f=0 throughout U. The Poisson formula implies that a C2 harmonic function is real analytic locally. Since f vanishes on a nonempty vortical open subset and U is connected, the identity theorem for harmonic functions gives f=0 on U. Consequently

    k=V=0 on O intersect U,
    bS grad k=ak grad S on all of U.                        (8)

For the last statement, (4) holds on K and both sides vanish on O. No integration by parts across a nonsmooth boundary or unproved boundary-flux condition is used.

## 4. A regular zero of S forces a zero-potential neighbourhood

Suppose (4) holds on a neighbourhood of z0, S(z0)=0 and grad S(z0)!=0. The submersion theorem gives a product coordinate box with first coordinate s=S and connected level discs. For s!=0, (4) makes every tangential derivative of k on a level disc vanish. Thus k=K_+(s) on the positive side and k=K_-(s) on the negative side. The scalar equation is

    b s K'(s)=aK(s),
    K(s)=C_+ s^(a/b) for s>0,
    K(s)=C_- (-s)^(a/b) for s<0.                            (9)

At s=0, (4) and grad S!=0 give k=0. Since 0<a/b<1, the derivative of a nonzero power in (9) is unbounded as s tends to zero. C1 regularity of k therefore forces C_+=C_-=0. Hence k vanishes on a whole neighbourhood of z0. Connected level discs are obtained by choosing the coordinate box; no global connectedness of level sets is assumed.

## 5. Proof of the nonzero-gradient and contact-sequence conclusions

For (a), choose a connected neighbourhood U of w with |grad S|>=2m0>0 and 2|X||DV|_F^2<m0 throughout U. This is possible by DV(w)=0 and continuity. At any boundary point of O in U, a nonzero value of V would contradict (6). Hence every such contact has V=0 and grad S!=0, so (7) gives the required vanishing two-jet of k there. Because w belongs to K, every neighbourhood of w contains a vortical point and hence a nonempty vortical open subset. The harmonic extension in Section3 gives (4) throughout U, and Section4 at w gives k=0 near w. Formula (3) then gives V=X cross W/a. This proves (a), including when O is empty locally.

For (b), use the local flowbox for the nonzero field X at w to move each contact to the affine transverse disc w+E, E=X(w)^perp. This takes times tending to zero and preserves the contact and nonzero-velocity conditions. The new contacts are w+h_n, r_n=|h_n|>0, and after a subsequence h_n/r_n tends to a unit vector e in E. A contact on the central orbit could not have nonzero V by (2) and transport.

Let H=D2S(w). Differentiating X.grad S=-bS gives

    H X(w)=-(bI+A^T)grad S(w)=0.

At w, the last identity in (3) and (2) give tr H=0. Thus H is a symmetric trace-free form on the two-dimensional plane E. Since DV is C1 and DV(w)=0, |DV(w+h)|<=C|h| on a small disc. Estimate (6) gives |grad S(w+h_n)|<=Cr_n^2. Taylor's theorem gives grad S(w+h_n)=Hh_n+o(r_n), so He=0. A symmetric trace-free 2 by 2 matrix with a nonzero kernel vector is zero. Hence H=0 on E and on all of R3. Differentiating |V|^2/2 twice at w, where V=DV=0, gives D2P2(w)=D2S(w)=0. This proves (b).

## 6. Proof of the second-jet alternative without a contact-sequence premise

Assume grad S(w)=0 and H=D2S(w)!=0. As in Section5, H is a trace-free symmetric form on E and kills X(w). Its two eigenvalues on E are therefore +-sigma for sigma>0. On a sufficiently small transverse disc,

    |grad S(w+h)|>=(sigma/2)|h|,
    2|X(w+h)||DV(w+h)|_F^2<=C|h|^2.                        (10)

Consequently any flat-vorticity contact off the central orbit has V=0, by (6), and has nonzero grad S. It obeys (7). These estimates extend to a finite product flowbox N with compact time interval: scalar and field transport preserve their zero conditions and multiply the relevant norms by bounded factors. Shrink the transverse radius so (10) excludes all nonzero-velocity contacts throughout that box.

On the central orbit V=DV=W=0 by (2) and transport. At its points on boundary O one additionally has DW=0 from the boundary property, since W is C1 and zero on O. The differentiated first identity in (3) therefore gives k=grad k=D2k=0 at precisely these boundary points, even though grad S is zero there. Nothing about DW elsewhere on the central orbit is needed. Thus all points of boundary O intersect N have the zero two-jet needed in Section3. Choose N connected. Since w is supported, N contains a nonempty vortical open subset. We obtain (4) on all of N.

On the transverse disc Taylor's theorem says

    S(w+h)=(1/2)h^T Hh+o(|h|^2).

For every sufficiently small radius r, the values in the positive and negative eigendirections have opposite signs. By continuity around the circle there is a point h_r with |h_r|=r and S(w+h_r)=0. Inequality (10) makes this a regular zero. Section4 supplies a neighbourhood of each w+h_r on which k=0. Thus w+h_r belongs to Z and w belongs to closure_D Z. Taking the contrapositive proves (c).

This argument proves proximity to open zero-potential regions. It does not prove that w itself belongs to Z in the zero-gradient case, nor exclude the alternative H=0.

## 7. Exact application to B67 and two source qualifications

For the actual-tail application assume 2/5<c<1/2 and any real omega. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, Omega=curl U, B=Ax+U,
    (1-c)U+(B.grad)U+omega JU+grad P=0,
    U.Omega=0 everywhere, U(x)->0 uniformly at infinity.

Assume finite C in the natural bounds |U(x)|<=C(1+|x|)^(-p), |DU(x)|<=C(1+|x|)^(-p-1), p=(1-c)/c. Take the established C1 local tail limit V(x)=lim_(t->infinity) exp(tL)U(exp(tA)x), x!=0, and the locally uniform pressure limit P2 obtained after subtracting the pressure constant at infinity and multiplying by exp(bt). The established pressure result supplies P2 in C2 locally. Assume additionally V in C2 near the nonzero scattering direction w.

A lower-window W2 witness is a nonconstant periodic B-orbit Gamma in closure{Omega!=0}, with Omega=DOmega=0, U!=0, U.B=0 and Hprofile=P+|U|^2/2+(Ax).U constant there. Its covector rate rho satisfies rho<=-2a and U(Phi_t x)^flat composed with DPhi_t(x)=exp(rho t)U(x)^flat. An escaping trace is a distinct B-orbit z(t) in closure{Omega!=0} intersect W^u(Gamma), with |z(t)| tending to infinity forward, and w=lim_(t->infinity)exp(-tA)z(t)!=0.

The established tail and scattering results A1129-A1130, A1729-A1737, A1798-A1799 and B60 supply (1), w in K, V(w)=W(w)=S(w)=0 and the rate dichotomy: rho=-b exactly when grad S(w)!=0, and rho<-b when grad S(w)=0. B66, confirmed A2457-A2460, supplies DV(w)=0 under this extra C2 tail regularity. Therefore all premises (2) hold and the local conclusions (a)-(c) apply. This proves the intended B67 statements at exactly these conditional hypotheses. It supersedes the equality-rate outside-closure-Z residual of W2.15(c), but not the zero-gradient, zero-Hessian case.

Two qualifications should remain explicit in the source. First, DW(w)=0 is not a consequence of DV(w)=0 and is not needed in this theorem. The proposed replacement citation A1255 is inapplicable here: its exact statement and proof assume the nonflat condition DV(w)!=0. Its derivative conclusion therefore supplies no flat-direction jet assertion. At central-orbit boundary points the needed DW=0 instead follows from the boundary property. Second, Lemma IP gives a nonzero-velocity boundary contact somewhere on a nontrivial irrotational component. It does not by itself put contacts arbitrarily close to a selected w. The contact-sequence premise in (b) must be retained; merely w in closure O is not the checked substitute. The parenthetical reference to IP should be read only when that sequence has independently been supplied, or removed. Parts (a) and (c) need no such premise.

The complete B67 setting, three lemmas and three conclusion proofs were read. The independent argument supplies the boundary gluing, connected level box, finite-time projection, all-dimensional Hessian reduction and actual-tail premises. No C3, quartic pressure expansion or general flat-case derivative-sign assertion from the adjacent unclaimed consultation is used. There is no assertion that the original arbitrary-helicity smooth decaying Euler conjecture has been settled, that natural bounds imply C2 tail regularity, or that a finite-jet T0 point is infinitely flat. The complete eleven-item coordinator comparison in the team records was read and agrees, including its rejection of the unused A1255 citation. Existing configured model collaboration is through files; actual provider execution is independently unattested.

Revision at 2026-11-03T23:17:25.643403+00:00: the exact A1255 claim and full proof Section3 were reread. The unused DW(w)=0 premise and unsupported actual-tail transfer were removed, and Section6 now uses only the central boundary jets. All three conclusions and their proofs otherwise remain unchanged.
