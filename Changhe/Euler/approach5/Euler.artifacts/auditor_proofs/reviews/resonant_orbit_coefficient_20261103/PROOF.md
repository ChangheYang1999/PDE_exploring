# The actual resonant pressure coefficient along characteristics

## 1. Exact class and notation

Fix 2/5<c<1/2 and finite real omega. Set a=1-2c, b=2-2c=a+1, p=(1-c)/c, Jx=e3 cross x and A=cI-omega J. Let U in C2(R3;R3), P in C1(R3) satisfy

    div U=0,
    ((1-c)I+omega J)U+DU(Ay+U)+grad P=0,
    U.curl U=0,
    |U(y)|<=C(1+|y|)^(-p), |DU(y)|<=C(1+|y|)^(-p-1).

Here C is finite and may depend on the solution and omega. Use the canonical pressure constant Pinf, B=Ay+U, H=P-Pinf+|U|²/2+(Ay).U, Q=P-Pinf-|U|²/2 and g=H-Q. For the actual scattering conjugacy Xi, choose x0 in D=R3 minus{0}, y0=Xi^(-1)x0 and the complete characteristic y_t=Phi_t(y0). Put z_t=exp(-tA)y_t, so z_t->x0.

Let R_t=exp(omega tJ), u_t(x)=exp((1-c)t)R_t U(exp(tA)x), p_t(x)=exp(bt)(P(exp(tA)x)-Pinf), S_t=p_t-|u_t|²/2. Their actual leading limits are V,P2,S=P2-|V|²/2. Write W=curl V, X=Ax, k=X.V and Z=DV V+grad P2. Every reference to these tails and the orbit-sign law retains the full global class above. Bare velocity decay alone is not enough.

## 2. Which resonant fact was actually proved

The complete nine-section proof in the team records, A653-A655, was reread. At c=3/7 it gives the ordinary locally uniform limit

    q_t=exp(t)(p_t-P2) -> pbar1.

It is not merely a period average: its potential logarithmic coefficient and every nonconstant rotation-periodic harmonic mode were separately eliminated using global zero helicity, the natural bounds, the scalar symmetry theorem and the actual-tail axisymmetric exclusion. No raw borderline tensor moment was asserted convergent, and only the contracted harmonic moments were set to zero.

The function selected by this limit obeys

    pbar1(exp(sA)x)=exp(-(3-2c)s)pbar1(x),
    -Delta pbar1=partial_i partial_j(V_i Z_j+Z_i V_j),
    pbar1-2V.grad P2 in C^(1,alpha)_loc, every alpha<1.

The homogeneous Poisson equation alone does not select pbar1: |x|^(-5)P4(x3/|x|) is an admissible nonzero harmonic addition. For omega=0, the actual nonrotating C1 Liouville theorem A010, re-audited in A197, already gives U=0 and P=Pinf. No rotation period is used in this case. The previous dependency's citation A053 was a wrong identifier and has been corrected to these identifiers; its underlying conclusion is unchanged.

For c!=3/7 the full A575/A623 proof already supplies the same ordinary limit with pbar1=p1. Thus the limit now exists at every c in the campaign interval.

## 3. Exact expansion on the moving characteristic

A539 gives w_t=exp(t)(u_t-V)->Z locally in positive Holder norms and S_t->S in C1. Direct algebra, without differentiating a remainder, gives

    exp(t)(S_t-S)=q_t-V.w_t-exp(-t)|w_t|²/2
                ->Sbar1=pbar1-V.Z.

The exact differential equation z_t'=exp(-t)u_t(z_t), boundedness on a fixed compact subset of D and terminal integration give

    z_t-x0=-exp(-t)(V(x0)+o(1)).

At k(x0)=S(x0)=0, the exact identity exp(bt)Q(y_t)=S_t(z_t) and the integral first-order Taylor formula give

    exp((b+1)t)Q(y_t)->Sbar1-V.grad S
        =pbar1-2V.grad P2=:sigmabar1.

The cancellation uses V.DV V=V.grad(|V|²/2). Next BH=-a(H-Q) gives

    (exp(at)H(y_t))'=a exp(at)Q(y_t).

Its terminal limit is k(x0)=0. Since b+1=a+2, the future integral is absolutely convergent. Integrating its leading coefficient and bounding the error by its supremum after t yields

    exp((a+2)t)(Q,H,g)(y_t)
       ->sigmabar1(x0)(1,-a/2,-(a+2)/2).

In particular, at c=3/7 the common rate is15/7 and the vector is (1,-1/14,-15/14). At V(x0)=0, sigmabar1(x0)=pbar1(x0). This reconstructs C50's proof with the actual resonant limit, not a separately chosen homogeneous pressure solution.

## 4. Signs and the transverse rank alternative

The confirmed C47/C49 inputs hold for every target c. At a supported zero of W with range DW contained in R X0, g(y_t)<=0 for every real t. At any zero of W, DW is nilpotent and DW X0=0; rank two implies X0 lies in its range. If X0 lies in that range, g=H=Q=0 on the characteristic and k=S=0. If V=W=0 and DW!=0, the range is exactly R X0.

Apply these facts to Section3. At a supported W-zero point with DW=0 and k=S=0, sigmabar1>=0. If X0 is in range DW, then k=S=sigmabar1=0. On

    T0={V=DV=0,S=0} intersect supp W,

these alternatives give pbar1>=0, with equality where DW!=0. At a point of T0 where V is C2 nearby and vanishes to infinite order, DW=0, so only nonnegativity is forced. If pbar1>0 there, H and g are strictly negative for all sufficiently late t. Flatness alone does not force the coefficient to vanish.

Conversely suppose x0 is a supported zero of W with k=S=0 and sigmabar1<0. The preceding sign laws rule out DW=0 and X0 in range DW, and V=0 would force that range condition. Rank two is excluded, so V!=0 and

    DW=w tensor ell, w not parallel to X0,
    ell(w)=ell(X0)=0.

Nilpotence gives the first zero pairing and DW X0=0 the second. The support and W-zero hypotheses are indispensable to this conclusion.

## 5. Smooth correction means at a common flat point

If V and P2 are smooth and vanish to infinite order near x0, then Z and V tensor Z+Z tensor V do too. The distributional Poisson equation in Section2 has a smooth right side, so local elliptic regularity makes pbar1 smooth. Its Laplacian vanishes to infinite order at x0. For the spherical average M(r),

    (r² M'(r))'=r² average_(dB_r) Delta pbar1.

Integrating twice with M(0)=pbar1(x0) gives M(r)=pbar1(x0)+O(r^N) for every N. This says nothing about the other jets of pbar1, which can contain a harmonic part. It also supplies no sign bound for the leading pressure on full neighboring spheres from information on a single characteristic.

## 6. Verdict and dependencies

All four current C51 sections, all nine A653-A655 dependency sections and the relevant complete C50 derivation were read. The exact coefficient and signs are confirmed for the full class in Section1, including c=3/7 and every finite omega. The resonance restriction in the earlier C50 audit is removed for these actual selected-coefficient conclusions, not for uniqueness of the resonant homogeneous Poisson problem. The main common-flat and bare-decay questions remain open. This is a continued comparison with the existing configured model C agent; provider runtime is unattested. No computation or formal build was needed.
