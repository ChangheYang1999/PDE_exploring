# First integrals, trapping tori, and the specific singular reconstruction

## Exact statements

Let B,W be smooth real vector fields on R3. Assume B is complete, div B=d>0, every compact set has its backward B orbit in a compact set, and [B,W]=-kappa W with kappa>0. Assume W is complete and its time-one map is recurrent at almost every point with respect to Lebesgue measure.

**Rank statement.** For any two globally defined C2 first integrals F,G of W, dF wedge dG=0 at every point where W is nonzero.

**Trapping-level statement.** Suppose also that the W-zero set is a finite union of proper connected smooth lines. If a smooth first integral F tends to zero at infinity and vanishes on that zero set, every component T of a nonzero regular level is a compact torus. It bounds a compact connected smooth domain D disjoint from the W-zero set, and B points strictly outward on T.

**Index obstruction.** If B has exactly one zero p outside the W-zero set, its index is nonzero, and every nonempty compact smooth domain D disjoint from that zero set with B strictly outward on its boundary contains p, then every such F is zero.

**Specific reconstruction.** For the smooth fields U0,W of A121, with the return blocks and fillings specified in the team records and in the team records, let V be the A179 Biot-Savart inverse of W. For 2/5<c<1/2 and every finite omega,

    [lambda V-U0,W] is not identically zero

for every nonzero real scalar lambda. Consequently no lambda V from this particular reconstruction is an Euler profile. This conclusion does not extend to unspecified independent eigenfields or to an unconstructed regular plug.

## 1. Rank of global first integrals

There is no nonconstant periodic W orbit. The bracket identity contracts its period by exp(-kappa s) under backward B time s, while all the image loops remain in one compact ball. On that ball let L be a Lipschitz constant of W. If z(t) is a nonconstant periodic orbit with period T and mean zbar, then

    integral |z'|^2 = integral (W(z)-W(zbar)) dot z'
        <= L ||z-zbar||_2 ||z'||_2
        <= L T/(2pi) ||z'||_2^2.

The final inequality is the periodic Wirtinger inequality. Thus T>=2pi/L; if L=0 no nonconstant orbit exists. This contradicts the contracted periods.

Suppose the pair H=(F,G) has rank two at a W-nonzero point. Its rank-two locus there contains an open set O. Sard's theorem for a C2 map R3 to R2 makes the globally critical values a planar null set. In a countable cover by submersion charts, the preimage in O of that null set is a spatial null set, by Fubini and local coordinate regularity. Choose a recurrent point in O whose H value is globally regular.

Its fiber is a closed embedded one-dimensional manifold. The W orbit stays on one connected component. In the intrinsic coordinate of a line, or in an interval obtained by deleting zeros from a circle, the orbit is strictly monotone and cannot recur to its initial point. The embedded-submanifold chart rules out additional fiber sheets accumulating at that point. On a zero-free circle the orbit is periodic. Completeness handles the full parameter interval. All alternatives contradict recurrence or the preceding period obstruction. Hence the rank-two locus is empty.

## 2. The level surface and the index

A nonzero regular level of F is compact by decay. Its connected component T is an orientable compact surface without boundary. W is a nonvanishing tangent field there because F is zero on the W-zero set. Thus chi(T)=0 and T is a torus.

Set G=B dot grad F. The bracket gives W(G)=[W,B]F+B(WF)=kappa WF=0. The rank result implies dG is proportional to dF on T, so G is constant there. Jordan separation supplies a bounded connected component with closure D and boundary T. If the constant were zero, B would be tangent and the divergence theorem would give d|D|=0. Otherwise B has a strict constant normal sign. The same flux identity selects the outward sign.

Each proper connected line of the W-zero set is disjoint from T. If it met the bounded side, connectedness would place the whole line there, contradicting properness and unboundedness. Thus W is nowhere zero in D.

Under the index assumptions D contains the unique off-zero-set equilibrium p. It lies in the interior because B is transverse on the boundary. Poincare-Hopf gives i(p)=chi(D). The double of D is a closed orientable three-manifold, with Euler characteristic zero, so 2chi(D)=chi(T)=0. This contradicts the nonzero index. If F were nonzero, its range would contain an interval of nonzero values and Sard would supply the regular level used above. Therefore F is identically zero.

## 3. Verifying the extra assumptions for A121

Write X=-B0. All statements in this paragraph refer to the explicit blocks before their final smooth volume-coordinate change; diffeomorphisms preserve zeros, indices, orbit access, and strict boundary transversality.

There is one zero p in the original trapping handlebody H. In its central box,

    X=(Lx,-a y,-b z),   L,a,b>0,   W=partial_y.

Therefore the index of B0 at p is sign det diag(-L,a,b)=-1. Return tubes have X=partial_t and no zeros. Each smooth filling handle has one zero, on its W-zero axis. The exterior linear region has no zero. Hence p is the unique zero of B0 off the two proper W-zero lines.

Every point off those lines enters the interior of H in finite positive X time. In a filling handle, r'=epsilon r^3, so every r>0 reaches the outgoing side in time (r^(-2)-1)/(2epsilon). The exterior flows inward to the filled ball. The cap-center exceptions and their continuations are exactly the two zero lines. The rounding uses the same smooth vector field in enlarged flow collars; it introduces no new invariant block.

Every nonempty open subset of H has an orbit passage producing an open subset of the incoming section z=1. An open subset of a return tube advances to its endpoint. An open subset of the central box contains x!=0 points, which exit through an x face and return through a tube. The set x=0 has empty interior. The slightly enlarged tube footprints still land strictly inside the original top face by the positive margins in A066. Incoming corner collars can be chosen short enough to flow into these same box or tube pieces. Thus this access statement survives their rounding; it is a local passage argument, not an attractor classification.

On that top face the quotient return has two increasing branches,

    f(x)=sign(x) K(|x|^q-1/2),   0<|x|<1,
    1/2<q<1, Kq>1, K<2.

Its image lies in (-1,1) and f'(x)=Kq |x|^(q-1)>=Kq>1. Given a nonempty open interval I of x coordinates, some finite successive branch image contains zero. Otherwise all images would be intervals of length at least (Kq)^n |I| inside (-1,1), an impossibility. Until that first intersection every branch passage is defined.

Now take a compact smooth D on which B0 is outward and W never vanishes. Its X flow stays inside D. Its interior first enters H and then produces an open section set S contained in D. Apply the preceding interval argument to its x projection and select a point of S with the required x value. The corresponding finite return orbit stays in D and reaches x=0 on the section. Its ensuing box orbit converges to p. Compactness puts p in D, and boundary transversality puts it in the interior. This verifies the required index hypothesis without transitivity, mixing, or density of a selected orbit.

The bracket, completeness, recurrence and proper-zero-line assumptions are A121 and A179. The abstract index obstruction therefore applies to these particular fields.

## 4. Consequence for Biot-Savart reconstruction

Suppose [lambda V-U0,W]=0 for some nonzero real lambda. Both fields in the bracket are divergence-free, so the cross product is curl-free. On R3 there is a smooth F with

    grad F=(lambda V-U0) cross W.

The A179 exterior bounds give grad F=O(r^(1-2gamma)), gamma=1/c>2. Integrating rays, then comparing along large spheres, gives one common limit at infinity. Normalize it to zero; then F=O(r^(2-2gamma)). It is a W first integral. On each W-zero line its full gradient vanishes, so F is constant there; properness and decay make that constant zero. Sections 2-3 force F=0 everywhere.

Outside the compact support of U0, this gives V cross W=0. A179 gives W=Wh and V=Vh+O(r^-3), with Vh nonzero and rotating homogeneous of degree 1-gamma. Scaling the identity to a fixed annulus leaves an error O(R^(gamma-4)), which tends to zero. Thus Vh cross curl Vh=0. The real rotating homogeneous Beltrami exclusion A191 applies because eta=gamma-1 lies in (1,3/2). It forces Vh=0, a contradiction.

## Dependencies and scope

The proof uses A121, A179 and A191, plus Sard, the periodic Wirtinger inequality, the divergence theorem, Jordan separation, the classification of compact orientable surfaces, and Poincare-Hopf. It uses no numerical evidence. It strengthens LIT37's conditional reconstruction screen for the explicit A121 model; it does not resolve the full Euler conjecture. The reconstructed field remains a useful actual-curl decaying non-profile with the stated critical tail.

Audited: 2026-11-02T21:27:51Z
