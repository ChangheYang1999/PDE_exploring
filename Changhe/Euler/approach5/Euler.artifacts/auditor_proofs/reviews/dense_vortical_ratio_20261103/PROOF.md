# Dense vorticity, ratio transport and an isolated scalar zero

## 1. Statement and hypotheses

Fix 0<c<1/2 and any finite real omega. Put Jx=e3 cross x, A=cI-omega J, X=Ax, a=1-2c, b=2-2c, eta=a/b and q=1/eta. Thus b-a=1 and 0<eta<1/2. On an open set away from the origin let V,S be smooth and satisfy

    div V=0, W=curl V, k=X.V,
    X.grad V=-(1-c)V-omega JV, X.grad S=-bS,
    grad k=X cross W-aV, W.grad S=0,
    bS grad k=ak grad S wherever W!=0.

On every connected open region O with S!=0 and dense {W!=0}, set H=|S| and R=|V|²/H. Then k/H^eta is a single constant, grad H cross V=qHW, and curl(H^(-eta)V)=0. If O approaches a scalar zero and R stays bounded above, this constant is zero. No flatness or pressure hypothesis is required for these assertions.

In particular suppose O is a punctured X-flowbox with its central orbit removed, S vanishes on that orbit, has one strict sign on O, and vorticity is dense in O. If S is infinitely flat at its central point, R lies between positive constants and has finite transverse integral |D log R|², no such germ exists. This last assertion uses the previously checked critical continuation theorem A1449.

## 2. Density supplies one constant

Both sides of the rank identity are continuous, so the identity holds on O. Since S has one nonzero sign on each connected O,

    grad k=eta k grad H/H,
    grad(k H^(-eta))=0.

A connected open subset of Euclidean space is polygonally connected. Integrating the last derivative along such paths proves k=C H^eta with one finite real C. This argument also covers C=0 and does not divide by k. A single zero of k in O forces C=0. It does not join constants across an open irrotational hole, because rank there has not been supplied by continuity.

Let x_j in O approach a finite point x0 with S(x0)=0. On a small neighborhood |X|<=K. If R<=M along this sequence, then

    |C|<=K sqrt(M) H(x_j)^(1/2-eta)->0.

Therefore C=0 throughout O. On a punctured interval-times-disk flowbox O is connected, so k vanishes off the orbit and, by continuity, on it. This proves the submitted part(a), without any derivative bound, lower ratio bound, flatness, cone or boundary smoothness beyond the specified flowbox.

## 3. A weaker sequential criterion and necessary growth

The same proof needs only a sequence approaching the scalar zero for which

    |V(x_j)|/H(x_j)^eta ->0,

or equivalently R(x_j) H(x_j)^(1-2eta)->0. The ratio R may be unbounded. For example R=o(H^(-(1-2eta))) along that sequence suffices. Conversely if C!=0, then at every point of O within the neighborhood

    |V|>=|C| H^eta/K,
    R>=C² H^(-(1-2eta))/K².

This is a necessary blowup rate on one connected rank-valid region. It does not give uniform constants across infinitely many regions, nor rule out ratios that diverge at least this fast. The denominator K can be chosen positive because X has no zero near x0!=0.

## 4. Closed weighted form without a k-zero premise

Since grad k is parallel to grad H, cross the gradient identity with grad H. Using W.grad H=0 and X.grad H=-bH gives

    0=grad H cross(X cross W)-a grad H cross V
     =bHW-a grad H cross V.

Thus grad H cross V=qHW. The curl product rule now gives

    curl(H^(-eta)V)=H^(-eta)W
                    -eta H^(-eta-1)(grad H cross V)=0.

There is no need to assume C=0 here. This is a local closed-form conclusion, not a claim that all its periods vanish or that a potential exists globally on O.

## 5. Exact pressure-ratio flux

Assume additionally P=S+|V|²/2 is smooth and -Delta P=tr((DV)^2). Let sigma=sign S and E=|V|². Incompressibility gives div div(V tensor V)=tr((DV)^2), so div F=0 for F=(V.grad)V+grad P. The vector identity (V.grad)V=grad(E/2)-V cross W and Section4 give

    V cross W=eta R grad H-eta V(V.grad H)/H,
    F=grad E+sigma grad H-eta R grad H
                                  +eta V(V.grad H)/H
     =M_R grad H+H grad R,
    M_R=((1-eta)R+sigma)I+eta(V tensor V)/H.

The eigenvalue parallel to nonzero V is R+sigma, and each perpendicular eigenvalue is (1-eta)R+sigma. At V=0 the matrix expression itself still applies. Only div F=0 was assumed or proved, not the stronger equation F=0. No steady momentum equation has been inserted into the tail system.

## 6. Critical continuation in the isolated flat case

Under the second paragraph of Section1, Section2 first gives k=0. Positive bounded R and finite transverse logarithmic energy imply finite integral |DR|². The bounded extension is W1,2 across the puncture: multiply a compact test by a cutoff that changes over epsilon<r<2epsilon. The extra derivative term is at most C||R||infinity epsilon and vanishes. All other terms converge by local L1 integrability of DR. Conversely the bounded-derivative chain rule for log on a fixed positive compact interval recovers logarithmic energy from W1,2.

Since S is flat and |V|²<=M|S|, V vanishes in size to every order at x0. Smoothness then forces every derivative of V there to vanish. The twisted homogeneity propagates the isolated orbit geometry and the required flatness along its short central segment. Every hypothesis of A1449, in the team records, is now met: smooth V,S, the transport identities, k=0, one strict scalar sign off the isolated orbit, infinite flatness, and positive bounded transverse W1,2 ratio. Its complete first-order critical argument gives V=0 locally, contradicting the positive ratio where S!=0. Either scalar sign is allowed, and pressure was not needed.

## 7. Audit and unresolved scope

All five submitted sections and all seven independent sections have been read. Sections2-5 were derived directly; Section6 uses the explicitly named previously confirmed analytic proof. The sequence refinement in Section3 is stronger than the submitted upper-bound condition but remains conditional on one rank-valid connected region. Density, isolated scalar zero geometry and finite logarithmic energy are not consequences of bare velocity decay. Sign-changing scalars, extra zeros, irrotational holes and unbounded-energy ratios remain outside the exclusion. Local constants may depend on omega; no estimate uniform as |omega| tends to infinity is asserted. The unrestricted campaign remains open. No computation or formal build was used.
