# A nonzero homogeneous trace at infinity

Date: 2026-10-20. Status: independent informal proof, submitted to the lead for Opus review. This result does not establish either strong-setting endpoint or freedom to prescribe far-field data.

## Statement and hypotheses

Let rho be a nonzero real C^(2,alpha)_loc function on R^2, with 0<alpha<1, even in x and odd in y. Suppose, for a constant C and an exponent 0<gamma<1,

    |rho(X)| + (1+|X|)|grad rho(X)| <= C(1+|X|)^gamma.

Let U be its canonical velocity,

    U(X) = -rho(X)e_2/2 + lim_(R->infinity) PV int_(|Y|<R) K(X-Y)rho(Y)dY,
    K_1(Z) = -z_1 z_2/(pi |Z|^4),
    K_2(Z) = (z_1^2-z_2^2)/(2pi |Z|^4).

Assume c_l>1 and the exact equation (c_l X+U).grad rho=rho on the whole plane. Put k=1/c_l. Then k<=gamma, and there is a unique nonzero F on the circle such that, uniformly in theta,

    rho(r theta) = r^k F(theta) + O(r^(k+gamma-1)),   r->infinity.

Here theta denotes a unit vector. The function F has the inherited x-even and y-odd parities and is Holder continuous with exponent

    beta_0 = (1-gamma)/(1-k),   0<beta_0<=1,

where exponent1 means Lipschitz continuity. In addition,

    |U(X)| <= C'(1+|X|)^k,
    r^(-k)U(r theta) -> U_infinity(theta)

uniformly on the circle. U_infinity is the canonical velocity of the homogeneous density rho_infinity(X)=|X|^k F(X/|X|), with rho_infinity(0)=0. This density need not be differentiable at zero, but its velocity is well-defined by the displayed principal-value law for X!=0 and by parity at zero.

For nonzero profiles in the task's admissible class, the published R2 already gives c_l>1 and 0<gamma<1, so these hypotheses impose no extra source regularity. No smoothness at the center, positivity, minimal stagnation topology or finite angular support is used. The proof below recalls and proves the relevant growth consequences rather than assuming the sharper velocity bound it seeks.

## 1. Kernel estimates and growth along characteristics

Each component of K is homogeneous of degree-2, has zero integral on every circle centered at zero, and satisfies |D K(Z)|<=C|Z|^-3. Since rho(-Y)=-rho(Y), symmetric far tails can be paired. For |Y|>2|X|,

    |K(X-Y)-K(X+Y)| <= C |X| |Y|^-3.

The integral of this expression times |rho(Y)| converges for gamma<1. Near X, subtract rho(X) and use its gradient. At radius r=|X|>=2, the local ball |X-Y|<r/2 contributes at most C r^(gamma-1)r. The part |Y|<=2r outside that ball contributes at most C r^-2 int_0^(2r)(1+s)^gamma s ds <= C r^gamma. The paired far part contributes at most C r int_(2r)^infinity s^(gamma-2)ds <= C r^gamma. Including the local term gives U(X)=O((1+r)^gamma). Local C^1 regularity of U follows by the same principal-value construction and the stated C^(2,alpha) regularity; in particular W=c_l X+U generates a unique global flow because it is locally Lipschitz and has at most linear growth.

Along this flow, rho(X(t))=e^t rho(X(0)). A trajectory with nonzero initial density cannot stay bounded. Choose R0 large enough that outside it

    c_l r/2 <= r' <= 3 c_l r/2,
    r'/r = c_l + O(r^(gamma-1)).

After such a trajectory first reaches R0 outward, it never returns, and r grows at least exponentially. Consequently the error term in the second identity is integrable in forward time. Thus e^(-c_l t)r(t) has a finite positive limit. Now e^(-c_l t)U(X(t)) is integrable, since r(t) is comparable to e^(c_l t) and gamma<1. It follows that e^(-c_l t)X(t) tends to a vector Q!=0. Comparing e^t|rho(X(0))| with C r(t)^gamma gives 1<=c_l gamma, or k<=gamma.

Every point with r>R0 can be traced backward to the sphere R0, in a time T. The radial equation and r'>=c_l r/2 give a uniform bound

    int_0^T r(t)^(gamma-1)dt <= (2/c_l)int_(R0)^infinity s^(gamma-2)ds.

Therefore T=k log(r/R0)+O(1), uniformly over the endpoint on radius r. Transport from the bounded values on radius R0 now gives the improved density bound

    |rho(X)| <= C(1+|X|)^k.                                      (1)

This argument permits trajectories on which rho is zero, because their transported density remains zero. Only the assertion Q!=0 with a nonzero transported value used the choice of a nonzero trajectory.

## 2. A preliminary logarithmic velocity bound and radial trace

We retain the original gradient bound, which has exponent gamma-1; it has not yet been improved to k-1. To estimate the local principal value at |X|=r, split its ball of radius r/2 at

    delta_r = r^(1+k-gamma)/8 <= r/8.

Inside delta_r the gradient estimate gives C r^(gamma-1)delta_r <= C r^k. Between delta_r and r/2, use (1) after subtracting rho(X), giving C r^k[1+log(r/delta_r)]. The medium and paired far regions are bounded by C r^k exactly as in step1, with k in place of gamma. Hence

    |U(X)| <= C r^k(1+log r),   r>=2.                            (2)

For fixed unit theta the exact transport equation gives the exact radial derivative identity

    d_r[r^(-k)rho(r theta)] = -k r^(-k-1) U(r theta).grad rho(r theta).  (3)

Indeed c_l r rho_r-rho=-U.grad rho and c_l k=1. Combining (2) with the original gradient bound makes the right side at most C r^(gamma-2)(1+log r), uniformly in theta. This is integrable at infinity. Thus r^(-k)rho(r theta) has a uniform limit F(theta), continuous as a uniform limit of continuous functions, with

    |r^(-k)rho(r theta)-F(theta)| <= C r^(gamma-1)(1+log r).       (4)

Uniqueness and parity follow directly from the limit. The angular Lipschitz constant of r^(-k)rho(r theta) is at most C r^(gamma-k). For a small angular distance d, take r=d^(-1/(1-k)). Comparing both values with (4) yields

    |F(theta)-F(eta)| <= C d^beta_0(1+|log d|).

Consequently F belongs to C^beta for every 0<beta<beta_0. If gamma=k, the angular Lipschitz constants are already uniformly bounded, so F is Lipschitz. At this stage it suffices that some beta>0 exists.

## 3. Removing the logarithm from the velocity bound

Define rho_infinity(X)=|X|^k F(X/|X|). On an annulus comparable to radius r its Holder seminorm is at most C r^(k-beta). It is odd under X->-X and has growth r^k with k<1. The principal value at a nonzero point exists by this Holder bound; the paired far integral converges. Scaling the symmetric integral gives a homogeneous velocity U_infinity of degree k, with |U_infinity(X)|<=C|X|^k. There is no added harmonic strain.

Set E=rho-rho_infinity. Globally |E(Y)|<=C(1+|Y|)^k. On an annulus comparable to a large r, (4) gives

    |E(Y)| <= C r^(k+gamma-1)(1+log r).                          (5)

Although E need not have a classical gradient, its local increment can be bounded by the sum of the increments of rho and rho_infinity. At |X|=r let eta_r=r^(-m), h=r eta_r, where m>gamma-k is fixed. The principal value over |Z|<h, after subtracting E(X), obeys

    r^(-k) |int_(|Z|<h) K(Z)[E(X-Z)-E(X)]dZ|
       <= C[r^(gamma-k)eta_r + eta_r^beta] = o(1).              (6)

This follows by integrating the bounds C r^(gamma-1)|Z| and C r^(k-beta)|Z|^beta against |K|. On h<|Z|<r/2, (5) and the zero-circle-mean kernel give a bound

    C r^(gamma-1)(1+log r) log(r/h) = o(1)                     (7)

after division by r^k. The local term -E(X)e_2/2 has the same vanishing normalized bound. In the medium region |Y|<=2r, |X-Y|>=r/2, and in the paired far region |Y|>2r, the coarse global bound on E gives O(r^k), by the estimates of step1 with k. Thus U[E]=O(r^k). Linearity of the common symmetric principal values implies

    U=U_infinity+U[E]=O(r^k).                                 (8)

This step uses the positive Holder continuity already proved for F. It does not assume gradient convergence to rho_infinity or interchange a nonuniform singular integral with a limit.

## 4. Sharp stated trace remainder and Holder exponent

Insert (8) in (3). Its absolute right side is now at most C r^(gamma-2), so (4) improves to

    |r^(-k)rho(r theta)-F(theta)| <= C r^(gamma-1).              (9)

The limit is the same unique F. Comparing angular values as in step2, with r=d^(-1/(1-k)), gives |F(theta)-F(eta)|<=C d^beta_0. This proves the stated exponent and density remainder, including beta_0=1. No assertion is made that the original gradient has improved decay or that F has more derivatives.

## 5. Uniform convergence of the scaled velocity

It remains to improve the coarse O(r^k) estimate for U[E] to o(r^k). The local singular region is already o(r^k) uniformly in theta by (6)-(7). These bounds remain true with the improved remainder (9). In the remaining medium region scale Y=rZ. For any fixed 0<tau<1/2 and T>2, on tau<=|Z|<=T away from |Z-theta|<1/2 the normalized density difference r^(-k)E(rZ) tends uniformly to zero by (9); the kernel is uniformly bounded and the region has finite area. Its contribution tends to zero uniformly in theta.

The small scaled ball |Z|<tau is away from the observation circle. There

    r^(-k)|E(rZ)| <= C(r^(-k)+|Z|^k),

so its absolute contribution is at most C[r^(-k)tau^2+tau^(k+2)]. Finally E is odd, so the far scaled tail |Z|>T is paired and bounded by C[T^(k-1)+r^(-k)/T], uniformly in theta and r>=2. First choose tau small and T large, then take r large. Both remainder bounds vanish in this order. Therefore r^(-k)U[E](r theta)->0 uniformly, which is the claimed velocity limit.

## 6. The trace cannot vanish identically

Choose a characteristic with rho(X(0))!=0. Step1 gives e^(-c_l t)X(t)->Q!=0, hence X(t)/|X(t)|->Q/|Q| and

    |X(t)|^(-k)rho(X(t)) -> |Q|^(-k)rho(X(0)) != 0.

The uniform radial convergence (9) and continuity of F identify this limit with F(Q/|Q|). Thus F is not identically zero. This also rules out a nonzero exact profile with rho=o(r^k) uniformly at infinity under the stated assumptions.

## Dependencies and scope

The proof uses elementary singular-kernel cancellation, classical ODE existence for locally Lipschitz vector fields, and the exact pointwise transport equation. The class-wide forced regime c_l>1 is the previously audited R2; the theorem itself states it explicitly. Every other estimate needed for the conclusion is proved above. There is no assertion that F can be prescribed independently, that two profiles have different traces, or that a fixed F selects a unique profile. An exterior homogeneous limit need not solve the full stationary equation: its leading transport part c_l X.grad rho_infinity=rho_infinity is automatic, whereas its nonlinear self-advection has lower degree2k-1. No condition U_infinity.grad rho_infinity=0 follows from this theorem.

The compact extension in ../compact-extension/PROOF.md does not contradict the theorem, because that field fails the profile equation outside a prescribed bounded set. The result does not decide B_3, source higher derivatives, exact linearized kernel dimension, YES_inf or NO_inf. It describes a necessary global datum and gives a controlled meaning to the phrase far-field data in Task question1.

## Manufactured inverse test

For a separate check of kernel signs and homogeneous scaling, use the smooth density

    rho_test=x^2 y (1+r^2)^((k-3)/2),  k=1/5.

It has asymptotic F(theta)=cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4. Its homogeneous stream function is

    psi_infinity=r^(k+1)[a2 sin(2theta)+a4 sin(4theta)],
    a2=(k+1)/(4(1-k)(k+3)),   a4=-1/(8(k+5)).

To derive these coefficients, differentiate r^k sin(n theta) in x, obtaining r^(k-1)[(k+n)sin((n-1)theta)+(k-n)sin((n+1)theta)]/2, and apply -Laplace to each stream mode. Thus

    U_infinity/r^k = -[2a2 cos(2theta)+4a4 cos(4theta)] e_r
                    +(k+1)[a2 sin(2theta)+a4 sin(4theta)] e_theta.

The independent split kernel can be compared with this formula at growing radii. This test field is not a profile: it does not satisfy the transport equation or the central identity at c_l=5. Numerical agreement is evidence for the inverse implementation only, not a proof of the trace theorem. Exact symbolic and numerical evidence are kept under verification.
