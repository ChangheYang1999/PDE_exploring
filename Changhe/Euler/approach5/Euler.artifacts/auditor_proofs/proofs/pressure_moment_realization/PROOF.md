# Realizing finitely many pressure moments with a distant velocity perturbation

## Exact statement

Let c>0 and omega be finite, A=cI-omega J, and let U0 in C_c-infinity(R3;R3) be divergence-free. Put B0=Ay+U0. Let mu be a compactly supported B0-invariant probability with support Sigma. Assume:

1. Sigma has three-dimensional Lebesgue measure zero and R3 minus Sigma is connected.
2. If c!=1/2, integral U0 dot B0 dmu=0.
3. If the vector measure (lambda1 U0+lambda2 y+lambda3 Jy)mu is distributionally divergence-free, then (lambda1,lambda2,lambda3) is a multiple of (1,c,-omega).

For every nonempty open Z whose closure is disjoint from Sigma and supp U0, there exists a divergence-free V in C_c-infinity(Z) such that U=U0+V, with its canonical pressure P, satisfies the pressure Poisson equation and all three moment relations R1-R3 of A124 against mu. The identity integral B dot grad P dmu=0 also holds. Near Sigma, U, B, curl U and the momentum field F agree with their unperturbed values. Nevertheless U is not an Euler profile.

For every c>0 and omega!=0, such data U0,mu exist with Sigma a periodic orbit on which both B0 and curl U0 are nonzero. This proves insufficiency of this finite pressure-moment package. It does not realize the full Euler equation, a regular-attractor basin, all possible moments, or all finite-time shrinking-domain balances.

## Canonical pressure and targets

For compact smooth divergence-free U, let N(x)=-1/(4pi|x|), so Delta N=delta0, and define

    P_can(U)=N*[-tr(DU)^2],
    F(U)=-[(1-c)U+(Ay+U) dot grad U+omega JU],
    D(U)=grad P_can(U)-F(U).

The pressure is smooth and satisfies its Poisson equation. Because supp V and supp U0 are disjoint,

    F(U0+V)=F(U0)+F(V),
    P_can(U0+V)=P_can(U0)+h_V,
    h_V=N*sigma_V,
    sigma_V=-tr(DV)^2=-partial_i partial_j(V_i V_j).

Thus near Sigma, D(U)=D(U0)+grad h_V, while the velocity and all its derivatives are unchanged.

Put V1=U0, V2=y, V3=Jy on Sigma, and define

    t_i=-integral V_i dot D(U0) dmu,
    ell_i(V)=integral V_i dot grad h_V dmu.

By A124, the desired moment relations are exactly ell(V)=t. Define the plane

    Pi={x in R3:x1+c x2-omega x3=0}.

Invariance gives ell(V) in Pi, because V1+cV2-omega V3=B0. A124 also gives

    t1+c t2-omega t3=(2c-1) integral U0 dot B0 dmu=0.

Hence t lies in Pi, including at c=1/2 without assumption 2.

## The dual harmonic potentials

For lambda in R3, let V_lambda=sum lambda_i V_i and define the compactly supported distribution

    <T_lambda,phi>=integral V_lambda dot grad phi dmu,
    Phi_lambda=N*T_lambda.

Explicitly Phi_lambda(x)=-integral grad N(x-y) dot V_lambda(y) dmu(y). Since grad N is locally integrable and V_lambda is bounded on Sigma, Phi_lambda is in L1_loc, is harmonic and analytic outside Sigma, and is O(|x|^-2) at infinity. Let H_lambda=D2 Phi_lambda off Sigma. Fubini and two integrations by parts, justified since V is smooth and supported away from Sigma, give

    lambda dot ell(V)=integral Phi_lambda sigma_V
                    =-integral V^T H_lambda V.           (1)

The distribution T_(1,c,-omega) vanishes by invariance, so H_(1,c,-omega)=0.

For z in Z and unit e define m(z,e) in Pi by

    m_i(z,e)=-e^T H_{e_i}(z)e.

These vectors positively span Pi. To see this, suppose a linear functional lambda is nonnegative on every m(z,e). Then H_lambda(z) is negative semidefinite for every z in Z. It is trace-free because Phi_lambda is harmonic, so H_lambda=0 on Z. Analytic continuation through the connected complement of Sigma gives H_lambda=0 everywhere there. Thus Phi_lambda is affine on that complement. Its decay at infinity makes it zero there. Since Sigma is null and Phi_lambda is L1_loc, it is zero as a distribution, and T_lambda=Delta Phi_lambda=0. Assumption 3 makes lambda a multiple of (1,c,-omega), which is the zero functional on Pi.

Here is the finite-dimensional step explicitly. If no finite subcollection of the m(z,e) positively spanned Pi, zero would fail to be an interior point of their convex hull in Pi. A separating line would then give a nonzero functional on Pi nonnegative on all of them, contradicting the preceding paragraph. Equivalently, finitely many of the m(z,e) surround zero in a polygon. This strict surrounding property persists under small perturbations.

## Exact realization by disjoint oscillatory fields

Choose finitely many (z_j,e_j) whose m vectors positively span Pi. By continuity, their z_j can be made distinct. Choose pairwise disjoint small balls in Z around these points. In the jth ball take a smooth compactly supported chi_j with integral chi_j^2=2, and choose a unit n_j perpendicular to e_j. Define

    V_j=curl[chi_j(y) K^-1 sin(K n_j dot y)(n_j cross e_j)].

Each V_j is smooth, compactly supported and divergence-free. For fixed chi_j and K tending to infinity,

    V_j=-chi_j cos(K n_j dot y)e_j+O(K^-1)

uniformly. Integration of the oscillatory cosine square against the smooth H fields yields

    ell_i(V_j) -> -(1/2) integral chi_j^2 e_j^T H_{e_i}e_j.

First choose the balls small, and then K large. These vectors are then arbitrarily close to m(z_j,e_j), so they still positively span Pi. Choose nonnegative theta_j with t=sum theta_j ell(V_j), and put V=sum sqrt(theta_j)V_j. Disjoint supports remove every quadratic cross term in sigma_V, so ell(V)=sum theta_j ell(V_j)=t exactly. Approximation was used only to preserve positive spanning; the final moment equality is exact.

The resulting U and P satisfy the claimed relations and leave a neighborhood of Sigma unchanged. The pressure contribution from V is harmonic there but generally nonzero.

## Why this velocity is not a profile

Assumption 3 forces U0 nonzero. Indeed if U0=0, invariance under B0=Ay and the test |y|^2 give integral |y|^2 dmu=0, so mu=delta0. Every V_lambda then vanishes on its support, violating assumption 3. Because the supports of U0 and V are disjoint, U is also nonzero.

If this nonzero compactly supported U were a profile, its nonzero-vorticity set would be an open B-invariant bounded set. The exact Cauchy law gives invariance, and the Jacobian exp(3ct) makes any invariant set have zero or infinite volume. A nonempty bounded open set cannot have either property. Thus curl U would vanish. Together with div U=0, compact support and smoothness, harmonicity would give U=0, a contradiction. This uses only the already confirmed A067 argument and does not assume the conjecture.

## Explicit data for every nonzero rotation

Fix real a,h,s with a h s!=0, and r>0. Define the polynomial divergence-free field

    W0(y)=omega a e2
       +[3c(y3-h)+s((y1-a)^2+y2^2-r^2)]e3-cy.

A polynomial vector potential exists for this divergence-free polynomial field, by the elementary radial homotopy formula for closed two-forms. Choose a compact smooth cutoff equal to one on a neighborhood of the circle

    gamma(theta)=(a+r cos theta,r sin theta,h),

and take U0 to be the curl of the cutoff potential. Then U0=W0 near gamma and is smooth, compactly supported and divergence-free.

On gamma,

    B0=-omega J(y-ae1),
    Omega0=2s(y2,a-y1,0),
    U0=omega a e2-cy.

The first field traverses gamma with period 2pi/|omega| and never vanishes. The second never vanishes there either. The U0 circulation is zero, because a constant vector and -cy both have zero circulation. Thus the normalized time measure mu_gamma satisfies assumption 2. The circle is null and has connected complement.

To check assumption 3, a distributionally divergence-free vector measure V_lambda mu_gamma must first be tangent to gamma: test functions vanishing on gamma have arbitrary smooth normal gradients there. Write V_lambda=kappa(t)B0. Testing arbitrary smooth functions on the time circle gives kappa constant. Hence

    (lambda1-kappa)U0+(lambda2-kappa c)y+(lambda3+kappa omega)Jy=0

on gamma. But det[U0,y,Jy]=-omega a h y2, nonzero at some points of gamma. Therefore lambda=kappa(1,c,-omega), as required.

In this example B0 and Omega0 are parallel on gamma. The construction does not place gamma in Reg={B cross Omega!=0}; nor does it enforce the vorticity transport equation there. It is a counterexample only to the finite moment package specified at the start.

## Verification and dependencies

This is an independent reconstruction of Theory Agent A C16, Proposition E.7 and Example E.8. Its inputs are the exact defect identities A124, elementary potential theory and analyticity off a compact support, finite-dimensional separation, oscillatory integration, and the already confirmed invariant-volume argument A067. No numerical computation was run or used as proof.
