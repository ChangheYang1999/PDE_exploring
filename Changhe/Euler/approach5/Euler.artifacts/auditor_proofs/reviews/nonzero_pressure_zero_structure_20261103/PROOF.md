# Smooth velocity zeros in an open nonzero-pressure region

Status: CONFIRMED A2134-A2140 at the stated scope; common-flat and global extensions OPEN A2141. The proof below includes a direct Euclidean Carleman argument and does not assume analyticity.

## 1. Exact local theorem and its hypotheses

Let 0<c<1/2, omega in R, Jx=e3 cross x, A=cI-omega J, X(x)=Ax, a=1-2c, b=2(1-c), eta=a/b and L=(1-c)I+omega J. Let G be a connected open subset of R3 not containing zero. Suppose V and S are smooth on G and satisfy

    S!=0, div V=0, X.V=0,
    X.grad S=-bS,
    X cross W=aV, W.grad S=0, W=curl V.          (1.1)

Then either V=0 throughout G, or W has relative support G and every zero p of V has a finite exact order N>=1. At each such p, W has that same exact order. On a sufficiently small neighborhood their common zero set is one X-orbit arc. In orthonormal coordinates on a transverse plane at p, the transverse velocity has leading term F(p)grad P, where F=|S|^eta>0 and P is a nonzero homogeneous harmonic polynomial of degree N+1 in two variables. The transverse index, using matching orientations for domain and range, is -N.

Here exact order N means that all derivatives of orders below N vanish and some derivative of order N does not. The theorem does not assign a three-dimensional isolated-point index to an orbit arc. G need not be globally invariant under the X-flow. Only local flowboxes will be used. No Poisson equation, next-pressure scalar, original profile or decay premise is part of (1.1).

## 2. Reduction to a scalar equation with smooth bounded drift

The triple-product identity and (1.1) give

    a grad S cross V=grad S cross(X cross W)=bS W.

Thus the smooth form |S|^(-eta)V.dx is closed. On a small ball it has a smooth potential phi satisfying

    V=F grad phi, F=|S|^eta>0,
    Delta phi+beta.grad phi=0, beta=grad log F,
    X.grad phi=0.                              (2.1)

The drift beta is bounded on a smaller closed ball because S never vanishes there. The curl is

    W=eta F S^(-1) grad S cross grad phi.       (2.2)

Since grad S.X=-bS!=0, the map grad S cross is injective on X-perp. Every grad phi lies in that plane. Therefore V and W have the same zero set locally, and hence on G. This also shows that the leading nonzero gradient tensor at a zero cannot be annihilated by (2.2).

The usual vector identity supplies an additional useful check without imposing another hypothesis. As k=X.V=0,

    0=grad k=A^T V+DV^T X,
    X cross W=(DV^T-DV)X=aV,

and therefore X.grad V=-(A^T+aI)V=-LV. This is the expected vector homogeneity. It can propagate zero orders along any finite local orbit segment, but it is not needed to justify the bounded-drift equation.

## 3. Two Carleman estimates from a factored multiplier

For this section center coordinates at an arbitrary base point, write r=|x| and dmu=r^(-3)dx, and let f be smooth with compact support in a punctured ball. For every tau=j+1/2, j=0,1,2,..., define

    K_tau(f)=||r^(-tau)r^2 Delta f||_(L2(dmu)).

We prove

    tau||r^(-tau)f||_2<=2K_tau(f),
    ||r^(-tau)r grad f||_2<=2K_tau(f).           (3.1)

Put t=log r and v=e^(-tau t)f. Then dmu=dt dOmega and r^2 Delta=partial_t^2+partial_t+Delta_(S2). Expand in spherical harmonics of degree ell and Fourier transform in t with frequency xi. The conjugated multiplier is

    (i xi+tau-ell)(i xi+tau+ell+1).

This factorization is an independent check of the expanded source multiplier. Its squared magnitude is

    [xi^2+(tau-ell)^2][xi^2+(tau+ell+1)^2].     (3.2)

The half-integer gap gives |tau-ell|>=1/2. Therefore (3.2) is at least

    (1/4)[xi^2+(tau+ell+1)^2]
        >=(1/4)[xi^2+tau^2+ell(ell+1)].         (3.3)

For the weighted Euclidean gradient, the radial Fourier multiplier is i xi+tau and the squared angular contribution is ell(ell+1). Plancherel applied to (3.3) gives the second estimate in (3.1), and also the first. This controls the full gradient, including the radial term; no loss depending on tau is hidden in its constant. Compact annular support justifies the transforms and eliminates boundary terms. The proof applies to complex components as well, although only a real scalar is needed.

## 4. Flatness implies local vanishing, with the limits in order

Suppose phi is smooth near the center, is flat there, and solves Delta phi+beta.grad phi=0 with |beta|<=M on a ball. Choose a smaller radius R with 2MR<=1/2. If M=0, only containment is required. Let chi be smooth, equal to one on r<=R/2 and zero on r>=R. Let zeta_epsilon vanish on r<=epsilon and equal one on r>=2epsilon, with the usual first and second derivative bounds C/epsilon and C/epsilon^2. Put h=chi zeta_epsilon and f=h phi. Direct differentiation, including the sign of the drift term, gives

    Delta f=-beta.grad f+E_epsilon,
    E_epsilon=2grad h.grad phi+(Delta h+beta.grad h)phi.

Thus

    K_tau(f)<=MR||r^(-tau)r grad f||_2
                       +||r^(-tau)r^2E_epsilon||_2
             <=2MR K_tau(f)+||r^(-tau)r^2E_epsilon||_2.

Absorption and (3.1) give

    tau||r^(-tau)f||_2<=4||r^(-tau)r^2E_epsilon||_2.       (4.1)

Fix tau first. Smooth flatness gives |phi|+r|grad phi|<=C_K r^K for every integer K. On the inner annulus, r^2E_epsilon=O(epsilon^K), and its dmu measure is bounded independently of epsilon. Hence its weighted norm is O(epsilon^(K-tau)). Choose K>tau and let epsilon tend to zero. The same bound proves convergence of the left side. Only the fixed outer error

    E_out=2grad chi.grad phi+(Delta chi+beta.grad chi)phi

remains; it is supported in R/2<=r<=R. With C_R=||r^2E_out||_2 finite and independent of tau, (4.1) becomes

    tau||r^(-tau)chi phi||_2<=4(R/2)^(-tau)C_R.

For any fixed 0<rho<R/2 this yields

    ||phi||_(L2(B_rho,dmu))<=(4C_R/tau)(2rho/R)^tau.

Let tau tend to infinity through positive half-integers. The right side tends to zero, so phi=0 on B_rho, first almost everywhere and then pointwise by continuity. Flatness makes all the weighted integrals finite. The order epsilon-to-zero before tau-to-infinity is essential and has been respected.

If V is flat at p in Section2, normalize phi(p)=0. Since grad phi=F^(-1)V and F is smooth positive, all derivatives of phi vanish at p. The preceding argument gives V=0 on a neighborhood of p. It uses an ordinary smooth bounded drift on a small ball, not a general system-level elliptic assertion.

## 5. Finite orders, zero arcs and the transverse index

Let Z_open consist of points where V vanishes on a neighborhood. It is relatively open in G. If p_j in Z_open tend to p in G, all derivatives of V vanish at p_j and hence at p by continuity. Section4 gives local vanishing at p. Thus Z_open is also relatively closed. Connectedness implies Z_open=G or Z_open is empty.

In the nonzero case it is empty. Since W=0 exactly where V=0, W has no open zero set and supp_G W=G. A zero p of V cannot be flat, so it has a finite exact order N>=1.

Choose an orthonormal basis of X(p)-perp and coordinates u,v on that affine plane through p. Extend u,v constantly along local X-orbits. At p their Euclidean gradients are the chosen orthonormal vectors. The equation X.phi=0 gives phi=phit(u,v). Subtract phi(p). Smooth multiplication by F and the invertible local coordinate change show that the first nonzero term of phit has degree n=N+1. In (2.1), the degree N-1 equation is just

    partial_uu P+partial_vv P=0.

The varying coefficients and the drift contribute only higher orders. Therefore P=Re(C(u+iv)^n), C!=0. Its gradient has norm n|C|rho^N, where rho^2=u^2+v^2. Taylor's theorem gives grad phit=grad P+O(rho^(N+1)). After shrinking the transverse disk, the gradient is nonzero off its center. Since u,v are independent smooth coordinates, grad phi, V and W vanish precisely on the central X-orbit arc in the resulting flowbox.

At p the leading tensor of grad phi takes values in X(p)-perp. The injectivity in Section2 proves that multiplication by the smooth map in (2.2) preserves its exact order N. Hence W has that order as claimed. Either applying the same argument at every arc point or using the derived vector homogeneity verifies the orbitwise statement.

The coordinate components (V.grad u,V.grad v) have leading term F(p)grad P. On a sufficiently small circle, their higher-order remainder gives a homotopy through nonzero fields to that leading term. In complex notation

    P_u+i P_v=n conjugate(C(u+iv)^(n-1)).

Its winding number is -(n-1)=-N. Using the same orientation in the transverse domain and its velocity components gives the stated index. Positivity of F does not change it.

## 6. Actual-tail application and exact limits

Suppose in addition that the pointwise law DV=0 holds at supported common zeros in the open region X.V=0. In the nonzero branch all zeros are supported, so N>=2. If S>0 and a next scalar satisfies the exact LIT286 hypotheses, then A2107-A2110 apply at every such zero, since infinite order has now been excluded. The necessary tensor condition is

    [3D2S+(eta/S)dS tensor dS] restricted to X(p)-perp
        is a scalar multiple of the Euclidean metric.

For the stated original-profile application retain every premise: a global helicity-free profile U in C2(R3), P_original in C1(R3), its complete rotating momentum and divergence equations, 2/5<c<1/2, and both natural bounds

    |U(y)|<=C(1+|y|)^(-p0),
    |DU(y)|<=C(1+|y|)^(-p0-1), p0=(1-c)/c.

Its actual leading pair V,P2 must be smooth near the point, with k=X.V identically zero on a neighborhood and S=P2-|V|^2/2>0 there. The confirmed pointwise law gives N>=2. The next scalar is supplied by A647-A648 away from c=3/7 and by A653-A654's averaged scalar at that resonance. The latter does not require an unaveraged resonant limit. A2112 already checks these exact transfers; omega=0 is also subject to the ordinary-profile Liouville theorem. No smoothness of the leading pair is deduced merely from the C2 original profile.

This theorem is consistent with every finite-order local construction in LIT285 and LIT287, including the isotropic-pressure examples. It does not exclude those arcs or construct their next scalar. It does not cover S=0, where grad log|S| may be unbounded, or a boundary point of int{k=0} without a full open k=0 neighborhood. Those common-flat and boundary cases, and unrestricted global nonexistence, remain open.

All six source sections and all six independent sections are read before the final verdict. The only analytic inputs are local integration of a smooth closed form, Fourier-Plancherel and spherical harmonics, elementary cutoffs and Taylor expansion. The Carleman and continuation estimates are proved here. No numerical computation or formal build is used.

Precision note 2026-11-03T19:28:56.587754+00:00, A2173-A2174: the actual-tail application in Section6 retains the source hypothesis p in supp curl V. Its nonzero branch is essential. The second application paragraph must not be read as dropping that supported-zero premise. The explicit local V=0, positive harmonic homogeneous S countertest and exact corrected implication are in the team records, Section8. The local theorem and supported application A2134-A2140 are unchanged.
