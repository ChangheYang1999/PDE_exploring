# Irrotational component boundaries and local nodal germs

Status: CONFIRMED in A625-A627 at the exact scopes below, after complete independent reconstruction and postread.

## 1. Exact setting and statement

Put D=R^3\{0}, Jx=e_3 cross x, A=cI-omega J, a=1-2c, p=(1-c)/c, t=omega/c, and eta=(p-1)/(2p). For the component theorem assume 1/3<c<1/2, hence 1<p<2, and any real omega. Let V be C1 on D, divergence free, and satisfy

    V(exp(sA)x)=exp(-s((1-c)I+omega J))V(x).

Let k=(Ax).V, W=curl V, and let S be a C1 twisted homogeneous scalar of degree -2p. Assume grad k cross grad S=0 wherever W!=0. No helicity or pressure assumption is needed for the component theorem.

If grad k cross grad S!=0 at x0, the connected component Sigma of int{W=0} containing x0 is proper and has a boundary point at which k!=0. More generally, if k vanishes on the boundary of such a component, then V vanishes throughout it. A globally irrotational V is zero.

For the supplementary harmonic and germ results assume the target interval 2/5<c<1/2. A local tail pair additionally satisfies V.W=0, -Delta P2=tr((DV)^2), S=P2-|V|^2/2, W.grad S=0, and the same rank condition on W!=0. The pressure equation is distributional initially and classical on the analytic regions below. P2 is C1 and twisted homogeneous of degree -2p. Local germs need not be global tails or solve the full Euler profile equation.

## 2. Harmonic reduction and maximum principle

Differentiating the velocity homogeneity and using the vector identity for grad((Ax).V) gives

    grad k=-a V+(Ax) cross W.

Thus on an irrotational component Sigma, grad k=-aV and Delta k=0 distributionally. The harmonic representative equals the given C1 k, so k is smooth there. Twisted homogeneity preserves int{W=0}; its continuous one-parameter action preserves every connected component.

Use rho=log r, z=cos(theta), chi=phi+t rho. The quotient of Sigma is an open connected domain O in S2. With lambda=1-p in (-1,0), write k=r^lambda kappa(z,chi). For any scalar exponent q, direct radial differentiation gives

    Delta(r^q f)=r^(q-2) M_q f,
    M_q=Delta_S2+t^2 Z^2+t(2q+1)Z+q(q+1), Z=partial_chi.

This is an intrinsic smooth elliptic operator on S2; Z is the smooth rotation field and creates no pole singularity. Its principal quadratic form is the spherical metric inverse plus t^2 Z tensor Z. In particular M_lambda kappa=0 with strictly negative zeroth-order coefficient lambda(lambda+1).

If k=0 on the relative boundary of Sigma in D, kappa=0 on the boundary of O. It is continuous on the compact closure of O because k is globally continuous on the unit sphere. If kappa has a positive value, its positive maximum is attained in O. At that point the principal part is nonpositive, the first-order part is zero, and the zeroth-order part is negative, contradicting the equation. Apply the same argument to -kappa. It also works if O=S2. Thus kappa=0 and V=-grad k/a=0. This argument makes no regularity assumption on the boundary of O.

The complement of int{W=0} is closure{W!=0}. A boundary point of a component of int{W=0} cannot belong to int{W=0}: a sufficiently small connected ball there would join that component. Hence the component boundary is contained in closure{W!=0}. By continuity the rank identity holds on that closure. Every rank failure therefore lies in int{W=0}. If its component had k=0 on its boundary, the preceding argument would give grad k=0 in it, a contradiction. This proves the theorem.

For actual natural-decay helicity-free profiles in the scalar A2 class, A604 supplies a rank failure whenever the profile is nonzero. The present theorem then supplies a proper irrotational component and a boundary point with k!=0. It does not assert a regular interface, a sign of k on the boundary, or density of vorticity.

## 3. Harmonic pair and the boundary matching obstruction

On Sigma let Pi=P2+|V|^2/2. Since V is a harmonic gradient,

    Delta Pi=0,
    S=Pi-|grad k|^2/a^2,
    Delta S=-2|D2 k|^2/a^2.

Indeed tr((DV)^2)=|DV|^2 on this set and Delta(|V|^2/2)=|DV|^2. Smoothness of the harmonic Pi follows from the distributional identity. Its angular equation is M_(-2p)pi=0.

On closure{W!=0}, contract grad k cross grad S=0 with Ax and use (Ax).grad k=-ak and (Ax).grad S=-2(1-c)S. This gives

    S grad k=eta k grad S.

It holds on the component boundary. On a connected regular C1 interface piece Gamma on which k!=0, the full ambient gradient of S|k|^(-1/eta) is zero. A connected C1 manifold is path connected, so there is a real constant D_Gamma, possibly zero, such that, with b=1/eta,

    S=D_Gamma |k|^b,
    grad S=D_Gamma b |k|^(b-2) k grad k.

Consequently the traces from the harmonic side satisfy

    Pi=|grad k|^2/a^2+D_Gamma |k|^b,
    partial_n Pi=2 D2k(grad k,n)/a^2
                 +D_Gamma b |k|^(b-2) k partial_n k.

The required D2k trace exists at this C1 velocity regularity: on the interior it equals -a DV, whose continuous boundary trace exists. A normal is defined on a regular C1 interface. No second derivative of the interface is being presumed.

These are Cauchy data for Pi, but F=Pi-|grad k|^2/a^2-D_Gamma |k|^b is not harmonic:

    Delta F=-2|D2k|^2/a^2
            -D_Gamma b(b-1)|k|^(b-2)|grad k|^2.

Zero Dirichlet and normal traces of F do not give harmonic unique continuation. At an analytic angular interface, the elliptic analytic Cauchy theorem solves for harmonic Pi with these analytic data after choosing a nonvanishing harmonic k. This constructs the harmonic side only. In a smooth-interface gluing problem one must still match the velocity first jet and the pressure first jet to a vortical solution, and impose global pole regularity. The interior Dirichlet problem for M_(-2p) can be resonant even though the full-sphere operator is invertible; its Cauchy-data space is the appropriate formulation without an extra nonresonance hypothesis.

## 4. Analytic k=0 germs with arbitrarily high scalar vanishing

Fix target p, any t, and any integer N>=1. There is a real analytic local twisted tail on an equatorial band with k=0, W!=0 everywhere, and S<=0 vanishing to exactly order 2N on a regular analytic twisted hypersurface. This is a local obstruction to automatic inverse integrability, not a global counterexample.

Let w=1-z^2, s=sqrt(w), and use the ansatz

    V=r^(-p)(tF e_r+(H/s)e_theta+(F/s)e_phi),
    D(z)=t^2+1/w,
    e=(D F^2+H^2/w)/2,
    P2=r^(-2p)(h+e), S=r^(-2p)h.

Then k=0. Direct spherical differentiation gives

    r^(p+1) div V=(2-p)tF+D F_chi-H_z,
    r^(p+1) W_r=-F_z-H_chi/w,
    r^(p+1) W_theta=(p-1)F/s,
    r^(p+1) W_phi=(-(p-1)H+t H_chi+t w F_z)/s.

Their dot product with V is identically zero. Near F=1, the two remaining first-order equations are

    E=H_z-(2-p)tF-D F_chi=0,
    B=h_z+H h_chi/(wF)-b h(F_z+H_chi/w)/F=0,
    b=2p/(p-1).

The second equation is precisely W.grad S=0; its numerator before division is 2p h(F_z+H_chi/w)-(p-1)(F h_z+H h_chi/w). The rank condition is automatic because k=0.

Let qV=tr((DV)^2) at r=1. It is analytic in z,F,H and their first derivatives. The pressure equation is

    P=M_(-2p)(h+e)+qV=0.

Solve the second-order system E_z=B_z=P=0. Its coefficient matrix for (F_zz,H_zz,h_zz) is

    [ 0          1  0 ]
    [ -b h/F     0  1 ]
    [ w D F      H  w ].

Its determinant is w(D F+b h/F). All other terms have total differential order at most two and fewer than two z derivatives. Thus invertibility gives the ordinary second-order analytic Cauchy normal form, not an invalid first-order problem with second tangential derivatives.

Choose 0<epsilon<(1+t^2)/(2^(N+1)b). On z=0 prescribe the periodic analytic data

    F=1, H=0, h=-epsilon(1-cos chi)^N,
    F_z=0, H_z=(2-p)t, h_z=0.

Both E and B vanish initially. The determinant is 1+t^2-b epsilon(1-cos chi)^N>(1+t^2)/2. The analytic Cauchy theorem gives a convergent solution locally along the initial circle. Compactness, uniqueness on overlaps and periodicity give a common band. Shrinking it keeps F>1/2 and the determinant nonzero. Since E_z=B_z=0, the two constraints propagate exactly. All five local tail equations now hold, and W_theta is nonzero everywhere.

Let X_z=H(z,X)/(wF(z,X)), X(0,xi)=xi. It is an analytic circle diffeomorphism on a smaller band. The transport equation gives

    h(z,X(z,xi))=-epsilon(1-cos xi)^N
      exp integral_0^z [b(F_z+H_chi/w)/F](u,X(u,xi)) du.

The exponential is positive and bounded above and below. Thus |h| is comparable to |xi|^(2N) near xi=0 and h<=0 throughout. The inverse characteristic coordinate xi(z,phi+t log r) has nonzero differential. Its zero set is a regular analytic hypersurface, and locally |S| is comparable to distance^(2N). The reciprocal of |S|^eta fails local integrability if 2N eta>=1, including equality. In particular N>=ceil(p/(p-1)) suffices. A local A2 weight must have an integrable reciprocal, so this weight is not A2.

No continuation to the poles, origin, or global canonical pressure has been supplied. This germ solves the local tail equations only. Its scalar sign is compatible with the negative canonical mean identity, so that sign alone does not rule it out.

## 5. Original-profile patch transfer and dependencies

With the natural derivative bound |DU|=O(r^(-p-1)), normalized carrier maps exp(-sA)Phi_s converge C1 on escaping sets, with determinant one. A fixed small original irrotational ball sufficiently far out therefore has images containing a fixed open ball in normalized coordinates for all large s. Curl-free rescaled fields then give a curl-free tail on that ball. This is already included in the stronger exact scattering correspondence A603. Merely noting fixed normalized volume would not control an inradius. The weaker starting derivative bound O(sqrt r) yields the natural bound for the actual profile through A601; omitting that bootstrap would leave a gap in this transfer argument.

Sources independently read in full: coordinator in the team records and in the team records, with its research/irrotational_patches, research/zero_set and research/profile_transport proofs. The configured model coordinator supplied its own comparison; the inner requested model response was unavailable, and no successful inner consultation is presumed. The analytic Cauchy step is the same precise second-order theorem used in the independently audited A599. No new numerical computation was needed.

Scope: the component theorem is global and arbitrary-omega; the analytic construction is local; unrestricted Euler nonexistence remains open.
