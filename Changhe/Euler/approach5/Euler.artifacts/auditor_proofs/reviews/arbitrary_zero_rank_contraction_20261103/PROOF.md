# Rank and comparison remove the contraction

## 1. Exact scalar statement

Let G be a connected open subset of R^n, S,k in C1(G), and 0<eta<1/2. Assume S has a zero in G, and

    S grad k=eta k grad S on {S!=0}.

Suppose E is continuous and nonnegative, and each point has a neighborhood with finite constants C,M such that |k|<=C sqrt(E) and E<=M|S|. Then k=0 on G. No flatness, zero-set regularity or common boundary point for different components is assumed.

## 2. Proof component by component

On every connected component O of {S!=0}, H=|S| is positive and grad(k H^(-eta))=0. The open connected set O is polygonally connected, so k H^(-eta)=C_O for one real constant.

The relative boundary of O in G is nonempty. Otherwise O would be relatively open and closed in connected G and equal G, contradicting the zero of S. At any point z of that relative boundary, S(z)=0: if it were nonzero, a sufficiently small ball about z in G would be a connected nonzero-scalar set meeting O, and hence contained in O, contradicting the boundary property.

Choose x_j in O with x_j->z. The locally fixed comparison constants near z give

    |C_O|<=C sqrt(M)|S(x_j)|^(1/2-eta)->0.

Thus k=0 on each O. On {S=0}, E=0 and |k|<=C sqrt(E) give k=0 directly. This proves the assertion. No selection of a component whose closure contains a prescribed x0 was used.

The zero premise cannot be removed. Take S=1, k=1 and E=1 on a connected domain; all other hypotheses hold with C=M=1. The strict condition eta<1/2 is also necessary for this argument: on (-1,1), S=x^2, k=x and E=x^2 satisfy all comparisons and the rank equation at eta=1/2, but k is nonzero. These are scalar countertests only.

## 3. Homogeneous velocity application

Fix 0<c<1/2, omega real, X=(cI-omega J)x, a=1-2c, b=2-2c and eta=a/b. Suppose smooth V,S on a connected neighborhood G of x0!=0 satisfy

    div V=0, DV X=-((1-c)I+omega J)V,
    X.grad S=-bS, (curl V).grad S=0,
    bS grad k=ak grad S on {S!=0}, k=X.V.

If S has a zero and E=|V|^2<=M|S| locally, then |k|<=|X|sqrt(E) supplies the scalar lemma's other bound. Therefore k=0 throughout G. This uses only the rank and upper comparison, not Poisson, helicity as an extra assumption, a lower ratio bound, or flatness.

The rank premise may instead be stated on {curl V!=0,S!=0} if that set is dense in {S!=0}. Continuity then gives rank on the whole nonzero-scalar set. No density on an open scalar-zero set is necessary. Rank solely on vortical points, without this density, does not provide the asserted extension across open irrotational holes.

## 4. Critical-ratio consequence and scope

On an X-flowbox assume the equations above and the full-disk condition

    R0 in Wloc^(1,2), 0<r_-<=R0<=r_+<infinity,
    |V|^2=R0|S| almost everywhere on the transverse disk.

Pointwise comparison and homogeneity extend the bounds through the flowbox. Infinite value flatness of V at x0 implies S(x0)=0, so Section 3 gives k=0. The complete A1748-A1754 theorem in the team records applies and gives V=S=0 locally. This corollary allows arbitrary scalar zeros and signs, but retains full-disk ratio energy and full rank, or the explicitly stated density alternative.

All four submitted sections and all four independent sections were read. The scalar lemma, rank application and conditional corollary are CONFIRMED. The ratio derivative and density assumptions have not been deduced from arbitrary profile decay. All finite omega are allowed with local constants permitted to depend on omega. No computation or formal build was used. The full conjecture remains OPEN.
