# Original vorticity nonflatness excludes smooth infinite-order tail zeros

Status: independent conditional theorem. It does not assert that smooth original vorticity has finite vanishing order.

## 1. Exact global setting

Fix 2/5<c<1/2 and finite real omega. Put Jx=(-x2,x1,0), A=cI-omega J, p=(1-c)/c, a=1-2c. Let U in C2(R3;R3), P in C1(R3) solve

    div U=0, (1-c)U+DU(Ay+U)+omega JU+grad P=0,
    U.Omega=0, Omega=curl U,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1), C<infinity.

Use the confirmed actual tails V,W=curl V,P2, S=P2-|V|^2/2, and the C1 scattering diffeomorphism Xi from the escaping original region onto R3 minus0. The scattering identity is

    W(Xi(y))=DXi(y) Omega(y).                       (1.1)

Set T0={x in S2: V(x)=DV(x)=P2(x)=0} intersect supp W. Here support is the closure of the set where W is nonzero. By A1057, U!=0 implies T0 is nonempty. By A1151, if V is smooth near every point of T0 and has a finite first nonzero Taylor order there, then U=0.

## 2. Local transfer of flatness requires only a C1 map

Let x0=Xi(y0) be any point with V smooth near x0 and flat to all orders at x0. Then W=curl V is also smooth and flat to all orders there. For each integer n>=1, Taylor's theorem on a small fixed closed ball gives

    |W(x)|<=C_n |x-x0|^n.

Shrink the original neighborhood so its image lies in that ball. The C1 map Xi is locally Lipschitz, and the continuous matrix (DXi)^(-1) is bounded on a smaller closed neighborhood. Thus (1.1) gives, for every n,

    |Omega(y)|<=D_n |y-y0|^n.                      (2.1)

The constants may depend on n. No derivative of Xi beyond its first is used. No differentiability of Omega beyond its already given C1 regularity is needed for this estimate.

## 3. A precise sufficient original nonflatness condition

Say that Omega is polynomially nonflat at y0 if some finite integer d>=0, some epsilon>0, and a sequence y_j tending to y0 with y_j!=y0 satisfy

    |Omega(y_j)|>=epsilon |y_j-y0|^d.             (3.1)

This is an explicit local assumption, not a consequence of C1 regularity. It contradicts (2.1) with n=d+1. Therefore, if V is smooth at x0 and (3.1) holds at its preimage, V cannot be flat to all orders there.

If Omega is C^d and has a nonzero derivative of some finite order at y0, its first nonzero homogeneous Taylor polynomial has a nonzero value on some direction. The Taylor remainder along that ray supplies (3.1). For d=0 the same argument uses a nonzero value. At a point of T0, Omega(y0)=0, so any such first order is positive.

Consequently, under the exact global setting in Section1, if V is smooth near every T0 point and Omega is polynomially nonflat at every corresponding preimage, then U=0. Indeed each T0 point has finite first velocity order, necessarily at least2, and A1151 applies. This theorem does not need the nodal condition k=0 implies W=0.

## 4. Analytic original vorticity is sufficient locally

Suppose Omega is real analytic on a neighborhood of y0=Xi^(-1)(x0), where x0 belongs to supp W. If Omega had all Taylor coefficients zero at y0, its convergent power series would vanish on a neighborhood. Equation(1.1) would then make W vanish on the image neighborhood, contradicting x0 in supp W. Hence Omega has a finite nonzero Taylor order and is polynomially nonflat.

It follows that the global setting in Section1, smooth V near every T0 point, and real analyticity of Omega near every T0 preimage imply U=0. Analyticity is imposed on the original vorticity, not on the scattering map or the tail. Global real analyticity of Omega is a sufficient special case. This conclusion needs no semianalytic-set theorem and no nodal hypothesis.

## 5. An explicit condition entirely on the original profile

Assume in addition to Section1 that U is smooth and, for each integer j>=0, there is a finite C_j such that

    |D^j U(y)|<=C_j (1+|y|)^(-p-j).

For the usual natural rescaling u_t(z)=exp((1-c)t) R_t U(exp(tA)z), rotations preserve norms and cp=1-c. Thus, for t>=0 and z!=0,

    |D^j u_t(z)|<=C_j |z|^(-p-j).

On each compact annulus these are uniform bounds at every order. Arzela-Ascoli applied successively to derivatives produces convergent subsequences in every finite C^j norm. Their function limits equal the already unique actual tail V, so V is smooth. This is the confirmed A1145 argument; it needs neither a uniform analytic radius nor factorial growth control of the constants.

If Omega is real analytic near all T0 preimages, in particular if Omega is real analytic throughout R3, Section4 now proves U=0. This tail proof uses separate constants C_j, together with an independent analytic-original-vorticity premise. It does not assert that these derivative estimates alone imply analyticity or finite order. Scope correction A1213-A1214: the entire global smooth-U, zero-helicity class is already excluded by A309 under decay, without these extra derivative or analytic assumptions. Section4 remains useful when smoothness and analyticity are only local near the relevant tail points and original preimages.

## 6. Scope, dependencies and verification

The proof uses the actual C1 invertible scattering identity, the common supported zero theorem A1057, the finite-order theorem A1151, and the smooth-tail compactness statement A1145. Support is essential in Section4: an analytic vorticity field may vanish on a neighborhood of an unsupported point.

The theorem leaves open whether every bare-decay profile satisfies the derivative estimates, whether the helicity premise can be removed, whether a merely C1alpha tail has enough local structure, and whether smooth original vorticity can be flat at all relevant preimages. It makes no inference from original analyticity alone to tail analyticity.

No numerical computation, formal build, external model client or extra agent is used. A focused comparison with the existing configured model agents is pending. Their configured model has been checked separately, while runtime provider identity remains unattested.
