# Sharp matrix constant in the common-flat strain test

Status: independent audit of LIT294. The proof below checks the exact local statement; global nonexistence and any endpoint optimality remain open.

## 1. Statement, notation and dependencies

Let 0<c<1/2, omega be any real number, Jx=e3 cross x, A=cI-omega J, X(x)=Ax, L=(1-c)I+omega J, a=1-2c, b=2(1-c), eta=a/b and q=1/eta. Let G be a smooth X-flowbox around one orbit segment Gamma through x0!=0. On G let V and S be smooth real fields, W=curl V, E=|V|^2, with

    div V=0, X dot V=0, (X dot grad)V=-LV,
    (X dot grad)S=-bS, X cross W=aV, W dot grad S=0,
    P=S+E/2, -Delta P=tr((DV)^2).

Assume S=0 on Gamma, S<0 on G minus Gamma, and V,S vanish to infinite order at x0. Derivative matrices use (DV)_ij=partial_j V_i, and matrix norms are Frobenius norms. Define

    C(mu)=1+sqrt(2mu) for 0<=mu<=9/2,
    C(mu)=sqrt(4+8mu/3) for mu>=9/2.

For every mu>=0 with eta C(mu)<1, every neighborhood of x0 contains a point where |sym DV|^2>mu|W|^2. In particular mu=12 is allowed throughout 2/5<c<1/2, and mu=1/2 throughout 0<c<1/2, for every omega. The algebraic constant is sharp for the matrix problem below, with no claim of sharpness for fields satisfying these equations.

Dependencies are the local flowbox theorem, elementary differential inequalities along curves, the strong maximum principle for harmonic functions, and compact continuation of a smooth ordinary differential equation. The tensor lemma and matrix estimate used from C61/A1610 are proved here. The argument concerns a local pressure with an exact Poisson equation; it uses no choice of whole-space pressure normalization or condition at infinity.

## 2. A sharp trace-free matrix inequality

Let D be a real trace-free 3 by 3 matrix. Write B=(D+D^T)/2 and define w by (D-D^T)h=w cross h. Given v!=0 with w dot v=0 and |B|^2<=mu|w|^2, we claim

    |2D^T v|<=C(mu)|w||v|.

For w=0 the hypothesis gives B=0, hence D=0. Otherwise an oriented orthonormal frame sends v/|v| to e1 and w/|w| to e3. If the first column of B/|w| is (alpha,beta,delta), trace zero and minimization over the remaining diagonal entries imply

    |B/|w||^2 >= 3alpha^2/2+2beta^2+2delta^2.

The normalized squared left side is 4alpha^2+(2beta-1)^2+4delta^2. For t=|beta|, we have 0<=t<=sqrt(mu/2). Since

    4alpha^2+4delta^2 <= (8/3)(3alpha^2/2+2delta^2),

its squared norm is at most

    (8/3)(mu-2t^2)+(2t+1)^2
      =8mu/3-4t^2/3+4t+1.

The vertex of this concave quadratic is t=3/2. If mu<=9/2 the maximum on the allowed interval is attained at sqrt(mu/2), giving (1+sqrt(2mu))^2. If mu>=9/2 the vertex is permitted, giving 4+8mu/3. Both formulas agree at mu=9/2.

For sharpness take w=e3, v=e1, t=min(3/2,sqrt(mu/2)), alpha=sqrt((2/3)(mu-2t^2)), and

    B=[[alpha,-t,0],[-t,-alpha/2,0],[0,0,-alpha/2]],
    D=B+[w cross]/2.

It satisfies |B|^2=mu and every preceding inequality is an equality. The case mu=0 is included. These are matrix data, with no embedding into a field claimed.

## 3. The gradient inequality and positivity before logarithms

Suppose the forbidden strain bound holds on a neighborhood. Write H=-S and lambda=eta C(mu), so 0<lambda<1. Since A is invertible, X(x0)!=0. Choose a small plane disc D0 through x0 orthogonal to X(x0), whose short X-flowbox is contained in that neighborhood and meets Gamma only at x0. The linear transport gives XE=-bE and XH=-bH. Thus R=E/H is X-invariant wherever H>0, and V vanishes along Gamma.

Take grad S cross the equation X cross W=aV. The triple-product identity and XS=-bS, W dot grad S=0 give

    bS W=a grad S cross V,
    W=eta grad(log H) cross V.

In particular W dot V=0. Apply Section 2 to D=DV and v=V where V!=0. It yields

    |grad E|=|2(DV)^T V|
       <=C(mu)|W||V|
       <=lambda |grad log H| E.                 (3.1)

At V=0 both sides of (3.1) vanish directly. At W=0 the strain assumption also gives DV=0. On compact subdiscs of D0 minus {x0}, the coefficient |grad log H| is bounded. Gronwall along segments shows that a zero of E forces E=0 on a small disc, and conversely a positive value stays positive along any compact connecting path. Connectedness of the punctured two-dimensional disc therefore gives either E>0 everywhere or E=0 everywhere there.

In the second case transport and continuity give V=0 on the whole short flowbox. The Poisson equation then makes S harmonic there. Its interior maximum zero at x0 contradicts S<0 off Gamma. Thus E>0 on the punctured disc. All subsequent logarithms are well-defined.

## 4. The bounded-ratio sequence from pressure

We prove the needed tensor fact. Let T be smooth, symmetric and infinitely flat at the center of a three-dimensional ball, with div div T=0 and alpha h I<=T<=beta h I for h>=0 and fixed 0<alpha<=beta. Write A0(r) for the sphere average of n dot T(rn)n and B0(r) for the sphere average of tr T(rn)-n dot T(rn)n. Integrating div div T=0 on the enclosed ball and using the spherical divergence identity gives

    A0'(r)+(2A0(r)-B0(r))/r=0.

There is no point flux at the center: T is smooth there. The comparison implies B0<=2(beta/alpha)A0 and A0>=0, hence A0'<=K A0/r with K=2(beta/alpha-1). Thus r^(-K)A0(r) is nonincreasing, or

    A0(r)>=(r/r1)^K A0(r1), 0<r<r1.

Flatness gives A0(r)=O(r^m) for every integer m. Taking m>K and r down to zero forces A0(r1)=0. Positivity and the tensor comparison then give h=0 and T=0 throughout the ball.

If liminf E/H at x0 off Gamma were greater than 2, fix Rl>2 below that liminf and shrink the ball so that R>=Rl. For T=V tensor V+PI we have div div T=tr((DV)^2)+Delta P=0, using div V=0. Since P=E/2-H, its eigenvalues lie between (1/2-1/Rl)E and 3E/2. The comparison extends to Gamma because E=P=0 there. T is infinitely flat because V,S are flat. The tensor fact gives E=P=S=0, contrary to the strict sign of S. Hence liminf R<=2.

Choose y_j off Gamma with y_j->x0 and R(y_j)<3. The inverse short flowbox sends y_j to sigma_j in D0 minus {x0}, with sigma_j->x0 and R(sigma_j)<3 by invariance. Also H(sigma_j)->0. No lower bound on H uniform in j is asserted or needed.

## 5. Exact oblique projection estimates

Put u=grad log H and z=grad log R, as ambient gradients along the punctured disc. Then

    u dot X=-b, z dot X=0, |u+z|<=lambda|u|.

Let e=X/|X| and n0=X(x0)/|X(x0)|. Shrink the disc until epsilon=|n0-e|<=min(1/2,(1-lambda^2)/(6lambda)). Set beta0=b/|X| and nu=(1-epsilon^2/2)^(-1). The constraints imply beta0<=lambda|u|, and 1<=nu<=1+epsilon^2<=2. The vector

    Z=u-[(u dot n0)/(X dot n0)]X

is tangent to D0. Direct substitution gives

    u dot Z=|u|^2-nu beta0^2+nu beta0 u dot(n0-e).

The lower bound is at least [1-lambda^2-epsilon^2 lambda^2-2epsilon lambda]|u|^2. Because epsilon lambda<=1/2, the last two errors are at most (5/2)epsilon lambda<=(5/12)(1-lambda^2). In particular

    u dot Z >= (1-lambda^2)|u|^2/2.

Dropping the negative term gives u dot Z<=(1+2epsilon lambda)|u|^2<=(1+lambda)|u|^2. Since z dot X=0 and |u+z|<=lambda|u|,

    z dot Z=z dot u<=-(1-lambda)|u|^2.

For gamma=(1-lambda)/2 it follows that

    (z+gamma u) dot Z<=-(1-lambda)^2|u|^2/2.

This verifies the constants and signs independently of the copied C61 argument. If Xmax bounds |X| on a closed surrounding ball, then |u|>=b/(lambda Xmax), so Z(log H) has the positive uniform lower bound (1-lambda^2)b^2/(2lambda^2 Xmax^2).

## 6. Continuation and contradiction

Choose a fixed small circle C about x0 in D0 and take sigma_j inside it. Along the forward Z-trajectory from sigma_j, H is increasing, so H>=H(sigma_j)>0. For this individual j, the part of the closed disc where H>=H(sigma_j) is compact and stays a positive distance from x0. If the trajectory did not reach C, smooth ODE continuation on this compact set would extend it for every positive time. The positive uniform lower bound on Z(log H) would then contradict boundedness of H on the disc. It must therefore reach C at some point z_j.

The other inequality in Section 5 gives

    log R(z_j)+gamma log H(z_j)
       <=log 3+gamma log H(sigma_j) -> -infinity.

Both E and H are continuous and strictly positive on C, so the left side has a finite lower bound independent of j. This is the required contradiction. It uses no global completeness assumption on the punctured disc and no uniform lower bound on H(sigma_j).

## 7. Constants and exact limits

Since q=2(1-c)/(1-2c)>2, solving C(mu)<q gives mu<(q-1)^2/2 when 2<q<=4 and mu<3(q^2-4)/8 when q>=4. At q=4 both give 9/2. In the target interval q>6, C(12)=6, so mu=12 is admissible. At c=2/5 it is not admitted by this proof. Also C(1/2)=2 and eta<1/2 for every 0<c<1/2. Since tr((DV)^2)=|sym DV|^2-|W|^2/2, the latter case gives positive trace arbitrarily close to x0.

Only div V=0 and the already forced W dot V=0 sharpen C61's matrix estimate. Every local sign, smoothness, common-flatness, orbit-zero-set and exact pressure premise remains in force. The bound holds for every finite omega without an angular-period assumption. The strict endpoint eta C(mu)=1, optimality within the field equations, nonnegative trace in a neighborhood, sign-changing S, general common zero sets and unrestricted global-profile nonexistence remain open. No computation or formalization is used.
