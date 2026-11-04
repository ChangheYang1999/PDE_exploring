# Fixed-direction tails: no zero and a local classification

## 1. Exact theorem and hypotheses

Let G be a connected open subset of R3, 0<c<1/2, omega finite, J(x,y,z)=(-y,x,0), X=(cI-omega J)x, a=1-2c, b=2(1-c), q=b/a>2. Let e be a fixed unit vector, V=u e be C1 on G, and P2 be C2. Put W=curl V, k=X.V and S=P2-|V|²/2. Assume

    div V=0,
    X.grad V=-(1-c)V-omega JV,
    X.grad P2=-bP2,
    -Delta P2=tr((DV)²),
    grad k cross grad S=0 on {W!=0}.                 (1)

Then V is identically zero or nowhere zero. In the second case S=0, P2=|V|²/2 is positive harmonic, and V is real analytic. If omega!=0, e must be axial. No full momentum equation, infinite flatness, original-profile reconstruction or uniform bound on component constants is assumed. Sections6-7 give an additional explicit local classification and full-annulus exclusion. The general variable-direction problem is not settled.

## 2. Geometry, harmonic pressure and the vortical nonzero set

Since e is constant,

    e.grad u=0, DV=e tensor grad u,
    tr((DV)²)=(e.grad u)²=0.

Thus P2 is harmonic on all G and u is locally independent of the e coordinate. Project velocity homogeneity perpendicular to e at a nonzero point. It gives omega Je=0. Therefore either omega=0 or the fixed direction is the rotation axis. Choose orthonormal coordinates with V=u e3, reversing u if necessary when the axis orientation is reversed. In the zero-rotation case the coordinate rotation is unrestricted. In these coordinates X3=cz and

    k=czu, X.grad u=-(1-c)u.

Moreover W=grad u cross e and e.grad u=0. If W=0 then grad u=0, and homogeneity forces u=0. Thus every nonzero velocity point lies in the open vortical set where rank is assumed.

## 3. Rank and the C1 regularity issue

Take a small connected product box where u and z have fixed nonzero signs. Homogeneity gives X.grad k=-ak and X.grad S=-bS. Since k!=0, grad k!=0. Rank therefore gives grad S=lambda grad k; contraction with X identifies lambda=qS/k. Hence

    S=D|k|^q=Dc^q|z|^q|u|^q                         (2)

for one finite constant D on the box.

Before differentiating twice in the horizontal variables, recover their regularity. The two functions P2(x,y,z1), P2(x,y,z2) at distinct positive absolute axial values are C2. Their equations

    P2(x,y,zi)=u²/2+Dc^q|zi|^q|u|^q

form an invertible linear system for u²/2 and Dc^q|u|^q, regardless of D. Thus u² is C2. Since u has fixed nonzero sign, taking its smooth square root makes u C2 there. No extra global velocity regularity has been assumed.

For a fixed horizontal point, write t=|z|. Harmonic pressure now reads

    A0+B0t^q+C0t^(q-2)=0,
    C0=Dc^q q(q-1)|u|^q.

Differentiate in the explicit variable t and multiply by t^(3-q). This gives qB0t²+(q-2)C0=0 on an interval, so C0=0 and D=0. Therefore P2=u²/2 and S=0 on every nonzero box with z!=0. Nonzero points on z=0 are limits of such points within the same open nonzero set, so the conclusion holds there too.

## 4. An explicit barrier rules out a zero

Suppose the nonzero set is neither empty nor all G. Connectedness supplies an internal boundary point. Choose a nonzero point p near that boundary with R=dist(p,{u=0})>0 and the closed ball B(p,R) contained in G. The distance is attained at a zero xstar. P2=u²/2 is positive in the ball, nonnegative on its boundary, and P2(xstar)=0. By C1 regularity and continuity of grad P2,

    grad P2(xstar)=lim_(x->xstar from the ball) u(x)grad u(x)=0.  (3)

On R/2<=|x-p|<=R choose lambda>6/R² and

    w(x)=exp(-lambda|x-p|²)-exp(-lambda R²).

It is positive inside the annulus, zero on the outer sphere, and

    Delta w=exp(-lambda|x-p|²)(4lambda²|x-p|²-6lambda)>0.

A sufficiently small epsilon>0 makes P2>=epsilon w on both boundary spheres. The function P2-epsilon w has strictly negative Laplacian; it cannot have a negative interior minimum. Thus the same inequality holds throughout the annulus. With nu=(xstar-p)/R,

    P2(xstar-t nu)>=2epsilon lambda R exp(-lambda R²)t+O(t²).

This contradicts(3), which makes the left side o(t). The nonzero set has no internal boundary, so it is empty or all G. In the latter case u has one sign and equals that sign times sqrt(2P2); harmonic analyticity makes u and V real analytic. The pressure equality and S=0 hold everywhere.

## 5. What the result excludes

This proves LIT233 at C1 velocity and C2 pressure regularity. In particular it strengthens A1386: no fixed-direction zero is possible, even of finite order, and omega=0 permits any fixed direction. There is no assumption that the zero lies in the support of vorticity. The theorem makes no extra claim about a harmonic homogeneous pressure when V is identically zero.

If G contains a point on the line R e through the origin, nonzero fixed-direction V is impossible. At that point divergence gives e.grad u=0, X is parallel to e in the admissible orientation, and homogeneity gives 0=-(1-c)u. The resulting zero and Section4 imply V=0 throughout G.

## 6. Additional explicit local classification away from the axis

Set p=(1-c)/c>1. In the permitted axial coordinates let tau=omega/c; for omega=0 and an arbitrary e, tau=0. On a local product chart with rho>0, theta=phi+tau log rho, every nonzero solution has

    V=epsilon0 rho^(-p)sqrt(h(theta)) e3,
    P2=(1/2)rho^(-2p)h(theta), S=0, epsilon0 in {1,-1},

where h>0. This follows directly from the homogeneity equation and independence of z. The two-dimensional Laplacian of the harmonic function 2P2 gives

    (1+tau²)h''-4p tau h'+4p²h=0.                  (4)

Solving its characteristic polynomial yields exactly

    h(theta)=exp(2p tau theta/(1+tau²))
       [C1 cos(2p theta/(1+tau²))+C2 sin(2p theta/(1+tau²))]. (5)

Conversely, on any chart where(5) is positive, the displayed fields satisfy every equation(1): divergence and homogeneity are direct, pressure is harmonic by(4), the rank equation holds because S=0, and tr((DV)²)=0. Thus this is an actual classification of the local nonzero fixed-direction necessary system, not merely a necessary ansatz. It does not assert full similarity momentum; in fact that additional equation would require grad P2=0 and is incompatible with a nonzero homogeneous P2 here.

## 7. Additional full-angular-annulus exclusion

Suppose, in addition to(1), that G is a full cylindrical annulus rho_-<rho<rho_+, z_-<z<z_+, with all angular values, about the admissible e axis. A nonzero solution would be nowhere zero by Section4. Its positive harmonic squared speed is rho^(-2p)h(phi+tau log rho), where h is a positive smooth2pi-periodic function. Integrating(4) over a period eliminates both derivative terms and gives

    4p² integral_0^(2pi) h(theta)dtheta=0,

contradicting positivity. Hence V=0 in this full-annulus class for every0<c<1/2 and every finite rotation rate. This is a statement about the restricted necessary system; it supplies no reduction of a general tail to fixed direction.

## 8. Verification and remaining scope

The complete seven-section source was read and pinned. The C1-to-C2 local recovery, distinct-power argument and barrier were independently reconstructed. Sections5-7 add analyticity, axis-contact exclusion, local classification and full-annulus exclusion. Each is analytic and requires no numerical or formal computation.

Comparison of these additions is requested through the existing configured model agents; provider runtime is unattested. No new model client or agent was used. Variable velocity direction, genuine axial dependence and the arbitrary-helicity whole-space conjecture remain outside the theorem.
