# The expanding singular variant has no scalar Biot-Savart repair

## Exact statement and dependencies

Fix 2/5<c<1/2 and a finite real omega. Let J(y1,y2,y3)=(-y2,y1,0), A=cI-omega J, and let U0,W be the smooth independent bracket fields obtained from A066/A121 using the A252 parameters

    kappa=1+c, d=3c, a=1-2c,
    b=1-c/2, L=2-5c/2, q=b/L,
    K=1+sqrt(2)/(2q), T=log(Kq)/a,
    rho=exp(-kappa T), delta=(1-rho)/4,
    epsilon=min(delta,1/K-1/2)/2,
    m=(rho(1+2delta)+1+delta)/2.

Thus U0 is compactly supported, div U0=div W=0, B0=Ay+U0 is complete, and [B0,W]=-kappa W. This specifies the fixed construction, not an arbitrary bracket pair. Define

    V(y)=(1/(4pi)) integral_R3 W(z) cross (y-z)/|y-z|^3 dz.

Then V is smooth, divergence free, curl V=W, and V tends to zero at infinity. For every nonzero real eta,

    [eta V-U0,W] is not identically zero.                    (1)

Consequently eta V cannot be a rotating Euler profile with parameters c,omega and any pressure. The proof uses the exact block and filling constructions A066/A121, not the physical-measure conclusion A253. Their full constructions are in the team records and in the team records. The remaining argument is given below.

## 1. Geometry retained by the parameter change

In the target range q>1/sqrt(2). Thus

    1/q<K<2, Kq>sqrt(2)>1,
    0<epsilon<delta, K(1/2+epsilon)<1,
    rho(1+2delta)<m<1+delta,
    b K rho=L exp(-dT).                                    (2)

The last identity uses Kq=exp(aT) and kappa-a=d. These are exactly the strict footprint and signed-flux inequalities of A066. Its two return tubes and the short rounded incoming collars therefore still attach. The rounded boundary changes the domain only; it does not change the local vector field or return maps. The same cancelling-handle topology and smooth relative-volume correction are available for every such strict choice.

Write X=-B0. In the central core,

    X=(Lx,-kappa y,-bz), W=partial_y.

The only zero there is p=0, of B0-index sign det diag(-L,kappa,b)=-1. A return tube has X=partial_t and no zero. Each A121 filling has

    X_u=epsilon_f |u|^2 u,
    X_v=-(d+4epsilon_f |u|^2)v, epsilon_f>0.

Its only zero is on u=0, and the transported W vanishes exactly on that axis. Every u!=0 reaches the outgoing side in finite time (|u|^(-2)-1)/(2epsilon_f). Flat extension across the axes and fixed-time continuation through the cap centers yield exactly two smooth proper W-zero lines Z in the completed R3. Every point outside Z enters the original handlebody H in finite X time. The filling formulas require only kappa-d=a>0 and smooth side data, not the old value of K.

The Euclidean volume correction is a diffeomorphism, hence preserves zero sets, indices and finite orbit entry. Outside its ball B0=Ay, whose radial component is cr, so the continued exceptional lines are proper and no new carrier zero appears. Therefore p is the unique B0 zero outside Z.

Every nonempty open subset of H has a forward passage meeting a nonempty open subset of the incoming section z=1. In a return tube this is immediate. In the core the plane x=0 has empty interior; points with x!=0 exit through a side and then return to the top. The short incoming collars flow into these same pieces. On the section, the quotient return is

    f(x)=sign(x) K(|x|^q-1/2), 0<|x|<1,
    f'(x)=Kq |x|^(q-1)>=Kq>1.                              (3)

All returned points lie strictly inside the section. A section point with x=0 converges to p. These finite-entry statements are the only dynamical information needed below.

## 2. Recurrence and absence of closed W orbits

Put gamma=1/c, so 2<gamma<5/2. Exterior transport gives |W(y)|<=C(1+|y|)^(-gamma), with the corresponding derivative bounds. In particular W is bounded and its smooth flow Gamma_t is complete. Along any trajectory,

    |d_t(1+|Gamma_t y|)^(gamma+1)|<=(gamma+1)C

almost everywhere. Images up to time N of a bounded set lie in a ball of volume at most C0(1+N)^(3/(gamma+1)). The flow preserves volume. If a bounded measurable set E is wandering for Gamma_1, its N+1 disjoint images imply

    (N+1)|E|<=C0(1+N)^(3/(gamma+1)).

Since 3/(gamma+1)<1, |E|=0. Apply this to the nonreturning subsets of a countable basis of bounded balls and their last-return decomposition. Almost every point is recurrent under Gamma_1. Apply the same argument to Gamma_-1 for recurrence in the other direction.

There is no nonconstant periodic W orbit. Backward B0 time s transforms such an orbit of period T0 to a W orbit of period exp(-kappa s)T0, by the exact bracket transport. All these curves stay in one compact set because B0 is linear and outward outside a ball. On a containing convex ball let L0 bound DW. The periodic Wirtinger inequality gives every nonconstant W orbit period at least 2pi/L0: subtract its mean and estimate integral |z'|^2 by L0 ||z-zbar||_2 ||z'||_2. For L0=0 no such orbit exists. The exponentially shrinking periods are impossible.

## 3. A decaying first integral would create an impossible torus

For any smooth global W first integrals F,G,

    dF wedge dG=0 on R3 minus Z.                            (4)

Otherwise the map (F,G) is a submersion on a nonempty open subset of R3 minus Z. Sard's theorem and local submersion coordinates show that almost every point in this open set has a globally regular value. Choose such a recurrent point. Its fiber is a closed embedded one-dimensional manifold. A W orbit on a line component, or on a circle cut by zeros, is ordered and cannot recur at its starting point; the local embedded-fiber chart rules out return through a different accumulating sheet. A zero-free circle gives a periodic W orbit. Both cases contradict Section 2. This proves (4).

Suppose F is smooth, WF=0, F tends to zero at infinity, F|Z=0, and F is nonzero. A nonzero regular value exists by Sard and continuity. A connected component S of its level is a compact orientable embedded surface. The nowhere-zero tangent field W makes its Euler characteristic zero, so S is a torus. Set G=B0 F. The bracket gives WG=kappa WF=0. Equation (4) says G is constant on S. If that constant were zero, B0 would be tangent to S, contradicting div B0=d>0 on the bounded domain D enclosed by S. Otherwise B0 has a strict constant normal sign, and its positive total flux makes the sign outward.

Each connected proper line of Z is disjoint from S. It cannot enter the bounded side without lying wholly there, which would contradict properness and unboundedness. Thus D is disjoint from Z, and its forward X flow stays in D.

Take an interior point of D and a small open neighborhood. By finite entry and Section 1's return access, some forward passage produces an open section subset contained in D. Its x projection contains an interval I. If no successive defined branch image of I met zero, the lengths would grow by at least (Kq)^n while all images remained in (-1,1), an impossibility. Some finite image therefore contains zero. Choose a section point realizing that itinerary. Its finite returns stay in D and its final x=0 orbit tends to p. Hence p belongs to D; strict transversality puts it in the interior.

The sole zero in D is p. Poincare-Hopf for B0 pointing outward gives

    -1=index_D(B0)=chi(D)=chi(S)/2=0.

Here the middle topological equality follows by doubling the compact orientable three-manifold D, whose closed odd-dimensional double has Euler characteristic zero. No unknottedness assumption on the torus is needed. The contradiction proves that every such F is identically zero.

## 4. Biot-Savart inversion and the leading field

Let Q_t=exp(-(omega/c)J log t). Exact exterior transport extends W uniquely to a punctured-space field Wh with

    Wh(t Q_t y)=t^(-gamma)Q_t Wh(y).

It is locally integrable because gamma<3. Its flux through a sphere is constant by divergence freedom on annuli and scales as r^(2-gamma), so it is zero. Subtracting a test function's value at zero leaves boundary error O(r^(3-gamma)); hence div Wh=0 distributionally at zero as well.

The Newton potentials of W and Wh converge at infinity because gamma>2; for Wh use points y!=0. Curling them gives V and Vh with div V=div Vh=0, curl V=W and curl Vh=Wh. Local elliptic regularity makes V smooth. The same identities can be obtained by differentiating the Biot-Savart integral distributionally and then using its local regularity.

The field D0=W-Wh is compactly supported, integrable and distributionally divergence free. Testing div D0 against a coordinate function with cutoff equal to one on its support gives integral D0=0. Expansion of the Biot-Savart kernel at infinity therefore yields

    V=Vh+O(r^-3),
    Vh(t Q_t y)=t^(1-gamma)Q_t Vh(y),
    curl Vh=Wh!=0.                                        (5)

Differentiated remainders have the corresponding extra inverse powers. In particular V tends to zero. This proof is the exact inversion argument of A179 and does not depend on the return parameter K.

## 5. No nonzero scalar amplitude can obey the second bracket law

Suppose (1) failed for eta!=0. Both eta V-U0 and W are divergence free, so their cross product is curl free. Simple connectivity gives a smooth real F with

    grad F=(eta V-U0) cross W, WF=0.

Outside the compact support of U0, grad F=O(r^(1-2gamma)). Ray integration gives limits at infinity, and the oscillation on a radius-r sphere is at most pi r sup|grad F|=O(r^(2-2gamma)), so all limits agree. Normalize this common limit to zero. Then F=O(r^(2-2gamma)). Its full gradient vanishes on Z, so it is constant on each proper zero line and that constant is zero. Section 3 gives F=0.

It follows that V cross W=0 outside a ball. Apply (5), scale to infinity and undo Q_t. The scaled remainder is O(t^(gamma-4)), which tends to zero. Thus

    Vh cross curl Vh=0.                                    (6)

Put beta=gamma-1, so 1<beta<3/2. Since Vh is real and divergence free, (6) makes T=Vh tensor Vh-|Vh|^2 I/2 divergence free. For n=y/|y|,

    div(T n)=-|Vh dot n|^2/|y|.

Define A(r) and C(r) by integrating the radial and tangential squared components of Vh(r theta) over the UNIT sphere in theta. The annular divergence theorem gives

    d/dr [r^2(A(r)-C(r))/2]=-r A(r).

Twisted homogeneity gives A(r)=r^(-2beta)A(1) and C(r)=r^(-2beta)C(1). Therefore

    (2-beta)A(1)+(beta-1)C(1)=0.

Both coefficients and both squares are nonnegative, with strictly positive coefficients. Hence Vh=0, contradicting curl Vh=Wh!=0. This proves (1).

If eta V were an Euler profile, its vorticity eta W would satisfy [Ay+eta V,eta W]=-kappa eta W. Subtract [Ay+U0,W]=-kappa W after division by eta. The result is the impossible equation [eta V-U0,W]=0. Thus no pressure can repair this particular scalar reconstruction.

## Scope

This checks LIT54 for the entire target interval and every finite omega. The decisive new audit is the transfer of the exact zero-set and finite-entry geometry under the parameter change. The argument does not use transitivity, a physical measure or the singular-hyperbolic classification. It does not exclude a different W, a different completion, or a genuine Euler singular attractor.
