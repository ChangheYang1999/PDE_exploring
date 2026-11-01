# Finite continuum residuals of the single-harmonic tuned series

Status: the argument is written before the new interval evaluations. Admissions are recorded separately.

## Statement and hypotheses

Fix one of the unit-amplitude branches with (h,Q,M)=(2,5,7), (2,7,9), (2,9,11) or (3,13,17), delta=2h/Q, c=Q/(Q-2h), and leading density sin(M theta). Let f_n and g_n be its uniquely tuned exact coefficients. For each selected truncation N and positive rational radius R, the calculation below encloses the continuum angular supremum of the density-weighted stationary residual, its first two angular derivatives, the first omitted density term and its first two angular derivatives. It also encloses three weighted density partial sums.

The numerical conclusion assumes that the retained coefficient balls enclose f_n and the fully tuned g_n through N, and f_(N+1). Topic271 checks these hypotheses for each particular source file by the producer enclosure induction and independent finite checks. A final unresolved free stream harmonic is never used. This result concerns finite polynomials only. It neither proves nor refutes convergence of the infinite series at the tested radii.

## Derivation of the residual

Write z=R^(-delta), p_n=1-n delta and P_n=p_n+1. In the real antisymmetric Laurent representation of topic271, let X_q and Y_q be the Cartesian differentiation operators there. The physical sine field is -i times that representative, and physical partial_y is iY. Set

    A = sum_(n<=N) z^(n-1) X_(P_n) G_n,
    B = sum_(n<=N) z^(n-1) Y_(P_n) G_n,
    C = sum_(n<=N) z^(n-1) X_(p_n) F_n,
    D = sum_(n<=N) z^(n-1) Y_(p_n) F_n.

The weighted residual is represented by

    E = -(c-1) sum_(n<=N) (n-1) z^(n-1) F_n + z(AD-BC).

Indeed, the linear coefficient of r^(p_n) is cp_n-1=-(n-1)(c-1). Each ordered nonlinear pair has radial degree p_(i+j), and after division by R^(p_1) its factor is z^(i+j-1). The Cartesian product identity of topic271 gives the sign AD-BC. Expanding the finite products proves the displayed equality without assuming cancellation of the low-order terms. The first omitted weighted density term is z^N F_(N+1). The weighted partial sum is sum_(n<=N)z^(n-1)F_n.

## Continuum enclosure

For a sine polynomial H(theta)=sum_m a_m sin(m theta), define B_k=sum_m |a_m|m^(k+2). The second derivative of H^(k) is bounded by B_k. On each interval between grid points theta_j=j pi/L, the error of linear interpolation is at most pi^2 B_k/(8L^2). The absolute value of the interpolant is at most the larger endpoint magnitude. Therefore the largest rigorously evaluated sample lower bound is a lower bound for the continuum supremum; the largest sample upper bound plus this interpolation remainder is an upper bound. S1 symmetry extends the bound from [0,pi] to the full circle. For odd k the samples are cosine sums, and their common derivative sign has no effect on absolute values.

All finite operations use outward interval arithmetic. Interval evaluation of R^(-delta) is valid because R>0. Complex polynomial evaluation at exp(i theta_j) encloses each trigonometric sample. Dependency between input balls can enlarge the resulting enclosures but cannot remove the exact value. The full source checkpoint digest, the independent prefix archive in271, the precision and the grid size identify each calculation. The full producer checkpoint remains read-only in the numerical experiments; no second full copy is retained here. Strict separation of two supremum intervals certifies a finite increase or decrease. Agreement with a sampled binary64 value is recorded as such, never as a new convergence theorem.

## Dependencies and scope

The Laurent calculus and enclosure induction are in271. The residual identity is independently established in188 and196, and the interpolation proof is in162 and196. The present specialization changes the exact rational parameter and leading harmonic, not those arguments. Any conclusion about a sharp radius, an asymptotic growth constant or a global solution remains outside the scope of this result.
