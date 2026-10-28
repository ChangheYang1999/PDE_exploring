# Additional disjoint reflection disks

## Statement

Use the real or complex scalar homogeneous Holder seminorm, circular principal-value operators, and positive local measure mu_R of the parent proof. Fix finitely many pairs (c_i,a_i) satisfying

    0<a_i<c_i/2, c_i+a_i<=1,
    |c_i-c_j|>=a_i+a_j for i!=j,
    P_i(t):=c_i^2-a_i^2-4c_i t+4t^2+4c_i t^3-4t^4>=0
       for 0<=t<=1/sqrt(2).

Put s=R/|x-y| and assume 2s max_i a_i<1. Define

    I_(i,n)=int_0^(a_i) u^(2n)sqrt(a_i^2-u^2)/(c_i^2+2c_i u+a_i^2) du,
    H_(i,n)=2^(2n+2)(-binom(alpha,2n)) s^(2n) I_(i,n)/pi.

For every 0<alpha<1 and every positive integer N,

    |mu_R*f(x)-mu_R*f(y)|
       <= [1/2-sum_i sum_(n=1)^N H_(i,n)] |x-y|^alpha [f]_alpha.

For the retained-cutoff bound J_D at s=rho<1/2, replace each I_(i,n) by

    I_(i,n)-rho^2/(1-rho)^2 int_0^(a_i) u^(2n)sqrt(a_i^2-u^2) du.

These savings are simultaneous because their supporting disks are disjoint. A saving for a disk already included in this family cannot be added again. The theorem is conditional only on the explicit finite geometry inequalities above; no chosen numerical family is certified in this statement.

## Geometry

Scale R=1. Put a disk of radius a_i at each of plus and minus c_i on the negative kernel axis. The outer-circle condition and a_i<c_i/2 keep it inside the unit disk and the cone of half-angle pi/6. A boundary point of the inner lobe at angle theta from the axis is

    (2t(1-t^2), 2t^2 sqrt(1-t^2)), t=sin(theta).

Its squared distance from (c_i,0), less a_i^2, is exactly P_i(t). Thus the open disk does not meet the inner boundary. It is connected, contains its center in the lobe, and avoids the origin. It lies in the required lobe. Opposite disks are disjoint because c_i>a_i; same-axis disks have disjoint interiors by the pair condition. Boundaries have zero area and cause no issue.

## Couplings

The parent proof's local density calculation never uses c+a=1 until its numerical series specialization. For every disk here the density q_r(v) is decreasing and convex for r<=a_i<c_i/2. Its minimum with its reflection is a reflection-invariant subdensity. Pairing transverse angles proves that the moment saving for every orientation is at least the axis-parallel saving. Exact transverse integration gives I_(i,n), with the same factor for four quadrants and two disks as in the parent proof.

Use this reflection coupling on each disk and translation on the complement. Disjointness allows their costs to be added and preserves both marginals. Positivity of the even series proves the finite and infinite versions, with 2s max a_i<1 ensuring convergence. For the cutoff version, q_r(v)>=1/(c_i+r)^2>=1 because c_i+a_i<=1. Subtracting kappa=rho^2/(1-rho)^2<1 therefore leaves a positive retained subdensity. The same reflected-density argument applies.

## Exact finite verification of geometry

Each P_i is a rational polynomial if c_i,a_i are rational. To prove P_i>=0 on the larger rational interval [0,3/4], subdivide that interval into finitely many rational subintervals [l,l+h]. If P_i(l+hu)=sum_(j=0)^4 d_j u^j, its Bernstein coefficients of degree four are

    b_k=sum_(j=0)^k d_j binom(k,j)/binom(4,j), 0<=k<=4.

The Bernstein basis is nonnegative and sums to one on [0,1], so min_k b_k bounds P_i below on that subinterval. Nonnegative exact rational coefficients on every subinterval prove the required geometry without a floating-point minimum. The main nearly maximal disk may instead use the accepted quartic-root containment proof.

## Candidate, not yet certified

A candidate supplemental family is (41/100,3/40), (29/100,1/25), (9/40,3/125), (7/40,7/500). The main disk has the accepted rational c near 0.7430325154 and a=1-c. The candidate radii and all Bernstein conditions must be checked before any numerical saving is used. Status: OPEN pending independent cross-read and exact geometry verification.
